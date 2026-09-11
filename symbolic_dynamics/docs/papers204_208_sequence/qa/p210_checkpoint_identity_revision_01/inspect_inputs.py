#!/usr/bin/env python3
"""Read-only identity-failure inputs and accepted staged-tree preflight."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import time

HERE=Path(__file__).resolve().parent
QA=HERE.parent
OLD=QA/'p210_checkpoint_preparation'
REV=QA/'p210_checkpoint_stage_revision_01'
DEST=Path('/root/symbolic-dynamics-private-sync-20260907')
MIRROR=Path('/root/autodl-tmp/hilbert-polya-structure')
EVIDENCE=Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
BASE='a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
TREE='a26e19ee04c7a25fd0b0d00c67df784206baba4c'


def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()


def dump(p,obj):
    with p.open('x') as f:
        json.dump(obj,f,sort_keys=True,indent=2)
        f.write('\n')


def main():
    out=HERE/'inspection_01'
    out.mkdir()
    records=sorted((EVIDENCE/'commit_revision_01').glob('command_*.actual.json'))
    assert len(records)==8
    for i,p in enumerate(records,1):
        r=json.loads(p.read_text())
        assert r['exit']==(128 if i==8 else 0)
        g=r['process_group_settlement']
        assert g['quiescent'] and not g['signals'] and not g['remaining_members']
        assert g['native_returncode']==r['exit']
        for key in ('stdin','stdout','stderr'):
            assert sha(p.parent/r[key]['path'])==r[key]['sha256']
    failed=(EVIDENCE/'commit_revision_01/command_008.stderr.raw').read_text()
    assert 'Author identity unknown' in failed and 'unable to auto-detect email address' in failed
    assert not (EVIDENCE/'commit_revision_01/RESULT.actual.json').exists()
    source=QA/'P210_CHECKPOINT_EXISTING_IDENTITY_ROOT_READ.actual.json'
    identity_read=json.loads(source.read_text())
    values={}
    for row in identity_read['results']:
        assert row['result']['exit_code']==0
        origin,value=row['result']['output'].rstrip('\n').split('\t')
        assert origin=='file:/root/.gitconfig'
        values[row['key']]=value
    assert values=={'user.name':'mariswang','user.email':'wangliang.f@gmail.com'}
    stage=json.loads((EVIDENCE/'stage_revision_01/RESULT.actual.json').read_text())
    assert stage['status']=='PASS' and stage['tree']==TREE and stage['commands']==19
    assert stage['executor_sha256']=='497db8a936d1080523f9407799d3f9e094275ec18557c30f4307cf4c0babc1f8'
    pins=[]
    for folder in (EVIDENCE/'stage_revision_01',EVIDENCE/'commit_revision_01'):
        for p in sorted(folder.rglob('*')):
            if p.is_file():
                pins.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
    for p in [source,REV/'SHA256SUMS',REV/'execute.py',REV/'process_support.py']:
        pins.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
    dump(HERE/'IDENTITY_INPUT_PINS.json',pins)
    commands=[]
    env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0')
    def git(repo,*args):
        options=[]
        if repo==DEST:
            options=['-c','include.path='+str(MIRROR/'.git/config'),'-c','core.worktree='+str(DEST),
                     '-c','core.bare=false','-c','core.hooksPath='+str(EVIDENCE/'empty_hooks'),
                     '-c','core.fsmonitor=false','-c','gc.auto=0']
        argv=['git','-C',str(repo),*options,*args]
        stem=out/f'command_{len(commands)+1:03d}'
        start=time.time()
        r=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env,timeout=45)
        stem.with_suffix('.stdout.raw').write_bytes(r.stdout)
        stem.with_suffix('.stderr.raw').write_bytes(r.stderr)
        dump(stem.with_suffix('.actual.json'),{'argv':argv,'exit':r.returncode,'start_epoch':start,'end_epoch':time.time(),
             'stdout_sha256':sha(stem.with_suffix('.stdout.raw')),'stderr_sha256':sha(stem.with_suffix('.stderr.raw')),
             'environment_overrides_only':{'GIT_OPTIONAL_LOCKS':'0','GIT_TERMINAL_PROMPT':'0'}})
        assert r.returncode==0,(stem.name,r.returncode)
        commands.append(r.stdout)
        return r.stdout
    index_before=sha(DEST/'.git/index')
    assert git(DEST,'rev-parse','HEAD').decode().strip()==BASE
    assert git(DEST,'rev-parse','origin/main').decode().strip()==BASE
    assert not git(DEST,'diff','--cached','--name-status','-z',TREE,'--')
    changes=git(DEST,'diff','--cached','--name-status','-z','--no-renames',BASE,'--').split(b'\0')[:-1]
    selected=json.loads((OLD/'preparation_01/SELECTED_PATHS.json').read_text())
    assert len(changes)==2*2318
    assert {changes[i+1].decode():changes[i].decode() for i in range(0,len(changes),2)}=={r['path']:r['change'] for r in selected}
    assert git(MIRROR,'rev-parse','HEAD').decode().strip()==BASE
    assert not git(MIRROR,'status','--porcelain=v1','-z','--untracked-files=all')
    binding=json.loads((EVIDENCE/'preflight/ORIGINAL_MIRROR_BINDING.json').read_text())
    assert binding=={'config':sha(MIRROR/'.git/config'),'refs':hashlib.sha256(git(MIRROR,'show-ref')).hexdigest()}
    assert index_before==sha(DEST/'.git/index') and not (DEST/'.git/index.lock').exists()
    for row in pins:
        assert sha(Path(row['path']))==row['sha256']
    result={'status':'READ_ONLY_IDENTITY_FAILURE_AND_ACCEPTED_STAGE_INPUTS_PASS','identity':values,
            'identity_read_sha256':sha(source),'identity_input_pins_sha256':sha(HERE/'IDENTITY_INPUT_PINS.json'),
            'identity_input_pins':len(pins),'failed_native_commands_checked':8,'new_readonly_commands':len(commands),
            'accepted_stage_tree':TREE,'index_identical_to_accepted_stage':True,'exact_staged_changes':2318,
            'current_commit':BASE,'original_mirror_unchanged':True,'index_sha256':index_before,
            'git_config_writes':0,'commit_push_or_executor_execution':0}
    dump(out/'RESULT.actual.json',result)
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
