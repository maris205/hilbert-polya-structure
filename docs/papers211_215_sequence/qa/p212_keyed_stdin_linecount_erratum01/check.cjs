'use strict';
// Documentary bytes only. Never loads/evaluates the reviewed programs.
const fs = require('node:fs');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const base = 'docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/';
const local = 'docs/papers211_215_sequence/qa/p212_keyed_stdin_linecount_erratum01/';
let checks = 0;
const ok = (a, m) => { checks++; assert(a, m); };
const eq = (a, b, m) => { checks++; assert.deepEqual(a, b, m); };
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const keys = [];
function read(p) {
  const before = fs.lstatSync(p, {bigint:true});
  ok(before.isFile() && !before.isSymbolicLink(), p);
  const fd = fs.openSync(p, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW);
  try {
    const opened = fs.fstatSync(fd, {bigint:true});
    const b = fs.readFileSync(fd);
    const after = fs.fstatSync(fd, {bigint:true});
    const end = fs.lstatSync(p, {bigint:true});
    for (const s of [opened, after, end]) for (const k of
      ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs','birthtimeNs'])
      eq(s[k], before[k], p+':'+k);
    eq(BigInt(b.length), before.size, p+':bytes');
    keys.push({path:p,bytes:b.length,sha256:sha(b)});
    return b;
  } finally { fs.closeSync(fd); }
}
const manifest = read(base+'SHA256SUMS');
eq(sha(manifest),'f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8');
const mt = manifest.toString('utf8');
ok(mt.endsWith('\n') && !mt.endsWith('\n\n') && !mt.includes('\r'));
const rows = mt.slice(0,-1).split('\n').map(line => {
  const m = /^([0-9a-f]{64})  \.\/([^\n]+)$/.exec(line);
  ok(m, 'exact ./-relative source manifest');
  ok(m[2].split('/').every(s=>s!==''&&s!=='.'&&s!=='..'));
  return {path:m[2],sha256:m[1]};
});
eq(rows.length,55); eq(new Set(rows.map(r=>r.path)).size,55);
const content = new Map();
for (const row of rows) {
  const b = read(base+row.path); eq(sha(b),row.sha256,row.path);
  content.set(row.path,b);
}
const actual=[];
function walk(rel='') {
  for (const name of fs.readdirSync(base+rel).sort()) {
    const p=rel+name,s=fs.lstatSync(base+p);
    ok(!s.isSymbolicLink(),p);
    if(s.isDirectory()) {ok(p==='companions'||p==='diffs',p);walk(p+'/');}
    else {ok(s.isFile(),p);actual.push(p);}
  }
}
walk(); eq(actual.sort(),[...rows.map(r=>r.path),'SHA256SUMS'].sort());
const handoff=content.get('HANDOFF.md');
eq(sha(handoff),'da09c9697133988256adec01aa4e5df66bc02aa99588edfef204a8471d9db9d8');
ok(handoff.toString().includes('The seven programs are 2,779 lines / 148,546 bytes.'));
const names=['observe.py','driver.js','outer_contract.py','python_runtime_probe.py',
  'node_runtime_probe.js','node_preload.js','product_capture.js'];
const expected=[[436,22106],[1048,55092],[747,41004],[146,8600],[66,5001],[147,10913],[89,5830]];
const lf=b=>b.reduce((n,v)=>n+(v===10),0);
const origin=JSON.parse(content.get('SOURCE_ORIGIN.json'));
const diff=JSON.parse(content.get('DIFF_TEXT_CHECK.json'));
const programRows=[];
let oldLines=0,added=0,deleted=0,lines=0,bytes=0;
for(let i=0;i<names.length;i++) {
  const name=names[i],b=content.get(name);
  eq([lf(b),b.length],expected[i],name);
  ok(handoff.toString().includes('| '+name+' | '+sha(b)+' |'));
  const origins=origin.derivatives.filter(r=>r.name===name);eq(origins.length,1);
  const d=diff.rows.filter(r=>r.name===name);eq(d.length,1);
  const old=read(origins[0].old_path);
  const entry={name,lines:lf(b),bytes:b.length,sha256:sha(b),old_lines:lf(old),
    added:d[0].added,deleted:d[0].deleted};
  eq(entry.old_lines+entry.added-entry.deleted,entry.lines);
  programRows.push(entry);oldLines+=entry.old_lines;added+=entry.added;deleted+=entry.deleted;
  lines+=entry.lines;bytes+=entry.bytes;
}
eq({oldLines,added,deleted,lines,bytes},{oldLines:2519,added:204,deleted:44,lines:2679,bytes:148546});
const wc=JSON.parse(read(local+'WC_NATIVE.json'));
eq(wc.request.cmd,'wc -l -c '+names.map(n=>base+n).join(' '));
eq(wc.return.exit_code,0);eq(wc.return.chunk_id,'abb65c');
const wcrows=wc.return.output.trim().split('\n').map(line=>line.trim().split(/\s+/));
eq(wcrows.length,8);
for(let i=0;i<7;i++) eq(wcrows[i],[String(expected[i][0]),String(expected[i][1]),base+names[i]]);
eq(wcrows[7],['2679','148546','total']);
const err=read(local+'ERRATUM.md').toString('utf8');
ok(err.includes('The seven programs are 2,679 lines / 148,546 bytes.'));
ok(err.includes('2,519 original program lines + 204 inserted − 44 deleted'));
process.stdout.write(JSON.stringify({schema:'p212-linecount-documentary-check-v1',
  status:'EXACT_LINECOUNT_ERRATUM_ONLY_NONAUTHOR_DELTA_PENDING',checks,
  old_package_payloads:rows.length,old_package_files:actual.length,programs:programRows,
  totals:{oldLines,added,deleted,lines,bytes},whole_read_keys:keys,
  no_reviewed_program_parse_or_execution:true,no_host_or_runtime_observation:true},null,2)+'\n');
