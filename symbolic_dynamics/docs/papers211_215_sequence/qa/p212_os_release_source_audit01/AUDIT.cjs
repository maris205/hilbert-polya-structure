// SOURCE-DATA ONLY: fixed documentary inputs; never import or execute proposals.
// Independent audit by /root/p212_eight_file_source_independent_audit.
'use strict';
const fs=require('node:fs'),crypto=require('node:crypto');
const B='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/';
const P={
 old_reader:'p212_three_leaf_preparation01/three_leaves.proposed.mjs.txt',
 old_request:'p212_three_leaf_preparation01/REQUEST.disabled.json',
 old_entry:'p212_three_leaf_capture_preparation01/ENTRY.proposed.mjs.txt',
 old_capture:'p212_three_leaf_capture_preparation01/capture.proposed.sh.txt',
 old_operation:'p212_three_leaf_capture_preparation01/OPERATION_REQUEST.proposed.json',
 old_reception:'p212_three_leaf_root01/SOURCE_RECEPTION.md',
 old_native:'p212_three_leaf_root01/SOURCE_CHECK_NATIVE.json',
 reader:'p212_package_provenance_preparation01/os_release.proposed.mjs.txt',
 request:'p212_package_provenance_preparation01/REQUEST.disabled.json',
 entry:'p212_package_provenance_preparation01/ENTRY.proposed.mjs.txt',
 capture:'p212_package_provenance_preparation01/capture.proposed.sh.txt',
 operation:'p212_package_provenance_preparation01/OPERATION_REQUEST.proposed.json',
 handoff:'p212_package_provenance_preparation01/HANDOFF.md'
};
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' ');
const report={schema:'p212-os-release-source-data-audit-v1',status:'RUNNING',checks:0,inputs:[],deltas:[],source_execution:false,host_or_future_path_queries:false};
const need=(v,m)=>{report.checks++;if(!v)throw Error(m);};
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
const stable=v=>JSON.stringify(v,(_,x)=>x&&typeof x==='object'&&!Array.isArray(x)?Object.fromEntries(Object.keys(x).sort().map(k=>[k,x[k]])):x);
const same=(a,b,m)=>need(stable(a)===stable(b),m);
const fields=s=>Object.fromEntries(F.map(k=>{need(typeof s[k]==='bigint','actual bigint '+k);return[k,s[k].toString()];}));
function read(role,phase){
 const path=B+P[role],r={role,phase,path,lstat_before:null,fstat_before:null,fstat_after:null,lstat_after:null,reads:[],eof:false,close_succeeded:false,content:null};report.inputs.push(r);
 let fd=null;const chunks=[];
 try{
  const s=fs.lstatSync(path,{bigint:true});r.lstat_before=fields(s);
  need(s.isFile()&&!s.isSymbolicLink()&&s.size>=0n&&s.size<=1048576n,'bounded physical documentary source');
  fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);r.fstat_before=fields(fs.fstatSync(fd,{bigint:true}));same(r.lstat_before,r.fstat_before,'four-key before');
  const block=Buffer.alloc(65536);let total=0;
  for(;;){const wanted=Math.min(block.length,1048577-total);need(wanted>0,'documentary limit');const n=fs.readSync(fd,block,0,wanted,null);r.reads.push({requested:wanted,returned:n});need(Number.isSafeInteger(n)&&n>=0&&n<=wanted,'actual read count');if(n===0){r.eof=true;break;}chunks.push(Buffer.from(block.subarray(0,n)));total+=n;need(total<=1048576,'documentary overflow');}
  r.fstat_after=fields(fs.fstatSync(fd,{bigint:true}));r.lstat_after=fields(fs.lstatSync(path,{bigint:true}));same(r.fstat_before,r.fstat_after,'fd stable');same(r.lstat_before,r.lstat_after,'leaf stable');
  const b=Buffer.concat(chunks);need(BigInt(b.length)===s.size&&r.eof,'full size actual zero EOF');r.content=pin(b);return b;
 }catch(e){r.error={name:e.name,code:e.code??null,message:e.message};throw e;}
 finally{if(fd!==null){fs.closeSync(fd);r.close_succeeded=true;}}
}
function text(b){const s=b.toString('utf8');need(Buffer.from(s,'utf8').equals(b),'reversible full UTF8');return s;}
function once(b,oldText,newText,label,count=1){
 const old=Buffer.from(oldText,'utf8'),replacement=Buffer.from(newText,'utf8');let pos=0,n=0;const chunks=[],positions=[];
 for(;;){const found=b.indexOf(old,pos);if(found<0){chunks.push(b.subarray(pos));break;}positions.push(found);chunks.push(b.subarray(pos,found),replacement);pos=found+old.length;n++;}
 need(n===count,label+' exact occurrence count');report.deltas.push({label,kind:'literal-byte-replacement',old_utf8:oldText,new_utf8:newText,occurrences:n,positions_in_step_input:positions,step_input:pin(b)});const out=Buffer.concat(chunks);report.deltas.at(-1).step_output=pin(out);return out;
}
try{
 const raw={},before={};for(const role of Object.keys(P)){raw[role]=read(role,'before');before[role]=report.inputs.at(-1);}
 const oldEntries="const ENTRIES=[\n {id:'INTERPRETER_LEAF',path:'/lib64/ld-linux-x86-64.so.2',role:'loader_alias_or_body',optional:false,max_regular_bytes:16777216,max_link_bytes:4096},\n {id:'TINFO_LEAF',path:'/usr/lib/x86_64-linux-gnu/libtinfo.so.6',role:'needed_alias_or_body',optional:false,max_regular_bytes:16777216,max_link_bytes:4096},\n {id:'KPATHSEA_LEAF',path:'/usr/lib/x86_64-linux-gnu/libkpathsea.so.6',role:'needed_alias_or_body',optional:false,max_regular_bytes:16777216,max_link_bytes:4096}\n];";
 const newEntries="const ENTRIES=[\n {id:'OS_RELEASE',path:'/etc/os-release',role:'distributor_identity_alias_or_body',optional:false,max_regular_bytes:65536,max_link_bytes:4096}\n];";
 let expected=once(raw.old_reader,oldEntries,newEntries,'reader sole exact ENTRIES');
 expected=once(expected,'total_regular_byte_limit:50331648','total_regular_byte_limit:65536','reader total regular bound');
 expected=once(expected,'total_link_byte_limit:12288','total_link_byte_limit:4096','reader total link bound');
 need(expected.equals(raw.reader),'ALL other reader bytes identical');
 expected=once(raw.old_entry,'p212_three_leaf_binding01','p212_os_release_binding01','entry only fixed binding namespace');need(expected.equals(raw.entry),'ALL other entry bytes identical');
 expected=once(raw.old_capture,'p212_three_leaf_raw01','p212_os_release_raw01','capture only raw namespace',2);
 expected=once(expected,'p212_three_leaf_enabled01','p212_os_release_enabled01','capture only enabled namespace');need(expected.equals(raw.capture),'ALL other capture bytes identical');
 const disabled=' const SOURCE_ENABLED=false;',enabled=' const SOURCE_ENABLED=true;';
 const future=once(raw.reader,disabled,enabled,'FUTURE DATA ONLY sole activation delta');
 report.future_enabled_pin_only={...pin(future),materialized:false,queried:false,authorized:false};
 const one=[{id:'OS_RELEASE',path:'/etc/os-release',role:'distributor_identity_alias_or_body',optional:false,max_regular_bytes:65536,max_link_bytes:4096}];
 const oldRequest=JSON.parse(text(raw.old_request)),request=JSON.parse(text(raw.request));
 const expectedRequest={...oldRequest,entries:one,total_regular_byte_limit:65536,total_link_byte_limit:4096};same(request,expectedRequest,'WHOLE exact disabled request');
 need(request.enabled===false&&request.permission_receipt===null,'disabled null grant');
 report.deltas.push({label:'disabled request full JSON value delta',kind:'exact-JSON-values',changes:[{path:'entries',old:oldRequest.entries,new:one},{path:'total_regular_byte_limit',old:oldRequest.total_regular_byte_limit,new:65536},{path:'total_link_byte_limit',old:oldRequest.total_link_byte_limit,new:4096}],all_other_values_identical:true,formatting_not_raw_compared:true});
 const oldOp=JSON.parse(text(raw.old_operation)),op=JSON.parse(text(raw.operation)),expectedOp=structuredClone(oldOp),opChanges=[];
 function change(path,value){const parts=path.split('.');let at=expectedOp;for(const k of parts.slice(0,-1))at=at[k];const k=parts.at(-1);opChanges.push({path,old_present:Object.hasOwn(at,k),old:at[k]??null,new:value});at[k]=value;}
 const local='docs/papers211_215_sequence/qa/p212_package_provenance_preparation01/';
 change('source_copies.0.source',local+'os_release.proposed.mjs.txt');
 change('source_copies.0.required_source_delta',{old:disabled,new:enabled,occurrences:1,all_other_bytes_identical:true});
 change('source_copies.0.destination',B+'p212_os_release_enabled01/three_leaves.mjs');
 change('source_copies.1.source',local+'ENTRY.proposed.mjs.txt');
 change('source_copies.1.destination',B+'p212_os_release_enabled01/ENTRY.mjs');
 change('binding.template',local+'REQUEST.disabled.json');
 change('binding.destination',B+'p212_os_release_binding01/REQUEST.json');
 change('capture_directory.path',B+'p212_os_release_raw01');
 change('proposed_native_request.arguments.cmd',text(raw.capture));
 same(op,expectedOp,'WHOLE operation only nine explicit value changes');
 need(Buffer.from(op.proposed_native_request.arguments.cmd,'utf8').equals(raw.capture),'WHOLE capture command RAW equality');
 need(Buffer.from(oldOp.proposed_native_request.arguments.cmd,'utf8').equals(raw.old_capture),'WHOLE baseline capture command RAW equality');
 report.deltas.push({label:'operation whole JSON value delta',kind:'exact-JSON-values',changes:opChanges,all_other_values_identical:true,formatting_not_raw_compared:true});
 const oldNative=JSON.parse(text(raw.old_native));need(oldNative.exit_code===0&&!oldNative.session_id,'actual old source reception exit zero');
 same(JSON.parse(oldNative.output),{status:'ROOT_SOURCE_ACCEPTED_ONLY',input_occurrences:16,enabled_exact_single_constant:true,whole_native_capture_equal:true},'whole old root summary (not full outside keys)');
 need(text(raw.old_reception).includes('Three-leaf reader and capture source accepted'),'literal prior root source receipt');
 for(const role of Object.keys(P)){
  const again=read(role,'after');need(again.equals(raw[role]),'WHOLE before/after input RAW equality '+role);
  const after=report.inputs.at(-1);same(before[role].lstat_before,after.lstat_after,'ALL ten fields across audit '+role);same(before[role].content,after.content,'full source pins across audit '+role);
 }
 report.status='PASS_BOUNDED_OS_RELEASE_SOURCE_ONLY';report.current_findings={reader:0,entry:0,capture:0,request:0};
 report.input_files=Object.keys(P).length;report.complete_read_keys=report.inputs.length;
 report.holds=['MATERIALIZATION','BINDING','NEW_CONSUMED_ONE_USE_GRANT','OPERATION','OS_IDENTITY_DATA','PACKAGE_MEMBER_SOURCE_CORRESPONDENCE','HOLD_EXTERNAL'];
}catch(e){report.status='FAIL_PRESERVED';report.error={name:e.name,code:e.code??null,message:e.message};process.exitCode=1;}
process.stdout.write(JSON.stringify(report,null,2)+'\n');
