#!/usr/bin/env python3
"""Two original MPL executions with pinned stdlib origins and raw cmp."""
import hashlib
import importlib.util
import json
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
SELF = pathlib.Path(__file__).resolve()
OWN = SELF.parent
inputs = [SELF, OWN / 'pilot_mpl.py', OWN / 'SLATE.md', pathlib.Path(sys.executable).resolve()]
origins = {}
for name, module in sorted(sys.modules.copy().items()):
    filename = getattr(module, '__file__', None)
    if filename and pathlib.Path(filename).is_file():
        origins[name] = str(pathlib.Path(filename).resolve())
for path in sorted(set(origins.values())):
    inputs.append(pathlib.Path(path))
record.save(OWN / 'RUNTIME_ORIGINS.json', origins)
inputs.append(OWN / 'RUNTIME_ORIGINS.json')
for label in ['10_mpl_run1', '11_mpl_run2']:
    result = record.capture(label, [sys.executable, '-I', '-B', str(OWN / 'pilot_mpl.py')], inputs)
    assert result.returncode == 0
raw1 = OWN / 'commands/10_mpl_run1/stdout.raw'
raw2 = OWN / 'commands/11_mpl_run2/stdout.raw'
result = record.capture('12_mpl_raw_pair', ['cmp', str(raw1), str(raw2)], inputs + [raw1, raw2])
assert result.returncode == 0
canonical = OWN / 'CANONICAL.raw'
assert not canonical.exists()
canonical.write_bytes(raw1.read_bytes())
for label, raw in [('13_mpl_raw1_canonical', raw1), ('14_mpl_raw2_canonical', raw2)]:
    result = record.capture(label, ['cmp', str(raw), str(canonical)], inputs + [raw, canonical])
    assert result.returncode == 0
