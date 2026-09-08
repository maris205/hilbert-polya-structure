"""Root narrow Git-only control delta and unchanged prior documentary keys."""
from pathlib import Path
import ast
import difflib
import hashlib
import json
import os
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
BATCH = QA.parent
OLD = QA / 'p210_round1_central_update_check/inputs'
OUT = QA / 'p210_checkpoint_index_delta_root'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert Path.cwd() == ROOT and dict(os.environ) == ENV and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
assert not OUT.exists() and not Path(sys.pycache_prefix).exists()
reads = {}
def read(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    raw = path.read_bytes()
    key = {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
    assert str(path) not in reads or reads[str(path)] == key, str(path)
    reads[str(path)] = key
    return raw

def stripped_links(content):
    content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
    content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
    content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)

def write(path, value):
    with path.open('x') as stream:
        json.dump(value, stream, sort_keys=True, ensure_ascii=False, indent=2)
        stream.write('\n')

prior_raw = read(QA / 'p210_round1_central_update_root/stdout.raw')
assert hashlib.sha256(prior_raw).hexdigest() == '463ff779316fee32df00ca870674dcf3ae8e1f2a0496f518e33465bfe7f6721b'
prior = json.loads(prior_raw)
assert prior['status'] == 'DOCUMENTARY_SCOPE_CLOSED_NOT_TERMINAL_PASS' and not prior['failures']
controls = {'SYMBOLIC_DYNAMICS_STATE.md': ROOT / 'SYMBOLIC_DYNAMICS_STATE.md',
    **{name: BATCH / name for name in ('PIPELINE_STATE.md', 'GIT_SYNC_RECEIPT.md', 'FINAL_THEOREM_CONTRACTS.md')}}
changed = {str(controls[name]) for name in controls if name != 'FINAL_THEOREM_CONTRACTS.md'}
for name, pin in prior['input_keys'].items():
    if name not in changed:
        assert hashlib.sha256(read(Path(name))).hexdigest() == pin['sha256'], name
old = {name: read(OLD / name).decode() for name in controls}
new = {name: read(path).decode() for name, path in controls.items()}
assert new['FINAL_THEOREM_CONTRACTS.md'] == old['FINAL_THEOREM_CONTRACTS.md']
o, n = old['PIPELINE_STATE.md'], new['PIPELINE_STATE.md']
op, osuffix = o.split('Private checkpoint1f028072', 1)
np, nsuffix = n.split('The corrected private checkpoint', 1)
end = '\nPrevious milestone:'
assert op == np and osuffix.split(end, 1)[1] == nsuffix.split(end, 1)[1]
o, n = old['GIT_SYNC_RECEIPT.md'], new['GIT_SYNC_RECEIPT.md']
original_heading = '## Current local milestone and actual rejected checkpoint\n'
historical_heading = '## Previous local milestone and actual rejected checkpoint — historical\n'
prefix, body = o.split(original_heading, 1)
assert n.startswith(prefix + '## Latest confirmed: captured P210 Round0 scope, corrected private checkpoint\n')
assert n.split(historical_heading, 1)[1] == body
o, n = old['SYMBOLIC_DYNAMICS_STATE.md'], new['SYMBOLIC_DYNAMICS_STATE.md']
for a, b in (('- 新本地检查点 ', '- 最新限定私有检查点 '), ('- 最新确认私有推送为 ', '- 前次私有推送 `a380d247')):
    left = next(line for line in o.splitlines(True) if line.startswith(a))
    right = next(line for line in n.splitlines(True) if line.startswith(b))
    n = n.replace(right, left, 1)
added = next(line for line in n.splitlines(True) if line.startswith('本次隔离同步使用 '))
n = n.replace(added + '\n', '', 1)
assert n == o, 'STATE changed outside two Git bullets and exact repository-role paragraph'
for name in ('SYMBOLIC_DYNAMICS_STATE.md', 'PIPELINE_STATE.md', 'GIT_SYNC_RECEIPT.md'):
    assert '36e7b365b35f454d6fa94d6674746eafde314872' in new[name]
    assert 'HOLD_EXTERNAL' in new[name]
parser = read(QA / 'p209_terminal_artifact_revision_04/audit_p209.py')
ours = read(Path(__file__))
def ast_function(raw):
    return next(node for node in ast.parse(raw).body if isinstance(node, ast.FunctionDef) and node.name == 'stripped_links')
assert ast.dump(ast_function(parser), include_attributes=False) == ast.dump(ast_function(ours), include_attributes=False)
documents = list(controls.values()) + [QA / 'P210_CHECKPOINT_ROOT_INSPECTION.md', QA / 'P210_ROUND1_CENTRAL_ROOT_INSPECTION.md']
links = []
for document in documents:
    for href in stripped_links(read(document).decode()):
        target = href.strip().strip('<>').split('#', 1)[0]
        if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
            continue
        path = (document.parent / target).resolve()
        assert path.exists(), (str(document), href)
        if path.is_file(): read(path)
        else: assert path.is_dir()
        links.append({'document': str(document), 'href': href, 'target': str(path)})
for path, pin in list(reads.items()):
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == pin['sha256'], path
OUT.mkdir()
for name in controls:
    with (OUT / name).open('xb') as stream: stream.write(new[name].encode())
result = {'status': 'PASS_ROOT_EXACT_GIT_ONLY_INDEX_DELTA', 'actual_ref': '36e7b365b35f454d6fa94d6674746eafde314872',
    'prior_input_keys': len(prior['input_keys']), 'exact_changed_prior_paths': sorted(changed),
    'all_other_prior_keys_unchanged': True, 'full_contract_unchanged': True, 'current_reread_paths': len(reads),
    'links': links, 'input_keys': reads, 'new_science_build_view_review_git_execution': False,
    'diffs': {name: ''.join(difflib.unified_diff(old[name].splitlines(True), new[name].splitlines(True), fromfile='old/' + name, tofile='current/' + name)) for name in controls},
    'scope': 'Two Git-status bullets and one repository paragraph in STATE; one exact private-checkpoint paragraph in PIPE; one prepended successful receipt and historical heading in GIT; entire FINAL unchanged. No historical receipt rewritten.',
    'external': 'HOLD_EXTERNAL'}
write(OUT / 'RESULT.actual.json', result)
with (OUT / 'SHA256SUMS').open('x') as stream:
    for path in sorted(p for p in OUT.iterdir() if p.is_file() and p.name != 'SHA256SUMS'):
        stream.write(hashlib.sha256(path.read_bytes()).hexdigest() + '  ' + path.name + '\n')
print(json.dumps({k: v for k, v in result.items() if k not in {'links', 'input_keys', 'diffs'}}, sort_keys=True))
