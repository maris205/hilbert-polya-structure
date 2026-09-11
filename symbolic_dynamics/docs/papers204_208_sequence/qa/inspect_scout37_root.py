"""Read-only root closure of lane37 and the separate exact QEF correction.
No original audit, analysis or scientific producer is imported or executed.
"""
import ast
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BATCH=ROOT/'docs/papers204_208_sequence'
BASE=BATCH/'scouting/finite_systems_thirty_seventh'
OLD=BATCH/'scouting/finite_algebra_ninth'
SUP=BATCH/'qa/scout37_qef_static_correction'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
WATCH={}

def read(path):
    path=Path(path); assert path.is_file() and not path.is_symlink(),str(path)
    raw=path.read_bytes(); row={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}
    assert str(path) not in WATCH or WATCH[str(path)]==row,str(path)
    WATCH[str(path)]=row; return raw

def j(path): return json.loads(read(path))

def pin(path,value):
    read(path); row={'sha256':value} if isinstance(value,str) else value
    for key in ('sha256','bytes'):
        if key in row: assert WATCH[str(path)][key]==row[key],(str(path),key)

def manifest(base,count,wanted=None):
    raw=read(base/'SHA256SUMS')
    if wanted: assert sha256(raw).hexdigest()==wanted,str(base)
    rows={}
    for line in raw.decode().splitlines():
        match=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert match
        digest,name=match.groups(); path=Path(name)
        assert name not in rows and name!='SHA256SUMS' and not path.is_absolute() and '..' not in path.parts
        rows[name]=digest; pin(base/name,digest)
    files=set()
    for path in base.rglob('*'):
        assert not path.is_symlink()
        if path.is_file(): files.add(path.relative_to(base).as_posix())
    assert len(rows)==count and files==set(rows)|{'SHA256SUMS'},str(base)
    return {'payloads':len(rows),'sha256':sha256(raw).hexdigest()}

def main():
    began=datetime.now(timezone.utc).isoformat()
    read(Path(__file__)); read(Path(sys.executable)); read('/usr/bin/cmp')
    packages={'lane37':manifest(BASE,73,'99889910709c10e12b6d790764bc89016f109f9677da003124129e7bb97cc4e3'),
              'old_qef':manifest(OLD,66,'75e0b287ce1050a4097c5499c7f0aa352aba88617abb0942d59ddf84bcaac1ba'),
              'root_static_correction':manifest(SUP,2)}
    roles=j(BASE/'CONTROL_ROLES.json'); assert len(roles)==3
    aliases={row['original_path']:row for row in roles}; assert len(aliases)==3
    for row in roles: pin(row['copy_path'],row['sha256'])
    identities=set(); occurrences=0
    def historical(path,value):
        nonlocal occurrences
        digest=value if isinstance(value,str) else value['sha256']
        physical=path
        if path in aliases:
            assert aliases[path]['sha256']==digest
            physical=aliases[path]['copy_path']
        pin(physical,value); identities.add((path,digest)); occurrences+=1
    complete=j(BASE/'commands/09_documentary_audit_corrected/stdout.raw')
    assert complete['status']=='PASS_BOUNDED_DOCUMENTARY_AUDIT_NOT_MATH_REVIEW'
    consumed=complete['complete_consumed_inputs_read_twice_unchanged']
    assert len(consumed)==complete['consumed_file_count']==95
    for path,value in consumed.items(): pin(path,value)
    groups=sorted((BASE/'commands').glob('*/receipt.json'))
    assert [p.parent.name[:2] for p in groups]==[f'{n:02d}' for n in range(1,10)]
    summaries=[]; sed_count=rg_count=0
    for path in groups:
        folder=path.parent; row=j(path); before=j(folder/'inputs_before.json')
        assert before==j(folder/'inputs_after.json') and row['unchanged'] and len(before)==row['input_count']
        for name,value in before.items(): historical(name,value)
        raw=read(folder/'stdout.raw'); err=read(folder/'stderr.raw')
        pin(folder/'stdout.raw',row['stdout_sha256']); pin(folder/'stderr.raw',row['stderr_sha256'])
        assert row['cwd']==str(ROOT) and row['started_epoch']<=row['finished_epoch']
        expected=1 if folder.name=='08_documentary_audit' else 0
        assert row['exit']==expected
        if expected:
            assert raw==b'' and len(err)==543 and len(before)==61
            assert row['stderr_sha256']=='db853c7ceb86383f21200f5dc8bf1fb1feb783e1e3345a49175027071746c5db'
        else: assert err==b''
        argv=row['argv']
        if argv[0]=='sed':
            assert argv[:3]==['sed','-n','1,4000p']
            joined=b''.join(read(p) for p in argv[3:])
            lines=re.findall(rb'[^\n]*\n|[^\n]+$',joined)
            assert raw==b''.join(lines[:4000]); sed_count+=1
        elif argv[0]=='rg':
            assert argv[1]=='-n' and argv[3]=='--'; pattern=re.compile(argv[2]); expected_lines=[]
            for name in argv[4:]:
                for num,line in enumerate(read(name).decode().split('\n'),1):
                    if pattern.search(line): expected_lines.append(f'{name}:{num}:{line}')
            assert Counter(raw.decode().splitlines())==Counter(expected_lines); rg_count+=1
        elif argv[0]=='cp':
            assert argv[:2]==['cp','-p'] and set(argv[2:-1])==set(aliases)
            assert argv[-1]==str(BASE/'controls') and raw==b''
        else:
            assert folder.name in {'07_archived_pilot_analysis','08_documentary_audit','09_documentary_audit_corrected'}
        summaries.append({'command':folder.name,'inputs':len(before),'exit':row['exit'],'stdout_bytes':len(raw),'stderr_bytes':len(err)})
    run=BASE/'pilot_run'; before=j(run/'inputs_before.json'); assert before==j(run/'inputs_after.json') and len(before)==7
    for name,value in before.items(): pin(name,value)
    command=j(run/'receipt.json'); attempt=j(run/'attempt.json')
    assert command['argv']==attempt['argv']==[attempt['python_executable'],'-I','-S','-B',str(BASE/'pilot.py')]
    assert command['cwd']==attempt['cwd']==str(ROOT) and command['exit']==0 and command['unchanged']
    assert not command['timed_out'] and attempt['timeout_seconds']==60
    pin(run/'stdout.raw',command['stdout_sha256']); pin(run/'stderr.raw',command['stderr_sha256'])
    assert len(read(run/'stdout.raw'))==68160 and read(run/'stderr.raw')==b''
    data=j(run/'stdout.raw')
    assert data['status']=='PASS_FIXED_BOX_PILOT_NOT_ALL_FIELD_TEMPORAL_PROOF'
    assert data['checks']==124629 and data['total_states']==data['total_targets']==5408 and data['primes']==[3,5,7,17]
    for box in data['boxes']:
        assert box['state_count']==box['prime']**3
        for key in ('successor_indices','every_target_fibre_size','every_state_depth','every_state_eventual_period'):
            assert len(box[key])==box['state_count']
        assert sum(box['every_target_fibre_size'])==box['state_count']
        assert sum(row['basin_states'] for row in box['cycles'])==box['state_count']
    compact={k:data[k] for k in ('status','total_states','total_targets','checks')}
    compact['fields']=[{k:b[k] for k in ('prime','state_count','maximum_depth','cycle_length_histogram','image_size','fibre_histogram')} for b in data['boxes']]
    assert compact==command['compact_result']
    analysis=j(BASE/'commands/07_archived_pilot_analysis/stdout.raw')
    assert analysis['new_successor_evaluations']==analysis['extra_fields']==analysis['extrapolated_theorems']==0
    assert analysis['rows'][-1]['recurrent_all_distinct_squares']==48
    sources=sorted((BASE/'sources').glob('*.json')); assert len(sources)==5
    for path in sources:
        row=j(path); assert set(row)=={'role','request','result'} and row['result']
        assert row['role'].startswith('Full available serialized Web tool return')
    parsed=[]
    for path in sorted(BASE.glob('*.py')):
        compile(ast.parse(read(path)),str(path),'exec',dont_inherit=True,optimize=0); parsed.append(path.name)
    comparisons=[]
    for folder in (run,BASE/'commands/08_documentary_audit',BASE/'commands/09_documentary_audit_corrected'):
        argv=['/usr/bin/cmp','--',str(folder/'inputs_before.json'),str(folder/'inputs_after.json')]
        child=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,check=False)
        assert child.returncode==0 and child.stdout==child.stderr==b''
        comparisons.append({'argv':argv,'cwd':str(ROOT),'environment':ENV,'exit_code':0,'stdout':'','stderr':''})
    for name,value in WATCH.items():
        raw=Path(name).read_bytes(); assert value=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)},name
    print(json.dumps({'status':'PASS_ROOT_SCOUT37_COMPLETE_ORIGINAL_DOCUMENTARY_CLOSURE_NO_PROMOTION',
        'started_utc':began,'ended_utc':datetime.now(timezone.utc).isoformat(),'packages':packages,
        'original_successful_audit_consumed_paths':95,'historical_pin_occurrences':occurrences,'distinct_historical_identities':len(identities),
        'root_current_paths_checked_twice':len(WATCH),'root_read_map_sha256':sha256(json.dumps(WATCH,sort_keys=True).encode()).hexdigest(),
        'native_command_originals':summaries,'raw_LF_only_sed_reconstructions':sed_count,'rg_multiset_reconstructions':rg_count,
        'fresh_raw_comparisons':comparisons,'original_scientific_pilots':1,'original_pilot_checks':124629,
        'original_states_targets':5408,'new_scientific_or_analysis_executions':0,'python_sources_parsed_only':parsed,
        'root_added_static_collision':'SMV = old QEF composed with input negation; not dynamical conjugacy',
        'independent_mathematical_review':False,'external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    main()
