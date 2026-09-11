#!/usr/bin/env python3
"""Pre-Round0 pressure only: not a paper reviewer canonical verifier."""
from collections import Counter
from itertools import permutations, product

checks = 0


def check(value):
    global checks
    checks += 1
    assert value, checks


def difference(word):
    return tuple((b > a) - (b < a) for a, b in zip(word, word[1:] + word[:1]))


def open_difference(word):
    return tuple((b > a) - (b < a) for a, b in zip(word, word[1:]))


def iterate(word, count, transform=difference):
    for _ in range(count):
        word = transform(word)
    return word


def tail_period(word):
    seen = {}
    while word not in seen:
        seen[word] = len(seen)
        word = difference(word)
    return seen[word], len(seen) - seen[word]


def planes(word):
    return (sum(1 << i for i, a in enumerate(word) if a < 0),
            sum(1 << i for i, a in enumerate(word) if a > 0))


def bit_update(pair, n):
    low, high = pair
    mask = (1 << n) - 1
    zeros = mask ^ (low | high)
    low_next = (low >> 1) | ((low & 1) << (n - 1))
    high_next = (high >> 1) | ((high & 1) << (n - 1))
    return ((high & (mask ^ high_next)) | (zeros & low_next),
            (low & (mask ^ low_next)) | (zeros & high_next))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def gap_count(word):
    signs = tuple(a for a in word if a)
    if not signs:
        return 3
    if len(set(signs)) == 1:
        return 0
    cut = next(i for i in range(len(signs)) if signs[i] != signs[i - 1])
    signs = signs[cut:] + signs[:cut]
    runs = [1]
    for a, b in zip(signs, signs[1:]):
        if a == b:
            runs[-1] += 1
        else:
            runs.append(1)
    if max(runs) >= 3:
        return 0
    doubled = [i for i, length in enumerate(runs) if length == 2]
    if not doubled:
        return fib(len(signs) - 1) + fib(len(signs) + 1)
    answer = 1
    for i, j in zip(doubled, doubled[1:] + [doubled[0] + len(runs)]):
        answer *= fib(j - i)
    return answer


def main():
    local_counts = []
    for n, forbidden, power, center in ((6, 2, 5, (2, 4)), (7, 3, 6, (2, 5))):
        count = 0
        for word in product((-1, 0, 1), repeat=n):
            if any(len(set(word[i:i + forbidden])) == 1 for i in range(n - forbidden + 1)):
                continue
            check(iterate(word, power, open_difference)[0] ==
                  iterate(word[center[0]:center[1]], center[1] - center[0] - 1, open_difference)[0])
            count += 1
        local_counts.append(count)
    check(local_counts == [96, 1344])
    print('local_certificate_counts=', local_counts)
    witnesses = 0
    for r in range(1, 25):
        for length in range(2, 25):
            for sign in (-1, 1):
                word = (0,) * r + tuple(sign * (-1) ** i for i in range(length))
                n = len(word)
                target = (0,) * (r - 1) + tuple(sign * (-1) ** i for i in range(length + 1))
                check(difference(word) == target)
                d4 = iterate(word, 4)
                shift = word[2:] + word[:2]
                check((d4 == shift) == (r == 1 and length % 2 == 0))
                if r >= 4:
                    index = r - 4
                    check(d4[index] == sign and shift[index] == 0)
                elif r == 3:
                    check(d4[0] == -sign and shift[0] == 0)
                elif r == 2 or (r == 1 and n % 2 == 0):
                    check(d4[n - 2] != 0 and shift[n - 2] == 0)
                witnesses += 1
    print('junction_cases=', witnesses)
    for n in range(2, 9):
        boundary = []
        for a, b in permutations((-1, 0, 1), 2):
            tau, period = tail_period((a,) * (n - 1) + (b,))
            expected = (0 if abs(a - b) == 2 else 1) if n <= 3 else n - 1 - n % 2
            check(tau == expected)
            boundary.append((a, b, tau))
        check(tail_period((0,) * (n - 1) + (1,))[0] == n - 1 - n % 2)
        print(f'one_exception n={n} (a,b,tail)={boundary}')
    for n in range(1, 9):
        fibres = Counter()
        for word in product((-1, 0, 1), repeat=n):
            image = difference(word)
            check(planes(image) == bit_update(planes(word), n))
            fibres[image] += 1
        for target in product((-1, 0, 1), repeat=n):
            check(fibres[target] == gap_count(target))
        print(f'gap_and_bitplanes n={n} states={3**n} image={len(fibres)} max_fibre={max(fibres.values())}')
    encoded = tuple(tuple((b > a) - (b < a) + 1 for b in range(3)) for a in range(3))
    triples = tuple(product(range(3), repeat=3))
    hits, count = 0, 0
    for left, right, out in product(tuple(permutations(range(3))), repeat=3):
        op = tuple(tuple(out[encoded[left[a]][right[b]]] for b in range(3)) for a in range(3))
        associative = all(op[op[a][b]][c] == op[a][op[b][c]] for a, b, c in triples)
        check(not associative)
        hits += associative
        count += 1
    print(f'local_operation_isotopy assignments={count} associative_hits={hits}')
    check(gap_count((1, 1, -1, -1)) == 1)
    check(fib(1) * fib(1) == fib(1 + 1 - 1))
    print('old_each_merge_strict_counterexample=++-- with F1*F1=F1=1')
    print(f'ASSERTIONS={checks}')
    print('PREPARATION_ONLY / NOT_REVIEW_A / HOLD_EXTERNAL')


if __name__ == '__main__':
    main()
