// Documentation only: no mathematical producer import or execution.
'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto'),cp=require('child_process');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const P='docs/papers211_215_sequence/scouting/arithmetic_automata_residual02';
const HERE='docs/papers211_215_sequence/scouting/root_reception/arithmetic_automata02';
let checks=0;const need=(x,m)=>{checks++;if(!x)throw Error(m);};
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(path.join(ROOT,p));
const fields=['dev','mode','nlink','uid','gid','rdev','blksize','ino','size','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const stats=s=>Object.fromEntries(fields.map(f=>[f,s[f].toString()]));
function key(p){const abs=path.join(ROOT,p),a=fs.lstatSync(abs,{bigint:true}),b=fs.statSync(abs,{bigint:true});need(a.isFile()&&!a.isSymbolicLink()&&b.isFile(),'physical file '+p);const raw=read(p);return {path:p,bytes:raw.length,sha256:hash(raw),resolved:fs.realpathSync(abs),lstat:stats(a),stat:stats(b)};}
const stable=k=>{const v=JSON.parse(JSON.stringify(k));delete v.stat.atimeNs;delete v.lstat.atimeNs;return v;};
function rows(b){return b.toString('utf8').trimEnd().split('\n').map(l=>{const m=/^([0-9a-f]{64})  (.+)$/.exec(l);need(!!m,'pin syntax');return {sha:m[1],path:m[2]};});}
const manifest=rows(read(P+'/SHA256SUMS')),inputs=rows(read(P+'/INPUT_PINS.sha256'));
need(manifest.length===7&&inputs.length===9,'complete declared lists');
need(fs.readdirSync(path.join(ROOT,P)).sort().join('\n')===[...manifest.map(x=>x.path),'SHA256SUMS'].sort().join('\n'),'exact eight-file inventory');
for(const x of manifest){need(!x.path.includes('/')&&x.path!=='SHA256SUMS','flat nonself');need(hash(read(P+'/'+x.path))===x.sha,'whole payload '+x.path);}
for(const x of inputs)need(hash(read(x.path))===x.sha,'whole historical input '+x.path);
const history=JSON.parse(read(P+'/READ_RECORDS.json'));
need(history.selected_returns.length===15&&history.other_call_index.length===44,'exact documentary record boundary');
const sed=history.selected_returns.filter(x=>(x.command??x.cmd).startsWith('sed ')&&x.result.exit_code===0);
const paths=[...new Set([...manifest.map(x=>P+'/'+x.path),P+'/SHA256SUMS',...inputs.map(x=>x.path),...sed.map(x=>(x.command??x.cmd).split(' ').at(-1)),HERE+'/receive.js',HERE+'/ROOT_LOCAL_READS.json',HERE+'/PRIMARY_READS.json'])].sort();
const before=paths.map(key),native=[];
need(sed.length===12,'twelve complete successful source slices');
for(const x of sed){const cmd=x.command??x.cmd,m=/^sed -n '([0-9]+),([0-9]+)p' ([A-Za-z0-9_./-]+)$/.exec(cmd);need(!!m,'bounded literal sed');const r=cp.spawnSync('/usr/bin/sed',['-n',m[1]+','+m[2]+'p',m[3]],{cwd:ROOT,encoding:null,maxBuffer:1048576});need(r.status===0&&r.signal===null&&r.stderr.length===0,'actual sed closure');need(r.stdout.equals(Buffer.from(x.result.output,'utf8')),'whole decoded native source output '+x.index);native.push({source_index:x.index,command:['/usr/bin/sed','-n',m[1]+','+m[2]+'p',m[3]],cwd:ROOT,exit_status:r.status,signal:r.signal,stdout_utf8:r.stdout.toString('utf8'),stderr_utf8:r.stderr.toString('utf8'),stdout_bytes:r.stdout.length,stdout_sha256:hash(r.stdout),comparison:'raw bytes equal the complete saved decoded UTF-8 output'});}
for(const x of history.selected_returns){const m=history.other_call_index.find(y=>y.index===x.index);need(!!m&&m.cmd===(x.command??x.cmd)&&m.chunk_id===x.result.chunk_id&&m.exit_code===x.result.exit_code&&m.output_in_selected_returns===true,'actual metadata binding '+x.index);need(!/tokens truncated|^Warning: truncated output/m.test(x.result.output),'selected return complete');}
const failed=history.selected_returns.find(x=>x.index===37);need(failed.result.exit_code===2&&failed.result.output.includes('No such file or directory'),'preserve failed guessed path; no reexecution');
const sh=history.selected_returns.find(x=>x.index===43);need(sh.result.exit_code===0&&Buffer.from(sh.result.output).equals(read(P+'/INPUT_PINS.sha256')),'whole original nine-row pin output');
const rg=history.selected_returns.find(x=>x.index===40);need(rg.result.exit_code===0&&rg.result.output.trimEnd().split('\n').length===3,'three-line original discovery preserved, not executed or raw-replay claimed');
const local=JSON.parse(read(HERE+'/ROOT_LOCAL_READS.json'));need(local.runs.length===9,'nine actual root original reads');for(const x of local.runs){const m=/^sed -n '([0-9]+),([0-9]+)p' (.+)$/.exec(x.request.cmd);need(!!m&&x.result.exit_code===0,'root read valid');const r=cp.spawnSync('/usr/bin/sed',['-n',m[1]+','+m[2]+'p',m[3]],{cwd:ROOT,encoding:null,maxBuffer:1048576});need(r.status===0&&r.stderr.length===0&&r.stdout.equals(Buffer.from(x.result.output)),'root whole decoded read exact');}
const decision=JSON.parse(read(P+'/DECISIONS.json'));need(decision.literal_attempts===2&&decision.candidates.length===2&&decision.promotions===0&&decision.reserves===0&&decision.new_scientific_executions===0,'two negatives no science');
need(decision.candidates[1].published_n_step_comparison==='UNRESOLVED_EXACT_VARIANT_COMPARISON'&&decision.candidates[1].earlier_legitimacy_vs_recurrence_explanation==='WITHDRAWN_FOR_THIS_LITERAL','source boundary retained');
const web=JSON.parse(read(P+'/PRIMARY_REQUESTS.json'));need(web.requests.length===11&&web.read_annotations.length===4,'metadata-only primary boundary');
const after=paths.map(key);for(let i=0;i<paths.length;i++)need(JSON.stringify(stable(before[i]))===JSON.stringify(stable(after[i])),'whole documentary stable key '+paths[i]);
process.stdout.write(JSON.stringify({status:'PASS_DOCUMENTARY_ORIGINAL_RECEPTION_ONLY',checks,paths:paths.length,payloads:7,payload_bytes:manifest.reduce((s,x)=>s+read(P+'/'+x.path).length,0),input_pins:9,before,after,native,original_selected_records:15,metadata_only_local_index:44,primary_metadata_requests:11,source_slices:12,root_original_reads:9,failures_preserved:[{index:37,original:failed}],scientific_execution:false,proof_or_review_pass:false,atime_policy:'recorded but excluded from stable comparison; all other thirteen fields per stat/lstat compared',scope:'No candidate or manuscript code imported; only documentation reads/hash/source-slice comparisons. Source full hashes do not assert whole-file human reading.'},null,2)+'\n');
