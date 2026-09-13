"""Read-only component assembler: stdout only; no validators or artifact writes.

Semantic judgments below were made after reading the current draft, original
held sources, and every old/new operation with its specific authority. Extraction
is an indexing aid, not a semantic-verification engine. Root owns formal outputs.
"""
import importlib.util
import json
import re
import hashlib
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/flow_systems')
PAPER = ROOT / 'papers/31-level11-conjugacy-owner-ledger'
N = PAPER / 'notes'
def read(name):
    return json.loads((N / name).read_text())
def descriptor(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
def blocks(text):
    return {m.group(1): {'text': m.group(2).rstrip(), 'start': m.start(2)}
            for m in re.finditer(r'<!--block:(B\d+)-->\n(.*?)(?=<!--block:|\Z)', text, re.S)}
DRAFT = N / 'stage4_prime_revision_round4.tex'
draft = DRAFT.read_text()
bs = blocks(draft)
rawhash = hashlib.sha256(draft.encode()).hexdigest()
prefix_bytes = [0]
for c in draft:
    prefix_bytes.append(prefix_bytes[-1] + len(c.encode()))
def span(a, b):
    return {'start_byte': prefix_bytes[a], 'end_byte': prefix_bytes[b]}

# Each block has a separately reasoned classification; sentence verdicts below
# retain finer finding boundaries and do not equate a block touch with support.
R = {}
def assign(ids, kind, rationale, carriers):
    for bid in ids.split():
        R[bid] = {'basis_kind': kind, 'reason': rationale, 'carriers': carriers}
POP = 'papers/26-level11-newform-time-change/results/round8_summary.json'
BRIEF = 'papers/31-level11-conjugacy-owner-ledger/notes/stage1_prestart_brief.md'
MATRIX = str((N/'stage4_prime_method_passage_matrix_round3.json').relative_to(ROOT))
HIST = str((N/'stage1_phase6_claim_intent_manifest.json').relative_to(ROOT))
BUNDLE = str((N/'stage4_prime_revision_evidence_bundle_round4.json').relative_to(ROOT))
LOCK = 'BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json'
assign('B0006 B0007','bounded_synthesis_and_prospective_target','The 138/55 input is inherited, 9453 is choose(138,2), source partition is 7+15 among the original 22. Design targets are expressly unexecuted; A1-only and no novelty/Route promotion agree with the controlling P31 scope. Reproducible refers to architecture and artifacts, not a implemented verifier or current archive.',[POP,BRIEF,MATRIX,LOCK])
assign('B0011 B0012','inherited_population_and_owner_policy','Read P26 instance/group controls and P31 intake. Counts and period-coordinate inheritance are not owner results. Three inverse branches are conditional on subgroup witnesses; unresolved remains a valid disposition. No equality filter is promoted into a complete subgroup decision.',[POP,BRIEF,BUNDLE])
assign('B0013 B0014','research_question','A question proposes conditional full closure; it does not assert that the 138 owners have been certified.',[BRIEF])
assign('B0015','prospective_byte_audit','The same canonical partition generates the pair rows, so agreement is byte/bookkeeping consistency, not independent semantic validation. Explicit absent labels and theorem commitments are retained.',[BUNDLE])
assign('B0016','bounded_family_context','The four families are expressly project categories. S05/S06 original abstracts support existence of recognition/domain ingredients; S16/S17 support existence of conjugacy algorithms with important hypotheses. This supports a family-level possible ingredient description, not every source in a range or any P31 specialization. S23/S24 are explicitly metadata-only. No new theorem or priority is asserted.',[MATRIX,'papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round1_reference_network_audit.json'])
assign('B0017 B0018','prospective_evidence_order','Owner identity, proof objects, and projected estimands are correctly distinguished; required registration and evidence order are normative future gates, not a completed workflow.',[BRIEF,BUNDLE])
assign('B0021 B0025 B0029 B0032','source_specific_bounded_disposition','Each individual context is adjudicated separately in phase_B. Metadata-only roles are project labels; seven excerpts support only the identified narrow context. None proves the registered role or the P31 canonicalizer in full.',[MATRIX,'papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round1_source_finalization_proposal.json'])
assign('B0022 B0023','bounded_synthesis','The modest plausible-ingredient statement is supported by S05/S06; the seven/fifteen partition is a local source-finalization result. Explicitly a project-use boundary, not exhaustive literature absence or full theorem transfer.',[MATRIX])
assign('B0026 B0027','logical_transfer_boundary','Conjugacy in an ambient group is existential over a larger set of witnesses; it does not imply a witness in Gamma0(11). Failed bounded search is not a nonexistence proof. Prospective subgroup/orientation/root and termination obligations are valid design conditions.',[MATRIX,BRIEF])
assign('B0030','admissibility_definition','The acceptance predicates are normative. The final negative claim is narrowed to no retained source admitted here as the complete project-specific solver; it is not a theorem that no solver exists in the literature.',[MATRIX])
assign('B0033','logical_information_comparison','A labeled partition determines its cardinality but a cardinality does not determine the labeled partition: for four elements, partitions {ab,cd} and {ac,bd} both have two blocks. Thus aggregate agreement cannot certify pair identities.',[])
assign('B0112 B0038','metadata_not_method_transfer','Current prose explicitly withholds substantive mechanisms from S23/S24 and calls categories project-assigned roles. Fresh metadata identity does not upgrade these to original method passages.',[MATRIX])
assign('B0036','bounded_search_provenance','44 manifestations -9 duplicates =35 unique -13 exclusions =22 retained. The 20-query one-top-result Crossref replay is expressly a new dated supplement, not recovered original exclusion decisions; two added method records yield 24 current bibliography entries.',[str((N/'stage1_phase2_source_inventory.tsv').relative_to(ROOT)),BUNDLE])
assign('B0037 B0039','matrix_and_citation_accounting','Current matrix contains 24 rows: 7 bounded locators,15 unavailable,2 metadata-only. Current bibliography has24 unique entries and26 cite occurrences. Source identity and citation closure are distinct from passage support.',[MATRIX,str((N/'stage4_prime_references_round2.bib').relative_to(ROOT))])
assign('B0041','historical_method_and_review','The retained screening/coding and review records support bounded closed-corpus synthesis and four procedurally separated same-family roles, not statistically independent replications or scientific experiments.',[BUNDLE,HIST])
assign('B0042','historical_inventory_not_semantic_completeness','Revision1 is a dated historical scope, and the Phase6 manifest has eight entries. Eight cannot establish completeness of current semantic extraction: source-status, metadata, workflow, and design-assertion sentences extend beyond that inventory.',[HIST,BUNDLE])
assign('B0045 B0046 B0047 B0048','prospective_typed_map','The equations define a proposed partial root/canonicalizer and total typed disposition. Returning Unresolved makes delta total without making owner certification total. No existence or termination theorem has been proved here.',[BRIEF,BUNDLE])
assign('B0049','conditional_inverse_policy','Self-reciprocal witness gives one owner; certified nonconjugacy gives two oriented values; absent either certificate gives Unresolved. These are prospective branches, not results for any frozen instance.',[BUNDLE])
assign('B0050 B0051','conditional_biconditional','On X_res, equality of canonical bytes iff same oriented primitive owner supplies soundness and completeness; determinism is a separate implementation obligation. A total-owner theorem additionally needs X_res=X. This is a target contract, not a theorem proved by the present manuscript.',[BUNDLE])
assign('B0052','prospective_root_metadata','Rooting first avoids counting a traversal power as a primitive owner; retaining the exponent preserves incidence provenance. The required maximality proof is not asserted executed.',[BRIEF,BUNDLE])
assign('B0054 B0055 B0057','prospective_certificate_and_verifier','The future certificate fields, verifier rejection rules, schema versioning and typed failures are normative design requirements. No frozen schema, verifier, witness, or executed acceptance predicate is claimed.',[BUNDLE])
assign('B0056 B0091','unexecuted_scientific_state','The selected lock and empty protected P31 science trees contain no solver/canonicalizer/owner result. The article explicitly calls the design non-executable and makes no computation or theorem-completion claim.',[LOCK])
assign('B0058','positive_negative_proof_distinction','An explicit subgroup conjugator can witness a positive existential claim. A negative requires complete theorem-backed coverage; search exhaustion without a completeness theorem is insufficient. The paragraph specifies proof obligations, not a found negative.',[])
assign('B0059','prospective_target_blind_fixtures','Fixture list and pre-outcome registration are proposals. No fixture is claimed passed, no outcome-tuned certification is authorized.',[BUNDLE])
assign('B0061 B0062 B0063 B0064','finite_pair_coverage_limits','138*137/2=9453 unordered distinct pairs omits diagonal, ordered reverse duplication and triples. A table derived from one partition cannot supply independent semantic labels. Disagreement retention and separate direct certificates are conditional design provisions.',[])
assign('B0065','byte_equivalence_and_unjustified_superlative','Equality of deterministic byte strings induces an equivalence relation, but the distinct-pair expansion has explicitly omitted fixtures and no independent semantic truth source. The unqualified most-demanding comparison has no metric or demonstrated comparison class.',[])
assign('B0067 B0068 B0069 B0070 B0071 B0072 B0113','conditional_G_I_C_definitions','After X_res=X, I has one row per138 inputs, G is distinct owner_bytes, C is distinct(cell_key,owner_bytes). Equivalent representatives preserve owner bytes by the conditional biconditional; global dedup and cell dedup answer different questions. Until closure only I_diag accepts unresolved diagnostics and no complete G/I/C is materialized. The table is prospective, not experimental output.',[BUNDLE])
assign('B0073','internal_schema_consistency','First sentence preserves zero-unresolved closure. The following reference to I retaining unresolved diagnostics conflicts with the controlling B0067/B0113 I_diag-only rule. Schema precedence preserves the principal gate but does not remove the inconsistent referent.',[BUNDLE])
assign('B0075 B0076 B0077','precommitted_design_positions','The eight listed positions match a historical eight-entry design inventory; they are explicitly design and bounded synthesis, not current semantic-registry size or executed theorem. The corpus contribution phrase is interpreted only at the bounded family level under B0021/B0025/B0029/B0032.',[HIST,MATRIX])
assign('B0079 B0105','historical_reader_inventory_limit','Current prose explicitly states the older reader inventory is stale and not a present recovery certificate or archive; it does not claim future synchronization complete. Parent retains ownership of official binding checks; historical descriptor mismatch is not silently rewritten.',[str((N/'stage4_prime_reader_artifact_manifest_round2.json').relative_to(ROOT)),LOCK])
assign('B0080 B0081','prospective_execution_gates','Four future layers and theorem-to-certificate fixtures are a design recommendation and authorization boundary, not a demonstrated globally smallest test or completed scientific execution.',[BRIEF,BUNDLE])
assign('B0083','comparative_design_claim','Partition/invariant correspondence is elementary and replacing independent foundational pair claims with a canonicalizer is an architectural change. No complexity or superiority theorem establishes most demanding adversarial check available.',[])
assign('B0084 B0085 B0086 B0111','conditional_design_scope','Conditional canonicalizer requirements and G/I/C interpretation follow their definitions. The two reducer comparison is explicitly hypothetical with no frozen matrices/theorems/fixture corpus, so it is not implementation evidence. Loss of one biconditional direction indeed loses either soundness or completeness.',[BUNDLE])
assign('B0087','scope_not_new_Route_review','Current P31 frozen route state is A1-only, no formal tuple/A2/B; no determinant or operator result is claimed. This is a scope consistency check, not a fresh Route evaluation.',[BRIEF,LOCK])
assign('B0089','screening_and_source_limits','The twenty replay decisions cannot recover the original13 exclusions; current matrix partition is7+15+2 and stronger role transfer remains withheld. It is a bounded provenance statement.',[MATRIX,BUNDLE])
assign('B0090','unknown_integrity_screen','No general current retraction/conflict clearance is asserted. S16 primary page range287-305 resolves the field note but cannot establish corpus-wide clearance. No priority conclusion follows a bounded comparison.',[MATRIX])
assign('B0092','procedural_not_independent_AI_review','Same-family role separation gives documented viewpoints, not independent statistical evidence. Author gate confirmations establish decisions, not personal source-reading attestation.',[BUNDLE])
assign('B0094 B0095 B0096','future_work_only','The ordered list requires new authority for source-finalization, theorem/schema work,138 certifications,9453 audit rows, and G/I/C materialization. The manuscript itself grants no execution or retrieval authority.',[BRIEF,BUNDLE])
assign('B0098 B0099','conclusions_bounded_by_unexecuted_state','Conclusion restates prospective total closure and derived pair audit, differentiates G/I/C, and explicitly denies scientific result or Route promotion. Seven/fifteen provenance counts are supported; no computed owner count is inferred.',[MATRIX,BRIEF,LOCK])
assign('B0101 B0108','human_accountability_and_verification_boundary','Author identity and decisions are in the retained metadata/authority chain. Personal full-text/exact-passage verification is not independently evidenced. B0108 surviving any-to-every disclaimer change is separately flagged under E6; bounded seven/fifteen source claims do not establish human reading.',[BUNDLE,HIST])
assign('B0102 B0103','author_declaration','Funding and competing-interest statements are retained author declarations, not independently verified financial facts. No conflicting evidence was found in the allowed materials; no external clean screen is implied.',[LOCK])
assign('B0104','nonhuman_study_scope','The project consists of theoretical methods, published sources and project-owned records; no human/animal experimental intake exists. Ethics applicability is N/A on that scope, not an institutional exemption determination.',[BRIEF,LOCK])
assign('B0107','narrowed_AI_disclosure','Current clause explicitly declines complete chronology/backend/task inventory from insufficient retained author metadata, and separates historical review roles from later assistance. No AI scientific execution or correction validation is asserted.',[BUNDLE,LOCK])

findings = [
 {'id':'P31-R3-F01','severity':'SERIOUS','blocks':['B0042'],'class':'UNSUPPORTED_CURRENT_COMPLETENESS','verdict':'UNVERIFIABLE','trigger':'complete set of eight substantive article claims','reason':R['B0042']['reason'],'required_disposition':'At mandatory checkpoint, obtain a specific author disposition; do not use historical eight as current extraction denominator or revise automatically.'},
 {'id':'P31-R3-F02','severity':'SERIOUS','blocks':['B0065','B0083'],'class':'UNSUPPORTED_COMPARATIVE_SUPERLATIVE','verdict':'UNVERIFIABLE','trigger':'most demanding','reason':'No comparison metric, complete alternative fixture inventory, or evidence proves the superlative; current B0061/B0062 explicitly omit self/reversal/triple/independent semantic coverage. The valid9453 arithmetic is unaffected.','required_disposition':'Author must choose removal/narrowing or supply support; no automatic correction.'},
 {'id':'P31-R3-F03','severity':'MINOR','blocks':['B0073'],'class':'INTERNAL_SCHEMA_REFERENT_CONFLICT','verdict':'CONTRADICTED','trigger':'may retain a diagnostic record','reason':R['B0073']['reason'],'required_disposition':'Author disposition needed for I versus I_diag referent; principal closure gate remains preserved.'},
 {'id':'P31-R3-F04','severity':'SERIOUS','blocks':['B0108'],'class':'STRENGTH-DRIFTED','verdict':'STRENGTH-DRIFTED','trigger':'verified every claim','reason':'Round3 operation13 changes the no-personal-passage-verification disclaimer from any claim to every claim. This narrows the disclaimer and allows an implication of some verified claims that the old sentence excluded. The status-only authority required preservation of integrity limitations and does not specifically authorize this semantic latitude.','required_disposition':'Specific author keep/restore/replace decision is mandatory. Empty registered claim surfaces and an authorized block target do not waive E6.'}
]

network = read('stage4_5_round1_reference_network_audit.json')
web = read('stage4_5_round3_p31_reference_web_raw.json')
proposal = read('stage4_5_round1_source_finalization_proposal.json')
matrix = read('stage4_prime_method_passage_matrix_round3.json')
supplement = read('stage4_5_round3_p31_reference_same_author_supplement_raw.json')
prow = {r['source_id']:(i,r) for i,r in enumerate(proposal['rows'])}
sources = {}
for i,r in enumerate(network['references']):
    sid = r['ref_slug']; q = (r.get('query_attempts') or {}).get('crossref_doi') or {}
    md = q.get('crossref_message') or {}
    src = {'ref_slug':sid,'anchor':None,'writer_anchor_status':'NONE_UNLESS_SPECIFIC_CONTEXT_BELOW',
           'held_source_path':str((N/'stage4_5_round1_reference_network_audit.json').relative_to(ROOT)),
           'json_pointer':f'/references/{i}/query_attempts/crossref_doi/crossref_message',
           'source_kind':'publisher_deposited_metadata_not_theorem','excerpt':None,
           'observed_capture_time':q.get('requested_at_utc') or q.get('retrieved_at_utc') or 'Historical Round1 capture; see exact retained query-attempt fields'}
    if sid in prow:
        pi,p = prow[sid]
        if p.get('support_excerpt'):
            src.update(anchor=p['exact_passage_locator'],source_kind='bounded_original_abstract_or_page_excerpt',excerpt=p['support_excerpt'],
                       held_excerpt_path=str((N/'stage4_5_round1_source_finalization_proposal.json').relative_to(ROOT)),excerpt_pointer=f'/rows/{pi}/support_excerpt',
                       original_excerpt_capture_trace=p['authoritative_query_trace'])
            if md.get('abstract'):
                src.update(json_pointer=f'/references/{i}/query_attempts/crossref_doi/crossref_message/abstract',fuller_original_passage=md['abstract'])
            if sid=='P31-S19':
                src.update(held_source_path=str((N/'stage4_5_round3_p31_reference_same_author_supplement_raw.json').relative_to(ROOT)),json_pointer='/reference_event/result',observed_capture_time=supplement['reference_event']['completed_at'],anchor_validation='Exact sentence corroborated in original AMS indexed text and page182 footer in same original university-hosted PDF index. Physical PDF page1 structural preflight NOT_RUN; no successful PDF-validator assertion.')
    sources[sid]=src

A_notes = {
1:'Fresh Wiley primary record plus original DOI metadata match author,title,1969,series2 volume1 issue1 pages351-357 and DOI.',
2:'Primary indexed references and original registry identify Kulkarni1991 113(4)1053-1133. Registry only supplies first page1053; end1133 is independently corroborated in primary article references, not inferred from first-page metadata.',
3:'Four named authors,1993,title,venue pages11-34 and DOI match original registry; primary Hsu article references corroborate identity.',
4:'Fresh Wiley primary record and original registry match Lang/Lim/Tan1995 volume27 issue5 pages491-502 DOI.',
5:'Hsu1996 metadata and primary author/original-paper surfaces agree; abstract proves a congruence test exists, not a P31 conjugacy solver.',
6:'Voight2009 Journal de Theorie des Nombres de Bordeaux21(2)467-489 DOI match Mersenne/Numdam original record; finite exact algebraic generators and cofinite-area scope retained.',
7:'Latimer/MacDuffee1933 original registry and Taussky primary reference support pages313-316; first-page-only registry is not treated as the entire page range.',
8:'Cambridge original record identifies Taussky1949 volume1 issue3 pages300-302 DOI;2018 online digitization date is not publication year.',
9:'Wallace1984 original DOI metadata plus author publication list support volume283 issue1 pages177-184.',
10:'Appelgate/Onishi1981 original journal record9(11)1121-1130 matches;2007 online posting is not the original publication year.',
11:'Grunewald1980 chapter Word ProblemsII Studies in Logic95 pages101-139 and DOI confirmed in publisher index and Grunewald/Segal own reference. Missing registry author field is supplemented, not guessed.',
12:'Grunewald/Segal1980 Annals112(3)531-583 DOI match original registry and primary JSTOR record.',
13:'Eick/Hofmann/OBrien2019 JLMS100(3)731-756 match Wiley journal record; preprint date distinguished.',
14:'Sarnak1982 JNT15(2)229-247 original registry/publisher record; asymptotic class-number subject not finite labeled owners.',
15:'Series1985 JLMS series2 volume31 issue1 pages69-80 DOI match Wiley and primary records.',
16:'Epstein/Holt2006 IJAC16(2)287-305 verified by primary author/institutional Warwick record and original DOI metadata. Secondary287-306 is a retained discrepancy, not a manuscript error.',
17:'Buckley/Holt2013 IJAC23(5)1127-1150 original registry identifies journal article;2011 arXiv preprint is not substituted for journal year.',
18:'Baake/Roberts2001 Nonlinearity14(4)R1-R24 confirmed in author-hosted original first page and original DOI metadata.',
19:'Lenstra Jr2002 Notices49(2)182-192 identified by primary AMS/university-hosted original and retained bibliography. No DOI is assigned in this bibliography; lack of a DOI is not a fabricated-reference finding. Exact PDF page1 structural preflight is not claimed.',
20:'Cohen1993 book GTM138 Springer and DOI verified by primary Springer book page; electronic posting2013 is not the print publication year. GTM138 is a series volume, not an article volume.',
21:'Golovchanskii/Smotrov2008 English Sbornik Mathematics199(7)1009-1031 and DOI match Mathnet primary journal; Russian original pagination is not substituted.',
22:'Traina1985 JNT21(2)176-184 and DOI match original publisher-deposited metadata; bounded fresh query does not itself prove project applicability.',
23:'Necula1997 POPL24 pages106-119 DOI and author match original ACM registry metadata and Berkeley author primary listing. Current manuscript uses metadata only.',
24:'Crosby/Wallach2009 18th USENIX Security title,authors,venue,publisher,Montreal and official URL agree with original conference metadata; no unprovided DOI/pages invented.'}
A=[]
for i,r in enumerate(network['references'],1):
    sid=r['ref_slug']; ev=[]
    for j,e in enumerate(web['events']):
        if any(q.get('ref')==sid for q in e.get('queries',[])):
            ev.append({'held_source_path':str((N/'stage4_5_round3_p31_reference_web_raw.json').relative_to(ROOT)),'json_pointer':f'/events/{j}/result','queries':e['queries'],'actual_started_at':e.get('start'),'actual_completed_at':e.get('end')})
    A.append({'ref_slug':sid,'verdict':'VERIFIED_IDENTITY_WITH_LIMITS','fields_examined':r['fields'],'field_disposition':{k:'MATCH_WITH_PRIMARY_OR_ORIGINAL_REGISTRY_SUPPORT' for k in r['fields']},'reason':A_notes[i],'fresh_query_evidence':ev,'original_metadata_pointer':f'/references/{i-1}/query_attempts','held_original_metadata_path':str((N/'stage4_5_round1_reference_network_audit.json').relative_to(ROOT)),'retraction_conflict_clearance':'UNKNOWN_NOT_ESTABLISHED','theorem_or_full_text_verification':False})

B=[]
for bid,b in bs.items():
    matches=list(re.finditer(r'\\citep\{([^}]+)\}',b['text']))
    for occ,m in enumerate(matches,1):
        sid=m.group(1)
        # Current draft citations are single-source occurrences. Include the full
        # surrounding source-specific paragraph, not a title-only snippet.
        starts=[x.start() for x in re.finditer(r'(?:The bibliographic record|The bounded source-finalization record)',b['text'])]
        if starts:
            lo=max([x for x in starts if x<=m.start()] or [0]);hi=min([x for x in starts if x>m.start()] or [len(b['text'])])
        else:lo,hi=0,len(b['text'])
        context=b['text'][lo:hi].rstrip();g=re.search(r'anchor=(\S+)',context)
        anchor=unquote(g.group(1)) if g and g.group(1)!='none' else None
        ss=sources[sid];isbounded=ss['excerpt'] is not None
        reason = 'Current occurrence expressly limits the source to metadata identity and a project-assigned prospective role; no substantive transfer is made. Identity evidence supports that narrow claim; author-supplied passage anchor is absent and no theorem support is inferred.'
        if isbounded:
            limits={'P31-S05':'The excerpt only establishes a congruence-recognition test; it does not give the P31 permutation implementation or owner policy.', 'P31-S06':'Cofinite-area hypothesis is explicit; this is a computable domain context, not a proven terminating complete Gamma0(11) pair certificate.', 'P31-S08':'The opening sentence attributes earlier matrix work to Latimer and MacDuffee; it does not establish Taussky refinement or P31 transfer.', 'P31-S09':'Five retained words identify hyperbolic matrices; the fuller abstract gives ideal-class context, but the five-word phrase alone is not the bijection theorem.', 'P31-S16':'Fuller original abstract qualifies linear-time claim by RAM computation model; no complexity or specialization result for P31 follows.', 'P31-S17':'Fuller original abstract assumes finitely generated group/precomputed structures and calls algorithm non-practical; applicability/termination for the frozen P31 representation remains unproved.', 'P31-S19':'Continued-fraction sentence supplies Pell-equation context only. Indexed original text corroborates sentence; page182 footer supports first-page context, but physical page1 structural preflight was not run.'}
            reason='Current text explicitly says bounded context, not proof of the registered role in full. '+limits[sid]
        B.append({'context_id':f'P31-R3-B-{len(B)+1:03d}','block_id':bid,'ref_slug':sid,'cite_occurrence':occ,'draft_span':span(b['start']+lo,b['start']+lo+len(context)),'context_text':context,'writer_anchor':anchor,'verdict':'VERIFIED_BOUNDED_CONTEXT' if isbounded else 'VERIFIED_METADATA_ONLY_CONTEXT','substantive_registered_role_full_verification':'NOT_ESTABLISHED','reason':reason,'source_tuples':[dict(ss,writer_anchor_status='EXPLICIT' if anchor else 'ANCHOR_NONE')],'matrix_dependency':MATRIX})

# Full prose-sentence extraction plus exact finite lexical coverage candidates.
# Sentence boundaries keep raw UTF8 offsets. TeX comments and layout syntax are
# excluded, while equations, the schema table and future-work items are indexed.
claims=[]; semantic=[]
def emit(bid,lo,hi,role='semantic_full_sentence'):
    txt=draft[lo:hi]
    left=len(txt)-len(txt.lstrip());right=len(txt.rstrip());lo+=left;hi=lo+right-left;txt=draft[lo:hi]
    if len(txt)<3:return
    rr=R[bid];sid=[];anchors=[]
    for c in B:
        if c['block_id']==bid and c['draft_span']['start_byte']<=prefix_bytes[lo]<c['draft_span']['end_byte']:
            sid.append(c['ref_slug'])
            if c['writer_anchor']:anchors.append(c['writer_anchor'])
    # Do not attach every source in a grouped paragraph to an unrelated claim.
    sid=list(dict.fromkeys(sid));anchors=list(dict.fromkeys(anchors))
    if bid in ['B0016','B0112']:
        sid=re.findall(r'\\citep\{([^}]+)\}',txt)
        anchors=[]
        if bid=='B0016' and 'Finite-index subgroup' in txt:
            sid=['P31-S05','P31-S06']
        elif bid=='B0016' and 'hyperbolic conjugacy methods' in txt:
            sid=['P31-S16','P31-S17']
        elif bid=='B0112' and not sid and re.search(r'\bTheir\b|from them',txt):
            sid=['P31-S23','P31-S24']
    kinds=['other_factual']
    if re.search(r'\d|eight|seven|fifteen|138|一百三十八|九千四百五十三',txt,re.I):kinds=['quantitative','other_factual']
    if re.search(r'\b(?:must|only|no |not |requires|cannot|complete|exact|all )',txt,re.I):kinds=list(dict.fromkeys(kinds+['categorical']))
    cid=f'P31-R3-{bid}-{sum(c["claim_id"].startswith("P31-R3-"+bid+"-") for c in claims)+1:03d}'
    selected=[]
    for f in findings:
        if bid in f['blocks'] and f['trigger'] in re.sub(r'\s+',' ',txt):selected.append(f)
    verdict = selected[0]['verdict'] if selected else 'VERIFIED'
    if bid in ['B0102','B0103'] and not selected:verdict='UNVERIFIABLE'
    entry={'claim_id':cid,'claim_text':txt,'draft_span':span(lo,hi),'claim_kinds':kinds,'ref_slugs':sid,'writer_anchors':anchors,'paper_section':bid,'selection_tier':'ALL'}
    claims.append(entry)
    semantic.append({'claim_id':cid,'block_id':bid,'extraction_role':role,'verdict':verdict,'basis_kind':rr['basis_kind'],'reason':(' '.join(f['reason'] for f in selected) if selected else rr['reason']),'finding_ids':[f['id'] for f in selected],'project_evidence_carriers':rr['carriers'],'source_tuples':[sources[x] for x in sid],'original_passage_support':('BOUNDED_CONTEXT_OR_METADATA_ONLY; see phase_B' if sid else 'No writer passage anchor supplied; local analytical/prospective or project-record claim as classified'),'claim_truth_not_implied_by_coverage':True})
for bid,rr in R.items():
    b=bs[bid];t=b['text']
    # Paragraph headings are presentation only. Remove contiguous syntax-only
    # lines, never normalize retained prose before taking exact spans.
    valid=[]
    for lm in re.finditer(r'[^\n]+(?:\n|\Z)',t):
        line=lm.group().strip()
        if not line or line.startswith('%') or line.startswith(('\\end{','\\begin{','\\scriptsize','\\toprule','\\midrule','\\bottomrule','\\tightlist','\\par\\endgroup','\\setlength')):continue
        a,bend=lm.start(),lm.end()
        if line.startswith('\\paragraph{'):
            close=t.find('}',a);a=close+1
            while t[a:a+1]=='\\':
                mm=re.match(r'\\[A-Za-z]+\s*',t[a:])
                if not mm:break
                a+=mm.end()
        if line.startswith('\\item'):a=t.find('\\item',a)+5
        if a<bend:valid.append((a,bend))
    chunks=[]
    for a,e in valid:
        if chunks and a==chunks[-1][1]:chunks[-1]=(chunks[-1][0],e)
        else:chunks.append((a,e))
    for a,e in chunks:
        segment=t[a:e];start=0
        for m in list(re.finditer(r'(?<=[.!?。])\s+(?=[A-Z\\本文只有有界本階段未])',segment))+[None]:
            end=m.start() if m else len(segment)
            emit(bid,bs[bid]['start']+a+start,bs[bid]['start']+a+end)
            if m:start=m.end()

coverage_path=Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/scripts/claim_registry_coverage.py')
spec=importlib.util.spec_from_file_location('p31_readonly_lexical_helpers',coverage_path)
cov=importlib.util.module_from_spec(spec);spec.loader.exec_module(cov)
lexical_count=0
for s in cov._sentences(draft):
    if not cov._candidate_kinds(s['text']):continue
    lexical_count+=1
    if any(c['draft_span']==span(s['start_char'],s['end_char']) for c in claims):continue
    bid=next((k for k,v in bs.items() if v['start']<=s['start_char']<v['start']+len(v['text'])),None)
    if bid in R:emit(bid,s['start_char'],s['end_char'],'finite_lexical_candidate_exact_span_supplement')

registry={'schema_version':'claim-registry/1.0','draft_raw_sha256':rawhash,'claims':claims}

E6_comments = [
 [
 ('same_rung_reframing','Bounded closest-work comparison names frozen families and disclaims exhaustive priority; no P31 solver result is added.'),
 ('authorized_narrowing','Reader traceability is narrowed to retained paths and missing availability fields, as REV002 requests.'),
 ('authorized_narrowing','Separates review-development provenance from scientific research method; role count is not independent validation.'),
 ('authorized_narrowing','Introduces resolved-domain scope and typed disposition; avoids asserting total owner certification before all inputs resolve.'),
 ('authorized_narrowing','Explicitly separates self/order/triple fixtures from distinct-pair coverage; no executed test is added.'),
 ('authorized_narrowing','Replaces implementation-like reproducibility with non-executable specification and missing-schema/verifier statement.'),
 ('authorized_narrowing','Exposes original exclusions/locator gaps without inventing ledger decisions or anchors.'),
 ('authorized_narrowing','Unresolved inverse relation no longer automatically creates two owners; mathematical status remains prospective.'),
 ('authorized_design_precision','Separates G/I/C schema, provenance, keys and I_diag gating, conditional on closure.'),
 ('authorized_design_addition','Inserted synthetic producer example is explicitly hypothetical/unexecuted and demonstrates required common fields only.'),
 ('authorized_narrowing','Removes implication that derived byte rows independently expose semantic false merges/splits; no independent labels exist.')],
 [
 ('authorized_narrowing','Absolute inversion separation becomes self-reciprocal/inverse-separated/unresolved branches, each evidence-gated.'),
 ('authorized_narrowing','Removes unsupported semantic/triple audit coverage and restricts pair expansion to bookkeeping consequences.'),
 ('authorized_bounded_addition_later_corrected','Specific closest-work search authority adds S23/S24 method neighbors. Historical stronger mechanism transfer lacked retained exact passages and was withdrawn inRound4; target authority is not retroactive passage verification.'),
 ('authorized_bounded_addition_later_corrected','Inserted S23/S24 mechanism paragraph fits requested two missing families but passage claims were later explicitly withdrawn inRound4. Current metadata-only state is not retrospective proof of the old paragraph.'),
 ('authorized_provenance_addition','Adds dated20-query one-top-record replay and two methods; explicitly not reconstructed original exclusions.'),
 ('authorized_provenance_update_later_corrected','Updates current row count24 and records two then-finalized neighbors; Round4 withholds their mechanism passages. No current inherited method PASS is accepted.'),
 ('same_rung_with_later_narrowing','Reorganizes component categories without claiming an executed P31 theorem; Round4 explicitly makes these project-assigned roles.'),
 ('authorized_structural_update','Updates citation identity closure24; explicitly does not make structural resolution a theorem-passage check.'),
 ('authorized_narrowing','Adds X_res=X closure while delta remains total even with Unresolved; no completed owner theorem.'),
 ('authorized_design_precision','Adds three inverse branches with exact witness or lawful obstruction and fail-closed remainder.'),
 ('authorized_narrowing','Canonical biconditional restricted to resolved domain; complete total-owner claim additionally requires closure.'),
 ('authorized_narrowing','Distinguishes soundness/completeness/determinism on kappa from total typed delta; no tool implementation claimed.'),
 ('same_prospective_rung','Future certificate should-bind-at-least becomes each-future-certificate-binds plus inverse fields; governing future marker preserves normative status, not an executed certificate.'),
 ('authorized_narrowing','Derived byte audit explicitly cannot detect semantic errors without independent labels or binding theorem; no third route added.'),
 ('authorized_design_precision','Separate fixture categories and omitted first-class coverage made explicit; all remain prospective.'),
 ('authorized_design_precision','Condenses schema precedence and preserves zero-unresolved closure/I_diag; downstream results remain unexecuted.'),
 ('authorized_design_addition','Inserts consolidated normative G/I/C/I_diag table with closure/provenance rules, not a populated result table.'),
 ('authorized_traceability_addition_later_corrected','Reader manifest inventory language then overreached current matrix recovery; Round4 explicitly marks historical staleness. Scope authority not scientific or archive certification.'),
 ('authorized_provenance_update','Adds20 dated replay decisions and two locators while retaining no theorem/exclusion-recovery claim; later narrower metadata state applies.'),
 ('authorized_traceability_addition_later_corrected','Materials language describes listed manifest only; Round4 corrects current recovery implication by declaring staleness.')],
 [
 ('authorized_narrowing','First aggregate citation block replaced with S01-S06 source-specific metadata/unavailable or bounded-context dispositions; exact roles not proved in full.'),
 ('authorized_narrowing','Second aggregate block replaced with S07-S13 per-source bounded dispositions and preserved transfer limits.'),
 ('authorized_narrowing','Third aggregate block replaced with S15-S20 per-source bounded dispositions and preserved transfer limits.'),
 ('authorized_narrowing','Fourth aggregate block replaced with S14/S21/S22 metadata-only unavailable dispositions; no aggregate result becomes owner certificate.'),
 ('authorized_disclosure_update_later_corrected','Adds dated AI chronology under disclosure authority; later carrier audit found chronology unsupported andRound4 narrows it. No current scientific execution claim survives.'),
 ('authorized_bounded_status_update','English abstract22-all-unavailable becomes7 bounded/15 unavailable, retaining not-full-role-proof and no execution.'),
 ('authorized_bounded_status_update','Chinese abstract status coherently becomes7 bounded/15 unavailable while no novelty/theorem/result remains.'),
 ('authorized_bounded_status_update','Negative-boundary paragraph updates7/15 and retains no universal literature absence/full-role proof.'),
 ('authorized_bounded_status_update','Matrix summary updates7/15 plus retained2method neighbors; Round4 explicitly metadata-only for latter.'),
 ('authorized_bounded_status_update','Citation closure update preserves distinction between identity, narrow locator and full role support.'),
 ('authorized_bounded_status_update','Limitations update7/15 and preserve missing original exclusions and no guessed anchors.'),
 ('authorized_bounded_status_update','Conclusion source provenance update remains partial and no scientific result/Route advance.'),
 ('STRENGTH-DRIFTED','The7/15 status update is authorized, but any claim to every claim silently narrows the no-personal-exact-passage-verification disclaimer. Specific request permits only status/coherence change and expressly preserves integrity limitations. This exact change survives in currentB0108.')],
 [
 ('authorized_narrowing','EA003 withdraws S23/S24 mechanism transfer; metadata identity and prospective design only remain.'),
 ('authorized_narrowing','EA002 replaces literature-wide no-solver claim with no retained source admitted as the complete project solver.'),
 ('authorized_narrowing','EA003 keeps24=7+15+2 but makes two method neighbors metadata-only and disclaims exact support excerpts.'),
 ('authorized_narrowing','EA003 distinguishes project-assigned source categories from passage-established mechanisms.'),
 ('authorized_narrowing','EA004 explicitly marks historical reader manifest stale and not a current content-addressed archive/recovery certificate.'),
 ('authorized_narrowing','EA004 materials statement narrows exact recovery and forbids uncompleted future synchronization assertion.'),
 ('authorized_narrowing','EA001 AI disclosure drops unsupported full chronology/backend/task inventory, keeps known assistance and same-family limits.'),
 ('authorized_narrowing','EA003 withdraws safety-checking/membership/append-only mechanism transfers absent original passages.')]
]
bundle=read('stage4_prime_revision_evidence_bundle_round4.json')
E6=[]
for ri,r in enumerate(bundle['rounds']):
    pre=blocks((PAPER/r['pre_round_draft']['path']).read_text());patch=read(Path(r['revision_patch']['path']).name)
    authkey='revision_roadmap' if 'revision_roadmap' in r else 'issue_list'
    ap=PAPER/r[authkey]['path'];authority=json.loads(ap.read_text());items=authority.get('items',authority.get('issues',[]))
    for oi,op in enumerate(patch['ops']):
        disposition,why=E6_comments[ri][oi];ids=op.get('roadmap_item_ids',[]);specific=[x for x in items if x.get('id',x.get('correction_id')) in ids]
        old=pre[op['block_id']]['text'] if op['op']=='replace_block' else ''
        entry={'operation_id':f'P31-R{ri+1}-OP{oi+1:02d}','revision_round':ri+1,'operation_index':oi+1,'operation':op['op'],'block_id':op['block_id'],'old_text':old,'new_text':op['new_text'],'old_claim_rung':'prospective_or_bounded_as_in_old_text','new_claim_rung':disposition,'semantic_disposition':disposition,'specific_authority_path':str(ap.relative_to(ROOT)),'specific_authority_items':specific,'judgment':why,'registered_surface_array_is_not_semantic_evidence':True,'author_specific_disposition_required':disposition=='STRENGTH-DRIFTED'}
        if disposition=='STRENGTH-DRIFTED':
            entry.update(old_claim_rung='No implication of personal exact-passage verification of ANY claim',new_claim_rung='Only no implication of verification of EVERY claim; weaker disclaimer permits partial-verification implication',exact_old_clause='personally read every source in full or verified any claim at the exact source-passage level.',exact_new_clause='personally read every source in full or verified every claim at the exact source-passage level.',additional_controlling_authority='BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json',authority_required_semantic_branch='Replace only the all-22-no-locators status with the 7/22 versus 15/22 bounded disposition; preserve the human-accountability, no-personal-full-text-attestation, no novelty, and no clean retraction/conflict-screen limitations.',finding_id='P31-R3-F04',current_carry_forward='B0108 is untouched inRound4 and retains verified every claim.')
        E6.append(entry)

orig=read('stage4_5_round3_p31_originality_web_raw.json');D=[]
for unit in orig['units']:
    ei,e=next((i,e) for i,e in enumerate(orig['query_events']) if unit['id'] in e['unit_ids'])
    normalized=re.sub(r'\s+',' ',str(e['result'])).lower();phrase=re.sub(r'\s+',' ',unit['query']).lower()
    hit=phrase in normalized
    D.append(dict(unit,held_returned_pool_path=str((N/'stage4_5_round3_p31_originality_web_raw.json').relative_to(ROOT)),returned_pool_pointer=f'/query_events/{ei}/result',actual_started_at=e['started_at'],actual_completed_at=e['completed_at'],literal_phrase_seen_in_pool=hit,adjudication='STANDARD_DECLARATION_BOILERPLATE_NOT_PLAGIARISM_EVIDENCE' if unit['id'] in ['B0102','B0103'] else 'NO_SUBSTANTIVE_EXACT_MATCH_IDENTIFIED_IN_BOUNDED_RETURNED_POOL',adequacy='Quoted query covers one selected phrase from this unit; many results are broad irrelevant matches. This is bounded search, not plagiarism-detector or full-corpus originality clearance.'))

C=[
 {'id':'C1-population','assertions':['138 instances','55 source-word/prime groups','2/2/134 instance split','three55-group summaries'],'verdict':'VERIFIED_INHERITED_CONTROLS','evidence':descriptor(ROOT/POP),'pointers':['/instances/classification_counts','/groups/word_prime_groups','/groups/law_classification_counts'],'arithmetic':'2+2+134=138; each group-law row sums55; 3*55=165. These are not owner counts.'},
 {'id':'C1-pair-count','assertions':['9453 unordered distinct pairs'],'verdict':'VERIFIED_ARITHMETIC','derivation':'138*137/2=9453. Does not count self pairs, ordered pairs, or triples and proves neither semantic accuracy nor adversarial superiority.'},
 {'id':'C1-search','assertions':['44-9=35','35-13=22','20 exact frozen query strings','2 added methods','24 current entries'],'verdict':'VERIFIED_BOUNDED_ACCOUNTING','carriers':[str((N/'stage1_phase2_source_inventory.tsv').relative_to(ROOT)),BUNDLE],'limits':'Original exclusion ledger not recovered; dated one-top-record replay is separate.'},
 {'id':'C1-matrix','assertions':['7 bounded','15 unavailable','2 metadata-only','24 total','26 citation occurrences'],'verdict':'VERIFIED_STRUCTURAL_ACCOUNTING','observed_matrix_rows':len(matrix['rows']),'observed_bibliography_entries':len(A),'observed_citation_occurrences':len(B),'carriers':[MATRIX,str((N/'stage4_prime_references_round2.bib').relative_to(ROOT))]},
 {'id':'C1-eight','assertions':['eight substantive article claims complete'],'verdict':'UNVERIFIABLE_CURRENT_COMPLETENESS','finding_id':'P31-R3-F01','evidence':descriptor(N/'stage1_phase6_claim_intent_manifest.json'),'limits':'Eight is only a historical ClaimIntent inventory, not this fresh semantic extraction denominator.'},
 {'id':'C2-results','verdict':'NOT_APPLICABLE_NO_P31_EXPERIMENT','reason':'No P31 numerical result, p-value, effect size, sample experiment or populated scientific table is asserted. Inherited P26 controls are labeled and remain distinct. No P31 scientific replay was run.'},
 {'id':'C3-table','verdict':'PROSPECTIVE_SCHEMA_NOT_RESULT','table_block':'B0113','reason':'G/I/C/I_diag cardinalities and gates agree with conditional definitions except B0073 referent conflict. Schema table has no experiment data or alleged measurement. Standalone table traceability is advisory; no figure-result package exists.'},
 {'id':'C4-intake','verdict':'NO_EXPERIMENTS_DECLARED','declaration':read('stage4_5_round2_material_passport.json')['experiment_intake_declaration'],'experiment_provenance':[],'experiment_alignment_results':[],'repro_lock':None,'limits':'Historical passport is intake seed only, not a fresh integrity verdict; inherited P26 result carrier is not a P31 experiment.'}
]

failure_modes=[
 {'id':'reference_fabrication','disposition':'NO_FABRICATED_IDENTITY_FOUND_WITHIN24','basis':'A24 current per-field rows; no current fabricated-reference finding. Metadata verification is not passage/theorem verification.'},
 {'id':'citation_misrepresentation','disposition':'BOUNDED_CONTEXT_ONLY','basis':'B26 distinguishes15 unavailable+7 bounded original contexts+4 metadata-neighbor occurrences; no source role is proved in full. B0016 family taxonomy is bounded by actual ingredient abstracts, not every-source applicability.'},
 {'id':'data_fabrication','disposition':'NO_P31_EXPERIMENTAL_RESULT_CLAIM','basis':'C no-experiment declaration; counts are inherited controls or elementary accounting and prospective cardinalities.'},
 {'id':'plagiarism','disposition':'NO_SUBSTANTIVE_MATCH_IDENTIFIED_BOUNDED_SCREEN','basis':'D84 queries and two same-author primary article surfaces; short funding/conflict boilerplate is not a plagiarism finding. Semantic/whole-corpus originality remains unknown.'},
 {'id':'false_review_independence','disposition':'LIMITATION_RETAINED','basis':'B0041/B0092/B0107 explicitly same-family procedural roles, not statistically independent evidence.'},
 {'id':'overclaiming_or_hallucinated_reasoning','disposition':'OPEN_SERIOUS_FINDINGS','basis':'F01 historical eight cannot certify current completeness; F02 ungrounded comparative superlatives; F03 I/I_diag inconsistency. Conditional mathematical definitions are not theorem execution.'},
 {'id':'undisclosed_AI_or_accountability_laundering','disposition':'DISCLOSED_WITH_OPEN_E6','basis':'Current narrow AI disclosure does not invent chronology or human full-text reading; F04 any-to-every disclaimer drift survives without specific semantic authority.'}
]
compliance={
 'stage':'4.5','research_type':'other_evidence_synthesis','classification_basis':'Closed-corpus literature synthesis plus prospective mathematical certificate design; not SR/meta-analysis and no P31 experiment/human study. Scope metadata is prose, not invented typed prior scope.',
 'RAISE':[
 {'item':'R1-human_responsibility','status':'WARN','evidence':['B0101','B0108'],'reason':'Human accountability is explicit; gate confirmations are not personal source verification. Open disclaimer driftF04 requires author decision.'},
 {'item':'R2-AI_role_disclosure','status':'PASS_BOUNDED','evidence':['B0107','B0092'],'reason':'Codex assistance and same-family review limits disclosed; unknown chronology/backend explicitly not claimed.'},
 {'item':'R3-source_integrity','status':'WARN','evidence':['phase_A','phase_B'],'reason':'24 identities and bounded excerpts distinguished;15 unavailable and2metadata-only remain, no general retraction/conflict clearance.'},
 {'item':'R4-method_transparency','status':'WARN','evidence':['B0036','B0089'],'reason':'Frozen search counts and dated replay distinguished; original excluded-row ledger unavailable.'},
 {'item':'R5-reproducibility','status':'WARN','evidence':['B0056','B0079','B0105'],'reason':'Non-executable architecture and stale historical reader manifest clearly limited; no complete theorem/verifier or persistent archive.'},
 {'item':'R6-claim_calibration','status':'WARN','evidence':['F01','F02','F03','F04'],'reason':'Mandatory author disposition of current semantic defects; no quiet narrowing.'},
 {'item':'R7-privacy_ethics','status':'NOT_APPLICABLE','evidence':['B0104'],'reason':'No humans/animals/identifiable study data under declared intake.'},
 {'item':'R8-review_independence','status':'PASS_BOUNDED','evidence':['B0041','B0092','B0107'],'reason':'Procedural same-family separation is not represented as independent scientific replication.'}],
 'PRISMA_trAIce_adapted':[
 {'item':'identification','status':'INFO','reason':'44manifestations,9duplicates,35unique,13exclusions,22retained is bounded corpus accounting, not a prospective comprehensiveSR claim.'},
 {'item':'search_strategy','status':'INFO','reason':'20query supplement is dated bounded replay; original-session exclusion recoverability not established.'},
 {'item':'screening_AI_role','status':'INFO','reason':'Documented AI role and human gates, no asserted personal fulltext review.'},
 {'item':'extraction_traceability','status':'INFO','reason':'Current24rows and26contexts;7bounded locators15unavailable2metadata-only. This fresh semantic registry supersedes no historical protocol surface.'},
 {'item':'verification','status':'INFO','reason':'Identity, passage, math, reproduction checked separately; currentF01/F02/F03/F04 remain.'},
 {'item':'synthesis_bias_limits','status':'INFO','reason':'Historically weighted corpus and no general retraction/conflict/novelty clearance disclosed.'},
 {'item':'availability_reproducibility','status':'INFO','reason':'Historical stale inventory disclosed; no present archive/verifier/experiment completion inferred.'}],
 'non_SR_severity_cap':'PRISMA-derived reporting observations INFO; other_evidence_synthesis RAISE reporting gaps at mostWARN. This does NOT downgrade independently serious semantic/E6 findings.',
 'ethics_IRB':'NOT_APPLICABLE_BY_DECLARED_SCOPE','funding_and_competing_interests':'AUTHOR_DECLARATIONS_NOT_INDEPENDENTLY_VERIFIED',
 'compliance_checkpoint':'MANDATORY_AUTHOR_DECISION_REQUIRED; NO_AUTOMATIC_REVISION',
 'official_schema_validation':'NOT_RUN_BY_COMPONENT_ROOT_COORDINATES'}

report={'schema_version':'p31-round3-resume-semantic-audit-component/1.0','paper_id':'P31','audit_round':3,'status':'COMPONENT_COMPLETE_PENDING_ROOT_OFFICIAL_ASSEMBLY_AND_MANDATORY_AUTHOR_CHECKPOINT','current_draft':descriptor(DRAFT),'input_lock':descriptor(ROOT/LOCK),'resume_authority':descriptor(ROOT/'BATCH_ROUND10_STAGE4_5_ROUND3_RESUME_AUTHORIZATION.json'),'evidence_boundary':'Fresh semantic adjudication of current draft; already completed2026-09-05 raw queries reused at actual timestamps, not rerun or relabeled. Old verdicts never inherited. No manuscript, matrix, reader, canonical, science, Route or historical output changed. No official validator/build/replay executed by this component.','findings':findings,'phase_A':A,'phase_B':B,'phase_C':C,'phase_D':{'D1_units':D,'D1_scope':'69main-English blocks+7declarations+7future-list items+Chinese abstract;84selected units. One phrase per unit, not every sentence. Main source blocks contain multiple source paragraphs; this declared unit scope is not fullparagraph exhaustive originality clearance.','D2_same_author':{'held_carrier':supplement['shared_same_author_carrier'],'primary_surfaces':['Chaos primes article indexed primary sections','Period3 logistic/3x+1 primary article HTML'],'original_capture_events':[{'started_at':e['started_at'],'completed_at':e['completed_at'],'url':e['open_url']} for e in supplement['same_author_events']],'lexical_comparison_12_20_words':supplement['lexical_comparison'],'judgment':'No12or20word match in held normalized surfaces. Topics and mathematical objects differ; thematic use of dynamics/spectral vocabulary is not overlap evidence. Not entire-author-corpus, hidden-version, semantic-novelty or priority clearance.'},'overall':'BOUNDED_NO_SUBSTANTIVE_MATCH_IDENTIFIED_NOT_GLOBAL_ORIGINALITY_PASS'},'phase_E':{'E1_registry_claim_count':len(claims),'E1_semantic_method':'Full selected current semantic prose sentences/formal definitions/schema/list items indexed with exact UTF8 spans; finite lexical candidates supplemented separately. Historical8is not denominator. Sentence conjunctions preserve full context and compound claims; semantic classification is model-mediated, not keyword-derived truth.','E1_finite_lexical_candidate_count':lexical_count,'E2_E3_semantic_rows':semantic,'E4_internal_consistency':{'finding_ids':['P31-R3-F01','P31-R3-F02','P31-R3-F03'],'conditional_math':'Resolved-domain biconditional, delta totality versus owner closure, representative-invariantG/C and preserved incidence are logically coherent as conditional definitions; no theorem existence is proven.','evidence_propagation':'Metadata rows support identity/project labels only; bounded excerpts support context not full role; no unsupported source role is promoted to canonicalizer/owner result.'},'E5_discussion_conclusion_alignment':{'judgment':'MAIN_STATUS_ALIGNED_WITH_LOCAL_COMPARATIVE_DEFECT','reason':'Abstracts and conclusions retain no scientific execution, no novelty and A1-only. Discussionmost-demanding inheritsF02; current8completeness inheritsF01; no owner counts/Route promotion appears.'},'E6_operations':E6,'E6_counts':{'total':len(E6),'rounds':[11,20,13,8],'strength_drifted':1,'specific_author_disposition_required':1},'E6_advisory_only':'Field-relative rungs are semantic interpretation; this component does not auto-route, modify author text, or treat token conservation as proof.'},'seven_failure_modes':failure_modes,'compliance':compliance,'final_checkpoint':{'action':'STOP_FOR_AUTHOR_DISPOSITION_AFTER_ROOT_OFFICIAL_ASSEMBLY','automatic_correction':False,'stage5_or6_authorized':False,'new_scientific_execution_authorized':False,'route_state_changed':False,'formal_integrity_PASS':False}}
report['seven_failure_modes']=[
 {'mode':1,'name':'Implementation bug passing AI self-review','status':'CLEAR','evidence':['C1-population','C2-results','C4-intake'],'reason':'No P31 scientific implementation or experimental output exists. Only inherited P26 control fields are transcribed; neither those source computations nor a prospective solver is certified bug-free by this audit.'},
 {'mode':2,'name':'Hallucinated citation','status':'CLEAR','evidence':['phase_A','phase_B'],'reason':'No fabricated or presently miscited identity among24; current26uses are metadata or expressly bounded context, not full registered-role/P31 theorem transfer. General retraction/conflict clearance remains unknown.'},
 {'mode':3,'name':'Hallucinated experimental result','status':'CLEAR','evidence':['C2-results','B0006','B0091','B0099'],'reason':'Current draft denies P31 experiments, owner results and completed G/I/C. Counts are elementary arithmetic or explicitly inherited controls; no claimed P31 result requires an invented run.'},
 {'mode':4,'name':'Shortcut reliance','status':'CLEAR','evidence':['B0015','B0061','B0062','B0033'],'reason':'No learned model or scientific generalization result is reported. Current prose explicitly says byte agreement/coarse counts cannot certify semantic ownership. F02 remains an unsupported audit comparison, not evidence of a demonstrated shortcut-relying result.'},
 {'mode':5,'name':'Implementation bug reframed as novel insight','status':'CLEAR','evidence':['B0056','B0091','B0099'],'reason':'No P31 unexpected implementation outcome is narrated as novelty; design-level contribution is explicitly not a scientific result. Historical artifact errors are disclosed rather than minted as scientific findings.'},
 {'mode':6,'name':'Methodology fabrication','status':'SUSPECTED','evidence':['P31-R3-F01','B0042'],'reason':'Historical eight-entry ClaimIntent inventory is described as a complete set of current substantive article claims without a current semantic completeness basis. Other Methods passages retain the distinction between dated replay, unavailable original exclusions, and future work.'},
 {'mode':7,'name':'Frame-lock at early pipeline stage','status':'SUSPECTED','evidence':['P31-R3-F02','B0065','B0083'],'reason':'Foundational quadratic lock has been explicitly removed, but unsupported most-demanding language continues to privilege the9453table despite omitted self/reversal/triple/independent-semantic coverage. Author must resolve the current comparative framing; no automatic return or rewrite is authorized.'}
]
report['compliance']['RAISE']={
 'mode':'full','scope':'other_evidence_synthesis; full roles adapted to closed-corpus mathematical-methods synthesis',
 'principles':[
  {'id':1,'name':'Human oversight','status':'WARN','reason':'Responsible author and gate adjudication present. Reviewer count concerns four same-family AI roles, not independent human screeners; human qualifications/verification detail are not fully supplied. Evidence:B0041,B0101,B0108;F04 remains separate.'},
  {'id':2,'name':'Transparency','status':'WARN','reason':'Codex assistance and historical GPT5role separation disclosed; exact backend/full chronology/stagepromptparameter inventory remains explicitly unestablished. Evidence:B0107.'},
  {'id':3,'name':'Reproducibility','status':'WARN','reason':'repro_lock=null; no complete model/seed/prompt replay lock. Same-family limitations and unexecuted verifier are disclosed, historical reader inventory explicitly stale. Evidence:passport intake,B0056,B0079,B0105.'},
  {'id':4,'name':'Fit-for-purpose','status':'WARN','reason':'Task-specific synthesis/design/review roles described, but no per-tool independent performance validation/gold-standard study is supplied. No generic accuracy claim is inferred.'}],
 'roles':[
  {'role':1,'name':'Evidence Synthesists','attribution':'Liang Wang','status':'WARN','reason':'Responsibility and AI disclosure present; gate confirmation is not full-text attestation;F04 requires author disposition.'},
  {'role':2,'name':'AI Development Teams','attribution':'ARS tools and configured model provider','status':'INFO','reason':'ARS procedural self-declarations are tool context only; this manuscript does not independently validate development practices or model accuracy.'},
  {'role':3,'name':'Methodologists','attribution':'ARS procedural reviewer roles','status':'WARN','reason':'Same-family fresh-context review is documented but explicitly not independent scientific validation.'},
  {'role':4,'name':'Publishers of evidence synthesis','attribution':'No target publisher selected','status':'INFO','reason':'External stakeholder context; no journal policy conformance asserted.'},
  {'role':5,'name':'Users of evidence synthesis','attribution':'Future readers','status':'INFO','reason':'Source,execution,AI,archive andRoute limits disclosed for downstream interpretation; currentF01-F04 remain.'},
  {'role':6,'name':'Trainers of evidence synthesis methods','attribution':'Out of manuscript scope','status':'INFO','reason':'No training programme evaluated.'},
  {'role':7,'name':'Organisations producing evidence synthesis','attribution':'Out of manuscript scope','status':'INFO','reason':'No institutional responsible-AI governance audit claimed.'},
  {'role':8,'name':'Funders of evidence synthesis','attribution':'Author declares no funding','status':'INFO','reason':'Declaration retained; no independent funder verification or sustainability evaluation.'}]
}
report['compliance']['PRISMA_trAIce_adapted']=[
 {'item':'T1','name':'Title','tier':'Optional','status':'INFO','assessment':'AI not named in title. Optional reporting observation only; method architecture is not presented as anSR.'},
 {'item':'A1','name':'Abstract','tier':'Optional','status':'INFO','assessment':'Abstracts identify bounded synthesis/design but do not explicitly name anAItool and stage; AI disclosed later.'},
 {'item':'I1','name':'Introduction','tier':'Recommended','status':'INFO','assessment':'Introduction lacks a specific rationale for AItool choice; role separation later is procedural, not a validated justification.'},
 {'item':'R1','name':'Study selection AI-assisted','tier':'Mandatory_upstream_SR_only','status':'INFO','assessment':'44/9/35/13/22flow does not separate human versusAIhandled records. Human gates are not human screening counts; adapted non-SR reporting gap.'},
 {'item':'R2','name':'AI performance metrics','tier':'Mandatory_upstream_SR_only','status':'INFO','assessment':'No gold-standard sensitivity/agreementAIperformance result supplied. Four role opinions are not measuredAIaccuracy; absence is disclosed as a limit, not filled with invented metrics.'},
 {'item':'D1','name':'Limitations ofAIuse','tier':'Recommended','status':'INFO','assessment':'B0092 has three sentences on same-family dependence and author confirmations, withB0107/B0108bounded verification details; limitation present.'},
 {'item':'D2','name':'Implications ofAIuse','tier':'Optional','status':'INFO','assessment':'No specific forward-lookingAIusability reflection in discussion; optional adapted reporting observation.'}
]
report['phase_D']['D1_unquoted_supplement']={
 'artifact':descriptor(N/'stage4_5_round3_resume_p31_unquoted_originality_raw.json'),
 'query_count':84,'batch_count':21,
 'judgment':'All84same selected units received complementary unquoted keyword queries at actual2026-09-05timestamps. Inspected returned snippets contain generic software canonicalization/governance, elementary mathematical definitions, synthesis guidance and standard declarations. No substantive paraphrase-copying candidate identified; this is bounded snippet screening, not fulltext/corpus originality clearance.',
 'close_surface_distinctions':['Ambit governance/independent receipt replay concerns policy decisions, not orientedGamma0(11)primitive owners.','Aver certificate format concerns compilerWASMproof obligations; shared schema andfailclosed vocabulary is not substantive copied ownership content.','Arneth architectural basis article concerns abstract transport/interaction/closure/hierarchy process algebra; no frozen138/55owner-ledger result or corresponding passage identified.','Canonicalization-for-synthesis compiler paper concerns program equivalence; the general invariant principle is established common background, not a novelty claim here.','Clinical manuscript integrity-gate article concerns manuscript workflow automation; noP31mathematical method passage duplication identified.'],
 'scope_caveat':'Declared84units are selected blocks/declarations/listitems, not every individual source subparagraph. No novelty/priority clearance.'}
data={'registry':registry,'report':report}
component=sys.argv[1] if len(sys.argv)>1 else 'all'
if component=='registry':data=registry
elif component=='semantic':data=report['phase_E'].pop('E2_E3_semantic_rows')
elif component=='e6':data=report['phase_E'].pop('E6_operations')
elif component=='head':
    report['phase_E']['E2_E3_semantic_rows']=[]
    report['phase_E']['E6_operations']=[]
    data=report
print(json.dumps(data,ensure_ascii=False,separators=(',',':')))
