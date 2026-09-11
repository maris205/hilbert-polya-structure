#!/usr/bin/python3.10
"""Exact scoped adapter for the 21-local plus six-paper documentary seal."""
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
BASE = QA / 'p211_author_execution_documentation01'
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
ORIGINAL = QA / 'p211_author_source_reception/source_preparation_original'
OUT = Path(__file__).resolve().parent
EXTERNAL = {'AUTHOR_EXECUTION_RECEIPT.md', 'CANONICAL_SCHEMA.md', 'HANDOFF.md', 'PREPARATION_PLAN.md', 'README.md', 'sections/5_scope.tex'}
ENV4 = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
reads, checks, native, links = {}, 0, [], []


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def pin(raw):
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    value = pin(raw)
    check(str(path) not in reads or reads[str(path)] == value, ('drift', str(path)))
    reads[str(path)] = value
    return raw


def data(path):
    return json.loads(read(path))


def put(name, value):
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with p.open('xb') as f:
        f.write(raw)


def parse(raw):
    rows = {}
    for line in raw.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        check(m is not None, 'sha list grammar')
        digest, name = m.groups()
        check(name not in rows, 'unique sha path')
        rows[name] = digest
    return rows


manifest = read(BASE / 'MANIFEST.sha256')
check(pin(manifest)['sha256'] == '82a3e951435019691571090eed85dd2ce6d515f4ff12a1c375167028d54af0bd', 'immutable documentary seal')
rows = parse(manifest)
prefix = '../../../../papers/211-kernel-image-projection-feedback/'
external, local = {}, {}
for name, digest in rows.items():
    if name.startswith(prefix):
        external[name[len(prefix):]] = digest
        check(name[len(prefix):] in EXTERNAL, 'exact allowed external output')
    else:
        check(not Path(name).is_absolute() and '..' not in Path(name).parts and name != 'MANIFEST.sha256', 'safe local payload')
        local[name] = digest
    check(pin(read((BASE / name).resolve()))['sha256'] == digest, 'full payload bytes')
check(set(external) == EXTERNAL and len(local) == 21 and len(rows) == 27, 'exact 21+6 layout')
check({p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()} == set(local) | {'MANIFEST.sha256'}, 'complete local nonself inventory')
for filename, count in [('PROTECTED_INPUTS.sha256', 52), ('EVIDENCE_INPUTS.sha256', 29)]:
    pins = parse(read(BASE / filename))
    check(len(pins) == count, 'exact pin-list count')
    for name, digest in pins.items():
        check(not Path(name).is_absolute() and '..' not in Path(name).parts, 'workspace input path')
        check(pin(read(ROOT / name))['sha256'] == digest, 'complete current input pin')
mapping = data(BASE / 'ORIGINAL_MAPPING.json')['copies']
check(len(mapping) == 5, 'five exact old copies')
for row in mapping:
    check(read(ROOT / row['physical_copy']) == read(ROOT / row['root_preparation_original']) and
          pin(read(ROOT / row['physical_copy']))['sha256'] == row['sha256'], 'physical old source mapping')
    current = ROOT / row['source']
    label = Path(row['source']).name
    argv = ['/usr/bin/diff', '-u', str(ROOT / row['physical_copy']), str(current)]
    result = subprocess.run(argv, cwd=ROOT, env=ENV4, stdin=subprocess.DEVNULL, capture_output=True, timeout=30)
    put('native/' + label + '/stdout.raw', result.stdout)
    put('native/' + label + '/stderr.raw', result.stderr)
    record = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV4, 'native_exit_code': result.returncode,
              'stdout': pin(result.stdout), 'stderr': pin(result.stderr)}
    put('native/' + label + '/RECEIPT.json', record)
    check(result.returncode == 1 and result.stderr == b'', 'actual documentary native diff')
    native.append(record)
current = {p.relative_to(PAPER).as_posix(): pin(read(p)) for p in PAPER.rglob('*') if p.is_file()}
original = {p.relative_to(ORIGINAL).as_posix(): pin(read(p)) for p in ORIGINAL.rglob('*') if p.is_file()}
check(len(original) == 28 and len(current) == 30, 'current paper versus original inventory')
check(set(current) - set(original) == {'CANONICAL.json', 'AUTHOR_EXECUTION_RECEIPT.md'}, 'exact two later additions since preparation')
changed = sorted(name for name in original if current[name] != original[name])
check(changed == sorted(EXTERNAL - {'AUTHOR_EXECUTION_RECEIPT.md'}), 'only five authorized original files changed')
schema = read(PAPER / 'CANONICAL_SCHEMA.md').decode()
old_schema = read(ORIGINAL / 'CANONICAL_SCHEMA.md').decode()
core_start, core_end = 'Serialization is exactly', 'The fresh canonical is the complete actual stdout'
check(schema[schema.index(core_start):schema.index(core_end)] == old_schema[old_schema.index(core_start):old_schema.index(core_end)], 'entire schema core unchanged')
old_scope, new_scope = read(ORIGINAL / 'sections/5_scope.tex').decode(), read(PAPER / 'sections/5_scope.tex').decode()
check(re.findall(r'\\[A-Za-z]+', old_scope) == re.findall(r'\\[A-Za-z]+', new_scope), 'TeX control sequence order')
check(old_scope[old_scope.index('The scope is the exact clock'):] == new_scope[new_scope.index('The scope is the exact clock'):], 'all terminal limitations unchanged')
delta = data(QA / 'p211_initial_build_binding01/SOURCE_LOCK_DELTA.json')
check(delta['before'] == pin(old_scope.encode()) and delta['after'] == pin(new_scope.encode()) and
      delta['TeX_macro_sequence_and_source_graph_identical'] and delta['all_other_candidate_fields_identical'], 'received exact source-only binding delta')
old_plan, new_plan = read(ORIGINAL / 'PREPARATION_PLAN.md').decode(), read(PAPER / 'PREPARATION_PLAN.md').decode()
start, end = '## 4. Exact TeX source/build design', '## 5. Downstream gates'
check(old_plan[old_plan.index(start):old_plan.index(end)] == new_plan[new_plan.index(start):new_plan.index(end)], 'build design unchanged')
for name in EXTERNAL:
    if not name.endswith('.md'):
        continue
    p = PAPER / name
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', read(p).decode()):
        if target.startswith(('https://', 'http://', '#', 'mailto:')):
            continue
        q = (p.parent / unquote(target.split('#', 1)[0])).resolve()
        check(q.is_relative_to(ROOT) and q.exists(), ('local link', str(p), target))
        links.append({'document': str(p), 'target': target, 'resolved': str(q)})
checks_report = data(BASE / 'FINAL_CHECKS.json')
check(checks_report['paper_delta']['changed'] == ['papers/211-kernel-image-projection-feedback/' + n for n in changed], 'actual reported paper delta')
check(all(checks_report['predicates'].values()), 'documentary predicate report')
for path, expected in reads.items():
    check(pin(Path(path).read_bytes()) == expected, 'whole reception input set unchanged')
put('INPUTS.json', reads)
put('LINKS.json', links)
result = {'status': 'ROOT_RECEIVED_EXACT_EXECUTION_DOCUMENTARY_DELTA', 'checks': checks,
          'read_paths': len(reads), 'payloads': len(rows), 'payload_bytes': sum((BASE / n).resolve().stat().st_size for n in rows),
          'protected_pins': 52, 'evidence_pins': 29, 'physical_old_copies': len(mapping),
          'native_diffs': len(native), 'changed_originals': changed, 'link_occurrences': len(links),
          'unique_link_targets': len({v['resolved'] for v in links}), 'scientific_executions': 0, 'builds': 0}
put('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
