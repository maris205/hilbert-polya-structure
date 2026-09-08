#!/usr/bin/env python3
"""Exhaust the analytically proved IR1 core, using exact Python integers.

No chosen parameter bound, period bound, numerical tolerance or random
sample occurs. D_MAX=100 is the theorem's proved reduction constant.
The input contract and termination argument are in IR1_PROOF.md, §4.
Generated JSON files are evidence, not independent proof of the reduction.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import monotonic

D_MAX = 100
OUT = Path(__file__).resolve().parent


def canonical(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def family(a, word):
    n = len(word)
    if n <= 2:
        return "F2"
    for j in range(n):
        w = word[j:] + word[:j]
        t = w[1]
        if n == 3 and w[:2] == (-2, -2) and a == 2*w[2]-4:
            return "F3"
        if n == 4 and w[0] == w[2] == -1 and w[3] == a+1-t:
            return "F4"
        if n == 5 and a == -1 and w == (-1, t, 0, 0, -1-t):
            return "F5"
        if n == 6 and a == 0 and w == (0, 0, w[2], 0, 0, -w[2]):
            return "F6"
        if n == 8 and a == -1 and w == (-1,t,1,t,-1,-t-2,1,-t-2):
            return "F8"
        if n == 12 and a == 0 and t >= 1:
            if w == (1,t,1,t-1,-1,-t,1,1-t,1,-t,-1,t-1):
                return "F12"
    return "EXCEPTION"


def verify_cycle(a, word):
    n = len(word)
    assert n > 0
    for i in range(n):
        assert word[(i+3) % n] == word[(i+1) % n]*word[(i+2) % n]+a-word[i]
    assert all(any(word[i] != word[(i+k) % n] for i in range(n)) for k in range(1,n))


def run():
    start = monotonic()
    counts = Counter()
    exits = Counter()
    cycles = set()
    max_steps = 0
    # No change of a or D during an orbit. Every loop is explicitly finite
    # except its orbit iteration, whose termination follows by injectivity.
    for D in range(1, D_MAX+1):
        lo, hi = -3*D-1, 3*D-1
        for u in range(lo, hi-D+1):
            v = u+D
            for s in (-3,-2,-1,0,1):
                if not lo <= s <= hi:
                    continue
                center_sum = (s+1)*D
                p_lo = max(-D, center_sum-D)
                p_hi = min(D, center_sum+D)
                if u+1:
                    bp = (2*D)//abs(u+1)
                    p_lo, p_hi = max(p_lo,-bp), min(p_hi,bp)
                if v+1:
                    bq = (2*D)//abs(v+1)
                    p_lo, p_hi = max(p_lo,center_sum-bq), min(p_hi,center_sum+bq)
                for p in range(p_lo,p_hi+1):
                    q = center_sum-p
                    assert abs(p)<=D and abs(q)<=D
                    assert abs((u+1)*p)<=2*D and abs((v+1)*q)<=2*D
                    a = v-s*u+s-p
                    seed = (u,s,v)
                    x,y,z = seed
                    word = []
                    counts["seeds"] += 1
                    while True:
                        if not (lo<=x<=hi and lo<=y<=hi and lo<=z<=hi):
                            exits["height"] += 1
                            break
                        if abs(z-x)>D:
                            exits["difference"] += 1
                            break
                        word.append(x)
                        x,y,z = y,z,y*z+a-x
                        if (x,y,z) == seed:
                            w = tuple(word)
                            verify_cycle(a,w)
                            # The extremal normalization may reverse time.
                            # Restore both native orientations explicitly.
                            for candidate in (w, tuple(reversed(w))):
                                verify_cycle(a,candidate)
                                cycles.add((a,canonical(candidate)))
                            counts["returning_seeds"] += 1
                            break
                    max_steps = max(max_steps,len(word))
    ordered = sorted(cycles)
    rows = []
    family_counts = Counter()
    exceptions = []
    for a,w in ordered:
        kind = family(a,w)
        row = {"a":a,"least_period":len(w),"word":list(w),"family":kind}
        rows.append(row)
        family_counts[kind] += 1
        if kind == "EXCEPTION":
            exceptions.append(row)
    assert counts["seeds"] == counts["returning_seeds"] + sum(exits.values())
    raw = "".join(json.dumps(row,separators=(",",":"),sort_keys=True)+"\n" for row in rows)
    (OUT/"IR1_CORE_CYCLES.jsonl").write_text(raw,encoding="utf-8")
    summary = {
        "D_MAX":D_MAX,
        "seed_rule":"IR1_PROOF.md section 4; neighbor bounds included",
        "parameter_cutoff":None,"period_cutoff":None,"exact_integer_arithmetic":True,
        "all_counts":dict(counts),"exit_counts":dict(exits),
        "max_orbit_steps_before_return_or_certified_exit":max_steps,
        "distinct_oriented_cycles_in_completed_seed_output":len(rows),
        "family_cycle_counts_in_finite_certificate_only":dict(sorted(family_counts.items())),
        "exceptions":exceptions,
        "cycle_jsonl_sha256":sha256(raw.encode()).hexdigest(),
        "code_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds":round(monotonic()-start,6),
    }
    (OUT/"IR1_CORE_SUMMARY.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,sort_keys=True))


if __name__ == "__main__":
    run()
