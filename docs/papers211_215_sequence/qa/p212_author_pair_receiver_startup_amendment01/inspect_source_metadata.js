'use strict';
// Only workspace source/document metadata. Never load proposed code or future paths.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert').strict;
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa';
const BASE=QA+'/p212_author_pair_receiver_startup_amendment01';
const OLD=QA+'/p212_author_pair_receiver_preparation01';
const CONTROLLER=QA+'/p212_author_pair_controller_preparation01';
const PAPER=ROOT+'/papers/212-closed-pointer-orbits';
let checks=0;
function eq(x,y){checks++;assert.deepEqual(x,y);}
function need(x){checks++;assert(x);}
function hash(b){return crypto.createHash('sha256').update(b).digest('hex');}
function safe(p){
  need(path.isAbsolute(p)&&path.normalize(p)===p&&p.startsWith(ROOT+'/'));
  for(let q=p;q.startsWith(ROOT);q=path.dirname(q)){need(!fs.lstatSync(q).isSymbolicLink());if(q===ROOT)break;}
  eq(fs.realpathSync(p),p);
}
function read(p){safe(p);need(fs.statSync(p).isFile());return fs.readFileSync(p);}
function pin(p){const b=read(p);return{bytes:b.length,sha256:hash(b),resolved:p,symlink:null};}
const obj=p=>JSON.parse(read(p));
function tree(base){
  safe(base);const files={},directories=[];
  function walk(p){for(const n of fs.readdirSync(p).sort()){
    const q=p+'/'+n,r=path.relative(base,q);need(!fs.lstatSync(q).isSymbolicLink());
    if(fs.statSync(q).isDirectory()){directories.push(r);walk(q);}else files[r]=pin(q);
  }}walk(base);return{files,directories:directories.sort()};
}
function sealed(base,count,seal){
  const t=tree(base),b=read(base+'/SHA256SUMS');eq(hash(b),seal);need(b.toString().endsWith('\n'));
  const names=[];for(const line of b.toString().slice(0,-1).split('\n')){
    const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.]+)$/.exec(line);need(m&&!names.includes(m[2])&&m[2]!=='SHA256SUMS');
    names.push(m[2]);eq(t.files[m[2]].sha256,m[1]);
  }eq(names.length,count);eq(Object.keys(t.files).sort(),names.concat(['SHA256SUMS']).sort());eq(t.directories,[]);return t;
}
const oldTree=sealed(OLD,14,'79b80be29725ec0a6a429da40de552dd63b39ace4348f4036da87d7b0c299ba8');
const controllerTree=sealed(CONTROLLER,13,'5287daf8dfad0ccbd9b5e3f9708cbd43b0fda72ca0a09aad6f5c758d1a9dfd95');
eq(oldTree.files['inspect_production.py'].bytes,30176);eq(oldTree.files['inspect_production.py'].sha256,'29b445892d42c9952d361298a11cffdb666701a549ebe7db79446d9c925a4e87');
eq(oldTree.files['supplement.js'].bytes,11248);eq(oldTree.files['supplement.js'].sha256,'e59b458e6dca8fb719d93c69148b25eb274b1b5ec431049a8971e8b3ac9bd514');
eq(controllerTree.files['run.py'].bytes,6263);eq(controllerTree.files['run.py'].sha256,'2c6f2a7378a7c5411b262376415e1a77bbdc35523eb7821e44b01a787da93fd0');
const accepted=obj(OLD+'/PREPARATION_RESULT.json');
const inventory=accepted.historical_inventory;eq(pin(inventory.path),{bytes:inventory.bytes,sha256:inventory.sha256,resolved:inventory.resolved,symlink:inventory.symlink});
const prior=obj(inventory.path),canonical=pin(PAPER+'/CANONICAL.json');
eq(canonical,{bytes:12501943,sha256:'1a32be6bb36dd8b4b27b9891a42876fe235bf2555a3dd9f4e36195a6ad72676c',resolved:PAPER+'/CANONICAL.json',symlink:null});
let preservedFiles=0,preservedBytes=0;
for(const[base,expected]of Object.entries(prior.trees)){
  const current=tree(base);if(base===PAPER){eq(current.files['CANONICAL.json'],canonical);delete current.files['CANONICAL.json'];}
  eq(current,expected);preservedFiles+=Object.keys(expected.files).length;preservedBytes+=Object.values(expected.files).reduce((n,p)=>n+p.bytes,0);
}
for(const[p,k]of Object.entries(prior.files)){eq(pin(p),k);preservedFiles++;preservedBytes+=k.bytes;}
eq(preservedFiles,416);eq(preservedBytes,20149659);eq(Object.keys(prior.trees).length,11);
// Archived host metadata remains byte data; never dereference its embedded paths.
for(const[p,k]of Object.entries(accepted.saved_host_metadata_as_documents))eq(pin(p),k);
for(const[base,expected]of Object.entries(accepted.sealed_original_trees))eq(tree(base),expected);
const originals=obj(BASE+'/ORIGINAL_READS_NATIVE.json');eq(originals.length,6);
const originalPins={};for(const r of originals){const p=ROOT+'/'+r.path;eq(r.result.exit_code,0);eq(Buffer.from(r.result.output),read(p));originalPins[p]=pin(p);}
const deltas=obj(BASE+'/LITERAL_DELTAS.json');eq(deltas.ordered_replacements.length,3);eq(deltas.controller_changed,false);eq(deltas.supplement_changed,false);eq(deltas.operational_execution_authorized,false);
eq(deltas.source,'docs/papers211_215_sequence/qa/p212_author_pair_receiver_preparation01/inspect_production.py');eq(deltas.target,'inspect_production.py');
eq(deltas.source_pin,{bytes:30176,sha256:'29b445892d42c9952d361298a11cffdb666701a549ebe7db79446d9c925a4e87'});
let amended=read(ROOT+'/'+deltas.source).toString();
for(const d of deltas.ordered_replacements){eq(amended.split(d.before).length-1,1);amended=amended.replace(d.before,d.after);}
eq(Buffer.from(amended),read(BASE+'/inspect_production.py'));
const diff=obj(BASE+'/SOURCE_DIFF_NATIVE.json');eq(diff.result.exit_code,1);eq(diff.result.output,read(BASE+'/SOURCE_DIFF.patch').toString());
const disabled=obj(BASE+'/EXECUTION.disabled.json');eq(disabled.approved,false);eq(disabled.authority,null);eq(disabled.independent_review,false);
for(const k of ['future_binding_pin','future_product_capture_pin','future_receiver_result','future_receiver_inputs','runtime_authority'])eq(disabled[k],null);
eq(disabled.future_deployment.pin,null);eq(disabled.root_selected_startup_delta.actual_preproduction_absence_record,null);eq(disabled.root_selected_startup_delta.actual_postproduction_absence_record,null);
eq(disabled.root_selected_startup_delta.arguments,['-X','pycache_prefix='+QA+'/p212_author_pair_binding01/never_created_root_capture_cache']);
eq(disabled.root_selected_startup_delta.startup_contract,QA+'/p212_author_pair_binding01/ROOT_STARTUP_CONTRACT.md');
for(const k of ['operational_source_executions','host_runtime_probes','future_pair_outputs_read','mathematical_reevaluations'])eq(disabled[k],0);
const prepared={};for(const n of ['inspect_production.py','LITERAL_DELTAS.json','ORIGINAL_READS_NATIVE.json','SOURCE_DIFF.patch','SOURCE_DIFF_NATIVE.json','PLAN.md','EXECUTION.disabled.json','inspect_source_metadata.js'])prepared[n]=pin(BASE+'/'+n);
const result={status:'SOURCE_ONLY_ROOT_STARTUP_RECEIVER_AMENDMENT_METADATA_VALID',checks,prior_receiver_tree:oldTree,unchanged_controller_tree:controllerTree,historical_inventory:inventory,preserved_historical_files:preservedFiles,preserved_historical_bytes:preservedBytes,historical_trees:11,current_canonical_document:{path:PAPER+'/CANONICAL.json',...canonical},original_source_and_document_pins:originalPins,prepared_files:prepared,literal_python_replacements:3,controller_changed:false,supplement_changed:false,future_paths_inspected:0,operational_sources_executed:0,host_paths_dereferenced:0,mathematical_reevaluations:0,authority_created:false,independent_review:false};
process.stdout.write(JSON.stringify(result,null,2)+'\n');
