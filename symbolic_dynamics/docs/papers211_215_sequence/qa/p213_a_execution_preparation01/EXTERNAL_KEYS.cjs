'use strict';
// Proposed external fixed-file keys only. Never starts Python or reads /proc.
// Invocation still needs root's separate acceptance and operation grant.
const fs = require('node:fs'), crypto = require('node:crypto');
const BASE = '/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/';
const PREP = BASE + 'p213_a_execution_preparation01/';
const SHA = b => crypto.createHash('sha256').update(b).digest('hex');
const stat = s => Object.fromEntries(['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'].map(n => [n, s[n].toString()]));
const equal = (a,b) => JSON.stringify(a) === JSON.stringify(b);
const requireTrue = (v,m) => { if (!v) throw Error(m); };
const records = [];
let total = 0;
let totalLimit = 16777216;
function key(spec, bound) {
  const r = {path:spec.path, kind:spec.kind, complete:false, eof:false, close_succeeded:false};
  records.push(r);
  let fd = null;
  try {
    if (spec.kind === 'required-absence') {
      try { fs.lstatSync(spec.path,{bigint:true}); throw Error('required absent path exists'); }
      catch (e) { if (e.code !== 'ENOENT') throw e; r.absence = {operation:'lstat',code:'ENOENT',path:spec.path}; }
      r.complete = true; return r;
    }
    const a = fs.lstatSync(spec.path,{bigint:true});
    requireTrue(a.isFile() && !a.isSymbolicLink(), 'not a regular no-link leaf');
    requireTrue(a.size <= BigInt(bound), 'input/output exceeds accepted byte bound');
    if (spec.single_link) requireTrue(a.nlink===1n, 'output must have a single link');
    r.begin = stat(a);
    fd = fs.openSync(spec.path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
    const b = fs.fstatSync(fd,{bigint:true}); r.fd_before = stat(b);
    requireTrue(equal(r.begin,r.fd_before), 'endpoint/fd mismatch');
    const h = crypto.createHash('sha256'), chunk = Buffer.alloc(65536);
    let size = 0;
    for (;;) {
      const n = fs.readSync(fd,chunk,0,Math.min(chunk.length,bound-size+1,totalLimit-total+1),null);
      if (n === 0) { r.eof = true; break; }
      size += n; total += n; h.update(chunk.subarray(0,n));
      requireTrue(size <= bound, 'read bound exceeded');
      requireTrue(total <= totalLimit, 'total read bound exceeded');
    }
    r.bytes = size; r.sha256 = h.digest('hex');
    r.fd_after = stat(fs.fstatSync(fd,{bigint:true}));
    fs.closeSync(fd); fd = null; r.close_succeeded = true;
    r.end = stat(fs.lstatSync(spec.path,{bigint:true}));
    requireTrue(equal(r.begin,r.fd_before)&&equal(r.fd_before,r.fd_after)&&equal(r.fd_after,r.end), 'full key changed while reading');
    requireTrue(BigInt(size)===a.size, 'EOF byte count differs from size');
    if (spec.bytes !== undefined) requireTrue(size===spec.bytes, 'expected byte count changed');
    if (spec.sha256 !== undefined) requireTrue(r.sha256===spec.sha256, 'expected input bytes changed');
    r.complete = true; return r;
  } catch (e) {
    r.failure = {message:e.message,code:e.code||null};
    if (fd !== null) { try { fs.closeSync(fd); r.close_succeeded=true; } catch (c) { r.close_failure={message:c.message,code:c.code||null}; } }
    throw e;
  }
}
const report = {schema:'P213_A_EXTERNAL_KEYS_V1',mode:null,scope:'fixed external before/after file observations; ordinary bootstrap and pathname traversal trusted; no own-Python process observer',records};
try {
  const [mode,stage,...extra]=process.argv.slice(2);
  report.mode=mode;
  requireTrue(extra.length===0 && ['inputs','outputs'].includes(mode), 'unsupported arguments');
  const raw=fs.readFileSync(PREP+'DEPENDENCIES.proposed.json');
  requireTrue(SHA(raw)==='23cf1daad6b0873cc703ecf7e726e588ec08affb9de35910ecb59db42af11979', 'dependency document changed');
  const deps=JSON.parse(raw.toString('utf8'));
  if (mode==='inputs') {
    requireTrue(stage===undefined && deps.inputs.length===20, 'wrong input key invocation');
    for (const x of deps.inputs) key(x,deps.limits.individual_input_bytes);
    requireTrue(total<=deps.limits.total_present_input_bytes, 'total input byte bound exceeded');
  } else {
    const dirs={initial:'p213_a_initial_run01',strict01:'p213_a_strict_pair_run01',strict02:'p213_a_strict_pair_run02'};
    requireTrue(Object.hasOwn(dirs,stage), 'unknown fixed output stage');
    const out=BASE+dirs[stage]+'/';
    key({path:out+'stdout.bin',kind:'regular-file',single_link:true},deps.limits.stdout_success_bytes);
    key({path:out+'stderr.bin',kind:'regular-file',single_link:true},deps.limits.failed_stream_hash_bytes);
    key({path:out+'python.exit',kind:'regular-file',single_link:true},32);
  }
  report.total_read_bytes=total;
  report.status='COMPLETE_EXTERNAL_KEYS_PENDING_RECEPTION';
  console.log(JSON.stringify(report,null,2));
} catch (e) {
  report.total_read_bytes=total; report.status='HOLD_EXTERNAL_KEY_FAILURE'; report.failure={message:e.message,code:e.code||null};
  console.log(JSON.stringify(report,null,2)); process.exitCode=78;
}
