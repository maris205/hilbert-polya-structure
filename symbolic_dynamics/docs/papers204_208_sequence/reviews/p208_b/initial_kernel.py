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

if __name__ == "__main__":
    print(json.dumps(produce(), sort_keys=True, separators=(",", ":")))
