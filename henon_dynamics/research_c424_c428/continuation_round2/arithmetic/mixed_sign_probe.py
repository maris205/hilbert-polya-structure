#!/usr/bin/env python3
"""One frozen short-word falsification probe; never an all-period proof."""
import itertools
import json
import sympy as s

a, alpha, beta, r, C, t = s.symbols("a alpha beta r C t")


def canonical(e, d):
    n = len(e)
    reps = []
    for j in range(n):
        er = e[j:] + e[:j]
        dr = d[j:] + d[:j]
        reps.append(tuple((x * er[0], y * dr[0]) for x, y in zip(er, dr)))
    return min(reps)


def run():
    stats = {"cutoff": 6, "characteristic": 0, "linear_systems": 0,
             "consistent_linear_systems": 0, "by_length": {}}
    for n in range(2, 7):
        seen = set()
        for tail in itertools.product((-1, 1), repeat=2 * (n - 1)):
            e = (1,) + tail[:n - 1]
            d = (1,) + tail[n - 1:]
            w = tuple(x * y for x, y in zip(e, d))
            if len(set(w)) == 1:
                continue
            word = tuple(zip(e, d))
            if any(n % j == 0 and word == word[:j] * (n // j)
                   for j in range(1, n)):
                continue
            key = canonical(e, d)
            if key in seen:
                continue
            seen.add(key)
            b = [(e[(i + 1) % n] + a * e[(i - 1) % n] - alpha)
                 / (2 * s.Integer(e[i])) for i in range(n)]
            lin = [s.expand(2 * d[i] * b[i] + beta
                            - d[(i + 1) % n] - a * d[(i - 1) % n])
                   for i in range(n)]
            stats["linear_systems"] += 1
            solset = s.linsolve(lin, (a, alpha, beta))
            if not solset:
                continue
            stats["consistent_linear_systems"] += 1
            aa, al, be = next(iter(solset))
            if aa == 0:
                continue
            sub = {a: aa, alpha: al, beta: be}
            bs = [s.expand(x.subs(sub, simultaneous=True)) for x in b]
            f = [s.expand(bs[i] ** 2 - bs[(i + 1) % n]
                          - aa * bs[(i - 1) % n]) for i in range(n)]
            j = next(j for j in range(n) if w[j] != w[0])
            rr = s.factor(-(f[j] - f[0]) / (2 * (w[j] - w[0])))
            if rr == 0:
                continue
            cc = s.factor(-f[0] - 2 * w[0] * rr)
            constraints = [s.factor(f[i] + 2 * w[i] * rr + cc)
                           for i in range(n)]
            constraints = [x for x in constraints if x != 0]
            free = sorted(set().union(*(x.free_symbols for x in
                          (aa, al, be, rr, cc))), key=str)
            if not constraints:
                answers = [{}]
            elif not free:
                continue
            elif len(free) == 1:
                g = constraints[0]
                for q in constraints[1:]:
                    g = s.gcd(g, q)
                answers = [{free[0]: root} for root in s.solve(g, free[0])]
            else:
                answers = s.solve(constraints, free, dict=True)
            for ans in answers:
                av, alphav, betav, rv, cv = [s.factor(x.subs(ans))
                                             for x in (aa, al, be, rr, cc)]
                if av == 0 or rv == 0:
                    continue
                bv = [s.factor(x.subs(ans)) for x in bs]
                if any(s.simplify(x.subs(ans)) != 0 for x in constraints):
                    continue
                # u=1, v=r, q=t. The parameter field contains free constants.
                ys = [e[i] * t + d[i] * rv / t + bv[i] for i in range(n)]
                param = -t**2 - rv**2 / t**2 + alphav * t + betav * rv / t + cv
                assert all(s.simplify(ys[i] ** 2 + param - ys[(i + 1) % n]
                                     - av * ys[(i - 1) % n]) == 0
                           for i in range(n))
                stats["by_length"][n] = len(seen)
                return {"status": "MIXED_SIGN_COUNTEREXAMPLE", "stats": stats,
                        "n": n, "epsilon": e, "delta": d,
                        "a": str(av), "alpha": str(alphav), "beta": str(betav),
                        "r": str(rv), "C": str(cv), "b": list(map(str, bv)),
                        "c(t)": str(param), "y": list(map(str, ys)),
                        "direct_symbolic_recurrence": True,
                        "scope": "One counterexample, not an exhaustive atlas."}
        stats["by_length"][n] = len(seen)
    return {"status": "NO_CHARACTERISTIC_ZERO_WITNESS_THROUGH_FROZEN_CUTOFF",
            "stats": stats, "scope": "No claim about periods above 6 or positive characteristic."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
