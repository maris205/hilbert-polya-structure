'use strict';
// Pure documentary event consumer. No filesystem, subprocess, source import,
// dynamic evaluation, path resolution syscall or observer execution.
const assert=require('assert/strict'), crypto=require('crypto');
const {parseCanonical}=require('./JSON_LOSSLESS.cjs');
module.exports=function auditTrace(v, authorization, controls) {
  let checks=0,ni=0,pi=0,readBytes=0,captureBytes=0,decoded=0,absences=0,zeroAbsence=0;
  let fileCount=0,capturedCount=0,memberCount=0,ancestorComparisons=0,leafComparisons=0,ignoredAtimeChanges=0;
  const spans=[],contents=[],aliasReads=[],absenceEvents=[],fieldCopies=[];
  const eq=(a,b,m)=>{checks++;assert.deepStrictEqual(a,b,m);},ok=(a,m)=>{checks++;assert(a,m);};
  const shape=(v,ks,m)=>eq(Object.keys(v).sort(),ks.slice().sort(),m);
  const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
  const F=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
  const I=['dev','ino','mode','uid','gid','rdev','birthtimeNs'];
  const kind=k=>Number(BigInt(k.mode)&61440n);
  function physical(p) {
    return typeof p==='string'&&p.startsWith('/')&&Buffer.byteLength(p)<=4096&&!p.includes('\0')&&
      (p==='/'||p.slice(1).split('/').every(s=>s!==''&&s!=='.'&&s!=='..'));
  }
  function components(p) {
    ok(physical(p),'canonical captured absolute spelling');
    return p==='/'?['/']:['/',...p.slice(1).split('/').map((_,i,a)=>'/'+a.slice(0,i+1).join('/'))];
  }
  function stable(a,b,ancestor=false) {
    ok(a!==null&&b!==null,'two present native keys');
    const names=ancestor?I:F.filter(f=>f!=='atimeNs');
    eq(Object.fromEntries(names.map(f=>[f,a[f]])),Object.fromEntries(names.map(f=>[f,b[f]])),'source-required stable native fields');
    if(ancestor)ancestorComparisons++;else leafComparisons++;
    if(a.atimeNs!==b.atimeNs)ignoredAtimeChanges++;
  }
  const masks={},flags={},errnoCounts={};
  for(let i=0;i<v.native_events.length;i++) {
    const e=v.native_events[i];
    shape(e,['path','handle','flags','requested_mask','return','errno','mask','raw_statx_hex','status',...(e.return===0?['fields']:[])],'whole native event shape');
    ok(physical(e.path));ok(e.handle===null||(Number.isSafeInteger(e.handle)&&e.handle>=3));
    ok([2304,2048,6144].includes(e.flags));eq(e.handle===null,e.flags!==6144);
    eq(e.requested_mask,4095);ok(/^[0-9a-f]{512}$/.test(e.raw_statx_hex),'exact 256-byte raw native structure');
    const b=Buffer.from(e.raw_statx_hex,'hex');eq(b.length,256);
    flags[e.flags]=(flags[e.flags]||0)+1;
    if(e.return===-1) {
      eq(e.mask,null);ok(e.errno===2||e.errno===20);eq(e.status,'ABSENCE_ERRNO_ONLY_NO_DECODED_FIELDS');
      ok(!Object.hasOwn(e,'fields'));absences++;errnoCounts[e.errno]=(errnoCounts[e.errno]||0)+1;
      if(b.every(x=>x===0))zeroAbsence++;
      absenceEvents.push({index:i,path:e.path,errno:e.errno,raw_sha256:sha(b)});
      continue;
    }
    eq(e.return,0);eq(e.errno,0);eq(e.mask,b.readUInt32LE(0));ok((e.mask&4095)===4095);
    eq(e.status,'ACTUAL_MASKED_FIELDS');shape(e.fields,F);
    const u32=o=>BigInt(b.readUInt32LE(o)),u64=o=>b.readBigUInt64LE(o);
    function stamp(o) {const nano=u32(o+8);ok(nano<1000000000n);return b.readBigInt64LE(o)*1000000000n+nano;}
    function device(major,minor) {
      return ((major&4095n)<<8n)|((major&~4095n)<<32n)|(minor&255n)|((minor&~255n)<<12n);
    }
    const values=[device(u32(136),u32(140)),u64(32),BigInt(b.readUInt16LE(28)),u32(16),u32(20),u32(24),
      device(u32(128),u32(132)),u64(40),u32(4),u64(48),stamp(64),stamp(112),stamp(96),stamp(80)];
    const decodedFields=Object.fromEntries(F.map((f,j)=>[f,values[j].toString()]));
    eq(e.fields,decodedFields,'all fourteen decoded fields from actual raw bytes');
    for(const f of F)ok(/^-?(?:0|[1-9][0-9]*)$/.test(e.fields[f]),'canonical decimal field string');
    decoded++;masks[e.mask]=(masks[e.mask]||0)+1;
  }
  for(const e of v.path_events) {
    ok(e.operation==='readlink'||e.operation==='membership_name');
    if(e.operation==='readlink') {
      shape(e,['operation','path','text']);ok(physical(e.path));ok(typeof e.text==='string');
    } else {
      shape(e,['operation','directory','name','ordinal']);ok(physical(e.directory));ok(typeof e.name==='string');
      ok(Number.isSafeInteger(e.ordinal)&&e.ordinal>0);
    }
  }
  function native(p,handle=null,follow=false) {
    ok(ni<v.native_events.length,'recorded native event available');
    const e=v.native_events[ni++];
    eq(e.path,p,'exact ordered native path operand string');eq(e.handle,handle);
    eq(e.flags,handle===null?(follow?2048:2304):6144);
    return e.return===0?e.fields:null;
  }
  function pathEvent(expected) {
    ok(pi<v.path_events.length,'recorded path event available');
    const e=v.path_events[pi++];for(const[k,x]of Object.entries(expected))eq(e[k],x);
    return e;
  }
  class Stop extends Error {}
  function resolve(p,allowed) {
    ok(physical(p));
    let queue=p==='/'?[]:p.slice(1).split('/'),current='/',chain=[],links=0,steps=0,lexical=null;
    const root=native('/');ok(root!==null&&kind(root)===16384,'recorded root directory');
    chain.push({path:'/',lstat:root,link:null});
    while(queue.length) {
      steps++;ok(steps<=1024);const name=queue.shift(),candidate=(current==='/'?'':current)+'/'+name;
      if(!allowed.has(candidate))throw new Stop('unapproved component; not read: '+candidate);
      const key=native(candidate),row={path:candidate,lstat:key,link:null};chain.push(row);
      if(key===null)return{path:p,resolved:null,absent_at:candidate,chain};
      if(queue.length===0&&lexical===null)lexical=key;
      if(kind(key)===40960) {
        links++;ok(links<=40&&BigInt(key.size)<=4096n);
        const event=pathEvent({operation:'readlink',path:candidate}),link=event.text;row.link=link;
        aliasReads.push({native_index:ni-1,path_index:pi-1,path:candidate,text:link});
        ok(Buffer.byteLength(link)<=4096);stable(key,native(candidate));
        ok(link!==''&&link.replace(/^\/+/,'').split('/').every(x=>x!==''&&x!=='.'&&x!=='..'));
        const target=link.startsWith('/')?link:(current==='/'?'':current)+'/'+link;
        ok(physical(target));
        if(!components(target).every(x=>allowed.has(x)))
          throw new Stop('unapproved link target; link text retained, referent not read: '+target);
        queue=target.slice(1).split('/').concat(queue);current='/';continue;
      }
      current=candidate;
      if(queue.length&&kind(key)!==16384) {
        const full=current+'/'+queue.join('/');ok(allowed.has(full),'approved blocked leaf');
        eq(native(full),null);eq(v.native_events[ni-1].errno,20);
        return{path:p,resolved:null,absent_at:full,chain};
      }
    }
    const leaf=chain[chain.length-1].lstat,followed=native(current,null,true);stable(leaf,followed);
    return{path:p,resolved:current,absent_at:null,chain,lstat:lexical||leaf,stat:followed};
  }
  function compare(a,b) {
    eq([a.path,a.resolved,a.absent_at],[b.path,b.resolved,b.absent_at]);eq(a.chain.length,b.chain.length);
    for(let j=0;j<a.chain.length;j++) {
      const x=a.chain[j],y=b.chain[j];eq([x.path,x.link],[y.path,y.link]);
      if(x.lstat===null||y.lstat===null)eq(x.lstat,y.lstat);
      else stable(x.lstat,y.lstat,x.path!==a.resolved&&kind(x.lstat)===16384);
    }
  }
  function content(p,target,expected,recorded) {
    shape(recorded,['bytes','sha256','before','after','raw_hex']);
    ok(Number.isSafeInteger(recorded.bytes)&&recorded.bytes>=0&&recorded.bytes<=target.max_bytes);
    ok(/^[0-9a-f]{64}$/.test(recorded.sha256));
    ok(ni<v.native_events.length);const fd=v.native_events[ni].handle;ok(Number.isSafeInteger(fd)&&fd>=3);
    const before=native(p,fd);ok(before!==null&&kind(before)===32768&&BigInt(before.size)<=BigInt(target.max_bytes));
    stable(expected,before);eq(recorded.before,before);
    const after=native(p,fd);stable(before,after);eq(recorded.after,after);eq(BigInt(recorded.bytes),BigInt(before.size));
    let raw=null;
    if(target.capture_hex) {
      ok(typeof recorded.raw_hex==='string'&&/^(?:[0-9a-f]{2})*$/.test(recorded.raw_hex));
      raw=Buffer.from(recorded.raw_hex,'hex');eq(raw.length,recorded.bytes);eq(sha(raw),recorded.sha256);
      ok(raw.length<=1048576);captureBytes+=raw.length;capturedCount++;
    } else eq(recorded.raw_hex,null);
    if(recorded.bytes===0)eq(recorded.sha256,sha(Buffer.alloc(0)));
    readBytes+=recorded.bytes;fileCount++;ok(readBytes<=536870912&&captureBytes<=8388608);
    contents.push({path:p,bytes:recorded.bytes,sha256:recorded.sha256,captured:target.capture_hex,handle:fd});
    return{content:{bytes:recorded.bytes,sha256:recorded.sha256,before,after,raw_hex:recorded.raw_hex},raw};
  }
  function observe(target,allowed,recorded) {
    const p=target.path,before=resolve(p,allowed);
    const row={target,before,content:null,members:null};
    let raw=null;
    if(before.resolved===null)ok(['absent','optional_file','optional_directory'].includes(target.mode));
    else {
      ok(target.mode!=='absent');const k=kind(before.stat);
      const stdin=p==='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_keyed_stdin_input01/empty.stdin';
      if(stdin) {
        eq([target.mode,target.max_bytes,target.capture_hex],['file',0,true]);
        eq(before.resolved,p);ok(before.chain.every(x=>x.link===null));eq(k,32768);eq(before.stat.size,'0');
      }
      if(['file','optional_file'].includes(target.mode)) {
        eq(k,32768);const r=content(before.resolved,target,before.stat,recorded.content);
        row.content=r.content;raw=r.raw;stable(before.stat,row.content.before);
        if(stdin)eq([row.content.bytes,row.content.sha256,row.content.raw_hex],[0,sha(Buffer.alloc(0)),'']);
      } else if(['directory','optional_directory','membership'].includes(target.mode)) {
        eq(k,16384);
        if(target.mode==='membership') {
          const names=[];
          // The source emits one event per recorded name; expected finite membership
          // fixes the complete count. No directory operand is used by this checker.
          for(let ordinal=1;ordinal<=target.expected_names.length;ordinal++) {
            const e=pathEvent({operation:'membership_name',directory:p,ordinal});
            ok(Buffer.byteLength(e.name)<=255);names.push(e.name);ok(names.length<=target.max_members);memberCount++;
          }
          row.members=names.sort();eq(row.members,target.expected_names);
        }
      } else eq(target.mode,'metadata');
    }
    const after=resolve(p,allowed);compare(before,after);row.after=after;
    return{row,raw};
  }
  shape(v,['schema','status','provenance','observer_bootstrap_attested','author_probe_executed','closure_certified',
    'controls','closing_controls','passes','errors','closure_gaps','native_events','path_events','actual_read_bytes','actual_captured_bytes']);
  eq(v.schema,'p212-independent-preprobe-observation-v1');
  eq(v.provenance,{schema:'p212-trusted-product-boundary-v1',assumption:'ordinary_product_observer_bash_env_bootstrap',
    product_startup_attested:false,claim:'finite_received_keys_and_discrete_downstream_observations'});
  eq(authorization.provenance,v.provenance);
  eq([v.observer_bootstrap_attested,v.author_probe_executed,v.closure_certified],[false,false,false]);
  eq(v.controls.length,3);let frontier=null;
  for(const[i,role]of ['source_receipt','trust_receipt','frontier'].entries()) {
    const item=v.controls[i],ref=authorization[role];shape(item,['role','observation']);eq(item.role,role);
    const target={path:ref.path,mode:'file',max_bytes:ref.pin.bytes,capture_hex:true};
    const startN=ni,startP=pi,r=observe(target,new Set(components(ref.path)),item.observation);
    eq(r.row,item.observation,'complete generated control matches recorded control');
    eq(r.row.before.resolved,ref.path);eq([r.row.content.bytes,r.row.content.sha256],[ref.pin.bytes,ref.pin.sha256]);
    eq(r.raw,controls[role],'entire captured control equals selected frozen documentary bytes');
    spans.push({role,native_start:startN,native_end:ni,path_start:startP,path_end:pi});
    if(role==='frontier')frontier=parseCanonical(r.raw).value;
  }
  shape(frontier,['schema','status','author_probe_execution_allowed','targets','allowed_components','closure_gaps']);
  eq([frontier.schema,frontier.status,frontier.author_probe_execution_allowed],
    ['p212-finite-preprobe-frontier-v1','SOURCE_ONLY_INITIAL_FRONTIER_NOT_CLOSURE',false]);
  const targets=frontier.targets,allowed=new Set(frontier.allowed_components);
  ok(targets.length>0&&targets.length<=384);eq(frontier.allowed_components,[...allowed].sort());ok(allowed.size<=768);
  for(const p of allowed)ok(components(p).every(x=>allowed.has(x)));
  eq(targets.map(t=>t.path),[...new Set(targets.map(t=>t.path))].sort());
  for(const t of targets) {
    shape(t,['path','mode','role','origin','max_bytes','capture_hex','max_members','expected_names']);
    ok(allowed.has(t.path)&&typeof t.role==='string'&&typeof t.origin==='string');
    ok(['file','optional_file','directory','optional_directory','membership','absent','metadata'].includes(t.mode));
    ok(typeof t.capture_hex==='boolean'&&Number.isSafeInteger(t.max_bytes)&&t.max_bytes>=0&&t.max_bytes<=134217728);
    ok(Number.isSafeInteger(t.max_members)&&t.max_members>=0&&t.max_members<=320);
    if(t.mode==='membership') {
      eq(t.expected_names,[...new Set(t.expected_names)].sort());ok(t.expected_names.length<=t.max_members);
      for(const n of t.expected_names)ok(typeof n==='string'&&!['','.','..'].includes(n)&&!n.includes('/')&&!n.includes('\0')&&Buffer.byteLength(n)<=255);
    } else eq([t.max_members,t.expected_names],[0,null]);
    if(!['file','optional_file'].includes(t.mode))eq([t.max_bytes,t.capture_hex],[0,false]);
  }
  eq(v.closure_gaps,frontier.closure_gaps);ok(Array.isArray(v.closure_gaps)&&v.closure_gaps.length>0);
  eq(v.passes.length,1);shape(v.passes[0],['number','targets']);eq(v.passes[0].number,1);
  const rows=v.passes[0].targets,generated=[];let failure=null;
  for(let i=0;i<rows.length;i++) {
    const recorded=rows[i],target=targets[i],startN=ni,startP=pi;eq(recorded.target,target);
    try {
      const r=observe(target,allowed,recorded);r.row.status='OBSERVED';eq(r.row,recorded,'whole observed target row');
      generated.push(r.row);
    } catch(error) {
      if(!(error instanceof Stop))throw error;
      const row={target,status:'HOLD',error_type:'Hold',error_message:error.message,first_event:startN};
      eq(row,recorded,'exact expected pre-read stop row');failure={pass:1,...row};generated.push(row);
      eq(i,rows.length-1,'first failure is final target record');
    }
    spans.push({target_index:i,path:target.path,status:recorded.status,native_start:startN,native_end:ni,path_start:startP,path_end:pi});
    if(failure)break;
  }
  ok(failure!==null);eq(v.errors,[failure]);eq(v.status,'HOLD_FINITE_OBSERVATION_ERRORS');eq(v.closing_controls,[]);
  eq(ni,v.native_events.length,'all native events consumed exactly once in order');
  eq(pi,v.path_events.length,'all path events consumed exactly once in order');
  eq(readBytes,v.actual_read_bytes);eq(captureBytes,v.actual_captured_bytes);
  ok(v.native_events.length<=60000);
  eq([targets.length,allowed.size,rows.length,generated.filter(r=>r.status==='OBSERVED').length],[164,207,158,157]);
  eq([decoded,absences,zeroAbsence,memberCount],[2224,50,50,292]);
  eq(failure.target.path,'/usr/local/cuda/lib64');eq(failure.first_event,2262);
  eq(failure.error_message,'unapproved component; not read: /usr/local/cuda-12.8/lib64');
  const refused='/usr/local/cuda-12.8/lib64';
  eq(allowed.has(refused),false);
  eq(v.native_events.filter(e=>e.path===refused).length,0);
  eq(v.path_events.filter(e=>e.path===refused||e.directory===refused).length,0);
  eq(contents.filter(c=>c.path===refused).length,0);
  eq(v.native_events.some(e=>e.handle===0),false);
  const stdin=generated[42];
  const tail=targets.slice(rows.length).map(t=>({path:t.path,mode:t.mode,role:t.role}));
  const observedAbsent=generated.filter(r=>r.status==='OBSERVED'&&r.before.resolved===null).map(r=>({path:r.target.path,mode:r.target.mode,absent_at:r.before.absent_at}));
  const memberships=generated.filter(r=>r.status==='OBSERVED'&&r.members!==null).map(r=>({path:r.target.path,names:r.members}));
  return {checks,native_events:ni,path_events:pi,decoded_events:decoded,absence_events:absences,zero_raw_absence_events:zeroAbsence,
    masks,flags,errno_counts:errnoCounts,file_contents:fileCount,captured_contents:capturedCount,
    uncaptured_content_hashes_not_independently_recomputed:fileCount-capturedCount,
    actual_read_bytes:readBytes,actual_captured_bytes:captureBytes,member_names:memberCount,membership_directories:memberships.length,
    comparisons:{ancestor:ancestorComparisons,leaf:leafComparisons,ignored_atime_differences:ignoredAtimeChanges},
    frontier_targets:targets.length,allowed_components:allowed.size,observed_targets:157,failed_targets:1,unattempted_targets:tail,
    stop:failure,spans,contents,aliases:aliasReads,absences:absenceEvents,observed_absent:observedAbsent,memberships,
    stdin:{index:42,path:stdin.target.path,status:stdin.status,resolved:stdin.before.resolved,physical_chain:stdin.before.chain.every(x=>x.link===null),
      content:{bytes:stdin.content.bytes,sha256:stdin.content.sha256,raw_hex:stdin.content.raw_hex},fd0_event_observed:false},
    closure_gaps:v.closure_gaps,runtime_accepted:false,bootstrap_attested:false,operational_authorization:false};
};
