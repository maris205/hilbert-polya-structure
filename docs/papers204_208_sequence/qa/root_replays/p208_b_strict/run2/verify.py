"""Prereading independent P208 B chord-bitmask/reverse-agenda kernel."""
import json
import sys

CHECKS = 0

def require(test, label):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(label)

def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit

class Polygon:
    def __init__(self, n):
        require(3 <= n <= 10, "declared polygon box")
        self.n = n
        self.chords = [(a, b) for a in range(n) for b in range(a + 2, n)
                       if (a, b) != (0, n - 1)]
        self.index = {e: i for i, e in enumerate(self.chords)}
        self.conflict = []
        for a, b in self.chords:
            self.conflict.append(sum(1 << j for j, (c, d) in enumerate(self.chords)
                                     if a < c < b < d or c < a < d < b))
        self.states = []
        def select(mask, candidates, left):
            if left == 0:
                self.states.append(mask)
                return
            while candidates.bit_count() >= left:
                bit = candidates & -candidates
                candidates ^= bit
                j = bit.bit_length() - 1
                select(mask | bit, candidates & ~self.conflict[j], left - 1)
        select(0, (1 << len(self.chords)) - 1, n - 3)
        self.states.sort()
        self.state_set = set(self.states)

    def side(self, mask, a, b):
        a, b = sorted((a, b))
        if b == a + 1 or (a, b) == (0, self.n - 1):
            return True
        return bool(mask & (1 << self.index[a, b]))

    def replacement(self, mask, j):
        a, b = self.chords[j]
        opposite = [v for v in range(self.n) if v not in (a, b)
                    and self.side(mask, a, v) and self.side(mask, b, v)]
        require(len(opposite) == 2, "unique cyclic quadrilateral")
        u, v = sorted(opposite)
        k = self.index[u, v]
        require(bool(self.conflict[j] & (1 << k)), "opposite diagonals cross")
        return k

    def flip(self, mask, j):
        require(bool(mask & (1 << j)), "scheduled edge remains present")
        k = self.replacement(mask, j)
        ans = mask ^ (1 << j) ^ (1 << k)
        require(ans in self.state_set, "flip remains compatible maximal set")
        return ans, k

    def sweep(self, mask):
        current = mask
        for j in bits(mask):
            current, _ = self.flip(current, j)
        return current

    def predecessors(self, target):
        answers = []
        def undo(current, upper, restored, remaining):
            if remaining == 0:
                require(current == restored, "all original edges reconstructed")
                answers.append(current)
                return
            for j in bits(current & ~restored):
                previous, k = self.flip(current, j)
                if k >= upper or restored & (1 << k):
                    continue
                undo(previous, k, restored | (1 << k), remaining - 1)
        undo(target, len(self.chords), 0, self.n - 3)
        require(len(answers) == len(set(answers)), "unique inverse agenda history")
        return sorted(answers)

def produce():
    records = []
    total = 0
    catalan_counts = [1, 2, 5, 14, 42, 132, 429, 1430]
    for n in range(3, 11):
        p = Polygon(n)
        require(len(p.states) == catalan_counts[n - 3], "complete Catalan carrier size")
        total += len(p.states)
        transition = {s: p.sweep(s) for s in p.states}
        source_sets = {s: [] for s in p.states}
        for s, t in transition.items():
            source_sets[t].append(s)
        rows, cycles = [], set()
        for s in p.states:
            decoded = p.predecessors(s)
            require(decoded == source_sets[s], "reverse-agenda complete source-set equality")
            trajectory, seen, cur = [], {}, s
            while cur not in seen:
                seen[cur] = len(trajectory)
                trajectory.append(cur)
                cur = transition[cur]
            depth = seen[cur]
            cycle = trajectory[depth:]
            rotation = min(tuple(cycle[j:] + cycle[:j]) for j in range(len(cycle)))
            cycles.add(rotation)
            rows.append({"mask": s, "edges": [list(p.chords[j]) for j in bits(s)],
                         "next": transition[s], "predecessors": decoded,
                         "depth": depth, "cycle": list(rotation)})
        maximum = max(len(row["predecessors"]) for row in rows)
        require(maximum == (1 if n < 5 else 2 ** (n - 4)), "claimed sharp fibre maximum")
        require(max(row["depth"] for row in rows) == (0 if n < 5 else n - 2),
                "claimed sharp entrance")
        require(len(cycles) == 1 and len(next(iter(cycles))) == (1 if n == 3 else 2),
                "claimed unique recurrent orbit")
        if n >= 5:
            fans = [row for row in rows if len(row["predecessors"]) == maximum]
            require(len(fans) == 1 and all(1 in edge for edge in fans[0]["edges"]),
                    "unique labelled extremal fan at vertex one")
        records.append({"n": n, "chords": p.chords, "rows": rows,
                        "cycles": [list(c) for c in sorted(cycles)],
                        "max_fibre": maximum})
    require(total == 2055, "exact original total")
    return {"representation": "chord-bitmask/crossing-compatible-subsets/reverse-agenda",
            "total_states": total, "checks": CHECKS, "polygons": records}


# Post-prereading proof pressure, implemented with labelled laminar intervals.
# The protected-cell / K identities are shared deductions from the manuscript,
# not a claimed new proof or a renamed independent tree/face carrier.
from functools import lru_cache
from itertools import product

POLYGONS = {}
E = (1, ())
C = (2, ((0, 2),))

@lru_cache(None)
def polygon(n):
    return Polygon(n)

def join(a, b):
    N = a[0] + b[0]
    require(N <= 9, "no constructed shape beyond original leaf bound")
    spans = list(a[1]) + [(i+a[0], j+a[0]) for i, j in b[1]] + [(0, N)]
    return N, tuple(sorted(spans))

def restrict(shape, lo, hi):
    return hi-lo, tuple((a-lo, b-lo) for a, b in shape[1] if lo <= a < b <= hi)

@lru_cache(None)
def split_shape(shape):
    N, spans = shape
    require(N >= 2, "split nonleaf")
    present = set(spans)
    middle = [k for k in range(1, N)
              if (k == 1 or (0, k) in present)
              and (N-k == 1 or (k, N) in present)]
    require(len(middle) == 1, "unique interval cut at root")
    return restrict(shape, 0, middle[0]), restrict(shape, middle[0], N)

def to_shape(p, mask):
    return p.n-1, tuple(sorted([(0, p.n-1)] + [p.chords[j] for j in bits(mask)]))

def to_mask(shape):
    N, spans = shape
    require(2 <= N <= 9, "actual polygon size only")
    p = polygon(N+1)
    return sum(1 << p.index[e] for e in spans if e != (0, N))

@lru_cache(None)
def geom(shape):
    if shape == E:
        return E
    p = polygon(shape[0]+1)
    return to_shape(p, p.sweep(to_mask(shape)))

def ggeom(shape):
    return geom(join(E, shape))

def left_comb(N):
    return N, tuple((0, j) for j in range(2, N+1))

def right_comb(N):
    return N, tuple((i, N) for i in range(N-1))

def is_left(shape):
    return shape == left_comb(shape[0])

def graft_first(shape, inserted):
    # Replacing the boundary interval [0,1] by a polygon of inserted[0] leaves.
    d = inserted[0]-1
    spans = list(inserted[1])
    spans += [(0 if a == 0 else a+d, b+d) for a, b in shape[1]]
    return shape[0]+d, tuple(sorted(spans))

def spine_intervals(shape):
    answer = []
    N = shape[0]
    # The old neighbours of polygon vertex 0 determine consecutive arc cells.
    points = sorted({1, N} | {b for a, b in shape[1] if a == 0})
    for lo, hi in zip(points, points[1:]):
        answer.append(restrict(shape, lo, hi))
    return tuple(answer)

def fold(parts):
    ans = E
    for item in parts:
        ans = join(ans, item)
    return ans

def cell_product(parts):
    require(len(parts) >= 2, "seed has two branches")
    ans = geom(join(parts[0], parts[1]))
    for branch in parts[2:]:
        ans = graft_first(ggeom(branch), ans)
    return ans

def protected_prediction(shape):
    if shape == E or shape == C:
        return shape
    a, b = split_shape(shape)
    if a != E:
        return join(E, cell_product(spine_intervals(shape)))
    if b == E:
        return C
    u, v = split_shape(b)
    if u == E:
        return graft_first(ggeom(v), C)
    return join(C, cell_product(spine_intervals(b)))

def wrapped(shape, count):
    for _ in range(count):
        shape = join(E, shape)
    return shape

@lru_cache(None)
def parser(shape, kind):
    if shape == E:
        return (E,) if kind == "F" else ()
    left, right = split_shape(shape)
    if not is_left(left):
        return ()
    if right == E:
        return (right_comb(shape[0] - (kind == "G")),)
    if kind == "G" and left == E:
        return ()
    return tuple(wrapped(fold(parts), left[0]-1-(kind == "G"))
                 for parts in parse_lists(right))

@lru_cache(None)
def parse_lists(shape):
    pieces = spine_intervals(shape)
    answer = []
    # Independent cut enumeration in an ordered interval partition.
    for cutmask in range(1 << (len(pieces)-1)):
        stops = [0] + [j+1 for j in range(len(pieces)-1) if cutmask & (1 << j)] + [len(pieces)]
        blocks = [fold(pieces[a:b]) for a, b in zip(stops, stops[1:])]
        seeds = parser(blocks[0], "F")
        tails = [parser(block, "G") for block in blocks[1:]]
        for seed in seeds:
            first, second = split_shape(seed)
            for tail in product(*tails):
                answer.append((first, second)+tail)
    return tuple(answer)

@lru_cache(None)
def evaluated(shape):
    if shape == E:
        return 1
    gaps = [0]
    decorations = []
    for piece in spine_intervals(shape):
        if piece == E:
            gaps[-1] += 1
        else:
            decorations.append(piece)
            gaps.append(0)
    if not decorations:
        return 2 ** (gaps[0]-1)
    if any(x == 0 for x in gaps[1:-1]):
        return 0
    exponent = max(gaps[0]-1, 0)+sum(x-1 for x in gaps[1:-1])+max(gaps[-1]-1, 0)
    count = 2 ** exponent
    for piece in decorations:
        count *= evaluated(piece)
    return count

@lru_cache(None)
def kgeom(shape):
    if shape == E or shape == C:
        return shape
    left, right = split_shape(shape)
    if left != E:
        return geom(geom(shape))
    # Same-size consequence of G((e,R)) = iota(G(R),c); all actual F
    # evaluations are on this polygon or smaller, never N+1/N+2 above nine.
    a, q = split_shape(ggeom(right))
    require(is_left(a), "geometric G output left comb")
    return graft_first(ggeom(q), left_comb(a[0]))

def closed(shape):
    if shape[0] <= 2:
        return shape == left_comb(shape[0])
    left, _ = split_shape(shape)
    return left[0] >= 2 and is_left(left)

def zshape(N):
    return E if N == 1 else C if N == 2 else join(C, zshape(N-2))

def witness_shape(N):
    require(3 <= N <= 9, "witness original bound")
    ans = join(E, C)
    for _ in range(N-3):
        ans = join(ans, E)
    return ans

def jpow(shape, k):
    for _ in range(k):
        shape = join(C, shape)
    return shape

def orbit(start, transition):
    current, path, seen = start, [], {}
    while current not in seen:
        seen[current] = len(path)
        path.append(current)
        current = transition[current]
    return path, seen[current], path[seen[current]:]

def full_produce():
    data = produce()  # First independently reconstruct all complete F graphs.
    for box in data["polygons"]:
        n, N = box["n"], box["n"]-1
        p = polygon(n)
        shapes = {r["mask"]: to_shape(p, r["mask"]) for r in box["rows"]}
        require(len(set(shapes.values())) == len(p.states), "labelled interval injection")
        fk = {s: to_mask(kgeom(t)) for s, t in shapes.items()}
        ft = {r["mask"]: r["next"] for r in box["rows"]}
        kinvariant = set()
        gpre = {s: [] for s in shapes}
        smaller = [E] if n == 3 else [to_shape(polygon(n-1), s) for s in polygon(n-1).states]
        for shape in smaller:
            gpre[to_mask(ggeom(shape))].append(shape)
        for row in box["rows"]:
            s, t = row["mask"], shapes[row["mask"]]
            a, b = split_shape(t)
            require(to_mask(t) == s and join(a,b) == t, "interval roundtrip")
            require(spine_intervals(t) and fold(spine_intervals(t)) == t, "geometric arc-spine roundtrip")
            require(protected_prediction(t) == shapes[row["next"]], "all protected-cell branches")
            expected = evaluated(b) if is_left(a) else 0
            require(expected == len(row["predecessors"]), "evaluated all-target fibre")
            require(expected == 0 or expected & (expected-1) == 0, "positive fibre power")
            decoded = parser(t, "F")
            decoded_masks = [to_mask(q) for q in decoded]
            require(len(decoded_masks) == len(set(decoded_masks)), "parser disjointness")
            require(sorted(decoded_masks) == row["predecessors"], "parser vs independent reverse-agenda exact sources")
            gdecoded = parser(t, "G")
            require(len(gdecoded) == len(set(gdecoded)) and set(gdecoded) == set(gpre[s]), "all G source-set boundaries")
            require(evaluated(t) <= 2 ** (N-2), "strict decoration upper bound")
            require((evaluated(t) == 2 ** (N-2)) == is_left(t), "all strict equality cases")
            if N <= 8:
                lists = parse_lists(t)
                require(len(lists) == len(set(lists)), "cell-list uniqueness")
                require(len(lists) == evaluated(t), "cell-list count")
                for parts in lists:
                    require(cell_product(parts) == t, "each decoded interval cell list maps back")
            path, depth, cycle = orbit(s, fk)
            kinvariant.update(cycle)
            row["intervals"] = t[1]
            row["K_next"] = fk[s]
            row["K_depth"] = depth
            row["G_source_intervals"] = sorted(gdecoded)
            row["parser_sources"] = sorted(decoded_masks)
            require(depth <= N//2 if N>=3 else depth == 0, "K arbitrary clock")
            if N >= 3:
                require(closed(kgeom(t)), "K full image closure")
                if closed(t):
                    ka, kb = split_shape(kgeom(t))
                    require(ka == C and closed(kb), "strong K closure including N3 N4")
                    require(depth <= (N-2)//2, "K closed-class clock")
            if a == E:
                require(geom(geom(t)) == join(E, kgeom(b)), "leaf-phase square")
            else:
                require(geom(geom(t)) == kgeom(t), "non-ear square construction")
            if N+1 <= 9:
                require(kgeom(ggeom(t)) == ggeom(kgeom(t)), "KG equals GK")
                require(protected_prediction(join(E,t)) == ggeom(t), "G dictionary")
            if N+2 <= 9:
                require(ggeom(ggeom(t)) == join(C,kgeom(t)), "independent defining G2 factorization")
                require(kgeom(join(C,t)) == join(C,kgeom(t)), "K cherry transport")
            if row["predecessors"] and N>=3:
                require(row["depth"] <= N-2, "every first image sharp upper bound")
        require(kinvariant == {to_mask(zshape(N))}, "full K recurrent state")
        box["K_cycle"] = sorted(kinvariant)
        if n >= 5:
            witness = to_mask(witness_shape(N))
            path, depth, _ = orbit(witness, ft)
            require(depth == N-1, "sharp witness full depth")
            require(ft[witness] == to_mask(join(E,witness_shape(N-1))), "witness first update")
            expected_k = left_comb(4) if N == 4 else join(C,witness_shape(N-2))
            require(fk[witness] == to_mask(expected_k), "witness K transport")
            tail = jpow(left_comb(4), N//2-2)
            if N % 2:
                tail = join(E,tail)
            require(path[N-2] == to_mask(tail), "exact both-parity terminal obstruction")
            require(path[N-2] not in set(box["cycles"][0]) and ft[path[N-2]] in set(box["cycles"][0]),
                    "last unit cannot be lost")
            box["witness"] = witness
            box["witness_full_orbit_to_core"] = path[:depth+1]
        else:
            box["witness"] = None
            box["witness_full_orbit_to_core"] = None
    require(geom(E) == E and ggeom(E) == C and kgeom(E) == E and kgeom(C) == C, "formal bases")
    data["checks"] = CHECKS
    data["proof_pressure"] = "laminar labelled intervals; geometry-evaluated F and smaller-cell K; shared structural equations disclosed"
    return data

if __name__ == "__main__":
    print(json.dumps(full_produce(), sort_keys=True, separators=(",", ":")))
