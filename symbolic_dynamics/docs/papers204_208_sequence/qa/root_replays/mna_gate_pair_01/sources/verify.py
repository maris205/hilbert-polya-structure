#!/usr/bin/env python3
"""Nonauthor falsifier: fixed N=1..12, no imported repository science/data.

Primary state is an ordered partition of labelled unit cells. Simultaneous
mergers are connected components of the old-block eligibility graph. Fibres
are checked by explicit monotone refinements and endpoint multiplicity
polynomials, separately from the graph; both bijection directions are checked.
All-size proofs remain deductive inputs, not consequences of this program.
"""
import json

CHECKS = {}

def check(ok, name, detail=None):
    CHECKS[name] = CHECKS.get(name, 0) + 1
    if not ok:
        raise AssertionError((name, detail))

def words(total, least=1):
    """Recursive positive compositions; least=1 is the entire carrier."""
    if total == 0:
        yield ()
    for first in range(least, total + 1):
        for tail in words(total - first):
            yield (first,) + tail

def cell_partition(parts):
    cells, position = [], 0
    for mass in parts:
        cells.append(frozenset(range(position, position + mass)))
        position += mass
    return tuple(cells)

def sizes(blocks):
    return tuple(map(len, blocks))

def component_step(blocks):
    # Compute ALL eligibility edges before doing any component union.
    adjacency = {i: set() for i in range(len(blocks))}
    for i in range(len(blocks) - 1):
        if len(blocks[i]) <= len(blocks[i + 1]):
            adjacency[i].add(i + 1)
            adjacency[i + 1].add(i)
    visited, components = set(), []
    for i in range(len(blocks)):
        if i in visited:
            continue
        todo, vertices = [i], set()
        while todo:
            j = todo.pop()
            if j in vertices:
                continue
            vertices.add(j)
            todo.extend(adjacency[j] - vertices)
        visited.update(vertices)
        cells = frozenset().union(*(blocks[j] for j in vertices))
        components.append(cells)
    return tuple(components)

def monotone_partitions(total, minimum=1):
    if total == 0:
        yield ()
    for first in range(minimum, total + 1):
        for tail in monotone_partitions(total - first, first):
            yield (first,) + tail

def coefficient(total, first, last):
    if first == last:
        return int(total % first == 0)
    # Multiply finite geometric polynomials from scratch, not in-place coin DP.
    target = total - first - last
    if target < 0:
        return 0
    polynomial = {0: 1}
    for value in range(first, last + 1):
        updated = {}
        for degree, count in polynomial.items():
            for multiplicity in range((target - degree) // value + 1):
                exponent = degree + multiplicity * value
                updated[exponent] = updated.get(exponent, 0) + count
        polynomial = updated
    return polynomial.get(target, 0)

def refinement_sources(target, catalog):
    """Construct all legal run refinements, never scanning whole input carrier."""
    partial = [()]
    for mass in target:
        partial = [old + run for old in partial for run in catalog[mass]
                   if not old or old[-1] > run[0]]
    return sorted(partial)

def matrix_fibre(target, endpoint):
    # Left-to-right DP indexed by the final endpoint (author uses suffix firsts).
    previous = {None: 1}
    for mass in target:
        next_values = {}
        for (first, last), coefficient_value in endpoint[mass].items():
            count = sum(v for old_last, v in previous.items()
                        if old_last is None or old_last > first)
            next_values[last] = next_values.get(last, 0) + count * coefficient_value
        previous = next_values
    return sum(previous.values())

def scan(target):
    threshold, records = 1, [1]
    for mass in target[-2::-1]:
        if mass <= threshold:
            return None, records + [None]
        threshold = mass if mass == threshold + 1 else 1
        records.append(threshold)
    return threshold, records

def triangle(k):
    return k * (k + 1) // 2

def encode(target):
    output = [1] * (target[-1] - 1)
    ladder = 1
    for mass in target[-2::-1]:
        check(mass > ladder, 'encode_legality', target)
        if mass == ladder + 1:
            ladder += 1
        else:
            output.append(triangle(ladder + 1))
            output.extend([1] * (mass - ladder - 2))
            ladder = 1
    output.append(triangle(ladder))
    return tuple(output)

def triangular_words(total):
    if total == 0:
        yield ()
    k = 1
    while triangle(k) <= total:
        for rest in triangular_words(total - triangle(k)):
            yield (triangle(k),) + rest
        k += 1

def triangular_index(value):
    k = 1
    while triangle(k) < value:
        k += 1
    check(triangle(k) == value, 'triangular_part', value)
    return k

def decode(code):
    # Final triangular atom is reserved BEFORE parsing any strings of ones.
    last, body = triangular_index(code[-1]), code[:-1]
    index = 0
    while index < len(body) and body[index] == 1:
        index += 1
    read_order = [index + 1]
    while index < len(body):
        k = triangular_index(body[index])
        check(k >= 2, 'decode_reset_atom', body[index])
        index += 1
        ones = 0
        while index < len(body) and body[index] == 1:
            ones += 1
            index += 1
        read_order.extend(range(2, k))
        read_order.append(k + 1 + ones)
    read_order.extend(range(2, last + 1))
    return tuple(reversed(read_order))

def orbit_certificates(source):
    state = cell_partition(source)
    past = None
    orbit, events = [source], []
    time = 0
    while True:
        target = component_step(state)
        if target == state:
            break
        time += 1
        check(time <= len(source) - 1, 'generic_termination', source)
        check(len(target) < len(state), 'strict_coarsening', source)
        old_to_new = {old: next(new for new in target if old <= new) for old in state}
        vanished, new_blocks = [], []
        for left, right in zip(state, state[1:]):
            if old_to_new[left] == old_to_new[right]:
                check(len(left) >= time, 'lemma_A_left_mass', (source, time, sizes(state)))
                check(len(left) <= len(right), 'literal_deleted_cut', (source, time))
                right_new = None
                if time >= 2:
                    right_new = right not in past
                    check(right_new, 'lemma_A_right_born_previous', (source, time))
                    a = next(old for old in reversed(past) if old <= left)
                    c = next(old for old in past if old <= right)
                    check(len(a) > len(c), 'ancestral_surviving_descent', (source, time))
                    check(len(c) >= time - 1, 'ancestral_left_mass', (source, time))
                vanished.append([max(left)+1, len(left), len(right), right_new])
        for new in target:
            parents = [old for old in state if old <= new]
            check(frozenset().union(*parents) == new, 'parent_union', (source, time))
            if len(parents) > 1:
                check(len(new) >= 1 + triangle(time), 'lemma_B_new_mass', (source, time))
                new_blocks.append([min(new), max(new)+1, list(map(len, parents))])
        events.append({'t':time, 'deleted':vanished, 'created':new_blocks})
        past, state = state, target
        orbit.append(sizes(state))
    return orbit, events

def main():
    catalog = {n: list(monotone_partitions(n)) for n in range(1,13)}
    endpoint, endpoint_rows = {}, []
    for total, partitions in catalog.items():
        observed = {}
        for partition in partitions:
            key = (partition[0], partition[-1])
            observed[key] = observed.get(key, 0) + 1
        endpoint[total] = {}
        for first in range(1, total+1):
            for last in range(first, total+1):
                predicted = coefficient(total, first, last)
                check(predicted == observed.get((first,last),0), 'endpoint_polynomial', (total,first,last))
                endpoint[total][first,last] = predicted
                endpoint_rows.append([total,first,last,predicted])
    boxes, recurrence = [], [1]
    for n in range(1,13):
        states = list(words(n))
        check(len(states) == len(set(states)) == 2**(n-1), 'carrier_census', n)
        transitions = {s:sizes(component_step(cell_partition(s))) for s in states}
        fibres = {s:[] for s in states}
        for source, target in transitions.items():
            check(target in fibres and sum(target) == n, 'closed_carrier', source)
            fibres[target].append(source)
        depth = {}
        for source in sorted(states,key=lambda s:(len(s),s)):
            target = transitions[source]
            strict = all(x>y for x,y in zip(source,source[1:]))
            check((source == target) == strict, 'fixed_iff_strict', source)
            depth[source] = 0 if source == target else depth[target] + 1
        h = max(k for k in range(n+1) if 1+triangle(k) <= n)
        rows, image_codes = [], []
        for source in states:
            orbit, events = orbit_certificates(source)
            check(len(orbit)-1 == depth[source], 'graph_depth_vs_orbit', source)
            check(depth[source] <= h, 'sharp_clock_bound', source)
            threshold, scan_states = scan(source)
            minimum = min((p[0] for p in fibres[source]), default=None)
            check(threshold == minimum, 'image_scan_minimum_first', source)
            constructed = refinement_sources(source,catalog)
            check(constructed == fibres[source], 'every_fibre_source_set', source)
            formula = matrix_fibre(source,endpoint)
            check(formula == len(fibres[source]), 'endpoint_formula_fibre', source)
            code = None
            if threshold is not None:
                code = encode(source)
                check(sum(code) == n, 'encode_weight', source)
                check(decode(code) == source, 'decode_encode_identity', source)
                image_codes.append(code)
            rows.append({'state':source,'next':transitions[source], 'tail':depth[source],
                         'terminal':orbit[-1],'orbit':orbit,'events':events,
                         'preimages':fibres[source], 'fibre':len(fibres[source]),
                         'formula':formula,'minimum_first':minimum,
                         'threshold_states':scan_states,'triangular_code':code})
        codewords = sorted(triangular_words(n))
        check(sorted(image_codes) == codewords, 'full_image_bijection_census', n)
        inverse_rows = []
        for code in codewords:
            image = decode(code)
            check(image in fibres and bool(fibres[image]), 'decode_is_image', code)
            check(sum(image) == n, 'decode_weight', code)
            check(encode(image) == code, 'encode_decode_identity', code)
            inverse_rows.append({'code':code,'image':image})
        count = sum(recurrence[n-triangle(k)] for k in range(1,n+1) if triangle(k)<=n)
        recurrence.append(count)
        check(len(codewords) == count, 'known_triangular_recurrence', n)
        check(max(depth.values()) == h, 'sharp_global_maximum', n)
        witnesses = []
        # Pressure the already stated ALL-surplus family at every h allowed by this N.
        for level in range(1,h+1):
            surplus = n - 1 - triangle(level)
            witness = tuple(range(level,0,-1))+(1+surplus,)
            check(depth[witness] == level, 'all_in_box_surplus_witness', (n,level,surplus))
            witnesses.append({'h':level,'r':surplus,'source':witness})
        max_fibre = max(map(len,fibres.values()))
        boxes.append({'N':n,'states':rows,'triangular_preimages':inverse_rows,
                      'summary':{'state_count':len(states),'image_count':len(codewords),
                                 'fixed_count':sum(d==0 for d in depth.values()),
                                 'max_tail':h,'max_fibre':max_fibre,
                                 'max_fibre_targets':[s for s in states if len(fibres[s])==max_fibre],
                                 'surplus_witnesses':witnesses}})
    check(sum(len(b['states']) for b in boxes) == 4095, 'fixed_total_box')
    result={'role':'independent_candidate_falsifier_not_all_size_proof',
            'literal':'simultaneously_sum_maximal_weakly_increasing_old_runs',
            'N_min':1,'N_max':12,'state_count':4095,'endpoint_coefficients':endpoint_rows,
            'boxes':boxes,'checks':CHECKS,'check_count':sum(CHECKS.values()),'status':'PASS'}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__ == '__main__':
    main()
