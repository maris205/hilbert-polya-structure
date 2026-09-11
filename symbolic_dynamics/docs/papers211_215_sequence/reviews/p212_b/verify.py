"""P212 nonauthor B. SOURCE ONLY until root accepts and binds invocation.

No file inputs. Fixed full carriers n=1..4; one complete JSON stdout.
Inverse integer-digit graph + DSU, Pruefer tree/two-cotree catalogue,
degree-two edge contraction, static destination assignments, denominator
recurrences. No author/A import, canonical input, or inherited pilot.
"""
import itertools
import sys

ROWS = ('figure_eight_double_loop', 'figure_eight_short_nontrivial',
        'figure_eight_long', 'barbell_short', 'barbell_long',
        'theta_triple_direct', 'theta_other')
FIRST = (1, 2, 3, 2, 4, 2, 3)
FAMILIES = ('figure_eight', 'barbell', 'theta')
CHECKS = []


def wire(value):
    """Canonical compact JSON for the finite supported value-tree domain."""
    kind = type(value)
    if kind is bool:
        return 'true' if value else 'false'
    if kind is int:
        return str(value)
    if kind is str:
        escaped = {'"': '\\"', '\\': '\\\\', '\b': '\\b', '\t': '\\t',
                   '\n': '\\n', '\f': '\\f', '\r': '\\r'}
        parts = ['"']
        for char in value:
            code = ord(char)
            if code > 127:
                raise ValueError('wire requires ASCII strings')
            if char in escaped:
                parts.append(escaped[char])
            elif code < 32 or code == 127:
                parts.append('\\u%04x' % code)
            else:
                parts.append(char)
        parts.append('"')
        return ''.join(parts)
    if kind is list or kind is tuple:
        return '[' + ','.join(wire(item) for item in value) + ']'
    if kind is dict:
        if any(type(key) is not str for key in value):
            raise TypeError('wire requires string dictionary keys')
        return '{' + ','.join(wire(key) + ':' + wire(value[key])
                              for key in sorted(value)) + '}'
    raise TypeError('unsupported wire value type')


def factorial(value):
    """Integer factorial on exact nonnegative integers."""
    if type(value) is not int or value < 0:
        raise ValueError('factorial requires a nonnegative integer')
    result = 1
    for factor in range(2, value + 1):
        result *= factor
    return result


def check(name, scope, observed, expected):
    ok = wire(observed) == wire(expected)
    CHECKS.append(dict(id=len(CHECKS), name=name, scope=scope,
                       observed=observed, expected=expected, passed=ok))


def digits(code, n, length):
    out = []
    for _ in range(length):
        code, digit = divmod(code, n)
        out.append(digit)
    return tuple(out)


def encode(state, n):
    return sum(x * n**i for i, x in enumerate(state))


def backwards(code, n):
    # (a,b,g) -> (g(a),a,g[a:=b]); arithmetic replacement, no slot swaps.
    a, b = code % n, (code // n) % n
    pointer = (code // n**(a + 2)) % n
    return code + (pointer-a) + (a-b)*n + (b-pointer)*n**(a+2)


def edge(a, b):
    return (min(a, b), max(a, b))


def edges(state):
    u, v, *f = state
    return tuple(sorted([edge(u, v)] + [edge(a, b) for a, b in enumerate(f)]))


def degree(vertices, es):
    return {v: sum((a == v) + (b == v) for a, b in es) for v in vertices}


def invariant(state):
    u, v, *f = state
    es = edges(state)
    active = {u}
    while True:
        more = active | {b for a, b in es if a in active} | {a for a, b in es if b in active}
        if more == active:
            break
        active = more
    core = set(active)
    layers = []
    while True:
        retained = tuple((a, b) for a, b in es if a in core and b in core)
        d = degree(core, retained)
        remove = {a for a in core if d[a] < 2}
        if not remove:
            break
        layers.append(sorted(remove))
        core -= remove
    vertices = tuple(sorted(core))
    complement = tuple((a, b) for a, b in enumerate(f) if a not in core)
    return (vertices, retained, complement), dict(edges=es, active=sorted(active),
            pruning_layers=layers, core=vertices, core_edges=retained,
            complement=complement)


def describe(vertices, es):
    # Contract degree-two vertices globally; retain actual path vertex strings.
    d = degree(vertices, es)
    branches = sorted(v for v in vertices if d[v] > 2)
    paths = [tuple(e) for e in es]
    for v in sorted(set(vertices) - set(branches)):
        incident = [i for i, p in enumerate(paths) if p[0] == v or p[-1] == v]
        if len(incident) != 2:
            raise ValueError('degree-two contraction incidence')
        i, j = incident
        p, q = paths[i], paths[j]
        if p[-1] != v:
            p = p[::-1]
        if q[0] != v:
            q = q[::-1]
        paths = [p0 for k, p0 in enumerate(paths) if k not in (i, j)] + [p + q[1:]]
    paths = [min(p, p[::-1]) for p in paths]
    if len(branches) == 1:
        family = 'figure_eight'
        paths.sort()
        a, b = [len(p)-1 for p in paths]
        row = ROWS[0] if a == b == 1 else ROWS[1] if max(a,b) <= 2 else ROWS[2]
        period = 1 if row == ROWS[0] else (a+b)*(2 if max(a,b)>=3 else 1)
        classes = 2 if min(a,b)>=3 else 1
    elif len(branches) == 2 and any(p[0] == p[-1] for p in paths):
        family = 'barbell'
        paths = (sorted(p for p in paths if p[0] == p[-1]) +
                 sorted(p for p in paths if p[0] != p[-1]))
        a,b,c = [len(p)-1 for p in paths]
        row = ROWS[3] if max(a,b)<=2 else ROWS[4]
        period = (a+b+2*c)*(2 if max(a,b)>=3 else 1)
        classes = 2 if min(a,b)>=3 else 1
    elif len(branches) == 2:
        family = 'theta'
        paths.sort()
        lengths = [len(p)-1 for p in paths]
        row = ROWS[5] if lengths == [1,1,1] else ROWS[6]
        period = 2 if row == ROWS[5] else 2*sum(lengths)
        classes = 1 if lengths.count(1)>=2 else 2
    else:
        raise ValueError('bicyclic branch signature')
    return dict(family=family,row=row,branches=branches,paths=paths,
                lengths=[len(p)-1 for p in paths],period=period,classes=classes)


def catalogue(s):
    # Every connected s-vertex/s+1-edge multigraph contains a simple spanning
    # tree and exactly two leftover multiset edges (loops allowed).
    vs = tuple(range(s))
    pairs = tuple((a,b) for a in vs for b in vs if a<=b)
    found = set()
    words = [()] if s<=2 else itertools.product(vs, repeat=s-2)
    for word in words:
        deg = [1 + word.count(v) for v in vs]
        tree = []
        for v in word:
            leaf = next(a for a in vs if deg[a] == 1)
            tree.append(edge(leaf,v))
            deg[leaf] -= 1
            deg[v] -= 1
        if s>=2:
            tree.append(tuple(a for a in vs if deg[a] == 1))
        for e1, e2 in itertools.combinations_with_replacement(pairs,2):
            es = tuple(sorted(tree + [e1,e2]))
            if min(degree(vs,es).values())>=2:
                found.add(es)
    return sorted(found)


def anchor(state, desc):
    u,v,*f = state
    if u != desc['branches'][0]:
        return None
    paths = desc['paths']
    if desc['family'] == 'theta':
        tokens = [tuple(p[1:-1]) for p in paths]
        remain = list(tokens)
        role = []
        for target in (v,f[u]):
            eligible = [t for t in remain if (t[0] if t else desc['branches'][1]) == target]
            if not eligible:
                return None
            t = min(eligible)
            role.append(t)
            remain.remove(t)
        if len(remain) != 1:
            raise ValueError('theta role multiplicity')
        raw = tuple(role + remain)
        cls = min(raw[i:]+raw[:i] for i in range(3))
    else:
        if desc['family'] == 'figure_eight':
            if v not in (paths[0][1], paths[0][-2]):
                return None
            targets = (v,f[u])
        else:
            if v != paths[2][1]:
                return None
            targets = (f[desc['branches'][0]],f[desc['branches'][1]])
        bits = []
        for p,t in zip(paths[:2],targets):
            if t not in (p[1],p[-2]):
                return None
            bits.append(0 if len(p)<=3 or t == p[1] else 1)
        raw = tuple(bits)
        reverse = tuple(1-b if len(p)>3 else 0 for p,b in zip(paths,bits))
        cls = min(raw,reverse)
    return raw,cls


def static_core_anchors(s, catalogues):
    # Complete static destination-map enumeration, not orbit representatives,
    # oriented-chain constructor, last-arrival reconstruction or visit words.
    result = {es: [] for es in catalogues}
    descriptions = {es:describe(tuple(range(s)),es) for es in catalogues}
    for state in itertools.product(range(s),repeat=s+2):
        es = edges(state)
        if es in result:
            value = anchor(state,descriptions[es])
            if value is not None:
                result[es].append((state,value))
    return result


def series():
    # All coefficients scaled by 24. Denominator recurrences, no Fraction
    # algebra and no enumeration of core path-length parameters.
    pieces = {family:{} for family in FAMILIES}
    def solve(family,numerator,denominator):
        coeff = {}
        for s in range(5):
            row = {p:c for (size,p),c in numerator.items() if size==s}
            for (ds,dp),v in denominator.items():
                if ds and s>=ds:
                    for p,c in coeff[s-ds].items():
                        row[p+dp] = row.get(p+dp,0)-v*c
            coeff[s] = {p:c for p,c in row.items() if c}
        for s,row in coeff.items():
            for p,c in row.items():
                pieces[family][s,p] = pieces[family].get((s,p),0)+c
    # D = (2x^2-x^4)/(1-x)^2. Expanded numerator only, s<=4.
    solve('figure_eight',{(1,1):24,(2,3):24,(3,4):12},{(0,0):1})
    solve('figure_eight',{(3,8):12,(5,12):-6},{(0,0):1,(1,2):-2,(2,4):1})
    solve('barbell',{(2,4):12,(3,5):24,(4,6):12},{(0,0):1,(1,2):-1})
    solve('barbell',{(4,12):12,(6,16):-6},
          {(0,0):1,(1,2):-2,(2,4):1,(1,4):-1,(2,6):2,(3,8):-1})
    solve('theta',{(2,2):12},{(0,0):1})
    # Q+Q^2+Q^3/3 = (x-x^2+x^3/3)/(1-x)^3.
    solve('theta',{(3,8):12,(4,10):-12,(5,12):4},
          {(0,0):1,(1,2):-3,(2,4):3,(3,6):-1})
    return pieces


def poly(mapping):
    return [[k,v] for k,v in sorted(mapping.items()) if v]


def carrier(n, cats, anchors, pieces):
    count = n**(n+2)
    states = [digits(i,n,n+2) for i in range(count)]
    inv = [backwards(i,n) for i in range(count)]
    forward = [-1]*count
    parents = list(range(count))
    def root(i):
        while parents[i] != i:
            i = parents[i]
        return i
    for i,j in enumerate(inv):
        check('inverse_range',f'{n}/{i}',0<=j<count,True)
        check('unit_preimage',f'{n}/{i}',forward[j],-1)
        forward[j] = i
        a,b = root(i),root(j)
        parents[max(a,b)] = min(a,b)
    groups = {}
    records = []
    for i,state in enumerate(states):
        key, data = invariant(state)
        groups.setdefault(key,[]).append(i)
        u,v,*f = state
        g = list(f)
        g[v] = u
        check('literal_forward',f'{n}/{i}',states[forward[i]],(v,f[v],*g))
        check('backward_invariant',f'{n}/{i}',invariant(states[inv[i]])[0],key)
        check('full_edges_invariant',f'{n}/{i}',edges(states[inv[i]]),data['edges'])
        check('registers_core',f'{n}/{i}',[u in key[0],v in key[0]],[True,True])
        check('core_internal',f'{n}/{i}',all(f[a] in key[0] for a in key[0]),True)
        check('active_excess',f'{n}/{i}',sum(a in data['active'] and b in data['active'] for a,b in data['edges']),len(data['active'])+1)
        records.append(dict(id=i,state=state,inverse=inv[i],forward=forward[i],
                            orbit=root(i),invariant=data))
    components = {}
    for i in range(count):
        components.setdefault(root(i),[]).append(i)
    orbits = []
    for oid, members in sorted(components.items()):
        order, current = [],oid
        while current not in order:
            order.append(current)
            current = inv[current]
        check('dsu_cycle',f'{n}/{oid}',[current,sorted(order)],[oid,members])
        orbits.append(dict(id=oid,inverse_time=order,period=len(order)))
    expected = {}
    for s in range(1,n+1):
        for vertices in itertools.combinations(range(n),s):
            outside = tuple(v for v in range(n) if v not in vertices)
            for es in cats[s]:
                lifted = tuple(sorted(edge(vertices[a],vertices[b]) for a,b in es))
                desc = describe(vertices,lifted)
                for destinations in itertools.product(range(n),repeat=n-s):
                    complement = tuple(zip(outside,destinations))
                    key = (vertices,lifted,complement)
                    expected[key] = (s,es,desc)
    check('complete_groups',str(n),sorted(groups),sorted(expected))
    group_records = []
    observed_poly = {}
    pure = {family:{} for family in FAMILIES}
    row_counts = {r:[0,0,0] for r in ROWS}
    for gid,key in enumerate(sorted(expected)):
        vertices,es,complement = key
        s,local_es,desc = expected[key]
        members = groups.get(key,[])
        oids = sorted({root(i) for i in members})
        periods = [len(components[oid]) for oid in oids]
        check('period_table',f'{n}/g{gid}',periods,[desc['period']]*desc['classes'])
        actual = []
        class_to_orbits = {}
        for i in members:
            value = anchor(states[i],desc)
            if value is not None:
                raw,cls = value
                actual.append((i,raw,cls))
                class_to_orbits.setdefault(cls,set()).add(root(i))
        wanted = []
        for local_state,value in anchors[s][local_es]:
            u,v,*f = local_state
            full = [0]*n
            for a,b in complement:
                full[a]=b
            for a,b in enumerate(f):
                full[vertices[a]]=vertices[b]
            state = (vertices[u],vertices[v],*full)
            # Decode after monotone relabelling: theta internal tokens contain
            # labels, while cycle bits remain invariant.
            raw,cls = anchor(state,desc)
            wanted.append((encode(state,n),raw,cls))
        check('complete_anchor_states',f'{n}/g{gid}',sorted(actual),sorted(wanted))
        check('decoration_bijection',f'{n}/g{gid}',
              sorted(sorted(ids) for ids in class_to_orbits.values()),[[i] for i in oids])
        check('decoration_cardinality',f'{n}/g{gid}',len(class_to_orbits),desc['classes'])
        for oid in oids:
            p = len(components[oid])
            observed_poly[p] = observed_poly.get(p,0)+1
            if s == n:
                pure[desc['family']][p] = pure[desc['family']].get(p,0)+1
        values = row_counts[desc['row']]
        values[0]+=1
        values[1]+=len(oids)
        values[2]+=len(members)
        group_records.append(dict(id=gid,key=key,description=desc,states=members,
            orbits=oids,actual_anchors=sorted(actual),expected_anchors=sorted(wanted),
            class_to_orbits=[(cls,sorted(ids)) for cls,ids in sorted(class_to_orbits.items())]))
    contributions = []
    expected_poly24 = {}
    for s in range(1,n+1):
        multiplier = factorial(n)//factorial(n-s)*n**(n-s)
        terms = {}
        for family in FAMILIES:
            for (size,p),c in pieces[family].items():
                if size == s:
                    terms[p] = terms.get(p,0)+c*multiplier
                    expected_poly24[p] = expected_poly24.get(p,0)+c*multiplier
        contributions.append(dict(s=s,multiplier=multiplier,terms24=poly(terms)))
    check('full_census',str(n),poly({p:24*c for p,c in observed_poly.items()}),poly(expected_poly24))
    for family in FAMILIES:
        expected_family = {p:c*factorial(n) for (s,p),c in pieces[family].items() if s==n}
        check('pure_family_series',f'{n}/{family}',poly({p:24*c for p,c in pure[family].items()}),poly(expected_family))
    period_set = [1] if n==1 else sorted(set(range(1,2*n+1)) | set(range(2*n+2,4*n-3,2)))
    check('attained_period_set',str(n),sorted(observed_poly),period_set)
    check('maximum',str(n),max(observed_poly),1 if n==1 else 4*n-4)
    check('fixed_states',str(n),observed_poly.get(1,0),n**n)
    check('state_mass',str(n),sum(p*c for p,c in observed_poly.items()),count)
    fixed = []
    iterates = list(range(count))
    for k in range(1,(1 if n==1 else 4*n-4)+1):
        iterates = [inv[i] for i in iterates]
        ids = [i for i,j in enumerate(iterates) if i==j]
        predicted24 = sum(p*c for p,c in expected_poly24.items() if k%p==0)
        check('fixed_iterate',f'{n}/{k}',24*len(ids),predicted24)
        fixed.append(dict(k=k,ids=ids,predicted24=predicted24))
    for row,first in zip(ROWS,FIRST):
        check('row_presence',f'{n}/{row}',row_counts[row][0]>0,n>=first)
    return dict(n=n,states=records,orbits=orbits,groups=group_records,
                row_counts=row_counts,period_polynomial=poly(observed_poly),
                extension_contributions=contributions,fixed_iterates=fixed)


def main():
    if len(sys.argv)!=1:
        raise ValueError('no application arguments permitted')
    cats = {s:catalogue(s) for s in range(1,5)}
    anchors = {s:static_core_anchors(s,cats[s]) for s in range(1,5)}
    pieces = series()
    carriers = [carrier(n,cats,anchors,pieces) for n in range(1,5)]
    series_records = []
    rational24 = [0]*5
    numerator24 = {1:24,2:-24,4:12,5:-2}
    for s in range(1,5):
        terms = {}
        for family in FAMILIES:
            for (size,p),c in pieces[family].items():
                if size == s:
                    terms[p] = terms.get(p,0)+c
        closed24 = 24 if s==1 else 48 if s==2 else 5*s*s+s+24
        rational24[s] = numerator24.get(s,0) + sum(
            c*rational24[s-j] for j,c in ((1,3),(2,-3),(3,1)) if s>=j)
        check('univariate_rational_identity',str(s),sum(terms.values()),rational24[s])
        check('closed_core_coefficient',str(s),sum(terms.values()),closed24)
        check('weighted_core_coefficient',str(s),sum(p*c for p,c in terms.items()),12*s*s*(s+1))
        series_records.append(dict(s=s,terms24=poly(terms),closed24=closed24))
    limits = []
    for family,first in [('figure_eight_both_long',5),('barbell_both_long',6),('theta_all_nondirect',5)]:
        witnesses=[]
        for c in carriers:
            for g in c['groups']:
                d=g['description']
                hit = ((family=='figure_eight_both_long' and d['family']=='figure_eight' and min(d['lengths'])>=3) or
                       (family=='barbell_both_long' and d['family']=='barbell' and min(d['lengths'][:2])>=3) or
                       (family=='theta_all_nondirect' and d['family']=='theta' and min(d['lengths'])>=2))
                if hit:
                    witnesses.append([c['n'],g['id']])
        check('finite_coverage_boundary',family,witnesses,[])
        limits.append(dict(family=family,first_size=first,witnesses=witnesses,status='deductive_only'))
    check('total_states','all',sum(len(c['states']) for c in carriers),4356)
    failures=[c['id'] for c in CHECKS if not c['passed']]
    names=sorted({c['name'] for c in CHECKS})
    result=dict(schema='p212-review-b-v1',role='nonauthor_process_separated_B',
        method='inverse_digits_DSU_Pruefer_cotree_contraction_static_anchors_denominator_recurrence',
        labels='zero_based_little_endian',carrier_sizes=[1,2,3,4],
        catalogues=[dict(s=s,entries=[dict(edges=es,description=describe(tuple(range(s)),es),
            static_anchors=anchors[s][es]) for es in cats[s]]) for s in range(1,5)],
        carriers=carriers,series_pieces=[dict(family=f,terms24=[[s,p,c] for (s,p),c in sorted(pieces[f].items())]) for f in FAMILIES],
        core_series=series_records,coverage_limits=limits,predicates=CHECKS,
        predicate_census=[dict(name=name,checks=sum(c['name']==name for c in CHECKS),
            failures=sum(c['name']==name and not c['passed'] for c in CHECKS)) for name in names],
        summary=dict(states=4356,orbits=[len(c['orbits']) for c in carriers],
            predicates=len(CHECKS),failure_ids=failures,passed=not failures),
        exclusions=['finite evidence is not an all-n proof','first-size 5/6/5 families are unexecuted',
                    'no external review or global novelty certificate','no build or lifecycle completion'])
    sys.stdout.write(wire(result)+'\n')
    return 1 if failures else 0


if __name__=='__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        sys.stderr.write('P212 B failure: '+str(exc)+'\n')
        sys.exit(2)
