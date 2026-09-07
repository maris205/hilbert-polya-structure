#!/usr/bin/env python3
"""Read-only root reception of the actual scoped private checkpoint.

Writes only a fresh local reception package. Never imports the sync executor,
copies/stages/commits/pushes, changes a central control, or runs science.
"""
from pathlib import Path
from hashlib import sha256, sha1
import gzip
import json
import os
import re
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
QA = ROOT / 'docs/papers204_208_sequence/qa'
EXECUTION = QA / 'p209_completion_private_checkpoint'
FINAL = EXECUTION / 'attempt_03'
OUT = QA / 'p209_completion_root_reception'
BASE = '4bc38b63e7e0bbfd5365c08e5635ebc7ac9af953'
HEAD = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
TREE = '9cedcdbde3ee647a1bc60b56afcfe7c63e05c466'
SEAL = 'd9af32a696d22846ce777da1b55cc43fcb19c8ad0deedf78ab6ee924bf0d70d5'
CODE = '0850e7f0065f5abc0497c522cbc64c417c6492b8e9d62c6f2a45228ad95917f3'
CHECKS, COMMANDS, READS = 0, [], {}


def ck(test, detail):
    global CHECKS
    CHECKS += 1
    assert test, detail


def meta(path, blob=False):
    path = Path(path)
    ck(path.is_file() and not path.is_symlink(), ('ordinary file', str(path)))
    size = path.stat().st_size
    h = sha256(); b = sha1(b'blob ' + str(size).encode() + b'\0')
    read_size = 0
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk); b.update(chunk); read_size += len(chunk)
    ck(read_size == size, ('stable size', str(path)))
    result = {'bytes': size, 'sha256': h.hexdigest()}
    ck(str(path) not in READS or READS[str(path)] == result, ('stable bytes', str(path)))
    READS[str(path)] = result
    return dict(result, git_blob_sha1=b.hexdigest()) if blob else result


def obj(path):
    meta(path)
    return json.loads(Path(path).read_bytes())


def save(name, value):
    data = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with (OUT / name).open('xb') as stream:
        stream.write(data)


def seal(base, expected, count):
    ck(meta(base / 'SHA256SUMS')['sha256'] == expected, ('sealed manifest', str(base)))
    rows = {}
    for line in (base / 'SHA256SUMS').read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(match is not None, 'manifest syntax')
        h, name = match.groups(); path = Path(name)
        ck(not path.is_absolute() and '..' not in path.parts and name not in rows and name != 'SHA256SUMS', 'safe nonself path')
        rows[name] = h
        ck(meta(base / name)['sha256'] == h, ('payload', name))
    ck(len(rows) == count and {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} == set(rows) | {'SHA256SUMS'}, ('complete seal', str(base)))
    ck(all(not p.is_symlink() for p in base.rglob('*')), 'no package symlink')


def git(args):
    index = len(COMMANDS) + 1
    prefix = 'git_%02d' % index
    argv = ['/usr/bin/git', '-C', str(MIRROR)] + args
    override = {'GIT_OPTIONAL_LOCKS': '0', 'GIT_TERMINAL_PROMPT': '0', 'GIT_LITERAL_PATHSPECS': '1' if args[0] == 'ls-tree' else '0',
                'GIT_SSH_COMMAND': 'ssh -o BatchMode=yes -o ConnectTimeout=20 -o ConnectionAttempts=1'}
    row = {'argv': argv, 'cwd': str(ROOT), 'environment_overrides': override, 'started_epoch': time.time(), 'exit_code': None, 'timeout_seconds': 45}
    save(prefix + '.attempt.json', row)
    try:
        run = subprocess.run(argv, cwd=ROOT, env=dict(os.environ, **override), capture_output=True, timeout=45, check=False)
        stdout, stderr = run.stdout, run.stderr
        row.update(exit_code=run.returncode, status='COMPLETED', streams_complete=True)
    except subprocess.TimeoutExpired as exc:
        stdout, stderr = exc.stdout or b'', exc.stderr or b''
        row.update(status='TIMED_OUT', streams_complete=False, failure=repr(exc))
    except OSError as exc:
        stdout = stderr = b''
        row.update(status='SPAWN_FAILED', streams_complete=False, failure=repr(exc))
    save(prefix + '.stdout.raw', stdout); save(prefix + '.stderr.raw', stderr)
    row.update(finished_epoch=time.time(), stdout=meta(OUT / (prefix + '.stdout.raw')), stderr=meta(OUT / (prefix + '.stderr.raw')))
    COMMANDS.append(row); save(prefix + '.receipt.json', row)
    ck(row['exit_code'] == 0 and row['streams_complete'], ('fresh native Git completion', row))
    return stdout


def main():
    ck(not os.path.lexists(OUT), 'exclusive reception output')
    OUT.mkdir()
    save('SOURCE_PIN.json', {'source': str(Path(__file__).resolve()), 'pin': meta(Path(__file__).resolve())})
    seal(EXECUTION, SEAL, 305)
    ck(meta(FINAL / 'execute.py')['sha256'] == CODE, 'fully read final executor identity')
    phases = {}
    native_count = 0
    wanted = {'prepare': 'PASS_FROZEN_SELECTION_AND_NINE_PATH_AMENDMENT', 'copy': 'PASS_EXACT_1482_PATH_COPY_NOT_STAGED',
              'stage': 'PASS_EXACT_STAGED_TREE_NOT_COMMITTED', 'commit': 'PASS_EXACT_COMMITTED_TREE_NOT_PUSHED', 'push': 'PASS_NORMAL_PRIVATE_PUSH_ACTUAL_REMOTE_CONFIRMED'}
    for phase, status in wanted.items():
        result = phases[phase] = obj(FINAL / phase / 'RESULT.actual.json')
        ck(result['status'] == status and result['executor_sha256'] == CODE and result['started_epoch'] <= result['finished_epoch'], ('actual phase', phase))
        for index, row in enumerate(result['native_commands'], 1):
            ck(row == obj(FINAL / phase / ('command_%03d.actual.json' % index)), ('entire native record', phase, index))
            ck(row['started_epoch'] <= row['finished_epoch'], 'native chronology')
            for stream in ('stdin', 'stdout', 'stderr'):
                if stream in row:
                    info = row[stream]; ck(meta(FINAL / info['path']) == {k: info[k] for k in ('bytes', 'sha256')}, ('full native stream', phase, index, stream))
            ck(row['exit_code'] in (0, 1), ('actual success/expected nonmatch exit', phase, index))
            if row['exit_code'] == 1:
                ck(row['argv'][3] in ('check-ignore', 'config'), 'only expected absence exits')
            native_count += 1
        wrapper = obj(EXECUTION / (phase.upper() + '_03.actual_tool_return.json'))
        returns = [wrapper['start']] + wrapper.get('polls', []) if 'start' in wrapper else [wrapper['native_return']]
        completed = [r for r in returns if r.get('exit_code') is not None]
        ck(len(completed) == 1 and completed[0]['exit_code'] == 0, ('actual outer return', phase))
        short = json.loads(completed[0]['output'])
        ck(all(result.get(k) == v for k, v in short.items()), ('complete native summary crosslink', phase))
    prepared, staged, committed, pushed = (phases[n] for n in ('prepare', 'stage', 'commit', 'push'))
    ck(prepared['selected_count'] == 1482 and len(prepared['pins']) == 12555 and prepared['named_manifest_count'] == 19 and prepared['named_manifest_payload_rows'] == 12474, 'exact scope census')
    ck(staged['tree'] == committed['tree'] == pushed['tree'] == TREE and committed['commit'] == pushed['commit'] == pushed['actual_remote_commit'] == HEAD and committed['parent'] == BASE, 'actual stage commit push identity')
    ck(set(staged['staged_paths']) == set(committed['committed_changes']) == set(prepared['selected']) and staged['staged_paths'] == committed['committed_changes'], 'exact scope retained through commit')
    kinds = list(committed['committed_changes'].values())
    ck(kinds.count('A') == 1476 and kinds.count('M') == 6 and len(kinds) == 1482, 'no deletion or out of scope')
    for phase in (staged, committed):
        ck(phase['expected_blob_keys_checked'] == 12555 and phase['blob_payload_bytes_checked'] == 2940838098 and phase['all_byte_lengths_sha256_blob_sha1_matched'] and phase['complete_tree_coverage'], 'full actual blob phase')
    left = FINAL / staged['full_cat_file_stdout_lossless_gzip']['path']
    right = FINAL / committed['full_cat_file_stdout_lossless_gzip']['path']
    with left.open('rb') as a, right.open('rb') as b:
        while True:
            x, y = a.read(1024 * 1024), b.read(1024 * 1024)
            ck(x == y, 'complete compressed streams raw byte equality')
            if not x: break
    ck(staged['original_stdout'] == committed['original_stdout'], 'same recorded raw native stream')
    h = sha256(); length = payload = 0
    with gzip.open(left, 'rb') as stream:
        for name, expected in sorted(prepared['pins'].items()):
            header = stream.readline(); data = stream.read(expected['bytes']); end = stream.read(1)
            ck(header.decode().split() == [expected['git_blob_sha1'], 'blob', str(expected['bytes'])] and end == b'\n', ('exact native header', name))
            ck(len(data) == expected['bytes'] and sha256(data).hexdigest() == expected['sha256'] and sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == expected['git_blob_sha1'], ('full decompressed blob', name))
            h.update(header); h.update(data); h.update(end); length += len(header) + len(data) + 1; payload += len(data)
        ck(stream.read(1) == b'', 'no extra native bytes')
    ck({'bytes': length, 'sha256': h.hexdigest()} == staged['original_stdout'] and payload == 2940838098, 'lossless entire stream')
    for name, expected in prepared['pins'].items():
        ck(meta(ROOT / name, True) == expected and meta(MIRROR / name, True) == expected, ('all current workspace/mirror blob pins', name))
    ck(git(['rev-parse', 'HEAD', 'HEAD^{tree}', 'HEAD^', 'refs/remotes/origin/main']).decode().splitlines() == [HEAD, TREE, BASE, HEAD], 'fresh actual refs')
    ck(git(['status', '--porcelain=v1', '--untracked-files=all', '-z']) == b'', 'fresh clean mirror')
    ck(git(['rev-list', '--left-right', '--count', 'HEAD...origin/main']) == b'0\t0\n', 'fresh 0/0')
    ck(git(['ls-remote', '--exit-code', 'origin', 'refs/heads/main']) == (HEAD + '\trefs/heads/main\n').encode(), 'fresh actual remote ref')
    tree = git(['ls-tree', '-r', '-z', '--full-tree', HEAD, '--'] + prepared['query_paths'])
    seen = {}
    for row in tree.split(b'\0'):
        if not row: continue
        description, path = row.split(b'\t', 1); mode, kind, blob = description.decode().split(); name = path.decode()
        ck(name not in seen and kind == 'blob' and mode in ('100644', '100755'), 'fresh ordinary unique blob')
        seen[name] = blob
    ck(seen == {k: v['git_blob_sha1'] for k, v in prepared['pins'].items()}, 'fresh complete Git object identity map')
    diff = git(['diff', BASE, HEAD, '--no-renames', '--name-status', '-z']).decode().split('\0')[:-1]
    ck(dict(zip(diff[1::2], diff[0::2])) == committed['committed_changes'], 'fresh exact complete committed changes')
    failure = obj(EXECUTION / 'prepare/FAILURE.actual.json')
    ck(failure['native_commands'][-1]['exit_code'] == 128 and failure['native_commands'][-1]['argv'][3] == 'check-ignore', 'original literal flag failure retained')
    old = obj(EXECUTION / 'attempt_02/prepare/RESULT.actual.json')
    ck(old['status'] == wanted['prepare'] and not (EXECUTION / 'attempt_02/copy').exists(), 'superseded successful preflight only')
    result = {'status': 'PASS_ROOT_P209_COMPLETION_PRIVATE_CHECKPOINT_RECEPTION', 'checks': CHECKS, 'commit': HEAD, 'tree': TREE, 'parent': BASE,
              'selected_paths': 1482, 'additions': 1476, 'modifications': 6, 'deletions': 0, 'complete_blob_keys': 12555, 'native_original_records_checked': native_count,
              'entire_original_blob_stream': staged['original_stdout'], 'one_full_decompression_with_both_archives_raw_equal': True,
              'actual_fresh_git_commands': COMMANDS, 'actual_remote_matches': True, 'divergence': '0/0', 'mirror_clean': True,
              'execution_seal': SEAL, 'original_execution_payloads': 305, 'current_file_pins_checked': len(READS),
              'scope': 'Read-only source/original Git-object reception. No third cat-file stream, Git mutation, central edit, scientific run or admission claim.'}
    save('RESULT.json', result)
    files = sorted(p for p in OUT.rglob('*') if p.is_file())
    save('SHA256SUMS', ''.join(meta(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in files).encode())
    print(json.dumps({k: v for k, v in result.items() if k != 'actual_fresh_git_commands'} | {'reception_payloads': len(files), 'reception_seal': meta(OUT / 'SHA256SUMS')}, sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        main()
    except BaseException as exc:
        if OUT.is_dir() and not (OUT / 'FAILURE.json').exists():
            save('FAILURE.json', {'status': 'FAILED_ROOT_RECEPTION_PRESERVED', 'error': repr(exc), 'checks': CHECKS, 'actual_fresh_git_commands': COMMANDS})
        raise
