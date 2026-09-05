#!/usr/bin/env python3
"""P200 Review B: column incidences, cross-column events and SCC distances.

Written without reading author or Review-A verifier source. Standard library.
No row bit masks, packed matrix scalar, Kahn peeling or path-tail recursion.
"""
from collections import Counter, deque
from itertools import combinations, product

ASSERTIONS = 0
STATES = 0


def check(value, expected, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if value != expected:
        raise AssertionError((label,value,expected))


def subsets(n):
    return tuple(frozenset(c) for k in range(n+1)
                 for c in combinations(range(n),k))


def event(columns):
    """Each column pair contributes its first crossing row pair."""
    best = None
    for a,b in combinations(range(len(columns)),2):
        left = columns[a]-columns[b]
        right = columns[b]-columns[a]
        if not left or not right:
            continue
        i = min(min(left),min(right))
        k = min(right if i in left else left)
        q = (i,k,a,b)
        if best is None or q < best:
            best = q
    return best


def all_events(columns):
    result = set()
    for a,b in combinations(range(len(columns)),2):
        for u in columns[a]-columns[b]:
            for v in columns[b]-columns[a]:
                i,k = sorted((u,v))
                result.add((i,k,a,b))
    return result


def flip(columns,q):
    if q is None:
        return columns
    i,k,a,b = q
    pair = frozenset((i,k))
    return tuple(c^pair if j in (a,b) else c for j,c in enumerate(columns))


def comparable(columns,i,h,toggled=()):
    directions = {(int(i in c)^int(j in toggled))-int(h in c)
                  for j,c in enumerate(columns)}
    return not (-1 in directions and 1 in directions)


def sign_word(columns,i,k):
    return tuple((j,1 if i in c else -1) for j,c in enumerate(columns)
                 if (i in c) != (k in c))


def target_sources(columns,r):
    """A scan of pair-sign words and ternary comparison directions only.

    Does not call event() on any proposed source, nor enumerate rectangles
    of proposed sources. Constructs precisely the theorem's target atlas.
    """
    pivot = next((i for i in range(r)
                  if any(not comparable(columns,i,k) for k in range(i+1,r))),None)
    if pivot is None:
        return {columns}
    answers = set()
    for k in range(pivot+1,r):
        word = sign_word(columns,pivot,k)
        if not word or len({t for j,t in word}) < 2:
            continue
        j,first = word[0]
        for ell,kind in word[1:]:
            if kind == first:
                break
            if all(comparable(columns,pivot,h,(j,ell)) for h in range(pivot+1,k)):
                source = flip(columns,(pivot,k,j,ell))
                check(source not in answers,True,"inverse has no repeated source")
                answers.add(source)
    return answers


def recurrent_certificate(columns,q):
    if q is None:
        return True
    i,k,a,b = q
    word = sign_word(columns,i,k)
    return word[0][1] != word[1][1] and all(
        comparable(columns,i,h,(word[0][0],word[1][0])) for h in range(i+1,k))


def scc_graph(nxt,back):
    """Two-pass directed SCC, followed by multi-source reverse BFS."""
    n = len(nxt)
    visited = bytearray(n)
    finishing = []
    for start in range(n):
        if visited[start]:
            continue
        stack = [(start,False)]
        while stack:
            v,done = stack.pop()
            if done:
                finishing.append(v)
                continue
            if visited[v]:
                continue
            visited[v] = 1
            stack.append((v,True))
            if not visited[nxt[v]]:
                stack.append((nxt[v],False))
    component = [-1]*n
    groups = []
    for start in reversed(finishing):
        if component[start] >= 0:
            continue
        label = len(groups)
        group = []
        stack = [start]
        component[start] = label
        while stack:
            v = stack.pop()
            group.append(v)
            for u in back[v]:
                if component[u] < 0:
                    component[u] = label
                    stack.append(u)
        groups.append(group)
    cycles = Counter()
    distance = [-1]*n
    queue = deque()
    for group in groups:
        if len(group)>1 or nxt[group[0]] == group[0]:
            cycles[len(group)] += 1
            for v in group:
                distance[v] = 0
                queue.append(v)
    while queue:
        v = queue.popleft()
        for u in back[v]:
            if distance[u] < 0:
                distance[u] = distance[v]+1
                queue.append(u)
    check(min(distance)>=0,True,"SCC reverse BFS covers carrier")
    return distance,cycles


def from_rows(rows,s):
    return tuple(frozenset(i for i,p in enumerate(rows) if j in p) for j in range(s))


def complement(columns,r):
    full = frozenset(range(r))
    return tuple(full-c for c in columns)


def stirling(n,k):
    row = [1]+[0]*k
    for _ in range(n):
        row = [0]+[j*row[j]+row[j-1] for j in range(1,k+1)]
    return row[k]


def lonesum(r,s):
    fac = 1
    result = 0
    for k in range(min(r,s)+1):
        if k:
            fac *= k
        result += fac*fac*stirling(r+1,k+1)*stirling(s+1,k+1)
    return result


def box(r,s):
    global STATES
    states = list(product(subsets(r),repeat=s))
    STATES += len(states)
    index = {x:i for i,x in enumerate(states)}
    selectors = [event(x) for x in states]
    nxt = [index[flip(x,q)] for x,q in zip(states,selectors)]
    back = [[] for _ in states]
    for i,j in enumerate(nxt):
        back[j].append(i)
    depths,cycles = scc_graph(nxt,back)
    check(set(cycles)<= {1,2},True,"entire temporal cycle support")
    margins = lambda x:(tuple(sum(i in c for c in x) for i in range(r)),
                       tuple(map(len,x)))
    for idx,x in enumerate(states):
        q = selectors[idx]
        y = states[nxt[idx]]
        qnext = selectors[nxt[idx]]
        check(margins(x),margins(y),"both labelled margins")
        check(recurrent_certificate(x,q),depths[idx] == 0,"recurrent iff")
        check(q is None,all(comparable(x,i,k) for i,k in combinations(range(r),2)),
              "fixed exactly containment chain")
        check(depths[idx]<=2*r-3,True,"width-uniform tail upper bound")
        check({index[z] for z in target_sources(x,r)},set(back[idx]),
              "entire inverse source set including absent targets")
        check(nxt[index[complement(x,r)]],index[complement(y,r)],"complement conjugacy")
        if len(states)<=4096:
            events = all_events(x)
            check(min(events) if events else None,q,"all column-crossing events")
        if q is not None:
            check(qnext is not None,True,"nonfixed cannot enter fixed")
            check(qnext[0],q[0],"first pivot invariant")
            check(qnext[1]<=q[1],True,"partner never increases")
            check(qnext<=q,True,"selector never increases")
            check(qnext == q,depths[idx] == 0,"equal selector exactly recurrence")
            # Bounded certificate follows from SCC distance, not a tail finder.
            u = idx
            partners = []
            for _ in range(depths[idx]+1):
                partners.append(selectors[u][1])
                u = nxt[u]
            counts = Counter(partners)
            check(max(counts.values())<=2,True,"two visits including first core state")
            check(depths[idx]<=2*len(counts)-1,True,"pointwise distinct-partner tail")
        else:
            check(back[idx],[idx],"fixed unique self predecessor")
    maximum = max(map(len,back))
    check(maximum,(r-1)*(s-1),"sharp inverse maximum")
    maximal = {states[i] for i,v in enumerate(back) if len(v) == maximum}
    if (r,s) == (2,2):
        expected = set(states)
    else:
        base = from_rows([frozenset((0,))]+[frozenset(range(1,s))]*(r-1),s)
        expected = {base,complement(base,r)}
    check(maximal,expected,"complete maximum equality class")
    check(cycles[1],lonesum(r,s),"classical fixed census control")
    if s>=r+1:
        check(max(depths),2*r-3,"wide-box sharpness")
    result = (len(states),sum(bool(v) for v in back),cycles[1],
              max(depths),maximum,len(maximal),tuple(sorted(cycles.items())))
    print(f"BOX {r}x{s} states,image,fixed,tail,maxfibre,max_targets,cycles={result}",flush=True)
    return result


def witnesses():
    count = 0
    for r in range(2,25):
        for s in (r+1,r+7):
            rows = [frozenset((r,))]+[
                frozenset((0,k))|frozenset(range(k+2,r+1)) for k in range(1,r)]
            x = from_rows(rows,s)
            itinerary = [(0,k,0,b) for k in range(r-1,0,-1) for b in (k+1,k)]
            for t,q in enumerate(itinerary):
                check(event(x),q,"wide witness exact whole itinerary")
                check(recurrent_certificate(x,q),t == len(itinerary)-1,
                      "wide witness first core entrance")
                x = flip(x,q)
            check(len(itinerary)-1,2*r-3,"wide witness attained exact tail")
            check(event(x),itinerary[-1],"wide witness terminal same selector")
            count += 1
    print(f"WIDE_WITNESSES={count} r=2..24 widths=r+1,r+7",flush=True)


def main():
    print("P200_REVIEW_B / COLUMN_INCIDENCE_CROSSINGS / SCC_REVERSE_BFS / HOLD_EXTERNAL")
    boxes = [(2,s) for s in range(2,9)]+[(3,s) for s in range(2,6)]+[
        (4,s) for s in range(2,5)]+[(5,2),(5,3),(6,2),(7,2),(8,2)]
    results = {shape:box(*shape) for shape in boxes}
    check(results[3,4][1],3292,"printed nonsquare image count")
    check(results[4,3][1],3290,"transposed image count differs")
    witnesses()
    print(f"BOXES={len(boxes)} FULL_STATES={STATES} ASSERTIONS={ASSERTIONS}")
    print("PASS / INDEPENDENT_REVIEW_B_CONTROL / NO_CROSS_MODEL_CLAIM / HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
