#!/usr/bin/python3.10
"""Read-only preparation syntax/metadata checks; never import either recorder."""
import ast
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT/'docs/papers211_215_sequence/qa/p211_round1_adapter01'
OLD = ROOT/'docs/papers211_215_sequence/qa/p211_round0_execution01'
UPSTREAM = ROOT/'docs/papers211_215_sequence/qa/p211_round1_preparation'
ALLOWED = {HERE/'freeze.py',HERE/'BINDING.schema.json',HERE/'BINDING_PENDING.json',
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
print(json.dumps({'status':'STATIC_SOURCE_METADATA_CONSISTENT_NOT_FREEZE_EXECUTION',
                  'checks':len(checks),'check_labels':checks,'inputs':read_keys,
                  'author_names':32,'inherited_read_rows':727,'inherited_external_rows':660,
                  'acceptance_reference_roles':17,'recorder_executions':0,
                  'physical_copies':0,'scientific_executions':0,'builds':0,
                  'schema_validation_scope':'JSON syntax, local ref existence and explicit cross-field metadata; not a full JSON-schema-engine validation',
                  'future_binding_or_freeze_accepted':False},sort_keys=True))
