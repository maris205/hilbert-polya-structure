#!/usr/bin/env python3
"""Bounded set-selection diagnosis only; no builder/original inspector execution."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sysconfig

QA = Path(__file__).resolve().parents[1]
OUT = QA / "batch_terminal_builds_01"
STDLIB = Path("/usr/lib/python3.10")
TOOLS = {Path("/usr/bin") / n for n in ("pdflatex", "bibtex", "kpsewhich", "pdfinfo", "pdffonts", "pdftotext",
    "pdftoppm", "ldd", "cmp", "env", "python3.10")} | {Path("/bin/bash"), Path("/bin/sh")}
TEX_ROOTS = tuple(map(Path, ("/usr/share/texlive/texmf-dist", "/usr/share/texmf", "/var/lib/texmf", "/etc/texmf",
    "/usr/local/share/texmf", "/root/texmf", "/root/.texlive2021/texmf-config", "/root/.texlive2021/texmf-var")))
LIB_ROOTS = tuple(map(Path, ("/usr/lib/x86_64-linux-gnu", "/usr/lib64", "/usr/local/lib")))
CONFIG_ROOTS = tuple(map(Path, ("/etc/ld.so.conf.d", "/usr/share/fonts", "/etc/fonts", "/var/cache/fontconfig",
    "/usr/share/fontconfig", "/usr/lib/locale/C.utf8", "/usr/lib/x86_64-linux-gnu/gconv", "/usr/lib/gconv",
    "/usr/share/poppler", "/usr/local/share/fonts", "/etc/xdg/fontconfig", "/etc/profile.d", "/root/.fonts",
    "/root/.fontconfig", "/root/.fonts.conf.d", "/root/.config/fontconfig", "/root/.cache/fontconfig", "/root/.local/share/fonts")))


def hash_file(path):
    data = Path(path).read_bytes()
    return dict(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))


def main():
    ledgers = {phase: json.loads(gzip.decompress((OUT / ("KNOWN_INPUTS_" + phase + ".json.gz")).read_bytes()))
               for phase in ("BEFORE", "AFTER")}
    std = {STDLIB}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [n for n in folders if n not in {"site-packages", "dist-packages", "__pycache__"}]
        std.update(Path(directory) / n for n in files if not n.endswith((".pyc", ".pyo")))
    runtime = std | TOOLS | set(LIB_ROOTS)
    for base in LIB_ROOTS:
        paths = base.glob("*") if base == Path("/usr/local/lib") else base.rglob("*")
        runtime.update(p for p in paths if p.is_file() and (p.name.endswith(".so") or ".so." in p.name))
    recursive = {}
    for name, roots in (("tex", TEX_ROOTS), ("configuration", CONFIG_ROOTS)):
        selected = set(roots)
        for base in roots:
            if base.is_dir():
                selected.update(base.rglob("*"))
        recursive[name] = selected
    fixed = set(map(Path, ("/etc/ld.so.cache", "/etc/ld.so.conf", "/etc/ld.so.preload", "/etc/locale.conf",
        "/etc/default/locale", "/etc/nsswitch.conf", "/etc/localtime", "/etc/bash.bashrc", "/etc/profile",
        "/etc/passwd", "/etc/group", "/etc/fonts/local.conf", "/usr/lib/locale/locale-archive", "/root/.fonts.conf",
        "/root/.config/fontconfig/fonts.conf", "/usr/lib/python310.zip", "/usr/bin/pyvenv.cfg", "/usr/pyvenv.cfg")))
    for base in (Path("/usr/bin"), Path("/usr/lib")):
        fixed.update(base / n for n in ("python._pth", "python3._pth", "python310._pth", "python3.10._pth"))
    fixed.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    config_values = {k: sysconfig.get_config_var(k) for k in ("LDLIBRARY", "INSTSONAME")}
    fixed.update(STDLIB.parent / (v + "._pth") for v in config_values.values() if v)
    ldd = Path("/usr/bin/ldd").read_text()
    match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    assert ldd.startswith("#!/bin/bash\n") and match is not None
    fixed.update(map(Path, match.group(1).split()))
    original = dict(runtime=runtime, tex=recursive["tex"], configuration=recursive["configuration"] | fixed)
    comparisons = {}
    omitted = set()
    for phase, ledger in ledgers.items():
        failed = dict(runtime=runtime, tex=recursive["tex"], configuration=recursive["configuration"] |
            {Path(p) for p in ledger["configuration"] if not any(Path(p).is_relative_to(b) for b in CONFIG_ROOTS)})
        comparisons[phase] = {}
        for group in ("runtime", "tex", "configuration"):
            historical = set(ledger[group])
            current_original = {str(p) for p in original[group]}
            current_failed = {str(p) for p in failed[group]}
            comparisons[phase][group] = dict(historical_count=len(historical), original_rule_count=len(current_original),
                failed_rule_count=len(current_failed), original_rule_missing=sorted(historical - current_original),
                original_rule_unexpected=sorted(current_original - historical),
                failed_rule_missing=sorted(historical - current_failed), failed_rule_unexpected=sorted(current_failed - historical))
            omitted.update(historical - current_failed)
    details = {}
    for spelling in sorted(omitted):
        path = Path(spelling)
        details[spelling] = dict(before=ledgers["BEFORE"]["configuration"].get(spelling),
            after=ledgers["AFTER"]["configuration"].get(spelling), explicitly_fixed=path in fixed,
            currently_exists=path.exists(), currently_lexists=os.path.lexists(path), currently_resolved=str(path.resolve()),
            recursive_parent_roots=[str(b) for b in CONFIG_ROOTS if path.is_relative_to(b)])
    sources = [Path(__file__), QA / "batch_terminal_build_preparation/build_four.py",
        QA / "batch_four_build_original_preparation/inspect_four_builds.py", Path("/usr/bin/python3.10"),
        Path("/usr/bin/ldd"), Path(sysconfig.__file__), Path(sysconfig.get_makefile_filename()),
        Path(sysconfig.get_config_h_filename()), STDLIB / "_sysconfigdata__x86_64-linux-gnu.py"]
    sources += [OUT / ("KNOWN_INPUTS_" + phase + ".json.gz") for phase in ("BEFORE", "AFTER")]
    print(json.dumps(dict(status="BOUNDED_SELECTION_DIAGNOSIS_ONLY", ledgers_equal=ledgers["BEFORE"] == ledgers["AFTER"],
        groups=comparisons, omitted_path_details=details, fixed_candidate_count=len(fixed),
        sysconfig_values=config_values, ldd_RTLDLIST=match.group(1).split(), source_pins={str(p): hash_file(p) for p in sources},
        scope="Only original defined candidate path selection was enumerated; no host-file content inventory, build, original/corrected inspector run or acceptance."), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
