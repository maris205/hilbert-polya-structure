// Root documentary reception only. No candidate/scientific code is imported or run.
'use strict';
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const OUT = 'docs/papers211_215_sequence/scouting/root_reception/residual_bgr_word_laver01';
const SCOUT = 'docs/papers211_215_sequence/scouting/';
const digest = b => crypto.createHash('sha256').update(b).digest('hex');
const abs = p => path.isAbsolute(p) ? p : path.join(ROOT, p);
let checks = 0;
function need(v, why) { checks++; if (!v) throw Error(why); }
const inputs = new Map();
function key(p) {
  const a = abs(p), l = fs.lstatSync(a, {bigint:true}), s = fs.statSync(a, {bigint:true});
  need(l.isFile() && s.isFile(), 'regular documentary file '+p);
  const f = t => Object.fromEntries(['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs','birthtimeNs'].map(k=>[k,t[k].toString()]));
  const b = fs.readFileSync(a); need(BigInt(b.length)===s.size, 'read length '+p);
  return {path:p, resolved:fs.realpathSync(a), bytes:b.length, sha256:digest(b),lstat:f(l),stat:f(s)};
}
function read(p) { const k=key(p); if(inputs.has(p)) need(JSON.stringify(k)===JSON.stringify(inputs.get(p)), 'stable reread '+p); else inputs.set(p,k); return fs.readFileSync(abs(p)); }
function list(p) { return read(p).toString('utf8').trimEnd().split('\n').map(l=>{const m=/^([0-9a-f]{64})  (.+)$/.exec(l);need(!!m,'strict manifest '+p); return {sha256:m[1],path:m[2]};}); }
const packages=[];
for (const [dir,seal,pins,expectedPayload,expectedPins] of [
 ['functional_surgery_residual_desk01','SHA256SUMS','INPUT_PINS.sha256',7,11],
 ['finite_word_morphism_residual_desk01','PAYLOAD.sha256','INPUTS.sha256',6,12],
 ['fresh_residual_algebra_order01','SHA256SUMS','INPUT_PINS.sha256',7,8]]) {
 const prefix=SCOUT+dir+'/', rows=list(prefix+seal);
 need(rows.length===expectedPayload,'payload count '+dir); need(new Set(rows.map(r=>r.path)).size===rows.length,'unique names');
 for(const r of rows){need(!path.isAbsolute(r.path)&&!r.path.split('/').includes('..')&&r.path!==seal,'nonself payload');need(digest(read(prefix+r.path))===r.sha256,'payload hash '+r.path);}
 const names=fs.readdirSync(abs(prefix)).sort();need(JSON.stringify(names)===JSON.stringify([...rows.map(r=>r.path),seal].sort()),'complete flat package '+dir);
 const old=list(prefix+pins);need(old.length===expectedPins,'historical count '+dir);for(const r of old)need(digest(read(r.path))===r.sha256,'historical hash '+r.path);
 packages.push({dir,seal,files:names.length,payload:rows.length,inputs:old.length,manifest:inputs.get(prefix+seal)});
}
// Receive actual complete source slices preserved in author tool returns.
// Historical central-state navigation is deliberately excluded, not remapped to current bytes.
const records=[];
function sedSlice(p,lo,hi){const text=read(p).toString('utf8'), lines=text.match(/[^\n]*\n|[^\n]+$/g)||[];return lines.slice(lo-1,hi).join('');}
for(const [rel,selected] of [
 ['functional_surgery_residual_desk01/LOCAL_READ_RECORDS.json',[0,1,2,5,6,7,8]],
 ['finite_word_morphism_residual_desk01/LOCAL_READ_RECORDS.json',[1,2,3,4,5]],
 ['fresh_residual_algebra_order01/NATIVE_READS.json',[4,5,7]]]) {
 const j=JSON.parse(read(SCOUT+rel));for(const i of selected){const r=j.records[i], cmd=r.request?.cmd||r.command;need(r.result.exit_code===0,'native success');
 let whole='';const parts=[];for(const part of cmd.split(' && ')){const m=/^sed -n '(\d+),(\d+)p' ([^\s]+)$/.exec(part);need(!!m,'exact source-read grammar');whole+=sedSlice(m[3],+m[1],+m[2]);parts.push({path:m[3],first:+m[1],last:+m[2]});}
 need(Buffer.from(whole).equals(Buffer.from(r.result.output)),'full native source bytes '+rel+' '+i);
 records.push({record_file:SCOUT+rel,index:i,chunk_id:r.result.chunk_id,bytes:Buffer.byteLength(whole),sha256:digest(Buffer.from(whole)),parts});
 }}
// Original eight-pin author documentary check is independently reconstructed, not rerun.
const close=JSON.parse(read(SCOUT+'fresh_residual_algebra_order01/CLOSING_CHECKS.json'));
const eight=list(SCOUT+'fresh_residual_algebra_order01/INPUT_PINS.sha256');
need(close.result.exit_code===0&&close.result.output===eight.map(r=>r.path+': OK\n').join(''),'archived closing output');
need(close.scientific_executions===0&&close.literal_desk_definitions===2&&close.fresh_nominations===0,'author scope');
for(const p of [OUT+'/ROOT_PRIMARY_RETURNS.json',OUT+'/NATIVE_SCHEMA_INSPECTION.json',OUT+'/RECEPTION.md',OUT+'/receive.js'])read(p);
for(const k of inputs.values())need(JSON.stringify(key(k.path))===JSON.stringify(k),'closing complete input key '+k.path);
const result={status:'PASS_ROOT_NEGATIVE_DOCUMENTARY_RECEPTION',checks,packages,native_source_records:records,complete_inputs:[...inputs.values()],closed_literal_delta:3,word_new_literals:0,new_scientific_runs:0,new_reviews:0,manuscript_pass:false,external:'HOLD_EXTERNAL'};
const bytes=Buffer.from(JSON.stringify(result,null,2)+'\n');fs.writeFileSync(abs(OUT+'/RESULT.json'),bytes,{flag:'wx'});process.stdout.write(bytes);
