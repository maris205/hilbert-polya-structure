"""Post-commitment whole-transcript adapter, not the independent checker."""
import collections
import hashlib
import json
import pathlib

D = pathlib.Path(__file__).resolve().parent
F = D.parents[3]/'papers/210-weakly-increasing-run-aggregation/frozen_round0'
paths = [D/'CANONICAL.json', F/'CANONICAL.json', pathlib.Path(__file__)]
def pins():
    return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before = pins()
a = json.loads((D/'CANONICAL.json').read_bytes())
b = json.loads((F/'CANONICAL.json').read_bytes())
checks = collections.Counter()
def eq(x,y,kind):
    checks[kind] += 1
    assert x == y,(kind,x,y)
def keys(x,k):
    eq(set(x),set(k.split()),'exact_keys')
def parts(n,m):
    ends=[0]+[i for i in range(1,n) if m & (1<<(i-1))]+[n]
    return [y-x for x,y in zip(ends,ends[1:])]
def mask(p):
    pos=m=0
    for x in p[:-1]:
        pos+=x;m|=1<<(pos-1)
    return m
def intervals(p):
    pos=0;out=[]
    for x in p:
        out.append([pos,pos+x]);pos+=x
    return out
keys(b,'schema mass_box parameters masses totals checks_by_kind checks')
eq(b['schema'],'P210_AUTHOR_FULL_CANONICAL_V1','schema')
eq(b['mass_box'],[1,12],'box')
eq(b['parameters'],{'positive_parts':True,'old_part_synchronous':True,'external_data':False},'parameters')
eq(len(b['masses']),12,'mass_count')
eq(b['checks'],sum(b['checks_by_kind'].values()),'author_internal_count_sum')
eq(b['checks'],197471,'author_internal_count_record_not_independent_count')
eq(all(isinstance(x,int) and x>0 for x in b['checks_by_kind'].values()),True,'author_internal_positive_counts')
total_image=total_witnesses=0
for independent,author in zip(a['tables'],b['masses']):
    keys(author,'N states targets fixed_points triangular_objects witnesses endpoint_partition_coefficients summary')
    n=independent['N'];eq(author['N'],n,'mass')
    state_rows=independent['states'];target_rows=independent['targets']
    eq(len(author['states']),len(state_rows),'state_count')
    eq([r['state'] for r in author['states']],sorted(parts(n,m) for m in range(1<<(n-1))),'complete_ordered_states')
    for row in author['states']:
        keys(row,'state edge depth fixed_endpoint orbit birth_rounds')
        own=state_rows[mask(row['state'])]
        eq(row['edge'],parts(n,own[1]),'edge')
        eq(row['depth'],own[2],'depth')
        eq(row['fixed_endpoint'],parts(n,own[3]),'endpoint')
        eq(row['orbit'],[parts(n,own[0])]+[parts(n,e[2]) for e in own[4]],'complete_orbit')
        eq(len(row['birth_rounds']),len(own[4]),'round_count')
        for event,e in zip(row['birth_rounds'],own[4]):
            keys(event,'round old new deleted_cuts new_blocks')
            eq(event['round'],e[0],'round_time')
            eq(event['old'],parts(n,e[1]),'round_old')
            eq(event['new'],parts(n,e[2]),'round_new')
            eq(event['deleted_cuts'],[dict(zip(['cut','left_mass','right_mass','right_birth'],r)) for r in e[3]],'all_deleted_cuts')
            old=intervals(event['old'])
            expected=[]
            for left,right,time in e[4]:
                expected.append({'interval':[left,right],'mass':right-left,'parents':[p for p in old if left<=p[0] and p[1]<=right]})
            eq(event['new_blocks'],expected,'all_births_and_parents')
    eq(len(author['targets']),len(target_rows),'target_count')
    eq([r['target'] for r in author['targets']],sorted(parts(n,m) for m in range(1<<(n-1))),'complete_ordered_targets')
    for row in author['targets']:
        keys(row,'target fibre sources suffixes image code')
        own=target_rows[mask(row['target'])]
        eq(row['sources'],sorted(parts(n,m) for m in own[2]),'complete_source_set')
        eq(row['fibre'],own[5],'fibre')
        eq(row['image'],bool(own[2]),'image')
        eq(row['code'],own[6],'encoding')
        s=row['target'];eq(len(row['suffixes']),len(s),'suffix_count')
        for i,suffix in enumerate(row['suffixes']):
            keys(suffix,'index part threshold branch attainable_first_parts first_part_counts attaining_preimage')
            eq(suffix['index'],i,'suffix_index');eq(suffix['part'],s[i],'suffix_part')
            tail=s[i:];mass=sum(tail)
            src=a['tables'][mass-1]['targets'][mask(tail)][2]
            first=collections.Counter(parts(mass,m)[0] for m in src)
            minfirst=min(first) if first else None
            eq(suffix['threshold'],minfirst,'every_attained_minimum')
            eq(suffix['attainable_first_parts'],sorted(first),'every_attained_set')
            eq(suffix['first_part_counts'],[list(x) for x in sorted(first.items())],'every_first_count')
            if i==len(s)-1:branch='initial'
            elif not own[3][i+1]:branch='infeasible_suffix'
            else:
                r=min(own[3][i+1])
                branch='fail' if s[i]<=r else 'increment' if s[i]==r+1 else 'reset'
            eq(suffix['branch'],branch,'every_scan_branch')
            w=suffix['attaining_preimage']
            if minfirst is None: eq(w,None,'no_infeasible_witness')
            else:
                eq(sum(w),mass,'witness_mass');eq(w[0],minfirst,'witness_attainment')
                eq(mask(w) in src,True,'witness_actual_source_membership')
    fixed=sorted(parts(n,r[0]) for r in state_rows if r[2]==0)
    eq(author['fixed_points'],fixed,'complete_fixed_set')
    expected_tri=sorted([{'parts':r[1],'decoded_target':r[2]} for r in independent['triangular']],key=lambda x:x['parts'])
    eq(author['triangular_objects'],expected_tri,'all_triangular_decodings')
    expected_w=[{'h':r[0],'surplus':r[1],'state':r[2],'orbit':[parts(n,m) for m in r[3]]} for r in independent['witnesses']]
    eq(author['witnesses'],expected_w,'all_surplus_orbits')
    refinements=[parts(n,m) for m in range(1<<(n-1)) if all(x<=y for x,y in zip(parts(n,m),parts(n,m)[1:]))]
    coeff=[[x,y,sum(r[0]==x and r[-1]==y for r in refinements)] for x in range(1,n+1) for y in range(x,n+1)]
    eq(author['endpoint_partition_coefficients'],coeff,'all_endpoint_coefficients')
    hist=collections.Counter(r[2] for r in state_rows)
    summary={'states':len(state_rows),'fixed':len(fixed),'depth_histogram':[list(x) for x in sorted(hist.items())],
             'max_depth':max(hist),'H':independent['H'],'image':independent['image_count'],
             'triangular_count':len(expected_tri),'witness_count':len(expected_w)}
    eq(author['summary'],summary,'all_mass_summary_fields')
    total_image+=len(expected_tri);total_witnesses+=len(expected_w)
eq(b['totals'],{'states':4095,'edges':4095,'targets':4095,'image_objects':total_image,
               'triangular_objects':total_image,'surplus_witnesses':total_witnesses},'whole_totals')
after=pins();eq(before,after,'unchanged_complete_inputs')
print(json.dumps({'status':'PASS','role':'whole author canonical semantic comparison after independent commitment; not raw byte equality across different schemas',
                 'inputs_before':before,'inputs_after':after,'checks':sum(checks.values()),'checks_by_kind':dict(sorted(checks.items())),
                 'independent_scientific_checks':a['checks'],'state_count':4095,'image_objects':total_image,'surplus_witnesses':total_witnesses,
                 'author_metadata_limit':'author assertion categories/census checked internally for consistency, not equated with independent execution count',
                 'noninterval_example':{'target':[6],'actual_first_parts':a['tables'][5]['targets'][0][3][0]}},sort_keys=True,indent=2))
