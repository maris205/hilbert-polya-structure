'use strict';
const fs=require('node:fs'),p=require('node:path'),c=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',HERE=ROOT+'/docs/papers211_215_sequence/qa/control_before_p211_completed01';
function key(b){return {bytes:b.length,sha256:c.createHash('sha256').update(b).digest('hex')};}
function transform(old,diff){const original=old.toString('utf8').split('\n');a.equal(original.pop(),'');const ds=diff.split('\n');a.ok(ds[0].startsWith('--- '));a.ok(ds[1].startsWith('+++ '));let cursor=0,i=2,out=[],hunks=0;while(i<ds.length&&ds[i]!==''){const m=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@/.exec(ds[i++]);a.ok(m);hunks++;const start=+m[1]-1;out.push(...original.slice(cursor,start));cursor=start;let gone=0,added=0;while(i<ds.length&&!ds[i].startsWith('@@ ')&&ds[i]!==''){const l=ds[i++],op=l[0],text=l.slice(1);a.ok([' ','+','-'].includes(op));if(op!=='+' ){a.equal(original[cursor++],text);gone++;}if(op!=='-'){out.push(text);added++;}}a.equal(gone,m[2]===undefined?1:+m[2]);a.equal(added,m[4]===undefined?1:+m[4]);}out.push(...original.slice(cursor));return {body:Buffer.from(out.join('\n')+'\n'),hunks};}
const map=JSON.parse(fs.readFileSync(HERE+'/MAPPING.json')),n=JSON.parse(fs.readFileSync(HERE+'/UPDATE_NATIVE.json')),oldKeys={};
a.equal(n.diffs.length,2);a.equal(n.order,'batch_then_stream_root');
const changed=[];
for(let i=0;i<2;i++){
 const row=map.mappings[i],d=n.diffs[i];a.equal(d.result.exit_code,1);
 const before=fs.readFileSync(row.physical_copy),after=fs.readFileSync(row.original);a.deepEqual(key(before),{bytes:row.original_full_key.bytes,sha256:row.original_full_key.sha256});
 const derived=transform(before,d.result.output);a.ok(derived.body.equals(after));oldKeys[row.original]=row.original_full_key;
 changed.push({path:row.original,before:key(before),after:key(after),actual_full_diff_reconstruction:true,hunks:derived.hunks});
}
const life=ROOT+'/docs/papers211_215_sequence/qa/p211_lifecycle_root01';const ledger=JSON.parse(fs.readFileSync(life+'/LIFECYCLE_INPUTS.json')).files;
for(const [q,k] of Object.entries(oldKeys))a.deepEqual(ledger[q],k);
const decision=JSON.parse(fs.readFileSync(life+'/CLOSING_RESULT.json'));a.equal(decision.paper_complete,true);a.equal(decision.batch_complete,false);
a.equal(key(fs.readFileSync(life+'/SHA256SUMS')).sha256,'970f1d7d918b8a12f6411178d55b7681f8eaff549ffd45f7697e0d15c4cc5b23');
const result={status:'PASS_COMPLETION_INDEX_ONLY_UPDATE_AND_PHYSICAL_OLD_KEY_MAP',changed,old_lifecycle_read_keys_exactly_mapped:2,retained:2,completed:1,open_seats:3,closed_attempts:43,paper_complete:'P211',batch_complete:false,new_science:0,new_builds:0,new_views:0,new_git:0};
fs.writeFileSync(HERE+'/UPDATE_RESULT.json',JSON.stringify(result,null,2)+'\n',{flag:'wx'});
const names=fs.readdirSync(HERE).sort();a.ok(!names.includes('SHA256SUMS'));
const b=Buffer.from(names.map(n=>{a.ok(fs.lstatSync(HERE+'/'+n).isFile());return key(fs.readFileSync(HERE+'/'+n)).sha256+'  '+n+'\n';}).join(''));fs.writeFileSync(HERE+'/SHA256SUMS',b,{flag:'wx'});
console.log(JSON.stringify({...result,payloads:names.length,seal:key(b)}));
