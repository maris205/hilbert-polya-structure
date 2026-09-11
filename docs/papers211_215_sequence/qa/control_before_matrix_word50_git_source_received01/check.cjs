'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const w='/root/autodl-tmp/symbolic_dynamics',o='docs/papers211_215_sequence/qa/control_before_matrix_word50_git_source_received01/';
const read=p=>fs.readFileSync(path.join(w,p)),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;function need(v,s){checks++;if(!v)throw Error(s);}
const map=JSON.parse(read(o+'MAPPING.json'));
for(const m of map.mappings){const b=read(m.copy);need(b.length===m.bytes&&sha(b)===m.sha256,'old physical '+m.copy);need(fs.lstatSync(path.join(w,m.copy)).isFile(),'physical regular copy');}
const state=read('SYMBOLIC_DYNAMICS_STATE.md').toString(),batch=read('docs/papers211_215_sequence/PIPELINE_STATE.md').toString();
const bs=read(o+'PIPELINE_STATE.md').toString(),ss=read(o+'SYMBOLIC_DYNAMICS_STATE.md').toString();
const begin=batch.indexOf('## Root-received CSS/word negatives and private executor source\n'),end=batch.indexOf('## Confirmed private checkpoint and temporal boundary\n');
need(begin>=0&&end>begin,'exact milestone range');
need((batch.slice(0,begin)+batch.slice(end)).replace('Closed literal attempts: 50. Reserves: 0.','Closed literal attempts: 48. Reserves: 0.')===bs,'only batch milestone and count');
const sl=state.split('\n'),ol=ss.split('\n');need(sl[2].includes('累计关闭50次尝试'),'date count');
sl[2]=ol[2];sl[6]=sl[6].replace('累计50根接收关闭尝试','累计48根接收关闭尝试');
const at=sl.findIndex(x=>x.startsWith('最新侦察／私有源码节点：'));need(at>=0&&sl[at+1]==='','one new state paragraph');sl.splice(at,2);need(sl.join('\n')===ss,'only exact state lifecycle changes');
const newtext=batch.slice(begin,end)+'\n'+state.split('\n')[at];
const links=[...newtext.matchAll(/\]\(([^)]+)\)/g)].map(x=>x[1]);for(const x of links){const p=x.startsWith('docs/')?x:path.posix.join('docs/papers211_215_sequence',x);need(fs.statSync(path.join(w,p)).isFile(),'milestone link '+p);}
for(const [dir,pin,n]of[['docs/papers211_215_sequence/scouting/root_reception/matrix_word04','79ddcfbbde75dc0990167987be2a9fd3a08e3a2f79141be5c7579e54f2b5f2ff',9],['docs/papers211_215_sequence/qa/private_checkpoint_executor_source_root03','21c30c73d7fb396a5f9c6456a7580b1e74681c8e262ef0fef57a9401df13a608',13]]){const s=read(dir+'/SHA256SUMS');need(sha(s)===pin,'root seal');const rows=s.toString().trimEnd().split('\n');need(rows.length===n,'root payload count');for(const r of rows){const m=/^([a-f0-9]{64})  (.+)$/.exec(r);need(!!m&&sha(read(dir+'/'+m[2]))===m[1],'root payload');}need(fs.readdirSync(path.join(w,dir)).length===n+1,'whole root packet');}
const p212=JSON.parse(read('docs/papers211_215_sequence/qa/p212_execution_scope_amendment_root01/APPLICATION_RESULT.json'));
let bytes=0;for(const k of p212.final_live_sources){const b=read(k.path);need(b.length===k.bytes&&sha(b)===k.sha256,'unchanged live source '+k.path);bytes+=b.length;}need(p212.final_live_sources.length===8&&bytes===20092,'eight live sources');
const lifecycle=JSON.parse(JSON.parse(read('docs/papers211_215_sequence/qa/p211_lifecycle_root01/CLOSING_NATIVE.json')).result.output);
const s211=read('papers/211-kernel-image-projection-feedback/SHA256SUMS');need(s211.length===lifecycle.paper_seal.bytes&&sha(s211)===lifecycle.paper_seal.sha256,'unchanged accepted P211 whole-paper seal');
const result={status:'PASS_LIFECYCLE_ONLY_MATRIX_WORD50_AND_GIT_SOURCE',checks,physical_previous:map.mappings,current:[{path:'docs/papers211_215_sequence/PIPELINE_STATE.md',bytes:Buffer.byteLength(batch),sha256:sha(Buffer.from(batch))},{path:'SYMBOLIC_DYNAMICS_STATE.md',bytes:Buffer.byteLength(state),sha256:sha(Buffer.from(state))}],closed_attempts:50,retained:2,completed:1,open:3,unchanged_p212_live_sources:8,unchanged_p211_accepted_manifest:true,new_scientific_build_view_replay:false,git_operation:false,external:'HOLD_EXTERNAL'};
process.stdout.write(JSON.stringify(result,null,2)+'\n');
