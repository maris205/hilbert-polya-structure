'use strict';
// Original documentary data only; no observer/probe/source import or evaluation.
const fs=require('fs'),p=require('path'),c=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const Q='docs/papers211_215_sequence/qa/';
const A=Q+'p212_preprobe_bootstrap_preparation01/',B=Q+'p212_preprobe_bootstrap_source_audit01/';
const D=Q+'p212_preprobe_bootstrap_read_order_delta01/',E=Q+'p212_preprobe_bootstrap_read_order_delta_audit01/';
const R=Q+'p212_preprobe_bootstrap_source_root01/';
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
let checks=0,readCount=0,readBytes=0;const keys=new Map();
const need=(v,m)=>{checks++;if(!v)throw Error(m);},eq=(a,b,m)=>need(JSON.stringify(a)===JSON.stringify(b),m);
const hash=b=>c.createHash('sha256').update(b).digest('hex');
const stamp=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function read(rel){need(typeof rel==='string'&&/^(docs|papers|\.agents)\//.test(rel)&&p.posix.normalize(rel)===rel&&!rel.includes('..'),'bounded workspace only '+rel);
 const full=ROOT+rel,s=fs.lstatSync(full,{bigint:true});need(s.isFile()&&!s.isSymbolicLink()&&s.size<=3000000n,'regular finite workspace');
 const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b;
 try{const f=fs.fstatSync(fd,{bigint:true});eq(stamp(f),stamp(s),'pre-read identity');b=fs.readFileSync(fd);eq(stamp(f),stamp(fs.fstatSync(fd,{bigint:true})),'same fd closing');}finally{fs.closeSync(fd);}
 eq(stamp(s),stamp(fs.lstatSync(full,{bigint:true})),'path closing');need(b.length===Number(s.size),'wholebytes');
 const k={path:rel,bytes:b.length,sha256:hash(b),metadata:stamp(s)};if(keys.has(rel))eq(k,keys.get(rel),'unchanged whole key '+rel);else keys.set(rel,k);return b;}
const txt=rel=>read(rel).toString('utf8'),json=rel=>JSON.parse(txt(rel));
function pins(rel,prefix,n){const s=txt(rel);need(s.endsWith('\n'),'pin LF');const rows=s.trimEnd().split('\n');need(rows.length===n,'pin count '+rel);const names=new Set();
 for(const line of rows){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(m,'pin format');const name=([B,E].includes(prefix)&&m[2].startsWith('./'))?m[2].slice(2):m[2];need(!names.has(name),'unique normalized scoped pin');names.add(name);need(hash(read(prefix+name))===m[1],'complete input hash '+m[2]);}return names;}
function seal(b,n,digest){need(hash(read(b+'SHA256SUMS'))===digest,'fixed seal '+b);const names=pins(b+'SHA256SUMS',b,n);eq(fs.readdirSync(ROOT+b).sort(),[...names,'SHA256SUMS'].sort(),'complete nonself membership');}
seal(A,17,'5741ce7f3dd3019b67d084d13dbd7672bd22e9a49ce575e18af96d6bbf8d3e29');
seal(B,9,'7bb9d6e0be690fcd200e2686797bd7de0bc111479656235a06ae9df36550fd18');
seal(D,6,'9e9e371cf1cf4a69ab49c2785cfa9544626b1e9fad234f50eb56e04e8bb4a103');
seal(E,9,'a950d13a6154ddab4a5461bc357fbce6110234854461c11f086782b7fa9e851d');
pins(A+'SOURCE_INPUTS.sha256','',16);pins(B+'SOURCE_INPUTS.sha256','',36);pins(D+'INPUTS.sha256','',7);pins(E+'SOURCE_INPUTS.sha256','',53);
function rawRead(rec){const cmd=rec.command||rec.request?.cmd;let m,body;
 if((m=/^sed -n '(\d+),(\d+)p' '?((?:docs|papers|\.agents)\/[^']+)'?$/.exec(cmd))){const s=txt(m[3]),lines=s.match(/[^\n]*\n|[^\n]+$/g)||[];body=Buffer.from(lines.slice(+m[1]-1,+m[2]).join(''));}
 else if((m=/^cat '?((?:docs|papers)\/[^']+)'?$/.exec(cmd))){body=read(m[1]);}
 else if((m=/^nl -ba ((?:docs|papers)\/\S+) \| sed -n '(\d+),(\d+)p'$/.exec(cmd))){const lines=txt(m[1]).match(/[^\n]*\n|[^\n]+$/g)||[];body=Buffer.from(lines.map((s,i)=>String(i+1).padStart(6)+'\t'+s).slice(+m[2]-1,+m[3]).join(''));}
 else return false;
 need(rec.result.exit_code===0&&body.equals(Buffer.from(rec.result.output)),'complete actual read '+rec.result.chunk_id);readCount++;readBytes+=body.length;return true;}
function hashOutput(rec,n){need(rec.result.exit_code===0,'hash output exit');const ls=rec.result.output.trimEnd().split('\n');need(ls.length===n,'entire hash output count');for(const l of ls){const m=/^([0-9a-f]{64})  (.+)$/.exec(l);need(m&&hash(read(m[2]))===m[1],'actual hash row');}}
const ar=json(A+'PREPARATION_READS_NATIVE.json');need(ar.final_complete_reads.length===15,'author15complete');for(const r of ar.final_complete_reads)need(rawRead(r),'author knownread');
const br=json(B+'READS_NATIVE.json'),er=json(E+'READS_NATIVE.json');need(br.length===34&&er.length===23,'independent34+23commandreturns');
for(const r of [...br,...er,...json(B+'INTEGRITY_NATIVE.json').records,...json(E+'INTEGRITY_NATIVE.json').records])rawRead(r);
hashOutput(br[29],36);hashOutput(br[33],36);need(br[29].result.output===br[33].result.output,'old36beforeafter raw');
hashOutput(er[20],53);hashOutput(er[22],53);need(er[20].result.output===er[22].result.output,'delta53beforeafter raw');
hashOutput(json(A+'DOCUMENTARY_INPUT_KEYS_NATIVE.json').records[0],16);
hashOutput(json(A+'INTEGRITY_NATIVE.json').actual_checks[0],16);
const old=txt(A+'observe.py'),now=txt(D+'observe.py');need(old.split('\n').length-1===425&&now.split('\n').length-1===426,'source lengths');
let transformed=old;const changes=[
 ["def whole_file(path, limit, capture):","def whole_file(path, limit, capture, expected):"],
 ["        digest, chunks, size = sha256(), [], 0","        stable(expected, before)\n        digest, chunks, size = sha256(), [], 0"],
 ["row['content'] = whole_file(before['resolved'], target['max_bytes'], target['capture_hex'])","row['content'] = whole_file(before['resolved'], target['max_bytes'], target['capture_hex'], before['stat'])"]];
for(const[a,b]of changes){need(transformed.split(a).length===2,'unique exact source substitution');transformed=transformed.replace(a,b);}need(transformed===now,'whole exact three edits');
const sr=json(D+'SOURCE_READ_NATIVE.json');need(rawRead(sr),'old source native');need(sr.result.output===old,'old notnewsource');
const da=json(D+'ACTUAL_DIFF_NATIVE.json'),dr=json(R+'ACTUAL_DIFF_NATIVE.json');need(da.result.exit_code===1&&dr.result.exit_code===1&&er[6].result.exit_code===1,'actual three diff exits');
need(dr.result.output===da.result.output&&dr.result.output===er[6].result.output,'entire raw diff equality');need((dr.result.output.match(/^@@/gm)||[]).length===3,'three hunks');
const dc=json(D+'DOCUMENTARY_CHECKS_NATIVE.json');need(dc.first_failed.result.chunk_id==='731dc5'&&dc.first_failed.result.exit_code===1&&dc.corrected.result.chunk_id==='5e23e9'&&dc.corrected.result.exit_code===0,'failedcorrecteddoccommands');
need(dc.corrected.request.cmd===dc.first_failed.request.cmd.replaceAll('MANIFEST.sha256','SHA256SUMS'),'exact docbasename correction');
const derived=JSON.parse(dc.corrected.result.output);need(derived.exact_replacements===3&&derived.inputs.length===7,'corrected actualresult');
for(const k of derived.inputs){const b=read(k.path);need(b.length===k.bytes&&hash(b)===k.sha256,'originalcorrectedinput');}
const third=json(R+'THIRD_DOCUMENTARY_COMMAND_NATIVE.json');need(third.result.chunk_id==='524989'&&third.result.exit_code===0,'third actualdocumentary original');
need(third.result.output===txt(D+'SHA256SUMS'),'third actual output exactly finaldelta seal');
const tc=json(E+'TEXT_COMPARISON.json');need(tc.exact_literal_replacement_count===3&&tc.transformed_old_text_equals_complete_new_text&&tc.author_SOURCE_READ_NATIVE_is_original_source_not_corrected&&tc.reviewer_source_executed===false,'reviewtextcomparison');
const f=json(A+'FRONTIER.json'),g=json(A+'AUTHORIZATION.disabled.json'),pr=json(B+'JSON_PROJECTION.json');
need(JSON.stringify(f,null,2)+'\n'===txt(A+'FRONTIER.json'),'whole ASCIIcanonical JSON');
need(f.targets.length===164&&f.allowed_components.length===204&&f.closure_gaps.length===7,'finite frontiercensus');
eq(f.allowed_components,[...new Set(f.allowed_components)].sort(),'component unique/sort');
eq(f.targets.map(t=>t.path),[...new Set(f.targets.map(t=>t.path))].sort(),'targetunique/sort');
const mode={};let captures=0,names=0;const members=[];
for(const t of f.targets){need(f.allowed_components.includes(t.path)&&p.posix.normalize(t.path)===t.path&&t.path.startsWith('/'),'literal target data');mode[t.mode]=(mode[t.mode]||0)+1;if(t.capture_hex)captures++;
 if(t.mode==='membership'){eq(t.expected_names,[...new Set(t.expected_names)].sort(),'names unique/sort');need(t.expected_names.length<=t.max_members,'member ceiling');names+=t.expected_names.length;members.push({path:t.path,max_members:t.max_members,expected_name_count:t.expected_names.length});}
 else need(t.max_members===0&&t.expected_names===null,'nohiddenmembers');
 if(!['file','optional_file'].includes(t.mode))need(t.max_bytes===0&&t.capture_hex===false,'metadatahasnobytes');}
const sortObj=x=>Object.fromEntries(Object.entries(x).sort());eq(sortObj(mode),sortObj(pr.mode_counts),'complete mode census');
eq(members,pr.membership,'allmemberships');need(names===292&&captures===120,'capture/member census');eq(f.closure_gaps,pr.closure_gaps,'closuregaps retained');
need(g.enabled===false&&f.author_probe_execution_allowed===false,'disabledfrontier');
for(const k of ['source_receipt','trust_receipt','frontier'])need(g[k].pin===null,'disabledpin');
const of=json(B+'FINDINGS.json'),nf=json(E+'FINDINGS.json');need(of.open_source_findings===1&&of.findings[0].status==='OPEN','originalopen preserved');need(nf.current_open_observer_source_findings===0&&nf.findings[0].id==='PSA-F1'&&nf.findings[0].status==='CLOSED'&&nf.runtime_executed===false&&nf.observer_authorization_granted===false,'exact new acceptance notgrant');
for(const base of [A,B,D,E])for(const n of fs.readdirSync(ROOT+base))if(n.endsWith('.json'))JSON.parse(txt(base+n));
const rr=json(R+'ROOT_SELECTED_READS_NATIVE.json');need(rr.records.length===14,'14rootreadreturns');for(const r of rr.records)need(rawRead(r),'rootread');
for(const n of fs.readdirSync(ROOT+R))read(R+n);
const first=[...keys.values()];for(const k of first)read(k.path);
process.stdout.write(JSON.stringify({status:'PASS_P212_PREPROBE_ORIGINAL_SOURCE_RECEPTION',checks,whole_workspace_keys:keys.size,packages:[17,9,6,9],pins:[16,36,7,53],raw_original_reads:readCount,raw_original_read_bytes:readBytes,root_read_count:14,old_source_lines:425,accepted_source_lines:426,exact_diff_hunks:3,exact_diff_bytes:Buffer.byteLength(dr.result.output),frontier_targets:164,allowed_components:204,closure_gaps:7,current_source_open_findings:0,original_source_open_findings:1,documentary_node_preparation_commands:3,observer_probe_science_git_ssh_build_executions:0,keys:[...keys.values()]},null,2)+'\n');


