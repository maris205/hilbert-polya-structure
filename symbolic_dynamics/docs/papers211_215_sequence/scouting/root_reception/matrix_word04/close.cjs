'use strict';
const fs=require('fs'), path=require('path'), crypto=require('crypto');
const w='/root/autodl-tmp/symbolic_dynamics', o='docs/papers211_215_sequence/scouting/root_reception/matrix_word04/';
let checks=0;function need(v,s){checks++;if(!v)throw Error(s);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const raw=fs.readFileSync(path.join(w,o,'RESULT.json'));
const native=JSON.parse(fs.readFileSync(path.join(w,o,'RECEIVE_NATIVE.json')));
need(native.result.exit_code===0,'native status');need(raw.equals(Buffer.from(native.result.output)),'raw attached stdout');
const j=JSON.parse(raw);need(j.checks===940&&j.complete_input_keys.length===53&&j.native_complete_source_returns.length===30,'receipt census');
for(const k of j.complete_input_keys){const a=path.join(w,k.path),s=fs.lstatSync(a,{bigint:true});need(s.isFile(),'regular '+k.path);for(const [n,v] of Object.entries(k.lstat))need(s[n].toString()===v,'lstat '+n+' '+k.path);const b=fs.readFileSync(a);need(b.length===k.bytes&&sha(b)===k.sha256&&fs.realpathSync(a)===k.resolved,'whole input '+k.path);}
need(fs.readFileSync(path.join(w,o,'RECEPTION.md'),'utf8').includes('ROOT_ACCEPTED_NO_PROMOTION'),'root decision');
process.stdout.write(JSON.stringify({status:'PASS_ROOT_NEGATIVE_CLOSING',checks,keys:53,source_returns:30,result_bytes:raw.length,result_sha256:sha(raw),closed_literal_delta:2,science:0,manuscript_reviews:0,git:0})+'\n');
