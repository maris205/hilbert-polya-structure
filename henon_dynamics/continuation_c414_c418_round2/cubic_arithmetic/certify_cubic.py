"""Finite proof certificate after the global cubic secant reduction.

This is not a coefficient scan. The large-diameter graphs live in Z[D],
with literal coefficient-pair equality; the small range is D = 2,...,15.
The mathematical reduction and the no-carry threshold need separate proof.
"""

from itertools import product
import json


def cycle_graph(symbols, values):
    """All cycles of (x,y) -> (y, values[y]-x) on the finite symbol square."""
    symbols = tuple(sorted(symbols))
    symbol_set = set(symbols)
    subtract = (lambda x, y: tuple(a-b for a, b in zip(x, y))) if isinstance(symbols[0], tuple) else (lambda x, y: x-y)
    seen = set()
    cycles = []
    for point in product(symbols, repeat=2):
        if point in seen:
            continue
        path, positions = [], {}
        while point not in seen:
            if point in positions:
                cycle = path[positions[point]:]
                word = tuple(x for x, _ in cycle)
                word = min(word[i:]+word[:i] for i in range(len(word)))
                cycles.append(word)
                break
            positions[point] = len(path)
            path.append(point)
            xx, yy = point
            zz = subtract(values[yy], xx)
            if zz not in symbol_set:
                break
            point = (yy, zz)
        seen.update(path)
    return sorted(cycles, key=lambda w: (len(w), w))


def symbolic_certificate():
    rows, extremal_patterns = [], []
    for r in (-1, 0, 1, 2, 3):
        small = [t for t in range(4) if t == 0 or abs(t*(t-r)) <= 2]
        symbols = [(0, t) for t in small]+[(1, 0)]
        sums = set((u[0]+v[0], u[1]+v[1]) for u, v in product(symbols, repeat=2))
        maximum, cases, realized, periods, max_error, max_symbols_per_cycle = 0, 0, 0, set(), 0, 0
        for (k, s), q in product(sorted(sums), range(-2, 3)):
            # f(D) must be a sum of two symbols, just as f(0) is.
            if (k+q, s) not in sums:
                continue
            cases += 1
            values = {(0, t): (k-t*(t-r), s+q*t+t*t*(t-r)) for t in small}
            values[(1, 0)] = (k+q, s)
            for y, u, v in product(symbols, repeat=3):
                max_error = max(max_error, abs(values[y][1]-u[1]-v[1]))
            cycles = cycle_graph(symbols, values)
            size = sum(map(len, cycles))
            maximum = max(maximum, size)
            periods.update(map(len, cycles))
            if cycles:
                max_symbols_per_cycle = max(max_symbols_per_cycle, *(len(set(w)) for w in cycles))
            used = {t for word in cycles for t in word}
            if (0, 0) in used and (1, 0) in used:
                realized += 1
                extremal_patterns.append({'r': r, 'A_coefficients': [k, s], 'q': q, 'cycles': cycles})
        assert max_error < 16
        rows.append({'r': r, 'small_symbols': small, 'endpoint_compatible_cases': cases,
                     'graph_endpoint_cases': realized, 'max_points': maximum,
                     'periods': sorted(periods), 'max_constant_discrepancy': max_error,
                     'max_symbols_per_cycle': max_symbols_per_cycle})
    return {'rows': rows, 'all_graph_endpoint_patterns': extremal_patterns}


def small_certificate():
    rows, equality, all_periods, global_maximum = [], [], set(), -1
    for diameter in range(2, 16):
        maximum, cases, realized, periods, max_symbols_per_cycle = 0, 0, 0, set(), 0
        for r, A, q in product(range(-3, diameter+4), range(2*diameter+1), range(-2, 3)):
            if not 0 <= A+q*diameter <= 2*diameter:
                continue
            cases += 1
            # The necessary secant bound is used only for graph size.
            # Every periodic symbol between actual extrema satisfies it.
            symbols = [t for t in range(diameter+1)
                       if abs(t*(t-diameter)*(t-r)) <= 2*diameter]
            values = {t: A+q*t+t*(t-diameter)*(t-r) for t in symbols}
            cycles = cycle_graph(symbols, values)
            used = {t for word in cycles for t in word}
            if not (0 in used and diameter in used):
                continue
            realized += 1
            size = sum(map(len, cycles))
            maximum = max(maximum, size)
            periods.update(map(len, cycles))
            all_periods.update(map(len, cycles))
            max_symbols_per_cycle = max(max_symbols_per_cycle, *(len(set(w)) for w in cycles))
            if size > global_maximum:
                global_maximum, equality = size, []
            if size == global_maximum:
                equality.append({'D': diameter, 'r': r, 'A': A, 'q': q, 'cycles': cycles})
        rows.append({'D': diameter, 'cases': cases, 'graph_endpoint_cases': realized,
                     'max_points': maximum, 'periods': sorted(periods),
                     'max_symbols_per_cycle': max_symbols_per_cycle})
    return {'rows': rows, 'global_maximum': global_maximum,
            'all_periods': sorted(all_periods), 'all_equality_cases': equality}


def main():
    print(json.dumps({'large_diameter_symbolic': symbolic_certificate(),
                      'small_diameter_exhaustive': small_certificate()}, indent=2))


if __name__ == '__main__':
    main()
