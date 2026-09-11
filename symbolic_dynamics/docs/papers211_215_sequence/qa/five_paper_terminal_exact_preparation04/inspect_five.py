#!/usr/bin/env python3
"""Read-only exact-five evidence gate for P211-P215."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/qa/five_paper_terminal_exact_preparation04'
IDS = ['P211', 'P212', 'P213', 'P214', 'P215']
ROLES = {'author', 'A', 'B'}
ROUNDS = {'Round0', 'Round1', 'Round2'}
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
CACHE = ROOT / 'docs/papers211_215_sequence/qa/five_paper_terminal_exact_run01/never_created_reader_cache'
PINS = {}
CHECKS = {}


def need(condition, rule, detail=None):
    CHECKS[rule] = CHECKS.get(rule, 0) + 1
    if not condition:
        raise AssertionError({'rule': rule, 'detail': detail})


def resolve(name):
    need(type(name) is str and name and not Path(name).is_absolute(),
         'bounded workspace-relative input path', name)
    path = ROOT / name
    need(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(ROOT),
         'physical regular workspace input', name)
    return path


def read_twice(name):
    path = resolve(name)
    first = path.read_bytes()
    second = path.read_bytes()
    need(first == second, 'stable whole-byte reread', name)
    row = {'sha256': hashlib.sha256(first).hexdigest(), 'bytes': len(first)}
    old = PINS.setdefault(name, row)
    need(old == row, 'one complete pin per lexical input', name)
    return first


def json_file(name):
    return json.loads(read_twice(name), object_pairs_hook=unique_pairs)


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'unique JSON keys', key)
        result[key] = value
    return result


def manifest(name, exact_membership=True):
    data = read_twice(name)
    need(data.endswith(b'\n'), 'manifest terminal LF', name)
    base = resolve(name).parent
    rows = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'strict two-space manifest row', (name, line))
        digest, child = match.groups()
        rel = Path(child)
        need(not rel.is_absolute() and '..' not in rel.parts and child not in rows,
             'unique bounded manifest member', (name, child))
        rows[child] = digest
    if exact_membership:
        actual = {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
        own = Path(name).name
        need(own not in rows and set(rows) == actual - {own},
             'exact nonself manifest membership', name)
    for child, digest in rows.items():
        lexical = (Path(name).parent / child).as_posix()
        read_twice(lexical)
        need(PINS[lexical]['sha256'] == digest, 'manifest payload digest', lexical)


def all_paths(value):
    if value is None:
        yield None
    elif isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from all_paths(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from all_paths(item)


def zero_findings(name):
    value = json_file(name)
    text = json.dumps(value, sort_keys=True).lower()
    need(not re.search(r'"(critical|major|minor)"\s*:\s*[1-9]', text),
         'zero numeric current finding census', name)
    for key in ('current_findings', 'open_findings', 'findings_current'):
        if key in value:
            need(value[key] in ([], {}, None), 'empty authoritative current findings', name)
    need(('0' in text or '[]' in text) and ('finding' in text or 'census' in text),
         'finding record carries explicit zero/empty evidence', name)


def preparation_seal(expected):
    seal = HERE / 'SHA256SUMS'
    raw = seal.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == expected,
         'explicit preparation seal digest', expected)
    rows = {}
    for line in raw.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None and match.group(2) not in rows,
             'strict unique preparation manifest row', line)
        rows[match.group(2)] = match.group(1)
    actual = {p.name for p in HERE.iterdir() if p.is_file()} - {'SHA256SUMS'}
    need(set(rows) == actual, 'exact preparation package membership')
    for child, digest in rows.items():
        need(hashlib.sha256((HERE / child).read_bytes()).hexdigest() == digest,
             'preparation payload digest', child)


def history(binding):
    selected = set()
    markers = tuple(binding['history_markers'])
    for root_name in binding['history_roots']:
        base = ROOT / root_name
        need(base.is_dir() and not base.is_symlink(), 'physical history root', root_name)
        for path in base.rglob('*'):
            relative = path.relative_to(ROOT).as_posix()
            if path.is_file() and any(marker in relative.lower() for marker in markers):
                need(not path.is_symlink(), 'historical evidence is physical', relative)
                selected.add(relative)
    need(len(selected) >= 20, 'nonempty broad failed/HOLD/rejected history census', len(selected))
    for name in sorted(selected):
        read_twice(name)
    return sorted(selected)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--expected-preparation-sha256', required=True)
    args = parser.parse_args()
    need(Path.cwd() == ROOT and dict(os.environ) == ENV and
         sys.executable == '/usr/bin/python3.10' and sys.flags.isolated == 1 and
         sys.flags.no_site == 1 and sys.dont_write_bytecode and
         sys.pycache_prefix == str(CACHE) and not os.path.lexists(CACHE),
         'exact isolated clean read-only invocation')
    preparation_seal(args.expected_preparation_sha256)
    binding = json_file(HERE.relative_to(ROOT).joinpath('INPUT_BINDINGS.json').as_posix())
    need(binding['schema'] == 'p211-p215-exact-five-input-binding-v1' and
         binding['external'] == 'HOLD_EXTERNAL', 'binding schema and external hold')
    papers = binding['papers']
    need([paper['id'] for paper in papers] == IDS, 'exact ordered retained five')
    pending = [{'paper': paper['id'], 'path_role': path}
               for paper in papers for path in all_paths(paper) if path is None]
    need(not pending, 'all execution bindings populated', pending)
    pairs = builds = 0
    for paper in papers:
        need(set(paper['replay_pairs']) == ROLES, 'exact author/A/B replay roles', paper['id'])
        need(set(paper['freezes']) == ROUNDS, 'exact Round0/1/2 roles', paper['id'])
        need(len(paper['terminal_builds']) == 2 and
             {row['run_id'] for row in paper['terminal_builds']} == {'terminal01', 'terminal02'},
             'exact two distinct terminal run identities', paper['id'])
        pairs += len(paper['replay_pairs'])
        builds += len(paper['terminal_builds'])
        for name in paper['replay_pairs'].values():
            read_twice(name)
        for freeze in paper['freezes'].values():
            read_twice(freeze['receipt'])
            manifest(freeze['manifest'])
        for build in paper['terminal_builds']:
            data = read_twice(build['evidence']).decode(errors='replace').lower()
            need(build['run_id'] in data or ('terminal01' in data and 'terminal02' in data),
                 'terminal evidence identifies its run', (paper['id'], build['run_id']))
        views = read_twice(paper['page_views']).decode(errors='replace').lower()
        need(('view' in views or 'opened' in views) and ('page' in views or '页' in views),
             'actual final page-view receipt', paper['id'])
        need(len(paper['findings']) == 2, 'exact A/B finding records', paper['id'])
        for name in paper['findings']:
            zero_findings(name)
        final = read_twice(paper['final_qa']).decode(errors='replace')
        need(('INTERNAL_COMPLETE' in final or 'internally complete' in final.lower()) and
             'HOLD_EXTERNAL' in final, 'individual final QA completion and hold', paper['id'])
        manifest(paper['final_manifest'], exact_membership=False)
    need(pairs == 15 and builds == 10, 'exact batch replay/build cardinalities', [pairs, builds])
    indexes = [read_twice(name).decode(errors='replace') for name in binding['central_indexes']]
    for text in indexes:
        need(re.search(r'(5\s*retained\s*/\s*5\s*complete|保留\s*5\s*[／/]\s*完成\s*5)', text) is not None,
             'central exact-five completion census')
        need('HOLD_EXTERNAL' in text, 'central external hold')
    historical = history(binding)
    output = {
        'schema': 'p211-p215-exact-five-terminal-result-v1',
        'status': 'PASS_EXACT_FIVE_GATE_ROOT_ACCEPTANCE_PENDING',
        'papers': IDS,
        'accepted_replay_pairs': pairs,
        'accepted_terminal_builds': builds,
        'round_manifests': 15,
        'current_findings': {'Critical': 0, 'Major': 0, 'Minor': 0},
        'historical_failed_hold_rejected_files': historical,
        'complete_input_pins': dict(sorted(PINS.items())),
        'checks': dict(sorted(CHECKS.items())),
        'root_acceptance': False,
        'five_paper_completion': False,
        'external': 'HOLD_EXTERNAL'
    }
    print(json.dumps(output, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
