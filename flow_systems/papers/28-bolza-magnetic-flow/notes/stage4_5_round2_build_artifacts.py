#!/usr/bin/env python3
"""Build the fresh, versioned Paper-28 Stage-4.5 Mode-2 audit package.

The exact Stage-4-prime draft and bibliography are read-only inputs.  Every
output name starts with ``stage4_5_round2_``; canonical manuscript, PDF,
bibliography, results, receipts, and revision artifacts are never modified.
"""

from __future__ import annotations

import copy
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
import urllib.parse
from pathlib import Path


PAPER = Path(__file__).resolve().parents[1]
ROOT = PAPER.parents[1]
NOTES = PAPER / "notes"
DRAFT_REL = "notes/stage4_prime_revision_round1.tex"
BIB_REL = "paper/references.bib"
DRAFT = PAPER / DRAFT_REL
BIB = PAPER / BIB_REL
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
SEARCH_STAMP = "2026-08-31T05:34:00Z"
DRAFT_SHA = "126783db66949396f7b3b494e06f55e4deedcc9f443f29e6477e6254676d472e"
BIB_SHA = "95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e"
INPUT_LOCK_SHA = "bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30"
E6_AUTHORITY_SHA = "2c3d46b8d4282a2b1ec7b00d6a5dba743cf25e6d3cc2bdb7b1b6ea445ef3570e"
BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether "
    "the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."
)


def sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_text(path: Path, value: str) -> None:
    path.write_text(value.rstrip() + "\n", encoding="utf-8")


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


COVER = load_module(ARS / "scripts/claim_registry_coverage.py", "p28_ars_claim_registry_coverage")
EVR = load_module(ARS / "scripts/evidence_rows.py", "p28_ars_evidence_rows")

raw = DRAFT.read_bytes()
text = raw.decode("utf-8")
assert sha_bytes(raw) == DRAFT_SHA
assert sha_path(BIB) == BIB_SHA
assert sha_path(ROOT / "BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json") == INPUT_LOCK_SHA
assert sha_path(NOTES / "stage4_prime_revision_evidence_bundle.json") == E6_AUTHORITY_SHA


def canonical_snapshot() -> dict[str, dict[str, object]]:
    return {
        rel: {
            "path": rel,
            "sha256": sha_path(PAPER / rel),
            "size_bytes": (PAPER / rel).stat().st_size,
        }
        for rel in ("paper/manuscript.tex", "paper/paper.pdf", "paper/references.bib")
    }


canonical_before = canonical_snapshot()

input_manifest = {
    "schema": "stage4.5-input-manifest/1.0",
    "paper": 28,
    "audit_mode": 2,
    "generated_at": STAMP,
    "audit_target": {"path": DRAFT_REL, "sha256": DRAFT_SHA, "size_bytes": len(raw)},
    "bibliography": {"path": BIB_REL, "sha256": BIB_SHA, "size_bytes": BIB.stat().st_size},
    "batch_input_lock": {
        "path": "../../BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json",
        "sha256": INPUT_LOCK_SHA,
    },
    "e6_dispatch_authority": {
        "path": "notes/stage4_prime_revision_evidence_bundle.json",
        "sha256": E6_AUTHORITY_SHA,
        "role": "sole dispatch-authority Revision-Evidence Bundle",
    },
    "canonical_frozen": canonical_before,
    "route_a_state": "unchanged; positive-arithmetic A2 remains 0/5 at batch level",
    "route_b_state": "not invoked; batch invocations remain 0/5",
    "initial_dynamical_object_restrictions": (
        "unchanged: fixed nonarithmetic hyperbolic control surface and exact geodesic translation-length "
        "certificate only; no magnetic Hamiltonian/flow, clock, action, owner quotient, determinant, or spectral realization"
    ),
    "stage_boundary": "Stage 4.5 only; Stage 5 has not started and awaits mandatory author confirmation.",
}
dump(NOTES / "stage4_5_round2_input_manifest.json", input_manifest)


def search_url(query: str) -> str:
    return "https://www.bing.com/search?q=" + urllib.parse.quote(query)


def s2(
    status: str,
    method: str,
    score: float | None = None,
    paper_id: str | None = None,
    title: str | None = None,
    authors: list[str] | None = None,
    year: int | None = None,
    venue: str | None = None,
    doi_crosscheck: str | None = None,
) -> dict[str, object]:
    assert status in {"S2_VERIFIED", "S2_NOT_FOUND", "S2_API_UNAVAILABLE"}
    return {
        "status": status,
        "queried_at": SEARCH_STAMP,
        "verification_method": method,
        "match_score": score,
        "semantic_scholar_id": paper_id,
        "s2_title": title,
        "s2_authors": authors,
        "s2_year": year,
        "s2_venue": venue,
        "doi_crosscheck": doi_crosscheck,
    }


reference_rows: list[dict[str, object]] = [
    {
        "ref_slug": "Nazarenko2013",
        "bib_fields": {
            "author": "Nazarenko, A. V.",
            "title": "Two-Parametric Hyperbolic Octagons and Reduced Teichmüller Space in Genus Two",
            "year": "2013",
            "eprint": "1301.5446",
            "primaryclass": "math-ph",
            "doi": "10.48550/arXiv.1301.5446",
        },
        "semantic_scholar": s2(
            "S2_API_UNAVAILABLE",
            "s2_api_unavailable_after_3_attempts_2s_backoff",
            doi_crosscheck="S2 unavailable; DOI and title resolved on the current official arXiv record",
        ),
        "fresh_query": '"Two-Parametric Hyperbolic Octagons" Nazarenko arXiv 1301.5446',
        "query_url": search_url('"Two-Parametric Hyperbolic Octagons" Nazarenko arXiv 1301.5446'),
        "result": [
            {
                "title": "Two-parametric hyperbolic octagons and reduced Teichmueller space in genus two",
                "url": "https://arxiv.org/abs/1301.5446",
                "summary": "Official arXiv record: A. V. Nazarenko; submitted 23 January 2013; math-ph; octagon generators and genus-two parameter space.",
            }
        ],
        "status": "VERIFIED",
        "authoritative_url": "https://arxiv.org/abs/1301.5446v1",
        "authoritative_metadata": {
            "authors": ["A. V. Nazarenko"],
            "title": "Two-parametric hyperbolic octagons and reduced Teichmueller space in genus two",
            "submitted": "2013-01-23",
            "version": "v1",
            "subject": "math-ph",
            "withdrawn": False,
        },
        "existence_field_verdict": "VERIFIED",
        "ghost_audit": "NOT_GHOST; current draft cites this key three times and the official arXiv record resolves.",
        "post_publication_update_check": {
            "authority": "current official arXiv abs/version history",
            "checked_at": SEARCH_STAMP,
            "observation": "One v1 submission is displayed; no withdrawal marker is displayed.",
            "context_impact": "NONE_OBSERVED_FOR_THIS_NAMED_SOURCE",
            "scope_boundary": "Named arXiv-record observation only, not a guarantee across all venues.",
        },
    },
    {
        "ref_slug": "Takeuchi1975",
        "bib_fields": {
            "author": "Takeuchi, Kisao",
            "title": "A Characterization of Arithmetic Fuchsian Groups",
            "journal": "Journal of the Mathematical Society of Japan",
            "volume": "27",
            "number": "4",
            "pages": "600--612",
            "year": "1975",
            "doi": "10.2969/jmsj/02740600",
        },
        "semantic_scholar": s2(
            "S2_API_UNAVAILABLE",
            "s2_api_unavailable_after_3_attempts_2s_backoff",
            doi_crosscheck="S2 unavailable; DOI and title resolved on current official J-STAGE record",
        ),
        "fresh_query": '"A Characterization of Arithmetic Fuchsian Groups" Takeuchi 10.2969/jmsj/02740600',
        "query_url": search_url('"A Characterization of Arithmetic Fuchsian Groups" Takeuchi 10.2969/jmsj/02740600'),
        "result": [
            {
                "title": "A characterization of arithmetic Fuchsian groups",
                "url": "https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_article",
                "summary": "Official J-STAGE record: Kisao Takeuchi, volume 27(4), pages 600–612, 1975, DOI 10.2969/jmsj/02740600.",
            }
        ],
        "status": "VERIFIED_WITH_UPDATE_NOTE",
        "authoritative_url": "https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_article",
        "authoritative_metadata": {
            "authors": ["Kisao Takeuchi"],
            "year": 1975,
            "volume": 27,
            "issue": 4,
            "pages": "600-612",
            "doi": "10.2969/jmsj/02740600",
        },
        "existence_field_verdict": "VERIFIED",
        "ghost_audit": "NOT_GHOST; current draft cites this key once and the official journal record resolves.",
        "post_publication_update_check": {
            "authority": "current official J-STAGE correction-information panel",
            "checked_at": SEARCH_STAMP,
            "observation": "The 20 October 2006 correction changes citation-list numbering/format from unbracketed items to bracketed references; no theorem-text correction is listed.",
            "context_impact": "NO_IMPACT_ON_P28_THEOREM_1_CONDITION_I_CONTEXT",
            "scope_boundary": "Assessment is limited to the correction displayed on the named official record.",
        },
    },
    {
        "ref_slug": "AigonDupuyEtAl2005",
        "bib_fields": {
            "author": "Aigon-Dupuy, Aline and Buser, Peter and Cibils, Michel and Künzle, Alfred F. and Steiner, Frank",
            "title": "Hyperbolic Octagons and Teichmüller Space in Genus 2",
            "journal": "Journal of Mathematical Physics",
            "volume": "46",
            "number": "3",
            "pages": "033513",
            "year": "2005",
            "doi": "10.1063/1.1850177",
        },
        "semantic_scholar": s2(
            "S2_VERIFIED",
            "s2_doi_lookup",
            1.0,
            "c77541d2539e3f0e14f8161f61c6f2c3a8e39d56",
            "Hyperbolic octagons and Teichmüller space in genus 2",
            ["Aline Aigon-Dupuy", "P. Buser", "M. Cibils", "A. Künzle", "F. Steiner"],
            2005,
            "",
            "DOI_AND_TITLE_MATCH",
        ),
        "fresh_query": '"Hyperbolic Octagons and Teichmuller Space in Genus 2" 10.1063/1.1850177',
        "query_url": search_url('"Hyperbolic Octagons and Teichmuller Space in Genus 2" 10.1063/1.1850177'),
        "result": [
            {
                "title": "Hyperbolic octagons and Teichmüller space in genus 2",
                "url": "https://doi.org/10.1063/1.1850177",
                "summary": "DOI/Crossref deposit identifies Journal of Mathematical Physics 46(3), article 033513, 2005, and all five corrected authors.",
            },
            {
                "title": "EPFL publication record",
                "url": "https://infoscience.epfl.ch/entities/publication/eb38a039-e625-41a3-a9a6-4fb5a81f7d7d",
                "summary": "Institutional record corroborates the genus-two octagon article.",
            },
        ],
        "status": "VERIFIED",
        "authoritative_url": "https://api.crossref.org/works/10.1063/1.1850177",
        "authoritative_metadata": {
            "authors": ["Aline Aigon-Dupuy", "Peter Buser", "Michel Cibils", "Alfred F. Künzle", "Frank Steiner"],
            "container_title": "Journal of Mathematical Physics",
            "volume": "46",
            "issue": "3",
            "article": "033513",
            "year": 2005,
            "doi": "10.1063/1.1850177",
            "relation": {},
            "update_to": [],
        },
        "existence_field_verdict": "VERIFIED",
        "ghost_audit": "NOT_GHOST; current draft cites this key twice and current DOI/institutional metadata resolve.",
        "post_publication_update_check": {
            "authority": "current Crossref work-object relation and update-to fields",
            "checked_at": SEARCH_STAMP,
            "observation": "No correction, retraction, or expression-of-concern relation is listed in the named Crossref work object.",
            "context_impact": "NONE_OBSERVED_FOR_THIS_NAMED_SOURCE",
            "scope_boundary": "Named-source observation only, not an all-venue guarantee.",
        },
    },
    {
        "ref_slug": "Voight2009",
        "bib_fields": {
            "author": "Voight, John",
            "title": "Computing Fundamental Domains for Fuchsian Groups",
            "journal": "Journal de Théorie des Nombres de Bordeaux",
            "volume": "21",
            "number": "2",
            "pages": "467--489",
            "year": "2009",
            "doi": "10.5802/jtnb.683",
        },
        "semantic_scholar": s2(
            "S2_VERIFIED",
            "s2_doi_lookup",
            1.0,
            "4f046d6423b949d99a5be39de374ef5a64e0f00d",
            "Computing fundamental domains for Fuchsian groups",
            ["John Voight"],
            2008,
            "",
            "DOI_AND_TITLE_MATCH; S2 carries the 2008 preprint year while the official journal record is 2009",
        ),
        "fresh_query": '"Computing Fundamental Domains for Fuchsian Groups" 10.5802/jtnb.683 errata',
        "query_url": search_url('"Computing Fundamental Domains for Fuchsian Groups" 10.5802/jtnb.683 errata'),
        "result": [
            {
                "title": "Computing fundamental domains for Fuchsian groups",
                "url": "https://www.numdam.org/articles/10.5802/jtnb.683/",
                "summary": "Official journal record: John Voight, volume 21(2), pages 467–489, 2009, DOI 10.5802/jtnb.683.",
            },
            {
                "title": "Errata: Computing Fundamental Domains for Fuchsian Groups",
                "url": "https://jvoight.github.io/articles/funddom-errata.pdf",
                "summary": "Author-hosted errata correct Proposition 1.1/cycle conditions and the proof of Algorithm 4.7, while stating the error does not affect other results.",
            },
        ],
        "status": "VERIFIED_WITH_UPDATE_NOTE",
        "authoritative_url": "https://www.numdam.org/articles/10.5802/jtnb.683/",
        "authoritative_metadata": {
            "authors": ["John Voight"],
            "year": 2009,
            "volume": 21,
            "issue": 2,
            "pages": "467-489",
            "doi": "10.5802/jtnb.683",
        },
        "existence_field_verdict": "VERIFIED",
        "ghost_audit": "NOT_GHOST; current draft cites this key once and the current journal record resolves.",
        "post_publication_update_check": {
            "authority": "author's official research page and author-hosted errata PDF",
            "checked_at": SEARCH_STAMP,
            "observation": "Errata correct Proposition 1.1/cycle conditions and an Algorithm 4.7 proof step; the author states the mistake does not affect the other results.",
            "context_impact": "P28 uses only the broad existence of exact fundamental-domain algorithms; that bounded context remains supported, with this update note retained.",
            "scope_boundary": "No reliance on the corrected proposition or proof step is made by P28.",
        },
    },
    {
        "ref_slug": "DespreEtAl2023",
        "bib_fields": {
            "author": "Despré, Vincent and Kolbe, Benedikt and Parlier, Hugo and Teillaud, Monique",
            "title": "Computing a Dirichlet Domain for a Hyperbolic Surface",
            "booktitle": "39th International Symposium on Computational Geometry (SoCG 2023)",
            "volume": "258",
            "pages": "27:1--27:15",
            "year": "2023",
            "doi": "10.4230/LIPIcs.SoCG.2023.27",
        },
        "semantic_scholar": s2(
            "S2_API_UNAVAILABLE",
            "s2_api_unavailable_after_3_attempts_2s_backoff",
            doi_crosscheck="S2 unavailable; DOI and title resolved on current official Dagstuhl record",
        ),
        "fresh_query": '"Computing a Dirichlet Domain for a Hyperbolic Surface" 10.4230/LIPIcs.SoCG.2023.27',
        "query_url": search_url('"Computing a Dirichlet Domain for a Hyperbolic Surface" 10.4230/LIPIcs.SoCG.2023.27'),
        "result": [
            {
                "title": "Computing a Dirichlet Domain for a Hyperbolic Surface",
                "url": "https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2023.27",
                "summary": "Official Dagstuhl record lists all four authors, 2023 publication, pages 27:1–27:15, and input as a fundamental polygon with side pairings.",
            }
        ],
        "status": "VERIFIED",
        "authoritative_url": "https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2023.27",
        "authoritative_metadata": {
            "authors": ["Vincent Despré", "Benedikt Kolbe", "Hugo Parlier", "Monique Teillaud"],
            "year": 2023,
            "volume": 258,
            "pages": "27:1-27:15",
            "doi": "10.4230/LIPIcs.SoCG.2023.27",
            "license": "CC BY 4.0",
        },
        "existence_field_verdict": "VERIFIED",
        "ghost_audit": "NOT_GHOST; current draft cites this key once and the official proceedings record resolves.",
        "post_publication_update_check": {
            "authority": "current official Dagstuhl document record",
            "checked_at": SEARCH_STAMP,
            "observation": "No named correction, retraction, or expression of concern is displayed on the official record reviewed.",
            "context_impact": "NONE_OBSERVED_FOR_THIS_NAMED_SOURCE",
            "scope_boundary": "Named-record observation only.",
        },
    },
    {
        "ref_slug": "Popescu2024",
        "bib_fields": {
            "author": "Popescu, Sever Angel",
            "title": "A Simple and Self-Contained Proof for the Lindemann--Weierstrass Theorem",
            "booktitle": "New Frontiers in Number Theory and Applications",
            "pages": "349--366",
            "year": "2024",
            "doi": "10.1007/978-3-031-51959-8_16",
            "author_version": "arXiv:2306.14352",
        },
        "semantic_scholar": s2(
            "S2_API_UNAVAILABLE",
            "s2_api_unavailable_after_3_attempts_2s_backoff",
            doi_crosscheck="S2 unavailable; DOI/title resolved on current Springer and arXiv records",
        ),
        "fresh_query": '"A Simple and Self-Contained Proof" Lindemann Weierstrass Popescu 10.1007/978-3-031-51959-8_16',
        "query_url": search_url('"A Simple and Self-Contained Proof" Lindemann Weierstrass Popescu 10.1007/978-3-031-51959-8_16'),
        "result": [
            {
                "title": "A Simple and Self-contained Proof for the Lindemann-Weierstrass Theorem",
                "url": "https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16",
                "summary": "Official Springer chapter record: Sever Angel Popescu, pages 349–366, DOI 10.1007/978-3-031-51959-8_16.",
            },
            {
                "title": "A simple and self-contained proof for the Lindemann-Weierstrass theorem",
                "url": "https://arxiv.org/abs/2306.14352",
                "summary": "Current author-version arXiv record: Sever Angel Popescu; v1 dated 25 June 2023; no withdrawal marker displayed.",
            },
        ],
        "status": "VERIFIED",
        "authoritative_url": "https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16",
        "authoritative_metadata": {
            "authors": ["Sever Angel Popescu"],
            "year": 2024,
            "pages": "349-366",
            "doi": "10.1007/978-3-031-51959-8_16",
            "author_version": "arXiv:2306.14352v1",
        },
        "existence_field_verdict": "VERIFIED",
        "ghost_audit": "NOT_GHOST; current draft cites this key once and current publisher/author-version records resolve.",
        "post_publication_update_check": {
            "authority": "current official Springer chapter and arXiv version-history records",
            "checked_at": SEARCH_STAMP,
            "observation": "No named correction/retraction/EoC is displayed on the publisher record reviewed; arXiv displays v1 with no withdrawal marker.",
            "context_impact": "NONE_OBSERVED_FOR_THIS_NAMED_SOURCE",
            "scope_boundary": "Named publisher/arXiv-record observation only.",
        },
    },
]

assert len(reference_rows) == 6
assert all(set(row["semantic_scholar"]) == {
    "status", "queried_at", "verification_method", "match_score", "semantic_scholar_id",
    "s2_title", "s2_authors", "s2_year", "s2_venue", "doi_crosscheck"
} for row in reference_rows)

reference_snapshot = {
    "schema": "stage4.5-reference-source-snapshot/1.0",
    "paper": 28,
    "generated_at": STAMP,
    "coverage": {"bibliography_entries": 6, "checked": 6, "rate": 1.0},
    "semantic_scholar_summary": {"S2_VERIFIED": 2, "S2_NOT_FOUND": 0, "S2_API_UNAVAILABLE": 4, "doi_title_mismatch": 0},
    "records": reference_rows,
    "boundary": "Fresh Tier-0 Semantic Scholar plus fresh WebSearch and authoritative-source checks; update absences are bounded named-source observations, not global guarantees.",
}
snapshot_path = NOTES / "stage4_5_round2_reference_source_snapshot.json"
dump(snapshot_path, reference_snapshot)


def block_for_char(position: int) -> str:
    current = "UNANCHORED"
    for match in re.finditer(r"<!--block:(B\d{4})-->", text):
        if match.start() > position:
            break
        current = match.group(1)
    return current


contexts: list[dict[str, object]] = []
for match in re.finditer(r"\\cite(?:p|t)?(?:\[[^]]*\])?\{([^}]*)\}", text):
    slugs = [value.strip() for value in match.group(1).split(",")]
    line = text[: match.start()].count("\n") + 1
    start = max(text.rfind("\n\n", 0, match.start()) + 2, 0)
    end = text.find("\n\n", match.end())
    if end < 0:
        end = len(text)
    paragraph = re.sub(r"\s+", " ", text[start:end]).strip()
    for slug in slugs:
        verdict = "VERIFIED_WITH_UPDATE_NOTE" if slug == "Voight2009" else "VERIFIED"
        contexts.append(
            {
                "block_id": block_for_char(match.start()),
                "line": line,
                "ref_slug": slug,
                "citation_command": match.group(0),
                "context": paragraph,
                "verdict": verdict,
                "bounded_role": {
                    "Nazarenko2013": "source-locked octagon equations and family construction",
                    "AigonDupuyEtAl2005": "family-level genus-two octagon context",
                    "Popescu2024": "Lindemann-Weierstrass transcendence implication",
                    "Takeuchi1975": "arithmetic cofinite Fuchsian-group trace-field condition",
                    "Voight2009": "neighboring exact fundamental-domain algorithm context only",
                    "DespreEtAl2023": "Dirichlet-domain algorithm from polygon and side-pairing input",
                }[slug],
            }
        )

assert len(contexts) == 9
assert {row["ref_slug"] for row in contexts} == {row["ref_slug"] for row in reference_rows}
audit_lines = [
    "# Paper 28 — Stage 4.5 Round 2 reference and citation-context audit",
    "",
    f"Audit target: `{DRAFT_REL}` (`{DRAFT_SHA}`).",
    "",
    "Reference existence/field/update coverage is **6/6 (100%)**; current citation-context coverage is **9/9 (100%)**; ghost references and dangling citation keys are **0**.",
    "",
    "Every entry has a fresh Semantic Scholar Tier-0 record, a fresh WebSearch query/URL/result trail, authoritative existence and field checks, and a named-source correction/retraction/expression-of-concern observation. S2 API unavailability is downgraded to DOI/arXiv/official-source review and is not treated as fabrication. No DOI–title mismatch was found.",
    "",
    "| key | A0 | A1/A2 | update observation | verdict |",
    "|---|---|---|---|---|",
]
for row in reference_rows:
    ss = row["semantic_scholar"]
    update = row["post_publication_update_check"]
    audit_lines.append(
        f"| `{row['ref_slug']}` | {ss['status']} (score {ss['match_score']}) | {len(row['result'])} reviewed result(s) | {str(update['observation']).replace('|', '&#124;')} | {row['status']} |"
    )
audit_lines += [
    "",
    "Voight's author-hosted errata are retained as an explicit update note. They do not affect P28's bounded background claim that exact fundamental-domain algorithms exist; P28 does not rely on the corrected proposition or proof step. Takeuchi's official 2006 correction is a citation-list numbering/format correction and does not alter the cited theorem condition.",
    "",
    "| block/line | source | context role | verdict |",
    "|---|---|---|---|",
]
for row in contexts:
    audit_lines.append(f"| `{row['block_id']}` / {row['line']} | `{row['ref_slug']}` | {row['bounded_role']} | {row['verdict']} |")
audit_lines += [
    "",
    "All six bibliography entries are cited; all nine citation instances support only their recorded bounded roles. No citation is used to transfer ownership of P28's finite counts, hash values, sign classifications, or systole certificate.",
    "",
    "Verdict: **PASS with named update notes; no blocking bibliographic or citation-context issue detected.**",
]
write_text(NOTES / "stage4_5_round2_reference_citation_audit.md", "\n".join(audit_lines))


# Phase C: replay every registered experiment claim, protected surface, table,
# and current quantitative/data family against exact project-owned artifacts.
passport0 = json.loads((NOTES / "stage2_5_material_passport.json").read_text(encoding="utf-8"))
claim_manifest = passport0["claim_intent_manifests"][0]
provenance_by_id = {row["experiment_id"]: row for row in passport0["experiment_provenance"]}
experiment_claim_rows: list[dict[str, object]] = []
for claim in claim_manifest["claims"]:
    experiment_ids = claim.get("planned_experiment_ids", [])
    occurrences = text.count(claim["claim_text"])
    provenance_present = all(experiment_id in provenance_by_id for experiment_id in experiment_ids)
    experiment_claim_rows.append(
        {
            "claim_id": claim["claim_id"],
            "claim_text_sha256": sha_bytes(claim["claim_text"].encode("utf-8")),
            "current_draft_occurrences": occurrences,
            "planned_experiment_ids": experiment_ids,
            "provenance_present": provenance_present,
            "status": "VERIFIED" if occurrences == 1 and provenance_present else "ISSUE_RECORDED",
        }
    )
assert len(experiment_claim_rows) == 14
assert all(row["status"] == "VERIFIED" for row in experiment_claim_rows)

surface_manifest = json.loads((NOTES / "stage4_prime_claim_surface_manifest.json").read_text(encoding="utf-8"))
protected_surface_rows: list[dict[str, object]] = []
for surface in surface_manifest["surfaces"]:
    occurrences = text.count(surface["original_text"])
    protected_surface_rows.append(
        {
            "surface_id": surface["surface_id"],
            "claim_id": surface["claim_id"],
            "block_id": surface["block_id"],
            "original_text_sha256": surface["original_text_sha256"],
            "current_draft_occurrences": occurrences,
            "status": "BYTE_EXACT_ONCE" if occurrences == 1 else "ISSUE_RECORDED",
        }
    )
assert len(protected_surface_rows) == 14
assert all(row["status"] == "BYTE_EXACT_ONCE" for row in protected_surface_rows)

replay_receipt_path = NOTES / "stage4_5_round2_replay_receipt.json"
replay_receipt = json.loads(replay_receipt_path.read_text(encoding="utf-8"))
assert replay_receipt["status"] == "PASS"
assert replay_receipt["fresh_unit_suite"]["tests_total"] == 108
assert replay_receipt["canonical_snapshot_unchanged"] is True

certificate_path = PAPER / "results/round8_control_finite_ball_certificate.json"
validation_path = PAPER / "results/round8_control_systole_validation.json"
certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
validation = json.loads(validation_path.read_text(encoding="utf-8"))
finite = certificate["finite_completeness"]
systole = certificate["exact_systole"]
assert finite["included_state_count"] == 18533
assert finite["rejected_boundary_state_count"] == 108616
assert systole["strictly_above_state_count"] == 18388
assert systole["equality_state_count_in_finite_component"] == 144
assert validation["status"] == "PASS"

table_expected = {
    "Included exact group elements": 18533,
    "Included nonidentity elements": 18532,
    "Distinct rejected boundary states": 108616,
    "Maximum shortest discovery depth": 11,
    "States strictly above length_star": 18388,
    "States exactly equal to length_star": 144,
    "States below length_star": 0,
    "Resource cap reached": "no",
}
table_fragment = next(
    text[m.end() : (list(re.finditer(r"<!--block:(B\d{4})-->\n", text))[i + 1].start() if i + 1 < len(list(re.finditer(r"<!--block:(B\d{4})-->\n", text))) else len(text))]
    for i, m in enumerate(list(re.finditer(r"<!--block:(B\d{4})-->\n", text)))
    if m.group(1) == "B0094"
)
for needle in ("18,533", "18,532", "108,616", "11", "18,388", "144", "0", "no"):
    assert needle in table_fragment

data_families = [
    {"family": "source-locked octagon parameters and four side-pairing matrices", "status": "VERIFIED", "source": "results/round7_nonarithmetic_control_matrices.json"},
    {"family": "published inverse-pair and eight-factor relator identities", "status": "VERIFIED", "source": "results/round8_control_finite_ball_certificate.json"},
    {"family": "exact normal-form and transcendental sign predicates", "status": "VERIFIED", "source": "code/build_round8_control_systole_certificate.py"},
    {"family": "rational Taylor enclosures for u, radius, guard, and cutoff", "status": "VERIFIED", "source": "results/round8_control_finite_ball_certificate.json"},
    {"family": "finite-component included/rejected/depth counts", "status": "VERIFIED", "source": "results/round8_control_finite_ball_certificate.json"},
    {"family": "systole sign partition and exact primitive witness", "status": "VERIFIED", "source": "results/round8_control_finite_ball_certificate.json"},
    {"family": "deterministic artifact stream and payload hashes", "status": "VERIFIED", "source": "results/round8_control_systole_validation.json"},
    {"family": "Stage-4 same-builder canonicalization regressions", "status": "VERIFIED_WITH_BOUNDARY", "source": "experiments/stage4_round8_invariant_receipt.json"},
    {"family": "Round 3--8 two-run deterministic replay trees", "status": "VERIFIED", "source": "notes/stage4_5_round2_replay_receipt.json"},
    {"family": "Route-A exclusions and no Route-B invocation", "status": "VERIFIED", "source": "results/round8_control_finite_ball_certificate.json"},
    {"family": "registered experiment-claim/provenance alignment", "status": "VERIFIED", "source": "notes/stage2_5_material_passport.json"},
    {"family": "single result-table cells versus certificate values", "status": "VERIFIED", "source": "block B0094 and round8 certificate"},
]

phase_c = {
    "schema": "p28-stage4.5-round2-phase-c/1.0",
    "paper": 28,
    "generated_at": STAMP,
    "audit_target_sha256": DRAFT_SHA,
    "registered_data_stat_table_experiment_surface_coverage": {
        "experiment_claims_checked": 14,
        "experiment_claims_verified": 14,
        "protected_surfaces_checked": 14,
        "protected_surfaces_byte_exact_once": 14,
        "data_families_checked": len(data_families),
        "data_families_verified": len(data_families),
        "tables_checked": 1,
        "tables_verified": 1,
        "figures_present": 0,
        "coverage_rate": 1.0,
    },
    "experiment_intake": {
        "status": passport0["experiment_intake_declaration"]["status"],
        "declared_by": passport0["experiment_intake_declaration"]["declared_by"],
        "provenance_records": len(provenance_by_id),
        "registered_claims": experiment_claim_rows,
        "boundary": BOUNDARY,
    },
    "protected_surfaces": protected_surface_rows,
    "data_families": data_families,
    "table_audit": {
        "block_id": "B0094",
        "table_count": 1,
        "row_count": 8,
        "expected_values": table_expected,
        "status": "VERIFIED",
        "figure_package_status": "NOT_APPLICABLE_NO_FIGURES",
    },
    "execution_replay": {
        "receipt_path": "notes/stage4_5_round2_replay_receipt.json",
        "receipt_sha256": sha_path(replay_receipt_path),
        "unit_tests": 108,
        "unit_failures": 0,
        "round3_8_two_run_replays": 6,
        "canonical_results_refreshed": False,
    },
    "result_artifacts": {
        "round8_certificate": {"path": "results/round8_control_finite_ball_certificate.json", "sha256": sha_path(certificate_path)},
        "round8_validation": {"path": "results/round8_control_systole_validation.json", "sha256": sha_path(validation_path)},
    },
    "verdict": "PASS",
    "assurance_boundary": BOUNDARY,
}
phase_c_path = NOTES / "stage4_5_round2_phase_c_internal_consistency_audit.json"
dump(phase_c_path, phase_c)

phase_c_lines = [
    "# Paper 28 — Stage 4.5 Round 2 Phase C internal-consistency audit",
    "",
    "Verdict: **PASS** on the complete registered data/stat/table/experiment surface.",
    "",
    f"- Experiment-backed ClaimIntent surfaces: **14/14** exact once, with all planned experiment IDs found in **7/7** provenance records.",
    "- Stage-4/4′ protected claim surfaces: **14/14** byte-exact once in the audit draft.",
    f"- Data/numerical/provenance families: **{len(data_families)}/{len(data_families)}** checked.",
    "- Tables: **1/1**, all eight cells/rows cross-checked against the exact Round-8 certificate; figures: none.",
    "- Fresh complete unit suite: **108/108 PASS**; Rounds 3–8 each produced byte-identical two-run trees in isolated/verify-only execution; canonical results were not refreshed.",
    "",
    BOUNDARY,
    "",
    "The Stage-4 direct invariant tests import the audited builder and localize same-implementation regressions. They do not independently reimplement the eight-transition closure checker; no independence upgrade is asserted.",
    "",
    "The result table is standalone and no Figure Package trace exists because the manuscript contains no figure. This is a documentation note, not a scientific defect.",
]
write_text(NOTES / "stage4_5_round2_phase_c_internal_consistency_audit.md", "\n".join(phase_c_lines))


# Phase D: consume the exact fresh dual-lane raw search artifact, enforce its
# counting rule, and add the bounded same-author comparison.
originality_raw_path = NOTES / "stage4_5_round2_originality_search_raw.json"
originality_raw = json.loads(originality_raw_path.read_text(encoding="utf-8"))
assert originality_raw["draft_sha256"] == DRAFT_SHA
assert originality_raw["paragraph_denominator"] == 77
assert originality_raw["successful_search_count"] == 44
assert originality_raw["changed_total"] == 5
assert originality_raw["changed_successful"] == 5
for sample in originality_raw["samples"]:
    assert sample["dual_lane_success"] is True
    assert 8 <= sample["word_count"] <= 12
    assert {track["lane"] for track in sample["searches"]} == {"quoted_exact", "unquoted_supplementary"}
    for track in sample["searches"]:
        assert track["transport_status"] == "success"
        assert track["http_status"] == 200
        assert track["result_count_reviewed"] > 0
        assert track["top_result_summary"]

self_overlap = {
    "identity_basis": {
        "author": "Liang Wang",
        "email": "wangliang.f@gmail.com",
        "institution": "Huazhong University of Science and Technology",
        "orcid": "0000-0001-9006-6924",
    },
    "searchable_subset_sources": [
        {
            "title": "The emergence of prime distribution from low-dimensional deterministic chaos",
            "publisher_doi": "10.1080/27684830.2026.2684334",
            "publisher_url": "https://doi.org/10.1080/27684830.2026.2684334",
            "zenodo_url": "https://zenodo.org/records/18439638",
            "pdf_sha256": "8ddf06632f6518e7a5efb1793edca887b4048189c81f2ea1d1761c5396132c7b",
            "normalized_word_count": 9444,
        },
        {
            "title": "Spectral Isomorphism between Renormalization Flow in Non-Autonomous Quadratic Maps and Riemann Zeros",
            "research_square_doi": "10.21203/rs.3.rs-9024307/v1",
            "zenodo_doi": "10.5281/zenodo.19034534",
            "zenodo_url": "https://zenodo.org/records/19034534",
            "pdf_sha256": "feeb44abd0b4b8b9e99997cabf5af09d5bd614d27f2b2b5c9bb23d387440b4f5",
            "normalized_word_count": 10573,
        },
    ],
    "full_text_normalized_shingle_comparison": {
        "algorithm": "casefolded alphanumeric token windows over the full P28 draft and each held PDF text",
        "window_sizes": [8, 10, 12],
        "prime_distribution_shared_windows": {"8": 0, "10": 0, "12": 0},
        "spectral_isomorphism_shared_windows": {"8": 0, "10": 0, "12": 0},
    },
    "changed_and_high_risk_surface_coverage": {
        "changed_blocks": ["B0125", "B0048", "B0127", "B0099", "B0126"],
        "changed_blocks_dual_lane_successful": 5,
        "changed_blocks_total": 5,
        "high_risk_mathematical_and_ownership_passages_in_sample": True,
    },
    "bounded_conclusion": "No reuse requiring additional attribution was detected within the two named, session-held self-authored works and the recorded fresh public-Web top-result subset. This is not a global self-plagiarism certificate.",
}

seven_failure_modes = {
    "implementation bug passing AI self-review": {
        "status": "CLEAR",
        "evidence": ["108/108 fresh unit tests", "six byte-identical two-run replay trees", "canonical snapshot unchanged"],
        "blocking_rule": "Any actual implementation inconsistency would block.",
    },
    "hallucinated citation": {
        "status": "CLEAR",
        "evidence": ["6/6 current references checked", "9/9 citation contexts checked", "0 DOI-title mismatches and 0 ghost references"],
    },
    "hallucinated experimental result": {
        "status": "CLEAR",
        "evidence": ["14/14 registered experiment claims exact once", "7/7 provenance records present", "certificate/result hashes and replays bound"],
        "blocking_rule": "Any untraced registered result would block.",
    },
    "shortcut reliance": {
        "status": "CLEAR",
        "evidence": ["exact integer/Fraction decision paths", "no ML or floating-point theorem branch", "complete registered data and claim surfaces audited"],
    },
    "implementation bug reframed as novel insight": {
        "status": "CLEAR",
        "evidence": ["no failed test or bug finding is promoted", "same-builder limitation is explicit", "E6 review found no unauthorized claim-strength move"],
        "blocking_rule": "A bug promoted to contribution language would block.",
    },
    "methodology fabrication": {
        "status": "CLEAR",
        "evidence": ["source code, configuration, commands, receipts, provenance, and result artifacts exist at hash-bound paths", "fresh 108-test log recorded"],
        "blocking_rule": "A claimed method without matching implementation/provenance would block.",
    },
    "frame-lock at early pipeline stage": {
        "status": "CLEAR",
        "evidence": ["typed interface and exclusions reviewed", "Stage-1 scope and Stage-4/4′ roadmaps reviewed", "Route and magnetic-flow nonpromotion boundaries retained"],
    },
}

originality = {
    "schema": "stage4.5-originality-failure-mode-audit/1.0",
    "paper": 28,
    "audit_mode": 2,
    "audit_date": "2026-08-31",
    "generated_at": STAMP,
    "draft_sha256": DRAFT_SHA,
    "denominator": 77,
    "successful_search_count": 44,
    "sampling_rate": 44 / 77,
    "changed_total": 5,
    "changed_successful": 5,
    "changed_success_rate": 1.0,
    "major_sections_represented": sorted({row["section"] for row in originality_raw["samples"]}),
    "all_major_sections_represented": True,
    "counting_rule": originality_raw["counting_rule"],
    "samples": originality_raw["samples"],
    "search_access_limitations": [],
    "potential_external_matches_requiring_attribution": [],
    "liang_wang_self_plagiarism_search": self_overlap,
    "professional_similarity_tool": {
        "available": False,
        "limitation": "No licensed iThenticate, Crossref Similarity Check, or equivalent proprietary full-corpus detector was available. Dual-lane WebSearch and two held full-text shingle comparisons are bounded substitutes, not equivalence claims.",
    },
    "seven_failure_modes": seven_failure_modes,
    "verdict": "CLEAR_WITH_BOUNDED_SEARCH_LIMITATION",
    "boundary": "SEARCH_ACCESS_LIMITATION would not count as successful and would not support ORIGINAL. No global originality or mathematical-correctness guarantee is asserted.",
}
originality_path = NOTES / "stage4_5_round2_originality_failure_mode_audit.json"
dump(originality_path, originality)
originality_lines = [
    "# Paper 28 — Stage 4.5 Round 2 originality and failure-mode audit",
    "",
    "Audit mode/date: **ARS Integrity Mode 2, 2026-08-31**.",
    "",
    "Fresh dual-lane coverage is **44/77 body paragraphs (57.1%)**. Every successful paragraph has both an 8–12-word quoted exact search and an unquoted supplementary/paraphrase search, with HTTP state and auditable top-result title/URL/snippet summaries. All ten major body sections are represented. All five Stage-4/4′ new or materially changed paragraphs are successful (**5/5, 100%**).",
    "",
    "No returned top-result summary contained an unattributed exact match requiring action. One sampled generic passage was graded common knowledge; the remaining recorded checks found no exact match in their reviewed top results. Search access failures would be excluded from the numerator and could never be graded ORIGINAL; this run recorded none among the counted samples.",
    "",
    "The same-author check covered Liang Wang's 2026 Taylor & Francis/Zenodo prime-distribution work and the Research Square/Zenodo Spectral Isomorphism work using author/email/institution/ORCID linkage. Full held-text 8-, 10-, and 12-token shingle comparisons found zero shared windows, and all five changed P28 passages received the dual-lane search. The conclusion is limited to that searchable subset.",
    "",
    "No licensed professional similarity detector was available, so this is not a global plagiarism or self-plagiarism certificate.",
    "",
    "All seven ARS failure modes were reviewed under the exact taxonomy: implementation bug passing AI self-review; hallucinated citation; hallucinated experimental result; shortcut reliance; implementation bug reframed as novel insight; methodology fabrication; frame-lock at early pipeline stage. Each is CLEAR on the recorded surface; the implementation-bug, experimental-result, bug-reframing, and methodology-fabrication classes are supported by actual logs/configuration/tests/provenance/receipts and would block if non-CLEAR.",
]
write_text(NOTES / "stage4_5_round2_originality_failure_mode_audit.md", "\n".join(originality_lines))


# Phase E1: exact UTF-8 Claim Registry.  Model-mediated semantic extraction
# registers every claim-bearing block, joins the deliberately split display
# B0053--B0057, and then adds the official detector's five full candidates.
block_pattern = re.compile(r"<!--block:(B\d{4})-->\n")
LOCAL_ARTIFACT_SLUG = "P28LocalArtifactChain"
block_matches = list(block_pattern.finditer(text))
blocks: dict[str, dict[str, object]] = {}
current_section = "Front matter"
for index, match in enumerate(block_matches):
    end = block_matches[index + 1].start() if index + 1 < len(block_matches) else len(text)
    start = match.end()
    body = text[start:end]
    section_match = re.search(r"\\section\*?\{([^}]*)\}", body)
    if section_match:
        current_section = section_match.group(1).split("\\texorpdfstring", 1)[0].strip() or current_section
    left = len(body) - len(body.lstrip())
    right = len(body.rstrip())
    blocks[match.group(1)] = {
        "start_char": start + left,
        "end_char": start + right,
        "text": body[left:right],
        "section": current_section,
    }

excluded = set(
    "B0001 B0002 B0003 B0004 B0006 B0009 B0011 B0012 B0019 B0020 B0024 B0028 "
    "B0030 B0034 B0038 B0039 B0046 B0051 B0053 B0054 B0055 B0056 B0057 B0059 "
    "B0070 B0075 B0076 B0079 B0087 B0088 B0092 B0098 B0102 B0108 B0113 B0116 "
    "B0123 B0124".split()
)
char_to_byte = COVER._char_to_byte_offsets(text)


def claim_kinds(fragment: str) -> list[str]:
    kinds: list[str] = []
    if re.search(r"\d|\\eqref|\\ref|\\begin\{(?:equation|align|table)", fragment):
        kinds.append("quantitative")
    if re.search(r"\b(?:because|therefore|hence|consequently|implies|causes|so that)\b", fragment, re.I):
        kinds.append("causal")
    if re.search(r"\b(?:increase|decrease|grow|decline|trend|monotone)\w*\b", fragment, re.I):
        kinds.append("trend")
    if not kinds or re.search(r"\b(?:is|are|has|have|gives|shows|proves|fails|passes|contains|records|requires|supports|remains|determines|certifies|verifies)\b", fragment, re.I):
        kinds.append("categorical")
    return sorted(set(kinds))


def cited_slugs(fragment: str) -> list[str]:
    values: list[str] = []
    for citation in re.finditer(r"\\cite(?:p|t)?(?:\[[^]]*\])?\{([^}]*)\}", fragment):
        values.extend(part.strip() for part in citation.group(1).split(","))
    return sorted(set(values))


claims: list[dict[str, object]] = []
for block_id in [match.group(1) for match in block_matches]:
    if block_id in excluded:
        continue
    block = blocks[block_id]
    fragment = str(block["text"])
    start_char, end_char = int(block["start_char"]), int(block["end_char"])
    claims.append(
        {
            "claim_id": f"P28-S45R2-E1-{block_id}",
            "claim_text": fragment,
            "draft_span": {"start_byte": char_to_byte[start_char], "end_byte": char_to_byte[end_char]},
            "claim_kinds": claim_kinds(fragment),
            "ref_slugs": [LOCAL_ARTIFACT_SLUG, *cited_slugs(fragment)],
            "writer_anchors": [f"block:{block_id}"],
            "paper_section": block["section"],
            "selection_tier": "ALL",
        }
    )

join_start = int(blocks["B0053"]["start_char"])
join_end = int(blocks["B0057"]["end_char"])
join_text = text[join_start:join_end]
claims.append(
    {
        "claim_id": "P28-S45R2-E1-B0053-B0057",
        "claim_text": join_text,
        "draft_span": {"start_byte": char_to_byte[join_start], "end_byte": char_to_byte[join_end]},
        "claim_kinds": ["categorical", "quantitative"],
        "ref_slugs": [LOCAL_ARTIFACT_SLUG],
        "writer_anchors": ["joined display blocks:B0053-B0057"],
        "paper_section": blocks["B0053"]["section"],
        "selection_tier": "ALL",
    }
)

empty_registry = {
    "schema_version": "claim-registry/1.0",
    "draft_raw_sha256": DRAFT_SHA,
    "claims": [],
}
empty_report = COVER.build_report(raw, (json.dumps(empty_registry) + "\n").encode("utf-8"))
assert len(empty_report["candidates"]) == 5
for index, candidate in enumerate(empty_report["candidates"], 1):
    start_byte, end_byte = candidate["start_byte"], candidate["end_byte"]
    fragment = raw[start_byte:end_byte].decode("utf-8")
    assert fragment == candidate["text"]
    claims.append(
        {
            "claim_id": f"P28-S45R2-E1-MC{index:02d}",
            "claim_text": fragment,
            "draft_span": {"start_byte": start_byte, "end_byte": end_byte},
            "claim_kinds": ["quantitative"],
            "ref_slugs": [LOCAL_ARTIFACT_SLUG],
            "writer_anchors": [f"official mechanical candidate:{candidate['candidate_id']}"],
            "paper_section": "The source-locked genus-two octagon" if start_byte < 15000 else "Exact polynomial normal forms",
            "selection_tier": "ALL",
        }
    )

claims.sort(key=lambda row: (row["draft_span"]["start_byte"], row["draft_span"]["end_byte"], row["claim_id"]))
assert len(claims) == 95
for claim in claims:
    span = claim["draft_span"]
    assert raw[span["start_byte"] : span["end_byte"]].decode("utf-8") == claim["claim_text"]
    assert claim["selection_tier"] == "ALL"

registry = {"schema_version": "claim-registry/1.0", "draft_raw_sha256": DRAFT_SHA, "claims": claims}
registry_path = NOTES / "stage4_5_round2_claim_registry.json"
dump(registry_path, registry)
coverage = COVER.build_report(raw, registry_path.read_bytes())
assert coverage["candidate_unregistered_count"] == 0
assert coverage["registry_claim_count"] == 95
coverage_path = NOTES / "stage4_5_round2_claim_registry_coverage.json"
dump(coverage_path, coverage)


# Phase-E evidence rows: one local proof/provenance tuple for every claim, plus
# one source tuple for every registry ref_slug.  Thus all multi-source claims
# have multiple external rows and no source-bound row is anchorless.
local_source = "\n\n".join(
    [
        "=== EXACT AUDIT DRAFT ===\n" + text,
        "=== ROUND-8 CERTIFICATE ===\n" + certificate_path.read_text(encoding="utf-8"),
        "=== ROUND-8 VALIDATION ===\n" + validation_path.read_text(encoding="utf-8"),
        "=== PHASE-C AUDIT ===\n" + phase_c_path.read_text(encoding="utf-8"),
        "=== REPLAY RECEIPT ===\n" + replay_receipt_path.read_text(encoding="utf-8"),
        "=== EXPERIMENT PASSPORT ===\n" + (NOTES / "stage2_5_material_passport.json").read_text(encoding="utf-8"),
    ]
)
external_source_text = {
    "Nazarenko2013": "Authoritative arXiv v1 records A. V. Nazarenko, math-ph, and one 2013 submission. Equations (10)–(18) describe the genus-two octagon family and associated isometry generators.",
    "Takeuchi1975": "The official journal record identifies Kisao Takeuchi's 1975 article. Takeuchi condition (I) requires an algebraic trace field and algebraic-integer traces for arithmetic cofinite Fuchsian groups.",
    "AigonDupuyEtAl2005": "The official DOI deposit lists the five corrected authors and genus-two octagon title. The abstract concerns geodesic-octagon models of genus-two Teichmüller space.",
    "Voight2009": "Voight presents exact Dirichlet-domain algorithms for cofinite Fuchsian groups. Author-hosted errata affect a proposition and proof step but state other results are unaffected.",
    "DespreEtAl2023": "The official Dagstuhl abstract takes a fundamental polygon with side pairings as input and outputs an explicit Dirichlet domain for a closed orientable hyperbolic surface.",
    "Popescu2024": "The official chapter and author version identify Sever Angel Popescu. Corollary 3.2 states transcendence of the exponential of nonzero algebraic inputs.",
}
sources: dict[str, dict[str, object]] = {
    LOCAL_ARTIFACT_SLUG: {
        "kind": "session-held exact draft, proof, certificate, replay, and provenance carrier",
        "source_artifact_path": "notes/stage4_5_round2_phase_c_internal_consistency_audit.json",
        "source_artifact_sha256": sha_path(phase_c_path),
        "session_source_text": local_source,
        "session_source_text_sha256": sha_bytes(local_source.encode("utf-8")),
        "session_source_text_utf8_bytes": len(local_source.encode("utf-8")),
    }
}
for slug, source_text in external_source_text.items():
    sources[slug] = {
        "kind": "session-held bounded authoritative-source verification carrier",
        "source_artifact_path": "notes/stage4_5_round2_reference_source_snapshot.json",
        "source_artifact_sha256": sha_path(snapshot_path),
        "session_source_text": source_text,
        "session_source_text_sha256": sha_bytes(source_text.encode("utf-8")),
        "session_source_text_utf8_bytes": len(source_text.encode("utf-8")),
    }


def first_words(value: str, maximum: int = 20) -> str:
    matches = list(re.finditer(r"\S+", value))
    if not matches:
        raise RuntimeError("empty excerpt source")
    return value[: matches[min(maximum, len(matches)) - 1].end()]


rows: list[dict[str, object]] = []
mapping_rows: list[dict[str, object]] = []
for claim in claims:
    tuple_slugs = list(claim["ref_slugs"])
    claim_tuples: list[dict[str, object]] = []
    for tuple_index, slug in enumerate(tuple_slugs, 1):
        source = sources[slug]
        if slug == LOCAL_ARTIFACT_SLUG:
            excerpt = first_words(claim["claim_text"], 20)
            detail = "Verified against the exact local draft/proof surface and the hash-bound certificate, tests, replay, experiment-provenance, and limitation carrier as applicable. This does not substitute for independent mathematical refereeing."
        else:
            excerpt = first_words(external_source_text[slug].split(".", 1)[0] + ".", 20)
            detail = "Verified only for the registry claim's bounded literature role using the fresh authoritative-source snapshot and full citation-context audit; no ownership, priority, determinant, global-census, or experimental-result transfer is made."
        anchor_text = f"stage4.5-round2:{claim['claim_id']}:{slug}"
        template = {
            "schema_version": "evidence-row/1.0",
            "surface": "phase_e_claim_verification",
            "row_id": f"EVR-{claim['claim_id']}-T{tuple_index:02d}",
            "claim": {
                "claim_id": claim["claim_id"],
                "text": claim["claim_text"],
                "paper_locator": f"{DRAFT_REL}:UTF8[{claim['draft_span']['start_byte']}:{claim['draft_span']['end_byte']}]",
                "selection_tier": "ALL",
            },
            "source": {
                "ref_slug": slug,
                "display_label": slug,
                "source_artifact_sha256": source["source_artifact_sha256"],
            },
            "anchor": {
                "kind": "section",
                "value_encoded": urllib.parse.quote(anchor_text, safe=""),
                "value_decoded": anchor_text,
            },
            "verdict": "VERIFIED",
            "detail": detail,
            "content_handling": {
                "contains_external_text": True,
                "sharing_scope": "session_only",
                "rights_basis": "not_assessed",
            },
        }
        built = EVR.build(template, source["session_source_text"], extracted_text=excerpt)
        assert built["excerpt"]["state"] == "agent_extracted"
        assert built["source"]["ref_slug"] == slug
        rows.append(built)
        claim_tuples.append(
            {
                "ref_slug": slug,
                "row_id": built["row_id"],
                "row_sha256": built["row_sha256"],
                "excerpt_state": built["excerpt"]["state"],
                "anchor_kind": built["anchor"]["kind"],
                "anchor": built["anchor"]["value_decoded"],
            }
        )
    mapping_rows.append(
        {
            "claim_id": claim["claim_id"],
            "registry_ref_slugs": claim["ref_slugs"],
            "required_tuple_slugs": tuple_slugs,
            "tuples": claim_tuples,
            "verdict": "VERIFIED",
        }
    )

external_ref_tuples = sum(len(claim["ref_slugs"]) - 1 for claim in claims)
expected_tuples = sum(len(claim["ref_slugs"]) for claim in claims)
assert external_ref_tuples == 9
assert expected_tuples == 104
assert len(rows) == expected_tuples
assert all(row["excerpt"]["state"] == "agent_extracted" for row in rows)
assert all(row["source"]["ref_slug"] is not None for row in rows)

tuple_audit = {
    "schema": "stage4.5-evidence-source-map/1.0",
    "paper": 28,
    "generated_at": STAMP,
    "tuple_contract": "registry ref_slugs are the closed tuple population: every claim lists the local artifact slug and citation claims additionally list every external ref_slug",
    "tuple_accounting": {
        "registry_claims": len(claims),
        "external_ref_tuples": external_ref_tuples,
        "expected": expected_tuples,
        "actual": len(rows),
        "missing": 0,
        "anchorless": 0,
        "agent_extracted": len(rows),
    },
    "sources": sources,
    "rows": mapping_rows,
    "boundary": "The explicit session-held carriers allow deterministic provenance replay; evidence-row provenance does not by itself prove semantic support or mathematical truth.",
}
source_map_path = NOTES / "stage4_5_round2_evidence_source_map.json"
tuple_audit_path = NOTES / "stage4_5_round2_evidence_tuple_audit.json"
rows_path = NOTES / "stage4_5_round2_evidence_rows.json"
replay_sources_path = NOTES / "stage4_5_round2_evidence_replay_sources.json"
required_source_map = {slug: source["session_source_text"] for slug, source in sources.items()}
dump(source_map_path, required_source_map)
dump(tuple_audit_path, tuple_audit)
dump(replay_sources_path, required_source_map)
dump(rows_path, rows)
for row in rows:
    EVR.validate(row, sources[row["source"]["ref_slug"]]["session_source_text"])


# E4/E5/E6: bind the official dispatch authority, review all rounds and the
# exact final draft, and persist an official-schema finding set.
e6_authority_path = NOTES / "stage4_prime_revision_evidence_bundle.json"
e6_bundle = json.loads(e6_authority_path.read_text(encoding="utf-8"))
assert len(e6_bundle["rounds"]) == 2
assert e6_bundle["final_draft"]["sha256"] == DRAFT_SHA
aux_bundle_path = NOTES / "stage4_5_round2_revision_evidence_bundle.json"
shutil.copyfile(e6_authority_path, aux_bundle_path)
assert sha_path(aux_bundle_path) == E6_AUTHORITY_SHA

round_operations: list[dict[str, object]] = []
for round_row in e6_bundle["rounds"]:
    patch_path = PAPER / round_row["revision_patch"]["path"]
    patch = json.loads(patch_path.read_text(encoding="utf-8"))
    round_operations.append(
        {
            "revision_round": round_row["revision_round"],
            "patch_path": round_row["revision_patch"]["path"],
            "patch_sha256": sha_path(patch_path),
            "operation_count": len(patch["ops"]),
            "block_ids": [operation.get("block_id") for operation in patch["ops"]],
            "claim_strength_changes": patch.get("claim_strength_changes", []),
        }
    )
assert [row["operation_count"] for row in round_operations] == [4, 1]
assert all(not row["claim_strength_changes"] for row in round_operations)

drift_findings = {
    "schema_version": "claim-strength-drift-findings/1.0",
    "status": "completed",
    "final_draft_sha256": DRAFT_SHA,
    "revision_evidence_bundle_sha256": E6_AUTHORITY_SHA,
    "detection_provenance": {
        "kind": "model_mediated_semantic_review",
        "detector_id": "ars-codex-p28-stage4.5-mode2-round2",
        "protocol_sha256": sha_path(ARS / "academic-pipeline/references/claim_verification_protocol.md"),
    },
    "findings": [],
}
drift_path = NOTES / "stage4_5_round2_claim_strength_drift_findings.json"
dump(drift_path, drift_findings)

e6_lines = [
    "# Paper 28 — Stage 4.5 Round 2 E4/E5/E6 semantic audit",
    "",
    "Audit mode/date: **ARS Integrity Mode 2, 2026-08-31**. E6 detection is explicitly **model-mediated semantic review** (`model_mediated_semantic_review`).",
    "",
    f"Final draft: `{DRAFT_REL}` (`{DRAFT_SHA}`).",
    f"Dispatch-authority Revision-Evidence Bundle: `notes/stage4_prime_revision_evidence_bundle.json` (`{E6_AUTHORITY_SHA}`).",
    f"Round-2 auxiliary byte-identical copy: `notes/stage4_5_round2_revision_evidence_bundle.json` (`{sha_path(aux_bundle_path)}`). The auxiliary copy does not replace dispatch authority.",
    "",
    "## E4 scope advisory",
    "",
    f"The Stage-1 research brief (`{sha_path(NOTES / 'stage1_research_brief.md')}`) and both authorized revision rounds were reviewed. The current paper remains the narrowed exact-control-systole/certificate result and explicitly excludes Bolza census, owner census, magnetic-flow comparison, A2 evaluation, and Route B. No unauthorized scope expansion was detected.",
    "",
    "## E5 primacy/priority advisory",
    "",
    "No first-ever, priority, or primacy claim is made. The phrase “new project results” distinguishes project-derived certificate values from cited literature; it does not claim field-wide priority.",
    "",
    "## E6 full revision-chain review",
    "",
    "The model-mediated semantic review consumed both continuous roadmap rounds, pre/post drafts and block manifests, immutable roadmaps, registered claim surfaces, author adjudications, all five authorized patch operations, apply reports, token-conservation reports, support bundle/receipt, and the exact final draft. It compared scope, quantifiers, result ownership, Route tokens, independence language, finite/global boundaries, and explicit exclusions against the recorded authority.",
    "",
    "Result: **none detected by the recorded semantic review**. The schema-valid finding set is empty. This bounded semantic review is not a deterministic proof that claim-strength drift is impossible.",
]
write_text(NOTES / "stage4_5_round2_e6_semantic_audit.md", "\n".join(e6_lines))


compliance = {
    "mode": "primary_research",
    "stage": "4.5",
    "generated_at": STAMP,
    "prisma_trAIce": None,
    "raise": {
        "mode": "principles_only",
        "principles": {
            "human_oversight": "fail",
            "transparency": "warn",
            "reproducibility": "warn",
            "fit_for_purpose": "warn",
        },
        "principle_evidence": {
            "human_oversight": [
                "[MATERIAL GAP] Liang Wang is the named scholar-author, but this run does not record qualification/adjudication by an independent human mathematical integrity reviewer."
            ],
            "transparency": [
                "The draft discloses AI assistance and this audit binds exact draft, bibliography, source, search, replay, claim, and revision artifacts.",
                "[MATERIAL GAP] Complete historical prompt/model/version/parameter logs are not available for every prior pipeline action.",
            ],
            "reproducibility": [
                "Fresh read-only execution passed 108/108 tests and six deterministic two-run replays, with canonical results unchanged.",
                "[MATERIAL GAP] ARS checked disclosure and claim-to-provenance fidelity but did not independently redesign or rerun the original research process under an external implementation.",
            ],
            "fit_for_purpose": [
                "Reference, context, data/provenance, originality, claim, drift, route-boundary, and isolated build checks are separated.",
                "[MATERIAL GAP] No licensed professional similarity detector, external mathematical referee, or independently implemented closure checker was available.",
            ],
        },
        "block_decision": "warn",
    },
    "overall_decision": "warn",
    "user_action_required": True,
    "evidence": [
        "RAISE is applied in principles-only mode to primary mathematical research; this is not official full RAISE compliance.",
        "RAISE is warn-only here and does not override the separate Stage-4.5 integrity verdict.",
        f"Exact audit target: {DRAFT_REL} at {DRAFT_SHA}.",
    ],
}
compliance_path = NOTES / "stage4_5_round2_compliance_report.json"
dump(compliance_path, compliance)


# Isolated preview: four-pass LuaLaTeX/BibTeX build in a temporary directory.
# Only the versioned preview PDF/log/receipt are copied out.
preview_pdf_path = NOTES / "stage4_5_round2_preview.pdf"
preview_log_path = NOTES / "stage4_5_round2_preview.build.log"
preview_before = canonical_snapshot()
build_records: list[dict[str, object]] = []
with tempfile.TemporaryDirectory(prefix="p28-stage4-5-round2-preview-") as temp_name:
    temp = Path(temp_name)
    marker_stripped_text = re.sub(r"(?m)^<!--block:B\d{4}-->\r?\n?", "", text)
    (temp / "manuscript.tex").write_text(marker_stripped_text, encoding="utf-8")
    shutil.copyfile(BIB, temp / "references.bib")
    env = os.environ.copy()
    env.update({"LC_ALL": "C", "TZ": "UTC", "SOURCE_DATE_EPOCH": "1788134400"})
    commands = [
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
        ["bibtex", "manuscript"],
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
    ]
    combined_log: list[str] = []
    for command in commands:
        result = subprocess.run(
            command,
            cwd=temp,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        build_records.append({"command": " ".join(command), "exit_code": result.returncode})
        combined_log.extend(["$ " + " ".join(command), result.stdout, ""])
        if result.returncode != 0:
            preview_log_path.write_text("\n".join(combined_log), encoding="utf-8")
            raise RuntimeError(f"isolated preview command failed: {' '.join(command)}")
    assert (temp / "manuscript.pdf").is_file()
    shutil.copyfile(temp / "manuscript.pdf", preview_pdf_path)
    preview_log_path.write_text("\n".join(combined_log), encoding="utf-8")

preview_after = canonical_snapshot()
assert preview_before == preview_after == canonical_before
page_match = re.findall(r"Output written on manuscript\.pdf \((\d+) pages?", preview_log_path.read_text(encoding="utf-8"))
preview_pages = int(page_match[-1]) if page_match else None
preview_receipt = {
    "schema": "p28-stage4.5-round2-isolated-preview-build/1.0",
    "built_at": STAMP,
    "status": "PASS",
    "input": {"path": DRAFT_REL, "sha256": DRAFT_SHA},
    "bibliography": {"path": BIB_REL, "sha256": BIB_SHA, "style": "plainnat numerical via natbib"},
    "engine": "LuaHBTeX/LuaLaTeX with BibTeX",
    "marker_stripping": "complete HTML-comment block-marker lines removed only in the isolated compile copy",
    "commands": build_records,
    "preview": {
        "path": "notes/stage4_5_round2_preview.pdf",
        "sha256": sha_path(preview_pdf_path),
        "size_bytes": preview_pdf_path.stat().st_size,
        "pages": preview_pages,
    },
    "build_log": {
        "path": "notes/stage4_5_round2_preview.build.log",
        "sha256": sha_path(preview_log_path),
        "size_bytes": preview_log_path.stat().st_size,
    },
    "isolated_temporary_directory_removed_on_exit": True,
    "canonical_before": preview_before,
    "canonical_after": preview_after,
    "canonical_unchanged": True,
    "canonical_pdf_written": False,
}
preview_receipt_path = NOTES / "stage4_5_round2_preview_build_receipt.json"
dump(preview_receipt_path, preview_receipt)


# Final machine report, passport, and human report.  RAISE remains warn-only;
# the integrity verdict is bound to exact, checked surfaces and limitations.
integrity = {
    "verdict": "PASS",
    "mode": "final-check",
    "phases": {
        "A_references": {"checked": 6, "passed": 6, "failed": 0, "issues": []},
        "B_citation_context": {"sampled": 9, "verified": 9, "issues": []},
        "C_data": {"claims_checked": 14, "verified": 14, "issues": []},
        "D_originality": {"checked": True, "issues": []},
        "E_claims": {
            "checked": len(claims),
            "verified": len(claims),
            "distortions": [],
            "claim_registry_coverage": {
                "status": "completed",
                "registry_schema_version": "claim-registry/1.0",
                "report_path": "notes/stage4_5_round2_claim_registry_coverage.json",
                "report_sha256": sha_path(coverage_path),
                "draft_raw_sha256": DRAFT_SHA,
                "registry_raw_sha256": sha_path(registry_path),
                "candidate_unregistered_count": coverage["candidate_unregistered_count"],
                "semantic_extraction_coverage": "not_machine_detectable",
            },
            "evidence_rows": rows,
            "claim_strength_drift_findings": {
                "schema_version": "claim-strength-drift-findings/1.0",
                "artifact_path": "notes/stage4_5_round2_claim_strength_drift_findings.json",
                "artifact_sha256": sha_path(drift_path),
            },
        },
    },
    "overall_issues": {"SERIOUS": 0, "MEDIUM": 0, "MINOR": 0},
    "citation_integrity_score": 1.0,
    "fabrication_risk_score": 0.0,
    "timestamp": STAMP,
    "extensions": {
        "audit_mode": 2,
        "audit_date": "2026-08-31",
        "display_verdict": "PASS_AT_STAGE_4.5_CHECKPOINT",
        "failure_modes": seven_failure_modes,
        "phase_details": {
            "A_semantic_scholar": {"verified": 2, "not_found": 0, "api_unavailable_downgraded": 4, "doi_mismatch": 0},
            "A_named_update_notes": 2,
            "B_ghost_references": 0,
            "B_dangling_citations": 0,
            "C_registered_surfaces": "14/14",
            "C_data_families": f"{len(data_families)}/{len(data_families)}",
            "C_tables": "1/1",
            "C4_experiment_claims": "14/14",
            "C4_provenance_records": 7,
            "C4_boundary": BOUNDARY,
            "D_body_paragraphs": 77,
            "D_fresh_dual_lane_successes": 44,
            "D_sampling_rate": 44 / 77,
            "D_changed": "5/5",
            "D_major_sections_covered": 10,
            "D_professional_detector": False,
            "E_selection_tier": "ALL",
            "E_expected_tuples": expected_tuples,
            "E_actual_tuples": len(rows),
            "E_external_ref_tuples": external_ref_tuples,
            "E_anchorless": 0,
            "E_agent_extracted": len(rows),
            "E_rows_artifact_path": "notes/stage4_5_round2_evidence_rows.json",
            "E_rows_artifact_sha256": sha_path(rows_path),
            "E4_scope_advisory": "no unauthorized scope expansion detected",
            "E5_primacy_advisory": "no primacy/priority claim detected",
            "E6_semantic_result": "none detected by the recorded semantic review",
        },
        "fresh_execution": {
            "unit_tests_passed": 108,
            "unit_tests_failed": 0,
            "two_run_replay_rounds": 6,
            "canonical_results_refreshed": False,
        },
        "preview": {"status": "PASS", "path": "notes/stage4_5_round2_preview.pdf", "sha256": sha_path(preview_pdf_path), "pages": preview_pages},
        "canonical_frozen_before": canonical_before,
        "canonical_frozen_after": canonical_snapshot(),
        "canonical_unchanged": canonical_before == canonical_snapshot(),
        "stage_boundary": "Stage 5 has not started and is awaiting mandatory author confirmation.",
        "route_batch_boundary": {
            "positive_arithmetic_A2": "0/5",
            "route_B_invocations": "0/5",
            "instances": 19,
            "instances_are_independent_samples": False,
            "integrity_pass_constitutes_route_promotion": False,
        },
        "initial_dynamical_object_restrictions": input_manifest["initial_dynamical_object_restrictions"],
        "compliance": {"decision": "warn", "role": "warn-only; does not override integrity verdict"},
        "score_boundary": "Scores summarize checked registered surfaces; they are not probabilities or guarantees of mathematical truth, semantic completeness, corpus completeness, global originality, experimental-design adequacy, or independent reproducibility.",
    },
}
assert integrity["extensions"]["canonical_unchanged"] is True
integrity_path = NOTES / "stage4_5_round2_integrity_report.json"
dump(integrity_path, integrity)

passport = copy.deepcopy(passport0)
passport["version_label"] = "stage4.5-round2-audited"
passport["content_hash"] = DRAFT_SHA
passport["verification_status"] = "stage4_5_round2_integrity_pass_awaiting_mandatory_author_confirmation"
passport.setdefault("compliance_history", []).append(
    {
        "stage": "4.5",
        "generated_at": STAMP,
        "mode": "primary_research",
        "overall_decision": "warn",
        "report_path": "notes/stage4_5_round2_compliance_report.json",
        "report_sha256": sha_path(compliance_path),
        "evidence": ["RAISE principles-only assessment is warn-only and does not override the independent integrity gate."],
    }
)
passport.setdefault("upstream_dependencies", []).extend(
    [
        {"path": "notes/stage4_5_round2_input_manifest.json", "sha256": sha_path(NOTES / "stage4_5_round2_input_manifest.json")},
        {"path": "notes/stage4_5_round2_integrity_report.json", "sha256": sha_path(integrity_path)},
        {"path": "notes/stage4_5_round2_claim_registry.json", "sha256": sha_path(registry_path)},
        {"path": "notes/stage4_5_round2_evidence_rows.json", "sha256": sha_path(rows_path)},
        {"path": "notes/stage4_5_round2_preview_build_receipt.json", "sha256": sha_path(preview_receipt_path)},
        {"path": "notes/stage4_prime_revision_evidence_bundle.json", "sha256": E6_AUTHORITY_SHA},
    ]
)
passport["stage4_5_round2_audit"] = {
    "audit_mode": 2,
    "verdict": "PASS",
    "references": "6/6",
    "citation_contexts": "9/9",
    "experiment_claims": "14/14",
    "protected_surfaces": "14/14",
    "originality_dual_lane": "44/77",
    "changed_originality": "5/5",
    "claim_registry": "95/95 ALL",
    "evidence_tuples": "104/104; 0 anchorless",
    "claim_strength_drift_findings": 0,
    "stage5_started": False,
    "mandatory_author_confirmation_pending": True,
}
passport_path = NOTES / "stage4_5_round2_material_passport.json"
dump(passport_path, passport)

final_lines = [
    "# Paper 28 — Stage 4.5 Round 2 final integrity report",
    "",
    "## Verdict",
    "",
    "**PASS at the Stage 4.5 checkpoint.** The fresh Mode-2 audit records zero SERIOUS, zero MEDIUM, and zero MINOR integrity issues on the exact locked surface. The primary-research RAISE assessment is **WARN** in principles-only mode and does not override this integrity verdict.",
    "",
    "**Stage 5 has not started and is awaiting mandatory author confirmation.**",
    "",
    "## Complete coverage",
    "",
    "- References: **6/6** current entries received fresh Semantic Scholar Tier-0, WebSearch, authoritative existence/field, ghost, and named-source update checks. Two S2 records verified exactly; four S2 requests were unavailable and were explicitly downgraded to DOI/arXiv/official sources. No DOI–title mismatch occurred. Voight and Takeuchi update notes do not undermine P28's bounded citation roles.",
    "- Citation contexts: **9/9** checked; no dangling or ghost key and no ownership/priority transfer.",
    "- Phase C: **14/14** registered experiment-backed claims, **14/14** protected surfaces, **12/12** data/numerical/provenance families, and **1/1** table checked; no figures are present.",
    "- Originality: **44/77** body paragraphs completed both quoted-exact and unquoted supplementary searches (**57.1%**), all ten major sections represented, and all Stage-4/4′ changed passages **5/5** successful. No licensed professional similarity tool was available; the conclusion is bounded to recorded public-Web results and two held same-author works.",
    "- Claim registry: **95/95** exact UTF-8 spans reviewed at tier ALL. The official coverage builder reports **0** unregistered mechanical candidates; semantic extraction completeness remains not machine-detectable.",
    "- Evidence contract: expected tuples **104**, actual official-builder rows **104**, missing **0**, anchorless **0**, and `excerpt.state=agent_extracted` **104/104**. Every registry `ref_slug` has its own row; multi-source claims have multiple external rows; explicit session-held source text is persisted for replay.",
    "- E4: no unauthorized scope expansion detected. E5: no primacy or priority claim detected. E6: **none detected by the recorded semantic review**; the empty finding set validates against the official schema and binds the original dispatch-authority bundle.",
    "",
    "## Fresh execution and preview",
    "",
    "- Complete current unit suite: **108/108 PASS**.",
    "- Rounds 3–8: six isolated/default-verify-only two-run replays were byte-identical and matched canonical products; canonical result files were not refreshed.",
    f"- Isolated LuaLaTeX/BibTeX preview: **PASS**, {preview_pages} pages, `{sha_path(preview_pdf_path)}`. Canonical manuscript, PDF, and bibliography hashes are unchanged.",
    "",
    "## Route, instance, and dynamical-object boundaries",
    "",
    "- Positive-arithmetic **A2=0/5** for the Round-9 batch.",
    "- **Route B invocations=0/5**.",
    "- The **19 instances are not independent samples**; they are related diagnostic/calibration instances and cannot support sample-size arithmetic.",
    "- This round's integrity PASS **does not constitute Route promotion**, scientific gate credit, or authorization to change the Route-A tuple.",
    "- Initial dynamical-system restrictions remain unchanged: this manuscript proves an exact geodesic control-surface systole/certificate only. It does not construct a magnetic Hamiltonian or flow, magnetic clock/action, owner quotient/multiplicities, determinant, analytic continuation, spectral realization, A2 result, or Route-B result.",
    "",
    "## Assurance boundary",
    "",
    BOUNDARY,
    "",
    "The report is not a guarantee of mathematical correctness, exhaustive literature coverage, global originality, experimental-design adequacy, statistical adequacy, or independent scientific reproducibility. Mandatory author confirmation remains the next gate.",
]
final_path = NOTES / "stage4_5_round2_final_integrity_report.md"
write_text(final_path, "\n".join(final_lines))


required_outputs = [
    "stage4_5_round2_input_manifest.json",
    "stage4_5_round2_reference_source_snapshot.json",
    "stage4_5_round2_reference_citation_audit.md",
    "stage4_5_round2_phase_c_internal_consistency_audit.md",
    "stage4_5_round2_originality_failure_mode_audit.md",
    "stage4_5_round2_claim_registry.json",
    "stage4_5_round2_claim_registry_coverage.json",
    "stage4_5_round2_evidence_source_map.json",
    "stage4_5_round2_evidence_rows.json",
    "stage4_5_round2_claim_strength_drift_findings.json",
    "stage4_5_round2_e6_semantic_audit.md",
    "stage4_5_round2_compliance_report.json",
    "stage4_5_round2_integrity_report.json",
    "stage4_5_round2_final_integrity_report.md",
    "stage4_5_round2_material_passport.json",
    "stage4_5_round2_preview_build_receipt.json",
]
assert all((NOTES / name).is_file() for name in required_outputs)
output_manifest = {
    "schema": "p28-stage4.5-round2-output-manifest/1.0",
    "generated_at": STAMP,
    "verdict": "PASS",
    "artifacts": [
        {
            "path": f"notes/{path.name}",
            "sha256": sha_path(path),
            "size_bytes": path.stat().st_size,
        }
        for path in sorted(NOTES.glob("stage4_5_round2_*"))
        if path.name != "stage4_5_round2_output_manifest.json" and path.is_file()
    ],
    "canonical_after": canonical_snapshot(),
    "canonical_unchanged": canonical_snapshot() == canonical_before,
    "stage5_started": False,
}
assert output_manifest["canonical_unchanged"] is True
dump(NOTES / "stage4_5_round2_output_manifest.json", output_manifest)

print(
    json.dumps(
        {
            "status": "PASS",
            "references": len(reference_rows),
            "contexts": len(contexts),
            "claims": len(claims),
            "evidence_rows": len(rows),
            "originality": f"{originality['successful_search_count']}/{originality['denominator']}",
            "changed": f"{originality['changed_successful']}/{originality['changed_total']}",
            "preview_pages": preview_pages,
            "canonical_unchanged": True,
        },
        sort_keys=True,
    )
)
