"""Independent Review A: complete cut-subset graph, no author imports."""
import json
import sys

PARAMETERS = {"mass_min": 1, "mass_max": 12,
              "carrier": "cumulative-cut-bitmask",
              "update": "synchronous-old-weak-increasing-run-sums"}
with open(sys.argv[1] if len(sys.argv) > 1 else "PARAMETERS.json") as f:
    assert json.load(f) == PARAMETERS
checks = 0


def demand(ok):
    global checks
    checks += 1
    assert ok, checks


def blocks(n, mask):
    ends = [0] + [i for i in range(1, n) if mask & (1 << (i-1))] + [n]
    return tuple(zip(ends, ends[1:]))


def parts(n, mask):
    return tuple(v-u for u, v in blocks(n, mask))


def cuts(seq):
    m, pos = 0, 0
    for x in seq[:-1]:
        pos += x
        m |= 1 << (pos-1)
    return m


def step(n, mask):
    old = blocks(n, mask)
    retain = 0
    for (u, v), (w, z) in zip(old, old[1:]):
        demand(v == w)
        if v-u > z-w:
            retain |= 1 << (v-1)
    return retain


def tri(k):
    return k*(k+1)//2


def scan(s):
    r = 1
    suffix = [r]
    for x in s[-2::-1]:
        if x <= r:
            return None
        r = x if x == r+1 else 1
        suffix.append(r)
    return tuple(reversed(suffix))


def encode(s):
    out = [1] * (s[-1]-1)
    threshold = 1
    for x in s[-2::-1]:
        if x == threshold+1:
            threshold += 1
        else:
            demand(x >= threshold+2)
            out.append(tri(threshold+1))
            out.extend([1] * (x-threshold-2))
            threshold = 1
    out.append(tri(threshold))
    return tuple(out)


def decode(q):
    ranks = {tri(k): k for k in range(1, 13)}
    terminal = ranks[q[-1]]
    rest = q[:-1]
    j = 0
    while j < len(rest) and rest[j] == 1:
        j += 1
    read = [j+1]
    while j < len(rest):
        rank = ranks[rest[j]]
        demand(rank >= 2)
        j += 1
        surplus = 0
        while j < len(rest) and rest[j] == 1:
            surplus += 1
            j += 1
        read.extend(range(2, rank))
        read.append(rank+1+surplus)
    read.extend(range(2, terminal+1))
    return tuple(reversed(read))


def coefficient(s, a, b):
    if a == b:
        return int(s % a == 0)
    residual = s-a-b
    if residual < 0:
        return 0
    dp = [1]+[0]*residual
    for coin in range(a, b+1):
        for total in range(coin, residual+1):
            dp[total] += dp[total-coin]
    return dp[residual]


def refine_sources(s, increasing):
    assembled = [()]
    for x in s:
        assembled = [a+r for a in assembled for r in increasing[x]
                     if not a or a[-1] > r[0]]
    return tuple(sorted(cuts(a) for a in assembled))


increasing = {}
endpoints = {}
for n in range(1, 13):
    increasing[n] = [parts(n, m) for m in range(1 << (n-1))
                     if all(a <= b for a, b in zip(parts(n, m), parts(n, m)[1:]))]
    endpoints[n] = {}
    for a in range(1, n+1):
        for b in range(a, n+1):
            c = coefficient(n, a, b)
            demand(c == sum(r[0] == a and r[-1] == b for r in increasing[n]))
            endpoints[n][a, b] = c

graphs = {}
fibres = {}
for n in range(1, 13):
    graphs[n] = [step(n, m) for m in range(1 << (n-1))]
    fibres[n] = [[] for _ in graphs[n]]
    for m, nxt in enumerate(graphs[n]):
        fibres[n][nxt].append(m)

tables = []
total_states = 0
for n in range(1, 13):
    state_rows, target_rows, triangular_rows, witnesses = [], [], [], []
    h = max(k for k in range(n+1) if 1+tri(k) <= n)
    for mask, nxt in enumerate(graphs[n]):
        total_states += 1
        demand(nxt & mask == nxt)
        p = parts(n, mask)
        demand((nxt == mask) == all(a > b for a, b in zip(p, p[1:])))
        cur, time = mask, 0
        born = {b: 0 for b in blocks(n, mask)}
        events = []
        while graphs[n][cur] != cur:
            time += 1
            old, newmask = blocks(n, cur), graphs[n][cur]
            new = blocks(n, newmask)
            removed, births = [], []
            for left, right in zip(old, old[1:]):
                u, v = left
                w, z = right
                if not newmask & (1 << (v-1)):
                    demand(v-u <= z-w)
                    demand(v-u >= time)
                    demand(time == 1 or born[right] == time-1)
                    removed.append([v, v-u, z-w, born[right]])
            for b in new:
                if b not in born:
                    demand(b[1]-b[0] >= 1+tri(time))
                    parents = [a for a in old if b[0] <= a[0] and a[1] <= b[1]]
                    demand(len(parents) >= 2)
                    born[b] = time
                    births.append([b[0], b[1], time])
            demand(newmask != cur and newmask & cur == newmask)
            events.append([time, cur, newmask, removed, births])
            cur = newmask
            demand(time < n)
        demand(time <= h)
        state_rows.append([mask, nxt, time, cur, events])
    demand(max(r[2] for r in state_rows) == h)
    for mask in range(1 << (n-1)):
        s = parts(n, mask)
        pre = fibres[n][mask]
        demand(tuple(pre) == refine_sources(s, increasing))
        sets = []
        for i in range(len(s)):
            tail = s[i:]
            mass = sum(tail)
            f = fibres[mass][cuts(tail)]
            sets.append(sorted({parts(mass, a)[0] for a in f}))
        tested = scan(s)
        demand((tested is not None) == bool(pre))
        if pre:
            demand(tested == tuple(min(a) for a in sets))
        count_by_first = {}
        for x in reversed(s):
            following = count_by_first
            count_by_first = {}
            for a in range(1, x+1):
                count_by_first[a] = sum(endpoints[x][a, b] *
                    (sum(v for c, v in following.items() if c < b) if following else 1)
                    for b in range(a, x+1))
        fibre_formula = sum(count_by_first.values())
        demand(fibre_formula == len(pre))
        encoded = encode(s) if pre else None
        if pre:
            demand(sum(encoded) == n)
            demand(decode(encoded) == s)
        target_rows.append([mask, list(s), pre, sets, tested, fibre_formula, encoded])
        if all(x in {tri(k) for k in range(1, 13)} for x in s):
            decoded = decode(s)
            demand(sum(decoded) == n)
            demand(scan(decoded) is not None)
            demand(bool(fibres[n][cuts(decoded)]))
            demand(encode(decoded) == s)
            triangular_rows.append([mask, s, decoded, cuts(decoded)])
    image_count = sum(bool(x) for x in fibres[n])
    demand(image_count == len(triangular_rows))
    demand(image_count == sum((1 if n-tri(k) == 0 else
               sum(bool(x) for x in fibres[n-tri(k)])) for k in range(1, 13) if tri(k) <= n))
    for k in range(1, n+1):
        surplus = n-1-tri(k)
        if surplus < 0:
            break
        seq = tuple(range(k, 0, -1))+(1+surplus,)
        cur = cuts(seq)
        trajectory = [cur]
        for t in range(1, k+1):
            cur = graphs[n][cur]
            expected = tuple(range(k, t, -1))+(surplus+1+tri(t),)
            demand(parts(n, cur) == expected)
            trajectory.append(cur)
        demand(state_rows[cuts(seq)][2] == k)
        witnesses.append([k, surplus, seq, trajectory])
    tables.append({"N": n, "H": h, "image_count": image_count,
                   "states": state_rows, "targets": target_rows,
                   "triangular": triangular_rows, "witnesses": witnesses})
demand(total_states == 4095)
demand(bool(fibres[7][cuts((2, 3, 2))]) and not fibres[7][cuts((2, 2, 3))])
print(json.dumps({"schema":"p210-review-a-cut-graph-v1", "parameters":PARAMETERS,
    "columns":{"states":["mask","next","tau","fixed","events"],
               "events":["round","oldmask","newmask","deleted_cut_left_right_rightbirth","newblocks"],
               "targets":["mask","parts","sources","attained_suffix_first_sets","scan","fibre_formula","triangular_code"],
               "triangular":["mask","parts","decoded_target","decoded_mask"],
               "witnesses":["h","r","parts","orbit_masks"]},
    "total_states": total_states, "checks":checks, "tables":tables},
    sort_keys=True,separators=(",", ":")))
