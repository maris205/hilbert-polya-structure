#!/usr/bin/env python3
"""Pin exact header searches and selected excerpts, without broader discovery."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import scope_adapter
import record
SELF = pathlib.Path(__file__).resolve()
if sys.argv[1] == 'headers':
    label = sys.argv[2]
    paths = [record.ROOT / p for p in sys.argv[3:]]
    result = record.capture(label, ['rg', '-n', '^#|^##|ORR|HXC|NED|GCF|CTM', '--'] + [str(p) for p in paths],
                            [SELF, pathlib.Path(scope_adapter.__file__)] + paths)
    assert result.returncode in (0, 1)
elif sys.argv[1] == 'excerpt':
    label, extent, name = sys.argv[2:]
    path = record.ROOT / name
    result = record.capture(label, ['sed', '-n', extent, str(path)],
                            [SELF, pathlib.Path(scope_adapter.__file__), path])
    assert result.returncode == 0
else:
    raise SystemExit('bad mode')
