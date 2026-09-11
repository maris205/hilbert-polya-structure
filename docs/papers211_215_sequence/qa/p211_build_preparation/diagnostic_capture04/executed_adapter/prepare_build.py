#!/usr/bin/env python3
"""Diagnostic dependency selection only. Never run TeX or scientific code."""
import argparse
import ast
import json
import os
from pathlib import Path
import re
import sys
import sysconfig
import traceback

HERE = Path(__file__).resolve().parent
exec(compile((HERE / 'build_core.py').read_bytes(), str(HERE / 'build_core.py'), 'exec'))

PRIOR_KEY = ROOT / 'papers/210-weakly-increasing-run-aggregation/qa_final/CONSUMED_TEX_BEFORE.json'
ACCEPTANCE = ROOT / 'docs/papers204_208_sequence/qa/P210_TERMINAL_BUILD_ROOT_INSPECTION.md'
OLD_BUILDER = ROOT / 'docs/papers204_208_sequence/qa/p210_terminal_build_revision_02/build_p210.py'
TOOLS = tuple('/usr/bin/' + name for name in
              ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo', 'pdffonts',
               'pdftotext', 'pdftoppm', 'ldd', 'env', 'cmp', 'fc-conflist'))
CODE_NAMES = ('build_core.py', 'prepare_build.py', 'build_p211.py',
              'launch_build.py', 'static_checks.py')
# Class/style and explicit font-family additions to the actual accepted key.
# No texmf, font-tree, shared-library-tree or history recursion is used.
SEEDS = ('amsart.cls', 'amsplain.bst', 'amsmath.sty', 'amsfonts.sty',
         'amssymb.sty', 'amsthm.sty', 'fontenc.sty', 'lmodern.sty',
         'geometry.sty', 'mathtools.sty', 'booktabs.sty', 'microtype.sty',
         'hyperref.sty', 't1lmr.fd', 't1lmtt.fd', 't1lmss.fd', 'ts1lmr.fd',
         'ot1lmr.fd', 'omllmm.fd', 'omslmsy.fd', 'omxlmex.fd',
         'ot1cmr.fd', 'omlcmm.fd', 'omscmsy.fd', 'omxcmex.fd',
         'umsa.fd', 'umsb.fd', 'pdftex.map', 'texmf.cnf', 'pdflatex.fmt',
         'pdftexconfig.tex', 'updmap.cfg', 'fmtutil.cnf', 'texfonts.map')
BASE_TFMS = tuple(name + '.tfm' for name in
                 ('cmr5', 'cmr6', 'cmr7', 'cmr8', 'cmr9', 'cmr10', 'cmr12',
                  'cmr17', 'cmmi5', 'cmmi6', 'cmmi7', 'cmmi8', 'cmmi9',
                  'cmmi10', 'cmmi12', 'cmsy5', 'cmsy6', 'cmsy7', 'cmsy8',
                  'cmsy9', 'cmsy10', 'cmex10', 'msam5', 'msam7', 'msam10',
                  'msbm5', 'msbm7', 'msbm10', 'ecrm1095'))
CONFIG = ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
          '/etc/locale.conf', '/etc/default/locale', '/etc/nsswitch.conf',
          '/etc/localtime', '/etc/passwd', '/etc/group', '/etc/fonts/fonts.conf',
          '/etc/fonts/local.conf', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf',
          '/root/.fonts.conf.d', '/root/.config/fontconfig/conf.d',
          '/root/.cache/fontconfig', '/root/.fontconfig',
          '/usr/lib/locale/locale-archive', '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules',
          '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache',
          '/usr/lib/x86_64-linux-gnu/gconv/UTF-16.so',
          '/usr/lib/x86_64-linux-gnu/gconv/UTF-32.so',
          '/usr/lib/x86_64-linux-gnu/gconv/UNICODE.so',
          '/usr/lib/x86_64-linux-gnu/gconv/ISO8859-1.so',
          '/usr/lib/locale/C.utf8/LC_MESSAGES/SYS_LC_MESSAGES',
          '/usr/lib/python310.zip', '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg',
          '/dev/null', '/bin/bash', '/bin/sh')
BOUNDED_DIRS = ('/etc/ld.so.conf.d', '/etc/fonts/conf.d', '/var/cache/fontconfig',
                '/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.d',
                '/usr/share/poppler/nameToUnicode')


def discover(out):
    require(out.parent == PREP and re.fullmatch(r'discovery[0-9]+', out.name),
            'Discovery output must be a new explicit owned discovery directory')
    require(out.resolve() == out and not os.path.lexists(out), 'No discovery overwrite/retry')
    require(dict(os.environ) == ENV8 and sys.flags.isolated and sys.flags.no_site and
            sys.dont_write_bytecode and not sys.flags.optimize, 'Exact isolated diagnostic launch')
    require(Path(sys.executable).resolve() == PYTHON, 'Exact diagnostic Python')
    out.mkdir(mode=0o700)
    codes_before = {name: pin(PREP / name) for name in CODE_NAMES}
    sources_before = physical_sources()
    write_new(out / 'CODE_BEFORE.json', codes_before)
    write_new(out / 'SOURCES_BEFORE.json', sources_before)
    write_new(out / 'SOURCE_GRAPH.json', source_graph())
    write_new(out / 'HISTORICAL_INPUTS.json',
              {str(p): pin(p) for p in (PRIOR_KEY, ACCEPTANCE, OLD_BUILDER)})
    specs, reasons, calls, query_results, relative_roots, query_commands = {}, {}, [], {}, {}, {}

    def select(path, reason, members=False):
        p = Path(path)
        require(p.is_absolute(), 'Only exact absolute selected paths')
        key = str(p)
        specs.setdefault(key, {'members': False})['members'] |= members
        reasons.setdefault(key, set()).add(reason)
        # Preserve every actually encountered ancestor/link spelling, without
        # listing its siblings or inventing whole-directory coverage.
        for ancestor in (p, *p.parents):
            if ancestor.is_symlink():
                a = str(ancestor)
                specs.setdefault(a, {'members': False})
                reasons.setdefault(a, set()).add('explicit-path symlink chain')
        if p.is_symlink():
            target = str(p.resolve())
            specs.setdefault(target, {'members': False})
            reasons.setdefault(target, set()).add('resolved selected symlink')

    def command(label, argv, expected=(0,), inputs=()):
        row, raw = run_native(out, label, argv, out, inputs, expected=expected)
        calls.append(row)
        require(row['successful'], 'Diagnostic command failed: ' + label)
        return raw

    def relative_absence(role, raw):
        relative = Path(raw)
        require(relative.parts and not relative.is_absolute() and '..' not in relative.parts and
                not any(c in raw for c in '${}'), 'Unexpanded/escaping cwd-relative TeX root')
        actual = out / relative
        require(not os.path.lexists(actual), 'Diagnostic user TeX root exists')
        relative_roots[role] = {'raw': raw, 'relative': relative.as_posix(),
                                'required_state': 'ABSENT',
                                'diagnostic_cwd': str(out), 'diagnostic_entry': entry(actual)}

    def lookup(label, names, required=()):
        names = sorted(set(names))
        argv = ['/usr/bin/kpsewhich', '--progname=pdflatex', '--engine=pdftex', '--all', *names]
        raw = command(label, argv, (0, 1)).decode()
        found = {name: [] for name in names}
        for line in raw.splitlines():
            p = Path(line)
            require(p.is_absolute() and p.name in found, 'Unmapped kpse resolution: ' + line)
            found[p.name].append(line)
            select(p, label + ':' + p.name)
        query_results[label] = {'names': names, 'resolutions': found}
        query_commands[label] = argv
        require(all(found[name] for name in required),
                'Required named TeX seed absent: ' + repr([n for n in required if not found[n]]))
        return found

    status, error = 'HOLD_PREPARATION_INCOMPLETE', None
    try:
        prior = json.loads(PRIOR_KEY.read_bytes())
        require(len(prior) == 139, 'Accepted previous consumed key must have 139 paths')
        for path, expected in prior.items():
            require(pin(path) == expected, 'Historical consumed path changed: ' + path)
            select(path, 'accepted P210 consumed TeX key (candidate, not P211 observation)')
        for path in (*TOOLS, str(PYTHON), *CONFIG,
                     sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename()):
            select(path, 'explicit native/configuration seed')
        for path in BOUNDED_DIRS:
            select(path, 'bounded immediate configuration membership', True)
            p = Path(path)
            if p.is_dir():
                for child in sorted(p.iterdir()):
                    select(child, 'immediate member of ' + path)
        for base in ('/usr/bin', '/usr/lib'):
            for stem in ('python', 'python3', 'python310', 'python3.10'):
                select(Path(base) / (stem + '._pth'), 'isolated Python override candidate')
        early = runtime_sample()
        write_new(out / 'PARENT_RUNTIME_EARLY.json', early)
        for path in [*early['mapped_files'], *(v['path'] for v in early['modules'].values())]:
            select(path, 'actual early diagnostic module or mapping')
        for name in ('pdflatex', 'bibtex', 'kpsewhich'):
            command('version_' + name, ['/usr/bin/' + name, '--version'])
        for name in ('pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm'):
            command('version_' + name, ['/usr/bin/' + name, '-v'])
        for variable in ('TEXMF', 'TEXMFCNF', 'TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR',
                         'TEXMFDBS', 'TEXINPUTS', 'BIBINPUTS', 'BSTINPUTS', 'shell_escape',
                         'openin_any', 'openout_any'):
            program = 'bibtex' if variable in ('BIBINPUTS', 'BSTINPUTS') else 'pdflatex'
            argv = ['/usr/bin/kpsewhich', '--progname=' + program, '--engine=pdftex',
                    '-var-value=' + variable]
            raw = command('var_' + variable, argv, (0, 1)).decode().strip()
            query_results['var_' + variable] = raw.replace(str(out), '{COMMAND_CWD}')
            query_commands['var_' + variable] = argv
            if variable in ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR'):
                require(raw, 'Empty user TeX root')
                if Path(raw).is_absolute():
                    select(raw, 'user TeX search root required absent')
                    require(not os.path.lexists(raw), 'User TeX root exists: ' + raw)
                else:
                    relative_absence(variable, raw)
        expand_argv = ['/usr/bin/kpsewhich', '--progname=pdflatex', '--engine=pdftex', '-expand-path=$TEXMF']
        expanded = command('expanded_TEXMF', expand_argv).decode().strip()
        query_results['expanded_TEXMF'] = expanded.replace(str(out), '{COMMAND_CWD}')
        query_commands['expanded_TEXMF'] = expand_argv
        for number, item in enumerate(expanded.split(':')):
            if item:
                p = Path(item.removeprefix('!!'))
                if p.is_absolute() and not p.is_relative_to(out):
                    select(p, 'expanded search-root presence, not recursive contents')
                    select(p / 'ls-R', 'search-root filename database')
                else:
                    rel = p.relative_to(out) if p.is_absolute() else p
                    relative_absence('expanded_TEXMF_' + str(number), rel.as_posix())
        found = lookup('explicit_graph_seeds', (*SEEDS, *BASE_TFMS),
                       ('amsart.cls', 'amsplain.bst', 'pdftex.map', 'pdflatex.fmt'))
        # Parse only named/previously consumed FD files; each yielded metric
        # is looked up explicitly. No fonts directory is enumerated.
        fd_paths = {p for p in specs if p.endswith('.fd') and Path(p).is_file()}
        metrics, font_edges = set(BASE_TFMS), []
        for path in sorted(fd_paths):
            body = Path(path).read_text(errors='strict')
            names = sorted(set(re.findall(r'(?<![A-Za-z])(?:[a-z0-9]+-)?lm[a-z]+[0-9]+[a-z]*', body)))
            metrics.update(name + '.tfm' for name in names)
            font_edges.append({'fd': path, 'pin': pin(path), 'literal_metrics': names})
        metric_found = lookup('literal_fd_metrics', metrics, tuple(metrics))
        map_paths = found['pdftex.map']
        require(len(map_paths) == 1, 'Ambiguous effective pdftex map')
        mapped_names = set()
        wanted = {name[:-4] for name in metrics}
        map_lines = []
        for line in Path(map_paths[0]).read_text().splitlines():
            words = line.split()
            if words and words[0] in wanted:
                files = re.findall(r'<\[?<?([^\s<>\"]+\.(?:pfb|enc))', line)
                mapped_names.update(files)
                map_lines.append({'metric': words[0], 'line': line, 'files': files})
        lookup('selected_font_map_files', mapped_names, tuple(mapped_names))
        write_new(out / 'FONT_SELECTOR_EDGES.json', {'fd_edges': font_edges, 'map_lines': map_lines})
        # ldd's actual script interpreter and loader alternatives are explicit
        # dependencies; libraries are selected from one finite actual ldd query.
        ldd_text = Path('/usr/bin/ldd').read_text()
        match = re.search(r'^RTLDLIST="([^"]+)"', ldd_text, re.M)
        require(ldd_text.startswith('#!/bin/bash\n') and match, 'Unknown ldd script')
        for path in match.group(1).split():
            select(path, 'ldd RTLDLIST candidate')
        elf = []
        for path in sorted(specs):
            if Path(path).is_file():
                with Path(path).open('rb') as stream:
                    if stream.read(4) == b'\x7fELF':
                        elf.append(path)
        raw = command('ldd_selected_tools_modules', ['/usr/bin/ldd', *elf], inputs=elf).decode()
        require('not found' not in raw, 'Unresolved native linkage')
        for path in sorted(set(re.findall(r'(/[^\s():]+)', raw))):
            select(path, 'actual native ldd closure')
        fc = command('fontconfig_conflist', ['/usr/bin/fc-conflist']).decode()
        for line in fc.splitlines():
            match = re.match(r'^[+\-]\s+(/[^:]+):', line)
            require(match is not None, 'Unparsed fontconfig configuration line')
            select(match.group(1), 'actual fontconfig configuration resolution')
        late = runtime_sample()
        write_new(out / 'PARENT_RUNTIME_LATE.json', late)
        for path in [*late['mapped_files'], *(v['path'] for v in late['modules'].values())]:
            select(path, 'actual late diagnostic module or mapping')
        # Sources and adapter files are bound separately; they are not native
        # search candidates and cannot be smuggled through a historical key.
        records = snapshot(specs)
        lock = {'schema': 'p211-bounded-dependency-candidate-v1',
                'status': 'CANDIDATE_ONLY_PENDING_ROOT_BINDING',
                'environment': ENV8, 'selector_specs': specs, 'entries': records,
                'selection_reasons': {k: sorted(v) for k, v in sorted(reasons.items())},
                'queries': query_results, 'query_commands': query_commands, 'ldd_elf_inputs': elf,
                'cwd_relative_absence_roles': relative_roots,
                'source_observations': sources_before, 'code_observations': codes_before,
                'historical_inputs': {str(p): pin(p) for p in (PRIOR_KEY, ACCEPTANCE, OLD_BUILDER)},
                'scope': 'Explicit candidates, immediate named configuration memberships, actual parent imports/maps, native link-time ldd and future exact per-pass FLS. No recursive host inventory; no OS-hermetic, child-map, transient-dlopen or non-FLS trace claim.',
                'residual_review': ['Root must justify the finite candidate set and bind these actual bytes before any build.',
                                    'All PDF fonts must be embedded; fontconfig config/cache presence is tracked, not the whole system font tree.',
                                    'Any unknown FLS input/output or changed selector member fails and preserves the build; never expand the lock from that run.']}
        write_new(out / 'DEPENDENCY_LOCK.candidate.json', lock)
        write_new(out / 'CONFIGURATION_AFTER_SELECTION.json', snapshot(specs))
        require(snapshot(specs) == records, 'Prospective dependency key changed during closing reads')
        require(physical_sources() == sources_before, 'Physical manuscript sources changed')
        require({name: pin(PREP / name) for name in CODE_NAMES} == codes_before, 'Adapter changed during diagnostic')
        status = 'DIAGNOSTIC_CANDIDATE_WRITTEN_NO_BUILD_NO_ACCEPTANCE'
    except BaseException:
        error = traceback.format_exc()
        write_new(out / 'PARTIAL_SELECTOR.json', {'specs': specs,
                  'reasons': {k: sorted(v) for k, v in reasons.items()},
                  'queries': query_results, 'query_commands': query_commands,
                  'cwd_relative_absence_roles': relative_roots,
                  'status': 'PARTIAL_DIAGNOSTIC_NOT_A_PRELOCK'})
    write_new(out / 'SOURCES_AFTER.json', physical_sources())
    write_new(out / 'CODE_AFTER.json', {name: pin(PREP / name) for name in CODE_NAMES})
    result = {'status': status, 'error': error, 'native_commands': calls,
              'candidate_paths': len(specs), 'scientific_executions': 0,
              'tex_compilations': 0, 'visual_review': 'NOT_VIEWED',
              'root_binding': 'PENDING_ROOT_BINDING', 'build_acceptance': False}
    write_new(out / 'RESULT.json', result)
    result['seal'] = seal(out)
    print(json.dumps(result, sort_keys=True))
    return 0 if error is None else 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(discover(args.output))
