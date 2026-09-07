"""Read-only root closure of original lane38 and its documentary supplement.
No historical producer is imported, executed, queried or repaired here.
"""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_thirty_eighth'
CHILD=BASE/'orientation_source_desk'
QA=ROOT/'docs/papers204_208_sequence/qa/scout38_documentary_audit'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
WATCH={}

def read(path):
    path=Path(path); assert path.is_file() and not path.is_symlink(),str(path)
    raw=path.read_bytes(); value={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}
    assert str(path) not in WATCH or WATCH[str(path)]==value,str(path)
    WATCH[str(path)]=value; return raw

def obj(path): return json.loads(read(path))

def pin(path,value):
    read(path); value={'sha256':value} if isinstance(value,str) else value
    for key in ('sha256','bytes'):
        if key in value: assert WATCH[str(path)][key]==value[key],(str(path),key)

def files(base):
    found=list(base.rglob('*')); assert not any(p.is_symlink() for p in found)
    return {p.relative_to(base).as_posix() for p in found if p.is_file()}

def manifest(base,count,wanted,extra=()):
    raw=read(base/'SHA256SUMS'); assert sha256(raw).hexdigest()==wanted
    entries={}
    for line in raw.decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m
        digest,name=m.groups(); path=Path(name)
        assert name not in entries and not path.is_absolute() and '..' not in path.parts and name!='SHA256SUMS'
        entries[name]=digest; pin(base/name,digest)
    assert len(entries)==count and files(base)==set(entries)|{'SHA256SUMS'}|set(extra)
    return {'payloads':count,'sha256':wanted,'physical_files':len(files(base))}

def lf_lines(raw): return re.findall(rb'[^\n]*\n|[^\n]+$',raw)

def main():
    began=datetime.now(timezone.utc).isoformat()
    for path in (Path(__file__),Path(sys.executable),Path('/usr/bin/cmp')): read(path)
    packages={
        'original_lane':manifest(BASE,156,'778fe4f92eb351eab1fe97a782e9ab93cb5c53f73f31024465778868eb188e45'),
        'original_child':manifest(CHILD,60,'88b0c0f4d85e3f2d47e011001858a6782f4c2aa34f757e7574d3d99a5ddd9984',
            ('SEAL_CHECK.json','SEAL_CHECK.stdout','SEAL_CHECK.stderr')),
        'documentary_supplement':manifest(QA,36,'629d18a50996ed032f09cc964d1f41eaa818ad3a6c84a65dbe226080948d0856')}
    roles=obj(BASE/'CONTROL_ROLES.json'); assert len(roles)==2
    aliases={r['original_path']:r for r in roles}
    for r in roles: pin(r['copy_path'],r['sha256'])
    def historical(path,digest):
        if path in aliases:
            assert aliases[path]['sha256']==digest
            path=aliases[path]['copy_path']
        pin(path,digest); return path
    native=[]; comparisons=[]
    for label,count,exit_code in [('attempt01',275,1),('attempt02',275,0),('payload_check',30,0)]:
        folder=QA/label; r=obj(folder/'receipt.json'); before=obj(folder/'inputs_before.json')
        assert before==obj(folder/'inputs_after.json') and len(before)==count==r['inputs_count']
        assert r['inputs_unchanged'] and r['exit_code']==exit_code and r['cwd']==str(ROOT)
        assert r['start_epoch']<=r['finish_epoch'] and obj(folder/'invocation.json')=={k:r[k] for k in ('argv','cwd','start_epoch','role')}
        for path,value in before.items():
            physical=path
            if label=='attempt01' and path in {str(QA/'check.py'),str(QA/'capture.py')}:
                physical=str(QA/'failed01_source'/Path(path).name)
            pin(physical,value)
        for stream in ('stdout','stderr'):
            assert set(r[stream])=={str(folder/(stream+'.raw'))}
            for path,value in r[stream].items(): pin(path,value)
        if label=='attempt01':
            assert read(folder/'stdout.raw')==b'' and len(read(folder/'stderr.raw'))==414
            assert sha256(read(folder/'stderr.raw')).hexdigest()=='8c6ef71afaa10cb90dc356842d7f7577b8f0ab0bb240d758791217a6bfbc95fe'
        else:
            assert read(folder/'stderr.raw')==b''
            for name in ('check.py','capture.py'):
                assert read(folder/(name+'.at_execution'))==read(QA/name)
        if label=='payload_check':
            entries=[]
            for line in read(QA/'PAYLOAD_SHA256SUMS').decode().splitlines():
                digest,path=line.split('  ',1); pin(path,digest); entries.append(path)
            assert len(entries)==27 and set(entries)|{str(QA/'PAYLOAD_SHA256SUMS'),'/usr/bin/sha256sum'}<=set(before)
            remaining=set(before)-(set(entries)|{str(QA/'PAYLOAD_SHA256SUMS'),'/usr/bin/sha256sum'})
            assert len(remaining)==1 and Path(next(iter(remaining))).name.startswith('python')
            assert read(folder/'stdout.raw')==''.join(p+': OK\n' for p in entries).encode()
        argv=['/usr/bin/cmp','--',str(folder/'inputs_before.json'),str(folder/'inputs_after.json')]
        run=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,check=False)
        assert run.returncode==0 and run.stdout==run.stderr==b''
        comparisons.append({'argv':argv,'exit_code':0,'stdout':'','stderr':''})
        native.append({'label':label,'inputs':count,'exit_code':exit_code,'stdout_bytes':len(read(folder/'stdout.raw')),'stderr_bytes':len(read(folder/'stderr.raw'))})
    records=obj(QA/'attempt02/pin_occurrences.json'); assert len(records)==1164
    for r in records:
        assert historical(r['original_path'],r['sha256'])==r['physical_path']
        pin(r['physical_path'],r)
    commands=obj(QA/'attempt02/commands.json'); assert len(commands)==26
    parent=child=0; reconstructed=0; expected=set(str(BASE/p) for p in files(BASE))|{str(QA/'check.py'),str(QA/'capture.py')}
    for row in commands:
        is_parent=row['schema']=='parent'; parent+=is_parent; child+=not is_parent
        folder=(BASE if is_parent else CHILD)/'commands'/row['label']
        r=obj(folder/'receipt.json'); assert row['receipt']==r
        if is_parent:
            before=obj(folder/'inputs_before.json'); assert before==obj(folder/'inputs_after.json')==row['before']==row['after']
            assert r['input_count']==len(before) and r['unchanged'] and r['exit']==0
            for path,digest in before.items(): expected.add(historical(path,digest))
            stdout=read(folder/'stdout.raw'); pin(folder/'stdout.raw',r['stdout_sha256']); pin(folder/'stderr.raw',r['stderr_sha256'])
        else:
            assert obj(folder/'invocation.json')==row['invocation'] and r['inputs_before']==r['inputs_after']
            assert r['exit_code']==(22 if row['label'] in {'r1_acm_curl','r2_tcs_curl'} else 0)
            before={p['path']:p['sha256'] for p in r['inputs_before']}
            for p in r['inputs_before']+[r[k] for k in ('executable','recorder','stdout','stderr')]:
                path=historical(p['path'],p['sha256']); pin(path,p); expected.add(path)
            stdout=read(folder/'stdout.bin')
        if r['argv'][0]=='sed':
            ranges=[tuple(map(int,s[:-1].split(','))) for s in r['argv'][2].split(';')]; lines=[]
            for arg in r['argv'][3:]:
                path=str(Path(r['cwd'])/arg)
                if path in before: path=historical(path,before[path])
                else: assert not is_parent and row['label']=='read_failures'
                lines.extend(lf_lines(read(path)))
            assert stdout==b''.join(line for n,line in enumerate(lines,1) for lo,hi in ranges if lo<=n<=hi)
            reconstructed+=1
    actual_inputs=obj(QA/'attempt02/inputs_before.json')
    extras=set(actual_inputs)-expected
    assert len(extras)==1 and Path(next(iter(extras))).name.startswith('python')
    assert set(actual_inputs)==expected|extras and len(actual_inputs)==275
    assert parent==14 and child==12 and reconstructed==11
    summary=obj(QA/'attempt02/summary.json'); assert obj(QA/'attempt02/stdout.raw')==summary
    assert read(QA/'attempt02/stdout.raw')==(json.dumps(summary,sort_keys=True)+'\n').encode()
    assert summary['result']=='PASS_DOCUMENTARY_SELF_FAMILIARITY_ONLY' and summary['historical_audit_input_paths']==265
    discovery=obj(QA/'attempt02/discovery.json'); assert discovery['scope']==obj(BASE/'DISCOVERY_SCOPE.json')
    assert len(discovery['metadata_paths'])==len(discovery['filename_classifications'])==901
    assert len(discovery['archived_hit_checks'])==55 and len(discovery['scope']['selected_paths'])==104
    for hit in discovery['archived_hit_checks']:
        assert sha256(lf_lines(read(hit['path']))[hit['line']-1]).hexdigest()==hit['content_sha256']
    for path in [*QA.glob('*.py'),*BASE.glob('*.py'),CHILD/'record_command.py']:
        ast.parse(read(path))
    for path,value in WATCH.items():
        raw=Path(path).read_bytes(); assert value=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)},path
    print(json.dumps({'status':'PASS_ROOT_SCOUT38_ORIGINAL_DOCUMENTARY_CLOSURE_NO_PROMOTION','started_utc':began,
        'ended_utc':datetime.now(timezone.utc).isoformat(),'packages':packages,'native_supplement_attempts':native,
        'current_read_paths_checked_twice':len(WATCH),'read_map_sha256':sha256(json.dumps(WATCH,sort_keys=True).encode()).hexdigest(),
        'checked_original_pin_occurrences':len(records),'original_command_records':len(commands),'LF_only_sed_reconstructions':reconstructed,
        'supplement_input_set_reconstructed':len(actual_inputs),'fresh_raw_comparisons':comparisons,
        'historical_scientific_pilots':0,'new_scientific_source_or_original_audit_executions':0,
        'independent_mathematical_review':False,'external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    main()
