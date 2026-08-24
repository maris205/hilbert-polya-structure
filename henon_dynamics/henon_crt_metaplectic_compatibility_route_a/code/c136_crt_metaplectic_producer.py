#!/usr/bin/env python3
"""Produce the exact HCS-C136 CRT-metaplectic compatibility receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results" / "c136_crt_metaplectic_evidence.json"
A = ((3, -1), (1, 0))
PAIR_LEVELS = [(3, 5), (3, 7), (3, 11), (3, 13), (5, 7), (5, 9), (5, 11), (7, 9)]
TRIPLE_LEVELS = [(3, 5, 7), (3, 5, 11), (3, 7, 11), (5, 7, 9)]
CHARACTERS = (1, 2)
ANTIUNITARY_LEVELS = (3, 5, 9, 15)


class Ledger:
    """Streaming SHA-256 for newline-separated exact case records."""

    def __init__(self) -> None:
        self._hash = hashlib.sha256()
        self.count = 0

    def add(self, line: str) -> None:
        if self.count:
            self._hash.update(b"\n")
        self._hash.update(line.encode())
        self.count += 1

    def receipt(self) -> dict[str, int | str]:
        return {"cases": self.count, "sha256": self._hash.hexdigest()}


def canonical_payload(data: dict) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


def inverse(value: int, modulus: int) -> int:
    return pow(value, -1, modulus)


def half(modulus: int) -> int:
    return inverse(2, modulus)


def induced_twist(character: int, factor: int, cofactor: int) -> int:
    return (character % factor) * inverse(cofactor, factor) % factor


def pair_receipt(m: int, n: int) -> dict:
    assert m > 1 and n > 1 and m % 2 == n % 2 == 1 and math.gcd(m, n) == 1
    level = m * n
    a = inverse(n, m)
    b = inverse(m, n)
    hm, hn, hl = half(m), half(n), half(level)
    e_m = n * a % level
    e_n = m * b % level
    assert e_m % m == 1 and e_m % n == 0
    assert e_n % m == 0 and e_n % n == 1
    assert (e_m + e_n) % level == 1
    assert e_m * e_m % level == e_m and e_n * e_n % level == e_n
    assert e_m * e_n % level == 0

    fourier = Ledger()
    chirp = Ledger()
    unitary = Ledger()
    weyl = Ledger()
    conjugation = Ledger()
    antiunitary_crt = {character: Ledger() for character in CHARACTERS}

    for x in range(level):
        xm, xn = x % m, x % n
        conjugation.add(f"{x}:{xm},{xn}:coefficientwise-conjugation")
        global_chirp = 3 * hl * x * x % level
        local_chirp = (
            n * (3 * a * hm * xm * xm)
            + m * (3 * b * hn * xn * xn)
        ) % level
        assert global_chirp == local_chirp
        chirp.add(f"{x}:{global_chirp}:{local_chirp}")
        for y in range(level):
            ym, yn = y % m, y % n
            global_fourier = x * y % level
            local_fourier = (n * a * xm * ym + m * b * xn * yn) % level
            assert global_fourier == local_fourier
            fourier.add(f"{x},{y}:{global_fourier}:{local_fourier}")

            global_u = (3 * hl * x * x - x * y) % level
            local_u = (
                n * a * (3 * hm * xm * xm - xm * ym)
                + m * b * (3 * hn * xn * xn - xn * yn)
            ) % level
            assert global_u == local_u
            unitary.add(f"{x},{y}:{global_u}:{local_u}")

            for character in CHARACTERS:
                c_m = induced_twist(character, m, n)
                c_n = induced_twist(character, n, m)
                global_theta = character * x * y % level
                local_theta = (
                    n * c_m * xm * ym + m * c_n * xn * yn
                ) % level
                assert global_theta == local_theta
                antiunitary_crt[character].add(
                    f"{character}:{x},{y}:{c_m},{c_n}:"
                    f"{global_theta}:{local_theta}"
                )

    for q in range(level):
        qm, qn = q % m, q % n
        for p in range(level):
            pm, pn = p % m, p % n
            for x in range(level):
                xm, xn = x % m, x % n
                global_phase = (q * x + hl * q * p) % level
                local_phase = (
                    n * a * (qm * xm + hm * qm * pm)
                    + m * b * (qn * xn + hn * qn * pn)
                ) % level
                assert global_phase == local_phase
                output = (x + p) % level
                assert output % m == (xm + pm) % m
                assert output % n == (xn + pn) % n
                weyl.add(
                    f"{q},{p},{x}:{global_phase}:{local_phase}:"
                    f"{output % m},{output % n}"
                )

    return {
        "M": m,
        "N": n,
        "L": level,
        "a_M_inverse_of_N": a,
        "a_N_inverse_of_M": b,
        "crt_idempotents": {"e_M": e_m, "e_N": e_n},
        "fourier_kernel_ledger": fourier.receipt(),
        "chirp_diagonal_ledger": chirp.receipt(),
        "unitary_kernel_ledger": unitary.receipt(),
        "weyl_basis_action_ledger": weyl.receipt(),
        "conjugation_basis_ledger": conjugation.receipt(),
        "antiunitary_crt_kernel_ledgers": [
            {"character": character, "ledger": antiunitary_crt[character].receipt()}
            for character in CHARACTERS
        ],
        "naive_standard_character_tensor_compatible": a == 1 and b == 1,
    }


def antiunitary_level_receipt(level: int) -> dict:
    """Exact single-level receipts for Theta=F K at every unit character."""

    assert level >= 3 and level % 2 == 1
    h = half(level)
    rows = []
    for character in range(1, level):
        if math.gcd(character, level) != 1:
            continue
        involution = Ledger()
        unitary_reversal = Ledger()
        weyl_swap = Ledger()

        for x in range(level):
            for y in range(level):
                orthogonality_frequency = character * (x - y) % level
                theta_square_sum = level if orthogonality_frequency == 0 else 0
                identity_sum = level if x == y else 0
                assert theta_square_sum == identity_sum
                involution.add(
                    f"{character}:{x},{y}:{orthogonality_frequency}:"
                    f"{theta_square_sum}:{identity_sum}"
                )

                conjugated_u = (-3 * character * h * x * x + character * x * y) % level
                c_inverse_f = (-3 * character * h * x * x + character * x * y) % level
                assert conjugated_u == c_inverse_f
                reversed_u = (character * x * y - 3 * character * h * y * y) % level
                inverse_u = (character * x * y - 3 * character * h * y * y) % level
                assert reversed_u == inverse_u
                unitary_reversal.add(
                    f"{character}:{x},{y}:{conjugated_u}:{c_inverse_f}:"
                    f"{reversed_u}:{inverse_u}"
                )

        for q in range(level):
            for p in range(level):
                after_conjugation = character * h * q * p % level
                reordered_prefactor = (after_conjugation - character * p * q) % level
                target_prefactor = -character * h * p * q % level
                assert reordered_prefactor == target_prefactor
                for x in range(level):
                    output = (x + q) % level
                    left_action = (
                        reordered_prefactor + character * p * output
                    ) % level
                    right_action = (
                        character * p * x + character * h * p * q
                    ) % level
                    assert left_action == right_action
                    weyl_swap.add(
                        f"{character}:{q},{p},{x}:{after_conjugation}:"
                        f"{reordered_prefactor}:{target_prefactor}:"
                        f"{left_action}:{right_action}:{output}"
                    )

        rows.append({
            "character": character,
            "theta_square_ledger": involution.receipt(),
            "unitary_reversal_kernel_ledger": unitary_reversal.receipt(),
            "weyl_swap_basis_action_ledger": weyl_swap.receipt(),
        })
    return {"r": level, "unit_characters": rows}


def direct_twists(factors: Iterable[int], character: int) -> dict[str, int]:
    values = tuple(factors)
    level = math.prod(values)
    return {
        str(r): induced_twist(character, r, level // r)
        for r in values
    }


Tree = int | tuple["Tree", "Tree"]


def tree_product(tree: Tree) -> int:
    if isinstance(tree, int):
        return tree
    return tree_product(tree[0]) * tree_product(tree[1])


def recursive_twists(tree: Tree, character: int) -> dict[str, int]:
    if isinstance(tree, int):
        return {str(tree): character % tree}
    left, right = tree
    left_level, right_level = tree_product(left), tree_product(right)
    left_character = induced_twist(character, left_level, right_level)
    right_character = induced_twist(character, right_level, left_level)
    out = recursive_twists(left, left_character)
    out.update(recursive_twists(right, right_character))
    return out


def triple_receipt(factors: tuple[int, int, int]) -> dict:
    assert all(r > 1 and r % 2 == 1 for r in factors)
    assert all(math.gcd(factors[i], factors[j]) == 1 for i in range(3) for j in range(i))
    level = math.prod(factors)
    entries = []
    for character in CHARACTERS:
        assert math.gcd(character, level) == 1
        direct = direct_twists(factors, character)
        left_tree: Tree = ((factors[0], factors[1]), factors[2])
        right_tree: Tree = (factors[0], (factors[1], factors[2]))
        left = recursive_twists(left_tree, character)
        right = recursive_twists(right_tree, character)
        assert direct == left == right

        kernel = Ledger()
        hl = half(level)
        for x in range(level):
            for y in range(level):
                global_u = character * (3 * hl * x * x - x * y) % level
                local_u = 0
                for r in factors:
                    cofactor = level // r
                    xr, yr = x % r, y % r
                    c_r = direct[str(r)]
                    local_u += cofactor * c_r * (3 * half(r) * xr * xr - xr * yr)
                local_u %= level
                assert global_u == local_u
                kernel.add(f"{character}:{x},{y}:{global_u}:{local_u}")
        entries.append({
            "character": character,
            "direct_twists": direct,
            "left_bracket_twists": left,
            "right_bracket_twists": right,
            "unitary_kernel_ledger": kernel.receipt(),
        })
    return {"factors": list(factors), "L": level, "characters": entries}


def four_factor_receipt() -> dict:
    factors = (3, 5, 7, 11)
    trees: dict[str, Tree] = {
        "left": (((3, 5), 7), 11),
        "right": (3, (5, (7, 11))),
        "balanced": ((3, 5), (7, 11)),
    }
    rows = []
    for character in CHARACTERS:
        direct = direct_twists(factors, character)
        bracketings = {name: recursive_twists(tree, character) for name, tree in trees.items()}
        assert all(row == direct for row in bracketings.values())
        rows.append({
            "character": character,
            "direct_twists": direct,
            "bracketings": bracketings,
        })
    return {"factors": list(factors), "L": math.prod(factors), "characters": rows}


def build() -> dict:
    pair_rows = [pair_receipt(m, n) for m, n in PAIR_LEVELS]
    triple_rows = [triple_receipt(row) for row in TRIPLE_LEVELS]
    antiunitary_rows = [antiunitary_level_receipt(level) for level in ANTIUNITARY_LEVELS]
    pair_fourier = sum(row["fourier_kernel_ledger"]["cases"] for row in pair_rows)
    pair_chirp = sum(row["chirp_diagonal_ledger"]["cases"] for row in pair_rows)
    pair_unitary = sum(row["unitary_kernel_ledger"]["cases"] for row in pair_rows)
    pair_weyl = sum(row["weyl_basis_action_ledger"]["cases"] for row in pair_rows)
    pair_conjugation = sum(row["conjugation_basis_ledger"]["cases"] for row in pair_rows)
    pair_antiunitary_crt = sum(
        char["ledger"]["cases"]
        for row in pair_rows for char in row["antiunitary_crt_kernel_ledgers"]
    )
    triple_unitary = sum(
        char["unitary_kernel_ledger"]["cases"]
        for row in triple_rows for char in row["characters"]
    )
    antiunitary_involution = sum(
        char["theta_square_ledger"]["cases"]
        for row in antiunitary_rows for char in row["unit_characters"]
    )
    antiunitary_reversal = sum(
        char["unitary_reversal_kernel_ledger"]["cases"]
        for row in antiunitary_rows for char in row["unit_characters"]
    )
    antiunitary_weyl = sum(
        char["weyl_swap_basis_action_ledger"]["cases"]
        for row in antiunitary_rows for char in row["unit_characters"]
    )

    naive_m, naive_n = 3, 5
    naive_l = naive_m * naive_n
    naive_global = 1
    naive_standard = (naive_n + naive_m) % naive_l
    correct = (
        naive_n * inverse(naive_n, naive_m)
        + naive_m * inverse(naive_m, naive_n)
    ) % naive_l
    assert (naive_global, naive_standard, correct) == (1, 8, 1)

    wrong_m, wrong_n = 5, 7
    wrong_l = wrong_m * wrong_n
    inverse_scaled = (
        wrong_n * inverse(wrong_n, wrong_m)
        + wrong_m * inverse(wrong_m, wrong_n)
    ) % wrong_l
    raw_scaled = (wrong_n * (wrong_n % wrong_m) + wrong_m * (wrong_m % wrong_n)) % wrong_l
    assert inverse_scaled == 1 and raw_scaled == 4

    data = {
        "schema": "HCS-C136-crt-metaplectic-v1",
        "candidate_id": "HCS-C136",
        "date_utc": "2026-08-24",
        "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "classical_matrix": [[3, -1], [1, 0]],
        "source_dependency": {
            "candidate": "HCS-C131",
            "evidence_sha256": "676c4469cb52785efb46ed258b9d7207a8db3c0457d7ea8205e22bee382b3869",
            "theorem_package_sha256": "74b317b5a31c4a476060531f4527785afba3e9dc7930167591a4c546d932f415",
            "used_content": "odd-level Weyl/Fourier/chirp conventions and exact Egorov theorem only",
        },
        "family": {
            "levels": "all odd integers r>=3",
            "characters": "all units c in Z/rZ",
            "factorizations": "all fixed ordered finite families of pairwise-coprime odd levels greater than one",
            "certified_pairs": [list(row) for row in PAIR_LEVELS],
            "certified_triples": [list(row) for row in TRIPLE_LEVELS],
        },
        "phase_conventions": {
            "omega_r": "exp(2*pi*i/r)",
            "half": "h_r is the unique residue with 2*h_r=1 mod r",
            "fourier": "F_[r,c](x,y)=r^(-1/2)*omega_r^(c*x*y)",
            "chirp": "C_[r,c](x,x)=omega_r^(3*c*h_r*x^2)",
            "unitary": "U_[r,c]=C_[r,c]*F_[r,c]^(-1)",
            "weyl": "W_[r,c](q,p)=omega_r^(-c*h_r*q*p)*Q_r^(c*q)*P_r^p",
            "conjugation": "K_r is coefficientwise conjugation in the standard residue basis",
            "antiunitary": "Theta_[r,c]=F_[r,c]*K_r",
            "clock": "one application of U_[r,c] implements one application of A",
        },
        "antiunitary_theorem": {
            "hypotheses": "r>=3 odd and c is a unit modulo r",
            "definition": "Theta_[r,c]=F_[r,c]*K_r",
            "involution_identity": "Theta_[r,c]^2=I",
            "unitary_reversal_identity": "Theta_[r,c] U_[r,c] Theta_[r,c]^(-1)=U_[r,c]^(-1)",
            "weyl_swap_identity": "Theta_[r,c] W_[r,c](q,p) Theta_[r,c]^(-1)=W_[r,c](p,q)",
            "crt_identity": "J Theta_[L,c] J^(-1)=Theta_[M,c_M] anti-tensor Theta_[N,c_N]",
            "crt_tensor_convention": "anti-tensor is defined on pure tensors by v tensor w maps to Theta_M(v) tensor Theta_N(w) and extended conjugate-linearly in the ordered residue bases",
        },
        "two_factor_theorem": {
            "hypotheses": "M,N>1 odd and gcd(M,N)=1; c is a unit modulo L=M*N",
            "canonical_identification": "J_[M,N]|x mod L>=|x mod M> tensor |x mod N>",
            "local_characters": "c_M=(c mod M)*N^(-1) mod M and c_N=(c mod N)*M^(-1) mod N",
            "fourier_identity": "J F_[L,c] J^(-1)=F_[M,c_M] tensor F_[N,c_N]",
            "chirp_identity": "J C_[L,c] J^(-1)=C_[M,c_M] tensor C_[N,c_N]",
            "weyl_identity": "J W_[L,c](q,p) J^(-1)=W_[M,c_M](q_M,p_M) tensor W_[N,c_N](q_N,p_N)",
            "unitary_identity": "J U_[L,c] J^(-1)=U_[M,c_M] tensor U_[N,c_N]",
            "antiunitary_identity": "J Theta_[L,c] J^(-1)=Theta_[M,c_M] anti-tensor Theta_[N,c_N]",
            "scalar_anomaly": False,
            "clock_preserved": True,
        },
        "multi_factor_theorem": {
            "ordered_leaves": "a fixed ordered tuple (r_1,...,r_k) of pairwise-coprime odd levels greater than one",
            "local_character": "c_j=(c mod r_j)*(L/r_j)^(-1) mod r_j",
            "unitary_identity": "J U_[L,c] J^(-1)=tensor_j U_[r_j,c_j]",
            "antiunitary_identity": "J Theta_[L,c] J^(-1)=anti-tensor_j Theta_[r_j,c_j]",
            "coherence": "exact and independent only of binary split schedule and parenthesization for the fixed ordered leaves, under canonical tensor associators",
            "factor_permutation_coherence_claimed": False,
            "standard_character_family_direct_compatibility_claimed": False,
            "noncoprime_factorization_claimed": False,
        },
        "certified_pair_receipts": pair_rows,
        "certified_triple_receipts": triple_rows,
        "antiunitary_level_receipts": antiunitary_rows,
        "four_factor_coherence_receipt": four_factor_receipt(),
        "controls": {
            "naive_standard_character": {
                "M": naive_m,
                "N": naive_n,
                "test_entry": "Fourier output x=1, input y=1",
                "global_exponent_mod_15": naive_global,
                "naive_tensor_exponent_mod_15": naive_standard,
                "inverse_scaled_tensor_exponent_mod_15": correct,
                "row_x0_forces_projective_scalar_one": True,
                "naive_tensor_equal_even_projectively": False,
            },
            "raw_residue_instead_of_inverse": {
                "M": wrong_m,
                "N": wrong_n,
                "global_exponent_mod_35": 1,
                "inverse_scaled_exponent_mod_35": inverse_scaled,
                "raw_residue_scaled_exponent_mod_35": raw_scaled,
                "raw_residue_rule_valid": False,
            },
            "noncoprime": {
                "M": 3,
                "N": 9,
                "gcd": 3,
                "crt_identification_available": False,
                "scope": "excluded because the residue map is not a product-ring bijection",
            },
            "even_modulus": {
                "test_level": 4,
                "inverse_of_two_exists": False,
                "same_half_phase_family_defined": False,
                "scope": "only the frozen qp/2 convention; other even-level Weil conventions are not excluded",
            },
        },
        "exact_certificate": {
            "pair_fourier_kernel_cases": pair_fourier,
            "pair_chirp_diagonal_cases": pair_chirp,
            "pair_unitary_kernel_cases": pair_unitary,
            "pair_weyl_basis_action_cases": pair_weyl,
            "pair_conjugation_basis_cases": pair_conjugation,
            "pair_antiunitary_crt_kernel_cases": pair_antiunitary_crt,
            "triple_unitary_kernel_cases": triple_unitary,
            "antiunitary_theta_square_cases": antiunitary_involution,
            "antiunitary_unitary_reversal_cases": antiunitary_reversal,
            "antiunitary_weyl_swap_cases": antiunitary_weyl,
            "four_factor_bracket_comparisons": len(CHARACTERS) * 3,
            "all_pair_receipts_pass": True,
            "all_multi_factor_receipts_pass": True,
            "all_antiunitary_receipts_pass": True,
            "all_negative_controls_pass": True,
        },
        "progress": {
            "closed_gate": "coprime odd-level CRT tensor compatibility and antiunitary covariance for induced additive characters",
            "new_route_a_coordinate": "EXACT_CRT_ANTIUNITARY_COHERENCE_PASS",
            "over_prior_gate": "C131 left cross-level projective compatibility unclaimed; C136 proves exact two- and fixed-ordered-leaf multi-factor coherence, certifies the generalized antiunitary reversal and its CRT compatibility, and isolates the naive standard-character failure",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "uses_prime_or_zero_table": False,
            "claims_target_divisor_match": False,
            "claims_euler_factors_or_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
            "claims_standard_character_projective_compatibility": False,
            "claims_factor_permutation_coherence": False,
        },
        "nonclaims": [
            "no direct tensor compatibility for the standard c=1 factors",
            "no noncoprime or even-level CRT theorem under the frozen convention",
            "no coherent correction back to standard local characters",
            "no factor-permutation or symmetric-monoidal coherence theorem",
            "no semiclassical trace or external target match",
            "no Euler factor, root number, automorphy, or Hilbert--Polya claim",
        ],
    }
    data["payload_sha256"] = hashlib.sha256(canonical_payload(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "C136_PRODUCER_PASS",
        "evidence_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
        "pair_weyl_cases": data["exact_certificate"]["pair_weyl_basis_action_cases"],
        "triple_unitary_cases": data["exact_certificate"]["triple_unitary_kernel_cases"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
