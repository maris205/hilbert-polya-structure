#!/usr/bin/env python3
"""Producer-independent checker for the C230 open-Toda receipt."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c230_open_toda_evidence.json"
SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
RK_STEPS_PER_UNIT = 256
TIMES = [F(-2), F(-1), F(0), F(1), F(2)]
SCATTER_T = F(8)
PARAMETERS = [
    ("N2_reference", 2, [F(1)], [F(1, 2), F(-1, 2)]),
    ("N2_asymmetric", 2, [F(3, 4)], [F(1, 3), F(-1, 6)]),
    ("N2_near_free", 2, [F(1, 10)], [F(1, 5), F(-1, 5)]),
    ("N3_symmetric", 3, [F(1), F(1)], [F(1), F(0), F(-1)]),
    ("N3_generic", 3, [F(1, 2), F(3, 2)], [F(1, 2), F(-1, 4), F(1, 3)]),
    ("N3_weak_links", 3, [F(1, 8), F(1, 6)], [F(2, 5), F(-1, 10), F(-3, 10)]),
]
TOL = mp.mpf("1e-60")
NUM_TOL = mp.mpf("2e-7")


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F | int) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator if isinstance(x, F) else mp.mpf(x)


def matrix(a: list[mp.mpf], b: list[mp.mpf]) -> mp.matrix:
    n = len(b); L = mp.matrix(n)
    for i in range(n):
        L[i, i] = b[i]
        if i + 1 < n: L[i, i + 1] = L[i + 1, i] = a[i]
    return L


def invs(a: list[mp.mpf], b: list[mp.mpf]) -> list[mp.mpf]:
    L = matrix(a, b); n = len(b); out = []
    for k in range(1, n + 1):
        P = L ** k; out.append(sum(P[i, i] for i in range(n)) / k)
    return out


def eigs(a: list[mp.mpf], b: list[mp.mpf]) -> list[mp.mpf]:
    vals, _ = mp.eigsy(matrix(a, b))
    return sorted([mp.re(vals[i]) for i in range(len(b))], reverse=True)


def weights(a: list[mp.mpf], b: list[mp.mpf]) -> tuple[list[mp.mpf], list[mp.mpf]]:
    vals, vecs = mp.eigsy(matrix(a, b))
    pairs = sorted([(mp.re(vals[i]), mp.re(vecs[0, i]) ** 2) for i in range(len(b))], reverse=True)
    z = sum(x[1] for x in pairs)
    return [x[0] for x in pairs], [x[1] / z for x in pairs]


def rhs(a: list[mp.mpf], b: list[mp.mpf]) -> tuple[list[mp.mpf], list[mp.mpf]]:
    n = len(b); da = [a[j] * (b[j + 1] - b[j]) for j in range(n - 1)]
    db = [2 * ((a[j] ** 2 if j < n - 1 else 0) - (a[j - 1] ** 2 if j > 0 else 0)) for j in range(n)]
    return da, db


def plus(x, y, c): return [x[i] + c * y[i] for i in range(len(x))]


def step(a, b, h):
    a1, b1 = rhs(a, b); a2, b2 = rhs(plus(a, a1, h / 2), plus(b, b1, h / 2))
    a3, b3 = rhs(plus(a, a2, h / 2), plus(b, b2, h / 2)); a4, b4 = rhs(plus(a, a3, h), plus(b, b3, h))
    return ([a[i] + h * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) / 6 for i in range(len(a))],
            [b[i] + h * (b1[i] + 2 * b2[i] + 2 * b3[i] + b4[i]) / 6 for i in range(len(b))])


def integrate(aq, bq, tq):
    a = [mpq(x) for x in aq]; b = [mpq(x) for x in bq]
    if tq == 0: return a, b
    steps = RK_STEPS_PER_UNIT * abs(tq.numerator) // tq.denominator
    h = mpq(tq) / steps
    for _ in range(steps): a, b = step(a, b, h)
    return a, b


def n2exact(aq, bq, tq):
    a = mpq(aq[0]); b1 = mpq(bq[0]); b2 = mpq(bq[1]); dif = b1 - b2
    d = mp.sqrt(dif * dif + 4 * a * a); alpha = mp.atanh(dif / d); u = mp.tanh(d * mpq(tq) + alpha)
    aa = d / (2 * mp.cosh(d * mpq(tq) + alpha))
    return aa, (b1 + b2 + d * u) / 2, (b1 + b2 - d * u) / 2


def _keys(obj, expected, where, check):
    check(isinstance(obj, dict), where + " mapping")
    check(set(obj) == set(expected), where + " exact keys")


def validate(data: dict) -> int:
    mp.mp.dps = 90; assertions = 0
    def check(ok, msg):
        nonlocal assertions
        assertions += 1
        if not ok: raise AssertionError(msg)
    top = ["schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","summary","route_a","scope_flags","citations","nonclaims","payload_sha256"]
    _keys(data, top, "top", check)
    _keys(data["evaluator"], ["path","version","sha256"], "evaluator", check)
    frozen_keys = ["hamiltonian","equations","flaschka","lax_pair","phase_space","clock","normalization","determinant_convention","arithmetic_origin","allowed_data","forbidden_data"]
    theorem_keys = ["global_lax","simple_spectrum","scattering","norming_coordinates","tau_inverse_scattering","action_angle","n2_closed_form","hamiltonian_invariants","degenerate_boundary","flow_distinction"]
    _keys(data["frozen_object"], frozen_keys, "frozen", check); _keys(data["theorem"], theorem_keys, "theorem", check)
    reg_keys = ["parameter_rows","ledger_times","scatter_T","lax_rows","n2_exact_rows","scattering_rows","action_angle_rows","boundary_rows"]
    _keys(data["regression"], reg_keys, "regression", check)
    sum_keys = ["parameter_count","lax_row_count","n2_exact_row_count","scattering_row_count","action_angle_row_count","boundary_row_count","N2_case_count","N3_case_count","rk_steps_per_unit","working_decimal_digits","serialized_significant_digits"]
    _keys(data["summary"], sum_keys, "summary", check)
    _keys(data["route_a"], ["tuple","overall","route_b_invocation_allowed","strongest_positive","strongest_failure"], "route", check)
    flags = ["uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"]
    _keys(data["scope_flags"], flags, "scope", check)
    check(data["schema"] == "hcs-c230-open-toda-v1" and data["candidate_id"] == "HCS-C230", "identity")
    check(data["evaluation_date"] == "2026-08-29" and data["source_commit"] == SOURCE_COMMIT and data["fixed_epoch"] == FIXED_EPOCH, "date/source")
    check(data["scope_literal"] == SCOPE and data["evaluator"] == EVALUATOR, "locks")
    check(data["headline"] == "Finite open Toda flow closes a global Hamiltonian/Lax/scattering theorem with exact N=2 sech dynamics and simple-spectrum norming coordinates", "headline")
    check(data["summary"]["parameter_count"] == 6 and data["summary"]["lax_row_count"] == len(data["regression"]["lax_rows"]) and data["summary"]["n2_exact_row_count"] == len(data["regression"]["n2_exact_rows"]) and data["summary"]["scattering_row_count"] == len(data["regression"]["scattering_rows"]) and data["summary"]["action_angle_row_count"] == len(data["regression"]["action_angle_rows"]) and data["summary"]["boundary_row_count"] == len(data["regression"]["boundary_rows"]), "summary counts")
    check(data["frozen_object"] == {
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
    }, "frozen semantics")
    expected_theorem = {
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
    }
    check(data["theorem"] == expected_theorem, "theorem semantics")
    check(data["route_a"]["tuple"] == ["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"] and data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route")
    check(all(v is False for v in data["scope_flags"].values()), "scope flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    # Citation and nonclaim shape is closed, while exact strings are checked in the manifest.
    for i, c in enumerate(data["citations"]): _keys(c, ["key","claim","title","authors","venue","date","url","persistent_url"], f"citation[{i}]", check)
    expected_urls = ["https://doi.org/10.1103/PhysRevB.9.1924", "https://doi.org/10.1007/3-540-07171-7_12", "https://doi.org/10.1215/S0012-7094-84-05144-5"]
    expected_nonclaims = [
        "priority for the open Toda Lax/scattering theorem or norming-coordinate formulas",
        "a compact real Liouville torus for the uncompactified positive open chain; its physical isospectral leaf is a noncompact simplex/scattering chamber",
        "any Toda eigenvalue, characteristic root, trajectory or norming weight is a target zero, prime, Euler factor or arithmetic local datum",
        "an orbit zeta, Fredholm determinant, target divisor, functional equation, automorphy statement or zero correspondence",
        "a Hilbert--Polya operator, Route-B construction, global chaos claim or external peer review",
    ]
    check(len(data["citations"]) == 3 and [c["persistent_url"] for c in data["citations"]] == expected_urls and [c["url"] for c in data["citations"]] == expected_urls and data["nonclaims"] == expected_nonclaims, "citation/nonclaim counts")

    lookup = {cid: (n, a, b) for cid, n, a, b in PARAMETERS}
    expected_params = [{"case_id": cid, "N": n, "a0": [str(x) for x in a], "b0": [str(x) for x in b],
                        "q_gap_log_arguments": [mp.nstr(2 * mpq(x), 72, strip_zeros=False) for x in a],
                        "eigenvalues_desc": [mp.nstr(x, 72, strip_zeros=False) for x in eigs([mpq(x) for x in a], [mpq(x) for x in b])],
                        "trace_invariants_initial": [mp.nstr(x, 72, strip_zeros=False) for x in invs([mpq(x) for x in a], [mpq(x) for x in b])],
                        "hamiltonian_initial": mp.nstr(4 * invs([mpq(x) for x in a], [mpq(x) for x in b])[1], 72, strip_zeros=False)} for cid, n, a, b in PARAMETERS]
    # String exactness is intentionally relaxed for transcendental fields, but rational identity fields are exact.
    check(len(data["regression"]["parameter_rows"]) == len(PARAMETERS), "parameter closure")
    for i, row in enumerate(data["regression"]["parameter_rows"]):
        _keys(row, ["case_id","N","a0","b0","q_gap_log_arguments","eigenvalues_desc","trace_invariants_initial","hamiltonian_initial"], f"parameter[{i}]", check)
        cid = row["case_id"]; check(cid in lookup and row["N"] == lookup[cid][0], f"parameter[{i}] domain")
        check(row["a0"] == [str(x) for x in lookup[cid][1]] and row["b0"] == [str(x) for x in lookup[cid][2]], f"parameter[{i}] rational data")
        check(row == expected_params[i], f"parameter[{i}] derived fields")

    lax_keys = ["case_id","N","time","a","b","a_min","trace_invariants","eigenvalues_desc","invariant_drift_max","spectrum_drift_max","hamiltonian"]
    seen = set(); check(len(data["regression"]["lax_rows"]) == 30, "lax count")
    for i, row in enumerate(data["regression"]["lax_rows"]):
        _keys(row, lax_keys, f"lax[{i}]", check); cid = row["case_id"]; tq = F(row["time"])
        check(cid in lookup and tq in TIMES, f"lax[{i}] domain"); ident = (cid, tq); check(ident not in seen, f"lax[{i}] duplicate"); seen.add(ident)
        n, aq, bq = lookup[cid]; a, b = integrate(aq, bq, tq); iv = invs(a, b); ev = eigs(a, b); i0 = invs([mpq(x) for x in aq], [mpq(x) for x in bq]); ev0 = eigs([mpq(x) for x in aq], [mpq(x) for x in bq])
        got_a = [mp.mpf(x) for x in row["a"]]; got_b = [mp.mpf(x) for x in row["b"]]
        check(len(got_a) == n - 1 and len(got_b) == n and max(abs(got_a[j] - a[j]) for j in range(n - 1)) < TOL and max(abs(got_b[j] - b[j]) for j in range(n)) < TOL, f"lax[{i}] integration")
        check(mp.mpf(row["a_min"]) == min(got_a) and min(got_a) > 0, f"lax[{i}] positivity")
        check(max(abs(mp.mpf(row["trace_invariants"][k]) - iv[k]) for k in range(n)) < TOL and max(abs(mp.mpf(row["eigenvalues_desc"][k]) - ev[k]) for k in range(n)) < TOL, f"lax[{i}] spectral reconstruction")
        check(max(abs(iv[k] - i0[k]) for k in range(n)) < NUM_TOL and max(abs(ev[k] - ev0[k]) for k in range(n)) < NUM_TOL, f"lax[{i}] drift bound")
        check(abs(mp.mpf(row["invariant_drift_max"]) - max(abs(iv[k] - i0[k]) for k in range(n))) < TOL and abs(mp.mpf(row["spectrum_drift_max"]) - max(abs(ev[k] - ev0[k]) for k in range(n))) < TOL, f"lax[{i}] drift ledger")
        check(abs(mp.mpf(row["hamiltonian"]) - 4 * iv[1]) < TOL, f"lax[{i}] Hamiltonian")
    check(len(seen) == 30, "lax closure")

    n2_keys = ["case_id","time","a_exact","b_exact","a_numeric","b_numeric","max_formula_error"]
    seen = set(); check(len(data["regression"]["n2_exact_rows"]) == 15, "N2 closure count")
    for i, row in enumerate(data["regression"]["n2_exact_rows"]):
        _keys(row, n2_keys, f"n2[{i}]", check); cid = row["case_id"]; tq = F(row["time"]); check(cid in lookup and lookup[cid][0] == 2 and tq in TIMES, f"n2[{i}] domain"); ident = (cid, tq); check(ident not in seen, f"n2[{i}] duplicate"); seen.add(ident)
        aq, bq = lookup[cid][1:]; ae, be1, be2 = n2exact(aq, bq, tq); got = [mp.mpf(row["a_exact"]), *[mp.mpf(x) for x in row["b_exact"]]]
        check(max(abs(got[0] - ae), abs(got[1] - be1), abs(got[2] - be2)) < TOL, f"n2[{i}] closed form")
        check(row["a_numeric"] == next(r["a"] for r in data["regression"]["lax_rows"] if r["case_id"] == cid and r["time"] == str(tq)) and row["b_numeric"] == next(r["b"] for r in data["regression"]["lax_rows"] if r["case_id"] == cid and r["time"] == str(tq)), f"n2[{i}] link")
        an, bn = integrate(aq, bq, tq); err = max(abs(an[0] - ae), abs(bn[0] - be1), abs(bn[1] - be2)); check(abs(mp.mpf(row["max_formula_error"]) - err) < TOL and err < NUM_TOL, f"n2[{i}] error")
    check(len(seen) == 15, "n2 closure")

    sc_keys = ["case_id","N","endpoint_T","b_minus","b_plus","target_b_minus_reversed","target_b_plus_desc","minus_sorting_error","plus_sorting_error","a_endpoint_max","status"]
    check(len(data["regression"]["scattering_rows"]) == len(PARAMETERS), "scattering count")
    for i, row in enumerate(data["regression"]["scattering_rows"]):
        _keys(row, sc_keys, f"scatter[{i}]", check); cid = row["case_id"]; n, aq, bq = lookup[cid]; check(row["N"] == n and row["endpoint_T"] == str(SCATTER_T), f"scatter[{i}] identity")
        am, bm = integrate(aq, bq, -SCATTER_T); ap, bp = integrate(aq, bq, SCATTER_T); ev = eigs([mpq(x) for x in aq], [mpq(x) for x in bq]); gm = [mp.mpf(x) for x in row["b_minus"]]; gp = [mp.mpf(x) for x in row["b_plus"]]
        check(max(abs(gm[j] - bm[j]) for j in range(n)) < TOL and max(abs(gp[j] - bp[j]) for j in range(n)) < TOL, f"scatter[{i}] endpoints")
        check(row["target_b_minus_reversed"] == [mp.nstr(x, 72, strip_zeros=False) for x in reversed(ev)] and row["target_b_plus_desc"] == [mp.nstr(x, 72, strip_zeros=False) for x in ev], f"scatter[{i}] targets")
        me = max(abs(bm[j] - list(reversed(ev))[j]) for j in range(n)); pe = max(abs(bp[j] - ev[j]) for j in range(n)); ae = max(max(abs(x) for x in am), max(abs(x) for x in ap))
        check(abs(mp.mpf(row["minus_sorting_error"]) - me) < TOL and abs(mp.mpf(row["plus_sorting_error"]) - pe) < TOL and abs(mp.mpf(row["a_endpoint_max"]) - ae) < TOL, f"scatter[{i}] diagnostics")
        check(row["status"] == "finite_endpoint_diagnostic_not_exact_limit", f"scatter[{i}] scope")

    aa_keys = ["case_id","time","eigenvalues_desc","rho0","rho_pred","rho_numeric","max_norming_error","simple_spectrum","coordinate_note"]
    check(len(data["regression"]["action_angle_rows"]) == 9, "action count")
    for i, row in enumerate(data["regression"]["action_angle_rows"]):
        _keys(row, aa_keys, f"action[{i}]", check); cid = row["case_id"]; tq = F(row["time"]); check(cid.startswith("N3_") and tq in [F(-1),F(0),F(1)], f"action[{i}] domain")
        aq, bq = lookup[cid][1:]; a0 = [mpq(x) for x in aq]; b0 = [mpq(x) for x in bq]; lam, rho0 = weights(a0, b0); a, b = integrate(aq, bq, tq); _lam, rhon = weights(a, b); ww = [rho0[k] * mp.exp(2 * lam[k] * mpq(tq)) for k in range(3)]; z = sum(ww); rhop = [x/z for x in ww]
        check(max(abs(mp.mpf(row["eigenvalues_desc"][k]) - lam[k]) for k in range(3)) < TOL and max(abs(mp.mpf(row["rho0"][k]) - rho0[k]) for k in range(3)) < TOL and max(abs(mp.mpf(row["rho_pred"][k]) - rhop[k]) for k in range(3)) < TOL and max(abs(mp.mpf(row["rho_numeric"][k]) - rhon[k]) for k in range(3)) < TOL, f"action[{i}] coordinates")
        err = max(abs(rhon[k] - rhop[k]) for k in range(3)); check(abs(mp.mpf(row["max_norming_error"]) - err) < TOL and err < NUM_TOL and row["simple_spectrum"] is True, f"action[{i}] flow")

    bkeys = ["boundary_id","condition","statement"]; expected_bids = ["positive_jacobi","edge_decoupling","repeated_root","center_of_mass","n2_sech_collision","spectral_order"]
    expected_boundary_rows = [
        {"boundary_id": "positive_jacobi", "condition": "a_j>0 for every edge", "statement": "Irreducible real symmetric Jacobi matrices have simple real spectrum; the Lax flow stays in this regular chamber."},
        {"boundary_id": "edge_decoupling", "condition": "a_j=0", "statement": "The matrix splits into blocks; the open-chain scattering theorem is applied only to positive edges and the zero-edge face is a lower-dimensional boundary."},
        {"boundary_id": "repeated_root", "condition": "N=3, a_1=a_2=0, b=(0,0,1)", "statement": "The characteristic polynomial is x^2(x-1); the repeated zero root is a singular block boundary, not a regular Jacobi point."},
        {"boundary_id": "center_of_mass", "condition": "q_j to q_j+c and p_j to p_j+u", "statement": "A common position shift leaves a and the relative dynamics unchanged; a common momentum translates all b/eigenvalues and separates the free center of mass."},
        {"boundary_id": "n2_sech_collision", "condition": "N=2, a_1>0", "statement": "a_1(t)=(d/2) sech(d t+atanh((b_1-b_2)/d)); it is positive for every finite t and tends to zero only at scattering ends."},
        {"boundary_id": "spectral_order", "condition": "lambda_1>...>lambda_N", "statement": "As t tends to +infinity b_j tends to lambda_j and as t tends to -infinity b_j tends to lambda_{N+1-j}; finite endpoint rows are diagnostics of this theorem."},
    ]
    check(len(data["regression"]["boundary_rows"]) == 6, "boundary count")
    for i, row in enumerate(data["regression"]["boundary_rows"]): _keys(row, bkeys, f"boundary[{i}]", check); check(row == expected_boundary_rows[i] and row["boundary_id"] == expected_bids[i], f"boundary[{i}] identity")

    # Independent exact matrix checks, including characteristic repeated-root boundary.
    import sympy as sp
    x = sp.symbols("x")
    for cid, n, aq, bq in PARAMETERS:
        L = sp.zeros(n)
        for j in range(n):
            L[j,j] = sp.Rational(bq[j].numerator, bq[j].denominator)
            if j + 1 < n: L[j,j+1] = L[j+1,j] = sp.Rational(aq[j].numerator, aq[j].denominator)
        check(sp.simplify(L - L.T) == sp.zeros(n), "Jacobi symmetry")
        check(sp.Poly(L.charpoly(x).as_expr(), x).degree() == n, "characteristic degree")
    boundary = sp.diag(0,0,1); check(sp.factor(boundary.charpoly(x).as_expr()) == x**2 * (x-1), "repeated root boundary")
    # Lax commutator has zero trace for powers in a generic symbolic 3x3 case.
    aa1, aa2, bb1, bb2, bb3 = sp.symbols("a1 a2 b1 b2 b3")
    Ls = sp.Matrix([[bb1,aa1,0],[aa1,bb2,aa2],[0,aa2,bb3]])
    Bs = sp.Matrix([[0,aa1,0],[-aa1,0,aa2],[0,-aa2,0]])
    C = Bs*Ls-Ls*Bs
    check(sp.simplify(sp.trace(C)) == 0 and sp.simplify(sp.trace(C*Ls + Ls*C)) == 0, "Lax trace identities")
    check(sp.simplify(sp.det(Ls - x*sp.eye(3)) + sp.det(x*sp.eye(3)-Ls)) == 0, "determinant sign")
    return assertions


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text()); n = validate(data)
    print(json.dumps({"status": "C230_CHECKER_PASS", "assertions": n, "lax_rows": len(data["regression"]["lax_rows"]), "n2_exact_rows": len(data["regression"]["n2_exact_rows"]), "producer_imported": False}, sort_keys=True))


if __name__ == "__main__": main()
