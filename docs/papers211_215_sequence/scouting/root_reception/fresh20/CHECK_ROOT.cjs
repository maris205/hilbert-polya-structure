'use strict';
// Root's fixed documentary receiver. No author scientific code, host observations,
// embedded command execution, network, discovery, or data/model changes.
const fs=require('node:fs');
const make=require('../../../qa/p213_initial_science_enabled_root01/READ_FIXED.cjs');
const R='docs/papers211_215_sequence/scouting/root_reception/fresh20/';
const spec=JSON.parse(fs.readFileSync(R+'INPUT_SPEC.json','utf8'));
const own=['INPUT_SPEC.json','ROOT_READS_NATIVE.json','ROOT_AUDIT_READS_NATIVE.json','ROOT_WEB_RETURNS.json','ROOT_REPLAY_NATIVE.json','CREATION_NATIVE.json','CHECK_ROOT.cjs'];
const I=spec.independentBase;
const allowed=new Set([...spec.external.map(x=>x.path),...spec.independentNames.map(n=>I+n),...own.map(n=>R+n),spec.readerPath]);
const r=make(allowed),read=p=>r.read(p),json=p=>JSON.parse(read(p).toString('utf8'));
const pin=(p,b)=>({path:p,bytes:b.length,sha256:r.sha(b)});
for(const p of allowed)read(p);
r.need(r.sha(read(spec.readerPath))===spec.readerSha,'REUSED_READER_ENTIRE_CURRENT_PIN');
r.need(r.equal(json(R+'INPUT_SPEC.json'),spec),'BOOTSTRAP_SPEC_FULL_RECEIVED');
for(const p of spec.external)r.need(r.equal(pin(p.path,read(p.path)),p),'COMPLETE_FIXED_SOURCE_PIN '+p.path);
const sourceBase='docs/papers211_215_sequence/scouting/finite_residual_fresh20/';
const sourceNames=spec.external.slice(0,9).map(x=>x.path.slice(sourceBase.length));
const rawPairs=[];
function pair(label,a,b){r.need(a.equals(b),'FULL_RAW_PAIR '+label);rawPairs.push({label,bytes:a.length,sha256:r.sha(a),byte_equal:true});}
function packageCheck(base,names,manifest,seal){
  r.need(r.equal(fs.readdirSync(base).sort(),[...names].sort()),'EXACT_CURRENT_PACKAGE_INVENTORY '+base);
  const payload=names.filter(n=>n!==manifest),data=read(base+manifest);
  r.need(r.sha(data)===seal,'CURRENT_MANIFEST_PIN '+base);
  const lines=data.toString('utf8').trimEnd().split('\n');
  const seen=new Set();
  for(const line of lines){const m=line.match(/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/);r.need(!!m,'STRICT_MANIFEST_ROW');r.need(payload.includes(m[2])&&!seen.has(m[2]),'EXACT_NONSELF_PAYLOAD');seen.add(m[2]);r.need(r.sha(read(base+m[2]))===m[1],'COMPLETE_PAYLOAD_CONTENT');}
  r.need(seen.size===payload.length,'ALL_NONSELF_PAYLOADS_RECEIVED');
  return {base,payloads:payload.length,files:names.length,bytes:names.reduce((n,x)=>n+read(base+x).length,0),manifest:pin(base+manifest,data)};
}
const packages=[packageCheck(sourceBase,sourceNames,'SHA256SUMS',spec.external[8].sha256),packageCheck(I,spec.independentNames,'MANIFEST.sha256',spec.independentSeal)];
r.need(packages[0].bytes===530030&&packages[1].bytes===682382,'EXACT_PHYSICAL_BYTE_CENSUSES');
const n=json(I+'ARTIFACT_CHECK_NATIVE.json'),a=json(I+'ARTIFACT_CHECK.json');
r.need(n.actual_return.exit_code===0&&n.actual_return.chunk_id==='3f6331','INDEPENDENT_ACTUAL_ARTIFACT_NATIVE');
r.need(n.request.cmd==='node '+I+'check_artifacts.mjs','EXACT_DOCUMENTARY_COMMAND');
pair('independent actual full artifact stdout',Buffer.from(n.actual_return.output),read(I+'ARTIFACT_CHECK.json'));
const cn=json(I+'CLOSING_NATIVE.json');
r.need(cn.actual_return.exit_code===0&&cn.request.cmd==='node '+I+'close_check.mjs','INDEPENDENT_ACTUAL_BASE_CLOSURE');
pair('independent actual full base closure stdout',Buffer.from(cn.actual_return.output),read(I+'CLOSING_CHECK.json'));
const replay=json(R+'ROOT_REPLAY_NATIVE.json').records;
r.need(replay.length===2&&replay.every(x=>x.result.exit_code===0&&!('session_id'in x.result)),'TWO_ACTUAL_COMPLETED_DOCUMENTARY_REPLAYS');
r.need(replay[0].result.chunk_id==='068a6d'&&replay[0].request.cmd==='node '+I+'check_artifacts.mjs','EXACT_ROOT_ARTIFACT_REPLAY');
pair('root full artifact replay vs canonical',Buffer.from(replay[0].result.output),read(I+'ARTIFACT_CHECK.json'));
pair('root full artifact replay vs original native',Buffer.from(replay[0].result.output),Buffer.from(n.actual_return.output));
r.need(a.assertion_count===74&&Object.keys(a.assertions).length===74&&Object.values(a.assertions).every(x=>x===true),'ALL_74_ACTUAL_DOCUMENTARY_ASSERTIONS');
r.need(a.full_raw_pair_count===14&&a.full_raw_pairs.length===14&&a.full_raw_pairs.every(x=>x.byte_equal),'ALL_14_ORIGINAL_FIXED_DATA_PAIRS_REPLAYED');
r.need(replay[1].request.cmd==='node '+I+'close_check.mjs --sealed'&&replay[1].result.chunk_id==='07c4ff','EXACT_ROOT_FINAL_CLOSURE_REPLAY');
const sealed=JSON.parse(replay[1].result.output);
r.need(sealed.base_assertion_count===30&&sealed.sealed_assertion_count===7,'EXACT_30_PLUS_7_ACTUAL_FINAL_CHECKS');
r.need(Object.values(sealed.base_assertions).every(x=>x===true)&&Object.values(sealed.sealed_assertions).every(x=>x===true),'ALL_FINAL_CHECKS_TRUE');
r.need(sealed.payload_count===12&&sealed.physical_file_count===13&&sealed.physical_bytes===682382&&sealed.manifest.sha256===spec.independentSeal,'FINAL_SCOPE_BOUND');
const findings=json(I+'FINDINGS.json');
r.need(['critical','major','minor','current_open'].every(k=>findings[k]===0)&&findings.findings.length===0,'CENSUS_ZERO_EXAMINED_SCOPE');
r.need(findings.new_literal_attempts===1&&findings.closed_attempts===1&&findings.nominations===0&&findings.reserves===0&&findings.scientific_executions===0,'ONE_NEW_CLOSED_ZERO_PROMOTION');
r.need(findings.personal_author_noncontribution&&findings.inherited_root_familiarity_disclosed&&!findings.author_contact,'DISCLOSED_PERSONAL_NONSELF_SCOPE');
const rootReadCoverage=[],excludedReads=[];
function lines(b){return b.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];}
for(const archive of ['ROOT_READS_NATIVE.json','ROOT_AUDIT_READS_NATIVE.json']){
  for(const rec of json(R+archive).records){
    const command=rec.request.cmd,m=command.match(/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_./-]+)$/);
    if(!m||rec.result.exit_code!==0){excludedReads.push({archive,chunk:rec.result.chunk_id,command,exit:rec.result.exit_code,reason:'Navigation or actual failed basename read; no semantic completeness inferred'});continue;}
    const p=m[3];r.need(allowed.has(p),'ROOT_READ_FIXED_INPUT_ONLY');
    const expected=Buffer.from(lines(read(p)).slice(Number(m[1])-1,Number(m[2])).join(''));
    pair('actual root read '+rec.result.chunk_id,Buffer.from(rec.result.output),expected);
    rootReadCoverage.push({archive,path:p,start:Number(m[1]),end:Number(m[2]),chunk:rec.result.chunk_id,bytes:expected.length});
  }
}
r.need(rootReadCoverage.length===15,'EXACT_ROOT_COMPLETE_SUCCESSFUL_READ_RANGES');
const web=json(R+'ROOT_WEB_RETURNS.json');
r.need(web.records.length===3&&web.records.every(x=>typeof x.result==='string'&&x.result.length>0),'THREE_COMPLETE_SELECTED_PRIMARY_RETURNS');
const webPins=web.records.map((x,i)=>pin('root-primary-return-'+i,Buffer.from(x.result)));
const structurePins=[];
for(const [document,object]of [['artifact',a],['sealed',sealed],['findings',findings]]){
  let objects=0,arrays=0,scalars=0,strings=0;
  function walk(v){if(Array.isArray(v)){arrays++;for(const x of v)walk(x);}else if(v!==null&&typeof v==='object'){objects++;for(const [k,x]of Object.entries(v)){r.need(typeof k==='string','JSON_KEY');walk(x);}}else{scalars++;if(typeof v==='string')strings++;else if(typeof v==='number')r.need(Number.isFinite(v),'FINITE_DOCUMENT_NUMBER');}}
  walk(object);structurePins.push({document,objects,arrays,scalars,strings});
}
process.stdout.write(JSON.stringify({status:'PASS_FRESH20_ROOT_FIXED_DOCUMENT_RECEIPT_ONLY',scientific_execution:false,host_target_observation:false,new_attempts:1,closed_attempts:1,admissions:0,reserves:0,checks:r.checks,read_bytes:r.total,packages,raw_pair_count:rawPairs.length,raw_pairs:rawPairs,root_read_coverage:rootReadCoverage,excluded_reads:excludedReads,web_return_pins:webPins,structure_census:structurePins,keys:[...r.keys.values()]},null,2)+'\n');
