'use strict';
// Root receipt of source-only preparation and independent source metadata.
// Complete unchanged metadata helper is explicitly run, not any assembler.
const fs=require('node:fs'),crypto=require('node:crypto'),u=require('node:util'),cp=require('node:child_process'),path=require('node:path');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const HERE=QA+'p211_terminal_binding_source_root01',A=QA+'p211_terminal_binding_independent01';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
const reads={},STAT=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];let checks=0;
function need(x,s){checks++;if(!x)throw Error(s);}
function eq(a,b,s){need(u.isDeepStrictEqual(a,b),s);}
function pin(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function rich(p){
 need(path.isAbsolute(p)&&(p.startsWith(ROOT+'/')||['/usr/bin/node','/usr/bin/cmp'].includes(p)),'exact workspace or named native tool scope');
 const a=fs.lstatSync(p,{bigint:true});need(a.isFile()&&!a.isSymbolicLink()&&fs.realpathSync(p)===p,'ordinary exact path');
 const raw=fs.readFileSync(p),b=fs.lstatSync(p,{bigint:true});const stat=STAT.map(k=>String(a[k]));
 eq(STAT.map(k=>String(b[k])),stat,'stable complete selected stat');
 const key={...pin(raw),stat};need(BigInt(raw.length)===b.size,'whole read size');
 if(reads[p])eq(key,reads[p],'unchanged repeated root original');reads[p]=key;return {raw,key};
}
function read(p){return rich(p).raw;}
function obj(p){return JSON.parse(read(p));}
function put(n,v){const b=Buffer.isBuffer(v)?v:Buffer.from(JSON.stringify(v,null,2)+'\n');const fd=fs.openSync(HERE+'/'+n,'wx',0o600);try{fs.writeFileSync(fd,b);fs.fsyncSync(fd);}finally{fs.closeSync(fd);}}
function seal(base,count,digest){
 const raw=read(base+'/SHA256SUMS');eq(pin(raw).sha256,digest,'exact full independent seal');need(raw.at(-1)===10,'whole manifest LF');
 const rows={},dirs=new Set(['.']);
 for(const line of raw.toString().trimEnd().split('\n')){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(!!m,'manifest row');const n=m[2];
  need(!n.startsWith('/')&&!n.split('/').some(x=>!x||x==='.'||x==='..')&&!rows[n]&&n!=='SHA256SUMS','unique safe nonself row');rows[n]=m[1];
  eq(pin(read(base+'/'+n)).sha256,m[1],'whole payload');let par=path.posix.dirname(n);while(par!=='.'){dirs.add(par);par=path.posix.dirname(par);}}
 const files=[],actualDirs=['.'];function walk(d){for(const n of fs.readdirSync(d).sort()){const p=d+'/'+n,s=fs.lstatSync(p);need(!s.isSymbolicLink(),'no alias tree');if(s.isDirectory()){actualDirs.push(path.relative(base,p));walk(p);}else{need(s.isFile(),'ordinary tree file');files.push(path.relative(base,p));}}}walk(base);
 eq(files.sort(),[...Object.keys(rows),'SHA256SUMS'].sort(),'whole file membership');eq(actualDirs.sort(),[...dirs].sort(),'whole directory membership');need(Object.keys(rows).length===count,'whole payload count');return rows;
}
function record(n,label){need(n.request&&typeof n.request.cmd==='string'&&n.result&&n.result.exit_code===0&&!n.result.session_id,'actual settled native '+label);need(typeof n.result.output==='string'&&!n.result.output.includes('tokens truncated'),'complete actual stream '+label);return Buffer.from(n.result.output);}
function command(label,argv,timeout){
 const at={argv,cwd:ROOT,environment:ENV,stdin:'empty pipe',timeout_ms:timeout,started_utc:new Date().toISOString(),executable:rich(argv[0]).key};put(label+'.ATTEMPT.json',at);
 const r=cp.spawnSync(argv[0],argv.slice(1),{cwd:ROOT,env:ENV,input:Buffer.alloc(0),timeout,maxBuffer:4*1024*1024,encoding:null});
 const out=r.stdout||Buffer.alloc(0),err=r.stderr||Buffer.alloc(0);put(label+'.stdout.raw',out);put(label+'.stderr.raw',err);
 const n={...at,ended_utc:new Date().toISOString(),status:r.status,signal:r.signal,error:r.error?{name:r.error.name,message:r.error.message,code:r.error.code||null}:null,stdout:pin(out),stderr:pin(err)};put(label+'.NATIVE.json',n);
 need(r.status===0&&r.signal===null&&!r.error&&err.length===0,'actual native success '+label);eq(rich(argv[0]).key,at.executable,'native tool full unchanged');return out;
}
need(process.cwd()===ROOT,'literal root cwd');eq({...process.env},ENV,'literal ENV4 only');
read(__filename);read(HERE+'/AUTHORITY.md');put('EXECUTED_CAPTURE_SOURCE.js',read(__filename));
seal(A,7,'0efe4f74f47030cef2f2cdbe9c73b2cda50b1f5fd1fe7c2203a15f9fccbc395e');
const source=read(A+'/audit_metadata.js');eq(pin(source),{bytes:20986,sha256:'f68572b2d12ce9a444c4df7784639380da2c68935c7e3e633d8c5cc54d065f44'},'fully read independent source exact');
const n=obj(A+'/NATIVE_CHECK.json'),original=record(n,'independent metadata');eq(pin(original),{bytes:118870,sha256:'471c6feb21760d9b091d5c969f769f6924dfab6a9372e1a8766d344491346664'},'whole original output identity');
const o=JSON.parse(original);need(o.checks===22191&&o.unique_workspace_files===190&&Object.keys(o.read_pins).length===190,'whole original metadata scope');eq(o.read_stat_schema,STAT,'full selected stat schema');
function prior(){for(const [rel,p] of Object.entries(o.read_pins)){need(!rel.startsWith('/')&&rel.split('/').every(x=>x&&x!=='.'&&x!=='..'),'literal original relative');const x=rich(ROOT+'/'+rel);eq(pin(x.raw),p,'all190 original byte pins');eq(x.key.stat,o.read_stats[rel],'all190 original selected stats');}}
prior();put('INPUTS_BEFORE.json',reads);put('INDEPENDENT_ORIGINAL_STDOUT.raw',original);
const actual=command('01_metadata_reuse',['/usr/bin/node',A+'/audit_metadata.js'],60000);eq(actual,original,'entire actual root and independent output raw identical');
eq(command('02_raw_compare',['/usr/bin/cmp','--',HERE+'/INDEPENDENT_ORIGINAL_STDOUT.raw',HERE+'/01_metadata_reuse.stdout.raw'],60000),Buffer.alloc(0),'actual empty raw comparison result');
const close=obj(A+'/CLOSING_NATIVE.json');eq(record(close.source_read,'whole source closing read'),source,'entire actual source read bound');
const c=JSON.parse(record(close.metadata_closing,'metadata closing'));need(c.original_execution_chunk==='cd446b'&&c.input_pins_and_full_selected_stats_rechecked===190&&c.source_lines===244&&c.source_edited_since_execution===false&&c.host_referents_read===0&&c.ambient_environment_read===false,'complete saved independent closure role');
eq(c.original_output_pin,pin(original),'whole saved closing output pin');for(const [name,p] of Object.entries(c.files))eq(pin(read(A+'/'+name)),p,'entire closing originals');
const nr=obj(A+'/NATIVE_READS.json');need(nr.records.length===22,'all22 independent reads');let sourceBindings=0;
for(let i=0;i<nr.records.length;i++){const r=nr.records[i],raw=record(r,'independent read '+i),m=/^sed -n '(\d+),(\d+)p' (\S+)$/.exec(r.request.cmd);if(m&&i!==0){const all=read(ROOT+'/'+m[3]).toString().match(/[^\n]*\n|[^\n]+$/g)||[];eq(raw,Buffer.from(all.slice(Number(m[1])-1,Number(m[2])).join('')),'whole source slice '+i);sourceBindings++;}}
const f=obj(A+'/FINDINGS.json');eq(f.census,{critical:0,major:0,minor:0},'actual zero source finding census');eq(f.findings,[],'actual empty source findings');need(f.verdict==='GO_SOURCE_RECEPTION_ONLY'&&f.operational_status==='HOLD_OPERATIONAL'&&!f.whole_round2_accepted_here&&!f.root_authority_issued_here,'source authority remains separate');
for(const name of ['SOURCE_REPORT.md']){for(const match of read(A+'/'+name).toString().matchAll(/!?\[[^\]\n]*\]\(([^)\n]+)\)/g)){const target=path.resolve(A,match[1].split('#')[0]);need(target.startsWith(ROOT+'/'),'workspace source report link');read(target);}}
prior();seal(A,7,'0efe4f74f47030cef2f2cdbe9c73b2cda50b1f5fd1fe7c2203a15f9fccbc395e');
for(const [p,k] of Object.entries({...reads}))eq(rich(p).key,k,'all root consumed original keys close');put('INPUTS_AFTER.json',reads);
const result={status:'PASS_ROOT_TERMINAL_BINDING_SOURCE_AND_INDEPENDENT_METADATA_RECEPTION_ONLY',checks,read_paths:Object.keys(reads).length,independent_payloads:7,submitted_payloads:o.submitted.payloads,plan_input_pins:166,independent_checks:22191,complete_independent_key:190,independent_native_reads:22,raw_source_read_bindings:sourceBindings,whole_reused_output:pin(actual),native_cmp_exit:0,assembly_executed:false,host_key_refreshed:false,operational_authority:false,round2_accepted_here:false,new_science:0,new_builds:0,new_page_views:0,paper_complete:false,external:'OWNER_AMBER / HOLD_EXTERNAL'};
put('RESULT.json',result);process.stdout.write(JSON.stringify(result)+'\n');
