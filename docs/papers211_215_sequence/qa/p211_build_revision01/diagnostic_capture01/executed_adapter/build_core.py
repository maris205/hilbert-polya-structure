"""New bounded recorder primitives for P211 build preparation; no science.

Recording ideas are taken from the accepted P210 builder, not its schemas or
whole-host inventories. This module never compiles TeX by itself.
"""
import hashlib
import json
import locale
import os
from pathlib import Path
import re
import signal
import stat
import subprocess
import sys
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASELINE_PREP = ROOT / 'docs/papers211_215_sequence/qa/p211_build_preparation'
PREP = ROOT / 'docs/papers211_215_sequence/qa/p211_build_revision01'
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
PYTHON = Path('/usr/bin/python3.10')
ENV8 = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
        'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788825600', 'FORCE_SOURCE_DATE': '1',
        'openin_any': 'p', 'openout_any': 'p'}
SOURCES = ('main.tex', 'math_commands.tex', 'references.bib',
           'sections/0_abstract.tex', 'sections/1_introduction.tex',
           'sections/2_image.tex', 'sections/3_clock.tex',
           'sections/4_inverse.tex', 'sections/5_scope.tex')
PACKAGES = ('fontenc', 'lmodern', 'geometry', 'amsmath', 'amssymb',
            'mathtools', 'booktabs', 'microtype', 'hyperref')
TEX_COMMAND = ['/usr/bin/pdflatex', '-no-shell-escape',
               '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
               '-recorder', 'main.tex']
FOUR_COMMANDS = [('pass1', TEX_COMMAND), ('bibtex', ['/usr/bin/bibtex', 'main']),
                 ('pass2', TEX_COMMAND), ('pass3', TEX_COMMAND)]
GENERATED = frozenset('main.' + ext for ext in
                     ('aux', 'bbl', 'blg', 'log', 'fls', 'out', 'toc', 'pdf'))


def require(value, message):
    if not value:
        raise RuntimeError(message)


def digest_bytes(raw):
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def pin(path):
    path = Path(path)
    h, size = hashlib.sha256(), 0
    with path.open('rb') as stream:
        for raw in iter(lambda: stream.read(1024 * 1024), b''):
            size += len(raw)
            h.update(raw)
    return {'sha256': h.hexdigest(), 'bytes': size}


def write_new(path, value):
    path = Path(path)
    raw = value if isinstance(value, bytes) else (
        json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with path.open('xb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())


def entry(path, members=False):
    """One explicit spelling, link chain endpoint, bytes or device identity."""
    p = Path(path)
    value = {'path': str(p), 'present': os.path.lexists(p),
             'symlink': p.is_symlink(), 'resolved': str(p.resolve())}
    if p.is_symlink():
        value['link'] = os.readlink(p)
    if not value['present']:
        return value
    s = p.stat()
    if stat.S_ISREG(s.st_mode):
        value.update(kind='file', **pin(p))
    elif stat.S_ISDIR(s.st_mode):
        value['kind'] = 'directory'
        if members:
            value['members'] = sorted(child.name for child in p.iterdir())
    elif stat.S_ISCHR(s.st_mode):
        value.update(kind='character_device', major=os.major(s.st_rdev),
                     minor=os.minor(s.st_rdev))
    else:
        value.update(kind='other', mode=stat.S_IFMT(s.st_mode))
    return value


def snapshot(specs):
    return {path: entry(path, spec.get('members', False))
            for path, spec in sorted(specs.items())}


def file_coverage(records):
    result = {}
    for item in records.values():
        if item.get('kind') == 'file':
            value = {k: item[k] for k in ('sha256', 'bytes')}
            previous = result.setdefault(item['resolved'], value)
            require(previous == value, 'Conflicting duplicate resolved pin')
    return result


def physical_sources(base=PAPER):
    require(base.resolve() == base and not base.is_symlink(), 'Source root alias')
    result = {}
    for name in SOURCES:
        p = base / name
        require(p.resolve() == p and p.is_file() and not p.is_symlink(),
                'Source is not physical: ' + str(p))
        result[name] = pin(p)
    return result


def source_graph(base=PAPER):
    """Validate the read nine-file literal graph, not general TeX safety."""
    text = {name: (base / name).read_text() for name in SOURCES}
    main = text['main.tex']
    require('\\documentclass[11pt,a4paper]{amsart}' in main, 'Expected amsart')
    require('\\bibliographystyle{amsplain}' in main and
            '\\bibliography{references}' in main, 'Expected amsplain/references')
    inputs = re.findall(r'\\input\{([^}]+)\}', main)
    require([v + '.tex' if not v.endswith('.tex') else v for v in inputs] ==
            [name for name in SOURCES if name not in ('main.tex', 'references.bib')],
            'Exact ordered main input graph')
    packages = []
    for group in re.findall(r'\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}', main):
        packages.extend(group.split(','))
    require(tuple(packages) == PACKAGES, 'Actual package list changed')
    forbidden = r'\\(?:include|includegraphics|write18|openin|openout|read|catcode)\b'
    require(not any(re.search(forbidden, body) for body in text.values()),
            'Unsupported source-level external I/O or dynamic graph')
    require(not any(re.search(r'\\(?:input|usepackage|RequirePackage|documentclass)\b', body)
                    for name, body in text.items() if name != 'main.tex'),
            'Nested source dependencies require a new reviewed selector')
    sections = sorted(p.name for p in (base / 'sections').iterdir())
    require(sections == sorted(Path(n).name for n in SOURCES if n.startswith('sections/')),
            'Unexpected section membership')
    return {'sources': list(SOURCES), 'class': 'amsart', 'bibliography_style': 'amsplain',
            'packages': packages, 'inputs': inputs, 'external_figures': [],
            'limitation': 'Literal source graph, protected by exact source pins; not a TeX sandbox.'}


def runtime_sample():
    modules = {}
    for name, module in sorted(sys.modules.items()):
        raw_path = getattr(module, '__file__', None)
        if raw_path and Path(raw_path).is_file():
            p = Path(raw_path).resolve()
            require(p.suffix not in ('.pyc', '.pyo'), 'Bytecode module: ' + name)
            modules[name] = {'path': str(p), **pin(p)}
    raw = Path('/proc/self/maps').read_bytes()
    mapped = {}
    for line in raw.decode().splitlines():
        columns = line.split(None, 5)
        if len(columns) == 6 and columns[5].startswith('/'):
            p = Path(columns[5])
            require(p.is_file(), 'Unresolved/deleted parent mapping: ' + str(p))
            mapped[str(p.resolve())] = pin(p)
    return {'modules': modules, 'mapped_files': mapped,
            'maps_raw': raw.decode(), 'maps_pin': digest_bytes(raw),
            'locale_ctype': locale.setlocale(locale.LC_CTYPE),
            'argv': sys.orig_argv, 'cwd': str(Path.cwd()), 'environment': dict(os.environ),
            'flags': str(sys.flags), 'sys_path': sys.path,
            'pycache_prefix': sys.pycache_prefix}


def check_runtime(sample, coverage, extra=()):
    known = {**coverage, **{str(Path(p).resolve()): pin(p) for p in extra}}
    observed = dict(sample['mapped_files'])
    observed.update({v['path']: {k: v[k] for k in ('sha256', 'bytes')}
                     for v in sample['modules'].values()})
    require(all(known.get(path) == value for path, value in observed.items()),
            'Observed parent module/map absent from prelocked key')
    require(sample['environment'] == ENV8, 'Parent environment is not ENV8')


def session_members(sid):
    """Read process identities only for an owned session; no file inventory."""
    members = []
    for name in os.listdir('/proc'):
        if not name.isdecimal():
            continue
        try:
            raw = Path('/proc', name, 'stat').read_text()
            fields = raw[raw.rfind(')') + 2:].split()
            if int(fields[3]) == sid:
                members.append({'pid': int(name), 'state': fields[0],
                                'ppid': int(fields[1]), 'pgrp': int(fields[2]),
                                'session': int(fields[3]), 'starttime': int(fields[19])})
        except (FileNotFoundError, ProcessLookupError):
            continue
    return sorted(members, key=lambda x: x['pid'])


def run_native(root, label, argv, cwd, inputs=(), timeout=120, expected=(0,)):
    """Record native bytes and actual wait status; no retry or output deletion."""
    work = root / 'commands' / label
    work.mkdir(parents=True, exist_ok=False)
    row = {'schema': 'p211-native-attempt-v1', 'label': label,
           'argv': [str(x) for x in argv], 'cwd': str(cwd), 'environment': ENV8,
           'stdin': {'path': '/dev/null', 'policy': 'DEVNULL'},
           'timeout_seconds': timeout, 'requested_new_session': True,
           'attempted_epoch': time.time(), 'expected_exit_codes': list(expected)}
    write_new(work / 'ATTEMPT.json', row)
    proc, error, reason, native_exit = None, None, 'NOT_SPAWNED', None
    # BLD-I1: before Popen returns an actual handle, native writer outcome
    # is unknown. Neither a constructor exception nor missing pid proves
    # that no writer exists. Only the owned-session wait below may settle.
    settled, members, interventions = False, [], []
    try:
        direct = {str(p): entry(p) for p in [Path(argv[0]), Path('/dev/null'), *map(Path, inputs)]}
        require(direct['/dev/null'].get('kind') == 'character_device' and
                (direct['/dev/null']['major'], direct['/dev/null']['minor']) == (1, 3),
                'Exact stdin character device')
        write_new(work / 'INPUTS_BEFORE.json', direct)
        with (work / 'stdout.raw').open('xb') as stdout, (work / 'stderr.raw').open('xb') as stderr:
            proc = subprocess.Popen(row['argv'], cwd=cwd, env=ENV8,
                                    stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                    start_new_session=True)
            write_new(work / 'SPAWNED.json', {'pid': proc.pid, 'session': proc.pid,
                                           'spawned_epoch': time.time()})
            native_exit = proc.wait(timeout=timeout)
            reason = 'NATIVE_EXIT'
    except subprocess.TimeoutExpired:
        reason, error = 'TIMEOUT', traceback.format_exc()
    except BaseException:
        reason, error = 'SPAWN_OR_RECORDER_EXCEPTION', traceback.format_exc()
    if proc is not None:
        try:
            members = session_members(proc.pid)
            if members or proc.poll() is None:
                # Own-session settlement is not artifact cleanup. No other
                # session is signalled and no generated file is removed.
                for member in members:
                    try:
                        if member in session_members(proc.pid):
                            os.kill(member['pid'], signal.SIGKILL)
                            interventions.append(member)
                    except ProcessLookupError:
                        pass
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                native_exit = proc.wait(timeout=10)
                if error is None:
                    error = 'Owned session remained after native wait; success prohibited.'
            native_exit = proc.wait(timeout=10)
            remaining = session_members(proc.pid)
            settled = not remaining
            row['remaining_session_members'] = remaining
        except BaseException:
            settled = False
            error = (error or '') + traceback.format_exc()
    if proc is None:
        reason = 'NO_NATIVE_HANDLE_UNKNOWN_LAUNCH'
    row.update(native_handle_received=proc is not None,
               launch_outcome=('KNOWN_NATIVE_HANDLE' if proc is not None else
                               'UNKNOWN_NO_NATIVE_HANDLE'),
               native_exit_code=native_exit, wrapper_reason=reason, error=error,
               ended_epoch=time.time(), session_members_at_settlement=members,
               owned_session_interventions=interventions, streams_settled=settled)
    if not settled:
        write_new(work / 'UNCLOSED.json', row)
        raise RuntimeError('UNCLOSED_NATIVE_STREAMS: no final hashes or seal')
    row['streams'] = {name: pin(work / name) for name in ('stdout.raw', 'stderr.raw')
                      if (work / name).is_file()}
    if 'direct' in locals():
        after = {p: entry(p) for p in direct}
        write_new(work / 'INPUTS_AFTER.json', after)
        row['direct_inputs_equal'] = direct == after
    row['successful'] = (error is None and native_exit in expected and
                         row.get('direct_inputs_equal') is True)
    write_new(work / 'RECEIPT.json', row)
    return row, ((work / 'stdout.raw').read_bytes() if (work / 'stdout.raw').exists() else b'')


def incomplete_native(root):
    """An interrupted inner recorder cannot be mistaken for a closed child."""
    return [str(p.parent) for p in sorted(root.rglob('ATTEMPT.json'))
            if not (p.parent / 'RECEIPT.json').is_file()]


def seal(root):
    require(not list(root.rglob('UNCLOSED.json')), 'Unsettled subtree prevents seal')
    require(not incomplete_native(root), 'Incomplete native attempts prevent seal')
    files = sorted(p for p in root.rglob('*') if p.is_file())
    require(not any(p.is_symlink() for p in root.rglob('*')), 'Symlink in output package')
    require(not (root / 'SHA256SUMS').exists(), 'Never reseal an existing attempt')
    write_new(root / 'SHA256SUMS', ''.join(pin(p)['sha256'] + '  ' +
              p.relative_to(root).as_posix() + '\n' for p in files).encode())
    return {'payloads': len(files), 'manifest': pin(root / 'SHA256SUMS')}
