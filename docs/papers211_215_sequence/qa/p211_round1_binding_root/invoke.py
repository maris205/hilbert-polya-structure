"""One root-authorized physical Round1 invocation. No retry or science.

The recorder was completely source-received and the exact binding inspected.
Four documentary native commands place/compare the two starter files. The
separate recorder then supplies its own 119 operations. All failures and any
partial destination are retained. No preexisting destination is overwritten.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round1_binding_root'
CONTROL = HERE/'entry01'
EXEC = QA/'p211_round1_execution01'
SOURCE = QA/'p211_round1_adapter01/freeze.py'
BINDING = HERE/'selection01/BINDING_READY.json'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
SOURCE_PIN = {'bytes':35397,'sha256':'50c32a6fa4c703275cb55535bc56507ba5bdbb909fb57ed31ffc6d3ff9566ab2'}
BINDING_PIN = {'bytes':1550719,'sha256':'5bf3f123a1088ff73bf5812f8cb8b4fff36bacc321de7cb582f3a434e2393f5a'}


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def put(path, value):
    raw = value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with path.open('xb') as stream:
        stream.write(raw)


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def run(argv, target, label, timeout=60):
    need(not os.path.lexists(target/(label+'.ATTEMPT.json')), 'new literal command record')
    request = {'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
               'timeout_seconds':timeout,'started_epoch':time.time()}
    put(target/(label+'.ATTEMPT.json'),request)
    exit_code, exception, status = None, None, 'captured'
    try:
        result = subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,
                                capture_output=True,timeout=timeout)
        stdout,stderr,exit_code = result.stdout,result.stderr,result.returncode
    except subprocess.TimeoutExpired as exc:
        stdout,stderr = exc.stdout or b'',exc.stderr or b''
        exception = {'type':type(exc).__name__,'message':str(exc)}
        status = 'captured_partial_at_timeout; no exit code invented'
    except OSError as exc:
        stdout,stderr = b'',b''
        exception = {'type':type(exc).__name__,'message':str(exc)}
        status = 'not_launched; streams unavailable'
    put(target/(label+'.stdout.raw'),stdout)
    put(target/(label+'.stderr.raw'),stderr)
    native = {**request,'ended_epoch':time.time(),'native_exit_code':exit_code,
              'exception':exception,'stream_capture_status':status,
              'stdout':{'path':label+'.stdout.raw',**pin(stdout)},
              'stderr':{'path':label+'.stderr.raw',**pin(stderr)}}
    put(target/(label+'.NATIVE.json'),native)
    need(exception is None and exit_code == 0 and stderr == b'' and stdout == b'', ('native placement',label))
    return native


need(Path.cwd() == ROOT and not os.path.lexists(CONTROL) and not os.path.lexists(EXEC), 'exclusive new root attempt')
need(not os.path.lexists(ROOT/'papers/211-kernel-image-projection-feedback/frozen_round1'), 'new Round1 absent')
for path, expected in ((SOURCE,SOURCE_PIN),(BINDING,BINDING_PIN)):
    need(path.is_file() and path.resolve() == path and pin(path.read_bytes()) == expected, 'exact accepted source/binding')
binding = json.loads(BINDING.read_bytes())
need(binding['enabled'] is True and binding['root_authorization']['issuer'] == '/root'
     and binding['root_authorization']['decision'] == 'AUTHORIZE_PHYSICAL_P211_ROUND1_FROM_ACCEPTED_FINAL_A', 'root exact authorization')
need(binding['execution_source_pin'] == SOURCE_PIN and binding['execution_directory'] == str(EXEC.relative_to(ROOT)), 'literal bound destination')
# Final pre-entry ordinary input and selected directory membership checks.
# The recorder repeats these with rich keys and does the actual physical work.
for row in binding['external_inputs']:
    path = ROOT/row['physical_path']
    need(path.is_file() and path.resolve() == path and pin(path.read_bytes()) == row['pin'], ('exact external pre-entry',str(path)))
for tree in binding['external_trees']:
    base = ROOT/tree['root']
    actual_files, actual_dirs = set(), {'.'}
    for p in base.rglob('*'):
        need(p.resolve() == p and (p.is_dir() or p.is_file()), 'ordinary selected tree')
        (actual_dirs if p.is_dir() else actual_files).add(p.relative_to(base).as_posix())
    parents = {'.'}
    for name in tree['files']:
        parents.update(p.as_posix() for p in Path(name).parents)
    need(actual_files == set(tree['files']) and actual_dirs == parents, ('entire exact tree before invocation',str(base)))
CONTROL.mkdir()
put(CONTROL/'EXECUTED_CONTROLLER.py',Path(__file__).read_bytes())
put(CONTROL/'INPUT_PINS.json',{'source':SOURCE_PIN,'binding':BINDING_PIN,'controller':pin(Path(__file__).read_bytes())})
EXEC.mkdir()
for label, source, destination in [('source',SOURCE,EXEC/'freeze.py'),('binding',BINDING,EXEC/'BINDING.json')]:
    run(['/usr/bin/cp','-p','--',str(source),str(destination)],CONTROL,'copy_'+label)
    run(['/usr/bin/cmp','--',str(source),str(destination)],CONTROL,'compare_'+label)
    need(source.read_bytes() == destination.read_bytes(), 'full placement bytes')
argv = ['/usr/bin/python3.10','-I','-S','-B',str(EXEC/'freeze.py'),'--binding',str(EXEC/'BINDING.json')]
attempt = {'argv':argv,'cwd':str(ROOT),'environment':ENV,'source_pin':SOURCE_PIN,
           'binding_pin':BINDING_PIN,'started_epoch':time.time(),'stdin':'subprocess.DEVNULL'}
put(EXEC/'ROOT_INVOCATION_ATTEMPT.json',attempt)
native = {**attempt,'timeout_seconds':900}
exit_code, exception, status = None, None, 'captured'
try:
    result = subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,
                            capture_output=True,timeout=900)
    stdout,stderr,exit_code = result.stdout,result.stderr,result.returncode
except subprocess.TimeoutExpired as exc:
    stdout,stderr = exc.stdout or b'',exc.stderr or b''
    exception = {'type':type(exc).__name__,'message':str(exc)}
    status = 'captured_partial_at_timeout; no exit code invented'
except OSError as exc:
    stdout,stderr = b'',b''
    exception = {'type':type(exc).__name__,'message':str(exc)}
    status = 'not_launched; streams unavailable'
put(EXEC/'root.stdout.raw',stdout)
put(EXEC/'root.stderr.raw',stderr)
native.update({'ended_epoch':time.time(),'native_exit_code':exit_code,'exception':exception,
               'stream_capture_status':status,
               'stdout':{'path':'root.stdout.raw',**pin(stdout)},
               'stderr':{'path':'root.stderr.raw',**pin(stderr)}})
put(EXEC/'ROOT_INVOCATION_NATIVE.json',native)
files = []
for p in sorted(EXEC.rglob('*')):
    need(p.resolve() == p and (p.is_file() or p.is_dir()), 'ordinary completed attempt tree')
    if p.is_file():
        files.append(p)
put(EXEC/'SHA256SUMS',''.join(pin(p.read_bytes())['sha256']+'  '+p.relative_to(EXEC).as_posix()+'\n' for p in files).encode())
summary = {'native_exit_code':exit_code,'exception':exception,'stream_capture_status':status,
           'execution_payloads':len(files),'execution_manifest':pin((EXEC/'SHA256SUMS').read_bytes()),
           'outer_stdout':pin(stdout),'outer_stderr':pin(stderr),
           'physical_freeze_accepted':False,'scientific_executions':0}
put(CONTROL/'RESULT.json',summary)
print(json.dumps(summary,sort_keys=True))
need(exception is None and exit_code == 0 and stderr == b'', 'actual recorder invocation success; all failures preserved')
need(json.loads(stdout) == json.loads((EXEC/'RESULT.json').read_bytes()), 'whole actual recorder stdout/result equality')
