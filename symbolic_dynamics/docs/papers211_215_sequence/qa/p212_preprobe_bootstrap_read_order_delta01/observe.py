"""SOURCE ONLY. Ordinary-trusted observer, NOT an author probe or self-attester.

Its own interpreter/import/ctypes bootstrap is explicitly assumed, not keyed
retroactively. A future separate root grant is required before target reads.
This program never imports/evaluates the author sources, starts a child,
reads /proc, changes settings, writes target files, or grants a later phase.
"""
import ctypes
from hashlib import sha256
import json
import os
import stat
import sys

ROOT = '/root/autodl-tmp/symbolic_dynamics'
QA = ROOT + '/docs/papers211_215_sequence/qa'
HERE = QA + '/p212_preprobe_bootstrap_preparation01'
FRONTIER = HERE + '/FRONTIER.json'
SOURCE_RECEIPT = QA + '/p212_preprobe_bootstrap_source_root01/RECEPTION.md'
TRUST_RECEIPT = QA + '/p212_trusted_product_boundary_root01/RECEPTION.md'
PROVENANCE = {
    'schema': 'p212-trusted-product-boundary-v1',
    'assumption': 'ordinary_product_observer_bash_env_bootstrap',
    'product_startup_attested': False,
    'claim': 'finite_received_keys_and_discrete_downstream_observations',
}
FIELDS = ('dev', 'ino', 'mode', 'nlink', 'uid', 'gid', 'rdev', 'size',
          'blksize', 'blocks', 'atimeNs', 'mtimeNs', 'ctimeNs', 'birthtimeNs')
IDENTITY = ('dev', 'ino', 'mode', 'uid', 'gid', 'rdev', 'birthtimeNs')
MAX_TARGETS = 384
MAX_COMPONENTS = 768
MAX_NATIVE_CALLS = 60000
MAX_ALL_READ_BYTES = 536870912
MAX_CAPTURE_BYTES = 8388608
MAX_OUTPUT_BYTES = 134217728
CHUNK = 65536
NATIVE_EVENTS = []
PATH_EVENTS = []
READ_BYTES = 0
CAPTURE_BYTES = 0
LIBC = None


class Hold(Exception):
    pass


def need(condition, message):
    if not condition:
        raise Hold(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=True, indent=2, allow_nan=False) + '\n'


def load_canonical(raw):
    value = json.loads(raw)
    need(canonical(value).encode('ascii') == raw, 'noncanonical JSON/duplicates')
    return value


def physical_spelling(path):
    return (type(path) is str and path.startswith('/') and len(os.fsencode(path)) <= 4096
            and '\x00' not in path and os.path.normpath(path) == path
            and not path.startswith('//'))


def components(path):
    need(physical_spelling(path), 'noncanonical absolute spelling')
    parts, current = ['/'], ''
    for name in path.split('/')[1:]:
        if name:
            current += '/' + name
            parts.append(current)
    return parts


class Stamp(ctypes.Structure):
    _fields_ = [('seconds', ctypes.c_int64), ('nanoseconds', ctypes.c_uint32),
                ('reserved', ctypes.c_int32)]


class Statx(ctypes.Structure):
    _fields_ = [
        ('mask', ctypes.c_uint32), ('blksize', ctypes.c_uint32),
        ('attributes', ctypes.c_uint64), ('nlink', ctypes.c_uint32),
        ('uid', ctypes.c_uint32), ('gid', ctypes.c_uint32),
        ('mode', ctypes.c_uint16), ('spare0', ctypes.c_uint16),
        ('ino', ctypes.c_uint64), ('size', ctypes.c_uint64),
        ('blocks', ctypes.c_uint64), ('attributes_mask', ctypes.c_uint64),
        ('atime', Stamp), ('btime', Stamp), ('ctime', Stamp), ('mtime', Stamp),
        ('rdev_major', ctypes.c_uint32), ('rdev_minor', ctypes.c_uint32),
        ('dev_major', ctypes.c_uint32), ('dev_minor', ctypes.c_uint32),
        ('uninterpreted_tail', ctypes.c_ubyte * 112),
    ]


def initialize_native():
    global LIBC
    need(sys.platform == 'linux' and sys.byteorder == 'little', 'HOLD native platform')
    need((ctypes.sizeof(ctypes.c_int), ctypes.sizeof(ctypes.c_long),
          ctypes.sizeof(ctypes.c_void_p), ctypes.sizeof(Stamp), ctypes.sizeof(Statx))
         == (4, 8, 8, 16, 256), 'HOLD Linux little-endian LP64/layout')
    expected = {'mask': 0, 'blksize': 4, 'nlink': 16, 'uid': 20, 'gid': 24,
                'mode': 28, 'ino': 32, 'size': 40, 'blocks': 48,
                'atime': 64, 'btime': 80, 'ctime': 96, 'mtime': 112,
                'rdev_major': 128, 'rdev_minor': 132,
                'dev_major': 136, 'dev_minor': 140, 'uninterpreted_tail': 144}
    need(all(getattr(Statx, name).offset == offset for name, offset in expected.items()),
         'HOLD independent Structure offsets')
    need(Stamp.nanoseconds.offset == 8, 'HOLD timestamp layout')
    LIBC = ctypes.CDLL(None, use_errno=True)
    LIBC.statx.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int,
                          ctypes.c_uint, ctypes.POINTER(Statx)]
    LIBC.statx.restype = ctypes.c_int


def native(path, *, fd=None, follow=False):
    need(len(NATIVE_EVENTS) < MAX_NATIVE_CALLS, 'native-call ceiling')
    data = Statx()
    flags = 0x800 | (0x1000 if fd is not None else (0 if follow else 0x100))
    raw_path, dirfd = (b'', fd) if fd is not None else (os.fsencode(path), -100)
    ctypes.set_errno(0)
    rc = LIBC.statx(dirfd, raw_path, flags, 0xFFF, ctypes.byref(data))
    event = {'path': path, 'handle': fd, 'flags': flags, 'requested_mask': 0xFFF,
             'return': rc, 'errno': ctypes.get_errno(),
             'mask': int(data.mask) if rc == 0 else None,
             'raw_statx_hex': ctypes.string_at(ctypes.byref(data), 256).hex()}
    NATIVE_EVENTS.append(event)
    if rc != 0:
        need(rc == -1 and event['errno'] in (2, 20), 'statx error; original retained')
        event['status'] = 'ABSENCE_ERRNO_ONLY_NO_DECODED_FIELDS'
        return None
    need(data.mask & 0xFFF == 0xFFF, 'HOLD missing basic/birthtime mask; raw retained')

    def ns(stamp):
        need(stamp.nanoseconds < 1000000000, 'HOLD native nanoseconds range')
        return stamp.seconds * 1000000000 + stamp.nanoseconds

    values = (os.makedev(data.dev_major, data.dev_minor), data.ino, data.mode,
              data.nlink, data.uid, data.gid,
              os.makedev(data.rdev_major, data.rdev_minor), data.size,
              data.blksize, data.blocks, ns(data.atime), ns(data.mtime),
              ns(data.ctime), ns(data.btime))
    key = dict(zip(FIELDS, map(str, values)))
    event.update({'mask': data.mask, 'fields': key, 'status': 'ACTUAL_MASKED_FIELDS'})
    return key


def stable(a, b, *, ancestor=False):
    names = IDENTITY if ancestor else tuple(k for k in FIELDS if k != 'atimeNs')
    need(a is not None and b is not None and all(a[k] == b[k] for k in names),
         'changed native key')


def resolve(path, allowed):
    queue = path.split('/')[1:] if path != '/' else []
    current, chain, links, steps = '/', [], 0, 0
    lexical_lstat = None
    root = native('/')
    need(root is not None and stat.S_ISDIR(int(root['mode'])), 'physical root directory')
    chain.append({'path': '/', 'lstat': root, 'link': None})
    while queue:
        steps += 1
        need(steps <= 1024, 'component-step ceiling')
        name = queue.pop(0)
        candidate = current.rstrip('/') + '/' + name
        need(candidate in allowed, 'unapproved component; not read: ' + candidate)
        key = native(candidate)
        row = {'path': candidate, 'lstat': key, 'link': None}
        chain.append(row)
        if key is None:
            return {'path': path, 'resolved': None, 'absent_at': candidate, 'chain': chain}
        if not queue and lexical_lstat is None:
            lexical_lstat = key
        if stat.S_ISLNK(int(key['mode'])):
            links += 1
            need(links <= 40 and int(key['size']) <= 4096, 'link count/byte ceiling')
            link = os.readlink(candidate)
            row['link'] = link
            PATH_EVENTS.append({'operation': 'readlink', 'path': candidate, 'text': link})
            need(len(os.fsencode(link)) <= 4096, 'link byte ceiling')
            stable(key, native(candidate))
            need(link and all(x not in ('.', '..', '') for x in link.lstrip('/').split('/')),
                 'dot/empty link component requires an explicit mechanism delta')
            target = link if link.startswith('/') else current.rstrip('/') + '/' + link
            need(physical_spelling(target), 'noncanonical link target')
            need(all(p in allowed for p in components(target)),
                 'unapproved link target; link text retained, referent not read: ' + target)
            queue = target.split('/')[1:] + queue
            current = '/'
            continue
        current = candidate
        if queue and not stat.S_ISDIR(int(key['mode'])):
            full = current + '/' + '/'.join(queue)
            need(full in allowed, 'unapproved blocked leaf')
            need(native(full) is None and NATIVE_EVENTS[-1]['errno'] == 20,
                 'actual ENOTDIR required after observed non-directory component')
            return {'path': path, 'resolved': None, 'absent_at': full, 'chain': chain}
    leaf = chain[-1]['lstat']
    followed = native(current, follow=True)
    stable(leaf, followed)
    return {'path': path, 'resolved': current, 'absent_at': None,
            'chain': chain, 'lstat': lexical_lstat or leaf, 'stat': followed}


def compare_resolution(a, b):
    need((a['path'], a['resolved'], a['absent_at']) ==
         (b['path'], b['resolved'], b['absent_at']), 'changed resolution/absence')
    need(len(a['chain']) == len(b['chain']), 'changed chain length')
    for x, y in zip(a['chain'], b['chain']):
        need((x['path'], x['link']) == (y['path'], y['link']), 'changed alias chain')
        if x['lstat'] is None or y['lstat'] is None:
            need(x['lstat'] is y['lstat'], 'changed missing component')
        else:
            stable(x['lstat'], y['lstat'], ancestor=(x['path'] != a['resolved']
                   and stat.S_ISDIR(int(x['lstat']['mode']))))


def whole_file(path, limit, capture, expected):
    global READ_BYTES, CAPTURE_BYTES
    need(type(limit) is int and 0 <= limit <= 134217728, 'file byte ceiling')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        before = native(path, fd=fd)
        need(before is not None and stat.S_ISREG(int(before['mode']))
             and int(before['size']) <= limit, 'bounded regular handle only')
        stable(expected, before)
        digest, chunks, size = sha256(), [], 0
        while True:
            remaining = min(limit - size, MAX_ALL_READ_BYTES - READ_BYTES)
            need(remaining >= 0, 'total read byte ceiling')
            chunk = os.read(fd, min(CHUNK, remaining + 1))
            if not chunk:
                break
            size += len(chunk)
            READ_BYTES += len(chunk)
            need(size <= limit and READ_BYTES <= MAX_ALL_READ_BYTES,
                 'growth/total read ceiling; one sentinel byte may be read')
            digest.update(chunk)
            if capture:
                CAPTURE_BYTES += len(chunk)
                need(size <= 1048576 and CAPTURE_BYTES <= MAX_CAPTURE_BYTES,
                     'source/config raw-capture ceiling')
                chunks.append(chunk)
        after = native(path, fd=fd)
        stable(before, after)
        need(size == int(before['size']), 'complete handle byte count')
        return {'bytes': size, 'sha256': digest.hexdigest(), 'before': before,
                'after': after, 'raw_hex': b''.join(chunks).hex() if capture else None}
    finally:
        os.close(fd)


def observe_target(target, allowed):
    path, mode = target['path'], target['mode']
    before = resolve(path, allowed)
    row = {'target': target, 'before': before, 'content': None, 'members': None}
    if before['resolved'] is None:
        need(mode in ('absent', 'optional_file', 'optional_directory'),
             'required target absent: ' + path)
    else:
        need(mode != 'absent', 'required absence is present: ' + path)
        kind = int(before['stat']['mode'])
        if path == '/dev/null':
            need(stat.S_ISCHR(kind), 'metadata-only /dev/null must be a character device')
        if mode in ('file', 'optional_file'):
            need(stat.S_ISREG(kind), 'file target must be regular before open')
            row['content'] = whole_file(before['resolved'], target['max_bytes'], target['capture_hex'], before['stat'])
            stable(before['stat'], row['content']['before'])
        elif mode in ('directory', 'optional_directory', 'membership'):
            need(stat.S_ISDIR(kind), 'directory required')
            if mode == 'membership':
                names = []
                with os.scandir(before['resolved']) as directory:
                    for entry in directory:
                        name = entry.name
                        need(len(os.fsencode(name)) <= 255, 'member-name byte ceiling')
                        names.append(name)
                        PATH_EVENTS.append({'operation': 'membership_name', 'directory': path,
                                            'name': name, 'ordinal': len(names)})
                        need(len(names) <= target['max_members'], 'member ceiling plus one sentinel')
                row['members'] = sorted(names)
                need(row['members'] == target['expected_names'], 'changed finite membership')
        else:
            need(mode == 'metadata', 'unknown mode')
    after = resolve(path, allowed)
    compare_resolution(before, after)
    row['after'] = after
    return row


def control(path, pin):
    need(type(pin) is dict and set(pin) == {'bytes', 'sha256'}
         and type(pin['bytes']) is int and 0 <= pin['bytes'] <= 1048576
         and type(pin['sha256']) is str and len(pin['sha256']) == 64
         and set(pin['sha256']) <= set('0123456789abcdef'), 'control pin shape')
    allowed = set(components(path))
    target = {'path': path, 'mode': 'file', 'max_bytes': pin['bytes'], 'capture_hex': True}
    result = observe_target(target, allowed)
    need(result['before']['resolved'] == path, 'control is physical, no alias')
    need({k: result['content'][k] for k in ('bytes', 'sha256')} == pin, 'whole control pin')
    return result


def validate_frontier(frontier):
    need(set(frontier) == {'schema', 'status', 'author_probe_execution_allowed',
                           'targets', 'allowed_components', 'closure_gaps'}, 'frontier keys')
    need(frontier['schema'] == 'p212-finite-preprobe-frontier-v1'
         and frontier['status'] == 'SOURCE_ONLY_INITIAL_FRONTIER_NOT_CLOSURE'
         and frontier['author_probe_execution_allowed'] is False, 'frontier is not a grant')
    targets, allowed = frontier['targets'], frontier['allowed_components']
    need(type(targets) is list and 0 < len(targets) <= MAX_TARGETS, 'target ceiling')
    need(type(allowed) is list and allowed == sorted(set(allowed))
         and len(allowed) <= MAX_COMPONENTS and all(physical_spelling(p) for p in allowed),
         'literal component ceiling/order')
    need(all(p in allowed for path in allowed for p in components(path)), 'ancestor closure')
    need([t['path'] for t in targets] == sorted({t['path'] for t in targets}), 'target order/unique')
    for target in targets:
        need(set(target) == {'path', 'mode', 'role', 'origin', 'max_bytes',
                             'capture_hex', 'max_members', 'expected_names'}, 'target keys')
        need(target['path'] in allowed and type(target['role']) is str
             and type(target['origin']) is str, 'target spelling/role')
        mode = target['mode']
        need(mode in ('file', 'optional_file', 'directory', 'optional_directory',
                      'membership', 'absent', 'metadata'), 'target mode')
        need(type(target['capture_hex']) is bool and type(target['max_bytes']) is int
             and 0 <= target['max_bytes'] <= 134217728, 'target byte shape')
        need(type(target['max_members']) is int and 0 <= target['max_members'] <= 320,
             'member maximum')
        if mode == 'membership':
            names = target['expected_names']
            need(type(names) is list and names == sorted(set(names))
                 and len(names) <= target['max_members']
                 and all(type(n) is str and n not in ('', '.', '..') and '/' not in n
                         and '\x00' not in n and len(os.fsencode(n)) <= 255 for n in names),
                 'literal one-level membership')
        else:
            need(target['max_members'] == 0 and target['expected_names'] is None, 'no hidden enumeration')
        if mode not in ('file', 'optional_file'):
            need(target['max_bytes'] == 0 and target['capture_hex'] is False, 'metadata has no byte read')
    need(type(frontier['closure_gaps']) is list and frontier['closure_gaps'], 'unclosed frontier retained')
    return targets, set(allowed)


def main():
    result = {'schema': 'p212-independent-preprobe-observation-v1',
              'status': 'HOLD_BEFORE_TARGET_READS', 'provenance': PROVENANCE,
              'observer_bootstrap_attested': False, 'author_probe_executed': False,
              'closure_certified': False, 'controls': [], 'closing_controls': [],
              'passes': [], 'errors': []}
    try:
        need(len(sys.argv) == 2 and len(sys.argv[1].encode('utf-8')) <= 32768,
             'one finite external canonical authorization required')
        authorization = load_canonical(sys.argv[1].encode('utf-8'))
        need(set(authorization) == {'schema', 'enabled', 'status', 'provenance',
                                    'source_receipt', 'trust_receipt', 'frontier'}, 'grant keys')
        need(authorization['schema'] == 'p212-independent-preprobe-observer-authorization-v1'
             and authorization['enabled'] is True
             and authorization['status'] == 'ROOT_BOUND_FINITE_OBSERVATION_ONLY', 'disabled/unreceived grant')
        need(authorization['provenance'] == PROVENANCE
             and authorization['provenance']['product_startup_attested'] is False, 'fixed explicit trust')
        # This is the observer's ordinary-trusted native initialization, not an author import.
        initialize_native()
        for role, path in (('source_receipt', SOURCE_RECEIPT), ('trust_receipt', TRUST_RECEIPT),
                           ('frontier', FRONTIER)):
            ref = authorization[role]
            need(type(ref) is dict and set(ref) == {'path', 'pin'} and ref['path'] == path,
                 'fixed control role/path')
            result['controls'].append({'role': role, 'observation': control(path, ref['pin'])})
        raw_frontier = bytes.fromhex(result['controls'][-1]['observation']['content']['raw_hex'])
        frontier = load_canonical(raw_frontier)
        targets, allowed = validate_frontier(frontier)
        result['closure_gaps'] = frontier['closure_gaps']
        for pass_number in (1, 2):
            rows = []
            result['passes'].append({'number': pass_number, 'targets': rows})
            for target in targets:
                start_event = len(NATIVE_EVENTS)
                try:
                    row = observe_target(target, allowed)
                    row['status'] = 'OBSERVED'
                except Exception as error:
                    row = {'target': target, 'status': 'HOLD', 'error_type': type(error).__name__,
                           'error_message': str(error), 'first_event': start_event}
                    result['errors'].append({'pass': pass_number, **row})
                rows.append(row)
                if result['errors']:
                    break
            if result['errors']:
                break
        comparisons = (zip(result['passes'][0]['targets'], result['passes'][1]['targets'])
                       if len(result['passes']) == 2 else ())
        for first, second in comparisons:
            if first['status'] == second['status'] == 'OBSERVED':
                compare_resolution(first['before'], second['after'])
                need(first['members'] == second['members'], 'changed membership between passes')
                if first['content'] is not None:
                    need({k: first['content'][k] for k in ('bytes', 'sha256')} ==
                         {k: second['content'][k] for k in ('bytes', 'sha256')}, 'changed complete bytes')
        if not result['errors']:
            for role, path in (('source_receipt', SOURCE_RECEIPT), ('trust_receipt', TRUST_RECEIPT),
                               ('frontier', FRONTIER)):
                closing = control(path, authorization[role]['pin'])
                opening = next(row['observation'] for row in result['controls'] if row['role'] == role)
                compare_resolution(opening['before'], closing['after'])
                result['closing_controls'].append({'role': role, 'observation': closing})
        result['status'] = ('HOLD_FINITE_OBSERVATION_ERRORS' if result['errors'] else
                            'FINITE_OBSERVATION_ONLY_ROOT_RECEPTION_AND_CLOSURE_PENDING')
    except Exception as error:
        result['errors'].append({'error_type': type(error).__name__, 'error_message': str(error)})
        result['status'] = 'HOLD_FINITE_OBSERVER'
    result.update({'native_events': NATIVE_EVENTS, 'path_events': PATH_EVENTS,
                   'actual_read_bytes': READ_BYTES,
                   'actual_captured_bytes': CAPTURE_BYTES})
    raw = canonical(result).encode('ascii')
    # A ceiling violation is a failed/incomplete capture, never a sealed truncated success.
    need(len(raw) <= MAX_OUTPUT_BYTES, 'HOLD output ceiling; no success record emitted')
    sys.stdout.buffer.write(raw)
    sys.stdout.buffer.flush()
    return 78 if result['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
