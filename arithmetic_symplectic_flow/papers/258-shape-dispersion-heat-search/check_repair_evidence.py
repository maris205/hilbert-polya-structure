"""Read-only integration checks; no scientific imports, executions or writes."""
import ast
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
SCOPE = "ASFS-DISCOVERY-20260919-CS08"
STATUS = "FIXED REPAIR COMPLETE; FINE-320 STABILITY MET; STATIC NEAR-IDENTICAL"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def anchors(path):
    found = set()
    counts = {}
    fenced = False
    for line in path.read_text().splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        if not fenced and re.match(r"^#{1,6} ", line):
            heading = re.sub(r"^#{1,6}\s+", "", line).strip()
            heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
            slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
            count = counts.get(slug, 0)
            counts[slug] = count + 1
            found.add(slug if count == 0 else f"{slug}-{count}")
    return found


markdown = sorted(PACKAGE.rglob("*.md")) + [ROOT / "readme.md", ROOT / "papers/README.md"]
link_count = 0
for path in markdown:
    content = path.read_text()
    check(not any(line.endswith((" \t", "\t ")) for line in content.splitlines()), f"mixed trailing whitespace: {path}")
    for match in re.finditer(r"!?\[[^]\n]*\]\(([^)\n]+)\)", content):
        target = match.group(1).strip().strip("<>")
        parts = urlsplit(target)
        if parts.scheme or target.startswith("//"):
            continue
        link_count += 1
        linked = (path.parent / unquote(parts.path)).resolve() if parts.path else path
        check(linked.exists(), f"missing link: {path.name}: {target}")
        if linked.exists() and parts.fragment:
            fragment = unquote(parts.fragment)
            if re.fullmatch(r"L\d+", fragment):
                check(int(fragment[1:]) <= len(linked.read_text().splitlines()), f"line anchor: {target}")
            elif linked.suffix.lower() == ".md":
                check(fragment in anchors(linked), f"heading anchor: {target}")

for name in ["paper.md", "README.md", "claim-ledger.md", "evidence/README.md"]:
    content = (PACKAGE / name).read_text()
    check(SCOPE in content and STATUS in content, f"scope/status: {name}")
for path in [ROOT / "readme.md", ROOT / "papers/README.md"]:
    check(STATUS in path.read_text() and SCOPE in path.read_text(), f"root scope/status: {path}")
for name in ["candidate-card.md", "execution-card.md", "repair-execution-card.md"]:
    check(SCOPE in (PACKAGE / name).read_text(), f"frozen card scope: {name}")

lock_counts = {}
for name in ["input-locks.json", "repair-input-locks.json"]:
    locks = read_json(PACKAGE / name)
    if "inputs" in locks:
        locks = locks["inputs"]
    for relative, expected in locks.items():
        check(digest(ROOT / relative) == expected, f"input hash: {relative}")
    lock_counts[name] = len(locks)

inventory_counts = {}
for dirname, inventory_path in [
    ("run-1", PACKAGE / "evidence/failed-run-inventory.json"),
    ("run-2-fixed", PACKAGE / "evidence/run-2-fixed/file-inventory.json"),
]:
    base = PACKAGE / "evidence" / dirname
    listing = read_json(inventory_path)["files"]
    actual = {str(p.relative_to(base)) for p in base.rglob("*") if p.is_file()}
    expected_members = set(listing)
    if dirname == "run-2-fixed":
        expected_members.add("file-inventory.json")
    check(actual == expected_members, f"inventory membership: {dirname}")
    for relative, item in listing.items():
        path = base / relative
        check(path.stat().st_size == item["bytes"] and digest(path) == item["sha256"], f"inventory item: {dirname}/{relative}")
    inventory_counts[dirname] = len(actual)

for name, expected in {
    "run_search.py": "4c8a52f7b5f57519d09ef241e0a3c7e7633f35848b957857d1fc10bee05db763",
    "resume_fixed.py": "94e8f9a0a6435ad86f8bbe159782cd0a5fe6763e985f33c4da64e59154c8c1ce",
}.items():
    ast.parse((PACKAGE / name).read_text())
    check(digest(PACKAGE / name) == expected, f"runner hash: {name}")

receipt = read_json(PACKAGE / "evidence/repair-launch-receipt.json")
check(receipt["actual_process_exit_code"] == 0, "launcher exit")
result = read_json(PACKAGE / "evidence/run-2-fixed/result.json")
check(result["status"] == "completed" and result["global_joint_winner"] == "Q", "result status/primary")
for field in ["propagations", "full_svd", "static_readouts"]:
    check(result["counters"][field + "_attempted"] == result["counters"][field + "_completed"] == 22, field)
check(result["counters"]["optimization_calls"] == 0, "no optimization")
print(json.dumps({
    "scope_id": SCOPE,
    "result_state": STATUS,
    "checked_markdown_files": len(markdown),
    "checked_local_links_and_anchors": link_count,
    "locked_inputs": lock_counts,
    "inventory_members": inventory_counts,
    "runner_hashes_unchanged": True if not errors else "see errors",
    "contract_state": "Original frozen cards preserved; current status carried by result documents",
    "scientific_computations_performed": False,
    "errors": errors,
    "command": "PYTHONDONTWRITEBYTECODE=1 python papers/258-shape-dispersion-heat-search/check_repair_evidence.py",
}, indent=2))
raise SystemExit(bool(errors))
