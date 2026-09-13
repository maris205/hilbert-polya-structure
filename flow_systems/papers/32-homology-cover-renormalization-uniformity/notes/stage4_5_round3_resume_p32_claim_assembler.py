"""Read-only indexing of the main reviewer's current P32 semantic judgments.

No official validator, evidence-row builder, scientific execution, or file write.
The per-block bases below are human-readable model-mediated judgments after the
entire current draft, relevant source fragments and revision chain were read.
Sentence extraction only supplies exact raw UTF-8 locators.
"""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path('/root/autodl-tmp/flow_systems')
P = ROOT/'papers/32-homology-cover-renormalization-uniformity'
N = P/'notes'
DRAFT = N/'stage4_prime_revision_round4.tex'
raw = DRAFT.read_bytes()
draft = raw.decode('utf-8')
bs = {m[1]: {'text':m[2].rstrip(), 'start':m.start(2)} for m in re.finditer(r'<!--block:(B\d+)-->\n(.*?)(?=<!--block:|\Z)',draft,re.S)}
byte_offsets = [0]
for char in draft:
    byte_offsets.append(byte_offsets[-1]+len(char.encode()))
def span(a,b):
    return {'start_byte':byte_offsets[a], 'end_byte':byte_offsets[b]}
def relative(path):
    return str(path.relative_to(ROOT))
LOCK = 'BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json'
BRIEF = relative(N/'stage1_prestart_brief.md')
BUNDLE = relative(N/'stage4_prime_revision_evidence_bundle_round4.json')
SOURCE = relative(N/'stage4_prime_source_finalization_round3.json')
MATRIX = relative(N/'stage4_prime_claim_passage_matrix_round4.json')
READER = relative(N/'stage4_prime_reader_artifact_manifest_round2.json')
R = {}
def assign(ids,kind,reason,carriers):
    for bid in ids.split():
        R[bid]={'basis_kind':kind,'reason':reason,'carriers':carriers}

assign('B0003','declared_identity_metadata','Title and named author/affiliation/date are retained configuration metadata, not independently certified employment or act-by-act contribution.',[relative(N/'stage2_paper_configuration.md')])
assign('B0006 B0007','bounded_abstract','The pure genus-two tower, full oriented primitive-owner scope and fixed 1/N and 1/N^3 normalizations match the frozen input. Scalar factors, owner binding and analytic limits remain unexecuted targets. Eighteen held inherited excerpts/eight unavailable/four CW metadata-only are distinct; the English bounded-CW phrase is read with the explicit Chinese and B0018 limitations. Formal-unresolved wording means project application under B0131, not denial that a candidate carrier is defined.',[BRIEF,MATRIX,BUNDLE,LOCK])
assign('B0011 B0012 B0013 B0014 B0019','frozen_object_and_scope','The marked genus-two relation, unit-speed flow, pure homology kernel, oriented primitive owners and separate inverses are fixed definitions. A restricted stratum/panel is a strict subset of the universal target and does not logically certify all owners. Residual and pure towers are not identified.',[BRIEF,LOCK])
assign('B0016','research_question','This is an explicit conditional research question, not a claim that its factors or obstruction have been established.',[BRIEF])
assign('B0017 B0021 B0118','dependency_priority','Shortest/earlier is interpreted through B0017 as fewer declared downstream obligations in this program, not optimal runtime, global minimality or superiority over all alternative proof strategies. The early scalar comparison depends on fewer stated gates than a global compact-uniform product.',[BUNDLE])
assign('B0018 B0132','qualified_comparison_hypotheses','B0018 explicitly scopes every role, absence, overlap, closest label and concluding joint-chain phrase in the following table as a provisional comparison hypothesis. All four CW rows lack bound support excerpts; their metadata identity is verified, their substantive contribution/ranking remains unverified and is not a transferred premise. Historical matrix wording is not silently upgraded.',[MATRIX,SOURCE,relative(N/'stage4_prime_closest_work_comparison_matrix_round2.json')])
assign('B0020','prospective_gate_definitions','Owner, local-factor and global-formal/analytic gates are normative dependencies. Neither the present manuscript nor a source title is an execution certificate.',[BRIEF,BUNDLE])
assign('B0024 B0028 B0032 B0033 B0036 B0039','bounded_source_disposition','Each source-specific statement is checked against its exact held fragment or explicit unavailability. The current prose limits fragment conclusions: abstract openings and contents/heading tokens are not full theorems, and no project owner/factor/equality/tail/Route transfer follows. Bibliographic identity is checked separately in fresh Phase A.',[SOURCE,MATRIX])
assign('B0025 B0026','unbound_owner_interface','No project-local binding to SG2OwnerCanonical-v1 is present in the retained evidence. List decision alone does not certify exhaustion of all earlier eligible owners. Equality, oriented conjugacy, maximal roots and deterministic serialization/prefix completeness are prospective obligations, not impossibility claims about the literature.',[BRIEF,MATRIX])
assign('B0029 B0030','cover_transfer_boundary','Deck/splitting/homology roles are possible ingredients, while specific owner order/lift counts/time and logarithmic factors require the project derivation. The group-level cover description is independently corroborated by primary cover/homology records but establishes no normalized P32 factor.',[SOURCE,MATRIX])
assign('B0034','source_absence_boundary','Narrow abstract/contents fragments do not certify source-wide absences. The transfer restriction is valid as no accepted P32 proof here, but wording about what the works do not establish should not be read as a verified exhaustive negative about their contents.',[SOURCE,MATRIX])
assign('B0037','analytic_requirement_not_result','An asymptotic at a nearby system does not alone imply an absolute logarithmic-summand majorant uniform over every frozen compact and every required interchange. The paragraph states the stronger project target, not a newly proved theorem.',[BRIEF,BUNDLE])
assign('B0040 B0041','formal_truth_conditions','A fixed coefficient comparison requires specified coefficient ring, support, topology, maps and allowed specialization. Similar source vocabulary does not define a project object. B0131 later distinguishes the supplied formal carrier from its unproved factor realization.',[SOURCE,BUNDLE])
assign('B0044 B0133 B0109','screening_accounting','Historical 51-12=39 and 39-13=26 are frozen aggregate records, not recovered original exclusion decisions. The separate dated replay has 51 manifestations=19 retained+31 out-of-scope+1 duplicate; actual JSON/TSV scalar fields match row-for-row. Replayed rows do not replace the original corpus or prove completeness of retrieval.',[relative(N/'stage1_phase2_source_inventory.tsv'),relative(N/'stage4_prime_literature_replay_round2.raw.json'),relative(N/'stage4_prime_literature_screening_ledger_round2.json'),relative(N/'stage4_prime_literature_screening_ledger_round2.tsv')])
assign('B0045 B0046','closed_corpus_coding','The source/literature matrices contain the 26 frozen IDs and theme/admitted/excluded-role coding. These are project judgments, not votes that establish a theorem or independent experiments.',[relative(N/'stage1_phase3_literature_matrix.tsv'),MATRIX])
assign('B0047 B0139','local_source_inventory','The retained R3 source-finalization projection and validation receipt are historical bounded carriers distinct from the current R4 context matrix. Eighteen exact snippets/eight unavailable/four retained provisional CW labels count30; current B0018 expressly withholds all CW substantive support. Inventory hashes/fields do not prove theorem applicability.',[SOURCE,MATRIX,relative(N/'stage4_prime_claim_passage_matrix_round3.json')])
assign('B0049 B0050','dated_method_provenance','The historical Phase6 manifest and revision bundle support staged source synthesis and dated prose work. No-new-retrieval wording is scoped to the original article-writing phase, not all later rounds. Later source finalization and audit activity is disclosed separately; scientific work remains unexecuted.',[relative(N/'stage1_phase6_claim_intent_manifest.json'),BUNDLE,LOCK])
assign('B0053 B0054 B0055 B0056 B0057 B0058 B0059 B0061 B0062','candidate_factor_contract','Displayed positive/zero factors, deck order N/q, component count N^3q and normalization are explicitly later derivation targets. The time rescaling changes the exponential argument; logarithmic normalization changes the exponent. Neither formula is promoted to a physically derived owner factor.',[BRIEF,BUNDLE])
assign('B0060','self_contained_scalar_lemma','For x=exp(-s ell/m) in (0,1), m>=2: (1-x)^m < 1-x < 1-x^m, hence inverses give (1-x)^(-m)>(1-x^m)^(-1). The proof is elementary on the stated real positive domain. Its use for project factors is expressly conditional on a separate valid derivation.',[relative(DRAFT)])
assign('B0064 B0065 B0066','conditional_higher_content','For fixed positive integer d, d divides k! once k>=d. Then gcd(k!,d)=d, so the candidate factor specializes to the displayed scalar expression. The scalar lemma applies only after a legitimate project factor derivation; there is no executed owner obstruction.',[relative(DRAFT),BRIEF])
assign('B0067 B0068 B0069','conditional_falsification_logic','A correctly derived counterexample for one eligible universally quantified owner refutes the universal endpoint; one surviving test cannot prove all owners or an infinite product. Target-blind selection and non-execution limits are explicit.',[relative(DRAFT),BRIEF])
assign('B0071 B0072 B0073 B0074','conditional_zero_content','Zero content has a separate proposed order/count/time branch; none is derived from a performed cover computation. Conditional on that branch, the m=N scalar lemma gives the strict inequality at N>=2. Derivation-failed, equality, and inequality outcomes remain distinct.',[relative(DRAFT),BRIEF])
assign('B0076 B0077 B0078 B0079','restricted_stratum_not_universal_recovery','d=1 gives gcd(N,1)=1 within the candidate expression. A theorem on that subproduct would not imply full-owner recovery or repair a distinct residual tower. Required owner enumeration, factor derivation and analytic limits remain open.',[relative(DRAFT),BRIEF])
assign('B0081 B0131','inverse_limit_definition','The explicitly supplied finite-variable/truncated rings and compatible projections define an inverse-limit carrier. B0131 calls carrier objects defined but project factor/analytic realization unproved; broad unresolved wording elsewhere is explicitly limited to the latter. No external source is needed to check this formal definition.',[relative(DRAFT)])
assign('B0082','localization_injection','Each 1-u_g^r has constant term1, so is invertible in every finite-degree completion. A nonzero rational numerator has a first nonzero finite degree, proving injection into the product-compatible inverse limit; no actual owner factor is asserted to lie there.',[relative(DRAFT)])
assign('B0134','separate_hahn_fibers','Well-ordered nonnegative rational supports give coefficientwise well-defined Hahn-series multiplication; valuation topology separates coefficients. The displayed zero-content object is a product of individual owner fibers, not an unrestricted multiowner Hahn algebra. CP-P32-004 is explicitly not a premise of this definition.',[relative(DRAFT)])
assign('B0083 B0135','formal_compatibility_proof','Variable deletion preserves total degree and truncations compose. The inverse limit is a closed subset of complete discrete quotient products, hence Hausdorff and complete. Compatible rational localization embeds by its first nonzero coefficient. Singleton maps have the stated domains; their joint injectivity is not claimed.',[relative(DRAFT)])
assign('B0084','one_way_projection','Equality implies equality under each well-defined projection, so one coordinate inequality refutes joint equality. Conversely singleton coordinates miss mixed monomials (u_g u_h), so no joint faithfulness follows.',[relative(DRAFT)])
assign('B0086 B0087 B0088 B0089','prospective_compacts_and_schedules','K(delta,T,R), factorial and neighboring schedules, and owner exhaustion are explicit frozen domains and future indices. No compact-uniform convergence is claimed merely from choosing them.',[BRIEF,BUNDLE])
assign('B0090 B0136 B0091','five_analytic_obligations','All AN1–AN5 rows remain unproved. With q_N=1 the candidate log summand has no N dependence; this does not supply a factor derivation or summable owner-tail bound. The stated M_j(K) controls the pointwise candidate on Re(s)>=1+delta, but summability and limit interchanges remain requirements.',[relative(DRAFT),relative(N/'stage4_prime_analytic_registry_audit_round2.json')])
assign('B0092 B0116','finite_diagnostic_limit','A finite prefix through k=8 tests only future serialization/replay, not a limit. Predetermined schedules must not be shortened after observing an unfavorable content.',[BRIEF,BUNDLE])
assign('B0094','historical_eight_positions','Eight counts the enumerated synthesis/design positions, not all present semantic claims. Family-level normal-form/conjugacy/root/list candidates are tentative ingredients; no serialization or SG2 interface is source-certified.',[relative(N/'stage1_phase6_claim_intent_manifest.json'),SOURCE])
assign('B0095','formal_application_ambiguity','B0134 explicitly says CP-P32-004 is not a definition premise, while this sentence ties unresolved constructions to that checkpoint. Under B0131 only project realization remains open, but the causal wording conflates defined carrier and unproved application; a localized clarification is warranted.',[relative(DRAFT)])
assign('B0096','nonresult_conclusion','The enumerated output is synthesis and conditional design, not factor derivations, owner certificates, global limits, novelty or Route promotion.',[LOCK])
assign('B0098 B0125','reader_recoverability','All25 local files match this reader inventory;11 are historically marked public and14 local-only. This round made no successful remote byte comparison: the first exact pinned URL failed TLS before response/hash evaluation. The remote byte-identity assertion therefore has UNVERIFIABLE_ACCESS, not an invented mismatch or fresh remote PASS.',[READER,relative(N/'stage4_5_round3_resume_p32_remote_artifact_check.json')])
assign('B0137','artifact_not_archive','Notes source/matrix/validation records and downstream apply/build events are separate provenance stages. Content addressing is not permanent archival or proof of prose determinism, source faithfulness or scientific reproducibility.',[SOURCE,BUNDLE,LOCK])
assign('B0099 B0100 B0101 B0102','future_dossier_requirements','The proof-binding dossier and later population manifest are proposed requirements conditional on local derivation and certification. Smallest is dependency-scoped under B0017, not an empirically proved global optimum. No hidden producer state is accepted as a reproducibility proof.',[BRIEF,BUNDLE])
assign('B0104 B0105 B0106','discussion_of_conditional_design','The revised order may expose a local obstruction before formal/analytic work, but it does not decide outcomes. Failure to derive a factor is not an obstruction. Content-one success remains restricted and does not erase adverse owners elsewhere.',[BRIEF,BUNDLE])
assign('B0107','frozen_route_consistency','Current scoped Route state has arithmetic A0 unavailable, no assigned formal tuple/positive arithmetic A2/A3/A4, and Route B uninvoked. This is consistency with the frozen record, not a newly invoked Route assessment.',[BRIEF,LOCK])
assign('B0110','bounded_source_correction_status','S13 remains metadata-only, S06 is a preprint with no presentation transfer, and S17 is limited to the first-part continuation scope. Fresh original erratum arXiv2203.04917 confirms Section7 error and unaffected first part. No general retraction/conflict clearance is asserted.',[SOURCE,relative(N/'stage4_5_round3_resume_p32_web_A14_erratum.json')])
assign('B0111','unproved_project_application','Read with B0131, core scientific interface/factor/application/tail questions remain open even though a candidate formal carrier has been defined and formal compatibility proved. No population has been certified or coefficient/limit experiment run.',[relative(DRAFT),LOCK])
assign('B0112 B0121 B0127 B0128 B0138','secondary_provenance_boundary','Current revisions explicitly identify contributions, approvals, model-family labels and activity chronology as secondary records, not original personal acts or complete raw runtime evidence. B0121 disclaims personal full-text and exact-passage verification. R3 deletion in B0128 remains separately listed under E6 and is not silently authorized by this semantic boundary.',[BUNDLE,LOCK])
assign('B0115','future_work_only','Each listed item is a prospective dependency and requires separate authority; the list itself does not authorize this audit to execute scientific work.',[BRIEF,BUNDLE])
assign('B0119','bounded_conclusion','The current conclusion retains no owner/factor/coefficient/panel/limit execution and no arithmetic Route advancement. Its bounded-source phrases are subject to explicit B0018 four-CW unverified scope and the18/eight partition.',[MATRIX,LOCK])
assign('B0122 B0123','declared_funding_and_interests','The wording is present in the author-configuration/declaration cargo. Fidelity to that declaration can be checked; no original financial/conflict attestation or independent fact audit is held. Register UNVERIFIABLE for the literal personal-world fact, not falsehood or misconduct.',[relative(N/'stage2_paper_configuration.md'),relative(DRAFT)])
assign('B0124','nonhuman_study_scope','The declared project is theoretical mathematics with published sources and project workflow artifacts, not human/animal research. N/A follows this intake scope; it is not an institutional exemption determination.',[BRIEF,LOCK])

src_doc=json.loads((ROOT/SOURCE).read_text())
sources={r['source_id']:(i,r) for i,r in enumerate(src_doc['rows'])}
claims=[]
semantics=[]
def emit(bid,lo,hi,role='semantic_full_sentence'):
    original=draft[lo:hi]
    lo+=len(original)-len(original.lstrip())
    hi-=len(original)-len(original.rstrip())
    text=draft[lo:hi]
    if len(text)<3:
        return
    if any(c['draft_span']==span(lo,hi) for c in claims):
        return
    refs=[]
    for group in re.findall(r'\\citep\{([^}]+)\}',text):
        refs.extend(group.split(','))
    explicit=list(dict.fromkeys(re.findall(r'P32-(?:S\d\d|CW\d\d)',text)))
    if bid in {'B0024','B0028','B0032','B0033','B0036','B0039'} and explicit:
        refs=explicit
    refs=list(dict.fromkeys(refs))
    # A group's terminal citation sentence refers to the preceding source-specific
    # dispositions; it receives no blanket theorem-pass anchor for every source.
    anchors=[]
    tuples=[]
    for ref in refs:
        index,s=sources[ref]
        anchor=s.get('exact_passage_locator') if s.get('support_excerpt') and ref in explicit and 'bound excerpt' in text else None
        if anchor:
            anchors.append(anchor)
        tuples.append({'ref_slug':ref,'anchor':anchor,'excerpt':s.get('support_excerpt') if anchor else None,'held_excerpt_path':SOURCE if anchor else None,'excerpt_pointer':f'/rows/{index}/support_excerpt' if anchor else None,'writer_anchor_status':'EXPLICIT' if anchor else 'ANCHOR_NONE'})
    kinds=['other_factual']
    if re.search(r'\d|eight|four|eighteen|zero|one|two',text,re.I):
        kinds.append('quantitative')
    if re.search(r'\b(?:all|none|no|only|every|must|cannot)\b',text,re.I):
        kinds.append('categorical')
    verdict='VERIFIED'
    findings=[]
    if bid in {'B0122','B0123'}:
        verdict='UNVERIFIABLE'; findings=['P32-R3-F01']
    if bid in {'B0098','B0125'} and re.search(r'byte.identical|byte.verified|rehashed every|public files|public\s+commit',text):
        verdict='UNVERIFIABLE_ACCESS'; findings=['P32-R3-N01']
    if bid=='B0034' and re.search(r'do not establish',text):
        verdict='MINOR_DISTORTION'; findings=['P32-R3-F02']
    if bid=='B0095' and 'because' in text:
        verdict='MINOR_DISTORTION'; findings=['P32-R3-F03']
    cid=f'P32-R3-{bid}-{sum(c["paper_section"]==bid for c in claims)+1:03d}'
    claims.append({'claim_id':cid,'claim_text':text,'draft_span':span(lo,hi),'claim_kinds':kinds,'ref_slugs':refs,'writer_anchors':list(dict.fromkeys(anchors)),'paper_section':bid,'selection_tier':'ALL'})
    rr=R[bid]
    semantics.append({'claim_id':cid,'block_id':bid,'extraction_role':role,'verdict':verdict,'basis_kind':rr['basis_kind'],'reason':rr['reason'],'project_evidence_carriers':rr['carriers'],'source_tuples':tuples,'finding_ids':findings})

for bid in bs:
    if bid not in R:
        continue
    t=bs[bid]['text']; segments=[]
    for m in re.finditer(r'[^\n]+(?:\n|\Z)',t):
        line=m.group().strip()
        if not line or line.startswith('%') or line.startswith(('\\end{','\\begin{','\\scriptsize','\\small','\\toprule','\\midrule','\\bottomrule','\\tightlist','\\par\\endgroup','\\def\\label','\\setlength','\\begingroup')):
            continue
        a,e=m.start(),m.end()
        if line.startswith('\\paragraph{'):
            a=t.find('}',a)+1
        if line.startswith('\\item'):
            a=t.find('\\item',a)+5
        if a<e:
            if segments and segments[-1][1]==a and '\\\\' not in line:
                segments[-1]=(segments[-1][0],e)
            else:
                segments.append((a,e))
    for a,e in segments:
        segment=t[a:e]; start=0
        for m in list(re.finditer(r'(?<=[.!?。])\s+(?=[A-Z\\本文只有有界本階段未])',segment))+[None]:
            stop=m.start() if m else len(segment)
            emit(bid,bs[bid]['start']+a+start,bs[bid]['start']+a+stop)
            if m:
                start=m.end()

coverage_path=Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/scripts/claim_registry_coverage.py')
spec=importlib.util.spec_from_file_location('p32_readonly_lexical_helpers',coverage_path)
cov=importlib.util.module_from_spec(spec);spec.loader.exec_module(cov)
lexical=[]
for sentence in cov._sentences(draft):
    if not cov._candidate_kinds(sentence['text']):
        continue
    lexical.append(sentence)
    bid=next((k for k,v in bs.items() if v['start']<=sentence['start_char']<v['start']+len(v['text'])),None)
    if bid in R:
        emit(bid,sentence['start_char'],sentence['end_char'],'finite_lexical_candidate_exact_span_supplement')

registry={'schema_version':'claim-registry/1.0','draft_raw_sha256':hashlib.sha256(raw).hexdigest(),'claims':claims}
meta={'paper_id':'P32','draft_path':relative(DRAFT),'draft_raw_sha256':registry['draft_raw_sha256'],'total_blocks':len(bs),'selected_blocks':len(R),'claim_count':len(claims),'max_claim_characters':max(map(lambda x:len(x['claim_text']),claims)),'finite_lexical_candidates':len(lexical),'excluded_blocks':[k for k in bs if k not in R],'semantic_extraction_coverage':'not_machine_detectable','verdict_counts':{v:sum(s['verdict']==v for s in semantics) for v in sorted({s['verdict'] for s in semantics})}}
kind=sys.argv[1] if len(sys.argv)>1 else 'meta'
first=int(sys.argv[2]) if len(sys.argv)>2 else 0
count=int(sys.argv[3]) if len(sys.argv)>3 else len(claims)
if kind=='meta':
    print(json.dumps(meta,ensure_ascii=False))
elif kind=='registry':
    print(json.dumps(claims[first:first+count],ensure_ascii=False))
elif kind=='semantic':
    print(json.dumps(semantics[first:first+count],ensure_ascii=False))
