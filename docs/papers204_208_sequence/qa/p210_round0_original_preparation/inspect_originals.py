#!/usr/bin/env python3
"""Read-only P210 author-original reception preparation; never execute originals.

This was written by the P210 manuscript/verifier author. Running it checks
documentary originals only; it is not a scientific replay, build, page view,
manuscript review, physical freeze, or root acceptance decision.
"""
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[3]
PAPER = WORKSPACE / "papers/210-weakly-increasing-run-aggregation"
AUTHOR_SEAL = "b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c"
PACKAGE_NAMES = ("author_produce_01", "author_pair_01", "author_pair_02", "draft_build_01", "draft_build_02")
SOURCES = ("main.tex", "math_commands.tex", "references.bib", "sections/0_abstract.tex",
           "sections/1_introduction.tex", "sections/2_clock.tex", "sections/3_image.tex",
           "sections/4_coding.tex", "sections/5_fibres.tex", "sections/6_scope.tex")
HISTORY = (
    ("author_produce_01", "PROOF_PACKAGE.md", "210b0f093c331d9e27bdc5ca8f396c2ed70b106c809bbd0e8e406db1fd91be79", "5965484e29af80c9b757cfee6257d1dcc71bde55aea378dfda2455c40481f295"),
    ("author_pair_01", "PROOF_PACKAGE.md", "210b0f093c331d9e27bdc5ca8f396c2ed70b106c809bbd0e8e406db1fd91be79", "5965484e29af80c9b757cfee6257d1dcc71bde55aea378dfda2455c40481f295"),
    ("draft_build_01", "sections/0_abstract.tex", "c5bf88f661058bba9e10f0f38b89aa4a49b8a4819a2f34c94fb01a6004c34ec0", "565e635318972b9149aa14e36421dc5200b03d65fd1fb64d684c8496cf891c71"),
    ("draft_build_01", "sections/1_introduction.tex", "7bfcd3dbab1835937976801b3d1a5ca9bf49b3d4967b35c3ce178b71236613e9", "15089d4e56baa52fdaba87635885e4ddf775f24800838c9b94da13278958043a"),
    ("draft_build_01", "sections/2_clock.tex", "2c8fe8c1efb26b36be4b6cb83e7a801d53435111aab301701c83997625df4cc3", "469c6462fee3c735bc3402caacca7497dc6c3315549e52d4d8973a1cfdbd70ea"),
)
CURRENT = {}
CHECKS = 0
NATIVE = []
USED_HISTORY = set()


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


def manifest(root, name, expected_count):
    rows = {}
    for line in text(root / name).splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, "strict manifest row")
        digest, relative = match.groups()
        require(relative not in rows and not Path(relative).is_absolute() and ".." not in Path(relative).parts,
                "unique contained manifest path")
        rows[relative] = digest
        require(memo(root / relative)["sha256"] == digest, "manifest digest: " + relative)
    require(len(rows) == expected_count and set(rows) == physical(root, (name,)), "complete handoff inventory")
    return rows


def isolated(flags):
    for name in ("dont_write_bytecode", "no_user_site", "no_site", "ignore_environment", "isolated"):
        require(re.search(r"(?:\(|, )" + name + r"=1(?:,|\))", flags) is not None, "isolated flag: " + name)


def expected_environment(root):
    return dict(PATH="/usr/bin:/bin", LANG="C", LC_ALL="C", TZ="UTC",
                HOME=str(root / "empty_home"), TMPDIR=str(root / "tmp"),
                SOURCE_DATE_EPOCH="1704067200", FORCE_SOURCE_DATE="1",
                openout_any="p", openin_any="p", shell_escape="f")


def native_record(directory, argv, env=None, cwd=None, parent=False):
    attempt = document(directory / "ATTEMPT.json")
    result = document(directory / "RESULT.json")
    stdout, stderr = raw(directory / "stdout"), raw(directory / "stderr")
    require(attempt["argv"] == argv and attempt["cwd"] == str(cwd), "entire recorded argv/cwd: " + str(directory))
    require(isinstance(attempt["start_ns"], int) and result["end_ns"] >= attempt["start_ns"], "native time ordering")
    require(result["stdout_sha256"] == hashlib.sha256(stdout).hexdigest() and
            result["stderr_sha256"] == hashlib.sha256(stderr).hexdigest(), "complete native stdout/stderr")
    if parent:
        require(set(attempt) == {"argv", "cwd", "start_ns", "input_sha256", "relevant_parent_environment"}, "parent attempt schema")
        require(set(result) == {"native_exit", "end_ns", "stdout_sha256", "stderr_sha256", "input_sha256_after", "inputs_unchanged"}, "parent result schema")
        require(result["native_exit"] == 0 and result["inputs_unchanged"] is True and
                attempt["input_sha256"] == result["input_sha256_after"], "actual completed parent return and pins")
        expected_keys = {"PATH", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "PYTHONHOME", "PYTHONPATH", "PYTHONHASHSEED",
                         "PYTHONPYCACHEPREFIX", "SOURCE_DATE_EPOCH", "TEXINPUTS"}
        require(set(attempt["relevant_parent_environment"]) == expected_keys and
                all(v is None or isinstance(v, str) for v in attempt["relevant_parent_environment"].values()),
                "entire bounded original parent environment; not child environment")
        expected_inputs = {str(PAPER / "record_command.py"), "/usr/bin/python3.10", argv[6]}
        require(set(attempt["input_sha256"]) == expected_inputs, "original wrapper exact known command inputs")
        for path, digest in attempt["input_sha256"].items():
            require(memo(path)["sha256"] == digest, "parent original current pin")
    else:
        require(set(attempt) == {"argv", "cwd", "environment", "start_ns"}, "child attempt schema")
        require(set(result) == {"native_returncode", "end_ns", "stdout_sha256", "stderr_sha256"}, "child result schema")
        require(result["native_returncode"] == 0 and attempt["environment"] == env, "entire native child status/environment")
    NATIVE.append(dict(record=str(directory.relative_to(PAPER)), argv=argv, stdout_bytes=len(stdout),
                       stderr_bytes=len(stderr), native_exit=0))
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
    require(fonts == report["fonts_embedded"] and len(fonts) == (17 if root.name.endswith("01") else 20) and all(v == "yes" for v in fonts), "every actual embedded final font")
    info = text(root / "commands/pdfinfo/stdout")
    require(re.search(r"^Pages:\s+6$", info, re.M) and re.search(r"^Author:[ \t]*$", info, re.M), "actual PDF pages and anonymous metadata")
    require(int(re.search(r"^File size:\s+(\d+) bytes$", info, re.M)[1]) == memo(source / "main.pdf")["size"], "actual PDF size metadata")
    require(report["pages"] == report["rendered_pages"] == 6 and len(list(root.glob("page-*.png"))) == 6, "all six rendered artifacts, not new views")
    for name in ("texmf.cnf", "pdflatex.fmt", "pdftex.map", "fmtutil.cnf", "updmap.cfg"):
        for spelling in text(root / "commands" / ("kpse_" + name.replace(".", "_")) / "stdout").splitlines():
            require(str(Path(spelling).resolve()) in known, "every reported TeX configuration/resource result pinned")
    return dict(source_count=10, engine_passes=3, bibliography_passes=1, fls_input_rows=len(closure), fonts=len(fonts), pages=6)


def package(name, history, canonical):
    root = PAPER / name
    mode = "build" if name.startswith("draft") else "produce" if name.startswith("author_produce") else "pair"
    report, context = document(root / "REPORT.json"), document(root / "CONTEXT.json")
    require(report["status"] == "PASS" and report["checks_passed"] is True and report["changed_inputs"] == [] and
            report["driver_cache_remained_absent"] is True, "actual author package status")
    require(report["mode"] == ("draft_build" if mode == "build" else mode), "exact package role")
    env = expected_environment(root)
    require(context["environment"] == env and context["interpreter"] == "/usr/bin/python3.10" and context["cwd"] == str(WORKSPACE), "entire original context environment/interpreter/cwd")
    isolated(context["flags"])
    driver = [str(PAPER / "evidence_tools/evidence.py"), mode, "--paper", str(PAPER), "--out", str(root)]
    require(context["argv"] == driver and "NOT an OS/startup trace" in context["boundary"], "full driver argv and bounded scope")
    require(not (root / "absent_driver_cache").exists(), "dedicated driver cache still absent")
    suffix = ".json.gz" if mode == "build" else ".json"
    before, after = document(root / ("INPUTS_BEFORE" + suffix)), document(root / ("INPUTS_AFTER" + suffix))
    require(before == after and len(before) == report["input_count"] == (117808 if mode == "build" else 2631 if mode == "produce" else 2633), "entire original pre/post path keys and values")
    for spelling, value in before.items():
        role = (name, spelling, value["sha256"])
        if role in history:
            snapshot, current_digest = history[role]
            require(value["real"] == spelling and value["symlink"] is None, "exact historical original path role")
            require(memo(snapshot)["sha256"] == value["sha256"] and memo(snapshot)["size"] == value["size"], "exact old bytes in physical snapshot")
            require(memo(spelling)["sha256"] == current_digest, "explicit known current replacement bytes")
            USED_HISTORY.add(role)
        else:
            pin(spelling, value)
    payloads = document(root / "PAYLOADS.json")
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
            require(stdout == stderr == b"" and raw(argv[1]) == raw(argv[2]), "original native comparison plus new raw byte documentary equality")
    source_names = SOURCES if mode == "build" else ("verify.py", "PARAMETERS.json", "PROOF_PACKAGE.md", "CLAIMS_EVIDENCE.md", "SOURCE_AUDIT.md") + (("CANONICAL.json",) if mode == "pair" else ())
    for relative in source_names:
        copied = root / "source" / relative
        require(str(copied) in before and str(PAPER / relative) in before and
                before[str(copied)]["sha256"] == before[str(PAPER / relative)]["sha256"], "original source-only copy key equality")
    for name2 in ("evidence.py", "runtime_probe.py"):
        require(raw(root / "tools" / name2) == raw(PAPER / "evidence_tools" / name2), "exact archived producer/instrumentation sources; never executed here")
    if mode == "build":
        require(report["warnings"] == report["unpinned_fls_inputs"] == report["unresolved_text_markers"] == [] and
                report["visual_inspection"] == "NOT_PERFORMED", "author build versus viewing roles")
        details = build_records(root, before, report)
    else:
        runs = 2 if mode == "pair" else 1
        require(report["raw_outputs"] == [str(root / ("commands/run_%d/stdout" % n)) for n in range(1, runs + 1)] and
                report["cache_remained_absent"] == [True] * runs and report["unpinned_observed_files"] == report["forbidden_import_inputs"] == [], "complete scientific raw/runtime records")
        require(report["canonical_written"] is False and report["scientific_stdout_not_normalized"] is True, "raw canonical role")
        observations = []
        for n in range(1, runs + 1):
            require(raw(root / ("commands/run_%d/stdout" % n)) == canonical, "entire original scientific stdout equals canonical bytes")
            observations.append(runtime(root, n, before, env))
        details = dict(archived_science_runs=runs, runtime_observations=observations)
    return dict(package=root.name, original_inputs=len(before), original_payloads=len(payloads), native_commands=len(commands), **details)


def main():
    require(len(sys.argv) == 1 and sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode,
            "invoke read-only checker with /usr/bin/python3.10 -I -S -B and no arguments")
    require(memo(PAPER / "SHA256SUMS")["sha256"] == AUTHOR_SEAL, "exact immutable author seal")
    original_manifest = manifest(PAPER, "SHA256SUMS", 489)
    inputs = document(HERE / "INPUT_PINS.json")
    require(inputs["role"] == "PREPARATION_INPUT_BINDINGS_ONLY" and inputs["author_seal_sha256"] == AUTHOR_SEAL, "preparation boundary and original seal")
    for spelling, value in inputs["pins"].items():
        pin(spelling, value)
    history_rows = document(PAPER / "HISTORICAL_INPUT_ROLES.actual.json")
    expected_rows, history = [], {}
    for pack, relative, old, current in HISTORY:
        key, copy = str(PAPER / relative), str(Path(pack) / "source" / relative)
        expected_rows.append(dict(package=pack, original_key=key, snapshot=copy, old_sha256=old,
                                  current_sha256=current, reason="documented author integer-domain clarification"))
        history[(pack, key, old)] = (PAPER / copy, current)
    require(history_rows == expected_rows, "all and only five exact old-path+hash roles, no fallback")
    canonical = raw(PAPER / "CANONICAL.json")
    stored = json.loads(canonical)
    require(stored["checks"] == 197471 and stored["mass_box"] == [1, 12] and stored["totals"] ==
            dict(states=4095, edges=4095, targets=4095, image_objects=265, triangular_objects=265, surplus_witnesses=28),
            "recorded canonical census only; no mathematical recomputation")
    packages = [package(name, history, canonical) for name in PACKAGE_NAMES]
    require(USED_HISTORY == set(history), "every exact historical adapter used, no skipped role")
    parents = {"archive01": ("absent_archive_cache", [str(PAPER / "archive_inputs.py")]),
               "audit01": ("absent_audit01", [str(PAPER / "audit_author.py"), "01"])}
    for tag, name, mode in (("produce01", "author_produce_01", "produce"), ("pair01", "author_pair_01", "pair"),
                            ("pair02", "author_pair_02", "pair"), ("build01", "draft_build_01", "build"), ("build02", "draft_build_02", "build")):
        parents[tag] = (name + "/absent_driver_cache", [str(PAPER / "evidence_tools/evidence.py"), mode, "--paper", str(PAPER), "--out", str(PAPER / name)])
    require(set(parents) == {p.name for p in (PAPER / "execution").iterdir()}, "all seven actual completed parent commands, including audit")
    parent_outputs = {}
    for tag, (cache, tail) in parents.items():
        argv = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X", "pycache_prefix=" + str(PAPER / cache)] + tail
        stdout, stderr = native_record(PAPER / "execution" / tag, argv, cwd=WORKSPACE, parent=True)
        require(stderr == b"" and not (PAPER / cache).exists(), "completed parent stderr/cache record")
        parent_outputs[tag] = json.loads(stdout)
        if tag not in {"archive01", "audit01"}:
            require(parent_outputs[tag] == dict(status="PASS", output=tail[-1]), "parent output binds completed named package")
    archive = document(PAPER / "sources/ARCHIVE_INPUTS.actual.json")
    require(archive["count"] == len(archive["records"]) == 19 and archive["status"] == "PASS_EXACT_ARCHIVAL_COPIES", "all archival records")
    require(archive["source_script_sha256"] == memo(PAPER / "archive_inputs.py")["sha256"], "original archive script binding; not execution")
    require(parent_outputs["archive01"] == dict(count=19, receipt_sha256=memo(PAPER / "sources/ARCHIVE_INPUTS.actual.json")["sha256"], status=archive["status"]), "actual archive parent receipt")
    for row in archive["records"]:
        original, copy = raw(row["original"]), raw(PAPER / row["copy"])
        require(original == copy and len(copy) == row["bytes"] and hashlib.sha256(copy).hexdigest() == row["sha256"], "full raw original/archive equality")
    author_audit = document(PAPER / "AUTHOR_AUDIT.actual.json")
    require(author_audit["status"] == "PASS_AUTHOR_DOCUMENTARY_ONLY" and author_audit["checks"] == 1245194 and
            author_audit["current_paths_rechecked"] == 118199 and author_audit["changed_current_inputs"] == [] and
            author_audit["science_executions"] == author_audit["tex_builds"] == author_audit["independent_reviews"] == 0,
            "original audit scope/status, not a new execution of that audit")
    require(document(PAPER / "author_audit_01/RESULT.json") == dict(status=author_audit["status"], checks=author_audit["checks"],
            receipt_sha256=memo(PAPER / "AUTHOR_AUDIT.actual.json")["sha256"]), "original author audit receipt binding")
    require(parent_outputs["audit01"] == dict(status=author_audit["status"], checks=author_audit["checks"], current_paths_rechecked=118199), "actual native enclosing audit return now included")
    require(raw(PAPER / "author_audit_01/audit_author.py") == raw(PAPER / "audit_author.py"), "original audit source copy")
    views = []
    for view_name, build in (("AUTHOR_VIEW.actual.json", "draft_build_01"), ("AUTHOR_VIEW_DRAFT02.actual.json", "draft_build_02")):
        view = document(PAPER / view_name)
        require(view["status"] == "AUTHOR_VISUAL_PASS" and view["viewer"] == "/root/p210_author" and
                view["root_viewing"] == view["terminal_builds_and_views"] == "PENDING", "original author-only actual-view role")
        require(view["pdf"] == build + "/source/main.pdf" and memo(PAPER / view["pdf"])["sha256"] == view["pdf_sha256"], "exact viewed PDF")
        require(view["render_command_record"] == build + "/commands/render/RESULT.json" and view["render_native_exit"] == 0 and
                document(PAPER / view["render_command_record"])["native_returncode"] == 0, "original rendering command binding")
        require(view["page_count"] == len(view["pages"]) == 6 and [r["number"] for r in view["pages"]] == list(range(1, 7)), "all six separately stated views")
        for row in view["pages"]:
            require(row["path"] == build + "/page-%d.png" % row["number"] and row["viewed"] is True and
                    isinstance(row["observation"], str) and bool(row["observation"]) and memo(PAPER / row["path"])["sha256"] == row["sha256"], "actual original receipt/page binding, not new viewing")
        views.append(dict(receipt=view_name, pdf_sha256=view["pdf_sha256"], archived_viewed_pages=6))
    require(raw(PAPER / "main.pdf") == raw(PAPER / "draft_build_02/source/main.pdf"), "selected final author PDF exact bytes")
    # All 489 sealed author payloads and all source/runtime/config referents above
    # have already been read. Recheck the exact current key set once, uncached.
    read_keys = sorted(CURRENT)
    key_digest = hashlib.sha256(json.dumps(read_keys, separators=(",", ":")).encode()).hexdigest()
    for spelling in read_keys:
        require(fresh_pin(spelling) == CURRENT[spelling], "final uncached reread unchanged: " + spelling)
    require(set(original_manifest) == physical(PAPER, ("SHA256SUMS",)), "handoff membership remained unchanged")
    print(json.dumps(dict(status="PASS_DOCUMENTARY_ORIGINALS_ONLY", prepared_by="/root/p210_author (author, not reviewer)",
        checks=CHECKS, author_payloads=489, exact_historical_roles=5, packages=packages, native_records=NATIVE,
        archive_raw_pairs=19, archived_view_bindings=views, current_paths_reread=len(read_keys),
        current_path_key_sha256=key_digest, author_seal_sha256=AUTHOR_SEAL,
        science_executions=0, builds=0, new_page_views=0, manuscript_reviews=0, root_acceptance=False,
        limits=["Author-prepared documentary checker; root must inspect and execute it separately.",
                "Original runtime scope is bounded post-hook/import/maps plus conservative pins, not OS/startup tracing.",
                "Prior pass overwritten PDFs have recorded product hashes/chain roles, not preserved historical PDF bytes; final PDFs are physical.",
                "Original source failures and Robbins extraction caveat remain; archived bytes do not prove novel priority."]
    ), sort_keys=True))


if __name__ == "__main__":
    main()
