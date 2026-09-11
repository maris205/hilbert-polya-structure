#!/usr/bin/env python3
"""No-overwrite physical P208 freeze of its sealed author tree plus root reports.

This scoped adapter preserves older layouts unchanged. It copies every
explicit author-manifest referent, including actual execution/build records,
so the copied author seal is not left with missing paper-relative inputs.
An actual accepted review delta is a separate gate, not inferred by copying.
"""
import argparse
from hashlib import sha256
from pathlib import Path
import shutil


ROOT_ADDITIONS = ('main.pdf', 'AUTHOR_REPLAY.md', 'ROUND0_BUILD_REPORT.md',
                  'INTEGRITY_REVIEW.md')
REQUIRED_AUTHOR = ('main.tex', 'math_commands.tex', 'references.bib',
                   'PROOF_PACKAGE.md', 'verify.py', 'CANONICAL.json',
                   'record_author.py', 'build_author.py', 'AUTHOR_EXECUTION.md',
                   'BUILD_REPORT.md', 'AUTHOR_HANDOFF.md', 'PAPER_PLAN.md',
                   'NARRATIVE_REPORT.md', 'CLAIMS_EVIDENCE.md', 'SOURCE_AUDIT.md',
                   'VERIFICATION_SCOPE.md', 'README.md', 'sections/00_abstract.tex')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paper', type=Path)
    parser.add_argument('round', type=int, choices=(0, 1, 2))
    args = parser.parse_args()
    paper = args.paper.resolve(strict=True)
    if paper.name != '208-original-snapshot-triangulation-sweeps':
        raise SystemExit('adapter is scoped to P208')
    target = paper / ('frozen_round%d' % args.round)
    if target.exists():
        raise SystemExit('refusing existing freeze')
    if args.round and not (paper / ('frozen_round%d' % (args.round - 1)) / 'SHA256SUMS').is_file():
        raise SystemExit('prior physical freeze absent')
    manifest = paper / 'AUTHOR_MANIFEST.sha256'
    originals = {}
    for line in manifest.read_text().splitlines():
        expected, name = line.split('  ', 1)
        rel = Path(name)
        if rel.is_absolute() or '..' in rel.parts or not rel.parts:
            raise SystemExit('unsafe author path')
        key = rel.as_posix()
        if key in originals or key == manifest.name or any(p.startswith('frozen_round') for p in rel.parts):
            raise SystemExit('duplicate, circular or frozen author input')
        path = paper / rel
        if not path.is_file() or path.is_symlink() or digest(path) != expected:
            raise SystemExit('missing, nonregular or changed author input: ' + key)
        originals[key] = expected
    if any(name not in originals for name in REQUIRED_AUTHOR):
        raise SystemExit('required author input absent from explicit seal')
    if {p.relative_to(paper).as_posix() for p in (paper / 'sections').glob('*.tex')} != {
            name for name in originals if Path(name).parent == Path('sections') and name.endswith('.tex')}:
        raise SystemExit('incomplete modular TeX set')
    for name in (manifest.name,) + ROOT_ADDITIONS:
        path = paper / name
        if not path.is_file() or path.is_symlink():
            raise SystemExit('missing/nonregular root or manifest input: ' + name)
        value = digest(path)
        if name in originals and originals[name] != value:
            raise SystemExit('root/author input conflict')
        originals[name] = value
    target.mkdir()
    for name in sorted(originals):
        destination = target / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(paper / name, destination)
    copied = {p.relative_to(target).as_posix(): digest(p)
              for p in target.rglob('*') if p.is_file()}
    if copied != originals or any(digest(paper / name) != value for name, value in originals.items()):
        raise SystemExit('physical copy mismatch or live input changed; preserve failed copy')
    with (target / 'SHA256SUMS').open('x', encoding='utf-8') as stream:
        stream.write(''.join(f'{value}  {name}\n' for name, value in sorted(copied.items())))
    print(f'FROZEN {target} files={len(copied)}; review acceptance remains a separate evidence gate')


if __name__ == '__main__':
    main()
