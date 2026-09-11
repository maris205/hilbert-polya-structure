"""Fetch exact cited primary PDF bodies; no manuscript upload or API review."""
from pathlib import Path
import hashlib
import json
import subprocess
import time

BASE=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p208_b')
OUT=BASE/'sources/primary'
OUT.mkdir(exist_ok=False)
ENV={'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
URLS={
 'bose':'https://arxiv.org/pdf/1310.1166v2',
 'pallo':'https://acta.bibl.u-szeged.hu/12796/1/Pallo_2006_ActaCybernetica.pdf',
 'hong':'https://arxiv.org/pdf/2201.10030v1',
 'barnard':'https://arxiv.org/pdf/2312.03959v1',
 'ajran':'https://arxiv.org/pdf/2501.10311v1',
 'mansour':'https://cs.uwaterloo.ca/journals/JIS/VOL9/Mansour/mansour86.pdf'}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(name,args):
    start=time.time()
    p=subprocess.run(args,cwd=OUT,env=ENV,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (OUT/(name+'.stdout')).write_bytes(p.stdout);(OUT/(name+'.stderr')).write_bytes(p.stderr)
    (OUT/(name+'.command.json')).write_text(json.dumps({'argv':args,'cwd':str(OUT),'env':ENV,'exit_code':p.returncode,'seconds':time.time()-start},indent=2)+'\n')
    assert p.returncode==0,(name,p.returncode)
tools=['/root/miniconda3/bin/curl','/usr/bin/pdftotext']
before={p:sha(Path(p).resolve()) for p in tools}
(OUT/'TOOLS_BEFORE.json').write_text(json.dumps(before,indent=2)+'\n')
for name,url in URLS.items():
    run(name+'_download',[tools[0],'--fail','--location','--silent','--show-error','--max-time','45',url,'--output',str(OUT/(name+'.pdf'))])
    run(name+'_extract',[tools[1],'-layout',str(OUT/(name+'.pdf')),str(OUT/(name+'.txt'))])
    assert (OUT/(name+'.pdf')).read_bytes().startswith(b'%PDF-')
after={p:sha(Path(p).resolve()) for p in tools}
assert before==after
(OUT/'TOOLS_AFTER.json').write_text(json.dumps(after,indent=2)+'\n')
(OUT/'BODY_PINS.json').write_text(json.dumps({p.name:sha(p) for p in OUT.iterdir() if p.suffix in ('.pdf','.txt')},indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','downloaded_exact_version_primary_bodies':URLS,'read_scope':'Downloading/extraction is not complete reviewer reading; selected sections recorded separately.'},sort_keys=True))
