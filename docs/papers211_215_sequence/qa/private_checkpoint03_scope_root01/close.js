'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics',p='docs/papers211_215_sequence/qa/private_checkpoint03_scope_root01';
const abs=n=>path.isAbsolute(n)?n:path.join(root,n),read=n=>fs.readFileSync(abs(n)),sha=b=>crypto.createHash('sha256').update(b).digest('hex');let checks=0;const need=(v,m)=>{checks++;if(!v)throw Error(m);};
const r=JSON.parse(read(p+'/RESULT.json')),i=JSON.parse(read(p+'/INPUTS.json')),c=JSON.parse(read(p+'/CHOSEN_SCOPE.json')),n=JSON.parse(read(p+'/RECEIVE_NATIVE.json'));
need(r.status==='PASS_ROOT_CHECKPOINT03_SOURCE_SCOPE'&&r.checks===242538&&i.files.length===11129,'actual scope');
need(n.initial.result.session_id===n.poll.poll.session_id&&n.poll.result.exit_code===0,'actual root session');const a=JSON.parse(n.poll.result.output);need(a.checks===r.checks&&a.input_files===i.files.length&&JSON.stringify(a.selected)===JSON.stringify(r.selected),'actual native result');
for(const [file,k]of [['INPUTS.json',r.inputs],['CHOSEN_SCOPE.json',r.chosen_key]])need(read(p+'/'+file).length===k.bytes&&sha(read(p+'/'+file))===k.sha256,'whole saved object');
for(const k of i.files){const b=read(k.path),s=fs.lstatSync(abs(k.path),{bigint:true});need(s.isFile()&&fs.realpathSync(abs(k.path))===k.resolved&&b.length===k.bytes&&sha(b)===k.sha256,'full input '+k.path);for(const[f,v]of Object.entries(k.lstat))need(s[f].toString()===v,'rich key '+k.path+' '+f);}
need(c.counts.files===8207&&c.counts.bytes===386716363&&c.counts.additions===8204&&c.counts.modifications===2&&c.counts.unchanged===1&&c.minimum_free_bytes===2333581815,'exact chosen scope');
const g=JSON.parse(read(p+'/BRIDGE_GIT_NATIVE.json'));need(g.native_exit===0&&g.signal===null&&!g.error&&g.stdout_base64===''&&g.stderr_base64==='','actual bridge query');
const text=read(p+'/RECEPTION.md').toString();for(const m of text.matchAll(/\]\(([^)]+)\)/g))need(fs.statSync(path.resolve(abs(p),m[1])).isFile(),'receipt link');
const files=fs.readdirSync(abs(p)).sort();need(!files.includes('SHA256SUMS'),'exclusive seal');const seal=files.map(f=>sha(read(p+'/'+f))+'  '+f).join('\n')+'\n';fs.writeFileSync(abs(p+'/SHA256SUMS'),seal,{flag:'wx'});for(const f of files)need(fs.lstatSync(abs(p+'/'+f)).isFile(),'flat sealed payload');
console.log(JSON.stringify({status:'PASS_CHECKPOINT03_SCOPE_ROOT_CLOSING',checks,input_path_spellings:i.files.length,selected:c.counts,payload:files.length,files:files.length+1,manifest:{bytes:Buffer.byteLength(seal),sha256:sha(Buffer.from(seal))},git_mutations:0,private_push:false},null,2));
