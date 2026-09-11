#!/usr/bin/python3.10
"""Same-reviewer documentary delta check. Reads only; stdout only.

No submitted checker, scientific program, formula or coefficient is executed.
This independently checks the declared archival evidence, not its mathematics.
"""
from hashlib import sha256
import json
from pathlib import Path
import re
import stat

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT/'docs/papers211_215_sequence/scouting'
RESPONSE = SCOUT/'finite_pointer_gate_response01'
GATE = SCOUT/'finite_pointer_residual_gate'
AUTHOR = SCOUT/'finite_local_state_fresh_desk'
reads = {}
checks = 0


def need(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def meta(s):
    return {k:getattr(s,'st_'+v) for k,v in [('mode','mode'),('device','dev'),
        ('inode','ino'),('uid','uid'),('gid','gid'),('nlink','nlink'),
        ('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns')]}


def fresh(path):
    need(path.is_absolute() and path.is_relative_to(ROOT) and path.resolve()==path and
         stat.S_ISREG(path.lstat().st_mode),('ordinary scoped physical original',str(path)))
    before = meta(path.lstat())
    raw = path.read_bytes()
    after = meta(path.lstat())
    need(before==after and after['size']==len(raw),('read metadata stability',str(path)))
    return raw,{**pin(raw),'stat':after}


def read(path):
    raw,value = fresh(path)
    name = str(path)
    need(name not in reads or reads[name]==value,('rich repeated input equality',name))
    reads[name] = value
    return raw


def obj(path):
    return json.loads(read(path))


def seal(base, count, digest):
    raw = read(base/'MANIFEST.sha256')
    need(pin(raw)['sha256']==digest,('literal accepted manifest',str(base)))
    rows = {}
    for line in raw.decode('utf-8').splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  ([^/\\\x00\r\n\t]+)',line)
        need(m is not None,('flat exact manifest row',line))
        h,n = m.groups()
        need(n not in rows and n not in ('.','..','MANIFEST.sha256'),'unique nonself file name')
        rows[n] = h
        need(pin(read(base/n))['sha256']==h,('full accepted payload hash',n))
    need(raw.endswith(b'\n') and len(rows)==count and
         {p.name for p in base.iterdir()}==set(rows)|{'MANIFEST.sha256'},'entire exact flat original package')
    return rows


def main():
    need(Path.cwd()==ROOT,'literal workspace cwd')
    response_rows = seal(RESPONSE,9,'4414fa67223ff50cdcba6c310bf5ed66ceeb7582a9c8afb1011ad272032555db')
    gate_rows = seal(GATE,8,'da1bf1d5a2daf9e1de2b4731187dab2029dd02b25ec8aa8b14fa55b5f63f1364')
    author_rows = seal(AUTHOR,5,'d6299f026e02195f145f33f819dcedb27b367c300280b3d3f7255fea1e136ada')
    before,after = obj(RESPONSE/'INPUT_PINS_BEFORE.json'),obj(RESPONSE/'INPUT_PINS_AFTER.json')
    need(before==after and len(before)==18,'complete18 response before/after byte pins')
    for path,expected in before.items():
        need(pin(read(Path(path)))==expected,('every actual response input unchanged',path))
    records = obj(RESPONSE/'NATIVE_DOCUMENTARY_RECORDS.json')['records']
    expected_cmd = '/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B '+str(RESPONSE/'inspect_inputs.py')
    runs = [r for r in records if r['request'].get('cmd')==expected_cmd]
    need(len(runs)==2,'exact two archived documentary invocations')
    outputs = []
    for row,chunk in zip(runs,['3ef8b7','dc068e']):
        need(row['request']=={'cmd':expected_cmd,'workdir':str(ROOT),'max_output_tokens':9000},'literal archived documentary request')
        result = row['result']
        need(result['chunk_id']==chunk and type(result['exit_code']) is int and result['exit_code']==0 and 'session_id' not in result,'actual completed documentary tool return')
        out = json.loads(result['output'])
        need(out['status']=='PASS_DOCUMENTARY_INPUT_CHECK_ONLY' and out['checks']==64 and
             out['inputs']==before and out['scientific_execution_or_import_count']==0 and
             out['open_findings']==['PTR-G-E1','PTR-G-S1','PTR-G-C1','PTR-G-D1'],'whole actual documentary output content')
        outputs.append(out)
    need(runs[0]['result']['output']==runs[1]['result']['output'] and outputs[0]==outputs[1],'complete archived decoded stdout and parsed results equal')
    author_records = obj(AUTHOR/'NATIVE_READS.json')['records']
    old_matches = [r for r in author_records if r['result'].get('chunk_id')=='c59488']
    gate_records = obj(GATE/'NATIVE_READS.json')['records']
    later_matches = [r for r in gate_records if r['result'].get('chunk_id')=='9a718e']
    need(len(old_matches)==len(later_matches)==1,'unique separate earlier and later native records')
    old,later = old_matches[0],later_matches[0]
    need(old['cmd']=="sed -n '1,180p' papers/167-minimum-inverse-position-feedback/main.tex" and old['result']['exit_code']==0,'actual original limited request/zero return')
    need(later['args']['cmd']=='cat papers/167-minimum-inverse-position-feedback/main.tex' and later['result']['exit_code']==0,'actual later whole-source request/zero return')
    source = read(ROOT/'papers/167-minimum-inverse-position-feedback/main.tex')
    need(pin(source)=={'bytes':16159,'sha256':'500fdea81499204a92bd3b6e24c5f9fd7b758d29b5c5dcdbf60e5e3f8e861d73'} and len(source.splitlines())==385,'unchanged whole385-line original')
    old_raw,later_raw = old['result']['output'].encode('utf-8'),later['result']['output'].encode('utf-8')
    need(old_raw==b''.join(source.splitlines(keepends=True)[:180]) and len(old_raw.splitlines())==180 and old_raw.splitlines()[-1]==b'\\midrule','exact old180-line prefix; not complete')
    need(later_raw==source,'later archived decoded stdout encodes entire unchanged source')
    history = {'original':{'chunk_id':'c59488','command':old['cmd'],'line_count':180,'last_line':'\\midrule','native_exit':0,'exact_source_prefix':True},'later_gate':{'chunk_id':'9a718e','command':later['args']['cmd'],'line_count':385,'native_exit':0,'exact_full_source':True}}
    need(outputs[0]['history']==history,'archived documentary output matches actual historical record reconstruction')
    summary = obj(RESPONSE/'DOCUMENTARY_CHECK.json')
    need(summary=={'status':'PASS_DOCUMENTARY_RESPONSE_INPUT_CHECK_ONLY','checks_per_actual_invocation':64,'actual_invocations':2,'input_paths':18,'prepost_inputs_identical':True,'entire_decoded_documentary_stdout_identical':True,'history':history,'scope':'All8gate and5author payload manifests; adjacentpilot/runtime manifests only; no candidate execution, gate acceptance or new proof.','scientific_executions':0,'open_findings':['PTR-G-E1','PTR-G-S1','PTR-G-C1','PTR-G-D1']},'entire response summary bound to originals, not accepted by its label')
    status = obj(RESPONSE/'RESPONSE_STATUS.json')
    need(status['source_gate_manifest']==pin(read(GATE/'MANIFEST.sha256'))['sha256'] and
         status['status']=='CORRECTIONS_SUBMITTED_SAME_REVIEWER_ACCEPTANCE_PENDING' and
         [r['id'] for r in status['findings']]==['PTR-G-S1','PTR-G-C1','PTR-G-D1','PTR-G-E1'] and
         all(r['reviewer_status']=='OPEN' and r['resolved_by_author'] is False for r in status['findings']), 'author has not self-resolved the gate')
    need(status['scientific_executions']==status['new_proof_claims']==0 and status['new_larger_boxes']==[] and status['paper_number'] is None and status['admission'] is None and status['prior_artifacts_modified']==[],'documentary-only author response scope')
    findings = obj(GATE/'FINDINGS.json')
    need([(r['id'],r['status']) for r in findings['major']]==[('PTR-G-E1','OPEN')] and
         [(r['id'],r['status']) for r in findings['minor']]==[('PTR-G-S1','OPEN'),('PTR-G-C1','OPEN'),('PTR-G-D1','OPEN')], 'original gate stays historically open and unchanged')
    expected_paths = {str(RESPONSE/n) for n in set(response_rows)|{'MANIFEST.sha256'}}|set(before)
    need(set(reads)==expected_paths and len(reads)==28,'complete28 original documentary input membership')
    final = {p:fresh(Path(p))[1] for p in sorted(reads)}
    need(final==reads,'entire28 rich before/after input equality')
    return {'schema':'pointer-gate-minor-delta-documentary-audit-v1','status':'PASS_DOCUMENTARY_ORIGINAL_BINDING_ONLY_NOT_SCIENCE_OR_ADMISSION','checks':checks,'fully_read_original_paths':len(reads),'response_payloads':len(response_rows),'gate_payloads':len(gate_rows),'author_payloads':len(author_rows),'archived_documentary_runs_received':2,'archived_decoded_stdout_equal':True,'historical_read_reconstruction':history,'INPUTS_BEFORE':reads,'INPUTS_AFTER':final,'source_pin':pin(Path(__file__).read_bytes()),'scientific_program_imports_or_runs':0,'larger_cutoffs':[],'finite_evidence_received':False,'E1_status':'OPEN_MAJOR'}


if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True))
