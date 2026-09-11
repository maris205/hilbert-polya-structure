#!/usr/bin/env python3
"""Read-only Git/workspace selection planner; writes new owned plan artifacts only.

No source text evaluation, no science execution, no fetch/copy/stage/commit/push.
All path sets come from fixed manifest lists and exact approved files in CONFIG.
"""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import time

HERE = Path(__file__).absolute().parent
ROOT = HERE.parents[3]
BATCH = 'docs/papers204_208_sequence/'
QA = BATCH + 'qa/'
CONFIG = json.loads((HERE / 'CONFIG.json').read_text())
MIRROR = Path(CONFIG['mirror'])
COMMANDS, WORKSPACE, MIRROR_READS = [], {}, {}
CHECKS = 0


def check(ok, detail):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(detail)


def digest(body):
    return hashlib.sha256(body).hexdigest()


def metadata(body):
    return {'bytes': len(body), 'sha256': digest(body),
            'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()}


def relative(name):
    p = PurePosixPath(name)
    check(not p.is_absolute() and '..' not in p.parts and str(p) == name
          and not any(c in name for c in ('\n', '\t', '\0')) and not name.startswith(':'), ('safe exact relative path', name))
    check(not any(name.startswith(prefix) for prefix in CONFIG['excluded_prefixes']), ('excluded work', name))
    check(name == 'SYMBOLIC_DYNAMICS_STATE.md' or name.startswith(BATCH)
          or name.startswith('papers/209-ordered-fibre-threading/'), ('authorized mapping', name))
    return name


def file_meta(base, name, collection):
    path = base / name
    check(path.is_file() and not path.is_symlink(), ('regular exact input', str(path)))
    record = metadata(path.read_bytes())
    if name in collection:
        check(collection[name] == record, ('input drift', str(path)))
    collection[name] = record
    return record


def save(name, obj):
    with (HERE / name).open('x') as stream:
        stream.write(json.dumps(obj, sort_keys=True, indent=2) + '\n')


def git(args, input_bytes=None, allowed=(0,), large_name=None):
    argv = ['git', '-C', str(MIRROR), *args]
    environment = dict(os.environ, GIT_OPTIONAL_LOCKS='0')
    result = subprocess.run(argv, input=input_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            env=environment, timeout=60, check=False)
    record = {'argv': argv, 'exit': result.returncode, 'stderr_utf8': result.stderr.decode(),
              'read_only_environment_override': {'GIT_OPTIONAL_LOCKS': '0'}}
    if input_bytes is not None:
        record['stdin'] = {'bytes': len(input_bytes), 'sha256': digest(input_bytes),
                           'role': 'NUL-separated exact selected paths in SCOPE.json order'}
    if large_name:
        with (HERE / large_name).open('xb') as stream:
            stream.write(result.stdout)
        record['stdout_raw'] = {'path': large_name, 'bytes': len(result.stdout), 'sha256': digest(result.stdout)}
    else:
        record['stdout_utf8'] = result.stdout.decode()
    COMMANDS.append(record)
    check(result.returncode in allowed, ('read-only Git command exit', record))
    return result.stdout


def baseline():
    refs = git(['rev-parse', 'HEAD', 'HEAD^{tree}', 'refs/remotes/origin/main']).decode().splitlines()
    check(refs == [CONFIG['baseline'], CONFIG['baseline_tree'], CONFIG['baseline']], 'exact clean baseline refs')
    check(git(['rev-list', '--left-right', '--count', 'HEAD...origin/main']) == b'0\t0\n', 'baseline divergence 0/0')
    check(git(['status', '--porcelain=v1', '--untracked-files=all']) == b'', 'mirror has no tracked/untracked changes')
    check(not (MIRROR / '.git/index.lock').exists(), 'no index lock')
    return refs


def main():
    check(str(ROOT) == CONFIG['workspace'] and not (ROOT / '.git').exists(), 'documented separate workspace')
    check(sys.flags.isolated == sys.flags.no_site == sys.flags.dont_write_bytecode == 1
          and sys.flags.optimize == 0, 'isolated documentary runtime')
    started = time.time()
    refs_before = baseline()
    check(git(['rev-parse', '--show-object-format']) == b'sha1\n', 'Git object format')
    prior_name = QA + 'GIT_OBJECT_P209_ARTIFACT_CORRECTIONS_4BC38B63.json'
    prior = json.loads((ROOT / prior_name).read_text())
    check(prior['commit'] == CONFIG['baseline'] and prior['tree'] == CONFIG['baseline_tree'], 'actual previous checkpoint identity')
    for receipt in prior['native_receipts']:
        name = BATCH + receipt['path']
        check(name in CONFIG['exact_files'], 'explicit previous native receipt inclusion')
        check(file_meta(ROOT, name, WORKSPACE)['sha256'] == receipt['sha256'], 'actual previous receipt bytes')
    expected, packages = {}, []
    for package in CONFIG['packages']:
        base, manifest = package['base'], package['manifest']
        relative(base + '/' + manifest)
        manifest_name = base + '/' + manifest
        manifest_meta = file_meta(ROOT, manifest_name, WORKSPACE)
        check(manifest_meta['sha256'] == package['sha256'], ('named manifest digest', manifest_name))
        payloads = {}
        for line in (ROOT / manifest_name).read_text().splitlines():
            sha, rel = line.split('  ', 1)
            relative(base + '/' + rel)
            check(re.fullmatch('[0-9a-f]{64}', sha) is not None and rel not in payloads
                  and rel != manifest and not PurePosixPath(rel).is_absolute()
                  and '..' not in PurePosixPath(rel).parts, ('nonself manifest row', manifest_name, rel))
            payloads[rel] = sha
        check(len(payloads) == package['payloads'], ('expected payload count', manifest_name))
        actual = set()
        for path in (ROOT / base).rglob('*'):
            check(not path.is_symlink(), ('no package symlink', str(path)))
            if path.is_file():
                actual.add(path.relative_to(ROOT / base).as_posix())
        check(actual == set(payloads) | {manifest}, ('complete physical package coverage', manifest_name,
                                                     sorted(actual - set(payloads) - {manifest})))
        for rel, sha in payloads.items():
            name = relative(base + '/' + rel)
            check(file_meta(ROOT, name, WORKSPACE)['sha256'] == sha, ('manifest payload bytes', name))
            check(name not in expected or expected[name] == sha, ('consistent overlapping package pin', name))
            expected[name] = sha
        expected[manifest_name] = package['sha256']
        packages.append(dict(package, manifest_path=manifest_name, mirror_base=base,
                             physical_files=len(actual), complete_physical_coverage=True))
    exact = []
    for name in CONFIG['exact_files']:
        relative(name)
        record = file_meta(ROOT, name, WORKSPACE)
        check(name not in expected or expected[name] == record['sha256'], 'exact/package matching pin')
        expected[name] = record['sha256']
        exact.append({'path': name, **record})
    # The four unsealed MNA originals must have the exact archived lane40 reference identities.
    role_name = BATCH + 'scouting/finite_systems_fortieth/ROOT_REFERENCE_ROLES.json'
    mna_roles = json.loads((ROOT / role_name).read_text())
    check(len(mna_roles) == 4, 'four exact MNA original roles')
    for row in mna_roles:
        name = str(Path(row['original_path']).relative_to(ROOT))
        check(name in CONFIG['exact_files'] and expected[name] == row['sha256']
              and WORKSPACE[name]['bytes'] == row['bytes'], ('exact frozen-role MNA original', name))
    query_paths = [p['base'] for p in packages] + CONFIG['exact_files']
    tree_raw = git(['ls-tree', '-r', '-z', '--full-tree', 'HEAD', '--',
                    *[':(literal)' + name for name in query_paths]], large_name='BASELINE_TREE.stdout.raw')
    tree = {}
    for entry in tree_raw.split(b'\0'):
        if not entry:
            continue
        descriptor, path = entry.split(b'\t', 1)
        mode, kind, blob = descriptor.decode().split()
        name = path.decode()
        relative(name)
        check(kind == 'blob' and name not in tree, ('baseline ordinary blob', name))
        tree[name] = {'mode': mode, 'blob': blob}
    check(set(tree) <= set(expected), ('baseline has out-of-contract files under explicit package bases', sorted(set(tree) - set(expected))))
    selected, unchanged, mirror_observations = [], [], {}
    for name in sorted(expected):
        workspace = WORKSPACE[name]
        mirror_path = MIRROR / name
        mirror = file_meta(MIRROR, name, MIRROR_READS) if mirror_path.is_file() else None
        check(not mirror_path.is_symlink() and (not mirror_path.exists() or mirror is not None), 'exact mirror target type')
        mirror_observations[name] = mirror
        head = tree.get(name)
        if head:
            check(mirror is not None and mirror['git_blob_sha1'] == head['blob'], ('mirror bytes equal clean HEAD', name))
        equal = mirror is not None and mirror['sha256'] == workspace['sha256']
        if equal and head and head['blob'] == workspace['git_blob_sha1']:
            unchanged.append(name)
        else:
            reason = 'absent_mirror_and_HEAD' if mirror is None and head is None else (
                     'same_mirror_bytes_but_not_in_HEAD' if equal else 'workspace_differs_from_mirror')
            selected.append({'path': name, 'mirror_path': name, **workspace, 'selection_reason': reason,
                             'mirror_before': mirror, 'HEAD_before': head,
                             'workspace_executable_bit': bool((ROOT / name).stat().st_mode & 0o111)})
    stdin = b''.join(row['path'].encode() + b'\0' for row in selected)
    ignored_raw = git(['check-ignore', '--no-index', '-z', '--stdin'], input_bytes=stdin, allowed=(0, 1))
    ignored = [name.decode() for name in ignored_raw.split(b'\0') if name]
    check(set(ignored) <= {r['path'] for r in selected}, 'exact ignored paths inside selection')
    # Rehash the complete source and every existing mirror path; record absent paths unchanged too.
    for name, record in list(WORKSPACE.items()):
        check(metadata((ROOT / name).read_bytes()) == record, ('final source stability', name))
    for name, before in mirror_observations.items():
        path = MIRROR / name
        if before is None:
            check(not path.exists(), ('absent mirror target stayed absent', name))
        else:
            check(metadata(path.read_bytes()) == before, ('final mirror stability', name))
    refs_after = baseline()
    check(refs_before == refs_after, 'baseline refs unchanged')
    expected_serialized = json.dumps(expected, sort_keys=True, separators=(',', ':')).encode()
    producer = {p.name: metadata(p.read_bytes()) for p in (HERE / 'CONFIG.json', Path(__file__).absolute())}
    scope = {'schema': 'p209-completion-private-checkpoint-exact-selection-v1',
        'status': 'READY_READ_ONLY_PLAN_NOT_A_COPY_STAGE_OR_PUSH', 'created_epoch': time.time(),
        'workspace': str(ROOT), 'mirror': str(MIRROR), 'baseline': CONFIG['baseline'], 'baseline_tree': CONFIG['baseline_tree'],
        'mapping': CONFIG['mapping'], 'lifecycle_roles': CONFIG['lifecycle_roles'],
        'packages_for_complete_source_and_future_Git_blob_checks': packages, 'exact_additional_files': exact,
        'all_expected_blob_keys': {'construction': 'Union of every explicitly named manifest payload, the manifests themselves, and exact_additional_files; no glob',
            'count': len(expected), 'canonical_path_sha256_map_sha256': digest(expected_serialized),
            'canonical_encoding': 'UTF-8 json.dumps(path_to_sha256,sort_keys=True,separators=(comma,colon)), without final newline'},
        'selected_paths': selected, 'ignored_selected_paths_require_exact_root_handling': ignored,
        'counts': {'named_manifests': len(packages), 'manifest_payload_rows': sum(p['payloads'] for p in packages),
            'exact_additional_files': len(exact), 'expected_blob_keys': len(expected), 'selected_paths': len(selected),
            'unchanged_HEAD_and_mirror_paths': len(unchanged), 'ignored_selected_paths': len(ignored),
            'selection_reasons': {reason: sum(r['selection_reason'] == reason for r in selected)
                                  for reason in sorted({r['selection_reason'] for r in selected})},
            'source_paths_rehashed_before_after': len(WORKSPACE), 'existing_mirror_paths_rehashed_before_after': len(MIRROR_READS),
            'deletions_planned': 0, 'scientific_executions': 0, 'Git_mutations': 0},
        'producer_pins': producer, 'MNA_unsealed_original_exact_roles': mna_roles,
        'excluded_prefixes': CONFIG['excluded_prefixes'],
        'explicit_exclusion_rule': 'Only these fixed package expansions and exact files are eligible; all other stream paths and active/new MNA/P210 work are excluded.',
        'checks': CHECKS, 'verification_limits': ['Read-only local refs/status only; no new fetch or independent network query.',
            'P209 completion and MNA pending lifecycle roles follow the root assignment; no theorem or gate re-review here.',
            'This plan is a fixed snapshot, not authority to silently absorb later root index, MNA closure, or P210 changes.',
            'Root must recheck all source hashes, baseline, exact ignores, physical coverage and all named-manifest Git blobs during its own synchronization.',
            'This preparation package is excluded from its own selection; root may explicitly add its final seal/payloads separately.']}
    save('READONLY_GIT.actual.json', {'role': 'actual_read_only_local_Git_subprocess_returns', 'started_epoch': started,
                                    'finished_epoch': time.time(), 'commands': COMMANDS})
    save('SCOPE.json', scope)
    print(json.dumps({'status': scope['status'], 'scope': str((HERE / 'SCOPE.json').relative_to(ROOT)),
                      'scope_sha256': digest((HERE / 'SCOPE.json').read_bytes()), 'counts': scope['counts'],
                      'checks': CHECKS, 'read_only_git_commands': len(COMMANDS),
                      'large_native_stdout_path': 'BASELINE_TREE.stdout.raw'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
