#!/usr/bin/python3.10
"""Check the exact initial-build documentary delta and physical historical pins."""
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
reads = {}
checks = 0


def need(value,label):
    global checks
    checks += 1
    assert value,label


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def read(p):
    p = Path(p)
    raw = p.read_bytes()
    need(str(p) not in reads or reads[str(p)] == pin(raw),('read drift',str(p)))
    reads[str(p)] = pin(raw)
    return raw


def obj(p):
    return json.loads(read(p))


def put(name,value):
    raw = value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (HERE/name).open('xb') as stream:
        stream.write(raw)


need(Path.cwd() == ROOT,'cwd')
before = obj(HERE/'PAPER_BEFORE.json')
after = {str(p.relative_to(PAPER)):pin(read(p)) for p in PAPER.rglob('*') if p.is_file()}
need(len(before) == 30 and len(after) == 32,'exact paper inventory')
need(set(after)-set(before) == {'main.pdf','INITIAL_BUILD_RECEIPT.md'} and set(before) <= set(after),'only two additions')
need([name for name in before if before[name] != after[name]] == ['README.md'],'only README among 30 existing files changes')
adoption = obj(HERE/'RESULT.json')
need(adoption['status'] == 'ROOT_INITIAL_PDF_EXCLUSIVELY_ADOPTED_AND_PREUPDATE_ORIGINALS_PRESERVED','adoption accepted')
need(after['main.pdf'] == {k:adoption['pdf'][k] for k in ('bytes','sha256')},'adopted PDF pin')
need(read(PAPER/'main.pdf') == read(adoption['pdf']['source']),'whole source/adopted PDF bytes')
native = obj(HERE/'NATIVE01.json')['result']
need(native['exit_code'] == 0 and json.loads(native['output']) == adoption,'actual adoption tool return')
mapping = obj(HERE/'HISTORICAL_MAPPING.json')
need(len(mapping) == 3,'three historical originals')
for row in mapping:
    physical = Path(row['physical_original'])
    need(physical.parent == HERE/'originals' and pin(read(physical)) == row['pin'],'physical mapping')
    need(pin(read(row['logical_path'])) != row['pin'],'three actual lifecycle deltas')
    label = physical.stem
    argv = ['/usr/bin/diff','-u',str(physical),row['logical_path']]
    actual = subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=30)
    put(label+'_DIFF_STDOUT.raw',actual.stdout)
    put(label+'_DIFF_STDERR.raw',actual.stderr)
    put(label+'_DIFF_NATIVE.json',{'argv':argv,'cwd':str(ROOT),'environment':ENV,'native_exit_code':actual.returncode,
                                 'stdout':pin(actual.stdout),'stderr':pin(actual.stderr)})
    need(actual.returncode == 1 and actual.stderr == b'','complete actual documentary diff')
for package in ['p211_initial_build_independent_reception','p211_initial_build_root_reception']:
    prior = obj(HERE.parent/package/'run01/READ_INPUTS_BEFORE.json')
    for row in mapping[:2]:
        need(prior[row['logical_path']] == row['pin'],'old audit exact control mapping')
doc_inputs = obj(HERE.parent/'p211_author_execution_documentation_root/INPUTS.json')
need(doc_inputs[str(PAPER/'README.md')] == mapping[2]['pin'],'old documentary exact README mapping')
documents = sorted(PAPER.glob('*.md'))+[ROOT/'SYMBOLIC_DYNAMICS_STATE.md',ROOT/'docs/papers211_215_sequence/PIPELINE_STATE.md']
links = []
for doc in documents:
    for match in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',read(doc).decode()):
        href = match.group(1).strip().strip('<>')
        if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',href) or href.startswith('#'):
            continue
        part = unquote(href.split('#',1)[0])
        target = (doc.parent/part).resolve()
        need(target.exists(),('local link',str(doc),href,str(target)))
        links.append({'document':str(doc),'href':href,'target':str(target)})
for p,value in list(reads.items()):
    need(pin(Path(p).read_bytes()) == value,('final drift',p))
put('LIFECYCLE_INPUTS.json',reads)
put('PAPER_INPUTS_AFTER.json',after)
put('LIFECYCLE_LINKS.json',links)
result = {'status':'ROOT_INITIAL_BUILD_DOCUMENTARY_DELTA_AND_LINKS_PASS','checks':checks,'read_paths':len(reads),
          'paper_files':32,'changed_existing':['README.md'],'added':['INITIAL_BUILD_RECEIPT.md','main.pdf'],
          'unchanged_existing':29,'physical_historical_mappings':3,'fresh_native_diffs':3,
          'documents_checked':len(documents),'local_link_occurrences':len(links),
          'scientific_executions':0,'builds':0,'reviews':0,'round0':False}
put('LIFECYCLE_RESULT.json',result)
print(json.dumps(result,sort_keys=True))
