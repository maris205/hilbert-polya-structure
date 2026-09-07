#!/usr/bin/env python3
"""Second mechanism query on the already prefiltered original-note set."""
import json
import pathlib
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

scope = record.OWN / 'DISCOVERY_SCOPE.json'
selected = [pathlib.Path(p) for p in json.loads(scope.read_text())['selected_paths']]
pattern = 'whirl|winch|cyclic.{0,30}(legal|admiss|feasi|increm)|successor.{0,30}(legal|admiss)|parallel.{0,30}toggl|simultaneous.{0,30}toggl|P.?partition|order.revers.{0,30}label'
run = record.capture('08_whirling_history', ['rg', '-n', '-i', pattern, '--'] + [str(p) for p in selected],
    [pathlib.Path(__file__).resolve(), scope] + selected)
print(run.stdout.decode(), end='')
print(run.stderr.decode(), end='', file=sys.stderr)
assert run.returncode in (0, 1)
