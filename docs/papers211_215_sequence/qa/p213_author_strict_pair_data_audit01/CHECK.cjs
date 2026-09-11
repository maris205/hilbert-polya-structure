'use strict';
// Fixed accepted documentary/raw inputs only. Never open a control-derived path.
const fs=require('node:fs'),crypto=require('node:crypto');
const Q='docs/papers211_215_sequence/qa/',S='papers/213-receiver-limited-cyclic-transfer/';
const O=Q+'p213_author_strict_pair_data_audit01/',R=Q+'p213_author_strict_pair_execution_root01/',A=Q+'p213_initial_science_data_audit01/',D=Q+'p213_initial_science_data_root01/',E=Q+'p213_initial_science_enabled_root01/',M=Q+'p213_initial_science_materialization_root01/',C=Q+'p213_author_canonical_adoption_root01/',P=Q+'p213_initial_science_enabled_preparation01/',I=Q+'p213_initial_science_run01/';
const W=Q+'p213_initial_science_enabled01/run_science.py',B=Q+'p213_initial_science_preparation01/BINDING.proposed.json',READER=E+'READ_FIXED.cjs',PARSER=Q+'p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs',CONTROL=A+'CONTROL_DATA.cjs';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const HASHES=[[READER,'f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7'],[PARSER,'9d6e081b7c8940f6730cc41c62bfc67862738eb49ded8f4021b6875583120471'],[CONTROL,'93607e331fe344ef87c8790e9f6ea452bbe8edc7b32734ede1ea108db7b31298'],[R+'INPUT_SPEC.json','e7f23bff78a2d5c1e3cff406324d8fde296154e04a23d93cffb519e8db0fe57b']];
const packages=[
 [R,'7c0fbb5782836aff63c28b57a94f60323a14d091275b802a11e675751010f9bb',20],
 [A,'353711b266e6eef4b51a7aceb8bb234b91abcd12d31ec7822de24efa94766a10',27],
 [D,'59337ecab14eb2c7e0155b48b460b6452f1ec4fb37396d3b1ca6beceb8642308',10]
];
function load(){
 if(process.cwd()!=='/root/autodl-tmp/symbolic_dynamics')throw Error('fixed DATA workspace');
 for(const[p,h]of HASHES)if(sha(fs.readFileSync(p))!==h)throw Error('accepted immutable helper/spec pin '+p);
 const make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
 const {parseIntegerJSON,typedEqual,canonicalIntegerJSON}=require('../p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs');
 const pkgNames=new Map();
 for(const[p,h,n]of packages){const raw=fs.readFileSync(p+'SHA256SUMS');if(sha(raw)!==h)throw Error('accepted nonself seal '+p);
  const lines=raw.toString('ascii').split('\n');if(lines.pop()!==''||lines.length!==n)throw Error('whole nonself seal framing');
  const names=lines.map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);if(!m||m[2]==='SHA256SUMS')throw Error('fixed leaf-only payload');return m[2];});
  if(new Set(names).size!==n)throw Error('duplicate manifest payload');pkgNames.set(p,[...names,'SHA256SUMS']);
 }
 const external=JSON.parse(fs.readFileSync(R+'INPUT_SPEC.json','utf8')).external.map(k=>k.path);
 // This exact 34-path list was personally read before the existing CLOSE replay;
 // its entire source spec is pinned above. No control path contributes a member.
 if(external.length!==34||external.some(p=>!(p.startsWith(Q)||p.startsWith(S))||p.includes('..')||p.includes('\\')))throw Error('fixed accepted external paths');
 const own=['ORIGIN.md','PAIR_DATA.cjs','CHECK.cjs','NEGATIVE.cjs','INPUT_NATIVE.json'];
 const paths=[...new Set([...external,...[...pkgNames].flatMap(([p,n])=>n.map(x=>p+x)),B,P+'run_science.proposed.py.txt',I+'stderr.bin',I+'runtime_control.bin','.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md',...own.map(n=>O+n)])];
 const r=make(new Set(paths)),{read,need,keys}=r;paths.forEach(read);
 const equal=(a,b,m)=>need(typedEqual(a,b),m),json=p=>JSON.parse(read(p));
 const full=(k,label)=>{need(k&&keys.has(k.path),'fixed full key '+label);equal(Object.keys(k).sort(),['path','eof','byte_count','complete','closed','lstat_before','fd_before','eof_zero_return','fd_after','lstat_after','sha256'].sort(),'complete key fields '+label);
  need(k.eof===true&&k.eof_zero_return===0&&k.complete===true&&k.closed===true,'actual EOF/close '+label);
  for(const n of ['lstat_before','fd_before','fd_after','lstat_after']){equal(Object.keys(k[n]).sort(),r.fields.slice().sort(),'all ten metadata fields '+label);for(const v of Object.values(k[n]))need(typeof v==='string'&&/^(0|-?[1-9][0-9]*)$/.test(v),'lossless metadata '+label);}
  equal(k,keys.get(k.path),'entire current/original key '+label);};
 const runs=['01','02'].map(num=>{const raw=Q+'p213_author_strict_pair_run'+num+'/',parsed=parseIntegerJSON(read(raw+'runtime_control.bin').toString('ascii'));
  return {id:num,stage:'replay'+num,nativeId:json(R+'ACTUAL.replay'+num+'.NATIVE.json').result.chunk_id,grantId:json(R+'CONSUMPTION.replay'+num+'.json').grant_id,
   control:parsed.data,controlRaw:read(raw+'runtime_control.bin'),
   external:{sources:Object.fromEntries([W,S+'verify.py'].map(p=>['/root/autodl-tmp/symbolic_dynamics/'+p,keys.get(p)])),raw:{stdout:keys.get(raw+'stdout.bin'),stderr:keys.get(raw+'stderr.bin'),control:keys.get(raw+'runtime_control.bin')}}};});
 return {r,read,need,keys,equal,json,full,runs,pkgNames,paths,parseIntegerJSON,canonicalIntegerJSON,binding:parseIntegerJSON(read(B).toString('ascii')).data};
}
function audit(){
 const f=load(),{r,read,need,keys,equal,json,full,runs,pkgNames,parseIntegerJSON,canonicalIntegerJSON,binding}=f;
 const report={scope:'INDEPENDENT_TWO_NEW_STRICT_CONTROLS_DATA_ONLY',status:'RUNNING',packages:[],raw_pairs:[],old_key_occurrences:{preflight:0,raw:0,other:0,reused_initial_premises:0},science_execution:false,host_queries:false,new_grant:false,manuscript_review:false};
 const rawEq=(a,b,label)=>{need(a.equals(b),'whole RAW equality '+label);report.raw_pairs.push({label,bytes:a.length,sha256:sha(a)});};
 const native=(n,chunk,cmd)=>{need(n&&n.request&&n.result,'actual native envelope');equal(Object.keys(n.result).sort(),['chunk_id','wall_time_seconds','exit_code','original_token_count','output'].sort(),'complete actual native result');
  need(n.result.chunk_id===chunk&&n.result.exit_code===0&&typeof n.result.output==='string'&&!n.result.output.startsWith('Warning: truncated output'),'complete actual successful native '+chunk);
  need(n.request.cmd===cmd&&n.request.workdir==='/root/autodl-tmp/symbolic_dynamics','exact actual documentary native request '+chunk);return n.result.output;};
 for(const[p,h,n]of packages){const names=pkgNames.get(p);equal(fs.readdirSync(p).sort(),names.slice().sort(),'whole explicit accepted packet membership');
  const expected=names.filter(x=>x!=='SHA256SUMS').map(x=>sha(read(p+x))+'  '+x+'\n').join('');rawEq(Buffer.from(expected),read(p+'SHA256SUMS'),'complete nonself manifest '+p);
  need(sha(read(p+'SHA256SUMS'))===h,'accepted seal');report.packages.push({path:p,payloads:n,files:n+1,payload_bytes:names.filter(x=>x!=='SHA256SUMS').reduce((s,x)=>s+read(p+x).length,0),seal:h});
 }
 for(const[p,h]of HASHES)need(sha(read(p))===h,'whole currently keyed helper/spec bytes');
 for(const[p,bytes,h]of[[W,108715,'87cd4409bf5394792f66318893cc9e187ff43c1419bcfd819f17f874cdb7c121'],[S+'verify.py',17539,'a01d3d93619cea90adfc2e5be1bdfd8089d7eae6fcaae153b4fb4af398fc1812'],[B,null,'78da1d06c05cd6244e9de9c1565a843823051e98c8702c07c5447e20d1da3ab6']]){need(sha(read(p))===h&&(bytes===null||read(p).length===bytes),'complete accepted executable/binding bytes as DATA');}
 rawEq(read(W),read(P+'run_science.proposed.py.txt'),'entire proposed/materialized wrapper');
 // Same literal rendering as the accepted source gate; no Python/AST/eval.
 const jsonBinding=JSON.stringify(json(B),null,2);let py='',inside=false,escape=false;
 for(let i=0;i<jsonBinding.length;i++){const ch=jsonBinding[i];if(inside){py+=ch;if(escape)escape=false;else if(ch==='\\')escape=true;else if(ch==='"')inside=false;continue;}if(ch==='"'){inside=true;py+=ch;continue;}const m=/^(true|false|null)\b/.exec(jsonBinding.slice(i));if(m){py+=({true:'True',false:'False',null:'None'})[m[1]];i+=m[1].length-1;}else py+=ch;}
 need(read(W).toString('ascii').startsWith('# Prospective enabled bytes; materialization and execution require separate authority.\n\nBINDING = '+py+'\n\nif BINDING is None:\n'),'entire exact embedded binding literal');
 const archived=json(O+'INPUT_NATIVE.json');
 need(archived.replays.length===3,'all three actual permitted DATA replays');
 for(let i=0;i<2;i++){
  const num=i===0?'01':'02',stage='replay'+num,run=runs[i],raw=Q+'p213_author_strict_pair_run'+num+'/',g=json(R+'GRANT.'+stage+'.json'),c=json(R+'CONSUMPTION.'+stage+'.json'),a=json(R+'ACTUAL.'+stage+'.NATIVE.json'),request=json(P+'REQUEST.'+stage+'.proposed.json');
  equal(Object.keys(g).sort(),['id','kind','status','permitted_native_submissions','consumed','stage','native_request','continuation','source_acceptance','materialization','initial_data','canonical_adoption','canonical_pin','preflight','record_consumption_before_submission','old_initial_or_probe_grants_reused','initial_counts_as_replay','other_run_granted','automatic_retry','on_failure','scope'].concat(i===1?['first_run_cutoff']:[]).sort(),'entire grant fields');
  if(i===1)equal(g.first_run_cutoff,{actual_native_chunk_id:'2aa611',exit_code:0,grant_consumed:true,raw_receiver_chunk_id:'a0a5dc',full_control_semantics_accepted:false,pair_accepted:false,meaning:"The first run's entire raw bytes are received and science stdout RAW equals canonical. Its new control remains pending independent acceptance. This distinct grant does not borrow its permission."},'entire actual first-run cutoff in second grant');
  need(g.id==='P213_AUTHOR_STRICT_PAIR_NEW_RUN_'+num&&g.stage===stage&&g.kind==='DISTINCT_OPERATION_SPECIFIC_ROOT_GRANT'&&g.status==='GRANTED_SUBJECT_TO_CURRENT_EXACT_PREFLIGHT_UNCONSUMED_AT_ISSUANCE'&&g.permitted_native_submissions===1&&g.consumed===false&&g.record_consumption_before_submission===true,'historical distinct one-use grant');
  for(const k of ['old_initial_or_probe_grants_reused','initial_counts_as_replay','other_run_granted','automatic_retry'])equal(g[k],false,'grant limit '+k);
  equal(g.native_request,request.proposed_native_request,'whole accepted proposed/granted native request');equal(g.continuation,request.proposed_continuation,'whole unused continuation proposal');
  equal(a.request,g.native_request.arguments,'whole actually submitted native request');equal(a.continuations,[],'no continuation/session substitution');equal(a.tool,'exec_command','actual scientific tool');
  equal(Object.keys(a.result).sort(),['chunk_id','wall_time_seconds','exit_code','original_token_count','output'].sort(),'entire scientific native result fields');
  need(a.result.chunk_id===run.nativeId&&a.result.exit_code===0&&!a.result.session_id,'actual complete scientific native identity');
  rawEq(Buffer.from(a.result.output),Buffer.from('P213_SCIENCE_NATIVE_EXIT=0\n'),'complete actual scientific native return '+num);
  rawEq(Buffer.from(a.request.cmd),read(P+'capture.'+stage+'.proposed.sh.txt'),'entire actual capture bytes '+num);
  equal(Object.keys(c).sort(),['grant_id','status','remaining_submissions','exact_native_request','preflight_original','preflight_actual_chunk_id','actual_result','automatic_retry','old_grant_reused','meaning'].sort(),'entire consumption fields');
  need(c.grant_id===g.id&&c.status==='CONSUMED_BEFORE_NATIVE_SUBMISSION'&&c.remaining_submissions===0&&c.actual_result===null&&c.automatic_retry===false&&c.old_grant_reused===false,'actual pre-submission consumed boundary');equal(c.exact_native_request,g.native_request,'entire consumed request');equal(c.preflight_original,'PREFLIGHT.'+stage+'.NATIVE.json','own preflight record');
  for(const[field,p,leaf]of[['source_acceptance',E,'RECEPTION.md'],['materialization',M,'RECEIPT.md'],['initial_data',D,'RECEPTION.md'],['canonical_adoption',C,'RECEIPT.md']])equal(g[field],{receipt:p+leaf,sha256:sha(read(p+leaf)),seal:sha(read(p+'SHA256SUMS'))},'complete current granted prerequisite '+field);
  full(g.canonical_pin,'full granted canonical');report.old_key_occurrences.other++;
  const pre=json(R+'PREFLIGHT.'+stage+'.NATIVE.json'),preId=i===0?'2a4e1c':'a1cd2a',pv=JSON.parse(native(pre,preId,'node '+R+'PREFLIGHT.cjs '+stage));
  need(c.preflight_actual_chunk_id===preId&&pv.stage===stage&&pv.status==='PASS_CURRENT_PREFLIGHT_FOR_NEW_DISTINCT_STRICT_RUN'&&pv.keys.length===27,'entire actual historical preflight');
  equal(pv.exact_native_request,g.native_request,'full historical preflight request');for(const k of pv.keys){full(k,stage+' preflight');report.old_key_occurrences.preflight++;}
  need(pv.output_directory.actual_lstat_errno==='ENOENT','recorded historical absence, no rerun');
  const original=json(R+'RAW.'+stage+'.NATIVE.json'),rv=JSON.parse(native(original,i===0?'a0a5dc':'d64a46','node '+R+'RAW_RECEIVE.cjs '+stage));
  need(rv.keys.length===36&&rv.status==='PASS_COMPLETE_STRICT_RAW_BYTES_PENDING_INDEPENDENT_CONTROL_AND_PAIR_RECEPTION','whole original raw reception');
  for(const k of rv.keys){full(k,stage+' original raw');report.old_key_occurrences.raw++;}
  for(const k of rv.raw_keys){full(k,stage+' raw alias');report.old_key_occurrences.other++;}
  const replay=archived.replays[i],replayId=i===0?'cfd5c2':'c68be9';
  rawEq(Buffer.from(native(replay,replayId,'node '+R+'RAW_RECEIVE.cjs '+stage)),Buffer.from(original.result.output),'entire actual/original RAW_RECEIVE stdout '+num);
  const nr=JSON.parse(replay.result.output);for(const k of nr.keys){full(k,stage+' own raw replay');report.old_key_occurrences.other++;}
  const parsed=parseIntegerJSON(run.controlRaw.toString('ascii'));equal(parsed.counts,rv.control_integer_counts,'entire per-run lossless integer census');
  rawEq(Buffer.from(canonicalIntegerJSON(parsed.data)+'\n','ascii'),run.controlRaw,'complete per-run original control roundtrip '+num);
  need(read(raw+'stderr.bin').length===0,'entire empty scientific stderr');rawEq(read(raw+'stdout.bin'),read(S+'canonical_stdout.txt'),'run/canonical complete science '+num);rawEq(read(raw+'stdout.bin'),read(I+'stdout.bin'),'run/initial complete science '+num);
 }
 need(report.old_key_occurrences.preflight===54&&report.old_key_occurrences.raw===72,'exact54 preflight and72 raw original key occurrences');
 const finalReplay=archived.replays[2],fr=JSON.parse(native(finalReplay,'7e88cf','node '+R+'CLOSE.cjs --sealed'));
 need(fr.status==='PASS_STRICT_EXECUTION_RAW_DOCUMENTARY_CLOSURE'&&fr.phase==='FINAL_TWENTY_PAYLOADS'&&fr.key_count===55&&fr.entire_prior_keys===218,'entire actual execution-final replay');
 for(const k of fr.keys){full(k,'own execution final');report.old_key_occurrences.other++;}
 const prior=json(A+'CHECK_NATIVE.json'),priorReport=JSON.parse(prior.native.output),priorRoot=json(D+'RESULT.json'),priorRootNative=json(D+'CHECK_NATIVE.json'),rootReplays=json(D+'REPLAY_NATIVE.json');
 need(prior.native.chunk_id==='a18585'&&prior.native.exit_code===0&&priorReport.status==='PASS_INDEPENDENT_INITIAL_CAPTURE_CONTROL_AND_BOUNDED_SCIENCE_DATA','actual complete earlier independent scientific semantics');
 rawEq(Buffer.from(prior.native.output),read(A+'DOCUMENTARY_CANONICAL.txt'),'whole prior independent DATA stdout/canonical');
 rawEq(Buffer.from(rootReplays.records[0].result.output),read(A+'DOCUMENTARY_CANONICAL.txt'),'whole accepted root semantic replay/original');
 need(rootReplays.records[0].result.chunk_id==='4dcc30'&&rootReplays.records[0].result.exit_code===0&&priorRoot.status==='PASS_ROOT_ORIGINAL_INITIAL_CONTROL_AND_BOUNDED_SCIENCE_DATA','actual accepted initial root semantic provenance');
 rawEq(Buffer.from(priorRootNative.result.output),read(D+'RESULT.json'),'whole accepted root native/result');
 const reused=[W,P+'run_science.proposed.py.txt',B,READER,PARSER,CONTROL,A+'SCIENCE_DATA.cjs',...['verify.py','VERIFICATION_PARAMETERS.json','OUTPUT_SCHEMA.md','SCIENTIFIC_DEPENDENCIES.md','RUNTIME_PLAN.md','REVIEW_INTERFACES.md'].map(n=>S+n),...['stdout.bin','stderr.bin','runtime_control.bin'].map(n=>I+n)];
 for(const p of reused)for(const[label,old]of[['independent',priorReport],['root',priorRoot]]){const k=old.keys.find(x=>x.path===p);need(!!k,'full prior semantic premise exists '+p);full(k,label+' semantic premise');report.old_key_occurrences.reused_initial_premises++;}
 equal(priorReport.science,priorRoot.science_scope,'entire accepted bounded scientific semantics, not only counts');report.science_semantics_reused=priorRoot.science_scope;
 rawEq(read(I+'stdout.bin'),read(S+'canonical_stdout.txt'),'whole accepted initial/canonical physical copy');
 rawEq(read(Q+'p213_author_strict_pair_run01/stdout.bin'),read(Q+'p213_author_strict_pair_run02/stdout.bin'),'whole strict pair science');
 const cmp=json(R+'CMP_NATIVE.json');need(cmp.native.length===3,'all actual native raw comparisons');
 for(const[i,[left,right]]of [[Q+'p213_author_strict_pair_run01/stdout.bin',S+'canonical_stdout.txt'],[Q+'p213_author_strict_pair_run02/stdout.bin',S+'canonical_stdout.txt'],[Q+'p213_author_strict_pair_run01/stdout.bin',Q+'p213_author_strict_pair_run02/stdout.bin']].entries())need(cmp.native[i].request.cmd==='cmp -- '+left+' '+right&&cmp.native[i].result.exit_code===0&&cmp.native[i].result.output===''&&!cmp.native[i].result.session_id,'entire original actual cmp '+i);
 let fullReadPairs=0;for(const n of archived.reads){if(n.result.exit_code!==0||n.result.output.startsWith('Warning: truncated output')||!n.request.cmd.startsWith('cat ')||n.request.cmd.includes(' && '))continue;const paths=n.request.cmd.slice(4).split(' ');if(paths.every(p=>keys.has(p))){rawEq(Buffer.from(n.result.output),Buffer.concat(paths.map(read)),'entire personally read source/document output '+n.result.chunk_id);fullReadPairs++;}}
 report.whole_personal_read_outputs=fullReadPairs;
 report.pair=require('./PAIR_DATA.cjs')(runs,binding);
 report.status='PASS_INDEPENDENT_NEW_STRICT_PAIR_DATA_PENDING_ROOT_RECEPTION';
 report.documentary_checks=r.checks;report.key_count=keys.size;report.total_read_bytes=r.total;report.keys=[...keys.values()];
 return report;
}
module.exports={load,audit};
if(require.main===module){
 let result;try{if(process.argv.length!==2)throw Error('no-argument DATA audit only');result=audit();}
 catch(e){result={status:'HOLD_DATA_AUDIT_FAILURE',failure:{name:e.name,code:e.code||null,message:e.message,stack:e.stack},science_execution:false,host_queries:false};process.exitCode=1;}
 process.stdout.write(JSON.stringify(result,null,2)+'\n');
}
