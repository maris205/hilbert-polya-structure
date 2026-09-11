'use strict';
// Fixed DATA only. Reuses accepted three-leaf/three-terminal reception mechanics.
// Never import, execute, open or resolve a path obtained from captured DATA.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const base='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/';
const names=[
 'p212_package_provenance_preparation01/os_release.proposed.mjs.txt',
 'p212_package_provenance_preparation01/ENTRY.proposed.mjs.txt',
 'p212_os_release_enabled01/three_leaves.mjs',
 'p212_os_release_enabled01/ENTRY.mjs',
 'p212_os_release_binding01/REQUEST.json',
 'p212_os_release_root01/CONDITIONAL_GRANT.md',
 'p212_package_provenance_preparation01/OPERATION_REQUEST.proposed.json',
 'p212_package_provenance_preparation01/capture.proposed.sh.txt',
 'p212_package_provenance_preparation01/REQUEST.disabled.json',
 'p212_os_release_root01/SOURCE_RECEPTION.md',
 'p212_os_release_root01/SOURCE_REPLAY_NATIVE.json',
 'p212_os_release_root01/MATERIALIZATION_RECEPTION_NATIVE.json',
 'p212_os_release_root01/PREFLIGHT.cjs',
 'p212_os_release_root01/PREFLIGHT_NATIVE.json',
 'p212_os_release_root01/CONSUMPTION.md',
 'p212_os_release_root01/ACTUAL_NATIVE.json',
 'p212_os_release_root01/CLOSE_RAW.cjs',
 'p212_os_release_root01/CLOSED_RAW_NATIVE.json',
 'p212_os_release_raw01/stdout.json',
 'p212_os_release_raw01/stderr.raw',
 'p212_os_release_source_audit01/RESULT.json',
 'p212_three_leaf_data_audit01/CHECK.cjs',
 'p212_three_terminal_data_audit01/CHECK.cjs'
];
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' ');
const V=['begin','fd_before','fd_after','end'],W=['lstat_before','fstat_before','fstat_after','lstat_after'];
const eq=(a,b)=>assert.deepStrictEqual(a,b),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),pin=b=>({bytes:b.length,sha256:sha(b)});
const keys=(x,w)=>{assert(x!==null&&typeof x==='object'&&!Array.isArray(x));eq(Object.keys(x).sort(),w.slice().sort());};
const stat=s=>Object.fromEntries(F.map(k=>{assert.equal(typeof s[k],'bigint');return[k,String(s[k])];}));
function validStat(s,kind){keys(s,F);for(const k of F)assert.match(s[k],k.endsWith('Ns')?/^-?(0|[1-9][0-9]*)$/:/^(0|[1-9][0-9]*)$/);assert.equal(BigInt(s.mode)&0o170000n,kind);}
const current=[],bodies=[],directories=[];
function readFixed(i){
 const path=base+names[i],limit=1048576,a=fs.lstatSync(path,{bigint:true});
 assert(a.isFile()&&!a.isSymbolicLink()&&a.nlink===1n&&a.uid===0n&&a.gid===0n&&a.size>=0n&&a.size<=BigInt(limit));
 const item={path,begin:stat(a),fd_before:null,fd_after:null,end:null,reads:[],eof:false,close_succeeded:false,bytes:0,sha256:null};current.push(item);
 let fd=null;const chunks=[],block=Buffer.alloc(65536);
 try{fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);item.fd_before=stat(fs.fstatSync(fd,{bigint:true}));eq(item.fd_before,item.begin);
  for(;;){const requested=Math.min(block.length,limit-item.bytes+1),returned=fs.readSync(fd,block,0,requested,null);item.reads.push({requested,returned});assert(Number.isSafeInteger(returned)&&returned>=0&&returned<=requested);if(returned===0){item.eof=true;break;}chunks.push(Buffer.from(block.subarray(0,returned)));item.bytes+=returned;assert(item.bytes<=limit);}
  item.fd_after=stat(fs.fstatSync(fd,{bigint:true}));eq(item.fd_after,item.begin);
 }finally{if(fd!==null){fs.closeSync(fd);item.close_succeeded=true;}}
 item.end=stat(fs.lstatSync(path,{bigint:true}));eq(item.end,item.begin);assert.equal(BigInt(item.bytes),a.size);const b=Buffer.concat(chunks);item.sha256=sha(b);bodies.push(b);
}
function json(i){const s=bodies[i].toString('utf8');assert(Buffer.from(s,'utf8').equals(bodies[i]));return JSON.parse(s);}
function native(x,chunk){keys(x,['chunk_id','wall_time_seconds','exit_code','original_token_count','output']);assert.equal(x.chunk_id,chunk);assert.equal(x.exit_code,0);assert(typeof x.output==='string'&&Number.isFinite(x.wall_time_seconds)&&x.wall_time_seconds>=0&&Number.isSafeInteger(x.original_token_count)&&x.original_token_count>=0);}
function wrapped(i,chunk){const x=json(i);keys(x,['arguments','result']);native(x.result,chunk);return x;}
function prior(k,i){keys(k,['path',...V,'bytes','sha256','eof','close_succeeded']);assert.equal(k.path,base+names[i]);for(const v of V){validStat(k[v],0o100000n);eq(k[v],current[i].begin);}assert.equal(k.eof,true);assert.equal(k.close_succeeded,true);eq({bytes:k.bytes,sha256:k.sha256},pin(bodies[i]));}
function decodeHex(hex,p,limit){keys(p,['bytes','sha256']);assert(Number.isSafeInteger(p.bytes)&&p.bytes>=0&&p.bytes<=limit);assert(typeof p.sha256==='string'&&/^[0-9a-f]{64}$/.test(p.sha256));assert(typeof hex==='string'&&hex.length===2*p.bytes&&/^(?:[0-9a-f]{2})*$/.test(hex));const b=Buffer.from(hex,'hex');eq(pin(b),p);return b;}
function reads(list,total,limit){assert(Array.isArray(list)&&list.length>0);let got=0;for(let i=0;i<list.length;i++){const r=list[i];keys(r,['requested','returned']);assert.equal(r.requested,Math.min(65536,limit-got+1));assert(Number.isSafeInteger(r.returned)&&r.returned>=0&&r.returned<=r.requested);if(i===list.length-1)assert.equal(r.returned,0);else assert(r.returned>0);got+=r.returned;assert(got<=limit);}assert.equal(got,total);}
try{
 for(let i=0;i<names.length;i++)readFixed(i);
 const expected={
  0:[6871,'1c10daa164921da42a2e5a16e050f9024060bf0a41a880b7a5b2519ede6c3ab5'],
  1:[6173,'39a2855690c3a30f24d855775f04f9c3153381c35a6c9c26bd6eac639dbed29f'],
  2:[6870,'be8be3f84251ea2f87dcc9d0cb7621cb7f172ea416c24f23588b4d3d5f2669ef'],
  4:[734,'66beb0fb490e9dfc3937f358510f1d4554cbcf81dde7031a08bbc8c095e32d12'],
  5:[1301,'fc2a05d04202068607260df20fd7e424721e56e2d32aeb4c628753b412621acf'],
  6:[4022,'9a234978509897877089c057e742682da77a004f6359072d1238007a1ee5a200'],
  7:[536,'d7c325d290f75f672dc9e8121eb21283fae72353dee431d9ae633fb545bbc036'],
  8:[479,'b533cf7504157153bfeecf6d465bab29db738dc2391498e40479162ffeac66e1'],
  18:[4667,'b625162f978b20129579004c8185d659a61d41d254431fdaedaf75ececa0a009'],
  19:[0,'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'],
  20:[56987,'d9e91c1db1f4e65565f790c645053edebf82d787d115ed5b56d91e3d29cce638'],
  21:[13128,'7874ace4378f46e6933236c2be21d7f878a6076f3d0debedf9c91644870832ce'],
  22:[16907,'426b736be8c9eb00cf7982de4f1e5b39677bf3297553e75c3ef63a13956bab1d']
 };
 for(const [i,p] of Object.entries(expected))eq([bodies[i].length,sha(bodies[i])],p);
 const disabled=bodies[0].toString('utf8');assert.equal(disabled.split(' const SOURCE_ENABLED=false;').length,2);assert(Buffer.from(disabled.replace(' const SOURCE_ENABLED=false;',' const SOURCE_ENABLED=true;')).equals(bodies[2]));assert(bodies[1].equals(bodies[3]));
 // Explicit native-layout delta: source replay is direct; the four new calls are {arguments,result}.
 const sourceNative=json(10);native(sourceNative,'7fd4ac');assert(Buffer.from(sourceNative.output).equals(bodies[20]));const source=JSON.parse(sourceNative.output);
 assert.equal(source.status,'PASS_BOUNDED_OS_RELEASE_SOURCE_ONLY');assert.equal(source.source_execution,false);assert.equal(source.host_or_future_path_queries,false);assert.equal(source.input_files,13);assert.equal(source.complete_read_keys,26);assert.equal(source.inputs.length,26);eq(source.current_findings,{reader:0,entry:0,capture:0,request:0});
 for(const i of [0,1,6,7,8]){const p=source.inputs.filter(p=>p.path===base+names[i]);assert.equal(p.length,2);eq(p.map(p=>p.phase).sort(),['after','before']);for(const k of p){for(const v of W){validStat(k[v],0o100000n);eq(k[v],current[i].begin);}eq(k.content,pin(bodies[i]));assert.equal(k.eof,true);assert.equal(k.close_succeeded,true);eq(k.reads,[{requested:65536,returned:bodies[i].length},{requested:65536,returned:0}]);}}
 eq(source.future_enabled_pin_only,{...pin(bodies[2]),materialized:false,queried:false,authorized:false});
 const request=json(4),template=json(8),proposal=json(6),actual=wrapped(15,'f7f84e');
 assert.equal(request.enabled,true);assert.equal(request.status,'ROOT_BOUND_THREE_LEXICAL_LEAVES_ONLY');eq({...request,enabled:false,status:template.status,permission_receipt:null},template);eq(request.permission_receipt,{path:base+names[5],pin:pin(bodies[5])});
 assert.equal(actual.result.output,'');assert.equal(actual.result.original_token_count,0);eq(actual.arguments,proposal.proposed_native_request.arguments);assert(Buffer.from(actual.arguments.cmd).equals(bodies[7]));
 const preNative=wrapped(13,'45b3da'),closeNative=wrapped(17,'66c18e'),matNative=wrapped(11,'6c8bf2');
 eq(preNative.arguments,{cmd:'node docs/papers211_215_sequence/qa/p212_os_release_root01/PREFLIGHT.cjs',max_output_tokens:15000});eq(closeNative.arguments,{cmd:'node docs/papers211_215_sequence/qa/p212_os_release_root01/CLOSE_RAW.cjs',max_output_tokens:13000});
 const pre=JSON.parse(preNative.result.output);keys(pre,['status','keys','directories','request']);assert.equal(pre.status,'PASS_SOURCE_COPIES_BOUND_REQUEST_FRESH_DIRECTORIES');eq(pre.request,request);assert.equal(pre.keys.length,9);for(let i=0;i<9;i++)prior(pre.keys[i],i);
 const closed=JSON.parse(closeNative.result.output);keys(closed,['status','actual_chunk','inputs','raw','raw_directory','host_candidates_reopened']);assert.equal(closed.status,'CLOSED_RAW_NINE_OUTSIDE_KEYS_ACCEPTED_DATA_PENDING');assert.equal(closed.actual_chunk,'f7f84e');assert.equal(closed.host_candidates_reopened,false);assert.equal(closed.inputs.length,9);for(let i=0;i<9;i++)prior(closed.inputs[i],i);assert.equal(closed.raw.length,2);for(let j=0;j<2;j++){prior(closed.raw[j],18+j);assert.equal(BigInt(current[18+j].begin.mode)&0o7777n,0o600n);}assert(current[18].begin.dev!==current[19].begin.dev||current[18].begin.ino!==current[19].begin.ino);
 const mat=JSON.parse(matNative.result.output);keys(mat,['status','sources','destinations','directories','absent','source_keys_unchanged','reader_exact_single_activation_delta','entry_whole_raw_equal','observation_permission','binding_request_created']);assert.equal(mat.status,'EXACT_WORKSPACE_MATERIALIZATION_ONLY');for(const k of ['source_keys_unchanged','reader_exact_single_activation_delta','entry_whole_raw_equal'])assert.equal(mat[k],true);for(const k of ['observation_permission','binding_request_created'])assert.equal(mat[k],false);assert.equal(mat.sources.length,5);assert.equal(mat.destinations.length,2);
 for(const [j,i] of [0,1,8,6,9,2,3].entries()){const p=mat.sources.concat(mat.destinations)[j];keys(p,['path',...W,'reads','eof','close_succeeded','bytes','sha256','raw_hex']);assert.equal(p.path,base+names[i]);for(const v of W){validStat(p[v],0o100000n);eq(p[v],current[i].begin);}assert(decodeHex(p.raw_hex,{bytes:p.bytes,sha256:p.sha256},1048576).equals(bodies[i]));eq(p.reads,[bodies[i].length,0]);assert.equal(p.eof,true);assert.equal(p.close_succeeded,true);}
 eq(mat.absent,[4,18,19].map(i=>({path:base+names[i],actual_error:'ENOENT'})));
 const dirs=['p212_os_release_enabled01','p212_os_release_binding01','p212_os_release_raw01'],initialMembers=[['ENTRY.mjs','three_leaves.mjs'],['REQUEST.json'],[]],nowMembers=[initialMembers[0],initialMembers[1],['stderr.raw','stdout.json']];assert.equal(pre.directories.length,3);assert.equal(mat.directories.length,3);keys(closed.raw_directory,['path','key','members']);assert.equal(closed.raw_directory.path,base+dirs[2]);eq(closed.raw_directory.members,nowMembers[2]);validStat(closed.raw_directory.key,0o040000n);
 for(let i=0;i<3;i++){const d=pre.directories[i],m=mat.directories[i];keys(d,['path','begin','end','entries']);assert.equal(d.path,base+dirs[i]);validStat(d.begin,0o040000n);eq(d.begin,d.end);eq(d.entries,initialMembers[i]);keys(m,['path',...W,'members','close_succeeded']);assert.equal(m.path,d.path);for(const v of W){validStat(m[v],0o040000n);eq(m[v],m.lstat_before);}assert.equal(m.close_succeeded,true);eq(m.members,i===0?initialMembers[0]:[]);for(const f of F.slice(0,7))assert.equal(d.begin[f],m.lstat_before[f]);if(i!==1)eq(d.begin,m.lstat_before);
  const path=base+dirs[i],begin=stat(fs.lstatSync(path,{bigint:true})),members=fs.readdirSync(path).sort(),end=stat(fs.lstatSync(path,{bigint:true}));validStat(begin,0o040000n);eq(begin,end);assert.equal(BigInt(begin.mode)&0o7777n,0o700n);assert.equal(begin.uid,'0');assert.equal(begin.gid,'0');eq(members,nowMembers[i]);eq(begin,i===2?closed.raw_directory.key:d.end);for(const f of F.slice(0,7))assert.equal(begin[f],d.end[f]);directories.push({path,begin,end,members});
 }
 const capture=json(18);assert(Buffer.from(JSON.stringify(capture)+'\n','utf8').equals(bodies[18]));keys(capture,['schema','status','request_input','reader_called','reader_returned','reader_result','entry_failure','operation_permission','installed_closure','referents_followed','package_queries']);assert.equal(capture.schema,'p212-three-leaf-captured-result-v1');assert.equal(capture.status,'THREE_LEXICAL_LEAVES_ROOT_RECEPTION_PENDING');assert.equal(capture.reader_called,true);assert.equal(capture.reader_returned,true);assert.equal(capture.entry_failure,null);for(const k of ['operation_permission','installed_closure','referents_followed','package_queries'])assert.equal(capture[k],false);
 const input=capture.request_input;keys(input,['path','byte_limit',...W,'bytes_read','reads','eof','close_succeeded','raw_hex','content','complete','error','close_error']);assert.equal(input.path,base+names[4]);assert.equal(input.byte_limit,65536);for(const v of W){validStat(input[v],0o100000n);eq(input[v],current[4].begin);}assert(decodeHex(input.raw_hex,input.content,65536).equals(bodies[4]));assert.equal(input.bytes_read,bodies[4].length);reads(input.reads,input.bytes_read,65536);for(const k of ['eof','close_succeeded','complete'])assert.equal(input[k],true);assert.equal(input.error,null);assert.equal(input.close_error,null);
 const result=capture.reader_result;keys(result,['schema','status','request','rows','accepted_regular_bytes','accepted_link_bytes','failure','referents_followed','terminal_selection','actual_ancestor_scan','source_acceptance','operation_permission','installed_closure']);assert.equal(result.schema,'p212-three-lexical-leaves-v1');assert.equal(result.status,capture.status);eq(result.request,request);assert.equal(result.failure,null);assert.equal(result.terminal_selection,null);for(const k of ['referents_followed','actual_ancestor_scan','source_acceptance','operation_permission','installed_closure'])assert.equal(result[k],false);
 const entry={id:'OS_RELEASE',path:'/etc/os-release',role:'distributor_identity_alias_or_body',optional:false,max_regular_bytes:65536,max_link_bytes:4096};eq(request.entries,[entry]);assert.equal(request.total_regular_byte_limit,65536);assert.equal(request.total_link_byte_limit,4096);assert.equal(result.rows.length,1);
 // This pinned actual is a symlink, so a regular-body branch would overstate its scope.
 const row=result.rows[0];keys(row,['id','path','role','kind','lstat_before','lstat_after','regular','link','complete','error']);for(const k of ['id','path','role'])assert.equal(row[k],entry[k]);assert.equal(row.kind,'symlink');assert.equal(row.regular,null);assert.equal(row.error,null);assert.equal(row.complete,true);validStat(row.lstat_before,0o120000n);validStat(row.lstat_after,0o120000n);eq(row.lstat_before,row.lstat_after);
 const link=row.link;keys(link,['readlink_returned','raw_hex','content','target_utf8','point_complete','same_fd_attested']);assert.equal(link.readlink_returned,true);assert.equal(link.point_complete,true);assert.equal(link.same_fd_attested,false);const target=decodeHex(link.raw_hex,link.content,4096);assert(target.length>0&&!target.includes(0));assert.equal(BigInt(target.length),BigInt(row.lstat_before.size));assert(Buffer.from(link.target_utf8,'utf8').equals(target));assert.equal(link.target_utf8,'../usr/lib/os-release');assert.equal(target.length,21);
 assert.equal(result.accepted_regular_bytes,0);assert.equal(result.accepted_link_bytes,target.length);
 console.log(JSON.stringify({status:'ACCEPT_ONE_OS_RELEASE_LITERAL_LINK_DATA_ONLY',findings:{critical:0,major:0,minor:0,open:0},actual_native:actual.result,stdout:pin(bodies[18]),stderr:pin(bodies[19]),ordinary_json_utf8_plus_one_lf_exact:true,nine_outside_keys_match_preflight_closed_and_current:true,exact_source_activation_and_entry_copy:true,full_bound_request_bytes_keys_and_grant_reference_match:true,accepted_source_replay_whole_output_equal:true,materialization_receipt_checked:true,reused_checkers:[21,22].map(i=>({path:base+names[i],...pin(bodies[i])})),observation:{id:row.id,origin_lexical_candidate:row.path,role:row.role,kind:row.kind,lstat_before:row.lstat_before,lstat_after:row.lstat_after,...link,scope:'LITERAL_READLINK_BYTES_WITH_TWO_EQUAL_POINT_STAT_VIEWS_ONLY'},accepted_regular_bytes:0,accepted_link_bytes:21,failure:null,host_candidates_reopened:false,received_source_executed_or_imported:false,os_identity_fields_parsed:false,elf_or_package_interpretation:false,referents_followed:false,terminal_selection:null,operation_permission:false,installed_closure:false,bootstrap_boundary:'Ordinary Node/filesystem/product/trusted ancestors; not historical race freedom, link simultaneity, same-fd link identity or distributor/package provenance',current_documents:current,current_directories:directories}));
}catch(e){console.log(JSON.stringify({status:'FAIL_DATA_RECEPTION_PRESERVE_ORIGINALS',error:{name:e.name,message:e.message,stack:e.stack},current_documents:current,current_directories:directories,host_candidates_reopened:false,received_source_executed_or_imported:false}));process.exitCode=1;}
