"""SOURCE ONLY: root reception of every saved B field, no producer imports.

Disclosed forward design from the fully read A saved-output receiver.
B histograms are reconstructed from whole nondecreasing value tuples;
literal arrows and forward orbits determine graph data, independently of
the claimed clock. Full target descriptions are recovered from actual
incoming sources, and all kernel-option/binomial/Laurent records are checked.
Later invocation requires exact received runtime binding/output byte pins.
"""
from hashlib import sha256
import itertools
import json
import math
from pathlib import Path
import sys

SOURCE_SHA = '6888ea1df1c20e4786c3582a61fcc5c7d6c8901d9e322d16dc50b047786c5fa7'
PARAMETER_SHA = '214b1832a5aae184bd0617334307d87cdcb51f29d2b41983593bdae2d5fc2cac'
CATEGORIES = [
    'B01_carrier_and_encoding','B02_literal_histogram_update',
    'B03_support_identity_and_normalization','B04_composition_certificate',
    'B05_fixed_recurrent_terminal','B06_pointwise_clock','B07_boundary_lifetimes',
    'B08_image_iff_and_witness','B09_kernel_first_decoder','B10_rank_branch_binomial_counts',
    'B11_laurent_identity_and_total_mass','B12_sharp_parity_and_boundaries']
EXPECTED_PARAMETERS = {
    'schema':'p211-b-parameters-v1','n_values':[1,2,3,4,5,6,7],
    'carrier_sizes':[1,3,10,35,126,462,1716],'expected_total_states':2353,
    'carrier':'all_nondecreasing_maps_[n]_to_[n]_without_initial_restrictions',
    'representation':'weak_composition_histograms_and_stars_bars_paths',
    'graph_method':'whole_carrier_successive_composition_tables_full_carrier_guard',
    'inverse_method':'kernel_first_last_kernel_cut_then_global_fixed_size_image_subsets',
    'output_schema':'p211-b-complete-path-certificate-v1',
    'ordering':'n_ascending_histogram_lexicographic_ids_kernel_masks_ascending_sources_by_id',
    'serialization':'JSON_sort_keys_ensure_ascii_compact_allow_nan_false_plus_single_LF',
    'predicate_categories':CATEGORIES,
    'excluded_claims':['global_fibre_maximum_or_maximizers','basin_cardinality_formulas',
        'all_time_inverse_formulas','global_priority_or_no_factor_no_lift_theorems']}
CHECKS = 0
READS = {}

def need(ok, detail):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(detail)

def compact(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)

def same(got, wanted, detail):
    need(compact(got)==compact(wanted), ('complete typed equality',detail))

def unique(pairs):
    result = {}
    for k,v in pairs:
        need(k not in result, ('duplicate object key',k))
        result[k] = v
    return result

def bad_number(value):
    raise ValueError('floating/nonfinite JSON number not allowed: '+value)

def parse(data):
    return json.loads(data,object_pairs_hook=unique,parse_float=bad_number,parse_constant=bad_number)

def raw(path, digest):
    p = Path(path)
    need(p.is_absolute() and p.is_file() and p.resolve()==p and not p.is_symlink(), ('physical exact input',str(p)))
    data = p.read_bytes()
    need(sha256(data).hexdigest()==digest, ('entire prebound input',str(p)))
    need(str(p) not in READS or READS[str(p)]==data, ('unchanged input',str(p)))
    READS[str(p)] = data
    return data

def mask(sites):
    return sum(2**(i-1) for i in sorted(set(sites)))

def supports(values):
    n = len(values)
    ends = [i for i in range(1,n+1) if i==n or values[i-1]!=values[i]]
    return ends,[values[i-1] for i in ends]

def reconstruct(x,y,n):
    return tuple(y[next(j for j,end in enumerate(x) if end>=i)] for i in range(1,n+1))

def boundary(w,z,n):
    if z[-1]!=n or any(a>b for a,b in zip(w,z)) or any(z[j]>=w[j+1] for j in range(len(w)-1)):
        return None
    intervals,labels = [],[]
    for a,b in zip(w,z):
        if a!=b:
            labels += [a,b]
        else:
            tokens = [{'site':site,'initial_role':'K' if j%2==0 else 'V',
                       'death_epoch':min(j+1,len(labels)-j)} for j,site in enumerate(labels)]
            intervals.append({'anchor':a,'tokens':tokens})
            labels = []
    need(not labels, 'all strict intervals end at common anchors')
    return {'anchor_mask':mask(set(w)&set(z)),'intervals':intervals,
            'radius':max((t['death_epoch'] for g in intervals for t in g['tokens']),default=0)}

def coeffs(d):
    result = {e:0 for e in range(-d,d+1)}
    for a in range(d+1):
        for b in range(d-a+1):
            result[b-a] += math.comb(d,a+b)
    return result

def terms(poly):
    return [[e,c] for e,c in sorted(poly.items())]

def receive(binding_path,binding_sha,stdout_path,stdout_sha):
    need(sys.flags.isolated==sys.flags.no_site==1 and sys.flags.optimize==0 and sys.dont_write_bytecode,
         'isolated no-site no-bytecode unoptimized receiver')
    binding_raw = raw(binding_path,binding_sha)
    binding = parse(binding_raw)
    need(binding['format']=='p211-runtime-binding-v1' and binding['approved'] is True and
         binding['purpose']=='P211_MANUSCRIPT' and binding['role']=='B' and binding['mode'] in ('initial','pair'), 'exact B runtime binding')
    files = {r['name']:r for r in binding['capsule_files']}
    need(set(files)=={'verify.py','parameters.json'} and len(binding['capsule_files'])==2, 'exact two scientific inputs')
    for name,digest in (('verify.py',SOURCE_SHA),('parameters.json',PARAMETER_SHA)):
        item = files[name]
        body = raw(item['path'],digest)
        need(item['sha256']==digest and item['bytes']==len(body), 'entire scientific source/parameter metadata')
    same(parse(READS[files['parameters.json']['path']]),EXPECTED_PARAMETERS,'complete fixed parameter file')
    data = raw(stdout_path,stdout_sha)
    out = parse(data)
    need(data==(compact(out)+'\n').encode('ascii'), 'whole compact sorted ASCII object plus exactly one LF')
    for item in binding['schema']['equalities']:
        got = out
        for part in item['path']:
            got = got[part]
        same(got,item['value'],('bound equality',item['path']))
    for item in binding['schema']['lengths']:
        got = out
        for part in item['path']:
            got = got[part]
        need(len(got)==item['value'], ('bound length',item['path']))
    summaries, rebuilt = [],[]
    need(type(out.get('carriers')) is list and len(out['carriers'])==7, 'exact seven complete carriers')
    for n, saved in enumerate(out['carriers'],1):
        values = list(itertools.combinations_with_replacement(range(1,n+1),n))
        ordered = sorted((tuple(v.count(j) for j in range(1,n+1)),v) for v in values)
        histograms, states = [r[0] for r in ordered],[r[1] for r in ordered]
        ids = {state:i for i,state in enumerate(states)}
        count = len(states)
        need(count==EXPECTED_PARAMETERS['carrier_sizes'][n-1]==math.comb(2*n-1,n-1), 'complete weak composition population')
        arrows,cells = [],[]
        incoming = [[] for _ in states]
        boundaries = []
        for i,state in enumerate(states):
            x,y = supports(state)
            a = sorted(set(y)|{n})
            result = tuple(next(c for c in x if c>=next(d for d in a if d>=j)) for j in range(1,n+1))
            arrows.append(ids[result])
            incoming[ids[result]].append(i)
            previous,row = 0,[]
            for d in a:
                row.append({'inner_block_end':d,'block_width':d-previous,'outer_suffix_mask':mask(x)>>(d-1),
                            'assigned_output':next(c for c in x if c>=d)})
                previous = d
            cells.append(row)
            boundaries.append(boundary(x,y,n))
        times,terminals = [],[]
        for start in range(count):
            path,seen,vertex = [],{},start
            while vertex not in seen:
                seen[vertex] = len(path)
                path.append(vertex)
                vertex = arrows[vertex]
            need(len(path)-seen[vertex]==1, 'every literal orbit enters a fixed point')
            times.append(seen[vertex])
            terminals.append(vertex)
        height = max(times)
        tables = [list(range(count))]
        for _ in range(height+1):
            tables.append([arrows[v] for v in tables[-1]])
        need(tables[-1]==tables[-2], 'complete duplicated stable power')
        fixed = [i for i in range(count) if arrows[i]==i]
        need(fixed==[i for i,s in enumerate(states) if supports(s)[0]==supports(s)[1]] and len(fixed)==2**(n-1), 'whole fixed and recurrent set')
        image = [i for i in range(count) if incoming[i]]
        zero = [i for i in range(count) if not incoming[i]]
        records,option_total,survival_total = [],0,0
        for i,state in enumerate(states):
            w,z = supports(state)
            completed = sorted(set(z)|{n})
            anchor = sorted(set(w)&set(completed))
            predicted_terminal = ids[reconstruct(anchor,anchor,n)]
            predicted_time = 0 if w==z else 1+boundaries[arrows[i]]['radius']
            need(predicted_terminal==terminals[i] and predicted_time==times[i], 'literal full time and terminal predictions')
            image_boundary = boundaries[i]
            need((image_boundary is not None)==bool(incoming[i]), 'whole target image iff')
            survival = atlas = laurent = None
            if image_boundary is not None:
                need(times[i]==image_boundary['radius'], 'exact image clock')
                survival = []
                for t in range(image_boundary['radius']+2):
                    k,v = image_boundary['anchor_mask'],image_boundary['anchor_mask']
                    for group in image_boundary['intervals']:
                        for token in group['tokens']:
                            if t<token['death_epoch']:
                                role = token['initial_role'] if t%2==0 else ('V' if token['initial_role']=='K' else 'K')
                                if role=='K':
                                    k |= 2**(token['site']-1)
                                else:
                                    v |= 2**(token['site']-1)
                    actual_id = tables[t][i]
                    actual_k,actual_v = supports(states[actual_id])
                    need((mask(actual_k),mask(actual_v))==(k,v), 'every labelled endpoint lifetime against literal graph')
                    survival.append({'epoch':t,'kernel_mask':k,'image_mask':v,'state_id':actual_id})
                survival_total += len(survival)
                need(arrows[ids[reconstruct(z,w,n)]]==i, 'constructive transposed-support predecessor')
                gaps,previous = [],0
                for a,b in zip(w,z):
                    sites = list(range(previous+1,a))
                    gaps.append({'previous_output':previous,'target_end':a,'target_output':b,'sites':sites,'mask':mask(sites)})
                    previous = b
                free = sorted(site for gap in gaps for site in gap['sites'])
                options,branch_counts = [],[0,0]
                for sub in range(1<<n):
                    selected = [j for j in range(1,n+1) if sub & 2**(j-1)]
                    if not set(selected)<=set(free):
                        continue
                    last = [max([j for j in selected if j in gap['sites']],default=gap['previous_output']) for gap in gaps]
                    eligible = [j for gap,q in zip(gaps,last) for j in gap['sites'] if j>q]
                    a,e = len(selected),len(eligible)
                    branches = [math.comb(e,a+d) if a+d<=e else 0 for d in (0,1)]
                    options.append({'extra_kernel_mask':sub,'rightmost_kernel_by_gap':last,'eligible_image_mask':mask(eligible),
                        'kernel_extra_count':a,'eligible_image_count':e,'branch_binomial_counts':branches})
                    branch_counts = [branch_counts[d]+branches[d] for d in (0,1)]
                option_total += len(options)
                descriptions,actual_branches = [],[0,0]
                for source in incoming[i]:
                    sx,sy = supports(states[source])
                    sa = sorted(set(sy)|{n})
                    extra_k,extra_v = sorted(set(sx)-set(z)),sorted(set(sa)-set(w))
                    delta = len(sa)-len(sx)
                    need(delta in (0,1) and sy==(sa if delta==0 else sa[:-1]), 'every known rank branch')
                    need(set(sx)==set(z)|set(extra_k) and set(sa)==set(w)|set(extra_v) and
                         set(extra_k)|set(extra_v)<=set(free) and not set(extra_k)&set(extra_v), 'all forced/free/forbidden sites')
                    for gap in gaps:
                        a = [j for j in extra_k if j in gap['sites']]
                        b = [j for j in extra_v if j in gap['sites']]
                        need(not a or not b or max(a)<min(b), 'all extra kernel sites precede all image sites')
                    descriptions.append({'source_histogram':list(histograms[source]),'source_kernel_mask':mask(sx),'source_image_mask':mask(sy),
                        'completed_image_mask':mask(sa),'extra_kernel_mask':mask(extra_k),'extra_image_mask':mask(extra_v),'balance':delta,'source_id':source})
                    actual_branches[delta] += 1
                need(actual_branches==branch_counts, 'global binomial branch counts match whole incoming census')
                for option in options:
                    actual = [sum(r['balance']==d and r['extra_kernel_mask']==option['extra_kernel_mask'] for r in descriptions) for d in (0,1)]
                    need(actual==option['branch_binomial_counts'], 'every kernel option, including zero branches')
                atlas = {'gaps':gaps,'free_mask':mask(free),'kernel_options':options,'branch_counts':branch_counts,
                         'count':sum(branch_counts),'descriptions':descriptions}
                factors,product = [coeffs(len(gap['sites'])) for gap in gaps],{0:1}
                for factor in factors:
                    combined = {}
                    for a,ca in product.items():
                        for b,cb in factor.items():
                            combined[a+b] = combined.get(a+b,0)+ca*cb
                    product = combined
                pair = [product.get(0,0),product.get(1,0)]
                need(pair==actual_branches, 'independent full Laurent coefficients and branch census')
                laurent = {'gap_factors':[terms(f) for f in factors],'product':terms(product),'branch_counts':pair,'count':sum(pair)}
            wanted = {'id':i,'histogram':list(histograms[i]),'path_word':'|'.join('*'*h for h in histograms[i]),
                'whole_values':list(state),'kernel_mask':mask(w),'image_mask':mask(z),'completed_image_mask':mask(completed),
                'literal_block_cells':cells[i],'successor_id':arrows[i],'predecessor_ids':incoming[i],
                'fixed':arrows[i]==i,'recurrent':arrows[i]==i,'first_fixed_epoch':times[i],'terminal_id':terminals[i],
                'predicted_terminal_id':predicted_terminal,'predicted_time':predicted_time,'image_criterion':image_boundary is not None,
                'boundary_lifetimes':image_boundary,'survival_certificate':survival,'kernel_first_atlas':atlas,
                'laurent_certificate':laurent,'fibre_count':len(incoming[i])}
            need(type(saved.get('records')) is list and len(saved['records'])==count, 'all state/target rows')
            same(saved['records'][i],wanted,('entire state, nested atlas and graph record',n,i))
            records.append(wanted)
        expected_height = 0 if n==1 else (n+1)//2
        if n==1:
            wx,wy = [1],[1]
        elif n%2:
            wx,wy = list(range(2,n,2))+[n],list(range(1,n-1,2))+[n]
        else:
            wx,wy = list(range(2,n+1,2)),list(range(1,n,2))
        witness = ids[reconstruct(wx,wy,n)]
        need(height==expected_height==times[witness], 'sharp full height and exact parity witness')
        need(n==1 or (states[witness][0]==1 and states[arrows[witness]][0]==2), 'genuine initial normalization')
        counters = dict(zip(CATEGORIES,[1+2*count,count,2*count,len(tables)+count,1+count,count+len(image),
            survival_total,count+len(image),3*count,len(image)+option_total,len(image)+1,1+int(n>1)]))
        wanted = {'n':n,'state_count':count,'records':records,'successor_table':arrows,'composition_tables':tables,
            'first_fixed_epochs':times,'terminal_table':terminals,'fixed_ids':fixed,'recurrent_ids':fixed,
            'image_ids':image,'zero_fibre_ids':zero,'height':height,'height_formula':expected_height,'sharp_witness_id':witness,
            'inverse_mass':sum(map(len,incoming)),'kernel_first_mass':sum(0 if r['kernel_first_atlas'] is None else r['kernel_first_atlas']['count'] for r in records),
            'check_counts':counters,'check_total':sum(counters.values())}
        need(wanted['inverse_mass']==wanted['kernel_first_mass']==count, 'entire all-target mass')
        same(saved,wanted,('whole carrier including every table and count',n))
        rebuilt.append(wanted)
        summaries.append({'n':n,'states':count,'image_targets':len(image),'zero_targets':len(zero),'height':height,'saved_B_checks':wanted['check_total']})
    attacks = [
        {'name':'right_factor_first_and_initial_time','n':3,'source_histogram':[2,0,1],'forward_histogram':[0,1,2],'reversed_product_histogram':[0,0,3],'full_time':2},
        {'name':'extensive_top_fixing_is_not_image_iff','n':4,'target_histogram':[0,1,1,2],'fibre_count':0},
        {'name':'constant_three_rank_branches','n':3,'target_histogram':[0,0,3],
         'predecessor_histograms':[[0,0,3],[0,1,2],[0,3,0],[3,0,0]],'branch_counts':[2,2]}]
    counters = {k:sum(c['check_counts'][k] for c in rebuilt) for k in CATEGORIES}
    wanted = {'schema':'p211-b-complete-path-certificate-v1','role':'P211_REVIEW_B','parameters':EXPECTED_PARAMETERS,
        'carrier_count':7,'carriers':rebuilt,'total_states':2353,'total_targets':2353,'total_edges':2353,
        'check_counts':counters,'carrier_check_total':sum(counters.values()),'hand_attack_checks':3,
        'hand_boundary_attacks':attacks,'check_total':sum(counters.values())+3,'status':'FINITE_COMPLETE_PATH_CHECKS_PASS',
        'scope':'original n=1..7 counterexample pressure; not all-n proof or manuscript acceptance'}
    same(out,wanted,'entire top-level exact typed output')
    for p,body in READS.items():
        need(Path(p).read_bytes()==body, ('entire consumed byte input unchanged',p))
    return {'status':'PASS_FULL_SAVED_B_OUTPUT_SEMANTICS','root_checks':CHECKS,'carriers':summaries,
        'saved_B_check_total':wanted['check_total'],'binding':{'path':binding_path,'bytes':len(binding_raw),'sha256':binding_sha},
        'saved_stdout':{'path':stdout_path,'bytes':len(data),'sha256':stdout_sha},
        'receiver_source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scientific_producer_invocations':0,
        'scope':'Every saved field reconstructed; no submitted science import/AST/producer, new theorem, manuscript PASS or canonical adoption.'}

if __name__=='__main__':
    need(len(sys.argv)==5,'EXACT_BINDING_PATH BINDING_SHA256 EXACT_SAVED_STDOUT STDOUT_SHA256')
    print(compact(receive(*sys.argv[1:])))
