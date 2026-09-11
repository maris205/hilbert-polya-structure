"""Root documentary reception only; no submitted checker/producer execution."""
from hashlib import sha256
import json
from pathlib import Path
import re
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'pointer_saved_output_root'
PREP = QA/'finite_pointer_initial_runtime_reception01'
ATTEMPT = QA/'root_replays/finite_pointer_initial01'
READS, CHECKS = {}, 0

def need(ok, detail):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(detail)

def raw(path):
    p = Path(path)
    need(p.is_absolute() and p.is_file() and p.resolve()==p and not p.is_symlink(), str(p))
    need(p != ATTEMPT/'recorder/commands/03_verify_01/stdout.raw', 'no scientific stdout body read')
    data = p.read_bytes()
    need(str(p) not in READS or READS[str(p)]==data, ('stable raw input',str(p)))
    READS[str(p)] = data
    return data

def val(data):
    return {'bytes':len(data),'sha256':sha256(data).hexdigest()}

def doc(path):
    return json.loads(raw(path))

def native(row, code=0):
    need(set(row)=={'request','result'} and row['request']['workdir']==str(ROOT), 'whole native envelope')
    r = row['result']
    need(type(r['exit_code']) is int and r['exit_code']==code and 'session_id' not in r and
         isinstance(r['chunk_id'],str) and isinstance(r['output'],str), 'actual complete native return')
    return r['output']

def equals_native(row, value):
    need(json.loads(native(row))==value, 'whole reconstructed documentary JSON stdout')

manifest = raw(PREP/'SHA256SUMS')
need(val(manifest)=={'bytes':767,'sha256':'44ea091871b62f2e5889f6ec644ddc1acb56163b8791d077309080870e343ddd'}, 'exact sealed preparation')
members = {}
for line in manifest.decode().splitlines():
    match = re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.]+)',line)
    need(match is not None, 'strict flat package row')
    h,n = match.groups()
    need(n not in members and n!='SHA256SUMS', 'unique nonself member')
    data = raw(PREP/n)
    need(sha256(data).hexdigest()==h, ('whole payload',n))
    members[n] = val(data)
need(len(members)==9 and sum(v['bytes'] for v in members.values())==584716 and
     {p.name for p in PREP.iterdir()}==set(members)|{'SHA256SUMS'}, 'entire 9 payload / 10 physical files')
source = raw(PREP/'inspect_initial.py')
need(val(source)=={'bytes':38572,'sha256':'daf7b06a20252979c96cca9f13793ae0d3230cd65e30f5124ffff1a379c44bdc'} and len(source.splitlines())==581, 'entire received checker source')
pins = {}
for line in raw(PREP/'INPUTS.sha256').decode().splitlines():
    h,n = line.split('  ',1)
    need(re.fullmatch('[0-9a-f]{64}',h) and not Path(n).is_absolute() and '..' not in Path(n).parts and n not in pins, 'safe unique historical pin')
    need(sha256(raw(ROOT/n)).hexdigest()==h, ('entire historical input',n))
    pins[n] = h
need(len(pins)==13, 'complete historical input set')
need(native(doc(PREP/'SOURCE_INPUTS_NATIVE.json')).encode()==raw(PREP/'INPUTS.sha256'), 'entire actual pin-collection stdout')
diff = raw(PREP/'DERIVATION.diff')
need(native(doc(PREP/'DERIVATION_NATIVE.json'),1).encode()==diff, 'entire native unified difference stdout')
lines = diff.splitlines(keepends=True)
need(lines[:3]==[b'--- p211_a_root_reception/inspect_production.py\n',b'+++ finite_pointer_initial_runtime_reception01/inspect_initial.py\n',b'@@ -1,281 +1,581 @@\n'], 'exact complete single diff hunk')
need(all(x[:1] in (b' ',b'+',b'-') for x in lines[3:]), 'all hunk line types')
need(b''.join(x[1:] for x in lines[3:] if x[:1] in (b' ',b'-'))==raw(QA/'p211_a_root_reception/inspect_production.py') and
     b''.join(x[1:] for x in lines[3:] if x[:1] in (b' ',b'+'))==source, 'full old/new source byte reconstruction')
static = doc(PREP/'STATIC_NATIVE.json')
need(set(static)=={'syntax','literal_derivative','imports'}, 'three actual static records')
for name,row in static.items():
    observed = json.loads(native(row))
    need(observed['checker_invocations']==observed['producer_invocations']==0, 'static only')
    need(observed.get('source_sha256',observed.get('sha256',observed.get('source',{}).get('sha256')))==sha256(source).hexdigest(), 'all actual static results bound to exact source')
need(json.loads(static['imports']['result']['output'])['imports']==['datetime','hashlib','json','math','os','pathlib','re','stat','sys','traceback'], 'exact ten stdlib imports')
reads = doc(PREP/'NATIVE_READS.json')
records = reads['records']
need(len(records)==23 and len(reads['display_failures'])==1, 'complete selected documentary record census and preserved failure')
for i,row in enumerate(records):
    output = native(row)
    argv = shlex.split(row['request']['cmd'])
    if argv[:2]==['sed','-n']:
        m = re.fullmatch(r'(\d+),(\d+)p',argv[2])
        need(m is not None and len(argv)==4, 'literal source excerpt')
        a,b = map(int,m.groups())
        need(output.encode()==b''.join(raw(ROOT/argv[3]).splitlines(keepends=True)[a-1:b]), ('entire actual source/excerpt output',i))
    elif argv[0]=='sha256sum':
        need(output==''.join(sha256(raw(ROOT/n)).hexdigest()+'  '+n+'\n' for n in argv[1:]), 'whole actual hash stdout')
    elif argv[:2]==['wc','-l']:
        rows = [x.split() for x in output.splitlines()]
        expected = [(len(raw(ROOT/n).splitlines()),n) for n in argv[2:]]
        need([(int(x[0]),x[1]) for x in rows[:-1]]==expected and rows[-1]==[str(sum(x[0] for x in expected)),'total'], 'all native wc rows')
    else:
        need(i in (14,15,16,18,19,20) and argv[:5]==['/usr/bin/python3.10','-I','-S','-B','-c'] and len(argv)==6, 'only fully root-read documentary snippets')
binding = doc(QA/'finite_pointer_initial_binding01/BINDING.json')
key = doc(QA/'finite_pointer_initial_binding01/INPUTS_AT_BINDING.json')
lock = doc(Path(binding['runtime_lock']['path']))
prov = {r['path']:{k:v for k,v in r.items() if k!='path'} for r in binding['provenance_inputs']}
equals_native(records[14], {'type':'preparation_data_read_no_receiver_invocation',
    'binding_bytes':len(raw(QA/'finite_pointer_initial_binding01/BINDING.json')),'binding_sha256':sha256(raw(QA/'finite_pointer_initial_binding01/BINDING.json')).hexdigest(),
    'binding_keys':sorted(binding),'input_key_file_bytes':len(raw(QA/'finite_pointer_initial_binding01/INPUTS_AT_BINDING.json')),
    'input_keys':len(key),'provenance_rows':len(binding['provenance_inputs']),'complete_key_equals_complete_provenance':key==prov,
    'lock_keys':sorted(lock),'lock_other_fields':{k:v for k,v in lock.items() if k not in ('files','configuration')},
    'lock_file_count':len(lock['files']),'configuration_keys':sorted(lock['configuration']),
    'configuration_paths':sorted(lock['configuration']['paths']),'membership_roots':sorted(lock['configuration']['memberships'])})
stages = ('outer','launcher','recorder','child01')
metadata, small, all_opens = {}, {}, {}
for stage in stages:
    folder = ATTEMPT/stage
    row = {n:doc(folder/n) for n in ('ENTERED.json','RESULT.json')}
    row['native_attempts'] = {p.parent.name:doc(p) for p in sorted((folder/'commands').glob('*/ATTEMPT.json'))}
    row['sample_metadata'] = {phase:{k:v for k,v in doc(folder/('RUNTIME_'+phase+'.json')).items() if k not in ('modules','mapped_files','proc_maps')} for phase in ('BEFORE','AFTER')}
    metadata[stage] = row
    sample, events = doc(folder/'RUNTIME_BEFORE.json'),doc(folder/'OPEN_EVENTS_RAW.json')
    project = {k:v for k,v in sample['modules'].items() if v['path'].startswith('/root/')}
    all_opens[stage] = {'sample_keys':sorted(sample),'project_modules':project,'open_events':events}
    small[stage] = {'sample_keys':sorted(sample),'project_modules':project,'open_event_count':len(events),
        'mode_flag_pairs':[json.loads(v) for v in sorted({json.dumps({k:r[k] for k in ('mode','flags','writing')},sort_keys=True) for r in events})],
        'outside_attempt_unique_paths':sorted({r['path'] for r in events if not Path(r['path']).is_relative_to(ATTEMPT) and not r['path'].startswith('/proc/')})}
equals_native(records[15],metadata)
equals_native(records[16],{'child_events':doc(ATTEMPT/'child01/OPEN_EVENTS_RAW.json'),'child_observations':doc(ATTEMPT/'child01/OPEN_OBSERVATIONS.json'),'source_copies':doc(ATTEMPT/'recorder/SOURCE_COPIES.json')})
need(records[18]['result']['original_token_count']>records[18]['request']['max_output_tokens'] and
     'truncated' in records[18]['result']['output'][:200].lower(), 'actual failed display remains truncated, not full equality')
equals_native(records[19],small)
receipts = {str(p.relative_to(ROOT)):doc(p) for p in sorted(ATTEMPT.glob('*/commands/*/RECEIPT.json'))}
equals_native(records[20],receipts)
final = doc(PREP/'FINAL_PREPARATION_NATIVE.json')
need(len(final['records'])==2 and native(final['records'][0])==''.join(n+': OK\n' for n in pins), 'actual thirteen old input checks')
f = json.loads(native(final['records'][1]))
need(f['source_sha256']==sha256(source).hexdigest() and f['checker_invocations']==f['producer_invocations']==f['scientific_stdout_body_reads']==0 and
     f['historical_input_rows']==13 and f['static_checks']==3 and set(f['physical_files_before_final_record_and_seal'])==set(members)-{'FINAL_PREPARATION_NATIVE.json'}, 'actual preparation state before final record and seal')
links = re.findall(r'\[[^\]]+\]\(([^)]+)\)',raw(PREP/'PLAN.md').decode())
need(links==f['links'] and len(links)==10 and all((PREP/n).is_file() for n in links), 'all actual now-closed plan links')
raw(Path(__file__).resolve())
for p,data in list(READS.items()):
    need(Path(p).read_bytes()==data, ('complete final raw reread',p))
result = {'status':'PASS_ROOT_COMPLETE_POINTER_RUNTIME_SOURCE_PREPARATION','checks':CHECKS,'read_paths':len(READS),
    'payloads':members,'input_pins':pins,'complete_source':val(source),'native_read_records':23,
    'native_static_records':3,'preserved_truncated_record':18,'checker_executions':0,'producer_executions':0,
    'scientific_stdout_body_reads':0,'READ_INPUTS':{p:val(data) for p,data in sorted(READS.items())}}
with (HERE/'RUNTIME_PREPARATION_RESULT.json').open('xb') as stream:
    stream.write((json.dumps(result,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps({k:v for k,v in result.items() if k not in ('READ_INPUTS','payloads','input_pins')},sort_keys=True))
