#!/usr/bin/env python3
"""Read-only selection and hashing; never clones, copies, stages or pushes."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import os
import re
import subprocess
import time

HERE = Path(__file__).resolve().parent
SOURCE = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
DEST = Path('/root/symbolic-dynamics-private-sync-20260907')
BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
BATCH = 'docs/papers204_208_sequence'
QA = BATCH + '/qa/'
PACKAGES = [
    ('papers/210-weakly-increasing-run-aggregation', 'PAPER_MANIFEST.sha256'),
] + [(QA + p, 'SHA256SUMS') for p in (
    'p209_completion_private_checkpoint', 'p209_completion_root_reception',
    'mna_root_pair_preparation', 'mna_root_pair_execution', 'mna_root_source_read',
    'mna_root_original_preparation', 'mna_root_original_01',
    'root_replays/mna_gate_pair_01', 'central_admission_p210', 'central_round0_p210',
    'batch_terminal_strict_preparation',
    'root_replays/batch_terminal_strict_p205_author_01',
    'root_replays/batch_terminal_strict_p205_a_01',
    'root_replays/batch_terminal_strict_p205_b_01',
    'root_replays/batch_terminal_strict_p207_author_01',
    'root_replays/batch_terminal_strict_p207_a_01',
    'root_replays/batch_terminal_strict_p207_b_01',
    'batch_terminal_build_preparation', 'batch_terminal_builds_01',
    'batch_four_build_original_preparation', 'batch_four_build_original_revision_01',
    'p210_author_strict_preparation', 'root_replays/p210_author_strict_pair_01',
    'p210_round0_original_preparation',
)]
EXCLUDE_PREFIXES = [BATCH + '/reviews/p210', QA + 'p210_a_', QA + 'root_replays/p210_a_',
                    QA + 'p208_p209_', QA + 'five_paper_terminal_preparation/',
                    QA + 'p210_checkpoint_preparation/']
EXCLUDE_FILE_TOKENS = ('P210_A_', 'p210_a_', 'P208_P209_', 'p208_p209_', 'reuse')


def dump(path, obj):
    with path.open('x') as f:
        json.dump(obj, f, sort_keys=True, indent=2)
        f.write('\n')


def safe(name):
    p = PurePosixPath(name)
    assert name == str(p) and not p.is_absolute() and '..' not in p.parts
    assert not any(c in name for c in '\n\r\t\0') and not name.startswith(':')
    return p


def pin(path):
    assert path.is_file() and not path.is_symlink()
    size = path.stat().st_size
    h, g = hashlib.sha256(), hashlib.sha1(b'blob ' + str(size).encode() + b'\0')
    actual = 0
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
            g.update(b)
            actual += len(b)
    assert actual == size == path.stat().st_size
    return {'bytes': size, 'sha256': h.hexdigest(), 'git_blob_sha1': g.hexdigest(),
            'mode': '100755' if path.stat().st_mode & 0o111 else '100644'}


def main():
    out = HERE / 'preparation_01'
    out.mkdir()
    commands = []
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0',
               GIT_SSH_COMMAND='ssh -o BatchMode=yes -o ConnectTimeout=20 -o ConnectionAttempts=1')

    def run(argv, allowed=(0,), stdin=None):
        stem = out / ('command_%03d' % (len(commands) + 1))
        start = time.time()
        p = subprocess.run(argv, input=stdin, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=50)
        stem.with_suffix('.stdout.raw').write_bytes(p.stdout)
        stem.with_suffix('.stderr.raw').write_bytes(p.stderr)
        if stdin is not None:
            stem.with_suffix('.stdin.raw').write_bytes(stdin)
        rec = {'argv': argv, 'cwd': str(SOURCE), 'start_epoch': start, 'end_epoch': time.time(),
               'exit': p.returncode, 'stdout_bytes': len(p.stdout), 'stderr_bytes': len(p.stderr),
               'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
               'stderr_sha256': hashlib.sha256(p.stderr).hexdigest(),
               'environment_overrides_only': {k: env[k] for k in ('GIT_OPTIONAL_LOCKS', 'GIT_TERMINAL_PROMPT', 'GIT_SSH_COMMAND')}}
        dump(stem.with_suffix('.actual.json'), rec)
        commands.append(rec)
        assert p.returncode in allowed, (argv, p.returncode)
        return p

    def git(*args, **kwargs):
        return run(['git', '-C', str(MIRROR), *args], **kwargs)

    capacity = run(['df', '-B1', '--output=source,fstype,size,used,avail,pcent,target', '/root', str(SOURCE), str(MIRROR)])
    run(['du', '-sb', str(MIRROR / '.git'), str(SOURCE / (QA + 'p209_completion_private_checkpoint'))])
    head = git('rev-parse', 'HEAD').stdout.decode().strip()
    tree = git('rev-parse', 'HEAD^{tree}').stdout.decode().strip()
    branch = git('symbolic-ref', '--short', 'HEAD').stdout.decode().strip()
    tracking = git('rev-parse', 'refs/remotes/origin/main').stdout.decode().strip()
    status = git('status', '--porcelain=v1', '-z', '--untracked-files=all').stdout
    divergence = git('rev-list', '--left-right', '--count', 'HEAD...origin/main').stdout.decode().split()
    remote = git('ls-remote', '--exit-code', 'origin', 'refs/heads/main', allowed=(0,128))
    assert head == tracking == BASE and branch == 'main' and not status and divergence == ['0','0']
    if remote.returncode == 0:
        assert remote.stdout.decode().split() == [BASE, 'refs/heads/main']
    assert not DEST.exists() and not DEST.is_symlink()
    assert Path('/root').stat().st_dev != SOURCE.stat().st_dev
    rawtree = git('ls-tree', '-r', '-z', '--full-tree', BASE, '--', BATCH,
                  'papers/210-weakly-increasing-run-aggregation', 'SYMBOLIC_DYNAMICS_STATE.md').stdout
    baseline = {}
    for row in rawtree.split(b'\0'):
        if row:
            attrs, name = row.split(b'\t', 1)
            mode, kind, oid = attrs.decode().split()
            baseline[name.decode()] = {'mode': mode, 'type': kind, 'git_blob_sha1': oid}

    expected, packages = {}, []
    for base, manifest in PACKAGES:
        mp = SOURCE / base / manifest
        assert mp.is_file(), str(mp)
        package_paths = set()
        for line in mp.read_text().splitlines():
            m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
            assert m, (str(mp), line)
            rel = str(safe(m[2]))
            name = base + '/' + rel
            assert name not in package_paths
            package_paths.add(name)
            obj = pin(SOURCE / name)
            assert obj['sha256'] == m[1], name
            assert name not in expected or expected[name] == obj
            expected[name] = obj
        manifest_name = base + '/' + manifest
        expected[manifest_name] = pin(mp)
        physical = {p.relative_to(SOURCE).as_posix() for p in (SOURCE / base).rglob('*') if p.is_file()}
        assert physical == package_paths | {manifest_name}, ('complete package coverage', base, sorted(physical - package_paths - {manifest_name})[:10])
        packages.append({'base': base, 'manifest': manifest, 'manifest_sha256': expected[manifest_name]['sha256'],
                         'payload_count': len(package_paths), 'complete_physical_coverage': True})

    extras, excluded = [], []
    # Only these three flat directories are considered; exact resulting paths are frozen below.
    candidates = [SOURCE / 'SYMBOLIC_DYNAMICS_STATE.md']
    for directory in [SOURCE / BATCH, SOURCE / (BATCH + '/qa'), SOURCE / (BATCH + '/scouting')]:
        candidates.extend(p for p in directory.iterdir() if p.is_file())
    for p in sorted(candidates):
        name = p.relative_to(SOURCE).as_posix()
        obj = pin(p)
        old = baseline.get(name)
        if old and old['git_blob_sha1'] == obj['git_blob_sha1'] and old['mode'] == obj['mode']:
            continue
        if any(t in p.name for t in EXCLUDE_FILE_TOKENS):
            excluded.append({'path': name, 'reason': 'A/reuse work not yet accepted at this frozen checkpoint'})
            continue
        if '/scouting/' in name and not p.name.startswith('MNA_'):
            excluded.append({'path': name, 'reason': 'not part of this bounded completed milestone'})
            continue
        expected[name] = obj
        extras.append(name)

    selected = []
    for name, obj in sorted(expected.items()):
        assert not any(name.startswith(p) for p in EXCLUDE_PREFIXES), name
        old = baseline.get(name)
        if old:
            mirror_obj = pin(MIRROR / name)
            assert mirror_obj['git_blob_sha1'] == old['git_blob_sha1'] and mirror_obj['mode'] == old['mode'], name
        if old is None or old['git_blob_sha1'] != obj['git_blob_sha1'] or old['mode'] != obj['mode']:
            selected.append({'path': name, **obj, 'baseline': old, 'change': 'A' if old is None else 'M'})
    paths = b''.join(p['path'].encode() + b'\0' for p in selected)
    ignore = git('check-ignore', '--no-index', '-z', '--stdin', allowed=(0,1), stdin=paths)
    attrs = git('check-attr', '-z', '--stdin', 'filter', 'text', 'eol', 'working-tree-encoding', 'ident', stdin=paths)
    fields = attrs.stdout.split(b'\0')[:-1]
    assert len(fields) == 15 * len(selected)
    assert all(fields[i] in (b'unspecified', b'unset') for i in range(2, len(fields), 3)), 'conversion attribute'
    ignored = [p.decode() for p in ignore.stdout.split(b'\0') if p]
    selected_bytes = sum(p['bytes'] for p in selected)
    total_bytes = sum(p['bytes'] for p in expected.values())
    expected_rows = [{'path': k, **v} for k,v in sorted(expected.items())]
    dump(out / 'EXPECTED_BLOBS.json', expected_rows)
    dump(out / 'SELECTED_PATHS.json', selected)
    # Compact exact map for root review; executable consumes JSON, not dynamic discovery.
    with (out / 'SELECTED_PATHS.tsv').open('x') as f:
        f.write('change\tbytes\tsha256\tgit_blob_sha1\tgit_relative_equals_source_relative\n')
        for p in selected:
            f.write('\t'.join([p['change'], str(p['bytes']), p['sha256'], p['git_blob_sha1'], p['path']]) + '\n')
    changed_controls = [p for p in selected if p['path'] in ('SYMBOLIC_DYNAMICS_STATE.md', BATCH+'/PIPELINE_STATE.md', BATCH+'/FINAL_THEOREM_CONTRACTS.md', BATCH+'/GIT_SYNC_RECEIPT.md')]
    # This is an immutable byte identity, not a copied control snapshot or current A acceptance.
    scope = {'status': 'PREPARED_ONLY_ROOT_REVIEW_REQUIRED', 'baseline': BASE, 'baseline_tree': tree,
             'source': str(SOURCE), 'original_mirror': str(MIRROR), 'supplementary_clone': str(DEST),
             'overlay_execution_evidence': '/root/symbolic-dynamics-private-sync-evidence-20260907',
             'mapping': 'identical source-relative paths at supplementary repository root; original mirror untouched',
             'packages': packages, 'exact_extra_paths': extras, 'excluded_flat_candidates': excluded,
             'excluded_prefixes': EXCLUDE_PREFIXES, 'ignored_selected_paths': ignored,
             'selected_count': len(selected), 'selected_source_bytes': selected_bytes,
             'additions': sum(p['change']=='A' for p in selected), 'modifications': sum(p['change']=='M' for p in selected),
             'deletions': 0, 'expected_blob_count': len(expected), 'expected_blob_payload_bytes': total_bytes,
             'selected_json_sha256': pin(out/'SELECTED_PATHS.json')['sha256'],
             'expected_json_sha256': pin(out/'EXPECTED_BLOBS.json')['sha256'],
             'mutable_controls_pinned_but_not_physically_copied': changed_controls,
             'remote_retry_exit': remote.returncode, 'remote_confirmed_now': remote.returncode==0,
             'local_head_and_tracking': BASE, 'local_status_clean': True, 'local_divergence': [0,0],
             'source_free_bytes': os.statvfs(SOURCE).f_bavail * os.statvfs(SOURCE).f_frsize,
             'overlay_free_bytes': os.statvfs('/root').f_bavail * os.statvfs('/root').f_frsize,
             'conservative_overlay_storage_budget_bytes': selected_bytes * 3 + 1024**3,
             'shared_clone_dependency': str(MIRROR / '.git/objects'),
             'git_sync_log_filename_absent': True,
             'scientific_scope': 'Backup only; P210 Round0 complete, A not included; four earlier papers complete, no batch PASS; HOLD_EXTERNAL.'}
    dump(out / 'SCOPE.json', scope)
    print(json.dumps({k: scope[k] for k in ('status','selected_count','selected_source_bytes','expected_blob_count','expected_blob_payload_bytes','additions','modifications','ignored_selected_paths','remote_confirmed_now','overlay_free_bytes','conservative_overlay_storage_budget_bytes')}, sort_keys=True))


if __name__ == '__main__':
    main()
