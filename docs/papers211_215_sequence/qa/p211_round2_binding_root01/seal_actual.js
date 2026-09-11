'use strict';
// Root-owned post-return packaging only. No freeze/science/build execution.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics/',QA=ROOT+'docs/papers211_215_sequence/qa/';
const HERE=QA+'p211_round2_binding_root01/',EXEC=QA+'p211_round2_execution01/';
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
const json=p=>JSON.parse(fs.readFileSync(p));
const n=json(EXEC+'ROOT_PRODUCT_NATIVE01.json');
assert.equal(n.polls.at(-1).result.exit_code,0);assert(!n.polls.at(-1).result.session_id);
assert.deepStrictEqual(JSON.parse(n.result.output+n.polls.map(p=>p.result.output).join('')),json(HERE+'entry01/RESULT.json'));
const rootNative=json(HERE+'entry01/ROOT_INVOCATION.NATIVE.json');
assert.equal(rootNative.native_exit_code,0);assert.equal(rootNative.exception,null);
const out=fs.readFileSync(HERE+'entry01/ROOT_INVOCATION.stdout.raw');
assert.deepStrictEqual(pin(out),{bytes:rootNative.stdout.bytes,sha256:rootNative.stdout.sha256});
assert.deepStrictEqual(JSON.parse(out),json(EXEC+'RESULT.json'));
assert.equal(json(EXEC+'RESULT.json').native_commands,160);
const post=json(HERE+'refresh02/postcopy01/RESULT.json'),postNative=json(HERE+'refresh02/POSTCOPY_NATIVE01.json');
assert.equal(post.checks,24347);assert.equal(post.phase,'postcopy');
assert.equal(postNative.polls.at(-1).result.exit_code,0);
assert.deepStrictEqual(JSON.parse(postNative.result.output+postNative.polls.map(p=>p.result.output).join('')),post);
function seal(base){
  assert(!fs.existsSync(base+'SHA256SUMS'));const names=[];
  function walk(pre){for(const e of fs.readdirSync(base+pre,{withFileTypes:true})){const n=pre+e.name,p=base+n;assert(!e.isSymbolicLink()&&fs.realpathSync(p)===p);if(e.isDirectory())walk(n+'/');else{assert(e.isFile());names.push(n);}}}
  walk('');names.sort();let total=0;
  const raw=Buffer.from(names.map(n=>{const b=fs.readFileSync(base+n);total+=b.length;return pin(b).sha256+'  '+n+'\n';}).join(''));
  fs.writeFileSync(base+'SHA256SUMS',raw,{flag:'wx',mode:0o600});
  for(const n of names)assert(raw.toString().includes(pin(fs.readFileSync(base+n)).sha256+'  '+n+'\n'));
  return {path:base,payloads:names.length,files:names.length+1,payload_bytes:total,seal:pin(raw)};
}
const result={status:'ACTUAL_EXECUTION_PACKAGED_PENDING_COMPLETE_ROOT_INDEPENDENT_RECEPTION',execution:seal(EXEC),controller:seal(HERE+'entry01/'),postcopy:seal(HERE+'refresh02/postcopy01/'),enabled:seal(HERE+'enabled01/'),paper_complete:false,science_runs:0};
fs.writeFileSync(HERE+'PACKAGING_RESULT.json',JSON.stringify(result,null,2)+'\n',{flag:'wx',mode:0o600});
console.log(JSON.stringify(result));
