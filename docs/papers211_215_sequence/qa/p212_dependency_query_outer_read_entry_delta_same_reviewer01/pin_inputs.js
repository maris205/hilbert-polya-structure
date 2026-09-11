'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const paths=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const stat=s=>Object.fromEntries(F.map(k=>{if(typeof s[k]!=='bigint')throw Error('all14 integer fields');return [k,String(s[k])];}));
const inputs=paths.map(p=>{if(typeof p!=='string'||p.startsWith('/')||p.split('/').some(x=>!x||x==='.'||x==='..'))throw Error('workspace path');const q=path.join(ROOT,p),l=fs.lstatSync(q,{bigint:true}),s=fs.statSync(q,{bigint:true});if(!l.isFile()||!s.isFile())throw Error('physical file');const raw=fs.readFileSync(q);return{path:p,resolved:fs.realpathSync(q),bytes:raw.length,sha256:crypto.createHash('sha256').update(raw).digest('hex'),lstat:stat(l),stat:stat(s)};});
process.stdout.write(JSON.stringify({schema:'p212-outer-documentary-delta-finite-key-v1',scope:'Whole finite workspace inputs; all14 lstat/stat integer fields; later stability excludes atime only; no host runtime or execution claim.',inputs},null,2)+'\n');
