#!/usr/bin/env python3
"""One-time P210 Round0; disclosed exact-origin adaptation of the P209 freezer.
No old producer/parser/manifest is changed. Preconditions precede all copying.
"""
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
TARGET = PAPER / 'frozen_round0'
EXPECTED = 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
# Only these three physically copied source-context documents retain the
# author paper's Markdown origin. All other capsule Markdown has no links.
CAPSULE_ORIGINS = {
    'author_produce_01/source/SOURCE_AUDIT.md': 'SOURCE_AUDIT.md',
    'author_pair_01/source/SOURCE_AUDIT.md': 'SOURCE_AUDIT.md',
    'author_pair_02/source/SOURCE_AUDIT.md': 'SOURCE_AUDIT.md',
}
# These are archived internal snapshots, not arbitrary path-prefix rewrites.
WORKSPACE_ORIGINS = {
    'sources/archive/CRG_SCOUT.md': 'docs/papers162_166_sequence/scouting/replacement_crossclass/SCOUT.md',
    'sources/archive/FPT_LEDGER.md': 'docs/papers182_186_sequence/scouting/combinatorial_lane/SCOUT_AND_KILL_LEDGER.md',
    'sources/archive/PDCF_CANDIDATES.md': 'docs/papers187_191_sequence/scouting/combinatorial_lane/CANDIDATES.md',
}


def digest(path):
    assert path.is_file() and not path.is_symlink(), ('physical regular file', str(path))
    return sha256(path.read_bytes()).hexdigest()


def safe(name):
    p = Path(name)
    assert name and p.as_posix() == name and not p.is_absolute()
    assert '..' not in p.parts and '.' not in p.parts
    return p


def read_manifest(path, base):
    rows = {}
    data = path.read_bytes()
    assert data.endswith(b'\n')
    for line in data.decode().splitlines():
        value, name = line.split('  ', 1)
        assert re.fullmatch('[0-9a-f]{64}', value) and name not in rows and name != path.name
        rel = safe(name)
        assert not any(x.startswith('frozen_round') for x in rel.parts)
        assert digest(base / rel) == value, name
        rows[name] = value
    return rows


def raw_cmp(a, b):
    argv = ['/usr/bin/cmp', '--', str(a), str(b)]
    p = subprocess.run(argv, cwd=ROOT, capture_output=True, check=False, env=ENV, timeout=60)
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
           'exit_code': p.returncode, 'stdout': p.stdout.decode(), 'stderr': p.stderr.decode()}
    assert p.returncode == 0 and p.stdout == p.stderr == b'', row
    return row


def prerequisites():
    required = {
        'P210_ORIGINALS_ROOT_SECOND_COMPLETION.actual.json': 'PASS_DOCUMENTARY_ORIGINALS_ONLY',
        'P210_AUTHOR_STRICT_ROOT_COMPLETION.actual.json': 'PASS_ROOT_P210_AUTHOR_STRICT_PAIR_ORIGINAL_RECEPTION',
    }
    pins = {}
    for name, expected_status in required.items():
        p = QA / name
        result = json.loads(p.read_bytes())
        assert result['exit_code'] == 0 and json.loads(result['output'])['status'] == expected_status
        pins[str(p)] = digest(p)
    viewpath = QA / 'P210_ROOT_ROUND0_VIEW.actual.json'
    view = json.loads(viewpath.read_bytes())
    assert view['status'] == 'PASS_ROOT_ACTUAL_SIX_PAGE_ROUND0_VIEW_NOT_TERMINAL'
    assert view['viewer'] == '/root' and view['page_count'] == 6
    assert [r['number'] for r in view['pages']] == list(range(1, 7))
    assert digest(ROOT / view['pdf']) == view['pdf_sha256'] == digest(PAPER / 'main.pdf')
    for row in view['pages']:
        assert row['viewed'] is True and row['observation']
        assert digest(ROOT / row['path']) == row['sha256']
    pins[str(viewpath)] = digest(viewpath)
    return pins


def main():
    assert sys.flags.isolated == sys.flags.no_site == 1 and sys.dont_write_bytecode and sys.flags.optimize == 0
    assert len(sys.argv) == 1 and Path.cwd() == ROOT
    assert not TARGET.exists() and not TARGET.is_symlink(), 'existing freeze'
    historical, alias = PAPER / 'SHA256SUMS', PAPER / 'AUTHOR_MANIFEST.sha256'
    assert not alias.exists() and not alias.is_symlink(), 'existing alias'
    prerequisite_pins = prerequisites()
    assert digest(historical) == EXPECTED
    author = read_manifest(historical, PAPER)
    assert len(author) == 489
    assert {p.relative_to(PAPER).as_posix() for p in PAPER.rglob('*') if p.is_file()} == set(author) | {'SHA256SUMS', 'ROOT_ADOPTION.md'}
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
    archival = json.loads((PAPER / 'sources/ARCHIVE_INPUTS.actual.json').read_bytes())
    assert archival['count'] == len(archival['records']) == 19
    origins = {}
    origin_pins = {}
    for row in archival['records']:
        copy, original = PAPER / row['copy'], Path(row['original'])
        assert copy.read_bytes() == original.read_bytes()
        assert digest(copy) == digest(original) == row['sha256']
        origins[row['copy']] = original
        origin_pins[str(original)] = row['sha256']
    for name, relative in CAPSULE_ORIGINS.items():
        assert (PAPER / name).read_bytes() == (PAPER / relative).read_bytes()
        origins[name] = PAPER / relative
    for name, relative in WORKSPACE_ORIGINS.items():
        assert name in origins and str(origins[name]).endswith('/inputs/originals/' + relative)
        # The old snapshot is authoritative for its text; only relative-link
        # origin is restored here. No current document replacement is claimed.
        origins[name] = ROOT / relative

    links, external = [], dict(origin_pins)
    for name in sorted(sources):
        if not name.endswith('.md'):
            continue
        source = PAPER / name
        origin = origins.get(name, source)
        for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', source.read_text()):
            href = href.strip().strip('<>')
            if href.startswith(('https://', 'http://', 'mailto:', '#')):
                continue
            pathpart = unquote(href.split('#', 1)[0])
            if not pathpart:
                continue
            candidate = (origin.parent / pathpart).resolve()
            mode = 'external-exact-original-origin'
            if candidate == historical:
                physical, expected = TARGET / 'AUTHOR_MANIFEST.sha256', EXPECTED
                mode = 'exact-author-seal-alias'
            elif candidate.is_relative_to(PAPER) and candidate.relative_to(PAPER).as_posix() in sources:
                rel = candidate.relative_to(PAPER).as_posix()
                physical, expected = TARGET / rel, sources[rel]
                mode = 'physical-copied-input'
            else:
                expected, physical = digest(candidate), candidate
                external[str(candidate)] = expected
            links.append({'document': name, 'document_sha256': sources[name],
                          'exact_markdown_origin': str(origin), 'href': href,
                          'mode': mode, 'physical_target': str(physical), 'sha256': expected})

    # Every original/link/prerequisite is resolved before first new file.
    with alias.open('xb') as stream:
        stream.write(historical.read_bytes())
    comparisons = [raw_cmp(historical, alias)]
    TARGET.mkdir()
    for name in sorted(sources):
        dest = TARGET / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(PAPER / name, dest)
    shutil.copyfile(selfpath, TARGET / 'FREEZE_ADAPTER.py')
    metadata = {'scope': 'P210 physical Round0; A/B still pending',
                'historical_author_manifest_sha256': EXPECTED,
                'historical_author_manifest_name': str(historical),
                'physical_author_manifest_alias': 'AUTHOR_MANIFEST.sha256',
                'author_payloads': len(author), 'copied_input_count': len(sources),
                'freezer_origin': str(selfpath), 'freezer_sha256': selfhash,
                'launch_argv': sys.argv, 'links': links,
                'exact_document_origin_roles': {k: str(v) for k, v in origins.items()},
                'external_input_pins': external, 'prerequisite_pins': prerequisite_pins}
    with (TARGET / 'FROZEN_LINK_MAP.json').open('x') as stream:
        json.dump(metadata, stream, indent=2, sort_keys=True); stream.write('\n')
    expected_frozen = dict(sources)
    expected_frozen['FREEZE_ADAPTER.py'] = selfhash
    expected_frozen['FROZEN_LINK_MAP.json'] = digest(TARGET / 'FROZEN_LINK_MAP.json')
    assert {p.relative_to(TARGET).as_posix(): digest(p) for p in TARGET.rglob('*') if p.is_file()} == expected_frozen
    assert read_manifest(TARGET / 'AUTHOR_MANIFEST.sha256', TARGET) == author
    assert read_manifest(historical, PAPER) == author
    assert digest(historical) == digest(alias) == EXPECTED
    assert all(digest(PAPER / name) == value for name, value in sources.items())
    assert digest(selfpath) == selfhash and prerequisites() == prerequisite_pins
    assert all(digest(Path(path)) == value for path, value in external.items())
    assert all(digest(Path(row['physical_target'])) == row['sha256'] for row in links)
    comparisons.append(raw_cmp(alias, TARGET / 'AUTHOR_MANIFEST.sha256'))
    comparisons.append(raw_cmp(PAPER / 'main.pdf', TARGET / 'main.pdf'))
    with (TARGET / 'SHA256SUMS').open('x') as stream:
        stream.write(''.join(value + '  ' + name + '\n' for name, value in sorted(expected_frozen.items())))
    assert read_manifest(TARGET / 'SHA256SUMS', TARGET) == expected_frozen
    print(json.dumps({'status': 'PASS_PHYSICAL_P210_ROUND0', 'payloads': len(expected_frozen),
                      'manifest_sha256': digest(TARGET / 'SHA256SUMS'),
                      'historical_author_payloads': len(author), 'author_alias_sha256': EXPECTED,
                      'links': len(links), 'external_paths': len(external),
                      'raw_comparisons': comparisons, 'freezer_sha256': selfhash,
                      'boundary': 'No new scientific producer/build/view; actual accepted A/B required next'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
