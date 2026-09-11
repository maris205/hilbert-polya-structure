"""Independent P210 Review B: inverse-refinement incidence, not forward runs.

No author, scout or reviewer implementation is imported or read.
All meaningful finite state and target records are deterministic stdout.
"""
import collections
import functools
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
PARAMETERS = json.loads((HERE / 'PARAMETERS.json').read_text())
checks = 0


def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


@functools.lru_cache(None)
def partitions(total, least=1):
    if total == 0:
        return ((),)
    return tuple((head,) + tail for head in range(least, total + 1)
                 for tail in partitions(total - head, head))


def rearrangements(partition):
    counts = collections.Counter(partition)
    letters = sorted(counts)
    word = []

    def visit():
        if len(word) == len(partition):
            yield tuple(word)
            return
        for letter in letters:
            if counts[letter]:
                counts[letter] -= 1
                word.append(letter)
                yield from visit()
                word.pop()
                counts[letter] += 1
    yield from visit()


def incoming(target):
    """Sparse inverse relation: blocks are partitions, separated by descents."""
    def visit(index, old, block_certificate):
        if index == len(target):
            yield old, block_certificate
            return
        for block in partitions(target[index]):
            if old and old[-1] <= block[0]:
                continue
            yield from visit(index + 1, old + block,
                             block_certificate + (block,))
    yield from visit(0, (), ())


def suffix_threshold(target):
    threshold = 1
    trace = [(target[-1], threshold)]
    for value in reversed(target[:-1]):
        if value <= threshold:
            return None, tuple(trace + [(value, None)])
        threshold = threshold + 1 if value == threshold + 1 else 1
        trace.append((value, threshold))
    return threshold, tuple(trace)


def endpoint_transfer(target):
    table = collections.Counter((p[0], p[-1]) for p in partitions(target[0]))
    running = collections.Counter()
    for (first, last), count in table.items():
        running[last] += count
    stages = [dict(sorted(running.items()))]
    for mass in target[1:]:
        table = collections.Counter((p[0], p[-1]) for p in partitions(mass))
        nxt = collections.Counter()
        for (first, last), count in table.items():
            nxt[last] += count * sum(n for previous, n in running.items()
                                    if previous > first)
        running = +nxt
        stages.append(dict(sorted(running.items())))
    return sum(running.values()), stages


def triangular_compositions(total):
    if total == 0:
        return ((),)
    answer = []
    height = 1
    while height * (height + 1) // 2 <= total:
        weight = height * (height + 1) // 2
        answer.extend((height,) + tail for tail in
                      triangular_compositions(total - weight))
        height += 1
    return tuple(answer)


def encode_image(target):
    """Return triangular heights, using the mathematical reset-cycle code."""
    tokens = [1] * (target[-1] - 1)
    ladder = 1
    for value in reversed(target[:-1]):
        if value <= ladder:
            raise ValueError('target outside image')
        if value == ladder + 1:
            ladder += 1
        else:
            tokens.append(ladder + 1)
            tokens.extend([1] * (value - ladder - 2))
            ladder = 1
    tokens.append(ladder)
    return tuple(tokens)


def decode_triangles(tokens):
    """Reserve last token before grouping the nontrivial tokens and ones."""
    prefix, final = tokens[:-1], tokens[-1]
    index = 0
    while index < len(prefix) and prefix[index] == 1:
        index += 1
    read_backwards = [index + 1]
    while index < len(prefix):
        height = prefix[index]
        require(height >= 2, 'nontrivial triangle token')
        end = index + 1
        while end < len(prefix) and prefix[end] == 1:
            end += 1
        read_backwards.extend(range(2, height))
        read_backwards.append(height + 1 + end - index - 1)
        index = end
    read_backwards.extend(range(2, final + 1))
    return tuple(reversed(read_backwards))


def main():
    require(sys.flags.optimize == 0 and sys.flags.isolated == 1 and
            sys.flags.no_site == 1 and sys.dont_write_bytecode,
            'strict interpreter flags')
    require(PARAMETERS['masses'] == list(range(1, 13)), 'original box')
    census = []
    for mass in PARAMETERS['masses']:
        carrier = tuple(sorted(word for part in partitions(mass)
                               for word in rearrangements(part)))
        require(len(carrier) == len(set(carrier)) == 2 ** (mass - 1),
                ('partition/permutation carrier', mass))
        successors = {}
        predecessor_records = {}
        for target in carrier:
            records = tuple(incoming(target))
            predecessor_records[target] = records
            for source, blocks in records:
                require(source in carrier, ('source membership', source))
                require(source not in successors, ('unique outgoing edge', source))
                require(tuple(map(sum, blocks)) == target, 'block mass')
                require(all(all(a <= b for a, b in zip(block, block[1:]))
                            for block in blocks), 'weak partition blocks')
                require(all(a[-1] > b[0] for a, b in zip(blocks, blocks[1:])),
                        'strict old boundary descents')
                successors[source] = target
        require(set(successors) == set(carrier), ('total map', mass))
        times = {}
        orbits = {}
        for source in sorted(carrier, key=lambda state: (len(state), state)):
            target = successors[source]
            require(sum(source) == sum(target) == mass, 'mass conservation')
            decreasing = all(a > b for a, b in zip(source, source[1:]))
            require((source == target) == decreasing, 'fixed iff strict decrease')
            if target == source:
                times[source] = 0
                orbits[source] = (source,)
            else:
                require(len(target) < len(source), 'DAG strict length rank')
                require(target in times, 'topological rank order')
                times[source] = 1 + times[target]
                orbits[source] = (source,) + orbits[target]
            require(len(set(orbits[source])) == len(orbits[source]), 'no nontrivial cycle')
        height = 0
        while 1 + (height + 1) * (height + 2) // 2 <= mass:
            height += 1
        excess = mass - 1 - height * (height + 1) // 2
        witness = tuple(range(height, 0, -1)) + (1 + excess,)
        require(witness in successors and times[witness] == height, 'all-surplus witness')
        require(max(times.values()) == height, 'sharp triangular global clock')
        states = []
        images = []
        for state in carrier:
            threshold, trace = suffix_threshold(state)
            records = predecessor_records[state]
            actual_minimum = min((old[0] for old, blocks in records), default=None)
            require(threshold == actual_minimum, ('attained minimum', state))
            fibre, stages = endpoint_transfer(state)
            require(fibre == len(records), ('support endpoint formula', state))
            if records:
                images.append(state)
                code = encode_image(state)
                require(decode_triangles(code) == state, 'target encode/decode')
                require(sum(k * (k + 1) // 2 for k in code) == mass,
                        'encode weight')
            else:
                code = None
            states.append({'state': state, 'next': successors[state],
                           'time': times[state], 'orbit': orbits[state],
                           'fixed': successors[state] == state,
                           'preimages': [{'source': old, 'blocks': blocks}
                                         for old, blocks in records],
                           'attained_minimum': actual_minimum,
                           'triangular_code_as_heights': code,
                           'threshold_trace_right_to_left': trace,
                           'fibre': fibre, 'endpoint_stages': stages})
        triangle_words = triangular_compositions(mass)
        require(len(triangle_words) == len(images), 'triangular image enumeration')
        triangular_records = []
        for tokens in triangle_words:
            decoded = decode_triangles(tokens)
            require(decoded in images, 'every triangular word decodes into image')
            require(encode_image(decoded) == tokens, 'triangle decode/encode')
            require(sum(decoded) == mass, 'decode weight')
            triangular_records.append({'heights': tokens, 'decoded': decoded})
        require({encode_image(s) for s in images} == set(triangle_words),
                'exact image code set')
        census.append({'mass': mass, 'carrier_size': len(carrier),
                       'height': height, 'sharp_witness': witness,
                       'image_size': len(images),
                       'triangular_codes': triangular_records,
                       'states': states})
    print(json.dumps({'reviewer': 'p210_b_reviewer',
                      'representation': PARAMETERS['carrier'],
                      'edge_construction': PARAMETERS['edges'],
                      'checks': checks, 'states': sum(x['carrier_size'] for x in census),
                      'census': census}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
