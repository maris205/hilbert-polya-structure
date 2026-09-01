#!/usr/bin/env python3
"""Deterministic high-precision and finite-DFT receipt for HCS-C283."""
from __future__ import annotations

import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C283_OUTPUT_PATH", ROOT / "results/c283_padic_evidence.json"))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90


def qs(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def ds(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-78"):
        x = mp.mpf(0)
    return mp.nstr(x, 72, strip_zeros=False)


def payload_hash(data: dict) -> str:
    payload = dict(data)
    payload.pop("payload_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def valuation(k: int, p: int) -> int:
    value = 0
    while k and k % p == 0:
        value += 1
        k //= p
    return value


def conditional_expectation(vector: np.ndarray, p: int, n: int) -> np.ndarray:
    """Average over cosets modulo p^n on a finite p-power quotient."""
    modulus = p**n
    answer = np.empty_like(vector, dtype=np.complex128)
    for residue in range(modulus):
        answer[residue::modulus] = np.mean(vector[residue::modulus])
    return answer


def finite_dft_error(p: int, level: int, alpha: Q) -> tuple[float, float]:
    q = p**level
    aa = float(alpha)
    j = np.arange(q, dtype=np.float64)
    vector = (np.cos((j + 1.0) * math.sqrt(2.0))
              + 0.25 * np.sin((j + 2.0) * math.sqrt(3.0))
              + 1j * np.cos((j + 3.0) * math.sqrt(5.0)))
    multipliers = np.zeros(q, dtype=np.float64)
    for k in range(1, q):
        conductor = level - valuation(k, p)
        multipliers[k] = p ** (aa * conductor)
    via_dft = np.fft.ifft(multipliers * np.fft.fft(vector))
    previous = conditional_expectation(vector, p, 0)
    via_filtration = np.zeros(q, dtype=np.complex128)
    for n in range(1, level + 1):
        current = conditional_expectation(vector, p, n)
        via_filtration += p ** (aa * n) * (current - previous)
        previous = current
    trace = sum((p - 1) * p ** (n - 1) * p ** (aa * n)
                for n in range(1, level + 1))
    return float(np.max(np.abs(via_dft - via_filtration))), float(trace)


def heat_trace(p: int, alpha: Q, mu: Q, t: Q) -> tuple[mp.mpf, int]:
    aa = mp.mpf(alpha.numerator) / alpha.denominator
    mm = mp.mpf(mu.numerator) / mu.denominator
    tt = mp.mpf(t.numerator) / t.denominator
    total = mp.mpf(1)
    decreasing = 0
    previous = mp.inf
    for n in range(1, 1000):
        term = (p - 1) * p ** (n - 1) * mp.exp(-tt * mp.power(p, aa * n))
        total += term
        decreasing = decreasing + 1 if term < previous else 0
        previous = term
        if decreasing >= 8 and term < mp.mpf("1e-82"):
            return mp.exp(-mm * tt) * total, n
    raise RuntimeError("heat trace summation did not settle")


def main() -> None:
    primes = (2, 3, 5, 7)
    alphas = (Q(1, 2), Q(1), Q(2))

    shell_cells = []
    for p in primes:
        for alpha in alphas:
            aa = mp.mpf(alpha.numerator) / alpha.denominator
            for n in range(1, 9):
                shell_cells.append({
                    "p": p, "alpha": qs(alpha), "conductor": n,
                    "eigenvalue": ds(mp.power(p, aa * n)),
                    "multiplicity": (p - 1) * p ** (n - 1),
                    "cumulative_mean_zero_count": p**n - 1,
                })

    quotient_cases = ((2, 4), (2, 8), (2, 12), (3, 3), (3, 5), (3, 7),
                      (5, 2), (5, 4), (5, 5), (7, 2), (7, 3), (7, 4))
    finite_quotient_cells = []
    for p, level in quotient_cases:
        for alpha in alphas:
            error, trace = finite_dft_error(p, level, alpha)
            finite_quotient_cells.append({
                "p": p, "level": level, "quotient_order": p**level,
                "alpha": qs(alpha),
                "dft_hierarchical_max_error": f"{error:.17e}",
                "dft_error_over_top_eigenvalue": f"{error / p ** (float(alpha) * level):.17e}",
                "trace_D": f"{trace:.17e}",
                "nonzero_character_count": p**level - 1,
                "top_shell_multiplicity": (p - 1) * p ** (level - 1),
            })

    heat_trace_cells = []
    for p in primes:
        for alpha in alphas:
            for mu in (Q(0), Q(1, 3)):
                for t in (Q(1, 8), Q(1), Q(8)):
                    value, terms = heat_trace(p, alpha, mu, t)
                    heat_trace_cells.append({
                        "p": p, "alpha": qs(alpha), "mu": qs(mu), "t": qs(t),
                        "heat_trace": ds(value), "shells_summed": terms,
                    })

    zeta_cells = []
    for p in primes:
        for alpha in alphas:
            aa = mp.mpf(alpha.numerator) / alpha.denominator
            for alpha_s in (Q(3, 2), Q(2), Q(3)):
                cc = mp.mpf(alpha_s.numerator) / alpha_s.denominator
                ratio = mp.power(p, 1 - cc)
                value = (1 - mp.mpf(1) / p) * ratio / (1 - ratio)
                partial = mp.fsum((p - 1) * p ** (n - 1) * mp.power(p, -cc * n)
                                  for n in range(1, 161))
                zeta_cells.append({
                    "p": p, "alpha": qs(alpha), "alpha_times_s": qs(alpha_s),
                    "s": ds(cc / aa), "closed_value": ds(value),
                    "partial_160_error": ds(abs(value - partial)),
                })

    pole_cells = []
    for p in primes:
        for alpha in alphas:
            aa = mp.mpf(alpha.numerator) / alpha.denominator
            residue = (1 - mp.mpf(1) / p) / (aa * mp.log(p))
            for k in range(-3, 4):
                pole_cells.append({
                    "p": p, "alpha": qs(alpha), "k": k,
                    "real_part": ds(1 / aa),
                    "imaginary_part": ds(2 * mp.pi * k / (aa * mp.log(p))),
                    "residue": ds(residue),
                })

    counting_cells = []
    for p in primes:
        for alpha in alphas:
            for m in range(1, 7):
                count = p**m - 1
                counting_cells.append({
                    "p": p, "alpha": qs(alpha), "shell": m,
                    "N_at_eigenvalue": count,
                    "scaled_ratio_at_eigenvalue": qs(Q(count, p**m)),
                    "scaled_ratio_before_next_shell": qs(Q(count, p ** (m + 1))),
                })

    schatten_cells = []
    for alpha in alphas:
        for sigma in (Q(1, 2), Q(1), Q(2)):
            for q in (Q(1, 2), Q(1), Q(2)):
                product = alpha * sigma * q
                schatten_cells.append({
                    "alpha": qs(alpha), "sigma": qs(sigma), "q": qs(q),
                    "alpha_sigma_q": qs(product), "in_S_q": product > 1,
                    "endpoint_diverges": product == 1,
                })

    control_cells = []
    for branching in (4, 6, 10):
        for m in range(1, 6):
            control_cells.append({
                "branching": branching, "shell": m,
                "multiplicity": (branching - 1) * branching ** (m - 1),
                "cumulative_count": branching**m - 1,
                "same_closed_form": True,
            })

    counts = {
        "shell_cells": len(shell_cells),
        "finite_quotient_cells": len(finite_quotient_cells),
        "heat_trace_cells": len(heat_trace_cells),
        "zeta_cells": len(zeta_cells),
        "pole_cells": len(pole_cells),
        "counting_cells": len(counting_cells),
        "schatten_cells": len(schatten_cells),
        "control_cells": len(control_cells),
    }
    data = {
        "schema": "hcs-c283-padic-conductor-shell-heat-v1",
        "candidate_id": "HCS-C283",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "owner": {
            "state_space": "L2(Z_p,Haar probability)",
            "prime_parameter": "p is an arbitrary but fixed rational prime",
            "dual": "Q_p/Z_p with conductor shells n>=1",
            "operator": "D_{p,alpha}1=0 and D_{p,alpha}chi=p^(alpha*n(chi))*chi",
            "parameters": "p prime, alpha>0, mu>=0, t>=0",
            "normalization": "explicit Fourier multiplier; no Vladimirov normalization is imported",
        },
        "theorem_contract": {
            "spectrum": "D has 0 simple and p^(alpha*n) with multiplicity (p-1)*p^(n-1); A=D+mu*I has mu simple and mu+p^(alpha*n) with the same multiplicities",
            "markov": "exp(-t*D) is positive, conservative, self-adjoint, and contractive for t>=0",
            "killing": "exp(-t*(D+mu*I)) is positive sub-Markov with norm exp(-mu*t)",
            "heat_trace": "for t>0 the trace is exp(-mu*t)*(1+sum_(n>=1)(p-1)*p^(n-1)*exp(-t*p^(alpha*n)))",
            "zeta": "on mean-zero space zeta(s)=(1-p^(-1))*p^(1-alpha*s)/(1-p^(1-alpha*s))",
            "pole_lattice": "simple poles 1/alpha+2*pi*i*k/(alpha*log(p)), residue (1-p^(-1))/(alpha*log(p))",
            "determinant": "zeta(0)=-1, zeta'(0)=-alpha*log(p)/(p-1), det'_zeta(D)=p^(alpha/(p-1))",
            "counting": "p^(alpha*m)<=Lambda<p^(alpha*(m+1)) implies N(Lambda)=p^m-1; limsup=1 and liminf=1/p",
            "schatten": "(I+D)^(-sigma) is in S_q iff alpha*sigma*q>1; equality diverges",
            "boundaries": "alpha=0 gives I-P0 and only strong semigroup convergence; mu=0 retains the zero mode; t=0 is the noncompact identity",
        },
        "proof_obligations": [
            "Pontryagin character count and self-adjoint multiplier domain",
            "filtration reconstruction and positive Markov contraction",
            "trace class heat formula and compact resolvent",
            "meromorphic zeta continuation, complete pole lattice, and primed determinant",
            "exact staircase counting, discrete-scale oscillation, and sharp Schatten endpoint",
            "alpha=0, mu=0, t=0 boundary atlas and finite-quotient DFT reconstruction",
        ],
        "regression": {
            "shell_cells": shell_cells,
            "finite_quotient_cells": finite_quotient_cells,
            "heat_trace_cells": heat_trace_cells,
            "zeta_cells": zeta_cells,
            "pole_cells": pole_cells,
            "counting_cells": counting_cells,
            "schatten_cells": schatten_cells,
            "control_cells": control_cells,
            "boundaries": [
                {"face": "alpha=0", "operator": "I-P0", "compact": False, "convergence_from_alpha_positive": "strong_not_norm"},
                {"face": "mu=0", "constant_mode": "zero", "markov": True, "determinant_convention": "mean_zero_primed"},
                {"face": "t=0", "operator": "identity", "compact": False, "finite_S_q": False},
                {"face": "alpha_to_infinity", "positive_time_limit": "exp(-mu*t)*P0", "convergence": "operator_norm"},
            ],
            "counts": counts,
        },
        "route_a": {
            "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "target_arithmetic_local_data": False, "euler_factors": False,
            "root_numbers": False, "automorphy": False, "target_divisor": False,
            "functional_equation": False, "hilbert_polya_operator": False,
        },
        "sources": [
            {"author": "V. S. Vladimirov", "title": "On the spectrum of some pseudodifferential operators over the field of p-adic numbers", "venue": "Algebra i Analiz 2:6 (1990), 107-124; Leningrad Math. J. 2:6 (1991), 1261-1278", "url": "https://www.mathnet.ru/eng/aa223", "role": "p-adic pseudodifferential spectral setting, not the frozen normalization"},
            {"author": "S. V. Kozyrev", "title": "Wavelet theory as p-adic spectral analysis", "venue": "Izvestiya: Mathematics 66:2 (2002), 367-376", "doi": "10.1070/IM2002v066n02ABEH000381", "role": "p-adic wavelet spectral decomposition"},
            {"author": "A. D. Bendikov, A. A. Grigor'yan, Ch. Pittet, and W. Woess", "title": "Isotropic Markov semigroups on ultra-metric spaces", "venue": "Russian Mathematical Surveys 69:4 (2014), 589-680", "doi": "10.1070/RM2014v069n04ABEH004907", "role": "hierarchical ultrametric Markov semigroups"},
            {"author": "L. F. Chacon-Cortes and W. A. Zuniga-Galindo", "title": "Heat traces and spectral zeta functions for p-adic Laplacians", "venue": "Algebra i Analiz 29:3 (2017), 144-166; St. Petersburg Math. J. 29:3 (2018), 529-544", "doi": "10.1090/spmj/1505", "role": "p-adic heat-trace and spectral-zeta context"},
            {"author": "V. S. Vladimirov, I. V. Volovich, and E. I. Zelenov", "title": "p-Adic Analysis and Mathematical Physics", "venue": "World Scientific, 1994, xx+319 pp., ISBN 978-981-02-0880-6", "role": "monograph background"},
        ],
        "collision_audit": [
            "C277 is a time-Caputo Dirichlet non-semigroup; C283 is a spatial compact p-adic Markov semigroup.",
            "C184 is finite pre-gasket spectral decimation; C283 uses an infinite compact ultrametric group.",
            "C174 is a deterministic 2-adic parity return map; C283 is a self-adjoint Fourier multiplier for every fixed prime p.",
            "C28 is an all-prime weighted direct sum; C283 deliberately freezes one local prime and forbids aggregation over primes.",
            "NLS, KdV, and Euclidean fractional-heat owners do not share this conductor filtration or spectrum.",
        ],
        "nonclaims": [
            "An arbitrary fixed p is not the family of all rational primes and supplies no target Euler data.",
            "The multiplier is not asserted to equal every convention called the Vladimirov operator.",
            "The mean-zero spectral zeta and determinant are source-local and are not a target zeta function or Hilbert-Polya construction.",
            "Workspace ownership is not a literature-priority claim.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C283_PRODUCER_PASS cells={sum(counts.values())} dft={counts['finite_quotient_cells']} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
