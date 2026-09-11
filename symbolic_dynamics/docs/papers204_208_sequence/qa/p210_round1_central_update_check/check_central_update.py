#!/usr/bin/env python3
"""Read-only documentary comparison, never science/build/review/terminal PASS.

Only stdout is produced. No old program is imported or executed. The exact
accepted Markdown lexer is copied below and checked against its source AST.
The caller may retain stdout inside this exclusively assigned QA directory.
"""
import ast
from collections import Counter
from datetime import datetime, timezone
import difflib
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
HERE = BATCH / 'qa/p210_round1_central_update_check'
OLD = BATCH / 'qa/central_round1_p210'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
ROUND1 = PAPER / 'frozen_round1'
PARSER = BATCH / 'qa/p209_terminal_artifact_revision_04/audit_p209.py'
CONTROLS = {'SYMBOLIC_DYNAMICS_STATE.md': ROOT / 'SYMBOLIC_DYNAMICS_STATE.md',
            **{n: BATCH / n for n in ('PIPELINE_STATE.md', 'FINAL_THEOREM_CONTRACTS.md', 'GIT_SYNC_RECEIPT.md')}}
CAPTURED = {**CONTROLS, 'P210_ROOT_LIFECYCLE.md': PAPER / 'ROOT_LIFECYCLE.md',
            'P210_PAPER_MANIFEST.sha256': PAPER / 'PAPER_MANIFEST.sha256'}
EXPECTED = dict(zip(CAPTURED, (
    '3b6e0a8c49dad394539f410e0617948249ef2fe7b2eae98598fd9e12298c5b4b',
    'aef1da0ac9efbd86d70326847ef1c16450f8bc361f002872efe44ef4d33493ed',
    '329cb32f4764dd59b1a500a8c21ef7dd4b2d83c87dd781d9934a413142f2a914',
    '3a4eaf19c452a8b6be2b2ac4bfe43fd39b3a34e2b3d5c3125e38ebd83c765ec6',
    'd1548b317d0575c4ab8c95912f9154786df79763aeebcbe63daa832de0430a7d',
    'a1abc5b290ed6a74cb6f8b1fb959f479d84926886ff9ce0b8d8179b806e6c94f')))
READS, CHECKS, FAILURES, LINKS, MANIFESTS = {}, Counter(), [], [], []


def ck(ok, category, detail):
    CHECKS[category] += 1
    if not ok:
        FAILURES.append({'category': category, 'detail': detail})
    return bool(ok)


def key(raw):
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def read(path):
    path = Path(path)
    if not ck(path.is_file() and not path.is_symlink(), 'regular_input', str(path)):
        return b''
    raw = path.read_bytes()
    pin = key(raw)
    ck(str(path) not in READS or READS[str(path)] == pin, 'input_stability', str(path))
    READS[str(path)] = pin
    return raw


def j(path):
    return json.loads(read(path))


def pin(path, wanted):
    digest = wanted if isinstance(wanted, str) else wanted['sha256']
    raw = read(path)
    ck(sha256(raw).hexdigest() == digest, 'referent_key', str(path))
    if isinstance(wanted, dict) and 'bytes' in wanted:
        ck(len(raw) == wanted['bytes'], 'referent_bytes', str(path))
    return raw


def rows(path):
    result = {}
    for line in read(path).decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        if not ck(m is not None, 'manifest_syntax', str(path)):
            continue
        digest, rel = m.groups()
        ck(rel not in result, 'manifest_unique', (str(path), rel))
        ck(not Path(rel).is_absolute() and '..' not in Path(rel).parts, 'manifest_safe_relative', rel)
        result[rel] = digest
    return result


def physical(base):
    out = set()
    for p in base.rglob('*'):
        ck(not p.is_symlink(), 'physical_no_symlink', str(p))
        if p.is_file():
            out.add(p.relative_to(base).as_posix())
    return out


def manifest(base, name, expected, complete=True):
    result = rows(base / name)
    ck(name not in result, 'manifest_nonself', str(base / name))
    ck(len(result) == expected, 'manifest_count', (str(base / name), len(result), expected))
    if complete:
        ck(set(result) == physical(base) - {name}, 'manifest_complete', str(base / name))
    for rel, digest in result.items():
        pin(base / rel, digest)
    MANIFESTS.append({'path': str(base / name), **key(read(base / name)),
                      'entries': len(result), 'complete_nonself': complete})
    return result


def stripped_links(content):
    content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
    content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
    content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)


def links(document, origin):
    total = 0
    for href in stripped_links(read(document).decode()):
        target = href.strip().strip('<>').split('#', 1)[0]
        if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
            continue
        p = (origin.parent / unquote(target)).resolve()
        exists = ck(p.exists(), 'genuine_local_link', (str(document), href, str(p)))
        row = {'document': str(document), 'semantic_origin': str(origin), 'href': href,
               'target': str(p), 'exists': exists, 'kind': 'directory' if p.is_dir() else 'file'}
        if p.is_file():
            row.update(key(read(p)))
        elif p.is_dir():
            row['direct_child_names'] = sorted(x.name for x in p.iterdir())
        LINKS.append(row)
        total += 1
    return total


def byte_section(raw, start, end):
    a = raw.index(start)
    b = raw.index(end, a) if end else len(raw)
    return raw[a:b]


def main():
    started = datetime.now(timezone.utc).isoformat()
    ck(sys.argv[1:] == ['documentary-only'], 'bounded_invocation', sys.argv)
    ck(Path(__file__).resolve() == HERE / 'check_central_update.py', 'exact_script_path', __file__)
    ck(sys.dont_write_bytecode and sys.flags.isolated and sys.flags.no_site,
       'no_import_cache_isolated_runtime', 'require -I -S -B')
    source = read(Path(__file__).resolve())
    upstream = read(PARSER)
    def extract(raw):
        return next(n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef) and n.name == 'stripped_links')
    ck(ast.dump(extract(source), include_attributes=False) == ast.dump(extract(upstream), include_attributes=False),
       'exact_accepted_parser_ast', str(PARSER))
    captures = {}
    for name, current in CAPTURED.items():
        copy = HERE / 'inputs' / name
        raw = pin(copy, EXPECTED[name])
        ck(read(current) == raw, 'captured_current_exact_bytes', str(current))
        captures[name] = {'origin': str(current), 'copy': str(copy), **key(raw)}
    manifest(OLD, 'SHA256SUMS', 6)
    preservation = j(OLD / 'PRESERVATION.actual.json')
    for record in preservation['copies']:
        raw = pin(record['copy'], record['before'])
        for k in ('before', 'after', 'copy_pin'):
            ck(record[k] == key(raw), 'original_preservation_three_keys', (record['copy'], k))
        ck(all(c['exit_code'] == 0 and c['stdout'] == c['stderr'] == '' for c in record['commands']),
           'historically_recorded_native_copy_cmp', record['copy'])
    diffs = {}
    link_counts = {}
    for name, origin in CONTROLS.items():
        old, new = read(OLD / name), read(HERE / 'inputs' / name)
        diffs[name] = ''.join(difflib.unified_diff(old.decode().splitlines(True), new.decode().splitlines(True),
                             fromfile=str(OLD / name), tofile=str(HERE / 'inputs' / name)))
        link_counts['old:' + name] = links(OLD / name, origin)
        link_counts['current:' + name] = links(HERE / 'inputs' / name, origin)
    old = read(OLD / 'FINAL_THEOREM_CONTRACTS.md')
    new = read(HERE / 'inputs/FINAL_THEOREM_CONTRACTS.md')
    contract_keys = {}
    for n in range(204, 210):
        a, b = f'## P{n} '.encode(), f'## P{n+1} '.encode()
        x, y = byte_section(old, a, b), byte_section(new, a, b)
        ck(x == y, 'unchanged_complete_contract_section', 'P' + str(n))
        contract_keys['P' + str(n)] = key(x)
    p210_old = byte_section(old, b'## P210 ', None)
    p210_new = byte_section(new, b'## P210 ', None)
    for label, start in (('P210_proof_ownership_and_theorem_exclusions', b'Proof contributors:'),
                         ('P210_exact_theorem_and_exclusions', b'For every $N\\ge1$')):
        x = byte_section(p210_old, start, b'\nPaper path:')
        y = byte_section(p210_new, start, b'\nPaper path:')
        ck(x == y, 'unchanged_p210_prepaper_block', label)
        contract_keys[label] = key(x)
    whole = manifest(PAPER, 'PAPER_MANIFEST.sha256', 1496)
    round1 = manifest(ROUND1, 'SHA256SUMS', 508)
    round0 = manifest(PAPER / 'frozen_round0', 'SHA256SUMS', 493)
    author = manifest(PAPER, 'AUTHOR_MANIFEST.sha256', 489, False)
    ck(read(PAPER / 'SHA256SUMS') == read(PAPER / 'AUTHOR_MANIFEST.sha256'),
       'author_time_seal_unchanged_role', 'not rolling whole manifest')
    meta = j(ROUND1 / 'ROUND1_PROVENANCE.json')
    prev = meta['prior_whole_manifest']
    life = meta['prior_lifecycle']
    ck(prev['original_path'] == str(PAPER / 'PAPER_MANIFEST.sha256') and
       prev['original_referent_base'] == str(PAPER) and prev['complete_before_creation_only'] is True and
       prev['current_whole_manifest_after_creation'] is False, 'old_whole_original_role', prev['original_path'])
    old_seal = ROUND1 / prev['physical_anchor']
    old_life = ROUND1 / life['physical_anchor']
    pin(old_seal, prev['sha256'])
    pin(old_life, life['sha256'])
    ck(life['original_path'] == str(PAPER / 'ROOT_LIFECYCLE.md') and
       life['old_whole_manifest_row'] == 'ROOT_LIFECYCLE.md', 'old_lifecycle_exact_role', life)
    old_rows = rows(old_seal)
    ck(len(old_rows) == 987, 'old_whole_exact_987', len(old_rows))
    ck(old_rows == prev['original_referent_pins'],
       'old_whole_all_original_roles', len(old_rows))
    for rel, digest in old_rows.items():
        pin(old_life if rel == 'ROOT_LIFECYCLE.md' else PAPER / rel, digest)
    added = {n: whole[n] for n in sorted(set(whole) - set(old_rows))}
    removed = sorted(set(old_rows) - set(whole))
    changed = {n: {'old': old_rows[n], 'current': whole[n]} for n in sorted(set(old_rows) & set(whole))
               if old_rows[n] != whole[n]}
    ck(not removed and set(changed) == {'ROOT_LIFECYCLE.md'}, 'whole_only_old_lifecycle_changed', changed)
    ck(set(added) == {'frozen_round1/' + n for n in physical(ROUND1)} and len(added) == 509,
       'whole_adds_exact_physical_round1', len(added))
    ck(meta['core_payload_pins'] == round0, 'round1_exact_493_core_pins', len(round0))
    for name, digest in round0.items():
        ck(round1[name] == digest and read(ROUND1 / name) == read(PAPER / 'frozen_round0' / name),
           'round1_unchanged_core_bytes', name)
    for name, digest in author.items():
        ck(round0[name] == digest and round1[name] == digest, '489_author_keys_unchanged', name)
    anchor_records = []
    for name, role in meta['anchors'].items():
        physical_path = ROUND1 / role['physical_path']
        pin(physical_path, role['sha256'])
        historical = name in ('PRE_ROUND1_PAPER_MANIFEST.sha256', 'PRE_ROUND1_ROOT_LIFECYCLE.md')
        if not historical:
            ck(read(physical_path) == pin(role['original_path'], role['sha256']), 'anchor_current_original_bytes', name)
        anchor_records.append({**role, 'historical_replacement_role': historical})
    ck(len(anchor_records) == 13, 'round1_13_anchors', len(anchor_records))
    frozen_link_rows = meta['round1_core_link_map'] + meta['acceptance_anchor_link_map']
    for row in frozen_link_rows:
        doc = ROUND1 / row['document']
        ck(row['href'] in stripped_links(read(doc).decode()), 'mapped_href_genuine', (str(doc), row['href']))
        pin(row['physical_target'], row['sha256'])
    link_counts['current:P210_ROOT_LIFECYCLE.md'] = links(HERE / 'inputs/P210_ROOT_LIFECYCLE.md', PAPER / 'ROOT_LIFECYCLE.md')
    # Old lifecycle is interpreted by exact Round1 anchor rows, never from the
    # deeper anchor directory and never by silently relabelling old whole scope.
    expected_life_links = stripped_links(read(old_life).decode())
    mapped_life_links = [r['href'] for r in meta['acceptance_anchor_link_map']
                         if r['document'] == life['physical_anchor']]
    ck(expected_life_links == mapped_life_links, 'historical_lifecycle_all_links_mapped', expected_life_links)
    lifecycle = read(HERE / 'inputs/P210_ROOT_LIFECYCLE.md').decode()
    ck(all(s in lifecycle for s in ('ROUND1_COMPLETE_AFTER_ACCEPTED_A', 'MANUSCRIPT_B_IN_PROGRESS',
                                   'NOT_COMPLETE', 'OWNER_AMBER', 'HOLD_EXTERNAL', 'No B', 'Round2')),
       'captured_pending_b_not_terminal', 'P210 remains not complete')
    diffs['P210_ROOT_LIFECYCLE.md'] = ''.join(difflib.unified_diff(read(old_life).decode().splitlines(True),
        lifecycle.splitlines(True), fromfile=str(old_life), tofile=str(HERE / 'inputs/P210_ROOT_LIFECYCLE.md')))
    before = dict(READS)
    for path, wanted in before.items():
        ck(key(Path(path).read_bytes()) == wanted, 'final_reread_every_file', path)
    return {'schema': 'p210-round1-central-documentary-comparison-v1',
        'status': 'DOCUMENTARY_SCOPE_CLOSED_NOT_TERMINAL_PASS' if not FAILURES else 'DOCUMENTARY_MISMATCH_FOUND',
        'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Four controls and P210 lifecycle/whole-manifest at six captured keys; no subsequent corrective Git result',
        'scientific_runs': 0, 'builds': 0, 'page_views': 0, 'old_receivers_executed': 0, 'git_commands': 0,
        'new_review_or_paper_or_five_paper_acceptance': False, 'external': 'OWNER_AMBER / HOLD_EXTERNAL',
        'source': key(source), 'accepted_markdown_parser_source': {'path': str(PARSER), **key(upstream)},
        'checks': sum(CHECKS.values()), 'checks_by_category': dict(CHECKS), 'failures': FAILURES,
        'captures': captures, 'contract_byte_keys': contract_keys, 'diffs': diffs,
        'local_link_counts': link_counts, 'local_links': LINKS, 'frozen_mapped_link_count': len(frozen_link_rows),
        'manifests': MANIFESTS, 'old_whole_role': {k: v for k, v in prev.items() if k != 'original_referent_pins'},
        'old_lifecycle_role': life, 'whole_manifest_delta': {'old_entries': len(old_rows), 'current_entries': len(whole),
        'added_exact_round1_files': added, 'removed': removed, 'changed_existing_rows': changed},
        'round1_anchor_roles': anchor_records, 'unique_file_inputs_reread': len(READS), 'input_keys': READS}


if __name__ == '__main__':
    result = main()
    print(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2))
    sys.exit(0 if not FAILURES else 1)
