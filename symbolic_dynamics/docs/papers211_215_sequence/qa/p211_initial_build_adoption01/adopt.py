#!/usr/bin/python3.10
"""Adopt the accepted initial PDF and preserve exact pre-lifecycle originals."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = Path(__file__).resolve().parent
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
REC = QA/'p211_initial_build_root_reception'
SOURCE = QA/'p211_initial_build_01/inner/source_only/main.pdf'
TARGET = PAPER/'main.pdf'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
reads = {}


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    assert str(p) not in reads or reads[str(p)] == pin(raw), str(p)
    reads[str(p)] = pin(raw)
    return raw


def data(path):
    return json.loads(read(path))


def put(name, value):
    p = HERE/name
    raw = value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with p.open('xb') as stream:
        stream.write(raw)


def command(label, argv):
    directory = HERE/'commands'/label
    directory.mkdir(parents=True)
    result = subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=30)
    put(directory/'stdout.raw',result.stdout)
    put(directory/'stderr.raw',result.stderr)
    receipt = {'argv':argv,'cwd':str(ROOT),'environment':ENV,'native_exit_code':result.returncode,
               'stdout':pin(result.stdout),'stderr':pin(result.stderr)}
    put(directory/'NATIVE.json',receipt)
    assert result.returncode == 0 and result.stdout == result.stderr == b'', label


assert Path.cwd() == ROOT and TARGET.resolve() == TARGET and not os.path.lexists(TARGET)
assert not any((PAPER/('frozen_round'+str(n))).exists() for n in range(3))
assert data(REC/'AUDITOR_RESULT.json')['status'] == 'ROOT_RECEIVES_COMPLETE_INDEPENDENT_BUILD_AUDIT_AND_DISCLOSED_ROOT_RECHECK'
native = data(REC/'AUDITOR_NATIVE01.json')['result']
assert native['exit_code'] == 0 and json.loads(native['output']) == data(REC/'AUDITOR_RESULT.json')
read(REC/'RECEPTION.md')
visual = read(REC/'VISUAL_RECEPTION.md')
pdf = read(SOURCE)
assert pin(pdf) == {'bytes':301007,'sha256':'532b8c462e907878c3d75829b2c4ff86de7d59c137efa91b61ebc80717a077dc'}
assert pin(pdf)['sha256'].encode() in visual
accepted = data(QA/'p211_author_execution_documentation_root/INPUTS.json')
paper_key = {str(Path(p).relative_to(PAPER)):value for p,value in accepted.items() if Path(p).is_relative_to(PAPER)}
assert len(paper_key) == 30
current = {str(p.relative_to(PAPER)):pin(read(p)) for p in PAPER.rglob('*') if p.is_file()}
assert current == paper_key and not any(p.is_symlink() for p in PAPER.rglob('*'))
put('PAPER_BEFORE.json',current)
audited_inputs = data(REC/'run01/READ_INPUTS_BEFORE.json')
controls = [(ROOT/'SYMBOLIC_DYNAMICS_STATE.md','SYMBOLIC_DYNAMICS_STATE.md'),
            (ROOT/'docs/papers211_215_sequence/PIPELINE_STATE.md','PIPELINE_STATE.md'),
            (PAPER/'README.md','P211_README.md')]
originals = HERE/'originals'
originals.mkdir()
mapping = []
for index,(source,name) in enumerate(controls,1):
    value = pin(read(source))
    assert value == (paper_key['README.md'] if name == 'P211_README.md' else audited_inputs[str(source)])
    destination = originals/name
    assert not destination.exists()
    command('copy_%02d'%index,['/usr/bin/cp','-p','--',str(source),str(destination)])
    command('compare_%02d'%index,['/usr/bin/cmp','--',str(source),str(destination)])
    assert read(source) == read(destination)
    mapping.append({'logical_path':str(source),'physical_original':str(destination),'pin':value,
                    'role':'Pre-initial-build-lifecycle bytes, physically copied before modification'})
put('HISTORICAL_MAPPING.json',mapping)
put('ADOPTION_ATTEMPT.json',{'source':str(SOURCE),'target':str(TARGET),'pin':pin(pdf),
                            'target_absent_before':True,'exclusive_raw_adoption':True,'new_science':False})
with TARGET.open('xb') as stream:
    stream.write(pdf)
    stream.flush()
    os.fsync(stream.fileno())
command('compare_adopted_pdf',['/usr/bin/cmp','--',str(SOURCE),str(TARGET)])
assert read(TARGET) == pdf
after = {str(p.relative_to(PAPER)):pin(read(p)) for p in PAPER.rglob('*') if p.is_file()}
assert after == {**current,'main.pdf':pin(pdf)}
for p,value in list(reads.items()):
    assert pin(Path(p).read_bytes()) == value, ('final drift',p)
put('INPUTS.json',reads)
result = {'status':'ROOT_INITIAL_PDF_EXCLUSIVELY_ADOPTED_AND_PREUPDATE_ORIGINALS_PRESERVED',
          'pdf':{'source':str(SOURCE),'target':str(TARGET),**pin(pdf)},'physical_control_originals':3,
          'native_commands':7,'original_paper_files_unchanged':30,'paper_files_after_pdf':31,
          'scientific_executions':0,'builds':0,'new_page_views':0,'reviews':0,'round0':False}
put('RESULT.json',result)
print(json.dumps(result,sort_keys=True))
