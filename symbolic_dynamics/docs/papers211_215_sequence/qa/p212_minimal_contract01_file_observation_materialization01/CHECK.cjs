'use strict';
// Fixed documentary paths only. Never require/import/parse-as-code the carriers.
const fs=require('node:fs'), {createHash}=require('node:crypto');
const QA='docs/papers211_215_sequence/qa/';
const P=QA+'p212_minimal_contract01_file_observation_';
const OWN=P+'materialization01', AUTHOR=P+'preparation01';
const ENABLED=P+'enabled01', RAW=P+'raw01';
const FIELDS=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const DIR_ID=['dev','ino','mode','uid','gid','rdev'];
const DOCS=[
  ['reader',AUTHOR+'/file_keys.proposed.mjs.txt',13660,'957111a4a680f61cc94e89eb220b8c7c10d779e04eabd4734948690ef11b41f8'],
  ['entry',AUTHOR+'/collect_files.proposed.mjs.txt',13540,'bd9baeb57f2387860a400f4b27e8acf9897da3843482cf856378f9807a2b2b87'],
  ['capture',AUTHOR+'/capture.proposed.sh.txt',638,'11c0ac1540f30fa60cc691e7c42586918d4061d07aaca41d5b66a1329e3d30a4'],
  ['file_request',AUTHOR+'/FILE_REQUEST.proposed.json',1979,'c81d8d5e3fd5e4305c0871365832dca0256256ffd63a899686c236b0fb3df790'],
  ['entry_request',AUTHOR+'/ENTRY_REQUEST.proposed.json',10602,'4157587f5cc3f1179aff59a6a55dedd7c7290bd487f90c74d4d0dc51694d3fff'],
  ['author_seal',AUTHOR+'/SHA256SUMS',1627,'8a296cda89323b49cef3a6797a3e8d75b47f0966ff9b440e2c57bc29f0415d0e'],
  ['audit_report',P+'source_audit01/REPORT.md',null,null],
  ['audit_seal',P+'source_audit01/SHA256SUMS',1043,'7164ffbc6f14882130700168a094e5bfd802529f9cdd3bb23d974f981aca3a8a'],
  ['root_receipt',P+'source_root01/RECEPTION.md',null,'6f81e56517f976b61acf9ffea5e737b6b6dce7eb219dfa5133e175f04142217a'],
  ['root_seal',P+'source_root01/SHA256SUMS',null,'1f8f1039dbed8239b8d54ea8c501b6e8469f737e83e30f4c8f8edc61b52b6cd1'],
  ['materializer',OWN+'/CHECK.cjs',null,null],
  ['scope',OWN+'/ORIGIN.md',null,null],
  ['read_native',OWN+'/READ_NATIVE.json',null,null]
];
const COPIES=[['reader',ENABLED+'/file_keys.mjs'],['entry',ENABLED+'/collect_files.mjs']];
const allowedFiles=new Set([...DOCS.map(x=>x[1]),...COPIES.map(x=>x[1]),
  ...['MATERIALIZE_NATIVE.json','MATERIALIZE_RESULT.json'].map(x=>OWN+'/'+x)]);
const report={schema:'p212-two-source-materialization-v1',mode:null,status:'FAILED_PARTIAL_PRESERVED',
  checks:0,current_uid:process.getuid(),current_gid:process.getgid(),keys:[],directories:[],
  absence:[],actions:[],comparisons:[],input_pins:[],failure:null,source_execution:false,
  candidate_observation:false,binding_materialized:false,observation_grant:false,
  operation_permission:false,installed_closure:false,external_status:'HOLD_EXTERNAL',
  directory_handle_identity_attested:false,unscanned_ancestors_trusted:true};
const buffers=new Map();
const need=(value,label)=>{report.checks++;if(!value)throw new Error(label);};
const eq=(a,b,label)=>need(JSON.stringify(a)===JSON.stringify(b),label);
const pin=b=>({bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')});
const errorData=e=>({name:String(e?.name??'Error'),code:typeof e?.code==='string'?e.code:null,message:String(e?.message??e)});
const fields=s=>Object.fromEntries(FIELDS.map(k=>{need(typeof s[k]==='bigint','actual bigint '+k);return[k,s[k].toString()];}));
function file(path,phase){
  need(allowedFiles.has(path),'literal permitted documentary/copy path');
  const row={path,phase,lstat_before:null,fstat_before:null,fstat_after:null,lstat_after:null,
    fd:null,reads:[],bytes_read:0,eof:false,content:null,close_succeeded:null,error:null,close_error:null};
  report.keys.push(row);let fd=null;const chunks=[];
  try{
    const l=fs.lstatSync(path,{bigint:true});row.lstat_before=fields(l);
    need(l.isFile()&&!l.isSymbolicLink(),'physical regular file');
    need(l.size>=0n&&l.size<=8388608n,'bounded document/copy, never host candidate');
    fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);row.fd=fd;
    const s=fs.fstatSync(fd,{bigint:true});row.fstat_before=fields(s);need(s.isFile(),'regular opened file');
    eq(row.lstat_before,row.fstat_before,'same-fd before bytes');
    const block=Buffer.alloc(65536);
    for(;;){const requested=Math.min(block.length,8388609-row.bytes_read);need(requested>0,'positive read request');
      const count=fs.readSync(fd,block,0,requested,null);row.reads.push({requested,returned:count});
      if(count===0){row.eof=true;break;}
      chunks.push(Buffer.from(block.subarray(0,count)));row.bytes_read+=count;need(row.bytes_read<=8388608,'document byte bound');}
    const raw=Buffer.concat(chunks);row.content=pin(raw);need(BigInt(raw.length)===s.size,'entire size through actual EOF');
    row.fstat_after=fields(fs.fstatSync(fd,{bigint:true}));row.lstat_after=fields(fs.lstatSync(path,{bigint:true}));
    eq(row.fstat_before,row.fstat_after,'same-fd after EOF');eq(row.lstat_before,row.lstat_after,'lexical endpoint after EOF');
    need(Buffer.from(raw.toString('utf8'),'utf8').equals(raw),'UTF8 reversible document/copy bytes');
    buffers.set(phase+'\0'+path,raw);
  }catch(e){row.error=errorData(e);throw e;}
  finally{if(fd!==null){try{fs.closeSync(fd);row.close_succeeded=true;}
    catch(e){row.close_succeeded=false;row.close_error=errorData(e);throw e;}}}
  need(row.eof&&row.close_succeeded===true,'actual EOF and successful close');return row;
}
function absence(path){
  need(path===ENABLED||path===RAW,'only two new runtime directories');
  const row={path,state:null,error:null};report.absence.push(row);
  try{const s=fs.lstatSync(path,{bigint:true});row.state='EXISTS_REFUSE';row.metadata=fields(s);throw new Error('existing target: refuse without repair');}
  catch(e){row.error=errorData(e);if(e.code==='ENOENT'){row.state='ABSENT';return;}throw e;}
}
function directory(path,phase,names){
  need(path===ENABLED||path===RAW,'exact directory target, no discovery');
  const row={path,phase,before:null,after:null,names:[],eof:false,close_succeeded:null,error:null,close_error:null};
  report.directories.push(row);let d=null;
  try{const s=fs.lstatSync(path,{bigint:true});row.before=fields(s);
    need(s.isDirectory()&&!s.isSymbolicLink(),'physical directory leaf');
    need((s.mode&0o7777n)===0o700n,'owned private mode0700 exactly');
    need(s.uid===BigInt(report.current_uid)&&s.gid===BigInt(report.current_gid),'current root tool owner/group');
    d=fs.opendirSync(path);
    for(;;){const ent=d.readSync();if(ent===null){row.eof=true;break;}row.names.push(ent.name);
      need(row.names.length<=names.length+1,'unexpected member preserved and refused');}
    row.names.sort();eq(row.names,[...names].sort(),'exact membership through null EOF');
    row.after=fields(fs.lstatSync(path,{bigint:true}));eq(row.before,row.after,'whole directory ten-field stability during preflight');
  }catch(e){row.error=errorData(e);throw e;}
  finally{if(d!==null){try{d.closeSync();row.close_succeeded=true;}
    catch(e){row.close_succeeded=false;row.close_error=errorData(e);throw e;}}}
  need(row.eof&&row.close_succeeded===true,'directory EOF and successful close');return row;
}
function sameFile(a,b,label){
  for(const k of ['lstat_before','fstat_before','fstat_after','lstat_after','bytes_read','eof','content','close_succeeded','error','close_error'])eq(a[k],b[k],label+' '+k);
  const left=buffers.get(a.phase+'\0'+a.path),right=buffers.get(b.phase+'\0'+b.path);
  need(left.equals(right),label+' full RAW equality');report.comparisons.push({label,left:{path:a.path,phase:a.phase},right:{path:b.path,phase:b.phase},bytes:left.length,raw_equal:true});
}
function sealMap(raw,count){const text=raw.toString('utf8');need(text.endsWith('\n'),'full seal newline');
  const out=new Map();for(const line of text.slice(0,-1).split('\n')){const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);need(!!m,'strict leaf-only nonself seal line');need(m[2]!=='SHA256SUMS'&&!out.has(m[2]),'no self or duplicate');out.set(m[2],m[1]);}
  need(out.size===count,'exact accepted payload count');return out;}
function documentChecks(rows){
  for(const [id,path,bytes,sha]of DOCS){const row=rows.get(id);if(bytes!==null)need(row.content.bytes===bytes,id+' expected bytes');if(sha!==null)need(row.content.sha256===sha,id+' expected sha256');}
  const get=id=>buffers.get(rows.get(id).phase+'\0'+rows.get(id).path);
  const author=sealMap(get('author_seal'),19),audit=sealMap(get('audit_seal'),13),root=sealMap(get('root_seal'),11);
  for(const id of ['reader','entry','capture','file_request','entry_request']){const row=rows.get(id);need(author.get(row.path.split('/').at(-1))===row.content.sha256,'accepted author seal binds '+id);}
  need(audit.get('REPORT.md')===rows.get('audit_report').content.sha256,'accepted audit seal binds report');
  need(root.get('RECEPTION.md')===rows.get('root_receipt').content.sha256,'accepted root seal binds receipt');
  const entry=JSON.parse(get('entry_request')),request=JSON.parse(get('file_request'));
  need(request.enabled===false&&request.permission_receipt===null&&request.settlement_receipt===null,'unchanged unbound documentary template');
  need(entry.operation_authorized===false&&entry.actual_bound_request===null&&entry.root_grant===null&&entry.new_observation_grant===null&&!entry.operation_permission,'no submitted binding or grant in accepted request');
  need(Buffer.from(entry.proposed_native_request.arguments.cmd,'utf8').equals(get('capture')),'whole proposed native command RAW equals capture carrier');
  report.comparisons.push({label:'complete proposed native command vs capture carrier',bytes:get('capture').length,raw_equal:true});
  for(const[id,dst]of COPIES){const spec=entry.prospective_sources.find(x=>x.documentary_carrier.path===rows.get(id).path);
    need(!!spec&&spec.future_path==='/root/autodl-tmp/symbolic_dynamics/'+dst,'exact accepted source/destination mapping');eq(rows.get(id).content,{bytes:spec.documentary_carrier.bytes,sha256:spec.documentary_carrier.sha256},'entire accepted source pin');}
  need(entry.proposed_target_directory==='/root/autodl-tmp/symbolic_dynamics/'+RAW,'exact accepted raw-directory spelling');
}
try{
  need(process.argv.length===3&&['--materialize','--preflight'].includes(process.argv[2]),'exact mode; no implicit mutation');report.mode=process.argv[2];
  need(process.cwd()==='/root/autodl-tmp/symbolic_dynamics','fixed trusted workspace cwd');need(report.current_uid===0&&report.current_gid===0,'root-owned directories under adopted key tool');
  const before=new Map(DOCS.map(([id,path])=>[id,file(path,'before')]));documentChecks(before);
  report.input_pins=DOCS.map(([id,path])=>({id,path,...before.get(id).content}));
  let original=null;
  if(report.mode==='--materialize'){
    absence(ENABLED);absence(RAW);
    for(const path of [ENABLED,RAW]){const action={operation:'mkdirSync',path,requested_mode:'0700',recursive:false,success:false,error:null};report.actions.push(action);
      try{fs.mkdirSync(path,{mode:0o700});action.success=true;}catch(e){action.error=errorData(e);throw e;}}
    directory(ENABLED,'fresh_created',[]);directory(RAW,'fresh_created',[]);
    for(const[id,dst]of COPIES){const source=before.get(id).path;const current=file(source,'before_copy_'+id);sameFile(before.get(id),current,id+' immediately before copy');
      const action={operation:'copyFileSync',source,destination:dst,flags:'COPYFILE_EXCL',success:false,error:null};report.actions.push(action);
      try{fs.copyFileSync(source,dst,fs.constants.COPYFILE_EXCL);action.success=true;}catch(e){action.error=errorData(e);throw e;}}
  }else{
    const nr=file(OWN+'/MATERIALIZE_NATIVE.json','native_original'),rr=file(OWN+'/MATERIALIZE_RESULT.json','result_original');
    const native=JSON.parse(buffers.get(nr.phase+'\0'+nr.path)),raw=buffers.get(rr.phase+'\0'+rr.path);original=JSON.parse(raw);
    need(native.tool==='exec_command'&&native.result.exit_code===0&&!native.result.session_id,'actual completed materialization native');
    need(native.request.cmd==='node '+OWN+'/CHECK.cjs --materialize'&&native.request.workdir===process.cwd(),'exact native materialization request');
    need(Buffer.from(native.result.output,'utf8').equals(raw),'whole native stdout RAW equals full result');
    report.comparisons.push({label:'complete materialization native stdout vs full result',bytes:raw.length,raw_equal:true});
    need(original.status==='MATERIALIZED_ROOT_RECEPTION_PENDING'&&original.mode==='--materialize'&&original.failure===null,'actual materialization passed within scope');
    need(original.absence.length===2&&original.absence.every(x=>x.state==='ABSENT'&&x.error.code==='ENOENT'),'actual two pre-mutation absences');
    need(original.actions.length===4&&original.actions.every(x=>x.success===true&&x.error===null),'actual two mkdir and two exclusive-copy returns');
    for(const[id,row]of before){const old=original.keys.find(x=>x.path===row.path&&x.phase==='after');need(!!old,'all prior inputs present');
      for(const k of ['lstat_before','fstat_before','fstat_after','lstat_after','content','bytes_read','eof','close_succeeded','error','close_error'])eq(row[k],old[k],id+' whole prior input key');}
  }
  const copied=new Map();for(const[id,path]of COPIES){const row=file(path,'copy_final');copied.set(id,row);
    need(row.lstat_before.nlink==='1'&&row.lstat_before.uid==='0'&&row.lstat_before.gid==='0','fresh private single-link root-owned copy');
    const a=buffers.get('before\0'+before.get(id).path),b=buffers.get('copy_final\0'+path);need(a.equals(b),'source to copy entire RAW equality');
    report.comparisons.push({label:id+' full source/copy RAW comparison',source:before.get(id).path,destination:path,bytes:a.length,raw_equal:true});
    eq(row.content,before.get(id).content,id+' source/copy exact full pin');
    need(row.lstat_before.dev!==before.get(id).lstat_before.dev||row.lstat_before.ino!==before.get(id).lstat_before.ino,'physical copy not same inode');
    if(original){const old=original.keys.find(x=>x.path===path&&x.phase==='copy_final');need(!!old,'prior copy key present');for(const k of ['lstat_before','fstat_before','fstat_after','lstat_after','content','bytes_read','eof','close_succeeded','error','close_error'])eq(row[k],old[k],id+' complete prior copy key');}}
  const after=new Map(DOCS.map(([id,path])=>[id,file(path,'after')]));documentChecks(after);
  for(const[id,row]of before)sameFile(row,after.get(id),id+' entire input before/after');
  const finalEnabled=directory(ENABLED,'final_preflight',['collect_files.mjs','file_keys.mjs']),finalRaw=directory(RAW,'final_preflight',[]);
  for(const current of [finalEnabled,finalRaw]){
    const prior=original?original.directories.find(x=>x.path===current.path&&x.phase==='final_preflight'):report.directories.find(x=>x.path===current.path&&x.phase==='fresh_created');
    need(!!prior,'actual original directory key');for(const k of DIR_ID)eq(current.before[k],prior.before[k],'same created directory identity '+k);
    if(current.path===RAW||original)eq(current.before,prior.before,'whole stable directory key since creation/materialization');}
  report.disposition={enabled_directory:finalEnabled,raw_directory:finalRaw,copies:COPIES.map(([id,path])=>({id,path,key:copied.get(id)})),raw_members:[],binding_path_queried:false,raw_leaves_queried:false};
  report.status=report.mode==='--materialize'?'MATERIALIZED_ROOT_RECEPTION_PENDING':'PASS_READ_ONLY_PREFLIGHT_ROOT_RECEPTION_PENDING';
}catch(e){report.failure=errorData(e);process.exitCode=78;}
report.key_count=report.keys.length;report.total_read_bytes=report.keys.reduce((s,x)=>s+x.bytes_read,0);
process.stdout.write(JSON.stringify(report,null,2)+'\n');
