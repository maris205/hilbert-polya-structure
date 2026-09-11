'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',BASE='docs/papers211_215_sequence/qa/p212_dependency_query_outer_source_audit01',AUTHOR='docs/papers211_215_sequence/qa/p212_dependency_query_outer_preparation01',CONSULT=BASE+'/product_envelope_consult01';
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const need=(v,m)=>{if(!v)throw Error(m);},hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const local=r=>{need(typeof r==='string'&&!r.startsWith('/')&&!r.split('/').some(s=>!s||s==='.'||s==='..'),'literal workspace relative');return path.join(ROOT,r);};
const read=r=>fs.readFileSync(local(r)),json=r=>JSON.parse(read(r)),pin=r=>{const b=read(r);return {path:r,bytes:b.length,sha256:hash(b)};};
function listed(name,prefix,expected){
 const raw=read(name);if(expected)need(hash(raw)===expected,'exact seal '+name);need(raw.at(-1)===10,'whole manifest LF');
 const rows=raw.toString().trimEnd().split('\n').map(line=>{const m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(m,'manifest syntax');const r=(prefix?prefix+'/':'')+m[2],p=pin(r);need(p.sha256===m[1],'whole manifest member '+r);return p;});
 need(new Set(rows.map(x=>x.path)).size===rows.length,'unique manifest entries');return {file:pin(name),rows};
}
const a=listed(AUTHOR+'/SHA256SUMS',AUTHOR,'2c886f9fb07053c5ca6dcf46b5eba397a9e92e2d4949a9ca0598bb05b9779138');
need(a.rows.length===23,'frozen author23');
const review=listed(AUTHOR+'/REVIEW_INPUTS.sha256','', 'b3e9164a37e641db38a6a4e77cd03f66a90e205b19be5cdd7bfe59247a1166ef');
const source=listed(AUTHOR+'/SOURCE_INPUTS.sha256','', '91e3854856d16a2cbb8983c80859af3e1f4ba484ca00c8ec20d152ad7fd188be');
need(review.rows.length===14&&source.rows.length===46,'exact review/source lists');
const c=listed(CONSULT+'/SHA256SUMS',CONSULT,'c6fee879a0ccb99e67a5e26b739cd8bc160cf9822b4eb92e08c4c8b24dd4677e');
need(c.rows.length===4,'consult4payloads');
const cp=listed(CONSULT+'/INPUT_PINS.sha256','');need(cp.rows.length===8,'consult8wholepins');
need(JSON.stringify(fs.readdirSync(local(CONSULT)).sort())===JSON.stringify(['SHA256SUMS',...c.rows.map(x=>x.path.slice(CONSULT.length+1))].sort()),'consult exact nonself membership');
const cr=json(CONSULT+'/NATIVE_READS.json').records;need(cr.length===13&&cr.every(r=>r.result.exit_code===0),'all actual consult13successful reads');
const comparedReads=[];
for(const r of cr){const m=/^sed -n '[0-9]+,[0-9]+p' '([^']+)'$/.exec(r.cmd);if(m){need(Buffer.from(r.result.output).equals(read(m[1])),'consult actual complete read '+m[1]);comparedReads.push({path:m[1],native_chunk:r.result.chunk_id,bytes:Buffer.byteLength(r.result.output)});}}
need(comparedReads.length===7,'seven complete consult source/collateral native outputs');
const b=json(BASE+'/INPUTS_BEFORE.json');need(b.inputs.length===72,'fixed own72');
const stable=b.inputs.map(x=>{const p=local(x.path),ls=fs.lstatSync(p,{bigint:true}),s=fs.statSync(p,{bigint:true}),z=pin(x.path);need(z.sha256===x.sha256&&z.bytes===x.bytes&&fs.realpathSync(p)===x.resolved,'current whole owninput '+x.path);for(const [field,ob]of[['lstat',ls],['stat',s]])for(const k of F)if(k!=='atimeNs')need(typeof ob[k]==='bigint'&&String(ob[k])===x[field][k],'stable own14minusatime '+x.path+' '+field+' '+k);return z;});
const findings=json(BASE+'/FINDINGS.json'),cf=json(CONSULT+'/FINDINGS.json');
need(findings.census.major_open===0&&findings.census.minor_open===1&&findings.census.critical_open===0,'actual main finding census');
need(findings.findings.length===1&&findings.findings[0].id==='PCE-D1'&&findings.findings[0].status==='OPEN_DOCUMENTARY_CORRECTION_REQUIRED','main actual open minor preserved');
need(cf.findings.length===1&&cf.findings[0].id==='PCE-D1'&&cf.findings[0].status==='OPEN','consult same actual open minor');
need(findings.authority.unqualified_source_acceptance===false&&findings.authority.root_reception===false&&findings.authority.source_execution===false,'no source/operational overclaim');
const fail=json(BASE+'/INTEGRITY_NATIVE.json'),pass=json(BASE+'/INTEGRITY02_NATIVE.json');
need(fail.result.exit_code===1&&pass.result.exit_code===0,'actual failed helper and corrected success preserved');
const parsed=JSON.parse(pass.result.output);need(parsed.input_count===72&&parsed.complete_core_native_reads===13,'corrected actual helper evidence');
const crSelf=json(BASE+'/CONSULTATION_READS_NATIVE.json');need(crSelf.some(r=>r.result.exit_code===2&&r.request.cmd.includes('/INPUTS.sha256')),'actual wrong consulted input-name read preserved');
need(json(BASE+'/CONSULTATION_INPUT_READ_NATIVE.json').result.exit_code===0,'correct named input read preserved');
process.stdout.write(JSON.stringify({schema:'p212-outer-audit-close-documentary-v1',status:'DOCUMENTARY_CLOSURE_PASS_ONE_MINOR_STILL_OPEN',author:{seal:a.file,payloads:a.rows.length},review_targets:review.rows.length,source_inputs:source.rows.length,consult:{seal:c.file,payloads:c.rows.length,total_files:5,total_bytes:c.file.bytes+c.rows.reduce((n,r)=>n+r.bytes,0),input_pins:cp.rows.length,native_records:cr.length,whole_reads:comparedReads},current_independent_stable_input_count:stable.length,stable_inputs:stable,main_findings:{critical_open:0,major_open:0,minor_open:1,id:'PCE-D1'},failed_documentary_helper_preserved:true,corrected_helper_native_exit:0,submitted_source_executions:0,AST_syntax_import_tests:0,runtime_probes:0,host_dependency_reads:0,manuscript_reviews:0,outer_runtime_or_product_acceptance:false},null,2)+'\n');
