'use strict';
// Exact documentary bytes, transcript slices, and literal boundaries only.
const fs=require('fs'),crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics/';
const own='docs/papers211_215_sequence/qa/private_checkpoint_d01_cancellation_audit_delta01/';
const prep='docs/papers211_215_sequence/qa/private_checkpoint_d01_cancellation_delta01/';
const old='docs/papers211_215_sequence/qa/private_checkpoint_d01_preparation01/';
let checks=0;const need=(v,m)=>{checks++;if(!v)throw Error(m);};
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const json=p=>JSON.parse(fs.readFileSync(root+p,'utf8'));
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,s[k].toString()]));
const b=json(own+'INPUT_BEFORE_NATIVE.json'),a=json(own+'INPUT_AFTER_NATIVE.json');
need(b.response.exit_code===0&&a.response.exit_code===0,'Input native exits');
const before=JSON.parse(b.response.output),after=JSON.parse(a.response.output);
need(JSON.stringify(before)===JSON.stringify(after),'Complete input endpoints');
const rows=[...before.author_inputs,...before.historical_inputs],cache=new Map();
need(rows.length===19&&new Set(rows.map(r=>r.path)).size===19,'Nineteen distinct inputs');
for(const k of rows){
 need(k.path.startsWith('docs/')&&k.path.split('/').every(x=>x&&x!=='.'&&x!=='..'),'Fixed doc path');
 const s=fs.lstatSync(root+k.path,{bigint:true});
 need(s.isFile()&&!s.isSymbolicLink()&&JSON.stringify(meta(s))===JSON.stringify(k.metadata),'Pre metadata '+k.path);
 const fd=fs.openSync(root+k.path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  need(JSON.stringify(meta(fs.fstatSync(fd,{bigint:true})))===JSON.stringify(k.metadata),'Opened metadata');
  const body=fs.readFileSync(fd);
  need(body.length===k.bytes&&hash(body)===k.sha256,'Whole byte key '+k.path);
  need([fs.fstatSync(fd,{bigint:true}),fs.lstatSync(root+k.path,{bigint:true})]
   .every(x=>JSON.stringify(meta(x))===JSON.stringify(k.metadata)),'Read endpoints '+k.path);
  need(Buffer.from(body.toString('utf8')).equals(body),'Lossless UTF8');
  cache.set(k.path,body);
 }finally{fs.closeSync(fd);}
}
const text=p=>cache.get(p).toString('utf8');
const source=text(prep+'launch.py'),oldSource=text(old+'launch.py');
need(source.split('\n').length-1===347&&oldSource.split('\n').length-1===327,'Source line counts');
const cut='\ndef capture(environment, directory_fd):\n',tail='\ndef main():\n';
need(source.indexOf(cut)>0&&oldSource.indexOf(cut)>0,'Literal capture boundaries');
need(source.slice(0,source.indexOf(cut))===oldSource.slice(0,oldSource.indexOf(cut)).replace(
"SELF = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_d01_preparation01/launch.py'",
"SELF = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_d01_cancellation_delta01/launch.py'"),'Only SELF before capture');
need(source.slice(source.indexOf(tail))===oldSource.slice(oldSource.indexOf(tail)),'Complete main/tail identical');
need(source.split('subprocess.Popen(').length-1===1,'One literal Popen');
need(source.split('origin = time.monotonic()').length-1===1,'One literal origin assignment');
need(source.split('phase_index = 0').length-1===1,'One cursor initialization');
need(source.split('        handle_remaining()\n').length-1===2,'Two shared handler calls');
const diff=json(own+'DIFF_NATIVE.json'),patch=cache.get(prep+'EXACT_DELTA.patch');
need(diff.response.exit_code===1,'Diff expected exit one');
need(Buffer.from(diff.response.output).equals(patch),'Actual independent diff equals author patch raw');
need(fs.readFileSync(root+own+'INDEPENDENT_DELTA.patch').equals(patch),'Raw diff attachment exact');
need((patch.toString('utf8').match(/^@@ /gm)||[]).length===4,'Four diff hunks');
const native=JSON.parse(text(prep+'NATIVE_READS.json'));
const nr=native.all_preparation_workspace_native_records;
const cr=JSON.parse(text(prep+'CLOSING_NATIVE.json')).records;
need(nr.length===19&&cr.length===8,'Complete author record counts');
need(nr[16].result.exit_code===1&&Buffer.from(nr[16].result.output).equals(patch),'Author final actual diff exact');
need(Buffer.from(nr[2].result.output+nr[3].result.output).equals(cache.get(old+'launch.py')),'Complete old source native reconstruction');
need(Buffer.from(nr[15].result.output).equals(cache.get(prep+'launch.py')),'Complete final source native exact');
const draft=Buffer.from(nr[11].result.output+nr[12].result.output);
need(draft.length===18241&&hash(draft)==='a462ea8b4ab9c4bc3b271eb3dc21b75af4b81bfc8c4f9aeda7c0ac4cfda1ff6e'
 &&draft.toString('utf8').split('\n').length-1===345,'Distinct retained draft original');
need(!draft.equals(cache.get(prep+'launch.py')),'Draft not final');
const verified=[],unclaimed=[];
function record(label,r,reason){
 need(r.request&&r.result&&typeof r.request.cmd==='string'&&typeof r.result.output==='string','Actual record shape '+label);
 if(reason){unclaimed.push({label,reason,request:r.request});return;}
 const m=/^sed -n '(\d+),(\d+)p' (docs\/[A-Za-z0-9_./-]+)$/.exec(r.request.cmd);
 if(!m||!cache.has(m[3])){unclaimed.push({label,reason:'Not a single pinned sed; not executed or claimed as original-slice equality',request:r.request});return;}
 const lines=text(m[3]).match(/[^\n]*\n|[^\n]+$/g)||[],expected=lines.slice(Number(m[1])-1,Number(m[2])).join('');
 need(r.result.exit_code===0&&r.result.output===expected,'Exact native original slice '+label);
 verified.push({label,path:m[3],first:Number(m[1]),last:Number(m[2]),bytes:Buffer.byteLength(expected),sha256:hash(Buffer.from(expected))});
}
nr.forEach((r,i)=>record('author/native/'+i,r,i>=10&&i<=14?'Explicit pre-refinement 345-line draft evidence; not final source/diff':null));
cr.forEach((r,i)=>record('author/closing/'+i,r,i===1?'Explicit earlier handoff wording; final is record 7':null));
const rr=json(own+'READS_NATIVE.json').records;
rr.forEach((r,i)=>record('reviewer/'+i,{request:r.request,result:r.response},i<5?'Orientation only; not frozen source input':null));
for(const [i,file,start,end] of [[19,'NATIVE_READS.json',0,4],[20,'NATIVE_READS.json',4,11],[21,'NATIVE_READS.json',11,15],[22,'NATIVE_READS.json',15,19],[23,'CLOSING_NATIVE.json',0,8]]){
 const r=rr[i],x=JSON.parse(r.response.output),original=file==='NATIVE_READS.json'?nr:cr;
 need(r.response.exit_code===0&&x.whole_sha256===hash(cache.get(prep+file))
  &&x.range_start_inclusive===start&&x.range_end_exclusive===end
  &&JSON.stringify(x.records)===JSON.stringify(original.slice(start,end)),'Exact whole-bound archival record group '+i);
}
need(rr[14].response.exit_code===1&&rr[14].response.output.includes('Expected actual records'),'Preserved own schema-adapter failure');
const oldFind=JSON.parse(text('docs/papers211_215_sequence/qa/private_checkpoint_d01_source_audit01/FINDINGS.json'));
need(oldFind.findings.length===1&&oldFind.findings[0].status==='open','Old independent finding unchanged/open');
process.stdout.write(JSON.stringify({status:'DOCUMENTARY_DELTA_CHECKS_PASS_NOT_OPERATION',
checks,complete_input_keys:rows.length,identical_input_endpoints:true,
raw_diff_bytes:patch.length,raw_diff_sha256:hash(patch),four_hunks:true,
unchanged_prefix_except_self:true,unchanged_main_and_entry:true,
retained_draft:{lines:345,bytes:draft.length,sha256:hash(draft),final:false},
final_source:{lines:347,bytes:cache.get(prep+'launch.py').length,sha256:hash(cache.get(prep+'launch.py'))},
exact_sed_outputs:verified.length,verified_slices:verified,unclaimed_records:unclaimed,
author_records_all_read:27,old_finding_still_open:true,submitted_source_executed:false},null,2)+'\n');
