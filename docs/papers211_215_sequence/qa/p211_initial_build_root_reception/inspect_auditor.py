#!/usr/bin/python3.10
"""Root receives the complete independent audit and its disclosed code reuse."""
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
AUD = HERE.parent / 'p211_initial_build_independent_reception'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
reads = {}
checks = 0


def need(value, label):
    global checks
    checks += 1
    assert value, label


def identity(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def read(p):
    p = Path(p)
    raw = p.read_bytes()
    need(str(p) not in reads or reads[str(p)] == identity(raw), ('drift',str(p)))
    reads[str(p)] = identity(raw)
    return raw


def obj(p):
    return json.loads(read(p))


def put(name, value):
    raw = value if isinstance(value, bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (HERE/name).open('xb') as stream:
        stream.write(raw)


def seal(base):
    rows = {}
    for line in read(base/'SHA256SUMS').decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(match is not None, ('syntax',base))
        digest,name = match.groups()
        need(name not in rows and name != 'SHA256SUMS' and not Path(name).is_absolute() and '..' not in Path(name).parts, name)
        p = base/name
        need(p.resolve() == p and not p.is_symlink(), ('physical',name))
        need(sha256(read(p)).hexdigest() == digest, ('hash',name))
        rows[name] = digest
    need(set(rows) == {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()}-{'SHA256SUMS'}, ('complete',base))
    return {'payloads':len(rows),'manifest':identity(read(base/'SHA256SUMS'))}


need(Path.cwd() == ROOT, 'cwd')
independent = seal(AUD)
need(independent == {'payloads':18,'manifest':{'bytes':1615,'sha256':'53ad4467c84d0e06b72f6e0194ae4b0eedb7d90cf3599d24c082746df82fa57f'}}, 'exact final independent package')
old = read(AUD/'inspect_build.py')
new = read(HERE/'inspect_build.py')
need(old == read(AUD/'run01/executed_checker.py') and new == read(HERE/'run01/executed_checker.py'), 'exact executed sources')
need(old.replace(b"HERE = QA / 'p211_initial_build_independent_reception'",b"HERE = QA / 'p211_initial_build_root_reception'").replace(b"(HERE/'SCOPE.md',ROOT/",b"(QA/'p211_initial_build_independent_reception/SCOPE.md',ROOT/") == new, 'only root output/scope routing replacements')
argv = ['/usr/bin/diff','-u',str(AUD/'inspect_build.py'),str(HERE/'inspect_build.py')]
native = subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=30)
put('AUDITOR_DIFF_STDOUT.raw',native.stdout)
put('AUDITOR_DIFF_STDERR.raw',native.stderr)
put('AUDITOR_DIFF_NATIVE.json',{'argv':argv,'cwd':str(ROOT),'environment':ENV,'native_exit_code':native.returncode,'stdout':identity(native.stdout),'stderr':identity(native.stderr)})
need(native.returncode == 1 and native.stderr == b'', 'exact routing diff')
results = []
for base in (AUD,HERE):
    run = base/'run01'
    manifest = seal(run)
    result = obj(run/'RESULT.json')
    need(result['status'] == 'INDEPENDENT_INITIAL_BUILD_EVIDENCE_PASS_PENDING_ROOT_RECEPTION' and result['failure'] is None and result['inputs_equal'], 'actual successful audit')
    need(result['checks'] == 26316 and result['read_paths'] == 1299, 'complete audit counts')
    before = obj(run/'READ_INPUTS_BEFORE.json')
    need(before == obj(run/'READ_INPUTS_AFTER.json'), 'all saved keys equal')
    for p,value in before.items():
        need(identity(read(p)) == value, ('actual full input',p))
    results.append((result,manifest))
    if base == AUD:
        launch = obj(base/'TOOL_LAUNCH01.actual.json')
        end = obj(base/'TOOL_COMPLETION01.actual.json')
        need(launch['launch']['session_id'] == end['request']['session_id'] == 58839, 'independent session')
        completion = end['completion']
    else:
        native_tool = obj(base/'NATIVE01.json')
        need(native_tool['result']['session_id'] == native_tool['polls'][0]['request']['session_id'] == 57016, 'root session')
        completion = native_tool['polls'][0]['result']
    need(completion['exit_code'] == 0 and completion['output'] == json.dumps({**result,'run':str(run),'seal':manifest},sort_keys=True)+'\n', 'actual full result/seal completion')
need(read(AUD/'run01/INDEPENDENT_ORDERED_IO_RECONSTRUCTION.json') == read(HERE/'run01/INDEPENDENT_ORDERED_IO_RECONSTRUCTION.json'), 'all rebuilt ordered FLS/BibTeX raw bytes equal')
need(obj(AUD/'FINDINGS.json')['current_open_counts'] == {'Critical':0,'Major':0,'Minor':0}, 'no new infrastructure findings')
native_seal = obj(HERE/'INDEPENDENT_SEAL_NATIVE.json')['response']
need(native_seal['exit_code'] == 0 and json.loads(native_seal['output']) == {'bytes_including_manifest':2468926,'files_including_manifest':19,'manifest':independent['manifest'],'payload_bytes':2467311,'payloads':18,'status':'COMPLETE_NEW_ONLY_NONSELF_SEAL_VERIFIED'}, 'actual independent documentary seal')
for p,value in list(reads.items()):
    need(identity(Path(p).read_bytes()) == value, ('final closure',p))
put('AUDITOR_READ_INPUTS.json',reads)
result = {'status':'ROOT_RECEIVES_COMPLETE_INDEPENDENT_BUILD_AUDIT_AND_DISCLOSED_ROOT_RECHECK',
          'checks':checks,'read_paths':len(reads),'independent_package':independent,
          'independent_checks':results[0][0]['checks'],'root_recheck_checks':results[1][0]['checks'],
          'root_reuses_reviewed_auditor_code_with_two_path_replacements':True,
          'scientific_executions':0,'new_builds':0,'manuscript_reviews':0}
put('AUDITOR_RESULT.json',result)
print(json.dumps(result,sort_keys=True))
