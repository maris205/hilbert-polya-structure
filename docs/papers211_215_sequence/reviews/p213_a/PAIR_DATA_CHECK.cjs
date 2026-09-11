'use strict';
// Existing strict-pair DATA and current declared fixed-file keys only.
const fs=require('node:fs'),crypto=require('node:crypto');
const root='/root/autodl-tmp/symbolic_dynamics/';
const batch=root+'docs/papers211_215_sequence/';
const review=batch+'reviews/p213_a/',qa=batch+'qa/';
const sourceRoot=qa+'p213_a_source_root01/',prep=qa+'p213_a_execution_preparation01/';
const read=p=>fs.readFileSync(p),json=p=>JSON.parse(read(p));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;function ok(v,m){checks++;if(!v)throw Error(m);}
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const current=p=>{const s=fs.lstatSync(p,{bigint:true});ok(s.isFile()&&!s.isSymbolicLink(),'regular current leaf');return Object.fromEntries(fields.map(k=>[k,s[k].toString()]));};
const initial=qa+'p213_a_initial_run01/';
const canonical=read(review+'canonical_stdout.txt'),original=read(initial+'stdout.bin');
ok(canonical.equals(original)&&canonical.length===40888&&sha(canonical)==='8846c5ba91c095a079f356a193fbd8721c145160190294f63300a07169771aac','adopted canonical exact original');
const accepted=json(review+'INITIAL_DATA_NATIVE.json');
ok(accepted.result.exit_code===0,'accepted initial DATA');
const initialData=JSON.parse(accepted.result.output);
ok(initialData.checks===7817&&initialData.stdout_sha256===sha(canonical),'complete prior semantic receipt');
const inputBytes=read(initial+'keys.before.json'),inputs=JSON.parse(inputBytes);
const deps=json(prep+'DEPENDENCIES.proposed.json');
ok(sha(read(prep+'DEPENDENCIES.proposed.json'))==='23cf1daad6b0873cc703ecf7e726e588ec08affb9de35910ecb59db42af11979','dependency pin');
ok(sha(read(prep+'EXTERNAL_KEYS.cjs'))==='ea89a37e57f3fed6909fd568c972d8b97537ecb07ae86febc130470f971abdac','collector pin');
ok(inputs.records.length===20&&deps.inputs.length===20,'complete declared shared inputs');
for(let i=0;i<20;i++){
 const r=inputs.records[i],d=deps.inputs[i];ok(r.path===d.path&&r.kind===d.kind,'ordered shared key');
 if(r.kind==='required-absence'){
  let absent=false;try{fs.lstatSync(d.path);}catch(e){if(e.code==='ENOENT')absent=true;else throw e;}
  ok(absent&&r.absence.code==='ENOENT','current declared absence');
 }else{
  const before=current(d.path),b=read(d.path),after=current(d.path);
  ok(equal(before,after)&&equal(before,r.begin),'complete current shared stat');
  ok(b.length===r.bytes&&sha(b)===r.sha256&&r.sha256===d.sha256,'current shared bytes');
 }
}
function manifest(name){for(const line of read(review+name).toString().trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);ok(m&&sha(read(review+m[2]))===m[1],'immutable '+name);}}
manifest('SOURCE_HANDOFF.sha256');manifest('INITIAL_RECEPTION.sha256');
const results=[];
for(const [tag,dir,chunk,session,end] of [['strict01','p213_a_strict_pair_run01','7d4d66',41276,'953db9'],['strict02','p213_a_strict_pair_run02','d09053',42626,'98f8fa']]){
 const run=qa+dir+'/',native=json(sourceRoot+tag+'_NATIVE.json'),finish=json(sourceRoot+tag+'_CONTINUATION01.json');
 const initialNative=json(sourceRoot+'INITIAL_NATIVE.json');
 const expected=initialNative.request.cmd.replaceAll('p213_a_initial_run01',dir).replace('outputs initial','outputs '+tag);
 ok(native.request.cmd===expected,'only designated output path/stage launch differences');
 const settings={...native.request};delete settings.cmd;const oldSettings={...initialNative.request};delete oldSettings.cmd;ok(equal(settings,oldSettings),'identical launch settings');
 ok(native.result.chunk_id===chunk&&native.result.session_id===session&&native.result.output==='','actual run origin');
 ok(finish.chunk_id===end&&finish.exit_code===0&&finish.output==='P213_A_CAPTURE_EXIT=0\n','actual sole continuation');
 for(const f of ['python.exit','controller.exit'])ok(read(run+f).equals(Buffer.from('0\n')),'zero child/controller status');
 for(const f of ['stderr.bin','controller.stdout','controller.stderr','keys.before.stderr','keys.after.stderr','raw.keys.stderr','input-key-cmp.stdout','input-key-cmp.stderr'])ok(read(run+f).length===0,'empty '+tag+' '+f);
 ok(read(run+'stdout.bin').equals(canonical),'entire strict stdout equals canonical');
 for(const f of ['keys.before.json','keys.after.json'])ok(read(run+f).equals(inputBytes),'entire unchanged shared input keys');
 const out=json(run+'raw.keys.json');ok(out.records.length===3&&out.status==='COMPLETE_EXTERNAL_KEYS_PENDING_RECEPTION','raw key completion');
 for(const [i,f]of ['stdout.bin','stderr.bin','python.exit'].entries()){
  const r=out.records[i],b=read(run+f);ok(r.path===run+f&&r.complete&&r.eof&&r.close_succeeded&&!r.failure,'complete output record');
  for(const name of ['fd_before','fd_after','end'])ok(equal(r.begin,r[name]),'output four-key equality');
  ok(equal(current(run+f),r.begin)&&b.length===r.bytes&&sha(b)===r.sha256,'current output key bytes');
 }
 const inventory=fs.readdirSync(run).sort().map(p=>({path:p,bytes:read(run+p).length,sha256:sha(read(run+p))}));ok(inventory.length===14,'complete14raw');
 results.push({stage:tag,chunk,session,completion:end,command_sha256:sha(Buffer.from(native.request.cmd)),stdout_sha256:sha(read(run+'stdout.bin')),input_keys_sha256:sha(read(run+'keys.before.json')),inventory});
}
ok(read(qa+'p213_a_strict_pair_run01/stdout.bin').equals(read(qa+'p213_a_strict_pair_run02/stdout.bin')),'entire pair equality');
console.log(JSON.stringify({status:'ACCEPT_TWO_STRICT_REPLAYS_ORDINARY_TRUST_ONLY',checks,canonical_bytes:canonical.length,canonical_sha256:sha(canonical),semantics_reused_from:'INITIAL_DATA_NATIVE.json actual6f0e8c/7817checks, all495records/461states/30carriers',current_shared_entries:20,results},null,2));
