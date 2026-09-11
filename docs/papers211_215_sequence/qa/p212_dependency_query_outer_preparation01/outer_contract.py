"""SOURCE ONLY: one P212 contract-phase outer supervisor. Never executed here.

This is new infrastructure, not the old auto-signal runtime core. It creates
no lookup/body binding. Default/disabled input refuses. Root must receive
source, validate the new runtime and supply the external nonself descriptor.
"""
import ctypes
from hashlib import sha256
import json
import os
import signal
import stat
import struct
import subprocess
import sys
import time
import traceback

ROOT = '/root/autodl-tmp/symbolic_dynamics'
QA = ROOT + '/docs/papers211_215_sequence/qa'
SOURCE = QA + '/p212_dependency_query_outer_preparation01'
SELF = SOURCE + '/outer_contract.py'
PRELOAD = SOURCE + '/node_preload.js'
DRIVER = QA + '/p212_execution_scope_source_amendment01/driver.js'
DRIVER_SHA = 'e2bc505d81a377386dd6d6286f601bdbae86ffbda9a751ac7f67ad493251007d'
RECEIPT = QA + '/p212_dependency_source_root01/RECEPTION.md'
RECEIPT_SHA = 'd850da4f954a203338d432b826111ab5ea6f63cc4f0bbffe30752c359b655ca2'
BINDING = QA + '/p212_build_dependency_outer_binding01/contract01/BINDING.json'
INNER_BINDING = QA + '/p212_build_dependency_binding01/contract01/BINDING.json'
OUT = QA + '/p212_build_dependency_outer_capture01/contract01'
QUERY_ROOT = QA + '/p212_build_dependency_query01'
INNER_OUT = QUERY_ROOT + '/contract01'
QUERY_CWD = QUERY_ROOT + '/query_cwd'
CACHE = QA + '/p212_build_dependency_outer_binding01/contract01/never_created_cache'
ENV8 = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC',
        'SOURCE_DATE_EPOCH':'1788825600','FORCE_SOURCE_DATE':'1','openin_any':'p','openout_any':'p'}
STATS = ('dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks',
         'atimeNs','mtimeNs','ctimeNs','birthtimeNs')
IDENTITY = ('dev','ino','mode','uid','gid','rdev')
DKEYS = ('path','role','kind','comparison','lstat','stat','resolved','symlink_target','content','members')
POLICY = {'outer_timeout_seconds':600,'poll_interval_ms':100,'stream_limit_bytes':16777216,
          'automatic_retry':False,'automatic_intervention':False,
          'subreaper_required':True,'continuous_or_escaped_writer_claim':False}
FORBIDDEN = {'lookup':False,'body_capture':False,'engine':False,'bibtex':False,'ldd':False,
             'build':False,'science':False,'lock':False,'external':'HOLD_EXTERNAL'}
BOUND = {}
CREATED = []
EVENT_FD = None
LIBC = None

def need(test, label):
    if not test:
        raise RuntimeError(label)

def equal(a, b, label):
    need(type(a) is type(b) and a == b, label)

def keys(value, wanted, label):
    need(type(value) is dict and set(value) == set(wanted), label + ': exact keys')

def absolute(p):
    need(type(p) is str and p.startswith('/') and os.path.normpath(p) == p
         and all(ord(c) >= 32 and ord(c) != 127 for c in p), 'literal absolute path')
    return p

def wire(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()

def parse(raw):
    def pairs(rows):
        result = {}
        for k, v in rows:
            need(k not in result, 'duplicate JSON key')
            result[k] = v
        return result
    def bad(value):
        raise ValueError('floating/nonfinite JSON is outside this interface: ' + value)
    value = json.loads(raw, object_pairs_hook=pairs, parse_float=bad, parse_constant=bad)
    equal(wire(value), raw, 'complete canonical UTF-8 JSON')
    return value

def value(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def pin_shape(p):
    keys(p, ('bytes','sha256'), 'whole pin')
    need(type(p['bytes']) is int and p['bytes'] >= 0, 'whole finite byte count')
    need(type(p['sha256']) is str and len(p['sha256']) == 64
         and set(p['sha256']) <= set('0123456789abcdef'), 'whole digest')

def native_init():
    global LIBC
    need(sys.platform == 'linux' and sys.byteorder == 'little'
         and struct.calcsize('P') == 8 and struct.calcsize('l') == 8,
         'received Linux little-endian LP64 ABI only')
    LIBC = ctypes.CDLL(None, use_errno=True)
    LIBC.statx.argtypes = [ctypes.c_int,ctypes.c_char_p,ctypes.c_int,ctypes.c_uint,ctypes.c_void_p]
    LIBC.statx.restype = ctypes.c_int
    LIBC.prctl.argtypes = [ctypes.c_int,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong]
    LIBC.prctl.restype = ctypes.c_int

def full_stat(p=None, fd=None, follow=True):
    # Linux UAPI statx has a fixed 256-byte buffer. Preserve its whole returned
    # buffer and masks; never invent a birth time when STATX_BTIME is missing.
    data = (ctypes.c_ubyte * 256)()
    flags = 0x800 | (0x1000 if fd is not None else 0 if follow else 0x100)
    result = LIBC.statx(fd if fd is not None else -100,
                        b'' if fd is not None else os.fsencode(p), flags, 0xFFF, data)
    if result != 0:
        error = ctypes.get_errno()
        raise OSError(error, os.strerror(error), p)
    raw = bytes(data)
    u32 = lambda offset: struct.unpack_from('<I', raw, offset)[0]
    u64 = lambda offset: struct.unpack_from('<Q', raw, offset)[0]
    mask = u32(0)
    need(mask & 0xFFF == 0xFFF, 'all basic fields plus birth time required; no dummy fallback')
    def ns(offset):
        seconds, nanos = struct.unpack_from('<qI', raw, offset)
        need(nanos < 1000000000, 'statx nanosecond range')
        return seconds * 1000000000 + nanos
    numbers = (os.makedev(u32(136),u32(140)),u64(32),struct.unpack_from('<H',raw,28)[0],
               u32(16),u32(20),u32(24),os.makedev(u32(128),u32(132)),u64(40),
               u32(4),u64(48),ns(64),ns(112),ns(96),ns(80))
    return {'fields':dict(zip(STATS, map(str,numbers))), 'statx_mask':mask,
            'attributes':str(u64(8)),'attributes_mask':str(u64(56)),
            'raw_statx_hex':raw.hex()}

def projection(fields, comparison='stable'):
    names = IDENTITY if comparison == 'identity' else tuple(k for k in STATS if k != 'atimeNs')
    return {k:fields[k] for k in names}

def kind(fields):
    mode = int(fields['mode'])
    if stat.S_ISREG(mode): return 'file'
    if stat.S_ISDIR(mode): return 'directory'
    if stat.S_ISLNK(mode): return 'symlink'
    if stat.S_ISCHR(mode): return 'character'
    return 'unsupported'

def descriptor(d):
    keys(d,DKEYS,'finite input descriptor')
    absolute(d['path'])
    need(d['role'] in ('source','runtime','configuration','ancestor','cwd','receipt','device'),
         'contract outer has no body or query-result channel')
    need(d['comparison'] in ('stable','identity'), 'comparison projection')
    if d['comparison'] == 'identity':
        need(d['kind'] == 'directory' and d['role'] == 'ancestor','identity only for namespace ancestors')
    if d['kind'] == 'absent':
        equal([d[k] for k in ('lstat','stat','resolved','symlink_target','content','members')],
              [None]*6,'exact absent descriptor')
        return
    need(d['kind'] in ('file','symlink','directory','character'),'supported finite kind')
    for field in ('lstat','stat'):
        keys(d[field],STATS,'all fourteen integer fields')
        need(all(type(v) is str and v.lstrip('-').isdigit() for v in d[field].values()),
             'integer decimal stat fields')
    absolute(d['resolved'])
    need(d['symlink_target'] is None or type(d['symlink_target']) is str,'literal link target')
    if d['kind'] == 'symlink':
        need(type(d['symlink_target']) is str,'alias target required')
    else:
        equal(d['symlink_target'],None,'nonalias target')
    if d['content'] is not None: pin_shape(d['content'])
    if d['kind'] == 'file': pin_shape(d['content'])
    if d['members'] is not None:
        need(d['kind'] == 'directory' and type(d['members']) is list,'finite membership directory')
        need(all(type(x) is str and x not in ('','.','..') and '/' not in x for x in d['members']),
             'literal member names')
        equal(d['members'],sorted(set(d['members'])),'complete sorted unique membership')

def observe(p):
    need(p in BOUND,'unbound alias/ancestor: '+p)
    d = BOUND[p]
    s = full_stat(p,follow=False)
    equal(kind(s['fields']),d['kind'],'bound lexical kind: '+p)
    equal(projection(s['fields'],d['comparison']),projection(d['lstat'],d['comparison']),
          'bound lexical metadata: '+p)
    target = os.readlink(p) if d['kind'] == 'symlink' else None
    equal(target,d['symlink_target'],'bound link text: '+p)
    return {'path':p,'lstat':s,'symlink_target':target}

def resolve(p):
    absolute(p)
    todo, done, hops, chain = p.split('/')[1:], '/', 0, [observe('/')]
    while todo:
        nxt = os.path.join(done,todo.pop(0))
        row = observe(nxt)
        chain.append(row)
        if row['symlink_target'] is None:
            done = nxt
        else:
            hops += 1
            need(hops <= 40,'finite alias chain')
            target = row['symlink_target']
            rewritten = os.path.normpath(os.path.join(os.path.dirname(nxt),target,*todo))
            todo, done = rewritten.split('/')[1:], '/'
    return done, chain

def read_bound(p, purpose=None):
    d = BOUND[p]
    if purpose is not None: equal(d['role'],purpose,'exact source read purpose')
    need(d['kind'] in ('file','symlink'),'file/alias byte channel')
    r = BOUND.get(d['resolved'])
    need(r and r['kind'] == 'file' and r['role'] == d['role']
         and r['path'] == r['resolved'],'canonical regular same-purpose referent')
    equal(d['stat'],r['stat'],'matching alias and referent metadata')
    equal(d['content'],r['content'],'matching alias and referent complete pins')
    pin_shape(d['content'])
    resolved, chain = resolve(p)
    equal(resolved,d['resolved'],'complete bound resolution')
    fd = os.open(resolved,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK)
    try:
        before = full_stat(fd=fd)
        equal(kind(before['fields']),'file','actual read handle is regular')
        equal(projection(before['fields']),projection(d['stat']),'read handle metadata before')
        chunks, size = [], 0
        while True:
            chunk = os.read(fd,1048576)
            if not chunk: break
            size += len(chunk)
            need(size <= d['content']['bytes'],'bound byte limit, not a prefix claim')
            chunks.append(chunk)
        raw = b''.join(chunks)
        equal(value(raw),d['content'],'entire source pin')
        after = full_stat(fd=fd)
        equal(projection(after['fields']),projection(before['fields']),'same handle stable after')
        return raw, {'path':p,'resolved':resolved,'alias_chain':chain,
                     'handle_before':before,'handle_after':after,'content':value(raw)}
    finally:
        os.close(fd)

def snapshot():
    rows = []
    for d in BOUND.values():
        p = d['path']
        if d['kind'] == 'absent':
            try:
                os.lstat(p)
            except OSError as e:
                need(e.errno == 2,'absence is exactly ENOENT')
            else:
                raise RuntimeError('expected absent: '+p)
            resolve(os.path.dirname(p))
            rows.append({'path':p,'absent':True})
            continue
        resolved, chain = resolve(p)
        equal(resolved,d['resolved'],'snapshot full resolution')
        s = full_stat(p)
        equal(projection(s['fields'],d['comparison']),projection(d['stat'],d['comparison']),
              'snapshot stat projection')
        read_record = read_bound(p)[1] if d['content'] is not None else None
        members = sorted(os.listdir(p)) if d['members'] is not None else None
        equal(members,d['members'],'complete declared membership')
        rows.append({'path':p,'stat':s,'alias_chain':chain,'read':read_record,'members':members})
    return rows

def external_binding(d):
    # The expected descriptor comes from the actual product request, outside
    # BINDING.json. No in-file self-hash, inferred empty pin or alias exemption.
    descriptor(d)
    equal(d['path'],BINDING,'one external binding path')
    need(d['kind'] == 'file' and d['role'] == 'configuration'
         and d['comparison'] == 'stable' and d['resolved'] == BINDING
         and d['symlink_target'] is None and d['members'] is None,'physical binding role')
    equal(os.path.realpath(BINDING),BINDING,'binding and all parents physical')
    ls = full_stat(BINDING,follow=False)
    equal(projection(ls['fields']),projection(d['lstat']),'external binding lexical key')
    fd = os.open(BINDING,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK)
    try:
        before = full_stat(fd=fd)
        equal(kind(before['fields']),'file','external binding regular handle')
        equal(projection(before['fields']),projection(d['stat']),'external binding handle key')
        chunks, size = [], 0
        while True:
            chunk = os.read(fd,1048576)
            if not chunk: break
            size += len(chunk)
            need(size <= d['content']['bytes'],'external binding complete size bound')
            chunks.append(chunk)
        raw = b''.join(chunks)
        equal(value(raw),d['content'],'actual external binding bytes')
        after = full_stat(fd=fd)
        equal(projection(after['fields']),projection(before['fields']),'external same handle after')
        ls_after = full_stat(BINDING,follow=False)
        equal(projection(ls_after['fields']),projection(ls['fields']),'external binding lexical after')
        equal(os.path.realpath(BINDING),BINDING,'external binding resolved after')
        return raw, {'expected_nonself_descriptor':d,'lexical_before':ls,'handle_before':before,
                     'handle_after':after,'lexical_after':ls_after,'pin':value(raw)}
    finally:
        os.close(fd)

def write(name, raw):
    need('/' not in name and name not in ('','.','..'),'flat owned output member')
    fd = os.open(OUT+'/'+name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    try:
        at = 0
        while at < len(raw): at += os.write(fd,raw[at:])
        os.fsync(fd)
    finally: os.close(fd)
    CREATED.append(name)

def record(name, obj):
    write(name,wire(obj))

def event(kind_, **fields):
    raw = json.dumps({'event':kind_,'unix_ns':str(time.time_ns()),**fields},
                     ensure_ascii=False,allow_nan=False,separators=(',',':')).encode()+b'\n'
    at = 0
    while at < len(raw): at += os.write(EVENT_FD,raw[at:])
    os.fsync(EVENT_FD)

def python_sample():
    modules = {}
    for name, module in sorted(sys.modules.items()):
        p = getattr(module,'__file__',None)
        if p:
            p = absolute(os.path.abspath(p))
            need(not p.endswith(('.pyc','.pyo')),'no loaded bytecode path')
            need(p in BOUND and BOUND[p]['role'] in ('runtime','source'),'every Python module prebound')
            modules[name] = {'path':p,'pin':value(read_bound(p)[0])}
    raw = open('/proc/self/maps','rb').read()
    paths = set()
    for line in raw.decode().splitlines():
        fields = line.split(None,5)
        need(len(fields) >= 5,'complete proc-map row')
        if len(fields) == 6 and fields[5].startswith('/'):
            p = fields[5]
            need(not p.endswith(' (deleted)'),'no deleted map')
            need(p in BOUND and BOUND[p]['role'] == 'runtime','every mapped file prebound')
            if p not in paths: read_bound(p,'runtime')
            paths.add(p)
    return {'modules':modules,'mapped_paths':sorted(paths),'proc_maps_hex':raw.hex(),
            'version':sys.version,'executable':os.path.realpath(sys.executable),
            'flags':repr(sys.flags),'sys_path':list(sys.path),'argv':list(sys.argv),
            'orig_argv':list(sys.orig_argv),'environment':dict(os.environ),'cwd':os.getcwd(),
            'pycache_prefix':sys.pycache_prefix,'cache_exists':os.path.lexists(CACHE)}

def proc_row(pid):
    p = '/proc/'+str(pid)+'/stat'
    raw = open(p,'rb').read()
    text = raw.decode()
    close = text.rfind(')')
    need(close >= 0 and int(text[:text.index(' ')]) == pid,'complete proc identity')
    fields = text[close+2:].split()
    need(len(fields) >= 20,'full proc-stat fields')
    return {'pid':pid,'state':fields[0],'ppid':int(fields[1]),'pgid':int(fields[2]),
            'sid':int(fields[3]),'start_ticks':int(fields[19]),'stat_raw_hex':raw.hex()}

def owned_sample():
    # Only own task/children chains. Not every process in any SID, not global
    # /proc inventory, and explicitly not an exhaustive historical spawn trace.
    pending, seen, rows = [(os.getpid(),None)], set(), []
    try:
        while pending:
            pid, expected_parent = pending.pop(0)
            if pid in seen: continue
            seen.add(pid)
            row = {'pid':pid,'expected_parent':expected_parent,'before':None,'after':None,
                   'tasks':None,'children':[]}
            rows.append(row)
            before = proc_row(pid)
            row['before'] = before
            if expected_parent is not None:
                need(before['ppid'] in (expected_parent,os.getpid()),
                     'observed child still belongs to sampled parent or this adopting subreaper')
            tasks = sorted(os.listdir('/proc/'+str(pid)+'/task'))
            row['tasks'] = tasks
            need(all(x.isdigit() for x in tasks),'literal owned task names')
            children = []
            for tid in tasks:
                p = '/proc/'+str(pid)+'/task/'+tid+'/children'
                raw = open(p,'rb').read()
                row['children'].append({'tid':int(tid),'path':p,'raw_hex':raw.hex()})
                words = raw.split()
                need(all(x.isdigit() for x in words),'literal children PID stream')
                children.extend(int(x) for x in words)
            after = proc_row(pid)
            row['after'] = after
            equal(after['start_ticks'],before['start_ticks'],'sampled PID not reused')
            if expected_parent is not None:
                need(after['ppid'] in (expected_parent,os.getpid()),'sampled child ownership after')
            pending.extend((child,pid) for child in children)
    except BaseException as error:
        if EVENT_FD is not None:
            event('OWNED_SAMPLE_INCOMPLETE',root_pid=os.getpid(),rows=rows,
                  pending=pending,error=repr(error),complete=False)
        raise
    return {'root_pid':os.getpid(),'rows':rows,
            'scope':'DISCRETE_OWN_CHILDREN_CHAIN_SAMPLE_NOT_EXHAUSTIVE_HISTORY_OR_SID_CENSUS'}

def subreaper():
    prior = ctypes.c_int()
    need(LIBC.prctl(37,ctypes.addressof(prior),0,0,0) == 0,'PR_GET_CHILD_SUBREAPER supported')
    need(prior.value == 0,'fresh non-subreaper supervisor at entry')
    need(LIBC.prctl(36,1,0,0,0) == 0,'PR_SET_CHILD_SUBREAPER succeeded')
    actual = ctypes.c_int()
    need(LIBC.prctl(37,ctypes.addressof(actual),0,0,0) == 0 and actual.value == 1,
         'actual subreaper setting read back')
    signal.signal(signal.SIGCHLD,signal.SIG_DFL)
    equal(signal.getsignal(signal.SIGCHLD),signal.SIG_DFL,'waitable child disposition')
    return {'previous':prior.value,'set_return':0,'actual':actual.value,
            'scope':'OWN_ORPHANED_DESCENDANT_REPARENTING_NOT_ESCAPED_WRITER_EXCLUSION'}

def validate(b):
    keys(b,('schema','status','enabled','phase','output','inner_binding','node_preload',
            'python','runtime','inputs','receipts','policy','forbidden'),'outer binding')
    equal(b['schema'],'p212-contract-outer-binding-v1','binding schema')
    need(b['enabled'] is True and b['status'] == 'ROOT_BOUND_CONTRACT_ONLY','explicit future root binding')
    equal(b['phase'],'contract','no lookup or body mode')
    equal(b['output'],OUT,'one exclusive outer capture')
    equal(b['policy'],POLICY,'entire native policy')
    equal(b['forbidden'],FORBIDDEN,'all forbidden successors')
    keys(b['python'],('executable_resolved','orig_argv_prefix','sys_path','version',
                     'mapped_paths','modules'),'entire selected Python startup')
    equal(b['python']['orig_argv_prefix'],
          ['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+CACHE,SELF,BINDING],
          'fixed interpreter prefix; final external descriptor is not recursively embedded')
    keys(b['runtime'],('node','native_request_ref','tool_closure'),'entire selected runtime')
    keys(b['runtime']['node'],('executable_spelling','executable_resolved','mapped_paths',
         'builtin_source_fingerprints','versions','architecture','platform','internal_bindings'),
         'complete finite Node runtime policy')
    equal(b['inner_binding']['path'],INNER_BINDING,'exact inner binding')
    equal(b['node_preload']['path'],PRELOAD,'exact received preload')
    for field in ('inner_binding','node_preload'):
        keys(b[field],('path','pin'),'bound reference'); pin_shape(b[field]['pin'])
    keys(b['receipts'],('dependency_source','source_amendment','outer_source','runtime','product_startup'),
         'all independent gates including the new manuscript-state source amendment')
    need(type(b['inputs']) is list and b['inputs'],'complete finite input list')
    for d in b['inputs']:
        descriptor(d)
        need(d['path'] not in BOUND,'duplicate input path')
        BOUND[d['path']] = d
    need(BINDING not in BOUND,'selected outer binding is covered only by external nonself descriptor')
    need(not any(p == OUT or p.startswith(OUT+'/') or p == INNER_OUT or p.startswith(INNER_OUT+'/')
                 for p in BOUND),'new output is not an immutable input')
    for p in ('/',SELF,PRELOAD,DRIVER,INNER_BINDING,RECEIPT,'/usr/bin/python3.10','/bin/bash','/usr/bin/env',
              '/usr/bin/kpsewhich','/dev/null',CACHE,QUERY_ROOT,QUERY_CWD,os.path.dirname(OUT)):
        need(p in BOUND,'mandatory finite input: '+p)
    equal(BOUND[CACHE]['kind'],'absent','cache must remain absent')
    equal(BOUND[QUERY_CWD]['members'],[],'actual query cwd observed empty')
    for p in (SELF,PRELOAD,DRIVER): equal(BOUND[p]['role'],'source','mandatory source role')
    for p in ('/usr/bin/python3.10','/bin/bash','/usr/bin/env'):
        equal(BOUND[p]['role'],'runtime','actual product bootstrap runtime role')
    equal(BOUND['/usr/bin/kpsewhich']['role'],'runtime','exact native tool role')
    equal(BOUND['/dev/null']['kind'],'character','explicit stdin device')
    for label, ref in b['receipts'].items():
        keys(ref,('path','pin'),'receipt ref')
        need(ref['path'].startswith(ROOT+'/'),'workspace receipt only')
        pin_shape(ref['pin'])
        raw, _ = read_bound(ref['path'],'receipt')
        equal(value(raw),ref['pin'],'whole received gate: '+label)
    equal(b['receipts']['dependency_source']['path'],RECEIPT,'accepted joint source receipt')
    equal(b['receipts']['dependency_source']['pin']['sha256'],RECEIPT_SHA,'exact root source decision')
    equal(value(read_bound(DRIVER,'source')[0])['sha256'],DRIVER_SHA,
          'exact prospective amended driver; independent amendment acceptance also required')
    for field in ('inner_binding','node_preload'):
        equal(value(read_bound(b[field]['path'])[0]),b[field]['pin'],'whole '+field)
    inner = parse(read_bound(INNER_BINDING,'configuration')[0])
    need(inner['enabled'] is True and inner['phase'] == 'contract','one contract-only inner binding')
    equal(inner['receipts']['driver_source'],b['receipts']['source_amendment'],
          'separate exact amendment acceptance, not only historical revision02 receipt')
    equal(inner['query_inputs'],[],'no archived queries/body scope')
    equal(inner['body_requests'],[],'no bodies')
    for d in inner['inputs']:
        equal(BOUND.get(d['path']),d,'entire inner input descriptor prechecked by outer')
    node = b['runtime']['node']
    argv = [node['executable_resolved'],'--require',PRELOAD,DRIVER,INNER_BINDING]
    equal(inner['controller']['executable_spelling'],node['executable_spelling'],'same Node spelling')
    equal(inner['controller']['executable_resolved'],node['executable_resolved'],'same Node referent')
    equal(inner['controller']['exec_argv'],['--require',PRELOAD],'received exact preload options')
    equal(inner['controller']['argv'],[node['executable_resolved'],DRIVER,INNER_BINDING],
          'actual Node application argv')
    equal(inner['controller']['environment'],ENV8,'actual Node replacement ENV8')
    equal(inner['controller']['outer_entry_source'],{'path':SELF,'pin':BOUND[SELF]['content']},
          'exact outer source receipt in inner')
    equal(inner['controller']['outer_request_record'],b['runtime']['native_request_ref'],
          'prepared exact native request ref in inner')
    ref = b['runtime']['native_request_ref']
    keys(ref,('path','pin'),'nonrecursive prepared Node request reference')
    pin_shape(ref['pin'])
    prepared_raw = read_bound(ref['path'],'receipt')[0]
    equal(value(prepared_raw),ref['pin'],'whole prepared Node request')
    equal(parse(prepared_raw),{'schema':'p212-prepared-node-contract-request-v1',
          'phase':'contract','argv':argv,'cwd':ROOT,'environment':ENV8,'umask':0o077,
          'stdin':'BOUND_/dev/null','stdout':OUT+'/driver.stdout.raw',
          'stderr':OUT+'/driver.stderr.raw','start_new_session':True,'close_fds':True,
          'not_an_actual_product_tool_result':True},'actual Popen request exactly prepared')
    equal(inner['receipts']['prestartup'],b['receipts']['runtime'],'same separately received startup gate')
    need(node['executable_resolved'] in BOUND and node['executable_spelling'] in BOUND,
         'both Node executable spellings prebound')
    for p in (node['executable_resolved'],node['executable_spelling']):
        equal(BOUND[p]['role'],'runtime','Node runtime role')
    need(b['runtime']['tool_closure'] and '/usr/bin/kpsewhich' in b['runtime']['tool_closure'],
         'explicit source-received kpsewhich ELF/configuration closure')
    for p in b['runtime']['tool_closure']: need(p in BOUND,'every finite native closure path keyed')
    return argv

def main():
    global EVENT_FD
    need(len(sys.argv) == 3,'HOLD: external canonical nonself descriptor JSON required')
    equal(sys.argv[1],BINDING,'one exact outer binding')
    external = parse(sys.argv[2].encode())
    native_init()
    raw, external_before = external_binding(external)
    b = parse(raw)
    argv = validate(b)
    equal(dict(os.environ),ENV8,'cleared supervisor ENV8')
    equal(os.getcwd(),ROOT,'physical workspace cwd')
    equal(os.path.realpath(sys.executable),b['python']['executable_resolved'],'Python executable')
    equal(sys.orig_argv[:-1],b['python']['orig_argv_prefix'],'actual original interpreter argv prefix')
    equal(sys.orig_argv[-1],sys.argv[2],'actual final externally keyed descriptor argument')
    need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.dont_write_bytecode == 1
         and sys.flags.optimize == 0,'isolated no-site no-bytecode exact supervisor startup')
    equal(sys.pycache_prefix,CACHE,'unique externally selected cache prefix')
    equal(sys.path,b['python']['sys_path'],'complete selected Python import path')
    equal(sys.version,b['python']['version'],'complete Python version')
    need(not os.path.lexists(CACHE),'real cache absence before Node startup')
    prior_umask = os.umask(0o077)
    before = snapshot()
    python_before = python_sample()
    equal(python_before['mapped_paths'],b['python']['mapped_paths'],'all current Python native maps')
    equal(python_before['modules'],b['python']['modules'],'complete pre-received Python modules')
    for p in (OUT,INNER_OUT): need(not os.path.lexists(p),'exclusive new output required: '+p)
    resolve(os.path.dirname(OUT))
    os.mkdir(OUT,0o700)
    record('BINDING_KEY_BEFORE.json',external_before)
    write('OUTER_BINDING_ORIGINAL.json',raw)
    record('INPUTS_BEFORE.json',before)
    record('PYTHON_BEFORE.json',python_before)
    write('INNER_BINDING_ORIGINAL.json',read_bound(INNER_BINDING,'configuration')[0])
    record('UMASK.json',{'inherited':prior_umask,'selected_before_Node':0o077})
    setup = subreaper()
    record('SUBREAPER_BEFORE.json',setup)
    EVENT_FD = os.open(OUT+'/EVENTS.jsonl',os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    CREATED.append('EVENTS.jsonl')
    baseline = owned_sample()
    need(len(baseline['rows']) == 1,'new supervisor has no prior child tree')
    event('OWNED_SAMPLE_BEFORE',sample=baseline)
    null_path, null_chain = resolve('/dev/null')
    null_fd = os.open(null_path,os.O_RDONLY|os.O_NOFOLLOW)
    null_stat = full_stat(fd=null_fd)
    equal(kind(null_stat['fields']),'character','actual stdin handle is character device')
    equal(projection(null_stat['fields']),projection(BOUND['/dev/null']['stat']),'bound stdin identity')
    streams = [os.open(OUT+'/'+name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
               for name in ('driver.stdout.raw','driver.stderr.raw')]
    CREATED.extend(('driver.stdout.raw','driver.stderr.raw'))
    record('ATTEMPT.json',{'argv':argv,'cwd':ROOT,'environment':ENV8,'umask':0o077,
                          'policy':POLICY,'stdin_handle':null_stat,'stdin_chain':null_chain,
                          'pre_Node_input_key':value(wire(before)),
                          'external_binding_key':external_before,
                          'actual_product_records':'SEPARATE_ROOT_VALUES_REQUIRED'})
    process, driver_code, ech = None, None, False
    reaped = []
    try:
        event('SPAWN_ATTEMPT',argv=argv)
        process = subprocess.Popen(argv,cwd=ROOT,env=ENV8,stdin=null_fd,
                                   stdout=streams[0],stderr=streams[1],
                                   start_new_session=True,close_fds=True)
        event('SPAWN_RETURN',pid=process.pid,requested_new_session=True)
        deadline = time.monotonic()+POLICY['outer_timeout_seconds']
        while True:
            sample = owned_sample()
            event('OWNED_SAMPLE',sample=sample)
            try:
                info = os.waitid(os.P_ALL,0,os.WEXITED|os.WNOHANG|os.WNOWAIT|0x40000000)
            except ChildProcessError:
                event('WAIT_ECHILD',driver_pid=process.pid,driver_code=driver_code)
                ech = True
                break
            if info is not None:
                row = {k:getattr(info,k) for k in ('si_pid','si_uid','si_signo','si_status','si_code')}
                identity = proc_row(info.si_pid)
                pid, status = os.waitpid(info.si_pid,os.WNOHANG|0x40000000)
                equal(pid,info.si_pid,'actual waited PID')
                code = os.waitstatus_to_exitcode(status)
                reaped.append({'waitid':row,'identity':identity,'waitpid_status':status,'exit_code':code})
                event('REAP',actual=reaped[-1])
                if pid == process.pid:
                    driver_code = code
                    process.returncode = code
            if time.monotonic() >= deadline:
                raise RuntimeError('UNKNOWN_UNCLOSED: no automatic signal or cleanup on deadline')
            time.sleep(POLICY['poll_interval_ms']/1000)
        need(ech and driver_code == 0,'actual driver success plus ECHILD required')
        final_owned = owned_sample()
        need(len(final_owned['rows']) == 1,'no sampled remaining owned descendant')
        event('OWNED_SAMPLE_FINAL',sample=final_owned)
        need(len(reaped) == 1 and reaped[0]['waitid']['si_pid'] == process.pid,
             'unexpected adopted native descendant requires root disposition')
    except BaseException as exc:
        record('UNKNOWN_OR_FAILED.json',{'error':repr(exc),'traceback':traceback.format_exc(),
               'pid':process.pid if process is not None else None,'driver_code':driver_code,
               'observed_echild':ech,'reaped':reaped,'final_stream_hashes':None,'outer_seal':None,
               'automatic_intervention':False,'automatic_retry':False,
               'next_action':'ROOT_ACTUAL_OWNED_PROCESS_SETTLEMENT_NO_SUCCESS_HASH_OR_SEAL',
               'limit':'Supervisor exit does not settle any still-running descendant or escaped writer.'})
        return 76
    finally:
        for fd in [null_fd,*streams]:
            os.close(fd)
        if EVENT_FD is not None:
            os.close(EVENT_FD)
            EVENT_FD = None
    inner_result = parse(open(INNER_OUT+'/RESULT.json','rb').read())
    equal(inner_result['schema'],'p212-finite-frontier-capture-v1','actual inner result schema')
    equal(inner_result['status'],'FINITE_INNER_CAPTURE_COMPLETE_ROOT_ORIGINAL_RECEPTION_PENDING',
          'actual inner result remains pending root reception')
    equal(inner_result['phase'],'contract','actual completed contract role')
    equal(inner_result['actual_kpsewhich_commands'],2,'only two actual help/version commands')
    equal(inner_result['actual_body_copies'],0,'no body copies')
    equal(inner_result['installed_option_semantics_accepted_by_this_driver'],False,'no self-accepted options')
    equal(inner_result['next_phase_automatically_authorized'],False,'no automatic successor')
    equal([x['label'] for x in inner_result['completed']],['contract_help','contract_version'],
          'exact completed command labels')
    node_result = parse(open(OUT+'/NODE_RESULT.json','rb').read())
    equal(node_result['status'],'OBSERVED_CONTRACT_NODE_RUNTIME_PENDING_ROOT','actual Node observation')
    equal(node_result['driver_exit_code'],0,'actual successful driver exit observation')
    equal(node_result['errors'],[],'no preload observation errors')
    equal(node_result['lookup_or_body_permission'],False,'preload grants no successor')
    equal(node_result['spawn_argv'],[['/usr/bin/kpsewhich','--help'],['/usr/bin/kpsewhich','--version']],
          'preload observed only two exact native vectors')
    # Only settled lifetime plus both actual inner/preload completion records
    # can reach any final native stream hash.
    stream_values = {}
    for name in ('driver.stdout.raw','driver.stderr.raw'):
        need(os.stat(OUT+'/'+name).st_size <= POLICY['stream_limit_bytes'],'whole retained stream bound')
        data = open(OUT+'/'+name,'rb').read()
        stream_values[name] = value(data)
    equal(stream_values['driver.stderr.raw']['bytes'],0,'driver stderr requires separate disposition')
    after = snapshot()
    python_after = python_sample()
    equal(python_after['modules'],python_before['modules'],'no late unreceived Python module')
    equal(python_after['mapped_paths'],python_before['mapped_paths'],'no late unreceived Python map')
    raw_after, external_after = external_binding(external)
    equal(raw_after,raw,'binding whole raw bytes after entire native lifetime')
    record('BINDING_KEY_AFTER.json',external_after)
    record('INPUTS_AFTER.json',after)
    record('PYTHON_AFTER.json',python_after)
    need(not os.path.lexists(CACHE),'cache still absent after Node')
    record('RESULT.json',{'status':'CONTRACT_OUTER_CLOSED_ROOT_PRODUCT_RECEPTION_PENDING',
                         'phase':'contract','driver_pid':process.pid,'driver_exit_code':driver_code,
                         'wait_echild':ech,'reaped':reaped,'stream_pins':stream_values,
                         'inner_result_pin':value(wire(inner_result)),'node_result_pin':value(wire(node_result)),
                         'actual_product_request_yield_poll_final':'REQUIRED_FROM_ROOT_ORIGINAL_TOOL_VALUES',
                         'interventions':[],'outer_manifest':None,'next_phase_authorized':False,
                         'scope':'Subreaper-owned descendant settlement and discrete samples only; no continuous/SID/escaped-writer claim.',
                         'forbidden':FORBIDDEN})
    print(json.dumps({'status':'CONTRACT_OUTER_CLOSED_ROOT_PRODUCT_RECEPTION_PENDING',
                      'output':OUT,'driver_exit_code':0,'outer_manifest':None},sort_keys=True),flush=True)
    return 0

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        # Pre-spawn failures can occur before OUT exists. The actual product
        # request and every native return remain root-owned originals.
        print('HOLD_OUTER: '+repr(exc),file=sys.stderr,flush=True)
        raise SystemExit(78)
