#!/usr/bin/env python3
"""Independent semantic checker for the C106 exact variational audit."""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
from hashlib import sha256
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c106_variational_lattice_evidence.json"
A = Fraction(7)
K = Fraction(1, 4)
Z = Fraction(0)
O = Fraction(1)
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def parse(x: dict[str, int]) -> Fraction:
    return Fraction(int(x["numerator"]), int(x["denominator"]))


def parse_vec(xs: list[dict[str, int]]) -> tuple[Fraction, ...]:
    return tuple(parse(x) for x in xs)


def parse_mat(xs: list[list[dict[str, int]]]) -> list[list[Fraction]]:
    return [[parse(x) for x in row] for row in xs]


def rat(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Z) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def eye(n: int) -> list[list[Fraction]]:
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def omega() -> list[list[Fraction]]:
    z = [[Z, Z], [Z, Z]]
    i = eye(2)
    mi = [[-x for x in row] for row in i]
    return [z[0] + i[0], z[1] + i[1], mi[0] + z[0], mi[1] + z[1]]


def determinant(a: list[list[Fraction]]) -> Fraction:
    n = len(a)
    out = Z
    for p in itertools.permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = O if inv % 2 == 0 else -O
        for i, j in enumerate(p):
            term *= a[i][j]
        out += term
    return out


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [(a[i] if i < len(a) else Z) + (b[i] if i < len(b) else Z) for i in range(max(len(a), len(b)))]


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Z] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def det_i_minus_zj(j: list[list[Fraction]]) -> list[Fraction]:
    total = [Z]
    for p in itertools.permutations(range(4)):
        inv = sum(p[i] > p[k] for i in range(4) for k in range(i + 1, 4))
        term = [O if inv % 2 == 0 else -O]
        for i, col in enumerate(p):
            term = poly_mul(term, [O, -j[i][col]] if i == col else [Z, -j[i][col]])
        total = poly_add(total, term)
    while len(total) > 1 and total[-1] == Z:
        total.pop()
    return total


def gradient(q: tuple[Fraction, Fraction], coupling: Fraction = K) -> tuple[Fraction, Fraction]:
    x, y = q
    return (A * x - x * x - coupling * (x - y), A * y - y * y + coupling * (x - y))


def hessian(q: tuple[Fraction, Fraction], coupling: Fraction = K) -> list[list[Fraction]]:
    x, y = q
    return [[A - coupling - 2 * x, coupling], [coupling, A - coupling - 2 * y]]


def jacobian(q: tuple[Fraction, Fraction], coupling: Fraction = K) -> list[list[Fraction]]:
    h = hessian(q, coupling)
    return [h[0] + [-O, Z], h[1] + [Z, -O], [O, Z, Z, Z], [Z, O, Z, Z]]


def map_state(s: tuple[Fraction, Fraction, Fraction, Fraction], coupling: Fraction = K) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    x, y, u, v = s
    gx, gy = gradient((x, y), coupling)
    return (gx - u, gy - v, x, y)


def inverse_state(s: tuple[Fraction, Fraction, Fraction, Fraction], coupling: Fraction = K) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    x, y, u, v = s
    gu, gv = gradient((u, v), coupling)
    return (u, v, gu - x, gv - y)


def reversor(s: tuple[Fraction, Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    return (s[2], s[3], s[0], s[1])


def zero_matrix(a: list[list[Fraction]]) -> bool:
    return all(x == Z for row in a for x in row)


def cycle_row(row: dict[str, object], expected_states: list[tuple[Fraction, Fraction, Fraction, Fraction]]) -> None:
    states = [parse_vec(x) for x in row["states"]]  # type: ignore[index]
    assert states == expected_states
    assert row["period"] == len(states)
    assert bool(row["primitive_verified"]) == (len(states) == 1 or states[0] != states[1])
    assert bool(row["cycle_closure_verified"]) == (map_state(states[-1]) == states[0])
    matrices = [jacobian((s[0], s[1])) for s in states]
    mono = eye(4)
    for j in matrices:
        mono = matmul(j, mono)
    assert parse_mat(row["jacobian_at_first"]) == matrices[0]  # type: ignore[arg-type]
    assert parse_mat(row["monodromy"]) == mono  # type: ignore[arg-type]
    assert parse(row["monodromy_determinant"]) == determinant(mono)  # type: ignore[arg-type]
    assert parse(row["monodromy_trace"]) == sum(mono[i][i] for i in range(4))
    j0sq = matmul(matrices[0], matrices[0])
    assert parse(row["monodromy_trace_square_at_first"]) == sum(j0sq[i][i] for i in range(4))
    assert parse_vec(row["det_I_minus_z_monodromy"]) == tuple(det_i_minus_zj(mono))  # type: ignore[arg-type]
    for j in matrices:
        om = omega()
        jt = transpose(j)
        diff = [[matmul(matmul(jt, om), j)[i][k] - om[i][k] for k in range(4)] for i in range(4)]
        assert zero_matrix(diff)
    assert row["symplectic_at_each_step"] is True


def validate_evidence_path(path: Path = EVIDENCE) -> dict[str, object]:
    raw = path.read_bytes()
    value = json.loads(raw)
    assert raw == canonical(value)
    assert value["schema_id"] == "hcs-c106-variational-coupled-henon-lattice-prefreeze-v1"
    assert value["status"] == "PREFREEZE_G3_PASS"
    assert value["scope_literal"] == FIREWALL
    assert value["model"]["parameters"]["a"] == rat(A)
    assert value["model"]["parameters"]["kappa"] == rat(K)
    ledger = value["certified_orbit_ledger"]
    fixed_rows = ledger["fixed_rows"]
    assert len(fixed_rows) == 2
    cycle_row(fixed_rows[0], [(Z, Z, Z, Z)])
    cycle_row(fixed_rows[1], [(Fraction(5), Fraction(5), Fraction(5), Fraction(5))])
    cycles = ledger["period_two_rows"]
    assert len(cycles) == 1
    cycle_row(cycles[0], [(Fraction(3), Fraction(3), Fraction(6), Fraction(6)), (Fraction(6), Fraction(6), Fraction(3), Fraction(3))])
    # Independent period-two trace and polynomial control.
    states = [(Fraction(3), Fraction(3), Fraction(6), Fraction(6)), (Fraction(6), Fraction(6), Fraction(3), Fraction(3))]
    cmono = matmul(jacobian((6, 6)), jacobian((3, 3)))
    umono = matmul(jacobian((6, 6), Z), jacobian((3, 3), Z))
    controls = value["controls"]
    assert parse_mat(controls["uncoupled_kappa_zero_period_two_monodromy"]) == umono
    assert parse_vec(controls["uncoupled_det_I_minus_z"]) == tuple(det_i_minus_zj(umono))
    assert parse_vec(controls["coupled_det_I_minus_z"]) == tuple(det_i_minus_zj(cmono))
    delta = sum(cmono[i][i] for i in range(4)) - sum(umono[i][i] for i in range(4))
    assert parse(controls["trace_difference_coupled_minus_uncoupled"]) == delta
    assert parse(controls["z2_coefficient_difference_coupled_minus_uncoupled"]) == det_i_minus_zj(cmono)[2] - det_i_minus_zj(umono)[2]
    assert controls["mixed_trace_is_nonzero"] is True and controls["mixed_z2_coefficient_is_nonzero"] is True
    # Reversor checks at exact points not used by the producer's output rows.
    samples = [(Fraction(1, 2), Fraction(-1, 3), Fraction(2, 5), Fraction(-3, 7)), (Fraction(-2), Fraction(1), Z, Fraction(3, 2)), (Fraction(4, 3), Fraction(5, 7), Fraction(-1, 2), Fraction(2, 3))]
    assert all(reversor(map_state(reversor(s))) == inverse_state(s) for s in samples)
    primitive_checks = []
    for x, y, u, v in samples:
        gx, gy = gradient((x, y))
        ux = A * x - x * x - K * (x - y)
        uy = A * y - y * y + K * (x - y)
        primitive_checks.append((gx - u, gy - v, -x, -y) == (ux - u, uy - v, -x, -y))
    assert all(primitive_checks)
    checks = value["checks"]
    for key in checks:
        assert checks[key] is True
    claims = value["claims"]
    assert claims["complete_primitive_orbit_atlas"] is False
    assert claims["fredholm_determinant_constructed"] is False
    assert claims["euler_factors_claimed"] is False
    verdict = value["route_a_verdict"]
    assert verdict == {
        "A1": "A1_WEAK",
        "A1_qualification": "PARTIAL_CERTIFIED_LOW_PERIOD_ONLY",
        "A2": "A2_FAIL",
        "A2_qualification": "OPERATOR_OWNER_OPEN",
        "A3": "A3_NOT_ADDRESSED",
        "A4": "A4_FAIL",
        "overall": "ROUTE_A_EXPLORATORY",
    }
    return {"status": "C106_INDEPENDENT_CHECK_PASS", "evidence_sha256": digest(raw), "fixed_count": 2, "period_two_count": 1}


def main() -> None:
    print(json.dumps(validate_evidence_path(), sort_keys=True))


if __name__ == "__main__":
    main()
