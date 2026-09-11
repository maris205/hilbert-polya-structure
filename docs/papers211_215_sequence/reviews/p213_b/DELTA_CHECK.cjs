'use strict';
// Read-only exact no-change delta and build-parser adapter check.
const fs=require('node:fs'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics/';
const PAPER=W+'papers/213-receiver-limited-cyclic-transfer/';
const F=PAPER+'frozen_round1/',OWN=W+'docs/papers211_215_sequence/reviews/p213_b/';
const BUILD=W+'docs/papers211_215_sequence/qa/p213_b_build_run01/';
const read=p=>fs.readFileSync(p),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;function ok(v,m){checks++;if(!v)throw Error(m);}
const manifest=read(F+'SHA256SUMS');
ok(sha(manifest)==='cd24d1ae5960456a7ed29978c9dbfac9794243b6bb913f19c6de1fb47d7479ce','Round1 manifest unchanged');
const rows=manifest.toString().trimEnd().split('\n').map(line=>{
  const m=/^([0-9a-f]{64})  ([A-Za-z0-9_./]+)$/.exec(line);ok(!!m&&!m[2].includes('..'),'safe freeze row');
  return {hash:m[1],path:m[2]};
});ok(rows.length===25,'complete Round1 payload count');
const comparisons=[];
for(const row of rows){
  const before=read(F+row.path);ok(sha(before)===row.hash,'current frozen payload');
  if(row.path==='FREEZE_SCOPE.md')continue;
  const afterPath=row.path==='main.pdf'?BUILD+'source_only/main.pdf':PAPER+row.path;
  const after=read(afterPath);ok(before.equals(after),'entire no-change counterpart '+row.path);
  comparisons.push({before:F+row.path,after:afterPath,bytes:before.length,sha256:row.hash});
}
ok(comparisons.length===24,'twenty-three live plus actual B PDF');
let a=read(W+'docs/papers211_215_sequence/reviews/p213_a/BUILD_DATA_CHECK.cjs').toString();
ok(sha(Buffer.from(a))==='8b4256d78033438ee1bd25817444b6f21b18d40ffa8ab66860f335462df75679','accepted A build parser source');
const adapter=[
 ['// Read-only A-build reception; accepted baseline role grammar reused explicitly.','// Read-only B-build reception; A\'s accepted complete parser reused explicitly.'],
 ['p213_a_build_run01','p213_b_build_run01'],['p213_a_build_preparation01','p213_b_build_preparation01'],
 ['frozen_round0','frozen_round1'],['p213_a_source_root01','p213_b_source_root01'],
 ['850799079c0e764025ebcf4df9f8528373c7007844b5e0f5981a8e06ac032dcb','aba046ae2b204a3a94139e3017b8214aeaabb886b382f7d8ab15bc317c63360f'],
 ['A_BUILD_NATIVE.json','B_BUILD_NATIVE.json'],['A_BUILD_CONTINUATION01.json','B_BUILD_CONTINUATION01.json'],
 ['session_id===3025','session_id===9998'],["chunk_id==='4b6308'","chunk_id==='d5a217'"],
 ["chunk_id==='2986fb'","chunk_id==='095b8a'"],['ACCEPT_A_BUILD_DATA_ORDINARY_TRUST_ONLY','ACCEPT_B_BUILD_DATA_ORDINARY_TRUST_ONLY']
];
for(const [oldValue,newValue]of adapter){ok(a.includes(oldValue),'adapter occurrence');a=a.split(oldValue).join(newValue);}
ok(Buffer.from(a).equals(read(OWN+'BUILD_DATA_CHECK.cjs')),'exact disclosed parser adapter');
console.log(JSON.stringify({status:'B_ACCEPTED_EXACT_NO_CHANGE_DELTA',checks,freeze_payloads:25,whole_raw_comparisons:24,scientific_delta:[],lifecycle_exclusion:'FREEZE_SCOPE.md unchanged here; future Round2 lifecycle only after root reception',comparisons,build_parser_adapter:adapter},null,2));
