"""One bounded exact FRI pilot; all parameters are literal below.

No file writes, project imports, randomness, network or subprocesses.
Output is a complete aggregate canonical transcript, not a per-state dump.
"""
import itertools
import sys


def step(w):
    a = w[0]
    for j in range(1, len(w)):
        if w[j] == a:
            return w[1:j] + (a,) + w[j:]
    return w[1:] + (a,)


def predicted_clock(w):
    seen = set()
    for j, a in enumerate(w):
        if a in seen:
            return j - 1 if w[j - 1] == a else j
        seen.add(a)
    return 0


def predicted_parents(y):
    parents = set()
    seen = set()
    for j, a in enumerate(y):
        if a not in seen:
            if j + 1 < len(y) and y[j + 1] == a:
                parents.add((a,) + y[:j] + y[j + 1:])
            seen.add(a)
    if y.count(y[-1]) == 1:
        parents.add((y[-1],) + y[:-1])
    return parents


def orbit(w):
    seen = {}
    z = w
    while z not in seen:
        seen[z] = len(seen)
        z = step(z)
    return seen[z], len(seen) - seen[z]


print('FRI_PILOT_V1')
print('scope q=1..4 n=1..6; complete boxes; no cutoff extension')
checks = 0
total_states = 0
for q in range(1, 5):
    for n in range(1, 7):
        states = list(itertools.product(range(q), repeat=n))
        reverse = {y: set() for y in states}
        for w in states:
            reverse[step(w)].add(w)
        periods = {}
        depth_counts = {}
        max_fibre = 0
        for w in states:
            tau, period = orbit(w)
            predicted_tau = predicted_clock(w)
            assert tau == predicted_tau, ('clock', w, tau, predicted_tau)
            checks += 1
            predicted_period = n if len(set(w)) == n else 1
            assert period == predicted_period, ('period', w, period, predicted_period)
            checks += 1
            parents = predicted_parents(w)
            assert reverse[w] == parents, ('inverse', w, reverse[w], parents)
            checks += 1
            periods[period] = periods.get(period, 0) + 1
            depth_counts[tau] = depth_counts.get(tau, 0) + 1
            max_fibre = max(max_fibre, len(reverse[w]))
        expected_height = min(q, n - 1) if q >= 2 and n >= 3 else 0
        assert max(depth_counts) == expected_height, ('height', q, n, depth_counts)
        checks += 1
        assert max_fibre == min(q, (n + 1) // 2), ('max_fibre', q, n, max_fibre)
        checks += 1
        assert sum(map(len, reverse.values())) == len(states)
        checks += 1
        total_states += len(states)
        print('q=%d n=%d states=%d images=%d fixed=%d height=%d max_fibre=%d depths=%s periods=%s' % (
            q, n, len(states), sum(bool(v) for v in reverse.values()),
            sum(step(w) == w for w in states), max(depth_counts), max_fibre,
            sorted(depth_counts.items()), sorted(periods.items())))
print('PASS total_states=%d assertions=%d' % (total_states, checks))
print('RUNTIME executable=' + sys.executable)
print('RUNTIME version=' + repr(sys.version))
print('RUNTIME flags=' + repr(sys.flags))
print('RUNTIME path=' + repr(sys.path))
print('RUNTIME builtins=' + repr(sys.builtin_module_names))
print('RUNTIME modules_begin')
for name, module in sorted(sys.modules.items()):
    filename = getattr(module, '__file__', None)
    if filename:
        print(name + ' ' + filename)
print('RUNTIME modules_end')
print('RUNTIME native_paths_begin')
with open('/proc/self/maps', encoding='ascii') as handle:
    paths = sorted({line.split()[-1] for line in handle if '/' in line})
for path in paths:
    print(path)
print('RUNTIME native_paths_end')
