"""Final preparation document/source syntax inspection only; no target imports."""
import importlib.util
from pathlib import Path

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation'
spec=importlib.util.spec_from_file_location('owned_preparation_recorder',BASE/'prepare_inputs.py')
rec=importlib.util.module_from_spec(spec);spec.loader.exec_module(rec)
PROGRAM=r'''import ast,hashlib,json,re
from pathlib import Path
B=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation')
contract=json.loads((B/'INPUT_CONTRACT.json').read_bytes())
assert contract['status']=='PREPARED_ONLY_NOT_EXECUTED_OR_ACCEPTED'
code={}
for p in sorted(B.rglob('*.py')):
 text=p.read_text();compile(ast.parse(text),str(p),'exec');code[str(p.relative_to(B))]=hashlib.sha256(p.read_bytes()).hexdigest()
readme=(B/'README.md').read_text();links=[]
readme=re.sub(r'(?ms)^```.*?^```\s*$', '', readme)
for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',readme):
 assert (B/target).exists(),target;links.append(target)
final=json.loads((B/'FINAL_STATIC_CHECK_v2.json').read_bytes())
for name in ('audit_p209.py','record_audit.py','lifecycle_audit.py'):
 assert code[name]==final['syntax'][name]['sha256']
previous=json.loads((B/'checks/final_static/INPUTS_BEFORE.json').read_bytes())
for name in ('audit_p209.py','lifecycle_audit.py','p209_specific.py.fragment'):
 assert hashlib.sha256((B/'draft_history/unexecuted_02'/name).read_bytes()).hexdigest()==previous[str(B/name)]['sha256']
print(json.dumps({'status':'PASS_PREPARATION_DOCUMENTS_AND_ALL_SOURCE_SYNTAX_ONLY',
 'contract_schema':contract['schema'],'python_sources':code,'readme_local_links':links,
 'final_target_source_pins_unchanged':True,'exact_unexecuted_draft02_bytes_retained':True,
 'auditor_build_view_executions':0},indent=2,sort_keys=True))
'''

if __name__=='__main__':
    files=sorted(p for p in BASE.rglob('*.py'))+[BASE/'README.md',BASE/'INPUT_CONTRACT.json',
          BASE/'FINAL_STATIC_CHECK_v2.json',BASE/'checks/final_static/INPUTS_BEFORE.json',
          BASE/'draft_history/unexecuted_02/p209_specific.py.fragment']
    row,raw=rec.command('final_documents',['/usr/bin/python3.10','-I','-S','-B','-c',PROGRAM],files,0)
    import json
    rec.save(BASE/'FINAL_DOCUMENT_CHECK.json',json.loads(raw))
    print(raw.decode())
