// Root workspace-only source reception. Explicit metadata reuse, not independent design.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',Q=ROOT+'/docs/papers211_215_sequence/qa/';
const C=Q+'p211_round2_original_capture_preparation01/',P=Q+'p211_round2_original_receiver_preparation01/',HERE=Q+'p211_round2_original_root01/';
const INPUTS={};let checks=0;function need(v,s){checks++;assert.ok(v,s);}function eq(a,b,s){checks++;assert.deepStrictEqual(a,b,s);}
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p){need(p.startsWith(ROOT+'/'),'workspace only');const st=fs.lstatSync(p);need(st.isFile()&&!st.isSymbolicLink()&&fs.realpathSync(p)===p,'ordinary complete source file');const b=fs.readFileSync(p),v=pin(b);if(INPUTS[p])eq(v,INPUTS[p],'stable repeat');INPUTS[p]=v;return b;}
const obj=p=>JSON.parse(read(p));
read(__filename);
const names=['DERIVATION.diff','DERIVATION_NATIVE.json','DISABLED_SPEC.json','ORIGINAL_PINS.json','PREPARATION_NATIVE.json','SHA256SUMS','SOURCE_METADATA.md','capture_originals.py'];
eq(fs.readdirSync(C).sort(),names,'whole exact eight-file preparation');const seal=read(C+'SHA256SUMS');
eq(pin(seal),{bytes:603,sha256:'7d79d68ef8d9444a0e73c192de5d8c37d3385ea5d8bce6ced0e3ffa1640a3ed5'},'root received final seal');
const found=[];for(const line of seal.toString().trimEnd().split('\n')){const m=line.match(/^([0-9a-f]{64})  (.+)$/);need(m&&names.includes(m[2])&&m[2]!=='SHA256SUMS','exact nonself row');eq(pin(read(C+m[2])).sha256,m[1],'every full payload');found.push(m[2]);}
eq(found,names.filter(n=>n!=='SHA256SUMS'),'complete sorted nonself set');
const pins=obj(C+'ORIGINAL_PINS.json');eq(pins.entries,112,'full original pin census');eq(Object.keys(pins.pins).length,112,'full original pins');for(const [p,v]of Object.entries(pins.pins))eq(pin(read(p)),v,'all original byte pins');
const prep=obj(C+'PREPARATION_NATIVE.json'),native=obj(HERE+'SOURCE_METADATA_REUSE_NATIVE.json'),old=prep.records.at(-1);
eq(native.request,old.request,'actual entire accepted metadata command reused');eq(native.result.exit_code,0,'actual root metadata success');eq(native.result.output,old.result.output,'entire actual original/root output bytes');
const result=JSON.parse(native.result.output);eq(result.checks,1363,'actual count');eq(result.source,{lines:339,bytes:19798,sha256:'b1a9c30917d5c8d1a9ca4bf94fbf80dfd5ecbc4436dd8e401cba0f6bf54439ad'},'exact full-source binding');
const dn=obj(C+'DERIVATION_NATIVE.json').record;eq(Buffer.from(dn.result.output),read(C+'DERIVATION.diff'),'whole final actual source diff');eq(dn.result.exit_code,1,'actual diff exit');
let natives=0;for(const r of [...prep.records,dn,native,obj(HERE+'SOURCE_SEAL_NATIVE.json')]){need(typeof r.request.cmd==='string'&&typeof r.result.output==='string'&&Number.isInteger(r.result.exit_code)&&!r.result.session_id&&!r.result.output.startsWith('Warning:'),'whole actual completed native');natives++;}
eq(natives,8,'all selected original and root source envelopes');
const before=INPUTS;for(const [p,v]of Object.entries(before))eq(pin(read(p)),v,'final full source key');
const value={status:'PASS_ROOT_COMPLETE_CAPTURE_SOURCE_RECEPTION',checks,paths:Object.keys(INPUTS).length,preparation_payloads:7,preparation_files:8,original_pins:112,actual_metadata_reuse_checks:1363,entire_metadata_output_identical:true,full_source_read_lines:339,old_receiver_source_read_lines:595,native_envelopes:8,new_science:0,new_builds:0,independent_design:false,operational_attempt:false,external:'OWNER_AMBER / HOLD_EXTERNAL'};
for(const[n,v]of [['SOURCE_INPUTS.json',INPUTS],['SOURCE_RESULT.json',value]])fs.writeFileSync(HERE+n,JSON.stringify(v,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify(value));
