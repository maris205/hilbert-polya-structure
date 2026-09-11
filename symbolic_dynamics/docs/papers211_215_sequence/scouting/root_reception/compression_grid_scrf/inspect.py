#!/usr/bin/python3.10
"""Bounded original reception of three negative desks, never science."""
from pathlib import Path
from hashlib import sha256
import json
import os
import re
import shlex
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT/'docs/papers211_215_sequence/scouting'
HERE = Path(__file__).resolve().parent
ENV = {'PATH':'/usr/bin:/bin','LC_ALL':'C.UTF-8','LANG':'C.UTF-8','TZ':'UTC'}
checks, reads, native, packages = 0, {}, [], {}

def need(value,label):
    global checks
    checks += 1
    assert value,label

def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def read(path):
    path=Path(path); raw=path.read_bytes()
    need(str(path) not in reads or reads[str(path)] == pin(raw),('read drift',str(path)))
    reads[str(path)]=pin(raw)
    return raw

def obj(path): return json.loads(read(path))

def save(name,value):
    with (HERE/name).open('xb') as f:
        f.write((json.dumps(value,sort_keys=True,indent=2)+'\n').encode())

def lines_manifest(base,name,count):
    result={}
    for line in read(base/name).decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None,'exact sha syntax'); digest,path=m.groups()
        need(path not in result and not Path(path).is_absolute() and '..' not in Path(path).parts,'unique relative safe')
        need(pin(read(base/path))['sha256']==digest,('all digest bytes',path))
        result[path]=digest
    need(len(result)==count,('exact count',name))
    return result

def compare(label,a,b):
    need(a==b,('complete raw equality',label))
    fds=[os.memfd_create('archived-raw'),os.memfd_create('current-raw')]
    try:
        for fd,raw in zip(fds,[a,b]): os.write(fd,raw);os.lseek(fd,0,0)
        argv=['/usr/bin/cmp','--',*[f'/proc/self/fd/{fd}' for fd in fds]]
        r=subprocess.run(argv,env=ENV,cwd=ROOT,pass_fds=fds,capture_output=True,timeout=60)
        native.append({'role':'new root raw-byte comparison','label':label,'argv':argv,'cwd':str(ROOT),'environment':ENV,'input_bytes':[pin(a),pin(b)],'exit_code':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()})
        need(r.returncode==0 and r.stdout==r.stderr==b'',('native raw cmp',label))
    finally:
        for fd in fds:os.close(fd)

def records_read(base,filename,count):
    records=obj(base/filename)['records'];need(len(records)==count,'all local records')
    raw_count=0
    for row in records:
        cmd=row.get('cmd',row.get('request',{}).get('cmd'))
        result=row.get('result',row.get('returned'))
        need(isinstance(cmd,str) and isinstance(result['output'],str) and isinstance(result['exit_code'],int),'actual request and result')
        if not cmd.startswith("sed -n '"):continue
        argv=shlex.split(cmd)
        need(len(argv)==4 and argv[:2]==['sed','-n'],'bounded sed only')
        m=re.fullmatch(r'(\d+),(\d+|\$)p',argv[2]);need(m is not None,'explicit bounded source range')
        first,last=m.groups();body=read(ROOT/argv[3]);lines=body.splitlines(keepends=True)
        excerpt=b''.join(lines[int(first)-1:None if last=='$' else int(last)])
        need(result['exit_code']==0,'source read success')
        compare(str(base.name)+':'+cmd,result['output'].encode(),excerpt);raw_count+=1
    return records,raw_count

read(Path(__file__))
obj(HERE/'ROOT_GRID_PRIMARY_RETURNS.json')
obj(HERE.parent/'compression_reception/ROOT_PRIMARY_RETURNS.json')
specs=[('finite_compression_recoding_fresh_desk','SHA256SUMS',5,5),('bounded_lattice_profile_fresh_desk','MANIFEST.sha256',5,4),('finite_feedback_residual_design_desk','MANIFEST.sha256',6,7)]
for name,manifest,count,pincount in specs:
    base=SCOUT/name;payload=lines_manifest(base,manifest,count)
    need(set(payload)|{manifest}=={str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()},'complete nonself package')
    need(manifest not in payload and all(not p.is_symlink() for p in base.rglob('*')),'physical nonself inputs')
    if name.startswith('finite_compression'):
        pins=obj(base/'HISTORICAL_INPUT_PINS.json')['pins'];need(len(pins)==pincount,'five historical pins')
        for row in pins:need(pin(read(ROOT/row['path']))['sha256']==row['sha256'],'whole historical original')
        records,raws=records_read(base,'OLD_READ_RECORDS.json',11)
        sources=obj(base/'PRIMARY_RETURNS.json');web=sources['records'];need(len(web)==8,'eight actual browser returns')
        need(sources['local_fetch_lookup_failure']['returned']['exit_code']==2,'preserved fetch lookup failure')
        check=obj(base/'DOCUMENTARY_CHECK.json');need(check['returned']['exit_code']==0,'actual documentary completion')
        need(json.loads(check['returned']['output'])['archived_body_ranges_equal_now']==6,'actual six-science-original scope')
        need(all(r['returned']['exit_code']==0 for r in records),'eleven native archived completions')
    else:
        lines_manifest(ROOT,str((base/'INPUT_PINS.sha256').relative_to(ROOT)),pincount)
        nlocal,nweb=(14,4) if name.startswith('bounded') else (12,2)
        records,raws=records_read(base,'NATIVE_READS.json',nlocal)
        web=obj(base/'SOURCES_NATIVE.json')['calls'];need(len(web)==nweb,'all actual browser returns')
        check=obj(base/'CHECKS_NATIVE.json')
        rows=check['corrected_checks'] if 'corrected_checks' in check else check['records']
        need(all(r['result']['exit_code']==0 for r in rows),'every actual corrected check')
        expected_cmp=4 if name.startswith('bounded') else 6
        need(len([r for r in rows if 'cmp -' in r['cmd']])==expected_cmp,'all actual archived native comparisons')
        need(all(r['result']['output']=='' for r in rows if 'cmp -' in r['cmd']),'complete native cmp empty successful output')
        if name.startswith('bounded'):
            need([r['result']['exit_code'] for r in check['first_attempt']]==[0,127,1,1,1,1,0],'five retained first-check failures')
        else:
            matches=[r for r in records if r['cmd'].startswith('pdftotext ')];need(len(matches)==1,'one actual archived primary extraction')
            row=matches[0];argv=shlex.split(row['cmd']);read(ROOT/argv[-2])
            r=subprocess.run(['/usr/bin/pdftotext',*argv[1:]],env=ENV,cwd=ROOT,capture_output=True,timeout=60)
            native.append({'role':'new text extraction, not science/build/view','argv':['/usr/bin/pdftotext',*argv[1:]],'cwd':str(ROOT),'environment':ENV,'exit_code':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()})
            need(r.returncode==0 and r.stderr==b'','new primary extraction')
            compare(name+':primary 3-page extraction',row['result']['output'].encode(),r.stdout);raws+=1
    for row in web:
        need(isinstance(row['request'],dict) and isinstance(row.get('result',row.get('returned')),str),'complete actual browser object')
    local_links=0
    for path in base.glob('*.md'):
        for href in re.findall(r'\]\(([^\n)]+)\)',read(path).decode()):
            if '://' in href or href.startswith('#'):continue
            target=(path.parent/href.split('#')[0]).resolve();need(target.is_file(),'actual local link');read(target);local_links+=1
    packages[name]={'payloads':count,'whole_historical_pins':pincount,'raw_comparisons':raws,'native_read_records':len(records),'browser_returns':len(web),'local_links':local_links,'manifest':pin(read(base/manifest))}
for path,value in list(reads.items()):need(pin(Path(path).read_bytes())==value,('final immutable bytes',path))
result={'status':'PASS_NEGATIVE_DESK_ORIGINAL_RECEPTION','checks':checks,'read_paths':len(reads),'packages':packages,'new_native_operations':len(native),'new_scientific_runs':0,'new_review_or_admission':False,'new_literal_attempts':1,'disposition':'SCRF_NO_PROMOTION_VALUE_PLUS_TWO_ZERO_LITERAL_DESKS','external':'HOLD_EXTERNAL'}
save('INPUTS.json',reads);save('NATIVE_OPERATIONS.json',native);save('RESULT.json',result)
print(json.dumps(result,sort_keys=True))
