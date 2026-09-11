'use strict';
const fs = require('node:fs'), path = require('node:path'), crypto = require('node:crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
function abs(p) { if (typeof p !== 'string' || p.startsWith('/') || p.split('/').includes('..')) throw Error('scope'); return path.join(ROOT,p); }
function sha(b) { return crypto.createHash('sha256').update(b).digest('hex'); }
function stat(s) { const o={}; for(const k of ['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs']) o[k]=String(s[k]); return o; }
function pin(p) { const a=abs(p),l=fs.lstatSync(a,{bigint:true}),s=fs.statSync(a,{bigint:true}); if(!s.isFile()) throw Error('not file '+p); const b=fs.readFileSync(a); return {path:p,realpath:fs.realpathSync(a),lstat:stat(l),stat:stat(s),size:b.length,sha256:sha(b)}; }
const [mode,list] = process.argv.slice(2), paths = JSON.parse(fs.readFileSync(abs(list),'utf8'));
if(mode==='pins') process.stdout.write(JSON.stringify({schema:'p212-execution-amendment-audit-rich-pins-v1',scope:'documentary finite observations; not runtime capture',inputs:paths.map(pin)},null,2)+'\n');
else if(mode==='read') { const records=[]; for(const p of paths) { const before=pin(p),b=fs.readFileSync(abs(p)),after=pin(p); if(JSON.stringify(before)!==JSON.stringify(after)||before.sha256!==sha(b)) throw Error('drift '+p); records.push({before,text:b.toString('utf8'),after}); } process.stdout.write(JSON.stringify({schema:'p212-execution-amendment-audit-full-text-reads-v1',records},null,2)+'\n'); }
else throw Error('mode');
