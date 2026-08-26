#!/usr/bin/env python3
"""Build P22 Stage-4.5 Round-2 exact-draft claim and evidence artifacts.

The claim population and source-to-claim comparisons are semantic/model-mediated.
This script performs the bounded mechanical work: resolve unique substrings, bind
UTF-8 byte spans, validate the closed Claim Registry shape, and build replayable
ARS evidence rows from explicitly held source text.  It does not establish semantic
extraction completeness or mathematical truth.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from urllib.parse import quote

from jsonschema import Draft202012Validator


PROJECT = Path(__file__).resolve().parent.parent
NOTES = PROJECT / "notes"
MANUSCRIPT = PROJECT / "paper" / "manuscript.tex"
REGISTRY = NOTES / "stage4_5_round2_claim_registry.json"
EVIDENCE = NOTES / "stage4_5_round2_evidence_rows.json"
SOURCE_MAP = Path("/tmp/p22_stage4_5_round2_evidence_source_map.json")
DENINGER_TEXT = Path("/tmp/deninger2508.05329v1.txt")
DENINGER_PDF = Path("/tmp/deninger2508.05329v1.pdf")
DM_TEXT = Path("/tmp/p22-stage45-deninger-mellit-2019.txt")
DM_PDF = Path("/tmp/p22-stage45-deninger-mellit-2019.pdf")
DENINGER_PDF_SHA256 = "19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002"
DM_PDF_SHA256 = "458e81abf5933a09db7d48b3e422256eee8fe75f26d530a756f5b4420d0aeb65"
ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
BASE_BUILDER = NOTES / "stage2_5_build_evidence_artifacts.py"
EVIDENCE_ROWS_MODULE = ARS_ROOT / "scripts" / "evidence_rows.py"
REGISTRY_SCHEMA = ARS_ROOT / "shared/contracts/evidence/claim_registry.schema.json"


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_module("p22_stage2_5_builder", BASE_BUILDER)
evidence_rows = load_module("ars_evidence_rows_stage45", EVIDENCE_ROWS_MODULE)


def claim(
    claim_id: str,
    start: str,
    end: str,
    kinds: list[str],
    refs: list[str],
    anchors: list[str],
    section: str,
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
        "selection_tier": "ALL",
    }
    if basis:
        row["high_impact_basis"] = basis
    return row


DROP_IDS = {
    "P22-E1-06",
    "P22-E1-09",
    "P22-E1-10",
    "P22-E1-31",
    "P22-E1-32",
}
CLAIMS: list[dict[str, object]] = []
for old in base.CLAIMS:
    if old["claim_id"] in DROP_IDS:
        continue
    current = copy.deepcopy(old)
    if current["claim_id"] == "P22-E1-33":
        current["end"] = "this draft are available from the author upon reasonable request."
    current["selection_tier"] = "ALL"
    CLAIMS.append(current)

CLAIMS.extend(
    [
        claim(
            "P22-E1-06",
            r"For \(\tau\in\{\fppf,\ff\}\), \(N>1\), and every endomorphism",
            r"\(\tau\).",
            ["categorical", "other_factual"],
            [],
            ["Corollary extension obstruction"],
            "1. Introduction and main results",
            ["headline_conclusion"],
        ),
        claim(
            "P22-E1-09A",
            "The exact source is Deninger's version-1 preprint.",
            r"\cite[Cor.~4.7, p.~24]{Deninger2025Rational}.",
            ["other_factual"],
            ["Deninger2025Rational"],
            ["Deninger v1 Props.4.3/4.5 and Cor.4.7"],
            "1. Introduction and main results",
        ),
        claim(
            "P22-E1-09B",
            "The closest earlier\nalgebraic presentation result is Deninger--Mellit's explicit kernel",
            "and it does not treat sheafification or finite-flat/fppf descent.",
            ["other_factual"],
            ["DeningerMellit2019"],
            ["Deninger--Mellit Thm.1.1"],
            "1. Introduction and main results",
        ),
        claim(
            "P22-E1-09C",
            "The\nStacks references used below supply general local-exactness and",
            "or obstruction.",
            ["other_factual"],
            ["StacksProject"],
            ["Stacks Tags 03CN/010I/06XP"],
            "1. Introduction and main results",
        ),
        claim(
            "P22-E1-10",
            "A bounded update completed on 25 August 2026 searched the current arXiv",
            "This bounded negative result is not a claim of global priority.",
            ["categorical", "other_factual"],
            [],
            ["notes/stage4_rev001_research.md"],
            "1. Introduction and main results",
            ["disputed"],
        ),
        claim(
            "P22-E1-40",
            "Our contribution is correspondingly narrow:",
            "or a ring endomorphism.",
            ["categorical", "other_factual"],
            [],
            ["Contribution-boundary paragraph"],
            "1. Introduction and main results",
            ["headline_conclusion"],
        ),
        claim(
            "P22-E1-41",
            "The proof isolates a reusable descent-obstruction template.",
            "by itself imply these Ext inequalities.",
            ["causal", "categorical", "other_factual"],
            [],
            ["Reusable descent template"],
            "1. Introduction and main results",
            ["causal", "methods_critical"],
        ),
        claim(
            "P22-E1-42",
            r"In the present argument, \(p=\omega\), \(z_0=(x)^\sh\),",
            "reusable categorical core.",
            ["causal", "other_factual"],
            [],
            ["Template instantiation"],
            "1. Introduction and main results",
            ["methods_critical"],
        ),
        claim(
            "P22-E1-32",
            "The conclusion is therefore exact and modest.",
            r"\(\tau\in\{\fppf,\ff\}\), gives \(V_N^*e_\tau\ne0\).",
            ["causal", "categorical", "other_factual"],
            [],
            ["Conclusion theorem synthesis"],
            "7. Scope, controls, and conclusion",
            ["headline_conclusion", "causal"],
        ),
        claim(
            "P22-E1-43",
            "The reusable mechanism is the conditional implication from a selected",
            "principal verification artifact of the note.",
            ["causal", "categorical", "other_factual"],
            [],
            ["Conclusion mechanism inventory"],
            "7. Scope, controls, and conclusion",
            ["headline_conclusion", "methods_critical"],
        ),
        claim(
            "P22-E1-44",
            r"\author{Liang Wang\textsuperscript{1}\\",
            r"\small Contact: \texttt{wangliang.f@gmail.com}}",
            ["categorical", "other_factual"],
            [],
            ["Confirmed author metadata event"],
            "Title block",
        ),
        claim(
            "P22-E1-45",
            "Liang Wang conceived the study, developed and verified the proofs,",
            "and wrote and revised the manuscript.",
            ["categorical", "other_factual"],
            [],
            ["Confirmed contribution event"],
            "Declarations",
        ),
        claim(
            "P22-E1-46",
            "The author received no specific funding for this work.",
            "The author received no specific funding for this work.",
            ["categorical", "other_factual"],
            [],
            ["Confirmed funding event"],
            "Declarations",
        ),
        claim(
            "P22-E1-47",
            "The author declares no competing interests.",
            "The author declares no competing interests.",
            ["categorical", "other_factual"],
            [],
            ["Confirmed competing-interests event"],
            "Declarations",
        ),
        claim(
            "P22-E1-48",
            r"\date{Draft of 25 August 2026}",
            r"\date{Draft of 25 August 2026}",
            ["categorical", "other_factual"],
            [],
            ["Title-block draft date; Stage3-prime NEW-1 input"],
            "Title block",
        ),
    ]
)


STACKS_SOURCE = base.STACKS_SOURCE


def resolve_claims(text: str, draft_raw: bytes) -> list[dict[str, object]]:
    resolved: list[dict[str, object]] = []
    seen_spans: set[tuple[int, int]] = set()
    for item in CLAIMS:
        start_marker = str(item["start"])
        end_marker = str(item["end"])
        occurrences = text.count(start_marker)
        if occurrences != 1:
            raise ValueError(
                f"{item['claim_id']}: start marker occurrence count {occurrences}, expected 1"
            )
        start_char = text.index(start_marker)
        end_at = text.index(end_marker, start_char)
        end_char = end_at + len(end_marker)
        fragment = text[start_char:end_char]
        start_byte = len(text[:start_char].encode("utf-8"))
        end_byte = len(text[:end_char].encode("utf-8"))
        if draft_raw[start_byte:end_byte].decode("utf-8") != fragment:
            raise ValueError(f"{item['claim_id']}: byte-span round trip failed")
        span = (start_byte, end_byte)
        if span in seen_spans:
            raise ValueError(f"{item['claim_id']}: duplicate claim span {span}")
        seen_spans.add(span)
        start_line = text.count("\n", 0, start_char) + 1
        end_line = text.count("\n", 0, end_char) + 1
        source_anchors = [
            str(anchor)
            for anchor in item["writer_anchors"]
            if not str(anchor).startswith("manuscript.tex:L")
        ]
        row = {
            "claim_id": item["claim_id"],
            "claim_text": fragment,
            "draft_span": {"start_byte": start_byte, "end_byte": end_byte},
            "claim_kinds": item["claim_kinds"],
            "ref_slugs": item["ref_slugs"],
            "writer_anchors": [f"manuscript.tex:L{start_line}-L{end_line}", *source_anchors],
            "paper_section": item["paper_section"],
            "selection_tier": "ALL",
        }
        if "high_impact_basis" in item:
            row["high_impact_basis"] = item["high_impact_basis"]
        if len(fragment) > 2000:
            raise ValueError(f"{item['claim_id']}: claim text exceeds evidence-row limit")
        resolved.append(row)
    return resolved


def source_spec(
    code: str,
    ref_slug: str,
    label: str,
    anchor: str,
    source_key: str,
    excerpt: str,
    detail: str,
    artifact_sha256: str | None,
) -> dict[str, object]:
    return {
        "code": code,
        "ref_slug": ref_slug,
        "label": label,
        "anchor": anchor,
        "source_key": source_key,
        "excerpt": excerpt,
        "detail": detail,
        "artifact_sha256": artifact_sha256,
    }


SPECS: dict[str, list[dict[str, object]]] = {
    "P22-E1-01": [
        source_spec("D25F", "Deninger2025Rational", "Deninger v1", "p.25 Frobenius construction", "deninger", "It induces a homomorphism of presheaves of rings FN : Z(O) → Z(O)", "The source constructs Frobenius maps before posing the Verschiebung question.", DENINGER_PDF_SHA256),
        source_spec("D25V", "Deninger2025Rational", "Deninger v1", "p.25 Verschiebung question", "deninger", "the (sheafified) Verschiebung VN on Wrat (O)♯ can be lifted to\nan endomorphism of Z(O)♯ .", "The source explicitly asks whether Verschiebung lifts on the fp/fppf sites.", DENINGER_PDF_SHA256),
    ],
    "P22-E1-02": [
        source_spec("D34", "Deninger2025Rational", "Deninger v1", "p.19 Theorem 3.4", "deninger", "Both presheaves satisfy the sheaf condition for f pqc-coverings.", "The cited theorem supplies the fpqc sheaf condition.", DENINGER_PDF_SHA256),
        source_spec("D43", "Deninger2025Rational", "Deninger v1", "p.21 Proposition 4.3", "deninger", "the map of presheaves ω : Z(O) → Wrat (O) induces a surjection of\nsheaves Z(O)♯ ↠ Wrat (O)♯ .", "The cited proposition supplies the sheaf epimorphism.", DENINGER_PDF_SHA256),
    ],
    "P22-E1-07": [
        source_spec("D46", "Deninger2025Rational", "Deninger v1", "p.23 Corollary 4.6", "deninger", "For any\nDedekind ring A we have\n                              Wrat (A) = Z(A)♯ .", "The source states the sectionwise Dedekind-ring equality reported by the manuscript.", DENINGER_PDF_SHA256),
    ],
    "P22-E1-08": [
        source_spec("D46", "Deninger2025Rational", "Deninger v1", "p.23 Corollary 4.6", "deninger", "For any\nDedekind ring A we have\n                              Wrat (A) = Z(A)♯ .", "The external row establishes the exact statement independently tested by the paper.", DENINGER_PDF_SHA256),
    ],
    "P22-E1-09A": [
        source_spec("D43", "Deninger2025Rational", "Deninger v1", "p.21 Proposition 4.3", "deninger", "the map of presheaves ω : Z(O) → Wrat (O) induces a surjection of\nsheaves Z(O)♯ ↠ Wrat (O)♯ .", "Proposition 4.3 supplies local preimages through sheaf epimorphy.", DENINGER_PDF_SHA256),
        source_spec("D45", "Deninger2025Rational", "Deninger v1", "pp.22-23 Proposition 4.5", "deninger", "has a refinement to a\ncovering {spec Bj → spec A}j∈J where the Bj are integral domains.", "Proposition 4.5 supplies the conditional injectivity criterion.", DENINGER_PDF_SHA256),
        source_spec("D47", "Deninger2025Rational", "Deninger v1", "p.24 Corollary 4.7", "deninger", "the map Z(O)♯ → Wrat (O)♯ is an isomorphism of ring sheaves.", "Corollary 4.7 is the stated positive comparison on finer topologies.", DENINGER_PDF_SHA256),
    ],
    "P22-E1-09B": [
        source_spec("DM11A", "DeningerMellit2019", "Deninger--Mellit 2019", "p.94 Theorem 1.1", "dm", "Theorem 1.1. Consider the unique (special)", "The closest paper contains the cited explicit kernel theorem for its localized/truncated owner.", DM_PDF_SHA256),
        source_spec("DM11B", "DeningerMellit2019", "Deninger--Mellit 2019", "p.93 abstract and p.94 theorem formula", "dm", "we give some results on the kernel of the natural map from", "The article and its Theorem 1.1 concern a kernel formula for the truncated S-Witt map, not sheaf descent.", DM_PDF_SHA256),
    ],
    "P22-E1-09C": [
        source_spec("S03CN", "StacksProject", "Stacks Project", "Tag 03CN", "stacks", STACKS_SOURCE.split("\n\n")[0], "Tag 03CN supplies general sheaf exactness formalism.", None),
        source_spec("S010I", "StacksProject", "Stacks Project", "Tag 010I", "stacks", STACKS_SOURCE.split("\n\n")[3], "Tag 010I supplies extension pullback formalism.", None),
        source_spec("S06XP", "StacksProject", "Stacks Project", "Tag 06XP", "stacks", STACKS_SOURCE.split("\n\n")[5], "Tag 06XP supplies Yoneda/Ext equivalence formalism.", None),
    ],
    "P22-E1-11": [
        source_spec("D04", "Deninger2025Rational", "Deninger v1", "p.3 equation (4)", "deninger", "factors over Wrat (A) and induces a functorial ring homomorphism", "Equation (4) is the reduced monoid-algebra-to-rational-Witt morphism.", DENINGER_PDF_SHA256),
        source_spec("D20", "Deninger2025Rational", "Deninger v1", "p.14 equation (20)", "deninger", "VN (f )(T ) = f (T N ) .", "Equation (20) supplies the displayed Verschiebung substitution formula.", DENINGER_PDF_SHA256),
    ],
    "P22-E1-12": [source_spec("S03CN", "StacksProject", "Stacks Project", "Tag 03CN", "stacks", STACKS_SOURCE.split("\n\n")[0], "Tag 03CN supports cokernel sheafification and local exactness.", None)],
    "P22-E1-15": [source_spec("D44", "Deninger2025Rational", "Deninger v1", "p.22 Example 4.4", "deninger", "Example 4.4 For A = F2 [ε], ε2 = 0 and any subcanonical topology on NoethAffSch", "Example 4.4 supplies the nilpotent noninjectivity control used by the detector discussion.", DENINGER_PDF_SHA256)],
    "P22-E1-16": [
        source_spec("D45", "Deninger2025Rational", "Deninger v1", "pp.22-23 Proposition 4.5", "deninger", "has a refinement to a\ncovering {spec Bj → spec A}j∈J where the Bj are integral domains.", "Proposition 4.5 supplies injectivity after integral-domain refinement.", DENINGER_PDF_SHA256),
        source_spec("S00HS", "StacksProject", "Stacks Project", "Tag 00HS", "stacks", STACKS_SOURCE.split("\n\n")[1], "Flat going-down controls contractions of minimal primes.", None),
        source_spec("S0AUW", "StacksProject", "Stacks Project", "Tag 0AUW", "stacks", STACKS_SOURCE.split("\n\n")[2], "Dedekind torsion-free modules are flat; finite ones are finite locally free.", None),
    ],
    "P22-E1-17": [
        source_spec("S00HS", "StacksProject", "Stacks Project", "Tag 00HS", "stacks", STACKS_SOURCE.split("\n\n")[1], "Flat going-down supplies the minimal-prime contraction used in the refinement.", None),
        source_spec("S0AUW", "StacksProject", "Stacks Project", "Tag 0AUW", "stacks", STACKS_SOURCE.split("\n\n")[2], "The Dedekind torsion-free criterion supplies flatness of the quotient.", None),
    ],
    "P22-E1-18": [
        source_spec("D45", "Deninger2025Rational", "Deninger v1", "pp.22-23 Proposition 4.5", "deninger", "has a refinement to a\ncovering {spec Bj → spec A}j∈J where the Bj are integral domains.", "The source injectivity criterion applies after the manuscript's refinement.", DENINGER_PDF_SHA256),
        source_spec("S0AUW", "StacksProject", "Stacks Project", "Tag 0AUW", "stacks", STACKS_SOURCE.split("\n\n")[2], "Finite torsion-free modules over the Dedekind base are finite locally free.", None),
    ],
    "P22-E1-25": [
        source_spec("S010IP", "StacksProject", "Stacks Project", "Tag 010I pullback", "stacks", STACKS_SOURCE.split("\n\n")[3], "Tag 010I defines pullback functoriality for extensions.", None),
        source_spec("S010IO", "StacksProject", "Stacks Project", "Tag 010I pushout", "stacks", STACKS_SOURCE.split("\n\n")[4], "Tag 010I defines pushout functoriality for extensions.", None),
        source_spec("S06XP", "StacksProject", "Stacks Project", "Tag 06XP", "stacks", STACKS_SOURCE.split("\n\n")[5], "Tag 06XP identifies Yoneda equivalence classes with Ext classes.", None),
    ],
    "P22-E1-29": [source_spec("D47", "Deninger2025Rational", "Deninger v1", "p.24 Corollary 4.7", "deninger", "the map Z(O)♯ → Wrat (O)♯ is an isomorphism of ring sheaves.", "The source positive comparator is accurately bounded to finer topologies.", DENINGER_PDF_SHA256)],
}


def build() -> None:
    draft_raw = MANUSCRIPT.read_bytes()
    text = draft_raw.decode("utf-8", errors="strict")
    resolved = resolve_claims(text, draft_raw)
    registry = {
        "schema_version": "claim-registry/1.0",
        "draft_raw_sha256": sha256(draft_raw),
        "claims": resolved,
    }
    schema = json.loads(REGISTRY_SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(registry)
    REGISTRY.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    for path, expected in ((DENINGER_PDF, DENINGER_PDF_SHA256), (DM_PDF, DM_PDF_SHA256)):
        if not path.is_file() or sha256(path.read_bytes()) != expected:
            raise ValueError(f"source artifact absent or stale: {path}")
    sources = {
        "deninger": DENINGER_TEXT.read_text(encoding="utf-8"),
        "dm": DM_TEXT.read_text(encoding="utf-8"),
        "stacks": STACKS_SOURCE,
    }

    claim_by_id = {str(row["claim_id"]): row for row in resolved}
    rows: list[dict[str, object]] = []

    def template(item: dict[str, object], row_id: str, spec: dict[str, object] | None) -> dict[str, object]:
        source: dict[str, object]
        anchor_kind = "none"
        anchor_value = ""
        detail = "Verified against the manuscript's explicit proof/declaration and the frozen local audit chain."
        if spec is None:
            source = {"ref_slug": None, "display_label": None}
        else:
            source = {
                "ref_slug": spec["ref_slug"],
                "display_label": spec["label"],
            }
            if spec["artifact_sha256"] is not None:
                source["source_artifact_sha256"] = spec["artifact_sha256"]
            anchor_value = str(spec["anchor"])
            anchor_kind = "page" if anchor_value.startswith("p.") else "section"
            detail = str(spec["detail"])
        return {
            "surface": "phase_e_claim_verification",
            "row_id": row_id,
            "claim": {
                "claim_id": item["claim_id"],
                "text": item["claim_text"],
                "paper_locator": item["writer_anchors"][0],
                "selection_tier": "ALL",
            },
            "source": source,
            "anchor": {"kind": anchor_kind, "value_encoded": quote(anchor_value, safe="-._~")},
            "verdict": "VERIFIED",
            "detail": detail,
        }

    for item in resolved:
        claim_id = str(item["claim_id"])
        specs = SPECS.get(claim_id, [])
        expected_refs = set(item["ref_slugs"])
        actual_refs = {str(spec["ref_slug"]) for spec in specs}
        if expected_refs != actual_refs:
            raise ValueError(
                f"{claim_id}: evidence ref coverage mismatch expected={expected_refs} actual={actual_refs}"
            )
        if not specs:
            draft = template(item, f"EVR-{claim_id}-INT", None)
            rows.append(evidence_rows.build(draft, None, failure_state="anchorless"))
            continue
        for spec in specs:
            source_text = sources[str(spec["source_key"])]
            excerpt = str(spec["excerpt"])
            if excerpt not in source_text:
                raise ValueError(f"{claim_id}/{spec['code']}: exact excerpt not in session source")
            if len(excerpt.split()) > 25:
                raise ValueError(f"{claim_id}/{spec['code']}: excerpt exceeds 25 words")
            draft = template(item, f"EVR-{claim_id}-{spec['code']}", spec)
            rows.append(evidence_rows.build(draft, source_text, extracted_text=excerpt))

    evidence_rows.paginate(rows, page=1, page_size=min(25, max(1, len(rows))))
    EVIDENCE.write_text(
        json.dumps(rows, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    SOURCE_MAP.write_text(
        json.dumps(
            {
                "Deninger2025Rational": sources["deninger"],
                "DeningerMellit2019": sources["dm"],
                "StacksProject": sources["stacks"],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"claim registry: {len(resolved)} ALL claims -> {REGISTRY}")
    print(f"evidence rows: {len(rows)} -> {EVIDENCE}")
    print(f"temporary replay source map -> {SOURCE_MAP}")


if __name__ == "__main__":
    build()
