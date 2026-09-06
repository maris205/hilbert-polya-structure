#!/usr/bin/env python3
"""Record the actual raw comparison of the two final author preparations.

No build is run by this helper. No viewing is inferred from hashes.
The author's actual seven-page view is separately attested in BUILD_REPORT.md.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump(p, obj):
    with p.open('x', encoding='utf-8') as f:
        json.dump(obj, f, sort_keys=True, indent=2)
        f.write('\n')


def main():
    assert sys.flags.optimize == 0 and sys.flags.isolated == 1 and sys.dont_write_bytecode
    root = BASE / 'qa_build' / 'stable_pair'
    root.mkdir()
    builds = [BASE / 'qa_build' / ('preparation_%02d' % n) for n in (2, 3)]
    before = {}
    for build in builds:
        receipt = json.loads((build / 'RECEIPT.json').read_bytes())
        assert receipt['status'] == 'AUTHOR_BUILD_PREPARED_NOT_VIEWED'
        assert receipt['pages'] == 7
        for p in sorted(build.rglob('*')):
            if p.is_file():
                before[str(p)] = sha(p)
        for p, expected in json.loads((build / 'CONSUMED_TEX_INPUTS.json').read_bytes()).items():
            assert sha(Path(p)) == expected
        for rel, expected in receipt['source_before'].items():
            assert sha(BASE / rel) == expected
    tools = {str(Path(p).resolve()): sha(Path(p).resolve())
             for p in ['/usr/bin/cmp', sys.executable, __file__]}
    dump(root / 'INPUTS_BEFORE.json', before)
    dump(root / 'TOOLS_BEFORE.json', tools)
    argv = ['/usr/bin/cmp'] + [str(b / 'source_only' / 'main.pdf') for b in builds]
    env = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
    with (root / 'cmp.stdout').open('xb') as out, (root / 'cmp.stderr').open('xb') as err:
        child = subprocess.run(argv, cwd=root, env=env, stdout=out, stderr=err, check=False)
    after = {p: sha(Path(p)) for p in before}
    tools_after = {p: sha(Path(p)) for p in tools}
    dump(root / 'INPUTS_AFTER.json', after)
    dump(root / 'TOOLS_AFTER.json', tools_after)
    record = {'role': 'author_raw_pdf_comparison_not_new_build_or_view',
              'argv': argv, 'cwd': str(root), 'environment': env,
              'exit_code': child.returncode, 'stdout': 'cmp.stdout', 'stderr': 'cmp.stderr',
              'stdout_sha256': sha(root / 'cmp.stdout'), 'stderr_sha256': sha(root / 'cmp.stderr'),
              'inputs_unchanged': before == after, 'tools_unchanged': tools == tools_after,
              'pdf_sha256': [sha(b / 'source_only' / 'main.pdf') for b in builds],
              'status': 'RAW_PDF_PAIR_PASS' if child.returncode == 0 and before == after
                        and tools == tools_after else 'RAW_PDF_PAIR_FAILED'}
    dump(root / 'RECEIPT.json', record)
    assert record['status'] == 'RAW_PDF_PAIR_PASS'
    # A new deliverable copy, never overwriting an existing manuscript product.
    with (BASE / 'main.pdf').open('xb') as f:
        f.write((builds[0] / 'source_only' / 'main.pdf').read_bytes())
    assert sha(BASE / 'main.pdf') == record['pdf_sha256'][0]
    print(json.dumps(record, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
