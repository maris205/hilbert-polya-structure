"""Root documentary closure including exact later reconstruction roles; no science."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BATCH=ROOT/'docs/papers204_208_sequence'
S=BATCH/'scouting/finite_systems_thirty_fifth'
R=BATCH/'qa/scout35_initial_document_recovery'
C=BATCH/'qa/central_lifecycle_p209_terminal_push'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
WATCH={}


def read(p):
    p=Path(p); assert p.is_file() and not p.is_symlink(), str(p)
    raw=p.read_bytes(); row={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}
    if str(p) in WATCH: assert WATCH[str(p)]==row
    WATCH[str(p)]=row
    return raw


def pin(p,value):
    read(p); expected={'sha256':value} if isinstance(value,str) else value
    assert WATCH[str(p)]==expected if 'bytes' in expected else WATCH[str(p)]['sha256']==expected['sha256'], str(p)


def j(p): return json.loads(read(p))


def manifest(base,name,count,digest,excluded=()):
    pin(base/name,digest); rows={}
    for line in read(base/name).decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m
        value,rel=m.groups(); path=Path(rel)
        assert not path.is_absolute() and '..' not in path.parts and rel not in rows and rel!=name
        rows[rel]=value; pin(base/rel,value)
    assert len(rows)==count
    assert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}==set(rows)|{name}|set(excluded)
    return rows


def run(argv,expected=0,cwd=ROOT):
    started=datetime.now(timezone.utc).isoformat()
    child=subprocess.run(argv,cwd=cwd,env=ENV,capture_output=True,check=False)
    assert child.returncode==expected and not child.stderr, (argv,child.returncode,child.stderr)
    return {'argv':argv,'cwd':str(cwd),'environment':ENV,'started_utc':started,
            'ended_utc':datetime.now(timezone.utc).isoformat(),'exit_code':child.returncode,
            'stdout':child.stdout.decode(),'stderr':child.stderr.decode()}


def main():
    read(Path(__file__).resolve()); read(Path(sys.executable).resolve())
    read(Path('/usr/bin/diff')); read(Path('/usr/bin/cmp'))
    rows=manifest(S,'MANIFEST.sha256',31,'81660274d7cc677c7fac2b917fe2f5b6d8c2d5c18ccd68ffde5b6f85306be81a',{'CLOSURE_AUDIT.actual.json'})
    manifest(R,'RECOVERY_SHA256SUMS',18,'305c7b712d6cc20d435bbba9f68507e982d57f02e7ac4755741f1fe068141906')
    manifest(C,'SHA256SUMS',5,'e5b02d4594deba8e6bec8a5d31dac9b20dd2f40f8245be57dbf56bc5a39fad80')
    oldrows={}
    for line in read(S/'MANIFEST.initial_before_audit_failure.sha256').decode().splitlines():
        digest,name=line.split('  ',1); assert name not in oldrows
        path=R/'reconstructed_initial'/name if name in {'REPORT.md','SOURCE_AND_HISTORY.md'} else S/name
        pin(path,digest); oldrows[name]=digest
    assert len(oldrows)==27
    wrapper=j(S/'CLOSURE_AUDIT.actual.json'); assert wrapper['actual_result']['exit_code']==0
    actual=json.loads(wrapper['actual_result']['output']); assert actual==wrapper['parsed_stdout']
    assert actual['status']=='PASS_DOCUMENTARY_ONLY' and actual['documentary_checks']==2970
    assert actual['manifest_pin']==WATCH[str(S/'MANIFEST.sha256')]
    assert set(actual['all_owned_payload_pins'])==set(rows)
    for name,value in actual['all_owned_payload_pins'].items(): pin(S/name,value)
    assert wrapper['manifest_generation_actual']['exit_code']==0
    assert wrapper['manifest_generation_actual']['output'].encode()==read(S/'MANIFEST.sha256')
    checked=wrapper['strict_manifest_check']; assert checked['exit_code']==0
    assert checked['output']==''.join(n+': OK\n' for n in rows)
    captures=j(C/'CAPTURE.actual.json')
    for control in actual['controls']:
        origin=Path(control['literal_original_path']); old=Path(control['physical_oldhash_role'])
        pin(old,control['old_pin']); read(origin)
        newer=C/(origin.stem+'.before.md'); pin(newer,control['current_pin'])
        rel=origin.relative_to(ROOT).as_posix()
        rr=[r for r in captures['copies'] if r['source']==rel]; assert len(rr)==1
        assert rr[0]['copy']==newer.relative_to(ROOT).as_posix()
        assert rr[0]['actual_comparison']['exit_code']==0 and rr[0]['actual_comparison']['output']==''
        assert (read(newer)==read(old))==control['current_raw_equal_snapshot']
    search=j(S/'HISTORY_SEARCH_01.actual.json'); other=j(S/'HISTORY_SEARCH_02.actual.json')
    assert search['inputs_before']==search['inputs_after']==other['inputs_before']==other['inputs_after']
    assert len(search['inputs_before'])==537
    for path,value in search['inputs_before'].items(): pin(Path(path),value)
    for rr in (search,other):
        assert rr['exit']==0 and rr['stderr']=='' and rr['argv'][6:]==sorted(rr['inputs_before'])
        for key in ('searcher','tool'):
            pin(Path(rr[key]['path']),{k:rr[key][k] for k in ('sha256','bytes')})
        for line in rr['stdout'].splitlines():
            m=re.fullmatch(r'([^:]+):([0-9]+):(.*)',line); assert m and m[1] in search['inputs_before']
            assert read(Path(m[1])).decode().splitlines()[int(m[2])-1]==m[3]
    native_recovery=j(R/'PHYSICAL_RECOVERY_CHECK.actual.json'); assert native_recovery['exit_code']==0
    recovered=json.loads(native_recovery['output'])
    assert recovered['status']=='LATER_RECONSTRUCTION_FROM_ACTUAL_HISTORY_AND_MATCHING_OLD_PIN'
    assert recovered['complete_forward_delta_reaches_both_exact_current_documents']
    receipts=[]
    receipts.append(run(['/usr/bin/python3','-I','-S','-B',str(R/'validate_recovery.py')]))
    assert json.loads(receipts[-1]['stdout'])==recovered
    receipts.append(run(['/usr/bin/python3','-I','-S','-B',str(S/'audit_closure_v2.py'),'--audit']))
    current=json.loads(receipts[-1]['stdout']); assert current['status']=='PASS_DOCUMENTARY_ONLY'
    assert current['documentary_checks']==2972 and current['payload_file_count']==31
    assert current['all_owned_payload_pins']==actual['all_owned_payload_pins']
    for row in j(S/'DIRECT_ORIGINAL_INPUTS.json')['inputs']:
        origin,snapshot=Path(row['original_path']),S/row['snapshot_path']
        pin(origin,{k:row[k] for k in ('sha256','bytes')}); pin(snapshot,{k:row[k] for k in ('sha256','bytes')})
        receipts.append(run(['/usr/bin/cmp','--',str(origin),str(snapshot)]))
    diffs=j(R/'ACTUAL_FORWARD_DIFFS.json')['commands']; assert len(diffs)==2
    for name,old in zip(('REPORT.md','SOURCE_AND_HISTORY.md'),diffs):
        rec=run(['/usr/bin/diff','-u','--label','initial/'+name,'reconstructed_initial/'+name,
                 '--label','captured_final/'+name,'inputs/'+name],expected=1,cwd=R)
        assert rec['stdout']==old['output'] and old['exit_code']==1; receipts.append(rec)
    for path,wanted in WATCH.items():
        raw=Path(path).read_bytes(); assert wanted=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}, path
    print(json.dumps({'status':'PASS_ROOT_SCOUT35_ORIGINAL_DOCUMENTARY_CLOSURE_WITH_EXPLICIT_LATER_RECONSTRUCTION',
        'science_executions':0,'final_payloads':31,'final_physical_files':33,'recovery_payloads':18,
        'initial_payload_roles':27,'initial_same_paths':25,'later_reconstructed_documents':2,
        'old_final_documentary_checks':2970,'fresh_existing_documentary_auditor_checks':2972,
        'historical_originals':537,'current_paths_checked_twice':len(WATCH),
        'current_read_map':WATCH,'actual_documentary_commands':receipts,
        'preservation_boundary':'Two initial documents are later matching-pin reconstructions, not pre-edit physical snapshots. All existing original manifests, failures and accepted payloads unchanged.',
        'owner':'OWNER_AMBER','external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))


if __name__=='__main__': main()
