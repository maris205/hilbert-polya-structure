#!/usr/bin/env python3
"""Deterministic, read-only audit for Round-10 Stage-2 papers.

The three cumulative phases are:

``inputs``
    Verify the authorization, roadmap, Stage-1, science-tree, and frozen
    Stage-2 pre-prose inputs.
``draft``
    Add manuscript structure, bilingual abstracts, bibliography/citation
    closure, ARS marker, claim-boundary, science-firewall, and route-firewall
    checks.
``full``
    Add an isolated LuaLaTeX/BibTeX rebuild and checks of the published PDF,
    build/review receipts, README/state summaries, and batch output manifest.

The audit never modifies the repository.  Its output contains stable failure
codes and deterministic counts; timestamps and temporary paths are omitted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]

PAPERS: dict[str, dict[str, Any]] = {
    "P29": {
        "slug": "29-bianchi-ideal-owner-refinement",
        "sources": 22,
        "special": (
            "gate m",
            "gate q",
            "literal gaussian",
            "deliberately strict",
            "p29-s06",
            "p29-s07",
            "correction",
            "p29-s09",
            "preprint",
        ),
    },
    "P30": {
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "sources": 26,
        "special": (
            "d=6a",
            "six scientific gates remain open",
            "five-channel",
            "p30-s01",
            "p30-s02",
            "p30-s03",
            "p30-s17",
            "p30-s18",
            "a0_fail",
            "a2_not_eligible",
            "no_route_promotion",
        ),
    },
    "P31": {
        "slug": "31-level11-conjugacy-owner-ledger",
        "sources": 22,
        "special": (
            "138",
            "55",
            "9,453",
            "canonicalization",
            "biconditional",
            "287--305",
            "a1-only",
        ),
    },
    "P32": {
        "slug": "32-homology-cover-renormalization-uniformity",
        "sources": 26,
        "special": (
            "1/n",
            "1/n^3",
            "higher-content",
            "zero-content",
            "content one is contingent",
            "p32-s13",
            "plausible",
            "background-only",
            "p32-s06",
            "preprint",
            "p32-s17",
            "correction",
            "a0 is unavailable",
        ),
    },
    "P33": {
        "slug": "33-bolza-control-matched-census",
        "sources": 20,
        "special": (
            "b=1/2",
            "signed-field even subsequence",
            "lambda=21/10",
            "target-blind",
            "must not be retuned",
            "surface-specific",
            "common semantic",
            "independent validator",
            "p33-rc-1",
            "zero of seven",
            "plausible",
            "context-only",
            "page-unpinned",
            "a0_inconclusive_systole_confounded",
            "a0_control_panel_incomplete",
            "not_evaluable_conjugacy_method_unavailable",
        ),
    },
}

# These are the externally closed roots of the Stage-2 input chain.  The
# per-paper and Stage-1 hashes are then read from the hash-bound input freeze.
FIXED_HASHES = {
    "BATCH_ROUND10_STAGE2_AUTHORIZATION_20260902.txt":
        "dacd32a6408007a69732ff052120f02126233a079c3783d6676d490113266bd5",
    "BATCH_ROUND10_STAGE2_WRITING_CONTRACT.md":
        "cd79c1508ada0acc02fa0413592e9772b8edad04d84a859a5642f010bac8fd08",
    "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json":
        "923339d65d4fd073483d01d54cdf8eb4e1e0e540d944dae7aaf1198db9f2212c",
    "BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json":
        "8c5f320d65988f4d69d4a69604fda22df6defb8ffa74c387248c7865f1fd9bb6",
    "BATCH_ROUND10_STAGE1_HANDOFF_TO_STAGE2.md":
        "8a8bd4ea42fe67366d8d7849bd941170b4793320f9296c6c3b6f4b357ea98dfd",
    "skills/route-a-evaluator.md":
        "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
    "skills/route-b-evaluator.md":
        "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595",
}

STAGE1_BATCH_PATHS = {
    "checkpoint_sha256": "BATCH_ROUND10_STAGE1_PHASE6_CHECKPOINT.md",
    "audit_receipt_sha256": "BATCH_ROUND10_STAGE1_PHASE6_AUDIT_RECEIPT.json",
    "independent_audit_sha256": "BATCH_ROUND10_STAGE1_PHASE6_INDEPENDENT_AUDIT.md",
    "canonical_guard_sha256": "BATCH_ROUND10_STAGE1_PHASE6_CANONICAL_GUARD.json",
}

MAP_SCHEMA_KEYS = {
    "schema",
    "paper",
    "inventory_path",
    "inventory_sha256",
    "normalization_policy",
    "source_to_bibtex_key",
}

MARKER_RE = re.compile(
    r"^% ARS-CITE source_ids=([^\s]+) anchor=none "
    r"claim_to_passage=INCONCLUSIVE$"
)
CITE_RE = re.compile(
    r"\\cite[a-zA-Z]*\*?(\s*(?:\[[^\]]*\]\s*)*)\{([^{}]+)\}"
)
BIB_RE = re.compile(r"(?m)^@(?:article|book|inbook|incollection|inproceedings|misc|phdthesis|techreport)\s*\{\s*([^,\s]+)\s*,", re.I)
WORD_RE = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*")
HAN_RE = re.compile(r"[\u3400-\u9fff]")


@dataclass(order=True)
class Failure:
    code: str
    paper: str = "BATCH"
    path: str = ""
    detail: str = ""

    def as_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "paper": self.paper,
            "path": self.path,
            "detail": self.detail,
        }


@dataclass
class Audit:
    phase: str
    papers: list[str]
    failures: list[Failure] = field(default_factory=list)
    checks_run: int = 0
    metrics: dict[str, Any] = field(default_factory=dict)
    input_freeze: dict[str, Any] | None = None
    preprose_freeze: dict[str, Any] | None = None

    def require(
        self,
        condition: bool,
        code: str,
        detail: str,
        *,
        paper: str = "BATCH",
        path: str = "",
    ) -> bool:
        self.checks_run += 1
        if not condition:
            self.failures.append(Failure(code, paper, path, detail))
        return condition

    def fail(
        self,
        code: str,
        detail: str,
        *,
        paper: str = "BATCH",
        path: str = "",
    ) -> None:
        self.require(False, code, detail, paper=paper, path=path)


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return str(path)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(audit: Audit, path: Path, code: str, paper: str = "BATCH") -> dict[str, Any] | None:
    if not audit.require(path.is_file(), "I001_MISSING_FILE", "required JSON file is absent", paper=paper, path=rel(path)):
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        audit.fail(code, f"invalid JSON: {exc}", paper=paper, path=rel(path))
        return None
    if not audit.require(isinstance(value, dict), code, "top-level JSON value must be an object", paper=paper, path=rel(path)):
        return None
    return value


def check_hash(audit: Audit, path: Path, expected: str, paper: str = "BATCH") -> bool:
    if not audit.require(path.is_file(), "I001_MISSING_FILE", "hash-bound file is absent", paper=paper, path=rel(path)):
        return False
    actual = sha256(path)
    return audit.require(
        actual == expected,
        "I002_HASH_MISMATCH",
        f"expected {expected}; observed {actual}",
        paper=paper,
        path=rel(path),
    )


def tree_hash(paths: Iterable[Path]) -> str:
    rows: list[str] = []
    for path in sorted((item for item in paths if item.is_file()), key=lambda item: rel(item)):
        rows.append(f"{sha256(path)}  {rel(path)}\n")
    return hashlib.sha256("".join(rows).encode("utf-8")).hexdigest()


def paper_paths(code: str) -> tuple[Path, Path, Path]:
    base = ROOT / "papers" / PAPERS[code]["slug"]
    return base, base / "paper", base / "notes"


def input_row(audit: Audit, code: str) -> dict[str, Any] | None:
    if not audit.input_freeze:
        return None
    rows = [row for row in audit.input_freeze.get("papers", []) if row.get("paper") == code]
    if not audit.require(len(rows) == 1, "I003_FREEZE_SCHEMA", "paper must occur exactly once in input freeze", paper=code, path="BATCH_ROUND10_STAGE2_INPUT_FREEZE.json"):
        return None
    return rows[0]


def preprose_row(audit: Audit, code: str) -> dict[str, Any] | None:
    if not audit.preprose_freeze:
        return None
    rows = [row for row in audit.preprose_freeze.get("papers", []) if row.get("paper") == code]
    if not audit.require(len(rows) == 1, "I003_FREEZE_SCHEMA", "paper must occur exactly once in pre-prose freeze", paper=code, path="BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json"):
        return None
    return rows[0]


def inventory_ids(path: Path) -> list[str]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return [str(row.get("source_id", "")).strip() for row in reader]


def check_inputs(audit: Audit) -> None:
    audit.metrics["input_files_hashed"] = 0
    audit.metrics["preprose_artifacts_hashed"] = 0
    audit.metrics["claim_intents"] = 0
    audit.metrics["lineage_mappings"] = 0

    for name, expected in sorted(FIXED_HASHES.items()):
        if check_hash(audit, ROOT / name, expected):
            audit.metrics["input_files_hashed"] += 1

    audit.input_freeze = load_json(
        audit,
        ROOT / "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json",
        "I003_FREEZE_SCHEMA",
    )
    audit.preprose_freeze = load_json(
        audit,
        ROOT / "BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json",
        "I003_FREEZE_SCHEMA",
    )
    if not audit.input_freeze or not audit.preprose_freeze:
        return

    audit.require(
        audit.input_freeze.get("schema") == "round10-stage2-input-freeze/1.0",
        "I003_FREEZE_SCHEMA",
        "unexpected input-freeze schema",
        path="BATCH_ROUND10_STAGE2_INPUT_FREEZE.json",
    )
    audit.require(
        audit.preprose_freeze.get("schema") == "round10-stage2-preprose-freeze/1.0",
        "I003_FREEZE_SCHEMA",
        "unexpected pre-prose-freeze schema",
        path="BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json",
    )

    stage1 = audit.input_freeze.get("stage1_batch", {})
    for key, name in sorted(STAGE1_BATCH_PATHS.items()):
        expected = stage1.get(key)
        audit.require(isinstance(expected, str) and len(expected) == 64, "I003_FREEZE_SCHEMA", f"missing Stage-1 hash field {key}", path="BATCH_ROUND10_STAGE2_INPUT_FREEZE.json")
        if isinstance(expected, str) and len(expected) == 64 and check_hash(audit, ROOT / name, expected):
            audit.metrics["input_files_hashed"] += 1

    roadmaps = audit.input_freeze.get("roadmaps", {})
    for prefix in ("route_a", "route_b"):
        path_value = roadmaps.get(f"{prefix}_path")
        expected = roadmaps.get(f"{prefix}_sha256")
        if isinstance(path_value, str) and isinstance(expected, str):
            check_hash(audit, ROOT / path_value, expected)
        else:
            audit.fail("I009_ROUTE_DOC_DRIFT", f"missing {prefix} path/hash binding", path="BATCH_ROUND10_STAGE2_INPUT_FREEZE.json")

    for code in audit.papers:
        base, _, notes = paper_paths(code)
        row = input_row(audit, code)
        frozen = preprose_row(audit, code)
        if not row or not frozen:
            continue
        audit.require(row.get("slug") == PAPERS[code]["slug"], "I003_FREEZE_SCHEMA", "slug differs from paper registry", paper=code, path="BATCH_ROUND10_STAGE2_INPUT_FREEZE.json")

        phase_files = (
            (notes / "stage1_phase6_final_report.md", row.get("phase6_report_sha256")),
            (notes / "stage1_phase6_claim_intent_manifest.json", row.get("phase6_manifest_sha256")),
            (notes / "stage1_phase6_checkpoint.md", row.get("phase6_checkpoint_sha256")),
        )
        for path, expected in phase_files:
            if isinstance(expected, str) and check_hash(audit, path, expected, code):
                audit.metrics["input_files_hashed"] += 1
            elif not isinstance(expected, str):
                audit.fail("I003_FREEZE_SCHEMA", "missing per-paper Phase-6 hash", paper=code, path="BATCH_ROUND10_STAGE2_INPUT_FREEZE.json")

        stage1_actual = tree_hash(notes.glob("stage1_*"))
        audit.require(
            stage1_actual == row.get("stage1_notes_tree_sha256"),
            "I004_STAGE1_TREE_DRIFT",
            f"expected {row.get('stage1_notes_tree_sha256')}; observed {stage1_actual}",
            paper=code,
            path=rel(notes),
        )
        science_files: list[Path] = []
        for dirname in ("code", "experiments", "results"):
            science_files.extend((base / dirname).rglob("*"))
        science_actual = tree_hash(science_files)
        audit.require(
            science_actual == row.get("science_tree_sha256"),
            "I005_SCIENCE_TREE_DRIFT",
            f"expected {row.get('science_tree_sha256')}; observed {science_actual}",
            paper=code,
            path=rel(base),
        )

        artifacts = frozen.get("artifacts", [])
        audit.require(len(artifacts) == 7, "I003_FREEZE_SCHEMA", "expected seven frozen pre-prose artifacts", paper=code, path="BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json")
        for artifact in artifacts:
            path_value = artifact.get("path")
            expected = artifact.get("sha256")
            if not isinstance(path_value, str) or not isinstance(expected, str):
                audit.fail("I003_FREEZE_SCHEMA", "malformed pre-prose artifact row", paper=code, path="BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json")
                continue
            if check_hash(audit, ROOT / path_value, expected, code):
                audit.metrics["preprose_artifacts_hashed"] += 1

        manifest_path = notes / "stage2_claim_intent_manifest.json"
        lineage_path = notes / "stage2_claim_lineage.json"
        manifest = load_json(audit, manifest_path, "I007_CLAIM_MANIFEST", code)
        lineage = load_json(audit, lineage_path, "I008_CLAIM_LINEAGE", code)
        if not manifest or not lineage:
            continue
        claims = manifest.get("claims", [])
        claim_ids = [claim.get("claim_id") for claim in claims if isinstance(claim, dict)]
        audit.require(len(claims) == 8 and len(set(claim_ids)) == 8, "I007_CLAIM_MANIFEST", "expected eight unique Stage-2 ClaimIntents", paper=code, path=rel(manifest_path))
        audit.require(all(isinstance(claim.get("negative_constraints"), list) and claim["negative_constraints"] for claim in claims if isinstance(claim, dict)), "I007_CLAIM_MANIFEST", "every claim needs an explicit negative constraint", paper=code, path=rel(manifest_path))
        inv_path = notes / "stage1_phase2_source_inventory.tsv"
        inv = set(inventory_ids(inv_path)) if inv_path.is_file() else set()
        planned = {
            source
            for claim in claims if isinstance(claim, dict)
            for source in claim.get("planned_refs", [])
        }
        audit.require(planned <= inv, "I007_CLAIM_MANIFEST", f"planned references outside frozen inventory: {sorted(planned - inv)}", paper=code, path=rel(manifest_path))
        mappings = lineage.get("mappings", [])
        audit.require(len(mappings) == 8, "I008_CLAIM_LINEAGE", "expected eight lineage mappings", paper=code, path=rel(lineage_path))
        audit.require({item.get("stage2_claim_id") for item in mappings if isinstance(item, dict)} == set(claim_ids), "I008_CLAIM_LINEAGE", "lineage does not cover the eight Stage-2 claims exactly", paper=code, path=rel(lineage_path))
        audit.require(all(item.get("strength_relation") == "same_or_narrower" for item in mappings if isinstance(item, dict)), "I008_CLAIM_LINEAGE", "all lineage relations must be same_or_narrower", paper=code, path=rel(lineage_path))
        audit.metrics["claim_intents"] += len(claims)
        audit.metrics["lineage_mappings"] += len(mappings)


def strip_comments(text: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def tex_words(text: str) -> list[str]:
    text = strip_comments(text)
    text = re.sub(r"\\begin\{(?:equation\*?|align\*?|displaymath|verbatim)\}.*?\\end\{(?:equation\*?|align\*?|displaymath|verbatim)\}", " ", text, flags=re.S)
    text = re.sub(r"\$.*?\$|\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("{", " ").replace("}", " ").replace("~", " ")
    return WORD_RE.findall(text)


def document_body(text: str) -> str:
    start_doc = text.find(r"\begin{document}")
    search_start = max(start_doc, 0)
    start = -1
    for match in re.finditer(r"\\section\*?\{", text[search_start:]):
        absolute = search_start + match.start()
        if "introduction" in text[absolute:absolute + 220].lower():
            start = absolute
            break
    if start < 0:
        start = search_start
    ends: list[int] = []
    for match in re.finditer(r"\\(?:section\*?|paragraph)\{", text[start:]):
        absolute = start + match.start()
        window = text[absolute:absolute + 180].lower()
        if "declaration" in window or "author contribution" in window:
            ends.append(absolute)
            break
    bib = text.find(r"\bibliographystyle", start)
    if bib >= 0:
        ends.append(bib)
    return text[start:min(ends) if ends else len(text)]


def normalized(text: str) -> str:
    value = text.replace(r"\hspace{0pt}", "")
    value = value.replace(r"\_", "_").replace(r"\^{}", "^")
    value = value.replace("\\", "")
    value = value.replace("{", " ").replace("}", " ").replace("$", " ")
    value = re.sub(r"\s+", " ", value)
    return value.lower()


def english_abstract_words(text: str) -> int:
    match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
    return len(tex_words(match.group(1))) if match else 0


def chinese_abstract_han(text: str) -> int:
    clean = text.replace(r"\hspace{0pt}", "")
    match = re.search(r"\\begin\{zhabstract\}(.*?)\\end\{zhabstract\}", clean, re.S)
    if match:
        return len(HAN_RE.findall(match.group(1)))
    doc = clean[clean.find(r"\begin{document}"):] if r"\begin{document}" in clean else clean
    title = doc.find("繁體中文摘要")
    if title < 0:
        return 0
    start = doc.find("\n", title)
    stop = doc.find("關鍵詞", start)
    if stop < 0:
        stop = doc.find(r"\end{otherlanguage}", start)
    if start < 0 or stop < 0:
        return 0
    return len(HAN_RE.findall(doc[start:stop]))


def keyword_counts(text: str) -> tuple[int, int]:
    clean = text.replace(r"\hspace{0pt}", "")
    en_match = re.search(
        r"\\textbf\{Keywords:\}\s*(.*?)(?=\n\s*\n|\\section\*?\{|\\begin\{zhabstract\}|\\medskip)",
        clean,
        re.S | re.I,
    )
    en = len([item for item in en_match.group(1).split(";") if item.strip()]) if en_match else 0
    pos = clean.rfind("關鍵詞")
    zh = 0
    if pos >= 0:
        segment = clean[pos:]
        stops = [value for value in (segment.find("\n\n"), segment.find(r"\hypertarget", 1), segment.find(r"\section", 1)) if value >= 0]
        if stops:
            segment = segment[:min(stops)]
        zh = len([item for item in segment.split("；") if HAN_RE.search(item)])
    return en, zh


def bibliography_keys(text: str) -> list[str]:
    return BIB_RE.findall(text)


def citation_groups(text: str) -> list[dict[str, Any]]:
    groups = []
    for match in CITE_RE.finditer(text):
        groups.append({
            "start": match.start(),
            "end": match.end(),
            "optional": match.group(1).strip(),
            "keys": tuple(key.strip() for key in match.group(2).split(",") if key.strip()),
        })
    return groups


def marker_groups(text: str) -> tuple[list[dict[str, Any]], list[str]]:
    groups: list[dict[str, Any]] = []
    invalid: list[str] = []
    offset = 0
    for line in text.splitlines(keepends=True):
        raw = line.rstrip("\r\n")
        if raw.startswith("% ARS-CITE"):
            match = MARKER_RE.fullmatch(raw)
            if not match:
                invalid.append(raw)
            else:
                groups.append({
                    "start": offset,
                    "end": offset + len(raw),
                    "keys": tuple(key for key in match.group(1).split(",") if key),
                })
        offset += len(line)
    return groups, invalid


def pair_markers(cites: list[dict[str, Any]], markers: list[dict[str, Any]]) -> tuple[int, int]:
    unmatched = set(range(len(cites)))
    paired = 0
    for marker in markers:
        candidates: list[tuple[int, int]] = []
        for index in unmatched:
            cite = cites[index]
            if cite["keys"] != marker["keys"]:
                continue
            gap = min(abs(marker["start"] - cite["end"]), abs(cite["start"] - marker["end"]))
            if gap <= 1200:
                candidates.append((gap, index))
        if candidates:
            _, index = min(candidates)
            unmatched.remove(index)
            paired += 1
    return paired, len(unmatched)


def check_declarations(audit: Audit, code: str, text: str, path: Path) -> None:
    lower = normalized(text)
    required = (
        "liang wang",
        "school of artificial intelligence and automation",
        "huazhong university of science and technology",
        "luoyu road 1037",
        "430070",
        "hubei",
        "p.r. china",
        "wangliang.f@gmail.com",
        "funding",
        "competing",
        "author contribution",
        "ethics",
        "data",
        "materials",
        "openai codex",
        "gpt-5",
        "responsible human author",
        "backend",
    )
    missing = [token for token in required if token not in lower]
    audit.require(not missing, "D015_AUTHOR_DECLARATIONS", f"missing declaration/author tokens: {missing}", paper=code, path=rel(path))
    audit.require("no funding" in lower or "received no funding" in lower, "D015_AUTHOR_DECLARATIONS", "funding declaration is not explicitly zero", paper=code, path=rel(path))
    audit.require("full-text" in lower or "full text" in lower, "D015_AUTHOR_DECLARATIONS", "human full-text verification limitation is absent", paper=code, path=rel(path))


def check_firewalls(audit: Audit, code: str, text: str, bib: str, path: Path) -> None:
    source = text + "\n" + bib
    lower = normalized(source)
    forbidden = {
        "D016_SCIENCE_FIREWALL": (
            r"SCIENTIFIC_EXECUTION=(?!NOT_RUN)",
            r"NEW_RETRIEVAL=(?!NO)",
            r"CANONICAL_RESULTS?_REFRESH=(?:RUN|YES|TRUE)",
        ),
        "D017_ROUTE_FIREWALL": (
            r"FORMAL_ROUTE_A_TUPLE=(?!UNASSIGNED)",
            r"POSITIVE_ARITHMETIC_A2=(?:1/1|TRUE|YES)",
            r"ROUTE_B_INVOCATION=(?:TRUE|YES|1)",
            r"ROUTE_A_SUCCESS_ROUTE_B_READY",
            r"HILBERT_POLYA_REALIZATION",
            r"STAGE2_5_INTEGRITY=(?!NOT_STARTED)",
        ),
    }
    for failure_code, patterns in forbidden.items():
        hits = [pattern for pattern in patterns if re.search(pattern, source, re.I)]
        audit.require(not hits, failure_code, f"forbidden promotion/status patterns: {hits}", paper=code, path=rel(path))
    audit.require("unassigned" in lower, "D017_ROUTE_FIREWALL", "formal Route-A tuple is not visibly UNASSIGNED", paper=code, path=rel(path))
    route_b_negative = "route b remains" in lower or "route b is closed" in lower or "route b closed" in lower or "route-b invocation" in lower or "route b remains uninvoked" in lower
    audit.require(route_b_negative, "D017_ROUTE_FIREWALL", "Route-B closure/noninvocation is not explicit", paper=code, path=rel(path))
    a2_negative = "positive arithmetic a2" in lower and ("absent" in lower or "0/1" in lower or "not eligible" in lower or "remains" in lower)
    audit.require(a2_negative, "D017_ROUTE_FIREWALL", "positive arithmetic A2 absence is not explicit", paper=code, path=rel(path))

    missing = [token for token in PAPERS[code]["special"] if token not in lower]
    audit.require(not missing, "D018_SPECIAL_BOUNDARY", f"missing paper-specific frozen-boundary tokens: {missing}", paper=code, path=rel(path))
    if code == "P33":
        audit.require("P33_RC_1_IMPLEMENTED=0/7" in text, "D018_SPECIAL_BOUNDARY", "P33 machine boundary does not retain P33-RC-1=0/7", paper=code, path=rel(path))
        audit.require("ROUTE_B_INVOCATION=false" in text, "D017_ROUTE_FIREWALL", "P33 machine boundary does not close Route B", paper=code, path=rel(path))
        audit.require("SCIENTIFIC_EXECUTION=NOT_RUN" in text, "D016_SCIENCE_FIREWALL", "P33 machine boundary does not state scientific nonexecution", paper=code, path=rel(path))
        audit.require("PRODUCERS_IMPLEMENTED=2/2" not in source and "P33_RC_1_IMPLEMENTED=7/7" not in source, "D016_SCIENCE_FIREWALL", "P33 contains a completed implementation status", paper=code, path=rel(path))


def check_draft(audit: Audit) -> None:
    totals = {
        "papers": 0,
        "body_words": 0,
        "bibliography_entries": 0,
        "citation_calls": 0,
        "citation_key_occurrences": 0,
        "citation_markers": 0,
        "unique_cited_keys": 0,
        "english_abstract_words": 0,
        "traditional_chinese_abstract_han": 0,
    }

    for code in audit.papers:
        _, paper_dir, notes = paper_paths(code)
        tex_path = paper_dir / "manuscript.tex"
        bib_path = paper_dir / "references.bib"
        map_path = notes / "stage2_bib_key_map.json"
        files_ok = all(
            audit.require(path.is_file(), "D001_MISSING_DRAFT", "required draft artifact is absent", paper=code, path=rel(path))
            for path in (tex_path, bib_path, map_path)
        )
        if not files_ok:
            continue
        try:
            text = tex_path.read_text(encoding="utf-8")
            bib = bib_path.read_text(encoding="utf-8")
        except UnicodeError as exc:
            audit.fail("D020_TEX_ENCODING", f"UTF-8 decode failed: {exc}", paper=code, path=rel(tex_path))
            continue
        row = input_row(audit, code)
        if row:
            audit.require(sha256(tex_path) != row.get("canonical_manuscript_sha256"), "D002_STALE_SKELETON", "manuscript still has the frozen pre-write skeleton hash", paper=code, path=rel(tex_path))
            audit.require(sha256(bib_path) != row.get("canonical_bibliography_sha256"), "D002_STALE_SKELETON", "bibliography still has the frozen pre-write placeholder hash", paper=code, path=rel(bib_path))

        key_map = load_json(audit, map_path, "D003_BIB_MAP_SCHEMA", code)
        if not key_map:
            continue
        audit.require(set(key_map) == MAP_SCHEMA_KEYS, "D003_BIB_MAP_SCHEMA", f"map keys must be exactly {sorted(MAP_SCHEMA_KEYS)}", paper=code, path=rel(map_path))
        audit.require(key_map.get("schema") == "round10-stage2-bib-key-map/1.0" and key_map.get("paper") == code, "D003_BIB_MAP_SCHEMA", "wrong map schema or paper code", paper=code, path=rel(map_path))
        inv_value = key_map.get("inventory_path")
        inv_path = ROOT / str(inv_value)
        inv_safe = isinstance(inv_value, str) and inv_path.resolve().is_relative_to(ROOT.resolve())
        audit.require(inv_safe and inv_path.is_file(), "D004_BIB_MAP_CLOSURE", "map inventory path is absent or outside repository", paper=code, path=str(inv_value))
        if not inv_safe or not inv_path.is_file():
            continue
        audit.require(sha256(inv_path) == key_map.get("inventory_sha256"), "D004_BIB_MAP_CLOSURE", "inventory hash differs from bib-key map", paper=code, path=rel(inv_path))
        ids = inventory_ids(inv_path)
        mapping = key_map.get("source_to_bibtex_key")
        audit.require(isinstance(mapping, dict), "D003_BIB_MAP_SCHEMA", "source_to_bibtex_key must be an object", paper=code, path=rel(map_path))
        if not isinstance(mapping, dict):
            continue
        audit.require(len(ids) == PAPERS[code]["sources"] and len(set(ids)) == len(ids), "D004_BIB_MAP_CLOSURE", f"expected {PAPERS[code]['sources']} unique inventory IDs", paper=code, path=rel(inv_path))
        audit.require(set(mapping) == set(ids), "D004_BIB_MAP_CLOSURE", f"map/inventory source-ID difference: {sorted(set(mapping) ^ set(ids))}", paper=code, path=rel(map_path))
        mapped_keys = list(mapping.values())
        audit.require(len(set(mapped_keys)) == len(mapped_keys) and all(re.fullmatch(fr"{code}-S\d{{2}}", str(key)) for key in mapped_keys), "D004_BIB_MAP_CLOSURE", "BibTeX values must be unique paper-namespaced keys", paper=code, path=rel(map_path))

        bib_keys = bibliography_keys(bib)
        bib_set = set(bib_keys)
        audit.require(len(bib_keys) == len(bib_set), "D005_BIB_KEY_CLOSURE", "duplicate BibTeX keys detected", paper=code, path=rel(bib_path))
        audit.require(bib_set == set(mapped_keys), "D005_BIB_KEY_CLOSURE", f"BibTeX/map difference: {sorted(bib_set ^ set(mapped_keys))}", paper=code, path=rel(bib_path))
        malformed_accents = re.findall(r"(?<!\\)\{[\"'][A-Za-z]", bib)
        audit.require(not malformed_accents, "D020_TEX_ENCODING", f"malformed BibTeX accent escapes: {malformed_accents[:5]}", paper=code, path=rel(bib_path))

        cites = citation_groups(text)
        cite_keys = [key for group in cites for key in group["keys"]]
        cite_set = set(cite_keys)
        audit.require(cite_set == bib_set, "D006_CITE_KEY_CLOSURE", f"citation/BibTeX difference: {sorted(cite_set ^ bib_set)}", paper=code, path=rel(tex_path))
        audit.require(all(not group["optional"] for group in cites), "D009_LOCATOR_OR_QUOTE", "optional citation locators are prohibited in Stage 2", paper=code, path=rel(tex_path))
        markers, invalid_markers = marker_groups(text)
        audit.require(not invalid_markers, "D007_MARKER_SYNTAX", f"invalid ARS marker lines: {invalid_markers[:3]}", paper=code, path=rel(tex_path))
        marker_keys = [key for marker in markers for key in marker["keys"]]
        audit.require(set(marker_keys) == bib_set, "D008_MARKER_CLOSURE", f"marker/BibTeX difference: {sorted(set(marker_keys) ^ bib_set)}", paper=code, path=rel(tex_path))
        paired, unmatched = pair_markers(cites, markers)
        audit.require(paired == len(markers) == len(cites) and unmatched == 0, "D008_MARKER_CLOSURE", f"paired={paired}; markers={len(markers)}; citations={len(cites)}; unmatched_citations={unmatched}", paper=code, path=rel(tex_path))

        document = text[text.find(r"\begin{document}"):] if r"\begin{document}" in text else text
        quote_envs = re.findall(r"\\begin\{(?:quote|quotation)\}", document)
        audit.require(not quote_envs and r"\blockquote" not in document, "D009_LOCATOR_OR_QUOTE", "direct quotation environment/command appears in document body", paper=code, path=rel(tex_path))
        audit.require(r"\usepackage[numbers,sort&compress]{natbib}" in text and r"\bibliographystyle{plainnat}" in text and r"\bibliography{references}" in text, "D010_CITATION_STYLE", "required natbib/plainnat/references binding is absent", paper=code, path=rel(tex_path))

        lower = normalized(text)
        required_sections = (
            "introduction",
            "literature",
            "methodology",
            "evidence-synthesis",
            "reproducibility",
            "discussion",
            "limitation",
            "future work",
            "conclusion",
        )
        missing_sections = [name for name in required_sections if name not in lower]
        audit.require(not missing_sections, "D011_STRUCTURE", f"missing article sections: {missing_sections}", paper=code, path=rel(tex_path))
        audit.require(r"\documentclass" in text and r"\begin{document}" in text and r"\end{document}" in text, "D011_STRUCTURE", "incomplete LaTeX document envelope", paper=code, path=rel(tex_path))

        en_abs = english_abstract_words(text)
        zh_abs = chinese_abstract_han(text)
        en_kw, zh_kw = keyword_counts(text)
        body_words = len(tex_words(document_body(text)))
        audit.require(150 <= en_abs <= 300, "D012_ABSTRACT_LENGTH", f"English abstract has {en_abs} words; required 150--300", paper=code, path=rel(tex_path))
        audit.require(300 <= zh_abs <= 500, "D012_ABSTRACT_LENGTH", f"Traditional-Chinese abstract has {zh_abs} Han characters; required 300--500", paper=code, path=rel(tex_path))
        audit.require(5 <= en_kw <= 7 and 5 <= zh_kw <= 7, "D013_KEYWORD_COUNT", f"keyword counts English={en_kw}, Traditional-Chinese={zh_kw}; each required 5--7", paper=code, path=rel(tex_path))
        audit.require(body_words >= 4000, "D014_BODY_LENGTH", f"English body has {body_words} words; minimum is 4000", paper=code, path=rel(tex_path))

        stale = re.findall(r"(?i)\b(?:TODO|TBD|FIXME)\b|pre-stage-1 skeleton|skeleton only|lorem ipsum|citation needed", text)
        audit.require(not stale, "D019_STALE_TOKEN", f"stale draft tokens: {stale[:5]}", paper=code, path=rel(tex_path))
        check_declarations(audit, code, text, tex_path)
        check_firewalls(audit, code, text, bib, tex_path)

        per_paper = {
            "body_words": body_words,
            "english_abstract_words": en_abs,
            "traditional_chinese_abstract_han": zh_abs,
            "english_keywords": en_kw,
            "traditional_chinese_keywords": zh_kw,
            "bibliography_entries": len(bib_set),
            "citation_calls": len(cites),
            "citation_key_occurrences": len(cite_keys),
            "citation_markers": len(markers),
            "unique_cited_keys": len(cite_set),
            "manuscript_sha256": sha256(tex_path),
            "bibliography_sha256": sha256(bib_path),
            "bib_key_map_sha256": sha256(map_path),
        }
        audit.metrics.setdefault("per_paper", {})[code] = per_paper
        totals["papers"] += 1
        for name in totals:
            if name != "papers" and name in per_paper:
                totals[name] += int(per_paper[name])

    audit.metrics["draft_totals"] = totals


def pdf_pages(path: Path) -> int:
    result = subprocess.run(
        ("pdfinfo", str(path)),
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=30,
    )
    match = re.search(r"(?m)^Pages:\s+(\d+)", result.stdout)
    return int(match.group(1)) if match else 0


def isolated_build(audit: Audit, code: str, paper_dir: Path) -> dict[str, int] | None:
    required = ("lualatex", "bibtex", "pdfinfo")
    missing = [tool for tool in required if shutil.which(tool) is None]
    if missing:
        audit.fail("F003_BUILD_RECEIPT", f"build tools unavailable: {missing}", paper=code, path=rel(paper_dir))
        return None
    chain = (
        ("lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=paper", "manuscript.tex"),
        ("bibtex", "paper"),
        ("lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=paper", "manuscript.tex"),
        ("lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=paper", "manuscript.tex"),
    )
    try:
        with tempfile.TemporaryDirectory(prefix="round10-stage2-audit-") as tmp:
            work = Path(tmp)
            for name in ("manuscript.tex", "references.bib"):
                shutil.copy2(paper_dir / name, work / name)
            logs: list[str] = []
            for command in chain:
                result = subprocess.run(
                    command,
                    cwd=work,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    timeout=120,
                )
                logs.append(result.stdout)
                if result.returncode:
                    audit.fail("F003_BUILD_RECEIPT", f"isolated build command failed: {' '.join(command)}", paper=code, path=rel(paper_dir / "manuscript.tex"))
                    return None
            # First-pass undefined citations are expected before BibTeX.  The
            # integrity decision is based on the final LuaLaTeX pass and its
            # final log after the complete build chain.
            final_log = (work / "paper.log").read_text(encoding="utf-8", errors="replace")
            combined = (logs[-1] + "\n" + final_log).lower()
            fatal_patterns = (
                "undefined citations",
                "undefined references",
                "there were undefined",
                "missing character:",
                "overfull \\hbox",
                "fatal error",
            )
            hits = [pattern for pattern in fatal_patterns if pattern in combined]
            audit.require(not hits, "F005_BUILD_LOG", f"isolated build log findings: {hits}", paper=code, path=rel(paper_dir / "manuscript.tex"))
            pdf = work / "paper.pdf"
            if not audit.require(pdf.is_file() and pdf.read_bytes().startswith(b"%PDF-"), "F002_PDF_INVALID", "isolated build did not produce a valid PDF", paper=code, path=rel(paper_dir / "manuscript.tex")):
                return None
            return {
                "pages": pdf_pages(pdf),
                "underfull_boxes": combined.count("underfull \\hbox") + combined.count("underfull \\vbox"),
            }
    except (OSError, subprocess.SubprocessError) as exc:
        audit.fail("F003_BUILD_RECEIPT", f"isolated build exception: {exc}", paper=code, path=rel(paper_dir / "manuscript.tex"))
        return None


def check_full(audit: Audit) -> None:
    audit.metrics["fresh_builds"] = 0
    audit.metrics["fresh_build_pages"] = 0
    audit.metrics["canonical_pdf_pages"] = 0
    manifest_path = ROOT / "BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json"
    output_manifest = load_json(audit, manifest_path, "F008_OUTPUT_MANIFEST")
    if output_manifest:
        audit.require(output_manifest.get("schema") == "round10-stage2-output-manifest/1.0", "F008_OUTPUT_MANIFEST", "unexpected output-manifest schema", path=rel(manifest_path))

    for code in audit.papers:
        base, paper_dir, notes = paper_paths(code)
        tex_path = paper_dir / "manuscript.tex"
        bib_path = paper_dir / "references.bib"
        pdf_path = paper_dir / "paper.pdf"
        receipt_path = notes / "stage2_build_receipt.json"
        review_path = notes / "stage2_independent_recheck.md"
        paper_readme = paper_dir / "README.md"
        paper_audit = paper_dir / "stage2_manuscript_audit.md"
        state_path = notes / "pipeline_state.md"
        root_readme = base / "README.md"

        if audit.require(pdf_path.is_file(), "F001_PDF_MISSING", "canonical Stage-2 PDF is absent", paper=code, path=rel(pdf_path)):
            header_ok = pdf_path.stat().st_size > 1024 and pdf_path.read_bytes()[:5] == b"%PDF-"
            audit.require(header_ok, "F002_PDF_INVALID", "canonical PDF header/size is invalid", paper=code, path=rel(pdf_path))
            if header_ok:
                try:
                    pages = pdf_pages(pdf_path)
                except (OSError, subprocess.SubprocessError) as exc:
                    audit.fail("F002_PDF_INVALID", f"pdfinfo failed: {exc}", paper=code, path=rel(pdf_path))
                    pages = 0
                audit.require(pages > 0, "F002_PDF_INVALID", "PDF has no pages", paper=code, path=rel(pdf_path))
                audit.metrics["canonical_pdf_pages"] += pages

        receipt = load_json(audit, receipt_path, "F003_BUILD_RECEIPT", code)
        if receipt:
            audit.require(receipt.get("schema") == "round10-stage2-build-receipt/1.0" and receipt.get("verdict") == "PASS", "F003_BUILD_RECEIPT", "build receipt schema/verdict is not PASS", paper=code, path=rel(receipt_path))
            expected = {
                "manuscript_sha256": sha256(tex_path) if tex_path.is_file() else "",
                "bibliography_sha256": sha256(bib_path) if bib_path.is_file() else "",
                "pdf_sha256": sha256(pdf_path) if pdf_path.is_file() else "",
            }
            drift = {key: (receipt.get(key), value) for key, value in expected.items() if receipt.get(key) != value}
            audit.require(not drift, "F004_BUILD_HASH", f"build receipt hash drift: {drift}", paper=code, path=rel(receipt_path))
            scan = receipt.get("log_scan", {})
            audit.require(isinstance(scan, dict) and all(value == 0 for value in scan.values()), "F005_BUILD_LOG", f"nonzero receipt log scan: {scan}", paper=code, path=rel(receipt_path))

        if audit.require(review_path.is_file(), "F006_RECHECK", "independent Stage-2 recheck is absent", paper=code, path=rel(review_path)):
            review = review_path.read_text(encoding="utf-8")
            audit.require("PASS" in review and ("8/8" in review or "eight" in review.lower()), "F006_RECHECK", "independent recheck lacks PASS and 8/8 closure", paper=code, path=rel(review_path))

        for path in (paper_readme, paper_audit, state_path, root_readme):
            if audit.require(path.is_file(), "F007_README_STATE", "required README/state artifact is absent", paper=code, path=rel(path)):
                value = path.read_text(encoding="utf-8").lower()
                audit.require("stage 2" in value and "complete" in value and ("stage 2.5" in value or "stage-2.5" in value), "F007_README_STATE", "README/state does not record Stage-2 completion and Stage-2.5 boundary", paper=code, path=rel(path))

        if output_manifest:
            rows = [row for row in output_manifest.get("papers", []) if row.get("paper") == code]
            audit.require(len(rows) == 1, "F008_OUTPUT_MANIFEST", "paper must occur once in output manifest", paper=code, path=rel(manifest_path))
            if len(rows) == 1:
                row = rows[0]
                drift = {}
                for key, path in (
                    ("manuscript_sha256", tex_path),
                    ("bibliography_sha256", bib_path),
                    ("pdf_sha256", pdf_path),
                ):
                    if path.is_file() and row.get(key) != sha256(path):
                        drift[key] = (row.get(key), sha256(path))
                audit.require(not drift, "F008_OUTPUT_MANIFEST", f"output-manifest hash drift: {drift}", paper=code, path=rel(manifest_path))

        built = isolated_build(audit, code, paper_dir)
        if built:
            audit.metrics["fresh_builds"] += 1
            audit.metrics["fresh_build_pages"] += built["pages"]
            audit.metrics.setdefault("per_paper", {}).setdefault(code, {})["fresh_build_pages"] = built["pages"]
            audit.metrics["per_paper"][code]["fresh_build_underfull_boxes"] = built["underfull_boxes"]


def parse_papers(values: list[str] | None) -> list[str]:
    if not values:
        return sorted(PAPERS)
    result: set[str] = set()
    for value in values:
        for item in value.split(","):
            code = item.strip().upper()
            if code == "ALL":
                result.update(PAPERS)
            elif code in PAPERS:
                result.add(code)
            else:
                raise argparse.ArgumentTypeError(f"unknown paper {item!r}; expected P29--P33 or all")
    return sorted(result)


def render_human(payload: dict[str, Any]) -> str:
    lines = [
        f"ROUND10_STAGE2_AUDIT phase={payload['phase']} verdict={payload['verdict']} papers={','.join(payload['papers'])}",
        f"checks={payload['checks_run']} failures={payload['failure_count']}",
    ]
    metrics = payload["metrics"]
    if "draft_totals" in metrics:
        totals = metrics["draft_totals"]
        lines.append(
            "draft_counts "
            f"papers={totals['papers']} body_words={totals['body_words']} "
            f"refs={totals['bibliography_entries']} cites={totals['citation_calls']} "
            f"cite_keys={totals['citation_key_occurrences']} markers={totals['citation_markers']}"
        )
        for code, row in sorted(metrics.get("per_paper", {}).items()):
            lines.append(
                f"{code} body_words={row['body_words']} en_abstract={row['english_abstract_words']} "
                f"zh_han={row['traditional_chinese_abstract_han']} refs={row['bibliography_entries']} "
                f"unique_cited={row['unique_cited_keys']} markers={row['citation_markers']}"
            )
    for failure in payload["failures"]:
        location = f" {failure['path']}" if failure["path"] else ""
        lines.append(f"FAIL {failure['code']} {failure['paper']}{location}: {failure['detail']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase_pos", nargs="?", choices=("inputs", "draft", "full"), help="audit phase")
    parser.add_argument("--phase", dest="phase_opt", choices=("inputs", "draft", "full"), help="audit phase (alternative to positional phase)")
    parser.add_argument("--paper", action="append", help="P29--P33, comma-separated values, or all; repeatable")
    parser.add_argument("--json", action="store_true", help="emit deterministic JSON instead of the compact report")
    args = parser.parse_args(argv)
    if args.phase_pos and args.phase_opt:
        parser.error("provide the phase either positionally or with --phase, not both")
    phase = args.phase_opt or args.phase_pos
    if not phase:
        parser.error("an audit phase is required: inputs, draft, or full")
    try:
        papers = parse_papers(args.paper)
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))

    audit = Audit(phase=phase, papers=papers)
    check_inputs(audit)
    if phase in ("draft", "full"):
        check_draft(audit)
    if phase == "full":
        check_full(audit)

    failures = [failure.as_dict() for failure in sorted(audit.failures)]
    payload = {
        "schema": "round10-stage2-audit-result/1.0",
        "phase": phase,
        "papers": papers,
        "verdict": "PASS" if not failures else "FAIL",
        "checks_run": audit.checks_run,
        "failure_count": len(failures),
        "failures": failures,
        "metrics": audit.metrics,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2))
    else:
        print(render_human(payload))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
