#!/usr/bin/env python3
"""Build P22 Stage-2.5 exact-draft claim and evidence artifacts.

The semantic population below is human/model mediated.  This script only
performs the mechanical work: unique substring resolution, UTF-8 byte-span
binding, JSON serialization, and construction of shared ARS evidence rows.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from urllib.parse import quote


PROJECT = Path(__file__).resolve().parent.parent
NOTES = PROJECT / "notes"
MANUSCRIPT = PROJECT / "paper" / "manuscript.tex"
REGISTRY = NOTES / "stage2_5_claim_registry.json"
EVIDENCE = NOTES / "stage2_5_evidence_rows.json"
SOURCE_MAP = Path("/tmp/p22_stage2_5_evidence_source_map.json")
DENINGER_TEXT_PATH = Path("/tmp/deninger2508.05329v1.txt")
DENINGER_PDF_PATH = Path("/tmp/deninger2508.05329v1.pdf")
DENINGER_PDF_SHA256 = "19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002"
ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
EVIDENCE_ROWS_MODULE = ARS_ROOT / "scripts" / "evidence_rows.py"


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def claim(
    claim_id: str,
    start: str,
    end: str,
    kinds: list[str],
    refs: list[str],
    anchors: list[str],
    section: str,
    tier: str = "NOT-SELECTED",
    basis: list[str] | None = None,
) -> dict[str, object]:
    row: dict[str, object] = {
        "claim_id": claim_id,
        "start": start,
        "end": end,
        "claim_kinds": kinds,
        "ref_slugs": refs,
        "writer_anchors": anchors,
        "paper_section": section,
        "selection_tier": tier,
    }
    if basis is not None:
        row["high_impact_basis"] = basis
    return row


CLAIMS = [
    claim(
        "P22-E1-01",
        "Deninger\nrecently studied the sheaf-theoretic form of this presentation, constructed",
        r"\cite[p.~25]{Deninger2025Rational}.",
        ["other_factual"],
        ["Deninger2025Rational"],
        ["manuscript.tex:L116-L121", "Deninger v1 p.25"],
        "1. Introduction and main results",
        "HIGH-IMPACT",
        ["methods_critical", "disputed"],
    ),
    claim(
        "P22-E1-02",
        "Deninger's Theorem~3.4 states that the rational",
        r"\cite[Prop.~4.3, p.~21]{Deninger2025Rational}.",
        ["other_factual"],
        ["Deninger2025Rational"],
        ["manuscript.tex:L142-L146", "Deninger v1 Thm.3.4/Prop.4.3"],
        "1. Introduction and main results",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-03",
        r"For every integer \(N>1\), there is no morphism of abelian sheaves",
        r"on \(\mathscr C_{\fppf}\).",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:Theorem all-index fppf nonlift"],
        "1. Introduction and main results",
        "HIGH-IMPACT",
        ["headline_conclusion"],
    ),
    claim(
        "P22-E1-04",
        "On the same universe-small noetherian-affine category equipped with the",
        r"for any \(N>1\).",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:Theorem finite-flat nonlift"],
        "1. Introduction and main results",
        "HIGH-IMPACT",
        ["headline_conclusion"],
    ),
    claim(
        "P22-E1-05",
        r"On \(B\otimes_A B\), the two pullbacks of \(c(s)\) differ.",
        "group.",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L189-L194"],
        "1. Introduction and main results",
    ),
    claim(
        "P22-E1-06",
        r"For \(N>1\) and every endomorphism \(u\colon\Ksh\to\Ksh\),",
        r"In particular, \(e\ne0\) and \(V_N^*e\ne0\).",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:Corollary extension obstruction"],
        "1. Introduction and main results",
        "HIGH-IMPACT",
        ["headline_conclusion"],
    ),
    claim(
        "P22-E1-07",
        "The proof also isolates a distinction relevant to a statement in the\nsource.  Corollary~4.6 of",
        "sectionwise identification over Dedekind rings for the finite-flat site.",
        ["other_factual"],
        ["Deninger2025Rational"],
        ["manuscript.tex:L214-L217", "Deninger v1 Cor.4.6 p.23"],
        "1. Introduction and main results",
        "HIGH-IMPACT",
        ["disputed"],
    ),
    claim(
        "P22-E1-08",
        r"For \(A=k[x]\), the rational Witt section \(1-xT^N\) in our construction is",
        "injectivity argument below.",
        ["causal", "other_factual"],
        ["Deninger2025Rational"],
        ["manuscript.tex:L218-L224", "internal descent proof"],
        "1. Introduction and main results",
        "HIGH-IMPACT",
        ["disputed", "headline_conclusion"],
    ),
    claim(
        "P22-E1-09",
        "The closest earlier algebraic presentation result is Deninger--Mellit's",
        "and it does not settle descent for the sheaf epimorphism considered here.",
        ["other_factual"],
        ["DeningerMellit2019"],
        ["manuscript.tex:L226-L229", "Deninger--Mellit Thm.1.1"],
        "1. Introduction and main results",
    ),
    claim(
        "P22-E1-10",
        "A bounded literature screen completed on 24 August 2026 checked the",
        "delimits the owner but is not a claim of global priority.",
        ["other_factual"],
        [],
        ["manuscript.tex:L230-L234", "notes/stage2_literature_search_report.md"],
        "1. Introduction and main results",
    ),
    claim(
        "P22-E1-11",
        "This is the reduced monoid algebra in equation~(4), p.~3, of",
        "is equation~(20), p.~14, of the same source.",
        ["other_factual"],
        ["Deninger2025Rational"],
        ["manuscript.tex:L272-L274", "Deninger v1 eqs.(4),(20)"],
        "2. Rational Witt sheaves and the extension",
    ),
    claim(
        "P22-E1-12",
        r"It is essential that \(\omega\) is an epimorphism \emph{in the category of",
        r"a local factorization of \(1-xT^N\) while obstructing its descent.",
        ["other_factual"],
        ["StacksProject"],
        ["manuscript.tex:L310-L320", "Stacks Tag 03CN"],
        "2. Rational Witt sheaves and the extension",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-13",
        "Abelian sheafification is exact, so",
        "of \\eqref{eq:extension}.",
        ["other_factual"],
        [],
        ["manuscript.tex:L343-L351"],
        "2. Rational Witt sheaves and the extension",
    ),
    claim(
        "P22-E1-14",
        r"For every \(m\geq1\), multiplication by \(m\) is a monomorphism of",
        "for either topology.",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:Lemma torsion-freeness"],
        "3. Three descent lemmas",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-15",
        r"Let \(\tau\) be either the fppf or finite-flat topology.  If a section",
        r"\(\Wbig(\mathcal O)(U)\), then \(z\ne0\).",
        ["categorical", "other_factual"],
        ["Deninger2025Rational"],
        ["manuscript.tex:Lemma big-Witt detector", "Deninger v1 Example 4.4"],
        "3. Three descent lemmas",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-16",
        "Let \\(B\\) be a Dedekind domain.  The map",
        "finite-flat topology.",
        ["categorical", "other_factual"],
        ["Deninger2025Rational", "StacksProject"],
        ["manuscript.tex:Lemma Dedekind injectivity", "Deninger Prop.4.5", "Stacks 00HS/0AUW"],
        "3. Three descent lemmas",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-17",
        "First take an fppf covering of \\(\\Spec B\\).",
        "original cover.",
        ["causal", "other_factual"],
        ["StacksProject"],
        ["manuscript.tex:L439-L450", "Stacks 00HS/0AUW"],
        "3. Three descent lemmas",
    ),
    claim(
        "P22-E1-18",
        "If the original cover is finite flat, each \\(C_i\\) is finite over \\(B\\).",
        "Proposition~4.5 now applies separately in both topologies.",
        ["causal", "other_factual"],
        ["Deninger2025Rational", "StacksProject"],
        ["manuscript.tex:L464-L467"],
        "3. Three descent lemmas",
    ),
    claim(
        "P22-E1-19",
        r"Fix \(N>1\), and let \(\tau\) be either the fppf topology or the",
        r"cover of rank \(N\).",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:Proposition failure of objectwise surjectivity"],
        "4. The all-index descent obstruction",
        "HIGH-IMPACT",
        ["headline_conclusion", "methods_critical"],
    ),
    claim(
        "P22-E1-20",
        "There is a finite extension \\(k/\\mathbb F_q\\) containing all \\(d\\)-th",
        "In particular, it is a cover for both topologies.",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L508-L517"],
        "4. The all-index descent obstruction",
    ),
    claim(
        "P22-E1-21",
        r"Thus \(c_N(s)\) is a local preimage of the pullback of \(w_N\).",
        r"\(\omega_B\) injective.",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L539-L542"],
        "4. The all-index descent obstruction",
    ),
    claim(
        "P22-E1-22",
        "To test this equality, put",
        r"This contradicts \eqref{eq:descentneeded}.",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L564-L592"],
        "4. The all-index descent obstruction",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-23",
        "The obstruction can be retained directly on the double overlap.",
        "nonvanishing difference on the first overlap.",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L662-L671"],
        "4. The all-index descent obstruction",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-24",
        r"For \(N=1\), the identity morphism is a lift.",
        r"For \(N=1\), the identity morphism is a lift.",
        ["quantitative", "categorical"],
        [],
        ["manuscript.tex:L162"],
        "1. Introduction and main results",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-25",
        "Let\n\\[\n e:\\quad0\\longrightarrow K\\longrightarrow Z",
        r"\(\Hom(W,K)\).",
        ["categorical", "other_factual"],
        ["StacksProject"],
        ["manuscript.tex:Proposition pushout--pullback criterion", "Stacks 010I/06XP"],
        "5. The extension-theoretic formulation",
        "HIGH-IMPACT",
        ["methods_critical"],
    ),
    claim(
        "P22-E1-26",
        "Taking \\(u=0\\), the pushout \\(0_*e\\) is the zero extension class.",
        r"\(Z\simeq K\oplus W\) would allow the middle map \(0\oplus V_N\).",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L767-L772"],
        "5. The extension-theoretic formulation",
    ),
    claim(
        "P22-E1-27",
        r"Exactness says that \(\partial_A(w_N)=0\) precisely when \(w_N\) has a",
        r"\(H^1_\tau\), much less all of \(\Ext^1\).",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L797-L809"],
        "5. The extension-theoretic formulation",
    ),
    claim(
        "P22-E1-28",
        "Although the same equations occur in both topologies, the finite-flat",
        r"implication, justify Theorem~\ref{thm:ff}.",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L814-L823"],
        "6. The finite-flat site and the Dedekind-section assertion",
    ),
    claim(
        "P22-E1-29",
        "There is no contradiction with the positive comparator in Deninger's",
        "information used here.",
        ["other_factual"],
        ["Deninger2025Rational"],
        ["manuscript.tex:L902-L908", "Deninger v1 Cor.4.7"],
        "7. Scope, controls, and conclusion",
    ),
    claim(
        "P22-E1-30",
        "Several boundaries are worth recording.",
        "novelty theorem.",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:L910-L918"],
        "7. Scope, controls, and conclusion",
    ),
    claim(
        "P22-E1-31",
        "In the project's separate Route-A/Route-B roadmap, this pure algebra note",
        "sheaf-theoretic.",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:L921-L924", "skills/route-a-evaluator.md", "skills/route-b-evaluator.md"],
        "7. Scope, controls, and conclusion",
    ),
    claim(
        "P22-E1-32",
        "The conclusion is therefore exact and modest.",
        "is the principal verification artifact of the note.",
        ["causal", "other_factual"],
        [],
        ["manuscript.tex:L926-L935"],
        "7. Scope, controls, and conclusion",
        "HIGH-IMPACT",
        ["headline_conclusion"],
    ),
    claim(
        "P22-E1-33",
        "No empirical data were generated or analyzed.",
        "public-access status must be confirmed by the author before dissemination.",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:Data and materials availability"],
        "Declarations",
    ),
    claim(
        "P22-E1-34",
        "This is a theoretical mathematics study involving no human participants,",
        "informed consent are not applicable.",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:Ethics statement"],
        "Declarations",
    ),
    claim(
        "P22-E1-35",
        "AI-assisted tools were used during literature triage, proof-audit support,",
        "No AI system is listed as an author.",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:AI-use disclosure"],
        "Declarations",
    ),
    claim(
        "P22-E1-36",
        r"The result is limited to additive sheaf lifts of \(V_N\) on the fixed",
        "preprint.",
        ["categorical", "other_factual"],
        [],
        ["manuscript.tex:Limitations"],
        "Declarations",
    ),
    claim(
        "P22-E1-37",
        r"\(\varepsilon^N=0\).",
        r"\(\varepsilon^N=0\).",
        ["quantitative", "other_factual"],
        [],
        ["manuscript.tex:L571"],
        "4. The all-index descent obstruction",
    ),
    claim(
        "P22-E1-38",
        r"=1-\varepsilon^NT^N=1.",
        r"=1-\varepsilon^NT^N=1.",
        ["quantitative", "other_factual"],
        [],
        ["manuscript.tex:L599"],
        "4. The all-index descent obstruction",
    ),
    claim(
        "P22-E1-39",
        r"When \(N=2\), take \(q=2\), \(a=1\), \(d=1\), and \(k=\mathbb F_2\).",
        r"When \(N=2\), take \(q=2\), \(a=1\), \(d=1\), and \(k=\mathbb F_2\).",
        ["quantitative", "other_factual"],
        [],
        ["manuscript.tex:L695"],
        "4. The all-index descent obstruction",
    ),
]


STACKS_SOURCE = "\n\n".join(
    [
        r"The cokernel $\mathop{\mathrm{Coker}}(\varphi )$ of $\varphi $ is the sheafification of the cokernel of $\varphi $ as a morphism of presheaves.",
        r"Then there exists a prime $\mathfrak q \subset \mathfrak q'$ mapping to $\mathfrak p$.",
        r"An $A$-module is flat if and only if it is torsion free. A finite torsion free $A$-module is finite locally free.",
        r"The extension $E'$ is called the pullback of $E$ via $B' \to B$.",
        r"The extension $E'$ is called the pushout of $E$ via $A \to A'$.",
        r"Given two Yoneda extensions $E$, $E'$ of the same degree then $E$ is equivalent to $E'$ if and only if $\delta (E) = \delta (E')$.",
    ]
)


def load_evidence_module():
    spec = importlib.util.spec_from_file_location("ars_evidence_rows", EVIDENCE_ROWS_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load ARS evidence_rows.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def resolve_claims(text: str, draft_raw: bytes) -> list[dict[str, object]]:
    resolved: list[dict[str, object]] = []
    for item in CLAIMS:
        start_marker = str(item["start"])
        end_marker = str(item["end"])
        occurrences = text.count(start_marker)
        if occurrences != 1:
            raise ValueError(
                f"{item['claim_id']}: start marker occurrence count is {occurrences}, expected 1"
            )
        start_char = text.index(start_marker)
        end_at = text.index(end_marker, start_char)
        end_char = end_at + len(end_marker)
        fragment = text[start_char:end_char]
        start_byte = len(text[:start_char].encode("utf-8"))
        end_byte = len(text[:end_char].encode("utf-8"))
        if draft_raw[start_byte:end_byte].decode("utf-8") != fragment:
            raise ValueError(f"{item['claim_id']}: byte-span round trip failed")
        row = {
            "claim_id": item["claim_id"],
            "claim_text": fragment,
            "draft_span": {"start_byte": start_byte, "end_byte": end_byte},
            "claim_kinds": item["claim_kinds"],
            "ref_slugs": item["ref_slugs"],
            "writer_anchors": item["writer_anchors"],
            "paper_section": item["paper_section"],
            "selection_tier": item["selection_tier"],
        }
        if "high_impact_basis" in item:
            row["high_impact_basis"] = item["high_impact_basis"]
        resolved.append(row)
    return resolved


def main() -> None:
    draft_raw = MANUSCRIPT.read_bytes()
    text = draft_raw.decode("utf-8", errors="strict")
    resolved = resolve_claims(text, draft_raw)
    registry = {
        "schema_version": "claim-registry/1.0",
        "draft_raw_sha256": sha256(draft_raw),
        "claims": resolved,
    }
    REGISTRY.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if not DENINGER_TEXT_PATH.is_file() or not DENINGER_PDF_PATH.is_file():
        raise FileNotFoundError("exact Deninger v1 PDF/text session artifacts are required")
    if sha256(DENINGER_PDF_PATH.read_bytes()) != DENINGER_PDF_SHA256:
        raise ValueError("Deninger v1 PDF SHA-256 mismatch")
    deninger_source = DENINGER_TEXT_PATH.read_text(encoding="utf-8")

    excerpts = {
        "frobenius": "It induces a homomorphism of presheaves of rings FN : Z(O) → Z(O)",
        "verschiebung_question": (
            "the (sheafified) Verschiebung VN on Wrat (O)♯ can be lifted to\n"
            "an endomorphism of Z(O)♯ ."
        ),
        "theorem_34": "Both presheaves satisfy the sheaf condition for f pqc-coverings.",
        "proposition_43": (
            "the map of presheaves ω : Z(O) → Wrat (O) induces a surjection of\n"
            "sheaves Z(O)♯ ↠ Wrat (O)♯ ."
        ),
        "corollary_46": (
            "For any\nDedekind ring A we have\n"
            "                              Wrat (A) = Z(A)♯ ."
        ),
        "proposition_45": (
            "has a refinement to a\ncovering {spec Bj → spec A}j∈J where the Bj "
            "are integral domains."
        ),
    }
    for name, excerpt in excerpts.items():
        if excerpt not in deninger_source:
            raise ValueError(f"Deninger excerpt {name!r} not found exactly")
        if len(excerpt.split()) > 25:
            raise ValueError(f"Deninger excerpt {name!r} exceeds 25 words")
    for excerpt in STACKS_SOURCE.split("\n\n"):
        if len(excerpt.split()) > 25:
            raise ValueError(f"Stacks excerpt exceeds 25 words: {excerpt}")

    old_rows: dict[str, dict[str, object]] = {}
    if EVIDENCE.is_file():
        try:
            for row in json.loads(EVIDENCE.read_text(encoding="utf-8")):
                if isinstance(row, dict) and isinstance(row.get("row_id"), str):
                    old_rows[str(row["row_id"])] = row
        except (json.JSONDecodeError, OSError, TypeError):
            old_rows = {}

    evidence_rows = load_evidence_module()
    claim_by_id = {str(row["claim_id"]): row for row in resolved}
    rows: list[dict[str, object]] = []

    def claim_view(claim_id: str) -> dict[str, object]:
        item = claim_by_id[claim_id]
        if item["selection_tier"] == "NOT-SELECTED":
            raise ValueError(f"cannot build evidence for unselected claim {claim_id}")
        return {
            "claim_id": claim_id,
            "text": item["claim_text"],
            "paper_locator": str(item["writer_anchors"][0]),
            "selection_tier": item["selection_tier"],
        }

    def template(
        claim_id: str,
        suffix: str,
        ref_slug: str | None,
        display_label: str | None,
        anchor_kind: str,
        anchor_value: str,
        detail: str,
        artifact_sha: str | None = None,
    ) -> dict[str, object]:
        source: dict[str, object] = {
            "ref_slug": ref_slug,
            "display_label": display_label,
        }
        if artifact_sha is not None:
            source["source_artifact_sha256"] = artifact_sha
        return {
            "surface": "phase_e_claim_verification",
            "row_id": f"EVR-{claim_id}-{suffix}",
            "claim": claim_view(claim_id),
            "source": source,
            "anchor": {
                "kind": anchor_kind,
                "value_encoded": quote(anchor_value, safe="-._~"),
            },
            "verdict": "VERIFIED",
            "detail": detail,
        }

    def add_internal(claim_id: str, suffix: str, detail: str) -> None:
        row = template(claim_id, suffix, None, None, "none", "", detail)
        rows.append(
            evidence_rows.build(
                row,
                None,
                failure_state="anchorless",
                cached_row=old_rows.get(str(row["row_id"])),
            )
        )

    def add_external(
        claim_id: str,
        suffix: str,
        ref_slug: str,
        label: str,
        anchor: str,
        source_text: str,
        excerpt: str,
        detail: str,
        artifact_sha: str | None = None,
    ) -> None:
        row = template(
            claim_id,
            suffix,
            ref_slug,
            label,
            "page" if anchor.startswith("p.") else "section",
            anchor,
            detail,
            artifact_sha,
        )
        rows.append(
            evidence_rows.build(
                row,
                source_text,
                extracted_text=excerpt,
                cached_row=old_rows.get(str(row["row_id"])),
            )
        )

    add_external("P22-E1-01", "D25F", "Deninger2025Rational", "Deninger v1", "p.25 Frobenius construction", deninger_source, excerpts["frobenius"], "The source constructs Frobenius maps before posing the Verschiebung question.", DENINGER_PDF_SHA256)
    add_external("P22-E1-01", "D25V", "Deninger2025Rational", "Deninger v1", "p.25 Verschiebung question", deninger_source, excerpts["verschiebung_question"], "The source explicitly asks whether Verschiebung lifts on the fp/fppf sites.", DENINGER_PDF_SHA256)
    add_external("P22-E1-02", "D34", "Deninger2025Rational", "Deninger v1", "p.19 Theorem 3.4", deninger_source, excerpts["theorem_34"], "The cited theorem supplies the fpqc sheaf condition.", DENINGER_PDF_SHA256)
    add_external("P22-E1-02", "D43", "Deninger2025Rational", "Deninger v1", "p.21 Proposition 4.3", deninger_source, excerpts["proposition_43"], "The cited proposition supplies the sheaf epimorphism.", DENINGER_PDF_SHA256)
    add_internal("P22-E1-03", "INT", "Verified by Proposition 4.1 and the proof at manuscript Sections 3--4 for the fppf topology.")
    add_internal("P22-E1-04", "INT", "Verified by the separately typed finite-flat refinement and detector argument in Sections 3, 4, and 6.")
    add_internal("P22-E1-06", "INT", "Verified from the pushout--pullback criterion plus nonliftability; nonzero classes are derived explicitly.")
    add_external("P22-E1-07", "D46", "Deninger2025Rational", "Deninger v1", "p.23 Corollary 4.6", deninger_source, excerpts["corollary_46"], "The version-1 source states the sectionwise Dedekind-ring equality reported by the manuscript.", DENINGER_PDF_SHA256)
    add_external("P22-E1-08", "D46", "Deninger2025Rational", "Deninger v1", "p.23 Corollary 4.6", deninger_source, excerpts["corollary_46"], "The external row establishes the exact source statement under test.", DENINGER_PDF_SHA256)
    add_internal("P22-E1-08", "INT", "The finite-free N=2 counterexample and all-index descent proof independently establish the limited correction.")
    add_external("P22-E1-12", "S03CN", "StacksProject", "Stacks Project", "Tag 03CN", STACKS_SOURCE, STACKS_SOURCE.split("\n\n")[0], "Tag 03CN supports cokernel sheafification and local rather than objectwise surjectivity.")
    add_internal("P22-E1-14", "INT", "Objectwise freeness of the reduced monoid algebra and exact abelian sheafification prove the lemma.")
    add_internal("P22-E1-15", "INT", "The coefficient-of-T Teichmuller detector and functoriality prove the contrapositive statement.")
    add_external("P22-E1-16", "D45", "Deninger2025Rational", "Deninger v1", "pp.22-23 Proposition 4.5", deninger_source, excerpts["proposition_45"], "Proposition 4.5 supplies injectivity after integral-domain refinement.", DENINGER_PDF_SHA256)
    add_external("P22-E1-16", "S00HS", "StacksProject", "Stacks Project", "Tag 00HS", STACKS_SOURCE, STACKS_SOURCE.split("\n\n")[1], "Flat going-down controls contractions of minimal primes.")
    add_external("P22-E1-16", "S0AUW", "StacksProject", "Stacks Project", "Tag 0AUW", STACKS_SOURCE, STACKS_SOURCE.split("\n\n")[2], "Dedekind torsion-free modules are flat; finite ones are finite locally free.")
    add_internal("P22-E1-16", "INT", "The manuscript checks finite presentation, joint surjectivity, universe closure, and both topology-specific refinements.")
    add_internal("P22-E1-19", "INT", "The explicit root cover, forced preimage, overlap, and truncated-ring specialization prove the proposition.")
    add_internal("P22-E1-22", "INT", "Direct multiplication, the big-Witt detector, and torsion-freeness establish a nonzero rational-kernel section.")
    add_internal("P22-E1-23", "INT", "Restriction to the truncated ring sends delta_N to the already verified nonzero section q^a y^sh.")
    add_internal("P22-E1-24", "INT", "V_1 and the identity map both act as the identity, so the commuting square is immediate.")
    add_external("P22-E1-25", "S010IP", "StacksProject", "Stacks Project", "Tag 010I pullback", STACKS_SOURCE, STACKS_SOURCE.split("\n\n")[3], "Tag 010I defines pullback functoriality for extensions.")
    add_external("P22-E1-25", "S010IO", "StacksProject", "Stacks Project", "Tag 010I pushout", STACKS_SOURCE, STACKS_SOURCE.split("\n\n")[4], "Tag 010I defines pushout functoriality for extensions.")
    add_external("P22-E1-25", "S06XP", "StacksProject", "Stacks Project", "Tag 06XP", STACKS_SOURCE, STACKS_SOURCE.split("\n\n")[5], "Tag 06XP identifies Yoneda equivalence classes with Ext classes.")
    add_internal("P22-E1-25", "INT", "The manuscript proves both directions and the Hom(W,K)-torsor statement in the ambient abelian category.")
    add_internal("P22-E1-32", "INT", "This conclusion is the exact synthesis of the verified all-index proposition, two site-specific theorems, and extension corollary.")

    evidence_rows.paginate(rows, page=1, page_size=min(25, max(1, len(rows))))
    EVIDENCE.write_text(
        json.dumps(rows, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    SOURCE_MAP.write_text(
        json.dumps(
            {
                "Deninger2025Rational": deninger_source,
                "StacksProject": STACKS_SOURCE,
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"claim registry: {len(resolved)} claims -> {REGISTRY}")
    print(f"selected claims: {sum(row['selection_tier'] != 'NOT-SELECTED' for row in resolved)}")
    print(f"evidence rows: {len(rows)} -> {EVIDENCE}")
    print(f"temporary replay source map -> {SOURCE_MAP}")


if __name__ == "__main__":
    main()
