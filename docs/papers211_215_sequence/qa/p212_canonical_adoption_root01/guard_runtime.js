'use strict';
// Root forward guard, explicitly derived from the fully read accepted
// receive_discovery.js resolveLoose/pathState/current-configuration checks.
// Reads only the exact lock's file keys and bounded configuration memberships.
const fs=require('fs'),path=require('path'),a=require('assert').strict;
module.exports=function guard(lock,read){
  let checks=0;const ok=(v,l)=>{checks++;a(v,l)},eq=(x,y,l)=>{checks++;a.deepEqual(x,y,l)};
  const files={},config={paths:{},memberships:{},scope:lock.configuration.scope},loader={};
  function resolveLoose(input){let todo=input.split('/').filter(Boolean),done=[],links=0;while(todo.length){const n=todo.shift();if(n==='.')continue;if(n==='..'){done.pop();continue;}const p='/'+[...done,n].join('/');let s;try{s=fs.lstatSync(p);}catch(e){if(!['ENOENT','ENOTDIR'].includes(e.code))throw e;}if(s?.isSymbolicLink()){ok(++links<=40,'no symlink loop');const t=fs.readlinkSync(p);if(t.startsWith('/'))done=[];todo=t.split('/').filter(Boolean).concat(todo);}else done.push(n);}return '/'+done.join('/');}
  function state(p,withBytes){ok(path.isAbsolute(p)&&path.normalize(p)===p,'literal state path');let ls=null,st=null;try{ls=fs.lstatSync(p);}catch(e){if(!['ENOENT','ENOTDIR'].includes(e.code))throw e;}try{st=fs.statSync(p);}catch(e){if(!['ENOENT','ENOTDIR'].includes(e.code))throw e;}const v={lexists:ls!==null,exists:st!==null,is_file:!!st?.isFile(),is_dir:!!st?.isDirectory(),is_character_device:!!st?.isCharacterDevice(),resolved:resolveLoose(p),symlink:ls?.isSymbolicLink()?fs.readlinkSync(p):null};if(v.is_character_device){const d=BigInt(st.rdev);v.character_device={major:Number(((d>>8n)&0xfffn)|((d>>32n)&0xfffff000n)),minor:Number((d&0xffn)|((d>>12n)&0xffffff00n)),mode:st.mode};}if(withBytes&&v.is_file){const r=read(p);v.bytes=r.key.bytes;v.sha256=r.key.sha256;}return v;}
  eq(lock.format,'p212-bounded-runtime-lock-v1');eq(Object.keys(lock.files).length,130);
  for(const[p,k]of Object.entries(lock.files)){const r=read(p);eq(r.key,k,'whole current lexical/resolved runtime key');files[p]=r.key;}
  eq(new Set(Object.values(files).map(k=>k.resolved)).size,121);
  eq(Object.keys(lock.configuration.paths).length,69);eq(Object.keys(lock.configuration.memberships).length,5);
  for(const[p,k]of Object.entries(lock.configuration.paths)){const v=state(p,true);eq(v,k,'whole current configuration path');config.paths[p]=v;}
  let members=0;for(const[d,v]of Object.entries(lock.configuration.memberships)){const current={directory:state(d,false),members:{}};eq(current.directory,v.directory,'membership directory');eq(current.directory.is_dir?fs.readdirSync(d).sort():[],Object.keys(v.members).sort(),'whole direct membership');for(const[n,k]of Object.entries(v.members)){ok(path.basename(n)===n,'literal member');const s=state(d+'/'+n,false);eq(s,k,'whole member state');current.members[n]=s;members++;}config.memberships[d]=current;}eq(members,292);
  const lines=read('/etc/ld.so.conf').raw.toString().split('\n').map(x=>x.trim()).filter(x=>x&&!x.startsWith('#'));eq(lines,['include /etc/ld.so.conf.d/*.conf'],'single actual loader include');const names=new Set();for(const[p,k]of Object.entries(config.paths))if(path.dirname(p)==='/etc/ld.so.conf.d'&&k.is_file){for(const line of read(p).raw.toString().split('\n')){const t=line.split('#')[0].trim();if(!t)continue;ok(t.startsWith('/')&&!/[*?\[\]\t ]/.test(t),'bounded actual directive');names.add(t);}}
  eq([...names].sort(),Object.keys(lock.loader_search_directory_states).sort(),'all actual loader targets');eq(names.size,9);for(const[p,k]of Object.entries(lock.loader_search_directory_states)){const v=state(p,false);eq(v,k,'current loader state');loader[p]=v;}
  return {checks,files,configuration:config,loader_search_directory_states:loader,scope:'Fresh full accepted 130/121 file, 69 configuration, 5/292 membership and 9 loader states; no new probe/linkage or continuous tracing.'};
};
