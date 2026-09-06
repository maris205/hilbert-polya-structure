#!/usr/bin/env python3
"""Gated P208 terminal source-only build pair; no overwrite or visual verdict.

Prepared during B; execution requires both actual root-accepted deltas and
physical Round2. Existing A/author/P207 recorders are immutable and not imported.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import sysconfig
import traceback

ROOT = Path(__file__).resolve().parents[3]
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/208-original-snapshot-triangulation-sweeps'
FREEZE = PAPER / 'frozen_round2'
OUT = PAPER / 'qa_final'
PYTHON = Path(sys.executable).resolve()
STDLIB = Path(sysconfig.get_path('stdlib')).resolve()
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
       'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788652800', 'FORCE_SOURCE_DATE': '1',
       'openin_any': 'p', 'openout_any': 'p'}
TOOLS = [Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich',
         'pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp')]
TOOLS += [Path('/bin/bash'), PYTHON]
TEX_ROOTS = [Path(p) for p in (
    '/usr/share/texlive/texmf-dist/tex', '/usr/share/texlive/texmf-dist/fonts',
    '/usr/share/texlive/texmf-dist/web2c', '/usr/share/texlive/texmf-dist/bibtex',
    '/usr/share/texmf', '/var/lib/texmf', '/etc/texmf', '/usr/local/share/texmf',
    '/root/texmf', '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')]
CONFIG_ROOTS = [Path(p) for p in ('/etc/ld.so.conf.d', '/usr/share/fonts',
    '/etc/fonts', '/var/cache/fontconfig', '/usr/share/fontconfig', '/usr/lib/locale/C.utf8')]


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
    source = base / name
    records = {}
    for line in source.read_text().splitlines():
        digest, rel = line.split('  ', 1)
        local = Path(rel)
        assert not local.is_absolute() and '..' not in local.parts and local.parts
        assert rel != name and rel not in records
        p = base / local
        assert p.is_file() and not p.is_symlink() and info(p)['sha256'] == digest, str(p)
        records[rel] = info(p)
    if complete:
        assert set(records) == {p.relative_to(base).as_posix() for p in base.rglob('*')
                                if p.is_file() and p != source}
    records[name] = info(source)
    return {str(base / n): v for n, v in records.items()}


def science():
    result = manifest(FREEZE, 'SHA256SUMS', complete=True)
    for path, value in list(result.items()):
        rel = Path(path).relative_to(FREEZE)
        if rel.as_posix() == 'SHA256SUMS':
            continue
        assert info(PAPER / rel) == value, str(PAPER / rel)
        result[str(PAPER / rel)] = value
    for letter in ('a', 'b'):
        report = BATCH / ('qa/P208_' + letter.upper() + '_ROOT_DELTA_INSPECTION.actual.json')
        data = json.loads(report.read_bytes())
        assert data['status'] == 'ROOT_ACCEPTED_' + letter.upper() + '_DELTA_ORIGINAL_CLOSURE_PASS'
        assert data['current_open_findings'] == 0
        review = BATCH / ('reviews/p208_' + letter)
        assert info(review / 'SHA256SUMS')['sha256'] == data['review_manifest_sha256']
        assert info(review / 'DELTA.md')['sha256'] == data['delta_sha256']
        result.update(manifest(review, 'SHA256SUMS', complete=True))
        result[str(report)] = info(report)
    result[str(Path(__file__).resolve())] = info(Path(__file__).resolve())
    return result


def tree_inventory(roots):
    return pins(p for root in roots if root.is_dir() for p in root.rglob('*') if p.is_file())


def runtime_inventory():
    return pins([p for p in STDLIB.rglob('*') if p.is_file()
                 and 'site-packages' not in p.parts and '__pycache__' not in p.parts] + TOOLS)


def configuration():
    candidates = set(CONFIG_ROOTS + TEX_ROOTS + TOOLS)
    candidates.update(Path(p) for p in ('/etc/ld.so.cache', '/etc/ld.so.conf',
        '/etc/ld.so.preload', '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2',
        '/libx32/ld-linux-x32.so.2'))
    candidates.add(STDLIB.parent / ('python%d%d.zip' % sys.version_info[:2]))
    for root in CONFIG_ROOTS:
        if root.is_dir():
            candidates.update(p for p in root.rglob('*') if p.is_file())
    return {str(p): {'exists': p.exists(), 'is_file': p.is_file(),
                    'resolved': str(p.resolve()), **(info(p) if p.is_file() else {})}
            for p in sorted(candidates)}


def current_parent_runtime():
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
            'pycache_prefix': sys.pycache_prefix}


def main():
    assert len(sys.argv) == 1
    assert sys.flags.optimize == 0 and sys.flags.isolated == sys.flags.no_site == 1
    assert sys.dont_write_bytecode and sys.pycache_prefix
    assert not Path(sys.pycache_prefix).exists()
    # No output/build directory is made before the real acceptance gates pass.
    before = science()
    OUT.mkdir(exist_ok=False)
    save(OUT / 'executed_recorder_snapshot.py', Path(__file__).read_bytes())
    dump(OUT / 'INPUTS_BEFORE.json', before)
    commands, builds, failures = [], [], []
    runtime_before, config_before, tex_before, libs_before = {}, {}, {}, {}
    consumed = {}
    began = datetime.now(timezone.utc).isoformat()

    def command(label, argv, cwd):
        started = datetime.now(timezone.utc).isoformat()
        child = subprocess.run(argv, cwd=cwd, env=ENV, capture_output=True, check=False)
        row = {'label': label, 'argv': argv, 'cwd': str(cwd), 'environment': ENV,
               'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
               'exit_code': child.returncode}
        for kind, raw in [('stdout', child.stdout), ('stderr', child.stderr)]:
            path = OUT / (label + '.' + kind)
            save(path, raw)
            row[kind] = {'path': path.name, **info(path)}
        commands.append(row)
        dump(OUT / (label + '.command.json'), row)
        assert child.returncode == 0, (label, child.returncode)
        return child

    def library_capture(label):
        objects = sorted({str(p.resolve()) for p in TOOLS if p.name != 'ldd'} |
                         {p for p in runtime_before if p.endswith('.so')})
        raw = command(label, ['/usr/bin/ldd', *objects], OUT).stdout.decode()
        assert 'not found' not in raw
        paths = [Path(p).resolve() for p in re.findall(r'/[^\s():]+', raw) if Path(p).is_file()]
        assert paths
        return pins(paths)

    def failure(phase, error):
        failures.append({'phase': phase, 'type': type(error).__name__, 'message': str(error)})
        save(OUT / (phase + '_exception.txt'), traceback.format_exc().encode())

    try:
        runtime_before = runtime_inventory()
        config_before = configuration()
        tex_before = tree_inventory(TEX_ROOTS)
        dump(OUT / 'RUNTIME_BEFORE.json', runtime_before)
        dump(OUT / 'CONFIGURATION_BEFORE.json', config_before)
        dump(OUT / 'TEX_INVENTORY_BEFORE.json', tex_before)
        libs_before = library_capture('ldd_before')
        dump(OUT / 'LIBRARIES_BEFORE.json', libs_before)
        for tool in ('pdflatex', 'bibtex'):
            command(tool + '_version', ['/usr/bin/' + tool, '--version'], OUT)
        command('texmf_roots', ['/usr/bin/kpsewhich', '-var-value=TEXMF'], OUT)
        sources = [FREEZE / n for n in ('main.tex', 'math_commands.tex', 'references.bib')]
        sources += sorted((FREEZE / 'sections').glob('*.tex'))
        assert len(sources) == 11
        for k in (1, 2):
            label = 'cold_build_' + str(k)
            cold = OUT / label
            cold.mkdir()
            for p in sources:
                q = cold / p.relative_to(FREEZE)
                q.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(p, q)
            initial = {p.relative_to(cold).as_posix(): info(p) for p in cold.rglob('*') if p.is_file()}
            assert len(initial) == 11 and not any(Path(n).suffix in ('.pdf', '.bbl', '.aux') for n in initial)
            dump(OUT / (label + '_SOURCE_ONLY_INITIAL.json'), initial)
            for j in (1, 2, 3):
                command(label + '_tex' + str(j), ['/usr/bin/pdflatex', '-no-shell-escape',
                    '-recorder', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'], cold)
                for suffix in ('log', 'fls', 'aux'):
                    save(OUT / (label + '_pass' + str(j) + '.' + suffix), (cold / ('main.' + suffix)).read_bytes())
                for line in (cold / 'main.fls').read_text().splitlines():
                    if line.startswith('INPUT '):
                        p = Path(line[6:]); p = (p if p.is_absolute() else cold / p).resolve()
                        assert p.is_file(), str(p)
                        if not p.is_relative_to(cold):
                            value = info(p)
                            assert tex_before.get(str(p)) == value, str(p)
                            consumed[str(p)] = value
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
            command(label + '_frozen_pdf_cmp', ['/usr/bin/cmp', str(cold / 'main.pdf'), str(FREEZE / 'main.pdf')], cold)
            log = (cold / 'main.log').read_text()
            warnings = {k: re.findall(r'^.*' + v + r'.*$', log, re.M)
                        for k, v in [('undefined', 'undefined'), ('overfull', 'Overfull'),
                                     ('underfull', 'Underfull'), ('warnings', 'Warning')]}
            assert not warnings['undefined'] and not warnings['overfull']
            font_rows = [s.split()[-5:] for s in font_text.splitlines()[2:] if s.strip()]
            assert font_rows and all(row[0] == 'yes' for row in font_rows)
            pages_n = int(re.search(r'^Pages:\s+(\d+)$', raw_info, re.M).group(1))
            assert pages_n == 7 and len(list(pages.glob('*.png'))) == pages_n
            assert initial == {n: info(cold / n) for n in initial}
            assert all(info(Path(p)) == value for p, value in consumed.items())
            builds.append({'directory': label, 'source_only_initial': initial,
                           'pdf': info(cold / 'main.pdf'), 'pages': pages_n,
                           'embedded_fonts': len(font_rows), 'actual_diagnostics': warnings})
        command('pair_pdf_cmp', ['/usr/bin/cmp', str(OUT / 'cold_build_1/main.pdf'),
                                str(OUT / 'cold_build_2/main.pdf')], OUT)
    except BaseException as error:
        failure('build_phase', error)
    try:
        after = science()
        runtime_after = runtime_inventory()
        config_after = configuration()
        tex_after = tree_inventory(TEX_ROOTS)
        libs_after = library_capture('ldd_after')
        for name, values in [('INPUTS_AFTER', after), ('RUNTIME_AFTER', runtime_after),
                             ('CONFIGURATION_AFTER', config_after), ('TEX_INVENTORY_AFTER', tex_after),
                             ('LIBRARIES_AFTER', libs_after), ('CONSUMED_TEX_BEFORE', consumed),
                             ('CONSUMED_TEX_AFTER', pins(consumed))]:
            dump(OUT / (name + '.json'), values)
        assert before == after and runtime_before == runtime_after and runtime_before
        assert config_before == config_after and config_before
        assert tex_before == tex_after and tex_before and consumed
        assert libs_before == libs_after and libs_before and pins(consumed) == consumed
        parent = current_parent_runtime()
        dump(OUT / 'RECORDER_CONSUMED_RUNTIME.json', parent)
        coverage = {**before, **runtime_before, **libs_before}
        for value in parent['modules'].values():
            assert coverage[value['path']] == {k: value[k] for k in ('sha256', 'bytes')}, value['path']
        for path, value in parent['mapped_files'].items():
            assert coverage[path] == value, path
        assert not Path(sys.pycache_prefix).exists()
    except BaseException as error:
        failure('closure_phase', error)
    passed = not failures and len(builds) == 2 and all(c['exit_code'] == 0 for c in commands)
    receipt = {'status': 'PASS_P208_TERMINAL_BUILD_PAIR_NOT_VIEWED' if passed else 'FAIL',
        'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'commands': commands, 'builds': builds, 'failures': failures,
        'input_count': len(before), 'runtime_count': len(runtime_before),
        'configuration_count': len(config_before), 'tex_inventory_count': len(tex_before),
        'consumed_tex_count': len(consumed), 'resolved_link_file_count': len(libs_before),
        'visual_review': 'PENDING_NOT_INFERRED_FROM_HASH_OR_RENDER',
        'boundary': 'Contemporaneous file/resource/configuration provenance, not a hermetic OS/kernel image.',
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
