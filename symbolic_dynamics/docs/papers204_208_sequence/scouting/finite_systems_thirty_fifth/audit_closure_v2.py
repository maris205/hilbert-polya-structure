#!/usr/bin/env python3
"""Read-only, bounded documentary checks. Contains no candidate implementation."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OWN = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_thirty_fifth'
EXCLUDED = {'MANIFEST.sha256', 'CLOSURE_AUDIT.actual.json'}
SUBDIRS = {'control_snapshot', 'original_snapshot', 'sources'}
BUNDLED_RG = '/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg'
checks = 0


def require(ok, description):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(description)


def pin(path):
    require(path.is_file() and not path.is_symlink() and path.resolve() == path, str(path))
    raw = path.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def read_json(name):
    return json.loads((OWN / name).read_text())


def payload():
    paths = []
    for p in sorted(OWN.iterdir()):
        require(not p.is_symlink(), 'owned symlink: ' + str(p))
        if p.is_file():
            if p.name not in EXCLUDED:
                paths.append(p)
        else:
            require(p.is_dir() and p.name in SUBDIRS, 'unexpected owned subdirectory: ' + str(p))
            for child in sorted(p.iterdir()):
                require(child.is_file() and not child.is_symlink(), 'unexpected nested payload: ' + str(child))
                paths.append(child)
    return sorted(paths)


def allowed_history(path):
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        return False
    parts = rel.parts
    if len(parts) == 3 and parts[0] == 'papers':
        match = re.match(r'^(\d+)-', parts[1])
        return bool(match and 57 <= int(match[1]) <= 207 and
                    parts[2] in {'README.md', 'main.tex', 'PROOF_PACKAGE.md'})
    if len(parts) == 5 and parts[:3] == ('docs', 'papers204_208_sequence', 'scouting'):
        return (parts[3] not in {'FTH_GATE', 'OFS_GATE', 'finite_systems_thirty_third',
                                'finite_systems_thirty_fourth', 'finite_systems_thirty_fifth'}
                and parts[4].endswith('.md')
                and not any(s in parts[4].upper() for s in ('FTH', 'OFS', 'P208', 'P209')))
    return (len(parts) == 3 and parts[0] == 'docs'
            and bool(re.fullmatch(r'papers\d+_\d+_sequence', parts[1]))
            and parts[2] in {'BREADTH_LEDGER.md', 'TITLE_COLLISION_INVENTORY.md', 'KILL_LEDGER.md'})


def main():
    require(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
            and not sys.flags.optimize, 'isolated unoptimized no-site/no-bytecode runtime')
    require(Path.cwd() == ROOT, 'workspace cwd')
    require(len(sys.argv) == 2 and sys.argv[1] in {'--manifest', '--audit'}, 'mode')
    paths = payload()
    before_payload = {str(p.relative_to(OWN)): pin(p) for p in paths}
    if sys.argv[1] == '--manifest':
        print(''.join(row['sha256'] + '  ' + name + '\n' for name, row in before_payload.items()), end='')
        return

    manifest_raw = (OWN / 'MANIFEST.sha256').read_bytes()
    manifest = {}
    for line in manifest_raw.decode().splitlines():
        require(bool(re.fullmatch(r'[0-9a-f]{64}  [^\r\n]+', line)), 'manifest syntax')
        digest, name = line.split('  ', 1)
        require(name not in manifest and not Path(name).is_absolute() and '..' not in Path(name).parts,
                'manifest unique safe relative path')
        manifest[name] = digest
    require(manifest == {name: row['sha256'] for name, row in before_payload.items()},
            'complete nonself manifest')

    searches = [read_json('HISTORY_SEARCH_01.actual.json'), read_json('HISTORY_SEARCH_02.actual.json')]
    search_inputs = searches[0]['inputs_before']
    require(len(search_inputs) == 537, 'fixed original selection count')
    for search in searches:
        require(search['selection_count'] == 537 and search['inputs_unchanged']
                and search['inputs_before'] == search_inputs == search['inputs_after'],
                'both historical before/after maps exact')
        require(search['exit'] == 0 and search['stderr'] == '' and search['stdout'],
                'successful original rg complete output recorded')
        require(search['argv'][:5] == [BUNDLED_RG, '-n', '-i', '--no-heading', '--'],
                'literal search command')
        require(search['argv'][6:] == sorted(search_inputs), 'argv covers only frozen exact originals')
        require(pin(Path(search['searcher']['path'])) ==
                {k: search['searcher'][k] for k in ('sha256', 'bytes')}, 'searcher unchanged')
        require(pin(Path(search['tool']['path'])) ==
                {k: search['tool'][k] for k in ('sha256', 'bytes')}, 'actual rg unchanged')
    for name, expected in search_inputs.items():
        require(allowed_history(Path(name)), 'exact-depth history selector: ' + name)
        require(pin(Path(name)) == expected, 'original history pin unchanged: ' + name)

    original = (OWN / 'search_originals.py').read_text()
    corrected = (OWN / 'search_originals_v2.py').read_text()
    require(original.count('/usr/bin/rg') == 3 and
            original.replace('/usr/bin/rg', BUNDLED_RG) == corrected,
            'path-only v2 adapter')
    failure = read_json('HISTORY_SEARCH_01.failed.actual.json')
    require(failure['status'] == 'DOCUMENTARY_SEARCH_CHILD_NOT_STARTED'
            and failure['result']['exit_code'] == 1
            and "FileNotFoundError: [Errno 2] No such file or directory: '/usr/bin/rg'"
            in failure['result']['output'], 'retained actual failed child startup')
    delta = read_json('SEARCHER_DIFF.actual.json')
    require(delta['exit_code'] == 1 and delta['output'].count('\n@@ ') == 2,
            'retained full two-hunk documentary diff')

    controls = []
    captured = read_json('CONTROL_CAPTURE.json')
    require(len(captured['inputs']) == 3, 'three captured control roles')
    for rel, row in captured['inputs'].items():
        origin = Path(row['original_path'])
        snap = OWN / row['physical_path']
        expected = {k: row[k] for k in ('sha256', 'bytes')}
        require(origin == ROOT / rel and pin(snap) == expected, 'original-path/oldhash control alias')
        current = pin(origin)
        equal = origin.read_bytes() == snap.read_bytes()
        require(equal == (current == expected), 'control raw equality/hash agreement')
        controls.append({'literal_original_path': str(origin), 'old_pin': expected,
                         'physical_oldhash_role': str(snap), 'current_pin': current,
                         'current_raw_equal_snapshot': equal,
                         'resolution': 'EXACT_OLDHASH_SNAPSHOT'})
    comparisons = read_json('CONTROL_COMPARISONS.actual.json')
    require(len(comparisons['commands']) == 3
            and all(c['exit_code'] == 0 and c['output'] == '' for c in comparisons['commands']),
            'three archived actual raw comparisons')

    direct = read_json('DIRECT_ORIGINAL_INPUTS.json')
    require(len(direct['inputs']) == 5 and direct['capture_exit'] == 0, 'five direct originals')
    for row in direct['inputs']:
        origin, snap = Path(row['original_path']), OWN / row['snapshot_path']
        expected = {k: row[k] for k in ('sha256', 'bytes')}
        require(pin(origin) == pin(snap) == expected, 'direct original and snapshot pins')
        require(origin.read_bytes() == snap.read_bytes(), 'direct original raw byte equality')
    require(sum(row['original_path'] in search_inputs for row in direct['inputs']) == 4,
            'four searched direct originals plus one explicitly targeted original')

    for name in ['INTAKE.md', 'PROOF_PACKAGE.md', 'SOURCE_AND_HISTORY.md', 'REPORT.md']:
        body = (OWN / name).read_text()
        require('NO_PROMOTION' in body, 'negative disposition: ' + name)
        for link in re.findall(r'\]\(([^)]+)\)', body):
            if '://' in link or link.startswith('#'):
                continue
            target = OWN / link.split('#', 1)[0]
            require(target.is_file() or target == OWN / 'CLOSURE_AUDIT.actual.json',
                    'owned documentary local link exists: ' + link)
    require('NOT CURRENTLY JUSTIFIED' in (OWN / 'PROOF_PACKAGE.md').read_text(),
            'target proof explicitly unjustified')
    for name, expected in search_inputs.items():
        require(pin(Path(name)) == expected, 'end-of-audit unchanged original: ' + name)
    require({str(p.relative_to(OWN)): pin(p) for p in payload()} == before_payload,
            'owned payload unchanged during audit')
    print(json.dumps({'schema': 'scout35-documentary-closure-v1',
                      'status': 'PASS_DOCUMENTARY_ONLY',
                      'scope': 'Fixed original-only history, snapshots, failure/diff records and complete nonself payload. Not a science run, proof certification, admission, source/value gate or review.',
                      'documentary_checks': checks,
                      'literal_definitions': 2, 'mathematical_pilots': 0,
                      'new_paper_numbers': 0, 'reserves': 0, 'promotions': 0,
                      'historical_originals': 537, 'direct_originals': 5,
                      'direct_originals_additional_to_search': 1,
                      'controls': controls,
                      'payload_file_count': len(paths),
                      'payload_bytes': sum(row['bytes'] for row in before_payload.values()),
                      'manifest_pin': {'sha256': sha256(manifest_raw).hexdigest(), 'bytes': len(manifest_raw)},
                      'manifest_excluded_exactly': sorted(EXCLUDED),
                      'environment': dict(os.environ), 'executable': sys.executable,
                      'python_version': sys.version,
                      'all_owned_payload_pins': before_payload}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
