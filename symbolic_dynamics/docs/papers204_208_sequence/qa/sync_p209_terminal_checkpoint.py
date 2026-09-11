#!/usr/bin/env python3
"""Root's exact-scope private checkpoint; no science or lifecycle acceptance.

prepare: verify immutable selections and capture real pins, read-only Git.
copy: copy precisely those verified bytes into a clean known mirror.
stage: stage only copied pins (including exact ignored evidence) and audit tree.
Outputs are exclusive generated execution receipts, never overwritten.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
B = 'docs/papers204_208_sequence/'
P = 'papers/209-ordered-fibre-threading/'
Q = B + 'qa/'
OUT = ROOT / (Q + 'p209_terminal_private_checkpoint')
BASE = '2974f8ea5f9e7cb0f8146cae017add38a6939da0'
EXCLUDED = [B+'scouting/finite_systems_thirty_'+i+'/' for i in ('third','fourth','fifth')]
EXCLUDED += [B+'scouting/LNR_SOURCE_RECHECK/', Q+'p209_terminal_artifact_preparation/', Q+'p209_terminal_artifact/']
COMMANDS = []


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    return path.read_bytes()


def valid(path):
    p = PurePosixPath(path)
    assert not p.is_absolute() and '..' not in p.parts and str(p) == path
    assert not any(path.startswith(e) for e in EXCLUDED), path
    return path


def git(*args, input=None, allowed=(0,)):
    argv = ['git','-C',str(MIRROR),*args]
    r = subprocess.run(argv, input=input, capture_output=True)
    COMMANDS.append({'argv':argv,'exit_code':r.returncode,
                     'stdout':r.stdout.decode(),'stderr':r.stderr.decode()})
    assert r.returncode in allowed, COMMANDS[-1]
    return r.stdout


def parse(data):
    result = {}
    for line in data.decode().splitlines():
        h, name = line.split(maxsplit=1)
        name = name.removeprefix('*')
        valid(name)
        assert len(h)==64 and set(h)<=set('0123456789abcdef') and name not in result
        result[name] = h
    assert result
    return result


def emit(name, result):
    OUT.mkdir(exist_ok=True)
    result['commands'] = COMMANDS
    target = OUT / name
    with target.open('x') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps({'receipt':str(target.relative_to(ROOT)), 'sha256':sha(read(target)),
                      **{k:v for k,v in result.items() if k not in ('commands','pins','named_manifests','staged_paths','ignored_paths','tree_pins')}}, sort_keys=True))


def clean_baseline():
    assert git('status','--porcelain=v1') == b''
    assert git('rev-parse','HEAD').decode().strip() == BASE
    assert git('rev-parse','origin/main').decode().strip() == BASE
    assert git('rev-list','--left-right','--count','HEAD...origin/main') == b'0\t0\n'
    assert not (MIRROR/'.git/index.lock').exists()


def recheck(pins, base):
    for path, h in pins.items():
        valid(path)
        assert sha(read(base/path)) == h, (str(base),path)


def prepare():
    clean_baseline()
    plan = json.loads(read(ROOT/(Q+'p209_private_sync_preparation/SCOPES.plan.json')))
    packages = [(p['data_relative'], p['seal_sha256'],p['declared_payloads'])
                for p in plan['completed_sealed_package_candidates']]
    c = plan['conditional_author_archive']
    packages.append((c['data_relative'],c['manifest']['sha256'],153))
    packages.extend([
        (P+'qa_final','2034f023775cdc7682c418fb9da7fb54fddd88a56439e969793a6576c9845a5e',225),
        (Q+'root_replays/p209_terminal_strict/launcher_terminal_pair_01','6cfa3166f36f409d6cde2419d4050f69cfd70f0d8296a6279d9dc0fe1b0eb88e',10),
        (Q+'central_lifecycle_p209_terminal','d9ff597596feaf765531b3c863ebbe4636a10cbca6599caac72ffda4b67fc20a',5),
        (Q+'p209_postterminal_rollup','cdf8c7ab9e144a86cac553ae89359da00bc6c415f89190af1d76f5265ed5712d',3),
        (Q+'p209_private_sync_preparation','ac345e8626efbc3cbfeaaa9a7926fd17410e2cd97e5da540d820dc019a0556d0',7),
    ])
    pins, named = {}, []
    def add(path, h=None):
        valid(path)
        actual=sha(read(ROOT/path))
        assert h is None or actual==h, path
        assert path not in pins or pins[path]==actual
        pins[path]=actual
    def manifest(path, base, count, complete, select=True, expected=None):
        data=read(ROOT/path)
        assert expected is None or sha(data)==expected, path
        rows=parse(data)
        assert len(rows)==count, (path,len(rows),count)
        if complete:
            names={str(p.relative_to(ROOT/base)) for p in (ROOT/base).rglob('*') if p.is_file()}
            assert names == set(rows)|{str(PurePosixPath(path).relative_to(base))}, (path,len(names))
        for rel,h in rows.items():
            assert sha(read(ROOT/(base+'/'+rel)))==h, (path,rel)
            if select: add(base+'/'+rel,h)
        if select: add(path)
        named.append({'manifest':path,'base':base,'entries':count,'complete':complete,'sha256':sha(data)})
    for base,h,count in packages:
        manifest(base+'/SHA256SUMS',base,count,True,expected=h)
    manifest(P+'PAPER_MANIFEST.sha256',P.rstrip('/'),8231,True,
             expected='84337036dead70c7680aed5678ed770505b1caa0184b5f405d353c4d9a811c77')
    for leaf,count in [('SHA256SUMS',1985),('AUTHOR_MANIFEST.sha256',1985),('frozen_round0/SHA256SUMS',1989),('frozen_round1/SHA256SUMS',2003)]:
        base=P.rstrip('/') if '/' not in leaf else P+leaf.rsplit('/',1)[0]
        manifest(P+leaf,base,count,'/' in leaf,False)
    manifest(P+'frozen_round2/ROUND2_ACCEPTANCE/PRE_ROUND2_PAPER_MANIFEST.sha256',P.rstrip('/'),5982,False,False)
    manifest(Q+'p209_postterminal_rollup/PRE_TERMINAL_PAPER_MANIFEST.sha256',P.rstrip('/'),8004,False,False)
    manifest(B+'reviews/p209_a/SHA256SUMS',B+'reviews/p209_a',1342,True,False)
    for d in plan['exact_changed_document_candidates']:
        rel=d['data_relative']
        add(rel,None if rel in ['SYMBOLIC_DYNAMICS_STATE.md',B+'PIPELINE_STATE.md'] else d['observed_sha256'])
    extras=[Q+'SCOUT32_ROOT_INSPECTION.actual.json',Q+'inspect_scout32_root.py',B+'scouting/THIRTY_SECOND_ROOT_INSPECTION.md',
            Q+'P209_TERMINAL_PREPARATION_ROOT_INSPECTION.actual.json',Q+'inspect_p209_terminal_preparation.py',
            Q+'P209_TERMINAL_BUILD_EXECUTION.actual.json',Q+'P209_TERMINAL_ROOT_VIEWS.actual.json',Q+'P209_TERMINAL_ROOT_VIEWS.md',
            Q+'sync_p209_terminal_checkpoint.py']
    for rel in extras: add(rel)
    for d in plan['unchanged_protected_paper_files']:
        if d['path']!=P+'PAPER_MANIFEST.sha256': assert pins[d['path']]==d['sha256']
    recheck(pins,ROOT)
    emit('SELECTION.actual.json',{'schema':'p209-terminal-private-selection-v1','status':'VERIFIED_EXACT_SELECTION_NOT_COPIED',
         'baseline':BASE,'selected_paths':len(pins),'pins':pins,'named_manifests':named,'named_manifest_count':len(named),
         'exclusions':EXCLUDED,'paper_role':'P209_ARTIFACT_GATE_PENDING_NOT_COMPLETE','scope':'Private byte-integrity archive, not new math/build/view or terminal acceptance.'})


def selected():
    return json.loads(read(OUT/'SELECTION.actual.json'))


def copy():
    s=selected()
    clean_baseline()
    recheck(s['pins'],ROOT)
    changed=[]
    for rel,h in s['pins'].items():
        target=MIRROR/rel
        if target.exists() and sha(read(target))==h: continue
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT/rel,target)
        changed.append(rel)
    recheck(s['pins'],ROOT)
    recheck(s['pins'],MIRROR)
    emit('COPY.actual.json',{'status':'EXACT_SELECTION_COPIED_NOT_STAGED','selection_sha256':sha(read(OUT/'SELECTION.actual.json')),
         'selected_paths':len(s['pins']),'copied_paths':len(changed),'copied_names':changed})


def stage():
    s=selected()
    assert json.loads(read(OUT/'COPY.actual.json'))['status']=='EXACT_SELECTION_COPIED_NOT_STAGED'
    assert git('diff','--cached','--name-only')==b''
    assert git('rev-parse','HEAD').decode().strip()==BASE
    recheck(s['pins'],ROOT)
    recheck(s['pins'],MIRROR)
    names=sorted(s['pins'])
    ignored_raw=git('check-ignore','--stdin','-z',input=b''.join(p.encode()+b'\0' for p in names),allowed=(0,1))
    ignored=ignored_raw.decode().split('\0')[:-1]
    assert set(ignored)<=set(names)
    for force,group in [(False,[p for p in names if p not in set(ignored)]),(True,ignored)]:
        for start in range(0,len(group),200):
            git('add',*(['-f'] if force else []),'--',*group[start:start+200])
    raw=git('diff','--cached','--name-status','-z').decode().split('\0')[:-1]
    assert len(raw)%2==0
    staged={raw[i+1]:raw[i] for i in range(0,len(raw),2)}
    assert set(staged)<=set(names) and set(staged.values())<={'A','M'}
    tree=git('write-tree').decode().strip()
    allpins=dict(s['pins'])
    rows_count=0
    for m in s['named_manifests']:
        allpins[m['manifest']]=m['sha256']
        for rel,h in parse(read(ROOT/m['manifest'])).items():
            path=m['base']+'/'+rel
            assert path not in allpins or allpins[path]==h
            allpins[path]=h
            rows_count+=1
    argv=['git','-C',str(MIRROR),'cat-file','--batch']
    proc=subprocess.Popen(argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for path,h in sorted(allpins.items()):
        proc.stdin.write((tree+':'+path+'\n').encode()); proc.stdin.flush()
        header=proc.stdout.readline().decode().split()
        assert len(header)==3 and header[1]=='blob',(path,header)
        data=proc.stdout.read(int(header[2])); assert proc.stdout.read(1)==b'\n'
        assert sha(data)==h, path
    proc.stdin.close(); err=proc.stderr.read(); code=proc.wait()
    assert code==0 and err==b''
    COMMANDS.append({'argv':argv,'exit_code':code,'stdin_description':'tree:path for every explicit tree_pins key, sorted','blob_keys':len(allpins),'all_sha256_matched':True,'stderr':''})
    for m in s['named_manifests']:
        if not m['complete']: continue
        names_tree=set(git('ls-tree','-r','--name-only',tree,'--',m['base']+'/').decode().splitlines())
        expected={m['base']+'/'+p for p in parse(read(ROOT/m['manifest']))}|{m['manifest']}
        assert names_tree==expected,(m['manifest'],len(names_tree),len(expected))
    recheck(s['pins'],ROOT); recheck(s['pins'],MIRROR)
    assert git('diff','--name-only')==b''
    emit('STAGED_TREE.actual.json',{'schema':'p209-terminal-checkpoint-git-object-v1','status':'PASS_EXACT_SCOPED_STAGED_TREE_NOT_COMMITTED',
         'baseline':BASE,'tree':tree,'selected_paths':len(names),'staged_count':len(staged),'staged_paths':staged,
         'ignored_count':len(ignored),'ignored_paths':ignored,'named_manifest_count':len(s['named_manifests']),
         'manifest_rows_checked':rows_count,'tree_blob_keys_checked':len(allpins),'tree_pins':allpins,
         'selection_sha256':sha(read(OUT/'SELECTION.actual.json')),'scope':'Named original-base archival hashes only; P209 artifact pending; no new science/build/view.'})


if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('prepare','copy','stage')
    globals()[sys.argv[1]]()
