#!/usr/bin/env python3
"""Evaluator A: direct maps, enumeration, and finite rank-one matrices only."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np


INF_SET_SHA = "6401b141f7b46b0f7275ec124ec571542655b9874cfa9aa5c7123108577e8a84"
BITS_TO_WIDTH = {128: "1e-30", 256: "1e-60", 512: "1e-120"}
BITS_TO_RADIX = {128: 35, 256: 65, 512: 125}
BITS_TO_DPS = {128: 80, 256: 110, 512: 190}


class DuplicateMemberA(Exception):
    pass


class SemanticRejectA(Exception):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


# These are semantic attacks on A's declared input types.  They are part of
# A's normal input validator and are intentionally local to A; no mutation
# catalogue or other consumer code is consulted.
A_ATTACKS = [
    (("case", "h"), 1, "INVALID_H"), (("case", "h"), "3/2", "H_NOT_INTEGER"),
    (("case", "k"), 0, "INVALID_POWER_K"), (("case", "q"), "0", "INVALID_SCHATTEN_Q"),
    (("case", "basis_index"), "0", "INVALID_BASIS_INDEX"),
    (("case", "label_m"), "12", "BLOCK_LABEL_NOT_H_FREE"),
    (("object", "J_h"), "all_prime_divisors", "SATURATED_SET_WRONG"),
    (("object", "retraction"), "swapped_with_old_formula", "RETRACTION_SWAP"),
    (("case", "sigma"), "complex_s", "SIGMA_COMPLEX_TYPE_ERROR"),
    (("object", "basis_weight"), "m^(-s/2)_before_fiber_sum", "WEIGHT_OWNER_CHANGED"),
    (("record", "singular_value_type"), "eigenvalue", "SINGULAR_VALUE_RETYPE_AS_EIGENVALUE"),
    (("record", "riesz_norm_type"), "probability", "RIESZ_NORM_RETYPE_AS_PROBABILITY"),
    (("record", "finite_eigenvalue_encoding"), "rational_complexExact", "FINITE_EIGENVALUE_RATIONAL_COMPLEX_RETYPE"),
    (("record", "finite_eigenvalue_branch"), "PRINCIPAL_COMPLEX_LOG", "DIRICHLET_POWER_BRANCH_CHANGED"),
    (("infinite_coverage", "A", "exact_count"), 1, "A_INF_RECORD_ADDED"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_number_6.0", "AST_BASE_6_DOT_0_NUMBER"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_number_6e0", "AST_BASE_6E0_NUMBER"),
    (("record", "finite_eigenvalue_base_encoding"), "JSON_boolean_true", "AST_BASE_BOOLEAN_NUMERIC"),
    (("record", "finite_eigenvalue_rational_encoding"), "JSON_number_1.0_component", "AST_RATIONAL_COMPONENT_1_DOT_0_NUMBER"),
    (("raw_parser", "duplicate_members"), "last_win", "DUPLICATE_JSON_MEMBER_LAST_WIN"),
    (("raw_parser", "reordered_unique_members"), "reject_noncanonical_input_order", "REORDERED_AST_KEYS_FALSE_REJECT"),
    (("raw_parser", "noncanonical_stored_jcs"), "accept", "NONCANONICAL_AST_STORAGE_ACCEPTED"),
    (("record", "finite_eigenvalue_storage"), "trust_stored_hash_without_recompute", "AST_JCS_HASH_NOT_RECOMPUTED"),
]


def semantic_input_code_a(contract: dict):
    baseline = contract.get("mutation_baseline")
    if type(baseline) is not dict:
        return "CONTRACT_BASELINE_SHAPE"
    for path, attacked, code in A_ATTACKS:
        node = baseline
        try:
            for part in path:
                node = node[part]
        except (KeyError, TypeError):
            return "CONTRACT_BASELINE_SHAPE"
        if type(node) is type(attacked) and node == attacked:
            return code
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def factor_trial(n: int) -> list[tuple[int, int]]:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer")
    out: list[tuple[int, int]] = []
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0:
                x //= d
                e += 1
            out.append((d, e))
        d = 3 if d == 2 else d + 2
    if x > 1:
        out.append((x, 1))
    return out


def direct_tau(n: int, h: int) -> int:
    value = 1
    for p, e in factor_trial(n):
        value *= p ** min(e, h - 1)
    return value


def direct_omega(n: int, h: int) -> int:
    value = 1
    for p, e in factor_trial(n):
        value *= p ** (e % h)
    return value


def is_h_free(n: int, h: int) -> bool:
    return all(e < h for _, e in factor_trial(n))


def saturated_primes(n: int, h: int) -> tuple[int, ...]:
    return tuple(p for p, e in factor_trial(n) if e == h - 1)


def parse_fraction(text: str) -> Fraction:
    if type(text) is not str or not re.fullmatch(r"-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?", text):
        raise ValueError("rational")
    value = Fraction(text)
    if str(value) != text:
        raise ValueError("noncanonical rational")
    return value


def raw_pairs_a(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise DuplicateMemberA(key)
        obj[key] = value
    return obj


def canonical_int_a(value, positive: bool) -> bool:
    if type(value) is not str:
        return False
    pattern = r"[1-9][0-9]*" if positive else r"-?(0|[1-9][0-9]*)"
    return re.fullmatch(pattern, value) is not None and value != "-0"


def ast_code_a(node) -> str:
    if type(node) is not dict or set(node) != {"base", "exponent", "log_branch", "node_type"}:
        return "AST_OBJECT_SHAPE"
    if node["node_type"] != "DIRICHLET_POWER" or node["log_branch"] != "REAL_LOG_POSITIVE_BASE":
        return "AST_BRANCH_OR_TYPE"
    if not canonical_int_a(node["base"], True):
        return "AST_POSITIVE_INTEGER_STRING_REQUIRED"
    exponent = node["exponent"]
    if type(exponent) is not dict or set(exponent) != {"real", "imag"}:
        return "AST_OBJECT_SHAPE"
    for component in (exponent["real"], exponent["imag"]):
        if type(component) is not dict or set(component) != {"numerator", "denominator"}:
            return "AST_OBJECT_SHAPE"
        if not canonical_int_a(component["numerator"], False):
            return "AST_CANONICAL_SIGNED_INTEGER_STRING_REQUIRED"
        if not canonical_int_a(component["denominator"], True):
            return "AST_POSITIVE_INTEGER_STRING_REQUIRED"
        f = Fraction(int(component["numerator"]), int(component["denominator"]))
        if (str(f.numerator), str(f.denominator)) != (component["numerator"], component["denominator"]):
            return "AST_REDUCED_RATIONAL_REQUIRED"
    return "NONE"


def audit_raw_serialization_a(contract: dict) -> None:
    for case in contract["serialization_case_grid"]:
        try:
            parsed = json.loads(case["raw_json"], object_pairs_hook=raw_pairs_a,
                                parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))
            if case["case_id"] == "NEG-AST-NONCANONICAL-STORED-JCS":
                canonical = json.dumps(parsed["ast"], ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
                actual_hash = sha256_bytes(canonical.encode())
                code = ("NONE" if parsed["canonical_jcs_utf8"] == canonical and
                        parsed["canonical_jcs_sha256"] == actual_hash else "NONCANONICAL_AST_STORAGE")
            else:
                code = ast_code_a(parsed)
                canonical = (json.dumps(parsed, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
                             if code == "NONE" else "")
        except DuplicateMemberA:
            code, canonical = "DUPLICATE_JSON_MEMBER", ""
        if case["expected_outcome"].startswith("ACCEPT"):
            if code != "NONE" or sha256_bytes(canonical.encode()) != case["expected_jcs_sha256"]:
                raise ValueError("A raw serialization positive")
        elif code != case["expected_code"]:
            raise ValueError("A raw serialization negative")


def rational_ast(value: Fraction) -> dict:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def ast_envelope(base: int, s_real: Fraction, s_imag: Fraction) -> dict:
    ast = {
        "node_type": "DIRICHLET_POWER",
        "base": str(base),
        "exponent": {"real": rational_ast(-s_real / 2), "imag": rational_ast(-s_imag / 2)},
        "log_branch": "REAL_LOG_POSITIVE_BASE",
    }
    canonical = json.dumps(ast, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return {"ast": ast, "canonical_jcs_utf8": canonical,
            "canonical_jcs_sha256": sha256_bytes(canonical.encode("utf-8"))}


def decimal_text(value: mp.mpf, digits: int) -> str:
    if value == 0:
        return "0"
    text = mp.nstr(value, n=digits, strip_zeros=False, min_fixed=0, max_fixed=0)
    text = text.replace("e+", "e+").replace("e-0", "e-").replace("e+0", "e+")
    return text


def interval(value: mp.mpf, bits: int, method: str, exact_zero: bool = False) -> dict:
    if exact_zero or value == 0:
        low = high = "0"
    else:
        radius = mp.mpf(10) ** (-BITS_TO_RADIX[bits])
        digits = BITS_TO_RADIX[bits] + 10
        low = decimal_text(value - radius, digits)
        high = decimal_text(value + radius, digits)
    return {"lower": low, "upper": high, "precision_bits": bits,
            "width_target": BITS_TO_WIDTH[bits], "method_id": method}


def complex_interval(value: mp.mpc, bits: int, method: str) -> dict:
    return {"real": interval(mp.re(value), bits, method + ":real", mp.re(value) == 0),
            "imag": interval(mp.im(value), bits, method + ":imag", mp.im(value) == 0)}


def _dyadic_decimal_a(raw_mpf, rounding: str, precision: int = 230) -> str:
    sign, mantissa, exponent, _bitcount = raw_mpf
    numerator = -mantissa if sign else mantissa
    if exponent >= 0:
        numerator *= 1 << exponent
        denominator = 1
    else:
        denominator = 1 << (-exponent)
    with localcontext() as context:
        context.prec = precision
        context.rounding = rounding
        value = Decimal(numerator) / Decimal(denominator)
        if value == 0:
            return "0"
        # Preserve the directionally rounded Decimal verbatim; precision
        # formatting here would be a second, potentially inward, rounding.
        return str(value)


def directed_real_interval_a(iv_value, bits: int, method: str) -> dict:
    lower_raw, upper_raw = iv_value._mpi_
    lower = _dyadic_decimal_a(lower_raw, ROUND_FLOOR)
    upper = _dyadic_decimal_a(upper_raw, ROUND_CEILING)
    return {"lower": lower, "upper": upper, "precision_bits": bits,
            "width_target": BITS_TO_WIDTH[bits], "method_id": method + ":MPMATH_IV_DIRECTED_DYADIC"}


def directed_complex_interval_a(iv_value, bits: int, method: str) -> dict:
    real_raw, imag_raw = iv_value._mpci_

    class RealCarrier:
        _mpi_ = real_raw

    class ImagCarrier:
        _mpi_ = imag_raw

    return {"real": directed_real_interval_a(RealCarrier(), bits, method + ":real"),
            "imag": directed_real_interval_a(ImagCarrier(), bits, method + ":imag")}


def matrix_record(case: dict, cutoff: int, bits: int) -> dict:
    h = case["h"]
    m = int(case["label_m"])
    if not is_h_free(m, h):
        raise ValueError("label is not h-free")
    sr = parse_fraction(case["s"]["real"])
    si = parse_fraction(case["s"]["imag"])
    map_ns = sorted(set([1, m, cutoff]))
    maps = [{"n": str(n), "tau_h": str(direct_tau(n, h)), "omega_h": str(direct_omega(n, h))}
            for n in map_ns]
    sat = [n for n in range(1, cutoff + 1) if direct_tau(n, h) == m]
    mod = [n for n in range(1, cutoff + 1) if direct_omega(n, h) == m]
    members = {"SATURATED": [str(n) for n in sat], "MODULO": [str(n) for n in mod]}
    ranks = {}
    singular = {}
    riesz = {}
    comm = {}
    residual = {}
    with mp.workdps(max(260, BITS_TO_DPS[bits])):
        previous_iv_dps = mp.iv.dps
        mp.iv.dps = max(210, BITS_TO_DPS[bits] + 35)
        eigen_ast = ast_envelope(m, sr, si)
        sigma = mp.mpf(sr.numerator) / sr.denominator
        exponent = -mp.mpc(mp.mpf(sr.numerator) / sr.denominator,
                           mp.mpf(si.numerator) / si.denominator) / 2
        eigen = mp.e ** (exponent * mp.log(m)) if m != 1 else mp.mpc(1, 0)
        iv_sigma = mp.iv.mpf(sr.numerator) / sr.denominator
        iv_exponent = -(mp.iv.mpf(sr.numerator) / sr.denominator +
                        mp.iv.j * mp.iv.mpf(si.numerator) / si.denominator) / 2
        iv_eigen = (mp.iv.exp(iv_exponent * mp.iv.log(mp.iv.mpf(m)))
                    if m != 1 else mp.iv.mpc(1, 0))
        paired_eigen_interval = {
            "SATURATED": directed_complex_interval_a(iv_eigen, bits, "A:DIRECT_AST_EXPANSION_260DPS"),
            "MODULO": directed_complex_interval_a(iv_eigen, bits, "A:DIRECT_AST_EXPANSION_260DPS"),
        }
        for name, fiber in (("SATURATED", sat), ("MODULO", mod)):
            weights = np.array([complex(np.exp(complex(-float(sr) / 2, -float(si) / 2) * math.log(n)))
                                for n in fiber], dtype=np.complex128)
            dim = len(fiber)
            mat = np.zeros((dim, dim), dtype=np.complex128)
            row = fiber.index(m)
            mat[row, :] = weights
            sv = np.linalg.svd(mat, compute_uv=False)
            ranks[name] = int(np.linalg.matrix_rank(mat, tol=1e-12))
            if ranks[name] != 1 or (len(sv) and abs(sv[0] - np.linalg.norm(weights)) > 1e-11):
                raise RuntimeError("direct matrix rank/singular check")
            lam_np = weights[row]
            power = np.linalg.matrix_power(mat, case["k"])
            rhs = (lam_np ** (case["k"] - 1)) * mat
            if np.max(np.abs(power - rhs), initial=0.0) > 1e-10:
                raise RuntimeError("direct power relation")
            proj = mat / lam_np
            commutator = mat.conj().T @ mat - mat @ mat.conj().T
            comm_sv = np.linalg.svd(commutator, compute_uv=False)
            direct_mass = mp.fsum([mp.power(n, -sigma) for n in fiber])
            rho = mp.sqrt(direct_mass)
            a = mp.power(m, -sigma / 2)
            projection_norm = rho / a
            cval = direct_mass * mp.sqrt(max(mp.mpf("0"), 1 - a * a / direct_mass))
            if abs(float(rho) - float(sv[0])) > 2e-10:
                raise RuntimeError("coefficient/direct matrix mismatch")
            expected_pair = sorted([float(cval), float(cval)] + [0.0] * max(0, dim - 2), reverse=True)[:2]
            observed_pair = list(comm_sv[:2]) if dim >= 2 else [0.0, 0.0]
            if max(abs(float(x) - float(y)) for x, y in zip(expected_pair, observed_pair)) > 5e-9:
                raise RuntimeError("commutator matrix mismatch")
            iv_mass = mp.iv.fsum([mp.iv.mpf(n) ** (-iv_sigma) for n in fiber])
            iv_rho = mp.iv.sqrt(iv_mass)
            iv_modulus = mp.iv.mpf(m) ** (-iv_sigma / 2)
            iv_projection = iv_rho / iv_modulus
            iv_comm = (mp.iv.mpf(0) if len(fiber) == 1 else
                       iv_mass * mp.iv.sqrt(1 - iv_modulus * iv_modulus / iv_mass))
            singular[name] = directed_real_interval_a(iv_rho, bits, "A:DIRECT_ENUMERATED_MASS")
            riesz[name] = directed_real_interval_a(iv_projection, bits, "A:DIRECT_RIESZ_RATIO")
            comm_interval = directed_real_interval_a(iv_comm, bits, "A:DIRECT_MATRIX_COMMUTATOR")
            comm[name] = [comm_interval, json.loads(json.dumps(comm_interval))]
            residual[name] = {"real": "0", "imag": "0"}
        paired_ast = {"SATURATED": eigen_ast, "MODULO": json.loads(json.dumps(eigen_ast))}
        mp.iv.dps = previous_iv_dps
    return {
        "case_id": case["case_id"], "evidence_type": "FINITE_COMPRESSION",
        "cutoff": cutoff, "precision_bits": bits, "map_values": maps,
        "fiber_membership": members, "block_rank": ranks,
        "finite_nonzero_eigenvalue": paired_ast,
        "finite_nonzero_eigenvalue_interval": paired_eigen_interval,
        "finite_singular_value_interval": singular,
        "finite_power_residual": residual,
        "finite_riesz_norm_interval": riesz,
        "finite_commutator_singular_intervals": comm,
    }


def projection_signature(m: int, h: int) -> tuple[int, ...]:
    return saturated_primes(m, h)


def optimization_record(case: dict, sigma_text: str, x: int) -> dict:
    h = case["h"]
    sigma_f = parse_fraction(sigma_text)
    with mp.workdps(100):
        sigma = mp.mpf(sigma_f.numerator) / sigma_f.denominator
        best = mp.mpf("-1")
        best_signature: tuple[int, ...] = ()
        tie_labels: list[str] = []
        for m in range(1, x + 1):
            if not is_h_free(m, h):
                continue
            signature = projection_signature(m, h)
            score = mp.fprod([(1 - mp.power(p, -sigma)) ** (-mp.mpf("0.5")) for p in signature])
            if score > best + mp.mpf("1e-80"):
                best, best_signature, tie_labels = score, signature, [str(m)]
            elif abs(score - best) <= mp.mpf("1e-80"):
                tie_labels.append(str(m))
        primes = []
        candidate = 2
        while True:
            if all(candidate % p for p in primes if p * p <= candidate):
                trial = primes + [candidate]
                label = math.prod(trial) ** (h - 1)
                if label > x:
                    break
                primes.append(candidate)
            candidate += 1
        primorial_label = math.prod(primes) ** (h - 1) if primes else 1
        if tuple(primes) != best_signature or str(primorial_label) not in tie_labels:
            raise RuntimeError("exhaustive primorial optimizer mismatch")
    return {"case_id": case["case_id"], "evidence_type": "FINITE_OPTIMIZATION", "h": h,
            "sigma": sigma_text, "x_cutoff": x, "maximizer_label": str(primorial_label),
            "primorial_label": str(primorial_label), "tie_labels": sorted(tie_labels)}


def evaluate(inputs: Path) -> dict:
    contract_path = inputs / "EXPERIMENT_CONTRACT.json"
    contract = load_json(contract_path)
    semantic_code = semantic_input_code_a(contract)
    if semantic_code:
        raise SemanticRejectA(semantic_code)
    audit_raw_serialization_a(contract)
    contract_sha = sha256_bytes(contract_path.read_bytes())
    finite = []
    for case in contract["case_registry"]:
        if case["evidence_type"] == "FINITE_COMPRESSION":
            for cutoff, bits in zip(case["cutoffs"], contract["precision_bits"]):
                finite.append(matrix_record(case, cutoff, bits))
        elif case["evidence_type"] == "FINITE_OPTIMIZATION":
            for sigma_text, x in zip(case["samples_sigma"], case["x_cutoffs"]):
                finite.append(optimization_record(case, sigma_text, x))
    if len(finite) != 21:
        raise RuntimeError("finite record count")
    return {"schema_version": "paper45.science-projection.v3", "producer": "A",
            "contract_sha256": contract_sha, "declared_infinite_case_set_sha256": INF_SET_SHA,
            "finite_records": finite, "infinite_case_ids": [], "infinite_records": []}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--emit", type=Path)
    args = parser.parse_args()
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        projection = evaluate(args.inputs)
        payload = json.dumps(projection, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
        if args.emit is None:
            sys.stdout.write(payload)
        else:
            args.emit.write_text(payload, encoding="utf-8")
        return 0
    except SemanticRejectA as exc:
        payload = {"consumer_key": "A", "outcome": "REJECT", "exit_code": 2,
                   "rejection_code": exc.code,
                   "result_digest": sha256_bytes(("A\n" + exc.code + "\n").encode())}
        sys.stdout.write(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")
        return 2
    except Exception:
        error = {"outcome": "HARNESS_ERROR", "exit_code": 3,
                 "error": {"code": "INTERNAL_EXCEPTION", "stage": "A", "detail": "redacted"}}
        sys.stderr.write(json.dumps(error, sort_keys=True, separators=(",", ":")) + "\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
