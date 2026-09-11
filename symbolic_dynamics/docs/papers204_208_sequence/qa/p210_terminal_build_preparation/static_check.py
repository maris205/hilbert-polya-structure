#!/usr/bin/env python3
"""AST/data-only preparation check; never import or invoke the builder."""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers204_208_sequence/qa/p210_terminal_build_preparation'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
BASE = ROOT / 'docs/papers204_208_sequence/qa/batch_terminal_build_preparation/build_four.py'
INPUTS, CHECKS = {}, []


def raw(path):
    p = Path(path)
    assert p.is_file() and not p.is_symlink(), str(p)
    value = p.read_bytes()
    key = {'sha256': sha256(value).hexdigest(), 'bytes': len(value)}
    assert str(p) not in INPUTS or INPUTS[str(p)] == key, str(p)
    INPUTS[str(p)] = key
    return value


def ck(condition, label):
    assert condition, label
    CHECKS.append(label)


def main():
    ck(sys.argv[1:] == ['ast-data-only'], 'explicit AST/data-only invocation')
    ck(sys.dont_write_bytecode and sys.flags.isolated and sys.flags.no_site,
       'isolated no-site no-bytecode static interpreter')
    script = PREP / 'build_p210.py'
    source, base = raw(script), raw(BASE)
    tree, parent = ast.parse(source), ast.parse(base)
    own = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    old = {n.name: n for n in ast.walk(parent) if isinstance(n, ast.FunctionDef)}
    names = ('require', 'pin', 'save', 'save_ledger', 'manifest', 'entry',
             'inventory', 'coverage', 'observed', 'command', 'libraries')
    copied = {}
    for name in names:
        ck(ast.dump(own[name], include_attributes=False) == ast.dump(old[name], include_attributes=False),
           'exact accepted infrastructure function AST: ' + name)
        selected = ast.get_source_segment(source.decode(), own[name]).encode()
        copied[name] = {'sha256': sha256(selected).hexdigest(), 'bytes': len(selected)}
    stub = own['final_schema_binding']
    ck(len(stub.body) == 3 and isinstance(stub.body[0], ast.Expr) and
       isinstance(stub.body[1], ast.Expr) and isinstance(stub.body[-1], ast.Raise),
       'final schema binding is unconditional hard failure, not an acceptance boolean')
    ck(not any(isinstance(n, ast.Return) for n in ast.walk(stub)), 'unbound function has no return branch')
    originals = own['originals']
    ck(isinstance(originals.body[1], ast.Assign) and isinstance(originals.body[1].value, ast.Call) and
       isinstance(originals.body[1].value.func, ast.Name) and originals.body[1].value.func.id == 'final_schema_binding',
       'originals invokes hard gate immediately after preparation manifest read')
    body = own['main'].body
    original_calls = [n.lineno for n in body if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call)
                      and isinstance(n.value.func, ast.Name) and n.value.func.id == 'originals']
    output_mkdir = [n.lineno for n in body if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
                    and isinstance(n.value.func, ast.Attribute) and n.value.func.attr == 'mkdir'
                    and isinstance(n.value.func.value, ast.Name) and n.value.func.value.id == 'out']
    ck(len(original_calls) == len(output_mkdir) == 1 and original_calls[0] < output_mkdir[0],
       'hard gate precedes output mkdir and later host/native work')
    ck(not any(isinstance(n, (ast.Import, ast.ImportFrom)) and
               any('build_four' in a.name or 'root_launch' in a.name for a in n.names)
               for n in ast.walk(tree)), 'no old program imported')
    ck(not (PAPER / 'qa_final').exists() and not (PAPER / 'qa_final').is_symlink(),
       'qa_final physically absent during preparation')
    assignments = {target.id: n.value for n in tree.body if isinstance(n, ast.Assign)
                   for target in n.targets if isinstance(target, ast.Name)}
    source_names = ast.literal_eval(assignments['SOURCE_NAMES'])
    env = ast.literal_eval(assignments['ENV'])
    ck(len(source_names) == 10 and all(Path(n).suffix in ('.tex', '.bib') for n in source_names),
       'ten named source files only; no PDF or auxiliary input')
    ck(env == {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC',
               'SOURCE_DATE_EPOCH': '1704067200', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'},
       'exact prior P210 C-locale reproducibility environment, no system-variable repurposing')
    contract = json.loads(raw(PREP / 'INPUT_CONTRACT.json'))
    ck(contract['stage'] == 'PRELIMINARY_UNBOUND_NO_EXECUTION' and contract['final_schema_binding'] is None,
       'contract is explicitly unbound; no future verdict or hash supplied')
    for path, expected in contract['infrastructure_pins'].items():
        value = raw(path)
        ck({'sha256': sha256(value).hexdigest(), 'bytes': len(value)} == expected,
           'actual read infrastructure pin: ' + path)
    historical = contract['historical_round1_source_baseline']
    ck(tuple(historical['source_names']) == source_names, 'current historical source names match prepared names')
    for base in (PAPER, PAPER / 'frozen_round1'):
        for name, wanted in {**historical['source_pins'], 'main.pdf': historical['pdf_pin']}.items():
            value = raw(base / name)
            ck({'sha256': sha256(value).hexdigest(), 'bytes': len(value)} == wanted,
               'current historical source/PDF equality only: ' + str(base / name))
    main_tex = raw(PAPER / 'main.tex').decode()
    actual_inputs = {n if n.endswith('.tex') else n + '.tex' for n in re.findall(r'\\input\{([^}]+)\}', main_tex)}
    ck(actual_inputs == set(source_names) - {'main.tex', 'references.bib'}, 'actual main input graph and no orphan sections')
    section_names = {p.relative_to(PAPER).as_posix() for p in (PAPER / 'sections').rglob('*') if p.is_file()}
    ck(section_names == {n for n in source_names if n.startswith('sections/')}, 'actual section directory exact census')
    # Pure regex fixtures, not a PDF command, prove the empty Author line
    # cannot absorb the following metadata field.
    pattern = r'^Author:[ \t]*([^\r\n]*)$'
    ck(re.search(pattern, 'Author:          \nCreator: LaTeX\n', re.M).group(1).strip() == '',
       'anonymous metadata regex cannot consume following line')
    ck(re.search(pattern, 'Author: Named Person\nCreator: LaTeX\n', re.M).group(1).strip() == 'Named Person',
       'anonymous metadata regex exposes nonempty author')
    command_labels = ['source_cmp', 'ldd_before', 'pdflatex_version', 'bibtex_version', 'texmf_roots', 'P210_round2_pdfinfo']
    suffixes = ['TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR', 'pass1', 'bst', 'bibtex', 'pass2', 'pass3',
                'pdfinfo', 'pdffonts', 'pdftotext', 'frozen_cmp']
    for number in (1, 2):
        stem = 'P210_cold_build_' + str(number)
        command_labels.extend(stem + '_' + suffix for suffix in suffixes)
        if number == 1:
            command_labels.append(stem + '_render')
    command_labels += ['P210_pair_cmp', 'ldd_after']
    ck(len(command_labels) == len(set(command_labels)) == 33, 'prospective 33-command ordered census')
    text = source.decode()
    for token in ('streams_settled', 'UNCLOSED_NO_SEAL', 'SIGKILL_OWNED_PROCESS_GROUP',
                  'timeout=600', 'timeout=10', "'P210_round2_pdfinfo'", "'P210_pair_cmp'",
                  "'reference_heading_pages'", "'final_schema_binding'", "'NOT_VIEWED'",
                  "'new_mathematical_executions': 0"):
        # The pair comparison label is built dynamically in the source.
        if token == "'P210_pair_cmp'":
            ck("ident + '_pair_cmp'" in text, 'native pair comparison is present')
        else:
            ck(token in text, 'prepared mechanism present: ' + token)
    for path, expected in dict(INPUTS).items():
        value = Path(path).read_bytes()
        ck({'sha256': sha256(value).hexdigest(), 'bytes': len(value)} == expected,
           'final static input reread: ' + path)
    return {'schema': 'p210-terminal-build-preparation-static-v1',
        'status': 'STATIC_PREPARATION_OK_UNBOUND_NOT_EXECUTED', 'checked_utc': datetime.now(timezone.utc).isoformat(),
        'checks': len(CHECKS), 'check_labels': CHECKS, 'exact_reused_functions': copied,
        'source_key': INPUTS[str(script)], 'input_keys': INPUTS,
        'prospective_command_count': 33, 'prospective_command_labels': command_labels,
        'builder_executions': 0, 'old_program_executions': 0, 'scientific_runs': 0,
        'native_build_pdfinfo_font_render_cmp_calls': 0, 'host_resource_inventories': 0,
        'page_views': 0, 'qa_final_created': False, 'root_launch_authorized_by_this_report': False,
        'required_next_step': 'Actual accepted B/root strict pair+delta/physical Round2, then new sealed schema-bound revision and root full-source inspection',
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, ensure_ascii=False, indent=2))
