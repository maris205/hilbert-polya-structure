#!/usr/bin/env python3
"""Independent CCI candidate gate: no author or repository imports/data reads.

Representations: edge-list literal update; all-pairs Floyd closure for arrival;
functional-graph leaf peeling for exact h/period; held-set (dual) decoder;
bitset independent complements for the cover extremum. All stdlib.
Fixed boxes: all graphs n<=5,q=3; n<=4,q=4; n<=3,q=5,7. Static all n<=6.
Extra sharp paths n=2..14,q=3..11; decoder ablations and source-rule controls.
"""
from collections import Counter, deque
from itertools import combinations, product
import hashlib
import json

CHECKS = Counter()
DIGEST = hashlib.sha256()


def check(label, condition):
    CHECKS[label] += 1
    assert condition, (label,CHECKS[label])


def digest(record):
    DIGEST.update(json.dumps(record,separators=(",",":"),sort_keys=True).encode())
    DIGEST.update(b"\n")


def graphs(n):
    possible = tuple(combinations(range(n),2))
    for mask in range(1 << len(possible)):
        yield mask,tuple(e for i,e in enumerate(possible) if (mask >> i)&1)


def literal(x, edges, q):
    active = 0
    for a,b in edges:
        if x[a] == x[b]:
            active |= (1 << a) | (1 << b)
    return tuple((c+((active >> v)&1))%q for v,c in enumerate(x)),active


def predicted_distances(x,edges,q):
    n = len(x)
    infinity = q*(n+1)
    lengths = [[0 if i == j else infinity for j in range(n)] for i in range(n)]
    seeds = set()
    for a,b in edges:
        lengths[a][b] = (x[b]-x[a])%q
        lengths[b][a] = (x[a]-x[b])%q
        if x[a] == x[b]:
            seeds.update((a,b))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                lengths[i][j] = min(lengths[i][j],lengths[i][k]+lengths[k][j])
    return tuple(min((lengths[s][v] for s in seeds),default=infinity)
                 for v in range(n)),infinity


def orbit_coordinates(arrows):
    incoming = [0]*len(arrows)
    for j in arrows:
        incoming[j] += 1
    queue = deque(i for i,k in enumerate(incoming) if not k)
    peeled = []
    while queue:
        i = queue.popleft()
        peeled.append(i)
        incoming[arrows[i]] -= 1
        if not incoming[arrows[i]]:
            queue.append(arrows[i])
    height, period = [0]*len(arrows),[0]*len(arrows)
    for i,k in enumerate(incoming):
        if not k or period[i]:
            continue
        cycle,j = [],i
        while not cycle or j != i:
            cycle.append(j)
            j = arrows[j]
        for j in cycle:
            period[j] = len(cycle)
    for i in reversed(peeled):
        height[i] = height[arrows[i]]+1
        period[i] = period[arrows[i]]
    return height,period


def encode(x,q):
    value = 0
    for a in x:
        value = value*q+a
    return value


def held_decoder(y,edges,q):
    """I=held set: independent in H, outside vertices have outside H-neighbor,
    and I is successor-closed in D. This is the dual of author's active mask.
    """
    n = len(y)
    full = (1 << n)-1
    same_neighbors = [0]*n
    successors = [0]*n
    for a,b in edges:
        if y[a] == y[b]:
            same_neighbors[a] |= 1 << b
            same_neighbors[b] |= 1 << a
        if (y[b]-y[a])%q == 1:
            successors[a] |= 1 << b
        if (y[a]-y[b])%q == 1:
            successors[b] |= 1 << a
    sources = []
    for held in range(1 << n):
        active = full^held
        okay = True
        for v in range(n):
            if (held >> v)&1:
                if same_neighbors[v] & held or successors[v] & active:
                    okay = False
                    break
            elif not same_neighbors[v] & active:
                okay = False
                break
        if okay:
            source = tuple((a-((active >> v)&1))%q for v,a in enumerate(y))
            sources.append(encode(source,q))
    return sorted(sources)


def is_extreme_graph(n,edges):
    if n <= 2:
        return True
    if n == 3:
        return len(edges) == 3
    degrees = Counter(v for e in edges for v in e)
    return len(edges) == n-1 and any(degrees[v] == n-1 for v in range(n))


def maximum_fibre(n):
    return 1 if n <= 2 else (4 if n == 3 else 2**(n-1)-1)


def full_dynamics(n,q):
    states = list(product(range(q),repeat=n))
    bound = (q-1)*max(0,n-2)
    max_height,max_fibre,extremizers,total_sources = 0,0,0,0
    all_periods = set()
    for graph_mask,edges in graphs(n):
        arrows, active_sets = [],[]
        inverse = [[] for _ in states]
        for i,x in enumerate(states):
            y,active = literal(x,edges,q)
            arrow = encode(y,q)
            arrows.append(arrow)
            active_sets.append(active)
            inverse[arrow].append(i)
        heights,periods = orbit_coordinates(arrows)
        for i,x in enumerate(states):
            total_sources += 1
            distances,infinity = predicted_distances(x,edges,q)
            entrance = max((d for d in distances if d < infinity),default=0)
            check("height_from_floyd",heights[i] == entrance)
            check("uniform_height",heights[i] <= bound)
            expected_period = q if active_sets[i] else 1
            check("exact_period",periods[i] == expected_period)
            current = i
            first = [infinity]*n
            for t in range(bound+q+1):
                formula = tuple((a+max(0,t-d))%q if d < infinity else a
                                for a,d in zip(x,distances))
                check("all_time_coordinate_formula",states[current] == formula)
                current_active = active_sets[current]
                for v in range(n):
                    if (current_active >> v)&1 and first[v] == infinity:
                        first[v] = t
                check("permanent_activation",current_active & ~active_sets[arrows[current]] == 0)
                current = arrows[current]
            check("first_conflict_from_floyd",tuple(first) == distances)
            check("held_set_exact_inverse",held_decoder(x,edges,q) == inverse[i])
            fibre = len(inverse[i])
            check("uniform_fibre",fibre <= maximum_fibre(n))
            if n >= 3:
                predicted_extreme = is_extreme_graph(n,edges) and len(set(x)) == 1
                check("all_equality_targets",(fibre == maximum_fibre(n)) == predicted_extreme)
            max_height = max(max_height,heights[i])
            max_fibre = max(max_fibre,fibre)
            extremizers += (fibre == maximum_fibre(n))
            all_periods.add(periods[i])
            digest([n,q,graph_mask,i,distances,heights[i],periods[i],inverse[i]])
        if n >= 4:
            check("sharp_graph_targets",sum(len(a) == maximum_fibre(n) for a in inverse)
                  == (q if is_extreme_graph(n,edges) else 0))
    check("global_height_attainment",max_height == bound)
    check("global_fibre_attainment",max_fibre == maximum_fibre(n))
    return {"n":n,"q":q,"sources":total_sources,"max_height":max_height,
            "max_fibre":max_fibre,"extremal_graph_targets":extremizers,
            "periods":sorted(all_periods)}


def total_cover_count(n,edges):
    full = (1 << n)-1
    neighbors = [0]*n
    for a,b in edges:
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a
    count = 0
    for held in range(1 << n):
        active = full^held
        if all(not (neighbors[v] & held) if ((held >> v)&1)
               else bool(neighbors[v] & active) for v in range(n)):
            count += 1
    return count


def static_checks():
    results = []
    for n in range(7):
        maximum,extreme,total = 0,0,0
        for mask,edges in graphs(n):
            value = total_cover_count(n,edges)
            check("static_cover_upper",value <= maximum_fibre(n))
            check("static_cover_equality",(value == maximum_fibre(n)) == is_extreme_graph(n,edges))
            maximum = max(maximum,value)
            extreme += (value == maximum_fibre(n))
            total += 1
            digest(["static",n,mask,value])
        results.append({"n":n,"graphs":total,"maximum":maximum,"extremizers":extreme})
    return results


def extra_controls():
    sharp = 0
    for n in range(2,15):
        edges = tuple((v,v+1) for v in range(n-1))
        for q in range(3,12):
            x = (0,0)+tuple((-j)%q for j in range(1,n-1))
            distances,_ = predicted_distances(x,edges,q)
            check("sharp_path_arrival",distances == (0,0)+tuple((q-1)*j for j in range(1,n-1)))
            current = x
            for t in range((q-1)*(n-2)+q+1):
                check("sharp_path_literal",current == tuple((a+max(0,t-d))%q for a,d in zip(x,distances)))
                current,_ = literal(current,edges,q)
            sharp += 1
    # Each omitted decoder constraint admits a concrete false source.
    ablations = [
        ("cover",(0,0),((0,1),),0),
        ("nonisolated",(0,1),((0,1),),1),
        ("predecessor",(0,1,1),((0,1),(1,2)),6),
    ]
    for name,y,edges,active in ablations:
        x = tuple((a-((active >> v)&1))%3 for v,a in enumerate(y))
        check("ablation_"+name,literal(x,edges,3)[0] != y)
        check("ablation_excluded_"+name,encode(x,3) not in held_decoder(y,edges,3))
    # A monochromatic edge: CCI rotates, CCA holds; CCI has proper fixed states.
    check("CCA_literal_separator",literal((0,0),((0,1),),3)[0] == (1,1))
    check("proper_coloring_holds",literal((0,1),((0,1),),3)[0] == (0,1))
    check("recurrent_not_constant",literal((0,0,1,1),((0,1),(1,2),(2,3)),3)[0] == (1,1,2,2))
    # Waiting depends on oriented residues, not ordinary graph distance.
    check("weighted_not_unweighted",predicted_distances((0,0,2),((0,1),(1,2)),3)[0] == (0,0,2))
    check("orientation_not_reversed",predicted_distances((0,0,1),((0,1),(1,2)),3)[0] == (0,0,1))
    return sharp


def main():
    dynamics = []
    for q,top in ((3,5),(4,4),(5,3),(7,3)):
        for n in range(top+1):
            dynamics.append(full_dynamics(n,q))
    statics = static_checks()
    sharp = extra_controls()
    print(json.dumps({"status":"PASS_INDEPENDENT_BOUNDED_CCI_GATE",
        "external_status":"HOLD_EXTERNAL","dynamics":dynamics,"statics":statics,
        "sharp_paths":sharp,"checks":dict(sorted(CHECKS.items())),
        "assertions":sum(CHECKS.values()),"enumeration_sha256":DIGEST.hexdigest()},
        sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
