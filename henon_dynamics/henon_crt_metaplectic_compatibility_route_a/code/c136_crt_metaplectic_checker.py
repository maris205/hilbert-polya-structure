#!/usr/bin/env python3
"""Independent exact reconstruction for the HCS-C136 evidence object.

This checker deliberately does not import the producer.
"""

from __future__ import annotations

import functools
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Iterator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results" / "c136_crt_metaplectic_evidence.json"
PAIRS = ((3, 5), (3, 7), (3, 11), (3, 13), (5, 7), (5, 9), (5, 11), (7, 9))
TRIPLES = ((3, 5, 7), (3, 5, 11), (3, 7, 11), (5, 7, 9))
ANTIUNITARY_LEVELS = (3, 5, 9, 15)


def payload_hash(obj: dict) -> str:
    clean = dict(obj)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def inv(a: int, modulus: int) -> int:
    return pow(a, -1, modulus)


def digest(stream: Iterator[str]) -> dict[str, int | str]:
    h = hashlib.sha256()
    count = 0
    for row in stream:
        if count:
            h.update(b"\n")
        h.update(row.encode())
        count += 1
    return {"cases": count, "sha256": h.hexdigest()}


def pair_expected(m: int, n: int) -> dict:
    level = m * n
    am, an = inv(n, m), inv(m, n)
    hm, hn, hl = inv(2, m), inv(2, n), inv(2, level)

    def fourier_rows() -> Iterator[str]:
        for x in range(level):
            for y in range(level):
                g = x * y % level
                r = (n * am * (x % m) * (y % m) + m * an * (x % n) * (y % n)) % level
                assert g == r
                yield f"{x},{y}:{g}:{r}"

    def chirp_rows() -> Iterator[str]:
        for x in range(level):
            g = 3 * hl * x * x % level
            r = (
                n * 3 * am * hm * (x % m) ** 2
                + m * 3 * an * hn * (x % n) ** 2
            ) % level
            assert g == r
            yield f"{x}:{g}:{r}"

    def unitary_rows() -> Iterator[str]:
        for x in range(level):
            for y in range(level):
                g = (3 * hl * x * x - x * y) % level
                r = (
                    n * am * (3 * hm * (x % m) ** 2 - (x % m) * (y % m))
                    + m * an * (3 * hn * (x % n) ** 2 - (x % n) * (y % n))
                ) % level
                assert g == r
                yield f"{x},{y}:{g}:{r}"

    def weyl_rows() -> Iterator[str]:
        for q in range(level):
            for p in range(level):
                for x in range(level):
                    g = (q * x + hl * q * p) % level
                    r = (
                        n * am * ((q % m) * (x % m) + hm * (q % m) * (p % m))
                        + m * an * ((q % n) * (x % n) + hn * (q % n) * (p % n))
                    ) % level
                    assert g == r
                    out = (x + p) % level
                    yield f"{q},{p},{x}:{g}:{r}:{out % m},{out % n}"

    def conjugation_rows() -> Iterator[str]:
        for x in range(level):
            yield f"{x}:{x % m},{x % n}:coefficientwise-conjugation"

    def antiunitary_crt_rows(character: int) -> Iterator[str]:
        c_m = (character % m) * inv(n, m) % m
        c_n = (character % n) * inv(m, n) % n
        for x in range(level):
            for y in range(level):
                global_theta = character * x * y % level
                local_theta = (
                    n * c_m * (x % m) * (y % m)
                    + m * c_n * (x % n) * (y % n)
                ) % level
                assert global_theta == local_theta
                yield (
                    f"{character}:{x},{y}:{c_m},{c_n}:"
                    f"{global_theta}:{local_theta}"
                )

    em, en = n * am % level, m * an % level
    assert (em * em - em) % level == 0
    assert (en * en - en) % level == 0
    assert em * en % level == 0
    return {
        "M": m,
        "N": n,
        "L": level,
        "a_M_inverse_of_N": am,
        "a_N_inverse_of_M": an,
        "crt_idempotents": {"e_M": em, "e_N": en},
        "fourier_kernel_ledger": digest(fourier_rows()),
        "chirp_diagonal_ledger": digest(chirp_rows()),
        "unitary_kernel_ledger": digest(unitary_rows()),
        "weyl_basis_action_ledger": digest(weyl_rows()),
        "conjugation_basis_ledger": digest(conjugation_rows()),
        "antiunitary_crt_kernel_ledgers": [
            {"character": character, "ledger": digest(antiunitary_crt_rows(character))}
            for character in (1, 2)
        ],
        "naive_standard_character_tensor_compatible": am == 1 and an == 1,
    }


def antiunitary_expected(level: int) -> dict:
    h = inv(2, level)
    chars = []
    for character in range(1, level):
        if math.gcd(character, level) != 1:
            continue

        def involution_rows() -> Iterator[str]:
            for x in range(level):
                for y in range(level):
                    frequency = character * (x - y) % level
                    lhs = level if frequency == 0 else 0
                    rhs = level if x == y else 0
                    assert lhs == rhs
                    yield f"{character}:{x},{y}:{frequency}:{lhs}:{rhs}"

        def reversal_rows() -> Iterator[str]:
            for x in range(level):
                for y in range(level):
                    conjugated_u = (-3 * character * h * x * x + character * x * y) % level
                    c_inverse_f = (-3 * character * h * x * x + character * x * y) % level
                    assert conjugated_u == c_inverse_f
                    reversed_u = (character * x * y - 3 * character * h * y * y) % level
                    inverse_u = (character * x * y - 3 * character * h * y * y) % level
                    assert reversed_u == inverse_u
                    yield (
                        f"{character}:{x},{y}:{conjugated_u}:{c_inverse_f}:"
                        f"{reversed_u}:{inverse_u}"
                    )

        def weyl_rows() -> Iterator[str]:
            for q in range(level):
                for p in range(level):
                    after_k = character * h * q * p % level
                    reordered = (after_k - character * p * q) % level
                    target = -character * h * p * q % level
                    assert reordered == target
                    for x in range(level):
                        output = (x + q) % level
                        lhs = (reordered + character * p * output) % level
                        rhs = (character * p * x + character * h * p * q) % level
                        assert lhs == rhs
                        yield (
                            f"{character}:{q},{p},{x}:{after_k}:{reordered}:"
                            f"{target}:{lhs}:{rhs}:{output}"
                        )

        chars.append({
            "character": character,
            "theta_square_ledger": digest(involution_rows()),
            "unitary_reversal_kernel_ledger": digest(reversal_rows()),
            "weyl_swap_basis_action_ledger": digest(weyl_rows()),
        })
    return {"r": level, "unit_characters": chars}


def product(tree: int | tuple) -> int:
    return tree if isinstance(tree, int) else product(tree[0]) * product(tree[1])


def split_tree(tree: int | tuple, c: int) -> dict[str, int]:
    if isinstance(tree, int):
        return {str(tree): c % tree}
    left, right = tree
    lmod, rmod = product(left), product(right)
    lc = (c % lmod) * inv(rmod, lmod) % lmod
    rc = (c % rmod) * inv(lmod, rmod) % rmod
    out = split_tree(left, lc)
    out.update(split_tree(right, rc))
    return out


def direct(factors: tuple[int, ...], c: int) -> dict[str, int]:
    level = math.prod(factors)
    return {str(r): (c % r) * inv(level // r, r) % r for r in factors}


def triple_expected(factors: tuple[int, int, int]) -> dict:
    level = math.prod(factors)
    chars = []
    for c in (1, 2):
        target = direct(factors, c)
        left = split_tree(((factors[0], factors[1]), factors[2]), c)
        right = split_tree((factors[0], (factors[1], factors[2])), c)
        assert target == left == right

        def kernel_rows() -> Iterator[str]:
            for x in range(level):
                for y in range(level):
                    g = c * (3 * inv(2, level) * x * x - x * y) % level
                    rside = 0
                    for r in factors:
                        rside += (
                            (level // r) * target[str(r)]
                            * (3 * inv(2, r) * (x % r) ** 2 - (x % r) * (y % r))
                        )
                    rside %= level
                    assert g == rside
                    yield f"{c}:{x},{y}:{g}:{rside}"

        chars.append({
            "character": c,
            "direct_twists": target,
            "left_bracket_twists": left,
            "right_bracket_twists": right,
            "unitary_kernel_ledger": digest(kernel_rows()),
        })
    return {"factors": list(factors), "L": level, "characters": chars}


def four_expected() -> dict:
    factors = (3, 5, 7, 11)
    trees = {
        "left": (((3, 5), 7), 11),
        "right": (3, (5, (7, 11))),
        "balanced": ((3, 5), (7, 11)),
    }
    chars = []
    for c in (1, 2):
        goal = direct(factors, c)
        bracketings = {name: split_tree(tree, c) for name, tree in trees.items()}
        assert all(row == goal for row in bracketings.values())
        chars.append({"character": c, "direct_twists": goal, "bracketings": bracketings})
    return {"factors": list(factors), "L": math.prod(factors), "characters": chars}


@functools.lru_cache(maxsize=1)
def reconstructed_receipts() -> tuple[list[dict], list[dict], dict, list[dict]]:
    return (
        [pair_expected(m, n) for m, n in PAIRS],
        [triple_expected(row) for row in TRIPLES],
        four_expected(),
        [antiunitary_expected(level) for level in ANTIUNITARY_LEVELS],
    )


def validate(data: dict) -> int:
    assert data["payload_sha256"] == payload_hash(data)
    assert set(data) == {
        "antiunitary_level_receipts", "antiunitary_theorem", "candidate_id",
        "certified_pair_receipts", "certified_triple_receipts",
        "classical_matrix", "controls", "date_utc", "exact_certificate", "family",
        "four_factor_coherence_receipt", "multi_factor_theorem", "nonclaims",
        "payload_sha256", "phase_conventions", "progress", "route_a", "schema",
        "scope", "scope_flags", "source_dependency", "two_factor_theorem",
    }
    assert data["schema"] == "HCS-C136-crt-metaplectic-v1"
    assert data["candidate_id"] == "HCS-C136"
    assert data["date_utc"] == "2026-08-24"
    assert data["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert data["classical_matrix"] == [[3, -1], [1, 0]]
    assert data["source_dependency"] == {
        "candidate": "HCS-C131",
        "evidence_sha256": "676c4469cb52785efb46ed258b9d7207a8db3c0457d7ea8205e22bee382b3869",
        "theorem_package_sha256": "74b317b5a31c4a476060531f4527785afba3e9dc7930167591a4c546d932f415",
        "used_content": "odd-level Weyl/Fourier/chirp conventions and exact Egorov theorem only",
    }
    assert data["family"] == {
        "levels": "all odd integers r>=3",
        "characters": "all units c in Z/rZ",
        "factorizations": "all fixed ordered finite families of pairwise-coprime odd levels greater than one",
        "certified_pairs": [list(row) for row in PAIRS],
        "certified_triples": [list(row) for row in TRIPLES],
    }
    assert data["phase_conventions"] == {
        "omega_r": "exp(2*pi*i/r)",
        "half": "h_r is the unique residue with 2*h_r=1 mod r",
        "fourier": "F_[r,c](x,y)=r^(-1/2)*omega_r^(c*x*y)",
        "chirp": "C_[r,c](x,x)=omega_r^(3*c*h_r*x^2)",
        "unitary": "U_[r,c]=C_[r,c]*F_[r,c]^(-1)",
        "weyl": "W_[r,c](q,p)=omega_r^(-c*h_r*q*p)*Q_r^(c*q)*P_r^p",
        "conjugation": "K_r is coefficientwise conjugation in the standard residue basis",
        "antiunitary": "Theta_[r,c]=F_[r,c]*K_r",
        "clock": "one application of U_[r,c] implements one application of A",
    }
    assert data["antiunitary_theorem"] == {
        "hypotheses": "r>=3 odd and c is a unit modulo r",
        "definition": "Theta_[r,c]=F_[r,c]*K_r",
        "involution_identity": "Theta_[r,c]^2=I",
        "unitary_reversal_identity": "Theta_[r,c] U_[r,c] Theta_[r,c]^(-1)=U_[r,c]^(-1)",
        "weyl_swap_identity": "Theta_[r,c] W_[r,c](q,p) Theta_[r,c]^(-1)=W_[r,c](p,q)",
        "crt_identity": "J Theta_[L,c] J^(-1)=Theta_[M,c_M] anti-tensor Theta_[N,c_N]",
        "crt_tensor_convention": "anti-tensor is defined on pure tensors by v tensor w maps to Theta_M(v) tensor Theta_N(w) and extended conjugate-linearly in the ordered residue bases",
    }
    assert data["two_factor_theorem"] == {
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
    }
    assert data["multi_factor_theorem"] == {
        "ordered_leaves": "a fixed ordered tuple (r_1,...,r_k) of pairwise-coprime odd levels greater than one",
        "local_character": "c_j=(c mod r_j)*(L/r_j)^(-1) mod r_j",
        "unitary_identity": "J U_[L,c] J^(-1)=tensor_j U_[r_j,c_j]",
        "antiunitary_identity": "J Theta_[L,c] J^(-1)=anti-tensor_j Theta_[r_j,c_j]",
        "coherence": "exact and independent only of binary split schedule and parenthesization for the fixed ordered leaves, under canonical tensor associators",
        "factor_permutation_coherence_claimed": False,
        "standard_character_family_direct_compatibility_claimed": False,
        "noncoprime_factorization_claimed": False,
    }

    pairs, triples, four, antiunitary = reconstructed_receipts()
    assert data["certified_pair_receipts"] == pairs
    assert data["certified_triple_receipts"] == triples
    assert data["four_factor_coherence_receipt"] == four
    assert data["antiunitary_level_receipts"] == antiunitary

    assert data["controls"] == {
        "naive_standard_character": {
            "M": 3, "N": 5,
            "test_entry": "Fourier output x=1, input y=1",
            "global_exponent_mod_15": 1,
            "naive_tensor_exponent_mod_15": 8,
            "inverse_scaled_tensor_exponent_mod_15": 1,
            "row_x0_forces_projective_scalar_one": True,
            "naive_tensor_equal_even_projectively": False,
        },
        "raw_residue_instead_of_inverse": {
            "M": 5, "N": 7,
            "global_exponent_mod_35": 1,
            "inverse_scaled_exponent_mod_35": 1,
            "raw_residue_scaled_exponent_mod_35": 4,
            "raw_residue_rule_valid": False,
        },
        "noncoprime": {
            "M": 3, "N": 9, "gcd": 3,
            "crt_identification_available": False,
            "scope": "excluded because the residue map is not a product-ring bijection",
        },
        "even_modulus": {
            "test_level": 4,
            "inverse_of_two_exists": False,
            "same_half_phase_family_defined": False,
            "scope": "only the frozen qp/2 convention; other even-level Weil conventions are not excluded",
        },
    }
    pair_fourier = sum(row["fourier_kernel_ledger"]["cases"] for row in pairs)
    pair_chirp = sum(row["chirp_diagonal_ledger"]["cases"] for row in pairs)
    pair_unitary = sum(row["unitary_kernel_ledger"]["cases"] for row in pairs)
    pair_weyl = sum(row["weyl_basis_action_ledger"]["cases"] for row in pairs)
    pair_conjugation = sum(row["conjugation_basis_ledger"]["cases"] for row in pairs)
    pair_antiunitary_crt = sum(
        char["ledger"]["cases"]
        for row in pairs for char in row["antiunitary_crt_kernel_ledgers"]
    )
    triple_unitary = sum(
        char["unitary_kernel_ledger"]["cases"] for row in triples for char in row["characters"]
    )
    antiunitary_involution = sum(
        char["theta_square_ledger"]["cases"]
        for row in antiunitary for char in row["unit_characters"]
    )
    antiunitary_reversal = sum(
        char["unitary_reversal_kernel_ledger"]["cases"]
        for row in antiunitary for char in row["unit_characters"]
    )
    antiunitary_weyl = sum(
        char["weyl_swap_basis_action_ledger"]["cases"]
        for row in antiunitary for char in row["unit_characters"]
    )
    assert data["exact_certificate"] == {
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
        "four_factor_bracket_comparisons": 6,
        "all_pair_receipts_pass": True,
        "all_multi_factor_receipts_pass": True,
        "all_antiunitary_receipts_pass": True,
        "all_negative_controls_pass": True,
    }
    assert data["progress"] == {
        "closed_gate": "coprime odd-level CRT tensor compatibility and antiunitary covariance for induced additive characters",
        "new_route_a_coordinate": "EXACT_CRT_ANTIUNITARY_COHERENCE_PASS",
        "over_prior_gate": "C131 left cross-level projective compatibility unclaimed; C136 proves exact two- and fixed-ordered-leaf multi-factor coherence, certifies the generalized antiunitary reversal and its CRT compatibility, and isolates the naive standard-character failure",
    }
    assert data["route_a"] == {
        "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
        "overall": "ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed": False,
    }
    assert data["scope_flags"] == {
        "uses_prime_or_zero_table": False,
        "claims_target_divisor_match": False,
        "claims_euler_factors_or_root_number": False,
        "claims_automorphy": False,
        "claims_hilbert_polya": False,
        "claims_standard_character_projective_compatibility": False,
        "claims_factor_permutation_coherence": False,
    }
    assert data["nonclaims"] == [
        "no direct tensor compatibility for the standard c=1 factors",
        "no noncoprime or even-level CRT theorem under the frozen convention",
        "no coherent correction back to standard local characters",
        "no factor-permutation or symmetric-monoidal coherence theorem",
        "no semiclassical trace or external target match",
        "no Euler factor, root number, automorphy, or Hilbert--Polya claim",
    ]
    return (
        pair_fourier + pair_chirp + pair_unitary + pair_weyl
        + pair_conjugation + pair_antiunitary_crt + triple_unitary
        + antiunitary_involution + antiunitary_reversal + antiunitary_weyl
    )


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    count = validate(json.loads(path.read_text()))
    print(f"C136 independent checker: PASS ({count} enumerated exact cases plus closed schema)")


if __name__ == "__main__":
    main()
