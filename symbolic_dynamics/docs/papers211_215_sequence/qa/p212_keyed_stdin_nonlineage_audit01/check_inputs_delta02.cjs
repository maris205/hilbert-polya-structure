'use strict';
// Auditor-owned documentary reader only. Reviewed source bytes are never evaluated/imported/parsed as code.
const fs=require('fs'), path=require('path'), crypto=require('crypto');
const base='docs/papers211_215_sequence/qa/';
const own=base+'p212_keyed_stdin_nonlineage_audit01/';
const packets=[
 ['p212_keyed_stdin_source_delta01','f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8',55],
 ['p212_keyed_stdin_source_audit01','2bf279e75d81ad1383bb8eab451b7252bd2d4f0d395a74ccf92d01c1e6970aa6',21],
 ['p212_keyed_stdin_linecount_erratum01','7876c67cf7a4f436e746bf7ac282868dce74aa7c5ef31063725af815371c4007',7],
 ['p212_keyed_stdin_linecount_audit01','405df307b2cba91ecb389c9942cacce85929aab7d67a116288f2b318a2c0996a',7]
];
const permitted=new Set(packets.map(x=>x[0]).concat([
 'p212_execution_scope_source_amendment01','p212_preprobe_bootstrap_preparation01',
 'p212_preprobe_bootstrap_read_order_delta01','p212_preprobe_native_mask_analysis01',
 'p212_preprobe_native_mask_root01','p212_trusted_product_boundary_root01',
 'p212_trusted_product_source_delta01','p212_preprobe_bootstrap_source_root01',
 'p212_trusted_product_source_root01','p212_dependency_query_outer_source_root01',
 'p212_execution_scope_amendment_root01','p212_dependency_source_root01'
]));
const selected=new Set(['.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md']);
let checks=0;
function ok(x,msg){checks++;if(!x)throw Error(msg);}
function permittedPath(p){
 ok(typeof p==='string'&&!p.includes('..')&&!p.includes('\\')&&!p.startsWith('/'),'safe relative path '+p);
 if(selected.has(p)&&!p.startsWith(base))return;
 ok(p.startsWith(base)&&permitted.has(p.slice(base.length).split('/')[0]),'documentary allowlist '+p);
 ok(!p.includes('empty.stdin'),'no proposed target '+p);
}
function read(p){permittedPath(p);selected.add(p);return fs.readFileSync(p);}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex');}
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>{ok(!e.isSymbolicLink(),'no packet symlink');return e.isDirectory()?walk(dir+'/'+e.name):[dir+'/'+e.name];}).sort();}
function lines(b){return [...b].filter(c=>c===10).length;}
function manifest(raw,prefix,layout){
 const text=raw.toString('utf8');ok(Buffer.from(text).equals(raw),'utf8 manifest');
 ok(text.endsWith('\n')&&!text.endsWith('\n\n'),'one terminal LF '+prefix);
 const records=text.slice(0,-1).split('\n').map(line=>{
   const m=line.match(layout==='dot'?/^([a-f0-9]{64})  \.\/([^\r\n]+)$/:/^([a-f0-9]{64})  ([^\r\n]+)$/);
   ok(m,'exact manifest layout '+line);
   ok(m[2]!=='SHA256SUMS'&&!m[2].startsWith('/')&&!m[2].split('/').includes('..'),'nonself confined path');
   return {path:prefix+m[2],sha256:m[1]};
 });
 ok(new Set(records.map(r=>r.path)).size===records.length,'manifest unique');
 return records;
}
const sealResults=[];
for(const [dir,sealdigest,count]of packets){
 const prefix=base+dir+'/';const seal=read(prefix+'SHA256SUMS');
 ok(sha(seal)===sealdigest,'fixed seal '+dir);
 // All four named originals were inspected: their exact frozen syntax is bare-relative.
 const layout='bare';
 const records=manifest(seal,prefix,layout);
 ok(records.length===count,'payload cardinality '+dir);
 const physical=walk(prefix.slice(0,-1));
 ok(JSON.stringify(physical)===JSON.stringify(records.map(r=>r.path).concat(prefix+'SHA256SUMS').sort()),'complete physical membership '+dir);
 for(const r of records)ok(sha(read(r.path))===r.sha256,'payload '+r.path);
 sealResults.push({path:prefix+'SHA256SUMS',sha256:sha(seal),payloads:records.length,files:physical.length,layout});
}
const sourcePins=read(base+'p212_keyed_stdin_source_delta01/SOURCE_INPUTS.sha256').toString('utf8');
ok(sourcePins.endsWith('\n')&&!sourcePins.endsWith('\n\n'),'source pins terminal LF');
const pins=sourcePins.slice(0,-1).split('\n').map(line=>{const m=line.match(/^([a-f0-9]{64})  (docs\/[^\r\n]+)$/);ok(m,'source pin syntax');return {path:m[2],sha256:m[1]};});
ok(pins.length===29,'29 source pins');
for(const p of pins)ok(sha(read(p.path))===p.sha256,'source input '+p.path);
for(const name of [
 'p212_preprobe_bootstrap_source_root01/RECEPTION.md',
 'p212_trusted_product_source_root01/RECEPTION.md',
 'p212_dependency_query_outer_source_root01/RECEPTION.md',
 'p212_execution_scope_amendment_root01/RECEPTION.md',
 'p212_dependency_source_root01/RECEPTION.md'
]) read(base+name);
const inputs=[...selected].sort().map(p=>{const b=read(p);return{path:p,bytes:b.length,lf_lines:lines(b),sha256:sha(b)};});
if(process.argv[2]==='closing'){
 const before=JSON.parse(fs.readFileSync(own+'INPUTS_BEFORE.json','utf8'));
 ok(JSON.stringify(inputs)===JSON.stringify(before.inputs),'all before-after whole byte keys unchanged');
}
console.log(JSON.stringify({kind:'documentary-bytes-not-runtime-key',mode:process.argv[2]||'initial',checks,sealResults,inputs},null,2));

