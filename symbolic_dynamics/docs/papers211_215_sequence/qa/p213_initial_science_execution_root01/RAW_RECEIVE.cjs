'use strict';
// Exact closed raw artifacts from aa582c only. No runtime/host/source execution.
const fs=require('node:fs'),crypto=require('node:crypto');
const {parseIntegerJSON,canonicalIntegerJSON}=require('../p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs');
const BASE='docs/papers211_215_sequence/qa/p213_initial_science_run01/';
const specs=[{name:'stdout.bin',max:67108864},{name:'stderr.bin',max:16777216},{name:'runtime_control.bin',max:16777216}];
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const stat=s=>Object.fromEntries(fields.map(k=>[k,s[k].toString()]));
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const keys=[],buffers=new Map();let checks=0,total=0;
function need(v,m){checks++;if(!v)throw Error(m);}
function read(s){
 const path=BASE+s.name,k={path,eof:false,byte_count:0,complete:false,closed:false};keys.push(k);let fd=null;
 try{
  const first=fs.lstatSync(path,{bigint:true});k.lstat_before=stat(first);
  need(first.isFile()&&!first.isSymbolicLink()&&first.nlink===1n&&(first.mode&0o7777n)===0o600n,'REGULAR_SINGLE_LINK_0600_CAPTURE');
  need(first.size>=0n&&first.size<=BigInt(s.max),'DECLARED_CAPTURE_BOUND');
  fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);k.fd_before=stat(fs.fstatSync(fd,{bigint:true}));
  need(equal(k.lstat_before,k.fd_before),'ENDPOINT_FD_BEFORE');
  const blocks=[],block=Buffer.alloc(65536);
  for(;;){const n=fs.readSync(fd,block,0,block.length,null);need(Number.isInteger(n)&&n>=0&&n<=block.length,'NATIVE_READ_COUNT');if(n===0){k.eof=true;k.eof_zero_return=0;break;}blocks.push(Buffer.from(block.subarray(0,n)));k.byte_count+=n;total+=n;need(k.byte_count<=s.max&&total<=100663296,'FINITE_RAW_READ_BOUNDS');}
  k.fd_after=stat(fs.fstatSync(fd,{bigint:true}));k.lstat_after=stat(fs.lstatSync(path,{bigint:true}));
  need(equal(k.fd_before,k.fd_after)&&equal(k.lstat_before,k.lstat_after),'UNCHANGED_FULL_CURRENT_CAPTURE_KEY');
  const b=Buffer.concat(blocks);need(BigInt(b.length)===first.size&&b.length===k.byte_count,'WHOLE_ACTUAL_EOF_SIZE');k.sha256=sha(b);
  fs.closeSync(fd);fd=null;k.closed=true;k.complete=true;buffers.set(s.name,b);return b;
 }catch(e){k.failure={name:e.name,code:e.code||null,message:e.message};throw e;}
 finally{if(fd!==null){fs.closeSync(fd);k.closed=true;}}
}
const report={scope:'ROOT_INITIAL_RAW_BYTE_CAPTURE_ONLY_PENDING_FULL_INDEPENDENT_SCIENCE_CONTROL_RECEPTION',status:'RUNNING',science_accepted:false,canonical_adopted:false,strict_pair_complete:false,no_science_rerun:true};
try{
 need(process.argv.length===2&&process.cwd()==='/root/autodl-tmp/symbolic_dynamics','FIXED_NOARG_CONTEXT');
 const dir=fs.lstatSync(BASE,{bigint:true});need(dir.isDirectory()&&!dir.isSymbolicLink()&&(dir.mode&0o7777n)===0o700n&&dir.uid===0n,'EXACT_0700_CAPTURE_DIRECTORY');
 need(equal(fs.readdirSync(BASE).sort(),specs.map(s=>s.name).sort()),'EXACT_THREE_RAW_FILES');
 for(const s of specs)read(s);
 need(buffers.get('stderr.bin').length===0,'EMPTY_SUCCESS_STDERR');
 const out=buffers.get('stdout.bin'),control=buffers.get('runtime_control.bin');
 need(out.length>0&&out.every(c=>c<128)&&out.at(-1)===10,'COMPLETE_ASCII_SCIENCE_FRAMING_ONLY');
 need(control.every(c=>c<128)&&control.at(-1)===10,'ASCII_INTEGER_CONTROL');
 const parsed=parseIntegerJSON(control.toString('ascii')),d=parsed.data;
 const reconstructed=Buffer.from(canonicalIntegerJSON(d)+'\n','ascii');
 need(reconstructed.equals(control),'ENTIRE_LOSSLESS_INTEGER_CONTROL_RAW_ROUNDTRIP');
 report.control_integer_counts=parsed.counts;report.control_top_level_fields=Object.keys(d);
 report.control_status=d.status;report.control_science_fields=Object.keys(d.science||{});
 report.reported_science_progress=Object.fromEntries(Object.entries(d.science||{}).filter(([k,v])=>typeof v==='boolean'||v===null||typeof v==='string'));
 report.before_file_entry_count=Object.keys(d.before_keys||{}).length;report.after_file_entry_count=Object.keys(d.after_keys||{}).length;
 report.actual_output_line_count=out.reduce((n,c)=>n+(c===10),0);
 const lines=out.toString('ascii').split('\n');report.actual_first_lines=lines.slice(0,4);report.actual_last_lines=lines.slice(-4,-1);
 report.capture_directory={path:BASE,metadata:stat(dir)};
 report.status='PASS_COMPLETE_RAW_BYTES_ONLY_NOT_SCIENTIFIC_ACCEPTANCE';
}catch(e){report.status='FAIL_INITIAL_RAW_CAPTURE_HOLD';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=checks;report.key_count=keys.length;report.total_read_bytes=total;report.keys=keys;
process.stdout.write(JSON.stringify(report,null,2)+'\n');
