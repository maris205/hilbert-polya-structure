#!/usr/bin/env python3
"""Read-only archival planning: metadata/seals/Git observations, no payload audit."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
B = 'docs/papers204_208_sequence/'
Q = B + 'qa/'
S = B + 'scouting/'
P = 'papers/209-ordered-fibre-threading/'
BASELINE = '2974f8ea5f9e7cb0f8146cae017add38a6939da0'
READS = {}
COMMANDS = []
EXCLUDED = (S + 'finite_systems_thirty_third/', Q + 'p209_terminal_artifact_preparation/')
PACKAGES = (
    (B + 'reviews/p209_b', 'accepted_B_originals'),
    (Q + 'p209_b_root_preparation', 'sealed_infrastructure_not_independent_review'),
    (Q + 'root_replays/p209_b_strict/root_b_pair_01', 'root_B_pair_closed'),
    (Q + 'root_replays/p209_b_strict/launcher_root_b_pair_01', 'root_B_outer_closed'),
    (Q + 'p209_round2_preparation', 'executed_freezer_preparation_preserved'),
    (Q + 'p209_terminal_preparation', 'sealed_unexecuted_terminal_preparation'),
    (Q + 'central_lifecycle_p209_round1_push', 'historical_control_snapshots'),
    (Q + 'central_lifecycle_p209_b_initial', 'historical_control_snapshots'),
    (Q + 'central_lifecycle_p209_b_delta', 'historical_control_snapshots'),
    (S + 'finite_systems_twenty_eighth', 'root_closed_negative'),
    (S + 'finite_systems_twenty_ninth', 'root_closed_negative'),
    (S + 'finite_systems_thirtieth', 'root_closed_negative'),
    (S + 'finite_systems_thirty_first', 'root_closed_negative'),
    (S + 'finite_systems_thirty_second', 'sealed_author_negative_root_closure_pending'),
    (P + 'frozen_round2', 'physical_freeze_root_closure_pending'),
)


def data(path):
    path = Path(path)
    raw = path.read_bytes()
    row = {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
           'resolved': str(path.resolve()), 'symlink': os.readlink(path) if path.is_symlink() else None}
    assert str(path) not in READS or READS[str(path)] == row, str(path)
    READS[str(path)] = row
    return raw


def pin(path):
    data(path)
    return READS[str(Path(path))]


def git(args):
    assert args[0] in {'status', 'rev-parse', 'symbolic-ref', 'for-each-ref', 'rev-list', 'diff', 'ls-tree', 'show', 'check-ignore'}
    argv = ['/usr/bin/git', '--no-optional-locks', *args]
    result = subprocess.run(argv, cwd=MIRROR, env={**os.environ, 'GIT_OPTIONAL_LOCKS': '0'},
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    stdout_record = ({'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
                      'stdout_bytes': len(result.stdout), 'stdout_scope': 'Blob bytes hashed, not reproduced or interpreted.'}
                     if args[0] == 'show' else {'stdout': result.stdout.decode()})
    COMMANDS.append({'argv': argv, 'cwd': str(MIRROR), 'exit': result.returncode,
                     **stdout_record, 'stderr': result.stderr.decode(),
                     'network_contact': False, 'worktree_or_index_write_requested': False})
    assert result.returncode == 0, COMMANDS[-1]
    return result.stdout


def head_entry(relative):
    raw = git(['ls-tree', 'HEAD', '--', relative]).decode().strip()
    if not raw:
        return {'exists': False}
    fields, name = raw.split('\t', 1)
    mode, kind, oid = fields.split()
    assert name == relative
    row = {'exists': True, 'mode': mode, 'kind': kind, 'git_object': oid}
    if kind == 'blob':
        old = git(['show', 'HEAD:' + relative])
        row.update(sha256=hashlib.sha256(old).hexdigest(), bytes=len(old))
    return row


def sealed_package(relative, role):
    base = ROOT / relative
    assert base.is_dir() and base.resolve() == base and not base.is_symlink()
    seal = base / 'SHA256SUMS'
    rows = {}
    for line in data(seal).decode().splitlines():
        digest, name = line.split('  ', 1)
        local = Path(name)
        assert re.fullmatch(r'[0-9a-f]{64}', digest)
        assert local.as_posix() == name and local.parts and not local.is_absolute() and '..' not in local.parts
        assert name not in rows and name != 'SHA256SUMS'
        rows[name] = digest
    entries = list(base.rglob('*'))
    links = [p.relative_to(base).as_posix() for p in entries if p.is_symlink()]
    files = {p.relative_to(base).as_posix() for p in entries if p.is_file() and p != seal}
    missing, extra = sorted(set(rows) - files), sorted(files - set(rows))
    assert not links and not missing and not extra, (relative, links, missing, extra)
    head = head_entry(relative)
    return {'data_relative': relative, 'mirror_relative': relative, 'role': role,
            'manifest_relative': relative + '/SHA256SUMS', 'manifest': pin(seal),
            'declared_payloads': len(rows), 'physical_payload_names': len(files),
            'complete_name_census': True, 'symlinks': links, 'payload_hashes_replayed_here': False,
            'head_path': head,
            'selection_rule': 'Enumerate exactly the named manifest payloads plus the manifest; preserve raw bytes.'}


def summary_json(relative):
    value = json.loads(data(ROOT / relative))
    for key in ('measured_result', 'completion', 'result'):
        if key in value and isinstance(value[key], dict):
            candidate = value[key]
            if 'output' in candidate:
                try:
                    decoded = json.loads(candidate['output'])
                    if isinstance(decoded, dict):
                        value = {**decoded, 'recorded_tool_exit': candidate.get('exit_code')}
                        break
                except (TypeError, json.JSONDecodeError):
                    pass
            elif key == 'measured_result':
                value = candidate
                break
    fields = ('schema', 'status', 'paper', 'input_round', 'current_open_findings',
              'review_manifest_entries', 'review_manifest_sha256', 'root_pair_manifest_sha256',
              'root_launcher_manifest_sha256', 'round1_manifest_sha256', 'payloads',
              'manifest_sha256', 'physical_new_historical_alias_payloads', 'core_payloads',
              'author_payloads_unchanged', 'recorded_tool_exit')
    return {k: value[k] for k in fields if k in value}


def main():
    assert sys.argv[1:] == [] and Path.cwd() == ROOT and sys.flags.optimize == 0
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
    assert not (ROOT / '.git').exists() and (MIRROR / '.git').is_dir()
    began = time.time()
    observation = {
        'status_porcelain': git(['status', '--porcelain=v1', '--untracked-files=all']).decode(),
        'head': git(['rev-parse', 'HEAD']).decode().strip(),
        'tree': git(['rev-parse', 'HEAD^{tree}']).decode().strip(),
        'branch': git(['symbolic-ref', 'HEAD']).decode().strip(),
        'local_and_cached_remote_refs': git(['for-each-ref', '--format=%(refname):%(objectname):%(upstream)', 'refs/heads', 'refs/remotes']).decode(),
        'cached_ahead_behind': git(['rev-list', '--left-right', '--count', 'HEAD...refs/remotes/origin/main']).decode().strip(),
        'unstaged_names': git(['diff', '--name-status', 'HEAD']).decode(),
        'staged_names': git(['diff', '--cached', '--name-status']).decode(),
    }
    assert observation['head'] == BASELINE and observation['status_porcelain'] == ''
    packages = [sealed_package(path, role) for path, role in PACKAGES]
    qa_base = ROOT / Q
    current_top = {p.name: p for p in qa_base.iterdir() if p.is_file()}
    head_top = set(git(['ls-tree', '--name-only', 'HEAD:' + Q.rstrip('/')]).decode().splitlines())
    new_qa = sorted(name for name in current_top if name not in head_top)
    documents = ['SYMBOLIC_DYNAMICS_STATE.md', B + 'PIPELINE_STATE.md', B + 'GIT_SYNC_RECEIPT.md',
                 B + 'P209_B_RESPONSE.md']
    documents += [Q + name for name in new_qa]
    documents += [S + name for name in ('TWENTY_EIGHTH_ROOT_INSPECTION.md', 'TWENTY_NINTH_ROOT_INSPECTION.md',
                                       'THIRTIETH_ROOT_INSPECTION.md', 'THIRTY_FIRST_ROOT_INSPECTION.md')]
    for name in ('ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256', 'ROOT_ADOPTION.md', 'PAPER_STATUS.md', 'SHA256SUMS', 'AUTHOR_MANIFEST.sha256'):
        if (ROOT / P / name).is_file():
            documents.append(P + name)
    document_rows = []
    for relative in sorted(set(documents)):
        assert not relative.startswith(EXCLUDED)
        current = pin(ROOT / relative)
        head = head_entry(relative)
        document_rows.append({'data_relative': relative, 'mirror_relative': relative, 'current': current,
                              'head': head, 'changed_since_HEAD': not head['exists'] or head.get('sha256') != current['sha256']})
    current_controls = {n: pin(ROOT / n) for n in ('SYMBOLIC_DYNAMICS_STATE.md', B + 'PIPELINE_STATE.md', B + 'GIT_SYNC_RECEIPT.md')}
    gates = {relative: summary_json(relative) for relative in (
        Q + 'P209_B_ROOT_DELTA_INSPECTION.actual.json', Q + 'P209_ROUND2_FREEZE.actual.json',
        Q + 'SCOUT28_ROOT_INSPECTION.actual.json', Q + 'SCOUT29_ROOT_INSPECTION.actual.json',
        Q + 'SCOUT30_ROOT_INSPECTION.actual.json', Q + 'SCOUT31_ROOT_INSPECTION.actual.json')}
    pending = {}
    for relative in (Q + 'P209_ROUND2_ROOT_INSPECTION.actual.json', Q + 'P209_ROUND2_ROOT_INSPECTION.md',
                     Q + 'SCOUT32_ROOT_INSPECTION.actual.json', S + 'THIRTY_SECOND_ROOT_INSPECTION.md',
                     P + 'qa_final', Q + 'root_replays/p209_terminal_strict'):
        path = ROOT / relative
        pending[relative] = {'exists_at_observation': path.exists(), 'plan_role': 'Deferred until explicit root closure; never assumed from existence.'}
    before = dict(READS)
    assert before == {path: pin(path) for path in before}
    status_end = git(['status', '--porcelain=v1', '--untracked-files=all']).decode()
    assert status_end == observation['status_porcelain']
    print(json.dumps({'schema': 'p209-private-sync-readonly-plan-inventory-v1',
        'status': 'READ_ONLY_PLAN_NOT_SYNCHRONIZED', 'started_epoch': began, 'finished_epoch': time.time(),
        'data_root': str(ROOT), 'mirror': str(MIRROR), 'baseline_commit': BASELINE,
        'git_observation': observation, 'sealed_package_name_inventories': packages,
        'exact_document_candidates': document_rows, 'new_qa_top_level_filenames': new_qa,
        'recorded_gate_summaries_not_fresh_reviews': gates, 'pending_gate_and_output_existence': pending,
        'explicit_excluded_prefixes': list(EXCLUDED), 'control_pins_at_observation': current_controls,
        'read_metadata_paths_rechecked': len(before), 'read_metadata_pins': before,
        'git_commands': COMMANDS, 'final_status_porcelain': status_end,
        'network_fetch_push_or_remote_query': False, 'git_worktree_index_mutations': False,
        'mathematical_or_compilation_execution': False, 'runtime_library_hashing': False,
        'scope': 'Manifest text hashes and safe path/physical-name census, current lifecycle metadata, cached Git refs and blob comparisons only. No scientific payload, verifier, proof or runtime referents are interpreted or replayed.'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
