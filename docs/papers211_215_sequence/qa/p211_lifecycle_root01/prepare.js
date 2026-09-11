'use strict';
const fs=require('node:fs'),c=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const PAPER=ROOT+'/papers/211-kernel-image-projection-feedback';
const HERE=ROOT+'/docs/papers211_215_sequence/qa/p211_lifecycle_root01';
const CONTROL=ROOT+'/docs/papers211_215_sequence/qa/control_before_p211_completed01';
const fields=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];
function key(b){return {bytes:b.length,sha256:c.createHash('sha256').update(b).digest('hex')};}
function rich(p){const b=fs.readFileSync(p),s=fs.statSync(p,{bigint:true}),l=fs.lstatSync(p,{bigint:true});a.ok(s.isFile());return {...key(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null,stat:fields.map(f=>s[f].toString()),lstat:fields.map(f=>l[f].toString())};}
function walk(p){return fs.readdirSync(p).sort().flatMap(n=>{const q=p+'/'+n,s=fs.lstatSync(q);a.ok(!s.isSymbolicLink());return s.isDirectory()?walk(q):[q];});}
function save(p,x){fs.writeFileSync(p,JSON.stringify(x,null,2)+'\n',{flag:'wx'});return key(fs.readFileSync(p));}
a.equal(process.cwd(),ROOT);a.equal(process.argv.length,2);
const paths=walk(PAPER);a.equal(paths.length,999);
a.ok(!fs.existsSync(PAPER+'/SHA256SUMS'));a.ok(!fs.existsSync(PAPER+'/FINAL_QA_REPORT.md'));
const baseline=Object.fromEntries(paths.map(p=>[p,rich(p)]));
a.equal(baseline[PAPER+'/README.md'].sha256,'b8090a4271f453fd7f45f835d7a80319e202a62fd2e61e6f3a63e4908f1bea27');
const readme=HERE+'/README.before.md';a.ok(!fs.existsSync(readme));
fs.copyFileSync(PAPER+'/README.md',readme,fs.constants.COPYFILE_EXCL);
a.ok(fs.readFileSync(PAPER+'/README.md').equals(fs.readFileSync(readme)));
a.ok(!fs.existsSync(CONTROL));fs.mkdirSync(CONTROL);
const mappings=[];
for(const [src,dst] of [[PAPER+'/README.md',readme],[ROOT+'/docs/papers211_215_sequence/PIPELINE_STATE.md',CONTROL+'/PIPELINE_STATE.before.md'],[ROOT+'/SYMBOLIC_DYNAMICS_STATE.md',CONTROL+'/SYMBOLIC_DYNAMICS_STATE.before.md']]){
 const old=rich(src);if(dst!==readme)fs.copyFileSync(src,dst,fs.constants.COPYFILE_EXCL);
 const copied=rich(dst);a.ok(fs.readFileSync(src).equals(fs.readFileSync(dst)));a.deepEqual(rich(src),old);
 mappings.push({original:src,original_full_key:old,physical_copy:dst,copy_full_key:copied,actual_whole_raw_bytes_equal:true});
}
for(const [p,k] of Object.entries(baseline))a.deepEqual(rich(p),k);
const baselineKey=save(HERE+'/PAPER_BEFORE.json',{stat_fields:fields,files:baseline});
const mappingKey=save(HERE+'/MAPPING.json',{status:'ACTUAL_PHYSICAL_PRE_LIFECYCLE_COPIES_RAW_COMPARED',mappings});
save(CONTROL+'/MAPPING.json',{status:'ACTUAL_PHYSICAL_PRE_COMPLETION_CENTRAL_COPIES',parent_mapping:HERE+'/MAPPING.json',parent_mapping_key:mappingKey,mappings:mappings.slice(1)});
const result={status:'PASS_PRE_LIFECYCLE_PHYSICAL_PRESERVATION',paper_files:paths.length,physical_copies:mappings.length,paper_before:baselineKey,mapping:mappingKey,allowed_existing_paper_change:'README.md',allowed_added_paper_paths:['FINAL_QA_REPORT.md','SHA256SUMS'],new_science:0,new_builds:0,new_views:0};
save(HERE+'/PREPARATION_RESULT.json',result);console.log(JSON.stringify(result));
