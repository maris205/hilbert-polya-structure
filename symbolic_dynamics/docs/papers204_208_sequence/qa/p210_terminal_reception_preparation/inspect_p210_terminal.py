#!/usr/bin/env python3
"""UNBOUND source-only P210 terminal original-evidence receiver preparation.

Prepared by P210's manuscript/verifier author, not a manuscript reviewer.
No original program is imported or executed. No new build/view is performed.
Actual terminal seals and native evidence require a later exact-schema revision.
The preparation hard-refuses before original/host inspection or PASS output.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import sys
import sysconfig

HERE = Path(__file__).resolve().parent
QA = HERE.parent
ROOT = QA.parents[2]
PAPER = ROOT / "papers/210-weakly-increasing-run-aggregation"
OUT = PAPER / "qa_final"
PREP = QA / "p210_terminal_build_revision_01"
SOURCE_NAMES = ("main.tex", "math_commands.tex", "references.bib",
    "sections/0_abstract.tex", "sections/1_introduction.tex", "sections/2_clock.tex",
    "sections/3_image.tex", "sections/4_coding.tex", "sections/5_fibres.tex", "sections/6_scope.tex")
ENV = dict(PATH="/usr/bin:/bin", LANG="C", LC_ALL="C", TZ="UTC", SOURCE_DATE_EPOCH="1704067200",
           FORCE_SOURCE_DATE="1", openin_any="p", openout_any="p")
TOOLS = {Path("/usr/bin") / n for n in ("pdflatex", "bibtex", "kpsewhich", "pdfinfo", "pdffonts",
         "pdftotext", "pdftoppm", "ldd", "cmp", "env", "python3.10")} | {Path("/bin/bash"), Path("/bin/sh")}
STDLIB = Path("/usr/lib/python3.10")
TEX_ROOTS = tuple(map(Path, ("/usr/share/texlive/texmf-dist", "/usr/share/texmf", "/var/lib/texmf", "/etc/texmf",
    "/usr/local/share/texmf", "/root/texmf", "/root/.texlive2021/texmf-config", "/root/.texlive2021/texmf-var")))
LIB_ROOTS = tuple(map(Path, ("/usr/lib/x86_64-linux-gnu", "/usr/lib64", "/usr/local/lib")))
CONFIG_ROOTS = tuple(map(Path, ("/etc/ld.so.conf.d", "/usr/share/fonts", "/etc/fonts", "/var/cache/fontconfig",
    "/usr/share/fontconfig", "/usr/lib/locale/C.utf8", "/usr/lib/x86_64-linux-gnu/gconv", "/usr/lib/gconv",
    "/usr/share/poppler", "/usr/local/share/fonts", "/etc/xdg/fontconfig", "/etc/profile.d", "/root/.fonts",
    "/root/.fontconfig", "/root/.fonts.conf.d", "/root/.config/fontconfig", "/root/.cache/fontconfig", "/root/.local/share/fonts")))
USER_VARS = ("TEXMFHOME", "TEXMFCONFIG", "TEXMFVAR")
CURRENT = {}
CHECKS = 0
RAW_PAIRS = 0


def require(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)


def digest_bytes(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def fresh_entry(path):
    path = Path(path)
    row = dict(exists=path.exists(), symlink=path.is_symlink(), link=str(path.readlink()) if path.is_symlink() else None,
               resolved=str(path.resolve()), is_file=path.is_file(), is_dir=path.is_dir())
    if row["is_file"]:
        sha = hashlib.sha256()
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1 << 20), b""):
                sha.update(block)
        row.update(bytes=path.stat().st_size, sha256=sha.hexdigest())
    return row


def current(path):
    key = str(Path(path))
    if key not in CURRENT:
        CURRENT[key] = fresh_entry(key)
    return CURRENT[key]


def pin(path):
    row = current(path)
    require(row["is_file"], "missing current file: " + str(path))
    return {k: row[k] for k in ("sha256", "bytes")}


def raw(path):
    data = Path(path).read_bytes()
    require(digest_bytes(data) == pin(path), "complete raw read changed: " + str(path))
    return data


def read(path):
    return json.loads(raw(path))


def text(path):
    return raw(path).decode("utf-8")


def exact_pair(left, right):
    global RAW_PAIRS
    require(raw(left) == raw(right), "whole raw byte pair: " + str(left))
    RAW_PAIRS += 1


def physical(base):
    entries = list(base.rglob("*"))
    require(not any(p.is_symlink() for p in entries), "no symlink in physical sealed package")
    return {str(p): pin(p) for p in entries if p.is_file() and p != base / "SHA256SUMS"}


def manifest(base, seal, count):
    require(pin(base / "SHA256SUMS")["sha256"] == seal, "exact original manifest identity")
    rows = {}
    for line in text(base / "SHA256SUMS").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, "strict original manifest row")
        sha, name = match.groups()
        path = base / name
        require(not Path(name).is_absolute() and ".." not in Path(name).parts and name != "SHA256SUMS" and
                str(path) not in rows and path.resolve() == path, "exact contained original member")
        value = pin(path)
        require(value["sha256"] == sha, "original manifest digest")
        rows[str(path)] = value
    require(len(rows) == count and rows == physical(base), "complete nonself original membership")
    return {**rows, str(base / "SHA256SUMS"): pin(base / "SHA256SUMS")}


def ledger(name):
    path = OUT / (name + ".json.gz")
    compressed = raw(path)
    body = gzip.decompress(compressed)
    sidecar = read(OUT / (name + ".json.gz.meta.json"))
    data = json.loads(body)
    require(sidecar == dict(encoding="gzip of exact UTF-8 JSON with terminal LF; mtime=0",
            json_bytes=len(body), json_sha256=hashlib.sha256(body).hexdigest(), compressed=pin(path),
            semantic_groups={k: len(v) for k, v in data.items()}), "entire lossless ledger sidecar")
    require(body.endswith(b"\n") and compressed[:4] == b"\x1f\x8b\x08\x00" and compressed[4:8] == b"\x00" * 4,
            "exact gzip header and final JSON newline")
    return data, digest_bytes(body)


def known_membership(snapshot):
    # Match the original bounded selection rules; never copy any host tree.
    std = {STDLIB}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [n for n in folders if n not in {"site-packages", "dist-packages", "__pycache__"}]
        std.update(Path(directory) / n for n in files if not n.endswith((".pyc", ".pyo")))
    runtime = std | TOOLS | set(LIB_ROOTS)
    for base in LIB_ROOTS:
        paths = base.glob("*") if base == Path("/usr/local/lib") else base.rglob("*")
        runtime.update(p for p in paths if p.is_file() and (p.name.endswith(".so") or ".so." in p.name))
    groups = {"runtime": {str(p) for p in runtime}}
    for name, roots in (("tex", TEX_ROOTS), ("configuration", CONFIG_ROOTS)):
        selected = set(roots)
        for base in roots:
            if base.is_dir():
                selected.update(base.rglob("*"))
        if name == "configuration":
            # Restore the original explicit selection, including ABSENT fixed
            # children underneath recursive roots; never inherit ledger extras.
            selected.update(map(Path, ("/etc/ld.so.cache", "/etc/ld.so.conf", "/etc/ld.so.preload",
                "/etc/locale.conf", "/etc/default/locale", "/etc/nsswitch.conf", "/etc/localtime",
                "/etc/bash.bashrc", "/etc/profile", "/etc/passwd", "/etc/group", "/etc/fonts/local.conf",
                "/usr/lib/locale/locale-archive", "/root/.fonts.conf", "/root/.config/fontconfig/fonts.conf",
                "/usr/lib/python310.zip", "/usr/bin/pyvenv.cfg", "/usr/pyvenv.cfg")))
            for base in (Path("/usr/bin"), Path("/usr/lib")):
                selected.update(base / n for n in ("python._pth", "python3._pth", "python310._pth", "python3.10._pth"))
            selected.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
            for key in ("LDLIBRARY", "INSTSONAME"):
                value = sysconfig.get_config_var(key)
                if value:
                    selected.add(STDLIB.parent / (value + "._pth"))
            ldd = text("/usr/bin/ldd")
            match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
            require(ldd.startswith("#!/bin/bash\n") and match is not None, "original ldd interpreter/loader-list rule")
            selected.update(map(Path, match.group(1).split()))
        groups[name] = {str(p) for p in selected}
    differences = {name: dict(missing=sorted(set(snapshot.get(name, {})) - groups.get(name, set())),
                              unexpected=sorted(groups.get(name, set()) - set(snapshot.get(name, {}))))
                   for name in sorted(set(snapshot) | set(groups))}
    require(set(snapshot) == set(groups) and all(not d["missing"] and not d["unexpected"] for d in differences.values()),
            "complete original-scope current directory membership: " + json.dumps(differences, sort_keys=True))


def final_schema_binding():
    """Hard unbound prerequisite; this preparation has no success branch.

    A later separately sealed revision must fully read the actual builder
    preparation/output manifests, FINAL_SCHEMA_BINDING_RETURN, accepted
    B/root/Round2 prerequisites and actual outer native launch/completion
    plus complete raw streams. It must use their actual schemas, pin every
    consumed path through current/raw, and derive this adapter's own binding
    interface: preparation/build sha256 and payload counts, the full final
    schema-binding return, and actual_native normalized argv/cwd/native exit
    plus stdout/stderr bytes. Those interface names are not claims about
    future artifact filenames or schema. A caller-provided bool, dictionary,
    output RESULT or proposed manifest cannot attest native completion.
    """
    recipe = read(HERE / "INPUT_CONTRACT.json")
    require(recipe["schema"] == "p210-terminal-reception-unbound-contract-v1" and
            recipe["stage"] == "PRELIMINARY_UNBOUND_NO_EXECUTION" and
            recipe["final_schema_binding"] is None, "unchanged unbound preparation contract")
    raise RuntimeError("UNBOUND_ACTUAL_P210_TERMINAL_SEALS_ROOT_NATIVE_AND_FINAL_SCHEMA: "
                       "new exact-schema source review and separate seal required")


def originals(recipe, binding):
    expected = manifest(PREP, binding["preparation_sha256"], binding["preparation_payloads"])
    final = read(OUT / "FINAL_SCHEMA_BINDING_RETURN.json")
    require(final == binding["final_schema_binding_return"] and set(final["papers"]) == {"P210"},
            "entire actually bound final return and one-paper scope")
    require(all(path not in recipe["infrastructure_pins"] or recipe["infrastructure_pins"][path] == value
                for path, value in final["required_input_pins"].items()), "no conflicting original roles")
    for path, value in {**recipe["infrastructure_pins"], **final["required_input_pins"]}.items():
        require(pin(path) == value, "actual complete prerequisite original")
        expected[path] = value
    paper = final["papers"]["P210"]
    freeze, live = Path(paper["freeze"]), Path(paper["paper"])
    require(live == PAPER and freeze == PAPER / "frozen_round2" and paper["round"] == 2,
            "actual physical P210 Round2, not Round1 or a proposed freezer")
    expected.update(manifest(freeze, paper["freeze_manifest"]["sha256"], paper["freeze_payloads"]))
    names = paper["source_names"]
    require(tuple(names) == SOURCE_NAMES and set(names) == set(paper["source_pins"]), "exact ten-source contract")
    require(paper["underfull"] == [] and paper["pages"] == 6, "exact six-page zero-Underfull baseline")
    for base in (freeze, live):
        require({str(p.relative_to(base)) for p in (base / "sections").rglob("*") if p.is_file()} ==
                {n for n in names if n.startswith("sections/")}, "exact accepted source membership")
        for name, value in {**paper["source_pins"], "main.pdf": paper["pdf_pin"]}.items():
            require(pin(base / name) == value, "actual live/frozen scientific source and PDF")
            expected[str(base / name)] = value
        main_tex = text(base / "main.tex")
        inputs = {n if n.endswith(".tex") else n + ".tex" for n in re.findall(r"\\input\{([^}]+)\}", main_tex)}
        require(inputs == set(names) - {"main.tex", "references.bib"}, "entire main input graph")
        require("\\bibliography{references}" in main_tex and "\\bibliographystyle{plainnat}" in main_tex and
                "\\author{Anonymous}" in main_tex and "pdfauthor={}" in main_tex, "exact bibliography and anonymity")
    require(read(OUT / "ORIGINALS_BEFORE.json") == read(OUT / "ORIGINALS_AFTER.json") == expected,
            "entire original pre/post key and all actual current original pins")
    return expected, final


def commands(contract):
    # Expected native sequence/argv/direct inputs; none of these commands run here.
    result = {}
    def add(label, argv, cwd, direct=(), mutable=()):
        result[label] = (list(map(str, argv)), str(cwd), {str(argv[0]), *map(str, direct)}, {str(p) for p in mutable})
    add("source_cmp", ["/usr/bin/cmp", "--", PREP / "build_p210.py", OUT / "executed_source.py"], OUT,
        [PREP / "build_p210.py", OUT / "executed_source.py"])
    elf = sorted(str(p) for p in TOOLS | set((STDLIB / "lib-dynload").glob("*.so")) if raw(p)[:4] == b"\x7fELF")
    add("ldd_before", ["/usr/bin/ldd", *elf], OUT, elf)
    for tool in ("pdflatex", "bibtex"):
        add(tool + "_version", ["/usr/bin/" + tool, "--version"], OUT)
    add("texmf_roots", ["/usr/bin/kpsewhich", "-var-value=TEXMF"], OUT)
    for ident in ("P210",):
        paper = contract["papers"][ident]
        freeze_pdf = Path(paper["freeze"]) / "main.pdf"
        add("P210_round2_pdfinfo", ["/usr/bin/pdfinfo", freeze_pdf], OUT, [freeze_pdf])
        for number in (1, 2):
            label = ident + "_cold_build_" + str(number)
            cold = OUT / ("cold_build_" + str(number))
            pdf = cold / "main.pdf"
            for variable in USER_VARS:
                add(label + "_" + variable, ["/usr/bin/kpsewhich", "-var-value=" + variable], cold)
            for n in (1, 2, 3):
                add(label + "_pass" + str(n), ["/usr/bin/pdflatex", "-no-shell-escape", "-recorder",
                    "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cold,
                    [cold / name for name in paper["source_names"]], [cold / ("main." + s) for s in ("aux", "bbl", "out", "toc")])
                if n == 1:
                    add(label + "_bst", ["/usr/bin/kpsewhich", "plainnat.bst"], cold)
                    bst = Path(text(OUT / "commands" / (label + "_bst") / "stdout").strip()).resolve()
                    add(label + "_bibtex", ["/usr/bin/bibtex", "main"], cold, [cold / "main.aux", cold / "references.bib", bst])
            for tool in ("pdfinfo", "pdffonts"):
                add(label + "_" + tool, ["/usr/bin/" + tool, "main.pdf"], cold, [pdf])
            add(label + "_pdftotext", ["/usr/bin/pdftotext", "-layout", "main.pdf", OUT / (label + ".txt")], cold, [pdf])
            add(label + "_frozen_cmp", ["/usr/bin/cmp", "--", pdf, Path(paper["freeze"]) / "main.pdf"], cold,
                [pdf, Path(paper["freeze"]) / "main.pdf"])
            if number == 1:
                add(label + "_render", ["/usr/bin/pdftoppm", "-png", "-r", "105", "main.pdf", cold / "pages/page"], cold, [pdf])
        pair = [OUT / ("cold_build_" + str(n)) / "main.pdf" for n in (1, 2)]
        add(ident + "_pair_cmp", ["/usr/bin/cmp", "--", *pair], OUT, pair)
    add("ldd_after", ["/usr/bin/ldd", *elf], OUT, elf)
    return result


def native_records(result, expected):
    require(result["expected_command_count"] == len(expected) == 33 and result["expected_command_labels"] == list(expected) and
            [r["label"] for r in result["commands"]] == list(expected), "all 33 native commands, original order including actual Round2 pdfinfo")
    require({p.name for p in (OUT / "commands").iterdir()} == set(expected), "entire native command directory census")
    rows = {}
    attempt_keys = {"label", "argv", "cwd", "env", "started_epoch", "timeout_seconds", "start_new_session",
                    "exit_code", "status", "inputs_before", "generated_inputs_before"}
    for row in result["commands"]:
        label = row["label"]
        directory = OUT / "commands" / label
        attempt, receipt = read(directory / "ATTEMPT.json"), read(directory / "RECEIPT.json")
        argv, cwd, direct, mutable = expected[label]
        require(receipt == row and set(attempt) == attempt_keys, "entire original receipt/result row and attempt schema")
        require({k: v for k, v in attempt.items() if k not in {"status", "exit_code"}} ==
                {k: row[k] for k in attempt if k not in {"status", "exit_code"}}, "complete pre-spawn attempt binding")
        require(attempt["status"] == "ATTEMPTED" and attempt["exit_code"] is None and row["status"] == "COMPLETED" and
                row["exit_code"] == 0 and row["error"] is None and row["streams_settled"] is True and "cleanup" not in row,
                "real settled native success, no cleanup/failure hidden")
        require(row["argv"] == argv and row["cwd"] == cwd and row["env"] == ENV and row["timeout_seconds"] == 600 and
                row["start_new_session"] is True and isinstance(row["pid"], int) and row["pid"] > 0 and
                row["ended_epoch"] >= row["started_epoch"], "complete argv/env/cwd/process/time metadata")
        require(set(row["inputs_before"]) == direct and row["inputs_before"] == row["inputs_after"] and
                set(row["generated_inputs_before"]) == set(row["generated_inputs_after"]) == mutable, "complete direct and generated input keys")
        for path, value in row["inputs_before"].items():
            # Only the exact BibTeX .aux input role was later overwritten.
            archived = OUT / (label[:-7] + "_pass1.aux") if label.endswith("_bibtex") and path == str(Path(cwd) / "main.aux") else Path(path)
            require(pin(archived) == value, "exact immutable native input or saved BibTeX-aux role")
        require(set(row["streams"]) == {"stdout", "stderr"}, "both complete native stream pins")
        for stream in ("stdout", "stderr"):
            require(digest_bytes(raw(directory / stream)) == row["streams"][stream], "entire raw native stream")
        if argv[0] == "/usr/bin/cmp":
            require(raw(directory / "stdout") == raw(directory / "stderr") == b"", "original cmp empty success streams")
            exact_pair(argv[2], argv[3])
        require({p.name for p in directory.iterdir()} == {"ATTEMPT.json", "RECEIPT.json", "stdout", "stderr"}, "closed native record directory")
        rows[label] = row
    return rows


def build(label, paper, rows, known):
    match = re.fullmatch(r"P210_cold_build_([12])", label)
    require(match is not None, "exact P210 command label, separate from physical directory")
    cold = OUT / ("cold_build_" + match.group(1))
    initial = read(OUT / (label + "_SOURCE_ONLY_INITIAL.json"))
    require(initial == paper["source_pins"], "exact source-only initial ledger; no PDF/aux/bbl input")
    for name, value in initial.items():
        require(pin(cold / name) == value, "all final copied scientific sources unchanged")
    consumed = {}
    previous = None
    historical_out = []
    for n in (1, 2, 3):
        stem = label + "_pass" + str(n)
        row = rows[stem]
        before, after = row["generated_inputs_before"], row["generated_inputs_after"]
        for path in before:
            suffix = Path(path).suffix
            for moment, record in (("before", before[path]), ("after", after[path])):
                base = dict(exists=record["is_file"], symlink=False, link=None, resolved=path, is_file=record["is_file"], is_dir=False)
                require(record == {**base, **({k: record[k] for k in ("sha256", "bytes")} if record["is_file"] else {})}, "entire original auxiliary state schema")
                if record["is_file"]:
                    value = {k: record[k] for k in ("sha256", "bytes")}
                    if suffix == ".aux":
                        saved_pass = n if moment == "after" else n - 1
                        require(saved_pass >= 1 and pin(OUT / (label + "_pass%d.aux" % saved_pass)) == value, "physical exact per-pass auxiliary input/output")
                    elif suffix == ".bbl":
                        require(pin(OUT / (label + ".bbl")) == value, "physical bibliography product")
                    elif suffix == ".out" and value != pin(cold / "main.out"):
                        require((n, moment) in {(1, "after"), (2, "before")}, "only exact first-pass historical bookmark role")
                        historical_out.append(dict(command=stem, moment=moment, path=path, **value))
                    else:
                        require(pin(path) == value, "unchanged or final auxiliary product")
            if n == 1:
                require(before[path]["exists"] is False, "no generated input in cold first pass")
            elif suffix == ".bbl" and n == 2:
                require(before[path]["is_file"] and before[path] == after[path], "BibTeX inserts unchanged bbl between passes")
            else:
                require(before[path] == previous[path], "complete successive auxiliary state chain")
        previous = after
        observed = read(OUT / (stem + "_INPUTS.json"))
        require(set(observed) == {"local", "external"}, "entire per-pass recorder ledger")
        expected = {"local": {}, "external": {}}
        # Original recorder ledger stores unique resolved INPUT paths at the end
        # of this pass; duplicate raw lines remain physically bound in the .fls.
        for line in text(OUT / (stem + ".fls")).splitlines():
            if not line.startswith("INPUT "):
                continue
            path = Path(line[6:])
            path = (path if path.is_absolute() else cold / path).resolve()
            if path.is_relative_to(cold):
                name = str(path.relative_to(cold))
                if name in initial:
                    value = initial[name]
                else:
                    require(path.suffix in {".aux", ".bbl", ".out", ".toc"} and str(path) in after and after[str(path)]["is_file"], "exact local generated FLS role")
                    value = {k: after[str(path)][k] for k in ("sha256", "bytes")}
                expected["local"][str(path)] = value
            else:
                require(str(path) in known, "every observed external TeX input already known")
                value = pin(path)
                require(value == known[str(path)], "exact external TeX input")
                expected["external"][str(path)] = value
                consumed[str(path)] = value
        require(expected == observed, "complete raw FLS-to-ledger correspondence")
        require("Output written on main.pdf" in text(OUT / (stem + ".log")), "physical complete engine pass log")
    for suffix in ("aux", "fls", "log"):
        exact_pair(cold / ("main." + suffix), OUT / (label + "_pass3." + suffix))
    for suffix in ("bbl", "blg"):
        exact_pair(cold / ("main." + suffix), OUT / (label + "." + suffix))
    require(re.search(r"(?im)Warning--|I couldn't open|There (?:was|were) [1-9][0-9]* error messages?",
                      text(OUT / (label + ".blg"))) is None, "complete bibliography log without warnings/errors")
    bst = str(Path(text(OUT / "commands" / (label + "_bst") / "stdout").strip()).resolve())
    require(pin(bst) == known[bst], "exact recorded bibliography-style input")
    consumed[bst] = pin(bst)
    metadata = text(OUT / "commands" / (label + "_pdfinfo") / "stdout")
    fonts = text(OUT / "commands" / (label + "_pdffonts") / "stdout")
    font_rows = [line.split()[-5:] for line in fonts.splitlines()[2:] if line.strip()]
    require(font_rows and all(len(row) == 5 and row[0] == "yes" for row in font_rows), "all complete font records embedded")
    pages = int(re.search(r"^Pages:\s+(\d+)$", metadata, re.M)[1])
    require(pages == paper["pages"] and pin(cold / "main.pdf") == paper["pdf_pin"] and
            int(re.search(r"^File size:\s+(\d+) bytes$", metadata, re.M)[1]) == paper["pdf_pin"]["bytes"] and
            re.search(r"^Author:[ \t]*$", metadata, re.M), "full metadata/PDF bytes/anonymous author")
    log = text(cold / "main.log")
    diagnostics = {name: re.findall(pattern, log, re.M) for name, pattern in dict(undefined=r"^.*undefined.*$",
        overfull=r"^.*Overfull.*$", underfull=r"^.*Underfull.*$", warnings=r"^.*Warning.*$",
        rerun=r"^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$").items()}
    require(diagnostics["underfull"] == paper["underfull"] and all(not v for k, v in diagnostics.items() if k != "underfull"), "exact allowed final diagnostics")
    extracted = text(OUT / (label + ".txt"))
    require(not any(x in extracted for x in ("[VERIFY]", "??", "[?]")), "complete extracted text")
    text_pages = extracted.split("\f")
    if text_pages and not text_pages[-1].strip():
        text_pages.pop()
    require(len(text_pages) == pages == 6, "actual complete PDF/text six-page agreement")
    bibliography_pages = [i + 1 for i, page_text in enumerate(text_pages)
                          if re.search(r"^\s*(?:References|Bibliography)\s*$", page_text, re.M)]
    require(bibliography_pages, "actual reference heading pages, not inferred venue compliance")
    frozen_metadata = text(OUT / "commands/P210_round2_pdfinfo/stdout")
    round2_pages = int(re.search(r"^Pages:\s+(\d+)$", frozen_metadata, re.M)[1])
    require(round2_pages == pages and int(re.search(r"^File size:\s+(\d+) bytes$", frozen_metadata, re.M)[1]) ==
            paper["pdf_pin"]["bytes"], "actual native Round2 six-page and file-byte baseline")
    expected_measured = dict(label=label, pages=pages, pdf=pin(cold / "main.pdf"), fonts=len(font_rows),
                            diagnostics=diagnostics, source_count=len(initial), visual_review="NOT_VIEWED",
                            reference_heading_pages=bibliography_pages, round2_measured_pages=round2_pages,
                            venue_page_limit=None, bibtex_warnings_or_errors=[])
    require(read(OUT / (label + "_MEASURED.json")) == expected_measured, "exact measured build result")
    products = {"main." + s for s in ("aux", "bbl", "blg", "fls", "log", "out", "pdf")}
    rendered = {"pages/page-%d.png" % n for n in range(1, pages + 1)} if label.endswith("_1") else set()
    require({str(p.relative_to(cold)) for p in cold.rglob("*") if p.is_file()} == set(initial) | products | rendered, "complete final cold directory, no unexpected inputs/products")
    for name in rendered:
        require(raw(cold / name).startswith(b"\x89PNG\r\n\x1a\n"), "rendered PNG binding, not new viewing")
    return expected_measured, consumed, historical_out


def runtime(phase, known, original, argv):
    row = read(OUT / ("PARENT_RUNTIME_" + phase + ".json"))
    require(row["argv"] == argv and row["cwd"] == str(ROOT) and row["env"] == ENV and row["sys_path"] ==
            ["/usr/lib/python310.zip", "/usr/lib/python3.10", "/usr/lib/python3.10/lib-dynload"], "entire recorded isolated parent context")
    require(row["phase"] == ("before_first_child" if phase == "BEFORE" else "after_last_child_and_inventory"), "actual runtime sample phase")
    for flag in ("dont_write_bytecode", "no_user_site", "no_site", "ignore_environment", "isolated"):
        require(re.search(r"(?:\(|, )" + flag + r"=1(?:,|\))", row["flags"]), "isolated recorded parent flags")
    require("optimize=0" in row["flags"] and row["cache_absent"] is True and row["cache_prefix"] == str(OUT / "unused_parent_cache") and
            not os.path.lexists(row["cache_prefix"]), "absent exact parent bytecode prefix")
    body = row["maps_raw"].encode()
    require(digest_bytes(body) == dict(bytes=row["maps_bytes"], sha256=row["maps_sha256"]), "entire raw original maps")
    mapped = {str(Path(line.split(None, 5)[5]).resolve()) for line in row["maps_raw"].splitlines()
              if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith("/")}
    require(mapped == set(row["mapped_files"]), "complete raw-map-to-file key")
    allowed = {**known, **original}
    for path, value in row["mapped_files"].items():
        require(pin(path) == value == allowed[path], "all observed mapped parent files")
    for name, value in row["modules"].items():
        path = value["path"]
        require(Path(path).suffix not in {".pyc", ".pyo"} and not {"site-packages", "dist-packages"}.intersection(Path(path).parts), "observed source-only modules")
        require({k: value[k] for k in ("sha256", "bytes")} == pin(path) == allowed[path], "every observed parent module")
    return dict(phase=phase, modules=len(row["modules"]), mapped=len(mapped))


def main():
    require(len(sys.argv) == 1 and sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode, "read-only isolated invocation with no arguments")
    binding = final_schema_binding()
    for path, expected in read(HERE / "INPUT_PINS.json")["pins"].items():
        require(pin(path) == expected, "preparation direct input binding")
    manifest(OUT, binding["build_sha256"], binding["build_payloads"])
    recipe = read(PREP / "INPUT_CONTRACT.json")
    original, contract = originals(recipe, binding)
    result = read(OUT / "RESULT.json")
    require(result["status"] == "PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED" and result["failures"] == [] and
            result["new_mathematical_executions"] == 0 and result["external"] == "OWNER_AMBER / HOLD_EXTERNAL" and
            result["visual_review"] == "NOT_VIEWED_ROOT_ACTUAL_PAGE_INSPECTION_REQUIRED" and
            result["paper_completion"] is False and result["five_paper_completion"] is False, "exact original completion scope")
    before, before_raw = ledger("KNOWN_INPUTS_BEFORE")
    after, after_raw = ledger("KNOWN_INPUTS_AFTER")
    require(before == after and before_raw == after_raw and set(before) == {"configuration", "runtime", "tex"},
            "entire original lossless pre/post ledger; counts derived from exact current bounded membership")
    known_membership(before)
    known = {}
    for group in before.values():
        for path, value in group.items():
            require(current(path) == value, "exact current original path/presence/link/bytes")
            if value["is_file"]:
                simple = {k: value[k] for k in ("sha256", "bytes")}
                require(value["resolved"] not in known or known[value["resolved"]] == simple, "consistent aliased known coverage")
                known[value["resolved"]] = simple
    rows = native_records(result, commands(contract))
    measured, consumed, bookmark_roles = [], {}, []
    user_roots = read(OUT / "USER_ROOTS.json")
    require(len(user_roots) == 6, "all six user TeX root queries")
    for ident in ("P210",):
        for n in (1, 2):
            label = ident + "_cold_build_" + str(n)
            value, external, historical = build(label, contract["papers"][ident], rows, known)
            measured.append(value); consumed.update(external); bookmark_roles.extend(historical)
            for variable in USER_VARS:
                raw_query = text(OUT / "commands" / (label + "_" + variable) / "stdout").strip()
                query = Path(raw_query)
                resolved = (query if query.is_absolute() else OUT / ("cold_build_" + str(n)) / query).resolve()
                require(user_roots[label + ":" + variable] == dict(query=raw_query, resolved=str(resolved), absent=True) and
                        not os.path.lexists(resolved), "every original user-root absence and query binding")
                current(resolved)
    require(measured == result["builds"] and read(OUT / "CONSUMED_TEX_BEFORE.json") ==
            read(OUT / "CONSUMED_TEX_AFTER.json") == consumed, "all measured results and complete actual consumed-TeX union")
    libraries = []
    for phase in ("BEFORE", "AFTER"):
        body = text(OUT / "commands" / ("ldd_" + phase.lower()) / "stdout")
        require("not found" not in body, "full ldd output has no unresolved dependency")
        paths = {str(Path(p).resolve()) for p in re.findall(r"(/[^\s():]+)", body)}
        record = read(OUT / ("LIBRARIES_" + phase + ".json"))
        require(paths == set(record), "all ldd headers/resolved-library paths")
        for path, value in record.items():
            require(pin(path) == value == known[path], "entire original linked-library closure")
        libraries.append(record)
    require(libraries[0] == libraries[1], "complete original link-time pre/post closure")
    argv = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X", "pycache_prefix=" + str(OUT / "unused_parent_cache"),
            str(PREP / "build_p210.py"), "--output", str(OUT), "--expected-preparation-sha256", binding["preparation_sha256"]]
    observed = [runtime(phase, known, original, argv) for phase in ("BEFORE", "AFTER")]
    expected_stdout = dict(status=result["status"], output=str(OUT), commands=33, builds=measured, failures=[],
                           seal=pin(OUT / "SHA256SUMS"), payloads=binding["build_payloads"])
    expected_native = dict(argv=["/usr/bin/env", "-i", *[k + "=" + v for k, v in ENV.items()], *argv],
                           cwd=str(ROOT), exit_code=0, stdout=json.dumps(expected_stdout, sort_keys=True) + "\n", stderr="")
    require(binding["actual_native"] == expected_native,
            "entire actual outer native normalized context/exit/raw streams, derived by exact-schema gate")
    require(text(OUT / "commands/texmf_roots/stdout") == "{{}./.texlive2021/texmf-config,./.texlive2021/texmf-var,./texmf,!!/usr/local/share/texmf,/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf,!!/usr/share/texlive/texmf-dist}\n", "exact native TeX search-root configuration")
    # No generated broad ledger is written: the original ledgers remain controlling.
    keys = sorted(CURRENT)
    for path in keys:
        require(fresh_entry(path) == CURRENT[path], "final uncached current path/presence/link/bytes reread")
    known_membership(before)
    require(len(physical(OUT)) == binding["build_payloads"], "original output membership unchanged")
    require(sorted(CURRENT) == keys, "no unreported current key added after final uncached rereads")
    known_original_paths = {}
    for group in before.values():
        for path, value in group.items():
            require(path not in known_original_paths or known_original_paths[path] == value,
                    "consistent duplicate original spelling across known ledger groups")
            known_original_paths[path] = value
    extra = {path: CURRENT[path] for path in keys if path not in known_original_paths}
    require({**known_original_paths, **extra} == CURRENT and not set(known_original_paths).intersection(extra),
            "complete disjoint original-spelling known union plus rich current extras")
    complete_raw = json.dumps(CURRENT, sort_keys=True, separators=(",", ":")).encode("utf-8")
    reconstruction = dict(known_ledger=str(OUT / "KNOWN_INPUTS_BEFORE.json.gz"),
        known_ledger_pin=pin(OUT / "KNOWN_INPUTS_BEFORE.json.gz"), known_original_paths=len(known_original_paths),
        merge_rule="Union all three original ledger groups by original path spelling with exact duplicate equality, then disjoint extra_entries; no resolved-path substitution.",
        canonical_encoding="json.dumps(complete_map, sort_keys=True, separators=(',', ':')).encode('utf-8'); ensure_ascii=True; no terminal LF",
        extra_entries=extra, extra_count=len(extra), complete_entries=len(CURRENT), complete_map=digest_bytes(complete_raw))
    print(json.dumps(dict(status="PASS_P210_TERMINAL_BUILD_ORIGINAL_DOCUMENTS_ONLY", preparer="/root/p210_checkpoint_planner; author, not reviewer",
        checks=CHECKS, original_payloads=binding["build_payloads"], original_commands=33, original_builds=measured,
        current_path_keys=len(keys), current_path_keys_sha256=hashlib.sha256(json.dumps(keys, separators=(",", ":")).encode()).hexdigest(),
        current_key_reconstruction=reconstruction,
        gzip_groups={k: len(v) for k, v in before.items()}, original_inputs=len(original), consumed_tex=len(consumed),
        linked_files=len(libraries[0]), parent_runtime_samples=observed, raw_documentary_pairs=RAW_PAIRS,
        historical_first_pass_bookmark_hash_roles=bookmark_roles, build_seal=binding["build_sha256"],
        new_science_executions=0, new_builds=0, new_views=0, manuscript_reviews=0, root_acceptance=False,
        limitations=["Author-prepared documentary adapter; root owns source inspection, execution and acceptance.",
            "Six root page views are explicitly outside this inspector; rendered PNGs are not visual review.",
            "Historical first-pass .out files have complete native before/after chain roles, not separate physical old-byte snapshots.",
            "Original bounded known-path/FLS/link-time/parent-map scope is not child-map, transient dlopen, non-FLS or continuous OS/startup tracing.",
            "The actual outer native schema and raw-stream provenance must be bound in a later sealed exact-schema revision; this preparation is unbound."]
    ), sort_keys=True))


if __name__ == "__main__":
    main()
