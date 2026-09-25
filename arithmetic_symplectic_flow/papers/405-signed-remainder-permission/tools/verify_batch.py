#!/usr/bin/env python3
"""Read-only batch-L artifact checks, not mathematics or calibrated review.

Run from arithmetic_symplectic_flow. Default mode is strict; --pre-handoff
may report planned missing artifacts but NEVER reports PASS. No file writes,
network, subprocesses, imports or execution of archived verifiers occur.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


BATCH = "NONLINEAR-PACKET-20260923-L"
BASE = Path("papers/405-signed-remainder-permission")
SCRIPT = BASE / "tools/verify_batch.py"
LOG = BASE / "batch-log.md"
SURFACES = ("candidate-card.md", "paper.md", "README.md", "claim-ledger.md")
EVIDENCE = ("scope-review.md", "independent-review-raw.md", "independent-review.md")
# Opening snapshots measured before any new-batch scientific/overview edits.
OPENING = [
    ("400-nonlinear-exchange-return", 11, "0b3d0b248672cd61e0fedd34f8547eb86565931bfbd677fc206f4ed9395d5c9e"),
    ("401-matrix-remainder-feedback", 7, "9557752116139aa3ae32d7705a33d03220f9c6a645e1ef266bc1c73356b989b7"),
    ("402-quaternion-divisor-memory", 7, "9ab1bd0194af2b8a377f6e04ec4a2554a665db6d01d2362644d94cb39bca0f7a"),
    ("403-affine-torus-admission", 7, "5dfbf65cedfb508ac9bfa8ca76d57500d08840b6c0d7b2127404cb7b3c66dd02"),
    ("404-gaussian-cycle-norm", 7, "05e048daef40393b2c1b430a2423a27e0723f3f6c4760a1145a0e09ec63f0eb6"),
]
ANCHORS = [
    ("AGENTS.md", "86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d"),
    ("plan.md", "9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0"),
    ("docs/prior_work/README.md", "d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd"),
    ("papers/paper-template.md", "ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b"),
    ("papers/283-nonlinear-residue-clock-screen/paper.md", "50429784fc1f634da86aa6aae1aac1b0e109b7fcc82a6169a68bb80a5bf95d38"),
]
PACKAGES = [
    ("405-signed-remainder-permission", "ANG-20260923-SRP01", [
        (96, "d69d39a4115002b725175ca673e42e617a687abbe2eb53f2a6808b80ec1d0540"),
        (101, "02c8aa8e26bb30dc3ab9e85509db99062e615b578a40a2f30807aea303061b79")]),
    ("406-moving-sum-divisor", "ANG-20260923-MSD01", [
        (93, "ef460079eb0f5f604822611f93e09382fcd688a4e3d49f037e07ac04ffaba80c")]),
    ("407-divisor-power-reassembly", "ANG-20260923-DPR01", [
        (105, "52ad8cc8d271c49317cf7245aed09ef3d421d2245b3b091c0f6c5054c96b25a1")]),
    ("408-conjugation-packet-involution", "ANG-AUDIT-20260923-CPI01", [
        (75, "e510fd67204c529c745e272cb9ac38673446efb7c2fb510321084763396fb00b"),
        (81, "2a6f1a70c08b1cfc2c434cc002c0693c8fd696ddf24326e71a312f37294dceae")]),
    ("409-first-return-clock-audit", "ANG-AUDIT-20260923-FRC01", [
        (85, "bb233bb504c4fa265df1807f7b0377397dfb3a571199c2ef3bff28a8bc1d9069"),
        (94, "9e0220ef714ed52af183a5db5ad4f722ec984eef7364654d6a4274ead513cfee")]),
]
OVERVIEWS = [
    ("readme.md", "# Arithmetic Symplectic Flow\n\n> **Round 2 — Candidate Engineering / Structural Synthesis**\n",
     "> **Preceding batch handoff (2026-09-23): NONLINEAR-RETURN",
     "> **Current workflow state (2026-09-23): NONLINEAR-RETURN",
     "c130e2c8be92b332b00d9c27ccf6bef5758908db3537fb3a1cefaaef21fc6b67"),
    ("papers/README.md", "# Markdown paper registry\n\n",
     "**Preceding batch handoff (2026-09-23): Nonlinear-return",
     "**Current workflow state (2026-09-23): Nonlinear-return",
     "b632c8629fa9edbb84f4991cedb22a728249ef374b0fce88f00ecfa08701d0b3"),
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def read(file):
    # Bytes first: do not silently normalize CRLF before validation or hashing.
    return Path(file).read_bytes().decode("utf-8")


def files(directory):
    directory = Path(directory)
    require(not directory.is_symlink(), "Unexpected symlink: " + str(directory))
    result = []
    for entry in directory.iterdir():
        require(not entry.is_symlink(), "Unexpected symlink: " + str(entry))
        if entry.is_dir():
            result.extend(files(entry))
        else:
            require(entry.is_file(), "Unexpected non-regular file: " + str(entry))
            result.append(entry)
    return sorted(result, key=lambda file: file.as_posix())


def archived_anchors(source, pattern, expected, label):
    block = re.search(pattern, read(source), re.S)
    require(block is not None, "Missing archived anchor block: " + label)
    rows = [(name, int(count), digest) for name, count, digest in re.findall(
        r"\['([^']+)',(\d+),'([a-f0-9]{64})'\]", block.group(1))]
    require(len(rows) == expected, "Archived anchor count: " + label)
    return rows


def normalize_outcome(value):
    value = re.sub(r"\*\*|`", "", value).strip()
    return re.sub(r"\s+", " ", re.sub(r"[.。]$", "", value))


def unique_rows(rows, label):
    require(len({row[0] for row in rows}) == len(rows), "Duplicate " + label)
    return {row[0]: row[1:] for row in rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pre-handoff", action="store_true")
    parser.add_argument("--brief", action="store_true")
    args = parser.parse_args()
    pending = set()
    pre = args.pre_handoff
    required = [Path("papers") / directory / name
                for directory, _, _ in PACKAGES for name in SURFACES]
    required += [Path("papers") / directory / "evidence" / name
                 for directory, _, _ in PACKAGES for name in EVIDENCE]
    required += [LOG, BASE / "batch-summary.md", BASE / "evidence/verification.md"]
    planned = {file.resolve() for file in required}
    for file in required:
        if pre and not file.exists():
            pending.add("Missing final artifact: " + file.as_posix())
        else:
            require(file.is_file(), "Required final artifact missing: " + str(file))
    batch_log = read(LOG) if LOG.exists() else ""

    # Parse frozen old literals as DATA; never import, eval or run old verifiers.
    old = archived_anchors("papers/360-profinite-two-step-gate/evidence/verify-batch.cjs",
                           r"const old = (\[.*?\n\]);", 12, "348–359")
    old += archived_anchors("papers/365-divisibility-scheduled-radix/evidence/verify-batch.cjs",
                            r"old\.push\((.*?)\n\);", 5, "360–364")
    for directory, label in [
        ("370-divisor-renewal-clock", "365–369"),
        ("375-odd-distance-coprime-measure", "370–374"),
        ("380-factor-allocation-history", "375–379"),
        ("385-divisor-fractional-return", "380–384"),
        ("390-sublattice-interface-screen", "385–389"),
        ("395-simultaneous-content-return", "390–394"),
        ("400-nonlinear-exchange-return", "395–399"),
    ]:
        old += archived_anchors(Path("papers") / directory / "evidence/verify-batch.cjs",
                                r"const opening = (\[.*?\n\]);", 5, label)
    opening_rows = unique_rows(re.findall(
        r"^\| (40[0-4]) \| (\d+) \| `([a-f0-9]{64})` \|$", batch_log, re.M),
        "opening bundle receipt")
    for directory, count, digest in OPENING:
        row = opening_rows.get(directory[:3])
        if pre and row is None:
            pending.add("Opening bundle receipt pending: " + directory)
        else:
            require(row is not None and int(row[0]) == count and row[1] == digest,
                    "Opening receipt changed or missing: " + directory)
    old += OPENING
    require(len(old) == 57 and len({row[0] for row in old}) == 57,
            "Unique old348–404 packages required")
    for directory, count, digest in old:
        base = Path("papers") / directory
        listed = files(base)
        bundle = "".join(file.relative_to(base).as_posix() + "\t" +
                         sha(file.read_bytes()) + "\n" for file in listed)
        require(len(listed) == count and sha(bundle) == digest,
                "Frozen bundle changed: " + directory)
    for file, digest in ANCHORS:
        require(sha(Path(file).read_bytes()) == digest, "Immutable anchor changed: " + file)

    outcome_rows = unique_rows(re.findall(
        r"^\| (40[5-9]) \| `outcome: ([^`\n]+)` \|$", batch_log, re.M | re.I),
        "final outcome receipt")
    outcomes = {number: normalize_outcome(row[0]) for number, row in outcome_rows.items()}
    counts = dict(packages=5, identitySurfaces=0, statusSurfaces=0, markdown=0,
                  relativeLinks=0, frozenPrefixes=0, preservedPackages=len(old),
                  preservedAnchors=len(ANCHORS), preservedOverviewArchives=0,
                  boundEvidenceReceipts=0, boundSurfaceReceipts=0)
    inputs = []

    def destination(target, file):
        target = re.sub(r"^<|>$", "", target).split("#", 1)[0]
        if not target or re.match(r"[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("//"):
            return
        resolved = (file.parent / unquote(target, errors="strict")).resolve()
        if pre and not resolved.exists() and resolved in planned:
            pending.add("Pending linked final artifact: " + str(resolved.relative_to(Path.cwd())))
            return
        require(resolved.exists(), "Broken local link: " + str(file) + " -> " + target)
        counts["relativeLinks"] += 1

    def markdown(source, file):
        require(source.endswith("\n") and "\r" not in source, "LF/final newline: " + str(file))
        body, fence = [], None
        for line in source.split("\n"):
            if fence:
                close = re.match(r"^ {0,3}(`{3,}|~{3,})\s*$", line)
                if close and close[1][0] == fence[0] and len(close[1]) >= len(fence):
                    fence = None
                body.append("")
            else:
                opening = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
                if opening:
                    fence = opening[1]
                    body.append("")
                else:
                    body.append(line)
        require(fence is None, "Unclosed Markdown fence: " + str(file))
        body = "\n".join(body)
        for match in re.finditer(r"\]\((<[^>\n]+>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\)", body):
            destination(match[1], file)
        for match in re.finditer(r"^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", body, re.M):
            destination(match[1], file)

    for directory, candidate_id, freezes in PACKAGES:
        base = Path("papers") / directory
        listed = files(base)
        require(all(file.suffix == ".md" or file == SCRIPT for file in listed),
                "Unexpected non-Markdown artifact: " + directory)
        for file in (file for file in listed if file.suffix == ".md"):
            source = read(file)
            markdown(source, file)
            counts["markdown"] += 1
            inputs.append(dict(file=file.as_posix(), lines=source.count("\n"), sha256=sha(source)))
        card = read(base / "candidate-card.md")
        for count, digest in freezes:
            require(sha("\n".join(card.split("\n")[:count]) + "\n") == digest,
                    "Frozen card prefix changed: " + directory + "/" + str(count))
            counts["frozenPrefixes"] += 1
        outcome = outcomes.get(directory[:3])
        if pre and not outcome:
            pending.add("Final outcome receipt pending: " + directory)
        else:
            require(bool(outcome), "Missing final outcome receipt: " + directory)
        for name in SURFACES:
            file = base / name
            if pre and not file.exists():
                continue
            source = read(file)
            require(candidate_id in source, "Candidate ID missing: " + str(file))
            counts["identitySurfaces"] += 1
            lines = source.split("\n")
            status = lines[max(row[0] for row in freezes):] if name == "candidate-card.md" else lines[:20]
            declared = []
            for line in status:
                match = re.match(r"^(?:Final\s+)?Outcome:\s*(.+)$",
                                 re.sub(r"^>\s*", "", normalize_outcome(line)), re.I)
                if match:
                    declared.append(normalize_outcome(match[1]))
            require(len(declared) <= 1, "Ambiguous final Outcome field: " + str(file))
            if pre and (not outcome or not declared):
                pending.add("Final Outcome field/receipt pending: " + str(file))
            else:
                require(len(declared) == 1 and declared[0] == outcome,
                        "Final Outcome field disagrees with batch receipt: " + str(file))
                counts["statusSurfaces"] += 1

    receipt_rows = unique_rows(re.findall(
        r"^\| (40[5-9]) \| `([a-f0-9]{64})` \| `([a-f0-9]{64})` \| `([a-f0-9]{64})` \|$",
        batch_log, re.M), "final evidence receipt")
    aliases = {"paper.md": "Paper", "candidate-card.md": "Card",
               "claim-ledger.md": r"(?:FINAL\s+)?ledger", "README.md": "README"}
    aliases = {name: re.compile(r"^\s*(?:[-*+]|\|)?\s*(?:\*\*)?" + label +
                               r"(?:\*\*)?(?=[,\s:|])", re.I) for name, label in aliases.items()}
    for directory, _, _ in PACKAGES:
        row = receipt_rows.get(directory[:3])
        if pre and row is None:
            pending.add("Final evidence receipt pending: " + directory)
            continue
        require(row is not None, "Missing final CP1/raw/review receipt: " + directory)
        base = Path("papers") / directory
        for name, digest in zip(EVIDENCE, row):
            file = base / "evidence" / name
            require(file.is_file() and sha(file.read_bytes()) == digest,
                    "Evidence receipt mismatch: " + str(file))
        review = read(base / "evidence/independent-review.md")
        require(all(re.search(r"\b" + checkpoint + r"\s*:?\s*(?:\*\*|`)?PASS\b", review)
                    for checkpoint in ("CP2", "CP3")),
                "Final CP2/CP3 PASS markers missing: " + directory)
        review_lines = review.split("\n")
        for name in SURFACES:
            digest = sha((base / name).read_bytes())
            alias_rows = [line for line in review_lines if aliases[name].search(line)
                          and re.findall(r"\b[a-f0-9]{64}\b", line) == [digest]]
            require(len(alias_rows) <= 1, "Ambiguous aliased surface receipt: " + directory + "/" + name)
            bound = len(alias_rows) == 1
            for index, line in enumerate(review_lines):
                if bound or name not in line:
                    continue
                if digest in line:
                    bound = True
                    continue
                if any(other != name and other in line for other in SURFACES):
                    continue
                for following in review_lines[index + 1:index + 3]:
                    if any(other in following for other in SURFACES):
                        break
                    if digest in following:
                        bound = True
                        break
            require(bound, "Reviewed final-surface receipt mismatch: " + directory + "/" + name)
            counts["boundSurfaceReceipts"] += 1
        counts["boundEvidenceReceipts"] += 3

    for name, prefix, marker, original_marker, digest in OVERVIEWS:
        file = Path(name)
        source = read(file)
        markdown(source, file)
        if pre and sha(source) == digest:
            pending.add("New overview handoff not yet prepended: " + name)
            continue
        index = source.find(marker)
        require(index >= 0, "Old overview archive marker missing: " + name)
        archive = prefix + source[index:].replace(marker, original_marker, 1)
        require(sha(archive) == digest, "Old overview archive changed: " + name)
        current = source[:index]
        require("2026-09-23" in current and "5/5" in current,
                "Current five-round overview marker missing: " + name)
        for directory, _, _ in PACKAGES:
            require(directory + "/README.md" in current,
                    "Current overview package missing: " + name + "/" + directory)
        counts["preservedOverviewArchives"] += 1
    if pre:
        pending.add("Pre-handoff mode: rerun without --pre-handoff for final handoff")
    else:
        require(counts["identitySurfaces"] == counts["statusSurfaces"] == 20
                and len(outcomes) == 5 and counts["boundEvidenceReceipts"] == 15
                and counts["boundSurfaceReceipts"] == 20
                and counts["preservedOverviewArchives"] == 2 and not pending,
                "Incomplete strict handoff")
    result = dict(result="PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL" if pre else "PASS",
                  scope="Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.",
                  reviewCalibration="NOT_CALIBRATED", batch=BATCH, **counts,
                  pending=sorted(pending))
    if not args.brief:
        result["inputs"] = inputs
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, UnicodeError, ValueError) as error:
        print(json.dumps(dict(result="FAIL", error=str(error)), ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
# EOF: all task operations read local files or write results to stdout/stderr only.
