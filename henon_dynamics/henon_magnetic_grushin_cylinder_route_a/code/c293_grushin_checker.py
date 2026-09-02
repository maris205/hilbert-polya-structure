#!/usr/bin/env python3
"""Strict producer-independent checker for HCS-C293.

Heat cells are reconstructed by summing individual Fourier--Hermite levels,
not by using the producer's hyperbolic-sine channel formula.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c293_grushin_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C293/2026-09-02.yaml"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION_SHA = "e3ff56c62d1830a03a8a0b2a7d33acf73d6d997de4d9c872e6f6ff278d98adae"

MODEL = {
    "space": "L2(R_x times S1_theta, dx dtheta/(2pi))",
    "form": "q_alpha[u]=integral(|partial_x u|^2+x^2|(-i partial_theta+alpha)u|^2)",
    "realization": "nonnegative closed-form Friedrichs realization; essential self-adjointness is not claimed",
    "channels": "theta-Fourier mode k gives -d_x^2+(k+alpha)^2 x^2",
    "flux": "alpha is real modulo integer gauge shifts",
}
THEOREM = {
    "realization": "the closed nonnegative quadratic form defines a unique Friedrichs self-adjoint operator G_alpha",
    "noninteger": "for alpha outside Z the resolvent is compact and the spectrum is pure point lambda_(k,n)=(2n+1)|k+alpha|",
    "integer": "for alpha in Z exactly one resonant Fourier channel has absolutely continuous spectrum [0,infinity) of almost-everywhere multiplicity two, the singular-continuous spectrum is empty, and positive-integer oscillator eigenvalues remain embedded",
    "nonresonant": "after deleting the integer-flux free channel the resolvent is compact and eigenvalue N has multiplicity 2 d_odd(N)",
    "heat": "Tr exp(-t G_alpha)=sum_k 1/(2 sinh(t|k+alpha|)) off integer flux and Tr_perp=sum_(m>=1)1/sinh(tm) at integer flux",
    "source_zeta": "the zero-flux nonresonant spectral zeta is 2(1-2^(-s)) zeta(s)^2 for Re(s)>1",
    "weyl": "N_perp(Lambda)=2 sum_(j odd) floor(Lambda/j)=Lambda log Lambda+(2 gamma+log 2-1)Lambda+O(sqrt Lambda)",
    "boundary": "integer/noninteger flux, half-flux pairing, rational/irrational coincidences, and divergence on approach to resonance are explicit",
}
PROOF = {
    "form": "close the densely defined nonnegative form and use the representation theorem rather than asserting essential self-adjointness",
    "decomposition": "unitary Fourier expansion gives an orthogonal direct sum of one-dimensional channel forms",
    "oscillator": "Hermite scaling gives eigenvalues (2n+1)|k+alpha| whenever k+alpha is nonzero",
    "compactness": "off resonance only finitely many channel-level pairs lie below any energy bound",
    "integer_type": "the resonant block is the free line Laplacian while the orthogonal oscillator sum has compact resolvent, so absolutely continuous and embedded point parts coexist and no singular-continuous part occurs",
    "trace_zeta": "positive-term summation of channel heat traces and Mellin sums yields the displayed source-local series",
    "weyl": "d_odd(N)=d(N)-d(N/2) reduces the count to the elementary divisor summatory formula",
    "finite_role": "finite exact cells audit channel indexing, multiplicity, trace, and counting constants but do not prove the operator theorem",
}
ROUTE = {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
FLAGS = {"arithmetic_local_data": False, "euler_factors": False, "root_numbers": False, "automorphy": False, "target_divisor_or_counting_law": False, "target_functional_equation": False, "target_zero_match": False, "hilbert_polya_operator": False, "route_b_input": False}
INTEGER_SPECTRUM = {
    "absolutely_continuous_spectrum": "[0,infinity) from exactly one free Fourier channel",
    "absolutely_continuous_multiplicity": 2,
    "point_spectrum": "every positive integer, embedded in [0,infinity)",
    "singular_continuous_spectrum_empty": True,
    "nonresonant_compact_resolvent": True,
}
TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "model", "theorem_contract", "proof_contract", "route_a", "scope_flags", "enumeration", "spectral_cells", "heat_cells", "integer_heat_cells", "multiplicity_cells", "counting_cells", "zeta_cells", "symmetry_cells", "integer_spectrum", "references", "nonclaims", "payload_sha256"}
ENUM_KEYS = {"noninteger_fluxes", "k_values", "n_values", "spectral_cells", "heat_cells", "integer_heat_cells", "multiplicity_cells", "counting_cells", "zeta_cells", "symmetry_cells"}
SPEC_KEYS = {"alpha", "k", "n", "frequency", "eigenvalue"}
HEAT_KEYS = {"alpha", "t", "trace", "k_cutoff"}
IHEAT_KEYS = {"t", "nonresonant_trace", "mode_cutoff"}
MULT_KEYS = {"N", "odd_divisor_count", "multiplicity"}
COUNT_KEYS = {"Lambda", "exact_count", "normalized_by_Lambda_log_Lambda"}
ZETA_KEYS = {"s", "value"}
SYM_KEYS = {"alpha", "fundamental_distance", "ground_energy", "integer_flux", "half_flux_pairing"}
REF_KEYS = {"id", "authors", "title", "venue", "identifier", "url", "ownership"}
DECIMAL_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?$")
EVALUATION_EXPECTED = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C293",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": 1788307200,
    "scope_literal": SCOPE,
    "evaluator_authority_sha256": EVALUATOR,
    "theorem_status": "PROVABLE AS STATED",
    "tuple": [
        "A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL",
        "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_NATURAL_QUANTIZATION",
    ],
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "axes": {
        "A0": "weak source-local coefficient relation only",
        "A1": "no primitive-orbit repetition bridge",
        "A2": "no arithmetic clock",
        "A3": "partial source-local meromorphic structure only",
        "A4": "natural Friedrichs quantization",
    },
    "scope_flags": FLAGS,
}


class Checks:
    def __init__(self) -> None: self.n = 0
    def ok(self, condition: bool, label: str) -> None:
        self.n += 1
        if not condition: raise AssertionError(label)


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out = {}
    for key, value in pairs:
        if key in out: raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def strict_load(path: Path) -> dict[str, Any]:
    def bad(token: str) -> None: raise ValueError(f"nonfinite JSON: {token}")
    value = json.loads(path.read_text(), object_pairs_hook=reject_duplicate_keys, parse_constant=bad)
    if type(value) is not dict: raise TypeError("top level must be object")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader with duplicate rejection and dates kept as strings."""


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    out: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in out
        except TypeError as error:
            raise yaml.constructor.ConstructorError(None, None, "unhashable YAML key", key_node.start_mark) from error
        if duplicate:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate YAML key: {key}", key_node.start_mark)
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def strict_yaml_load(path: Path) -> dict[str, Any]:
    value = yaml.load(path.read_text(), Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("evaluation YAML top level must be object")
    return value


def semantic_hash(value: dict[str, Any]) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def phash(data: dict[str, Any]) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def keys(c: Checks, value: Any, expected: set[str], label: str) -> None:
    c.ok(type(value) is dict, f"{label} object"); c.ok(set(value) == expected, f"{label} keys")


def typ(c: Checks, value: Any, expected: type, label: str) -> None: c.ok(type(value) is expected, f"{label} exact type")


def require(value: Any, expected: type, label: str) -> None:
    if type(value) is not expected: raise TypeError(f"{label} exact type {expected.__name__}")


def exact_tree(c: Checks, value: Any, expected: Any, label: str) -> None:
    c.ok(type(value) is type(expected), f"{label} exact type")
    if type(expected) is dict:
        c.ok(set(value) == set(expected), f"{label} exact keys")
        for key in expected:
            exact_tree(c, value[key], expected[key], f"{label}.{key}")
    elif type(expected) is list:
        c.ok(len(value) == len(expected), f"{label} length")
        for index, item in enumerate(expected):
            exact_tree(c, value[index], item, f"{label}[{index}]")
    else:
        c.ok(value == expected, f"{label} value")


def frac(c: Checks, value: Any, label: str) -> Fraction:
    typ(c, value, str, label)
    try: out = Fraction(value)
    except (ValueError, ZeroDivisionError) as error: raise AssertionError(label) from error
    c.ok(str(out) == value, f"{label} canonical")
    return out


def decimal(c: Checks, value: Any, label: str) -> mp.mpf:
    typ(c, value, str, label); c.ok(DECIMAL_RE.fullmatch(value) is not None, f"{label} syntax")
    out = mp.mpf(value); c.ok(mp.isfinite(out), f"{label} finite")
    return out


def string_list(value: Any, label: str) -> list[str]:
    require(value, list, label)
    for i, item in enumerate(value): require(item, str, f"{label}[{i}]")
    return value


def int_list(value: Any, label: str) -> list[int]:
    require(value, list, label)
    for i, item in enumerate(value): require(item, int, f"{label}[{i}]")
    return value


def d_odd(n: int) -> int:
    return sum(n % d == 0 for d in range(1, n + 1, 2))


def direct_channel_trace(omega: mp.mpf, t: mp.mpf) -> mp.mpf:
    total = mp.mpf("0")
    n = 0
    while True:
        term = mp.exp(-t * (2 * n + 1) * omega)
        total += term
        if term < mp.mpf("1e-65"):
            return total
        n += 1
        if n > 10000: raise RuntimeError("trace failed to converge")


def reduce_flux(alpha: Fraction) -> Fraction:
    remainder = alpha - alpha.numerator // alpha.denominator
    return min(remainder, 1 - remainder)


def main() -> None:
    mp.mp.dps = 80
    parser = argparse.ArgumentParser(); parser.add_argument("input", nargs="?", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args(); data = strict_load(args.input); c = Checks()
    evaluation = strict_yaml_load(args.evaluation)
    exact_tree(c, evaluation, EVALUATION_EXPECTED, "evaluation")
    c.ok(semantic_hash(evaluation) == EVALUATION_SHA, "evaluation semantic hash")
    keys(c, data, TOP_KEYS, "top")
    typ(c, data["payload_sha256"], str, "payload hash"); c.ok(re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "hash syntax"); c.ok(data["payload_sha256"] == phash(data), "payload hash")
    for field, expected in (("schema", "hcs-c293-magnetic-grushin-cylinder-v1"), ("candidate_id", "HCS-C293"), ("evaluation_date", "2026-09-02"), ("source_commit", SOURCE), ("scope_literal", SCOPE)):
        typ(c, data[field], str, field); c.ok(data[field] == expected, f"{field} value")
    typ(c, data["fixed_epoch"], int, "epoch"); c.ok(data["fixed_epoch"] == 1788307200, "epoch value")
    keys(c, data["evaluator"], {"version", "sha256"}, "evaluator")
    require(data["evaluator"]["version"], str, "evaluator version"); require(data["evaluator"]["sha256"], str, "evaluator hash")
    c.ok(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator value")
    for label, value, expected in (("model", data["model"], MODEL), ("theorem", data["theorem_contract"], THEOREM), ("proof", data["proof_contract"], PROOF)):
        keys(c, value, set(expected), label)
        for key, item in value.items(): require(item, str, f"{label}.{key}")
        c.ok(value == expected, f"{label} contract")
    keys(c, data["route_a"], set(ROUTE), "route"); string_list(data["route_a"]["tuple"], "route tuple")
    require(data["route_a"]["overall"], str, "route overall"); require(data["route_a"]["route_b_invocation_allowed"], bool, "route B")
    c.ok(data["route_a"] == ROUTE, "route value")
    keys(c, data["scope_flags"], set(FLAGS), "flags")
    for key, value in data["scope_flags"].items(): require(value, bool, f"flag {key}")
    c.ok(data["scope_flags"] == FLAGS, "flag values")
    keys(c, data["enumeration"], ENUM_KEYS, "enumeration")
    fluxes = [frac(c, value, "enumeration flux") for value in string_list(data["enumeration"]["noninteger_fluxes"], "fluxes")]
    k_values = int_list(data["enumeration"]["k_values"], "k values"); n_values = int_list(data["enumeration"]["n_values"], "n values")
    for key in ENUM_KEYS - {"noninteger_fluxes", "k_values", "n_values"}: require(data["enumeration"][key], int, f"enumeration {key}")
    c.ok(fluxes == [Fraction(1, 3), Fraction(1, 2), Fraction(2, 5)], "flux grid"); c.ok(k_values == list(range(-5, 6)), "k grid"); c.ok(n_values == list(range(5)), "n grid")

    require(data["spectral_cells"], list, "spectral cells"); expected_spec = []
    for alpha in fluxes:
        for k in k_values:
            for n in n_values:
                omega = abs(Fraction(k) + alpha)
                expected_spec.append({"alpha": str(alpha), "k": k, "n": n, "frequency": str(omega), "eigenvalue": str((2*n+1)*omega)})
    for i, row in enumerate(data["spectral_cells"]):
        keys(c, row, SPEC_KEYS, f"spectral {i}"); frac(c, row["alpha"], "spectral alpha"); frac(c, row["frequency"], "frequency"); frac(c, row["eigenvalue"], "eigenvalue")
        require(row["k"], int, "spectral k"); require(row["n"], int, "spectral n")
    c.ok(data["spectral_cells"] == expected_spec, "all channel eigenvalues")
    c.ok(len({(r["alpha"], r["k"], r["n"]) for r in data["spectral_cells"]}) == len(expected_spec), "unique spectral grid")

    require(data["heat_cells"], list, "heat cells"); heat_grid = set()
    for i, row in enumerate(data["heat_cells"]):
        keys(c, row, HEAT_KEYS, f"heat {i}"); alpha = frac(c, row["alpha"], "heat alpha"); t = decimal(c, row["t"], "heat t"); reported = decimal(c, row["trace"], "heat trace")
        require(row["k_cutoff"], int, "k cutoff"); c.ok(row["k_cutoff"] == 500, "k cutoff value")
        heat_grid.add((row["alpha"], row["t"]))
        direct = mp.fsum(direct_channel_trace(abs(mp.mpf(alpha.numerator)/alpha.denominator + k), t) for k in range(-row["k_cutoff"], row["k_cutoff"] + 1))
        c.ok(abs(direct - reported) < mp.mpf("1e-40"), "direct Fourier-Hermite heat reconstruction")
    c.ok(heat_grid == {(str(a), t) for a in fluxes for t in ("0.25", "0.5", "1.0")}, "complete heat grid")

    require(data["integer_heat_cells"], list, "integer heat"); integer_times = set()
    for i, row in enumerate(data["integer_heat_cells"]):
        keys(c, row, IHEAT_KEYS, f"integer heat {i}"); t = decimal(c, row["t"], "integer heat t"); reported = decimal(c, row["nonresonant_trace"], "integer trace")
        require(row["mode_cutoff"], int, "mode cutoff"); c.ok(row["mode_cutoff"] == 500, "mode cutoff value")
        integer_times.add(row["t"])
        direct = 2 * mp.fsum(direct_channel_trace(mp.mpf(k), t) for k in range(1, row["mode_cutoff"] + 1))
        c.ok(abs(direct - reported) < mp.mpf("1e-40"), "direct nonresonant heat reconstruction")
    c.ok(integer_times == {"0.25", "0.5", "1.0"}, "integer heat grid")

    require(data["multiplicity_cells"], list, "multiplicity cells")
    for i, row in enumerate(data["multiplicity_cells"], 1):
        keys(c, row, MULT_KEYS, f"multiplicity {i}")
        for field in MULT_KEYS: require(row[field], int, f"multiplicity {field}")
        c.ok(row == {"N": i, "odd_divisor_count": d_odd(i), "multiplicity": 2*d_odd(i)}, "multiplicity enumeration")

    require(data["counting_cells"], list, "counting cells"); limits = []
    for i, row in enumerate(data["counting_cells"]):
        keys(c, row, COUNT_KEYS, f"count {i}"); require(row["Lambda"], int, "Lambda"); require(row["exact_count"], int, "exact count")
        ratio = decimal(c, row["normalized_by_Lambda_log_Lambda"], "count ratio"); limit = row["Lambda"]; limits.append(limit)
        exact = 2 * sum(limit // j for j in range(1, limit + 1, 2))
        c.ok(row["exact_count"] == exact == sum(2*d_odd(n) for n in range(1, limit+1)), "two count routes")
        c.ok(abs(ratio - exact/(mp.mpf(limit)*mp.log(limit))) < mp.mpf("1e-40"), "count ratio")
    c.ok(limits == [8,16,32,64,128,256], "count grid")

    require(data["zeta_cells"], list, "zeta cells"); zeta_grid = []
    for i, row in enumerate(data["zeta_cells"]):
        keys(c, row, ZETA_KEYS, f"zeta {i}"); require(row["s"], int, "zeta s"); value = decimal(c, row["value"], "zeta value"); s = row["s"]; zeta_grid.append(s)
        odd_level_sum = mp.nsum(lambda n: mp.power(2*n+1, -s), [0, mp.inf])
        channel_sum = mp.nsum(lambda k: mp.power(k, -s), [1, mp.inf])
        c.ok(abs(value - 2*odd_level_sum*channel_sum) < mp.mpf("1e-40"), "direct double-index zeta")
    c.ok(zeta_grid == [3,4,5,6], "zeta grid")

    require(data["symmetry_cells"], list, "symmetry cells"); seen = set()
    for i, row in enumerate(data["symmetry_cells"]):
        keys(c, row, SYM_KEYS, f"symmetry {i}"); alpha = frac(c, row["alpha"], "symmetry alpha"); distance = frac(c, row["fundamental_distance"], "distance"); ground = frac(c, row["ground_energy"], "ground")
        require(row["integer_flux"], bool, "integer flag"); require(row["half_flux_pairing"], bool, "half flag")
        expected = reduce_flux(alpha); c.ok(distance == ground == expected, "flux reduction"); c.ok(row["integer_flux"] is (expected == 0), "integer flag value"); c.ok(row["half_flux_pairing"] is (expected == Fraction(1,2)), "half flag value")
        seen.add(row["alpha"])
    c.ok(len(seen) == len(data["symmetry_cells"]) == 10, "unique symmetry grid")

    keys(c, data["integer_spectrum"], set(INTEGER_SPECTRUM), "integer spectrum")
    require(data["integer_spectrum"]["absolutely_continuous_spectrum"], str, "ac spectrum"); require(data["integer_spectrum"]["absolutely_continuous_multiplicity"], int, "ac multiplicity"); require(data["integer_spectrum"]["point_spectrum"], str, "point spectrum")
    require(data["integer_spectrum"]["singular_continuous_spectrum_empty"], bool, "sc flag"); require(data["integer_spectrum"]["nonresonant_compact_resolvent"], bool, "nonres compact")
    c.ok(data["integer_spectrum"] == INTEGER_SPECTRUM, "integer full spectral type")

    expected_enum = {"noninteger_fluxes": [str(a) for a in fluxes], "k_values": k_values, "n_values": n_values, "spectral_cells": len(data["spectral_cells"]), "heat_cells": len(data["heat_cells"]), "integer_heat_cells": len(data["integer_heat_cells"]), "multiplicity_cells": len(data["multiplicity_cells"]), "counting_cells": len(data["counting_cells"]), "zeta_cells": len(data["zeta_cells"]), "symmetry_cells": len(data["symmetry_cells"])}
    c.ok(data["enumeration"] == expected_enum, "enumeration value")
    require(data["references"], list, "references"); c.ok(len(data["references"]) == 2, "reference count")
    for i, row in enumerate(data["references"]):
        keys(c, row, REF_KEYS, f"reference {i}")
        for key, value in row.items(): require(value, str, f"reference {i}.{key}")
    c.ok([r["identifier"] for r in data["references"]] == ["arXiv:1406.6578", "arXiv:2312.04359"], "reference identities")
    string_list(data["nonclaims"], "nonclaims"); c.ok(len(data["nonclaims"]) == 3, "nonclaim count")
    print(
        f"C293 independent Fourier-Hermite checker: PASS ({c.n} assertions; "
        f"strict duplicate-rejecting JSON/YAML schemas; evaluation-semantic-sha256={EVALUATION_SHA})"
    )


if __name__ == "__main__":
    main()
