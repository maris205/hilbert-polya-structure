#!/usr/bin/env python3
"""Exact source-defined P210 membership excerpts for the new exact-five gate.

The driver injects its own read/check callbacks. This module does not import
or execute the old artifact reader, producers, builders or writers. Import
alone does not scan a host tree; membership functions run only in the actual
root-launched exact-five gate.
"""
import os
from pathlib import Path
import re
import sysconfig

def unbound(*args, **kwargs):
    raise RuntimeError('Exact-five driver callbacks not installed')

ck = need = raw = val = unbound

BASE_CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/lib/locale/C.utf8',
                                  '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv')))

BUILD_CONFIG_ROOTS = tuple(map(Path, ('/usr/local/share/texmf', '/root/texmf',
    '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var',
    '/usr/local/share/fonts', '/root/.fonts', '/root/.fontconfig',
    '/root/.config/fontconfig', '/root/.cache/fontconfig', '/root/.local/share/fonts',
    '/etc/xdg/fontconfig', '/etc/profile.d')))

BUILD_TREE_ROOTS = tuple(map(Path, ('/etc/texmf', '/var/lib/texmf', '/usr/share/texlive/texmf-dist',
    '/usr/share/texmf', '/etc/fonts', '/usr/share/fontconfig', '/var/cache/fontconfig',
    '/usr/share/poppler', '/usr/share/fonts')))

DATA_ROOTS = tuple(map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')))

LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))

STDLIB = Path('/usr/lib/python3.10')

TREE_ROOTS = tuple(map(Path, ('/usr/lib/python3.10', '/usr/lib/locale', '/usr/lib/x86_64-linux-gnu/gconv')))

def current_configuration(path):
    p = Path(path)
    return {'lexists': os.path.lexists(p), 'exists': p.exists(), 'is_file': p.is_file(),
            'is_dir': p.is_dir(), 'resolved': str(p.resolve()),
            'symlink': os.readlink(p) if p.is_symlink() else None}

def configuration_scope(build):
    roots = TREE_ROOTS + (BUILD_TREE_ROOTS if build else ())
    conf_roots = BASE_CONFIG_ROOTS + (BUILD_CONFIG_ROOTS if build else ())
    conf = set(LIB_ROOTS + conf_roots + roots)
    conf.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
        '/etc/locale.conf', '/etc/default/locale', '/etc/nsswitch.conf', '/etc/localtime',
        '/etc/ssl/openssl.cnf', '/usr/lib/ssl/openssl.cnf', '/usr/lib/locale/locale-archive',
        '/usr/lib/python310.zip', '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg',
        '/etc/fonts/local.conf', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf',
        sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    for base in map(Path, ('/usr/bin', '/usr/lib')):
        conf.update(base / n for n in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
    for name in ('LDLIBRARY', 'INSTSONAME'):
        value = sysconfig.get_config_var(name)
        if value:
            conf.add(Path('/usr/lib') / (value + '._pth'))
    loader = re.search(r'^RTLDLIST="([^"]+)"', raw('/usr/bin/ldd').decode(), re.M)
    ck(loader is not None, 'actual_ldd_loader_declaration')
    conf.update(map(Path, loader.group(1).split()))
    return roots, conf_roots, conf

def selected_tree_path(path, roots, conf_roots):
    p = Path(path)
    if any(p.is_relative_to(base) and p != base for base in conf_roots):
        return True
    if any(p.is_relative_to(base) and p != base for base in roots):
        if not any(x in {'__pycache__', 'site-packages', 'dist-packages'} for x in p.parts) and p.suffix not in {'.pyc', '.pyo'}:
            return True
    for base in LIB_ROOTS:
        if p.is_relative_to(base) and p != base and (p.name.endswith('.so') or '.so.' in p.name):
            if base != Path('/usr/local/lib') or len(p.relative_to(base).parts) == 1:
                return True
    return False

def current_membership(ledger, build):
    roots, conf_roots, conf = configuration_scope(build)
    ck(set(ledger['configuration']) == set(map(str, conf)), 'exact_declared_configuration_scope', build)
    for name, expected in ledger['configuration'].items():
        ck(current_configuration(name) == expected, 'current_configuration_presence_link', name)
    discovered = set()
    for base in roots:
        if base.is_dir():
            discovered.update(str(p) for p in base.rglob('*') if p.is_file() and
                not any(x in {'__pycache__', 'site-packages', 'dist-packages'} for x in p.parts)
                and p.suffix not in {'.pyc', '.pyo'})
    for base in conf_roots:
        if base.is_dir():
            discovered.update(str(p) for p in base.rglob('*') if p.is_file())
    for base in LIB_ROOTS:
        choices = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        discovered.update(str(p) for p in choices if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    fixed = {p for p in ledger['files'] if not selected_tree_path(p, roots, conf_roots)}
    current = fixed | discovered | {str(p) for p in conf if p.is_file()}
    ck(current == set(ledger['files']), 'current_selected_membership_exact',
       {'added': sorted(current - set(ledger['files'])), 'removed': sorted(set(ledger['files']) - current)})
    return {'files': len(current), 'configuration': len(conf), 'fixed_named_files': len(fixed),
            'selected_current_tree_files': len(discovered)}

def current_resources():
    names = {'/usr/bin/python3.10', '/usr/bin/cmp', '/usr/bin/ldd', '/usr/bin/env', '/bin/bash', '/bin/sh'}
    for directory, folders, files in os.walk('/usr/lib/python3.10'):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')):
        if base.is_dir():
            paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
            names.update(str(p) for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    for base in map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')):
        if base.is_dir():
            names.update(str(p) for p in base.rglob('*') if p.is_file())
    return sorted(names)

def configuration_snapshot():
    """Reconstruct exact source-defined names independently, never import runner."""
    paths = set(LIB_ROOTS + DATA_ROOTS + (STDLIB,))
    paths.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    paths.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload', '/etc/localtime', '/etc/locale.conf',
        '/etc/default/locale', '/etc/nsswitch.conf', '/etc/passwd', '/etc/group', '/etc/bash.bashrc', '/etc/profile',
        '/etc/ssl/openssl.cnf', '/usr/lib/ssl/openssl.cnf',
        '/usr/lib/locale/locale-archive', '/usr/lib/python310.zip', '/root/miniconda3/lib/python312.zip',
        '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg', '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2')))
    pth = ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth')
    for directory in (Path('/usr/bin'), Path('/usr/lib')):
        paths.update(directory / name for name in pth)
    for key in ('LDLIBRARY', 'INSTSONAME'):
        name = sysconfig.get_config_var(key)
        if name:
            paths.add(Path('/usr/lib') / (name + '._pth'))
    ldd = raw('/usr/bin/ldd').decode()
    match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    need(ldd.splitlines()[0] == '#!/bin/bash' and match is not None, 'known_ldd_script_and_loader_declaration')
    paths.update(map(Path, match.group(1).split()))
    result = {}
    for p in sorted(paths, key=str):
        row = {'lexists': os.path.lexists(p), 'exists': p.exists(), 'is_file': p.is_file(), 'is_dir': p.is_dir(),
               'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
        if p.is_file():
            row.update(val(p))
        result[str(p)] = row
    need(not result['/etc/ld.so.preload']['lexists'] and not result['/usr/lib/python310.zip']['lexists'],
         'no_preload_or_system_python_zip')
    need(all(not row['lexists'] for name, row in result.items() if name.endswith(('._pth', '/pyvenv.cfg'))),
         'no_interpreter_path_injection_files')
    return result

TERM_TOOLS = {Path('/usr/bin') / name for name in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo',
              'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp', 'env', 'python3.10')} | {Path('/bin/bash'), Path('/bin/sh')}

TERM_TEX_ROOTS = tuple(map(Path, ('/usr/share/texlive/texmf-dist', '/usr/share/texmf', '/var/lib/texmf', '/etc/texmf',
    '/usr/local/share/texmf', '/root/texmf', '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')))

TERM_CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/share/fonts', '/etc/fonts', '/var/cache/fontconfig',
    '/usr/share/fontconfig', '/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv',
    '/usr/share/poppler', '/usr/local/share/fonts', '/etc/xdg/fontconfig', '/etc/profile.d', '/root/.fonts',
    '/root/.fontconfig', '/root/.fonts.conf.d', '/root/.config/fontconfig', '/root/.cache/fontconfig', '/root/.local/share/fonts')))

TERM_NONFILES = {}

def terminal_entry(path):
    p = Path(path)
    row = dict(exists=p.exists(), symlink=p.is_symlink(), link=os.readlink(p) if p.is_symlink() else None,
               resolved=str(p.resolve()), is_file=p.is_file(), is_dir=p.is_dir())
    if row['is_file']:
        row.update(val(p))
    else:
        ck(str(p) not in TERM_NONFILES or TERM_NONFILES[str(p)] == row, 'terminal nonfile presence/link stability')
        TERM_NONFILES[str(p)] = row
    return row

def terminal_membership(snapshot):
    std = {STDLIB}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [name for name in folders if name not in {'site-packages', 'dist-packages', '__pycache__'}]
        std.update(Path(directory) / name for name in files if not name.endswith(('.pyc', '.pyo')))
    runtime = std | TERM_TOOLS | set(LIB_ROOTS)
    for base in LIB_ROOTS:
        paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        runtime.update(p for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    groups = {'runtime': {str(p) for p in runtime}}
    for name, roots in (('tex', TERM_TEX_ROOTS), ('configuration', TERM_CONFIG_ROOTS)):
        selected = set(roots)
        for base in roots:
            if base.is_dir():
                selected.update(base.rglob('*'))
        if name == 'configuration':
            selected.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
                '/etc/locale.conf', '/etc/default/locale', '/etc/nsswitch.conf', '/etc/localtime',
                '/etc/bash.bashrc', '/etc/profile', '/etc/passwd', '/etc/group', '/etc/fonts/local.conf',
                '/usr/lib/locale/locale-archive', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf',
                '/usr/lib/python310.zip', '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg')))
            for base in (Path('/usr/bin'), Path('/usr/lib')):
                selected.update(base / child for child in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
            selected.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
            for key in ('LDLIBRARY', 'INSTSONAME'):
                value = sysconfig.get_config_var(key)
                if value:
                    selected.add(STDLIB.parent / (value + '._pth'))
            body = raw('/usr/bin/ldd').decode()
            match = re.search(r'^RTLDLIST="([^"]+)"', body, re.M)
            ck(body.startswith('#!/bin/bash\n') and match is not None, 'terminal original ldd loader list rule')
            selected.update(map(Path, match.group(1).split()))
        groups[name] = {str(p) for p in selected}
    ck(set(snapshot) == set(groups) and all(set(snapshot[name]) == values for name, values in groups.items()),
       'exact source-defined current terminal candidate membership including absent fixed children')
    return {name: len(values) for name, values in groups.items()}
