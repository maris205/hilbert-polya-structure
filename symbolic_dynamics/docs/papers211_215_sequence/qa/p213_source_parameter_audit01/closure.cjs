'use strict';
// Documentary closure only: saved request/returns and immutable text as data.
const fs = require('fs');
const crypto = require('crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics/';
const OWN = 'docs/papers211_215_sequence/qa/p213_source_parameter_audit01/';
const FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
let checks = 0;
function need(ok, message) { checks++; if (!ok) throw Error(message); }
function same(a,b) { return JSON.stringify(a) === JSON.stringify(b); }
function digest(body) { return crypto.createHash('sha256').update(body).digest('hex'); }
function metadata(st) { return FIELDS.map(k => st[k].toString()); }
function read(rel) {
  need(/^(docs|papers)\/[A-Za-z0-9_.\/-]+$/.test(rel) && !rel.split('/').some(p => !p || p === '.' || p === '..'), 'workspace path');
  const components = rel.split('/');
  for (let i=1; i<components.length; i++) need(fs.lstatSync(ROOT+components.slice(0,i).join('/')).isDirectory(), 'physical parent');
  const path = ROOT+rel;
  const start = fs.lstatSync(path,{bigint:true});
  need(start.isFile() && start.size <= 8n*1024n*1024n, 'bounded regular document');
  const fd = fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let body;
  try {
    need(same(metadata(start),metadata(fs.fstatSync(fd,{bigint:true}))), 'opened document key');
    const parts=[]; let total=0;
    while (true) {
      const buffer=Buffer.alloc(Math.min(65536,8*1024*1024-total+1));
      const got=fs.readSync(fd,buffer,0,buffer.length,null);
      if (!got) break;
      total+=got; need(total<=8*1024*1024,'bounded document stream');
      parts.push(buffer.subarray(0,got));
    }
    body=Buffer.concat(parts);
    need(same(metadata(start),metadata(fs.fstatSync(fd,{bigint:true}))), 'descriptor ending key');
  } finally { fs.closeSync(fd); }
  need(same(metadata(start),metadata(fs.lstatSync(path,{bigint:true}))), 'path ending key');
  need(BigInt(body.length) === start.size, 'whole document bytes');
  return {body,key:{path:rel,bytes:body.length,sha256:digest(body),metadata:metadata(start)}};
}
need(process.argv.length === 2,'no external arguments or modes');
const ownNames=['READS_NATIVE.json','ADDITIONAL_READS_NATIVE.json','INVENTORY_BEFORE_NATIVE.json','INVENTORY_AFTER_NATIVE.json','INPUT_PINS.sha256','inventory.cjs','closure.cjs'];
const own=new Map(ownNames.map(name=>[name,read(OWN+name)]));
const json=name=>JSON.parse(own.get(name).body.toString('utf8'));
const firstNative=json('INVENTORY_BEFORE_NATIVE.json');
const lastNative=json('INVENTORY_AFTER_NATIVE.json');
for (const record of [firstNative,lastNative]) {
  need(record.request.cmd === 'node '+OWN+'inventory.cjs','exact documentary inventory request');
  need(record.result.exit_code === 0 && typeof record.result.output === 'string','actual successful inventory return');
}
const first=JSON.parse(firstNative.result.output), last=JSON.parse(lastNative.result.output);
need(same(first,last),'complete two inventory bodies agree');
need(first.keys.length === 48 && first.checks === 1602,'declared forty-eight full input keys');
const inputs=new Map();
for(const key of first.keys) {
  need(!inputs.has(key.path),'unique pinned input');
  const current=read(key.path);
  need(same(current.key,key),'unchanged final complete input key: '+key.path);
  inputs.set(key.path,current);
}
const pinText=first.keys.map(key=>key.sha256+'  '+key.path).join('\n')+'\n';
need(own.get('INPUT_PINS.sha256').body.equals(Buffer.from(pinText)),'exact whole input pins');
const records=[...json('READS_NATIVE.json').records,...json('ADDITIONAL_READS_NATIVE.json').records];
need(records.length === 50,'fifty actual original and additional reads');
function textFor(path) {
  if(inputs.has(path)) return inputs.get(path).body.toString('utf8');
  if(path === OWN+'inventory.cjs') return own.get('inventory.cjs').body.toString('utf8');
  return null;
}
function expectedPart(command) {
  let match=/^sed -n '([0-9]+),([0-9]+)p' ([A-Za-z0-9_.\/-]+)$/.exec(command);
  let numbered=false;
  if(!match) {
    const nl=/^nl -ba ([A-Za-z0-9_.\/-]+) \| sed -n '([0-9]+),([0-9]+)p'$/.exec(command);
    if(nl) { match=[nl[0],nl[2],nl[3],nl[1]]; numbered=true; }
  }
  let start,end,path;
  if(match) {start=Number(match[1]);end=Number(match[2]);path=match[3];}
  else {
    const nl=/^nl -ba ([A-Za-z0-9_.\/-]+)$/.exec(command);
    if(!nl) return null;
    start=1;end=Number.MAX_SAFE_INTEGER;path=nl[1];numbered=true;
  }
  const text=textFor(path);
  if(text===null) return null;
  need(text.endsWith('\n'),'selected text has final LF');
  const lines=text.slice(0,-1).split('\n');
  return lines.map((line,i)=>numbered?String(i+1).padStart(6,' ')+'\t'+line:line).slice(start-1,end).map(line=>line+'\n').join('');
}
let compared=0,comparedBytes=0,allReadBytes=0;
const comparisons=[];
for(const record of records) {
  const returned=record.result||record.returned;
  need(typeof record.request.cmd === 'string' && returned.exit_code === 0 && typeof returned.output === 'string','actual request and complete successful return');
  allReadBytes+=Buffer.byteLength(returned.output);
  const parts=record.request.cmd.split(' && ').map(expectedPart);
  if(parts.some(part=>part===null)) continue;
  const expected=parts.join('');
  need(returned.output === expected,'exact saved read output: '+record.request.cmd);
  compared++;comparedBytes+=Buffer.byteLength(expected);
  comparisons.push({chunk_id:returned.chunk_id,command:record.request.cmd,bytes:Buffer.byteLength(expected),sha256:digest(Buffer.from(expected))});
}
need(compared>30,'substantial exact read-return coverage');
for(const name of ownNames) need(same(read(OWN+name).key,own.get(name).key),'unchanged own evidence endpoint');
for(const [path,current] of inputs) need(same(read(path).key,current.key),'unchanged final source endpoint');
console.log(JSON.stringify({schema:'p213-independent-source-closure-v1',status:'DOCUMENTARY_PASS_NOT_SCIENCE_OR_RUNTIME',checks,source_executed:false,source_ast_or_syntax_parsed:false,whole_input_keys:48,inventory_passes:2,checks_per_inventory:1602,all_input_keys_equal:true,actual_read_records:records.length,actual_read_output_bytes:allReadBytes,exact_compared_read_records:compared,exact_compared_read_output_bytes:comparedBytes,comparisons}));
