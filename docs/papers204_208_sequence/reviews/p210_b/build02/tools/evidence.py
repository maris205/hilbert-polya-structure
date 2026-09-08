"""P210 B disclosed artifact adaptation; scientific checker is independently authored."""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import signal
import sysconfig

PYTHON = Path("/usr/bin/python3.10")
HELPERS = Path(__file__).resolve().parent
BOUNDARY = "B infrastructure adapted after independent scientific commitment from A evidence, root resource-key and owned-session patterns; no mathematical implementation reuse; not continuous OS/startup tracing or page view."


def write(path, obj):
    with (gzip.open(path, "xt") if path.suffix == ".gz" else path.open("x")) as stream:
        json.dump(obj, stream, sort_keys=True, indent=2)
        stream.write("\n")


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def pins(paths):
    return {str(p): dict(real=str(p.resolve()), sha256=digest(p), size=p.stat().st_size,
                         symlink=os.readlink(p) if p.is_symlink() else None)
            for p in sorted(set(paths)) if p.is_file()}


def tree(root):
    return [p for p in Path(root).rglob("*") if p.is_file() and not
            any(x in {"__pycache__", "site-packages", "dist-packages"} for x in p.parts)
            and p.suffix not in {".pyc", ".pyo"}]


def maps(text):
    return [Path(line.split(None, 5)[5]) for line in text.splitlines()
            if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith("/")]


class Capture:
    def __init__(self, args):
        self.paper, self.out = Path(args.paper).resolve(), Path(args.out).resolve()
        allowed = Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p210_b')
        if self.out == allowed or not self.out.is_relative_to(allowed) or self.out.exists():
            raise ValueError("--out must be an absent strict descendant of Review B ownership")
        self.out.mkdir(parents=True)
        self.env = dict(PATH="/usr/bin:/bin", LANG="C.UTF-8", LC_ALL="C.UTF-8", TZ="UTC")
        for name in ("empty_home", "tmp", "source", "tools", "commands"):
            (self.out / name).mkdir()
        self.source, self.codes = self.out / "source", []
        for path in HELPERS.glob("*.py"):
            shutil.copy2(path, self.out / "tools" / path.name)
        write(self.out / "CONTEXT.json", dict(boundary=BOUNDARY, argv=sys.argv,
              environment=self.env, interpreter=sys.executable, version=sys.version,
              flags=str(sys.flags), cwd=str(Path.cwd()), platform=os.uname()[:]))
        write(self.out / "PARENT_MAPS_BEFORE.json", dict(raw=Path('/proc/self/maps').read_text(),
              modules={name: getattr(module, '__file__', None) for name, module in sorted(sys.modules.items())}))

    def command(self, name, argv, cwd=None):
        directory = self.out / "commands" / name
        directory.mkdir()
        write(directory / "ATTEMPT.json", dict(argv=list(map(str, argv)), cwd=str(cwd or self.source),
                                               environment=self.env, start_ns=time.time_ns()))
        process = None
        timed_out = False
        with (directory / "stdout").open("xb") as stdout, (directory / "stderr").open("xb") as stderr:
            process = subprocess.Popen(list(map(str, argv)), cwd=cwd or self.source,
                    env=self.env, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                    start_new_session=True)
            try:
                process.wait(timeout=300)
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(process.pid, signal.SIGTERM)
                process.wait(timeout=10)
        members = []
        for proc in Path("/proc").iterdir():
            if not proc.name.isdigit():
                continue
            try:
                raw = (proc / "stat").read_text()
                fields = raw[raw.rfind(")") + 2:].split()
                if int(fields[2]) == process.pid:
                    members.append(dict(pid=int(proc.name), state=fields[0],
                                        pgid=int(fields[2]), sid=int(fields[3])))
            except (OSError, ProcessLookupError, PermissionError):
                continue
        live = [row for row in members if row["state"] != "Z"]
        if live:
            assert all(row["sid"] == process.pid for row in live)
            os.killpg(process.pid, signal.SIGKILL)
            raise RuntimeError("Unexpected live owned descendant; unsealed streams")
        write(directory / "RESULT.json", dict(native_returncode=process.returncode,
              native_pid=process.pid, owned_sid=process.pid, owned_pgid=process.pid,
              end_ns=time.time_ns(), timed_out=timed_out,
              process_group_settlement=dict(quiescent=True, remaining_members=members),
              stdout_sha256=digest(directory / "stdout"), stderr_sha256=digest(directory / "stderr")))
        self.codes.append((name, process.returncode if not timed_out else 124))
        return directory

    def copy(self, names):
        self.inputs = []
        for name in sorted(set(names)):
            relative = Path(name)
            source = self.paper / relative
            if relative.is_absolute() or ".." in relative.parts or not source.resolve().is_relative_to(self.paper):
                raise ValueError("Source input escapes paper")
            if not source.is_file():
                raise FileNotFoundError(source)
            target = self.source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            self.inputs.extend([source, target])
        self.inputs.extend(HELPERS.glob("*.py"))
        self.inputs.extend((self.out / "tools").glob("*.py"))

    def inventory(self, executables, build=False):
        roots = ["/usr/lib/python3.10", "/usr/lib/locale", "/usr/lib/x86_64-linux-gnu/gconv"]
        if build:
            roots += ["/etc/texmf", "/var/lib/texmf", "/usr/share/texlive/texmf-dist",
                      "/usr/share/texmf", "/etc/fonts", "/usr/share/fontconfig", "/var/cache/fontconfig",
                      "/usr/share/poppler", "/usr/share/fonts"]
        self.pin_suffix = ".json.gz"
        self.roots = roots
        self.build = build
        self.fixed = self.inputs + list(executables) + [PYTHON, Path("/usr/bin/ldd"), Path("/usr/bin/bash")]
        self.fixed += maps(Path("/proc/self/maps").read_text())
        self.fixed += [Path(x) for x in ("/etc/ld.so.cache", "/etc/ld.so.conf", "/etc/localtime",
                       "/etc/nsswitch.conf", "/etc/locale.alias", "/etc/locale.gen", "/etc/default/locale",
                       "/usr/share/locale/locale.alias", "/etc/texmf/web2c/texmf.cnf")]
        self.fixed += tree("/etc/ld.so.conf.d")
        for index, executable in enumerate(sorted(set(executables) | {PYTHON})):
            record = self.command("ldd_%02d" % index, ["/usr/bin/ldd", executable])
            for line in (record / "stdout").read_text().splitlines():
                self.fixed += [Path(value) for value in re.findall(r"(?:=>\s+|^\s*)(/[^\s]+)", line)]
        self.fixed += [Path(__file__).resolve()]
        pinfile = self.paper / "INPUT_PINS.sha256"
        if pinfile.is_file():
            self.fixed.append(pinfile)
            self.fixed += [Path("/root/autodl-tmp/symbolic_dynamics") / line.split("  ", 1)[1] for line in pinfile.read_text().splitlines()]
        self.before = self.current()
        write(self.out / ("INPUTS_BEFORE" + self.pin_suffix), self.before)

    def current(self):
        paths = self.fixed + [p for root in self.roots for p in tree(root)]
        lib_roots = list(map(Path, ("/usr/lib/x86_64-linux-gnu", "/usr/lib64", "/usr/local/lib")))
        config_roots = list(map(Path, ("/etc/ld.so.conf.d", "/usr/lib/locale/C.utf8",
                         "/usr/lib/x86_64-linux-gnu/gconv", "/usr/lib/gconv")))
        if self.build:
            config_roots += list(map(Path, ("/usr/local/share/texmf", "/root/texmf",
                 "/root/.texlive2021/texmf-config", "/root/.texlive2021/texmf-var",
                 "/usr/local/share/fonts", "/root/.fonts", "/root/.fontconfig",
                 "/root/.config/fontconfig", "/root/.cache/fontconfig",
                 "/root/.local/share/fonts", "/etc/xdg/fontconfig", "/etc/profile.d")))
        for base in lib_roots:
            choices = base.glob("*") if base == Path("/usr/local/lib") else base.rglob("*")
            paths += [p for p in choices if p.is_file() and (p.name.endswith(".so") or ".so." in p.name)]
        for base in config_roots:
            paths += [p for p in base.rglob("*") if p.is_file()] if base.is_dir() else []
        conf = set(lib_roots + config_roots + list(map(Path, self.roots)))
        conf.update(map(Path, ("/etc/ld.so.cache", "/etc/ld.so.conf", "/etc/ld.so.preload",
            "/etc/locale.conf", "/etc/default/locale", "/etc/nsswitch.conf", "/etc/localtime",
            "/etc/ssl/openssl.cnf", "/usr/lib/ssl/openssl.cnf", "/usr/lib/locale/locale-archive",
            "/usr/lib/python310.zip", "/usr/bin/pyvenv.cfg", "/usr/pyvenv.cfg",
            "/etc/fonts/local.conf", "/root/.fonts.conf", "/root/.config/fontconfig/fonts.conf",
            sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
        for base in map(Path, ("/usr/bin", "/usr/lib")):
            conf.update(base / name for name in ("python._pth", "python3._pth", "python310._pth", "python3.10._pth"))
        for key in ("LDLIBRARY", "INSTSONAME"):
            name = sysconfig.get_config_var(key)
            if name:
                conf.add(Path("/usr/lib") / (name + "._pth"))
        match = re.search(r'^RTLDLIST="([^"]+)"', Path("/usr/bin/ldd").read_text(), re.M)
        assert match, "Known ldd loader declaration"
        conf.update(map(Path, match.group(1).split()))
        for p in conf:
            if p.is_file():
                paths.append(p)
        files = pins(paths)
        configuration = {str(p): dict(lexists=os.path.lexists(p), exists=p.exists(),
             is_file=p.is_file(), is_dir=p.is_dir(), resolved=str(p.resolve()),
             symlink=os.readlink(p) if p.is_symlink() else None) for p in sorted(conf)}
        assert not configuration["/etc/ld.so.preload"]["lexists"]
        assert not configuration["/usr/lib/python310.zip"]["lexists"]
        return dict(files=files, configuration=configuration, membership=sorted(files))

    def finish(self, details):
        write(self.out / "PARENT_MAPS_AFTER.json", dict(raw=Path('/proc/self/maps').read_text(),
              modules={name: getattr(module, '__file__', None) for name, module in sorted(sys.modules.items())}))
        after = self.current()
        write(self.out / ("INPUTS_AFTER" + self.pin_suffix), after)
        changed = sorted(p for p in set(self.before) | set(after) if self.before.get(p) != after.get(p))
        known = {v['real'] for v in self.before['files'].values()}
        unpinned_parent = []
        for phase in ('BEFORE', 'AFTER'):
            sample = json.loads((self.out / ('PARENT_MAPS_' + phase + '.json')).read_text())
            observed = maps(sample['raw']) + [Path(p) for p in sample['modules'].values() if p]
            unpinned_parent += [str(p) for p in observed if p.is_file() and str(p.resolve()) not in known]
        driver_cache_absent = not Path(sys.pycache_prefix).exists()
        ok = not changed and not unpinned_parent and driver_cache_absent and all(code == 0 for _, code in self.codes) and details["checks_passed"]
        write(self.out / "REPORT.json", dict(status="PASS" if ok else "FAIL", boundary=BOUNDARY,
              native_commands=self.codes, changed_inputs=changed, input_count=len(after["files"]),
              driver_cache_remained_absent=driver_cache_absent, **details))
        # This is a nonself artifact inventory, not the outer paper SHA256SUMS.
        write(self.out / "PAYLOADS.json", pins(p for p in self.out.rglob("*") if p.is_file()))
        print(json.dumps(dict(status="PASS" if ok else "FAIL", output=str(self.out))))
        return 0 if ok else 1


def replay(args):
    cap = Capture(args)
    names = list(args.input or ["verify.py", "PARAMETERS.json", "COMPLETE_SOURCE_COMMITMENT.actual.json"])
    if args.mode == "pair":
        names.append(args.canonical)
    if "verify.py" not in names:
        names.append("verify.py")
    cap.copy(names)
    cap.inventory([Path("/usr/bin/cmp")])
    runs, absent, missing, forbidden = [], [], [], []
    known = {v["real"] for v in cap.before["files"].values()}
    for number in range(1, 3 if args.mode == "pair" else 2):
        cache = cap.out / ("absent_pyc_%d" % number)
        if cache.exists():
            raise RuntimeError("Cache prefix is not absent")
        runtime = cap.out / ("runtime_%d.json" % number)
        record = cap.command("run_%d" % number, [PYTHON, "-I", "-S", "-B", "-X", "pycache_prefix=" + str(cache),
                             cap.out / "tools/runtime_probe.py", cap.source / "verify.py", runtime])
        runs.append(record / "stdout")
        absent.append(not cache.exists())
        if not runtime.exists():
            missing.append(str(runtime))
            continue
        data = json.loads(runtime.read_text())
        files = list(map(Path, data["existing_reads"])) + maps(data["maps_before"]) + maps(data["maps_after"])
        files += [Path(p) for p in data["modules"].values() if p]
        missing += sorted({str(p) for p in files if p.is_file() and str(p.resolve()) not in known})
        forbidden += sorted({str(p) for p in files if p.suffix in {".pyc", ".pyo"} or
                             any(x in p.parts for x in ("site-packages", "dist-packages"))})
    if args.mode == "pair":
        canonical = cap.source / args.canonical
        for name, left, right in [("cmp_pair", runs[0], runs[1]), ("cmp_1_canonical", runs[0], canonical),
                                  ("cmp_2_canonical", runs[1], canonical)]:
            cap.command(name, ["/usr/bin/cmp", left, right])
    return cap.finish(dict(checks_passed=all(absent) and not missing and not forbidden,
                      mode=args.mode, raw_outputs=list(map(str, runs)), cache_remained_absent=absent,
                      unpinned_observed_files=sorted(set(missing)), forbidden_import_inputs=sorted(set(forbidden)),
                      canonical_written=False, scientific_stdout_not_normalized=True))


def build(args):
    cap = Capture(args)
    names = ["main.tex", "math_commands.tex", "references.bib"]
    names += [str(p.relative_to(cap.paper)) for p in sorted((cap.paper / "sections").glob("*.tex"))]
    cap.copy(names)
    binaries = [Path("/usr/bin/" + x) for x in ("pdflatex", "bibtex", "kpsewhich", "pdfinfo", "pdffonts", "pdftotext", "pdftoppm")]
    cap.inventory(binaries, build=True)
    for variable in ("TEXMFHOME", "TEXMFCONFIG", "TEXMFVAR"):
        rec = cap.command("user_" + variable, ["/usr/bin/kpsewhich", "-var-value=" + variable])
        spelling = (rec / "stdout").read_text().strip()
        resolved = (cap.source / spelling).resolve() if not Path(spelling).is_absolute() else Path(spelling).resolve()
        assert not os.path.lexists(resolved), ("unexpected user TeX root", variable, str(resolved))
    cap.command("pdflatex_version", ["/usr/bin/pdflatex", "--version"])
    cap.command("bibtex_version", ["/usr/bin/bibtex", "--version"])
    for name in ("texmf.cnf", "pdflatex.fmt", "pdftex.map", "fmtutil.cnf", "updmap.cfg"):
        cap.command("kpse_" + name.replace(".", "_"), ["/usr/bin/kpsewhich", "-engine=pdftex", "-progname=pdflatex", "-all", name])
    known = {v["real"]: v["sha256"] for v in cap.before.values()}
    closure, missing = [], []
    engine = ["/usr/bin/pdflatex", "-recorder", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]
    for index, argv in enumerate([engine, ["/usr/bin/bibtex", "main"], engine, engine], 1):
        # Pin all prior-pass products before each pass; preserve each overwritten log/recorder physically.
        products = pins(p for p in cap.source.rglob("*") if p.is_file())
        record = cap.command("pass_%d" % index, argv)
        write(record / "SOURCE_BEFORE.json", products)
        write(record / "SOURCE_AFTER.json", pins(p for p in cap.source.rglob("*") if p.is_file()))
        for suffix in ("log", "fls", "aux", "bbl", "blg", "out", "toc"):
            product = cap.source / ("main." + suffix)
            if product.exists():
                shutil.copy2(product, record / product.name)
        if argv[0].endswith("pdflatex") and (record / "main.fls").exists():
            prior = {v["real"]: v["sha256"] for v in products.values()}
            generated = set()
            for line in (record / "main.fls").read_text().splitlines():
                if line.startswith(("INPUT ", "OUTPUT ")):
                    kind, spelling = line.split(" ", 1)
                    p = Path(spelling)
                    p = (p if p.is_absolute() else cap.source / p).resolve()
                    if kind == "OUTPUT":
                        generated.add(str(p))
                        continue
                    status = ("pinned_external" if str(p) in known else "prior_product" if str(p) in prior
                              else "same_pass_recorded_output" if str(p) in generated else "unresolved")
                    closure.append(dict(pass_number=index, path=str(p), role=status,
                                        final_sha256=digest(p) if p.is_file() else None))
                    if status == "unresolved":
                        missing.append(str(p))
    write(cap.out / "FLS_CLOSURE.json", closure)
    for name, argv in [("pdfinfo", ["/usr/bin/pdfinfo", "main.pdf"]), ("pdffonts", ["/usr/bin/pdffonts", "main.pdf"]),
                       ("pdftotext", ["/usr/bin/pdftotext", "-layout", "main.pdf", "-"]),
                       ("render", ["/usr/bin/pdftoppm", "-png", "-r", "110", "main.pdf", str(cap.out / "page")])]:
        cap.command(name, argv)
    log = (cap.source / "main.log").read_text(errors="replace") if (cap.source / "main.log").exists() else "MISSING LOG"
    warnings = [line for line in log.splitlines() if re.search(r"undefined|multiply defined|Rerun to|Label\(s\) may have changed|Overfull|Underfull", line)]
    bad = [line for line in warnings if re.search(r"undefined|multiply defined|Rerun to|Label\(s\) may have changed", line)]
    extracted = (cap.out / "commands/pdftotext/stdout").read_text(errors="replace")
    markers = [marker for marker in ("??", "[?]", "[VERIFY]") if marker in extracted]
    fonts = (cap.out / "commands/pdffonts/stdout").read_text(errors="replace")
    embedding = re.findall(r"\s+(yes|no)\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$", fonts, re.M)
    info = (cap.out / "commands/pdfinfo/stdout").read_text(errors="replace")
    count = re.search(r"^Pages:\s+(\d+)", info, re.M)
    pages = int(count[1]) if count else 0
    rendered = sorted(cap.out.glob("page-*.png"))
    return cap.finish(dict(checks_passed=not missing and not bad and not markers and bool(embedding)
                      and all(v == "yes" for v in embedding) and pages > 0 and len(rendered) == pages,
                      mode="draft_build", unpinned_fls_inputs=sorted(set(missing)), warnings=warnings,
                      unresolved_text_markers=markers, fonts_embedded=embedding,
                      pages=pages, rendered_pages=len(rendered), visual_inspection="NOT_PERFORMED",
                      pdf_sha256=digest(cap.source / "main.pdf") if (cap.source / "main.pdf").exists() else None))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["produce", "pair", "build"])
    parser.add_argument("--paper", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--input", action="append", help="paper-relative scientific input; repeatable")
    parser.add_argument("--canonical", default="CANONICAL.json")
    args = parser.parse_args()
    if Path(sys.executable).resolve() != PYTHON.resolve() or not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode):
        parser.error("Run with /usr/bin/python3.10 -I -S -B")
    if not sys.pycache_prefix or not Path(sys.pycache_prefix).is_absolute() or Path(sys.pycache_prefix).exists():
        parser.error("Also pass -X pycache_prefix=ABSOLUTE_ABSENT_PATH for the driver itself")
    return build(args) if args.mode == "build" else replay(args)


if __name__ == "__main__":
    raise SystemExit(main())
