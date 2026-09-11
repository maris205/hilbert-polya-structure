'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics', base='docs/papers211_215_sequence/scouting/root_reception/residual_bgr_word_laver01';
const abs=p=>path.isAbsolute(p)?p:path.join(root,p), sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;function need(v,m){checks++;if(!v)throw Error(m);}
const resultBytes=fs.readFileSync(abs(base+'/RESULT.json')),r=JSON.parse(resultBytes),n=JSON.parse(fs.readFileSync(abs(base+'/RECEIVE_NATIVE.json')));
need(n.result.exit_code===0&&Buffer.from(n.result.output).equals(resultBytes),'complete actual native bytes');
need(r.status==='PASS_ROOT_NEGATIVE_DOCUMENTARY_RECEPTION'&&r.checks===580&&r.closed_literal_delta===3,'exact root scope');
for(const k of r.complete_inputs){const a=abs(k.path),b=fs.readFileSync(a),l=fs.lstatSync(a,{bigint:true}),s=fs.statSync(a,{bigint:true});need(sha(b)===k.sha256&&b.length===k.bytes&&fs.realpathSync(a)===k.resolved,'content '+k.path);for(const [old,now] of [[k.lstat,l],[k.stat,s]])for(const [f,v]of Object.entries(old))need(now[f].toString()===v,'stat '+k.path+' '+f);}
const text=fs.readFileSync(abs(base+'/RECEPTION.md'),'utf8');let links=0;for(const m of text.matchAll(/\]\(([^)]+)\)/g)){if(/^https?:/.test(m[1]))continue;need(fs.statSync(path.resolve(abs(base),m[1])).isFile(),'reception link');links++;}
const all=fs.readdirSync(abs(base)).sort();need(!all.includes('SHA256SUMS'),'new-only seal');
const rows=all.map(p=>{need(fs.lstatSync(abs(base+'/'+p)).isFile(),'flat payload');return sha(fs.readFileSync(abs(base+'/'+p)))+'  '+p;});
const seal=Buffer.from(rows.join('\n')+'\n');fs.writeFileSync(abs(base+'/SHA256SUMS'),seal,{flag:'wx'});
for(const row of rows){const p=row.slice(66);need(sha(fs.readFileSync(abs(base+'/'+p)))===row.slice(0,64),'final payload '+p);}
console.log(JSON.stringify({status:'PASS_ROOT_NEGATIVE_CLOSING',checks,complete_inputs:r.complete_inputs.length,source_native_bindings:r.native_source_records.length,local_links:links,payload:rows.length,files:rows.length+1,result:{bytes:resultBytes.length,sha256:sha(resultBytes)},manifest:{bytes:seal.length,sha256:sha(seal)}},null,2));
