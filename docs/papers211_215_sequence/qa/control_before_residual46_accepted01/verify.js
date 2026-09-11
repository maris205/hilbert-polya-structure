'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics',base='docs/papers211_215_sequence/qa/control_before_residual46_accepted01',rp='docs/papers211_215_sequence/scouting/root_reception/residual_bgr_word_laver01';
const abs=p=>path.isAbsolute(p)?p:path.join(root,p),read=p=>fs.readFileSync(abs(p)),json=p=>JSON.parse(read(p)),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const need=(v,m)=>{checks++;if(!v)throw Error(m);};
const mapping=json(base+'/MAPPING.json'),cmp=json(base+'/CMP_NATIVE.json');
need(cmp.length===2&&cmp.every(x=>x.result.exit_code===0&&x.result.output===''),'two actual comparisons');
for(const m of mapping.rows){need(read(m.copy).length===m.bytes&&sha(read(m.copy))===m.sha256,'complete physical old '+m.original);const d=json(base+'/'+(m.original==='SYMBOLIC_DYNAMICS_STATE.md'?'STATE':'PIPELINE')+'.diff.json');need(d.result.exit_code===1,'actual expected diff');
 const old=read(m.copy).toString('utf8').split('\n'),lines=d.result.output.split('\n');let pos=0,out=[],hunks=0;
 for(let i=2;i<lines.length;){const head=lines[i++];if(!head)continue;const h=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@/.exec(head);need(!!h,'hunk header');hunks++;const start=+h[1]-1;out.push(...old.slice(pos,start));pos=start;let removed=0,added=0;
 while(i<lines.length&&!lines[i].startsWith('@@ ')){const l=lines[i++];if(i===lines.length&&l==='')break;if(l[0]===' '){need(old[pos]===l.slice(1),'context');out.push(old[pos++]);removed++;added++;}else if(l[0]==='-'){need(old[pos]===l.slice(1),'removed');pos++;removed++;}else if(l[0]==='+'){out.push(l.slice(1));added++;}else throw Error('unexpected diff line');}
 need(removed===+(h[2]||1)&&added===+(h[4]||1),'whole hunk counts');}
 out.push(...old.slice(pos));need(Buffer.from(out.join('\n')).equals(read(m.original)),'complete diff reconstruction');need(hunks>0,'changed control');}
const r=json(rp+'/RESULT.json');for(const k of r.complete_inputs){const b=read(k.path),s=fs.statSync(abs(k.path),{bigint:true}),l=fs.lstatSync(abs(k.path),{bigint:true});need(sha(b)===k.sha256&&b.length===k.bytes,'unchanged accepted input');for(const [o,t]of [[k.stat,s],[k.lstat,l]])for(const[f,v]of Object.entries(o))need(t[f].toString()===v,'unchanged rich field');}
const lines=read(rp+'/SHA256SUMS').toString().trimEnd().split('\n');need(lines.length===7,'root seal complete');for(const l of lines)need(sha(read(rp+'/'+l.slice(66)))===l.slice(0,64),'root seal');
const after=mapping.rows.map(m=>({path:m.original,bytes:read(m.original).length,sha256:sha(read(m.original))}));
need(read('SYMBOLIC_DYNAMICS_STATE.md').toString().split('\n').find(x=>x.startsWith('- 新一轮')).includes('累计46根接收关闭尝试'),'root current46');need(read('docs/papers211_215_sequence/PIPELINE_STATE.md').toString().includes('Closed literal attempts: 46. Reserves: 0.'),'batch current46');
const out={status:'PASS_SCOPED_RESIDUAL46_CONTROL_UPDATE',checks,unchanged_root_inputs:r.complete_inputs.length,root_seal_payload:lines.length,after};fs.writeFileSync(abs(base+'/RESULT.json'),JSON.stringify(out,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify(out,null,2));
