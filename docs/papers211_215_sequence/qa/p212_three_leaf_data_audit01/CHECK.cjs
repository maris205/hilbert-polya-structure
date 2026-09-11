'use strict';
// Fixed existing evidence only. Never import received source or open DATA paths.
const fs=require('node:fs'), crypto=require('node:crypto'), assert=require('node:assert/strict');
const base='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/';
const names=[
 'p212_three_leaf_capture_preparation01/three_leaves.enabled.proposed.mjs.txt',
 'p212_three_leaf_capture_preparation01/ENTRY.proposed.mjs.txt',
 'p212_three_leaf_enabled01/three_leaves.mjs',
 'p212_three_leaf_enabled01/ENTRY.mjs',
 'p212_three_leaf_binding01/REQUEST.json',
 'p212_three_leaf_root01/CONDITIONAL_GRANT.md',
 'p212_three_leaf_capture_preparation01/OPERATION_REQUEST.proposed.json',
 'p212_three_leaf_capture_preparation01/capture.proposed.sh.txt',
 'p212_three_leaf_preparation01/REQUEST.disabled.json',
 'p212_three_leaf_root01/SOURCE_RECEPTION.md',
 'p212_three_leaf_root01/SOURCE_CHECK_NATIVE.json',
 'p212_three_leaf_root01/PREFLIGHT.cjs',
 'p212_three_leaf_root01/PREFLIGHT_NATIVE.json',
 'p212_three_leaf_root01/CONSUMPTION.md',
 'p212_three_leaf_root01/ACTUAL_NATIVE.json',
 'p212_three_leaf_root01/CLOSED_RAW_NATIVE.json',
 'p212_three_leaf_raw01/stdout.json',
 'p212_three_leaf_raw01/stderr.raw',
 'p212_three_leaf_preparation01/three_leaves.proposed.mjs.txt',
 'p212_three_leaf_source_audit01/reader/REVIEW.md',
 'p212_three_leaf_source_audit01/capture/REVIEW.md'
];
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' ');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pin=b=>({bytes:b.length,sha256:sha(b)}), eq=(a,b)=>assert.deepStrictEqual(a,b);
const keys=(x,k)=>eq(Object.keys(x).sort(),k.slice().sort());
const stat=s=>Object.fromEntries(F.map(k=>{assert.equal(typeof s[k],'bigint');return[k,String(s[k])];}));
function validStat(s,kind){keys(s,F);for(const k of F)assert.match(s[k],k.endsWith('Ns')?/^-?(0|[1-9][0-9]*)$/:/^(0|[1-9][0-9]*)$/);if(kind!==undefined)assert.equal(BigInt(s.mode)&0o170000n,kind);}
const current=[],bodies=[];
function readFixed(i){
 const path=base+names[i],a=fs.lstatSync(path,{bigint:true});
 assert(a.isFile()&&!a.isSymbolicLink()&&a.nlink===1n&&a.uid===0n&&a.gid===0n&&a.size>=0n&&a.size<=1048576n);
 const item={path,begin:stat(a),fd_before:null,fd_after:null,end:null,reads:[],eof:false,close_succeeded:false,bytes:0,sha256:null};current.push(item);
 let fd=null;const chunks=[],buf=Buffer.alloc(65536);
 try{fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);item.fd_before=stat(fs.fstatSync(fd,{bigint:true}));eq(item.fd_before,item.begin);
  for(;;){const requested=Math.min(buf.length,1048577-item.bytes),returned=fs.readSync(fd,buf,0,requested,null);item.reads.push({requested,returned});assert(Number.isSafeInteger(returned)&&returned>=0&&returned<=requested);if(returned===0){item.eof=true;break;}chunks.push(Buffer.from(buf.subarray(0,returned)));item.bytes+=returned;assert(item.bytes<=1048576);}
  item.fd_after=stat(fs.fstatSync(fd,{bigint:true}));eq(item.fd_after,item.begin);
 }finally{if(fd!==null){fs.closeSync(fd);item.close_succeeded=true;}}
 item.end=stat(fs.lstatSync(path,{bigint:true}));eq(item.end,item.begin);assert.equal(BigInt(item.bytes),a.size);const b=Buffer.concat(chunks);item.sha256=sha(b);bodies.push(b);return b;
}
function json(i){const text=bodies[i].toString('utf8');assert(Buffer.from(text,'utf8').equals(bodies[i]));return JSON.parse(text);}
function native(x,chunk){keys(x,['chunk_id','wall_time_seconds','exit_code','original_token_count','output']);assert.equal(x.chunk_id,chunk);assert.equal(x.exit_code,0);assert(typeof x.output==='string'&&Number.isFinite(x.wall_time_seconds)&&x.wall_time_seconds>=0&&Number.isSafeInteger(x.original_token_count)&&x.original_token_count>=0);}
function prior(k,i,views){assert.equal(k.path,base+names[i]);for(const v of views){validStat(k[v],0o100000n);eq(k[v],current[i].begin);}assert.equal(k.eof,true);assert.equal(k.close_succeeded,true);assert.equal(k.bytes,bodies[i].length);assert.equal(k.sha256,sha(bodies[i]));}
function bytes(hex,p){assert(typeof hex==='string'&&/^(?:[0-9a-f]{2})*$/.test(hex));const b=Buffer.from(hex,'hex');keys(p,['bytes','sha256']);eq(pin(b),p);return b;}
function reads(list,total,limit){assert(Array.isArray(list)&&list.length>0);let got=0;for(let j=0;j<list.length;j++){const r=list[j];keys(r,['requested','returned']);assert.equal(r.requested,Math.min(65536,limit-got+1));assert(Number.isSafeInteger(r.returned)&&r.returned>=0&&r.returned<=r.requested);if(j===list.length-1)assert.equal(r.returned,0);else assert(r.returned>0);got+=r.returned;assert(got<=limit);}assert.equal(got,total);}
try{
 for(let i=0;i<names.length;i++)readFixed(i);
 const expectedPins={0:[7201,'2975cbe6f2ada2562a219846d17acc24b0488684d253ba0013b18d7232a1904a'],1:[6173,'17ce91d1eba2ea2ba0e8ef54394985097d4cbc9d9fc632565e360169a9312f94'],6:[3861,'2fb17f155c467849bbacc3debd67b5160d5305864ec8b1fed90e738a0e1f6b74'],7:[536,'651734b6f69d91274db71c8390c4f5e927c39bd4a9eb798272d7b0d39bb31090'],8:[820,'37156890d64d7b7e100b258e6c1f6b8f506b33ee64cbfe9bd43ec657bb051356'],16:[7599,'3072a7bdd483048cbd5105359336e37a543283a28fc4c32835a78c6582dcf682'],17:[0,'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'],18:[7202,'a9f95d7d136890ae46199a2689d699441302f91500998572d56e3d12b2165140'],19:[5688,'a0b2de470c5d33644dd617b1307bad5b727c62d5fd883d0893320be848e503f1'],20:[5801,'e6ad970ca58f082e71d73d66d96b9c29b9a1d72589134552c525120b7d3be6f6']};
 for(const [i,p] of Object.entries(expectedPins))eq([bodies[i].length,sha(bodies[i])],p);
 assert(bodies[0].equals(bodies[2])&&bodies[1].equals(bodies[3]));const disabled=bodies[18].toString('utf8');assert.equal(disabled.split('const SOURCE_ENABLED=false;').length,2);assert(Buffer.from(disabled.replace('const SOURCE_ENABLED=false;','const SOURCE_ENABLED=true;')).equals(bodies[0]));
 const source=json(10);native(source,'4c4c12');eq(JSON.parse(source.output),{status:'ROOT_SOURCE_ACCEPTED_ONLY',input_occurrences:16,enabled_exact_single_constant:true,whole_native_capture_equal:true});
 const request=json(4),template=json(8),proposal=json(6),actual=json(14),preNative=json(12),closedNative=json(15);
 assert.equal(request.enabled,true);assert.equal(request.status,'ROOT_BOUND_THREE_LEXICAL_LEAVES_ONLY');eq({...request,enabled:false,status:template.status,permission_receipt:null},template);eq(request.permission_receipt,{path:base+names[5],pin:pin(bodies[5])});
 keys(actual,['request','result']);native(actual.result,'ba28b7');eq(actual.result.output,'');assert.equal(actual.result.original_token_count,0);eq(actual.request,proposal.proposed_native_request.arguments);assert(Buffer.from(actual.request.cmd,'utf8').equals(bodies[7]));
 native(preNative,'c2b6c0');const pre=JSON.parse(preNative.output);keys(pre,['status','keys','directories','request']);assert.equal(pre.status,'PASS_SOURCE_COPIES_BOUND_REQUEST_FRESH_DIRECTORIES');eq(pre.request,request);assert.equal(pre.keys.length,9);for(let i=0;i<9;i++)prior(pre.keys[i],i,['begin','fd_before','fd_after','end']);
 const dirs=['p212_three_leaf_enabled01','p212_three_leaf_binding01','p212_three_leaf_raw01'],entries=[['ENTRY.mjs','three_leaves.mjs'],['REQUEST.json'],[]];assert.equal(pre.directories.length,3);for(let i=0;i<3;i++){const d=pre.directories[i];keys(d,['path','begin','end','entries']);assert.equal(d.path,base+dirs[i]);validStat(d.begin,0o040000n);eq(d.begin,d.end);assert.equal(BigInt(d.begin.mode)&0o7777n,0o700n);assert.equal(d.begin.uid,'0');assert.equal(d.begin.gid,'0');eq(d.entries,entries[i]);}
 native(closedNative,'259c82');const closed=JSON.parse(closedNative.output);keys(closed,['status','actual_chunk','inputs','captures']);assert.equal(closed.status,'CLOSED_RAW_AND_NINE_OUTSIDE_KEYS_ACCEPTED_DATA_PENDING');assert.equal(closed.actual_chunk,'ba28b7');assert.equal(closed.inputs.length,9);for(let i=0;i<9;i++)prior(closed.inputs[i],i,['begin','fd_before','end']);assert.equal(closed.captures.length,2);for(let j=0;j<2;j++){const k=closed.captures[j],i=16+j;assert.equal(k.path,'docs/papers211_215_sequence/qa/'+names[i]);prior({...k,path:base+names[i]},i,['begin','fd_before','end']);assert.equal(BigInt(current[i].begin.mode)&0o7777n,0o600n);}assert(current[16].begin.dev!==current[17].begin.dev||current[16].begin.ino!==current[17].begin.ino);
 const capture=json(16);assert(Buffer.from(JSON.stringify(capture)+'\n','utf8').equals(bodies[16]));
 keys(capture,['schema','status','request_input','reader_called','reader_returned','reader_result','entry_failure','operation_permission','installed_closure','referents_followed','package_queries']);assert.equal(capture.schema,'p212-three-leaf-captured-result-v1');assert.equal(capture.status,'THREE_LEXICAL_LEAVES_ROOT_RECEPTION_PENDING');assert.equal(capture.reader_called,true);assert.equal(capture.reader_returned,true);assert.equal(capture.entry_failure,null);for(const k of ['operation_permission','installed_closure','referents_followed','package_queries'])assert.equal(capture[k],false);
 const input=capture.request_input;keys(input,['path','byte_limit','lstat_before','fstat_before','fstat_after','lstat_after','bytes_read','reads','eof','close_succeeded','raw_hex','content','complete','error','close_error']);assert.equal(input.path,base+names[4]);assert.equal(input.byte_limit,65536);for(const k of ['lstat_before','fstat_before','fstat_after','lstat_after']){validStat(input[k],0o100000n);eq(input[k],current[4].begin);}assert(bytes(input.raw_hex,input.content).equals(bodies[4]));assert.equal(input.bytes_read,bodies[4].length);reads(input.reads,input.bytes_read,65536);for(const k of ['eof','close_succeeded','complete'])assert.equal(input[k],true);assert.equal(input.error,null);assert.equal(input.close_error,null);
 const result=capture.reader_result;keys(result,['schema','status','request','rows','accepted_regular_bytes','accepted_link_bytes','failure','referents_followed','terminal_selection','actual_ancestor_scan','source_acceptance','operation_permission','installed_closure']);assert.equal(result.schema,'p212-three-lexical-leaves-v1');assert.equal(result.status,capture.status);eq(result.request,request);assert.equal(result.failure,null);assert.equal(result.terminal_selection,null);for(const k of ['referents_followed','actual_ancestor_scan','source_acceptance','operation_permission','installed_closure'])assert.equal(result[k],false);
 assert.equal(result.rows.length,3);assert.equal(request.entries.length,3);const targets=['/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2','libtinfo.so.6.3','libkpathsea.so.6.3.4'],summaries=[];let linkTotal=0;
 for(let i=0;i<3;i++){const row=result.rows[i],entry=request.entries[i];keys(row,['id','path','role','kind','lstat_before','lstat_after','regular','link','complete','error']);for(const k of ['id','path','role'])assert.equal(row[k],entry[k]);assert.equal(row.kind,'symlink');assert.equal(row.regular,null);validStat(row.lstat_before,0o120000n);eq(row.lstat_before,row.lstat_after);assert.equal(row.complete,true);assert.equal(row.error,null);
  const link=row.link;keys(link,['readlink_returned','raw_hex','content','target_utf8','point_complete','same_fd_attested']);assert.equal(link.readlink_returned,true);assert.equal(link.point_complete,true);assert.equal(link.same_fd_attested,false);const b=bytes(link.raw_hex,link.content);assert(b.length>0&&b.length<=entry.max_link_bytes&&!b.includes(0));assert.equal(BigInt(b.length),BigInt(row.lstat_before.size));assert.equal(link.target_utf8,targets[i]);assert(Buffer.from(link.target_utf8,'utf8').equals(b));linkTotal+=b.length;
  summaries.push({id:row.id,origin_lexical_leaf:row.path,kind:row.kind,link_content:link.content,target_utf8:link.target_utf8,scope:'COMPLETE_LINK_POINT_DATA_ONLY',same_fd_attested:false,terminal_body_received:false});
 }
 assert.equal(linkTotal,77);assert(linkTotal<=request.total_link_byte_limit);assert.equal(result.accepted_link_bytes,linkTotal);assert.equal(result.accepted_regular_bytes,0);
 console.log(JSON.stringify({status:'ACCEPT_THREE_LEAF_POINT_OBSERVATION_DATA_ONLY',findings:{critical:0,major:0,minor:0,open:0},actual_native:actual.result,ordinary_json_utf8_plus_one_lf_exact:true,source_copies_and_single_enabled_delta_exact:true,nine_outside_full_keys_match_preflight_and_current:true,closed_root_exposes_three_metadata_views_only:true,current_reader_exposes_four_metadata_views:true,bound_request_full_key_and_hex_bytes_match:true,stdout:pin(bodies[16]),stderr:pin(bodies[17]),observations:summaries,accepted_link_bytes:77,accepted_regular_bytes:0,failure:null,candidate_path_operations_by_auditor:0,received_source_execution_or_import:false,referents_followed:false,terminal_selection:null,operation_permission:false,installed_closure:false,bootstrap_boundary:'Existing ordinary Node/filesystem/product and trusted ancestors; no runtime observer or historical race freedom claim',current_documents:current}));
}catch(e){console.log(JSON.stringify({status:'FAIL_DATA_RECEPTION_PRESERVE_ORIGINALS',error:{name:e.name,message:e.message,stack:e.stack},current_documents:current,source_execution:false,candidate_path_operations:0}));process.exitCode=1;}
