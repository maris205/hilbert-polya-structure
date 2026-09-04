#!/usr/bin/env python3
"""Emit the authorized P29/P32 Round-3 writer artifacts without applying them.

The script keeps the authority-builder and draft-writer roles explicit:

1. project the hash-bound expanded request into fresh Schema-7/claim/author
   authority artifacts and invoke the official ``revision_roadmap.py``
   ``build-adjudication`` command;
2. hand the resulting immutable hashes to the writer emission routine;
3. emit exactly the request's 46 ``replace_block`` operations; and
4. validate the emission without importing or invoking the patch applier.

It deliberately creates no successor TeX/PDF, apply report, build output,
canonical artifact, scientific result, Route file, initial-system file, or
README mutation.
"""

from __future__ import annotations

import datetime as dt
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/"
    "academic-research-suite/ars"
)
ARS_SCRIPTS = ARS_ROOT / "scripts"
REVISION_ROADMAP_CLI = ARS_SCRIPTS / "revision_roadmap.py"
sys.path.insert(0, str(ARS_SCRIPTS))

from _block_parser import parse_document  # noqa: E402
import revision_roadmap as rr  # noqa: E402


REQUEST = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json"
REQUEST_SHA256 = "51735eed804f9bd933e2f5a1f69ad0068b74921b4ab6fc4cdddaade0b6bc2e5b"
AUTH_RECEIPT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHORIZATION_RECEIPT.json"
AUTH_RECEIPT_SHA256 = "b154d92f84487b381b50e2e9addb5aecd924c6d9d2fb2277d6604a5cb42a17d1"
INPUT_FREEZE = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_INPUT_FREEZE.json"
INPUT_FREEZE_SHA256 = "e835f073d785fbad2de809fcf44dd24bc4abf98300ed21857d3b5e9f67751ce4"
AUTHOR_EVENT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHOR_EVENT_20260904.txt"
AUTHOR_EVENT_SHA256 = "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812"
AUTHOR_EVENT_BYTES = b"\xe7\xa1\xae\xe8\xae\xa4\xef\xbc\x8c\xe4\xb8\x8b\xe4\xb8\x80\xe8\xbd\xae\n"

PAPER_CONFIG = {
    "P29": {
        "slug": "29-bianchi-ideal-owner-refinement",
        "op_count": 31,
        "source_summary": {
            "registered_contexts": 22,
            "exact_locators_finalized": 13,
            "prior_bounded_scopes_retained": 0,
            "explicit_bounded_unavailability": 9,
            "passage_bounded_total": 13,
        },
    },
    "P32": {
        "slug": "32-homology-cover-renormalization-uniformity",
        "op_count": 15,
        "source_summary": {
            "registered_contexts": 30,
            "exact_locators_finalized": 18,
            "prior_bounded_scopes_retained": 4,
            "explicit_bounded_unavailability": 8,
            "passage_bounded_total": 22,
        },
    },
}

SUPERSEDED_PATCH_SHA256 = {
    "P29": "c5394ec96262398498e8e7d492a915a5739c019e429502a850932cfde96c6e67",
    "P32": "55c06a97fdcbff2a2ef6a8adb38b70b2509815e01880a0af60ee3049f818662e",
}

# These sentences are deliberately no broader than the retained excerpts.  In
# particular, a title, opening fragment, or table-of-contents entry is never
# promoted into support for the manuscript's former aggregate motivation.
P29_EXACT_EXCERPT_SCOPE = {
    "P29-S01": (
        "the excerpt identifies PSL(2,Z[i]) as the Picard group, places it in "
        "three-dimensional hyperbolic space, and begins to describe a prime-geodesic study"
    ),
    "P29-S02": (
        "the excerpt identifies the Picard manifold as a quotient by "
        "PSL(2,Z[i]) and frames the work around the prime geodesic theorem"
    ),
    "P29-S03": (
        "the excerpt says that a result of Bykovskii is generalized to the Gaussian "
        "integers and that an asymptotic formula is proved for the prime geodesic theorem"
    ),
    "P29-S08": (
        "the excerpt reports prime-geodesic theorems counting primitive closed geodesics "
        "on a compact hyperbolic three-manifold and mentions length and holonomy constraints"
    ),
    "P29-S06": (
        "the excerpt reports a Selberg-zeta approach to reducing an error-term exponent "
        "in a prime geodesic theorem"
    ),
    "P29-S07": (
        "the excerpt states that an error-term exponent is corrected for a prime "
        "geodesic theorem on hyperbolic three-manifolds and in Park's theorem"
    ),
    "P29-S09": (
        "the excerpt states that the work improves an error term in the prime geodesic "
        "theorem for the Picard manifold"
    ),
    "P29-S10": (
        "the excerpt identifies arithmetic Kleinian groups as arithmetic lattices in "
        "PSL(2,C) and announces an algorithm taking such a group as input; the retained "
        "fragment does not state the algorithm's output"
    ),
    "P29-S13": (
        "the excerpt states that the conjugacy problem in word-hyperbolic groups is "
        "solvable in linear time"
    ),
    "P29-S14": (
        "the excerpt announces an algorithm that decides whether two matrices in "
        "GL(n,Q) are conjugate in GL(n,Z)"
    ),
    "P29-S20": (
        "the excerpt describes the paper as a discussion of basic problems in "
        "algorithmic algebraic number theory"
    ),
    "P29-S21": (
        "the excerpt describes practical algorithms in computational algebraic number "
        "theory and mentions applications to class field theory"
    ),
    "P29-S22": (
        "the excerpt announces an algorithm taking an integral ideal in a number field "
        "as input; the retained fragment does not state the algorithm's output"
    ),
}

P32_EXACT_EXCERPT_SCOPE = {
    "P32-S02": (
        "the conjugacy problem in word-hyperbolic groups is solvable in linear time"
    ),
    "P32-S03": (
        "a quadratic-time algorithm decides conjugacy of finite subsets in a "
        "torsion-free hyperbolic group"
    ),
    "P32-S04": (
        "the article sets up a word-hyperbolic group with a finite generating set; "
        "the retained fragment does not state an algorithmic conclusion"
    ),
    "P32-S06": (
        "the article investigates the displayed symmetric presentation of a surface "
        "group; the excerpt states no normal-form, conjugacy, or root-finding result"
    ),
    "P32-S07": (
        "the article considers a finite abelian group and a closed surface; the "
        "retained fragment stops before stating the classification or enumeration object"
    ),
    "P32-S11": "the article counts closed orbits in a homology class",
    "P32-S12": (
        "the excerpt says that a preceding chapter constructed a Riemannian covering "
        "realizing a wreath product"
    ),
    "P32-S15": (
        "the article begins by extending a zeta function for an Axiom A flow "
        "restricted to a basic set; the retained fragment does not state the extension's target"
    ),
    "P32-S16": (
        "the excerpt defines a finite-volume quotient of hyperbolic three-space by a "
        "discrete subgroup of SL(2,C)"
    ),
    "P32-S17": "the article studies the Ruelle and Selberg zeta functions",
    "P32-S18": (
        "the article gives a short microlocal proof of meromorphic continuation of "
        "the Ruelle zeta function"
    ),
    "P32-S19": (
        "the table of contents contains an item titled `Periodic orbits of suspension "
        "flows'; the retained passage states no renewal theorem"
    ),
    "P32-S21": (
        "the article considers transitive Anosov flows and homology classes; the "
        "retained fragment stops before stating the announced conditions"
    ),
    "P32-S22": (
        "the article considers two counting problems for compact negatively curved "
        "surfaces and says that it improves classical asymptotic estimates"
    ),
    "P32-S23": (
        "the contents contain a section titled `Well-ordered sequences in an ordered semigroup'"
    ),
    "P32-S24": "the dissertation abstract begins by saying that it studies a power-series ring",
    "P32-S25": (
        "the article introduces embedding codimension for an arbitrary local ring; "
        "the excerpt does not discuss adic completion"
    ),
    "P32-S26": "the cited DLMF surface is only the section heading `Power Series'",
}

STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def json_bytes(value: object, *, canonical: bool = False) -> bytes:
    if canonical:
        return rr.canonical_bytes(value) + b"\n"
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def binding(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha_bytes(raw),
        "bytes": len(raw),
    }


def binding_for(path: Path, raw: bytes) -> dict[str, Any]:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha_bytes(raw),
        "bytes": len(raw),
    }


def latex_hash(value: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{64}", value):
        raise ValueError(f"not a SHA-256: {value}")
    return r"\texttt{" + r"\allowbreak{}".join(value[i : i + 8] for i in range(0, 64, 8)) + "}"


def tex_text(value: str) -> str:
    """Escape the small plain-text locator vocabulary used in this run."""
    return (
        value.replace("\\", r"\textbackslash{}")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
    )


def cap_sentence(value: str) -> str:
    value = value.strip().rstrip(".")
    if not value:
        raise RuntimeError("empty preserved prohibition")
    return value[0].upper() + value[1:] + "."


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one replacement site, found {count}")
    return text.replace(old, new, 1)


def insert_before_endgroup(text: str, addition: str, *, label: str) -> str:
    marker = r"\par\endgroup"
    if not text.endswith(marker):
        raise RuntimeError(f"{label}: expected terminal {marker}")
    return text[: -len(marker)].rstrip() + "\n\n" + addition.strip() + "\n" + marker


def citation_keys(text: str) -> list[str]:
    keys: list[str] = []
    for match in re.finditer(r"\\cite[a-zA-Z*]*\{([^}]*)\}", text):
        keys.extend(key.strip() for key in match.group(1).split(",") if key.strip())
    return keys


def source_status_tex(row: dict[str, Any]) -> str:
    status = row["finalization_status"]
    return status.replace("_", r"\_")


def p29_citation_replacement(old: str, row: dict[str, Any]) -> str:
    lines = old.splitlines()
    try:
        comment_at = next(i for i, line in enumerate(lines) if line.startswith("% ARS-CITE "))
    except StopIteration as exc:
        raise RuntimeError(f"{row['block_id']}: missing ARS-CITE marker") from exc
    prose = " ".join(line.strip() for line in lines[:comment_at]).strip()
    cite_lines = lines[comment_at + 1 :]
    if len(cite_lines) != 1 or row["source_id"] not in cite_lines[0]:
        raise RuntimeError(f"{row['block_id']}: unexpected citation line")
    if ". " not in prose:
        raise RuntimeError(f"{row['block_id']}: cannot isolate contextual sentence")
    first, second = prose.split(". ", 1)
    first += "."
    if ", and " in second:
        prohibition = second.rsplit(", and ", 1)[1]
    elif ", with no " in second:
        prohibition = "no " + second.rsplit(", with no ", 1)[1]
    else:
        raise RuntimeError(f"{row['block_id']}: cannot preserve prohibited-transfer clause")

    if row["finalization_status"] == "EXACT_LOCATOR_FINALIZED":
        locator = tex_text(row["exact_passage_locator"])
        digest = row["support_excerpt_sha256"]
        excerpt_scope = P29_EXACT_EXCERPT_SCOPE.get(row["source_id"])
        if excerpt_scope is None:
            raise RuntimeError(
                f"{row['block_id']}: no excerpt-bounded semantic scope for {row['source_id']}"
            )
        body = (
            "Within the frozen corpus, this citation is limited to the following "
            f"source-side statement: {excerpt_scope}. The Round-3 source-finalization "
            rf"record binds that statement to \emph{{{locator}}} and to support-excerpt "
            f"SHA-256 {latex_hash(digest)}. No broader proposition from the earlier "
            "context sentence is attributed to this passage. "
            f"{cap_sentence(prohibition)}"
        )
        comment = (
            f"% ARS-CITE source_ids={row['source_id']} context_id={row['context_id']} "
            "anchor=recorded_exact_locator claim_to_passage=EXACT_LOCATOR_FINALIZED "
            f"support_excerpt_sha256={digest}"
        )
    elif row["finalization_status"] == "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY":
        body = (
            "Within the frozen corpus, this citation is retained only as an explicitly "
            "metadata-only source record. The bounded Round-3 finalization pass yielded no "
            "passage-bearing locator, so no substantive proposition from the earlier context "
            "sentence is attributed to this source at passage level. "
            f"{cap_sentence(prohibition)}"
        )
        if row["source_id"] == "P29-S11":
            body = body.replace("Serialization are not imported.", "No serialization rule is imported.")
        comment = (
            f"% ARS-CITE source_ids={row['source_id']} context_id={row['context_id']} "
            "anchor=none claim_to_passage=EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY "
            "support_excerpt_sha256=none"
        )
    else:
        raise RuntimeError(f"{row['block_id']}: unsupported status {row['finalization_status']}")
    return "\n".join([body, comment, *cite_lines])


def p32_group_replacement(old: str, rows_by_source: dict[str, dict[str, Any]]) -> str:
    groups = re.findall(r"\\citep\{([^}]*)\}", old)
    marker_groups = re.findall(r"^% ARS-CITE source_ids=([^ ]+)", old, flags=re.MULTILINE)
    if groups != marker_groups or not groups:
        raise RuntimeError("P32 source block citation/annotation groups do not align")

    out: list[str] = []
    for ids_text in groups:
        source_ids = ids_text.split(",")
        rows = [rows_by_source[source_id] for source_id in source_ids]
        exact = [row for row in rows if row["finalization_status"] == "EXACT_LOCATOR_FINALIZED"]
        unavailable = [
            row
            for row in rows
            if row["finalization_status"] == "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY"
        ]
        if len(exact) + len(unavailable) != len(rows):
            raise RuntimeError(f"unexpected P32 source status in {source_ids}")
        out.append("The source-level dispositions in this citation group are separated as follows.")
        for row in rows:
            if row in exact:
                excerpt_scope = P32_EXACT_EXCERPT_SCOPE.get(row["source_id"])
                if excerpt_scope is None:
                    raise RuntimeError(
                        f"no excerpt-bounded semantic scope for {row['source_id']}"
                    )
                out.append(
                    f"For {row['source_id']}, the bound excerpt at "
                    rf"\emph{{{tex_text(row['exact_passage_locator'])}}} supports only that "
                    f"{excerpt_scope}; its support-excerpt SHA-256 is "
                    f"{latex_hash(row['support_excerpt_sha256'])}."
                )
            else:
                out.append(
                    f"{row['source_id']} is retained only as a metadata-identified record: "
                    "the bounded pass finalized no passage-bearing locator, and no substantive "
                    "proposition in this manuscript is attributed to it at passage level."
                )
        if "P32-S17" in source_ids:
            out.append(
                "The separately frozen correction lineage for P32-S17 remains a provenance "
                "constraint; it is not evidence supplied by the retained excerpt."
            )
        out.append(
            "No source in this group is transferred to a P32 owner interface, factor "
            "derivation, formal equality, tail theorem, scientific result, or Route credit."
        )
        out.append(rf"\citep{{{ids_text}}}.")
        if exact and unavailable:
            status = "MIXED_EXACT_AND_EXPLICIT_UNAVAILABILITY"
            anchor = "recorded_exact_locator_or_none"
        elif exact:
            status = "EXACT_LOCATOR_FINALIZED"
            anchor = "recorded_exact_locator"
        else:
            status = "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY"
            anchor = "none"
        support = ",".join(
            f"{row['source_id']}:{row['support_excerpt_sha256']}" for row in exact
        ) or "none"
        exact_status = "EXACT_LOCATOR_FINALIZED" if exact else "none"
        unavailable_status = (
            "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY" if unavailable else "none"
        )
        out.append(
            f"% ARS-CITE source_ids={ids_text} anchor={anchor} claim_to_passage={status} "
            f"exact_status={exact_status} unavailable_status={unavailable_status} "
            f"support_excerpt_sha256={support}"
        )
    return "\n".join(out)


def p29_new_texts(
    blocks: dict[str, Any], source: dict[str, Any], matrix_path: Path, validation_path: Path
) -> dict[str, str]:
    notes = matrix_path.parent
    source_path = notes / "stage4_prime_source_finalization_round3.json"
    rows_by_block = {row["block_id"]: row for row in source["rows"]}
    texts: dict[str, str] = {}
    for block_id, row in rows_by_block.items():
        texts[block_id] = p29_citation_replacement(blocks[block_id].normalized_text, row)

    matrix_binding = binding(matrix_path)
    source_binding = binding(source_path)
    validation_binding = binding(validation_path)
    matrix_addition = rf"""The completed Round-3 source-finalization inputs are
\path{{notes/stage4_prime_source_finalization_round3.json}} (SHA-256
{latex_hash(source_binding['sha256'])}), the 22-row claim--passage matrix
\path{{notes/stage4_prime_claim_passage_matrix_round3.json}} (SHA-256
{latex_hash(matrix_binding['sha256'])}), and its deterministic validation receipt
\path{{notes/stage4_prime_source_finalization_round3_validation.json}} (SHA-256
{latex_hash(validation_binding['sha256'])}).  The matrix records exactly 13 finalized
passage locators and nine explicit bounded-unavailability, metadata-only records.
Each locator supports only its row's stated contextual use; none supplies a
project-specific owner law, quotient procedure, scientific result, or Route credit."""
    texts["B0080"] = insert_before_endgroup(
        blocks["B0080"].normalized_text, matrix_addition, label="P29 B0080"
    )
    texts["B0107"] = insert_before_endgroup(
        blocks["B0107"].normalized_text, matrix_addition, label="P29 B0107"
    )

    texts["B0109"] = r"""Liang Wang made the recorded stage-gate confirmations and
author-adjudicated framing decisions. Neither that responsibility nor the present
composition implies human full-text or source-passage verification. Stage 2.5 is
complete. The bounded Round-3 source finalization records 13 exact passage locators
and nine explicit metadata-only unavailability records across 22 contexts. Passage
support is limited to those row-specific uses; the prior Stage-4.5 Round-1 verdict
remains a correction-required failure until a fresh post-apply Stage-4.5 audit is
separately authorized and passed. No owner, quotient, statistic, scientific result,
or Route advancement follows from the locator work."""

    texts["B0108"] = r"""\section*{AI-Assistance Disclosure and Verification Limitation}
OpenAI Codex, operating in the GPT-5 model family, assisted during sessions dated
2--4 September 2026 UTC; the exact backend snapshot or build was not exposed.
Assistance covered organization of the frozen bibliography and source identities,
bounded evidence synthesis, drafting and review integration, LaTeX conversion,
deterministic checks of identifiers, citations, references, hashes, and word counts,
and on 3--4 September the Stage-4/Stage-4-prime provenance work, bounded source
finalization, scope-reissue preparation, authority projection, and writer-side patch
emission. No AI-authored scientific data, experiment, mechanism, quotient, proof, or
numerical result is presented. Procedural role separation inside one model family is
not independent validation and retains a correlated-error limitation. AI assistance
is not credited with authorship."""

    old = blocks["B0004"].normalized_text
    stale = (
        "Because every inherited citation lacks a passage locator, claim-to-passage "
        "support remains inconclusive."
    )
    current = (
        "Across the 22 inherited citation contexts, 13 exact passage locators are "
        "finalized and nine uses are explicitly limited to metadata-only records "
        "because no passage-bearing locator was finalized; each bound supports only "
        "its stated contextual use."
    )
    texts["B0004"] = replace_once(old, stale, current, label="P29 B0004 locator clause")

    texts["B0050"] = r"""The method has an explicit evidentiary ceiling. In this paper,
the 22 inherited prose citation contexts now split into 13 exact, row-bounded passage
locators and nine explicit bounded-unavailability, metadata-only records. The exact
locators identify an abstract, theorem-adjacent section, page, or paragraph surface
and bind a short support excerpt; they do not discharge project-specific hypotheses
or justify a stronger transfer. The unavailable rows do not guess a locator. Across
the five-paper Round-10 batch, historical aggregate statements are retained only as
workflow context and are not recalculated here. No direct quotation appears, and no
scientific value, owner law, quotient result, or Route status is inferred."""

    texts["B0054"] = r"""Source identity remains separate from passage support. The
source inventory, DOI closure, bounded metadata checks, and support-role coding
justify citing a record for a narrow contextual purpose. Thirteen row-specific exact
locators now bound those contextual uses; nine other rows explicitly remain
metadata-only because the bounded pass finalized no passage-bearing surface. Neither
class identifies a project theorem or discharges its hypotheses. The correction
relation between P29-S06 and P29-S07 is retained, and the preprint status of P29-S09
remains visible, but neither condition is converted into a general integrity
clearance. This is a deliberate limit of the manuscript rather than a silent
assumption."""

    texts["B0090"] = r"""Of the 22 paper-specific citation contexts, 13 have exact,
row-bounded passage locators and support-excerpt digests, while nine are explicit
bounded-unavailability, metadata-only records. Statements near theorem boundaries
remain narrowed to the recorded contextual scope. The locator work certifies no
theorem-hypothesis transfer, maximal-root formula, conjugacy procedure, or split-ideal
fact for this project. P29-S06/P29-S07 correction handling remains mandatory,
structured retraction screening was not run, and source-level conflicts were not
audited. Historical five-paper batch counts are workflow context, not a refreshed
scientific or bibliographic result."""

    texts["B0091"] = r"""No separately authorized field-wide novelty analysis was
performed. Passage adjudication is limited to 13 exact contextual locators and nine
explicit metadata-only unavailability records in the 22-row matrix. The contribution
therefore remains the manuscript's project-specific synthesis and prospective
specification; it is not a priority claim against all certificate-methods,
proof-carrying computation, or arithmetic-dynamics workflows. The exact locators do
not strengthen any scientific claim, while unavailable rows authorize no passage
transfer. The machine-audit comments preserve those boundaries."""
    return texts


def p32_new_texts(
    blocks: dict[str, Any], source: dict[str, Any], matrix_path: Path, validation_path: Path
) -> dict[str, str]:
    notes = matrix_path.parent
    source_path = notes / "stage4_prime_source_finalization_round3.json"
    rows_by_source = {row["source_id"]: row for row in source["rows"]}
    texts: dict[str, str] = {}
    for block_id in ["B0024", "B0028", "B0032", "B0033", "B0036", "B0039"]:
        texts[block_id] = p32_group_replacement(blocks[block_id].normalized_text, rows_by_source)

    matrix_binding = binding(matrix_path)
    source_binding = binding(source_path)
    validation_binding = binding(validation_path)
    matrix_addition = rf"""The current bounded source layer is
\path{{notes/stage4_prime_source_finalization_round3.json}} (SHA-256
{latex_hash(source_binding['sha256'])}); its 30-row projection is
\path{{notes/stage4_prime_claim_passage_matrix_round3.json}} (SHA-256
{latex_hash(matrix_binding['sha256'])}), with deterministic validation at
\path{{notes/stage4_prime_source_finalization_round3_validation.json}} (SHA-256
{latex_hash(validation_binding['sha256'])}).  The matrix retains four prior bounded
closest-work scopes, finalizes exact locators for 18 inherited-source uses, and
records eight inherited uses as explicitly unavailable and metadata-only. These
bounds support only their row-specific contextual roles and create no owner panel,
factor, formal equality, tail theorem, scientific result, or Route credit."""
    texts["B0125"] = insert_before_endgroup(
        blocks["B0125"].normalized_text, matrix_addition, label="P32 B0125"
    )

    texts["B0119"] = r"""This manuscript is a design-level advance, not a mathematical
obstruction or recovery result. No owner interface, factor derivation, coefficient
test, panel, compact-uniform bound, limit, or scientific computation was executed.
The current 30-row passage matrix retains four prior bounded closest-work scopes,
finalizes exact locators for 18 inherited-source uses, and records eight inherited
uses as explicitly unavailable and metadata-only. Those bounds support only their
recorded contextual roles. Arithmetic A0 remains unavailable, the formal Route-A
tuple remains \texttt{UNASSIGNED}, positive arithmetic A2 remains absent, and Route B
remains closed."""

    texts["B0127"] = r"""OpenAI Codex, using the GPT-5 model family, assisted during
sessions dated 2026-09-02 through 2026-09-04 UTC; the exact backend snapshot/build
was not exposed. Recorded AI-assisted work included literature-search support,
source-identity and metadata checking, evidence-matrix construction, evidence
synthesis, report drafting, role-based reviews, review synthesis,
ClaimIntent-constrained Revision-1 drafting, citation/reference closure checks,
source-status preservation checks, stable-ID revision accounting, and on 3--4
September the Stage-4-prime Round-2 provenance work, Stage-4.5 audit support,
bounded source finalization, scope-reissue authority projection, and writer-side
Round-3 patch emission. No AI system executed an owner interface, cover calculation,
factor derivation, coefficient test, numerical panel, limit proof, experiment,
obstruction certificate, or canonical-results refresh."""

    texts["B0138"] = r"""\begingroup\sloppy
\paragraph{Development provenance.} Four procedurally separated review
labels---citation integrity, Devil's Advocate, editorial, and ethics/integrity---were
instantiated within one Codex model family. Their same-family, correlated-error
limitation remains explicit; role separation is not independent validation. The
recorded \texttt{MAJOR\_REVISION} code and Liang Wang's author adjudication are
workflow history, not evidence for a factor, formal equality, inequality application,
obstruction, recovery result, or limit theorem. The 3--4 September Stage-4-prime
Round-2 and Stage-4.5 assistance is included in that limitation. The current 30-row
matrix retains four prior bounded closest-work scopes, finalizes 18 inherited-source
locators, and records eight inherited uses as explicitly unavailable and
metadata-only; none is transferred beyond its row-specific contextual role.
\par\endgroup"""

    old = blocks["B0006"].normalized_text
    stale = (
        "All 26\ninherited citations retain \\texttt{anchor:none}; P32-S13 is\n"
        "bibliographically \\texttt{VERIFIED} but remains background-only, so\n"
        "claim-to-passage faithfulness is \\texttt{INCONCLUSIVE}."
    )
    current = (
        "Across the current 30-row matrix, four prior closest-work scopes remain\n"
        "bounded, 18 inherited-source exact locators are finalized, and eight\n"
        "inherited uses are explicitly metadata-only because no passage-bearing\n"
        "locator was finalized. P32-S13 remains bibliographically\n"
        "\\texttt{VERIFIED} but belongs to that bounded-unavailability group; none\n"
        "of these passage statuses establishes a project theorem."
    )
    texts["B0006"] = replace_once(old, stale, current, label="P32 B0006 locator clause")

    texts["B0047"] = rf"""\begingroup\sloppy
Citation closure is recorded in the current 30-row source-to-claim matrix at
\path{{notes/stage4_prime_claim_passage_matrix_round3.json}} (SHA-256
{latex_hash(matrix_binding['sha256'])}). Its immutable source-finalization input is
\path{{notes/stage4_prime_source_finalization_round3.json}} (SHA-256
{latex_hash(source_binding['sha256'])}), and the deterministic validation receipt is
\path{{notes/stage4_prime_source_finalization_round3_validation.json}} (SHA-256
{latex_hash(validation_binding['sha256'])}). Four prior closest-work scopes remain
bounded; 18 inherited-source uses now have exact locators and hashed support
excerpts; eight inherited uses are explicitly metadata-only because no passage-
bearing locator was finalized. The Round-3 matrix rows record source and context IDs,
base-block bindings, passage status, exact locator where available, support-excerpt
digest and word count, and the authorized future disposition. Hypotheses, correction
lineage, applicability, and prohibited stronger transfers remain manuscript-side
boundaries; they are not represented as fields that the Round-3 matrix does not
contain. No direct quotation is introduced, metadata identity is not treated as
theorem verification, and no row establishes a P32 owner interface, factor, formal
application, tail theorem, joint novelty, scientific result, or Route credit.
\par\endgroup"""

    texts["B0109"] = r"""The dated supplement exposes all 51 current replay
manifestations and their row decisions, but it is not a reconstruction of the
unavailable historical 51 rows. Its 19 inventory matches, 31 out-of-scope screens,
and one duplicate do not replace or recalculate the frozen 26-source corpus. The
current 30-row claim--passage matrix retains four prior bounded closest-work scopes,
finalizes exact locators for 18 inherited-source uses, and records eight inherited
uses as explicitly unavailable and metadata-only. These row-specific bounds neither
reconstruct missing evidence nor expand correction, retraction, source-conflict, or
conflict-of-interest screening. No scientific result or remote access state is
refreshed."""

    texts["B0128"] = r"""Liang Wang is the responsible human author. He approved the
project restrictions, workflow gates, and the Phase-6 falsification-first design
choice. Those approvals do not state that he personally read every source in full.
The bounded source work now records four retained closest-work scopes, 18 exact
locators for inherited-source contextual uses, and eight explicit metadata-only
unavailability records. Exact locators and support-excerpt digests do not establish
project-specific theorem applicability; unavailable rows authorize no passage
transfer. The article does not claim comprehensive full-text verification, novelty,
impossibility, or a clean retraction/conflict screen."""

    texts["B0137"] = r"""The current notes-side inventory includes the immutable
Round-3 source-finalization record, its 30-row claim--passage matrix, and the
deterministic validation receipt; their exact digests are reported in the data and
materials paragraph. Successor draft, apply, build, and repository-sync status are
separate downstream provenance events and are not inferred from writer emission.
The commit locator remains content-addressed but is not a persistent archive,
release DOI, or preservation guarantee. Artifact hash closure does not make prose
generation deterministic, passage transfer theorem-verified, or any scientific
result reproducible.
\par\endgroup"""
    return texts


def roadmap_for(paper: dict[str, Any], *, base_sha: str, manifest_sha: str) -> tuple[dict[str, Any], dict[str, str]]:
    items: list[dict[str, Any]] = []
    issue_map: dict[str, str] = {}
    for ordinal, issue in enumerate(paper["issues"], start=1):
        source_id = issue["issue_id"]
        item_id = f"REV-{source_id}"
        issue_map[source_id] = item_id
        block_ids = [target["block_id"] for target in issue["proposed_targets"]]
        targets = [
            {
                "block_id": target["block_id"],
                "allowed_operations": list(target["allowed_operations"]),
            }
            for target in issue["proposed_targets"]
        ]
        items.append(
            {
                "id": item_id,
                "source_refs": [
                    {"seat": "EIC", "channel": "editorial", "ordinal": ordinal, "subclaim_ordinal": 0}
                ],
                "description": (
                    f"Source issue {source_id}; request severity {issue['severity']}. "
                    f"{issue['implementation_branch']}"
                ),
                "reviewer": "Hash-bound Round-10 Stage-4.5 correction scope-reissue request",
                "source_kind": "editorial",
                "obligation_class": "must_fix",
                "cost_scope": {
                    "kind": "other",
                    "surface_id": "exact_replace_block_set",
                    "locator": ",".join(block_ids),
                },
                "consequence_if_unaddressed": {
                    "code": "reader_traceability_reduced",
                    "target": {"kind": "manuscript", "locator": ",".join(block_ids)},
                },
                "target_section": ",".join(block_ids),
                "suggested_action": issue["implementation_branch"],
                "consensus_level": "SINGLE-VERIFIER",
                "verification_criteria": (
                    f"Emit exactly {len(targets)} replace_block operation(s), in the request's "
                    "source_traceability order, on the listed targets only; preserve every "
                    "scientific, claim-strength, Route, initial-system, and stage boundary in "
                    "the expanded request."
                ),
                "proposed_targets": targets,
            }
        )
    roadmap = {
        "schema_version": "revision-roadmap/1.0",
        "revision_round": 3,
        "base_draft_sha256": base_sha,
        "block_manifest_sha256": manifest_sha,
        "items": items,
        "total_items": len(items),
        "obligation_counts": {"must_fix": len(items), "should_fix": 0, "consider": 0},
        "editorial_decision": "Major Revision",
        "consensus_summary": (
            "Mechanical projection of the four hash-bound correction issues; this non-ranking "
            "roadmap grants no write, claim-strength, collateral, scientific, Route, or later-stage authority."
        ),
        "dissenting_opinions": [],
    }
    return roadmap, issue_map


def author_choices_for(item_ids: list[str], issue_targets: dict[str, list[dict[str, Any]]], paper_id: str) -> dict[str, Any]:
    event_id = f"AUTHOR-EVENT-R10-SCOPE-REISSUE-20260904-{paper_id}"
    return {
        "schema_version": "author-adjudication-input/1.0",
        "author_events": [
            {
                "event_id": event_id,
                "source": "explicit_session_user_message",
                "actor_role": "author",
                "input_sha256": AUTHOR_EVENT_SHA256,
            }
        ],
        "display_order": {
            "mode": "source_traceability",
            "item_ids": item_ids,
            "author_event_id": event_id,
        },
        "author_adjudications": [
            {
                "item_id": item_id,
                "author_event_id": event_id,
                "author_triage": "will_address",
                "authorized_targets": issue_targets[item_id],
                "claim_strength_authorizations": [],
            }
            for item_id in item_ids
        ],
        "collateral_authorizations": [],
    }


def markdown_response(paper_id: str, paper: dict[str, Any], issue_map: dict[str, str]) -> str:
    rows = []
    for issue in paper["issues"]:
        blocks = ", ".join(target["block_id"] for target in issue["proposed_targets"])
        rows.append(
            f"| {issue['issue_id']} | {issue_map[issue['issue_id']]} | {issue['severity']} | "
            f"will_address | {blocks} / replace_block | Patch emitted; application and post-apply facts pending |"
        )
    return (
        f"# {paper_id} Stage 4-prime Round-3 provisional response\n\n"
        "Writer-emission artifact only. No patch has been applied, no successor draft has been "
        "created, and no Stage 4.5 finding has been re-adjudicated. The initial writer patch "
        "was superseded after semantic preflight; the controlling patch narrows every located "
        "source statement to what its retained excerpt actually supports.\n\n"
        "| Source issue | Roadmap item | Request severity | Author triage | Exact target/op | Provisional action |\n"
        "|---|---|---|---|---|---|\n"
        + "\n".join(rows)
        + "\n\nMechanical fields such as changed block IDs, fresh block IDs, word-count delta, "
        "and apply status remain for the independent deterministic applier.\n"
    )


def revision_log(paper_id: str, paper: dict[str, Any], issue_map: dict[str, str]) -> str:
    rows = []
    for issue in paper["issues"]:
        scopes = ", ".join(
            f"{target['block_id']}/replace_block" for target in issue["proposed_targets"]
        )
        rows.append(
            f"| {issue_map[issue['issue_id']]} | {issue['issue_id']} | {issue['severity']} | "
            f"must_fix | will_address | {scopes} | Emitted in patch; not applied |"
        )
    return (
        f"# {paper_id} Stage 4-prime Round-3 writer revision log\n\n"
        "| # | Source | Severity | Obligation class | Author triage | Exact target/op | Action Taken |\n"
        "|---|---|---|---|---|---|---|\n"
        + "\n".join(rows)
        + "\n\nSemantic-preflight disposition: the initial patch was superseded before apply; "
        "all source-facing prose was re-audited and narrowed to excerpt-bounded or "
        "explicitly metadata-only wording.\n\n"
        "Role boundary: this log records writer emission only. It contains no apply, build, "
        "scientific-result, Route, canonical-promotion, or Stage 4.5 completion claim.\n"
    )


def main() -> int:
    expected_top = {
        REQUEST: REQUEST_SHA256,
        AUTH_RECEIPT: AUTH_RECEIPT_SHA256,
        INPUT_FREEZE: INPUT_FREEZE_SHA256,
        AUTHOR_EVENT: AUTHOR_EVENT_SHA256,
    }
    for path, expected in expected_top.items():
        if not path.exists() or sha(path) != expected:
            raise RuntimeError(f"frozen control artifact mismatch: {path}")
    if AUTHOR_EVENT.read_bytes() != AUTHOR_EVENT_BYTES:
        raise RuntimeError("author event bytes mismatch")

    request = json.loads(REQUEST.read_text(encoding="utf-8"))
    freeze = json.loads(INPUT_FREEZE.read_text(encoding="utf-8"))
    if request["proposed_display_order"] != "source_traceability":
        raise RuntimeError("expanded request display order drift")
    if request["proposed_author_triage"] != "will_address":
        raise RuntimeError("expanded request triage drift")
    if request["proposed_revision_round"] != 3:
        raise RuntimeError("expanded request round drift")
    if request["totals"]["block_operation_pairs"] != 46:
        raise RuntimeError("expanded request aggregate count drift")
    freeze_by_id = {paper["paper_id"]: paper for paper in freeze["papers"]}
    request_by_id = {paper["paper_id"]: paper for paper in request["papers"]}

    final_artifacts: dict[Path, bytes] = {}
    immutable_artifacts: set[Path] = set()
    captured_existing: dict[Path, bytes] = {}
    new_incident_paths: set[Path] = set()
    summaries: dict[str, Any] = {}

    with tempfile.TemporaryDirectory(prefix="round10-p2932-writer-") as temp_name:
        temp_root = Path(temp_name)
        for paper_id in ("P29", "P32"):
            cfg = PAPER_CONFIG[paper_id]
            paper = request_by_id[paper_id]
            frozen = freeze_by_id[paper_id]
            notes = ROOT / "papers" / cfg["slug"] / "notes"
            base_path = ROOT / frozen["current_working_draft"]["path"]
            bib_path = ROOT / frozen["current_working_bibliography"]["path"]
            manifest_path = ROOT / frozen["block_manifest"]["path"]
            source_path = notes / "stage4_prime_source_finalization_round3.json"
            matrix_path = notes / "stage4_prime_claim_passage_matrix_round3.json"
            source_validation_path = notes / "stage4_prime_source_finalization_round3_validation.json"
            patch_path = notes / "stage4_prime_revision_patch_round3.json"
            response_path = notes / "stage4_prime_response_to_reviewers_provisional_round3.json"
            response_md_path = notes / "stage4_prime_response_to_reviewers_provisional_round3.md"
            log_path = notes / "stage4_prime_revision_log_round3.md"
            receipt_path = notes / "stage4_prime_writer_validation_receipt_round3.json"
            handoff_path = notes / "stage4_prime_correction_round3_writer_handoff.json"
            incident_path = notes / "stage4_prime_correction_round3_semantic_preflight_incident.json"

            prior_chain_paths = [
                patch_path,
                response_path,
                response_md_path,
                log_path,
                receipt_path,
                handoff_path,
            ]
            if incident_path.exists():
                raise RuntimeError(f"{paper_id}: semantic-preflight incident already exists")
            for path in prior_chain_paths:
                if not path.exists():
                    raise RuntimeError(f"{paper_id}: prior writer artifact missing: {path}")
                captured_existing[path] = path.read_bytes()
            if sha_bytes(captured_existing[patch_path]) != SUPERSEDED_PATCH_SHA256[paper_id]:
                raise RuntimeError(f"{paper_id}: superseded patch hash drift")
            for path, field_path in [
                (response_path, ("patch", "sha256")),
                (receipt_path, ("emitted_artifacts", "patch", "sha256")),
                (handoff_path, ("patch", "sha256")),
            ]:
                value: Any = json.loads(captured_existing[path])
                for field in field_path:
                    value = value[field]
                if value != SUPERSEDED_PATCH_SHA256[paper_id]:
                    raise RuntimeError(f"{paper_id}: prior chain does not bind superseded patch at {path}")

            for row in (
                frozen["current_working_draft"],
                frozen["current_working_bibliography"],
                frozen["block_manifest"],
                *frozen["canonical_files"],
                *frozen["science_files"],
                frozen["initial_system_source"],
                frozen["route_crosswalk"],
            ):
                path = ROOT / row["path"]
                if not path.exists() or sha(path) != row["sha256"] or path.stat().st_size != row["bytes"]:
                    raise RuntimeError(f"{paper_id}: frozen boundary drift at {row['path']}")

            request_bindings = [
                paper["current_stage4_prime_draft"],
                paper["current_stage4_prime_bibliography"],
                paper["completed_read_only_source_finalization"],
                paper["completed_read_only_claim_passage_matrix"],
                paper["completed_read_only_source_validation"],
            ]
            for row in request_bindings:
                path = ROOT / row["path"]
                if not path.exists() or sha(path) != row["sha256"] or path.stat().st_size != row["bytes"]:
                    raise RuntimeError(f"{paper_id}: expanded-request binding drift at {row['path']}")

            base_raw = base_path.read_bytes()
            base_sha = sha_bytes(base_raw)
            manifest_raw = manifest_path.read_bytes()
            manifest_sha = sha_bytes(manifest_raw)
            manifest = json.loads(manifest_raw)
            source = json.loads(source_path.read_text(encoding="utf-8"))
            matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
            source_validation = json.loads(source_validation_path.read_text(encoding="utf-8"))
            expected_source = {**cfg["source_summary"], "manuscript_patch_applied": False}
            if source["summary"] != expected_source or matrix["summary"] != expected_source:
                raise RuntimeError(f"{paper_id}: source/matrix summary drift")
            if source_validation.get("verdict") != "PASS" or source_validation.get("failed") != 0:
                raise RuntimeError(f"{paper_id}: source validation is not PASS")

            parsed = parse_document(base_raw.decode("utf-8"))
            blocks = parsed.block_by_id()
            manifest_hashes = {row["block_id"]: row["old_hash"] for row in manifest["blocks"]}
            ordered_pairs: list[tuple[dict[str, Any], dict[str, Any]]] = []
            seen: set[str] = set()
            for issue in paper["issues"]:
                for target in issue["proposed_targets"]:
                    block_id = target["block_id"]
                    if block_id in seen:
                        raise RuntimeError(f"{paper_id}: duplicate target {block_id}")
                    seen.add(block_id)
                    if target["allowed_operations"] != ["replace_block"]:
                        raise RuntimeError(f"{paper_id}: non-replace operation at {block_id}")
                    if block_id not in blocks:
                        raise RuntimeError(f"{paper_id}: target block missing: {block_id}")
                    full_hash = sha_bytes(blocks[block_id].normalized_text.encode("utf-8"))
                    if full_hash != target["expected_old_hash"]:
                        raise RuntimeError(f"{paper_id}: request old hash mismatch at {block_id}")
                    if manifest_hashes.get(block_id) != full_hash[:12]:
                        raise RuntimeError(f"{paper_id}: manifest old hash mismatch at {block_id}")
                    ordered_pairs.append((issue, target))
            if len(ordered_pairs) != cfg["op_count"] or len(seen) != cfg["op_count"]:
                raise RuntimeError(f"{paper_id}: exact operation count mismatch")

            roadmap, issue_map = roadmap_for(paper, base_sha=base_sha, manifest_sha=manifest_sha)
            roadmap_raw = json_bytes(roadmap)
            roadmap_path = notes / "stage4_prime_correction_round3_revision_roadmap.json"
            claim = {
                "schema_version": "claim-surface-manifest/1.0",
                "revision_round": 3,
                "roadmap_sha256": sha_bytes(roadmap_raw),
                "base_draft_sha256": base_sha,
                "claim_intent_sources": [],
                "surfaces": [],
            }
            claim_raw = json_bytes(claim)
            claim_path = notes / "stage4_prime_correction_round3_claim_surface_manifest.json"
            issue_targets = {
                item["id"]: item["proposed_targets"] for item in roadmap["items"]
            }
            item_ids = [item["id"] for item in roadmap["items"]]
            author_choices = author_choices_for(item_ids, issue_targets, paper_id)
            choices_raw = json_bytes(author_choices)
            choices_path = notes / "stage4_prime_correction_round3_author_choices.json"
            adjudication_path = notes / "stage4_prime_correction_round3_author_adjudication.json"

            temp_dir = temp_root / paper_id
            temp_dir.mkdir(parents=True)
            temp_roadmap = temp_dir / roadmap_path.name
            temp_claim = temp_dir / claim_path.name
            temp_choices = temp_dir / choices_path.name
            temp_adjudication = temp_dir / adjudication_path.name
            temp_roadmap.write_bytes(roadmap_raw)
            temp_claim.write_bytes(claim_raw)
            temp_choices.write_bytes(choices_raw)
            completed = subprocess.run(
                [
                    sys.executable,
                    str(REVISION_ROADMAP_CLI),
                    "build-adjudication",
                    str(temp_roadmap),
                    "--base",
                    str(base_path),
                    "--block-manifest",
                    str(manifest_path),
                    "--claim-surface",
                    str(temp_claim),
                    "--author-choices",
                    str(temp_choices),
                    "--artifact-root",
                    str(ROOT),
                    "--output",
                    str(temp_adjudication),
                ],
                cwd=ROOT,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if completed.returncode != 0:
                raise RuntimeError(
                    f"{paper_id}: official build-adjudication failed:\n"
                    + completed.stdout
                    + completed.stderr
                )
            adjudication_raw = temp_adjudication.read_bytes()
            adjudication = json.loads(adjudication_raw)
            if adjudication["collateral_authorizations"] or any(
                row["claim_strength_authorizations"] for row in adjudication["author_adjudications"]
            ):
                raise RuntimeError(f"{paper_id}: unexpected claim/collateral authority")

            if paper_id == "P29":
                texts = p29_new_texts(blocks, source, matrix_path, source_validation_path)
            else:
                texts = p32_new_texts(blocks, source, matrix_path, source_validation_path)

            expected_order = [target["block_id"] for _issue, target in ordered_pairs]
            if list(texts) != expected_order:
                raise RuntimeError(
                    f"{paper_id}: writer text order differs from source_traceability order: "
                    f"{list(texts)} != {expected_order}"
                )

            writer_authority = {
                "base_draft_hash": manifest["base_draft_hash"],
                "roadmap_sha256": sha_bytes(roadmap_raw),
                "author_adjudication_sha256": sha_bytes(adjudication_raw),
                "author_decision_digest": rr.author_decision_digest(adjudication),
                "claim_surface_manifest_sha256": sha_bytes(claim_raw),
            }
            ops = []
            for issue, target in ordered_pairs:
                block_id = target["block_id"]
                new_text = texts[block_id]
                if new_text == blocks[block_id].normalized_text:
                    raise RuntimeError(f"{paper_id}: no-op replacement at {block_id}")
                if "<!--block:" in new_text:
                    raise RuntimeError(f"{paper_id}: forbidden block marker in {block_id}")
                parse_document(new_text, fragment=True)
                if citation_keys(new_text) != citation_keys(blocks[block_id].normalized_text):
                    raise RuntimeError(f"{paper_id}: citation key drift at {block_id}")
                ops.append(
                    {
                        "op": "replace_block",
                        "block_id": block_id,
                        "old_hash": manifest_hashes[block_id],
                        "new_text": new_text,
                        "roadmap_item_ids": [issue_map[issue["issue_id"]]],
                        "claim_strength_changes": [],
                        "collateral_authorization_ids": [],
                    }
                )
            patch = {
                "patch_format_version": "1.1",
                "authorization_context": "review_roadmap",
                "revision_round": 3,
                **writer_authority,
                "ops": ops,
                "emitted_by": "draft_writer_agent",
            }
            patch_raw = json_bytes(patch)
            patch_path = notes / "stage4_prime_revision_patch_round3.json"

            # Official authority/patch replay, deliberately stopping before apply.
            rr.validate_review_patch_authorization(
                patch,
                base_raw=base_raw,
                roadmap=roadmap,
                roadmap_raw=roadmap_raw,
                adjudication=adjudication,
                adjudication_raw=adjudication_raw,
                claim_surface=claim,
                claim_surface_raw=claim_raw,
                surfaces_by_id={},
            )

            # Source rows must be visibly projected into their targeted new text.
            for row in source["rows"]:
                if row["block_id"] not in texts:  # P32 retained CW rows live in untouched B0018.
                    if row["finalization_status"] != "RETAINED_PRIOR_BOUNDED_SCOPE":
                        raise RuntimeError(f"{paper_id}: unprojected source row {row['context_id']}")
                    continue
                new_text = texts[row["block_id"]]
                if row["source_id"] not in new_text:
                    raise RuntimeError(f"{paper_id}: source id missing in {row['block_id']}")
                if row["finalization_status"] == "EXACT_LOCATOR_FINALIZED":
                    if row["exact_passage_locator"] not in new_text:
                        raise RuntimeError(f"{paper_id}: locator missing in {row['block_id']}")
                    if row["support_excerpt_sha256"] not in new_text:
                        raise RuntimeError(f"{paper_id}: excerpt hash missing in {row['block_id']}")
                    excerpt_scope = (
                        P29_EXACT_EXCERPT_SCOPE.get(row["source_id"])
                        if paper_id == "P29"
                        else P32_EXACT_EXCERPT_SCOPE.get(row["source_id"])
                    )
                    if excerpt_scope is None or excerpt_scope not in new_text:
                        raise RuntimeError(
                            f"{paper_id}: excerpt-bounded prose missing for {row['source_id']}"
                        )
                elif "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY" not in new_text:
                    raise RuntimeError(f"{paper_id}: unavailable status missing in {row['block_id']}")

            exact_source_ids = {
                row["source_id"]
                for row in source["rows"]
                if row["finalization_status"] == "EXACT_LOCATOR_FINALIZED"
            }
            expected_scope_ids = set(
                P29_EXACT_EXCERPT_SCOPE if paper_id == "P29" else P32_EXACT_EXCERPT_SCOPE
            )
            if exact_source_ids != expected_scope_ids:
                raise RuntimeError(
                    f"{paper_id}: exact-row semantic scope table mismatch: "
                    f"{sorted(exact_source_ids ^ expected_scope_ids)}"
                )
            if any(
                phrase in op["new_text"]
                for op in ops
                for phrase in (
                    "supports only the preceding contextual statement",
                    "support only the preceding contextual use",
                )
            ):
                raise RuntimeError(f"{paper_id}: aggregate preceding-context support language remains")
            if paper_id == "P32" and "Every row retains its hypotheses" in texts["B0047"]:
                raise RuntimeError("P32: Round-3 matrix field overstatement remains in B0047")

            prior_chain = {
                path.name: binding_for(path, captured_existing[path]) for path in prior_chain_paths
            }
            semantic_findings = {
                "P29": [
                    "The initial exact-locator prose sometimes treated a 20-word opening excerpt as support for a broader contextual sentence.",
                    "The metadata-only prose retained earlier substantive motivation too close to the citation.",
                    "B0034 contained the grammatical defect `Serialization are not imported'.",
                ],
                "P32": [
                    "The initial grouped source blocks attributed aggregate contextual uses across sources whose excerpts supported different, narrower propositions.",
                    "Metadata-only rows appeared adjacent to grouped scientific context without source-specific non-attribution.",
                    "B0047 named hypotheses, correction state, applicability, and prohibited-transfer fields that the Round-3 matrix does not contain.",
                    "B0032 used plural `records' for a single metadata-only source.",
                ],
            }[paper_id]
            incident = {
                "schema_version": "round10-stage4-prime-round3-semantic-preflight-incident/1.0",
                "paper_id": paper_id,
                "recorded_at_utc": STAMP,
                "status": "SUPERSEDED_BEFORE_APPLY",
                "trigger": "independent_cross_track_source_excerpt_semantic_preflight",
                "authority_unchanged": {
                    "execution_receipt_sha256": AUTH_RECEIPT_SHA256,
                    "input_freeze_sha256": INPUT_FREEZE_SHA256,
                    "expanded_request_sha256": REQUEST_SHA256,
                    "author_event_sha256": AUTHOR_EVENT_SHA256,
                    "roadmap_sha256": writer_authority["roadmap_sha256"],
                    "author_adjudication_sha256": writer_authority[
                        "author_adjudication_sha256"
                    ],
                    "author_decision_digest": writer_authority["author_decision_digest"],
                    "claim_surface_manifest_sha256": writer_authority[
                        "claim_surface_manifest_sha256"
                    ],
                },
                "findings": semantic_findings,
                "full_source_scan": {
                    "rows_reviewed": len(source["rows"]),
                    "exact_locator_rows_reviewed": len(exact_source_ids),
                    "explicit_metadata_only_rows_reviewed": sum(
                        row["finalization_status"]
                        == "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY"
                        for row in source["rows"]
                    ),
                    "retained_prior_bounded_rows_reviewed": sum(
                        row["finalization_status"] == "RETAINED_PRIOR_BOUNDED_SCOPE"
                        for row in source["rows"]
                    ),
                    "semantic_rule": (
                        "Each located statement is no broader than its retained excerpt; each "
                        "unavailable row is metadata-only and supports no substantive proposition."
                    ),
                },
                "superseded_patch": prior_chain[patch_path.name],
                "superseded_writer_chain": prior_chain,
                "controlling_patch": binding_for(patch_path, patch_raw),
                "remediation": {
                    "operation_scope_unchanged": True,
                    "operation_count": len(ops),
                    "target_blocks_unchanged": True,
                    "citation_keys_unchanged": True,
                    "claim_strength_increase": False,
                    "collateral_authorization_used": False,
                    "source_prose_rewritten_source_by_source": True,
                    "matrix_description_corrected": paper_id == "P32",
                },
                "boundaries": {
                    "patch_applied": False,
                    "successor_draft_created": False,
                    "latex_build_run": False,
                    "bibliography_or_matrix_mutated": False,
                    "canonical_science_result_route_or_initial_system_mutated": False,
                },
            }
            incident_raw = json_bytes(incident)

            response = {
                "schema_version": "round10-stage4-prime-correction-provisional-response/1.0",
                "artifact_status": "WRITER_EMITTED_NOT_APPLIED",
                "paper_id": paper_id,
                "revision_round": 3,
                "generated_at_utc": STAMP,
                "patch": binding_for(patch_path, patch_raw),
                "semantic_preflight_incident": binding_for(incident_path, incident_raw),
                "authority": {
                    "roadmap": binding_for(roadmap_path, roadmap_raw),
                    "claim_surface_manifest": binding_for(claim_path, claim_raw),
                    "author_choices": binding_for(choices_path, choices_raw),
                    "author_adjudication": binding_for(adjudication_path, adjudication_raw),
                    "author_decision_digest": writer_authority["author_decision_digest"],
                },
                "source_issue_to_roadmap_item": [
                    {"source_issue_id": source_id, "roadmap_item_id": issue_map[source_id]}
                    for source_id in issue_map
                ],
                "items": [
                    {
                        "source_issue_id": issue["issue_id"],
                        "roadmap_item_id": issue_map[issue["issue_id"]],
                        "request_severity": issue["severity"],
                        "author_triage": "will_address",
                        "authorized_targets": [
                            {
                                "block_id": target["block_id"],
                                "operation": "replace_block",
                            }
                            for target in issue["proposed_targets"]
                        ],
                        "status": "PATCH_EMITTED_NOT_APPLIED",
                        "response_text": (
                            "The writer emitted only the exact authorized replacement operations. "
                            "Application, changed/fresh block IDs, word-count delta, and scientific "
                            "or integrity conclusions remain pending."
                        ),
                    }
                    for issue in paper["issues"]
                ],
                "post_apply_fields_pending": [
                    "ops_applied",
                    "change_block_ids",
                    "fresh_block_ids",
                    "word_count_delta",
                    "output_draft_hash",
                ],
                "boundaries": {
                    "patch_applied": False,
                    "successor_draft_created": False,
                    "latex_build_run": False,
                    "stage4_5_run": False,
                    "claim_strength_authority": False,
                    "collateral_authority": False,
                    "bibliography_mutated": False,
                    "canonical_or_scientific_result_mutated": False,
                    "route_or_initial_system_mutated": False,
                },
            }
            response_raw = json_bytes(response)
            response_md_raw = markdown_response(paper_id, paper, issue_map).encode("utf-8")
            log_raw = revision_log(paper_id, paper, issue_map).encode("utf-8")

            checks: list[dict[str, str]] = []

            def check(check_id: str, condition: bool, detail: str) -> None:
                checks.append(
                    {"check_id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail}
                )

            check("W001", sha(REQUEST) == REQUEST_SHA256, "expanded request exact hash")
            check("W002", sha(AUTH_RECEIPT) == AUTH_RECEIPT_SHA256, "execution receipt exact hash")
            check("W003", sha(INPUT_FREEZE) == INPUT_FREEZE_SHA256, "execution freeze exact hash")
            check("W004", sha(AUTHOR_EVENT) == AUTHOR_EVENT_SHA256, "author event exact hash")
            check("W005", base_sha == frozen["current_working_draft"]["sha256"], "base draft exact hash")
            check("W006", sha(bib_path) == frozen["current_working_bibliography"]["sha256"], "Bib unchanged")
            check("W007", manifest_sha == frozen["block_manifest"]["sha256"], "Round-3 manifest exact hash")
            check("W008", source["summary"] == expected_source, "source finalization exact partition")
            check("W009", matrix["summary"] == expected_source, "claim-passage matrix exact partition")
            check("W010", source_validation.get("verdict") == "PASS", "source validation PASS")
            check("W011", len(ordered_pairs) == cfg["op_count"], "request operation count exact")
            check("W012", len(seen) == cfg["op_count"], "request targets unique")
            check("W013", all(t["allowed_operations"] == ["replace_block"] for _, t in ordered_pairs), "closed operation vocabulary")
            check("W014", [op["block_id"] for op in ops] == expected_order, "source_traceability operation order")
            check("W015", len({op["block_id"] for op in ops}) == len(ops), "each block appears once")
            check("W016", all(op["old_hash"] == manifest_hashes[op["block_id"]] for op in ops), "old hashes copied from manifest")
            check("W017", all(op["roadmap_item_ids"] == [issue_map[issue["issue_id"]]] for op, (issue, _t) in zip(ops, ordered_pairs)), "transparent REV-X mapping")
            check("W018", all(not op["claim_strength_changes"] for op in ops), "no claim-strength authority")
            check("W019", all(not op["collateral_authorization_ids"] for op in ops), "no collateral authority")
            check("W020", all("<!--block:" not in op["new_text"] for op in ops), "no block marker in new text")
            check("W021", all(citation_keys(op["new_text"]) == citation_keys(blocks[op["block_id"]].normalized_text) for op in ops), "no citation-key additions/removals")
            check("W022", all(op["new_text"] != blocks[op["block_id"]].normalized_text for op in ops), "no no-op replacement")
            check("W023", patch["patch_format_version"] == "1.1" and patch["authorization_context"] == "review_roadmap", "current review patch branch")
            check("W024", len(adjudication["author_adjudications"]) == len(paper["issues"]), "complete author adjudication")
            check("W025", not adjudication["collateral_authorizations"], "author sidecar has no collateral grants")
            check("W026", all(not a["claim_strength_authorizations"] for a in adjudication["author_adjudications"]), "author sidecar has no claim grants")
            check("W027", writer_authority["roadmap_sha256"] == sha_bytes(roadmap_raw), "roadmap binding copied")
            check("W028", writer_authority["author_adjudication_sha256"] == sha_bytes(adjudication_raw), "adjudication binding copied")
            check("W029", writer_authority["claim_surface_manifest_sha256"] == sha_bytes(claim_raw), "claim manifest binding copied")
            check("W030", claim["surfaces"] == [] and claim["claim_intent_sources"] == [], "fresh empty exact-surface registry")
            check("W031", all(sha(ROOT / row["path"]) == row["sha256"] for row in frozen["canonical_files"]), "canonical files frozen")
            check("W032", all(sha(ROOT / row["path"]) == row["sha256"] for row in frozen["science_files"]), "science/results files frozen")
            check("W033", sha(ROOT / frozen["initial_system_source"]["path"]) == frozen["initial_system_source"]["sha256"], "initial-system source frozen")
            check("W034", sha(ROOT / frozen["route_crosswalk"]["path"]) == frozen["route_crosswalk"]["sha256"], "Route crosswalk frozen")
            forbidden_outputs = [
                notes / "stage4_prime_revision_round3.tex",
                notes / "stage4_prime_revision_round3.pdf",
                notes / "stage4_prime_revision_round3.tex.apply-report.json",
                notes / "stage4_prime_revision_round3_build_receipt.json",
                notes / "stage4_prime_revision_evidence_bundle_round3.json",
                notes / "stage4_prime_response_to_reviewers_round3.json",
            ]
            check("W035", all(not path.exists() for path in forbidden_outputs), "no apply/build/final response artifact created")
            check(
                "W036",
                exact_source_ids == expected_scope_ids
                and all(
                    (P29_EXACT_EXCERPT_SCOPE if paper_id == "P29" else P32_EXACT_EXCERPT_SCOPE)[
                        row["source_id"]
                    ]
                    in texts[row["block_id"]]
                    for row in source["rows"]
                    if row["finalization_status"] == "EXACT_LOCATOR_FINALIZED"
                ),
                "every located row is projected through an excerpt-bounded source-specific statement",
            )
            check(
                "W037",
                all(
                    "no substantive proposition" in texts[row["block_id"]]
                    for row in source["rows"]
                    if row["finalization_status"]
                    == "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY"
                ),
                "every unavailable row is explicitly metadata-only with no substantive attribution",
            )
            check(
                "W038",
                all(
                    phrase not in op["new_text"]
                    for op in ops
                    for phrase in (
                        "supports only the preceding contextual statement",
                        "support only the preceding contextual use",
                    )
                ),
                "no aggregate preceding-context support projection remains",
            )
            check(
                "W039",
                paper_id != "P32"
                or (
                    "Every row retains its hypotheses" not in texts["B0047"]
                    and "they are not represented as fields" in texts["B0047"]
                ),
                "Round-3 matrix description matches its actual field set",
            )
            if any(row["status"] != "PASS" for row in checks):
                raise RuntimeError(f"{paper_id}: writer-only validation failed")

            receipt = {
                "schema_version": "round10-stage4-prime-correction-round3-writer-validation-receipt/1.0",
                "paper_id": paper_id,
                "generated_at_utc": STAMP,
                "validation_scope": "WRITER_EMISSION_ONLY_NO_APPLY",
                "authority": {
                    "execution_receipt": binding(AUTH_RECEIPT),
                    "execution_freeze": binding(INPUT_FREEZE),
                    "expanded_request": binding(REQUEST),
                    "author_event": binding(AUTHOR_EVENT),
                },
                "emitted_artifacts": {
                    "roadmap": binding_for(roadmap_path, roadmap_raw),
                    "claim_surface_manifest": binding_for(claim_path, claim_raw),
                    "author_choices": binding_for(choices_path, choices_raw),
                    "author_adjudication": binding_for(adjudication_path, adjudication_raw),
                    "patch": binding_for(patch_path, patch_raw),
                    "semantic_preflight_incident": binding_for(incident_path, incident_raw),
                    "provisional_response_json": binding_for(response_path, response_raw),
                    "provisional_response_md": binding_for(response_md_path, response_md_raw),
                    "revision_log": binding_for(log_path, log_raw),
                },
                "source_issue_to_roadmap_item": [
                    {"source_issue_id": source_id, "roadmap_item_id": issue_map[source_id]}
                    for source_id in issue_map
                ],
                "counts": {
                    "source_issues": len(paper["issues"]),
                    "replace_block_ops": len(ops),
                    "unique_target_blocks": len({op["block_id"] for op in ops}),
                    "claim_strength_changes": 0,
                    "collateral_authorizations": 0,
                    "source_rows_semantically_rechecked": len(source["rows"]),
                    "exact_locator_rows_semantically_rechecked": len(exact_source_ids),
                    "checks_passed": len(checks),
                    "checks_failed": 0,
                },
                "checks": checks,
                "boundaries": {
                    "patch_applied": False,
                    "successor_tex_or_pdf_created": False,
                    "latex_build_run": False,
                    "bibliography_mutated": False,
                    "canonical_or_scientific_artifact_mutated": False,
                    "route_or_initial_system_mutated": False,
                    "fresh_stage4_5_run": False,
                },
                "next_required_actor": "independent deterministic patch applier",
                "supersedes_patch_sha256": SUPERSEDED_PATCH_SHA256[paper_id],
                "verdict": "PASS",
            }
            receipt_raw = json_bytes(receipt)

            handoff = {
                "schema_version": "round10-stage4-prime-correction-round3-writer-handoff/1.0",
                "paper_id": paper_id,
                "revision_round": 3,
                "generated_at_utc": STAMP,
                "handoff_status": "WRITER_PATCH_EMITTED_AWAITING_INDEPENDENT_APPLY",
                "authority": {
                    "execution_receipt": binding(AUTH_RECEIPT),
                    "execution_freeze": binding(INPUT_FREEZE),
                    "expanded_request": binding(REQUEST),
                    "author_event": binding(AUTHOR_EVENT),
                },
                "base_draft": binding(base_path),
                "block_manifest": binding(manifest_path),
                "bibliography_read_only": binding(bib_path),
                "source_finalization_read_only": binding(source_path),
                "claim_passage_matrix_read_only": binding(matrix_path),
                "source_validation_read_only": binding(source_validation_path),
                "roadmap": binding_for(roadmap_path, roadmap_raw),
                "claim_surface_manifest": binding_for(claim_path, claim_raw),
                "author_choices": binding_for(choices_path, choices_raw),
                "author_adjudication": binding_for(adjudication_path, adjudication_raw),
                "author_decision_digest": writer_authority["author_decision_digest"],
                "patch": binding_for(patch_path, patch_raw),
                "semantic_preflight_lineage": {
                    "incident": binding_for(incident_path, incident_raw),
                    "superseded_patch_sha256": SUPERSEDED_PATCH_SHA256[paper_id],
                    "controlling_patch_sha256": sha_bytes(patch_raw),
                    "full_source_rows_rechecked": len(source["rows"]),
                    "status": "SUPERSEDED_BEFORE_APPLY",
                },
                "provisional_response_json": binding_for(response_path, response_raw),
                "provisional_response_md": binding_for(response_md_path, response_md_raw),
                "revision_log": binding_for(log_path, log_raw),
                "writer_validation_receipt": binding_for(receipt_path, receipt_raw),
                "source_issue_to_roadmap_item": [
                    {
                        "source_issue_id": source_id,
                        "roadmap_item_id": issue_map[source_id],
                        "source_traceability_ordinal": ordinal,
                    }
                    for ordinal, source_id in enumerate(issue_map, start=1)
                ],
                "counts": {
                    "source_issues": len(paper["issues"]),
                    "replace_block_ops": len(ops),
                    "unique_target_blocks": len({op["block_id"] for op in ops}),
                    "claim_strength_changes": 0,
                    "collateral_authorizations": 0,
                    "source_rows_semantically_rechecked": len(source["rows"]),
                },
                "role_separation": {
                    "writer_emitted_patch": True,
                    "writer_applied_patch": False,
                    "writer_created_successor_draft": False,
                    "writer_built_latex": False,
                    "writer_modified_bibliography": False,
                },
                "next_step": {
                    "actor": "independent deterministic patch applier",
                    "operation": "Run ars_apply_revision_patch.py against the exact base, manifest, roadmap, author adjudication, claim-surface manifest, and patch bindings above.",
                    "stop_after": "isolated post-apply validation/build; fresh Stage 4.5 remains separately gated",
                },
                "boundaries": {
                    "registered_claim_strength_change_authorized": False,
                    "collateral_edit_authorized": False,
                    "bibliography_mutation_authorized": False,
                    "structural_edit_authorized": False,
                    "scientific_execution_or_result_refresh_authorized": False,
                    "canonical_promotion_authorized": False,
                    "route_or_initial_system_mutation_authorized": False,
                    "fresh_stage4_5_authorized": False,
                    "stage5_or_stage6_authorized": False,
                },
            }
            handoff_raw = json_bytes(handoff)

            final_artifacts.update(
                {
                    roadmap_path: roadmap_raw,
                    claim_path: claim_raw,
                    choices_path: choices_raw,
                    adjudication_path: adjudication_raw,
                    patch_path: patch_raw,
                    incident_path: incident_raw,
                    response_path: response_raw,
                    response_md_path: response_md_raw,
                    log_path: log_raw,
                    receipt_path: receipt_raw,
                    handoff_path: handoff_raw,
                }
            )
            immutable_artifacts.update(
                {roadmap_path, claim_path, choices_path, adjudication_path}
            )
            new_incident_paths.add(incident_path)
            summaries[paper_id] = {
                "roadmap": binding_for(roadmap_path, roadmap_raw),
                "claim_surface_manifest": binding_for(claim_path, claim_raw),
                "author_choices": binding_for(choices_path, choices_raw),
                "author_adjudication": binding_for(adjudication_path, adjudication_raw),
                "author_decision_digest": writer_authority["author_decision_digest"],
                "patch": binding_for(patch_path, patch_raw),
                "semantic_preflight_incident": binding_for(incident_path, incident_raw),
                "superseded_patch_sha256": SUPERSEDED_PATCH_SHA256[paper_id],
                "writer_validation_receipt": binding_for(receipt_path, receipt_raw),
                "writer_handoff": binding_for(handoff_path, handoff_raw),
                "ops": len(ops),
                "checks": f"{len(checks)}/{len(checks)} PASS",
            }

    # All papers validate before the first final write.  Fresh authority is immutable
    # and must remain byte-identical.  Only the prior writer-dependent chain may be
    # replaced, and only while its bytes still match the versions captured above.
    for path in immutable_artifacts:
        if not path.exists() or path.read_bytes() != final_artifacts[path]:
            raise RuntimeError(f"immutable fresh authority drift: {path}")
    for path in new_incident_paths:
        if path.exists():
            raise RuntimeError(f"refusing to overwrite semantic-preflight incident: {path}")
    for path, old_raw in captured_existing.items():
        if not path.exists() or path.read_bytes() != old_raw:
            raise RuntimeError(f"prior writer chain changed during semantic preflight: {path}")

    writable_artifacts = {
        path: raw for path, raw in final_artifacts.items() if path not in immutable_artifacts
    }
    for path, raw in writable_artifacts.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, temp_path = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(raw)
            os.replace(temp_path, path)
        except BaseException:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
            raise

    print(json.dumps({"status": "PASS_WRITER_EMISSION_ONLY", "papers": summaries}, ensure_ascii=False, indent=2))
    return 0


EXACT_CONFIRMATION_PREFIX = (
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
)
EXACT_CONFIRMATION_AUTHORITY = {
    "author_event": (
        f"{EXACT_CONFIRMATION_PREFIX}_AUTHOR_EVENT_20260904.txt",
        "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe",
    ),
    "authorization_record": (
        f"{EXACT_CONFIRMATION_PREFIX}_AUTHORIZATION_RECORD.md",
        "98755a5998aeee16034db32c89d997b3349a1b77b0c41a93ab32ac994a8d8f79",
    ),
    "input_freeze": (
        f"{EXACT_CONFIRMATION_PREFIX}_INPUT_FREEZE.json",
        "7a140287ce95ad6304cc52e7568d66780d77f54d7aaba461515cb087886075e1",
    ),
    "authorization_receipt": (
        f"{EXACT_CONFIRMATION_PREFIX}_AUTHORIZATION_RECEIPT.json",
        "a21655745ea33c565626c5cc980b8f91a82f4b87ce2d74cfcb012f0c5d7bae21",
    ),
    "authority_audit": (
        f"{EXACT_CONFIRMATION_PREFIX}_AUTHORITY_AUDIT.json",
        "813a600253cdeac98003a69beb7f28dbf35080cfdfe7bb974d1d8c9a323857b2",
    ),
}
EXACT_CONFIRMATION_EVENT_BYTES = "确认\n".encode("utf-8")
EXACT_CONFIRMATION_PREPARATION_ROLE = (
    "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY"
)
EXACT_CONFIRMATION_EVENT_ID = (
    "AUTHOR-EVENT-20260904-ROUND10-STAGE4-PRIME-SCOPE-REISSUE-"
    "EXACT-CONFIRMATION-{paper_id}"
)
EXACT_CONFIRMATION_CONFIG = {
    "P29": {
        "slug": "29-bianchi-ideal-owner-refinement",
        "expected_ops": 31,
        "source_rows": 22,
        "exact_locator_rows": 13,
        "prepared_patch_sha256": (
            "2e2db6ad458c5acb0ed96481a0c01f83af2f5c6f18009b9e0e77ac4fcf455309"
        ),
    },
    "P32": {
        "slug": "32-homology-cover-renormalization-uniformity",
        "expected_ops": 15,
        "source_rows": 30,
        "exact_locator_rows": 18,
        "prepared_patch_sha256": (
            "c19b10178928a7873a612d48b7e330c3bc513bdbe18f7cd55720da5990784ae6"
        ),
    },
}


def _exact_diff_paths(left: Any, right: Any, prefix: tuple[Any, ...] = ()) -> set[tuple[Any, ...]]:
    """Return the precise leaf paths that differ between two JSON values."""
    if type(left) is not type(right):
        return {prefix}
    if isinstance(left, dict):
        paths: set[tuple[Any, ...]] = set()
        for key in set(left) | set(right):
            if key not in left or key not in right:
                paths.add(prefix + (key,))
            else:
                paths.update(_exact_diff_paths(left[key], right[key], prefix + (key,)))
        return paths
    if isinstance(left, list):
        if len(left) != len(right):
            return {prefix + ("length",)}
        paths: set[tuple[Any, ...]] = set()
        for index, (old, new) in enumerate(zip(left, right)):
            paths.update(_exact_diff_paths(old, new, prefix + (index,)))
        return paths
    return set() if left == right else {prefix}


def _exact_publish_new(artifacts: dict[Path, bytes]) -> None:
    """Publish an all-new artifact set with collision checks and rollback."""
    for target in artifacts:
        if target.exists() or target.is_symlink():
            raise RuntimeError(f"refusing to overwrite exact-confirmation artifact: {target}")

    staged: list[tuple[Path, Path]] = []
    created: list[Path] = []
    try:
        for target, raw in artifacts.items():
            target.parent.mkdir(parents=True, exist_ok=True)
            fd, temporary_name = tempfile.mkstemp(
                prefix=f".{target.name}.exact-confirmation.", dir=target.parent
            )
            temporary = Path(temporary_name)
            with os.fdopen(fd, "wb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            staged.append((temporary, target))
        for temporary, target in staged:
            os.link(temporary, target)
            created.append(target)
    except BaseException:
        for target in reversed(created):
            try:
                target.unlink()
            except FileNotFoundError:
                pass
        raise
    finally:
        for temporary, _target in staged:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def exact_confirmation_reemit() -> int:
    """Re-sign P29/P32 prepared writer emissions under the exact `确认\n` event.

    This mode is intentionally non-generative: author decisions and every patch op,
    including every ``new_text`` string, come byte-for-byte at the JSON-value level
    from the frozen preparation evidence.  Only event/authority bindings and the
    resulting adjudication-dependent patch header are refreshed.
    """

    authority_paths: dict[str, Path] = {}
    authority_rows: dict[str, dict[str, Any]] = {}
    for role, (relative, expected_sha) in EXACT_CONFIRMATION_AUTHORITY.items():
        path = ROOT / relative
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"missing regular exact-confirmation authority: {relative}")
        raw = path.read_bytes()
        actual_sha = sha_bytes(raw)
        if actual_sha != expected_sha:
            raise RuntimeError(
                f"exact-confirmation authority hash drift for {relative}: "
                f"{actual_sha} != {expected_sha}"
            )
        authority_paths[role] = path
        authority_rows[role] = {
            "path": relative,
            "sha256": actual_sha,
            "bytes": len(raw),
        }
    if authority_paths["author_event"].read_bytes() != EXACT_CONFIRMATION_EVENT_BYTES:
        raise RuntimeError("exact-confirmation author event is not exact UTF-8 `确认\\n`")
    authority_rows["author_event"]["exact_text"] = "确认\n"

    freeze = json.loads(authority_paths["input_freeze"].read_text(encoding="utf-8"))
    receipt = json.loads(
        authority_paths["authorization_receipt"].read_text(encoding="utf-8")
    )
    audit = json.loads(authority_paths["authority_audit"].read_text(encoding="utf-8"))
    if (
        freeze.get("schema_version")
        != "round10-stage4-prime-correction-scope-reissue-exact-confirmation-input-freeze/1.0"
        or freeze.get("status") != "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION"
    ):
        raise RuntimeError("exact-confirmation input freeze schema/status mismatch")
    if (
        receipt.get("schema_version")
        != "round10-stage4-prime-correction-scope-reissue-exact-confirmation-authorization-receipt/1.0"
        or receipt.get("status")
        != "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION"
    ):
        raise RuntimeError("exact-confirmation authorization receipt schema/status mismatch")
    if (
        audit.get("schema_version")
        != "round10-stage4-prime-correction-scope-reissue-exact-confirmation-authority-audit/1.0"
        or audit.get("status")
        != "PASS_EXACT_CONFIRMATION_AUTHORITY_FROZEN_READY_FOR_DETERMINISTIC_APPLY"
        or audit.get("checks_run") != 81
        or audit.get("checks_passed") != 81
        or audit.get("checks_failed") != 0
        or len(audit.get("checks", [])) != 81
        or any(row.get("status") != "PASS" for row in audit.get("checks", []))
    ):
        raise RuntimeError("exact-confirmation authority audit is not 81/81 PASS")
    if (
        freeze.get("prepared_evidence_authority_role")
        != EXACT_CONFIRMATION_PREPARATION_ROLE
        or receipt.get("prepared_evidence_authority_role")
        != EXACT_CONFIRMATION_PREPARATION_ROLE
    ):
        raise RuntimeError("prepared evidence was not demoted to re-emission-only provenance")
    if freeze.get("author_event") != authority_rows["author_event"]:
        raise RuntimeError("input freeze does not bind the exact author event")
    if receipt.get("author_event") != authority_rows["author_event"]:
        raise RuntimeError("authorization receipt does not bind the exact author event")
    for role in ("authorization_record", "input_freeze"):
        if receipt.get(role) != authority_rows[role]:
            raise RuntimeError(f"authorization receipt {role} binding drift")
    if receipt.get("aggregate", {}).get("unique_replace_block_pairs") != 130:
        raise RuntimeError("authorization receipt aggregate operation count drift")

    request_path = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json"
    request_raw = request_path.read_bytes()
    request_sha = sha_bytes(request_raw)
    if request_sha != REQUEST_SHA256:
        raise RuntimeError("P29/P32 expanded request hash drift")
    request_row = receipt.get("tracks", {}).get("P29_P32")
    request_binding = binding(request_path)
    if request_row is None or any(
        request_row.get(key) != request_binding[key] for key in ("path", "sha256", "bytes")
    ):
        raise RuntimeError("authorization receipt P29/P32 track binding drift")
    if request_row.get("replace_block_pairs") != 46:
        raise RuntimeError("authorization receipt P29/P32 operation count drift")
    request = json.loads(request_raw)
    if (
        request.get("proposed_display_order") != "source_traceability"
        or request.get("proposed_author_triage") != "will_address"
        or request.get("proposed_revision_round") != 3
        or request.get("totals", {}).get("block_operation_pairs") != 46
    ):
        raise RuntimeError("expanded request execution contract drift")
    request_by_id = {paper["paper_id"]: paper for paper in request["papers"]}
    frozen_by_id = {paper["paper_id"]: paper for paper in freeze["papers"]}

    timestamp = (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    all_outputs: dict[Path, bytes] = {}
    summaries: dict[str, Any] = {}

    with tempfile.TemporaryDirectory(
        prefix=".round10-p2932-exact-confirmation.", dir=ROOT
    ) as temporary_root_name:
        temporary_root = Path(temporary_root_name)
        for paper_id in ("P29", "P32"):
            config = EXACT_CONFIRMATION_CONFIG[paper_id]
            notes = ROOT / "papers" / config["slug"] / "notes"
            paper_request = request_by_id[paper_id]
            frozen_paper = frozen_by_id[paper_id]
            if frozen_paper.get("authorized_unique_replace_block_pairs") != config["expected_ops"]:
                raise RuntimeError(f"{paper_id}: frozen operation count drift")

            # Replay every frozen no-touch boundary before constructing sidecars.
            frozen_rows = [
                frozen_paper["current_working_draft"],
                frozen_paper["current_working_bibliography"],
                frozen_paper["block_manifest"],
                *frozen_paper["canonical_files"],
                *frozen_paper["science_files"],
                frozen_paper["initial_system_source"],
                frozen_paper["route_crosswalk"],
            ]
            for row in frozen_rows:
                path = ROOT / row["path"]
                if (
                    not path.is_file()
                    or path.is_symlink()
                    or sha(path) != row["sha256"]
                    or path.stat().st_size != row["bytes"]
                ):
                    raise RuntimeError(f"{paper_id}: frozen boundary drift at {row['path']}")

            preparation = freeze["prepared_execution_evidence"][paper_id]
            prepared_names = {
                "author_choices": "stage4_prime_correction_round3_author_choices.json",
                "author_adjudication": "stage4_prime_correction_round3_author_adjudication.json",
                "patch": "stage4_prime_revision_patch_round3.json",
                "writer_handoff": "stage4_prime_correction_round3_writer_handoff.json",
                "writer_validation": "stage4_prime_writer_validation_receipt_round3.json",
            }
            prepared_rows: dict[str, dict[str, Any]] = {}
            prepared_objects: dict[str, dict[str, Any]] = {}
            for role, filename in prepared_names.items():
                row = preparation[role]
                path = notes / filename
                if row.get("path") != path.relative_to(ROOT).as_posix():
                    raise RuntimeError(f"{paper_id}: prepared {role} path drift")
                if (
                    not path.is_file()
                    or path.is_symlink()
                    or sha(path) != row.get("sha256")
                    or path.stat().st_size != row.get("bytes")
                ):
                    raise RuntimeError(f"{paper_id}: prepared {role} binding drift")
                prepared_rows[role] = copy.deepcopy(row)
                prepared_objects[role] = json.loads(path.read_text(encoding="utf-8"))
            if prepared_rows["patch"]["sha256"] != config["prepared_patch_sha256"]:
                raise RuntimeError(f"{paper_id}: controlling prepared patch hash drift")

            base_path = ROOT / frozen_paper["current_working_draft"]["path"]
            bibliography_path = ROOT / frozen_paper["current_working_bibliography"]["path"]
            manifest_path = ROOT / frozen_paper["block_manifest"]["path"]
            roadmap_path = notes / "stage4_prime_correction_round3_revision_roadmap.json"
            claims_path = notes / "stage4_prime_correction_round3_claim_surface_manifest.json"
            source_path = notes / "stage4_prime_source_finalization_round3.json"
            matrix_path = notes / "stage4_prime_claim_passage_matrix_round3.json"
            source_validation_path = notes / "stage4_prime_source_finalization_round3_validation.json"
            incident_path = notes / "stage4_prime_correction_round3_semantic_preflight_incident.json"

            choices_path = notes / "stage4_prime_correction_round3_exact_confirmation_author_choices.json"
            adjudication_path = notes / "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json"
            patch_path = notes / "stage4_prime_revision_patch_round3_exact_confirmation.json"
            validation_path = notes / "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json"
            handoff_path = notes / "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json"
            for path in (choices_path, adjudication_path, patch_path, validation_path, handoff_path):
                if path.exists() or path.is_symlink():
                    raise RuntimeError(f"{paper_id}: exact-confirmation output collision at {path}")

            base_raw = base_path.read_bytes()
            roadmap_raw = roadmap_path.read_bytes()
            claims_raw = claims_path.read_bytes()
            roadmap = json.loads(roadmap_raw)
            claims = json.loads(claims_raw)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if sha(roadmap_path) != preparation["revision_roadmap"]["sha256"]:
                raise RuntimeError(f"{paper_id}: prepared roadmap hash drift")
            if sha(claims_path) != preparation["claim_surface_manifest"]["sha256"]:
                raise RuntimeError(f"{paper_id}: prepared claim-surface hash drift")

            item_order: list[str] = []
            target_by_item: dict[str, list[dict[str, Any]]] = {}
            block_order: list[str] = []
            request_full_hash: dict[str, str] = {}
            for issue in paper_request["issues"]:
                item_id = (
                    issue["issue_id"]
                    if issue["issue_id"].startswith("REV-")
                    else f"REV-{issue['issue_id']}"
                )
                item_order.append(item_id)
                targets: list[dict[str, Any]] = []
                for target in issue["proposed_targets"]:
                    if target["allowed_operations"] != ["replace_block"]:
                        raise RuntimeError(f"{paper_id}/{item_id}: non-replace request")
                    block_id = target["block_id"]
                    if block_id in request_full_hash:
                        raise RuntimeError(f"{paper_id}: duplicate requested block {block_id}")
                    block_order.append(block_id)
                    request_full_hash[block_id] = target["expected_old_hash"]
                    targets.append(
                        {
                            "block_id": block_id,
                            "allowed_operations": ["replace_block"],
                        }
                    )
                target_by_item[item_id] = targets
            if item_order != [item["id"] for item in roadmap["items"]]:
                raise RuntimeError(f"{paper_id}: roadmap/source-traceability order drift")
            if len(block_order) != config["expected_ops"]:
                raise RuntimeError(f"{paper_id}: requested operation count drift")

            old_choices = prepared_objects["author_choices"]
            old_event_id = old_choices["author_events"][0]["event_id"]
            new_event_id = EXACT_CONFIRMATION_EVENT_ID.format(paper_id=paper_id)
            fresh_choices = copy.deepcopy(old_choices)
            fresh_choices["author_events"] = [
                {
                    "actor_role": "author",
                    "event_id": new_event_id,
                    "input_sha256": EXACT_CONFIRMATION_AUTHORITY["author_event"][1],
                    "source": "explicit_session_user_message",
                }
            ]
            fresh_choices["display_order"]["author_event_id"] = new_event_id
            for decision in fresh_choices["author_adjudications"]:
                decision["author_event_id"] = new_event_id
            allowed_choice_diffs = {
                ("author_events", 0, "event_id"),
                ("author_events", 0, "input_sha256"),
                ("display_order", "author_event_id"),
                *{
                    ("author_adjudications", index, "author_event_id")
                    for index in range(len(old_choices["author_adjudications"]))
                },
            }
            if _exact_diff_paths(old_choices, fresh_choices) != allowed_choice_diffs:
                raise RuntimeError(f"{paper_id}: fresh choices changed substantive decisions")
            if (
                fresh_choices["display_order"]
                != {
                    "mode": "source_traceability",
                    "item_ids": item_order,
                    "author_event_id": new_event_id,
                }
                or [row["item_id"] for row in fresh_choices["author_adjudications"]]
                != item_order
                or fresh_choices["collateral_authorizations"] != []
            ):
                raise RuntimeError(f"{paper_id}: fresh choices order/collateral drift")
            for decision in fresh_choices["author_adjudications"]:
                if (
                    decision["author_triage"] != "will_address"
                    or decision["authorized_targets"] != target_by_item[decision["item_id"]]
                    or decision["claim_strength_authorizations"] != []
                ):
                    raise RuntimeError(
                        f"{paper_id}/{decision['item_id']}: fresh decision scope drift"
                    )
            choices_raw = json_bytes(fresh_choices)

            # The official ARS authority builder, not this writer, constructs the
            # fresh author-adjudication/1.0 artifact.
            paper_temp = temporary_root / paper_id
            paper_temp.mkdir()
            temporary_choices = paper_temp / choices_path.name
            temporary_adjudication = paper_temp / adjudication_path.name
            temporary_choices.write_bytes(choices_raw)
            build_command = [
                sys.executable,
                str(REVISION_ROADMAP_CLI),
                "build-adjudication",
                str(roadmap_path),
                "--base",
                str(base_path),
                "--block-manifest",
                str(manifest_path),
                "--claim-surface",
                str(claims_path),
                "--author-choices",
                str(temporary_choices),
                "--artifact-root",
                str(ROOT),
                "--output",
                str(temporary_adjudication),
            ]
            built = subprocess.run(
                build_command,
                cwd=ROOT,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if built.returncode != 0:
                raise RuntimeError(
                    f"{paper_id}: official build-adjudication failed:\n"
                    f"{built.stdout}{built.stderr}"
                )
            adjudication_raw = temporary_adjudication.read_bytes()
            fresh_adjudication = json.loads(adjudication_raw)
            old_adjudication = prepared_objects["author_adjudication"]
            allowed_adjudication_diffs = {
                ("author_events", 0, "event_id"),
                ("author_events", 0, "input_sha256"),
                ("display_order", "author_event_id"),
                *{
                    ("author_adjudications", index, "author_event_id")
                    for index in range(len(old_adjudication["author_adjudications"]))
                },
            }
            if _exact_diff_paths(old_adjudication, fresh_adjudication) != allowed_adjudication_diffs:
                raise RuntimeError(f"{paper_id}: official adjudication changed substantive decisions")

            validate_command = [
                sys.executable,
                str(REVISION_ROADMAP_CLI),
                "validate-adjudication",
                str(roadmap_path),
                str(temporary_adjudication),
                "--base",
                str(base_path),
                "--block-manifest",
                str(manifest_path),
                "--claim-surface",
                str(claims_path),
                "--artifact-root",
                str(ROOT),
            ]
            validated = subprocess.run(
                validate_command,
                cwd=ROOT,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if validated.returncode != 0:
                raise RuntimeError(
                    f"{paper_id}: official validate-adjudication failed:\n"
                    f"{validated.stdout}{validated.stderr}"
                )

            old_patch = prepared_objects["patch"]
            fresh_patch = copy.deepcopy(old_patch)
            fresh_patch["author_adjudication_sha256"] = sha_bytes(adjudication_raw)
            fresh_patch["author_decision_digest"] = rr.author_decision_digest(
                fresh_adjudication
            )
            if set(_exact_diff_paths(old_patch, fresh_patch)) != {
                ("author_adjudication_sha256",),
                ("author_decision_digest",),
            }:
                raise RuntimeError(f"{paper_id}: exact re-sign changed patch outside authority header")
            if fresh_patch["ops"] != old_patch["ops"]:
                raise RuntimeError(f"{paper_id}: exact re-sign changed prepared patch ops")
            if [op["block_id"] for op in fresh_patch["ops"]] != block_order:
                raise RuntimeError(f"{paper_id}: patch op order differs from source traceability")
            if (
                len(fresh_patch["ops"]) != config["expected_ops"]
                or len({op["block_id"] for op in fresh_patch["ops"]})
                != config["expected_ops"]
                or any(
                    op["op"] != "replace_block"
                    or op["claim_strength_changes"] != []
                    or op["collateral_authorization_ids"] != []
                    for op in fresh_patch["ops"]
                )
            ):
                raise RuntimeError(f"{paper_id}: patch operation scope/count drift")

            parsed = parse_document(base_raw.decode("utf-8"))
            blocks = parsed.block_by_id()
            manifest_hashes = {
                row["block_id"]: row["old_hash"] for row in manifest["blocks"]
            }
            for op in fresh_patch["ops"]:
                block_id = op["block_id"]
                full_hash = sha_bytes(blocks[block_id].normalized_text.encode("utf-8"))
                if (
                    full_hash != request_full_hash[block_id]
                    or manifest_hashes.get(block_id) != full_hash[:12]
                    or op["old_hash"] != full_hash[:12]
                ):
                    raise RuntimeError(f"{paper_id}/{block_id}: base/request/manifest hash drift")

            patch_schema_failures = rr._schema_failures(  # type: ignore[attr-defined]
                fresh_patch, rr.PATCH_SCHEMA_PATH, "exact-confirmation review patch"
            )
            if patch_schema_failures:
                raise RuntimeError(
                    f"{paper_id}: patch schema failure: {'; '.join(patch_schema_failures)}"
                )
            surfaces_by_id = rr.validate_claim_surface_manifest(
                claims,
                claim_surface_raw=claims_raw,
                roadmap=roadmap,
                roadmap_raw=roadmap_raw,
                base_raw=base_raw,
                artifact_store=rr._standalone_store(ROOT),  # type: ignore[attr-defined]
            )
            patch_witness = rr.validate_review_patch_authorization(
                fresh_patch,
                base_raw=base_raw,
                roadmap=roadmap,
                roadmap_raw=roadmap_raw,
                adjudication=fresh_adjudication,
                adjudication_raw=adjudication_raw,
                claim_surface=claims,
                claim_surface_raw=claims_raw,
                surfaces_by_id=surfaces_by_id,
            )
            patch_raw = json_bytes(fresh_patch)
            ops_canonical = rr.canonical_bytes(fresh_patch["ops"])
            trace_canonical = json.dumps(
                item_order, ensure_ascii=False, separators=(",", ":")
            ).encode("utf-8")

            fresh_bindings = {
                "revision_roadmap": binding(roadmap_path),
                "claim_surface_manifest": binding(claims_path),
                "author_choices": binding_for(choices_path, choices_raw),
                "author_adjudication": binding_for(adjudication_path, adjudication_raw),
                "patch": binding_for(patch_path, patch_raw),
            }
            source_traceability = {
                "mode": "source_traceability",
                "item_ids": item_order,
                "count": len(item_order),
                "canonicalization": "JSON.generate(item_ids) UTF-8",
                "sha256": sha_bytes(trace_canonical),
            }
            preparation_evidence = {
                "authority_role": EXACT_CONFIRMATION_PREPARATION_ROLE,
                "author_event_sha256": AUTHOR_EVENT_SHA256,
                "artifacts": prepared_rows,
                "ops_canonical_sha256": sha_bytes(
                    rr.canonical_bytes(old_patch["ops"])
                ),
            }

            validation = {
                "schema_version": (
                    "round10-stage4-prime-correction-round3-exact-confirmation-"
                    "writer-validation-receipt/1.0"
                ),
                "generated_at_utc": timestamp,
                "status": "PASS_EXACT_CONFIRMATION_WRITER_EMITTED_NOT_APPLIED",
                "paper_id": paper_id,
                "paper_number": int(paper_id[1:]),
                "lineage_label": "round3_exact_confirmation",
                "revision_round": 3,
                "authority": authority_rows,
                "request": request_binding,
                "artifacts": {
                    "base_draft": binding(base_path),
                    "bibliography_read_only": binding(bibliography_path),
                    "block_manifest": binding(manifest_path),
                    **fresh_bindings,
                    "source_finalization_read_only": binding(source_path),
                    "claim_passage_matrix_read_only": binding(matrix_path),
                    "source_validation_read_only": binding(source_validation_path),
                    "semantic_preflight_incident": binding(incident_path),
                },
                "preparation_evidence": preparation_evidence,
                "author_decision_digest": fresh_patch["author_decision_digest"],
                "source_traceability": source_traceability,
                "checks": {
                    "exact_author_event_bytes": "PASS",
                    "exact_five_artifact_authority_chain": "PASS",
                    "authority_audit_81_of_81": "PASS",
                    "prepared_evidence_non_authorizing": "PASS",
                    "prepared_decisions_unchanged_except_event_binding": "PASS",
                    "official_build_adjudication": "PASS",
                    "official_validate_adjudication": "PASS",
                    "author_choice_schema_via_official_builder": "PASS",
                    "author_adjudication_schema_via_official_validator": "PASS",
                    "patch_schema_1_1": "PASS",
                    "official_review_patch_authorization": patch_witness["status"].upper(),
                    "patch_ops_json_value_preservation": "PASS",
                    "patch_ops_canonical_sha256": sha_bytes(ops_canonical),
                    "patch_ops_source_traceability_order": "PASS",
                    "base_request_manifest_old_hashes": "PASS",
                    "unique_replace_block_ops": len(fresh_patch["ops"]),
                    "claim_strength_changes": 0,
                    "collateral_authorizations": 0,
                    "all_required_checks_passed": True,
                },
                "counts": {
                    "roadmap_items": len(item_order),
                    "will_address_decisions": len(item_order),
                    "unique_replace_block_ops": len(fresh_patch["ops"]),
                    "source_rows_previously_semantically_rechecked": config["source_rows"],
                    "exact_locator_rows_previously_semantically_rechecked": config[
                        "exact_locator_rows"
                    ],
                    "claim_strength_changes": 0,
                    "collateral_authorizations": 0,
                },
                "boundaries": {
                    "prepared_artifacts_are_non_authorizing_provenance_only": True,
                    "patch_applied": False,
                    "successor_draft_or_apply_report_emitted": False,
                    "build_run": False,
                    "bibliography_changed": False,
                    "matrix_changed": False,
                    "readme_changed": False,
                    "git_changed": False,
                    "canonical_or_science_or_route_or_initial_system_changed": False,
                    "fresh_stage4_5_or_re_review_run": False,
                },
            }
            validation_raw = json_bytes(validation)
            validation_binding = binding_for(validation_path, validation_raw)

            handoff = {
                "schema_version": (
                    "round10-stage4-prime-correction-round3-exact-confirmation-"
                    "writer-handoff/1.0"
                ),
                "generated_at_utc": timestamp,
                "handoff_status": (
                    "EXACT_CONFIRMATION_WRITER_PATCH_EMITTED_AWAITING_INDEPENDENT_APPLY"
                ),
                "paper_id": paper_id,
                "paper_number": int(paper_id[1:]),
                "lineage_label": "round3_exact_confirmation",
                "revision_round": 3,
                "authority": authority_rows,
                "request": request_binding,
                "artifacts": {
                    "base_draft": binding(base_path),
                    "bibliography_read_only": binding(bibliography_path),
                    "block_manifest": binding(manifest_path),
                    **fresh_bindings,
                    "writer_validation": validation_binding,
                    "source_finalization_read_only": binding(source_path),
                    "claim_passage_matrix_read_only": binding(matrix_path),
                    "source_validation_read_only": binding(source_validation_path),
                    "semantic_preflight_incident": binding(incident_path),
                },
                "preparation_evidence": preparation_evidence,
                "author_decision_digest": fresh_patch["author_decision_digest"],
                "source_traceability": source_traceability,
                "semantic_payload_preservation": {
                    "prepared_patch_sha256": prepared_rows["patch"]["sha256"],
                    "prepared_ops_canonical_sha256": sha_bytes(
                        rr.canonical_bytes(old_patch["ops"])
                    ),
                    "fresh_ops_canonical_sha256": sha_bytes(ops_canonical),
                    "ops_json_value_equal": True,
                    "new_text_values_equal": True,
                },
                "counts": validation["counts"],
                "role_separation": {
                    "writer_emitted_patch": True,
                    "writer_applied_patch": False,
                    "writer_created_successor_draft": False,
                    "writer_built_latex": False,
                    "writer_modified_bibliography_or_matrix": False,
                },
                "boundaries": validation["boundaries"],
                "next_step": {
                    "actor": "independent deterministic patch applier",
                    "operation": (
                        "Apply only after the final exact-confirmation emission manifest "
                        "and independent exact-confirmation cross-audits bind this fresh chain."
                    ),
                    "stop_after": (
                        "isolated post-apply validation/build; fresh Stage 4.5 remains "
                        "separately gated"
                    ),
                },
            }
            handoff_raw = json_bytes(handoff)

            for document_name, document in (
                ("writer validation", validation),
                ("writer handoff", handoff),
            ):
                encoded = json.dumps(document, ensure_ascii=False, sort_keys=True)
                required_digests = [
                    *(value[1] for value in EXACT_CONFIRMATION_AUTHORITY.values()),
                    fresh_bindings["author_choices"]["sha256"],
                    fresh_bindings["author_adjudication"]["sha256"],
                    fresh_bindings["patch"]["sha256"],
                ]
                missing = [digest for digest in required_digests if digest not in encoded]
                if missing:
                    raise RuntimeError(
                        f"{paper_id}: {document_name} omits required exact bindings {missing}"
                    )

            paper_outputs = {
                choices_path: choices_raw,
                adjudication_path: adjudication_raw,
                patch_path: patch_raw,
                validation_path: validation_raw,
                handoff_path: handoff_raw,
            }
            all_outputs.update(paper_outputs)
            summaries[paper_id] = {
                "event_id": new_event_id,
                "author_decision_digest": fresh_patch["author_decision_digest"],
                "ops": len(fresh_patch["ops"]),
                "ops_canonical_sha256": sha_bytes(ops_canonical),
                "official_build_adjudication": built.stdout.strip(),
                "official_validate_adjudication": validated.stdout.strip(),
                "artifacts": {
                    path.name: binding_for(path, raw) for path, raw in paper_outputs.items()
                },
            }

    # Recheck protected inputs immediately before the only final write phase.
    for paper_id, config in EXACT_CONFIRMATION_CONFIG.items():
        frozen_paper = frozen_by_id[paper_id]
        for row in [
            frozen_paper["current_working_draft"],
            frozen_paper["current_working_bibliography"],
            frozen_paper["block_manifest"],
            *frozen_paper["canonical_files"],
            *frozen_paper["science_files"],
            frozen_paper["initial_system_source"],
            frozen_paper["route_crosswalk"],
        ]:
            path = ROOT / row["path"]
            if sha(path) != row["sha256"] or path.stat().st_size != row["bytes"]:
                raise RuntimeError(f"{paper_id}: protected input changed before publish")

    _exact_publish_new(all_outputs)
    for path, expected_raw in all_outputs.items():
        if path.read_bytes() != expected_raw:
            raise RuntimeError(f"post-publish exact artifact verification failed: {path}")

    print(
        json.dumps(
            {
                "status": "PASS_EXACT_CONFIRMATION_WRITER_REEMISSION_ONLY",
                "authority": authority_rows,
                "papers": summaries,
                "boundaries": {
                    "patch_applied": False,
                    "successor_created": False,
                    "latex_build_run": False,
                    "bibliography_or_matrix_changed": False,
                    "readme_or_git_changed": False,
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--exact-confirmation-reemit"]:
        raise SystemExit(exact_confirmation_reemit())
    if sys.argv[1:]:
        raise SystemExit(
            "usage: build_round10_scope_reissue_p29_p32_writer.py "
            "[--exact-confirmation-reemit]"
        )
    raise SystemExit(main())
