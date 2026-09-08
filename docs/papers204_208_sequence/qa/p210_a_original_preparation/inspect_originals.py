#!/usr/bin/env python3
"""Read-only exact initial P210 manuscript A original-evidence inspector.

Prepared by /root/p210_a_original_desk, not a manuscript review. This program
never imports or executes original checkers, recorders, builds, or audits.
It validates recorded bytes, full canonical-data comparisons, and exact roles.
Root must read then run it separately; preparation is not actual acceptance.
"""
import ast
import collections
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[3]
PAPER = WORKSPACE / "docs/papers204_208_sequence/reviews/p210_a"
FROZEN = WORKSPACE / "papers/210-weakly-increasing-run-aggregation/frozen_round0"
INITIAL_SEAL = "e60d352a6520dd5f56b01035912ce753bb1a669c7368ce0a999ff56a72ff966d"
FREEZE_SEAL = "e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26"
AUTHOR_SEAL = "b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c"
PACKAGE_NAMES = ("produce01", "pair01", "pair02", "build01", "build02")
PAYLOAD_COUNTS = dict(produce01=23, pair01=41, pair02=41, build01=144, build02=144)
INPUT_COUNTS = dict(produce01=2629, pair01=2631, pair02=2631, build01=117808, build02=117808)
PARAMETERS = dict(mass_min=1, mass_max=12, carrier="cumulative-cut-bitmask",
                  update="synchronous-old-weak-increasing-run-sums")
BOUNDARY = "Review A artifact instrumentation adapted from frozen author helper after full reading; NOT scientific checker reuse, OS/startup trace, or visual review."
SOURCES = ("main.tex", "math_commands.tex", "references.bib", "sections/0_abstract.tex",
           "sections/1_introduction.tex", "sections/2_clock.tex", "sections/3_image.tex",
           "sections/4_coding.tex", "sections/5_fibres.tex", "sections/6_scope.tex")
CURRENT = {}
CHECKS = 0
NATIVE = []
RAW_COMPARISONS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def fresh_pin(path):
    path = Path(path)
    require(path.is_file(), "missing current input: " + str(path))
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return dict(sha256=digest.hexdigest(), size=path.stat().st_size,
                real=str(path.resolve()), symlink=str(path.readlink()) if path.is_symlink() else None)


def memo(path):
    key = str(Path(path))
    if key not in CURRENT:
        CURRENT[key] = fresh_pin(key)
    return CURRENT[key]


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    pin = memo(path)
    require(hashlib.sha256(data).hexdigest() == pin["sha256"] and len(data) == pin["size"],
            "raw read changed within inspection: " + str(path))
    return data


def document(path):
    data = raw(path)
    return json.loads(gzip.decompress(data) if str(path).endswith(".gz") else data)


def text(path):
    return raw(path).decode("utf-8", errors="strict")


def pin(path, expected):
    require(set(expected) == {"real", "sha256", "size", "symlink"}, "complete pin schema: " + str(path))
    require(memo(path) == expected, "exact current path/hash/size/target: " + str(path))


def physical(root, excluding=()):
    return {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() and str(p.relative_to(root)) not in excluding}


def manifest(root, name, expected_count, complete=True):
    rows = {}
    for line in text(root / name).splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, "strict manifest row")
        digest, relative = match.groups()
        require(relative not in rows and not Path(relative).is_absolute() and ".." not in Path(relative).parts,
                "unique contained manifest path")
        rows[relative] = digest
        require(memo(root / relative)["sha256"] == digest, "manifest digest: " + relative)
    require(len(rows) == expected_count, "exact manifest count")
    if complete:
        require(set(rows) == physical(root, (name,)), "complete nonself physical inventory")
    return rows


def isolated(flags):
    require(re.search(r"(?:\(|, )optimize=0(?:,|\))", flags) is not None, "unoptimized original interpreter")
    for name in ("dont_write_bytecode", "no_user_site", "no_site", "ignore_environment", "isolated"):
        require(re.search(r"(?:\(|, )" + name + r"=1(?:,|\))", flags) is not None, "isolated flag: " + name)


def expected_environment(root):
    return dict(PATH="/usr/bin:/bin", LANG="C", LC_ALL="C", TZ="UTC",
                HOME=str(root / "empty_home"), TMPDIR=str(root / "tmp"),
                SOURCE_DATE_EPOCH="1704067200", FORCE_SOURCE_DATE="1",
                openout_any="p", openin_any="p", shell_escape="f")


def equal_raw(left, right):
    global RAW_COMPARISONS
    require(raw(left) == raw(right), "complete raw-byte comparison: " + str(left) + " / " + str(right))
    RAW_COMPARISONS += 1


def native_result(directory):
    result = document(directory / "RESULT.json")
    stdout, stderr = raw(directory / "stdout"), raw(directory / "stderr")
    require(set(result) == {"native_returncode", "end_ns", "stdout_sha256", "stderr_sha256"},
            "exact original native result schema")
    require(result["native_returncode"] == 0 and isinstance(result["end_ns"], int), "actual native zero return")
    require(result["stdout_sha256"] == hashlib.sha256(stdout).hexdigest() and
            result["stderr_sha256"] == hashlib.sha256(stderr).hexdigest(), "entire actual native streams")
    return result, stdout, stderr


def native_record(directory, argv, env, cwd):
    attempt = document(directory / "ATTEMPT.json")
    result, stdout, stderr = native_result(directory)
    require(set(attempt) == {"argv", "cwd", "environment", "start_ns"}, "child attempt schema")
    require(attempt["argv"] == argv and attempt["cwd"] == str(cwd), "entire child argv/cwd")
    require(attempt["environment"] == env, "entire explicit clean child environment")
    require(isinstance(attempt["start_ns"], int) and result["end_ns"] >= attempt["start_ns"], "child native time ordering")
    NATIVE.append(dict(record=str(directory.relative_to(PAPER)), argv=argv, stdout_bytes=len(stdout),
                       stderr_bytes=len(stderr), native_exit=0, role="original_child"))
    return stdout, stderr


def child_commands(root, mode):
    source = root / "source"
    executables = (["cmp", "python3.10"] if mode != "build" else
                   sorted(["pdflatex", "bibtex", "kpsewhich", "pdfinfo", "pdffonts", "pdftotext", "pdftoppm", "python3.10"]))
    commands = {"ldd_%02d" % i: ["/usr/bin/ldd", "/usr/bin/" + name] for i, name in enumerate(executables)}
    if mode == "build":
        for name in ("texmf.cnf", "pdflatex.fmt", "pdftex.map", "fmtutil.cnf", "updmap.cfg"):
            commands["kpse_" + name.replace(".", "_")] = ["/usr/bin/kpsewhich", "-engine=pdftex", "-progname=pdflatex", "-all", name]
        engine = ["/usr/bin/pdflatex", "-recorder", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]
        for i, argv in enumerate((engine, ["/usr/bin/bibtex", "main"], engine, engine), 1):
            commands["pass_%d" % i] = argv
        commands.update(pdfinfo=["/usr/bin/pdfinfo", "main.pdf"], pdffonts=["/usr/bin/pdffonts", "main.pdf"],
                        pdftotext=["/usr/bin/pdftotext", "-layout", "main.pdf", "-"],
                        render=["/usr/bin/pdftoppm", "-png", "-r", "110", "main.pdf", str(root / "page")])
    else:
        for i in range(1, 3 if mode == "pair" else 2):
            commands["run_%d" % i] = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X",
                "pycache_prefix=" + str(root / ("absent_pyc_%d" % i)), str(root / "tools/runtime_probe.py"),
                str(source / "verify.py"), str(root / ("runtime_%d.json" % i))]
        if mode == "pair":
            a, b, c = str(root / "commands/run_1/stdout"), str(root / "commands/run_2/stdout"), str(source / "CANONICAL.json")
            commands.update(cmp_pair=["/usr/bin/cmp", a, b], cmp_1_canonical=["/usr/bin/cmp", a, c], cmp_2_canonical=["/usr/bin/cmp", b, c])
    return commands


def map_paths(body):
    return [line.split(None, 5)[5] for line in body.splitlines()
            if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith("/")]


def runtime(root, number, before, env):
    record = document(root / ("runtime_%d.json" % number))
    require(set(record) == {"scope", "settings", "read_attempts", "imports", "modules", "maps_before", "maps_after", "existing_reads"}, "complete bounded runtime record")
    require("NOT OS/startup tracing" in record["scope"], "runtime coverage limitation retained")
    settings = record["settings"]
    require(set(settings) == {"environment", "executable", "flags", "path", "version", "xoptions"}, "complete runtime settings")
    require(settings["environment"] == env and settings["executable"] == "/usr/bin/python3.10", "observed runtime env/interpreter")
    isolated(settings["flags"])
    require(settings["path"] == ["/usr/lib/python310.zip", "/usr/lib/python3.10", "/usr/lib/python3.10/lib-dynload"], "isolated runtime search path")
    cache = root / ("absent_pyc_%d" % number)
    require(settings["xoptions"] == {"pycache_prefix": str(cache)} and not cache.exists(), "exact observed absent source-only cache")
    require(record["imports"] == sorted(set(record["imports"])) and all(isinstance(v, str) for v in record["imports"]), "complete import-event list")
    attempts = record["read_attempts"]
    require(attempts == sorted(set(attempts)), "entire unique read-attempt list")
    existing = sorted(p for p in attempts if Path(p).is_file() and not p.startswith("/proc/"))
    require(record["existing_reads"] == existing, "actual existing versus failed read attempts")
    observed = set(existing + map_paths(record["maps_before"]) + map_paths(record["maps_after"]) +
                   [p for p in record["modules"].values() if p])
    known = {v["real"] for v in before.values()}
    for spelling in observed:
        path = Path(spelling)
        require(path.is_file() and str(path.resolve()) in known, "all observed existing source/library/module files pinned")
        require(path.suffix not in {".pyc", ".pyo"} and not {"site-packages", "dist-packages"}.intersection(path.parts), "no consumed forbidden cache/site file")
        memo(path)
    require(str(root / "source/verify.py") in existing, "literal copied verifier was observed")
    require({str(Path(p).relative_to(root / "source")) for p in existing
             if Path(p).is_relative_to(root / "source")} == {"verify.py", "PARAMETERS.json"},
            "only independent scientific program and declared PARAMETERS actually read from source capsule")
    return dict(existing_reads=len(existing), read_attempts=len(attempts), import_events=len(record["imports"]),
                observed_file_spellings=len(observed), missing_search_path=[p for p in settings["path"] if not Path(p).exists()])


def build_records(root, before, report):
    source = root / "source"
    known = {v["real"]: v for v in before.values()}
    previous, closure = None, []
    for number in range(1, 5):
        command = root / ("commands/pass_%d" % number)
        prior = document(command / "SOURCE_BEFORE.json")
        after = document(command / "SOURCE_AFTER.json")
        if number == 1:
            require(set(prior) == {str(source / s) for s in SOURCES}, "exact ten-source cold start, no products")
        else:
            require(prior == previous, "complete original successive-pass product ledger")
        for ledger in (prior, after):
            for spelling, value in ledger.items():
                require(Path(spelling).is_relative_to(source) and value["real"] == spelling and value["symlink"] is None,
                        "recorded source/product role stays within build capsule")
                require(set(value) == {"real", "sha256", "size", "symlink"} and re.fullmatch(r"[0-9a-f]{64}", value["sha256"]), "full product pin schema")
        for relative in SOURCES:
            require(prior[str(source / relative)] == after[str(source / relative)] == before[str(source / relative)], "all ten scientific source roles unchanged in each pass")
        for suffix in ("log", "fls", "aux", "bbl", "blg", "out", "toc"):
            original = str(source / ("main." + suffix))
            saved = command / ("main." + suffix)
            if original in after:
                require(saved.is_file() and memo(saved)["sha256"] == after[original]["sha256"] and
                        memo(saved)["size"] == after[original]["size"], "physical preserved pass product")
            else:
                require(not saved.exists(), "no invented pass product")
        if number != 2:
            generated = set()
            for line in text(command / "main.fls").splitlines():
                if not line.startswith(("INPUT ", "OUTPUT ")):
                    continue
                kind, spelling = line.split(" ", 1)
                path = Path(spelling)
                actual = str((path if path.is_absolute() else source / path).resolve())
                if kind == "OUTPUT":
                    generated.add(actual)
                    continue
                role = ("pinned_external" if actual in known else "prior_product" if actual in prior else
                        "same_pass_recorded_output" if actual in generated else "unresolved")
                require(role != "unresolved", "reconstructed complete recorder input role")
                value = known[actual] if actual in known else after.get(actual)
                require(value is not None, "recorder end-of-pass digest available")
                closure.append(dict(pass_number=number, path=actual, role=role, final_sha256=value["sha256"]))
        previous = after
    require(document(root / "FLS_CLOSURE.json") == closure, "entire actual ordered FLS closure, including duplicates")
    require(set(previous) == {str(source / r) for r in physical(source)}, "complete final source/product inventory")
    for spelling, value in previous.items():
        pin(spelling, value)
    require(memo(source / "main.pdf")["sha256"] == report["pdf_sha256"], "final actual PDF binding")
    log = text(source / "main.log")
    require(not re.search(r"undefined|multiply defined|Rerun to|Label\(s\) may have changed|Overfull|Underfull", log), "full final engine log clear")
    require("Output written on main.pdf (6 pages" in log, "actual six-page engine output")
    require(not re.search(r"Warning--|error message", text(source / "main.blg"), re.I), "full bibliography log clear")
    extracted = text(root / "commands/pdftotext/stdout")
    require(not any(v in extracted for v in ("??", "[?]", "[VERIFY]")), "complete extracted final text marker check")
    font_text = text(root / "commands/pdffonts/stdout")
    fonts = re.findall(r"\s+(yes|no)\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$", font_text, re.M)
    require(fonts == report["fonts_embedded"] and len(fonts) == 20 and all(v == "yes" for v in fonts), "every actual embedded final font")
    info = text(root / "commands/pdfinfo/stdout")
    require(re.search(r"^Pages:\s+6$", info, re.M) and re.search(r"^Author:[ \t]*$", info, re.M), "actual PDF pages and anonymous metadata")
    require(int(re.search(r"^File size:\s+(\d+) bytes$", info, re.M)[1]) == memo(source / "main.pdf")["size"], "actual PDF size metadata")
    require(report["pages"] == report["rendered_pages"] == 6 and len(list(root.glob("page-*.png"))) == 6, "all six rendered artifacts, not new views")
    for name in ("texmf.cnf", "pdflatex.fmt", "pdftex.map", "fmtutil.cnf", "updmap.cfg"):
        for spelling in text(root / "commands" / ("kpse_" + name.replace(".", "_")) / "stdout").splitlines():
            require(str(Path(spelling).resolve()) in known, "every reported TeX configuration/resource result pinned")
    return dict(source_count=10, engine_passes=3, bibliography_passes=1, fls_input_rows=len(closure), fonts=len(fonts), pages=6)


def package(name, canonical):
    root = PAPER / name
    mode = "build" if name.startswith("build") else "produce" if name.startswith("produce") else "pair"
    report, context = document(root / "REPORT.json"), document(root / "CONTEXT.json")
    require(set(context) == {"boundary", "argv", "environment", "interpreter", "version", "flags", "cwd", "platform"},
            "complete original context schema")
    require(report["status"] == "PASS" and report["checks_passed"] is True and report["changed_inputs"] == [] and
            report["driver_cache_remained_absent"] is True, "actual Review A child package status")
    require(report["mode"] == ("draft_build" if mode == "build" else mode), "exact package role")
    env = expected_environment(root)
    require(context["environment"] == env and context["interpreter"] == "/usr/bin/python3.10" and context["cwd"] == str(WORKSPACE), "entire original context environment/interpreter/cwd")
    isolated(context["flags"])
    origin = FROZEN if mode == "build" else PAPER
    driver = [str((PAPER / "instrumentation/evidence.py").relative_to(WORKSPACE)), mode,
              "--paper", str(origin.relative_to(WORKSPACE)), "--out", str(root.relative_to(WORKSPACE))]
    require(context["argv"] == driver and context["boundary"] == report["boundary"] == BOUNDARY, "full driver argv and bounded scope")
    if mode != "produce":
        require(not (PAPER / ("absent_driver_" + name)).exists(), "recorded dedicated driver cache still absent")
    suffix = ".json.gz" if mode == "build" else ".json"
    before, after = document(root / ("INPUTS_BEFORE" + suffix)), document(root / ("INPUTS_AFTER" + suffix))
    require(before == after and len(before) == report["input_count"] == INPUT_COUNTS[name], "entire original pre/post path keys and values")
    for ledger in (before, after):
        for spelling, value in ledger.items():
            pin(spelling, value)
    payloads = document(root / "PAYLOADS.json")
    require(len(payloads) == PAYLOAD_COUNTS[name], "exact original child payload count")
    require(set(payloads) == {str(root / relative) for relative in physical(root, ("PAYLOADS.json",))}, "original complete nonself package inventory")
    for spelling, value in payloads.items():
        pin(spelling, value)
    commands = child_commands(root, mode)
    require(report["native_commands"] == [[command, 0] for command in commands] and
            set(commands) == {p.name for p in (root / "commands").iterdir()}, "all and only actual native commands in original order")
    for command, argv in commands.items():
        stdout, stderr = native_record(root / "commands" / command, argv, env, root / "source")
        require(argv[0] in before, "native executable pinned")
        if command.startswith("ldd_"):
            known = {v["real"] for v in before.values()}
            for path in re.findall(r"(?:=>\s+|^\s*)(/[^\s]+)", stdout.decode(), re.M):
                require(str(Path(path).resolve()) in known, "entire recorded ldd resolution covered")
        if command.startswith("cmp_"):
            require(stdout == stderr == b"", "native cmp full empty streams")
            equal_raw(argv[1], argv[2])
    source_names = SOURCES if mode == "build" else ("verify.py", "PARAMETERS.json", "DESIGN_COMMITMENT.md", "COMMITMENT_PINS.sha256") + (("CANONICAL.json",) if mode == "pair" else ())
    for relative in source_names:
        copied = root / "source" / relative
        require(str(copied) in before and str(origin / relative) in before and
                before[str(copied)]["sha256"] == before[str(origin / relative)]["sha256"], "original source-only copy key equality")
        equal_raw(copied, origin / relative)
    if mode != "build":
        require(physical(root / "source") == set(source_names), "exact standalone scientific source capsule")
        require(document(root / "source/PARAMETERS.json") == PARAMETERS, "unchanged original parameter box")
    for name2 in ("evidence.py", "runtime_probe.py"):
        equal_raw(root / "tools" / name2, PAPER / "instrumentation" / name2)
    if mode == "build":
        require(report["warnings"] == report["unpinned_fls_inputs"] == report["unresolved_text_markers"] == [] and
                report["visual_inspection"] == "NOT_PERFORMED", "machine build versus manual viewing roles")
        details = build_records(root, before, report)
    else:
        runs = 2 if mode == "pair" else 1
        require(report["raw_outputs"] == [str(root / ("commands/run_%d/stdout" % n)) for n in range(1, runs + 1)] and
                report["cache_remained_absent"] == [True] * runs and report["unpinned_observed_files"] == report["forbidden_import_inputs"] == [], "complete scientific raw/runtime records")
        require(report["canonical_written"] is False and report["scientific_stdout_not_normalized"] is True, "raw canonical role")
        observations = []
        for n in range(1, runs + 1):
            require(raw(root / ("commands/run_%d/stdout" % n)) == canonical, "entire original scientific stdout equals canonical bytes")
            equal_raw(root / ("commands/run_%d/stdout" % n), PAPER / "CANONICAL.json")
            observations.append(runtime(root, n, before, env))
        details = dict(archived_science_runs=runs, runtime_observations=observations)
    return dict(package=root.name, original_inputs=len(before), original_payloads=len(payloads), native_commands=len(commands), **details)


SAFE_PARENT_FIELDS = {"PATH", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "LD_LIBRARY_PATH", "LIBRARY_PATH",
                      "OMP_NUM_THREADS", "MKL_NUM_THREADS", "PYTHONHASHSEED", "PYTHONPATH",
                      "PYTHONDONTWRITEBYTECODE", "PYTHONOPTIMIZE"}
OLD_TAGS = ("pair01", "build01", "compare_author01", "build_pdf_cmp")
EMPTY_SHA = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
AUDIT_STDOUT_SHA = "5438c5abf2b66c97b472fa7be09c26f3717a0d6c2ce98efa5808f878d877c7d3"


def safe_environment(attempt):
    # Inspect only the already-sanitized saved whitelist; never consult os.environ.
    environment = attempt["environment"]
    require(isinstance(environment, dict) and set(environment) <= SAFE_PARENT_FIELDS and
            all(isinstance(value, str) for value in environment.values()), "saved parent whitelist schema")
    omitted = attempt["omitted_launcher_environment_keys"]
    require(omitted == sorted(set(omitted)) and all(isinstance(key, str) for key in omitted) and
            not set(omitted) & set(environment), "omitted launcher names only, no values")
    require("AutodlAutoPanelToken" in omitted and "Sensitive platform fields" in attempt["environment_scope"],
            "explicit privacy omission and bounded parent scope")


def parent_argv(tag):
    relative = str(PAPER.relative_to(WORKSPACE))
    frozen = str(FROZEN.relative_to(WORKSPACE))
    if tag in {"build_pdf_cmp", "build_pdf_cmp02"}:
        build = "build01" if tag == "build_pdf_cmp" else "build02"
        return ["/usr/bin/cmp", relative + "/" + build + "/source/main.pdf", frozen + "/main.pdf"]
    if tag in {"pair01", "pair02", "build01", "build02"}:
        mode = "pair" if tag.startswith("pair") else "build"
        cache = "absent_driver_" + tag
        tail = [relative + "/instrumentation/evidence.py", mode, "--paper",
                relative if mode == "pair" else frozen, "--out", relative + "/" + tag]
    else:
        cache, script = {
            "compare_author01": ("absent_compare01", "compare_author.py"),
            "compare_author02": ("absent_compare02", "compare_author.py"),
            "restore_metadata01": ("absent_restore_metadata", "restore_launcher_metadata.py"),
            "finish_records01": ("absent_finish_records", "finish_records.py"),
            "audit01": ("absent_audit01", "audit_initial.py"),
            "audit_roles01": ("absent_inspect_roles01", "inspect_audit_roles.py"),
        }[tag]
        tail = [relative + "/" + script]
    return ["/usr/bin/python3.10", "-I", "-S", "-B", "-X", "pycache_prefix=" + str(PAPER / cache)] + tail


def parents():
    tags = set(OLD_TAGS) | {"pair02", "build02", "compare_author02", "build_pdf_cmp02",
                          "restore_metadata01", "finish_records01", "audit01", "audit_roles01"}
    require(tags == {p.name for p in (PAPER / "execution").iterdir()}, "all and only twelve recorded parents")
    outputs = {}
    for tag in sorted(tags):
        directory = PAPER / "execution" / tag
        require(physical(directory) == {"ATTEMPT.json", "RESULT.json", "stdout", "stderr"}, "complete parent quartet")
        attempt = document(directory / "ATTEMPT.json")
        result, stdout, stderr = native_result(directory)
        argv = parent_argv(tag)
        require(attempt["argv"] == argv and attempt["cwd"] == str(WORKSPACE), "exact complete parent argv/cwd: " + tag)
        require(stderr == b"", "entire successful parent stderr")
        if tag in OLD_TAGS:
            require(set(attempt) == {"role", "argv", "cwd", "native_returncode_evidence", "reconstruction_basis",
                    "original_start_ns", "start_time_scope", "environment_scope", "redacted_sensitive_key_names",
                    "all_unneeded_launcher_fields_omitted", "sanitizer_failure"}, "exact limited reconstructed metadata schema")
            require(attempt["role"] == "RECONSTRUCTED_KNOWN_LAUNCH_METADATA_AFTER_SANITIZER_FAILURE_NOT_ORIGINAL_RECEIPT" and
                    attempt["native_returncode_evidence"] == "RESULT.json" and
                    attempt["all_unneeded_launcher_fields_omitted"] is True, "old reconstructed parents are NOT original launch receipts")
            require(attempt["original_start_ns"] == (1788787619979700744 if tag == "pair01" else None),
                    "only first original start known; exactly three remain unavailable")
            require("not inferred" in attempt["start_time_scope"] and "emptied all four" in attempt["sanitizer_failure"],
                    "genuine historical failure and loss retained")
            require(attempt["redacted_sensitive_key_names"] == ["AutodlAutoPanelToken", "AutoDLServiceURL", "AutoDLService6006URL",
                    "AutoDLService6008URL", "http_proxy", "https_proxy"], "only names retained for the known redactions")
            role = "preserved_native_result_with_limited_reconstructed_launch_NOT_original"
        else:
            require(set(attempt) == {"argv", "cwd", "environment", "omitted_launcher_environment_keys", "environment_scope",
                    "start_ns", "scope"}, "fresh safe parent exact schema")
            require(attempt["scope"] == "A artifact launcher, not scientific code" and
                    isinstance(attempt["start_ns"], int) and result["end_ns"] >= attempt["start_ns"], "actual safe parent time ordering")
            safe_environment(attempt)
            role = "fresh_safe_parent_current_recorded_evidence"
            if tag in {"pair02", "build02"}:
                for command in (PAPER / tag / "commands").iterdir():
                    child = document(command / "ATTEMPT.json")
                    returned = document(command / "RESULT.json")
                    require(attempt["start_ns"] <= child["start_ns"] <= returned["end_ns"] <= result["end_ns"],
                            "selected parent really encloses each surviving child time")
        if argv[0] == "/usr/bin/python3.10":
            require(not Path(argv[5].split("=", 1)[1]).exists(), "exact recorded parent-child cache remained absent")
            memo(WORKSPACE / argv[6])
            outputs[tag] = json.loads(stdout)
        else:
            require(stdout == b"", "complete native PDF cmp stdout")
            equal_raw(WORKSPACE / argv[1], WORKSPACE / argv[2])
        if tag in {"pair01", "pair02", "build01", "build02"}:
            require(outputs[tag] == dict(status="PASS", output=str(PAPER / tag)), "parent stdout binds exact completed child package")
        NATIVE.append(dict(record=str(directory.relative_to(PAPER)), argv=argv, stdout_bytes=len(stdout),
                           stderr_bytes=len(stderr), native_exit=0, role=role))
    return outputs


def privacy_history(outputs):
    failure = document(PAPER / "history/SANITIZER_FAILURE.actual.json")
    require(failure["sanitizer_native_exit"] == 0 and failure["semantic_sanitizer_status"] == "FAIL_WRONG_IN_PLACE_LOOP" and
            failure["subsequent_wc_native_exit"] == 0 and failure["subsequent_json_reader_native_exit"] == 255,
            "retain true native0-but-failed sanitizer and native255 reader failure")
    require(failure["actual_zero_byte_files"] == ["execution/" + tag + "/ATTEMPT.json" for tag in OLD_TAGS] and
            failure["secret_bearing_original_receipts_retained"] is False and
            failure["original_launcher_source_prehash_available"] is False, "exact lost four unsealed files and no false source authentication")
    require("at character offset 0" in failure["subsequent_json_reader_stderr"], "actual empty-input reader diagnostic retained")
    safe = document(PAPER / "history/SANITIZER_FIRST_SAFE_STDOUT.actual.json")
    require(set(safe) == {"argv", "cwd", "environment", "environment_scope", "omitted_launcher_environment_keys", "scope", "start_ns"},
            "first actual safe stdout parsed-content transcription schema, not raw-whitespace preservation")
    safe_environment(safe)
    require(safe["argv"] == parent_argv("pair01") and safe["cwd"] == str(WORKSPACE) and
            safe["start_ns"] == 1788787619979700744, "first start anchored to surviving actual safe output")
    reconstruction = outputs["restore_metadata01"]
    require(reconstruction == dict(status="RECONSTRUCTED_LIMITED_NOT_ORIGINAL", records=[
        dict(path="execution/" + tag + "/ATTEMPT.json", sha256=memo(PAPER / "execution" / tag / "ATTEMPT.json")["sha256"])
        for tag in OLD_TAGS]), "actual restoration output binds only exact four limited reconstructions")
    source = text(PAPER / "history/record_source_reconstruction_unverified.py")
    parsed = ast.parse(source)
    require("UNVERIFIED RECONSTRUCTION" in ast.get_docstring(parsed) and "DO NOT EXECUTE" in ast.get_docstring(parsed) and
            "not\nauthenticated original evidence" in ast.get_docstring(parsed), "unverified source never authenticated or executed")
    current = ast.parse(text(PAPER / "record.py"))
    assignment = [node for node in current.body if isinstance(node, ast.Assign) and any(
        isinstance(target, ast.Name) and target.id == "safe" for target in node.targets)]
    require(len(assignment) == 1 and ast.literal_eval(assignment[0].value) == SAFE_PARENT_FIELDS,
            "current recorder literal whitelist, inspected AST only; no prehash invented")
    require("original source/pin is therefore unavailable" in text(PAPER / "SANITIZATION.md"), "honest authenticated old-source limitation")
    return dict(reconstructed_parent_records=4, unavailable_original_parent_starts=3,
                authenticated_original_launcher_source="UNAVAILABLE", old_source_reconstruction="UNVERIFIED_NOT_EXECUTED",
                first_safe_output_role="parsed-content transcription of actual safe stdout; not original whitespace bytes",
                selected_acceptance_parents=["pair02", "build02", "compare_author02", "build_pdf_cmp02"],
                historical_lost_bytes_recovered=False, secret_bearing_original_backup=False)


def reviewed_inputs():
    require(memo(FROZEN / "SHA256SUMS")["sha256"] == FREEZE_SEAL, "exact physical Round0 seal")
    frozen_rows = manifest(FROZEN, "SHA256SUMS", 493)
    require(memo(FROZEN / "AUTHOR_MANIFEST.sha256")["sha256"] == AUTHOR_SEAL, "original author seal physical alias")
    author_rows = manifest(FROZEN, "AUTHOR_MANIFEST.sha256", 489, complete=False)
    require(set(frozen_rows) == set(author_rows) | {"AUTHOR_MANIFEST.sha256", "ROOT_ADOPTION.md", "FREEZE_ADAPTER.py", "FROZEN_LINK_MAP.json"},
            "493 physical frozen payloads:489 immutable author roles plus exact four freeze additions")
    frozen_inputs = {}
    for line in text(PAPER / "INPUT_PINS.sha256").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, "strict root-relative reviewed input row")
        digest, relative = match.groups()
        require(relative not in frozen_inputs and not Path(relative).is_absolute() and ".." not in Path(relative).parts,
                "unique root-relative reviewed input")
        frozen_inputs[relative] = digest
        require(memo(WORKSPACE / relative)["sha256"] == digest, "all actual reviewed frozen bytes")
    require(len(frozen_inputs) == 494 and set(frozen_inputs) == {
        str((FROZEN / name).relative_to(WORKSPACE)) for name in set(frozen_rows) | {"SHA256SUMS"}},
            "all and only 494 reviewed freeze payloads+seal")
    commitments = manifest(PAPER, "COMMITMENT_PINS.sha256", 3, complete=False)
    require(commitments == {
        "DESIGN_COMMITMENT.md": "a7aadeafecde7c56c15158b0be265e38112c43add54bbe46591a816a7af56b1e",
        "verify.py": "4d152ceb7eebb8f1b4bf7632ad1a91f8be7e373520682022843fa6e81dd2de9b",
        "PARAMETERS.json": "854c270325ec270875863ed1110106ea397b1587f3da7f67876e4ce1d84e6de0"},
        "exact independent design/code/parameter commitment roles")
    require(document(PAPER / "PARAMETERS.json") == PARAMETERS, "original unchanged independent parameter data")
    intake = document(PAPER / "INTAKE.actual.json")
    require(intake == dict(status="PASS", frozen_payloads=493, input_pins=494, freeze_seal=FREEZE_SEAL,
        actual_command="/usr/bin/python3.10 -I -S -B docs/papers204_208_sequence/reviews/p210_a/intake.py", native_exit=0,
        record_role="transcribed actual intake stdout and tool native result; not future execution",
        semantic_author_checker_read_at_commitment=False), "original transcribed intake role; not manufactured native file receipt")
    mapping = document(FROZEN / "FROZEN_LINK_MAP.json")
    require(mapping["author_payloads"] == 489 and mapping["copied_input_count"] == 491 and
            mapping["historical_author_manifest_sha256"] == AUTHOR_SEAL and
            mapping["physical_author_manifest_alias"] == "AUTHOR_MANIFEST.sha256", "sealed frozen origin/alias roles")
    # Scope is reviewed physical freeze, not a second audit of the growing live author directory.
    equal_raw(PAPER / "instrumentation/runtime_probe.py", FROZEN / "evidence_tools/runtime_probe.py")
    checker = ast.parse(text(PAPER / "verify.py"))
    imported = {alias.name for node in ast.walk(checker) if isinstance(node, ast.Import) for alias in node.names}
    require(imported == {"json", "sys"} and not any(isinstance(node, ast.ImportFrom) for node in ast.walk(checker)),
            "independent scientific source imports only declared standard libraries, no author/helper code")
    require(memo(PAPER / "verify.py")["sha256"] != memo(FROZEN / "verify.py")["sha256"], "distinct scientific code; no assertion of blind mathematical vocabulary")
    return frozen_rows


def canonical_structure():
    data = document(PAPER / "CANONICAL.json")
    require(memo(PAPER / "CANONICAL.json")["sha256"] == "d96ed0240dec421d78cdbfb013869680c91685c1848ea2ee030a71f86ab7aa74" and
            memo(PAPER / "CANONICAL.json")["size"] == 703850, "entire independent original stdout identity")
    require(set(data) == {"schema", "parameters", "columns", "total_states", "checks", "tables"} and
            data["schema"] == "p210-review-a-cut-graph-v1" and data["parameters"] == PARAMETERS and
            data["total_states"] == 4095 and data["checks"] == 133978, "exact original scientific census, not recomputed proof")
    require(data["columns"] == dict(states=["mask", "next", "tau", "fixed", "events"],
        events=["round", "oldmask", "newmask", "deleted_cut_left_right_rightbirth", "newblocks"],
        targets=["mask", "parts", "sources", "attained_suffix_first_sets", "scan", "fibre_formula", "triangular_code"],
        triangular=["mask", "parts", "decoded_target", "decoded_mask"], witnesses=["h", "r", "parts", "orbit_masks"]),
        "full declared independent table columns")
    require([row["N"] for row in data["tables"]] == list(range(1, 13)), "entire original N1..12 table order")
    for table in data["tables"]:
        require(set(table) == {"N", "H", "image_count", "states", "targets", "triangular", "witnesses"}, "entire per-mass schema")
        size = 1 << (table["N"] - 1)
        for name, width in (("states", 5), ("targets", 7)):
            require([row[0] for row in table[name]] == list(range(size)) and all(len(row) == width for row in table[name]),
                    "all original masks, no missing or summary-only transcript row")
        require(all(len(event) == 5 for row in table["states"] for event in row[4]) and
                all(len(row) == 4 for name in ("triangular", "witnesses") for row in table[name]), "all nested event/triangular/witness columns")
    require(memo(FROZEN / "CANONICAL.json")["size"] == 6471668, "whole author transcript, no digest-only substitute")


def replay_keys_and_views(outputs):
    keys = document(PAPER / "REPLAY_KEYS.json")
    expected_files = {"verify.py", "PARAMETERS.json", "CANONICAL.json", "DESIGN_COMMITMENT.md", "COMMITMENT_PINS.sha256",
        "INPUT_PINS.sha256", "instrumentation/evidence.py", "instrumentation/runtime_probe.py", "record.py",
        "pair02/INPUTS_BEFORE.json", "pair02/INPUTS_AFTER.json", "pair02/CONTEXT.json", "pair02/runtime_1.json", "pair02/runtime_2.json",
        "pair02/REPORT.json", "execution/pair02/ATTEMPT.json", "execution/pair02/RESULT.json"}
    require(keys["schema"] == "p210-a-replay-keys-v1" and keys["interpreter"] == "/usr/bin/python3.10" and
            keys["unoptimized"] is True and keys["parameters"] == PARAMETERS and
            keys["environment"] == expected_environment(PAPER / "pair02"), "exact selected replay configuration")
    require(keys["file_keys"] == {str((PAPER / name).relative_to(WORKSPACE)): memo(PAPER / name)["sha256"] for name in expected_files},
            "all17 exact selected key bindings, including current safe recorder")
    require(keys["flags"] == ["-I", "-S", "-B", "-X", "pycache_prefix=NEW_ABSOLUTE_ABSENT_PATH"] and
            keys["root_direct_command_template"] == ["/usr/bin/python3.10", "-I", "-S", "-B", "-X",
                "pycache_prefix=NEW_ABSOLUTE_ABSENT_PATH", str(PAPER / "verify.py"), str(PAPER / "PARAMETERS.json")],
            "exact parameter-aware root interface; not run here")
    require(keys["complete_runtime_key_ledgers"] == ["pair02/INPUTS_BEFORE.json", "pair02/INPUTS_AFTER.json"] and
            keys["runtime_input_count"] == 2631 and keys["scientific_output_bytes"] == 703850 and
            keys["scientific_checks_per_run"] == 133978 and keys["complete_box_states"] == 4095 and
            keys["scientific_schema"] == "p210-review-a-cut-graph-v1" and "not an OS/startup trace" in keys["probe_scope"],
            "original full dependency key and bounded trace limitation")
    require(outputs["finish_records01"] == dict(status="RECORDED_ACTUAL_OBSERVATIONS", views=12, replay_key_paths=17),
            "original metadata materialization native output; not the view operation")
    views = []
    for build in ("build01", "build02"):
        view = document(PAPER / ("VIEW_" + build + ".actual.json"))
        require(set(view) == {"reviewer", "role", "pdf", "pdf_sha256", "pages", "status", "open_layout_findings", "boundary"}, "view receipt exact schema")
        require(view["reviewer"] == "/root/p210_a_reviewer" and view["status"] == "PASS" and view["open_layout_findings"] == 0 and
                view["role"] == "actual manual inspection after viewing all6 page images with view_image, not inferred from hashes" and
                view["boundary"] == "Review A page inspection, not root or terminal-batch inspection", "actual A-only view provenance")
        require(view["pdf"] == str((PAPER / build / "source/main.pdf").relative_to(WORKSPACE)) and
                view["pdf_sha256"] == memo(WORKSPACE / view["pdf"])["sha256"], "actual viewed PDF binding")
        require([row["page"] for row in view["pages"]] == list(range(1, 7)), "all six individually recorded views")
        for row in view["pages"]:
            require(set(row) == {"page", "path", "sha256", "actually_viewed", "observation"} and
                    row["path"] == str((PAPER / build / ("page-%d.png" % row["page"])).relative_to(WORKSPACE)) and
                    row["actually_viewed"] is True and isinstance(row["observation"], str) and bool(row["observation"]) and
                    memo(WORKSPACE / row["path"])["sha256"] == row["sha256"], "actual manual observation/rendered-image binding, NOT new view")
        equal_raw(PAPER / build / "source/main.pdf", FROZEN / "main.pdf")
        views.append(dict(receipt="VIEW_" + build + ".actual.json", recorded_manual_views=6, pdf_sha256=view["pdf_sha256"]))
    equal_raw(PAPER / "build01/source/main.pdf", PAPER / "build02/source/main.pdf")
    return views


def audit_ledger(outputs):
    report = outputs["audit01"]
    require(report["schema"] == "p210-a-initial-original-audit-v1" and report["status"] == "PASS" and
            report["checks"] == 2808495 and report["actual_read_paths"] == 118753 and report["freeze_inputs"] == 494 and
            report["child_payload_counts"] == PAYLOAD_COUNTS and report["child_runtime_input_counts"] == INPUT_COUNTS and
            report["current_open_findings"] == 0 and report["resolved_major_findings"] == 1,
            "original own-audit complete result/census, NOT its re-execution")
    require(report["native_commands"] == [[name, command, 0] for name in PACKAGE_NAMES for command in
            child_commands(PAPER / name, "build" if name.startswith("build") else "produce" if name.startswith("produce") else "pair")],
            "all59 original documentary audit child-command records")
    require(report["read_ledger"] == "AUDIT_READS.json.gz" and report["read_ledger_sha256"] ==
            memo(PAPER / "AUDIT_READS.json.gz")["sha256"] == "5592833bcd0dde7c2c995ac908446459af44320703e6c8bb195e865acc9de696",
            "actual native audit stdout names whole original lossless read ledger")
    require(memo(PAPER / "execution/audit01/stdout")["sha256"] == AUDIT_STDOUT_SHA, "exact final emitted audit output")
    roles = document(PAPER / "AUDIT_READ_ROLES.json")
    require(roles["schema"] == "p210-a-audit-read-roles-v1" and roles["read_ledger"] == "AUDIT_READS.json.gz" and
            roles["ledger_sha256"] == report["read_ledger_sha256"] and roles["actual_scope_check"] == "execution/audit_roles01/stdout",
            "exact original documentary role contract")
    exceptions = roles["exact_exceptions"]
    require(len(exceptions) == 1, "only one explicit own generated-output observation role")
    exception = exceptions[0]
    require(set(exception) == {"path", "role", "observed_size", "observed_sha256", "final_sha256", "final_native_result", "explanation"} and
            exception["path"] == "execution/audit01/stdout" and exception["observed_size"] == 0 and
            exception["observed_sha256"] == EMPTY_SHA and exception["final_sha256"] == AUDIT_STDOUT_SHA and
            exception["final_native_result"] == "execution/audit01/RESULT.json" and
            exception["role"] == "auditor own open output before final result emission; NOT an input dependency", "exact one output role, no wildcard drift waiver")
    ledger = document(PAPER / "AUDIT_READS.json.gz")
    require(len(ledger) == 118753, "whole original audit read dictionary")
    special = str(PAPER / "execution/audit01/stdout")
    require(ledger[special] == dict(sha256=EMPTY_SHA, size=0, real=special, symlink=None), "actual historic empty self-output observation")
    differences = []
    for spelling, value in ledger.items():
        if spelling == special:
            require(memo(spelling)["sha256"] == AUDIT_STDOUT_SHA, "only generated audit output has explicit current role")
        else:
            pin(spelling, value)
        if Path(spelling).is_relative_to(PAPER) and memo(spelling)["sha256"] != value["sha256"]:
            differences.append(dict(path=str(Path(spelling).relative_to(PAPER)), observed_sha256=value["sha256"], current_sha256=memo(spelling)["sha256"]))
    require(outputs["audit_roles01"] == dict(role="actual documentary read-ledger observations versus later owned-file state, not scientific input changes",
        changes=[dict(path="execution/audit01/stdout", observed_sha256=EMPTY_SHA, current_sha256=AUDIT_STDOUT_SHA)]) and
        outputs["audit_roles01"]["changes"] == differences, "actual full owned-path difference census exactly matches sole output exception")
    return dict(whole_original_read_paths=len(ledger), exact_generated_self_output_roles=1, all_other_original_keys_current_unchanged=True)


def documents_and_sources():
    findings = document(PAPER / "FINDINGS.json")
    require(findings["schema"] == "p210-a-findings-v1" and findings["reviewer"] == "/root/p210_a_reviewer" and
            findings["round"] == "A_initial" and findings["verdict"] == "PASS_NARROW_TWO_AXIS_INITIAL_AWAITING_ROOT_RESPONSE",
            "actual initial A only, not a new review or accepted delta")
    require(findings["census"] == {"Critical": {"open": 0, "resolved": 0}, "Major": {"open": 0, "resolved": 1},
            "Minor": {"open": 0, "resolved": 0}, "total_open": 0, "total_resolved": 1} and len(findings["findings"]) == 1,
            "exact initial finding census with real resolved Major retained")
    finding = findings["findings"][0]
    require(finding["id"] == "P210-A-E1" and finding["severity"] == "Major" and finding["status"] == "resolved" and
            finding["changed_scientific_inputs"] == [] and "remain unavailable" in finding["historical_loss_not_repaired"],
            "resolution by fresh evidence, NOT recovery of historical lost bytes")
    for relative in finding["resolution_evidence"]:
        require(not Path(relative).is_absolute() and ".." not in Path(relative).parts, "exact local resolution-evidence role")
        memo(PAPER / relative)
    for name in ("REPORT.md", "SOURCE_AND_PROOF.md", "REPLAY_LOG.md", "BUILD_REPORT.md", "DELTA.md", "ARTIFACT_ROLES.md",
                 "SANITIZATION.md", "DESIGN_COMMITMENT.md", "INDEPENDENCE_ORDER.md"):
        body = text(PAPER / name)
        require(bool(body.strip()), "nonempty original report, not template")
    require("NOT_YET_ACCEPTED_DELTA" in text(PAPER / "DELTA.md") and "AWAITING_ROOT_RESPONSE" in text(PAPER / "REPORT.md"),
            "initial report cannot become delta acceptance or Round1")
    require("HOLD_EXTERNAL" in text(PAPER / "REPORT.md") and "OWNER_AMBER" in text(PAPER / "REPORT.md"), "internal external-hold scope")
    expected_requests = [
        {"open": [{"ref_id": uri} for uri in ["https://oeis.org/A353847", "https://oeis.org/A375123", "https://oeis.org/A023361",
           "https://ac.inf.elte.hu/Vol_043_2014/239_43.pdf"]], "response_length": "long"},
        {"open": [{"ref_id": uri} for uri in ["https://ajc.maths.uq.edu.au/pdf/74/ajc_v74_p364.pdf", "https://arxiv.org/abs/1505.02308",
           "https://arxiv.org/pdf/1505.02308", "https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2019/6.html"]], "response_length": "long"},
        {"open": [{"ref_id": "https://arxiv.org/pdf/1505.02308", "lineno": 308},
                  {"ref_id": "https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2019/6.html", "lineno": 0}], "response_length": "long"},
        {"click": [{"ref_id": "turn9803view1", "id": 0}], "response_length": "long"}]
    for index, request in enumerate(expected_requests, 1):
        evidence = document(PAPER / ("sources/web%02d.actual.json" % index))
        require(set(evidence) == {"request", "result"} and evidence["request"] == request and
                isinstance(evidence["result"], str) and bool(evidence["result"]), "whole archived native browser request/return, no refetch")
        if index == 1:
            require("Failed to fetch https://ac.inf.elte.hu/Vol_043_2014/239_43.pdf: (400) Timeout fetching" in evidence["result"],
                    "actual new Robbins failure retained")
        if index == 2:
            require("Failed to fetch https://ajc.maths.uq.edu.au/pdf/74/ajc_v74_p364.pdf: Failed to fetch restricted URL" in evidence["result"],
                    "actual new Gessel access failure retained")
    return dict(source_returns=4, original_open_operations=10, original_click_operations=1,
                actual_source_failures_retained=2, new_source_requests=0, current_open_findings=0, resolved_major_findings=1,
                delta_accepted=False, global_priority_or_new_proof_review=False)


def semantic_compare():
    """Entire original 300628-predicate DATA adapter, no dynamics/checker execution.

    Reproduced transparently from pinned compare_author.py, with only original
    filesystem reads replaced by inspection readers and output returned as data.
    This is not an independently invented scientific proof or verifier.
    """
    D = PAPER
    F = FROZEN
    paths = [D/'CANONICAL.json', F/'CANONICAL.json', D/'compare_author.py']
    def pins():
        return {str(p):fresh_pin(p)['sha256'] for p in paths}
    before = pins()
    a = document(D/'CANONICAL.json')
    b = document(F/'CANONICAL.json')
    checks = collections.Counter()
    def eq(x,y,kind):
        checks[kind] += 1
        require(x == y, 'full canonical semantic field: ' + kind)
    def keys(x,k):
        eq(set(x),set(k.split()),'exact_keys')
    def parts(n,m):
        ends=[0]+[i for i in range(1,n) if m & (1<<(i-1))]+[n]
        return [y-x for x,y in zip(ends,ends[1:])]
    def mask(p):
        pos=m=0
        for x in p[:-1]:
            pos+=x;m|=1<<(pos-1)
        return m
    def intervals(p):
        pos=0;out=[]
        for x in p:
            out.append([pos,pos+x]);pos+=x
        return out
    keys(b,'schema mass_box parameters masses totals checks_by_kind checks')
    eq(b['schema'],'P210_AUTHOR_FULL_CANONICAL_V1','schema')
    eq(b['mass_box'],[1,12],'box')
    eq(b['parameters'],{'positive_parts':True,'old_part_synchronous':True,'external_data':False},'parameters')
    eq(len(b['masses']),12,'mass_count')
    eq(b['checks'],sum(b['checks_by_kind'].values()),'author_internal_count_sum')
    eq(b['checks'],197471,'author_internal_count_record_not_independent_count')
    eq(all(isinstance(x,int) and x>0 for x in b['checks_by_kind'].values()),True,'author_internal_positive_counts')
    total_image=total_witnesses=0
    for independent,author in zip(a['tables'],b['masses']):
        keys(author,'N states targets fixed_points triangular_objects witnesses endpoint_partition_coefficients summary')
        n=independent['N'];eq(author['N'],n,'mass')
        state_rows=independent['states'];target_rows=independent['targets']
        eq(len(author['states']),len(state_rows),'state_count')
        eq([r['state'] for r in author['states']],sorted(parts(n,m) for m in range(1<<(n-1))),'complete_ordered_states')
        for row in author['states']:
            keys(row,'state edge depth fixed_endpoint orbit birth_rounds')
            own=state_rows[mask(row['state'])]
            eq(row['edge'],parts(n,own[1]),'edge')
            eq(row['depth'],own[2],'depth')
            eq(row['fixed_endpoint'],parts(n,own[3]),'endpoint')
            eq(row['orbit'],[parts(n,own[0])]+[parts(n,e[2]) for e in own[4]],'complete_orbit')
            eq(len(row['birth_rounds']),len(own[4]),'round_count')
            for event,e in zip(row['birth_rounds'],own[4]):
                keys(event,'round old new deleted_cuts new_blocks')
                eq(event['round'],e[0],'round_time')
                eq(event['old'],parts(n,e[1]),'round_old')
                eq(event['new'],parts(n,e[2]),'round_new')
                eq(event['deleted_cuts'],[dict(zip(['cut','left_mass','right_mass','right_birth'],r)) for r in e[3]],'all_deleted_cuts')
                old=intervals(event['old'])
                expected=[]
                for left,right,time in e[4]:
                    expected.append({'interval':[left,right],'mass':right-left,'parents':[p for p in old if left<=p[0] and p[1]<=right]})
                eq(event['new_blocks'],expected,'all_births_and_parents')
        eq(len(author['targets']),len(target_rows),'target_count')
        eq([r['target'] for r in author['targets']],sorted(parts(n,m) for m in range(1<<(n-1))),'complete_ordered_targets')
        for row in author['targets']:
            keys(row,'target fibre sources suffixes image code')
            own=target_rows[mask(row['target'])]
            eq(row['sources'],sorted(parts(n,m) for m in own[2]),'complete_source_set')
            eq(row['fibre'],own[5],'fibre')
            eq(row['image'],bool(own[2]),'image')
            eq(row['code'],own[6],'encoding')
            s=row['target'];eq(len(row['suffixes']),len(s),'suffix_count')
            for i,suffix in enumerate(row['suffixes']):
                keys(suffix,'index part threshold branch attainable_first_parts first_part_counts attaining_preimage')
                eq(suffix['index'],i,'suffix_index');eq(suffix['part'],s[i],'suffix_part')
                tail=s[i:];mass=sum(tail)
                src=a['tables'][mass-1]['targets'][mask(tail)][2]
                first=collections.Counter(parts(mass,m)[0] for m in src)
                minfirst=min(first) if first else None
                eq(suffix['threshold'],minfirst,'every_attained_minimum')
                eq(suffix['attainable_first_parts'],sorted(first),'every_attained_set')
                eq(suffix['first_part_counts'],[list(x) for x in sorted(first.items())],'every_first_count')
                if i==len(s)-1:branch='initial'
                elif not own[3][i+1]:branch='infeasible_suffix'
                else:
                    r=min(own[3][i+1])
                    branch='fail' if s[i]<=r else 'increment' if s[i]==r+1 else 'reset'
                eq(suffix['branch'],branch,'every_scan_branch')
                w=suffix['attaining_preimage']
                if minfirst is None: eq(w,None,'no_infeasible_witness')
                else:
                    eq(sum(w),mass,'witness_mass');eq(w[0],minfirst,'witness_attainment')
                    eq(mask(w) in src,True,'witness_actual_source_membership')
        fixed=sorted(parts(n,r[0]) for r in state_rows if r[2]==0)
        eq(author['fixed_points'],fixed,'complete_fixed_set')
        expected_tri=sorted([{'parts':r[1],'decoded_target':r[2]} for r in independent['triangular']],key=lambda x:x['parts'])
        eq(author['triangular_objects'],expected_tri,'all_triangular_decodings')
        expected_w=[{'h':r[0],'surplus':r[1],'state':r[2],'orbit':[parts(n,m) for m in r[3]]} for r in independent['witnesses']]
        eq(author['witnesses'],expected_w,'all_surplus_orbits')
        refinements=[parts(n,m) for m in range(1<<(n-1)) if all(x<=y for x,y in zip(parts(n,m),parts(n,m)[1:]))]
        coeff=[[x,y,sum(r[0]==x and r[-1]==y for r in refinements)] for x in range(1,n+1) for y in range(x,n+1)]
        eq(author['endpoint_partition_coefficients'],coeff,'all_endpoint_coefficients')
        hist=collections.Counter(r[2] for r in state_rows)
        summary={'states':len(state_rows),'fixed':len(fixed),'depth_histogram':[list(x) for x in sorted(hist.items())],
                 'max_depth':max(hist),'H':independent['H'],'image':independent['image_count'],
                 'triangular_count':len(expected_tri),'witness_count':len(expected_w)}
        eq(author['summary'],summary,'all_mass_summary_fields')
        total_image+=len(expected_tri);total_witnesses+=len(expected_w)
    eq(b['totals'],{'states':4095,'edges':4095,'targets':4095,'image_objects':total_image,
                   'triangular_objects':total_image,'surplus_witnesses':total_witnesses},'whole_totals')
    after=pins();eq(before,after,'unchanged_complete_inputs')
    return {'status':'PASS','role':'whole author canonical semantic comparison after independent commitment; not raw byte equality across different schemas',
                     'inputs_before':before,'inputs_after':after,'checks':sum(checks.values()),'checks_by_kind':dict(sorted(checks.items())),
                     'independent_scientific_checks':a['checks'],'state_count':4095,'image_objects':total_image,'surplus_witnesses':total_witnesses,
                     'author_metadata_limit':'author assertion categories/census checked internally for consistency, not equated with independent execution count',
                     'noninterval_example':{'target':[6],'actual_first_parts':a['tables'][5]['targets'][0][3][0]}}


def main():
    require(len(sys.argv) == 1 and sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and
            sys.flags.optimize == 0 and Path(sys.executable).resolve() == Path("/usr/bin/python3.10").resolve(),
            "invoke read-only with /usr/bin/python3.10 -I -S -B, no optimization and no arguments")
    require(memo(PAPER / "SHA256SUMS")["sha256"] == INITIAL_SEAL, "exact sealed initial A package, no unfinished or later delta pins")
    original_manifest = manifest(PAPER, "SHA256SUMS", 484)
    preparation = document(HERE / "INPUT_PINS.json")
    require(preparation["role"] == "PREPARATION_INPUT_BINDINGS_ONLY" and preparation["initial_review_seal_sha256"] == INITIAL_SEAL and
            preparation["round0_seal_sha256"] == FREEZE_SEAL and preparation["author_alias_sha256"] == AUTHOR_SEAL,
            "exact declared preparation/current immutable inputs")
    for spelling, value in preparation["pins"].items():
        pin(spelling, value)
    memo(Path(__file__).resolve())
    frozen_manifest = reviewed_inputs()
    canonical_structure()
    packages = [package(name, raw(PAPER / "CANONICAL.json")) for name in PACKAGE_NAMES]
    require(len(NATIVE) == 59, "all59 child native original records")
    outputs = parents()
    require(len(NATIVE) == 71, "59 child and twelve enclosing parent records, no invented producer parent")
    history = privacy_history(outputs)
    semantic = []
    for tag in ("compare_author01", "compare_author02"):
        comparison = semantic_compare()
        require(comparison["checks"] == 300628 and sum(comparison["checks_by_kind"].values()) == 300628 and
                outputs[tag] == comparison, "entire recomputed DATA mapping equals entire original semantic receipt: " + tag)
        semantic.append(dict(original_record="execution/" + tag, complete_comparison_predicates=300628,
                             exact_input_paths=3, selected_safe_parent=tag.endswith("02")))
    equal_raw(PAPER / "execution/compare_author01/stdout", PAPER / "execution/compare_author02/stdout")
    views = replay_keys_and_views(outputs)
    audit = audit_ledger(outputs)
    documents = documents_and_sources()
    # Reuse full original ledgers without copying them or creating a new host tree inventory.
    # All consumed current file keys are reread uncached only after their complete role checks.
    read_keys = sorted(CURRENT)
    key_digest = hashlib.sha256(json.dumps(read_keys, separators=(",", ":")).encode()).hexdigest()
    for spelling in read_keys:
        require(fresh_pin(spelling) == CURRENT[spelling], "final uncached entire current-input reread unchanged: " + spelling)
    require(set(original_manifest) == physical(PAPER, ("SHA256SUMS",)), "complete initial review membership unchanged after checks")
    require(set(frozen_manifest) == physical(FROZEN, ("SHA256SUMS",)), "complete493 physical freeze membership unchanged after checks")
    print(json.dumps(dict(status="PASS_DOCUMENTARY_INITIAL_A_ORIGINALS_ONLY",
        prepared_by="/root/p210_a_original_desk (artifact desk, not reviewer; ineligible for future P210 B)",
        initial_review_seal_sha256=INITIAL_SEAL, initial_payloads=484, physical_round0_payloads=493, reviewed_input_pins=494,
        checks=CHECKS, original_packages=packages, complete_native_records=NATIVE, privacy_history=history,
        original_semantic_comparisons=semantic, raw_byte_comparisons=RAW_COMPARISONS, archived_view_bindings=views,
        original_audit_read_ledger=audit, source_and_finding_scope=documents, current_paths_reread=len(read_keys),
        current_path_key_sha256=key_digest, science_executions=0, tex_builds=0, new_page_views=0,
        manuscript_reviews=0, root_acceptance=False, delta_accepted=False, batch_pass=False,
        limits=["Root must read and separately execute this desk-prepared inspector; it is not manuscript acceptance.",
                "Current selected evidence uses fresh safe pair02/build02 and comparison02 parents; original E1 loss is not repaired.",
                "Old authenticated recorder source/prehash and three original start times remain UNAVAILABLE; reconstruction is UNVERIFIED.",
                "Original producer was directly tool-launched; no producer parent file receipt or keyed driver-cache path is invented.",
                "Actual source/build child runtime scope remains post-hook imports/opens/maps plus known pins, not OS/startup tracing.",
                "Original prior-pass overwritten PDFs have saved hashes/chain roles, not physical old PDF bytes; both final PDFs are physical.",
                "Recorded actual twelve page views are bound, not newly performed; no scientific checker/recorder/audit is imported or executed.",
                "Only exact audit01/stdout oldempty-to-final generated-output role is allowed; all other original ledger entries remain unchanged.",
                "Growing live author directory is not reparsed as the old489-package; reviewed physical493 Round0 and original author alias are checked.",
                "Source failures/Robbins extraction caveat and OWNER_AMBER/HOLD_EXTERNAL remain; no new external request or global priority claim."]
    ), sort_keys=True))


if __name__ == "__main__":
    main()
