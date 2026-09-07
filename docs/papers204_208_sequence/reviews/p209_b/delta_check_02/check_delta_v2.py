"""Same-B exact documentary delta evidence check, without science execution.

Uses only B's unchanged infrastructure primitives. No author/A/B verifier,
root inspector, root launcher or root recorder is imported or executed.
Every historical logical path/hash keeps an explicit physical resolution.
"""
import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import traceback

W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
Q=W/'docs/papers204_208_sequence/qa'
P=W/'papers/209-ordered-fibre-threading'
F=P/'frozen_round1'
PREP=Q/'p209_b_root_preparation'
PAIR=Q/'root_replays/p209_b_strict/root_b_pair_01'
LAUNCH=PAIR.parent/'launcher_root_b_pair_01'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
SEAL='d88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea'
INITIAL_DELTA='282dc2ab3f0021abeca145c20b76d0e0ef10e0b0e9948a173a24e6ead05b1400'
RESPONSE='c2cab3d26ddd9f5e5ba7e31dc0f3afa1c8d06510fd1276294cae33c63cdbc1f8'
spec=importlib.util.spec_from_file_location('unchanged_recording_primitives',B/'record_review.py')
rec=importlib.util.module_from_spec(spec);spec.loader.exec_module(rec)
READS={}
ALIASES={}
USED_ALIASES={}
COUNTS={}


def current(path):
    path=str(path)
    if path not in READS: READS[path]=rec.info(path)
    return READS[path]


def physical(origin,digest):
    key=(str(origin),digest)
    target=ALIASES.get(key,str(origin))
    got=current(target)
    assert got['sha256']==digest,('EXACT_HASH',str(origin),target,digest,got)
    if target!=str(origin):USED_ALIASES[str(origin)+' @ '+digest]=target
    return target


def alias(origin,digest,target):
    assert current(target)['sha256']==digest
    key=(str(origin),digest)
    ALIASES.setdefault(key,str(target))


def read(path):
    current(path)
    return Path(path).read_bytes()


def js(path): return json.loads(read(path))


def pinned(origin,info):
    assert 'error' not in info and {'sha256','bytes'}<=set(info)
    target=physical(origin,info['sha256']);got=current(target)
    assert got['bytes']==info['bytes']
    if target==str(origin):
        assert set(info)<=set(got) and all(got[k]==v for k,v in info.items()),('RECORDED_FIELD',origin)
    return target


def manifest(path,base=None,complete=False):
    path=Path(path);base=Path(base) if base is not None else path.parent
    rows={}
    for line in read(path).decode().splitlines():
        digest,name=line.split('  ',1);rel=Path(name)
        assert len(digest)==64 and set(digest)<=set('0123456789abcdef')
        assert not rel.is_absolute() and '..' not in rel.parts and rel.as_posix()==name
        assert name not in rows and base/rel!=path
        assert not (base/rel).is_symlink()
        physical(base/rel,digest);rows[name]=digest
    if complete:
        assert set(rows)=={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file() and p!=path}
    return rows


def pairmap(folder,before,after,count=None):
    values=js(folder/before)
    assert values==js(folder/after),('RECORDED_INTERVAL_DRIFT',str(folder),before)
    if count is not None:assert len(values)==count
    for path,info in values.items():pinned(path,info)
    return values


def commands(folder,count,exits):
    rows=js(folder/'ALL_COMMAND_RECORDS.json');assert len(rows)==count==len(exits)
    for entry,wanted in zip(rows,exits):
        where=Path(entry['folder']);tag=entry['tag'];row=entry['command']
        assert where.is_relative_to(folder)
        assert js(where/(tag+'.command.json'))==row
        attempt=js(where/(tag+'.attempt.json'))
        assert all(attempt[k]==row[k] for k in ('argv','cwd','env','stdout','stderr'))
        assert row['exit']==wanted and row['process_outcome']=='COMPLETED'
        assert row['spawn_error'] is None and row['cleanup']==[] and row['env']==ENV
        for name in ('stdout','stderr'):pinned(where/row[name],row[name+'_info'])
        samples=js(where/(tag+'.maps.json'))
        assert sorted({p for sample in samples['samples'] for p in sample['mapped_files']})==entry['mapped_files']
    return rows


def settings(obs,folder,parent=False):
    assert obs['env']==ENV and obs['cwd']==str(W if parent else folder)
    assert not obs['cache_exists']
    if parent:
        assert obs['optimization']==0
        assert all(x in obs['flags'] for x in ('isolated=1','no_site=1','dont_write_bytecode=1','optimize=0'))
        cache=folder/'never_created_parent_cache'
    else:
        assert obs['optimize']==0 and obs['isolated']==obs['no_site']==1 and obs['dont_write_bytecode']
        cache=folder/'never_created_child_cache'
    assert obs['pycache_prefix']==str(cache) and not cache.exists()


def configuration():
    result={}
    for folder in (B/'review_pair_01',B/'review_build_01',PAIR):
        old=js(folder/'CONFIGURATION_BEFORE.json');assert old==js(folder/'CONFIGURATION_AFTER.json')
        now=rec.presence([Path(p) for p in old['optional']],[Path(p) for p in old['directories']])
        assert now==old,('CONFIGURATION_RECAPTURE',str(folder))
        result[str(folder)]=now
        for p,v in old['optional'].items():
            if v['is_file']:physical(p,v['sha256'])
        for names in old['directories'].values():
            for p in names or []:current(p)
    # Reenumerate the declared runtime file sets, not only known old hashes.
    for mode,folder in [('pair',PAIR),('build',B/'review_build_01')]:
        old=js(folder/'RUNTIME_BEFORE.json');assert old==js(folder/'RUNTIME_AFTER.json')
        now,optional,dirs,config=rec.runtime(mode)
        external={p:v for p,v in now.items() if not Path(p).is_relative_to(W)}
        oldexternal={p:v for p,v in old.items() if not Path(p).is_relative_to(W)}
        assert external==oldexternal,('RUNTIME_RECAPTURE',mode)
        result['runtime_'+mode]={'count':len(external),'original_map_sha256':current(folder/'RUNTIME_BEFORE.json')['sha256']}
        for p,v in external.items():pinned(p,v)
    build=B/'review_build_01'
    tex=js(build/'TEX_RESOURCES_BEFORE.json');assert tex==js(build/'TEX_RESOURCES_AFTER.json')
    assert len(tex['files'])==113733
    assert {str(p) for root in tex['roots'] if Path(root).is_dir() for p in Path(root).rglob('*') if p.is_file()}==set(tex['files'])
    assert all(Path(p).exists()==v for p,v in tex['roots'].items())
    for p,v in tex['files'].items():pinned(p,v)
    roots=js(build/'USER_ROOTS_BEFORE.json');assert roots==js(build/'USER_ROOTS_AFTER.json')
    assert all(not v['exists'] and not Path(v['path']).exists() for v in roots.values())
    result['tex']={'roots':tex['roots'],'file_count':113733,'original_map_sha256':current(build/'TEX_RESOURCES_BEFORE.json')['sha256'],'user_roots':roots}
    return result


def root_result(name):
    raw=js(Q/name)
    if 'parsed_stdout' in raw:
        assert raw['actual_completion']['exit_code']==0
        return raw['parsed_stdout']
    assert raw['completion']['exit_code']==0
    return json.loads(raw['completion']['output'])


def main():
    out=Path(sys.argv[1]);assert out==B/'delta_check_02'
    assert sys.flags.isolated and sys.flags.no_site and sys.flags.optimize==0 and sys.dont_write_bytecode
    assert dict(os.environ)==ENV and not Path(sys.pycache_prefix).exists()
    for name in ('check_delta_v2.py','launch_delta_v2.py','record_review.py'):current(B/name)
    prior_aliases=js(B/'artifact_audit_03/EXACT_HISTORICAL_RESOLUTION.json');assert len(prior_aliases)==13
    for key,target in prior_aliases.items():
        origin,digest=key.rsplit(' @ ',1);alias(origin,digest,target)
    alias(B/'SHA256SUMS',SEAL,B/'INITIAL_REVIEW_SEAL.sha256')
    alias(B/'DELTA.md',INITIAL_DELTA,B/'INITIAL_DELTA.md')
    intake=js(B/'delta_intake_01/INTAKE_RESULT.json')
    assert intake['status']=='PASS_EXACT_INITIAL_PRESERVATION_AND_INTAKE'
    assert not intake['acceptance_performed'] and intake['initial_payloads_checked']==1298
    for item in intake['copies']:
        alias(item['original'],item['sha256'],item['physical'])
        if item['original'] not in {str(W/'SYMBOLIC_DYNAMICS_STATE.md'),str(W/'docs/papers204_208_sequence/PIPELINE_STATE.md')}:
            assert current(item['original'])['sha256']==item['sha256']
    manifest(B/'delta_check_01/SHA256SUMS',complete=True)
    prior_failure=js(B/'delta_check_01/CLOSURE_AFTER_FAILURE.json')
    assert prior_failure['status']=='FAIL_PRESERVED_OUTER_WRAPPER_FILENAME_COLLISION'
    assert prior_failure['actual_outer_exit']==1 and prior_failure['actual_child_exit']==0
    COUNTS['preserved_failed_delta_wrappers']=1
    # Preserve current response-bound lifecycle/rollup bytes for later changes.
    anchors=out/'response_anchors';anchors.mkdir()
    for name,digest in [('PAPER_MANIFEST.sha256','3e94a72637733ca46f7950f4feb8508fdf14b5ff6386c971821932ae9231e5a9'),
                        ('ROOT_ADOPTION.md','8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e'),
                        ('PAPER_STATUS.md','304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73')]:
        assert rec.info(P/name)['sha256']==digest
        shutil.copyfile(P/name,anchors/name)
        assert rec.info(P/name)['sha256']==digest and read(anchors/name)==(P/name).read_bytes()
        alias(P/name,digest,anchors/name)
    response=physical(W/'docs/papers204_208_sequence/P209_B_RESPONSE.md',RESPONSE)
    read(response)
    assert len(manifest(B/'INITIAL_REVIEW_SEAL.sha256',B))==1298
    initial=manifest(B/'INITIAL_REVIEW_SEAL.sha256',B)
    assert initial['REPORT.md']=='089f10c004f933f17db0a701e161b5d19edb3c74f9c3896348fad5711f109f12'
    assert initial['FINDINGS.json']=='395340caae7a758f1791b71f684c8c11fb82ccbfa383d98c83141b9e8cf74e17'
    assert initial['DELTA.md']==INITIAL_DELTA
    COUNTS.update(initial_payloads=1298,initial_same_path_payloads=1297,initial_delta_aliases=1)
    for name,row in js(B/'PRESEAL_CHECK.json')['nested_seals'].items():
        assert current(B/name/'SHA256SUMS')['sha256']==row['sha256']
        assert len(manifest(B/name/'SHA256SUMS',complete=True))==row['payloads']
    assert len(manifest(B/'delta_intake_01/SHA256SUMS',complete=True))==29
    old_dependencies=pairmap(B/'artifact_audit_03','DOCUMENTARY_INPUTS_BEFORE.json','DOCUMENTARY_INPUTS_AFTER.json',127544)
    COUNTS['all_original_documentary_pins_retained']=len(old_dependencies)
    assert len(manifest(F/'SHA256SUMS',complete=True))==2003
    assert current(F/'SHA256SUMS')['sha256']=='c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
    assert len(manifest(B/'INPUT_PINS.sha256',W))==2004
    author=manifest(P/'AUTHOR_MANIFEST.sha256');assert len(author)==1985
    assert author==manifest(F/'AUTHOR_MANIFEST.sha256')
    assert current(P/'AUTHOR_MANIFEST.sha256')['sha256']=='9fd20cd746f1ae03c22a87283313248ad79ffcfb9a0f1ea45458937dd5901a0e'
    whole=manifest(anchors/'PAPER_MANIFEST.sha256',P)
    assert len(whole)==5982
    assert set(whole)=={p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file() and p!=P/'PAPER_MANIFEST.sha256'}
    COUNTS.update(author_payloads=1985,round1_payloads=2003,frozen_inputs=2004,current_whole_paper_referents=5982)
    for base,digest,count in [(PREP,'4beef4a4e9f60c6039ceb89df1f3a12b2d61049ad75654e35825390c4b68133a',57),
                              (PAIR,'51dd81f7c6dac413612ef57437dde389c3b20a44e94412dd7bee008a77c9c841',462),
                              (LAUNCH,'7874f814ce0cf9177b417ae1d1b1e10f233f51fd92c3826d5753f388ed994eed',10)]:
        assert current(base/'SHA256SUMS')['sha256']==digest
        assert len(manifest(base/'SHA256SUMS',complete=True))==count
    for m in PAIR.parent.rglob('SHA256SUMS'):manifest(m,complete=True)
    fixed=js(PREP/'FIXED_INPUTS.json');assert len(fixed)==2021
    assert current(PREP/'FIXED_INPUTS.json')['sha256']=='09a5033597e9b218296f624c256fe2d370331e08269bf1fcc2928352104fb7c8'
    for p,v in fixed.items():pinned(p,v)
    for name in ('verify.py','bootstrap.py','record_review.py','launch_review.py','PARAMETERS.json'):
        assert read(PREP/'original_snapshot'/name)==read(B/name)
    # Recheck unchanged machinery directly from source AST and exact blocks.
    for old,new,allowed in [('record_review.py','root_record_pair.py',{'science','pair','main'}),
                            ('launch_review.py','root_launch_pair.py',{'check_closed_recorder','main'})]:
        a=read(B/old).decode();b=read(PREP/new).decode()
        aa={x.name:x for x in ast.parse(a).body if isinstance(x,ast.FunctionDef)}
        bb={x.name:x for x in ast.parse(b).body if isinstance(x,ast.FunctionDef)}
        assert aa.keys()==bb.keys()
        assert {n for n in aa if ast.dump(aa[n])!=ast.dump(bb[n])}==allowed
        assert all(ast.get_source_segment(a,aa[n])==ast.get_source_segment(b,bb[n]) for n in aa.keys()-allowed)
    inputs=pairmap(PAIR,'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json','ALL_INPUTS_AFTER.json',5164)
    runtime=pairmap(PAIR,'RUNTIME_BEFORE.json','RUNTIME_AFTER.json',3133)
    assert all(inputs[p]==v for p,v in runtime.items())
    science=js(PAIR/'SCIENCE_BEFORE.json');assert len(science)==2025
    assert all(inputs[p]==v for p,v in science.items())
    r=js(PAIR/'RECEIPT.json');assert r['status']=='PASS_ROOT_REVIEW_B_PAIR' and not r['failures']
    assert r['result']['canonical_adopted'] is False
    rows=commands(PAIR,85,[0]*85);assert sum(e['tag'].startswith('ldd_') for e in rows)==80
    covered={v['resolved'] for v in inputs.values()}
    assert all(set(e['mapped_files'])<=covered for e in rows)
    link=js(PAIR/'LINKAGE.json');assert not link['pending_targets'] and len(link['entries'])==80
    assert all(e['status']=='VALIDATED' for e in link['entries'])
    closed=js(PAIR/'OBSERVED_CLOSURE.json');assert closed['uncovered']==closed['bytecode']==[]
    for phase in ('BEFORE','AFTER'):settings(js(PAIR/('PARENT_'+phase+'.json')),PAIR,True)
    for label in ('replay_01','replay_02'):
        folder=PAIR/label;child=js(folder/'RECEIPT.json')
        assert child['status']=='PASS' and child['failure'] is None and child['inputs_unchanged']
        assert child['checks']==54794 and child['total_states']==3414
        assert child['source_only_initial_names']==['bootstrap.py','verify.py']
        assert child['closure']['uncovered']==child['closure']['bytecode']==[]
        for name in child['source_only_initial_names']:assert read(folder/'source_inputs'/name)==read(B/name)
        pairmap(folder,'INPUTS_BEFORE.json','INPUTS_AFTER.json')
        for phase in ('before','after'):
            obs=js(folder/('child.'+phase+'.json'));settings(obs,folder)
            assert obs['orig_argv']==child['command']['argv']
        data=js(folder/'producer.stdout')
        assert data['schema']=='p209-b-ports-constructive-carrier-v1' and data['status']=='PASS'
        assert (data['checks'],data['states'],data['max_n'])==(54794,3414,5)
        assert [box['n'] for box in data['boxes']]==list(range(6))
        assert all(len(box['rows'])==box['states'] for box in data['boxes'])
    launch=js(LAUNCH/'RECEIPT.json')
    assert launch['status']=='PASS_ROOT_LAUNCH' and launch['exit']==0 and launch['outcome']=='COMPLETED'
    assert launch['failure'] is None and launch['inputs_unchanged'] and launch['cache_absent']
    assert launch['env']==ENV and launch['cwd']==str(W) and not Path(launch['launcher_cache']).exists()
    assert all(flag in launch['launcher_flags'] for flag in ('isolated=1','no_site=1','dont_write_bytecode=1','optimize=0'))
    pairmap(LAUNCH,'INPUTS_BEFORE.json','INPUTS_AFTER.json',2026)
    for name in ('recorder.stdout','recorder.stderr'):pinned(LAUNCH/name,launch[name+'_pin'])
    assert launch['recorder_closure']['payloads']==462 and launch['recorder_closure']['status']==r['status']
    pinned(PAIR/'SHA256SUMS',launch['recorder_seal'])
    assert js(LAUNCH/'recorder.stdout')['status']==r['status']
    assert read(PAIR/'executed_recorder.py')==read(PREP/'root_record_pair.py')
    pairmap(PAIR/'comparison','INPUTS_BEFORE.json','INPUTS_AFTER.json')
    COUNTS.update(root_fixed_inputs=2021,root_pair_inputs=5164,root_runtime_inputs=3133,root_pair_payloads=462,root_launcher_payloads=10,root_commands=85)
    initial_root=root_result('P209_B_ROOT_INITIAL_INSPECTION.actual.json')
    assert initial_root['status']=='PASS_ROOT_B_INITIAL_COMPLETE_ORIGINAL_CLOSURE'
    assert initial_root['review_payloads']==1298 and initial_root['full_documentary_inputs']==127544
    assert initial_root['all_current_read_paths_checked_twice']==127591
    assert {e['original_path']+' @ '+e['sha256']:e['physical_path'] for e in initial_root['actual_resolved_historical_aliases']}==prior_aliases
    prep_root=root_result('P209_B_ROOT_PAIR_PREPARATION.actual.json')
    assert prep_root['status']=='PASS_ROOT_B_PAIR_PREPARATION' and prep_root['fixed_inputs']==2021
    assert [e['exit'] for e in prep_root['actual_commands']]==[0,0,0,0,0,1,1]
    assert ''.join(e['stdout'] for e in prep_root['actual_commands'][-2:]).encode()==read(PREP/'ADAPTATION.diff')
    execution=root_result('P209_B_ROOT_PAIR_EXECUTION.actual.json');assert execution['status']=='PASS_ROOT_LAUNCH' and execution['exit']==0
    closure=root_result('P209_B_ROOT_PAIR_INSPECTION.actual.json')
    assert closure['status']=='PASS_ROOT_NEW_B_PAIR_FULL_CLOSURE' and closure['all_current_paths_twice']==6970
    exact=root_result('P209_B_EXACT_NOCHANGE_CHECK.actual.json')
    assert exact['status']=='PASS_EXACT_B_NOCHANGE_BEFORE_RESPONSE' and exact['all_current_paths_twice']==7282
    for p,v in exact['anchors'].items():pinned(W/p,v)
    for name in ('inspect_p209_a_initial.py','inspect_p209_b_initial.py','inspect_p209_b_root_pair.py'):read(Q/name)
    for record,key in [(initial_root,'actual_root_raw_comparisons'),(closure,'actual_new_root_raw_comparisons'),(exact,'actual_raw_comparisons')]:
        assert all(e['exit']==0 and e['stdout']==e['stderr']=='' for e in record[key])
    cfg_before=configuration()
    pairs=[(PAIR/'replay_01/producer.stdout',PAIR/'replay_02/producer.stdout'),
           (PAIR/'replay_01/producer.stdout',B/'CANONICAL.json'),(PAIR/'replay_02/producer.stdout',B/'CANONICAL.json'),
           (P/'main.pdf',F/'main.pdf'),(P/'verify.py',F/'verify.py'),(P/'CANONICAL.json',F/'CANONICAL.json'),
           (P/'AUTHOR_MANIFEST.sha256',F/'AUTHOR_MANIFEST.sha256'),
           (W/'docs/papers204_208_sequence/P209_B_RESPONSE.md',Path(response))]
    # These command inputs are immutable science/response, never current delta or outer seal.
    for a,b in pairs:current(a);current(b)
    rec.save(out/'EXACT_HISTORY_ALIASES.json',{p+' @ '+h:t for (p,h),t in sorted(ALIASES.items())})
    rec.save(out/'USED_HISTORY_ALIASES.json',USED_ALIASES)
    before=dict(READS);rec.save(out/'INPUTS_FULL_BEFORE.json',before)
    rec.save(out/'CONFIGURATION_BEFORE.json',cfg_before)
    problem=None
    try:
        for index,(a,b) in enumerate(pairs,1):rec.command(['/usr/bin/cmp','--',str(a),str(b)],W,out,'raw_cmp_'+str(index).zfill(2),ENV)
        cfg_after=configuration();assert cfg_after==cfg_before
        rec.save(out/'CONFIGURATION_AFTER.json',cfg_after)
    except BaseException:
        problem=traceback.format_exc()
    rec.save(out/'ALL_COMMAND_RECORDS.json',rec.COMMAND_RECORDS)
    assert set(READS)==set(before),'LATE_UNPINNED_DELTA_INPUT'
    after=rec.pins(before);rec.save(out/'INPUTS_FULL_AFTER.json',after)
    assert before==after,'DELTA_INPUTS_CHANGED'
    assert problem is None,problem
    assert not rec.UNREAPED_CHILDREN
    result={'status':'PASS_EXACT_NOCHANGE_DELTA_EVIDENCE','reviewer':'/root/p209_b_reviewer',
            'response_sha256':RESPONSE,'initial_seal_sha256':SEAL,'initial_delta_sha256':INITIAL_DELTA,
            'counts':COUNTS,'delta_full_input_paths':len(before),'all_inputs_unchanged':True,
            'prior_aliases_retained':13,'declared_aliases':len(ALIASES),'used_aliases':len(USED_ALIASES),
            'actual_raw_comparisons':len(rec.COMMAND_RECORDS),'new_delta_mathematical_producers':0,
            'new_delta_builds_renders_views':0,'initial_report_and_census_unchanged':True,
            'accepted_decision_not_written_by_checker':True,
            'limit':'Exact historical roles and unchanged complete keys; no new mathematical execution or visual inspection, no continuous/startup/grandchild trace or OS-hermeticity.',
            'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    rec.save(out/'DELTA_EVIDENCE_RESULT.json',result)
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':main()
