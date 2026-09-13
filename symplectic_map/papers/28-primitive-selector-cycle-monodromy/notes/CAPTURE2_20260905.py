#!/usr/bin/env python3
"""Paper28 capture successor: metadata census first; bounded one-read receipts.

No subprocess/network/compiler calls. --self-test uses memory fixtures only.
--capture REVIEW_SHA uses one exclusive new evidence root; never retries.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import stat
import sys
import tarfile

PROJECT = Path('/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy')
NOTES = PROJECT / 'notes'
OUTPUT = NOTES / 'dependency-capture2-20260905'
PLAN = NOTES / 'CAPTURE2_PLAN_20260905.md'
REVIEW = NOTES / 'CAPTURE2_REVIEW_20260905.md'
BASE_PATH = NOTES / 'DEPENDENCY_CAPTURE_20260905.py'
BASE_SHA = '7b6731cb725a63beefea1ff3f46588be919e9858183f529dcec61bf66610393f'
ELF_PATH = NOTES / 'CAPTURE_ELF_20260905.py'
ELF_SHA = '3e68a46b6821e500b2e95358f43c2de8803dd9f7f27669dce49406ecc95a9fa6'
PRIOR_RESULT = NOTES / 'DEPENDENCY_CAPTURE_RESULT_20260905.md'
PRIOR_RESULT_SHA = '8028fcb97e130cd162393388e48bb82ae437e7484505f2ff88cd3e6abeee2e5c'
MAX_FILE = 256 * 1024 * 1024
MAX_TOTAL = 2 * 1024 * 1024 * 1024
MAX_ENTRIES = 50000
MAX_WAVES = 64
TEX = '/usr/share/texlive/texmf-dist'
PYLIB = '/root/miniconda3/lib/python3.12'
LATEX_FAMILIES = ('base', 'amsmath', 'amsfonts', 'amscls', 'geometry', 'microtype',
    'mathtools', 'tools', 'booktabs', 'enumitem', 'natbib', 'xurl', 'hyperref',
    'graphics', 'graphics-cfg', 'graphics-def', 'l3backend', 'l3kernel', 'etoolbox',
    'kvoptions', 'hycolor', 'letltxmacro', 'auxhook', 'refcount', 'rerunfilecheck',
    'url', 'atveryend', 'oberdiek')
TREES = {TEX + '/tex/latex/' + family: () for family in LATEX_FAMILIES}
TREES.update({
    TEX + '/tex/generic': ('tex4ht',),
    TEX + '/tex/plain/base': (), TEX + '/tex/context/base/mkii': (),
    TEX + '/web2c': (), TEX + '/bibtex/bst/natbib': (), TEX + '/bibtex/bst/base': (),
    TEX + '/fonts/tfm/public/cm': (), TEX + '/fonts/tfm/public/amsfonts': (),
    TEX + '/fonts/type1/public/amsfonts': (), TEX + '/fonts/enc/dvips/base': (),
    TEX + '/fonts/map/fontname': (), '/usr/share/texmf/tex/latex/lm': (),
    '/usr/share/texmf/fonts/tfm/public/lm': (), '/usr/share/texmf/fonts/type1/public/lm': (),
    '/usr/share/texmf/fonts/enc/dvips/lm': (), '/usr/share/texmf/fonts/map/dvips/lm': (),
    '/usr/share/fonts/type1/lmodern': (), '/etc/texmf': (),
    '/var/lib/texmf/web2c/pdftex': (), '/var/lib/texmf/fonts/map/pdftex/updmap': (),
    '/usr/share/poppler': (), '/etc/fonts': (), '/usr/share/fontconfig': (),
    '/var/cache/fontconfig': (), '/usr/share/fonts/truetype/dejavu': (),
    '/usr/share/fonts/truetype/liberation2': (), '/usr/share/fonts/type1/urw-base35': (),
    '/usr/share/fonts/opentype/urw-base35': (),
    PYLIB: ('site-packages', 'test', 'idlelib', 'tkinter', 'turtledemo', 'ensurepip',
            'config-3.12-x86_64-linux-gnu'),
    PYLIB + '/site-packages/pymupdf': (), PYLIB + '/site-packages/fitz': (),
})
LIBDIRS = ('/root/miniconda3/lib', '/usr/lib/x86_64-linux-gnu',
           '/lib/x86_64-linux-gnu', '/lib64', '/usr/lib64')
TOOLS = ('/usr/bin/pdflatex', '/usr/bin/bibtex', '/usr/bin/kpsewhich',
         '/usr/bin/pdfinfo', '/usr/bin/pdftotext', '/usr/bin/pdffonts',
         '/usr/bin/pdftoppm', '/root/miniconda3/bin/python3',
         '/root/miniconda3/bin/python3.12')
DATA = (TEX + '/ls-R', '/usr/share/texmf/ls-R', '/var/lib/texmf/ls-R',
        '/var/lib/texmf/ls-R-TEXLIVEDIST', '/var/lib/texmf/ls-R-TEXMFMAIN',
        '/usr/share/texmf/web2c/texmf.cnf', '/var/lib/texmf/web2c/texmf.cnf',
        '/etc/ld.so.cache', '/usr/share/zoneinfo/UTC', '/usr/share/zoneinfo/Etc/UTC')
EXACT = frozenset(TOOLS + DATA + ('/usr/bin/pdftex', '/usr/bin/bibtex.original',
    '/etc/alternatives/bibtex'))
REQUIRED = tuple(TEX + '/tex/latex/' + name for name in (
    'base/article.cls', 'base/fontenc.sty', 'base/inputenc.sty',
    'geometry/geometry.sty', 'microtype/microtype.sty', 'amsmath/amsmath.sty',
    'amsfonts/amssymb.sty', 'amscls/amsthm.sty', 'mathtools/mathtools.sty',
    'tools/bm.sty', 'booktabs/booktabs.sty', 'tools/array.sty', 'tools/tabularx.sty',
    'enumitem/enumitem.sty', 'natbib/natbib.sty', 'xurl/xurl.sty',
    'hyperref/hyperref.sty')) + (
    '/usr/share/texmf/tex/latex/lm/lmodern.sty', TEX + '/bibtex/bst/natbib/plainnat.bst',
    '/var/lib/texmf/web2c/pdftex/pdflatex.fmt',
    '/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def administrative_read(path):
    """Exact control-code read; never used for resource content."""
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or before.st_size > 2 * 1024 * 1024:
            raise ValueError('administrative-file type/size')
        data = b''
        while len(data) < before.st_size:
            chunk = os.read(fd, before.st_size - len(data))
            if not chunk:
                raise ValueError('short administrative read')
            data += chunk
        def stable(st):
            return (st.st_dev, st.st_ino, st.st_mode, st.st_nlink, st.st_size,
                    st.st_mtime_ns, st.st_ctime_ns)
        if stable(os.fstat(fd)) != stable(before) or stable(os.lstat(path)) != stable(before):
            raise ValueError('administrative read drift')
        return data
    finally:
        os.close(fd)


def load_utilities():
    data = administrative_read(BASE_PATH)
    if sha(data) != BASE_SHA:
        raise ValueError('frozen utility identity')
    ns = {'__name__': 'paper28_capture2_utilities', '__file__': str(BASE_PATH)}
    exec(compile(data, str(BASE_PATH), 'exec'), ns)
    ns.update(TREES=TREES, LIBDIRS=LIBDIRS, EXACT=EXACT, OUTPUT=OUTPUT,
              MAX_FILE=MAX_FILE, MAX_TOTAL=MAX_TOTAL, MAX_ENTRIES=MAX_ENTRIES)
    original_write = ns['write_new']

    def durable_write(name, data):
        original_write(name, data)
        parent = ns['parent_descriptor'](OUTPUT / name)
        try:
            os.fsync(parent)
        finally:
            os.close(parent)

    ns['write_new'] = durable_write
    return ns


class Budget:
    def __init__(self, total=MAX_TOTAL, per_file=MAX_FILE):
        self.limit, self.per_file, self.used = total, per_file, 0

    def reserve(self, size):
        if not 0 <= size <= self.per_file or self.used + size > self.limit:
            raise ValueError('pre-read resource budget exceeded')

    def read_bytes(self, reader, size, progress):
        self.reserve(size)  # Must precede the first read, including synthetic tests.
        chunks, done = [], 0
        while done < size:
            request = min(1024 * 1024, size - done)
            block = reader(request)
            if not block or len(block) > request:
                raise ValueError('short/invalid bounded read')
            self.used += len(block)
            done += len(block)
            chunks.append(block)
            progress(block)
        return b''.join(chunks)


def make_collector(base, journal, elf_parser):
    require, ident = base['require'], base['identity']

    class Collector:
        # Reuse only metadata link traversal, static metadata edge lookup,
        # and terminal metadata checks; never the old resource read/add loop.
        resolve = base['Scanner'].resolve
        native_closure = base['Scanner'].native_closure
        terminal_rebind = base['Scanner'].terminal_rebind

        def __init__(self):
            self.rows, self.observations, self.stat_objects = {}, {}, {}
            self.omissions, self.edges, self.pending_elf = [], [], []
            self.omission_keys, self.captured = set(), set()
            self.aliases, self.budget, self.active_read = {}, Budget(), None

        def event(self, obj, durable=False):
            journal.write((json.dumps(obj, sort_keys=True, ensure_ascii=True) + '\n').encode())
            if durable:
                journal.flush()
                os.fsync(journal.fileno())

        def omit(self, path, reason, **details):
            row = {'path': path, 'reason': reason, **details}
            key = json.dumps(row, sort_keys=True)
            if key not in self.omission_keys:
                self.omission_keys.add(key)
                self.omissions.append(row)
                self.event({'omission': row})

        def add(self, path, kind, st, target=None):
            if path in self.rows:
                require(self.observations[path] == ident(st), 'metadata revisit drift: ' + path)
                return
            require(len(self.rows) < MAX_ENTRIES, 'metadata entry limit')
            row = {'path': path, 'kind': kind, **base['metadata'](st)}
            if kind == 'symlink':
                row['target'] = target
            self.rows[path], self.observations[path], self.stat_objects[path] = row, ident(st), st
            self.event({'metadata': row})

        def visit(self, path, essential=False):
            self.event({'census_request': path})
            try:
                resolved, st = self.resolve(path)
            except (FileNotFoundError, NotADirectoryError, base['OutsideEnvelope']) as exc:
                self.omit(path, type(exc).__name__, detail=str(exc))
                require(not essential, 'required input unavailable: ' + path)
                return None
            self.aliases[path] = resolved
            if resolved in self.rows and self.rows[resolved]['kind'] != 'symlink':
                require(self.observations[resolved] == ident(st), 'metadata revisit drift: ' + resolved)
                return resolved
            if stat.S_ISREG(st.st_mode):
                require(st.st_size <= MAX_FILE, 'metadata single-file bound: ' + resolved)
                self.add(resolved, 'file', st)
            elif stat.S_ISDIR(st.st_mode):
                require(base['in_tree'](resolved), 'directory census outside named resource roots')
                self.add(resolved, 'dir', st)
                members = base['safe_listdir'](resolved, st)
                for child in members:
                    candidate = base['normalize'](resolved + '/' + child)
                    if base['content_allowed'](candidate):
                        self.visit(candidate)
                    else:
                        self.omit(candidate, 'declared_exclusion')
                require(members == base['safe_listdir'](resolved, st), 'membership drift')
                self.rows[resolved]['members'] = members
            else:
                self.omit(resolved, 'non_regular_resource')
                require(not essential, 'required input is special')
                return None
            return resolved

        def unread(self):
            return sorted(path for path, row in self.rows.items()
                          if row['kind'] == 'file' and path not in self.captured)

        def census_wave(self, wave):
            paths = self.unread()
            capacity = sum(self.rows[path]['size'] for path in paths)
            require(self.budget.used + capacity <= MAX_TOTAL, 'whole-wave capacity bound before read')
            record = {'wave': wave, 'resource_reads_before_wave': self.budget.used,
                'pending_regular_bytes': capacity, 'remaining_budget': MAX_TOTAL - self.budget.used,
                'entry_count': len(self.rows),
                'entries': [dict(self.rows[path]) for path in sorted(self.rows)],
                'pending_regular_paths': paths, 'omissions': list(self.omissions)}
            name = 'census-%03d.json' % wave
            base['write_new'](name, base['encoded'](record))
            self.event({'capacity_pass': {'wave': wave, 'bytes': capacity,
                'files': len(paths), 'read_so_far': self.budget.used}}, durable=True)
            print(json.dumps({'census_wave': wave, 'pending_files': len(paths),
                              'pending_bytes': capacity, 'read_so_far': self.budget.used}), flush=True)
            return name, paths

        def read_one(self, path):
            expected, st_expected = self.rows[path], self.stat_objects[path]
            size = expected['size']
            self.active_read = {'path': path, 'expected_bytes': size, 'read_bytes': 0,
                                'sha256_so_far': sha(b''), 'resource_reads_before': self.budget.used,
                                'remaining_budget': MAX_TOTAL - self.budget.used}
            self.event({'read_intent': dict(self.active_read)}, durable=True)
            self.budget.reserve(size)  # Before opening the regular input.
            parent, fd = base['parent_descriptor'](path), None
            digest = hashlib.sha256()
            try:
                fd = os.open(Path(path).name, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent)
                before = os.fstat(fd)
                require(ident(before) == ident(st_expected), 'pre-read descriptor drift: ' + path)
                self.budget.reserve(before.st_size)  # Again before the first os.read.

                def progress(block):
                    digest.update(block)
                    self.active_read['read_bytes'] += len(block)
                    self.active_read['sha256_so_far'] = digest.hexdigest()

                data = self.budget.read_bytes(lambda count: os.read(fd, count), size, progress)
                require(ident(before) == ident(os.fstat(fd)), 'post-read descriptor drift: ' + path)
                require(ident(before) == ident(os.stat(Path(path).name, dir_fd=parent, follow_symlinks=False)),
                        'post-read parent-relative drift: ' + path)
                require(ident(before) == ident(base['safe_lstat'](path)), 'post-read pathname drift: ' + path)
                return data
            finally:
                if fd is not None:
                    os.close(fd)
                os.close(parent)

        def copy_wave(self, archive, paths):
            for path in paths:
                data = self.read_one(path)
                row = self.rows[path]
                row.update(sha256=sha(data), lf=data.count(b'\n'))
                info = tar_info(row)
                archive.addfile(info, io.BytesIO(data))
                self.captured.add(path)
                self.event({'read_complete': {'path': path, 'bytes': len(data),
                    'sha256': row['sha256'], 'lf': row['lf'], 'resource_reads': self.budget.used}})
                self.active_read = None
                try:
                    elf = elf_parser(data)
                except ValueError as exc:
                    self.omit(path, 'unsupported_or_malformed_elf', detail=str(exc))
                    elf = None
                if elf is not None:
                    self.pending_elf.append((path, elf))
            # The old edge enumerator calls our metadata-only visit. New files
            # are read solely in a subsequent budget-checked wave.
            batch = list(self.pending_elf)
            self.pending_elf = batch
            self.native_closure()
            self.pending_elf = []

    return Collector()


def tar_info(row):
    info = tarfile.TarInfo(row['path'].lstrip('/'))
    info.uid = info.gid = info.mtime = 0
    info.uname = info.gname = ''
    info.mode = int(row['mode'], 8)
    if row['kind'] == 'file':
        info.size = row['size']
    elif row['kind'] == 'dir':
        info.type = tarfile.DIRTYPE
    elif row['kind'] == 'symlink':
        info.type, info.linkname = tarfile.SYMTYPE, row['target']
    else:
        raise ValueError('unsupported archive member type')
    return info


def run_capture(base, review_sha):
    require = base['require']
    code = administrative_read(Path(__file__))
    plan, review = administrative_read(PLAN), administrative_read(REVIEW)
    helper, prior = administrative_read(ELF_PATH), administrative_read(PRIOR_RESULT)
    require(sha(helper) == ELF_SHA and sha(prior) == PRIOR_RESULT_SHA, 'helper/history drift')
    require(sha(review) == review_sha, 'independent review identity')
    text = review.decode('utf-8')
    require('\nDecision: CAPTURE2_PLAN_CODE_PASS\n' in text, 'review decision')
    for label, digest in (('Plan', sha(plan)), ('Scanner', sha(code)),
                          ('Utilities', BASE_SHA), ('ELF helper', ELF_SHA)):
        require(label + ' SHA256: ' + digest in text, 'review byte binding: ' + label)
    helper_ns = {'__name__': 'capture2_elf'}
    exec(compile(helper, str(ELF_PATH), 'exec'), helper_ns)
    sources = base['source_bindings']()
    parent = base['parent_descriptor'](OUTPUT)
    try:
        os.mkdir(OUTPUT.name, 0o700, dir_fd=parent)
        os.fsync(parent)
    finally:
        os.close(parent)
    collector, created = None, []
    try:
        base['write_new']('intent.json', base['encoded']({'authorization':
            'latest user confirmation of fresh narrowed capture after prior failure',
            'plan_sha256': sha(plan), 'scanner_sha256': sha(code), 'utilities_sha256': BASE_SHA,
            'elf_sha256': ELF_SHA, 'review_sha256': review_sha, 'prior_result_sha256': PRIOR_RESULT_SHA,
            'sources': sources, 'trees': TREES, 'exact_inputs': sorted(EXACT),
            'required_files': REQUIRED, 'tools': TOOLS, 'library_directories': LIBDIRS,
            'limits': {'total_resource_reads': MAX_TOTAL, 'per_file': MAX_FILE,
                       'entries': MAX_ENTRIES, 'waves': MAX_WAVES}}))
        created.append('intent.json')
        with base['create_file']('events.jsonl') as journal:
            created.append('events.jsonl')
            collector = make_collector(base, journal, helper_ns['elf_dependencies'])
            for root in TREES:
                collector.visit(root)
            for path in DATA:
                collector.visit(path)
            for path in TOOLS + REQUIRED:
                target = collector.visit(path, essential=True)
                require(collector.rows[target]['kind'] == 'file', 'required input not regular')
            with base['create_file']('capsule.tar') as archive_file:
                created.append('capsule.tar')
                with tarfile.open(fileobj=archive_file, mode='w|', format=tarfile.PAX_FORMAT) as archive:
                    for wave in range(MAX_WAVES):
                        name, paths = collector.census_wave(wave)
                        created.append(name)
                        if not paths:
                            break
                        collector.copy_wave(archive, paths)
                    else:
                        raise ValueError('native metadata closure wave limit')
                    collector.terminal_rebind()
                    require(base['source_bindings']() == sources, 'terminal source drift')
                    require(not collector.unread() and collector.active_read is None, 'incomplete capture')
                    require(collector.budget.used == sum(row['size'] for row in collector.rows.values()
                            if row['kind'] == 'file'), 'read/archive accounting mismatch')
                    for path in sorted(collector.rows):
                        if collector.rows[path]['kind'] != 'file':
                            archive.addfile(tar_info(collector.rows[path]))
                archive_file.flush()
                os.fsync(archive_file.fileno())
            journal.flush()
            os.fsync(journal.fileno())
        manifest = {'schema': 'paper28-capture2-v1',
            'entries': [collector.rows[path] for path in sorted(collector.rows)],
            'aliases': collector.aliases, 'native_edges': collector.edges,
            'unresolved_native_edges': [edge for edge in collector.edges if not edge['candidates']],
            'omissions': collector.omissions, 'sources': sources,
            'actual_resource_read_bytes': collector.budget.used}
        base['write_new']('manifest.json', base['encoded'](manifest))
        created.append('manifest.json')
        outcome = {'decision': 'CAPTURE2_RECORDED_REVIEW_REQUIRED',
            'outputs': {name: base['hash_output'](name) for name in sorted(created)},
            'entries': len(collector.rows), 'regular_files': len(collector.captured),
            'actual_resource_read_bytes': collector.budget.used,
            'unresolved_native_edges': len(manifest['unresolved_native_edges']),
            'omissions': len(collector.omissions), 'compiler_invocations': 0,
            'limitations': ['Trusted administrative bootstrap/kernel, not atomic filesystem snapshot',
                'Native candidate superset, not general loader/dlopen completeness',
                'Independent capsule and executable build-profile review still required']}
        base['write_new']('outcome.json', base['encoded'](outcome))
        print(json.dumps(outcome, sort_keys=True), flush=True)
    except BaseException as exc:
        failure = {'decision': 'CAPTURE2_FAILED_PRESERVED_NO_RETRY',
            'exception': type(exc).__name__, 'detail': str(exc),
            'active_read': collector.active_read if collector else None,
            'actual_resource_read_bytes': collector.budget.used if collector else 0}
        try:
            base['write_new']('failure.json', base['encoded'](failure))
        except BaseException:
            pass
        raise


def self_test(base):
    # Insufficient budgets must not call the reader even once.
    for limit, used, size, per_file in ((3, 0, 4, 8), (5, 3, 3, 8), (10, 0, 5, 4)):
        budget, called = Budget(limit, per_file), []
        budget.used = used
        try:
            budget.read_bytes(lambda count: called.append(count) or b'x' * count,
                              size, lambda block: None)
        except ValueError:
            pass
        else:
            raise AssertionError('oversized synthetic read accepted')
        assert called == [] and budget.used == used
    budget, calls = Budget(5, 5), []
    data = budget.read_bytes(lambda count: calls.append(count) or b'x' * count,
                             5, lambda block: None)
    assert data == b'xxxxx' and calls == [5] and budget.used == 5
    assert budget.read_bytes(lambda count: (_ for _ in ()).throw(AssertionError()),
                             0, lambda block: None) == b''
    assert not base['content_allowed'](TEX + '/fonts/truetype/public/unrelated/font.ttf')
    assert not base['content_allowed'](TEX + '/tex/generic/tex4ht/tex4ht.sty')
    assert not base['content_allowed']('/root/.ssh/id_rsa')
    assert base['content_allowed']('/usr/share/texmf/fonts/type1/public/lm/lmr10.pfb')
    for path in TOOLS + REQUIRED:
        assert base['content_allowed'](path), path
    stream = io.BytesIO()
    row = {'path': '/usr/share/texmf/synthetic', 'kind': 'file', 'size': 3, 'mode': '0644'}
    with tarfile.open(fileobj=stream, mode='w') as archive:
        archive.addfile(tar_info(row), io.BytesIO(b'abc'))
    stream.seek(0)
    with tarfile.open(fileobj=stream, mode='r:') as archive:
        assert archive.extractfile(archive.getmembers()[0]).read() == b'abc'
    print('CAPTURE2_SELF_TEST_PASS: pre-read refusal, cumulative/per-file limits, exact-bound reads, scope and memory archive')


if __name__ == '__main__':
    if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode):
        raise SystemExit('invoke configured Python with -I -S -B')
    utilities = load_utilities()
    if sys.argv[1:] == ['--self-test']:
        self_test(utilities)
    elif len(sys.argv) == 3 and sys.argv[1] == '--capture' and len(sys.argv[2]) == 64:
        run_capture(utilities, sys.argv[2])
    else:
        raise SystemExit('usage: --self-test | --capture REVIEW_SHA256')
