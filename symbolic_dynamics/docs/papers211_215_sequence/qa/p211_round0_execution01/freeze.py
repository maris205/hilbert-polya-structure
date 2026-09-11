#!/usr/bin/python3.10
"""Physical, narrowly selected P211 Round0; no scientific/build execution."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import time
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = Path(__file__).resolve().parent
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
FROZEN = PAPER/'frozen_round0'
ADOPT = QA/'p211_initial_build_adoption01'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
NAMES = '''AUTHOR_EXECUTION_RECEIPT.md CANONICAL.json CANONICAL_SCHEMA.md CLAIMS_EVIDENCE.md HANDOFF.md INITIAL_BUILD_RECEIPT.md NARRATIVE_REPORT.md PAPER_PLAN.md PARAMETER_SPECIFICATION.md PREPARATION_PLAN.md PROOF_PACKAGE.md README.md SOURCE_AUDIT.md SOURCE_INPUT_PINS.json SOURCE_PIN_COLLECTION_TOOL_RETURN.json SOURCE_PREPARATION_MANIFEST.json STATIC_CHECK_TOOL_RETURN.json main.pdf main.tex math_commands.tex parameters.json references.bib sections/0_abstract.tex sections/1_introduction.tex sections/2_image.tex sections/3_clock.tex sections/4_inverse.tex sections/5_scope.tex sources/bibliographic_metadata_web.json sources/stein_definition_web.json sources/stein_support_web.json verify.py'''.split()
reads, external = {}, {}
checks, commands = 0, []


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
    p = HERE/name
    raw = value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with p.open('xb') as stream:
        stream.write(raw)


def consume(path,role,logical=None):
    p = Path(path)
    need(p.is_file() and not p.is_symlink() and p.resolve() == p,('physical external file',str(p)))
    value = pin(read(p))
    key = str(p.relative_to(ROOT))
    row = external.setdefault(key,{'physical_path':key,'pin':value,'roles':[],'logical_paths':[]})
    need(row['pin'] == value,('external consistent',key))
    if role not in row['roles']:
        row['roles'].append(role)
    if logical is not None and str(Path(logical).relative_to(ROOT)) not in row['logical_paths']:
        row['logical_paths'].append(str(Path(logical).relative_to(ROOT)))
    return value


def command(label,argv,cwd=ROOT,empty=True):
    directory = HERE/'commands'/label
    directory.mkdir(parents=True)
    request = {'argv':argv,'cwd':str(cwd),'environment':ENV,'started_epoch':time.time()}
    put(directory/'ATTEMPT.json',request)
    actual = subprocess.run(argv,cwd=cwd,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=60)
    put(directory/'stdout.raw',actual.stdout)
    put(directory/'stderr.raw',actual.stderr)
    receipt = {**request,'native_exit_code':actual.returncode,'ended_epoch':time.time(),
               'stdout':pin(actual.stdout),'stderr':pin(actual.stderr)}
    put(directory/'NATIVE.json',receipt)
    commands.append(receipt)
    need(actual.returncode == 0 and actual.stderr == b'' and (not empty or actual.stdout == b''),('native',label))
    return actual.stdout


def sealed_external(base,expected_count):
    raw = read(base/'SHA256SUMS')
    consume(base/'SHA256SUMS','complete accepted package nonself manifest')
    seen = set()
    for line in raw.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None,('manifest syntax',str(base)))
        digest,name = m.groups()
        need(name not in seen and name != 'SHA256SUMS' and not Path(name).is_absolute() and '..' not in Path(name).parts,('nonself path',name))
        seen.add(name)
        need(consume(base/name,'complete accepted package payload')['sha256'] == digest,('external payload',name))
    need(len(seen) == expected_count and seen == {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()}-{'SHA256SUMS'},('complete package',str(base)))


need(Path.cwd() == ROOT and HERE == QA/'p211_round0_execution01','literal execution path')
need(not os.path.lexists(FROZEN) and not (PAPER/'frozen_round1').exists() and not (PAPER/'frozen_round2').exists(),'first physical Round0 only')
put('EXECUTED_FREEZE_SOURCE.py',read(Path(__file__).resolve()))
need(len(NAMES) == len(set(NAMES)) == 32,'literal 32-file scope')
need(obj(ADOPT/'LIFECYCLE_RESULT.json')['status'] == 'ROOT_INITIAL_BUILD_DOCUMENTARY_DELTA_AND_LINKS_PASS','accepted current lifecycle prerequisite')
native = obj(ADOPT/'LIFECYCLE_NATIVE01.json')['result']
need(native['exit_code'] == 0 and json.loads(native['output']) == obj(ADOPT/'LIFECYCLE_RESULT.json'),'actual lifecycle completion')
expected = obj(ADOPT/'PAPER_INPUTS_AFTER.json')
need(set(expected) == set(NAMES),'exact accepted selection')
current_names = {str(p.relative_to(PAPER)) for p in PAPER.rglob('*') if p.is_file()}
need(current_names == set(NAMES) and not any(p.is_symlink() for p in PAPER.rglob('*')),'current complete ordinary source set')
before = {n:pin(read(PAPER/n)) for n in sorted(NAMES)}
need(before == expected,'accepted full paper bytes unchanged')
need(before['main.pdf'] == {'bytes':301007,'sha256':'532b8c462e907878c3d75829b2c4ff86de7d59c137efa91b61ebc80717a077dc'},'accepted PDF')
need(before['CANONICAL.json'] == {'bytes':1327062,'sha256':'2a9d1311a491805644efa7cd4884ae50ed9f9ffa48e347b822a7ff68e12ee6b4'},'accepted canonical')
need(read(PAPER/'main.pdf') == read(QA/'p211_initial_build_01/inner/source_only/main.pdf'),'full accepted PDF equality')
put('SOURCE_INPUTS_BEFORE.json',before)
for p in [QA/'p211_round0_preparation/PLAN.md',ROOT/'docs/papers211_215_sequence/P211_REVIEW_CONTRACT.md',
          ROOT/'docs/research_state/WORKFLOW.md',ROOT/'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
          ADOPT/'RECEPTION.md',ADOPT/'LIFECYCLE_RESULT.json',ADOPT/'LIFECYCLE_NATIVE01.json',
          ADOPT/'PAPER_INPUTS_AFTER.json',ADOPT/'HISTORICAL_MAPPING.json',ADOPT/'RESULT.json',
          QA/'p211_initial_build_root_reception/RECEPTION.md',QA/'p211_initial_build_root_reception/VISUAL_RECEPTION.md',
          QA/'p211_initial_build_root_reception/AUDITOR_RESULT.json',QA/'p211_initial_build_root_reception/AUDITOR_NATIVE01.json',
          QA/'p211_initial_build_root_reception/run01/READ_INPUTS_BEFORE.json',
          QA/'p211_initial_build_root_reception/run01/READ_INPUTS_AFTER.json',
          QA/'p211_initial_build_binding01/BINDING.json',QA/'p211_initial_build_binding01/ROOT_DERIVED_SOURCE_LOCK.json',
          QA/'p211_initial_build_binding01/SOURCE_LOCK_DELTA.json',QA/'p211_initial_build_binding01/BUILD_TOOL_INVOCATION.json',
          QA/'P211_AUTHOR_RUNTIME_RECEPTION.md',QA/'p211_runtime_root_reception/RECEPTION.md',
          QA/'p211_author_execution_documentation_root/RECEPTION.md',QA/'p211_author_binding_closure/RECEPTION.md']:
    consume(p,'accepted prerequisite or explicit bounded dependency key; not a fresh runtime/build gate')
for base,count in [(QA/'p211_initial_build_01',362),(QA/'root_replays/p211_author_initial_01',77),
                   (QA/'root_replays/p211_author_pair_01',104),(QA/'p211_author_initial_binding',20),
                   (QA/'p211_author_pair_binding',10),(QA/'p211_initial_build_independent_reception',18)]:
    sealed_external(base,count)
controls = [ROOT/'SYMBOLIC_DYNAMICS_STATE.md',ROOT/'docs/papers211_215_sequence/PIPELINE_STATE.md']
historical = []
(HERE/'control_originals').mkdir()
for index,source in enumerate(controls,1):
    value = pin(read(source)); destination = HERE/'control_originals'/source.name
    command('control_copy_'+str(index),['/usr/bin/cp','-p','--',str(source),str(destination)])
    command('control_compare_'+str(index),['/usr/bin/cmp','--',str(source),str(destination)])
    need(pin(read(destination)) == value,'pre-freeze control physical copy')
    consume(destination,'navigation version physically preserved before next index update',source)
    historical.append({'logical_path':str(source.relative_to(ROOT)),'physical_original':str(destination.relative_to(ROOT)),'pin':value})
for row in obj(ADOPT/'HISTORICAL_MAPPING.json'):
    consume(row['physical_original'],'exact earlier initial-build/README historical pin',row['logical_path'])
put('CONTROL_HISTORICAL_MAPPING.json',historical)
FROZEN.mkdir()
command('copy_all_32',['/usr/bin/cp','-p','--parents','--',*sorted(NAMES),str(FROZEN)],cwd=PAPER)
roles = []
for index,name in enumerate(sorted(NAMES),1):
    source,destination = PAPER/name,FROZEN/name
    ss,ds = source.stat(),destination.stat()
    need(stat.S_ISREG(ds.st_mode) and not destination.is_symlink() and destination.resolve() == destination,'physical frozen file')
    need((ss.st_dev,ss.st_ino) != (ds.st_dev,ds.st_ino),'not a hardlink')
    command('compare_%02d'%index,['/usr/bin/cmp','--',str(source),str(destination)])
    need(read(source) == read(destination) and pin(read(destination)) == before[name],('full bytes',name))
    roles.append({'original_path':str(source.relative_to(ROOT)),'frozen_path':str(destination.relative_to(ROOT)),
                  'relative_name':name,'pin':before[name],'source_inode':[ss.st_dev,ss.st_ino],'frozen_inode':[ds.st_dev,ds.st_ino]})
manifest = ''.join(before[name]['sha256']+'  '+name+'\n' for name in sorted(NAMES)).encode()
with (FROZEN/'SHA256SUMS').open('xb') as stream:
    stream.write(manifest)
need({str(p.relative_to(FROZEN)) for p in FROZEN.rglob('*') if p.is_file()} == set(NAMES)|{'SHA256SUMS'},'complete frozen membership')
sumout = command('verify_frozen_manifest',['/usr/bin/sha256sum','-c','SHA256SUMS'],cwd=FROZEN,empty=False)
need(sumout == ''.join(n+': OK\n' for n in sorted(NAMES)).encode(),'all 32 actual native hash results')
links = []
for name in sorted(n for n in NAMES if n.endswith('.md')):
    original,frozen = PAPER/name,FROZEN/name
    for match in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',read(frozen).decode()):
        href = match.group(1).strip().strip('<>')
        if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',href) or href.startswith('#'):
            continue
        logical = (original.parent/unquote(href.split('#',1)[0])).resolve()
        if logical.is_relative_to(PAPER) and str(logical.relative_to(PAPER)) in NAMES:
            physical = FROZEN/logical.relative_to(PAPER)
            need(pin(read(physical)) == before[str(logical.relative_to(PAPER))],'paper link to exact frozen target')
            role = 'frozen paper input'
        elif logical in controls:
            physical = HERE/'control_originals'/logical.name
            role = 'navigation version observed at freeze, not proof evidence'
        else:
            physical = logical
            role = 'external original-location evidence link'
            need(physical.exists(),('external link',name,href))
            if physical.is_dir():
                allowed = QA/'p211_author_source_reception/source_preparation_original'
                need(physical == allowed,'only explicitly scoped directory link')
                files = [p for p in physical.rglob('*') if p.is_file()]
                need(len(files) == 28,'full historical preparation directory scope')
                for p in files:
                    consume(p,'full 28-file historical source-preparation directory target')
            else:
                consume(physical,role,logical)
        links.append({'frozen_document':str(frozen.relative_to(ROOT)),'original_document':str(original.relative_to(ROOT)),
                      'href':href,'logical_target':str(logical.relative_to(ROOT)),'physical_target':str(physical.relative_to(ROOT)),'role':role})
after = {n:pin(read(PAPER/n)) for n in sorted(NAMES)}
need(after == before,'source key unchanged after freeze')
need(not any(p.is_symlink() for p in FROZEN.rglob('*')),'no frozen symlink')
for p,value in list(reads.items()):
    need(pin(Path(p).read_bytes()) == value,('final read closure',p))
put('SOURCE_INPUTS_AFTER.json',after)
put('FROZEN_ORIGIN_MAP.json',roles)
put('MARKDOWN_LINK_MAP.json',links)
put('EXTERNAL_REFERENCES.json',external)
put('READ_INPUTS.json',reads)
result = {'status':'PHYSICAL_P211_ROUND0_CREATED_PENDING_ROOT_AND_INDEPENDENT_RECEPTION','payloads':32,'files_with_manifest':33,
          'manifest':pin(manifest),'payload_bytes':sum(v['bytes'] for v in before.values()),'checks':checks,
          'read_paths':len(reads),'native_commands':len(commands),'external_files':len(external),'mapped_local_links':len(links),
          'physical_control_originals':2,'all_source_before_after_frozen_bytes_equal':True,
          'scientific_executions':0,'builds':0,'new_page_views':0,'reviews':0,'paper_complete':False,'external':'HOLD_EXTERNAL'}
put('RESULT.json',result)
print(json.dumps(result,sort_keys=True))
