"""Same-reviewer exact no-change delta audit; never executes old code or science.

Reads preserved native evidence and actual full dependency bytes. Infrastructure
scope mirrors the fully read B/root key contracts, with exactly two historical
B aliases; no generic path rewrite and no new theorem, build or page view.
"""
import ast
import collections
from datetime import datetime, timezone
import difflib
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import sys
import sysconfig
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
B = Path(__file__).resolve().parent
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
FROZEN = PAPER / 'frozen_round1'
HISTORY = B / 'history/initial_before_delta'
PAIR = QA / 'root_replays/p210_b_strict_pair_01'
PREP = QA / 'p210_b_strict_preparation'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PYTHON = Path('/usr/bin/python3.10')
PY_PATH = ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload']
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
DATA_ROOTS = tuple(map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')))
ALIASES = {
    str(B / 'DELTA.md'): ('6b59ce7b8f12206a5fe9f761e1aa1d3990c8fa66451961cd9645db63d5d9d618', HISTORY / 'DELTA.md'),
    str(B / 'SHA256SUMS'): ('81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3', HISTORY / 'SHA256SUMS')}
RESPONSE = ROOT / 'docs/papers204_208_sequence/P210_B_RESPONSE.md'
RESPONSE_SHA = '10d856f1c5b0ab7aa12229c9b4262b6888b439bacaa28b0374483f9a60cf12c7'
READS, ROLES, ALIAS_USES, NATIVE, COMPARES = {}, collections.defaultdict(set), {}, [], []
CHECKS = 0


def need(test, label):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(label)


def digest(body):
    return hashlib.sha256(body).hexdigest()


def actual_key(path):
    p = Path(path)
    need(p.is_file(), ('physical file', str(p)))
    h = hashlib.sha256()
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return {'sha256': h.hexdigest(), 'bytes': p.stat().st_size, 'resolved': str(p.resolve()),
            'symlink': os.readlink(p) if p.is_symlink() else None}


def pin(path, expected=None, role='declared_input', force=False, historical=True):
    logical = str(Path(path))
    physical = Path(path)
    wanted_sha = expected if isinstance(expected, str) else expected.get('sha256') if expected else None
    if historical and logical in ALIASES:
        old_sha, selected = ALIASES[logical]
        need(wanted_sha is None or wanted_sha == old_sha, ('only exact old B role may alias', logical))
        physical = selected
        ALIAS_USES[logical] = {'physical': str(selected), 'sha256': old_sha,
                              'scope': 'exact initial role, not current same-named lifecycle bytes'}
        wanted_sha = old_sha
    name = str(physical)
    ROLES[role].add(name)
    if force or name not in READS:
        row = actual_key(physical)
        need(name not in READS or READS[name] == row, ('input changed during audit', name))
        READS[name] = row
    row = READS[name]
    if wanted_sha:
        need(row['sha256'] == wanted_sha, ('full sha256', logical, name))
    if isinstance(expected, dict):
        size = expected.get('bytes', expected.get('size'))
        need(size is None or row['bytes'] == size, ('full size', logical))
        old_resolved = expected.get('resolved', expected.get('real'))
        if historical and logical in ALIASES:
            need(old_resolved is None or old_resolved == logical, ('old logical resolved metadata', logical))
            need(expected.get('symlink') is None and physical.resolve() == physical, ('physical exact historical copy', logical))
        else:
            need(old_resolved is None or row['resolved'] == old_resolved, ('resolved file role', logical))
            if 'symlink' in expected:
                need(row['symlink'] == expected['symlink'], ('symlink file role', logical))
    return row


def raw(path, role='decoded_input', historical=True):
    row = pin(path, role=role, historical=historical)
    actual = ALIASES[str(Path(path))][1] if historical and str(Path(path)) in ALIASES else Path(path)
    body = actual.read_bytes()
    need(digest(body) == row['sha256'] and len(body) == row['bytes'], ('complete decoded bytes stable', str(path)))
    return body


def js(path, role='decoded_json', historical=True):
    body = raw(path, role, historical)
    return json.loads(gzip.decompress(body) if str(path).endswith('.gz') else body)


def val(path, historical=True):
    row = pin(path, historical=historical)
    return {k: row[k] for k in ('sha256', 'bytes')}


def compare(left, right, role):
    need(raw(left) == raw(right), ('complete Python bytes comparison', str(left), str(right)))
    COMPARES.append({'left': str(left), 'right': str(right), 'role': role,
                     'method': 'full Python bytes, not another native cmp'})


def manifest(base, filename, count, sha=None, complete=False):
    path = base / filename
    if sha:
        pin(path, sha, 'manifest')
    body = raw(path, 'manifest')
    need(body.endswith(b'\n'), ('manifest final newline', str(path)))
    rows = {}
    for line in body.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, ('manifest strict syntax', str(path)))
        h, name = match.groups()
        p = Path(name)
        need(not p.is_absolute() and '..' not in p.parts and name not in rows and name != filename, ('safe unique nonself', name))
        rows[name] = h
        pin(base / name, h, 'manifest_payload')
    need(len(rows) == count, ('exact manifest count', str(path), len(rows), count))
    if complete:
        need(set(rows) == {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file() and p != path}, ('physical full manifest coverage', str(base)))
    return rows


def native_wrapper(stem, expected_session, source, source_sha, count_key, expected_count):
    launch = js(QA / (stem + '_LAUNCH.actual.json'), 'root_actual_launch')
    completion = js(QA / (stem + '_COMPLETION.actual.json'), 'root_actual_completion')
    need(completion['launch_record'] == stem + '_LAUNCH.actual.json', 'exact actual launch referent')
    need(launch['result']['session_id'] == completion['session_id'] == expected_session, 'actual same parent session')
    need(launch['result']['output'] == '' and type(completion['result']['exit_code']) is int and completion['result']['exit_code'] == 0, 'actual complete native zero')
    need('Warning: truncated' not in completion['result']['output'], 'complete original JSON stdout')
    tokens = shlex.split(launch['command'])
    need(tokens[:6] == ['/usr/bin/env', '-i', 'PATH=/usr/bin:/bin', 'LANG=C.UTF-8', 'LC_ALL=C.UTF-8', 'TZ=UTC'], 'exact safe native environment command')
    need(tokens[6:11] == [str(PYTHON), '-I', '-S', '-B', '-X'] and tokens[11].startswith('pycache_prefix='), 'source-only original parent flags')
    need(tokens[12] == str(source) and not os.path.lexists(tokens[11].split('=', 1)[1]), 'actual pinned source and absent parent cache')
    pin(source, source_sha, 'fully_read_root_receiver_or_runner_source')
    out = json.loads(completion['result']['output'])
    need(out[count_key] == expected_count, ('actual output count', stem))
    NATIVE.append({'root_stem': stem, 'session': expected_session, 'native_exit': 0,
                   'launch': str(QA / (stem + '_LAUNCH.actual.json')), 'completion': str(QA / (stem + '_COMPLETION.actual.json'))})
    return out


def resources():
    names = {str(PYTHON), '/usr/bin/cmp', '/usr/bin/ldd', '/usr/bin/env', '/bin/bash', '/bin/sh'}
    for directory, folders, files in os.walk('/usr/lib/python3.10'):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in LIB_ROOTS:
        paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        names.update(str(p) for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    names.update(str(p) for base in DATA_ROOTS for p in base.rglob('*') if p.is_file())
    return sorted(names)


def config_now(row):
    out = {}
    for name, expected in row.items():
        p = Path(name)
        got = {'lexists': os.path.lexists(p), 'exists': p.exists(), 'is_file': p.is_file(), 'is_dir': p.is_dir(),
               'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
        if 'sha256' in expected:
            got.update(val(p))
        need(got == expected, ('full configuration and presence key', name))
        out[name] = got
    return out


def b_scope(ledger, build):
    roots = list(map(Path, ('/usr/lib/python3.10', '/usr/lib/locale', '/usr/lib/x86_64-linux-gnu/gconv')))
    conf_roots = list(map(Path, ('/etc/ld.so.conf.d', '/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv')))
    if build:
        roots += list(map(Path, ('/etc/texmf', '/var/lib/texmf', '/usr/share/texlive/texmf-dist', '/usr/share/texmf',
                     '/etc/fonts', '/usr/share/fontconfig', '/var/cache/fontconfig', '/usr/share/poppler', '/usr/share/fonts')))
        conf_roots += list(map(Path, ('/usr/local/share/texmf', '/root/texmf', '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var',
                     '/usr/local/share/fonts', '/root/.fonts', '/root/.fontconfig', '/root/.config/fontconfig', '/root/.cache/fontconfig',
                     '/root/.local/share/fonts', '/etc/xdg/fontconfig', '/etc/profile.d')))
    def chosen(p):
        if any(p.is_relative_to(base) and p != base for base in conf_roots):
            return True
        if any(p.is_relative_to(base) and p != base for base in roots) and not any(v in p.parts for v in ['__pycache__', 'site-packages', 'dist-packages']) and p.suffix not in {'.pyc', '.pyo'}:
            return True
        return any(p.is_relative_to(base) and p != base and (p.name.endswith('.so') or '.so.' in p.name)
                   and (base != Path('/usr/local/lib') or len(p.relative_to(base).parts) == 1) for base in LIB_ROOTS)
    discovered = {str(p) for base in roots for p in base.rglob('*') if p.is_file() and
                  not any(v in p.parts for v in ['__pycache__', 'site-packages', 'dist-packages']) and p.suffix not in {'.pyc', '.pyo'}}
    discovered.update(str(p) for base in conf_roots for p in base.rglob('*') if p.is_file())
    for base in LIB_ROOTS:
        paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        discovered.update(str(p) for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    fixed = {p for p in ledger['files'] if not chosen(Path(p))}
    current = fixed | discovered | {p for p, row in ledger['configuration'].items() if row['is_file']}
    need(current == set(ledger['files']) and ledger['membership'] == sorted(current), 'full current original B resource membership')
    config_now(ledger['configuration'])
    return {'files': len(current), 'configuration': len(ledger['configuration']), 'fixed': len(fixed), 'discovered': len(discovered)}


def sample(known=None):
    maps = Path('/proc/self/maps').read_text()
    modules = {name: getattr(module, '__file__', None) for name, module in sorted(sys.modules.items())}
    paths = [p for p in modules.values() if p]
    paths += [line.split(None, 5)[5] for line in maps.splitlines() if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith('/')]
    for path in paths:
        need(Path(path).suffix not in {'.pyc', '.pyo'}, ('no delta sampled bytecode', path))
        pin(path, role='delta_runtime_module_or_map')
        if known is not None and not Path(path).is_relative_to(B):
            need(str(Path(path).resolve()) in known, ('delta runtime covered by full root resource key', path))
    return {'proc_maps': maps, 'modules': modules, 'flags': repr(sys.flags), 'environment': ENV,
            'argv': sys.orig_argv, 'cwd': str(Path.cwd()), 'executable': sys.executable,
            'sys_path': sys.path, 'pycache_prefix': sys.pycache_prefix,
            'scope': 'before/after file-backed module/maps, not OS/startup or continuous tracing'}


def recorded_sample(data, known, cache):
    need(data['environment'] == ENV and data['cwd'] == str(ROOT) and data['executable'] == str(PYTHON) and data['sys_path'] == PY_PATH, 'recorded strict identity')
    need(data['pycache_prefix'] == str(cache) and not data['cache_lexists'] and not os.path.lexists(cache), 'recorded strict absent cache')
    need(all(t in data['flags'] for t in ['isolated=1', 'no_site=1', 'optimize=0', 'dont_write_bytecode=1']), 'recorded strict flags')
    body = data['proc_maps'].encode()
    need(digest(body) == data['proc_maps_sha256'] and len(body) == data['proc_maps_bytes'], 'entire recorded maps bytes')
    paths = {str(Path(line.split(None, 5)[5]).resolve()) for line in data['proc_maps'].splitlines()
             if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith('/')}
    need(paths == set(data['mapped_files']), 'complete recorded map reclassification')
    for path, key in list(data['mapped_files'].items()) + [(r['path'], r) for r in data['modules'].values()]:
        need(path in known and all(known[path][k] == key[k] for k in ['sha256', 'bytes']), 'full recorded sampled input coverage')
        need(Path(path).suffix not in {'.pyc', '.pyo'}, 'recorded source-only module')
        pin(path, key, 'root_recorded_runtime_sample')


def main():
    need(len(sys.argv) == 2 and sys.argv[1] in {'before', 'after'}, 'exact phase')
    phase = sys.argv[1]
    need(dict(os.environ) == ENV and Path.cwd() == ROOT and Path(sys.executable).resolve() == PYTHON, 'actual safe delta runtime')
    need(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0 and sys.path == PY_PATH, 'actual delta source-only flags/path')
    need(sys.pycache_prefix and not os.path.lexists(sys.pycache_prefix), 'actual delta new absent cache')
    started = time.time()
    runtime_before = sample()
    for name in ['delta_inspect.py', 'launch_command.py', 'preserve_initial_delta.py', 'INITIAL_PRESERVATION.actual.json', 'INITIAL_PRESERVED_PINS.sha256']:
        pin(B / name, role='same_B_delta_source_or_preservation')
    pin(RESPONSE, RESPONSE_SHA, 'exact_response')
    pin(QA / 'P210_B_ROOT_INITIAL_INSPECTION.md', '2b06d0b4b25bcb89bb7180fa0403a46ead8a170d54bcdaa9b839d09c8a11f96d', 'exact_root_acceptance')
    for name in ['P210_B_ROOT_ORIGINAL_INITIAL_INSPECTION.md', 'P210_B_INITIAL_SEAL_NATIVE_RETURN.actual.json',
                 'P210_B_INITIAL_ORIGINALS_METADATA_ROOT.actual.json', 'P210_B_STRICT_ORIGINALS_METADATA_ROOT.actual.json',
                 'P210_B_STRICT_ORIGINALS_PREPARATION.actual.json', 'P210_B_STRICT_RECEIVER_REVISION01_ROOT_STATIC.actual.json',
                 'P210_B_STRICT_RECEIVER_REVISION01_ROOT_STATIC02.actual.json', 'P210_B_STRICT_ROOT_PREFLIGHT.actual.json', 'P210_B_STRICT_ROOT_SEAL.actual.json']:
        pin(QA / name, role='exact_additional_root_document_or_return')
    preservation = js(B / 'INITIAL_PRESERVATION.actual.json')
    need(preservation['initial_payloads'] == 407 and preservation['complete_preserved_roles_including_seal'] == 408 and not preservation['accepted_delta'], 'real initial preservation before replacement')
    initial = manifest(B, 'SHA256SUMS', 407, ALIASES[str(B / 'SHA256SUMS')][0])
    need(len(preservation['roles']) == 408 and {r['initial_name'] for r in preservation['roles']} == set(initial) | {'SHA256SUMS'}, 'all actual initial role names')
    for row in preservation['roles']:
        pin(row['physical_path'], row, 'all_408_initial_physical_roles')
    pin(B / 'REPORT.md', 'd2d42801e61ef278affc16af6659ba708bf5dec0ca7585b3cb1cf5d738877dfb', 'immutable_initial_report')
    pin(B / 'FINDINGS.json', '0db9eea2a59a6bfb01b5ce3dbd57c84aa2cb84ab4ac952e2a72829a3f56f5bbb', 'immutable_initial_findings')
    old_audit = js(B / 'AUDIT_INPUTS.actual.json.gz')
    need(len(old_audit) == 120840, 'original full B reuse ledger')
    for name, wanted in old_audit.items():
        pin(name, wanted, 'all_120840_original_B_dependency_keys')

    initial_root = native_wrapper('P210_B_INITIAL_ORIGINALS_ROOT', 11639,
        QA / 'p210_b_initial_reception_preparation/receive_p210_b_initial.py',
        '096508c3ac6886f2ea57a040575520c01bb36ffc6944606431b76550c2c7ab76', 'checks', 1116081)
    extra = initial_root['extra_read_keys_not_in_B_audit_ledger']
    need(len(extra) == 55 and not set(extra) & set(old_audit), 'exact 55 initial receiver extra roles')
    merged = {**old_audit, **extra}
    need(len(merged) == initial_root['all_current_read_keys_count'] == 120895 and
         digest(json.dumps(merged, sort_keys=True, separators=(',', ':')).encode()) == initial_root['all_current_read_keys_canonical_json_sha256'], 'full initial receiver logical read-map reconstruction')
    for name, wanted in extra.items():
        pin(name, wanted, 'all_55_initial_receiver_extra_keys')
    need(initial_root['B_named_keys_fully_read_twice'] == 120840 and initial_root['native_originals_bound'] == 63 and
         initial_root['full_python_raw_comparisons'] == 515 and not initial_root['accepted_delta'] and initial_root['new_scientific_runs'] == 0, 'actual initial reception boundary')
    for row in initial_root['manifests']:
        pin(row['path'], row['sha256'], 'initial_receiver_consumed_manifest')
    historical_pdfs = initial_root['intermediate_unconsumed_pdf_historical_keys_only']
    need([r['pass_number'] for r in historical_pdfs] == [1, 2, 3] and all(r['old_bytes_reread'] is False for r in historical_pdfs), 'unconsumed overwritten PDF limits remain')
    for row in historical_pdfs:
        product = js(B / ('build02/commands/pass_' + str(row['pass_number']) + '/SOURCE_AFTER.json'))
        need(product[str(B / 'build02/source/main.pdf')] == row['recorded_key'], 'historical PDF key only, not recovered bytes')
    need(not any(Path(r['path']).name == 'main.pdf' for r in js(B / 'build02/FLS_CLOSURE.json')), 'intermediate PDF never consumed by FLS')
    reuse_scope = {}
    for label in ['produce01', 'pair01', 'build01', 'build02']:
        ledger = js(B / label / 'INPUTS_BEFORE.json.gz')
        if label != 'build01':
            need(ledger == js(B / label / 'INPUTS_AFTER.json.gz'), 'decoded original source/runtime keys unchanged')
        for name, wanted in ledger['files'].items():
            pin(name, wanted, 'old_run_full_dependency_key')
        reuse_scope[label] = b_scope(ledger, label.startswith('build'))

    pair_root = native_wrapper('P210_B_STRICT_ROOT', 31521, PREP / 'run_pair.py',
        'bacc8bf0351bdfbcc2bc671cd61131d6382fe5caccd00f02e3988afbf1d066d1', 'checks_each', [51129, 51129])
    pair_rows = manifest(PAIR, 'SHA256SUMS', 59, '54cdd8ca9a00374f53a82e7f84a47fdd91f3fcde8b1519b027b98c7925ace181', True)
    prep_rows = manifest(PREP, 'SHA256SUMS', 4, '987367c15fae0bd4d34ebf6c97cd1ee2dc71d1f15782ec57d73f61a332d97eec', True)
    need(pair_root['closure']['manifest'] == val(PAIR / 'SHA256SUMS') and pair_root['closure']['payloads'] == 59 and pair_root['known_inputs'] == 3558, 'actual root pair output binds full seal')
    seal_record = js(QA / 'P210_B_STRICT_ROOT_SEAL.actual.json')
    need(seal_record['result']['exit_code'] == 0 and seal_record['cwd'] == str(PAIR) and
         seal_record['result']['output'] == ''.join(name + ': OK\n' for name in pair_rows), 'actual complete native 59-payload seal stdout')
    resources_before = js(PAIR / 'RESOURCE_NAMES_BEFORE.json')
    need(resources_before == js(PAIR / 'RESOURCE_NAMES_AFTER.json') == resources() and len(resources_before) == 3121, 'all exact current strict resource names')
    conf = js(PAIR / 'CONFIGURATION_BEFORE.json')
    need(conf == js(PAIR / 'CONFIGURATION_AFTER.json') and len(conf) == 41, 'strict entire configuration before/after')
    config_now(conf)
    known = js(PAIR / 'INPUTS_BEFORE.json')
    need(known == js(PAIR / 'INPUTS_AFTER.json') and len(known) == 3558, 'strict all 3558 rich keys before/after')
    copies = js(PAIR / 'SOURCE_ONLY_INITIAL.json')
    need(set(copies) == {'run_pair.py', 'verify.py', 'PARAMETERS.json'}, 'three strict source-only inputs')
    for name, row in copies.items():
        compare(row['origin'], row['copy'], 'exact strict source copy')
        need(row['copy'] == str(PAIR / 'sources' / name), 'source copy exact physical role')
    input_pins = js(PREP / 'INPUT_PINS.json')['inputs']
    need(len(input_pins) == 17, '17 strict preparation inputs')
    for name, wanted in input_pins.items():
        pin(name, wanted, 'strict_preparation_original')
    baseline = {'role': 'p210_b', 'package_payloads': 407, 'package_manifest': val(B / 'SHA256SUMS'),
        'preparation_manifest': val(PREP / 'SHA256SUMS'), 'verifier': val(B / 'verify.py'),
        'canonical': val(B / 'CANONICAL.json'), 'parameters': val(B / 'PARAMETERS.json'),
        'package_files': sorted(str(B / name) for name in initial) + [str(B / 'SHA256SUMS')],
        'preparation_files': sorted(str(PREP / name) for name in prep_rows) + [str(PREP / 'SHA256SUMS')]}
    need(js(PAIR / 'PACKAGE_AND_PREPARATION_CLOSURE.json') == {'before': baseline, 'after': baseline}, 'full initial logical package closure')
    names = set(baseline['package_files']) | set(baseline['preparation_files']) | set(resources_before) | set(input_pins)
    names.update(row['copy'] for row in copies.values())
    names.update(name for name, row in conf.items() if row['is_file'])
    # Logical resolved names are the pre-delta original roles, not current alias targets.
    names.update(str(Path(name).resolve()) for name in list(names))
    need(names == set(known), 'independently rebuilt full strict known union')
    for name, wanted in known.items():
        pin(name, wanted, 'all_3558_strict_dependency_keys')
    entered = js(PAIR / 'RUN_ENTERED.json')
    need(entered['environment'] == ENV and entered['cwd'] == str(ROOT), 'actual entered cwd, not invented outer launch field')
    for name in ['before', 'after']:
        recorded_sample(js(PAIR / ('observations/parent_' + name + '.json')), known, PAIR / 'unused_parent_cache')
    result = js(PAIR / 'RESULT.json')
    need(result['status'] == 'PASS_ROOT_P210_B_STRICT_PAIR' and result['errors'] == [] and result['unfinalized_native_labels'] == [], 'complete actual strict pair result')
    expected = {
        '00_cmp_runner_source': ['/usr/bin/cmp', '--', str(PREP / 'run_pair.py'), str(PAIR / 'sources/run_pair.py')],
        '01_cmp_verifier_source': ['/usr/bin/cmp', '--', str(B / 'verify.py'), str(PAIR / 'sources/verify.py')],
        '01a_cmp_parameters_source': ['/usr/bin/cmp', '--', str(B / 'PARAMETERS.json'), str(PAIR / 'sources/PARAMETERS.json')]}
    ldd = ['/usr/bin/ldd', str(PYTHON), '/usr/bin/cmp'] + sorted(p for p in resources_before if p.startswith('/usr/lib/python3.10/') and p.endswith('.so'))
    expected['02_ldd_before'] = ldd
    for number in ['01', '02']:
        expected['03_verify_' + number] = [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(PAIR / ('unused_child_' + number + '_cache')),
                                          str(PAIR / 'sources/run_pair.py'), 'child', number, 'p210_b']
    for number in ['01', '02']:
        expected['04_cmp_canonical_' + number] = ['/usr/bin/cmp', '--', str(PAIR / ('commands/03_verify_' + number + '/stdout.raw')), str(B / 'CANONICAL.json')]
    expected['05_cmp_pair'] = ['/usr/bin/cmp', '--', str(PAIR / 'commands/03_verify_01/stdout.raw'), str(PAIR / 'commands/03_verify_02/stdout.raw')]
    expected['06_ldd_after'] = ldd
    need([r['label'] for r in result['commands']] == list(expected) and {p.name for p in (PAIR / 'commands').iterdir()} == set(expected), 'ten exact native commands')
    groups = []
    previous = datetime.fromisoformat(entered['started_utc'])
    for row in result['commands']:
        label = row['label']
        folder = PAIR / 'commands' / label
        receipt, attempt = js(folder / 'RECEIPT.json'), js(folder / 'ATTEMPT.json')
        need(receipt == {k: v for k, v in row.items() if k != 'label'}, 'entire actual receipt equals summary')
        need(attempt == {'argv': expected[label], 'cwd': str(ROOT), 'environment': ENV, 'started_utc': attempt['started_utc'],
             'timeout_seconds': 300 if label.startswith('03_verify_') else 60, 'status': 'ATTEMPTED', 'exit_code': None,
             'stdin': 'DEVNULL', 'new_owned_session_requested': True}, 'every exact native prestart field')
        need(all(receipt[k] == v for k, v in attempt.items() if k not in {'status', 'exit_code'}), 'all prestart fields bound into native result')
        need(receipt['status'] == 'COMPLETED' and type(receipt['exit_code']) is int and receipt['exit_code'] == receipt['wrapper_exit_code'] == 0 and
             receipt['spawned'] and receipt['streams_complete'] and not receipt['timed_out'] and not receipt['interrupted'] and receipt['failure'] is None, 'actual native successful complete computation')
        begin, end = map(datetime.fromisoformat, [receipt['started_utc'], receipt['ended_utc']])
        need(previous <= begin <= end <= datetime.fromisoformat(result['ended_utc']), 'full native command chronology')
        previous = end
        group = receipt['process_group_settlement']
        need(group['quiescent'] and group['remaining_members'] == group['signals'] == [] and group['native_returncode'] == 0 and
             type(group['owned_pgid']) is int and group['owned_pgid'] == group['owned_sid'] > 0, 'actual settled owned session')
        groups.append({'label': label, **group})
        for stream in ['stdout', 'stderr']:
            pin(folder / (stream + '.raw'), receipt[stream], 'complete_strict_native_stream')
        need(raw(folder / 'stderr.raw') == b'', 'full native empty stderr')
        if receipt['argv'][0] == '/usr/bin/cmp':
            need(raw(folder / 'stdout.raw') == b'', 'full native cmp output')
            compare(receipt['argv'][-2], receipt['argv'][-1], 'rechecked actual native cmp operands')
    need(len({r['owned_pgid'] for r in groups}) == 10, 'ten distinct owned groups')
    for number in ['01', '02']:
        observed = js(PAIR / ('observations/child_' + number + '.json'))
        need(observed['status'] == 'RETURNED' and observed['scientific_argv'] == [str(PAIR / 'sources/verify.py')] and observed['parameter_locator'] == 'sibling of scientific __file__', 'unaltered B scientific interface')
        for name in ['before', 'after']:
            recorded_sample(observed[name], known, PAIR / ('unused_child_' + number + '_cache'))
        opens = {str(PAIR / 'sources' / name): val(PAIR / 'sources' / name) for name in ['verify.py', 'PARAMETERS.json']}
        need(observed['opened_ordinary_files'] == opens and observed['python_open_events'] == [{'path': path, 'mode': 'r', 'flags': os.O_RDONLY | os.O_CLOEXEC} for path in opens]
             and observed['volatile_open_paths'] == observed['nonfile_open_paths_at_end'] == [], 'two exact scientific open events, no global trace claim')
        compare(PAIR / ('commands/03_verify_' + number + '/stdout.raw'), B / 'CANONICAL.json', 'complete actual strict output')
    links = js(PAIR / 'LINKED_RUNTIME.json')
    for label, phase_name in [('02_ldd_before', 'before'), ('06_ldd_after', 'after')]:
        body = raw(PAIR / ('commands/' + label + '/stdout.raw'))
        paths = sorted({str(Path(os.fsdecode(p)).resolve()) for p in re.findall(rb'(/[^\s()]+)', body) if Path(os.fsdecode(p)).is_file()})
        need(b'not found' not in body and paths == links[phase_name] and all(path in known for path in paths), 'full recorded ldd dependency parse')
    need(links['before'] == links['after'], 'same linked-runtime membership')

    strict_root = native_wrapper('P210_B_STRICT_ORIGINALS_ROOT', 69598,
        QA / 'p210_b_strict_receiver_revision_01/receive_p210_b_strict.py',
        '4781a5452647c529370e2a335bb7a2d3f1db7a2025bf351125ad6247a7a796b6', 'checks', 43609)
    extra = strict_root['extra_read_keys_outside_original_known_ledger']
    need(len(extra) == 75 and not set(extra) & set(known), '75 exact strict receiver extra inputs')
    logical = {name: {k: row[k] for k in ['sha256', 'bytes']} for name, row in known.items()}
    logical.update(extra)
    need(len(logical) == 3633 and digest(json.dumps(logical, sort_keys=True, separators=(',', ':')).encode()) == strict_root['read_ledger_sha256'], 'complete strict receiver 3633-map reconstruction')
    for name, wanted in extra.items():
        pin(name, wanted, 'all_75_strict_receiver_extra_keys')
    need(strict_root['actual_owned_groups'] == groups and strict_root['checks_each'] == [51129, 51129] and strict_root['fresh_scientific_runs_by_this_inspector'] == 0, 'root receiver exact groups and no new science')
    for prep_name, count, sha in [('p210_b_initial_reception_preparation', 6, 'ae22036abc63c452bd24910a9210bf3a5f0da1f8485a7e0f9d7033cab1efd0d2'),
                                 ('p210_b_strict_receiver_revision_01', 7, '6e4bfae68f5bca13af25bcd2572a87cf9fa6484792c2b0d0dda2e3a64d264ff6'),
                                 ('p210_b_strict_receiver_static_review', 5, '62c3d32b698cdaaa1ea9ae4dd01c1e538ece12bf88349065fac412d77e8a9719')]:
        manifest(QA / prep_name, 'SHA256SUMS', count, sha, True)
    failure = js(QA / 'P210_B_STRICT_RECEIVER_REVISION01_ROOT_STATIC.actual.json')
    success = js(QA / 'P210_B_STRICT_RECEIVER_REVISION01_ROOT_STATIC02.actual.json')
    need(failure['result']['exit_code'] == 1 and 'AssertionError' in failure['result']['output'] and success['result']['exit_code'] == 0, 'retained real root static failure and separate correction')
    old = QA / 'p210_b_strict_receiver_static_review/inspect_p210_b_strict_pair.before_root_followup.py'
    new = QA / 'p210_b_strict_receiver_revision_01/receive_p210_b_strict.py'
    expected_diff = ''.join(difflib.unified_diff(raw(old).decode().splitlines(True), raw(new).decode().splitlines(True),
                     fromfile=str(old.relative_to(ROOT)), tofile=str(new.relative_to(ROOT))))
    need(raw(new.parent / 'SOURCE_DIFF.diff').decode() == expected_diff, 'exact full newline-preserving receiver source diff')
    old_functions = {n.name: ast.dump(n, include_attributes=False) for n in ast.parse(raw(old)).body if isinstance(n, ast.FunctionDef)}
    new_functions = {n.name: ast.dump(n, include_attributes=False) for n in ast.parse(raw(new)).body if isinstance(n, ast.FunctionDef)}
    need(all(new_functions[name] == value for name, value in old_functions.items() if name != 'main'), 'eight old helpers actually unchanged')

    nochange = native_wrapper('P210_B_EXACT_NOCHANGE', 75160, QA / 'check_p210_b_response.py',
        'da271d87febda6cae1e3f76c79a64e8206a6d2113e95b424910f100e55ae34d3', 'checks', 29277)
    nochange_names = {str(QA / 'check_p210_b_response.py')}
    sets = {}
    for role, base, filename, count, complete in [('review', B, 'SHA256SUMS', 407, False), ('round1', FROZEN, 'SHA256SUMS', 508, True),
        ('round0', PAPER / 'frozen_round0', 'SHA256SUMS', 493, True), ('author', PAPER, 'AUTHOR_MANIFEST.sha256', 489, False),
        ('whole', PAPER, 'PAPER_MANIFEST.sha256', 1496, True)]:
        rows = manifest(base, filename, count, nochange['seals'][role], complete)
        sets[role] = rows
        nochange_names.add(str(base / filename))
        nochange_names.update(str(base / name) for name in rows)
    for name in ['ROOT_ADOPTION.md', 'ROOT_LIFECYCLE.md']:
        pin(PAPER / name, role='unchanged_submission_control')
    pin(PAPER / 'ROOT_LIFECYCLE.md', 'd1548b317d0575c4ab8c95912f9154786df79763aeebcbe63daa832de0430a7d')
    start_compare = len(COMPARES)
    compare(PAPER / 'SHA256SUMS', PAPER / 'AUTHOR_MANIFEST.sha256', 'unchanged author seal alias')
    compare(PAPER / 'AUTHOR_MANIFEST.sha256', FROZEN / 'AUTHOR_MANIFEST.sha256', 'unchanged frozen author seal')
    for name in sets['author']:
        compare(PAPER / name, FROZEN / name, 'unchanged all author input bytes')
    for name in sets['round0']:
        compare(PAPER / 'frozen_round0' / name, FROZEN / name, 'unchanged all Round0 core bytes')
    need(len(COMPARES) - start_compare == nochange['full_python_raw_comparisons'] == 984, 'all exact nochange byte comparisons')
    nochange_keys = {}
    for name in sorted(nochange_names):
        row = pin(name)
        nochange_keys[name] = {'resolved': name, 'symlink': None, 'bytes': row['bytes'], 'sha256': row['sha256']}
    need(len(nochange_keys) == nochange['current_paths_reread'] == 1906 and
         digest(json.dumps(nochange_keys, sort_keys=True, separators=(',', ':')).encode()) == nochange['complete_key_digest'], 'entire exact nochange original logical key map')
    input_rows = manifest(ROOT, str((B / 'INPUT_PINS.sha256').relative_to(ROOT)), 509)
    need(set(input_rows) == {str((FROZEN / name).relative_to(ROOT)) for name in set(sets['round1']) | {'SHA256SUMS'}}, 'all 509 reviewed inputs unchanged')
    need(js(B / 'FINDINGS.json')['current_open_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 0}, 'original zero-open finding census')
    runtime_after = sample(known)
    need(resources_before == resources() and config_now(conf) == conf, 'end-phase complete strict resource/presence unchanged')
    first_reads = dict(READS)
    for name, wanted in first_reads.items():
        need(actual_key(name) == wanted, ('second full physical delta input read', name))
    common = dict(READS)
    summary = {'status': 'PASS_SAME_B_EXACT_NOCHANGE_DELTA_' + phase.upper(), 'phase': phase,
        'started_epoch': started, 'ended_epoch': time.time(), 'checks': CHECKS,
        'full_physical_input_paths_reread_twice': len(common), 'root_native_wrappers_checked': len(NATIVE),
        'root_actual_strict_native_commands_checked': len(groups), 'full_Python_byte_comparisons': len(COMPARES),
        'response': {'path': str(RESPONSE), **val(RESPONSE)}, 'same_reviewer': '/root/p210_b_reviewer',
        'initial_payloads_preserved': 407, 'unchanged_in_place_initial_payloads_except_delta': 406,
        'exact_initial_aliases': ALIAS_USES, 'all_120840_B_reuse_keys_current': True,
        'root_initial_receiver_map': initial_root['all_current_read_keys_canonical_json_sha256'],
        'root_strict_receiver_map': strict_root['read_ledger_sha256'], 'root_nochange_map': nochange['complete_key_digest'],
        'root_checks_each': [51129, 51129], 'B_original_reuse_scope': reuse_scope,
        'historical_unconsumed_PDF_keys_only': historical_pdfs, 'manuscript_changed': False,
        'new_scientific_runs': 0, 'new_builds': 0, 'new_views': 0, 'old_writers_executed': 0,
        'owner': 'OWNER_AMBER', 'external': 'HOLD_EXTERNAL', 'accepted_delta_written_by_this_program': False}
    def write(name, data):
        path = B / name
        with (gzip.open(path, 'xt') if path.suffix == '.gz' else path.open('x')) as stream:
            json.dump(data, stream, sort_keys=True, indent=2)
            stream.write('\n')
    if phase == 'after':
        previous = js(B / 'DELTA_INPUTS_BEFORE.json.gz', historical=False)
        need(common == previous, 'all common before/after physical delta inputs exactly unchanged')
        findings = js(B / 'CURRENT_FINDINGS.json', historical=False)
        need(findings['phase'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA' and findings['current_open_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 0}
             and findings['accepted_response_sha256'] == RESPONSE_SHA, 'actual same-reviewer current decision exact response')
        body = raw(B / 'DELTA.md', historical=False).decode()
        need('ACCEPTED_EXACT_NOCHANGE_DELTA' in body and RESPONSE_SHA in body, 'actual accepted decision binds exact response')
        summary['all_common_before_after_keys_equal'] = True
        summary['accepted_decision_independently_authored_before_this_check'] = True
        summary['checks'] = CHECKS
        write('DELTA_AFTER_EXTRA_INPUTS.actual.json', {name: row for name, row in READS.items() if name not in common})
    write('DELTA_INPUTS_' + phase.upper() + '.json.gz', common)
    write('DELTA_RUNTIME_' + phase.upper() + '.actual.json', {'before': runtime_before, 'after': runtime_after})
    write('DELTA_ROLES_' + phase.upper() + '.actual.json', {role: sorted(paths) for role, paths in ROLES.items()})
    write('DELTA_' + phase.upper() + '.actual.json', summary)
    if phase == 'before':
        write('DELTA_ROOT_NATIVE_BINDINGS.actual.json', {'parents': NATIVE, 'strict_native_groups': groups})
        write('DELTA_FULL_BYTE_COMPARISONS.actual.json', COMPARES)
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    main()
