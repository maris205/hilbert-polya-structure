"""Root receipt of actual independent P212 SOURCE_ONLY audit, not a runtime."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
OUT=Path(__file__).resolve().parent
QA=OUT.parent
AUDIT=QA/'p212_runtime_source_audit01'
PREP=QA/'p212_runtime_preparation01'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
KEY={}
LABELS=[]
NATIVE=[]

def need(ok,label):
    if not ok: raise AssertionError(label)
    LABELS.append(label)

def digest(raw): return sha256(raw).hexdigest()

def meta(p):
    p=Path(p); raw=p.read_bytes(); st=p.lstat()
    return {'bytes':len(raw),'sha256':digest(raw),'resolved':str(p.resolve(strict=True)),
      'regular':p.is_file() and not p.is_symlink(),'symlink':p.is_symlink(),
      'nlink':st.st_nlink,'mode':st.st_mode,'size':st.st_size,'mtime_ns':str(st.st_mtime_ns)}

def read(p):
    p=Path(p); k=meta(p)
    need(str(p) not in KEY or KEY[str(p)]==k,'repeat_same:'+str(p))
    KEY[str(p)]=k
    return p.read_bytes()

def obj(p): return json.loads(read(p))

def put(name,value):
    raw=value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (OUT/name).open('xb') as f: f.write(raw)

def seal(p,base,count,exact=False):
    rows={}
    for line in read(p).decode().splitlines():
        match=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(match is not None,'complete_hash_row:'+str(p))
        h,n=match.groups(); need(n not in rows and '..' not in Path(n).parts,'unique_safe_pin:'+n)
        target=Path(n) if Path(n).is_absolute() else base/n
        need(digest(read(target))==h,'full_payload_hash:'+n); rows[n]=h
    need(len(rows)==count,'complete_expected_pin_count:'+str(p))
    if exact:
        need(set(x.name for x in base.iterdir())==set(rows)|{p.name},'whole_nonself_membership')
        for n in [*rows,p.name]:
            k=meta(base/n)
            need(k['regular'] and not k['symlink'] and k['nlink']==1 and k['resolved']==str(base/n),'ordinary_singlelink:'+n)
    return rows

def run(argv,cwd,expected=0):
    i=len(NATIVE); prefix='AUDIT_COMMAND_%02d'%i
    request={'argv':argv,'cwd':str(cwd),'environment':ENV,'stdin':'DEVNULL','timeout_seconds':60}
    put(prefix+'_ATTEMPT.json',request)
    done=subprocess.run(argv,cwd=cwd,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=60)
    put(prefix+'_stdout.raw',done.stdout); put(prefix+'_stderr.raw',done.stderr)
    record={'request':request,'exit_code':done.returncode,
      'stdout':{'bytes':len(done.stdout),'sha256':digest(done.stdout)},
      'stderr':{'bytes':len(done.stderr),'sha256':digest(done.stderr)}}
    put(prefix+'_NATIVE.json',record); NATIVE.append(record)
    need(done.returncode==expected and done.stderr==b'','native_complete_expected:'+str(i))
    return done.stdout

need(not (OUT/'AUDIT_RESULT.json').exists(),'new_audit_result')
read(__file__)
payloads=seal(AUDIT/'SHA256SUMS',AUDIT,8,True)
need(digest(read(AUDIT/'SHA256SUMS'))=='b78eac6a29e4ca02abbe75f3d7d1f89341ec878efd3c4f8510b9ceedf8539d9d','exact_delivered_audit_seal')
need(sum(len(read(AUDIT/n)) for n in [*payloads,'SHA256SUMS'])==528068,'all_nine_file_bytes')
seal(AUDIT/'INPUTS.sha256',ROOT,36)
checks=obj(AUDIT/'CHECKS_NATIVE.json')['records']
reads=obj(AUDIT/'NATIVE_READS.json')['records']
diffs=obj(AUDIT/'NATIVE_DIFFS.json')['records']
closing=obj(AUDIT/'CLOSING_NATIVE.json')['records']
need([len(v) for v in [checks,reads,diffs,closing]]==[10,19,3,3],'full_actual_record_census')
for label,records in [('checks',checks),('reads',reads),('diffs',diffs),('closing',closing)]:
    for i,row in enumerate(records):
        r=row['result']; need(isinstance(row['request']['cmd'],str) and isinstance(r['output'],str) and isinstance(r['chunk_id'],str) and 'session_id' not in r,'actual_native_envelope:'+label+str(i))
        need(r['exit_code']==(1 if label=='diffs' or label=='closing' and i==1 else 0),'actual_expected_or_preserved_exit:'+label+str(i))
observed=json.loads(checks[3]['result']['output'])
need(observed['status']=='PASS_DOCUMENTARY_METADATA_ONLY' and observed['checks']==1311 and observed['input_key_count']==37 and len(observed['input_keys'])==37,'actual_complete_independent_documentary_result')
for p,k in observed['input_keys'].items():
    read(p); need(meta(p)==k,'entire_independent_rich_key:'+p)
need(len(observed['complete_archived_output_bindings'])==40 and observed['ordered_local_links']==47,'whole_archived_binding_and_link_census')
original=obj(PREP/'ORIGINAL_NATIVE_READS.json')['records']
for i in range(3):
    need(diffs[i]['result']['output']==original[49+i]['result']['output'] and diffs[i]['request']['cmd']==original[49+i]['request']['cmd'],'whole_actual_independent_diff_bytes:'+str(i))
for i in range(4,10):
    need(checks[i]['result']['output']=='' and ' | /usr/bin/cmp -- - ' in checks[i]['request']['cmd'],'six_actual_raw_source_comparisons:'+str(i))
def nl(p): return ''.join('%6d\t%s'%(i,line) for i,line in enumerate(read(p).decode().splitlines(keepends=True),1)).encode()
need(reads[8]['result']['output'].encode()==nl(PREP/'runtime_core.py'),'complete_independent_numbered_core_read')
need(''.join(reads[i]['result']['output'] for i in [9,10,11]).encode()==nl(PREP/'p212_runtime.py'),'complete_independent_numbered_adapter_read')
need(reads[12]['result']['output'].encode()==nl(PREP/'prepare_runtime.py'),'complete_independent_numbered_preparer_read')
final=json.loads(closing[2]['result']['output'])
for row in final['unsealed_payload_inventory']:
    raw=read(AUDIT/row['name']); need(len(raw)==row['bytes'] and digest(raw)==row['sha256'],'complete_actual_preseal_original:'+row['name'])
need(len(final['unsealed_payload_inventory'])==7,'exact_preclosing_payload_snapshot')
need(closing[1]['request']['cmd'].endswith("}'") and closing[1]['request']['cmd'][:-2]+"'"==closing[2]['request']['cmd'],'exact_one_brace_documentary_failure_correction')
need('SyntaxError' in closing[1]['result']['output'],'actual_syntax_failure_preserved')
for row in final['local_links']:
    need((AUDIT/row['literal']).resolve(strict=True)==Path(row['resolved']),'complete_actual_audit_link:'+row['literal'])
findings=obj(AUDIT/'FINDINGS.json')
need(findings['counts']=={'Critical':0,'Major':0,'Minor':0} and findings['findings']==[] and findings['decision']=='GO_IMPORT_DISCOVERY_PREPARATION' and findings['operational_status']=='HOLD_OPERATIONAL' and findings['scientific_status']=='HOLD_SCIENCE','actual_scope_limited_finding_decision')
prep_result=obj(OUT/'PREPARATION_RESULT.json')
need(prep_result['checks']==754 and prep_result['input_count']==54,'previous_actual_root_artifact_intake')
for p,k in prep_result['input_key'].items():
    raw=read(p)
    need(len(raw)==k['size'] and digest(raw)==k['sha256'] and str(Path(p).resolve())==k['resolved'],'full_root_previous_intake_content_key:'+p)
run(['/usr/bin/sha256sum','-c','SHA256SUMS'],AUDIT)
run(['/usr/bin/sha256sum','-c',str(AUDIT/'INPUTS.sha256')],ROOT)
raw=run(['/usr/bin/node',str(AUDIT/'audit_metadata.js')],ROOT)
need(raw==checks[3]['result']['output'].encode(),'whole_unchanged_reused_documentary_stdout_bytes')
for p,k in list(KEY.items()): need(meta(p)==k,'entire_before_after_rich_key:'+p)
result={'status':'PASS_ROOT_P212_SOURCE_AND_INDEPENDENT_AUDIT_RECEPTION_ONLY',
  'checks':len(LABELS),'labels':LABELS,'input_count':len(KEY),'input_key':KEY,
  'independent_documentary_checks_reused':1311,'entire_independent_stdout':{'bytes':len(raw),'sha256':digest(raw)},
  'actual_native_commands':NATIVE,'source_only_findings':findings['counts'],
  'submitted_programs_executed':0,'scientific_executions':0,'discovery_authorized':False,
  'limits':'Complete original source/audit receipt only. Explicit reuse of unchanged independent documentary checker is not a new independent audit or science. Root actual import-only authority, discovery/dependency reception and all scientific/build/review gates remain separate.'}
put('AUDIT_RESULT.json',result)
print(json.dumps({'status':result['status'],'checks':len(LABELS),'input_count':len(KEY),'same_documentary_stdout_bytes':len(raw),'same_documentary_stdout_sha256':digest(raw),'result_sha256':digest((OUT/'AUDIT_RESULT.json').read_bytes())},sort_keys=True))
