'use strict';
// Reads an archival JSON transcript as data. No contained command is executed.
const fs = require('fs');
const crypto = require('crypto');
const rel = 'docs/papers211_215_sequence/qa/private_checkpoint_d01_preparation01/DOCUMENT_READS_NATIVE.json';
const root = '/root/autodl-tmp/symbolic_dynamics/';
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta = s => Object.fromEntries(fields.map(k=>[k,s[k].toString()]));
const need = (ok,s) => { if(!ok) throw Error(s); };
const first = Number(process.argv[2]), last = Number(process.argv[3]);
need(process.argv.length===4 && Number.isInteger(first) && Number.isInteger(last)
  && first>=0 && last>=first && last<=10, 'Documentary record bounds');
const before = fs.lstatSync(root+rel,{bigint:true});
need(before.isFile()&&!before.isSymbolicLink(), 'Physical archival document only');
const fd = fs.openSync(root+rel,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
try {
  const opened=fs.fstatSync(fd,{bigint:true}), bytes=fs.readFileSync(fd);
  const ended=fs.fstatSync(fd,{bigint:true}), after=fs.lstatSync(root+rel,{bigint:true});
  need([opened,ended,after].every(s=>JSON.stringify(meta(s))===JSON.stringify(meta(before)))
    && BigInt(bytes.length)===before.size,'Document changed while read');
  const digest=crypto.createHash('sha256').update(bytes).digest('hex');
  need(digest==='d9d84959e0a60a577af119f258748bc4d63fcc610c45bdff84a0a9c0f73e21cd'
    &&bytes.length===70170,'Expected whole archival document');
  const x=JSON.parse(bytes.toString('utf8'));
  need(x.records.length===10,'Expected ten records');
  process.stdout.write(JSON.stringify({
    documentary_only:true,path:rel,whole_bytes:bytes.length,whole_sha256:digest,
    metadata:meta(before),schema:x.schema,exhaustive_transcript:x.exhaustive_transcript,
    selected_records_start_inclusive:first,selected_records_end_exclusive:last,
    records:x.records.slice(first,last)
  },null,2)+'\n');
} finally { fs.closeSync(fd); }

