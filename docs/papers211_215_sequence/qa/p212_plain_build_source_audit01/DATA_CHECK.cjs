'use strict';
// Independent, read-only workspace DATA checks. Never import or execute a proposal.
const fs = require('node:fs');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const Q = 'docs/papers211_215_sequence/qa/';
const P = Q + 'p212_plain_build_source_proposal02/';
const V1 = Q + 'p212_plain_build_source_proposal01/';
const OLD = Q + 'p213_round2_terminal_preparation01/';
const LIVE = 'papers/212-closed-pointer-orbits/';
const names = ['main.tex','math_commands.tex','references.bib','sections/01_setup.tex','sections/02_returns.tex','sections/03_period_set.tex','sections/04_census.tex','sections/05_scope.tex'];
const accepted = ['da04d4ca19ed94ce2fae1d181f238b0e1ae944ca09a714a30c6bb0e11f375d8a','3ebb1fd506f17810d19531cee9333b52617ee5a5f9231df6307936e0a392f938','9ad7c6bebc1aeef3a9d0e3f0703e876f2e1a634c5bf2d7f46297cfa7d5d1cf38','44ca562e26d6e8c6c5d92f33245e0a26f1a2cbbd2d5caf204352437d343cc04b','7185cd89b09569bc2977e71a5a74ea6c65b5a734a18905e8b11a592985be9002','45f2e69dbe9d9f4418a439c407fd77309513fb515b12b38ab64bb421f12df490','4f4e2db96c6f2fd9734f0ed29d1dedc759daef2d87e02d68890deb5f0cf4b353','44ab0ee97ab09a7bd0d68ddaf116d74f43314f69ef00821a77b67282d851012d'];
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const read = p => fs.readFileSync(ROOT + '/' + p);
const ascii = b => { assert(b.every(x => x < 128)); return b.toString('ascii'); };
const exact = (a,b) => assert(Buffer.from(a).equals(Buffer.from(b)));
const replaceOne = (s,a,b) => { assert.equal(s.split(a).length,2); return s.replace(a,b); };
const docs = ['BUILD_REQUEST.proposed.sh.txt','CONTRACT.md','DOCUMENTARY_CHECKS.md','HANDOFF.md','NATIVE_REQUEST.proposed.json','PROPOSED_SOURCE_ONLY.sha256','RECIPE.diff','SOURCE.diff','V1_TO_V2.diff'];
const expectedFiles = [...docs,...names.map(n=>'originals/'+n),...names.map(n=>'proposed/'+n)].sort();
function list(p) {
  return fs.readdirSync(ROOT+'/'+P+p,{withFileTypes:true}).flatMap(e=>{
    assert(e.isDirectory() || e.isFile(), 'Unexpected proposal entry type');
    return e.isDirectory() ? list(p+e.name+'/') : [p+e.name];
  }).sort();
}
assert.deepEqual(list(''),[...expectedFiles,'SHA256SUMS'].sort());
function manifest(raw,allowed) {
  const s=ascii(raw); assert(s.endsWith('\n'));
  const rows=s.slice(0,-1).split('\n').map(l=>{
    const m=/^([0-9a-f]{64})  ([A-Za-z0-9_./-]+)$/.exec(l); assert(m);
    assert(allowed.includes(m[2])); return {sha256:m[1],path:m[2]};
  });
  assert.equal(new Set(rows.map(r=>r.path)).size,rows.length);
  assert.deepEqual(rows.map(r=>r.path).sort(),[...allowed].sort()); return rows;
}
const seal=read(P+'SHA256SUMS');
const sealRows=manifest(seal,expectedFiles);
const proposalPins=sealRows.map(r=>{
  const b=read(P+r.path); assert.equal(sha(b),r.sha256); return {...r,bytes:b.length};
});
const sourceManifest=read(P+'PROPOSED_SOURCE_ONLY.sha256');
const sourceRows=manifest(sourceManifest,names);
assert.deepEqual(sourceRows.map(r=>r.path),names);
const originals={}, proposed={}, v1={};
const sourceChecks=names.map((n,i)=>{
  const o=read(P+'originals/'+n), p=read(P+'proposed/'+n), l=read(LIVE+n);
  const previous=read(V1+'proposed/'+n), previousOriginal=read(V1+'originals/'+n);
  assert.equal(sha(o),accepted[i]); exact(l,o); exact(previousOriginal,o);
  assert.equal(sha(p),sourceRows[i].sha256);
  originals[n]=ascii(o); proposed[n]=ascii(p); v1[n]=ascii(previous);
  if(!['main.tex','sections/02_returns.tex'].includes(n)) exact(o,p);
  if(n!=='sections/02_returns.tex') exact(previous,p);
  return {path:n,original_bytes:o.length,original_sha256:sha(o),proposed_bytes:p.length,proposed_sha256:sha(p),original_equals_current_live:true,original_equals_v1_original:true,changed:!o.equals(p)};
});
const oldPrefix='\\documentclass[10pt]{article}\n\\usepackage[margin=0.85in]{geometry}\n\\usepackage{amsmath,amssymb,amsthm,booktabs,array}\n\\usepackage[T1]{fontenc}\n\\usepackage[hidelinks]{hyperref}\n';
const newPrefix='\\documentclass[11pt]{article}\n\\usepackage{amsmath,amssymb,amsthm}\n\\setlength{\\textwidth}{6.25in}\n\\setlength{\\oddsidemargin}{0.125in}\n\\setlength{\\evensidemargin}{0.125in}\n\\setlength{\\textheight}{8.8in}\n\\setlength{\\topmargin}{-0.3in}\n';
assert(originals['main.tex'].startsWith(oldPrefix+'\\input{math_commands}\n'));
exact(replaceOne(originals['main.tex'],oldPrefix,newPrefix),proposed['main.tex']);
const p213Main=ascii(read('papers/213-receiver-limited-cyclic-transfer/frozen_round2/main.tex'));
assert(p213Main.startsWith(newPrefix));
let table=originals['sections/02_returns.tex'];
for(const [a,b] of [['\\centering\\small\n','\\centering\n'],['\\begin{tabular}{@{}p{0.45\\linewidth}ll@{}}','\\begin{tabular}{@{}p{0.42\\linewidth}p{0.25\\linewidth}p{0.25\\linewidth}@{}}'],['\\toprule','\\hline'],['\\midrule','\\hline'],['\\bottomrule','\\hline']]) table=replaceOne(table,a,b);
exact(table,proposed['sections/02_returns.tex']);
exact(replaceOne(v1['sections/02_returns.tex'],'\\centering\\small\n','\\centering\n'),proposed['sections/02_returns.tex']);
const inputNames=[...proposed['main.tex'].matchAll(/\\input\{([^}]+)\}/g)].map(m=>m[1]+'.tex');
assert.deepEqual(['main.tex','references.bib',...inputNames].sort(),[...names].sort());
const citations=[...names.filter(n=>n.endsWith('.tex')).map(n=>proposed[n]).join('\n').matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(',')).sort();
const bibKeys=[...proposed['references.bib'].matchAll(/^@[A-Za-z]+\{([^,]+),/gm)].map(m=>m[1]).sort();
assert.deepEqual(citations,['berdine2006','holroyd2008','loginov2007','manna1987','pham2015']);
assert.deepEqual(citations,bibKeys);
assert(!/\\(?:toprule|midrule|bottomrule|geometry|hypersetup|href|url|small)\b/.test(names.filter(n=>n.endsWith('.tex')).map(n=>proposed[n]).join('\n')));
// Check every unified-diff context/deletion/addition against whole input bytes.
// Header timestamps remain documentary text; they are not normalized-byte claims.
function checkDiff(raw,pairs) {
  const s=ascii(raw); assert(s.endsWith('\n'));
  const blocks=s.replace(/^diff -ru [^\n]*\n/gm,'').split(/(?=^--- )/m).filter(Boolean);
  assert.equal(blocks.length,pairs.length);
  return blocks.map((block,i)=>{
    const [oldPath,newPath,oldText,newText]=pairs[i];
    const lines=block.slice(0,-1).split('\n');
    assert(lines[0].startsWith('--- '+oldPath+'\t'));
    assert(lines[1].startsWith('+++ '+newPath+'\t'));
    const o=oldText.slice(0,-1).split('\n'), n=newText.slice(0,-1).split('\n');
    assert(oldText.endsWith('\n') && newText.endsWith('\n'));
    let oc=0,nc=0,j=2,hunks=0;
    while(j<lines.length){
      const m=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?:.*)$/.exec(lines[j++]); assert(m);
      const os=Number(m[1])-1,ns=Number(m[3])-1,olen=Number(m[2]??1),nlen=Number(m[4]??1);
      assert(os>=oc && ns>=nc); assert.deepEqual(o.slice(oc,os),n.slice(nc,ns)); oc=os; nc=ns;
      while(j<lines.length && !lines[j].startsWith('@@ ')){
        const row=lines[j++], tag=row[0], body=row.slice(1); assert([' ','-','+'].includes(tag));
        if(tag!=='+' ) assert.equal(o[oc++],body);
        if(tag!=='-' ) assert.equal(n[nc++],body);
      }
      assert.equal(oc-os,olen); assert.equal(nc-ns,nlen); hunks++;
    }
    assert.deepEqual(o.slice(oc),n.slice(nc)); return {old_path:oldPath,new_path:newPath,hunks,whole_pair_consistent:true};
  });
}
const sourceDiff=checkDiff(read(P+'SOURCE.diff'),['main.tex','sections/02_returns.tex'].map(n=>[P+'originals/'+n,P+'proposed/'+n,originals[n],proposed[n]]));
const v1Diff=checkDiff(read(P+'V1_TO_V2.diff'),[[V1+'proposed/sections/02_returns.tex',P+'proposed/sections/02_returns.tex',v1['sections/02_returns.tex'],proposed['sections/02_returns.tex']]]);
const oldRecipe=ascii(read(OLD+'BUILD_REQUEST.terminal01.sh'));
const recipe=ascii(read(P+'BUILD_REQUEST.proposed.sh.txt'));
let adapted=oldRecipe.replaceAll('P213','P212').replaceAll('p213','p212');
for(const [a,b] of [
 ["P212_PREP='"+ROOT+'/'+Q+"p212_round2_terminal_preparation01'","P212_PREP='"+ROOT+'/'+P.slice(0,-1)+"'"],
 ["P212_SRC='"+ROOT+"/papers/213-receiver-limited-cyclic-transfer/frozen_round2'","P212_SRC='"+ROOT+'/'+LIVE.slice(0,-1)+"'"],
 ["P212_BIND='"+ROOT+'/'+Q+"p212_round2_terminal_preparation01'","P212_BIND='"+ROOT+'/'+Q+"p212_plain_build_binding01'"],
 ["P212_OUT='"+ROOT+"/papers/213-receiver-limited-cyclic-transfer/qa_final/cold_build_1'","P212_OUT='"+ROOT+'/'+LIVE+"qa_initial/plain_build01'"],
 ['P212_SOURCES=(main.tex math_commands.tex references.bib\n  sections/00_abstract.tex sections/01_introduction.tex\n  sections/02_temporal.tex sections/03_inverse.tex\n  sections/04_fibres.tex sections/05_verification.tex)','P212_SOURCES=('+names.join(' ')+')'],
 ['BUILD_REQUEST.terminal01.sh','BUILD_REQUEST.proposed.sh.txt'],
 ['NATIVE_REQUESTS.terminal01.proposed.json','NATIVE_REQUEST.proposed.json']
]) adapted=replaceOne(adapted,a,b);
exact(adapted,recipe);
exact(ascii(read(V1+'BUILD_REQUEST.proposed.sh.txt')).replaceAll('p212_plain_build_source_proposal01','p212_plain_build_source_proposal02'),recipe);
const recipeDiff=checkDiff(read(P+'RECIPE.diff'),[[OLD+'BUILD_REQUEST.terminal01.sh',P+'BUILD_REQUEST.proposed.sh.txt',oldRecipe,recipe]]);
const requestText=ascii(read(P+'NATIVE_REQUEST.proposed.json'));
exact(ascii(read(V1+'NATIVE_REQUEST.proposed.json')).replaceAll('p212_plain_build_source_proposal01','p212_plain_build_source_proposal02'),requestText);
const request=JSON.parse(requestText);
assert.equal(request.operation_authorized,false);
for(const k of ['root_grant','actual_native_request','actual_native_result','actual_session_id']) assert.equal(request[k],null);
assert.equal(request.runtime_manifest.entries,null); assert.equal(request.runtime_manifest.sha256,null);
assert.equal(request.runtime_manifest.path,Q+'p212_plain_build_binding01/RUNTIME_INPUTS.sha256');
assert.deepEqual(request.source_list,names); assert.equal(request.source_root,ROOT+'/'+LIVE.slice(0,-1));
assert.equal(request.source_hash_manifest,P+'PROPOSED_SOURCE_ONLY.sha256');
assert.equal(request.proposed_output_directory,ROOT+'/'+LIVE+'qa_initial/plain_build01');
const env={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',SOURCE_DATE_EPOCH:'1789084800',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p',MKTEXFMT:'0',MKTEXPK:'0',MKTEXTFM:'0',MKTEXMF:'0',MKTEXTEX:'0'};
assert.deepEqual(request.environment,env);
const command='/usr/bin/env -i '+Object.entries(env).map(([k,v])=>k+'='+v).join(' ')+' /bin/bash --noprofile --norc '+ROOT+'/'+P+'BUILD_REQUEST.proposed.sh.txt --execute-under-separate-root-grant';
assert.deepEqual(request.proposed_native_request,{tool:'exec_command',arguments:{cmd:command,workdir:ROOT,shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:16000}});
assert.deepEqual(request.proposed_continuation.arguments,{session_id:null,chars:'',yield_time_ms:10000,max_output_tokens:16000});
assert.equal(request.proposed_continuation.tool,'write_stdin'); assert.equal(request.hold_external,true);
assert.equal(request.future_output_queried,false);
const outcome={scope:'SOURCE/POLICY documentary DATA only; no proposal execution, host-resource reception or build acceptance',proposal:P,proposal_files:26,proposal_payloads:25,seal_sha256:sha(seal),proposal_pins:proposalPins,source_manifest_sha256:sha(sourceManifest),source_checks:sourceChecks,original_bytes:sourceChecks.reduce((s,r)=>s+r.original_bytes,0),proposed_bytes:sourceChecks.reduce((s,r)=>s+r.proposed_bytes,0),six_full_unchanged_sources:true,main_exact_preamble_only:true,table_exact_five_replacements_only:true,v1_to_v2_only_explicit_small_removed:true,source_diff:sourceDiff,v1_diff:v1Diff,recipe_diff:recipeDiff,recipe_exact_p213_namespace_paths_and_source_vector_adaptation:true,request_v1_to_v2_only_namespace_change:true,request_eight_sources_and_exact_thirteen_variable_environment:true,five_citations_equal_five_bibliography_keys:bibKeys,runtime_manifest_unreceived:true,operation_authorized:false,all_checks_passed:true};
process.stdout.write(JSON.stringify(outcome,null,2)+'\n');
