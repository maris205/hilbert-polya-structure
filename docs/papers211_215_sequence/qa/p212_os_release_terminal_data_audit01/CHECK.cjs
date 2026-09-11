'use strict';
// Fixed DATA only. Reuses accepted single-leaf and regular-body reception mechanics.
// Never import, execute, open or resolve a path obtained from captured DATA.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const base='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/';
const names=[
 'p212_os_release_terminal_preparation01/os_release_terminal.proposed.mjs.txt',
 'p212_os_release_terminal_preparation01/ENTRY.proposed.mjs.txt',
 'p212_os_release_terminal_enabled01/three_leaves.mjs',
 'p212_os_release_terminal_enabled01/ENTRY.mjs',
 'p212_os_release_terminal_binding01/REQUEST.json',
 'p212_os_release_terminal_root01/CONDITIONAL_GRANT.md',
 'p212_os_release_terminal_preparation01/OPERATION_REQUEST.proposed.json',
 'p212_os_release_terminal_preparation01/capture.proposed.sh.txt',
 'p212_os_release_terminal_preparation01/REQUEST.disabled.json',
 'p212_os_release_terminal_root01/SOURCE_RECEPTION.md',
 'p212_os_release_terminal_root01/SOURCE_CHECK_NATIVE.json',
 'p212_os_release_terminal_root01/MATERIALIZATION_RECEPTION_NATIVE.json',
 'p212_os_release_terminal_root01/PREFLIGHT.cjs',
 'p212_os_release_terminal_root01/PREFLIGHT_NATIVE.json',
 'p212_os_release_terminal_root01/CONSUMPTION.md',
 'p212_os_release_terminal_root01/ACTUAL_NATIVE.json',
 'p212_os_release_terminal_root01/CLOSE_RAW.cjs',
 'p212_os_release_terminal_root01/CLOSED_RAW_NATIVE.json',
 'p212_os_release_terminal_raw01/stdout.json',
 'p212_os_release_terminal_raw01/stderr.raw',
 'p212_os_release_terminal_materialization01/NATIVE.json',
 'p212_os_release_data_audit01/CHECK.cjs',
 'p212_three_terminal_data_audit01/CHECK.cjs',
 'p212_os_release_terminal_preparation01/SHA256SUMS',
 'p212_os_release_root01/DATA_RECEPTION.md'
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
  0:[5897,'b38f0513f0224980e040434ea9b060d95bacdaed0b018d65aa0b2c2a617b8f12'],
  1:[6182,'62e434388f8b0443d76571217e719a94e3594bb4821d2fc92698d5a25e619200'],
  2:[5896,'9322c3b64b897819a0bad71cb3bce5f299c00a3725a45b0b1600f2a63ac21be1'],
  4:[745,'28a3fe7f79c7f9bdb7ed628aab99619feb83d2aadda3598e943cf7045711c23e'],
  5:[1373,'84250cdfde21f2dde70c2049aa7ad5aa6d61fa7ac5914ef272a036d427ab9b4e'],
  6:[4137,'bd801b27956735317b13389f1442abcfe345720123673e900a53993b95449115'],
  7:[563,'e3d637fed9633d34e214ac6803e0d443f2dbd06ce7c78f500d17f046bebef785'],
  8:[481,'8934875881fd7dae45d50fa5f735d9e3a6b5944b382008f06ee54fae9ab43f04'],
  10:[16889,'887da72a7ce7701ac69861f7150bc4cba9b517b7d4c3b29d3a9a98176b8e06ec'],
  18:[5860,'c755f4dcc29702b7185070e53722e16f37a67b0534803298a87a93fdba6e5c8c'],
  19:[0,'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'],
  20:[283691,'3101e83eb6fc6726a2fd920697314ce288da817ff27f5be98446a809f5e3fba3'],
  21:[17530,'8de0936fd3b761631a4404483a601dbb97f3aca26f1202643c29da9d4e843410'],
  22:[16907,'426b736be8c9eb00cf7982de4f1e5b39677bf3297553e75c3ef63a13956bab1d']
 };
 for(const [i,p] of Object.entries(expected))eq([bodies[i].length,sha(bodies[i])],p);
 const disabled=bodies[0].toString('utf8');assert.equal(disabled.split(' const SOURCE_ENABLED=false;').length,2);assert(Buffer.from(disabled.replace(' const SOURCE_ENABLED=false;',' const SOURCE_ENABLED=true;')).equals(bodies[2]));assert(bodies[1].equals(bodies[3]));
 // All five root records are explicitly {arguments,result}; materializer POST uses request/result.
 const sourceNative=wrapped(10,'f64d8c'),source=JSON.parse(sourceNative.result.output);
 eq(sourceNative.arguments,{cmd:'node docs/papers211_215_sequence/qa/p212_os_release_terminal_root01/SOURCE_CHECK.cjs',max_output_tokens:18000});
 keys(source,['status','keys','source_deltas','request_deltas','operation_deltas','reader_pin','enabled_reader_pin','candidate','host_candidate_read','operation_permission','data_reception_separate']);
 assert.equal(source.status,'PASS_ROOT_INDEPENDENT_SOURCE_DELTA_ONLY');assert.equal(source.host_candidate_read,false);assert.equal(source.operation_permission,false);assert.equal(source.data_reception_separate,true);assert.equal(source.keys.length,22);assert.equal(source.source_deltas,5);assert.equal(source.request_deltas,2);assert.equal(source.operation_deltas,8);assert.equal(source.candidate,'/usr/lib/os-release');
 for(const i of [0,1,6,7,8]){const matches=source.keys.filter(p=>p.path==='docs/papers211_215_sequence/qa/'+names[i]);assert.equal(matches.length,1);const k=matches[0];keys(k,['path','key','four_views_equal','reads','eof','close_succeeded','bytes','sha256']);validStat(k.key,0o100000n);eq(k.key,current[i].begin);eq({bytes:k.bytes,sha256:k.sha256},pin(bodies[i]));for(const f of ['four_views_equal','eof','close_succeeded'])assert.equal(k[f],true);eq(k.reads,[bodies[i].length,0]);}
 eq(source.reader_pin,pin(bodies[0]));eq(source.enabled_reader_pin,pin(bodies[2]));
 const request=json(4),template=json(8),proposal=json(6),actual=wrapped(15,'e2bc8e');
 assert.equal(request.enabled,true);assert.equal(request.status,'ROOT_BOUND_THREE_LEXICAL_LEAVES_ONLY');eq({...request,enabled:false,status:template.status,permission_receipt:null},template);eq(request.permission_receipt,{path:base+names[5],pin:pin(bodies[5])});
 assert.equal(actual.result.output,'');assert.equal(actual.result.original_token_count,0);eq(actual.arguments,proposal.proposed_native_request.arguments);assert(Buffer.from(actual.arguments.cmd).equals(bodies[7]));
 const preNative=wrapped(13,'97e340'),closeNative=wrapped(17,'317e0d'),matNative=wrapped(11,'cc57fe');
 eq(preNative.arguments,{cmd:'node docs/papers211_215_sequence/qa/p212_os_release_terminal_root01/PREFLIGHT.cjs',max_output_tokens:15000});eq(closeNative.arguments,{cmd:'node docs/papers211_215_sequence/qa/p212_os_release_terminal_root01/CLOSE_RAW.cjs',max_output_tokens:14000});
 const pre=JSON.parse(preNative.result.output);keys(pre,['status','keys','directories','request']);assert.equal(pre.status,'PASS_SOURCE_COPIES_BOUND_REQUEST_FRESH_DIRECTORIES');eq(pre.request,request);assert.equal(pre.keys.length,9);for(let i=0;i<9;i++)prior(pre.keys[i],i);
 const closed=JSON.parse(closeNative.result.output);keys(closed,['status','actual_chunk','inputs','raw','raw_directory','host_candidates_reopened']);assert.equal(closed.status,'CLOSED_RAW_NINE_OUTSIDE_KEYS_ACCEPTED_DATA_PENDING');assert.equal(closed.actual_chunk,'e2bc8e');assert.equal(closed.host_candidates_reopened,false);assert.equal(closed.inputs.length,9);for(let i=0;i<9;i++)prior(closed.inputs[i],i);assert.equal(closed.raw.length,2);for(let j=0;j<2;j++){prior(closed.raw[j],18+j);assert.equal(BigInt(current[18+j].begin.mode)&0o7777n,0o600n);}assert(current[18].begin.dev!==current[19].begin.dev||current[18].begin.ino!==current[19].begin.ino);
 const archive=json(20);keys(archive,['schema','scope','records','read_only_replay_record','cutoff']);assert.equal(archive.read_only_replay_record,'otmPost01');assert(Array.isArray(archive.records));const postMatches=archive.records.filter(r=>r.name==='otmPost01');assert.equal(postMatches.length,1);const post=postMatches[0];keys(post,['name','tool','request','result']);assert.equal(post.tool,'exec_command');native(post.result,'520ce9');eq(post.request,matNative.arguments);assert(Buffer.from(post.result.output).equals(Buffer.from(matNative.result.output)));
 const mat=JSON.parse(matNative.result.output);keys(mat,['status','source_inputs','copies','directories','source_execution','host_queries','request_created','grant_created','whole_source_input_raw_comparisons','whole_transformed_copy_raw_comparisons','current_file_keys','current_directory_keys']);assert.equal(mat.status,'POST_COMPLETE_PRE_INPUTS_UNCHANGED_TWO_EXACT_0600_COPIES_THREE_0700_DIRECTORIES');for(const k of ['source_execution','host_queries','request_created','grant_created'])assert.equal(mat[k],false);assert.equal(mat.source_inputs.length,8);assert.equal(mat.copies.length,2);eq([mat.whole_source_input_raw_comparisons,mat.whole_transformed_copy_raw_comparisons,mat.current_file_keys,mat.current_directory_keys],[8,2,10,3]);
 for(const [j,i] of [0,1,7,8,6,23,9,24,2,3].entries()){const p=mat.source_inputs.concat(mat.copies)[j];keys(p,['path','role',...W,'reads','eof','close_succeeded','raw_hex','content']);assert.equal(p.path,base+names[i]);assert.equal(p.role,['reader','entry','capture','request','operation','preparation_seal','source_reception','data_reception','enabled_reader','entry'][j]);for(const v of W){validStat(p[v],0o100000n);eq(p[v],current[i].begin);}assert(decodeHex(p.raw_hex,p.content,1048576).equals(bodies[i]));eq(p.reads,[{requested:65536,returned:bodies[i].length},{requested:65536,returned:0}]);assert.equal(p.eof,true);assert.equal(p.close_succeeded,true);}
 const dirs=['p212_os_release_terminal_enabled01','p212_os_release_terminal_binding01','p212_os_release_terminal_raw01'],initialMembers=[['ENTRY.mjs','three_leaves.mjs'],['REQUEST.json'],[]],nowMembers=[initialMembers[0],initialMembers[1],['stderr.raw','stdout.json']];assert.equal(pre.directories.length,3);assert.equal(mat.directories.length,3);keys(closed.raw_directory,['path','key','members']);assert.equal(closed.raw_directory.path,base+dirs[2]);eq(closed.raw_directory.members,nowMembers[2]);validStat(closed.raw_directory.key,0o040000n);
 for(let i=0;i<3;i++){const d=pre.directories[i],m=mat.directories[i];keys(d,['path','begin','end','entries']);assert.equal(d.path,base+dirs[i]);validStat(d.begin,0o040000n);eq(d.begin,d.end);eq(d.entries,initialMembers[i]);keys(m,['path','lstat_before','members_hex','members_utf8','lstat_after','enumeration']);assert.equal(m.path,d.path);for(const v of ['lstat_before','lstat_after']){validStat(m[v],0o040000n);eq(m[v],m.lstat_before);}assert.equal(m.enumeration,'one exact pathname directory; matching ten-field endpoint keys, not a same-fd membership claim');eq(m.members_utf8,i===0?initialMembers[0]:[]);eq(m.members_hex,m.members_utf8.map(n=>Buffer.from(n).toString('hex')));for(const f of F.slice(0,7))assert.equal(d.begin[f],m.lstat_before[f]);if(i!==1)eq(d.begin,m.lstat_before);
  const path=base+dirs[i],begin=stat(fs.lstatSync(path,{bigint:true})),members=fs.readdirSync(path).sort(),end=stat(fs.lstatSync(path,{bigint:true}));validStat(begin,0o040000n);eq(begin,end);assert.equal(BigInt(begin.mode)&0o7777n,0o700n);assert.equal(begin.uid,'0');assert.equal(begin.gid,'0');eq(members,nowMembers[i]);eq(begin,i===2?closed.raw_directory.key:d.end);for(const f of F.slice(0,7))assert.equal(begin[f],d.end[f]);directories.push({path,begin,end,members});
 }
 const capture=json(18);assert(Buffer.from(JSON.stringify(capture)+'\n','utf8').equals(bodies[18]));keys(capture,['schema','status','request_input','reader_called','reader_returned','reader_result','entry_failure','operation_permission','installed_closure','referents_followed','package_queries']);assert.equal(capture.schema,'p212-three-leaf-captured-result-v1');assert.equal(capture.status,'THREE_LEXICAL_LEAVES_ROOT_RECEPTION_PENDING');assert.equal(capture.reader_called,true);assert.equal(capture.reader_returned,true);assert.equal(capture.entry_failure,null);for(const k of ['operation_permission','installed_closure','referents_followed','package_queries'])assert.equal(capture[k],false);
 const input=capture.request_input;keys(input,['path','byte_limit',...W,'bytes_read','reads','eof','close_succeeded','raw_hex','content','complete','error','close_error']);assert.equal(input.path,base+names[4]);assert.equal(input.byte_limit,65536);for(const v of W){validStat(input[v],0o100000n);eq(input[v],current[4].begin);}assert(decodeHex(input.raw_hex,input.content,65536).equals(bodies[4]));assert.equal(input.bytes_read,bodies[4].length);reads(input.reads,input.bytes_read,65536);for(const k of ['eof','close_succeeded','complete'])assert.equal(input[k],true);assert.equal(input.error,null);assert.equal(input.close_error,null);
 const result=capture.reader_result;keys(result,['schema','status','request','rows','accepted_regular_bytes','accepted_link_bytes','failure','referents_followed','terminal_selection','actual_ancestor_scan','source_acceptance','operation_permission','installed_closure']);assert.equal(result.schema,'p212-three-lexical-leaves-v1');assert.equal(result.status,capture.status);eq(result.request,request);assert.equal(result.failure,null);assert.equal(result.terminal_selection,null);for(const k of ['referents_followed','actual_ancestor_scan','source_acceptance','operation_permission','installed_closure'])assert.equal(result[k],false);
 const entry={id:'OS_RELEASE',path:'/usr/lib/os-release',role:'distributor_identity_regular_candidate',optional:false,max_regular_bytes:65536,max_link_bytes:0};eq(request.entries,[entry]);assert.equal(request.total_regular_byte_limit,65536);assert.equal(request.total_link_byte_limit,0);assert.equal(result.rows.length,1);
 const row=result.rows[0];keys(row,['id','path','role','kind','lstat_before','lstat_after','regular','link','complete','error']);for(const k of ['id','path','role'])assert.equal(row[k],entry[k]);assert.equal(row.kind,'regular');assert.equal(row.link,null);assert.equal(row.error,null);assert.equal(row.complete,true);
 const r=row.regular;keys(r,['fd','fstat_before','fstat_after','reads','bytes_read','eof','close_succeeded','raw_hex','content','close_error']);assert(Number.isSafeInteger(r.fd)&&r.fd>=0);for(const s of [row.lstat_before,r.fstat_before,r.fstat_after,row.lstat_after]){validStat(s,0o100000n);eq(s,row.lstat_before);}assert(BigInt(row.lstat_before.size)<=65536n);assert(Number.isSafeInteger(r.bytes_read)&&r.bytes_read>=0&&r.bytes_read<=65536);const body=decodeHex(r.raw_hex,r.content,65536);assert.equal(body.length,r.bytes_read);assert.equal(BigInt(r.bytes_read),BigInt(row.lstat_before.size));reads(r.reads,r.bytes_read,65536);assert.equal(r.eof,true);assert.equal(r.close_succeeded,true);assert.equal(r.close_error,null);
 eq(pin(body),{bytes:386,sha256:'594d5ddd35aedb47f00d9c34d140017907a5b9f93c975aba125fc924daac5c07'});assert.equal(result.accepted_regular_bytes,386);assert.equal(result.accepted_link_bytes,0);
 // Parse only this pinned simple ASCII assignment subset; no shell, escape or substitution evaluation.
 const bodyText=body.toString('utf8');assert(Buffer.from(bodyText,'utf8').equals(body));assert([...body].every(n=>n===10||(n>=32&&n<=126)));assert(bodyText.endsWith('\n'));const lines=bodyText.slice(0,-1).split('\n');assert.equal(lines.length,12);const fields={},assignments=[];let offset=0;
 for(let i=0;i<lines.length;i++){const line=lines[i],m=/^([A-Z][A-Z0-9_]*)=(.*)$/.exec(line);assert(m);const name=m[1],rawValue=m[2];assert(!Object.hasOwn(fields,name));let value,quoting;if(rawValue.startsWith('"')){assert(/^"[^"\\$\x60]*"$/.test(rawValue));value=rawValue.slice(1,-1);quoting='simple_double_quoted_literal';}else{assert(/^[A-Za-z0-9._-]+$/.test(rawValue));value=rawValue;quoting='unquoted_literal';}fields[name]=value;const bytes=Buffer.from(line+'\n');assert(body.subarray(offset,offset+bytes.length).equals(bytes));assignments.push({line:i+1,byte_start:offset,byte_end_exclusive:offset+bytes.length,key:name,raw_value:rawValue,value,quoting});offset+=bytes.length;}
 assert.equal(offset,body.length);eq(fields,{PRETTY_NAME:'Ubuntu 22.04.5 LTS',NAME:'Ubuntu',VERSION_ID:'22.04',VERSION:'22.04.5 LTS (Jammy Jellyfish)',VERSION_CODENAME:'jammy',ID:'ubuntu',ID_LIKE:'debian',HOME_URL:'https://www.ubuntu.com/',SUPPORT_URL:'https://help.ubuntu.com/',BUG_REPORT_URL:'https://bugs.launchpad.net/ubuntu/',PRIVACY_POLICY_URL:'https://www.ubuntu.com/legal/terms-and-policies/privacy-policy',UBUNTU_CODENAME:'jammy'});
 console.log(JSON.stringify({status:'ACCEPT_ONE_OS_RELEASE_REGULAR_BODY_AND_LITERAL_FIELDS_DATA_ONLY',findings:{critical:0,major:0,minor:0,open:0},actual_native:actual.result,stdout:pin(bodies[18]),stderr:pin(bodies[19]),ordinary_json_utf8_plus_one_lf_exact:true,nine_outside_keys_match_preflight_closed_and_current:true,exact_source_activation_and_entry_copy:true,full_bound_request_bytes_keys_and_grant_reference_match:true,accepted_root_source_review_current_pins_match:true,materialization_post_whole_request_and_output_equal:true,reused_checkers:[21,22].map(i=>({path:base+names[i],...pin(bodies[i])})),observation:{id:row.id,origin_lexical_candidate:row.path,role:row.role,kind:row.kind,body:pin(body),lstat_before:row.lstat_before,fstat_before:r.fstat_before,fstat_after:r.fstat_after,lstat_after:row.lstat_after,fd_recorded:r.fd,reads:r.reads,eof:r.eof,close_succeeded:r.close_succeeded,scope:'COMPLETE_REGULAR_BODY_POINT_AND_SAME_FD_DATA_ONLY'},literal_identity:{body_utf8:bodyText,fields,assignments,interpretation:'Self-description of the captured body only; no shell semantics, package mapping or installed identity guarantee'},accepted_regular_bytes:386,accepted_link_bytes:0,failure:null,host_candidates_reopened:false,received_source_executed_or_imported:false,shell_sourced:false,elf_or_package_interpretation:false,referents_followed:false,terminal_selection:null,operation_permission:false,installed_closure:false,bootstrap_boundary:'Ordinary Node/filesystem/product/trusted ancestors; not historical race freedom, automatic link resolution or distributor/package provenance',current_documents:current,current_directories:directories}));
}catch(e){console.log(JSON.stringify({status:'FAIL_DATA_RECEPTION_PRESERVE_ORIGINALS',error:{name:e.name,message:e.message,stack:e.stack},current_documents:current,current_directories:directories,host_candidates_reopened:false,received_source_executed_or_imported:false}));process.exitCode=1;}
