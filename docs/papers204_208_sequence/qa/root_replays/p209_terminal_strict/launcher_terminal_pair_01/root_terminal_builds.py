#!/usr/bin/env python3
"""Root-only gated P209 terminal source-only pair; no overwrite or view verdict.

Disclosed adaptation of P208 terminal v2, with P209 strict launch/stream
failure preservation. Actual accepted deltas and physical Round2/root closure
are prerequisites, never manufactured here. No old recorder is imported.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import sysconfig
import traceback

SCRIPT = Path(__file__).resolve()
ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREPARATION = ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_preparation'
ROOT_LAUNCHER = PREPARATION / 'root_launch_terminal.py'
SOURCE_PINS = PREPARATION / 'SOURCE_PINS.json'
EXPECTED_SOURCE_PINS = 'bb707e351669318169eb558dc9097ef700bb44c01418253e3944aaa8dd4cd8f2'
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ROUND1 = PAPER / 'frozen_round1'
FREEZE = PAPER / 'frozen_round2'
OUT = PAPER / 'qa_final'
PYTHON = Path(sys.executable).resolve()
STDLIB = Path(sysconfig.get_path('stdlib')).resolve()
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
       'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788652800', 'FORCE_SOURCE_DATE': '1',
       'openin_any': 'p', 'openout_any': 'p'}
TOOLS = [Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich',
         'pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp')]
TOOLS += [Path('/bin/bash'), Path('/bin/sh'), Path('/usr/bin/env'), PYTHON]
LIB_ROOTS = (Path('/usr/lib/x86_64-linux-gnu'), Path('/usr/lib64'), Path('/usr/local/lib'))
TEX_ROOTS = [Path(p) for p in (
    '/usr/share/texlive/texmf-dist',
    '/usr/share/texmf', '/var/lib/texmf', '/etc/texmf', '/usr/local/share/texmf',
    '/root/texmf', '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')]
CONFIG_ROOTS = [Path(p) for p in ('/etc/ld.so.conf.d', '/usr/share/fonts',
    '/etc/fonts', '/var/cache/fontconfig', '/usr/share/fontconfig', '/usr/lib/locale/C.utf8',
    '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/usr/share/poppler',
    '/usr/local/share/fonts', '/etc/xdg/fontconfig', '/etc/profile.d',
    '/root/.fonts', '/root/.fontconfig', '/root/.fonts.conf.d',
    '/root/.config/fontconfig', '/root/.cache/fontconfig', '/root/.local/share/fonts')]
SOURCE_NAMES = ('main.tex', 'math_commands.tex', 'references.bib',
    'sections/00_abstract.tex', 'sections/01_setup.tex',
    'sections/02_recurrence.tex', 'sections/03_inverse.tex', 'sections/04_scope.tex')
USER_TEX_VARS = ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR')
UNREAPED_CHILDREN = set()


def info(path):
    raw = Path(path).read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(path, raw):
    with Path(path).open('xb') as stream:
        stream.write(raw)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def pins(paths):
    return {str(p.resolve()): info(p.resolve()) for p in sorted(set(map(Path, paths)))}


def manifest(base, name, complete=False):
    assert base.is_dir() and base.resolve() == base and not base.is_symlink(), str(base)
    source = base / name
    records = {}
    for line in source.read_text().splitlines():
        digest, rel = line.split('  ', 1)
        local = Path(rel)
        assert re.fullmatch(r'[0-9a-f]{64}', digest)
        assert local.as_posix() == rel and not local.is_absolute() and '..' not in local.parts and local.parts
        assert rel != name and rel not in records
        p = base / local
        assert p.resolve() == p and p.is_file() and not p.is_symlink() and info(p)['sha256'] == digest, str(p)
        records[rel] = info(p)
    if complete:
        entries = list(base.rglob('*'))
        assert all(not p.is_symlink() for p in entries)
        assert set(records) == {p.relative_to(base).as_posix() for p in entries
                                if p.is_file() and p != source}
    records[name] = info(source)
    return {str(base / n): v for n, v in records.items()}

def science():
    # Future acceptance values come only from actual root-controlled files.
    # This function does not create a gate, copy a freeze or execute science.
    result = manifest(PREPARATION, 'SHA256SUMS', complete=True)

    def read_json(path):
        result[str(path)] = info(path)
        return json.loads(path.read_bytes())

    assert info(SOURCE_PINS)['sha256'] == EXPECTED_SOURCE_PINS
    expected_sources = read_json(SOURCE_PINS)
    assert set(expected_sources) == set(SOURCE_NAMES) and len(expected_sources) == 8
    core = manifest(ROUND1, 'SHA256SUMS', complete=True)
    assert core[str(ROUND1 / 'SHA256SUMS')]['sha256'] == 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
    assert len(core) == 2004
    result.update(core)
    frozen = manifest(FREEZE, 'SHA256SUMS', complete=True)
    result.update(frozen)
    for n, v in expected_sources.items():
        assert all((base / n).resolve() == base / n and not (base / n).is_symlink()
                   for base in (PAPER, ROUND1, FREEZE)), n
        assert info(PAPER / n) == info(ROUND1 / n) == info(FREEZE / n) == v, n
        result[str(PAPER / n)] = v
    assert {p.relative_to(FREEZE).as_posix() for p in (FREEZE / 'sections').rglob('*.tex')} == set(SOURCE_NAMES[3:])
    assert info(PAPER / 'main.pdf') == info(FREEZE / 'main.pdf') == info(ROUND1 / 'main.pdf')
    result[str(PAPER / 'main.pdf')] = info(PAPER / 'main.pdf')
    gates = {}
    for letter, input_round in (('a', 0), ('b', 1)):
        report = BATCH / ('qa/P209_' + letter.upper() + '_ROOT_DELTA_INSPECTION.actual.json')
        data = read_json(report)
        assert data['schema'] == 'p209-' + letter + '-root-delta-closure-v1'
        assert data['status'] == 'ROOT_ACCEPTED_' + letter.upper() + '_DELTA_ORIGINAL_CLOSURE_PASS'
        assert data['paper'] == 'P209' and type(data['input_round']) is int and data['input_round'] == input_round
        assert type(data['current_open_findings']) is int and data['current_open_findings'] == 0
        for field in ('reviewer_delta_accepted', 'root_original_inspection_complete', 'root_replay_closure_complete'):
            assert data[field] is True, field
        review = BATCH / ('reviews/p209_' + letter)
        reviewed = manifest(review, 'SHA256SUMS', complete=True)
        assert len(reviewed) - 1 == data['review_manifest_entries']
        result.update(reviewed)
        for field, path in (('review_manifest_sha256', review / 'SHA256SUMS'),
                            ('delta_sha256', review / 'DELTA.md'),
                            ('current_findings_sha256', review / 'CURRENT_FINDINGS.json'),
                            ('response_sha256', BATCH / ('P209_' + letter.upper() + '_RESPONSE.md'))):
            assert info(path)['sha256'] == data[field], field
            result[str(path)] = info(path)
        current = read_json(review / 'CURRENT_FINDINGS.json')
        assert current['schema'] == 'p209-manuscript-review-findings-v1'
        assert current['input_round'] == input_round and current['reviewer'] == '/root/p209_' + letter + '_reviewer'
        assert current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'
        assert current['current_open_counts'] == {'critical': 0, 'major': 0, 'minor': 0}
        assert current['findings'] == [] and current['scientific_inputs_changed'] is False
        assert current['response_sha256'] == data['response_sha256']
        narrative = report.with_name(report.name.replace('.actual.json', '.md'))
        result[str(narrative)] = info(narrative)
        gates[letter] = (report, data)
    b = gates['b'][1]
    assert b['round1_path'] == str(ROUND1) and b['round1_manifest_sha256'] == core[str(ROUND1 / 'SHA256SUMS')]['sha256']
    assert b['unchanged_author_payloads'] == 1985 and b['unchanged_round1_payloads'] == 2003
    receipt = BATCH / 'qa/P209_ROUND2_ROOT_INSPECTION.actual.json'
    closure = read_json(receipt)
    assert closure['schema'] == 'p209-round2-root-physical-closure-v1'
    assert closure['status'] == 'PASS_ROOT_ROUND2_COMPLETE_PHYSICAL_CLOSURE' and closure['paper'] == 'P209'
    assert type(closure['round']) is int and closure['round'] == 2
    assert type(closure['current_open_findings']) is int and closure['current_open_findings'] == 0
    assert closure['round2_manifest_sha256'] == frozen[str(FREEZE / 'SHA256SUMS')]['sha256']
    assert type(closure['round2_payloads']) is int and closure['round2_payloads'] == len(frozen) - 1
    for letter in ('a', 'b'):
        assert closure['accepted_' + letter.upper() + '_root_gate_sha256'] == info(gates[letter][0])['sha256']
    assert set(closure['source_pins']) == {str(PAPER / n) for n in SOURCE_NAMES}
    for n, value in expected_sources.items():
        actual = closure['source_pins'][str(PAPER / n)]
        assert all(actual[k] == value[k] for k in ('sha256', 'bytes'))
    result[str(receipt.with_name('P209_ROUND2_ROOT_INSPECTION.md'))] = info(receipt.with_name('P209_ROUND2_ROOT_INSPECTION.md'))
    provenance = read_json(FREEZE / 'ROUND2_PROVENANCE.json')
    assert provenance['schema'] == 'p209-round2-provenance-v1'
    assert provenance['round1_core_payloads_copied'] == 2003 and provenance['author_payloads_preserved'] == 1985
    core_rows = {Path(p).relative_to(ROUND1).as_posix(): v['sha256'] for p, v in core.items()
                 if p != str(ROUND1 / 'SHA256SUMS')}
    assert provenance['core_payload_pins'] == core_rows
    assert all(frozen[str(FREEZE / n)]['sha256'] == h for n, h in core_rows.items())
    assert provenance['accepted_root_assertions'] == b
    pair = BATCH / 'qa/root_replays/p209_b_strict/root_b_pair_01'
    launcher = BATCH / 'qa/root_replays/p209_b_strict/launcher_root_b_pair_01'
    for path, key in ((pair, 'root_pair_manifest_sha256'), (launcher, 'root_launcher_manifest_sha256')):
        closed = manifest(path, 'SHA256SUMS', complete=True)
        assert closed[str(path / 'SHA256SUMS')]['sha256'] == b[key]
        result.update(closed)
    anchors = {
        'ROUND1_CORE_MANIFEST.sha256': ROUND1 / 'SHA256SUMS',
        'B_REVIEW_MANIFEST.sha256': BATCH / 'reviews/p209_b/SHA256SUMS',
        'B_INITIAL_REVIEW_SEAL.sha256': BATCH / 'reviews/p209_b/INITIAL_REVIEW_SEAL.sha256',
        'B_DELTA.md': BATCH / 'reviews/p209_b/DELTA.md',
        'B_INITIAL_DELTA.md': BATCH / 'reviews/p209_b/INITIAL_DELTA.md',
        'B_INITIAL_FINDINGS.json': BATCH / 'reviews/p209_b/FINDINGS.json',
        'B_CURRENT_FINDINGS.json': BATCH / 'reviews/p209_b/CURRENT_FINDINGS.json',
        'B_INPUT_PINS.sha256': BATCH / 'reviews/p209_b/INPUT_PINS.sha256',
        'ROOT_RESPONSE.md': BATCH / 'P209_B_RESPONSE.md',
        'ROOT_INITIAL_INSPECTION.md': BATCH / 'qa/P209_B_ROOT_INITIAL_INSPECTION.md',
        'ROOT_DELTA_INSPECTION.md': BATCH / 'qa/P209_B_ROOT_DELTA_INSPECTION.md',
        'ROOT_DELTA_CLOSURE.actual.json': gates['b'][0],
        'ROOT_PAIR_MANIFEST.sha256': pair / 'SHA256SUMS',
        'ROOT_LAUNCHER_MANIFEST.sha256': launcher / 'SHA256SUMS',
        'PRE_ROUND2_PAPER_MANIFEST.sha256': PAPER / 'PAPER_MANIFEST.sha256',
    }
    assert set(provenance['anchor_mapping']) == set(anchors)
    for name, original in anchors.items():
        row = provenance['anchor_mapping'][name]
        local = 'ROUND2_ACCEPTANCE/' + name
        assert row['original_path'] == str(original) and row['physical_path'] == local
        assert frozen[str(FREEZE / local)]['sha256'] == row['sha256']
        if name == 'PRE_ROUND2_PAPER_MANIFEST.sha256':
            # Exact historical PAPER-relative role, not the later live whole seal.
            assert row['sha256'] == '3e94a72637733ca46f7950f4feb8508fdf14b5ff6386c971821932ae9231e5a9'
        else:
            assert info(original)['sha256'] == row['sha256']
            result[str(original)] = info(original)
    aliases = {}
    for row in provenance['historical_input_resolution']:
        local = row['copy_relative']
        if local is not None:
            path = Path(local)
            assert path.as_posix() == local and path.parts[0] == 'ROUND2_HISTORICAL_ALIASES' and '..' not in path.parts
            assert local not in aliases and row['round2_physical_path'] == str(FREEZE / local)
            assert frozen[str(FREEZE / local)]['sha256'] == row['sha256']
            aliases[local] = row['sha256']
    expected_names = set(core_rows) | {'ROUND2_ACCEPTANCE/' + n for n in anchors} | set(aliases)
    expected_names |= {'ROUND2_FREEZE_ADAPTER.py', 'ROUND2_PROVENANCE.json'}
    assert {Path(p).relative_to(FREEZE).as_posix() for p in frozen if p != str(FREEZE / 'SHA256SUMS')} == expected_names
    assert closure['round2_payloads'] == 2020 + len(aliases)
    assert info(FREEZE / 'ROUND2_FREEZE_ADAPTER.py')['sha256'] == '787357029ae3d4f50c1a9998a3b1e4fe9377786cc06cb024e3a7a96ef95b46c7'
    result[str(SCRIPT)] = info(SCRIPT)
    result[str(ROOT_LAUNCHER)] = info(ROOT_LAUNCHER)
    return result

def tree_inventory(roots):
    return pins(p for root in roots if root.is_dir() for p in root.rglob('*') if p.is_file())


def is_elf(path):
    with Path(path).open('rb') as stream:
        return stream.read(4) == b'\x7fELF'


def runtime_inventory():
    std = []
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        std.extend(Path(directory) / n for n in files if not n.endswith(('.pyc', '.pyo')))
    potential = []
    for root in LIB_ROOTS:
        if root.is_dir():
            entries = root.glob('*') if root == Path('/usr/local/lib') else root.rglob('*')
            potential.extend(p for p in entries if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    return pins(std + potential + TOOLS)

def configuration():
    candidates = set(CONFIG_ROOTS + TEX_ROOTS + TOOLS)
    candidates.update(Path(p) for p in ('/etc/ld.so.cache', '/etc/ld.so.conf',
        '/etc/ld.so.preload', '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2',
        '/libx32/ld-linux-x32.so.2'))
    candidates.add(STDLIB.parent / ('python%d%d.zip' % sys.version_info[:2]))
    candidates.update([PYTHON.parent / 'pyvenv.cfg', PYTHON.parent.parent / 'pyvenv.cfg',
        PYTHON.with_name(PYTHON.name + '._pth'), PYTHON.with_name('python._pth'),
        Path('/etc/locale.conf'), Path('/etc/default/locale'),
        Path('/etc/nsswitch.conf'), Path('/etc/localtime'), Path('/etc/bash.bashrc'), Path('/etc/profile'),
        Path('/usr/lib/locale/locale-archive'), Path('/etc/passwd'), Path('/etc/group'),
        Path('/root/.fonts.conf'), Path('/root/.config/fontconfig/fonts.conf'), Path('/etc/fonts/local.conf'),
        Path(sysconfig.get_makefile_filename()), Path(sysconfig.get_config_h_filename())])
    names = {'python._pth', 'python3._pth', 'python%d%d._pth' % sys.version_info[:2],
             'python%d.%d._pth' % sys.version_info[:2], PYTHON.name + '._pth'}
    for directory in {PYTHON.parent, Path(sys.executable).parent, STDLIB.parent}:
        candidates.update(directory / name for name in names)
    for key in ('LDLIBRARY', 'INSTSONAME'):
        value = sysconfig.get_config_var(key)
        if value:
            candidates.add(STDLIB.parent / (value + '._pth'))
    ldd = Path('/usr/bin/ldd').read_text()
    match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    assert ldd.splitlines()[0] == '#!/bin/bash' and match
    candidates.update(Path(p) for p in match.group(1).split())
    for root in CONFIG_ROOTS:
        if root.is_dir():
            candidates.update(p for p in root.rglob('*') if p.is_file())
    return {str(p): {'exists': p.exists(), 'is_file': p.is_file(),
                    'resolved': str(p.resolve()), **(info(p) if p.is_file() else {})}
            for p in sorted(candidates)}


def current_parent_runtime(phase):
    modules = {}
    for name, module in sorted(sys.modules.items()):
        origin = getattr(module, '__file__', None)
        if origin and Path(origin).is_file():
            p = Path(origin).resolve()
            assert p.suffix != '.pyc', str(p)
            modules[name] = {'path': str(p), **info(p)}
    mapped = {}
    for line in Path('/proc/self/maps').read_text().splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            p = Path(fields[5]).resolve()
            assert p.is_file(), str(p)
            mapped[str(p)] = info(p)
    return {'modules': modules, 'mapped_files': mapped, 'flags': repr(sys.flags),
            'sys_path': sys.path, 'executable': str(PYTHON), 'version': sys.version,
            'pycache_prefix': sys.pycache_prefix, 'original_argv': sys.orig_argv,
            'cwd': str(Path.cwd()), 'environment': dict(os.environ), 'pid': os.getpid(),
            'phase': phase, 'utc': datetime.now(timezone.utc).isoformat(),
            'mapping_scope': 'This parent only; file-backed map snapshot, not child or transient access trace.'}


def main():
    # These guards must remain effective even with -O and run before any output.
    if sys.argv[1:] != ['terminal-pair-after-round2'] or sys.flags.optimize != 0:
        raise RuntimeError('Require exact terminal-pair-after-round2 argument and optimization zero')
    if SCRIPT != PREPARATION / 'root_terminal_builds.py' or PYTHON != Path('/usr/bin/python3.10'):
        raise RuntimeError('Require exact prepared recorder path and Python 3.10')
    if sys.flags.isolated != 1 or sys.flags.no_site != 1 or not sys.dont_write_bytecode:
        raise RuntimeError('Require -I -S -B')
    if sys.pycache_prefix != str(OUT / 'never_created_parent_cache') or Path(sys.pycache_prefix).exists():
        raise RuntimeError('Require exact absent terminal recorder cache prefix')
    if OUT.resolve() != OUT or OUT.exists() or OUT.is_symlink():
        raise RuntimeError('Refuse aliased or existing terminal output root')
    if dict(os.environ) != ENV or Path.cwd().resolve() != ROOT:
        raise RuntimeError('Require exact controlled ENV and workspace cwd; environment values not dumped on refusal')
    # No output/build directory is made before the real acceptance gates pass.
    before = science()
    OUT.mkdir(exist_ok=False)
    save(OUT / 'executed_recorder_snapshot.py', Path(__file__).read_bytes())
    dump(OUT / 'INPUTS_BEFORE.json', before)
    commands, builds, failures = [], [], []
    generated_tex = {}
    runtime_before, config_before, tex_before, libs_before = {}, {}, {}, {}
    consumed = {}
    parent_before, parent_pins_before, user_roots = {}, {}, {}
    began = datetime.now(timezone.utc).isoformat()

    def command(label, argv, cwd):
        started = datetime.now(timezone.utc).isoformat()
        row = {'label': label, 'argv': argv, 'cwd': str(cwd), 'environment': ENV,
               'started_utc': started, 'status': 'ATTEMPTED', 'exit_code': None,
               'start_new_session': True, 'cleanup': []}
        dump(OUT / (label + '.attempt.json'), row)
        commands.append(row)
        proc = None
        try:
            with (OUT / (label + '.stdout')).open('xb') as stdout, (OUT / (label + '.stderr')).open('xb') as stderr:
                proc = subprocess.Popen(argv, cwd=cwd, env=ENV, stdout=stdout, stderr=stderr, start_new_session=True)
                UNREAPED_CHILDREN.add(proc.pid)
                row.update(pid=proc.pid, status='UNKNOWN_UNTIL_WAIT')
                code = proc.wait()
                UNREAPED_CHILDREN.discard(proc.pid)
                row.update(status='COMPLETED', exit_code=code)
        except BaseException as error:
            row.update(status='NOT_STARTED' if proc is None else 'NO_COMPLETED_CHILD_RESULT',
                       exception_type=type(error).__name__, exception_message=str(error))
        finally:
            if proc is not None and proc.pid in UNREAPED_CHILDREN:
                try:
                    if proc.poll() is None:
                        try:
                            os.killpg(proc.pid, signal.SIGTERM)
                            row['cleanup'].append({'action': 'SIGTERM_OWNED_PROCESS_GROUP', 'pgid': proc.pid})
                        except ProcessLookupError:
                            pass
                    try:
                        cleaned = proc.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        os.killpg(proc.pid, signal.SIGKILL)
                        row['cleanup'].append({'action': 'SIGKILL_OWNED_PROCESS_GROUP', 'pgid': proc.pid})
                        cleaned = proc.wait(timeout=5)
                    try:
                        os.killpg(proc.pid, signal.SIGKILL)
                        row['cleanup'].append({'action': 'SIGKILL_REMAINING_OWNED_GROUP', 'pgid': proc.pid})
                    except ProcessLookupError:
                        pass
                    row['cleanup'].append({'action': 'DIRECT_CHILD_REAPED', 'cleanup_exit': cleaned,
                                           'does_not_replace_original_exit': True})
                    UNREAPED_CHILDREN.discard(proc.pid)
                except BaseException:
                    row['cleanup'].append({'action': 'CLEANUP_FAILED_DO_NOT_SEAL', 'traceback': traceback.format_exc()})
            row['ended_utc'] = datetime.now(timezone.utc).isoformat()
            if not UNREAPED_CHILDREN:
                for kind in ('stdout', 'stderr'):
                    path = OUT / (label + '.' + kind)
                    if path.is_file():
                        row[kind] = {'path': path.name, **info(path)}
            else:
                row['stream_scope'] = 'Raw streams only; no settled-stream hashes while owned child unreaped.'
            dump(OUT / (label + '.command.json'), row)
        assert row['status'] == 'COMPLETED' and row['exit_code'] == 0, (label, row)
        return subprocess.CompletedProcess(argv, row['exit_code'],
                   (OUT / (label + '.stdout')).read_bytes(), (OUT / (label + '.stderr')).read_bytes())

    def library_capture(label):
        candidates = {str(p.resolve()) for p in TOOLS if p.name != 'ldd'}
        candidates.update(p for p in runtime_before if Path(p).is_relative_to(STDLIB) and p.endswith('.so'))
        objects = sorted(p for p in candidates if is_elf(p))
        assert objects, 'no ELF linkage targets'
        raw = command(label, ['/usr/bin/ldd', *objects], OUT).stdout.decode()
        assert 'not found' not in raw
        paths = [Path(p).resolve() for p in re.findall(r'/[^\s():]+', raw) if Path(p).is_file()]
        assert paths
        values = pins(paths)
        assert all(runtime_before.get(path) == value for path, value in values.items()), 'ldd dependency absent from pre-child runtime inventory'
        return values

    def failure(phase, error):
        failures.append({'phase': phase, 'type': type(error).__name__, 'message': str(error)})
        save(OUT / (phase + '_exception.txt'), traceback.format_exc().encode())

    try:
        parent_before = current_parent_runtime('before_resource_inventory_and_children')
        dump(OUT / 'RECORDER_RUNTIME_BEFORE.json', parent_before)
        parent_pins_before = {**parent_before['mapped_files'],
            **{v['path']: {k: v[k] for k in ('sha256', 'bytes')} for v in parent_before['modules'].values()}}
        dump(OUT / 'RECORDER_INPUTS_BEFORE.json', parent_pins_before)
        runtime_before = runtime_inventory()
        dump(OUT / 'RUNTIME_BEFORE.json', runtime_before)
        config_before = configuration()
        dump(OUT / 'CONFIGURATION_BEFORE.json', config_before)
        dump(OUT / 'INTERPRETER_CONFIGURATION.json', {'sysconfig_paths': sysconfig.get_paths(),
             'sysconfig_vars': sysconfig.get_config_vars(), 'stdlib': str(STDLIB),
             'potential_library_roots': list(map(str, LIB_ROOTS)),
             'bash_mode': 'Noninteractive non-login ldd shell; ENV/BASH_ENV absent.'})
        tex_before = tree_inventory(TEX_ROOTS)
        dump(OUT / 'TEX_INVENTORY_BEFORE.json', tex_before)
        libs_before = library_capture('ldd_before')
        dump(OUT / 'LIBRARIES_BEFORE.json', libs_before)
        for tool in ('pdflatex', 'bibtex'):
            command(tool + '_version', ['/usr/bin/' + tool, '--version'], OUT)
        command('texmf_roots', ['/usr/bin/kpsewhich', '-var-value=TEXMF'], OUT)
        sources = [FREEZE / n for n in SOURCE_NAMES]
        assert len(sources) == 8
        for k in (1, 2):
            label = 'cold_build_' + str(k)
            cold = OUT / label
            cold.mkdir()
            for p in sources:
                q = cold / p.relative_to(FREEZE)
                q.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(p, q)
            initial = {p.relative_to(cold).as_posix(): info(p) for p in cold.rglob('*') if p.is_file()}
            assert initial == {n: info(FREEZE / n) for n in SOURCE_NAMES} and len(initial) == 8
            assert not any(Path(n).suffix in ('.pdf', '.bbl', '.aux') for n in initial)
            dump(OUT / (label + '_SOURCE_ONLY_INITIAL.json'), initial)
            for variable in USER_TEX_VARS:
                raw = command(label + '_' + variable, ['/usr/bin/kpsewhich', '-var-value=' + variable], cold).stdout.decode().strip()
                p = Path(raw); p = (p if p.is_absolute() else cold / p).resolve()
                assert raw and not p.exists(), (variable, raw, str(p))
                user_roots[label + ':' + variable] = {'query_value': raw, 'resolved': str(p), 'exists': False}
            dump(OUT / (label + '_USER_ROOTS_BEFORE.json'),
                 {k: v for k, v in user_roots.items() if k.startswith(label + ':')})
            for j in (1, 2, 3):
                command(label + '_tex' + str(j), ['/usr/bin/pdflatex', '-no-shell-escape',
                    '-recorder', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'], cold)
                for suffix in ('log', 'fls', 'aux'):
                    save(OUT / (label + '_pass' + str(j) + '.' + suffix), (cold / ('main.' + suffix)).read_bytes())
                for line in (cold / 'main.fls').read_text().splitlines():
                    if line.startswith('INPUT '):
                        p = Path(line[6:]); p = (p if p.is_absolute() else cold / p).resolve()
                        assert p.is_file(), str(p)
                        value = info(p)
                        if not p.is_relative_to(cold):
                            assert tex_before.get(str(p)) == value, str(p)
                            consumed[str(p)] = value
                        else:
                            name = p.relative_to(cold).as_posix()
                            if name in initial:
                                assert value == initial[name], str(p)
                            else:
                                assert p.suffix in {'.aux', '.bbl', '.out', '.toc'}, str(p)
                                generated_tex[label + ':pass' + str(j) + ':' + name] = value
                dump(OUT / (label + '_pass' + str(j) + '_TEX_INPUTS.json'),
                     {'consumed_external': consumed, 'generated_local': generated_tex})
                if j == 1:
                    bst = command(label + '_bst', ['/usr/bin/kpsewhich', 'plainnat.bst'], cold).stdout.decode().strip()
                    bp = Path(bst).resolve()
                    assert tex_before[str(bp)] == info(bp)
                    consumed[str(bp)] = info(bp)
                    command(label + '_bibtex', ['/usr/bin/bibtex', 'main'], cold)
                    save(OUT / (label + '_generated.bbl'), (cold / 'main.bbl').read_bytes())
                    save(OUT / (label + '_generated.blg'), (cold / 'main.blg').read_bytes())
            raw_info = command(label + '_pdfinfo', ['/usr/bin/pdfinfo', 'main.pdf'], cold).stdout.decode()
            font_text = command(label + '_pdffonts', ['/usr/bin/pdffonts', 'main.pdf'], cold).stdout.decode()
            command(label + '_pdftotext', ['/usr/bin/pdftotext', '-layout', 'main.pdf', str(OUT / (label + '_main.txt'))], cold)
            pages = cold / 'pages'; pages.mkdir()
            command(label + '_render', ['/usr/bin/pdftoppm', '-png', '-r', '120', 'main.pdf', str(pages / 'page')], cold)
            pages_n = int(re.search(r'^Pages:\s+(\d+)$', raw_info, re.M).group(1))
            dump(OUT / (label + '_MEASURED_PDF.json'),
                 {'pages': pages_n, 'expected_pages': 4, 'rendered_pages': len(list(pages.glob('*.png'))),
                  'pdf': info(cold / 'main.pdf')})
            assert pages_n == 4 and len(list(pages.glob('*.png'))) == pages_n, ('actual_page_mismatch', pages_n)
            command(label + '_frozen_pdf_cmp', ['/usr/bin/cmp', '--', str(cold / 'main.pdf'), str(FREEZE / 'main.pdf')], cold)
            log = (cold / 'main.log').read_text()
            warnings = {k: re.findall(r'^.*' + v + r'.*$', log, re.M)
                        for k, v in [('undefined', 'undefined'), ('overfull', 'Overfull'),
                                     ('underfull', 'Underfull'), ('warnings', 'Warning')]}
            warnings['rerun'] = re.findall(r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$', log, re.M)
            assert not warnings['undefined'] and not warnings['overfull'] and not warnings['rerun']
            extracted = (OUT / (label + '_main.txt')).read_text()
            assert not any(marker in extracted for marker in ('[VERIFY]', '??', '[?]'))
            font_rows = [s.split()[-5:] for s in font_text.splitlines()[2:] if s.strip()]
            assert font_rows and all(row[0] == 'yes' for row in font_rows)
            dump(OUT / (label + '_DIAGNOSTICS.json'),
                 {'pages': pages_n, 'expected_pages': 4, 'rendered_pages': len(list(pages.glob('*.png'))),
                  'pdf': info(cold / 'main.pdf'), 'diagnostics': warnings, 'embedded_fonts': len(font_rows)})
            assert initial == {n: info(cold / n) for n in initial}
            assert all(info(Path(p)) == value for p, value in consumed.items())
            builds.append({'directory': label, 'source_only_initial': initial,
                           'pdf': info(cold / 'main.pdf'), 'pages': pages_n,
                           'embedded_fonts': len(font_rows), 'actual_diagnostics': warnings})
        command('pair_pdf_cmp', ['/usr/bin/cmp', '--', str(OUT / 'cold_build_1/main.pdf'),
                                str(OUT / 'cold_build_2/main.pdf')], OUT)
    except BaseException as error:
        failure('build_phase', error)
    # Independent capture/save: one inaccessible input never suppresses others.
    dump(OUT / 'CONSUMED_TEX_BEFORE.json', consumed)
    dump(OUT / 'GENERATED_LOCAL_TEX_INPUTS.json', generated_tex)
    after_values = {}
    collectors = [
        ('INPUTS_AFTER', science), ('RUNTIME_AFTER', runtime_inventory),
        ('CONFIGURATION_AFTER', configuration), ('TEX_INVENTORY_AFTER', lambda: tree_inventory(TEX_ROOTS)),
        ('LIBRARIES_AFTER', lambda: library_capture('ldd_after')),
        ('CONSUMED_TEX_AFTER', lambda: pins(consumed)),
        ('RECORDER_INPUTS_AFTER', lambda: pins(parent_pins_before)),
        ('RECORDER_RUNTIME_AFTER', lambda: current_parent_runtime('after_children_and_resource_inventories')),
        ('USER_ROOTS_AFTER', lambda: {k: {**v, 'exists': Path(v['resolved']).exists()} for k, v in user_roots.items()})]
    for name, collect in collectors:
        try:
            value = collect()
            dump(OUT / (name + '.json'), value)
            after_values[name] = value
        except BaseException as error:
            failure('capture_' + name, error)
    for name, value in [('INPUTS_AFTER', before), ('RUNTIME_AFTER', runtime_before),
        ('CONFIGURATION_AFTER', config_before), ('TEX_INVENTORY_AFTER', tex_before),
        ('LIBRARIES_AFTER', libs_before), ('CONSUMED_TEX_AFTER', consumed),
        ('RECORDER_INPUTS_AFTER', parent_pins_before), ('USER_ROOTS_AFTER', user_roots)]:
        try:
            assert value and after_values.get(name) == value, name
        except BaseException as error:
            failure('compare_' + name, error)
    try:
        parent = after_values['RECORDER_RUNTIME_AFTER']
        normalized_config = {v['resolved']: {k: v[k] for k in ('sha256', 'bytes')}
                             for v in config_before.values() if v['is_file']}
        coverage = {**before, **runtime_before, **libs_before, **normalized_config, **parent_pins_before}
        for value in parent['modules'].values():
            assert coverage[value['path']] == {k: value[k] for k in ('sha256', 'bytes')}, value['path']
        for path, value in parent['mapped_files'].items():
            assert coverage[path] == value, path
        assert not Path(sys.pycache_prefix).exists()
        assert parent['environment'] == ENV
    except BaseException as error:
        failure('parent_coverage', error)
    if UNREAPED_CHILDREN:
        dump(OUT / 'UNCLOSED_BUILD.json', {'status': 'UNCLOSED_BUILD_NO_SEAL',
             'unreaped_owned_children': sorted(UNREAPED_CHILDREN), 'commands': commands, 'failures': failures,
             'scope': 'Do not hash unsettled output, create final manifest or infer descendant termination.'})
        print(json.dumps({'status': 'UNCLOSED_BUILD_NO_SEAL', 'output': str(OUT)}))
        raise SystemExit(1)
    expected_labels = ['ldd_before', 'pdflatex_version', 'bibtex_version', 'texmf_roots']
    for k in (1, 2):
        label = 'cold_build_' + str(k)
        expected_labels.extend(label + '_' + v for v in USER_TEX_VARS)
        expected_labels.extend(label + '_' + v for v in ('tex1', 'bst', 'bibtex', 'tex2', 'tex3',
                               'pdfinfo', 'pdffonts', 'pdftotext', 'render', 'frozen_pdf_cmp'))
    expected_labels.extend(['pair_pdf_cmp', 'ldd_after'])
    census_okay = [c['label'] for c in commands] == expected_labels
    if not census_okay:
        failures.append({'phase': 'command_census', 'actual': [c['label'] for c in commands], 'expected': expected_labels})
    passed = not failures and len(builds) == 2 and all(c['status'] == 'COMPLETED' and c['exit_code'] == 0 for c in commands)
    receipt = {'status': 'PASS_P209_TERMINAL_BUILD_PAIR_NOT_VIEWED' if passed else 'FAIL_PRESERVED',
        'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'commands': commands, 'builds': builds, 'failures': failures,
        'command_census_complete': census_okay, 'expected_command_labels': expected_labels,
        'input_count': len(before), 'runtime_count': len(runtime_before),
        'configuration_count': len(config_before), 'tex_inventory_count': len(tex_before),
        'consumed_tex_count': len(consumed), 'resolved_link_file_count': len(libs_before),
        'visual_review': 'PENDING_NOT_INFERRED_FROM_HASH_OR_RENDER',
        'parent_launch': sys.orig_argv, 'parent_cwd': str(Path.cwd()), 'parent_environment': dict(os.environ),
        'boundary': ('Before/after byte inventories of known runtime, TeX and potential font/Poppler/gconv resources; '
            'ldd link-time closure; actual early/late parent file-backed map samples; TeX .fls per-pass inputs observed. '
            'TeX/BibTeX/Poppler child maps, transient dlopen and non-fls resource accesses are not directly observed. '
            'No claim of hermetic OS/kernel reconstruction or continuous tracing.'),
        'external': 'HOLD_EXTERNAL'}
    dump(OUT / 'BUILD_EXECUTION.json', receipt)
    rows = [(info(p)['sha256'], p.relative_to(OUT).as_posix()) for p in sorted(OUT.rglob('*')) if p.is_file()]
    save(OUT / 'SHA256SUMS', ''.join(d + '  ' + n + '\n' for d, n in rows).encode())
    manifest(OUT, 'SHA256SUMS', complete=True)
    print(json.dumps({k: receipt[k] for k in ('status', 'builds', 'failures', 'input_count',
        'runtime_count', 'configuration_count', 'tex_inventory_count', 'consumed_tex_count',
        'resolved_link_file_count')}, sort_keys=True, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
