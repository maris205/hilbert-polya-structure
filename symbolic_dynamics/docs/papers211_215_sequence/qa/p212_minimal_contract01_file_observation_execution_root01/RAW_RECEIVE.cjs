'use strict';
const FIXED=[
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_execution_root01/GRANT.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_execution_root01/CREATION_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_execution_root01/PREFLIGHT.cjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_binding01/FILE_REQUEST.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization_root01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization_root01/CHECK_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization_root01/REPLAY_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization_root01/SCOPE.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_root01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_enabled01/file_keys.mjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_enabled01/collect_files.mjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/FILE_REQUEST.proposed.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/ENTRY_REQUEST.proposed.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/capture.proposed.sh.txt",
  "docs/papers211_215_sequence/qa/p213_initial_science_enabled_root01/READ_FIXED.cjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_execution_root01/PREFLIGHT_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_execution_root01/CONSUMPTION.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_execution_root01/ACTUAL_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_execution_root01/RAW_RECEIVE.cjs"
];
// Bytes/keys only; do not parse or interpret either captured raw stream.
const fs=require('node:fs'),crypto=require('node:crypto'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const P='docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_',R=P+'execution_root01/',RAW=P+'raw01/';
const r=make(new Set(FIXED)),{need,read,equal,keys}=r;const rawKeys=[];
const report={status:'RUNNING',raw_semantics_accepted:false,source_execution:false,observer_rerun:false,host_query:false};
try{
 need(process.argv.length===2&&process.cwd()==='/root/autodl-tmp/symbolic_dynamics','EXACT_CLOSED_RAW_RECEPTION');FIXED.forEach(read);
 const an=JSON.parse(read(R+'ACTUAL_NATIVE.json')),g=JSON.parse(read(R+'GRANT.json')),c=JSON.parse(read(R+'CONSUMPTION.json')),pn=JSON.parse(read(R+'PREFLIGHT_NATIVE.json')),pv=JSON.parse(pn.result.output);
 need(an.result.chunk_id==='e08313'&&an.result.exit_code===0&&!an.result.session_id&&an.result.output===''&&an.continuations.length===0,'ACTUAL_SETTLED_ZERO_EMPTY_NATIVE_CONTROL');
 need(equal(an.request,g.native_request.arguments)&&equal(c.exact_native_request,g.native_request)&&c.grant_id===g.id&&c.remaining_submissions===0,'ENTIRE_NEW_CONSUMED_GRANT_REQUEST_BINDING');
 need(pn.result.chunk_id==='00bf7a'&&pn.result.exit_code===0&&pv.status==='PASS_EXACT_BOUND_EIGHT_FILE_OBSERVATION_PREFLIGHT','ACTUAL_PRE_LAUNCH_BINDING_RECEIPT');
 for(const old of pv.keys)need(equal(keys.get(old.path),old),'EVERY_FULL_CURRENT_PREFLIGHT_KEY_UNCHANGED_AFTER_OBSERVER');
 const before=fs.lstatSync(RAW,{bigint:true});need(before.isDirectory()&&!before.isSymbolicLink()&&(before.mode&0o7777n)===0o700n&&before.uid===0n,'EXACT_PREPARED_PRIVATE_CAPTURE_DIRECTORY');
 const oldDir=pv.directories.find(d=>d.path===RAW.slice(0,-1));for(const f of r.fields.slice(0,7))need(r.stat(before)[f]===oldDir.before[f],'SAME_PREPARED_DIRECTORY_IDENTITY');
 need(equal(fs.readdirSync(RAW).sort(),['stderr.raw','stdout.canonical.json']),'EXACT_TWO_CAPTURE_MEMBERS');
 let total=0;
 for(const name of ['stdout.canonical.json','stderr.raw']){
  const path=RAW+name,k={path,lstat_before:null,fd_before:null,fd_after:null,lstat_after:null,reads:[],byte_count:0,eof:false,closed:false,sha256:null};rawKeys.push(k);let fd=null;
  try{
   const s=fs.lstatSync(path,{bigint:true});k.lstat_before=r.stat(s);need(s.isFile()&&!s.isSymbolicLink()&&s.nlink===1n&&(s.mode&0o7777n)===0o600n&&s.uid===0n,'PHYSICAL_PRIVATE_SINGLE_LINK_RAW');
   need(s.size>=0n&&s.size<=268435456n,'EXPLICIT_RAW_BYTE_RECEPTION_BOUND_NO_SEMANTIC_CLAIM');
   fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);k.fd_before=r.stat(fs.fstatSync(fd,{bigint:true}));need(equal(k.fd_before,k.lstat_before),'RAW_SAME_FD_BEFORE');
   const h=crypto.createHash('sha256'),block=Buffer.alloc(65536);
   for(;;){const n=fs.readSync(fd,block,0,block.length,null);k.reads.push({requested:block.length,returned:n});need(Number.isSafeInteger(n)&&n>=0&&n<=block.length,'ACTUAL_RAW_READ_COUNT');if(n===0){k.eof=true;break;}h.update(block.subarray(0,n));k.byte_count+=n;total+=n;need(k.byte_count<=268435456&&total<=536870912,'FINITE_CLOSED_RAW_BYTES');}
   k.fd_after=r.stat(fs.fstatSync(fd,{bigint:true}));k.lstat_after=r.stat(fs.lstatSync(path,{bigint:true}));need(equal(k.fd_before,k.fd_after)&&equal(k.lstat_before,k.lstat_after),'ALL_FULL_RAW_KEY_FIELDS_STABLE');
   need(BigInt(k.byte_count)===s.size,'ACTUAL_COMPLETE_RAW_EOF_SIZE');k.sha256=h.digest('hex');
  }finally{if(fd!==null){fs.closeSync(fd);k.closed=true;}}
  need(k.eof&&k.closed,'ACTUAL_RAW_EOF_AND_CLOSE');
 }
 const after=fs.lstatSync(RAW,{bigint:true});need(equal(r.stat(before),r.stat(after)),'CAPTURE_DIRECTORY_STABLE_DURING_RECEPTION');
 report.capture_directory={path:RAW,before:r.stat(before),after:r.stat(after),members:['stderr.raw','stdout.canonical.json']};
 report.raw_total_bytes=total;report.raw_keys=rawKeys;report.prior_complete_keys_compared=pv.keys.length;
 report.status='PASS_COMPLETE_CLOSED_RAW_BYTES_ONLY_DATA_SOURCE_AND_SEMANTIC_RECEPTION_PENDING';
}catch(e){report.status='FAIL_RAW_BYTE_RECEPTION_PRESERVE_HOLD';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=r.checks;report.key_count=keys.size;report.total_document_read_bytes=r.total;report.keys=[...keys.values()];report.raw_keys=rawKeys;
process.stdout.write(JSON.stringify(report,null,2)+'\n');
