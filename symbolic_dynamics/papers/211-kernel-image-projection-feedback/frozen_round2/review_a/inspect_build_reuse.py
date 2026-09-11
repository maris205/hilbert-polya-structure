"""Read-only artifact reuse check. Does not import or run any scientific code."""
import hashlib
import json
import os
from pathlib import Path
import stat

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
FREEZE = ROOT / 'papers/211-kernel-image-projection-feedback/frozen_round0'
READ_KEY = QA / 'p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json'
BUILD = QA / 'p211_initial_build_01'
CONFIG = BUILD / 'inner/CONFIGURATION_BEFORE.json'
MAPPING = QA / 'p211_initial_build_adoption01/HISTORICAL_MAPPING.json'
checks = 0


def check(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)


def pin(path):
    data = Path(path).read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads(Path(path).read_bytes())


def manifest(directory, expected_count):
    lines = (directory / 'SHA256SUMS').read_text().splitlines()
    names = []
    for line in lines:
        digest, name = line.split('  ', 1)
        check(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'digest syntax')
        check(not Path(name).is_absolute() and '..' not in Path(name).parts, 'relative manifest path')
        check(name != 'SHA256SUMS', 'nonself manifest')
        check(pin(directory / name)['sha256'] == digest, 'payload ' + str(directory / name))
        names.append(name)
    actual = sorted(str(p.relative_to(directory)) for p in directory.rglob('*')
                    if p.is_file() and p != directory / 'SHA256SUMS')
    check(names == actual, 'complete ordered membership ' + str(directory))
    check(len(names) == expected_count, 'payload count ' + str(directory))
    return pin(directory / 'SHA256SUMS')


def configuration(expected):
    for spelling, entry in expected.items():
        path = Path(spelling)
        current = {'path': spelling, 'present': path.exists(),
                   'resolved': str(path.resolve()), 'symlink': path.is_symlink()}
        if path.is_symlink():
            current['link'] = os.readlink(path)
        if path.exists():
            mode = path.stat().st_mode
            if stat.S_ISREG(mode):
                current['kind'] = 'file'
                current.update(pin(path))
            elif stat.S_ISDIR(mode):
                current['kind'] = 'directory'
                if 'members' in entry:
                    current['members'] = sorted(p.name for p in path.iterdir())
            elif stat.S_ISCHR(mode):
                current['kind'] = 'character_device'
                current['major'] = os.major(path.stat().st_rdev)
                current['minor'] = os.minor(path.stat().st_rdev)
            else:
                raise AssertionError('unexpected configuration object ' + spelling)
        check(current == entry, 'full configuration entry ' + spelling)


def main():
    historical = {row['logical_path']: row for row in read_json(MAPPING)}
    old_key = read_json(READ_KEY)
    check(len(old_key) == 1299, 'complete accepted prior read key')
    substitutions = {}
    for path, expected in old_key.items():
        if path in historical:
            row = historical[path]
            check(row['pin'] == expected, 'exact historical-key correspondence ' + path)
            physical = row['physical_original']
            substitutions[path] = physical
        else:
            physical = path
        check(pin(physical) == expected, 'complete prior read key ' + physical)
    check(len(substitutions) == 2, 'only the two historical navigation substitutions')
    expected_configuration = read_json(CONFIG)
    check(len(expected_configuration) == 843, 'complete bound configuration')
    configuration(expected_configuration)
    for relative in ('inner/CONFIGURATION_AFTER.json', 'outer/CONFIGURATION_BEFORE.json',
                     'outer/CONFIGURATION_AFTER.json'):
        check(read_json(BUILD / relative) == expected_configuration, 'saved configuration ' + relative)
    bound = read_json(QA / 'p211_initial_build_binding01/BINDING.json')
    check(pin(bound['dependency_lock']['path']) == bound['dependency_lock']['pin'], 'derived full lock')
    sources = {}
    for name, expected in bound['source_pins'].items():
        check(pin(FREEZE / name) == expected, 'reviewed source pin ' + name)
        check((FREEZE / name).read_bytes() == (BUILD / 'inner/source_only' / name).read_bytes(),
              'raw reviewed-to-built source equality ' + name)
        sources[name] = expected
    check(len(sources) == 9, 'all nine source inputs')
    measurements = read_json(BUILD / 'inner/RESULT.json')['measurements']
    check(pin(FREEZE / 'main.pdf') == measurements['pdf'], 'reviewed PDF pin')
    check((FREEZE / 'main.pdf').read_bytes() == (BUILD / 'inner/source_only/main.pdf').read_bytes(),
          'raw reviewed-to-built PDF equality')
    check(measurements['pages'] == 5, 'all five pages')
    for page in measurements['renders']:
        check(pin(page['image']) == page['pin'], 'actually viewed PNG pin')
    seals = {
        'build': manifest(BUILD, 362),
        'initial_build_audit': manifest(QA / 'p211_initial_build_independent_reception', 18),
        'freeze': manifest(FREEZE, 32),
    }
    configuration(expected_configuration)
    for path, expected in old_key.items():
        check(pin(substitutions.get(path, path)) == expected, 'after prior-key equality ' + path)
    result = {
        'status': 'UNCHANGED_ACCEPTED_BUILD_KEY_CHECKED',
        'scientific_execution': False, 'fresh_build': False,
        'visual_claim_source': 'separate actual reviewer view, not this checksum program',
        'checks': checks, 'prior_read_key_entries_checked_twice': len(old_key),
        'prior_read_key': {'path': str(READ_KEY), 'pin': pin(READ_KEY)},
        'historical_mapping': {'path': str(MAPPING), 'pin': pin(MAPPING)},
        'exact_navigation_substitutions': substitutions,
        'configuration_entries_checked_twice': len(expected_configuration),
        'configuration_key': {'path': str(CONFIG), 'pin': pin(CONFIG)},
        'binding': {'path': str(QA / 'p211_initial_build_binding01/BINDING.json'),
                    'pin': pin(QA / 'p211_initial_build_binding01/BINDING.json')},
        'dependency_lock': bound['dependency_lock'], 'sources': sources,
        'pdf': measurements['pdf'], 'render_pins': measurements['renders'],
        'manifests': seals, 'environment_of_reused_build': bound['environment'],
        'executed_checker': {'path': str(Path(__file__)), 'pin': pin(__file__)},
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
