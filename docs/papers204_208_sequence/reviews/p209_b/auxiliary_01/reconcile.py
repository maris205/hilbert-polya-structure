"""Postcommitment full scientific-payload reconciliation, not a producer.

No author/A/B mathematical code import. Derive their row representations
from B's actual complete state/output/parent data and compare every field.
Only verifier-specific assertion counters and top-level scope/schema text
are excluded from mathematical projection. Never raw-compare unlike schemas.
"""
import json
from pathlib import Path
import sys

W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
F=W/'papers/209-ordered-fibre-threading/frozen_round1'
A=W/'docs/papers204_208_sequence/reviews/p209_a'
checks=0
def require(test, context):
    global checks
    checks+=1
    if not test: raise AssertionError(context)

def graph_fields(f, row):
    n=len(f)
    cycles=set()
    for start in range(n):
        orbit=[]; pos={}; v=start
        while v not in pos:
            pos[v]=len(orbit); orbit.append(v); v=f[v]
        cyc=orbit[pos[v]:]
        pivot=cyc.index(min(cyc))
        cycles.add(tuple(cyc[pivot:]+cyc[:pivot]))
    cycles=[list(c) for c in sorted(cycles)]
    cyclic=sorted({v for c in cycles for v in c})
    noncyclic=set(range(n))-set(cyclic)
    indegree=[f.count(v) for v in range(n)]
    paths=[]
    if row['recurrent']:
        for start in sorted(v for v in noncyclic if indegree[v]==0):
            path=[]; v=start
            while v in noncyclic:
                path.append(v); v=f[v]
            paths.append({'vertices':path,'attachment':v})
    return {'cycles':cycles,'cycle_vertices':cyclic,'indegree':indegree,
            'paths':paths,'finals':sorted(v for v in noncyclic if f[v] in cyclic),
            'recurrent_predicate':row['recurrent'],
            'predicted_period':row['carrier']['period'] if row['recurrent'] else None}

def main():
    require(sys.flags.optimize==0,'optimization')
    b=json.loads((B/'CANONICAL.json').read_bytes())
    author=json.loads((F/'CANONICAL.json').read_bytes())
    a=json.loads((A/'CANONICAL.json').read_bytes())
    author_projected=[]; a_projected=[]
    full_comparisons=[]
    for bb,ab,aa in zip(b['boxes'],author['boxes'],a['boxes']):
        n=bb['n']; states=[row['f'] for row in bb['rows']]
        require(n==ab['n']==aa['n'],'box n')
        require(len(states)==ab['state_count']==aa['state_count'],'state census')
        reconstructed=[]; reconstructed_a=[]
        per_census={}; fibre_census={}
        for row,ar,rr in zip(bb['rows'],ab['rows'],aa['records']):
            i=row['rank']; f=row['f']
            require(f==states[i],'rank order')
            image=states[row['T_rank']]
            graph=graph_fields(f,row)
            current=set(range(n)); images=[]
            for _ in range(n+2):
                images.append(sorted(current)); current={f[v] for v in current}
            orbit=[]; v=i; seen=set()
            while v not in seen:
                seen.add(v); orbit.append(states[v]); v=bb['rows'][v]['T_rank']
            eligible=[j for j in range(n) if j<f[j]]
            codes=[]
            for parent in row['predecessors']:
                source=states[parent]
                selected=[j for j in range(n) if any(source[j]==source[k] for k in range(j+1,n))]
                endpoints=[]
                for j in range(n):
                    while j in selected: j=f[j]
                    endpoints.append(j)
                codes.append({'selected':selected,'endpoints':endpoints,'source':source})
            codes.sort(key=lambda c:sum(1<<eligible.index(j) for j in c['selected']))
            rebuilt={'state':f,'image':image,'vertex_images':images,'graph':graph,
                     'entrance_steps_observed':row['entrance'],
                     'whole_function_period':row['period'],'whole_orbit':orbit,
                     'eligible':eligible,'inverse_codes':codes,
                     'literal_predecessors':[states[p] for p in row['predecessors']],
                     'fibre_size':len(row['predecessors'])}
            require(set(rebuilt)==set(ar),('author row schema',n,i))
            for key in rebuilt: require(rebuilt[key]==ar[key],('author',n,i,key,rebuilt[key],ar[key]))
            reconstructed.append(rebuilt)
            if row['recurrent']: per_census[row['period']]=per_census.get(row['period'],0)+1
            size=len(row['predecessors']); fibre_census[size]=fibre_census.get(size,0)+1
            reb_a={'f':f,'image_rank':row['T_rank'],'entrance':row['entrance'],
                   'period':row['period'],'recurrent':row['recurrent'],
                   'carrier_period':row['period'] if row['recurrent'] else None,
                   'cycle_sccs':[sorted(c) for c in graph['cycles']],
                   'inverse_ranks':row['predecessors'],
                   'inverse_masks':sorted(sum(1<<j for j in c['selected']) for c in codes)}
            require(set(reb_a)==set(rr),('A row schema',n,i))
            for key in reb_a: require(reb_a[key]==rr[key],('A',n,i,key))
            reconstructed_a.append(reb_a)
            full_comparisons.append({'n':n,'rank':i,'author_fields':len(rebuilt),'A_fields':len(reb_a),'status':'ALL_EQUAL'})
        maximum=max(fibre_census)
        maximum_ranks=[i for i,row in enumerate(bb['rows']) if len(row['predecessors'])==maximum]
        rebuilt_box={'n':n,'state_count':len(states),'recurrent_count':bb['recurrent'],
                     'recurrent_period_census':[list(x) for x in sorted(per_census.items())],
                     'fibre_census':[list(x) for x in sorted(fibre_census.items())],
                     'maximum_fibre':maximum,'maximizing_targets':[states[i] for i in maximum_ranks],
                     'rows':reconstructed}
        require({k:v for k,v in ab.items() if k!='checks'}==rebuilt_box,('author whole box',n))
        # Bell count in A is its independent auxiliary partition-enumeration
        # census; verify it via the elementary Bell recurrence, not A code.
        bell=[1]
        for k in range(n):
            from math import comb
            bell.append(sum(comb(k,j)*bell[j] for j in range(k+1)))
        rebuilt_a_box={'n':n,'state_count':len(states),'partition_count':bell[n],
                       'maximum_fibre':maximum,'extremizer_ranks':maximum_ranks,
                       'records':reconstructed_a}
        require(rebuilt_a_box==aa,('A whole box',n))
        author_projected.append(rebuilt_box); a_projected.append(rebuilt_a_box)
    require(len(full_comparisons)==3414,'all 3414 original rows')
    out=Path(sys.argv[1])
    for name,value in [('author_projection.json',[{k:v for k,v in box.items() if k!='checks'} for box in author['boxes']]),
                       ('B_to_author_projection.json',author_projected),
                       ('A_projection.json',a['boxes']),('B_to_A_projection.json',a_projected)]:
        with (out/name).open('x') as stream:
            stream.write(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'status':'PASS_FULL_MATHEMATICAL_PAYLOAD_RECONCILIATION','checks':checks,
                     'row_count':len(full_comparisons),'rows':full_comparisons,
                     'normalization':'Only author assertion counters and top-level schemas/scope omitted; all author row fields, all A rows and all mathematical box fields compared. Unlike canonicals are not raw-equal.'},sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
