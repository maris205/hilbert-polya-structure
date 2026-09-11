"""Seal only this assessor's package; preserve all prior scientific records."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def write_new(name,value):
    path=HERE/name
    assert not path.exists(), 'do not overwrite audit outputs'
    path.write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')

def main():
    before=[]
    for manifest in ('INPUT_PINS.sha256','HISTORY_PINS.sha256'):
        for line in (HERE/manifest).read_text().splitlines():
            expected,path=line.split('  ',1)
            actual=sha(ROOT/path)
            before.append({'manifest':manifest,'path':path,'expected':expected,'actual':actual,'pass':expected==actual})
    assert len(before)==149 and all(row['pass'] for row in before)
    runs=['initial_production_03','fresh_execution_01','fresh_execution_02']
    canonical=HERE/'CANONICAL.json'; canonical_before=sha(canonical)
    code_before=sha(HERE/'verify.py')
    recorder_before=sha(HERE/'record_execution.py')
    executable=Path(sys.executable).resolve(); interpreter_before=sha(executable)
    records={label:json.loads((HERE/label/'RECORD.json').read_text()) for label in runs}
    comparisons=[]
    names=[('fresh_execution_01/stdout.json','fresh_execution_02/stdout.json'),
           ('fresh_execution_01/stdout.json','CANONICAL.json'),
           ('fresh_execution_02/stdout.json','CANONICAL.json'),
           ('fresh_execution_01/stderr.txt','fresh_execution_02/stderr.txt'),
           ('fresh_execution_01/runtime.stdout','fresh_execution_02/runtime.stdout'),
           ('fresh_execution_01/runtime.stderr','fresh_execution_02/runtime.stderr'),
           ('fresh_execution_01/verify.py','fresh_execution_02/verify.py')]
    for index,(left,right) in enumerate(names,1):
        command=['/usr/bin/cmp',str(HERE/left),str(HERE/right)]
        completed=subprocess.run(command,cwd=HERE,capture_output=True)
        out=HERE/f'pair_cmp_{index:02d}.stdout'; err=HERE/f'pair_cmp_{index:02d}.stderr'
        assert not out.exists() and not err.exists()
        out.write_bytes(completed.stdout); err.write_bytes(completed.stderr)
        comparisons.append({'command':command,'exit':completed.returncode,'kind':'raw byte cmp',
                            'left_sha256':sha(HERE/left),'right_sha256':sha(HERE/right),
                            'stdout':out.name,'stderr':err.name})
        assert completed.returncode==0
    write_new('PAIR_COMPARISONS.json',comparisons)
    data=json.loads(canonical.read_text())
    assert data['total_assertions']==628980
    assert [row['states'] for row in data['rows']]==[1,2,5,14,42,132,429,1430]
    assert sum(row['states'] for row in data['rows'])==2055
    assert [row['n'] for row in data['rows']]==list(range(3,11))
    assert len(data['full_graph_and_source_sets'])==8
    full_count=sum(len(row['states']) for row in data['full_graph_and_source_sets'])
    assert full_count==2055
    census=json.loads((HERE/'FINDINGS.json').read_text())
    assert census['open_critical']==census['open_major']==0
    for label,record in records.items():
        assert record['exit']==record['runtime_exit']==0
        assert record['stdout_sha256']==canonical_before
        assert sha(HERE/label/'stdout.json')==canonical_before
        assert (HERE/label/'stderr.txt').read_bytes()==b''
        assert len(record['input_before'])==len(record['input_after'])==149
        assert all(row['pass'] for row in record['input_before']+record['input_after'])
        assert record['source_sha256_before']==record['source_sha256_after']==code_before
        assert record['copied_source_sha256_before']==record['copied_source_sha256_after']==code_before
        assert record['recorder_sha256_before']==record['recorder_sha256_after']==recorder_before
        assert record['interpreter_sha256_before']==record['interpreter_sha256_after']==interpreter_before
        assert sha(HERE/label/'verify.py')==code_before
        assert all(row['exit']==0 for row in record['comparisons'])
    assert records[runs[0]]['environment']==records[runs[1]]['environment']==records[runs[2]]['environment']
    after=[dict(row,actual=sha(ROOT/row['path']),pass_final=sha(ROOT/row['path'])==row['expected']) for row in before]
    assert all(row['pass_final'] for row in after)
    assert sha(canonical)==canonical_before and sha(HERE/'verify.py')==code_before
    assert sha(HERE/'record_execution.py')==recorder_before and sha(executable)==interpreter_before
    write_new('FINAL_REFERENTS.json',{'path_base':str(ROOT),'before':before,'after':after,
              'canonical_before':canonical_before,'canonical_after':sha(canonical),
              'code_before':code_before,'code_after':sha(HERE/'verify.py'),
              'interpreter':str(executable),'interpreter_before':interpreter_before,'interpreter_after':sha(executable),
              'recorded_runs':runs,'environment_equal':True})
    write_new('SEAL_AUDIT.json',{'scope':'ALL original n=3..10 only','full_state_records':full_count,
              'assertions_per_final_code_run':data['total_assertions'],'runs':runs,
              'canonical_sha256':canonical_before,'verify_sha256':code_before,
              'recorder_sha256':recorder_before,'input_referents_before_after':len(before),
              'actual_raw_comparisons':len(comparisons),'raw_comparison_exits':[row['exit'] for row in comparisons],
              'open_critical':0,'open_major':0,'verdict':census['candidate_value_verdict'],
              'status':'PASS','note':'Manifest is generated after this nonself audit; actual final manifest validation is a subsequent read-only command, not a self-referential receipt.'})
    manifest=HERE/'SHA256SUMS'
    assert not manifest.exists()
    paths=sorted(p for p in HERE.rglob('*') if p.is_file() and p!=manifest)
    assert not any(p.is_symlink() for p in paths)
    manifest.write_text(''.join(f'{sha(path)}  {path.relative_to(HERE).as_posix()}\n' for path in paths))
    manifest_before=sha(manifest)
    expected_paths={str(path.relative_to(HERE)) for path in paths}
    actual_paths={str(path.relative_to(HERE)) for path in HERE.rglob('*') if path.is_file() and path!=manifest}
    assert expected_paths==actual_paths
    command=['/usr/bin/sha256sum','-c','SHA256SUMS']
    result=subprocess.run(command,cwd=HERE,capture_output=True)
    assert result.returncode==0 and sha(manifest)==manifest_before
    print(json.dumps({'manifest_sha256':manifest_before,'manifest_nonself_files':len(paths),
                      'exact_fileset':True,'manifest_check_command':command,'manifest_check_exit':result.returncode,
                      'manifest_check_stdout':result.stdout.decode(),'manifest_check_stderr':result.stderr.decode(),
                      'canonical_sha256':canonical_before,'verify_sha256':code_before,'status':'PASS'},sort_keys=True,indent=2))

if __name__=='__main__': main()
