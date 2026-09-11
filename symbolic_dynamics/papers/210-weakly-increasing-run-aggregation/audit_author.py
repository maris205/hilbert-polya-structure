#!/usr/bin/env python3
"""P210 final author documentary audit. Does not execute mathematical verifier/TeX."""
import ast
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys
import traceback

PAPER = Path(__file__).resolve().parent
CHECKS = 0
CURRENT = {}


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def sha(path):
    path = Path(path)
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as stream:
        return json.load(stream)


def write(path, data):
    with path.open("x") as stream:
        json.dump(data, stream, indent=2, sort_keys=True)
        stream.write("\n")


def validate_pin(path, expected):
    path = Path(path)
    check(path.is_file(), "missing pinned file: " + str(path))
    if str(path) not in CURRENT:
        CURRENT[str(path)] = sha(path)
    check(CURRENT[str(path)] == expected["sha256"], "current digest: " + str(path))
    check(path.stat().st_size == expected["size"], "current size: " + str(path))
    check(str(path.resolve()) == expected["real"], "resolved target: " + str(path))
    actual_link = path.readlink().as_posix() if path.is_symlink() else None
    check(actual_link == expected["symlink"], "symlink target: " + str(path))


def run(attempt):
    required = ["main.tex", "math_commands.tex", "references.bib", "main.pdf", "verify.py", "CANONICAL.json",
                "PROOF_PACKAGE.md", "PAPER_PLAN.md", "NARRATIVE_REPORT.md", "CLAIMS_EVIDENCE.md",
                "SOURCE_AUDIT.md", "README.md", "PARAMETERS.json", "AUTHOR_REPLAY.md", "AUTHOR_BUILD.md",
                "AUTHOR_VIEW.actual.json", "AUTHOR_VIEW_DRAFT02.actual.json", "AUTHOR_SOURCE_READ.md",
                "AUTHOR_REVISION_LOG.md"]
    for name in required:
        check((PAPER / name).is_file(), "required file " + name)
    check(not list(PAPER.glob("frozen_round*")), "author must not freeze a round")
    syntax = ast.parse((PAPER / "verify.py").read_text())
    imports = sorted({node.module.split(".")[0] for node in ast.walk(syntax) if isinstance(node, ast.ImportFrom)} |
                     {a.name.split(".")[0] for node in ast.walk(syntax) if isinstance(node, ast.Import) for a in node.names})
    check(imports == ["collections", "functools", "json"], "standalone stdlib-only verifier")
    check(any(isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "MAX_N" for t in node.targets)
              and isinstance(node.value, ast.Constant) and node.value.value == 12 for node in syntax.body), "original fixed box")
    main = (PAPER / "main.tex").read_text()
    included = re.findall(r"\\input\{([^}]+)\}", main)
    expected_sections = {str(p.relative_to(PAPER).with_suffix("")) for p in (PAPER / "sections").glob("*.tex")}
    check(set(included) == expected_sections | {"math_commands"}, "all and only modular source inputs")
    tex = main + "\n" + "\n".join((PAPER / (path + ".tex")).read_text() for path in included)
    labels = re.findall(r"\\label\{([^}]+)\}", tex)
    refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", tex)
    check(len(labels) == len(set(labels)) and set(refs) <= set(labels), "reference closure")
    cites = {key.strip() for group in re.findall(r"\\cite[pt]?\{([^}]+)\}", tex) for key in group.split(",")}
    bib = (PAPER / "references.bib").read_text()
    keys = re.findall(r"@\w+\{([^,]+),", bib)
    check(len(keys) == len(set(keys)) == 7 and set(keys) == cites, "seven verified cited-only bibliography keys")
    check(not any(marker in tex for marker in ("TODO", "FIXME", "[VERIFY]", "XXX")), "no draft markers")
    check("\\author{Anonymous}" in main and "pdfauthor={}" in main, "anonymous sources")
    canonical_bytes = (PAPER / "CANONICAL.json").read_bytes()
    canonical = json.loads(canonical_bytes)
    check(canonical["checks"] == 197471 and canonical["mass_box"] == [1, 12], "actual canonical checks/box")
    check(canonical["totals"] == dict(states=4095, edges=4095, targets=4095,
          image_objects=265, triangular_objects=265, surplus_witnesses=28), "complete canonical census")
    for mass in canonical["masses"]:
        n = mass["N"]
        states = {tuple(row["state"]): row for row in mass["states"]}
        target_rows = {tuple(row["target"]): row for row in mass["targets"]}
        check(len(states) == len(target_rows) == 2 ** (n - 1), "all state/target rows")
        check(states.keys() == target_rows.keys(), "identical complete carriers")
        from_edges = {target: [] for target in target_rows}
        for source, row in states.items():
            from_edges[tuple(row["edge"])].append(list(source))
            check(row["orbit"][0] == row["state"] and row["orbit"][-1] == row["fixed_endpoint"], "stored full orbit endpoints")
            check(len(row["orbit"]) == row["depth"] + 1 == len(row["birth_rounds"]) + 1, "full stored time rows")
        for target, row in target_rows.items():
            check(sorted(row["sources"]) == sorted(from_edges[target]), "explicit fibre matches all stored edges")
            check(row["fibre"] == len(row["sources"]) and row["image"] == bool(row["sources"]), "stored fibre/image census")
            check(len(row["suffixes"]) == len(target), "complete suffix rows")
    history = []
    package_rows = []
    for name in ("author_produce_01", "author_pair_01", "author_pair_02", "draft_build_01", "draft_build_02"):
        root = PAPER / name
        report = read(root / "REPORT.json")
        check(report["status"] == "PASS" and report["checks_passed"] and not report["changed_inputs"], "recorded package PASS " + name)
        check(all(code == 0 for _, code in report["native_commands"]), "all actual native package exits")
        suffix = ".json.gz" if name.startswith("draft") else ".json"
        before = read(root / ("INPUTS_BEFORE" + suffix))
        after = read(root / ("INPUTS_AFTER" + suffix))
        check(before == after and len(after) == report["input_count"], "exact original before/after inventory " + name)
        for spelling, pin in before.items():
            path = Path(spelling)
            if name in {"author_produce_01", "author_pair_01", "draft_build_01"} and path.is_relative_to(PAPER):
                relative = path.relative_to(PAPER)
                copy = root / "source" / relative
                if relative in {Path("PROOF_PACKAGE.md"), Path("sections/0_abstract.tex"),
                                Path("sections/1_introduction.tex"), Path("sections/2_clock.tex")} and copy.is_file() and sha(path) != pin["sha256"]:
                    check(sha(copy) == pin["sha256"] and copy.stat().st_size == pin["size"], "exact historical source role")
                    history.append(dict(package=name, original_key=spelling, snapshot=str(copy.relative_to(PAPER)),
                                        old_sha256=pin["sha256"], current_sha256=sha(path),
                                        reason="documented author integer-domain clarification"))
                    continue
            validate_pin(path, pin)
        payloads = read(root / "PAYLOADS.json")
        physical = {str(path) for path in root.rglob("*") if path.is_file() and path != root / "PAYLOADS.json"}
        check(set(payloads) == physical, "complete package nonself payload inventory " + name)
        for path, pin in payloads.items():
            validate_pin(path, pin)
        for command, code in report["native_commands"]:
            directory = root / "commands" / command
            result = read(directory / "RESULT.json")
            check(result["native_returncode"] == code, "native exit record")
            check(sha(directory / "stdout") == result["stdout_sha256"] and sha(directory / "stderr") == result["stderr_sha256"], "raw stream pins")
        if name.startswith("author"):
            check(not report["unpinned_observed_files"] and not report["forbidden_import_inputs"], "runtime observation closure")
            for output in report["raw_outputs"]:
                check(Path(output).read_bytes() == canonical_bytes, "full raw canonical equality " + output)
            check(all(report["cache_remained_absent"]), "cache absence")
        else:
            check(report["pages"] == report["rendered_pages"] == 6, "six actual pages")
            check(not report["warnings"] and not report["unpinned_fls_inputs"] and not report["unresolved_text_markers"], "build/ref/recorder checks")
            for row in read(root / "FLS_CLOSURE.json"):
                check(row["role"] != "unresolved", "every actual recorder input classified")
        package_rows.append(dict(package=name, inputs=len(before), payloads=len(payloads),
                                 report_sha256=sha(root / "REPORT.json"), inventory_sha256=sha(root / "PAYLOADS.json")))
    check(len(history) == 5, "exactly five historical live-to-snapshot key roles")
    write(PAPER / "HISTORICAL_INPUT_ROLES.actual.json", history)
    archive = read(PAPER / "sources/ARCHIVE_INPUTS.actual.json")
    check(archive["count"] == len(archive["records"]) == 19, "nineteen exact archive inputs")
    for row in archive["records"]:
        check(sha(Path(row["original"])) == sha(PAPER / row["copy"]) == row["sha256"], "exact archival primary input")
    for view_name in ("AUTHOR_VIEW.actual.json", "AUTHOR_VIEW_DRAFT02.actual.json"):
        view = read(PAPER / view_name)
        check(view["status"] == "AUTHOR_VISUAL_PASS" and len(view["pages"]) == view["page_count"] == 6, "six explicit author views")
        check(sha(PAPER / view["pdf"]) == view["pdf_sha256"], "view PDF binding")
        for row in view["pages"]:
            check(row["viewed"] and sha(PAPER / row["path"]) == row["sha256"], "actual page receipt/hash binding")
    check((PAPER / "main.pdf").read_bytes() == (PAPER / "draft_build_02/source/main.pdf").read_bytes(), "selected live PDF exact copy")
    for directory in (PAPER / "execution").iterdir():
        if directory.name.startswith("audit"):
            continue  # This enclosing collector has not returned yet; it is sealed after return.
        result = read(directory / "RESULT.json")
        check(result["native_exit"] == 0 and result["inputs_unchanged"], "captured parent native completion")
        check(sha(directory / "stdout") == result["stdout_sha256"] and sha(directory / "stderr") == result["stderr_sha256"], "parent full streams")
    # Relative links in flattened archival originals retain their explicit original origins.
    links = []
    owned = list(PAPER.glob("*.md")) + list((PAPER / "evidence_tools").glob("*.md"))
    for document in owned:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text()):
            if target.startswith(("https://", "http://", "#")):
                continue
            destination = (document.parent / target.split("#", 1)[0]).resolve()
            check(destination.exists(), "authored link closure " + str(document) + " -> " + target)
            links.append(dict(origin=str(document.relative_to(PAPER)), target=target))
    changed = [path for path, old in CURRENT.items() if sha(Path(path)) != old]
    check(not changed, "all actually pinned current audit files unchanged on second read")
    report = dict(status="PASS_AUTHOR_DOCUMENTARY_ONLY", checks=CHECKS, science_executions=0, tex_builds=0,
                  independent_reviews=0, current_paths_rechecked=len(CURRENT), changed_current_inputs=changed,
                  package_records=package_rows, historical_role_count=len(history), authored_links=links,
                  verifier_sha256=sha(PAPER / "verify.py"), canonical_sha256=sha(PAPER / "CANONICAL.json"),
                  selected_pdf_sha256=sha(PAPER / "main.pdf"),
                  pending="Root reception/replay/view, physical Round0, two nonauthor manuscript reviews, later freezes, terminal builds/views and full five-paper gate",
                  limit="Complete documentary checks of native originals and current pins, not a new science execution or independent review")
    write(PAPER / "AUTHOR_AUDIT.actual.json", report)
    write(attempt / "RESULT.json", dict(status=report["status"], checks=CHECKS,
          receipt_sha256=sha(PAPER / "AUTHOR_AUDIT.actual.json")))
    print(json.dumps(dict(status=report["status"], checks=CHECKS, current_paths_rechecked=len(CURRENT)), sort_keys=True))


if __name__ == "__main__":
    tag = sys.argv[1]
    if not re.fullmatch(r"[0-9]{2}", tag):
        raise ValueError("two-digit fresh attempt required")
    attempt = PAPER / ("author_audit_" + tag)
    attempt.mkdir(exist_ok=False)
    (attempt / "audit_author.py").write_bytes(Path(__file__).read_bytes())
    try:
        run(attempt)
    except BaseException as error:
        write(attempt / "FAILURE.json", dict(checks_before_failure=CHECKS, error=repr(error), traceback=traceback.format_exc()))
        raise
