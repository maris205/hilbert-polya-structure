"""Assemble one exact root-authorized Round1 binding, without any freeze.

Only accepted named ledgers/trees and explicit original-document targets are
read. No copied JSON is executed or interpreted as new scientific evidence.
Output is a proposed exact binding outside the future execution directory;
root still inspects it before the separate physical invocation.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round1_binding_root'
PREP = QA/'p211_round1_adapter02'
A = ROOT/'docs/papers211_215_sequence/reviews/p211_a'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
R0 = PAPER/'frozen_round0'
EXEC = QA/'p211_round1_execution01'
OUT = HERE/'selection02'
EXT, READS, TREES = {}, {}, {}
CHECKS = 0
# Exact forward revision for the preserved pre-entry failure; not a prune.
EMPTY_DIRECTORIES = {
    "docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01": [
        "child01/commands"
    ],
    "docs/papers211_215_sequence/qa/root_replays/p211_a_pair_01": [
        "child01/commands",
        "child02/commands"
    ],
    "docs/papers211_215_sequence/qa/p211_runtime_preparation": [
        "discovery01/empty_probe_capsule",
        "discovery02/empty_probe_capsule",
        "tests01/existing_cache",
        "tests02/existing_cache",
        "tests02/fixture_initial/child01/commands",
        "tests02/fixture_pair/child01/commands",
        "tests02/fixture_pair/child02/commands"
    ]
}


def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def relative(path):
    path = Path(path)
    need(path.is_absolute() and path.is_relative_to(ROOT), ('workspace path', str(path)))
    return path.relative_to(ROOT).as_posix()


def read(path):
    path = Path(path)
    need(path.is_file() and not path.is_symlink() and path.resolve() == path, ('ordinary source', str(path)))
    raw = path.read_bytes()
    key = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}
    need(str(path) not in READS or READS[str(path)] == key, ('unchanged read', str(path)))
    READS[str(path)] = key
    return raw


def pin(path):
    read(path)
    return READS[str(Path(path))]


def obj(path):
    return json.loads(read(path))


def consume(path, role, expected=None, logical=None):
    path = Path(path)
    name = relative(path)
    actual = pin(path)
    if expected is not None:
        need(actual == {k: expected[k] for k in ('bytes','sha256')}, ('accepted exact bytes', name))
    row = EXT.setdefault(name, {'physical_path': name, 'pin': actual, 'roles': [], 'logical_paths': []})
    need(row['pin'] == actual, ('one exact external version', name))
    if role not in row['roles']:
        row['roles'].append(role)
    if logical is not None:
        logical = relative(logical) if Path(logical).is_absolute() else logical
        if logical not in row['logical_paths']:
            row['logical_paths'].append(logical)
    return actual


def reference(path, role='accepted original reference'):
    return {'path': relative(path), 'pin': consume(path, role)}


def members(base):
    need(base.is_dir() and base.resolve() == base, ('ordinary selected tree', str(base)))
    files = []
    for p in sorted(base.rglob('*')):
        need(p.resolve() == p and (p.is_dir() or p.is_file()), ('ordinary tree entry', str(p)))
        if p.is_file():
            files.append(p.relative_to(base).as_posix())
    return files


def manifest(path):
    rows = {}
    raw = read(path)
    need(raw.endswith(b'\n'), ('complete manifest', str(path)))
    for line in raw.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(m is not None, ('exact manifest line', str(path)))
        digest, name = m.groups()
        need(name not in rows and not Path(name).is_absolute() and '..' not in Path(name).parts,
             ('safe manifest path', name))
        value = pin(path.parent/name)
        need(value['sha256'] == digest, ('whole sealed file', str(path), name))
        rows[name] = value
    return rows


def tree(base, scope_reference, seal_name='SHA256SUMS', expected_files=None):
    files = members(base)
    if expected_files is not None:
        need(len(files) == expected_files, ('whole accepted tree population', str(base)))
    if seal_name is not None:
        rows = manifest(base/seal_name)
        need(set(rows) == set(files)-{seal_name}, ('whole nonself tree', str(base)))
    for name in files:
        consume(base/name, 'complete accepted tree '+relative(base))
    empties = EMPTY_DIRECTORIES.get(relative(base), [])
    actual_dirs = {'.'} | {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_dir()}
    expected_dirs = {'.'} | set(empties)
    for name in files + empties:
        expected_dirs.update(p.as_posix() for p in Path(name).parents)
    need(actual_dirs == expected_dirs, ('complete exact selected directory membership', str(base)))
    for name in empties:
        need(not any((base/name).iterdir()), ('literal ordinary truly empty directory', str(base/name)))
    spec = {'root': relative(base), 'files': files, 'empty_directories': empties,
            'manifest': seal_name if seal_name == 'SHA256SUMS' else None,
            'accepted_scope_reference': scope_reference}
    need(relative(base) not in TREES or TREES[relative(base)] == spec, 'consistent tree interpretation')
    TREES[relative(base)] = spec
    return files


need(Path.cwd() == ROOT and not os.path.lexists(OUT), 'new exact selection output')
need(not os.path.lexists(EXEC) and not os.path.lexists(PAPER/'frozen_round1'), 'freeze has not started')
consume(Path(__file__), 'root binding assembly source')
auth = reference(HERE/'SOURCE_RECEPTION_AND_AUTHORIZATION02.md', 'root explicit physical authorization')
precheck = obj(HERE/'precopy02/RESULT.json')
need(precheck['status'] == 'PASS_COMPLETE_PREPARATION_AND_HOST_KEY_SETTINGS_RECHECK'
     and precheck['phase'] == 'precopy' and precheck['accepted_key_entries'] == 1688,
     'actual root full-key/settings precheck')
for name in ('PRECOPY_NATIVE02.json','PREPARATION_SEAL_NATIVE02.json','PREPARATION_RECEPTION02.json','BUILD_PRECOPY_NATIVE02.json',
             'recheck02.py','precopy02/RESULT.json','precopy02/READ_INPUTS.json'):
    consume(HERE/name, 'actual root preparation and precopy evidence')
whole_a_ref = reference(QA/'p211_a_final_root/RECEPTION.md')
round0_ref = reference(QA/'p211_round0_root_reception/RECEPTION.md')
runtime_ref = reference(QA/'P211_A_RUNTIME_RECEPTION.md')
build_ref = reference(QA/'p211_initial_build_root_reception/RECEPTION.md')
author = obj(QA/'p211_round0_execution01/SOURCE_INPUTS_AFTER.json')
need(len(author) == 32, 'exact author baseline')
response_keys = obj(QA/'p211_a_report_root/RESPONSE_KEYS.json')
need(set(response_keys['author_before_after']) == set(author), 'complete accepted response names')
for name, value in author.items():
    for role in ('before','after','frozen'):
        need({k: response_keys['author_before_after'][name][role][k] for k in ('bytes','sha256')} == value,
             ('actual accepted no-change author key', name, role))
    consume(PAPER/name, 'unchanged live author baseline', value)
    consume(R0/name, 'unchanged physical Round0', value)
apayloads = manifest(A/'SHA256SUMS')
need(len(apayloads) == 50 and sum(v['bytes'] for v in apayloads.values()) == 2614821, 'complete final A package')
amanifest = pin(A/'SHA256SUMS')
need(amanifest['sha256'] == 'a0677d174d3e9af26b32fabb8a97e099d12753101734a6fe43252eea636b97cc', 'accepted final A seal')
decision = obj(A/'DELTA_ACCEPTANCE.json')
need(decision['reviewer'] == '/root/round211_rational_scout/relation_primary_sources/lyndon_primary_check'
     and decision['status'] == 'ACCEPTED_EXACT_NO_CHANGE_BY_SAME_A_REVIEWER'
     and decision['delta_accepted'] is True and decision['delta_received'] is True
     and decision['actual_decision_after_evidence'] is True
     and decision['current_open_findings'] == {'Critical':0,'Major':0,'Minor':0,'total':0}
     and decision['author_changes'] == {'added':[],'removed':[],'modified':[]}, 'same-A actual semantic decision correspondence')
for key in ('response','response_keys'):
    r = decision[key]
    consume(ROOT/r['path'], 'same-A exact '+key, r)
roles = {
    'round0_root_reception': QA/'p211_round0_root_reception/RECEPTION.md',
    'round0_complete_execution_read_key': QA/'p211_round0_execution01/READ_INPUTS.json',
    'a_final_report': A/'REPORT.md', 'a_final_findings': A/'FINDINGS.json',
    'root_exact_response': ROOT/'docs/papers211_215_sequence/P211_A_RESPONSE.md',
    'same_a_accepted_delta': A/'DELTA.md', 'a_same_reviewer_acceptance': A/'DELTA_ACCEPTANCE.json',
    'root_whole_a_reception': QA/'p211_a_final_root/RECEPTION.md',
    'a_initial_output_reception': QA/'p211_a_initial_binding/OUTPUT_SEMANTICS_NATIVE01.json',
    'a_exclusive_canonical_adoption': QA/'p211_a_initial_binding/ADOPTION/RESULT.json',
    'a_strict_pair_and_three_native_comparisons': QA/'P211_A_RUNTIME_RECEPTION.md',
    'a_complete_runtime_dependency_key': QA/'p211_runtime_preparation/discovery02/RUNTIME_LOCK.json',
    'a_schema_and_parameter_explanation': A/'CANONICAL_SCHEMA.md',
    'accepted_build_complete_key': QA/'p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json',
    'actual_all_page_view_reception': QA/'p211_initial_build_root_reception/RECEPTION.md',
    'author_delta_before_key': QA/'p211_a_report_root/RESPONSE_KEYS.json',
    'author_delta_after_key': QA/'p211_a_report_root/RESPONSE_KEYS.json'}
acceptance_refs = {name: reference(path, 'acceptance role '+name) for name,path in roles.items()}
# The accepted full A reception key contains host files. Only its entire
# ordinary-workspace projection is bound to the recorder; root separately
# rechecked all host entries and current runtime/build settings.
full_key = obj(QA/'p211_a_final_root/run01/READ_INPUTS.json')
need(len(full_key) == 1688, 'entire accepted A key')
for path, value in full_key.items():
    if Path(path).is_relative_to(ROOT):
        consume(Path(path), 'entire accepted A workspace key', value)
need(sum(Path(p).is_relative_to(ROOT) for p in full_key) == 889, 'exact workspace/host split')
# Every historical Round0 key uses the already accepted exact physical
# version. No historical checksum is regenerated from mutable navigation.
mapping_path = QA/'p211_round0_execution01/CONTROL_HISTORICAL_MAPPING.json'
maps = {r['logical_path']:r for r in obj(mapping_path)}
consume(mapping_path, 'accepted complete old navigation mapping')
old_resolutions = {}
for filename, field, external in [('READ_INPUTS.json','round0_read_resolutions',False),
                                  ('EXTERNAL_REFERENCES.json','round0_external_resolutions',True)]:
    old = obj(QA/'p211_round0_execution01'/filename)
    need(len(old) == (660 if external else 727), 'entire old key population')
    resolved = {}
    for logical, row in old.items():
        value = row['pin'] if external else row
        name = relative(logical) if Path(logical).is_absolute() else logical
        if name in maps:
            need(maps[name]['pin'] == value, ('exact old-version correspondence', name))
            physical = maps[name]['physical_original']
        else:
            physical = name
        consume(ROOT/physical, 'whole inherited Round0 '+filename, value, logical)
        resolved[logical] = physical
    old_resolutions[field] = resolved
# Complete explicitly named physical evidence scopes. A tree with a historic
# non-SHA256SUMS seal keeps that original spelling; recorder gets its exact
# membership plus accepted reference, never a rebased manifest.
scope_trees = [
    ('p211_round1_adapter01',auth,'SHA256SUMS',17),
    ('p211_round1_adapter02',auth,'SHA256SUMS',None),
    ('p211_round1_preparation',auth,'SHA256SUMS',6),
    ('p211_round1_plan_audit',auth,'SHA256SUMS',3),
    ('p211_round0_execution01',round0_ref,None,166),
    ('p211_round0_root_reception',round0_ref,'SHA256SUMS',None),
    ('p211_round0_independent_reception',round0_ref,'SHA256SUMS',9),
    ('p211_a_final_root',whole_a_ref,'SHA256SUMS',15),
    ('p211_a_report_root',whole_a_ref,None,None),
    ('p211_a_root_reception',runtime_ref,None,None),
    ('p211_a_initial_binding',runtime_ref,'SHA256SUMS',18),
    ('p211_a_pair_binding',runtime_ref,'SHA256SUMS',11),
    ('p211_a_binding_closure',runtime_ref,None,None),
    ('root_replays/p211_a_initial_01',runtime_ref,'SHA256SUMS',78),
    ('root_replays/p211_a_pair_01',runtime_ref,'SHA256SUMS',105),
    ('p211_initial_build_01',build_ref,'SHA256SUMS',363),
    ('p211_initial_build_independent_reception',build_ref,'SHA256SUMS',19),
    ('p211_initial_build_root_reception',build_ref,None,None),
    ('p211_initial_build_binding01',build_ref,None,None),
    ('p211_initial_build_adoption01',build_ref,None,None),
    ('p211_runtime_preparation',runtime_ref,'MANIFEST.sha256',626),
    ('p211_runtime_independent_audit',runtime_ref,'MANIFEST.sha256',42),
    ('p211_runtime_root_reception',runtime_ref,None,None)]
for name, ref, seal_name, count in scope_trees:
    tree(QA/name, ref, seal_name, count)
tree(A, whole_a_ref, 'SHA256SUMS', 51)
tree(R0, round0_ref, 'SHA256SUMS', 33)
# All copied documents preserve their actual original origin. There are no
# embedded historical Markdown copies in the final A membership.
source_map = {n:{'source':R0/n,'original':PAPER/n} for n in author}
source_map.update({'review_a/'+n:{'source':A/n,'original':A/n} for n in [*apayloads,'SHA256SUMS']})
old_links = obj(QA/'p211_round0_execution01/MARKDOWN_LINK_MAP.json')
origins = {}
for name, row in sorted(source_map.items()):
    if not name.endswith('.md'):
        continue
    source, original = row['source'], row['original']
    body = read(source).decode()
    need(re.search(r'(?m)^\s{0,3}\[[^\]\n]+\]:',body) is None
         and re.search(r'\[[^\]\n]*\]\[[^\]\n]*\]',body) is None, ('bounded supported inline syntax',name))
    links = []
    for m in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',body):
        href = m.group(1).strip().strip('<>')
        if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',href) or href.startswith('#'):
            continue
        logical = Path(os.path.abspath(original.parent/unquote(href.split('#',1)[0])))
        logical_name = relative(logical)
        if logical.is_relative_to(PAPER) and logical.relative_to(PAPER).as_posix() in author:
            target = logical.relative_to(PAPER).as_posix()
            link = {'href':href,'logical_target':logical_name,'kind':'copied','target':target}
        elif logical.is_relative_to(A) and 'review_a/'+logical.relative_to(A).as_posix() in source_map:
            target = 'review_a/'+logical.relative_to(A).as_posix()
            link = {'href':href,'logical_target':logical_name,'kind':'copied','target':target}
        else:
            # Match the complete accepted original author link row, not an
            # arbitrary newest navigation version or a digest-only search.
            old_match = [r for r in old_links if r['original_document'] == relative(original)
                         and r['href'] == href and r['logical_target'] == logical_name]
            need(len(old_match) <= 1, 'unambiguous accepted old link')
            target_path = ROOT/old_match[0]['physical_target'] if old_match else logical
            evidence = round0_ref if old_match else whole_a_ref
            if target_path.is_file():
                consume(target_path, 'exact original-document link', logical=logical)
                link = {'href':href,'logical_target':logical_name,'kind':'external_file',
                        'target':relative(target_path),'accepted_resolution_reference':evidence}
            else:
                files = members(target_path)
                for f in files:
                    consume(target_path/f, 'complete original-document directory link')
                if relative(target_path) not in TREES:
                    tree(target_path,evidence,None)
                link = {'href':href,'logical_target':logical_name,'kind':'external_directory',
                        'target':relative(target_path),'directory_files':files,
                        'accepted_resolution_reference':evidence}
        links.append(link)
    origins[name] = {'original_document':relative(original),
                     'accepted_origin_reference':whole_a_ref if name.startswith('review_a/') else None,
                     'local_links':links}
pin_bases = []
for name, row in source_map.items():
    if not name.endswith('.sha256'):
        continue
    need(name in ('review_a/INPUT_PINS.sha256','review_a/EXTERNAL_READ_PINS.sha256'), 'literal known A pin lists')
    resolutions = {}
    for line in read(row['source']).decode().splitlines():
        digest, logical = line.split('  ',1)
        need(logical not in resolutions, 'unique original pin-list target')
        value = consume(ROOT/logical, 'copied A workspace-root pin list', logical=logical)
        need(value['sha256'] == digest, ('actual original pin-list target',logical))
        resolutions[logical] = logical
    pin_bases.append({'document':name,'base':'','accepted_origin_reference':whole_a_ref,'resolutions':resolutions})
# Explicit original JSON schema/base annotations preserve all bytes. These
# are metadata, not a new generic nested-JSON interpretation or audit.
json_bases = {}
for name, row in source_map.items():
    if name.endswith('.json'):
        is_a = name.startswith('review_a/')
        json_bases[name] = {
            'base':relative(A if is_a else PAPER),
            'accepted_origin_and_schema_reference':whole_a_ref if is_a else round0_ref,
            'scope_note':'Unchanged JSON at its original document location. Absolute and workspace-root path fields retain those explicit field meanings; nested native-result/source pin schemas are those received in the cited original reception. This annotation does not rebase any path or claim generic recursive validation.'}
json_bases['SOURCE_INPUT_PINS.json']['base'] = ''
json_bases['SOURCE_INPUT_PINS.json']['scope_note'] = ('The literal path_base is the workspace root; all 18 files[] path/bytes/sha256 rows retain that base and are explicitly consumed. No path rebasing.')
for row in obj(PAPER/'SOURCE_INPUT_PINS.json')['files']:
    consume(ROOT/row['path'], 'complete 18-row original author source pin list', row)
json_bases['SOURCE_PREPARATION_MANIFEST.json']['scope_note'] = ('The files[] names have original live-paper-relative meaning at the pre-Round0 preparation stage, not current final-paper bytes. All 27 rows resolve to the accepted physical source_preparation_original directory in qa/p211_author_source_reception. The Round0 receipt explicitly validates that 28-file historical scope. No historical digest is refreshed.')
old_prep = QA/'p211_author_source_reception/source_preparation_original'
for row in obj(PAPER/'SOURCE_PREPARATION_MANIFEST.json')['files']:
    consume(old_prep/row['path'], 'complete 27-row historical author preparation', row)
tool_pins = {p:pin(Path(p)) for p in ('/usr/bin/cp','/usr/bin/cmp','/usr/bin/sha256sum','/usr/bin/python3.10')}
binding = {
    'schema':'p211_round1_binding_v2','enabled':True,'execution_directory':relative(EXEC),
    'root_authorization':{'issuer':'/root','decision':'AUTHORIZE_PHYSICAL_P211_ROUND1_FROM_ACCEPTED_FINAL_A','record':auth},
    'execution_source_pin':pin(PREP/'freeze.py'),
    'preparation_manifest':reference(PREP/'SHA256SUMS'),
    'role_preparation_manifest':reference(QA/'p211_round1_preparation/SHA256SUMS'),
    'author_delta_before':author,'author_delta_after':author,
    'acceptance_references':acceptance_refs,
    'a_acceptance':{'reviewer':decision['reviewer'],'current_open_findings':0,
                    'same_reviewer_accepted_exact_delta':True,'root_received_whole_originals':True,
                    'accepted_final_manifest_pin':amanifest},
    'a_package':{'root':relative(A),'manifest_pin':amanifest,'payloads':apayloads,'payload_count':50,'all_file_count':51},
    'host_reuse_boundary':{'mode':'ROOT_SEPARATE_COMPLETE_HOST_KEY_AND_SETTINGS_RECHECK',
        'complete_host_key_reference':reference(QA/'p211_a_final_root/run01/READ_INPUTS.json'),
        'accepted_runtime_settings_reference':reference(QA/'p211_a_pair_binding/BINDING.json'),
        'precopy_recheck_reference':reference(HERE/'precopy02/RESULT.json'),
        'postcopy_root_recheck_required':True,'recorder_rehashes_complete_host_key':False},
    'external_trees':list(TREES.values()), **old_resolutions,
    'native_tool_pins':tool_pins,'pin_list_bases':pin_bases,'json_pin_bases':json_bases,'document_origins':origins}
binding['external_inputs'] = [EXT[k] for k in sorted(EXT)]
schema = obj(PREP/'BINDING.schema.json')
need(set(binding) == set(schema['required']), 'complete exact binding fields')
need(len(source_map) == 83 and len(acceptance_refs) == 17, 'complete physical/acceptance roles')
need(not any((ROOT/p).is_relative_to(EXEC) or (ROOT/p).is_relative_to(PAPER/'frozen_round1') for p in EXT), 'no output/self-referent')
for path, expected in dict(READS).items():
    need(pin(path) == expected, ('all assembly inputs unchanged',path))
result = {'status':'EXACT_BINDING_ASSEMBLED_NOT_EXECUTED','checks':CHECKS,'read_paths':len(READS),
          'external_files':len(EXT),'external_trees':len(TREES),'author_payloads':32,'a_files':51,
          'round1_payloads':83,'round1_files_with_manifest':84,'native_copy_commands_planned':119,
          'round0_read_resolutions':len(old_resolutions['round0_read_resolutions']),
          'round0_external_resolutions':len(old_resolutions['round0_external_resolutions']),
          'copied_markdown_documents':len(origins),'local_links':sum(len(r['local_links']) for r in origins.values()),
          'copied_pin_lists':len(pin_bases),'json_base_annotations':len(json_bases),
          'scientific_executions':0,'recorder_executions':0,'round1_accepted':False}
OUT.mkdir()
for name, value in [('BINDING_READY.json',binding),('INPUTS.json',READS),('RESULT.json',result)]:
    with (OUT/name).open('x') as stream:
        json.dump(value,stream,sort_keys=True,indent=2); stream.write('\n')
print(json.dumps(result,sort_keys=True))
