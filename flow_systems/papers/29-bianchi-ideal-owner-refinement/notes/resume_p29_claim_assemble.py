"""Read-only stdout assembler for the current P29 sentence-level review.

Judgments are explicit after reading all current blocks and original held source
surfaces. This is not a verifier, patch replay, or scientific computation.
"""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path('/root/autodl-tmp/flow_systems')
P = ROOT / 'papers/29-bianchi-ideal-owner-refinement'
N = P / 'notes'
DRAFT = N / 'stage4_prime_revision_round5.tex'
raw = DRAFT.read_bytes()
draft = raw.decode('utf-8')
draft_hash = hashlib.sha256(raw).hexdigest()
bs = {m.group(1): {'text': m.group(2).rstrip(), 'start': m.start(2)}
      for m in re.finditer(r'<!--block:(B\d+)-->\n(.*?)(?=<!--block:|\Z)', draft, re.S)}
prefix = [0]
for ch in draft:
    prefix.append(prefix[-1] + len(ch.encode('utf-8')))
def span(a, b):
    return {'start_byte': prefix[a], 'end_byte': prefix[b]}
def rel(path):
    return str(path.relative_to(ROOT))
def desc(path):
    data = path.read_bytes()
    return {'path': rel(path), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

LOCK = 'BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json'
BRIEF = rel(N / 'stage1_prestart_brief.md')
BUNDLE = rel(N / 'stage4_prime_revision_evidence_bundle_round5.json')
FINAL = rel(N / 'stage4_prime_source_finalization_round3.json')
MATRIX = rel(N / 'stage4_prime_claim_passage_matrix_round3.json')
PASSPORT = rel(N / 'stage4_5_round2_material_passport.json')
INTENT = rel(N / 'stage1_phase6_claim_intent_manifest.json')
TRACE = rel(N / 'stage3_prime_round3_traceability.json')

R = {}
def assign(ids, kind, reason, carriers):
    for bid in ids.split():
        R[bid] = {'basis_kind': kind, 'reason': reason, 'carriers': carriers}
assign('B0004 B0006', 'bounded_abstract_and_prospective_design',
       'The current abstracts state the same bounded 22-source, 13+9 source-use partition and open project owner/quotient obligations, expressly not literature-wide absence. Gate, serializer, registration and replay statements are prospective; no owner, statistic, theorem or Route promotion is reported. R5 specifically corrected the Chinese corpus-scope sentence.',
       [LOCK, MATRIX, BUNDLE])
assign('B0009', 'frozen_object_definition',
       'The lock and prestart inheritance specify unit-speed level-(3) Gaussian Bianchi flow, arclength clock, primitive loxodromic inversion-paired owners and one literal prime ideal. These are selected definitions, not new source-derived results. If alpha=u beta for a unit u, (alpha)=(beta); conjugate split prime ideals are distinct by the stated split-ideal convention.', [LOCK, BRIEF])
assign('B0010', 'conditional_research_question',
       'The question asks for certification obligations without assuming an admissible mechanism exists. Replacing the codomain changes that explicitly frozen question; no alternative is proved impossible.', [BRIEF, LOCK])
assign('B0011 B0070 B0078', 'design_non_entailment_not_statistical_independence',
       'A label-valued rule alone supplies no complete root/conjugacy/inversion decision, while a certified population alone supplies no ideal-selection rule. This separates proof obligations, not random events or every implementation. Gate-M evaluation can require certified inputs without its formal law supplying the complete finite Gate-Q construction. No mathematical or empirical independence theorem is established.', [BRIEF, BUNDLE])
assign('B0012 B0014 B0017 B0086 B0102', 'typed_failure_and_design_interpretation',
       'The architecture distinguishes missing evidence, candidate-specific law violation, unresolved relations and downstream non-evaluability. These are proposed reporting/typing rules. Interpretable or diagnostic value concerns that distinction, not observed effectiveness, robustness or performance. Undefined downstream estimand is not a computed zero.', [BRIEF, BUNDLE, LOCK])
assign('B0015', 'input_output_and_quantifier_distinction',
       'An ideal factorization routine operates on supplied arithmetic input and does not by itself specify a geometric-owner-to-ideal map. Ambient algorithms need hypothesis and representation bridges. Labeling rows does not prove primitive-owner identities, and failure of bounded search is not a universal negative. These are logical distinctions, not a complete inventory of the cited algorithms.', [])
assign('B0016 B0077 B0098', 'frozen_strict_codomain_and_prospective_scope',
       'The frozen project defines one literal nonzero prime ideal with associates identified and split conjugates distinct. Norms, composite ideals and Galois orbits are different output types. The authorizing chain explicitly retains this strict noncanonical frame, candidate-local obstruction and pre-outcome registration; alternative studies require separate scope.', [BRIEF, LOCK, BUNDLE])
assign('B0112 B0081', 'prospective_dependency_and_replay_interfaces',
       'The five named interfaces and their acceptance/stop rules are prospective design requirements. Complete Gate-Q population and admissible Gate-M record are prerequisites for performance; replay pass requires expected dispositions and dependency hashes to agree. Producer/verifier non-reuse is a future contract, not present independent scientific validation.', [BUNDLE, LOCK])
assign('B0031', 'logical_object_law_distinction',
       'The retained Picard/geodesic excerpts supply object context, but object terminology alone does not specify an owner-to-ideal function. Read as that project-use distinction under the individual bounded paragraphs, not as a source-wide proof of absence.', [FINAL, MATRIX])
assign('B0040 B0061 B0062 B0065 B0076 B0085', 'prospective_quotient_and_negative_certificates',
       'Primitive roots, subgroup conjugacy, inversion and canonical unoriented IDs require their own complete decisions and population reconciliation. Positive existential relations admit witnesses; bounded failure to find a witness does not certify a negative. Present project bindings do not supply a complete solver; that is not a corpus-wide nonexistence theorem. Ledgers and stop outcomes are unexecuted.', [BRIEF, BUNDLE, LOCK])
assign('B0046 B0058 B0059', 'conditional_gate_M_law',
       'Invariance under conjugacy and inversion is the declared descent law. If M(gamma inverse)=conjugate(M(gamma)) differs from M(gamma), the same unoriented owner would have two outputs, so that candidate fails this codomain law. Split obstruction takes specified priority and records formal refutation; no other mechanism or broader codomain is refuted. These are explicit conditional requirements, not an implemented gate.', [BUNDLE])
assign('B0048 B0089', 'bounded_corpus_not_historical_recount',
       'The fixed corpus has 22 rows and 13+9 source-use states. Current prose deliberately withholds historical-screening/replay counts and original-session reconstruction. A missing binding is not evidence that historical rows never existed. No new recount or original-query reconstruction is performed in this review.', [MATRIX, LOCK, BUNDLE])
assign('B0049', 'narrowed_traceability_and_no_review_independence',
       'The held traceability describes the project synthesis, but it does not by itself prove a complete source-effect/report/review/adjudication sequence. Current prose explicitly withholds that history and any same-family review independence. The no-science claim is bounded to this composition and the locked placeholder science trees.', [TRACE, LOCK, BUNDLE])
assign('B0050 B0054 B0075 B0090 B0091', 'bounded_source_partition_and_transfer_ceiling',
       'Direct inspection of the frozen finalization and matrix gives 22 contexts: 13 retained 20-word excerpts with exact abstract locators and nine metadata-only unavailability rows. The present contexts retain that split. This validates narrow source-use bookkeeping, not project theorem hypotheses, full-text coverage, novelty, retraction/conflict clearance, or scientific/Route results.', [FINAL, MATRIX, LOCK])
assign('B0051', 'correction_binding_and_status_limit',
       'S06/S07 are explicitly linked as original article and correction; current fresh publisher correction text confirms the relationship. The arXiv representation S09 remains the cited preprint record, but fresh v3 comments also report journal acceptance, which must not be silently treated as unpublished/unaccepted. No full per-source retraction or conflict clearance is established.', [FINAL, MATRIX, rel(N/'stage4_5_round3_web_captures/p29r3A3.json'), rel(N/'stage4_5_round3_web_captures/p29r3A9.json')])
assign('B0053', 'historical_registered_intent_not_current_completeness',
       'Each of the eight historical Phase6 entries has planned_refs and negative_constraints. That supports the sentence about registered intent, not completeness of the current sentence registry. The remaining text states the no-unassigned-source/no-stronger-theorem/no-prospective-as-executed conversion rule, rather than proving every past draft obeyed it.', [INTENT, BUNDLE])
assign('B0055 B0082 B0092', 'unexecuted_project_state',
       'The current manuscript does not report scientific owner/quotient/mechanism/performance results; the input lock lists only .gitkeep files in P29 code, experiments and results, and the historical intake declares no experiments. Source-audit/build receipts are not scientific replay receipts. This is not an audit of all unrecorded external activity.', [LOCK, PASSPORT])
assign('B0064', 'prospective_object_schema',
       'Projective-matrix bytes, subgroup/loxodromic evidence, dependency hashes, serializer versions and expected positive/negative/malformed fixtures are requirements for a future ObjectLedger. A requirement that the validator reject malformed input is not a report that such a validator or fixture was executed.', [BUNDLE])
assign('B0066', 'prospective_mechanism_schema',
       'The proposed registry binds formula and conventions to a hash. Literal type, invariance and declared laws are separate acceptance predicates, with predeclared inert/split/nonprime/malformed/timeout cases. Failures are record-local and no mechanism execution is asserted.', [BUNDLE])
assign('B0067 B0072', 'conditional_performance_estimand',
       'The proposed statistic concerns predeclared baseline-collision pairs of certified holdout owners with distinct valid outputs of one frozen admissible mechanism. Incomplete quotient/raw rows or changed formula/control bytes are differently typed inputs. No S_H value is supplied; even a later positive finite score would not prove a global orbit-to-prime theorem.', [BUNDLE, BRIEF])
assign('B0068', 'prospective_independent_replay_contract',
       'Hash/version/fixture/disposition/first-mismatch receipts and non-reuse of producer transformation logic are explicitly future verifier requirements. Agreement would establish only the registered finite procedure, not general mathematical truth. No verifier, fixture execution or receipt is claimed.', [BUNDLE, LOCK])
assign('B0073 B0113', 'prospective_control_scope',
       'A bijective relabeling preserving equality classes preserves an equality-based separation predicate. Inversion pairs test representative independence, not the correct split branch. Changing to a composite or broader codomain changes type and cannot count as the frozen primary estimand. Controls and their typed stops remain unobserved.', [BUNDLE])
assign('B0080 B0107', 'narrowed_materials_availability',
       'Current prose limits material claims to the named Round3 source-support carriers and withholds earlier public availability, historical file identities/recounts and original-session absence claims. No archive or scientific-package availability is inferred from the older provenance.', [LOCK, FINAL, MATRIX, BUNDLE])
assign('B0114 B0115', 'source_carrier_identity_and_partition',
       'The exact source-finalization, matrix and validation receipt descriptors occur in the controlling lock. Their retained matrix contains 22 rows with 13 finalized and nine metadata-only uses. Each 20-word excerpt is only contextual: none of these excerpts supplies the complete project-specific owner law or quotient. The deterministic receipt does not prove mathematical applicability.', [LOCK, FINAL, MATRIX, rel(N/'stage4_prime_source_finalization_round3_validation.json')])
assign('B0084', 'prospective_synthetic_oracle',
       'For one synthetic unoriented token, assigning distinct branch tokens to inverse representatives violates the declared inversion invariance. The two-element unordered pair baseline can avoid that fixture-local branch mismatch but changes codomain. This is an intended test oracle, not an executed fixture, observed obstruction, or claim about every codomain.', [BUNDLE])
assign('B0087 B0100 B0101', 'bounded_contribution_and_route_status',
       'The contribution is project-specific prospective certificate architecture. The lock preserves formal tuple UNASSIGNED, positive arithmetic A2=0, and Route B uninvoked. No field-general novelty, implementation, scientific computation, performance or Route advancement follows from source/citation maintenance. This is a scope check, not a fresh Route assessment.', [BRIEF, LOCK, BUNDLE])
assign('B0093 B0094 B0096 B0097', 'future_work_order_not_executed_result',
       'These are proposed next-step and reporting rules: passage/hypothesis mapping before implementation evaluation, and sealed gates before output access. Smallest is read as a suggested bounded next task, not a proved globally minimal research strategy. Partial future progress would need its own authority and evidence; candidate failure remains distinct from universal nonexistence.', [BRIEF, BUNDLE])
assign('B0103 B0109', 'human_identification_not_personal_verification',
       'The latest passport seed literally names Liang Wang in historical human-oversight narrative entries, while the current manuscript expressly withholds role-by-role accountability, complete gate/adjudication history and personal full-text/source-passage verification. Narrative naming is not a typed verified-identity or contribution attestation. Stage2.5 completion and prior integrity failure are historical procedural states, not current audit success.', [PASSPORT, LOCK, BUNDLE])
assign('B0104 B0105', 'author_declaration_not_independent_financial_audit',
       'Funding/competing-interest content is an author declaration in the manuscript. The permitted evidence does not independently establish funding or personal conflicts; no clean external financial/conflict screen is implied.', [LOCK])
assign('B0106', 'nonhuman_mathematical_study_scope',
       'The declared intake is no experiments and the project concerns mathematical objects, published sources and workflow records. No human/animal study or participant dataset is reported. This supports non-applicability on the described scope, not an institutional ethics exemption determination.', [BRIEF, LOCK, PASSPORT])
assign('B0108', 'AI_disclosure_with_unknown_activity_ledger',
       'AI assistance is disclosed, but the current clause deliberately withholds complete session/backend/date/task history. Same-family procedural roles do not remove correlated-error risk or supply independent validation. No AI scientific result or AI authorship is credited.', [LOCK, BUNDLE])

finalization = json.loads((N/'stage4_prime_source_finalization_round3.json').read_text())
source_rows = {row['block_id']: (i, row) for i, row in enumerate(finalization['rows'])}
fresh = {
 'P29-S01': ('p29r3B1.json','response',0,'L16'),
 'P29-S02': ('p29r3A9.json','response',3,'L16-L18'),
 'P29-S03': ('p29r3B1.json','response',1,'L16-L17'),
 'P29-S08': ('p29r3B2.json','response',0,'L60'),
 'P29-S06': ('p29r3B2.json','response',2,'L16'),
 'P29-S07': ('p29r3A3.json','response',1,'Abstract and original-article reference'),
 'P29-S09': ('p29r3A9.json','response',4,'L15-L18'),
 'P29-S10': ('p29r3B2.json','response',3,'L17'),
 'P29-S13': ('p29r3B3.json','raw_response',4,'Primary World Scientific abstract, including RAM model caveat'),
 'P29-S14': ('p29r3B2.json','response',4,'L16-L17'),
 'P29-S20': ('p29r3A9.json','response',1,'L16-L17'),
 'P29-S21': ('p29r3A8.json','response',0,'Primary journal abstract'),
 'P29-S22': ('p29r3A7.json','response',2,'Primary journal identity; retained historical 20-word excerpt supplies narrow input-only passage')
}
source_limits = {
 'P29-S01': 'The actual abstract identifies Picard PSL(2,Z[i]) and H3; no owner-law construction is transferred.',
 'P29-S02': 'The first20 words identify the Picard quotient and prime-geodesic question, not any project mechanism.',
 'P29-S03': 'The excerpt reports a Gaussian-integer Bykovskii generalization and asymptotic prime-geodesic formula; no exponent or owner-assignment theorem is imported.',
 'P29-S08': 'The original abstract explicitly concerns compact hyperbolic three-manifolds and length/holonomy intervals; no noncompact level-(3) solver follows.',
 'P29-S06': 'The old source reports an error-exponent improvement; affected use requires S07 correction. The manuscript reports what the old excerpt says without importing the uncorrected result.',
 'P29-S07': 'The original publisher abstract states the correction and its original article reference. It is not mechanism evidence or general retraction clearance.',
 'P29-S09': 'The first20 words report a Picard error-term improvement. Current v3 changes title and reports acceptance in Sci. China Math; the cited arXiv representation and journal acceptance must remain distinct.',
 'P29-S10': 'The retained fragment stops before the algorithm output. Fuller original abstract gives a fundamental domain and finite presentation, but the manuscript expressly does not transfer that output or a project quotient theorem.',
 'P29-S13': 'The abstract opening states linear-time word-hyperbolic conjugacy. Fuller primary text assumes a standard RAM model; the manuscript claims only what the opening sentence states and no project certificate or complexity result.',
 'P29-S14': 'The source handles rational matrices with integral conjugators. Existence in ambient GL(n,Z) does not guarantee a conjugator in the frozen projective congruence subgroup.',
 'P29-S20': 'The primary abstract is a survey of algorithmic algebraic number theory; no class-to-ideal law is transferred.',
 'P29-S21': 'The primary abstract describes practical computational number-theory algorithms with class-field applications; it does not justify choosing one split branch for the project.',
 'P29-S22': 'The 20-word retained excerpt stops after giving an integral ideal in a number field as input. The manuscript correctly withholds the algorithm output and any group-element maximal-root transfer.'
}
source_tuples = {}
for bid, (idx, row) in source_rows.items():
    sid = row['source_id']
    R[bid] = {'basis_kind': 'bounded_source_context' if row.get('support_excerpt') else 'metadata_only_context',
              'reason': source_limits.get(sid, 'The current source occurrence explicitly retains metadata only and makes no substantive passage attribution. A missing finalized locator is a historical bounded result, not nonexistence of a passage or algorithm.'),
              'carriers': [FINAL, MATRIX]}
    tup = {'ref_slug': sid, 'anchor': row['exact_passage_locator'],
           'writer_anchor_status': 'EXPLICIT_PROSE_LOCATOR' if row['exact_passage_locator'] else 'ANCHOR_NONE',
           'held_source_path': FINAL, 'json_pointer': '/rows/'+str(idx)+'/support_excerpt',
           'excerpt': row.get('support_excerpt'), 'support_excerpt_sha256': row.get('support_excerpt_sha256'),
           'source_kind': row['source_authority'],
           'observed_capture_time': row['retrieval_trace'].get('retrieved_at_utc'),
           'original_retrieval_trace_pointer': '/rows/'+str(idx)+'/retrieval_trace',
           'historical_status_not_current_search_denominator': True,
           'full_source_body_local_availability': 'Not inferred from retrieval hashes; held excerpts and current raw browser surfaces only.'}
    if sid in fresh:
        name, key, segment, locator = fresh[sid]
        path = N/'stage4_5_round3_web_captures'/name
        cap = json.loads(path.read_text())
        tup['fresh_current_round_corroboration'] = {
            'held_source_path': rel(path), 'json_pointer': '/'+key,
            'delimiter_separated_segment_zero_based': segment,
            'surface_locator': locator,
            'observed_capture_time': cap.get('retrieved_at_utc') or cap.get('stamp',{}).get('current_time'),
            'interpretation': source_limits[sid]}
    if not row.get('support_excerpt'):
        tup['json_pointer'] = '/rows/'+str(idx)+'/retrieval_trace'
        tup['source_kind'] = 'bounded_metadata_and_finalization_record_not_original_passage'
    source_tuples[sid] = tup

findings = [{
 'finding_id': 'P29-R3-F01-S19-UNSUPPORTED-NEGATIVE', 'block_id': 'B0042',
 'trigger': 'The algorithms do not select an ideal owner.', 'severity': 'SERIOUS',
 'verdict': 'UNVERIFIABLE', 'class': 'SOURCE_WIDE_NEGATIVE_FROM_METADATA_ONLY',
 'reason': 'The S19 paragraph declares metadata-only use and no substantive passage attribution, but its last sentence predicates a negative of the algorithms themselves. Neither the metadata record nor the absence of a finalized passage establishes what all relevant algorithms in the book do not select. It should not be silently read as the narrower project-use statement that no owner law is imported.',
 'required_disposition': 'Root must adjudicate this candidate and obtain a specific author disposition at the mandatory checkpoint if retained; no automatic manuscript correction.'
}]

# All115 blocks are accounted for. Pure TeX setup/boundaries and keywords are not
# factual claims. Headings with a factual predicate receive a standalone entry.
excluded = {'B0001':'TeX setup only','B0003':'document opening only',
            'B0005':'keyword list only','B0007':'keyword list and language closing only',
            'B0110':'bibliography commands only','B0111':'document closing only'}
heading_claims = {'B0019','B0032','B0041','B0047','B0056'}
metadata_block = 'B0002'
for bid, block in bs.items():
    if bid in R or bid in excluded or bid == metadata_block:
        continue
    if bid in heading_claims:
        R[bid] = {'basis_kind':'heading_scoped_by_body',
                  'reason':'Heading is interpreted under the explicit bounded/prospective body. Object/ideal-arithmetic types alone do not give an owner law; review-adjudicated refers to recorded framing decisions, not independent review or complete personal accountability. It does not broaden the adjacent source uses.',
                  'carriers':[LOCK,BUNDLE]}
    else:
        excluded[bid] = 'section/subsection navigation heading only; no additional factual predicate'
R[metadata_block] = {'basis_kind':'author_supplied_title_and_contact_metadata',
                     'reason':'Title/date/author affiliation/contact are manuscript metadata, not an independent identity or employment audit. Passport narrative corroborates the named author only; affiliation/contact/date attribution is not separately verified by permitted evidence.',
                     'carriers':[PASSPORT,LOCK]}

claims = []
reviews = []
def emit(bid, start, end, role):
    value = draft[start:end]
    left = len(value)-len(value.lstrip())
    right = len(value.rstrip())
    start += left
    end = start+right-left
    if end <= start:
        return
    value = draft[start:end]
    if len(value) < 3:
        return
    if any(c['draft_span'] == span(start,end) for c in claims):
        return
    rr = R[bid]
    sid = []
    anchors = []
    if bid in source_rows:
        _, src = source_rows[bid]
        sid = [src['source_id']]
        if src['exact_passage_locator']:
            anchors = [src['exact_passage_locator']]
    kinds = ['other_factual']
    if re.search(r'\d|\b(?:one|two|three|four|five|eight|nine|thirteen|twenty.two)\b|二十二|十三|九項',value,re.I):
        kinds.append('quantitative')
    if re.search(r'\b(?:must|only|no|not|requires|cannot|complete|all|every)\b',value,re.I):
        kinds.append('categorical')
    cid = 'P29-R3-'+bid+'-'+str(sum(c['paper_section']==bid for c in claims)+1).zfill(3)
    normalized = re.sub(r'\s+',' ',value)
    matched = [f for f in findings if f['block_id']==bid and f['trigger'] in normalized]
    verdict = matched[0]['verdict'] if matched else 'VERIFIED'
    reason = matched[0]['reason'] if matched else rr['reason']
    if bid in ['B0104','B0105']:
        verdict = 'UNVERIFIABLE'
    if bid == 'B0002' and role == 'author_contact_metadata':
        verdict = 'UNVERIFIABLE'
    claim = {'claim_id':cid, 'claim_text':value, 'draft_span':span(start,end),
             'claim_kinds':list(dict.fromkeys(kinds)), 'ref_slugs':sid,
             'writer_anchors':anchors, 'paper_section':bid, 'selection_tier':'ALL'}
    claims.append(claim)
    review = {'claim_id':cid, 'block_id':bid, 'extraction_role':role,
              'claim_text':value, 'draft_span':span(start,end),
              'verdict':verdict, 'basis_kind':rr['basis_kind'], 'reason':reason,
              'finding_ids':[f['finding_id'] for f in matched],
              'project_evidence_carriers':rr['carriers'],
              'source_tuples':[source_tuples[x] for x in sid],
              'writer_anchor_rule':'Explicit prose locator is preserved; generic comment anchor=recorded_exact_locator is not invented as a theorem/page locator. Metadata-only rows retain no anchor.',
              'scientific_completion_inferred':False}
    if bid in source_rows:
        if 'Round-3' in value or 'finalization pass' in value:
            review['component_evidence_kind'] = 'project_source_finalization_record'
            review['reason'] = ('The retained source-finalization row records this exact historical bounded disposition/locator and excerpt digest. Current frozen row identity is evidence of the local record; it is not full-source theorem verification. '+(reason if matched else ''))
        elif any(t in value for t in ['No broader','not be transferred','No transfer','not transferred','No project','No direct','not used','not treated','No serialization','No instantiated','remain separate','No class-to-ideal','not evidence','do not justify','not inferred']):
            review['component_evidence_kind'] = 'explicit_project_transfer_prohibition'
        else:
            review['component_evidence_kind'] = 'original_bounded_statement' if anchors else 'metadata_only_statement'
    if bid in ['B0103','B0109']:
        review['passport_naming_pointers'] = [
            '/compliance_history/0/raise/principle_evidence/human_oversight/0',
            '/compliance_history/1/raise/principle_evidence/human_oversight/0']
    reviews.append(review)

for bid, block in bs.items():
    if bid not in R:
        continue
    t = block['text']
    if bid == 'B0002':
        for m in re.finditer(r'\\title\{([^\n]+)\}|\\date\{([^\n]+)\}',t):
            emit(bid,block['start']+m.start(),block['start']+m.end(),'title_or_date_metadata')
        start = t.index('\\author{')
        end = t.index('\n\\date{')
        emit(bid,block['start']+start,block['start']+end,'author_contact_metadata')
        continue
    if bid in heading_claims:
        emit(bid,block['start'],block['start']+len(t),'claim_bearing_heading')
        continue
    valid = []
    for lm in re.finditer(r'[^\n]+(?:\n|\Z)',t):
        line = lm.group().strip()
        if not line or line.startswith(('%','\\begin{','\\end{','\\section','\\subsection','\\begingroup','\\par\\endgroup')):
            continue
        if re.fullmatch(r'\\citep\{[^}]+\}\.',line):
            continue
        a,b = lm.start(),lm.end()
        if line.startswith('\\paragraph{'):
            a = t.index('}',a)+1
        # Layout closers are not part of the last prose sentence.
        closer = t.find('\\par\\endgroup',a,b)
        if closer >= 0:
            b = closer
        if a < b:
            valid.append((a,b))
    chunks = []
    for a,b in valid:
        if chunks and a == chunks[-1][1]:
            chunks[-1] = (chunks[-1][0],b)
        else:
            chunks.append((a,b))
    for a,b in chunks:
        piece = t[a:b]
        # English sentence punctuation requires following whitespace; Chinese
        # full stops split without whitespace. Decimal periods and TeX contents
        # are retained. The manuscript has no abbreviation needing a split.
        boundaries = list(re.finditer(r'(?<=[.!?])\s+(?=[A-Z\\])|(?<=[。！？])\s*',piece))
        at = 0
        for cut in boundaries+[None]:
            until = cut.start() if cut else len(piece)
            emit(bid,block['start']+a+at,block['start']+a+until,'semantic_full_sentence')
            if cut:
                at = cut.end()

# Required finite lexical candidates use the official helper's exact original
# offsets. Importing these two pure helpers does not build or validate anything.
coverage = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/scripts/claim_registry_coverage.py')
spec = importlib.util.spec_from_file_location('p29_read_only_lexical_helpers',coverage)
cov = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cov)
lexical = []
for sentence in cov._sentences(draft):
    if not cov._candidate_kinds(sentence['text']):
        continue
    bid = next((k for k,b in bs.items() if b['start'] <= sentence['start_char'] < b['start']+len(b['text'])),None)
    if bid not in R:
        R[bid] = {'basis_kind':'finite_lexical_supplement_not_semantic_prose',
                  'reason':'A finite lexical trigger in metadata/layout is registered exactly so coverage does not silently omit it. It does not become independent scientific evidence.', 'carriers':[LOCK]}
        excluded.pop(bid,None)
    before = len(claims)
    emit(bid,sentence['start_char'],sentence['end_char'],'finite_lexical_candidate_exact_span_supplement')
    lexical.append({'block_id':bid,'draft_span':span(sentence['start_char'],sentence['end_char']),
                    'text':sentence['text'],'already_exactly_registered':before==len(claims)})

registry = {'schema_version':'claim-registry/1.0','draft_raw_sha256':draft_hash,'claims':claims}
block_inventory = []
for bid,b in bs.items():
    selected = [c['claim_id'] for c in claims if c['paper_section']==bid]
    block_inventory.append({'block_id':bid, 'raw_span':span(b['start'],b['start']+len(b['text'])),
                            'disposition':'SELECTED' if selected else 'EXCLUDED_NONCLAIM',
                            'claim_ids':selected, 'excluded_reason':excluded.get(bid)})
review = {
 'schema_version':'p29-current-sentence-semantic-review/1.0', 'paper_id':'P29',
 'current_draft':desc(DRAFT), 'selection_tier':'ALL',
 'scope':'All115 current blocks independently read and inventoried; prose sentences, claim-bearing headings, title/contact declarations and every finite lexical exact candidate selected as specified below. No historical eight-claim denominator is inherited.',
 'method':'Manual current-draft/source/authority reading with exact UTF8 byte-span indexing; descriptive per-sentence judgments distinguish original passage statements, local record claims, prospective contracts, mathematical conditionals and author declarations. No official validator, replay, build, new source search or protected input change.',
 'counts':{'current_blocks':len(bs),'selected_blocks':sum(bool(x['claim_ids']) for x in block_inventory),
           'excluded_nonclaim_blocks':sum(not x['claim_ids'] for x in block_inventory),
           'claims':len(claims),'semantic_full_sentences':sum(x['extraction_role']=='semantic_full_sentence' for x in reviews),
           'finite_lexical_candidates':len(lexical),
           'finite_lexical_added_claims':sum(x['extraction_role']=='finite_lexical_candidate_exact_span_supplement' for x in reviews),
           'citation_contexts':22,'bounded_contextual_locators':13,'metadata_only_contexts':9},
 'coverage_completeness_limit':'Manual full-surface extraction is documented, not mathematically proven semantic completeness. Pure lexical coverage has a narrow detector and cannot establish claim truth.',
 'source_tuple_limit':'Historical retained excerpts are held original-text fragments with source-finalization trace; current raw browser captures corroborate specified passages. Retrieval digests alone do not mean full source bodies are available. No metadata-only row is silently promoted by a fresh metadata hit.',
 'verdicts_not_scientific_results':True,
 'source_carriers':[desc(N/'stage4_prime_source_finalization_round3.json'),desc(N/'stage4_prime_claim_passage_matrix_round3.json'),desc(N/'stage4_5_round2_material_passport.json')],
 'findings':findings,
 'advisories':[
   {'id':'P29-R3-A01-S09-VERSION-STATUS','reason':'Fresh arXiv v3 comments report changed title and acceptance in Sci. China Math. Retained preprint representation is not evidence of no journal acceptance; root owns full A/status disposition. No bibliography mutation authorized.'},
   {'id':'P29-R3-A02-PASSPORT-NARRATIVE','reason':'Liang Wang naming is literal in passport compliance-history narrative, not a typed verified identity/CRediT/approval attestation. Current B0103/B0109 expressly withhold stronger claims.'},
   {'id':'P29-R3-A03-GENERATED-CARRIER-BLOCKS','reason':'Current B0114/B0115 were created when R3 replacement operations23/24 split added source-carrier paragraphs into fresh block IDs. Their full added text was read in E6 and is separately indexed here; neither is later replaced. Root E6 JSON contains full patch new_text, while its current_block field names the original replacement target.'}
 ],
 'block_inventory':block_inventory,'lexical_candidates':lexical,'sentence_reviews':reviews,
 'E6_handoff':{'path':rel(N/'stage4_5_round3_resume_p29_E6_semantic.json'),
               'sha256':'843df6bb7defd7be9a1c735f2426d3d2cfc488f4fa95a0a2f3ae7e32de624ca4',
               'operation_count':100,'historical_corrected_drift':1,'persistent_drift':0},
 'mandatory_checkpoint':'Root adjudicates the specific S19 source-negative candidate and other integrity findings; this handoff authorizes no automatic correction or stage advancement.'
}
if sys.argv[1:] == ['registry']:
    print(json.dumps(registry,ensure_ascii=False,indent=2))
elif sys.argv[1:] == ['review']:
    print(json.dumps(review,ensure_ascii=False,indent=2))
elif sys.argv[1:] == ['summary']:
    print(json.dumps({'counts':review['counts'],'verdict_counts':{k:sum(x['verdict']==k for x in reviews) for k in sorted({x['verdict'] for x in reviews})},'findings':findings,'excluded':[x for x in block_inventory if not x['claim_ids']]},ensure_ascii=False,indent=2))
elif len(sys.argv)==4 and sys.argv[1]=='slice':
    start,end = map(int,sys.argv[2:])
    print(json.dumps({'registry_claims':claims[start:end],'sentence_reviews':reviews[start:end]},ensure_ascii=False))
elif sys.argv[1:] == ['header']:
    print(json.dumps({'registry':{k:v for k,v in registry.items() if k!='claims'},'review':{k:v for k,v in review.items() if k!='sentence_reviews'}},ensure_ascii=False))
else:
    raise SystemExit('Usage: resume_p29_claim_assemble.py registry|review|summary|header|slice START END')
