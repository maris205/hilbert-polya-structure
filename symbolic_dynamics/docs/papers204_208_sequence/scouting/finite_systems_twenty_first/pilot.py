"""One original full-box NED pilot; no imported scientific kernels."""
import collections
import json
import os
import sys

CHECKS = 0


def check(value, context):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(context)


def compositions(n, mass):
    if n == 1:
        yield (mass,)
        return
    for first in range(mass + 1):
        for tail in compositions(n - 1, mass - first):
            yield (first,) + tail


def dispatch(x):
    n = len(x)
    if all(x):
        return x
    out = list(x)
    for i, value in enumerate(x):
        if value:
            j = (i + 1) % n
            while x[j]:
                j = (j + 1) % n
            out[i] -= 1
            out[j] += 1
    return tuple(out)


def run_lengths(x):
    if all(x):
        return x
    out = []
    n = len(x)
    for i, value in enumerate(x):
        if value:
            out.append(value - 1)
        else:
            size = 0
            j = (i - 1) % n
            while x[j]:
                size += 1
                j = (j - 1) % n
            out.append(size)
    return tuple(out)


def decoder(y):
    n = len(y)
    eligible = {i for i, v in enumerate(y) if v < n}
    cycles = set()
    for start in sorted(eligible):
        walk = []
        seen = {}
        here = start
        while here in eligible and here not in seen:
            seen[here] = len(walk)
            walk.append(here)
            here = (here - y[here] - 1) % n
        if here in seen:
            cycle = tuple(sorted(walk[seen[here]:]))
            if sum(y[j] + 1 for j in cycle) == n:
                cycles.add(cycle)
    sources = [tuple(0 if i in cycle else v + 1 for i, v in enumerate(y))
               for cycle in sorted(cycles)]
    if all(y):
        sources.append(y)
    return sorted(sources), sorted(cycles)


def orbit_data(start, transition):
    seen = {}
    walk = []
    here = start
    while here not in seen:
        seen[here] = len(walk)
        walk.append(here)
        here = transition[here]
    return seen[here], len(walk) - seen[here], walk


def main():
    total_states = 0
    boxes = 0
    for n, max_mass in ((1, 2), (2, 5), (3, 6), (4, 7), (5, 8)):
        for mass in range(max_mass + 1):
            states = list(compositions(n, mass))
            index = {x: i for i, x in enumerate(states)}
            transition = []
            fibres = [[] for _ in states]
            for i, x in enumerate(states):
                y = dispatch(x)
                check(y == run_lengths(x), ('literal_views', n, mass, x))
                check(sum(y) == mass and min(y) >= 0, ('mass', n, mass, x))
                transition.append(index[y])
                fibres[index[y]].append(x)
            rows = []
            depths, periods = [], []
            for i, target in enumerate(states):
                inverse, codes = decoder(target)
                actual = sorted(fibres[i])
                check(actual == inverse, ('all_target_inverse', n, mass, target))
                check(len(codes) <= min(n, mass // n + 1), ('bound', target))
                depth, period, walk = orbit_data(i, transition)
                if mass < n:
                    check(depth == 0 and len(actual) == 1, ('low_mass', n, mass, target))
                depths.append(depth)
                periods.append(period)
                rows.append(dict(state=target, successor=states[transition[i]], entrance=depth,
                    period=period, actual_fibre=actual, decoded_fibre=inverse, codes=codes))
            maximum = max(map(len, fibres))
            summary = dict(n=n, mass=mass, states=len(states), image=sum(bool(f) for f in fibres),
                recurrent=sum(d == 0 for d in depths), max_entrance=max(depths),
                period_histogram=sorted(collections.Counter(periods).items()),
                fibre_histogram=sorted(collections.Counter(map(len, fibres)).items()),
                max_fibre=maximum, max_fibre_targets=[states[i] for i, f in enumerate(fibres) if len(f) == maximum],
                max_entrance_states=[states[i] for i, d in enumerate(depths) if d == max(depths)],
                rows=rows, checks_cumulative=CHECKS)
            print(json.dumps(summary, sort_keys=True, separators=(',', ':')), flush=True)
            boxes += 1
            total_states += len(states)
    check(boxes == 33 and total_states == 1725, ('predeclared_boxes', boxes, total_states))
    print(json.dumps(dict(status='PASS', boxes=boxes, states=total_states, checks=CHECKS), sort_keys=True))
    modules = {}
    for name, module in sorted(sys.modules.items()):
        modules[name] = dict(origin=getattr(getattr(module, '__spec__', None), 'origin', None),
                             file=getattr(module, '__file__', None))
    with open('/proc/self/maps', encoding='utf8') as source:
        mapped = sorted({line.split()[-1] for line in source if '/' in line and os.path.isfile(line.split()[-1])})
    print(json.dumps(dict(modules=modules, mapped_files=mapped, executable=sys.executable,
        version=sys.version, flags=repr(sys.flags), path=sys.path, xoptions=sys._xoptions,
        byteorder=sys.byteorder), sort_keys=True), file=sys.stderr)


if __name__ == '__main__':
    main()
