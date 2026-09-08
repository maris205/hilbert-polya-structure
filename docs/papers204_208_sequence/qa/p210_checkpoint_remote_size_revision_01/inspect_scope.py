#!/usr/bin/env python3
"""Read-only rejected-push diagnosis and captured-source corrective scope."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import time

HERE=Path(__file__).resolve().parent
QA=HERE.parent
SOURCE=Path('/root/autodl-tmp/symbolic_dynamics')
CAPSULE=Path('/root/symbolic-dynamics-private-sync-20260907')
MIRROR=Path('/root/autodl-tmp/hilbert-polya-structure')
EVIDENCE=Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
BARE=Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
ORIGINAL=QA/'p210_checkpoint_preparation'
BASE='a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
REJECTED='1f028072dc408a7d4404a7276f22f8666ba81801'
TREE='a26e19ee04c7a25fd0b0d00c67df784206baba4c'
EXCLUDED='docs/papers204_208_sequence/qa/p209_completion_private_checkpoint'
DISCLOSURE='docs/papers204_208_sequence/qa/P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json'


def dump(p,obj):
    with p.open('x') as f:
        json.dump(obj,f,sort_keys=True,indent=2)
        f.write('\n')


def sha(p):
    assert p.is_file() and not p.is_symlink(),str(p)
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()


def key(p):
    size=p.stat().st_size
    h=hashlib.sha256()
    g=hashlib.sha1(b'blob '+str(size).encode()+b'\0')
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
            g.update(b)
    return {'bytes':size,'sha256':h.hexdigest(),'git_blob_sha1':g.hexdigest(),
            'mode':'100755' if p.stat().st_mode&0o111 else '100644'}


def main():
    out=HERE/'inspection_01'
    out.mkdir()
    assert not BARE.exists()
    env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0',
             GIT_SSH_COMMAND='ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=20 -o ConnectionAttempts=1')
    commands=[]
    def git(repo,*args,stdin=b'',allowed=(0,)):
        argv=['git','-C',str(repo),*args]
        stem=out/f'command_{len(commands)+1:03d}'
        start=time.time()
        r=subprocess.run(argv,input=stdin,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env,timeout=45)
        for kind,data in (('stdin',stdin),('stdout',r.stdout),('stderr',r.stderr)):
            with stem.with_suffix('.'+kind+'.raw').open('xb') as f:
                f.write(data)
        rec={'argv':argv,'exit':r.returncode,'start_epoch':start,'end_epoch':time.time(),
             'stdin_sha256':sha(stem.with_suffix('.stdin.raw')),'stdout_sha256':sha(stem.with_suffix('.stdout.raw')),
             'stderr_sha256':sha(stem.with_suffix('.stderr.raw'))}
        dump(stem.with_suffix('.actual.json'),rec)
        commands.append(rec)
        assert r.returncode in allowed,(stem.name,r.returncode)
        return r.stdout
    assert git(MIRROR,'ls-remote','--exit-code','origin','refs/heads/main').decode().split()==[BASE,'refs/heads/main']
    failed=EVIDENCE/'push_revision_02/command_010.actual.json'
    native=json.loads(failed.read_text())
    assert native['exit']==1 and native['process_group_settlement']['quiescent']
    assert not native['process_group_settlement']['signals'] and not native['process_group_settlement']['remaining_members']
    assert sha(failed.parent/native['stderr']['path'])==native['stderr']['sha256']
    stderr=(failed.parent/native['stderr']['path']).read_text()
    assert 'GH001' in stderr and EXCLUDED+'/attempt_03/commit/command_014.stdout.raw.gz' in stderr
    assert not (EVIDENCE/'push_revision_02/RESULT.actual.json').exists()
    selected=json.loads((ORIGINAL/'preparation_01/SELECTED_PATHS.json').read_text())
    expected=json.loads((ORIGINAL/'preparation_01/EXPECTED_BLOBS.json').read_text())
    assert len(selected)==len(expected)==2318
    excluded=[r for r in selected if r['path'].startswith(EXCLUDED+'/')]
    retained=[r for r in selected if not r['path'].startswith(EXCLUDED+'/')]
    assert len(excluded)==306 and all(r['change']=='A' for r in excluded)
    unique={r['git_blob_sha1']:r for r in selected}
    stdin=b''.join((oid+'\n').encode() for oid in sorted(unique))
    headers=git(CAPSULE,'cat-file','--batch-check',stdin=stdin)
    assert headers==b''.join((oid+' blob '+str(unique[oid]['bytes'])+'\n').encode() for oid in sorted(unique))
    oversized=[r for r in selected if r['bytes']>100_000_000]
    assert oversized and all(r['path'].startswith(EXCLUDED+'/') for r in oversized)
    assert not [r for r in retained if r['bytes']>100_000_000]
    capsule_binding={'head':git(CAPSULE,'rev-parse','HEAD').decode().strip(),
                     'tracking':git(CAPSULE,'rev-parse','origin/main').decode().strip(),
                     'tree':git(CAPSULE,'rev-parse','HEAD^{tree}').decode().strip(),
                     'config_sha256':sha(CAPSULE/'.git/config'),'refs_sha256':hashlib.sha256(git(CAPSULE,'show-ref')).hexdigest(),
                     'index_sha256':sha(CAPSULE/'.git/index')}
    assert (capsule_binding['head'],capsule_binding['tracking'],capsule_binding['tree'])==(REJECTED,BASE,TREE)
    assert not git(CAPSULE,'status','--porcelain=v1','-z','--untracked-files=all')
    assert git(MIRROR,'rev-parse','HEAD').decode().strip()==BASE
    assert not git(MIRROR,'status','--porcelain=v1','-z','--untracked-files=all')
    original_binding={'config':sha(MIRROR/'.git/config'),'refs':hashlib.sha256(git(MIRROR,'show-ref')).hexdigest()}
    assert original_binding==json.loads((EVIDENCE/'preflight/ORIGINAL_MIRROR_BINDING.json').read_text())
    assert not git(MIRROR,'config','--get','core.worktree',allowed=(1,))
    for row in expected:
        assert key(CAPSULE/row['path'])=={k:row[k] for k in ('bytes','sha256','git_blob_sha1','mode')},row['path']
    physical={p.relative_to(CAPSULE).as_posix() for p in CAPSULE.rglob('*') if p.is_file() and '.git' not in p.relative_to(CAPSULE).parts}
    assert physical=={r['path'] for r in selected}
    disclosure={'status':'SCOPED_PRIVATE_BACKUP_DISCLOSURE_NOT_BATCH_COMPLETION','base_commit':BASE,
                'captured_source_commit':REJECTED,'captured_source_tree':TREE,
                'captured_source_role':'Immutable first overlay; current live workspace may have advanced.',
                'retained_prior_selected_paths':len(retained),'excluded_package':EXCLUDED,
                'excluded_path_count':len(excluded),'excluded_payload_bytes':sum(r['bytes'] for r in excluded),
                'excluded_paths':excluded,'reason':'The prior execution package contains a GitHub-rejected oversized raw gzip. This entire package is omitted from this replacement private checkpoint only; all original files and the rejected commit remain locally preserved.',
                'oversized_path_scan_threshold_bytes':100_000_000,'oversized_original_selected_paths':oversized,
                'retained_oversized_paths':[],'no_git_history_rewrite_or_force_push':True,
                'new_parent_is_base_not_rejected_commit':True,'scientific_scope_unchanged':'P210 Round0 checkpoint; later A/reuse/Round1/live-index changes are not included; HOLD_EXTERNAL.',
                'bare_worktree_and_status':'N/A: the new destination is bare; tree/index/ref gates remain mandatory.'}
    dump(HERE/'P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json',disclosure)
    extra={'path':DISCLOSURE,'change':'A',**key(HERE/'P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json')}
    new=sorted(retained+[extra],key=lambda r:r['path'])
    dump(HERE/'SELECTED_PATHS.json',new)
    dump(HERE/'EXCLUDED_PATHS.json',excluded)
    scope={'status':'CORRECTIVE_BARE_SCOPE_PREPARED_ONLY','base':BASE,'captured_source_commit':REJECTED,
           'captured_source_tree':TREE,'captured_source':str(CAPSULE),'new_bare':str(BARE),
           'new_evidence':str(EVIDENCE/'remote_size_revision_01'),'original_mirror':str(MIRROR),
           'selected_count':len(new),'additions':sum(r['change']=='A' for r in new),'modifications':4,
           'excluded_package':EXCLUDED,'excluded_count':len(excluded),'disclosure_path':DISCLOSURE,
           'selected_sha256':sha(HERE/'SELECTED_PATHS.json'),'excluded_sha256':sha(HERE/'EXCLUDED_PATHS.json'),
           'disclosure_sha256':sha(HERE/'P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json'),
           'capsule_binding':capsule_binding,'original_binding':original_binding,
           'retained_max_blob_bytes':max(r['bytes'] for r in new),'source_live_read_or_required':False,
           'bare_worktree_status':'N/A; bare repository, exact index/tree/ref checks required'}
    assert max(r['bytes'] for r in new)<100_000_000
    dump(HERE/'SCOPE.json',scope)
    pins=[]
    groups=[]
    for folder in [QA/n for n in ('p210_checkpoint_preparation','p210_checkpoint_stage_revision_01','p210_checkpoint_identity_revision_01')]+[EVIDENCE/n for n in ('preflight','clone','copy','stage','stage_revision_01_lock_preservation','stage_revision_01','commit_revision_01','commit_revision_02','push_revision_02')]:
        files=sorted(p for p in folder.rglob('*') if p.is_file())
        groups.append({'base':str(folder),'files':[p.relative_to(folder).as_posix() for p in files]})
        pins.extend({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files)
    for p in sorted(QA.glob('P210_CHECKPOINT_*.json')):
        pins.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
    dump(HERE/'PRESERVED_INPUT_PINS.json',pins)
    dump(HERE/'PRESERVED_GROUPS.json',groups)
    assert sha(CAPSULE/'.git/config')==capsule_binding['config_sha256'] and sha(CAPSULE/'.git/index')==capsule_binding['index_sha256']
    result={'status':'READ_ONLY_REMOTE_AND_ALL_RETAINED_SIZE_CHECK_PASS','new_readonly_native_commands':len(commands),
            'remote_confirmed':BASE,'rejected_commit_preserved':REJECTED,'captured_selected_paths_hashed':2318,
            'actual_unique_object_headers_checked':len(unique),'original_oversized_path_count':len(oversized),
            'excluded_paths':len(excluded),'excluded_bytes':sum(r['bytes'] for r in excluded),
            'new_selected_paths':len(new),'retained_max_blob_bytes':scope['retained_max_blob_bytes'],
            'preserved_input_pins':len(pins),'scope_sha256':sha(HERE/'SCOPE.json'),
            'new_git_writes':0,'moving_live_source_used':False}
    dump(out/'RESULT.actual.json',result)
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
