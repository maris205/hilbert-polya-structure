#!/usr/bin/env python3
"""One-time no-overwrite P209 Round0, with explicit historical-seal alias."""
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
TARGET = PAPER / 'frozen_round0'
EXPECTED = '9fd20cd746f1ae03c22a87283313248ad79ffcfb9a0f1ea45458937dd5901a0e'


def digest(path):
    if not path.is_file() or path.is_symlink():
        raise AssertionError('not a regular nonsymlink file: ' + str(path))
    return sha256(path.read_bytes()).hexdigest()


def safe(name):
    p = Path(name)
    assert name and p.as_posix() == name and not p.is_absolute()
    assert '..' not in p.parts and '.' not in p.parts
    return p


def read_manifest(path, base):
    rows = {}
    for line in path.read_text().splitlines():
        value, name = line.split('  ', 1)
        assert re.fullmatch('[0-9a-f]{64}', value) and name not in rows
        rel = safe(name)
        assert not any(x.startswith('frozen_round') for x in rel.parts)
        assert digest(base / rel) == value, name
        rows[name] = value
    return rows


def raw_cmp(a, b):
    argv = ['/usr/bin/cmp', '--', str(a), str(b)]
    p = subprocess.run(argv, capture_output=True, check=False,
                       env={'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8',
                            'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'})
    row = {'argv': argv, 'exit': p.returncode,
           'stdout': p.stdout.decode(), 'stderr': p.stderr.decode()}
    assert p.returncode == 0, row
    return row


def main():
    assert not TARGET.exists() and not TARGET.is_symlink(), 'existing freeze'
    historical = PAPER / 'SHA256SUMS'
    alias = PAPER / 'AUTHOR_MANIFEST.sha256'
    assert digest(historical) == digest(alias) == EXPECTED
    comparisons = [raw_cmp(historical, alias)]
    author = read_manifest(alias, PAPER)
    assert len(author) == 1985 and 'SHA256SUMS' not in author
    assert {p.relative_to(PAPER).as_posix() for p in PAPER.rglob('*')
            if p.is_file()} == set(author) | {
                'SHA256SUMS', 'AUTHOR_MANIFEST.sha256', 'ROOT_ADOPTION.md'}
    assert not any(p.is_symlink() for p in PAPER.rglob('*'))
    for name in ('main.tex', 'main.pdf', 'math_commands.tex', 'references.bib',
                 'PROOF_PACKAGE.md', 'verify.py', 'CANONICAL.json', 'README.md',
                 'SOURCE_AUDIT.md', 'PAPER_PLAN.md', 'CLAIMS_EVIDENCE.md'):
        assert name in author
    sources = dict(author)
    sources['AUTHOR_MANIFEST.sha256'] = EXPECTED
    sources['ROOT_ADOPTION.md'] = digest(PAPER / 'ROOT_ADOPTION.md')
    selfpath = Path(__file__).resolve(strict=True)
    selfhash = digest(selfpath)

    # Resolve all links before copying. Copied historical controls keep their
    # own workspace origins when their neighbouring targets were not captured.
    links, external = [], {}
    for name in sorted(sources):
        if not name.endswith('.md'):
            continue
        source = PAPER / name
        for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', source.read_text()):
            href = href.strip().strip('<>')
            if href.startswith(('https://', 'http://', 'mailto:', '#')):
                continue
            pathpart = unquote(href.split('#', 1)[0])
            if not pathpart:
                continue
            candidate = (source.parent / pathpart).resolve()
            mode = 'external-original-origin'
            if candidate == historical:
                physical = TARGET / 'AUTHOR_MANIFEST.sha256'
                expected = EXPECTED
                mode = 'exact-author-seal-alias'
            elif candidate.is_relative_to(PAPER) and candidate.relative_to(PAPER).as_posix() in sources:
                rel = candidate.relative_to(PAPER).as_posix()
                physical = TARGET / rel
                expected = sources[rel]
                mode = 'physical-copied-input'
            else:
                if not candidate.is_file() and name.startswith('source_context/workspace/'):
                    origin = ROOT / name.removeprefix('source_context/workspace/')
                    candidate = (origin.parent / pathpart).resolve()
                expected = digest(candidate)
                physical = candidate
                external[str(candidate)] = expected
            links.append({'document': name, 'href': href, 'mode': mode,
                          'physical_target': str(physical), 'sha256': expected})

    TARGET.mkdir()
    for name in sorted(sources):
        dest = TARGET / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(PAPER / name, dest)
    shutil.copyfile(selfpath, TARGET / 'FREEZE_ADAPTER.py')
    metadata = {'scope': 'P209 physical Round0; no manuscript acceptance',
                'historical_author_manifest_sha256': EXPECTED,
                'historical_author_manifest_name': str(historical),
                'physical_author_manifest_alias': 'AUTHOR_MANIFEST.sha256',
                'author_payloads': len(author), 'copied_input_count': len(sources),
                'freezer_origin': str(selfpath), 'freezer_sha256': selfhash,
                'launch_argv': sys.argv, 'links': links,
                'external_input_pins': external}
    with (TARGET / 'FROZEN_LINK_MAP.json').open('x') as stream:
        json.dump(metadata, stream, indent=2, sort_keys=True)
        stream.write('\n')
    expected_frozen = dict(sources)
    expected_frozen['FREEZE_ADAPTER.py'] = selfhash
    expected_frozen['FROZEN_LINK_MAP.json'] = digest(TARGET / 'FROZEN_LINK_MAP.json')
    assert {p.relative_to(TARGET).as_posix(): digest(p)
            for p in TARGET.rglob('*') if p.is_file()} == expected_frozen
    assert read_manifest(TARGET / 'AUTHOR_MANIFEST.sha256', TARGET) == author
    assert read_manifest(alias, PAPER) == author
    assert digest(historical) == digest(alias) == EXPECTED
    assert all(digest(PAPER / name) == value for name, value in sources.items())
    assert digest(selfpath) == selfhash
    assert all(digest(Path(path)) == value for path, value in external.items())
    assert all(digest(Path(row['physical_target'])) == row['sha256'] for row in links)
    comparisons.append(raw_cmp(alias, TARGET / 'AUTHOR_MANIFEST.sha256'))
    with (TARGET / 'SHA256SUMS').open('x') as stream:
        stream.write(''.join(value + '  ' + name + '\n'
                             for name, value in sorted(expected_frozen.items())))
    assert read_manifest(TARGET / 'SHA256SUMS', TARGET) == expected_frozen
    print(json.dumps({'status': 'PASS_PHYSICAL_P209_ROUND0',
                      'payloads': len(expected_frozen),
                      'manifest_sha256': digest(TARGET / 'SHA256SUMS'),
                      'historical_author_payloads': len(author),
                      'author_alias_sha256': EXPECTED, 'links': len(links),
                      'external_paths': len(external), 'raw_comparisons': comparisons,
                      'boundary': 'No new scientific producer/build/view; A/B pending'},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
