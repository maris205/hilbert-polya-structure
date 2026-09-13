// Read-only extraction helper: stdout only; does not write or validate scientific artifacts.
'use strict';
const fs = require('fs');
const crypto = require('crypto');
const draft = 'papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round6.tex';
const text = fs.readFileSync(draft, 'utf8');
const blocks = [...text.matchAll(/<!--block:(B\d+)-->\n([\s\S]*?)(?=<!--block:|$)/g)];
const excluded = new Set(['B0001','B0002','B0003','B0005','B0007','B0103','B0104','B0105','B0106','B0107','B0108','B0109','B0110','B0111','B0115']);
let section = 'Abstract';
const rows = [];
const exclusions = [];
const overrides = {
  B0024: 'supplies neither an owner law nor a literal-ideal selection mechanism',
  B0025: 'No project mechanism or owner assignment is inferred',
  B0029: 'no substantive proposition from the earlier context sentence is attributed',
  B0030: 'The setting is not evidence that a literal ideal owner',
  B0034: 'The bounded Round-3 finalization pass yielded no passage-bearing locator',
  B0035: 'passage level. No instantiated level-(3) solver is claimed',
  B0036: 'this source at passage level. Canonicalization certificates remain separate obligations',
  B0037: 'this source at passage level. The algorithm is not transferred',
  B0042: 'No ideal-owner selection law is established by the retained metadata-only',
  B0080: 'Earlier manuscript-audit paths, a commit locator, and dated replay, ledger',
  B0081: 'Each interface must publish canonical bytes, dependency hashes, an allowed'
};
for (const match of blocks) {
  const [matched, blockId, raw] = match;
  const heading = raw.match(/\\(?:sub)?section\*?\{([^}]+)\}/);
  if (heading) section = heading[1];
  let clean = raw.replace(/^%.*$/gm, '').replace(/\\(?:sub)?section\*?\{[^}]+\}/g, '')
    .replace(/\\(?:begin|end)\{[^}]+\}/g, '').replace(/\\(?:begingroup|endgroup|sloppy|maketitle|noindent|par)\b/g, '').trim();
  if (excluded.has(blockId) || !clean) {
    exclusions.push({block_id:blockId, reason:excluded.has(blockId)?'frontmatter, keywords, closing author declarations, or bibliography outside body-screen denominator':'heading-only block'});
    continue;
  }
  const queryText = clean.replace(/\\allowbreak\{\}/g, '').replace(/\\[a-zA-Z]+\{([^{}]*)\}/g, '$1').replace(/~/g, ' ').replace(/\s+/g, ' ');
  const area = queryText.includes('source-side statement:') ? queryText.split('source-side statement:')[1] : queryText;
  const fragmentMatch = area.match(/\b(?:[A-Za-z][A-Za-z'’-]*[,;:]?\s+){9}[A-Za-z][A-Za-z'’-]*\b/);
  let fragment = fragmentMatch?.[0];
  if (overrides[blockId]) fragment = overrides[blockId];
  let language = 'en';
  if (blockId === 'B0006') { fragment = '研究僅綜整已凍結的二十二項來源及既有評審紀錄'; language = 'zh-TW'; }
  if (!fragment) throw Error(blockId + ': no characteristic fragment');
  rows.push({paragraph_id:'P29-D-'+String(rows.length+1).padStart(3,'0'), block_id:blockId, section,
    first_line:text.slice(0,match.index).split('\n').length+1, characteristic_fragment:fragment, language,
    quoted_query:'"'+fragment+'"', supplementary_query:fragment,
    raw_block_sha256:crypto.createHash('sha256').update(raw).digest('hex')});
}
console.log(JSON.stringify({draft, draft_sha256:crypto.createHash('sha256').update(text).digest('hex'),
  selection:'all body prose blocks including both abstracts; headings, frontmatter, keywords, closing author declarations, and bibliography excluded',
  paragraph_count:rows.length, exclusions, rows}));
