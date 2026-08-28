#!/usr/bin/env python3
"""Deterministic controls for the Bernoulli-reset golden random SFT.

The discrete checks use only Python integers and ``fractions.Fraction``.
Floating-point evaluations are printed separately as diagnostics and are not
used to certify an identity.  No third-party package is required.
"""

from fractions import Fraction
from itertools import product
import math


A = ((1, 1), (1, 0))
E = ((1, 1), (0, 0))
I = ((1, 0), (0, 1))
ONES = (1, 1)

ASSERTIONS = 0
DIAGNOSTIC_CHECKS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def diagnostic_check(condition, message):
    global DIAGNOSTIC_CHECKS
    DIAGNOSTIC_CHECKS += 1
    if not condition:
        raise AssertionError(message)


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2))
              for j in range(2))
        for i in range(2)
    )


def matpow(matrix, exponent):
    answer = I
    base = matrix
    while exponent:
        if exponent & 1:
            answer = matmul(answer, base)
        base = matmul(base, base)
        exponent //= 2
    return answer


def sandwich(left, matrix, right):
    return sum(left[i] * matrix[i][j] * right[j]
               for i in range(2) for j in range(2))


def scalar_times(scalar, matrix):
    return tuple(tuple(scalar * entry for entry in row) for row in matrix)


def fibonacci(maximum):
    values = [0, 1]
    while len(values) <= maximum:
        values.append(values[-1] + values[-2])
    return values


def matrix_word(environment):
    answer = I
    for reset in environment:
        answer = matmul(answer, E if reset else A)
    return answer


def matrix_path_count(environment):
    return sandwich(ONES, matrix_word(environment), ONES)


def direct_path_count(environment):
    """Independent definition-level enumeration of allowed state paths."""
    count = 0
    for path in product((0, 1), repeat=len(environment) + 1):
        legal = True
        for i, reset in enumerate(environment):
            matrix = E if reset else A
            if matrix[path[i]][path[i + 1]] == 0:
                legal = False
                break
        count += int(legal)
    return count


def renewal_factor_count(environment, fib):
    """Count after collapsing every internal E A^k E sandwich."""
    reset_positions = [i for i, symbol in enumerate(environment) if symbol]
    n = len(environment)
    if not reset_positions:
        return sandwich(ONES, matpow(A, n), ONES)

    left = reset_positions[0]
    right = n - 1 - reset_positions[-1]
    factor = 1
    for first, second in zip(reset_positions, reset_positions[1:]):
        gap = second - first - 1
        factor *= fib[gap + 2]
    boundary = matmul(matmul(matpow(A, left), E), matpow(A, right))
    return factor * sandwich(ONES, boundary, ONES)


def weighted_environment_ledgers(maximum, p):
    """Enumerate the full binary environment tree once, exactly."""
    reset_free = 1 - p
    masses = [Fraction(0) for _ in range(maximum + 1)]
    counts = [Fraction(0) for _ in range(maximum + 1)]

    def visit(depth, matrix, weight):
        masses[depth] += weight
        counts[depth] += weight * sandwich(ONES, matrix, ONES)
        if depth == maximum:
            return
        visit(depth + 1, matmul(matrix, A), weight * reset_free)
        visit(depth + 1, matmul(matrix, E), weight * p)

    visit(0, I, Fraction(1))
    return masses, counts


def expected_matrix(n, p):
    reset_free = 1 - p
    mean = tuple(
        tuple(reset_free * A[i][j] + p * E[i][j] for j in range(2))
        for i in range(2)
    )
    return sandwich(ONES, matpow(mean, n), ONES)


def check_fibonacci_identities():
    fib = fibonacci(55)
    for k in range(51):
        actual = matmul(matmul(E, matpow(A, k)), E)
        check(actual == scalar_times(fib[k + 2], E),
              f"failed E A^{k} E identity")

    for k in range(1, 51):
        claimed = ((fib[k + 1], fib[k]), (fib[k], fib[k - 1]))
        check(matpow(A, k) == claimed, f"failed A^{k} Fibonacci form")
    return fib


def check_definition_level_paths(maximum=9):
    for n in range(maximum + 1):
        for environment in product((0, 1), repeat=n):
            check(matrix_path_count(environment) == direct_path_count(environment),
                  f"path-count mismatch for {environment}")


def check_renewal_factorization(fib, maximum=15):
    for n in range(maximum + 1):
        for environment in product((0, 1), repeat=n):
            check(matrix_path_count(environment)
                  == renewal_factor_count(environment, fib),
                  f"renewal factorization mismatch for {environment}")


def check_annealed_identity(maximum=16):
    for p in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
        masses, enumerated_counts = weighted_environment_ledgers(maximum, p)
        for n in range(maximum + 1):
            check(masses[n] == 1,
                  f"environment mass mismatch for p={p}, n={n}")
            check(enumerated_counts[n] == expected_matrix(n, p),
                  f"annealed matrix identity mismatch for p={p}, n={n}")


def check_renewal_algebra():
    """Exact rational reductions behind the strict Jensen argument."""
    for p in (Fraction(1, 17), Fraction(1, 5), Fraction(1, 2),
              Fraction(4, 5), Fraction(16, 17)):
        r = 1 - p

        # K has mass p r^k and L=K+1.  These are generating-function
        # evaluations, represented entirely in Q.
        mass = p / (1 - r)
        mean_length = p / (1 - r) ** 2
        second_length = p * (1 + r) / (1 - r) ** 3
        check(mass == 1, f"geometric mass mismatch for p={p}")
        check(mean_length == 1 / p, f"mean cycle length mismatch for p={p}")
        check(second_length == (1 + r) / p ** 2,
              f"second cycle moment mismatch for p={p}")

        # Let lambda^2=lambda+r.  The equality E[Z]=1 for
        # Z=F_{K+2}/lambda^{K+1} reduces to
        # lambda^2-r lambda-r^2 = p(lambda+r).  Reduce both sides modulo
        # lambda^2-lambda-r and compare the rational coefficients of
        # lambda and 1.
        lambda_coefficient = 1 - r - p
        constant_coefficient = r - r * r - p * r
        check(lambda_coefficient == 0 and constant_coefficient == 0,
              f"cycle normalization reduction failed for p={p}")

        # Z is nonconstant: equality of its k=0 and k=1 values would force
        # lambda=2, incompatible with lambda^2=lambda+r for 0<r<1.
        check(Fraction(4) - Fraction(2) - r != 0,
              f"strictness witness unexpectedly vanished for p={p}")


def entropy_and_variance(p, terms=20000):
    r = 1.0 - p
    # Update log Fibonacci without ever converting a huge integer to float.
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    log_sqrt5 = 0.5 * math.log(5.0)

    def log_fibonacci(index):
        # Binet: F_n=(phi^n/sqrt(5))*(1-(-phi^{-2})^n).
        correction = math.log1p(-((-1.0 / (phi * phi)) ** index))
        return index * math.log(phi) - log_sqrt5 + correction

    hq = 0.0
    raw = []
    probability = p
    for k in range(terms):
        reward = log_fibonacci(k + 2)
        hq += p * probability * reward
        raw.append((probability, k + 1, reward))
        probability *= r
        if probability < 1e-18:
            break

    variance = p * sum(probability_k * (reward - hq * length) ** 2
                       for probability_k, length, reward in raw)
    annealed = math.log((1.0 + math.sqrt(5.0 - 4.0 * p)) / 2.0)
    return hq, annealed, variance, len(raw)


def check_numeric_diagnostics():
    rows = []
    for p in (0.1, 0.25, 0.5, 0.75, 0.9):
        quenched, annealed, variance, terms = entropy_and_variance(p)
        diagnostic_check(0.0 < quenched < annealed,
                         f"numeric gap failed for p={p}")
        diagnostic_check(variance > 0.0,
                         f"numeric variance failed for p={p}")
        rows.append((p, quenched, annealed, variance, terms))
    return rows


def main():
    print("Bernoulli-reset golden random-SFT controls")
    fib = check_fibonacci_identities()
    check_definition_level_paths()
    check_renewal_factorization(fib)
    check_annealed_identity()
    check_renewal_algebra()
    diagnostics = check_numeric_diagnostics()

    totals = []
    for n in range(1, 9):
        totals.append(sum(matrix_path_count(environment)
                          for environment in product((0, 1), repeat=n)))
    expected_totals = [5, 14, 38, 104, 284, 776, 2120, 5792]
    check(totals == expected_totals, "uniform environment ledger mismatch")

    print(f"E A^k E = F_(k+2) E checked for 0 <= k <= 50")
    print(f"definition-level paths checked for 0 <= n <= 9")
    print(f"renewal factorization checked for 0 <= n <= 15")
    print(f"annealed identity checked at 3 rational p values for 0 <= n <= 16")
    print(f"sum_environment N_n for n=1..8: {totals}")
    for p, quenched, annealed, variance, terms in diagnostics:
        print(f"p={p:.2f}: h_q={quenched:.15f}, h_a={annealed:.15f}, "
              f"sigma^2={variance:.15f}, terms={terms}")
    print(f"ALL DISCRETE EXACT CONTROLS PASSED ({ASSERTIONS:,} assertions; "
          f"{DIAGNOSTIC_CHECKS} floating diagnostics)")


if __name__ == "__main__":
    main()
