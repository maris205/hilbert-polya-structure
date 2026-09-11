#!/usr/bin/env python3
"""Root-only read-only captured-source and successful bare-checkpoint receiver."""
from pathlib import Path
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
import re
import time
import traceback

HERE=Path(__file__).resolve().parent
QA=HERE.parent
SOURCE=Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR=Path('/root/autodl-tmp/hilbert-polya-structure')
DEST=Path('/root/symbolic-dynamics-private-sync-20260907')
BARE=Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
EVIDENCE=Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
NEWEXEC=EVIDENCE/'remote_size_revision_01'
ORIGINAL=QA/'p210_checkpoint_preparation'
REV=QA/'p210_checkpoint_stage_revision_01'
IDENTITY=QA/'p210_checkpoint_identity_revision_01'
SIZEPREP=QA/'p210_checkpoint_remote_size_revision_01'
PREP=ORIGINAL/'preparation_01'
BASE='a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
REJECTED='1f028072dc408a7d4404a7276f22f8666ba81801'
TREE='a26e19ee04c7a25fd0b0d00c67df784206baba4c'
SCOPE_SHA='bf8e4f358cb175374eec840d02894beecbeda722e6b9e559dc75ee899d49eb0e'
SUPPORT_SHA='8ce99e3b7684123c5a04d99d8fa5cee98bd4e8e8b9bca7f7a4dd5dc93b5dde7c'
PHASES=('preflight','clone','copy','stage','stage_revision_01','commit_revision_01','commit_revision_02','push_revision_02')
OUT=NEWEXEC/'root_receiver_01'


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


def manifest(base,name,expected_sha=None):
    p=base/name
    if expected_sha is not None:
        assert sha(p)==expected_sha,str(p)
    rows={}
    for line in p.read_text().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  ([^\r\n]+)',line)
        assert m,line
        digest,rel=m.groups()
        assert rel!=name and not rel.startswith('/') and '..' not in Path(rel).parts
        assert rel not in rows and (base/rel).resolve().is_relative_to(base.resolve())
        rows[rel]=digest
        assert sha(base/rel)==digest,str(base/rel)
    physical={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
    assert physical==set(rows)|{name},str(base)
    return rows


def file_key(p):
    assert p.is_file() and not p.is_symlink(),str(p)
    size=p.stat().st_size
    h=hashlib.sha256()
    g=hashlib.sha1(b'blob '+str(size).encode()+b'\0')
    count=0
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
            g.update(b)
            count+=len(b)
    assert size==count==p.stat().st_size
    return {'bytes':size,'sha256':h.hexdigest(),'git_blob_sha1':g.hexdigest(),
            'mode':'100755' if p.stat().st_mode&0o111 else '100644'}


def tree_rows(data):
    rows={}
    assert not data or data.endswith(b'\0')
    for raw in data.split(b'\0')[:-1]:
        attrs,name=raw.split(b'\t',1)
        mode,kind,oid=attrs.decode().split()
        assert kind=='blob' and name.decode() not in rows
        rows[name.decode()]=(mode,oid)
    return rows


def change_rows(data):
    fields=data.split(b'\0')[:-1]
    assert (not data or data.endswith(b'\0')) and len(fields)%2==0
    rows={fields[i+1].decode():fields[i].decode() for i in range(0,len(fields),2)}
    assert 2*len(rows)==len(fields)
    return rows


def preserved_inputs(config,pins):
    for row in pins:
        p=Path(row['path'])
        assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],str(p)
    for group in config['physical_groups']:
        base=Path(group['base'])
        current={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
        assert current==set(group['files']),str(base)
    for pinfile,count in ((REV/'inspection_01/ORIGINAL_INPUT_PINS.json',266),
                          (IDENTITY/'IDENTITY_INPUT_PINS.json',118),
                          (SIZEPREP/'PRESERVED_INPUT_PINS.json',624)):
        rows=json.loads(pinfile.read_text())
        assert len(rows)==count
        for row in rows:
            assert sha(Path(row['path']))==row['sha256'],row['path']
    residue=json.loads((REV/'FAILED_RESIDUE_PINS.actual.json').read_text())
    receipt=EVIDENCE/'stage_revision_01_lock_preservation/ROOT_PRESERVATION.actual.json'
    assert sha(receipt)=='208b59678887f7741403dc3110d0585f10b730ceca94788203d3bc92403fa00e'
    lock=json.loads(receipt.read_text())
    assert lock['source_pin']==residue['pins'][0] and lock['no_deleted_bytes'] is True
    assert lock['preserved_path']==residue['proposed_lock_archive']
    for i,row in enumerate(residue['pins']):
        p=Path(lock['preserved_path'] if i==0 else row['path'])
        s=p.stat()
        assert sha(p)==row['sha256'] and s.st_size==row['bytes']
        assert (s.st_dev,s.st_ino,s.st_mode,s.st_mtime_ns)==(row['device'],row['inode'],row['mode'],row['mtime_ns'])
    assert not (DEST/'.git/index.lock').exists()


def native_record(p):
    r=json.loads(p.read_text())
    assert isinstance(r['argv'],list) and r['argv']
    assert type(r['exit']) is int or r['exit']=='TIMEOUT'
    if 'process_group_settlement' in r:
        g=r['process_group_settlement']
        assert g['quiescent'] and not g['signals'] and not g['remaining_members']
        assert g['native_returncode']==r['exit'] and g['owned_pgid']==g['owned_sid']
    for key in ('stdin','stdout','stderr'):
        if isinstance(r.get(key),dict):
            assert sha(p.parent/r[key]['path'])==r[key]['sha256']
        elif key+'_sha256' in r:
            if key=='stdout' and 'stdout_lossless_gzip' in r:
                continue
            raw=p.parent/(p.name.removesuffix('.actual.json')+'.'+key+'.raw')
            if p.name in ('SOURCE_DIFF_NATIVE.actual.json','SOURCE_DELTA.actual.json'):
                raw=p.parent/('SOURCE_DELTA.diff' if key=='stdout' else 'SOURCE_DELTA.stderr.raw')
            assert sha(raw)==r[key+'_sha256'],str(raw)
            if key+'_bytes' in r:
                assert raw.stat().st_size==r[key+'_bytes']
    if 'stdout_lossless_gzip' in r:
        raw=p.parent/r['stdout_lossless_gzip']
        assert sha(raw)==r['gzip_sha256'] and raw.stat().st_size==r['gzip_bytes']
    return r


def decode_objects(p,r,unique):
    stream=hashlib.sha256()
    total=payload=0
    keys=[]
    with gzip.open(p,'rb') as f:
        def take(n):
            nonlocal total
            b=f.read(n)
            total+=len(b)
            stream.update(b)
            return b
        for oid,row in sorted(unique.items()):
            header=(oid+' blob '+str(row['bytes'])+'\n').encode()
            assert take(len(header))==header,oid
            h=hashlib.sha256()
            g=hashlib.sha1(b'blob '+str(row['bytes']).encode()+b'\0')
            left=row['bytes']
            while left:
                b=take(min(left,1024*1024))
                assert b,oid
                h.update(b)
                g.update(b)
                left-=len(b)
            assert take(1)==b'\n' and h.hexdigest()==row['sha256'] and g.hexdigest()==oid,oid
            payload+=row['bytes']
            keys.append({'git_blob_sha1':oid,'bytes':row['bytes'],'sha256':h.hexdigest()})
        assert not take(1)
    assert total==r['raw_stream_bytes']==658641270 and stream.hexdigest()==r['raw_stream_sha256']
    assert payload==r['verified_payload_bytes']==658584369 and len(keys)==r['unique_blob_count']==1096
    return {'path':str(p),'raw_bytes':total,'raw_sha256':stream.hexdigest(),'payload_bytes':payload,'keys':keys}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--seal-sha256',required=True)
    args=ap.parse_args()
    assert os.getcwd()==str(SOURCE) and not any(k.startswith('GIT_') for k in os.environ)
    manifest(HERE,'SHA256SUMS',args.seal_sha256)
    config=json.loads((HERE/'INPUT_BINDING.json').read_text())
    pins=json.loads((HERE/'INPUT_PINS.json').read_text())
    assert config['status']=='PREPARED_AFTER_ACTUAL_BARE_PUSH_ROOT_EXECUTION_REQUIRED'
    assert config['receiver_sha256']==sha(Path(__file__)) and config['input_pins_sha256']==sha(HERE/'INPUT_PINS.json')
    assert config['baseline']==BASE and config['captured_source_commit']==REJECTED
    commit,newtree=config['commit'],config['tree']
    assert re.fullmatch('[0-9a-f]{40}',commit) and re.fullmatch('[0-9a-f]{40}',newtree)
    assert not OUT.exists() and OUT.parent==NEWEXEC
    OUT.mkdir()
    started=time.time()
    try:
        preserved_inputs(config,pins)
        for base,digest in ((ORIGINAL,'94dd0c398aa4d91eaf809d56e0e0ea7d5f7f8d6129a111d37e4aca6c75dd7285'),
                            (REV,'117842bb30756ec05841fea61196cc20ba975947a8a550c0e75384af815cb200'),
                            (IDENTITY,'b103e401c62ea310eea2aa19ff89f88f72177e5d41743468c317220d96888cc7'),
                            (SIZEPREP,'e2e222b03ea6844f938de8fd8b004e374daa14a3bee0732d5000524674dc4070')):
            manifest(base,'SHA256SUMS',digest)
        assert sha(PREP/'SCOPE.json')==SCOPE_SHA
        oldscope=json.loads((PREP/'SCOPE.json').read_text())
        assert sha(PREP/'EXPECTED_BLOBS.json')==oldscope['expected_json_sha256']
        old=json.loads((PREP/'EXPECTED_BLOBS.json').read_text())
        oldpaths={r['path']:r for r in old}
        scope=json.loads((SIZEPREP/'SCOPE.json').read_text())
        assert sha(SIZEPREP/'SCOPE.json')==config['corrective_scope_sha256']
        assert sha(SIZEPREP/'SELECTED_PATHS.json')==scope['selected_sha256']
        assert sha(SIZEPREP/'EXCLUDED_PATHS.json')==scope['excluded_sha256']
        selected=json.loads((SIZEPREP/'SELECTED_PATHS.json').read_text())
        excluded=json.loads((SIZEPREP/'EXCLUDED_PATHS.json').read_text())
        paths={r['path']:r for r in selected}
        extra=paths[scope['disclosure_path']]
        disclosure=SIZEPREP/'P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json'
        assert sha(disclosure)==scope['disclosure_sha256']
        assert len(oldpaths)==2318 and len(paths)==2013 and len(excluded)==306
        omitted={r['path'] for r in excluded}
        assert set(paths)-{scope['disclosure_path']}==set(oldpaths)-omitted
        assert all(r['path'].startswith(scope['excluded_package']+'/') and r['change']=='A' for r in excluded)
        assert sum(r['bytes'] for r in excluded)==1169593078 and max(r['bytes'] for r in selected)==6471668
        assert json.loads(disclosure.read_text())['excluded_paths']==excluded
        def captured_files():
            for rel,row in oldpaths.items():
                assert file_key(DEST/rel)=={k:row[k] for k in ('bytes','sha256','git_blob_sha1','mode')},rel
            materialized={p.relative_to(DEST).as_posix() for p in DEST.rglob('*') if p.is_file() and '.git' not in p.relative_to(DEST).parts}
            assert materialized==set(oldpaths)
            assert file_key(disclosure)=={k:extra[k] for k in ('bytes','sha256','git_blob_sha1','mode')}
            for row in oldscope['mutable_controls_pinned_but_not_physically_copied']:
                assert file_key(EVIDENCE/'copy/source_control_snapshot'/row['path'])=={k:row[k] for k in ('bytes','sha256','git_blob_sha1','mode')}
        captured_files()
        retained_manifest_rows=all_manifest_rows=0
        for package in oldscope['packages']:
            rows=manifest(DEST/package['base'],package['manifest'],package['manifest_sha256'])
            assert len(rows)==package['payload_count']
            for rel,digest in rows.items():
                assert oldpaths[package['base']+'/'+rel]['sha256']==digest
            all_manifest_rows+=len(rows)
            if package['base']!=scope['excluded_package']:
                retained_manifest_rows+=len(rows)
        assert len(oldscope['packages'])==25 and all_manifest_rows==2229 and retained_manifest_rows==1924
        oldmap={p:(r['mode'],r['git_blob_sha1']) for p,r in oldpaths.items()}
        newmap={p:(r['mode'],r['git_blob_sha1']) for p,r in paths.items()}
        records=[]
        captures=[]
        for phase in list(PHASES)+['bare_build','bare_push']:
            fresh=phase.startswith('bare_')
            folder=NEWEXEC/phase.removeprefix('bare_') if fresh else EVIDENCE/phase
            executor=SIZEPREP/'execute.py' if fresh else ORIGINAL/'execute.py' if phase in PHASES[:4] else REV/'execute.py' if phase in PHASES[4:6] else IDENTITY/'execute.py'
            binding=json.loads((folder/'APPROVAL_BINDING.actual.json').read_text())
            assert sha(Path(binding['approval_path']))==binding['approval_sha256']
            assert binding['approval']['executor_sha256']==sha(executor)
            commands=sorted(folder.glob('command_*.actual.json'))
            assert len(commands)==config['native_counts'][phase]
            for i,p in enumerate(commands,1):
                assert p.name==f'command_{i:03d}.actual.json'
                r=native_record(p)
                expected_exit={('stage',7):'TIMEOUT',('commit_revision_01',8):128,('push_revision_02',10):1}.get((phase,i),0)
                assert r['exit']==expected_exit
                records.append({'path':str(p),'exit':r['exit'],'sha256':sha(p)})
                if 'stdout_lossless_gzip' in r:
                    assert phase in ('stage_revision_01','commit_revision_02')
                    captures.append((p.parent/r['stdout_lossless_gzip'],r))
                if 'ls-tree' in r['argv'] and '-z' in r['argv']:
                    raw=p.parent/r['stdout']['path'] if isinstance(r.get('stdout'),dict) else p.parent/(p.name.removesuffix('.actual.json')+'.stdout.raw')
                    assert tree_rows(raw.read_bytes())==(newmap if fresh else oldmap)
            failed=phase in ('stage','commit_revision_01','push_revision_02')
            result=json.loads((folder/('FAILURE.actual.json' if failed else 'RESULT.actual.json')).read_text())
            if fresh:
                assert result['scope_sha256']==config['corrective_scope_sha256']
                assert result['commit']==commit and result['tree']==newtree and result['base']==BASE
                assert result['moving_live_source_used'] is False and result['captured_source_preserved']==REJECTED
            else:
                assert result['scope_sha256']==SCOPE_SHA
                if phase in ('stage_revision_01','commit_revision_02'):
                    assert result['tree']==TREE
            if not failed:
                assert result['status']=='PASS' and result['commands']==len(commands)
            else:
                assert result['completed_commands']==len(commands)
        for base in (ORIGINAL,REV,IDENTITY,SIZEPREP):
            for p in sorted(base.rglob('*.actual.json')):
                r=json.loads(p.read_text())
                if isinstance(r,dict) and 'argv' in r and 'exit' in r:
                    native_record(p)
                    records.append({'path':str(p),'exit':r['exit'],'sha256':sha(p)})
        moved=json.loads((EVIDENCE/'stage_revision_01_lock_preservation/NATIVE_RESULT.actual.json').read_text())
        assert moved['native_exit']==0 and moved['stdout']==moved['stderr']==''
        assert moved['argv']==['/usr/bin/mv','--no-clobber','--',str(DEST/'.git/index.lock'),str(EVIDENCE/'stage_revision_01_lock_preservation/index.lock.failed-stage-01')]
        print('ROOT_RECEPTION: complete captured-source and archived native records checked; no live-paper reads',flush=True)
        unique={}
        for row in old:
            oid=row['git_blob_sha1']
            assert oid not in unique or (unique[oid]['sha256'],unique[oid]['bytes'])==(row['sha256'],row['bytes'])
            unique[oid]=row
        assert len(captures)==2 and len(unique)==1096
        equal=True
        compared=0
        with captures[0][0].open('rb') as a,captures[1][0].open('rb') as b:
            while True:
                x,y=a.read(1024*1024),b.read(1024*1024)
                equal=equal and x==y
                compared+=max(len(x),len(y))
                if not x and not y:
                    break
        decoded=[decode_objects(*captures[0],unique)]
        if not equal:
            decoded.append(decode_objects(*captures[1],unique))
        else:
            for key in ('raw_stream_bytes','raw_stream_sha256','unique_blob_count','verified_payload_bytes','gzip_bytes','gzip_sha256'):
                assert captures[0][1][key]==captures[1][1][key]
        for p,r in captures:
            assert r['argv']==['git','-C',str(DEST),'cat-file','--batch']
            assert r['stdin_sha256']==hashlib.sha256(b''.join((oid+'\n').encode() for oid in sorted(unique))).hexdigest()
            assert json.loads((p.parent/'BLOB_KEYS.actual.json').read_text())==decoded[0]['keys']
        for rel,row in paths.items():
            if rel!=scope['disclosure_path']:
                assert {k:row[k] for k in ('bytes','sha256','git_blob_sha1','mode')}=={k:oldpaths[rel][k] for k in ('bytes','sha256','git_blob_sha1','mode')}
        dump(OUT/'OBJECT_RECEPTION.actual.json',{'gzip_raw_byte_equal':equal,'compressed_bytes_compared':compared,
             'independent_complete_decompressions':len(decoded),'audits':decoded,
             'second_capture_basis':'compressed byte equality' if equal else 'second complete independent decompression',
             'new_bare_body_basis':'All retained old blob keys occur in these decoded objects; the new disclosure is read separately below.'})
        assert sha(REV/'process_support.py')==SUPPORT_SHA
        spec=importlib.util.spec_from_file_location('p210_bare_root_native_support',REV/'process_support.py')
        support=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(support)
        env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0',
                 GIT_SSH_COMMAND='ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=20 -o ConnectionAttempts=1')
        native=[]
        def git(repo,*args,stdin=b''):
            assert args[0] in ('rev-parse','rev-list','status','show-ref','diff','ls-tree','ls-files','cat-file','ls-remote','show')
            assert not (repo==BARE and args[0]=='status')
            options=['-c','include.path='+str(MIRROR/'.git/config'),'-c','core.bare=true','-c','core.fsmonitor=false','-c','gc.auto=0'] if repo==BARE else []
            argv=['git','-C',str(repo),*options,*args]
            stem=OUT/f'command_{len(native)+1:03d}'
            inp,out,err=[stem.with_suffix('.'+k+'.raw') for k in ('stdin','stdout','stderr')]
            with inp.open('xb') as f:
                f.write(stdin)
            r=support.run_files(argv,inp,out,err,env,timeout=45)
            rec={'argv':argv,'cwd':str(SOURCE),**r,'stdin_sha256':sha(inp),'stdout_sha256':sha(out),'stderr_sha256':sha(err)}
            dump(stem.with_suffix('.actual.json'),rec)
            native.append(rec)
            assert r['exit']==0 and r['process_group_settlement']['quiescent'] and not r['process_group_settlement']['signals']
            return out.read_bytes()
        before_index=sha(BARE/'index')
        assert (BARE/'objects/info/alternates').read_bytes()==(str(DEST/'.git/objects')+'\n'+str(MIRROR/'.git/objects')+'\n').encode()
        assert git(BARE,'rev-parse','--is-bare-repository').strip()==b'true'
        assert git(BARE,'rev-parse','HEAD').decode().strip()==commit
        assert git(BARE,'rev-list','--parents','-n','1',commit).decode().split()==[commit,BASE]
        assert git(BARE,'rev-parse',commit+'^{tree}').decode().strip()==newtree
        prefixes=[p['base'] for p in oldscope['packages'] if p['base']!=scope['excluded_package']]+oldscope['exact_extra_paths']+[scope['disclosure_path']]
        assert tree_rows(git(BARE,'ls-tree','-r','-z','--full-tree',commit,'--',*prefixes))==newmap
        assert not git(BARE,'ls-tree','-r',commit,'--',scope['excluded_package'])
        changes={r['path']:r['change'] for r in selected}
        assert change_rows(git(BARE,'diff','--name-status','-z','--no-renames',BASE,commit,'--'))==changes
        assert change_rows(git(BARE,'diff','--cached','--name-status','-z','--no-renames',BASE,'--'))==changes
        assert not git(BARE,'diff','--cached','--name-status','-z',commit,'--')
        assert not git(BARE,'ls-files','--unmerged','-z')
        newunique={r['git_blob_sha1']:r for r in selected}
        assert len(newunique)==964 and sum(r['bytes'] for r in newunique.values())==69914981
        stdin=b''.join((oid+'\n').encode() for oid in sorted(newunique))
        assert git(BARE,'cat-file','--batch-check',stdin=stdin)==b''.join((oid+' blob '+str(newunique[oid]['bytes'])+'\n').encode() for oid in sorted(newunique))
        assert git(BARE,'cat-file','blob',extra['git_blob_sha1'])==disclosure.read_bytes()
        assert git(BARE,'show','-s','--format=%an%x00%ae%x00%cn%x00%ce',commit).decode().rstrip('\n').split('\0')==['mariswang','wangliang.f@gmail.com','mariswang','wangliang.f@gmail.com']
        assert git(BARE,'ls-remote','--exit-code','origin','refs/heads/main').decode().split()==[commit,'refs/heads/main']
        assert git(BARE,'rev-parse','origin/main').decode().strip()==commit
        assert git(BARE,'rev-list','--left-right','--count','HEAD...origin/main').split()==[b'0',b'0']
        capsule=scope['capsule_binding']
        assert git(DEST,'rev-parse','HEAD').decode().strip()==REJECTED
        assert git(DEST,'rev-parse','HEAD^{tree}').decode().strip()==TREE
        assert git(DEST,'rev-parse','origin/main').decode().strip()==BASE
        assert tree_rows(git(DEST,'ls-tree','-r','-z','--full-tree',TREE,'--',*[p['base'] for p in oldscope['packages']],*oldscope['exact_extra_paths']))==oldmap
        assert not git(DEST,'status','--porcelain=v1','-z','--untracked-files=all')
        assert sha(DEST/'.git/config')==capsule['config_sha256'] and sha(DEST/'.git/index')==capsule['index_sha256']
        assert hashlib.sha256(git(DEST,'show-ref')).hexdigest()==capsule['refs_sha256']
        assert git(MIRROR,'rev-parse','HEAD').decode().strip()==BASE
        assert git(MIRROR,'rev-parse','origin/main').decode().strip()==BASE
        assert not git(MIRROR,'status','--porcelain=v1','-z','--untracked-files=all')
        assert scope['original_binding']=={'config':sha(MIRROR/'.git/config'),'refs':hashlib.sha256(git(MIRROR,'show-ref')).hexdigest()}
        assert before_index==sha(BARE/'index')
        captured_files()
        preserved_inputs(config,pins)
        manifest(HERE,'SHA256SUMS',args.seal_sha256)
        dump(OUT/'ARCHIVED_NATIVE_RECORDS.actual.json',records)
        result={'status':'ROOT_READ_ONLY_CAPTURED_SOURCE_BARE_CHECKPOINT_RECEPTION_PASS','commit':commit,'tree':newtree,'baseline':BASE,
                'selected_paths':2013,'additions':2009,'modifications':4,'retained_manifests':24,'retained_manifest_rows':1924,
                'captured_source_paths':2318,'captured_manifests':25,'excluded_paths_locally_preserved':306,'excluded_bytes':1169593078,
                'selected_unique_objects':964,'selected_unique_payload_bytes':69914981,'largest_selected_blob_bytes':6471668,
                'old_unique_objects_fully_decoded':1096,'old_decoded_payload_bytes':658584369,'gzip_bytes_compared':compared,
                'gzip_byte_identical':equal,'independent_complete_decompressions':len(decoded),'new_disclosure_body_byte_equal':True,
                'archived_native_records_checked':len(records),'new_readonly_git_commands':len(native),'preserved_input_pins':len(pins),
                'captured_files_checked_twice':True,'moving_live_science_or_controls_read':False,'rejected_capsule_preserved':REJECTED,
                'new_bare_worktree_status':'N/A: bare; exact index/tree/ref checks passed','remote_confirmed':True,'divergence':[0,0],
                'original_mirror_unchanged':BASE,'new_git_writes':0,'new_scientific_executions':0,'new_bulk_body_capture_bytes':0,
                'receiver_seal_sha256':args.seal_sha256,'elapsed_seconds':time.time()-started}
        dump(OUT/'RESULT.actual.json',result)
        files=sorted(p for p in OUT.rglob('*') if p.is_file())
        with (OUT/'SHA256SUMS').open('x') as f:
            for p in files:
                f.write(sha(p)+'  '+p.relative_to(OUT).as_posix()+'\n')
        print(json.dumps(result,sort_keys=True))
    except BaseException:
        dump(OUT/'FAILURE.actual.json',{'exception':traceback.format_exc(),'no_cleanup_or_automatic_retry':True})
        raise


if __name__=='__main__':
    main()

