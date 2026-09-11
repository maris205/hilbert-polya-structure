#!/usr/bin/python3.10
"""New read-only infrastructure evidence checker; never evaluates submitted code.

Only named preparation artifacts and controls are read. Referenced TeX,
scientific, canonical, old-builder and host dependency paths are not followed.
"""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers211_215_sequence/qa/p211_build_preparation'
OUT = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
ENV8 = {**ENV, 'SOURCE_DATE_EPOCH': '1788825600', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
NAMES = ['build_core.py', 'prepare_build.py', 'build_p211.py', 'launch_build.py', 'static_checks.py']
controls = [ROOT / p for p in ('.agents/skills/symbolic-dynamics-research/SKILL.md',
    'docs/research_state/WORKFLOW.md', 'SYMBOLIC_DYNAMICS_STATE.md',
    'docs/papers211_215_sequence/PIPELINE_STATE.md', 'docs/papers211_215_sequence/PROBLEM_ANCHOR.md',
    'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md')]
controls.append(Path('/root/autodl-tmp/.codex/skills/paper-compile/SKILL.md'))
selected = set(controls + [PREP / p for p in NAMES + ['README.md', 'BINDING.pending.json', 'SHA256SUMS', 'DOCUMENTARY_AUDIT.json']])
for name in ('discovery05', 'diagnostic_capture05', 'history/diagnostic01_source'):
    selected.update(p for p in (PREP / name).rglob('*') if p.is_file())
reads, checks, native = {}, [], []


def value(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def read(p):
    assert p in selected and p.is_file() and not p.is_symlink(), ('read scope/type', str(p))
    raw = p.read_bytes()
    row = value(raw)
    if str(p) in reads:
        assert reads[str(p)] == row, ('read drift', str(p))
    reads[str(p)] = row
    return raw


def data(p):
    return json.loads(read(p))


def write(name, raw):
    p = OUT / name
    assert p.is_relative_to(OUT)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('xb') as stream:
        stream.write(raw)


def dump(name, row):
    write(name, (json.dumps(row, sort_keys=True, indent=2) + '\n').encode())


def check(test, label):
    if not test:
        raise AssertionError(label)
    checks.append(label)


def manifest(p, full):
    raw = read(p)
    assert raw.endswith(b'\n')
    entries = {}
    for line in raw.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert m, ('manifest syntax', str(p))
        digest, name = m.groups()
        assert name not in entries and name != 'SHA256SUMS' and not Path(name).is_absolute() and '..' not in Path(name).parts
        entries[name] = digest
    if full:
        inventory = {q.relative_to(p.parent).as_posix() for q in p.parent.rglob('*') if q.is_file()}
        check(inventory == set(entries) | {'SHA256SUMS'}, 'complete manifest inventory ' + str(p))
    count = 0
    for name, digest in entries.items():
        q = p.parent / name
        if q in selected:
            check(value(read(q))['sha256'] == digest, 'selected payload digest ' + str(q))
            count += 1
        elif full:
            raise AssertionError(('unselected complete payload', str(q)))
    return {'declared': len(entries), 'independently_verified_selected': count}


for p in sorted(selected):
    read(p)
dump('READ_INPUTS_BEFORE.json', reads)
check(value(read(PREP / 'SHA256SUMS'))['sha256'] == '5fa2620b27e04f0d07f9b72434f801a948e95d7df884d2e46a915c42028bd042', 'original preparation pin')
lock_path = PREP / 'discovery05/DEPENDENCY_LOCK.candidate.json'
check(value(read(lock_path))['sha256'] == '4c66d15e0720bb064fe890c81d531d2400b99891e7f59e537a42657c685d31e6', 'candidate lock pin')
manifests = {'top_selected_only': manifest(PREP / 'SHA256SUMS', False)}
check(manifests['top_selected_only']['declared'] == 891, 'top manifest 891 payloads')
for folder in ('discovery05', 'diagnostic_capture05'):
    manifests[folder] = manifest(PREP / folder / 'SHA256SUMS', True)

lock = data(lock_path)
check(lock['schema'] == 'p211-bounded-dependency-candidate-v1' and lock['status'] == 'CANDIDATE_ONLY_PENDING_ROOT_BINDING', 'candidate scope')
check(lock['environment'] == ENV8 and 'HOME' not in lock['environment'], 'exact ENV8 without HOME')
check(len(lock['entries']) == 840 and sum(v.get('kind') == 'file' for v in lock['entries'].values()) == 795, '840 paths 795 file entries')
check(set(lock['entries']) == set(lock['selector_specs']) == set(lock['selection_reasons']), 'complete selector/key/reason relationship')
check(len(lock['ldd_elf_inputs']) == 33 and all(p in lock['entries'] for p in lock['ldd_elf_inputs']), '33 selected ELF inputs covered')
check(lock['entries'] == data(PREP / 'discovery05/CONFIGURATION_AFTER_SELECTION.json'), 'complete saved configuration closure')
check(lock['code_observations'] == data(PREP / 'discovery05/CODE_BEFORE.json') == data(PREP / 'discovery05/CODE_AFTER.json'), 'saved current code closure')
check(lock['source_observations'] == data(PREP / 'discovery05/SOURCES_BEFORE.json') == data(PREP / 'discovery05/SOURCES_AFTER.json'), 'saved nine-source metadata closure')
check(len(lock['source_observations']) == 9, 'nine source metadata entries, not independently read TeX')
for name in NAMES:
    check(value(read(PREP / name)) == lock['code_observations'][name] ==
          value(read(PREP / 'diagnostic_capture05/executed_adapter' / name)), 'actual current/snapshot/code-key equality ' + name)
check(data(PREP / 'BINDING.pending.json')['status'] == 'PENDING_ROOT_BINDING', 'pending remains disabled')
roots = lock['cwd_relative_absence_roles']
check(set(roots) == {'TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR'} and
      {v['relative'] for v in roots.values()} == {'texmf', '.texlive2021/texmf-config', '.texlive2021/texmf-var'} and
      all(v['required_state'] == 'ABSENT' and not v['diagnostic_entry']['present'] for v in roots.values()), 'exact three cwd-relative ABSENT roles')
check(lock['queries']['explicit_graph_seeds']['resolutions']['amsart.cfg'] == [] and
      len(lock['queries']['explicit_graph_seeds']['resolutions']['amsplain.bst']) == 1 and
      len(lock['queries']['explicit_graph_seeds']['resolutions']['amsart.cls']) == 1, 'optional AMS cfg absent and selected AMS class/style unique')
for key in ('explicit_graph_seeds', 'literal_fd_metrics', 'selected_font_map_files'):
    query = lock['queries'][key]
    check(set(query['names']) == set(query['resolutions']), 'complete lookup keys ' + key)
    check(all(p in lock['entries'] and lock['entries'][p].get('kind') == 'file' for paths in query['resolutions'].values() for p in paths), 'selected lookup paths covered ' + key)
check(len(lock['queries']['literal_fd_metrics']['names']) == 173 and len(lock['queries']['selected_font_map_files']['names']) == 115, '173 metrics and 115 mapped font/encoding names')
query_labels = list(lock['queries'])
for key in query_labels:
    folder = PREP / 'discovery05/commands' / key
    receipt = data(folder / 'RECEIPT.json')
    check(receipt['argv'] == lock['query_commands'][key], 'literal saved query argv ' + key)
    raw = read(folder / 'stdout.raw').decode()
    if isinstance(lock['queries'][key], str):
        check(raw.strip().replace(str(PREP / 'discovery05'), '{COMMAND_CWD}') == lock['queries'][key], 'literal query output binding ' + key)
    else:
        result = {name: [] for name in lock['queries'][key]['names']}
        for line in raw.splitlines():
            result[Path(line).name].append(line)
        check(result == lock['queries'][key]['resolutions'], 'full original lookup resolutions ' + key)

archived = []
for p in sorted(q for q in selected if q.name == 'RECEIPT.json'):
    receipt = data(p)
    attempt = data(p.with_name('ATTEMPT.json'))
    check(all(receipt[k] == v for k, v in attempt.items()), 'literal attempt/receipt fields ' + str(p))
    check(receipt['environment'] == ENV8 and receipt['streams_settled'] and
          receipt['remaining_session_members'] == [] and receipt['owned_session_interventions'] == [] and
          receipt['successful'] and receipt['error'] is None, 'saved successful real native settlement ' + str(p))
    spawned = data(p.with_name('SPAWNED.json'))
    check(spawned['pid'] == spawned['session'] and
          attempt['attempted_epoch'] <= spawned['spawned_epoch'] <= receipt['ended_epoch'], 'saved spawned identity/epochs ' + str(p))
    check(receipt['direct_inputs_equal'] and data(p.with_name('INPUTS_BEFORE.json')) == data(p.with_name('INPUTS_AFTER.json')), 'native direct input closure ' + str(p))
    for stream in ('stdout.raw', 'stderr.raw'):
        check(value(read(p.with_name(stream))) == receipt['streams'][stream], 'complete raw stream ' + str(p) + ':' + stream)
    archived.append({'path': p.relative_to(PREP).as_posix(), 'argv': receipt['argv'],
                     'native_exit_code': receipt['native_exit_code'], 'streams': receipt['streams']})
check(len(archived) == 32, '32 final discovery/capture native receipts')
static = data(PREP / 'diagnostic_capture05/commands/static/stdout.raw')
check(static['status'] == 'STATIC_ONLY_NO_BUILD' and static['native_children'] == 0 and
      len(static['checks']) == 11 and all(v['passed'] for v in static['checks']), 'saved eleven static predicate groups, not executed here')
check(data(PREP / 'diagnostic_capture05/RESULT.json')['status'] == 'DIAGNOSTICS_RECORDED_NO_BUILD', 'saved capture status')

# Mechanically inspect the reported control-flow defect without evaluating it.
trees = {name: ast.parse(read(PREP / name), filename=str(PREP / name)) for name in NAMES}
fn = next(n for n in trees['build_core.py'].body if isinstance(n, ast.FunctionDef) and n.name == 'run_native')
spawning_try = next(n for n in fn.body if isinstance(n, ast.Try))
handler = next(n for n in spawning_try.handlers if isinstance(n.type, ast.Name) and n.type.id == 'BaseException')
check(len(handler.body) == 1 and isinstance(handler.body[0], ast.Assign), 'BLD-I1 catch changes only reason/error assignment')
check('settled, members, interventions = True, [], []' in read(PREP / 'build_core.py').decode(), 'BLD-I1 settled defaults true before spawn')
check('if proc is not None:' in read(PREP / 'build_core.py').decode() and
      'if not settled:' in read(PREP / 'build_core.py').decode(), 'BLD-I1 settlement skipped with no returned handle')
witness = {'finding': 'BLD-I1', 'severity': 'Major', 'status': 'OPEN_BLOCKS_CURRENT_BINDING',
           'method': 'Static control-flow witness only; no submitted function or mock of it was executed.',
           'premise': 'A non-OSError interruption/exception occurs during Popen before assignment returns; proc remains None. No returned handle does not establish absence of a native writer.',
           'path': ['build_core.py:211-212: proc=None and settled=True',
                    'build_core.py:220-230: BaseException handler assigns only reason/error; proc remains None',
                    'build_core.py:231: no-handle branch skips session inspection and settlement',
                    'build_core.py:258-272: streams_settled=True, raw stream hashes and RECEIPT are written despite unknown outcome',
                    'build_core.py:276-289: receipt exists and UNCLOSED is absent, so enclosing FAIL_PRESERVED seal is not blocked'],
           'impact': 'Not a false successful-build status; unsupported finalized raw/failed-artifact immutability claim.',
           'submitted_function_lines': [fn.lineno, fn.end_lineno],
           'catch_source': ast.get_source_segment(read(PREP / 'build_core.py').decode(), handler),
           'required_delta': 'Preserve an unknown/unclosed no-handle outcome with no final stream hashes or native receipt, prevent every enclosing seal, and add a focused non-scientific regression before a new candidate/binding.'}
dump('STATIC_BRANCH_WITNESS.json', witness)

def command(label, argv, expected):
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'expected_exit_codes': expected,
           'started_epoch': time.time(), 'scope': 'Fresh read-only infrastructure byte comparison/diff, not TeX or science.'}
    dump('native/' + label + '/ATTEMPT.json', row)
    result = subprocess.run(argv, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL, capture_output=True, timeout=30)
    write('native/' + label + '/stdout.raw', result.stdout)
    write('native/' + label + '/stderr.raw', result.stderr)
    row.update(ended_epoch=time.time(), native_exit_code=result.returncode,
               stdout=value(result.stdout), stderr=value(result.stderr))
    dump('native/' + label + '/RECEIPT.json', row)
    native.append(row)
    check(result.returncode in expected and result.stderr == b'', 'fresh native expected outcome ' + label)
    return result.stdout

for number, name in enumerate(NAMES):
    raw = command(str(number) + '_cmp', ['/usr/bin/cmp', '--', str(PREP / name),
                  str(PREP / 'diagnostic_capture05/executed_adapter' / name)], [0])
    check(raw == b'', 'fresh current/snapshot byte identity ' + name)
    raw = command(str(number) + '_diff', ['/usr/bin/diff', '-u', str(PREP / 'history/diagnostic01_source' / name),
                  str(PREP / name)], [0, 1])
    saved = PREP / 'diagnostic_capture05/commands' / ('diff_' + name.replace('.', '_')) / 'stdout.raw'
    check(raw == read(saved), 'fresh native complete original diff bytes ' + name)

after = {str(p): value(p.read_bytes()) for p in sorted(selected)}
check(after == reads, 'complete selected input set unchanged')
dump('READ_INPUTS_AFTER.json', after)
dump('CHECKS.json', checks)
dump('SAVED_NATIVE_CENSUS.json', archived)
result = {'status': 'HOLD_CONCRETE_BLOCKER_BLD_I1', 'open_findings': ['BLD-I1'],
          'evidence_integrity_checks_passed': len(checks), 'input_files': len(reads),
          'input_bytes': sum(v['bytes'] for v in reads.values()), 'manifests': manifests,
          'archived_native_receipts': len(archived), 'fresh_native_readonly_commands': len(native),
          'submitted_scripts_executed_or_imported': 0, 'TeX_or_scientific_source_files_read': 0,
          'TeX_science_render_commands': 0, 'host_or_historical_pin_referents_followed': 0,
          'scope': 'Independent static current-code audit and selected original archive integrity only; not production approval, live failure reproduction, build/visual/manuscript acceptance or hermetic tracing.',
          'finished_utc': datetime.now(timezone.utc).isoformat()}
dump('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
