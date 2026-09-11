'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const FIELDS=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const paths=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const stat=s=>Object.fromEntries(FIELDS.map(k=>[k,String(s[k])]));
const pin=p=>{if(typeof p!=='string'||p.startsWith('/')||p.split('/').includes('..'))throw Error('workspace relative');const a=path.join(ROOT,p),l=fs.lstatSync(a,{bigint:true}),s=fs.statSync(a,{bigint:true});if(!s.isFile())throw Error('nonfile');const b=fs.readFileSync(a);return{path:p,resolved:fs.realpathSync(a),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex'),lstat:stat(l),stat:stat(s)};};
process.stdout.write(JSON.stringify({schema:'p212-outer-source-audit-finite-workspace-key-v1',scope:'All14 integer fields recorded; atime alone excluded from later stability. No runtime capture or continuous path-race claim.',inputs:paths.map(pin)},null,2)+'\n');
