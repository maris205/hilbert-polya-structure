// Independent fixed-document receipt audit. No reviewed-source execution, Python,
// shell spawning, AST/syntax check, candidate-path traversal, or runtime queries.
'use strict';
const fs=require('node:fs'), crypto=require('node:crypto');
const q='docs/papers211_215_sequence/qa/';
const own=q+'p213_minimal_observer_source_delta_audit01/';
const delta=q+'p213_minimal_observer_source_delta01/';
const prep=q+'p213_minimal_observer_binding_preparation01/';
const old=q+'p213_minimal_observer_source01/';
const checkpoint=q+'quota_interruption_checkpoint01/';
const archive=q+'root_replays/p211_author_pair_01/child01/RUNTIME_BEFORE.json';
let checks=0;const keys=new Map(),bodies=new Map(),pairs=[],native=[];
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function ok(v,m){checks++;if(!v)throw Error(m);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const allowed=new Set([own+'KEYS_BEFORE_NATIVE.json',own+'AUTHOR_DOCUMENT_REPLAY_NATIVE.json',own+'PROGRAM_READS_NATIVE.json',own+'ADDITIONAL_READS_NATIVE.json']);
function meta(s){return Object.fromEntries(fields.map(k=>{ok(typeof s[k]==='bigint','native integer field');return[k,String(s[k])];}));}
function read(p){
 ok(allowed.has(p),'fixed documentary selection '+p);
 if(bodies.has(p))return bodies.get(p);
 const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink()&&a.nlink===1n&&a.size<10000000n,'bounded regular document');
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,m,z;
 try{const s=fs.fstatSync(fd,{bigint:true});ok(s.isFile(),'regular fd');m=meta(s);ok(eq(m,meta(a)),'initial fd/path');b=fs.readFileSync(fd);z=meta(fs.fstatSync(fd,{bigint:true}));}finally{fs.closeSync(fd);}
 ok(eq(m,z)&&eq(m,meta(fs.lstatSync(p,{bigint:true})))&&BigInt(b.length)===BigInt(m.size),'whole stable bytes');
 const k={path:p,bytes:b.length,sha256:sha(b),metadata:m};keys.set(p,k);bodies.set(p,b);return b;
}
function text(p){const b=read(p),s=b.toString('utf8');ok(Buffer.from(s,'utf8').equals(b),'lossless UTF8 document');return s;}
const json=p=>JSON.parse(text(p));
const baselineCarrier=json(own+'KEYS_BEFORE_NATIVE.json');
ok(baselineCarrier.native.exit_code===0,'real baseline exit');
const baseline=JSON.parse(baselineCarrier.native.output);
ok(baseline.keys.length===68&&baseline.checks===6912,'exact baseline census');
for(const k of baseline.keys){ok((k.path.startsWith(q+'p213_')&&!k.path.includes('..'))||k.path===archive,'baseline has only approved documents');allowed.add(k.path);}
for(const n of ['SHA256SUMS','INVENTORY.json','CHECKPOINT.md'])allowed.add(checkpoint+n);
for(const k of baseline.keys){read(k.path);ok(eq(keys.get(k.path),k),'68 full pre-audit keys unchanged');}
const inventory=[];
for(const [d,count,pin]of [[delta,24,'98ed7e008e16eef37dfb37dcbb00060cef97479957ef25f4df939b6e3314ee34'],[prep,21,'98f27ead29fa8862591d3b5a4cc6813eea1f09814f5d03a5edce0571ab278d96']]){
 const seal=text(d+'SHA256SUMS');ok(sha(Buffer.from(seal))===pin&&seal.endsWith('\n')&&!seal.endsWith('\n\n'),'strict pinned seal');
 const lines=seal.slice(0,-1).split('\n'),names=[];ok(lines.length===count,'seal count');
 for(const l of lines){const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(m&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'strict nonself unique role');names.push(m[2]);ok(sha(read(d+m[2]))===m[1],'payload pinned');}
 ok(eq(fs.readdirSync(d).sort(),[...names,'SHA256SUMS'].sort()),'complete physical inventory');
 inventory.push({path:d,payloads:count,files:count+1,bytes:[...names,'SHA256SUMS'].reduce((s,n)=>s+read(d+n).length,0),seal_sha256:pin});
 const pins=text(d+'INPUTS.sha256');ok(pins.endsWith('\n')&&!pins.endsWith('\n\n'),'strict input list');
 const ps=pins.slice(0,-1).split('\n');ok(ps.length===(d===delta?17:6),'all input pins count');
 const seen=new Set();for(const l of ps){const m=/^([a-f0-9]{64})  (docs\/[A-Za-z0-9_./-]+)$/.exec(l);ok(m&&!seen.has(m[2])&&allowed.has(m[2]),'pin allowed unique');seen.add(m[2]);ok(sha(read(m[2]))===m[1],'input raw pin');}
}
function pair(r,p,label){
 ok(r&&r.exit_code===0&&typeof r.output==='string'&&!r.session_id,'complete successful native read');
 const got=Buffer.from(r.output,'utf8'),want=read(p);ok(got.equals(want),'full raw return equals selected body '+label);
 pairs.push({label,path:p,bytes:want.length,sha256:sha(want),chunk_id:r.chunk_id});
}
for(const [d,n]of [[delta,'SOURCE_READS_NATIVE.json'],[delta,'READBACK_NATIVE.json'],[prep,'SOURCE_READS_NATIVE.json'],[prep,'FINAL_READS_NATIVE.json'],[delta,'EVIDENCE_NATIVE.json']]){
 for(const r of json(d+n).records)pair(r.result,r.path,n);
}
pair(json(delta+'CHECK_SOURCE_NATIVE.json').read.result,delta+'CHECK_DOCUMENTS.cjs','source checker full');
pair(json(prep+'CHECK_SOURCE_NATIVE.json').final_read.result,prep+'CHECK_DOCUMENTS.cjs','proposal checker full');
pair(json(prep+'CHECK_DRAFT_FAILURE_NATIVE.json').checker_full_read.result,prep+'CHECK_DOCUMENTS_DRAFT.cjs','retained failed checker full');
pair(json(prep+'EVIDENCE_NATIVE.json').evidence_final_read.result,prep+'EVIDENCE.md','proposal evidence full');
const program=json(own+'PROGRAM_READS_NATIVE.json');ok(program.length===3,'three actual program segments');
ok(Buffer.from(program.map(r=>r.native.output).join(''),'utf8').equals(Buffer.concat([read(delta+'observe.py'),read(delta+'capture.sh')])),'complete 690+40 actual program pair');
pairs.push({label:'reviewer whole program concatenation',paths:[delta+'observe.py',delta+'capture.sh'],bytes:read(delta+'observe.py').length+read(delta+'capture.sh').length,sha256:sha(Buffer.concat([read(delta+'observe.py'),read(delta+'capture.sh')]))});
pair(json(own+'ADDITIONAL_READS_NATIVE.json').responses.p213DeltaArchiveRead,archive,'reviewer full historical archive');
function diffCheck(a,b,d){
 const al=a.split('\n'),bl=b.split('\n'),dl=d.split('\n');ok(al.pop()===''&&bl.pop()===''&&dl.pop()==='','all source/diff LF complete');
 ok(dl[0].startsWith('--- ')&&dl[1].startsWith('+++ '),'diff file headers');let i=2,x=0,y=0,hunks=0;
 while(i<dl.length){
  const m=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@/.exec(dl[i++]);ok(m,'every unified hunk parsed as text');hunks++;
  const ac=m[2]===undefined?1:Number(m[2]),bc=m[4]===undefined?1:Number(m[4]);
  const ax=Number(m[1])-(ac?1:0),by=Number(m[3])-(bc?1:0);
  ok(ax>=x&&by>=y&&ax-x===by-y,'ordered unchanged gaps');ok(eq(al.slice(x,ax),bl.slice(y,by)),'unchanged gap exact');x=ax;y=by;let ca=0,cb=0;
  while(i<dl.length&&!dl[i].startsWith('@@ ')){
   const l=dl[i++],s=l[0],v=l.slice(1);ok([' ','+','-'].includes(s),'diff prefix');
   if(s!=='+' ){ok(al[x++]===v,'old-side every hunk line');ca++;}
   if(s!=='-' ){ok(bl[y++]===v,'new-side every hunk line');cb++;}
  }
  ok(ca===ac&&cb===bc,'exact old/new hunk counts');
 }
 ok(hunks>0&&eq(al.slice(x),bl.slice(y)),'complete unchanged suffix');return hunks;
}
const diffs=[];
for(const d of json(delta+'SOURCE_DIFF_NATIVE.json').records){
 ok(d.result.exit_code===1&&!d.result.session_id&&d.old.startsWith(old)&&d.new.startsWith(delta),'native differing-file record');
 ok(d.request.cmd==='diff -u -- '+d.old+' '+d.new,'exact diff request');
 const n=diffCheck(text(d.old),text(d.new),d.result.output);diffs.push({role:d.role,old:d.old,new:d.new,hunks:n,native_exit:1,diff_bytes:Buffer.byteLength(d.result.output),old_bytes:read(d.old).length,new_bytes:read(d.new).length,old_sha256:sha(read(d.old)),new_sha256:sha(read(d.new))});
}
ok(diffs.length===6,'all six diffs');
const replays=json(own+'AUTHOR_DOCUMENT_REPLAY_NATIVE.json').records;
for(const [i,d,want]of [[0,delta,5031],[1,prep,2484]]){
 const orig=json(d+'CHECK_NATIVE.json').result,now=replays[i].result;ok(orig.exit_code===0&&now.exit_code===0,'real documentary execution exits');ok(Buffer.from(orig.output).equals(Buffer.from(now.output)),'fresh documentary stdout equals archived stdout raw');
 const j=JSON.parse(now.output);ok(j.checks===want,'actual checker count');for(const k of j.keys){const current=keys.get(k.path);ok(current&&current.bytes===k.bytes&&current.sha256===k.sha256&&eq(current.metadata,k.metadata||k.ten_fields),'all author current full keys');}
 pairs.push({label:'fresh checker raw stdout versus archived original',path:d+'CHECK_NATIVE.json',bytes:Buffer.byteLength(now.output),sha256:sha(Buffer.from(now.output)),native_chunk:now.chunk_id,checks:want});
}
const resume=json(delta+'RESUMPTION_NATIVE.json');
ok(resume.document_recheck.result.exit_code===0&&Buffer.from(resume.document_recheck.result.output).equals(Buffer.from(replays[0].result.output)),'third source checker stdout exact');
const resumed=JSON.parse(resume.own19_and_checkpoint_check.result.output);ok(resume.own19_and_checkpoint_check.result.exit_code===0&&resumed.checks===67,'real resumption record');
const interrupted=resumed.keys.filter(k=>k.path.startsWith(delta));ok(interrupted.length===19&&interrupted.reduce((s,k)=>s+k.bytes,0)===1479263,'exact interrupted19');
for(const k of resumed.keys){read(k.path);ok(eq(keys.get(k.path),k),'all22 resumption full keys retained');}
const checkpointSeal=text(checkpoint+'SHA256SUMS');for(const n of ['INVENTORY.json','CHECKPOINT.md'])ok(checkpointSeal.split('\n').includes(sha(read(checkpoint+n))+'  '+n),'selected checkpoint membership');
const interruption=json(checkpoint+'INVENTORY.json').files.filter(k=>k.path.startsWith(delta));ok(eq(interruption,interrupted),'interrupted19 against independent checkpoint');
for(const [d,count,keyField]of [[delta,23,'keys'],[prep,20,'inventory']]){
 const c=json(d+'CLOSING_NATIVE.json');ok(c.result.exit_code===0,'actual closing exit');const j=JSON.parse(c.result.output);ok(j.preclosing_payloads===count,'actual preclosing inventory');
 for(const k of j[keyField]){ok(allowed.has(k.path),'closing exact documentary path');read(k.path);const a=keys.get(k.path);ok(a.bytes===k.bytes&&a.sha256===k.sha256&&eq(a.metadata,k.metadata||k.ten_fields),'all closing full keys');}
}
const fail=json(prep+'CHECK_DRAFT_FAILURE_NATIVE.json');ok(fail.result.exit_code===1&&fail.result.output.includes('Error: explicit module reason'),'real retained author failure');
ok(text(prep+'CHECK_DOCUMENTS_DRAFT.cjs').replace('x.reason.length>30','x.reason.trim().length>0')===text(prep+'CHECK_DOCUMENTS.cjs'),'one documentary reason assertion only');
const evidence=json(prep+'EVIDENCE_NATIVE.json');ok(evidence.evidence_draft_read.result.output.includes('154 lines')&&text(prep+'EVIDENCE.md').includes('137 lines / 12,401 bytes'),'incorrect prose count retained with measured correction');
const policy=json(prep+'POLICY.proposed.json'),binding=json(delta+'BINDING.disabled.json'),filter=json(prep+'ARCHIVE_FILTER.json'),arch=json(archive);
ok(binding.enabled===false&&binding.operation_authorized===false&&binding.id===null&&binding.actual_launch_record===null&&binding.actual_module_rows===null&&binding.source_pins===null&&binding.capture_pins===null,'all disabled/unobserved fields');
ok(binding.files.length===69&&Object.keys(binding.modules).length===62&&binding.module_names.early.length===23,'finite counts');
ok(eq(binding.launch_policy,policy.launch_admissibility)&&eq(binding.bounds,policy.bounds)&&eq(binding.loader_ids,policy.loader_permission_records),'exact full policy adaptation');
const candidates=new Map();for(const f of policy.files){ok(!candidates.has(f.lexical),'unique policy path');candidates.set(f.lexical,f);}
for(const f of binding.files){const p=candidates.get(f.lexical);ok(p&&p.final_policy==='must_equal_lexical'&&p.links_policy==='no_leaf_symlink','explicit lexical variant');ok(f.final===f.lexical&&eq(f.links,[])&&f.optional===p.optional&&f.earliest_phase===p.earliest_phase&&eq(f.roles,p.roles)&&f.absence_required===p.roles.includes('startup_zip_must_be_absent')&&f.observed_presence===null&&f.observed_key===null,'every file adaptation');}
const moduleCounts={};for(const [name,m]of Object.entries(binding.modules)){moduleCounts[m.mechanism]=(moduleCounts[m.mechanism]||0)+1;ok(m.observed_row===null&&!Object.hasOwn(m,'record'),'no fabricated full module row');for(const r of m.file_roles)ok(candidates.has(r.path)&&candidates.get(r.path).roles.includes(r.role),'finite role link');}
ok(eq(moduleCounts,{direct_script:1,builtin:26,source_file:30,frozen:3,extension_file:2}),'exact five mechanism counts');
ok(filter.modules.length===57&&filter.mapped_files.length===11,'complete old disposition census');for(const r of filter.modules)ok(eq(r.archived_file,arch.modules[r.name]),'old module original exact');for(const r of filter.mapped_files)ok(eq(r.archived_key,arch.mapped_files[r.path]),'old map original exact');
ok(filter.modules.filter(x=>x.disposition==='PROPOSED_FINITE_CANDIDATE').length===32&&filter.modules.filter(x=>x.disposition==='REJECT_OLD_MODULE').length===25,'complete32/25');
ok(filter.mapped_files.filter(x=>x.disposition==='PROPOSED_FINITE_CANDIDATE').length===9&&filter.mapped_files.filter(x=>x.disposition==='REJECT_OLD_ENVIRONMENT_MAP').length===2,'complete9/2');
ok(Buffer.byteLength(arch.proc_maps)===arch.proc_maps_bytes&&sha(Buffer.from(arch.proc_maps))===arch.proc_maps_sha256,'whole historical maps only');
const source=text(delta+'observe.py'),prior=text(old+'observe.py');
function region(s,n){const a=s.indexOf('def '+n+'(');ok(a>=0,'function start');const b=s.indexOf('\n\n\n',a);ok(b>a,'function end');return s.slice(a,b);}
for(const n of ['module_snapshot','attribute','loader_id','raw_maps','full_stat','key_file'])ok(region(source,n)===region(prior,n),'whole unchanged function '+n);
ok(region(source,'map_roles')===region(prior,'map_roles').replace('            need(item["inode"] > 0, "file_map_inode")','            need(phase != "early" or entries[path]["earliest_phase"] == "early", "early_map_path")\n            need(item["inode"] > 0, "file_map_inode")'),'whole map parser exact one guard and relocation');
const codes=json(delta+'FINITE_FAILURE_CODES.json').owned_codes;const block=source.slice(source.indexOf('FAILURE_CODES = (\n'),source.indexOf('\n)\n',source.indexOf('FAILURE_CODES = (\n')));ok(eq([...block.matchAll(/"([a-z_]+)"/g)].map(m=>m[1]),codes)&&codes.length===99&&new Set(codes).size===99,'99 complete finite literal codes');
ok(source.split('\n').length-1===690&&read(delta+'observe.py').length===32940,'full observer size');ok(text(delta+'capture.sh').split('\n').length-1===40,'full capture lines');
for(const d of [delta,prep])for(const n of fs.readdirSync(d).filter(n=>n.endsWith('.json'))){const j=json(d+n);walk(j,d+n);}
function walk(x,path){if(!x||typeof x!=='object')return;if(x.request&&x.result&&typeof x.result==='object'&&typeof x.result.output==='string'){ok(Number.isInteger(x.result.exit_code)&&!x.result.session_id,'finite completed native document record');native.push({carrier:path,chunk_id:x.result.chunk_id,exit_code:x.result.exit_code,bytes:Buffer.byteLength(x.result.output),sha256:sha(Buffer.from(x.result.output))});}for(const [k,v]of Object.entries(x))if(k!=='request'&&k!=='result'&&typeof v==='object')walk(v,path+'/'+k);}
for(const k of keys.values())ok(eq(meta(fs.lstatSync(k.path,{bigint:true})),k.metadata),'closing endpoint unchanged');
process.stdout.write(JSON.stringify({scope:'INDEPENDENT_DOCUMENTARY_RECEIPT_ONLY_NOT_OBSERVER_TEST',checks,baseline_keys_unchanged:68,input_pins:23,selected_checkpoint_keys:3,interrupted19_unchanged:true,inventory,pairs,raw_pair_count:pairs.length,raw_pair_bytes:pairs.reduce((s,p)=>s+p.bytes,0),diffs,complete_diff_count:6,native_records:native,module_counts:moduleCounts,source_policy_verdict_from_this_checker:false,observer_executed:false,capture_executed:false,installed_paths_inspected:false,keys:[...keys.values()]},null,2)+'\n');
