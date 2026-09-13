#!/usr/bin/env python3
"""One Paper28 scanner-only capture. No subprocess, network or compiler API.

--self-test reads only this administrative code/helper.
--capture REVIEW_SHA exclusively creates its single named evidence root.
No retries, root reuse, removals or edits of captured inputs are implemented.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
import sys
import tarfile

PROJECT = Path('/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy')
NOTES = PROJECT / 'notes'
OUTPUT = NOTES / 'dependency-capture-20260905'
PLAN = NOTES / 'DEPENDENCY_CAPTURE_PLAN_20260905.md'
HELPER = NOTES / 'CAPTURE_ELF_20260905.py'
REVIEW = NOTES / 'DEPENDENCY_CAPTURE_REVIEW_20260905.md'
TREES = {
    '/usr/share/texlive/texmf-dist': ('doc', 'source'),
    '/usr/share/texmf': ('doc', 'source'),
    '/var/lib/texmf': (),
    '/etc/texmf': (),
    '/usr/share/poppler': (),
    '/etc/fonts': (),
    '/usr/share/fontconfig': (),
    '/usr/share/fonts': (),
    '/var/cache/fontconfig': (),
    '/root/miniconda3/lib/python3.12': ('site-packages',),
    '/root/miniconda3/lib/python3.12/site-packages/pymupdf': (),
    '/root/miniconda3/lib/python3.12/site-packages/fitz': (),
}
LIBDIRS = ('/root/miniconda3/lib', '/usr/lib/x86_64-linux-gnu',
           '/lib/x86_64-linux-gnu', '/lib64', '/usr/lib64')
TOOLS = ('/usr/bin/pdflatex', '/usr/bin/bibtex', '/usr/bin/kpsewhich',
         '/usr/bin/pdfinfo', '/usr/bin/pdftotext', '/usr/bin/pdffonts',
         '/usr/bin/pdftoppm', '/root/miniconda3/bin/python3',
         '/root/miniconda3/bin/python3.12')
EXACT = frozenset(TOOLS + ('/usr/bin/pdftex', '/usr/bin/bibtex.original',
    '/etc/alternatives/bibtex', '/etc/ld.so.cache', '/usr/share/zoneinfo/UTC',
    '/usr/share/zoneinfo/Etc/UTC'))
SOURCES = {
    'main.tex': 'bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e',
    'math_commands.tex': '16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5',
    'references.bib': 'e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e',
}
MAX_FILE = 256 * 1024 * 1024
MAX_TOTAL = 2 * 1024 * 1024 * 1024
MAX_ENTRIES = 250000


class CaptureStop(Exception):
    pass


class OutsideEnvelope(CaptureStop):
    pass


def require(condition, message):
    if not condition:
        raise CaptureStop(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, indent=2) + '\n').encode()


def normalize(path):
    require(isinstance(path, str) and path.startswith('/'), 'absolute path required')
    require(not any(c in path for c in '\x00\r\n\t'), 'control character in path')
    return os.path.normpath(path)


def beneath(path, root):
    return path == root or path.startswith(root + '/')


def in_tree(path):
    for root, excluded in TREES.items():
        if beneath(path, root):
            relative = path[len(root):].lstrip('/')
            if not relative or relative.split('/')[0] not in excluded:
                return True
    return False


def library_name(name):
    return ('/' not in name and '$' not in name and
            name.startswith(('lib', 'ld-')) and '.so' in name)


def content_allowed(path):
    return (path in EXACT or in_tree(path) or
            any(os.path.dirname(path) == root for root in LIBDIRS)
            and library_name(os.path.basename(path)))


def metadata_allowed(path):
    if content_allowed(path) or path in LIBDIRS:
        return True
    return any(beneath(root, path) for root in (*TREES, *LIBDIRS, *EXACT))


def identity(st):
    return (st.st_dev, st.st_ino, st.st_mode, st.st_nlink, st.st_size,
            st.st_mtime_ns, st.st_ctime_ns)


def metadata(st):
    return {'mode': format(stat.S_IMODE(st.st_mode), '04o'), 'nlink': st.st_nlink,
            'size': st.st_size, 'device': st.st_dev, 'inode': st.st_ino,
            'mtime_ns': st.st_mtime_ns, 'ctime_ns': st.st_ctime_ns}


def parent_descriptor(path):
    path = Path(path)
    require(path.is_absolute() and '..' not in path.parts, 'canonical absolute read path required')
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC)
    try:
        for component in path.parts[1:-1]:
            next_fd = os.open(component, os.O_RDONLY | os.O_DIRECTORY |
                              os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=fd)
            os.close(fd)
            fd = next_fd
        return fd
    except BaseException:
        os.close(fd)
        raise


def safe_lstat(path):
    if str(path) == '/':
        return os.lstat('/')
    parent = parent_descriptor(path)
    try:
        return os.stat(Path(path).name, dir_fd=parent, follow_symlinks=False)
    finally:
        os.close(parent)


def safe_readlink(path, expected):
    parent = parent_descriptor(path)
    try:
        require(identity(os.stat(Path(path).name, dir_fd=parent, follow_symlinks=False)) == identity(expected),
                'pre-readlink drift: ' + str(path))
        target = os.readlink(Path(path).name, dir_fd=parent)
        require(identity(os.stat(Path(path).name, dir_fd=parent, follow_symlinks=False)) == identity(expected),
                'post-readlink drift: ' + str(path))
        return target
    finally:
        os.close(parent)


def safe_listdir(path, expected):
    parent, fd = parent_descriptor(path), None
    try:
        fd = os.open(Path(path).name, os.O_RDONLY | os.O_DIRECTORY |
                     os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent)
        require(identity(os.fstat(fd)) == identity(expected), 'pre-census drift: ' + str(path))
        result = sorted(os.listdir(fd))
        require(identity(os.fstat(fd)) == identity(expected), 'post-census drift: ' + str(path))
        return result
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def read_regular(path, maximum=MAX_FILE):
    parent = parent_descriptor(path)
    fd = None
    try:
        fd = os.open(Path(path).name, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent)
        before = os.fstat(fd)
        require(stat.S_ISREG(before.st_mode), 'not regular: ' + str(path))
        require(before.st_size <= maximum, 'file size bound: ' + str(path))
        chunks, length = [], 0
        while True:
            block = os.read(fd, 1024 * 1024)
            if not block:
                break
            length += len(block)
            require(length <= maximum, 'file growth bound: ' + str(path))
            chunks.append(block)
        require(length == before.st_size, 'short/drifting read: ' + str(path))
        require(identity(before) == identity(os.fstat(fd)), 'descriptor drift: ' + str(path))
        require(identity(before) == identity(os.stat(Path(path).name, dir_fd=parent, follow_symlinks=False)),
                'parent-relative path drift: ' + str(path))
        require(identity(before) == identity(safe_lstat(path)), 'path drift: ' + str(path))
        return b''.join(chunks), before
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def create_file(name):
    require('/' not in name and name not in ('.', '..'), 'output basename')
    parent = parent_descriptor(OUTPUT / name)
    try:
        fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL |
                     os.O_NOFOLLOW | os.O_CLOEXEC, 0o600, dir_fd=parent)
    finally:
        os.close(parent)
    os.fchmod(fd, 0o600)
    return os.fdopen(fd, 'wb')


def write_new(name, data):
    with create_file(name) as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def hash_output(name):
    digest, size = hashlib.sha256(), 0
    parent, fd = parent_descriptor(OUTPUT / name), None
    try:
        fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent)
        before = os.fstat(fd)
        require(stat.S_ISREG(before.st_mode), 'output must be regular')
        maximum = MAX_TOTAL + MAX_ENTRIES * 8192
        require(before.st_size <= maximum, 'output size bound')
        while True:
            block = os.read(fd, 1024 * 1024)
            if not block:
                break
            size += len(block)
            require(size <= maximum, 'output growth bound')
            digest.update(block)
        require(size == before.st_size and identity(os.fstat(fd)) == identity(before), 'output read drift')
        require(identity(os.stat(name, dir_fd=parent, follow_symlinks=False)) == identity(before), 'output path drift')
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)
    return {'bytes': size, 'sha256': digest.hexdigest()}


def source_bindings():
    result = {}
    for name, expected in SOURCES.items():
        data, st = read_regular(PROJECT / 'paper' / name)
        require(sha(data) == expected, 'source hash: ' + name)
        require(stat.S_IMODE(st.st_mode) == 0o644 and st.st_nlink == 1, 'source metadata: ' + name)
        result[name] = {'sha256': expected, 'bytes': len(data), 'lf': data.count(b'\n')}
    return result


def load_elf_helper(data):
    namespace = {'__name__': 'paper28_capture_elf'}
    exec(compile(data, str(HELPER), 'exec'), namespace)
    return namespace['elf_dependencies']


class Scanner:
    def __init__(self, archive, journal, elf_parser):
        self.archive, self.journal, self.elf_parser = archive, journal, elf_parser
        self.rows, self.observations = {}, {}
        self.pending_elf, self.edges, self.omissions = [], [], []
        self.total = 0

    def event(self, value):
        self.journal.write((json.dumps(value, sort_keys=True, ensure_ascii=True) + '\n').encode())
        if len(self.rows) % 256 == 0:
            self.journal.flush()
            os.fsync(self.journal.fileno())

    def omit(self, path, reason, **details):
        row = {'path': path, 'reason': reason, **details}
        if row not in self.omissions:
            self.omissions.append(row)
            self.event({'omission': row})

    def add(self, path, kind, st, data=None, target=None):
        if path in self.rows:
            require(self.observations[path] == identity(st), 'revisit drift: ' + path)
            return
        require(len(self.rows) < MAX_ENTRIES, 'entry count bound')
        row = {'path': path, 'kind': kind, **metadata(st)}
        info = tarfile.TarInfo(path.lstrip('/'))
        info.uid = info.gid = info.mtime = 0
        info.uname = info.gname = ''
        info.mode = stat.S_IMODE(st.st_mode)
        if kind == 'file':
            require(data is not None, 'missing captured bytes')
            require(self.total + len(data) <= MAX_TOTAL, 'total byte bound')
            self.total += len(data)
            row.update(sha256=sha(data), lf=data.count(b'\n'))
            info.size = len(data)
            self.archive.addfile(info, io.BytesIO(data))
            try:
                elf = self.elf_parser(data)
            except ValueError as exc:
                self.omit(path, 'unsupported_or_malformed_elf', detail=str(exc))
                elf = None
            if elf is not None:
                self.pending_elf.append((path, elf))
        elif kind == 'dir':
            info.type = tarfile.DIRTYPE
            self.archive.addfile(info)
        elif kind == 'symlink':
            row['target'] = target
            info.type, info.linkname = tarfile.SYMTYPE, target
            self.archive.addfile(info)
        else:
            raise CaptureStop('unknown entry kind')
        self.rows[path], self.observations[path] = row, identity(st)
        self.event({'entry': row})
        if len(self.rows) % 2000 == 0:
            print(json.dumps({'captured_entries': len(self.rows), 'input_bytes': self.total}), flush=True)

    def resolve(self, path):
        path, hops = normalize(path), 0
        require(content_allowed(path) or path in LIBDIRS, 'initial input outside envelope: ' + path)
        pending, current = path.lstrip('/').split('/'), '/'
        while pending:
            part = pending.pop(0)
            candidate = normalize(os.path.join(current, part))
            if not metadata_allowed(candidate):
                raise OutsideEnvelope('link traversal outside envelope: ' + candidate)
            st = safe_lstat(candidate)
            if stat.S_ISLNK(st.st_mode):
                target = safe_readlink(candidate, st)
                self.add(candidate, 'symlink', st, target=target)
                # Collapsing a/../ before following a possible symlink a would
                # change POSIX resolution. Only leading parent chains are safe
                # to normalize from the already canonical containing directory.
                concrete_component = target.startswith('/')
                for component in target.split('/'):
                    if component == '..' and concrete_component:
                        raise OutsideEnvelope('non-leading parent component in link target: ' + candidate)
                    if component not in ('', '.', '..'):
                        concrete_component = True
                hops += 1
                require(hops <= 32, 'symlink depth/cycle: ' + path)
                destination = normalize(target if target.startswith('/') else os.path.join(current, target))
                destination = normalize(os.path.join(destination, *pending))
                if not (content_allowed(destination) or destination in LIBDIRS):
                    raise OutsideEnvelope('link target outside envelope: ' + destination)
                pending, current = destination.lstrip('/').split('/'), '/'
            else:
                if pending:
                    require(stat.S_ISDIR(st.st_mode), 'non-directory ancestor: ' + candidate)
                current = candidate
        require(content_allowed(current) or current in LIBDIRS, 'resolved input outside envelope')
        return current, st

    def visit(self, path, essential=False):
        try:
            resolved, st = self.resolve(path)
        except (FileNotFoundError, NotADirectoryError, OutsideEnvelope) as exc:
            self.omit(path, type(exc).__name__, detail=str(exc))
            require(not essential, 'essential input unavailable: ' + path)
            return None
        if resolved in self.rows and self.rows[resolved]['kind'] != 'symlink':
            require(self.observations[resolved] == identity(st), 'revisit drift: ' + resolved)
            return resolved
        if stat.S_ISREG(st.st_mode):
            data, observed = read_regular(resolved)
            require(identity(st) == identity(observed), 'pre-open drift: ' + resolved)
            self.add(resolved, 'file', observed, data=data)
        elif stat.S_ISDIR(st.st_mode):
            # Library directories are search locations, never census roots.
            require(in_tree(resolved), 'directory census outside resource tree: ' + resolved)
            self.add(resolved, 'dir', st)
            before = safe_listdir(resolved, st)
            for child in before:
                child_path = normalize(resolved + '/' + child)
                if content_allowed(child_path):
                    self.visit(child_path)
                else:
                    self.omit(child_path, 'declared_top_level_exclusion')
            after = safe_listdir(resolved, st)
            require(before == after and identity(st) == identity(safe_lstat(resolved)),
                    'directory drift: ' + resolved)
            self.rows[resolved]['members'] = before
        else:
            self.omit(resolved, 'non_regular_resource', mode=oct(st.st_mode))
            require(not essential, 'essential input not regular/directory')
            return None
        return resolved

    def native_closure(self):
        index = 0
        while index < len(self.pending_elf):
            path, elf = self.pending_elf[index]
            index += 1
            interpreter = elf['interpreter']
            if interpreter:
                try:
                    admitted = content_allowed(normalize(interpreter))
                except CaptureStop:
                    admitted = False
                target = self.visit(interpreter) if admitted else None
                self.edges.append({'requester': path, 'kind': 'interpreter', 'name': interpreter,
                                   'candidates': [target] if target else []})
            directories = [os.path.dirname(path), *LIBDIRS]
            for raw in elf['rpath'] + elf['runpath']:
                expanded = re.sub(r'\$\{ORIGIN\}|\$ORIGIN(?![A-Za-z0-9_])',
                                  lambda match: os.path.dirname(path), raw)
                if not expanded.startswith('/') or '$' in expanded:
                    self.omit(path, 'unsupported_search_token', value=raw)
                    continue
                candidate = normalize(expanded)
                if candidate in LIBDIRS or in_tree(candidate):
                    directories.append(candidate)
                else:
                    self.omit(path, 'excluded_search_directory', value=raw)
            for needed in elf['needed']:
                found = []
                if library_name(needed):
                    for directory in sorted(set(directories)):
                        candidate = normalize(directory + '/' + needed)
                        if not content_allowed(candidate):
                            continue
                        # Missing candidate metadata is normal search evidence.
                        target = self.visit(candidate)
                        if target and target not in found:
                            found.append(target)
                self.edges.append({'requester': path, 'kind': 'needed', 'name': needed,
                                   'candidates': sorted(found)})
        return [edge for edge in self.edges if not edge['candidates']]

    def terminal_rebind(self):
        # No second content capture: metadata/member drift check only.
        for path, row in sorted(self.rows.items()):
            current = safe_lstat(path)
            require(identity(current) == self.observations[path], 'terminal metadata drift: ' + path)
            if row['kind'] == 'dir':
                require(safe_listdir(path, current) == row['members'], 'terminal membership drift: ' + path)
            elif row['kind'] == 'symlink':
                require(safe_readlink(path, current) == row['target'], 'terminal symlink drift: ' + path)


def capture(review_sha, helper_data):
    plan_data, _ = read_regular(PLAN)
    code_data, _ = read_regular(Path(__file__))
    review_data, _ = read_regular(REVIEW)
    intake_data, _ = read_regular(NOTES / 'RECOVERY_CONTEXT_20260905.md')
    require(sha(review_data) == review_sha, 'review hash mismatch')
    review_text = review_data.decode('utf-8')
    require('\nDecision: CAPTURE_PLAN_CODE_PASS\n' in review_text, 'review decision missing')
    for label, data in (('Plan', plan_data), ('Scanner', code_data), ('ELF helper', helper_data)):
        require(label + ' SHA256: ' + sha(data) in review_text, 'review binding: ' + label)
    elf_parser = load_elf_helper(helper_data)
    sources = source_bindings()
    # Exact administrative ancestor checks; no root census or prior-output probe.
    for parent in reversed(OUTPUT.parents):
        require(stat.S_ISDIR(safe_lstat(parent).st_mode), 'output ancestor must be a real directory')
    parent = parent_descriptor(OUTPUT)
    try:
        os.mkdir(OUTPUT.name, 0o700, dir_fd=parent)
    finally:
        os.close(parent)
    try:
        write_new('intent.json', encoded({'operation': 'one_time_read_only_resource_capture',
            'plan_sha256': sha(plan_data), 'scanner_sha256': sha(code_data),
            'helper_sha256': sha(helper_data), 'review_sha256': review_sha,
            'intake_sha256': sha(intake_data), 'sources': sources,
            'trees': TREES, 'library_search_directories': LIBDIRS, 'exact_inputs': sorted(EXACT),
            'limits': {'entries': MAX_ENTRIES, 'file_bytes': MAX_FILE, 'total_bytes': MAX_TOTAL},
            'controller': 'configured Python bootstrap trusted; no pre-import trace claimed'}))
        with create_file('events.jsonl') as journal, create_file('capsule.tar') as raw_archive:
            with tarfile.open(fileobj=raw_archive, mode='w|', format=tarfile.PAX_FORMAT) as archive:
                scanner = Scanner(archive, journal, elf_parser)
                for number, root in enumerate(TREES):
                    scanner.visit(root, essential=number < 4)
                for path in TOOLS:
                    scanner.visit(path, essential=True)
                for path in ('/etc/ld.so.cache', '/usr/share/zoneinfo/UTC'):
                    scanner.visit(path)
                unresolved = scanner.native_closure()
                scanner.terminal_rebind()
                require(source_bindings() == sources, 'terminal source drift')
                manifest = {'schema': 'paper28-read-only-capture-v1',
                    'entries': [scanner.rows[path] for path in sorted(scanner.rows)],
                    'static_native_edges': scanner.edges, 'unresolved_native_edges': unresolved,
                    'omissions': scanner.omissions, 'sources': sources,
                    'regular_input_bytes': scanner.total,
                    'completeness': 'recorded superset; independent capsule/profile review required'}
            raw_archive.flush()
            os.fsync(raw_archive.fileno())
            journal.flush()
            os.fsync(journal.fileno())
        write_new('manifest.json', encoded(manifest))
        outputs = {name: hash_output(name) for name in
                   ('intent.json', 'events.jsonl', 'capsule.tar', 'manifest.json')}
        outcome = {'decision': 'CAPTURE_RECORDED_REVIEW_REQUIRED', 'outputs': outputs,
            'entries': len(scanner.rows), 'regular_input_bytes': scanner.total,
            'unresolved_native_edges': len(unresolved), 'omissions': len(scanner.omissions),
            'compiler_invocations': 0, 'network_operations': 0, 'input_writes': 0,
            'limitations': ['Trusted controller bootstrap/host kernel; not OS-level attestation',
                'Static native superset does not choose a loader winner or prove arbitrary dlopen closure',
                'No build/PDF acceptance or permission to use unreviewed capsule']}
        write_new('outcome.json', encoded(outcome))
        directory_fd = os.open(OUTPUT, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        print(json.dumps(outcome, sort_keys=True), flush=True)
    except BaseException as exc:
        try:
            write_new('failure.json', encoded({'decision': 'CAPTURE_FAILED_PRESERVED_NO_RETRY',
                'exception': type(exc).__name__, 'detail': str(exc)}))
        except BaseException:
            pass
        raise


def self_test(elf_parser):
    assert in_tree('/usr/share/texlive/texmf-dist/tex/latex/base/article.cls')
    assert not in_tree('/usr/share/texlive/texmf-dist/doc/guide.pdf')
    assert not in_tree('/root/miniconda3/lib/python3.12/site-packages/unrelated/a.py')
    assert in_tree('/root/miniconda3/lib/python3.12/site-packages/pymupdf/__init__.py')
    assert not content_allowed('/root/.ssh/id_rsa')
    assert not content_allowed('/etc/passwd')
    assert not content_allowed('/root/miniconda3/lib/secret.txt')
    assert content_allowed('/usr/lib/x86_64-linux-gnu/libc.so.6')
    assert metadata_allowed('/root') and not metadata_allowed('/root/.ssh')
    assert normalize('/usr/share/texmf/../texlive/texmf-dist') == '/usr/share/texlive/texmf-dist'
    assert not library_name('../libc.so.6') and not library_name('$ORIGIN/libc.so.6')
    assert elf_parser(b'not ELF') is None
    print('SELF_TEST_PASS: scope/parser assertions; no resource reads or output-root access')


if __name__ == '__main__':
    require(sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode,
            'invoke configured Python with -I -S -B')
    helper_bytes, _ = read_regular(HELPER)
    if sys.argv[1:] == ['--self-test']:
        self_test(load_elf_helper(helper_bytes))
    elif len(sys.argv) == 3 and sys.argv[1] == '--capture':
        require(len(sys.argv[2]) == 64 and all(c in '0123456789abcdef' for c in sys.argv[2]), 'review SHA256 required')
        capture(sys.argv[2], helper_bytes)
    else:
        raise SystemExit('usage: --self-test | --capture REVIEW_SHA256')
