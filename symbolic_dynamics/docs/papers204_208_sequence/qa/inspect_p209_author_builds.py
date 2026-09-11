#!/usr/bin/env python3
"""Read-only root inspection of the two already completed P209 author builds.

This reads existing artifacts and current dependencies, and runs raw cmp.
It does not run a compiler, mathematical producer, renderer or page viewer.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
EXPECTED = ('main.tex', 'math_commands.tex', 'references.bib',
            'sections/00_abstract.tex', 'sections/01_setup.tex',
            'sections/02_recurrence.tex', 'sections/03_inverse.tex', 'sections/04_scope.tex')


def require(value, *detail):
    if not value:
        raise RuntimeError(detail)


def info(raw):
    p = Path(raw)
    h = hashlib.sha256()
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return dict(sha256=h.hexdigest(), bytes=p.stat().st_size,
                resolved=str(p.resolve()), symlink=os.readlink(p) if p.is_symlink() else None)


def j(p):
    return json.loads(p.read_text())


def agrees(p, expected):
    actual = info(p)
    require(all(actual.get(k) == v for k, v in expected.items()), 'PIN', str(p))


def manifest(base):
    names = {}
    for line in (base / 'SHA256SUMS').read_text().splitlines():
        h, n = line.split('  ', 1)
        require(re.fullmatch('[0-9a-f]{64}', h) and n not in names and
                n != 'SHA256SUMS' and not Path(n).is_absolute() and '..' not in Path(n).parts,
                'MANIFEST_SYNTAX', str(base), n)
        require(not (base / n).is_symlink(), 'PAYLOAD_SYMLINK', n)
        agrees(base / n, {'sha256': h})
        names[n] = h
    require(set(names) == {str(p.relative_to(base)) for p in base.rglob('*')
                          if p.is_file() and p != base / 'SHA256SUMS'}, 'MANIFEST_COVERAGE', str(base))
    return {'payloads': len(names), 'seal': info(base / 'SHA256SUMS')}


def main():
    known, builds, seals = {}, [], {}
    for label in ('01', '02'):
        base = PAPER / ('author_build_' + label)
        outer = PAPER / ('launcher_author_build_' + label)
        for directory, count in ((base, 680), (outer, 10)):
            seals[str(directory)] = manifest(directory)
            require(seals[str(directory)]['payloads'] == count, 'PAYLOAD_COUNT', str(directory))
        r, launch = j(base / 'RECEIPT.json'), j(outer / 'RECEIPT.json')
        require(r['status'] == 'PASS_AUTHOR_BUILD' and r['failures'] == [], 'BUILD_RECEIPT', label)
        require(launch['status'] == 'PASS_LAUNCH' and launch['exit'] == 0 and
                launch['inputs_unchanged'] and launch['outcome'] == 'COMPLETED' and
                launch['cache_absent'] and launch['failure'] is None, 'LAUNCH', label)
        agrees(base / 'SHA256SUMS', launch['recorder_seal'])
        for name in ('recorder.stdout', 'recorder.stderr'):
            agrees(outer / name, launch[name + '_pin'])
        counts = {}
        for directory, x, y in ((base, 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json', 'ALL_INPUTS_AFTER.json'),
                                 (base, 'RUNTIME_BEFORE.json', 'RUNTIME_AFTER.json'),
                                 (outer, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')):
            d = j(directory / x)
            require(d == j(directory / y), 'BEFORE_AFTER', str(directory), x)
            counts[x] = len(d)
            for n, v in d.items():
                require('error' not in v, 'INPUT_ERROR', n)
                if n in known:
                    require(all(known[n].get(k) == value for k, value in v.items()), 'CROSS_BUILD_PIN', n)
                else:
                    known[n] = v
        tex = j(base / 'TEX_RESOURCES_BEFORE.json')
        require(tex == j(base / 'TEX_RESOURCES_AFTER.json') and len(tex['files']) == 113733,
                'TEX_BEFORE_AFTER', label)
        for n, v in tex['files'].items():
            require(known.get(n) == v, 'TEX_NOT_IN_ALL_INPUTS', n)
        for n, exists in tex['roots'].items():
            require(Path(n).exists() == exists, 'TEX_ROOT_PRESENCE', n)
        # Reconstruct the exact selected TeX path set, not merely the file hashes.
        actual_tex = {str(p) for n in tex['roots'] if Path(n).is_dir()
                      for p in Path(n).rglob('*') if p.is_file()}
        require(actual_tex == set(tex['files']), 'TEX_ROOT_PATH_SET', label)
        config = j(base / 'CONFIGURATION_BEFORE.json')
        require(config == j(base / 'CONFIGURATION_AFTER.json'), 'CONFIG_BEFORE_AFTER', label)
        for n, value in config['optional'].items():
            require(Path(n).exists() == value['exists'], 'CONFIG_PRESENCE', n)
            require(Path(n).is_file() == value['is_file'] and str(Path(n).resolve()) == value['resolved'],
                    'CONFIG_FILE_OR_RESOLUTION', n)
            if value['is_file']:
                agrees(n, {k: value[k] for k in ('sha256', 'bytes', 'resolved')})
        for n, paths in config['directories'].items():
            current = sorted(str(p) for p in Path(n).rglob('*') if p.is_file()) if Path(n).is_dir() else None
            require(current == paths, 'CONFIG_PATH_SET', n)
        require(j(base / 'USER_ROOTS_BEFORE.json') == j(base / 'USER_ROOTS_AFTER.json'), 'USER_ROOTS', label)
        for v in j(base / 'USER_ROOTS_AFTER.json').values():
            require(not v['exists'] and not Path(v['path']).exists(), 'USER_ROOT_NOT_ABSENT', v)
        source = j(base / 'SOURCE_ONLY_INITIAL.json')
        require(set(source) == {str(base / 'cold_build' / n) for n in EXPECTED}, 'SOURCE_ONLY_NAMES', label)
        for n, v in source.items():
            require(known.get(n) == v, 'SOURCE_INPUT_PIN', n)
            agrees(PAPER / Path(n).relative_to(base / 'cold_build'), {k: v[k] for k in ('sha256', 'bytes')})
        used = j(base / 'CONSUMED_TEX.json')
        require(len(used) == 131, 'CONSUMED_TEX_COUNT', label)
        for n, v in used.items():
            require(all(known[n][k] == value for k, value in v.items()), 'CONSUMED_TEX_PIN', n)
        closure = j(base / 'OBSERVED_CLOSURE.json')
        require(closure['uncovered'] == closure['bytecode'] == [], 'OBSERVED_CLOSURE', label)
        rows = j(base / 'ALL_COMMAND_RECORDS.json')
        require(len(rows) == 125 and sum(row['tag'].startswith('ldd_') for row in rows) == 110,
                'COMMAND_COUNTS', label)
        for row in rows:
            c, folder = row['command'], Path(row['folder'])
            require(c['exit'] == 0 and c['process_outcome'] == 'COMPLETED' and
                    c['spawn_error'] is None and c['start_new_session'], 'ACTUAL_COMMAND', label, row['tag'])
            expected_env = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
            if not row['tag'].startswith('ldd_'):
                expected_env.update(SOURCE_DATE_EPOCH='1788652800', FORCE_SOURCE_DATE='1', openin_any='p', openout_any='p')
                expected_env.update({key: str(base / ('never_created_' + key.lower()))
                                     for key in ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR')})
            require(c['env'] == expected_env, 'COMMAND_ENV', label, row['tag'])
            for name in ('stdout', 'stderr'):
                agrees(folder / c[name], c[name + '_info'])
        rr = r['result']
        require(rr['pages'] == 4 and rr['embedded_fonts'] == 20 and
                rr['source_names'] == list(EXPECTED) and all(not v for v in rr['diagnostics'].values()),
                'BUILD_RESULT', label)
        agrees(base / 'cold_build/main.pdf', rr['pdf'])
        log, text = (base / 'cold_build/main.log').read_text(), (base / 'main.txt').read_text()
        require(not re.search(r'undefined|Overfull|Underfull|Warning|Rerun to|Please .*rerun|Label\(s\) may have changed', log), 'FINAL_LOG', label)
        require(not any(x in text for x in ('??', '[?]', '[VERIFY]')), 'PDF_TEXT_MARKER', label)
        fonts = [line.split()[-5:] for line in (base / 'pdffonts.stdout').read_text().splitlines()[2:] if line.strip()]
        require(len(fonts) == 20 and all(row[0] == 'yes' for row in fonts), 'EMBEDDED_FONTS', label)
        pngs = {str(n): info(base / 'cold_build/pages' / ('page-' + str(n) + '.png')) for n in range(1, 5)}
        builds.append({'label': label, 'pin_sets': counts, 'tex_resources': len(tex['files']),
                       'consumed_tex': len(used), 'actual_commands': len(rows), 'pdf': rr['pdf'],
                       'pages': 4, 'font_rows_all_embedded': 20, 'diagnostics': rr['diagnostics'], 'rendered_pages': pngs})
    for n, v in known.items():
        agrees(n, v)
    comparisons = []
    for name in ('main.pdf', 'pages/page-1.png', 'pages/page-2.png', 'pages/page-3.png', 'pages/page-4.png'):
        argv = ['/usr/bin/cmp', '--', str(PAPER / 'author_build_01/cold_build' / name),
                str(PAPER / 'author_build_02/cold_build' / name)]
        z = subprocess.run(argv, capture_output=True)
        comparisons.append({'argv': argv, 'exit': z.returncode, 'stdout': z.stdout.decode(), 'stderr': z.stderr.decode()})
        require(z.returncode == 0, 'ACTUAL_RAW_COMPARISON', name)
    for base, expected in seals.items():
        require(manifest(Path(base)) == expected, 'FINAL_SEAL_CHANGED', base)
    print(json.dumps({'status': 'PASS_ROOT_AUTHOR_BUILD_ARCHIVE_INSPECTION', 'builds': builds,
                      'distinct_current_input_paths_checked': len(known), 'seals': seals,
                      'actual_raw_comparisons': comparisons,
                      'boundary': 'Existing author source-only build originals and full dependencies inspected. No new root compilation or view is performed by this checker.'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
