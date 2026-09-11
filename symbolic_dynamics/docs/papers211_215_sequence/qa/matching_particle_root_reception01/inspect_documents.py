#!/usr/bin/python3.10
"""New bounded documentary intake; never imports or runs a scientific source."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shlex
import stat
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).absolute().parent
SCOUT = ROOT/'docs/papers211_215_sequence/scouting'
RG = '/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
inputs, checks, commands, slices = {}, [], [], []

def need(ok, label):
    checks.append(label)
    if not ok:
        raise AssertionError(label)

def key(p):
    p = Path(p)
    a = p.lstat()
    need(stat.S_ISREG(a.st_mode) and p.resolve() == p, ('physical file',str(p)))
    raw = p.read_bytes()
    b = p.lstat()
    fields = ('st_mode','st_dev','st_ino','st_nlink','st_uid','st_gid','st_size','st_mtime_ns','st_ctime_ns')
    before, after = ({f:getattr(s,f) for f in fields} for s in (a,b))
    need(before == after and len(raw) == a.st_size, ('stable read',str(p)))
    return raw, {'bytes':len(raw),'sha256':sha256(raw).hexdigest(),'stat':after}

def read(p):
    p = Path(p)
    raw, value = key(p)
    need(str(p) not in inputs or inputs[str(p)] == value, ('repeated exact key',str(p)))
    inputs[str(p)] = value
    return raw

def obj(p):
    return json.loads(read(p))

def parse(raw):
    need(raw.endswith(b'\n'), 'pin list newline')
    rows = {}
    for line in raw.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(m is not None, ('pin syntax',line))
        h,n = m.groups()
        need(n not in rows and not Path(n).is_absolute() and '..' not in Path(n).parts,
             ('unique bounded relative pin',n))
        rows[n] = h
    return rows

def native(argv, cwd=ROOT, stdin=None):
    # Only these fixed documentary tools are invoked. No archived shell eval.
    need(argv[0] in ('/usr/bin/sha256sum',RG,'/usr/bin/pdftotext'), 'documentary executable allowlist')
    read(Path(argv[0]).resolve())
    request = {'argv':argv,'cwd':str(cwd),'environment':ENV,'timeout_seconds':30,
               'stdin':'DEVNULL' if stdin is None else 'explicit bytes'}
    kwargs = {'stdin':subprocess.DEVNULL} if stdin is None else {'input':stdin}
    actual = subprocess.run(argv,cwd=cwd,env=ENV,capture_output=True,timeout=30,**kwargs)
    result = {**request,'exit_code':actual.returncode,
              'stdout_utf8':actual.stdout.decode(),'stderr_utf8':actual.stderr.decode(),
              'stdout_pin':{'bytes':len(actual.stdout),'sha256':sha256(actual.stdout).hexdigest()},
              'stderr_pin':{'bytes':len(actual.stderr),'sha256':sha256(actual.stderr).hexdigest()}}
    commands.append(result)
    need(actual.returncode == 0 and actual.stderr == b'', ('actual documentary native',argv))
    return actual.stdout

def envelope(row, result_field='result'):
    need(isinstance(row['request'],dict) and isinstance(row['request']['cmd'],str), 'actual request dictionary')
    r = row[result_field]
    need(isinstance(r,dict) and type(r['exit_code']) is int and isinstance(r['output'],str)
         and isinstance(r['chunk_id'],str) and 'session_id' not in r, 'completed stored native envelope')
    return r

def source_bytes(row, allowed, result_field='result'):
    r = envelope(row,result_field)
    argv = shlex.split(row['request']['cmd'])
    if argv[0] == 'cat':
        names, bounds = argv[1:], None
    else:
        need(argv[0:2] == ['sed','-n'] and len(argv) == 4, 'literal selected sed command')
        m = re.fullmatch(r'(\d+),(\d+)p',argv[2])
        need(m is not None, 'exact finite source range')
        names, bounds = [argv[3]], tuple(map(int,m.groups()))
    need(set(names) <= allowed, ('selected old source scope',names))
    raw = b''.join(read(ROOT/n) for n in names)
    if bounds:
        raw = b''.join(raw.splitlines(keepends=True)[bounds[0]-1:bounds[1]])
    need(r['exit_code'] == 0 and r['output'].encode() == raw, ('entire archived raw source output',row['id']))
    slices.append({'id':row['id'],'names':names,'line_range':bounds,'bytes':len(raw),
                   'sha256':sha256(raw).hexdigest(),'comparison':'raw bytes, no normalization'})
    return raw

read(Path(__file__).absolute())
packages, oldsets, records_by_kind = {}, {}, {}
for kind, dirname, expected_sha, old_count, total_bytes in (
    ('matching','finite_matching_residual_scout01','acfc3a810fe17bd51796605ab274d2573ca8b0595ec0078bca49bd1a456db837',9,238874),
    ('particle','finite_particle_residual_scout01','ce4a304dac1032d8764e0ff1a159ae132724a665ff8940531ed3c499201e8f2f',8,94779)):
    base = SCOUT/dirname
    manifest = read(base/'SHA256SUMS')
    need(sha256(manifest).hexdigest() == expected_sha, ('original literal seal',kind))
    rows = parse(manifest)
    need(len(rows) == 6 and 'SHA256SUMS' not in rows and
         {p.name for p in base.iterdir()} == set(rows)|{'SHA256SUMS'}, ('whole six payload inventory',kind))
    for n,h in rows.items():
        need('/' not in n and sha256(read(base/n)).hexdigest() == h, ('payload',kind,n))
    need(sum(inputs[str(base/n)]['bytes'] for n in (*rows,'SHA256SUMS')) == total_bytes,
         ('whole original package bytes',kind))
    need(native(['/usr/bin/sha256sum','-c','SHA256SUMS'],base) ==
         ''.join(n+': OK\n' for n in rows).encode(), ('whole actual manifest output',kind))
    old = parse(read(base/'INPUTS.sha256'))
    need(len(old) == old_count, ('whole original history pin census',kind))
    for n,h in old.items():
        need(sha256(read(ROOT/n)).hexdigest() == h, ('old immutable source',kind,n))
    expected_ok = ''.join(n+': OK\n' for n in old).encode()
    need(native(['/usr/bin/sha256sum','-c',str((base/'INPUTS.sha256').relative_to(ROOT))]) == expected_ok,
         ('whole actual historical pins',kind))
    local = obj(base/'NATIVE_READS.json')['records']
    stored_checks = obj(base/'CHECKS_NATIVE.json')['records']
    need(len(local) == (6 if kind == 'matching' else 9), ('local record census',kind))
    need(len(stored_checks) == (8 if kind == 'matching' else 7), ('check record census',kind))
    for r in local:
        need(envelope(r)['exit_code'] == 0, ('actual local recorded exit',kind,r['id']))
    for i,r in enumerate(stored_checks):
        expected = ([0,1,1,127,0,0,0,0] if kind == 'matching' else [0]*7)[i]
        need(envelope(r)['exit_code'] == expected, ('preserve exact documentary exit',kind,i))
    need(stored_checks[0]['result']['output'].encode() == expected_ok, ('old native full pin output',kind))
    pin_id = 'pins_before' if kind == 'matching' else 'particle_inputs_hash'
    need(next(r for r in local if r['id'] == pin_id)['result']['output'].encode() == read(base/'INPUTS.sha256'),
         ('original sha raw stdout byte binding',kind))
    selected = ('old_read01','old_read03') if kind == 'matching' else tuple('particle_old_read%02d'%n for n in range(1,6))
    for r in local:
        if r['id'] in selected:
            source_bytes(r,set(old))
    for i in ((5,6) if kind == 'matching' else (1,2,3,4,5)):
        need(stored_checks[i]['result']['output'] == '' and
             'set -o pipefail\nnode -e ' in stored_checks[i]['request']['cmd'] and
             '| cmp - <(' in stored_checks[i]['request']['cmd'], ('actual successful archived raw comparison',kind,i))
    packages[kind] = {'payloads':6,'files':7,'total_bytes':total_bytes,'old_pin_count':old_count,'seal_sha256':expected_sha}
    oldsets[kind], records_by_kind[kind] = set(old), local

matching = SCOUT/'finite_matching_residual_scout01'
ms = obj(matching/'SOURCES_NATIVE.json')['records']
need(len(ms) == 6 and all(isinstance(r['request'],dict) and isinstance(r['result'],str) for r in ms), 'six actual browser request/string returns')
need(sum(len(r['request'].get('search_query',[])) for r in ms) == 9 and
     sum(len(r['request'].get('open',[])) for r in ms) == 7, 'exact source call census')
for index in (2,4,5):
    need('Internal Error' in ms[index]['result'], ('primary access failures preserved',index))
need('L130@' in ms[2]['result'] and 'L204@' in ms[2]['result'] and 'L254@' in ms[4]['result'], 'retained successful primary context bodies')
mchecks = obj(matching/'CHECKS_NATIVE.json')['records']
need(all('jq: command not found' in mchecks[i]['result']['output'] for i in (1,2,3)), 'all three actual missing-jq failures retained')
need(mchecks[-1]['result']['output'] == 'browser records: 6\n', 'actual corrected browser shape output')
search = next(r for r in records_by_kind['matching'] if r['id'] == 'old_read02')
argv = shlex.split(search['request']['cmd'])
need(argv[:2] == ['rg','-n'] and set(argv[3:]) <= oldsets['matching'], 'exact bounded old search')
actual = native([RG,*argv[1:]])
need(sorted(actual.splitlines()) == sorted(search['result']['output'].encode().splitlines()),
     'complete old search line content; sorting explicitly not raw equality')

particle = SCOUT/'finite_particle_residual_scout01'
ps = obj(particle/'SOURCE_ACCESS.json')
need(ps['kind'] == 'derived_browser_query_and_access_log_not_complete_native_response_archive' and
     len(ps['records']) == 11, 'particle browser metadata-only archive boundary')
for r in ps['records']:
    need(isinstance(r['request'],dict) and r['response_type'] == 'string' and
         type(r['response_characters']) is int and 'result' not in r, ('derived source metadata is not original body',r['id']))
need(ps['publisher_denial_native']['request'] == ps['records'][-1]['request'] and
     len(ps['publisher_denial_native']['result'].encode('utf-16-le'))//2 == ps['records'][-1]['response_characters'] and
     'Access Denied' in ps['publisher_denial_native']['result'], 'actual short publisher denial preserved')
shape = json.loads(obj(particle/'CHECKS_NATIVE.json')['records'][-1]['result']['output'])
need(shape == {'native_local_records':9,'browser_request_records':11,
               'all_stored_shell_exits_zero':True,'current_payloads_are_regular_files':True}, 'exact archived particle shape claim')

read(HERE/'INTAKE.md')
root_reads = obj(HERE/'ROOT_SELECTED_READS.json')['records']
root_browser = obj(HERE/'ROOT_BROWSER_NATIVE.json')['records']
need(len(root_reads) == 12 and len(root_browser) == 4, 'actual selected root record census')
for r in root_reads:
    envelope(r,'native')
    if r['id'] in ('matching_old_complete01','matching_old_complete03'):
        source_bytes(r,oldsets['matching'],'native')
    if r['id'].startswith('particle_old_complete'):
        source_bytes(r,oldsets['particle'],'native')
    if r['id'] in ('matching_local_pdf0','matching_local_pdf1'):
        args = shlex.split(r['request']['cmd'])
        need(args[:5] == ['/usr/bin/pdftotext','-f','1','-l','3'] and args[-1] == '-', 'bounded old PDF text role only')
        read(ROOT/args[-2])
        need(native(args) == r['native']['output'].encode(), 'whole old PDF text output; not viewing')
for r in root_browser:
    need(isinstance(r['request'],dict) and isinstance(r['result'],str), ('stored actual root browser body',r['id']))
bounded = next(r for r in root_reads if r['id'] == 'matching_primary_bounded')
expected = ''
for index,lo,hi in ((2,130,204),(4,0,115),(4,159,175),(4,254,275)):
    lines = []
    for line in ms[index]['result'].splitlines():
        m = re.match(r'L(\d+)@P[^:]+:',line)
        if m and lo <= int(m[1]) <= hi:
            lines.append((int(m[1]),line))
    need([n for n,line in lines] == list(range(lo,hi+1)), 'entire selected primary line range')
    expected += 'RECORD_RANGE %d %d %d\n'%(index,lo,hi)+'\n'.join(line for n,line in lines)+'\n'
need(bounded['native']['output'] == expected, 'root actual complete bounded primary extraction')

before = dict(inputs)
after = {p:key(Path(p))[1] for p in sorted(before)}
need(before == after, 'whole actually consumed rich file key unchanged')
result = {'status':'PASS_BOUNDED_DOCUMENTARY_ORIGINAL_RECEPTION','packages':packages,
          'checks':len(checks),'check_labels':checks,'actual_native_commands':commands,
          'raw_source_bindings':slices,'inputs_before':before,'inputs_after':after,
          'scientific_executions':0,'new_literals':0,'manuscript_reviews':0,'page_views':0,
          'closed_attempt_increment':0,'external':'OWNER_AMBER / HOLD_EXTERNAL',
          'limitations':['metadata checks are not independent mathematical review',
                        'particle browser full bodies are absent except the denial; root selected bodies are separate',
                        'archived discovery/search results are not whole-history absence certificates',
                        'all failed jq/source/display/navigation evidence stays unchanged',
                        'sorted rg line equality is not raw-output equality']}
with (HERE/'RESULT.json').open('xb') as stream:
    stream.write((json.dumps(result,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(result,sort_keys=True))
