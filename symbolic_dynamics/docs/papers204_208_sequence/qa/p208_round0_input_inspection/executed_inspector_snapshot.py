#!/usr/bin/env python3
"""Read-only inspection of actual P208 author/root evidence; no new mathematics.

Also preserves the exact seven workspace origin bytes in a new exclusive
historical context archive. Later changes to the central admission ledger
must not be hidden by pretending these historical pins describe live bytes.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
import traceback

ROOT = Path(__file__).resolve().parents[3]
PAPER = ROOT / 'papers/208-original-snapshot-triangulation-sweeps'
QA = ROOT / 'docs/papers204_208_sequence/qa'
OUT = QA / 'p208_round0_input_inspection'
counts = {}


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(p.read_bytes())


def save(p, value):
    with p.open('x', encoding='utf-8') as f:
        json.dump(value, f, sort_keys=True, indent=2)
        f.write('\n')


def pins(mapping, base):
    assert mapping
    for name, value in mapping.items():
        p = base / name
        assert p.is_file()
        expected = value['sha256'] if isinstance(value, dict) else value
        assert digest(p) == expected, str(p)
        if isinstance(value, dict) and 'bytes' in value:
            assert p.stat().st_size == value['bytes'], str(p)
    return len(mapping)


def seal(folder, name):
    entries = {}
    for line in (folder / name).read_text().splitlines():
        value, rel = line.split('  ', 1)
        p = Path(rel)
        assert not p.is_absolute() and '..' not in p.parts and rel != name
        assert rel not in entries and not (folder / p).is_symlink()
        entries[rel] = value
    pins(entries, folder)
    assert set(entries) == {p.relative_to(folder).as_posix() for p in folder.rglob('*')
                            if p.is_file() and p != folder / name}
    return len(entries)


def recorded_commands(folder, rows, root_schema=False):
    for row in rows:
        assert row['exit_code'] == 0
        assert read(folder / (row['label'] + '.command.json')) == row
        for stream in ('stdout', 'stderr'):
            info = row[stream]
            rel = info['path'] if root_schema else info
            expected = info['sha256'] if root_schema else row[stream + '_sha256']
            assert digest(folder / rel) == expected
    return len(rows)


def runtime(folder):
    for before in sorted(folder.glob('*_BEFORE.json')):
        if not before.name.startswith(('TOOLS_', 'LIBRARIES_')):
            continue
        after = before.with_name(before.name.replace('_BEFORE', '_AFTER'))
        a, b = read(before), read(after)
        assert a == b
        pins(a, Path('/'))
    if (folder / 'runtime_before.stdout').is_file():
        a, b = (folder / 'runtime_before.stdout').read_bytes(), (folder / 'runtime_after.stdout').read_bytes()
        assert a == b
        data = json.loads(a)
        assert data['optimize'] == 0 and data['isolated'] == 1 and data['dont_write_bytecode']
        for value in data['module_files'].values():
            assert digest(Path(value['path'])) == value['sha256']


def inspect():
    assert sys.flags.optimize == 0 and sys.flags.isolated == 1 and sys.dont_write_bytecode
    counts['author_manifest'] = seal(PAPER, 'AUTHOR_MANIFEST.sha256')
    assert counts['author_manifest'] == 483
    for name, producers, commands in [('initial_01', 1, 7), ('pair_01', 2, 10)]:
        d = PAPER / 'qa_author' / name
        r = read(d / 'RECEIPT.json')
        assert r['status'] == 'AUTHOR_EXECUTION_PASS' and r['validation_exception'] is None
        before, after = read(d / 'INPUTS_BEFORE.json'), read(d / 'INPUTS_AFTER.json')
        assert before == r['input_pins_before'] and after == r['input_pins_after']
        expected = dict(before)
        if producers == 1:
            assert 'CANONICAL.json' not in before
            expected['CANONICAL.json'] = digest(PAPER / 'CANONICAL.json')
        assert expected == after
        pins(before, d / 'input_snapshot')
        assert set(before) == {p.relative_to(d / 'input_snapshot').as_posix()
                               for p in (d / 'input_snapshot').rglob('*') if p.is_file()}
        counts[name + '_inputs_after'] = pins(after, PAPER)
        assert recorded_commands(d, r['commands']) == commands
        assert len(r['runs']) == producers
        for run in r['runs']:
            assert run['initial_files'] == run['final_files'] == {'verify.py': digest(PAPER / 'verify.py')}
            pins(run['final_files'], d / run['directory'])
            data = read(d / run['producer']['stdout'])
            assert data['assertions'] == 62101 and data['total_states'] == 2055
            assert (d / run['producer']['stdout']).read_bytes() == (PAPER / 'CANONICAL.json').read_bytes()
        runtime(d)
    for name in ['preparation_01', 'preparation_02', 'preparation_03']:
        d = PAPER / 'qa_build' / name
        r = read(d / 'RECEIPT.json')
        assert r['status'] == 'AUTHOR_BUILD_PREPARED_NOT_VIEWED' and r['validation_exception'] is None
        before, after = read(d / 'SOURCE_PINS_BEFORE.json'), read(d / 'SOURCE_PINS_AFTER.json')
        assert before == after == r['source_before'] == r['source_after'] == read(d / 'SOURCE_ONLY_INITIAL.json')
        assert len(before) == 11
        pins(before, d / 'source_only')
        changed = [k for k, v in before.items() if digest(PAPER / k) != v]
        assert changed == (['sections/04_extremum.tex'] if name.endswith('01') else [])
        inventory = read(d / 'TEX_RUNTIME_INVENTORY_BEFORE.json')
        consumed = read(d / 'CONSUMED_TEX_INPUTS.json')
        assert consumed == read(d / 'CONSUMED_TEX_INPUTS_AFTER.json')
        assert all(inventory[k] == v for k, v in consumed.items())
        counts[name + '_consumed'] = pins(consumed, Path('/'))
        assert len(inventory) == 105987 and len(consumed) == 146
        assert recorded_commands(d, r['commands']) == 15
        runtime(d)
        assert r['pages'] == 7 and digest(d / 'source_only/main.pdf') == r['pdf_sha256']
        fonts = read(d / 'FONT_EMBEDDING_CHECK.json')
        assert len(fonts['actual_tail_fields']) == 27 and all(f[0] == 'yes' for f in fonts['actual_tail_fields'])
        assert r['warnings']['undefined'] == []
        assert r['warnings']['underfull'] == ['Underfull \\hbox (badness 5681) in paragraph at lines 9--13']
        if name != 'preparation_01':
            assert r['warnings']['overfull'] == []
            assert (d / 'source_only/main.pdf').read_bytes() == (PAPER / 'main.pdf').read_bytes()
        else:
            assert r['warnings']['overfull'] == ['Overfull \\hbox (44.62468pt too wide) detected at line 19']
    d = QA / 'root_replays/p208_author'
    counts['root_replay_manifest'] = seal(d, 'SHA256SUMS')
    r = read(d / 'RECEIPT.json')
    assert r['status'] == 'PASS_ROOT_P208_AUTHOR_REPLAY_PAIR' and r['failures'] == []
    assert r['inputs_before'] == r['inputs_after'] == read(d / 'INPUTS_BEFORE.json') == read(d / 'INPUTS_AFTER.json')
    for key, value in r['inputs_after'].items():
        base, name = (ROOT, key.split(':', 1)[1]) if key.startswith('workspace_origin:') else (PAPER, key)
        pins({name: value}, base)
    counts['root_inputs'] = len(r['inputs_after'])
    assert counts['root_inputs'] == 491 and recorded_commands(d, r['commands'], True) == 10
    assert len(r['runs']) == 2 and all(x['assertions'] == 62101 and x['states'] == 2055 for x in r['runs'])
    runtime(d)
    comparisons = []
    for label, a, b in [
            ('author_pair', PAPER / 'qa_author/pair_01/producer_01.stdout', PAPER / 'qa_author/pair_01/producer_02.stdout'),
            ('root_pair', d / 'run1.stdout', d / 'run2.stdout'),
            ('pdf_pair', PAPER / 'qa_build/preparation_02/source_only/main.pdf', PAPER / 'qa_build/preparation_03/source_only/main.pdf')]:
        argv = ['/usr/bin/cmp', str(a), str(b)]
        result = subprocess.run(argv, capture_output=True, check=False)
        for suffix, raw in [('stdout', result.stdout), ('stderr', result.stderr)]:
            with (OUT / (label + '.' + suffix)).open('xb') as f:
                f.write(raw)
        comparisons.append({'label': label, 'argv': argv, 'exit_code': result.returncode,
                            'input_sha256': [digest(a), digest(b)], 'stdout': result.stdout.decode(),
                            'stderr': result.stderr.decode()})
        assert result.returncode == 0
    save(OUT / 'ACTUAL_RAW_COMPARISONS.json', comparisons)
    origins = {}
    for line in (PAPER / 'provenance/INPUT_ORIGINS.sha256').read_text().splitlines():
        value, name = line.split('  ', 1)
        assert name not in origins and not Path(name).is_absolute() and '..' not in Path(name).parts
        origins[name] = value
    assert len(origins) == 7
    pins(origins, ROOT)
    archive = OUT / 'historical_workspace_origins'
    archive.mkdir()
    for name, value in origins.items():
        dest = archive / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, dest)
        assert digest(dest) == value
    pins(origins, ROOT)
    with (archive / 'SHA256SUMS').open('x') as f:
        f.write(''.join(f'{v}  {k}\n' for k, v in sorted(origins.items())))
    counts['preserved_historical_origins'] = seal(archive, 'SHA256SUMS')


if __name__ == '__main__':
    OUT.mkdir(exist_ok=False)
    shutil.copyfile(__file__, OUT / 'executed_inspector_snapshot.py')
    failure = None
    try:
        inspect()
    except BaseException as error:
        failure = {'type': type(error).__name__, 'message': str(error), 'traceback': traceback.format_exc()}
    save(OUT / 'RECEIPT.json', {'status': 'PASS' if failure is None else 'FAIL',
         'kind': 'ROOT_ARTIFACT_INSPECTION_NOT_NEW_MATH_OR_BUILD_OR_VIEW',
         'ended_utc': datetime.now(timezone.utc).isoformat(), 'counts': counts,
         'failure': failure, 'external': 'HOLD_EXTERNAL'})
    with (OUT / 'SHA256SUMS').open('x') as f:
        f.write(''.join(f'{digest(p)}  {p.relative_to(OUT).as_posix()}\n'
                        for p in sorted(OUT.rglob('*')) if p.is_file()))
    print((OUT / 'RECEIPT.json').read_text())
    raise SystemExit(0 if failure is None else 1)
