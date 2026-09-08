#!/usr/bin/env python3
"""Read-only failed-stage/current index inspection; only writes this new prep."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import time

HERE = Path(__file__).resolve().parent
SOURCE = Path('/root/autodl-tmp/symbolic_dynamics')
ORIGINAL = SOURCE/'docs/papers204_208_sequence/qa/p210_checkpoint_preparation'
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
DEST = Path('/root/symbolic-dynamics-private-sync-20260907')
EVIDENCE = Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'


def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()


def dump(p, obj):
    with p.open('x') as f:
        json.dump(obj,f,sort_keys=True,indent=2)
        f.write('\n')


def file_state(p):
    if not p.exists():
        return {'path':str(p),'exists':False}
    st=p.stat()
    assert p.is_file() and not p.is_symlink()
    return {'path':str(p),'exists':True,'bytes':st.st_size,'sha256':sha(p),
            'inode':st.st_ino,'device':st.st_dev,'mode':st.st_mode,'mtime_ns':st.st_mtime_ns}


def owned_processes():
    """No environment reads. Retain argv only for the exact known failed Git."""
    failed=json.loads((EVIDENCE/'stage/command_007.actual.json').read_text())['argv']
    hits=[]
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            comm=(proc/'comm').read_text().strip()
            if comm not in ('git','git-remote-https','git-remote-http','ssh','index-pack','pack-objects'):
                continue
            argv=(proc/'cmdline').read_bytes().split(b'\0')[:-1]
            cwd=os.readlink(proc/'cwd')
            direct=str(DEST).encode() in argv or cwd==str(DEST)
            fds=[]
            for fd in (proc/'fd').iterdir():
                try:
                    target=os.readlink(fd)
                    if target.startswith(str(DEST)+'/.git/'):
                        fds.append({'fd':fd.name,'target':target})
                except (OSError,PermissionError):
                    pass
            if direct or fds:
                stat=(proc/'stat').read_text()
                tail=stat[stat.rfind(')')+2:].split()
                decoded=[x.decode(errors='replace') for x in argv]
                hits.append({'pid':int(proc.name),'comm':comm,'cwd':cwd,'state':tail[0],
                             'ppid':int(tail[1]),'pgid':int(tail[2]),'sid':int(tail[3]),
                             'start_ticks':int(tail[19]),'argv_exact_failed_command':decoded==failed,
                             'argv':decoded if decoded==failed else '[not displayed; nonidentical argv]',
                             'argv_sha256':hashlib.sha256(b'\0'.join(argv)).hexdigest(),'owned_fds':fds})
        except (OSError,PermissionError,ProcessLookupError):
            continue
    return hits


def main():
    out=HERE/'inspection_01'
    out.mkdir()
    selected=json.loads((ORIGINAL/'preparation_01/SELECTED_PATHS.json').read_text())
    expected=json.loads((ORIGINAL/'preparation_01/EXPECTED_BLOBS.json').read_text())
    scope=json.loads((ORIGINAL/'preparation_01/SCOPE.json').read_text())
    rows={r['path']:r for r in selected}
    before={'index':file_state(DEST/'.git/index'),'index_lock':file_state(DEST/'.git/index.lock'),
            'processes':owned_processes(),'epoch':time.time()}
    dump(out/'BEFORE.actual.json',before)
    assert not before['processes'], 'owned process still live: root must settle it before further stable-state claims'
    original_pins=[]
    for line in (ORIGINAL/'SHA256SUMS').read_text().splitlines():
        h,name=line.split('  ',1)
        assert sha(ORIGINAL/name)==h,name
        original_pins.append({'path':str(ORIGINAL/name),'bytes':(ORIGINAL/name).stat().st_size,'sha256':h})
    assert len(original_pins)==103 and sha(ORIGINAL/'SHA256SUMS')=='94dd0c398aa4d91eaf809d56e0e0ea7d5f7f8d6129a111d37e4aca6c75dd7285'
    original_pins.append({'path':str(ORIGINAL/'SHA256SUMS'),'bytes':(ORIGINAL/'SHA256SUMS').stat().st_size,'sha256':sha(ORIGINAL/'SHA256SUMS')})
    native_count=0
    for name,count in [('preflight',12),('clone',19),('copy',10),('stage',7)]:
        phase=EVIDENCE/name
        records=sorted(phase.glob('command_*.actual.json'))
        assert len(records)==count
        for i,rp in enumerate(records,1):
            rec=json.loads(rp.read_text())
            assert rp.name==f'command_{i:03d}.actual.json'
            assert rec['exit']==('TIMEOUT' if name=='stage' and i==7 else 0)
            for key in ('stdout','stderr'):
                p=phase/rec[key]['path']
                assert sha(p)==rec[key]['sha256'],str(p)
            if name=='stage' and i==7:
                ordinary=(phase/'command_007.stdin.raw').read_bytes().split(b'\0')[:-1]
                assert {x.decode() for x in ordinary}==set(rows)-set(scope['ignored_selected_paths'])
                assert len(ordinary)==2138
                assert 60<=rec['ended_epoch']-rec['started_epoch']<62
                assert not (phase/'command_007.stdout.raw').read_bytes() and not (phase/'command_007.stderr.raw').read_bytes()
            native_count+=1
        for p in sorted(phase.rglob('*')):
            if p.is_file():
                original_pins.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
    failure=json.loads((EVIDENCE/'stage/FAILURE.actual.json').read_text())
    assert failure['completed_commands']==7 and failure['executor_sha256']=='8d42285eeebcfc23c145da9b0bf6bb8b82b2db1f04533f5d73c145665f4cdcba'
    assert not (EVIDENCE/'stage/RESULT.actual.json').exists() and not (EVIDENCE/'commit').exists() and not (EVIDENCE/'push').exists()
    original_pins.append({'path':str(SOURCE/'docs/papers204_208_sequence/qa/P210_CHECKPOINT_STAGE_ROOT_COMPLETION.actual.json'),
                          'sha256':sha(SOURCE/'docs/papers204_208_sequence/qa/P210_CHECKPOINT_STAGE_ROOT_COMPLETION.actual.json')})
    dump(out/'ORIGINAL_INPUT_PINS.json',original_pins)
    commands=[]
    env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0',GIT_LITERAL_PATHSPECS='0')
    def git(repo,*args):
        options=[]
        if repo==DEST:
            options=['-c','include.path='+str(MIRROR/'.git/config'),'-c','core.worktree='+str(DEST),
                     '-c','core.bare=false','-c','core.hooksPath='+str(EVIDENCE/'empty_hooks'),
                     '-c','core.fsmonitor=false','-c','gc.auto=0']
        argv=['git','-C',str(repo),*options,*args]
        stem=out/f'command_{len(commands)+1:03d}'
        start=time.time()
        p=subprocess.run(argv,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=45)
        stem.with_suffix('.stdout.raw').write_bytes(p.stdout)
        stem.with_suffix('.stderr.raw').write_bytes(p.stderr)
        dump(stem.with_suffix('.actual.json'),{'argv':argv,'exit':p.returncode,'start_epoch':start,'end_epoch':time.time(),
             'stdout_sha256':sha(stem.with_suffix('.stdout.raw')),'stderr_sha256':sha(stem.with_suffix('.stderr.raw')),
             'environment_overrides_only':{k:env[k] for k in ('GIT_OPTIONAL_LOCKS','GIT_TERMINAL_PROMPT','GIT_LITERAL_PATHSPECS')}})
        assert p.returncode==0,(stem.name,p.returncode)
        commands.append(p.stdout)
        return p.stdout
    assert git(MIRROR,'rev-parse','HEAD').decode().strip()==BASE
    assert git(MIRROR,'rev-parse','origin/main').decode().strip()==BASE
    assert not git(MIRROR,'status','--porcelain=v1','-z','--untracked-files=all')
    binding=json.loads((EVIDENCE/'preflight/ORIGINAL_MIRROR_BINDING.json').read_text())
    assert binding=={'config':sha(MIRROR/'.git/config'),'refs':hashlib.sha256(git(MIRROR,'show-ref')).hexdigest()}
    assert git(DEST,'rev-parse','HEAD').decode().strip()==BASE
    assert git(DEST,'rev-parse','origin/main').decode().strip()==BASE
    index_raw=git(DEST,'ls-files','--stage','-z')
    baseline_raw=git(DEST,'ls-tree','-r','-z','--full-tree',BASE)
    index,baseline={},{}
    for raw in index_raw.split(b'\0'):
        if raw:
            attrs,name=raw.split(b'\t',1)
            mode,oid,stage=attrs.decode().split()
            assert stage=='0','unmerged index'
            index[name.decode()]=(mode,oid)
    for raw in baseline_raw.split(b'\0'):
        if raw:
            attrs,name=raw.split(b'\t',1)
            mode,kind,oid=attrs.decode().split()
            assert kind=='blob',('unexpected nonblob baseline',name.decode())
            baseline[name.decode()]=(mode,oid)
    changed={p for p in set(index)|set(baseline) if index.get(p)!=baseline.get(p)}
    assert changed<=set(rows),'unrelated index change'
    assert all(index.get(p)==(rows[p]['mode'],rows[p]['git_blob_sha1']) for p in changed),'partial index differs from exact intended blob'
    diff=git(DEST,'diff','--cached','--name-status','-z','--no-renames',BASE,'--').split(b'\0')[:-1]
    assert len(diff)==2*len(changed)
    assert {diff[i+1].decode():diff[i].decode() for i in range(0,len(diff),2)}=={p:rows[p]['change'] for p in changed}
    status=git(DEST,'status','--porcelain=v1','-z','--untracked-files=all')
    git(DEST,'count-objects','-v')
    for row in expected:
        for base in (SOURCE,DEST):
            p=base/row['path']
            assert p.is_file() and not p.is_symlink() and p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],str(p)
    after={'index':file_state(DEST/'.git/index'),'index_lock':file_state(DEST/'.git/index.lock'),
           'processes':owned_processes(),'epoch':time.time()}
    dump(out/'AFTER.actual.json',after)
    assert before['index']==after['index'] and before['index_lock']==after['index_lock'] and not after['processes']
    for p in original_pins:
        assert sha(Path(p['path']))==p['sha256'],p['path']
    result={'status':'READ_ONLY_FAILURE_AND_PARTIAL_INDEX_INSPECTION_PASS','original_native_commands':native_count,
            'new_readonly_commands':len(commands),'original_input_pins':len(original_pins),
            'original_mirror_unchanged':True,'overlay_head':BASE,'partial_index_changed_count':len(changed),
            'partial_index_exact_subset':True,'unrelated_index_changes':0,'unmerged_entries':0,
            'index_entries':len(index),'baseline_entries':len(baseline),'source_overlay_exact_files':len(expected),
            'source_overlay_payload_bytes_each':sum(r['bytes'] for r in expected),'stable_index':after['index'],
            'stable_index_lock':after['index_lock'],'owned_processes_before_after':0,
            'retained_stage_failure':'TIMEOUT at ordinary add; no forced add/tree/object audit/commit/push executed',
            'lock_removed_or_moved':False,'git_mutations':0}
    dump(out/'RESULT.actual.json',result)
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
