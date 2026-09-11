'use strict';
// Read-only A-build reception; accepted baseline role grammar reused explicitly.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics',Q=W+'/docs/papers211_215_sequence/qa/';
const R=Q+'p213_a_build_run01',B=Q+'p213_initial_build_run02',C=R+'/source_only';
const P=Q+'p213_a_build_preparation01',F=W+'/papers/213-receiver-limited-cyclic-transfer/frozen_round0';
const read=p=>fs.readFileSync(p),txt=p=>read(p).toString('utf8'),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;function ok(v,m){checks++;if(!v)throw Error(m);}
const parse=s=>s.trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  (.+)$/.exec(l);ok(!!m,'manifest row');return{hash:m[1],path:m[2]};});
const same=(a,b)=>ok(read(a).equals(read(b)),'full raw equality '+a);
const inventory=[];function walk(d,rel=''){for(const e of fs.readdirSync(d,{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))){ok(!e.isSymbolicLink(),'no symlink');if(e.isDirectory())walk(d+'/'+e.name,rel+e.name+'/');else{ok(e.isFile(),'regular output');const b=read(d+'/'+e.name);inventory.push({path:rel+e.name,bytes:b.length,sha256:sha(b)});}}}walk(R);ok(inventory.length===165,'complete build inventory');
const baselineSeal=parse(txt(Q+'p213_initial_build_artifact_reception01/ARTIFACTS.sha256'));
for(const item of baselineSeal.filter(x=>path.resolve(W,x.path).startsWith(B+'/')))ok(sha(read(path.resolve(W,item.path)))===item.hash,'accepted baseline unchanged');
let sameCount=0,pathChanged=0,manifestCount=0;
for(const item of inventory){const p=item.path;
 if(p.endsWith('.sha256')){const base=p==='FINAL_PRODUCTS.sha256'?C:(p==='SOURCE_EXPECTED.sha256'?C:path.dirname(R+'/'+p));for(const x of parse(txt(R+'/'+p)))ok(sha(read(path.resolve(base,x.path)))===x.hash,'new manifest '+p);manifestCount++;continue;}
 if(p.endsWith('main.fls')){ok(txt(R+'/'+p)===txt(B+'/'+p).replace('PWD '+B+'/source_only\n','PWD '+C+'\n'),'exact single FLS PWD delta');pathChanged++;continue;}
 if(p.endsWith('.request.txt')){ok(txt(R+'/'+p)===txt(B+'/'+p).split(B).join(R),'exact recorded request path delta');pathChanged++;continue;}
 same(R+'/'+p,B+'/'+p);sameCount++;
}
const runtime=parse(txt(P+'/RUNTIME_INPUTS.sha256')),sources=parse(txt(P+'/PROPOSED_SOURCE_ONLY.sha256'));
ok(runtime.length===223&&sources.length===9,'runtime source counts');
for(const x of runtime)ok(sha(read(x.path))===x.hash,'current selected runtime');
for(const x of sources){ok(sha(read(F+'/'+x.path))===x.hash,'current frozen source');same(F+'/'+x.path,C+'/'+x.path);}
same(P+'/RUNTIME_INPUTS.sha256',R+'/RUNTIME_EXPECTED.sha256');same(P+'/PROPOSED_SOURCE_ONLY.sha256',R+'/SOURCE_EXPECTED.sha256');
const script=txt(P+'/BUILD_REQUEST.sh'),oldscript=txt(Q+'p213_initial_build_binding02/BUILD_REQUEST.sh');
const a=script.split('\n'),b=oldscript.split('\n');ok(a.length===b.length,'recipe line count');
const differences=a.flatMap((s,i)=>s===b[i]?[]:[i+1]);ok(JSON.stringify(differences)==='[11,12,13,14]','exact four assignments');
ok(sha(Buffer.from(script))==='850799079c0e764025ebcf4df9f8528373c7007844b5e0f5981a8e06ac032dcb','accepted recipe pin');
const native=JSON.parse(txt(Q+'p213_a_source_root01/A_BUILD_NATIVE.json')),end=JSON.parse(txt(Q+'p213_a_source_root01/A_BUILD_CONTINUATION01.json'));
const request=JSON.parse(txt(P+'/NATIVE_REQUESTS.proposed.json'));
ok(JSON.stringify(native.request)===JSON.stringify(request.proposed_native_request.arguments),'actual exact request');
ok(native.result.session_id===3025&&native.result.chunk_id==='4b6308','actual build session');
ok(end.exit_code===0&&end.chunk_id==='2986fb'&&end.output==='P213_INITIAL_BUILD_SUPERVISOR_EXIT=0\n','actual build completion');
const ordered=[];
for(const pass of ['pass1','pass2','pass3']){
 const snap=R+'/pass_artifacts/'+pass+'.before';
 const before=new Set(fs.existsSync(snap+'/PRESENT.sha256')?parse(txt(snap+'/PRESENT.sha256')).map(x=>x.path):[]),generated=new Set(),counts={};
 const ls=txt(R+'/pass_artifacts/'+pass+'.after/main.fls').trimEnd().split('\n');
 for(const [i,line]of ls.entries()){
  const m=/^(PWD|INPUT|OUTPUT) (.+)$/.exec(line);ok(!!m,'FLS grammar');const absolute=path.resolve(C,m[2]),local=absolute.startsWith(C+'/')?absolute.slice(C.length+1):null;let role;
  if(m[1]==='PWD'){ok(i===0&&m[2]===C,'new FLS cwd');role='cwd';}
  else if(m[1]==='OUTPUT'){ok(['main.log','main.aux','main.pdf'].includes(local),'generated output');generated.add(local);role='output';}
  else if(runtime.some(x=>x.path===absolute))role='runtime';
  else if(sources.some(x=>x.path===local))role='source';
  else if(generated.has(local))role='same-pass-generated';
  else if(before.has(local))role='prior-generated';
  else throw Error('unknown recorder input '+line);
  counts[role]=(counts[role]||0)+1;
 }
 ok(ls.length===(pass==='pass1'?246:253)&&counts.runtime===191&&counts.source===50&&counts.output===3&&counts['same-pass-generated']===1&&(counts['prior-generated']||0)===(pass==='pass1'?0:7),'complete event roles');
 ordered.push({pass,events:ls.length,counts});
}
const diagnostics=[];
for(const pass of ['pass1','pass2','pass3'])for(const role of ['log','stdout']){
 const p=role==='log'?R+'/pass_artifacts/'+pass+'.after/main.log':R+'/raw/'+pass+'.stdout.raw';
 const ls=txt(p).trimEnd().split('\n');let warnings=0;
 for(let i=0;i<ls.length;i++)if(/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!|No file/.test(ls[i])){
  let last=i+1;if(ls[i].startsWith('LaTeX Warning:'))while(last<ls.length&&ls[last]!=='')last++;
  const message=ls.slice(i,last).join('\n');let disposition;
  if(message===' file:line:error style messages enabled.')disposition='informational';
  else if(/^No file main\.(aux|bbl)\.$/.test(message)&&pass==='pass1')disposition='cold generated absence';
  else if(message.startsWith('LaTeX Warning:')&&pass!=='pass3'){disposition='resolved final';warnings++;}
  else throw Error('unresolved diagnostic '+message);
  diagnostics.push({pass,role,line:i+1,message,disposition});i=last-1;
 }
 ok(warnings===({pass1:42,pass2:5,pass3:0})[pass],'complete diagnostic count');
}
ok(txt(R+'/raw/final_diagnostics.stdout.raw')==='main.log:3: file:line:error style messages enabled.\n','only final informational match');
const fonts=txt(R+'/raw/pdffonts.stdout.raw').trimEnd().split('\n').slice(2);ok(fonts.length===17&&fonts.every(l=>/ Type 1\s+Builtin\s+yes\s+yes\s+yes\s+\d+\s+0$/.test(l)),'all17embeddedfonts');
const text=txt(R+'/raw/pdftotext.stdout.raw');ok(text.split('\f').length===8&&!/\?\?|\[\?\]|\[VERIFY\]/.test(text),'complete seven-page clean text');
ok(read(C+'/main.pdf').length===225140,'new PDF size');same(C+'/main.pdf',F+'/main.pdf');
console.log(JSON.stringify({status:'ACCEPT_A_BUILD_DATA_ORDINARY_TRUST_ONLY',checks,files:inventory.length,bytes:inventory.reduce((s,x)=>s+x.bytes,0),full_raw_baseline_pairs:sameCount,path_changed_records:pathChanged,validated_manifests:manifestCount,runtime:223,sources:9,ordered,diagnostics,pdf_sha256:sha(read(C+'/main.pdf')),fonts:17,pages:7,inventory},null,2));
