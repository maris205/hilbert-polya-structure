"""Document paths scanned beyond stated history exclusions; no science reads."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
first = json.loads((BASE / 'evidence_capture/history_selected.json').read_text())
second = json.loads((BASE / 'evidence_capture_02/history_selected.json').read_text())
exposure = [p for p in first if any(t in p.lower() for t in ('/papers/208-', '/order_geometry_tenth'))]
record = dict(first_selected=len(first), corrected_selected=len(second),
    excluded_scientific_paths_scanned=len(exposure), exact_paths=exposure,
    corrected_remaining_excluded=[p for p in second if any(t in p.lower() for t in
        ('/papers/208-', '/order_geometry_tenth', '/p208', '/ofs', '/fth_gate/', '/reviews/'))],
    interpretation='All exact_paths were read by first rg process; this author did not open their complete bodies or import kernels. No independence or P208 review is claimed.')
target = BASE / 'evidence_capture/EXACT_ADDITIONAL_EXPOSURE.json'
with target.open('x') as out:
    out.write(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps({k:v for k,v in record.items() if k != 'exact_paths'}, indent=2, sort_keys=True))
