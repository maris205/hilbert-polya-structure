'use strict';
// Root documentary receiver only: source, frontier and archived requests are data.
// New-only delta: five already-keyed workspace documentary records absent from the
// non-lineage selection are explicit; their private path strings are not followed.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const B='docs/papers211_215_sequence/qa/',R=B+'p212_keyed_stdin_source_root01/',A=B+'p212_keyed_stdin_nonlineage_audit01/';
let checks=0;const ok=(v,m)=>{checks++;assert(v,m);},eq=(a,b,m)=>{checks++;assert.deepEqual(a,b,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const own=['CHECK_RECEPTION.cjs','CHECK_RECEPTION_delta01.cjs','FAILED_CHECK_NATIVE.json','EXTRA_SELECTION_NATIVE.json','ROOT_CONTRACT_READS_NATIVE.json','ROOT_DIFF_FRONTIER_READS_NATIVE.json','ROOT_LIMITED_AUDIT_READS_NATIVE.json','ROOT_LIMITED_DOCUMENTARY_REPLAY_NATIVE.json','ROOT_NONLINEAGE_READS_NATIVE.json','ROOT_NONLINEAGE_REPLAYS_NATIVE.json','ROOT_PROGRAM_READS_NATIVE.json','ROOT_REPLAY_COMPARISON_NATIVE.json'];
const packets=[
 ['p212_keyed_stdin_source_delta01',55,'f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8'],
 ['p212_keyed_stdin_source_audit01',21,'2bf279e75d81ad1383bb8eab451b7252bd2d4f0d395a74ccf92d01c1e6970aa6'],
 ['p212_keyed_stdin_linecount_erratum01',7,'7876c67cf7a4f436e746bf7ac282868dce74aa7c5ef31063725af815371c4007'],
 ['p212_keyed_stdin_linecount_audit01',7,'405df307b2cba91ecb389c9942cacce85929aab7d67a116288f2b318a2c0996a'],
 ['p212_keyed_stdin_nonlineage_audit01',24,'ff622be9502a7bd931820cf1c22b5e858bc09243ef3e0488fe7d65cfbea71887']
];
const allowed=new Set(own.map(n=>R+n));for(const[p]of packets)allowed.add(B+p+'/SHA256SUMS');
for(const n of ['p212_preprobe_native_mask_analysis01/INPUT_SHA256SUMS','p212_preprobe_observation_root01/ACTUAL_OBSERVER_NATIVE.json','p212_preprobe_observation_root01/GRANT.md','p212_preprobe_observation_root01/INITIAL_RAW_INTAKE_NATIVE.json','p212_preprobe_observation_root01/REQUEST.json'])allowed.add(B+n);
const keys=new Map(),bodies=new Map();
const meta=s=>Object.fromEntries(fields.map(f=>{ok(typeof s[f]==='bigint','integer field');return[f,String(s[f])];}));
function read(p){
 ok(allowed.has(p),'explicit selected document '+p);
 const s=fs.lstatSync(p,{bigint:true});ok(s.isFile()&&!s.isSymbolicLink(),'physical document');
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,k;
 try{const t=fs.fstatSync(fd,{bigint:true});eq(meta(t),meta(s),'opening path/fd');ok(t.size<=3000000n,'bounded documentary bytes');k=meta(t);b=fs.readFileSync(fd);eq(meta(fs.fstatSync(fd,{bigint:true})),k,'same-fd closing');}finally{fs.closeSync(fd);}
 eq(meta(fs.lstatSync(p,{bigint:true})),k,'closing path');eq(String(b.length),k.size,'whole bytes');
 const key={path:p,bytes:b.length,sha256:sha(b),metadata:k};if(keys.has(p))eq(key,keys.get(p),'unchanged reread');keys.set(p,key);bodies.set(p,b);return b;
}
function rows(b){const s=b.toString('utf8');eq(Buffer.from(s),b,'manifest UTF8');ok(s.endsWith('\n')&&!s.endsWith('\n\n'),'single final LF');const a=s.slice(0,-1).split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(l);ok(m&&!m[2].startsWith('/')&&!m[2].split('/').includes('..'),'exact confined manifest');return{sha256:m[1],path:m[2]};});eq(new Set(a.map(r=>r.path)).size,a.length,'unique rows');return a;}
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>{ok(!e.isSymbolicLink(),'packet no symlink');return e.isDirectory()?walk(d+'/'+e.name):[d+'/'+e.name];}).sort();}
const inventories=[];
for(const[p,n,h]of packets){const d=B+p+'/',m=read(d+'SHA256SUMS');eq(sha(m),h,'fixed packet seal');const a=rows(m);eq(a.length,n,'payload cardinality');for(const r of a){ok(r.path!=='SHA256SUMS','nonself');allowed.add(d+r.path);eq(sha(read(d+r.path)),r.sha256,'whole payload digest');}eq(walk(d.slice(0,-1)),a.map(r=>d+r.path).concat(d+'SHA256SUMS').sort(),'exact physical membership');inventories.push({directory:d,payloads:n,files:n+1,sha256:h});}
const j=p=>JSON.parse((bodies.get(p)||read(p)).toString('utf8'));
const input=j(A+'INPUTS_BEFORE.json').inputs;eq(input.length,130,'nonlineage finite inputs');
for(const k of input){ok(!k.path.includes('empty.stdin')&&(k.path.startsWith(B)||['.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md'].includes(k.path)),'source-only pins');allowed.add(k.path);const b=read(k.path);eq(b.length,k.bytes);eq(sha(b),k.sha256);eq(b.reduce((n,c)=>n+(c===10),0),k.lf_lines);}
eq(j(A+'INPUTS_AFTER.json').inputs,input,'all 130 before-after keys');
const sourcePins=rows(bodies.get(B+'p212_keyed_stdin_source_delta01/SOURCE_INPUTS.sha256'));eq(sourcePins.length,29);for(const k of sourcePins)eq(sha(read(k.path)),k.sha256,'29 author input pins');
const legacy=j(B+'p212_keyed_stdin_source_audit01/DOCUMENTARY_RESULT.json');eq(legacy.input_keys.length,91);eq(legacy.checks,3816);
function oldKeys(a){for(const k of a){const b=read(k.path),now=keys.get(k.path);eq(b.length,k.byte_count,'old whole byte length');eq(sha(b),k.sha256,'old full content');for(const f of fields)eq(now.metadata[f],String(k[f]),'old full field '+f);}}
oldKeys(legacy.input_keys);
const limitedDelta=j(B+'p212_keyed_stdin_linecount_audit01/CHECK_NATIVE.json').record;
const limitedClose=j(B+'p212_keyed_stdin_linecount_audit01/CLOSING_NATIVE.json').record;
for(const r of [limitedDelta,limitedClose]){eq(r.result.exit_code,0);const x=JSON.parse(r.result.output);eq(x.checks,1473);eq(x.input_keys.length,121);oldKeys(x.input_keys);}
eq(Buffer.from(limitedDelta.result.output),Buffer.from(limitedClose.result.output),'entire same limited-delta documentary stdout');
const deltaPins=rows(bodies.get(B+'p212_keyed_stdin_linecount_audit01/INPUTS.sha256'));eq(deltaPins.length,121);for(const p of deltaPins)eq(sha(read(p.path)),p.sha256,'complete linecount input pin');
for(const n of own)read(R+n);
const raw=[];
function pair(actual,expected,label){eq(actual,expected,label);raw.push({label,bytes:actual.length,sha256:sha(actual)});}
const replays=j(R+'ROOT_NONLINEAGE_REPLAYS_NATIVE.json').replays;eq(replays.length,4);
for(const r of replays){eq(r.return.exit_code,0);ok(typeof r.request.cmd==='string'&&typeof r.return.chunk_id==='string','actual replay record');}
for(const[k,n]of [['p212_nonlineage_root_delta','DELTA_RESULT.json'],['p212_nonlineage_root_receipts','RECEIPT_RESULT.json'],['p212_nonlineage_root_inputs','INPUTS_AFTER.json']]){const r=replays.find(x=>x.key===k);ok(r,'actual selected replay');pair(Buffer.from(r.return.output),bodies.get(A+n),'root actual '+k);}
const final=JSON.parse(replays.find(r=>r.key==='p212_nonlineage_root_seal').return.output);eq(final.checks,236);eq(final.payloads,24);eq(final.manifest_sha256,packets[4][2]);
const limitedReplay=j(R+'ROOT_LIMITED_DOCUMENTARY_REPLAY_NATIVE.json');eq(limitedReplay.return.exit_code,0);pair(Buffer.from(limitedReplay.return.output),bodies.get(B+'p212_keyed_stdin_source_audit01/DOCUMENTARY_RESULT.json'),'prior root actual limited replay, not independent source acceptance');
const renderRows=[];
function rendered(cmd){
 const m=/^sed (-s )?-n '(\d+),(\d+)p' (.+)$/.exec(cmd);ok(m,'exact archived read syntax');const ns=m[4].split(' ');for(const p of ns)ok(allowed.has(p),'source read selection');
 const all=ns.map(p=>{const b=read(p),t=b.toString('utf8');eq(Buffer.from(t),b,'source UTF8');return t.match(/[^\n]*\n|[^\n]+$/g)||[];});
 const a=Number(m[2])-1,z=Number(m[3]);return Buffer.from(m[1]?all.map(v=>v.slice(a,z).join('')).join(''):all.flat().slice(a,z).join(''));
}
for(const n of ['ROOT_PROGRAM_READS_NATIVE.json','ROOT_CONTRACT_READS_NATIVE.json','ROOT_LIMITED_AUDIT_READS_NATIVE.json','ROOT_DIFF_FRONTIER_READS_NATIVE.json']){
 const x=j(R+n),rs=Array.isArray(x)?x:x.records;for(const r of rs){eq(r.return.exit_code,0);const actual=Buffer.from(r.return.output);pair(actual,rendered(r.request.cmd),'root source '+r.return.chunk_id);renderRows.push({file:n,chunk:r.return.chunk_id,bytes:actual.length});}}
for(const r of j(R+'ROOT_NONLINEAGE_READS_NATIVE.json').reads){eq(r.return.exit_code,0);let b=read(r.path);if(r.path.endsWith('.cjs'))b=Buffer.concat([Buffer.from(String(b.reduce((n,c)=>n+(c===10),0))+' '+r.path+'\n'),b]);pair(Buffer.from(r.return.output),b,'root independent audit full read '+r.path);}
const f=j(A+'FINDINGS.json');eq(f.current_source_census,{Blocker:0,Major:0,Minor:0});eq(f.limited_prior_review_is_independent_full_acceptance,false);eq(f.received_finding.status,'CLOSED_EXACT_ORIGINAL_PLUS_ERRATUM_ONLY');
const before=[...keys.values()];for(const k of before)read(k.path);
process.stdout.write(JSON.stringify({scope:'ROOT_DOCUMENTARY_ORIGINAL_RECEPTION_ONLY',checks,inventory:inventories,complete_keys:keys.size,keys:[...keys.values()],nonlineage_input_pins:130,author_source_pins:29,old_full_keys:91,limited_delta_full_keys:121,raw_comparisons:raw,root_source_renderings:renderRows,independent_source_verdict:f.verdict,no_reviewed_program_execution:true,no_host_or_input_observation:true},null,2)+'\n');
