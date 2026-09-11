#!/usr/bin/env python3
"""Exact read-only key selector excerpt; no original program import/execution."""
import json
import os
from pathlib import Path
import re
import sys
import sysconfig

# The gate supplies these callbacks so complete input reads join its one ledger.
def need(value, rule, detail=None):
    if not value:
        raise AssertionError((rule, detail))
require = need

def raw(path):
    raise RuntimeError('Gate read callback not installed')

def text(path):
    return raw(path).decode()

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
