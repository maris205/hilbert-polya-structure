#!/usr/bin/python3.10
"""Read-only preparation syntax/metadata checks; never import either recorder."""
import ast
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT/'docs/papers211_215_sequence/qa/p211_round1_adapter02'
OLD = ROOT/'docs/papers211_215_sequence/qa/p211_round0_execution01'
UPSTREAM = ROOT/'docs/papers211_215_sequence/qa/p211_round1_preparation'
PREVIOUS = ROOT/'docs/papers211_215_sequence/qa/p211_round1_adapter01'
PREFLIGHT_FAILURE = ROOT/'docs/papers211_215_sequence/qa/p211_round1_binding_root/ENTRY_PREFLIGHT_FAILED01_NATIVE.json'
ALLOWED = {PREVIOUS/'freeze.py',PREVIOUS/'BINDING.schema.json',PREVIOUS/'BINDING_PENDING.json',
           PREVIOUS/'SHA256SUMS',PREFLIGHT_FAILURE,HERE/'freeze.py',HERE/'BINDING.schema.json',HERE/'BINDING_PENDING.json',
           HERE/'static_check.py',OLD/'freeze.py',OLD/'SOURCE_INPUTS_AFTER.json',
           OLD/'READ_INPUTS.json',OLD/'EXTERNAL_REFERENCES.json',
           UPSTREAM/'ROLE_SELECTION_DRAFT.json'}
read_keys, checks = {}, []


def need(value,label):
    if not value:
        raise AssertionError(label)
    checks.append(label)


def read(path):
    need(path in ALLOWED and path.is_file() and not path.is_symlink(), 'whitelisted ordinary metadata/source path: '+str(path.relative_to(ROOT)))
    raw = path.read_bytes()
    read_keys[str(path.relative_to(ROOT))] = {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
    return raw


def assignment(tree,name):
    rows = [n.value for n in tree.body if isinstance(n,ast.Assign) and
            any(isinstance(t,ast.Name) and t.id == name for t in n.targets)]
    need(len(rows) == 1,'one top-level assignment: '+name)
    return rows[0]


def names(tree):
    value = assignment(tree,'NAMES')
    need(isinstance(value,ast.Call) and isinstance(value.func,ast.Attribute) and
         value.func.attr == 'split' and isinstance(value.func.value,ast.Constant) and
         not value.args and not value.keywords,'literal NAMES split, no recorder evaluation')
    return value.func.value.value.split()


raw = read(HERE/'freeze.py')
tree = ast.parse(raw,filename=str(HERE/'freeze.py'))
compile(tree,str(HERE/'freeze.py'),'exec')
need(True,'new recorder parses and compiles without execution or import')
old_tree = ast.parse(read(OLD/'freeze.py'),filename=str(OLD/'freeze.py'))
own_tree = ast.parse(read(HERE/'static_check.py'),filename=str(HERE/'static_check.py'))
need(isinstance(own_tree,ast.Module),'static checker source parsed')
current_names,old_names = names(tree),names(old_tree)
ledger = json.loads(read(OLD/'SOURCE_INPUTS_AFTER.json'))
draft = json.loads(read(UPSTREAM/'ROLE_SELECTION_DRAFT.json'))
need(len(current_names) == len(set(current_names)) == 32 and
     current_names == old_names and set(current_names) == set(ledger),
     'exact accepted 32-name baseline preserved')
need({r['relative_name']:r['pin'] for r in draft['author_role']['payloads']} == ledger,
     'upstream 32 name/size/hash metadata rows equal accepted ledger')
need(sum(v['bytes'] for v in ledger.values()) == 1819014,'accepted author metadata byte total')
old_reads = json.loads(read(OLD/'READ_INPUTS.json'))
old_external = json.loads(read(OLD/'EXTERNAL_REFERENCES.json'))
need(len(old_reads) == 727 and len(old_external) == 660,'exact inherited metadata-key counts; no referent opened')
for symbol,path in [('BASE_SOURCE_SHA256',OLD/'freeze.py'),('LEDGER_SHA256',OLD/'SOURCE_INPUTS_AFTER.json'),
                    ('ROUND0_READ_SHA256',OLD/'READ_INPUTS.json'),('ROUND0_EXTERNAL_SHA256',OLD/'EXTERNAL_REFERENCES.json')]:
    need(ast.literal_eval(assignment(tree,symbol)) == read_keys[str(path.relative_to(ROOT))]['sha256'],
         'fixed accepted source/metadata pin: '+symbol)
schema = json.loads(read(HERE/'BINDING.schema.json'))
pending = json.loads(read(HERE/'BINDING_PENDING.json'))
need(set(schema['required']) == set(schema['properties']) == set(pending),'schema/template top-level fields agree')
need(schema['properties']['enabled'] == {'const':True} and pending['enabled'] is False,
     'pending template deliberately cannot satisfy enabled binding schema')
roles = ast.literal_eval(assignment(tree,'ACCEPTANCE_ROLES'))
need(len(roles) == 17 and roles == set(schema['properties']['acceptance_references']['required']) ==
     set(schema['properties']['acceptance_references']['properties']) == set(pending['acceptance_references']),
     'all 17 literal acceptance-reference roles agree')
need(all(v is None for v in pending['acceptance_references'].values()),'all actual acceptance references remain pending')
need(pending['a_package']['manifest_pin'] is None and pending['a_package']['payloads'] is None and
     pending['a_package']['payload_count'] is None and pending['a_package']['all_file_count'] is None,
     'no final A pin/member/count binding invented')
need(pending['a_acceptance']['accepted_final_manifest_pin'] is None and
     pending['a_acceptance']['current_open_findings'] is None and
     pending['a_acceptance']['same_reviewer_accepted_exact_delta'] is None and
     pending['a_acceptance']['root_received_whole_originals'] is None,
     'root final-A acceptance flags remain pending')
fixed_pending = {'schema','enabled','acceptance_references','a_package','a_acceptance'}
need(all(v is None for k,v in pending.items() if k not in fixed_pending),
     'all actual execution/external/origin bindings remain null')
need(pending['host_reuse_boundary'] is None and
     schema['properties']['host_reuse_boundary']['properties']['recorder_rehashes_complete_host_key'] == {'const':False} and
     schema['properties']['host_reuse_boundary']['properties']['postcopy_root_recheck_required'] == {'const':True},
     'host boundary stays pending and requires separate root complete-key/settings rechecks')
need(schema['$defs']['invocationAttempt']['properties']['argv']['const'][:4] ==
     ['/usr/bin/python3.10','-I','-S','-B'] and
     any(isinstance(n,ast.Attribute) and n.attr == 'no_site' for n in ast.walk(tree)),
     'new invocation explicitly disables site; old recorder remains unchanged')
need(set(schema['$defs']['authorPins']['required']) == set(current_names), 'schema author keys exactly match 32 source names')
def inspect_refs(value):
    if isinstance(value,dict):
        if '$ref' in value:
            target = value['$ref']
            need(target.startswith('#/$defs/') and target[8:] in schema['$defs'], 'local schema reference exists: '+target)
        for child in value.values():
            inspect_refs(child)
    elif isinstance(value,list):
        for child in value:
            inspect_refs(child)
inspect_refs(schema)
functions = {n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)}
need({'pin','read','put','consume','command','inventory','main'} <= set(functions), 'accepted helper structure retained with bounded additions')
main_calls = [n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id == 'main']
guard = tree.body[-1]
need(len(main_calls) == 1 and isinstance(guard,ast.If) and
     ast.unparse(guard.test) == "__name__ == '__main__'" and main_calls[0] in list(ast.walk(guard)),
     'sole main invocation is inside entry guard')
need(not any(isinstance(n,ast.Attribute) and n.attr == 'rglob' for n in ast.walk(tree)), 'no rglob/files-only inventory inherited')
paper_inventories = [ast.unparse(n) for n in ast.walk(tree) if isinstance(n,ast.Call) and
                     isinstance(n.func,ast.Name) and n.func.id == 'inventory' and n.args and
                     isinstance(n.args[0],ast.Name) and n.args[0].id == 'PAPER']
need(set(paper_inventories) == {'inventory(PAPER, NAMES, (ROUND0,))','inventory(PAPER, NAMES, (ROUND0, FROZEN))'},
     'only two exact live-paper prune call sites')
subprocess_calls = [n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and
                    isinstance(n.func.value,ast.Name) and n.func.value.id == 'subprocess' and n.func.attr == 'run']
need(len(subprocess_calls) == 1 and subprocess_calls[0] in list(ast.walk(functions['command'])),
     'only subprocess launch is the disclosed native recorder helper')
need({'cwd','env','stdin','capture_output','timeout'} == {k.arg for k in subprocess_calls[0].keywords},
     'native launch explicitly supplies cwd/env/stdin/raw capture/timeout')
imports = {n.module for n in tree.body if isinstance(n,ast.ImportFrom)} | {a.name for n in tree.body if isinstance(n,ast.Import) for a in n.names}
need(imports == {'hashlib','json','os','pathlib','re','stat','subprocess','sys','time','traceback','urllib.parse'},
     'only literal infrastructure standard-library imports; no submitted science import')

# Additive adapter02 checks inspect syntax and metadata only; no recorder calls.
previous_raw = read(PREVIOUS/'freeze.py')
previous_tree = ast.parse(previous_raw,filename=str(PREVIOUS/'freeze.py'))
previous_schema = json.loads(read(PREVIOUS/'BINDING.schema.json'))
previous_pending = json.loads(read(PREVIOUS/'BINDING_PENDING.json'))
previous_seal = read(PREVIOUS/'SHA256SUMS')
need(sha256(previous_raw).hexdigest() == '50c32a6fa4c703275cb55535bc56507ba5bdbb909fb57ed31ffc6d3ff9566ab2',
     'exact sealed adapter01 source remains the derivation input')
need(sha256(previous_seal).hexdigest() == 'a8b177ff6c92c630b82868d2ac537cbd49f6461b7e1f50b31f328bab09495fb8',
     'exact sealed adapter01 complete manifest is unchanged')
failure_raw = read(PREFLIGHT_FAILURE)
need(sha256(failure_raw).hexdigest() == 'fc09863dc261e90834f03134d2ac953f2d0807af623d29749b4ed6e18e14f575',
     'actual root entry-preflight failure record is immutable')
failure = json.loads(failure_raw)
need(failure['result']['exit_code'] == 1 and failure['result']['chunk_id'] == '0d92db' and
     "entire exact tree before invocation" in failure['result']['output'] and
     "/qa/root_replays/p211_a_initial_01" in failure['result']['output'],
     'root failure was an entry inventory preflight, not a recorder/copy result')
expected_empties = {
    'docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01': ('child01/commands',),
    'docs/papers211_215_sequence/qa/root_replays/p211_a_pair_01': ('child01/commands','child02/commands'),
    'docs/papers211_215_sequence/qa/p211_runtime_preparation': (
        'discovery01/empty_probe_capsule','discovery02/empty_probe_capsule',
        'tests01/existing_cache','tests02/existing_cache',
        'tests02/fixture_initial/child01/commands',
        'tests02/fixture_pair/child01/commands','tests02/fixture_pair/child02/commands'),
}
allowed_empties = ast.literal_eval(assignment(tree,'EXTERNAL_EMPTY_DIRECTORIES'))
need(allowed_empties == expected_empties and sum(map(len,allowed_empties.values())) == 10,
     'exact three literal external roots and ten empty-directory paths')
need(all(len(v) == len(set(v)) and tuple(sorted(v)) == v for v in allowed_empties.values()),
     'every exact allowed list is unique and deterministically ordered')
previous_functions = {n.name:n for n in previous_tree.body if isinstance(n,ast.FunctionDef)}
need(set(functions) == set(previous_functions),'no extra executable recorder function added')
for name in sorted(set(functions)-{'inventory','verify_external_trees','main'}):
    need(ast.dump(functions[name]) == ast.dump(previous_functions[name]),
         'entire accepted function AST unchanged: '+name)
class RestoreSchemaLiteral(ast.NodeTransformer):
    def visit_Constant(self,node):
        if node.value == 'p211_round1_binding_v2':
            return ast.copy_location(ast.Constant(value='p211_round1_binding_v1'),node)
        return node
restored_main = RestoreSchemaLiteral().visit(ast.parse(ast.unparse(functions['main'])).body[0])
need(ast.dump(restored_main) == ast.dump(previous_functions['main']),
     'main differs only in required binding schema literal; native/copy/host logic unchanged')
normal = ast.parse(raw,filename=str(HERE/'freeze.py'))
normal.body = [node for node in normal.body if not (
    isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id == 'EXTERNAL_EMPTY_DIRECTORIES'
                                       for t in node.targets))]
for i,node in enumerate(normal.body):
    if isinstance(node,ast.FunctionDef) and node.name in ('inventory','verify_external_trees'):
        normal.body[i] = previous_functions[node.name]
    elif isinstance(node,ast.FunctionDef) and node.name == 'main':
        normal.body[i] = restored_main
    elif isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id == 'PREPARATION' for t in node.targets):
        normal.body[i] = next(n for n in previous_tree.body if isinstance(n,ast.Assign) and
                              any(isinstance(t,ast.Name) and t.id == 'PREPARATION' for t in n.targets))
need(ast.dump(normal) == ast.dump(previous_tree),
     'whole recorder delta limited to two inventory functions, allowlist, preparation path and schema literal')
need(ast.unparse(assignment(tree,'PREPARATION')) == "QA / 'p211_round1_adapter02'",
     'literal final prepared source now points only to adapter02')
inv = functions['inventory']
need([a.arg for a in inv.args.kwonlyargs] == ['empty_directories'] and
     len(inv.args.kw_defaults) == 1 and isinstance(inv.args.kw_defaults[0],ast.Tuple) and
     not inv.args.kw_defaults[0].elts,'empty-directory support is keyword-only with strict empty-tuple default')
inv_calls = [n for n in ast.walk(tree) if isinstance(n,ast.Call) and
             isinstance(n.func,ast.Name) and n.func.id == 'inventory']
expanded_calls = [n for n in inv_calls if any(k.arg == 'empty_directories' for k in n.keywords)]
need(len(expanded_calls) == 1 and expanded_calls[0] in list(ast.walk(functions['verify_external_trees'])) and
     ast.unparse(expanded_calls[0]) == 'inventory(base, names, empty_directories=empties)',
     'only the exact external-tree verifier passes empty-directory allowances')
need(ast.dump(functions['resolve_links']) == ast.dump(previous_functions['resolve_links']),
     'all external-directory Markdown links retain the old strict inventory call')
inv_assigns = {t.id:n.value for n in ast.walk(inv) if isinstance(n,ast.Assign)
               for t in n.targets if isinstance(t,ast.Name)}
need(ast.unparse(inv_assigns['expected_dirs']) ==
     'parent_names(names) | parent_names(empty_names) | set(empty_names)',
     'expected directory membership contains file ancestors, empty ancestors and the empty nodes themselves')
empty_branches = [n for n in ast.walk(inv) if isinstance(n,ast.If) and ast.unparse(n.test) == 'name in empty_names']
need(len(empty_branches) == 1 and len(empty_branches[0].body) == 2 and
     ast.unparse(empty_branches[0].body[0]) == 'ordinary(p, directory=True)' and
     ast.unparse(empty_branches[0].body[1]).startswith('need(not any(p.iterdir()),'),
     'each declared empty is checked as an ordinary physical no-children directory')
need("'declared_empty_directories': list(empty_names)" in ast.unparse(inv),
     'declared empties are recorded explicitly alongside rich entries, not pruned')
need('set(names) | parent_names(names) | parent_names(empty_names)' in ast.unparse(inv),
     'file collisions, file ancestors and nested empty ancestors are rejected')
need('not prune and base.is_relative_to(ROOT)' in ast.unparse(inv) and
     'EXTERNAL_EMPTY_DIRECTORIES.get(str(base.relative_to(ROOT)), ())' in ast.unparse(inv),
     'inventory itself rechecks literal-root allowance and disallows any prune with empties')
need("all((rows.get(n, {}).get('kind') == 'directory' for n in empty_names))" in ast.unparse(inv),
     'every named empty must appear as a directory row in the complete result')
verify_text = ast.unparse(functions['verify_external_trees'])
need("empties = spec['empty_directories']" in verify_text and
     "isinstance(empties, list) and empties == list(EXTERNAL_EMPTY_DIRECTORIES.get(spec['root'], ()))" in verify_text,
     'binding must provide exact ordered list; unknown roots must explicitly provide empty list')
need('rows[name] = ' in ast.unparse(inv) and
     "'kind': 'directory', 'stat': metadata(s)" in ast.unparse(inv),
     'empty directories retain the full existing rich-stat directory rows')
need(ast.unparse(functions['main']).count("verify_external_trees(binding['external_trees'])") == 2 and
     "need(external_trees_after == external_trees_before," in ast.unparse(functions['main']),
     'same full external directory/emptiness inventory repeats and is compared exactly after copy')
need(schema['$id'] == 'urn:p211:round1:binding:v2' and
     schema['properties']['schema'] == {'const':'p211_round1_binding_v2'} and
     pending['schema'] == 'p211_round1_binding_v2','source/schema/template use the new v2 binding literal')
item = schema['properties']['external_trees']['items']
need(set(item['required']) == set(item['properties']) ==
     {'root','files','empty_directories','manifest','accepted_scope_reference'},
     'every external tree requires exactly the five fields including explicit empties')
need(item['properties']['empty_directories']['type'] == 'array' and
     item['properties']['empty_directories']['items'] == {'$ref':'#/$defs/relativePath'} and
     item['properties']['empty_directories']['uniqueItems'] is True,
     'schema requires unique relative-path arrays, without an inferred default')
clauses = item['allOf']
need(len(clauses) == 4,'three exact-root schema clauses plus one all-other-roots clause')
for clause,(root,values) in zip(clauses[:3],allowed_empties.items()):
    need(clause == {'if':{'properties':{'root':{'const':root}}},
                    'then':{'properties':{'empty_directories':{'const':list(values)}}}},
         'schema exact-list clause agrees with source: '+root)
need(clauses[-1] == {'if':{'properties':{'root':{'not':{'enum':list(allowed_empties)}}}},
                    'then':{'properties':{'empty_directories':{'const':[]}}}},
     'schema requires [] at every unlisted or rebased root')
restored_schema = json.loads(json.dumps(schema))
restored_schema['$id'] = previous_schema['$id']
restored_schema['properties']['schema'] = previous_schema['properties']['schema']
restored_item = restored_schema['properties']['external_trees']['items']
del restored_item['properties']['empty_directories']
restored_item['required'].remove('empty_directories')
del restored_item['allOf']
need(restored_schema == previous_schema,'entire schema delta is only v2 identity and external-tree empty lists')
restored_pending = dict(pending)
restored_pending['schema'] = previous_pending['schema']
need(restored_pending == previous_pending,'pending template changes only v2 identity; no binding or authority filled')
need(32 + 2 + (32 + 50 + 1) + 2 == 119,
     'unchanged native-command formula gives 119 only for root-supplied final A N=50; not an observed run')

print(json.dumps({'status':'STATIC_SOURCE_METADATA_CONSISTENT_NOT_FREEZE_EXECUTION',
                  'checks':len(checks),'check_labels':checks,'inputs':read_keys,
                  'author_names':32,'inherited_read_rows':727,'inherited_external_rows':660,
                  'acceptance_reference_roles':17,'empty_directory_allowlist_roots':3,
                  'empty_directory_allowlist_paths':10,'observed_external_directories':0,
                  'recorder_executions':0,
                  'physical_copies':0,'scientific_executions':0,'builds':0,
                  'schema_validation_scope':'JSON syntax, local ref existence and explicit cross-field metadata; not a full JSON-schema-engine validation',
                  'future_binding_or_freeze_accepted':False},sort_keys=True))
