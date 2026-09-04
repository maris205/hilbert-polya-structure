#!/usr/bin/env python3
"""Process-separated exact hostile control for P190 Review A.

This verifier is reviewer-owned, standard-library only, deterministic, and
write-free.  It does not import the author verifier.  States are integer-coded
base-q words, while zero-output powers are rebuilt as directed walk tables.
Those choices differ from the author's tuple/product and matrix-vector code.

Finite exhaustion supplies falsification pressure.  The uniform statements
are established (or rejected) by the accompanying proof rederivation.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
PAPER = ROOT / "papers" / "190-brandt-sandwich-erosion"

PINNED = {
    "main_round0_original.pdf":
        "5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66",
    "main_round1.pdf":
        "81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d",
    "main.tex":
        "73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300",
    "code/verify_p190.py":
        "99bccb56fd9324409f7ee23742dbceda04c76cb887cac7bd8553a1ee84b4f081",
    "code/CANONICAL.txt":
        "9652d76deed795b561f9ceddd28ff4db1f296215f920d97ad4014b3ca75e6b2f",
    "PROOF_PACKAGE.md":
        "01ab488f347c91c41650c860ac8e396b6054bcb749e98efa0a83228cbffa6628",
    "SOURCE_VERIFICATION.md":
        "e873ff99bac17675c124b16a5b5107266e9736f12493bc7f317a5d7de768285c",
}


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, got, expected, label: str) -> None:
        self.assertions += 1
        if got != expected:
            raise AssertionError(f"{label}: got={got!r}, expected={expected!r}")

    def true(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def pin_inputs() -> None:
    for relative, expected in PINNED.items():
        payload = (PAPER / relative).read_bytes()
        AUDIT.equal(sha256(payload).hexdigest(), expected, f"pinned {relative}")
    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    # Round 1 must close exactly the two historical presentation findings.
    AUDIT.equal(source.count(r"(A^{h_j})_{,y_{i_j}^*,\,y_{i_{j+1}}}"), 0,
                "leading gap-subscript comma removed")
    AUDIT.equal(source.count(r"(A^{h_j})_{y_{i_j}^*,\,y_{i_{j+1}}}"), 1,
                "two-index gap entry retained")
    AUDIT.equal(source.count(r"\paragraph{CRediT.}"), 0,
                "double-stop CRediT source removed")
    AUDIT.equal(source.count(r"\paragraph{CRediT}"), 1,
                "single-stop CRediT rendering source retained")
    AUDIT.true("Rows represent the current source letter and columns the next"
               in source, "matrix convention stated")


def star(n: int, letter: int) -> int:
    if letter == 0:
        return 0
    row, column = divmod(letter - 1, n)
    return 1 + column * n + row


def product_unit(n: int, left: int, right: int) -> int:
    """Literal Brandt multiplication, without using the local-filter claim."""
    if left == 0 or right == 0:
        return 0
    a, b = divmod(left - 1, n)
    c, d = divmod(right - 1, n)
    return 1 + a * n + d if b == c else 0


def literal_local(n: int, left: int, right: int) -> int:
    return product_unit(n, product_unit(n, left, right), left)


def unpack_word(serial: int, q: int, length: int) -> tuple[int, ...]:
    digits = []
    for _ in range(length):
        serial, digit = divmod(serial, q)
        digits.append(digit)
    return tuple(digits)


def pack_word(word: tuple[int, ...], q: int) -> int:
    serial = 0
    place = 1
    for letter in word:
        serial += place * letter
        place *= q
    return serial


def literal_step(n: int, word: tuple[int, ...]) -> tuple[int, ...]:
    length = len(word)
    return tuple(literal_local(n, word[i], word[(i + 1) % length])
                 for i in range(length))


def edge_mask(n: int, word: tuple[int, ...]) -> int:
    mask = 0
    length = len(word)
    for i, letter in enumerate(word):
        if letter != 0 and word[(i + 1) % length] == star(n, letter):
            mask |= 1 << i
    return mask


def predicted_iterate(n: int, word: tuple[int, ...], time: int) -> tuple[int, ...]:
    mask = edge_mask(n, word)
    length = len(word)
    output = []
    for i, letter in enumerate(word):
        survives = all(mask & (1 << ((i + offset) % length))
                       for offset in range(time))
        output.append(letter if survives else 0)
    return tuple(output)


def longest_cyclic_one_run(mask: int, length: int) -> int:
    if mask == (1 << length) - 1:
        return length
    best = run = 0
    for offset in range(2 * length):
        if mask & (1 << (offset % length)):
            run += 1
            best = max(best, run)
        else:
            run = 0
    return min(best, length - 1)


def predicted_tail(n: int, word: tuple[int, ...]) -> int:
    if not any(word):
        return 0
    mask = edge_mask(n, word)
    if mask == (1 << len(word)) - 1:
        return 0
    return longest_cyclic_one_run(mask, len(word)) + 1


def orbit_signature(n: int, word: tuple[int, ...]) -> tuple[int, int]:
    first_seen = {}
    state = word
    while state not in first_seen:
        first_seen[state] = len(first_seen)
        state = literal_step(n, state)
    return first_seen[state], len(first_seen) - first_seen[state]


def matrix_multiply(left, right):
    size = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(size))
              for j in range(size))
        for i in range(size)
    )


def identity_matrix(size: int):
    return tuple(tuple(int(i == j) for j in range(size)) for i in range(size))


def matrix_trace(matrix) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def matrix_rank_integer(matrix) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    height = len(rows)
    width = len(rows[0]) if rows else 0
    pivot_row = 0
    for column in range(width):
        pivot = next((i for i in range(pivot_row, height)
                      if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for i in range(height):
            if i == pivot_row or not rows[i][column]:
                continue
            factor = rows[i][column]
            rows[i] = [rows[i][j] - factor * rows[pivot_row][j]
                       for j in range(width)]
        pivot_row += 1
        if pivot_row == height:
            break
    return pivot_row


def zero_walk_tables(n: int, maximum: int):
    q = n * n + 1
    adjacency = tuple(
        tuple(int(literal_local(n, left, right) == 0) for right in range(q))
        for left in range(q)
    )
    powers = [identity_matrix(q)]
    for _ in range(maximum):
        powers.append(matrix_multiply(powers[-1], adjacency))
    return adjacency, tuple(powers)


def target_matrices(n: int):
    q = n * n + 1
    return tuple(
        tuple(tuple(int(literal_local(n, left, right) == output)
                    for right in range(q)) for left in range(q))
        for output in range(q)
    )


def trace_formula(target: tuple[int, ...], matrices) -> int:
    current = identity_matrix(len(matrices))
    for output in target:
        current = matrix_multiply(current, matrices[output])
    return matrix_trace(current)


def gap_formula(n: int, target: tuple[int, ...], zero_powers) -> int:
    anchors = [i for i, letter in enumerate(target) if letter]
    if not anchors:
        return matrix_trace(zero_powers[len(target)])
    answer = 1
    length = len(target)
    for j, position in enumerate(anchors):
        following = anchors[(j + 1) % len(anchors)]
        gap = (following - position - 1) % length
        answer *= zero_powers[gap][star(n, target[position])][target[following]]
    return answer


def image_criterion(n: int, target: tuple[int, ...]) -> bool:
    anchors = [i for i, letter in enumerate(target) if letter]
    if not anchors:
        return True
    length = len(target)
    for j, position in enumerate(anchors):
        following = anchors[(j + 1) % len(anchors)]
        gap = (following - position - 1) % length
        if gap == 0 and target[following] != star(n, target[position]):
            return False
        if gap == 1 and target[following] == target[position]:
            return False
    return True


def recurrence_trace(n: int, exponent: int) -> int:
    r = n * n
    previous, current = 2, r
    for _ in range(2, exponent + 1):
        previous, current = current, r * current + previous
    exceptional = current
    return (exceptional
            + (-1) ** exponent * ((r + n) // 2 - 1)
            + (r - n) // 2)


def spectral_attack(n: int) -> str:
    q = n * n + 1
    r = n * n
    adjacency, powers = zero_walk_tables(n, 12)
    AUDIT.equal(adjacency,
                tuple(tuple(adjacency[j][i] for j in range(q))
                      for i in range(q)),
                f"A symmetric n={n}")

    minus_identity = tuple(
        tuple(adjacency[i][j] - int(i == j) for j in range(q))
        for i in range(q)
    )
    plus_identity = tuple(
        tuple(adjacency[i][j] + int(i == j) for j in range(q))
        for i in range(q)
    )
    plus_mult = q - matrix_rank_integer(minus_identity)
    minus_mult = q - matrix_rank_integer(plus_identity)
    AUDIT.equal(plus_mult, (r - n) // 2, f"+1 multiplicity n={n}")
    AUDIT.equal(minus_mult, (r + n) // 2 - 1, f"-1 multiplicity n={n}")
    AUDIT.equal(plus_mult + minus_mult + 2, q,
                f"exceptional spectral dimension n={n}")

    e0 = (1,) + (0,) * r
    units = (0,) + (1,) * r

    def action(vector):
        return tuple(sum(adjacency[i][j] * vector[j] for j in range(q))
                     for i in range(q))

    AUDIT.equal(action(e0), tuple(1 for _ in range(q)), f"A e0 n={n}")
    AUDIT.equal(action(units), (r,) + (r - 1,) * r, f"A w n={n}")
    # In the ordered basis (e0,w), the columns are (1,1) and (r,r-1).
    AUDIT.equal(1 + (r - 1), r, f"exceptional trace n={n}")
    AUDIT.equal(1 * (r - 1) - r, -1, f"exceptional determinant n={n}")

    for exponent in range(1, 13):
        AUDIT.equal(matrix_trace(powers[exponent]), recurrence_trace(n, exponent),
                    f"zero recurrence n={n} m={exponent}")
    return f"n={n} plus1={plus_mult} minus1={minus_mult} exceptional=2"


def verify_box(n: int, length: int) -> str:
    q = n * n + 1
    total = q ** length
    fibres = [0] * total
    fixed = 0
    maximum_tail = 0
    one_bad = 0
    digest = sha256()

    # The local filter is attacked from literal three-factor multiplication.
    for left in range(q):
        for right in range(q):
            expected = left if left and right == star(n, left) else 0
            AUDIT.equal(literal_local(n, left, right), expected,
                        f"local filter n={n} left={left} right={right}")

    for serial in range(total):
        source = unpack_word(serial, q, length)
        target = literal_step(n, source)
        target_serial = pack_word(target, q)
        fibres[target_serial] += 1
        fixed += int(target == source)
        digest.update(serial.to_bytes(8, "little"))
        digest.update(target_serial.to_bytes(8, "little"))

        state = source
        for time in range(0, 2 * length + 4):
            AUDIT.equal(state, predicted_iterate(n, source, time),
                        f"all-time n={n} m={length} t={time} source={serial}")
            state = literal_step(n, state)
        tail, period = orbit_signature(n, source)
        AUDIT.equal(period, 1, f"period n={n} m={length} source={serial}")
        AUDIT.equal(tail, predicted_tail(n, source),
                    f"tail n={n} m={length} source={serial}")
        maximum_tail = max(maximum_tail, tail)
        one_bad += int(edge_mask(n, source).bit_count() == length - 1)

    expected_fixed = 1 + (n if length % 2 else n * n)
    expected_height = (max(0, length - 1) if n == 1
                       else (length if length % 2 else length - 1))
    AUDIT.equal(fixed, expected_fixed, f"fixed census n={n} m={length}")
    AUDIT.equal(maximum_tail, expected_height,
                f"sharp height n={n} m={length}")
    if n >= 2 and length % 2 == 0:
        AUDIT.equal(one_bad, 0, f"even one-bad obstruction n={n} m={length}")
    if n >= 2 and length % 2 == 1 and length >= 3:
        AUDIT.true(one_bad > 0, f"odd one-bad witness n={n} m={length}")

    adjacency, zero_powers = zero_walk_tables(n, max(length, 2))
    matrices = target_matrices(n)
    predicted_mass = 0
    image_count = 0
    trace_all_targets = total <= 3125
    probe_serials = {0, total - 1, total // 2}
    for target_serial in range(total):
        target = unpack_word(target_serial, q, length)
        predicted = gap_formula(n, target, zero_powers)
        actual = fibres[target_serial]
        AUDIT.equal(predicted, actual,
                    f"gap product n={n} m={length} target={target_serial}")
        AUDIT.equal(actual > 0, image_criterion(n, target),
                    f"image iff n={n} m={length} target={target_serial}")
        if trace_all_targets or target_serial in probe_serials:
            AUDIT.equal(trace_formula(target, matrices), actual,
                        f"trace orientation n={n} m={length} target={target_serial}")
        predicted_mass += predicted
        image_count += int(actual > 0)
    AUDIT.equal(predicted_mass, total, f"fibre mass n={n} m={length}")
    AUDIT.equal(sum(fibres), total, f"literal mass n={n} m={length}")
    AUDIT.equal(fibres[0], recurrence_trace(n, length),
                f"zero fibre n={n} m={length}")

    # Boundary descriptions are target-by-target, not merely aggregate.
    if length == 1:
        AUDIT.equal(fibres[0], n * n - n + 1, f"m=1 zero boundary n={n}")
        for output in range(1, q):
            AUDIT.equal(fibres[output], int(output == star(n, output)),
                        f"m=1 labelled boundary n={n} y={output}")
    if length == 2:
        AUDIT.equal(fibres[0], q * q - n * n, f"m=2 zero boundary n={n}")
        for target_serial in range(1, total):
            target = unpack_word(target_serial, q, length)
            expected = int(target[0] and target[1] == star(n, target[0]))
            AUDIT.equal(fibres[target_serial], expected,
                        f"m=2 labelled boundary n={n} target={target_serial}")

    # Entry-level direction pressure: for an off-diagonal unit, M_y has its
    # one at row y, column y*, not at the reversed ordered pair.
    if n >= 2:
        off_diagonal = 2  # code for (0,1)
        inverse = star(n, off_diagonal)
        AUDIT.equal(matrices[off_diagonal][off_diagonal][inverse], 1,
                    f"matrix forward pin n={n} m={length}")
        AUDIT.equal(matrices[off_diagonal][inverse][off_diagonal], 0,
                    f"matrix reverse pin rejected n={n} m={length}")
        AUDIT.equal(adjacency[off_diagonal][inverse], 0,
                    f"A forbidden inverse successor n={n} m={length}")

    return (f"n={n} m={length} states={total} image={image_count} "
            f"fixed={fixed} max_tail={maximum_tail} zero_fibre={fibres[0]} "
            f"one_bad={one_bad} trace_all={str(trace_all_targets).lower()} "
            f"transition_sha256={digest.hexdigest()}")


def main() -> None:
    print("P190_PROCESS_SEPARATED_HOSTILE_REVIEW_A")
    print("representation=integer_base_q_words_plus_directed_walk_tables")
    print("author_code_imported=false")
    print("scope=finite_falsification_not_proof_not_novelty")
    pin_inputs()
    print("PINNED_INPUTS=PASS count=7")

    for n in range(1, 6):
        print("SPECTRUM " + spectral_attack(n))

    cases = (
        *((1, length) for length in range(1, 13)),
        *((2, length) for length in range(1, 8)),
        *((3, length) for length in range(1, 5)),
        *((4, length) for length in range(1, 4)),
        *((5, length) for length in range(1, 3)),
    )
    AUDIT.equal(len(cases), 28, "review box count")
    for n, length in cases:
        print("BOX " + verify_box(n, length))

    print("FORMAL_COUNTEREXAMPLES=0")
    print("CRITICAL=0")
    print("MAJOR=0")
    print("MINOR=0")
    print("FINDING_HISTORY=P190-A-MI-01_EQ11_LEADING_SUBSCRIPT_COMMA")
    print("FINDING_HISTORY=P190-A-MI-02_CREDIT_DOUBLE_FULL_STOP")
    print("DELTA=P190-A-MI-01_ACCEPTED")
    print("DELTA=P190-A-MI-02_ACCEPTED")
    print(f"BOXES={len(cases)}")
    print(f"ASSERTIONS={AUDIT.assertions}")
    print("OWNER=OWNER_AMBER")
    print("LIFECYCLE=HOLD_EXTERNAL")
    print("VERDICT=PASS_DELTA_ACCEPTED")


if __name__ == "__main__":
    main()
