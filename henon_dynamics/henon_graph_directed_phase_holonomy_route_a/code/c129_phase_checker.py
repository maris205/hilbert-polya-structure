#!/usr/bin/env python3
"""Independent standard-library checker for C129; imports no producer code."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c129_phase_evidence.json"


def fs(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


class Ring:
    def __init__(self, row=None):
        self.row = tuple(Fraction(v) for v in (row if row is not None else [0] * 5))

    @classmethod
    def one_at(cls, exponent, coefficient=1):
        row = [Fraction(0)] * 5
        row[exponent % 5] = Fraction(coefficient)
        return cls(row)

    @classmethod
    def scalar(cls, value):
        return cls.one_at(0, value)

    def __add__(self, other):
        return Ring([a + b for a, b in zip(self.row, other.row)])

    def __neg__(self):
        return Ring([-a for a in self.row])

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        out = [Fraction(0)] * 5
        for i, a in enumerate(self.row):
            for j, b in enumerate(other.row):
                out[(i + j) % 5] += a * b
        return Ring(out)

    def __eq__(self, other):
        return isinstance(other, Ring) and self.row == other.row

    def scale(self, value):
        return Ring([Fraction(value) * a for a in self.row])

    def augmentation(self):
        return sum(self.row)

    def cyclo(self):
        return tuple(self.row[k] - self.row[4] for k in range(4))


def add_many(items):
    total = Ring()
    for item in items:
        total = total + item
    return total


def eye(n):
    return [[Ring.scalar(i == j) for j in range(n)] for i in range(n)]


def mmul(a, b):
    return [[add_many(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def mpow(a, n):
    out = eye(len(a))
    base = a
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def tr(a):
    return add_many(a[i][i] for i in range(len(a)))


def ring_matrix(B, weights, exponents):
    return [[Ring.one_at(exponents[j], weights[j] * B[i][j]) for j in range(3)] for i in range(3)]


def coeffs(traces, degree):
    out = [Ring.scalar(1)]
    for n in range(1, degree + 1):
        total = add_many(traces[k] * out[n - k] for k in range(1, n + 1))
        out.append((-total).scale(Fraction(1, n)))
    return out


def receipt(x):
    return {
        "group_ring_Z5_e0_to_e4": [fs(v) for v in x.row],
        "primitive_zeta5_basis_1_zeta_zeta2_zeta3": [fs(v) for v in x.cyclo()],
        "trivial_character_augmentation": fs(x.augmentation()),
    }


def admissible(word, B):
    return all(B[word[k]][word[(k + 1) % len(word)]] for k in range(len(word)))


def primitive(word):
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def mul2(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def vec2(a, v):
    return [sum(a[i][j] * v[j] for j in range(2)) for i in range(2)]


def solve2(a, b):
    d = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return [(b[0] * a[1][1] - a[0][1] * b[1]) / d, (a[0][0] * b[1] - b[0] * a[1][0]) / d]


def cycle(A, translations, word):
    M = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    b = [Fraction(0), Fraction(0)]
    for symbol in word:
        b = [v + w for v, w in zip(vec2(A, b), [Fraction(translations[symbol]), Fraction(0)])]
        M = mul2(A, M)
    p = solve2([[Fraction(i == j) - M[i][j] for j in range(2)] for i in range(2)], b)
    phases = []
    for symbol in word:
        phases.append(p)
        p = [v + w for v, w in zip(vec2(A, p), [Fraction(translations[symbol]), Fraction(0)])]
    return M, phases


def claims_hash(claims):
    raw = json.dumps(claims, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(path.read_text())
    checks = 0

    def ck(condition, label):
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    def ck_keys(mapping, expected, label):
        ck(set(mapping) == set(expected), label)

    ck_keys(data, {"schema", "scope_literal", "claims_sha256", "claims"}, "payload key schema")
    ck(data["schema"] == "hcs-c129-phase-holonomy-v1", "schema")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["claims_sha256"] == claims_hash(data["claims"]), "repaired claims hash")
    c = data["claims"]
    ck_keys(
        c,
        {
            "source_lock", "frozen_model", "geometry", "periodic_orbits",
            "trace_and_fredholm", "controls", "progress_over_prior_gate",
            "verdict", "nonclaims",
        },
        "claims key schema",
    )

    A = [[Fraction(3, 16), Fraction(-1, 32)], [Fraction(1, 4), Fraction(0)]]
    B = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
    t = [-2, 0, 2]
    tc = [0, -2, 2]
    e = [3, 0, 2]
    ec = [0, 3, 2]
    W = ring_matrix(B, weights, e)
    Wc = ring_matrix(B, weights, ec)

    lock = c["source_lock"]
    ck_keys(
        lock,
        {
            "candidate_id", "phase_space", "clock", "normalization",
            "determinant_convention", "orbit_cutoff", "precision", "forbidden_data",
        },
        "source lock key schema",
    )
    ck(lock["candidate_id"] == "HCS-C129", "id")
    ck(lock["determinant_convention"] == "D_chi(z)=det(I-z*L_chi)", "det convention")
    ck(lock["orbit_cutoff"].startswith("none in theorem"), "cutoff")
    ck("prime tables" in lock["forbidden_data"], "forbidden")
    model = c["frozen_model"]
    ck_keys(
        model,
        {
            "A", "A_eigenvalues", "B", "weights", "translations",
            "holonomy_exponents_mod5", "character", "operator",
        },
        "frozen model key schema",
    )
    ck(model["A"] == [[fs(v) for v in row] for row in A], "A")
    ck(model["A_eigenvalues"] == ["1/8", "1/16"], "A eigenvalues")
    ck(model["B"] == [[str(v) for v in row] for row in B], "B")
    ck(model["weights"] == [fs(v) for v in weights], "weights")
    ck(model["translations"] == [str(v) for v in t], "translations")
    ck(model["holonomy_exponents_mod5"] == e, "exponents")
    ck(model["character"] == "chi(m)=zeta_5^m with zeta_5 primitive", "character")
    ck(
        model["operator"]
        == "(L_chi f)_i=sum_j B_ij*c_j*zeta_5^(t_j)*f_j(phi_j(z))",
        "operator headline",
    )
    geom = c["geometry"]
    ck_keys(
        geom,
        {
            "A_infinity_norm", "first_coordinate_radius", "second_coordinate_radius",
            "pairwise_gap", "strict_interior", "strong_separation",
        },
        "geometry key schema",
    )
    ck(geom["A_infinity_norm"] == "1/4", "norm")
    ck(geom["first_coordinate_radius"] == "21/32", "first radius")
    ck(geom["second_coordinate_radius"] == "3/4", "second radius")
    ck(geom["pairwise_gap"] == "11/16", "gap")
    ck(geom["strict_interior"] is True and geom["strong_separation"] is True, "geometry")

    rooted_counts = {}
    reps_by_n = {}
    hist = {}
    histc = {}
    for n in range(1, 9):
        rooted = [w for w in itertools.product(range(3), repeat=n) if admissible(w, B)]
        reps = sorted({least_rotation(w) for w in rooted if primitive(w)})
        rooted_counts[str(n)] = len(rooted)
        reps_by_n[str(n)] = ["".join(map(str, w)) for w in reps]
        h = [0] * 5
        hc = [0] * 5
        for w in reps:
            h[sum(e[j] for j in w) % 5] += 1
            hc[sum(ec[j] for j in w) % 5] += 1
        hist[str(n)] = h
        histc[str(n)] = hc
    po = c["periodic_orbits"]
    ck_keys(
        po,
        {
            "all_period_primitive_coding", "rooted_counts_n1_to_8",
            "primitive_representatives_n1_to_8",
            "primitive_holonomy_histogram_original_n1_to_8",
            "primitive_holonomy_histogram_control_n1_to_8", "example_word",
            "example_holonomy_original", "example_monodromy", "example_phase_points",
        },
        "periodic orbit key schema",
    )
    ck(po["all_period_primitive_coding"] is True, "all-period primitive coding")
    ck(po["rooted_counts_n1_to_8"] == rooted_counts, "rooted counts")
    ck(po["primitive_representatives_n1_to_8"] == reps_by_n, "primitive reps")
    ck(po["primitive_holonomy_histogram_original_n1_to_8"] == hist, "original hist")
    ck(po["primitive_holonomy_histogram_control_n1_to_8"] == histc, "control hist")
    ck(sum(rooted_counts.values()) == 284, "rooted total")
    ck(sum(len(v) for v in reps_by_n.values()) == 40, "primitive total")

    M, phases = cycle(A, t, (0, 1, 2))
    Mc, phasesc = cycle(A, tc, (0, 1, 2))
    ck(M == Mc, "same monodromy")
    ck(po["example_word"] == "012" and po["example_holonomy_original"] == "zeta_5^0=1", "example")
    ck(po["example_monodromy"] == [[fs(v) for v in row] for row in M], "example M")
    ck(po["example_phase_points"] == [[fs(v) for v in p] for p in phases], "example points")

    delta = [Ring.scalar(1), -Ring.one_at(3, Fraction(1, 2)), -Ring.one_at(3, Fraction(1, 6)), -Ring.scalar(Fraction(1, 30))]
    deltac = [Ring.scalar(1), -Ring.scalar(Fraction(1, 2)), -Ring.one_at(3, Fraction(1, 6)), -Ring.scalar(Fraction(1, 30))]
    traces = {}
    tracesc = {}
    for n in range(1, 9):
        den = (1 - Fraction(1, 8) ** n) * (1 - Fraction(1, 16) ** n)
        traces[n] = tr(mpow(W, n)).scale(1 / den)
        tracesc[n] = tr(mpow(Wc, n)).scale(1 / den)
    ds = coeffs(traces, 8)
    dsc = coeffs(tracesc, 8)
    tf = c["trace_and_fredholm"]
    ck_keys(
        tf,
        {
            "trace_class", "all_order_trace_formula", "all_order_lattice_product",
            "primitive_product", "symbolic_delta_original_z0_to_z3",
            "power_traces_original_n1_to_8", "fredholm_coefficients_original_z0_to_z8",
        },
        "trace and Fredholm key schema",
    )
    ck(tf["trace_class"] is True, "trace class")
    ck(
        tf["all_order_trace_formula"]
        == "Tr(L_chi^n)=Tr(W_chi^n)/((1-8^(-n))*(1-16^(-n)))",
        "all-order trace formula headline",
    )
    ck(tf["symbolic_delta_original_z0_to_z3"] == [receipt(v) for v in delta], "delta")
    ck(tf["power_traces_original_n1_to_8"] == {str(n): receipt(traces[n]) for n in range(1, 9)}, "traces")
    ck(tf["fredholm_coefficients_original_z0_to_z8"] == [receipt(v) for v in ds], "coefficients")
    ck(
        tf["all_order_lattice_product"]
        == "D_chi(z)=product_{r,s>=0} det(I-z*8^(-r)*16^(-s)*W_chi)",
        "lattice product headline",
    )
    ck(
        tf["primitive_product"]
        == "log D_chi=-sum_[gamma]sum_m (c_gamma*chi(M_gamma)*z^ell)^m/(m*det(I-A^(m*ell)))",
        "primitive product headline",
    )

    controls = c["controls"]
    ck_keys(
        controls,
        {
            "control_translations", "control_holonomy_exponents_mod5",
            "same_unordered_image_centers", "same_strong_separation",
            "same_untwisted_all_order_trace_and_determinant",
            "twisted_symbolic_delta_control_z0_to_z3", "power_traces_control_n1_to_8",
            "fredholm_coefficients_control_z0_to_z8", "control_example_phase_points",
            "positive_control", "negative_control", "trivial_character_degenerates_to_C124",
            "sensitivity_boundary",
        },
        "controls key schema",
    )
    ck(controls["control_translations"] == [str(v) for v in tc], "control translations")
    ck(controls["control_holonomy_exponents_mod5"] == ec, "control exponents")
    ck(controls["twisted_symbolic_delta_control_z0_to_z3"] == [receipt(v) for v in deltac], "control delta")
    ck(controls["power_traces_control_n1_to_8"] == {str(n): receipt(tracesc[n]) for n in range(1, 9)}, "control traces")
    ck(controls["fredholm_coefficients_control_z0_to_z8"] == [receipt(v) for v in dsc], "control coefficients")
    ck(controls["control_example_phase_points"] == [[fs(v) for v in p] for p in phasesc], "control points")
    ck(traces[1] != tracesc[1] and ds[1] != dsc[1], "positive sensitivity")
    ck(all(traces[n].augmentation() == tracesc[n].augmentation() for n in range(1, 9)), "negative trace control")
    ck(all(ds[n].augmentation() == dsc[n].augmentation() for n in range(9)), "negative coefficient control")
    ck(controls["same_unordered_image_centers"] is True, "same centers control")
    ck(controls["same_strong_separation"] is True, "same separation control")
    ck(controls["same_untwisted_all_order_trace_and_determinant"] is True, "untwisted theorem")
    ck(controls["trivial_character_degenerates_to_C124"] is True, "C124 degeneration")
    ck(
        controls["positive_control"]
        == "the primitive-zeta_5 linear Fredholm coefficient changes from -(64/105)zeta_5^3 to -64/105",
        "positive control headline",
    )
    ck(
        controls["negative_control"]
        == "the trivial-character augmentation of every checked trace and coefficient agrees exactly",
        "negative control headline",
    )
    ck(
        controls["sensitivity_boundary"]
        == "position-sensitive only through the frozen translation-lattice character and branch assignment; no complete geometry recovery",
        "sensitivity boundary",
    )

    verdict = c["verdict"]
    ck_keys(
        verdict,
        {"A1", "A2", "A3", "A4", "overall", "route_b_invocation_allowed"},
        "verdict key schema",
    )
    ck(verdict["A1"] == "A1_WEAK", "A1")
    ck(verdict["A2"] == "A2_FAIL", "A2")
    ck(verdict["A3"] == "A3_FAIL", "A3")
    ck(verdict["A4"] == "A4_FORMAL_HINT", "A4")
    ck(verdict["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(verdict["route_b_invocation_allowed"] is False, "route B")
    ck(
        c["nonclaims"]
        == [
            "complete geometric recovery from holonomy",
            "a target-facing zero or divisor match",
            "prime-like information, arithmetic/local data, Euler factors, root numbers, or automorphy",
            "a self-adjoint Hilbert--Polya operator or Riemann-zero correspondence",
            "a unitary quantization or Route-B authorization",
        ],
        "nonclaims",
    )
    ck(
        c["progress_over_prior_gate"]
        == {
            "over_C124": "restores exact phase sensitivity to translation residues and branch assignment while retaining the same all-period nuclear owner",
            "remaining_obstruction": "the character sees only one finite quotient of the translation lattice and no target divisor is compared",
        },
        "complete progress over prior gate",
    )

    print(json.dumps({"status": "C129_INDEPENDENT_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
