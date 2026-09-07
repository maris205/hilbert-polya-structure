"""Preserve unexecuted first revision02 draft and exact added link-origin data."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def info(path):
    raw = path.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def main():
    assert not (HERE / 'unexecuted_draft_before_link_registration').exists()
    names = ['audit_p209.py', 'audit_p209.py.diff', 'audit_p209.py.diff.stderr', 'ADAPTATION.diff',
             'SOURCE_EDITS.json', 'SOURCE_FUNCTION_CHECKS.json', 'DIFF_COMMANDS.json']
    draft = HERE / 'unexecuted_draft_before_link_registration'; draft.mkdir()
    selected = [PAPER / ('source_context/' + n) for n in ('MAPPING.json', 'RECEIPT.json')]
    selected += [PAPER / 'collect_context.py',
                 BATCH / 'reviews/p209_a/delta_check_01/RESPONSE_ORIGINALS_AND_COPIES.json',
                 BATCH / 'reviews/p209_b/delta_check_01/EXACT_HISTORY_ALIASES.json',
                 BATCH / 'reviews/p209_b/delta_check_01/check_delta.py',
                 BATCH / 'reviews/p209_b/delta_check_01/response_anchors/PAPER_STATUS.md',
                 BATCH / 'reviews/p209_b/delta_check_01/response_anchors/ROOT_ADOPTION.md']
    all_sources = [HERE / n for n in names] + selected
    before = {str(p): info(p) for p in all_sources}
    commands, copies = [], []
    for source in all_sources:
        target = draft / source.name if source.parent == HERE else HERE / 'original_snapshot' / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream: stream.write(source.read_bytes())
        argv = ['/usr/bin/cmp', '--', str(source), str(target)]
        run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert run.returncode == 0 and run.stdout == run.stderr == b''
        commands.append({'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
                         'stdout': run.stdout.decode(), 'stderr': run.stderr.decode()})
        copies.append({'original': str(source), 'copy': str(target), **info(target)})
    after = {str(p): info(p) for p in all_sources}
    assert before == after
    with (draft / 'SHA256SUMS').open('x') as stream:
        for name in sorted(names): stream.write(info(draft / name)['sha256'] + '  ' + name + '\n')
    report = {'scope': 'Unexecuted preparation draft preserved before separately disclosed static link-origin repair. Not a new actual auditor failure.',
              'copies': copies, 'actual_cmp_commands': commands, 'inputs_before': before, 'inputs_after': after,
              'all_inputs_unchanged': True, 'unexecuted_draft_seal': info(draft / 'SHA256SUMS'),
              'target_executions': 0}
    with (HERE / 'LINK_ADDITION_INTAKE.json').open('x') as stream: json.dump(report, stream, indent=2, sort_keys=True); stream.write('\n')
    print(json.dumps({'copies': len(copies), 'unexecuted_draft_payloads': len(names), 'draft_seal': info(draft / 'SHA256SUMS'), 'target_executions': 0}, sort_keys=True))


if __name__ == '__main__': main()
