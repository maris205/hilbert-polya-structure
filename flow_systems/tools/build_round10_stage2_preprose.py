#!/usr/bin/env python3
"""Build Round-10 Stage-2 pre-prose artifacts from frozen Stage-1 inputs.

This builder is intentionally closed-corpus and deterministic.  It creates no
manuscript prose, performs no retrieval, and never mutates Stage-1 artifacts.
"""

from __future__ import annotations

import json
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-09-02T13:29:43Z"

PAPERS = {
    "P29": {
        "slug": "29-bianchi-ideal-owner-refinement",
        "suffix": "29d2",
        "title": "A Fail-Closed Certificate Architecture for Literal Gaussian-Prime-Ideal Ownership in a Level-(3) Bianchi Flow",
        "target": 4500,
        "question": "Under the deliberately strict literal Gaussian-prime-ideal codomain, what must be certified before a performance-independently registered owner mechanism can be evaluated on a certified finite primitive-unoriented owner population?",
        "thesis": "Mechanism admissibility under the strict codomain and exact primitive-unoriented quotient completeness are separate fail-closed gates, and neither may be selected or repaired by downstream collision performance.",
        "subarguments": [
            "The frozen corpus identifies the Bianchi object and relevant vocabularies but supplies no project-specific owner law.",
            "The literal one-ideal codomain is a deliberate stress-test frame rather than a canonical arithmetic output.",
            "Gate M and Gate Q are non-entailing design obligations and require different certificates.",
            "Performance is interpretable only after both gates close; no score is available in this study.",
        ],
    },
    "P30": {
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "suffix": "30d2",
        "title": "A Falsifiable Certificate Architecture for a Physical-Roof Determinant in the Equilateral Three-Disk Flow",
        "target": 4800,
        "question": "What object, operator, coefficient, error, fidelity, and nontransfer certificates are required before a determinant computation for the no-eclipse three-disk flow at d=6a can be interpreted as a physical-roof result?",
        "thesis": "A physical-roof determinant claim requires six typed gates and a common-norm error contract with four numerical components plus separately propagated geometry and roof-input uncertainty.",
        "subarguments": [
            "Physical, symbolic, semiclassical, exact-quantum, and classical-transfer determinants are differently typed objects.",
            "A consistently typed roof may pass an internal determinant calibration without establishing physical fidelity.",
            "The numerical error ledger is incomplete unless input uncertainty, stability, propagation, and conditioning are explicit.",
            "Livsic-type nontransfer reasoning is directional and cannot be inferred from finite agreement.",
        ],
    },
    "P31": {
        "slug": "31-level11-conjugacy-owner-ledger",
        "suffix": "31d2",
        "title": "Canonicalization Before Quadratic Audit: A Certificate-Methods Architecture for an Oriented Level-11 Owner Ledger",
        "target": 4600,
        "question": "Which exact canonicalization and certificate interfaces must precede any pairwise audit of the frozen oriented level-11 owner ledger?",
        "thesis": "The primary target is a replayable canonicalization biconditional; the 9,453-row table is only a derived adversarial audit, and global owners, incidences, and cells remain distinct estimands.",
        "subarguments": [
            "Owner identity requires a deterministic canonical form with an if-and-only-if specification.",
            "Positive and negative conjugacy decisions need separately typed certificates and replay semantics.",
            "The all-pairs table cannot repair an absent canonicalizer and cannot define pair truth by itself.",
            "G, I, and C must remain distinct outputs; aggregate counts do not substitute for owner identity.",
        ],
    },
    "P32": {
        "slug": "32-homology-cover-renormalization-uniformity",
        "suffix": "32d2",
        "title": "Falsification Before Uniformity: Higher- and Zero-Content Tests for Pure Genus-Two Homology-Cover Renormalization",
        "target": 4800,
        "question": "Do the frozen time and multiplicity normalizations survive the higher-content and zero-content local-factor tests required before compact-uniform analysis of the pure genus-two homology-cover tower?",
        "thesis": "Higher-content and zero-content local factors are the first falsification targets; content one is exceptional and contingent, while the formal object and analytic tail remain unresolved.",
        "subarguments": [
            "The pure homology-cover tower, all content classes, and the two exact normalizations must remain fixed.",
            "Higher content tests whether the proposed factor scales beyond the exceptional content-one case.",
            "Zero content requires a separately typed formal object and cannot be absorbed into the positive-content formula.",
            "Compact-uniform convergence and tail control are conditional on local survival and currently remain open.",
        ],
    },
    "P33": {
        "slug": "33-bolza-control-matched-census",
        "suffix": "33d2",
        "title": "Interoperable Certificate Design for Primitive Geodesic Ownership on Two Frozen Genus-Two Surfaces",
        "target": 5000,
        "question": "How can two surface-specific exact proof producers emit one semantic owner-certificate schema for independent validation under a frozen target-blind cutoff?",
        "thesis": "Surface-specific internal proof systems may differ while sharing a common semantic certificate and independent validator; the frozen cutoff makes the scientific workload asymmetric and leaves the census gate open.",
        "subarguments": [
            "Exact proof producers may be heterogeneous because the two surfaces have different available representations.",
            "Interoperability belongs at the semantic certificate layer rather than in a forced shared internal solver.",
            "The independent validator must check full-group conjugacy, roots, inversion pairing, and population accounting.",
            "The frozen cutoff yields an inherited-empty target side and nontrivial control side; P33-RC-1 remains 0/7.",
        ],
    },
}


WRITER_DIMS = [
    ("D1", "section_completeness", "Every approved section will be written, and no material-gap placeholder will remain in the canonical draft."),
    ("D2", "citation_density", "Every literature-dependent factual statement will cite only the frozen corpus; no locator or quotation will be invented."),
    ("D3", "argument_blueprint_fidelity", "Each section will preserve the registered thesis, evidence boundary, counterargument, and paper-specific prohibited upgrades."),
    ("D4", "total_word_count", "The audited English body will remain within ten percent of the declared target and inside the batch range of 4,000--6,500 words."),
    ("D5", "per_section_word_count", "Section proportions will follow the inherited Stage-1 architecture, with no section displaced by more than fifteen percent without a recorded reason."),
    ("D6", "paragraph_structure", "Paragraphs will use claim, evidence, explanation, and transition where appropriate, while mathematical method sections may use their natural procedural form."),
    ("D7", "register_consistency", "The manuscript will use precise mathematical prose, preserve hedges and evidence labels, and avoid promotional or Route-inflating language."),
]

EVALUATOR_DIMS = [
    ("D1", "originality", "Look for a bounded certificate-methods contribution that is differentiated without a novelty claim.", "Block if the draft claims an unperformed theorem, mechanism, census, determinant, or novelty result.", "Warn if the methods contribution is present but weakly separated from the surrounding literature."),
    ("D2", "methodological_rigor", "Look for the exact frozen object, clock, owners, stop states, and prospective certificate interfaces.", "Block if the design changes the frozen system or reports an unexecuted gate as closed.", "Warn if a prospective interface lacks enough detail for later deterministic implementation."),
    ("D3", "evidence_sufficiency", "Look for closed-corpus citations, explicit anchor-none limitations, and no unsupported upgrade from metadata to theorem support.", "Block if core claims exceed the frozen evidence or if a source/locator/result is invented.", "Warn if a secondary contextual statement is insufficiently bounded or a special source restriction is missing."),
    ("D4", "argument_coherence", "Look for alignment among the conditional question, architecture, findings, limitations, and conclusion.", "Block if the conclusion claims a result that the methods and findings do not establish.", "Warn if transitions blur distinct gates, objects, or estimands."),
    ("D5", "writing_quality", "Look for precise mathematical register, clean LaTeX, complete declarations, and consistent plainnat citations.", "Block if prose is materially unclear or the manuscript has unresolved citations, missing sections, or compilation failures.", "Warn if several paragraphs are repetitive, promotional, or typographically inconsistent."),
]


def bounded_text(text: str) -> str:
    replacements = {
        "The report's contribution": "The article's contribution",
        "the report's contribution": "the article's contribution",
        "Phase-6 report revision": "Stage-2 manuscript composition",
        "Phase-6 report": "Stage-2 manuscript",
        "Phase-6 revision": "Stage-2 manuscript composition",
        "Phase 6": "Stage 2",
        "canonical manuscript authorization": "scientific-result refresh",
        "canonical manuscript result": "canonical scientific-result refresh",
        "canonical files unchanged": "canonical scientific-result artifacts unchanged",
        "canonical manuscript/result bytes unchanged": "canonical scientific-result artifacts unchanged",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_manifest(code: str, cfg: dict[str, object], notes: Path) -> None:
    parent_path = notes / "stage1_phase6_claim_intent_manifest.json"
    parent_bytes = parent_path.read_bytes()
    parent_sha256 = hashlib.sha256(parent_bytes).hexdigest()
    parent = json.loads(parent_bytes.decode("utf-8"))
    claims = []
    lineage = []
    for index, source in enumerate(parent["claims"], 1):
        claim_id = f"C-{index:03d}"
        claim = {
            "claim_id": claim_id,
            "claim_text": bounded_text(source["claim_text"]),
            "intended_evidence_kind": source["intended_evidence_kind"],
            "planned_refs": source["planned_refs"],
            "negative_constraints": [],
        }
        for j, nc in enumerate(source.get("negative_constraints", []), 1):
            claim["negative_constraints"].append(
                {"constraint_id": f"NC-C{index:03d}-{j}", "rule": bounded_text(nc["rule"])}
            )
        if not claim["negative_constraints"]:
            claim.pop("negative_constraints")
        claims.append(claim)
        lineage.append(
            {
                "stage2_claim_id": claim_id,
                "parent_claim_id": source["claim_id"],
                "parent_manifest_sha256": parent_sha256,
                "strength_relation": "same_or_narrower",
                "parent_claim_text": source["claim_text"],
            }
        )
    global_constraints = []
    for index, nc in enumerate(parent["manifest_negative_constraints"], 1):
        rule = bounded_text(nc["rule"])
        if "canonical scientific-result artifacts unchanged" in rule:
            rule = (
                "Preserve canonical scientific-result artifacts and route state; Stage-2 edits are limited to the "
                "authorized manuscript, bibliography, PDF, and supporting writing/audit documents."
            )
        global_constraints.append({"constraint_id": f"MNC-{index}", "rule": rule})
    manifest = {
        "manifest_version": "1.0",
        "manifest_id": f"M-2026-09-02T13:29:43Z-{cfg['suffix']}",
        "emitted_by": "draft_writer_agent",
        "emitted_at": STAMP,
        "session_id": "round10-stage2-write",
        "claims": claims,
        "manifest_negative_constraints": global_constraints,
    }
    write_json(notes / "stage2_claim_intent_manifest.json", manifest)
    write_json(
        notes / "stage2_claim_lineage.json",
        {
            "schema": "round10-stage2-claim-lineage/1.0",
            "paper": code,
            "stage2_manifest_id": manifest["manifest_id"],
            "parent_manifest_id": parent["manifest_id"],
            "mapping_policy": "one_to_one_same_or_narrower",
            "mappings": lineage,
        },
    )


def build_configuration(code: str, cfg: dict[str, object], notes: Path) -> None:
    text = f"""# {code} -- Stage 2 Paper Configuration Record

| Parameter | Value |
|---|---|
| Topic | {cfg['title']} |
| Research Question | {cfg['question']} |
| Paper Type | theoretical / certificate-methods mathematics article |
| Discipline | dynamical systems; arithmetic geometry; computational mathematics |
| Target Journal | General; no venue-specific conformance claimed |
| Citation Format | natbib with plainnat numeric output |
| Output Format | LaTeX source, closed BibTeX, compiled PDF |
| Body Language | English |
| Abstract | independently composed English and Traditional Chinese |
| Word Count Target | {cfg['target']} English body words |
| Existing Materials | complete Stage-1 closed-corpus research package and Phase-6 report |
| Co-Authors | single author: Liang Wang |
| Funding | no funding |
| Style Profile | null |
| Domain Evidence Profile | unknown_user_defined; corpus already frozen |
| Citation Verification | advisory in Stage 2; mandatory Stage 2.5 not run |
| Retraction Policy | mark only; not checked in Stage 2 |
| Experiment Intake | no experiments declared for this evidence-synthesis manuscript |
| Operational Mode | full, Stage 2 WRITE |

`criteria_binding_unavailable`: no venue/track/type target was declared, so no
venue-alignment claim is made. The user's Stage-2 confirmation accepts the
inherited Phase-6 structure as the writing outline; no new research scope is
authorized.
"""
    (notes / "stage2_paper_configuration.md").write_text(text, encoding="utf-8")


def build_outline(code: str, cfg: dict[str, object], notes: Path) -> None:
    target = int(cfg["target"])
    rows = [
        ("Introduction, question, and boundary", 0.12),
        ("Frozen literature and theoretical frame", 0.25),
        ("Executed closed-corpus methodology", 0.10),
        ("Certificate/proof-method architecture", 0.23),
        ("Evidence-synthesis findings", 0.08),
        ("Reproducibility and prospective interface", 0.08),
        ("Discussion and Route interpretation", 0.07),
        ("Limitations and future work", 0.05),
        ("Conclusion", 0.02),
    ]
    lines = [
        f"# {code} -- Stage 2 Paper Outline",
        "",
        "**Structure pattern:** theoretical / certificate-methods article with an explicit executed-method boundary.",
        "",
        f"**Overview:** {cfg['thesis']}",
        "",
        "The outline is inherited from the user-confirmed Stage-1 Phase-6 report. Every section uses only its frozen source assignments and preserves the paper-specific prohibited upgrades.",
        "",
        "| Section | Purpose | Target words | Evidence role |",
        "|---|---|---:|---|",
    ]
    for name, proportion in rows:
        purpose = "Frame and bound the conditional contribution" if name.startswith("Introduction") else "Carry the corresponding frozen Phase-6 section without claim strengthening"
        evidence = "frozen corpus / Stage-1 artifacts / definitional boundary"
        lines.append(f"| {name} | {purpose} | {round(target * proportion)} | {evidence} |")
    lines.extend(
        [
            "",
            "## Evidence map",
            "",
            "Every planned reference in `stage2_claim_intent_manifest.json` maps to the same-or-narrower Stage-2 claim descended from the corresponding Phase-6 claim. No unassigned or new source is permitted.",
            "",
            "## Transition logic",
            "",
            "Object and evidence boundaries lead to the executed method; the executed method licenses only the certificate architecture and bounded synthesis findings; findings lead to prospective interfaces, limitations, and a non-promotional Route conclusion.",
            "",
            "`criteria_binding_unavailable`",
        ]
    )
    (notes / "stage2_paper_outline.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_argument(code: str, cfg: dict[str, object], notes: Path) -> None:
    lines = [
        f"# {code} -- Stage 2 Argument Blueprint",
        "",
        "## Central thesis",
        "",
        str(cfg["thesis"]),
        "",
        "## Sub-arguments",
        "",
    ]
    for index, arg in enumerate(cfg["subarguments"], 1):
        lines.extend(
            [
                f"### Sub-argument {index}",
                "",
                f"- **Claim:** {arg}",
                "- **Evidence:** the exact planned-reference set of the corresponding Stage-2 ClaimIntent row and the frozen Stage-1 artifacts.",
                "- **Reasoning:** the source boundary licenses a design/certificate conclusion only; it does not license execution or Route promotion.",
                "- **Strongest counterargument:** an adjacent theorem, algorithm, or successful finite check may appear to close more of the interface.",
                "- **Response:** require exact hypothesis transfer, object typing, positive/negative certificate coverage, and a separately authorized execution before stronger wording.",
                "",
            ]
        )
    lines.extend(
        [
            "## Logical flow",
            "",
            "Conditional question -> frozen object and corpus -> executed evidence-synthesis method -> fail-closed architecture -> bounded findings -> prospective implementation -> limitations -> unchanged Route state.",
            "",
            "## Draft-writer notes",
            "",
            "Use precise active prose; keep all architecture interfaces prospective; preserve `anchor:none` and `INCONCLUSIVE`; do not use a positive verb such as proves, computes, establishes, completes, or certifies for an unexecuted scientific interface.",
        ]
    )
    (notes / "stage2_argument_blueprint.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_writer_precommitment(code: str, cfg: dict[str, object], notes: Path) -> None:
    lines = [
        "## Acceptance Criteria Paraphrase",
        "",
        f"Paper metadata only: {cfg['title']} | field=dynamical systems/arithmetic geometry | target_words={cfg['target']}.",
        "",
    ]
    for dim, name, paragraph in WRITER_DIMS:
        lines.extend([f"### {dim}: {name}", "", paragraph, ""])
    lines.append("[PRE-COMMITMENT-ACKNOWLEDGED]")
    (notes / "stage2_writer_precommitment.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_evaluator_precommitment(code: str, cfg: dict[str, object], notes: Path) -> None:
    lines = [
        "## Contract Paraphrase",
        "",
        f"Paper metadata only: {cfg['title']} | field=dynamical systems/arithmetic geometry | target_words={cfg['target']}.",
        "",
    ]
    for dim, name, look, block, warn in EVALUATOR_DIMS:
        lines.extend([f"### {dim}: {name}", "", f"The evaluator will judge {name.replace('_', ' ')} against the frozen research-design article contract without treating venue fit as scientific validity.", ""])
    lines.extend(["## Scoring Plan", ""])
    for dim, name, look, block, warn in EVALUATOR_DIMS:
        lines.extend(
            [
                f"### {dim}: {name}",
                f"dimension_id: {dim}",
                f"what_to_look_for: {look}",
                f"what_triggers_block: {block}",
                f"what_triggers_warn: {warn}",
                "",
            ]
        )
    lines.extend(["criteria_binding_unavailable", "[PRE-COMMITMENT-ACKNOWLEDGED]"])
    (notes / "stage2_evaluator_precommitment.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    for code, cfg in PAPERS.items():
        notes = ROOT / "papers" / str(cfg["slug"]) / "notes"
        build_manifest(code, cfg, notes)
        build_configuration(code, cfg, notes)
        build_outline(code, cfg, notes)
        build_argument(code, cfg, notes)
        build_writer_precommitment(code, cfg, notes)
        build_evaluator_precommitment(code, cfg, notes)


if __name__ == "__main__":
    main()
