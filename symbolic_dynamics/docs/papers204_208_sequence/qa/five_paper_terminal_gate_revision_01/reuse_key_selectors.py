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

PY = {208: Path('/root/miniconda3/bin/python3.12'), 209: Path('/usr/bin/python3.10')}

STD = {208: Path('/root/miniconda3/lib/python3.12'), 209: Path('/usr/lib/python3.10')}

TEX209 = tuple(map(Path, ('/usr/share/texlive/texmf-dist', '/usr/share/texmf', '/var/lib/texmf',
    '/etc/texmf', '/usr/local/share/texmf', '/root/texmf', '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')))

TEX208 = tuple(Path('/usr/share/texlive/texmf-dist') / n for n in ('tex', 'fonts', 'web2c', 'bibtex')) + TEX209[1:]

CONF208 = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/share/fonts', '/etc/fonts', '/var/cache/fontconfig',
    '/usr/share/fontconfig', '/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/share/poppler')))

CONF209 = CONF208 + tuple(map(Path, ('/usr/lib/gconv', '/usr/local/share/fonts', '/etc/xdg/fontconfig',
    '/etc/profile.d', '/root/.fonts', '/root/.fontconfig', '/root/.fonts.conf.d', '/root/.config/fontconfig',
    '/root/.cache/fontconfig', '/root/.local/share/fonts')))

LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))

TEX_TOOLS = tuple(Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo',
    'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp'))

LOADERS = tuple(map(Path, ('/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2')))

def files_under(roots, resolved=False):
    return {str(p.resolve() if resolved else p) for base in roots if base.is_dir() for p in base.rglob('*') if p.is_file()}

def runtime_names(number, build=False):
    std, python = STD[number], PY[number]
    if number == 208:
        paths = {p for p in std.rglob('*') if p.is_file() and 'site-packages' not in p.parts and '__pycache__' not in p.parts}
        paths |= set(TEX_TOOLS if build else (Path('/usr/bin/cmp'), Path('/usr/bin/ldd')))
        paths |= {python, Path('/bin/bash')}
        return {str(p.resolve()) for p in paths}
    names = set()
    for directory, folders, files in os.walk(std):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in LIB_ROOTS:
        paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        names.update(str(p) for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    names.update(('/usr/bin/env', '/usr/bin/cmp', '/usr/bin/ldd', '/bin/bash', '/bin/sh', str(python)))
    if build: names.update(map(str, TEX_TOOLS))
    return {str(Path(p).resolve()) for p in names} if build else names

def config_names(number, build, role=''):
    python, std = PY[number], STD[number]
    paths = {Path('/etc/ld.so.cache'), Path('/etc/ld.so.conf'), Path('/etc/ld.so.preload'), *LOADERS,
             std.parent / ('python312.zip' if number == 208 else 'python310.zip')}
    if number == 208 and not build:
        paths.update(Path('/etc/ld.so.conf.d').glob('*'))
        if role == 'b':
            paths.update(python.parent / n for n in ('pyvenv.cfg', 'python._pth', 'python3._pth'))
            paths.add(python.parent.parent / 'pyvenv.cfg')
        return set(map(str, paths))
    paths.update((python.parent / 'pyvenv.cfg', python.parent.parent / 'pyvenv.cfg',
                  python.with_name(python.name + '._pth'), python.with_name('python._pth'),
                  Path('/etc/locale.conf'), Path('/etc/default/locale')))
    if number == 208:
        paths.update(CONF208 + TEX208 + TEX_TOOLS + (Path('/bin/bash'), python))
        paths.update(map(Path, files_under(CONF208)))
        return set(map(str, paths))
    paths.update(map(Path, ('/etc/nsswitch.conf', '/etc/localtime', '/etc/bash.bashrc', '/etc/profile', '/usr/lib/locale/locale-archive')))
    paths.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    for base in {python.parent, Path(sys.executable).parent, std.parent}:
        paths.update(base / n for n in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
    for key in ('LDLIBRARY', 'INSTSONAME'):
        if sysconfig.get_config_var(key): paths.add(std.parent / (sysconfig.get_config_var(key) + '._pth'))
    ldd = raw(Path('/usr/bin/ldd')).decode(); match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    need(ldd.startswith('#!/bin/bash\n') and match, 'Recorded ldd loader rule changed'); paths.update(map(Path, match.group(1).split()))
    if build:
        paths.update(CONF209 + TEX209 + TEX_TOOLS + (Path('/bin/bash'), Path('/bin/sh'), Path('/usr/bin/env'), python))
        paths.update(map(Path, ('/etc/passwd', '/etc/group', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf', '/etc/fonts/local.conf')))
        paths.update(map(Path, files_under(CONF209)))
    return set(map(str, paths))
