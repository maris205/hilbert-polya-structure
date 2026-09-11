'use strict';
// Documentary receipt only: never import or execute a candidate or reviewer program.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const W = '/root/autodl-tmp/symbolic_dynamics';
const S = 'docs/papers211_215_sequence/scouting/';
const O = S + 'root_reception/matrix_word04/';
let checks = 0;
const keys = new Map(), native = [], groups = [];
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
function need(v, why) { checks++; if (!v) throw Error(why); }
function abs(p) { need(!path.isAbsolute(p) && !p.split('/').includes('..'), 'workspace relative ' + p); return path.join(W,p); }
function get(p) {
  const a = abs(p), s = fs.lstatSync(a,{bigint:true});
  need(s.isFile(), 'regular documentary input ' + p);
  const b = fs.readFileSync(a), t = fs.lstatSync(a,{bigint:true});
  const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs','birthtimeNs'];
  const st = x => Object.fromEntries(fields.map(k=>[k,x[k].toString()]));
  need(JSON.stringify(st(s)) === JSON.stringify(st(t)) && BigInt(b.length) === s.size, 'stable read ' + p);
  const k = {path:p,resolved:fs.realpathSync(a),bytes:b.length,sha256:sha(b),lstat:st(s)};
  if(keys.has(p)) need(JSON.stringify(k) === JSON.stringify(keys.get(p)), 'same complete key ' + p);
  else keys.set(p,k);
  return b;
}
function manifest(p) {
  const s=get(p).toString('utf8'); need(s.endsWith('\n'),'manifest LF '+p);
  const rows=s.trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([^\r\n]+)$/.exec(l);need(!!m,'manifest grammar '+p);return {sha256:m[1],path:m[2]};});
  need(new Set(rows.map(x=>x.path)).size===rows.length,'manifest unique '+p);return rows;
}
for(const [d,n,np] of [['noncommutative_graph_residual03',7,9],['noncommutative_graph_residual03_independent_desk01',9,20],['word_automata_residual04',7,8]]) {
  const p=S+d+'/', rows=manifest(p+'SHA256SUMS');need(rows.length===n,'payload count '+d);
  for(const r of rows){need(!r.path.includes('/')&&r.path!=='SHA256SUMS','flat nonself payload');need(sha(get(p+r.path))===r.sha256,'payload SHA '+p+r.path);}
  need(JSON.stringify(fs.readdirSync(abs(p)).sort())===JSON.stringify([...rows.map(x=>x.path),'SHA256SUMS'].sort()),'whole directory '+d);
  const pins=manifest(p+'INPUT_PINS.sha256');need(pins.length===np,'input pin count '+d);
  for(const r of pins)need(sha(get(r.path))===r.sha256,'input SHA '+r.path);
  groups.push({directory:p,payload:n,files:n+1,input_pins:np,seal_sha256:sha(get(p+'SHA256SUMS'))});
}
// Reconstruct complete original sed returns without executing the archived commands.
// Multiple files in one sed command have cumulative line numbering, as ordinary sed does.
function sed(cmd) {
  let out='';
  for(const part of cmd.split(' && ')) {
    const m=/^sed -n '([0-9,p;]+)' (.+)$/.exec(part);need(!!m,'bounded sed grammar '+cmd);
    const files=m[2].split(' ');need(files.every(x=>/^[.A-Za-z0-9_/-]+$/.test(x)),'plain file operands');
    const lines=files.flatMap(p=>get(p).toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[]);
    const spans=m[1].split(';').map(x=>{const z=/^(\d+),(\d+)p$/.exec(x);need(!!z,'bounded numeric span');return [+z[1],+z[2]];});
    lines.forEach((l,i)=>{for(const [a,b] of spans)if(i+1>=a&&i+1<=b)out+=l;});
  }
  return Buffer.from(out);
}
function record(file, index, r) {
  const cmd=r.args?.cmd??r.request?.cmd??r.cmd;
  need(typeof cmd==='string'&&r.result.exit_code===0,'successful original source read');
  const b=sed(cmd), saved=Buffer.from(r.result.output);need(b.equals(saved),'raw complete source-return '+file+' '+index);
  native.push({file,index,cmd,chunk_id:r.result.chunk_id,exit_code:r.result.exit_code,bytes:b.length,sha256:sha(b)});
}
const css=S+'noncommutative_graph_residual03/READ_RECORDS.json';
JSON.parse(get(css)).full_records.forEach((r,i)=>{if(r.args.cmd.startsWith('sed -n '))record(css,i,r);});
const word=S+'word_automata_residual04/NATIVE_READS.json';
JSON.parse(get(word)).selected.forEach((r,i)=>{if(r.args.cmd.startsWith('sed -n '))record(word,i,r);});
const di=S+'noncommutative_graph_residual03_independent_desk01/INTAKE_NATIVE.json', ji=JSON.parse(get(di));
ji.core_reads.forEach((r,i)=>record(di,'core_reads/'+i,r));record(di,'old_locators/2',ji.old_locators[2]);
const df=S+'noncommutative_graph_residual03_independent_desk01/FOLLOWUP_LOCAL_NATIVE.json', jf=JSON.parse(get(df));
for(const k of ['old_reads','proof_rereads','cac_and_plan'])jf[k].forEach((r,i)=>record(df,k+'/'+i,r));
record(df,'sources_reread',jf.sources_reread);
for(const p of ['ROOT_INITIAL_CSS_READS_NATIVE.json','ROOT_RECENT_READS_NATIVE.json','ROOT_PRIMARY_REQUESTS.json','receive.cjs'])get(O+p);
// These are bibliographic-context PDF text extractions, not new final-page visual reviews.
for(const p of ['papers/134-recomputed-border-array-dynamics/main.pdf','papers/103-double-adjugate-matrix-dynamics/main.pdf','papers/72-rank-two-graph-commutation-spectra/main.pdf','papers/175-diagonal-feedback-commutator/main.pdf'])get(p);
for(const p of [...keys.keys()])get(p);
const result={status:'PASS_ROOT_NEGATIVE_DOCUMENTARY_RECEPTION',checks,groups,native_complete_source_returns:native,complete_input_keys:[...keys.values()],closed_literal_delta:2,science_runs:0,pilots:0,reserves:0,admissions:0,manuscript_reviews:0,builds:0,final_page_visual_reviews:0,external:'HOLD_EXTERNAL'};
// Result is attached by the product caller after actual successful completion; this reader writes nothing.
process.stdout.write(JSON.stringify(result,null,2)+'\n');
