'use strict';
// Read-only documentary reception. Does not import or evaluate submitted code.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA='docs/papers211_215_sequence/qa/';
const A=QA+'p212_trusted_product_source_delta01',B=QA+'p212_trusted_product_source_audit01',D=QA+'p212_trusted_product_source_root01';
let checks=0;const cache=new Map(),keys=new Map(),nativeMatches=[];
function need(x,m){checks++;if(!x)throw Error(m);}
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function read(p){need(!path.isAbsolute(p)&&!p.split('/').includes('..'),'workspace literal');const a=fs.lstatSync(path.join(ROOT,p),{bigint:true});need(a.isFile()&&!a.isSymbolicLink(),'regular '+p);const b=fs.readFileSync(path.join(ROOT,p));const z=fs.lstatSync(path.join(ROOT,p),{bigint:true});need(JSON.stringify(meta(a))===JSON.stringify(meta(z))&&BigInt(b.length)===a.size,'stable entire '+p);const k={path:p,bytes:b.length,sha256:hash(b),metadata:meta(a)};if(keys.has(p))need(JSON.stringify(k)===JSON.stringify(keys.get(p)),'unchanged repeat '+p);else keys.set(p,k);cache.set(p,b);return b;}
const json=p=>JSON.parse(read(p));
function lines(b){return b.toString().match(/[^\n]*\n|[^\n]+$/g)||[];}
function roster(dir){const all=[];for(const e of fs.readdirSync(path.join(ROOT,dir),{withFileTypes:true})){if(e.isDirectory())all.push(...roster(dir+'/'+e.name));else{need(e.isFile(),'no aliased package entry');all.push(dir+'/'+e.name);}}return all.sort();}
function pinlist(p,base,count){const rows=read(p).toString().trimEnd().split('\n');need(rows.length===count,'pin count '+p);const paths=[];for(const row of rows){const m=/^([0-9a-f]{64})  (.+)$/.exec(row);need(!!m,'pin grammar');const f=base?base+'/'+m[2]:m[2];need(!paths.includes(f),'pin uniqueness');paths.push(f);need(hash(read(f))===m[1],'whole pin '+f);}return paths;}
function seal(dir,n,expected){need(hash(read(dir+'/SHA256SUMS'))===expected,'selected exact seal');const v=pinlist(dir+'/SHA256SUMS',dir,n);need(JSON.stringify(roster(dir))===JSON.stringify([...v,dir+'/SHA256SUMS'].sort()),'complete nonself roster');return v;}
const ap=seal(A,33,'3854f2d26bd3a0fed59dba5a4a59454a489219db4701a2a1f32656d657ef0cca');
const bp=seal(B,18,'66035a7dbb4216c70f8898b479f42fc804bf6f72342633d71fce12a40a6decde');
need(ap.reduce((n,p)=>n+keys.get(p).bytes,0)+keys.get(A+'/SHA256SUMS').bytes===783925,'whole author package bytes');
need(bp.reduce((n,p)=>n+keys.get(p).bytes,0)+keys.get(B+'/SHA256SUMS').bytes===937283,'whole audit package bytes');
const sourcePins=pinlist(A+'/SOURCE_INPUTS.sha256','',48);
pinlist(B+'/TARGET_PINS_BEFORE.sha256','',34);pinlist(B+'/TARGET_PINS_AFTER.sha256','',34);
need(read(B+'/TARGET_PINS_BEFORE.sha256').equals(read(B+'/TARGET_PINS_AFTER.sha256')),'entire target pin files raw equal');
pinlist(B+'/BACKGROUND_PINS.sha256','',29);pinlist(B+'/BACKGROUND_RELOCATION_PINS.sha256','',2);
const roles=json(A+'/INPUT_ROLES.json').inputs;need(roles.length===48,'48 roles');
for(const k of roles){need(sourcePins.includes(k.path),'role in input ledger');const v=read(k.path);need(v.length===k.bytes&&hash(v)===k.sha256,'role entire size/hash');}
const typed=json(A+'/TYPED_INVALIDATION_MAP.json');need(typed.changed_derivatives.length===10&&typed.dependencies.length===11,'ten derivatives/eleven invalidations');
const old=new Map(),current=new Map();
for(const r of typed.changed_derivatives){const x=read(r.baseline.path),y=read(A+'/'+r.name);need(x.length===r.baseline.bytes&&hash(x)===r.baseline.sha256,'baseline '+r.name);need(y.length===r.bytes&&hash(y)===r.sha256&&lines(y).length===r.lines,'derivative '+r.name);old.set(r.name,x.toString());current.set(r.name,y.toString());}
need([...typed.changed_derivatives].reduce((n,x)=>n+x.bytes,0)===109741,'derivative bytes');
need(typed.changed_derivatives.filter(x=>/\.(js|py)$/.test(x.name)).reduce((n,x)=>n+x.bytes,0)===67104,'source program bytes');
const diffSets=[json(A+'/DIFF_NATIVE.json').records,json(B+'/INDEPENDENT_DIFF_NATIVE.json').records,json(D+'/ROOT_DIFF_NATIVE.json').records];let diffBytes=0;
for(const list of diffSets){need(list.length===10,'ten full actual diffs');for(const r of list){const raw=read(A+'/diffs/'+r.name+'.diff');need(r.result.exit_code===1&&raw.equals(Buffer.from(r.result.output)),'actual complete diff '+r.name);nativeMatches.push({scope:'RAW_COMPLETE_DIFF',chunk_id:r.result.chunk_id,bytes:raw.length,sha256:hash(raw)});}}
for(const r of typed.changed_derivatives)diffBytes+=read(A+'/diffs/'+r.name+'.diff').length;
const comparison=json(B+'/TEXT_COMPARISON.json');
function slice(s,a,b){const i=s.indexOf(a);need(i>=0&&s.indexOf(a,i+a.length)===-1,'unique start');const j=s.indexOf(b,i+a.length);need(j>i,'end after start');return s.slice(i,j);}
for(const p of comparison.protected_slices){const x=slice(old.get(p.file),p.start_marker,p.end_marker_exclusive),y=slice(current.get(p.file),p.start_marker,p.end_marker_exclusive);need(x===y&&x.length===p.old_characters&&y.length===p.new_characters,'protected block '+p.scope);}
for(const p of comparison.import_lines){const select=s=>s.split('\n').filter(x=>/^(import |from .* import |const (fs|cp)=require\()/.test(x));const x=select(old.get(p.file)),y=select(current.get(p.file));need(JSON.stringify(x)===JSON.stringify(y)&&JSON.stringify(y)===JSON.stringify(p.lines),'whole literal import surface '+p.file);}
const row=s=>s.split('\n').filter(x=>x.startsWith('| Actual product capture |'));need(JSON.stringify(row(old.get('READ_ENTRY_COVERAGE.md')))===JSON.stringify(row(current.get('READ_ENTRY_COVERAGE.md'))),'entire corrected catch row');
const knownNative=[];
function collect(x,label){if(!x||typeof x!=='object')return;if(x.request&&x.result&&typeof x.result.output==='string')knownNative.push({label,...x});for(const [k,v]of Object.entries(x)){if(k==='request'||k==='result')continue;if(Array.isArray(v))v.forEach((t,i)=>collect(t,label+'.'+k+'['+i+']'));else if(v&&typeof v==='object')collect(v,label+'.'+k);}}
for(const p of [A+'/SOURCE_READS_NATIVE.json',A+'/DERIVATIVE_READS_NATIVE.json',B+'/READS_NATIVE.json',B+'/BACKGROUND_READS_NATIVE.json',B+'/BACKGROUND_RELOCATION_NATIVE.json',B+'/FINAL_DOCUMENT_READS_NATIVE.json',D+'/ROOT_READS_NATIVE.json'])collect(json(p),p);
let sourceReadMatches=0;const skipped=[];
for(const r of knownNative){let cmd=r.request.cmd;if(typeof cmd!=='string'||r.result.exit_code!==0||r.result.output.startsWith('Warning: truncated output')){skipped.push({label:r.label,chunk:r.result.chunk_id,reason:'nonzero/clipped/not command'});continue;}
let m=/^sed -n '([^']+)' (.+)$/.exec(cmd),parts,addresses;
if(m){parts=m[2].split(/\s+/).map(p=>p.replace(/^'|'$/g,''));addresses=m[1].split(';').map(s=>/^(\d+),(\d+)p$/.exec(s));if(addresses.some(x=>!x)){skipped.push({label:r.label,chunk:r.result.chunk_id,reason:'other sed grammar'});continue;}}
else {m=/^cat (.+)$/.exec(cmd);if(!m){skipped.push({label:r.label,chunk:r.result.chunk_id,reason:'not literal body read'});continue;}parts=m[1].split(/\s+/).map(p=>p.replace(/^'|'$/g,''));}
if(parts.some(p=>!p.startsWith(QA)||!fs.existsSync(path.join(ROOT,p)))){skipped.push({label:r.label,chunk:r.result.chunk_id,reason:'outside finite QA body read scope'});continue;}
const text=Buffer.concat(parts.map(read)).toString();let actual=text;
if(addresses){actual='';lines(Buffer.from(text)).forEach((line,i)=>addresses.forEach(a=>{if(i+1>=+a[1]&&i+1<=+a[2])actual+=line;}));}
need(actual===r.result.output,'complete archived source body '+r.label+' '+r.result.chunk_id);sourceReadMatches++;nativeMatches.push({scope:'COMPLETE_NATIVE_BODY',label:r.label,chunk_id:r.result.chunk_id,bytes:Buffer.byteLength(actual),sha256:hash(Buffer.from(actual))});
}
const census=json(B+'/FINDINGS.json');need(census.census.blocking===0&&census.census.major===0&&census.census.minor===0&&census.census.open_actual_source_findings.length===0,'actual source census only');need(census.old_strict_product_startup==='UNSATISFIED_NOT_CLOSED_BY_THIS_AUDIT','strict claim not closed');
const iface=json(A+'/INTERFACE.disabled.json');need(iface.enabled===false&&iface.provenance.product_startup_attested===false,'disabled source-only interface');
read(D+'/receive.cjs');const paths=[...keys.keys()];for(const p of paths)read(p);
process.stdout.write(JSON.stringify({schema:'p212-trusted-product-root-documentary-reception-v1',status:'WHOLE_SOURCE_AND_AUDIT_EVIDENCE_PASS_NOT_RUNTIME',checks,whole_documentary_keys:keys.size,author_payloads:33,audit_payloads:18,source_input_pins:48,audit_before_after_target_pins:34,audit_background_pins:31,ten_derivative_bytes:109741,five_source_bytes:67104,complete_diff_sets:3,complete_diffs:30,one_diff_set_bytes:diffBytes,protected_blocks:comparison.protected_slices.length,whole_import_surfaces:comparison.import_lines.length,complete_native_body_matches:sourceReadMatches,indexed_native_read_records:knownNative.length,read_limits:skipped,old_strict_startup:'UNSATISFIED',p212_probe_query_build_runs:0,nativeMatches,keys:[...keys.values()]},null,2)+'\n');
