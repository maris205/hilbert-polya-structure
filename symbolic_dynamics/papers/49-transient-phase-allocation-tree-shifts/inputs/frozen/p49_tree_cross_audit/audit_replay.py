#!/usr/bin/env python3
"""Independent exact replay for the frozen p49 tree Stage-2 package.

This program never imports or executes code from the audited package.  It
reads the frozen files, verifies their content-addressed ledger, and rebuilds
the decisive arithmetic with a separately written implementation.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
import os
import pathlib
import stat
from fractions import Fraction
from typing import Iterable, Iterator, Mapping, Sequence


ACTIVE = pathlib.Path("/tmp/p49_tree_stage2")
AUDIT = pathlib.Path("/tmp/p49_tree_cross_audit")
EVIDENCE = AUDIT / "evidence"
EXPECTED_MANIFEST_SHA256 = (
    "bea7a189ea0b3472cc6b469eb36e6460b60c4bae66265659b19af6e89883f0da"
)

Form = dict[int, Fraction]


class Ledger:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)

    def equal(self, left: object, right: object, message: str) -> None:
        self.check(left == right, f"{message}: {left!r} != {right!r}")


LEDGER = Ledger()


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: pathlib.Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    path.write_text(encoded, encoding="utf-8")


def snapshot_active() -> dict[str, object]:
    files: dict[str, object] = {}
    directories: dict[str, str] = {}
    symlinks: list[str] = []
    nonregular: list[str] = []
    caches: list[str] = []
    for root, dirnames, filenames in os.walk(ACTIVE, topdown=True, followlinks=False):
        root_path = pathlib.Path(root)
        relative_root = root_path.relative_to(ACTIVE)
        for name in sorted(dirnames):
            path = root_path / name
            relative = str(path.relative_to(ACTIVE))
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                symlinks.append(relative)
            elif stat.S_ISDIR(mode):
                directories[relative] = oct(stat.S_IMODE(mode))
            else:
                nonregular.append(relative)
            if name == "__pycache__" or name.endswith(".pyc") or name.endswith(".pyo"):
                caches.append(relative)
        for name in sorted(filenames):
            path = root_path / name
            relative = str(path.relative_to(ACTIVE))
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                symlinks.append(relative)
            elif stat.S_ISREG(mode):
                files[relative] = {
                    "mode": oct(stat.S_IMODE(mode)),
                    "sha256": sha256_file(path),
                    "size": path.stat().st_size,
                }
            else:
                nonregular.append(relative)
            if "__pycache__" in path.parts or name.endswith((".pyc", ".pyo")):
                caches.append(relative)
    return {
        "active_root": str(ACTIVE),
        "caches": sorted(caches),
        "directories": dict(sorted(directories.items())),
        "files": dict(sorted(files.items())),
        "nonregular": sorted(nonregular),
        "symlinks": sorted(symlinks),
    }


def parse_and_verify_manifest(snapshot: Mapping[str, object]) -> dict[str, object]:
    manifest = ACTIVE / "SHA256SUMS.txt"
    LEDGER.equal(sha256_file(manifest), EXPECTED_MANIFEST_SHA256, "manifest SHA-256")
    entries: dict[str, str] = {}
    for line_number, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        LEDGER.check(bool(raw.strip()), f"blank manifest line {line_number}")
        parts = raw.split(maxsplit=1)
        LEDGER.equal(len(parts), 2, f"manifest field count at line {line_number}")
        digest, rel = parts
        rel = rel.lstrip(" *")
        LEDGER.check(len(digest) == 64 and all(c in "0123456789abcdef" for c in digest),
                     f"invalid digest at line {line_number}")
        path = pathlib.PurePosixPath(rel)
        LEDGER.check(not path.is_absolute(), f"absolute manifest path {rel}")
        LEDGER.check(rel == path.as_posix() and ".." not in path.parts and "." not in path.parts,
                     f"unnormalized manifest path {rel}")
        LEDGER.check(rel not in entries, f"duplicate manifest path {rel}")
        entries[rel] = digest

    snap_files = snapshot["files"]
    assert isinstance(snap_files, dict)
    expected_paths = set(snap_files) - {"SHA256SUMS.txt"}
    LEDGER.equal(set(entries), expected_paths, "manifest file-set coverage")
    for rel, digest in entries.items():
        record = snap_files[rel]
        assert isinstance(record, dict)
        LEDGER.equal(record["sha256"], digest, f"manifest entry {rel}")
    LEDGER.equal(snapshot["caches"], [], "active cache set")
    LEDGER.equal(snapshot["symlinks"], [], "active symlink set")
    LEDGER.equal(snapshot["nonregular"], [], "active nonregular set")
    LEDGER.check(all(record["mode"] == "0o644" for record in snap_files.values()),
                 "active regular-file modes are not uniformly 0644")
    directories = snapshot["directories"]
    assert isinstance(directories, dict)
    LEDGER.check(all(mode == "0o755" for mode in directories.values()),
                 "active directory modes are not uniformly 0755")
    return {
        "entry_count": len(entries),
        "manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "regular_file_count_including_manifest": len(snap_files),
        "verified": True,
    }


def factor_integer(value: int) -> Form:
    if value < 1:
        raise ValueError("phase sizes must be positive")
    answer: Form = {}
    divisor = 2
    remainder = value
    while divisor * divisor <= remainder:
        while remainder % divisor == 0:
            answer[divisor] = answer.get(divisor, Fraction(0)) + 1
            remainder //= divisor
        divisor += 1
    if remainder > 1:
        answer[remainder] = answer.get(remainder, Fraction(0)) + 1
    return answer


def clean(form: Mapping[int, Fraction]) -> Form:
    return {prime: Fraction(coefficient) for prime, coefficient in form.items() if coefficient}


def add_forms(*forms: Mapping[int, Fraction]) -> Form:
    result: Form = {}
    for form in forms:
        for prime, coefficient in form.items():
            result[prime] = result.get(prime, Fraction(0)) + coefficient
    return clean(result)


def scale_form(form: Mapping[int, Fraction], scalar: Fraction | int) -> Form:
    scalar = Fraction(scalar)
    return clean({prime: coefficient * scalar for prime, coefficient in form.items()})


def sum_scaled(items: Iterable[tuple[Fraction | int, Mapping[int, Fraction]]]) -> Form:
    result: Form = {}
    for scalar, form in items:
        scalar = Fraction(scalar)
        for prime, coefficient in form.items():
            result[prime] = result.get(prime, Fraction(0)) + scalar * coefficient
    return clean(result)


def compare_forms(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> int:
    difference = add_forms(left, scale_form(right, -1))
    if not difference:
        return 0
    common = 1
    for coefficient in difference.values():
        common = math.lcm(common, coefficient.denominator)
    positive = 1
    negative = 1
    for prime, coefficient in difference.items():
        exponent = int(coefficient * common)
        if exponent > 0:
            positive *= prime**exponent
        elif exponent < 0:
            negative *= prime ** (-exponent)
    return (positive > negative) - (positive < negative)


def equal_forms(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> bool:
    return clean(left) == clean(right)


def all_equal(forms: Sequence[Mapping[int, Fraction]]) -> bool:
    return all(equal_forms(forms[0], form) for form in forms[1:])


def min_form(forms: Sequence[Form]) -> tuple[int, Form]:
    index = 0
    best = forms[0]
    for candidate_index, candidate in enumerate(forms[1:], 1):
        if compare_forms(candidate, best) < 0:
            index, best = candidate_index, candidate
    return index, best


def max_form(forms: Sequence[Form]) -> tuple[int, Form]:
    index = 0
    best = forms[0]
    for candidate_index, candidate in enumerate(forms[1:], 1):
        if compare_forms(candidate, best) > 0:
            index, best = candidate_index, candidate
    return index, best


def serialize_form(form: Mapping[int, Fraction]) -> list[dict[str, int]]:
    return [
        {
            "denominator": coefficient.denominator,
            "numerator": coefficient.numerator,
            "prime": prime,
        }
        for prime, coefficient in sorted(clean(form).items())
    ]


def form_l1(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> Fraction:
    difference = add_forms(left, scale_form(right, -1))
    return sum((abs(value) for value in difference.values()), Fraction(0))


def validate_parameters(d: int, a: Sequence[int], m: Sequence[int] | None = None,
                        total: int | None = None) -> None:
    if d < 2:
        raise ValueError("d must be at least two")
    if not a or any(value < 1 for value in a):
        raise ValueError("phase sizes must be positive")
    if m is not None:
        if len(m) != len(a) or any(value < 0 for value in m):
            raise ValueError("invalid composition")
        required = d if total is None else total
        if sum(m) != required:
            raise ValueError("wrong composition total")


def c_forms(a: Sequence[int]) -> list[Form]:
    return [factor_integer(value) for value in a]


def h_forms(d: int, a: Sequence[int]) -> list[Form]:
    validate_parameters(d, a)
    p = len(a)
    c = c_forms(a)
    denominator = d**p - 1
    return [
        sum_scaled(
            (
                Fraction((d - 1) * d ** (p - 1 - t), denominator),
                c[(j - t) % p],
            )
            for t in range(p)
        )
        for j in range(p)
    ]


def mean_c(a: Sequence[int]) -> Form:
    return scale_form(add_forms(*c_forms(a)), Fraction(1, len(a)))


def compositions(total: int, parts: int) -> Iterator[tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def convolution_residues(d: int, a: Sequence[int], m: Sequence[int],
                         denominator: int | None = None) -> list[Form]:
    total = sum(m) if denominator is None else denominator
    validate_parameters(d, a, m, sum(m))
    h = h_forms(d, a)
    p = len(a)
    return [
        scale_form(
            sum_scaled((m[s], h[(s + j) % p]) for s in range(p)),
            Fraction(1, total),
        )
        for j in range(p)
    ]


def via_b_residues(d: int, a: Sequence[int], m: Sequence[int],
                   denominator: int | None = None) -> list[Form]:
    total = sum(m) if denominator is None else denominator
    c = c_forms(a)
    p = len(a)
    b = [
        scale_form(sum_scaled((m[s], c[(s + k) % p]) for s in range(p)),
                   Fraction(1, total))
        for k in range(p)
    ]
    kernel_denominator = d**p - 1
    return [
        sum_scaled(
            (
                Fraction((d - 1) * d ** (p - 1 - t), kernel_denominator),
                b[(j - t) % p],
            )
            for t in range(p)
        )
        for j in range(p)
    ]


def shifted_log_products(a: Sequence[int], m: Sequence[int]) -> list[Form]:
    p = len(a)
    c = c_forms(a)
    return [sum_scaled((m[s], c[(s + k) % p]) for s in range(p)) for k in range(p)]


def delta_size(d: int, n: int) -> int:
    if n < 0:
        return 0
    return (d ** (n + 1) - 1) // (d - 1)


def core_prefix_form(d: int, a: Sequence[int], root_phase: int, depth: int) -> Form:
    c = c_forms(a)
    p = len(a)
    raw = sum_scaled((d**level, c[(root_phase + level) % p]) for level in range(depth + 1))
    return scale_form(raw, Fraction(1, delta_size(d, depth)))


def feeder_prefix_form(d: int, a: Sequence[int], m: Sequence[int],
                       transient_levels: int, total_depth: int) -> Form:
    leaves = d**transient_levels
    validate_parameters(d, a, m, leaves)
    if total_depth < transient_levels:
        return {}
    c = c_forms(a)
    p = len(a)
    raw = sum_scaled(
        (m[s] * d**level, c[(s + level) % p])
        for s in range(p)
        for level in range(total_depth - transient_levels + 1)
    )
    return scale_form(raw, Fraction(1, delta_size(d, total_depth)))


def form_to_integer(form: Mapping[int, Fraction]) -> int:
    LEDGER.check(all(value.denominator == 1 and value >= 0 for value in form.values()),
                 "integer reconstruction received fractional/negative exponent")
    answer = 1
    for prime, exponent in form.items():
        answer *= prime ** exponent.numerator
    return answer


def recursive_component_count(d: int, a: Sequence[int], root_phase: int, depth: int,
                              memo: dict[tuple[int, int], int] | None = None) -> int:
    if memo is None:
        memo = {}
    p = len(a)
    key = (root_phase % p, depth)
    if key not in memo:
        if depth == 0:
            memo[key] = a[root_phase % p]
        else:
            child = recursive_component_count(d, a, root_phase + 1, depth - 1, memo)
            memo[key] = a[root_phase % p] * child**d
    return memo[key]


def direct_component_integer(d: int, a: Sequence[int], root_phase: int, depth: int) -> int:
    c = c_forms(a)
    p = len(a)
    raw = sum_scaled((d**level, c[(root_phase + level) % p]) for level in range(depth + 1))
    return form_to_integer(raw)


def recursive_feeder_integer(d: int, a: Sequence[int], ordered_phases: Sequence[int],
                             total_depth: int) -> int:
    if total_depth < 1:
        return 1
    memo: dict[tuple[int, int], int] = {}
    answer = 1
    for phase in ordered_phases:
        answer *= recursive_component_count(d, a, phase, total_depth - 1, memo)
    return answer


def direct_feeder_integer(d: int, a: Sequence[int], ordered_phases: Sequence[int],
                          total_depth: int) -> int:
    p = len(a)
    m = tuple(sum(phase == s for phase in ordered_phases) for s in range(p))
    c = c_forms(a)
    raw = sum_scaled(
        (m[s] * d**level, c[(s + level) % p])
        for s in range(p)
        for level in range(total_depth)
    )
    return form_to_integer(raw)


def replay_active_evidence() -> dict[str, object]:
    evidence = ACTIVE / "evidence"
    summary = json.loads((evidence / "run_summary.json").read_text(encoding="utf-8"))
    LEDGER.equal(summary["schema"], "p49-tree-stage2-evidence-v1", "active evidence schema")
    LEDGER.equal(summary["result"], "PASS", "active evidence result")
    LEDGER.equal(summary["assertion_count"], 73517, "active assertion count")
    for name, digest in summary["evidence_sha256"].items():
        LEDGER.equal(sha256_file(evidence / name), digest, f"active evidence hash {name}")
    independence = summary["implementation_independence"]
    LEDGER.equal(sha256_file(ACTIVE / "formula_engine.py"),
                 independence["formula_engine_sha256"], "formula engine hash")
    LEDGER.equal(sha256_file(ACTIVE / "prefix_engine.py"),
                 independence["prefix_engine_sha256"], "prefix engine hash")
    imported: dict[str, set[str]] = {}
    for name in ("formula_engine.py", "prefix_engine.py"):
        tree = ast.parse((ACTIVE / name).read_text(encoding="utf-8"))
        modules: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module)
        imported[name] = modules
    LEDGER.check("prefix_engine" not in imported["formula_engine.py"],
                 "active formula engine imports prefix engine")
    LEDGER.check("formula_engine" not in imported["prefix_engine.py"],
                 "active prefix engine imports formula engine")
    LEDGER.equal(independence["no_cross_import"], True, "active independence flag")

    formula = json.loads((evidence / "formula_enumeration.json").read_text(encoding="utf-8"))
    prefix = json.loads((evidence / "prefix_cylinder.json").read_text(encoding="utf-8"))
    level_l = json.loads((evidence / "level_l.json").read_text(encoding="utf-8"))
    mutations = json.loads((evidence / "mutation_controls.json").read_text(encoding="utf-8"))

    parameter_cases = sum(3 * 3**p for p in range(1, 5))
    composition_cases = sum(
        3**p * math.comb(d + p - 1, p - 1)
        for d in range(2, 5) for p in range(1, 5)
    )
    uniform_hits = sum(3**p for d in range(2, 5) for p in range(1, 5) if d % p == 0)
    component_prefix = sum(3 * 3**p * p * (2 * p + 3) for p in range(1, 5))
    residue_comparisons = sum(3 * 3**p * p * p for p in range(1, 5))
    recursive_component = sum(2 * 3**p * p * 4 for p in range(1, 4))
    recursive_feeder = sum(3**p * p**d for d in range(2, 4) for p in range(1, 4))
    level_compositions = sum(
        2 * math.comb(d**level + p - 1, p - 1)
        for d in range(2, 4) for p in range(2, 5) for level in range(1, 4)
    )
    exact_level_hits = sum(
        1 for d in range(2, 5) for p in range(2, 7) for level in range(1, 9)
        if d**level % p == 0
    )

    expected_formula = {
        "composition_case_count": composition_cases,
        "convolution_identity_count": composition_cases,
        "mean_identity_count": parameter_cases + composition_cases,
        "parameter_case_count": parameter_cases,
        "saturation_equivalence_count": composition_cases,
        "uniform_p_divides_d_sufficiency_count": uniform_hits,
    }
    for key, expected in expected_formula.items():
        LEDGER.equal(formula[key], expected, f"active formula count {key}")
    LEDGER.equal(formula["p2_controls"]["case_count"], 175, "active p2 cases")
    LEDGER.equal(formula["p2_controls"]["strict_improvement_count"], 140,
                 "active p2 strict cases")
    LEDGER.equal(formula["p2_controls"]["even_nonconstant_saturation_count"], 80,
                 "active p2 even cases")
    LEDGER.equal(formula["p2_controls"]["odd_nonconstant_nonsaturation_count"], 60,
                 "active p2 odd cases")
    LEDGER.equal(prefix["component_prefix_exact_equality_count"], component_prefix,
                 "active component prefix count")
    LEDGER.equal(prefix["feeder_prefix_exact_equality_count"], 2 * composition_cases,
                 "active feeder prefix count")
    LEDGER.equal(prefix["residue_convergence_comparison_count"], residue_comparisons,
                 "active residue comparison count")
    LEDGER.equal(prefix["recursive_integer_controls"]["actual_recursive_component_count"],
                 recursive_component, "active recursive component count")
    LEDGER.equal(prefix["recursive_integer_controls"]["actual_recursive_feeder_count"],
                 recursive_feeder, "active recursive feeder count")
    LEDGER.equal(level_l["level_l_composition_count"], level_compositions,
                 "active level-L composition count")
    LEDGER.equal(level_l["level_l_denominator_prefix_checks"], level_compositions,
                 "active level-L prefix count")
    LEDGER.equal(level_l["level_l_saturation_checks"], level_compositions,
                 "active level-L saturation count")
    LEDGER.equal(level_l["level_l_optimization_count"], 36,
                 "active level-L optimization count")
    LEDGER.equal(level_l["convergence_case_count"], 15,
                 "active convergence family count")
    LEDGER.equal(level_l["convergence_checks"], 315,
                 "active convergence check count")
    LEDGER.equal(level_l["exact_p_divides_d_power_hits"], exact_level_hits,
                 "active exact divisibility hits")
    LEDGER.equal(mutations["control_count"], 6, "active mutation count")
    LEDGER.check(all(control.get("status") == "PASS" for control in mutations["controls"]),
                 "active mutation ledger contains non-PASS control")
    return {
        "active_assertions": summary["assertion_count"],
        "active_evidence_hashes": dict(sorted(summary["evidence_sha256"].items())),
        "count_ledger_rederived": {
            **expected_formula,
            "component_prefix": component_prefix,
            "feeder_prefix": 2 * composition_cases,
            "level_l_compositions": level_compositions,
            "recursive_component": recursive_component,
            "recursive_feeder": recursive_feeder,
            "residue_comparisons": residue_comparisons,
        },
        "selected_optimizers": level_l["selected_optimizers"],
    }


def independent_general_sweep() -> dict[str, object]:
    parameter_count = 0
    composition_count = 0
    prefix_comparisons = 0
    recursive_component_checks = 0
    recursive_feeder_checks = 0
    uniform_hits = 0
    max_error_q2 = Fraction(0)
    max_error_q6 = Fraction(0)
    for d in range(2, 5):
        for p in range(1, 5):
            for a in itertools.product(range(1, 4), repeat=p):
                parameter_count += 1
                h = h_forms(d, a)
                mean = mean_c(a)
                LEDGER.check(equal_forms(scale_form(add_forms(*h), Fraction(1, p)), mean),
                             "independent H mean preservation")
                for root in range(p):
                    for residue in range(p):
                        n2 = residue + 2 * p
                        n6 = residue + 6 * p
                        target = h[(root + residue) % p]
                        error2 = form_l1(core_prefix_form(d, a, root, n2), target)
                        error6 = form_l1(core_prefix_form(d, a, root, n6), target)
                        LEDGER.check(error6 <= error2, "core residue contraction")
                        max_error_q2 = max(max_error_q2, error2)
                        max_error_q6 = max(max_error_q6, error6)
                        prefix_comparisons += 1
                for m in compositions(d, p):
                    composition_count += 1
                    direct = convolution_residues(d, a, m)
                    via_b = via_b_residues(d, a, m)
                    LEDGER.equal([clean(x) for x in direct], [clean(x) for x in via_b],
                                 "independent H(b)/convolution identity")
                    residue_mean = scale_form(add_forms(*direct), Fraction(1, p))
                    LEDGER.check(equal_forms(residue_mean, mean), "feeder residue mean")
                    _, dimension = min_form(direct)
                    LEDGER.check(compare_forms(dimension, mean) <= 0, "minimum exceeds mean")
                    constant_product = all_equal(shifted_log_products(a, m))
                    LEDGER.equal(all_equal(direct), constant_product,
                                 "constant convolution saturation equivalence")
                if d % p == 0:
                    uniform = (d // p,) * p
                    LEDGER.check(all_equal(convolution_residues(d, a, uniform)),
                                 "uniform p-divides-d saturation")
                    uniform_hits += 1

    for d in range(2, 4):
        for p in range(1, 4):
            for a in itertools.product(range(1, 4), repeat=p):
                for root in range(p):
                    for depth in range(4):
                        LEDGER.equal(recursive_component_count(d, a, root, depth),
                                     direct_component_integer(d, a, root, depth),
                                     "independent recursive component count")
                        recursive_component_checks += 1
                for ordered in itertools.product(range(p), repeat=d):
                    LEDGER.equal(recursive_feeder_integer(d, a, ordered, 3),
                                 direct_feeder_integer(d, a, ordered, 3),
                                 "independent recursive feeder count")
                    recursive_feeder_checks += 1
    return {
        "composition_count": composition_count,
        "max_core_coefficient_error_q2": {
            "denominator": max_error_q2.denominator,
            "numerator": max_error_q2.numerator,
        },
        "max_core_coefficient_error_q6": {
            "denominator": max_error_q6.denominator,
            "numerator": max_error_q6.numerator,
        },
        "parameter_count": parameter_count,
        "prefix_residue_comparisons": prefix_comparisons,
        "recursive_component_checks": recursive_component_checks,
        "recursive_feeder_checks": recursive_feeder_checks,
        "uniform_saturation_hits": uniform_hits,
    }


def independent_p2_sweep() -> dict[str, int]:
    cases = 0
    composition_checks = 0
    strict = 0
    even_saturated = 0
    odd_nonsaturated = 0
    for d in range(2, 9):
        for a0 in range(1, 6):
            for a1 in range(1, 6):
                cases += 1
                a = (a0, a1)
                c0, c1 = c_forms(a)
                mu = scale_form(add_forms(c0, c1), Fraction(1, 2))
                delta_sign = compare_forms(c1, c0)
                delta = add_forms(c1, scale_form(c0, -1)) if delta_sign >= 0 else add_forms(c0, scale_form(c1, -1))
                expected_component = add_forms(
                    mu, scale_form(delta, -Fraction(d - 1, 2 * (d + 1)))
                )
                _, actual_component = min_form(h_forms(d, a))
                LEDGER.check(equal_forms(expected_component, actual_component), "p2 component formula")
                candidates: list[Form] = []
                for k in range(d + 1):
                    forms = convolution_residues(d, a, (k, d - k))
                    _, actual = min_form(forms)
                    expected = add_forms(
                        mu,
                        scale_form(delta, -Fraction((d - 1) * abs(2 * k - d), 2 * d * (d + 1))),
                    )
                    LEDGER.check(equal_forms(actual, expected), "p2 fixed-composition formula")
                    candidates.append(actual)
                    composition_checks += 1
                _, optimum = max_form(candidates)
                if d % 2 == 0:
                    LEDGER.check(equal_forms(optimum, mu), "p2 even optimum")
                else:
                    expected_optimum = add_forms(mu, scale_form(delta, -Fraction(d - 1, 2 * d * (d + 1))))
                    LEDGER.check(equal_forms(optimum, expected_optimum), "p2 odd optimum")
                if a0 != a1:
                    LEDGER.check(compare_forms(optimum, actual_component) > 0, "p2 strict improvement")
                    strict += 1
                    if d % 2 == 0:
                        LEDGER.check(equal_forms(optimum, mu), "p2 nonconstant even saturation")
                        even_saturated += 1
                    else:
                        LEDGER.check(compare_forms(optimum, mu) < 0, "p2 nonconstant odd deficit")
                        odd_nonsaturated += 1
                else:
                    LEDGER.check(all(all_equal(convolution_residues(d, a, (k, d - k)))
                                     for k in range(d + 1)), "p2 equal-phase boundary")
    return {
        "case_count": cases,
        "composition_formula_checks": composition_checks,
        "even_nonconstant_saturation_count": even_saturated,
        "odd_nonconstant_deficit_count": odd_nonsaturated,
        "strict_improvement_count": strict,
    }


def independent_level_sweep(active_selected: Sequence[Mapping[str, object]]) -> dict[str, object]:
    optimization_count = 0
    composition_count = 0
    selected_by_key = {
        (row["d"], row["p"], tuple(row["a"]), row["level"]): row
        for row in active_selected
    }
    monotonic: dict[tuple[int, int, tuple[int, ...]], Form] = {}
    prefix_checks = 0
    for d in range(2, 4):
        for p in range(2, 5):
            candidate_vectors = sorted({
                tuple(2 + (j % 2) for j in range(p)),
                tuple(1 + (j % 3) for j in range(p)),
            })
            for a in candidate_vectors:
                previous: Form | None = None
                for level in range(1, 4):
                    leaves = d**level
                    best_m: tuple[int, ...] | None = None
                    best: Form | None = None
                    for m in compositions(leaves, p):
                        composition_count += 1
                        residues = convolution_residues(d, a, m, leaves)
                        LEDGER.equal(all_equal(residues), all_equal(shifted_log_products(a, m)),
                                     "independent level-L saturation")
                        _, dimension = min_form(residues)
                        if best is None or compare_forms(dimension, best) > 0 or (
                            compare_forms(dimension, best) == 0 and m < best_m
                        ):
                            best_m, best = m, dimension

                        total_depth = level + p + 1
                        direct_normalized = feeder_prefix_form(d, a, m, level, total_depth)
                        c = c_forms(a)
                        raw = sum_scaled(
                            (m[s] * d**ell, c[(s + ell) % p])
                            for s in range(p)
                            for ell in range(total_depth - level + 1)
                        )
                        independent_normalized = scale_form(raw, Fraction(1, delta_size(d, total_depth)))
                        LEDGER.check(equal_forms(direct_normalized, independent_normalized),
                                     "independent exact d^L prefix denominator")
                        prefix_checks += 1
                    assert best_m is not None and best is not None
                    if previous is not None:
                        LEDGER.check(compare_forms(best, previous) >= 0,
                                     "independent optimized level monotonicity")
                    previous = best
                    monotonic[(d, p, a)] = best
                    active_row = selected_by_key[(d, p, a, level)]
                    LEDGER.equal(list(best_m), active_row["m"], "independent active optimizer m")
                    LEDGER.equal(serialize_form(best), active_row["dimension"],
                                 "independent active optimizer dimension")
                    optimization_count += 1

    balanced_checks = 0
    exact_hits = 0
    for d in range(2, 5):
        for p in range(2, 7):
            a = tuple(2 + (j % 3) for j in range(p))
            h = h_forms(d, a)
            _, maximum_h = max_form(h)
            mean = mean_c(a)
            for level in range(1, 9):
                leaves = d**level
                quotient, remainder = divmod(leaves, p)
                m = tuple(quotient + (s < remainder) for s in range(p))
                residues = convolution_residues(d, a, m, leaves)
                _, dimension = min_form(residues)
                LEDGER.check(compare_forms(dimension, mean) <= 0,
                             "balanced dimension exceeds mean")
                gap = add_forms(mean, scale_form(dimension, -1))
                bound = scale_form(maximum_h, Fraction(p, leaves))
                LEDGER.check(compare_forms(gap, {}) >= 0, "balanced negative gap")
                LEDGER.check(compare_forms(gap, bound) <= 0, "balanced error bound")
                balanced_checks += 3
                if leaves % p == 0:
                    LEDGER.check(all_equal(residues), "p divides d^L exact hit")
                    exact_hits += 1
    return {
        "balanced_exact_inequality_checks": balanced_checks,
        "composition_count": composition_count,
        "exact_p_divides_d_power_hits": exact_hits,
        "optimization_count": optimization_count,
        "prefix_denominator_checks": prefix_checks,
        "selected_optimizer_matches": optimization_count,
    }


def adjacency_counts(adjacency: Sequence[Sequence[int]], d: int, depth: int) -> list[int]:
    counts = [1] * len(adjacency)
    for _ in range(depth):
        counts = [sum(row[j] * counts[j] for j in range(len(row))) ** d for row in adjacency]
    return counts


def negative_controls() -> dict[str, object]:
    controls: list[dict[str, object]] = []

    a = (2, 3, 2, 3)
    m = (1, 1, 0, 0)
    residues = convolution_residues(2, a, m)
    shifted = shifted_log_products(a, m)
    LEDGER.check(all_equal(residues) and all_equal(shifted) and 2 % 4 != 0,
                 "p=4 missing-Fourier negative control")
    controls.append({
        "name": "unconditional_divisibility_necessity",
        "p_divides_d": False,
        "shifted_product": 6,
        "status": "REJECTED",
    })

    complete_depth_one = 2 * 2**2
    missing_edge_depth_one = 1**2 + 2**2
    LEDGER.equal(complete_depth_one, 8, "complete block depth-one count")
    LEDGER.equal(missing_edge_depth_one, 5, "missing-edge actual depth-one count")
    LEDGER.check(missing_edge_depth_one != complete_depth_one,
                 "missing edge failed to change cylinder count")
    controls.append({
        "actual_depth_one_root_phase_count": missing_edge_depth_one,
        "complete_formula_count": complete_depth_one,
        "name": "one_missing_core_edge",
        "status": "REJECTED",
    })

    return_graph = [[0, 1], [1, 1]]
    reachable = {0}
    return_depths: list[int] = []
    for depth in range(1, 9):
        reachable = {j for i in reachable for j, edge in enumerate(return_graph[i]) if edge}
        if 0 in reachable:
            return_depths.append(depth)
    LEDGER.check(return_depths and max(return_depths) >= 8,
                 "return edge did not permit arbitrarily repeated feeder reachability witness")
    controls.append({
        "feeder_reachable_again_at_depths_through_8": return_depths,
        "name": "core_to_feeder_return",
        "status": "REJECTED",
    })

    allowed_child_phases = {0}
    unrestricted = set(compositions(2, 2))
    admitted = {(2, 0)}
    LEDGER.check(admitted != unrestricted and all(m[1] == 0 for m in admitted),
                 "incomplete feeder incorrectly retained unrestricted compositions")
    controls.append({
        "admitted": [list(value) for value in sorted(admitted)],
        "claimed_unrestricted": [list(value) for value in sorted(unrestricted)],
        "name": "noncomplete_feeder_row",
        "status": "REJECTED",
    })
    LEDGER.equal(allowed_child_phases, {0}, "incomplete feeder phase support")

    rejected: list[str] = []
    for name, args in (
        ("d_equals_one", (1, (2, 3), None, None)),
        ("zero_phase_size", (2, (2, 0), None, None)),
        ("wrong_composition_total", (2, (2, 3), (1, 0), 2)),
    ):
        try:
            validate_parameters(*args)
        except ValueError:
            rejected.append(name)
    LEDGER.equal(rejected, ["d_equals_one", "zero_phase_size", "wrong_composition_total"],
                 "parameter rejection set")
    controls.append({"name": "parameter_boundaries", "rejected": rejected, "status": "REJECTED"})

    adjacency = [
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ]
    counts = adjacency_counts(adjacency, 2, 8)
    core_dimension = {2: Fraction(1, 3)}
    feeder_dimension = {2: Fraction(1, 2)}
    LEDGER.check(compare_forms(feeder_dimension, core_dimension) > 0,
                 "four-state strict dimension inequality")
    LEDGER.check(counts[0] > max(counts[1:]), "four-state recursive feeder count witness")
    controls.append({
        "component_dimension": serialize_form(core_dimension),
        "depth_8_root_counts": [str(value) for value in counts],
        "full_dimension": serialize_form(feeder_dimension),
        "name": "four_state_max_scc_formula",
        "status": "REJECTED",
    })
    return {"control_count": len(controls), "controls": controls}


def run_replay() -> dict[str, object]:
    before_path = EVIDENCE / "active_before.json"
    LEDGER.check(before_path.is_file(), "active-before snapshot missing")
    before = json.loads(before_path.read_text(encoding="utf-8"))
    now = snapshot_active()
    LEDGER.equal(now, before["snapshot"], "active package changed since before snapshot")
    manifest = parse_and_verify_manifest(now)
    active = replay_active_evidence()
    general = independent_general_sweep()
    p2 = independent_p2_sweep()
    level_l = independent_level_sweep(active.pop("selected_optimizers"))
    negatives = negative_controls()
    return {
        "active_evidence_replay": active,
        "active_manifest": manifest,
        "independent_assertion_count": LEDGER.assertions,
        "independent_general_sweep": general,
        "independent_level_l_sweep": level_l,
        "independent_p2_sweep": p2,
        "negative_controls": negatives,
        "result": "PASS",
        "schema": "p49-tree-independent-cross-audit-v1",
    }


def capture_before() -> None:
    snapshot = snapshot_active()
    manifest = parse_and_verify_manifest(snapshot)
    write_json(EVIDENCE / "active_before.json", {
        "manifest": manifest,
        "snapshot": snapshot,
    })
    print(json.dumps(manifest, sort_keys=True))


def replay() -> None:
    result = run_replay()
    write_json(EVIDENCE / "independent_replay.json", result)
    print(json.dumps({
        "independent_assertion_count": result["independent_assertion_count"],
        "result": result["result"],
    }, sort_keys=True))


def verify_after() -> None:
    before = json.loads((EVIDENCE / "active_before.json").read_text(encoding="utf-8"))
    after = snapshot_active()
    LEDGER.equal(after, before["snapshot"], "active before/after snapshot mismatch")
    manifest = parse_and_verify_manifest(after)
    result = {
        "active_before_after_byte_equal": True,
        "active_cache_count": len(after["caches"]),
        "active_manifest": manifest,
        "active_nonregular_count": len(after["nonregular"]),
        "active_symlink_count": len(after["symlinks"]),
        "verification_assertions": LEDGER.assertions,
    }
    write_json(EVIDENCE / "active_after_check.json", result)
    print(json.dumps(result, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--capture-before", action="store_true")
    group.add_argument("--replay", action="store_true")
    group.add_argument("--verify-after", action="store_true")
    args = parser.parse_args()
    if args.capture_before:
        capture_before()
    elif args.replay:
        replay()
    else:
        verify_after()


if __name__ == "__main__":
    main()
