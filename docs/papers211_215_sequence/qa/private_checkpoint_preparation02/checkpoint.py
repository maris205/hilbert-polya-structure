#!/usr/bin/env python3
"""Prepare only by default; four approved, separately invoked checkpoint phases.

No Git configuration, old-mirror mutation, force push, deletion, worktree
copy, scientific execution or whole-baseline object stream is implemented.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import stat
import subprocess
import sys
import tempfile
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_preparation02'
BARE = Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
BASE = 'f6f3560875f75025624367305b8a9328cbce712e'
BASE_TREE = '30df2d2b012b6e1567bdd2afa61c50e00a547d16'
MIRROR_BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
REMOTE = 'git@github.com:maris205/hilbert-polya-structure.git'
IDENTITY = ('mariswang', 'wangliang.f@gmail.com')
SCOUT = 'docs/papers211_215_sequence/scouting/'
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
PRIOR_QA_ROOTS = ('docs/papers211_215_sequence/qa/private_checkpoint_preparation',
                  'docs/papers211_215_sequence/qa/root_checkpoint_inspection')
ROOTS = ('SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers211_215_sequence/PIPELINE_STATE.md',
         'docs/papers211_215_sequence/PROBLEM_ANCHOR.md',
         *(SCOUT + name for name in LANES), SCOUT + 'spr_root_reception',
         *(SCOUT + 'root_reception/' + name for name in RECEPTIONS), *PRIOR_QA_ROOTS)
EXCLUDED = (SCOUT + 'common_sum_gcd_lane', SCOUT + 'cluster_completion_lane',
            SCOUT + 'queue_transfer_lane', SCOUT + 'root_reception/inspect_gcd_cluster.py',
            SCOUT + 'root_reception/GCD_CLUSTER_NATIVE.json',
            SCOUT + 'root_reception/GCD_CLUSTER_RECEPTION.md',
            'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md',
            'docs/papers204_208_sequence/PIPELINE_STATE.md',
            'README.md', 'AGENTS.md', str(PREP.relative_to(ROOT)))
# Exact root-reception file selection excludes every later receipt, including
# future queue receipts, even if its name has not yet been invented.
CONTROL_SOURCES = {
 'SYMBOLIC_DYNAMICS_STATE.md':
     str((PREP / 'controls_preview34/SYMBOLIC_DYNAMICS_STATE.md').relative_to(ROOT)),
 'docs/papers211_215_sequence/PIPELINE_STATE.md':
     str((PREP / 'controls_preview34/PIPELINE_STATE.md').relative_to(ROOT))}
SEALS = {
 SCOUT + 'arithmetic_lane': ('SHA256SUMS', 'workspace-text', 52),
 SCOUT + 'spr_gate': ('SHA256SUMS', 'local-text', 19),
 SCOUT + 'transport_lane': ('MANIFEST.sha256', 'local-text', 13),
 SCOUT + 'order_geometry_lane': ('MANIFEST.json', 'local-json', 59),
 SCOUT + 'sequence_combinatorics_lane': ('MANIFEST.sha256', 'local-text', 11),
 SCOUT + 'finite_function_lane': ('SHA256SUMS', 'local-text', 35),
 SCOUT + 'valley_absorption_lane': ('MANIFEST.json', 'local-json', 41),
 SCOUT + 'incidence_rewiring_lane': ('MANIFEST.json', 'local-json', 38),
 SCOUT + 'root_profile_preflight': ('SHA256SUMS', 'local-text', 4),
 SCOUT + 'finite_allocation_lane': ('SHA256SUMS', 'local-text', 60),
 SCOUT + 'rational_coupling_lane': ('MANIFEST.sha256', 'local-text', 47),
 SCOUT + 'discrete_geometry_gap_desk': ('MANIFEST.json', 'local-json', 41)}
PIN_LISTS = (SCOUT + 'arithmetic_lane/HISTORICAL_INPUT_PINS.sha256',
             SCOUT + 'spr_gate/INPUT_PINS.sha256',
             SCOUT + 'transport_lane/HISTORY_INPUTS.sha256',
             SCOUT + 'sequence_combinatorics_lane/HISTORY_INPUTS.sha256',
             SCOUT + 'finite_function_lane/HISTORICAL_INPUTS.sha256',
             SCOUT + 'root_profile_preflight/HISTORY_INPUTS.sha256',
             SCOUT + 'finite_allocation_lane/HISTORICAL_INPUTS.sha256',
             SCOUT + 'rational_coupling_lane/INPUT_PINS.sha256')
JSON_INPUTS = tuple(SCOUT + n + '/INPUT_PINS.json' for n in
                    ('order_geometry_lane', 'valley_absorption_lane',
                     'incidence_rewiring_lane', 'discrete_geometry_gap_desk'))
OLD_RUN = Path('/root/symbolic-dynamics-closed-scout-checkpoint-bllqdh27')
LOCAL_ONLY_FILES = ('RUN.json', 'PLAN.json', 'executed_source.py',
                    'capture/MANIFEST.sha256', 'stage/MANIFEST.sha256',
                    'commit/MANIFEST.sha256', 'push/MANIFEST.sha256',
                    'frozen/SYMBOLIC_DYNAMICS_STATE.md',
                    'frozen/docs/papers211_215_sequence/PIPELINE_STATE.md')
CONTRACT_FILES = ('.agents/skills/symbolic-dynamics-research/SKILL.md',
                  'docs/research_state/WORKFLOW.md', 'docs/research_state/HISTORY_AND_CAVEATS.md')
PHASES = ('capture', 'stage', 'commit', 'push')
LIMIT = 12_000_000                 # Entire selected payload, not per-file padding.
COMMIT_MESSAGE = (b'Checkpoint closed post-P210 scouting evidence; 34 closed literal attempts, '
                  b'zero retained papers; preserve all limitations; HOLD_EXTERNAL\n')

def need(condition, message):
    if not condition:
        raise RuntimeError(message)

def sha(body):
    return hashlib.sha256(body).hexdigest()

def save(path, value):
    body = value if isinstance(value, bytes) else (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()
    with Path(path).open('xb') as stream:
        stream.write(body)

def read(path):
    return json.loads(Path(path).read_bytes())

def safe_name(name):
    need(isinstance(name, str) and re.fullmatch(r'[A-Za-z0-9_.\-/]+', name)
         and not name.startswith('/') and all(p not in ('', '.', '..') for p in name.split('/')),
         'Unsafe or noncanonical selected pathname: ' + repr(name))
    return name

def selected(name):
    return any(name == p or name.startswith(p + '/') for p in ROOTS)

def key(path):
    path = Path(path)
    before = path.lstat()
    need(stat.S_ISREG(before.st_mode) and path.resolve() == path,
         'Expected unaliased regular source: ' + str(path))
    with path.open('rb') as stream:
        opened = os.fstat(stream.fileno())
        body = stream.read()
        ended = os.fstat(stream.fileno())
    after = path.lstat()
    attrs = ('st_dev', 'st_ino', 'st_mode', 'st_size', 'st_mtime_ns', 'st_ctime_ns')
    need(all(getattr(before, a) == getattr(opened, a) == getattr(ended, a) == getattr(after, a)
             for a in attrs), 'Source changed during complete read: ' + str(path))
    return {'sha256': sha(body), 'bytes': len(body),
            'mode': '100755' if before.st_mode & 0o111 else '100644',
            'oid': hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()}

def source_path(name, base=ROOT):
    # Future live central indexes are intentionally not inputs to this boundary.
    return base / (CONTROL_SOURCES.get(name, name) if base == ROOT else name)

def members(base=ROOT):
    result = []
    for name in ROOTS:
        path = source_path(name, base)
        need(path.exists() and path.resolve() == path, 'Missing/aliased approved root: ' + name)
        if path.is_file():
            result.append(name)
        else:
            need(path.is_dir(), 'Non-directory approved root')
            for directory, folders, files in os.walk(path):
                need(all(not (Path(directory) / p).is_symlink() for p in folders), 'Directory symlink')
                for filename in files:
                    relative = (Path(directory) / filename).relative_to(base).as_posix()
                    result.append(safe_name(relative))
    need(len(result) == len(set(result)), 'Overlapping approved roots')
    need(all(selected(n) and not any(n == x or n.startswith(x + '/') for x in EXCLUDED)
             for n in result), 'Explicit exclusion violated')
    return sorted(result)

def inventory(base=ROOT):
    names = members(base)
    values = {name: key(source_path(name, base)) for name in names}
    need(names == members(base), 'Selected membership changed while reading')
    need(sum(v['bytes'] for v in values.values()) <= LIMIT, 'Selected payload exceeds compact guard')
    return values

def environment(index=None, identity=False):
    env = {k: os.environ[k] for k in ('HOME', 'USER', 'LOGNAME', 'SSH_AUTH_SOCK', 'SSH_AGENT_PID')
           if k in os.environ}
    env.update(PATH='/usr/bin:/bin', LANG='C', LC_ALL='C', TZ='UTC', GIT_OPTIONAL_LOCKS='0',
               GIT_TERMINAL_PROMPT='0', GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL='/dev/null',
               GIT_SSH_COMMAND='/usr/bin/ssh -o BatchMode=yes -o StrictHostKeyChecking=yes '
                               '-o ConnectTimeout=20 -o ConnectionAttempts=1')
    if index is not None:
        env['GIT_INDEX_FILE'] = str(index)
    if identity:
        env.update(GIT_AUTHOR_NAME=IDENTITY[0], GIT_AUTHOR_EMAIL=IDENTITY[1],
                   GIT_COMMITTER_NAME=IDENTITY[0], GIT_COMMITTER_EMAIL=IDENTITY[1])
    return env

def stop_child(process):
    if process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait(timeout=3)
    return process.returncode

def interrupted(signum, frame):
    raise InterruptedError('Checkpoint interrupted by signal ' + str(signum))

class Commands:
    def __init__(self, directory, phase):
        self.directory, self.phase, self.count = directory, phase, 0

    def run(self, argv, stdin=b'', index=None, identity=False):
        self.count += 1
        directory = self.directory / f'command_{self.count:03d}'
        directory.mkdir()
        env = environment(index, identity)
        save(directory / 'stdin.raw', stdin)
        save(directory / 'ATTEMPT.json', {'argv': argv, 'cwd': str(ROOT), 'environment': env,
             'timeout_seconds': 50, 'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()})
        start, timed_out, code, process = time.monotonic(), False, None, None
        with (directory / 'stdout.raw').open('xb') as out, (directory / 'stderr.raw').open('xb') as err:
            try:
                process = subprocess.Popen(argv, cwd=ROOT, env=env, stdin=subprocess.PIPE,
                                           stdout=out, stderr=err, start_new_session=True)
                save(directory / 'SPAWN.json', {'pid': process.pid, 'spawned': True})
                try:
                    process.communicate(stdin, timeout=50)
                except subprocess.TimeoutExpired:
                    timed_out = True
                    stop_child(process)
                code = process.returncode
            except BaseException:
                original, cleanup_error = traceback.format_exc(), None
                if process is not None:
                    try:
                        code = stop_child(process)
                    except BaseException:
                        cleanup_error = traceback.format_exc()
                save(directory / 'EXCEPTION.json', {'traceback': original,
                     'cleanup_error': cleanup_error, 'actual_final_returncode': code})
                raise
            finally:
                save(directory / 'RESULT.json', {'returncode': code, 'timed_out': timed_out,
                     'elapsed_seconds': time.monotonic() - start})
        need(code == 0 and not timed_out, 'Native command failed; original streams retained: ' + str(directory))
        return (directory / 'stdout.raw').read_bytes()

    def git(self, *args, stdin=b'', index=None, identity=False):
        mutations = {'stage': {'read-tree', 'hash-object', 'update-index', 'write-tree'},
                     'commit': {'commit-tree'}, 'push': {'push', 'update-ref'}}
        readonly = {'rev-parse', 'symbolic-ref', 'remote', 'ls-remote', 'ls-tree',
                    'ls-files', 'diff-tree', 'cat-file', 'rev-list', 'show', '--version'}
        need(args[0] in readonly or args[0] in mutations.get(self.phase, set()),
             'Git operation is not allowed in this phase')
        argv = ['/usr/bin/git', '--git-dir=' + str(BARE), '-c', 'core.hooksPath=/dev/null',
                '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', '-c', 'commit.gpgSign=false', *args]
        return self.run(argv, stdin, index, identity)

    def mirror(self, *args):
        need(args in (('rev-parse', 'HEAD'), ('remote', 'get-url', 'origin'),
                      ('status', '--porcelain=v1', '-z', '--untracked-files=all')),
             'Original-mirror operation outside read-only allowlist')
        return self.run(['/usr/bin/git', '-C', str(MIRROR), *args])

def protected_roles():
    paths = [MIRROR / '.git' / p for p in ('config', 'HEAD', 'index', 'packed-refs', 'refs/heads/main',
                                           'objects/info/alternates')]
    paths += [BARE / p for p in ('config', 'HEAD', 'index', 'packed-refs', 'objects/info/alternates')]
    paths += [Path('/usr/bin/git'), Path('/usr/bin/ssh'), Path(sys.executable).resolve()]
    return {str(p): ({'present': True, **key(p)} if p.exists() else {'present': False}) for p in paths}

def remote(command, expected):
    output = command.git('ls-remote', '--exit-code', REMOTE, 'refs/heads/main')
    need(output.decode().split() == [expected, 'refs/heads/main'], 'Remote advanced or not confirmed')

def repository(command, expected=BASE, network=True):
    need(command.git('rev-parse', '--is-bare-repository').strip() == b'true', 'Accepted destination is not bare')
    need(command.git('symbolic-ref', 'HEAD').strip() == b'refs/heads/main', 'Unexpected bare HEAD')
    need(command.git('rev-parse', 'refs/heads/main').strip().decode() == expected, 'Bare main changed')
    need(command.git('rev-parse', '--show-object-format').strip() == b'sha1', 'Unexpected Git object format')
    need(command.git('rev-parse', BASE + '^{tree}').strip().decode() == BASE_TREE, 'Baseline tree changed')
    need(command.git('remote').strip() == b'', 'Bare remote configuration changed; do not add origin')
    need(command.mirror('rev-parse', 'HEAD').strip().decode() == MIRROR_BASE, 'Original mirror HEAD changed')
    need(command.mirror('status', '--porcelain=v1', '-z', '--untracked-files=all') == b'', 'Original mirror not clean')
    need(command.mirror('remote', 'get-url', 'origin').strip().decode() == REMOTE, 'Explicit mirror URL changed')
    if network:
        remote(command, expected)

def tree_map(raw):
    need(not raw or raw.endswith(b'\0'), 'Truncated selected tree stream')
    result = {}
    for row in raw.split(b'\0')[:-1]:
        head, name = row.split(b'\t', 1)
        mode, kind, oid = head.decode().split()
        name = safe_name(name.decode())
        need(name not in result and selected(name) and kind == 'blob' and mode in ('100644', '100755')
             and re.fullmatch('[0-9a-f]{40}', oid), 'Invalid selected tree record')
        result[name] = {'mode': mode, 'oid': oid}
    return result

def selected_tree(command, ref):
    return tree_map(command.git('ls-tree', '-r', '-z', '--full-tree', ref, '--', *ROOTS))

def diff_map(raw):
    need(not raw or raw.endswith(b'\0'), 'Truncated complete diff stream')
    fields, result = raw.split(b'\0')[:-1], {}
    need(len(fields) % 2 == 0, 'Invalid complete raw diff framing')
    for i in range(0, len(fields), 2):
        attrs = fields[i].decode().split()
        name = safe_name(fields[i + 1].decode())
        need(len(attrs) == 5 and attrs[0].startswith(':') and attrs[4] in ('A', 'M')
             and name not in result and selected(name), 'Deletion/rename/nonselected diff forbidden')
        oldmode, newmode, oldoid, newoid, status_ = attrs
        need(newmode in ('100644', '100755') and re.fullmatch('[0-9a-f]{40}', oldoid)
             and re.fullmatch('[0-9a-f]{40}', newoid), 'Invalid raw diff modes/OIDs')
        result[name] = {'oldmode': oldmode[1:], 'mode': newmode, 'oldoid': oldoid, 'oid': newoid, 'status': status_}
    return result

def manifest_rows(path):
    rows = {}
    for line in path.read_text().splitlines():
        digest, name = line.split('  ', 1)
        safe_name(name)
        need(re.fullmatch('[0-9a-f]{64}', digest) and name not in rows, 'Invalid manifest row')
        rows[name] = digest
    return rows

def complete_manifest(directory, name):
    rows = manifest_rows(directory / name)
    files = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()}
    need(set(rows) == files - {name} and name not in rows, 'Incomplete/nonself manifest: ' + str(directory))
    for path, expected in rows.items():
        need(key(directory / path)['sha256'] == expected, 'Manifest mismatch: ' + path)
    return {'sha256': key(directory / name)['sha256'], 'rows': len(rows)}

def artifacts(base=ROOT):
    packages, inherited, raw_pairs = {}, [], []
    for name, (seal, layout, count) in SEALS.items():
        directory = base / name
        if layout == 'local-json':
            entries = read(directory / seal)['files']
            rows = {}
            for entry in entries:
                relative = safe_name(entry['path'])
                need(relative not in rows, 'Duplicate JSON manifest path')
                actual = key(directory / relative)
                need(actual['sha256'] == entry['sha256'] and actual['bytes'] == entry['bytes'],
                     'JSON manifest byte/hash mismatch')
                rows[relative] = entry['sha256']
        else:
            rows = manifest_rows(directory / seal)
            if layout == 'workspace-text':
                prefix = name + '/'
                need(all(r.startswith(prefix) for r in rows), 'Workspace seal escapes its lane')
                rows = {r[len(prefix):]: digest for r, digest in rows.items()}
            for relative, digest in rows.items():
                need(key(directory / relative)['sha256'] == digest, 'Text manifest mismatch')
        actual_files = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()}
        need(not any(p.is_symlink() for p in directory.rglob('*')), 'Package symlink')
        need(len(rows) == count and set(rows) == actual_files - {seal} and seal not in rows,
             'Incomplete/nonself known package')
        packages[name] = {'seal': seal, 'sha256': key(directory / seal)['sha256'], 'rows': len(rows)}
    for name in PIN_LISTS:
        for line in (base / name).read_text().splitlines():
            digest, original = line.split('  ', 1)
            need(re.fullmatch('[0-9a-f]{64}', digest), 'Invalid inherited digest')
            physical = Path(original) if original.startswith('/') else (
                source_path(original, base) if selected(original) else ROOT / safe_name(original))
            value = key(physical.resolve())
            need(value['sha256'] == digest, 'Inherited input mismatch: ' + original)
            inherited.append({'list': name, 'key': original, 'mapped': original,
                              'sha256': digest, 'oid': value['oid'], 'bytes': value['bytes']})
    for name in JSON_INPUTS:
        directory = (base / name).parent
        for row in read(base / name)['inputs']:
            original, snapshot = safe_name(row['source']), safe_name(row['snapshot'])
            physical = source_path(original, base) if selected(original) else ROOT / original
            value = key(physical)
            copy = directory / snapshot
            need(value['sha256'] == row['sha256'] and value['bytes'] == row['bytes']
                 and copy.read_bytes() == physical.read_bytes(), 'Historical source/copy mismatch')
            inherited.append({'list': name, 'key': original,
                              'mapped': str(copy.relative_to(base)),
                              'sha256': value['sha256'], 'oid': value['oid'], 'bytes': value['bytes']})
            raw_pairs.append({'source': original, 'snapshot': str(copy.relative_to(base)),
                              'sha256': value['sha256']})
    # These snapshots remain historical roles, never future live central bytes.
    rational = SCOUT + 'rational_coupling_lane'
    rational_controls = []
    for row in read(base / rational / 'native02/receipt.json')['control_snapshots']:
        mapped = rational + '/' + safe_name(row['snapshot'])
        need(key(base / mapped)['sha256'] == row['sha256'], 'Rational historical control changed')
        rational_controls.append({**row, 'physical_role': mapped, 'future_live_comparison': False})
    # Root explicitly selected both prior QA packages. Their outside-workspace
    # executed archive stays local-only; only nine exact boundary files are read.
    prior_qa = {'preparation_seal':
        complete_manifest(base / PRIOR_QA_ROOTS[0], 'MANIFEST.sha256'),
        'postpush_readonly_seal':
        complete_manifest(base / PRIOR_QA_ROOTS[1] / 'postpush_readonly01', 'MANIFEST.sha256')}
    local_only = {str(OLD_RUN / n): key(OLD_RUN / n) for n in LOCAL_ONLY_FILES}
    old_plan = read(OLD_RUN / 'PLAN.json')
    need(key(OLD_RUN / 'executed_source.py')['sha256'] == old_plan['source_sha256'],
         'Prior actual executed source changed')
    previous_previews = []
    for label in ('preview01', 'preview02', 'preview03'):
        prior = read(base / PRIOR_QA_ROOTS[0] / label / 'PLAN.json')
        mapped_controls = {}
        for name, expected in prior['inventory'].items():
            if name in CONTROL_SOURCES:
                physical = OLD_RUN / 'frozen' / name
                mapped_controls[name] = str(physical)
            else:
                physical = base / name if selected(name) else ROOT / name
            need(key(physical) == expected, 'Prior preview historical role mismatch: ' + label + ':' + name)
        source_present = prior['source_sha256'] == old_plan['source_sha256']
        previous_previews.append({'label': label, 'selected_rows': len(prior['inventory']),
          'historical_control_mapping': mapped_controls,
          'source_sha256': prior['source_sha256'],
          'actual_final_executed_source_available': source_present,
          'scope': ('Executed-source match' if source_present else
                    'Superseded non-executed preview; former source version not represented as available')})
    return {'packages': packages, 'inherited_inputs': inherited,
            'historical_raw_pairs': raw_pairs, 'rational_historical_control_roles': rational_controls,
            'prior_qa': prior_qa, 'prior_previews': previous_previews,
            'local_only_execution_boundary': local_only,
            'local_only_boundary_file_count': 9, 'outside_archive_recursively_copied': False,
            'contracts': {n: key(ROOT / n) for n in CONTRACT_FILES}}

def dependency_tree(raw):
    need(not raw or raw.endswith(b'\0'), 'Truncated dependency metadata stream')
    rows = {}
    for row in raw.split(b'\0')[:-1]:
        head, name = row.split(b'\t', 1)
        mode, kind, oid = head.decode().split()
        name = safe_name(name.decode())
        need(kind == 'blob' and name not in rows, 'Invalid dependency object')
        rows[name] = {'mode': mode, 'oid': oid}
    return rows

def dependency_git_mapping(command, inherited, values):
    originals = sorted({r['key'] for r in inherited['inherited_inputs'] if not r['key'].startswith('/')})
    candidates = sorted({p for n in originals if not selected(n) for p in (n, 'symbolic_dynamics/' + n)})
    baseline = dependency_tree(command.git('ls-tree', '-r', '-z', '--full-tree', BASE, '--', *candidates)) if candidates else {}
    bindings = []
    for row in inherited['inherited_inputs']:
        name = row['key']
        if name.startswith('/'):
            places, status = [], 'local-only host skill/runtime; not a promised Git dependency'
        elif selected(name):
            need(values[name]['oid'] == row['oid'], 'Selected inherited object mismatch')
            places, status = [name], 'selected exact object'
        else:
            places = [p for p in (name, 'symbolic_dynamics/' + name)
                      if p in baseline and baseline[p]['oid'] == row['oid']]
            status = 'exact accepted-baseline object' if places else 'local-only original'
            if selected(row['mapped']) and row['mapped'] != name:
                need(values[row['mapped']]['oid'] == row['oid'], 'Selected snapshot object mismatch')
                places.append(row['mapped'])
                status += '; exact selected snapshot'
        bindings.append({'pin_list': row['list'], 'original_key': name,
                         'sha256': row['sha256'], 'git_paths': places, 'status': status})
    return {'bindings': bindings,
            'scope': 'Metadata-only baseline lookup; no old file copied or Git object written'}

def delta_preview(values, baseline):
    return [{'git_path': name, 'source_path': CONTROL_SOURCES.get(name, name),
             'old': baseline.get(name), 'new': value,
             'status': ('=' if baseline.get(name) == {k: value[k] for k in ('mode', 'oid')}
                        else 'M' if name in baseline else 'A')}
            for name, value in sorted(values.items())]

def finish(directory, result):
    save(directory / 'RESULT.json', result)
    files = sorted(p for p in directory.rglob('*') if p.is_file())
    save(directory / 'MANIFEST.sha256', ''.join(f'{key(p)["sha256"]}  {p.relative_to(directory).as_posix()}\n'
                                              for p in files).encode())
    complete_manifest(directory, 'MANIFEST.sha256')
    return key(directory / 'MANIFEST.sha256')['sha256']

def failure(directory, phase):
    save(directory / 'FAILURE.json', {'phase': phase, 'traceback': traceback.format_exc(),
         'no_rollback': True, 'raw_evidence_preserved': True,
         'boundary': 'Failure is not success; no retry, deletion, force push or automatic repair.'})

def prepare(label):
    need(re.fullmatch('preview[0-9]{2}', label), 'Use a fresh numbered preparation preview')
    directory = PREP / label
    directory.mkdir(exist_ok=False)
    command = Commands(directory, 'prepare')
    try:
        roles = protected_roles()
        repository(command, network=False)
        observed_identity = command.git('show', '-s', '--format=%an%x00%ae%x00%cn%x00%ce', BASE)
        need(observed_identity.decode().rstrip('\n').split('\0') == [*IDENTITY, *IDENTITY], 'Existing commit identity differs')
        values, inherited = inventory(), artifacts()
        mappings = dependency_git_mapping(command, inherited, values)
        baseline = selected_tree(command, BASE)
        need(set(baseline) <= set(values), 'Selected baseline path missing from live scope')
        need(values == inventory() and roles == protected_roles(), 'Read-only preparation input changed')
        plan = {'schema': 'closed-scout-checkpoint-plan-v2', 'status': 'PREPARED_NOT_AUTHORIZED_OR_EXECUTED',
                'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'source_sha256': key(Path(__file__).resolve())['sha256'],
                'base': BASE, 'base_tree': BASE_TREE, 'mirror_base': MIRROR_BASE, 'remote_url': REMOTE,
                'identity': list(IDENTITY), 'roots': list(ROOTS), 'excluded': list(EXCLUDED),
                'inventory': values, 'baseline_selected': baseline, 'protected_roles': roles, 'artifacts': inherited,
                'selected_bytes': sum(v['bytes'] for v in values.values()),
                'private_only': True, 'new_scientific_runs': 0,
                'closed_literal_boundary': 34, 'prior_qa_explicitly_selected': True,
                'source_mapping': {n: CONTROL_SOURCES.get(n, n) for n in values},
                'delta_preview': delta_preview(values, baseline),
                'dependency_git_mapping': mappings,
                'current_live_control_equality_required': False,
                'later_receipts_excluded': True, 'baseline_nonselected_policy': 'Preserve exactly; verify complete raw diff.'}
        save(directory / 'PLAN.json', plan)
        seal = finish(directory, {'status': 'PASS_READONLY_PREPARATION', 'selected_paths': len(values),
              'selected_bytes': plan['selected_bytes'], 'baseline_selected_paths': len(baseline),
              'commands': command.count,
              'additions': sum(r['status'] == 'A' for r in plan['delta_preview']),
              'modifications': sum(r['status'] == 'M' for r in plan['delta_preview']),
              'unchanged_selected': sum(r['status'] == '=' for r in plan['delta_preview']),
              'deletions': 0, 'closed_literal_boundary': 34, 'plan_sha256': key(directory / 'PLAN.json')['sha256'],
              'source_sha256': plan['source_sha256'], 'git_mutations': 0, 'remote_not_requeried': True})
        print(json.dumps({'preview': str(directory), 'manifest_sha256': seal,
                          'plan_sha256': key(directory / 'PLAN.json')['sha256']}))
    except BaseException:
        failure(directory, 'prepare')
        raise

def approved_plan(path, expected):
    need(re.fullmatch('[0-9a-f]{64}', expected or ''), 'Root must supply approved exact plan digest')
    need(key(path)['sha256'] == expected, 'Approved plan bytes changed')
    plan = read(path)
    need(plan['schema'] == 'closed-scout-checkpoint-plan-v2' and tuple(plan['roots']) == ROOTS
         and tuple(plan['excluded']) == EXCLUDED and plan['base'] == BASE and plan['base_tree'] == BASE_TREE
         and plan['remote_url'] == REMOTE and plan['mirror_base'] == MIRROR_BASE
         and tuple(plan['identity']) == IDENTITY and plan['new_scientific_runs'] == 0
         and plan['closed_literal_boundary'] == 34 and plan['prior_qa_explicitly_selected'] is True
         and plan['source_mapping'] == {n: CONTROL_SOURCES.get(n, n) for n in plan['inventory']}
         and plan['current_live_control_equality_required'] is False
         and plan['delta_preview'] == delta_preview(plan['inventory'], plan['baseline_selected']),
         'Plan scope or repository role mismatch')
    need(plan['source_sha256'] == key(Path(__file__).resolve())['sha256'], 'Approved executor source changed')
    return plan

def frozen_guard(run, plan, live=False):
    need(read(run / 'PLAN.json') == plan, 'Frozen approved plan changed')
    need(key(run / 'executed_source.py')['sha256'] == plan['source_sha256'], 'Frozen executor changed')
    need(inventory(run / 'frozen') == plan['inventory'], 'Frozen selected bytes/modes/paths changed')
    need(artifacts(run / 'frozen') == plan['artifacts'], 'Frozen package/input binding changed')
    need(protected_roles() == plan['protected_roles'], 'Protected old-repository/config/default-index role changed')
    if live:
        need(inventory() == plan['inventory'] and artifacts() == plan['artifacts'], 'Live capture source changed')

def verify_tree(command, plan, tree, index):
    values, baseline = plan['inventory'], plan['baseline_selected']
    expected = {n: {'mode': v['mode'], 'oid': v['oid']} for n, v in values.items()}
    need(selected_tree(command, tree) == expected, 'Selected committed tree differs from frozen inventory')
    raw = command.git('ls-files', '--stage', '-z', '--', *ROOTS, index=index)
    need(not raw or raw.endswith(b'\0'), 'Truncated selected-index stream')
    actual = {}
    for row in raw.split(b'\0')[:-1]:
        head, name = row.split(b'\t', 1)
        mode, oid, stage = head.decode().split()
        name = safe_name(name.decode())
        need(stage == '0' and name not in actual, 'Unmerged or duplicate selected-index entry')
        actual[name] = {'mode': mode, 'oid': oid}
    need(actual == expected, 'Selected isolated-index entries differ')
    delta = diff_map(command.git('diff-tree', '--no-commit-id', '--raw', '-r', '-z', '--no-renames', BASE_TREE, tree))
    changed = {n for n, value in expected.items() if baseline.get(n) != value}
    need(set(delta) == changed, 'Complete baseline diff differs; nonselected or missing change')
    for name, value in delta.items():
        old = baseline.get(name, {'mode': '000000', 'oid': '0' * 40})
        need(value == {'oldmode': old['mode'], 'mode': expected[name]['mode'], 'oldoid': old['oid'],
                       'oid': expected[name]['oid'], 'status': 'M' if name in baseline else 'A'}, 'Exact changed-record mismatch')
    unique = {v['oid']: v['bytes'] for v in values.values()}
    stream = ''.join(oid + '\n' for oid in sorted(unique)).encode()
    got = command.git('cat-file', '--batch-check', stdin=stream)
    need(got == ''.join(f'{oid} blob {unique[oid]}\n' for oid in sorted(unique)).encode(), 'Selected object type/OID/length mismatch')
    return len(changed)

def previous(run, phase, expected):
    number = PHASES.index(phase)
    if number == 0:
        need(expected is None, 'Capture cannot claim a previous phase')
        return None
    directory = run / PHASES[number - 1]
    need(re.fullmatch('[0-9a-f]{64}', expected or ''), 'Prior successful phase seal is required')
    need(key(directory / 'MANIFEST.sha256')['sha256'] == expected, 'Prior phase seal changed')
    complete_manifest(directory, 'MANIFEST.sha256')
    result = read(directory / 'RESULT.json')
    need(result['status'] == 'PASS_PRIVATE_CHECKPOINT_' + PHASES[number - 1].upper(), 'Prior phase did not pass')
    runinfo = read(run / 'RUN.json')
    need(result['approved_plan_sha256'] == runinfo['approved_plan_sha256']
         and result['source_sha256'] == runinfo['source_sha256'], 'Prior phase uses another approved plan/source')
    previous(run, PHASES[number - 1], result['previous_phase_sha256'])
    return result

def execute(args):
    path = Path(args.plan).resolve() if args.phase == 'capture' else Path(args.run) / 'PLAN.json'
    plan = approved_plan(path, args.approved_plan_sha256)
    if args.phase == 'capture':
        need(args.run is None and args.previous_phase_sha256 is None, 'Capture creates a fresh /root temporary run')
        need(inventory() == plan['inventory'] and artifacts() == plan['artifacts'], 'Plan stale before capture')
        need(protected_roles() == plan['protected_roles'], 'Protected roles changed before capture')
        need(set(plan['baseline_selected']) <= set(plan['inventory']), 'Selected baseline path missing')
        for destination in (Path('/root'), BARE):
            capacity = os.statvfs(destination)
            need(capacity.f_bavail * capacity.f_frsize >= 5 * plan['selected_bytes'] + LIMIT,
                 'Insufficient checked capacity for compact snapshot, objects, pack and logs')
        run = Path(tempfile.mkdtemp(prefix='symbolic-dynamics-closed-scout-checkpoint-', dir='/root'))
        (run / 'frozen').mkdir()
        indexdir = Path(tempfile.mkdtemp(prefix='index-', dir=run))
        save(run / 'RUN.json', {'index': str(indexdir / 'index'), 'approved_plan_sha256': args.approved_plan_sha256,
             'source_sha256': plan['source_sha256'], 'temp_creation': 'tempfile.mkdtemp under /root; never a broad cleanup target'})
        save(run / 'PLAN.json', path.read_bytes())
        save(run / 'executed_source.py', Path(__file__).resolve().read_bytes())
        print(json.dumps({'run': str(run), 'phase': 'capture'}), flush=True)
    else:
        run = Path(args.run)
        need(run.parent == Path('/root') and re.fullmatch('symbolic-dynamics-closed-scout-checkpoint-[a-z0-9_]+', run.name)
             and run.resolve() == run, 'Unexpected run path')
    prior = previous(run, args.phase, args.previous_phase_sha256)
    info = read(run / 'RUN.json')
    need(info['approved_plan_sha256'] == args.approved_plan_sha256 and info['source_sha256'] == plan['source_sha256'],
         'Run/approved-source binding changed')
    index = Path(info['index'])
    need(index.parent.parent == run and index.name == 'index' and index.resolve() == index, 'Unowned index path')
    directory = run / args.phase
    directory.mkdir(exist_ok=False)
    command = Commands(directory, args.phase)
    try:
        repository(command)
        if args.phase == 'capture':
            need(selected_tree(command, BASE) == plan['baseline_selected'], 'Captured selected baseline changed')
            for name, expected in plan['inventory'].items():
                need(key(source_path(name)) == expected, 'Source changed before frozen copy')
                target = run / 'frozen' / name
                target.parent.mkdir(parents=True, exist_ok=True)
                save(target, source_path(name).read_bytes())
                target.chmod(0o555 if expected['mode'] == '100755' else 0o444)
                need(key(target) == expected and key(source_path(name)) == expected, 'Frozen copy/source race')
            frozen_guard(run, plan, live=True)
            need(not index.exists(), 'Capture must not create a Git index')
            result = {'selected_paths': len(plan['inventory']), 'selected_bytes': plan['selected_bytes'], 'git_mutations': 0}
        else:
            frozen_guard(run, plan)
            if args.phase == 'stage':
                need(not index.exists(), 'Never overwrite an existing isolated index, including a failed stage')
                command.git('read-tree', BASE, index=index)
                changed = [n for n, v in sorted(plan['inventory'].items())
                           if plan['baseline_selected'].get(n) != {'mode': v['mode'], 'oid': v['oid']}]
                need(changed, 'No changes; no empty checkpoint')
                input_paths = ''.join(json.dumps(str(run / 'frozen' / n)) + '\n' for n in changed).encode()
                written = command.git('hash-object', '-w', '--no-filters', '--stdin-paths', stdin=input_paths, index=index)
                need(written.decode().splitlines() == [plan['inventory'][n]['oid'] for n in changed], 'Written frozen object OIDs differ')
                rows = b''.join((plan['inventory'][n]['mode'] + ' ' + plan['inventory'][n]['oid'] + '\t' + n).encode() + b'\0'
                                for n in changed)
                command.git('update-index', '-z', '--index-info', stdin=rows, index=index)
                tree = command.git('write-tree', index=index).decode().strip()
                result = {'tree': tree, 'changed_paths': verify_tree(command, plan, tree, index)}
            elif args.phase == 'commit':
                tree = prior['tree']
                verify_tree(command, plan, tree, index)
                commit = command.git('commit-tree', tree, '-p', BASE, stdin=COMMIT_MESSAGE, identity=True).decode().strip()
                need(command.git('rev-list', '--parents', '-n', '1', commit).decode().split() == [commit, BASE], 'Unexpected commit parent')
                need(command.git('rev-parse', commit + '^{tree}').decode().strip() == tree, 'Unexpected commit tree')
                identity = command.git('show', '-s', '--format=%an%x00%ae%x00%cn%x00%ce', commit)
                need(identity.decode().rstrip('\n').split('\0') == [*IDENTITY, *IDENTITY], 'Command-local existing identity differs')
                command.git('cat-file', '-p', commit)  # Small commit header/message, never bulk blob bodies.
                result = {'tree': tree, 'commit': commit, 'local_main_unchanged': True}
            else:
                tree, commit = prior['tree'], prior['commit']
                verify_tree(command, plan, tree, index)
                need(command.git('rev-list', '--parents', '-n', '1', commit).decode().split() == [commit, BASE]
                     and command.git('rev-parse', commit + '^{tree}').decode().strip() == tree, 'Commit chain changed')
                remote(command, BASE)
                frozen_guard(run, plan)
                command.git('push', '--porcelain', REMOTE, commit + ':refs/heads/main')
                remote(command, commit)
                command.git('update-ref', 'refs/heads/main', commit, BASE)
                repository(command, expected=commit)
                verify_tree(command, plan, tree, index)
                result = {'tree': tree, 'commit': commit, 'actual_remote_confirmed': True, 'bare_worktree_status': 'N/A'}
            frozen_guard(run, plan)
        result.update(status='PASS_PRIVATE_CHECKPOINT_' + args.phase.upper(), phase=args.phase,
             approved_plan_sha256=args.approved_plan_sha256, source_sha256=plan['source_sha256'],
             previous_phase_sha256=args.previous_phase_sha256, commands=command.count,
             no_deletions=True, no_nonselected_changes=True, no_force_push=True,
             no_new_science=True, hold_external=True, later_receipts_not_self_included=True)
        seal = finish(directory, result)
        print(json.dumps({'run': str(run), 'phase': args.phase, 'phase_sha256': seal, **result}))
    except BaseException:
        failure(directory, args.phase)
        raise

def main():
    for signum in (signal.SIGTERM, signal.SIGHUP):
        signal.signal(signum, interrupted)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=('prepare', *PHASES))
    parser.add_argument('--preview', default='preview01')
    parser.add_argument('--plan')
    parser.add_argument('--run')
    parser.add_argument('--approved-plan-sha256')
    parser.add_argument('--previous-phase-sha256')
    args = parser.parse_args()
    need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.dont_write_bytecode,
         'Invoke with python3 -I -S -B; no site packages or bytecode writes')
    if args.phase == 'prepare':
        need(Path(__file__).resolve() == PREP / 'checkpoint.py', 'Prepare only from the owned source path')
        prepare(args.preview)
    else:
        need(args.plan if args.phase == 'capture' else args.run, 'Exact approved plan/run argument required')
        execute(args)

if __name__ == '__main__':
    main()
