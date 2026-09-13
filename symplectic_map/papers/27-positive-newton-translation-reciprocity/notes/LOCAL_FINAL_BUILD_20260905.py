#!/usr/bin/env python3
"""Paper27: bounded local build, immutable fresh evidence, no retry/recovery.

Only --build writes. --preflight and --self-test never touch a build path.
This replaces the orchestration, not the scientific or PDF acceptance contract.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import stat
import subprocess
import sys
import time

PROJECT = Path('/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity')
NOTES = PROJECT / 'notes'
EVIDENCE = PROJECT / 'build/final-20260905-evidence'
ROOTS = (PROJECT / 'build/final-20260905-r0', PROJECT / 'build/final-20260905-r1')
SOURCES = {
    'main.tex': '9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8',
    'math_commands.tex': '34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957',
    'references.bib': 'a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5',
}
TOOLS = {
    '/usr/bin/pdftex': '01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9',
    '/usr/bin/bibtex.original': 'c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f',
    '/usr/bin/pdfinfo': '8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e',
    '/usr/bin/pdftotext': '7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d',
    '/usr/bin/pdffonts': '257a74fde0c3c36040504ff9068ee4b896c1cc2f19a9fae5a5b3dda55637ba5e',
    '/root/miniconda3/bin/python3.12': '9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101',
}
LINKS = {
    '/usr/bin/pdflatex': 'pdftex',
    '/usr/bin/bibtex': '/etc/alternatives/bibtex',
    '/etc/alternatives/bibtex': '/usr/bin/bibtex.original',
    '/root/miniconda3/bin/python3': 'python3.12',
    '/usr/share/texmf/web2c/texmf.cnf': '../../texlive/texmf-dist/web2c/texmf.cnf',
    '/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map': 'pdftex_dl14.map',
}
CACHES = ('texmf-var', 'texmf-config', 'texmf-home', 'xdg-cache', 'tmp')
TEX = ('/usr/bin/pdflatex', '-interaction=nonstopmode', '-halt-on-error',
       '-file-line-error', '-no-shell-escape', '-recorder', 'main.tex')
COMMANDS = (('R020', TEX), ('R030', ('/usr/bin/bibtex', 'main')),
            ('R040', TEX), ('R050', TEX))
SNAPSHOTS = (
    (('R021', 'main.log'), ('R022', 'main.aux'), ('R023', 'main.fls')),
    (('R031', 'main.bbl'), ('R032', 'main.blg')),
    (('R041', 'main.log'), ('R042', 'main.aux'), ('R043', 'main.fls')),
    (('R051', 'main.log'), ('R052', 'main.aux'), ('R053', 'main.fls')),
)
MANIFEST_IDS = ('R009', 'R024', 'R033', 'R044', 'R054')
KEYS = frozenset('abboud_xie_2026 bedford_kim_2008 berger_turaev_2025 '
    'bianchi_dinh_rakhimov_2024 blanc_van_santen_2022 cheng_wang_yu_1994 '
    'dang_favre_2021 deserti_2018 el_hilany_2024 favre_wulcan_2012 '
    'fordy_hone_2011 gomez_meiss_2004 grigoriev_containment hasselblatt_propp_2007 '
    'janeczko_jelonek_2008 koch_lomeli_2014 nisse_2026 shafikov_wolf_2003 '
    'shao_sun_2025 takenawa_2026'.split())
TITLE = 'Diagonal-Translation Rigidity and Literal Phase Reciprocity in Positive Newton-Fan Hamiltonian Shears'
HEADINGS = ('1 Introduction', '2 Collision positioning', '3 Typed cells and main theorem',
    '4 Positive-face survival', '5 Translation, envelopes, equality, and tail',
    '6 Full spans and literal reciprocity', '7 One-step radius and complete fixture',
    '8 Boundaries and conclusion')
CLAUSES = ('Typed survival', 'Translation and transience', 'Equality and tail',
           'Literal word reciprocity', 'One-step radius')
BOUNDARIES = ('Characteristic zero', 'Positive coordinates',
    'Coordinate lower bound and strictness', 'Complete row family', 'First carry',
    'Literal reflected label', 'Positive-support cancellation control')
CONCLUSION = ('Larger typed fan systems and perturbations of the row data would require new '
    'hypotheses and proofs; they are directions beyond the present result.')
PROVENANCE = ('BATCH07', 'B07-', 'SOURCE_LOCK', 'PUBLICATION_LOCK', 'reviewer_role',
    'candidate_id', '/root/', '/home/', 'autodl-tmp', 'symplectic_map',
    'localhost', '127.0.0.1', '::1')
ADMIN = {'LANG': 'C', 'LC_ALL': 'C', 'PATH': '/usr/bin:/bin', 'TZ': 'UTC'}
MAX_BYTES = 64 * 1024 * 1024
PDF_RUNTIME_FILES = ('fitz/__init__.py', 'fitz/table.py', 'fitz/utils.py',
    'pymupdf/__init__.py', 'pymupdf/__main__.py', 'pymupdf/_apply_pages.py',
    'pymupdf/_build.py', 'pymupdf/_extra.so', 'pymupdf/_mupdf.so',
    'pymupdf/_wxcolors.py', 'pymupdf/extra.py', 'pymupdf/libmupdf.so.27.2',
    'pymupdf/libmupdfcpp.so.27.2', 'pymupdf/mupdf.py', 'pymupdf/pymupdf.py',
    'pymupdf/table.py', 'pymupdf/utils.py')
PDF_RUNTIME_SHA = '66cb425ff3a012c077f5ee1f8b8e7019f8f4d8c471635a2cfc98acdbb3ee6a2b'


class Stop(Exception):
    pass


class ChildUnreaped(Stop):
    pass


def require(condition, tag):
    if not condition:
        raise Stop(tag)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=True, sort_keys=True, indent=2) + '\n').encode()


def parent_fd(path):
    """Open explicit absolute ancestors without following directory symlinks."""
    path = Path(path)
    require(path.is_absolute() and '..' not in path.parts, 'PATH')
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC)
    try:
        for part in path.parts[1:-1]:
            next_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=fd)
            os.close(fd)
            fd = next_fd
        return fd
    except BaseException:
        os.close(fd)
        raise


def identity(st):
    return (st.st_dev, st.st_ino, st.st_mode, st.st_nlink, st.st_size, st.st_mtime_ns, st.st_ctime_ns)


def read_file(path, mode=None, digest=None):
    fd = parent_fd(path)
    child = None
    try:
        child = os.open(Path(path).name, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=fd)
        before = os.fstat(child)
        require(stat.S_ISREG(before.st_mode) and before.st_nlink == 1, 'REGULAR:' + str(path))
        require(mode is None or stat.S_IMODE(before.st_mode) == mode, 'MODE:' + str(path))
        require(before.st_size <= MAX_BYTES, 'SIZE:' + str(path))
        chunks = []
        while True:
            chunk = os.read(child, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
            require(sum(map(len, chunks)) <= MAX_BYTES, 'GROWTH:' + str(path))
        data = b''.join(chunks)
        require(len(data) == before.st_size, 'SHORT_READ:' + str(path))
        require(identity(before) == identity(os.fstat(child)), 'READ_DRIFT:' + str(path))
        require(identity(before) == identity(os.stat(Path(path).name, dir_fd=fd, follow_symlinks=False)), 'PATH_DRIFT:' + str(path))
        require(digest is None or sha(data) == digest, 'HASH:' + str(path))
        return data
    finally:
        if child is not None:
            os.close(child)
        os.close(fd)


def write_new(path, data, mode=0o600):
    fd = parent_fd(path)
    child = None
    try:
        child = os.open(Path(path).name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, mode, dir_fd=fd)
        os.fchmod(child, mode)
        view = memoryview(data)
        while view:
            count = os.write(child, view)
            require(count > 0, 'SHORT_WRITE')
            view = view[count:]
        os.fsync(child)
        os.fsync(fd)
    finally:
        if child is not None:
            os.close(child)
        os.close(fd)
    require(read_file(path, mode) == data, 'WRITE_VERIFY:' + str(path))


def mkdir_new(path):
    fd = parent_fd(path)
    try:
        # mkdir itself is the exclusive freshness test; never inspect old namespaces.
        os.mkdir(Path(path).name, 0o700, dir_fd=fd)
        st = os.stat(Path(path).name, dir_fd=fd, follow_symlinks=False)
        require(stat.S_ISDIR(st.st_mode) and stat.S_IMODE(st.st_mode) == 0o700, 'NEW_DIR')
        os.fsync(fd)
    finally:
        os.close(fd)


def check_link(path, raw):
    fd = parent_fd(path)
    try:
        st = os.stat(Path(path).name, dir_fd=fd, follow_symlinks=False)
        require(stat.S_ISLNK(st.st_mode) and st.st_nlink == 1 and st.st_size == len(raw), 'LINK_META:' + path)
        require(os.readlink(Path(path).name, dir_fd=fd) == raw, 'LINK_TARGET:' + path)
    finally:
        os.close(fd)


def dependency_rows():
    data = read_file(NOTES / 'DEPENDENCY_LOCK_SUCCESSOR.md', 0o644,
                    '66c96cc6b40658370cc129e3bf828bcd08a7e69f7f2462ebea084cc77ce6ed17')
    stream = data.split(b'```text\n', 1)[1].split(b'```', 1)[0]
    require(sha(stream) == '2855b5fe4a859552fc581eb3c06b11c68008b8eb67351d37f2a44c57a91adf87', 'LOCK_STREAM')
    rows = [line.decode('utf-8').split('\t') for line in stream.splitlines()]
    require(len(rows) == 87 and all(len(row) == 7 for row in rows), 'LOCK_ROWS')
    require([row[0] for row in rows] == sorted(set(row[0] for row in rows)), 'LOCK_ORDER')
    return rows


def source_path(name):
    return PROJECT / ('paper-layout-20260905' if name == 'main.tex' else 'paper') / name


def bindings(root=None):
    read_file(PROJECT / 'paper/main.tex', 0o644,
              'd60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e')
    for path, raw in LINKS.items():
        check_link(path, raw)
    for path, digest in TOOLS.items():
        read_file(path, 0o755, digest)
    for name, digest in SOURCES.items():
        data = read_file(source_path(name), 0o644, digest)
        require(not data.startswith(b'\xef\xbb\xbf') and b'\r' not in data and b'\0' not in data
                and data.endswith(b'\n') and not data.endswith(b'\n\n'), 'SOURCE_ENCODING:' + name)
        data.decode('utf-8', 'strict')
        if root is not None:
            require(read_file(root / name, 0o644, digest) == data, 'SOURCE_COPY:' + name)
    rows = dependency_rows()
    finals = {}
    for logical, chain, final, size, mode, links, digest in rows:
        require(mode == '0644' and links == '1', 'LOCK_FIELDS')
        require(chain == logical if logical == final else chain == logical + '=>' + final, 'LOCK_CHAIN')
        if logical != final:
            require(logical in LINKS, 'LOCK_UNDECLARED_LINK')
        if final not in finals:
            data = read_file(final, 0o644, digest)
            require(len(data) == int(size), 'DEP_SIZE:' + final)
            finals[final] = digest
        require(finals[final] == digest, 'DEP_SHARED')
    require(len(finals) == 86, 'DEP_FINALS')
    return {'sources': SOURCES, 'tools': TOOLS, 'logical_dependencies': 87,
            'final_dependencies': 86, 'dependency_frame_sha256': sha(encoded(rows))}


def publication_env(root):
    return {'FORCE_SOURCE_DATE': '1', 'LANG': 'C', 'LC_ALL': 'C', 'PATH': '/usr/bin:/bin',
        'SOURCE_DATE_EPOCH': '0', 'TEXMFCONFIG': str(root / 'texmf-config'),
        'TEXMFHOME': str(root / 'texmf-home'), 'TEXMFVAR': str(root / 'texmf-var'),
        'TMPDIR': str(root / 'tmp'), 'TZ': 'UTC', 'XDG_CACHE_HOME': str(root / 'xdg-cache')}


def pdf_runtime_binding():
    base = Path('/root/miniconda3/lib/python3.12/site-packages')
    frame = b''
    for name in PDF_RUNTIME_FILES:
        path = base / name
        frame += (sha(read_file(path)) + '  ' + str(path) + '\n').encode()
    require(sha(frame) == PDF_RUNTIME_SHA, 'PDF_RUNTIME_HASH')
    return PDF_RUNTIME_SHA


def child_limits():
    os.umask(0o077)
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    resource.setrlimit(resource.RLIMIT_FSIZE, (MAX_BYTES, MAX_BYTES))
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    resource.setrlimit(resource.RLIMIT_NOFILE, (4096 if hard == resource.RLIM_INFINITY else min(4096, hard), hard))


def run_command(stage, ident, argv, cwd, env):
    write_new(stage / (ident + '.intent.json'), encoded({'argv': argv, 'cwd': str(cwd),
        'environment': list(env.items()), 'observation_start_ns': time.time_ns()}))
    start = time.monotonic_ns()
    proc = subprocess.Popen(argv, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True,
        start_new_session=True, preexec_fn=child_limits)
    error = None
    out = err = b''
    streams_complete = False
    cleanup_errors = []
    try:
        out, err = proc.communicate(timeout=190)
        streams_complete = True
    except BaseException as exc:
        error = exc
        if isinstance(exc, subprocess.TimeoutExpired):
            out, err = exc.output or b'', exc.stderr or b''
    finally:
        if not streams_complete:
            # A second Ctrl-C must not interrupt bounded cleanup of our own child.
            previous_sigint = signal.signal(signal.SIGINT, signal.SIG_IGN)
            try:
                for sig in (signal.SIGTERM, signal.SIGKILL):
                    try:
                        os.killpg(proc.pid, sig)
                    except ProcessLookupError:
                        pass  # Already exited: communicate still drains/reaps.
                    except OSError as exc:
                        cleanup_errors.append(type(exc).__name__ + ':' + str(exc))
                    try:
                        out, err = proc.communicate(timeout=3)
                        streams_complete = True
                        break
                    except subprocess.TimeoutExpired as exc:
                        out, err = exc.output or out, exc.stderr or err
                    except OSError as exc:
                        cleanup_errors.append(type(exc).__name__ + ':' + str(exc))
                if proc.returncode is None:
                    try:
                        proc.wait(timeout=3)
                    except (subprocess.TimeoutExpired, OSError) as exc:
                        cleanup_errors.append(type(exc).__name__ + ':' + str(exc))
            finally:
                signal.signal(signal.SIGINT, previous_sigint)
        for pipe in (proc.stdout, proc.stderr):
            if pipe is not None:
                pipe.close()
    write_new(stage / (ident + '.stdout'), out)
    write_new(stage / (ident + '.stderr'), err)
    write_new(stage / (ident + '.status'), (str(proc.returncode) if proc.returncode is not None else 'UNKNOWN').encode() + b'\n')
    write_new(stage / (ident + '.receipt.json'), encoded({'returncode': proc.returncode,
        'pid': proc.pid, 'timed_out': isinstance(error, subprocess.TimeoutExpired),
        'exception': type(error).__name__ if error else None,
        'streams_complete': streams_complete, 'cleanup_errors': cleanup_errors,
        'elapsed_ns': time.monotonic_ns() - start,
        'stdout_sha256': sha(out), 'stderr_sha256': sha(err)}))
    if proc.returncode is None:
        raise ChildUnreaped('HOLD_NO_RESTART pid=' + str(proc.pid) + ' command=' + ident)
    if error is not None:
        raise error
    require(streams_complete and proc.returncode == 0, 'COMMAND:' + ident)
    require(not err, 'COMMAND_STDERR:' + ident)
    return out


def root_manifest(root, phase):
    files = set(SOURCES)
    if phase >= 1:
        files.update(('main.aux', 'main.fls', 'main.log', 'main.pdf'))
    if phase >= 2:
        files.update(('main.bbl', 'main.blg'))
    require(set(os.listdir(root)) == files | set(CACHES), 'ROOT_UNIVERSE')
    result = []
    for name in sorted(files | set(CACHES) | {'.'}):
        path = root if name == '.' else root / name
        st = os.stat(path, follow_symlinks=False)
        if name in files:
            data = read_file(path, 0o644 if name in SOURCES else 0o600)
            result.append([name, 'file', len(data), data.count(b'\n'),
                           format(stat.S_IMODE(st.st_mode), '04o'), st.st_nlink, sha(data)])
        else:
            require(stat.S_ISDIR(st.st_mode) and stat.S_IMODE(st.st_mode) == 0o700, 'ROOT_DIR')
            if name != '.':
                require(not os.listdir(path), 'CACHE_NOT_EMPTY:' + name)
            result.append([name, 'dir', st.st_size, None, '0700', st.st_nlink, None])
    return result


def recorder_check(data, root, external, phase):
    lines = data.decode('utf-8', 'strict').splitlines()
    require(lines and lines[0] == 'PWD ' + str(root), 'FLS_PWD')
    inputs, outputs = set(), set()
    for line in lines[1:]:
        kind, sep, value = line.partition(' ')
        require(sep and kind in ('INPUT', 'OUTPUT') and value, 'FLS_ROW')
        path = Path(value)
        if path.is_absolute() and str(path) in external:
            require(kind == 'INPUT', 'FLS_EXTERNAL_OUTPUT')
            inputs.add(str(path))
            continue
        name = value[len(str(root)) + 1:] if value.startswith(str(root) + '/') else value
        if name.startswith('./'):
            name = name[2:]  # Allowlist spelling only; raw recorder bytes are never changed.
        allowed = {'main.tex', 'math_commands.tex', 'main.aux'} | ({'main.bbl'} if phase >= 3 else set())
        require(name in (allowed if kind == 'INPUT' else {'main.aux', 'main.log', 'main.fls', 'main.pdf'}), 'FLS_LOCAL:' + value)
        (inputs if kind == 'INPUT' else outputs).add(name)
    require({'main.tex', 'math_commands.tex'} <= inputs, 'FLS_SOURCE_MISSING')
    require({'main.aux', 'main.log', 'main.pdf'} <= outputs, 'FLS_OUTPUT_MISSING')
    return {'inputs': sorted(inputs), 'outputs': sorted(outputs)}


def strict_text(data):
    require(b'\r' not in data and b'\0' not in data, 'TEXT_ENCODING')
    return data.decode('utf-8', 'strict')


def collapse(text):
    return re.sub(r'[ \t\r\n\f\v]+', ' ', text).strip()


def log_check(data, pdf_size):
    text = strict_text(data)
    sentinels = re.findall(r'^BATCH07_REFERENCE_START_PAGE=([1-9][0-9]*)$', text, re.M)
    require(len(sentinels) == 1, 'SENTINEL')
    reference_page = int(sentinels[0])
    require(24 <= reference_page - 1 <= 28, 'PROOF_PAGES:' + str(reference_page - 1))
    outputs = re.findall(r'^Output written on main\.pdf \(([1-9][0-9]*) pages?, ([1-9][0-9]*) bytes\)\.$', text, re.M)
    require(len(outputs) == 1 and int(outputs[0][1]) == pdf_size, 'PDF_LOG_SIZE')
    require(int(outputs[0][0]) >= reference_page, 'PDF_LOG_PAGES')
    bad = re.compile(r'^!|error|undefined|multiply defined|missing character|emergency stop|fatal|overfull|rerun|label\(s\) may have changed|destination with the same identifier|token not allowed in a pdf string|font shape.*substitut|font.*fallback', re.I)
    for number, line in enumerate(text.splitlines(), 1):
        if line in ('file:line:error style messages enabled.', ' file:line:error style messages enabled.'):
            continue  # Exact normal header of the required -file-line-error mode.
        require(not bad.search(line), 'FINAL_LOG:' + str(number) + ':' + line)
    require('restricted \\write18 enabled' not in text and '\\write18 enabled' not in text, 'SHELL_ESCAPE')
    warnings = [{'line': i, 'text': line} for i, line in enumerate(text.splitlines(), 1)
                if re.search('warning|underfull', line, re.I)]
    return {'reference_page': reference_page, 'proof_pages': reference_page - 1,
            'total_pages': int(outputs[0][0]), 'warnings': warnings}


def bib_log_check(blg):
    lines = blg.splitlines()
    # This exact zero-count builtin statistic is not a warning diagnostic.
    headers = [i for i, line in enumerate(lines)
               if re.fullmatch(r'and the built_in function-call counts, [0-9]+ in all, are:', line)]
    require(len(headers) == 1 and lines.count('warning$ -- 0') == 1, 'BIB_STATISTICS')
    counter = lines.index('warning$ -- 0')
    require(headers[0] < counter, 'BIB_COUNTER_POSITION')
    require(all(re.fullmatch(r'\S+ -- [0-9]+', line)
                for line in lines[headers[0] + 1:]), 'BIB_COUNTER_TRAILER')
    for line in lines:
        if line == 'warning$ -- 0':
            continue
        require(not re.search('warning|error|undefined', line, re.I), 'BIB_LOG')


BOUNDARY_WRAPS = {
    'Positive coordinates': 'Positive coor- dinates',
    'Literal reflected label': 'Literal re- flected label',
    'Positive-support cancellation control': 'Positive- support can- cellation control',
}


def boundary_text_check(data, counts):
    # A separate content-order extraction keeps table cells together.
    # Only these exact, independently inspected line-wrap spellings are admitted.
    text = strict_text(data)
    require(not any(token in text for token in ('\ufffd', '??', '[?]', '[VERIFY]')), 'RAW_TEXT_MARKER')
    pages = text.split('\f')
    if pages[-1] == '':
        pages.pop()
    require(len(pages) == counts['total_pages'], 'RAW_PAGE_COUNT')
    ref = counts['reference_page']
    reference_pages = [i + 1 for i, page in enumerate(pages)
                       if page.strip().splitlines() and page.strip().splitlines()[0].strip() == 'References']
    require(reference_pages == [ref], 'RAW_REFERENCE_PAGE')
    pre = collapse('\n'.join(pages[:ref - 1]))
    require(pre.count(HEADINGS[-1]) == 1, 'RAW_BOUNDARY_SECTION')
    section = pre.split(HEADINGS[-1], 1)[1]
    suffix = collapse('\n'.join(pages[ref - 1:]))
    cursor = 0
    found = []
    for label in BOUNDARIES:
        variants = (label,) + ((BOUNDARY_WRAPS[label],) if label in BOUNDARY_WRAPS else ())
        matches = [(m.start(), variant) for variant in variants
                   for m in re.finditer(re.escape(variant), section)]
        require(len(matches) == 1 and matches[0][0] >= cursor, 'RAW_BOUNDARY:' + label)
        pos, spelling = matches[0]
        cursor = pos + len(spelling)
        require(not any(variant in suffix for variant in variants), 'RAW_BOUNDARY_AFTER_REFERENCES:' + label)
        found.append({'label': label, 'observed_spelling': spelling})
    return {'raw_text_sha256': sha(data), 'boundary_labels': found}


def citation_check(root):
    source = strict_text(read_file(root / 'main.tex'))
    bib = strict_text(read_file(root / 'references.bib'))
    aux = strict_text(read_file(root / 'main.aux'))
    bbl = strict_text(read_file(root / 'main.bbl'))
    blg = strict_text(read_file(root / 'main.blg'))
    source_keys = {key.strip() for group in re.findall(r'\\cite\{([^}]+)\}', source) for key in group.split(',')}
    aux_keys = {key.strip() for group in re.findall(r'\\citation\{([^}]+)\}', aux) for key in group.split(',')}
    bib_keys = re.findall(r'(?m)^@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,', bib)
    bbl_keys = re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', bbl)
    require(source_keys == aux_keys == set(bib_keys) == set(bbl_keys) == KEYS, 'CITATION_SET')
    require(len(bib_keys) == len(bbl_keys) == 20, 'CITATION_DUPLICATE')
    require(blg.splitlines().count('The style file: plain.bst') == 1, 'BST')
    require(blg.splitlines().count('Database file #1: references.bib') == 1, 'BIB_DATABASE')
    require(len(re.findall(r'^Database file', blg, re.M)) == 1, 'BIB_DATABASE_EXTRA')
    bib_log_check(blg)


def text_check(data, counts):
    text = strict_text(data)
    require('\ufffd' not in text and '??' not in text and '[?]' not in text and '[VERIFY]' not in text, 'PDF_TEXT_MARKER')
    pages = text.split('\f')
    if pages[-1] == '':
        pages.pop()
    require(len(pages) == counts['total_pages'], 'TEXT_PAGE_COUNT')
    reference_pages = [i + 1 for i, page in enumerate(pages) if page.strip().splitlines() and page.strip().splitlines()[0].strip() == 'References']
    require(reference_pages == [counts['reference_page']], 'TEXT_REFERENCE_PAGE')
    first = collapse(pages[0])
    require(all(part in first for part in (TITLE, 'Anonymous', 'Abstract')), 'TITLE_AUTHOR_ABSTRACT')
    pre = collapse('\n'.join(pages[:counts['reference_page'] - 1]))
    cursor = 0
    for heading in HEADINGS:
        pos = pre.find(heading, cursor)
        require(pos >= 0, 'HEADING:' + heading)
        cursor = pos + len(heading)
    for token in CLAUSES + ('P1', 'P2', 'P3', 'Q1', 'Q2', 'Q3', CONCLUSION):
        require(token in pre, 'CONTENT:' + token)
    require(all(len(page.strip()) > 80 for page in pages[:counts['reference_page'] - 1]), 'BLANK_PROOF_PAGE')
    suffix = '\n'.join(pages[counts['reference_page'] - 1:])
    for token in HEADINGS + CLAUSES + BOUNDARIES + (CONCLUSION,):
        require(token not in collapse(suffix), 'CONTENT_AFTER_REFERENCES:' + token)
    labels = re.findall(r'^[ \t]*\[([0-9]+)\][ \t]+', suffix, re.M)
    require(labels == [str(i) for i in range(1, 21)], 'VISIBLE_REFERENCES')
    for token in PROVENANCE:
        require(token not in text, 'PROVENANCE:' + token)
    require(not re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text), 'EMAIL')
    return sha(data)


def pdf_check(data, info_data, fonts_data):
    # Read-only semantic parser: no repair or write-back is accepted.
    pdf_runtime_binding()
    import fitz
    require(fitz.version[0] == '1.27.2.3', 'PDF_PARSER_VERSION')
    fitz.TOOLS.mupdf_warnings(reset=True)
    require(data.startswith(b'%PDF-1.5') and data.rstrip().endswith(b'%%EOF')
            and data.count(b'%%EOF') == 1, 'PDF_FRAMING')
    info = {}
    for line in strict_text(info_data).splitlines():
        key, sep, value = line.partition(':')
        require(sep and key not in info, 'PDFINFO_FIELDS')
        info[key] = value.strip()
    require(info.get('PDF version') == '1.5' and info.get('Creator') == 'TeX'
            and info.get('Producer') == 'pdfTeX-1.40.22', 'PDFINFO_TOOLING')
    for key in ('Custom Metadata', 'Metadata Stream', 'UserProperties', 'Suspects', 'JavaScript', 'Encrypted'):
        require(info.get(key) == 'no', 'PDFINFO_FLAG:' + key)
    require(info.get('Form') == 'none', 'PDFINFO_FORM')
    require(info.get('Author', '') in ('', 'Anonymous'), 'PDFINFO_AUTHOR')
    require(info.get('Title', '') in ('', TITLE), 'PDFINFO_TITLE')
    fonts_text = strict_text(fonts_data)
    font_rows = fonts_text.splitlines()[2:]
    require(font_rows, 'NO_FONTS')
    for row in font_rows:
        cols = row.split()
        require(len(cols) >= 8 and cols[-5] == 'yes' and 'Type 3' not in row, 'FONT_EMBEDDING')
    with fitz.open(stream=data, filetype='pdf') as doc:
        require(doc.is_pdf and not doc.is_repaired and not doc.is_encrypted
                and not doc.needs_pass and not doc.is_form_pdf, 'PDF_STRUCTURE')
        require(doc.page_count == int(info['Pages']) and int(info['File size'].split()[0]) == len(data), 'PDFINFO_SIZE_PAGES')
        meta = doc.metadata
        for key in ('creationDate', 'modDate'):
            require(meta.get(key) in ('D:19700101000000Z', "D:19700101000000+00'00'"), 'PDF_EPOCH:' + key)
        require(not doc.get_xml_metadata() and doc.embfile_count() == 0, 'PDF_ATTACHMENTS')
        require(1 < doc.xref_length() <= 10000, 'PDF_XREF_BOUND')
        objects = {xref: doc.xref_object(xref) for xref in range(1, doc.xref_length())}
        font_streams = set()
        forbidden = r'/(?:JavaScript|JS|Launch|EmbeddedFile|Filespec|RichMedia|SubmitForm|ImportData|Encrypt)\b|/Subtype\s*/Type3\b'
        for xref, obj in objects.items():
            require(not re.search(forbidden, obj), 'PDF_FORBIDDEN_OBJECT:' + str(xref))
            for token in PROVENANCE:
                require(token not in obj, 'PDF_OBJECT_PROVENANCE:' + token)
            if re.search(r'/Type\s*/FontDescriptor\b', obj):
                refs = re.findall(r'/FontFile[23]?\s+(\d+)\s+0\s+R', obj)
                require(refs, 'FONT_DESCRIPTOR_UNEMBEDDED')
                for value in refs:
                    font_streams.add(int(value))
                    require(bool(doc.xref_stream(int(value))), 'EMPTY_FONT_PROGRAM')
        for xref in objects:
            if doc.xref_is_stream(xref) and xref not in font_streams:
                stream = doc.xref_stream(xref)
                require(len(stream) <= MAX_BYTES, 'PDF_STREAM_SIZE')
                for token in PROVENANCE:
                    require(token.encode() not in stream, 'PDF_STREAM_PROVENANCE:' + token)
        font_census = set()
        for page in doc:
            box = page.mediabox
            require(tuple(box) == (0.0, 0.0, 612.0, 792.0) and page.rotation == 0, 'PAGE_GEOMETRY')
            require(not list(page.widgets() or ()) and not list(page.annots() or ()), 'PAGE_ANNOTATIONS')
            for row in page.get_fonts(full=True):
                require(row[0] > 0 and row[2] != 'Type3', 'PAGE_FONT')
                basename, extension, kind, content = doc.extract_font(row[0])
                require(content and extension != 'n/a', 'PAGE_FONT_UNEMBEDDED')
                font_census.add((basename, extension, kind, sha(content)))
            for block in page.get_text('dict')['blocks']:
                if block.get('type') != 0:
                    continue
                for line in block['lines']:
                    for span in line['spans']:
                        x0, y0, x1, y1 = span['bbox']
                        require(x0 >= -0.5 and y0 >= -0.5 and x1 <= 612.5 and y1 <= 792.5, 'PAGE_CLIPPED_TEXT')
        require(not fitz.TOOLS.mupdf_warnings(reset=True), 'PDF_PARSER_WARNING')
        pdf_runtime_binding()
        return {'metadata': meta, 'font_census': sorted(font_census), 'pdfinfo': info,
                'pdffonts_sha256': sha(fonts_data), 'pdf_sha256': sha(data), 'pages': doc.page_count,
                'pdf_parser_runtime_sha256': PDF_RUNTIME_SHA}


def build_root(root, stage):
    mkdir_new(root)
    for name in CACHES:
        mkdir_new(root / name)
    for name, digest in SOURCES.items():
        write_new(root / name, read_file(source_path(name), 0o644, digest), 0o644)
    write_new(stage / 'setup.receipt.json', encoded({'root': str(root), 'sources': SOURCES, 'cache_dirs': CACHES}))
    manifests = [root_manifest(root, 0)]
    write_new(stage / 'R009.manifest.json', encoded(manifests[0]))
    external = {row[0] for row in dependency_rows()} | {row[2] for row in dependency_rows()}
    recorders = []
    for index, (ident, argv) in enumerate(COMMANDS):
        write_new(stage / (ident + '.preflight.json'), encoded(bindings(root)))
        root_manifest(root, index)
        run_command(stage, ident, argv, root, publication_env(root))
        write_new(stage / (ident + '.postflight.json'), encoded(bindings(root)))
        current = root_manifest(root, index + 1)
        if index == 1:
            require(read_file(root / 'main.fls') == recorders[0], 'BIBTEX_CHANGED_RECORDER')
        for snapshot_id, name in SNAPSHOTS[index]:
            data = read_file(root / name, 0o600)
            write_new(stage / (snapshot_id + '--' + name + '.snapshot'), data)
            write_new(stage / (snapshot_id + '.receipt.json'), encoded({'source': str(root / name),
                'bytes': len(data), 'lf': data.count(b'\n'), 'mode': '0600', 'nlink': 1, 'sha256': sha(data)}))
            if name == 'main.fls':
                recorder_check(data, root, external, index + 1)
                recorders.append(data)
        manifests.append(current)
        write_new(stage / (MANIFEST_IDS[index + 1] + '.manifest.json'), encoded(current))
    pdf = read_file(root / 'main.pdf', 0o600)
    counts = log_check(read_file(root / 'main.log', 0o600), len(pdf))
    citation_check(root)
    info = run_command(stage, 'PDFINFO', ('/usr/bin/pdfinfo', '-rawdates', str(root / 'main.pdf')), root, ADMIN)
    text = run_command(stage, 'PDFTEXT', ('/usr/bin/pdftotext', '-layout', '-enc', 'UTF-8', str(root / 'main.pdf'), '-'), root, ADMIN)
    fonts = run_command(stage, 'PDFFONTS', ('/usr/bin/pdffonts', str(root / 'main.pdf')), root, ADMIN)
    raw = run_command(stage, 'PDFRAW', ('/usr/bin/pdftotext', '-raw', '-enc', 'UTF-8', str(root / 'main.pdf'), '-'), root, ADMIN)
    result = pdf_check(pdf, info, fonts)
    result.update(counts)
    result['text_sha256'] = text_check(text, counts)
    result.update(boundary_text_check(raw, counts))
    require(result['pages'] == result['total_pages'], 'LOG_PDF_PAGE_MISMATCH')
    # Warning disposition is semantic: keep it pending for an independent reader.
    result['status'] = 'OUTPUT_CHECKS_PASS_WARNING_REVIEW_PENDING' if counts['warnings'] else 'OUTPUT_CHECKS_PASS'
    write_new(stage / 'acceptance.json', encoded(result))
    write_new(stage / 'terminal.bindings.json', encoded(bindings(root)))
    require(root_manifest(root, 4) == manifests[-1], 'INSPECTION_MUTATED_ROOT')
    return {'result': result, 'manifests': manifests, 'recorders': recorders}


def compare_roots(left, right):
    for name in tuple(SOURCES) + ('main.pdf', 'main.aux', 'main.bbl', 'main.blg', 'main.log'):
        require(read_file(ROOTS[0] / name) == read_file(ROOTS[1] / name), 'CROSS_RAW:' + name)
    norms = []
    for root, bundle in zip(ROOTS, (left, right)):
        norms.append([data.replace(str(root).encode(), b'<ROOT>') for data in bundle['recorders']])
    require(norms[0] == norms[1], 'CROSS_RECORDERS')
    require(left['result'] == right['result'], 'CROSS_ACCEPTANCE')
    for index in range(5):
        projections = []
        for bundle, normalized in zip((left, right), norms):
            projected = [list(row) for row in bundle['manifests'][index]]
            if index:
                rec_index = (0, 0, 1, 2)[index - 1]
                raw = bundle['recorders'][rec_index]
                rows = [row for row in projected if row[0] == 'main.fls']
                require(len(rows) == 1, 'MANIFEST_FLS_ROW')
                row = rows[0]
                require(row[1:] == ['file', len(raw), raw.count(b'\n'), '0600', 1, sha(raw)], 'MANIFEST_RECORDER_BINDING')
                row[-1] = sha(normalized[rec_index])
            projections.append(encoded(projected))
        require(projections[0] == projections[1], 'CROSS_MANIFEST:' + MANIFEST_IDS[index])
    return {'status': 'DETERMINISTIC_BUILD_CHECKS_PASS_PENDING_INDEPENDENT_REVIEW',
            'pdf_sha256': left['result']['pdf_sha256'], 'proof_pages': left['result']['proof_pages'],
            'total_pages': left['result']['total_pages'], 'warnings': left['result']['warnings'],
            'source_sha256': SOURCES, 'roots': list(map(str, ROOTS))}


def self_test():
    good_log = b'BATCH07_REFERENCE_START_PAGE=25\nOutput written on main.pdf (26 pages, 123 bytes).\n'
    require(log_check(good_log, 123)['proof_pages'] == 24, 'TEST_LOG')
    rejected = 0
    cases = [good_log.replace(b'=25', b'=24'), good_log.replace(b'=25', b'=30'),
             good_log + b'Overfull \\hbox (1pt too wide)\n', good_log + b'LaTeX Warning: undefined reference\n',
             good_log + b'BATCH07_REFERENCE_START_PAGE=25\n', good_log.replace(b'123 bytes', b'124 bytes'),
             good_log + b'LaTeX Warning: Label(s) may have changed. Rerun\n', good_log + b'\x00']
    for case in cases:
        try:
            log_check(case, 123)
        except Stop:
            rejected += 1
    require(rejected == len(cases), 'TEST_NEGATIVES')
    valid_fls = b'PWD /synthetic/r0\nINPUT main.tex\nINPUT math_commands.tex\nOUTPUT main.aux\nOUTPUT main.log\nOUTPUT main.pdf\n'
    recorder_check(valid_fls, Path('/synthetic/r0'), set(), 1)
    for suffix in (b'INPUT /undeclared/file\n', b'OUTPUT ../escape\n', b'OUTPUT main.toc\n'):
        try:
            recorder_check(valid_fls + suffix, Path('/synthetic/r0'), set(), 1)
        except Stop:
            rejected += 1
        else:
            raise Stop('TEST_RECORDER_NEGATIVE')
    print(json.dumps({'status': 'SELF_TEST_PASS', 'positive_cases': 2, 'negative_cases': rejected,
                      'scope': 'pure log/recorder predicates only; no build or PDF correctness claim'}))


def main():
    require(len(sys.argv) == 2 and sys.argv[1] in ('--preflight', '--self-test', '--build'), 'USAGE')
    os.umask(0o077)
    if sys.argv[1] == '--self-test':
        self_test()
        return
    initial = bindings()
    initial['pdf_parser_runtime_sha256'] = pdf_runtime_binding()
    if sys.argv[1] == '--preflight':
        print(encoded(initial).decode(), end='')
        return
    own = read_file(Path(__file__), 0o644)
    review = strict_text(read_file(NOTES / 'LOCAL_FINAL_BUILD_20260905_REVIEW.md', 0o644))
    require('Decision: PASS\n' in review and ('Reviewed SHA256: ' + sha(own) + '\n') in review, 'PREBUILD_REVIEW')
    # No build pathname is touched before this point. Root1 is not touched until root0 passes.
    mkdir_new(EVIDENCE)
    try:
        write_new(EVIDENCE / 'bootstrap.json', encoded({'status': 'CREATED', 'path': str(EVIDENCE),
            'source_authorization': '用户：确认继续就行', 'script_sha256': sha(own),
            'independent_review_sha256': sha(review.encode()), 'initial_bindings': initial}))
        write_new(EVIDENCE / 'LOCAL_FINAL_BUILD_20260905.py', own, 0o500)
        bundles = []
        for label, root in zip(('r0', 'r1'), ROOTS):
            stage = EVIDENCE / label
            mkdir_new(stage)
            print('START ' + label, flush=True)
            bundles.append(build_root(root, stage))
            print('OUTPUT_CHECKS_PASS ' + label, flush=True)
        report = compare_roots(*bundles)
        write_new(EVIDENCE / 'result.json', encoded(report))
        print(encoded(report).decode(), end='', flush=True)
    except BaseException as exc:
        # Never overwrite an earlier result, delete an artifact or retry a command.
        write_new(EVIDENCE / 'failure.json', encoded({'status': 'HOLD_UNREAPED_CHILD_NO_RESTART'
            if isinstance(exc, ChildUnreaped) else 'FAIL_PRESERVED_NO_RETRY',
            'exception': type(exc).__name__, 'detail': str(exc), 'time_ns': time.time_ns()}))
        raise


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('STOP ' + type(exc).__name__ + ': ' + str(exc), file=sys.stderr, flush=True)
        sys.exit(1)

