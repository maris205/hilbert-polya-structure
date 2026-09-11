'use strict';
// Independent documentary audit only. Never imports/evaluates submitted sources,
// reads ambient environment, dereferences host inputs, or writes any file.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = 'docs/papers211_215_sequence/qa/';
const PREP = QA+'p211_round2_binding_preparation01/';
const SELF = QA+'p211_round2_binding_source_audit01/';
const PAPER = 'papers/211-kernel-image-projection-feedback/';
const pins = {}, rich = {}, categories = {}, coverage = {};
let checks = 0;
function need(v,label) { checks++; if (!v) throw Error(label); }
function same(a,b,label) { checks++; assert.deepStrictEqual(a,b,label); }
function pin(b) { return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')}; }
function relative(s) {
  need(typeof s==='string' && s.length && !s.includes('\\') && !/[\x00\r\n\t]/.test(s),'literal name');
  if (s.startsWith(ROOT+'/')) s=s.slice(ROOT.length+1);
  need(!path.posix.isAbsolute(s) && path.posix.normalize(s)===s && s.split('/').every(x=>x && x!=='.' && x!=='..'),'workspace-only normalized input '+s);
  return s;
}
function state(s) { return {dev:s.dev,ino:s.ino,size:s.size,mode:s.mode,nlink:s.nlink,mtimeNs:s.mtimeNs,ctimeNs:s.ctimeNs}; }
function read(s, category='metadata') {
  s=relative(s); const p=ROOT+'/'+s;
  const a=fs.lstatSync(p,{bigint:true});
  need(a.isFile()&&!a.isSymbolicLink()&&fs.realpathSync(p)===p,'physical plain file '+s);
  const b=fs.readFileSync(p),z=fs.lstatSync(p,{bigint:true});
  same(state(a),state(z),'stable whole read '+s);
  const k=pin(b);
  if(pins[s]) { same(pins[s],k,'unchanged bytes '+s); same(rich[s],state(z),'unchanged metadata '+s); }
  pins[s]=k; rich[s]=state(z);
  (categories[category] ||= new Set()).add(s);
  return b;
}
function obj(s) { return JSON.parse(read(s)); }
function bytePin(v) { need(v && Number.isSafeInteger(v.bytes)&&v.bytes>=0&&/^[a-f0-9]{64}$/.test(v.sha256),'original byte-pin schema');return {bytes:v.bytes,sha256:v.sha256}; }
function checkPin(s,v,category='original opaque bytes') { same(pin(read(s,category)),bytePin(v),'original byte equality '+s); }
function reference(v) { same(Object.keys(v).sort(),['path','pin'],'reference exact fields');checkPin(v.path,v.pin,'evidence references'); }
function sums(raw) {
  const str=raw.toString('utf8'); need(str.endsWith('\n'),'complete SHA line ending');
  const out={};
  for(const line of str.slice(0,-1).split('\n')) {
    const m=/^([a-f0-9]{64})  (.+)$/.exec(line);
    need(m&&!Object.hasOwn(out,m[2]),'unique exact SHA rows');
    out[m[2]]=m[1];
  }
  return out;
}
function namesEqual(a,b,label) {same([...a].sort(),[...b].sort(),label);}
function physicalTree(root,files,empties=[]) {
  root=relative(root); const foundFiles=[],foundDirs=['.'];
  function walk(dir) {
    const p=ROOT+'/'+root+(dir?'/'+dir:'');
    need(fs.lstatSync(p).isDirectory() && fs.realpathSync(p)===p,'physical named directory');
    for(const e of fs.readdirSync(p,{withFileTypes:true})) {
      const n=dir?dir+'/'+e.name:e.name;
      need(!e.isSymbolicLink(),'no tree symlink');
      if(e.isDirectory()){foundDirs.push(n);walk(n);}
      else {need(e.isFile(),'no special selected member');foundFiles.push(n);}
    }
  }
  walk('');
  namesEqual(foundFiles,files,'whole explicit tree '+root);
  const dirs=new Set(['.']);
  for(const f of [...files,...empties]) {
    if(empties.includes(f)) dirs.add(f);
    let p=path.posix.dirname(f);
    while(p!=='.'){dirs.add(p);p=path.posix.dirname(p);}
  }
  namesEqual(foundDirs,dirs,'whole explicit directory membership '+root);
  for(const d of empties) same(fs.readdirSync(ROOT+'/'+root+'/'+d),[],'literal historical empty directory');
  return {root,files:foundFiles.length,directories:foundDirs.length,empty_directories:empties};
}
const seal=sums(read(PREP+'SHA256SUMS','preparation'));
same(pin(read(PREP+'SHA256SUMS')), {bytes:776,sha256:'8c640abe8708bac71416cc062cc94728b34a4b3daa5100030863f456605a67b9'},'final accepted source-prep seal');
same(Object.keys(seal).length,9,'nine source preparation payloads');
coverage.preparation=physicalTree(PREP.slice(0,-1),[...Object.keys(seal),'SHA256SUMS']);
for(const [n,h] of Object.entries(seal))same(pin(read(PREP+relative(n),'preparation')).sha256,h,'whole source prep payload seal');
const plan=obj(PREP+'RESOLUTION_PLAN.json'),md=obj(PREP+'MD_ORIGIN_PLAN.json'),jo=obj(PREP+'JSON_ORIGIN_PLAN.json');
same(plan.status,'SOURCE_ONLY_NOT_EXECUTED','plan status');same(plan.root,ROOT,'literal root');
same(Object.keys(plan.input_references).length,70,'all explicit plan inputs');
for(const[n,v]of Object.entries(plan.input_references))checkPin(n,v);
same(Object.keys(plan.acceptance_role_paths).length,13,'all acceptance roles');
for(const n of Object.values(plan.acceptance_role_paths))need(Object.hasOwn(plan.input_references,n),'role pinned');
const legacy=obj(plan.legacy_binding),inv=obj(plan.intended_inventory);
const priorSelect=obj(QA+'p211_round1_execution01/SOURCE_SELECTION.json');
same(inv.rows.length,123,'full intended payload census');
same(inv.payload_bytes,10518152,'intended byte census');
same(inv.total_file_count_with_future_outer_manifest,124,'one future nonself outer seal');
const selected={},byOriginal={}; const roleCounts={},roleBytes={};
for(const r of inv.rows) {
  need(!Object.hasOwn(selected,r.destination)&&!Object.hasOwn(byOriginal,r.original_document),'unique selected/original roles');
  selected[r.destination]=r;byOriginal[r.original_document]=r.destination;
  checkPin(r.source,r.pin,'selected opaque bytes');
  roleCounts[r.role]=(roleCounts[r.role]||0)+1;roleBytes[r.role]=(roleBytes[r.role]||0)+r.pin.bytes;
  if(r.role==='UNCHANGED_ROUND1_PAYLOAD') {
    same(r.source,PAPER+'frozen_round1/'+r.destination,'literal old source');
    same(r.original_document,priorSelect[r.destination].original_document,'unchanged original location');
    same(r.pin,priorSelect[r.destination].pin,'unchanged R1 selected key');
  } else {same(r.role,'COMPLETE_FINAL_B_PACKAGE','literal B role');same(r.source,r.original_document,'B literal original');}
}
same(roleCounts,{UNCHANGED_ROUND1_PAYLOAD:83,COMPLETE_FINAL_B_PACKAGE:40},'83+40 roles');
same(roleBytes,{UNCHANGED_ROUND1_PAYLOAD:4438548,COMPLETE_FINAL_B_PACKAGE:6079604},'whole byte arithmetic');
coverage.selected={roleCounts,roleBytes,rows:123,bytes:10518152};
const catalog=new Map(),mapReport=[];
for(const spec of plan.key_roles) {
  const rows=obj(spec.path);same(Object.keys(rows).length,spec.entries,'complete original key census');
  let workspace=0,host=0;
  for(const [spelling,entry]of Object.entries(rows)) {
    const value=bytePin(spec.entry_layout==='WRAPPED_EXTERNAL_PIN'?entry.pin:entry);
    const abs=spelling.startsWith('/')?spelling:ROOT+'/'+relative(spelling);
    need(path.posix.normalize(abs)===abs,'original normalized absolute spelling');
    const variants=catalog.get(abs)||[];
    if(!variants.some(v=>v.bytes===value.bytes&&v.sha256===value.sha256))variants.push(value);
    catalog.set(abs,variants);
    if(abs.startsWith(ROOT+'/')) {workspace++;checkPin(abs,value,'whole inherited workspace');}
    else {host++;need(path.posix.isAbsolute(abs),'host original remains absolute');}
  }
  same([workspace,host],[spec.workspace,spec.host],'complete original workspace/host split');
  mapReport.push({role:spec.role,rows:spec.entries,workspace,host,host_dereferenced:0});
}
same(mapReport.map(r=>[r.rows,r.workspace,r.host]),[[2255,2251,4],[2164,2164,0],[1785,984,801]],'three whole immutable maps');
coverage.original_keys=mapReport;
function known(s,digest) {
  const abs=s.startsWith('/')?s:ROOT+'/'+relative(s);
  const v=(catalog.get(abs)||[]).filter(v=>digest===undefined||v.sha256===digest);
  same(v.length,1,'unique accepted original key '+s);return v[0];
}
coverage.sha_lists=[];
for(const spec of plan.sha_lists) {
  const rows=sums(read(selected[spec.document].source));same(Object.keys(rows).length,spec.entries,'entire mixed-base list');
  let host=0;
  for(const[s,h]of Object.entries(rows)) {
    const v=known(s,h);
    if(s.startsWith('/')&&!s.startsWith(ROOT+'/'))host++;else checkPin(s,v,'mixed-list workspace');
  }
  same(host,spec.host_entries,'all list host spellings preserved');same(spec.base,'','original workspace-root base');
  coverage.sha_lists.push({document:spec.document,rows:Object.keys(rows).length,host});
}
namesEqual(plan.sha_lists.map(r=>r.document),Object.keys(selected).filter(n=>n.endsWith('.sha256')),'all six copied SHA lists');
same(coverage.sha_lists.map(r=>[r.rows,r.host]),[[32,0],[33,0],[1774,801],[50,2],[84,0],[515,122]],'literal list census');
same(legacy.external_trees.length,26,'whole inherited26');
coverage.trees=[];
for(const t of legacy.external_trees) {
  reference(t.accepted_scope_reference);
  for(const n of t.files)checkPin(t.root+'/'+n,known(t.root+'/'+n),'inherited explicit tree');
  coverage.trees.push(physicalTree(t.root,t.files,t.empty_directories||[]));
  if(t.manifest) {
    const rows=sums(read(t.root+'/'+t.manifest));
    namesEqual(Object.keys(rows),t.files.filter(n=>n!==t.manifest),'inherited seal all nonself names');
    for(const[n,h]of Object.entries(rows))same(pins[t.root+'/'+n].sha256,h,'inherited tree seal key');
  }
}
const additionalEmpties = {
  [QA+'root_replays/p211_b_initial_01']:['child01/commands'],
  [QA+'root_replays/p211_b_pair_01']:['child01/commands','child02/commands']
};
same(plan.additional_trees.length,7,'seven exact additional scopes');
for(const t of plan.additional_trees) {
  reference(t.accepted_scope_reference);
  checkPin(t.root+'/SHA256SUMS',plan.input_references[t.root+'/SHA256SUMS']);
  const rows=sums(read(t.root+'/SHA256SUMS'));
  need(!Object.hasOwn(rows,'SHA256SUMS'),'nonself selected tree');
  same(Object.keys(rows).length+1,t.expected_files,'whole additional count');
  for(const[n,h]of Object.entries(rows))same(pin(read(t.root+'/'+relative(n),'additional explicit tree')).sha256,h,'additional seal bytes');
  coverage.trees.push(physicalTree(t.root,[...Object.keys(rows),'SHA256SUMS'],additionalEmpties[t.root]||[]));
}
same(new Set(coverage.trees.map(t=>t.root)).size,33,'distinct26+7 trees');
coverage.markdown={old:0,new_b:0,filled_old_null_origins:0,ordered_links:0,links:[]};
for(const[n,s]of Object.entries(md)) {
  same(s.original_document,selected[n].original_document,'MD literal origin');
  reference(s.accepted_origin_reference);
  let links;
  if(legacy.document_origins[n]) {
    const old=legacy.document_origins[n];same(s.local_links,old.local_links,'all original ordered mappings preserved');
    if(old.accepted_origin_reference===null) {
      coverage.markdown.filled_old_null_origins++;
      same(s.accepted_origin_reference.path,QA+'p211_round1_root_reception/RECEPTION.md','old null author origin filled by R1');
    }else same(s.accepted_origin_reference,old.accepted_origin_reference,'old received origin unchanged');
    coverage.markdown.old++;links=s.local_links;
  }else{
    coverage.markdown.new_b++;
    need(n.startsWith('review_b/'),'only B new origin');
    // Read Markdown solely to extract ordered href metadata, never semantic text.
    const body=read(selected[n].source,'MD href metadata only').toString('utf8');
    const hrefs=Array.from(body.matchAll(/!?\[[^\]\n]*\]\(([^)\n]+)\)/g),m=>m[1].trim().replace(/^<|>$/g,''))
      .filter(h=>!(/^[A-Za-z][A-Za-z0-9+.-]*:/.test(h)||h.startsWith('#')));
    same(s.local_hrefs,hrefs,'all actual ordered B hrefs');
    links=hrefs.map(h=>{
      const abs=path.posix.resolve(ROOT,path.posix.dirname(s.original_document),decodeURIComponent(h.split('#')[0]));
      const target=relative(abs);
      return byOriginal[target]?{href:h,kind:'copied',target:byOriginal[target]}:{href:h,kind:'external_file',target};
    });
  }
  for(const l of links) {
    coverage.markdown.ordered_links++;
    if(l.kind==='copied')need(Object.hasOwn(selected,l.target),'exact copied href target');
    else if(l.kind==='external_file')checkPin(l.target,known(l.target),'original MD target');
    else {same(l.kind,'external_directory','bounded link type');for(const child of l.directory_files)checkPin(l.target+'/'+child,known(l.target+'/'+child),'original MD directory');physicalTree(l.target,l.directory_files);}
    if(l.accepted_resolution_reference)reference(l.accepted_resolution_reference);
  }
  coverage.markdown.links.push({document:n,count:links.length});
}
namesEqual(Object.keys(md),Object.keys(selected).filter(n=>n.endsWith('.md')),'all35 MD roles');
same([coverage.markdown.old,coverage.markdown.new_b,coverage.markdown.filled_old_null_origins,coverage.markdown.ordered_links],[24,11,12,140],'exact MD role census');
coverage.json={old:0,new_b:0};
for(const[n,s]of Object.entries(jo)) {
  same(s.original_document,selected[n].original_document,'JSON literal original');
  reference(s.accepted_origin_and_schema_reference);
  if(legacy.json_pin_bases[n]) {
    const copy={...s};delete copy.original_document;
    same(copy,legacy.json_pin_bases[n],'all38 old JSON field interpretations unchanged');coverage.json.old++;
  }else {
    need(n.startsWith('review_b/'),'only B new JSON schema');
    // Parse top-level keys only; scientific/native payload bodies remain uninterpreted.
    namesEqual(s.original_top_level_keys,Object.keys(obj(selected[n].source)),'all actual B top-level keys');
    coverage.json.new_b++;
  }
}
namesEqual(Object.keys(jo),Object.keys(selected).filter(n=>n.endsWith('.json')),'all57 JSON roles');
same(coverage.json,{old:38,new_b:19},'JSON role split');
const runtime=obj(plan.runtime_lock),resolved={};
same(Object.keys(runtime.files).length,122,'all122 original runtime spellings');
for(const[spelling,v]of Object.entries(runtime.files)) {
  const q=bytePin(v);need(path.posix.isAbsolute(v.resolved),'old physical runtime spelling');
  if(resolved[v.resolved])same(resolved[v.resolved],q,'agreeing old aliases');resolved[v.resolved]=q;
  if(v.resolved.startsWith(ROOT+'/'))checkPin(v.resolved,q,'existing workspace adapter metadata');
}
same(Object.keys(resolved).length,114,'old122-to114 exact aliases');
same(Object.keys(resolved).filter(n=>n.startsWith(ROOT+'/')).length,2,'two old workspace adapter sources');
same(Object.keys(runtime.configuration.paths).length,69,'all69 old settings path roles');
same(Object.keys(runtime.configuration.memberships).length,5,'all5 old memberships');
same(Object.keys(runtime.loader_search_directory_states).length,9,'all9 old loader states');
namesEqual(Object.keys(legacy.native_tool_pins),['/usr/bin/cp','/usr/bin/cmp','/usr/bin/sha256sum','/usr/bin/python3.10'],'old tool pins exact names');
for(const v of Object.values(legacy.native_tool_pins))bytePin(v);
coverage.runtime={original_spellings:122,resolved_files:114,host:112,workspace:2,configuration_paths:69,memberships:5,loader_states:9,host_dereferenced:0};
for(const n of plan.historical_mapping_references)checkPin(n,plan.input_references[n],'historical mapping metadata');
const native=obj(PREP+'NATIVE_READS.json'),finalReads=obj(PREP+'FINAL_SOURCE_READS.json');
same(native.records.length,26,'all26 submitted original native records');
same(finalReads.records.length,5,'all5 final full source reads');
const nativeShape=[];
for(const [i,r]of native.records.entries()) {
  need(typeof r.request.cmd==='string'&&typeof r.result.output==='string'&&Number.isInteger(r.result.exit_code)&&!r.result.session_id,'complete native record envelope');
  nativeShape.push({index:i,exit_code:r.result.exit_code,truncated:r.result.output.startsWith('Warning: truncated output'),output_pin:pin(Buffer.from(r.result.output))});
}
same(nativeShape.filter(r=>r.exit_code!==0).map(r=>r.index),[1,17],'preserved absence/missing-jq failures');
same(nativeShape.filter(r=>r.truncated).map(r=>r.index),[3,24],'preserved state/oversized-projection truncations');
for(const r of finalReads.records) {
  same(r.result.exit_code,0,'complete final read');
  need(!r.result.session_id,'no pending final read');
  need(Buffer.from(r.result.output).equals(read(r.path)),'full archived final stdout equals current source bytes');
}
for(const group of [
  {indices:[11,12,13],file:QA+'p211_round2_preparation01/freeze.py'},
  {indices:[14,15],file:QA+'p211_round1_binding_root/assemble_binding02.py'},
  {indices:[16],file:QA+'p211_round1_binding_root/recheck02.py'}
]) need(Buffer.from(group.indices.map(i=>native.records[i].result.output).join('')).equals(read(group.file)),'full old/freeze archived native source bytes');
const census=JSON.parse(native.records[22].result.output);
same(census.distinct_workspace_files_read,2554,'author full raw key census retained');
for(const[n,v]of Object.entries(census.read_inputs))checkPin(n,v,'archived full original workspace key');
same(Object.keys(census.read_inputs).length,2554,'all2554 archive keys consumed');
same(census.host_paths_dereferenced,0,'author census declared no host read');
const projection=JSON.parse(native.records[25].result.output);
same(projection.lists,coverage.sha_lists.map(r=>({...r,missing:[]})),'complete replacement list projection');
for(const[n,v]of Object.entries(projection.inputs))checkPin(n,v,'archived compact projection inputs');
const checkRecord=obj(PREP+'PACKAGE_CHECK_NATIVE.json'),presealRecord=obj(PREP+'PRESEAL_NATIVE.json');
same(checkRecord.result.exit_code,0,'actual package metadata native');
same(presealRecord.result.exit_code,0,'actual preseal native');
const c=JSON.parse(checkRecord.result.output),z=JSON.parse(presealRecord.result.output);
same([c.original_reference_count,c.md_roles,c.json_roles,c.ordered_local_links,c.inherited_tree_count,c.selected_additional_trees],[70,35,57,140,26,7],'archived whole coverage comparison');
same(c.missing,[],'no missing original catalog');same(c.ambiguous,[],'no ambiguous original catalog');
for(const[n,v]of Object.entries(c.inputs))checkPin(n,v,'archived76 package keys');
same(Object.keys(c.inputs).length,76,'archived package input census');
for(const[n,v]of Object.entries(z.payload))checkPin(PREP+n,v,'archived8 preseal payloads');
same([z.payload_count,z.payload_bytes,z.full_native_source_text_bindings,z.complete_prior_workspace_keys_rechecked],[8,1708587,5,2554],'preseal arithmetic and full coverage');
coverage.native={original_records:26,final_source_records:5,closing_metadata_records:2,whole_final_source_byte_bindings:5,old_source_concatenation_bindings:3,whole_archived_workspace_keys:2554,compact_projection_inputs:Object.keys(projection.inputs).length,package_inputs:76,nativeShape};
for(const n of [
  QA+'p211_round2_execution01',QA+'p211_round2_binding_root/disabled_selection01',
  PAPER+'frozen_round2',PAPER+'qa_final'
]) {let absent=false;try{fs.lstatSync(ROOT+'/'+n);}catch(e){if(e.code==='ENOENT')absent=true;else throw e;}need(absent,'future output absent '+n);}
const ownDiff=obj(SELF+'NATIVE_DIFF.json');
same(ownDiff.result.exit_code,1,'fresh diff differences expected');
const diff=ownDiff.result.output.split('\n');
need(diff[0].startsWith('--- '+QA+'p211_round1_binding_root/assemble_binding02.py\t'),'actual original diff header');
need(diff[1].startsWith('+++ '+PREP+'assemble_disabled.py\t'),'actual new diff header');
const oldRaw=read(QA+'p211_round1_binding_root/assemble_binding02.py'),newRaw=read(PREP+'assemble_disabled.py');
const oldLines=oldRaw.toString().split('\n');oldLines.pop();
let pos=0,out=[],hunks=0;
for(let i=2;i<diff.length;) {
  if(!diff[i]){i++;continue;}
  const m=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@/.exec(diff[i]);
  need(m,'exact full unified hunk header');hunks++;
  const start=Number(m[1])-1;
  out.push(...oldLines.slice(pos,start));pos=start;i++;
  let removed=0,added=0;
  while(i<diff.length&&!diff[i].startsWith('@@ ')) {
    const l=diff[i++];if(l==='')continue;
    need([' ','+','-'].includes(l[0]),'ordinary complete unified line');
    if(l[0]!=='+' ){same(l.slice(1),oldLines[pos++],'original diff line exact');removed++;}
    if(l[0]!=='-'){out.push(l.slice(1));added++;}
  }
  same(removed,Number(m[2]||1),'whole old hunk count');same(added,Number(m[4]||1),'whole new hunk count');
}
out.push(...oldLines.slice(pos));
need(Buffer.from(out.join('\n')+'\n').equals(newRaw),'full fresh diff reconstructs exact new source');
coverage.fresh_diff={hunks,old_lines:oldLines.length,new_lines:newRaw.toString().split('\n').length-1,old_pin:pin(oldRaw),new_pin:pin(newRaw),diff_output_pin:pin(Buffer.from(ownDiff.result.output))};
read(SELF+'audit_metadata.js','audit helper source metadata');
for(const n of Object.keys(pins))read(n,'closing unchanged comparison');
const sortedPins=Object.fromEntries(Object.keys(pins).sort().map(n=>[n,pins[n]]));
console.log(JSON.stringify({
  status:'PASS_DOCUMENTARY_SOURCE_COVERAGE_NOT_OPERATIONAL_SOURCE_TEST',
  checks,coverage,input_files:Object.keys(pins).length,
  category_counts:Object.fromEntries(Object.entries(categories).map(([k,v])=>[k,v.size])),
  no_host_dereference:true,no_ambient_environment_capture:true,no_submitted_import_AST_compile_execution:true,
  no_binding_or_authority_output:true,no_science_or_build:true,
  input_pin_map_sha256:pin(Buffer.from(JSON.stringify(sortedPins))).sha256,input_pins:sortedPins
}));

