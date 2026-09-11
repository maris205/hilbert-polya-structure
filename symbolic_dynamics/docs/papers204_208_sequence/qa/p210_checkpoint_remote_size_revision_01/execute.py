#!/usr/bin/env python3
"""UNEXECUTED root-approved new bare checkpoint; preserve rejected overlay.

Build one ordinary child of the old remote base from exact captured blob keys,
omitting the entire disclosed oversized prior execution package. No worktree.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import os
import traceback

HERE=Path(__file__).resolve().parent
QA=HERE.parent
SOURCE=Path('/root/autodl-tmp/symbolic_dynamics')
CAPSULE=Path('/root/symbolic-dynamics-private-sync-20260907')
MIRROR=Path('/root/autodl-tmp/hilbert-polya-structure')
BARE=Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
OLD_EVIDENCE=Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
EVIDENCE=OLD_EVIDENCE/'remote_size_revision_01'
BASE='a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
REJECTED='1f028072dc408a7d4404a7276f22f8666ba81801'
SUPPORT=QA/'p210_checkpoint_stage_revision_01/process_support.py'
SUPPORT_SHA='8ce99e3b7684123c5a04d99d8fa5cee98bd4e8e8b9bca7f7a4dd5dc93b5dde7c'


def sha(p):
    assert p.is_file() and not p.is_symlink(),str(p)
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()


def dump(p,obj):
    with p.open('x') as f:
        json.dump(obj,f,sort_keys=True,indent=2)
        f.write('\n')


def file_key(p):
    size=p.stat().st_size
    h=hashlib.sha256()
    g=hashlib.sha1(b'blob '+str(size).encode()+b'\0')
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
            g.update(b)
    assert not p.is_symlink() and p.stat().st_size==size
    return {'bytes':size,'sha256':h.hexdigest(),'git_blob_sha1':g.hexdigest(),
            'mode':'100755' if p.stat().st_mode&0o111 else '100644'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase',choices=('build','push'))
    ap.add_argument('--approval',required=True,type=Path)
    args=ap.parse_args()
    assert os.getcwd()==str(SOURCE) and not any(k.startswith('GIT_') for k in os.environ)
    scope=json.loads((HERE/'SCOPE.json').read_text())
    approval=json.loads(args.approval.read_text())
    assert approval['status']=='ROOT_APPROVED_P210_REMOTE_SIZE_REVISION_01'
    assert approval['executor_sha256']==sha(Path(__file__))
    assert approval['scope_sha256']==sha(HERE/'SCOPE.json')
    assert approval['preparation_seal_sha256']==sha(HERE/'SHA256SUMS')
    assert approval['preserved_input_pins_sha256']==sha(HERE/'PRESERVED_INPUT_PINS.json')
    assert approval['process_support_sha256']==sha(SUPPORT)==SUPPORT_SHA
    assert approval['new_bare']==str(BARE) and approval['new_evidence']==str(EVIDENCE)
    assert approval['captured_source']==str(CAPSULE) and approval['rejected_commit_preserved']==REJECTED
    assert approval['approved_phases']==['build','push']
    assert approval['allow_exact_bare_index_commit_tree_and_normal_ref_updates'] is True
    assert approval['allow_readonly_object_alternates_and_origin_config_include'] is True
    assert approval['commit_identity']=={'user.name':'mariswang','user.email':'wangliang.f@gmail.com'}
    assert scope['base']==BASE and scope['captured_source_commit']==REJECTED and scope['source_live_read_or_required'] is False
    assert scope['selected_sha256']==sha(HERE/'SELECTED_PATHS.json') and scope['excluded_sha256']==sha(HERE/'EXCLUDED_PATHS.json')
    selected=json.loads((HERE/'SELECTED_PATHS.json').read_text())
    excluded=json.loads((HERE/'EXCLUDED_PATHS.json').read_text())
    assert len(selected)==2013 and len(excluded)==306 and all(r['change']=='A' for r in excluded)
    assert not {r['path'] for r in selected}&{r['path'] for r in excluded}
    assert all(r['bytes']<100_000_000 for r in selected)
    assert not any(r['path'].startswith(scope['excluded_package']+'/') for r in selected)
    disclosure=HERE/'P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json'
    assert sha(disclosure)==scope['disclosure_sha256']
    old=json.loads((QA/'p210_checkpoint_preparation/preparation_01/EXPECTED_BLOBS.json').read_text())
    pins=json.loads((HERE/'PRESERVED_INPUT_PINS.json').read_text())
    groups=json.loads((HERE/'PRESERVED_GROUPS.json').read_text())
    assert BARE.parent==Path('/root') and EVIDENCE.parent==OLD_EVIDENCE
    assert not BARE.is_symlink() and not EVIDENCE.is_symlink()
    if args.phase=='build':
        assert not BARE.exists() and not EVIDENCE.exists()
        EVIDENCE.mkdir()
    else:
        previous=json.loads((EVIDENCE/'build/RESULT.actual.json').read_text())
        assert previous['status']=='PASS' and previous['executor_sha256']==approval['executor_sha256']
    phase=EVIDENCE/args.phase
    phase.mkdir()
    dump(phase/'APPROVAL_BINDING.actual.json',{'approval_path':str(args.approval.resolve()),'approval_sha256':sha(args.approval),'approval':approval})
    spec=importlib.util.spec_from_file_location('p210_bare_process_support',SUPPORT)
    support=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(support)
    env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0',
             GIT_SSH_COMMAND='ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=20 -o ConnectionAttempts=1')
    commands=[]
    def command(argv,stdin=b'',allowed=(0,),timeout=300):
        stem=phase/f'command_{len(commands)+1:03d}'
        inp,out,err=[stem.with_suffix('.'+key+'.raw') for key in ('stdin','stdout','stderr')]
        with inp.open('xb') as f:
            f.write(stdin)
        native=support.run_files(argv,inp,out,err,env,timeout=timeout)
        rec={'argv':argv,'cwd':str(SOURCE),**native,'stdin_sha256':sha(inp),'stdout_sha256':sha(out),'stderr_sha256':sha(err)}
        dump(stem.with_suffix('.actual.json'),rec)
        commands.append(rec)
        assert native['exit'] in allowed and native['process_group_settlement']['quiescent']
        assert not native['process_group_settlement']['signals']
        return out.read_bytes()
    def git(repo,*args,**kwargs):
        options=[]
        if repo==BARE:
            options=['-c','include.path='+str(MIRROR/'.git/config'),'-c','core.bare=true',
                     '-c','core.hooksPath='+str(OLD_EVIDENCE/'empty_hooks'),'-c','core.fsmonitor=false',
                     '-c','core.sparseCheckout=false','-c','core.splitIndex=false','-c','gc.auto=0',
                     '-c','commit.gpgSign=false','-c','user.name=mariswang','-c','user.email=wangliang.f@gmail.com']
        return command(['git','-C',str(repo),*options,*args],**kwargs)
    def preserve():
        for row in pins:
            p=Path(row['path'])
            assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],str(p)
        for group in groups:
            base=Path(group['base'])
            assert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}==set(group['files'])
        for row in old:
            assert file_key(CAPSULE/row['path'])=={k:row[k] for k in ('bytes','sha256','git_blob_sha1','mode')}
        physical={p.relative_to(CAPSULE).as_posix() for p in CAPSULE.rglob('*') if p.is_file() and '.git' not in p.relative_to(CAPSULE).parts}
        assert physical=={r['path'] for r in old}
        binding=scope['capsule_binding']
        assert git(CAPSULE,'rev-parse','HEAD').decode().strip()==REJECTED
        assert git(CAPSULE,'rev-parse','origin/main').decode().strip()==BASE
        assert hashlib.sha256(git(CAPSULE,'show-ref')).hexdigest()==binding['refs_sha256']
        assert sha(CAPSULE/'.git/config')==binding['config_sha256'] and sha(CAPSULE/'.git/index')==binding['index_sha256']
        assert not git(CAPSULE,'status','--porcelain=v1','-z','--untracked-files=all')
        assert git(MIRROR,'rev-parse','HEAD').decode().strip()==BASE
        assert not git(MIRROR,'status','--porcelain=v1','-z','--untracked-files=all')
        assert {'config':sha(MIRROR/'.git/config'),'refs':hashlib.sha256(git(MIRROR,'show-ref')).hexdigest()}==scope['original_binding']
        residue=json.loads((QA/'p210_checkpoint_stage_revision_01/FAILED_RESIDUE_PINS.actual.json').read_text())
        for i,row in enumerate(residue['pins']):
            p=Path(residue['proposed_lock_archive'] if i==0 else row['path'])
            s=p.stat()
            assert s.st_size==row['bytes'] and sha(p)==row['sha256']
            assert (s.st_dev,s.st_ino,s.st_mode,s.st_mtime_ns)==(row['device'],row['inode'],row['mode'],row['mtime_ns'])
        assert not (CAPSULE/'.git/index.lock').exists()
        assert sha(CAPSULE/'.git/index')==binding['index_sha256']
    def remote(repo,expected):
        assert git(repo,'ls-remote','--exit-code','origin','refs/heads/main').decode().split()==[expected,'refs/heads/main']
    def tree_check(tree):
        old_scope=json.loads((QA/'p210_checkpoint_preparation/preparation_01/SCOPE.json').read_text())
        prefixes=[p['base'] for p in old_scope['packages'] if p['base']!=scope['excluded_package']]+old_scope['exact_extra_paths']+[scope['disclosure_path']]
        data=git(BARE,'ls-tree','-r','-z','--full-tree',tree,'--',*prefixes)
        got={}
        for raw in data.split(b'\0')[:-1]:
            attrs,name=raw.split(b'\t',1)
            mode,kind,oid=attrs.decode().split()
            assert kind=='blob' and name.decode() not in got
            got[name.decode()]=(mode,oid)
        assert got=={r['path']:(r['mode'],r['git_blob_sha1']) for r in selected}
        changes=git(BARE,'diff','--name-status','-z','--no-renames',BASE,tree,'--').split(b'\0')[:-1]
        assert len(changes)==2*len(selected)
        assert {changes[i+1].decode():changes[i].decode() for i in range(0,len(changes),2)}=={r['path']:r['change'] for r in selected}
        assert not git(BARE,'ls-tree','-r',tree,'--',scope['excluded_package'])
        unique={r['git_blob_sha1']:r for r in selected}
        stdin=b''.join((oid+'\n').encode() for oid in sorted(unique))
        assert git(BARE,'cat-file','--batch-check',stdin=stdin)==b''.join((oid+' blob '+str(unique[oid]['bytes'])+'\n').encode() for oid in sorted(unique))
        return len(unique)
    try:
        preserve()
        if args.phase=='build':
            remote(MIRROR,BASE)
            command(['git','init','--bare','--initial-branch=main',str(BARE)])
            alternate=(str(CAPSULE/'.git/objects')+'\n'+str(MIRROR/'.git/objects')+'\n').encode()
            with (BARE/'objects/info/alternates').open('xb') as f:
                f.write(alternate)
            git(BARE,'update-ref','refs/heads/main',BASE)
            assert git(BARE,'rev-parse','HEAD').decode().strip()==BASE
            git(BARE,'read-tree',BASE)
            oid=git(BARE,'hash-object','-w','--no-filters',str(disclosure)).decode().strip()
            assert oid==next(r['git_blob_sha1'] for r in selected if r['path']==scope['disclosure_path'])
            assert git(BARE,'cat-file','blob',oid)==disclosure.read_bytes()
            index_input=b''.join((r['mode']+' '+r['git_blob_sha1']+'\t'+r['path']).encode()+b'\0' for r in selected)
            git(BARE,'update-index','-z','--index-info',stdin=index_input)
            tree=git(BARE,'write-tree').decode().strip()
            unique_count=tree_check(tree)
            message=b'Private P210 Round0 checkpoint with disclosed prior execution-package exclusion; HOLD_EXTERNAL\n'
            commit=git(BARE,'commit-tree',tree,'-p',BASE,stdin=message).decode().strip()
            assert git(BARE,'rev-list','--parents','-n','1',commit).decode().split()==[commit,BASE]
            assert git(BARE,'rev-parse',commit+'^{tree}').decode().strip()==tree
            identity=git(BARE,'show','-s','--format=%an%x00%ae%x00%cn%x00%ce',commit).decode().rstrip('\n').split('\0')
            assert identity==['mariswang','wangliang.f@gmail.com','mariswang','wangliang.f@gmail.com']
            git(BARE,'update-ref','refs/heads/main',commit,BASE)
            assert git(BARE,'rev-parse','HEAD').decode().strip()==commit
            assert not git(BARE,'diff','--cached','--name-status','-z',commit,'--')
            assert git(BARE,'rev-parse','--is-bare-repository').strip()==b'true'
            result={'commit':commit,'tree':tree,'unique_selected_objects':unique_count,'normal_single_parent':BASE}
        else:
            commit,tree=previous['commit'],previous['tree']
            assert git(BARE,'rev-parse','HEAD').decode().strip()==commit
            assert git(BARE,'rev-parse','--is-bare-repository').strip()==b'true'
            tree_check(commit)
            remote(BARE,BASE)
            git(BARE,'push','origin',commit+':refs/heads/main')
            remote(BARE,commit)
            git(BARE,'fetch','--no-tags','origin','refs/heads/main:refs/remotes/origin/main')
            assert git(BARE,'rev-list','--left-right','--count','HEAD...origin/main').split()==[b'0',b'0']
            assert not git(BARE,'diff','--cached','--name-status','-z',commit,'--')
            result={'commit':commit,'tree':tree,'actual_remote_confirmed':True,'divergence':[0,0]}
        preserve()
        result.update(status='PASS',phase=args.phase,executor_sha256=approval['executor_sha256'],scope_sha256=approval['scope_sha256'],
                      base=BASE,captured_source_preserved=REJECTED,selected_paths=2013,excluded_paths=306,commands=len(commands),
                      moving_live_source_used=False,bare_worktree_status='N/A: bare; exact index/tree/ref checks passed',
                      no_rejected_commit_ancestry=True,new_object_body_capture_bytes=0)
        dump(phase/'RESULT.actual.json',result)
        print(json.dumps(result,sort_keys=True))
    except BaseException:
        dump(phase/'FAILURE.actual.json',{'phase':args.phase,'completed_commands':len(commands),'exception':traceback.format_exc(),
             'no_cleanup_or_automatic_retry':True,'rejected_capsule_not_a_mutation_target':True})
        raise


if __name__=='__main__':
    main()
