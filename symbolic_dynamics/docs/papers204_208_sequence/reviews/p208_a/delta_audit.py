"""P208 A documentary-only delta audit. Never execute scientific code or TeX."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,time,collections
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
OUT=ROOT/'docs/papers204_208_sequence/reviews/p208_a'
WORK=OUT/'delta'
BATCH=ROOT/'docs/papers204_208_sequence'
RR=BATCH/'qa/root_replays/p208_a_strict'
F=ROOT/'papers/208-original-snapshot-triangulation-sweeps/frozen_round0'
INITIAL='6d129aad1aec05cc08025030af1e1328cd59e66fccfd6311fc0176c901165ac8'
ROOT_SEAL='441506a2257387071fb104ea2bf169ff85c890c56cc6a66aa4ae02345b3d0284'
ENV={'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
COUNT=0
def ck(test,detail=''):
    global COUNT
    COUNT+=1
    if not test:raise AssertionError((COUNT,detail))
def info(p):
    b=Path(p).read_bytes()
    return dict(sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
def dump(p,x):
    with Path(p).open('x') as fp:json.dump(x,fp,sort_keys=True,indent=2);fp.write('\n')
def rawsave(p,b):
    with Path(p).open('xb') as fp:fp.write(b)
def load(p):return json.loads(Path(p).read_text())
def entries(p):
    a={}
    for line in Path(p).read_text().splitlines():
        h,rel=line.split('  ',1);ck(rel not in a);a[rel]=h
    return a
def snapshot_path(p):
    p=Path(p)
    return WORK/'initial_snapshot'/p.name if p in [OUT/'FINDINGS.json',OUT/'SHA256SUMS'] else p
def mapped_check(p,v,allow_relocation):
    p=Path(p)
    selected=snapshot_path(p) if allow_relocation else p
    ck(info(selected)==v,(str(p),'historical/current selected pin'))
    return selected
def add_map(target,source):
    for p,v in source.items():
        value=dict(sha256=v) if isinstance(v,str) else v
        ck(Path(p).is_file(),p)
        observed=info(p)
        ck(observed['sha256']==value['sha256'],p)
        if 'bytes' in value:ck(observed['bytes']==value['bytes'],p)
        if p in target:ck(target[p]==observed,('conflicting initial pin',p))
        target[p]=observed
def runtime_now():
    files={}
    for mod in tuple(sys.modules.values()):
        p=getattr(mod,'__file__',None)
        if p and Path(p).is_file():files[str(Path(p).resolve())]=info(p)
    mapped={}
    for line in Path('/proc/self/maps').read_text().splitlines():
        fields=line.split(None,5)
        if len(fields)==6 and fields[5].startswith('/'):
            p=Path(fields[5]).resolve();mapped[str(p)]=info(p)
    return dict(flags=dict(optimize=sys.flags.optimize,isolated=sys.flags.isolated,
        no_site=sys.flags.no_site,dont_write_bytecode=sys.dont_write_bytecode),
        pycache_prefix=sys.pycache_prefix,modules=files,mapped_files=mapped,
        environment=dict(sorted(os.environ.items())))
def prepare():
    ck(not WORK.exists(),'exclusive delta directory')
    ck(info(OUT/'SHA256SUMS')['sha256']==INITIAL)
    original=entries(OUT/'SHA256SUMS');ck(len(original)==743)
    for rel,h in original.items():ck(info(OUT/rel)['sha256']==h,rel)
    # Only this new auditor may precede preservation; every old payload is intact.
    ck({str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file()}==
        set(original)|{'SHA256SUMS','delta_audit.py'})
    WORK.mkdir();hist=WORK/'initial_snapshot';hist.mkdir()
    for name in ['FINDINGS.json','SHA256SUMS']:
        rawsave(hist/name,(OUT/name).read_bytes())
        ck((hist/name).read_bytes()==(OUT/name).read_bytes())
    response=[BATCH/'P208_A_RESPONSE.md',BATCH/'qa/P208_A_ROOT_INSPECTION.md',
        BATCH/'qa/P208_A_ROOT_ORIGINAL_INSPECTION.actual.json',
        BATCH/'qa/P208_A_ROOT_PAYLOAD_INSPECTION.actual.json',
        BATCH/'qa/replay_p208_strict.py']
    before={str(OUT/rel):info(OUT/rel) for rel in original}
    before[str(OUT/'SHA256SUMS')]=info(OUT/'SHA256SUMS')
    before[str(OUT/'delta_audit.py')]=info(OUT/'delta_audit.py')
    for p in response:before[str(p)]=info(p)
    for p in RR.rglob('*'):
        if p.is_file():before[str(p)]=info(p)
    for name in ['INPUT_PINS.sha256','HISTORY_CONTEXT_PINS.sha256']:
        for rel,h in entries(OUT/name).items():
            p=ROOT/rel;ck(info(p)['sha256']==h);before[str(p)]=info(p)
    for stem in ['INPUTS','RUNTIME_INVENTORY','LIBRARIES']:
        a=load(RR/(stem+'_BEFORE.json'));ck(a==load(RR/(stem+'_AFTER.json')))
        add_map(before,a)
    for label,stems in [('cold07',['INPUTS','TOOLS','LIBRARIES','CONFIG','RUNTIME_CONSUMED']),
                        ('cold08',['INPUTS','TOOLS','LIBRARIES','CONFIG','RUNTIME_CONSUMED']),
                        ('build03',['INPUTS','TOOLS','LIBRARIES','CONFIG','CONSUMED_TEX']),
                        ('artifact_inspection02',['INPUTS','TOOLS'])]:
        for stem in stems:
            if stem=='RUNTIME_CONSUMED':
                add_map(before,load(OUT/label/'RUNTIME_CONSUMED_AFTER.json'));continue
            a=load(OUT/label/(stem+'_BEFORE.json'));ck(a==load(OUT/label/(stem+'_AFTER.json')))
            add_map(before,a)
    config=load(RR/'CONFIGURATION_BEFORE.json')
    ck(config==load(RR/'CONFIGURATION_AFTER.json'))
    for p,v in config.items():
        ck(Path(p).exists()==v['exists']);ck(str(Path(p).resolve())==v['resolved'])
        if 'sha256' in v:before[str(Path(p).resolve())]=info(p)
    for p in [Path(sys.executable).resolve(),Path('/usr/bin/cmp')]:before[str(p)]=info(p)
    now=runtime_now()
    add_map(before,now['modules']);add_map(before,now['mapped_files'])
    dump(WORK/'INPUTS_BEFORE.json',before)
    dump(WORK/'ROOT_RESPONSE_PINS_BEFORE.json',{str(p):info(p) for p in response})
    dump(WORK/'ROOT_CONFIGURATION_BEFORE.json',config)
    dump(WORK/'PRE_REPAIR_SCOPE.json',dict(time_ns=time.time_ns(),finding='P208-A-ART1',
        severity='minor',status='open',initial_payloads=743,initial_manifest_sha256=INITIAL,
        initial_snapshot_before_current_ledger_update=True,
        chronology='Response/instructions and root recorder were read before this capture; this capture precedes the documentary repair and its actual count audit. No pre-first-read pin claim.',
        allowed_existing_mutations=['FINDINGS.json','SHA256SUMS'],
        prohibited='No scientific producer/recorder/canonical/manuscript/old log/build mutation or mathematical/TeX execution.'))
    print('PASS delta baseline and exact initial FINDINGS/manifest preservation')
def alias_audit(label):
    dest=OUT/label
    spellings=set()
    for name in ['python_ldd','extensions_ldd','cmp_ldd','bash_ldd']:
        rec=load(dest/(name+'.json'));ck(rec['exit']==0)
        for token in (dest/(name+'.stdout')).read_text().split():
            if token.startswith('/') and Path(token).is_file():spellings.add(token)
    groups=collections.defaultdict(list)
    for p in sorted(spellings):groups[str(Path(p).resolve())].append(p)
    before=load(dest/'LIBRARIES_BEFORE.json');after=load(dest/'LIBRARIES_AFTER.json')
    ck(before==after)
    ck(set(groups)==set(before),'exact resolved map coverage')
    for p,h in before.items():ck(info(p)['sha256']==h)
    aliases={p:v for p,v in groups.items() if len(v)>1}
    ck(len(spellings)==35 and len(groups)==32 and len(aliases)==3)
    ck({Path(p).name for p in aliases}=={'libncursesw.so.6.6','libtinfow.so.6.6','libz.so.1.3.2'})
    ck(load(dest/'RECEIPT.json')['libraries_count']==35)
    return dict(raw_distinct_spellings=len(spellings),canonical_distinct_files=len(groups),
        alias_groups=aliases,all_resolutions=groups,exact_before_after_map_coverage=True,
        missing_resolved_files=[],extra_pinned_files=[])
def audit(final):
    baseline=load(WORK/'INPUTS_BEFORE.json')
    for p,v in baseline.items():mapped_check(p,v,final)
    archived=entries(WORK/'initial_snapshot/SHA256SUMS');ck(len(archived)==743)
    preserved=[]
    for rel,h in archived.items():
        p=OUT/rel;q=snapshot_path(p) if final else p
        ck(info(q)['sha256']==h,rel)
        preserved.append(dict(original=rel,preserved=str(q.relative_to(OUT)),sha256=h))
    ck(info(WORK/'initial_snapshot/SHA256SUMS')['sha256']==INITIAL)
    strict=entries(RR/'SHA256SUMS');ck(len(strict)==38)
    ck(info(RR/'SHA256SUMS')['sha256']==ROOT_SEAL)
    for rel,h in strict.items():ck(info(RR/rel)['sha256']==h)
    ck(set(strict)=={str(p.relative_to(RR)) for p in RR.rglob('*') if p.is_file() and p!=RR/'SHA256SUMS'})
    r=load(RR/'RECEIPT.json');ck(r['status']=='PASS_ROOT_P208_STRICT_PAIR')
    ck(len(r['commands'])==7 and len(r['runs'])==2 and not r['failures'])
    for cmd in r['commands']:
        ck(cmd['exit_code']==0)
        for stream in ['stdout','stderr']:
            ck(info(RR/cmd[stream]['path'])=={k:cmd[stream][k] for k in ['sha256','bytes']})
        ck(load(RR/(cmd['label']+'.command.json'))==cmd)
    rootmap=load(RR/'INPUTS_BEFORE.json');ck(rootmap==load(RR/'INPUTS_AFTER.json'));ck(len(rootmap)==1878)
    root_relocations=[]
    for p,v in rootmap.items():
        q=mapped_check(p,v,final)
        if str(q)!=p:root_relocations.append(dict(original=p,preserved=str(q),historical=v))
    if final:ck({Path(p['original']).name for p in root_relocations}=={'FINDINGS.json','SHA256SUMS'})
    for stem,count in [('RUNTIME_INVENTORY',918),('LIBRARIES',112)]:
        a=load(RR/(stem+'_BEFORE.json'));ck(a==load(RR/(stem+'_AFTER.json')));ck(len(a)==count)
        for p,v in a.items():ck(info(p)==v)
    conf=load(RR/'CONFIGURATION_BEFORE.json');ck(conf==load(RR/'CONFIGURATION_AFTER.json'));ck(len(conf)==29)
    for p,v in conf.items():
        ck(Path(p).exists()==v['exists']);ck(str(Path(p).resolve())==v['resolved'])
        if 'sha256' in v:ck(info(p)=={k:v[k] for k in ['sha256','bytes']})
    for label in ['run1','run2']:
        payload=load(RR/(label+'.stdout'))
        ck(payload['assertions']==130961 and sum(b['states'] for b in payload['boxes'])==2055)
        ck((RR/(label+'.stdout')).read_bytes()==(OUT/'CANONICAL.json').read_bytes())
        runtime=load(RR/(label+'_CONSUMED_RUNTIME.json'))
        ck(runtime['optimize']==0 and runtime['isolated']==runtime['no_site']==1 and runtime['dont_write_bytecode'])
        ck(runtime['cache_absent'] and not Path(runtime['pycache_prefix']).exists())
        ck(runtime['environment']==ENV)
        actual=[v for v in runtime['modules'].values() if 'path' in v]
        ck(len(actual)==43 and len(runtime['mapped_files'])==12)
        for v in actual:ck(info(v['path'])['sha256']==v['sha256'])
        for p,h in runtime['mapped_files'].items():ck(info(p)['sha256']==h)
    rootpayload=load(BATCH/'qa/P208_A_ROOT_PAYLOAD_INSPECTION.actual.json')
    ck(rootpayload['status']=='PASS' and rootpayload['assertions']==18695 and rootpayload['author_records_compared']==2055)
    aliases={label:alias_audit(label) for label in ['cold07','cold08']}
    if final:
        ledger=load(OUT/'FINDINGS.json')
        ck(ledger['delta_accepted'] and ledger['stage']=='ACCEPTED_DOCUMENTARY_DELTA')
        ck(sum(ledger['census']['open'].values())==0)
        ck(ledger['census']['resolved']==dict(critical=0,major=4,minor=1))
        old=load(WORK/'initial_snapshot/FINDINGS.json')
        ck(ledger['findings'][:4]==old['findings'])
        ck(ledger['findings'][-1]['id']=='P208-A-ART1' and ledger['findings'][-1]['status']=='resolved')
        ck((OUT/'LIBRARY_COUNT_SUPPLEMENT.md').is_file() and (OUT/'DELTA.md').is_file())
        ck(info(OUT/'REPLAY_LOG.md')['sha256']==archived['REPLAY_LOG.md'])
    now=runtime_now()
    for p,v in {**now['modules'],**now['mapped_files']}.items():ck(baseline.get(p)==v,('audit runtime before coverage',p))
    print(json.dumps(dict(status='PASS_DOCUMENTARY_DELTA_AUDIT' if final else 'PASS_LIBRARY_COUNT_AUDIT',
        assertions=COUNT,initial_payloads_preserved=743,baseline_referents=len(baseline),
        aliases=aliases,root_pair_commands=7,root_pair_states_per_run=2055,
        root_pair_assertions_per_run=130961,root_pair_historical_relocations=root_relocations,
        initial_payload_mapping=preserved if final else None,runtime=now,
        mathematical_execution_performed=False,TeX_execution_performed=False),sort_keys=True,indent=2))
def run(label,final):
    dest=WORK/label;dest.mkdir()
    cache=dest/'unused_pycache';ck(not cache.exists())
    argv=[sys.executable,'-I','-S','-B','-X','pycache_prefix='+str(cache),__file__,'--child',str(int(final))]
    start=time.time_ns();p=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True)
    rawsave(dest/'audit.stdout',p.stdout);rawsave(dest/'audit.stderr',p.stderr)
    dump(dest/'COMMAND.json',dict(argv=argv,cwd=str(ROOT),environment=ENV,start_ns=start,end_ns=time.time_ns(),
        exit_code=p.returncode,stdout=info(dest/'audit.stdout'),stderr=info(dest/'audit.stderr')))
    ck(p.returncode==0,('actual child failed',p.stderr.decode()))
    result=load(dest/'audit.stdout')
    print(json.dumps({k:result[k] for k in ['status','assertions','initial_payloads_preserved','baseline_referents',
        'root_pair_historical_relocations','mathematical_execution_performed','TeX_execution_performed']},indent=2))
def close():
    result=load(WORK/'audit02/audit.stdout');ck(result['status']=='PASS_DOCUMENTARY_DELTA_AUDIT')
    baseline=load(WORK/'INPUTS_BEFORE.json')
    after={p:dict(pin_path=str(snapshot_path(p)),**info(snapshot_path(p)),
        historical_document_relocated=str(snapshot_path(p))!=p) for p in baseline}
    for p,v in baseline.items():ck(after[p]['sha256']==v['sha256'] and after[p]['bytes']==v['bytes'])
    dump(WORK/'INPUTS_AFTER.json',after)
    dump(WORK/'ROOT_RESPONSE_PINS_AFTER.json',{p:info(p) for p in load(WORK/'ROOT_RESPONSE_PINS_BEFORE.json')})
    ck(load(WORK/'ROOT_RESPONSE_PINS_BEFORE.json')==load(WORK/'ROOT_RESPONSE_PINS_AFTER.json'))
    changed=[]
    for name in ['FINDINGS.json','SHA256SUMS']:
        p=OUT/name;q=snapshot_path(p)
        changed.append(dict(original=str(p),historical_preserved=str(q),historical=info(q),
            current=info(p) if name=='FINDINGS.json' else None,
            current_manifest_boundary='Final top-level nonself seal is generated last and cannot hash itself.' if name=='SHA256SUMS' else None))
    dump(WORK/'DOCUMENTARY_RELOCATION.json',dict(changed_existing_documentary_refs=changed,
        all_other_initial_payloads_unchanged_in_place=742,
        exact_root_pair_relocations=result['root_pair_historical_relocations'],
        current_snapshot_is_not_the_initial_743_entry_tree=True))
    dump(WORK/'INITIAL_PAYLOAD_MAPPING.json',result['initial_payload_mapping'])
    # Capture the final delta/current ledger and documentary supplement without a self-hash.
    docs=['DELTA.md','FINDINGS.json','LIBRARY_COUNT_SUPPLEMENT.md','delta_audit.py']
    dump(WORK/'CHANGED_DOCUMENTS_AFTER.json',{rel:info(OUT/rel) for rel in docs})
    receipt=WORK/'FINAL_SEAL_RECEIPT.json'
    paths=[p for p in OUT.rglob('*') if p.is_file() and p!=OUT/'SHA256SUMS']
    dump(receipt,dict(status='PASS_ACCEPTED_DOCUMENTARY_DELTA_CLOSURE',time_ns=time.time_ns(),
        initial_manifest_sha256=INITIAL,final_nonself_referents=len(paths)+1,
        audit_assertions=result['assertions'],science_unchanged=True,
        note='Initial manifest is preserved; current final manifest is excluded from its own payload and replaced only at this last step.'))
    ck(info(OUT/'SHA256SUMS')['sha256']==INITIAL,'only expected initial seal is replaced')
    paths=sorted(p for p in OUT.rglob('*') if p.is_file() and p!=OUT/'SHA256SUMS')
    (OUT/'SHA256SUMS').write_text(''.join(f'{info(p)["sha256"]}  {p.relative_to(OUT)}\n' for p in paths))
    declared=entries(OUT/'SHA256SUMS');ck(len(declared)==len(paths))
    ck(set(declared)=={str(p.relative_to(OUT)) for p in paths})
    for rel,h in declared.items():ck(info(OUT/rel)['sha256']==h)
    print(json.dumps(dict(status='PASS',nonself_referents=len(declared),
        final_manifest_sha256=info(OUT/'SHA256SUMS')['sha256'],
        delta_sha256=info(OUT/'DELTA.md')['sha256'],
        current_findings_sha256=info(OUT/'FINDINGS.json')['sha256']),indent=2))
if __name__=='__main__':
    ck(sys.flags.optimize==0 and sys.flags.isolated==sys.flags.no_site==1 and sys.dont_write_bytecode)
    if sys.argv[1]=='prepare':prepare()
    elif sys.argv[1]=='--child':audit(bool(int(sys.argv[2])))
    elif sys.argv[1]=='run':run(sys.argv[2],bool(int(sys.argv[3])))
    elif sys.argv[1]=='close':close()
