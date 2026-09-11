"""Bounded primary-source retrieval/documentary records; no science execution."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/scouting/LNR_SOURCE_RECHECK'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
INPUTS=[
 'AGENTS.md','SYMBOLIC_DYNAMICS_STATE.md','docs/papers204_208_sequence/PIPELINE_STATE.md',
 '.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md',
 'docs/papers204_208_sequence/PROBLEM_ANCHOR.md','docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
 'docs/papers197_201_sequence/PROBLEM_ANCHOR.md','docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md',
 'docs/papers204_208_sequence/scouting/word_local/LNR_GATE/CANDIDATE_GATE.md',
 'docs/papers204_208_sequence/scouting/word_local/LNR_GATE/SOURCE_AUDIT.md',
 'docs/papers204_208_sequence/scouting/word_local/LNR_GATE/INPUT_PINS.sha256',
 'docs/papers204_208_sequence/scouting/word_local/LNR_GATE/MANIFEST.sha256',
 'docs/papers204_208_sequence/scouting/word_local/LNR_GATE/sources/Mukherjee2011_elsevier_attempt.xml',
 'docs/papers204_208_sequence/scouting/word_local/LNR_EXTRA_COLLISION_NOTE.md',
 'docs/papers204_208_sequence/scouting/word_local/LNR_TEMPORAL_PROOF.md',
 'docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/PROOF_PACKAGE.md',
 'docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/SOURCE_BOUNDARY.md',
 'docs/papers197_201_sequence/scouting/word_poset_lane/TCSD_THEOREM_CONTRACT.md',
 'docs/papers197_201_sequence/scouting/word_poset_lane/TCSD_EXACT_GAP_PROOF.md']

def info(path):
    p=Path(path);raw=p.read_bytes()
    return {'sha256':sha256(raw).hexdigest(),'bytes':len(raw),'resolved':str(p.resolve()),
            'symlink':os.readlink(p) if p.is_symlink() else None}

def save(path,raw):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('xb') as stream:stream.write(raw)

def dump(path,value):save(path,(json.dumps(value,sort_keys=True,indent=2)+'\n').encode())

def command(folder,argv,inputs=()):
    folder.mkdir(parents=True,exist_ok=False)
    before={str(p):info(p) for p in inputs};dump(folder/'INPUTS_BEFORE.json',before)
    row={'argv':argv,'cwd':str(ROOT),'environment':ENV,'started_utc':datetime.now(timezone.utc).isoformat(),
         'status':'ATTEMPTED','exit_code':None}
    dump(folder/'ATTEMPT.json',row)
    child=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,check=False)
    save(folder/'stdout',child.stdout);save(folder/'stderr',child.stderr)
    after={str(p):info(p) for p in inputs};dump(folder/'INPUTS_AFTER.json',after)
    row.update(status='COMPLETED',exit_code=child.returncode,ended_utc=datetime.now(timezone.utc).isoformat(),
        inputs_unchanged=before==after,stdout=info(folder/'stdout'),stderr=info(folder/'stderr'),
        scope='Documentary retrieval/copy/extraction only; no mathematical producer or candidate admission.')
    dump(folder/'RECEIPT.json',row)
    assert before==after
    return row,child.stdout

def intake():
    paths=[ROOT/n for n in INPUTS]+[Path('/root/autodl-tmp/.codex/skills/research-lit/SKILL.md')]
    before={str(p):info(p) for p in paths};copies={}
    for index,p in enumerate(paths):
        name=p.relative_to(ROOT).as_posix() if p.is_relative_to(ROOT) else 'INSTALLED_RESEARCH_LIT_SKILL.md'
        target=BASE/'originals'/name;save(target,p.read_bytes())
        row,_=command(BASE/'commands'/('intake_cmp_'+str(index).zfill(2)),['/usr/bin/cmp','--',str(p),str(target)],[p,target])
        assert row['exit_code']==0 and not (BASE/'commands'/('intake_cmp_'+str(index).zfill(2))/'stderr').read_bytes()
        copies[str(p)]={'physical':str(target),'relative_copy':str(target.relative_to(BASE)),**before[str(p)],
            'role':'Exact at-assignment historical input; a later central index revision is not this original.'}
    assert before=={str(p):info(p) for p in paths}
    dump(BASE/'ORIGINAL_INPUTS.json',copies)
    dump(BASE/'INTAKE_RESULT.json',{'status':'PASS_PHYSICAL_EXACT_SOURCE_RECHECK_INTAKE','inputs':len(paths),
        'actual_raw_copy_comparisons':len(paths),'unchanged_during_copy':True,'copies':copies,
        'scientific_executions':0,'admission':False})
    print(json.dumps({'status':'PASS_PHYSICAL_EXACT_SOURCE_RECHECK_INTAKE','inputs':len(paths),
        'controls':{str(p):before[str(p)] for p in paths[:3]}},indent=2,sort_keys=True))

def get(route,label,url):
    assert re.fullmatch(r'0[1-6]',route) and re.fullmatch(r'[a-z0-9_]+',label)
    assert url.startswith('https://')
    folder=BASE/'routes'/route/label
    argv=['/usr/bin/curl','--location','--max-time','45','--connect-timeout','15',
          '--dump-header',str(folder/'response.headers'),'--output',str(folder/'response.body'),
          '--write-out','%{json}\n',url]
    row,raw=command(folder,argv,[Path(__file__),Path('/usr/bin/curl')])
    extras={n:info(folder/n) for n in ('response.headers','response.body') if (folder/n).is_file()}
    parsed=None
    try:parsed=json.loads(raw)
    except (ValueError,UnicodeDecodeError):pass
    dump(folder/'HTTP_RESULT.json',{'actual_curl_exit':row['exit_code'],'transport_result':parsed,'retained_responses':extras,
        'request_url':url,'no_authentication_or_paywall_bypass':True,'full_text_status':'UNASSESSED_UNTIL_BODY_READ'})
    print(json.dumps({'route':route,'label':label,'exit':row['exit_code'],'http_code':None if parsed is None else parsed.get('http_code'),
        'content_type':None if parsed is None else parsed.get('content_type'),'effective_url':None if parsed is None else parsed.get('url_effective'),
        'responses':extras},sort_keys=True,indent=2))

if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    if sys.argv[1:]==['intake']:intake()
    elif len(sys.argv)==5 and sys.argv[1]=='get':get(*sys.argv[2:])
    else:raise RuntimeError('Require intake or get ROUTE LABEL HTTPS_URL')
