#!/usr/bin/env python3
"""Independent checker for the C217 rotating shallow-water certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re

import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c217_swe_evidence.json"
SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODES = [(i, j) for i in range(-3, 4) for j in range(-3, 4)]
CASES = [
    ("balanced", Fraction(1), Fraction(1)),
    ("fast_rotation", Fraction(2), Fraction(1)),
    ("fast_gravity", Fraction(1), Fraction(2)),
    ("anisotropic_rates", Fraction(3, 2), Fraction(5, 4)),
    ("zero_rotation", Fraction(0), Fraction(1)),
    ("zero_gravity", Fraction(1), Fraction(0)),
    ("fully_zero", Fraction(0), Fraction(0)),
    ("retrograde_rotation", Fraction(-1), Fraction(1)),
]
TIMES = (1.0 / 7.0, 1.0)
NUMBER_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?$")


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def matrix(f: float, c: float, n: tuple[int, int]) -> np.ndarray:
    nx, ny = n
    return np.array([[0.0, f, -1j*c*nx],
                     [-f, 0.0, -1j*c*ny],
                     [-1j*c*nx, -1j*c*ny, 0.0]], dtype=complex)


def shell_count(q: int) -> int:
    return sum(1 for i in range(-100, 101) for j in range(-100, 101)
               if i*i + j*j == q)


def divisor_formula(q: int) -> int:
    if q == 0:
        return 1
    d1 = sum(1 for d in range(1, q+1) if q % d == 0 and d % 4 == 1)
    d3 = sum(1 for d in range(1, q+1) if q % d == 0 and d % 4 == 3)
    return 4*(d1-d3)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = 0

    def check(condition: bool, label: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    def exact(actual, expected, label: str) -> None:
        check(type(actual) is type(expected), label + " type")
        check(actual == expected, label)

    top = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal",
           "evaluator", "headline", "frozen_object", "theorem", "regression",
           "exact_identities", "route_a", "scope_flags", "citations", "nonclaims",
           "payload_sha256"}
    check(set(data) == top, "top-level key closure")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    exact(data["schema"], "hcs-c217-rotating-shallow-water-v1", "schema")
    exact(data["candidate_id"], "HCS-C217", "candidate")
    exact(data["evaluation_date"], "2026-08-28", "date")
    exact(data["source_commit"], SOURCE_COMMIT, "source commit")
    exact(data["scope_literal"], SCOPE, "scope")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route verdict")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B lock")
    check(all(value is False for value in data["scope_flags"].values()), "scope firewall")
    check("beta-plane" in " ".join(data["nonclaims"]), "beta-plane boundary")
    check("Schatten" in data["theorem"]["operator_boundary"], "operator boundary")
    check("pv_invariant" in data["theorem"], "PV theorem field")
    check("iff" in data["theorem"]["periodicity"], "periodicity iff")
    check(data["regression"]["case_count"] == len(CASES), "case count")
    check(data["regression"]["modes_per_case"] == len(MODES), "mode count")

    rows = data["regression"]["cases"]
    check(len(rows) == len(CASES), "rows length")
    for ci, (row, spec) in enumerate(zip(rows, CASES)):
        case_id, fq, cq = spec
        check(set(row) == {"case_id", "f", "c", "mode_count", "modes", "shell_counts"}, f"case {ci} keys")
        exact(row["case_id"], case_id, f"case {ci} id")
        exact(row["f"], str(fq), f"case {ci} f")
        exact(row["c"], str(cq), f"case {ci} c")
        f, c = float(fq), float(cq)
        check(row["mode_count"] == len(MODES), f"case {ci} mode count")
        check(len(row["modes"]) == len(MODES), f"case {ci} mode rows")
        for mi, (mrow, n) in enumerate(zip(row["modes"], MODES)):
            check(set(mrow) == {"n", "rho", "omega", "skew_residual", "cubic_residual", "pv_residual",
                                "projector_residual", "zero_projector_rank", "times"}, f"mode {ci}/{mi} keys")
            exact(mrow["n"], [n[0], n[1]], f"mode {ci}/{mi} index")
            rho = n[0]*n[0] + n[1]*n[1]
            exact(mrow["rho"], rho, f"mode {ci}/{mi} rho")
            omega = float(np.sqrt(f*f + c*c*rho))
            check(NUMBER_RE.fullmatch(mrow["omega"]) is not None, f"mode {ci}/{mi} omega syntax")
            check(abs(float(mrow["omega"]) - omega) < 2e-14, f"mode {ci}/{mi} omega")
            G = matrix(f, c, n)
            check(np.linalg.norm(G.conj().T + G) < 2e-13, f"mode {ci}/{mi} skew")
            poly = np.poly(G)
            check(abs(poly[0] - 1) < 1e-12 and abs(poly[1]) < 2e-12
                  and abs(poly[2] - omega*omega) < 2e-10 and abs(poly[3]) < 2e-10,
                  f"mode {ci}/{mi} characteristic")
            check(float(mrow["skew_residual"]) < 2e-13, f"mode {ci}/{mi} stored skew")
            check(float(mrow["cubic_residual"]) < 2e-11, f"mode {ci}/{mi} stored cubic")
            if abs(c) > 1e-13:
                qrow = np.array([-1j*n[1], 1j*n[0], -f/c], dtype=complex)
                check(np.linalg.norm(qrow @ G) < 2e-12, f"mode {ci}/{mi} PV")
                check(float(mrow["pv_residual"]) < 2e-12, f"mode {ci}/{mi} stored PV")
            else:
                check(float(mrow["pv_residual"]) < 2e-12, f"mode {ci}/{mi} PV boundary")
            if omega > 1e-13:
                P0 = np.eye(3) + G @ G/(omega*omega)
                Pp = 0.5*(-G @ G/(omega*omega) - 1j*G/omega)
                Pm = 0.5*(-G @ G/(omega*omega) + 1j*G/omega)
                residual = max(np.linalg.norm(P0@P0-P0), np.linalg.norm(Pp@Pp-Pp),
                               np.linalg.norm(Pm@Pm-Pm), np.linalg.norm(P0@Pp),
                               np.linalg.norm(Pp@Pm), np.linalg.norm(P0+Pp+Pm-np.eye(3)))
                check(float(mrow["projector_residual"]) < 2e-11, f"mode {ci}/{mi} stored projectors")
                check(abs(float(mrow["projector_residual"]) - residual) < 2e-11,
                      f"mode {ci}/{mi} projector residual agreement")
                check(residual < 2e-11, f"mode {ci}/{mi} projectors")
                check(mrow["zero_projector_rank"] == 1, f"mode {ci}/{mi} zero rank")
                for ti, trow in enumerate(mrow["times"]):
                    check(set(trow) == {"t", "formula_residual", "unitarity_residual"}, f"time {ci}/{mi}/{ti} keys")
                    t = TIMES[ti]
                    closed = P0 + np.cos(omega*t)*(np.eye(3)-P0) + np.sin(omega*t)*G/omega
                    direct = expm(t*G)
                    check(abs(float(trow["formula_residual"])) < 2e-11, f"time {ci}/{mi}/{ti} formula")
                    check(np.linalg.norm(closed-direct) < 2e-11, f"time {ci}/{mi}/{ti} direct")
                    check(float(trow["unitarity_residual"]) < 2e-11, f"time {ci}/{mi}/{ti} unitary")
                    check(np.linalg.norm(direct.conj().T@direct-np.eye(3)) < 2e-11, f"time {ci}/{mi}/{ti} direct unitary")
            else:
                check(mrow["zero_projector_rank"] == 3, f"mode {ci}/{mi} zero degeneracy")
        check(len(row["shell_counts"]) == 19, f"case {ci} shell length")
        for srow in row["shell_counts"]:
            q = srow["q"]
            check(set(srow) == {"q", "enumerated", "formula"}, f"shell {ci}/{q} keys")
            check(srow["enumerated"] == shell_count(q), f"shell {ci}/{q} enum")
            check(srow["formula"] == divisor_formula(q), f"shell {ci}/{q} formula")
            check(srow["enumerated"] == srow["formula"], f"shell {ci}/{q} identity")
    check(len(data["exact_identities"]) == 7, "identity count")
    for identity in data["exact_identities"]:
        check(set(identity) == {"name", "formula"}, "identity keys")
        check(identity["formula"], "identity nonempty")
    for citation in data["citations"]:
        check(set(citation) == {"key", "claim", "title", "authors", "venue", "year", "doi"}, "citation closure")
        check(citation["doi"].startswith("10."), "citation DOI")
    print(f"C217 independent checker: PASS ({assertions} assertions; {len(CASES)*len(MODES)} Fourier modes)")
    print("skew-Hermitian blocks, projectors, exact exponentials, shell counts, boundary faces, and scope firewall: PASS")


if __name__ == "__main__":
    main()
