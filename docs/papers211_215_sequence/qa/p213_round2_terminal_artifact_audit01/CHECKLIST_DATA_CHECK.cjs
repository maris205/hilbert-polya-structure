'use strict';
// DATA-only current keys; accepted science/review semantics are not rerun.
const fs=require('node:fs'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics/',P=W+'papers/213-receiver-limited-cyclic-transfer/',Q=W+'docs/papers211_215_sequence/';
const read=p=>fs.readFileSync(p),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const rows=p=>read(p).toString().trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  (.+)$/.exec(l);if(!m)throw Error('manifest grammar');return{hash:m[1],path:m[2]};});
let checks=0;const keys=[];function pin(p,h){const b=read(p);if(sha(b)!==h)throw Error('changed '+p);checks++;keys.push({path:p.slice(W.length),bytes:b.length,sha256:h});}
const names=['verify.py','canonical_stdout.txt','VERIFICATION_PARAMETERS.json','PROOF_PACKAGE.md'];
const base=rows(P+'frozen_round2/SHA256SUMS');
for(const n of names){const x=base.find(x=>x.path===n);if(!x)throw Error('missing role '+n);for(const f of ['', 'frozen_round0/','frozen_round1/','frozen_round2/']){pin(P+f+n,x.hash);if(!read(P+f+n).equals(read(P+'frozen_round2/'+n)))throw Error('raw mismatch');checks++;}}
for(const id of ['a','b']){const d=Q+'reviews/p213_'+id+'/',manifest=id==='a'?'SHA256SUMS':'FINAL_PACKAGE_SHA256SUMS';const rs=rows(d+manifest);for(const n of ['verify.py','canonical_stdout.txt','FINDINGS_FINAL.json','DELTA.md']){const x=rs.find(x=>x.path===n);if(!x)throw Error('missing final review role '+n);pin(d+n,x.hash);}const finding=JSON.parse(read(d+'FINDINGS_FINAL.json'));const c=finding.current_open_census||finding.current_open;if(JSON.stringify(c)!=='{"Critical":0,"Major":0,"Minor":0}')throw Error('open review findings');checks++;}
console.log(JSON.stringify({status:'ACCEPT_CURRENT_SELECTED_SCIENTIFIC_KEYS_AND_ZERO_FINAL_FINDINGS_DATA_ONLY',checks,keys},null,2));
