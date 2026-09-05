#!/usr/bin/env python3
"""P199 Review B: labelled endpoint pairs, stabilized images and preimages.

No word/child-array state and no author or Review-A imports. Complete
incoming sets reconstructed by exposed-interval endpoints, not word-gap
Stirling validity search. Written before reading either earlier verifier.
"""
from collections import Counter, defaultdict
from math import factorial, prod

CHECKS = 0


def require(ok, reason):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(reason)


def insert_maximum(pairs):
    n = len(pairs)+1
    return [tuple((a+2*(a>=g), b+2*(b>=g)) for a,b in pairs)+((g,g+1),)
            for g in range(2*n-1)]


def forward(pairs):
    if not pairs:
        return pairs
    a,b = pairs[0]
    def move(x):
        after = x-int(x>a)-int(x>b)
        return after+2*(after>=a)
    return tuple((move(c),move(d)) for c,d in pairs[1:])+((a,a+1),)


def exposed(pairs):
    return sorted((a,b,j) for j,(a,b) in enumerate(pairs)
                  if not any(c<a<b<d for c,d in pairs))


def laminar_valid(pairs):
    n = len(pairs)
    if sorted(x for pair in pairs for x in pair) != list(range(2*n)):
        return False
    if any(a>=b for a,b in pairs):
        return False
    for i,(a,b) in enumerate(pairs):
        for j,(c,d) in enumerate(pairs):
            if i == j:
                continue
            if a<c<b<d or (a<c<d<b and i>=j):
                return False
    return True


def inverse(pairs):
    n = len(pairs)
    if n == 0:
        return {pairs}
    a,b = pairs[-1]
    roots = exposed(pairs)
    if not any(j == n-1 for _,_,j in roots):
        return set()
    assert b == a+1
    suffix = [(c,d) for c,d,j in roots if c>b]
    second = a+1
    stops = [second]
    for c,d in suffix:
        second += d-c+1
        stops.append(second)
    answer = set()
    for second in stops:
        def move(x):
            after = x-2*(x>b)
            after += int(after>=a)
            return after+int(after>=second)
        source = ((a,second),)+tuple((move(c),move(d)) for c,d in pairs[:-1])
        require(laminar_valid(source), 'constructed endpoint source valid')
        require(source not in answer, 'no repeated inverse source')
        answer.add(source)
    return answer


def graph_by_nested_sets(nxt):
    # The eventual image is extracted without a theorem-dependent cutoff.
    image = set(nxt)
    epochs = 0
    while True:
        new = {nxt[x] for x in image}
        epochs += 1
        if new == image:
            break
        image = new
    core = image
    layers = {x:0 for x in core}
    arrived = set(core)
    t = 0
    while len(arrived) < len(nxt):
        t += 1
        new = {x for x in nxt if nxt[x] in arrived}
        require(arrived < new, 'strict backward layer growth')
        layers.update((x,t) for x in new-arrived)
        arrived = new
    return core,layers,epochs


def main():
    states = [()]
    total = 0
    previous_degree = Counter({1:1})
    for n in range(8):
        if n:
            states = [new for old in states for new in insert_maximum(old)]
        require(len(states) == len(set(states)) == prod(range(1,2*n,2)), 'unique complete carrier')
        require(all(laminar_valid(x) for x in states), 'every interval nesting valid')
        nxt = {x:forward(x) for x in states}
        require(set(nxt.values()) <= set(states), 'literal closure')
        pre = defaultdict(set)
        for x,y in nxt.items():
            pre[y].add(x)
        core,depth,epochs = graph_by_nested_sets(nxt)
        degrees, hist, max_targets = Counter(),Counter(),set()
        for x in states:
            internal = {j+1 for j,(a,b) in enumerate(x) if b>a+1}
            next_internal = {j+1 for j,(a,b) in enumerate(nxt[x]) if b>a+1}
            require(next_internal == {j-1 for j in internal if j>1}, 'all internal labels transport')
            require(depth[x] == max(internal, default=0), 'exact pointwise clock')
            require((x in core) == (not internal), 'complete recurrent iff')
            hist[depth[x]] += 1
            roots = exposed(x)
            degrees[len(roots)+1] += 1
            candidates = inverse(x)
            require(candidates == pre[x], 'entire target inverse set')
            if n:
                a,b = x[-1]
                supported = any(j==n-1 for _,_,j in roots)
                expected = 1+sum(c>b for c,d,j in roots) if supported else 0
                require(len(pre[x]) == expected, 'target only count incl zero')
                if len(pre[x]) == n:
                    max_targets.add(x)
            else:
                require(pre[x] == {x}, 'empty boundary fibre')
        require(len(core) == factorial(n), 'recurrent census')
        image_count = sum(bool(pre[x]) for x in states)
        require(image_count == (2**(n-1)*factorial(n-1) if n else 1), 'image census')
        require(sum(map(len,pre.values())) == len(states), 'all target mass')
        if n:
            require(max(depth.values()) == n-1, 'sharp tail')
            require(max(map(len,pre.values())) == n, 'maximum fibre')
            expected_max = {x for x in core if x[-1] == (0,1)}
            require(max_targets == expected_max, 'all extremal equality targets')
            require(len(max_targets) == factorial(n-1), 'extremal equality census')
            for t in range(n):
                require(sum(v for d,v in hist.items() if d<=t) == factorial(n+t)//(2**t*factorial(t)), 'every CDF coefficient')
            # Fixed-iterate census on the independently stabilized core.
            iterate = {x:x for x in core}
            for t in range(1,2*n+1):
                iterate = {x:nxt[y] for x,y in iterate.items()}
                require(sum(x==y for x,y in iterate.items()) == (factorial(n) if t%n==0 else 0), 'exact core iterate trace')
            predicted = Counter()
            for e,count in previous_degree.items():
                predicted[e] += (2*n-1-e)*count
                predicted[e+1] += e*count
            require(+predicted == degrees, 'root gap polynomial all coefficients')
        previous_degree = degrees
        total += len(states)
        print(f'n={n} sources={len(states)} targets={len(states)} image={image_count} recurrent={len(core)} tail={max(depth.values())} image_stabilization_epoch={epochs} depths={tuple(hist[t] for t in range(max(depth.values())+1))}')
    print(f'full_sources={total} full_targets={total}')
    print(f'assertions={CHECKS}')
    print('status=PASS')
    print('findings=critical:0,major:0,minor:0')
    print('external_status=OWNER_AMBER/HOLD_EXTERNAL')


if __name__ == '__main__':
    main()
