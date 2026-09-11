#!/usr/bin/python3.10
"""Independent read-only documentary audit; never import submitted code."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import traceback
from urllib.parse import unquote, urlsplit

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
EXEC = QA / 'p211_round0_execution01'
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
FREEZE = PAPER / 'frozen_round0'
HERE = QA / 'p211_round0_root_reception'
NAMES = '''AUTHOR_EXECUTION_RECEIPT.md
CANONICAL.json
CANONICAL_SCHEMA.md
CLAIMS_EVIDENCE.md
HANDOFF.md
INITIAL_BUILD_RECEIPT.md
NARRATIVE_REPORT.md
PAPER_PLAN.md
PARAMETER_SPECIFICATION.md
PREPARATION_PLAN.md
PROOF_PACKAGE.md
README.md
SOURCE_AUDIT.md
SOURCE_INPUT_PINS.json
SOURCE_PIN_COLLECTION_TOOL_RETURN.json
SOURCE_PREPARATION_MANIFEST.json
STATIC_CHECK_TOOL_RETURN.json
main.pdf
main.tex
math_commands.tex
parameters.json
references.bib
sections/0_abstract.tex
sections/1_introduction.tex
sections/2_image.tex
sections/3_clock.tex
sections/4_inverse.tex
sections/5_scope.tex
sources/bibliographic_metadata_web.json
sources/stein_definition_web.json
sources/stein_support_web.json
verify.py'''.splitlines()
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
reads, blobs, inventories, resolutions = {}, {}, {}, []
checks = 0


def need(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def digest(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def rel(path):
    return str(Path(path).relative_to(ROOT))


def physical(path):
    p = Path(path)
    need(p.is_absolute() and p.is_relative_to(ROOT), ('workspace target', str(p)))
    info = p.lstat()
    need(stat.S_ISREG(info.st_mode) and not p.is_symlink() and p.resolve() == p,
         ('ordinary physical path', str(p)))
    return p


def read(path):
    p = physical(path)
    raw = p.read_bytes()
    value = digest(raw)
    need(str(p) not in reads or reads[str(p)] == value, ('input drift', str(p)))
    reads[str(p)] = value
    blobs[str(p)] = raw
    return raw


def obj(path):
    return json.loads(read(path))


def check_pin(path, expected):
    actual = digest(read(path))
    need(actual == expected, ('exact byte-size/hash pin', str(path)))
    return actual


def inventory(base):
    base = Path(base)
    need(base.is_dir() and not base.is_symlink() and base.resolve() == base,
         ('ordinary directory', str(base)))
    names = set()
    for p in base.rglob('*'):
        need(not p.is_symlink(), ('no symlink in selected tree', str(p)))
        if p.is_file():
            physical(p)
            names.add(str(p.relative_to(base)))
        else:
            need(p.is_dir(), ('ordinary tree node', str(p)))
    previous = inventories.setdefault(str(base), sorted(names))
    need(previous == sorted(names), ('inventory drift', str(base)))
    return names


def seal(base, expected_count=None):
    raw = read(base / 'SHA256SUMS')
    rows = {}
    for line in raw.decode('utf-8').splitlines():
        need(len(line) > 66 and line[64:66] == '  ', ('manifest syntax', str(base)))
        h, name = line[:64], line[66:]
        parts = Path(name).parts
        need(re.fullmatch('[0-9a-f]{64}', h) is not None and name not in rows
             and name != 'SHA256SUMS' and not Path(name).is_absolute()
             and '..' not in parts and str(Path(name)) == name,
             ('nonself unique safe manifest path', name))
        rows[name] = h
        need(digest(read(base / name))['sha256'] == h, ('manifest payload hash', name))
    need(set(rows) == inventory(base) - {'SHA256SUMS'}, ('complete manifest', str(base)))
    if expected_count is not None:
        need(len(rows) == expected_count, ('manifest count', str(base)))
    return rows


def inline_targets(text):
    """Scan explicit inline-link delimiters, independently of producer regex."""
    i = 0
    while i < len(text):
        if text[i] != '[' or (i > 0 and text[i - 1] in '!\\'):
            i += 1
            continue
        j = text.find(']', i + 1)
        if j < 0 or '\n' in text[i:j] or text[j + 1:j + 2] != '(':
            i += 1
            continue
        k = j + 2
        depth = 1
        while k < len(text) and depth and text[k] != '\n':
            if text[k] == '\\':
                k += 2
                continue
            if text[k] == '(':
                depth += 1
            elif text[k] == ')':
                depth -= 1
            k += 1
        need(depth == 0, ('balanced explicit Markdown target', i))
        yield text[j + 2:k - 1].strip().removeprefix('<').removesuffix('>')
        i = k


def audit():
    need(Path(__file__).resolve() == HERE / 'audit_round0.py', 'own audit location')
    need(Path.cwd() == ROOT, 'explicit workspace cwd')
    read(Path(__file__).resolve())
    result = obj(EXEC / 'RESULT.json')
    native = obj(EXEC / 'NATIVE01.json')
    need(native['result']['exit_code'] == 0 and native['polls'] == [], 'actual root completion')
    need(json.loads(native['result']['output']) == result, 'actual root stdout binds result')
    need(native['request']['cmd'] == '/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/p211_round0_execution01/freeze.py'
         and native['request']['workdir'] == str(ROOT), 'literal root launch')
    freeze_code = read(EXEC / 'freeze.py')
    need(freeze_code == read(EXEC / 'EXECUTED_FREEZE_SOURCE.py'), 'physical executed code equality')
    tree = ast.parse(freeze_code)
    selected = next(n.value for n in tree.body if isinstance(n, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == 'NAMES' for t in n.targets))
    need(isinstance(selected, ast.Call) and isinstance(selected.func, ast.Attribute)
         and selected.func.attr == 'split' and not selected.args,
         'literal scope AST without executing submitted module')
    need(ast.literal_eval(selected.func.value).split() == NAMES, 'literal root selection matches independent 32')
    read(EXEC / 'ROOT_AUTHORIZATION.md')
    expected = obj(QA / 'p211_initial_build_adoption01/PAPER_INPUTS_AFTER.json')
    before = obj(EXEC / 'SOURCE_INPUTS_BEFORE.json')
    after = obj(EXEC / 'SOURCE_INPUTS_AFTER.json')
    need(set(expected) == set(NAMES) and len(NAMES) == 32 and expected == before == after,
         'accepted 32 source pins before/after')
    need(inventory(FREEZE) == set(NAMES) | {'SHA256SUMS'}, 'exact 33-file freeze')
    live_names = inventory(PAPER)
    need(live_names == set(NAMES) | {'frozen_round0/' + n for n in NAMES + ['SHA256SUMS']},
         'no unselected live paper file or recursive freeze')
    origins = obj(EXEC / 'FROZEN_ORIGIN_MAP.json')
    need(len(origins) == 32, 'all origin rows')
    for name, row in zip(NAMES, origins):
        source, target = PAPER / name, FREEZE / name
        source_raw, frozen_raw = read(source), read(target)
        need(source_raw == frozen_raw and digest(source_raw) == before[name], ('full live/frozen bytes', name))
        ss, fs = source.stat(), target.stat()
        need((ss.st_dev, ss.st_ino) != (fs.st_dev, fs.st_ino) and fs.st_nlink == 1,
             ('physical non-hardlinked copy', name))
        need(row == {'original_path': rel(source), 'frozen_path': rel(target), 'relative_name': name,
                     'pin': before[name], 'source_inode': [ss.st_dev, ss.st_ino],
                     'frozen_inode': [fs.st_dev, fs.st_ino]}, ('exact origin/inode row', name))
    sums = seal(FREEZE, 32)
    need(set(sums) == set(NAMES), '32 manifest names')
    need((FREEZE / 'SHA256SUMS').stat().st_nlink == 1, 'physical manifest')
    need(digest(read(FREEZE / 'SHA256SUMS')) == result['manifest'] == {
        'bytes': 2799, 'sha256': '459459486a82c8f787d04e5e7fcb81e6c01b3abef320d1e82ea4cbb30ea8a8bd'},
        'accepted frozen manifest identity')
    need(sum(v['bytes'] for v in before.values()) == result['payload_bytes'] == 1819014,
         'complete payload byte census')
    check_pin(PAPER / 'main.pdf', {'bytes': 301007, 'sha256': '532b8c462e907878c3d75829b2c4ff86de7d59c137efa91b61ebc80717a077dc'})
    need(read(PAPER / 'main.pdf') == read(QA / 'p211_initial_build_01/inner/source_only/main.pdf'),
         'adopted PDF full bytes equal build original; not a view')
    check_pin(PAPER / 'CANONICAL.json', {'bytes': 1327062, 'sha256': '2a9d1311a491805644efa7cd4884ae50ed9f9ffa48e347b822a7ff68e12ee6b4'})

    # Independently reconstruct the exact 38 allowed operations and full streams.
    controls = [ROOT / 'SYMBOLIC_DYNAMICS_STATE.md', ROOT / 'docs/papers211_215_sequence/PIPELINE_STATE.md']
    command_specs = []
    for index, src in enumerate(controls, 1):
        dst = EXEC / 'control_originals' / src.name
        command_specs += [('control_copy_' + str(index), ['/usr/bin/cp', '-p', '--', str(src), str(dst)], ROOT, b''),
                          ('control_compare_' + str(index), ['/usr/bin/cmp', '--', str(src), str(dst)], ROOT, b'')]
    command_specs.append(('copy_all_32', ['/usr/bin/cp', '-p', '--parents', '--'] + NAMES + [str(FREEZE)], PAPER, b''))
    for index, name in enumerate(NAMES, 1):
        command_specs.append(('compare_%02d' % index, ['/usr/bin/cmp', '--', str(PAPER / name), str(FREEZE / name)], ROOT, b''))
    command_specs.append(('verify_frozen_manifest', ['/usr/bin/sha256sum', '-c', 'SHA256SUMS'], FREEZE,
                          ''.join(n + ': OK\n' for n in NAMES).encode()))
    need(len(command_specs) == result['native_commands'] == 38, '38 native commands')
    last_end = 0
    expected_command_files = set()
    for label, argv, cwd, expected_stdout in command_specs:
        d = EXEC / 'commands' / label
        expected_command_files.update(label + '/' + n for n in ['ATTEMPT.json', 'NATIVE.json', 'stdout.raw', 'stderr.raw'])
        attempt, receipt = obj(d / 'ATTEMPT.json'), obj(d / 'NATIVE.json')
        need(set(attempt) == {'argv', 'cwd', 'environment', 'started_epoch'}, ('attempt fields', label))
        need(attempt['argv'] == argv and attempt['cwd'] == str(cwd) and attempt['environment'] == ENV,
             ('literal allowed command', label))
        need(all(receipt[k] == v for k, v in attempt.items())
             and set(receipt) == set(attempt) | {'native_exit_code', 'ended_epoch', 'stdout', 'stderr'},
             ('native binds attempt', label))
        need(receipt['native_exit_code'] == 0 and last_end <= attempt['started_epoch'] <= receipt['ended_epoch'],
             ('actual ordered native exit', label))
        last_end = receipt['ended_epoch']
        out, err = read(d / 'stdout.raw'), read(d / 'stderr.raw')
        need(out == expected_stdout and err == b'' and digest(out) == receipt['stdout']
             and digest(err) == receipt['stderr'], ('full native stream equality', label))
    need(inventory(EXEC / 'commands') == expected_command_files, 'all 152 command payloads; no unsettled attempt')

    # Complete actual external/read keys, with explicit versioned historical routes.
    external = obj(EXEC / 'EXTERNAL_REFERENCES.json')
    read_key = obj(EXEC / 'READ_INPUTS.json')
    need(len(external) == result['external_files'] == 660 and len(read_key) == result['read_paths'] == 727,
         '660 external / 727 original read-key entries')
    for path, row in external.items():
        need(row['physical_path'] == path and not Path(path).is_absolute() and '..' not in Path(path).parts,
             ('workspace-relative external role', path))
        need(row['roles'] and len(set(row['roles'])) == len(row['roles'])
             and len(set(row['logical_paths'])) == len(row['logical_paths']), ('nonempty typed external roles', path))
        check_pin(ROOT / path, row['pin'])
    complete_packages = {
        QA / 'p211_initial_build_01': 362,
        QA / 'root_replays/p211_author_initial_01': 77,
        QA / 'root_replays/p211_author_pair_01': 104,
        QA / 'p211_author_initial_binding': 20,
        QA / 'p211_author_pair_binding': 10,
        QA / 'p211_initial_build_independent_reception': 18,
    }
    for base, count in complete_packages.items():
        package_rows = seal(base, count)
        need({rel(base / n) for n in list(package_rows) + ['SHA256SUMS']} <= set(external),
             ('complete accepted package physically referenced', str(base)))
    nested_seals = sorted(ROOT / p for p in external if p.endswith('/SHA256SUMS'))
    for path in nested_seals:
        seal(path.parent)

    alias = {}
    control_map = obj(EXEC / 'CONTROL_HISTORICAL_MAPPING.json')
    need(len(control_map) == 2 and {r['logical_path'] for r in control_map} == {rel(p) for p in controls},
         'two exact frozen navigation controls')
    for row in control_map:
        src, dst = ROOT / row['logical_path'], ROOT / row['physical_original']
        need(dst == EXEC / 'control_originals' / src.name, 'explicit current control route')
        check_pin(dst, row['pin'])
        need(row['pin'] == read_key[str(src)] and rel(dst) in external, 'control bound to actual freeze read key')
        need((src.stat().st_dev, src.stat().st_ino) != (dst.stat().st_dev, dst.stat().st_ino)
             and dst.stat().st_nlink == 1, 'physical non-hardlinked control original')
        alias[(str(src), row['pin']['sha256'])] = dst
    adoption_map = obj(QA / 'p211_initial_build_adoption01/HISTORICAL_MAPPING.json')
    need(len(adoption_map) == 3, 'three earlier lifecycle originals')
    for row in adoption_map:
        dst = Path(row['physical_original'])
        check_pin(dst, row['pin'])
        need(rel(dst) in external, 'adoption historical original in exact external key')
        alias[(row['logical_path'], row['pin']['sha256'])] = dst
    documentary_map = obj(QA / 'p211_author_execution_documentation01/ORIGINAL_MAPPING.json')
    need(len(documentary_map['copies']) == 5, 'five pre-execution-documentation originals')
    for row in documentary_map['copies']:
        dst, old = ROOT / row['physical_copy'], ROOT / row['root_preparation_original']
        a, b = read(dst), read(old)
        need(a == b and digest(a)['sha256'] == row['sha256'], 'documentary copy equals exact earlier preparation original')
        need((dst.stat().st_dev, dst.stat().st_ino) != (old.stat().st_dev, old.stat().st_ino), 'distinct historical physical copies')
        alias[(str(ROOT / row['source']), row['sha256'])] = dst
    prep = QA / 'p211_author_source_reception/source_preparation_original'
    preparation_manifest = obj(prep / 'SOURCE_PREPARATION_MANIFEST.json')
    old_rows = preparation_manifest['files']
    need(len(old_rows) == 27 and len({r['path'] for r in old_rows}) == 27, 'historical preparation 27 payloads')
    need(inventory(prep) == {r['path'] for r in old_rows} | {'SOURCE_PREPARATION_MANIFEST.json'}, 'historical preparation physical 28-file scope')
    for row in old_rows:
        need(not Path(row['path']).is_absolute() and '..' not in Path(row['path']).parts, 'historical preparation safe path')
        check_pin(prep / row['path'], {'bytes': row['bytes'], 'sha256': row['sha256']})
    need({rel(prep / n) for n in inventory(prep)} <= set(external), 'all 28 preparation originals externally pinned')
    expected_read_paths = {str(ROOT / p) for p in external} | {str(PAPER / n) for n in NAMES} | {
        str(FREEZE / n) for n in NAMES} | {str(p) for p in controls} | {str(EXEC / 'freeze.py')}
    need(set(read_key) == expected_read_paths, 'independently rebuilt complete 727 read-key membership')
    for logical, pin in read_key.items():
        target = alias.get((logical, pin['sha256']), Path(logical))
        check_pin(target, pin)
        if str(target) != logical:
            resolutions.append({'logical_path': logical, 'physical_path': str(target), 'pin': pin})

    # Link-only parsing, not mathematical interpretation of Markdown bodies.
    expected_links = []
    role_counts = {}
    control_targets = {ROOT / r['logical_path']: ROOT / r['physical_original'] for r in control_map}
    for name in (n for n in NAMES if n.endswith('.md')):
        original, frozen = PAPER / name, FREEZE / name
        for href in inline_targets(read(frozen).decode('utf-8')):
            url = urlsplit(href)
            if url.scheme or href.startswith('#'):
                continue
            need(not url.netloc and not url.query, ('supported exact local-link syntax', href))
            logical = (original.parent / unquote(url.path)).resolve()
            need(logical.is_relative_to(ROOT), ('local link stays in workspace', href))
            if logical.is_relative_to(PAPER) and str(logical.relative_to(PAPER)) in NAMES:
                physical_target = FREEZE / logical.relative_to(PAPER)
                role = 'frozen paper input'
                check_pin(physical_target, before[str(logical.relative_to(PAPER))])
            elif logical in control_targets:
                physical_target = control_targets[logical]
                role = 'navigation version observed at freeze, not proof evidence'
                need(rel(physical_target) in external, 'navigation copy pinned')
            else:
                physical_target = logical
                role = 'external original-location evidence link'
                if physical_target.is_dir():
                    need(physical_target == prep and len(inventory(prep)) == 28, 'sole explicitly scoped directory link')
                else:
                    need(rel(physical_target) in external, ('file link has explicit external pin', href))
                    check_pin(physical_target, external[rel(physical_target)]['pin'])
            expected_links.append({'frozen_document': rel(frozen), 'original_document': rel(original),
                                   'href': href, 'logical_target': rel(logical),
                                   'physical_target': rel(physical_target), 'role': role})
            role_counts[role] = role_counts.get(role, 0) + 1
    need(expected_links == obj(EXEC / 'MARKDOWN_LINK_MAP.json') and len(expected_links) == 59,
         'all 59 local links independently reconstructed in order')
    need(role_counts == {'external original-location evidence link': 45, 'frozen paper input': 12,
                         'navigation version observed at freeze, not proof evidence': 2}, 'exact link-role census')
    top = {'NATIVE01.json', 'RESULT.json', 'READ_INPUTS.json', 'EXTERNAL_REFERENCES.json', 'MARKDOWN_LINK_MAP.json',
           'FROZEN_ORIGIN_MAP.json', 'SOURCE_INPUTS_AFTER.json', 'CONTROL_HISTORICAL_MAPPING.json',
           'ROOT_AUTHORIZATION.md', 'freeze.py', 'EXECUTED_FREEZE_SOURCE.py', 'SOURCE_INPUTS_BEFORE.json',
           'control_originals/PIPELINE_STATE.md', 'control_originals/SYMBOLIC_DYNAMICS_STATE.md'}
    need(inventory(EXEC) == top | {'commands/' + n for n in expected_command_files}, 'entire 166-file execution scope')
    for name in sorted(inventory(EXEC)):
        read(EXEC / name)
    need(result['payloads'] == 32 and result['files_with_manifest'] == 33 and result['physical_control_originals'] == 2
         and result['all_source_before_after_frozen_bytes_equal'] is True
         and all(result[k] == 0 for k in ['builds', 'new_page_views', 'reviews', 'scientific_executions'])
         and result['paper_complete'] is False and result['external'] == 'HOLD_EXTERNAL',
         'freeze-only result scope, not science or review acceptance')
    after_pins = {p: digest(Path(p).read_bytes()) for p in reads}
    need(after_pins == reads, 'all audit-consumed bytes unchanged at completion')
    for p, names in list(inventories.items()):
        need(sorted(inventory(Path(p))) == names, ('all selected memberships unchanged', p))
    return {'status': 'PASS_PHYSICAL_DOCUMENTARY_SCOPE', 'checks': checks,
            'fully_read_paths': len(reads), 'source_frozen_pairs': 32, 'frozen_files': 33,
            'payload_bytes': 1819014, 'manifest': result['manifest'], 'native_records': 38, 'native_raw_streams': 76,
            'external_pins': 660, 'original_read_key_entries': 727, 'external_seals_checked': len(nested_seals),
            'local_links': 59, 'link_roles': role_counts, 'new_control_originals': 2,
            'earlier_adoption_originals': 3, 'earlier_documentary_copy_pairs': 5,
            'historical_preparation_files': 28, 'historical_read_key_routes': len(resolutions),
            'root_execution_files': 166, 'open_blocking_findings': 0,
            'all_audit_before_after_pins_equal': True, 'submitted_programs_executed': 0,
            'scientific_executions': 0, 'builds': 0, 'page_views': 0, 'manuscript_reviews': 0}


def save(name, value):
    # Generated audit artifacts only; never write an input or existing output.
    raw = (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with (output / name).open('xb') as stream:
        stream.write(raw)


need(len(sys.argv) == 3 and sys.argv[1] == '--output' and re.fullmatch('run[0-9]{2}', sys.argv[2]), 'explicit new own output')
output = HERE / sys.argv[2]
need(not os.path.lexists(output), 'never overwrite an earlier audit attempt')
output.mkdir()
try:
    outcome = audit()
except BaseException:
    outcome = {'status': 'FAIL_PRESERVED', 'checks_before_failure': checks, 'traceback': traceback.format_exc()}
    save('RESULT.json', outcome)
    save('READ_INPUTS_AT_FAILURE.json', reads)
    print(json.dumps(outcome, sort_keys=True))
    raise
else:
    save('READ_INPUTS_BEFORE.json', reads)
    save('READ_INPUTS_AFTER.json', {p: digest(Path(p).read_bytes()) for p in reads})
    save('INVENTORIES.json', inventories)
    save('HISTORICAL_READ_ROUTES.json', resolutions)
    save('RESULT.json', outcome)
    print(json.dumps(outcome, sort_keys=True))
