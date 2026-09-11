"""SOURCE ONLY: runtime enumeration/ABI under an explicit trusted-product model.
Missing separate source, finite bootstrap-key and trust-boundary receipts
refuses. This is NOT a product-startup attestation or operational permission;
it never imports the driver or creates a contract/lookup/body binding.
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
SELF = QA + '/p212_trusted_product_source_delta01/python_runtime_probe.py'
ENV8 = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC',
        'SOURCE_DATE_EPOCH':'1788825600','FORCE_SOURCE_DATE':'1','openin_any':'p','openout_any':'p'}
PROVENANCE = {'schema':'p212-trusted-product-boundary-v1',
              'assumption':'ordinary_product_observer_bash_env_bootstrap',
              'product_startup_attested':False,
              'claim':'finite_received_keys_and_discrete_downstream_observations'}
STATS = ('dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks',
         'atimeNs','mtimeNs','ctimeNs','birthtimeNs')

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def main():
    need(len(sys.argv) == 2, 'HOLD_RUNTIME_PROBE: explicit external received runtime-only authorization')
    a = json.loads(sys.argv[1])
    need(json.dumps(a,ensure_ascii=False,indent=2,allow_nan=False)+'\n' == sys.argv[1],
         'complete canonical runtime authorization; no duplicate or hidden fields')
    need(set(a) == {'schema','enabled','status','provenance','receipts','statx_validation_paths'},
         'exact trusted-product runtime-only keys')
    need(a['schema'] == 'p212-trusted-product-runtime-probe-authorization-v1', 'distinct probe schema')
    need(a['enabled'] is True and a['status'] == 'ROOT_BOUND_TRUSTED_PRODUCT_RUNTIME_DISCOVERY_ONLY',
         'separate runtime-only authority')
    need(a['provenance'] == PROVENANCE and a['provenance']['product_startup_attested'] is False,
         'fixed conditional model with literal false; no product-startup attestation')
    roles = ('source','bootstrap_key','trusted_product_boundary')
    need(type(a['receipts']) is dict and set(a['receipts']) == set(roles), 'three distinct receipt roles')
    receipt_originals = []
    for role in roles:
        ref = a['receipts'][role]
        need(set(ref) == {'path','pin'} and ref['path'].startswith(QA+'/')
             and os.path.realpath(ref['path']) == ref['path'], 'physical finite receipt path')
        need(set(ref['pin']) == {'bytes','sha256'} and type(ref['pin']['bytes']) is int
             and ref['pin']['bytes'] >= 0 and type(ref['pin']['sha256']) is str
             and len(ref['pin']['sha256']) == 64
             and set(ref['pin']['sha256']) <= set('0123456789abcdef'), 'complete finite receipt pin')
        fd = os.open(ref['path'],os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK)
        try:
            before = os.fstat(fd)
            need(stat.S_ISREG(before.st_mode) and before.st_size == ref['pin']['bytes'], 'whole regular receipt')
            chunks, size = [], 0
            while True:
                chunk = os.read(fd,1048576)
                if not chunk: break
                size += len(chunk)
                need(size <= ref['pin']['bytes'], 'whole receipt byte bound')
                chunks.append(chunk)
            raw = b''.join(chunks)
            after = os.fstat(fd)
            need((before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns,before.st_ctime_ns)
                 == (after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns,after.st_ctime_ns),
                 'same receipt handle stable')
            need({'bytes':len(raw),'sha256':sha256(raw).hexdigest()} == ref['pin'], 'complete external receipt pin')
            receipt_originals.append({'role':role,'reference':ref,'raw_hex':raw.hex()})
        finally:
            os.close(fd)
    need(len({r['reference']['path'] for r in receipt_originals}) == len(roles),
         'source, independent finite bootstrap key and trust decision use separate receipts')
    need(dict(os.environ) == ENV8 and os.getcwd() == ROOT, 'received ENV8 and cwd')
    need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.dont_write_bytecode == 1
         and sys.flags.optimize == 0, 'runtime probe isolated no-site no-bytecode')
    need(sys.pycache_prefix and not os.path.lexists(sys.pycache_prefix), 'unique absent probe cache')
    need(sys.platform == 'linux' and sys.byteorder == 'little'
         and struct.calcsize('P') == 8 and struct.calcsize('l') == 8, 'Linux little-endian LP64 only')
    libc = ctypes.CDLL(None,use_errno=True)
    libc.statx.argtypes = [ctypes.c_int,ctypes.c_char_p,ctypes.c_int,ctypes.c_uint,ctypes.c_void_p]
    libc.statx.restype = ctypes.c_int
    libc.prctl.argtypes = [ctypes.c_int,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong]
    libc.prctl.restype = ctypes.c_int
    rows = []
    paths = a['statx_validation_paths']
    need(type(paths) is list and paths == sorted(set(paths))
         and all(type(p) is str and p.startswith('/') and os.path.normpath(p) == p for p in paths)
         and all(p in paths for p in (SELF,'/dev/null','/')), 'finite explicit validation metadata targets')
    for p in paths:
        data = (ctypes.c_ubyte * 256)()
        need(libc.statx(-100,os.fsencode(p),0x800|0x100,0xFFF,data) == 0, 'actual statx call succeeds')
        raw = bytes(data)
        u32 = lambda n: struct.unpack_from('<I',raw,n)[0]
        u64 = lambda n: struct.unpack_from('<Q',raw,n)[0]
        need(u32(0) & 0xFFF == 0xFFF, 'all basic plus birthtime returned; no fabricated fallback')
        def ns(n):
            sec,nano = struct.unpack_from('<qI',raw,n)
            need(nano < 1000000000, 'actual nanos range')
            return sec*1000000000+nano
        numbers = (os.makedev(u32(136),u32(140)),u64(32),struct.unpack_from('<H',raw,28)[0],
                   u32(16),u32(20),u32(24),os.makedev(u32(128),u32(132)),u64(40),u32(4),u64(48),
                   ns(64),ns(112),ns(96),ns(80))
        rows.append({'path':p,'lstat_fields':dict(zip(STATS,map(str,numbers))),
                     'mask':u32(0),'raw_statx_hex':raw.hex()})
    previous,actual = ctypes.c_int(),ctypes.c_int()
    need(libc.prctl(37,ctypes.addressof(previous),0,0,0) == 0 and previous.value == 0, 'fresh subreaper status')
    need(libc.prctl(36,1,0,0,0) == 0, 'actual subreaper setter')
    need(libc.prctl(37,ctypes.addressof(actual),0,0,0) == 0 and actual.value == 1, 'actual subreaper readback')
    signal.signal(signal.SIGCHLD,signal.SIG_DFL)
    try:
        result = os.waitid(os.P_ALL,0,os.WEXITED|os.WNOHANG|os.WNOWAIT|0x40000000)
    except ChildProcessError:
        empty_wait = 'ACTUAL_ECHILD'
    else:
        raise RuntimeError('probe must have no child; returned '+repr(result))
    maps = open('/proc/self/maps','rb').read()
    modules = {name:os.path.abspath(m.__file__) for name,m in sorted(sys.modules.items())
               if getattr(m,'__file__',None)}
    need(not any(p.endswith(('.pyc','.pyo')) for p in modules.values()), 'no loaded bytecode')
    print(json.dumps({'status':'RUNTIME_ENUMERATION_ONLY_ROOT_FULL_KEY_AND_ABI_COMPARISON_PENDING',
        'source':SELF,'provenance':PROVENANCE,'receipts':receipt_originals,'statx':rows,
        'subreaper':{'previous':previous.value,'actual':actual.value,'wait':empty_wait},
        'module_paths':modules,'proc_maps_hex':maps.hex(),'version':sys.version,
        'executable':os.path.realpath(sys.executable),'flags':repr(sys.flags),'sys_path':sys.path,
        'orig_argv':sys.orig_argv,'environment':dict(os.environ),'cwd':os.getcwd(),
        'cache_prefix':sys.pycache_prefix,'cache_exists':os.path.lexists(sys.pycache_prefix),
        'driver_imported':False,'child_spawned':False,'source_or_runtime_acceptance':False,
        'limit':'Paths/maps are enumeration only. Root must bind every entire file/configuration/bootstrap dependency before contract.'},
        ensure_ascii=False,indent=2)+'\n',end='',flush=True)

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('HOLD_RUNTIME_PROBE: '+repr(error),file=sys.stderr,flush=True)
        raise SystemExit(78)
