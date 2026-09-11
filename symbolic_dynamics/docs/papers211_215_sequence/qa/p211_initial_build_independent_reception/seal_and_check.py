#!/usr/bin/python3.10
"""One new documentary nonself seal after the actual auditor has completed.

Only this exact new QA directory is writable. Does not rerun the audit,
builder or scientific code. The final product tool return is handed to root
outside the seal, avoiding a circular in-package completion claim.
"""
from hashlib import sha256
import json
from pathlib import Path

HERE = Path('/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_initial_build_independent_reception')


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def data(path):
    return json.loads(path.read_bytes())


assert Path(__file__).resolve()==HERE/'seal_and_check.py'
assert not (HERE/'SHA256SUMS').exists() and not (HERE/'PACKAGE_CHECK.json').exists()
run=HERE/'run01'
source=(HERE/'inspect_build.py').read_bytes()
assert source==(run/'executed_checker.py').read_bytes()
result=data(run/'RESULT.json')
assert result['status']=='INDEPENDENT_INITIAL_BUILD_EVIDENCE_PASS_PENDING_ROOT_RECEPTION'
assert result['failure'] is None and result['auditor_source']==pin(source)
assert (run/'READ_INPUTS_BEFORE.json').read_bytes()==(run/'READ_INPUTS_AFTER.json').read_bytes()
run_rows={}
for line in (run/'SHA256SUMS').read_text().splitlines():
    digest,name=line.split('  ',1)
    assert name not in run_rows and name!='SHA256SUMS' and not Path(name).is_absolute() and '..' not in Path(name).parts
    assert sha256((run/name).read_bytes()).hexdigest()==digest
    run_rows[name]=digest
assert set(run_rows)=={p.relative_to(run).as_posix() for p in run.rglob('*') if p.is_file()}-{'SHA256SUMS'}
launch=data(HERE/'TOOL_LAUNCH01.actual.json')
completion=data(HERE/'TOOL_COMPLETION01.actual.json')
assert launch['launch']['session_id']==completion['request']['session_id']==58839
assert launch['launch']['output']=='' and 'exit_code' not in launch['launch']
assert completion['completion']['exit_code']==0
expected={**result,'run':str(run),'seal':{'payloads':len(run_rows),'manifest':pin((run/'SHA256SUMS').read_bytes())}}
assert completion['completion']['output']==json.dumps(expected,sort_keys=True)+'\n'
assert launch['request']['cmd'].endswith(' '+str(HERE/'inspect_build.py')+' run01')
checks={'status':'ACTUAL_AUDITOR_COMPLETION_AND_RUN_SEAL_VERIFIED',
        'run_payloads':len(run_rows),'auditor_result':pin((run/'RESULT.json').read_bytes()),
        'executed_source':pin(source),'actual_product_session':58839,
        'actual_exit_code':0,'input_inventories_raw_equal':True,
        'new_audit_execution':False,'new_build':False,'new_science':False,
        'scope':'Documentary sealing after actual checker completion; not a new scientific or build run'}
with (HERE/'PACKAGE_CHECK.json').open('xb') as stream:
    stream.write((json.dumps(checks,sort_keys=True,indent=2)+'\n').encode())
files={}
for p in sorted(HERE.rglob('*')):
    assert not p.is_symlink()
    if p.is_file():
        files[p.relative_to(HERE).as_posix()]=pin(p.read_bytes())
raw=''.join(value['sha256']+'  '+name+'\n' for name,value in files.items()).encode()
with (HERE/'SHA256SUMS').open('xb') as stream:
    stream.write(raw)
assert set(files)=={p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()}-{'SHA256SUMS'}
assert all(pin((HERE/name).read_bytes())==value for name,value in files.items())
assert (HERE/'SHA256SUMS').read_bytes()==raw
print(json.dumps({'status':'COMPLETE_NEW_ONLY_NONSELF_SEAL_VERIFIED','payloads':len(files),
                  'payload_bytes':sum(v['bytes'] for v in files.values()),'manifest':pin(raw),
                  'files_including_manifest':len(files)+1,
                  'bytes_including_manifest':sum(v['bytes'] for v in files.values())+len(raw)},sort_keys=True))
