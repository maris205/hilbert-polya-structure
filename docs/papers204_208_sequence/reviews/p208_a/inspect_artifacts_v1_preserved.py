"""Read all author canonical records and compare against A without executing author code."""
from pathlib import Path
import hashlib,json,sys,runpy,collections,subprocess,os,time
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
OUT=ROOT/'docs/papers204_208_sequence/reviews/p208_a'
F=ROOT/'papers/208-original-snapshot-triangulation-sweeps/frozen_round0'
COUNT=0
def ck(test,detail=''):
    global COUNT
    COUNT+=1
    if not test:raise AssertionError((COUNT,detail))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def tupled(x):return tuple(tupled(y) for y in x) if isinstance(x,list) else x
def tword(t):return '.' if not t else '('+tword(t[0])+tword(t[1])+')'
def ds(faces):
    edges=collections.Counter(e for a,b,c in faces for e in [(a,b),(a,c),(b,c)])
    return tuple(sorted(e for e,m in edges.items() if m==2))
def audit():
    for line in (OUT/'INPUT_PINS.sha256').read_text().splitlines():
        h,rel=line.split('  ',1);ck(sha(ROOT/rel)==h,rel)
    for name in ['SHA256SUMS','AUTHOR_MANIFEST.sha256']:
        declared={}
        for line in (F/name).read_text().splitlines():
            h,rel=line.split('  ',1);ck(sha(F/rel)==h,rel);declared[rel]=h
        if name=='SHA256SUMS':ck(set(declared)=={str(p.relative_to(F)) for p in F.rglob('*') if p.is_file() and p!=F/name},'freeze nonself closure')
    a=json.loads((F/'CANONICAL.json').read_bytes());b=json.loads((OUT/'CANONICAL.json').read_bytes())
    ck(a['total_states']==sum(v['states'] for v in b['boxes'])==2055)
    allrows=[]
    for ar,br in zip(a['rows'],b['boxes']):
        n=ar['n'];ck(n==br['n']);rows={r['word']:r for r in br['rows']}
        bydiag={ds(r['faces']):r for r in br['rows']}
        ck(len(rows)==len(bydiag)==ar['states']==br['states'])
        ck(ar['maximum_fibre']==br['max_fibre']);ck(ar['maximum_height']==br['max_entrance'])
        ck(tupled(ar['all_maximum_targets'])==tuple(sorted(ds(rows[w]['faces']) for w in br['maximizers'])))
        table=[];fh=collections.Counter();hh=collections.Counter();core=[]
        for r in ar['complete_graph_and_sources']:
            w=tword(r['tree']);x=rows[w];d=ds(x['faces'])
            ck(d==tupled(r['diagonals']))
            ck(ds(rows[x['output']]['faces'])==tupled(r['next_diagonals']))
            ck(x['entrance']==r['height']);ck(len(x['sources'])==r['fibre'])
            ck(tuple(sorted(ds(rows[s]['faces']) for s in x['sources']))==tupled(r['source_diagonals']))
            ck(ds(rows[x['k_output']]['faces'])==tupled(r['K_next_diagonals']))
            ck(x['k_entrance']==r['K_height'])
            table.append([r['diagonals'],r['next_diagonals'],r['height'],r['fibre']])
            fh[r['fibre']]+=1;hh[r['height']]+=1
            if not r['height']:core.append(d)
        ck(hashlib.sha256(json.dumps(table,separators=(',',':')).encode()).hexdigest()==ar['literal_transition_depth_fibre_sha256'])
        ck(tuple(sorted(core))==tupled(ar['core_diagonals']))
        ck(tuple(sorted(fh.items()))==tupled(ar['fibre_histogram']))
        ck(tuple(sorted(hh.items()))==tupled(ar['height_histogram']))
        ck(max(r['k_entrance'] for r in rows.values())==ar['K_maximum_height'])
        ck(sum(len(r['sources']) for r in rows.values())==br['states'])
        ck(ar['image']==sum(1 for r in rows.values() if r['sources']))
        if n>=5:
            trajectory=tupled(ar['sharp_witness_full_orbit'])
            ck(trajectory[0]==tupled(ar['sharp_witness_diagonals']))
            for p,q in zip(trajectory,trajectory[1:]):ck(ds(rows[bydiag[p]['output']]['faces'])==q)
            ck(bydiag[trajectory[-1]]['entrance']==0 and bydiag[trajectory[-2]]['entrance']==1)
        allrows.append(dict(n=n,states=br['states'],image=ar['image'],K_image=len({r['k_output'] for r in rows.values()}),max_fibre=br['max_fibre'],max_entrance=br['max_entrance']))
    for label in ['cold05','cold06']:
        d=OUT/label;r=json.loads((d/'RECEIPT.json').read_text());ck(r['status']=='PASS')
        for stem in ['INPUTS','TOOLS','LIBRARIES']:
            p=json.loads((d/(stem+'_BEFORE.json')).read_text());q=json.loads((d/(stem+'_AFTER.json')).read_text())
            ck(p==q,(label,stem))
            for name,h in q.items():ck(sha(name)==h,name)
        runtime=json.loads((d/'CONSUMED_RUNTIME.json').read_text());ck(runtime['flags']==dict(optimize=0,isolated=1,dont_write_bytecode=True))
        before=json.loads((d/'RUNTIME_INVENTORY_BEFORE.json').read_text());after=json.loads((d/'RUNTIME_CONSUMED_AFTER.json').read_text())
        for name,h in runtime['modules'].items():ck(before[name]==after[name]==h==sha(name),name)
        for labelcmd in ['producer','canonical_cmp','python_ldd','extensions_ldd']:
            cmd=json.loads((d/(labelcmd+'.json')).read_text());ck(cmd['exit']==0)
            for key in ['stdout','stderr']:ck(Path(cmd[key]).is_file())
    bd=OUT/'build02';receipt=json.loads((bd/'RECEIPT.json').read_text());ck(receipt['pages']==7)
    for stem in ['INPUTS','TOOLS','LIBRARIES','CONSUMED_TEX']:
        p=json.loads((bd/(stem+'_BEFORE.json')).read_text());q=json.loads((bd/(stem+'_AFTER.json')).read_text());ck(p==q)
        for name,h in q.items():ck(sha(name)==h,name)
    ck(receipt['warnings']['underfull']==['Underfull \\hbox (badness 5681) in paragraph at lines 9--13'])
    ck(receipt['warnings']['undefined']==receipt['warnings']['overfull']==[])
    # All seven author origin referents match immutable historical copies.
    historical=ROOT/'docs/papers204_208_sequence/qa/p208_round0_input_inspection_v2/historical_workspace_origins'
    origin_rows=[]
    for line in (F/'provenance/INPUT_ORIGINS.sha256').read_text().splitlines():
        h,rel=line.split('  ',1);ck(sha(historical/rel)==h)
        origin_rows.append(dict(path=rel,historical_sha256=h,current_sha256=sha(ROOT/rel),current_equals_historical=sha(ROOT/rel)==h))
    print(json.dumps(dict(status='PASS',assertions=COUNT,author_records_compared=2055,rows=allrows,origin_contexts=origin_rows,
        scope='Whole author JSON scientific payload read and compared, not author code re-execution; original freezes and final A before/after dependency keys verified.'),sort_keys=True,indent=2))

def main():
    if len(sys.argv)>1 and sys.argv[1]=='--child':audit();return
    helper=runpy.run_path(str(OUT/'record.py'));pins,dump,command=[helper[k] for k in ('pins','dump','command')]
    dest=OUT/'artifact_inspection';dest.mkdir()
    inputs=[p for p in F.rglob('*') if p.is_file()]+[p for p in OUT.rglob('*') if p.is_file() and not p.is_relative_to(dest)]
    before=pins(inputs);dump(dest/'INPUTS_BEFORE.json',before)
    modules=[Path(m.__file__).resolve() for m in tuple(sys.modules.values()) if getattr(m,'__file__',None) and Path(m.__file__).is_file()]
    tools=pins([sys.executable,'/usr/bin/cmp',__file__,OUT/'record.py',*modules]);dump(dest/'TOOLS_BEFORE.json',tools)
    env={'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC','PYTHONOPTIMIZE':'0','PYTHONDONTWRITEBYTECODE':'1'}
    for label,left,right in [('canonical05',OUT/'cold05/producer.stdout',OUT/'CANONICAL.json'),('canonical06',OUT/'cold06/producer.stdout',OUT/'CANONICAL.json'),('pair',OUT/'cold05/producer.stdout',OUT/'cold06/producer.stdout'),('build_pair',OUT/'build01/source_only/main.pdf',OUT/'build02/source_only/main.pdf')]:
        command(['/usr/bin/cmp',str(left),str(right)],OUT,env,dest/label)
    command([sys.executable,'-I','-B',__file__,'--child'],ROOT,env,dest/'audit')
    dump(dest/'INPUTS_AFTER.json',pins(inputs));ck(pins(inputs)==before)
    dump(dest/'TOOLS_AFTER.json',pins(tools));ck(pins(tools)==tools)
    dump(dest/'RECEIPT.json',dict(status='PASS',inputs=len(inputs),read_only=True,all_five_child_exits_zero=True))
    print((dest/'audit.stdout').read_text())

if __name__=='__main__':main()
