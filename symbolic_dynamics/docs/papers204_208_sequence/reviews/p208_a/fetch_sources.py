"""Download the six exact primary read versions; preserve command evidence."""
from pathlib import Path
import runpy,sys,time,json
OUT=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p208_a')
shared=runpy.run_path(str(OUT/'record.py'))
command,pins,dump=[shared[k] for k in ('command','pins','dump')]
env={'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
urls={
 'bose':'https://arxiv.org/pdf/1310.1166v2',
 'barnard':'https://arxiv.org/pdf/2312.03959v1',
 'ajran':'https://arxiv.org/pdf/2501.10311v1',
 'hong':'https://arxiv.org/pdf/2201.10030v1',
 'pallo':'https://acta.bibl.u-szeged.hu/12796/1/Pallo_2006_ActaCybernetica.pdf',
 'mansour':'https://cs.uwaterloo.ca/journals/JIS/VOL9/Mansour/mansour86.pdf'}
dest=OUT/'sources'/'primary';dest.mkdir()
before=pins([__file__,OUT/'record.py','/usr/bin/curl','/usr/bin/pdftotext',sys.executable]);dump(dest/'TOOLS_BEFORE.json',before)
dump(dest/'REQUESTS_BEFORE.json',dict(time_ns=time.time_ns(),urls=urls,env=env))
for name,url in urls.items():
    command(['/usr/bin/curl','--location','--fail','--max-time','45','--url',url,'--output',str(dest/(name+'.pdf'))],dest,env,dest/(name+'_download'))
    command(['/usr/bin/pdftotext','-layout',str(dest/(name+'.pdf')),str(dest/(name+'.txt'))],dest,env,dest/(name+'_extract'))
dump(dest/'TOOLS_AFTER.json',pins(before));assert pins(before)==before
dump(dest/'BODY_PINS.json',pins([p for p in dest.iterdir() if p.suffix in ('.pdf','.txt')]))
print('Six exact primary PDFs downloaded and extracted; reading remains separate.')
