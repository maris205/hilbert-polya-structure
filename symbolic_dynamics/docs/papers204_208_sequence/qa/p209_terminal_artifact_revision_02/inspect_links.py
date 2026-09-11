"""Static Markdown-origin/data layout inspection, not target auditor execution.

Uses a separate line-oriented Markdown scan and named origin tables. It does
not import or run any artifact-auditor function, access a website, or view an
image. Hashing the original table bytes does not certify their historical
referents; that remains the future root auditor's complete closure duty.
"""
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
HERE = Path(__file__).resolve().parent
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
A, B = [BATCH / ('reviews/p209_' + c) for c in ('a', 'b')]
PINS = {}


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    row = {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
    assert str(path) not in PINS or row == PINS[str(path)]
    PINS[str(path)] = row
    return raw


def data(path): return json.loads(read(path))


def main():
    assert HERE == BATCH / 'qa/p209_terminal_artifact_revision_02'
    origins, fixed = {}, {}
    for key, dest in data(B / 'delta_check_02/EXACT_HISTORY_ALIASES.json').items():
        origins[dest] = key.rsplit(' @ ', 1)[0]
    roles = data(A / 'delta_check_02/HISTORICAL_PIN_ROLE_MAP.json')
    for original, row in roles['exact_documentary_aliases'].items(): origins[row['preserved_exact_path']] = original
    row = roles['initial_manifest_role']; origins[row['preserved_exact_path']] = row['original_path']
    for number in range(3):
        base = PAPER / ('frozen_round' + str(number))
        meta = data(base / ('FROZEN_LINK_MAP.json' if number == 0 else 'ROUND' + str(number) + '_PROVENANCE.json'))
        if number == 0: rows = meta['links']
        else:
            rows = meta['round1_core_link_map' if number == 1 else 'round2_historical_link_map'] + meta['acceptance_and_historical_anchor_link_map']
            for row in meta['anchor_mapping'].values(): origins[str(base / row['physical_path'])] = row['original_path']
            historical = meta['historical_external_resolution'].values() if number == 1 else meta['historical_input_resolution']
            for row in historical: origins[row['round1_physical_path' if number == 1 else 'round2_physical_path']] = row['original_path']
        for row in rows: fixed[(str(base / row['document']), row['href'])] = row
    for letter in ('A', 'B'):
        for row in data(BATCH / ('qa/P209_' + letter + '_ROOT_DELTA_INSPECTION.actual.json'))['historical_input_aliases']:
            origins[row['physical_path']] = row['original_path']
    for original, row in data(A / 'delta_check_02/RESPONSE_ORIGINALS_AND_COPIES.json').items(): origins[row['copy']] = original
    for row in data(B / 'assignment_context/ROLES.json'): origins[row['preserved']] = row['original']
    for row in data(B / 'delta_intake_01/INTAKE_RESULT.json')['copies']: origins[row['physical']] = row['original']
    docs = set(p for base in (PAPER, A, B) for p in base.rglob('*.md'))
    docs.update(BATCH / n for n in ('P209_A_RESPONSE.md', 'P209_B_RESPONSE.md'))
    docs.update((BATCH / 'qa').glob('P209_*.md'))
    links, missing = [], []
    for doc in sorted(docs):
        origin = Path(origins.get(str(doc), str(doc)))
        for depth in range(12):
            earlier = origin
            for marker in ('/source_context/', '/assignment_context/', '/exact_response_inputs/', '/original_snapshot/'):
                if marker in str(origin):
                    tail = str(origin).split(marker, 1)[1]
                    if tail.startswith(('docs/', 'papers/', '.agents/')) or tail in ('AGENTS.md', 'SYMBOLIC_DYNAMICS_STATE.md'):
                        origin = ROOT / tail
                        break
            if origin == earlier: break
        assert depth < 11
        fenced, marker = False, None
        for number, line in enumerate(read(doc).decode().splitlines(), 1):
            fence = re.match(r'^[ ]{0,3}(`{3,}|~{3,})', line)
            if fence:
                if not fenced: fenced, marker = True, fence.group(1)[0]
                elif fence.group(1)[0] == marker: fenced = False
                continue
            if fenced or line.startswith(('    ', '\t')): continue
            line = re.sub(r'(`+).*?\1', '', line)
            for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', line):
                target = href.strip().strip('<>').split('#', 1)[0]
                if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target): continue
                table = fixed.get((str(doc), href))
                destination = Path(table['physical_target']) if table else (origin.parent / unquote(target)).resolve()
                row = {'document': str(doc), 'line': number, 'href': href, 'semantic_origin': str(origin),
                       'explicit_table': bool(table), 'destination': str(destination), 'exists': destination.exists()}
                links.append(row)
                if not destination.exists(): missing.append(row)
    after = {p: {'sha256': sha256(Path(p).read_bytes()).hexdigest(), 'bytes': Path(p).stat().st_size} for p in PINS}
    assert after == PINS
    report = {'scope': __doc__, 'status': 'STATIC_LINK_LAYOUT_RECORDED_NOT_ARTIFACT_GATE',
        'documents': len(docs), 'explicit_table_rows': len(fixed), 'line_scan_local_links': len(links),
        'missing': missing, 'links': links, 'original_inputs_before': PINS, 'original_inputs_after': after,
        'target_executions': 0, 'network_calls': 0, 'image_views': 0}
    with (HERE / 'LINK_LAYOUT.json').open('x') as stream: json.dump(report, stream, sort_keys=True, indent=2); stream.write('\n')
    print(json.dumps({k: report[k] for k in ('status', 'documents', 'explicit_table_rows', 'line_scan_local_links', 'missing')}, sort_keys=True))


if __name__ == '__main__': main()
