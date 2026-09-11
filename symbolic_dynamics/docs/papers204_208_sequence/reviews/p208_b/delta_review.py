"""B's documentary-only delta: exact historical mapping and dependency audit.

No scientific implementation is executed or imported. Existing review,
producer, runtime and build receipts remain byte-identical. Only current
FINDINGS and the outer manifest may replace their archived initial bytes.
"""
from pathlib import Path
import hashlib
import json
import os
import sys
import time

BASE=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p208_b')
ROOT=BASE.parents[3]
BATCH=ROOT/'docs/papers204_208_sequence'
PAPER=ROOT/'papers/208-original-snapshot-triangulation-sweeps'
STRICT=BATCH/'qa/root_replays/p208_b_strict'
OUT=BASE/'delta'
INITIAL='64a58b80ac92f98caff178a34a8ef6199c83eace414c043d72d4ce81eeff78a5'
ROOT_SEAL='59934004f5974b8d2978268bd86c5441bdefc889ae02272630824da8ed068bbc'
CHECKS=0
def check(x,label):
    global CHECKS
    CHECKS+=1
    if not x:raise AssertionError(label)
def raw(p):return Path(p).read_bytes()
def sha(p):return hashlib.sha256(raw(p)).hexdigest()
def load(p):return json.loads(raw(p))
def dump(p,obj):
    Path(p).parent.mkdir(parents=True,exist_ok=True)
    with Path(p).open('x') as f:json.dump(obj,f,indent=2,sort_keys=True);f.write('\n')
def snapshot(src,dst,digest=None):
    b=raw(src);h=hashlib.sha256(b).hexdigest()
    if digest is not None:check(h==digest,('snapshot source',str(src)))
    Path(dst).parent.mkdir(parents=True,exist_ok=True)
    with Path(dst).open('xb') as f:f.write(b)
    check(h==sha(src)==sha(dst),('snapshot stable',str(src)))
    return h
def manifest_rows(path):
    rows={}
    for line in Path(path).read_text().splitlines():
        h,rel=line.split('  ',1);p=Path(rel)
        check(not p.is_absolute() and '..' not in p.parts and rel not in rows,'safe unique manifest path')
        rows[rel]=h
    return rows
def digest(value):return value if isinstance(value,str) else value['sha256']
def response_files():
    names=['P208_B_RESPONSE.md','qa/P208_B_ROOT_INSPECTION.md',
       'qa/P208_B_ROOT_ARTIFACT_INSPECTION.actual.json',
       'qa/P208_B_ROOT_PAYLOAD_INSPECTION.actual.json',
       'qa/P208_B_ROOT_ORIGINAL_INSPECTION.actual.json','qa/replay_p208_b_strict.py']
    return [BATCH/n for n in names]+sorted(p for p in STRICT.rglob('*') if p.is_file())
def runtime():
    r={'version':sys.version,'flags':repr(sys.flags),'executable':sys.executable,
       'path':sys.path,'environment':dict(os.environ),'pycache_prefix':sys.pycache_prefix,
       'modules':{}}
    for name,m in sorted(sys.modules.items()):
        p=getattr(m,'__file__',None);spec=getattr(m,'__spec__',None)
        r['modules'][name]={'file':p,'origin':getattr(spec,'origin',None),
          'loader':type(getattr(spec,'loader',None)).__name__,
          'sha256':sha(p) if p and Path(p).is_file() else None}
    txt=Path('/proc/self/maps').read_text();r['maps_raw']=txt
    r['mapped_files']={p:sha(p) for p in sorted(set(line.split(None,5)[5]
       for line in txt.splitlines() if len(line.split(None,5))==6 and line.split(None,5)[5].startswith('/')))}
    return r
def config_current(records):
    out={}
    for name,rows in records.items():
        current={}
        for p,row in rows.items():
            q=Path(p);v={'exists':q.exists()}
            if 'resolved' in row:v['resolved']=str(q.resolve())
            if 'sha256' in row:v['sha256']=sha(q) if q.is_file() else None
            if 'bytes' in row:v['bytes']=q.stat().st_size if q.is_file() else None
            current[p]=v
        out[name]=current
    return out
def prepare():
    check(sha(BASE/'SHA256SUMS')==INITIAL,'exact initial seal before modifications')
    initial=manifest_rows(BASE/'SHA256SUMS');check(len(initial)==1546,'initial payload count')
    for rel,h in initial.items():check(sha(BASE/rel)==h,('entire initial payload',rel))
    OUT.mkdir(exist_ok=False)
    snapshot(BASE/'SHA256SUMS',OUT/'initial_snapshot/SHA256SUMS',INITIAL)
    snapshot(BASE/'FINDINGS.json',OUT/'initial_snapshot/FINDINGS.json',initial['FINDINGS.json'])
    mapping={rel:{'sha256':h,'historical_path':('delta/initial_snapshot/FINDINGS.json' if rel=='FINDINGS.json' else rel)}
             for rel,h in initial.items()}
    dump(OUT/'INITIAL_PAYLOAD_MAPPING.json',mapping)
    history=load(BASE/'history_context/SEARCH_INPUTS_BEFORE.json')
    check(history==load(BASE/'history_context/SEARCH_INPUTS_AFTER.json') and len(history)==1917,'initial complete search input set')
    history_map={};origins={}
    for rel,h in sorted(history.items()):
        original=ROOT/rel;oldcopy=BASE/'history_context/snapshots'/rel
        if oldcopy.is_file() and sha(oldcopy)==h:chosen=oldcopy
        else:
            check(original.is_file() and sha(original)==h,('no matching historical bytes available',rel))
            chosen=original
        target=OUT/'history_inputs'/rel
        snapshot(chosen,target,h)
        history_map[str(original)]={'sha256':h,'historical_path':str(target.relative_to(BASE)),
            'source_at_archiving':str(chosen),'role':'exact original search bytes, not fresh current-source absence evidence'}
        origins[str(original)]={'exists':original.exists(),'sha256':sha(original) if original.is_file() else None,
                                'matches_initial_search':original.is_file() and sha(original)==h}
    dump(OUT/'HISTORY_INPUT_MAPPING.json',history_map)
    dump(OUT/'HISTORY_ORIGINALS_AT_ARCHIVE.json',origins)
    response={}
    for p in response_files():
        target=OUT/'root_context'/p.relative_to(ROOT)
        h=snapshot(p,target)
        response[str(p)]={'sha256':h,'snapshot':str(target.relative_to(BASE))}
    dump(OUT/'ROOT_RESPONSE_PINS_BEFORE.json',response)
    refs={}
    def add(p,h):
        p=str(Path(p));h=digest(h)
        if p in refs:check(refs[p]['sha256']==h,('conflicting dependency digest',p))
        if p==str(BASE/'SHA256SUMS'):resolved=OUT/'initial_snapshot/SHA256SUMS'
        elif p==str(BASE/'FINDINGS.json'):resolved=OUT/'initial_snapshot/FINDINGS.json'
        elif p in history_map:
            check(history_map[p]['sha256']==h,('history dependency version mismatch',p))
            resolved=BASE/history_map[p]['historical_path']
        else:resolved=Path(p)
        check(sha(resolved)==h,('complete dependency baseline',p))
        refs[p]={'sha256':h,'validated_path':str(resolved),
                 'role':'historical_exact_bytes' if str(resolved)!=p else 'unchanged_live_dependency'}
    for rel,h in initial.items():add(BASE/rel,h)
    add(BASE/'SHA256SUMS',INITIAL)
    for p,row in response.items():add(p,row['sha256']);add(BASE/row['snapshot'],row['sha256'])
    for freeze in ('frozen_round0','frozen_round1'):
        for rel,h in manifest_rows(PAPER/freeze/'SHA256SUMS').items():add(PAPER/freeze/rel,h);add(PAPER/rel,h)
        add(PAPER/freeze/'SHA256SUMS',sha(PAPER/freeze/'SHA256SUMS'))
    for directory,stems in [(BASE/'final_pair',['INPUTS']),
        (BASE/'source_build',['INPUTS','TOOLS','LIBRARIES','TEX_INVENTORY','CONFIG']),
        (STRICT,['INPUTS','RUNTIME_INVENTORY','LIBRARIES'])]:
        for stem in stems:
            before=load(directory/(stem+'_BEFORE.json'));after=load(directory/(stem+'_AFTER.json'))
            check(before==after,('previous actual unchanged inventory',str(directory),stem))
            for p,h in before.items():add(p,h)
    for p,row in load(BASE/'SOURCE_CONTEXT_PINS.json')['paths'].items():
        add(p,row['sha256']);add(BASE/row['snapshot'],row['sha256'])
    for p,row in history_map.items():add(p,row['sha256']);add(BASE/row['historical_path'],row['sha256'])
    for p in (Path(__file__),BASE/'delta_record.py'):add(p,sha(p))
    rt=runtime();dump(OUT/'PREPARER_RUNTIME.json',rt)
    for p,h in rt['mapped_files'].items():add(p,h)
    for row in rt['modules'].values():
        if row['sha256']:add(row['file'],row['sha256'])
    configs={str(BASE/'final_pair/CONFIG_BEFORE.json'):load(BASE/'final_pair/CONFIG_BEFORE.json'),
        str(BASE/'source_build/CONFIG_ABSENCE_BEFORE.json'):load(BASE/'source_build/CONFIG_ABSENCE_BEFORE.json'),
        str(STRICT/'CONFIGURATION_BEFORE.json'):load(STRICT/'CONFIGURATION_BEFORE.json')}
    check(config_current(configs)==configs,'complete current runtime/build configuration')
    dump(OUT/'CONFIGURATION_BEFORE.json',configs)
    dump(OUT/'INPUTS_BEFORE.json',refs)
    receipt={'status':'PASS_PREPARED_DOCUMENTARY_DELTA','checks':CHECKS,'baseline_paths':len(refs),
      'root_response_paths':len(response),'initial_payloads':len(initial),'history_inputs_archived':len(history_map),
      'history_originals_currently_matching':sum(r['matches_initial_search'] for r in origins.values()),
      'initial_manifest_sha256':INITIAL,'initial_findings_sha256':initial['FINDINGS.json'],
      'science_executed':False,'manuscript_changed':False,'utc':time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime())}
    dump(OUT/'PREPARE_RECEIPT.json',receipt);return receipt
def check_manifest(directory,filename='SHA256SUMS',expected_count=None,expected_sha=None):
    p=directory/filename
    if expected_sha:check(sha(p)==expected_sha,('manifest identity',str(p)))
    rows=manifest_rows(p)
    if expected_count is not None:check(len(rows)==expected_count,('manifest count',str(p)))
    for rel,h in rows.items():check(sha(directory/rel)==h,('manifest referent',str(p),rel))
    actual={str(q.relative_to(directory)) for q in directory.rglob('*') if q.is_file() and q!=p}
    check(set(rows)==actual,('complete nonself manifest',str(p)))
    return rows
def stream_commands(directory):
    count=0
    for p in sorted(directory.glob('*.command.json')):
        r=load(p);check(r['exit_code']==0,('recorded actual exit',str(p)));count+=1
        prefix=p.name[:-len('.command.json')]
        for stream in ('stdout','stderr'):
            if stream+'_sha256' in r:check(sha(directory/(prefix+'.'+stream))==r[stream+'_sha256'],('actual stream',str(p),stream))
            elif isinstance(r.get(stream),dict):check(sha(directory/r[stream]['path'])==r[stream]['sha256'],('actual root stream',str(p),stream))
    return count
def audit(label):
    check(label in ('audit01','audit02'),'bounded delta audit phase')
    run=OUT/label
    # Launcher creates this exclusive directory before child execution.
    rt_before=runtime();dump(run/'RUNTIME_BEFORE.json',rt_before)
    baseline=load(OUT/'INPUTS_BEFORE.json');observed={}
    for p,row in baseline.items():
        h=sha(row['validated_path']);check(h==row['sha256'],('unchanged complete dependency',p))
        observed[p]={**row,'sha256':h}
    dump(run/'INPUTS_AFTER.json',observed);check(observed==baseline,'full beforeafter equality through exact historical mapping')
    cfg=load(OUT/'CONFIGURATION_BEFORE.json');aftercfg=config_current(cfg)
    dump(run/'CONFIGURATION_AFTER.json',aftercfg);check(cfg==aftercfg,'all configuration presence/absence unchanged')
    response=load(OUT/'ROOT_RESPONSE_PINS_BEFORE.json');after_response={}
    for p,row in response.items():
        check(sha(p)==row['sha256']==sha(BASE/row['snapshot']),('exact response original and snapshot',p))
        after_response[p]=row
    dump(run/'ROOT_RESPONSE_PINS_AFTER.json',after_response)
    mapping=load(OUT/'INITIAL_PAYLOAD_MAPPING.json');check(len(mapping)==1546,'all initial payloads mapped')
    initial=manifest_rows(OUT/'initial_snapshot/SHA256SUMS')
    check(sha(OUT/'initial_snapshot/SHA256SUMS')==INITIAL and set(initial)==set(mapping),'exact initial manifest bytes')
    for rel,row in mapping.items():check(sha(BASE/row['historical_path'])==row['sha256']==initial[rel],('every initial payload retained',rel))
    history=load(OUT/'HISTORY_INPUT_MAPPING.json')
    expected=load(BASE/'history_context/SEARCH_INPUTS_BEFORE.json')
    check(len(history)==1917 and set(history)=={str(ROOT/p) for p in expected},'complete historical search mapping')
    for p,row in history.items():check(sha(BASE/row['historical_path'])==row['sha256']==expected[str(Path(p).relative_to(ROOT))],('exact archived search bytes',p))
    check_manifest(STRICT,expected_count=38,expected_sha=ROOT_SEAL)
    root_receipt=load(STRICT/'RECEIPT.json')
    check(root_receipt['status']=='PASS_ROOT_P208_B_STRICT_PAIR' and not root_receipt['failures'],'actual root pair status')
    check(root_receipt['inputs']==3037 and root_receipt['runtime_inventory']==918 and root_receipt['library_files']==112 and root_receipt['configuration_entries']==33,'root exact coverage counts')
    check(len(root_receipt['commands'])==7 and all(c['exit_code']==0 for c in root_receipt['commands']),'root seven actual exits')
    canonical=sha(BASE/'CANONICAL.json')
    check(canonical=='f809344b8692df7883109000b9914f441f7260739241e7f486547aea15335d07','unchanged B canonical')
    for number in (1,2):
        check(sha(STRICT/f'run{number}.stdout')==canonical,'root actual canonical bytes')
        check(raw(STRICT/f'run{number}.stderr')==b'','root producer empty stderr')
        report=load(STRICT/f'run{number}_CONSUMED_RUNTIME.json')
        check(report['optimize']==0 and report['isolated']==report['no_site']==1 and report['dont_write_bytecode'],'actual root producer flags')
        check(report['cache_absent'] and not Path(report['pycache_prefix']).exists(),'root no cached bytecode')
        modules=load(STRICT/'RUNTIME_INVENTORY_BEFORE.json');libs=load(STRICT/'LIBRARIES_BEFORE.json')
        for row in report['modules'].values():
            if 'path' in row:check(digest(modules[row['path']])==row['sha256']==sha(row['path']),'every actual root module')
        for p,h in report['mapped_files'].items():check(digest({**modules,**libs}[p])==h==sha(p),'every actual root mapped file')
        check(sha(BASE/'final_pair'/f'run_{number}.stdout')==canonical,'actual B final output unchanged')
    counts={}
    for directory in (STRICT,BASE/'final_pair',BASE/'source_build',BASE/'payload_comparison',BASE/'package_audit'):
        counts[str(directory.relative_to(ROOT))]=stream_commands(directory)
    artifact=load(BATCH/'qa/P208_B_ROOT_ARTIFACT_INSPECTION.actual.json')
    payload=load(BATCH/'qa/P208_B_ROOT_PAYLOAD_INSPECTION.actual.json')
    root_check=load(BATCH/'qa/P208_B_ROOT_ORIGINAL_INSPECTION.actual.json')
    check(artifact['status']=='PASS' and artifact['checks']==118278,'actual root final artifact audit')
    check(payload['status']=='PASS' and payload['checks']==266834 and payload['before']==payload['after'],'actual complete scientific data audit')
    check(root_check['status']=='ROOT_P208_B_ORIGINAL_AND_STRICT_CLOSURE_PASS' and len(root_check['fresh_raw_comparisons'])==7,'actual root original closure')
    check(all(c['exit_code']==0 and c['stdout']==c['stderr']=='' for c in root_check['fresh_raw_comparisons']),'actual seven root raw comparisons')
    for row in payload['before'].values():check(sha(row['path'])==row['sha256'],'unchanged all author/A/B canonical payloads')
    b=BASE/'source_build';br=load(b/'RECEIPT.json')
    check(br['pages']==7 and br['embedded_fonts']==27 and br['all_command_exits_zero'],'original build and viewed PDF reused')
    check(sha(b/'source_only/main.pdf')==sha(PAPER/'frozen_round1/main.pdf')==br['pdf_sha256'],'identical actually viewed PDF bytes')
    check(br['warnings']['underfull']==['Underfull \\hbox (badness 5681) in paragraph at lines 9--13'],'real underfull diagnostic retained')
    sources=load(b/'SOURCE_ONLY_INITIAL.json');check(len(sources)==11,'source-only initial build')
    for p,h in sources.items():check(sha(b/'source_only'/p)==h,'exact original TeX source')
    # Recapture the complete resource roots from the unchanged build recorder's
    # literal constants via AST, without executing that recorder or a build.
    import ast
    tree=ast.parse((BASE/'record_build.py').read_text())
    literals={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign)
      and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('TEX_ROOTS','CONFIG_ROOTS','CONFIG_EXPLICIT')}
    def inventory(roots):
        return {str(p.resolve()):sha(p) for name in roots if Path(name).exists() for p in Path(name).rglob('*') if p.is_file()}
    tex=inventory(literals['TEX_ROOTS']);conf=inventory(literals['CONFIG_ROOTS'])
    conf.update({p:sha(p) for p in literals['CONFIG_EXPLICIT'] if Path(p).is_file()})
    check(tex==load(b/'TEX_INVENTORY_BEFORE.json'),'recaptured full TeX/resource inventory unchanged')
    check(conf==load(b/'CONFIG_BEFORE.json'),'recaptured complete font/locale/loader/resource configuration unchanged')
    current_findings=load(BASE/'FINDINGS.json')
    check(current_findings['census']['open']=={'critical':0,'major':0,'minor':0},'zero current open findings')
    check(current_findings['census']['resolved']=={'critical':0,'major':0,'minor':2},'exact two resolved documentary issues')
    if label=='audit01':
        check(not current_findings['delta_accepted'] and not (BASE/'DELTA.md').exists(),'audit precedes actual delta decision')
    else:
        check(current_findings['delta_accepted'] and current_findings['stage']=='ACCEPTED_NO_CHANGE_DELTA','actual updated acceptance census')
        check('ACCEPT_NO_MANUSCRIPT_CHANGE' in (BASE/'DELTA.md').read_text(),'actual same-reviewer delta document')
        dump(run/'CHANGED_DOCUMENTS_AFTER.json',{p:sha(BASE/p) for p in ['FINDINGS.json','DELTA.md','HISTORICAL_CONTEXT_SUPPLEMENT.md']})
    rt_after=runtime();dump(run/'RUNTIME_AFTER.json',rt_after)
    covered={row['validated_path']:row['sha256'] for row in baseline.values()}
    consumed={**rt_before['mapped_files'],**rt_after['mapped_files']}
    for r in (rt_before,rt_after):
        consumed.update({row['file']:row['sha256'] for row in r['modules'].values() if row['sha256']})
    missing={p:h for p,h in consumed.items() if covered.get(p)!=h or sha(p)!=h}
    dump(run/'RUNTIME_COVERAGE.json',{'consumed':consumed,'missing':missing})
    check(not missing,('documentary auditor runtime coverage',missing))
    check(not Path(sys.pycache_prefix).exists(),'documentary audit bytecode prefix still absent')
    return {'status':'PASS_DOCUMENTARY_DELTA_AUDIT','phase':label,'checks':CHECKS,
      'baseline_paths':len(baseline),'initial_payloads_preserved':len(mapping),
      'historical_search_inputs_preserved':len(history),'response_paths':len(response),
      'recorded_command_counts':counts,'all_size_science_executed':False,'new_build_or_view':False,
      'TeX_resource_roots_recaptured':True,'runtime_coverage_missing':len(missing),
      'raw_root_pair_previously_executed':True,'delta_accepted':current_findings['delta_accepted']}
def seal():
    check(load(OUT/'audit02/audit.stdout')['status']=='PASS_DOCUMENTARY_DELTA_AUDIT','actual final audit completed')
    check(load(OUT/'audit02/COMMAND.json')['exit_code']==0,'actual final auditor exit zero')
    check(sha(BASE/'SHA256SUMS')==INITIAL,'initial outer manifest not previously overwritten')
    check(sha(OUT/'initial_snapshot/SHA256SUMS')==INITIAL,'original manifest preserved')
    count=sum(p.is_file() for p in BASE.rglob('*') if p!=BASE/'SHA256SUMS')+1
    dump(OUT/'FINAL_SEAL_RECEIPT.json',{'status':'ACCEPTED_NO_CHANGE_DELTA_SEALED',
       'payload_count':count,'initial_payloads_preserved':1546,'historical_search_inputs_preserved':1917,
       'initial_manifest_sha256':INITIAL,'delta_sha256':sha(BASE/'DELTA.md'),
       'changed_documentary_paths':['FINDINGS.json','SHA256SUMS'],
       'initial_payload_mapping':'INITIAL_PAYLOAD_MAPPING.json','history_mapping':'HISTORY_INPUT_MAPPING.json',
       'audit01':load(OUT/'audit01/audit.stdout'),'audit02':load(OUT/'audit02/audit.stdout'),
       'external':'HOLD_EXTERNAL','terminal_or_round2_claim':False})
    files=sorted(p for p in BASE.rglob('*') if p.is_file() and p!=BASE/'SHA256SUMS')
    check(len(files)==count,'exact final payload count')
    # Deliberate scoped manifest regeneration only after exact archival preservation.
    with (BASE/'SHA256SUMS').open('w') as f:
        for p in files:f.write(sha(p)+'  '+str(p.relative_to(BASE))+'\n')
    check_manifest(BASE,expected_count=count)
    return {'status':'PASS_ACCEPTED_DELTA_SEALED','payloads':count,'manifest_sha256':sha(BASE/'SHA256SUMS'),
       'DELTA_sha256':sha(BASE/'DELTA.md'),'FINDINGS_sha256':sha(BASE/'FINDINGS.json'),
       'initial_manifest_sha256':INITIAL,'terminal_or_round2_claim':False}
if __name__=='__main__':
    assert sys.flags.optimize==0 and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
    assert sys.pycache_prefix and not Path(sys.pycache_prefix).exists()
    mode=sys.argv[1]
    result=prepare() if mode=='prepare' else seal() if mode=='seal' else audit(mode)
    print(json.dumps(result,sort_keys=True))
