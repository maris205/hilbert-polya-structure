"""Receive complete unchanged E1 originals; no scientific implementation executed."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
B=ROOT/'docs/papers211_215_sequence'
E=B/'scouting/finite_pointer_gate_e1_delta01'
R=B/'qa/pointer_saved_output_root'
HERE=Path(__file__).resolve().parent
READS={}
CHECKS=0
def need(ok,label):
    global CHECKS
    CHECKS+=1
    assert ok,label
def raw(p):
    p=Path(p); b=p.read_bytes()
    need(str(p) not in READS or READS[str(p)]==b,('stable bytes',str(p)))
    READS[str(p)]=b
    return b
def ident(b): return {'bytes':len(b),'sha256':sha256(b).hexdigest()}
def pin(p,w=None):
    p=Path(p)
    row={**ident(raw(p)),'resolved':str(p.resolve(strict=True)),'symlink':os.readlink(p) if p.is_symlink() else None}
    if w is not None:
        need(set(w)<=set(row) and all(row[k]==v for k,v in w.items()),('whole supplied pin',str(p)))
    return row
def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,('duplicate JSON key',k));d[k]=v
    return d
def doc(p): return json.loads(raw(p),object_pairs_hook=unique)
def seal(base,name,count,expected=None):
    data=raw(base/name)
    if expected: need(sha256(data).hexdigest()==expected,('exact seal',str(base)))
    rows={}
    for line in data.decode().splitlines():
        m=re.fullmatch(r'([a-f0-9]{64})  (.+)',line);need(m is not None,'manifest form')
        h,rel=m.groups();p=Path(rel)
        need(not p.is_absolute() and '..' not in p.parts and rel!=name and rel not in rows,'safe unique manifest path')
        pin(base/rel,{'sha256':h});rows[rel]=h
    files={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
    need(all(not p.is_symlink() for p in base.rglob('*')),'physical package')
    need(len(rows)==count and files==set(rows)|{name},'complete nonself inventory')
    return rows
def completed(n):
    parts=[n['result']]+[v['result'] for v in n.get('polls',[])]
    need(parts[-1]['exit_code']==0 and 'session_id' not in parts[-1],'actual completed zero native')
    for v in n.get('polls',[]): need(v['request']['session_id']==parts[0]['session_id'],'actual same session')
    return ''.join(p['output'] for p in parts).encode('utf-8')
def write(name,value):
    with (HERE/name).open('xb') as f:f.write((json.dumps(value,sort_keys=True,indent=2,allow_nan=False)+'\n').encode())

need(Path.cwd()==ROOT and HERE==B/'qa/pointer_e1_root_reception01','exact receiver location')
pin(__file__);pin(HERE/'REUSE_SCOPE.md')
seal(E,'MANIFEST.sha256',6,'0df5a7c9c3b37a639395043e9e1eda3be16631d8f88d482351e7b8ee05ca0c34')
native=doc(E/'NATIVE_EVIDENCE.json'); advisory=doc(E/'NATIVE_CHAIN_ADVISORY.json')
d=doc(E/'DOCUMENTARY_RESULT.json');findings=doc(E/'FINDINGS.json')
root_doc=doc(HERE/'DOCUMENTARY_REUSE_NATIVE01.json');root_aux=doc(HERE/'NATIVE_CHAIN_REUSE_NATIVE01.json')
need(root_doc['request']['cmd']==native['documentary']['request']['cmd'],'exact full documentary source reuse')
need(root_aux['request']['cmd']==advisory['native_records'][1]['request']['cmd'],'exact full auxiliary source reuse')
need(completed(root_doc)==completed(native['documentary'])==raw(E/'DOCUMENTARY_RESULT.json'),'whole actual documentary output byte equality')
need(completed(root_aux)==completed(advisory['native_records'][1]),'whole actual native advisory output byte equality')
need(d['INPUTS_BEFORE']==d['INPUTS_AFTER'] and len(d['INPUTS_BEFORE'])==35,'35 complete primary keys')
declared={}
for line in raw(E/'INPUT_PINS.sha256').decode().splitlines():
    h,p=line.split('  ',1)
    need(p not in declared and Path(p).is_absolute() and re.fullmatch('[a-f0-9]{64}',h),'absolute E1 pin role')
    declared[p]=h
need(set(declared)==set(d['INPUTS_BEFORE']),'exact declared pin path set')
for p,w in d['INPUTS_BEFORE'].items():
    pin(p,w);need(declared[p]==w['sha256'],'pin membership identity')
for name,field,count in [('gate_check04/GATE_DOCUMENTS_RESULT.json','inputs',51),('PREPARATION_RESULT02.json','inputs',22),('RUNTIME_DELTA03_RESULT.json','READ_INPUTS',91)]:
    prior=doc(R/name)
    need(len(prior[field])==count,('prior full accepted key',name))
    for p,w in prior[field].items():pin(p,w)
for name,count,expected in [('finite_pointer_residual_gate',8,findings['prior_gate_manifest_sha256']),('finite_pointer_gate_minor_delta01',7,findings['prior_minor_delta_manifest_sha256']),('finite_local_state_fresh_desk',5,'d6299f026e02195f145f33f819dcedb27b367c300280b3d3f7255fea1e136ada'),('finite_pointer_gate_response01',9,'4414fa67223ff50cdcba6c310bf5ed66ceeb7582a9c8afb1011ad272032555db')]:
    seal(B/'scouting'/name,'MANIFEST.sha256',count,expected)
runtime=doc(R/'runtime_execution03/commands/01_receive_initial_runtime/stdout.raw')
need(runtime['READ_INPUTS_BEFORE']==runtime['READ_INPUTS_AFTER'] and len(runtime['READ_INPUTS_AFTER'])==319,'entire original runtime child key')
for p,w in runtime['READ_INPUTS_AFTER'].items():pin(p,w)
for folder,number in [('runtime_execution03',221),('semantic_execution01',342)]:
    pre=doc(R/folder/'INPUTS_BEFORE.json');post=doc(R/folder/'INPUTS_AFTER.json')
    need(pre==post and len(pre)==number,'complete controller keys')
    for p,w in pre.items():pin(p,w)
semantic=doc(R/'semantic_execution01/RESULT.json')
need(d['scientific_stdout']==runtime['scientific_stdout_opaque_pin']==semantic['saved_stdout'],'one exact actual scientific output')
need(d['documentary_assertions']==628671 and d['complete_saved_states']==4356 and d['complete_saved_check_pairs']==50392,'complete documentary scope')
need((d['saved_box_checks'],d['saved_global_checks'])==(50368,24),'box versus global actual check collections')
need((d['runtime_received_checks'],d['runtime_rich_keys'],d['actual_semantic_typed_comparisons'])==(72746,319,4461),'runtime and semantic original totals')
need(findings['actual_evidence']['boxes']==d['boxes'] and findings['actual_evidence']['scientific_output']==d['scientific_stdout'],'entire finding/evidence relation')
need(findings['census']=={k:0 for k in ('critical_open','major_open','minor_open','new_critical','new_major','new_minor')},'current zero census')
need(findings['disposition']['id']=='PTR-G-E1' and findings['disposition']['status']=='CLOSED_EVIDENCE_RECEIVED','actual same-reviewer E1 closure')
need({r['id']:r['status'] for r in findings['prior_minor_dispositions']}=={k:'CLOSED_UNCHANGED' for k in ('PTR-G-S1','PTR-G-C1','PTR-G-D1')},'same three earlier minor closures')
need(d['excluded_family_observed_counts']==[0,0,0] and [r['first_possible_core_size'] for r in findings['coverage']['missing_families']]==[5,6,5],'deductive-only uncovered families')
need(all(findings[k] is True for k in ('not_admission','not_manuscript_review','not_paper_pass','not_strict_pair','not_canonical','not_p212_allocation')),'reviewer decision boundary')
need(advisory['native_records'][0]['result']['exit_code']==1 and advisory['native_records'][0]['result']['chunk_id']=='ff3878','preserved auxiliary failure')
need('semantic_box_sums' in advisory['native_records'][0]['result']['output'],'actual auxiliary failure reason')
final=native['final_owned_document_check']
need(final['failed_actual']['result']['exit_code']==1 and 'aux request fields ff3878' in final['failed_actual']['result']['output'],'preserved exact package diagnostic failure')
owned=json.loads(completed(final['corrected_actual']))
need(owned['checks']==1280 and owned['original_rich_paths_unchanged']==35,'actual corrected package result')
for name,w in owned['stable_payload_pins'].items():pin(E/name,w)
read_count=0
for n in native['selected_actual_semantic_original_reads']:
    m=re.fullmatch(r"sed -n '(\d+),(\d+)p' (.+)",n['request']['cmd'])
    need(m is not None and n['result']['exit_code']==0,'actual selected original sed')
    lo,hi,path=m.groups();data=raw(ROOT/path)
    excerpt=b''.join(data.splitlines(keepends=True)[int(lo)-1:int(hi)])
    need(n['result']['output'].encode('utf-8')==excerpt,'entire selected original return bytes');read_count+=1
for target in re.findall(r'\]\(([^)]+)\)',raw(E/'DECISION.md').decode()):
    if not target.startswith(('http://','https://')):need((E/target).is_file(),'actual local evidence link')
before={p:pin(p) for p in list(READS)}
for p,w in before.items():pin(p,w)
write('INPUTS.json',before)
result={'status':'PASS_ROOT_COMPLETE_POINTER_E1_ORIGINAL_RECEPTION','checks':CHECKS,'read_paths':len(before),
    'e1_payloads':6,'primary_pins':35,'prior_accepted_keys':[51,22,91],
    'reused_documentary_assertions':628671,'reused_native_chain_checks':3123,'whole_reuse_outputs_byte_identical':True,
    'selected_original_return_byte_comparisons':read_count,'current_open_findings':{'critical':0,'major':0,'minor':0},
    'scientific_producer_or_receiver_invocations':0,'new_literal_map_evaluations':0,
    'admission':'SEPARATE_ROOT_DECISION_NEXT','external':'HOLD_EXTERNAL'}
write('RESULT.json',result)
print(json.dumps(result,sort_keys=True))
