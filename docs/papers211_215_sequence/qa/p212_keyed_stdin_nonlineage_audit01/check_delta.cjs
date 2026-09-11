'use strict';
// Auditor-owned documentary data/text checker. No reviewed language evaluation, import, AST or syntax testing.
const fs=require('fs'),cp=require('child_process'),crypto=require('crypto'),path=require('path');
const BASE='docs/papers211_215_sequence/qa/',SRC=BASE+'p212_keyed_stdin_source_delta01/',OWN=BASE+'p212_keyed_stdin_nonlineage_audit01/';
const before=JSON.parse(fs.readFileSync(OWN+'INPUTS_BEFORE.json','utf8'));
const allow=new Map(before.inputs.map(r=>[r.path,r]));
let checks=0;
function ok(v,m){checks++;if(!v)throw Error(m);}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex');}
function read(p){ok(allow.has(p),'fixed before-pin path '+p);const b=fs.readFileSync(p);ok(sha(b)===allow.get(p).sha256,'unchanged complete pin '+p);return b;}
function txt(p){const b=read(p),t=b.toString('utf8');ok(Buffer.from(t).equals(b),'raw UTF8 round trip '+p);return t;}
function json(p){const t=txt(p),v=JSON.parse(t);ok(JSON.stringify(v,null,2)+'\n'===t,'complete canonical JSON '+p);return v;}
function eq(a,b,m){ok(JSON.stringify(a)===JSON.stringify(b),m);}
function lf(b){let n=0;for(const c of b)if(c===10)n++;return n;}
function splitLines(b){const t=b.toString('utf8');ok(Buffer.from(t).equals(b),'whole UTF8 roundtrip');ok(t.endsWith('\n'),'source terminal LF');return t.slice(0,-1).split('\n');}
function reconstruct(old,newer,diff){
 const a=splitLines(old),b=splitLines(newer);
 if(diff.length===0){ok(old.equals(newer),'actually empty diff is raw equal');return{hunks:0,added:0,removed:0,old_lines:a.length,new_lines:b.length};}
 const ds=splitLines(diff);ok(ds[0].startsWith('--- ')&&ds[1].startsWith('+++ '),'exact unified headers');
 const rebuilt=[],reverse=[];let oi=0,ni=0,i=2,hunks=0,added=0,removed=0;
 while(i<ds.length){
  const m=ds[i++].match(/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?:.*)$/);
  ok(m,'full hunk syntax');hunks++;
  const oldStart=Number(m[1]),oldCount=m[2]===undefined?1:Number(m[2]);
  const newStart=Number(m[3]),newCount=m[4]===undefined?1:Number(m[4]);
  const ob=oldCount===0?oldStart:oldStart-1,nb=newCount===0?newStart:newStart-1;
  ok(ob>=oi&&nb>=ni,'ordered nonoverlap hunks');
  eq(a.slice(oi,ob),b.slice(ni,nb),'unchanged hunk gap exact lines');
  rebuilt.push(...a.slice(oi,ob));reverse.push(...b.slice(ni,nb));oi=ob;ni=nb;
  let oc=0,nc=0;
  while(i<ds.length&&!ds[i].startsWith('@@ ')){
   const row=ds[i++],tag=row[0],body=row.slice(1);ok([' ','+','-'].includes(tag),'only exact hunk line tags');
   if(tag!=='+' ){ok(a[oi]===body,'actual old line');oi++;oc++;reverse.push(body);}
   if(tag!=='-' ){ok(b[ni]===body,'actual new line');ni++;nc++;rebuilt.push(body);}
   if(tag==='+')added++;if(tag==='-')removed++;
  }
  ok(oc===oldCount&&nc===newCount,'complete hunk cardinality');
 }
 eq(a.slice(oi),b.slice(ni),'whole trailing unchanged bytes');
 rebuilt.push(...a.slice(oi));reverse.push(...b.slice(ni));
 ok(Buffer.from(rebuilt.join('\n')+'\n').equals(newer),'whole raw forward reconstruction');
 ok(Buffer.from(reverse.join('\n')+'\n').equals(old),'whole raw reverse reconstruction');
 return{hunks,added,removed,old_lines:a.length,new_lines:b.length};
}
const origin=json(SRC+'SOURCE_ORIGIN.json'),pairs=[];
ok(origin.derivatives.length===19,'19 declared exact pairs');
for(const pair of origin.derivatives){
 const old=read(pair.old_path),current=read(pair.new_path);
 const archivePath=SRC+'diffs/'+pair.name.replaceAll('/','__')+'.diff';
 const frozen=read(archivePath),request={executable:'diff',argv:['-u',pair.old_path,pair.new_path]};
 const actual=cp.spawnSync(request.executable,request.argv,{encoding:null,maxBuffer:2*1024*1024});
 const record={request,return:{status:actual.status,signal:actual.signal,error:actual.error?String(actual.error):null,
  stdout_utf8:actual.stdout.toString('utf8'),stderr_utf8:actual.stderr.toString('utf8'),
  stdout_bytes:actual.stdout.length,stderr_bytes:actual.stderr.length,stdout_sha256:sha(actual.stdout),stderr_sha256:sha(actual.stderr)}};
 ok(Buffer.from(record.return.stdout_utf8).equals(actual.stdout)&&Buffer.from(record.return.stderr_utf8).equals(actual.stderr),'actual raw transport roundtrip');
 ok(!actual.error&&actual.signal===null&&actual.stderr.length===0,'successful documentary diff call');
 ok(actual.status===(old.equals(current)?0:1),'exact diff status');
 ok(actual.stdout.equals(frozen),'complete actual raw diff equals archived bytes including headers '+pair.name);
 pairs.push({name:pair.name,old_path:pair.old_path,new_path:pair.new_path,old_bytes:old.length,new_bytes:current.length,
  old_sha256:sha(old),new_sha256:sha(current),diff_path:archivePath,...reconstruct(old,current,actual.stdout),native:record});
}
const programs=pairs.filter(p=>/\.(py|js)$/.test(p.name));
ok(programs.length===7,'seven complete programs');
const sum=rows=>({old_lines:rows.reduce((n,r)=>n+r.old_lines,0),new_lines:rows.reduce((n,r)=>n+r.new_lines,0),
 old_bytes:rows.reduce((n,r)=>n+r.old_bytes,0),new_bytes:rows.reduce((n,r)=>n+r.new_bytes,0),
 hunks:rows.reduce((n,r)=>n+r.hunks,0),added:rows.reduce((n,r)=>n+r.added,0),removed:rows.reduce((n,r)=>n+r.removed,0)});
eq(sum(programs),{old_lines:2519,new_lines:2679,old_bytes:139752,new_bytes:148546,hunks:32,added:204,removed:44},'independent whole program arithmetic');
eq(sum(pairs),{old_lines:5831,new_lines:6208,old_bytes:285595,new_bytes:313551,hunks:69,added:654,removed:277},'independent whole derivative arithmetic');
const frontier=json(SRC+'FRONTIER.json'),oldfront=json(BASE+'p212_preprobe_bootstrap_preparation01/FRONTIER.json');
eq(Object.keys(frontier),['schema','status','author_probe_execution_allowed','targets','allowed_components','closure_gaps'],'whole frontier top keys');
ok(frontier.author_probe_execution_allowed===false,'frontier no author grant');
ok(frontier.targets.length===164&&frontier.allowed_components.length===204,'literal cardinalities');
const modeCounts={};for(const t of frontier.targets)modeCounts[t.mode]=(modeCounts[t.mode]||0)+1;
eq(modeCounts,{metadata:5,file:110,optional_file:32,membership:5,optional_directory:11,absent:1},'all modes counts');
const allowed=new Set(frontier.allowed_components);
eq([...allowed].sort(),frontier.allowed_components,'unique ordered components');
eq(frontier.targets.map(t=>t.path),[...new Set(frontier.targets.map(t=>t.path))].sort(),'unique ordered targets');
for(const p of frontier.allowed_components){
 ok(path.posix.normalize(p)===p&&p.startsWith('/')&&!p.startsWith('//')&&!p.includes('\0'),'literal component');
 let q=p;while(true){ok(allowed.has(q),'complete source-level ancestor spelling');if(q==='/')break;q=path.posix.dirname(q);}
}
for(const t of frontier.targets){
 eq(Object.keys(t),['path','mode','role','origin','max_bytes','capture_hex','max_members','expected_names'],'complete target keys');
 ok(allowed.has(t.path),'target within allowed strings');
 ok(typeof t.role==='string'&&typeof t.origin==='string','role/origin strings');
 ok(Number.isInteger(t.max_bytes)&&t.max_bytes>=0&&t.max_bytes<=134217728,'finite bytes');
 ok(typeof t.capture_hex==='boolean','capture boolean');
 ok(Number.isInteger(t.max_members)&&t.max_members>=0&&t.max_members<=320,'member ceiling');
 if(t.mode==='membership'){
  eq(t.expected_names,[...new Set(t.expected_names)].sort(),'all actual membership names unique ordered');
  ok(t.expected_names.length<=t.max_members,'membership guard size');
  for(const n of t.expected_names)ok(typeof n==='string'&&n!==''&&n!=='.'&&n!=='..'&&!n.includes('/')&&!n.includes('\0')&&Buffer.byteLength(n)<=255,'all literal member names');
 }else ok(t.max_members===0&&t.expected_names===null,'no implicit enumeration');
 if(!['file','optional_file'].includes(t.mode))ok(t.max_bytes===0&&t.capture_hex===false,'metadata no byte channel');
}
const stdin='/root/autodl-tmp/symbolic_dynamics/'+BASE+'p212_keyed_stdin_input01/empty.stdin';
const target=frontier.targets.find(t=>t.path===stdin);ok(target,'one selected stdin target');
eq([target.mode,target.max_bytes,target.capture_hex,target.max_members,target.expected_names],['file',0,true,0,null],'exact stdin read policy');
ok(!allowed.has('/dev')&&!allowed.has('/dev/null')&&!frontier.targets.some(t=>t.path==='/dev/null'),'old device absent from new source frontier only');
const oldRows=new Map(oldfront.targets.map(t=>[JSON.stringify(t),t]));
const unchanged=frontier.targets.filter(t=>oldRows.has(JSON.stringify(t)));
ok(unchanged.length===159,'159 complete unchanged target values');
const oldTargets=new Set(oldfront.targets.map(t=>JSON.stringify(t))),newTargets=new Set(frontier.targets.map(t=>JSON.stringify(t)));
const removedTargets=oldfront.targets.filter(t=>!newTargets.has(JSON.stringify(t)));
const addedTargets=frontier.targets.filter(t=>!oldTargets.has(JSON.stringify(t)));
ok(removedTargets.length===5&&addedTargets.length===5,'all five old/new target replacements');
const removedComponents=oldfront.allowed_components.filter(p=>!allowed.has(p));
const oldAllowed=new Set(oldfront.allowed_components),addedComponents=frontier.allowed_components.filter(p=>!oldAllowed.has(p));
ok(removedComponents.length===8&&addedComponents.length===8,'all component replacement cardinality');
eq(frontier.targets.filter(t=>t.mode==='membership'),oldfront.targets.filter(t=>t.mode==='membership'),'all five whole membership rows unchanged');
ok(frontier.targets.filter(t=>t.mode==='membership').reduce((n,t)=>n+t.expected_names.length,0)===292,'all 292 actual member names');
eq(frontier.closure_gaps.slice(0,7),oldfront.closure_gaps,'all seven inherited closure gaps');
ok(frontier.closure_gaps.length===8&&frontier.closure_gaps[7].includes('preserved and unsatisfied'),'eighth gap keeps old failure open');
const iface=json(SRC+'INTERFACE.disabled.json'),auth=json(SRC+'AUTHORIZATION.disabled.json'),outerTemplate=json(SRC+'OUTER_INTERFACE.disabled.json');
ok(iface.enabled===false&&auth.enabled===false&&outerTemplate.enabled===false,'all three disabled');
ok(iface.inputs.length===0&&iface.driver_pin===null&&iface.phase===null,'driver no active inputs');
for(const v of Object.values(iface.receipts))ok(v===null,'driver no receipts');
for(const k of ['source_receipt','trust_receipt','frontier'])ok(auth[k].pin===null,'observer disabled pins remain null');
eq(iface.policy.stdin,{path:stdin,role:'stdin',kind:'file',content:{bytes:0,sha256:sha(Buffer.alloc(0))},handoff_offset:0},'complete exact driver stdin policy');
const cap=json(SRC+'companions/CAPTURE_CONTRACT.json'),oldcap=json(BASE+'p212_execution_scope_source_amendment01/companions/CAPTURE_CONTRACT.json');
const capRest=JSON.parse(JSON.stringify(cap)),oldcapRest=JSON.parse(JSON.stringify(oldcap));delete capRest.commands.stdin;delete oldcapRest.commands.stdin;
eq(capRest,oldcapRest,'whole companion change confined to commands.stdin');
ok(cap.commands.stdin.path===stdin&&cap.commands.stdin.kind==='file'&&cap.commands.stdin.content.bytes===0,'capture stdin literal');
const textByName=Object.fromEntries(programs.map(p=>[p.name,txt(p.new_path)]));
for(const name of ['observe.py','outer_contract.py','driver.js','python_runtime_probe.py','product_capture.js'])
 ok(textByName[name].includes("'/p212_keyed_stdin_input01/empty.stdin'"),'same exact selected stdin constant '+name);
ok(textByName['outer_contract.py'].includes("DRIVER_SHA = '"+sha(read(SRC+'driver.js'))+"'"),'full driver hash closure');
for(const c of origin.unchanged_companions)ok(textByName['driver.js'].includes('"path": "'+c.path+'"')&&textByName['driver.js'].includes('"sha256": "'+sha(read(c.path))+'"'),'all old whole companion pins '+c.name);
ok(textByName['driver.js'].includes('"sha256": "'+sha(read(SRC+'companions/CAPTURE_CONTRACT.json'))+'"'),'changed whole companion SHA embedded');
const observer=textByName['observe.py'],outer=textByName['outer_contract.py'],driver=textByName['driver.js'];
function slice(text,start,end){const a=text.indexOf(start),z=text.indexOf(end,a+start.length);ok(a>=0&&z>a,'exact source slice delimiters');return text.slice(a,z);}
const oldObserve=txt(origin.derivatives.find(d=>d.name==='observe.py').old_path);
for(const [start,end]of [['class Stamp(', 'def observe_target('],['def control(', "if __name__ == '__main__':"]])
 ok(Buffer.from(slice(observer,start,end)).equals(Buffer.from(slice(oldObserve,start,end))),'complete unchanged observer core block');
const oldOuter=txt(origin.derivatives.find(d=>d.name==='outer_contract.py').old_path);
ok(Buffer.from(slice(outer,'def full_stat(','def projection(')).equals(Buffer.from(slice(oldOuter,'def full_stat(','def projection('))),'entire inherited outer native decoder unchanged');
const oldProbe=txt(origin.derivatives.find(d=>d.name==='python_runtime_probe.py').old_path),probe=textByName['python_runtime_probe.py'];
ok(Buffer.from(slice(probe,"        data = (ctypes.c_ubyte * 256)()","        if p == STDIN_FILE:")).equals(Buffer.from(slice(oldProbe,"        data = (ctypes.c_ubyte * 256)()","        rows.append("))),'entire inherited probe native decoder unchanged');
const ob=slice(outer,'def open_stdin():','def snapshot():');
ok(ob.indexOf("expected stdin key before any byte read")<ob.indexOf('raw = os.read(fd,1)'),'outer expected key precedes byte read');
ok(ob.indexOf("observation['raw_hex'] = raw.hex()")<ob.indexOf("need(not raw"),'outer sentinel retained before refusal');
ok(ob.includes("actual_offset_query':None")&&ob.includes("source_handoff_offset'] = 0"),'outer offset labelled source-only');
ok(outer.includes('process = subprocess.Popen(argv,cwd=ROOT,env=ENV8,stdin=stdin_fd,'),'actual outer verified fd passed');
const dr=slice(driver,'function openStdin(label)','async function nativeCapture(');
ok(dr.indexOf('expected stdin key before any byte read')<dr.indexOf('fs.readSync(fd,buffer,0,1,null)'),'driver expected key precedes byte read');
ok(dr.indexOf('observation.raw_hex=')<dr.indexOf('need(count===0'),'driver sentinel recorded before refusal');
ok(dr.includes('actual_offset_query:null')&&dr.includes('source_handoff_offset=0'),'driver offset source-only');
ok(driver.includes('stdio:[stdinFd,outFd,errFd]'),'actual driver verified fd passed');
ok(dr.includes("role!=='body'")&&dr.includes('symlink_target===null'),'driver nonbody and physical chain guards');
const handoff=txt(SRC+'HANDOFF.md'),erratum=txt(BASE+'p212_keyed_stdin_linecount_erratum01/ERRATUM.md');
ok(handoff.includes('2,779 lines / 148,546 bytes'),'historical error unchanged');
ok(erratum.includes('2,679 lines / 148,546 bytes'),'exact count correction exists');
ok(sha(read(BASE+'p212_keyed_stdin_linecount_erratum01/ERRATUM.md'))==='b77fe4fea57429edd7090dbc88387ae2e9280c4be1ea2bd5d059f9bc936ac80b','fixed exact erratum');
for(const p of before.inputs)ok(sha(read(p.path))===p.sha256,'complete endpoint unchanged');
console.log(JSON.stringify({kind:'INDEPENDENT_DOCUMENTARY_RAW_DIFF_AND_DATA_CHECK_NOT_REVIEWED_PROGRAM_EXECUTION',checks,
 program_totals:sum(programs),derivative_totals:sum(pairs),frontier:{modeCounts,unchanged_targets:unchanged.length,removedTargets,addedTargets,removedComponents,addedComponents,membership_rows:5,membership_names:292,closure_gaps:frontier.closure_gaps},
 corrected_minor:{id:'P212-KSI-F1',independent_count:2679,bytes:148546,exact_combination_only:true},
 input_count:before.inputs.length,pairs},null,2));

