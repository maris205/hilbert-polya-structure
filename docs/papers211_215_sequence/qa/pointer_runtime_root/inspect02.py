"""Root full runtime-preparation reception; no project import or science.

Explicitly reuses accepted rich/state conventions, adds exact native request,
probe closure and full current 129-file/configuration reception. The separate
old documentary checker replay is disclosed, not a new independent runtime
probe. Every scientific source file remains outside this reader's scope.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
PREP = QA/'finite_pointer_runtime_preparation01'
HERE = QA/'pointer_runtime_root'
OUT = HERE/'run02'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
READS = {}
CHECKS = 0


def need(ok, why):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(why)


def read(path):
    p = Path(path)
    need(p.name not in ('pointer_pilot.py','PARAMETERS.json','verify.py'), 'no scientific-source read')
    raw = p.read_bytes()
    key = {'bytes':len(raw),'sha256':sha256(raw).hexdigest(),
           'resolved':str(p.resolve(strict=True)), 'symlink':os.readlink(p) if p.is_symlink() else None}
    need(str(p) not in READS or READS[str(p)] == key, ('full unchanged read',str(p)))
    READS[str(p)] = key
    return raw


def check_pin(path, expected):
    read(path)
    need(all(READS[str(Path(path))][k] == expected[k] for k in ('bytes','sha256','resolved','symlink') if k in expected),
         ('entire supplied rich pin',str(path)))


def obj(path):
    return json.loads(read(path))


def state(path, with_bytes=True):
    p = Path(path)
    row = {'lexists':os.path.lexists(p),'exists':p.exists(),'is_file':p.is_file(),
           'is_dir':p.is_dir(),'is_character_device':p.is_char_device(),
           'resolved':str(p.resolve()),'symlink':os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        st = p.stat()
        row['character_device'] = {'major':os.major(st.st_rdev),'minor':os.minor(st.st_rdev),'mode':st.st_mode}
    if with_bytes and p.is_file():
        read(p)
        row.update({k:READS[str(p)][k] for k in ('bytes','sha256')})
    return row


def seal(base, name, count):
    raw = read(base/name)
    need(raw.endswith(b'\n'), 'complete seal')
    names = []
    for line in raw.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None, 'exact manifest syntax')
        h, f = m.groups()
        need(f not in names and f != name and not Path(f).is_absolute() and '..' not in Path(f).parts, 'safe nonself name')
        check_pin(base/f, {'sha256':h})
        names.append(f)
    actual, dirs = set(), {'.'}
    for p in base.rglob('*'):
        need(p.resolve() == p and (p.is_file() or p.is_dir()), 'whole ordinary physical tree')
        (dirs if p.is_dir() else actual).add(p.relative_to(base).as_posix())
    need(actual == set(names)|{name} and len(names) == count, 'complete exact payload inventory')
    return names, sorted(dirs)


need(Path.cwd() == ROOT and not OUT.exists(), 'exclusive root reception')
read(__file__)
check_pin(PREP/'MANIFEST.sha256', {'bytes':6521,'sha256':'bb71a0b54f367f3c1116263081f06f37817677ed334788c1b1950227ba1f07f7'})
all_names, all_dirs = seal(PREP,'MANIFEST.sha256',64)
need(sum(READS[str(PREP/n)]['bytes'] for n in all_names) == 892846, 'complete preparation payload bytes')
source_pins = {
    PREP/'pointer_runtime.py':'89bec42ec8ae827156ac32cd0c8213faef06387930152bee6b1be3a37e4e92bf',
    PREP/'import_probe.py':'c0093d9401328acebfa73a3403ca94a7590ee27bb9ffb52c6bddd69fe6d9a7be',
    PREP/'prepare_runtime02.py':'2e139bcdd7ee5208036ad32e9696ba0af1e55a7c896a93e6e5c6ee58908d24d9',
    QA/'p211_runtime_preparation/runtime_core.py':'2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934',
    QA/'p211_runtime_preparation/p211_runtime.py':'bff2dcf25ee846b04eac0bbd46eb7b3e58c728c6d7e8e9ce591c9cef1ae4e421'}
for path, h in source_pins.items():
    check_pin(path, {'sha256':h})
expected_revision = read(PREP/'prepare_runtime.py').decode().replace(
    "'prepare_runtime.py')", "'prepare_runtime02.py')").replace(
    "HERE / 'REQUEST.json'", "HERE / 'REQUEST02.json'").replace(
    "    '/usr/lib/x86_64-linux-gnu/libmpdec.so.3',\n",
    "    '/usr/lib/x86_64-linux-gnu/libmpdec.so.3',\n    '/usr/lib/python3.10/encodings/ascii.py',  # discovery01 map-reader dependency; root-authorized prefix\n")
need(expected_revision.encode() == read(PREP/'prepare_runtime02.py'), 'whole exact forward-only controller diff')
revision = obj(PREP/'REVISION02_NATIVE.json')
need(revision['result']['exit_code'] == 1 and revision['result']['output'].startswith(
    source_pins[PREP/'prepare_runtime02.py']+'  docs/papers211_215_sequence/qa/finite_pointer_runtime_preparation01/prepare_runtime02.py\n11604 '),
    'preserved actual revision output, ordinary diff exit1; original request absent in this envelope')
old_lock = obj(QA/'p211_runtime_preparation/discovery02/RUNTIME_LOCK.json')
check_pin(QA/'p211_runtime_preparation/discovery02/RUNTIME_LOCK.json', {'sha256':'1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab'})
lock = obj(PREP/'discovery02/RUNTIME_LOCK.json')
check_pin(PREP/'discovery02/RUNTIME_LOCK.json', {'bytes':146209,'sha256':'e2fd2189f639feff28a8ae499da011e9ea6e9cadf3eb99b60944f3209fdebd02'})
need(len(lock['files']) == 129 and len(old_lock['files']) == 122
     and all(lock['files'][p] == k for p,k in old_lock['files'].items()), 'all old runtime keys retained')
additions = set(lock['files'])-set(old_lock['files'])
need(additions == {'/usr/lib/python3.10/fractions.py','/usr/lib/python3.10/decimal.py',
    '/usr/lib/python3.10/numbers.py','/usr/lib/python3.10/encodings/ascii.py',
    '/usr/lib/python3.10/lib-dynload/_decimal.cpython-310-x86_64-linux-gnu.so',
    '/usr/lib/x86_64-linux-gnu/libmpdec.so.3','/usr/lib/x86_64-linux-gnu/libmpdec.so.2.5.1'}, 'exact seven new lexical/resolved runtime keys')
native_count, receipt_rows, seals = 0, [], {}
for index, count in [(1,19),(2,25)]:
    base = PREP/('discovery%02d'%index)
    names, dirs = seal(base,'SHA256SUMS',count)
    seals[index] = names
    request = obj(PREP/('REQUEST.json' if index == 1 else 'REQUEST02.json'))
    tool = obj(PREP/('DISCOVERY%02d_NATIVE.json'%index))
    result = obj(base/'RESULT.json')
    need(tool['request']['cmd'] == ' '.join(request['native_argv'])
         and tool['request']['workdir'] == str(ROOT) and tool['result']['exit_code'] == (1 if index == 1 else 0),
         'entire actual documentary controller command/exit')
    actual = json.loads(tool['result']['output'])
    need(actual == {'status':result['status'],'errors':result['errors'],'output':str(base),
                   'seal':{'payloads':count,'manifest':{k:READS[str(base/'SHA256SUMS')][k] for k in ('bytes','sha256')}}},
         'whole actual outer result, including preserved failure')
    for p, k in request['frozen_sources'].items():
        check_pin(p,k)
    control = obj(base/'CONTROLLER_SETTINGS.json')
    need(control['orig_argv'] == request['argv'] and control['environment'] == ENV
         and control['cwd'] == str(ROOT), 'actual frozen controller settings')
    before = obj(base/'RUNTIME_INPUTS_BEFORE.json')
    need(len(before) == 135+index, 'complete pre-frozen key population')
    for stem in ('RUNTIME_INPUTS','CONFIGURATION','LOADER_DIRECTORIES'):
        need(read(base/(stem+'_BEFORE.json')) == read(base/(stem+'_AFTER.json')), 'complete saved raw prepost equality')
    for p,k in before.items():
        check_pin(p,k)
    for p,k in obj(base/'SOURCE_INPUTS_BEFORE.json').items():
        need(before[p] == k, 'all documentary sources prefrozen')
    probe_request = obj(base/'PROBE_REQUEST.json')
    probe = obj(base/'commands/02_named_import_probe/stdout.raw')
    argv = ['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(base/'never_created_probe_cache'),
            str(PREP/'import_probe.py'),str(base/'never_created_probe_cache'),str(base/'empty_probe_capsule')]
    need(probe_request['argv'] == probe['orig_argv'] == argv and probe['argv'] == argv[6:]
         and probe['cwd'] == str(base/'empty_probe_capsule') and probe['environment'] == ENV
         and probe['scientific_executions'] == 0 and probe['science_source_reads'] == []
         and probe['status'] == 'IMPORT_ONLY_NO_SCIENCE' and probe['cache_absent'] is True,
         'complete literal named-import probe interface and finite scope')
    need(probe['declared_imports'] == ['sys','json','collections.Counter','fractions.Fraction','itertools.product','math.factorial'],
         'exact named imports, not a scientific invocation')
    need(probe['sys_path'] == ['/usr/lib/python310.zip','/usr/lib/python3.10','/usr/lib/python3.10/lib-dynload']
         and probe['encodings'] == {'default':'utf-8','filesystem':'utf-8','filesystem_errors':'surrogateescape',
                                   'stdin':'utf-8','stdout':'utf-8','stderr':'utf-8'}, 'actual source-only paths and encodings')
    expected_labels = ['01_ldd_before','02_named_import_probe']+(['03_ldd_after'] if index == 2 else [])
    need([r['label'] for r in result['commands']] == expected_labels, 'entire exact native operation census')
    for row in result['commands']:
        folder = base/'commands'/row['label']
        receipt, attempted = obj(folder/'RECEIPT.json'), obj(folder/'ATTEMPT.json')
        need(receipt == {k:v for k,v in row.items() if k != 'label'}, 'whole actual command receipt')
        need(all(receipt[k] == v for k,v in attempted.items() if k not in ('status','exit_code')), 'complete attempted-to-actual correspondence')
        expected_argv = argv if row['label'] == '02_named_import_probe' else ['/usr/bin/ldd']+lock['ldd_targets']
        expected_cwd = str(base/'empty_probe_capsule') if row['label'] == '02_named_import_probe' else str(ROOT)
        need(receipt['argv'] == expected_argv and receipt['cwd'] == expected_cwd
             and receipt['environment'] == ENV and receipt['timeout_seconds'] == 60
             and receipt['stdin'] == 'DEVNULL' and receipt['new_owned_session_requested'] is True
             and receipt['status'] == 'COMPLETED' and receipt['exit_code'] == receipt['wrapper_exit_code'] == 0
             and receipt['streams_complete'] is True and receipt['spawned'] is True
             and receipt['failure'] is None and not receipt['interrupted'] and not receipt['timed_out']
             and receipt['started_epoch'] <= receipt['ended_epoch'], 'all native request/settled-success fields')
        settlement = receipt['process_group_settlement']
        need(settlement['quiescent'] is True and settlement['signals'] == []
             and settlement['owned_pgid'] == settlement['owned_sid'] == receipt['pid']
             and settlement['native_returncode'] == 0 and all(r['state'] == 'Z' for r in settlement['remaining_members']), 'full owned-group settlement')
        for stream in ('stdout','stderr'):
            check_pin(folder/(stream+'.raw'),receipt[stream])
        need(read(folder/'stderr.raw') == b'', 'actual empty native stderr')
        if row['label'] != '02_named_import_probe':
            raw = read(folder/'stdout.raw')
            linked = sorted({os.fsdecode(p) for p in re.findall(rb'(/[^\s()]+)',raw) if Path(os.fsdecode(p)).is_file()})
            need(b'not found' not in raw and linked == lock['ldd_paths'], 'complete actual linkage membership')
            for p in linked:
                need(p in before, 'all native ELF inputs prefrozen')
                check_pin(p,before[p])
        native_count += 1
        receipt_rows.append({'attempt':index,'label':row['label'],'receipt_key':READS[str(folder/'RECEIPT.json')]})
    observed = set()
    for m in probe['modules'].values():
        if m['file']:
            need(not m['file'].endswith(('.pyc','.pyo')), 'no loaded bytecode')
            observed.add(str(Path(m['file']).resolve(strict=True)))
    mapped, absent, volatile = set(), [], []
    for line in probe['proc_maps'].splitlines():
        fields = line.split(None,5)
        if len(fields) == 6 and fields[5].startswith('/'):
            need(not fields[5].endswith(' (deleted)'), 'no deleted map')
            mapped.add(str(Path(fields[5]).resolve(strict=True)))
    observed |= mapped
    for event in probe['audit_events']:
        need(event['event'] in ('open','import'), 'only recorded named import/open events')
        if event['event'] != 'open':
            continue
        p = Path(event['path'])
        need(p.is_absolute() and not event['flags'] & (1|2|64|512|1024), 'absolute read-only probe open')
        if str(p) == '/proc/self/maps':
            volatile.append(str(p))
        elif p.is_file():
            observed.add(str(p.resolve(strict=True)))
        else:
            need(p.is_relative_to(base/'never_created_probe_cache') and not os.path.lexists(p), 'absent cache probe only')
            absent.append(str(p))
    missing = observed-set(before)
    need(missing == ({'/usr/lib/python3.10/encodings/ascii.py'} if index == 1 else set()), 'exact original failure versus new registered closure')
    if index == 2:
        closure = obj(base/'OBSERVED_CLOSURE.json')
        need(closure == {'ordinary_files':{p:before[p] for p in sorted(observed)},'mapped_files':sorted(mapped),
                        'absent_cache_opens':absent,'volatile_reads':volatile,
                        'new_vs_old122_keys':sorted(set(before)-set(old_lock['files'])),
                        'all_observed_files_prefrozen':True,'unregistered_observed_files':[]}, 'every complete observed closure field')
        source_before = obj(base/'SOURCE_INPUTS_BEFORE.json')
        need(lock['files'] == {p:k for p,k in before.items() if p not in source_before or p in old_lock['files']}, 'entire runtime/provenance split')
    else:
        need(len(result['errors']) == 1 and 'encodings/ascii.py' in result['errors'][0]['error'], 'sole failure remains disclosed')
    need(not os.path.lexists(base/'never_created_probe_cache') and not os.path.lexists(base/'never_created_preparer_cache'), 'cache remains absent')
need(native_count == 5, 'exact total five documentary commands')
for p,k in lock['files'].items():
    check_pin(p,k)
need(lock['configuration'] == old_lock['configuration'] and lock['loader_search_directory_states'] == old_lock['loader_search_directory_states'], 'complete unchanged configuration keys')
for p,k in lock['configuration']['paths'].items():
    need(state(p) == k, ('entire current configuration path',p))
for d,k in lock['configuration']['memberships'].items():
    p = Path(d)
    actual = {'directory':state(p,False),'members':{q.name:state(q,False) for q in sorted(p.iterdir())} if p.is_dir() else {}}
    need(actual == k, ('entire current membership',d))
for p,k in lock['loader_search_directory_states'].items():
    need(state(p,False) == k, ('entire current loader directory',p))
closure_commands = obj(PREP/'CLOSURE_NATIVE_CHECKS.json')
need(len(closure_commands) == 8, 'all additional native hash/cmp records')
for record in closure_commands:
    need(record['result']['exit_code'] == 0 and not record['result'].get('session_id'), 'settled additional native check')
    cmd = record['request']['cmd']
    if cmd == '/usr/bin/sha256sum -c SHA256SUMS':
        base = Path(record['request']['workdir'])
        index = int(base.name[-2:])
        need(record['result']['output'] == ''.join(n+': OK\n' for n in seals[index]), 'every actual native hash line')
    else:
        parts = cmd.split()
        need(parts[:2] == ['/usr/bin/cmp','--'] and len(parts) == 4 and record['result']['output'] == '', 'literal actual cmp record')
        p,q = (Path(x) if Path(x).is_absolute() else Path(record['request']['workdir'])/x for x in parts[2:])
        need(p.is_relative_to(PREP) and q.is_relative_to(PREP) and read(p) == read(q), 'whole actual compared raw pair')
old_audit = obj(PREP/'ARTIFACT_INSPECTION_NATIVE.json')
new_audit = obj(HERE/'REUSED_DOCUMENTARY_CHECK_NATIVE01.json')
need(old_audit['result']['exit_code'] == new_audit['result']['exit_code'] == 0
     and old_audit['result']['output'] == new_audit['result']['output'], 'entire actual reused documentary-check output, not only counts')
pending = obj(PREP/'BINDING.pending.json')
need(pending['approved'] is False and pending['run_authorized'] is False and pending['attempt'] is None
     and pending['execution_root'] is None and all(pending[k] is False for k in
         ('reviewed_static_source_import_closure','reviewed_schema_and_parameters','reviewed_full_runtime_source_lock_and_probe_records',
          'canonical_adoption_authorized','automatic_retry_authorized','strict_pair_authorized')), 'all pending scientific authority remains disabled')
for p,k in dict(READS).items():
    check_pin(p,k)
result = {'status':'PASS_ROOT_RUNTIME_PREPARATION_RECEPTION_NO_SCIENCE', 'checks':CHECKS,'read_paths':len(READS),
          'preparation_payloads':64,'preparation_payload_bytes':892846,'runtime_keys':129,'old_runtime_keys':122,
          'added_runtime_keys':sorted(additions),'native_documentary_commands':5,'additional_native_checks':8,
          'discovery01_failure_preserved':True,'runtime_wrapper_executed':False,'scientific_executions':0,
          'root_binding_created':False,'admitted':False,'directory_inventory':all_dirs,
          'metadata_limits':['SOURCE_FREEZE_NATIVE and REVISION02_NATIVE preserve result but not original request object; LOCK_SUMMARY_NATIVE is result-only. No missing historical request is invented.'],
          'reused_documentary_checker_scope':'Actual unchanged 1441-check output; no new import probe or scientific run.'}
OUT.mkdir()
for n,v in [('RESULT.json',result),('READ_INPUTS.json',READS),('NATIVE_COMMAND_KEYS.json',receipt_rows)]:
    with (OUT/n).open('x') as stream:
        json.dump(v,stream,sort_keys=True,indent=2);stream.write('\n')
print(json.dumps(result,sort_keys=True))
