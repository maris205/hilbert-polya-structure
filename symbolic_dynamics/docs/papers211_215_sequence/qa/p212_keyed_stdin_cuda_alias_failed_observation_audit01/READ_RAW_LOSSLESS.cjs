'use strict';
// Documentary raw-data projection. Only the two explicitly granted capture files
// and their one exact directory are filesystem operands. Captured paths are data.
const fs = require('fs'), crypto = require('crypto'), assert = require('assert/strict');
const { parseCanonical } = require('./JSON_LOSSLESS.cjs');
const C = '/root/symbolic-dynamics-p212-cuda-alias-observation-20260910-01';
const names = ['stderr.raw', 'stdout.raw'];
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const stableFields = fields.filter(f => f !== 'atimeNs');
let checks = 0;
const eq = (a,b,m) => { checks++; assert.deepStrictEqual(a,b,m); };
const ok = (a,m) => { checks++; assert(a,m); };
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const meta = s => Object.fromEntries(fields.map(f => [f,String(s[f])]));
const stable = (a,b) => eq(Object.fromEntries(stableFields.map(f=>[f,a[f]])),Object.fromEntries(stableFields.map(f=>[f,b[f]])));
function read(name) {
  ok(names.includes(name), 'fixed captured basename');
  const path = C + '/' + name, before = fs.lstatSync(path,{bigint:true});
  ok(before.isFile() && before.nlink===1n && before.uid===0n && before.gid===0n && (before.mode&4095n)===384n);
  ok(before.size <= 134217728n);
  const fd = fs.openSync(path, fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let raw, start, end;
  try {
    start = meta(fs.fstatSync(fd,{bigint:true})); stable(meta(before),start);
    raw = fs.readFileSync(fd); end = meta(fs.fstatSync(fd,{bigint:true})); stable(start,end);
  } finally { fs.closeSync(fd); }
  const pathEnd = meta(fs.lstatSync(path,{bigint:true})); stable(end,pathEnd);
  eq(BigInt(raw.length), before.size);
  return {raw,key:{path,bytes:raw.length,sha256:sha(raw),path_before:meta(before),fd_before:start,fd_end:end,path_end:pathEnd,full_eof:true,leaf_links:1}};
}
const d = fs.lstatSync(C,{bigint:true});
ok(d.isDirectory() && d.uid===0n && d.gid===0n && (d.mode&4095n)===448n);
const dfd=fs.openSync(C,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_DIRECTORY|fs.constants.O_NONBLOCK);
let dstart,dend;
try {
  dstart=meta(fs.fstatSync(dfd,{bigint:true}));stable(meta(d),dstart);
  eq(fs.readdirSync(C).sort(),names);
  const stderr=read('stderr.raw'),stdout=read('stdout.raw');
  eq([stderr.key.bytes,stderr.key.sha256],[0,'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855']);
  eq([stdout.key.bytes,stdout.key.sha256],[7868291,'7b57c2f186676b8bfa7b7473a38a0140b1f1013f93e652c5dc22015602675da3']);
  const parsed=parseCanonical(stdout.raw),v=parsed.value;
  const counts={};
  for(const row of v.native_events) counts[row.status]=(counts[row.status]||0)+1;
  const operations={};
  for(const row of v.path_events) operations[row.operation]=(operations[row.operation]||0)+1;
  const passes=v.passes.map(p=>({number:p.number,targets:p.targets.map((r,i)=>({
    index:i,path:r.target.path,mode:r.target.mode,status:r.status,
    resolved:r.before?r.before.resolved:null,content:r.content?{bytes:r.content.bytes,sha256:r.content.sha256,captured:r.content.raw_hex!==null}:null,
    members:r.members?r.members.length:null,error_type:r.error_type||null,error_message:r.error_message||null,first_event:r.first_event===undefined?null:r.first_event
  }))}));
  const endStdout=read('stdout.raw'),endStderr=read('stderr.raw');
  eq(endStdout.raw,stdout.raw);eq(endStderr.raw,stderr.raw);
  stable(stdout.key.path_end,endStdout.key.path_end);stable(stderr.key.path_end,endStderr.key.path_end);
  dend=meta(fs.fstatSync(dfd,{bigint:true}));stable(dstart,dend);
  const dpath=meta(fs.lstatSync(C,{bigint:true}));stable(dend,dpath);
  eq(fs.readdirSync(C).sort(),names);
  process.stdout.write(JSON.stringify({
    scope:'PERSONAL_NONCONTRIBUTOR_DATA_ONLY_REVIEW_WITH_SOURCE_AUTHOR_PARENT_DISCLOSED',
    checks,canonical_full_raw_equality:true,parse_counts:parsed.counts,
    directory:{path:C,path_before:meta(d),fd_before:dstart,fd_end:dend,path_end:dpath,members:names},
    raw_keys:[stdout.key,stderr.key],closing_raw_keys:[endStdout.key,endStderr.key],
    schema:v.schema,status:v.status,provenance:v.provenance,
    observer_bootstrap_attested:v.observer_bootstrap_attested,author_probe_executed:v.author_probe_executed,closure_certified:v.closure_certified,
    controls:v.controls.map(r=>({role:r.role,path:r.observation.target.path,content:{bytes:r.observation.content.bytes,sha256:r.observation.content.sha256}})),
    closing_controls:v.closing_controls,passes,errors:v.errors,closure_gaps:v.closure_gaps,
    native_count:v.native_events.length,native_status_counts:counts,path_event_count:v.path_events.length,path_operation_counts:operations,
    tail_native_events:v.native_events.slice(-18),tail_path_events:v.path_events.slice(-12),
    actual_read_bytes:v.actual_read_bytes,actual_captured_bytes:v.actual_captured_bytes,
    runtime_accepted:false,operational_authorization:false
  },null,2)+'\n');
} finally {fs.closeSync(dfd);}
