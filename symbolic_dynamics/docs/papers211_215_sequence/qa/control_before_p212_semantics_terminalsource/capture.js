'use strict';
// Preserve the exact two current navigation originals before a milestone edit.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),a=require('assert/strict'),cp=require('child_process');
const ROOT='/root/autodl-tmp/symbolic_dynamics',OWN=ROOT+'/docs/papers211_215_sequence/qa/control_before_p212_semantics_terminalsource';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
const names=['docs/papers211_215_sequence/PIPELINE_STATE.md','SYMBOLIC_DYNAMICS_STATE.md'];
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
const before=Object.fromEntries(names.map(n=>[n,pin(fs.readFileSync(ROOT+'/'+n))]));
a.ok(!fs.existsSync(OWN+'/originals'));fs.mkdirSync(OWN+'/originals',{mode:0o700});
const records=[],mapping=[];
for(const [i,n]of names.entries()){
  const source=ROOT+'/'+n,target=OWN+'/originals/'+path.basename(n);
  for(const [role,argv]of [['copy',['/usr/bin/cp','--no-clobber','--',source,target]],['compare',['/usr/bin/cmp','--',source,target]]]){
    const r=cp.spawnSync(argv[0],argv.slice(1),{cwd:ROOT,env:ENV,timeout:30000,maxBuffer:1024*1024});
    const receipt={argv,cwd:ROOT,environment:ENV,exit_code:r.status,signal:r.signal,error:r.error?String(r.error):null,stdout:pin(r.stdout||Buffer.alloc(0)),stderr:pin(r.stderr||Buffer.alloc(0))};
    fs.writeFileSync(OWN+'/'+i+'_'+role+'.stdout.raw',r.stdout||Buffer.alloc(0),{flag:'wx'});fs.writeFileSync(OWN+'/'+i+'_'+role+'.stderr.raw',r.stderr||Buffer.alloc(0),{flag:'wx'});records.push(receipt);
    fs.writeFileSync(OWN+'/'+i+'_'+role+'.NATIVE.json',JSON.stringify(receipt,null,2)+'\n',{flag:'wx'});a.equal(r.status,0);a.equal(r.signal,null);a.ok(!r.error);a.equal(r.stderr.length,0);a.equal(r.stdout.length,0);
  }
  a.deepEqual(pin(fs.readFileSync(source)),before[n]);a.deepEqual(pin(fs.readFileSync(target)),before[n]);a.ok(fs.readFileSync(source).equals(fs.readFileSync(target)));
  mapping.push({original:source,physical_copy:target,...before[n]});
}
fs.writeFileSync(OWN+'/MAPPING.json',JSON.stringify({status:'PHYSICAL_HISTORICAL_CONTROLS_BEFORE_P212_SEMANTICS_TERMINAL_SOURCE_ACCEPTANCE',mapping,actual_native_commands:records.length},null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({status:'PASS_EXACT_TWO_CONTROL_COPIES_AND_FOUR_NATIVE_COMMANDS',mapping,native_commands:records.length}));
