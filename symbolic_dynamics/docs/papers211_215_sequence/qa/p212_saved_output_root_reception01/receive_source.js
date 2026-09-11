'use strict';
// Root documentary source reception only; no submitted JavaScript/Python execution.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',Q=ROOT+'/docs/papers211_215_sequence/qa/';
const PREP=Q+'p212_saved_output_semantic_preparation01',OWN=Q+'p212_saved_output_root_reception01';
let checks=0;const inputs={};
function need(v,s){checks++;a.ok(v,s);}
function same(x,y,s){checks++;a.deepStrictEqual(x,y,s);}
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p,k){
  need(path.normalize(p)===p&&p.startsWith(ROOT+'/'),'explicit workspace-only byte input');
  const l=fs.lstatSync(p);need(l.isFile()&&!l.isSymbolicLink()&&fs.realpathSync(p)===p,'physical source original');
  const b=fs.readFileSync(p),v={...pin(b),resolved:p,symlink:null};
  if(inputs[p])same(v,inputs[p],'full stable reread');if(k)for(const f of Object.keys(k))same(v[f],k[f],'supplied pin '+f);inputs[p]=v;return b;
}
const obj=p=>JSON.parse(read(p));
function manifest(file,base){
  const data=read(file).toString();need(data.endsWith('\n'),'complete manifest LF');const names=[];
  for(const line of data.trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(m&&!m[2].startsWith('/')&&!m[2].split('/').some(x=>['','.','..'].includes(x))&&!names.includes(m[2]),'exact safe unique manifest row');names.push(m[2]);read(base+'/'+m[2],{sha256:m[1]});}return names;
}
const names=manifest(PREP+'/MANIFEST.sha256',PREP);same(names.length,5,'complete five-payload preparation');
same(fs.readdirSync(PREP).sort(),[...names,'MANIFEST.sha256'].sort(),'whole six-file preparation');
same(manifest(PREP+'/INPUT_PINS.sha256',ROOT).length,8,'all eight original provenance inputs');
const all=[...obj(PREP+'/NATIVE_READS.json').records,...obj(PREP+'/PREPARATION_CHECKS.json').records];same(all.length,20,'all actual 15+5 preparation native calls');
let sourceSlices=0;
for(const row of all){
  need(row.request&&row.result&&Number.isInteger(row.result.exit_code)&&!row.result.session_id,'real completed native envelope');
  need(typeof row.result.output==='string'&&!row.result.output.includes('tokens truncated')&&!row.result.output.startsWith('Warning: truncated output'),'complete saved native output');
  const m=/^sed -n '(\d+),(\d+)p' ([^\s]+)$/.exec(row.request.cmd);
  if(m){
    const data=read(ROOT+'/'+m[3]).toString(),lines=data.match(/[^\n]*\n|[^\n]+$/g)||[];
    same(row.result.exit_code,0,'source read completed');need(Buffer.from(row.result.output).equals(Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(''))),'complete actual source-read stdout bytes');sourceSlices++;
  }else if(row.result.exit_code!==0){
    same(row.result.exit_code,2,'single expected bounded missing-directory discovery');
    same(row.request.cmd,'rg --files docs/papers211_215_sequence/qa/p212_saved_output_semantic_preparation01','missing future source directory scope');
    need(row.result.output.includes('No such file or directory'),'actual missing-path diagnostic retained');
  }
}
same(sourceSlices,12,'all twelve exact sed slices including closing source tail');
const js=read(PREP+'/receive_saved_output.js').toString(),py=read(ROOT+'/papers/212-closed-pointer-orbits/verify.py').toString();
const jnames=[...js.match(/const NAMES = \[([\s\S]*?)\];\s*const EXCLUDED/)[1].matchAll(/'([a-z_]+)'/g)].map(m=>m[1]);
const pnames=[...py.match(/PREDICATES = \(([\s\S]*?)\)\s*EXCLUDED_CLAIMS/)[1].matchAll(/"([a-z_]+)"/g)].map(m=>m[1]);
same(jnames,pnames,'whole ordered 46-name declaration');same(jnames.length,46,'all predicate names');
same([...new Set([...js.matchAll(/ledger\.check\('([a-z_]+)'/g)].map(m=>m[1]))].sort(),pnames.slice().sort(),'all forty-six literal comparison call names');
same([...js.matchAll(/require\('([^']+)'\)/g)].map(m=>m[1]),['node:fs','node:crypto','node:path'],'closed three builtin imports');
read(OWN+'/receive_source.js');
for(const p of Object.keys(inputs))read(p,inputs[p]);
fs.writeFileSync(OWN+'/SOURCE_INPUTS.json',JSON.stringify(inputs,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({status:'PASS_ROOT_COMPLETE_P212_SEMANTIC_SOURCE_PREPARATION_PENDING_BOUND_APPLICATION',checks,input_paths:Object.keys(inputs).length,preparation_payloads:5,provenance_pins:8,native_calls:20,exact_source_slices:sourceSlices,receiver:inputs[PREP+'/receive_saved_output.js'],scientific_executions:0,submitted_source_executions:0,scope:'Root full textual/source/native reception of an author-side untested saved-output receiver, not an independent mathematical review.'}));
