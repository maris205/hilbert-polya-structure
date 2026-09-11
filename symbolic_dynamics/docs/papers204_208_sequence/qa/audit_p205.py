#!/usr/bin/env python3
"""Read-only P205 terminal artifact gate for this batch's modular layout.

Checks retained actual evidence and full dependency pins. It does not
execute mathematical producers, manufacture page views, or prove theorems.
"""
import ast
import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[3]
BATCH = ROOT / "docs/papers204_208_sequence"
PAPER = ROOT / "papers/205-conflict-triggered-cyclic-increments"
CHECKS = []


def require(test, name):
    if not test:
        raise AssertionError(name)
    CHECKS.append(name)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files(folder):
    return {p.relative_to(folder).as_posix() for p in folder.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts}


def manifest(path, base, closed=False):
    names = []
    for line in path.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, f"manifest syntax {path}:{line}")
        pin, name = match.groups()
        target = base / name
        require(target.is_file() and not target.is_symlink(), f"regular pin {target}")
        require(digest(target) == pin, f"hash pin {target}")
        names.append(name)
    require(len(names) == len(set(names)), f"unique pins {path}")
    if closed:
        require(set(names) == files(base) - {path.name}, f"full nonself coverage {path}")
    return len(names)


def same(a, b):
    require(a.read_bytes() == b.read_bytes(), f"raw equality {a} {b}")


def imports(path):
    tree = ast.parse(path.read_text())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        if isinstance(node, ast.ImportFrom):
            require(not node.level, f"no relative imports {path}")
            names.add(node.module)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            require(node.func.id not in {"open", "eval", "exec", "__import__"},
                    f"no dynamic/file call {path}:{node.lineno}")
    require(names <= {"collections", "itertools", "hashlib", "heapq", "json"},
            f"standalone known stdlib imports {path}")
    return sorted(names)


def main():
    freeze_entries = []
    for k in range(3):
        freeze = PAPER / f"frozen_round{k}"
        freeze_entries.append(manifest(freeze / "SHA256SUMS", freeze, True))
        for name in files(freeze) - {"SHA256SUMS"}:
            same(freeze / name, PAPER / name)
    same(PAPER / "frozen_round0/SHA256SUMS", PAPER / "frozen_round2/SHA256SUMS")
    review_entries, reviewers = {}, []
    for letter in ("a", "b"):
        review = BATCH / f"reviews/p205_{letter}"
        review_entries[letter] = manifest(review / "SHA256SUMS", review, True)
        # The role contract permits distinct file names. Inspect each actual
        # accepted delta rather than rename an immutable reviewer package.
        after_names = {"a": ("AFTER_FROZEN_PINS.sha256", "AFTER_LIVE_PINS.sha256"),
                       "b": ("AFTER_INPUT_PINS.sha256", "LIVE_INPUT_PINS.sha256")}
        for name in ("INPUT_PINS.sha256", *after_names[letter]):
            manifest(review / name, ROOT)
        findings = json.loads((review / "FINDINGS.json").read_text())
        require(all(value == 0 for value in findings["counts"].values()), f"zero {letter} findings")
        require(not findings["findings"], f"empty {letter} finding list")
        require(findings["review_state"] == f"{letter.upper()}_ACCEPTED_NO_CHANGE", f"accepted {letter}")
        require(findings["acceptance"]["delta_status"] == "ACCEPTED_EXACT_NO_CHANGE", f"actual {letter} delta")
        require(not findings["independence"]["is_proof_or_manuscript_author"], f"nonauthor {letter}")
        require(not findings["independence"]["supplied_new_lemma_or_manuscript_text"], f"no proof contribution {letter}")
        require(findings["external_status"] == "HOLD_EXTERNAL", f"external hold {letter}")
        reviewers.append(findings["reviewer"])
    require(len(set(reviewers)) == 2 and "/root" not in reviewers, "two distinct nonroot reviewers")
    replay_info = []
    for label, directory, outputs, count in (
        ("author", PAPER, PAPER / "author_replay", 1029769),
        ("A", BATCH / "reviews/p205_a", BATCH / "qa/root_replays/p205_a", 11265033),
        ("B", BATCH / "reviews/p205_b", BATCH / "qa/root_replays/p205_b", 12023630),
    ):
        canonical = directory / "CANONICAL.json"
        code = directory / "verify.py"
        imported = imports(code)
        record = json.loads(canonical.read_text())
        count_keys = {"author": "total_checks", "A": "assertions", "B": "total_assertions"}
        actual = record[count_keys[label]]
        require(actual == count, f"declared actual assertion count {label}")
        for k in (1, 2):
            same(canonical, outputs / f"run{k}.stdout")
            err = outputs / f"run{k}.stderr"
            if err.exists():
                require(err.stat().st_size == 0, f"empty stderr {label} {k}")
        replay_info.append({"label": label, "assertions_each": count,
                            "mode": "reuse prior actual root pair under unchanged full dependency key",
                            "producer_sha256": digest(code), "stdout_sha256": digest(canonical),
                            "imports": imported})
    build_entries = []
    for k in (1, 2):
        build = PAPER / f"qa_final/cold_build_{k}"
        build_entries.append(manifest(build / "SOURCE_INPUTS.sha256", build))
        for line in (build / "SOURCE_INPUTS.sha256").read_text().splitlines():
            name = line.split("  ", 1)[1]
            same(build / name, PAPER / name)
        log = (build / "main.log").read_text()
        require(not re.search(r"undefined|Overfull|Underfull|Warning|^!", log, re.M), f"clean final TeX log {k}")
        require((build / "DIAGNOSTICS.txt").stat().st_size == 0, f"empty diagnostics {k}")
        require("Pages:           3" in (build / "PDFINFO.txt").read_text(), f"three pages {k}")
        info = (build / "PDFINFO.txt").read_text()
        for field in ("Title", "Author", "Creator", "Producer", "CreationDate", "ModDate"):
            found = re.search(rf"^{field}:(.*)$", info, re.M)
            require(not found or not found.group(1).strip(), f"blank metadata {k} {field}")
        font_rows = (build / "FONTS.txt").read_text().splitlines()[2:]
        require(len(font_rows) == 25, f"font row count {k}")
        require(all("Type 1" in row and row.split()[-5] == "yes" for row in font_rows), f"embedded Type 1 fonts {k}")
        same(build / "main.pdf", PAPER / "main.pdf")
    same(PAPER / "qa_final/cold_build_1/main.pdf", PAPER / "qa_final/cold_build_2/main.pdf")
    views = json.loads((PAPER / "qa_final/PAGE_VIEWS.json").read_text())
    require(views["pdf_sha256"] == digest(PAPER / "main.pdf"), "viewed exact final PDF")
    require([p["number"] for p in views["pages"]] == [1, 2, 3], "complete page coverage")
    for page in views["pages"]:
        require(page["actually_viewed"] and page["inspection"], f"actual attestation page {page['number']}")
        require(digest(PAPER / "qa_final" / page["path"]) == page["sha256"], f"exact viewed page {page['number']}")
    links = 0
    for folder in (PAPER, BATCH / "reviews/p205_a", BATCH / "reviews/p205_b"):
        for doc in folder.rglob("*.md"):
            origin = Path(re.sub(r"/frozen_round[012]/", "/", str(doc)))
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text()):
                link = link.strip("<>").split("#", 1)[0]
                if not link or re.match(r"[a-z]+:", link):
                    continue
                require((origin.parent / link).exists(), f"local Markdown link {doc}: {link}")
                links += 1
    print(json.dumps({"paper": "P205", "status": "PASS_TERMINAL_ARTIFACT_GATE",
                      "scope": "One paper only; original proof/source inspection and actual execution/viewing receipts remain controlling",
                      "fresh_mathematical_execution_in_this_auditor": False,
                      "freeze_entries": freeze_entries, "review_manifest_entries": review_entries,
                      "root_replay_pairs": replay_info, "source_only_build_entries": build_entries,
                      "actual_final_pages": 3, "local_markdown_links": links,
                      "checks_passed": len(CHECKS), "auditor_sha256": digest(Path(__file__)),
                      "external_status": "HOLD_EXTERNAL"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
