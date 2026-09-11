#!/usr/bin/python3.10
"""Forward-only receiver02 for exact adapter02; source preparation only.

Derived from sealed receiver01 (see PLAN.md and DERIVATION.diff). Stdout only;
no submitted-code import, science, A adjudication or complete-host acceptance.
"""
import argparse
import ast
from hashlib import sha256
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
EXEC = QA/'p211_round1_execution01'
PREP = QA/'p211_round1_adapter02'
ROLE = QA/'p211_round1_preparation'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
R0, R1 = PAPER/'frozen_round0', PAPER/'frozen_round1'
A = ROOT/'docs/papers211_215_sequence/reviews/p211_a'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
TOOLS = {'/usr/bin/cp','/usr/bin/cmp','/usr/bin/sha256sum','/usr/bin/python3.10'}
SOURCE_HASH = '0b43b429aa7381d138e81d5c849b0c9925c5f94107f044c94419150c3b059b1a'
SCHEMA_HASH = 'ceb305ffd8bb5a03016e2d74cf230b7242c7b19aac9d0aea58b9b6f7ccfc05ce'
LEDGER_HASH = '3a0257d637b721607339dc623aa2890bb24f86ed003e8dc1d0e40194cedfde5f'
R0_MANIFEST = {'bytes':2799,'sha256':'459459486a82c8f787d04e5e7fcb81e6c01b3abef320d1e82ea4cbb30ea8a8bd'}
NAMES = '''AUTHOR_EXECUTION_RECEIPT.md CANONICAL.json CANONICAL_SCHEMA.md CLAIMS_EVIDENCE.md HANDOFF.md INITIAL_BUILD_RECEIPT.md NARRATIVE_REPORT.md PAPER_PLAN.md PARAMETER_SPECIFICATION.md PREPARATION_PLAN.md PROOF_PACKAGE.md README.md SOURCE_AUDIT.md SOURCE_INPUT_PINS.json SOURCE_PIN_COLLECTION_TOOL_RETURN.json SOURCE_PREPARATION_MANIFEST.json STATIC_CHECK_TOOL_RETURN.json main.pdf main.tex math_commands.tex parameters.json references.bib sections/0_abstract.tex sections/1_introduction.tex sections/2_image.tex sections/3_clock.tex sections/4_inverse.tex sections/5_scope.tex sources/bibliographic_metadata_web.json sources/stein_definition_web.json sources/stein_support_web.json verify.py'''.split()
TOP = set('''freeze.py BINDING.json ROOT_INVOCATION_ATTEMPT.json PROCESS_CONTEXT.json EXECUTED_FREEZE_SOURCE.py BINDING_PIN.json EXTERNAL_INPUTS_BEFORE.json HOST_REUSE_BOUNDARY.json NATIVE_TOOLS_BEFORE.json SOURCE_INPUTS_BEFORE.json SOURCE_TREES_BEFORE.json EXTERNAL_TREES_BEFORE.json SOURCE_SELECTION.json DECLARED_PIN_LIST_BASES.json DECLARED_JSON_PIN_BASES.json INHERITED_ROUND0_RESOLUTIONS.json MARKDOWN_LINK_MAP.json SOURCE_INPUTS_AFTER.json SOURCE_TREES_AFTER.json EXTERNAL_INPUTS_AFTER.json EXTERNAL_TREES_AFTER.json NATIVE_TOOLS_AFTER.json FROZEN_ORIGIN_MAP.json FROZEN_TREE.json EXTERNAL_REFERENCES.json READ_INPUTS_BEFORE.json READ_INPUTS_AFTER.json NATIVE_COMMANDS.json RESULT.json ROOT_INVOCATION_NATIVE.json root.stdout.raw root.stderr.raw SHA256SUMS'''.split())
EXTERNAL_EMPTY_DIRECTORIES = {
    'docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01': (
        'child01/commands',
    ),
    'docs/papers211_215_sequence/qa/root_replays/p211_a_pair_01': (
        'child01/commands',
        'child02/commands',
    ),
    'docs/papers211_215_sequence/qa/p211_runtime_preparation': (
        'discovery01/empty_probe_capsule',
        'discovery02/empty_probe_capsule',
        'tests01/existing_cache',
        'tests02/existing_cache',
        'tests02/fixture_initial/child01/commands',
        'tests02/fixture_pair/child01/commands',
        'tests02/fixture_pair/child02/commands',
    ),
}
reads, trees = {}, {}
checks = 0


def need(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def bytepin(key):
    return {k:key[k] for k in ('bytes','sha256')}


def metadata(s):
    return {k:getattr(s,'st_'+v) for k,v in (
        ('mode','mode'),('device','dev'),('inode','ino'),('uid','uid'),('gid','gid'),
        ('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns'))}


def relative(name):
    need(isinstance(name,str) and name and '\\' not in name and
         not any(c in name for c in '\x00\r\n\t') and
         not PurePosixPath(name).is_absolute() and
         all(p not in ('','..','.') for p in name.split('/')),('normalized path',name))
    return name


def workspace(name):
    return ROOT/relative(name)


def ordinary(path, directory=False):
    p = Path(path)
    need(p.is_absolute() and (p.is_relative_to(ROOT) or str(p) in TOOLS),('scoped path',str(p)))
    s = p.lstat()
    need(p.resolve() == p and (stat.S_ISDIR(s.st_mode) if directory else stat.S_ISREG(s.st_mode)),
         ('ordinary physical path including parents',str(p)))
    return s


def fresh(path):
    p = Path(path)
    before = metadata(ordinary(p))
    raw = p.read_bytes()
    after = metadata(ordinary(p))
    need(before == after and len(raw) == after['size'],('rich read stability',str(p)))
    return raw,{**pin(raw),'stat':after}


def read(path):
    raw,key = fresh(path)
    name = str(path)
    need(name not in reads or reads[name] == key,('repeated rich read equality',name))
    reads[name] = key
    return raw


def obj(path):
    return json.loads(read(path))


def pinned(path, expected):
    raw = read(path)
    need(pin(raw) == expected,('exact pin',str(path)))
    return raw


def inventory(base, names, prune=(), remember=True, *, empty_directories=()):
    ordinary(base,True)
    need(type(empty_directories) in (list,tuple),'explicit empty-directory sequence')
    empties = tuple(relative(n) for n in empty_directories)
    need(len(empties)==len(set(empties)),'unique declared empty directories')
    need(not empties or (not prune and empties==EXTERNAL_EMPTY_DIRECTORIES.get(str(base.relative_to(ROOT)),())),
         ('only exact per-root external empty-directory allowance, never a prune',str(base)))
    directories = {'.'}
    for name in names:
        directories.update(str(p) for p in PurePosixPath(relative(name)).parents)
    empty_parents = {'.'}
    for name in empties:
        empty_parents.update(str(p) for p in PurePosixPath(name).parents)
    need(not set(empties)&(set(names)|directories|empty_parents),
         'declared empties are not payloads, payload ancestors or nested empty ancestors')
    directories.update(empty_parents|set(empties))
    rows = {'.':{'kind':'directory','stat':metadata(base.lstat())}}
    omitted = {}
    def walk(directory):
        for p in sorted(directory.iterdir()):
            name = relative(str(p.relative_to(base)))
            s = p.lstat()
            if name in prune:
                ordinary(p,True)
                omitted[name] = {'kind':'directory','stat':metadata(s)}
            elif stat.S_ISDIR(s.st_mode):
                ordinary(p,True)
                rows[name] = {'kind':'directory','stat':metadata(s)}
                if name in empties:
                    need(not any(p.iterdir()),('declared ordinary directory actually empty',str(p)))
                walk(p)
            else:
                ordinary(p)
                rows[name] = {'kind':'file','stat':metadata(s)}
    walk(base)
    need(all(rows.get(n,{}).get('kind')=='directory' for n in empties),'every declared empty directory is inventoried')
    need({n for n,r in rows.items() if r['kind']=='file'} == set(names) and
         {n for n,r in rows.items() if r['kind']=='directory'} == directories and
         set(omitted) == set(prune),('exact complete tree',str(base)))
    result = {'entries':rows,'pruned_exact_subtrees':omitted,'declared_empty_directories':list(empties)}
    if remember:
        key = (str(base),tuple(sorted(names)),tuple(sorted(prune)),empties)
        need(key not in trees or trees[key] == result,('tree drift',str(base)))
        trees[key] = result
    return result


def sums(raw, nonself=True):
    need(raw.endswith(b'\n'),'manifest newline')
    rows = {}
    for line in raw.decode('utf-8').splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None,('manifest syntax',line))
        digest,name = m.groups()
        relative(name)
        need(name not in rows and (not nonself or name != 'SHA256SUMS'),('manifest membership',name))
        rows[name] = digest
    need(bool(rows),'nonempty manifest')
    return rows


def seal(base, expected=None, *, empty_directories=()):
    rows = sums(read(base/'SHA256SUMS'))
    if expected is not None:
        need(rows == {n:v['sha256'] for n,v in expected.items()},('bound manifest',str(base)))
    inventory(base,set(rows)|{'SHA256SUMS'},empty_directories=empty_directories)
    for name,digest in rows.items():
        need(pin(read(base/name))['sha256'] == digest,('manifest full payload hash',str(base/name)))
    return rows


def schema_ok(value, schema, whole):
    """Only the finite keywords in the pinned binding schema; no external engine."""
    if '$ref' in schema:
        target = whole
        for part in schema['$ref'].removeprefix('#/').split('/'):
            target = target[part]
        return schema_ok(value,target,whole)
    if 'const' in schema and (value != schema['const'] or type(value) is not type(schema['const'])):
        return False
    if 'enum' in schema and value not in schema['enum']:
        return False
    if 'not' in schema and schema_ok(value,schema['not'],whole):
        return False
    if 'allOf' in schema and not all(schema_ok(value,s,whole) for s in schema['allOf']):
        return False
    if 'if' in schema:
        branch = 'then' if schema_ok(value,schema['if'],whole) else 'else'
        if branch in schema and not schema_ok(value,schema[branch],whole):
            return False
    for keyword,exact in [('anyOf',False),('oneOf',True)]:
        if keyword in schema:
            count = sum(schema_ok(value,s,whole) for s in schema[keyword])
            if (count != 1 if exact else count == 0):
                return False
    kind = schema.get('type')
    types = {'object':dict,'array':list,'string':str,'integer':int,'number':(int,float),'null':type(None)}
    if kind and (not isinstance(value,types[kind]) or kind in ('integer','number') and type(value) is bool):
        return False
    if isinstance(value,dict):
        if not set(schema.get('required',[])) <= set(value) or len(value) < schema.get('minProperties',0):
            return False
        for key,item in value.items():
            if 'propertyNames' in schema and not schema_ok(key,schema['propertyNames'],whole):
                return False
            rule = schema.get('properties',{}).get(key,schema.get('additionalProperties',True))
            if rule is False or isinstance(rule,dict) and not schema_ok(item,rule,whole):
                return False
    if isinstance(value,list):
        if len(value) < schema.get('minItems',0) or schema.get('uniqueItems') and len({json.dumps(v,sort_keys=True) for v in value}) != len(value):
            return False
        if 'items' in schema and not all(schema_ok(v,schema['items'],whole) for v in value):
            return False
    if isinstance(value,str) and (len(value) < schema.get('minLength',0) or 'pattern' in schema and re.search(schema['pattern'],value) is None):
        return False
    return not ('minimum' in schema and value < schema['minimum'])


def audit(args):
    need(Path.cwd() == ROOT,'literal workspace cwd')
    read(Path(__file__).absolute())
    code = read(PREP/'freeze.py')
    need(pin(code)['sha256'] == SOURCE_HASH,'pinned sealed recorder source')
    need(read(EXEC/'freeze.py') == code == read(EXEC/'EXECUTED_FREEZE_SOURCE.py'),'prepared/placed/executed full source equality')
    schema_raw = read(PREP/'BINDING.schema.json')
    need(pin(schema_raw)['sha256'] == SCHEMA_HASH,'pinned exact binding schema')
    schema = json.loads(schema_raw)
    binding = obj(EXEC/'BINDING.json')
    need(schema_ok(binding,schema,schema),'entire enabled binding finite schema')
    binding_pin,source_pin = pin(read(EXEC/'BINDING.json')),pin(code)
    need(binding['execution_source_pin'] == source_pin and obj(EXEC/'BINDING_PIN.json') == binding_pin,'binding/source pin cross-bind')
    selected = next(n.value for n in ast.parse(code).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='NAMES' for t in n.targets))
    need(isinstance(selected,ast.Call) and isinstance(selected.func,ast.Attribute) and selected.func.attr=='split' and not selected.args and not selected.keywords and ast.literal_eval(selected.func.value).split()==NAMES,'literal independent author32 AST; never import')
    declared = next(n.value for n in ast.parse(code).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXTERNAL_EMPTY_DIRECTORIES' for t in n.targets))
    need(ast.literal_eval(declared)==EXTERNAL_EMPTY_DIRECTORIES and len(EXTERNAL_EMPTY_DIRECTORIES)==3 and sum(map(len,EXTERNAL_EMPTY_DIRECTORIES.values()))==10,
         'exact three-root ten-directory independent literal allowlist, AST only')
    result = obj(EXEC/'RESULT.json')
    ledger_path = QA/'p211_round0_execution01/SOURCE_INPUTS_AFTER.json'
    ledger_raw = read(ledger_path)
    need(pin(ledger_raw)['sha256']==LEDGER_HASH,'accepted author ledger')
    author = json.loads(ledger_raw)
    need(set(author)==set(NAMES) and len(author)==32 and binding['author_delta_before']==author==binding['author_delta_after'],'accepted unchanged author32')
    draft = obj(ROLE/'ROLE_SELECTION_DRAFT.json')
    need({r['relative_name']:r['pin'] for r in draft['author_role']['payloads']} == author,'complete sealed role draft')
    a = binding['a_package']
    need(len(a['payloads'])==a['payload_count']==50 and a['all_file_count']==51,'this final A50/51, not dynamic substitute')
    a_all = {**a['payloads'],'SHA256SUMS':a['manifest_pin']}
    old = {**author,'SHA256SUMS':R0_MANIFEST}
    selection = {n:{'role':'author','source':str((R0/n).relative_to(ROOT)),'original_document':str((PAPER/n).relative_to(ROOT)),'pin':v,'destination':str((R1/n).relative_to(ROOT))} for n,v in author.items()}
    selection.update({'review_a/'+n:{'role':'review_a','source':str((A/n).relative_to(ROOT)),'original_document':str((A/n).relative_to(ROOT)),'pin':v,'destination':str((R1/'review_a'/n).relative_to(ROOT))} for n,v in a_all.items()})
    for n,spec in binding['document_origins'].items():
        need(n in selection,('origin selected document',n))
        if selection[n]['role']=='author':
            need(spec['original_document']==str((PAPER/n).relative_to(ROOT)),('unchanged author document base',n))
        selection[n]['original_document'] = spec['original_document']
    need(len(selection)==83 and obj(EXEC/'SOURCE_SELECTION.json')==selection,'exact 83-payload source/origin/destination map')
    expected = {n:r['pin'] for n,r in selection.items()}
    inner = seal(A,a['payloads'])
    seal(R0,author)
    seal(R1,expected)
    need(pinned(A/'SHA256SUMS',a['manifest_pin'])==read(R1/'review_a/SHA256SUMS'),'unchanged copied inner manifest')
    need(pin(read(R0/'SHA256SUMS'))==R0_MANIFEST,'immutable Round0 manifest')
    manifest = ''.join(expected[n]['sha256']+'  '+n+'\n' for n in sorted(expected)).encode()
    need(read(R1/'SHA256SUMS')==manifest and result['manifest']==pin(manifest),'exact new outer manifest bytes')
    source_before,source_after = obj(EXEC/'SOURCE_INPUTS_BEFORE.json'),obj(EXEC/'SOURCE_INPUTS_AFTER.json')
    need(source_before==source_after and set(source_before)=={'author_live','author_round0','review_a'},'whole rich source before/after equality')
    for role,base,pins in [('author_live',PAPER,author),('author_round0',R0,old),('review_a',A,a_all)]:
        need(set(source_after[role])==set(pins),('full source key membership',role))
        for n,v in pins.items():
            pinned(base/n,v)
            need(source_after[role][n]==reads[str(base/n)],('current rich source key',role,n))
    for n in NAMES:
        need(read(PAPER/n)==read(R0/n),('full current live/Round0 bytes',n))
    origins = []
    inodes = set()
    for n,row in sorted(selection.items()):
        src,dst = workspace(row['source']),R1/n
        need(read(src)==read(dst),('full source/copied bytes',n))
        sk,dk = reads[str(src)],reads[str(dst)]
        inode = (dk['stat']['device'],dk['stat']['inode'])
        need(inode != (sk['stat']['device'],sk['stat']['inode']) and inode not in inodes and dk['stat']['nlink']==1,('distinct ordinary non-hardlinked payload',n))
        inodes.add(inode)
        origins.append({'relative_name':n,'role':row['role'],'original_path':row['source'],'frozen_path':row['destination'],'pin':row['pin'],'source_key':sk,'frozen_key':dk})
    need(obj(EXEC/'FROZEN_ORIGIN_MAP.json')==origins,'entire exact83 rich origin rows')
    outer_inode = metadata(ordinary(R1/'SHA256SUMS'))
    need(outer_inode['nlink']==1 and (outer_inode['device'],outer_inode['inode']) not in inodes,'ordinary separate outer manifest')
    frozen_tree = inventory(R1,set(expected)|{'SHA256SUMS'})
    need(obj(EXEC/'FROZEN_TREE.json')==frozen_tree,'complete84 frozen rich tree')
    tb,ta = obj(EXEC/'SOURCE_TREES_BEFORE.json'),obj(EXEC/'SOURCE_TREES_AFTER.json')
    need(set(tb)==set(ta)=={'author_live','author_round0','review_a'},'whole source tree role set')
    for role,base,names in [('author_round0',R0,old),('review_a',A,a_all)]:
        need(tb[role]==ta[role]==inventory(base,names),('unchanged rich source tree',role))
    live = inventory(PAPER,NAMES,('frozen_round0','frozen_round1'))
    need(ta['author_live']==live,'live exact postcopy tree and two literal prunes')
    lb,la = tb['author_live'],ta['author_live']
    need(set(lb)==set(la)=={'entries','pruned_exact_subtrees','declared_empty_directories'} and
         lb['declared_empty_directories']==la['declared_empty_directories']==[],
         'strict live before/after inventory schema; no external empty allowance')
    need(set(lb['pruned_exact_subtrees'])=={'frozen_round0'} and lb['pruned_exact_subtrees']['frozen_round0']==la['pruned_exact_subtrees']['frozen_round0'],'precopy sole exact Round0 prune unchanged')
    need(la['pruned_exact_subtrees']['frozen_round1']==frozen_tree['entries']['.'],'postcopy Round1 prune fully accounted')
    need({n:v for n,v in lb['entries'].items() if n!='.'}=={n:v for n,v in la['entries'].items() if n!='.'},'all author descendants rich unchanged')
    allowed = {'size','mtime_ns','ctime_ns','nlink'}
    need({k:v for k,v in lb['entries']['.']['stat'].items() if k not in allowed}=={k:v for k,v in la['entries']['.']['stat'].items() if k not in allowed},'only four permitted live parent metadata changes')
    external = {r['physical_path']:r for r in binding['external_inputs']}
    need(len(external)==len(binding['external_inputs']) and obj(EXEC/'EXTERNAL_REFERENCES.json')==external,'complete unique bound external roles')
    eb,ea = obj(EXEC/'EXTERNAL_INPUTS_BEFORE.json'),obj(EXEC/'EXTERNAL_INPUTS_AFTER.json')
    need(eb==ea and set(ea)==set(external),'entire rich external before/after key')
    for n,row in external.items():
        p = workspace(n)
        need(not p.is_relative_to(EXEC) and not p.is_relative_to(R1),'no self/output external prerequisite')
        pinned(p,row['pin'])
        need(ea[n]==reads[str(p)],('current full rich external key',n))
    def evidence(ref):
        need(ref['path'] in external and external[ref['path']]['pin']==ref['pin'],('exact externally consumed evidence reference',ref['path']))
    for ref in binding['acceptance_references'].values():
        evidence(ref)
    evidence(binding['root_authorization']['record'])
    for field,base in [('preparation_manifest',PREP),('role_preparation_manifest',ROLE)]:
        evidence(binding[field])
        need(binding[field]['path']==str((base/'SHA256SUMS').relative_to(ROOT)),('exact preparation seal role',field))
    for role,n in [('a_final_report','REPORT.md'),('a_final_findings','FINDINGS.json'),('same_a_accepted_delta','DELTA.md')]:
        need(binding['acceptance_references'][role]=={'path':str((A/n).relative_to(ROOT)),'pin':a_all[n]},('copied exact A acceptance role',role))
    need(binding['a_acceptance']['accepted_final_manifest_pin']==a['manifest_pin'],'same accepted whole A manifest')
    need(binding['acceptance_references']['round0_root_reception']=={'path':str((QA/'p211_round0_root_reception/RECEPTION.md').relative_to(ROOT)),'pin':{'bytes':external[str((QA/'p211_round0_root_reception/RECEPTION.md').relative_to(ROOT))]['pin']['bytes'],'sha256':'aaf5f7dfcacc3b9efa20edbf08bbce49d996418b33722b3bfb399110bcf4f3bd'}},'accepted Round0 reception identity')
    et = {}
    for spec in binding['external_trees']:
        need(set(spec)=={'root','files','empty_directories','manifest','accepted_scope_reference'},'exact v2 external tree fields')
        base = workspace(spec['root'])
        empties = spec['empty_directories']
        need(type(empties) is list and empties==list(EXTERNAL_EMPTY_DIRECTORIES.get(spec['root'],())),
             'exact ordered per-root empties; mandatory [] for every other external root')
        need(str(base) not in et,'distinct external tree')
        evidence(spec['accepted_scope_reference'])
        need({str((base/relative(n)).relative_to(ROOT)) for n in spec['files']} <= set(external),'entire declared external tree consumed')
        et[str(base)] = inventory(base,spec['files'],empty_directories=empties)
        if spec['manifest'] is not None:
            seal(base,empty_directories=empties)
    need({str(workspace(n)) for n in EXTERNAL_EMPTY_DIRECTORIES} <= set(et),
         'all three accepted external roots with their ten literal empty directories received')
    need({str(PREP),str(ROLE),str(QA/'p211_round0_execution01')} <= set(et),'mandatory complete preparation/Round0 trees')
    need(obj(EXEC/'EXTERNAL_TREES_BEFORE.json')==et==obj(EXEC/'EXTERNAL_TREES_AFTER.json'),'all rich external tree keys before/after/current')
    inherited = {}
    for filename,field,digest,count,is_external in [('READ_INPUTS.json','round0_read_resolutions','cc80175837802c01265eacaf58c623c3a52effa7f8adab6b992b7e6fecced5a8',727,False),('EXTERNAL_REFERENCES.json','round0_external_resolutions','d4ec07df5b9f57831f1a01ada7486f9fee8b736b424344081bbb6cd9592263d3',660,True)]:
        raw = read(QA/'p211_round0_execution01'/filename)
        need(pin(raw)['sha256']==digest,'immutable old metadata key')
        old_key = json.loads(raw)
        resolutions = binding[field]
        need(len(old_key)==count and set(old_key)==set(resolutions),'every historical key route, no omitted entry')
        mapped = {}
        for logical,row in old_key.items():
            value = row['pin'] if is_external else row
            physical = resolutions[logical]
            need(physical in external and external[physical]['pin']==value,('unchanged exact historical resolution',logical))
            mapped[logical] = {'physical_path':physical,'pin':value}
        inherited[filename] = mapped
    need(obj(EXEC/'INHERITED_ROUND0_RESOLUTIONS.json')==inherited,'entire rebuilt inherited key map')
    need(obj(EXEC/'DECLARED_PIN_LIST_BASES.json')==binding['pin_list_bases'],'unchanged pin-list declarations')
    seen = set()
    for spec in binding['pin_list_bases']:
        n = spec['document']
        need(n in selection and n not in seen,'distinct selected pin-list')
        seen.add(n)
        evidence(spec['accepted_origin_reference'])
        if spec['base']:
            relative(spec['base'])
        rows = sums(read(workspace(selection[n]['source'])),False)
        need(set(rows)==set(spec['resolutions']),'entire pin-list resolution set')
        for logical,digest in rows.items():
            target = spec['resolutions'][logical]
            need(target in ea and ea[target]['sha256']==digest,('explicit original-base pin target',n,logical))
        if n=='review_a/INPUT_PINS.sha256':
            need(spec['base']=='','A inputs preserve workspace base')
            for oldname,value in old.items():
                logical = str((R0/oldname).relative_to(ROOT))
                need(rows.get(logical)==value['sha256'] and spec['resolutions'][logical]==logical,'every historical33 A input pin')
    need(seen=={n for n in selection if n.endswith('.sha256')},'every copied SHA input list has its original base')
    json_bases = binding['json_pin_bases']
    need(obj(EXEC/'DECLARED_JSON_PIN_BASES.json')==json_bases and {'SOURCE_INPUT_PINS.json','SOURCE_PREPARATION_MANIFEST.json'} <= set(json_bases),'copied JSON declared schema/base metadata; not generic semantic validation')
    for n,spec in json_bases.items():
        need(n in selection and n.endswith('.json'),'selected JSON metadata document')
        if spec['base']:
            relative(spec['base'])
        evidence(spec['accepted_origin_and_schema_reference'])
    need(set(binding['document_origins'])=={n for n in selection if n.endswith('.md')},'every copied Markdown has exact original base')
    links = []
    for n,spec in sorted(binding['document_origins'].items()):
        if selection[n]['role']!='author':
            evidence(spec['accepted_origin_reference'])
        original = workspace(spec['original_document'])
        body = read(workspace(selection[n]['source'])).decode('utf-8')
        need(re.search(r'(?m)^\s{0,3}\[[^\]\n]+\]:',body) is None and re.search(r'\[[^\]\n]*\]\[[^\]\n]*\]',body) is None,'no unsupported reference-link syntax')
        actual = []
        for match in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',body):
            href = match.group(1).strip().strip('<>')
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',href) or href.startswith('#'):
                continue
            target = unquote(href.split('#',1)[0])
            need(target and '\\' not in target and not any(c in target for c in '\x00\r\n\t'),'bounded local href')
            logical = Path(os.path.abspath(original.parent/target))
            need(logical.is_relative_to(ROOT),'local href remains workspace')
            actual.append((href,str(logical.relative_to(ROOT))))
        need(actual==[(r['href'],r['logical_target']) for r in spec['local_links']],('entire ordered inline/image local-link list',n))
        for row in spec['local_links']:
            logical = workspace(row['logical_target'])
            dest = str(logical.relative_to(PAPER)) if logical.is_relative_to(PAPER) and str(logical.relative_to(PAPER)) in author else 'review_a/'+str(logical.relative_to(A)) if logical.is_relative_to(A) and str(logical.relative_to(A)) in a_all else None
            if dest is not None:
                need(row['kind']=='copied' and row['target']==dest,'selected current link routed to exact copied role')
                value = selection[dest]['pin']
            else:
                evidence(row['accepted_resolution_reference'])
                physical = workspace(row['target'])
                if row['kind']=='external_file':
                    need(row['target'] in ea,'external link fully consumed')
                    value = bytepin(ea[row['target']])
                else:
                    need(row['kind']=='external_directory','literal external directory role')
                    inventory(physical,row['directory_files'])
                    need({str((physical/relative(k)).relative_to(ROOT)) for k in row['directory_files']} <= set(ea),'entire external directory link consumed')
                    value = None
            links.append({'destination_document':n,'original_document':spec['original_document'],**row,'resolved_target_pin':value})
    need(links==obj(EXEC/'MARKDOWN_LINK_MAP.json'),'entire independently rebuilt link resolution table')
    tools_before,tools_after = obj(EXEC/'NATIVE_TOOLS_BEFORE.json'),obj(EXEC/'NATIVE_TOOLS_AFTER.json')
    need(tools_before==tools_after and set(tools_after)==TOOLS,'exact four rich native tool before/after keys')
    for p,value in binding['native_tool_pins'].items():
        pinned(Path(p),value)
        need(reads[p]==tools_after[p],('current rich native tool',p))
    specs = [('live_round0_compare_%03d'%i,['/usr/bin/cmp','--',str(PAPER/n),str(R0/n)],ROOT,b'') for i,n in enumerate(sorted(author),1)]
    specs += [('copy_author32',['/usr/bin/cp','-p','--parents','--',*sorted(author),str(R1)],R0,b''),('copy_complete_final_a',['/usr/bin/cp','-p','--parents','--',*sorted(a_all),str(R1/'review_a')],A,b'')]
    specs += [('copy_compare_%05d'%i,['/usr/bin/cmp','--',str(workspace(row['source'])),str(R1/n)],ROOT,b'') for i,(n,row) in enumerate(sorted(selection.items()),1)]
    specs += [('verify_outer_manifest',['/usr/bin/sha256sum','-c','SHA256SUMS'],R1,''.join(n+': OK\n' for n in sorted(expected)).encode()),('verify_inner_a_manifest',['/usr/bin/sha256sum','-c','SHA256SUMS'],R1/'review_a',''.join(n+': OK\n' for n in inner).encode())]
    need(len(specs)==119,'exact119 reconstructed native operations')
    command_files,commands,last_end = set(),[],0
    for label,argv,cwd,stdout in specs:
        directory = EXEC/'commands'/label
        command_files.update('commands/'+label+'/'+n for n in ('ATTEMPT.json','NATIVE.json','stdout.raw','stderr.raw'))
        attempt,native = obj(directory/'ATTEMPT.json'),obj(directory/'NATIVE.json')
        fixed = {'argv':argv,'cwd':str(cwd),'environment':ENV,'stdin':'subprocess.DEVNULL','timeout_seconds':60,'executable_key':tools_before[argv[0]]}
        need(set(attempt)==set(fixed)|{'started_epoch'} and all(attempt[k]==v for k,v in fixed.items()),('literal native attempt scope',label))
        need(set(native)==set(attempt)|{'native_exit_code','exception','stream_capture_status','ended_epoch','stdout','stderr','record_directory'} and all(native[k]==v for k,v in attempt.items()),('native binds complete attempt',label))
        need(type(native['native_exit_code']) is int and native['native_exit_code']==0 and native['exception'] is None and native['stream_capture_status']=='captured' and native['record_directory']=='commands/'+label and last_end<=attempt['started_epoch']<=native['ended_epoch'],('actual successful ordered native return',label))
        out,err = read(directory/'stdout.raw'),read(directory/'stderr.raw')
        need(out==stdout and err==b'' and pin(out)==native['stdout'] and pin(err)==native['stderr'],('all actual native raw streams',label))
        commands.append(native)
        last_end = native['ended_epoch']
    need(commands==obj(EXEC/'NATIVE_COMMANDS.json'),'all119 aggregate native rows in actual order')
    inventory(EXEC,TOP|command_files)
    seal(EXEC)
    invocation = obj(EXEC/'ROOT_INVOCATION_ATTEMPT.json')
    argv = ['/usr/bin/python3.10','-I','-S','-B',str(EXEC/'freeze.py'),'--binding',str(EXEC/'BINDING.json')]
    need(schema_ok(invocation,schema['$defs']['invocationAttempt'],schema),'exact actual root pre-invocation schema')
    fixed = {'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL','source_pin':source_pin,'binding_pin':binding_pin}
    need(all(invocation[k]==v for k,v in fixed.items()),'root pre-invocation exact source/binding')
    native = obj(EXEC/'ROOT_INVOCATION_NATIVE.json')
    need(set(native)==set(fixed)|{'timeout_seconds','started_epoch','ended_epoch','native_exit_code','exception','stream_capture_status','stdout','stderr'} and all(native[k]==v for k,v in fixed.items()),'actual root outer return exact fields/request')
    need(native['timeout_seconds']==900 and type(native['native_exit_code']) is int and native['native_exit_code']==0 and native['exception'] is None and native['stream_capture_status']=='captured','actual root full successful outer exit')
    need(invocation['started_epoch']<=native['started_epoch']<=commands[0]['started_epoch']<=last_end<=native['ended_epoch'],'root/child temporal containment')
    for field,path in [('stdout','root.stdout.raw'),('stderr','root.stderr.raw')]:
        raw = read(EXEC/path)
        need(native[field]=={'path':path,**pin(raw)},('actual root raw stream pin',field))
    need(read(EXEC/'root.stderr.raw')==b'' and json.loads(read(EXEC/'root.stdout.raw'))==result,'outer actual stdout JSON binds actual RESULT; stderr empty')
    process = obj(EXEC/'PROCESS_CONTEXT.json')
    need(set(process)=={'argv','cwd','environment','executable','sys_flags','observed_epoch'} and process['argv']==argv[4:] and process['cwd']==str(ROOT) and process['environment']==ENV and process['executable']=='/usr/bin/python3.10','actual recorded process invocation/settings')
    flags = process['sys_flags']
    need(all(re.search(r'(?:\(|, )'+key+'=1(?:,|\))',flags) for key in ('isolated','no_site','dont_write_bytecode')),'actual recorded isolated/no-site/no-bytecode flags')
    need(native['started_epoch']<=process['observed_epoch']<=commands[0]['started_epoch'],'actual process observation lies inside root invocation before child commands')
    rb,ra = obj(EXEC/'READ_INPUTS_BEFORE.json'),obj(EXEC/'READ_INPUTS_AFTER.json')
    expected_read = {str(workspace(n)) for n in external}|{str(PAPER/n) for n in author}|{str(R0/n) for n in old}|{str(A/n) for n in a_all}|{str(R1/n) for n in set(expected)|{'SHA256SUMS'}}|TOOLS|{str(EXEC/n) for n in ('freeze.py','BINDING.json','ROOT_INVOCATION_ATTEMPT.json')}|{str(PREP/'freeze.py'),str(ROLE/'ROLE_SELECTION_DRAFT.json'),str(QA/'p211_round0_execution01/freeze.py'),str(ledger_path),str(QA/'p211_round0_execution01/READ_INPUTS.json'),str(QA/'p211_round0_execution01/EXTERNAL_REFERENCES.json')}
    need(rb==ra and set(ra)==expected_read,'entire independently reconstructed recorder read key, no omitted/redundant path')
    for p,key in ra.items():
        read(Path(p))
        need(reads[p]==key,('all recorder reads current full rich keys',p))
    host = binding['host_reuse_boundary']
    need(obj(EXEC/'HOST_REUSE_BOUNDARY.json')==host,'exact explicit host-reuse boundary')
    for field in ('complete_host_key_reference','accepted_runtime_settings_reference','precopy_recheck_reference'):
        evidence(host[field])
    host_path = workspace(args.root_host_evidence)
    need(not host_path.is_relative_to(EXEC) and not host_path.is_relative_to(R1),'separate root postcopy evidence outside sealed producer trees')
    host_raw = read(host_path)
    need(pin(host_raw)['sha256']==args.root_host_sha256,'root-supplied exact postcopy evidence identity')
    json.loads(host_raw)  # Original record bytes only; no generic host schema or implicit host PASS.
    need(result['status']=='PHYSICAL_P211_ROUND1_CREATED_PENDING_ROOT_RECEPTION' and result['author_payloads']==32 and result['a_manifest_payloads']==50 and result['a_copied_files']==51 and result['payloads']==83 and result['files_with_manifest']==84 and result['b_complete_round1_input_count']==84 and result['native_commands']==119 and result['read_paths']==len(ra) and result['external_files']==len(external) and result['mapped_local_links']==len(links) and result['payload_bytes']==sum(v['bytes'] for v in expected.values()),'actual result exact complete census')
    need(result['allowed_live_parent_directory_metadata_changes']==sorted(allowed) and all(type(result[k]) is int and result[k]==0 for k in ('scientific_executions','builds','new_page_views','reviews')) and result['paper_complete'] is False and result['execution_package_seal']=='PENDING_ACTUAL_ROOT_INVOCATION_RETURN' and result['complete_host_key_rehashed_by_recorder'] is False and result['complete_host_key_and_settings_postcopy_recheck']=='PENDING_SEPARATE_ROOT_RECEPTION' and result['external']=='HOLD_EXTERNAL','historical pending result not rewritten as root/science/host acceptance')
    before = dict(reads)
    after = {p:fresh(Path(p))[1] for p in sorted(before)}
    need(before==after,'all receiver full rich read keys unchanged at completion')
    tree_records = []
    for (base,names,prune,empties),value in list(trees.items()):
        need(inventory(Path(base),names,prune,False,empty_directories=empties)==value,('entire receiver-observed rich tree final closure',base))
        tree_records.append({'root':base,'files':list(names),'prune':list(prune),'declared_empty_directories':list(empties),'inventory':value})
    return {'schema':'p211_round1_documentary_receiver_v2','status':'PASS_PHYSICAL_DOCUMENTARY_SCOPE_HOST_ACCEPTANCE_EXTERNAL_ROOT','checks':checks,'payloads':83,'round1_files':84,'native_child_records':119,'native_child_raw_streams':238,'native_root_records':1,'declared_external_empty_directories':10,'external_files':len(external),'recorder_read_paths':len(ra),'receiver_read_paths':len(before),'execution_files':len(TOP|command_files),'root_postcopy_host_evidence':{'path':args.root_host_evidence,'pin':pin(host_raw),'interpretation':'FULL_BYTES_CONSUMED_ONLY; exact complete host/settings semantics and original native provenance require root reception'},'recorder_dereferences_complete_host_key':False,'receiver_dereferences_799_host_referents':False,'submitted_programs_executed':0,'scientific_executions':0,'builds':0,'page_views':0,'manuscript_reviews':0,'paper_complete':False,'external':'HOLD_EXTERNAL','READ_INPUTS_BEFORE':before,'READ_INPUTS_AFTER':after,'RICH_INVENTORIES':tree_records}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root-host-evidence',required=True,help='Workspace-relative original root postcopy JSON; consumed, not adjudicated')
    parser.add_argument('--root-host-sha256',required=True)
    args = parser.parse_args()
    try:
        need(re.fullmatch('[0-9a-f]{64}',args.root_host_sha256) is not None,'explicit root host evidence sha256')
        outcome = audit(args)
    except BaseException:
        print(json.dumps({'status':'FAIL_DOCUMENTARY_SCOPE_PRESERVE_ORIGINALS','checks':checks,'traceback':traceback.format_exc(),'READ_INPUTS_PARTIAL':reads},sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(outcome,sort_keys=True))
