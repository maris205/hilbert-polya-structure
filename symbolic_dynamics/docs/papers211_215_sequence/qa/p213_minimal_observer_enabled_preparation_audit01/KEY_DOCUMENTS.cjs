'use strict';
// Finite ordinary documentary operands only. Proposed operational paths are never used.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const QA='docs/papers211_215_sequence/qa/';
const PACK=QA+'p213_minimal_observer_enabled_preparation01/';
const names=['SHA256SUMS','CLOSING_NATIVE.json','CLOSE_DOCUMENTS.cjs','HANDOFF_READS_NATIVE.json','HANDOFF.md','EVIDENCE.md','READBACK_NATIVE.json','CHECK_SOURCE_NATIVE.json','CHECK_INITIAL_NATIVE.json','CHECK_NATIVE.json','CHECK_DOCUMENTS.cjs','READ_SCOPE.md','PREPARATION.md','SOURCE_DIFF_NATIVE.json','PROSPECTIVE_BYTES.json','PREPARED_KEYS_NATIVE.json','KEY_PREPARED_DOCUMENTS.cjs','CONSUMPTION_MAP.json','TRANSFORMATION.json','PROPOSED_REQUEST.json','CAPTURE_REQUEST.disabled.json','capture.proposed.sh.txt','observe.proposed.py.txt','capture.sh','observe.py','BINDING.literal.txt','BINDING.runtime_literal.json','BINDING.prepared.json','INPUTS.sha256','INPUT_KEYS_NATIVE.json','SOURCE_READS_NATIVE.json','ORIENTATION_NATIVE.json','KEY_INPUT_DOCUMENTS.cjs'];
const old={
 'p213_minimal_observer_source_delta_root01':['RECEPTION.md','SHA256SUMS'],
 'p213_minimal_observer_source_delta01':['CONTRACT.md','BINDING_FORMAT.md','COLLECTION_DELTA.md','observe.py','capture.sh','CAPTURE_REQUEST.disabled.json','BINDING.disabled.json','SHA256SUMS'],
 'p213_minimal_observer_source_delta_audit01':['REPORT.md','FINDINGS.json','SHA256SUMS'],
 'p213_minimal_observer_binding_preparation01':['PROPOSAL.md','POLICY.proposed.json','SHA256SUMS']
};
const files=[...names.map(n=>PACK+n),...Object.entries(old).flatMap(([dir,nn])=>nn.map(n=>QA+dir+'/'+n)),'.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md','docs/papers211_215_sequence/PROBLEM_ANCHOR.md','docs/papers204_208_sequence/ARTIFACT_CONTRACT.md'].sort();
let checks=0;
function ok(v,m){checks++;if(!v)throw new Error(m);}
ok(files.length===53&&new Set(files).size===53,'finite scope');
const ff=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'];
function key(p){ok(!p.includes('/p213_minimal_observer_enabled01/')&&!p.includes('/p213_minimal_observer_probe01/'),'forbidden future operand');const a=fs.lstatSync(path.join(ROOT,p),{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'ordinary document '+p);const b=fs.readFileSync(path.join(ROOT,p));const z=fs.lstatSync(path.join(ROOT,p),{bigint:true});for(const k of ff)ok(a[k]===z[k],'unstable '+p+' '+k);ok(BigInt(b.length)===a.size,'size '+p);return {path:p,type:'regular',...Object.fromEntries(ff.map(k=>[k,z[k].toString()])),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
const before=files.map(key);const after=files.map(key);ok(JSON.stringify(before)===JSON.stringify(after),'closing identity');
console.log(JSON.stringify({scope:'53 finite existing documentary files; no future-path/host/private operation',checks,fields:ff,atime:'excluded as read-sensitive',keys:before}));
