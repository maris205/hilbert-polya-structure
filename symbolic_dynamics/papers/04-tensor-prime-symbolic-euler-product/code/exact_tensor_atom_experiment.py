#!/usr/bin/env python3
"""Exact finite-registry test for the tensor-atomic full-shift hypothesis.

The recovery algorithm is deliberately given opaque object IDs.  It may read
only the registered unit, tensor table, entropy, and reciprocal Artin--Mazur
determinant D_X(z)=1-w(X)z.  It never calls the verifier's primality predicate.

The primality predicate below is used only *after* recovery, to score the
opaque output.  There is no stored prime table and no Riemann-zero data.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import statistics
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable


@dataclass(frozen=True)
class RegistrySpec:
    name: str
    labels: tuple[int, ...]
    unit_label: int
    operation: Callable[[int, int], int]


def stable_token(name: str, label: int) -> str:
    digest = hashlib.sha256(f"{name}:{label}".encode()).hexdigest()[:12]
    return f"obj_{digest}"


def build_public_registry(spec: RegistrySpec) -> tuple[dict, dict[str, int]]:
    """Return public opaque data and a private token->label scoring map."""
    token_of = {n: stable_token(spec.name, n) for n in spec.labels}
    private = {token: n for n, token in token_of.items()}
    label_set = set(spec.labels)
    objects = []
    for n in spec.labels:
        # Full n-shift: #Fix(sigma^r)=n^r and D_n(z)=1-nz.
        entropy = None if n == 0 else math.log(n)
        objects.append(
            {
                "id": token_of[n],
                "entropy": entropy,
                "am_reciprocal_determinant_coefficients": [1, -n],
                "fixed_point_counts_r1_to_r4": [n**r for r in range(1, 5)],
            }
        )
    products = []
    for a in spec.labels:
        for b in spec.labels:
            c = spec.operation(a, b)
            if c in label_set:
                products.append([token_of[a], token_of[b], token_of[c]])
    public = {
        "registry": spec.name,
        "object_ids_are_opaque": True,
        "allowed_fields": [
            "unit",
            "operation_table",
            "entropy",
            "am_reciprocal_determinant_coefficients",
            "fixed_point_counts",
        ],
        "forbidden_fields": ["integer_label", "prime_table", "Riemann_zero_table"],
        "unit": token_of[spec.unit_label],
        "objects": objects,
        "operation_table": products,
    }
    return public, private


def recover_from_registered_data(public: dict) -> dict:
    """Candidate-side recovery: no label map and no primality predicate."""
    unit = public["unit"]
    ids = [obj["id"] for obj in public["objects"]]
    by_id = {obj["id"]: obj for obj in public["objects"]}
    product = {(a, b): c for a, b, c in public["operation_table"]}
    decompositions: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for (a, b), c in product.items():
        if a != unit and b != unit:
            decompositions[c].append((a, b))
    atoms = sorted(x for x in ids if x != unit and not decompositions[x])

    # This integer is read from a symbolic invariant, not from an object label.
    weights = {
        x: -int(by_id[x]["am_reciprocal_determinant_coefficients"][1])
        for x in ids
    }
    entropies = {x: by_id[x]["entropy"] for x in ids}

    # Factorizations are computed from the operation table alone.
    memo: dict[str, set[tuple[str, ...]]] = {}
    visiting: set[str] = set()

    def canonical(parts: Iterable[str]) -> tuple[str, ...]:
        return tuple(sorted(parts))

    def factorizations(x: str) -> set[tuple[str, ...]]:
        if x == unit:
            return {()}
        if x in memo:
            return memo[x]
        if x in visiting:
            return set()
        if x in atoms:
            memo[x] = {(x,)}
            return memo[x]
        visiting.add(x)
        found: set[tuple[str, ...]] = set()
        for a, b in decompositions[x]:
            for fa in factorizations(a):
                for fb in factorizations(b):
                    found.add(canonical(fa + fb))
        visiting.remove(x)
        memo[x] = found
        return found

    factor_sets = {x: factorizations(x) for x in ids}
    entropy_weight_errors = []
    for x in ids:
        h = entropies[x]
        w = weights[x]
        if h is not None and w > 0:
            entropy_weight_errors.append(abs(math.exp(h) - w))

    operation_entropy_errors = []
    operation_weight_ok = []
    fixed_point_tensor_ok = []
    for (a, b), c in product.items():
        ha, hb, hc = entropies[a], entropies[b], entropies[c]
        if ha is not None and hb is not None and hc is not None:
            operation_entropy_errors.append(abs(hc - ha - hb))
        operation_weight_ok.append(weights[c] == weights[a] * weights[b])
        fpa = by_id[a]["fixed_point_counts_r1_to_r4"]
        fpb = by_id[b]["fixed_point_counts_r1_to_r4"]
        fpc = by_id[c]["fixed_point_counts_r1_to_r4"]
        fixed_point_tensor_ok.append(all(x * y == z for x, y, z in zip(fpa, fpb, fpc)))

    return {
        "unit": unit,
        "atoms": atoms,
        "atom_weights": sorted(weights[x] for x in atoms),
        "weights": weights,
        "factorizations": {
            x: [list(f) for f in sorted(factor_sets[x])] for x in ids
        },
        "unique_factorization_fraction": sum(len(factor_sets[x]) == 1 for x in ids) / len(ids),
        "unfactorable_nonatom_count": sum(
            x != unit and x not in atoms and len(factor_sets[x]) == 0 for x in ids
        ),
        "max_entropy_vs_determinant_weight_error": max(entropy_weight_errors, default=0.0),
        "max_operation_entropy_additivity_error": max(operation_entropy_errors, default=0.0),
        "operation_weight_multiplicativity_fraction": (
            sum(operation_weight_ok) / len(operation_weight_ok) if operation_weight_ok else 0.0
        ),
        "fixed_point_tensor_identity_fraction": (
            sum(fixed_point_tensor_ok) / len(fixed_point_tensor_ok)
            if fixed_point_tensor_ok
            else 0.0
        ),
    }


def euler_coefficients(atom_weights: Iterable[int], cutoff: int) -> list[int]:
    """Coefficients of prod_a (1-a^{-s})^{-1}, indexed by integer mass."""
    coeff = [0] * (cutoff + 1)
    coeff[1] = 1
    for a in sorted(atom_weights):
        if a <= 1:
            raise ValueError("Euler factor has zero/nonpositive entropy clock")
        old = coeff
        new = [0] * (cutoff + 1)
        for n in range(1, cutoff + 1):
            if old[n] == 0:
                continue
            power = 1
            while n * power <= cutoff:
                new[n * power] += old[n]
                power *= a
        coeff = new
    return coeff


def inverse_euler_coefficients(atom_weights: Iterable[int], cutoff: int) -> list[int]:
    """Coefficients of prod_a (1-a^{-s})."""
    coeff = [0] * (cutoff + 1)
    coeff[1] = 1
    for a in sorted(atom_weights):
        if a <= 1:
            raise ValueError("Euler factor has zero/nonpositive entropy clock")
        old = coeff
        new = old.copy()
        for n in range(1, cutoff + 1):
            if old[n] and n * a <= cutoff:
                new[n * a] -= old[n]
        coeff = new
    return coeff


def log_derivative_coefficients(atom_weights: Iterable[int], cutoff: int) -> list[float]:
    """Coefficients of -Z'/Z = sum_a sum_r log(a) a^{-rs}."""
    coeff = [0.0] * (cutoff + 1)
    for a in sorted(atom_weights):
        if a <= 1:
            raise ValueError("Euler factor has zero/nonpositive entropy clock")
        q = a
        while q <= cutoff:
            coeff[q] += math.log(a)
            q *= a
    return coeff


def free_word_coefficients(symbol_weights: Iterable[int], cutoff: int) -> list[int]:
    """Coefficients of 1/(1-sum_a a^{-s}), i.e. ordered mixed words."""
    weights = sorted(symbol_weights)
    coeff = [0] * (cutoff + 1)
    coeff[1] = 1
    for n in range(2, cutoff + 1):
        coeff[n] = sum(coeff[n // a] for a in weights if n % a == 0)
    return coeff


def free_word_log_derivative_coefficients(
    symbol_weights: Iterable[int], cutoff: int
) -> list[float]:
    """Coefficients of -d/ds log(1-sum_a a^{-s})^{-1}."""
    weights = sorted(symbol_weights)
    words = free_word_coefficients(weights, cutoff)
    coeff = [0.0] * (cutoff + 1)
    # (sum log(a)a^-s)/(1-sum a^-s): choose the differentiated first
    # letter, followed by an arbitrary ordered word.
    for n in range(1, cutoff + 1):
        coeff[n] = sum(
            math.log(a) * words[n // a] for a in weights if n % a == 0
        )
    return coeff


def is_prime_for_scoring_only(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_factorization_for_scoring_only(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def mobius_for_scoring_only(n: int) -> int:
    if n == 1:
        return 1
    factors = prime_factorization_for_scoring_only(n)
    if any(power > 1 for power in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def von_mangoldt_for_scoring_only(n: int) -> float:
    if n <= 1:
        return 0.0
    factors = prime_factorization_for_scoring_only(n)
    if len(factors) != 1:
        return 0.0
    return math.log(next(iter(factors)))


def exact_fraction(a: list[int], b: list[int], start: int = 1) -> float:
    return sum(x == y for x, y in zip(a[start:], b[start:])) / (len(a) - start)


def lambda_relative_l1(a: list[float], b: list[float]) -> float:
    numerator = sum(abs(x - y) for x, y in zip(a[1:], b[1:]))
    denominator = sum(abs(x) for x in b[1:])
    return numerator / denominator if denominator else 0.0


def set_jaccard(a: set[int], b: set[int]) -> float:
    union = a | b
    return len(a & b) / len(union) if union else 1.0


def summarize_random(rows: list[dict], n: int) -> dict:
    selected = [row for row in rows if row["N"] == n]
    keys = [
        "declared_vs_intrinsic_atom_jaccard",
        "zeta_coefficient_accuracy",
        "inverse_coefficient_accuracy",
        "lambda_relative_l1_error",
    ]
    summary = {"N": n, "seeds": len(selected)}
    for key in keys:
        values = [float(row[key]) for row in selected]
        summary[f"{key}_mean"] = statistics.fmean(values)
        summary[f"{key}_std"] = statistics.pstdev(values)
        summary[f"{key}_min"] = min(values)
        summary[f"{key}_max"] = max(values)
    return summary


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0].keys()), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("results"))
    parser.add_argument("--cutoffs", default="32,64,128,256")
    parser.add_argument("--random-seeds", type=int, default=64)
    parser.add_argument(
        "--save-registries",
        action="store_true",
        help="persist large opaque input registries (off by default)",
    )
    args = parser.parse_args()
    cutoffs = [int(x) for x in args.cutoffs.split(",")]
    out = args.output
    out.mkdir(parents=True, exist_ok=True)
    if args.save_registries:
        (out / "registries").mkdir(exist_ok=True)

    main_rows: list[dict] = []
    random_rows: list[dict] = []
    shifted_rows: list[dict] = []
    additive_rows: list[dict] = []
    no_mixing_rows: list[dict] = []

    for nmax in cutoffs:
        main_spec = RegistrySpec(
            name=f"tensor_product_N{nmax}",
            labels=tuple(range(1, nmax + 1)),
            unit_label=1,
            operation=lambda a, b: a * b,
        )
        main_public, _ = build_public_registry(main_spec)
        recovered = recover_from_registered_data(main_public)
        atoms = recovered["atom_weights"]
        zeta = euler_coefficients(atoms, nmax)
        inverse = inverse_euler_coefficients(atoms, nmax)
        lam = log_derivative_coefficients(atoms, nmax)
        # The exact target is generated by the candidate's own recovered atoms.
        # Its expected closed form is checked independently below.
        prime_check_fraction = sum(is_prime_for_scoring_only(a) for a in atoms) / len(atoms)
        expected_prime_count = sum(is_prime_for_scoring_only(k) for k in range(2, nmax + 1))
        mobius_reference = [0] + [mobius_for_scoring_only(k) for k in range(1, nmax + 1)]
        lambda_reference = [0.0] + [
            von_mangoldt_for_scoring_only(k) for k in range(1, nmax + 1)
        ]
        main_rows.append(
            {
                "N": nmax,
                "opaque_atom_count": len(atoms),
                "verifier_prime_count": expected_prime_count,
                "recovered_atoms_all_prime_fraction": prime_check_fraction,
                "recovered_all_primes": len(atoms) == expected_prime_count and prime_check_fraction == 1.0,
                "unique_factorization_fraction": recovered["unique_factorization_fraction"],
                "zeta_coefficients_all_one_fraction": sum(c == 1 for c in zeta[1:]) / nmax,
                "inverse_coefficients_exact_mobius_fraction": exact_fraction(
                    inverse, mobius_reference
                ),
                "lambda_coefficients_exact_fraction": sum(
                    abs(x - y) < 1e-12 for x, y in zip(lam[1:], lambda_reference[1:])
                )
                / nmax,
                "lambda_coefficients_max_abs_error": max(
                    abs(x - y) for x, y in zip(lam[1:], lambda_reference[1:])
                ),
                "lambda_nonzero_support_count": sum(abs(x) > 0 for x in lam[1:]),
                "max_entropy_vs_det_weight_error": recovered[
                    "max_entropy_vs_determinant_weight_error"
                ],
                "max_tensor_entropy_additivity_error": recovered[
                    "max_operation_entropy_additivity_error"
                ],
                "det_weight_multiplicativity_fraction": recovered[
                    "operation_weight_multiplicativity_fraction"
                ],
                "fixed_point_tensor_identity_fraction": recovered[
                    "fixed_point_tensor_identity_fraction"
                ],
            }
        )
        if nmax == max(cutoffs) and args.save_registries:
            (out / "registries" / "tensor_product_public.json").write_text(
                json.dumps(main_public, indent=2, sort_keys=True) + "\n", encoding="utf-8"
            )
        if nmax == max(cutoffs):
            (out / "tensor_recovery.json").write_text(
                json.dumps(recovered, indent=2, sort_keys=True) + "\n", encoding="utf-8"
            )
            (out / "coefficient_ledger_N256.json").write_text(
                json.dumps(
                    {
                        "cutoff": nmax,
                        "recovered_atom_weights": atoms,
                        "zeta_dirichlet_coefficients": {
                            str(k): zeta[k] for k in range(1, nmax + 1)
                        },
                        "reciprocal_determinant_coefficients": {
                            str(k): inverse[k] for k in range(1, nmax + 1)
                        },
                        "negative_log_derivative_coefficients": {
                            str(k): lam[k] for k in range(1, nmax + 1)
                        },
                    },
                    indent=2,
                    sort_keys=True,
                ) + "\n",
                encoding="utf-8",
            )

        target_atoms = atoms
        target_zeta = zeta
        target_inverse = inverse
        target_lam = lam
        # Positive grammar control.  The diagonal atom shift has one isolated
        # self-loop per atom.  A freely mixing two-symbol full shift has
        # Z=1/(1-p^-s-q^-s) and creates forbidden mixed primitive words.
        for i, p in enumerate(target_atoms[:8]):
            for q in target_atoms[i + 1 : 8]:
                pair_cutoff = p * q
                diagonal_zeta = euler_coefficients([p, q], pair_cutoff)
                diagonal_lam = log_derivative_coefficients([p, q], pair_cutoff)
                free_zeta = free_word_coefficients([p, q], pair_cutoff)
                free_lam = free_word_log_derivative_coefficients([p, q], pair_cutoff)
                no_mixing_rows.append(
                    {
                        "N": nmax,
                        "p": p,
                        "q": q,
                        "mixed_mass_pq": p * q,
                        "diagonal_atom_loop_zeta_coeff_at_pq": diagonal_zeta[p * q],
                        "free_mixing_zeta_coeff_at_pq": free_zeta[p * q],
                        "target_von_mangoldt_at_pq": 0.0,
                        "diagonal_atom_loop_logderiv_at_pq": diagonal_lam[p * q],
                        "free_mixing_logderiv_at_pq": free_lam[p * q],
                        "expected_free_mixing_log_pq": math.log(p * q),
                        "free_mixing_creates_spurious_mixed_term": free_lam[p * q] > 0,
                    }
                )
        for seed in range(args.random_seeds):
            rng = random.Random(10_000 * nmax + seed)
            random_atoms = sorted(rng.sample(range(2, nmax + 1), len(target_atoms)))
            rz = euler_coefficients(random_atoms, nmax)
            ri = inverse_euler_coefficients(random_atoms, nmax)
            rl = log_derivative_coefficients(random_atoms, nmax)
            random_rows.append(
                {
                    "N": nmax,
                    "seed": seed,
                    "atom_count": len(random_atoms),
                    "declared_vs_intrinsic_atom_jaccard": set_jaccard(
                        set(random_atoms), set(target_atoms)
                    ),
                    "zeta_coefficient_accuracy": exact_fraction(rz, target_zeta),
                    "inverse_coefficient_accuracy": exact_fraction(ri, target_inverse),
                    "lambda_relative_l1_error": lambda_relative_l1(rl, target_lam),
                }
            )

        # Additive alphabet law: F_m boxplus F_n := F_{m+n}, formal unit F_0.
        add_spec = RegistrySpec(
            name=f"alphabet_disjoint_union_N{nmax}",
            labels=tuple(range(0, nmax + 1)),
            unit_label=0,
            operation=lambda a, b: a + b,
        )
        add_public, _ = build_public_registry(add_spec)
        add_recovered = recover_from_registered_data(add_public)
        add_atoms = add_recovered["atom_weights"]
        additive_rows.append(
            {
                "N": nmax,
                "atom_count": len(add_atoms),
                "atom_weights": json.dumps(add_atoms),
                "unique_factorization_fraction": add_recovered["unique_factorization_fraction"],
                "has_zero_entropy_euler_atom": any(a == 1 for a in add_atoms),
                "euler_product_defined_for_Re_s_gt_1": all(a > 1 for a in add_atoms),
                "max_entropy_additivity_error": add_recovered[
                    "max_operation_entropy_additivity_error"
                ],
                "det_weight_multiplicativity_fraction": add_recovered[
                    "operation_weight_multiplicativity_fraction"
                ],
                "fixed_point_tensor_identity_fraction": add_recovered[
                    "fixed_point_tensor_identity_fraction"
                ],
            }
        )
        if nmax == max(cutoffs) and args.save_registries:
            (out / "registries" / "additive_public.json").write_text(
                json.dumps(add_public, indent=2, sort_keys=True) + "\n", encoding="utf-8"
            )

        # Shifted multiplication, conjugate to N under phi(n)=n-1:
        # m star n=(m-1)(n-1)+1, with unit F_2 and atoms F_{p+1}.
        shift_spec = RegistrySpec(
            name=f"shifted_multiplication_N{nmax}",
            labels=tuple(range(2, nmax + 1)),
            unit_label=2,
            operation=lambda a, b: (a - 1) * (b - 1) + 1,
        )
        shift_public, _ = build_public_registry(shift_spec)
        shift_recovered = recover_from_registered_data(shift_public)
        shift_atoms = shift_recovered["atom_weights"]
        shift_zeta = euler_coefficients(shift_atoms, nmax)
        shift_inverse = inverse_euler_coefficients(shift_atoms, nmax)
        shift_lam = log_derivative_coefficients(shift_atoms, nmax)
        centered_atoms = [a - 1 for a in shift_atoms]
        centered_zeta = euler_coefficients(centered_atoms, nmax)
        centered_inverse = inverse_euler_coefficients(centered_atoms, nmax)
        centered_lam = log_derivative_coefficients(centered_atoms, nmax)
        shifted_rows.append(
            {
                "N": nmax,
                "atom_count": len(shift_atoms),
                "all_atoms_are_shifted_primes_fraction": sum(
                    is_prime_for_scoring_only(a - 1) for a in shift_atoms
                )
                / len(shift_atoms),
                "unique_factorization_fraction": shift_recovered["unique_factorization_fraction"],
                "intrinsic_entropy_zeta_accuracy": exact_fraction(shift_zeta, target_zeta),
                "intrinsic_entropy_inverse_accuracy": exact_fraction(
                    shift_inverse, target_inverse
                ),
                "intrinsic_entropy_lambda_relative_l1_error": lambda_relative_l1(
                    shift_lam, target_lam
                ),
                "posthoc_centered_clock_zeta_accuracy": exact_fraction(
                    centered_zeta, target_zeta
                ),
                "posthoc_centered_clock_inverse_accuracy": exact_fraction(
                    centered_inverse, target_inverse
                ),
                "posthoc_centered_clock_lambda_relative_l1_error": lambda_relative_l1(
                    centered_lam, target_lam
                ),
                "max_intrinsic_entropy_additivity_error": shift_recovered[
                    "max_operation_entropy_additivity_error"
                ],
                "det_weight_multiplicativity_fraction": shift_recovered[
                    "operation_weight_multiplicativity_fraction"
                ],
                "fixed_point_tensor_identity_fraction": shift_recovered[
                    "fixed_point_tensor_identity_fraction"
                ],
            }
        )
        if nmax == max(cutoffs) and args.save_registries:
            (out / "registries" / "shifted_public.json").write_text(
                json.dumps(shift_public, indent=2, sort_keys=True) + "\n", encoding="utf-8"
            )

    write_csv(out / "main_raw.csv", main_rows)
    write_csv(out / "random_atom_raw.csv", random_rows)
    write_csv(out / "additive_raw.csv", additive_rows)
    write_csv(out / "shifted_raw.csv", shifted_rows)
    write_csv(out / "no_mixing_raw.csv", no_mixing_rows)
    no_mixing_summary = []
    for nmax in cutoffs:
        rows = [row for row in no_mixing_rows if row["N"] == nmax]
        no_mixing_summary.append(
            {
                "N": nmax,
                "distinct_atom_pairs_tested": len(rows),
                "diagonal_zeta_coeff_at_pq_all_one_fraction": sum(
                    row["diagonal_atom_loop_zeta_coeff_at_pq"] == 1 for row in rows
                )
                / len(rows),
                "diagonal_logderiv_at_pq_all_zero_fraction": sum(
                    row["diagonal_atom_loop_logderiv_at_pq"] == 0 for row in rows
                )
                / len(rows),
                "free_zeta_coeff_at_pq_all_two_fraction": sum(
                    row["free_mixing_zeta_coeff_at_pq"] == 2 for row in rows
                )
                / len(rows),
                "free_logderiv_spurious_mixed_fraction": sum(
                    row["free_mixing_creates_spurious_mixed_term"] for row in rows
                )
                / len(rows),
                "max_free_logderiv_vs_logpq_error": max(
                    abs(
                        row["free_mixing_logderiv_at_pq"]
                        - row["expected_free_mixing_log_pq"]
                    )
                    for row in rows
                ),
            }
        )
    summary = {
        "experiment": "tensor-atomic full-shift exact recovery",
        "candidate_algorithm_reads_prime_table": False,
        "candidate_algorithm_reads_Riemann_zeros": False,
        "candidate_input": "opaque IDs + operation table + entropy + AM reciprocal determinant",
        "cutoffs": cutoffs,
        "random_seeds_per_cutoff": args.random_seeds,
        "large_registries_persisted": args.save_registries,
        "main": main_rows,
        "random": [summarize_random(random_rows, n) for n in cutoffs],
        "additive": additive_rows,
        "shifted": shifted_rows,
        "no_mixing_positive_control": no_mixing_summary,
    }
    (out / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
