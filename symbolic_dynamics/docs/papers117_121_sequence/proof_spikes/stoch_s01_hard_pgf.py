#!/usr/bin/env python3
"""Hard exact pilot for S01: BA -> AB and AA -> A.

The script uses only the Python standard library.  Every probability is a
``Fraction``.  It cross-checks three exact descriptions:

* literal words;
* A-populations in the b+1 gaps cut out by the B's;
* the Young-diagram/crossing-count process on the labelled A-particles.

It also verifies the two solvable boundary families and freezes three failed
closed-form guesses.  This is a falsification pilot, not a novelty claim.
"""

from fractions import Fraction
from functools import lru_cache
from math import comb
from random import Random


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def add_laws(*laws):
    answer = {}
    for law, weight in laws:
        for degree, mass in law.items():
            answer[degree] = answer.get(degree, Fraction(0)) + weight * mass
    return {degree: answer[degree] for degree in sorted(answer) if answer[degree]}


def shifted(law, amount=1):
    return {degree + amount: mass for degree, mass in law.items()}


def word_successors(word):
    """Return one successor per literal redex occurrence, retaining duplicates."""
    answer = []
    for index in range(len(word) - 1):
        pair = word[index : index + 2]
        if pair == "BA":
            answer.append(word[:index] + "AB" + word[index + 2 :])
        if pair == "AA":
            answer.append(word[:index] + "A" + word[index + 2 :])
    return tuple(answer)


@lru_cache(maxsize=None)
def word_law(word):
    successors = word_successors(word)
    if not successors:
        return {0: Fraction(1)}
    weight = Fraction(1, len(successors))
    pieces = [(shifted(word_law(nxt)), weight) for nxt in successors]
    return add_laws(*pieces)


@lru_cache(maxsize=None)
def gap_law(gaps):
    """Exact recurrence on x_0,...,x_b in A^x0 B ... B A^xb."""
    b_count = len(gaps) - 1
    terminal = (1,) + (0,) * b_count
    if gaps == terminal:
        return {0: Fraction(1)}

    live = sum(gaps)
    redex_count = live - int(gaps[0] > 0)
    check(redex_count > 0, ("gap dead end", gaps))
    pieces = []

    # Every AA occurrence in gap i gives the same population successor, but
    # its multiplicity x_i-1 must remain in the transition probability.
    for index, population in enumerate(gaps):
        if population >= 2:
            nxt = list(gaps)
            nxt[index] -= 1
            pieces.append(
                (shifted(gap_law(tuple(nxt))), Fraction(population - 1, redex_count))
            )

    # A BA swap transfers the leading A of gap i one gap to the left.
    for index in range(1, b_count + 1):
        if gaps[index]:
            nxt = list(gaps)
            nxt[index] -= 1
            nxt[index - 1] += 1
            pieces.append((shifted(gap_law(tuple(nxt))), Fraction(1, redex_count)))

    return add_laws(*pieces)


@lru_cache(maxsize=None)
def diagram_law(rows, width):
    """Exact recurrence on a partition of particle crossing counts.

    ``rows`` is weakly decreasing.  Selecting a row adds one box if the row
    is strictly shorter than its predecessor; selecting a tied nonfirst row
    deletes that entire row.  Once the first row has width ``b``, it is the
    inactive immortal root.
    """
    if rows == (width,):
        return {0: Fraction(1)}
    root_finished = rows[0] == width
    active = tuple(range(1 if root_finished else 0, len(rows)))
    check(active, ("diagram dead end", rows, width))
    weight = Fraction(1, len(active))
    pieces = []
    for index in active:
        nxt = list(rows)
        if index == 0 or rows[index] < rows[index - 1]:
            nxt[index] += 1
        else:
            del nxt[index]
        pieces.append((shifted(diagram_law(tuple(nxt), width)), weight))
    return add_laws(*pieces)


def block_gap(a_count, b_count):
    return (0,) * b_count + (a_count,)


def block_law_gap(a_count, b_count):
    return gap_law(block_gap(a_count, b_count))


def block_law_diagram(a_count, b_count):
    return diagram_law((0,) * a_count, b_count)


def multiply_polynomials(left, right):
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x_value in enumerate(left):
        for j, y_value in enumerate(right):
            answer[i + j] += x_value * y_value
    return tuple(answer)


def b_one_formula(a_count):
    """z^(a-1) z(z+1)...(z+a-1)/a! as a probability law."""
    polynomial = (Fraction(1),)
    denominator = 1
    for offset in range(a_count):
        polynomial = multiply_polynomials(polynomial, (Fraction(offset), Fraction(1)))
        denominator *= offset + 1
    return {
        degree + a_count - 1: coefficient / denominator
        for degree, coefficient in enumerate(polynomial)
        if coefficient
    }


def catalan(index):
    return comb(2 * index, index) // (index + 1)


def a_two_formula(b_count):
    """Truncated Catalan first-passage law for two initial A-particles."""
    minimum = b_count + 1
    answer = {
        minimum + extra: Fraction(catalan(extra), 2 ** (2 * extra + 1))
        for extra in range(b_count)
    }
    answer[minimum + b_count] = Fraction(comb(2 * b_count, b_count), 2 ** (2 * b_count))
    return answer


def nested_record_depths(arrival_times, width):
    """Iterate upper-record filters on successive Poisson arrival layers."""
    labels = tuple(range(len(arrival_times)))
    depth = [0] * len(labels)
    survivors = labels
    for level in range(width):
        next_survivors = []
        record = None
        for label in survivors:
            value = arrival_times[label][level]
            if record is None or value > record:
                record = value
                next_survivors.append(label)
                depth[label] += 1
        survivors = tuple(next_survivors)
    return tuple(depth)


def clock_process_depths(arrival_times, width):
    """Run the labelled continuous-clock realization for a deterministic clock array."""
    particle_count = len(arrival_times)
    live = list(range(particle_count))
    depth = [0] * particle_count
    events = sorted(
        (time, label, occurrence + 1)
        for label, times in enumerate(arrival_times)
        for occurrence, time in enumerate(times)
    )
    check(len({event[0] for event in events}) == len(events), "clock ties")
    for _, label, _ in events:
        if label not in live:
            continue
        position = live.index(label)
        if position == 0:
            if depth[label] < width:
                depth[label] += 1
            # The first particle is inactive after its width-th crossing.
        else:
            predecessor = live[position - 1]
            if depth[label] < depth[predecessor]:
                depth[label] += 1
            else:
                live.pop(position)
        if live == [0] and depth[0] == width:
            break
    check(live == [0] and depth[0] == width, ("unfinished clock realization", live, depth))
    return tuple(depth)


def deterministic_clock_array(rng, particle_count, width):
    """Produce strictly increasing rational clocks with no global ties."""
    answer = []
    used = set()
    for label in range(particle_count):
        current = Fraction(0)
        row = []
        for occurrence in range(width + 1):
            # Different large prime-like denominators make accidental equality
            # vanishingly rare; retry deterministically if one nevertheless occurs.
            denominator = 1009 + 37 * label + 2 * occurrence
            current += Fraction(rng.randrange(1, 1000), denominator)
            while current in used:
                current += Fraction(1, denominator * 10007)
            used.add(current)
            row.append(current)
        answer.append(tuple(row))
    return tuple(answer)


def cubic_discriminant(a_value, b_value, c_value, d_value):
    return (
        18 * a_value * b_value * c_value * d_value
        - 4 * b_value**3 * d_value
        + b_value**2 * c_value**2
        - 4 * a_value * c_value**3
        - 27 * a_value**2 * d_value**2
    )


def run():
    # Orientation and all three exact recurrences agree on the block family.
    for a_count in range(1, 7):
        for b_count in range(0, 7):
            word = "B" * b_count + "A" * a_count
            literal = word_law(word)
            gaps = block_law_gap(a_count, b_count)
            diagram = block_law_diagram(a_count, b_count)
            check(literal == gaps == diagram, (a_count, b_count, literal, gaps, diagram))
            check(sum(literal.values(), Fraction(0)) == 1, (a_count, b_count, literal))
            lower = a_count + b_count - 1
            upper = a_count * b_count + a_count - 1
            check(tuple(literal) == tuple(range(lower, upper + 1)), (a_count, b_count, literal))

    # Closed edge 1: one B gives the classical record/rising-factorial law.
    for a_count in range(1, 15):
        check(block_law_gap(a_count, 1) == b_one_formula(a_count), ("b=1", a_count))

    # Closed edge 2: two A's give a Catalan first-passage law truncated at b.
    for b_count in range(0, 18):
        check(block_law_gap(2, b_count) == a_two_formula(b_count), ("a=2", b_count))

    # The iterated-record representation is a pathwise identity, not merely a
    # distributional fit.  Check it on deterministic rational clock arrays.
    rng = Random(20260830)
    for particle_count in range(1, 8):
        for width in range(0, 8):
            for trial in range(8):
                clocks = deterministic_clock_array(rng, particle_count, width)
                records = nested_record_depths(clocks, width)
                particles = clock_process_depths(clocks, width)
                check(records == particles, (particle_count, width, trial, records, particles))

    # Exact sentinels in the factored variable X=T-(a+b-1).
    check(
        block_law_gap(2, 3)
        == {
            4: Fraction(1, 2),
            5: Fraction(1, 8),
            6: Fraction(1, 16),
            7: Fraction(5, 16),
        },
        "B^3 A^2 sentinel",
    )
    check(
        block_law_gap(3, 2)
        == {
            4: Fraction(1, 3),
            5: Fraction(1, 9),
            6: Fraction(133, 324),
            7: Fraction(5, 72),
            8: Fraction(49, 648),
        },
        "B^2 A^3 sentinel",
    )

    # Killed conjecture 1: treating successive record layers as independent
    # would give (1/2,1/4,1/4), not the true (1/2,1/8,3/8), at (a,b)=(2,2).
    true_22 = tuple(block_law_gap(2, 2).values())
    independent_layers_22 = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 4))
    check(true_22 == (Fraction(1, 2), Fraction(1, 8), Fraction(3, 8)), true_22)
    check(true_22 != independent_layers_22, "independent record layers survived")

    # Killed conjecture 2: a uniform multiset-linear-extension/SYT measure
    # predicts 2/6 for full survival in the 2x2 rectangle; the clock measure is 3/8.
    check(block_law_gap(2, 2)[5] == Fraction(3, 8), "2x2 maximum mass")
    check(block_law_gap(2, 2)[5] != Fraction(2, 6), "uniform tableau measure survived")

    # Killed conjecture 3: after removing z^(a+b-1), the (2,3) numerator is
    # 8+2z+z^2+5z^3.  Its negative discriminant forces a complex-conjugate
    # root pair, ruling out a rising-factorial/real-linear-factor extension.
    check(cubic_discriminant(5, 1, 2, 8) == -41948, "cubic discriminant")

    print("stoch_s01_hard_pgf: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"word_cache={word_law.cache_info().currsize}")
    print(f"gap_cache={gap_law.cache_info().currsize}")
    print(f"diagram_cache={diagram_law.cache_info().currsize}")
    print("closed_edge_b1=z^(a-1)*(z)^(rising a)/a!")
    print("closed_edge_a2=truncated Catalan first-passage law")
    print("killed=independent_layers, uniform_SYT_measure, real_linear_factor_product")
    print("gate=KILL_no_full_coefficient_law")


if __name__ == "__main__":
    run()
