'use strict';
// One scoped physical artifact preparation; no reviewed source or host query.
const fs=require('node:fs'),crypto=require('node:crypto');
const directory='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_keyed_stdin_input01';
const file=directory+'/empty.stdin';
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const metadata=s=>Object.fromEntries(fields.map(f=>[f,String(s[f])]));
const result={scope:'PHYSICAL_EMPTY_REGULAR_INPUT_PREPARATION_ONLY',directory,file,events:[],status:'HOLD',native_fourteen_field_observed:false,observer_executed:false};
let fd=null;
function need(v,m){if(!v)throw new Error(m);}
try{
 for(const path of [directory,file]){
  let absent=false;
  try{const s=fs.lstatSync(path,{bigint:true});result.events.push({operation:'initial_lstat',path,metadata:metadata(s),exists:true});}
  catch(e){result.events.push({operation:'initial_lstat',path,error:{code:e.code,errno:e.errno,syscall:e.syscall}});if(e.code!=='ENOENT')throw e;absent=true;}
  need(absent,'selected input target already exists; no replacement');
 }
 fs.mkdirSync(directory,{mode:0o700});result.events.push({operation:'exclusive_nonrecursive_mkdir',path:directory});
 fs.chmodSync(directory,0o700);result.events.push({operation:'chmod_new_directory',mode:'0700'});
 const d=fs.lstatSync(directory,{bigint:true});need(d.isDirectory()&&!d.isSymbolicLink()&&(d.mode&0o777n)===0o700n,'private new directory');
 fd=fs.openSync(file,fs.constants.O_CREAT|fs.constants.O_EXCL|fs.constants.O_NOFOLLOW|fs.constants.O_RDONLY,0o600);
 result.events.push({operation:'exclusive_create_no_write',path:file});
 fs.fchmodSync(fd,0o600);
 const first=fs.fstatSync(fd,{bigint:true});need(first.isFile()&&first.size===0n&&first.nlink===1n&&(first.mode&0o777n)===0o600n,'empty private regular new file');
 const before=metadata(first);need(JSON.stringify(metadata(fs.lstatSync(file,{bigint:true})))===JSON.stringify(before),'initial path/fd equality');
 const sentinel=Buffer.alloc(1),count=fs.readSync(fd,sentinel,0,1,null);
 result.events.push({operation:'new_fd_current_position_read',requested_bytes:1,returned_bytes:count,raw_hex:sentinel.subarray(0,count).toString('hex')});
 need(count===0,'actual EOF on newly created empty input');const bytes=Buffer.alloc(0);
 const after=metadata(fs.fstatSync(fd,{bigint:true}));need(JSON.stringify(after)===JSON.stringify(before),'same fd unchanged');
 need(JSON.stringify(metadata(fs.lstatSync(file,{bigint:true})))===JSON.stringify(before),'closing path/fd equality');
 fs.closeSync(fd);fd=null;
 const finalDirectory=fs.lstatSync(directory,{bigint:true});need(finalDirectory.isDirectory()&&!finalDirectory.isSymbolicLink()&&(finalDirectory.mode&0o777n)===0o700n,'closing private directory');
 need(JSON.stringify(fs.readdirSync(directory))===JSON.stringify(['empty.stdin']),'only selected created leaf');
 result.input={path:file,bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex'),metadata:before};
 result.directory_metadata=metadata(finalDirectory);result.status='PREPARED_PENDING_ACTUAL_NATIVE_OBSERVATION';
}catch(e){result.failure={name:e.name,code:e.code||null,errno:e.errno??null,syscall:e.syscall||null,message:e.message};}
finally{if(fd!==null){try{fs.closeSync(fd);}catch(e){result.status='HOLD';result.close_failure={name:e.name,code:e.code||null,errno:e.errno??null};}}}
process.stdout.write(JSON.stringify(result,null,2)+'\n');
process.exitCode=result.status==='PREPARED_PENDING_ACTUAL_NATIVE_OBSERVATION'?0:78;
