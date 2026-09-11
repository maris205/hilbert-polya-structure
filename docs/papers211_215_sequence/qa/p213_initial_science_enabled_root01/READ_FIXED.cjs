'use strict';
// Ordinary-trust documentary reader only. Caller supplies an explicit finite set.
// No operational target strings, imports, code parsing or execution are inferred.
const fs = require('node:fs'), crypto = require('node:crypto');
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const stat = s => Object.fromEntries(fields.map(f => [f, s[f].toString()]));
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const equal = (a,b) => JSON.stringify(a) === JSON.stringify(b);
module.exports = function makeReader(allowed) {
  const keys = new Map(), buffers = new Map();
  let checks = 0, total = 0;
  function need(ok, label) { checks++; if (!ok) throw new Error(label); }
  function read(path) {
    need(allowed.has(path), 'FIXED_DOCUMENT_ALLOWLIST ' + path);
    if (buffers.has(path)) return buffers.get(path);
    const key = {path, eof:false, byte_count:0, complete:false, closed:false};
    keys.set(path,key); let fd = null;
    try {
      const before = fs.lstatSync(path, {bigint:true});
      key.lstat_before = stat(before);
      need(before.isFile() && !before.isSymbolicLink(), 'REGULAR_NOFOLLOW_DOCUMENT');
      need(before.size >= 0n && before.size <= 16777216n, 'PER_DOCUMENT_BOUND');
      fd = fs.openSync(path, fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
      key.fd_before = stat(fs.fstatSync(fd,{bigint:true}));
      need(equal(key.lstat_before,key.fd_before), 'ENDPOINT_FD_BEFORE');
      const chunks = [], block = Buffer.alloc(65536);
      for (;;) {
        const count = fs.readSync(fd,block,0,block.length,null);
        need(Number.isInteger(count) && count >= 0 && count <= block.length,'READ_COUNT');
        if (count === 0) { key.eof = true; key.eof_zero_return = 0; break; }
        key.byte_count += count; total += count;
        chunks.push(Buffer.from(block.subarray(0,count)));
        need(key.byte_count <= 16777216 && total <= 134217728,'FINITE_DOCUMENT_BYTES');
      }
      key.fd_after = stat(fs.fstatSync(fd,{bigint:true}));
      key.lstat_after = stat(fs.lstatSync(path,{bigint:true}));
      need(equal(key.fd_before,key.fd_after) && equal(key.lstat_before,key.lstat_after),'FULL_BEFORE_AFTER_KEY');
      need(BigInt(key.byte_count) === before.size,'COMPLETE_SIZE');
      const buffer = Buffer.concat(chunks);
      need(buffer.length === key.byte_count,'CAPTURED_LENGTH');
      need(Buffer.from(buffer.toString('utf8'),'utf8').equals(buffer),'WHOLE_UTF8_REVERSIBLE');
      key.sha256 = sha(buffer);
      fs.closeSync(fd); fd = null; key.closed = true; key.complete = true;
      buffers.set(path,buffer); return buffer;
    } catch (e) {
      key.failure = {name:e.name,code:e.code || null,message:e.message}; throw e;
    } finally {
      if (fd !== null) {
        try { fs.closeSync(fd); key.closed = true; }
        catch (e) { key.close_failure = {name:e.name,code:e.code || null,message:e.message}; throw e; }
      }
    }
  }
  return {need,read,keys,buffers,sha,equal,stat,fields,
    get checks(){return checks;},get total(){return total;}};
};
