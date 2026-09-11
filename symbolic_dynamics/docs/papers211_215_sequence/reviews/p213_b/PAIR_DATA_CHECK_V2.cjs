'use strict';
// DATA-only strict-pair receipt. No scientific execution, imports or writes.
const fs=require('node:fs'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const BASE=ROOT+'docs/papers211_215_sequence/';
const OWN=BASE+'reviews/p213_b/',QA=BASE+'qa/';
const INTAKE=QA+'p213_b_source_root01/',PREP=QA+'p213_b_execution_preparation01/';
const SHA=b=>crypto.createHash('sha256').update(b).digest('hex');
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const stat=s=>Object.fromEntries(fields.map(k=>[k,s[k].toString()]));
const evidence=[];let checks=0;
function ok(v,m){checks++;if(!v)throw Error(m);}
function equal(a,b,m){ok(JSON.stringify(a)===JSON.stringify(b),m);}
function read(path){
  ok(path.startsWith(BASE),'fixed workspace documentary input');
  const a=fs.lstatSync(path,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular leaf');
  const b=fs.readFileSync(path);equal(stat(a),stat(fs.lstatSync(path,{bigint:true})),'stable data read');
  ok(BigInt(b.length)===a.size,'complete read');
  evidence.push({path,bytes:b.length,sha256:SHA(b)});return b;
}
const json=path=>JSON.parse(read(path).toString('utf8'));
const sourceHash='11e631efcc32b1f78771061af134cf9ce3a81d3dc2c4c36b5a966db3a28db623';
const scienceHash='de88736304666d769cd2a863bf91aa9cee97c1de43dae3aa5f7f7d301c492fae';
const initialSeal=read(OWN+'INITIAL_PACKAGE_SHA256SUMS');
ok(SHA(initialSeal)==='b3b8bbff23186602900961e62a013b87aacb402663042f7398759d71693b0acd','accepted initial package pin');
for(const line of initialSeal.toString().trimEnd().split('\n')){
  const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.]+)$/.exec(line);ok(!!m,'manifest row');
  ok(SHA(read(OWN+m[2]))===m[1],'unchanged initial payload');
}
const independent=json(OWN+'INITIAL_DATA_NATIVE.json'), rootReplay=json(INTAKE+'INITIAL_DATA_REPLAY_NATIVE.json');
ok(independent.result.exit_code===0&&rootReplay.exit_code===0,'both initial DATA receipts succeeded');
ok(Buffer.from(independent.result.output).equals(Buffer.from(rootReplay.output)),'whole initial DATA replay output equality');
const interpreted=JSON.parse(independent.result.output.trimEnd().split('\n').at(-1));
equal([interpreted.checks,interpreted.lines,interpreted.states,interpreted.chambers,interpreted.carriers],[44890,19366,461,18872,30],'accepted complete semantic scope');
const initial=read(QA+'p213_b_initial_run01/stdout.bin'), canonical=read(OWN+'canonical_stdout.txt');
ok(initial.length===1124426&&SHA(initial)===scienceHash,'accepted initial bytes');
ok(canonical.equals(initial),'whole initial/canonical raw equality');
const adoption=json(INTAKE+'CANONICAL_ADOPTION_NATIVE.json');
ok(adoption.exit_code===0&&adoption.chunk_id==='8ef147','actual exclusive adoption');
const adopted=JSON.parse(adoption.output);
ok(adopted.status==='EXCLUSIVE_B_CANONICAL_ADOPTED'&&adopted.bytes===initial.length&&adopted.sha256===scienceHash,'adoption receipt');
for(const endpoint of ['source','target']){
  const expected=endpoint==='source'?QA+'p213_b_initial_run01/stdout.bin':OWN+'canonical_stdout.txt';
  ok(adopted[endpoint].path===expected,'adoption exact endpoint');
  equal(adopted[endpoint].key,stat(fs.lstatSync(expected,{bigint:true})),'current adoption endpoint key');
}
const initialKeysRaw=read(QA+'p213_b_initial_run01/keys.before.json');
const initialKeys=JSON.parse(initialKeysRaw);
ok(initialKeys.records.length===20,'accepted twenty shared input records');
const depsRaw=read(PREP+'DEPENDENCIES.proposed.json');
ok(SHA(depsRaw)==='1c0b5d506c285f2df7345668a4b673e92d8efb3b4cc9f403517413e59c785e6b','unchanged accepted dependency list');
const source=read(OWN+'verify.py');ok(SHA(source)===sourceHash,'current science source pin');
const sourceRecord=initialKeys.records.find(r=>r.path===OWN+'verify.py');
equal(sourceRecord.end,stat(fs.lstatSync(OWN+'verify.py',{bigint:true})),'current science source complete key');
const pair=[];
const rawReceiver01=read(INTAKE+'CHECK_strict01_RAW.cjs').toString();
const rawReceiver02=read(INTAKE+'CHECK_strict02_RAW.cjs').toString();
ok(rawReceiver01.replaceAll('strict01','strict02').replaceAll('run01','run02').replaceAll('STRICT01','STRICT02')===rawReceiver02,'root raw receiver exact stage-only delta');
const stages=[
  {name:'strict01',dir:'p213_b_strict_pair_run01',actual:'41e1e7',preflight:'17a2fb',request:'32047e700588d37b474b61bacc82ef5232ccad7daf4ea0f09513ef14b3fe96ff',command:'0f4ec19140f6583f54d81b0998a82ff38067a7656764ef569849c1b24d9f78c3'},
  {name:'strict02',dir:'p213_b_strict_pair_run02',actual:'8f6c7f',preflight:'13a2f2',request:'ae258dae24e81919db55b71993ac84ef6a2946d4f929931e0ee1e9bfe0fdff5a',command:'1f7ae345d1acc9a46561bf71ab666a4dcbdea3042c46eefd6039c244c17a0fd3'}
];
for(const stage of stages){
  const dir=QA+stage.dir+'/';
  const requestRaw=read(PREP+'REQUEST.'+stage.name+'.ready.json');
  ok(SHA(requestRaw)===stage.request,'pinned strict request');
  const request=JSON.parse(requestRaw),native=json(INTAKE+stage.name+'_NATIVE.json');
  equal(native.request,request.proposed_native_request.arguments,'exact actual strict launch arguments');
  ok(SHA(Buffer.from(native.request.cmd))===stage.command,'exact strict command pin');
  ok(native.result.chunk_id===stage.actual&&native.result.exit_code===0&&!native.result.session_id,'actual separately successful strict');
  ok(native.result.output==='P213_B_CAPTURE_EXIT=0\n','actual capture return');
  const grant=read(INTAKE+'GRANT_'+stage.name+'.md').toString();
  ok(grant.includes('GRANT CONSUMED BEFORE SUBMISSION')&&grant.includes(stage.request)&&grant.includes(stage.command),'separate exact consumed grant');
  const preflightEnvelope=json(INTAKE+stage.name+'_PREFLIGHT_NATIVE.json');
  equal(Object.keys(preflightEnvelope).sort(),['input_keys','request_check'],'exact strict preflight envelope');
  const requestCheck=preflightEnvelope.request_check;
  ok(requestCheck.exit_code===0&&requestCheck.chunk_id===(stage.name==='strict01'?'ce61e6':'ee43ff'),'actual request/canonical preflight');
  const checkedRequest=JSON.parse(requestCheck.output);
  equal(checkedRequest.arguments,native.request,'fresh checked launch arguments');
  ok(checkedRequest.request_sha256===stage.request&&checkedRequest.command_sha256===stage.command&&checkedRequest.canonical_bytes===1124426&&checkedRequest.canonical_sha256===scienceHash,'fresh request/source/canonical binding');
  ok(checkedRequest.request_path==='docs/papers211_215_sequence/qa/p213_b_execution_preparation01/REQUEST.'+stage.name+'.ready.json','exact preflight request path');
  const preflight=preflightEnvelope.input_keys;
  ok(preflight.exit_code===0&&preflight.chunk_id===stage.preflight&&!preflight.session_id,'fresh strict preflight');
  const before=read(dir+'keys.before.json'),after=read(dir+'keys.after.json');
  ok(before.equals(after)&&before.equals(initialKeysRaw),'entire shared-input before/after/initial keys equal');
  ok(Buffer.from(preflight.output).equals(before),'entire fresh preflight/before keys equal');
  const out=read(dir+'stdout.bin'),err=read(dir+'stderr.bin'),exit=read(dir+'python.exit');
  ok(out.equals(canonical)&&out.equals(initial),'entire strict/canonical/initial stdout equality');
  ok(err.length===0&&exit.toString()==='0\n','strict status/stderr');
  ok(read(dir+'controller.exit').toString()==='0\n','controller exited zero');
  for(const name of ['controller.stdout','controller.stderr','input-key-cmp.stdout','input-key-cmp.stderr','keys.before.stderr','keys.after.stderr','raw.keys.stderr'])ok(read(dir+name).length===0,'empty control '+name);
  const raw=json(dir+'raw.keys.json');
  ok(raw.schema==='P213_B_EXTERNAL_KEYS_V1'&&raw.mode==='outputs'&&raw.records.length===3&&raw.status==='COMPLETE_EXTERNAL_KEYS_PENDING_RECEPTION','raw report complete');
  let total=0;
  for(const [i,name] of ['stdout.bin','stderr.bin','python.exit'].entries()){
    const r=raw.records[i],bytes=[out,err,exit][i];
    ok(r.path===dir+name&&r.kind==='regular-file'&&r.complete===true&&r.eof===true&&r.close_succeeded===true,'raw exact record');
    equal(Object.keys(r).sort(),['path','kind','complete','eof','close_succeeded','begin','fd_before','bytes','sha256','fd_after','end'].sort(),'raw fields exact');
    for(const phase of ['begin','fd_before','fd_after','end']){
      equal(Object.keys(r[phase]).sort(),fields.slice().sort(),'full ten-field raw key');
      equal(r[phase],r.begin,'stable recorded raw phases');
    }
    equal(r.end,stat(fs.lstatSync(dir+name,{bigint:true})),'current raw key matches capture');
    ok(r.begin.nlink==='1'&&r.bytes===bytes.length&&r.sha256===SHA(bytes),'raw single-link bytes/hash');
    total+=bytes.length;
  }
  ok(raw.total_read_bytes===total,'raw aggregate byte count');
  const rootNative=json(INTAKE+stage.name+'_RAW_RECEPTION_NATIVE.json');
  ok(rootNative.exit_code===0&&rootNative.chunk_id===(stage.name==='strict01'?'3c0f75':'0ff2d2'),'actual root current-input observation');
  const rootData=JSON.parse(rootNative.output);
  ok(rootData.status==='PASS_'+stage.name.toUpperCase()+'_B_RAW_CURRENT_KEYS_FRAMING_ONLY','root current scope');
  equal(rootData.counts,{STATE:461,CHAMBER:18872,CARRIER:30,PASS:1},'root complete framing');
  ok(rootData.lines===19366&&rootData.stdout.bytes===out.length&&rootData.stdout.sha256===SHA(out),'root raw science match');
  const expectedPaths=[PREP+'REQUEST.'+stage.name+'.ready.json',...request.output_files.map(name=>dir+name),INTAKE+'PREFLIGHT_NATIVE.json',...initialKeys.records.filter(r=>r.kind==='regular-file').map(r=>r.path)];
  equal(rootData.pins.map(p=>p.path).sort(),expectedPaths.slice().sort(),'root full thirty-five present input/output inventory');
  for(const record of initialKeys.records.filter(r=>r.kind==='regular-file')){
    const p=rootData.pins.find(p=>p.path===record.path);
    equal(p.key,record.end,'root current shared complete key matches initial');
    ok(p.bytes===record.bytes&&p.sha256===record.sha256,'root current shared bytes/digest');
  }
  // The sole required absence is checked by the root receiver's explicit
  // lstat/ENOENT branch; it is not mislabelled a present pin or reopened here.
  for(const p of rootData.pins.filter(p=>p.path.startsWith(BASE))){
    const bytes=read(p.path);ok(p.bytes===bytes.length&&p.sha256===SHA(bytes),'root workspace raw pin match');
    equal(p.key,stat(fs.lstatSync(p.path,{bigint:true})),'root workspace complete current key');
  }
  pair.push(out);
  console.log('STRICT_DATA_ACCEPTED',stage.name,stage.actual,out.length,SHA(out),'INPUTS',20);
}
ok(pair[0].equals(pair[1]),'whole strict01/strict02 equality');
const cmp=json(INTAKE+'STRICT_RAW_COMPARISONS_NATIVE.json');
ok(cmp.chunk_id==='a42d96'&&cmp.exit_code===0&&cmp.output==='','root actual raw comparison receipt');
console.log(JSON.stringify({status:'B_STRICT_PAIR_DATA_ACCEPTED',checks,strict_runs:2,bytes_per_stdout:1124426,sha256:scienceHash,reused_initial_semantic_checks:44890,reused_lines:19366,shared_input_records:20,current_host_input_observation:'root 3c0f75/0ff2d2 full receipts received; host paths not reopened here',evidence}));
