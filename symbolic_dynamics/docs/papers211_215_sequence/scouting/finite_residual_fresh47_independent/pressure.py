"""Bounded independent counterexample search; not an all-size proof.

Scope is fixed: (q,N)=(1,8),(2,8),(3,7). Ordinary trusted Python execution.
No filesystem/network access by this program. Full output goes to stdout.
"""
from itertools import groupby, product
import json


def step(word):
    # Literal maximal-run update, independently implemented with groupby.
    return tuple(letter for letter, block in groupby(word)
                 if sum(1 for _ in block) % 2)


def walk(word):
    vertices = [()]
    for letter in word:
        vertex = vertices[-1]
        vertices.append(vertex[:-1] if vertex and vertex[-1] == letter
                        else vertex + (letter,))
    return vertices


def tree_distance(left, right):
    common = 0
    while common < min(len(left), len(right)):
        if left[common] != right[common]:
            break
        common += 1
    return len(left) + len(right) - 2 * common


def statistic(word):
    vertices = walk(word)
    endpoint = vertices[-1]
    maximum = max(len(vertices[i]) + tree_distance(vertices[j], endpoint)
                  for i in range(len(vertices))
                  for j in range(i, len(vertices)))
    return maximum, len(endpoint)


def require(condition, kind, q, word, details):
    if not condition:
        print(json.dumps({'finding': kind, 'q': q, 'word': word,
                          'details': details}, sort_keys=True))
        raise SystemExit(1)


def check(q, cutoff):
    tested = transitions = checks = conditional = 0
    worst = 0
    for n in range(cutoff + 1):
        for word in product(range(q), repeat=n):
            tested += 1
            current = word
            history = [word]
            while True:
                following = step(current)
                if following == current:
                    break
                require(len(following) <= len(current) - 2,
                        'strict_length', q, word, [current, following])
                current = following
                history.append(current)
            actual = len(history) - 1
            worst = max(worst, actual)
            maximum, endpoint_length = statistic(word)
            predicted = (maximum - endpoint_length + 1) // 2
            require(actual == predicted, 'clock', q, word,
                    [actual, predicted, maximum, endpoint_length, history])
            require(current == walk(word)[-1], 'normal_form', q, word,
                    [current, walk(word)[-1]])
            checks += 2
            for before in history:
                after = step(before)
                old, m = statistic(before)
                new, m_next = statistic(after)
                require(m == m_next, 'endpoint_length', q, word,
                        [before, after, m, m_next])
                require(new >= old - 2, 'first_inequality', q, word,
                        [before, after, old, new])
                require((old == m) == (before == after),
                        'detection', q, word, [before, after, old, m])
                checks += 3
                transitions += 1
                if new > m:
                    require(old >= new + 2, 'second_inequality', q, word,
                            [before, after, old, new, m])
                    checks += 1
                    conditional += 1
    return {'q': q, 'cutoff': cutoff, 'sources': tested,
            'orbit_steps_including_terminal': transitions,
            'conditional_second_inequality_checks': conditional,
            'checks': checks, 'worst_observed_clock': worst,
            'findings': 0}


def main():
    for q, cutoff in ((1, 8), (2, 8), (3, 7)):
        print(json.dumps(check(q, cutoff), sort_keys=True))
    print(json.dumps({'scope': 'bounded clock and schedule inequalities only',
                      'all_parameter_proof': False,
                      'inverse_fibres_tested': False}, sort_keys=True))


if __name__ == '__main__':
    main()
