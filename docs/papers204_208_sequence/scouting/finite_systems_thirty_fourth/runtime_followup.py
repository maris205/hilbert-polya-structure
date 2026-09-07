#!/usr/bin/env python3
"""Append-only import-source/cache closure and same-box reproducibility pair."""
import os
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
import pilot_mpl
SELF = pathlib.Path(__file__).resolve()
OWN = SELF.parent
origins = {}
paths = [SELF, OWN / 'pilot_mpl.py', OWN / 'SLATE.md', pathlib.Path(sys.executable).resolve()]
for name, module in sorted(sys.modules.copy().items()):
    entry = {}
    for field in ['__file__', '__cached__']:
        value = getattr(module, field, None)
        if value and pathlib.Path(value).is_file():
            path = pathlib.Path(value).resolve()
            entry[field] = str(path)
            paths.append(path)
    if entry:
        origins[name] = entry
runtime = OWN / 'RUNTIME_CLOSURE.json'
assert not runtime.exists()
record.save(runtime, dict(role='source_and_present_bytecode_origins_of_wrapper_superset',
    modules=origins, executable=str(pathlib.Path(sys.executable).resolve()),
    python_version=sys.version, flags=str(sys.flags),
    selected_environment={k: os.environ.get(k) for k in ['LANG', 'LC_ALL', 'TZ', 'PYTHONHASHSEED']},
    reused_scientific_code='pilot_mpl.py unchanged; same 873 states, not a second pilot'))
paths.append(runtime)
for label in ['19_mpl_runtime_run1', '20_mpl_runtime_run2']:
    result = record.capture(label, [sys.executable, '-I', '-B', str(OWN / 'pilot_mpl.py')], paths)
    assert result.returncode == 0
raw1 = OWN / 'commands/19_mpl_runtime_run1/stdout.raw'
raw2 = OWN / 'commands/20_mpl_runtime_run2/stdout.raw'
canonical = OWN / 'CANONICAL.raw'
for label, left, right in [('21_runtime_raw_pair', raw1, raw2),
                           ('22_runtime_raw1_canonical', raw1, canonical),
                           ('23_runtime_raw2_canonical', raw2, canonical)]:
    result = record.capture(label, ['cmp', str(left), str(right)], paths + [left, right])
    assert result.returncode == 0
