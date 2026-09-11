'use strict';
const fs=require('node:fs'),crypto=require('node:crypto'),a=require('node:assert/strict');
const p='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_lifecycle_scientific_key_root01';
let checks=0;function eq(x,y){checks++;a.deepStrictEqual(x,y);}
function key(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function rich(q){const b=fs.readFileSync(q),s=fs.lstatSync(q);a.ok(fs.statSync(q).isFile());return {...key(b),resolved:fs.realpathSync(q),symlink:s.isSymbolicLink()?fs.readlinkSync(q):null};}
const run=JSON.parse(fs.readFileSync(p+'/RUN_RESULT.json')),native=JSON.parse(fs.readFileSync(p+'/NATIVE.json'));
const tool=JSON.parse(fs.readFileSync(p+'/RUN_NATIVE.json'));
eq(tool.result.exit_code,0);eq(JSON.parse(tool.result.output).status,run.status);
eq(JSON.parse(tool.result.output).result,key(fs.readFileSync(p+'/RUN_RESULT.json')));
eq(key(fs.readFileSync(p+'/stdout.json')),native.stdout);eq(native.stdout,run.actual_stdout);
eq(key(fs.readFileSync(p+'/stderr.bin')),native.stderr);eq(native.stderr.bytes,0);
eq(native.native_exit_code,0);eq(native.invocations,1);eq(native.signal,null);eq(native.error,null);
eq(rich(native.argv[0]),native.executable);eq(rich(native.argv[4]),native.source);
eq(rich(p+'/receive_and_run.js'),native.root_source);eq(rich(p+'/AUTHORITY.md'),native.authority);
const source=JSON.parse(fs.readFileSync(p+'/SOURCE_RESULT.json'));
for(let pass=0;pass<2;pass++)for(const set of [source.READ_INPUTS,run.READ_INPUTS])for(const [q,k] of Object.entries(set))eq(rich(q),k);
const result={status:'PASS_ROOT_ORIGINAL_CLOSURE',checks,source_inputs:Object.keys(source.READ_INPUTS).length,run_inputs:Object.keys(run.READ_INPUTS).length,complete_raw_bytes:native.stdout.bytes,new_science:0,new_builds:0,new_views:0};
fs.writeFileSync(p+'/CLOSING_RESULT.json',JSON.stringify(result,null,2)+'\n',{flag:'wx'});
const names=fs.readdirSync(p).sort();a.ok(!names.includes('SHA256SUMS'));
const seal=Buffer.from(names.map(n=>{a.ok(fs.lstatSync(p+'/'+n).isFile());return key(fs.readFileSync(p+'/'+n)).sha256+'  '+n+'\n';}).join(''));
fs.writeFileSync(p+'/SHA256SUMS',seal,{flag:'wx'});
console.log(JSON.stringify({...result,payloads:names.length,seal:key(seal)}));
