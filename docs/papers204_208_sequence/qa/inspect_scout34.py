#!/usr/bin/env python3
"""Root read-only closure of scout34; no candidate implementation or execution."""
from collections import Counter
from hashlib import sha256
from itertools import product
import ast
import json
import math
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OWN = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_thirty_fourth'
SEAL = 'f83d97da576e55427425cbbe7f1f36b760904d0dde9632235599ef7e661a9bd9'
CANONICAL = '68586cf26e5b9a38941f5fe6a6ec5981ce1a39c3023b8682cc49c78f335b77e7'
USED = {}
ALIASES = {}
COMPARISONS = []


def check(value, detail):
    if not value:
        raise AssertionError(detail)


def read(path):
    path = Path(path)
    check(path.is_absolute() and path.resolve() == path and path.is_file()
          and not path.is_symlink(), ('regular literal path', str(path)))
    raw = path.read_bytes()
    pin = {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
    check(str(path) not in USED or USED[str(path)] == pin, ('changed while reading', str(path)))
    USED[str(path)] = pin
    return raw


def obj(path):
    return json.loads(read(path))


def hashed(path, digest):
    raw = read(path)
    check(sha256(raw).hexdigest() == digest, ('full-byte pin', str(path), digest))
    return raw


def referent(path, digest):
    path = Path(path)
    selected = ALIASES.get((str(path), digest), path)
    return hashed(selected, digest)


def cmp(left, right):
    first, second = read(left), read(right)
    command = ['/usr/bin/cmp', str(left), str(right)]
    result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            env={'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8',
                                 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}, check=False)
    COMPARISONS.append({'argv': command, 'cwd': str(ROOT), 'exit_code': result.returncode,
                        'stdout': result.stdout.decode(), 'stderr': result.stderr.decode(),
                        'left_sha256': sha256(first).hexdigest(),
                        'right_sha256': sha256(second).hexdigest()})
    check(result.returncode == 0 and not result.stdout and not result.stderr
          and first == second, ('actual raw comparison', command))


def main():
    check(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
          and not sys.flags.optimize and Path.cwd() == ROOT, 'isolated unoptimized root invocation')
    read(Path(__file__).resolve())
    read(Path(sys.executable).resolve())
    read(Path('/usr/bin/cmp').resolve())
    for module in list(sys.modules.values()):
        name = getattr(module, '__file__', None)
        if name and Path(name).is_file():
            read(Path(name).resolve())
    manifest_raw = hashed(OWN / 'SHA256SUMS', SEAL)
    manifest = {}
    for line in manifest_raw.decode().splitlines():
        check(re.fullmatch('[0-9a-f]{64}  [^\r\n]+', line), 'manifest syntax')
        digest, name = line.split('  ', 1)
        check(name not in manifest and not Path(name).is_absolute()
              and '..' not in Path(name).parts and name != 'SHA256SUMS', 'nonself unique safe path')
        manifest[name] = digest
        hashed(OWN / name, digest)
    files = sorted(p for p in OWN.rglob('*') if p.is_file())
    check(len(manifest) == 187 and {str(p.relative_to(OWN)) for p in files}
          == set(manifest) | {'SHA256SUMS'}, 'complete physical 187-payload census')
    check(all(not p.is_symlink() for p in OWN.rglob('*')), 'no owned symlink')

    controls = obj(OWN / 'CONTROL_SNAPSHOTS.json')
    check(len(controls) == 3, 'exact three historical controls')
    for row in controls:
        original, copy = Path(row['original_path']), Path(row['copy_path'])
        check(copy == OWN / 'controls' / original.name, 'documented copy role')
        hashed(copy, row['original_copy_sha256'])
        ALIASES[(str(original), row['original_copy_sha256'])] = copy
        read(original)

    packages = sorted((OWN / 'commands').glob('*/receipt.json'))
    check(len(packages) == 26, 'exact 26 native packages')
    receipt_summary, input_rows, unique_inputs = [], 0, set()
    for receipt in packages:
        base = receipt.parent
        record = obj(receipt)
        before, after = obj(base / 'inputs_before.json'), obj(base / 'inputs_after.json')
        paths = obj(base / 'pathset.json')
        check(record['label'] == base.name and record['role'] == 'new_native_command'
              and record['exit'] == 0 and record['unchanged'] is True, ('native execution', base.name))
        check(before == after and sorted(before) == paths == sorted(set(paths))
              and len(before) == record['input_count'], ('full input maps', base.name))
        for name, digest in before.items():
            referent(name, digest)
            input_rows += 1
            unique_inputs.add(name)
        for stream in ('stdout', 'stderr'):
            hashed(base / (stream + '.raw'), record[stream + '_sha256'])
        argv = record['argv']
        check(record['cwd'] == str(ROOT), ('literal cwd', base.name))
        if argv[0] == 'sed':
            check(argv[1] == '-n' and set(argv[3:]) <= set(before), ('all sed operands pinned', base.name))
        if argv[0] == 'cmp':
            check(len(argv) == 3 and set(argv[1:]) <= set(before), ('all cmp operands pinned', base.name))
        if argv[0] == 'rg' and '-n' in argv:
            check('--' in argv and set(argv[argv.index('--') + 1:]) <= set(before),
                  ('all content search operands pinned', base.name))
        receipt_summary.append({'label': base.name, 'inputs': len(before), 'argv': argv,
                                'exit': record['exit'], 'full_before_after_verified': True})

    code = sorted(OWN.glob('*.py'))
    for path in code:
        ast.parse(read(path).decode(), filename=str(path))
    old = read(OWN / 'drafts/PROOF_PACKAGE.initial.md').decode()
    new = read(OWN / 'PROOF_PACKAGE.md').decode()
    check(old != new and '00100' in old and '00100' in new, 'actual earlier prose error preserved')
    read(OWN / 'drafts/CORRECTION.md')

    raw = hashed(OWN / 'CANONICAL.raw', CANONICAL)
    rows = [json.loads(line) for line in raw.splitlines()]
    check(len(rows) == 880 and rows[-1]['kind'] == 'total'
          and rows[-1]['states'] == 873 and rows[-1]['assertions'] == 3504, 'full canonical row census')
    summaries = []
    for n in range(1, 7):
        states = [r for r in rows if r['kind'] == 'state' and r['n'] == n]
        by_state = {tuple(r['x']): r for r in states}
        check(set(by_state) == set(product(*(range(i + 1) for i in range(n))))
              and len(states) == math.factorial(n), ('complete original state box', n))
        fibres = Counter(tuple(r['next']) for r in states)
        check(set(fibres) <= set(by_state), ('table arrow closure', n))
        for x, row in by_state.items():
            following = by_state[tuple(row['next'])]
            check(row['fibre'] == fibres[x] and row['period'] == following['period'] == 1
                  and (row['depth'] == following['depth'] + 1 if row['depth'] > 0
                       else tuple(row['next']) == x), ('archived table consistency', n, x))
        summary = [r for r in rows if r['kind'] == 'summary' and r['n'] == n]
        check(len(summary) == 1, ('one summary', n))
        summary = summary[0]
        check(summary['states'] == len(states) and summary['image'] == len(fibres)
              and summary['recurrent'] == sum(r['depth'] == 0 for r in states)
              and summary['height'] == max(r['depth'] for r in states)
              and summary['max_fibre'] == max(fibres.values())
              and summary['image_monotonicity_failures'] == [], ('full summary agrees with table', n))
        summaries.append({k: summary[k] for k in ('n', 'states', 'image', 'recurrent', 'height', 'max_fibre')})
    producers = ('10_mpl_run1', '11_mpl_run2', '19_mpl_runtime_run1', '20_mpl_runtime_run2')
    for name in producers:
        check(read(OWN / 'commands' / name / 'stdout.raw') == raw, ('entire original producer bytes', name))
    for first, second in ((producers[0], producers[1]), (producers[2], producers[3])):
        cmp(OWN / 'commands' / first / 'stdout.raw', OWN / 'commands' / second / 'stdout.raw')
    for name in producers:
        cmp(OWN / 'commands' / name / 'stdout.raw', OWN / 'CANONICAL.raw')
    for name, extent in (('cpm2017', 220), ('ifip2008', 160)):
        text_raw = read(OWN / 'sources' / (name + '.txt'))
        source = obj(OWN / 'sources' / (name + '.json'))
        hashed(OWN / 'sources' / (name + '.pdf'), source['pdf_sha256'])
        check(sha256(text_raw).hexdigest() == source['text_sha256'], 'complete extracted source text pin')
        label = '24_cpm2017_body_excerpt' if name == 'cpm2017' else '25_ifip2008_body_excerpt'
        check(read(OWN / 'commands' / label / 'stdout.raw') == b'\n'.join(text_raw.split(b'\n')[:extent]) + b'\n',
              ('actual selected primary body extent', name))

    links = []
    for doc in sorted(OWN.glob('*.md')):
        for link in re.findall(r'\]\(([^)]+)\)', read(doc).decode()):
            if link.startswith(('http:', 'https:', '#')):
                continue
            target = (doc.parent / link.split('#', 1)[0]).resolve()
            check(target.is_file() and target.is_relative_to(OWN), ('local link', str(doc), link))
            read(target)
            links.append([str(doc), link])
    for name, expected in list(USED.items()):
        check({'sha256': sha256(Path(name).read_bytes()).hexdigest(),
               'bytes': Path(name).stat().st_size} == expected, ('second current-byte pass', name))
    print(json.dumps({'schema': 'scout34-root-original-closure-v1',
        'status': 'PASS_ROOT_ORIGINAL_CLOSURE_NO_PROMOTION',
        'scope': 'Original proof/source/code read separately by root. This execution checks archived evidence only; no scientific producer, new pilot, independent admission, review, build or view.',
        'payloads': len(manifest), 'manifest_sha256': SEAL, 'canonical_sha256': CANONICAL,
        'native_packages': len(packages), 'historical_input_rows': input_rows,
        'historical_unique_inputs': len(unique_inputs), 'historical_control_aliases': controls,
        'native_receipts': receipt_summary, 'python_sources_AST_only': [p.name for p in code],
        'original_producer_runs': 4, 'checks_per_original_producer': 3504,
        'new_scientific_runs': 0, 'original_states': 873, 'complete_canonical_rows': 880,
        'fresh_raw_comparisons': COMPARISONS, 'original_box_summaries': summaries,
        'local_links': links, 'current_paths_checked_twice': len(USED), 'current_input_pins': USED,
        'literal_definitions': 3, 'original_pilots': 1, 'admissions': 0,
        'limitations': 'Weak potential clock and deducted DP/special fibres do not give the required two-axis residual. Runtime provenance remains author-pilot evidence, not paper terminal reuse.',
        'external_status': 'HOLD_EXTERNAL'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
