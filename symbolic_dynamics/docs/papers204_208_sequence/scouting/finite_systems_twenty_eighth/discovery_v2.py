#!/usr/bin/env python3
"""Correct remaining search scope; never rewrite original v1 searches."""
from pathlib import Path
import json
import re
import subprocess
import sys
from capture import ROOT, LANE, pin

tag, pattern = sys.argv[1:]
out = LANE / 'discovery' / tag
out.mkdir(parents=True, exist_ok=False)
argv = ['rg', '--files', '--hidden', '-g', '*.md', '-g', '*.tex', '-g', '*.py', 'papers', 'docs', 'README.md']
r = subprocess.run(argv, cwd=ROOT, capture_output=True)
(out/'filenames.stdout.txt').write_bytes(r.stdout)
(out/'filenames.stderr.txt').write_bytes(r.stderr)
(out/'filenames.command.json').write_text(json.dumps({'argv':argv,'cwd':str(ROOT),'exit_code':r.returncode},indent=2)+'\n')
excluded = re.compile(r'(?:/frozen_|/history/|/source_context/|/historical_|/inputs/|/qa/|/reviews/|/evidence_capture/|/postcheck/|/execution_|/finite_systems_twenty_eighth/|/208-|/209-|/OFS|/FTH|/p208_|/p209_|/order_geometry_tenth/|/order_geometry_tenth_desk/|/finite_systems_tenth/|/finite_systems_nineteenth/|/proof_context/)', re.I)
files = sorted(p for p in r.stdout.decode().splitlines() if not excluded.search('/'+p))
assert not any('/order_geometry_tenth/' in '/'+p or '/order_geometry_tenth_desk/' in '/'+p for p in files)
(out/'scope.json').write_text(json.dumps({'regex_exclusions':excluded.pattern,'case_insensitive':True,'files':files,'note':'Corrected remaining search only. Original v1 three searches retain their actual scope failure.'},indent=2)+'\n')
(out/'PINS_BEFORE.json').write_text(json.dumps([pin(p) for p in files],indent=2)+'\n')
(out/'ARGV.json').write_text(json.dumps(['rg','-n','-i','--',pattern,*files],indent=2)+'\n')
r = subprocess.run(['rg','-n','-i','--',pattern,*files],cwd=ROOT,capture_output=True)
(out/'stdout.txt').write_bytes(r.stdout); (out/'stderr.txt').write_bytes(r.stderr)
(out/'RESULT.json').write_text(json.dumps({'exit_code':r.returncode,'stdout_bytes':len(r.stdout),'stderr_bytes':len(r.stderr)},indent=2)+'\n')
(out/'PINS_AFTER.json').write_text(json.dumps([pin(p) for p in files],indent=2)+'\n')
print(json.dumps({'tag':tag,'searched_files':len(files),'exit_code':r.returncode,'stdout_lines':len(r.stdout.splitlines()),'path':str(out.relative_to(ROOT))}))
