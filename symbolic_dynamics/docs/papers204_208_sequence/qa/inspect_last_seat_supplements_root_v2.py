"""Root documentary closure V2: original hash-string and rich-record pin schemas.\nV1 and its actual failure remain preserved; no old script/query/science run.\n"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence'
OWN=BASE/'qa/last_seat_supplements_documentary_audit'
READS={}

def read(p):
    p=Path(p); assert p.is_file() and not p.is_symlink() and p.resolve()==p,str(p)
    raw=p.read_bytes(); row={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}
    assert str(p) not in READS or READS[str(p)]==row,str(p)
    READS[str(p)]=row
    return raw

def j(p): return json.loads(read(p))

def pin(p,expected):
    read(p); row={'sha256':expected} if isinstance(expected,str) else expected
    for key in ('sha256','bytes'):
        if key in row: assert READS[str(p)][key]==row[key],(str(p),key)

def manifest(base,name,count,digest):
    pin(base/name,digest); rows={}
    for line in read(base/name).decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m
        h,rel=m.groups(); p=Path(rel)
        assert rel not in rows and rel!=name and not p.is_absolute() and '..' not in p.parts
        rows[rel]=h; pin(base/rel,h)
    physical=set()
    for p in base.rglob('*'):
        assert not p.is_symlink(),str(p)
        if p.is_file(): physical.add(p.relative_to(base).as_posix())
    assert len(rows)==count and physical==set(rows)|{name},str(base)
    return rows

def main():
    began=datetime.now(timezone.utc).isoformat(); read(Path(__file__).resolve())
    manifest(OWN,'SHA256SUMS',20,'b28759e405f8df29b79b73043c485f38cda3f6277639699db7afe2867fd01a49')
    result=j(OWN/'run_04/stdout.raw'); receipt=j(OWN/'run_04/receipt.json'); summary=result['summary']
    assert receipt['argv']==['python3','-I','-B',str(OWN/'check.py')] and receipt['cwd']==str(ROOT)
    assert receipt['exit']==0 and receipt['summary']==summary and read(OWN/'run_04/stderr.raw')==b''
    for stream in ('stdout','stderr'):
        pin(OWN/('run_04/'+stream+'.raw'),{'sha256':receipt[stream+'_sha256'],'bytes':receipt[stream+'_bytes']})
    pin(OWN/'run_04/stdout.raw','95fffcba17bd68adfc2cc6b2f7ce08b2ea6d88d807ec6d4df79bc8879a32a6b9')
    assert summary['verdict']=='PASS_DOCUMENTARY_ONLY_NOT_MATHEMATICAL_REVIEW'
    before=result['consumed_before']; assert before==result['consumed_after'] and len(before)==555
    assert sha256((json.dumps(before,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()==summary['pinmap_canonical_sha256']=='ec352122044d7ff2ae1a7a28c04e17e7ef05f61a6ac49a1c1f0e3617f209bdb7'
    for p,row in before.items():
        assert row['physical_path']==p and row['symlink'] is False
        pin(Path(p),row)
    packages=summary['packages']; assert len(packages)==7
    for row in packages:
        name='MANIFEST.sha256' if row['package']=='scouting/LNR_SOURCE_RECHECK' else 'SHA256SUMS'
        manifest(BASE/row['package'],name,row['payloads'],row['seal_sha256'])
        assert row['physical_files']==row['payloads']+1
    assert sum(r['payloads'] for r in packages)==484
    aliases={}
    for row in result['historical_control_aliases']:
        assert row['exact_physical_alias']==str(BASE/'qa/central_lifecycle_p209_terminal_push'/(Path(row['original']).stem+'.before.md'))
        pin(Path(row['exact_physical_alias']),row['historical_sha256'])
        aliases[(row['original'],row['historical_sha256'])]=Path(row['exact_physical_alias'])
    assert len(aliases)==3
    commands=result['commands']; assert len(commands)==summary['native_command_packages']==64
    seen=set(); pins_checked=0
    for entry in commands:
        folder=BASE/entry['path']; assert folder not in seen; seen.add(folder)
        upper=entry['schema']=='uppercase_native'
        assert upper or entry['schema']=='lowercase_native'
        rec=j(folder/('RECEIPT.json' if upper else 'receipt.json'))
        assert rec['argv']==entry['argv'] and rec['exit_code' if upper else 'exit']==entry['exit']
        suffix='' if upper else '.raw'
        stdout,stderr=read(folder/('stdout'+suffix)),read(folder/('stderr'+suffix))
        assert len(stdout)==entry['stdout_bytes']
        first=j(folder/('INPUTS_BEFORE.json' if upper else 'inputs_before.json'))
        second=j(folder/('INPUTS_AFTER.json' if upper else 'inputs_after.json'))
        assert first==second and len(first)==entry['input_count']
        for name,row in first.items():
            p=Path(name)
            if not p.is_absolute(): p=BASE/'scouting/LNR_SOURCE_RECHECK'/p
            digest=row if isinstance(row,str) else row['sha256']
            assert re.fullmatch(r'[0-9a-f]{64}',digest)
            pin(aliases.get((str(p),digest),p),row); pins_checked+=1
        if upper:
            attempt=j(folder/'ATTEMPT.json'); assert attempt['status']=='ATTEMPTED' and attempt['exit_code'] is None
            assert all(attempt[k]==rec[k] for k in ('argv','cwd','environment','started_utc'))
            for stream in ('stdout','stderr'): pin(folder/stream,rec[stream])
        else:
            for stream in ('stdout','stderr'): pin(folder/(stream+'.raw'),rec[stream+'_sha256'])
    assert len(result['http'])==summary['native_http_transactions']==8 and summary['serialized_web_returns']==7
    assert sum(row['curl_exit']==28 for row in result['http'])==summary['real_http_timeouts']==2
    for name in ('source_clearance','independent_mathematical_review'):
        assert summary[name] is False
    for name in ('scientific_executions','source_queries','old_scripts_executed','candidate_admissions'):
        assert summary[name]==0
    failures=[]
    for number in (1,2,3):
        failed=OWN/('run_%02d'%number); rec=j(failed/'receipt.json')
        assert rec['exit']==1 and read(failed/'stdout.raw')==b''
        pin(failed/'stderr.raw',{'sha256':rec['stderr_sha256'],'bytes':rec['stderr_bytes']})
        read(OWN/('failed_run_%02d_checker.py.txt'%number)); failures.append(rec['stderr_bytes'])
    for p,want in READS.items():
        raw=Path(p).read_bytes(); assert want=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)},p
    print(json.dumps({'status':'ROOT_COMPLETE_LAST_SEAT_SUPPLEMENTS_ORIGINAL_DOCUMENTARY_CLOSURE','started_utc':began,'ended_utc':datetime.now(timezone.utc).isoformat(),'auditor_native_exit':0,'auditor_consumed_paths_checked_twice':555,'all_root_current_read_paths_checked_twice':len(READS),'root_map_sha256':sha256(json.dumps(READS,sort_keys=True).encode()).hexdigest(),'six_bundle_payloads':479,'six_bundle_physical_files':485,'additional_exact_control_alias_payloads':5,'own_audit_payloads':20,'native_commands_checked':64,'native_command_input_pins_checked':pins_checked,'source_transport_records':result['http'],'original_copy_roles':summary['copy_roles'],'historical_controls':result['historical_control_aliases'],'real_failed_attempts_stderr_bytes':failures,'source_clearance':False,'independent_mathematical_review':False,'new_science_source_build_view_or_old_script_executions':0,'owner':'OWNER_AMBER','external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__': main()
