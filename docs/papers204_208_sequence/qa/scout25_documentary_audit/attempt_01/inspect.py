"""Read-only documentary audit. Never import or execute scout source code."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_fifth'
EXPECTED_SEAL = '50cdf62cb689c8fb0130336d62b16e8e815808b86235f7f43048c2f629b2913b'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
RG = '/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg'
CURL = '/root/miniconda3/bin/curl'
PDFTEXT = '/usr/bin/pdftotext'
SUM = '/usr/bin/sha256sum'
ROOTS = [str(p) for p in (ROOT / 'papers', ROOT / 'docs',
    Path('/root/autodl-tmp/hilbert-polya-structure/papers'),
    Path('/root/autodl-tmp/hilbert-polya-structure/docs'),
    Path('/root/autodl-tmp/hilbert-polya-structure/symbolic_dynamics/papers'),
    Path('/root/autodl-tmp/hilbert-polya-structure/symbolic_dynamics/docs'))]
# Exact old-control aliases, not permission to relax any other changed input.
ALIASES = {
    'SYMBOLIC_DYNAMICS_STATE.md': ('421cd6ca3023b4526179648d328319ac8be44c734f208aac7da0bffb5c1f9373',
        'evidence_capture/historical_inputs/01_SYMBOLIC_DYNAMICS_STATE.md'),
    'docs/papers204_208_sequence/PIPELINE_STATE.md': ('81619c39b239ec3d9012bde623a047db048aaa107c088ee7ce09f90344a8c491',
        'evidence_capture/historical_inputs/02_PIPELINE_STATE.md'),
}
CHECKS = 0
READS = {}
COMMANDS = []


def need(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


def raw(path):
    p = Path(path)
    need(p.is_file() and not p.is_symlink(), 'missing/nonphysical file: ' + str(p))
    data = p.read_bytes()
    pin = {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
    key = str(p)
    need(key not in READS or READS[key] == pin, 'changed during audit: ' + key)
    READS[key] = pin
    return data


def sha(path):
    raw(path)
    return READS[str(Path(path))]['sha256']


def obj(relative):
    return json.loads(raw(SCOUT / relative))


def constants(name, wanted):
    tree = ast.parse(raw(SCOUT / name), filename=name)
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in wanted:
                    need(target.id not in result, 'duplicate source constant')
                    result[target.id] = ast.literal_eval(node.value)
    need(set(result) == set(wanted), 'missing literal source constants: ' + name)
    return result


def manifest(path):
    result = {}
    for line in raw(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'bad manifest syntax')
        digest, relative = match.groups()
        p = Path(relative)
        need(not p.is_absolute() and '..' not in p.parts and relative == p.as_posix(), 'unsafe manifest path')
        need(relative not in result, 'duplicate manifest path')
        result[relative] = digest
    return result


def archive():
    need(sha(SCOUT / 'SHA256SUMS') == EXPECTED_SEAL, 'unexpected original seal')
    listing = manifest(SCOUT / 'SHA256SUMS')
    need(len(listing) == 115 and 'SHA256SUMS' not in listing, 'archive payload count/self inclusion')
    entries = list(SCOUT.rglob('*'))
    need(all(not p.is_symlink() for p in entries), 'archive symlink')
    actual = {p.relative_to(SCOUT).as_posix() for p in entries if p.is_file()}
    need(actual == set(listing) | {'SHA256SUMS'}, 'incomplete archive manifest')
    for relative, digest in listing.items():
        need(sha(SCOUT / relative) == digest, 'archive payload mismatch: ' + relative)
    return listing


def command(folder, tag, argv, cwd, expected_exit):
    key = folder + '/' + tag
    attempt = obj(key + '.ATTEMPT.json')
    result = obj(key + '.RESULT.json')
    need(set(attempt) == {'argv', 'cwd', 'environment', 'started_utc'}, 'attempt schema: ' + key)
    need(attempt['argv'] == argv and attempt['cwd'] == str(cwd) and attempt['environment'] == ENV, 'command arguments/environment: ' + key)
    need(re.fullmatch(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ', attempt['started_utc']) is not None, 'command time: ' + key)
    need(set(result) == {'exit', 'stdout_sha256', 'stderr_sha256'}, 'result schema: ' + key)
    need(type(result['exit']) is int and result['exit'] == expected_exit, 'literal recorded exit: ' + key)
    for stream in ('stdout', 'stderr'):
        need(sha(SCOUT / (key + '.' + stream)) == result[stream + '_sha256'], 'full command stream: ' + key)
    row = {'key': key, **attempt, **result,
        'stdout_bytes': len(raw(SCOUT / (key + '.stdout'))),
        'stderr_bytes': len(raw(SCOUT / (key + '.stderr')))}
    COMMANDS.append(row)
    return row


def tool_pins():
    groups = {
        'history_01': ('history_search.py', RG),
        'evidence_capture': ('finish.py', RG, SUM),
        'public_sources': ('fetch_sources.py', CURL, PDFTEXT),
        'public_sources_additional': ('fetch_sources_additional.py', CURL, PDFTEXT),
    }
    rows = {}
    for folder, names in groups.items():
        before = obj(folder + '/tools.before.json')
        after = obj(folder + '/tools.after.json')
        expected = {str(SCOUT / names[0]), *names[1:]}
        need(set(before) == expected and before == after, 'source/tool pin set: ' + folder)
        for p, digest in before.items():
            need(sha(p) == digest, 'current named source/tool mismatch: ' + p)
        rows[folder] = before
    return rows


def discovery():
    hs = constants('history_search.py', {'ENV', 'EXCLUDE', 'QUERIES'})
    fs = constants('finish.py', {'ENV', 'INPUTS', 'QUERIES'})
    need(hs['ENV'] == fs['ENV'] == ENV, 'source environment')
    selected = obj('history_01/selected.json')
    need(selected == sorted(set(selected)) and len(selected) == 3520, 'discovery unique/count/order')
    need(obj('evidence_capture/selected.json') == selected, 'initial/terminal selected set')
    recovered, pdfs = [], []
    inventory = raw(SCOUT / 'history_01/inventory.stdout').decode().splitlines()
    need(len(inventory) == len(set(inventory)), 'duplicate discovery inventory paths')
    for filename in inventory:
        p = Path(filename)
        need(any(p.is_relative_to(Path(root)) for root in ROOTS), 'inventory outside six roots')
        if any(token in filename.lower() for token in hs['EXCLUDE']) or 'review' in p.name.lower():
            continue
        if p.suffix == '.tex' or any(token in p.name.upper() for token in ('SCOUT', 'INTAKE', 'KILL', 'LEDGER', 'PROOF')):
            recovered.append(filename)
        if p.suffix == '.pdf' and str(p).startswith(str(ROOT / 'papers')):
            pdfs.append(filename)
    need(sorted(recovered) == selected, 'literal discovery selection from full inventory')
    need(sorted(pdfs) == obj('history_01/local_pdf_filenames.json'), 'PDF filename-only selection')
    maps = [obj(p) for p in ('history_01/inputs.before.json', 'history_01/inputs.after.json',
        'evidence_capture/search.before.json', 'evidence_capture/search.after.json')]
    need(all(set(m) == set(selected) and m == maps[0] for m in maps), 'all four full discovery maps')
    command('history_01', 'inventory', [RG, '--files', *ROOTS], ROOT, 0)
    for folder, queries in (('history_01', hs['QUERIES']), ('evidence_capture', fs['QUERIES'])):
        report = obj(folder + '/REPORT.json')
        need(report['status'] == 'PASS' and report['selected_files'] == 3520, 'historical report status/count')
        need(report['roots'] == ROOTS and report['exclusions'] == list(hs['EXCLUDE']) and report['excluded_remaining'] == [], 'historical discovery scope')
        rows = []
        for tag, query in queries:
            cmd = command(folder, tag, [RG, '-n', '-i', '-e', query, *selected], ROOT, 0)
            rows.append({'tag': tag, 'query': query, 'exit': cmd['exit'],
                'output_lines': len(raw(SCOUT / folder / (tag + '.stdout')).decode().splitlines())})
        need(report['queries'] == rows, 'historical query report/full output lines')
    need(obj('history_01/REPORT.json')['before_after_equal'] is True, 'initial report equality')
    return maps[0], fs['INPUTS'], len(inventory), len(pdfs)


def history(inputs, search):
    before = obj('evidence_capture/historical.before.json')
    need(before == obj('evidence_capture/historical.after.json') and set(before) == set(inputs) and len(inputs) == 15, 'historical 15 full before/after pins')
    copies = obj('evidence_capture/HISTORICAL_COPIES.json')
    expected = [{'original': relative, 'copied': f'evidence_capture/historical_inputs/{n:02d}_' + Path(relative).name,
        'sha256': before[relative]} for n, relative in enumerate(inputs, 1)]
    need(copies == expected, 'exact historical mapping')
    need(manifest(SCOUT / 'HISTORICAL_INPUTS.sha256') == before, 'historical originals manifest')
    need(manifest(SCOUT / 'HISTORICAL_COPIES.sha256') == {r['copied']: r['sha256'] for r in copies}, 'historical copies manifest')
    command('evidence_capture', 'live_check', [SUM, '-c', str(SCOUT / 'HISTORICAL_INPUTS.sha256')], ROOT, 0)
    command('evidence_capture', 'copies_check', [SUM, '-c', str(SCOUT / 'HISTORICAL_COPIES.sha256')], SCOUT, 0)
    need(raw(SCOUT / 'evidence_capture/live_check.stdout').decode() == ''.join(p + ': OK\n' for p in inputs), 'original historical sha command full output')
    need(raw(SCOUT / 'evidence_capture/copies_check.stdout').decode() == ''.join(r['copied'] + ': OK\n' for r in copies), 'copies sha command full output')
    report = obj('evidence_capture/REPORT.json')
    overlap = {p: search[str(ROOT / p)] == before[p] for p in inputs if str(ROOT / p) in search}
    need(len(overlap) == 7 and all(overlap.values()) and report['original_search_overlap_equal'] == overlap, 'historical/discovery overlap')
    need(report['historical_files'] == 15 and report['live_check_exit'] == report['copies_check_exit'] == 0, 'history report counts/exits')
    need(all(report[k] is True for k in ('historical_before_after_equal', 'selected_before_after_equal', 'tools_before_after_equal')), 'history report before/after assertions')
    return copies


def current_inputs(search, copies):
    for p, digest in search.items():
        need(Path(p).is_absolute() and sha(p) == digest, 'current discovery input mismatch: ' + p)
    rows = []
    for r in copies:
        need(sha(SCOUT / r['copied']) == r['sha256'], 'physical historical copy')
        current_sha = sha(ROOT / r['original'])
        mode = 'CURRENT_ORIGINAL_EXACT'
        if current_sha != r['sha256']:
            need(ALIASES.get(r['original']) == (r['sha256'], r['copied']), 'unapproved historical drift: ' + r['original'])
            mode = 'EXACT_HISTORICAL_CONTROL_ALIAS'
        rows.append({**r, 'current_sha256': current_sha, 'mode': mode})
    return rows


def sources():
    first = constants('fetch_sources.py', {'ENV', 'URLS'})
    extra = constants('fetch_sources_additional.py', {'ENV', 'URLS'})
    need(first['ENV'] == extra['ENV'] == ENV, 'source fetch environments')
    expected_exits = {'sonntag_teichert': 22, 'dmgt_landing': 60, 'schweitzer_dblp': 28, 'dmgt_direct': 60, 'schweitzer_slides': 0}
    outputs = []
    for folder, urls, timeout in (('public_sources', first['URLS'], '50'),
            ('public_sources_additional', [(tag, url, 'pdf') for tag, url in extra['URLS']], '45')):
        retrieval = obj(folder + '/RETRIEVAL.json')
        need(len(retrieval) == len(urls), 'retrieval row count')
        for (tag, url, suffix), row in zip(urls, retrieval):
            target = SCOUT / folder / (tag + '.' + suffix)
            header = SCOUT / folder / (tag + '.headers')
            argv = [CURL, '--location', '--fail-with-body', '--max-time', timeout,
                '--dump-header', str(header), '--output', str(target), '--write-out',
                '%{http_code}\n%{url_effective}\n%{size_download}\n', url]
            command(folder, tag + '.curl', argv, SCOUT, expected_exits[tag])
            raw(header)
            expected = {'tag': tag, 'url': url, 'curl_exit': expected_exits[tag], 'exists': target.exists()}
            if target.exists():
                data = raw(target)
                expected.update(bytes=len(data), sha256=sha(target))
                need(data.startswith(b'%PDF') == (tag == 'schweitzer_slides'), 'PDF magic/failure body distinction')
            if tag == 'schweitzer_slides':
                textpath = SCOUT / folder / (tag + '.txt')
                command(folder, tag + '.pdftotext', [PDFTEXT, '-layout', str(target), str(textpath)], SCOUT, 0)
                text = raw(textpath)
                need(text.count(b'\n') == 1865 and len(text.decode().splitlines()) == 1971, 'slides text newline/form-feed-aware line counts')
                need(len(raw(target)) == 942738 and sha(target) == '61a2cabae89d2ac966792030b55e3757c8d6057b6f9f414c9f16b6efab0b62dc', 'slides physical PDF pin')
                expected['pdftotext_exit'] = 0
                outputs.append({'path': str(textpath), **READS[str(textpath)], 'newline_count': 1865, 'splitlines_including_form_feeds': 1971})
            else:
                need(not (SCOUT / folder / (tag + '.txt')).exists(), 'failed acquisition cannot have success text')
            need(row == expected, 'literal source retrieval row: ' + tag)
            outputs.append({'path': str(target), **expected})
    return outputs


def main():
    started = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.dont_write_bytecode == 1 and sys.flags.optimize == 0, 'audit isolated interpreter flags')
    need(dict(os.environ) == ENV, 'audit exact minimal environment')
    need(sys.pycache_prefix is not None and not Path(sys.pycache_prefix).exists(), 'audit unused cache prefix')
    initial_archive = archive()
    initial_tools = tool_pins()
    search, inputs, inventory_count, pdf_filename_count = discovery()
    copies = history(inputs, search)
    initial_current = current_inputs(search, copies)
    outputs = sources()
    expected_attempts = {r['key'] + '.ATTEMPT.json' for r in COMMANDS}
    need(len(COMMANDS) == 15 and len(expected_attempts) == 15, 'all 15 documentary commands')
    need({p.relative_to(SCOUT).as_posix() for p in SCOUT.rglob('*.ATTEMPT.json')} == expected_attempts, 'complete attempt inventory')
    need({p.relative_to(SCOUT).as_posix() for p in SCOUT.rglob('*.RESULT.json')} == {s.replace('.ATTEMPT.json', '.RESULT.json') for s in expected_attempts}, 'complete result inventory')
    failures = [r for r in COMMANDS if r['exit'] != 0]
    need([r['exit'] for r in failures] == [22, 60, 28, 60], 'four original nonzero failures retained')
    need(archive() == initial_archive, 'second complete archive pass')
    need(tool_pins() == initial_tools, 'second current named source/tool pass')
    need(current_inputs(search, copies) == initial_current, 'second full current discovery/history pass')
    # Re-read every actual dependency, including all old receipts and external current files.
    for p, pin in list(READS.items()):
        need(sha(p) == pin['sha256'], 'final actual read-set drift: ' + p)
    report = {'status': 'PASS_DOCUMENTARY_AUDIT', 'started_utc': started,
        'completed_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'checks': CHECKS, 'original_archive': str(SCOUT), 'original_seal_sha256': EXPECTED_SEAL,
        'archive_payloads_each_pass': 115, 'archive_passes': 2,
        'discovery_inputs_each_pass': len(search), 'discovery_current_passes': 2,
        'initial_and_terminal_discovery_maps': 4, 'inventory_paths': inventory_count,
        'local_pdf_filenames_only': pdf_filename_count, 'history_originals_and_copies': initial_current,
        'history_current_passes': 2, 'named_tool_pins_each_pass': initial_tools,
        'source_artifacts': outputs, 'commands': COMMANDS, 'nonzero_command_exits': [r['exit'] for r in failures],
        'current_read_set': READS, 'current_read_files': len(READS), 'findings': [],
        'scope': 'Documentary archive and recorded command integrity only. No scout code import/execution, scientific producer, candidate review, download, source-body novelty adjudication, index edit, or Git operation.',
        'limits': ['Original documentary recorders pin their source and named tools, not a complete historical Python/TLS/loader/configuration dependency closure.',
            'The six-root rg inventory and selected 3,520 inputs are authenticated as recorded; no new current repository discovery was run.',
            'PDF/text bytes and the retained conversion command are authenticated; this audit did not perform a new conversion or visual/body reading.',
            'The four failed acquisitions remain failed; the 2012/2013 source-body access holds are not cleared.',
            'Two exact old central-control aliases are allowed only through their pre-existing pinned physical copies; all other discovery and historical inputs must match current originals.']}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
