"""Exact Review A original-package/documentary closure, not a scientific run."""
import gzip
import hashlib
import json
import os
import pathlib
import sys

D=pathlib.Path(__file__).resolve().parent
R=D.parents[3]
F=R/'papers/210-weakly-increasing-run-aggregation/frozen_round0'
count=0
read={}
def demand(v,message):
 global count
 count+=1
 assert v,message
def sha(p):
 p=pathlib.Path(p)
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 value=h.hexdigest()
 row={'sha256':value,'size':p.stat().st_size,'real':str(p.resolve()),'symlink':os.readlink(p) if p.is_symlink() else None}
 if str(p) in read:demand(read[str(p)]==row,'input changed during inspection:'+str(p))
 read[str(p)]=row
 return value
def obj(p):
 sha(p)
 with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)
def pinrow(path,row):
 p=pathlib.Path(path)
 demand(p.is_file(),'missing:'+path)
 demand(sha(p)==row['sha256'],'digest:'+path)
 demand(str(p.resolve())==row['real'],'realpath:'+path)
 demand(p.stat().st_size==row['size'],'size:'+path)
 demand((os.readlink(p) if p.is_symlink() else None)==row['symlink'],'symlink:'+path)

demand(sha(F/'SHA256SUMS')=='e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26','freeze seal')
listed=[]
for line in (D/'INPUT_PINS.sha256').read_text().splitlines():
 h,path=line.split('  ',1)
 p=R/path
 demand(not pathlib.Path(path).is_absolute() and '..' not in pathlib.Path(path).parts,'root-relative pin')
 demand(sha(p)==h,'frozen input:'+path)
 listed.append(p)
sha(D/'INPUT_PINS.sha256')
demand(len(listed)==494 and set(listed)=={p for p in F.rglob('*') if p.is_file()},'complete494freeze pins')
for line in (D/'COMMITMENT_PINS.sha256').read_text().splitlines():
 h,path=line.split('  ',1);demand(sha(D/path)==h,'unchanged independent commitment')
sha(D/'COMMITMENT_PINS.sha256')

package_counts={}
native=[]
runtime_counts={}
for name in ['produce01','pair01','pair02','build01','build02']:
 base=D/name
 payload=obj(base/'PAYLOADS.json')
 demand(set(payload)=={str(p) for p in base.rglob('*') if p.is_file() and p.name!='PAYLOADS.json'},'complete child payload:'+name)
 for path,row in payload.items():pinrow(path,row)
 package_counts[name]=len(payload)
 suffix='.json.gz' if name.startswith('build') else '.json'
 before=obj(base/('INPUTS_BEFORE'+suffix));after=obj(base/('INPUTS_AFTER'+suffix))
 demand(before==after,'historical prepost equality:'+name)
 for ledger in [before,after]:
  for path,row in ledger.items():pinrow(path,row)
 runtime_counts[name]=len(before)
 report=obj(base/'REPORT.json')
 demand(report['status']=='PASS' and not report['changed_inputs'],'child pass:'+name)
 for command,code in report['native_commands']:
  c=base/'commands'/command
  attempt=obj(c/'ATTEMPT.json');result=obj(c/'RESULT.json')
  demand(code==result['native_returncode']==0,'native command:'+name+'/'+command)
  demand(sha(c/'stdout')==result['stdout_sha256'],'native stdout')
  demand(sha(c/'stderr')==result['stderr_sha256'],'native stderr')
  native.append([name,command,code])
 if name.startswith('pair'):
  canonical=(D/'CANONICAL.json').read_bytes()
  for run in [1,2]:
   raw=base/'commands'/('run_'+str(run))/'stdout'
   demand(raw.read_bytes()==canonical,'complete canonical raw bytes')
   data=obj(raw);demand(data['checks']==133978 and data['total_states']==4095,'original scientific box')
   runtime=obj(base/('runtime_'+str(run)+'.json'))
   demand('-O' not in obj(base/'commands'/('run_'+str(run))/'ATTEMPT.json')['argv'],'unoptimized')
   demand(not pathlib.Path(runtime['settings']['xoptions']['pycache_prefix']).exists(),'absent runtime cache')
  demand(report['unpinned_observed_files']==report['forbidden_import_inputs']==[],'no unpinned runtime')
 if name.startswith('build'):
  initial=obj(base/'commands/pass_1/SOURCE_BEFORE.json')
  demand(len(initial)==10 and all(pathlib.Path(p).suffix in {'.tex','.bib'} for p in initial),'ten source-only inputs')
  demand(report['pages']==report['rendered_pages']==6,'six pages')
  demand(report['fonts_embedded']==['yes']*20 and report['warnings']==[],'fonts and logs')
  demand((base/'source/main.pdf').read_bytes()==(F/'main.pdf').read_bytes(),'PDF exact frozen bytes')
  view=obj(D/('VIEW_'+name+'.actual.json'))
  demand(view['status']=='PASS' and len(view['pages'])==6,'actual view record')
  for row in view['pages']:
   demand(row['actually_viewed'] is True and bool(row['observation']),'manual observation')
   demand(sha(R/row['path'])==row['sha256'],'view image pin')

privacy_environment_keys=set()
for p in D.rglob('*.json'):
 if p.name=='CANONICAL.json' or (p.name.startswith('INPUTS_')) or p.name=='PAYLOADS.json':continue
 data=obj(p)
 def inspect(v):
  if isinstance(v,dict):
   for k,x in v.items():
    if k=='environment' and isinstance(x,dict):
     privacy_environment_keys.update(x)
     demand(not {'AutodlAutoPanelToken','AutoDLServiceURL','AutoDLService6006URL','AutoDLService6008URL','http_proxy','https_proxy'} & set(x),'no credential/platform values in saved environment:'+str(p))
    inspect(x)
  elif isinstance(v,list):
   for x in v:inspect(x)
 inspect(data)

findings=obj(D/'FINDINGS.json')
demand(findings['census']=={'Critical':{'open':0,'resolved':0},'Major':{'open':0,'resolved':1},'Minor':{'open':0,'resolved':0},'total_open':0,'total_resolved':1},'exact finding census')
demand(len(findings['findings'])==1 and findings['findings'][0]['status']=='resolved','retain resolved Major')
for name in ['pair02','build02','compare_author02','build_pdf_cmp02']:
 base=D/'execution'/name
 attempt=obj(base/'ATTEMPT.json');result=obj(base/'RESULT.json')
 demand('start_ns' in attempt and 'environment_scope' in attempt,'fresh safe parent')
 demand(result['native_returncode']==0,'fresh parent native0')
 demand(sha(base/'stdout')==result['stdout_sha256'],'fresh parent stdout')
 demand(sha(base/'stderr')==result['stderr_sha256'],'fresh parent stderr')
comparison=obj(D/'execution/compare_author02/stdout')
demand(comparison['status']=='PASS' and comparison['checks']==300628,'complete author comparison')
for path,h in comparison['inputs_before'].items():demand(sha(path)==h,'whole comparison input pin')
demand(comparison['inputs_before']==comparison['inputs_after'],'comparison prepost')
demand('NOT_YET_ACCEPTED_DELTA' in (D/'DELTA.md').read_text(),'no invented acceptance')
for p in D.rglob('*'):
 if p.is_file():sha(p)
ledger=D/'AUDIT_READS.json.gz'
demand(not ledger.exists(),'new audit ledger')
with gzip.open(ledger,'xt') as f:json.dump(read,f,sort_keys=True);f.write('\n')
print(json.dumps({'schema':'p210-a-initial-original-audit-v1','status':'PASS','role':'reviewer documentary closure, not new scientific proof/run/root acceptance',
 'checks':count,'actual_read_paths':len(read),'freeze_inputs':494,'child_payload_counts':package_counts,'child_runtime_input_counts':runtime_counts,
 'native_commands':native,'current_open_findings':0,'resolved_major_findings':1,
 'read_ledger':str(ledger.relative_to(D)),'read_ledger_sha256':hashlib.sha256(ledger.read_bytes()).hexdigest(),
 'privacy_saved_environment_keys':sorted(privacy_environment_keys),'historical_exception':'SANITIZATION.md; three parent starts and authenticated original recorder prehash unavailable; no secret-bearing old receipt preserved'},sort_keys=True,indent=2))
