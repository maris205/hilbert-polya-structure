'use strict';
// Read-only serialization of the root agent's completed 102-operation semantic review.
// Writes stdout only; the caller preserves the new audit with apply_patch.
const fs=require('fs'), crypto=require('crypto');
const p='papers/29-bianchi-ideal-owner-refinement/';
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const read=x=>fs.readFileSync(p+x);
const bundlePath='notes/stage4_prime_revision_evidence_bundle_round6.json';
const bundle=JSON.parse(read(bundlePath));
function rationale(r,i,b) {
 if(r===1){
  if(i===26)return 'UNAUTHORIZED evidentiary-strength upgrade: procedurally separated reviews became independently assessed. REV-EIC-2 authorized reader-facing procedural translation, not reviewer/model independence. R2 operation 2 explicitly restores the correlated-error qualification; current R6 further narrows the historical activity assertion.';
  if(i>=2&&i<=23)return 'Authorized source-use narrowing: makes the unresolved passage ceiling explicit while retaining the project-specific no-transfer limitation. This is a contextual source-role statement, not an enacted owner mechanism or completed quotient. Existing source-wide negatives were not newly introduced by this operation.';
  if([1,34].includes(i))return 'Authorized prospective stop-state differentiation; unresolved design or numerical certification remains unresolved, not converted into a scientific negative or computed outcome.';
  if([24,27,28].includes(i))return 'Authorized codomain/mechanism construct clarification, with literal one-ideal frame explicitly strict rather than canonical, and downstream performance unable to select or rescue the mechanism.';
  if([29,30,31,32,33,36].includes(i))return 'Authorized typed prospective schema, interface and replay requirements; required fields and future controls are not represented as executed data or validation.';
  if([37,39].includes(i))return 'Authorized novelty and practical-usefulness narrowing; no field-wide priority or executed usefulness claim retained.';
  return 'Authorized provenance/reproducibility exposition or support-file provision. The operation does not itself upgrade a mathematical or empirical claim; later source-binding criticism and conservative withdrawals are retained separately in the history.';
 }
 if(r===2){
  if(i===2)return 'Authorized restoration of the R1 independence overstatement: same-model-family, procedural role separation, and correlated-error limitation are now explicit. This repairs current wording but does not erase R1 operation 26.';
  if(i===4)return 'Authorized fixture definition only: explicitly defined but not run, expected disposition is a test oracle and not an observed control or universal obstruction.';
  if(i>=7)return 'Authorized implementation-facing stop-state decision table, prospective and scoped; no gate or scientific result promoted.';
  return 'Authorized dated retrieval replay and file bindings, distinguished from original-session screening. This is newly observed bounded provenance, not reconstruction of missing historical rows or a scientific claim-strength upgrade.';
 }
 if(r===3){
  if(i<=22)return 'Authorized bounded source finalization: exact short source-side scope where available, otherwise explicit metadata-only use. Prior transfer claims are not strengthened; no locator is guessed. The retained source-wide S19 negative predates this operation and is later narrowed at R6.';
  if(i<=24)return 'Authorized binding of the 22-row source-finalization/matrix/receipt and 13+9 partition; file-level closure is expressly not a project theorem or Route credit.';
  if(i===25)return 'Authorized correction of stale Stage2.5/passage totals with the unresolved integrity failure and no-result limits retained.';
  if(i===26)return 'Authorized disclosure chronology update; exact backend unavailable and same-family correlated-error qualification retained. Later withdrawal of unbound activity details remains visible at R4.';
  return 'Authorized stale locator-count and status update to 13 exact contextual locators plus 9 metadata-only uses. The operation does not certify stronger theorem hypotheses, ownership, quotient completeness or Route advancement.';
 }
 if(r===4){
  if(i===2)return 'Authorized exact Chinese locator-status correction. Other source-wide Chinese wording remains inherited here and is explicitly aligned with the English narrowed scope at R5; the retained wording is not a newly introduced drift.';
  if([1,3,8,9,16].includes(i))return 'Authorized conservative narrowing from source-wide absence/sufficiency claims to open project obligations and bounded source use; this is not a mathematical nonexistence conclusion.';
  if([4,5,6,10,12,13,14,15,18,19,20].includes(i))return 'Authorized withdrawal of unbound historical, availability, integrity-clearance or activity claims, retaining present evidence limitations rather than asserting that missing records never existed.';
  if(i===7)return 'Authorized document-level and locked-tree scope; unexecuted scientific artifacts are no longer represented as an independent coherence or activity audit.';
  if(i===11)return 'Authorized narrowing from a separately-filed fixture assertion to a prospective in-text illustration and expected oracle, with no observed control or universal obstruction.';
  return 'Authorized withdrawal of unconfirmed personal contribution/accountability attestations; named-author metadata is not promoted to author approval or human verification.';
 }
 if(r===5)return 'Specifically authorized bilingual scope restoration: replaces source-wide absence with row-bounded use and open project obligations, retaining 13+9 and all frozen mathematical/Route boundaries.';
 return 'Specifically authorized heading and S19 paragraph narrowing: unresolved project evidence, not a universal statement that algorithms do not select owners. No locator or owner law is invented.';
}
const rows=[];
for(const r of bundle.rounds){
 const patch=JSON.parse(read(r.revision_patch.path));
 const pre=read(r.pre_round_draft.path).toString('utf8');
 const blocks=new Map([...pre.matchAll(/<!--block:(B\d+)-->\n([\s\S]*?)(?=<!--block:|$)/g)].map(m=>[m[1],m[2].trimEnd()]));
 const a=JSON.parse(read((r.author_adjudication||r.integrity_authorization).path));
 const road=JSON.parse(read((r.revision_roadmap||r.issue_list).path));
 patch.ops.forEach((o,k)=>{
  const hist=r.revision_round===1&&k===25;
  const auth=o.roadmap_item_ids.map(id=>(a.author_adjudications||a.author_decisions).find(x=>(x.item_id||x.correction_id)===id));
  const scope=o.roadmap_item_ids.map(id=>(road.items||road.issues).find(x=>(x.id||x.correction_id)===id));
  rows.push({revision_round:r.revision_round,operation_ordinal:k+1,operation:o.op,block_id:o.block_id,
   old_text:blocks.get(o.block_id),new_text:o.new_text,old_text_sha256:sha(blocks.get(o.block_id)),new_text_sha256:sha(o.new_text),
   roadmap_item_ids:o.roadmap_item_ids,declared_claim_strength_changes:o.claim_strength_changes||[],
   contemporaneous_authority:auth.map(x=>({id:x.item_id||x.correction_id,author_event_id:x.author_event_id,decision:x.author_triage||x.decision,authorized_targets:x.authorized_targets.filter(t=>t.block_id===o.block_id),claim_strength_authorizations:x.claim_strength_authorizations||[]})),contemporaneous_scope:scope.map(x=>({id:x.id||x.correction_id,description:x.description,suggested_action:x.suggested_action,verification_criteria:x.verification_criteria})),
   semantic_review:'completed_by_root_model_mediated_read_of_old_new_context_and_authority',
   judgment:hist?'STRENGTH-DRIFTED_HISTORICAL_CURRENT_RESTORED':'NO_UNAUTHORIZED_STRENGTH_MOVE_DETECTED',
   explanation:rationale(r.revision_round,k+1,o.block_id),
   current_repair_required:hist?false:null});
 });
}
const protocol='/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/shared/references/claim_strength_ladder.md';
const draft=read('notes/stage4_prime_revision_round6.tex');
const findings={schema_version:'claim-strength-drift-findings/1.0',status:'completed',final_draft_sha256:sha(draft),revision_evidence_bundle_sha256:sha(read(bundlePath)),
 detection_provenance:{kind:'model_mediated_semantic_review',detector_id:'P29-R4-FRESH-ROOT-CODEX-SEMANTIC-E6-20260906',protocol_sha256:sha(fs.readFileSync(protocol))},
 findings:[{finding_id:'ADV-E6-1',finding_type:'STRENGTH-DRIFTED',revision_round:1,block_id:'B0049',
 claim_location:'Historical Round1 operation26 B0049: procedurally separated reviews became independently assessed. Restored by Round2 operation2, further narrowed in Round4 operation5; CURRENT ROUND6 WORDING IS RESTORED and requires no repeat patch. New exact-draft finding binding does not automatically rebind any old author disposition.',
 prior_rung:'Procedurally separated review evidence, without independent-review warrant',
 current_rung:'Historical R1: independently assessed from editorial/domain/methodology/adversarial perspectives; current R6 no longer asserts this',
 dropped_qualifier:'procedurally separated (replaced with independently assessed without an authorized independence warrant)',
 roadmap_item_ids:['REV-EIC-2'],direction:'up'}]};
const start=Number(process.argv[2]||1),end=Number(process.argv[3]||rows.length);
console.log(JSON.stringify({audit:{schema_version:'p29-stage4.5-round4-e6-operation-audit/1.0',final_draft_sha256:sha(draft),bundle_sha256:sha(read(bundlePath)),rounds:6,operations:rows.length,all_operations_semantically_reviewed:true,current_drift_repair_required:false,historical_unauthorized_moves_detected:1,not_independent_scientific_validation:true,rows:rows.slice(start-1,end)},findings}));
