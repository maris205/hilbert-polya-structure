#!/usr/bin/env python3
"""Source-only draft: scoped capture/stage/commit/push after actual five-paper closure.

No worktree copy, implicit deletion, force push, config write or broad object
body capture. completion_binding is the sole not-yet-bound actual-evidence
adapter; root must bind/read the final source and seal before any execution.
"""
import argparse
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
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_five_completion_sync_preparation'
SCRIPT = PREP / 'sync_five.py'
BARE = Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
BASE = '36e7b365b35f454d6fa94d6674746eafde314872'
BASE_TREE = '57efe318eda9575fa785463358cacf9efc2dd3cd'
ROOTS = ('SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers204_208_sequence',
    'papers/204-previous-smaller-distance-feedback',
    'papers/205-conflict-triggered-cyclic-increments',
    'papers/206-ternary-cyclic-record-feedback',
    'papers/207-upper-neighbor-rank-dynamics',
    'papers/208-original-snapshot-triangulation-sweeps',
    'papers/209-ordered-fibre-threading',
    'papers/210-weakly-increasing-run-aggregation')
EXCLUDED = 'docs/papers204_208_sequence/qa/p209_completion_private_checkpoint'
LIMIT = 100000000
PHASES = ('capture', 'stage', 'commit', 'push')
PLAN_SHA = '821b8957e15da2563350dd11f2bdf231f44c435cfe022f4d1334af5e8fe5f1cb'
README_SHA = '14429cc014b6c00fa64238ad4010540de3ded7bd0762ccd678035e88a6c35fe8'
IDENTITY = ('mariswang', 'wangliang.f@gmail.com')
BASE_ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC',
    'GIT_OPTIONAL_LOCKS': '0', 'GIT_TERMINAL_PROMPT': '0', 'GIT_CONFIG_NOSYSTEM': '1',
    'GIT_CONFIG_GLOBAL': '/dev/null',
    'GIT_SSH_COMMAND': 'ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=20 -o ConnectionAttempts=1'}

def need(value, label):
    if not value:
        raise RuntimeError(label)

def save(path, value):
    body = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with Path(path).open('xb') as stream:
        stream.write(body)

def read(path):
    return json.loads(Path(path).read_bytes())

def key(path):
    path = Path(path)
    before = path.lstat()
    need(stat.S_ISREG(before.st_mode) and path.resolve() == path, 'Exact physical regular file: ' + str(path))
    sha, oid = hashlib.sha256(), hashlib.sha1(('blob ' + str(before.st_size) + '\0').encode())
    with path.open('rb') as stream:
        opened = os.fstat(stream.fileno())
        need((opened.st_dev, opened.st_ino) == (before.st_dev, before.st_ino), 'File replaced before open')
        for block in iter(lambda: stream.read(1 << 20), b''):
            sha.update(block); oid.update(block)
        ended = os.fstat(stream.fileno())
    after = path.lstat()
    fields = ('st_dev', 'st_ino', 'st_mode', 'st_size', 'st_mtime_ns', 'st_ctime_ns')
    need(all(getattr(before, f) == getattr(ended, f) == getattr(after, f) for f in fields), 'File changed during read')
    return dict(sha256=sha.hexdigest(), bytes=before.st_size, git_blob_sha1=oid.hexdigest(),
                mode='100755' if before.st_mode & 0o111 else '100644')

def pin(path):
    value = key(path)
    return {k: value[k] for k in ('sha256', 'bytes')}

def selected(name):
    return any(name == base or name.startswith(base + '/') for base in ROOTS) and not (
        name == EXCLUDED or name.startswith(EXCLUDED + '/'))

def members():
    result = set()
    for name in ROOTS:
        base = ROOT / name
        need(base.resolve() == base and not base.is_symlink(), 'Unaliased explicit root')
        if base.is_file():
            result.add(name)
            continue
        need(base.is_dir(), 'Missing explicit directory root')
        for directory, folders, files in os.walk(base):
            for folder in folders[:]:
                path = Path(directory) / folder
                need(not path.is_symlink(), 'No directory symlinks in selected scope')
                if not selected(path.relative_to(ROOT).as_posix()):
                    folders.remove(folder)
            for filename in files:
                path = Path(directory) / filename
                relative = path.relative_to(ROOT).as_posix()
                need(selected(relative) and path.is_file() and not path.is_symlink(), 'Exact selected regular member')
                need(not any(ord(c) < 32 or ord(c) == 127 for c in relative), 'Control character in Git pathname')
                result.add(relative)
    return sorted(result)

def inventory():
    names = members()
    values = {name: key(ROOT / name) for name in names}
    need(names == members(), 'Selected membership changed during capture')
    return values

def complete_manifest(base, expected):
    base = Path(base)
    need(base.resolve() == base and not base.is_symlink(), 'Exact package root')
    seal = base / 'SHA256SUMS'
    need(pin(seal)['sha256'] == expected, 'Exact complete package seal')
    rows = {}
    for line in seal.read_text().splitlines():
        digest, name = line.split('  ', 1)
        relative = Path(name)
        need(re.fullmatch('[0-9a-f]{64}', digest) and relative.parts and not relative.is_absolute() and
             '..' not in relative.parts and relative.as_posix() == name and name != 'SHA256SUMS' and
             name not in rows, 'Safe complete nonself manifest row')
        rows[name] = pin(base / name)
        need(rows[name]['sha256'] == digest, 'Package payload changed')
    paths = list(base.rglob('*'))
    need(not any(p.is_symlink() for p in paths) and set(rows) ==
         {p.relative_to(base).as_posix() for p in paths if p.is_file() and p != seal}, 'Complete package membership')
    return rows

def completion_binding():
    """Receive actual final originals; no gate, host-map or Git execution here.

    Only the three documentary roles in the pinned root refresh may use their
    exact physical old copies. All other prior inputs remain at their original
    paths. The unchanged caller verifies every returned pin and complete package.
    """
    spec_path = PREP / 'ACTUAL_COMPLETION_BINDING.json'
    spec_pin = {'bytes': 35292, 'sha256': 'a69c39ae89a6e5ab8ae230ecd2cabfec8e394ee93c6b8d3f4eef23e262192559'}
    need(pin(spec_path) == spec_pin, 'Exact actual completion binding data')
    spec = read(spec_path)
    need(spec['schema'] == 'actual-five-completion-private-sync-binding-v1' and
         spec['external'] == 'OWNER_AMBER / HOLD_EXTERNAL', 'Bound actual completion schema and hold')
    pins = {str(spec_path): spec_pin}

    def keep(path, expected=None):
        name = str(path)
        expected = spec['pins'][name] if expected is None else expected
        need(Path(name).is_absolute() and set(expected) == {'bytes', 'sha256'} and
             type(expected['bytes']) is int and expected['bytes'] >= 0 and
             re.fullmatch('[0-9a-f]{64}', expected['sha256']), 'Exact absolute byte-pin schema')
        need(name not in pins or pins[name] == expected, 'Conflicting actual completion input')
        pins[name] = expected
        return expected

    def actual(path):
        need(pin(path) == keep(path), 'Actual original bytes changed: ' + str(path))
        return read(path)

    def fields(value, expected):
        need(all(k in value and type(value[k]) is type(v) and value[k] == v for k, v in expected.items()),
             'Exact typed actual completion fields')

    native = {}
    for chain in spec['native_chains']:
        launch, done = actual(QA / chain['launch']), actual(QA / chain['completion'])
        need(launch['command'] == chain['command'] and launch['cwd'] == str(ROOT) and
             launch['result']['output'] == '' and 'exit_code' not in launch['result'] and
             launch['result']['session_id'] == done['session_id'] == chain['session'] and
             done['launch_record'] == chain['launch'] and done['result']['exit_code'] == 0 and
             'session_id' not in done['result'], 'Actual separate normal native closure before gate streams')
        need(done['result']['output'] == json.dumps(chain['summary'], sort_keys=True) + '\n',
             'Entire actual native stdout, not transport excerpt')
        native[chain['role']] = chain['summary']
    accepted = actual(QA / 'FIVE_EXACT_ROOT_ACCEPTANCE.actual.json')
    fields(accepted, spec['acceptance_fields'])
    prep, out = QA / 'five_paper_terminal_exact_revision_02', QA / 'five_paper_terminal_exact_run_02'
    result, attempt, spawn = (actual(out / n) for n in ('RESULT.json', 'ATTEMPT.json', 'SPAWN.json'))
    seal = keep(prep / 'SHA256SUMS')['sha256']
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
        'pycache_prefix=' + str(out / 'never_created_reader_cache'), str(prep / 'inspect_five.py'),
        '--expected-preparation-sha256', seal]
    env = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
    need(result['argv'] == argv and result['cwd'] == str(ROOT) and result['environment'] == env and
         type(result['original_wait_exit_code']) is type(result['cleanup_wait_exit_code']) is int and
         result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and
         result['timed_out'] is False and result['wait_error'] is None and result['cleanup_events'] == [] and
         result['child_reaped'] is result['process_group_absent'] is result['inputs_unchanged'] is
         result['all_five_terminal_evidence_present_after'] is True and
         result['inputs_before'] == result['inputs_after'], 'Actual clean gate capture interval')
    need(attempt == dict(argv=argv, cwd=str(ROOT), environment=env, inputs_before=result['inputs_before'],
         timeout_seconds=1800, start_new_session=True, started_epoch=attempt['started_epoch'],
         all_five_terminal_evidence_present_before=True) and
         spawn == dict(pid=result['pid'], process_group_id=result['pid'], spawned_epoch=spawn['spawned_epoch']) and
         type(result['pid']) is int and result['pid'] == 786046 and
         attempt['started_epoch'] <= spawn['spawned_epoch'] <= result['finished_epoch'] and
         group_absent(result['pid']) and not os.path.lexists(out / 'UNCLOSED.json') and
         not os.path.lexists(out / 'never_created_reader_cache'), 'Actual settled gate attempt and owned group')
    report = actual(out / 'FIVE_REPORT.json')
    fields(report, spec['report_fields'])
    need(result['stdout'] == keep(out / 'FIVE_REPORT.json') == accepted['complete_gate_stdout'] and
         result['stderr'] == keep(out / 'stderr') and (out / 'stderr').read_bytes() == b'' and
         accepted['gate_output_seal'] == keep(out / 'SHA256SUMS') and
         accepted['complete_current_map'] == report['complete_current_file_map'] and
         (out / 'executed_source.py').read_bytes() == (QA / 'record_five_terminal_exact_02.py').read_bytes(),
         'Accepted complete raw gate output, separate stderr and actual executed source')
    need(native['gate'] == dict(status='PASS_ACTUAL_EXACT_FIVE_CAPTURE', output=str(out),
         original_wait_exit_code=0, stdout=result['stdout'], stderr=result['stderr'], result=keep(out / 'RESULT.json'),
         seal=keep(out / 'SHA256SUMS'), checks=report['checks'], current_path_keys=report['complete_current_file_keys'],
         root_acceptance=False, five_paper_completion=False) and
         native['receiver']['full_raw'] == accepted['complete_gate_stdout'] and
         native['receiver']['complete_current_map'] == accepted['complete_current_map'] and
         native['receiver']['checks'] == accepted['root_receiver_checks'],
         'Actual gate and separate receiver summaries bind formal acceptance')
    retry = actual(QA / 'FIVE_COMPLETION_INDEX_REFRESH_ROOT_RETRY.actual.json')
    raw_documentary = retry['result']['output'].encode()
    need(retry['cwd'] == str(ROOT) and retry['result']['exit_code'] == 0 and
         'session_id' not in retry['result'] and retry['prior_incomplete_transport_record'] ==
         'FIVE_COMPLETION_INDEX_REFRESH_ROOT.actual.json' and
         dict(bytes=len(raw_documentary), sha256=hashlib.sha256(raw_documentary).hexdigest()) ==
         spec['documentary_stdout'], 'Actual complete documentary retry, truncated predecessor not adopted')
    doc = json.loads(raw_documentary)
    fields(doc, spec['documentary_fields'])
    need(set(doc) == set(spec['documentary_fields']) | {'unchanged_live_scientific_pins'} and
         raw_documentary == (json.dumps(doc, sort_keys=True) + '\n').encode() and
         doc['root_acceptance'] == keep(QA / 'FIVE_EXACT_ROOT_ACCEPTANCE.actual.json') and
         doc['unchanged_mathematical_ceilings'] == accepted['all_five_mathematical_ceilings'] ==
         report['current_live_theorem_ceilings'], 'Complete current documentary scope and unchanged five ceilings')
    controls = doc['current_indexes']
    need(set(controls) == {str(ROOT / 'SYMBOLIC_DYNAMICS_STATE.md'), str(QA.parent / 'PIPELINE_STATE.md'),
         str(QA.parent / 'FINAL_THEOREM_CONTRACTS.md')}, 'Exactly three final documentary old roles')
    history = QA / 'central_five_completion_01'
    copies = actual(history / 'PRESERVATION.actual.json')['copies']
    for name, row in controls.items():
        need(row['physical_history'] == str(history / Path(name).name) and
             copies[name] == dict(physical=row['physical_history'], **row['before']) and
             report['complete_current_read_keys'][name] == dict(real=name, size=row['before']['bytes'],
             sha256=row['before']['sha256'], symlink=None), 'Exact old rich field and physical history role')
        keep(name, row['after']); keep(row['physical_history'], row['before'])
    prepared = actual(prep / 'ACTUAL_BINDING.json')
    for values, count in ((result['inputs_before'], 21), (prepared['fixed_inputs'], 71)):
        need(len(values) == count and set(controls) <= set(values), 'Entire actual original input map')
        for name, expected in values.items():
            if name in controls:
                need(expected == controls[name]['before'], 'No generic stale-file substitution')
                keep(controls[name]['physical_history'], expected)
            else:
                keep(name, expected)
    need(len(accepted['input_pins']) == 20, 'Entire formal root acceptance input map')
    for name, expected in accepted['input_pins'].items():
        keep(name, expected)
    need(len(doc['unchanged_live_scientific_pins']) == 83 and len(doc['unchanged_whole_manifest_pins']) == 5,
         'All actual unchanged scientific and literal whole-manifest roles')
    for name, expected in {**doc['unchanged_live_scientific_pins'], **doc['unchanged_whole_manifest_pins']}.items():
        need(report['complete_current_read_keys'][name] == dict(real=name, size=expected['bytes'],
             sha256=expected['sha256'], symlink=None), 'Unchanged accepted scientific or whole-manifest rich row')
        keep(name, expected)
    for name, expected in doc['documents'].items():
        keep(name, expected)
    keep(QA.parent / 'GIT_SYNC_RECEIPT.md', doc['unchanged_git_receipt'])
    keep(history / 'GIT_SYNC_RECEIPT.md', doc['unchanged_git_receipt'])
    for name, expected in spec['pins'].items():
        keep(name, expected)
    packages = spec['packages']
    need(packages and len({p['path'] for p in packages}) == len(packages) and
         all(set(p) == {'path', 'seal'} for p in packages), 'Explicit unique complete SHA256SUMS package roles')
    for package in packages:
        need(keep(Path(package['path']) / 'SHA256SUMS')['sha256'] == package['seal'],
             'Literal complete package seal, not a PAPER_MANIFEST substitute')
    return {'pins': dict(sorted(pins.items())), 'packages': packages}

def readonly_roles():
    # The script never mutates these old repository roles or the default index.
    paths = [MIRROR / '.git' / n for n in ('config', 'index', 'HEAD', 'packed-refs')]
    paths += [BARE / n for n in ('config', 'index')]
    for base in (MIRROR / '.git/refs', MIRROR / '.git/objects/info', BARE / 'objects/info'):
        if base.exists():
            paths += [p for p in base.rglob('*') if p.is_file()]
    return {str(p): pin(p) if p.is_file() else None for p in sorted(set(paths))}

def group_absent(pid):
    try:
        os.killpg(pid, 0)
        return False
    except ProcessLookupError:
        return True

def interrupted(signum, frame):
    raise KeyboardInterrupt('Interrupted by signal ' + str(signum))

class Commands:
    def __init__(self, directory, index):
        self.directory, self.index, self.count = directory, index, 0
        self.env = {**BASE_ENV, 'GIT_INDEX_FILE': str(index)}
        self.prefix = ['/usr/bin/git', '-C', str(BARE),
            '-c', 'include.path=' + str(MIRROR / '.git/config'), '-c', 'core.bare=true',
            '-c', 'core.fsmonitor=false', '-c', 'gc.auto=0',
            '-c', 'core.sparseCheckout=false', '-c', 'core.splitIndex=false',
            '-c', 'core.hooksPath=' + str(index.parent / 'empty_hooks'),
            '-c', 'commit.gpgSign=false', '-c', 'user.name=' + IDENTITY[0], '-c', 'user.email=' + IDENTITY[1]]

    def git(self, *args, stdin=b'', allowed=(0,)):
        self.count += 1
        directory = self.directory / ('command_' + str(self.count).zfill(4))
        directory.mkdir()
        argv = self.prefix + list(args)
        save(directory / 'stdin', stdin)
        attempt = dict(argv=argv, cwd=str(ROOT), environment=self.env, stdin=pin(directory / 'stdin'),
                       timeout_seconds=1800, start_new_session=True, started_epoch=time.time())
        save(directory / 'ATTEMPT.json', attempt)
        proc, original_exit, error, cleanup = None, None, None, []
        with (directory / 'stdout').open('xb') as stdout, (directory / 'stderr').open('xb') as stderr:
            try:
                proc = subprocess.Popen(argv, cwd=ROOT, env=self.env, stdin=subprocess.PIPE,
                    stdout=stdout, stderr=stderr, start_new_session=True)
                save(directory / 'SPAWN.json', dict(pid=proc.pid, process_group_id=proc.pid))
                proc.communicate(input=stdin, timeout=1800)
                original_exit = proc.returncode
            except BaseException:
                error = traceback.format_exc()
            if proc is not None and not group_absent(proc.pid):
                for sig in (signal.SIGTERM, signal.SIGKILL):
                    event = dict(signal=int(sig), started_epoch=time.time())
                    cleanup.append(event)
                    try:
                        os.killpg(proc.pid, sig)
                    except ProcessLookupError:
                        event['already_absent'] = True
                    try:
                        proc.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        pass
                    if group_absent(proc.pid):
                        break
        settled = proc is not None and proc.returncode is not None and group_absent(proc.pid)
        result = dict(original_exit=original_exit, original_error=error, cleanup=cleanup,
                      child_reaped=proc is not None and proc.returncode is not None,
                      process_group_absent=group_absent(proc.pid) if proc is not None else None,
                      cleanup_exit=proc.returncode if proc is not None else None, finished_epoch=time.time())
        if settled:
            result['streams'] = {name: pin(directory / name) for name in ('stdout', 'stderr')}
        save(directory / 'RESULT.json', result)
        need(settled and error is None and not cleanup and original_exit in allowed, 'Native command failed; raw evidence retained')
        return (directory / 'stdout').read_bytes()

def tree_map(command, tree):
    data = command.git('ls-tree', '-r', '-z', '--full-tree', tree)
    need(not data or data.endswith(b'\0'), 'Full tree NUL framing')
    result = {}
    for line in data.split(b'\0')[:-1]:
        attrs, name = line.split(b'\t', 1)
        mode, kind, oid = attrs.decode().split()
        name = name.decode()
        need(name not in result and re.fullmatch('[0-9a-f]{40}', oid), 'Exact unique tree path/OID')
        result[name] = dict(mode=mode, kind=kind, oid=oid)
    return result

def repository_base(command):
    need(command.git('rev-parse', '--is-bare-repository').strip() == b'true', 'Exact bare role')
    need(command.git('symbolic-ref', 'HEAD').strip() == b'refs/heads/main', 'Exact accepted main HEAD')
    need(command.git('rev-parse', 'HEAD').strip().decode() == BASE, 'Accepted baseline advanced; do not overwrite')
    need(command.git('rev-parse', 'HEAD^{tree}').strip().decode() == BASE_TREE, 'Accepted baseline tree')
    remote(command, BASE)

def remote(command, expected):
    need(command.git('ls-remote', '--exit-code', 'origin', 'refs/heads/main').decode().split() ==
         [expected, 'refs/heads/main'], 'Actual remote agreement; remote advance requires root resolution')

def require_guard(capture, binding, roles):
    need(binding == capture['completion_binding'] and roles == capture['readonly_roles'], 'Changed completion/config/old-repository dependency')
    for path, value in binding['pins'].items():
        need(pin(path) == value, 'Changed exact completed-gate/control input')
    need(inventory() == capture['selected'], 'Changed selected pathname/mode/bytes after capture')
    for package in binding['packages']:
        complete_manifest(Path(package['path']), package['seal'])
    need(readonly_roles() == roles, 'Protected old repository/config/index changed')

def expected_tree(capture):
    result = dict(capture['base_tree_entries'])
    for name, value in capture['selected'].items():
        result[name] = dict(mode=value['mode'], kind='blob', oid=value['git_blob_sha1'])
    return result

def capacity(capture, run):
    # Loose objects plus a possible push pack and bounded metadata/log reserve;
    # no space is reserved for a paper/worktree copy because none is made.
    unique = {v['git_blob_sha1']: v['bytes'] for v in capture['changed'].values()}
    required = 2 * sum(unique.values()) + (1 << 30)
    for path in (BARE, run):
        usage = os.statvfs(path)
        need(usage.f_bavail * usage.f_frsize >= required, 'Insufficient checked destination/evidence capacity')
    return required

def verify_selected_objects(command, capture):
    unique = {}
    for value in capture['selected'].values():
        oid = value['git_blob_sha1']
        need(oid not in unique or unique[oid] == value['bytes'], 'Conflicting object size')
        unique[oid] = value['bytes']
    data = command.git('cat-file', '--batch-check', stdin=''.join(oid + '\n' for oid in sorted(unique)).encode())
    need(data == ''.join(oid + ' blob ' + str(unique[oid]) + '\n' for oid in sorted(unique)).encode(),
         'Every selected object type/OID/size without object-body capture')

def verify_stage(command, capture, tree):
    expected = expected_tree(capture)
    need(tree_map(command, tree) == expected, 'Entire tree: selected exact, unrelated preserved, zero deletions')
    raw_index = command.git('ls-files', '--stage', '-z')
    index = {}
    for line in raw_index.split(b'\0')[:-1]:
        attrs, name = line.split(b'\t', 1)
        mode, oid, stage = attrs.decode().split()
        need(stage == '0' and name.decode() not in index, 'No unmerged/duplicate temporary index entry')
        index[name.decode()] = (mode, oid)
    need(index == {n: (v['mode'], v['oid']) for n, v in expected.items()}, 'Entire isolated index matches complete tree')
    need(not any(n == EXCLUDED or n.startswith(EXCLUDED + '/') for n in expected), 'Full 306-file package excluded')
    verify_selected_objects(command, capture)

def phase_chain(run, phase, expected):
    position = PHASES.index(phase)
    if position == 0:
        need(expected is None, 'Capture has no invented prior phase')
        return None
    previous = PHASES[position - 1]
    directory = run / previous
    complete_manifest(directory, expected)
    result = read(directory / 'RESULT.json')
    need(result['status'] == 'PASS_PRIVATE_SYNC_' + previous.upper() and result['phase'] == previous,
         'Actual successful preceding phase')
    phase_chain(run, previous, result['previous_phase_sha256'])
    return result

def finish(directory, value):
    save(directory / 'RESULT.json', value)
    paths = sorted(p for p in directory.rglob('*') if p.is_file())
    save(directory / 'SHA256SUMS', ''.join(pin(p)['sha256'] + '  ' + p.relative_to(directory).as_posix() + '\n'
                                         for p in paths).encode())
    complete_manifest(directory, pin(directory / 'SHA256SUMS')['sha256'])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=PHASES)
    parser.add_argument('--run', required=True)
    parser.add_argument('--expected-preparation-sha256', required=True)
    parser.add_argument('--expected-previous-phase-sha256')
    args = parser.parse_args()
    need(Path(__file__) == SCRIPT and Path.cwd() == ROOT and sys.executable == '/usr/bin/python3.10' and
         sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.dont_write_bytecode, 'Exact source-only invocation')
    complete_manifest(PREP, args.expected_preparation_sha256)
    need(pin(PREP / 'README.md')['sha256'] == README_SHA and pin(PREP / 'SCOPE.json')['sha256'] == PLAN_SHA,
         'Approved historical scope documents unchanged')
    plan = read(PREP / 'SCOPE.json')
    need(tuple(p['workspace_relative'] for p in plan['candidate_roots']) == ROOTS and
         all(p['workspace_relative'] == p['git_relative'] for p in plan['candidate_roots']), 'Only approved nine identity roots')
    binding = completion_binding()  # Must fail before output creation/Git while no actual final binding exists.
    need(set(binding) == {'pins', 'packages'} and binding['pins'] and binding['packages'], 'Actual completion dependency roles')
    for path, value in binding['pins'].items():
        need(pin(path) == value, 'Exact actual completion input')
    for package in binding['packages']:
        base = Path(package['path'])
        need(base.is_relative_to(ROOT) and selected(base.relative_to(ROOT).as_posix()), 'Completed package inside approved roots')
        complete_manifest(base, package['seal'])
    run = Path(args.run)
    need(run.is_absolute() and run.parent == Path('/root') and
         re.fullmatch('symbolic-dynamics-private-sync-final-five-[0-9]+', run.name) and run.resolve() == run,
         'Fresh bounded outside-workspace evidence directory')
    if args.phase == 'capture':
        need(not os.path.lexists(run) and args.expected_previous_phase_sha256 is None, 'No capture overwrite/retry')
        run.mkdir(mode=0o700)
        index_dir = Path(tempfile.mkdtemp(prefix='index-', dir=run))
        (index_dir / 'empty_hooks').mkdir()
        save(run / 'RUN.json', dict(index=str(index_dir / 'index'), source=pin(SCRIPT),
             preparation=pin(PREP / 'SHA256SUMS'), output_scope='Outside workspace and outside selected tree'))
        save(run / 'executed_source.py', SCRIPT.read_bytes())
    else:
        need(run.is_dir() and args.expected_previous_phase_sha256 is not None, 'Actual prior run and phase seal required')
    info = read(run / 'RUN.json')
    need(info['source'] == pin(SCRIPT) and info['preparation'] == pin(PREP / 'SHA256SUMS') and
         pin(run / 'executed_source.py') == pin(SCRIPT), 'Exact run/source/preparation chain')
    index = Path(info['index'])
    need(index.parent.parent == run and index.name == 'index' and index.resolve() == index, 'Owned separate temporary index')
    prior = phase_chain(run, args.phase, args.expected_previous_phase_sha256)
    directory = run / args.phase
    need(not os.path.lexists(directory), 'No phase overwrite or automatic retry')
    directory.mkdir()
    command = Commands(directory, index)
    roles = readonly_roles()
    for sig in (signal.SIGTERM, signal.SIGHUP):
        signal.signal(sig, interrupted)
    try:
        repository_base(command)
        if args.phase == 'capture':
            need(not os.path.lexists(index), 'No preexisting temporary index')
            baseline = tree_map(command, BASE)
            need(not any(n == EXCLUDED or n.startswith(EXCLUDED + '/') for n in baseline), 'Accepted tree old exclusion remains entire')
            selected_keys = inventory()
            need(all(n in selected_keys for n in baseline if selected(n)), 'No disappeared tracked scoped path')
            changes = {n: v for n, v in selected_keys.items() if baseline.get(n) !=
                       dict(mode=v['mode'], kind='blob', oid=v['git_blob_sha1'])}
            need(changes and all(v['bytes'] <= LIMIT for v in changes.values()), 'No oversized new/changed blob')
            capture = dict(selected=selected_keys, changed=changes, base_tree_entries=baseline,
                           completion_binding=binding, readonly_roles=roles, run_inputs={
                           'RUN.json': pin(run / 'RUN.json'), 'executed_source.py': pin(run / 'executed_source.py')})
            capacity(capture, run)
            require_guard(capture, binding, roles)
            save(directory / 'CAPTURE.json', capture)
            result = dict(selected_paths=len(selected_keys), changed_paths=len(changes),
                          selected_apparent_bytes=sum(v['bytes'] for v in selected_keys.values()))
        else:
            capture = read(run / 'capture/CAPTURE.json')
            need(all(pin(run / name) == value for name, value in capture['run_inputs'].items()), 'Exact captured run metadata')
            require_guard(capture, binding, roles)
            capacity(capture, run)
            if args.phase == 'stage':
                need(not os.path.lexists(index), 'New index only')
                command.git('read-tree', BASE)
                # Existing complete tree object identities are reused; only changed
                # source paths go through hash-object and no filter is applied.
                paths = sorted(capture['changed'])
                input_paths = ''.join('"' + str(ROOT / n).replace('\\', '\\\\').replace('"', '\\"') + '"\n' for n in paths)
                written = command.git('hash-object', '-w', '--no-filters', '--stdin-paths', stdin=input_paths.encode()).decode().splitlines()
                need(written == [capture['changed'][n]['git_blob_sha1'] for n in paths], 'Only exact captured changed object bytes written')
                require_guard(capture, binding, roles)
                data = b''.join((v['mode'] + ' ' + v['git_blob_sha1'] + '\t' + n).encode() + b'\0'
                                for n, v in sorted(capture['changed'].items()))
                command.git('update-index', '-z', '--index-info', stdin=data)
                tree = command.git('write-tree').decode().strip()
                verify_stage(command, capture, tree)
                result = dict(tree=tree)
            elif args.phase == 'commit':
                tree = prior['tree']
                verify_stage(command, capture, tree)
                commit = command.git('commit-tree', tree, '-p', BASE, stdin=
                    b'Complete scoped five-paper batch P205 P207 P208 P209 P210; preserve rejected drafts and local-only oversized package; HOLD_EXTERNAL\n').decode().strip()
                need(command.git('rev-list', '--parents', '-n', '1', commit).decode().split() == [commit, BASE],
                     'Exact normal single-parent commit')
                need(command.git('rev-parse', commit + '^{tree}').decode().strip() == tree, 'Committed tree identity')
                need(command.git('show', '-s', '--format=%an%x00%ae%x00%cn%x00%ce', commit).decode().rstrip('\n').split('\0') ==
                     [*IDENTITY, *IDENTITY], 'Previously documented command-local identity; no config write')
                result = dict(tree=tree, commit=commit, local_main_not_changed=True)
            else:
                tree, commit = prior['tree'], prior['commit']
                verify_stage(command, capture, tree)
                need(command.git('rev-list', '--parents', '-n', '1', commit).decode().split() == [commit, BASE] and
                     command.git('rev-parse', commit + '^{tree}').decode().strip() == tree, 'Actual committed object chain')
                remote(command, BASE)
                require_guard(capture, binding, roles)
                command.git('push', '--porcelain', 'origin', commit + ':refs/heads/main')
                remote(command, commit)
                command.git('update-ref', 'refs/heads/main', commit, BASE)
                need(command.git('rev-parse', 'HEAD').decode().strip() == commit, 'CAS local main after actual normal push')
                remote(command, commit)
                need(tree_map(command, commit) == expected_tree(capture), 'Final exact committed complete tree')
                result = dict(tree=tree, commit=commit, actual_remote_confirmed=True,
                              bare_worktree_status='N/A', excluded_old_package=EXCLUDED)
        require_guard(capture, binding, roles)
        result.update(status='PASS_PRIVATE_SYNC_' + args.phase.upper(), phase=args.phase,
                      base=BASE, commands=command.count, source=pin(SCRIPT),
                      previous_phase_sha256=args.expected_previous_phase_sha256,
                      no_worktree_copy=True, no_deletions=True, no_force_push=True,
                      no_new_bulk_object_body_capture=True, external='OWNER_AMBER / HOLD_EXTERNAL')
        finish(directory, result)
        print(json.dumps({**result, 'phase_seal': pin(directory / 'SHA256SUMS')}, sort_keys=True))
        return 0
    except BaseException:
        save(directory / 'FAILURE.json', dict(phase=args.phase, commands=command.count,
             exception=traceback.format_exc(), raw_evidence_preserved=True,
             scope='No rollback, retries, deletion, force push or inferred remote success. Inspect real command originals.'))
        raise

if __name__ == '__main__':
    raise SystemExit(main())
