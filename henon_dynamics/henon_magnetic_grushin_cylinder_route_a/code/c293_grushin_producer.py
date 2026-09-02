#!/usr/bin/env python3
"""Deterministic evidence producer for HCS-C293 magnetic Grushin cylinder."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c293_grushin_evidence.json"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

MODEL = {
    "space": "L2(R_x times S1_theta, dx dtheta/(2pi))",
    "form": "q_alpha[u]=integral(|partial_x u|^2+x^2|(-i partial_theta+alpha)u|^2)",
    "realization": "nonnegative closed-form Friedrichs realization; essential self-adjointness is not claimed",
    "channels": "theta-Fourier mode k gives -d_x^2+(k+alpha)^2 x^2",
    "flux": "alpha is real modulo integer gauge shifts",
}
THEOREM = {
    "realization": "the closed nonnegative quadratic form defines a unique Friedrichs self-adjoint operator G_alpha",
    "noninteger": "for alpha outside Z the resolvent is compact and the spectrum is pure point lambda_(k,n)=(2n+1)|k+alpha|",
    "integer": "for alpha in Z exactly one resonant Fourier channel has absolutely continuous spectrum [0,infinity) of almost-everywhere multiplicity two, the singular-continuous spectrum is empty, and positive-integer oscillator eigenvalues remain embedded",
    "nonresonant": "after deleting the integer-flux free channel the resolvent is compact and eigenvalue N has multiplicity 2 d_odd(N)",
    "heat": "Tr exp(-t G_alpha)=sum_k 1/(2 sinh(t|k+alpha|)) off integer flux and Tr_perp=sum_(m>=1)1/sinh(tm) at integer flux",
    "source_zeta": "the zero-flux nonresonant spectral zeta is 2(1-2^(-s)) zeta(s)^2 for Re(s)>1",
    "weyl": "N_perp(Lambda)=2 sum_(j odd) floor(Lambda/j)=Lambda log Lambda+(2 gamma+log 2-1)Lambda+O(sqrt Lambda)",
    "boundary": "integer/noninteger flux, half-flux pairing, rational/irrational coincidences, and divergence on approach to resonance are explicit",
}
PROOF = {
    "form": "close the densely defined nonnegative form and use the representation theorem rather than asserting essential self-adjointness",
    "decomposition": "unitary Fourier expansion gives an orthogonal direct sum of one-dimensional channel forms",
    "oscillator": "Hermite scaling gives eigenvalues (2n+1)|k+alpha| whenever k+alpha is nonzero",
    "compactness": "off resonance only finitely many channel-level pairs lie below any energy bound",
    "integer_type": "the resonant block is the free line Laplacian while the orthogonal oscillator sum has compact resolvent, so absolutely continuous and embedded point parts coexist and no singular-continuous part occurs",
    "trace_zeta": "positive-term summation of channel heat traces and Mellin sums yields the displayed source-local series",
    "weyl": "d_odd(N)=d(N)-d(N/2) reduces the count to the elementary divisor summatory formula",
    "finite_role": "finite exact cells audit channel indexing, multiplicity, trace, and counting constants but do not prove the operator theorem",
}
ROUTE = {
    "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_NATURAL_QUANTIZATION"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}
FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
REFERENCES = [
    {
        "id": "BoscainPrandiSeri2016",
        "authors": "Ugo Boscain, Dario Prandi, and Marcello Seri",
        "title": "Spectral analysis and the Aharonov-Bohm effect on certain almost-Riemannian manifolds",
        "venue": "Communications in Partial Differential Equations 41 (2016), 32-50",
        "identifier": "arXiv:1406.6578",
        "url": "https://arxiv.org/abs/1406.6578",
        "ownership": "direct neighboring owner for Grushin-type cylinder spectra and magnetic flux effects; its geometric operator is not silently identified with the present Lebesgue-space form",
    },
    {
        "id": "HarakehHillairet2023",
        "authors": "Mohammad Harakeh and Luc Hillairet",
        "title": "A spectral condition for the control of eigenfunctions of Baouendi-Grushin type operators",
        "venue": "arXiv preprint (2023)",
        "identifier": "arXiv:2312.04359",
        "url": "https://arxiv.org/abs/2312.04359",
        "ownership": "direct neighboring owner for Fourier reduction and compact-resolvent Baouendi-Grushin cylinder sectors",
    },
]


def q(value: Fraction) -> str:
    return str(value)


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 45, strip_zeros=False)


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def d_odd(n: int) -> int:
    return sum(1 for d in range(1, n + 1, 2) if n % d == 0)


def noninteger_heat(alpha: Fraction, t: mp.mpf, cutoff: int = 500) -> mp.mpf:
    a = mp.mpf(alpha.numerator) / alpha.denominator
    return mp.fsum(1 / (2 * mp.sinh(t * abs(k + a))) for k in range(-cutoff, cutoff + 1))


def integer_heat(t: mp.mpf, cutoff: int = 500) -> mp.mpf:
    return mp.fsum(1 / mp.sinh(t * m) for m in range(1, cutoff + 1))


def reduce_flux(alpha: Fraction) -> Fraction:
    r = alpha - (alpha.numerator // alpha.denominator)
    return min(r, 1 - r)


def build() -> dict:
    mp.mp.dps = 80
    fluxes = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 5)]
    k_values = list(range(-5, 6))
    n_values = list(range(5))
    spectral_cells = []
    for alpha in fluxes:
        for k in k_values:
            for n in n_values:
                omega = abs(Fraction(k) + alpha)
                spectral_cells.append({
                    "alpha": q(alpha), "k": k, "n": n, "frequency": q(omega),
                    "eigenvalue": q((2 * n + 1) * omega),
                })

    heat_cells = []
    for alpha in fluxes:
        for t_text in ("0.25", "0.5", "1.0"):
            t = mp.mpf(t_text)
            heat_cells.append({"alpha": q(alpha), "t": t_text, "trace": dec(noninteger_heat(alpha, t)), "k_cutoff": 500})

    integer_heat_cells = []
    for t_text in ("0.25", "0.5", "1.0"):
        t = mp.mpf(t_text)
        integer_heat_cells.append({"t": t_text, "nonresonant_trace": dec(integer_heat(t)), "mode_cutoff": 500})

    multiplicity_cells = [{"N": n, "odd_divisor_count": d_odd(n), "multiplicity": 2 * d_odd(n)} for n in range(1, 97)]
    counting_cells = []
    for limit in (8, 16, 32, 64, 128, 256):
        exact = 2 * sum(limit // j for j in range(1, limit + 1, 2))
        normalized = mp.mpf(exact) / (mp.mpf(limit) * mp.log(limit))
        counting_cells.append({"Lambda": limit, "exact_count": exact, "normalized_by_Lambda_log_Lambda": dec(normalized)})

    zeta_cells = []
    for s in (3, 4, 5, 6):
        value = 2 * (1 - mp.power(2, -s)) * mp.zeta(s) ** 2
        zeta_cells.append({"s": s, "value": dec(value)})

    symmetry_cells = []
    for alpha in [Fraction(-3, 2), Fraction(-1), Fraction(-1, 2), Fraction(-1, 3), Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(3, 2)]:
        distance = reduce_flux(alpha)
        symmetry_cells.append({
            "alpha": q(alpha), "fundamental_distance": q(distance), "ground_energy": q(distance),
            "integer_flux": distance == 0, "half_flux_pairing": distance == Fraction(1, 2),
        })

    integer_spectrum = {
        "absolutely_continuous_spectrum": "[0,infinity) from exactly one free Fourier channel",
        "absolutely_continuous_multiplicity": 2,
        "point_spectrum": "every positive integer, embedded in [0,infinity)",
        "singular_continuous_spectrum_empty": True,
        "nonresonant_compact_resolvent": True,
    }
    enumeration = {
        "noninteger_fluxes": [q(a) for a in fluxes], "k_values": k_values, "n_values": n_values,
        "spectral_cells": len(spectral_cells), "heat_cells": len(heat_cells),
        "integer_heat_cells": len(integer_heat_cells), "multiplicity_cells": len(multiplicity_cells),
        "counting_cells": len(counting_cells), "zeta_cells": len(zeta_cells),
        "symmetry_cells": len(symmetry_cells),
    }
    data = {
        "schema": "hcs-c293-magnetic-grushin-cylinder-v1", "candidate_id": "HCS-C293",
        "evaluation_date": "2026-09-02", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE, "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL, "theorem_contract": THEOREM, "proof_contract": PROOF,
        "route_a": ROUTE, "scope_flags": FLAGS, "enumeration": enumeration,
        "spectral_cells": spectral_cells, "heat_cells": heat_cells,
        "integer_heat_cells": integer_heat_cells, "multiplicity_cells": multiplicity_cells,
        "counting_cells": counting_cells, "zeta_cells": zeta_cells,
        "symmetry_cells": symmetry_cells, "integer_spectrum": integer_spectrum,
        "references": REFERENCES,
        "nonclaims": [
            "the Friedrichs realization is used and essential self-adjointness on a smaller core is not claimed",
            "classical oscillator and Grushin spectral mechanisms are not claimed as literature originality",
            "the source-local divisor multiplicity and zeta factorization are not target Euler factors, a target divisor law, a target functional equation, a target zero correspondence, or a Hilbert-Polya operator",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = build(); args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    e = data["enumeration"]
    cells = sum(e[k] for k in ("spectral_cells", "heat_cells", "integer_heat_cells", "multiplicity_cells", "counting_cells", "zeta_cells", "symmetry_cells"))
    print(f"C293_PRODUCER_PASS {data['payload_sha256']} audited_cells={cells}")


if __name__ == "__main__":
    main()
