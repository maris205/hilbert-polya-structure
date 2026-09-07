"""Close same-B accepted documentary delta, preserving every initial role.

No scientific execution, build, render, image view or acceptance synthesis.
The same reviewer's existing decision is checked and sealed, not inferred.
"""
import hashlib
import json
import os
from pathlib import Path
import sys

W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
F=W/'papers/209-ordered-fibre-threading/frozen_round1'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
INITIAL_SEAL='d88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea'
INITIAL_DELTA='282dc2ab3f0021abeca145c20b76d0e0ef10e0b0e9948a173a24e6ead05b1400'
RESPONSE='c2cab3d26ddd9f5e5ba7e31dc0f3afa1c8d06510fd1276294cae33c63cdbc1f8'


def h(path):
    value=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):value.update(block)
    return value.hexdigest()


def info(path):
    path=Path(path)
    return {'sha256':h(path),'bytes':path.stat().st_size,'resolved':str(path.resolve()),
            'symlink':os.readlink(path) if path.is_symlink() else None}


def js(path):return json.loads(Path(path).read_bytes())


def manifest(path,base=None,complete=False,initial_alias=False):
    path=Path(path);base=Path(base) if base is not None else path.parent
    rows={}
    for line in path.read_text().splitlines():
        digest,name=line.split('  ',1);rel=Path(name)
        assert len(digest)==64 and set(digest)<=set('0123456789abcdef')
        assert not rel.is_absolute() and '..' not in rel.parts and rel.as_posix()==name
        assert name not in rows and base/rel!=path
        target=B/'INITIAL_DELTA.md' if initial_alias and name=='DELTA.md' else base/rel
        assert not target.is_symlink() and h(target)==digest,(str(path),name)
        rows[name]=digest
    if complete:
        assert set(rows)=={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file() and p!=path}
    return rows


def check_map(before,after,count):
    first=js(before);second=js(after)
    assert first==second and len(first)==count
    for path,wanted in first.items():
        assert info(path)==wanted,('CURRENT_DEPENDENCY_DRIFT',path)
    return first


def main():
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize==0
    assert dict(os.environ)==ENV and Path.cwd()==W and not Path(sys.pycache_prefix).exists()
    assert not (B/'PRESEAL_DELTA.json').exists() and not (B/'FINAL_REVIEW_SEAL.pending').exists()
    assert h(B/'SHA256SUMS')==h(B/'INITIAL_REVIEW_SEAL.sha256')==INITIAL_SEAL
    assert h(B/'INITIAL_DELTA.md')==INITIAL_DELTA and h(B/'DELTA.md')!=INITIAL_DELTA
    assert h(B/'REPORT.md')=='089f10c004f933f17db0a701e161b5d19edb3c74f9c3896348fad5711f109f12'
    assert h(B/'FINDINGS.json')=='395340caae7a758f1791b71f684c8c11fb82ccbfa383d98c83141b9e8cf74e17'
    original=manifest(B/'INITIAL_REVIEW_SEAL.sha256',B,initial_alias=True)
    assert len(original)==1298 and original['DELTA.md']==INITIAL_DELTA
    initial_census=js(B/'FINDINGS.json');assert initial_census['delta_status']=='UNASSESSED'
    census=js(B/'CURRENT_FINDINGS.json')
    assert census['schema']=='p209-manuscript-review-findings-v1'
    assert census['reviewer']=='/root/p209_b_reviewer' and census['input_round']==1
    assert census['delta_status']=='ACCEPTED_EXACT_NOCHANGE_DELTA'
    assert census['current_open_counts']=={'critical':0,'major':0,'minor':0} and census['findings']==[]
    assert census['scientific_inputs_changed'] is False and census['new_round2_created'] is False
    assert census['response_sha256']==RESPONSE
    assert census['initial_complete_manifest_role']=='INITIAL_REVIEW_SEAL.sha256'
    assert census['initial_complete_manifest_sha256']==INITIAL_SEAL
    assert (census['initial_payloads'],census['initial_same_path_payloads'],census['initial_exact_delta_alias_payloads'])==(1298,1297,1)
    assert 'ACCEPTED_EXACT_NOCHANGE_DELTA' in (B/'DELTA.md').read_text()
    assert h(W/'docs/papers204_208_sequence/P209_B_RESPONSE.md')==RESPONSE
    assert h(B/'delta_intake_01/context/08_P209_B_RESPONSE.md')==RESPONSE
    assert h(B/'DELTA_ADAPTATION.diff')=='03176a0ca4343e9fd7e4d4431d5ca7a6feba01df33217e4e8a47158bb2f495f2'
    assert h(B/'verify.py')=='d5fd105ddfc162323f06cd530fbd696b0093643a7a0c24c64747cd9c9be30467'
    assert h(B/'CANONICAL.json')=='612e1463162deba868cf7cf81d61c8f017713f9b28c4c38b81b00d376bac992c'
    assert h(F/'SHA256SUMS')=='c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
    assert len(manifest(F/'SHA256SUMS',complete=True))==2003
    assert len(manifest(B/'INPUT_PINS.sha256',W))==2004
    nested={}
    for name,row in js(B/'PRESEAL_CHECK.json')['nested_seals'].items():
        assert h(B/name/'SHA256SUMS')==row['sha256']
        assert len(manifest(B/name/'SHA256SUMS',complete=True))==row['payloads']
        nested[name]=row
    assert len(nested)==10
    for name,count,digest in [
        ('delta_intake_01',29,'5a655c39e3e32d433bd2449635c958980fcb60ef6412cd06719df15300e7fb97'),
        ('delta_check_01',64,'6ea48c853dfdf769b1b315d6f55d5b0341e68d6a466e5ae0f95e2a5be2494740'),
        ('delta_check_02',64,'8987d60fc57d05379e161d7631a508b325aca6f2edc4f08758065b9208d5d36c')]:
        assert h(B/name/'SHA256SUMS')==digest
        assert len(manifest(B/name/'SHA256SUMS',complete=True))==count
        nested[name]={'payloads':count,'sha256':digest}
    success=B/'delta_check_02'
    evidence=js(success/'DELTA_EVIDENCE_RESULT.json')
    assert evidence['status']=='PASS_EXACT_NOCHANGE_DELTA_EVIDENCE'
    assert evidence['response_sha256']==RESPONSE and evidence['accepted_decision_not_written_by_checker']
    assert evidence['delta_full_input_paths']==128227 and evidence['all_inputs_unchanged']
    assert evidence['counts']['all_original_documentary_pins_retained']==127544
    assert evidence['new_delta_mathematical_producers']==evidence['new_delta_builds_renders_views']==0
    assert evidence['counts']['preserved_failed_delta_wrappers']==1
    wrapper=js(success/'RECEIPT.json')
    assert wrapper['status']=='PASS' and wrapper['failure'] is None and wrapper['inputs_unchanged']
    assert wrapper['commands']==1 and wrapper['inputs']==5166
    wrapper_commands=js(success/'WRAPPER_COMMAND_RECORDS.json');assert len(wrapper_commands)==1
    assert wrapper_commands[0]['command']==js(success/'documentary_child.command.json')
    assert wrapper_commands[0]['command']['exit']==0
    actual=js(B/'DELTA_CHECK_EXECUTION.actual.json');assert actual['actual_exit_code']==0
    actual_result=json.loads(actual['actual_output']);assert actual_result['status']=='PASS'
    assert actual_result['seal']['sha256']==nested['delta_check_02']['sha256']
    for entry in wrapper_commands+js(success/'ALL_COMMAND_RECORDS.json'):
        row=entry['command'];folder=Path(entry['folder']);tag=entry['tag']
        assert row==js(folder/(tag+'.command.json'))
        assert row['exit']==0 and row['env']==ENV and row['process_outcome']=='COMPLETED'
        assert row['spawn_error'] is None and row['cleanup']==[]
        for channel in ('stdout','stderr'):
            got=info(folder/row[channel]);pin=row[channel+'_info']
            assert all(got[k]==v for k,v in pin.items())
    assert len(js(success/'ALL_COMMAND_RECORDS.json'))==8
    failure=js(B/'delta_check_01/CLOSURE_AFTER_FAILURE.json')
    assert failure['status']=='FAIL_PRESERVED_OUTER_WRAPPER_FILENAME_COLLISION'
    assert failure['actual_outer_exit']==1 and failure['actual_child_exit']==0
    # Retain and rehash the actual full consumed map; never rebase its keys.
    dependencies=check_map(success/'INPUTS_FULL_BEFORE.json',success/'INPUTS_FULL_AFTER.json',128227)
    assert str(B/'DELTA.md') not in dependencies and str(B/'SHA256SUMS') not in dependencies
    assert str(B/'INITIAL_DELTA.md') in dependencies and str(B/'INITIAL_REVIEW_SEAL.sha256') in dependencies
    wrapper_inputs=check_map(success/'INPUTS_BEFORE.json',success/'INPUTS_AFTER.json',5166)
    payload_paths=sorted(p for p in B.rglob('*') if p.is_file() and p!=B/'SHA256SUMS')
    assert all(not p.is_symlink() for p in payload_paths)
    payload_before={p.relative_to(B).as_posix():info(p) for p in payload_paths}
    assert manifest(B/'INITIAL_REVIEW_SEAL.sha256',B,initial_alias=True)==original
    for path,wanted in dependencies.items():assert info(path)==wanted,('FINAL_DEPENDENCY_DRIFT',path)
    for path,wanted in wrapper_inputs.items():assert info(path)==wanted,('FINAL_WRAPPER_DRIFT',path)
    assert payload_paths==sorted(p for p in B.rglob('*') if p.is_file() and p!=B/'SHA256SUMS')
    assert payload_before=={p.relative_to(B).as_posix():info(p) for p in payload_paths}
    # All writes below are new mechanical closure outputs and replacement of
    # the current outer role only, after its exact original was revalidated.
    record={'status':'PASS_ACCEPTED_DELTA_PRESEAL','reviewer':census['reviewer'],
            'delta_status':census['delta_status'],'current_open_counts':census['current_open_counts'],
            'initial_manifest_role':'INITIAL_REVIEW_SEAL.sha256','initial_manifest_sha256':INITIAL_SEAL,
            'initial_payloads':1298,'initial_same_path_payloads':1297,'initial_exact_delta_alias_payloads':1,
            'initial_report_and_census_unchanged':True,'original_documentary_pins_retained':127544,
            'delta_consumed_paths_rehashed_twice':len(dependencies),'wrapper_inputs_rehashed_twice':len(wrapper_inputs),
            'full_delta_map_roles':['delta_check_02/INPUTS_FULL_BEFORE.json','delta_check_02/INPUTS_FULL_AFTER.json'],
            'full_delta_map_sha256':h(success/'INPUTS_FULL_BEFORE.json'),
            'payload_inputs_before_and_rechecked_after':payload_before,'nested_seals':nested,
            'response_sha256':RESPONSE,'frozen_payloads':2003,'frozen_inputs':2004,
            'new_mathematical_producers_builds_renders_views':0,
            'scope':'Actual mechanical documentary closure of an already written same-reviewer decision; no mathematical execution, build, render, image view, continuous tracing or OS-hermeticity.',
            'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    with (B/'PRESEAL_DELTA.json').open('x') as stream:
        json.dump(record,stream,sort_keys=True,indent=2);stream.write('\n')
    paths=sorted(p for p in B.rglob('*') if p.is_file() and p!=B/'SHA256SUMS')
    assert all(not p.is_symlink() for p in paths)
    with (B/'FINAL_REVIEW_SEAL.pending').open('x') as stream:
        for path in paths:stream.write(h(path)+'  '+path.relative_to(B).as_posix()+'\n')
    assert h(B/'SHA256SUMS')==h(B/'INITIAL_REVIEW_SEAL.sha256')==INITIAL_SEAL
    (B/'FINAL_REVIEW_SEAL.pending').replace(B/'SHA256SUMS')
    final=manifest(B/'SHA256SUMS',complete=True)
    assert manifest(B/'INITIAL_REVIEW_SEAL.sha256',B,initial_alias=True)==original
    print(json.dumps({'status':'PASS_SEALED_SAME_B_ACCEPTED_EXACT_NOCHANGE_DELTA',
                      'payloads':len(final),'seal_sha256':h(B/'SHA256SUMS'),
                      'initial_payloads_preserved':1298,'initial_same_paths':1297,'initial_delta_aliases':1,
                      'initial_seal_sha256':INITIAL_SEAL,'nested_packages':len(nested),
                      'all_original_documentary_pins_retained':127544,
                      'delta_consumed_paths_rehashed_twice':128227,
                      'delta_status':census['delta_status'],'current_open_counts':census['current_open_counts'],
                      'external':'OWNER_AMBER / HOLD_EXTERNAL'},sort_keys=True))


if __name__=='__main__':main()
