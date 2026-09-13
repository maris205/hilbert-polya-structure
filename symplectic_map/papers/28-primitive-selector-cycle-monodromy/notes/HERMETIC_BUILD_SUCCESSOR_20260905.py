#!/root/miniconda3/bin/python3.12
"""Paper28 reviewed manuscript/validator successor, one-shot captured-only build.

Administrative Python -I -S -B only. --preflight never extracts/executes/writes.
--execute requires an independently authored exact-hash review gate. Any
execution-root failure preserves that root; there is no retry/repair API.
"""
import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import resource
import signal
import stat
import subprocess
import sys
import tarfile
import time

PROJECT = Path('/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy')
NOTES = PROJECT / 'notes'
CAPTURE = NOTES / 'dependency-capture2-20260905'
BUILD = PROJECT / 'build-capsule-successor-20260905'
REVIEW = NOTES / 'HERMETIC_BUILD_SUCCESSOR_REVIEW_20260905.json'
CONTROL_NAMES = ('HERMETIC_BUILD_SUCCESSOR_20260905.py', 'HERMETIC_BUILD_SUCCESSOR_PLAN_20260905.md',
                 'PDF_ACCEPTANCE_SUCCESSOR_20260905.py', 'LOADER_SELECTION_20260905.json',
                 'SOURCE_SUCCESSOR_REVIEW_20260905.md')
CAPTURE_SOURCE_DIR = PROJECT / 'paper'
SOURCE_DIR = PROJECT / 'paper-successor-20260905'
# Historical source pins belong to CAPTURE2/EC recording provenance forever.
CAPTURE_SOURCES = {
 'main.tex': ('bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e', 73733, 1605),
 'math_commands.tex': ('16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5', 444, 14),
 'references.bib': ('e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e', 6104, 204),
}
# Actual compilation pins belong to the separately reviewed successor trio.
SOURCE = {
 'main.tex': ('7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9', 84983, 1855),
 'math_commands.tex': ('16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5', 444, 14),
 'references.bib': ('e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e', 6104, 204),
}
VALIDATOR_SHA = 'af6125f5c7499e437f9e56aa54197bcadd3402e3a33d4607a9a1319a3e72f464'
SOURCE_REVIEW_SHA = 'a6c4c4de718dfab8afba7c19026678eb0a4241878e969c403606b722de04b76d'
AUDIT_SHA = '267648ddcc4292593c1c3d7e159fbcac96b6d3f455f9d6afeaaa5d03a741dc8b'
OUTCOME_SHA = '8a081a5f7a66fbcdd4d47899c4af1581ac9fba65c25d002609c118fc634b69f2'
MANIFEST_SHA = '6107892d5f9750e91ae48292a68117d490876b8a3164758dfdc3442e04eebb8d'
ARCHIVE_SHA = 'c1b7f241f2ef7d49de26868b5a23642eb0ddd1271896a72faeea4da97ccc457a'
LOADER_SHA = 'ecc5e3751def20eac1bb96a2ddb5336925d46cf8fcb80b5ee60f4ab25bed9606'
# The sole supplemental dependency input is the audited snapshot, never its live path.
SUPPLEMENT = NOTES / 'dependency-ec-supplement-20260905'
SUPPLEMENT_NAME = 'ecrm1095.tfm'
SUPPLEMENT_TARGET = '/usr/share/texlive/texmf-dist/fonts/tfm/jknappen/ec/ecrm1095.tfm'
SUPPLEMENT_OUTCOME_SHA = '507016423515267d4ab5ab55e9e08cc2818391a4f4e00ec803b3870d75645535'
SUPPLEMENT_AUDIT_SHA = '887fa0213c9a6866fc1ca7a4da0fd1fa951461c788a44b4e061818d7881f9a70'
SUPPLEMENT_FILE = {'bytes': 3584,
    'sha256': '6a3850cd71bbb2f43d98b7eb6b47f925de25626f5f4a0648c2d9d7b4b774eb2a',
    'lf': 12, 'mode': '0o644'}
SUPPLEMENT_OUTPUT_NAMES = frozenset(('intent.json', 'independent-review.json',
    'attempt.json', 'metadata-before.json', 'metadata-after.json', SUPPLEMENT_NAME))
UID = GID = 65534
CACHES = ('texmf-var', 'texmf-config', 'texmf-home', 'xdg-cache', 'tmp')
READ_FLAGS = os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC
DIR_FLAGS = READ_FLAGS | os.O_DIRECTORY
LIMITS = {'wall_seconds': 180, 'cpu_seconds': 120,
          'file_bytes': 128 * 1024**2, 'address_space_bytes': 2 * 1024**3,
          'open_files': 64, 'core_bytes': 0}
TREES = ('/etc/texmf', '/var/lib/texmf', '/usr/share/texmf',
         '/usr/share/texlive/texmf-dist')


def tree_path(suffix):
    return ':'.join(tree + suffix for tree in TREES)


ENV = {
 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC', 'PATH': '/usr/bin',
 'SOURCE_DATE_EPOCH': '0', 'FORCE_SOURCE_DATE': '1',
 'PYMUPDF_SUGGEST_LAYOUT_ANALYZER': '0',
 'TEXMF': '{' + ','.join(TREES) + '}', 'TEXMFDBS': ':'.join(TREES),
 'TEXMFCNF': '/etc/texmf/web2c:/usr/share/texlive/texmf-dist/web2c',
 'TEXMFVAR': '/work/texmf-var', 'TEXMFCONFIG': '/work/texmf-config',
 'TEXMFHOME': '/work/texmf-home', 'XDG_CACHE_HOME': '/work/xdg-cache',
 'TMPDIR': '/work/tmp', 'TEXMFCACHE': '/work/texmf-var',
 'VARTEXFONTS': '/work/texmf-var', 'WEB2C': tree_path('/web2c'),
 'TEXPOOL': tree_path('/web2c'),
 'TEXINPUTS': '/source:/work:' + tree_path('/tex//'),
 'BIBINPUTS': '/source', 'BSTINPUTS': tree_path('/bibtex/bst//'),
 'TEXFORMATS': '/var/lib/texmf/web2c/pdftex',
 'TFMFONTS': tree_path('/fonts/tfm//'), 'VFFONTS': tree_path('/fonts/vf//'),
 'TEXFONTMAPS': tree_path('/fonts/map//'),
 'T1FONTS': tree_path('/fonts/type1//') + ':/usr/share/fonts/type1//',
 'ENCFONTS': tree_path('/fonts/enc//'),
 'TEXPSHEADERS': tree_path('/dvips//') + ':' + tree_path('/fonts/enc//'),
 'PDFTEXCONFIG': tree_path('/pdftex//'), 'OSFONTDIR': '/usr/share/fonts',
 'FONTCONFIG_FILE': '/etc/fonts/fonts.conf', 'FONTCONFIG_PATH': '/etc/fonts',
 'MKTEXFMT': '0', 'MKTEXTFM': '0', 'MKTEXPK': '0',
 'shell_escape': '0', 'openin_any': 'p', 'openout_any': 'p',
}
TEX_ARGS = ['-progname=pdflatex', '-fmt=pdflatex', '-interaction=nonstopmode',
            '-halt-on-error', '-file-line-error', '-no-shell-escape', '-recorder',
            '-jobname=main',
            r'\pdfinfoomitdate=1\relax\pdftrailerid{}\pdfsuppressptexinfo=15\relax'
            r'\pdfcompresslevel=0\relax\pdfobjcompresslevel=0\relax'
            r'\pdfminorversion=5\relax\input{main.tex}']
COMMANDS = (
 ('01-latex', 'pdftex', TEX_ARGS), ('02-bibtex', 'bibtex', ['main']),
 ('03-latex', 'pdftex', TEX_ARGS), ('04-latex', 'pdftex', TEX_ARGS),
 ('05-pdfinfo', 'pdfinfo', ['-rawdates', '/work/main.pdf']),
 ('06-pdfmeta', 'pdfinfo', ['-meta', '/work/main.pdf']),
 ('07-pdffonts', 'pdffonts', ['/work/main.pdf']),
 ('08-pdftext', 'pdftotext', ['-layout', '-enc', 'UTF-8', '/work/main.pdf', '-']),
 ('09-validator', 'python_validator', ['-I', '-S', '-B',
  '/control/PDF_ACCEPTANCE_SUCCESSOR_20260905.py', '--pdf', '/work/main.pdf',
  '--source-dir', '/source', '--bbl', '/work/main.bbl', '--output-dir',
  '/work/report', '--site-packages', '/root/miniconda3/lib/python3.12/site-packages']),
)
FINAL_FILES = tuple('main.' + ext for ext in ('pdf', 'aux', 'bbl', 'blg', 'log', 'out', 'fls'))
LIBC = ctypes.CDLL(None, use_errno=True)
LIBC.prctl.argtypes = [ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong,
                       ctypes.c_ulong, ctypes.c_ulong]
LIBC.prctl.restype = ctypes.c_int


class CapHeader(ctypes.Structure):
    _fields_ = [('version', ctypes.c_uint32), ('pid', ctypes.c_int)]


class CapData(ctypes.Structure):
    _fields_ = [('effective', ctypes.c_uint32), ('permitted', ctypes.c_uint32),
                ('inheritable', ctypes.c_uint32)]


LIBC.capset.argtypes = [ctypes.POINTER(CapHeader), ctypes.POINTER(CapData)]
LIBC.capget.argtypes = [ctypes.POINTER(CapHeader), ctypes.POINTER(CapData)]
LIBC.capset.restype = LIBC.capget.restype = ctypes.c_int


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def regular_read(path):
    with os.fdopen(os.open(path, READ_FLAGS), 'rb') as stream:
        before = os.fstat(stream.fileno())
        require(stat.S_ISREG(before.st_mode), 'not regular: ' + str(path))
        data = stream.read()
        after = os.fstat(stream.fileno())
        require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns,
                 before.st_ctime_ns) == (after.st_dev, after.st_ino, after.st_size,
                 after.st_mtime_ns, after.st_ctime_ns), 'read mutation: ' + str(path))
    return data


def hash_file(path):
    h = hashlib.sha256()
    count = 0
    with os.fdopen(os.open(path, READ_FLAGS), 'rb') as stream:
        before = os.fstat(stream.fileno())
        require(stat.S_ISREG(before.st_mode), 'not regular: ' + str(path))
        for data in iter(lambda: stream.read(1024**2), b''):
            h.update(data)
            count += len(data)
        after = os.fstat(stream.fileno())
        require((before.st_size, before.st_mtime_ns, before.st_ctime_ns) ==
                (after.st_size, after.st_mtime_ns, after.st_ctime_ns), 'hash mutation')
    return {'bytes': count, 'sha256': h.hexdigest()}


def write_new(path, data, mode=0o600):
    with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL |
                           os.O_NOFOLLOW | os.O_CLOEXEC, mode), 'wb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def json_new(path, value):
    write_new(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def source_binding(directory, expected_sources=SOURCE):
    values = {}
    for name, (expected, size, lf) in expected_sources.items():
        data = regular_read(directory / name)
        require((digest(data), len(data), data.count(b'\n')) == (expected, size, lf),
                'source mismatch: ' + str(directory / name))
        values[name] = {'sha256': expected, 'bytes': size, 'lf': lf}
    return values


def safe_relative(name):
    require(isinstance(name, str) and bool(name) and not name.startswith('/'),
            'absolute/empty member name')
    parts = name.split('/')
    require(all(p not in ('', '.', '..') for p in parts), 'noncanonical member')
    require('\x00' not in name, 'NUL member')
    return tuple(parts)


def inventory(manifest):
    entries = {}
    for entry in manifest['entries']:
        path = entry['path']
        require(path.startswith('/'), 'manifest path not absolute')
        safe_relative(path[1:])
        require(path not in entries, 'duplicate manifest path')
        require(entry['kind'] in ('file', 'dir', 'symlink'), 'unsupported entry kind')
        entries[path] = entry
    require(len(entries) == 6838, 'manifest count mismatch')
    directories = set()
    for path, entry in entries.items():
        if entry['kind'] == 'dir':
            directories.add(path)
        for parent in PurePosixPath(path).parents:
            if str(parent) != '/':
                directories.add(str(parent))
    require(all(path not in entries or entries[path]['kind'] == 'dir'
                for path in directories), 'non-directory physical ancestor')
    require(not any(path == prefix or path.startswith(prefix + '/')
                    for path in entries for prefix in ('/source', '/control', '/work', '/dev', '/proc')),
            'captured member collides with private namespace')
    return entries, directories


def supplemental_entry():
    return {'path': SUPPLEMENT_TARGET, 'kind': 'file', 'size': SUPPLEMENT_FILE['bytes'],
            'sha256': SUPPLEMENT_FILE['sha256'], 'lf': SUPPLEMENT_FILE['lf'],
            'mode': SUPPLEMENT_FILE['mode']}


def supplement_binding(capture_sources):
    """Rebind the recorded supplement to its original sources, never the new trio."""
    require(all(isinstance(value, str) and re.fullmatch('[0-9a-f]{64}', value)
                for value in (SUPPLEMENT_OUTCOME_SHA, SUPPLEMENT_AUDIT_SHA,
                              SUPPLEMENT_FILE['sha256'])) and
            type(SUPPLEMENT_FILE['lf']) is int and SUPPLEMENT_FILE['lf'] >= 0,
            'EC supplement capture/audit hashes are not finalized')
    outcome_data = regular_read(SUPPLEMENT / 'outcome.json')
    require(digest(outcome_data) == SUPPLEMENT_OUTCOME_SHA, 'EC outcome binding mismatch')
    outcome = json.loads(outcome_data)
    require(outcome.get('decision') == 'EC_METRIC_CAPTURED_AUDIT_PENDING' and
            outcome.get('source_path') == SUPPLEMENT_TARGET and
            outcome.get('budget_bytes') == 4096 and
            outcome.get('host_bytes_read') == SUPPLEMENT_FILE['bytes'] and
            outcome.get('sources') == capture_sources and outcome.get('file') == SUPPLEMENT_FILE and
            outcome.get('no_retry') is True, 'EC capture contract mismatch')
    require(set(outcome['outputs']) == SUPPLEMENT_OUTPUT_NAMES, 'EC output seal set mismatch')
    outputs = {}
    for name in sorted(SUPPLEMENT_OUTPUT_NAMES):
        outputs[name] = hash_file(SUPPLEMENT / name)
        require(outputs[name] == outcome['outputs'][name], 'EC output seal mismatch: ' + name)
    require(outputs[SUPPLEMENT_NAME] == {'bytes': SUPPLEMENT_FILE['bytes'],
            'sha256': SUPPLEMENT_FILE['sha256']}, 'EC file seal mismatch')
    audit_data = regular_read(NOTES / 'EC_SUPPLEMENT_AUDIT_20260905.md')
    require(digest(audit_data) == SUPPLEMENT_AUDIT_SHA, 'EC audit binding mismatch')
    return {'target': SUPPLEMENT_TARGET, 'file': dict(SUPPLEMENT_FILE),
            'outcome': {'bytes': len(outcome_data), 'sha256': SUPPLEMENT_OUTCOME_SHA},
            'audit': {'bytes': len(audit_data), 'sha256': SUPPLEMENT_AUDIT_SHA},
            'outputs': outputs, 'capture_bindings': outcome['bindings'],
            'budget_bytes': 4096, 'host_bytes_read': outcome['host_bytes_read']}


def extend_inventory(entries, directories):
    """Keep all 6838 original entries; add exactly one file and real ancestors."""
    require(len(entries) == 6838 and SUPPLEMENT_TARGET not in entries,
            'EC target already captured or original member count changed')
    safe_relative(SUPPLEMENT_TARGET[1:])
    extended = dict(entries)
    extended[SUPPLEMENT_TARGET] = supplemental_entry()
    ancestors = {str(parent) for parent in PurePosixPath(SUPPLEMENT_TARGET).parents
                 if str(parent) != '/'}
    all_directories = set(directories) | ancestors
    require(all(path not in extended or extended[path]['kind'] == 'dir'
                for path in all_directories), 'EC ancestor is not a real directory')
    require(len(extended) == 6839, 'supplemented member count mismatch')
    return extended, all_directories


def archive_check(entries, consume=None):
    """Stream all member bytes; optional consumer gets already verified data."""
    require(entries.get(SUPPLEMENT_TARGET) == supplemental_entry(),
            'EC manifest entry mismatch')
    base_paths = set(entries) - {SUPPLEMENT_TARGET}
    require(len(base_paths) == 6838, 'base archive member count mismatch')
    seen = set()
    pax_count = 0
    with os.fdopen(os.open(CAPTURE / 'capsule.tar', READ_FLAGS), 'rb') as raw:
        with tarfile.open(fileobj=raw, mode='r|') as archive:
            for member in archive:
                safe_relative(member.name)
                path = '/' + member.name
                require(path in base_paths and path not in seen, 'unexpected/duplicate tar member')
                seen.add(path)
                entry = entries[path]
                require(member.mode == int(entry['mode'], 8), 'tar mode mismatch')
                require(member.uid == member.gid == member.mtime == 0 and
                        not member.uname and not member.gname, 'tar metadata mismatch')
                require(set(member.pax_headers) <= {'path'}, 'unapproved PAX fields')
                if member.pax_headers:
                    pax_count += 1
                    # tarfile removes a directory header's final slash only.
                    expected_pax_path = member.name + ('/' if member.isdir() else '')
                    require(member.pax_headers['path'] == expected_pax_path, 'PAX path mismatch')
                data = None
                if entry['kind'] == 'file':
                    require(member.isreg() and not member.linkname and member.size == entry['size'],
                            'tar regular mismatch')
                    data = archive.extractfile(member).read()
                    require((len(data), digest(data), data.count(b'\n')) ==
                            (entry['size'], entry['sha256'], entry['lf']), 'tar byte mismatch: ' + path)
                elif entry['kind'] == 'dir':
                    require(member.isdir() and member.size == 0 and not member.linkname,
                            'tar directory mismatch')
                else:
                    require(member.issym() and member.size == 0 and
                            member.linkname == entry['target'], 'tar link mismatch')
                if consume is not None:
                    consume(path, entry, data)
    require(seen == base_paths and pax_count == 199, 'tar closure/PAX count mismatch')
    # This named local snapshot is not a CAPTURE2 tar member. Verify it separately
    # and send it through the same no-follow regular-file consumer before links.
    supplement_data = regular_read(SUPPLEMENT / SUPPLEMENT_NAME)
    require((len(supplement_data), digest(supplement_data), supplement_data.count(b'\n')) ==
            (SUPPLEMENT_FILE['bytes'], SUPPLEMENT_FILE['sha256'], SUPPLEMENT_FILE['lf']),
            'EC snapshot byte mismatch')
    if consume is not None:
        consume(SUPPLEMENT_TARGET, entries[SUPPLEMENT_TARGET], supplement_data)
    return {'members': len(seen) + 1, 'base_archive_members': len(seen),
            'supplemental_members': 1, 'pax_path_members': pax_count,
            'verified_regular_files': sum(e['kind'] == 'file' for e in entries.values())}


def capabilities():
    # Administrative permission check, not a captured publication dependency.
    lines = Path('/proc/self/status').read_text().splitlines()
    values = dict(line.split(':', 1) for line in lines if ':' in line)
    mask = int(values['CapEff'].strip(), 16)
    wanted = {'setgid': 6, 'setuid': 7, 'sys_chroot': 18, 'mknod': 27}
    result = {'euid': os.geteuid(), 'egid': os.getegid(), 'cap_eff': hex(mask),
              'required': {key: bool(mask & (1 << bit)) for key, bit in wanted.items()},
              'existing_seccomp': values.get('Seccomp', '').strip()}
    require(result['euid'] == result['egid'] == 0 and all(result['required'].values()),
            'required existing chroot/drop/device authority unavailable; no bypass')
    return result


def preflight():
    require(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,
            'administrative Python requires -I -S -B')
    require(re.fullmatch('[0-9a-f]{64}', VALIDATOR_SHA) and
            re.fullmatch('[0-9a-f]{64}', SOURCE_REVIEW_SHA) and
            all(re.fullmatch('[0-9a-f]{64}', sha) and size > 0 and lf >= 0
                for sha, size, lf in SOURCE.values()),
            'successor source/validator/review pins are not finalized')
    require(set(SOURCE) == set(CAPTURE_SOURCES) and
            all(SOURCE[name] == CAPTURE_SOURCES[name]
                for name in ('math_commands.tex', 'references.bib')),
            'successor macro/bibliography identity changed')
    sources = source_binding(SOURCE_DIR)
    capture_sources = source_binding(CAPTURE_SOURCE_DIR, CAPTURE_SOURCES)
    audit = regular_read(NOTES / 'CAPTURE2_AUDIT_20260905.md')
    require(digest(audit) == AUDIT_SHA, 'audit binding mismatch')
    outcome_bytes = regular_read(CAPTURE / 'outcome.json')
    require(digest(outcome_bytes) == OUTCOME_SHA, 'capture outcome mismatch')
    outcome = json.loads(outcome_bytes)
    require(len(outcome['outputs']) == 12, 'capture seal count')
    outputs = {}
    for name, expected in outcome['outputs'].items():
        require('/' not in name and name not in ('.', '..'), 'invalid sealed name')
        outputs[name] = hash_file(CAPTURE / name)
        require(outputs[name] == expected, 'capture seal mismatch: ' + name)
    require(outputs['capsule.tar']['sha256'] == ARCHIVE_SHA and
            outputs['manifest.json']['sha256'] == MANIFEST_SHA, 'core capture binding')
    manifest = json.loads(regular_read(CAPTURE / 'manifest.json'))
    require(manifest['sources'] == capture_sources and not manifest['unresolved_native_edges'],
            'manifest source/native mismatch')
    entries, directories = inventory(manifest)
    supplement = supplement_binding(capture_sources)
    entries, directories = extend_inventory(entries, directories)
    archive_summary = archive_check(entries)
    bindings = {name: hash_file(NOTES / name) for name in CONTROL_NAMES}
    require(bindings['LOADER_SELECTION_20260905.json']['sha256'] == LOADER_SHA,
            'loader selection changed')
    require(bindings['PDF_ACCEPTANCE_SUCCESSOR_20260905.py']['sha256'] == VALIDATOR_SHA,
            'successor validator binding changed')
    require(bindings['SOURCE_SUCCESSOR_REVIEW_20260905.md']['sha256'] == SOURCE_REVIEW_SHA,
            'successor source review binding changed')
    loader = json.loads(regular_read(NOTES / 'LOADER_SELECTION_20260905.json'))
    require(entries[loader['loader']['path']]['sha256'] == loader['loader']['sha256'],
            'loader executable hash mismatch')
    for profile in loader['profiles'].values():
        for item in profile['closure']:
            require(entries[item['path']]['sha256'] == item['sha256'], 'selected ELF hash mismatch')
    report = {'schema': 'paper28-build-successor-preflight-v1', 'decision': 'PREFLIGHT_PASS_NOT_EXECUTED',
              'bindings': bindings, 'sources': sources, 'capture_sources': capture_sources,
              'source_directory': str(SOURCE_DIR), 'capture_source_directory': str(CAPTURE_SOURCE_DIR),
              'capture_outputs': outputs,
              'audit_sha256': AUDIT_SHA, 'capture_outcome_sha256': OUTCOME_SHA,
              'ec_supplement': supplement,
              'archive_validation': archive_summary, 'permissions': capabilities(),
              'environment': ENV, 'limits': LIMITS, 'fresh_root': str(BUILD)}
    return report, entries, directories, loader


def parent_fd(root_fd, relative):
    """Every physical ancestor opened O_DIRECTORY|O_NOFOLLOW via dirfd."""
    parts = safe_relative(relative)
    current = os.dup(root_fd)
    try:
        for part in parts[:-1]:
            newer = os.open(part, DIR_FLAGS, dir_fd=current)
            os.close(current)
            current = newer
        return current, parts[-1]
    except BaseException:
        os.close(current)
        raise


def namespace_file(root_fd, relative, data, mode):
    parent, leaf = parent_fd(root_fd, relative)
    try:
        fd = os.open(leaf, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW |
                     os.O_CLOEXEC, mode, dir_fd=parent)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            os.fchmod(stream.fileno(), mode)
            os.fchown(stream.fileno(), 0, 0)
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        os.close(parent)


def materialize(root, entries, directories):
    root.mkdir(mode=0o700)
    root_fd = os.open(root, DIR_FLAGS)
    try:
        all_dirs = directories | {'/source', '/control', '/work', '/dev'} | {
            '/work/' + name for name in CACHES}
        for path in sorted(all_dirs, key=lambda p: (p.count('/'), p)):
            parent, leaf = parent_fd(root_fd, path[1:])
            try:
                os.mkdir(leaf, mode=0o700, dir_fd=parent)
            finally:
                os.close(parent)

        def consume(path, entry, data):
            if entry['kind'] == 'file':
                mode = 0o555 if int(entry['mode'], 8) & 0o111 else 0o444
                namespace_file(root_fd, path[1:], data, mode)
        archive_check(entries, consume)
        for name in SOURCE:
            namespace_file(root_fd, 'source/' + name, regular_read(SOURCE_DIR / name), 0o444)
        namespace_file(root_fd, 'control/PDF_ACCEPTANCE_SUCCESSOR_20260905.py',
                       regular_read(NOTES / 'PDF_ACCEPTANCE_SUCCESSOR_20260905.py'), 0o444)
        dev_fd = os.open('dev', DIR_FLAGS, dir_fd=root_fd)
        try:
            os.mknod('null', stat.S_IFCHR | 0o666, os.makedev(1, 3), dir_fd=dev_fd)
            os.chmod('null', 0o666, dir_fd=dev_fd, follow_symlinks=False)
        finally:
            os.close(dev_fd)
        # Links installed only after all regular-file writes are complete.
        for path, entry in sorted(entries.items()):
            if entry['kind'] == 'symlink':
                parent, leaf = parent_fd(root_fd, path[1:])
                try:
                    os.symlink(entry['target'], leaf, dir_fd=parent)
                finally:
                    os.close(parent)
        for path in sorted(all_dirs, key=lambda p: (-p.count('/'), p)):
            parent, leaf = parent_fd(root_fd, path[1:])
            try:
                fd = os.open(leaf, DIR_FLAGS, dir_fd=parent)
                try:
                    writable = path == '/work' or path.startswith('/work/')
                    os.fchown(fd, UID if writable else 0, GID if writable else 0)
                    os.fchmod(fd, 0o700 if writable else 0o555)
                finally:
                    os.close(fd)
            finally:
                os.close(parent)
        os.fchmod(root_fd, 0o555)
    finally:
        os.close(root_fd)
    source_binding(root / 'source')


def snapshot(root, skip_work=False):
    """lstat-style member/type/mode/owner/content snapshot; never follows links."""
    rows = {}

    def walk(fd, relative):
        current = os.fstat(fd)
        names = sorted(os.listdir(fd))
        rows[relative] = {'kind': 'dir', 'mode': oct(stat.S_IMODE(current.st_mode)),
                          'uid': current.st_uid, 'gid': current.st_gid, 'members': names}
        for name in names:
            child = relative + '/' + name if relative else name
            s = os.stat(name, dir_fd=fd, follow_symlinks=False)
            row = {'mode': oct(stat.S_IMODE(s.st_mode)), 'uid': s.st_uid, 'gid': s.st_gid}
            if stat.S_ISDIR(s.st_mode):
                if skip_work and child == 'work':
                    rows[child] = {**row, 'kind': 'dir', 'contents': 'SEPARATELY_SNAPSHOTTED'}
                else:
                    cfd = os.open(name, DIR_FLAGS, dir_fd=fd)
                    try:
                        walk(cfd, child)
                    finally:
                        os.close(cfd)
            elif stat.S_ISREG(s.st_mode):
                with os.fdopen(os.open(name, READ_FLAGS, dir_fd=fd), 'rb') as f:
                    h = hashlib.sha256()
                    size = 0
                    for data in iter(lambda: f.read(1024**2), b''):
                        h.update(data)
                        size += len(data)
                require(size == s.st_size, 'snapshot size mutation')
                rows[child] = {**row, 'kind': 'file', 'bytes': size, 'sha256': h.hexdigest()}
            elif stat.S_ISLNK(s.st_mode):
                rows[child] = {**row, 'kind': 'symlink', 'target': os.readlink(name, dir_fd=fd)}
            elif stat.S_ISCHR(s.st_mode) and child == 'dev/null':
                rows[child] = {**row, 'kind': 'char', 'major': os.major(s.st_rdev),
                               'minor': os.minor(s.st_rdev)}
            else:
                raise RuntimeError('unapproved output/member type: ' + child)
    fd = os.open(root, DIR_FLAGS)
    try:
        walk(fd, '')
    finally:
        os.close(fd)
    return rows


def verify_materialized(rows, entries, directories, validator_binding):
    expected = {''} | {p[1:] for p in entries} | {p[1:] for p in directories} | {
        'source', 'control', 'work', 'dev', 'dev/null', 'control/PDF_ACCEPTANCE_SUCCESSOR_20260905.py'} | {
        'source/' + name for name in SOURCE}
    require(set(rows) == expected, 'materialized namespace closure mismatch')
    for path, entry in entries.items():
        row = rows[path[1:]]
        require(row['kind'] == entry['kind'], 'materialized kind mismatch')
        if entry['kind'] == 'file':
            require((row['bytes'], row['sha256']) == (entry['size'], entry['sha256']),
                    'materialized content mismatch')
            require(row['mode'] == oct(0o555 if int(entry['mode'], 8) & 0o111 else 0o444),
                    'materialized file mode mismatch')
        elif entry['kind'] == 'symlink':
            require(row['target'] == entry['target'], 'materialized link mismatch')
    for path, row in rows.items():
        require((row['uid'], row['gid']) == ((UID, GID) if path == 'work' else (0, 0)),
                'materialized ownership mismatch')
        if row['kind'] == 'dir':
            require(row['mode'] == ('0o700' if path == 'work' else '0o555'), 'directory mode mismatch')
    require(rows['dev/null'] == {'kind': 'char', 'mode': '0o666', 'uid': 0, 'gid': 0,
                                'major': 1, 'minor': 3}, 'null device mismatch')
    control = rows['control/PDF_ACCEPTANCE_SUCCESSOR_20260905.py']
    require(control['sha256'] == validator_binding['sha256'] and control['mode'] == '0o444',
            'validator materialization mismatch')
    for name, (sha, size, _) in SOURCE.items():
        row = rows['source/' + name]
        require(row['sha256'] == sha and row['bytes'] == size and row['mode'] == '0o444',
                'source materialization mismatch')


def child_setup(root, expected_parent, original_signal_mask):
    os.chroot(root)
    os.chdir('/work')
    os.setgroups([])
    os.setgid(GID)
    os.setuid(UID)
    os.umask(0o077)
    require(os.getuid() == os.geteuid() == UID and os.getgid() == os.getegid() == GID
            and os.getgroups() == [], 'child identity drop failed')
    header = CapHeader(0x20080522, 0)
    capability_data = (CapData * 2)()
    if LIBC.capset(ctypes.byref(header), capability_data) != 0:
        raise OSError(ctypes.get_errno(), 'clear child capabilities failed')
    if LIBC.capget(ctypes.byref(header), capability_data) != 0:
        raise OSError(ctypes.get_errno(), 'verify child capabilities failed')
    require(all(not (item.effective | item.permitted | item.inheritable)
                for item in capability_data), 'nonzero child capabilities')
    if LIBC.prctl(38, 1, 0, 0, 0) != 0:
        raise OSError(ctypes.get_errno(), 'PR_SET_NO_NEW_PRIVS failed')
    require(LIBC.prctl(39, 0, 0, 0, 0) == 1, 'no-new-privileges verification failed')
    # Set after UID change (which clears this setting); close the orphan window
    # by checking the parent identity after installing the death signal.
    if LIBC.prctl(1, signal.SIGKILL, 0, 0, 0) != 0:
        raise OSError(ctypes.get_errno(), 'PR_SET_PDEATHSIG failed')
    require(os.getppid() == expected_parent, 'parent exited before child ownership')
    for kind, value in ((resource.RLIMIT_CPU, LIMITS['cpu_seconds']),
                        (resource.RLIMIT_FSIZE, LIMITS['file_bytes']),
                        (resource.RLIMIT_AS, LIMITS['address_space_bytes']),
                        (resource.RLIMIT_NOFILE, LIMITS['open_files']),
                        (resource.RLIMIT_CORE, 0)):
        resource.setrlimit(kind, (value, value))
    signal.pthread_sigmask(signal.SIG_SETMASK, original_signal_mask)


def loader_argv(loader, role, args):
    selected = loader['roles'][role]
    profile = loader['profiles'][selected['profile']]
    return [loader['loader']['path'], '--inhibit-cache', '--glibc-hwcaps-mask', '',
            '--library-path', profile['library_path'], '--argv0', selected['argv0'],
            selected['executable'], *args]


def execute_child(root, evidence, stage, role, args, loader):
    before = source_binding(SOURCE_DIR)
    capture_before = source_binding(CAPTURE_SOURCE_DIR, CAPTURE_SOURCES)
    require(source_binding(root / 'source') == before, 'isolated source before command')
    dest = evidence / (root.name + '-' + stage)
    dest.mkdir(mode=0o700)
    argv = loader_argv(loader, role, args)
    json_new(dest / 'intent.json', {'argv': argv, 'environment': ENV, 'cwd': '/work',
        'root': str(root), 'uid': UID, 'gid': GID, 'groups': [], 'no_new_privileges': True,
        'limits': LIMITS, 'sources': before, 'capture_sources': capture_before})
    started = time.monotonic()
    status = {'stage': stage, 'role': role, 'returncode': None, 'timeout': False,
              'spawned': False, 'reaped': False}
    proc = None
    try:
        with (dest / 'stdout.txt').open('xb') as stdout, (dest / 'stderr.txt').open('xb') as stderr:
            expected_parent = os.getpid()
            original_signal_mask = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGINT})
            try:
                # A real SIGINT is deferred until the handle is assigned;
                # the child restores the original mask before executing.
                proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                    env=ENV, close_fds=True, start_new_session=True,
                    preexec_fn=lambda: child_setup(str(root), expected_parent, original_signal_mask))
                status['spawned'] = True
                status['pid'] = proc.pid
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK, original_signal_mask)
            try:
                status['returncode'] = proc.wait(timeout=LIMITS['wall_seconds'])
            except subprocess.TimeoutExpired:
                status['timeout'] = True
    except BaseException as exc:
        status['exception'] = {'type': type(exc).__name__, 'message': str(exc)}
    finally:
        if proc is not None:
            try:
                if proc.poll() is None:
                    try:
                        os.killpg(proc.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    status['killed_for_cleanup'] = True
                status['returncode'] = proc.wait()
                status['reaped'] = True
            except BaseException as cleanup_error:
                status['cleanup_error'] = {'type': type(cleanup_error).__name__,
                                           'message': str(cleanup_error)}
    status['elapsed_seconds'] = time.monotonic() - started
    # Status persists even if post-command source/output verification fails.
    json_new(dest / 'status.json', status)
    work = snapshot(root / 'work')
    json_new(dest / 'work-manifest.json', work)
    for name in FINAL_FILES:
        if name in work and work[name]['kind'] == 'file':
            write_new(dest / name, regular_read(root / 'work' / name))
    require(source_binding(SOURCE_DIR) == before and
            source_binding(root / 'source') == before, 'source changed during command')
    require(source_binding(CAPTURE_SOURCE_DIR, CAPTURE_SOURCES) == capture_before,
            'original capture source changed during command')
    require(status['returncode'] == 0 and status['reaped'] and not status['timeout']
            and 'exception' not in status and 'cleanup_error' not in status,
            'child failed at ' + root.name + '/' + stage)
    return work


def final_logs(root, evidence):
    log = regular_read(root / 'work/main.log').decode('utf-8', errors='replace')
    blg = regular_read(root / 'work/main.blg').decode('utf-8', errors='replace')
    bad = re.findall(r'(?im)^.*(?:undefined|multiply[- ]defined|multiply defined|'
                     r'duplicate (?:label|destination)|destination with the same identifier|'
                     r'\bRerun (?:to|LaTeX|BibTeX)|\bPlease (?:re)?run|'
                     r'Overfull|^!|LaTeX Error|Package \S+ Error).*$' , log)
    bib_bad = re.findall(r'(?im)^.*(?:Warning--|error message|I couldn.t open|I found no|'
                         r'Illegal|You.re missing).*$' , blg)
    report = {'fatal_log_lines': bad, 'fatal_bibtex_lines': bib_bad,
              'underfull_lines_pending_visual_disposition': re.findall(r'(?m)^.*Underfull.*$', log)}
    json_new(evidence / (root.name + '-final-log-check.json'), report)
    require(not bad and not bib_bad, 'final log/BibTeX readiness failed')


def run(review_sha):
    report, entries, directories, loader = preflight()
    review_data = regular_read(REVIEW)
    require(digest(review_data) == review_sha, 'independent review hash mismatch')
    review = json.loads(review_data)
    require(review.get('decision') == 'EXECUTABLE_PROFILE_REVIEW_PASS', 'review is not PASS')
    require(review.get('bindings') == report['bindings'] and review.get('sources') == report['sources']
            and review.get('capture_sources') == report['capture_sources']
            and review.get('audit_sha256') == AUDIT_SHA
            and review.get('capture_outcome_sha256') == OUTCOME_SHA
            and review.get('ec_supplement') == report['ec_supplement'], 'review binding mismatch')
    report['review_sha256'] = review_sha
    # First and sole execution namespace access: exclusive creation, never probe/reuse.
    BUILD.mkdir(mode=0o700)
    evidence = BUILD / 'evidence'
    stage = 'evidence-open'
    readonly = {}
    results = {}
    try:
        evidence.mkdir(mode=0o700)
        json_new(evidence / 'opening-contract.json', report)
        write_new(evidence / 'independent-review.json', review_data)
        for name in CONTROL_NAMES:
            data = regular_read(NOTES / name)
            require(digest(data) == report['bindings'][name]['sha256'], 'control changed before copy')
            write_new(evidence / name, data)
        for name in ('r0', 'r1'):
            root = BUILD / name
            stage = name + '/materialize'
            materialize(root, entries, directories)
            readonly[name] = snapshot(root, skip_work=True)
            verify_materialized(readonly[name], entries, directories,
                                report['bindings']['PDF_ACCEPTANCE_SUCCESSOR_20260905.py'])
            json_new(evidence / (name + '-inputs-before.json'), readonly[name])
            initial_work = snapshot(root / 'work')
            require(set(initial_work) == {''} | set(CACHES) and
                    all(row['kind'] == 'dir' and (key == '' or row['members'] == [])
                        for key, row in initial_work.items()), 'nonempty initial work/cache')
            json_new(evidence / (name + '-work-before.json'), initial_work)
            third = None
            for command, role, args in COMMANDS:
                stage = name + '/' + command
                if command == '09-validator':
                    (root / 'work/report').mkdir(mode=0o700)
                    os.chown(root / 'work/report', UID, GID)
                work = execute_child(root, evidence, command, role, args, loader)
                if command == '03-latex':
                    third = work
                if command == '04-latex':
                    final_logs(root, evidence)
                    require(all(work.get('main.' + ext) == third.get('main.' + ext)
                                and work.get('main.' + ext) is not None for ext in ('aux', 'out', 'bbl')),
                            'auxiliary convergence failed after fixed passes')
            stage = name + '/final-bindings'
            after = snapshot(root, skip_work=True)
            json_new(evidence / (name + '-inputs-after.json'), after)
            require(after == readonly[name], 'readonly namespace changed')
            source_binding(SOURCE_DIR)
            source_binding(CAPTURE_SOURCE_DIR, CAPTURE_SOURCES)
            source_binding(root / 'source')
            final_work = snapshot(root / 'work')
            json_new(evidence / (name + '-work-final.json'), final_work)
            acceptance = json.loads(regular_read(root / 'work/report/acceptance.json'))
            require(acceptance['automated_status'] == 'PASS', 'validator acceptance not PASS')
            require(all(file in final_work for file in FINAL_FILES), 'final output missing')
            results[name] = final_work
        stage = 'cross-root-identity'
        differences = [name for name in sorted(set(results['r0']) | set(results['r1']))
                       if results['r0'].get(name) != results['r1'].get(name)]
        json_new(evidence / 'cross-root.json', {'raw_work_snapshot_equal': not differences,
                 'differences': differences, 'required_final_files': FINAL_FILES,
                 'predicate': 'members/type/mode/uid/gid/regular-byte-sha256; no time/inode/dir-size'})
        require(not differences, 'cross-root raw output identity failed')
        stage = 'closing-contract'
        closing, _, _, _ = preflight()
        require(closing['bindings'] == report['bindings'] and
                closing['sources'] == report['sources'] and
                closing['capture_sources'] == report['capture_sources'] and
                closing['capture_outputs'] == report['capture_outputs'] and
                closing['ec_supplement'] == report['ec_supplement'], 'closing binding mismatch')
        json_new(evidence / 'closing-contract.json', closing)
        sealed = snapshot(evidence)
        json_new(evidence / 'outcome.json', {'decision': 'AUTOMATED_TWO_ROOT_PASS_VISUAL_REVIEW_PENDING',
                 'stage': stage, 'no_retry': True, 'source_unchanged': True,
                 'capture_sources_unchanged': True,
                 'main_pdf': results['r0']['main.pdf'], 'sealed_evidence': sealed,
                 'local_acceptance': 'NOT_GRANTED_BY_CONTROLLER'})
        print(json.dumps({'decision': 'AUTOMATED_TWO_ROOT_PASS_VISUAL_REVIEW_PENDING',
                          'root': str(BUILD), 'pdf': results['r0']['main.pdf']}), flush=True)
        return 0
    except BaseException as exc:
        failure = {'decision': 'BUILD_FAILED_PRESERVED_NO_RETRY', 'stage': stage,
                   'exception_type': type(exc).__name__, 'error': str(exc),
                   'completed_roots': list(results), 'root': str(BUILD)}
        try:
            failure['source_after'] = source_binding(SOURCE_DIR)
        except Exception as source_error:
            failure['source_check_error'] = str(source_error)
        try:
            failure['capture_source_after'] = source_binding(CAPTURE_SOURCE_DIR, CAPTURE_SOURCES)
        except Exception as capture_source_error:
            failure['capture_source_check_error'] = str(capture_source_error)
        try:
            failure['ec_supplement_after'] = supplement_binding(report['capture_sources'])
            failure['ec_supplement_unchanged'] = (
                failure['ec_supplement_after'] == report['ec_supplement'])
        except Exception as supplement_error:
            failure['ec_supplement_check_error'] = str(supplement_error)
        for name in readonly:
            try:
                rows = snapshot(BUILD / name, skip_work=True)
                json_new(evidence / (name + '-failure-inputs.json'), rows)
                failure[name + '_readonly_unchanged'] = rows == readonly[name]
            except Exception as check_error:
                failure[name + '_input_check_error'] = str(check_error)
        # If evidence opening itself failed, preserve a root-level failure record.
        failure_path = (evidence if evidence.is_dir() else BUILD) / 'failure.json'
        try:
            failure['sealed_evidence'] = snapshot(evidence)
        except Exception as seal_error:
            failure['evidence_seal_error'] = {'type': type(seal_error).__name__,
                                               'message': str(seal_error)}
        json_new(failure_path, failure)
        print(json.dumps(failure, sort_keys=True), flush=True)
        return 1


def self_test():
    for bad in ('', '/etc/x', '../x', 'a/../b', 'a//b', './a', 'a/./b'):
        try:
            safe_relative(bad)
        except RuntimeError:
            pass
        else:
            raise AssertionError('unsafe member accepted')
    assert safe_relative('usr/lib/example') == ('usr', 'lib', 'example')
    assert 'HOME' not in ENV and 'CODEX_HOME' not in ENV
    assert [role for _, role, _ in COMMANDS[:4]] == ['pdftex', 'bibtex', 'pdftex', 'pdftex']
    assert all(not key.startswith('LD_') for key in ENV)
    assert ENV['TEXINPUTS'].split(':')[:2] == ['/source', '/work']
    assert all(not part.endswith(':') for part in ENV.values())
    assert '-no-shell-escape' in TEX_ARGS and TEX_ARGS[-1].endswith(r'\input{main.tex}')
    assert not any('extractall' in str(item) for item in COMMANDS)
    fixture = {'/fixture/item' + str(i): {'kind': 'file'} for i in range(6838)}
    original = dict(fixture)
    extended, directories = extend_inventory(fixture, {'/fixture'})
    assert fixture == original and len(extended) == 6839
    assert extended[SUPPLEMENT_TARGET] == supplemental_entry()
    assert str(PurePosixPath(SUPPLEMENT_TARGET).parent) in directories
    for bad_path in (SUPPLEMENT_TARGET, '/usr/share/texlive'):
        collision = dict(fixture)
        collision.pop('/fixture/item0')
        collision[bad_path] = {'kind': 'symlink', 'target': '/unapproved'}
        try:
            extend_inventory(collision, {'/fixture'})
        except RuntimeError:
            pass
        else:
            raise AssertionError('supplement collision accepted')
    assert CAPTURE_SOURCE_DIR == PROJECT / 'paper' and SOURCE_DIR != CAPTURE_SOURCE_DIR
    assert all(SOURCE[name] == CAPTURE_SOURCES[name]
               for name in ('math_commands.tex', 'references.bib'))
    assert CAPTURE_SOURCES['main.tex'] == (
        'bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e', 73733, 1605)
    assert COMMANDS[-1][2][3] == '/control/PDF_ACCEPTANCE_SUCCESSOR_20260905.py'
    source_fixtures = {Path('/fixture/original/main.tex'): b'original\n',
                       Path('/fixture/successor/main.tex'): b'successor\n'}
    original_pins = {'main.tex': (digest(b'original\n'), 9, 1)}
    successor_pins = {'main.tex': (digest(b'successor\n'), 10, 1)}
    previous_reader = globals()['regular_read']
    globals()['regular_read'] = lambda path: source_fixtures[path]
    try:
        old_binding = source_binding(Path('/fixture/original'), original_pins)
        new_binding = source_binding(Path('/fixture/successor'), successor_pins)
        assert old_binding != new_binding
        try:
            source_binding(Path('/fixture/successor'), original_pins)
        except RuntimeError:
            pass
        else:
            raise AssertionError('new source accepted as historical capture source')
    finally:
        globals()['regular_read'] = previous_reader
    print(json.dumps({'self_test': 'PASS', 'filesystem_writes': 0, 'child_invocations': 0,
                      'supplement_inventory': 'one file; duplicate/symlink ancestors rejected',
                      'source_roles': 'distinct; historical/new source mismatch rejected'}))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--self-test', action='store_true')
    action.add_argument('--preflight', action='store_true')
    action.add_argument('--execute', action='store_true')
    parser.add_argument('--review-sha256')
    args = parser.parse_args()
    if args.self_test:
        require(args.review_sha256 is None, 'review argument only for execution')
        return self_test()
    if args.preflight:
        require(args.review_sha256 is None, 'review argument only for execution')
        report, _, _, _ = preflight()
        print(json.dumps(report, sort_keys=True, indent=2))
        return 0
    require(args.review_sha256 is not None and re.fullmatch('[0-9a-f]{64}', args.review_sha256),
            'exact review SHA256 required')
    return run(args.review_sha256)


if __name__ == '__main__':
    raise SystemExit(main())
