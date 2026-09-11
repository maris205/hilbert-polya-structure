'use strict';
// Only exact current source/binding/grant keys and previously prepared directories.
const fs=require('node:fs'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const P='docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_',R=P+'execution_root01/',M=P+'materialization_root01/',S=P+'source_root01/',A=P+'preparation01/',B=P+'binding01/',E=P+'enabled01/',RAW=P+'raw01';
const files=[R+'GRANT.json',R+'CREATION_NATIVE.json',R+'PREFLIGHT.cjs',B+'FILE_REQUEST.json',...['RECEPTION.md','SHA256SUMS','CHECK_NATIVE.json','REPLAY_NATIVE.json','SCOPE.md'].map(n=>M+n),S+'RECEPTION.md',S+'SHA256SUMS',E+'file_keys.mjs',E+'collect_files.mjs',A+'FILE_REQUEST.proposed.json',A+'ENTRY_REQUEST.proposed.json',A+'capture.proposed.sh.txt','docs/papers211_215_sequence/qa/p213_initial_science_enabled_root01/READ_FIXED.cjs'];
const r=make(new Set(files)),{need,read,equal,sha,keys}=r;
const report={status:'RUNNING',scope:'EXACT_CURRENT_BINDING_AND_EIGHT_FILE_CAPTURE_PREFLIGHT',candidate_observation:false,source_execution:false};
try{
 need(process.argv.length===2&&process.cwd()==='/root/autodl-tmp/symbolic_dynamics','EXACT_ROOT_PREFLIGHT_CONTEXT');files.forEach(read);
 const g=JSON.parse(read(R+'GRANT.json')),b=JSON.parse(read(B+'FILE_REQUEST.json')),t=JSON.parse(read(A+'FILE_REQUEST.proposed.json')),entry=JSON.parse(read(A+'ENTRY_REQUEST.proposed.json'));
 need(g.id==='P212_EIGHT_FILE_OBSERVATION_NEW_SINGLE_01'&&g.permitted_native_submissions===1&&!g.consumed&&!g.old_two_grants_reused,'DISTINCT_NEW_SINGLE_GRANT');
 need(sha(read(M+'RECEPTION.md'))===g.materialization_acceptance.sha256&&sha(read(M+'SHA256SUMS'))===g.materialization_acceptance.seal,'ACTUAL_MATERIALIZATION_ROOT_ACCEPTANCE');
 need(sha(read(S+'RECEPTION.md'))===g.source_acceptance.sha256&&sha(read(S+'SHA256SUMS'))===g.source_acceptance.seal,'ACCEPTED_SOURCE_RECEIPT_SEAL');
 const names=['CHECK_NATIVE.json','RECEPTION.md','REPLAY_NATIVE.json','SCOPE.md'].sort();
 need(Buffer.from(names.map(n=>sha(read(M+n))+'  '+n+'\n').join('')).equals(read(M+'SHA256SUMS')),'ENTIRE_FOUR_PAYLOAD_ROOT_NONSELF_SEAL');
 need(equal(fs.readdirSync(M).sort(),[...names,'SHA256SUMS'].sort()),'ENTIRE_ROOT_RECEIPT_LAYOUT');
 need(sha(read('docs/papers211_215_sequence/qa/p213_initial_science_enabled_root01/READ_FIXED.cjs'))==='f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7','EXACT_TRUSTED_ORDINARY_READER');
 const mn=JSON.parse(read(M+'CHECK_NATIVE.json')),mv=JSON.parse(mn.result.output),mr=JSON.parse(read(M+'REPLAY_NATIVE.json'));
 need(mn.result.exit_code===0&&mn.result.chunk_id==='20a7fd'&&mv.status==='PASS_ROOT_MATERIALIZATION_ORIGINAL_AND_CURRENT_RECEPTION','ACTUAL_ROOT_MATERIALIZATION_ORIGINAL');
 for(const p of [E+'file_keys.mjs',E+'collect_files.mjs',A+'FILE_REQUEST.proposed.json',A+'ENTRY_REQUEST.proposed.json',A+'capture.proposed.sh.txt',S+'RECEPTION.md',S+'SHA256SUMS'])need(equal(keys.get(p),mv.keys.find(k=>k.path===p)),'ALL_ENTIRE_CURRENT_MATERIALIZED_SOURCE_AND_TEMPLATE_KEYS');
 need(b.enabled===true&&b.status==='ROOT_BOUND_FINITE_FILES_ONLY','EXACT_ENABLED_BINDING_VALUES');
 need(equal({...b,enabled:false,status:t.status,permission_receipt:null},t),'ONLY_THREE_ACCEPTED_REQUEST_FIELD_CHANGES');
 const permission={path:'/root/autodl-tmp/symbolic_dynamics/'+R+'GRANT.json',pin:{bytes:read(R+'GRANT.json').length,sha256:sha(read(R+'GRANT.json'))}};
 need(equal(b.permission_receipt,permission),'ENTIRE_EXTERNAL_NEW_GRANT_REFERENCE_PIN');
 need(equal(g.ordered_eight_candidates,t.entries)&&g.total_byte_limit===t.total_byte_limit,'ALL_EIGHT_LITERAL_CANDIDATES_UNCHANGED');
 need(equal(g.native_request,entry.proposed_native_request)&&equal(g.continuation,entry.proposed_continuation),'FULL_ACCEPTED_NATIVE_AND_CONTINUATION_REQUEST');
 need(Buffer.from(g.native_request.arguments.cmd).equals(read(A+'capture.proposed.sh.txt')),'COMPLETE_INLINE_CAPTURE_RAW_BYTES');
 const bk=keys.get(B+'FILE_REQUEST.json').lstat_before;
 need(bk.nlink==='1'&&bk.uid==='0'&&bk.gid==='0'&&Number(bk.size)<=65536,'EXACT_PHYSICAL_BOUNDED_BINDING');
 function directory(p,expected){
  const before=fs.lstatSync(p,{bigint:true});need(before.isDirectory()&&!before.isSymbolicLink()&&(before.mode&0o7777n)===0o700n&&before.uid===0n&&before.gid===0n,'EXACT_PRIVATE_CURRENT_DIRECTORY');
  const d=fs.opendirSync(p),names=[];try{for(;;){const x=d.readSync();if(x===null)break;names.push(x.name);need(names.length<=expected.length,'NO_UNEXPECTED_DIRECTORY_MEMBER');}}finally{d.closeSync();}
  need(equal(names.sort(),expected.slice().sort()),'EXACT_CURRENT_MEMBERS_TO_EOF');const after=fs.lstatSync(p,{bigint:true});need(equal(r.stat(before),r.stat(after)),'ENTIRE_DIRECTORY_POINT_KEY_UNCHANGED');return{path:p,before:r.stat(before),after:r.stat(after),names,eof:true,closed:true};
 }
 const dirs=[directory(B.slice(0,-1),['FILE_REQUEST.json']),directory(E.slice(0,-1),['file_keys.mjs','collect_files.mjs']),directory(RAW,[])];
 const old=JSON.parse(mr.author_replays[0].result.output);
 need(equal(dirs[1].before,old.disposition.enabled_directory.before)&&equal(dirs[2].before,old.disposition.raw_directory.before),'COMPLETE_PREPARED_RUNTIME_DIRECTORY_KEYS_UNCHANGED');
 const c=JSON.parse(read(R+'CREATION_NATIVE.json'));need(c.absence.result.exit_code===0&&c.mkdir.result.exit_code===0,'ACTUAL_BINDING_CREATION_NATIVE');
 const prior=JSON.parse(c.absence.result.output);need(prior.directory===B.slice(0,-1)&&prior.lstat_errno==='ENOENT'&&equal(prior.grant,permission),'ACTUAL_EXACT_NEW_BINDING_ABSENCE_AND_GRANT_PIN');
 const want='*** Begin Patch\n*** Add File: '+B+'FILE_REQUEST.json\n'+read(B+'FILE_REQUEST.json').toString('utf8').trimEnd().split('\n').map(l=>'+'+l).join('\n')+'\n*** End Patch';
 need(c.request_patch.patch===want,'WHOLE_ACTUAL_BOUND_REQUEST_PATCH_BYTES');
 const sf=fs.statfsSync('.',{bigint:true}),available=sf.bavail*sf.bsize;need(available>=536870912n,'CURRENT_CAPTURE_CAPACITY_NOT_RESERVATION');
 report.capacity={available_bytes:available.toString(),minimum_bytes:'536870912',reserved:false};
 report.directories=dirs;report.bound_request_key=keys.get(B+'FILE_REQUEST.json');report.grant_key=keys.get(R+'GRANT.json');report.exact_native_request=g.native_request;
 report.status='PASS_EXACT_BOUND_EIGHT_FILE_OBSERVATION_PREFLIGHT';
}catch(e){report.status='FAIL_PREFLIGHT_NO_OBSERVATION_SUBMITTED';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=r.checks;report.key_count=keys.size;report.total_read_bytes=r.total;report.keys=[...keys.values()];
process.stdout.write(JSON.stringify(report,null,2)+'\n');
