#!/usr/bin/env node
'use strict';
/*
 * Documentary read-only scope preparation. No input copy, science/import,
 * Git object/index/ref write, remote request, or execution of submitted code.
 * Only fresh outputs beneath this owned preparation directory are created.
 * This is NOT a checkpoint executor or an operational/runtime acceptance.
 */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const cp = require('child_process');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const OWN = ROOT + '/docs/papers211_215_sequence/qa/private_checkpoint03_scope_preparation01';
const BATCH = 'docs/papers211_215_sequence', QA = BATCH + '/qa', SC = BATCH + '/scouting', RR = SC + '/root_reception';
const BARE = '/root/symbolic-dynamics-private-sync-accepted-20260907.git';
const MIRROR = '/root/autodl-tmp/hilbert-polya-structure';
const BASE = '7d43cb323adf7d27326263b8ce4158d4eefff43a';
const TREE = '64feab3a9eff397179a6670aff5b1ff7d0595796';
const MIRROR_BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10';
const controls = ['SYMBOLIC_DYNAMICS_STATE.md', BATCH + '/PIPELINE_STATE.md'];
const paper = 'papers/211-kernel-image-projection-feedback';
const qnames = `p211_a_binding_closure p211_a_final_root p211_a_initial_binding
p211_a_pair_binding p211_a_report_root p211_a_root_reception
p211_author_binding_closure p211_author_execution_documentation01
p211_author_execution_documentation_root p211_author_initial_binding
p211_author_pair_binding p211_author_source_reception p211_b_binding_closure
p211_b_final_root p211_b_initial_binding p211_b_pair_binding p211_b_report_root
p211_b_root_reception p211_build_independent_audit p211_build_independent_delta01
p211_build_preparation p211_build_revision01 p211_build_root_reception
p211_font_warning_root01 p211_font_warning_source_desk01 p211_initial_build_01
p211_initial_build_adoption01 p211_initial_build_binding01
p211_initial_build_independent_reception p211_initial_build_root_reception
p211_lifecycle_input_desk01 p211_lifecycle_integration_desk01 p211_lifecycle_root01
p211_lifecycle_scientific_key_desk01 p211_lifecycle_scientific_key_root01
p211_round0_execution01 p211_round0_independent_reception p211_round0_preparation
p211_round0_root_reception p211_round1_adapter01 p211_round1_adapter02
p211_round1_binding_root p211_round1_execution01 p211_round1_independent_reception01
p211_round1_plan_audit p211_round1_preparation p211_round1_reception_preparation01
p211_round1_reception_preparation02 p211_round1_root_reception
p211_round2_binding_preparation01 p211_round2_binding_root p211_round2_binding_root01
p211_round2_binding_source_audit01 p211_round2_execution01
p211_round2_original_capture_preparation01 p211_round2_original_receiver_preparation01
p211_round2_original_root01 p211_round2_physical_independent01 p211_round2_preparation01
p211_round2_root_reception01 p211_round2_source_audit01 p211_round2_source_root_reception01
p211_runtime_independent_audit p211_runtime_preparation p211_runtime_root_reception
p211_terminal_binding_independent01 p211_terminal_binding_preparation01
p211_terminal_binding_root01 p211_terminal_binding_source_root01
p211_terminal_cold2_source_root01 p211_terminal_cold_artifact_audit01
p211_terminal_cold_artifact_audit02 p211_terminal_cold_artifact_audit02_preparation
p211_terminal_cold_artifact_root01 p211_terminal_cold_artifact_root02
p211_terminal_diagnostic_disposition01 p211_terminal_enable_preparation01
p211_terminal_enable_root01 p211_terminal_entry_independent_audit01
p211_terminal_entry_independent_root01 p211_terminal_pair_pages_root01`.split(/\s+/);
const admission = `finite_semigroup_lane finite_semigroup_pilot kip_source_desk
kip_candidate_gate kip_candidate_gate_source_addendum finite_rewriting_residual_lane`.split(/\s+/);
const scouts = `common_sum_gcd_lane cluster_completion_lane queue_transfer_lane
coupled_integer_lane partition_surgery_lane parallel_run_erasure_lane
finite_lattice_arithmetic_lane planar_matching_lane
finite_compression_recoding_fresh_desk bounded_lattice_profile_fresh_desk
finite_feedback_residual_design_desk finite_ordered_interaction_fresh_desk
finite_algebraic_normal_form_fresh_desk finite_path_local_memory_desk
finite_graph_memory_fresh_desk finite_permutation_gap_desk01
finite_nonlinear_residual_desk01 finite_graph_rewiring_desk01
finite_resource_rewriting_desk02`.split(/\s+/);
const receiptFiles = `inspect_gcd_cluster.py GCD_CLUSTER_NATIVE.json GCD_CLUSTER_RECEPTION.md
inspect_queue.py QUEUE_COUPLED_NATIVE.json QUEUE_COUPLED_RECEPTION.md
inspect_partition.py PARTITION_NATIVE.json inspect_run_erasure.py RUN_ERASURE_NATIVE.json
PARTITION_RUN_ERASURE_RECEPTION.md inspect_lattice_planar.py LATTICE_PLANAR_NATIVE.json
LATTICE_PLANAR_RECEPTION.md inspect_kip_originals.py KIP_ORIGINALS_NATIVE.json
inspect_kip_gate.py KIP_GATE_NATIVE.json inspect_kip_addendum_rewriting.py
KIP_ADDENDUM_REWRITING_NATIVE.json KIP_ADMISSION_RECEPTION.md check_admission_links.py
ADMISSION_LINKS_NATIVE.json check_admission_links02.py ADMISSION_LINKS_NATIVE02.json
check_admission_links03.py ADMISSION_LINKS_NATIVE03.json
check_admission_links04.py ADMISSION_LINKS_NATIVE04.json
COMPRESSION_GRID_SCRF_RECEPTION.md ORDERED_ALGEBRA_MEMORY_RECEPTION.md`.split(/\s+/);
const qfiles = `P211_AUTHOR_RUNTIME_RECEPTION.md P211_A_RUNTIME_RECEPTION.md
P211_A_FINAL_ROOT_SEAL_NATIVE01.json P211_ROUND1_SEAL_NATIVE.json
P211_ROUND1_INDEX_REFRESH_NATIVE.json P211_B_RUNTIME_RECEPTION.md
P211_B_INDEX_NATIVE01.json`.split(/\s+/);
const controlDirs = `control_author_runtime_accepted01 control_before_a_runtime
control_before_a_final control_before_round1_accepted control_before_b_runtime
control_before_b_final_accepted control_before_four_desk_accepted
control_before_p211_round2_original_accepted01 control_before_build_source_received01
control_before_p211_first_cold_recorded01 control_before_p211_terminal_pair_recorded01
control_before_p211_terminal_artifacts_accepted01 control_before_p211_completed01`.split(/\s+/);
const groups = [];
function add(category, relative) { groups.push({category, relative}); }
controls.forEach(n => add('current_controls_proposed_capture', n));
[paper].forEach(n => add('p211_complete_paper', n));
['PROBLEM_ANCHOR.md','P211_REVIEW_CONTRACT.md','P211_A_RESPONSE.md','P211_B_RESPONSE.md'].forEach(n => add('p211_contracts', BATCH+'/'+n));
qnames.forEach(n => add('p211_original_qa_and_preserved_failures', QA+'/'+n));
qfiles.forEach(n => add('p211_original_runtime_receipts', QA+'/'+n));
['p211_a','p211_b'].forEach(n => add('p211_actual_reviews', BATCH+'/reviews/'+n));
['author','a','b'].forEach(r => ['initial','pair'].forEach(s => add('p211_actual_scientific_execution', QA+'/root_replays/p211_'+r+'_'+s+'_01')));
admission.forEach(n => add('p211_admission_originals_and_pilot_failure', SC+'/'+n));
scouts.forEach(n => add('accepted_35_to_43_with_joint_zero_literal_desks', SC+'/'+n));
receiptFiles.forEach(n => add('accepted_admission_and_35_to_43_root_receipts', RR+'/'+n));
['control_kip_admission','compression_reception','compression_grid_scrf','ordered_algebra_memory'].forEach(n => add('accepted_admission_and_35_to_43_root_originals', RR+'/'+n));
['four_desk_documentary_audit01','four_desk_root_reception01'].forEach(n => add('accepted_42_43_complete_originals', QA+'/'+n));
controlDirs.forEach(n => add('original_temporal_control_mappings', QA+'/'+n));
const EXCLUDED = [
  BATCH+'/qa/private_checkpoint03_scope_preparation01',
  BATCH+'/qa/p211_a_private_checkpoint_preparation',
  BATCH+'/qa/private_checkpoint_preparation02', BATCH+'/qa/root_checkpoint_inspection02',
  'papers/212-closed-pointer-reversal', 'all p212_* query/build/runtime/adoption/source packages',
  'pointer residual/pilot/admission packages except historical strings in selected records',
  'zero-literal desks outside the jointly accepted 35-43/admission packets',
  'unreceived/current scouting and all later additions',
  'outside-workspace host binaries, environment originals, settings, caches and runtime archives'
];
function need(x,msg){ if(!x) throw Error(msg); }
function digest(b,a='sha256'){ return crypto.createHash(a).update(b).digest('hex'); }
function readKey(p){
  const a=fs.lstatSync(p,{bigint:true}); need(a.isFile()&&!a.isSymbolicLink()&&fs.realpathSync(p)===p,'unsafe regular file '+p);
  const b=fs.readFileSync(p), z=fs.lstatSync(p,{bigint:true});
  for(const k of ['dev','ino','mode','size','mtimeNs','ctimeNs'])need(a[k]===z[k],'raced file '+p);
  return {bytes:b.length,sha256:digest(b),mode:(a.mode&73n)?'100755':'100644',
    oid:digest(Buffer.concat([Buffer.from('blob '+b.length+'\0'),b]),'sha1')};
}
function members(p){
  const a=fs.lstatSync(p); need(!a.isSymbolicLink()&&fs.realpathSync(p)===p,'aliased scope '+p);
  if(a.isFile())return[p]; need(a.isDirectory(),'unsupported scope '+p);
  return fs.readdirSync(p).sort().flatMap(n=>members(p+'/'+n));
}
function save(n,x){ const b=Buffer.from(JSON.stringify(x,null,2)+'\n'); fs.writeFileSync(OWN+'/'+n,b,{flag:'wx'}); return {bytes:b.length,sha256:digest(b)}; }
function guard(){
  const names = [
    ...['config','HEAD','index','packed-refs','refs/heads/main','objects/info/alternates'].map(n=>MIRROR+'/.git/'+n),
    ...['config','HEAD','index','packed-refs','refs/heads/main','objects/info/alternates'].map(n=>BARE+'/'+n),
    '/usr/bin/git','/usr/bin/ssh',fs.realpathSync('/usr/bin/node')];
  return Object.fromEntries(names.map(p=>[p,fs.existsSync(p)?readKey(p):{present:false}]));
}
const childEnv = {PATH:'/usr/bin:/bin',LANG:'C',LC_ALL:'C',TZ:'UTC',GIT_OPTIONAL_LOCKS:'0',
 GIT_TERMINAL_PROMPT:'0',GIT_CONFIG_NOSYSTEM:'1',GIT_CONFIG_GLOBAL:'/dev/null'};
const gitFlags=['-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false','-c','core.untrackedCache=false',
 '-c','gc.auto=0','-c','maintenance.auto=false','-c','commit.gpgSign=false'];
let serial=0;
function native(args){
  const n='git_'+String(++serial).padStart(2,'0');
  const attempt={argv:['/usr/bin/git',...args],cwd:ROOT,environment:childEnv,stdin_base64:'',
    started_utc:new Date().toISOString(),timeout_ms:50000,max_buffer_bytes:16000000,
    scope:'read-only local metadata; no remote, object/index/ref/config write; not strict runtime evidence'};
  save(n+'_ATTEMPT.json',attempt);
  const r=cp.spawnSync('/usr/bin/git',args,{cwd:ROOT,env:childEnv,input:Buffer.alloc(0),
    encoding:null,timeout:50000,maxBuffer:16000000,killSignal:'SIGKILL'});
  const result={pid:r.pid??null,spawned:!!r.pid,native_exit:r.status,signal:r.signal,
    error:r.error?String(r.error):null,stdout_base64:r.stdout? r.stdout.toString('base64'):null,
    stderr_base64:r.stderr? r.stderr.toString('base64'):null,ended_utc:new Date().toISOString()};
  save(n+'_RESULT.json',result); need(r.status===0&&!r.error,'native failure '+n); return r.stdout;
}
const git=(...args)=>native(['--git-dir='+BARE,...gitFlags,...args]);
const mirror=(...args)=>native(['-C',MIRROR,...gitFlags,...args]);
function parseTree(b){
  need(b.length===0||b[b.length-1]===0,'truncated tree');
  const out={}; for(const s of b.toString().split('\0').slice(0,-1)){
    const m=s.match(/^(\d+) blob ([0-9a-f]{40})\t(.+)$/);need(m,'tree framing');
    need(!out[m[3]],'duplicate tree path');out[m[3]]={mode:m[1],oid:m[2]};
  } return out;
}
function manifest(p, expected){
  const b=fs.readFileSync(p), lines=b.toString().trimEnd().split('\n'), rows=[];
  for(const line of lines){const m=line.match(/^([0-9a-f]{64})  (.+)$/);need(m,'manifest row '+p);
    const file=path.resolve(path.dirname(p),m[2]);need(file.startsWith(path.dirname(p)+'/'),'manifest escape');
    need(readKey(file).sha256===m[1],'manifest bytes '+file); rows.push(file);}
  const all=members(path.dirname(p)).filter(x=>x!==p);need(rows.length===new Set(rows).size,'duplicate manifest');
  need(JSON.stringify([...rows].sort())===JSON.stringify(all.sort()),'nonself whole manifest '+p);
  if(expected)need(digest(b)===expected.sha256&&rows.length===expected.payloads,'accepted seal mismatch '+p);
  return {path:p,sha256:digest(b),payloads:rows.length};
}
try{
  const protectedBefore=guard(), sourceKey=readKey(__filename), start=new Date().toISOString();
  const roles={
    bare:git('rev-parse','--is-bare-repository').toString().trim(),
    head:git('symbolic-ref','HEAD').toString().trim(),
    main:git('rev-parse','refs/heads/main').toString().trim(),
    tree:git('rev-parse',BASE+'^{tree}').toString().trim(),
    parents:git('rev-list','--parents','-n','1',BASE).toString().trim(),
    format:git('rev-parse','--show-object-format').toString().trim(),
    configured_remotes:git('remote').toString(),
    mirror_head:mirror('rev-parse','HEAD').toString().trim(),
    mirror_status_raw_base64:mirror('status','--porcelain=v1','-z','--untracked-files=all').toString('base64'),
    mirror_origin:mirror('remote','get-url','origin').toString().trim(),
    identity:git('show','-s','--format=%an%x00%ae%x00%cn%x00%ce',BASE).toString(),
    remote_not_requeried:true,bare_worktree_status:'N/A'
  };
  need(roles.bare==='true'&&roles.head==='refs/heads/main'&&roles.main===BASE&&roles.tree===TREE&&
    roles.format==='sha1'&&roles.configured_remotes===''&&roles.mirror_head===MIRROR_BASE&&
    roles.mirror_status_raw_base64===''&&roles.mirror_origin==='git@github.com:maris205/hilbert-polya-structure.git',
    'role mismatch');
  const inventory={}, summaries=[];
  for(const g of groups){
    const paths=members(ROOT+'/'+g.relative); let bytes=0;
    for(const absolute of paths){
      const n=path.relative(ROOT,absolute);need(!inventory[n],'overlapping selected scope '+n);
      const v=readKey(absolute);bytes+=v.bytes;
      inventory[n]={source_path:absolute,git_path:n,category:g.category,...v};
    }
    summaries.push({...g,files:paths.length,bytes});
  }
  const baseline=parseTree(git('ls-tree','-r','-z','--full-tree',BASE,'--',...groups.map(g=>g.relative)));
  for(const n of Object.keys(baseline))need(inventory[n],'baseline selected deletion '+n);
  const delta=Object.values(inventory).map(r=>({git_path:r.git_path,old:baseline[r.git_path]??null,
    status:!baseline[r.git_path]?'A':baseline[r.git_path].oid===r.oid&&baseline[r.git_path].mode===r.mode?'=':'M'}));
  const lifecycle=JSON.parse(fs.readFileSync(ROOT+'/'+QA+'/p211_lifecycle_root01/LIFECYCLE_RESULT.json'));
  const verified=[];
  for(const [p,v]of Object.entries(lifecycle.SEALS))verified.push(manifest(p,v));
  for(const p of [QA+'/p211_lifecycle_root01/SHA256SUMS',QA+'/p211_lifecycle_integration_desk01/SHA256SUMS'])verified.push(manifest(ROOT+'/'+p));
  const links=lifecycle.LINKS.map(r=>({...r,currently_exists:fs.existsSync(r.resolved),
    selected:fs.existsSync(r.resolved)&&(fs.statSync(r.resolved).isDirectory()?
      members(r.resolved).every(p=>inventory[path.relative(ROOT,p)]):!!inventory[path.relative(ROOT,r.resolved)])}));
  need(links.every(r=>r.currently_exists&&r.selected),'unselected current lifecycle target');
  const ledger=JSON.parse(fs.readFileSync(ROOT+'/'+QA+'/p211_lifecycle_root01/LIFECYCLE_INPUTS.json'));
  const lf=ledger.files; const dependencies=[];
  for(const [original,old]of Object.entries(lf)){
    const relative=original.startsWith(ROOT+'/')?path.relative(ROOT,original):null;
    const match=relative&&inventory[relative];
    dependencies.push({original,relative,selected:!!match,
      classification:match?'selected current bytes':relative?'workspace-local semantic dependency; not automatically selected':'host-local semantic dependency; never copied',
      recorded_sha256:old.sha256??null,current_selected_sha256:match?.sha256??null,
      same_recorded_hash:match&&old.sha256?match.sha256===old.sha256:null});
  }
  for(const r of Object.values(inventory))need(JSON.stringify(readKey(r.source_path))===JSON.stringify(
    {bytes:r.bytes,sha256:r.sha256,mode:r.mode,oid:r.oid}),'selected changed on closing read '+r.git_path);
  for(const g of summaries)need(members(ROOT+'/'+g.relative).length===g.files,'membership changed '+g.relative);
  need(JSON.stringify(protectedBefore)===JSON.stringify(guard()),'protected role changed');
  const counts={files:Object.keys(inventory).length,bytes:Object.values(inventory).reduce((a,r)=>a+r.bytes,0),
    additions:delta.filter(r=>r.status==='A').length,modifications:delta.filter(r=>r.status==='M').length,
    unchanged:delta.filter(r=>r.status==='=').length,deletions:0};
  const categories={};for(const g of summaries){const c=categories[g.category]??={files:0,bytes:0};c.files+=g.files;c.bytes+=g.bytes;}
  const pins=save('CANDIDATE_INVENTORY.json',{status:'PROPOSED_EXACT_SCOPE_NOT_AUTHORIZED_OR_CAPTURED',start_utc:start,
    completed_utc:new Date().toISOString(),source_key:sourceKey,base:BASE,base_tree:TREE,
    control_policy:'Only these observed hashes are proposed. No copy/freeze occurred. Capture must bind exact approved immutable controls; any source drift stops and requires a new plan.',
    counts,categories,groups:summaries,excluded:EXCLUDED,inventory,delta_preview:delta});
  save('ACCEPTED_SEAL_AND_LINK_CHECKS.json',{verified_seals:verified,lifecycle_links:links});
  save('LIFECYCLE_DEPENDENCY_BOUNDARY.json',{source:QA+'/p211_lifecycle_root01/LIFECYCLE_INPUTS.json',
    scope:'Exact direct ledger only, not recursive total semantic closure. Historical hash mismatches require existing mappings; no retrospective equality claimed.',
    counts:{total:dependencies.length,selected:dependencies.filter(r=>r.selected).length,local_only:dependencies.filter(r=>!r.selected).length},
    dependencies});
  save('READONLY_ROLE_RESULT.json',{status:'PASS_LOCAL_READONLY_ROLE_AND_SCOPE_PREPARATION',roles,protected_before:protectedBefore,
    protected_after:guard(),source_key:sourceKey,inventory_key:pins,commands:serial,counts,categories,
    git_mutations:0,remote_queries:0,input_copies:0,new_science:0,new_builds:0,new_views:0,
    limits:'No strict runtime trace; source-only plan, not capture approval, operational execution, scientific PASS or private synchronization.'});
  console.log(JSON.stringify({status:'PASS_LOCAL_READONLY_SCOPE_PREPARATION',counts,categories,inventory:pins,commands:serial}));
}catch(e){
  save('FAILURE.json',{status:'FAILED_PREPARATION_NOT_SUCCESS',error:String(e),stack:e.stack,
    partial_outputs_retained:true,retry_or_cleanup:false});
  throw e;
}

