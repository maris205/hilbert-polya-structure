#!/usr/bin/env python3
"""Producer-independent exact and high-precision audit for HCS-C225."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c225_mm1k_evidence.json"
SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
HEADLINE = "Finite-capacity M/M/1/K birth--death queues admit an exact reversible kernel, full spectral gap atlas, and controlled infinite-capacity boundaries"
PARAMETERS = [("subcritical", F(1), F(2)), ("critical", F(1), F(1)), ("supercritical", F(2), F(1)), ("asymmetric", F(3, 2), F(1))]
K_VALUES = [0, 1, 2, 4, 8]
TIME_VALUES = [F(1, 5), F(1, 2), F(1)]
LIMIT_K_VALUES = [4, 8, 16, 32]
TOL = mp.mpf("1e-70")


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def stationary(lam: F, mu: F, K: int) -> list[F]:
    if K == 0: return [F(1)]
    rho = lam / mu; w = [rho**n for n in range(K + 1)]; z = sum(w, F(0))
    return [x / z for x in w]


def gap(lam: F, mu: F, K: int) -> mp.mpf | None:
    if K == 0: return None
    return mpq(lam + mu) - 2 * mp.sqrt(mpq(lam * mu)) * mp.cos(mp.pi / (K + 1))


def expected_spectral(lam: F, mu: F, K: int, j: int):
    theta = mp.pi * j / (K + 1); alpha = mp.sqrt(mpq(mu / lam))
    raw = [mp.sin((n + 1) * theta) - alpha * mp.sin(n * theta) for n in range(K + 1)]
    norm = mp.sqrt(sum(x*x for x in raw))
    vec = [x / norm for x in raw]
    eig = -mpq(lam + mu) + 2 * mp.sqrt(mpq(lam * mu)) * mp.cos(theta)
    return theta, eig, vec


def expected_kernel(lam: F, mu: F, K: int, t: F) -> list[list[mp.mpf]]:
    if K == 0: return [[mp.mpf(1)]]
    pi = [mpq(x) for x in stationary(lam, mu, K)]
    vecs = [[mp.sqrt(x) for x in pi]]; eigs = [mp.mpf(0)]
    for j in range(1, K + 1):
        _theta, eig, vec = expected_spectral(lam, mu, K, j); vecs.append(vec); eigs.append(eig)
    tt = mpq(t)
    return [[sum(vecs[m][i]*vecs[m][j]*mp.exp(eigs[m]*tt) for m in range(K+1))*mp.sqrt(pi[j]/pi[i]) for j in range(K+1)] for i in range(K+1)]


def generator(lam: F, mu: F, K: int) -> sp.Matrix:
    n = K + 1; Q = sp.zeros(n)
    if K == 0: return Q
    la, mm = sp.Rational(lam.numerator, lam.denominator), sp.Rational(mu.numerator, mu.denominator)
    Q[0, 0], Q[0, 1] = -la, la
    for i in range(1, K): Q[i, i-1], Q[i, i], Q[i, i+1] = mm, -(la+mm), la
    Q[K, K-1], Q[K, K] = mm, -mm
    return Q


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text()); mp.mp.dps = 100; assertions = 0

    def check(ok: bool, msg: str):
        nonlocal assertions
        assertions += 1
        if not ok: raise AssertionError(msg)

    def keys(obj, expected, where):
        check(isinstance(obj, dict), where + " mapping"); check(set(obj) == set(expected), where + " keys")

    top = ["schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","summary","route_a","scope_flags","citations","nonclaims","payload_sha256"]
    keys(data, top, "top"); keys(data["evaluator"], ["path","version","sha256"], "evaluator")
    frozen = ["state_space","generator","parameters","clock","normalization","symmetrization","determinant_convention","arithmetic_origin","allowed_data","forbidden_data"]
    theorem = ["stationary","jacobi","spectrum","eigenbasis","kernel","mixing","boundaries","infinite_capacity","infinite_scope","distinction"]
    keys(data["frozen_object"], frozen, "frozen"); keys(data["theorem"], theorem, "theorem")
    regkeys = ["parameter_rows","K_values","time_values","limit_K_values","stationary_rows","spectral_rows","kernel_rows","mixing_rows","limit_rows","boundary_rows"]
    keys(data["regression"], regkeys, "regression")
    sumkeys = ["parameter_count","stationary_row_count","spectral_row_count","kernel_row_count","mixing_row_count","limit_row_count","boundary_row_count","max_K","serialized_decimal_digits"]
    keys(data["summary"], sumkeys, "summary")
    keys(data["route_a"], ["tuple","overall","route_b_invocation_allowed","strongest_positive","strongest_failure"], "route")
    flags = ["uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"]
    keys(data["scope_flags"], flags, "scope_flags")
    check(data["schema"] == "hcs-c225-mm1k-queue-v1" and data["candidate_id"] == "HCS-C225", "identity")
    check(data["evaluation_date"] == "2026-08-29" and data["source_commit"] == SOURCE_COMMIT and data["fixed_epoch"] == FIXED_EPOCH, "date/source/epoch")
    check(data["scope_literal"] == SCOPE and data["evaluator"] == EVALUATOR and data["headline"] == HEADLINE, "locks")
    expected_frozen = {
        "state_space": "{0,1,...,K}, where K includes the customer in service",
        "generator": "Q_{0,0}=-lambda,Q_{0,1}=lambda; Q_{n,n-1}=mu,Q_{n,n}=-(lambda+mu),Q_{n,n+1}=lambda (0<n<K); Q_{K,K-1}=mu,Q_{K,K}=-mu",
        "parameters": "lambda,mu>=0 rates, integer capacity K>=0, physical time t>=0",
        "clock": "continuous-time Markov semigroup exp(tQ)",
        "normalization": "row-stochastic transition kernel and probability stationary vector",
        "symmetrization": "S=D_pi^(1/2) Q D_pi^(-1/2), with off-diagonal sqrt(lambda*mu)",
        "determinant_convention": "finite characteristic polynomial only; no infinite Fredholm determinant",
        "arithmetic_origin": "none; queue states and rates are source-defined",
        "allowed_data": "exact rates, finite generators, stationary probabilities, eigenmodes, kernels and mixing bounds",
        "forbidden_data": "prime or zero tables, target labels, Euler factors, root numbers, automorphy and Route-B input",
    }
    check(data["frozen_object"] == expected_frozen, "frozen semantics")
    expected_theorem = {
        "stationary": "For lambda,mu>0 and K>=1, pi_n=(lambda/mu)^n / sum_{r=0}^K(lambda/mu)^r; at equal rates pi is uniform; K=0 is singleton.",
        "jacobi": "D_pi^(1/2) Q D_pi^(-1/2) is a symmetric tridiagonal Jacobi matrix with off-diagonal sqrt(lambda*mu).",
        "spectrum": "For K>=1 the eigenvalues are 0 and nu_j=-(lambda+mu)+2sqrt(lambda*mu)cos(j*pi/(K+1)), j=1,...,K.",
        "eigenbasis": "A normalized eigenvector for nu_j has components proportional to sin((n+1)theta_j)-sqrt(mu/lambda)sin(n theta_j), theta_j=j*pi/(K+1).",
        "kernel": "P_t(i,j)=sqrt(pi_j/pi_i) sum_{m=0}^K v_m(i)v_m(j)exp(nu_m t), with v_0=sqrt(pi) and nu_0=0.",
        "mixing": "The spectral gap is gamma_K=lambda+mu-2sqrt(lambda*mu)cos(pi/(K+1)); TV distance from i is at most 1/2 sqrt(pi_i^{-1}-1) exp(-gamma_K t).",
        "boundaries": "K=0, lambda=0, mu=0 and both-zero faces are absorbing degeneracies; equal rates are finite uniform but infinite null recurrent.",
        "infinite_capacity": "As K->infinity, rho<1 has geometric stationary convergence and gap limit (sqrt(mu)-sqrt(lambda))^2; rho=1 has gamma_K~lambda*pi^2/(K+1)^2 and no stationary probability; rho>1 finite stationary mass escapes and no stationary probability exists.",
        "infinite_scope": "No assertion is made here about a continuous-spectrum decomposition of the infinite generator; only the stated stationary and gap/boundary limits are claimed.",
        "distinction": "This is a reversible birth--death semigroup with capacity reflection, not the branching PGF of C208 and not the interacting-particle matrix-ansatz phase atlas of C220.",
    }
    check(data["theorem"] == expected_theorem, "theorem semantics")
    check(data["route_a"]["tuple"] == ["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"] and data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route")
    check(all(v is False for v in data["scope_flags"].values()), "scope flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    expected_citations = [
        {"key": "KarlinMcGregor1957", "claim": "spectral representation and Stieltjes moment framework for birth--death processes", "title": "The differential equations of birth-and-death processes, and the Stieltjes moment problem", "authors": "Samuel Karlin and James McGregor", "venue": "Transactions of the American Mathematical Society 85 (1957), 489--546", "date": "1957", "url": "https://doi.org/10.1090/S0002-9947-1957-0091566-1", "persistent_url": "https://doi.org/10.1090/S0002-9947-1957-0091566-1"},
        {"key": "EkstromGaroniJozefiakPerla2021", "claim": "tau-matrix spectral calculations with applications to Markov processes", "title": "Eigenvalues and eigenvectors of tau matrices with applications to Markov processes and economics", "authors": "Sven-Erik Ekström, Carlo Garoni, Adam Jozefiak and Jesse Perla", "venue": "Linear Algebra and its Applications 627 (2021), 41--71", "date": "2021", "url": "https://doi.org/10.1016/j.laa.2021.06.005", "persistent_url": "https://doi.org/10.1016/j.laa.2021.06.005"},
        {"key": "CallaertKeilson1973", "claim": "exponential ergodicity and spectral-structure boundary context for birth--death processes", "title": "On exponential ergodicity and spectral structure for birth-death processes, II", "authors": "Herman Callaert and Julian Keilson", "venue": "Stochastic Processes and their Applications 1(3) (1973), 217--235", "date": "1973", "url": "https://doi.org/10.1016/0304-4149(73)90001-X", "persistent_url": "https://doi.org/10.1016/0304-4149(73)90001-X"},
    ]
    for i,cit in enumerate(data["citations"]): keys(cit,["key","claim","title","authors","venue","date","url","persistent_url"],f"citation[{i}]")
    check(data["citations"] == expected_citations, "citation semantics")
    expected_nonclaims = [
        "priority for the finite M/M/1/K spectrum or queueing boundary classification",
        "the finite ledger is a proof of an unqualified infinite-dimensional spectral theorem",
        "any queue eigenvalue or state label is a target zero, prime, Euler factor or arithmetic local datum",
        "an infinite Fredholm determinant, target divisor, functional equation or automorphy statement",
        "a Hilbert--Polya operator, Route-B construction or external peer review",
    ]
    check(data["nonclaims"] == expected_nonclaims, "nonclaims")
    lookup = {x[0]: x[1:] for x in PARAMETERS}
    expected_params = [{"parameter_label": l, "lambda": str(la), "mu": str(mu)} for l, la, mu in PARAMETERS]
    check(data["regression"]["parameter_rows"] == expected_params, "parameter rows")
    check(data["regression"]["K_values"] == K_VALUES and data["regression"]["time_values"] == [str(t) for t in TIME_VALUES] and data["regression"]["limit_K_values"] == LIMIT_K_VALUES, "grids")

    # Exact stationary ledger.
    skeys = ["parameter_label","lambda","mu","K","rho","weights","stationary","normalization","pi0","piK"]
    seen = set()
    for i, row in enumerate(data["regression"]["stationary_rows"]):
        keys(row, skeys, f"stationary[{i}]"); label, K = row["parameter_label"], row["K"]; check(label in lookup and K in K_VALUES, f"stationary[{i}] domain")
        check((label,K) not in seen, f"stationary[{i}] duplicate"); seen.add((label,K)); lam, mu = lookup[label]; pi = stationary(lam,mu,K); rho = lam/mu
        check(row["rho"] == str(rho) and row["weights"] == [str(rho**n) for n in range(K+1)] and row["stationary"] == [str(x) for x in pi], f"stationary[{i}] exact")
        check(row["normalization"] == "1" and row["pi0"] == str(pi[0]) and row["piK"] == str(pi[-1]), f"stationary[{i}] normalization")
    check(len(seen) == len(PARAMETERS)*len(K_VALUES), "stationary closure")

    # Full finite Jacobi spectrum and eigenvector recurrence.
    eks = ["parameter_label","lambda","mu","K","mode","theta","eigenvalue","eigenvector","norm_squared"]
    seen = set()
    for i, row in enumerate(data["regression"]["spectral_rows"]):
        keys(row, eks, f"spectrum[{i}]"); label,K,j = row["parameter_label"],row["K"],row["mode"]; check(label in lookup and K in K_VALUES and K>=1 and 1<=j<=K, f"spectrum[{i}] domain")
        check((label,K,j) not in seen, f"spectrum[{i}] duplicate"); seen.add((label,K,j)); lam,mu=lookup[label]; theta,eig,vec=expected_spectral(lam,mu,K,j)
        check(abs(mp.mpf(row["theta"])-theta)<TOL and abs(mp.mpf(row["eigenvalue"])-eig)<TOL, f"spectrum[{i}] scalar")
        got=[mp.mpf(x) for x in row["eigenvector"]]; check(len(got)==K+1 and max(abs(got[n]-vec[n]) for n in range(K+1))<TOL, f"spectrum[{i}] vector")
        check(abs(mp.mpf(row["norm_squared"])-1)<TOL and abs(sum(x*x for x in got)-1)<TOL, f"spectrum[{i}] norm")
        # independent tridiagonal eigen-equation, including both reflecting faces
        r=mp.sqrt(mpq(lam*mu)); d=[-mpq(lam)]+[-mpq(lam+mu)]*(K-1)+[-mpq(mu)]
        res=[]
        for n in range(K+1):
            lhs=d[n]*got[n] + (r*got[n-1] if n>0 else 0) + (r*got[n+1] if n<K else 0)
            res.append(abs(lhs-eig*got[n]))
        check(max(res)<TOL, f"spectrum[{i}] recurrence")
    check(len(seen)==sum(K_VALUES)*len(PARAMETERS), "spectrum closure")

    # Exact transient kernel and mixing inequality.
    kkeys=["parameter_label","lambda","mu","K","time","initial_state","probabilities","row_sum","min_probability","tv_distance","tv_bound","bound_slack"]
    mkeys=["parameter_label","K","time","initial_state","tv_distance","tv_bound","gap"]
    kseen=set(); mseen=set(); kmap={}
    for i,row in enumerate(data["regression"]["kernel_rows"]):
        keys(row,kkeys,f"kernel[{i}]"); label,K,t,initial=row["parameter_label"],row["K"],F(row["time"]),row["initial_state"]; check(label in lookup and K in K_VALUES and t in TIME_VALUES and 0<=initial<=K,f"kernel[{i}] domain")
        ident=(label,K,t,initial); check(ident not in kseen,f"kernel[{i}] duplicate"); kseen.add(ident); lam,mu=lookup[label]; P=expected_kernel(lam,mu,K,t)[initial]; got=[mp.mpf(x) for x in row["probabilities"]]
        check(len(got)==K+1 and max(abs(got[j]-P[j]) for j in range(K+1))<TOL,f"kernel[{i}] spectral reconstruction")
        pi=[mpq(x) for x in stationary(lam,mu,K)]; tv=mp.mpf("0.5")*sum(abs(P[j]-pi[j]) for j in range(K+1)); b=mp.mpf(0) if K==0 else mp.mpf("0.5")*mp.sqrt(1/pi[initial]-1)*mp.exp(-gap(lam,mu,K)*mpq(t))
        check(abs(mp.mpf(row["row_sum"])-sum(P))<TOL and abs(mp.mpf(row["min_probability"])-min(P))<TOL and min(got)>-TOL,f"kernel[{i}] probability")
        check(abs(mp.mpf(row["tv_distance"])-tv)<TOL and abs(mp.mpf(row["tv_bound"])-b)<TOL and abs(mp.mpf(row["bound_slack"])-(mp.mpf(row["tv_bound"])-mp.mpf(row["tv_distance"])))<TOL,f"kernel[{i}] mixing")
        kmap[ident]=row
    check(len(kseen)==len(PARAMETERS)*sum(K+1 for K in K_VALUES)*len(TIME_VALUES),"kernel closure")
    for i,row in enumerate(data["regression"]["mixing_rows"]):
        keys(row,mkeys,f"mixing[{i}]"); ident=(row["parameter_label"],row["K"],F(row["time"]),row["initial_state"]); check(ident in kmap,f"mixing[{i}] link"); src=kmap[ident]; check(row["tv_distance"]==src["tv_distance"] and row["tv_bound"]==src["tv_bound"],f"mixing[{i}] values"); K=row["K"]; check((K==0 and row["gap"] is None) or (K>0 and abs(mp.mpf(row["gap"])-gap(*lookup[row["parameter_label"]],K))<TOL),f"mixing[{i}] gap"); mseen.add(ident)
    check(len(mseen)==len(kseen),"mixing closure")

    # Capacity limits and all absorbing/equal-rate faces.
    lkeys=["parameter_label","lambda","mu","rho","K","pi_state0","pi_stateK","finite_gap","infinite_gap_reference","gap_ratio_to_reference","critical_scaled_gap"]
    lseen=set()
    for i,row in enumerate(data["regression"]["limit_rows"]):
        keys(row,lkeys,f"limit[{i}]"); label,K=row["parameter_label"],row["K"]; check(label in lookup and K in LIMIT_K_VALUES,f"limit[{i}] domain"); check((label,K) not in lseen,f"limit[{i}] duplicate"); lseen.add((label,K)); lam,mu=lookup[label]; rho=lam/mu; pi=stationary(lam,mu,K); g=gap(lam,mu,K); ig=(mp.sqrt(mpq(mu))-mp.sqrt(mpq(lam)))**2
        check(row["rho"]==str(rho) and abs(mp.mpf(row["pi_state0"])-mpq(pi[0]))<TOL and abs(mp.mpf(row["pi_stateK"])-mpq(pi[-1]))<TOL and abs(mp.mpf(row["finite_gap"])-g)<TOL and abs(mp.mpf(row["infinite_gap_reference"])-ig)<TOL,f"limit[{i}] values")
        if rho==1: check(row["gap_ratio_to_reference"] is None and abs(mp.mpf(row["critical_scaled_gap"])-g*(K+1)**2)<TOL,f"limit[{i}] critical")
        else: check(row["critical_scaled_gap"] is None and abs(mp.mpf(row["gap_ratio_to_reference"])-g/ig)<TOL,f"limit[{i}] ratio")
    check(len(lseen)==len(PARAMETERS)*len(LIMIT_K_VALUES),"limit closure")
    b_expected=[("K_zero","K=0"),("lambda_zero","lambda=0, mu>0"),("mu_zero","mu=0, lambda>0"),("both_zero","lambda=mu=0"),("equal_rates","lambda=mu>0"),("infinite_subcritical","K to infinity with rho=lambda/mu<1"),("infinite_critical","K to infinity with rho=1"),("infinite_supercritical","K to infinity with rho>1")]
    bkeys=["boundary_id","condition","law"]; check(len(data["regression"]["boundary_rows"])==8,"boundary count")
    for i,row in enumerate(data["regression"]["boundary_rows"]): keys(row,bkeys,f"boundary[{i}]"); check((row["boundary_id"],row["condition"])==b_expected[i],f"boundary[{i}] identity")

    # Direct exact generator checks and a matrix-exponential spot check.
    for lam,mu in [(F(1),F(2)),(F(1),F(1)),(F(2),F(1))]:
        Q=generator(lam,mu,4); check(all(sum(Q[i,j] for j in range(5))==0 for i in range(5)),"generator row sums")
        pi=stationary(lam,mu,4); check(all(sp.Rational(pi[i].numerator,pi[i].denominator)*Q[i,j] == sp.Rational(pi[j].numerator,pi[j].denominator)*Q[j,i] for i in range(5) for j in range(5)),"detailed balance")
        # The exact semigroup preserves constants because Q*1=0.  A small
        # high-precision exponential spot-check is done independently below;
        # symbolic matrix exponentials are intentionally avoided (they create
        # enormous unevaluated radicals and are not needed for this gate).
        check(Q * sp.ones(5, 1) == sp.zeros(5, 1), "generator conserves constants")
    # Explicit singular-rate and capacity faces (not inferred by continuity).
    qk0 = generator(F(1), F(2), 0)
    check(qk0 == sp.zeros(1), "K=0 singleton")
    ql0 = generator(F(0), F(2), 3)
    qm0 = generator(F(2), F(0), 3)
    q00 = generator(F(0), F(0), 3)
    check(all(ql0[0,j] == 0 for j in range(4)) and all(ql0[i,i-1] == 2 for i in range(1,4)), "lambda=0 absorbing zero")
    check(all(qm0[3,j] == 0 for j in range(4)) and all(qm0[i,i+1] == 2 for i in range(3)), "mu=0 absorbing capacity")
    check(q00 == sp.zeros(4), "both rates zero")
    qsym = generator(F(1), F(2), 4)
    cp = sp.factor(qsym.charpoly().as_expr())
    check(cp.subs(qsym.charpoly().gen, 0) == 0, "zero characteristic root")
    # Numerical matrix exponential agrees with the independently reconstructed
    # spectral kernel on one nontrivial row.
    Qm = mp.matrix([[mp.mpf(str(qsym[i,j])) for j in range(5)] for i in range(5)])
    Em = mp.expm(Qm * mpq(F(1, 2)))
    Pspot = expected_kernel(F(1), F(2), 4, F(1, 2))[2]
    check(max(abs(Em[2,j] - Pspot[j]) for j in range(5)) < mp.mpf("1e-65"), "matrix exponential spot check")
    print(json.dumps({"status":"C225_CHECKER_PASS","assertions":assertions,"stationary_rows":len(data["regression"]["stationary_rows"]),"spectral_rows":len(data["regression"]["spectral_rows"]),"kernel_rows":len(data["regression"]["kernel_rows"]),"producer_imported":False},sort_keys=True))


if __name__ == "__main__": main()
