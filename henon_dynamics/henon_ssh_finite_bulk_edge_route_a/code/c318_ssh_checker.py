#!/usr/bin/env python3
"""Producer-independent exact checker for the HCS-C318 SSH package."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c318_ssh_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C318/2026-09-03.yaml"
SOURCE = "1938bae19e5a92f9ce2411aafdc68323bd641bd0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION_SEMANTIC_SHA256 = "a04a49976833a44cfd1ee4c8fb88938388395a0372815f0f9763777d4bfab957"
EVALUATION_RAW_SHA256 = "e2df7221a06d8e703ad4b7fcc1af2358543c518b5a78ff53989945e5ca4453c2"
mp.mp.dps = 90

EXPECTED_FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
EXPECTED_MODEL = {
    "owner": "balanced finite Su--Schrieffer--Heeger single-particle chain",
    "open_size": "M>=2 cells and 2M sites; M=1 is an explicit convention face",
    "hoppings": "real v,w>=0 with v intracell and w intercell",
    "open_block": "H=[[0,T],[T*,0]], T=vI+wS_-",
    "periodic_symbol": "h(k)=[[0,conj(q(k))],[q(k),0]], q(k)=v+w exp(ik)",
    "clock": "physical unitary time i psi_dot=H psi",
}
EXPECTED_THEOREM = {
    "characteristic": "det(EI-H)=(vw)^M[U_M(x)+(w/v)U_(M-1)(x)], x=(E^2-v^2-w^2)/(2vw), for v,w>0",
    "finite_edge": "one hyperbolic pair exists iff w/v>(M+1)/M",
    "bulk": "winding of q(k)=v+w exp(ik) is one for w>v and zero for v>w; continuum and finite sampled gaps are distinguished",
    "threshold_separation": "bulk critical ratio is one; the strict finite hyperbolic threshold is (M+1)/M",
    "periodic_parity": "at v=w>0 a finite ring has a two-dimensional zero sector iff M is even",
    "faces": "w=0 gives M dimers; v=0 gives M-1 dimers plus two exact edge zeros; both zero gives the zero matrix",
    "propagator": "the entire block sinc formula is valid on every singular face",
    "quench": "gapped opposite-phase Bloch quenches and only those have continuum mode Loschmidt zeros; finite rings require momentum-grid incidence",
}
EXPECTED_COLLISIONS = {
    "C308": "C308 is a one-site non-Hermitian nonreciprocal skin chain and explicitly excludes winding and topological edge modes; C318 is Hermitian, bipartite, chiral, and bulk--edge based.",
    "C267": "C267 is an infinite uniform-field Wannier--Stark ladder with Bessel propagation, not a dimerized finite topological chain.",
    "C297": "C297 is a two-site non-Hermitian PT dimer with an exceptional point, not a many-cell Hermitian bulk--edge system.",
    "C138": "C138 uses flux winding in a metric quantum graph primitive-walk determinant, not Bloch-band winding or SSH edge hybridization.",
}
EXPECTED_NONCLAIMS = [
    "No literature-priority claim is made for the SSH model, winding, bulk--edge correspondence, or finite edge splitting.",
    "The finite characteristic polynomial is not an Euler factor and the source spectrum is not a target zero set.",
    "No disorder, interaction, self-consistent phonon, many-body DQPT, automorphy, root number, or Hilbert--Polya claim is made.",
]
EXPECTED_REFERENCES = [
    {"identifier": "10.1103/PhysRevLett.42.1698", "role": "SSH model and polyacetylene provenance"},
    {"identifier": "10.1103/PhysRevB.22.2099", "role": "soliton excitation and localized gap-state lineage"},
    {"identifier": "10.1007/978-3-319-25607-8_1", "role": "chiral, winding, and bulk--boundary exposition"},
]


def exact_keys(value, expected, label):
    need(type(value) is dict and set(value) == set(expected), f"{label} keys")


def duplicate_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def strict_json(path: Path):
    value = json.loads(
        path.read_text(),
        object_pairs_hook=duplicate_pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )
    if type(value) is not dict:
        raise TypeError("JSON root must be an object")
    return value


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be an object")
    return value


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fr(value) -> Fraction:
    if type(value) is not str:
        raise TypeError("rational receipt must be a string")
    result = Fraction(value)
    if q(result) != value:
        raise ValueError("noncanonical rational")
    return result


def mpf(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def need(condition: bool, label: str):
    if not condition:
        raise AssertionError(label)


def near(got, want, label: str, tolerance=mp.mpf("3e-68")):
    if type(got) is not str:
        raise TypeError(f"{label}: decimal must be string")
    parsed = mp.mpf(got)
    if not mp.isfinite(parsed) or abs(parsed - want) > tolerance * max(mp.mpf(1), abs(want)):
        raise AssertionError(f"{label}: {got} != {want}")


def trim(poly: list[Fraction]) -> list[Fraction]:
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def p_add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def p_scale(a, c):
    return trim([c * value for value in a])


def p_shift(a):
    return [Fraction(0)] + list(a)


def p_eval(a, x):
    total = Fraction(0)
    for coefficient in reversed(a):
        total = total * x + coefficient
    return total


def p_derivative(a):
    return trim([Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)])


def p_divrem(a, b):
    a = trim(a)
    b = trim(b)
    if b == [0]:
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    remainder = list(a)
    while remainder != [0] and len(remainder) >= len(b):
        degree = len(remainder) - len(b)
        factor = remainder[-1] / b[-1]
        quotient[degree] += factor
        for i, coefficient in enumerate(b):
            remainder[i + degree] -= factor * coefficient
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def sturm(poly):
    sequence = [trim(poly), p_derivative(poly)]
    while sequence[-1] != [0]:
        _, remainder = p_divrem(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append(p_scale(remainder, Fraction(-1)))
    return sequence


def sign(value):
    return 1 if value > 0 else -1 if value < 0 else 0


def variations(signs):
    cleaned = [item for item in signs if item]
    return sum(cleaned[i] != cleaned[i - 1] for i in range(1, len(cleaned)))


def variations_at(sequence, point):
    if point == "-inf":
        return variations([sign(poly[-1]) * ((-1) ** (len(poly) - 1)) for poly in sequence])
    if point == "+inf":
        return variations([sign(poly[-1]) for poly in sequence])
    return variations([sign(p_eval(poly, point)) for poly in sequence])


def root_count(poly, left, right):
    sequence = sturm(poly)
    return variations_at(sequence, left) - variations_at(sequence, right)


def chebyshev_u(n: int) -> list[Fraction]:
    u0 = [Fraction(1)]
    if n == 0:
        return u0
    u1 = [Fraction(0), Fraction(2)]
    if n == 1:
        return u1
    for _ in range(2, n + 1):
        u0, u1 = u1, p_add(p_scale(p_shift(u1), Fraction(2)), p_scale(u0, Fraction(-1)))
    return u1


def site_characteristic_y(m: int, v: Fraction, w: Fraction) -> list[Fraction]:
    """Independent site-by-site continuant, returned in y=E^2."""
    d0 = [Fraction(1)]
    d1 = [Fraction(0), Fraction(1)]
    for n in range(2, 2 * m + 1):
        hopping = v if (n - 1) % 2 else w
        d0, d1 = d1, p_add(p_shift(d1), p_scale(d0, -hopping * hopping))
    need(all(d1[i] == 0 for i in range(1, len(d1), 2)), "odd characteristic coefficient")
    return trim([d1[2 * i] for i in range(m + 1)])


def ssh_matrix(m: int, v: Fraction, w: Fraction) -> mp.matrix:
    h = mp.matrix(2 * m)
    for j in range(m):
        h[j, m + j] = h[m + j, j] = mpf(v)
        if j + 1 < m:
            h[j + 1, m + j] = h[m + j, j + 1] = mpf(w)
    return h


def max_abs(matrix: mp.matrix) -> mp.mpf:
    return max((abs(matrix[i, j]) for i in range(matrix.rows) for j in range(matrix.cols)), default=mp.mpf(0))


def taylor_exponential(matrix: mp.matrix) -> mp.matrix:
    result = mp.eye(matrix.rows)
    term = mp.eye(matrix.rows)
    for n in range(1, 240):
        term = term * matrix / n
        result += term
        if max_abs(term) < mp.mpf("1e-82"):
            return result
    raise AssertionError("matrix exponential series did not converge")


def check_obc(data, counter):
    rows = data["obc_polynomial_rows"]
    need(type(rows) is list and len(rows) == 55, "OBC row count")
    for index, row in enumerate(rows):
        need(type(row) is dict, "OBC row type")
        exact_keys(row, {"M", "label", "v", "w", "ratio_w_over_v", "finite_edge_threshold", "root_zone", "q_coefficients_y_ascending", "det_T", "zero_eigenvalue_multiplicity"}, "OBC row")
        m = 2 + index // 5
        v, w = fr(row["v"]), fr(row["w"])
        expected_cases = [
            ("trivial", Fraction(3), Fraction(2)),
            ("bulk_critical", Fraction(1), Fraction(1)),
            ("bulk_topological_finite_subthreshold", Fraction(2 * m), Fraction(2 * m + 1)),
            ("finite_edge_threshold", Fraction(m), Fraction(m + 1)),
            ("hyperbolic_edge", Fraction(1), Fraction(2)),
        ]
        label, expected_v, expected_w = expected_cases[index % 5]
        need(
            (row["M"], row["label"], v, w) == (m, label, expected_v, expected_w),
            "OBC order and fixed producer parameters",
        )
        need(v > 0 and w > 0, "positive OBC receipt")
        need(fr(row["ratio_w_over_v"]) == w / v, "OBC ratio")
        threshold = Fraction(m + 1, m)
        need(fr(row["finite_edge_threshold"]) == threshold, "OBC threshold")
        coefficients = [fr(value) for value in row["q_coefficients_y_ascending"]]
        need(coefficients == site_characteristic_y(m, v, w), "OBC characteristic")
        need(len(coefficients) == m + 1 and coefficients[-1] == 1, "OBC degree")
        need(coefficients[0] == (-1) ** m * v ** (2 * m), "OBC constant")
        need(fr(row["det_T"]) == v**m and row["zero_eigenvalue_multiplicity"] == 0, "OBC invertibility")

        f = p_add(chebyshev_u(m), p_scale(chebyshev_u(m - 1), w / v))
        fminus, fplus = p_eval(f, Fraction(-1)), p_eval(f, Fraction(1))
        need(fplus != 0, "x=1 root forbidden")
        if w / v < threshold:
            expected_zone = "all_trigonometric"
            need(fminus != 0 and root_count(f, "-inf", Fraction(-1)) == 0, "subthreshold lower roots")
            need(root_count(f, Fraction(-1), Fraction(1)) == m, "subthreshold band roots")
            need(root_count(f, Fraction(1), "+inf") == 0, "subthreshold upper roots")
        elif w / v == threshold:
            expected_zone = "threshold_x_minus_one"
            need(fminus == 0 and p_eval(p_derivative(f), Fraction(-1)) != 0, "simple threshold root")
            quotient, remainder = p_divrem(f, [Fraction(1), Fraction(1)])
            need(remainder == [0], "threshold factor")
            need(root_count(quotient, "-inf", Fraction(-1)) == 0, "threshold lower quotient")
            need(root_count(quotient, Fraction(-1), Fraction(1)) == m - 1, "threshold band quotient")
            need(root_count(quotient, Fraction(1), "+inf") == 0, "threshold upper quotient")
        else:
            expected_zone = "one_hyperbolic_pair"
            need(fminus != 0 and root_count(f, "-inf", Fraction(-1)) == 1, "hyperbolic root count")
            need(root_count(f, Fraction(-1), Fraction(1)) == m - 1, "hyperbolic band roots")
            need(root_count(f, Fraction(1), "+inf") == 0, "hyperbolic upper roots")
        need(row["root_zone"] == expected_zone, "root-zone label")
        counter[0] += 18 + len(coefficients)


def check_edges(data, counter):
    rows = data["exact_edge_witnesses"]
    need(type(rows) is list and len(rows) == 33, "edge row count")
    for index, row in enumerate(rows):
        exact_keys(row, {"M", "z_exp_minus_kappa", "v", "w", "ratio_w_over_v", "threshold", "x_minus_cosh_kappa", "edge_energy", "edge_energy_squared", "a_vector", "b_vector", "joint_norm_squared", "strict_decay_bound"}, "edge row")
        m = 2 + index // 3
        z_expected = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4))[index % 3]
        need(row["M"] == m, "edge M")
        z, v, w = fr(row["z_exp_minus_kappa"]), fr(row["v"]), fr(row["w"])
        need(z == z_expected and v == 1 and 0 < z < 1, "edge parameters")
        ratio = (1 / z) * (1 - z ** (2 * m + 2)) / (1 - z ** (2 * m))
        threshold = Fraction(m + 1, m)
        need(w == ratio and fr(row["ratio_w_over_v"]) == ratio and ratio > threshold, "edge ratio")
        need(fr(row["threshold"]) == threshold, "edge threshold")
        x = -(z + 1 / z) / 2
        energy = v * z ** (m - 1) * (1 - z * z) / (1 - z ** (2 * m))
        need(fr(row["x_minus_cosh_kappa"]) == x and x < -1, "edge x")
        need(fr(row["edge_energy"]) == energy and fr(row["edge_energy_squared"]) == energy * energy, "edge energy")
        a = [fr(value) for value in row["a_vector"]]
        b = [fr(value) for value in row["b_vector"]]
        need(len(a) == len(b) == m, "edge vector length")
        expected_a = [Fraction((-1) ** (j - 1)) * (z ** (-(m + 1 - j)) - z ** (m + 1 - j)) / 2 for j in range(1, m + 1)]
        expected_b = [Fraction((-1) ** (j - 1)) * (z ** (-j) - z**j) / 2 for j in range(1, m + 1)]
        need(a == expected_a and b == expected_b, "edge vector formula")
        tb = [v * b[j] + (w * b[j - 1] if j else 0) for j in range(m)]
        tta = [v * a[j] + (w * a[j + 1] if j + 1 < m else 0) for j in range(m)]
        need(tb == [energy * value for value in a], "T b edge equation")
        need(tta == [energy * value for value in b], "T* a edge equation")
        norm_sq = sum(value * value for value in a) + sum(value * value for value in b)
        need(fr(row["joint_norm_squared"]) == norm_sq == 2 * sum(value * value for value in b), "edge norm")
        need(fr(row["strict_decay_bound"]) == z, "edge decay label")
        for j in range(m - 1):
            need(abs(a[j + 1]) < z * abs(a[j]), "left strict decay")
            need(abs(b[j]) < z * abs(b[j + 1]), "right strict decay")
        polynomial = site_characteristic_y(m, v, w)
        need(p_eval(polynomial, energy * energy) == 0, "edge characteristic root")
        counter[0] += 20 + 5 * m

    threshold_rows = data["finite_threshold_rows"]
    need(type(threshold_rows) is list and len(threshold_rows) == 11, "threshold row count")
    for index, row in enumerate(threshold_rows):
        exact_keys(row, {"M", "v", "w", "ratio_w_over_v", "x", "band_edge_energy", "a_linear_taper", "b_linear_taper"}, "threshold row")
        m = index + 2
        v, w, energy = Fraction(m), Fraction(m + 1), Fraction(1)
        need(row["M"] == m and fr(row["v"]) == v and fr(row["w"]) == w, "threshold parameters")
        need(fr(row["ratio_w_over_v"]) == Fraction(m + 1, m), "threshold ratio")
        need(fr(row["x"]) == -1 and fr(row["band_edge_energy"]) == energy, "threshold energy")
        a = [fr(value) for value in row["a_linear_taper"]]
        b = [fr(value) for value in row["b_linear_taper"]]
        need(a == [Fraction((-1) ** (j - 1) * (m + 1 - j)) for j in range(1, m + 1)], "threshold a")
        need(b == [Fraction((-1) ** (j - 1) * j) for j in range(1, m + 1)], "threshold b")
        tb = [v * b[j] + (w * b[j - 1] if j else 0) for j in range(m)]
        tta = [v * a[j] + (w * a[j + 1] if j + 1 < m else 0) for j in range(m)]
        need(tb == a and tta == b, "threshold eigenvectors")
        counter[0] += 12 + 4 * m


def check_periodic(data, counter):
    rows = data["periodic_rows"]
    labels = [
        ("trivial", Fraction(2), Fraction(1)),
        ("topological", Fraction(1), Fraction(2)),
        ("critical", Fraction(1), Fraction(1)),
        ("v_zero", Fraction(0), Fraction(2)),
        ("w_zero", Fraction(2), Fraction(0)),
    ]
    need(type(rows) is list and len(rows) == 70, "periodic rows")
    for index, row in enumerate(rows):
        exact_keys(
            row,
            {
                "M", "label", "v", "w", "winding_defined", "winding_value",
                "continuum_bulk_gap_to_zero", "continuum_central_band_gap",
                "finite_sampled_gap_to_zero", "finite_sampled_central_band_gap",
                "finite_zero_multiplicity", "momentum_cells",
            },
            "periodic row",
        )
        m = 2 + index // 5
        label, v, w = labels[index % 5]
        need((row["M"], row["label"], fr(row["v"]), fr(row["w"])) == (m, label, v, w), "periodic order")
        if w > v:
            expected_defined, expected_winding = True, 1
        elif v > w:
            expected_defined, expected_winding = True, 0
        else:
            expected_defined, expected_winding = False, None
        need(type(row["winding_defined"]) is bool and row["winding_defined"] == expected_defined, "winding defined")
        need(row["winding_value"] == expected_winding and (type(row["winding_value"]) is int if expected_defined else row["winding_value"] is None), "winding value")
        continuum_gap = abs(v - w)
        need(
            fr(row["continuum_bulk_gap_to_zero"]) == continuum_gap
            and fr(row["continuum_central_band_gap"]) == 2 * continuum_gap,
            "continuum Bloch gaps",
        )
        if m % 2 == 0:
            finite_gap = mpf(continuum_gap)
        else:
            finite_gap = mp.sqrt(
                mpf(v) ** 2
                + mpf(w) ** 2
                - 2 * mpf(v) * mpf(w) * mp.cos(mp.pi / m)
            )
        near(row["finite_sampled_gap_to_zero"], finite_gap, "finite sampled gap")
        near(row["finite_sampled_central_band_gap"], 2 * finite_gap, "finite sampled central gap")
        zero_mult = 2 if v == w and v > 0 and m % 2 == 0 else 0
        need(row["finite_zero_multiplicity"] == zero_mult, "periodic zero multiplicity")
        cells = row["momentum_cells"]
        need(type(cells) is list and len(cells) == m, "momentum cells")
        zero_cells = 0
        sampled_energies_squared = []
        for n, cell in enumerate(cells):
            exact_keys(cell, {"mode", "k_over_2pi", "q_real", "q_imag", "energy_squared"}, "momentum cell")
            need(cell["mode"] == n and fr(cell["k_over_2pi"]) == Fraction(n, m), "momentum index")
            k = 2 * mp.pi * n / m
            real = mpf(v) + mpf(w) * mp.cos(k)
            imag = mpf(w) * mp.sin(k)
            e2 = real * real + imag * imag
            sampled_energies_squared.append(e2)
            near(cell["q_real"], real, "q real")
            near(cell["q_imag"], imag, "q imag")
            near(cell["energy_squared"], e2, "periodic energy")
            if abs(e2) < mp.mpf("1e-70"):
                zero_cells += 1
            counter[0] += 7
        need(2 * zero_cells == zero_mult, "periodic sampled-zero parity")
        sampled_minimum = mp.sqrt(max(mp.mpf(0), min(sampled_energies_squared)))
        near(row["finite_sampled_gap_to_zero"], sampled_minimum, "finite gap versus momentum cells")
        need((finite_gap < mp.mpf("1e-70")) == (zero_mult > 0), "finite gap and zero multiplicity consistency")
        if label == "critical" and m % 2 == 1:
            need(finite_gap > 0, "odd critical ring is sampled-gapped")
            near(
                row["finite_sampled_gap_to_zero"],
                2 * mpf(v) * mp.sin(mp.pi / (2 * m)),
                "odd critical sampled-gap formula",
            )
        counter[0] += 18


def check_boundaries(data, counter):
    rows = data["boundary_rows"]
    need(type(rows) is list and len(rows) == 33, "boundary rows")
    for index, row in enumerate(rows):
        exact_keys(row, {"M", "face", "v", "w", "kernel_dimension", "positive_energy", "positive_multiplicity", "negative_multiplicity", "dimer_count"}, "boundary row")
        m = 2 + index // 3
        face = ("w_zero", "v_zero", "both_zero")[index % 3]
        need(row["M"] == m and row["face"] == face, "boundary order")
        if face == "w_zero":
            expected = (Fraction(2), Fraction(0), 0, Fraction(2), m, m, m)
        elif face == "v_zero":
            expected = (Fraction(0), Fraction(3), 2, Fraction(3), m - 1, m - 1, m - 1)
        else:
            expected = (Fraction(0), Fraction(0), 2 * m, Fraction(0), 0, 0, 0)
        got = (
            fr(row["v"]), fr(row["w"]), row["kernel_dimension"], fr(row["positive_energy"]),
            row["positive_multiplicity"], row["negative_multiplicity"], row["dimer_count"],
        )
        need(got == expected, "boundary spectrum")
        counter[0] += 10

    one = data["one_cell_convention"]
    need(
        one
        == {
            "M": 1,
            "v": "2",
            "w": "5",
            "open_eigenvalues": ["-2", "2"],
            "periodic_wrap_eigenvalues": ["-7", "7"],
            "statement": "the open intercell bond is absent; the periodic wrap bond merges with the intracell bond",
        },
        "one-cell convention",
    )
    counter[0] += 8


def check_propagators(data, counter):
    rows = data["propagator_rows"]
    cases = [
        ("trivial", Fraction(2), Fraction(1)),
        ("topological", Fraction(1), Fraction(2)),
        ("critical", Fraction(1), Fraction(1)),
        ("v_zero", Fraction(0), Fraction(2)),
        ("w_zero", Fraction(2), Fraction(0)),
        ("both_zero", Fraction(0), Fraction(0)),
    ]
    need(type(rows) is list and len(rows) == 30, "propagator rows")
    for index, row in enumerate(rows):
        exact_keys(row, {"M", "label", "v", "w", "time", "selected_entries", "trace_real", "trace_imag", "unitarity_residual", "chiral_time_reversal_residual"}, "propagator row")
        m = 2 + index // 6
        label, v, w = cases[index % 6]
        t = Fraction(m % 3 + 1, 5)
        need((row["M"], row["label"], fr(row["v"]), fr(row["w"]), fr(row["time"])) == (m, label, v, w, t), "propagator order")
        h = ssh_matrix(m, v, w)
        u = taylor_exponential(-mp.j * mpf(t) * h)
        expected_probes = sorted({(0, 0), (0, m), (0, 2 * m - 1), (m - 1, 2 * m - 1), (m, m), (2 * m - 1, 2 * m - 1)})
        cells = row["selected_entries"]
        need(type(cells) is list and [(x["row"], x["column"]) for x in cells] == expected_probes, "propagator probe coordinates")
        for cell, (i, j) in zip(cells, expected_probes):
            exact_keys(cell, {"row", "column", "real", "imag"}, "propagator cell")
            near(cell["real"], mp.re(u[i, j]), "propagator real")
            near(cell["imag"], mp.im(u[i, j]), "propagator imag")
            counter[0] += 5
        trace = sum(u[i, i] for i in range(2 * m))
        near(row["trace_real"], mp.re(trace), "propagator trace real")
        near(row["trace_imag"], mp.im(trace), "propagator trace imag")
        ident = mp.eye(2 * m)
        gamma = mp.diag([1] * m + [-1] * m)
        near(row["unitarity_residual"], max_abs(u.transpose_conj() * u - ident), "unitarity residual")
        near(row["chiral_time_reversal_residual"], max_abs(gamma * u * gamma - u.transpose_conj()), "chiral residual")
        counter[0] += 14


def check_quenches(data, counter):
    rows = data["quench_rows"]
    expected = [
        ("grid_hit_cross_phase", 3, 1, 1, 5),
        ("generic_cross_phase", 2, 1, 1, 2),
        ("reverse_cross_phase", 1, 4, 3, 1),
        ("same_trivial", 3, 1, 2, 1),
        ("same_topological", 1, 3, 1, 2),
        ("critical_endpoint_outside_contract", 2, 1, 1, 1),
    ]
    need(type(rows) is list and len(rows) == len(expected), "quench rows")
    for row, values in zip(rows, expected):
        exact_keys(row, {"label", "v_initial", "w_initial", "v_final", "w_final", "endpoints_gapped", "cross_phase", "has_continuum_mode_zero", "cos_k_star", "critical_energy_squared", "first_zero_time_over_pi", "finite_grid_hits_M_2_to_12"}, "quench row")
        label, vi0, wi0, vf0, wf0 = values
        vi, wi, vf, wf = map(Fraction, (vi0, wi0, vf0, wf0))
        need(
            (row["label"], fr(row["v_initial"]), fr(row["w_initial"]), fr(row["v_final"]), fr(row["w_final"]))
            == (label, vi, wi, vf, wf),
            "quench parameters",
        )
        gapped = vi != wi and vf != wf
        cross = gapped and (vi - wi) * (vf - wf) < 0
        need(type(row["endpoints_gapped"]) is bool and row["endpoints_gapped"] == gapped, "quench gap type")
        need(type(row["cross_phase"]) is bool and row["cross_phase"] == cross, "quench phase type")
        need(type(row["has_continuum_mode_zero"]) is bool and row["has_continuum_mode_zero"] == cross, "quench zero type")
        if cross:
            cosine = -(vi * vf + wi * wf) / (vi * wf + wi * vf)
            need(-1 < cosine < 0 and fr(row["cos_k_star"]) == cosine, "quench critical momentum")
            ef2 = vf * vf + wf * wf + 2 * vf * wf * cosine
            need(ef2 > 0 and fr(row["critical_energy_squared"]) == ef2, "quench critical energy")
            near(row["first_zero_time_over_pi"], 1 / (2 * mp.sqrt(mpf(ef2))), "quench first zero")
            numerator = vi * vf + wi * wf + (vi * wf + wi * vf) * cosine
            need(numerator == 0, "quench orthogonality")
            hits = []
            for m in range(2, 13):
                modes = [n for n in range(m) if abs(mp.cos(2 * mp.pi * n / m) - mpf(cosine)) < mp.mpf("1e-70")]
                if modes:
                    hits.append({"M": m, "modes": modes})
            for hit in row["finite_grid_hits_M_2_to_12"]:
                exact_keys(hit, {"M", "modes"}, "quench grid-hit row")
            need(row["finite_grid_hits_M_2_to_12"] == hits, "finite momentum-grid caveat")
        else:
            need(row["cos_k_star"] is None and row["critical_energy_squared"] is None and row["first_zero_time_over_pi"] is None, "no quench root")
            need(row["finite_grid_hits_M_2_to_12"] == [], "no finite-grid hits")
            if gapped:
                numerator = vi * vf + wi * wf
                denominator = vi * wf + wi * vf
                need(numerator > denominator, "same-phase no real orthogonality momentum")
        counter[0] += 18


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C318 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    checks = [0]

    evaluation_semantic_sha256 = hashlib.sha256(
        json.dumps(evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    need(evaluation_semantic_sha256 == EVALUATION_SEMANTIC_SHA256, "evaluation semantic digest")
    need(hashlib.sha256(args.evaluation.read_bytes()).hexdigest() == EVALUATION_RAW_SHA256, "evaluation raw-byte digest")
    checks[0] += 2

    exact_keys(
        data,
        {
            "schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit",
            "scope_literal", "evaluator", "model", "theorem_contract", "obc_polynomial_rows",
            "exact_edge_witnesses", "finite_threshold_rows", "periodic_rows", "boundary_rows",
            "propagator_rows", "quench_rows", "one_cell_convention", "collision_boundary", "route_a",
            "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256",
        },
        "evidence root",
    )

    need(payload_hash(data) == data.get("payload_sha256"), "payload hash")
    need(
        (data.get("schema"), data.get("candidate_id"), data.get("obstruction_id"), data.get("source_commit"), data.get("scope_literal"))
        == ("hcs-c318-ssh-finite-bulk-edge-v1", "HCS-C318", "HEN-O302", SOURCE, SCOPE),
        "identity",
    )
    need(data.get("evaluation_date") == "2026-09-03", "evaluation date")
    need(data.get("fixed_epoch") == 1788393600 and type(data.get("fixed_epoch")) is int, "epoch")
    need(data.get("evaluator") == {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    route = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    need(data.get("route_a") == route, "route")
    need(data.get("model") == EXPECTED_MODEL, "model semantics")
    need(data.get("theorem_contract") == EXPECTED_THEOREM, "theorem contract semantics")
    need(data.get("collision_boundary") == EXPECTED_COLLISIONS, "collision semantics")
    need(data.get("scope_flags") == EXPECTED_FLAGS, "scope flags")
    need(data.get("nonclaims") == EXPECTED_NONCLAIMS, "nonclaims")
    need(data.get("references") == EXPECTED_REFERENCES, "sources")
    checks[0] += 34

    check_obc(data, checks)
    check_edges(data, checks)
    check_periodic(data, checks)
    check_boundaries(data, checks)
    check_propagators(data, checks)
    check_quenches(data, checks)

    enumeration = data["enumeration"]
    exact_keys(enumeration, {"obc_polynomial_rows", "exact_edge_witnesses", "finite_threshold_rows", "periodic_rows", "periodic_momentum_cells", "boundary_rows", "propagator_rows", "propagator_selected_entries", "quench_rows", "audited_leaf_count"}, "enumeration")
    expected_enumeration = {
        "obc_polynomial_rows": len(data["obc_polynomial_rows"]),
        "exact_edge_witnesses": len(data["exact_edge_witnesses"]),
        "finite_threshold_rows": len(data["finite_threshold_rows"]),
        "periodic_rows": len(data["periodic_rows"]),
        "periodic_momentum_cells": sum(len(row["momentum_cells"]) for row in data["periodic_rows"]),
        "boundary_rows": len(data["boundary_rows"]),
        "propagator_rows": len(data["propagator_rows"]),
        "propagator_selected_entries": sum(len(row["selected_entries"]) for row in data["propagator_rows"]),
        "quench_rows": len(data["quench_rows"]),
        "audited_leaf_count": leaves(data),
    }
    need(enumeration == expected_enumeration, "enumeration")

    expected_evaluation = {
        "schema": "route-a-evaluation-v0.2.0",
        "candidate_id": "HCS-C318",
        "title": "Exact finite-size bulk--edge and quench atlas for the SSH chain",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": 1788393600,
        "scope_literal": SCOPE,
        "evaluator_authority": "route-a-evaluator",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": EVALUATOR,
        "obstruction_id": "HEN-O302",
        "candidate_definition": "The balanced finite Hermitian Su--Schrieffer--Heeger chain with real nonnegative intracell/intercell hopping, under open and periodic boundaries.",
        "family": "finite chiral bipartite quantum lattice and Bloch-band topology",
        "phase_space": "single-particle Hilbert space C^(2M), with a two-band Bloch fiber under periodic boundary conditions",
        "dynamics": "unitary Schrodinger evolution generated by the finite SSH Hamiltonian",
        "parameters": "M>=2 cells and v,w>=0; M=1 is a separately declared convention face",
        "parameter_provenance": "cell structure, hopping amplitudes, chiral block, and Bloch symbol are source SSH data",
        "arithmetic_origin": "none",
        "clock": "physical unitary time",
        "normalization": "q(k)=v+w exp(ik), winding counterclockwise when w>v; continuum and finite-ring sampled gaps are separately named",
        "determinant_convention": "finite characteristic polynomials and mode Loschmidt amplitudes are source-local; no target determinant is defined",
        "orbit_cutoff": "all-M analytic theorem; finite M<=15 receipts are regression only",
        "precision": "exact rational polynomial, threshold, edge-vector, boundary, quench, and continuum-gap receipts; 72-digit finite-sampled-gap, periodic-mode, and propagator receipts",
        "training_data": "none",
        "forbidden_data": "target arithmetic data, Euler factors, root numbers, automorphy, target divisors, target functional equations, target zeros, and Hilbert--Polya operators",
        "artifact_paths": ["results/c318_ssh_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
        "a0": {"verdict": "A0_FAIL", "strongest_evidence": "the chiral block, winding, finite edge threshold, and all hopping faces are analytic", "strongest_failure": "cell index, Bloch momentum, and continuous hoppings carry no rational-prime local payload"},
        "a1": {"verdict": "A1_FAIL", "strongest_evidence": "unitary propagation and mode-resolved quench zeros are exact source dynamics", "strongest_failure": "Bloch momentum is a parameter loop, not an arithmetic primitive-periodic-orbit ledger"},
        "a2": {"verdict": "A2_FAIL", "strongest_evidence": "the finite characteristic polynomial and periodic Fourier product are exact", "strongest_failure": "neither is a dynamical Euler product with prime-power repetition"},
        "a3": {"verdict": "A3_FAIL", "strongest_evidence": "chiral pairing, winding, and finite-size bulk--edge convergence are global source identities", "strongest_failure": "they do not supply a target functional equation, counting law, or divisor"},
        "a4": {"verdict": "A4_NATURAL_QUANTIZATION", "strongest_evidence": "the finite Hermitian hopping matrix is already a canonical self-adjoint quantum Hamiltonian", "strongest_failure": "its source lattice spectrum is not identified with target zeros and no same-clock arithmetic lift exists"},
        "tuple": route["tuple"],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "route_b_lock_reason": "no bad-prime, Euler-factor, root-number, target-divisor, or arithmetic-orbit datum exists",
        "scope_flags": EXPECTED_FLAGS,
        "theorem_status": "PROVABLE_AS_STATED",
        "finite_evidence_role": "regression and hostile-boundary evidence only; the continuant, Jacobi interlacing, hyperbolic root, Bloch winding, and entire functional-calculus proofs cover the declared all-M domain",
        "source_owner_tokens": ["10.1103/PhysRevLett.42.1698", "10.1103/PhysRevB.22.2099", "10.1007/978-3-319-25607-8_1"],
    }
    need(evaluation == expected_evaluation, "full evaluation semantics")
    checks[0] += 36
    print(f"C318 independent SSH checker: PASS ({checks[0]} checks; producer import forbidden; exact Sturm and boundary audit)")


if __name__ == "__main__":
    main()
