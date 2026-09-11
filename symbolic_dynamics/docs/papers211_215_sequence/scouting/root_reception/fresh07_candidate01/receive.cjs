'use strict';
// Documentary original reception only. No evaluation/import of either scientific source or update F.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const SC='docs/papers211_215_sequence/scouting/';
const A=SC+'finite_residual_fresh07/', B=SC+'fresh07_gate01/';
const E=SC+'fresh07_source_erratum01/', D=SC+'fresh07_gate_delta01/';
const R=SC+'root_reception/fresh07_candidate01/';
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const keys=new Map();let checks=0,matchedReads=0,matchedBytes=0;
function need(v,m){checks++;if(!v)throw Error(m);}
function eq(a,b,m){need(JSON.stringify(a)===JSON.stringify(b),m);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const stamp=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function read(rel){
  need(typeof rel==='string'&&/^(docs|papers)\//.test(rel)&&path.posix.normalize(rel)===rel&&!rel.includes('..'),'fixed workspace input '+rel);
  const p=ROOT+'/'+rel,s=fs.lstatSync(p,{bigint:true});need(s.isFile()&&!s.isSymbolicLink()&&s.size<=2000000n,'bounded regular '+rel);
  const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b;
  try{const f=fs.fstatSync(fd,{bigint:true});eq(stamp(s),stamp(f),'fd before');b=fs.readFileSync(fd);eq(stamp(f),stamp(fs.fstatSync(fd,{bigint:true})),'fd after');}finally{fs.closeSync(fd);}
  eq(stamp(s),stamp(fs.lstatSync(p,{bigint:true})),'closing path');need(b.length===Number(s.size),'whole byte count');
  const k={path:rel,bytes:b.length,sha256:sha(b),metadata:stamp(s)};
  if(keys.has(rel))eq(k,keys.get(rel),'unchanged complete key '+rel);else keys.set(rel,k);return b;
}
const text=p=>read(p).toString('utf8'), json=p=>JSON.parse(text(p));
function pins(p,prefix,count){const s=text(p);need(s.endsWith('\n'),'pin LF');const rows=s.trimEnd().split('\n');need(rows.length===count,'pin count '+p);const names=new Set();for(const row of rows){const m=/^([0-9a-f]{64})  (.+)$/.exec(row);need(m&&!names.has(m[2]),'pin format/unique');names.add(m[2]);need(sha(read(prefix+m[2]))===m[1],'pin '+m[2]);}return names;}
function seal(b,n,sealName,digest){need(sha(read(b+sealName))===digest,'fixed seal');const names=pins(b+sealName,b,n);eq(fs.readdirSync(ROOT+'/'+b).sort(),[...names,sealName].sort(),'complete nonself membership');}
seal(A,13,'MANIFEST.sha256','499d60b8c427e188c62cf9548907070030ca17e4d3c5b0fbe25dd6a39a735414');
seal(B,15,'MANIFEST.sha256','b0cf5f5a879df4474c177516cf602072f0800f96ae2f6d2eee0f7cd3f81551ac');
seal(E,3,'SHA256SUMS','46a8e5e652afeeec45354795a72b072bc82872fccbfd44e6e05e9972d292ca17');
seal(D,4,'MANIFEST.sha256','62084ca443604d853e8464eedcdb1a6c472899ff38398c9c9bc50b8d857d3067');
pins(A+'INPUTS.sha256','',12);pins(A+'PILOT_PRESERVATION.sha256','',4);pins(B+'AUTHOR_INPUT_PINS.sha256','',14);pins(E+'INPUTS.sha256','',3);pins(D+'INPUTS.sha256','',36);
function tuple(s){need(/^[0-9(), ]+$/.test(s),'integer tuple grammar');return JSON.parse(s.replaceAll('(','[').replaceAll(')',']').replace(/,\s*\]/g,']'));}
const id=a=>a.join(','), sum=a=>a.reduce((s,x)=>s+x,0);
function choose(n,k){let v=1;for(let j=1;j<=k;j++)v=v*(n-k+j)/j;return Math.round(v);}
function ensureState(a,n,m){need(Array.isArray(a)&&a.length===n&&a.every(x=>Number.isSafeInteger(x)&&x>=0)&&sum(a)===m,'full-carrier state');}
function hist(values){const h=new Map();for(const v of values)h.set(v,(h.get(v)||0)+1);return [...h].sort((a,b)=>a[0]-b[0]);}
function graphCheck(rows,n,m){
  need(rows.length===choose(n+m-1,n-1),'complete stars-and-bars census');const map=new Map();
  for(const row of rows){ensureState(row.a,n,m);ensureState(row.b,n,m);ensureState(row.t,n,m);need(Number.isSafeInteger(row.depth)&&row.depth>=0,'depth integer');need(!map.has(id(row.a)),'unique target');map.set(id(row.a),row);}
  const pred=new Map(rows.map(r=>[id(r.a),[]]));for(const r of rows){need(map.has(id(r.b))&&map.has(id(r.t)),'referent exists');pred.get(id(r.b)).push(r.a);}
  for(const r of rows){const next=map.get(id(r.b)),term=map.get(id(r.t));if(id(r.a)===id(r.b)){need(r.depth===0&&id(r.t)===id(r.a),'fixed metadata');}else need(r.depth===next.depth+1&&id(r.t)===id(next.t),'depth/terminal edge metadata');need(id(term.a)===id(term.b)&&term.depth===0,'terminal fixed');const sources=pred.get(id(r.a)).sort((a,b)=>{for(let i=0;i<n;i++)if(a[i]!==b[i])return a[i]-b[i];return 0;});need(r.fibre===sources.length,'archived indegree');if(r.sources)eq(r.sources,sources,'whole archived source set');r.sources=sources;}
  return {map,image:[...pred.values()].filter(x=>x.length).length,height:Math.max(...rows.map(r=>r.depth)),maxFibre:Math.max(...rows.map(r=>r.fibre))};
}
const pa=json(A+'PILOT_NATIVE.json'), pb=json(B+'VERIFICATION_NATIVE.json');
need(pa.command==='python3 -I -S -B '+A+'pilot.py'&&pa.result.chunk_id==='70be95'&&pa.result.exit_code===0,'actual author pilot identity');
need(pb.request.cmd==='python3 -I -S -B '+B+'verify.py'&&pb.result.chunk_id==='1d2ceb'&&pb.result.exit_code===0,'actual independent run identity');
const ra=Buffer.from(pa.result.output,'utf8'), rb=Buffer.from(pb.result.output,'utf8');
need(ra.length===61482&&ra.every(x=>x<128),'whole author ASCII');need(rb.length===29987&&rb.every(x=>x<128),'whole independent ASCII');
need(read(A+'PILOT_ACTUAL.txt').equals(Buffer.concat([ra,Buffer.from('\n')])),'author derivative extra LF disclosed');
need(read(B+'VERIFICATION_ACTUAL.txt').equals(rb),'review exact raw canonical');need(sha(rb)==='6f4a542c63207896d01b41618f0e138beafa01e008bd433ebc86fc3489b3b567','review stdout fixed hash');
const author=new Map();let current=null,authorRows=0;const al=pa.result.output.trimEnd().split('\n');
need(al.shift()==='FIXED_BOX n=3..5 N=0..6; AUTHOR_PILOT; no automatic enlargement','author opening');
need(al.pop()==='AUTHOR_FIXED_BOX_CHECKS_COMPLETED states=756 carriers=21; NO_ADMISSION; HOLD_EXTERNAL','author closing');
for(const line of al){let m;if((m=/^CARRIER (\d+) (\d+) states (\d+) image (\d+) depth_hist (.*?) fibre_hist (.*?) max_fibre_targets (.*)$/.exec(line))){const [n,mass,count,image]=m.slice(1,5).map(Number);const key=n+':'+mass;need(n>=3&&n<=5&&mass<=6&&!author.has(key),'fixed author carrier');current={n,mass,count,image,depthHist:tuple(m[5]),fibreHist:tuple(m[6]),maxTargets:tuple(m[7]),rows:[]};author.set(key,current);}else{m=/^ROW (\([0-9, ]+\)) -> (\([0-9, ]+\)) depth (\d+) terminal (\([0-9, ]+\)) fibre (\d+)$/.exec(line);need(m&&current,'author row grammar');current.rows.push({a:tuple(m[1]),b:tuple(m[2]),depth:+m[3],t:tuple(m[4]),fibre:+m[5]});authorRows++;}}
need(author.size===21&&authorRows===756,'complete author output counts');
for(const c of author.values()){need(c.count===c.rows.length,'author declared rows');const g=graphCheck(c.rows,c.n,c.mass);need(g.image===c.image,'author image');eq(hist(c.rows.map(r=>r.depth)),c.depthHist,'author whole depth histogram');eq(hist(c.rows.map(r=>r.fibre)),c.fibreHist,'author whole fibre histogram');eq(c.rows.filter(r=>r.fibre===g.maxFibre).map(r=>r.a),c.maxTargets,'author all max targets');c.graph=g;}
const reviewer=new Map();let pending=[],reviewRows=0,branch=null;const bl=pb.result.output.trimEnd().split('\n');
need(bl.shift()==='INDEPENDENT_FIXED_BOX n=1..6 N=0..4; one_run; no_author_import','review opening');
need(bl.pop()==='COMPLETE states=461 carriers=30 fixed_targets=205; finite_agreement_only; no_author_pilot_reclassification; HOLD_EXTERNAL','review closing');
for(const line of bl){let m;if(line.startsWith('TARGET ')){const v=JSON.parse(line.slice(7));need(v.length===5&&Array.isArray(v[4]),'review target schema');pending.push({a:v[0],b:v[1],depth:v[2],t:v[3],sources:v[4],fibre:v[4].length});reviewRows++;}else if((m=/^CARRIER (\d+) (\d+) (\d+) height (\d+) image (\d+) max_fibre (\d+)$/.exec(line))){const[n,mass,count,height,image,maxFibre]=m.slice(1).map(Number),key=n+':'+mass;need(n>=1&&n<=6&&mass<=4&&!reviewer.has(key),'fixed review carrier');need(pending.length===count,'review row count');const graph=graphCheck(pending,n,mass);need(graph.height===height&&graph.image===image&&graph.maxFibre===maxFibre,'review carrier summary');reviewer.set(key,{n,mass,rows:pending,graph});pending=[];}else{need(line.startsWith('BRANCH_COUNTS ')&&branch===null,'one branch record');branch=JSON.parse(line.slice(14));}}
need(reviewer.size===30&&reviewRows===461&&pending.length===0,'complete review output');need(Object.values(branch).every(x=>Number.isSafeInteger(x)&&x>0)&&branch.two_free_intervals===18,'reported branch data');
let overlap=0,fixed=0;for(const[key,c]of reviewer){fixed+=c.rows.filter(r=>id(r.a)===id(r.b)).length;if(author.has(key)){const other=author.get(key);for(const r of c.rows){const old=other.graph.map.get(id(r.a));eq([r.a,r.b,r.depth,r.t,r.sources],[old.a,old.b,old.depth,old.t,old.sources],'complete overlap row');overlap++;}}}need(fixed===205&&overlap===231,'cross-output fixed/overlap census');
function exactRead(rec,cmd){const m=/^sed -n '(\d+),(\d+)p' ((?:docs|papers)\/\S+)$/.exec(cmd);need(m,'selected exact original read request');const lines=text(m[3]).match(/[^\n]*\n|[^\n]+$/g)||[];const b=Buffer.from(lines.slice(+m[1]-1,+m[2]).join(''),'utf8');need(rec.result.exit_code===0&&b.equals(Buffer.from(rec.result.output,'utf8')),'selected full original bytes '+rec.result.chunk_id);matchedReads++;matchedBytes+=b.length;}
const ar=json(A+'NATIVE_READS.json');need(ar.record_count===53&&ar.records.length===53&&ar.scientific_process_count===1,'author native census');
const selected=new Set(['matching_control','old_matching_proof','matching_archive_original','planar_original_proof','current_matching_handoff','old_midpoint_adapter','old_midpoint_source','p212_setup_original','p211_setup_original','old_vector_feedback_original','minimum_absorption_original','mna_author_original','old_transport_proof','old_transport_handoff','prepilot_source_read','proof_readback_part1','proof_readback_part2','prepilot_readback','handoff_readback','collision_readback','readscope_readback']);
let selectedAuthor=0;for(const [i,rec]of ar.records.entries()){need(rec.sequence===i+1,'native sequence');if(selected.has(rec.label)){exactRead(rec,rec.command);selectedAuthor++;}if(rec.label==='one_author_pilot'){need(rec.command===pa.command&&rec.native_chunk==='70be95'&&rec.exit_code===0,'sole pilot reference');}}
need(selectedAuthor===21,'all author selected original regions');need(ar.records.some(r=>r.result?.chunk_id==='3ac43b'&&r.result.exit_code===2)&&ar.records.some(r=>r.result?.chunk_id==='07d2a9'&&r.result.exit_code===2),'author failed reads preserved');
const br=json(B+'READS_NATIVE.json');need(br.records.length===21,'21reviewreadrecords');let reconstructed=0;for(const rec of br.records){const cmd=rec.request?.cmd||rec.command_reconstructed_from_executed_tool_input;if(!rec.request){need(rec.original_request_object_retained===false,'explicit reconstructed command scope');reconstructed++;}exactRead(rec,cmd);}
need(reconstructed===9,'nine reconstructed-command descriptions disclosed');
const ad=json(A+'DOCUMENTARY_CHECK_NATIVE.json');need(ad.result.exit_code===0&&ad.result.chunk_id==='13c565','actual author doc check');const adv=JSON.parse(ad.result.output);need(adv.printed_row_count===756&&adv.printed_carrier_count===21&&adv.exact_original_read_regions===21,'author doc result');
const doc=json(B+'DOCUMENTARY_NATIVE.json');need(doc.raw_byte_check.result.exit_code===0&&doc.input_pin_check.result.exit_code===0,'actual review doc exits');const bd=JSON.parse(doc.raw_byte_check.result.output);need(bd.exact_native_output_bytes===29987&&bd.stdout_sha256===sha(rb),'raw review binding');
const ds=json(D+'CHECKS_NATIVE.json');need(ds.input_pin_check.result.exit_code===0&&ds.documentary_check.result.exit_code===0,'actual delta checks');
const di=json(D+'INTAKE_NATIVE.json');need(di.erratum_read_and_checks.length===7&&di.original_gate_final_seal_checks.length===3,'delta intake dimensions');
for(const rec of di.erratum_read_and_checks){const cmd=rec.request.cmd;if(/^sed -n/.test(cmd))exactRead(rec,cmd);}
need(text(B+'REPORT.md').includes('**EXACT_REPAIR_REQUIRED.**')&&text(D+'DELTA_ACCEPTANCE.md').includes('**DELTA_ACCEPTED — GO_NARROW.**'),'original finding and accepted delta');
need(text(A+'SOURCE_AND_COLLISION.md').includes('finite-field kernel/image')&&text(E+'ERRATUM.md').includes('nondecreasing selfmaps of the finite chain'),'mistake and erratum retained');
for(const b of [A,B,E,D])for(const n of fs.readdirSync(ROOT+'/'+b))if(n.endsWith('.json'))JSON.parse(text(b+n));
read(R+'receive.cjs');const initial=[...keys.values()];for(const k of initial)read(k.path);
process.stdout.write(JSON.stringify({status:'PASS_CANDIDATE_ORIGINAL_DOCUMENTARY_RECEPTION',checks,whole_workspace_keys:keys.size,package_payloads:[13,15,3,4],input_pin_counts:[12,4,14,3,36],author_rows:authorRows,author_carriers:author.size,review_rows:reviewRows,review_carriers:reviewer.size,review_fixed_targets:fixed,overlap_rows:overlap,author_raw_bytes:ra.length,review_raw_bytes:rb.length,selected_original_reads:matchedReads,selected_original_read_bytes:matchedBytes,reconstructed_command_descriptions:reconstructed,source_or_update_evaluated:false,scientific_replays:0,host_private_or_build_actions:0,keys:[...keys.values()]},null,2)+'\n');
