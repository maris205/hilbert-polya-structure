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
PREP = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_preparation'
BARE = Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
BASE = 'cd6066f471631bab7aa544867678578c573c03b1'
BASE_TREE = '4d6425878bf347448abeed4e4260fb2013420cc0'
MIRROR_BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
REMOTE = 'git@github.com:maris205/hilbert-polya-structure.git'
IDENTITY = ('mariswang', 'wangliang.f@gmail.com')
SCOUT = 'docs/papers211_215_sequence/scouting/'
LANES = ('combinatorial_lane', 'graph_lane', 'algebra_lane', 'root_zigzag',
         'residual_desk', 'set_code_lane', 'nonlinear_lane', 'tree_order_lane')
ROOTS = ('SYMBOLIC_DYNAMICS_STATE.md',
         'docs/papers211_215_sequence/PROBLEM_ANCHOR.md',
         'docs/papers211_215_sequence/PIPELINE_STATE.md',
         *(SCOUT + name for name in LANES), SCOUT + 'root_reception',
         'docs/papers204_208_sequence/qa/FIVE_PRIVATE_SYNC_ROOT_INSPECTION.md',
         'docs/papers204_208_sequence/qa/FIVE_PRIVATE_SYNC_ROOT_ACCEPTANCE.actual.json')
EXCLUDED = (SCOUT + 'arithmetic_lane', SCOUT + 'spr_gate',
            SCOUT + 'spr_root_reception', SCOUT + 'transport_lane',
            'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md',
            'docs/papers204_208_sequence/PIPELINE_STATE.md', str(PREP.relative_to(ROOT)))
SEALS = {SCOUT + name: ('SHA256SUMS' if name in ('graph_lane', 'algebra_lane')
                      else 'MANIFEST.sha256') for name in LANES}
PIN_LISTS = (SCOUT + 'combinatorial_lane/INPUT_PINS.sha256',
             SCOUT + 'graph_lane/INPUTS.sha256',
             SCOUT + 'algebra_lane/HISTORICAL_SHA256SUMS',
             SCOUT + 'residual_desk/INPUT_PINS.sha256',
             SCOUT + 'set_code_lane/INPUT_PINS.sha256',
             SCOUT + 'nonlinear_lane/INPUT_PINS.sha256',
             SCOUT + 'tree_order_lane/INPUT_PINS.sha256',
             SCOUT + 'tree_order_lane/RUNTIME_POST_PINS.sha256')
CONTROL_MAP = {'SYMBOLIC_DYNAMICS_STATE.md':
               SCOUT + 'root_reception/control_initial13/SYMBOLIC_DYNAMICS_STATE.md',
               'docs/papers211_215_sequence/PIPELINE_STATE.md':
               SCOUT + 'root_reception/control_initial13/PIPELINE_STATE.md'}
PHASES = ('capture', 'stage', 'commit', 'push')
LIMIT = 10_000_000                 # Entire selected payload, not per-file padding.
COMMIT_MESSAGE = (b'Checkpoint closed post-P210 scouting evidence; 18 closed literal attempts, '
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

def members(base=ROOT):
    result = []
    for name in ROOTS:
        path = base / name
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
    values = {name: key(base / name) for name in names}
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
    packages = {name: complete_manifest(base / name, seal) for name, seal in SEALS.items()}
    inherited = []
    for name in PIN_LISTS:
        for line in (base / name).read_text().splitlines():
            digest, original = line.split('  ', 1)
            need(re.fullmatch('[0-9a-f]{64}', digest), 'Invalid inherited input pin')
            mapped = CONTROL_MAP.get(original, original) if name == SCOUT + 'set_code_lane/INPUT_PINS.sha256' else original
            physical = Path(mapped) if mapped.startswith('/') else (base if selected(mapped) else ROOT) / mapped
            need(sha(physical.read_bytes()) == digest, 'Inherited input mismatch: ' + original)
            inherited.append({'list': name, 'key': original, 'mapped': mapped, 'sha256': digest})
    return {'packages': packages, 'inherited_inputs': inherited, 'set_control_mapping': CONTROL_MAP,
            'desk_control_mapping': 'Already literal snapshot paths in residual_desk/INPUT_PINS.sha256'}

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
        baseline = selected_tree(command, BASE)
        need(set(baseline) <= set(values), 'Selected baseline path missing from live scope')
        need(values == inventory() and roles == protected_roles(), 'Read-only preparation input changed')
        plan = {'schema': 'closed-scout-checkpoint-plan-v1', 'status': 'PREPARED_NOT_AUTHORIZED_OR_EXECUTED',
                'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'source_sha256': key(Path(__file__).resolve())['sha256'],
                'base': BASE, 'base_tree': BASE_TREE, 'mirror_base': MIRROR_BASE, 'remote_url': REMOTE,
                'identity': list(IDENTITY), 'roots': list(ROOTS), 'excluded': list(EXCLUDED),
                'inventory': values, 'baseline_selected': baseline, 'protected_roles': roles, 'artifacts': inherited,
                'selected_bytes': sum(v['bytes'] for v in values.values()),
                'private_only': True, 'new_scientific_runs': 0,
                'later_receipts_excluded': True, 'baseline_nonselected_policy': 'Preserve exactly; verify complete raw diff.'}
        save(directory / 'PLAN.json', plan)
        seal = finish(directory, {'status': 'PASS_READONLY_PREPARATION', 'selected_paths': len(values),
              'selected_bytes': plan['selected_bytes'], 'baseline_selected_paths': len(baseline),
              'commands': command.count, 'plan_sha256': key(directory / 'PLAN.json')['sha256'],
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
    need(plan['schema'] == 'closed-scout-checkpoint-plan-v1' and tuple(plan['roots']) == ROOTS
         and tuple(plan['excluded']) == EXCLUDED and plan['base'] == BASE and plan['base_tree'] == BASE_TREE
         and plan['remote_url'] == REMOTE and plan['mirror_base'] == MIRROR_BASE
         and tuple(plan['identity']) == IDENTITY and plan['new_scientific_runs'] == 0,
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
                need(key(ROOT / name) == expected, 'Source changed before frozen copy')
                target = run / 'frozen' / name
                target.parent.mkdir(parents=True, exist_ok=True)
                save(target, (ROOT / name).read_bytes())
                target.chmod(0o555 if expected['mode'] == '100755' else 0o444)
                need(key(target) == expected and key(ROOT / name) == expected, 'Frozen copy/source race')
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
