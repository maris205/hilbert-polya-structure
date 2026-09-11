#!/usr/bin/python3.10
"""SOURCE ONLY: assemble a disabled Round2 draft after separate root approval.

Disclosed adaptation of root assemble_binding02.py/read-key conventions.
No host reads, subprocesses, source imports, generic tree discovery, science,
freeze or authority issuance. This file has not been imported or executed.
The emitted draft is deliberately invalid for the enabled freeze contract.
"""
from hashlib import sha256
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round2_binding_preparation01'
OUT = QA/'p211_round2_binding_root/disabled_selection01'
EXECUTION = QA/'p211_round2_execution01'
FROZEN = ROOT/'papers/211-kernel-image-projection-feedback/frozen_round2'
READS, EXTERNAL, CATALOG = {}, {}, {}
CHECKS = 0


def need(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)


def rel(name):
    need(isinstance(name, str) and name and '\\' not in name
         and not any(c in name for c in '\x00\r\n\t')
         and not PurePosixPath(name).is_absolute()
         and PurePosixPath(name).as_posix() == name
         and all(p not in ('', '.', '..') for p in name.split('/')),
         ('normalized workspace-relative name', name))
    return name


def byte_pin(value):
    return {k:value[k] for k in ('bytes', 'sha256')}


def read(name, expected=None):
    path = ROOT/rel(name)
    need(path.is_file() and not path.is_symlink() and path.resolve() == path,
         ('ordinary explicit workspace input', name))
    before = path.stat()
    raw = path.read_bytes()
    after = path.stat()
    need(before == after and len(raw) == after.st_size, ('stable read', name))
    actual = {'bytes':len(raw), 'sha256':sha256(raw).hexdigest()}
    need(name not in READS or READS[name] == actual, ('unchanged input', name))
    if expected is not None:
        need(actual == byte_pin(expected), ('original byte pin, never refresh', name))
    READS[name] = actual
    return raw


def consume(name, role, expected=None, digest=None):
    raw = read(name, expected)
    actual = READS[name]
    if digest is not None:
        need(actual['sha256'] == digest, ('original sealed digest', name))
    row = EXTERNAL.setdefault(name, {'physical_path':name, 'pin':actual, 'roles':[]})
    need(row['pin'] == actual, ('one physical version', name))
    if role not in row['roles']:
        row['roles'].append(role)
    return raw


def reference(name, expected=None):
    consume(name, 'explicit accepted evidence reference', expected)
    return {'path':name, 'pin':READS[name]}


def consume_ref(row):
    need(set(row) == {'path', 'pin'}, 'literal reference fields')
    reference(row['path'], row['pin'])
    return row


def absolute(spelling):
    path = PurePosixPath(spelling)
    if not path.is_absolute():
        return str(ROOT/rel(spelling))
    need(str(path) == spelling and all(p not in ('.', '..', '') for p in path.parts[1:]),
         ('normalized original absolute spelling', spelling))
    return spelling


def add_catalog(spelling, value):
    key, value = absolute(spelling), byte_pin(value)
    variants = CATALOG.setdefault(key, [])
    if value not in variants:
        variants.append(value)


def known(spelling, digest=None):
    variants = CATALOG.get(absolute(spelling), [])
    if digest is not None:
        variants = [v for v in variants if v['sha256'] == digest]
    need(len(variants) == 1, ('unique exact accepted original key', spelling, digest))
    return variants[0]


def resolution(spelling, value):
    path = Path(absolute(spelling))
    if path.is_relative_to(ROOT):
        name = str(path.relative_to(ROOT))
        consume(name, 'whole inherited or SHA-list original', value)
        return {'kind':'WORKSPACE_FILE', 'physical_path':name,
                'accepted_resolution_reference':None}
    # A null here is a deliberate operational blocker, not a host check.
    return {'kind':'HOST_SEPARATE_ROOT', 'physical_path':str(path),
            'accepted_resolution_reference':None}


def sums(raw):
    need(raw.endswith(b'\n'), 'complete original SHA list')
    rows = {}
    for line in raw.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None and match[2] not in rows, 'exact unique SHA line')
        rows[match[2]] = match[1]
    need(rows, 'nonempty original SHA list')
    return rows


def main():
    need(Path.cwd() == ROOT and Path(__file__).absolute() == HERE/'assemble_disabled.py',
         'literal source placement and cwd')
    need(sys.argv[1:] == ['--write-disabled-draft'], 'explicit documentary-only invocation')
    need(not os.path.lexists(OUT) and OUT.parent.is_dir(),
         'root must independently create its assembly parent; fresh output only')
    need(not os.path.lexists(EXECUTION) and not os.path.lexists(FROZEN),
         'no physical Round2 has begun')
    prefix = str(HERE.relative_to(ROOT))+'/'
    plan = json.loads(read(prefix+'RESOLUTION_PLAN.json'))
    md_plan = json.loads(read(prefix+'MD_ORIGIN_PLAN.json'))
    json_origins = json.loads(read(prefix+'JSON_ORIGIN_PLAN.json'))
    need(plan['status'] == 'SOURCE_ONLY_NOT_EXECUTED', 'source-only plan')
    for name, value in plan['input_references'].items():
        consume(name, 'literal pinned preparation input', value)
    legacy = json.loads(read(plan['legacy_binding']))
    selected = json.loads(read(plan['intended_inventory']))
    need(len(selected['rows']) == 123 and selected['payload_count'] == 123
         and selected['payload_bytes'] == 10518152, 'exact selected 83 plus 40')
    source_map = {r['destination']:r for r in selected['rows']}
    need(len(source_map) == 123, 'no duplicated destination')
    for row in source_map.values():
        consume(row['source'], 'selected unchanged source payload', row['pin'])
    by_original = {r['original_document']:n for n,r in source_map.items()}
    need(len(by_original) == 123, 'unambiguous original document map')
    # Build the full original catalog before resolving any mixed-base list.
    inherited = {}
    originals = {}
    for spec in plan['key_roles']:
        original = json.loads(read(spec['path']))
        need(len(original) == spec['entries'], ('complete old key census', spec['role']))
        originals[spec['role']] = original
        for spelling, entry in original.items():
            value = entry['pin'] if spec['entry_layout'] == 'WRAPPED_EXTERNAL_PIN' else entry
            add_catalog(spelling, value)
    for spec in plan['key_roles']:
        mapped, workspace_count = {}, 0
        for spelling, entry in originals[spec['role']].items():
            value = byte_pin(entry['pin'] if spec['entry_layout'] == 'WRAPPED_EXTERNAL_PIN' else entry)
            mapped[spelling] = resolution(spelling, value)
            workspace_count += mapped[spelling]['kind'] == 'WORKSPACE_FILE'
        need(workspace_count == spec['workspace']
             and len(mapped)-workspace_count == spec['host'], 'whole original workspace/host split')
        inherited[spec['role']] = {'reference':reference(spec['path']),
            'entry_layout':spec['entry_layout'], 'resolutions':mapped}
    # Old document mappings are accepted physical substitutions, not a search
    # for the newest mutable index. The three original keys need no new remap.
    for name in plan['historical_mapping_references']:
        consume(name, 'preserved accepted historical mapping', plan['input_references'][name])
    trees = []
    for spec in legacy['external_trees']:
        consume_ref(spec['accepted_scope_reference'])
        for name in spec['files']:
            physical = spec['root']+'/'+rel(name)
            consume(physical, 'unchanged explicit inherited external tree', known(physical))
        trees.append(spec)
    need(len(trees) == 26, 'entire literal inherited tree scope')
    empties = {
        str((QA/'root_replays/p211_b_initial_01').relative_to(ROOT)):['child01/commands'],
        str((QA/'root_replays/p211_b_pair_01').relative_to(ROOT)):
            ['child01/commands', 'child02/commands']}
    for spec in plan['additional_trees']:
        seal = spec['root']+'/SHA256SUMS'
        rows = sums(consume(seal, 'exact selected accepted tree seal',
                            plan['input_references'][seal]))
        need('SHA256SUMS' not in rows and len(rows)+1 == spec['expected_files'],
             'whole nonself additional tree census')
        for name, digest in rows.items():
            consume(spec['root']+'/'+rel(name), 'explicit seal-selected external tree', digest=digest)
        trees.append({'root':spec['root'], 'files':sorted([*rows, 'SHA256SUMS']),
            'empty_directories':empties.get(spec['root'], []), 'manifest':'SHA256SUMS',
            'accepted_scope_reference':consume_ref(spec['accepted_scope_reference'])})
    need(len(trees) == 33 and len({r['root'] for r in trees}) == 33, 'exact distinct selected trees')
    sha_bases = []
    for spec in plan['sha_lists']:
        name = spec['document']
        rows = sums(read(source_map[name]['source']))
        need(len(rows) == spec['entries'], ('complete mixed-base SHA count', name))
        origin = md_plan['review_b/REPORT.md' if name.startswith('review_b/') else 'review_a/REPORT.md']['accepted_origin_reference']
        consume_ref(origin)
        mapped = {n:{'pin':known(n, h), 'resolution':resolution(n, known(n, h))}
                  for n,h in rows.items()}
        need(sum(r['resolution']['kind'] == 'HOST_SEPARATE_ROOT' for r in mapped.values())
             == spec['host_entries'], ('complete SHA host split', name))
        sha_bases.append({'document':name, 'base':'',
            'accepted_origin_reference':origin, 'resolutions':mapped})
    need({s['document'] for s in sha_bases} == {n for n in source_map if n.endswith('.sha256')},
         'all six lists covered, no list omitted')
    origins = {}
    for name, spec in md_plan.items():
        row = source_map[name]
        need(spec['original_document'] == row['original_document'], 'exact original Markdown')
        consume_ref(spec['accepted_origin_reference'])
        if 'local_links' in spec:
            # All unchanged R1 mappings and historical physical targets survive.
            links = spec['local_links']
        else:
            links = []
            for href in spec['local_hrefs']:
                original = ROOT/row['original_document']
                logical = Path(os.path.abspath(original.parent/unquote(href.split('#',1)[0])))
                need(logical.is_relative_to(ROOT), 'B local links remain workspace-scoped')
                target = str(logical.relative_to(ROOT))
                if target in by_original:
                    link = {'href':href, 'logical_target':target, 'kind':'copied',
                            'target':by_original[target]}
                else:
                    consume(target, 'complete B original-document link', known(target))
                    link = {'href':href, 'logical_target':target, 'kind':'external_file',
                            'target':target, 'accepted_resolution_reference':
                            spec['accepted_origin_reference']}
                links.append(link)
        for link in links:
            if link['kind'] == 'external_file':
                consume(link['target'], 'preserved original Markdown target', known(link['target']))
                consume_ref(link['accepted_resolution_reference'])
            elif link['kind'] == 'external_directory':
                for child in link['directory_files']:
                    target = link['target']+'/'+rel(child)
                    consume(target, 'entire accepted original directory link', known(target))
                consume_ref(link['accepted_resolution_reference'])
            else:
                need(link['kind'] == 'copied' and link['target'] in source_map, 'copied role')
        origins[name] = {'original_document':row['original_document'],
            'accepted_origin_reference':spec['accepted_origin_reference'], 'local_links':links}
    need(len(origins) == 35 and set(origins) == {n for n in source_map if n.endswith('.md')},
         'complete 35 original Markdown roles')
    need(len(json_origins) == 57
         and set(json_origins) == {n for n in source_map if n.endswith('.json')},
         'complete 57 original JSON roles')
    for name, spec in json_origins.items():
        need(spec['original_document'] == source_map[name]['original_document'], 'exact JSON origin')
        consume_ref(spec['accepted_origin_and_schema_reference'])
        if 'original_top_level_keys' in spec:
            need(set(json.loads(read(source_map[name]['source']))) == set(spec['original_top_level_keys']),
                 ('preserved exact B JSON schema keys', name))
    lock = json.loads(read(plan['runtime_lock']))
    need(len(lock['files']) == 122, 'existing complete 122-spelling runtime input')
    runtime = {}
    for spelling, value in lock['files'].items():
        physical, value = value['resolved'], byte_pin(value)
        need(Path(physical).is_absolute(), 'declared resolved runtime spelling')
        if Path(physical).is_relative_to(ROOT):
            consume(str(Path(physical).relative_to(ROOT)),
                    'existing workspace runtime source, data only', value)
        need(physical not in runtime or runtime[physical] == value, 'agreeing accepted runtime aliases')
        runtime[physical] = value
    need(len(runtime) == 114, 'exact finite existing resolved-file bound')
    tools = legacy['native_tool_pins']
    need(set(tools) == {'/usr/bin/cp', '/usr/bin/cmp', '/usr/bin/sha256sum', '/usr/bin/python3.10'},
         'four literal native tools, old pins retained')
    refs = {role:reference(path) for role,path in plan['acceptance_role_paths'].items()}
    binding = {
        'schema':'p211-round2-root-binding-v1', 'enabled':False,
        'execution_directory':str(EXECUTION.relative_to(ROOT)),
        'root_authorization':{'issuer':None, 'decision':None, 'record':None},
        'execution_source_pin':READS[str((QA/'p211_round2_preparation01/freeze.py').relative_to(ROOT))],
        'preparation_manifest':reference(str((QA/'p211_round2_preparation01/SHA256SUMS').relative_to(ROOT))),
        'base_source':reference(str((QA/'p211_round1_adapter02/freeze.py').relative_to(ROOT))),
        'intended_inventory':reference(plan['intended_inventory']),
        'acceptance_references':refs,
        'b_acceptance':{'reviewer':'/root/round211_rational_scout/relation_primary_sources',
            'same_reviewer_accepted_exact_delta':True, 'root_received_whole_final_originals':True,
            'current_open_findings':0, 'accepted_final_manifest_pin':
                {'bytes':3549, 'sha256':'45b7c0337259da2fccb078cf4d7b84ec7228a16a6bf6089167c19a26c477ca46'}},
        'host_reuse_boundary':{
            'mode':'ROOT_SEPARATE_COMPLETE_HOST_KEYS_AND_SETTINGS_RECHECK',
            'complete_host_key_references':[reference(s['path']) for s in plan['key_roles']],
            'accepted_settings_references':[reference(n) for n in plan['accepted_settings_paths']],
            'precopy_recheck_references':[],
            'postcopy_root_recheck_required':True,
            'recorder_rehashes_complete_reused_host_keys':False},
        'inherited_input_keys':inherited, 'external_trees':trees,
        'native_tool_pins':tools, 'recorder_runtime_file_pins':runtime,
        'pin_list_bases':sha_bases, 'document_origins':origins, 'json_pin_bases':json_origins}
    binding['external_inputs'] = [EXTERNAL[k] for k in sorted(EXTERNAL)]
    for row in binding['external_inputs']:
        path = ROOT/row['physical_path']
        need(not path.is_relative_to(EXECUTION) and not path.is_relative_to(FROZEN),
             'no future execution or frozen self-input')
    for name, value in dict(READS).items():
        read(name, value)
    report = {'status':'DISABLED_DRAFT_ASSEMBLED_PENDING_SEPARATE_ROOT_AUTHORITY',
        'checks':CHECKS, 'workspace_read_paths':len(READS), 'external_files':len(EXTERNAL),
        'external_trees':33, 'original_key_rows':[2255,2164,1785],
        'sha_list_rows':[32,33,1774,50,84,515], 'markdown_origins':35, 'json_origins':57,
        'runtime_original_spellings':122, 'runtime_resolved_files':114, 'host_files_read':0,
        'blocking_fields':['enabled false','root issuer/decision/record null',
            'precopy reference list empty','all host original resolutions have null references'],
        'source_execution_scope':'this future documentary assembly only; no recorder or science',
        'postcopy_full_host_settings_and_build_recheck':'NOT_PERFORMED_FUTURE_ROOT_OBLIGATION',
        'scientific_runs':0, 'builds':0, 'physical_round2_created':False, 'paper_complete':False}
    OUT.mkdir()
    for name,value in [('BINDING_DISABLED_DRAFT.json',binding),('INPUTS.json',READS),('RESULT.json',report)]:
        with (OUT/name).open('x') as stream:
            json.dump(value,stream,sort_keys=True,indent=2)
            stream.write('\n')
    print(json.dumps(report,sort_keys=True))


if __name__ == '__main__':
    main()
