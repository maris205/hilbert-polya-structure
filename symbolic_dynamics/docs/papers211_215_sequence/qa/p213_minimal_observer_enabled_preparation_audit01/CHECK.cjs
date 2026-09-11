'use strict';
// Independent documentary intake and exact prospective derivative check.
// No Python/Bash parser, import, compilation, command, observer or future-path I/O.
const fs=require('node:fs'),crypto=require('node:crypto'),path=require('node:path');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const QA='docs/papers211_215_sequence/qa/';
const P=QA+'p213_minimal_observer_enabled_preparation01/';
const A=QA+'p213_minimal_observer_enabled_preparation_audit01/';
const S=QA+'p213_minimal_observer_source_delta01/';
const FUTURE=ROOT+QA+'p213_minimal_observer_enabled01/'; // documentary string only
const OWN=['PLAN.md','ORIENTATION_NATIVE.json','KEY_DOCUMENTS.cjs','BASELINE_NATIVE.json','PROGRAM_READS_NATIVE.json','CONTRACT_READS_NATIVE.json','POLICY_READS_NATIVE.json','CHECKER_READS_NATIVE.json','AUTHOR_REPLAYS_NATIVE.json','PREDECESSOR_READS_NATIVE.json','ARTIFACT_SHAPES_NATIVE.json','DIFF_READS_NATIVE.json','CHECK.cjs'];
let checks=0;const rawPairs=[],records=[],keyCache=new Map(),buffers=new Map();
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function ok(v,m){checks++;if(!v)throw new Error(m);}
const baselineNative=JSON.parse(fs.readFileSync(ROOT+A+'BASELINE_NATIVE.json','utf8'));
ok(baselineNative.result.exit_code===0,'actual independent baseline exit');
const baseline=JSON.parse(baselineNative.result.output).keys;
ok(baseline.length===53,'exact baseline size');
const allowed=new Set([...baseline.map(k=>k.path),...OWN.map(n=>A+n)]);
const mf=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'];
const authorMF=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(mf.map(k=>[k,s[k].toString()]));
function same(a,b,label){
  ok(typeof a===typeof b,label+' type');
  if(a===null||b===null||typeof a!=='object'){ok(Object.is(a,b),label+' scalar');return;}
  ok(Array.isArray(a)===Array.isArray(b),label+' array/dict');
  const x=Object.keys(a),y=Object.keys(b);ok(JSON.stringify(x)===JSON.stringify(y),label+' keys/order');
  x.forEach(k=>same(a[k],b[k],label+'/'+k));
}
function acquire(p,force=false){
  ok(allowed.has(p),'outside independent finite document list '+p);
  ok(!p.includes('/p213_minimal_observer_enabled01/')&&!p.includes('/p213_minimal_observer_probe01/'),'future path must not be operand');
  if(!force&&buffers.has(p))return buffers.get(p);
  const file=ROOT+p,a=fs.lstatSync(file,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular no-link document');
  const fd=fs.openSync(file,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);let b,k;
  try{const f=fs.fstatSync(fd,{bigint:true});b=fs.readFileSync(fd);const g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(file,{bigint:true});for(const v of [f,g,z])same(meta(a),meta(v),'same-fd/end-path full metadata '+p);ok(BigInt(b.length)===a.size,'whole EOF length');k={path:p,type:'regular',...meta(a),bytes:b.length,sha256:sha(b)};}finally{fs.closeSync(fd);}
  if(keyCache.has(p))same(keyCache.get(p),k,'whole repeat key '+p);else keyCache.set(p,k);
  buffers.set(p,b);return b;
}
const doc=n=>acquire(P+n),str=n=>doc(n).toString('utf8'),json=n=>JSON.parse(str(n));
const own=n=>JSON.parse(acquire(A+n).toString('utf8'));
function raw(a,b,label){a=Buffer.isBuffer(a)?a:Buffer.from(a);b=Buffer.isBuffer(b)?b:Buffer.from(b);ok(a.equals(b),'raw byte comparison '+label);rawPairs.push({label,bytes:a.length,sha256:sha(a)});}
for(const k of baseline){acquire(k.path);same(k,keyCache.get(k.path),'independent baseline unchanged');}
const sealHash='daa0bc55ab3e1f8f2e9cc97ff846508434b0ac6f65e6ed84e9559f5fad9f049d';
ok(sha(doc('SHA256SUMS'))===sealHash,'current package external seal anchor');
function parseSeal(s){ok(s.endsWith('\n'),'seal newline');const out=s.slice(0,-1).split('\n').map(line=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);ok(!!m,'strict nonrecursive seal grammar');return {name:m[2],sha256:m[1]};});ok(new Set(out.map(x=>x.name)).size===out.length,'unique seal members');return out;}
const payloads=parseSeal(str('SHA256SUMS'));ok(payloads.length===32,'32 current payloads');
same(fs.readdirSync(ROOT+P).sort(),[...payloads.map(x=>x.name),'SHA256SUMS'].sort(),'complete physical package inventory');
for(const p of payloads){ok(p.name!=='SHA256SUMS','nonself');ok(sha(doc(p.name))===p.sha256,'every sealed payload '+p.name);}
const physicalBytes=[...payloads.map(x=>x.name),'SHA256SUMS'].reduce((s,n)=>s+doc(n).length,0);ok(physicalBytes===1177073,'physical package bytes');
ok(sha(doc('HANDOFF.md'))==='8baf0431456d76a3385decf937c4b4d0bef20dcc155ae3618b20db733d2fde2d','external handoff anchor');
const pinLines=str('INPUTS.sha256').trimEnd().split('\n');ok(pinLines.length===16,'all old pins');
const pins=pinLines.map(line=>{const m=/^([0-9a-f]{64})  (docs\/papers211_215_sequence\/qa\/[A-Za-z0-9_]+\/[A-Za-z0-9_.]+)$/.exec(line);ok(!!m,'pin grammar');ok(allowed.has(m[2])&&!m[2].startsWith(P),'selected old input only');ok(sha(acquire(m[2]))===m[1],'old pin content');return {path:m[2],sha256:m[1]};});
raw(str('INPUTS.sha256'),pins.map(x=>x.sha256+'  '+x.path+'\n').join(''),'whole old input manifest');
for(const dir of ['p213_minimal_observer_source_delta01','p213_minimal_observer_source_delta_root01','p213_minimal_observer_source_delta_audit01','p213_minimal_observer_binding_preparation01']){
  const prefix=QA+dir+'/';const rows=parseSeal(acquire(prefix+'SHA256SUMS').toString('utf8'));
  for(const x of pins.filter(x=>x.path.startsWith(prefix)&&!x.path.endsWith('/SHA256SUMS')))ok(rows.find(r=>r.name===x.path.slice(prefix.length))?.sha256===x.sha256,'selected member in accepted predecessor seal');
}
function checkAuthorKey(k,label){
  ok(allowed.has(k.path),'author record has finite accepted documentary path '+label);acquire(k.path);const n=keyCache.get(k.path);
  ok(k.sha256===n.sha256&&k.bytes===n.bytes,'author complete content key '+label);
  const expected=Object.fromEntries(authorMF.map(f=>[f,n[f]]));
  same(k.metadata,expected,'author complete metadata '+label);same(k.fd_end,expected,'author same fd '+label);same(k.path_end,expected,'author path end '+label);
  same(k.leaf_links,[],'author no leaf link');ok(k.full_eof===true,'author full EOF');
}
function native(id,r){
  ok(r&&r.request&&typeof r.request==='object','exact native request '+id);
  const v=r.result;ok(v&&typeof v.output==='string'&&Number.isInteger(v.exit_code),'native complete return '+id);
  ok(typeof v.chunk_id==='string'&&typeof v.wall_time_seconds==='number'&&Number.isInteger(v.original_token_count),'native metadata '+id);
  ok(!('session_id' in v),'no incomplete native session '+id);
  records.push({id,request:r.request,chunk:v.chunk_id,exit:v.exit_code,outputBytes:Buffer.byteLength(v.output),outputSha256:sha(v.output),returnJsonSha256:sha(JSON.stringify(v)),toolTruncated:/^Warning: truncated output \(original token count:/m.test(v.output)});
  return v;
}
const ori=json('ORIENTATION_NATIVE.json');native('orientation/absence',ori.absence);ori.reads.forEach((r,i)=>native('orientation/read/'+i,r));
ok(ori.absence.result.exit_code===0&&ori.absence.request.cmd==='test ! -e '+P.slice(0,-1),'author own artifact absence only');
const navigation=ori.reads.find(x=>x.role==='request');ok(navigation.result.exit_code===2&&navigation.path===S+'REQUEST.disabled.json','original missing documentary path failure');
raw(navigation.result.output,"sed: can't read "+S+"REQUEST.disabled.json: No such file or directory\n",'exact original missing-path diagnostic');
for(const r of ori.reads.filter(x=>x.role==='skill'||x.role==='workflow'))raw(r.result.output,acquire(r.path),'whole original instruction read '+r.role);
const sourceReads=json('SOURCE_READS_NATIVE.json').reads;ok(sourceReads.length===16,'complete author input read census');
sourceReads.forEach((r,i)=>{native('source/'+i,r);ok(r.result.exit_code===0&&r.path===pins[i].path,'exact input read identity');raw(r.result.output,acquire(r.path),'whole author predecessor read '+r.role);});
for(const [file,count] of [['INPUT_KEYS_NATIVE.json',16],['PREPARED_KEYS_NATIVE.json',11]]){const r=json(file);native(file,r);ok(r.result.exit_code===0,'key acquisition success');const ks=JSON.parse(r.result.output).keys;ok(ks.length===count,'all original key records');ks.forEach(k=>checkAuthorKey(k,file));}
const oldBinding=JSON.parse(acquire(S+'BINDING.disabled.json').toString('utf8')),b=json('BINDING.prepared.json'),projection=json('BINDING.runtime_literal.json');
const leafChanges=[];
function differences(x,y,p=''){
  if(x===null||y===null||typeof x!=='object'||typeof y!=='object'){if(!Object.is(x,y))leafChanges.push({path:p,before:x,after:y});return;}
  same(Object.keys(x),Object.keys(y),'unchanged binding object layout '+p);for(const k of Object.keys(x))differences(x[k],y[k],p+'/'+k);
}
differences(oldBinding,b);
const relocationPaths=['/observer','/launch_policy/argv/0','/launch_policy/orig_argv/4','/modules/__main__/file','/modules/__main__/file_roles/0/path','/files/0/lexical','/files/0/final'];
const expectedChanged=[...relocationPaths,'/schema','/id','/modules/__main__/provenance','/source_pins','/note'].sort();
same(leafChanges.map(x=>x.path).sort(),expectedChanged,'all and only twelve binding value changes');
for(const p of relocationPaths){const c=leafChanges.find(x=>x.path===p);ok(c.before===oldBinding.observer&&c.after===FUTURE+'observe.py','exact seven observer relocations');}
ok(b.schema==='P213_FINITE_PERMISSION_BINDING_PREPARED_DISABLED_V1'&&b.id==='P213_MINIMAL_FINITE_PERMISSION_OBSERVER_ENABLED01','exact schema/id');
ok(b.modules.__main__.provenance==='New prospective enabled01 path explicitly selected for this preparation; not a current presence or executed-source fact','exact main provenance');
ok(b.enabled===false&&b.operation_authorized===false&&b.capture_pins===null,'preparation flags unresolved capture');
for(const [role,k] of Object.entries(b.source_pins)){if(role==='scope')continue;ok(k.path.startsWith(ROOT),'old source pin path');const p=k.path.slice(ROOT.length);ok(pins.some(x=>x.path===p),'old pin role only');ok(k.sha256===sha(acquire(p))&&k.bytes===acquire(p).length,'every external documentary predecessor commitment');}
const consumed=['id','interpreter','observer','cwd','launch_policy','flag_names','module_names','required_module_names','modules','loader_ids','special_maps','files','bounds'];
same(Object.keys(projection),consumed,'exact projected keys');for(const name of consumed)same(projection[name],b[name],'entire consumed field '+name);
same(json('CONSUMPTION_MAP.json').consumed_top_level_fields,consumed,'declared consumption');same(json('CONSUMPTION_MAP.json').documentary_only_top_level_fields,Object.keys(b).filter(x=>!consumed.includes(x)),'all unconsumed fields');
function literalDomain(x){
  if(x===null||typeof x==='boolean')return;
  if(typeof x==='number'){ok(Number.isSafeInteger(x)&&!Object.is(x,-0),'exact integer literal');return;}
  if(typeof x==='string'){ok(/^[\x20-\x7e]*$/.test(x),'printable ASCII literal string');return;}
  ok(typeof x==='object','literal data type');for(const [k,v] of Object.entries(x)){if(!Array.isArray(x))literalDomain(k);literalDomain(v);}
}
literalDomain(projection);
// Independent JSON-lexeme transcoder: only bare null/true/false outside JSON
// strings are changed, unlike the author's recursive pretty-printer.
const lexemes=str('BINDING.runtime_literal.json').match(/"(?:[^"\\]|\\.)*"|\b(?:null|true|false)\b|[^"ntf]+|./gs);
ok(lexemes.join('')===str('BINDING.runtime_literal.json'),'complete JSON token coverage');
const translations={null:'None',true:'True',false:'False'};
const literal=lexemes.map(t=>Object.hasOwn(translations,t)?translations[t]:t).join('');
raw(literal,doc('BINDING.literal.txt'),'complete independent JSON-token-to-literal projection');
same(b.interpreter,b.files.find(x=>x.lexical===b.interpreter.lexical),'full interpreter duplicate including nulls');
ok(Object.keys(b.modules).length===62&&b.files.length===69&&b.module_names.early.length===23,'finite domain counts');
for(const phase of ['early','helper','closing']){ok(new Set(b.module_names[phase]).size===b.module_names[phase].length,'unique phase names');ok(b.required_module_names[phase].every(x=>b.module_names[phase].includes(x)),'required core membership');}
same(b.module_names.helper,b.module_names.closing,'helper and closing exact support');
same(b.bounds,oldBinding.bounds,'all unchanged bounds');same(b.launch_policy.flag_requirements,oldBinding.launch_policy.flag_requirements,'all unchanged typed flag values');
ok(b.launch_policy.flag_requirements.dev_mode===false,'boolean dev_mode not zero');
ok(b.actual_launch_record===null&&b.actual_module_rows===null&&b.launch_policy.full_actual_record===null,'no proposed actual rows');
for(const [name,m] of Object.entries(b.modules))ok(m.observed_row===null,'no actual module claim '+name);
for(const f of b.files){ok(f.lexical===f.final&&f.links.length===0,'finite no-leaf-link policy');ok(f.observed_presence===null&&f.observed_key===null,'no actual file key claim');}
const zip=b.files.filter(x=>x.absence_required);ok(zip.length===1&&zip[0].lexical==='/usr/lib/python310.zip'&&zip[0].optional===true,'exact required ENOENT zip');
const oldObserver=acquire(S+'observe.py').toString('utf8'),oldCapture=acquire(S+'capture.sh').toString('utf8');
const suffixAt=oldObserver.indexOf('if BINDING is None:\n');ok(suffixAt>0&&oldObserver.indexOf('if BINDING is None:\n',suffixAt+1)===-1,'unique accepted collector suffix anchor');
const suffix=oldObserver.slice(suffixAt),ogate='raise SystemExit("P213_OBSERVER_DISABLED_ENABLED_PREPARATION")\n';
const header='"""P213 exact finite-permission observer; operational authority is external."""\n\n# The preparation copy has an unconditional gate before its complete literal.\n';
const literalIntro='# Literal permissions only; never loaded from a file or predicted actual rows.\nBINDING = ';
raw(str('observe.py'),header+ogate+literalIntro+literal+suffix,'whole disabled observer exact derivation');
raw(str('observe.proposed.py.txt'),header+literalIntro+literal+suffix,'whole prospective observer exact derivation');
const bodyAt=oldCapture.indexOf('P213_CAPTURE_ENV=');ok(bodyAt>0,'accepted capture body start');
const oldBody=oldCapture.slice(bodyAt);ok(oldBody.split(oldBinding.observer).length===2,'unique observer constant in accepted capture body');
const captureBody=oldBody.replace(oldBinding.observer,FUTURE+'observe.py');
const cgate="printf '%s\\n' 'P213_CAPTURE_DISABLED_ENABLED_PREPARATION' >&2\nexit 78\n";
const cheader='# P213 exact finite-permission capture; operational authority is external.\n# The preparation copy has an unconditional gate before cwd/allocation.\n';
const comment='\n# Chosen paths are permissions, not observations of tool identity or presence.\n# Ordinary trusted bootstrap/filesystem limits are specified in PREPARATION.md.\n';
raw(str('capture.sh'),cheader+cgate+comment+captureBody,'whole disabled capture exact derivation');
raw(str('capture.proposed.sh.txt'),cheader+comment+captureBody,'whole prospective capture exact derivation');
const transformations=json('TRANSFORMATION.json');ok(transformations.operation_authorized===false&&transformations.materialized===false&&transformations.operations.length===2,'exact nonoperational transform');
for(const [n,out,gate,future] of [['observe.py','observe.proposed.py.txt',ogate,FUTURE+'observe.py'],['capture.sh','capture.proposed.sh.txt',cgate,FUTURE+'capture.sh']]){
  const t=transformations.operations.find(x=>x.prepared===n);ok(!!t&&t.proposed_text_carrier===out&&t.future_path===future,'exact transformation identities');ok(t.remove_exact_bytes===gate&&str(n).split(gate).length===2,'unique exact removal block');raw(str(n).replace(gate,''),doc(out),'complete declared gate removal '+n);
}
const used=[...new Set([...suffix.matchAll(/\bBINDING\["([^"\n]+)"\]/g)].map(m=>m[1]))].sort();same(used,[...consumed].sort(),'literal consumption covers complete accepted source');
ok(!suffix.includes('BINDING.get(')&&!suffix.includes('BINDING.items('),'no alternate top-level iteration/access');
const request=json('CAPTURE_REQUEST.disabled.json'),proposed=json('PROPOSED_REQUEST.json'),manifest=json('PROSPECTIVE_BYTES.json');
ok(request.request.cmd===null&&request.enabled===false&&request.operation_authorized===false&&request.output_directory_observed_absence===null,'disabled current request');
same(request.source_pins,b.source_pins,'request and documentary source commitments');
same(proposed.proposed_request,{cmd:"exec /usr/bin/env -i LANG=C LC_ALL=C /bin/bash --noprofile --norc '"+FUTURE+"capture.sh'",workdir:ROOT.slice(0,-1),shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:4000},'exact prospective tool request');
ok(proposed.enabled===false&&proposed.operation_authorized===false&&proposed.review_accepted===false&&proposed.actual_materialized===false&&proposed.actual_session_id===null&&proposed.actual_output_directory_absence===null,'all unobserved/ungranted request fields');
same(proposed.continuation,{tool:'write_stdin',only_if_actual_session_id_returned:true,chars:'',session_id:null,no_restart:true,no_retry:true},'no invented session/retry');
ok(request.capture_source===FUTURE+'capture.sh'&&request.observer_source===FUTURE+'observe.py','request source path agreement');
ok(request.capture_directory===ROOT+QA+'p213_minimal_observer_probe01'&&request.stdout_path===request.capture_directory+'/stdout.bin'&&request.stderr_path===request.capture_directory+'/stderr.bin','unchanged separate output strings');
same(request.child_environment,{LANG:'C',LC_ALL:'C'},'two-key child environment');same(request.flags,['-I','-S','-B'],'exact interpreter flags');
ok(manifest.current_documentary_artifacts.length===11&&manifest.proposed_future_artifacts.length===2,'all external byte commitments');
for(const m of manifest.current_documentary_artifacts){ok(allowed.has(P+m.path),'current carrier operand only');ok(doc(m.path).length===m.bytes&&sha(doc(m.path))===m.sha256,'every external current-byte commitment');}
for(const [n,bytes,digest,future] of [['observe.proposed.py.txt',98365,'6cdc550357b0b6f8322ecc8e22d2fca9ff1d22ee5d9a46caf0c191fcc81ff25d',FUTURE+'observe.py'],['capture.proposed.sh.txt',1949,'da71d93c5fd8c587ecbdeec339e054b6c6c0aa56a5c682b901a1c3c038b8705d',FUTURE+'capture.sh']]){
  ok(doc(n).length===bytes&&sha(doc(n))===digest,'root-supplied exact prospective anchor');same(manifest.proposed_future_artifacts.find(x=>x.carrier===n),{carrier:n,future_path:future,proposed_bytes:bytes,proposed_sha256:digest,actual_future_metadata:null,actual_future_presence:null,actual_future_hash:null},'future artifact remains a commitment not a key');
}
function diffCheck(d){
  native('diff/'+d.role,d);ok(d.result.exit_code===1,'true native difference exit');
  const old=acquire(d.oldPath).toString('utf8'),next=acquire(d.newPath).toString('utf8'),text=d.result.output;
  ok([old,next,text].every(x=>x.endsWith('\n')),'whole LF diff sources');
  const x=old.slice(0,-1).split('\n'),y=next.slice(0,-1).split('\n'),z=text.slice(0,-1).split('\n');
  ok(z[0].startsWith('--- '+d.oldPath+'\t')&&z[1].startsWith('+++ '+d.newPath+'\t'),'both diff path headers');
  let i=0,j=0,k=2,hunks=0;
  while(k<z.length){const m=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@.*$/.exec(z[k++]);ok(!!m,'exact hunk syntax');const ac=m[2]===undefined?1:+m[2],bc=m[4]===undefined?1:+m[4],ai=+m[1]-(ac?1:0),bi=+m[3]-(bc?1:0);ok(ai>=i&&bi>=j,'nonoverlap');same(x.slice(i,ai),y.slice(j,bi),'complete unchanged gap');i=ai;j=bi;let u=0,v=0;while(k<z.length&&!z[k].startsWith('@@ ')){const t=z[k++],mark=t[0],line=t.slice(1);ok(' +-'.includes(mark),'valid full hunk line');if(mark!=='+'){ok(x[i++]===line,'exact old line');u++;}if(mark!=='-'){ok(y[j++]===line,'exact new line');v++;}}ok(u===ac&&v===bc,'whole hunk line counts');hunks++;}
  same(x.slice(i),y.slice(j),'complete unchanged tail');return {role:d.role,hunks,oldBytes:Buffer.byteLength(old),newBytes:Buffer.byteLength(next),diffBytes:Buffer.byteLength(text)};
}
const diffs=json('SOURCE_DIFF_NATIVE.json').diffs;ok(diffs.length===6,'six source/transform diffs');const diffRows=diffs.map(diffCheck);
const initial=json('CHECK_INITIAL_NATIVE.json'),final=json('CHECK_NATIVE.json');native('initial-author-check',initial);native('final-author-check',final);ok(initial.result.exit_code===0&&final.result.exit_code===0,'author checks actual zero');
const initialData=JSON.parse(initial.result.output),finalData=JSON.parse(final.result.output);ok(finalData.checks===33405&&finalData.keys.length===39,'final author exact census');finalData.keys.forEach(k=>checkAuthorKey(k,'final author check'));
const changedAuthorKeys=[];for(let i=0;i<initialData.keys.length;i++){const x=initialData.keys[i],y=finalData.keys[i];ok(x.path===y.path,'same initial/final author key order');if(JSON.stringify(x)!==JSON.stringify(y))changedAuthorKeys.push(x.path);}same(changedAuthorKeys,[P+'PREPARATION.md'],'only disclosed preparation prose changed');
const readbacks=json('READBACK_NATIVE.json');ok(readbacks.reads.length===7,'seven author readbacks');
for(const [i,r] of readbacks.reads.entries()){native('readback/'+i,r);if(r.name==='PREPARATION.md'){const prev=initialData.keys.find(k=>k.path===r.path);ok(sha(r.result.output)===prev.sha256&&Buffer.byteLength(r.result.output)===prev.bytes,'complete old prose read matches old key');const a='JSON data is parsed only by the separate Node documentary checker.\n',b='JSON values are handled as documentary data by JavaScript; neither Python\nnor Bash source is parsed or executed.\n';ok(r.result.output.split(a).length===2,'one exact old prose phrase');raw(r.result.output.replace(a,b),doc('PREPARATION.md'),'exact disclosed prose correction');}else raw(r.result.output,doc(r.name),'whole author final readback '+r.name);}
native('final-preparation-read',readbacks.final_preparation_read);raw(readbacks.final_preparation_read.result.output,doc('PREPARATION.md'),'whole final preparation read');
const checkerReads=json('CHECK_SOURCE_NATIVE.json');native('checker-draft-read',checkerReads.draft_read);native('checker-final-read',checkerReads.final_read);raw(checkerReads.final_read.result.output,doc('CHECK_DOCUMENTS.cjs'),'whole final author checker source read');
const bad='ok(b.files.length===69&&b.module_names.length===62,"finite exact cardinalities");\nok(b.required_module_names.early.every(n=>b.module_names.includes(n)),"early required subset");';
const good='ok(b.files.length===69&&b.module_names.early.length===23&&b.module_names.helper.length===62&&b.module_names.closing.length===62,"finite exact phase cardinalities");\nfor(const phase of ["early","helper","closing"])ok(b.required_module_names[phase].every(n=>b.module_names[phase].includes(n)),"required phase subset "+phase);';
ok(checkerReads.draft_read.result.output.split(bad).length===2,'one unexecuted draft source block');raw(checkerReads.draft_read.result.output.replace(bad,good),doc('CHECK_DOCUMENTS.cjs'),'exact never-executed checker draft correction');
json('HANDOFF_READS_NATIVE.json').reads.forEach((r,i)=>{native('handoff/'+i,r);raw(r.result.output,doc(r.name),'whole handoff/evidence read');});
const closing=json('CLOSING_NATIVE.json');native('closing-source-read',closing.source_read);native('author-closing',closing);raw(closing.source_read.result.output,doc('CLOSE_DOCUMENTS.cjs'),'whole original closing-checker source read');const cd=JSON.parse(closing.result.output);ok(cd.checks===529&&cd.keys.length===47,'author closing census');cd.keys.forEach(k=>checkAuthorKey(k,'author closing'));
const replays=own('AUTHOR_REPLAYS_NATIVE.json').records;ok(replays.length===2,'two fresh documentary replays');for(const [i,r] of replays.entries()){ok(r.result.exit_code===0,'actual replay success');raw(r.result.output,i?closing.result.output:final.result.output,'whole fresh author documentary replay '+r.name);}
const programReads=own('PROGRAM_READS_NATIVE.json').records;ok(programReads.length===5,'five full prospective source chunks');const ranges=[[1,720],[721,1440],[1441,2165],[2166,2505],[2506,2845]];const sourceLines=str('observe.proposed.py.txt').split(/(?<=\n)/);programReads.forEach((r,i)=>{ok(r.result.exit_code===0,'source read success');raw(r.result.output,sourceLines.slice(ranges[i][0]-1,ranges[i][1]).join(''),'exact reviewer source range '+ranges[i].join('-'));});raw(programReads.map(r=>r.result.output).join(''),doc('observe.proposed.py.txt'),'whole concatenated 2845-line prospective source');
const captureRead=own('CONTRACT_READS_NATIVE.json').records.find(r=>r.request.cmd.includes('/capture.proposed.sh.txt'));ok(!!captureRead&&captureRead.result.exit_code===0,'full prospective capture semantic read');raw(captureRead.result.output,doc('capture.proposed.sh.txt'),'whole reviewer prospective capture');
ok(records.length===46,'all original native envelopes');same(records.reduce((x,r)=>(x[r.exit]=(x[r.exit]||0)+1,x),{}),{'0':39,'1':6,'2':1},'complete original exit census');ok(records.every(r=>!r.toolTruncated),'no original native tool truncation marker');
for(const n of OWN)acquire(A+n);
for(const p of [...keyCache.keys()])acquire(p,true);
console.log(JSON.stringify({scope:'INDEPENDENT_EXACT_PROSPECTIVE_DERIVATIVE_DOCUMENTARY_PASS_NOT_OPERATION_OR_RUNTIME',checks,currentPackage:{seal:sealHash,payloads:32,files:33,bytes:physicalBytes},acceptedPredecessorPins:pins,baselineKeys:53,fullKeys:[...keyCache.values()],bindingChanges:leafChanges,consumedFields:consumed,finiteModules:62,finiteFiles:69,collectorSuffixBytes:Buffer.byteLength(suffix),prospectiveObserverBytes:98365,prospectiveCaptureBytes:1949,diffs:diffRows,rawPairs,rawPairCount:rawPairs.length,rawPairedBytes:rawPairs.reduce((s,r)=>s+r.bytes,0),originalNativeRecords:records,originalNativeCount:records.length,originalNativeExits:{zero:39,difference:6,missingDocument:1},freshAuthorReplayCount:2,reviewedProgramsExecutedOrParsed:false,futureOperationalPathsUsedAsOperands:false,scientificRuns:0}));
