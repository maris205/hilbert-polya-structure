// Mechanical integrity/link audit only, not proof or scientific numerics.
// Run from arithmetic_symplectic_flow:
// node papers/365-divisibility-scheduled-radix/evidence/verify-batch.cjs --brief
const fs=require('fs'), path=require('path'), crypto=require('crypto');
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const read=f=>fs.readFileSync(f,'utf8');
const assert=(b,m)=>{if(!b)throw Error(m);};
const files=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>{
  const f=path.join(d,e.name); return e.isDirectory()?files(f):[f];
}).sort();
const oldBlock=read('papers/360-profinite-two-step-gate/evidence/verify-batch.cjs')
  .match(/const old = (\[[\s\S]*?\n\]);/)[1];
const old=[...oldBlock.matchAll(/\['([^']+)',(\d+),'([a-f0-9]+)'\]/g)]
  .map(m=>[m[1],Number(m[2]),m[3]]);
assert(old.length===12,'Old348–359 anchor extraction');
old.push(
 ['360-profinite-two-step-gate',11,'5d6919a070fc9dd24464474047bbb14a9fc010349d472a71a29663a99c454cf4'],
 ['361-matrix-arithmetic-action',7,'ecc73fcae0175e0674c065f7e5110bc49b0da1a1b8216c8b7ef1ca685e24938f'],
 ['362-variable-multiplier-admission',7,'c154b34ddce8aa6f7bea015fb23fa02d91ea3a893dc3471c356d7d33d5b7580b'],
 ['363-reversible-uniform-clock-gate',7,'88c164c142b92b61618c7c654a5b6184a62202e3fc130926198658da73de2ee4'],
 ['364-symbolic-index-branching-gate',7,'8360748d085c7e75a6e85d7d1bfee5010b719eb43d271ec4d5b574aa662b2b41']
);
for(const[d,n,h]of old){
 const base=path.join('papers',d), ff=files(base);
 const bundle=ff.map(f=>path.relative(base,f)+'\t'+sha(fs.readFileSync(f))+'\n').join('');
 assert(ff.length===n&&sha(bundle)===h,'Frozen bundle changed '+d);
}
const anchors=[
 ['AGENTS.md','86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d'],
 ['plan.md','9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0'],
 ['docs/prior_work/README.md','d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd'],
 ['papers/paper-template.md','ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b'],
 ['papers/283-nonlinear-residue-clock-screen/paper.md','50429784fc1f634da86aa6aae1aac1b0e109b7fcc82a6169a68bb80a5bf95d38']
];
for(const[f,h]of anchors)assert(sha(fs.readFileSync(f))===h,'Anchor changed '+f);
const packages=[
 ['365-divisibility-scheduled-radix','ANG-20260921-DSR01','OWNED CLOCK; RETAINED PHASE EXCLUDES RETURNS — STOP / FORK',[[106,'a97872251dc4605ea0e60fd65c2ebfee83fedddf221c6200c3517cc4c3d000e8']]],
 ['366-local-visit-memory','ANG-20260921-LVM01','ZERO HAAR CLOCK; FULL MEMORY PREVENTS RETURNS — STOP / FORK',[[86,'770a774cd4cff6bfe43eb4ee3c10996a556cfa1afa4468171072512e427ac28c'],[104,'821b07ec4510cecb9b6245b4fcd58724512724c7c5c1ad52fc6449eef3864a18']]],
 ['367-global-coprime-memory','ANG-SCREEN-20260921-GCM01','FULL-HISTORY SOURCE FREE; NO INVARIANT PROBABILITY — PRE-P0 STOP / FORK',[[67,'21ef68fe27d0d8e08e8b6c6b517684b387ce972470919af8ac10b39f55d55141']]],
 ['368-atomic-memory-clock','ANG-AUDIT-20260921-AMC01','CONDITIONAL ATOMIC CLOCK FILTER — STOP / FORK UNDER HYPOTHESES',[[69,'7b8cac9a4941a415d0edd74f263977df5b739a43513adf8b25ac03f247f30fa4']]],
 ['369-finite-write-memory-clock','ANG-AUDIT-20260921-FWM01','FINITE-WRITE CLOCK CANCELLATION — CONDITIONAL STOP / FORK',[[81,'8ca58d59d6498503a344e749c96bd28201e7c0684d3ad8022ce823bad3ce64a5']]]
];
let markdown=0,links=0,frozenPrefixes=0; const inputs=[];
const receiptRows=[...read('papers/365-divisibility-scheduled-radix/batch-log.md')
 .matchAll(/^\| (36[5-9]) \| `([a-f0-9]{64})` \| `([a-f0-9]{64})` \|$/gm)];
assert(receiptRows.length===5,'Five evidence receipts required');
for(const m of receiptRows){
 const p=packages.find(p=>p[0].startsWith(m[1]+'-'))[0];
 const base=path.join('papers',p,'evidence');
 assert(sha(fs.readFileSync(path.join(base,'independent-proof.md')))===m[2],'Raw receipt '+p);
 const review=read(path.join(base,'review.md'));
 assert(sha(review)===m[3]&&review.includes('CP2 PASS')&&review.includes('CP3 PASS'),'Final review receipt '+p);
}
function checkLinks(s,f){for(const m of s.matchAll(/\]\(([^)]+)\)/g)){
 const target=m[1].split('#')[0];
 if(target&&!/^(https?:|mailto:)/.test(target)){
 assert(fs.existsSync(path.resolve(path.dirname(f),target)),'Broken link '+f+' -> '+target);links++;
 }
}}
for(const[d,id,status,freezes]of packages){
 const base=path.join('papers',d);
 assert(files(base).every(f=>f.endsWith('.md')||f.endsWith('/evidence/verify-batch.cjs')),'Non-Markdown output '+d);
 for(const f of files(base).filter(f=>f.endsWith('.md'))){
 const s=read(f);markdown++;
 assert(s.endsWith('\n')&&(s.match(/^```/gm)||[]).length%2===0,'Markdown format '+f);
 checkLinks(s,f);inputs.push({file:f,lines:s.split('\n').length-1,sha256:sha(s)});
 }
 for(const n of ['candidate-card.md','paper.md','README.md','claim-ledger.md']){
 const s=read(path.join(base,n));assert(s.includes(id)&&s.includes(status),'ID/status '+d+'/'+n);
 }
 const card=read(path.join(base,'candidate-card.md'));
 for(const[n,h]of freezes){assert(sha(card.split('\n').slice(0,n).join('\n')+'\n')===h,'Frozen prefix '+d+'/'+n);frozenPrefixes++;}
}
const overview=[
 ['readme.md','# Arithmetic Symplectic Flow\n\n> **Round 2 — Candidate Engineering / Structural Synthesis**\n','> **Preceding batch handoff (2026-09-21): ARITHMETIC-FEEDBACK','> **Current workflow state (2026-09-21): ARITHMETIC-FEEDBACK','eab160a16d8bd3a83140bc8a84c80a0649a6697d28c95a0e75cdf6cae046bce0'],
 ['papers/README.md','# Markdown paper registry\n\n','**Preceding batch handoff (2026-09-21): Arithmetic-feedback','**Current workflow state (2026-09-21): Arithmetic-feedback','7c9673fbfe02f8b6b93a9dc3a47a3089c99c6d9e7f6a02bcb28f1d0ae789f967']
];
for(const[f,prefix,marker,oldMarker,h]of overview){
 const s=read(f),i=s.indexOf(marker);assert(i>=0,'Archive marker '+f);
 assert(sha(prefix+s.slice(i).replace(marker,oldMarker))===h,'Overview archive '+f);
 checkLinks(s.slice(0,i),f);
}
console.log(JSON.stringify({result:'PASS',packages:packages.length,identitySurfaces:20,markdown,
 relativeLinks:links,frozenPrefixes,preservedPackages:old.length,preservedAnchors:anchors.length,
 preservedOverviewArchives:overview.length,boundEvidenceReceipts:receiptRows.length*2,
 inputs:process.argv.includes('--brief')?undefined:inputs},null,2));
