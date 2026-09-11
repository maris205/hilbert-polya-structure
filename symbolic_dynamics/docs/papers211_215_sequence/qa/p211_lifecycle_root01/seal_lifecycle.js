'use strict';
const fs=require('node:fs'),p=require('node:path'),c=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',HERE=ROOT+'/docs/papers211_215_sequence/qa/p211_lifecycle_root01';
function key(b){return {bytes:b.length,sha256:c.createHash('sha256').update(b).digest('hex')};}
const n=JSON.parse(fs.readFileSync(HERE+'/CLOSING_NATIVE.json')),r=fs.readFileSync(HERE+'/CLOSING_RESULT.json');
a.equal(n.result.exit_code,0);a.deepEqual(JSON.parse(n.result.output).result,key(r));a.equal(JSON.parse(r).paper_complete,true);
const links=[];for(const m of fs.readFileSync(HERE+'/RECEPTION.md','utf8').matchAll(/\[[^\]\n]*\]\(([^)\n]+)\)/g)){
 if(/^(https?:|#)/.test(m[1]))continue;const q=p.resolve(HERE,m[1]);a.ok(q.startsWith(ROOT+'/'));a.ok(fs.statSync(q).isFile());links.push({literal:m[1],path:q,key:key(fs.readFileSync(q))});
}
fs.writeFileSync(HERE+'/FINAL_RECEIPT_LINKS.json',JSON.stringify({status:'ALL_FINAL_RECEPTION_LINKS_RESOLVED',links},null,2)+'\n',{flag:'wx'});
const names=fs.readdirSync(HERE).sort();a.ok(!names.includes('SHA256SUMS'));
const seal=Buffer.from(names.map(x=>{a.ok(fs.lstatSync(HERE+'/'+x).isFile());return key(fs.readFileSync(HERE+'/'+x)).sha256+'  '+x+'\n';}).join(''));
fs.writeFileSync(HERE+'/SHA256SUMS',seal,{flag:'wx'});
console.log(JSON.stringify({status:'P211_LIFECYCLE_PACKET_SEALED',payloads:names.length,files:names.length+1,seal:key(seal),final_receipt_links:links.length,paper_complete:true,batch_complete:false}));
