#!/usr/bin/python3.10
"""Source-only preparation for root's later stdout-only original reception.

Disclosed reuse: explicit rich-read, five-attempt, unified-diff and numbered
source-binding logic from the fully read independent close_documentary.py.
This is NOT a new independent physical/manuscript review. No submitted or
capture helper is imported/run. No subprocess, shell, writes, science, build,
ambient environment collection, host discovery or operational grant exists.
On actual future invocation only, exact already-pinned host file aliases in
the original successful receiver key are re-read; no host directory is scanned.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import stat
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
A = QA/'p211_round2_physical_independent01'
R = QA/'p211_round2_root_reception01'
HERE = QA/'p211_round2_original_receiver_preparation01'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
PREFIX = 'env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B '
READS = {}
HOST = set()
CHECKS = 0
ENVELOPES = []


def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def pin(raw):
    return {'bytes':len(raw), 'sha256':sha256(raw).hexdigest()}


def meta(s):
    return {k:getattr(s, 'st_'+v) for k,v in (
        ('mode','mode'),('device','dev'),('inode','ino'),('uid','uid'),('gid','gid'),
        ('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns'))}


def rich(p):
    p = Path(p)
    need(p.is_absolute(), ('literal absolute original', str(p)))
    need(p.is_relative_to(ROOT) or str(p) in HOST, ('bounded exact original host alias', str(p)))
    ls, st = p.lstat(), p.stat()
    need(stat.S_ISREG(st.st_mode), ('ordinary resolved original file', str(p)))
    resolved = str(p.resolve(strict=True))
    link = os.readlink(p) if stat.S_ISLNK(ls.st_mode) else None
    if p.is_relative_to(ROOT):
        need(resolved == str(p) and link is None, ('ordinary workspace original', str(p)))
    raw = p.read_bytes()
    value = {**pin(raw),'resolved':resolved,'symlink':link,'stat':meta(st),'lstat':meta(ls)}
    need(meta(p.lstat()) == value['lstat'] and meta(p.stat()) == value['stat'] and
         str(p.resolve(strict=True)) == resolved and len(raw) == st.st_size,
         ('entire original read/stat stability', str(p)))
    need(str(p) not in READS or READS[str(p)] == value, ('repeated entire original key', str(p)))
    READS[str(p)] = value
    return raw, value


def read(p):
    return rich(p)[0]


def obj(p):
    return json.loads(read(p))


def byte_key(value):
    need(set(value) == {'bytes','sha256'} and type(value['bytes']) is int and value['bytes'] >= 0 and
         isinstance(value['sha256'], str) and re.fullmatch('[0-9a-f]{64}', value['sha256']), 'exact byte-key schema')


def rich_key(value):
    need(set(value) == {'bytes','sha256','resolved','symlink','stat','lstat'}, 'entire rich-key schema')
    byte_key({k:value[k] for k in ('bytes','sha256')})
    need(isinstance(value['resolved'], str) and Path(value['resolved']).is_absolute() and
         (value['symlink'] is None or isinstance(value['symlink'], str)), 'rich alias/link fields')
    names = {'mode','device','inode','uid','gid','nlink','size','mtime_ns','ctime_ns'}
    for k in ('stat','lstat'):
        need(set(value[k]) == names and all(type(n) is int for n in value[k].values()),
             'all exact integer ordinary stat fields')


def exact_tree(base, files, directories):
    actual_files, actual_dirs, identities = set(), set(), set()
    for p in base.rglob('*'):
        s = p.lstat()
        name = str(p.relative_to(base))
        need(not stat.S_ISLNK(s.st_mode), ('no symlink in complete original tree', str(p)))
        if stat.S_ISREG(s.st_mode):
            need(s.st_nlink == 1 and (s.st_dev,s.st_ino) not in identities,
                 ('separate ordinary original payload inode', str(p)))
            identities.add((s.st_dev,s.st_ino))
            actual_files.add(name)
        else:
            need(stat.S_ISDIR(s.st_mode), ('no special original tree entry', str(p)))
            actual_dirs.add(name)
    need(actual_files == set(files) and actual_dirs == set(directories),
         ('complete exact original tree files and directories', str(base)))


def outer(record, label, exit_code=0, truncated=False):
    """Consume every actual request/result/poll, never infer a missing exit."""
    need(set(record) in ({'request','result'}, {'request','result','polls'},
                         {'record_id','request','result'}, {'record_id','request','result','polls'}),
         ('complete original outer envelope schema', label))
    request = record['request']
    need(isinstance(request, dict) and isinstance(request.get('cmd'), str) and request['cmd'] and
         set(request) <= {'cmd','workdir','login','max_output_tokens','yield_time_ms','shell','tty'},
         ('complete original command request schema', label))
    need(request.get('workdir', str(ROOT)) == str(ROOT), ('actual stated/default workspace request', label))
    if 'max_output_tokens' in request:
        need(type(request['max_output_tokens']) is int and request['max_output_tokens'] > 0, 'native output budget')
    if 'yield_time_ms' in request:
        need(type(request['yield_time_ms']) is int and request['yield_time_ms'] >= 0, 'native original yield')
    results = [record['result']]
    previous = record['result']
    for poll in record.get('polls', []):
        need(set(poll) == {'request','result'} and set(poll['request']) ==
             {'session_id','chars','max_output_tokens','yield_time_ms'}, ('entire original poll schema', label))
        need('session_id' in previous and 'exit_code' not in previous and
             poll['request']['session_id'] == previous['session_id'] and poll['request']['chars'] == '',
             ('actual same pending native session', label))
        need(type(poll['request']['max_output_tokens']) is int and poll['request']['max_output_tokens'] > 0 and
             type(poll['request']['yield_time_ms']) is int and poll['request']['yield_time_ms'] >= 0,
             ('actual poll bounded settings', label))
        previous = poll['result']
        results.append(previous)
    for i, result in enumerate(results):
        expected = {'chunk_id','wall_time_seconds','original_token_count','output',
                    'exit_code' if i == len(results)-1 else 'session_id'}
        need(set(result) == expected, ('all native result fields and finality', label, i))
        need(isinstance(result['chunk_id'], str) and result['chunk_id'] and
             type(result['wall_time_seconds']) in (int,float) and 0 <= result['wall_time_seconds'] < float('inf') and
             type(result['original_token_count']) is int and result['original_token_count'] >= 0 and
             isinstance(result['output'], str), ('whole original result field types', label, i))
        if i < len(results)-1:
            need(type(result['session_id']) is int and result['session_id'] > 0, 'real pending session identifier')
        else:
            need(type(result['exit_code']) is int and result['exit_code'] == exit_code, ('actual final native exit', label))
        starts_truncated = result['output'].startswith('Warning: truncated output')
        need(starts_truncated == (truncated and i == 0), ('only declared real truncation exception', label, i))
    output = ''.join(r['output'] for r in results).encode()
    ENVELOPES.append({'label':label,'exit_code':exit_code,'polls':len(results)-1,'truncated':truncated,
                      'request_pin':pin(json.dumps(request,sort_keys=True).encode()),'whole_saved_output':pin(output)})
    return output


def apply_diff(old, patch):
    """Complete explicit in-memory unified-diff replay; never an on-disk edit."""
    lines = patch.decode().splitlines(keepends=True)
    need(len(lines) >= 3 and lines[0].startswith('--- ') and lines[1].startswith('+++ '), 'whole unified headers')
    original, result, cursor, i = old.decode().splitlines(keepends=True), [], 0, 2
    while i < len(lines):
        m = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', lines[i])
        need(m is not None, ('whole original hunk header', lines[i]))
        old_start,old_count,new_start,new_count = [int(x) if x is not None else 1 for x in m.groups()]
        start = old_start-1 if old_count else old_start
        need(cursor <= start <= len(original), 'ordered original hunk interval')
        result.extend(original[cursor:start])
        cursor = start
        need(len(result) == (new_start-1 if new_count else new_start), 'exact next-source hunk position')
        i += 1
        removed = added = 0
        while i < len(lines) and not lines[i].startswith('@@ '):
            line = lines[i]
            need(line[:1] in (' ','-','+') and line.endswith('\n'), 'all complete newline-terminated hunk lines')
            if line[0] in (' ','-'):
                need(cursor < len(original) and original[cursor] == line[1:], 'entire original hunk bytes')
                cursor += 1
                removed += 1
            if line[0] in (' ','+'):
                result.append(line[1:])
                added += 1
            i += 1
        need((removed,added) == (old_count,new_count), 'complete original hunk counts')
    result.extend(original[cursor:])
    return ''.join(result).encode()


def native(attempt, receipt, directory, stdout_name, stderr_name, expected_exit):
    need(set(receipt) == set(attempt) | {'ended_epoch','native_exit_code','exception','stream_capture_status','stdout','stderr'} and
         all(receipt[k] == v for k,v in attempt.items()), 'entire actual inner attempt/receipt closure')
    need(attempt['cwd'] == str(ROOT) and attempt['environment'] == ENV and
         type(attempt['started_epoch']) in (int,float) and type(receipt['ended_epoch']) in (int,float) and
         0 < attempt['started_epoch'] <= receipt['ended_epoch'] < float('inf') and
         type(receipt['native_exit_code']) is int and receipt['native_exit_code'] == expected_exit and
         receipt['exception'] is None and receipt['stream_capture_status'] == 'captured', 'actual bounded native completion')
    stdout, stderr = read(directory/stdout_name), read(directory/stderr_name)
    need(stderr == b'', 'actual entire empty native stderr')
    return stdout,stderr


def main():
    global HOST
    need(Path.cwd() == ROOT, 'exact future root documentary working directory')
    need(Path(__file__).absolute() == HERE/'receive_originals.py', 'unchanged original preparation source path')
    read(HERE/'receive_originals.py')
    pins_raw = read(HERE/'ORIGINAL_PINS.json')
    need(sha256(pins_raw).hexdigest() == '83f3fceec96a6230c08004e925f75496f9508b22724a327a6adeb68b154d3e98',
         'exact prior workspace-only preparation original pin list')
    preparation = json.loads(pins_raw)
    need(preparation['schema'] == 'p211-root-original-receiver-preparation-byte-pins-v1' and
         preparation['entries'] == len(preparation['pins']) == 107 and preparation['independent_files'] == 76 and
         preparation['root_recheck_files'] == 19 and preparation['explicit_extra_workspace_files'] == 12,
         'complete preparation original input census')
    for p,v in preparation['pins'].items():
        need(Path(p).is_relative_to(ROOT), 'preparation never probes host files')
        byte_key(v)
        need(pin(read(p)) == v, ('all107 preparation originals unchanged', p))

    expected_base = {'PLAN.md','receive_physical.py','capture_once.py','DERIVATION.diff','DERIVATION_NATIVE.json',
                     'NATIVE_READS.json','CORRECTIONS_NATIVE.json','close_documentary.py','INPUTS.sha256','FINDINGS.json','REPORT.md'}
    attempt_names = {'CHECKS_ATTEMPT.json','CHECKS_NATIVE.json','CHECKS.stdout.raw','CHECKS.stderr.raw',
                     'EXECUTED_RECEIVER_SOURCE.py','EXECUTED_CAPTURE_SOURCE.py','RESULT.json'}
    expected_preseal = expected_base | attempt_names | {'closing01/RESULT.json'}
    versions = [(A,'receive_physical.py','capture_once.py')]
    for n in range(2,6):
        suffix = str(n).zfill(2)
        versions.append((A/('run'+suffix),'receive_physical'+suffix+'.py','capture'+suffix+'.py'))
        expected_preseal |= {'receive_physical'+suffix+'.py','capture'+suffix+'.py'}
        expected_preseal |= {'run'+suffix+'/'+x for x in attempt_names}
    closing_labels = ('01_source_cmp','02_source_cmp','03_source_cmp','04_external_pins')
    for label in closing_labels:
        expected_preseal |= {'closing01/'+label+'/'+x for x in ('ATTEMPT.json','NATIVE.json','stdout.raw','stderr.raw')}
        if label != '04_external_pins':
            expected_preseal.add('closing01/'+label+'/stdin.raw')
    expected_dirs = {'run02','run03','run04','run05','closing01', *('closing01/'+x for x in closing_labels)}
    need(len(expected_preseal) == 74, 'explicit complete74 preseal roles')
    exact_tree(A, expected_preseal | {'CLOSING_NATIVE.json','SHA256SUMS'}, expected_dirs)
    seal_raw = read(A/'SHA256SUMS')
    need(pin(seal_raw) == {'bytes':6880,'sha256':'f1eac068f6f8dea79ae9cda7028b671a2d5e792af5836c2f15f84b0a09c82e39'},
         'entire original final independent seal')
    sealed = {}
    need(seal_raw.endswith(b'\n'), 'complete final independent seal LF')
    for line in seal_raw.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(m is not None, 'whole original manifest grammar')
        digest,name = m.groups()
        need(name in expected_preseal | {'CLOSING_NATIVE.json'} and name not in sealed,
             'exact original nonself payload membership')
        value = pin(read(A/name))
        need(value['sha256'] == digest, ('every independent sealed original byte stream', name))
        sealed[name] = value
    need(set(sealed) == expected_preseal | {'CLOSING_NATIVE.json'} and len(sealed) == 75, 'all75 original payload pins')
    need(seal_raw == ''.join(sealed[n]['sha256']+'  '+n+'\n' for n in sorted(sealed)).encode(), 'entire sorted seal reconstruction')

    passing_raw = read(A/'run05/CHECKS.stdout.raw')
    need(pin(passing_raw) == {'bytes':3430632,'sha256':'ff715a36ffd80ada101e64bf39085606155d7ea3c87beefe80555910fee84fdc'},
         'entire successful independent original output pin')
    passing = json.loads(passing_raw)
    need(passing['status'] == 'PASS_PHYSICAL_ROUND2_DOCUMENTARY_RECEPTION_PENDING_ROOT_DECISION' and
         passing['checks'] == 488474 and passing['receiver_read_paths'] == len(passing['READ_INPUTS']) == 4821,
         'actual original successful physical scope; no root verdict')
    HOST = {p for p in passing['READ_INPUTS'] if not Path(p).is_relative_to(ROOT)}
    need(len(HOST) == 803, 'only exact803 already-consumed original host aliases')

    attempts, union, outcomes = [], {}, []
    counts = (372,159491,159491,159617,488474)
    paths = (14,3994,3994,3994,4821)
    for i,(directory,source_name,capture_name) in enumerate(versions):
        attempt,receipt = obj(directory/'CHECKS_ATTEMPT.json'),obj(directory/'CHECKS_NATIVE.json')
        source,capture = read(A/source_name),read(A/capture_name)
        need(source == read(directory/'EXECUTED_RECEIVER_SOURCE.py') and
             capture == read(directory/'EXECUTED_CAPTURE_SOURCE.py'), 'entire original executed source/capture snapshots')
        need(attempt == {'argv':['/usr/bin/python3.10','-I','-S','-B',str(A/source_name)],'cwd':str(ROOT),
                         'environment':ENV,'stdin':'subprocess.DEVNULL','timeout_seconds':180,
                         'started_epoch':attempt['started_epoch'],'source_pin':pin(source),'capture_source_pin':pin(capture),
                         'scope':'only independently owned read-only documentary receiver; no submitted program execution'},
             'all exact actual original attempt fields')
        raw,stderr = native(attempt,receipt,directory,'CHECKS.stdout.raw','CHECKS.stderr.raw',0 if i == 4 else 1)
        need(receipt['stdout'] == {'path':'CHECKS.stdout.raw',**pin(raw)} and
             receipt['stderr'] == {'path':'CHECKS.stderr.raw',**pin(stderr)}, 'all whole original native/raw path pins')
        outcome,saved = json.loads(raw),obj(directory/'RESULT.json')
        key = outcome['READ_INPUTS'] if i == 4 else outcome['READ_INPUTS_PARTIAL']
        need(outcome['checks'] == counts[i] and len(key) == paths[i], 'each actual original stopping point/full key')
        if i == 4:
            need(saved == {**{k:v for k,v in outcome.items() if k != 'READ_INPUTS'},
                           'whole_helper_stdout':receipt['stdout'],'whole_input_key_entries':len(key)},
                 'entire successful compact result projection')
        else:
            need(saved == {'status':'FAIL_DOCUMENTARY_ATTEMPT_PRESERVED','native_exit_code':1,'exception':None,
                           'stdout':receipt['stdout'],'stderr':receipt['stderr']} and
                 outcome['status'] == 'FAIL_DOCUMENTARY_SCOPE_PRESERVE_ALL_ORIGINALS' and
                 isinstance(outcome['traceback'],str) and outcome['traceback'].startswith('Traceback (most recent call last):'),
                 'complete original failed result and genuine traceback retained')
        for p,v in key.items():
            rich_key(v)
            need(p not in union or union[p] == v, ('every partial/final rich-key overlap', p))
            union[p] = v
        attempts.append({'version':i+1,'directory':str(directory.relative_to(A)),'checks':counts[i],
                         'input_paths':len(key),'native_exit_code':receipt['native_exit_code'],'stdout':pin(raw),'source':pin(source)})
        outcomes.append((outcome,saved,receipt))
    need(len(union) == 4829, 'complete all5attempt rich union4829')
    for p,v in union.items():
        need(rich(p)[1] == v, ('all original4829 full rich rows current', p))

    derivation = obj(A/'DERIVATION_NATIVE.json')
    diff_raw = outer(derivation['record'], 'original_R1_derivation', 1)
    need(diff_raw == read(A/'DERIVATION.diff') and len(diff_raw) == 112415 and
         apply_diff(read(QA/'p211_round1_reception_preparation02/receive_round1.py'),diff_raw) == read(A/'receive_physical.py'),
         'entire real R1 derivation diff reconstructs original receiver')
    need(outer(derivation['own_static'], 'original_static_check') ==
         b'PASS_OWN_DOCUMENTARY_HELPER_SYNTAX_AND_LITERAL_STDLIB_IMPORT_SCOPE\n', 'entire original static native output')
    corrections = obj(A/'CORRECTIONS_NATIVE.json')
    need(corrections['schema'] == 'p211-r2-independent-own-corrections-native-v1' and
         len(corrections['source_diffs']) == 4 and len(corrections['attempts']) == 5 and
         len(corrections['cause_summary']) == 5, 'complete original correction and attempt census')
    for i,record in enumerate(corrections['source_diffs']):
        before,after = versions[i][1],versions[i+1][1]
        need(record['request']['cmd'] == '/usr/bin/diff -u -- '+str((A/before).relative_to(ROOT))+' '+str((A/after).relative_to(ROOT)),
             'exact native correction source pair')
        need(apply_diff(read(A/before),outer(record,'original_correction_'+str(i+1),1)) == read(A/after),
             'whole original correction reconstructs exact next version')
    root_diff = outer(corrections['root_actual_capture_correction'], 'original_root_capture_correction', 1)
    need(apply_diff(read(QA/'p211_round2_binding_root01/FAILED_ASSEMBLE_CAPTURE01.js'),root_diff) ==
         read(QA/'p211_round2_binding_root01/assemble_capture.js'), 'entire original ENV4 plus3evidence-read capture correction')
    for i,record in enumerate(corrections['attempts']):
        need(record['request']['cmd'] == PREFIX+str((A/versions[i][2]).relative_to(ROOT)) and
             record['request']['workdir'] == str(ROOT), 'exact original outer capture command')
        stream = outer(record, 'actual_attempt_'+str(i+1), 0 if i == 4 else 1)
        outcome,saved,receipt = outcomes[i]
        projection = {'status':saved['status'],'checks':saved.get('checks'),
                      'read_paths':saved.get('receiver_read_paths'),'native':receipt}
        need(stream == (json.dumps(projection,sort_keys=True)+'\n').encode(), 'whole original outer capture emitted bytes')
        need(corrections['cause_summary'][i]['attempt'] == i+1 and corrections['cause_summary'][i]['checks'] == counts[i],
             'all original correction census stopping points')

    native_reads = obj(A/'NATIVE_READS.json')
    ids = ('orientation0 orientation1 orientation2 orientation3 orientation4 paths paths_compact contract0 '
           'source0 source1 source2 source3 receiver0 receiver1 contract1 source4 source5 shapes0 build_source '
           'shapes1 shapes2 initial_pins shapes3 own_preflight_counts first_failure_diagnostic scope_diagnostic '
           'read_own_failed_source read_own_failed_capture second_failure_diagnostic capture_correction_diff '
           'read_failed_source02 read_failed_capture02 third_failure_diagnostic fourth_failure_diagnostic '
           'source_outer_schema_diagnostic source_reception_source').split()
    need(native_reads['schema'] == 'p211-r2-independent-actual-native-reads-v1' and
         [r['record_id'] for r in native_reads['records']] == ids and len(ids) == 36, 'all36 exact selected native read originals')
    records,streams = {},{}
    for record in native_reads['records']:
        name = record['record_id']
        records[name] = record
        streams[name] = outer(record,'selected_read_'+name,2 if name == 'paths' else 1 if name == 'capture_correction_diff' else 0,
                              truncated=name == 'paths')
    need(records['shapes2']['result']['session_id'] == 5124 and len(records['shapes2']['polls']) == 2 and
         records['shapes2']['result']['output'] == records['shapes2']['polls'][0]['result']['output'] == '',
         'actual selected navigation session5124 complete chain')
    need(streams['paths'].startswith(b'Warning: truncated output (original token count: 22399)\nTotal output lines: 1012\n') and
         b'p211_round1_independent01' in records['paths']['request']['cmd'].encode(), 'genuine wrong-path truncated diagnostic preserved')
    need(streams['capture_correction_diff'] == root_diff, 'complete duplicate original capture-diff return')
    for name,path in (('read_own_failed_source',A/'receive_physical.py'),('read_own_failed_capture',A/'capture_once.py'),
                      ('read_failed_source02',A/'receive_physical02.py'),('read_failed_capture02',A/'capture02.py')):
        need(streams[name] == read(path), 'whole original unnumbered failed-source/capture read')

    def groups(record_ids):
        result = []
        for line in b''.join(streams[name] for name in record_ids).decode().splitlines(keepends=True):
            m = re.match(r'^ *(\d+)\t(.*)', line)
            if m is None:
                continue
            number = int(m.group(1))
            if number == 1:
                result.append([])
            need(result and number == len(result[-1])+1, 'entire bounded numbered original source sequence')
            result[-1].append(line[line.index('\t')+1:])
        return [''.join(g).encode() for g in result]

    specs = [
        (('source0','source1','source2'),0,QA/'p211_round2_execution01/freeze.py',687),
        (('source3',),0,QA/'p211_round2_binding_root01/invoke_round2.py',109),
        (('source3',),1,QA/'p211_round2_binding_root01/refresh02/recheck.py',157),
        (('receiver0','receiver1'),0,QA/'p211_round1_reception_preparation02/receive_round1.py',529),
        (('source4',),0,QA/'p211_round2_binding_root01/assemble_capture.js',46),
        (('source4',),1,QA/'p211_round2_binding_root01/seal_actual.js',32),
        (('source5',),0,QA/'p211_round2_binding_root01/prepare_enabled.js',72),
        (('build_source',),0,ROOT/'docs/papers211_215_sequence/reviews/p211_a/inspect_build_reuse.py',142),
        (('source_reception_source',),0,QA/'p211_round2_binding_root01/source_reception01/receive.js',102)]
    source_bindings,source_inputs = [],[]
    for record_ids,index,path,count in specs:
        raw = groups(record_ids)[index]
        need(raw == read(path) and len(raw.splitlines()) == count, 'all9 complete original numbered source-read byte bindings')
        source_bindings.append({'record_ids':list(record_ids),'group_index':index,'path':str(path),'lines':count,'pin':pin(raw)})
        source_inputs.append(raw)

    external = {p:{k:v[k] for k in ('bytes','sha256')} for p,v in passing['READ_INPUTS'].items() if not Path(p).is_relative_to(A)}
    need(len(external) == 4818, 'all original4818 external successful reader paths')
    for p in (QA/'p211_round2_binding_root01/ENABLED_BINDING_RECEPTION.md',QA/'p211_round2_binding_root01/HOST_PRECHECK_SCOPE.md'):
        value = pin(read(p))
        need(str(p) not in external or external[str(p)] == value, 'exact extra root documentary original')
        external[str(p)] = value
    need(len(external) == 4820, 'entire4820 external original manifest scope')
    manifest_raw = ''.join(v['sha256']+'  '+p+'\n' for p,v in sorted(external.items())).encode()
    need(manifest_raw == read(A/'INPUTS.sha256'), 'entire exact external input manifest reconstruction')
    for p,v in external.items():
        need(pin(read(p)) == v, ('all4820 original external byte pins', p))

    closing = obj(A/'closing01/RESULT.json')
    closing_natives = []
    for i,label in enumerate(closing_labels):
        directory = A/'closing01'/label
        attempt,receipt = obj(directory/'ATTEMPT.json'),obj(directory/'NATIVE.json')
        if i < 3:
            index = (0,1,3)[i]
            argv = ['/usr/bin/cmp','-',source_bindings[index]['path']]
            origin = source_bindings[index]
            stdin = 'saved stdin.raw bytes'
            input_pin = pin(source_inputs[index])
            need(read(directory/'stdin.raw') == source_inputs[index], 'entire actual closing cmp saved stdin')
            expected_stdout = b''
        else:
            argv = ['/usr/bin/sha256sum','-c',str(A/'INPUTS.sha256')]
            origin = {'manifest':str(A/'INPUTS.sha256'),'pin':pin(manifest_raw),'rows':4820}
            stdin,input_pin = 'subprocess.DEVNULL',None
            expected_stdout = ''.join(p+': OK\n' for p in sorted(external)).encode()
        need(attempt == {'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':stdin,'input_pin':input_pin,'origin':origin,
                         'timeout_seconds':60,'started_epoch':attempt['started_epoch'],'tool_pin':pin(read(argv[0]))},
             'all exact closing4 original native requests/tool pins')
        stdout,stderr = native(attempt,receipt,directory,'stdout.raw','stderr.raw',0)
        need(receipt['stdout'] == pin(stdout) and receipt['stderr'] == pin(stderr) and stdout == expected_stdout,
             'all4 entire closing actual native/raw semantics')
        if closing_natives:
            need(closing_natives[-1]['ended_epoch'] <= receipt['started_epoch'], 'actual ordered original closing commands')
        closing_natives.append({'label':label,**receipt})
    expected_closing = {'status':'PASS_OWN_FAILURE_PRESERVATION_COMPLETE_SOURCE_BINDINGS_AND_NATIVE_CLOSURE',
        'checks':60196,'attempts':attempts,'all_attempt_original_rich_paths':4829,'successful_main_checks':488474,
        'successful_main_paths':4821,'external_input_rows':4820,'manifest_pin':pin(manifest_raw),
        'complete_source_bindings':source_bindings,'native_commands':closing_natives,'original_derivation_bytes':112415,
        'submitted_execution':False,'science':False,'build':False,'manuscript_review':False,'terminal_authority':False}
    need(closing == expected_closing, 'whole original saved60196 closing result reconstructed')

    closing_record = obj(A/'CLOSING_NATIVE.json')
    closing_ids = ['actual_owned_closing','actual_main_summary_projection','failed_preseal_saved_vs_outer_count',
                   'exact_failed_preseal_diagnostic','successful_complete_preseal']
    need(closing_record['schema'] == 'p211-independent-physical-round2-closing-native-v1' and
         [r['record_id'] for r in closing_record['records']] == closing_ids, 'complete final5 closing record census')
    cr = {r['record_id']:r for r in closing_record['records']}
    cs = {name:outer(cr[name],'closing_'+name,1 if name == 'failed_preseal_saved_vs_outer_count' else 0) for name in closing_ids}
    need(cr['actual_owned_closing']['request']['cmd'] == PREFIX+str((A/'close_documentary.py').relative_to(ROOT)),
         'actual original closing writer request checked only; never executed')
    expected_outer = {'status':closing['status'],'checks':60198,'rich_paths':4829,'external_input_rows':4820,
                      'complete_source_bindings':9,'native_commands':4,
                      'result':{'path':str(A/'closing01/RESULT.json'),**pin(read(A/'closing01/RESULT.json'))}}
    need(cs['actual_owned_closing'] == (json.dumps(expected_outer,sort_keys=True)+'\n').encode(),
         'whole actual60198 outer summary versus saved60196 counter point')
    projection = {'status':passing['status'],'checks':passing['checks'],'receiver_read_paths':passing['receiver_read_paths'],
                  'outside_workspace_paths':len(HOST),'phases':passing['phases'],'native':passing['native'],
                  'runtime':passing['recorder_runtime'],'host_refresh':passing['host_refresh'],'packaging':passing['packaging'],
                  'tree_roles':len(passing['RICH_TREE_SUMMARIES']),'settings_snapshot':passing['configuration_snapshot_pin']}
    need(cs['actual_main_summary_projection'] == (json.dumps(projection,sort_keys=True,indent=2)+'\n').encode(),
         'whole actual main closing projection binds every emitted field')
    failed_cmd = cr['failed_preseal_saved_vs_outer_count']['request']['cmd']
    good_cmd = cr['successful_complete_preseal']['request']['cmd']
    need(failed_cmd.count('close["checks"]==60198') == 1 and
         failed_cmd.replace('close["checks"]==60198','close["checks"]==60196') == good_cmd,
         'exact sole saved-versus-outer count correction to original preseal request')
    need(cs['failed_preseal_saved_vs_outer_count'] ==
         b'Traceback (most recent call last):\n  File "<string>", line 78, in <module>\n  File "<string>", line 9, in need\nAssertionError: actual closing full result\n',
         'complete genuine failed preseal diagnostic preserved')
    diag = {k:v for k,v in closing.items() if k not in ('attempts','complete_source_bindings','native_commands')}
    expected_diagnostic = json.dumps(diag,sort_keys=True,indent=2)+'\n'+json.dumps({'native':4,'source_bindings':9},sort_keys=True)+'\n'
    need(cs['exact_failed_preseal_diagnostic'] == expected_diagnostic.encode(), 'whole exact failed-preseal diagnostic projection')

    preseal = json.loads(cs['successful_complete_preseal'])
    report_raw = read(A/'REPORT.md')
    report_pin = pin(report_raw)
    old_links,now_links = [],[]
    for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)',report_raw.decode()):
        if re.match(r'^[a-z]+:',href):
            continue
        target = href.split('#',1)[0]
        path = (A/target).resolve(strict=True)
        need(path.is_relative_to(ROOT), 'report local target remains workspace-only')
        value = pin(read(path))
        now_links.append({'href':href,'path':str(path),'pin':value})
        if target in ('CLOSING_NATIVE.json','SHA256SUMS'):
            old_links.append({'href':href,'status':'pending_exact_final_appendix'})
        else:
            old_links.append({'href':href,'status':'exists','pin':value})
    preseal_pins = {n:pin(read(A/n)) for n in sorted(expected_preseal)}
    expected_preseal_result = {'status':'PASS_COMPLETE_PRESEAL_MEMBERSHIP_INPUT_KEYS_AND_FINAL_REPORT_PIN',
        'checks':41187,'payloads':74,'payload_bytes':sum(v['bytes'] for v in preseal_pins.values()),
        'directories':sorted(expected_dirs),'all_original_rich_paths':4829,'external_original_rows':4820,
        'report_local_links':old_links,'first_report_preseal_pin':report_pin,'payload_pins':preseal_pins,
        'allowed_next_appends':['CLOSING_NATIVE.json','SHA256SUMS'],'science':False,'build':False,'submitted_code_execution':False}
    need(preseal == expected_preseal_result and preseal['payload_bytes'] == 15166762 and
         cs['successful_complete_preseal'] == (json.dumps(expected_preseal_result,sort_keys=True,indent=2)+'\n').encode(),
         'all74 preseal original pins, full membership, entire native output and original report links')
    need(closing_record['first_successfully_recorded_final_report_pin'] == report_pin ==
         {'bytes':15320,'sha256':'bda86dd71b092037e93fa28c829b3c0defd042c69016f50a388d56399b158eac'} and
         closing_record['post_preseal_allowed_appends'] == ['CLOSING_NATIVE.json','SHA256SUMS'] and
         closing_record['post_preseal_report_edits'] is False and all(closing_record[k] is False for k in
         ('science','build','submitted_code_execution','terminal_authority')), 'complete final report pin and unchanged authority limits')
    findings = obj(A/'FINDINGS.json')
    need(findings['decision'] == 'PASS_INDEPENDENT_PHYSICAL_DOCUMENTARY_SCOPE' and
         findings['root_acceptance'] == 'PENDING_SEPARATE_ROOT_DECISION' and
         findings['open_findings'] == {'Critical':0,'Major':0,'Minor':0,'total':0} and
         findings['evidence']['closing_checks'] == 60198 and len(findings['receiver_development_failures']) == 4 and
         findings['paper_complete'] is False and findings['terminal_authority'] is False,
         'actual independent findings use outer60198 and retain root/terminal boundary')

    root_files = {'recheck.py','AUTHORITY.md','EXECUTED_CAPTURE_SOURCE.py','RECHECK_INPUTS_BEFORE.json',
                  'RECHECK_INPUTS_AFTER.json','RECHECK_RESULT.json','RECHECK_TOOL_NATIVE.json',
                  'INITIAL_PIN_NATIVE.json','ORIGINAL_SHAPES_NATIVE.json',
                  'NAVIGATION_LIMIT.md','NAVIGATION_TRUNCATED_CLOSING_READ.json',
                  *(label+suffix for label in ('01_recheck','02_compare') for suffix in
                    ('.ATTEMPT.json','.NATIVE.json','.stdout.raw','.stderr.raw'))}
    need(len(root_files) == 19, 'all19 original root recheck/navigation files')
    exact_tree(R,root_files,set())
    need(read(R/'recheck.py') == read(R/'EXECUTED_CAPTURE_SOURCE.py'), 'whole actual root recheck capture source snapshot')
    before_raw,after_raw = read(R/'RECHECK_INPUTS_BEFORE.json'),read(R/'RECHECK_INPUTS_AFTER.json')
    before,after = json.loads(before_raw),json.loads(after_raw)
    need(before_raw == after_raw and before == after and len(before) == 4896,
         'both complete original root4896 before/after keys byte-identical')
    root_expected = set(passing['READ_INPUTS']) | {str(A/n) for n in expected_preseal | {'CLOSING_NATIVE.json','SHA256SUMS'}} | {
                    str(R/'recheck.py'),str(R/'AUTHORITY.md')}
    need(set(before) == root_expected, 'entire root capture key independently reconstructed')
    for p,v in before.items():
        rich_key(v)
        need(rich(p)[1] == v and (p not in union or union[p] == v), ('all4896 original root key fields and all5attempt overlap',p))
    root_natives = []
    for i,label in enumerate(('01_recheck','02_compare')):
        attempt,receipt = obj(R/(label+'.ATTEMPT.json')),obj(R/(label+'.NATIVE.json'))
        argv = (['/usr/bin/python3.10','-I','-S','-B',str(A/'receive_physical05.py')] if i == 0 else
                ['/usr/bin/cmp','--',str(A/'run05/CHECKS.stdout.raw'),str(R/'01_recheck.stdout.raw')])
        need(attempt == {'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
                         'timeout_seconds':180 if i == 0 else 60,'started_epoch':attempt['started_epoch'],
                         'executable_full_key':rich(argv[0])[1]}, 'all actual root2 native request and full executable-key fields')
        stdout,stderr = native(attempt,receipt,R,label+'.stdout.raw',label+'.stderr.raw',0)
        need(receipt['stdout'] == pin(stdout) and receipt['stderr'] == pin(stderr) and
             stdout == (passing_raw if i == 0 else b''), 'entire actual root recheck3430632-byte output and native cmp0')
        if root_natives:
            need(root_natives[-1]['ended_epoch'] <= receipt['started_epoch'], 'actual root recheck before native comparison')
        root_natives.append(receipt)
    root_result = obj(R/'RECHECK_RESULT.json')
    expected_root_result = {'status':'PASS_ROOT_EXPLICIT_COMPLETE_PHYSICAL_RECEIVER_RECHECK_PENDING_ORIGINAL_RECEPTION',
        'root_capture_checks':71562,'root_capture_read_paths':4896,'reused_receiver_checks':488474,
        'reused_receiver_read_paths':4821,'independent_payloads':75,'independent_files':76,
        'whole_raw_output':pin(passing_raw),'native_cmp_exit':0,'source':pin(read(A/'receive_physical05.py')),
        'independent_seal':pin(seal_raw),'new_science':0,'new_builds':0,'new_page_views':0,'paper_complete':False,
        'new_independent_design':False,'terminal_authority':False,'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    need(root_result == expected_root_result, 'every actual root capture result field reconstructed')
    root_outer = obj(R/'RECHECK_TOOL_NATIVE.json')
    need(root_outer['request'] == {'cmd':PREFIX+str((R/'recheck.py').relative_to(ROOT)),'workdir':str(ROOT),
                                 'login':False,'yield_time_ms':1000,'max_output_tokens':2500} and
         root_outer['result']['session_id'] == 20297 and len(root_outer['polls']) == 1,
         'exact actual root encompassing request and native session20297')
    need(outer(root_outer,'actual_root_complete_recheck') == (json.dumps(root_result,sort_keys=True)+'\n').encode(),
         'whole actual RECHECK_TOOL_NATIVE output binds complete saved result')
    navigation = obj(R/'NAVIGATION_TRUNCATED_CLOSING_READ.json')
    navigation_raw = outer(navigation,'actual_root_truncated_closing_navigation',0,truncated=True)
    need(navigation_raw.startswith(b'Warning: truncated output (original token count: 12315)\nTotal output lines: 75\n') and
         navigation['request']['max_output_tokens'] == 10500 and navigation['request']['login'] is False,
         'real root exit0 but truncated closing navigation; no missing display bytes reconstructed')
    need(str(R/'NAVIGATION_LIMIT.md') not in before and str(R/'NAVIGATION_TRUNCATED_CLOSING_READ.json') not in before,
         'two later root navigation originals were not retroactively inserted in old4896 key')

    for p,v in union.items():
        need(rich(p)[1] == v, ('all4829 original attempt rich endpoints close',p))
    for p,v in before.items():
        need(rich(p)[1] == v, ('all4896 original root rich endpoints close',p))
    for p,v in preparation['pins'].items():
        need(pin(read(p)) == v, ('all107 preparation original byte pins close',p))
    exact_tree(A,expected_preseal | {'CLOSING_NATIVE.json','SHA256SUMS'},expected_dirs)
    exact_tree(R,root_files,set())
    for p,v in dict(READS).items():
        need(rich(p)[1] == v, ('entire new receiver current rich input key stable',p))
    return {'status':'PASS_ORIGINAL_PHYSICAL_DOCUMENTARY_CLOSURE_PENDING_ROOT_DECISION','checks':CHECKS,
        'read_paths':len(READS),'independent_payloads':75,'independent_files':76,'preserved_attempts':attempts,
        'all_attempt_original_rich_paths':4829,'root_before_after_rich_paths':4896,'external_original_input_rows':4820,
        'complete_source_bindings':source_bindings,'closing_native_commands':4,'closing_saved_checks':60196,
        'closing_outer_checks':60198,'preseal_payloads':74,'selected_native_reads':36,'final_closing_records':5,
        'actual_root_recheck':expected_root_result,'actual_outer_envelopes':ENVELOPES,'current_report_links':now_links,
        'whole_independent_seal':pin(seal_raw),'whole_independent_stdout':pin(passing_raw),
        'new_science':0,'new_builds':0,'new_page_views':0,'new_helper_or_shell_subprocesses':0,
        'new_independent_physical_design':False,'root_acceptance':False,'terminal_authority':False,
        'paper_complete':False,'external':'OWNER_AMBER / HOLD_EXTERNAL','READ_INPUTS':READS}


if __name__ == '__main__':
    try:
        result = main()
    except Exception:
        print(json.dumps({'status':'FAIL_ORIGINAL_DOCUMENTARY_RECEPTION_PRESERVE_ATTEMPT','checks':CHECKS,
                          'traceback':traceback.format_exc(),'READ_INPUTS_PARTIAL':READS},sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(result,sort_keys=True))
