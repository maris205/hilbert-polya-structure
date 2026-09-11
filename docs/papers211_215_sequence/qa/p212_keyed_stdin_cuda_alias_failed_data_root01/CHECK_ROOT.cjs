'use strict';
// Root final-layout documentary/data receiver. It never follows captured paths.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const Q='docs/papers211_215_sequence/qa/',A=Q+'p212_keyed_stdin_cuda_alias_failed_observation_audit01/',R=Q+'p212_keyed_stdin_cuda_alias_failed_data_root01/';
const C='/root/symbolic-dynamics-p212-cuda-alias-observation-20260910-01';
const names=['AUDIT_TRACE.cjs','CHECK_DATA.cjs','CHECK_NATIVE.json','CHECK_RESULT.json','CLOSE_NATIVE.json','CLOSE_RESULT.json','FINDINGS.json','INITIAL_RAW_NATIVE.json','INITIAL_RAW_RESULT.json','INPUTS.sha256','JSON_LOSSLESS.cjs','READBACK_NATIVE.json','READS_NATIVE_01.json','READS_NATIVE_02.json','READS_NATIVE_03.json','READS_NATIVE_04.json','READ_RAW_LOSSLESS.cjs','REPORT.md','SCOPE.md','WRAPPER_FAILURE.md'];
const own=['CHECK_ROOT.cjs','READ_SCOPE.json','ROOT_READS_NATIVE.json','ROOT_REPLAY_NATIVE.json','ROOT_REPLAY_RESULT.json'];
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const setting=JSON.parse(fs.readFileSync(R+'READ_SCOPE.json','utf8'));
const allowed=new Set([...setting.paths,...names.map(n=>A+n),A+'SHA256SUMS',...own.map(n=>R+n)]);
const keys=new Map(),bodies=new Map(),pairs=[],atimeDifferences=[];let checks=0,oldKeyOccurrences=0;
const eq=(a,b,m)=>{checks++;assert.deepStrictEqual(a,b,m);},ok=(v,m)=>{checks++;assert(v,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),md=s=>Object.fromEntries(fields.map(n=>[n,String(s[n])]));
const stable=m=>Object.fromEntries(fields.filter(n=>n!=='atimeNs').map(n=>[n,m[n]]));
function fresh(p){
 ok(allowed.has(p),'exact fixed documentary/raw operand');const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&a.nlink===1n&&a.uid===0n&&a.size>=0n&&a.size<=134217728n);
 if(p.startsWith(C+'/'))eq(a.mode&4095n,384n);
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,s,e;
 try{s=md(fs.fstatSync(fd,{bigint:true}));eq(stable(s),stable(md(a)));b=fs.readFileSync(fd);e=md(fs.fstatSync(fd,{bigint:true}));eq(stable(e),stable(s));}finally{fs.closeSync(fd);}
 const z=md(fs.lstatSync(p,{bigint:true}));eq(stable(z),stable(e));eq(BigInt(b.length),a.size);
 return{b,key:{path:p,bytes:b.length,sha256:sha(b),fields:md(a),fd_before:s,fd_end:e,path_end:z,full_eof:true,leaf_links:1}};
}
function read(p){if(!bodies.has(p)){const x=fresh(p);bodies.set(p,x.b);keys.set(p,x.key);}return bodies.get(p);}
const json=p=>JSON.parse(read(p).toString('utf8'));
const pair=(label,a,b)=>{eq(a,b,label);pairs.push({label,bytes:a.length,sha256:sha(a)});};
function old(k){
 const b=read(k.path),now=keys.get(k.path);eq(Object.keys(k),['path','bytes','sha256','fields','fd_before','fd_end','path_end','full_eof','leaf_links']);eq([k.bytes,k.sha256],[b.length,now.sha256]);
 for(const role of['fields','fd_before','fd_end','path_end']){eq(Object.keys(k[role]),fields);eq(stable(k[role]),stable(now.fields),'complete old stable fields');ok(/^-?[0-9]+$/.test(k[role].atimeNs));}
 eq([k.full_eof,k.leaf_links],[true,1]);oldKeyOccurrences++;
}
const d0=md(fs.lstatSync(C,{bigint:true}));eq([d0.mode,d0.uid,d0.gid],['16832','0','0']);
const dfd=fs.openSync(C,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK|fs.constants.O_DIRECTORY);let ds,de,dz;
try{
 ds=md(fs.fstatSync(dfd,{bigint:true}));eq(stable(ds),stable(d0));eq(fs.readdirSync(C).sort(),['stderr.raw','stdout.raw']);
 eq(setting.schema,'P212_FAILED_DATA_ROOT_FIXED_SCOPE_V1');eq(setting.capture_directory,C);eq(setting.allow_embedded_target_path_following,false);
 eq(fs.readdirSync(A).sort(),[...names,'SHA256SUMS'].sort(),'complete final 21-file audit inventory');
 for(const p of allowed)read(p);
 const seal=read(A+'SHA256SUMS');eq(sha(seal),'2c39e690c23b0b17650384b74477e9f871119770ad72d208f9fc5e475b78b051');
 pair('exact complete twenty-payload audit manifest',seal,Buffer.from(names.map(n=>keys.get(A+n).sha256+'  '+n).join('\n')+'\n'));
 eq(names.reduce((n,p)=>n+keys.get(A+p).bytes,0),1989921);
 const main=json(A+'CHECK_RESULT.json'),mn=json(A+'CHECK_NATIVE.json').record,closing=json(A+'CLOSE_RESULT.json'),cn=json(A+'CLOSE_NATIVE.json').record;
 for(const[x,id,n]of[[mn,'676465','CHECK_RESULT.json'],[cn,'0ad0f3','CLOSE_RESULT.json']]){eq(x.result.chunk_id,id);eq(x.result.exit_code,0);ok(!x.result.session_id);pair('complete original native stdout '+n,Buffer.from(x.result.output),read(A+n));}
 eq([main.documentary_checks,main.trace_checks,main.total_checks,main.keys.length],[1536,96978,98514,49]);eq([closing.checks,closing.keys.length,closing.preclosing_payloads],[1307,56,18]);
 for(const k of main.keys)old(k);for(const k of closing.keys)old(k);
 // Do not execute the archived eighteen-file preclosing command on a final tree.
 ok(cn.request.cmd.includes('historical exact eighteen-payload preclosing inventory'));
 const priorNames=names.filter(n=>!['CLOSE_NATIVE.json','CLOSE_RESULT.json'].includes(n));
 pair('historical preclosing eighteen-payload manifest',Buffer.from(closing.preclosing_manifest),Buffer.from(priorNames.map(n=>keys.get(A+n).sha256+'  '+n).join('\n')+'\n'));
 eq(sha(Buffer.from(closing.preclosing_manifest)),closing.preclosing_manifest_sha256);
 pair('entire 36-document input digest list',read(A+'INPUTS.sha256'),Buffer.from(main.external_digest_list));
 const rootNative=json(R+'ROOT_REPLAY_NATIVE.json'),current=json(R+'ROOT_REPLAY_RESULT.json');eq(rootNative.result.chunk_id,'3c9b6e');eq(rootNative.result.exit_code,0);ok(!rootNative.result.session_id);
 eq(rootNative.request.cmd,'node '+A+'CHECK_DATA.cjs');pair('whole actual root DATA stdout artifact',Buffer.from(rootNative.result.output),read(R+'ROOT_REPLAY_RESULT.json'));
 const rawEqual=read(A+'CHECK_RESULT.json').equals(read(R+'ROOT_REPLAY_RESULT.json'));
 function compare(x,y,path=''){
  if(x===null||typeof x!=='object'){
   if(x!==y&&/^\/keys\/\d+\/(fields|fd_before|fd_end|path_end)\/atimeNs$/.test(path)){
    const i=Number(path.split('/')[2]);ok(current.keys[i].path===main.keys[i].path);ok(typeof x==='string'&&typeof y==='string'&&/^[0-9]+$/.test(x)&&/^[0-9]+$/.test(y));atimeDifferences.push({path,document:current.keys[i].path,old:x,current:y});
   }else eq(x,y,'whole non-atime semantic scalar '+path);return;
  }
  eq(typeof y,'object');ok(y!==null);eq(Array.isArray(x),Array.isArray(y));eq(Object.keys(x),Object.keys(y),'complete output shape '+path);
  for(const k of Object.keys(x))compare(x[k],y[k],path+'/'+k);
 }
 compare(main,current);eq(atimeDifferences.length,14);eq(new Set(atimeDifferences.map(x=>x.document)).size,7);
 eq(rawEqual,false,'whole stdout is honestly NOT raw-identical');
 // Captured trace/native atimes were never dropped: only external key slots above.
 eq(current.trace,main.trace,'complete trace remains exactly equal');
 for(const k of current.keys)old(k);
 const logs=['READS_NATIVE_01.json','READS_NATIVE_02.json','READS_NATIVE_03.json','READS_NATIVE_04.json'].flatMap(n=>json(A+n).records),rb=json(A+'READBACK_NATIVE.json').records;
 eq([...logs,...rb].map(r=>r.seq),Array.from({length:37},(_,i)=>i+1));eq(logs[31],mn);
 const numbered=b=>{const s=b.toString('utf8');ok(s.endsWith('\n'));return Buffer.from(s.slice(0,-1).split('\n').map((l,i)=>String(i+1).padStart(6,' ')+'\t'+l+'\n').join(''));};
 for(const[ix,n]of[[29,'AUDIT_TRACE.cjs'],[30,'CHECK_DATA.cjs']]){eq(logs[ix].request.cmd,'nl -ba '+A+n);eq(logs[ix].result.exit_code,0);pair('whole original source read '+n,Buffer.from(logs[ix].result.output),numbered(read(A+n)));}
 for(const[i,n]of['REPORT.md','FINDINGS.json','SCOPE.md','INPUTS.sha256','WRAPPER_FAILURE.md'].entries()){eq(rb[i].request.cmd,'nl -ba '+A+n);eq(rb[i].result.exit_code,0);pair('whole original final read '+n,Buffer.from(rb[i].result.output),numbered(read(A+n)));}
 const rootReads=json(R+'ROOT_READS_NATIVE.json');eq(rootReads.absence.result.exit_code,0);eq(rootReads.absence.result.output,'');
 for(const r of rootReads.records){eq(r.result.exit_code,0);if(r.request.cmd.startsWith('sed -n ')){
  const chunks=r.request.cmd.split('\n').map(cmd=>{const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(cmd);ok(m);const ls=read(m[3]).toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];return Buffer.from(ls.slice(Number(m[1])-1,Number(m[2])).join(''));});pair('actual complete root read '+r.result.chunk_id,Buffer.from(r.result.output),Buffer.concat(chunks));
 }else{ok(r.request.cmd.includes("d+'CLOSE_NATIVE.json'"));pair('actual full archived closure source read',Buffer.from(r.result.output),Buffer.from(cn.request.cmd+'\n'));}}
 const findings=json(A+'FINDINGS.json');eq(findings.finding_census,{blocker:0,major:0,minor:0});eq(findings.open_data_findings,[]);eq(findings.runtime_accepted,false);eq(findings.operational_authorization,false);
 for(const[p,k]of keys){const x=fresh(p);eq([x.key.bytes,x.key.sha256],[k.bytes,k.sha256]);eq(stable(x.key.fields),stable(k.fields));eq(x.b,bodies.get(p));}
 de=md(fs.fstatSync(dfd,{bigint:true}));dz=md(fs.lstatSync(C,{bigint:true}));eq(stable(d0),stable(de));eq(stable(de),stable(dz));eq(fs.readdirSync(C).sort(),['stderr.raw','stdout.raw']);
 process.stdout.write(JSON.stringify({schema:'P212_ROOT_FAILED_RAW_AND_COMPLETE_AUDIT_RECEPTION_V1',checks,document_keys:keys.size,old_complete_key_occurrences:oldKeyOccurrences,audit_payloads:20,audit_files:21,audit_payload_bytes:1989921,audit_seal_sha256:sha(seal),root_data_replay:{native:'3c9b6e',checks:current.total_checks,whole_stdout_raw_equal:rawEqual,exact_semantics_equal_except_declared_external_atime:true,atime_differences:atimeDifferences,complete_trace_equal:true},raw_pairs:pairs.length,raw_paired_bytes:pairs.reduce((n,p)=>n+p.bytes,0),pairs,keys:[...keys.values()],capture:{path:C,path_before:d0,fd_before:ds,fd_end:de,path_end:dz,members:['stderr.raw','stdout.raw']},verdict:'ACCEPT_FAILED_RAW_DATA_ONLY_UNDER_ORDINARY_TRUST',runtime_accepted:false,source_or_manuscript_acceptance:false,operational_authorization:false,grants_consumed:true,HOLD_EXTERNAL:true},null,2)+'\n');
}finally{fs.closeSync(dfd);}
