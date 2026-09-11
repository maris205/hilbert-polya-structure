"""Root full preparation integrity reception; imports no submitted program."""
import ast
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
REVIEW = ROOT/'docs/papers211_215_sequence/reviews/p211_a'
FREEZE = ROOT/'papers/211-kernel-image-projection-feedback/frozen_round0'
OUT = Path(__file__).resolve().parent
READS = {}
CHECKS = 0


def need(ok, why):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(why)


def raw(path):
    path = Path(path)
    need(path.is_file() and not path.is_symlink(), ('physical file', str(path)))
    data = path.read_bytes()
    if str(path) in READS:
        need(READS[str(path)] == data, ('unchanged read', str(path)))
    READS[str(path)] = data
    return data


def identity(data):
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def pin(path, expected=None):
    current = identity(raw(path))
    if expected is not None:
        expected = {'sha256': expected} if isinstance(expected, str) else expected
        need(all(current[k] == v for k, v in expected.items()), ('exact pin', str(path)))
    return current


def doc(path):
    return json.loads(raw(path))


def pins(path, base):
    result = {}
    for line in raw(path).decode().splitlines():
        match = re.fullmatch(r'([a-f0-9]{64})  (.+)', line)
        need(match is not None, ('pin syntax', str(path)))
        digest, name = match.groups()
        relative = Path(name)
        need(not relative.is_absolute() and '..' not in relative.parts and name not in result,
             ('safe unique path', name))
        result[name] = pin(base/name, digest)
    return result


def tool(value):
    need(value['exit_code'] == 0 and not value.get('session_id'), 'actual complete successful tool boundary')
    need(isinstance(value['output'], str), 'whole saved tool output')
    return value['output']


def write(name, value):
    with (OUT/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode())


seal = pin(REVIEW/'PREPARATION_SHA256SUMS', '67b61e77cca2195f264902e54fedb5688ca39d1c3b649282f3306c1172519a07')
payloads = pins(REVIEW/'PREPARATION_SHA256SUMS', REVIEW)
actual = sorted(p.relative_to(REVIEW).as_posix() for p in REVIEW.rglob('*') if p.is_file())
need(actual == sorted(list(payloads)+['PREPARATION_SHA256SUMS']) and len(payloads) == 20,
     'entire 20-payload preparation inventory, no invented later roles')
frozen = pins(REVIEW/'INPUT_PINS.sha256', ROOT)
external = pins(REVIEW/'EXTERNAL_READ_PINS.sha256', ROOT)
need(len(frozen) == 33 and len(external) == 32, 'whole distinct input populations')
need(set(frozen) == {p.relative_to(ROOT).as_posix() for p in FREEZE.rglob('*') if p.is_file()},
     'every exact physical frozen input including manifest')
frozen_manifest = pins(FREEZE/'SHA256SUMS', FREEZE)
need(len(frozen_manifest) == 32, 'all frozen nonself payloads')
pin(FREEZE/'SHA256SUMS', '459459486a82c8f787d04e5e7fcb81e6c01b3abef320d1e82ea4cbb30ea8a8bd')
need(tool(doc(REVIEW/'evidence/EXTERNAL_PIN_TOOL_RETURN.json')).encode() == raw(REVIEW/'EXTERNAL_READ_PINS.sha256'),
     'whole external native pin stream')
freeze_tools = doc(REVIEW/'evidence/FREEZE_PIN_TOOL_RETURN.json')
need(tool(freeze_tools['pin_command']).encode() == raw(REVIEW/'INPUT_PINS.sha256'), 'whole frozen pin stream')
need(tool(freeze_tools['manifest_command']) == pin(FREEZE/'SHA256SUMS')['sha256']+'  '+str((FREEZE/'SHA256SUMS').relative_to(ROOT))+'\n',
     'whole initial freeze manifest native stream')
rechecks = doc(REVIEW/'evidence/INPUT_RECHECK_TOOL_RETURNS.json')['records']
need(len(rechecks) == 2, 'both complete actual pin rechecks')
for record, name in zip(rechecks, ('INPUT_PINS.sha256', 'EXTERNAL_READ_PINS.sha256')):
    need(record['command'] == 'sha256sum --check --strict '+str((REVIEW/name).relative_to(ROOT))
         and record['working_directory'] == str(ROOT), 'exact recheck command/cwd')
    names = [line.split('  ', 1)[1] for line in raw(REVIEW/name).decode().splitlines()]
    need(tool(record['actual_tool_result']) == ''.join(p+': OK\n' for p in names), 'all native recheck lines')
own = doc(REVIEW/'evidence/BUILD_REUSE_RESULT01.json')
own_native = tool(doc(REVIEW/'evidence/BUILD_REUSE_TOOL_RETURN01.json'))
root_native = doc(OUT/'BUILD_REUSE_NATIVE01.json')
need(root_native['request']['cmd'] == '/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/reviews/p211_a/inspect_build_reuse.py'
     and root_native['request']['workdir'] == str(ROOT), 'explicit root whole-checker reuse request')
need(own_native == tool(root_native['result']) and json.loads(own_native) == own,
     'complete actual 5974-check result and all full-key fields exactly equal')
need(own['checks'] == 5974 and own['prior_read_key_entries_checked_twice'] == 1299
     and own['configuration_entries_checked_twice'] == 843, 'accepted full build reuse scope')
pin(REVIEW/'inspect_build_reuse.py', own['executed_checker']['pin'])
need(own['executed_checker']['path'] == str(REVIEW/'inspect_build_reuse.py'), 'actual reused checker locator')
sources = []
for index in range(1, 5):
    path = REVIEW/'sources'/('web'+str(index).zfill(2)+'.json')
    value = doc(path)
    need(isinstance(value, str) and 'Source: open(' in value and 'Total lines:' in value,
         'actual full browser return string, not guessed dictionary')
    sources.append({'path': str(path), **pin(path), 'decoded_characters': len(value)})
navigation = doc(REVIEW/'evidence/NAVIGATION_FAILURES.json')
need(len(navigation['failures']) == 3 and navigation['failures'][0]['exit_code'] == 127,
     'preserved navigation/read-scope failures')
source = pin(REVIEW/'verify.py', '35140051d98c1adcc14ca0041407f1a07a0488bb40a9962fa586ac517c0a389a')
parameters_pin = pin(REVIEW/'parameters.json', 'a12bcbda054a0a6a8cfc6ebd774e70ff8df4318dd7d902e0724a6d84212e78cc')
tree = ast.parse(raw(REVIEW/'verify.py'))
need([node.names[0].name for node in tree.body if isinstance(node, ast.Import)] == ['itertools', 'json', 'math', 'sys'], 'static ordinary import list')
need(not any(isinstance(node, ast.ImportFrom) for node in ast.walk(tree)), 'no from/local imports')
assignment = [node for node in tree.body if isinstance(node, ast.Assign)
              and isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'EXPECTED_PARAMETERS']
parameters = doc(REVIEW/'parameters.json')
need(len(assignment) == 1 and ast.literal_eval(assignment[0].value) == parameters, 'literal exact parameter object')
need(parameters['n_values'] == list(range(1, 8)) and parameters['expected_total_vertices'] == 2353,
     'original seven full carriers, no expanded cutoff')
pin(__file__)
for path, data in READS.items():
    need(Path(path).read_bytes() == data, ('all consumed inputs unchanged', path))
write('PREPARATION_READ_INPUTS.json', {p: identity(data) for p, data in READS.items()})
result = {'status': 'PASS_ROOT_A_PREPARATION_ORIGINALS', 'checks': CHECKS,
          'actual_read_paths': len(READS), 'payloads': len(payloads),
          'payload_bytes': sum(p['bytes'] for p in payloads.values()), 'preparation_manifest': seal,
          'complete_frozen_inputs': len(frozen), 'complete_external_inputs': len(external),
          'capsule': {'source': source, 'parameters': parameters_pin}, 'fresh_browser_returns': sources,
          'full_build_reuse_checks': own['checks'], 'full_build_result_equal': True,
          'scientific_execution_or_import': False, 'canonical_absent': not (REVIEW/'CANONICAL.json').exists(),
          'scope': 'Whole preparation and actual records received; manuscript verdict and exact initial production remain distinct.'}
write('PREPARATION_RESULT.json', result)
print(json.dumps(result, sort_keys=True))
