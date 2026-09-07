"""Static/copy/diff infrastructure only; never imports or invokes an auditor."""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
BASE = BATCH / 'qa/p209_terminal_artifact_revision_01'
OLD = BATCH / 'qa/p209_terminal_artifact_preparation'
FAILED = BATCH / 'qa/p209_terminal_artifact/initial_01'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
SEALS = (
    (OLD, 'SHA256SUMS', 347, '3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51'),
    (FAILED, 'SHA256SUMS', 8, 'deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04'),
    (BATCH / 'reviews/p209_b', 'SHA256SUMS', 1472, 'ab9f2cc94fb0b6eb112290bc9687a4d8479f5b832810f7a7c28013737e838d16'),
    (BATCH / 'scouting/LNR_SOURCE_RECHECK', 'MANIFEST.sha256', 202, '9137cb3fbccf56a077932d64c35509b3fe0ea918827f92a8de05849a3a709d07'),
)
COPY_PACKAGES = (OLD, FAILED, BATCH / 'qa/central_lifecycle_p209_round1',
                 BATCH / 'qa/central_lifecycle_p209_terminal_push')
EXTRA_NAMES = (
    'AGENTS.md', 'SYMBOLIC_DYNAMICS_STATE.md', '.agents/skills/symbolic-dynamics-research/SKILL.md',
    'docs/research_state/WORKFLOW.md', 'docs/papers204_208_sequence/PIPELINE_STATE.md',
    'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md', 'docs/papers204_208_sequence/PROBLEM_ANCHOR.md',
    'docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md',
    'docs/papers204_208_sequence/qa/P209_ARTIFACT_PREPARATION_ROOT_INSPECTION.actual.json',
    'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_01.failed.actual.json',
    'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md',
    'papers/209-ordered-fibre-threading/frozen_round1/ROUND1_PROVENANCE.json',
    'papers/209-ordered-fibre-threading/frozen_round2/ROUND2_PROVENANCE.json',
    'papers/209-ordered-fibre-threading/PAPER_STATUS.md',
    'papers/209-ordered-fibre-threading/ROOT_ADOPTION.md',
    'papers/209-ordered-fibre-threading/AUTHOR_MANIFEST.sha256',
    'papers/209-ordered-fibre-threading/PAPER_MANIFEST.sha256',
    'papers/209-ordered-fibre-threading/ROOT_LIFECYCLE.md',
    'docs/papers204_208_sequence/reviews/p209_b/SHA256SUMS',
    'docs/papers204_208_sequence/scouting/LNR_SOURCE_RECHECK/MANIFEST.sha256',
)


def info(path):
    path = Path(path)
    raw = path.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw), 'resolved': str(path.resolve()),
            'symlink': os.readlink(path) if path.is_symlink() else None}


def save(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(raw)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def j(path):
    return json.loads(Path(path).read_bytes())


def physical(base):
    names = set()
    for p in base.rglob('*'):
        assert not p.is_symlink(), p
        if p.is_file():
            names.add(p.relative_to(base).as_posix())
    return names


def seal_rows(base, name, count=None, wanted=None):
    if wanted is not None:
        assert info(base / name)['sha256'] == wanted, (base, name)
    result = {}
    for line in (base / name).read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match is not None, (base, line)
        digest, rel = match.groups()
        p = Path(rel)
        assert p.parts and not p.is_absolute() and '..' not in p.parts and rel not in result
        result[rel] = digest
    assert name not in result and set(result) == physical(base) - {name}
    assert count is None or len(result) == count
    for rel, digest in result.items():
        assert info(base / rel)['sha256'] == digest, (base, rel)
    return result


def command(argv, inputs, cwd=ROOT):
    before = {str(p): info(p) for p in inputs}
    began = datetime.now(timezone.utc).isoformat()
    child = subprocess.run(argv, cwd=cwd, env=ENV, capture_output=True, check=False)
    after = {str(p): info(p) for p in inputs}
    assert before == after
    return {'argv': argv, 'cwd': str(cwd), 'environment': ENV, 'started_utc': began,
            'ended_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': child.returncode,
            'stdout': child.stdout.decode(), 'stderr': child.stderr.decode(),
            'full_inputs_before': before, 'full_inputs_after': after, 'inputs_unchanged': True}


def intake():
    assert not (BASE / 'ORIGINAL_INPUTS.json').exists()
    package_checks = []
    immutable = {}
    for base, name, count, wanted in SEALS:
        rows = seal_rows(base, name, count, wanted)
        for rel in list(rows) + [name]:
            immutable[str(base / rel)] = info(base / rel)
        package_checks.append({'base': str(base), 'manifest': name, 'payloads': len(rows), 'sha256': wanted})
    for base in COPY_PACKAGES[2:]:
        seal_rows(base, 'SHA256SUMS', 5)
    selected = {ROOT / n for n in EXTRA_NAMES}
    selected.update(base / n for base in COPY_PACKAGES for n in physical(base))
    before = {str(p): info(p) for p in sorted(selected)}
    copies, commands = {}, []
    for p in sorted(selected):
        target = BASE / 'original_snapshot' / p.relative_to(ROOT)
        save(target, p.read_bytes())
        row = command(['/usr/bin/cmp', '--', str(p), str(target)], [p, target])
        assert row['exit_code'] == 0 and row['stdout'] == row['stderr'] == ''
        commands.append(row)
        copies[str(p)] = {'physical': str(target), **before[str(p)],
            'role': 'Exact at-revision-assignment original; no original input is repinned or rewritten.'}
    assert before == {str(p): info(p) for p in sorted(selected)}
    assert immutable == {name: info(name) for name in immutable}
    dump(BASE / 'ORIGINAL_INPUTS.json', copies)
    dump(BASE / 'IMMUTABLE_PACKAGE_INPUTS.json', immutable)
    dump(BASE / 'INTAKE_CMP_COMMANDS.json', commands)
    dump(BASE / 'INTAKE_RESULT.json', {'status': 'PASS_EXACT_DOCUMENTARY_INTAKE_NOT_AUDIT_EXECUTION',
        'copies': copies, 'copy_count': len(copies), 'actual_cmp_commands': len(commands),
        'preserved_package_checks': package_checks, 'immutable_paths_checked_twice': len(immutable),
        'auditor_lifecycle_guard_science_build_view_executions': 0})
    print(json.dumps({'status': 'PASS_EXACT_DOCUMENTARY_INTAKE_NOT_AUDIT_EXECUTION',
        'copy_count': len(copies), 'actual_cmp_commands': len(commands),
        'preserved_package_checks': package_checks, 'immutable_paths_checked_twice': len(immutable)},
        sort_keys=True, indent=2))


if __name__ == '__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    if sys.argv[1:] == ['intake']:
        intake()
    else:
        raise RuntimeError('Require intake')
