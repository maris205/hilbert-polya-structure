#!/usr/bin/env python3
"""Bounded read-only discovery of a 34-closed checkpoint and optional old QA."""
import datetime
import json
import os
from pathlib import Path
import re
import runpy
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_preparation02'
OLD = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_preparation/checkpoint.py'
old = runpy.run_path(str(OLD), run_name='inspected_readonly_helpers')
need, key, save = old['need'], old['key'], old['save']
BASE = 'f6f3560875f75025624367305b8a9328cbce712e'
TREE = '30df2d2b012b6e1567bdd2afa61c50e00a547d16'
S = 'docs/papers211_215_sequence/scouting/'
LANES = ('arithmetic_lane', 'spr_gate', 'transport_lane', 'order_geometry_lane',
         'sequence_combinatorics_lane', 'finite_function_lane', 'valley_absorption_lane',
         'incidence_rewiring_lane', 'root_profile_preflight', 'finite_allocation_lane',
         'rational_coupling_lane', 'discrete_geometry_gap_desk')
RECEPTIONS = ('TRANSPORT_GEOMETRY_RECEPTION.md', 'TRANSPORT_GEOMETRY_NATIVE.json',
 'SEQUENCE_FUNCTION_VALLEY_RECEPTION.md', 'SEQUENCE_FUNCTION_VALLEY_NATIVE.json',
 'inspect_sequence_function_valley.py', 'INCIDENCE_PROFILE_RECEPTION.md',
 'INCIDENCE_PROFILE_NATIVE.json', 'inspect_incidence_profile.py',
 'ALLOCATION_RATIONAL_GEOMETRY_RECEPTION.md', 'ALLOCATION_RATIONAL_GEOMETRY_NATIVE.json',
 'ALLOCATION_RATIONAL_GEOMETRY_FAILURE01.json', 'inspect_allocation_rational_geometry.py')
ROOTS = ('SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers211_215_sequence/PIPELINE_STATE.md',
         'docs/papers211_215_sequence/PROBLEM_ANCHOR.md', *(S + n for n in LANES),
         S + 'spr_root_reception', *(S + 'root_reception/' + n for n in RECEPTIONS))
OPTIONAL = ('docs/papers211_215_sequence/qa/private_checkpoint_preparation',
            'docs/papers211_215_sequence/qa/root_checkpoint_inspection')
CONTROL_SOURCES = {
 'SYMBOLIC_DYNAMICS_STATE.md': str((PREP / 'controls_preview34/SYMBOLIC_DYNAMICS_STATE.md').relative_to(ROOT)),
 'docs/papers211_215_sequence/PIPELINE_STATE.md': str((PREP / 'controls_preview34/PIPELINE_STATE.md').relative_to(ROOT)),
}

def inventory(roots):
    result = {}
    for name in roots:
        path = ROOT / CONTROL_SOURCES.get(name, name)
        need(path.exists() and path.resolve() == path, 'Missing/aliased explicit root: ' + name)
        files = [path] if path.is_file() else sorted(p for p in path.rglob('*') if p.is_file())
        if path.is_dir():
            need(not any(p.is_symlink() for p in path.rglob('*')), 'Symlink in selected root')
        for item in files:
            git = name if path.is_file() else str(item.relative_to(ROOT))
            old['safe_name'](git)
            need(git not in result, 'Duplicate selected name')
            result[git] = {'source': str(item.relative_to(ROOT)), **key(item)}
    return dict(sorted(result.items()))

def parse_tree(raw):
    need(not raw or raw.endswith(b'\0'), 'Truncated selected tree')
    result = {}
    for line in raw.split(b'\0')[:-1]:
        header, name = line.split(b'\t', 1)
        mode, kind, oid = header.decode().split()
        need(kind == 'blob' and mode in ('100644', '100755'), 'Unexpected selected object')
        name = old['safe_name'](name.decode())
        need(name not in result, 'Duplicate selected baseline path')
        result[name] = {'mode': mode, 'oid': oid}
    return result

def delta(values, baseline):
    need(set(baseline) <= set(values), 'Would delete a selected baseline path')
    rows = []
    for name, value in values.items():
        prior = baseline.get(name)
        unchanged = prior == {k: value[k] for k in ('mode', 'oid')}
        rows.append({'git_path': name, 'source_path': value['source'],
                     'status': '=' if unchanged else 'M' if prior else 'A',
                     'old': prior, 'new': {k: value[k] for k in ('mode', 'oid', 'bytes', 'sha256')}})
    return rows

def main():
    need(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode, 'Require -I -S -B')
    directory = PREP / 'readonly_discovery01'
    directory.mkdir(exist_ok=False)
    command = old['Commands'](directory, 'prepare')
    try:
        roles = old['protected_roles']()
        need(command.git('rev-parse', '--is-bare-repository').strip() == b'true', 'Not bare')
        need(command.git('symbolic-ref', 'HEAD').strip() == b'refs/heads/main', 'Wrong HEAD')
        need(command.git('rev-parse', 'refs/heads/main').strip().decode() == BASE, 'Wrong main')
        need(command.git('rev-parse', BASE + '^{tree}').strip().decode() == TREE, 'Wrong baseline tree')
        need(command.git('rev-parse', '--show-object-format').strip() == b'sha1', 'Wrong object format')
        need(command.git('remote').strip() == b'', 'Do not add a bare origin')
        need(command.mirror('rev-parse', 'HEAD').strip().decode() == old['MIRROR_BASE'], 'Mirror changed')
        need(command.mirror('status', '--porcelain=v1', '-z', '--untracked-files=all') == b'', 'Mirror dirty')
        need(command.mirror('remote', 'get-url', 'origin').strip().decode() == old['REMOTE'], 'Wrong explicit URL')
        identity = command.git('show', '-s', '--format=%an%x00%ae%x00%cn%x00%ce', BASE)
        need(identity.decode().rstrip('\n').split('\0') == [*old['IDENTITY'], *old['IDENTITY']], 'Wrong identity')
        values, optional = inventory(ROOTS), inventory(OPTIONAL)
        current_base = parse_tree(command.git('ls-tree', '-r', '-z', '--full-tree', BASE, '--', *ROOTS))
        optional_base = parse_tree(command.git('ls-tree', '-r', '-z', '--full-tree', BASE, '--', *OPTIONAL))
        need(values == inventory(ROOTS) and optional == inventory(OPTIONAL), 'Discovery sources changed')
        need(roles == old['protected_roles'](), 'Protected roles changed during read-only discovery')
        previous = Path('/root/symbolic-dynamics-closed-scout-checkpoint-bllqdh27')
        previous_keys = ['RUN.json', 'PLAN.json', 'executed_source.py',
                         'capture/MANIFEST.sha256', 'stage/MANIFEST.sha256',
                         'commit/MANIFEST.sha256', 'push/MANIFEST.sha256',
                         'frozen/SYMBOLIC_DYNAMICS_STATE.md',
                         'frozen/docs/papers211_215_sequence/PIPELINE_STATE.md']
        boundary = {str(previous / p): key(previous / p) for p in previous_keys}
        capacity = {}
        for path in (ROOT, Path('/root'), old['BARE']):
            stat = os.statvfs(path)
            capacity[str(path)] = {'available_bytes': stat.f_bavail * stat.f_frsize,
                                   'total_bytes': stat.f_blocks * stat.f_frsize}
        result = {
            'schema': 'documentary-exact-delta-discovery-v1',
            'status': 'PREPARATION_ONLY_NO_CAPTURE_STAGE_COMMIT_PUSH',
            'closed_literal_boundary': 34, 'base': BASE, 'base_tree': TREE,
            'roots': list(ROOTS), 'source_mapping': CONTROL_SOURCES,
            'core_inventory': values, 'core_delta': delta(values, current_base),
            'optional_prior_qa_roots': list(OPTIONAL),
            'optional_prior_qa_inventory': optional, 'optional_prior_qa_delta': delta(optional, optional_base),
            'optional_prior_qa_selected': False,
            'prior_execution_local_only_boundary': boundary,
            'prior_execution_recursive_inventory_performed': False,
            'protected_roles': roles, 'capacity': capacity,
            'source': {'path': str(Path(__file__).resolve()), **key(Path(__file__).resolve())},
            'imported_executor': {'path': str(OLD), **key(OLD)},
            'git_mutations': 0, 'science_runs': 0, 'remote_requeried': False,
        }
        save(directory / 'INVENTORY_PREVIEW.json', result)
        summary = {'status': result['status'], 'commands': command.count,
            'core_files': len(values), 'core_bytes': sum(v['bytes'] for v in values.values()),
            'core_additions': sum(r['status'] == 'A' for r in result['core_delta']),
            'core_modifications': sum(r['status'] == 'M' for r in result['core_delta']),
            'core_unchanged': sum(r['status'] == '=' for r in result['core_delta']),
            'optional_prior_qa_files': len(optional),
            'optional_prior_qa_bytes': sum(v['bytes'] for v in optional.values()),
            'deletions': 0, 'git_mutations': 0, 'scientific_runs': 0,
            'preview_sha256': key(directory / 'INVENTORY_PREVIEW.json')['sha256']}
        seal = old['finish'](directory, summary)
        print(json.dumps({**summary, 'manifest_sha256': seal}))
    except BaseException:
        old['failure'](directory, 'readonly-discovery')
        raise

if __name__ == '__main__':
    main()
