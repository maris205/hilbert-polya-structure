#!/usr/bin/env python3
"""Deterministic exact verifier for P138.

The exhaustive lane builds every functional graph through length 18.  It also
checks the normalized target decoder against literal one-step fibres through
length 15 and checks the closed sharp family through length 64.  Computation is
counterexample pressure; the all-length arguments are in main.tex.
"""

from collections import Counter


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def bits(value, n):
    return tuple((value >> (n - 1 - i)) & 1 for i in range(n))


def integer(word):
    value = 0
    for bit in word:
        value = 2 * value + bit
    return value


def literal_word_step(word):
    out = []
    for i, bit in enumerate(word):
        prefix = word[: i + 1]
        out.append(bit ^ (prefix == prefix[::-1]))
    return tuple(out)


def step(value, n):
    return integer(literal_word_step(bits(value, n)))


def normalize(word):
    return tuple(bit ^ word[0] for bit in word)


def quotient_step(word):
    check(word[0] == 0, "quotient input is not normalized")
    out = []
    for i, bit in enumerate(word):
        prefix = word[: i + 1]
        out.append(bit ^ 1 ^ (prefix == prefix[::-1]))
    check(out[0] == 0, "quotient output is not normalized")
    return tuple(out)


def leading_zeros(word):
    count = 0
    for bit in word:
        if bit:
            break
        count += 1
    return count


def decoder_count(target):
    """Count the original fibre via the frozen normalized decoder.

    The first bit of the original source is forced by the target phase, so the
    normalized recursion introduces no factor of two.
    """
    normalized_target = normalize(target)
    prefixes = [(0,)]
    for i in range(1, len(target)):
        new_prefixes = []
        for prefix in prefixes:
            middle = prefix[1:i]
            if middle != middle[::-1]:
                new_prefixes.append(prefix + (1 - normalized_target[i],))
            elif normalized_target[i] == 0:
                new_prefixes.append(prefix + (0,))
                new_prefixes.append(prefix + (1,))
        prefixes = new_prefixes
    return len(prefixes)


def classify(n):
    size = 1 << n
    nxt = [step(state, n) for state in range(size)]
    info = {}
    cycles = Counter()
    for start in range(size):
        if start in info:
            continue
        path = []
        position = {}
        state = start
        while state not in position and state not in info:
            position[state] = len(path)
            path.append(state)
            state = nxt[state]
        if state in position:
            split = position[state]
            period = len(path) - split
            cycles[period] += 1
            for i, vertex in enumerate(path):
                info[vertex] = (max(split - i, 0), period)
        else:
            old_tail, period = info[state]
            for i, vertex in enumerate(path):
                info[vertex] = (len(path) - i + old_tail, period)
    return nxt, info, cycles


def expected_max_tail(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return n - 2


def sharp_witness(n):
    return tuple(int(i % 4 == 3) for i in range(1, n + 1))


def quotient_tail(word):
    zero = (0,) * len(word)
    tail = 0
    while word != zero:
        word = quotient_step(word)
        tail += 1
        if tail > len(word) + 2:
            raise AssertionError("quotient orbit did not synchronize")
    return tail


def main():
    total_states = 0
    image_profile = []
    fibre_profile = []

    for n in range(1, 19):
        size = 1 << n
        total_states += size
        mask = size - 1
        nxt, info, cycles = classify(n)
        fibres = Counter(nxt)

        for state in range(size):
            word = bits(state, n)
            normalized = normalize(word)
            normalized_image = normalize(bits(nxt[state], n))
            check(nxt[state ^ mask] == (nxt[state] ^ mask),
                  "complement equivariance failed")
            check(normalized_image == quotient_step(normalized),
                  "literal/quotient conjugacy failed")
            check(info[state][1] == 2, "unexpected period")
            check(info[state][0] <= expected_max_tail(n), "tail bound failed")
            if n >= 3:
                check(leading_zeros(normalized_image) >= 3,
                      "three-coordinate reset failed")
            run = leading_zeros(normalized)
            if 3 <= run < n:
                check(leading_zeros(normalized_image) >= run + 1,
                      "zero-prefix amplifier failed")

        if n <= 15:
            for target in range(size):
                check(decoder_count(bits(target, n)) == fibres[target],
                      "decoder/literal fibre mismatch")

        max_tail = max(tail for tail, _ in info.values())
        recurrent = {state for state, (tail, _) in info.items() if tail == 0}
        check(max_tail == expected_max_tail(n), "sharp clock failed")
        check(recurrent == {0, mask}, "recurrent atlas failed")
        check(cycles == Counter({2: 1}), "cycle census failed")
        if n >= 3:
            check(quotient_tail(sharp_witness(n)) == n - 2,
                  "closed sharp family failed")

        image_profile.append(len(fibres))
        fibre_profile.append(max(fibres.values()))
        print(
            f"n={n:2d} states={size:6d} image={len(fibres):6d} "
            f"cycles={dict(cycles)} max_tail={max_tail:2d} "
            f"max_fibre={max(fibres.values()):3d}"
        )

    for n in range(19, 65):
        check(quotient_tail(sharp_witness(n)) == n - 2,
              "extended sharp-family check failed")

    print("IMAGE_PROFILE=" + ",".join(map(str, image_profile)))
    print("MAX_FIBRE_PROFILE=" + ",".join(map(str, fibre_profile)))
    print(f"TOTAL_EXHAUSTIVE_STATES={total_states}")
    print("DECODER_EXHAUSTIVE_THROUGH=15")
    print("SHARP_FAMILY_CHECKED_THROUGH=64")
    print(f"EXACT_ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
