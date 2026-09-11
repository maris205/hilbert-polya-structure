#!/usr/bin/env python3
"""Bounded preparation metadata inventory only; no root checker or science execution."""
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_thirty_third'
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
assert Path.cwd() == ROOT

def read(name):
    return json.loads((SCOUT / name).read_text())

def manifest(name):
    raw = (SCOUT / name).read_bytes()
    pairs = [line.split('  ', 1) for line in raw.decode().splitlines()]
    return {'path': name, 'sha256': sha256(raw).hexdigest(), 'bytes': len(raw),
            'count': len(pairs), 'entry_names': [rel for digest,rel in pairs]}

commands = []
historical = defaultdict(set)
for category in ('commands', 'postcheck'):
    for directory in sorted((SCOUT / category).iterdir()):
        assert directory.is_dir() and not directory.is_symlink()
        receipt = json.loads((directory / 'receipt.json').read_text())
        paths = json.loads((directory / 'pathset.json').read_text())
        before = json.loads((directory / 'inputs_before.json').read_text())
        after = json.loads((directory / 'inputs_after.json').read_text())
        for path, digest in before.items():
            historical[path].add(digest)
        commands.append({'directory': str(directory.relative_to(SCOUT)),
                         'physical_file_names': sorted(p.name for p in directory.iterdir()),
                         'receipt': {**receipt, 'argv': receipt['argv'] if len(receipt['argv']) < 40 else receipt['argv'][:5], 'full_argv_length': len(receipt['argv'])}, 'path_count': len(paths),
                         'before_count': len(before), 'after_count': len(after),
                         'maps_equal': before == after,
                         'maps_pathset_equal': sorted(before) == sorted(after) == paths,
                         'input_paths_recorded_in_sealed_originals': True,
                         'stdout_bytes': (directory / 'stdout.raw').stat().st_size,
                         'stderr_bytes': (directory / 'stderr.raw').stat().st_size})
selected = {}
for name in ('SELECTED_ORIGINALS.json', 'SELECTED_ORIGINALS_V2.json',
             'SELECTED_ORIGINALS_FINAL.json', 'SELECTED_ORIGINALS_SCOPED.json'):
    values = read(name)
    selected[name] = {'count': len(values)}
discovery = (SCOUT / 'commands/01_path_discovery/stdout.raw').read_text().splitlines()
listed = sorted(str(p.relative_to(SCOUT)) for p in SCOUT.rglob('*') if p.is_file())
suspect = [p for p in sorted(historical)
           if any('/scouting/' + lane + '/' in p for lane in
                  ('order_geometry_tenth', 'order_geometry_tenth_desk',
                   'finite_systems_nineteenth', 'finite_systems_twentieth'))
           or '/gate/' in p or '_gate/' in p]
print(json.dumps({'schema': 'scout33-preparation-metadata-v1',
                  'status': 'METADATA_INVENTORY_ONLY_NOT_ROOT_CHECK',
                  'scout_base': str(SCOUT),
                  'seals': [manifest('SHA256SUMS'), manifest('FINAL_SHA256SUMS')],
                  'physical_scout_files': listed, 'physical_scout_file_count': len(listed),
                  'commands': commands, 'native_command_count': len(commands),
                  'external_tool_input_names': [p for p in sorted(historical) if p.startswith('/') and not p.startswith(str(ROOT) + '/')],
                  'historical_distinct_literal_names': len(historical),
                  'historical_input_references': sum(c['path_count'] for c in commands),
                  'selected': selected, 'discovered_filename_count': len(discovery),
                  'conservatively_protected_historical_names': suspect,
                  'boundary': 'Current historical scientific bodies were not read or hashed by this inventory; only scout-owned documentary metadata was opened.'},
                 indent=2, sort_keys=True))
