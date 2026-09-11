'use strict';
// Receive the separately permitted exact source copy; no child process launch.
const fs=require('node:fs'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const Q='docs/papers211_215_sequence/qa/',M=Q+'p213_initial_science_materialization_root01/',E=Q+'p213_initial_science_enabled_root01/',P=Q+'p213_initial_science_enabled_preparation01/';
const source=P+'run_science.proposed.py.txt',dir=Q+'p213_initial_science_enabled01',target=dir+'/run_science.py';
const paths=[source,target,E+'RECEPTION.md',E+'SHA256SUMS',E+'READ_FIXED.cjs',E+'CHECK_NATIVE.json',M+'SCOPE.md',M+'CREATION_NATIVE.json',M+'CHECK_MATERIALIZATION.cjs'];
const r=make(new Set(paths)),{need,read,sha,stat,equal,keys}=r;
const report={scope:'ROOT_EXACT_WRAPPER_MATERIALIZATION_ONLY',status:'RUNNING',science_executed:false,run_granted:false,output_directories_queried:false};
try{
 need(process.argv.length===2&&process.cwd()==='/root/autodl-tmp/symbolic_dynamics','FIXED_NOARG_CONTEXT');
 for(const p of paths)read(p);
 need(sha(read(E+'RECEPTION.md'))==='eb0aaf832813de4b0ea194a1e49fe34f198986e891cfdde1b46923cab7963057','RECEIVED_EXACT_ENABLED_SOURCE');
 need(sha(read(E+'SHA256SUMS'))==='21021a4dc5ce6328ba5d7d4ea6929eef178e6dad55696f98f7129ecb67d39706','SOURCE_RECEIPT_SEAL');
 need(sha(read(E+'READ_FIXED.cjs'))==='f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7','EXACT_DOCUMENTARY_READER_SOURCE');
 const old=JSON.parse(JSON.parse(read(E+'CHECK_NATIVE.json')).result.output);
 need(equal(keys.get(source),old.keys.find(k=>k.path===source)),'UNCHANGED_COMPLETE_SOURCE_CARRIER_KEY');
 const d=fs.lstatSync(dir,{bigint:true});need(d.isDirectory()&&!d.isSymbolicLink()&&(d.mode&0o7777n)===0o700n&&d.uid===0n,'EXACT_0700_SOURCE_DIRECTORY');
 need(equal(fs.readdirSync(dir),['run_science.py']),'ONLY_EXACT_NEW_WRAPPER');
 const k=keys.get(target);need(BigInt(k.fd_before.mode)===0o100600n&&k.fd_before.nlink==='1'&&k.fd_before.uid==='0','EXACT_0600_REGULAR_SINGLE_LINK_SOURCE');
 const a=read(source),b=read(target);need(a.length===108715&&sha(a)==='87cd4409bf5394792f66318893cc9e187ff43c1419bcfd819f17f874cdb7c121','EXACT_SOURCE_PIN');
 need(a.equals(b),'COMPLETE_CURRENT_SOURCE_DESTINATION_RAW_EQUAL');
 const creation=JSON.parse(read(M+'CREATION_NATIVE.json'));
 need(creation.exec_entries.length===4,'FOUR_ACTUAL_NATIVE_CREATION_RECORDS');
 const chunks=['1c2e5f','1c00c2','2200af','862096'];
 for(let i=0;i<4;i++)need(creation.exec_entries[i].result.exit_code===0&&creation.exec_entries[i].result.chunk_id===chunks[i],'ACTUAL_CREATION_NATIVE_STATUS');
 const copyInput=JSON.parse(creation.exec_entries[2].result.output);
 need(Buffer.from(copyInput.text,'utf8').equals(a)&&equal(copyInput.source_key,keys.get(source)),'COMPLETE_ACTUAL_SOURCE_TRANSFER_AND_KEY');
 const patch=creation.apply_patch;need(patch.tool==='apply_patch'&&equal(patch.result,{}),'ACTUAL_PATCH_EVENT_NO_FALSE_RETURN_ATTESTATION');
 const lines=patch.request.split('\n');need(lines.shift()==='*** Begin Patch'&&lines.shift()==='*** Add File: '+target&&lines.pop()==='*** End Patch','EXACT_SOURCE_PATCH_TARGET');
 need(lines.every(s=>s.startsWith('+')),'ONLY_LITERAL_ADDITION');
 need(Buffer.from(lines.map(s=>s.slice(1)).join('\n')+'\n').equals(b),'ALL_ACTUAL_PATCH_BODY_RAW_BYTES');
 const after=fs.lstatSync(dir,{bigint:true});need(equal(stat(d),stat(after)),'UNCHANGED_DIRECTORY_POINT_RECORD');
 report.materialized_source_key=k;report.documentary_source_key=keys.get(source);report.directory={path:dir,before:stat(d),after:stat(after)};
 report.raw_equal=true;report.source_bytes=b.length;report.source_sha256=sha(b);report.source_line_count=b.reduce((n,c)=>n+(c===10),0);
 report.status='PASS_EXACT_SOURCE_MATERIALIZATION_NOT_RUN';
}catch(e){report.status='FAIL_EXACT_SOURCE_MATERIALIZATION_NOT_RUN';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=r.checks;report.key_count=keys.size;report.total_read_bytes=r.total;report.keys=[...keys.values()];
process.stdout.write(JSON.stringify(report,null,2)+'\n');
