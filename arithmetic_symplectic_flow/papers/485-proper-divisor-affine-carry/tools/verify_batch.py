#!/usr/bin/env python3
"""Read-only batch-AB artifact checks, not mathematics or calibrated review.

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


BATCH = "PRE-P0-STRUCTURE-20260925-AB"
HANDOFF_DATE = "2026-09-25"
BASE = Path("papers/485-proper-divisor-affine-carry")
SCRIPT = BASE / "tools/verify_batch.py"
LOG = BASE / "batch-log.md"
SURFACES = ("candidate-card.md", "paper.md", "README.md", "claim-ledger.md")
EVIDENCE = ("scope-review.md", "independent-raw.md", "review.md")
# Opening snapshots measured before any new-batch scientific/overview edits.
OPENING = [
    ("480-cf-prefix-period-multipliers", 11, "347b298e1bd8ad511b2d48c6b373c5e5d0447794f80c96312eeab5bb1ed4046c"),
    ("481-divisor-quotient-block-replication", 7, "98a6c08c65a8817e0a828ddcc0e1d303ae402aea3c74509b313ea702a18b93d0"),
    ("482-divisor-gap-factor-sum", 7, "bb6975e2d1a8e074b0569d637ec30f1c00733073e5b4a05215d8515df767e007"),
    ("483-common-factor-transport", 7, "4bd9255f920b56c13ff96f1ee51b993cd78c7e27501944747bcc243dd944c17e"),
    ("484-autonomous-divisor-digit-renewal", 7, "05f7f6f900e472025fba76accc46802b5bad2f6f4b6585abca13e94de9664b86"),
]
ANCHORS = [
    ("AGENTS.md", "86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d"),
    ("plan.md", "9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0"),
    ("docs/prior_work/README.md", "d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd"),
    ("papers/paper-template.md", "ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b"),
    ("papers/283-nonlinear-residue-clock-screen/paper.md", "50429784fc1f634da86aa6aae1aac1b0e109b7fcc82a6169a68bb80a5bf95d38"),
]
PACKAGES = [
    ("485-proper-divisor-affine-carry", "ANG-20260925-DAC01", [
        (88, "ee3e019ee38939ce6188ffd91c6f9d7a530c9410cfdc86672c0dd5edecdf5d9d")]),
    ("486-residue-block-rectangle-flow", "ABF-20260925-RBR01", [
        (91, "e023221e92c2939d80aba491c149437d96d1b1131fbe61045338361ca9dd73ba")]),
    ("487-divisor-scatterer-array", "ABF-20260925-DSA01", [
        (91, "a52c8793de88cd52dd03e0157e6aa755ec641c4ea0fa1ac16691f3865637de72")]),
    ("488-binary-period-root-rewrite", "ANG-20260925-BPR01", [
        (84, "fe59e005a560c186b3c666509318e1043bcc5ab16b8a19348d7acbe8e15b28ee")]),
    ("489-logarithmic-rectangle-control", "ABF-CONTROL-20260925-LRC01", [
        (84, "d875b4d93fa3cd5b37e4fd5a6e6a94a5841bd3ddfcf2a7ad8460f2ca68967068")]),
]
OVERVIEWS = [
    ("readme.md", "# Arithmetic Symplectic Flow\n\n> **Round 2 — Candidate Engineering / Structural Synthesis**\n",
     "> **Preceding batch handoff (2026-09-25): PERIOD-MULTIPLIER",
     "> **Current workflow state (2026-09-25): PERIOD-MULTIPLIER",
     "e56237bff38c85d1d29a7fb42cfc6ec7e6dee77cb738f6b6a977830a536fac50"),
    ("papers/README.md", "# Markdown paper registry\n\n",
     "**Preceding batch handoff (2026-09-25): Period-multiplier",
     "**Current workflow state (2026-09-25): Period-multiplier",
     "fa810e703bbb3cf1da9f4ba80bb542e972dc9e6c64ec754f79f8c0d356afa1ff"),
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


def archived_python_anchors(source, expected, label):
    block = re.search(r"^OPENING = (\[.*?\n\])", read(source), re.M | re.S)
    require(block is not None, "Missing archived Python anchor block: " + label)
    rows = [(name, int(count), digest) for name, count, digest in re.findall(
        r'\("([^"]+)", (\d+), "([a-f0-9]{64})"\)', block.group(1))]
    require(len(rows) == expected, "Archived Python anchor count: " + label)
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
    old += archived_python_anchors(
        "papers/405-signed-remainder-permission/tools/verify_batch.py", 5, "400–404")
    old += archived_python_anchors(
        "papers/410-euclidean-complex-feedback/tools/verify_batch.py", 5, "405–409")
    old += archived_python_anchors(
        "papers/415-divisor-word-sweep/tools/verify_batch.py", 5, "410–414")
    old += archived_python_anchors(
        "papers/420-divisor-reciprocal-displacement/tools/verify_batch.py", 5, "415–419")
    old += archived_python_anchors(
        "papers/425-divisor-remainder-companion/tools/verify_batch.py", 5, "420–424")
    old += archived_python_anchors(
        "papers/430-euclidean-complex-degree/tools/verify_batch.py", 5, "425–429")
    old += archived_python_anchors(
        "papers/435-content-remainder-newton/tools/verify_batch.py", 5, "430–434")
    old += archived_python_anchors(
        "papers/440-double-remainder-fraction/tools/verify_batch.py", 5, "435–439")
    old += archived_python_anchors(
        "papers/445-radial-admission-exit/tools/verify_batch.py", 5, "440–444")
    old += archived_python_anchors(
        "papers/450-divisor-additive-quotient/tools/verify_batch.py", 5, "445–449")
    old += archived_python_anchors(
        "papers/455-divisor-continued-quotient/tools/verify_batch.py", 5, "450–454")
    old += archived_python_anchors(
        "papers/460-gcd-recurrent-feedback/tools/verify_batch.py", 5, "455–459")
    old += archived_python_anchors(
        "papers/465-gcd-hyperbolic-exchange/tools/verify_batch.py", 5, "460–464")
    old += archived_python_anchors(
        "papers/470-gcd-memory-register/tools/verify_batch.py", 5, "465–469")
    old += archived_python_anchors(
        "papers/475-proper-divisor-tail-admission/tools/verify_batch.py", 5, "470–474")
    old += archived_python_anchors(
        "papers/480-cf-prefix-period-multipliers/tools/verify_batch.py", 5, "475–479")
    # Accept either the exact full slug in this log or the earlier numeric format.
    parsed_opening = re.findall(
        r"^\|\s*(48[0-4](?:-[a-z0-9-]+)?)\s*\|\s*(\d+)\s*\|\s*`?([a-f0-9]{64})`?\s*\|$",
        batch_log, re.M)
    opening_rows = unique_rows(
        [(label[:3], label, count, digest) for label, count, digest in parsed_opening],
        "opening bundle receipt")
    for directory, count, digest in OPENING:
        row = opening_rows.get(directory[:3])
        if pre and row is None:
            pending.add("Opening bundle receipt pending: " + directory)
        else:
            require(row is not None and row[0] in (directory[:3], directory)
                    and int(row[1]) == count and row[2] == digest,
                    "Opening receipt changed or missing: " + directory)
    old += OPENING
    require(len(old) == 137 and len({row[0] for row in old}) == 137,
            "Unique old348–484 packages required")
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
        r"^\| (48[5-9]) \| `outcome: ([^`\n]+)` \|$", batch_log, re.M | re.I),
        "final outcome receipt")
    outcomes = {number: normalize_outcome(row[0]) for number, row in outcome_rows.items()}
    counts = dict(packages=5, identitySurfaces=0, statusSurfaces=0, markdown=0,
                  relativeLinks=0, frozenPrefixes=0, preservedPackages=len(old),
                  preservedAnchors=len(ANCHORS), preservedOverviewArchives=0,
                  boundEvidenceReceipts=0, boundSurfaceReceipts=0)
    inputs = []

    # Ownership metadata only: references in the scientific body are not ID collisions.
    expected_cards = {candidate_id: Path("papers") / directory / "candidate-card.md"
                      for directory, candidate_id, _ in PACKAGES}
    require(len(expected_cards) == 5, "Five unique new candidate IDs required")
    declarations = {candidate_id: set() for candidate_id in expected_cards}
    id_pattern = re.compile(
        r"^[ \t]*(?:>[ \t]*)?(?:[-*+][ \t]+)?(?:\*\*)?(?:Candidate[ \t]+ID|ID)"
        r"[ \t]*(?:\*\*)?[ \t]*:[ \t]*(?:\*\*)?[ \t]*`?([A-Z][A-Z0-9-]+)",
        re.I)
    for card_file in sorted(Path("papers").glob("*/candidate-card.md")):
        for line in read(card_file).split("\n")[:20]:
            match = id_pattern.match(line)
            if match and match[1] in declarations:
                declarations[match[1]].add(card_file)
    for candidate_id, expected in expected_cards.items():
        require(declarations[candidate_id] == {expected},
                "Candidate ID declaration collision or missing: " + candidate_id)
    counts["candidateIDCollisionChecks"] = len(expected_cards)

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
        r"^\| (48[5-9]) \| `([a-f0-9]{64})` \| `([a-f0-9]{64})` \| `([a-f0-9]{64})` \|$",
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
        review = read(base / "evidence/review.md")
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
        require(HANDOFF_DATE in current and "5/5" in current,
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
                and counts["preservedOverviewArchives"] == 2
                and counts["candidateIDCollisionChecks"] == 5 and not pending,
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
