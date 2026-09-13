'use strict';
// Read-only semantic-audit view. Reads the bound chain; emits selected complete
// old/new text plus contemporaneous authority to stdout. It is not a validator.
const fs = require('fs');
const crypto = require('crypto');
const root = 'papers/29-bianchi-ideal-owner-refinement/';
const bundle = JSON.parse(fs.readFileSync(root + 'notes/stage4_prime_revision_evidence_bundle_round6.json'));
const round = bundle.rounds.find(r => r.revision_round === Number(process.argv[2]));
const start = Number(process.argv[3] || 1), end = Number(process.argv[4] || start);
if (!round) throw Error('Unknown round');
const patch = JSON.parse(fs.readFileSync(root + round.revision_patch.path));
const oldDraft = fs.readFileSync(root + round.pre_round_draft.path, 'utf8');
const blocks = new Map([...oldDraft.matchAll(/<!--block:(B\d+)-->\n([\s\S]*?)(?=<!--block:|$)/g)].map(m => [m[1], m[2].trimEnd()]));
const authority = JSON.parse(fs.readFileSync(root + (round.author_adjudication || round.integrity_authorization).path));
const roadmap = JSON.parse(fs.readFileSync(root + (round.revision_roadmap || round.issue_list).path));
for (let i = start - 1; i < Math.min(end, patch.ops.length); i++) {
  const op = patch.ops[i];
  const ids = op.roadmap_item_ids;
  console.log(JSON.stringify({round:round.revision_round, ordinal:i+1, op:op.op, block_id:op.block_id,
    old_text:blocks.get(op.block_id), new_text:op.new_text, declared_strength_changes:op.claim_strength_changes,
    authority:ids.map(id => (authority.author_adjudications || authority.author_decisions).find(x => (x.item_id || x.correction_id) === id)).map(x => ({id:x.item_id||x.correction_id,author_event_id:x.author_event_id,decision:x.author_triage||x.decision,target:x.authorized_targets.filter(t=>t.block_id===op.block_id),claim_strength_authorizations:x.claim_strength_authorizations||[]})),
    authorized_scope:ids.map(id => (roadmap.items || roadmap.issues).find(x => (x.id || x.correction_id) === id)).map(x => ({id:x.id||x.correction_id, description:x.description, action:x.suggested_action, criteria:x.verification_criteria})),
    old_sha256:crypto.createHash('sha256').update(blocks.get(op.block_id)||'').digest('hex'),
    new_sha256:crypto.createHash('sha256').update(op.new_text||'').digest('hex')}, null, 2));
}
