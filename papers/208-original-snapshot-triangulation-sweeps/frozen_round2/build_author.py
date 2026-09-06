#!/usr/bin/env python3
"""Source-only P208 author preparation build; never a Round0/final freeze.

Usage: python -I -B build_author.py LABEL
No cleanup, no shell escape, no overwrite of an existing evidence directory.
All passes, failures, exact source maps, runtime inventory and logs survive.
PDF rendering is recorded, but only an actual later view is a visual review.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
       'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788652800',
       'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
TOOLS = ['/usr/bin/pdflatex', '/usr/bin/bibtex', '/usr/bin/kpsewhich',
         '/usr/bin/pdfinfo', '/usr/bin/pdffonts', '/usr/bin/pdftotext',
         '/usr/bin/pdftoppm', '/usr/bin/ldd', '/usr/bin/cmp']
TEX_ROOTS = ['/usr/share/texlive/texmf-dist/tex',
             '/usr/share/texlive/texmf-dist/fonts',
             '/usr/share/texlive/texmf-dist/web2c',
             '/usr/share/texlive/texmf-dist/bibtex',
             '/usr/share/texmf', '/var/lib/texmf', '/etc/texmf',
             '/usr/local/share/texmf', '/root/texmf',
             '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var']


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump(p, obj):
    with p.open('x', encoding='utf-8') as f:
        json.dump(obj, f, sort_keys=True, indent=2)
        f.write('\n')


def source_files():
    names = ['main.tex', 'math_commands.tex', 'references.bib']
    names += [str(p.relative_to(BASE)) for p in sorted((BASE / 'sections').glob('*.tex'))]
    return {n: digest(BASE / n) for n in names}


def tex_inventory():
    result = {}
    for root in TEX_ROOTS:
        path = Path(root)
        if not path.exists():
            continue
        for p in path.rglob('*'):
            if p.is_file():
                resolved = p.resolve()
                if str(resolved) not in result:
                    result[str(resolved)] = digest(resolved)
    return result


def command(root, label, argv, cwd):
    start = time.time_ns()
    with (root / (label + '.stdout')).open('xb') as out:
        with (root / (label + '.stderr')).open('xb') as err:
            child = subprocess.run(argv, cwd=cwd, env=ENV, stdout=out, stderr=err,
                                   check=False)
    row = {'label': label, 'argv': argv, 'cwd': str(cwd), 'environment': ENV,
           'start_ns': start, 'end_ns': time.time_ns(), 'exit_code': child.returncode,
           'stdout': label + '.stdout', 'stderr': label + '.stderr',
           'stdout_sha256': digest(root / (label + '.stdout')),
           'stderr_sha256': digest(root / (label + '.stderr'))}
    dump(root / (label + '.command.json'), row)
    return row


def main():
    assert sys.flags.optimize == 0 and sys.flags.isolated == 1 and sys.dont_write_bytecode
    if len(sys.argv) != 2 or not re.fullmatch('[a-z0-9_-]+', sys.argv[1]):
        raise SystemExit('usage: build_author.py LABEL')
    parent = BASE / 'qa_build'
    parent.mkdir(exist_ok=True)
    root = parent / sys.argv[1]
    root.mkdir()
    cold = root / 'source_only'
    cold.mkdir()
    before = source_files()
    dump(root / 'SOURCE_PINS_BEFORE.json', before)
    for rel, sha in before.items():
        dest = cold / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(BASE / rel, dest)
        assert digest(dest) == sha
    initial = {str(p.relative_to(cold)): digest(p) for p in sorted(cold.rglob('*')) if p.is_file()}
    assert initial == before
    dump(root / 'SOURCE_ONLY_INITIAL.json', initial)
    tools_before = {str(Path(p).resolve()): digest(Path(p).resolve())
                    for p in TOOLS + [sys.executable, __file__]}
    dump(root / 'TOOLS_BEFORE.json', tools_before)
    runtime_before = tex_inventory()
    dump(root / 'TEX_RUNTIME_INVENTORY_BEFORE.json', runtime_before)
    commands, consumed = [], {}
    failure = None
    page_count = None
    warnings = {}

    def run(label, argv):
        row = command(root, label, argv, cold)
        commands.append(row)
        if row['exit_code'] != 0:
            raise RuntimeError(label + ' failed; all evidence retained')
        return row

    def capture_tex_pass(label, successful):
        if successful:
            assert (cold / 'main.fls').is_file(), 'successful TeX pass lacks recorder file'
            assert (cold / 'main.log').is_file(), 'successful TeX pass lacks log file'
        for suffix in ['fls', 'log']:
            p = cold / ('main.' + suffix)
            if p.exists():
                shutil.copyfile(p, root / (label + '.' + suffix))
        fls = cold / 'main.fls'
        if not successful:
            # A failed pass may not have reached recorder initialization.
            # Its optional raw files survive without replacing its primary error.
            return
        for line in fls.read_text(errors='replace').splitlines():
            if not line.startswith('INPUT '):
                continue
            p = Path(line[6:])
            if not p.is_absolute():
                p = cold / p
            p = p.resolve()
            if p.is_file() and not p.is_relative_to(cold):
                assert str(p) in runtime_before, ('unrecorded runtime input', str(p))
                assert digest(p) == runtime_before[str(p)], ('runtime changed', str(p))
                consumed[str(p)] = digest(p)

    try:
        run('engine_version', ['/usr/bin/pdflatex', '--version'])
        run('bibtex_version', ['/usr/bin/bibtex', '--version'])
        run('texmf_roots', ['/usr/bin/kpsewhich', '-var-value=TEXMF'])
        # Actual dynamic resolver output is retained; addresses are not byte-stable.
        for i, exe in enumerate(['/usr/bin/pdftex', '/usr/bin/bibtex', sys.executable]):
            row = run('ldd_%02d' % i, ['/usr/bin/ldd', str(Path(exe).resolve())])
            raw = (root / row['stdout']).read_text()
            if 'not found' in raw:
                raise RuntimeError('unresolved shared library')
            pins = {}
            for token in re.findall(r'/[^\s()]+', raw):
                p = Path(token).resolve()
                if p.is_file():
                    pins[str(p)] = digest(p)
            if not pins:
                raise RuntimeError('empty dynamic dependency pins')
            dump(root / ('LIBRARIES_%02d_BEFORE.json' % i), pins)
        for i in range(1, 4):
            label = 'pdflatex_%02d' % i
            try:
                run(label, ['/usr/bin/pdflatex', '-no-shell-escape', '-recorder',
                            '-interaction=nonstopmode', '-halt-on-error', 'main.tex'])
            except BaseException:
                try:
                    capture_tex_pass(label, successful=False)
                except BaseException as capture_error:
                    dump(root / (label + '.capture_failure.json'),
                         {'type': type(capture_error).__name__, 'message': str(capture_error)})
                raise
            else:
                capture_tex_pass(label, successful=True)
            if i == 1:
                # These bibliography resources are used by BibTeX, not necessarily .fls.
                row = run('bst_location', ['/usr/bin/kpsewhich', 'plainnat.bst'])
                bst = Path((root / row['stdout']).read_text().strip()).resolve()
                assert str(bst) in runtime_before and digest(bst) == runtime_before[str(bst)]
                consumed[str(bst)] = digest(bst)
                run('bibtex', ['/usr/bin/bibtex', 'main'])
        row = run('pdfinfo', ['/usr/bin/pdfinfo', 'main.pdf'])
        page_count = int(re.search(r'^Pages:\s+(\d+)', (root / row['stdout']).read_text(), re.M).group(1))
        run('pdffonts', ['/usr/bin/pdffonts', 'main.pdf'])
        run('pdftotext', ['/usr/bin/pdftotext', '-layout', 'main.pdf', str(root / 'main.txt')])
        log = (cold / 'main.log').read_text(errors='replace')
        warnings = {'undefined': re.findall(r'^.*(?:undefined|There were undefined).*$' , log, re.M),
                    'overfull': re.findall(r'^Overfull.*$', log, re.M),
                    'underfull': re.findall(r'^Underfull.*$', log, re.M),
                    'all_warning_lines': re.findall(r'^.*Warning.*$', log, re.M)}
        assert not warnings['undefined']
        assert page_count <= 9, ('page budget exceeded', page_count)
        fonts = (root / 'pdffonts.stdout').read_text().splitlines()[2:]
        # The last five fields are emb/sub/uni/object-number/generation.
        # A yes in subset or Unicode alone must never imply embedding.
        font_fields = [line.split()[-5:] for line in fonts if line.strip()]
        assert font_fields and all(len(f) == 5 and f[0] == 'yes' for f in font_fields)
        dump(root / 'FONT_EMBEDDING_CHECK.json',
             {'tail_columns': ['emb', 'sub', 'uni', 'object', 'generation'],
              'actual_tail_fields': font_fields, 'all_emb_yes': True})
        pages = root / 'pages'
        pages.mkdir()
        run('render_pages', ['/usr/bin/pdftoppm', '-png', '-r', '120', 'main.pdf', str(pages / 'page')])
        assert len(list(pages.glob('page-*.png'))) == page_count
    except BaseException as error:
        failure = {'type': type(error).__name__, 'message': str(error)}
        raise
    finally:
        after = source_files()
        dump(root / 'SOURCE_PINS_AFTER.json', after)
        tools_after = {p: digest(Path(p)) for p in tools_before}
        dump(root / 'TOOLS_AFTER.json', tools_after)
        consumed_after = {p: digest(Path(p)) for p in consumed}
        dump(root / 'CONSUMED_TEX_INPUTS.json', consumed)
        dump(root / 'CONSUMED_TEX_INPUTS_AFTER.json', consumed_after)
        lib_after = {}
        for pinfile in sorted(root.glob('LIBRARIES_*_BEFORE.json')):
            orig = json.loads(pinfile.read_text())
            current = {p: digest(Path(p)) for p in orig}
            dump(root / pinfile.name.replace('_BEFORE', '_AFTER'), current)
            lib_after[pinfile.name] = orig == current
        copied_after = {rel: digest(cold / rel) for rel in before}
        record = {'role': 'author_preparation_not_round0_or_terminal_freeze',
                  'validation_exception': failure, 'commands': commands,
                  'source_before': before, 'source_after': after,
                  'source_unchanged': before == after,
                  'copied_source_unchanged': before == copied_after,
                  'tools_unchanged': tools_before == tools_after,
                  'consumed_runtime_unchanged': consumed == consumed_after,
                  'shared_libraries_unchanged': lib_after,
                  'runtime_inventory_files': len(runtime_before),
                  'consumed_runtime_files': len(consumed), 'pages': page_count,
                  'warnings': warnings,
                  'pdf_sha256': digest(cold / 'main.pdf') if (cold / 'main.pdf').exists() else None,
                  'all_child_exits_zero': all(c['exit_code'] == 0 for c in commands),
                  'actual_page_viewing': False,
                  'runtime_limit': 'Pre-build TeX resource inventory covers all consumed .fls '
                                   'inputs and bibliography style; actual tools/libraries pinned. '
                                   'No historical OS or hermetic environment claim.'}
        record['status'] = 'AUTHOR_BUILD_PREPARED_NOT_VIEWED' if (
            failure is None and record['all_child_exits_zero'] and before == after and
            before == copied_after and tools_before == tools_after and
            consumed == consumed_after and all(lib_after.values())
        ) else 'AUTHOR_BUILD_FAILED'
        dump(root / 'RECEIPT.json', record)
    assert record['status'] == 'AUTHOR_BUILD_PREPARED_NOT_VIEWED'
    print(json.dumps({'receipt': str(root / 'RECEIPT.json'),
                      'pages': page_count, 'status': record['status'],
                      'pdf_sha256': record['pdf_sha256'], 'warnings': warnings}, indent=2))


if __name__ == '__main__':
    main()
