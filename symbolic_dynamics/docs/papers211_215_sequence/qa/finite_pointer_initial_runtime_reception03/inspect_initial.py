#!/usr/bin/python3.10
"""SOURCE_ONLY until separate root source acceptance; pointer initial infra only.

Forward derivative of p211_a_root_reception/inspect_production.py, not an
independent mathematical verifier. No submitted source import/exec/subprocess.
The scientific stdout is opaque: full streaming hash, never raw()/JSON parsed.
Maps have an independent raw reconstruction; modules have only the pinned
core's complete sys.modules loop and saved discrete table, not a second census.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import re
import stat
import sys
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'finite_pointer_initial_runtime_reception03'
BDIR = QA/'finite_pointer_initial_binding01'
BPATH = BDIR/'BINDING.json'
BINDING_SHA = '7575bf8027327615dbe3a938b4fb50de6f8b7b241668346435369d99874e01ac'
CAPTURE = BDIR/'PRODUCTION_TOOL_INVOCATION.json'
CAPTURE_SHA = 'f0ef5f54577f48e760533883ca1fb67aa2d31acdf7c876c539986a1ee9dedb16'
PREP = QA/'finite_pointer_runtime_preparation01'
OLD = QA/'p211_runtime_preparation'
WRAPPER = PREP/'pointer_runtime.py'
LOCK_PATH = PREP/'discovery02/RUNTIME_LOCK.json'
LOCK_SHA = 'e2fd2189f639feff28a8ae499da011e9ea6e9cadf3eb99b60944f3209fdebd02'
ATTEMPT = QA/'root_replays/finite_pointer_initial01'
ATTEMPT_SHA = 'fa2e6fc67759c537cf98ef99409fe99b72c986cb34f2dc8319e5b97ad9294c43'
CAPSULE = ATTEMPT/'recorder/capsule'
OPAQUE_STDOUT = ATTEMPT/'recorder/commands/03_verify_01/stdout.raw'
SCIENCE = ROOT/'docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01'
STAGES = ('outer', 'launcher', 'recorder', 'child01')
ENV = {'PATH':'/usr/bin:/bin', 'LANG':'C.UTF-8', 'LC_ALL':'C.UTF-8', 'TZ':'UTC'}
IMPORTS = ['collections','fractions','itertools','json','math','sys']
SOURCE_PINS = {
    str(WRAPPER): ('89bec42ec8ae827156ac32cd0c8213faef06387930152bee6b1be3a37e4e92bf',4933),
    str(OLD/'p211_runtime.py'): ('bff2dcf25ee846b04eac0bbd46eb7b3e58c728c6d7e8e9ce591c9cef1ae4e421',29041),
    str(OLD/'runtime_core.py'): ('2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934',13293),
}
CAPSULE_PINS = {
    'pointer_pilot.py': ('9b3c22ad86b36f5dece45d47de03d3cc309f05c46c40a152aec49dc8a0262cbb',27518),
    'PARAMETERS.json': ('f71aff49cb7b4fda75851992a85ce3150cd8f69f1dd5a4512bb6e7b3afe08a16',415),
}
COMMON = {'ENTERED.json','RESULT.json','INPUTS_BEFORE.json','INPUTS_AFTER.json',
          'CONFIGURATION_BEFORE.json','CONFIGURATION_AFTER.json','RUNTIME_BEFORE.json',
          'RUNTIME_AFTER.json','OPEN_EVENTS_RAW.json','OPEN_OBSERVATIONS.json'}
NATIVE_FILES = ('ATTEMPT.json','RECEIPT.json','stdout.raw','stderr.raw')
LABELS = {'outer':['01_launcher'], 'launcher':['01_recorder'],
          'recorder':['00_copy_0','00_copy_1','01_ldd_before','03_verify_01','06_ldd_after'],
          'child01':[]}
CONFIG_PATHS = (
    '/dev/null','/etc/ld.so.cache','/etc/ld.so.conf','/etc/ld.so.preload',
    '/etc/localtime','/etc/locale.conf','/etc/default/locale',
    '/etc/nsswitch.conf','/etc/passwd','/etc/group','/etc/ssl/openssl.cnf','/usr/lib/ssl/openssl.cnf',
    '/usr/lib/locale/locale-archive','/usr/lib/python310.zip','/usr/bin/pyvenv.cfg','/usr/pyvenv.cfg',
    '/lib/ld-linux.so.2','/lib64/ld-linux-x86-64.so.2','/libx32/ld-linux-x32.so.2',
    '/usr/lib/python3.10/config-3.10-x86_64-linux-gnu/Makefile','/usr/include/python3.10/pyconfig.h',
    '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules',
    '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache',
    '/usr/share/locale/C.UTF-8/LC_MESSAGES/libc.mo',
    '/usr/share/locale/C.utf8/LC_MESSAGES/libc.mo','/usr/share/locale/C/LC_MESSAGES/libc.mo')
MEMBER_DIRS = ('/usr/lib/locale/C.utf8','/usr/lib/locale/C.utf8/LC_MESSAGES',
    '/usr/lib/x86_64-linux-gnu/gconv','/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.d',
    '/etc/ld.so.conf.d')
CONFIG_SCOPE = 'Listed configuration and direct directory membership only; no host/library/stdlib recursion.'
OPEN_SCOPE = 'Post-hook Python opens and discrete file-backed maps/modules; not OS/startup/escaped-descendant tracing.'
SAMPLE_SCOPE = 'file-backed module/map sample, not continuous or OS syscall tracing'
RESULT_SCOPE = 'Bounded infrastructure execution evidence, not a proof, review or hermetic runtime trace.'
STREAM_SCOPE = 'Every emitted native byte retained in exclusive files; hashes finalized only after owned-group quiescence. A timeout/interruption remains an unsuccessful partial computation.'
FLAGS = 'sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=1, no_user_site=1, no_site=1, ignore_environment=1, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=1, dev_mode=False, utf8_mode=0, warn_default_encoding=0, int_max_str_digits=-1)'
CHECKS, READS, RAW_READS, TREES = 0, {}, {}, {}


def need(ok, detail):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(detail)


def identity(data):
    return {'sha256':sha256(data).hexdigest(), 'bytes':len(data)}


def basic(row):
    return {k:row[k] for k in ('sha256','bytes')}


def rich(path):
    """Streaming bytes only, including the deliberately opaque scientific stdout."""
    p = Path(path)
    need(p.is_absolute() and p.is_file(), ('absolute regular input',str(p)))
    pre = p.stat()
    resolved, link = str(p.resolve(strict=True)), os.readlink(p) if p.is_symlink() else None
    h, size = sha256(), 0
    with p.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024), b''):
            h.update(block)
            size += len(block)
    post = p.stat()
    need(stat.S_ISREG(post.st_mode) and
         (pre.st_dev,pre.st_ino,pre.st_size,pre.st_mtime_ns,pre.st_ctime_ns)==
         (post.st_dev,post.st_ino,post.st_size,post.st_mtime_ns,post.st_ctime_ns) and
         size==post.st_size and resolved==str(p.resolve(strict=True)) and
         link==(os.readlink(p) if p.is_symlink() else None), ('stable complete input',str(p)))
    value = {'sha256':h.hexdigest(),'bytes':size,'resolved':resolved,'symlink':link}
    need(str(p) not in READS or READS[str(p)]==value, ('unchanged whole rich reread',str(p)))
    READS[str(p)] = value
    return value


def pin(path, expected):
    actual = rich(path)
    expected = {'sha256':expected} if isinstance(expected,str) else expected
    need(isinstance(expected,dict) and 'sha256' in expected and
         set(expected)<={'sha256','bytes','resolved','symlink','path','name'} and
         all(actual[k]==expected[k] for k in actual if k in expected), ('exact complete pin',str(path)))
    return actual


def raw(path):
    p = Path(path)
    need(p.resolve()!=OPAQUE_STDOUT, 'scientific stdout is hash-only, never raw/body/JSON')
    value = rich(p)
    data = p.read_bytes()
    need(identity(data)==basic(value), ('complete raw read bound to stream pin',str(p)))
    need(str(p) not in RAW_READS or RAW_READS[str(p)]==data, ('exact raw reread',str(p)))
    RAW_READS[str(p)] = data
    return data


def unique(items):
    result = {}
    for key,value in items:
        need(key not in result, ('duplicate JSON key',key))
        result[key] = value
    return result


def json_value(data):
    return json.loads(data,object_pairs_hook=unique,
                      parse_constant=lambda v:need(False,('nonfinite JSON',v)))


def doc(path):
    return json_value(raw(path))


def state(path, with_bytes=True):
    p = Path(path)
    row = {'lexists':os.path.lexists(p),'exists':p.exists(),'is_file':p.is_file(),
           'is_dir':p.is_dir(),'is_character_device':p.is_char_device(),
           'resolved':str(p.resolve()),'symlink':os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        s = p.stat()
        row['character_device'] = {'major':os.major(s.st_rdev),'minor':os.minor(s.st_rdev),'mode':s.st_mode}
    if with_bytes and p.is_file():
        row.update(basic(rich(p)))
    return row


def configuration():
    paths, members = set(CONFIG_PATHS), {}
    for directory in ('/usr/bin','/usr/lib'):
        paths.update(str(Path(directory)/n) for n in ('python._pth','python3._pth','python310._pth','python3.10._pth'))
    for directory in MEMBER_DIRS:
        p = Path(directory)
        row = {'directory':state(p,False),'members':{}}
        if p.is_dir():
            row['members'] = {q.name:state(q,False) for q in sorted(p.iterdir())}
            if directory!='/usr/lib/x86_64-linux-gnu/gconv':
                paths.update(str(q) for q in p.iterdir() if q.is_file())
        members[directory] = row
    return {'paths':{p:state(p) for p in sorted(paths)},'memberships':members,'scope':CONFIG_SCOPE}


def loader_scope(config):
    lines = [s.strip() for s in raw(Path('/etc/ld.so.conf')).decode().splitlines()
             if s.strip() and not s.lstrip().startswith('#')]
    need(lines==['include /etc/ld.so.conf.d/*.conf'], 'exact single loader include')
    result = {}
    for name in config['paths']:
        p = Path(name)
        if p.parent==Path('/etc/ld.so.conf.d') and p.is_file():
            for line in raw(p).decode().splitlines():
                clean = line.split('#',1)[0].strip()
                if clean:
                    need(clean.startswith('/') and not any(c in clean for c in '*?[]\t '), 'literal loader directory')
                    result[clean] = state(clean,False)
    return result


def inventory(folder, names, empty=()):
    need(folder.is_dir() and folder.resolve()==folder, ('physical package root',str(folder)))
    dirs = set(empty)
    for name in names:
        dirs.update(str(p) for p in Path(name).parents if str(p)!='.')
    gotfiles, gotdirs = set(), set()
    for p in folder.rglob('*'):
        need(not p.is_symlink() and p.resolve()==p, ('physical artifact, no symlink',str(p)))
        name = str(p.relative_to(folder))
        if p.is_file():
            gotfiles.add(name)
        elif p.is_dir():
            gotdirs.add(name)
        else:
            need(False, ('no special artifact',str(p)))
    need(gotfiles==set(names) and gotdirs==dirs, ('whole files/directories incl exact empties',str(folder)))
    key = (str(folder),tuple(sorted(names)),tuple(sorted(empty)))
    TREES[key] = True


def manifest(folder, names, count, empty=()):
    data = raw(folder/'SHA256SUMS')
    need(data.endswith(b'\n'), 'complete manifest LF')
    rows = {}
    for line in data.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None, ('strict manifest row',str(folder)))
        digest,name = m.groups()
        need(not Path(name).is_absolute() and all(t not in ('','.','..') for t in name.split('/')) and
             name not in rows and name!='SHA256SUMS', ('safe unique nonself manifest',name))
        rows[name] = digest
    need(len(rows)==count and set(rows)==set(names), ('literal complete payload inventory',str(folder)))
    inventory(folder,set(rows)|{'SHA256SUMS'},empty)
    for name,digest in rows.items():
        pin(folder/name,digest)
    return rows


def worker(stage):
    need(stage in STAGES, 'initial stages only')
    return ['/usr/bin/python3.10','-I','-S','-B','-X',
            'pycache_prefix='+str(ATTEMPT/('never_created_'+stage+'_cache')),
            str(WRAPPER),stage,str(BPATH),BINDING_SHA,str(ATTEMPT)]


def epoch(utc):
    need(isinstance(utc,str), 'actual UTC timestamp string')
    value = datetime.fromisoformat(utc)
    need(value.tzinfo==timezone.utc and utc.endswith('+00:00'), 'explicit UTC timestamp')
    return value.timestamp()


def aliases(items):
    result = {}
    for p,wanted in sorted(items.items()):
        actual = pin(p,wanted)
        for name,value in ((p,actual),(actual['resolved'],rich(actual['resolved']))):
            need(name not in result or result[name]==value, ('consistent resolved alias',name))
            result[name] = value
    return result


def check_sample(sample, stage, phase, host, project):
    cwd = CAPSULE if stage=='child01' else ROOT
    cache = ATTEMPT/('never_created_'+stage+'_cache')
    saved_argv = [str(CAPSULE/n) for n in CAPSULE_PINS] if stage=='child01' and phase=='AFTER' else worker(stage)[6:]
    fixed = {'environment':ENV,'cwd':str(cwd),'argv':saved_argv,'interpreter_argv':worker(stage),
        'executable':'/usr/bin/python3.10','sys_path':['/usr/lib/python310.zip','/usr/lib/python3.10','/usr/lib/python3.10/lib-dynload'],
        'flags':FLAGS,'version':'3.10.12 (main, Mar  3 2026, 11:56:32) [GCC 11.4.0]',
        'pycache_prefix':str(cache),'cache_lexists':False,'filesystem_encoding':'utf-8',
        'filesystem_errors':'surrogateescape','default_encoding':'utf-8','preferred_encoding':'UTF-8',
        'LC_CTYPE':'C.UTF-8','stdin_encoding':'utf-8','stdout_encoding':'utf-8','stderr_encoding':'utf-8',
        'scope':SAMPLE_SCOPE,'volatile_proc_maps_not_an_immutable_input':True}
    need(set(sample)==set(fixed)|{'modules','mapped_files','proc_maps','proc_maps_sha256','proc_maps_bytes'} and
         all(type(sample[k]) is type(v) and sample[k]==v for k,v in fixed.items()), ('all sampled settings',stage,phase))
    need(not os.path.lexists(cache), 'current absent exact source-only cache')
    maps = sample['proc_maps'].encode('utf-8')
    need(identity(maps)=={'sha256':sample['proc_maps_sha256'],'bytes':sample['proc_maps_bytes']}, 'entire raw maps identity')
    mapped = {}
    for line in maps.decode('utf-8').splitlines():
        fields = line.split(None,5)
        need(len(fields) in (5,6) and re.fullmatch(r'[0-9a-f]+-[0-9a-f]+',fields[0]) and
             re.fullmatch(r'[r-][w-][x-][ps]',fields[1]) and re.fullmatch(r'[0-9a-f]+',fields[2]) and
             re.fullmatch(r'[0-9a-f]+:[0-9a-f]+',fields[3]) and fields[4].isdigit(), 'each saved maps line syntax')
        if len(fields)==6 and fields[5].startswith('/'):
            need(not fields[5].endswith(' (deleted)'), 'no deleted mapped input')
            p = str(Path(fields[5]).resolve(strict=True))
            need(p in host, ('mapped file only independently frozen host aliases',p))
            mapped[p] = basic(pin(p,host[p]))
    need(mapped==sample['mapped_files'], ('independent exact complete mapped-files reconstruction',stage,phase))
    modules, project_seen = sample['modules'], {}
    need(isinstance(modules,dict), 'saved discrete module table')
    for name,row in modules.items():
        need(isinstance(name,str) and name and set(row)=={'path','sha256','bytes'}, ('entire saved module row',name))
        p = row['path']
        need(Path(p).is_absolute() and str(Path(p).resolve(strict=True))==p and
             not p.endswith(('.pyc','.pyo')), ('resolved source-only module',name))
        if Path(p).is_relative_to(ROOT):
            need(name in project and p==project[name], ('exact registered infrastructure module',name,p))
            project_seen[name] = p
            expected = {'sha256':SOURCE_PINS[p][0],'bytes':SOURCE_PINS[p][1]}
        else:
            need(p in host, ('saved host module outside broad provenance key',name,p))
            expected = basic(host[p])
        need(row=={'path':p,**expected}, ('full saved module identity',name))
        pin(p,expected)
    need(project_seen==project, 'all three exact project module registrations present')
    # No equality to BEFORE, no required all127 host reads, no maps->module-census claim.
    return {'saved_modules':len(modules),'reconstructed_mapped_files':len(mapped),'raw_maps_lines':len(maps.splitlines())}


def check_opens(events, observed, stage, known, host, copies, physical_outputs):
    scientific = stage=='child01'
    cache = ATTEMPT/('never_created_'+stage+'_cache')
    need(isinstance(events,list), 'complete ordered raw open events')
    mask = os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND
    for row in events:
        need(isinstance(row,dict) and set(row)=={'path','mode','flags','writing'} and
             isinstance(row['path'],str) and (row['mode'] is None or isinstance(row['mode'],str)) and
             type(row['flags']) is int and row['flags']>=0 and type(row['writing']) is bool,
             'entire raw event fields, no forbidden process event or omitted writing bit')
        p = Path(row['path'])
        need(p.is_absolute() and str(p)==row['path'] and '..' not in p.parts, 'literal absolute event path')
        need(row['writing']==bool(row['flags']&mask), 'independently reconstructed writing bit')
        need(not row['writing'] or (not scientific and (p==Path('/dev/null') or p.is_relative_to(ATTEMPT))), 'exact write scope')
        need(p.suffix not in ('.pyc','.pyo') or not os.path.lexists(p), 'no inherited bytecode read')
    ordinary, absent, volatile, outputs, devices = {}, [], [], [], {}
    for name in sorted({r['path'] for r in events}):
        p = Path(name)
        if p==Path('/dev/null') and not scientific:
            need(p.is_char_device(), 'actual DEVNULL nonordinary device')
            devices[name] = state(p,False)
        elif name.startswith('/proc/'):
            need(not scientific, 'no child volatile proc read')
            volatile.append(name)
        elif not scientific and p.is_relative_to(ATTEMPT):
            need(name in physical_outputs, ('own attempt I/O is a sealed literal file',name))
            outputs.append(name)
        elif p.is_file():
            resolved = str(p.resolve(strict=True))
            allowed = {**host,**copies} if scientific else known
            need(name in allowed and resolved in allowed, ('ordinary input in correct narrow scope',stage,name))
            if scientific and p.is_relative_to(ROOT):
                need(name in copies and resolved==name, 'child exact two capsule paths only')
            actual = pin(p,allowed[name])
            target = pin(resolved,allowed[resolved])
            need(actual['resolved']==resolved and basic(actual)==basic(target),
                 'ordinary original and resolved identities share exact content')
            ordinary[resolved] = basic(target)
        else:
            need(p.is_relative_to(cache) and not os.path.lexists(p) and not os.path.lexists(cache), 'unique absent cache probe only')
            absent.append(name)
    rebuilt = {'events':events,'ordinary_files':ordinary,'absent_cache_probes':absent,
               'volatile_proc_reads':volatile,'own_attempt_io':outputs,'nonordinary_devices':devices,'scope':OPEN_SCOPE}
    need(observed==rebuilt, ('whole independent open classification, preserves order/duplicates',stage))
    if scientific:
        need(not devices and not volatile and not outputs and set(copies)<=set(ordinary)<=set(host)|set(copies),
             'child exact2 capsule plus only frozen host aliases; delayed Fraction imports allowed')
    return {'raw_events':len(events),'ordinary_files':len(ordinary),'absent_cache_probes':len(absent),
            'volatile_proc_paths':len(volatile),'own_attempt_paths':len(outputs),'devices':len(devices)}


def check_native(folder, label, spec):
    directory = folder/'commands'/label
    entry,native = doc(directory/'ATTEMPT.json'),doc(directory/'RECEIPT.json')
    argv,cwd,timeout = spec
    fixed = {'argv':argv,'cwd':str(cwd),'environment':ENV,'timeout_seconds':timeout,
             'stdin':'DEVNULL','new_owned_session_requested':True}
    need(set(entry)==set(fixed)|{'started_utc','started_epoch','status','exit_code'} and
         all(type(entry[k]) is type(v) and entry[k]==v for k,v in fixed.items()) and
         entry['status']=='ATTEMPTED' and entry['exit_code'] is None, 'whole exact native attempt')
    extra = {'ended_utc','ended_epoch','pid','wrapper_exit_code','spawned','streams_complete',
             'timed_out','interrupted','failure','process_group_settlement','stream_scope','stdout','stderr'}
    need(set(native)==set(entry)|extra and all(native[k]==v for k,v in entry.items() if k not in ('status','exit_code')), 'whole attempt-to-native binding')
    need(native['status']=='COMPLETED' and native['failure'] is None and
         type(native['exit_code']) is type(native['wrapper_exit_code']) is int and
         native['exit_code']==native['wrapper_exit_code']==0 and native['spawned'] is True and
         native['streams_complete'] is True and native['timed_out'] is False and native['interrupted'] is False and
         native['stream_scope']==STREAM_SCOPE, 'actual native full success/complete-stream fields')
    for prefix in ('started','ended'):
        value = native[prefix+'_epoch']
        need(type(value) in (int,float) and math.isfinite(value) and
             abs(epoch(native[prefix+'_utc'])-value)<0.05, 'paired actual UTC/epoch timing')
    need(native['started_epoch']<=native['ended_epoch'], 'ordered finite native interval')
    settlement = native['process_group_settlement']
    need(set(settlement)=={'owned_pgid','owned_sid','signals','remaining_members','quiescent','native_returncode'} and
         type(native['pid']) is int and native['pid']>0 and
         native['pid']==settlement['owned_pgid']==settlement['owned_sid'] and
         settlement['quiescent'] is True and settlement['signals']==[] and
         type(settlement['native_returncode']) is int and settlement['native_returncode']==0, 'owned settled native identity')
    need(isinstance(settlement['remaining_members'],list), 'retained remaining group members')
    for member in settlement['remaining_members']:
        need(set(member)=={'pid','state','ppid','pgid','sid','start_ticks'} and member['state']=='Z' and
             all(type(member[k]) is int for k in ('pid','ppid','pgid','sid','start_ticks')) and
             member['pgid']==member['sid']==native['pid'] and member['pid']>0 and member['start_ticks']>=0,
             'remaining identities may be zombies only, never silently discard')
    for stream in ('stdout','stderr'):
        need(set(native[stream])=={'bytes','sha256'}, 'entire native stream pin')
        need(basic(pin(directory/(stream+'.raw'),native[stream]))==native[stream], 'complete raw native stream pin')
    need(raw(directory/'stderr.raw')==b'', 'all seven actual stderr streams empty')
    if argv[0]=='/usr/bin/cmp':
        need(raw(Path(argv[-2]))==raw(Path(argv[-1])) and raw(directory/'stdout.raw')==b'', 'full source-copy byte equality and empty cmp stdout')
    return {'label':label,**native}


def audit():
    need(sys.argv[1:]==[str(BPATH),BINDING_SHA,str(CAPTURE)] and Path(__file__).resolve()==HERE/'inspect_initial.py', 'literal initial-only receiver source and inputs')
    rich(Path(__file__).resolve())
    pin(BPATH,{'sha256':BINDING_SHA,'bytes':87881})
    pin(CAPTURE,CAPTURE_SHA)
    binding,capture = doc(BPATH),doc(CAPTURE)
    fixed = {'format':'finite-pointer-initial-binding-v1','approved':True,'run_authorized':True,
        'purpose':'FINITE_POINTER_BOUNDED_INITIAL_PILOT','role':'author','mode':'initial',
        'attempt':str(ATTEMPT),'execution_root':str(ATTEMPT.parent),'declared_imports':IMPORTS,
        'local_helper_imports':[],'reviewed_static_source_import_closure':True,
        'reviewed_schema_and_parameters':True,'reviewed_full_runtime_source_lock_and_probe_records':True,
        'success_stderr':'empty','entry':'pointer_pilot.py','parameters':'PARAMETERS.json',
        'argv_template':['$ENTRY','$PARAMETERS'],'parameter_locator':'explicit_absolute_argv',
        'scientific_scope':{'n_values':[1,2,3,4],'total_states':4356},'canonical_adoption_authorized':False,
        'automatic_retry_authorized':False,'strict_pair_authorized':False,'pending':[],
        'timeouts':{'science':300,'native':60,'envelope':900}}
    need(set(binding)==set(fixed)|{'adapter_sources','capsule_files','runtime_lock','canonical','schema',
         'provenance_inputs','root_authorization','root_boundary','root_execution_interface'} and
         all(type(binding[k]) is type(v) and binding[k]==v for k,v in fixed.items()), 'complete exact approved initial binding')
    need(ATTEMPT.parent.resolve(strict=True)==ATTEMPT.parent and ATTEMPT.parent.is_relative_to(QA), 'literal physical execution parent')
    need(all(type(n) is int and 0<n<=3600 for n in binding['timeouts'].values()), 'strict positive prebound integer deadlines')
    canonical = {'path':str(BDIR/'UNADOPTED_CANONICAL.json'),'sha256':None,'bytes':None}
    need(binding['canonical']==canonical and not os.path.lexists(canonical['path']), 'initial unadopted canonical remains absent')
    need(set(binding['adapter_sources'])==set(SOURCE_PINS), 'exact three adapter sources')
    for p,(digest,size) in SOURCE_PINS.items():
        actual = pin(p,{'sha256':digest,'bytes':size})
        need(binding['adapter_sources'][p]==actual, 'full adapter rich source pin')
    need([r['name'] for r in binding['capsule_files']]==list(CAPSULE_PINS), 'literal ordered two-file capsule')
    for row in binding['capsule_files']:
        digest,size = CAPSULE_PINS[row['name']]
        need(row=={'name':row['name'],'path':str(SCIENCE/row['name']),**pin(SCIENCE/row['name'],{'sha256':digest,'bytes':size})}, 'full original capsule pin')
    need(binding['runtime_lock']=={'path':str(LOCK_PATH),**pin(LOCK_PATH,{'sha256':LOCK_SHA,'bytes':146209})}, 'exact prepared runtime lock')
    lock = doc(LOCK_PATH)
    need(lock['format']=='p211-bounded-runtime-lock-v1' and lock['declared_imports']==IMPORTS and
         lock['adapter_variant']=='finite-pointer-initial-v1' and len(lock['files'])==129,
         '129 frozen runtime rows, not broad provenance')
    lock_project = {p:row for p,row in lock['files'].items() if Path(p).is_relative_to(ROOT)}
    need(set(lock_project)=={str(OLD/'p211_runtime.py'),str(OLD/'runtime_core.py')} and
         all(row==binding['adapter_sources'][p] and
             basic(row)=={'sha256':SOURCE_PINS[p][0],'bytes':SOURCE_PINS[p][1]}
             for p,row in lock_project.items()), 'exact two SOURCE_PINS project rows in runtime lock')
    host_files = {p:row for p,row in lock['files'].items() if p not in lock_project}
    need(len(host_files)==127 and all(not Path(p).is_relative_to(ROOT) for p in host_files),
         '127 actual host rows, excluding the two frozen project sources')
    host = aliases(host_files)
    need(all(not Path(p).is_relative_to(ROOT) for p in host), 'resolved host aliases also exclude project paths')
    pin(BDIR/'INPUTS_AT_BINDING.json','7ab9c96459d2e824eacd9c5b889e1be3f45f0da77ec9eddd3f376385d7ec136a')
    key = doc(BDIR/'INPUTS_AT_BINDING.json')
    provenance = {}
    for row in binding['provenance_inputs']:
        need(set(row)=={'path','sha256','bytes','resolved','symlink'} and row['path'] not in provenance, 'unique entire provenance row')
        provenance[row['path']] = {k:v for k,v in row.items() if k!='path'}
    need(key==provenance and len(key)==235, 'whole actual pre-binding provenance key')
    expected = {**lock['files'],**binding['adapter_sources'],str(BPATH):rich(BPATH),str(LOCK_PATH):rich(LOCK_PATH)}
    for row in binding['capsule_files']+binding['provenance_inputs']:
        expected[row['path']] = row
    known = aliases(expected)  # Used for documentary stage keys, NEVER the child host allowlist.
    authorization = binding['root_authorization']
    need(authorization=={'issuer':'/root','record':str(BDIR/'AUTHORIZATION.md'),'record_pin':rich(BDIR/'AUTHORIZATION.md')}, 'actual whole root authorization pin')
    pin(BDIR/'RESULT.json','4cede5e0fb60bdd25380b57dd8f053a9f721a25430b48d5dd3d19ff0b5fe6d31')
    pin(BDIR/'NATIVE01.json','549474d4ced0f188dcd0097dc167f22920e7f7bc96dbb8bc45336ea2568c8e36')
    binding_result,binding_native = doc(BDIR/'RESULT.json'),doc(BDIR/'NATIVE01.json')
    need(binding_result=={'status':'ROOT_EXACT_POINTER_INITIAL_BINDING_READY_NOT_EXECUTED',
         'binding':{'path':str(BPATH),**rich(BPATH)},'attempt':str(ATTEMPT),'runtime_files':129,
         'input_keys':236,'schema_equalities':19,'schema_lengths':9,'scientific_executions':0,'canonical_absent':True}, 'historical actual binding result, not runtime/science acceptance')
    need(binding_native['request']=={'cmd':'/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/finite_pointer_initial_binding01/prepare_binding.py',
         'workdir':str(ROOT),'max_output_tokens':3500} and binding_native['polls']==[] and
         type(binding_native['result']['exit_code']) is int and binding_native['result']['exit_code']==0 and
         json_value(binding_native['result']['output'])==binding_result, 'actual original binding native return')
    config = configuration()
    need(config==lock['configuration'] and loader_scope(config)==lock['loader_search_directory_states'], 'complete current locked configuration and loader scope')
    dev = config['paths']['/dev/null']
    need(dev['is_character_device'] and dev['character_device']['major']==1 and dev['character_device']['minor']==3 and
         not config['paths']['/etc/ld.so.preload']['lexists'] and not config['paths']['/usr/lib/python310.zip']['lexists'] and
         all(not row['lexists'] for p,row in config['paths'].items() if p.endswith(('._pth','/pyvenv.cfg'))), 'DEVNULL and no preload/path-injection configuration')
    stage_names = {s:COMMON|{'commands/'+label+'/'+n for label in LABELS[s] for n in NATIVE_FILES} for s in STAGES}
    stage_names['recorder'] |= {'SOURCE_COPIES.json','CAPSULE_ADDED_INPUTS.json','INPUTS_BEFORE_SCIENCE.json'}|{'capsule/'+n for n in CAPSULE_PINS}
    whole = {s+'/'+n for s in STAGES for n in stage_names[s]|{'SHA256SUMS'}}
    pin(ATTEMPT/'SHA256SUMS',{'sha256':ATTEMPT_SHA,'bytes':7592})
    all_rows = manifest(ATTEMPT,whole,77,('child01/commands',))
    physical_outputs = {str(ATTEMPT/n) for n in whole|{'SHA256SUMS'}}
    copies, source_copies = {}, []
    for row in binding['capsule_files']:
        p = CAPSULE/row['name']
        copies[str(p)] = pin(p,basic(row))
        need(raw(p)==raw(Path(row['path'])), 'entire physical source-copy raw equality')
        source_copies.append({'original':row['path'],'copy':str(p),**basic(copies[str(p)])})
    need(doc(ATTEMPT/'recorder/SOURCE_COPIES.json')==source_copies, 'whole ordered SOURCE_COPIES semantic table')
    project = {'__main__':str(WRAPPER),'_finite_pointer_accepted_runtime':str(OLD/'p211_runtime.py'),'_p211_runtime_core':str(OLD/'runtime_core.py')}
    specs = {'outer':[(worker('launcher'),ROOT,900)],'launcher':[(worker('recorder'),ROOT,900)],'child01':[],
        'recorder':[(['/usr/bin/cmp','--',row['path'],str(CAPSULE/row['name'])],ROOT,60) for row in binding['capsule_files']]+
        [(['/usr/bin/ldd']+lock['ldd_targets'],ROOT,60),(worker('child01'),CAPSULE,300),(['/usr/bin/ldd']+lock['ldd_targets'],ROOT,60)]}
    results, entered, commands, samples, opens, counts = {}, {}, {}, {}, {}, {}
    for stage in STAGES:
        folder = ATTEMPT/stage
        counts[stage] = len(manifest(folder,stage_names[stage],{'outer':14,'launcher':14,'recorder':35,'child01':10}[stage],('commands',) if stage=='child01' else ()))
        result,entry = doc(folder/'RESULT.json'),doc(folder/'ENTERED.json')
        results[stage],entered[stage] = result,entry
        result_fixed = {'stage':stage,'role':'author','mode':'initial','status':'PASS','errors':[],
                        'wrapper_return':0,'unknown_descendant_closure':False,'unfinalized_native':[],'scope':RESULT_SCOPE}
        need(set(result)==set(result_fixed)|{'commands','output'} and all(type(result[k]) is type(v) and result[k]==v for k,v in result_fixed.items()), ('entire closed actual stage result',stage))
        cwd = CAPSULE if stage=='child01' else ROOT
        need(entry=={'stage':stage,'argv':worker(stage)[6:],'orig_argv':worker(stage),'cwd':str(cwd),
             'environment':ENV,'cache':str(ATTEMPT/('never_created_'+stage+'_cache')),'started_utc':entry['started_utc'],
             'status':'ENTERED_NOT_NATIVE_PRESPAWN'}, ('complete actual entered record',stage))
        start = epoch(entry['started_utc'])
        before = {**known,**copies} if stage=='child01' else known
        after = {**before,**copies} if stage=='recorder' else before
        need(doc(folder/'INPUTS_BEFORE.json')==before and doc(folder/'INPUTS_AFTER.json')==after, 'whole stage input keys exactly reconstructed')
        if stage=='recorder':
            need(doc(folder/'CAPSULE_ADDED_INPUTS.json')==copies and doc(folder/'INPUTS_BEFORE_SCIENCE.json')==after, 'entire pre-science copied-file key')
        samples[stage] = {}
        for phase in ('BEFORE','AFTER'):
            need(doc(folder/('CONFIGURATION_'+phase+'.json'))==config, 'entire saved configuration snapshot')
            samples[stage][phase] = check_sample(doc(folder/('RUNTIME_'+phase+'.json')),stage,phase,host,project)
        opens[stage] = check_opens(doc(folder/'OPEN_EVENTS_RAW.json'),doc(folder/'OPEN_OBSERVATIONS.json'),stage,after,host,copies,physical_outputs)
        commands[stage] = [check_native(folder,label,spec) for label,spec in zip(LABELS[stage],specs[stage])]
        need(result['commands']==commands[stage] and len(commands[stage])==len(LABELS[stage]), 'all exact ordered native records and aggregate equality')
        last = start
        for command in commands[stage]:
            need(last<=command['started_epoch']<=command['ended_epoch'], 'entered/native sequential temporal ordering')
            last = command['ended_epoch']
    for parent,child in (('outer','launcher'),('launcher','recorder')):
        native = commands[parent][0]
        closure = {'status':'PASS','payloads':counts[child],'manifest':rich(ATTEMPT/child/'SHA256SUMS')}
        need(results[parent]['output']=={'child_stage':child,'native_receipt':native,'closed_child':closure}, 'whole nested native/closed-stage relation')
        need(native['started_epoch']<=epoch(entered[child]['started_utc'])<=native['ended_epoch'] and
             all(native['started_epoch']<=r['started_epoch']<=r['ended_epoch']<=native['ended_epoch'] for r in commands[child]), 'complete nested child timing containment')
    child_native = commands['recorder'][3]
    need(child_native['started_epoch']<=epoch(entered['child01']['started_utc'])<=child_native['ended_epoch'], 'actual scientific child entered inside its native command')
    for label in ('01_ldd_before','06_ldd_after'):
        data = raw(ATTEMPT/'recorder/commands'/label/'stdout.raw')
        need(b'not found' not in data, 'no unresolved linkage')
        paths = sorted({os.fsdecode(p) for p in re.findall(rb'(/[^\s()]+)',data) if Path(os.fsdecode(p)).is_file()})
        need(paths==lock['ldd_paths'] and all(p in host for p in paths), 'complete raw ldd frozen host membership')
        for p in paths:
            pin(p,host[p])
    opaque = basic(pin(OPAQUE_STDOUT,{'bytes':10366275,'sha256':'45dc800a60a2d26da492a528f4a54c9a94a755338f598e8ccc161a9d719bb2b1'}))
    need(results['recorder']['output']=={'mode':'initial','raw_stdout':[{'path':str(OPAQUE_STDOUT),**opaque}],
         'canonical_policy':'initial stdout requires separate root acceptance/publication; pair never adopts or replaces canonical',
         'actual_raw_comparisons':0} and child_native['stdout']==opaque, 'exact sole opaque scientific stdout locator/pin; zero canonical comparisons')
    need(results['child01']['output']=={'scientific_argv':[str(CAPSULE/n) for n in CAPSULE_PINS],
         'parameter_locator':'explicit_absolute_argv','scientific_outcome':'SYSTEM_EXIT_ZERO',
         'source':copies[str(CAPSULE/'pointer_pilot.py')],'cwd':str(CAPSULE)}, 'actual root-reviewed pointer compile/exec interface/outcome only')
    need(set(capture)=={'request','result','polls'}, 'complete actual product envelope fields')
    launch = ['/usr/bin/env','-i']+[k+'='+v for k,v in ENV.items()]+worker('outer')
    need(capture['request']=={'cmd':' '.join(launch),'workdir':str(ROOT),'yield_time_ms':1000,'max_output_tokens':3500}, 'whole actual product command/cwd/options')
    parts, session = [capture['result']], capture['result'].get('session_id')
    for poll in capture['polls']:
        need(session is not None and poll['request']=={'session_id':session,'chars':'','yield_time_ms':1000,'max_output_tokens':4500}, 'exact actual read-only product poll chain')
        parts.append(poll['result'])
        session = poll['result'].get('session_id')
    need(type(parts[-1]['exit_code']) is int and parts[-1]['exit_code']==0 and session is None and
         all('exit_code' not in p for p in parts[:-1]), 'actual completed product native exit, no invented initial exit')
    messages = [json_value(line) for line in ''.join(p['output'] for p in parts).splitlines()]
    need(messages and all(set(row)=={'status','label','pid','timeout_seconds'} and row['status']=='P211_OWNED_NATIVE_RUNNING' for row in messages[:-1]), 'unchanged core progress literal only')
    need(messages[-1]=={'attempt':str(ATTEMPT),'seal':{'manifest':basic(rich(ATTEMPT/'SHA256SUMS')),'payloads':77},'status':'PASS'}, 'whole actual product control and physical seal relation')
    need(not os.path.lexists(canonical['path']) and not os.path.lexists(ATTEMPT/'child02') and
         all(not os.path.lexists(ATTEMPT/('never_created_'+s+'_cache')) for s in STAGES+('child02',)), 'no canonical/pair/unused cache creation')
    need(configuration()==config and loader_scope(config)==lock['loader_search_directory_states'], 'final whole configuration/membership/loader closure')
    before = dict(READS)
    after = {p:rich(p) for p in sorted(before)}
    need(before==after, 'entire current receiver read key unchanged, opaque stdout streaming only')
    for (folder,names,empty) in list(TREES):
        inventory(Path(folder),names,empty)
    need(str(OPAQUE_STDOUT) not in RAW_READS, 'scientific output body never consumed by raw/JSON route')
    return {'status':'PASS_POINTER_INITIAL_RUNTIME_RECORDS_ONLY_SCIENTIFIC_OUTPUT_UNREAD',
        'binding':{'path':str(BPATH),**rich(BPATH)},'attempt':str(ATTEMPT),'checks':CHECKS,
        'complete_payloads':77,'complete_files':78,'complete_manifest':basic(rich(ATTEMPT/'SHA256SUMS')),
        'stage_payloads':counts,'native_commands':sum(map(len,commands.values())),
        'received_scientific_native_commands':1,'received_canonical_comparisons':0,
        'frozen_runtime_lock_rows':len(lock['files']),'frozen_project_source_rows':len(lock_project),
        'frozen_host_file_rows':len(host_files),'host_resolved_alias_entries':len(host),'stage_samples':samples,'stage_opens':opens,
        'scientific_stdout_opaque_pin':{'path':str(OPAQUE_STDOUT),**opaque},
        'receiver_read_paths':len(before),'READ_INPUTS_BEFORE':before,'READ_INPUTS_AFTER':after,
        'scientific_output_nonhash_body_reads':0,'scientific_output_json_parses':0,'producer_invocations_in_this_audit':0,
        'scientific_output_semantics':'NOT_RECEIVED; separate saved-output reception and same-reviewer gate remain',
        'module_census_basis':'Pinned core102-123 complete sys.modules loop plus saved discrete table; no independent raw sys.modules census exists; maps reconstruct mapped files only.',
        'scope':'Initial-only bounded runtime documentary reception; no scientific recomputation, mathematical PASS, gate change, admission, or hermetic/continuous/OS tracing claim.',
        'paper_complete':False,'external':'HOLD_EXTERNAL'}


if __name__=='__main__':
    try:
        outcome = audit()
    except BaseException:
        print(json.dumps({'status':'FAIL_POINTER_INITIAL_RUNTIME_RECEIPT_PRESERVE_ORIGINALS',
                          'checks':CHECKS,'traceback':traceback.format_exc(),'READ_INPUTS_PARTIAL':READS,
                          'producer_invocations_in_this_audit':0,'scientific_output_json_parses':0},sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(outcome,sort_keys=True))
