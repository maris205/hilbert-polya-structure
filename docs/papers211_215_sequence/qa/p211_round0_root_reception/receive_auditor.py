#!/usr/bin/python3.10
"""Receive the sealed independent audit and bind the actual root recheck."""
from pathlib import Path
from hashlib import sha256
import json
import re
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round0_root_reception'
OTHER = QA/'p211_round0_independent_reception'
FREEZE = QA/'p211_round0_execution01'
reads = {}
checks = 0

def need(value, label):
    global checks
    checks += 1
    assert value, label

def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def read(path):
    path = Path(path)
    raw = path.read_bytes()
    need(str(path) not in reads or reads[str(path)] == pin(raw), ('drift',str(path)))
    reads[str(path)] = pin(raw)
    return raw

def obj(path):
    return json.loads(read(path))

def save(name, value):
    raw = value if isinstance(value, bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (HERE/name).open('xb') as stream:
        stream.write(raw)

read(Path(__file__))
manifest = read(OTHER/'SHA256SUMS')
need(pin(manifest) == {'bytes':706,'sha256':'c30ba21f855e71e49c9ca46da539ba01902c90f261dcd7ecfbfeeed6357e5f8c'}, 'announced final independent manifest')
names = []
for line in manifest.decode().splitlines():
    match = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
    need(match is not None,'manifest syntax')
    digest,name = match.groups()
    need(not Path(name).is_absolute() and '..' not in Path(name).parts and name != 'SHA256SUMS' and name not in names,'nonself safe unique')
    names.append(name)
    need(pin(read(OTHER/name))['sha256'] == digest,('independent payload',name))
need(len(names) == 8,'eight independent payloads')
need(sorted(names+['SHA256SUMS']) == sorted(str(p.relative_to(OTHER)) for p in OTHER.rglob('*') if p.is_file()),'whole final independent package')

keys = []
for base in [OTHER,HERE]:
    before,after = obj(base/'run01/READ_INPUTS_BEFORE.json'),obj(base/'run01/READ_INPUTS_AFTER.json')
    need(before == after and len(before) == 895,'complete before/after key')
    for path,value in before.items():
        need(pin(read(path)) == value,('actual current audited bytes',path))
    keys.append(before)
    for directory,names_here in obj(base/'run01/INVENTORIES.json').items():
        need(sorted(names_here) == sorted(str(p.relative_to(directory)) for p in Path(directory).rglob('*') if p.is_file()),('complete unchanged selected inventory',directory))
need(set(keys[0])-set(keys[1]) == {str(OTHER/'audit_round0.py')} and set(keys[1])-set(keys[0]) == {str(HERE/'audit_round0.py')},'exact distinct executed checker self paths')
need(all(keys[0][p] == keys[1][p] for p in set(keys[0]) & set(keys[1])),'same exact 894 shared original inputs')
need(read(OTHER/'run01/HISTORICAL_READ_ROUTES.json') == read(HERE/'run01/HISTORICAL_READ_ROUTES.json'),'same explicit two historical routes')
need(read(OTHER/'run01/INVENTORIES.json') == read(HERE/'run01/INVENTORIES.json'),'same exact selected inventories')
original, reused = read(OTHER/'audit_round0.py'),read(HERE/'audit_round0.py')
old = b"HERE = QA / 'p211_round0_independent_reception'"
new = b"HERE = QA / 'p211_round0_root_reception'"
need(original.count(old) == 1 and reused == original.replace(old,new),'only disclosed destination change')
request = {'argv':['/usr/bin/diff','-u','--',str(OTHER/'audit_round0.py'),str(HERE/'audit_round0.py')], 'cwd':str(ROOT), 'environment':{'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}}
save('AUDITOR_DIFF_ATTEMPT.json',request)
actual = subprocess.run(request['argv'],cwd=ROOT,env=request['environment'],capture_output=True,timeout=60)
save('AUDITOR_DIFF.stdout.raw',actual.stdout)
save('AUDITOR_DIFF.stderr.raw',actual.stderr)
save('AUDITOR_DIFF_NATIVE.json',{'request':request,'exit_code':actual.returncode,'stdout':pin(actual.stdout),'stderr':pin(actual.stderr)})
need(actual.returncode == 1 and actual.stderr == b'','actual disclosed-source diff')
changed = [line for line in actual.stdout.splitlines() if line[:1] in [b'-',b'+'] and not line.startswith((b'---',b'+++'))]
need(changed == [b'-'+old,b'+'+new],'complete actual diff content')

records = obj(OTHER/'TOOL_RECORDS.json')['records']
need(len(records) == 6 and len({r['id'] for r in records}) == 6,'all actual audit tool records')
by_id = {r['id']:r for r in records}
need(by_id['root-freezer-code-read']['returned']['output'].encode() == read(FREEZE/'freeze.py'),'complete native freezer source read')
parts = ['ROOT_AUTHORIZATION.md','RESULT.json','NATIVE01.json']
need(by_id['root-authorization-result-native-read']['returned']['output'].encode() == b''.join(read(FREEZE/name) for name in parts),'complete native root prerequisites read')
launch,completion = by_id['independent-audit-launch'],by_id['independent-audit-completion']
need(launch['returned']['session_id'] == completion['request']['session_id'] and launch['returned']['output'] == '' and completion['returned']['exit_code'] == 0,'actual complete audit launch/completion')
independent_result = obj(OTHER/'run01/RESULT.json')
need(json.loads(completion['returned']['output']) == independent_result,'actual native independent result')
need(launch['request']['cmd'].endswith('p211_round0_independent_reception/audit_round0.py --output run01'),'independent executed command')
root_native = obj(HERE/'NATIVE01.json')
need(root_native['result']['exit_code'] == 0 and root_native['request']['cmd'].endswith('p211_round0_root_reception/audit_round0.py --output run01'),'actual root successful invocation')
need(json.loads(root_native['result']['output']) == obj(HERE/'run01/RESULT.json') == independent_result,'both complete actual result objects')
need(independent_result['checks'] == 33244 and independent_result['scientific_executions'] == 0 and independent_result['manuscript_reviews'] == 0,'bounded non-scientific reception')
for path,value in list(reads.items()):
    need(pin(Path(path).read_bytes()) == value,('all consumed bytes still unchanged',path))
result = {'status':'PASS_ROUND0_ROOT_ORIGINAL_RECEPTION','checks':checks,'read_paths':len(reads),'independent_payloads':8,'auditor_key_entries':895,'common_original_keys':894,'distinct_executed_checker_paths':2,'complete_native_results_bound':2,'new_scientific_runs':0,'new_manuscript_reviews':0,'new_builds':0,'new_page_views':0,'independent_method_reused_for_root_recheck':True,'open_blocking_findings':0,'external':'HOLD_EXTERNAL'}
save('AUDITOR_INPUTS.json',reads)
save('AUDITOR_RESULT.json',result)
print(json.dumps(result,sort_keys=True))
