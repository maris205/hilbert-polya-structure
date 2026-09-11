#!/usr/bin/env python3
"""Static source/contract checks, safe final read-only Git checks and prep seal."""
from pathlib import Path
import ast
import hashlib
import json
import os
import subprocess
import time

HERE = Path(__file__).resolve().parent
PREP = HERE / 'preparation_01'
SOURCE = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest()


def main():
    out = HERE / 'validation_01'
    out.mkdir()
    scope = json.loads((PREP/'SCOPE.json').read_text())
    selected = json.loads((PREP/'SELECTED_PATHS.json').read_text())
    expected = json.loads((PREP/'EXPECTED_BLOBS.json').read_text())
    assert sha(PREP/'SELECTED_PATHS.json') == scope['selected_json_sha256']
    assert sha(PREP/'EXPECTED_BLOBS.json') == scope['expected_json_sha256']
    sources = []
    for p in sorted(HERE.glob('*.py')):
        body = p.read_text()
        ast.parse(body, filename=str(p))
        compile(body, str(p), 'exec')
        sources.append({'path': p.name, 'sha256': sha(p), 'lines': len(body.splitlines()), 'syntax_only_no_execution': True})
    assert len(selected) == len(expected) == 2318
    assert sum(r['bytes'] for r in selected) == 1410484831
    assert sum(r['change']=='A' for r in selected)==2314
    assert sum(r['change']=='M' for r in selected)==4
    assert scope['deletions']==0 and len(scope['packages'])==25
    assert not Path(scope['supplementary_clone']).exists()
    assert not Path(scope['overlay_execution_evidence']).exists()
    for row in expected:
        p = SOURCE / row['path']
        assert p.is_file() and not p.is_symlink() and p.stat().st_size==row['bytes']
        assert sha(p)==row['sha256'], row['path']
    unique = {r['git_blob_sha1']:r for r in expected}
    commands = []
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0',
               GIT_SSH_COMMAND='ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=20 -o ConnectionAttempts=1')
    for argv in [
        ['git','-C',str(MIRROR),'rev-parse','HEAD'],
        ['git','-C',str(MIRROR),'rev-parse','refs/remotes/origin/main'],
        ['git','-C',str(MIRROR),'status','--porcelain=v1','-z','--untracked-files=all'],
        ['git','-C',str(MIRROR),'rev-list','--left-right','--count','HEAD...origin/main'],
        ['git','-C',str(MIRROR),'ls-remote','--exit-code','origin','refs/heads/main'],
        ['git','-C',str(MIRROR),'config','--name-only','--get-regexp',r'^remote\.origin\.(url|pushurl)$'],
        ['git','-C',str(MIRROR),'for-each-ref','--format=%(refname)','refs/replace/'],
        ['df','-B1','--output=source,fstype,size,used,avail,pcent,target','/root',str(SOURCE)],
    ]:
        stem = out / ('command_%03d' % (len(commands)+1))
        start = time.time()
        p = subprocess.run(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, timeout=50)
        stem.with_suffix('.stdout.raw').write_bytes(p.stdout)
        stem.with_suffix('.stderr.raw').write_bytes(p.stderr)
        record = {'argv':argv,'exit':p.returncode,'start_epoch':start,'end_epoch':time.time(),
                  'stdout_sha256':sha(stem.with_suffix('.stdout.raw')),'stderr_sha256':sha(stem.with_suffix('.stderr.raw')),
                  'environment_overrides_only':{k:env[k] for k in ('GIT_OPTIONAL_LOCKS','GIT_TERMINAL_PROMPT','GIT_SSH_COMMAND')}}
        stem.with_suffix('.actual.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
        assert p.returncode==0, (argv,p.returncode)
        commands.append(p.stdout)
    assert commands[0].strip()==commands[1].strip()==BASE.encode()
    assert not commands[2] and commands[3].split()==[b'0',b'0']
    assert commands[4].split()==[BASE.encode(),b'refs/heads/main']
    assert commands[5].splitlines()==[b'remote.origin.url'] and not commands[6]
    result = {'status':'STATIC_PREPARATION_PASS_EXECUTOR_NOT_RUN', 'scope_sha256':sha(PREP/'SCOPE.json'),
              'sources':sources,'selected_count':len(selected),'source_payload_bytes':sum(r['bytes'] for r in selected),
              'unique_blob_count':len(unique),'unique_payload_bytes':sum(r['bytes'] for r in unique.values()),
              'packages':len(scope['packages']),'named_manifest_payload_rows':sum(p['payload_count'] for p in scope['packages']),
              'exact_extras':len(scope['exact_extra_paths']),'exact_ignored_paths':len(scope['ignored_selected_paths']),
              'source_second_hash_pass':True,'original_mirror_clean':True,'original_config_sha256':sha(MIRROR/'.git/config'),
              'actual_strict_known_host_remote_ref':BASE,'original_tracking_divergence':[0,0],
              'overlay_targets_still_absent':True,'executor_executions':0,'clone_copy_stage_commit_push_executions':0}
    with (out/'RESULT.actual.json').open('x') as f:
        json.dump(result,f,sort_keys=True,indent=2)
        f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='sources'},sort_keys=True))


if __name__=='__main__':
    main()
