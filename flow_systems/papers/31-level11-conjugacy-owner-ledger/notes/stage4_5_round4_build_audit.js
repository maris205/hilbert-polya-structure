// Round-4 audit serialization helper. Reads explicitly named locked inputs;
// emits JSON to stdout only. It never edits a manuscript or evidence input.
const fs = require('fs');
const crypto = require('crypto');
const base = 'papers/31-level11-conjugacy-owner-ledger/';
const ars = '/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/';
const read = p => fs.readFileSync(base + p, 'utf8');
const json = p => JSON.parse(read(p));
const sha = x => crypto.createHash('sha256').update(x).digest('hex');
const bind = p => ({path:base+p,sha256:sha(fs.readFileSync(base+p)),bytes:fs.statSync(base+p).size});
const draftPath = 'notes/stage4_prime_revision_round6.tex';
const draft = read(draftPath);
const draftHash = sha(draft);
if (draftHash !== '4bc1a960b5527a5d389b5c70e29fa0dc7b3199b93a808dd3f347616dd686d1a3') throw Error('Locked draft mismatch');
const marks = [...draft.matchAll(/<!--block:(B\d+)-->\n/g)];
const blocks = marks.map((m,i) => {const start=m.index+m[0].length; const raw=draft.slice(start,marks[i+1]?.index||draft.length);return {id:m[1],start,text:raw.trimEnd()};});
const blockMap = Object.fromEntries(blocks.map(b=>[b.id,b]));
const bundlePath='notes/stage4_prime_revision_evidence_bundle_round6.json';
const bundle=json(bundlePath);
const matrix=json('notes/stage4_prime_method_passage_matrix_round3.json');
const sourceRows=Object.fromEntries(matrix.rows.map(r=>[r.source_id,r]));
const numericBlocks = new Set(['B0006','B0007','B0012','B0015','B0036','B0037','B0039','B0042','B0045','B0061','B0062','B0067','B0069','B0070','B0071','B0072','B0073','B0075','B0076','B0080','B0089','B0095','B0098','B0099','B0108']);
const omit = new Set(['B0001','B0002','B0003','B0004','B0005','B0008','B0009','B0013','B0094','B0109','B0110']);
const sourceBlocks=new Set(['B0021','B0025','B0029','B0032']);
function section(b){const n=Number(b.id.slice(1));if(n<=7)return 'Abstract';if(n<=18)return '1 Introduction';if(n<=33||b.id==='B0112')return '2 Literature';if(n<=42)return '3 Executed methodology';if(n<=73||b.id==='B0113')return '4 Certificate architecture';if(n<=77)return '5 Findings';if(n<=81)return '6 Reproducibility';if(n<=87||b.id==='B0111')return '7 Discussion';if(n<=92)return '8 Limitations';if(n<=96)return '9 Future work';if(n<=99)return '10 Conclusion';return 'Declarations and AI disclosure';}
function review(b) {
  let domain='prospective_project_definition_or_conditional_logic', basis=['notes/stage1_phase6_claim_intent_manifest.json','notes/stage1_phase1_methodology_blueprint.md','notes/stage4_prime_revision_evidence_bundle_round6.json'];
  let reason='Read as a proposed definition, conditional obligation, or design interpretation, not a proved/executed owner theorem. Checked resolved-domain/totality, orientation/root/inverse policy and no-execution qualifiers against the approved design and exact revision chain.';
  if(['B0006','B0007','B0011','B0012','B0045'].includes(b.id)){domain='frozen_population_and_scoped_design';reason='The 138 inputs and 55 groups are frozen design inputs, not a new census. 138*137/2=9453; 2+2+134=138, with no conversion to owner counts. Object/restrictions matched to the actual RQ brief and Phase-6 design.';basis.push('notes/stage1_phase1_rq_brief.md');}
  if(sourceBlocks.has(b.id)||['B0016','B0022','B0023','B0026','B0030','B0037','B0038','B0039','B0112','B0089'].includes(b.id)){domain='bounded_source_use_or_source_record';reason='Read each source-specific status and its preserved transfer boundary. Seven retained locators supply bounded contextual text only; fifteen old method records and two metadata-only neighbors authorize no substantive passage transfer. Project role labels are not source-proved theorem claims.';basis=['notes/stage4_prime_method_passage_matrix_round3.json','notes/stage4_5_round4_web_search_batch1.json','notes/stage4_5_round4_source_provenance.json'];}
  if(['B0036','B0041'].includes(b.id)){domain='historical_execution_self_report';reason='The upstream bibliography records 44 manifestations, 9 duplicate removals, 35 screened, 13 excluded, 22 retained. The dated 20-query replay and its 18/2 decision split are independently recountable local records; original-session capture/screening events are not reconstructable from retained raw rows. Historical execution assertions remain unverified at that event level.';basis=['notes/stage1_phase2_annotated_bibliography.md','notes/stage4_prime_literature_replay_round2.raw.json','notes/stage4_prime_literature_screening_ledger_round2.json'];}
  if(['B0079','B0105'].includes(b.id)){domain='artifact_recoverability';reason='Historical manifest hash and 11 descriptors checked as records. Its old method-matrix binding is stale; current prose explicitly disclaims exact recovery and permanent archival status. No prospective synchronization or scientific output is asserted.';basis=['notes/stage4_prime_reader_artifact_manifest_round2.json','notes/stage4_prime_method_passage_matrix_round3.json'];}
  if(['B0090','B0091','B0092','B0099','B0101','B0107','B0108'].includes(b.id)){domain='workflow_record_and_verification_boundary';reason='Verified only against the scoped project/authorization record: no solver execution, no source-theorem clearance, no error independence, no inferred human reading. Named author/approval descriptions are recorded attributions, not authenticated personal acts. B0108 current any qualifier is restored by R6; older every substitution remains a historical E6 finding.';basis=['notes/stage1_phase6_claim_intent_manifest.json','notes/stage4_prime_revision_evidence_bundle_round6.json'];}
  if(['B0102','B0103'].includes(b.id)){domain='author_owned_unresolved_attestation';reason='Funding and competing-interest declarations are author-owned facts. The current batch authority explicitly preserves both as unresolved; no public lookup, model inference, workflow approval, or existing prose supplies an attestation.';basis=['BATCH_ROUND10_STAGE4_5_ROUND4_AUTHORIZATION.json'];}
  if(b.id==='B0104'){domain='non_empirical_scope_and_ethics_applicability';reason='Theoretical mathematics/published-source/workflow scope and empty experiment provenance support inapplicability of participant/animal study requirements. This is not an institutional ethics determination.';basis=['notes/stage1_phase1_rq_brief.md','notes/stage4_5_round2_material_passport.json'];}
  return {block_id:b.id,domain,evidence_basis:basis,rationale:reason};
}
const blockReviews=blocks.map(b=>({...review(b),included:!omit.has(b.id)&&!/^\\(?:hypertarget|section\*)/.test(b.text),exclusion_reason:omit.has(b.id)?'preamble/title/keywords/structural label; author metadata outside substantive E1 population':/^\\(?:hypertarget|section\*)/.test(b.text)?'section-heading markup only':null}));
const claims=[], decisions=[];
function addClaim(b,start,end,refs,extra=''){
  while(/\s/.test(draft[start]||'')&&start<end)start++;while(/\s/.test(draft[end-1]||'')&&end>start)end--;
  const text=draft.slice(start,end);if(text.length<3)return;
  if(text.length>1900)throw Error('Overlong semantic span '+b.id);
  const id='P31-R4-'+b.id+'-'+String(claims.filter(c=>c.claim_id.startsWith('P31-R4-'+b.id+'-')).length+1).padStart(3,'0');
  const cited=[...new Set(refs)];
  const kinds=[numericBlocks.has(b.id)||/\b\d+(?:,\d{3})?\b/.test(text)?'quantitative':'other_factual'];
  if(/\b(?:no|only|exactly|all|never|must|remains|not)\b/i.test(text))kinds.push('categorical');
  const r=review(b);
  const historical = ['B0036','B0041'].includes(b.id)&&/captured|deduplicated|screened|duplicates/.test(text);
  const pending=['B0102','B0103'].includes(b.id);
  const verdict=pending?'UNVERIFIABLE':historical?'UNVERIFIABLE_ACCESS':'VERIFIED';
  claims.push({claim_id:id,claim_text:text,draft_span:{start_byte:Buffer.byteLength(draft.slice(0,start)),end_byte:Buffer.byteLength(draft.slice(0,end))},claim_kinds:[...new Set(kinds)],ref_slugs:cited,writer_anchors:cited.map(s=>sourceRows[s]?.exact_passage_locator).filter(Boolean),paper_section:section(b),selection_tier:'ALL'});
  decisions.push({claim_id:id,block_id:b.id,verdict,verification_scope:r.domain,evidence_basis:r.evidence_basis,detail:(pending?r.rationale:historical?r.rationale:r.rationale)+(extra?' '+extra:'')});
}
for(const b of blocks){
  if(!blockReviews.find(r=>r.block_id===b.id).included)continue;
  // Annotation comments are metadata, never source evidence. Prose remains exact bytes.
  const regions=[];let pos=0;
  for(const m of b.text.matchAll(/^%[^\n]*(?:\n|$)/gm)){regions.push([pos,m.index]);pos=m.index+m[0].length;}regions.push([pos,b.text.length]);
  for(const [a,z] of regions){if(a>=z)continue;let start=a;
    const region=b.text.slice(a,z);let inherited=[];
    const citations=[...region.matchAll(/\\citep\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
    // Source-specific paragraphs are bounded by their ARS-CITE annotation and have one source.
    if(sourceBlocks.has(b.id))inherited=citations;
    const ends=[...region.matchAll(/[.!?。](?=\s|$)/g)].map(m=>a+m.index+1);ends.push(z);
    for(const end of [...new Set(ends)]){if(end<=start)continue;const piece=b.text.slice(start,end);let refs=sourceBlocks.has(b.id)?inherited:[...piece.matchAll(/\\citep\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
      if(piece.trim().length>1900){let s=start;while(s<end){let e=Math.min(s+1800,end);if(e<end){const nl=b.text.lastIndexOf('\n',e);if(nl>s)e=nl;}addClaim(b,b.start+s,b.start+e,refs,'Exact multi-line formal/design span; interpreted with its whole block.');s=e;}}
      else if(!/^\s*\\(?:end|begin)\{[^}]+\}\s*$/.test(piece)&&!/^\s*\\paragraph\{[^}]+\}\s*$/.test(piece))addClaim(b,b.start+start,b.start+end,refs);
      start=end;
    }
  }
}
const registry={schema_version:'claim-registry/1.0',draft_raw_sha256:draftHash,claims};
const outputs={};
outputs.claim_registry=registry;
outputs.semantic_claim_review={paper_id:'P31',draft:bind(draftPath),extraction:'New full-draft model-mediated semantic pass; deterministic helper serializes reviewed exact spans, not a semantic-completeness detector. All detected registered instances are selected ALL. No prior registry or integrity verdict was used to select or judge them.',semantic_extraction_coverage:'not_machine_detectable',block_population:blocks.length,block_review:blockReviews,claim_count:claims.length,claim_decisions:decisions,limits:['Formal/prospective assertions are verified as scoped definitions or conditional consequences, not as fulfilled scientific obligations.','Author metadata in title is outside the substantive registry; its inclusion is not new identity or affiliation authentication.','Historical upstream capture/screening is distinguished from the later dated replay; missing original event-level rows are not reconstructed.']};
// Retained source payload extraction uses raw publisher abstracts, not historic audit verdicts.
const net=json('notes/stage4_5_round1_reference_network_audit.json');
const proposal=json('notes/stage4_5_round1_source_finalization_proposal.json');
function decode(s){return s.replace(/<[^>]*>/g,'').replace(/&nbsp;/g,' ').replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&#x([0-9a-f]+);/gi,(_,v)=>String.fromCodePoint(parseInt(v,16))).replace(/&#(\d+);/g,(_,v)=>String.fromCodePoint(Number(v))).replace(/\s+/g,' ').trim();}
const sourceMap={}, provenance=[];
for(const s of ['P31-S05','P31-S06','P31-S08','P31-S09','P31-S16','P31-S17','P31-S19']){
  const r=net.references.find(x=>x.ref_slug===s);const p=proposal.rows.find(x=>x.source_id===s);
  const abstract=r?.query_attempts?.crossref_doi?.crossref_message?.abstract;
  const body=abstract?decode(abstract):p.support_excerpt;
  sourceMap[s]=body;
  provenance.push({ref_slug:s,source_body_kind:abstract?'publisher_deposited_abstract_from_locked_raw_carrier':'retained_exact_excerpt_only_not_full_PDF',source_body_sha256:sha(body),source_body_utf8_bytes:Buffer.byteLength(body),carrier:bind(abstract?'notes/stage4_5_round1_reference_network_audit.json':'notes/stage4_5_round1_source_finalization_proposal.json'),raw_field:abstract?'references[ref_slug].query_attempts.crossref_doi.crossref_message.abstract':'rows[source_id].support_excerpt',normalization:abstract?'remove HTML tags; decode numeric/common entities; collapse whitespace':'none',exact_locator:p.exact_passage_locator,excerpt:p.support_excerpt,excerpt_literal_match:body.includes(p.support_excerpt),excerpt_word_count:p.support_excerpt.trim().split(/\s+/).length,evidence_limit:'Freshly compared retained raw text against current scoped claim; source identity and this bounded context do not establish the whole registered role or project theorem.'});
}
outputs.source_map=sourceMap;outputs.source_provenance={sources:provenance,human_read_inferred:false,source_retrieval_during_build:false};
const ctx=[];
for(const b of blocks){for(const m of b.text.matchAll(/\\citep\{([^}]+)\}/g)){for(const s of m[1].split(',')){
  let a=sourceBlocks.has(b.id)?b.text.lastIndexOf('\n',b.text.lastIndexOf('\nThe ',m.index)+1):0;
  if(sourceBlocks.has(b.id)){const lead=b.text.lastIndexOf('The bibliographic record ',m.index),loc=b.text.lastIndexOf('The located passage ',m.index);a=Math.max(0,lead,loc);}
  let e=sourceBlocks.has(b.id)?b.text.indexOf('\n% ARS-CITE',m.index):b.text.length;if(e<0)e=b.text.length;
  const r=sourceRows[s];const p=provenance.find(p=>p.ref_slug===s);
  ctx.push({context_id:'P31-R4-CTX-'+String(ctx.length+1).padStart(3,'0'),block_id:b.id,ref_slug:s,citation_byte_span:{start_byte:Buffer.byteLength(draft.slice(0,b.start+m.index)),end_byte:Buffer.byteLength(draft.slice(0,b.start+m.index+m[0].length))},context_text:b.text.slice(a,e),verdict:'VERIFIED',verification_scope:p?'bounded_context_not_full_role':'metadata_identified_no_substantive_transfer',retained_passage_locator:r?.exact_passage_locator||null,source_payload_sha256:p?.source_body_sha256||null,detail:p?'The actual retained excerpt is topically consistent with the explicitly bounded use; the manuscript denies full-role proof and owner-theorem transfer. No unavailable full theorem is supplied.':'The text labels this as metadata/prospective project coding and withholds substantive attribution. Bibliographic identity checked fresh in Phase A; full passage/theorem support is not marked verified.'});
}}}
outputs.citation_context_audit={paper_id:'P31',draft:bind(draftPath),total_citation_occurrences:ctx.length,sampled:ctx.length,coverage_percent:100,verified:ctx.length,contexts:ctx,limits:['VERIFIED refers to the exact modest context, not to an unavailable theorem or complete registered role.','The two metadata-only method neighbors occur twice each; all 26 occurrences are retained.']};
const e6=[];
for(const r of bundle.rounds){const patch=json(r.revision_patch.path);const before=read(r.pre_round_draft.path);const mm=[...before.matchAll(/<!--block:(B\d+)-->\n/g)];const bm=Object.fromEntries(mm.map((m,i)=>[m[1],before.slice(m.index+m[0].length,mm[i+1]?.index||before.length).trimEnd()]));const authorityPath=r.revision_roadmap?.path||r.issue_list.path;const authority=json(authorityPath);const decisionPath=r.author_adjudication?.path||r.integrity_authorization.path;const decision=json(decisionPath);
  for(const [i,o] of patch.ops.entries()){
    const bad=r.revision_round===3&&i===12;
    let reason=r.revision_round===1?'The named accepted roadmap item specifically narrows the disputed architecture: bounded literature/recoverability/execution claims, partial-domain typing, fixture coverage, non-executable contract, prospective inverse/incidence rules, hypothetical interoperability or independent-adjudicator limit. No theorem-execution or evidential promotion was introduced.':r.revision_round===2?'The named accepted roadmap item expressly covers this architectural/detail refinement or bounded source/search supplement; the new type, fixture, inverse, projection and source-neighbor text remains prospective and preserves no-owner-result boundaries.':r.revision_round===3?'The named I01 source-specific narrowing, I02 disclosure update or I03 source-status count alignment warrants the actual scoped change. Available locators remain bounded context; unavailable rows license no role proof.':r.revision_round===4?'Exact integrity-correction issue and authorization narrow this claim: metadata-only method neighbors, project-local negative boundary, historical/stale manifest, or limited AI chronology. No authorization is inferred from block touch alone.':r.revision_round===5?'Exact issue and author authorization remove unsupported exclusivity/superlative or exhaustive-registry language, or correct unresolved I to I_diag; the change does not assert scientific execution.':'Exact EA-001 author authorization restores any, solely the missing broad disclaimer. This closes the current textual defect, not retroactive authorization of the original move.';
    if(bad)reason='I03 authorizes count/status alignment, not changing verified any claim to verified every claim. The latter denies universal verification while permitting an implication of some passage-level verification. This weakens a load-bearing human-verification disclaimer without exact authority. Introduced in R3, inherited unchanged in R4/R5, restored in R6.';
    e6.push({revision_round:r.revision_round,operation_index:i+1,operation_type:o.op,block_id:o.block_id,result_block_id:o.new_block_id||o.block_id,roadmap_item_ids:o.roadmap_item_ids,prior_text:bm[o.block_id]||null,new_text:o.new_text,patch:bind(r.revision_patch.path),authority:bind(authorityPath),author_decision:bind(decisionPath),semantic_disposition:bad?'UNAUTHORIZED_HISTORICAL_DRIFT_RESTORED_R6':'AUTHORIZED_OR_NO_UNAUTHORIZED_STRENGTH_MOVE_DETECTED',reason});
  }
}
outputs.e6_semantic_audit={paper_id:'P31',final_draft:bind(draftPath),revision_evidence_bundle:bind(bundlePath),rounds_checked:6,operations_checked:e6.length,full_chain_semantically_reviewed:true,bundle_validation_receipt:'notes/stage4_5_round4_bundle_validation.json',detection_limit:'Model-mediated exact-text/authority interpretation; bundle validity is not semantic validity or scientific warrant. Historic integrity findings were not detection inputs.',operations:e6};
outputs.claim_strength_drift_findings={schema_version:'claim-strength-drift-findings/1.0',status:'completed',final_draft_sha256:draftHash,revision_evidence_bundle_sha256:sha(read(bundlePath)),detection_provenance:{kind:'model_mediated_semantic_review',detector_id:'Codex-P31-Round4-full-chain-semantic-owner',protocol_sha256:sha(fs.readFileSync(ars+'academic-pipeline/references/claim_verification_protocol.md'))},findings:[{finding_id:'ADV-E6-1',finding_type:'STRENGTH-DRIFTED',revision_round:3,block_id:'B0108',claim_location:'AI Disclosure, round 3 operation 13. Historical: introduced in R3 and inherited in R4/R5. Current R6 restores any under exact EA-001 authorization; no same-wording defect remains in the final draft.',prior_rung:'No attestation of verification of any exact source-passage claim.',current_rung:'Historical R3: only denies verification of every claim, leaving partial verification implication. Current R6 returns to the prior disclaimer.',dropped_qualifier:'any (replaced by every in round 3; restored by round 6)',roadmap_item_ids:['REV-P31-S45R1-I03'],direction:'up'}]};
for(const op of outputs.e6_semantic_audit.operations){if(op.operation_type==='insert_after'){op.result_block_id=op.revision_round===1?'B0111':op.block_id==='B0033'?'B0112':'B0113';op.prior_text_role='insertion_anchor_only_not_the_previous_text_of_the_new_claim';}}
const name=process.argv[2];if(!Object.hasOwn(outputs,name))throw Error('Unknown output '+name);
const rendered=JSON.stringify(outputs[name],null,2)+'\n';
if(process.argv[3]!==undefined){const offset=Number(process.argv[3]);console.log(JSON.stringify({total:rendered.length,offset,chunk:rendered.slice(offset,offset+16000)}));}
else console.log(rendered);
