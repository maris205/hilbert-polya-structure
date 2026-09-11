'use strict';
// Root documentary receiver. No received code is evaluated or imported.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics/',Q='docs/papers211_215_sequence/qa/';
const A=Q+'p212_execution_scope_source_amendment01/',O=Q+'p212_dependency_source_root01/',SELF=Q+'p212_execution_scope_amendment_root01/';
let checks=0;const inputs=new Map(),packages=[],native=[];
const eq=(a,b,m)=>{assert.deepEqual(a,b,m);checks++;},yes=(x,m)=>{assert.ok(x,m);checks++;};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),bp=b=>({bytes:b.length,sha256:sha(b)});
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
function abs(p){yes(typeof p==='string'&&!p.startsWith('/')&&!p.split('/').some(x=>['..','.',''].includes(x)),'bounded workspace input '+p);return ROOT+p;}
function st(s){return Object.fromEntries(fields.map(k=>{yes(typeof s[k]==='bigint','integer '+k);return[k,String(s[k])];}));}
function key(p){const a=abs(p),l=fs.lstatSync(a,{bigint:true}),s=fs.statSync(a,{bigint:true}),resolved=fs.realpathSync(a);yes(s.isFile()&&resolved.startsWith(ROOT),'workspace regular referent '+p);return{path:p,...bp(fs.readFileSync(a)),resolved,lstat:st(l),stat:st(s)};}
function stable(a,b,label){eq(a.path,b.path,label+' path');eq(a.bytes,b.bytes,label+' bytes');eq(a.sha256,b.sha256,label+' SHA');eq(a.resolved,b.resolved,label+' realpath');for(const kind of ['lstat','stat'])for(const f of fields.filter(x=>x!=='atimeNs'))eq(a[kind][f],b[kind][f],label+' '+kind+'.'+f);}
function read(p){const k=key(p);if(inputs.has(p))stable(inputs.get(p),k,'repeat '+p);else inputs.set(p,k);const b=fs.readFileSync(abs(p));eq(bp(b),{bytes:k.bytes,sha256:k.sha256},'actual whole read '+p);return b;}
const json=p=>JSON.parse(read(p));
function rows(p){const text=read(p).toString('utf8');yes(text.endsWith('\n'),'manifest LF');const r=text.slice(0,-1).split('\n').map(x=>{const m=/^([a-f0-9]{64})  ([^\r\n]+)$/.exec(x);yes(m,'manifest syntax');abs(m[2]);return{sha256:m[1],path:m[2]};});eq(new Set(r.map(x=>x.path)).size,r.length,'no duplicate manifest');return r;}
function census(base){const files=[],directories=[];function walk(d){for(const name of fs.readdirSync(ROOT+base+d).sort()){const r=d+name,s=fs.lstatSync(ROOT+base+r);yes(!s.isSymbolicLink(),'package no symlinks');if(s.isDirectory()){directories.push(r);walk(r+'/');}else{yes(s.isFile(),'regular package');files.push(r);}}}walk('');return{files:files.sort(),directories:directories.sort(),empty_directories:directories.filter(d=>!files.some(f=>f.startsWith(d+'/'))).sort()};}
function seal(base,expected){const b=read(base+'SHA256SUMS'),r=rows(base+'SHA256SUMS'),c=census(base);eq(c.files,[...r.map(x=>x.path),'SHA256SUMS'].sort(),'complete membership '+base);for(const x of r)eq(sha(read(base+x.path)),x.sha256,'payload '+base+x.path);const item={base,payloads:r.length,files:c.files.length,seal:bp(b),directories:c.directories,empty_directories:c.empty_directories};if(expected)eq(item,expected,'accepted full package '+base);packages.push(item);return item;}
read(SELF+'PLAN.md');read(SELF+'receive_author.js');
const old=json(O+'RESULT.json');eq(old.inputs.length,150,'accepted complete key');
for(const r of old.inputs){read(r.path);stable(r,inputs.get(r.path),'accepted baseline '+r.path);}
seal(O);for(const p of old.packages)seal(p.base,p);
for(const r of old.input_pin_lists){eq(bp(read(r.path)),r.pin,'pinlist origin');const list=rows(r.path);eq(list.length,r.entries,'pinlist count');for(const e of list)eq(sha(read(e.path)),e.sha256,'entire workspace pinlist');}
const authored=seal(A);eq(authored.payloads,22,'whole author payload count');eq(authored.seal,{bytes:2026,sha256:'63c4518179e5213cbd8ea3b6802250b6be9b2a73d46050ea205b057612505f94'},'fixed author seal');
const origin=json(A+'SOURCE_ORIGIN.json'),rich=json(A+'DOCUMENTARY_RICH_PINS.json'),log=json(A+'NATIVE_READS.json');
eq(rich.paths.length,66,'author whole corrected key');eq(rich.integer_fields,fields,'all fields declaration');
for(const r of rich.paths){read(r.path);const current=inputs.get(r.path);for(const phase of ['before','after'])stable({path:r.path,bytes:r.bytes,sha256:r['sha256_'+phase],resolved:r['resolved_'+phase],lstat:r['lstat_'+phase],stat:r['stat_'+phase]},current,'author '+phase+' '+r.path);}
const chunks=new Map(log.captures.map(r=>[r.result.chunk_id,r]));eq(chunks.size,log.captures.length,'distinct author native chunks');
function nativeResult(chunk){const r=chunks.get(chunk);yes(r,'real captured chunk');eq(r.result.exit_code,0,'native completion '+chunk);yes(typeof r.result.output==='string','native whole text');return r;}
for(const [chunk,kind,phase] of [['b6def2','lstat','before'],['037ee9','stat','before'],['a142f6','lstat','after'],['1fe81e','stat','after']]){
  const r=nativeResult(chunk),ls=r.result.output.trimEnd().split('\n');eq(ls.length,66,'whole corrected stat native');eq(r.command.includes('stat -L '),kind==='stat','dereference mode');
  eq(r.command.split(' -- ')[1].split(' '),rich.paths.map(x=>x.path),'exact stat argv paths');
  for(let i=0;i<ls.length;i++){const v=ls[i].split('|');eq(v.length,20,'whole native stat row');eq(v[0],rich.paths[i].path,'stat row order');
    const ns=(seconds,text)=>{const m=/\.(\d{9}) [+-]\d{4}$/.exec(text);yes(m,'native nine digits');return String(BigInt(seconds)*1000000000n+BigInt(m[1]));};
    const major=BigInt('0x'+v[7]),minor=BigInt('0x'+v[8]);
    const rdev=(minor&255n)|((major&4095n)<<8n)|((minor&~255n)<<12n)|((major&~4095n)<<32n);
    const decoded={dev:v[1],ino:v[2],mode:String(BigInt('0x'+v[3])),nlink:v[4],uid:v[5],gid:v[6],rdev:String(rdev),size:v[9],blksize:v[10],blocks:v[11],atimeNs:ns(v[12],v[13]),mtimeNs:ns(v[14],v[15]),ctimeNs:ns(v[16],v[17]),birthtimeNs:ns(v[18],v[19])};
    eq(decoded,rich.paths[i][kind+'_'+phase],'raw all14 metadata '+chunk+' '+v[0]);
  }native.push({chunk,role:'corrected complete native14',rows:66});
}
for(const chunk of ['c7055f','63db24']){const r=nativeResult(chunk);eq(r.result.output.trimEnd().split('\n').map(x=>x.split('|')[7]),Array(66).fill('?'),'failed unsupported rdev remains');}
for(const [phase,hchunk,rchunk] of [['before','3d6bf4','885913'],['after','c2985e','edd8f9']]){
 eq(nativeResult(hchunk).result.output,rich.paths.map(x=>x['sha256_'+phase]+'  '+x.path+'\n').join(''),'whole native hash listing');
 eq(nativeResult(rchunk).result.output,rich.paths.map(x=>x['resolved_'+phase]+'\n').join(''),'whole native realpaths');
}
for(const r of log.captures){const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(r.command);if(m&&r.result.exit_code===0){const out=m[3].split(' ').map(p=>{const s=read(p).toString('utf8'),ls=s.match(/[^\n]*\n|[^\n]+$/g)||[];return ls.slice(Number(m[1])-1,Number(m[2])).join('');}).join('');eq(r.result.output,out,'entire actual source range '+r.result.chunk_id);native.push({chunk:r.result.chunk_id,role:'raw complete sed range',bytes:Buffer.byteLength(out)});}
 const c=/^cmp -- (\S+) (\S+)$/.exec(r.command);if(c){eq(r.result.exit_code,0,'archived cmp exit');eq(r.result.output,'','archived cmp whole stream');yes(read(c[1]).equals(read(c[2])),'current full raw operands');native.push({chunk:r.result.chunk_id,role:'actual archived cmp received',operands:c.slice(1)});}
}
eq(origin.native_copy_checks.length,14,'origin original cmp count');for(const x of origin.native_copy_checks){const r=nativeResult(x.chunk);eq(r.command,x.command,'copy receipt original vector');eq(r.result.output,x.stdout,'copy receipt original output');}
const diffs=log.captures.filter(x=>x.command.startsWith('diff -u '));eq(diffs.length,4,'complete four native diffs');
for(const d of diffs)eq(d.result.exit_code,1,'real changed diff exit');
eq(read(A+'AMENDMENT.diff').toString('utf8'),diffs.map(x=>x.result.output).join(''),'all four raw native deltas');eq(read(A+'DRIVER.diff').toString('utf8'),diffs[0].result.output,'complete narrow diff');
for(const d of origin.complete_diffs){eq(bp(read(d.old)),d.old_pin,'old delta operand');eq(bp(read(d.new)),d.new_pin,'new delta operand');}
let expectedDriver=read(origin.driver.old_path).toString('utf8');eq(origin.driver.exact_literal_operations.length,6,'six source literals');
for(const r of origin.driver.exact_literal_operations){eq(expectedDriver.split(r.before).length,2,'one exact literal occurrence');expectedDriver=expectedDriver.replace(r.before,r.after);}
eq(Buffer.from(expectedDriver),read(origin.driver.new_path),'entire derivative exactly six literals');
const frontier=json(origin.frontier.old_path);frontier.profile.source_graph_path=A+'SOURCE_GRAPH.json';frontier.profile.source_pins['sections/05_scope.tex']={bytes:1237,sha256:'44ab0ee97ab09a7bd0d68ddaf116d74f43314f69ef00821a77b67282d851012d'};frontier.profile.source_bytes=20092;
eq(Buffer.from(JSON.stringify(frontier,null,2)+'\n'),read(origin.frontier.new_path),'whole four-value frontier derivative');eq(frontier.initial_name_seeds.length,19,'same nineteen contexts');
const graph=json(A+'SOURCE_GRAPH.json');eq(graph.source_pins,frontier.profile.source_pins,'amended graph pins');eq(graph.historical_source_pins,json(Q+'p212_initial_build_preparation01/SOURCE_GRAPH.json').source_pins,'explicit historical source identity');eq(graph.paper_root,'papers/212-closed-pointer-orbits','future live target not capsule');
for(const [name,p] of Object.entries(graph.source_pins)){eq(bp(read(A+'source_only/'+name)),p,'physical prospective source');const live=read(graph.paper_root+'/'+name),oldphysical=read(graph.accepted_source_original_root+'/'+name);yes(live.equals(oldphysical),'live still historical raw pair');eq(bp(live),graph.historical_source_pins[name],'old live source full pin');if(name!=='sections/05_scope.tex')yes(live.equals(read(A+'source_only/'+name)),'seven whole unchanged sources');}
eq(Object.values(graph.source_pins).reduce((s,x)=>s+x.bytes,0),20092,'new eight-source size');eq(Object.values(graph.historical_source_pins).reduce((s,x)=>s+x.bytes,0),19659,'old eight-source size');
for(const r of origin.companions.whole_files)eq(bp(read(r.path)),r.pin,'complete companion');for(const n of origin.companions.unchanged_raw_copies)yes(read(A+'companions/'+n).equals(read(Q+'p212_build_dependency_source_preparation01/'+n)),'raw unchanged companion');
yes(read(A+'INTERFACE.disabled.json').equals(read(Q+'p212_dependency_query_driver_revision02/INTERFACE.disabled.json')),'whole separate driver disabled');
for(const r of origin.prose_origin.accepted_prose_evidence_input_pins)eq(bp(read(r.path)),{bytes:r.bytes,sha256:r.sha256},'all sentence evidence input '+r.id);
const cb=read('papers/212-closed-pointer-orbits/CANONICAL.json');eq(bp(cb),{bytes:12501943,sha256:'1a32be6bb36dd8b4b27b9891a42876fe235bf2555a3dd9f4e36195a6ad72676c'},'entire unchanged canonical');
for(const [dir,cmd] of [['p212_author_initial_01','03_verify_01'],['p212_author_pair_01','03_verify_01'],['p212_author_pair_01','03_verify_02']]){const base=Q+'root_replays/'+dir+'/recorder/commands/'+cmd+'/',raw=read(base+'stdout.raw'),receipt=json(base+'RECEIPT.json');yes(raw.equals(cb),'all actual raw outputs equal canonical');eq(receipt.stdout,bp(raw),'actual whole raw binding');eq(receipt.exit_code,0,'actual producer exit');eq(receipt.wrapper_exit_code,0,'actual wrapper exit');eq(receipt.streams_complete,true,'streams complete');eq(read(base+'stderr.raw').length,0,'raw stderr');const j=JSON.parse(raw);eq(j.summary.predicate_count,72476,'named count');eq(j.predicate_census.length,46,'classes');eq(j.summary.state_count,4356,'states');eq(j.parameters.carrier_sizes,[1,2,3,4],'four old boxes');eq(j.coverage_limits.map(x=>x.first_core_size),[5,6,5],'deductive limits');}
const semantic=json(Q+'p212_saved_output_root_reception01/initial02/commands/02_saved_output/stdout.raw');eq(semantic.semantic_checks,12375789,'separate original semantic count');eq(semantic.scientific_producer_invocations,0,'not new producer');
const pair=json(Q+'p212_author_pair_runtime_reception01/CLOSING_RESULT.json');eq(pair.new_semantic_reconstruction,false,'original pair explicit semantic reuse');eq(pair.semantic_evidence_reused_checks,12375789,'explicit original semantic count');
for(const [p,k] of inputs)stable(k,key(p),'final complete key '+p);
process.stdout.write(JSON.stringify({schema:'p212-execution-amendment-root-author-reception-v1',status:'PASS_AUTHOR_SOURCE_DOCUMENTS_BASELINE_AND_CORRECTED_NATIVE_NOT_YET_INDEPENDENT_ACCEPTANCE',checks,input_paths:inputs.size,packages,accepted_baseline_inputs:150,author_corrected_inputs:66,author_raw_native_bindings:native,driver:origin.driver.new_pin,frontier:origin.frontier.new_pin,live_source_status:'UNCHANGED_OLD_PROFILE_19659',prospective_source_bytes:20092,authority:{source_execution:false,query:false,build:false,new_science:false,new_semantic_reconstruction:false,live_application:false},inputs:[...inputs.values()]})+'\n');
