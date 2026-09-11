"""Independent root source/artifact reception; no scientific import or execution.

The optional archive mode makes exclusive physical documentary copies only.
It is not a Round0 freeze, runtime lock, mathematical replay or PDF build.
"""
import ast
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
HERE = ROOT/'docs/papers211_215_sequence/qa/p211_author_source_reception'
SEAL = 'SOURCE_PREPARATION_MANIFEST.json'
EXPECTED_SEAL = '125cc7efed09f400945d80ee8082f1479a8f7a444f2416db7fbefab614edb911'

def pin(raw):
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}

def decode(raw):
    def pairs(items):
        out = {}
        for key, value in items:
            assert key not in out, key
            out[key] = value
        return out
    return json.loads(raw, object_pairs_hook=pairs)

def file_rows(entries):
    out = {}
    for row in entries:
        assert set(row) == {'path', 'sha256', 'bytes'}
        name = row['path']
        p = Path(name)
        assert p.parts and p.as_posix() == name and not p.is_absolute()
        assert '..' not in p.parts and name not in out
        assert re.fullmatch('[0-9a-f]{64}', row['sha256'])
        assert type(row['bytes']) is int and row['bytes'] >= 0
        out[name] = {k: row[k] for k in ('sha256', 'bytes')}
    return out

def main():
    assert sys.argv[1:] in ([], ['--archive'])
    archive = bool(sys.argv[1:])
    seal_raw = (PAPER/SEAL).read_bytes()
    assert sha256(seal_raw).hexdigest() == EXPECTED_SEAL
    seal = decode(seal_raw)
    assert seal['kind'] == 'PRE_ROUND0_SOURCE_PREPARATION_ONLY'
    assert seal['self_excluded'] == SEAL
    assert seal['science_executed'] is seal['build_executed'] is seal['canonical_produced'] is False
    rows = file_rows(seal['files'])
    assert len(rows) == 27 and SEAL not in rows
    entries = list(PAPER.rglob('*'))
    assert not any(p.is_symlink() for p in entries)
    assert {p.relative_to(PAPER).as_posix() for p in entries if p.is_file()} == set(rows) | {SEAL}
    paper_bytes = {name: (PAPER/name).read_bytes() for name in rows}
    assert all(pin(paper_bytes[name]) == expected for name, expected in rows.items())
    assert sum(map(len,paper_bytes.values())) == 166366
    inputs = decode(paper_bytes['SOURCE_INPUT_PINS.json'])
    assert inputs['path_base'] == str(ROOT) and inputs['copied_into_paper'] is False
    originals = file_rows(inputs['files'])
    assert len(originals) == 18
    original_bytes = {name: (ROOT/name).read_bytes() for name in originals}
    assert all(pin(original_bytes[name]) == expected for name, expected in originals.items())
    collected = decode(paper_bytes['SOURCE_PIN_COLLECTION_TOOL_RETURN.json'])
    assert collected['result']['exit_code'] == 0
    assert decode(collected['result']['output']) == inputs
    native = decode(paper_bytes['STATIC_CHECK_TOOL_RETURN.json'])
    assert native['result']['exit_code'] == 0
    old_static = decode(native['result']['output'])
    assert old_static['scientific_code_executed'] is old_static['scientific_module_imported'] is False
    assert old_static['build_executed'] is False

    # Parse mathematical source, never import/exec/evaluate its functions.
    source = paper_bytes['verify.py']
    assert pin(source) == {'bytes':13009,'sha256':'595fbf7c81f52a86192e82b663526ecb9f5abf222f6854859bfee108ff1355f8'}
    tree = ast.parse(source, filename=str(PAPER/'verify.py'))
    imports = [a.name for node in ast.walk(tree) if isinstance(node,ast.Import) for a in node.names]
    assert imports == ['itertools','json','math','sys']
    assert not any(isinstance(node,ast.ImportFrom) for node in ast.walk(tree))
    assert not any(isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and
                   node.func.id in ('exec','eval','compile','__import__') for node in ast.walk(tree))
    assert all(isinstance(node,(ast.Expr,ast.Import,ast.Assign,ast.FunctionDef,ast.If)) for node in tree.body)
    guards = [node for node in tree.body if isinstance(node,ast.If)]
    assert len(guards) == 1 and ast.unparse(guards[0].test) == "__name__ == '__main__'"
    assert len(guards[0].body) == 1 and ast.unparse(guards[0].body[0]) == 'main()'
    assignment = [node for node in tree.body if isinstance(node,ast.Assign)]
    assert len(assignment) == 1 and ast.unparse(assignment[0].targets[0]) == 'EXPECTED_PARAMETERS'
    parameters = decode(paper_bytes['parameters.json'])
    assert ast.literal_eval(assignment[0].value) == parameters
    assert parameters['n_values'] == list(range(1,8)) and parameters['total_states'] == 2353
    assert parameters['carrier_sizes'] == [1,3,10,35,126,462,1716]
    assert len(parameters['predicates']) == 7

    tex_main = paper_bytes['main.tex'].decode()
    tex_inputs = [n+'.tex' for n in re.findall(r'\\input\{([^}]+)\}',tex_main)]
    assert len(tex_inputs) == len(set(tex_inputs)) == 7
    sections = {name for name in rows if name.startswith('sections/')}
    assert len(sections) == 6 and set(tex_inputs) == sections | {'math_commands.tex'}
    tex = '\n'.join(paper_bytes[n].decode() for n in ['main.tex',*tex_inputs])
    labels = re.findall(r'\\label\{([^}]+)\}',tex)
    references = re.findall(r'\\ref\{([^}]+)\}',tex)
    citations = {key.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',tex) for key in group.split(',')}
    bib_keys = re.findall(r'@\w+\{([^,\s]+),',paper_bytes['references.bib'].decode())
    assert len(labels) == len(set(labels)) == 19 and len(references) == 7 and set(references) <= set(labels)
    assert len(bib_keys) == len(set(bib_keys)) == 3 and citations == set(bib_keys)
    assert '\\documentclass[11pt,a4paper]{amsart}' in tex_main
    assert '\\bibliographystyle{amsplain}' in tex_main and '\\bibliography{references}' in tex_main
    assert '\\author{Anonymous}' in tex_main and 'pdfauthor={}' in tex_main
    assert all(marker not in tex for marker in ('TODO','FIXME','[VERIFY]','round211_queue_scout'))
    assert all(not (PAPER/name).exists() for name in ('CANONICAL.json','main.pdf','frozen_round0','frozen_round1','frozen_round2'))
    browser_records = [decode(content) for name,content in paper_bytes.items() if name.startswith('sources/')]
    assert len(browser_records) == 3 and all(isinstance(d['returned_value'],str) for d in browser_records)
    links = []
    for name, content in paper_bytes.items():
        if name.endswith('.md'):
            for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', content.decode()):
                if target.startswith(('http:','https:','mailto:','#')):
                    continue
                path = (PAPER/name).parent/unquote(target.strip('<>').split('#',1)[0])
                assert path.exists(), (name,target)
                links.append({'document':name,'target':str(path.resolve())})
    snapshot = None
    if archive:
        snapshot = HERE/'source_preparation_original'
        assert not snapshot.exists() and not snapshot.is_symlink()
        snapshot.mkdir()
        copied = {**paper_bytes, SEAL:seal_raw}
        for name, content in copied.items():
            dest = snapshot/name
            dest.parent.mkdir(parents=True,exist_ok=True)
            with dest.open('xb') as stream:
                stream.write(content)
            assert dest.read_bytes() == content
        assert {p.relative_to(snapshot).as_posix() for p in snapshot.rglob('*') if p.is_file()} == set(copied)
    assert all((PAPER/name).read_bytes() == content for name,content in paper_bytes.items())
    assert (PAPER/SEAL).read_bytes() == seal_raw
    assert all((ROOT/name).read_bytes() == content for name,content in original_bytes.items())
    result = {'status':'PASS_ROOT_P211_SOURCE_PREPARATION_ONLY','payloads':len(rows),'payload_bytes':166366,
      'source_preparation_manifest':pin(seal_raw),'historical_source_inputs':len(originals),
      'scientific_source':pin(source),'parameters':pin(paper_bytes['parameters.json']),
      'direct_imports':imports,'functions_parsed':sum(isinstance(n,ast.FunctionDef) for n in tree.body),
      'tex_bibliography_source_count':9,'labels':len(labels),'references':len(references),
      'citations':sorted(citations),'local_links':links,'browser_return_archives':3,
      'source_snapshot':str(snapshot) if snapshot else None,'snapshot_files':28 if snapshot else 0,
      'new_scientific_executions':0,'new_builds':0,'round0_freezes':0,
      'scope':'Source/content integrity and static parsing only; mathematical judgments require root original reading and later independent A/B.'}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
