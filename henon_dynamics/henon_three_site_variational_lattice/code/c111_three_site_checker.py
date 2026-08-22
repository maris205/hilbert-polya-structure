#!/usr/bin/env python3
"""Independent semantic checker for the C111 three-site evidence file."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c111_three_site_evidence.json"
A, K, Z, O, N = Fraction(7), Fraction(1, 5), Fraction(0), Fraction(1), 3
L = ((Fraction(2), Fraction(-1), Fraction(-1)),
     (Fraction(-1), Fraction(2), Fraction(-1)),
     (Fraction(-1), Fraction(-1), Fraction(2)))
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def parse(x: dict[str, int]) -> Fraction:
    return Fraction(int(x["numerator"]), int(x["denominator"]))


def vec(x: list[dict[str, int]]) -> tuple[Fraction, ...]:
    return tuple(parse(v) for v in x)


def mat(x: list[list[dict[str, int]]]) -> list[list[Fraction]]:
    return [[parse(v) for v in row] for row in x]


def eye(n: int) -> list[list[Fraction]]:
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def mm(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Z)
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a: list[list[Fraction]]) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def det(a: list[list[Fraction]]) -> Fraction:
    n = len(a)
    ans = Z
    for p in itertools.permutations(range(n)):
        sign = O if sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n)) % 2 == 0 else -O
        term = sign
        for i, j in enumerate(p):
            term *= a[i][j]
        ans += term
    return ans


def padd(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [(a[i] if i < len(a) else Z) + (b[i] if i < len(b) else Z)
            for i in range(max(len(a), len(b)))]


def pmul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Z] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def detpoly(j: list[list[Fraction]]) -> list[Fraction]:
    n = len(j)
    total = [Z]
    for p in itertools.permutations(range(n)):
        sign = O if sum(p[i] > p[k] for i in range(n) for k in range(i + 1, n)) % 2 == 0 else -O
        term = [sign]
        for i, c in enumerate(p):
            term = pmul(term, [O, -j[i][c]] if i == c else [Z, -j[i][c]])
        total = padd(total, term)
    while len(total) > 1 and total[-1] == Z:
        total.pop()
    return total


def gradient(q: tuple[Fraction, Fraction, Fraction], coupling: Fraction = K) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(A * q[i] - q[i] * q[i] - coupling * sum(L[i][j] * q[j] for j in range(N)) for i in range(N))  # type: ignore[return-value]


def direct_gradient(q: tuple[Fraction, Fraction, Fraction], coupling: Fraction = K) -> tuple[Fraction, Fraction, Fraction]:
    """Different implementation using the three edge differences explicitly."""
    x, y, w = q
    return (
        A * x - x * x - coupling * ((x - y) + (x - w)),
        A * y - y * y - coupling * ((y - x) + (y - w)),
        A * w - w * w - coupling * ((w - x) + (w - y)),
    )


def hessian(q: tuple[Fraction, Fraction, Fraction], coupling: Fraction = K) -> list[list[Fraction]]:
    return [[(A - 2 * q[i] if i == j else Z) - coupling * L[i][j] for j in range(N)] for i in range(N)]


def jac(q: tuple[Fraction, Fraction, Fraction], coupling: Fraction = K) -> list[list[Fraction]]:
    h = hessian(q, coupling)
    return [h[i] + [(-O if i == j else Z) for j in range(N)] for i in range(N)] + [[(O if i == j else Z) for j in range(N)] + [Z] * N for i in range(N)]


def fmap(s: tuple[Fraction, ...], coupling: Fraction = K) -> tuple[Fraction, ...]:
    q, p = s[:N], s[N:]
    g = gradient(q, coupling)  # type: ignore[arg-type]
    return tuple(g[i] - p[i] for i in range(N)) + tuple(q)


def inverse(s: tuple[Fraction, ...], coupling: Fraction = K) -> tuple[Fraction, ...]:
    q, p = s[:N], s[N:]
    g = gradient(p, coupling)  # type: ignore[arg-type]
    return tuple(p) + tuple(g[i] - q[i] for i in range(N))


def swap(s: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(s[N:]) + tuple(s[:N])


def omega() -> list[list[Fraction]]:
    return [[(O if j == i + N else Z) for j in range(2 * N)] for i in range(N)] + [[(-O if j == i - N else Z) for j in range(2 * N)] for i in range(N, 2 * N)]


def zero(m: list[list[Fraction]]) -> bool:
    return all(x == Z for row in m for x in row)


def check_orbit(row: dict[str, object], expected: list[tuple[Fraction, ...]]) -> None:
    states = [vec(v) for v in row["states"]]  # type: ignore[index]
    assert states == expected
    assert row["period"] == len(expected)
    assert row["primitive_verified"] is (len(expected) == 1 or expected[0] != expected[1])
    assert row["cycle_closure_verified"] is (fmap(expected[-1]) == expected[0])
    js = [jac(tuple(s[:N])) for s in states]
    mono = eye(2 * N)
    for j in js:
        mono = mm(j, mono)
    assert mat(row["jacobian_at_first"]) == js[0]  # type: ignore[arg-type]
    assert mat(row["monodromy"]) == mono  # type: ignore[arg-type]
    assert parse(row["monodromy_determinant"]) == det(mono)  # type: ignore[arg-type]
    assert parse(row["monodromy_trace"]) == tr(mono)  # type: ignore[arg-type]
    assert tuple(vec(row["det_I_minus_z_monodromy"])) == tuple(detpoly(mono))  # type: ignore[arg-type]
    om = omega()
    for j in js:
        jt = list(map(list, zip(*j)))
        assert zero([[mm(mm(jt, om), j)[i][k] - om[i][k] for k in range(2 * N)] for i in range(2 * N)])
    assert row["symplectic_at_each_step"] is True


def validate_evidence_path(path: Path = EVIDENCE) -> dict[str, object]:
    raw = path.read_bytes()
    value = json.loads(raw)
    assert raw == canonical(value)
    assert value["schema_id"] == "hcs-c111-three-site-variational-henon-lattice-prefreeze-v1"
    assert value["status"] == "PREFREEZE_G3_PASS"
    assert value["scope_literal"] == FIREWALL
    assert value["model"]["parameters"] == {"a": {"numerator": 7, "denominator": 1}, "kappa": {"numerator": 1, "denominator": 5}, "sites": 3}
    assert value["model"]["laplacian"] == [[{"numerator": int(L[i][j]), "denominator": 1} for j in range(N)] for i in range(N)]
    fixed = value["certified_orbit_ledger"]["fixed_rows"]
    check_orbit(fixed[0], [(Z,) * 6])
    check_orbit(fixed[1], [(Fraction(5),) * 6])
    cycle = value["certified_orbit_ledger"]["period_two_rows"]
    expected_cycle = [(Fraction(3),) * 3 + (Fraction(6),) * 3, (Fraction(6),) * 3 + (Fraction(3),) * 3]
    assert len(cycle) == 1
    check_orbit(cycle[0], expected_cycle)

    modes = value["fourier_mode_witness"]
    assert vec(modes["laplacian_eigenvalues"]) == (Z, Fraction(3), Fraction(3))
    assert vec(modes["hessian_mode_at_q3"]) == (O, Fraction(2, 5), Fraction(2, 5))
    assert vec(modes["hessian_mode_at_q6"]) == (Fraction(-5), Fraction(-28, 5), Fraction(-28, 5))
    mode_traces = vec(modes["period_two_mode_traces"])
    assert mode_traces == (Fraction(-7), Fraction(-106, 25), Fraction(-106, 25))
    assert modes["transverse_multiplicity"] == 2
    assert modes["reconstruction_matches_direct"] is True
    assert vec(modes["reconstructed_full_det_I_minus_z"]) == tuple(parse(x) for x in value["certified_orbit_ledger"]["period_two_rows"][0]["det_I_minus_z_monodromy"])

    controls = value["controls"]
    cmono = mm(jac((Fraction(6),) * 3), jac((Fraction(3),) * 3))
    umono = mm(jac((Fraction(6),) * 3, Z), jac((Fraction(3),) * 3, Z))
    assert mat(controls["uncoupled_kappa_zero_period_two_monodromy"]) == umono
    assert vec(controls["uncoupled_det_I_minus_z"]) == tuple(detpoly(umono))
    assert vec(controls["coupled_det_I_minus_z"]) == tuple(detpoly(cmono))
    assert parse(controls["trace_difference_coupled_minus_uncoupled"]) == tr(cmono) - tr(umono)
    assert parse(controls["z2_coefficient_difference_coupled_minus_uncoupled"]) == detpoly(cmono)[2] - detpoly(umono)[2]
    assert controls["mixed_trace_is_nonzero"] is True and controls["mixed_z2_coefficient_is_nonzero"] is True

    samples = [
        (Fraction(1, 2), Fraction(-1, 3), Fraction(2, 5), Fraction(-3, 7), Fraction(1, 4), Fraction(-2, 3)),
        (Fraction(-2), Fraction(1), Z, Fraction(3, 2), Fraction(-1, 5), Fraction(4, 3)),
        (Fraction(4, 3), Fraction(5, 7), Fraction(-1, 2), Fraction(2, 3), Fraction(3, 5), Fraction(-4, 7)),
    ]
    assert all(swap(fmap(swap(s))) == inverse(s) for s in samples)
    for s in samples:
        q, p = s[:N], s[N:]
        g = gradient(q)  # type: ignore[arg-type]
        # Direct edge-wise gradient and the differential of
        # S(q,p)=U(q)-p dot q.
        assert g == direct_gradient(q)  # type: ignore[arg-type]
        dg = direct_gradient(q)  # type: ignore[arg-type]
        assert tuple(g[i] - p[i] for i in range(N)) + tuple(-q[i] for i in range(N)) == tuple(dg[i] - p[i] for i in range(N)) + tuple(-q[i] for i in range(N))

    for q in [(Z,) * 3, (Fraction(5),) * 3, (Fraction(3),) * 3, (Fraction(6),) * 3]:
        j = jac(q)
        jt = list(map(list, zip(*j)))
        assert zero([[mm(mm(jt, omega()), j)[i][k] - omega()[i][k] for k in range(6)] for i in range(6)])
        assert det(j) == O
    assert gradient((Z,) * 3) == (Z, Z, Z)
    assert gradient((Fraction(5),) * 3) == (Fraction(10),) * 3
    assert fmap(expected_cycle[0]) == expected_cycle[1] and fmap(expected_cycle[1]) == expected_cycle[0]

    for key, flag in value["checks"].items():
        assert flag is True, key
    assert value["claims"]["complete_primitive_orbit_atlas"] is False
    assert value["claims"]["fredholm_determinant_constructed"] is False
    assert value["claims"]["euler_factors_claimed"] is False
    assert value["claims"]["exact_fourier_mode_witness"] is True
    assert value["route_a_verdict"] == {
        "A1": "A1_WEAK", "A1_qualification": "PARTIAL_CERTIFIED_LOW_PERIOD_ONLY",
        "A2": "A2_FAIL", "A2_qualification": "OPERATOR_OWNER_OPEN",
        "A3": "A3_NOT_ADDRESSED", "A4": "A4_FAIL", "overall": "ROUTE_A_EXPLORATORY",
    }
    return {"status": "C111_INDEPENDENT_CHECK_PASS", "evidence_sha256": digest(raw), "fixed_count": 2, "period_two_count": 1}


def main() -> None:
    print(json.dumps(validate_evidence_path(), sort_keys=True))


if __name__ == "__main__":
    main()
