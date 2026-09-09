"""Exhaustive symbolic end-template check for all integer D>=10.

Coordinates and p-values are pairs (coefficient of D, constant).
Every potential edge is either an identity or occurs at a single exact
integer D. Graphs are checked at all such D and at the generic parameter.
The mathematical end-template reduction must be proved separately.
We overapproximate polynomial restrictions; thus absence is rigorous,
while any surplus cycle must NOT be advertised as an integer realization.
"""
import itertools
import json
import time

from check_integer_periods import exact_cycles


def add(u, v, c=1):
    return u[0] + c * v[0], u[1] + c * v[1]


def scale(u, c):
    return c * u[0], c * u[1]


def at(u, d):
    return u[0] * d + u[1]


def root(u, v):
    slope, constant = add(u, v, -1)
    if slope == 0:
        return None
    if (-constant) % slope:
        return None
    d = (-constant) // slope
    return d if d >= 10 else None


def subsets(items, nonempty=False):
    for mask in range(1 if nonempty else 0, 1 << len(items)):
        yield [x for k, x in enumerate(items) if mask & (1 << k)]


def templates():
    endpoints = [(0, 0), (1, 0)]
    for side in (0, 1):
        for offsets in subsets([1, 2, 3], nonempty=True):
            alphabet = [endpoints[0]]
            alphabet += [(0, b) if side == 0 else (1, -b) for b in offsets]
            alphabet += [endpoints[1]]
            for vals in itertools.product(*[
                range(-2, 3) if b == 1 else range(-1, 2) if b == 2 else [0]
                for b in offsets]):
                if not any(vals):
                    continue
                if any((vals[i] - vals[j]) % (offsets[i] - offsets[j])
                       for i in range(len(vals)) for j in range(i)):
                    continue
                yield ('left' if side == 0 else 'right', alphabet,
                       [0] + list(vals) + [0])
    for left in subsets([1, 2], nonempty=True):
        for right in subsets([1, 2], nonempty=True):
            alphabet = [(0, 0)] + [(0, b) for b in left]
            alphabet += [(1, -b) for b in right] + [(1, 0)]
            bound = 1 if 2 in left + right else 2
            for c in range(-bound, bound + 1):
                if c:
                    yield ('both', alphabet, [0] + [c] * (len(alphabet) - 2) + [0])


def generic_cycles(alphabet, values, sign):
    """Use an integer D avoiding every nonidentity edge equation."""
    critical = {d for u in alphabet for v in values for w in alphabet
                if (d := root(add(v, u, -sign), w)) is not None}
    sample = max(critical, default=9) + 1
    nums = [at(u, sample) for u in alphabet]
    outs = [at(v, sample) for v in values]
    return list(exact_cycles(nums, outs, sign)), critical


def main():
    start = time.monotonic()
    stats = {s: {name: {'templates': 0, 'models': 0, 'viable_models': 0,
                       'generic_periods': set(), 'exceptional_periods': set(),
                       'critical_diameters': set()}
                 for name in ('left', 'right', 'both')} for s in (1, -1)}
    examples = []
    for name, alphabet, hvals in templates():
        for sign in (1, -1):
            rec = stats[sign][name]
            rec['templates'] += 1
            possible_outputs = {add(u, v, sign) for u in alphabet for v in alphabet}
            for intercept in possible_outputs:
                for slope in range(-2, 3):
                    rec['models'] += 1
                    values = []
                    for t, h in zip(alphabet, hvals):
                        # t(t-D)=(-b,b²) for t=b or D-b.
                        b = abs(t[1])
                        values.append(add(add(intercept, scale(t, slope)),
                                          scale((-b, b * b), h)))
                    allowed = None
                    for value in values:
                        if value in possible_outputs:
                            continue
                        hits = {d for out in possible_outputs
                                if (d := root(value, out)) is not None}
                        allowed = hits if allowed is None else allowed & hits
                        if not allowed:
                            break
                    if allowed == set():
                        continue
                    rec['viable_models'] += 1
                    if allowed is None:
                        cycles, critical = generic_cycles(alphabet, values, sign)
                        rec['generic_periods'].update(map(len, cycles))
                    else:
                        critical = allowed
                    for diameter in critical:
                        cycles = list(exact_cycles([at(t, diameter) for t in alphabet],
                                      [at(v, diameter) for v in values], sign))
                        rec['critical_diameters'].add(diameter)
                        rec['exceptional_periods'].update(map(len, cycles))
                        for cycle in cycles:
                            examples.append({'sign': sign, 'family': name,
                                             'diameter': diameter, 'period': len(cycle),
                                             'alphabet': alphabet, 'h': hvals,
                                             'intercept': intercept, 'slope': slope,
                                             'cycle': cycle})
    clean = {s: {name: {k: sorted(v) if isinstance(v, set) else v
                       for k, v in rec.items()} for name, rec in families.items()}
             for s, families in stats.items()}
    print(json.dumps({'scope': 'all integer D>=10 after end-template lemma',
                      'statistics': clean, 'exceptional_cycle_examples': examples,
                      'elapsed_seconds': round(time.monotonic() - start, 3)}, indent=2))


if __name__ == '__main__':
    main()
