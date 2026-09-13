// Read-only current-draft extraction. Emits candidates, never assigns verdicts or writes files.
const fs = require('fs'), crypto = require('crypto');
const base = 'papers/32-homology-cover-renormalization-uniformity/notes/';
const path = base + 'stage4_prime_revision_round6.tex';
const raw = fs.readFileSync(path), draft = raw.toString('utf8');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const markers = [...draft.matchAll(/<!--block:(B\d+)-->\n/g)];
const blocks = [], units = []; let section = 'Front matter';
function add(block, a, b, type) {
  const text = draft.slice(a,b); const left = text.search(/\S/); if(left < 0)return;
  const trimmed = text.trimEnd(); a += left; b = a + trimmed.length - left;
  const claim_text = draft.slice(a,b); if(!/[A-Za-z\u3400-\u9fff0-9]/.test(claim_text))return;
  units.push({block_id:block,unit_type:type,text:claim_text,start_byte:Buffer.byteLength(draft.slice(0,a)),end_byte:Buffer.byteLength(draft.slice(0,b)),section});
}
function prose(block,a,b) {
  let start=a, depth=0;
  for(let i=a;i<b;i++) {
    if(draft[i]==='{' && draft[i-1]!=='\\') depth++;
    if(draft[i]==='}' && draft[i-1]!=='\\') depth--;
    if(draft[i]==='.' && depth===0 && (i+1===b || /\s/.test(draft[i+1]))) { add(block,start,i+1,'sentence_or_math_clause'); start=i+1; }
  }
  add(block,start,b,'sentence_or_math_clause');
}
for(let i=0;i<markers.length;i++) {
  const m=markers[i], a=m.index+m[0].length,b=i+1<markers.length?markers[i+1].index:draft.length,t=draft.slice(a,b),id=m[1];
  blocks.push({block_id:id,start_byte:Buffer.byteLength(draft.slice(0,a)),end_byte:Buffer.byteLength(draft.slice(0,b)),text:t});
  const heading=t.match(/\\(?:sub)?section\*?\{([^}]+)\}/); if(heading){section=heading[1].replace(/\s+/g,' '); if(!/\\paragraph/.test(t))continue;}
  if(['B0001','B0002','B0004','B0005','B0129','B0130'].includes(id))continue;
  if(id==='B0003'){add(id,a,b,'author_metadata');continue;}
  if(id==='B0007'){add(id,a,b,'chinese_abstract_compound');continue;}
  if(/\\begin\{tabular\}/.test(t)) {
    // Preserve each literal table row, with table title/tail separately typed.
    const begin=t.indexOf('\\toprule'), end=t.indexOf('\\bottomrule');
    const bodyStart=a+begin+'\\toprule'.length,bodyEnd=a+end;
    let last=bodyStart;const slice=draft.slice(bodyStart,bodyEnd), rows=[...slice.matchAll(/\\\\\s*\n/g)];
    for(const r of rows){add(id,last,bodyStart+r.index+2,'table_row');last=bodyStart+r.index+r[0].length;}
    add(id,last,bodyEnd,'table_row');
    const tail=t.indexOf('\\end{center}');if(tail>=0)prose(id,a+tail+'\\end{center}'.length,b);
    continue;
  }
  // Exclude source-marker comments, not their adjacent manuscript context.
  let last=a;for(const c of t.matchAll(/^%[^\n]*(?:\n|$)/gm)){prose(id,last,a+c.index);last=a+c.index+c[0].length;}prose(id,last,b);
}
console.log(JSON.stringify({draft:{path,bytes:raw.length,sha256:sha(raw)},blocks,units}));
