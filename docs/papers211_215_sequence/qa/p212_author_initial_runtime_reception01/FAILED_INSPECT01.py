"""Root P212 full initial execution reception; disclosed forward adaptation of\naccepted P211 inspect_production.py. No submitted source is executed.\nAdds actual root-capture reception, full sampled fields, exact selected\nFraction opens, raw proc-map reconstruction and source-lineage pins.\n"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
PREP = QA/'p212_runtime_preparation01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
CHECKS, READS, STATE_KEY = 0, {}, {}
OWN = QA/'p212_author_initial_runtime_reception01'
SOURCE = Path(__file__).resolve()
OLD_SOURCE = QA/'p211_runtime_root_reception/inspect_production.py'


def need(condition, detail):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail)


def raw(path):
    path = Path(path)
    need(path.is_file(), ('file', str(path)))
    data = path.read_bytes()
    if str(path) in READS:
        need(data == READS[str(path)], ('unchanged reread', str(path)))
    READS[str(path)] = data
    return data


def identity(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def rich(path):
    path = Path(path)
    return {**identity(raw(path)), 'resolved': str(path.resolve(strict=True)),
            'symlink': os.readlink(path) if path.is_symlink() else None}


def pin(path, expected):
    actual = rich(path)
    expected = {'sha256': expected} if isinstance(expected, str) else expected
    need(all(actual[k] == expected[k] for k in actual if k in expected), ('exact file pin', str(path)))
    return actual


def unique(items):
    result = {}
    for key, value in items:
        need(key not in result, ('duplicate JSON key', key))
        result[key] = value
    return result


def doc(path):
    return json.loads(raw(path), object_pairs_hook=unique)


def manifest(folder):
    data = raw(folder/'SHA256SUMS')
    need(data.endswith(b'\n'), 'complete manifest LF')
    rows = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, ('manifest syntax', str(folder)))
        digest, name = match.groups()
        p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and name not in rows and name != 'SHA256SUMS', ('safe manifest path', name))
        rows[name] = digest
    actual, directories, wanted_directories = set(), {'.'}, {'.'}
    for p in folder.rglob('*'):
        need(not p.is_symlink(), ('physical artifact', str(p)))
        if p.is_file():
            actual.add(p.relative_to(folder).as_posix())
        else:
            need(p.is_dir(), ('no special artifact entry', str(p)))
            directories.add(p.relative_to(folder).as_posix())
    for name in rows:
        wanted_directories.update(str(p) for p in Path(name).parents)
    if folder.name.startswith('child'):
        wanted_directories.add('commands')
    if folder == attempt:
        wanted_directories.update(s+'/commands' for s in stages if s.startswith('child'))
    need(directories == wanted_directories, ('complete directory inventory including exact empty command scopes', str(folder)))
    need(actual == set(rows) | {'SHA256SUMS'}, ('complete artifact inventory', str(folder)))
    for name, digest in rows.items():
        pin(folder/name, digest)
    return rows


def state(path, with_bytes=True):
    p = Path(path)
    row = {'lexists': os.path.lexists(str(p)), 'exists': p.exists(),
           'is_file': p.is_file(), 'is_dir': p.is_dir(), 'is_character_device': p.is_char_device(),
           'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        stat = p.stat()
        row['character_device'] = {'major': os.major(stat.st_rdev), 'minor': os.minor(stat.st_rdev), 'mode': stat.st_mode}
    if with_bytes and p.is_file():
        row.update(identity(raw(p)))
    key = str(p)+('|bytes' if with_bytes else '|metadata')
    if key in STATE_KEY:
        need(STATE_KEY[key]['state'] == row, ('stable repeated complete state', key))
    STATE_KEY[key] = {'path':str(p), 'with_bytes':with_bytes, 'state':row}
    return row


def complete_sample(sample, stage, phase, known, wanted_argv, cwd, capsule):
    discovery = doc(QA/'p212_runtime_discovery01/commands/02_probe_child/stdout.raw')['sample']
    need(set(sample) == set(discovery), 'all sampled fields accounted')
    excluded = {'argv','interpreter_argv','cwd','pycache_prefix','cache_lexists','modules',
                'mapped_files','proc_maps','proc_maps_bytes','proc_maps_sha256'}
    need({k:v for k,v in sample.items() if k not in excluded} ==
         {k:v for k,v in discovery.items() if k not in excluded}, 'whole stable discovered settings/flags/encoding scope')
    wanted_app = [str(capsule/'verify.py'),'--parameters',str(capsule/'PARAMETERS.json')] if stage.startswith('child') and phase == 'AFTER' else wanted_argv[6:]
    need(sample['argv'] == wanted_app, 'entire actual per-phase application argv')
    wanted_modules = dict(discovery['modules'])
    wanted_maps = dict(discovery['mapped_files'])
    if not (stage.startswith('child') and phase == 'AFTER'):
        for name in ('fractions','decimal','numbers','_decimal'):
            del wanted_modules[name]
        for p in ('/usr/lib/python3.10/lib-dynload/_decimal.cpython-310-x86_64-linux-gnu.so',
                  '/usr/lib/x86_64-linux-gnu/libmpdec.so.2.5.1'):
            del wanted_maps[p]
    need(sample['modules'] == wanted_modules and sample['mapped_files'] == wanted_maps,
         'whole actual module/map role sets against accepted discovery, preimport delta explicit')
    mapped = set()
    for line in sample['proc_maps'].splitlines():
        m = re.fullmatch(r'([0-9a-f]+)-([0-9a-f]+)\s+([rwxps-]{4})\s+([0-9a-f]+)\s+([0-9a-f]+:[0-9a-f]+)\s+(\d+)(?:\s+(.*))?', line)
        need(m is not None and int(m[2],16)>int(m[1],16), 'entire original proc-map row')
        name = m[7]
        if name and name.startswith('/'):
            need(not name.endswith(' (deleted)'), 'no deleted actual file map')
            mapped.add(str(Path(name).resolve(strict=True)))
    need(mapped == set(sample['mapped_files']), 'all actual file-backed proc-map roles')
    need(all(p in known for p in mapped), 'all mapped files preaccepted')


def complete_opens(observed, known, stage, attempt, cache, capsule):
    ordinary, absent, volatile, outputs, devices = {}, [], [], [], {}
    scientific = stage.startswith('child')
    for event in observed['events']:
        need(set(event) == {'path','mode','flags','writing'}, 'every event field known')
        need(type(event['flags']) is int and type(event['writing']) is bool, 'typed actual open flags')
        need(event['writing'] == bool(event['flags'] & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND)), 'whole actual writing classification')
        p = Path(event['path'])
        need(p.is_absolute(), 'actual absolute open event')
        need(not scientific or not event['writing'], 'no scientific ordinary write')
        need(not event['writing'] or p == Path('/dev/null') or p.is_relative_to(attempt), 'exact infrastructure output scope')
    for name in sorted({v['path'] for v in observed['events']}):
        p = Path(name)
        if p == Path('/dev/null') and not scientific:
            devices[name] = state(p,False)
        elif name.startswith('/proc/'):
            need(not scientific, 'no scientific volatile read');volatile.append(name)
        elif not scientific and p.is_relative_to(attempt):
            outputs.append(name)
        elif p.is_file():
            resolved = str(p.resolve(strict=True))
            need(resolved in known, 'every actual ordinary open prefrozen')
            pin(p,known[resolved])
            need(not scientific or not p.is_relative_to(ROOT) or resolved in {str(capsule/n) for n in ('verify.py','PARAMETERS.json')}, 'scientific project read only own capsule')
            ordinary[resolved] = identity(raw(p))
        else:
            need(p.is_relative_to(cache) and not os.path.lexists(p) and not os.path.lexists(cache), 'only absent source-cache probe')
            absent.append(name)
    need(observed == {'events':observed['events'],'ordinary_files':ordinary,'absent_cache_probes':absent,
        'volatile_proc_reads':volatile,'own_attempt_io':outputs,'nonordinary_devices':devices,
        'scope':'Post-hook Python opens and discrete file-backed maps/modules; not OS/startup/escaped-descendant tracing.'}, 'entire open-observation map reconstructed')


need(len(sys.argv) == 4, 'BINDING_PATH BINDING_SHA256 ACTUAL_TOOL_CAPTURE')
binding_path, capture_path = Path(sys.argv[1]), Path(sys.argv[3])
need(binding_path.is_absolute() and capture_path.is_absolute(), 'exact absolute receipt inputs')
pin(binding_path, sys.argv[2])
binding, capture = doc(binding_path), doc(capture_path)
need(SOURCE == OWN/'inspect_production.py', 'exact new documentary helper placement')
raw(SOURCE);raw(OLD_SOURCE)
need(binding_path == QA/'p212_author_initial_binding01/BINDING.json' and capture_path == binding_path.parent/'PRODUCTION_TOOL_INVOCATION.json', 'exact initial original binding/capture roles')
need(binding['approved'] is True and binding['purpose'] == 'P212_AUTHOR_MANUSCRIPT' and binding['role'] == 'author', 'actual approved author binding')
mode, attempt = binding['mode'], Path(binding['attempt'])
need(mode == 'initial' and attempt == QA/'root_replays/p212_author_initial_01', 'exact initial-only scope; strict pair requires separate adaptation')
need(all(type(n) is int and 0 < n <= 900 for n in binding['timeouts'].values()), 'finite positive integer deadlines')
need(binding['argv_template'] == ['$ENTRY', '--parameters', '$PARAMETERS'] and binding['parameter_locator'] == 'explicit_absolute_argv', 'actual source interface')
need({r['name'] for r in binding['capsule_files']} == {'verify.py', 'PARAMETERS.json'} and len(binding['capsule_files']) == 2, 'two distinct scientific files')
lock_path = Path(binding['runtime_lock']['path'])
pin(lock_path, binding['runtime_lock'])
lock = doc(lock_path)
expected = dict(lock['files'])
expected.update(binding['adapter_sources'])
expected[str(binding_path)] = rich(binding_path)
expected[str(lock_path)] = rich(lock_path)
for row in binding['capsule_files']+binding['provenance_inputs']:
    expected[row['path']] = row
if mode == 'pair':
    expected[binding['canonical']['path']] = binding['canonical']
else:
    need(binding['canonical']['sha256'] is None, 'initial canonical unadopted at binding')
known = {}
for p, expected_pin in expected.items():
    actual = pin(p, expected_pin)
    known[p] = actual
    known[actual['resolved']] = rich(actual['resolved'])
for p, row in lock['configuration']['paths'].items():
    need(state(p) == row, ('live full configuration', p))
for directory, row in lock['configuration']['memberships'].items():
    p = Path(directory)
    current = {'directory': state(p, False), 'members': {}}
    if p.is_dir():
        current['members'] = {q.name: state(q, False) for q in sorted(p.iterdir())}
    need(current == row, ('live bounded direct membership', directory))
for p, row in lock['loader_search_directory_states'].items():
    need(state(p, False) == row, ('live loader directory state', p))

stages = ('outer', 'launcher', 'recorder', 'child01')+(('child02',) if mode == 'pair' else ())
capsule = attempt/'recorder/capsule'
need({p.name for p in capsule.iterdir()} == {'verify.py', 'PARAMETERS.json'}, 'physical source-only capsule')
copies = {}
for row in binding['capsule_files']:
    p = capsule/row['name']
    pin(p, {key: row[key] for key in ('sha256', 'bytes')})
    need(raw(p) == raw(row['path']), 'exact physical source copy bytes')
    copies[str(p)] = rich(p)


def argv(stage):
    return ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix='+str(attempt/('never_created_'+stage+'_cache')),
            str(PREP/'p212_runtime.py'), stage, str(binding_path), sys.argv[2], str(attempt)]


counts, native_count = {}, 0
for stage in stages:
    folder = attempt/stage
    counts[stage] = len(manifest(folder))
    result, entered = doc(folder/'RESULT.json'), doc(folder/'ENTERED.json')
    need(result['status'] == 'PASS' and result['errors'] == [] and result['wrapper_return'] == 0 and result['stage'] == stage and
         result['role'] == 'author' and result['mode'] == mode and not result['unfinalized_native'] and not result['unknown_descendant_closure'], ('complete successful stage', stage))
    cwd = capsule if stage.startswith('child') else ROOT
    need(entered['orig_argv'] == argv(stage) and entered['argv'] == argv(stage)[6:] and entered['cwd'] == str(cwd) and entered['environment'] == ENV, ('actual complete entry settings', stage))
    preknown = dict(known)
    if stage.startswith('child'):
        preknown.update(copies)
    need(doc(folder/'INPUTS_BEFORE.json') == preknown, ('entire expected prefrozen key', stage))
    final_known = {**preknown, **copies} if stage == 'recorder' else preknown
    if stage == 'recorder':
        need(doc(folder/'CAPSULE_ADDED_INPUTS.json') == copies and doc(folder/'INPUTS_BEFORE_SCIENCE.json') == final_known, 'entire pre-science source-copy key')
    need(doc(folder/'INPUTS_AFTER.json') == final_known, ('entire unchanged stage key', stage))
    for phase in ('BEFORE', 'AFTER'):
        sample = doc(folder/('RUNTIME_'+phase+'.json'))
        sample_known = preknown if phase == 'BEFORE' else final_known
        need(sample['environment'] == ENV and sample['cwd'] == str(cwd) and sample['interpreter_argv'] == argv(stage), ('actual sampled argv/ENV/cwd', stage, phase))
        need(sample['executable'] == '/usr/bin/python3.10' and sample['sys_path'] == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'], 'actual isolated interpreter/search path')
        need(all(flag in sample['flags'] for flag in ('isolated=1', 'no_site=1', 'optimize=0', 'dont_write_bytecode=1')), 'actual source-only flags')
        need(sample['pycache_prefix'] == str(attempt/('never_created_'+stage+'_cache')) and not sample['cache_lexists'] and not os.path.lexists(sample['pycache_prefix']), 'actual absent unique cache')
        need(identity(sample['proc_maps'].encode()) == {'sha256': sample['proc_maps_sha256'], 'bytes': sample['proc_maps_bytes']}, 'complete raw volatile maps identity')
        for p, row in list(sample['mapped_files'].items())+[(m['path'], m) for m in sample['modules'].values()]:
            need(p in sample_known and not p.endswith(('.pyc', '.pyo')), ('actual consumed file prefrozen', p))
            pin(p, row)
        need(doc(folder/('CONFIGURATION_'+phase+'.json')) == lock['configuration'], 'complete actual lock configuration')
        complete_sample(sample,stage,phase,sample_known,argv(stage),cwd,capsule)
    observed = doc(folder/'OPEN_OBSERVATIONS.json')
    complete_opens(observed,final_known,stage,attempt,attempt/('never_created_'+stage+'_cache'),capsule)
    need(observed['events'] == doc(folder/'OPEN_EVENTS_RAW.json'), 'complete actual open events')
    for p, row in observed['ordinary_files'].items():
        need(p in final_known, ('observed ordinary input in complete key', p))
        pin(p, row)
    for p in observed['absent_cache_probes']:
        need(not os.path.lexists(p), 'observed cache absence remains')
    if stage.startswith('child'):
        need(not observed['nonordinary_devices'] and not observed['volatile_proc_reads'] and not observed['own_attempt_io'], 'scientific read scope')
        need(all(not row.get('writing') and 'forbidden_process_event' not in row for row in observed['events']), 'no observed science write/process event')
        need(set(observed['ordinary_files']) == set(copies) | {'/usr/lib/python3.10/fractions.py','/usr/lib/python3.10/decimal.py','/usr/lib/python3.10/numbers.py'}, 'exact scientific opens: own two files and three preaccepted selected stdlib sources')
        need(result['output']['scientific_argv'] == [str(capsule/'verify.py'), '--parameters', str(capsule/'PARAMETERS.json')] and
             result['output']['parameter_locator'] == 'explicit_absolute_argv' and result['output']['scientific_outcome'] == 'SYSTEM_EXIT_ZERO', 'actual pinned compile/exec outcome')
        need(result['output']['source'] == copies[str(capsule/'verify.py')], 'actual executed source pin')
    commands = result['commands']
    actual_receipts = {p.parent.name: doc(p) for p in folder.glob('commands/*/RECEIPT.json')}
    need(set(actual_receipts) == {row['label'] for row in commands}, 'entire stage native census')
    for row in commands:
        label = row['label']
        native = actual_receipts[label]
        need({k: row[k] for k in native} == native, 'entire result/native binding')
        directory = folder/'commands'/label
        entry = doc(directory/'ATTEMPT.json')
        need(entry['status'] == 'ATTEMPTED' and entry['exit_code'] is None and all(entry[k] == native[k] for k in entry if k not in ('status', 'exit_code')), 'entire native pre-attempt relation')
        need(native['environment'] == ENV and native['exit_code'] == native['wrapper_exit_code'] == 0 and native['status'] == 'COMPLETED' and native['spawned'] and native['streams_complete'] and not native['timed_out'] and not native['interrupted'], 'actual successful complete native result')
        need(native['failure'] is None and native['stdin']=='DEVNULL' and native['new_owned_session_requested'] is True, 'complete native input/failure roles')
        need(native['ended_epoch'] >= native['started_epoch'], 'ordered actual native lifetime')
        deadline = binding['timeouts']['envelope'] if stage in ('outer','launcher') else binding['timeouts']['science'] if label.startswith('03_verify_') else binding['timeouts']['native']
        need(native['timeout_seconds'] == deadline, 'exact declared native deadline')
        settlement = native['process_group_settlement']
        need(settlement['quiescent'] and not settlement['signals'] and not any(m['state'] != 'Z' for m in settlement['remaining_members']) and native['pid'] == settlement['owned_pgid'] == settlement['owned_sid'] and settlement['native_returncode'] == 0, 'actual settled native process identity')
        for stream in ('stdout', 'stderr'):
            pin(directory/(stream+'.raw'), native[stream])
        need(raw(directory/'stderr.raw') == b'', 'declared empty native stderr')
        if native['argv'][0] == '/usr/bin/cmp':
            need(raw(native['argv'][-2]) == raw(native['argv'][-1]) and raw(directory/'stdout.raw') == b'', 'actual full native raw comparison inputs')
        native_count += 1
    if stage in ('outer', 'launcher'):
        child = 'launcher' if stage == 'outer' else 'recorder'
        need(len(commands) == 1 and commands[0]['label'] == '01_'+child and commands[0]['argv'] == argv(child), 'exact actual envelope child launch')
    elif stage.startswith('child'):
        need(not commands, 'scientific child no native command creation')

recorder = doc(attempt/'recorder/RESULT.json')
labels = ['00_copy_0', '00_copy_1', '01_ldd_before', '03_verify_01']
if mode == 'pair':
    labels += ['03_verify_02', '04_canonical_1', '04_canonical_2', '05_pair']
labels += ['06_ldd_after']
need([row['label'] for row in recorder['commands']] == labels, 'exact ordered recorder native census')
for label in ('01_ldd_before', '06_ldd_after'):
    directory = attempt/'recorder/commands'/label
    native = doc(directory/'RECEIPT.json')
    need(native['argv'] == ['/usr/bin/ldd']+lock['ldd_targets'], 'exact linkage targets')
    data = raw(directory/'stdout.raw')
    need(b'not found' not in data, 'no unresolved ELF input')
    linked = sorted({os.fsdecode(p) for p in re.findall(rb'(/[^\s()]+)', data) if Path(os.fsdecode(p)).is_file()})
    need(linked == lock['ldd_paths'] and all(p in known for p in linked), 'complete actual prefrozen linkage membership')
streams = recorder['output']['raw_stdout']
need(len(streams) == (1 if mode == 'initial' else 2) and recorder['output']['actual_raw_comparisons'] == (0 if mode == 'initial' else 3), 'initial/pair output distinction')
for index, row in enumerate(streams, 1):
    wanted = attempt/'recorder/commands'/('03_verify_'+str(index).zfill(2))/'stdout.raw'
    need(row['path'] == str(wanted), 'literal scientific stdout locator')
    pin(wanted, row)
    native = doc(wanted.with_name('RECEIPT.json'))
    need(native['argv'] == argv('child'+str(index).zfill(2)) and native['cwd'] == str(capsule), 'exact actual science native argv/cwd')
    science = doc(wanted)
    need(science['schema']=='p212-full-output-v1' and science['parameters']==doc(binding['capsule_files'][1]['path']) and science['summary']['state_count']==4356, 'scope locator only, every semantic field remains separate')
if mode == 'pair':
    need(raw(streams[0]['path']) == raw(streams[1]['path']) == raw(binding['canonical']['path']), 'entire actual pair/canonical raw bytes')
else:
    need(not os.path.lexists(binding['canonical']['path']), 'initial root reception before canonical publication')
all_rows = manifest(attempt)
need(len(all_rows) == (77 if mode == 'initial' else 104) and native_count == (7 if mode == 'initial' else 11), 'complete physical output/native population')
# Receive the genuinely separate root outer capture, not a direct old P211 launch.
root_entry = binding_path.parent/'entry01'
entry_rows = manifest(root_entry)
need(len(entry_rows)==9,'whole root nine-payload capture')
need(raw(root_entry/'EXECUTED_CONTROLLER.py')==raw(binding['root_capture']['controller']['path']) and raw(root_entry/'BINDING_ORIGINAL.json')==raw(binding_path),'entire actual executed controller/binding snapshots')
root_paths = sorted({str(binding_path),binding['runtime_lock']['path'],*binding['adapter_sources'],
                     *[r['path'] for r in binding['capsule_files']+binding['provenance_inputs']],
                     binding['root_capture']['controller']['path']})
root_known = {p:rich(p) for p in root_paths}
need(doc(root_entry/'INPUTS_BEFORE.json')==doc(root_entry/'INPUTS_AFTER.json')==root_known,'entire root capture pre/post source/authority key')
entry_result=doc(root_entry/'RESULT.json')
need(entry_result['status']=='CAPTURED_INITIAL_CANDIDATE_PENDING_COMPLETE_RECEPTION' and entry_result['errors']==[] and not entry_result['canonical_adopted'] and not entry_result['semantic_reception_completed'],'root capture not scientific acceptance')
need(len(entry_result['commands'])==1,'sole root native outer command')
entry_native=doc(root_entry/'commands/AUTHOR_INITIAL/RECEIPT.json')
need({k:v for k,v in entry_result['commands'][0].items() if k!='label'}==entry_native,'entire root native/result relation')
launch=['/usr/bin/env','-i']+[k+'='+v for k,v in ENV.items()]+argv('outer')
need(entry_native['argv']==launch and entry_native['cwd']==str(ROOT) and entry_native['environment']==ENV and entry_native['timeout_seconds']==1200,'exact actual root native argv/cwd/ENV/deadline')
entry_attempt=doc(root_entry/'commands/AUTHOR_INITIAL/ATTEMPT.json')
need(entry_attempt=={k:entry_native[k] for k in entry_attempt if k not in ('status','exit_code')} | {'status':'ATTEMPTED','exit_code':None},'entire root native attempt')
need(entry_native['exit_code']==entry_native['wrapper_exit_code']==0 and entry_native['status']=='COMPLETED' and entry_native['spawned'] and entry_native['streams_complete'] and not entry_native['timed_out'] and not entry_native['interrupted'] and entry_native['failure'] is None,'actual successful complete root native closure')
need(entry_native['process_group_settlement']=={'native_returncode':0,'owned_pgid':entry_native['pid'],'owned_sid':entry_native['pid'],'quiescent':True,'remaining_members':[],'signals':[]},'entire actual settled root owned group')
for stream in ('stdout','stderr'):
    pin(root_entry/'commands/AUTHOR_INITIAL'/(stream+'.raw'),entry_native[stream])
need(raw(root_entry/'commands/AUTHOR_INITIAL/stderr.raw')==b'','complete root native stderr empty')
need(doc(root_entry/'commands/AUTHOR_INITIAL/stdout.raw')=={'attempt':str(attempt),'seal':{'manifest':identity(raw(attempt/'SHA256SUMS')),'payloads':len(all_rows)},'status':'PASS'},'actual adapter outer summary with exact physical seal')
parts=[capture['result']]+[r['result'] for r in capture.get('polls',[])]
need(parts[-1]['exit_code']==0 and not parts[-1].get('session_id'),'actual product-boundary terminal completion')
need(capture['request']['workdir']==str(ROOT),'actual product cwd')
root_launch=['/usr/bin/env','-i']+[k+'='+v for k,v in ENV.items()]+['/usr/bin/python3.10','-I','-S','-B',binding['root_capture']['controller']['path'],str(binding_path),sys.argv[2]]
need(capture['request']['cmd']==' '.join(root_launch),'entire actual new root product launch')
if 'session_id' in capture['result']:
    need(capture['polls'][0]['request']['session_id']==capture['result']['session_id'] and 'exit_code' not in capture['result'],'genuine running-first/poll relation')
messages=[json.loads(line) for line in ''.join(p['output'] for p in parts).splitlines()]
need(messages and all(row.get('status')=='P212_OWNED_NATIVE_RUNNING' for row in messages[:-1]),'only declared native progress')
need(messages[-1]=={'attempt':str(attempt),'canonical_adopted':False,'entry':str(root_entry),'errors':[],'root_native_commands':1,'seal':{'manifest':identity(raw(root_entry/'SHA256SUMS')),'payloads':len(entry_rows)},'status':'CAPTURED_INITIAL_CANDIDATE_PENDING_COMPLETE_RECEPTION'},'entire actual root product/entry seal binding')
need(not os.path.lexists(binding['canonical']['path']) and not os.path.lexists(ROOT/'papers/212-closed-pointer-orbits/canonical.stdout.json'),'both canonical names remain absent')
for key,row in list(STATE_KEY.items()):
    need(state(row['path'],row['with_bytes'])==row['state'],'complete final present configuration role')
for p, data in READS.items():
    need(Path(p).read_bytes() == data, ('entire final read-set unchanged', p))
input_key={p:rich(p) for p in list(READS)}
with (OWN/'INPUTS_CURRENT.json').open('x') as stream:
    json.dump({'files':input_key,'configuration_state_roles':STATE_KEY},stream,sort_keys=True,indent=2);stream.write('\n')
print(json.dumps({'status': 'PASS_ROOT_COMPLETE_P212_INITIAL_PRODUCTION_RECORDS_PENDING_SEMANTICS', 'mode': mode,
    'binding': {'path': str(binding_path), **rich(binding_path)}, 'attempt': str(attempt),
    'checks': CHECKS, 'actual_read_paths': len(READS), 'complete_payloads': len(all_rows),
    'complete_manifest': identity(raw(attempt/'SHA256SUMS')), 'stage_payloads': counts,
    'native_commands': native_count, 'actual_author_invocations_received': len(streams),
    'actual_raw_comparisons_received': 0 if mode == 'initial' else 3,
    'raw_stdout': streams, 'root_scientific_producer_invocations_in_this_audit': 0,
    'scope': 'Complete actual author execution records and current bound inputs, not an additional scientific run or manuscript review.'}, sort_keys=True, indent=2))
