'use strict';
// Documentary change-sensitive verification. No received source execution.
const fs=require('node:fs'),path=require('node:path'),a=require('node:assert/strict'),c=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',Q='docs/papers211_215_sequence/qa/';
const B=Q+'control_before_p212_dependency_source_received01/',S=Q+'p212_dependency_source_root01/';
let checks=0;const eq=(x,y,s)=>{checks++;a.deepEqual(x,y,s);},need=(x,s)=>{checks++;a.ok(x,s);};
const pin=b=>({bytes:b.length,sha256:c.createHash('sha256').update(b).digest('hex')});
function read(p){need(!p.startsWith('/')&&path.normalize(p)===p&&!p.split('/').includes('..'));const q=ROOT+'/'+p;need(fs.lstatSync(q).isFile());eq(fs.realpathSync(q),q);return fs.readFileSync(q);}
const json=p=>JSON.parse(read(p));
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const stat=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const stable=s=>Object.fromEntries(Object.entries(s).filter(([k])=>k!=='atimeNs'));
const mapping=json(B+'MAPPING.json'),native=json(B+'PREPARATION_NATIVE.json');
eq(native.result.exit_code,0);eq(Buffer.from(native.result.output),read(B+'MAPPING.json'));
eq(mapping.files.map(x=>x.original_path),['SYMBOLIC_DYNAMICS_STATE.md','docs/papers211_215_sequence/PIPELINE_STATE.md']);
for(const row of mapping.files){eq(pin(read(row.physical_copy_path)),row.original_pin);eq(row.original_pin,row.copy_pin);eq(stable(stat(fs.statSync(ROOT+'/'+row.physical_copy_path,{bigint:true}))),stable(row.copy_stat));}
const comparisons=json(B+'COPY_COMPARISONS_NATIVE.json');eq(comparisons.records.length,2);for(const r of comparisons.records){eq(r.result.exit_code,0);eq(r.result.output,'');need(!r.result.session_id);}
const edits=json(B+'ROOT_EDIT_SPEC.json'),oldState=read(B+'STATE.before.md').toString();
const expectedState=oldState.replace(edits.root_old_heading,edits.root_new_heading).replace(edits.root_old_current_line,edits.root_new_current_line+'\n\n'+edits.root_inserted_milestone);
eq(Buffer.from(expectedState),read('SYMBOLIC_DYNAMICS_STATE.md'),'exact intended root edit');
function applyRecordedDiff(old,raw){
 const lines=raw.match(/[^\n]*\n|[^\n]+$/g)||[],source=old.match(/[^\n]*\n|[^\n]+$/g)||[];
 need(lines[0].startsWith('--- '));need(lines[1].startsWith('+++ '));let i=2,cursor=0,out=[],hunks=0;
 while(i<lines.length){const m=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@\n$/.exec(lines[i++]);need(m,'strict actual hunk header');
  const start=Number(m[1])-1,oldCount=m[2]===undefined?1:Number(m[2]),newStart=Number(m[3])-1,newCount=m[4]===undefined?1:Number(m[4]);
  need(start>=cursor);out.push(...source.slice(cursor,start));cursor=start;eq(out.length,newStart);let oldUsed=0,newUsed=0;
  while(i<lines.length&&!lines[i].startsWith('@@ ')){
   const line=lines[i++],op=line[0],text=line.slice(1);need([' ','+','-'].includes(op),'literal full hunk line');
   if(op!=='+' ){eq(source[cursor++],text,'complete old/context bytes');oldUsed++;}
   if(op!=='-'){out.push(text);newUsed++;}
  }eq(oldUsed,oldCount);eq(newUsed,newCount);hunks++;
 }out.push(...source.slice(cursor));return{text:out.join(''),hunks};
}
const diffs=json(B+'ACTUAL_CONTROL_DIFFS_NATIVE.json');eq(diffs.records.length,2);const targets=[['PIPELINE.before.md','docs/papers211_215_sequence/PIPELINE_STATE.md',2],['STATE.before.md','SYMBOLIC_DYNAMICS_STATE.md',1]];
const current=[];
for(let i=0;i<2;i++){
 const r=diffs.records[i],spec=targets[i];eq(r.result.exit_code,1);need(!r.result.session_id);
 const d=applyRecordedDiff(read(B+spec[0]).toString(),r.result.output);eq(d.hunks,spec[2]);eq(Buffer.from(d.text),read(spec[1]),'whole actual delta reconstruction');current.push({path:spec[1],...pin(read(spec[1]))});
}
const batch=read('docs/papers211_215_sequence/PIPELINE_STATE.md').toString();
need(batch.includes('P211_COMPLETE_WARNING_RETAINED_P212_DEPENDENCY_SOURCE_ACCEPTED_OUTER_PENDING / TWO_RETAINED / ONE_COMPLETE / THREE_OPEN_SEATS'));
eq(batch.split('The [P212 finite dependency source plan and corrected driver]').length-1,1);
need(batch.includes('Counts remain2 retained/1 completed/3 open/43 closed'));need(batch.includes('does not grant any host operation.'));
const sourceSeal=read(S+'SHA256SUMS');eq(pin(sourceSeal).sha256,'ef25ddc3cfdbec6e47d24f655eb74e01d5c16fc91fe2445416502b0ac528bc09');
const payloads=sourceSeal.toString().slice(0,-1).split('\n').map(line=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);need(m);eq(pin(read(S+m[2])).sha256,m[1]);return m[2];});eq(payloads.length,16);eq(fs.readdirSync(ROOT+'/'+S).sort(),payloads.concat('SHA256SUMS').sort());
const source=json(S+'RESULT.json');eq(source.inputs.length,150);
for(const k of source.inputs){eq(pin(read(k.path)),{bytes:k.bytes,sha256:k.sha256});eq(stable(stat(fs.lstatSync(ROOT+'/'+k.path,{bigint:true}))),stable(k.lstat));eq(stable(stat(fs.statSync(ROOT+'/'+k.path,{bigint:true}))),stable(k.stat));}
const priorSeal=json(B+'SOURCE_ROOT_SEAL_CHECK_NATIVE.json');eq(priorSeal.result.exit_code,0);eq(priorSeal.result.output,payloads.map(x=>x+': OK\n').join(''));
const before=fs.readdirSync(ROOT+'/'+B).sort().map(name=>({path:B+name,...pin(read(B+name))}));
process.stdout.write(JSON.stringify({status:'PASS_TWO_DOCUMENTARY_CONTROLS_UPDATED_UNCHANGED_SOURCE_KEYS',checks,current_controls:current,physical_before_copies:mapping.files.map(x=>({path:x.physical_copy_path,pin:x.copy_pin})),source_root_payloads:16,unchanged_source_keys:150,pre_result_payloads:before,source_only:true,host_query:false,build:false,science:false,Git_write:false,external:'HOLD_EXTERNAL'},null,2)+'\n');
