"""Bounded exact check frozen in SCOUT_REPORT.md; not a density proof."""

from fractions import Fraction
import json


def primes_up_to(limit):
    return [n for n in range(3, limit + 1, 2)
            if all(n % d for d in range(2, int(n ** 0.5) + 1))]


def v2(n):
    assert n > 0
    exponent = 0
    while n % 2 == 0:
        exponent += 1
        n //= 2
    return exponent


def elliptic_order(p, parameter):
    squares = {y * y % p for y in range(1, p)}
    total = 1
    for x in range(p):
        rhs = (x * x * x - parameter * x) % p
        total += 1 if rhs == 0 else (2 if rhs in squares else 0)
    return total


def periodic_count(p, parameter):
    # Infinity is encoded by p. All points of P^1, including poles, are kept.
    function = []
    for x in range(p):
        denominator = 4 * x * (x * x - parameter) % p
        numerator = (x * x + parameter) ** 2 % p
        assert denominator or numerator  # no base point at a good odd prime
        function.append(numerator * pow(denominator, -1, p) % p
                        if denominator else p)
    function.append(p)
    indegree = [0] * (p + 1)
    for value in function:
        indegree[value] += 1
    queue = [x for x, degree in enumerate(indegree) if degree == 0]
    for x in queue:
        value = function[x]
        indegree[value] -= 1
        if indegree[value] == 0:
            queue.append(value)
    return sum(degree != 0 for degree in indegree)


def run():
    parameters = [-8, -7, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 7, 8]
    primes = primes_up_to(101)
    checks = dict(graph_formula=0, inert_trace=0, split_residue=0,
                  split_nonresidue=0, base_valuation=0)
    failures = []
    base_counts = {}
    total_domain_points = 0
    for p in primes:
        base_counts[p] = periodic_count(p, 1)
        base_order = elliptic_order(p, 1)
        if p % 4 == 1:
            a, b = sorted([v2(base_order), v2(2 * (p + 1) - base_order)])
            checks['base_valuation'] += 1
            if not (a == 2 and b >= 3 and ((b == 3) == (p % 8 == 5))):
                failures.append(['base_valuation', p, a, b])
        for parameter in parameters:
            if parameter % p == 0:
                continue
            total_domain_points += p + 1
            size = elliptic_order(p, parameter)
            twist_size = 2 * (p + 1) - size
            count = periodic_count(p, parameter)
            predicted = Fraction((size >> v2(size)) +
                                 (twist_size >> v2(twist_size)), 2)
            checks['graph_formula'] += 1
            if count != predicted:
                failures.append(['graph_formula', p, parameter, count,
                                 str(predicted)])
            if p % 4 == 3:
                checks['inert_trace'] += 1
                if size != p + 1:
                    failures.append(['inert_trace', p, parameter, size])
            elif pow(parameter, (p - 1) // 2, p) == 1:
                checks['split_residue'] += 1
                if count != base_counts[p]:
                    failures.append(['split_residue', p, parameter, count,
                                     base_counts[p]])
            else:
                checks['split_nonresidue'] += 1
                if 2 * count != p + 1:
                    failures.append(['split_nonresidue', p, parameter, count])
    return dict(status='PASS' if not failures else 'FAIL',
                scope='finite exact convention check; not an asymptotic proof',
                prime_max=101, primes=primes, parameters=parameters,
                domain='P1(Fp), infinity and poles included, p odd and p not dividing D',
                total_domain_points=total_domain_points,
                checks=checks, failures=failures)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
