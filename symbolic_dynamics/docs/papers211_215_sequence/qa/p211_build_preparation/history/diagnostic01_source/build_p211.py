#!/usr/bin/env python3
"""One initially bound source-only P211 build; never science, replay or review.

This new adapter intentionally has no P210 actual-schema, Round2/PDF equality,
terminal pair, cleanup, install, automatic source fix or retry branch.
"""
import argparse
import json
import os
from pathlib import Path
import re
import sys
import traceback

HERE = Path(__file__).resolve().parent
exec(compile((HERE / 'build_core.py').read_bytes(), str(HERE / 'build_core.py'), 'exec'))
CODE_NAMES = ('build_core.py', 'prepare_build.py', 'build_p211.py',
              'launch_build.py', 'static_checks.py')


def binding_inputs(binding_path, role='inner', outer_started=False):
    """No creation, process or source copy before exact root binding checks."""
    require(binding_path.is_absolute() and binding_path.resolve() == binding_path,
            'Physical absolute root binding')
    binding = json.loads(binding_path.read_bytes())
    require(binding.get('schema') == 'p211-initial-source-only-root-binding-v1' and
            binding.get('status') == 'ROOT_AUTHORIZED_INITIAL_SOURCE_ONLY_BUILD',
            'PENDING_ROOT_BINDING: root must read/approve code and exact dependency/source bytes')
    require(binding['environment'] == ENV8 and binding['scope'] == 'ONE_INITIAL_BUILD_ONLY',
            'Initial build ENV8 and scope cannot be broadened')
    require(binding['scientific_execution'] is False and binding['manuscript_review'] is False and
            binding['terminal_acceptance'] is False, 'Science, A/B and terminal gates remain separate')
    out = Path(binding['output'])
    require(out.is_absolute() and out.resolve() == out and
            out.parent == ROOT / 'docs/papers211_215_sequence/qa' and
            re.fullmatch(r'p211_initial_build_[0-9]+', out.name), 'Exact bounded future output role')
    if outer_started:
        require(out.is_dir() and not out.is_symlink() and
                {p.name for p in out.iterdir()} == {'outer'},
                'Inner requires only the newly entered outer, not a prior build')
        entered = json.loads((out / 'outer/ENTERED.json').read_bytes())
        require(entered['binding'] == pin(binding_path) and entered['inner_started'] is False,
                'Exact current outer-entry binding')
    else:
        require(not os.path.lexists(out), 'Output must not exist; no replace/resume/retry')
    lock_path = Path(binding['dependency_lock']['path'])
    require(lock_path.resolve() == lock_path and pin(lock_path) == binding['dependency_lock']['pin'],
            'Exact prospective dependency lock')
    lock = json.loads(lock_path.read_bytes())
    require(lock['schema'] == 'p211-bounded-dependency-candidate-v1' and
            lock['environment'] == ENV8, 'Reviewed bounded dependency selector schema')
    require(set(binding['adapter_pins']) == set(CODE_NAMES), 'All new adapter code bound')
    for name, expected in binding['adapter_pins'].items():
        require(pin(PREP / name) == expected and
                lock['code_observations'][name] == expected, 'Final adapter code changed: ' + name)
    current_sources = physical_sources()
    require(binding['source_pins'] == current_sources == lock['source_observations'],
            'Exactly nine current, observed and root-bound physical sources')
    require(source_graph()['class'] == 'amsart', 'Actual source graph')
    receipt = Path(binding['root_read_receipt']['path'])
    require(receipt.is_absolute() and receipt.resolve() == receipt and
            pin(receipt) == binding['root_read_receipt']['pin'], 'Pinned actual root-read receipt')
    before = snapshot(lock['selector_specs'])
    require(before == lock['entries'], 'Prelocked candidate/configuration key changed')
    require(dict(os.environ) == ENV8 and Path(sys.executable).resolve() == PYTHON and
            sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and
            not sys.flags.optimize and sys.pycache_prefix == str(out / ('unused_' + role + '_cache')) and
            not os.path.lexists(sys.pycache_prefix), 'Exact source-only isolated parent settings')
    require(Path.cwd() == ROOT and sys.path ==
            ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'],
            'Exact cwd and isolated Python search path')
    originals = {str(p): pin(p) for p in
                 [binding_path, lock_path, receipt, *(PREP / n for n in CODE_NAMES),
                  *(PAPER / n for n in SOURCES)]}
    return binding, lock, before, originals


def generated_snapshot(cold):
    result = {}
    for name in sorted(GENERATED):
        p = cold / name
        require(not p.is_symlink(), 'Generated symlink prohibited')
        result[name] = {'present': p.exists(), **(pin(p) if p.is_file() else {})}
    return result


def archive_pass(audit, cold, phase):
    destination = audit / phase
    destination.mkdir()
    values = generated_snapshot(cold)
    for ext in ('log', 'fls', 'aux', 'bbl', 'blg', 'out', 'toc'):
        name = 'main.' + ext
        if values[name]['present']:
            write_new(destination / name, (cold / name).read_bytes())
            require(pin(destination / name) == pin(cold / name), 'Immutable pass copy mismatch')
    write_new(destination / 'GENERATED.json', values)
    return values


def classify_fls(raw, cold, sources, before, after, known):
    """Preserve every ordered FLS record, including duplicates and spellings.

For same-pass outputs, FLS gives ordering, not a read-time byte snapshot.
That limitation is explicit, not silently replaced by a post-pass pin.
"""
    events, written = [], set()
    for number, line in enumerate(raw.decode().splitlines(), 1):
        if line.startswith('PWD '):
            require(Path(line[4:]) == cold, 'Unexpected FLS PWD')
            events.append({'line': number, 'kind': 'PWD', 'raw': line})
            continue
        require(line.startswith(('INPUT ', 'OUTPUT ')), 'Unknown FLS record: ' + line)
        kind, spelling = line.split(' ', 1)
        path = Path(os.path.abspath(cold / spelling)) if not Path(spelling).is_absolute() else Path(os.path.abspath(spelling))
        resolved = path.resolve()
        item = {'line': number, 'kind': kind, 'spelling': spelling,
                'absolute': str(path), 'resolved': str(resolved)}
        if path.is_relative_to(cold):
            require(path == resolved and not path.is_symlink(), 'Local FLS alias')
            name = path.relative_to(cold).as_posix()
            item['relative'] = name
            if kind == 'OUTPUT':
                require(name in GENERATED and name not in sources, 'Unsupported/source FLS output')
                written.add(name)
                item.update(role='GENERATED_OUTPUT', after=after[name])
            elif name in sources:
                require(pin(path) == sources[name], 'Changed physical copied TeX source')
                item.update(role='SOURCE', pin=sources[name])
            else:
                require(name in GENERATED, 'Unknown local FLS input')
                if name in written:
                    item.update(role='GENERATED_EARLIER_OUTPUT_SAME_PASS',
                                read_time_bytes='NOT_OBSERVED_BY_FLS',
                                pass_start=before[name], pass_end=after[name])
                else:
                    require(before[name]['present'], 'Input had neither pre-pass bytes nor earlier OUTPUT')
                    item.update(role='GENERATED_BEFORE', input_pin=before[name],
                                pass_end=after[name])
        else:
            require(kind == 'INPUT', 'Output outside source-only directory')
            require(str(path) in known and known[str(path)].get('kind') == 'file',
                    'External FLS spelling absent from prelock: ' + str(path))
            require(entry(path, known[str(path)].get('members') is not None) == known[str(path)],
                    'External FLS input changed: ' + str(path))
            item.update(role='EXTERNAL_PRELOCKED', pin=pin(path))
        events.append(item)
    return {'events': events, 'count': len(events),
            'roles': {role: sum(e.get('role') == role for e in events) for role in
                      ('SOURCE', 'EXTERNAL_PRELOCKED', 'GENERATED_BEFORE',
                       'GENERATED_EARLIER_OUTPUT_SAME_PASS', 'GENERATED_OUTPUT')},
            'limitation': 'FLS records ordered declared I/O, not exact mid-pass content or non-FLS OS reads.'}


def bibtex_roles(cold, lock, before, after):
    aux = (cold / 'main.aux').read_text()
    require(re.findall(r'\\bibstyle\{([^}]+)\}', aux) == ['amsplain'] and
            re.findall(r'\\bibdata\{([^}]+)\}', aux) == ['references'] and
            not re.search(r'\\@input\{', aux), 'BibTeX auxiliary graph exceeds bound inputs')
    styles = lock['queries']['explicit_graph_seeds']['resolutions']['amsplain.bst']
    require(len(styles) == 1, 'Unique root-bound amsplain style')
    blg = (cold / 'main.blg').read_text()
    require(re.findall(r'^The top-level auxiliary file:\s*(.+)$', blg, re.M) == ['main.aux'] and
            re.findall(r'^The style file:\s*(.+)$', blg, re.M) == ['amsplain.bst'] and
            re.findall(r'^Database file #[0-9]+:\s*(.+)$', blg, re.M) == ['references.bib'],
            'Actual BLG bibliography/style graph differs')
    return {'mode': 'BibTeX has no FLS; explicit aux/style/database plus native/config lock',
            'inputs': [{'path': 'main.aux', 'role': 'GENERATED_BEFORE', 'pin': before['main.aux']},
                       {'path': 'references.bib', 'role': 'SOURCE', 'pin': pin(cold / 'references.bib')},
                       {'path': styles[0], 'role': 'EXTERNAL_PRELOCKED', 'pin': pin(styles[0])}],
            'outputs': {n: after[n] for n in ('main.bbl', 'main.blg')},
            'blg_pin': pin(cold / 'main.blg'), 'non_FLS_trace': False}


def execute(binding_path, expected_binding_pin, preflight=False):
    require(pin(binding_path)['sha256'] == expected_binding_pin, 'Root-specified binding digest')
    binding, lock, before_config, originals = binding_inputs(binding_path, outer_started=not preflight)
    coverage = file_coverage(before_config)
    early = runtime_sample()
    check_runtime(early, coverage, originals)
    if preflight:
        print(json.dumps({'status': 'BOUND_PREFLIGHT_ONLY_NO_BUILD',
                          'originals': originals, 'sources': binding['source_pins'],
                          'configuration_count': len(before_config), 'runtime': early,
                          'output_created': False, 'native_children': 0,
                          'build_acceptance': False}, sort_keys=True))
        return 0
    out = Path(binding['output']) / 'inner'
    out.mkdir(mode=0o700)
    cold = out / 'source_only'
    cold.mkdir()
    write_new(out / 'ENTERED.json', {'binding': pin(binding_path), 'argv': sys.orig_argv,
                                   'environment': dict(os.environ), 'runtime': early})
    write_new(out / 'ORIGINALS_BEFORE.json', originals)
    write_new(out / 'CONFIGURATION_BEFORE.json', before_config)
    write_new(out / 'SOURCES_BEFORE.json', physical_sources())
    for name in SOURCES:
        destination = cold / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        write_new(destination, (PAPER / name).read_bytes())
    initial = {p.relative_to(cold).as_posix(): pin(p) for p in cold.rglob('*') if p.is_file()}
    require(initial == binding['source_pins'], 'Initially exactly nine copied sources and no generated inputs')
    write_new(out / 'SOURCE_ONLY_INITIAL.json', initial)
    calls, passes, failures, measurements = [], [], [], {}

    def command(label, argv, cwd=out, inputs=(), expected=(0,), timeout=120):
        # Every actual native executable and every explicit immutable input is
        # already in a before key or is a named source/generated dependency.
        require(str(Path(argv[0])) in lock['entries'], 'Native executable absent from prelock')
        row, raw = run_native(out, label, argv, cwd, inputs, timeout, expected)
        calls.append(row)
        return row, raw

    def linkage(label):
        row, raw = command(label, ['/usr/bin/ldd', *lock['ldd_elf_inputs']],
                           inputs=lock['ldd_elf_inputs'])
        require(row['successful'] and b'not found' not in raw, 'Native ldd failure')
        names = sorted(set(re.findall(r'(/[^\s():]+)', raw.decode())))
        result = {str(Path(name).resolve()): pin(Path(name).resolve()) for name in names}
        require(all(coverage.get(p) == value for p, value in result.items()), 'Unprelocked native link')
        return result

    try:
        libs_before = linkage('ldd_before')
        write_new(out / 'LINKAGE_BEFORE.json', libs_before)
        for tool in ('pdflatex', 'bibtex', 'kpsewhich'):
            row, raw = command('version_' + tool, ['/usr/bin/' + tool, '--version'])
            require(row['successful'], 'Version command failed')
        for tool in ('pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm'):
            row, raw = command('version_' + tool, ['/usr/bin/' + tool, '-v'])
            require(row['successful'], 'PDF tool version command failed')
        actual_queries = {}
        for key, value in lock['queries'].items():
            if key.startswith('var_'):
                argv = ['/usr/bin/kpsewhich', '-var-value=' + key[4:]]
            elif key == 'expanded_TEXMF':
                argv = ['/usr/bin/kpsewhich', '-expand-path=$TEXMF']
            else:
                continue
            row, raw = command('config_' + key, argv, cold, expected=(0, 1))
            require(row['successful'] and raw.decode().strip() == value, 'Effective TeX configuration changed')
            actual_queries[key] = raw.decode().strip()
        write_new(out / 'EFFECTIVE_CONFIGURATION.json', actual_queries)
        for label, argv in FOUR_COMMANDS:
            audit = out / ('pass_artifacts_' + label)
            audit.mkdir()
            generated_before = archive_pass(audit, cold, 'before')
            inputs = [cold / name for name in SOURCES]
            if label == 'bibtex':
                styles = lock['queries']['explicit_graph_seeds']['resolutions']['amsplain.bst']
                require(len(styles) == 1, 'Unique prelocked bibliography style')
                inputs += [cold / 'main.aux', Path(styles[0])]
            row, raw = command(label, argv, cold, inputs, timeout=600)
            generated_after = archive_pass(audit, cold, 'after')
            require(physical_sources(cold) == initial, 'Copied sources altered by native pass')
            require(row['successful'], 'Native build pass failed; preserve all outputs, no retry')
            if label == 'bibtex':
                roles = bibtex_roles(cold, lock, generated_before, generated_after)
            else:
                roles = classify_fls((cold / 'main.fls').read_bytes(), cold, initial,
                                     generated_before, generated_after, before_config)
            write_new(audit / 'INPUT_OUTPUT_ROLES.json', roles)
            actual = {p.relative_to(cold).as_posix() for p in cold.rglob('*') if p.is_file()}
            require(actual <= set(SOURCES) | GENERATED, 'Unclassified local output')
            passes.append({'label': label, 'native': row, 'generated_after': generated_after,
                           'roles': pin(audit / 'INPUT_OUTPUT_ROLES.json')})
        pdf = cold / 'main.pdf'
        require(pdf.is_file() and pin(pdf)['bytes'] > 0, 'No completed initial PDF')
        row, raw = command('pdfinfo', ['/usr/bin/pdfinfo', 'main.pdf'], cold, [pdf])
        require(row['successful'], 'pdfinfo failed')
        metadata = raw.decode()
        found_pages = re.search(r'^Pages:\s+(\d+)$', metadata, re.M)
        require(found_pages is not None and int(found_pages.group(1)) > 0, 'Actual positive page count')
        pages = int(found_pages.group(1))
        row, raw = command('pdffonts', ['/usr/bin/pdffonts', 'main.pdf'], cold, [pdf])
        require(row['successful'], 'pdffonts failed')
        fonts = [line.split()[-5:] for line in raw.decode().splitlines()[2:] if line.strip()]
        require(fonts and all(len(v) == 5 and v[0] == 'yes' for v in fonts),
                'Unembedded/unknown PDF font: bounded renderer dependency premise failed')
        text_path = out / 'main.txt'
        row, raw = command('pdftotext', ['/usr/bin/pdftotext', '-layout', 'main.pdf', str(text_path)], cold, [pdf])
        require(row['successful'], 'pdftotext failed')
        content = text_path.read_text()
        text_pages = content.split('\f')
        if text_pages and not text_pages[-1].strip():
            text_pages.pop()
        require(len(text_pages) == pages, 'Actual text/PDF page census disagreement')
        log = (cold / 'main.log').read_text(errors='replace')
        diagnostics = {key: re.findall(pattern, log, re.M) for key, pattern in {
            'undefined': r'^.*undefined.*$', 'overfull': r'^.*Overfull.*$',
            'underfull': r'^.*Underfull.*$', 'warnings': r'^.*Warning.*$',
            'missing_characters': r'^.*Missing character.*$',
            'rerun': r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$'}.items()}
        markers = [marker for marker in ('[VERIFY]', '??', '[?]') if marker in content]
        blg_findings = re.findall(r'(?im)^.*(?:Warning--|I couldn.t open|error message).*$',
                                  (cold / 'main.blg').read_text())
        page_dir = out / 'pages'
        page_dir.mkdir()
        renders = []
        for page in range(1, pages + 1):
            prefix = page_dir / ('page-%04d' % page)
            row, raw = command('render_%04d' % page,
                               ['/usr/bin/pdftoppm', '-f', str(page), '-l', str(page),
                                '-singlefile', '-png', '-r', '105', 'main.pdf', str(prefix)],
                               cold, [pdf], timeout=180)
            require(row['successful'], 'Actual page rendering failed')
            image = prefix.with_suffix('.png')
            require(image.is_file(), 'Actual rendered page missing')
            renders.append({'page': page, 'image': str(image), 'pin': pin(image),
                            'visual_review': 'NOT_VIEWED'})
        require({p.name for p in page_dir.iterdir()} == {'page-%04d.png' % p for p in range(1, pages + 1)},
                'Complete actual all-page render census')
        measurements = {'pdf': pin(pdf), 'pages': pages, 'embedded_fonts': len(fonts),
                        'diagnostics': diagnostics, 'text_markers': markers,
                        'bibtex_findings': blg_findings,
                        'reference_heading_pages': [i + 1 for i, t in enumerate(text_pages)
                            if re.search(r'^\s*(?:References|Bibliography)\s*$', t, re.M)],
                        'renders': renders, 'visual_review': 'NOT_VIEWED',
                        'venue_page_limit': None, 'size_threshold_100KB': 'NOT_AN_ACCEPTANCE_RULE'}
        write_new(out / 'MEASURED_NOT_VIEWED.json', measurements)
        libs_after = linkage('ldd_after')
        write_new(out / 'LINKAGE_AFTER.json', libs_after)
        require(libs_after == libs_before, 'Native linkage changed')
    except BaseException:
        failures.append(traceback.format_exc())
    # Before/after closures are attempted even after a failed pass, but an
    # unsettled native stream forbids final hashes and package seals.
    if list(out.rglob('UNCLOSED.json')):
        write_new(out / 'UNCLOSED.json', {'failures': failures, 'status': 'UNCLOSED_NO_SEAL'})
        return 1
    for name, collect, expected in (
        ('SOURCES_AFTER', physical_sources, binding['source_pins']),
        ('COPIED_SOURCES_AFTER', lambda: physical_sources(cold), initial),
        ('ORIGINALS_AFTER', lambda: {p: pin(p) for p in originals}, originals),
        ('CONFIGURATION_AFTER', lambda: snapshot(lock['selector_specs']), before_config)):
        try:
            value = collect()
            write_new(out / (name + '.json'), value)
            require(value == expected, 'Before/after closure failed: ' + name)
        except BaseException:
            failures.append(traceback.format_exc())
    try:
        late = runtime_sample()
        write_new(out / 'PARENT_RUNTIME_AFTER.json', late)
        check_runtime(late, coverage, originals)
    except BaseException:
        failures.append(traceback.format_exc())
    require([p['label'] for p in passes] == [p[0] for p in FOUR_COMMANDS] or failures,
            'Four-command native order')
    result = {'status': 'FAIL_PRESERVED' if failures else 'INITIAL_BUILD_RECORDED_NOT_VIEWED_NOT_ACCEPTED',
              'failures': failures, 'passes': passes, 'native_commands': calls,
              'measurements': measurements, 'scientific_executions': 0,
              'manuscript_reviews': 0, 'visual_review': 'NOT_VIEWED',
              'root_diagnostic_review': 'PENDING', 'build_acceptance': False,
              'terminal_acceptance': False, 'paper_completion': False,
              'external': 'OWNER_AMBER / HOLD_EXTERNAL'}
    write_new(out / 'RESULT.json', result)
    result['seal'] = seal(out)
    print(json.dumps(result, sort_keys=True))
    return 1 if failures else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--binding', type=Path, required=True)
    parser.add_argument('--binding-sha256', required=True)
    parser.add_argument('--preflight-only', action='store_true')
    arguments = parser.parse_args()
    raise SystemExit(execute(arguments.binding, arguments.binding_sha256, arguments.preflight_only))
