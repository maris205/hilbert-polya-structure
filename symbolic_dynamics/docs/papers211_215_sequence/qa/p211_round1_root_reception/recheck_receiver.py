#!/usr/bin/python3.10
"""Root's disclosed reuse of the completely read receiver02; documentary only."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round1_root_reception'
SOURCE = QA/'p211_round1_reception_preparation02/receive_round1.py'
INDEPENDENT = QA/'p211_round1_independent_reception01'
HOST = QA/'p211_round1_binding_root/postcopy02/RESULT.json'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
SOURCE_SHA = '21d16d2560eeb68420a3c37c9a3fda98dcbcb0ea1043dc80cd36a81e24fef06e'
HOST_SHA = '04a123c5c7e9bba267ce380d387be7e4789f4a777d9c62bb5b7ed2f418630c77'

def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def put(name,value):
    raw = value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (HERE/name).open('xb') as stream:
        stream.write(raw)

def main():
    assert Path.cwd()==ROOT and dict(os.environ)==ENV
    source,host = SOURCE.read_bytes(),HOST.read_bytes()
    assert pin(source)=={'bytes':37766,'sha256':SOURCE_SHA}
    assert pin(host)['sha256']==HOST_SHA
    independent_raw = (INDEPENDENT/'receiver.stdout.raw').read_bytes()
    assert pin(independent_raw)=={'bytes':2971096,'sha256':'a761df245e742562df8bbcb6165f33c4d64d457bd0f22b5cb3be92698c78b23d'}
    independent = json.loads(independent_raw)
    assert independent['READ_INPUTS_BEFORE']==independent['READ_INPUTS_AFTER']
    argv = ['/usr/bin/python3.10','-I','-S','-B',str(SOURCE),
            '--root-host-evidence',str(HOST.relative_to(ROOT)),'--root-host-sha256',HOST_SHA]
    attempt = {'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
               'timeout_seconds':900,'started_epoch':time.time(),'receiver_source':pin(source),
               'root_host_record':pin(host),'independent_whole_output':pin(independent_raw),
               'scope':'Disclosed complete documentary checker reuse; zero science/build/view/review'}
    put('RECHECK_ATTEMPT.json',attempt)
    exception,code = None,None
    try:
        actual = subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=900)
        out,err,code = actual.stdout,actual.stderr,actual.returncode
    except subprocess.TimeoutExpired as exc:
        out,err = exc.stdout or b'',exc.stderr or b''
        exception = {'type':type(exc).__name__,'message':str(exc)}
    except OSError as exc:
        out,err = b'',b''
        exception = {'type':type(exc).__name__,'message':str(exc)}
    put('recheck.stdout.raw',out)
    put('recheck.stderr.raw',err)
    native = {**attempt,'ended_epoch':time.time(),'native_exit_code':code,'exception':exception,
              'stdout':pin(out),'stderr':pin(err)}
    put('RECHECK_NATIVE.json',native)
    assert exception is None and type(code) is int and code==0 and err==b''
    result = json.loads(out)
    assert result==independent and out==independent_raw
    assert SOURCE.read_bytes()==source and HOST.read_bytes()==host
    compare_argv = ['/usr/bin/cmp','--',str(INDEPENDENT/'receiver.stdout.raw'),str(HERE/'recheck.stdout.raw')]
    cmp_attempt = {'argv':compare_argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
                   'timeout_seconds':60,'started_epoch':time.time()}
    put('COMPARE_ATTEMPT.json',cmp_attempt)
    compared = subprocess.run(compare_argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=60)
    put('compare.stdout.raw',compared.stdout)
    put('compare.stderr.raw',compared.stderr)
    put('COMPARE_NATIVE.json',{**cmp_attempt,'ended_epoch':time.time(),'native_exit_code':compared.returncode,
        'stdout':pin(compared.stdout),'stderr':pin(compared.stderr)})
    assert type(compared.returncode) is int and compared.returncode==0 and compared.stdout==compared.stderr==b''
    summary = {k:v for k,v in result.items() if k not in ('READ_INPUTS_BEFORE','READ_INPUTS_AFTER','RICH_INVENTORIES')}
    summary.update({'whole_root_output':pin(out),'whole_independent_raw_identical':True,
                    'actual_cmp_exit':compared.returncode,'receiver_reuse':'Fully disclosed same source; not a new independent design',
                    'root_host_semantic_recheck':'Separate precopy02/postcopy02 and whole build keys, not supplied by receiver'})
    put('RECHECK_RESULT.json',summary)
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__':
    main()
