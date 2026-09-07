#!/usr/bin/env python3
"""Parse source only. Does NOT import, compile to bytecode, or execute the checker."""
import ast
from hashlib import sha256
import json
from pathlib import Path
import sys

BASE=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/scout33_root_check_preparation')
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
raw=(BASE/'ROOT_CHECKER.py').read_bytes()
tree=ast.parse(raw,filename='ROOT_CHECKER.py')
imports=[]
for node in ast.walk(tree):
    if isinstance(node,ast.Import):
        imports.extend(alias.name for alias in node.names)
    elif isinstance(node,ast.ImportFrom):
        imports.append(node.module)
assert set(imports)=={'argparse','collections','hashlib','json','os','pathlib','re','stat','struct','subprocess','sys'}
calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call)]
subprocess_calls=[n for n in calls if isinstance(n.func,ast.Attribute)
                  and isinstance(n.func.value,ast.Name) and n.func.value.id=='subprocess'
                  and n.func.attr=='run']
assert len(subprocess_calls)==1
write_names={'write_text','write_bytes','mkdir','unlink','remove','rename','replace','rmdir','touch'}
assert not [n for n in calls if isinstance(n.func,ast.Attribute) and n.func.attr in write_names]
print(json.dumps({'schema':'scout33-preparation-syntax-only-v1',
                  'status':'SYNTAX_AND_STATIC_CALL_CENSUS_ONLY',
                  'checker_sha256':sha256(raw).hexdigest(),'checker_bytes':len(raw),
                  'checker_lines':len(raw.splitlines()),'ast_nodes':sum(1 for _ in ast.walk(tree)),
                  'imports':sorted(imports),'subprocess_run_call_sites':1,
                  'checker_executions':0,'science_executions':0,
                  'boundary':'ast.parse only. Source was not imported or executed. One comparator call site and absence of file-write methods are static observations, not a successful root gate.'},indent=2,sort_keys=True))
