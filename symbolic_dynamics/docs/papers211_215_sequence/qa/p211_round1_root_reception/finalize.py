"""Preserve exactly two navigation originals, check receipt links, seal new root packet."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
HERE=ROOT/'docs/papers211_215_sequence/qa/p211_round1_root_reception'
CONTROL=HERE.parent/'control_before_round1_accepted'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}

def pin(raw):return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def put(path,value):
    raw=value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with path.open('xb') as stream:stream.write(raw)

def native(label,argv):
    record={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL','timeout_seconds':60,'started_epoch':time.time()}
    put(CONTROL/(label+'.ATTEMPT.json'),record)
    actual=subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=60)
    put(CONTROL/(label+'.stdout.raw'),actual.stdout);put(CONTROL/(label+'.stderr.raw'),actual.stderr)
    record.update({'ended_epoch':time.time(),'native_exit_code':actual.returncode,'stdout':pin(actual.stdout),'stderr':pin(actual.stderr)})
    put(CONTROL/(label+'.NATIVE.json'),record)
    assert type(actual.returncode) is int and actual.returncode==0 and actual.stdout==actual.stderr==b''
    return record

assert not os.path.lexists(CONTROL) and not os.path.lexists(HERE/'SHA256SUMS')
links=[]
for href in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',(HERE/'RECEPTION.md').read_text()):
    assert not re.match(r'[A-Za-z][A-Za-z0-9+.-]*:',href)
    p=(HERE/href.split('#',1)[0]).resolve(strict=True)
    assert p.is_relative_to(ROOT) and p.is_file()
    links.append({'href':href,'physical_path':str(p),'pin':pin(p.read_bytes())})
frozen=ROOT/'papers/211-kernel-image-projection-feedback/frozen_round1/SHA256SUMS'
assert pin(frozen.read_bytes())=={'bytes':8048,'sha256':'582630470c6d1b423f818ed566ed4b699865c04b30543aa502d4556011dd6828'}
CONTROL.mkdir()
mapping=[]
for i,rel in enumerate(['docs/papers211_215_sequence/PIPELINE_STATE.md','SYMBOLIC_DYNAMICS_STATE.md']):
    source=ROOT/rel;dest=CONTROL/source.name;before=source.read_bytes()
    copied=native('copy_'+str(i),['/usr/bin/cp','-p','--',str(source),str(dest)])
    compared=native('compare_'+str(i),['/usr/bin/cmp','--',str(source),str(dest)])
    assert source.read_bytes()==dest.read_bytes()==before and source.stat().st_ino!=dest.stat().st_ino and dest.stat().st_nlink==1
    mapping.append({'logical_path':rel,'physical_original':str(dest.relative_to(ROOT)),'pin':pin(before),
                    'copy_native':'copy_'+str(i)+'.NATIVE.json','compare_native':'compare_'+str(i)+'.NATIVE.json'})
put(CONTROL/'MAPPING.json',mapping)
controlrows={p.name:pin(p.read_bytes()) for p in CONTROL.iterdir() if p.is_file()}
put(CONTROL/'SHA256SUMS',''.join(v['sha256']+'  '+n+'\n' for n,v in sorted(controlrows.items())).encode())
put(HERE/'FINAL_DOCUMENTARY_CHECK.json',{'status':'PASS_DOCUMENTARY_LINKS_AND_PHYSICAL_PREUPDATE_CONTROLS',
    'local_receipt_links':links,'historical_mapping':mapping,'control_payloads':len(controlrows),
    'control_manifest':pin((CONTROL/'SHA256SUMS').read_bytes()),'native_copy_compare_commands':4,
    'new_scientific_executions':0,'paper_complete':False,'external':'HOLD_EXTERNAL'})
rows={p.relative_to(HERE).as_posix():pin(p.read_bytes()) for p in HERE.rglob('*') if p.is_file()}
assert all(p.resolve()==p for p in HERE.rglob('*'))
put(HERE/'SHA256SUMS',''.join(v['sha256']+'  '+n+'\n' for n,v in sorted(rows.items())).encode())
print(json.dumps({'status':'PASS_NEW_ROOT_ROUND1_PACKET_SEALED','root_payloads':len(rows),'root_payload_bytes':sum(v['bytes'] for v in rows.values()),
    'root_manifest':pin((HERE/'SHA256SUMS').read_bytes()),'historical_controls':mapping,'local_links':len(links),
    'new_scientific_executions':0,'external':'HOLD_EXTERNAL'},sort_keys=True))
