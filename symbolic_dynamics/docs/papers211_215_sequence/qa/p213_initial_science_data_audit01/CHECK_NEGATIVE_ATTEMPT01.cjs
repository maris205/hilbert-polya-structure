'use strict';
// In-memory mutations of received DATA. Never generates a new carrier/orbit,
// invokes submitted sources, or follows a data path into the filesystem.
const fs=require('node:fs'),crypto=require('node:crypto');
const Q='docs/papers211_215_sequence/qa/',A=Q+'p213_initial_science_data_audit01/',R=Q+'p213_initial_science_run01/',B=Q+'p213_initial_science_preparation01/BINDING.proposed.json',S='papers/213-receiver-limited-cyclic-transfer/verify.py',W=Q+'p213_initial_science_enabled01/run_science.py';
const parser=Q+'p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs',reader=Q+'p213_initial_science_enabled_root01/READ_FIXED.cjs';
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
if(digest(fs.readFileSync(parser))!=='9d6e081b7c8940f6730cc41c62bfc67862738eb49ded8f4021b6875583120471'||digest(fs.readFileSync(reader))!=='f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7')throw Error('EXACT_REVIEWED_PURE_HELPER_PINS');
const make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs'),{parseIntegerJSON,canonicalIntegerJSON}=require('../p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs');
const r=make(new Set([parser,reader,B,R+'stdout.bin',R+'stderr.bin',R+'runtime_control.bin',A+'CHECK_NATIVE.json',A+'CONTROL_DATA.cjs',A+'SCIENCE_DATA.cjs',A+'CHECK_NEGATIVE.cjs']));for(const p of r.keys.keys())throw Error('NONEMPTY_READER');
for(const p of[parser,reader,B,R+'stdout.bin',R+'stderr.bin',R+'runtime_control.bin',A+'CHECK_NATIVE.json',A+'CONTROL_DATA.cjs',A+'SCIENCE_DATA.cjs',A+'CHECK_NEGATIVE.cjs'])r.read(p);
const source=JSON.parse(r.read(A+'CHECK_NATIVE.json').toString('utf8')),baseline=JSON.parse(source.native.output),keys=new Map(baseline.keys.map(k=>[k.path,k]));
if(source.native.exit_code!==0||baseline.status!=='PASS_INDEPENDENT_INITIAL_CAPTURE_CONTROL_AND_BOUNDED_SCIENCE_DATA')throw Error('ACTUAL_BASELINE_REQUIRED');
for(const p of[B,R+'stdout.bin',R+'stderr.bin',R+'runtime_control.bin',A+'CONTROL_DATA.cjs',A+'SCIENCE_DATA.cjs'])r.need(r.equal(r.keys.get(p),keys.get(p)),'SAME_CURRENT_BASELINE_KEY '+p);
const x=parseIntegerJSON(r.read(R+'runtime_control.bin').toString('ascii')).data,binding=parseIntegerJSON(r.read(B).toString('ascii')).data,out=r.read(R+'stdout.bin');
const external={sources:Object.fromEntries([W,S].map(p=>['/root/autodl-tmp/symbolic_dynamics/'+p,keys.get(p)])),raw:{stdout:keys.get(R+'stdout.bin'),stderr:keys.get(R+'stderr.bin'),control:keys.get(R+'runtime_control.bin')}};
const control=require('./CONTROL_DATA.cjs'),science=require('./SCIENCE_DATA.cjs');
const findings=[];let controls=0,scientific=0,parsers=0;
function rejected(name,fn,expected){let message=null;try{fn();}catch(e){message=e.message;}r.need(typeof message==='string'&&message.includes(expected),'NEGATIVE_REJECTION '+name+' expected '+expected+' observed '+message);findings.push({name,rejected:true,message});}
function c(name,mutate,expected){controls++;const y=structuredClone(x);mutate(y);rejected(name,()=>control(y,binding,external),expected);}
function t(name,edit,expected,sameLength=true){scientific++;const changed=Buffer.from(edit(out.toString('ascii')),'ascii');r.need(!changed.equals(out),'MUTATION_ACTUALLY_CHANGED '+name);if(sameLength)r.need(changed.length===out.length,'SAME_LENGTH_DEEP_MUTATION '+name);rejected(name,()=>science(changed),expected);}
c('unknown top-level field',y=>{y.extra=true;},'complete initial science control exact fields');
c('numeric producer acceptance instead of false',y=>{y.runtime_accepted=0n;},'producer explicitly pending runtime_accepted');
c('missing second file pass',y=>{y.files.pop();},'exactly two finite passes');
c('missing original before dictionary entry',y=>{delete y.before_keys[binding.files[0].lexical];},'whole before dictionary exact fields');
c('large metadata integer changed by one',y=>{y.before_keys[binding.files[0].lexical].fd_before.st_mtime_ns+=1n;},'path/fd identity');
c('large metadata collapsed to Number',y=>{y.before_keys[binding.files[0].lexical].fd_before.st_mtime_ns=Number(y.before_keys[binding.files[0].lexical].fd_before.st_mtime_ns);},'exact integer token');
c('before file falsely non-EOF',y=>{y.before_keys[binding.files[0].lexical].eof=false;},'actual EOF');
c('absent zip errno substituted',y=>{y.before_keys['/usr/lib/python310.zip'].begin.absence.errno=20n;},'exact ENOENT');
c('closing file extra stat field',y=>{y.after_keys[binding.files[0].lexical].closing.final_lstat.extra=0n;},'exact fields');
c('changed source load hash',y=>{y.science.source_load.sha256_of_read_bytes='0'.repeat(64);},'whole loaded-source key equality');
c('unreported compilation',y=>{y.science.compile_completed=false;},'producer completed compile_completed');
c('changed isolated-dictionary fact',y=>{y.science.globals_policy.globals_equal_locals=false;},'entire isolated dictionary/shared-builtins policy');
c('missing phase module snapshot',y=>{y.module_snapshots.pop();},'seven actual module sampling points');
c('changed module row copied top only',y=>{y.helper_modules[0][1]=false;},'full top/snapshot duplicate');
c('integer launch flag substituted by bool',y=>{y.early_launch[1][0][1]=['value',false];},'typed flag debug');
c('missing raw maps phase',y=>{y.maps.pop();},'all five raw maps');
c('map byte-count off by one',y=>{y.maps[0].byte_count+=1n;},'complete ASCII raw map bytes');
c('parsed map inode off by one',y=>{y.maps[0].parsed[0].inode+=1n;},'every independent parsed map field');
c('claimed extra cached environment success field',y=>{y.pre_science.environment_matches=1n;},'cached environment pre_science');
c('output descriptor incorrectly reused',y=>{y.outputs_final['2']=structuredClone(y.outputs_final['1']);},'permanent output descriptor identity');
c('stdout extent differs from original',y=>{y.post_science.outputs['1'].st_size+=1n;},'exact scientific output size');
c('control descriptor written before final capture',y=>{y.outputs_begin['3'].st_size=1n;},'all initial captures empty');
c('file read total understated',y=>{y.total_file_read_bytes-=1n;},'two passes plus independent source-load accounting');
const modifyLine=(text,predicate,edit)=>{const lines=text.split('\n'),i=lines.findIndex(predicate);r.need(i>=0,'MUTATION_TARGET_EXISTS');lines[i]=edit(lines[i]);return lines.join('\n');};
t('scientific header changed',s=>s.replace('P213_VERIFY_V1','P213_VERIFY_V2'),'exact header');
t('scientific parameter range changed',s=>s.replace('n_max=6','n_max=7'),'exact header');
t('word mask bit altered',s=>modifyLine(s,l=>l.startsWith('WORD '),l=>l.replace(/ s=1/,' s=0')),'all masks once');
t('word first-failure status swapped',s=>{const lines=s.split('\n'),i=lines.findIndex(l=>l.startsWith('WORD ')&&l.includes(' status=PARITY ')),j=lines.findIndex(l=>l.startsWith('WORD ')&&l.includes(' status=SHORT_PEAK '));r.need(i>=0&&j>=0,'BRANCH_SWAP_PRESENT');lines[i]=lines[i].replace(' status=PARITY ',' status=SHORT_PEAK ');lines[j]=lines[j].replace(' status=SHORT_PEAK ',' status=PARITY ');return lines.join('\n');},'independent first-failure status');
t('word interval certificate altered',s=>modifyLine(s,l=>l.startsWith('WORD ')&&l.includes('status=ACCEPTED')&&!l.includes('intervals=-'),l=>l.replace(/intervals=([0-9]),/,(a,b)=>'intervals='+((+b+1)%6)+',')),'complete first-failure interval prefix');
t('word reported product changed',s=>modifyLine(s,l=>l.startsWith('WORD ')&&l.includes(' status=ACCEPTED ')&&l.includes(' weight=1 '),l=>l.replace(' weight=1 ',' weight=2 ')),'reported interval weight');
t('target fixed time altered',s=>modifyLine(s,l=>l.startsWith('TARGET ')&&l.includes(' tau=1 '),l=>l.replace(' tau=1 ',' tau=0 ')),'reported first fixed time');
t('target inverse count changed',s=>modifyLine(s,l=>l.startsWith('TARGET ')&&l.includes(' indegree=2 '),l=>l.replace(' indegree=2 ',' indegree=3 ')),'reported indegree');
t('target fixed product changed',s=>modifyLine(s,l=>l.startsWith('TARGET ')&&l.includes(' fixed_product=2 '),l=>l.replace(' fixed_product=2 ',' fixed_product=3 ')),'reported fixed product');
t('carrier sharp height changed',s=>modifyLine(s,l=>l.startsWith('CARRIER ')&&l.includes(' height=1 '),l=>l.replace(' height=1 ',' height=2 ')),'reported height');
t('carrier status census changed',s=>modifyLine(s,l=>l.startsWith('CARRIER ')&&l.includes('ACCEPTED:1,'),l=>l.replace('ACCEPTED:1,','ACCEPTED:2,')),'complete carrier status census');
t('global word count changed',s=>s.replace(' words=17990 ',' words=17991 '),'exact TOTAL words');
t('source assertion total changed',s=>s.replace('PASS checks=25015','PASS checks=25016'),'source assertion multiplicity');
t('truncated original scientific raw',s=>s.slice(0,-1),'exact raw byte length',false);
t('extra scientific LF',s=>s+'\n','exact raw byte length',false);
for(const [name,raw,expected]of[['duplicate JSON key','{"x":1,"x":2}','duplicate'],['floating point integer-control token','{"x":1.0}','integer'],['JSON trailing token','{} {}','trailing']]){parsers++;rejected(name,()=>parseIntegerJSON(raw),expected);}
const roundtrip=Buffer.from(canonicalIntegerJSON(x)+'\n');r.need(roundtrip.equals(r.read(R+'runtime_control.bin')),'ORIGINAL_CONTROL_UNCHANGED_AFTER_MUTATIONS');
process.stdout.write(JSON.stringify({status:'PASS_IN_MEMORY_NEGATIVE_DATA_CONTROLS',controls,scientific,parsers,total:findings.length,checks:r.checks,findings,key_count:r.keys.size,total_read_bytes:r.total,keys:[...r.keys.values()],submitted_source_execution:false,new_pilot:false,host_queries:false,originals_modified:false},null,2)+'\n');
