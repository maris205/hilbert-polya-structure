#!/usr/bin/python3.10
"""Four bounded negative-desk artifact receptions; no scientific execution."""
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
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
checks, reads, operations, summaries = 0, {}, [], {}

def need(ok, label):
    global checks
    checks += 1
    assert ok, label

def pin(raw): return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def read(path):
    path = Path(path).resolve(); raw = path.read_bytes()
    need(str(path) not in reads or reads[str(path)] == pin(raw), ('immutable read',str(path)))
    reads[str(path)] = pin(raw)
    return raw

def obj(path): return json.loads(read(path))

def save(name, value):
    with (HERE/name).open('xb') as f:
        f.write((json.dumps(value,sort_keys=True,indent=2)+'\n').encode())

def manifest(path, base, count):
    out = {}
    for line in read(path).decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None, 'exact sha line'); digest, rel = m.groups()
        need(rel not in out and not Path(rel).is_absolute() and '..' not in Path(rel).parts, 'safe unique manifest')
        target = (base/rel).resolve()
        need(pin(read(target))['sha256']==digest, ('full manifest bytes',rel))
        out[rel] = target
    need(len(out)==count, ('manifest population',path,count))
    return out

def cmp_raw(label, expected, actual, scope='raw equality'):
    need(expected==actual, (scope,label))
    fds = [os.memfd_create('expected-raw'),os.memfd_create('actual-raw')]
    try:
        for fd, raw in zip(fds,[expected,actual]):
            os.write(fd,raw); os.lseek(fd,0,0)
        argv=['/usr/bin/cmp','--',*[f'/proc/self/fd/{fd}' for fd in fds]]
        r=subprocess.run(argv,pass_fds=fds,cwd=ROOT,env=ENV,capture_output=True,timeout=60)
        operations.append({'role':scope,'label':label,'argv':argv,'cwd':str(ROOT),'env':ENV,'inputs':[pin(expected),pin(actual)],'exit_code':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()})
        need(r.returncode==0 and r.stdout==r.stderr==b'', ('actual native cmp',label))
    finally:
        for fd in fds: os.close(fd)

def sed_bytes(command):
    a=shlex.split(command)
    need(len(a)==4 and a[:2]==['sed','-n'], 'explicit sed source only')
    m=re.fullmatch(r'(\d+),(\d+|\$)p',a[2]); need(m is not None,'explicit sed range')
    lo,hi=m.groups(); raw=read(ROOT/a[3]); lines=raw.splitlines(keepends=True)
    return b''.join(lines[int(lo)-1:None if hi=='$' else int(hi)])

def split_record(row):
    cmd=row.get('cmd',row.get('request',{}).get('cmd'))
    ret=row.get('result',row.get('returned'))
    need(isinstance(cmd,str) and isinstance(ret,dict) and isinstance(ret.get('output'),str),'actual cmd and native result')
    need(isinstance(ret.get('exit_code'),int) or isinstance(ret.get('session_id'),int),'completed or honestly yielded native')
    return cmd,ret

def whole_sed(row,label):
    cmd,ret=split_record(row); need('\n' not in cmd and ret['exit_code']==0,'successful sole sed')
    cmp_raw(label,ret['output'].encode(),sed_bytes(cmd))

def sha_output(command):
    args=shlex.split(command); need(args[0]=='sha256sum' and all(not x.startswith('-') for x in args[1:]),'explicit original hashes')
    return ''.join(pin(read(ROOT/p))['sha256']+'  '+p+'\n' for p in args[1:]).encode()

def pins_in_output(raw,count):
    rows=re.findall(r'^([0-9a-f]{64})  (.+)$',raw,re.M)
    need(len(rows)==count,'complete historical pin rows')
    for digest,path in rows: need(pin(read(ROOT/path))['sha256']==digest,('historical original',path))

def sorted_rg(row,label):
    command,ret=split_record(row); args=shlex.split(command)
    need(args[0]=='rg' and '\n' not in command and '|' not in args, 'single bounded rg')
    # This allowlist excludes directory discovery and protected current trees.
    paths=[x for x in args if x.startswith('docs/')]
    need(paths and all((ROOT/p).is_file() and not p.startswith('docs/papers211_215') for p in paths),'old explicit files only')
    for p in paths: read(ROOT/p)
    r=subprocess.run(['/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg',*args[1:]],cwd=ROOT,env=ENV,capture_output=True,timeout=60)
    operations.append({'role':'new old-file text search, not science','label':label,'argv':['/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg',*args[1:]],'cwd':str(ROOT),'env':ENV,'exit_code':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode(),'raw_equal_archived':r.stdout==ret['output'].encode()})
    need(r.returncode==ret['exit_code']==0 and r.stderr==b'','successful bounded rg')
    cmp_raw(label,b''.join(sorted(ret['output'].encode().splitlines(keepends=True))),b''.join(sorted(r.stdout.splitlines(keepends=True))),'bytewise sorted-line equality, not raw-output equality')

read(Path(__file__))
read('/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg')
read('/usr/bin/cmp')
for path in HERE.glob('ROOT_PRIMARY*.json'): obj(path)
specs=[('finite_ordered_interaction_fresh_desk','MANIFEST.sha256',6,'local'),('finite_path_local_memory_desk','MANIFEST.sha256',6,'root'),('finite_algebraic_normal_form_fresh_desk','SHA256SUMS',5,'local'),('finite_graph_memory_fresh_desk','SHA256SUMS',5,'local')]
for name,mname,count,role in specs:
    base=SCOUT/name; payload=manifest(base/mname,ROOT if role=='root' else base,count)
    files={p.resolve() for p in base.rglob('*') if p.is_file()}
    need(files==set(payload.values())|{(base/mname).resolve()},'complete exact nonself inventory')
    need(all(not p.is_symlink() for p in base.rglob('*')),'physical originals')
    for path in files:
        if path.suffix=='.json':obj(path)
    nlinks=0
    for path in base.glob('*.md'):
        for href in re.findall(r'\]\(([^\n)]+)\)',read(path).decode()):
            if '://' in href or href.startswith('#'):continue
            target=(path.parent/href.split('#')[0]).resolve(); need(target.is_file(),('complete local link',href)); read(target);nlinks+=1
    if name.startswith('finite_ordered') or name.startswith('finite_path'):
        ordered=name.startswith('finite_ordered')
        manifest(base/'INPUTS.sha256',ROOT,6 if ordered else 5)
        rows=obj(base/'NATIVE_READS.json')['records']; web=obj(base/'SOURCES_NATIVE.json')['records']
        need(len(rows)==(6 if ordered else 13) and len(web)==(9 if ordered else 4),'whole local and browser records')
        for row in rows:split_record(row)
        for row in web:need(isinstance(row['request'],dict) and isinstance(row['result'],str),'complete archived browser return')
        need(sum(len(r['request'].get('search_query',[])) for r in web)==(11 if ordered else 6),'bounded actual query count')
        if ordered:
            whole_sed(rows[0],name+':old SCOUT');whole_sed(rows[3],name+':old M01')
            sorted_rg(rows[1],name+':search1');sorted_rg(rows[2],name+':search2')
            cmp_raw(name+':six original hashes',rows[4]['result']['output'].encode(),sha_output(rows[4]['cmd']))
            ch=obj(base/'CHECKS_NATIVE.json')['records']
            need(len(ch)==10 and [r['result']['exit_code'] for r in ch]==[0,0,0,1,1,0,0,0,0,0],'both failed raw compares preserved')
            need(all(ch[i]['result']['output']=='' for i in [2,5,7,8]),'actual successful raw and sorted compares')
        else:
            whole_sed(rows[4],name+':old SCOUT');whole_sed(rows[8],name+':old rotor code')
            for i in [5,9,10]:sorted_rg(rows[i],name+':search'+str(i))
            cmp_raw(name+':five original hashes',rows[11]['result']['output'].encode(),sha_output(rows[11]['cmd']))
            need('kip_candidate_gate' in rows[0]['result']['output'] and 'truncated' in rows[1]['result']['output'],'scope/truncation preserved')
            need(sum(r['result']['exit_code']!=0 for r in rows)==4,'four navigation nonzero returns')
            ch=obj(base/'CHECKS_NATIVE.json')['records'];need(len(ch)==5 and all(r['result']['exit_code']==0 for r in ch),'five actual checks')
    elif name.startswith('finite_algebraic'):
        local=obj(base/'LOCAL_READ_RECORDS.json');rows=local['records'];web=obj(base/'RETRIEVAL_RECORDS.json')['records']
        need(len(rows)==13 and len(web)==5,'all algebra provenance records')
        for row in rows:split_record(row)
        for row in web:need(isinstance(row['request'],dict) and isinstance(row['returned'],str),'actual algebra browser return')
        for i in range(5):whole_sed(rows[i],name+':read'+str(i))
        cmd,ret=split_record(rows[7]); parts=cmd.splitlines(); tail=sed_bytes(parts[1])+sha_output(parts[2])
        cmp_raw(name+':read7 exact scientific suffix',ret['output'].encode()[-len(tail):],tail,'raw suffix equality only')
        cmd,ret=split_record(rows[8]); prefix=sed_bytes(cmd.splitlines()[0])
        cmp_raw(name+':read8 exact code prefix',ret['output'].encode()[:len(prefix)],prefix,'raw prefix equality only; old central text excluded')
        pins_in_output(rows[5]['returned']['output'],4);pins_in_output(rows[7]['returned']['output'],1)
        need(rows[6]['returned']['exit_code']==2,'missing old pilot.py retained')
        need('session_id' in rows[10]['returned'] and 'exit_code' not in rows[10]['returned'],'yielded download not forged as complete')
        source=Path('/tmp/finite-algebraic-source-RLpHxE/Rutishauser.pdf'); raw=read(source)
        need(pin(raw)=={'bytes':9399955,'sha256':'1ed19def114812c8e6b815b0a44b81016ff3ed2a5aa882cd45ecf3328e7da48a'},'actual completed source bytes, not curl exit inference')
        for path in local['visual_read_receipt']['paths']:read(path)
        ch=local['document_checks'];need(len(ch)==3 and [r['returned']['exit_code'] for r in ch]==[0,1,0],'documentary failures plus successful fallback preserved')
        need('jq: command not found' in ch[0]['returned']['output'],'compound exit zero not jq success')
        need('13 complete request/return pairs' in ch[2]['returned']['output'],'corrected actual document check')
    else:
        local=obj(base/'LOCAL_READ_RECORDS.json');rows=local['records'];web=obj(base/'RETRIEVAL_RECORDS.json')['records']
        need(len(rows)==6 and len(web)==6,'all graph provenance records')
        for row in rows:split_record(row)
        for row in web:need(isinstance(row['request'],dict) and isinstance(row['native_returned_character_length'],int) and isinstance(row['observed_result_urls'],list),'graph metadata-only browser provenance, not body archive')
        for i,which in [(2,'prefix'),(3,'suffix')]:
            cmd,ret=split_record(rows[i]);parts=cmd.splitlines(); selected=parts[:3] if i==2 else parts[1:]
            actual=b''.join(sed_bytes(c) for c in selected); expected=ret['output'].encode()
            expected=expected[:len(actual)] if which=='prefix' else expected[-len(actual):]
            cmp_raw(name+':read'+str(i)+' selected science '+which,expected,actual,'raw '+which+' equality only')
        for i in [4,5]:
            cmd,ret=split_record(rows[i]); actual=b''.join(sha_output(c) if c.startswith('sha256sum ') else sed_bytes(c) for c in cmd.splitlines())
            cmp_raw(name+':complete read'+str(i),ret['output'].encode(),actual)
        pins_in_output(rows[5]['returned']['output'],7)
        ch=local['document_only_check'];_,ret=split_record(ch); summary=json.loads(ret['output'])
        need(ret['exit_code']==0 and summary['ok'] and summary['local_links']==12 and len(summary['original_source_pins'])==7 and all(r['matches'] for r in summary['original_source_pins']),'actual complete graph document check')
        need([r['returned']['exit_code'] for r in rows]==[2,0,2,0,0,0],'graph navigation failures preserved')
    summaries[name]={'payloads':count,'payload_bytes':sum(pin(read(p))['bytes'] for p in payload.values()),'manifest_base_role':role,'manifest':pin(read(base/mname)),'native_read_records':len(rows),'browser_records':len(web),'local_links':nlinks}

for path,key in list(reads.items()):need(pin(Path(path).read_bytes())==key,('complete closing immutable keys',path))
result={'status':'PASS_BOUNDED_NEGATIVE_ORIGINAL_RECEPTION','checks':checks,'read_paths':len(reads),'packages':summaries,'native_operations':len(operations),'new_scientific_runs':0,'new_manuscript_reviews':0,'new_eligible_literals':1,'disposition':'GBPR_NO_PROMOTION_VALUE_AND_THREE_ZERO_LITERAL_DESKS','limits':['Graph browser records retain metadata, not complete bodies.','Algebra curl record is yielded with no recorded final exit; exact PDF bytes are independently present.','Mixed native streams are checked only at explicitly selected scientific prefixes/suffixes.','Multi-file rg checks are sorted-line equality, not raw equality.','Path desk prior protected-content traversal and all prior failures remain.'],'external':'HOLD_EXTERNAL'}
save('INPUTS.json',reads);save('NATIVE_OPERATIONS.json',operations);save('RESULT.json',result)
print(json.dumps(result,sort_keys=True))
