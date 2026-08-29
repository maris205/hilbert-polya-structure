#!/usr/bin/env python3
"""Canonical source-local ledger for the finite open Toda chain.

The executable receipt separates theorem-level identities (Hamiltonian/Lax
form, isospectrality, norming-coordinate flow, and the N=2 closed form) from
finite-step diagnostics.  No arithmetic labels or target spectra are used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c230_open_toda_evidence.json"
WORKING_DIGITS = 90
SERIALIZED_DIGITS = 72
RK_STEPS_PER_UNIT = 256
LEDGER_TIMES = [F(-2), F(-1), F(0), F(1), F(2)]
SCATTER_T = F(8)

# Positive Jacobi off-diagonals and rational diagonal data are the frozen
# source parameters.  q differences are reconstructed as q_j-q_{j+1}=2 log(2a_j)
# and p_j=-2 b_j; no external data select these rows.
PARAMETERS = [
    {"case_id": "N2_reference", "N": 2, "a": [F(1)], "b": [F(1, 2), F(-1, 2)]},
    {"case_id": "N2_asymmetric", "N": 2, "a": [F(3, 4)], "b": [F(1, 3), F(-1, 6)]},
    {"case_id": "N2_near_free", "N": 2, "a": [F(1, 10)], "b": [F(1, 5), F(-1, 5)]},
    {"case_id": "N3_symmetric", "N": 3, "a": [F(1), F(1)], "b": [F(1), F(0), F(-1)]},
    {"case_id": "N3_generic", "N": 3, "a": [F(1, 2), F(3, 2)], "b": [F(1, 2), F(-1, 4), F(1, 3)]},
    {"case_id": "N3_weak_links", "N": 3, "a": [F(1, 8), F(1, 6)], "b": [F(2, 5), F(-1, 10), F(-3, 10)]},
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F | int) -> mp.mpf:
    if isinstance(x, F):
        return mp.mpf(x.numerator) / x.denominator
    return mp.mpf(x)


def fmt(x: mp.mpf | mp.mpc) -> str:
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False)


def matrix_from_ab(a: list[mp.mpf], b: list[mp.mpf]) -> mp.matrix:
    n = len(b)
    L = mp.matrix(n)
    for i in range(n):
        L[i, i] = b[i]
        if i + 1 < n:
            L[i, i + 1] = a[i]
            L[i + 1, i] = a[i]
    return L


def invariants(a: list[mp.mpf], b: list[mp.mpf]) -> list[mp.mpf]:
    L = matrix_from_ab(a, b)
    n = len(b)
    values = []
    for k in range(1, n + 1):
        P = L ** k
        values.append(sum(P[i, i] for i in range(n)) / k)
    return values


def eigvals_desc(a: list[mp.mpf], b: list[mp.mpf]) -> list[mp.mpf]:
    vals, _ = mp.eigsy(matrix_from_ab(a, b))
    return sorted([mp.re(vals[i]) for i in range(len(b))], reverse=True)


def spectral_weights_desc(a: list[mp.mpf], b: list[mp.mpf]) -> tuple[list[mp.mpf], list[mp.mpf]]:
    vals, vecs = mp.eigsy(matrix_from_ab(a, b))
    pairs = sorted([(mp.re(vals[i]), mp.re(vecs[0, i]) ** 2) for i in range(len(b))], reverse=True)
    lam = [x[0] for x in pairs]
    rho = [x[1] for x in pairs]
    z = sum(rho)
    return lam, [x / z for x in rho]


def lax_rhs(a: list[mp.mpf], b: list[mp.mpf]) -> tuple[list[mp.mpf], list[mp.mpf]]:
    n = len(b)
    da = [a[j] * (b[j + 1] - b[j]) for j in range(n - 1)]
    db = []
    for j in range(n):
        left = a[j - 1] ** 2 if j > 0 else mp.mpf(0)
        right = a[j] ** 2 if j < n - 1 else mp.mpf(0)
        db.append(2 * (right - left))
    return da, db


def addv(x: list[mp.mpf], y: list[mp.mpf], scale: mp.mpf) -> list[mp.mpf]:
    return [x[i] + scale * y[i] for i in range(len(x))]


def rk4_step(a: list[mp.mpf], b: list[mp.mpf], h: mp.mpf) -> tuple[list[mp.mpf], list[mp.mpf]]:
    k1a, k1b = lax_rhs(a, b)
    k2a, k2b = lax_rhs(addv(a, k1a, h / 2), addv(b, k1b, h / 2))
    k3a, k3b = lax_rhs(addv(a, k2a, h / 2), addv(b, k2b, h / 2))
    k4a, k4b = lax_rhs(addv(a, k3a, h), addv(b, k3b, h))
    anew = [a[i] + h * (k1a[i] + 2 * k2a[i] + 2 * k3a[i] + k4a[i]) / 6 for i in range(len(a))]
    bnew = [b[i] + h * (k1b[i] + 2 * k2b[i] + 2 * k3b[i] + k4b[i]) / 6 for i in range(len(b))]
    return anew, bnew


def integrate(a0: list[F], b0: list[F], tq: F) -> tuple[list[mp.mpf], list[mp.mpf]]:
    a = [mpq(x) for x in a0]
    b = [mpq(x) for x in b0]
    if tq == 0:
        return a, b
    steps = RK_STEPS_PER_UNIT * abs(tq.numerator) // tq.denominator
    if steps * tq.denominator != RK_STEPS_PER_UNIT * abs(tq.numerator):
        raise ValueError("ledger times must align with the fixed step grid")
    h = mpq(tq) / steps
    for _ in range(steps):
        a, b = rk4_step(a, b, h)
    return a, b


def n2_exact(a0: F, b10: F, b20: F, tq: F) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    a = mpq(a0); b1 = mpq(b10); b2 = mpq(b20)
    dlt = b1 - b2
    gap = mp.sqrt(dlt * dlt + 4 * a * a)
    alpha = mp.atanh(dlt / gap)
    u = mp.tanh(gap * mpq(tq) + alpha)
    at = gap / (2 * mp.cosh(gap * mpq(tq) + alpha))
    return at, (b1 + b2 + gap * u) / 2, (b1 + b2 - gap * u) / 2


def initial_case(case: dict) -> tuple[list[F], list[F]]:
    return list(case["a"]), list(case["b"])


def build() -> dict:
    mp.mp.dps = WORKING_DIGITS
    parameter_rows = []
    lax_rows = []
    n2_rows = []
    scattering_rows = []
    action_rows = []
    for case in PARAMETERS:
        cid, n = case["case_id"], case["N"]
        aq, bq = initial_case(case)
        a0 = [mpq(x) for x in aq]; b0 = [mpq(x) for x in bq]
        lam0 = eigvals_desc(a0, b0)
        i0 = invariants(a0, b0)
        parameter_rows.append({
            "case_id": cid, "N": n, "a0": [str(x) for x in aq], "b0": [str(x) for x in bq],
            "q_gap_log_arguments": [fmt(2 * mpq(x)) for x in aq],
            "eigenvalues_desc": [fmt(x) for x in lam0],
            "trace_invariants_initial": [fmt(x) for x in i0],
            "hamiltonian_initial": fmt(4 * i0[1]),
        })
        for tq in LEDGER_TIMES:
            a, b = integrate(aq, bq, tq)
            iv = invariants(a, b)
            ev = eigvals_desc(a, b)
            lax_rows.append({
                "case_id": cid, "N": n, "time": str(tq), "a": [fmt(x) for x in a], "b": [fmt(x) for x in b],
                "a_min": fmt(min(a)), "trace_invariants": [fmt(x) for x in iv],
                "eigenvalues_desc": [fmt(x) for x in ev],
                "invariant_drift_max": fmt(max(abs(iv[k] - i0[k]) for k in range(n))),
                "spectrum_drift_max": fmt(max(abs(ev[k] - lam0[k]) for k in range(n))),
                "hamiltonian": fmt(4 * iv[1]),
            })
            if n == 2:
                ae, be1, be2 = n2_exact(aq[0], bq[0], bq[1], tq)
                n2_rows.append({
                    "case_id": cid, "time": str(tq), "a_exact": fmt(ae), "b_exact": [fmt(be1), fmt(be2)],
                    "a_numeric": lax_rows[-1]["a"], "b_numeric": lax_rows[-1]["b"],
                    "max_formula_error": fmt(max(abs(a[0] - ae), abs(b[0] - be1), abs(b[1] - be2))),
                })
        # Scattering diagnostic at +/- T.  The theorem supplies the limiting
        # sorting; finite endpoints are explicitly labelled a controlled check.
        am, bm = integrate(aq, bq, -SCATTER_T)
        ap, bp = integrate(aq, bq, SCATTER_T)
        bminus_target = list(reversed(lam0))
        bplus_target = lam0
        scattering_rows.append({
            "case_id": cid, "N": n, "endpoint_T": str(SCATTER_T),
            "b_minus": [fmt(x) for x in bm], "b_plus": [fmt(x) for x in bp],
            "target_b_minus_reversed": [fmt(x) for x in bminus_target],
            "target_b_plus_desc": [fmt(x) for x in bplus_target],
            "minus_sorting_error": fmt(max(abs(bm[j] - bminus_target[j]) for j in range(n))),
            "plus_sorting_error": fmt(max(abs(bp[j] - bplus_target[j]) for j in range(n))),
            "a_endpoint_max": fmt(max(max(abs(x) for x in am), max(abs(x) for x in ap))),
            "status": "finite_endpoint_diagnostic_not_exact_limit",
        })
        if n == 3:
            lam, rho0 = spectral_weights_desc(a0, b0)
            for tq in [F(-1), F(0), F(1)]:
                a, b = integrate(aq, bq, tq)
                _lam, rho_num = spectral_weights_desc(a, b)
                weights = [rho0[k] * mp.exp(2 * lam[k] * mpq(tq)) for k in range(n)]
                z = sum(weights); rho_pred = [x / z for x in weights]
                action_rows.append({
                    "case_id": cid, "time": str(tq), "eigenvalues_desc": [fmt(x) for x in lam],
                    "rho0": [fmt(x) for x in rho0], "rho_pred": [fmt(x) for x in rho_pred],
                    "rho_numeric": [fmt(x) for x in rho_num],
                    "max_norming_error": fmt(max(abs(rho_num[k] - rho_pred[k]) for k in range(n))),
                    "simple_spectrum": True,
                    "coordinate_note": "positive norming simplex; angle torus only after complex phase compactification",
                })

    boundaries = [
        {"boundary_id": "positive_jacobi", "condition": "a_j>0 for every edge", "statement": "Irreducible real symmetric Jacobi matrices have simple real spectrum; the Lax flow stays in this regular chamber."},
        {"boundary_id": "edge_decoupling", "condition": "a_j=0", "statement": "The matrix splits into blocks; the open-chain scattering theorem is applied only to positive edges and the zero-edge face is a lower-dimensional boundary."},
        {"boundary_id": "repeated_root", "condition": "N=3, a_1=a_2=0, b=(0,0,1)", "statement": "The characteristic polynomial is x^2(x-1); the repeated zero root is a singular block boundary, not a regular Jacobi point."},
        {"boundary_id": "center_of_mass", "condition": "q_j to q_j+c and p_j to p_j+u", "statement": "A common position shift leaves a and the relative dynamics unchanged; a common momentum translates all b/eigenvalues and separates the free center of mass."},
        {"boundary_id": "n2_sech_collision", "condition": "N=2, a_1>0", "statement": "a_1(t)=(d/2) sech(d t+atanh((b_1-b_2)/d)); it is positive for every finite t and tends to zero only at scattering ends."},
        {"boundary_id": "spectral_order", "condition": "lambda_1>...>lambda_N", "statement": "As t tends to +infinity b_j tends to lambda_j and as t tends to -infinity b_j tends to lambda_{N+1-j}; finite endpoint rows are diagnostics of this theorem."},
    ]
    data = {
        "schema": "hcs-c230-open-toda-v1", "candidate_id": "HCS-C230", "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "Finite open Toda flow closes a global Hamiltonian/Lax/scattering theorem with exact N=2 sech dynamics and simple-spectrum norming coordinates",
        "frozen_object": {
            "hamiltonian": "H(q,p)=1/2 sum_j p_j^2 + sum_{j=1}^{N-1} exp(q_j-q_{j+1}), N>=2",
            "equations": "qdot_j=p_j; pdot_1=-exp(q_1-q_2); pdot_j=exp(q_{j-1}-q_j)-exp(q_j-q_{j+1}); pdot_N=exp(q_{N-1}-q_N)",
            "flaschka": "a_j=1/2 exp((q_j-q_{j+1})/2)>0, b_j=-p_j/2",
            "lax_pair": "L=diag(b)+offdiag(a), B_{j,j+1}=a_j, B_{j+1,j}=-a_j, Ldot=[B,L]",
            "phase_space": "R^{2N} with finite q,p; positive Jacobi chamber a_j>0",
            "clock": "continuous Hamiltonian time t in R",
            "normalization": "real symmetric Jacobi L with positive off-diagonals; I_k=tr(L^k)/k and H=4 I_2",
            "determinant_convention": "finite characteristic polynomial det(lambda I-L); no orbit/Fredholm determinant",
            "arithmetic_origin": "none; all rates and initial rows are source-defined",
            "allowed_data": "Hamiltonian, Lax matrices, exact trace identities, Jacobi eigenvalues, norming weights and finite RK4 diagnostics",
            "forbidden_data": "target primes or zeros, local arithmetic, Euler factors, root numbers, automorphy and Route-B input",
        },
        "theorem": {
            "global_lax": "For every finite initial (q,p), the Hamiltonian flow is global; a_j(t)>0, Ldot=[B,L], and all I_k=tr(L^k)/k are conserved.",
            "simple_spectrum": "Positive irreducible Jacobi L has simple real eigenvalues lambda_1>...>lambda_N; the spectrum is fixed by the Lax flow.",
            "scattering": "With lambda_1>...>lambda_N, b_j(t)->lambda_j as t->+infinity and b_j(t)->lambda_{N+1-j} as t->-infinity; q_j(t)=(-2 lambda_j)t+c_j^+ +o(1) at +infinity and the reversed velocities at -infinity.",
            "norming_coordinates": "If rho_k=|v_1(lambda_k)|^2 and sum rho_k=1, then rho_k(t)=rho_k(0) exp(2 lambda_k t)/sum_l rho_l(0) exp(2 lambda_l t); the positive fixed-spectrum leaf is an open simplex.",
            "tau_inverse_scattering": "With r_k(t)=rho_k(0) exp(2 lambda_k t), tau_j=sum_{|S|=j}(prod_{k in S} r_k) Delta(lambda_S)^2, tau_0=1; a_j=sqrt(tau_{j-1} tau_{j+1})/tau_j and b_j=(1/2) d_t log(tau_j/tau_{j-1}); dominant subsets give the two sorting ends.",
            "action_angle": "On the simple-spectrum regular set, logarithmic norming variables provide local canonical action-angle coordinates after center-of-mass reduction; phases compactify to an (N-1)-torus only in the complex/compactified isospectral extension, while the physical positive chamber is noncompact scattering data.",
            "n2_closed_form": "For d=sqrt((b_1-b_2)^2+4a_1^2), a_1(t)=d sech(d t+atanh((b_1-b_2)/d))/2 and b_{1,2}(t)=(b_1+b_2 +/- d tanh(...))/2.",
            "hamiltonian_invariants": "H=4 I_2=2 sum_j b_j^2+4 sum_j a_j^2 and center momentum sum p_j=-2 tr L are conserved.",
            "degenerate_boundary": "If an edge a_j reaches zero only in a boundary compactification, L splits; repeated characteristic roots occur there and invalidate regular action-angle coordinates.",
            "flow_distinction": "This is a continuous Hamiltonian scattering flow, not a discrete primitive-orbit/zeta construction and not a periodic Toda torus claim.",
        },
        "regression": {
            "parameter_rows": parameter_rows, "ledger_times": [str(x) for x in LEDGER_TIMES], "scatter_T": str(SCATTER_T),
            "lax_rows": lax_rows, "n2_exact_rows": n2_rows, "scattering_rows": scattering_rows,
            "action_angle_rows": action_rows, "boundary_rows": boundaries,
        },
        "summary": {
            "parameter_count": len(PARAMETERS), "lax_row_count": len(lax_rows), "n2_exact_row_count": len(n2_rows),
            "scattering_row_count": len(scattering_rows), "action_angle_row_count": len(action_rows), "boundary_row_count": len(boundaries),
            "N2_case_count": sum(c["N"] == 2 for c in PARAMETERS), "N3_case_count": sum(c["N"] == 3 for c in PARAMETERS),
            "rk_steps_per_unit": RK_STEPS_PER_UNIT, "working_decimal_digits": WORKING_DIGITS, "serialized_significant_digits": SERIALIZED_DIGITS,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "An intrinsic Hamiltonian Lax pair, exact Jacobi spectrum, norming-coordinate linearization and scattering asymptotics are fully closed.",
            "strongest_failure": "The open chain has no arithmetic owner, primitive periodic repetition law, target determinant/divisor or natural Hilbert--Polya lift; the finite characteristic polynomial is source-local only.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "Flaschka1974", "claim": "Lax representation and integrals for the finite Toda lattice", "title": "The Toda lattice. II. Existence of integrals", "authors": "H. Flaschka", "venue": "Physical Review B 9 (1974), 1924--1925", "date": "1974", "url": "https://doi.org/10.1103/PhysRevB.9.1924", "persistent_url": "https://doi.org/10.1103/PhysRevB.9.1924"},
            {"key": "Moser1975", "claim": "inverse-scattering/norming-coordinate solution of finitely many exponential particles", "title": "Finitely many mass points on the line under the influence of an exponential potential--an integrable system", "authors": "J. Moser", "venue": "Dynamical Systems, Theory and Applications, Lecture Notes in Physics 38, Springer (1975), 467--497", "date": "1975", "url": "https://doi.org/10.1007/3-540-07171-7_12", "persistent_url": "https://doi.org/10.1007/3-540-07171-7_12"},
            {"key": "Tomei1984", "claim": "topology of compactified isospectral manifolds of Jacobi matrices", "title": "The topology of isospectral manifolds of tridiagonal matrices", "authors": "C. Tomei", "venue": "Duke Mathematical Journal 51 (1984), 981--996", "date": "1984", "url": "https://doi.org/10.1215/S0012-7094-84-05144-5", "persistent_url": "https://doi.org/10.1215/S0012-7094-84-05144-5"},
        ],
        "nonclaims": [
            "priority for the open Toda Lax/scattering theorem or norming-coordinate formulas",
            "a compact real Liouville torus for the uncompactified positive open chain; its physical isospectral leaf is a noncompact simplex/scattering chamber",
            "any Toda eigenvalue, characteristic root, trajectory or norming weight is a target zero, prime, Euler factor or arithmetic local datum",
            "an orbit zeta, Fredholm determinant, target divisor, functional equation, automorphy statement or zero correspondence",
            "a Hilbert--Polya operator, Route-B construction, global chaos claim or external peer review",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    path = parser.parse_args().output; path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    data = json.loads(path.read_text())
    print(json.dumps({"status": "C230_PRODUCER_PASS", "parameter_count": data["summary"]["parameter_count"], "lax_rows": data["summary"]["lax_row_count"], "n2_exact_rows": data["summary"]["n2_exact_row_count"], "action_angle_rows": data["summary"]["action_angle_row_count"], "payload_sha256": data["payload_sha256"], "output": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
