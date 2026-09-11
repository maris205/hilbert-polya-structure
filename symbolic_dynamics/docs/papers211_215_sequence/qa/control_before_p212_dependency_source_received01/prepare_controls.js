'use strict';
const fs=require('node:fs'),c=require('node:crypto'),a=require('node:assert/strict');
const root='/root/autodl-tmp/symbolic_dynamics';
const out=root+'/docs/papers211_215_sequence/qa/control_before_p212_dependency_source_received01/';
const names=[['SYMBOLIC_DYNAMICS_STATE.md','STATE.before.md','81b03a8e002f7ab46cc8efaced8e6843b172505dfc5993361b610d8913a53a88'],['docs/papers211_215_sequence/PIPELINE_STATE.md','PIPELINE.before.md','5f5b586d452c3dfb9eecc349bcfb91a96ad08182d38b028bcb311fd1638753c1']];
const pin=b=>({bytes:b.length,sha256:c.createHash('sha256').update(b).digest('hex')});
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const stat=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const stable=s=>Object.fromEntries(Object.entries(s).filter(([k])=>k!=='atimeNs'));
const files=[];
for(const [rel,dest,expected]of names){
 const p=root+'/'+rel;a.ok(fs.lstatSync(p).isFile());a.equal(fs.realpathSync(p),p);
 const before=stat(fs.statSync(p,{bigint:true})),b=fs.readFileSync(p);a.equal(pin(b).sha256,expected);
 fs.copyFileSync(p,out+dest,fs.constants.COPYFILE_EXCL);
 const copy=fs.readFileSync(out+dest),after=stat(fs.statSync(p,{bigint:true}));a.deepEqual(copy,b);a.deepEqual(fs.readFileSync(p),b);a.deepEqual(stable(before),stable(after));
 files.push({original_path:rel,original_pin:pin(b),original_before:before,original_after:after,physical_copy_path:out.slice(root.length+1)+dest,copy_pin:pin(copy),copy_stat:stat(fs.statSync(out+dest,{bigint:true})),raw_buffer_equal:true});
}
process.stdout.write(JSON.stringify({schema:'p212-dependency-source-milestone-control-before-physical-v1',scope:'Exactly two previous documentary controls; no scientific/dependency remapping',files,manuscript_changes:0,science:0,host_queries:0,builds:0,Git:0,external:'HOLD_EXTERNAL'},null,2)+'\n');
