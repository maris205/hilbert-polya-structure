"""Root receipt of existing gate/minor delta: originals and documentary reuse.

Root separately read the complete author proof, gate audit, source boundary,
response and same-reviewer decision. No new all-parameter proof is asserted.
"""
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics');S=ROOT/'docs/papers211_215_sequence/scouting'
HERE=ROOT/'docs/papers211_215_sequence/qa/pointer_saved_output_root/gate_check02'
G=S/'finite_pointer_residual_gate';D=S/'finite_pointer_gate_minor_delta01';A=S/'finite_local_state_fresh_desk';R=S/'finite_pointer_gate_response01'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
READS={};CHECKS=0

def need(x,label):
    global CHECKS
    CHECKS+=1
    if not x:raise AssertionError(label)

def pin(raw):return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def read(p):
    p=Path(p);need(p.resolve()==p and p.is_file(),('physical original',str(p)))
    raw=p.read_bytes();key=pin(raw);need(str(p) not in READS or READS[str(p)]==key,'unchanged original')
    READS[str(p)]=key;return raw

def obj(p):return json.loads(read(p))

def put(name,value):
    raw=value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (HERE/name).open('xb') as stream:stream.write(raw)

def seal(base,count,digest):
    raw=read(base/'MANIFEST.sha256');need(pin(raw)['sha256']==digest,'exact frozen manifest')
    rows={}
    for line in raw.decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  ([^/]+)',line);need(m is not None,'strict manifest row')
        h,n=m.groups();need(n not in rows and n not in ('.','..','MANIFEST.sha256'),'unique flat payload')
        need(pin(read(base/n))['sha256']==h,'every payload pin');rows[n]=h
    need(len(rows)==count and {p.name for p in base.iterdir()}==set(rows)|{'MANIFEST.sha256'},'whole sealed flat package')
    return rows

def native(label,argv,timeout=60):
    attempt={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL','timeout_seconds':timeout,'started_epoch':time.time()}
    put(label+'.ATTEMPT.json',attempt)
    result=subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=timeout)
    put(label+'.stdout.raw',result.stdout);put(label+'.stderr.raw',result.stderr)
    put(label+'.NATIVE.json',{**attempt,'ended_epoch':time.time(),'native_exit_code':result.returncode,'stdout':pin(result.stdout),'stderr':pin(result.stderr)})
    need(type(result.returncode) is int and result.returncode==0 and result.stderr==b'','actual documentary native success')
    return result.stdout

read(Path(__file__))
seal(G,8,'da1bf1d5a2daf9e1de2b4731187dab2029dd02b25ec8aa8b14fa55b5f63f1364')
seal(R,9,'4414fa67223ff50cdcba6c310bf5ed66ceeb7582a9c8afb1011ad272032555db')
seal(D,7,'3ce50af64557c3dfe5e2a7c9cfe5d2f2a01080a3573fae26759e50f488f56157')
author=seal(A,5,'d6299f026e02195f145f33f819dcedb27b367c300280b3d3f7255fea1e136ada')
inputrows=read(G/'INPUT_PINS.sha256').decode().splitlines();need(len(inputrows)==21,'all gate original inputs')
for line in inputrows:
    h,n=line.split('  ',1);p=Path(n) if Path(n).is_absolute() else ROOT/n
    need(pin(read(p))['sha256']==h,('whole21 original pin',n))
source=D/'audit_documentary.py';need(pin(read(source))=={'bytes':8953,'sha256':'2942ed6b435942a8954a886a1fec539930c5025fd6ca3ae665e928889b0edc9a'},'fully read exact unchanged documentary checker')
out=native('gate_documentary_reuse',['/usr/bin/python3.10','-I','-S','-B',str(source)])
old=read(D/'DOCUMENTARY_RESULT.json');need(out==old,'whole original/reused documentary output raw equality')
decoded=json.loads(out);need(decoded['checks']==328 and decoded['INPUTS_BEFORE']==decoded['INPUTS_AFTER']
    and len(decoded['INPUTS_AFTER'])==28 and decoded['source_pin']==pin(read(source)),'complete actual328/28 result')
for p,key in decoded['INPUTS_AFTER'].items():
    path=Path(p);raw=read(path);st=path.stat()
    fields={k:getattr(st,'st_'+v) for k,v in [('mode','mode'),('device','dev'),('inode','ino'),('uid','uid'),('gid','gid'),
        ('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns')]}
    need({**pin(raw),'stat':fields}==key,'entire28 current rich input keys')
native('gate_documentary_cmp',['/usr/bin/cmp','--',str(D/'DOCUMENTARY_RESULT.json'),str(HERE/'gate_documentary_reuse.stdout.raw')])
envelope=obj(D/'NATIVE_EVIDENCE.json');archived=envelope['documentary_audit']
need(archived['request']['cmd']=='/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B '+str(source) and archived['request']['workdir']==str(ROOT)
     and archived['result']['exit_code']==0 and archived['result']['chunk_id']=='dcdcea'
     and archived['result']['output'].encode()==old,'whole original same-reviewer invocation')
current=obj(D/'FINDINGS.json');original=obj(G/'FINDINGS.json')
need(current['effective_current_census']=={'critical_open':0,'major_open':1,'minor_open':0}
     and [(r['id'],r['current_status']) for r in current['dispositions']]==[('PTR-G-S1','CLOSED_RESPONSE_ACCEPTED'),
         ('PTR-G-C1','CLOSED_RESPONSE_ACCEPTED'),('PTR-G-D1','CLOSED_RESPONSE_ACCEPTED'),('PTR-G-E1','OPEN')]
     and current['accepted_response']['pin']==pin(read(R/'RESPONSE.md')) and current['accepted_response_manifest']==pin(read(R/'MANIFEST.sha256'))
     and current['original_gate_manifest_sha256']==pin(read(G/'MANIFEST.sha256'))['sha256'],'same exact response current finite evidence remains open')
need(original['critical']==[] and [(x['id'],x['status']) for x in original['major']]==[('PTR-G-E1','OPEN')]
     and len(original['minor'])==3 and current['finite_evidence_received'] is False,'old pending census not rewritten')
records=obj(G/'NATIVE_READS.json')['records'];need(len(records)==12,'all selected gate native records')
for row in records:
    need(set(row)=={'args','result'} and type(row['result']['output']) is str and 'session_id' not in row['result'],'actual gate envelope shape')
need([r['result']['exit_code'] for r in records]==[0,0,0,0,0,1,0,0,0,0,0,0],'preserve unavailable helper failure')
expect=[read(ROOT/'papers/167-minimum-inverse-position-feedback/main.tex'),
        read(ROOT/'papers/209-ordered-fibre-threading/sections/01_setup.tex')+read(ROOT/'papers/209-ordered-fibre-threading/sections/02_recurrence.tex'),
        read('/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/henon_rotor_router_strong_digraph_route_a/THEOREM_PACKAGE.md'),
        ''.join(n+': OK\n' for n in author).encode()]
for i,wanted in enumerate(expect):need(records[i]['result']['output'].encode()==wanted,'whole original body/native manifest return')
pdfs=[]
for i,p in enumerate(['papers/167-minimum-inverse-position-feedback/main.pdf','papers/209-ordered-fibre-threading/main.pdf']):
    read(ROOT/p);pdfs.append(native('local_pdf_text_'+str(i),['/usr/bin/pdftotext','-f','1','-l','3','-layout',p,'-']))
need(records[6]['result']['output'].encode()==b''.join(pdfs),'both complete old PDF extraction bytes; not visual review')
scope_paths=['docs/papers197_201_sequence/scouting/fifth_fresh_20260905/period_feedback_reentry/SOURCE_OWNER_AND_COLLISION.md',
    'papers/93-random-push-pop-stack-cocycles/main.tex','papers/93-random-push-pop-stack-cocycles/README.md','papers/93-random-push-pop-stack-cocycles/HOSTILE_REVIEW.md']
context=native('old_literal_context',['/usr/bin/rg','-n','-i','-C','5','pointer.?revers|bicyclic|closed pointer',*scope_paths])
need(records[8]['result']['output'].encode()==context,'entire four-original bounded old context')
reads=envelope['selected_reads'];need(len(reads)==6 and all(r['result']['exit_code']==0 for r in reads),'complete six delta documentary envelopes')
for i,paths in [(0,[R/'RESPONSE.md',R/'RESPONSE_STATUS.json',G/'FINDINGS.json']),
    (2,[R/'DOCUMENTARY_CHECK.json',R/'WEB_REQUESTS_AND_READ_BOUNDARIES.json',R/'MANIFEST.sha256']),
    (3,[R/'inspect_inputs.py',R/'seal_response.py',R/'INPUT_PINS_BEFORE.json']),
    (4,[G/'SOURCES_AND_SUBTRACTION.md',G/'REPORT.md'])]:
    need(reads[i]['request']['cmd']=='cat '+' '.join(str(p.relative_to(ROOT)) for p in paths)
         and reads[i]['result']['output'].encode()==b''.join(read(p) for p in paths),'complete delta actual cat body')
doc=obj(D/'DOCUMENT_CHECK_NATIVE.json')['record'];small=json.loads(doc['result']['output'])
need(doc['result']['exit_code']==0 and small['checks']==45 and small['whole_original_rich_keys']==28,'actual final delta documentary check')
for n,key in small['owned_preseal_files'].items():need(pin(read(D/n))==key,'all actual delta preseal file bytes')
response_records=obj(R/'NATIVE_DOCUMENTARY_RECORDS.json')['records']
need(len(response_records)==6 and all(r['result']['exit_code']==0 for r in response_records),'complete response native envelopes')
need(response_records[2]['result']['original_token_count']>response_records[2]['request']['max_output_tokens'],
     'preserve original oversized display limitation, do not claim complete raw snippet equality')
gatecheck=obj(G/'DOCUMENT_CHECK_NATIVE.json')
need(gatecheck['unavailable_jq']['result']['exit_code']==1 and gatecheck['initial_check']['result']['exit_code']==0
     and 'WARNING: 1 line is improperly formatted' in gatecheck['initial_check']['result']['output']
     and gatecheck['initial_check']['failed_manifest_layout_reconstruction'].encode()==read(G/'INPUT_PINS.sha256')+b'\n'
     and gatecheck['corrected_check']['result']['exit_code']==0,'historical jq and malformed-line warning preserved')
web=obj(G/'WEB_REQUESTS_AND_METADATA.json')['records'];need(len(web)==16 and sum('response_character_length' in r for r in web)==15,'actual15 browser returns and one connection failure; metadata not full text')
links=[]
for docpath in [G/'REPORT.md',G/'SOURCES_AND_SUBTRACTION.md',G/'MATHEMATICAL_AUDIT.md',R/'RESPONSE.md',D/'DECISION.md']:
    for href in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',read(docpath).decode()):
        if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:',href) or href.startswith('#'):continue
        target=(docpath.parent/href.split('#',1)[0]).resolve(strict=True);need(target.is_relative_to(ROOT) and target.is_file(),'all local controlling document links')
        read(target);links.append(str(target))
for p,key in dict(READS).items():need(pin(read(p))==key,('complete final byte key',p))
result={'status':'PASS_ROOT_GATE_AND_EXACT_MINOR_DELTA_ORIGINAL_RECEPTION','checks':CHECKS,'read_paths':len(READS),
    'gate_payloads':8,'response_payloads':9,'delta_payloads':7,'author_payloads':5,'gate_input_pins':21,'current_original_rich_keys':28,
    'reused_documentary_checks':328,'native_documentary_commands':5,'old_native_records_received':12+6+6+1,
    'current_findings':{'critical_open':0,'major_open':1,'minor_open':0},'still_open':'PTR-G-E1',
    'new_scientific_executions':0,'new_builds':0,'new_page_views':0,'admission':'NOT_DECIDED','external':'HOLD_EXTERNAL','inputs':READS}
put('GATE_DOCUMENTS_RESULT.json',result);print(json.dumps({k:v for k,v in result.items() if k!='inputs'},sort_keys=True))
