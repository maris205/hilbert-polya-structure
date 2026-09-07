"""Three original bounded literals. No imports from historical science."""
import collections
import itertools
import json
import os
import sys

CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def fth_fibres(f):
    out = list(f)
    fibres = [[] for _ in f]
    for i, v in enumerate(f):
        fibres[v].append(i)
    for block in fibres:
        for i, j in zip(block, block[1:]):
            out[i] = j
    return tuple(out)


def fth_coordinates(f):
    return tuple(next((j for j in range(i + 1, len(f)) if f[j] == v), v)
                 for i, v in enumerate(f))


def components(f):
    remaining = set(range(len(f)))
    parts = []
    while remaining:
        todo = [min(remaining)]
        found = set()
        while todo:
            i = todo.pop()
            if i in found:
                continue
            found.add(i)
            todo.append(f[i])
            todo.extend(j for j, v in enumerate(f) if v == i)
        remaining -= found
        parts.append(tuple(sorted(found)))
    return tuple(sorted(parts))


def fth_fixed(f):
    for v in range(len(f)):
        block = [i for i, z in enumerate(f) if z == v]
        if len(block) > 2:
            return False
        if len(block) == 2 and block[1] != v:
            return False
    return True


def fth_inverse(g):
    # Increasing path-cover decoder derived before execution.
    n = len(g)
    eligible = [i for i in range(n) if i < g[i]]
    decoded = set()
    for bits in range(1 << len(eligible)):
        selected = {eligible[j] for j in range(len(eligible)) if bits >> j & 1}
        heads = [g[i] for i in selected]
        if len(heads) != len(set(heads)):
            continue
        ends = [i for i in range(n) if i not in selected]
        values = [g[i] for i in ends]
        if len(values) != len(set(values)):
            continue
        old = []
        for i in range(n):
            j = i
            while j in selected:
                j = g[j]
            old.append(g[j])
        decoded.add(tuple(old))
    return decoded


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for b in vertices[1:]:
        rest = tuple(v for v in vertices if v != a and v != b)
        for tail in matchings(rest):
            yield ((a, b),) + tail


def partner(edges, size):
    out = [-1] * size
    for a, b in edges:
        out[a] = b
        out[b] = a
    return tuple(out)


def edges(m):
    return frozenset((i, v) for i, v in enumerate(m) if i < v)


def repair_paths(m, imposed):
    c = dict(itertools.chain.from_iterable(((a, b), (b, a)) for a, b in imposed))
    out = [-1] * len(m)
    for a, b in imposed:
        out[a], out[b] = b, a
    for start in range(len(m)):
        if start in c or out[start] != -1:
            continue
        v = m[start]
        seen = {start}
        while v in c:
            check(v not in seen, ('path_loop', m, sorted(imposed), start))
            seen.add(v)
            v = m[c[v]]
        out[start], out[v] = v, start
    return tuple(out)


def repair_switches(m, imposed):
    # Separate implementation: sequentially impose disjoint edges.
    out = list(m)
    for a, b in sorted(imposed):
        if out[a] == b:
            continue
        x, y = out[a], out[b]
        out[a], out[b] = b, a
        out[x], out[y] = y, x
    return tuple(out)


def mcr(triple, method):
    sets = tuple(edges(m) for m in triple)
    return tuple(method(triple[i], sets[(i + 1) % 3] & sets[(i + 2) % 3])
                 for i in range(3))


def common(triple):
    a, b, c = (edges(m) for m in triple)
    return a & b & c


def majority(triple):
    a, b, c = (edges(m) for m in triple)
    return (a & b) | (b & c) | (c & a)


def tcr_structures(shape):
    a, b, c = shape
    cells = tuple(itertools.product(range(a), range(b), range(c)))
    idx = {v: j for j, v in enumerate(cells)}
    witnesses = []
    tetrads = set()
    for i, j, k in cells:
        masks = []
        for u, v, w in cells:
            if u == i or v == j or w == k:
                continue
            mask = sum(1 << idx[z] for z in ((i, v, w), (u, j, w), (u, v, k)))
            masks.append(mask)
            tetrads.add(mask | (1 << idx[(i, j, k)]))
        witnesses.append(tuple(sorted(set(masks))))
    for tetrad in tetrads:
        check(tetrad.bit_count() == 4, ('tetrad_size', shape, tetrad))
        for i in range(len(cells)):
            if tetrad >> i & 1:
                check((tetrad ^ (1 << i)) in witnesses[i], ('tetrad_symmetry', shape))
    return cells, witnesses, tuple(sorted(tetrads))


def tcr_existential(state, witnesses):
    out = 0
    for i, masks in enumerate(witnesses):
        if any(state & mask == mask for mask in masks):
            out |= 1 << i
    return out


def tcr_tetrads(state, tetrads):
    out = 0
    for tetrad in tetrads:
        active = state & tetrad
        k = active.bit_count()
        if k == 4:
            out |= tetrad
        elif k == 3:
            out |= tetrad ^ active
    return out


def analyze(label, parameter, states, transition):
    count = len(states)
    indeg = [0] * count
    for v in transition:
        check(0 <= v < count, ('closure', label, parameter, v))
        indeg[v] += 1
    work = indeg[:]
    queue = collections.deque(i for i, d in enumerate(work) if d == 0)
    peeled = []
    while queue:
        u = queue.popleft()
        peeled.append(u)
        v = transition[u]
        work[v] -= 1
        if work[v] == 0:
            queue.append(v)
    cycles = []
    cycle_id = [-1] * count
    for start in range(count):
        if work[start] == 0 or cycle_id[start] >= 0:
            continue
        cyc = []
        u = start
        while cycle_id[u] < 0:
            cycle_id[u] = len(cycles)
            cyc.append(u)
            u = transition[u]
        check(u == start, ('cycle_close', label, parameter))
        cycles.append(cyc)
    depth = [0] * count
    for u in reversed(peeled):
        v = transition[u]
        depth[u] = depth[v] + 1
        cycle_id[u] = cycle_id[v]
    # Independently certify recurrent set by repeated full image sets.
    image_chain_sizes = [count]
    current = set(range(count))
    while True:
        following = {transition[u] for u in current}
        if following == current:
            break
        current = following
        image_chain_sizes.append(len(current))
    check(current == {i for i, d in enumerate(depth) if d == 0}, ('core', label, parameter))
    check(len(image_chain_sizes) - 1 == max(depth), ('height', label, parameter))
    check(sum(indeg) == count, ('fibres', label, parameter))
    fibre_sets = [set() for _ in states]
    for i, j in enumerate(transition):
        fibre_sets[j].add(states[i])
    if label == 'FTH':
        for j, g in enumerate(states):
            check(fth_inverse(g) == fibre_sets[j], ('path_decoder', parameter, g))
            check(fth_fixed(g) == (transition[j] == j), ('fixed_fth', parameter, g))
    if label == 'MCR':
        for i, s in enumerate(states):
            check(depth[i] <= parameter - len(common(s)), ('common_clock', parameter, s))
            check((majority(s) == common(s)) == (transition[i] == i), ('fixed_mcr', parameter, s))
    if label == 'TCR' and parameter[:2] == (2, 2):
        for i in states:
            check((transition[transition[i]] & ~i) == 0, ('two_binary_erosion', parameter, i))
    max_fibre = max(indeg)
    deepest = next(i for i, d in enumerate(depth) if d == max(depth))
    witness = [deepest]
    while transition[witness[-1]] not in witness:
        witness.append(transition[witness[-1]])
    cycle_hist = collections.Counter(map(len, cycles))
    result = dict(rule=label, parameter=parameter, states=count, image=sum(v > 0 for v in indeg),
                  recurrent=len(current), height=max(depth), max_fibre=max_fibre,
                  cycle_hist=sorted(cycle_hist.items()), depth_hist=sorted(collections.Counter(depth).items()),
                  fibre_hist=sorted(collections.Counter(indeg).items()),
                  max_fibre_targets=[states[i] for i, d in enumerate(indeg) if d == max_fibre],
                  longest_cycle=[states[i] for i in max(cycles, key=len)],
                  deepest_orbit=[states[i] for i in witness], image_chain_sizes=image_chain_sizes,
                  state_encoding=('lexicographic function tuples' if label == 'FTH' else
                                  'lexicographic ordered triple of lexicographic partner tuples' if label == 'MCR' else
                                  'integer bitmask; lexicographic grid cells, least-significant bit first'),
                  transition=transition, indegrees=indeg, depths=depth,
                  cycle_state_indices=cycles, checks_cumulative=CHECKS)
    print(json.dumps(result, separators=(',', ':'), sort_keys=True), flush=True)


def main():
    for n in range(6):
        states = list(itertools.product(range(n), repeat=n))
        index = {s: i for i, s in enumerate(states)}
        trans = []
        for s in states:
            out = fth_fibres(s)
            check(out == fth_coordinates(s), ('fth_implementations', n, s))
            check(max(collections.Counter(out).values(), default=0) <= 2, ('indegree_two', n, s))
            check(components(s) == components(out), ('component_preserved', n, s))
            trans.append(index[out])
        analyze('FTH', n, states, trans)
    for n in range(4):
        mats = sorted(partner(e, 2 * n) for e in matchings(tuple(range(2 * n))))
        states = list(itertools.product(mats, repeat=3))
        index = {s: i for i, s in enumerate(states)}
        trans = []
        for s in states:
            out = mcr(s, repair_paths)
            check(out == mcr(s, repair_switches), ('mcr_implementations', n, s))
            check(majority(s) <= common(out), ('majority_to_common', n, s))
            check(common(s) <= common(out), ('common_preserved', n, s))
            trans.append(index[out])
        analyze('MCR', n, states, trans)
    for shape in ((0, 2, 2), (1, 2, 2), (2, 2, 2), (2, 2, 3), (2, 3, 3)):
        cells, witnesses, tetrads = tcr_structures(shape)
        states = list(range(1 << len(cells)))
        trans = []
        for s in states:
            out = tcr_existential(s, witnesses)
            check(out == tcr_tetrads(s, tetrads), ('tcr_implementations', shape, s))
            trans.append(out)
        analyze('TCR', shape, states, trans)
    print(json.dumps(dict(result='PASS', boxes=15, states=273331, checks=CHECKS), sort_keys=True), flush=True)
    # Runtime provenance is non-scientific and is emitted on stderr.
    modules = {}
    for name, module in sorted(sys.modules.items()):
        origin = getattr(getattr(module, '__spec__', None), 'origin', None)
        filename = getattr(module, '__file__', None)
        modules[name] = dict(origin=origin, file=filename)
    with open('/proc/self/maps', encoding='utf8') as source:
        mapped = sorted({line.split()[-1] for line in source if '/' in line and os.path.isfile(line.split()[-1])})
    print(json.dumps(dict(modules=modules, mapped_files=mapped, executable=sys.executable,
                          version=sys.version, flags=repr(sys.flags), path=sys.path,
                          xoptions=sys._xoptions, byteorder=sys.byteorder), sort_keys=True), file=sys.stderr)


if __name__ == '__main__':
    main()
