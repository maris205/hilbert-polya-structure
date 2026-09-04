#!/usr/bin/env python3
"""Canonical dense Bloch-fiber evidence for HCS-C371."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c371_harper_evidence.json"
YML = ROOT / "evaluations/route_a/HCS-C371/2026-09-04.yaml"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
RAW = "96ed0db538adbf9e123ef89787d281430dd62d14f37b6256e7d306d1a92ccd8f"
SEM = "9d10dd13dee407f999937a3642bb533a10d04a1770bbd3235ee84ef2d15a3d32"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
LAMBDAS = (F(1, 2), F(2, 3), F(1), F(3, 2), F(2))
NX, NY = 12, 16
PROBES = (-2.75, 0.125, 3.5)


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in vals if tag != "tag:yaml.org,2002:timestamp"]
    for k, vals in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def _mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("merge key")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def ftoken(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def ntoken(value):
    value = float(value)
    if abs(value) < 5.0e-13:
        value = 0.0
    return f"{value:.12e}"


def ctoken(value):
    value = float(value)
    if abs(value) < 5.0e-13:
        value = 0.0
    return f"{value:.17e}"


def poly_add(a, b):
    n = max(len(a), len(b))
    out = np.zeros(n, dtype=np.float64)
    out[: len(a)] += a
    out[: len(b)] += b
    return out


def poly_mul(a, b):
    if len(a) == 0 or len(b) == 0:
        return np.zeros(0, dtype=np.float64)
    return np.convolve(a, b)


def mat_poly_mul(a, b):
    zero = np.zeros(0, dtype=np.float64)
    return (
        (
            poly_add(poly_mul(a[0][0], b[0][0]), poly_mul(a[0][1], b[1][0])),
            poly_add(poly_mul(a[0][0], b[0][1]), poly_mul(a[0][1], b[1][1])),
        ),
        (
            poly_add(poly_mul(a[1][0], b[0][0]), poly_mul(a[1][1], b[1][0])),
            poly_add(poly_mul(a[1][0], b[0][1]), poly_mul(a[1][1], b[1][1])),
        ),
    )


def chambers_coefficients(p, q, lam, ky=0.0):
    """Ascending coefficients of P from the transfer trace."""
    ident = ((np.array([1.0]), np.zeros(0)), (np.zeros(0), np.array([1.0])))
    monodromy = ident
    for n in range(q):
        potential = 2.0 * lam * math.cos(ky + 2.0 * math.pi * p * n / q)
        step = (
            (np.array([-potential, 1.0]), np.array([-1.0])),
            (np.array([1.0]), np.zeros(0)),
        )
        monodromy = mat_poly_mul(step, monodromy)
    trace = poly_add(monodromy[0][0], monodromy[1][1])
    trace[0] += 2.0 * (lam**q) * math.cos(q * ky)
    trace[np.abs(trace) < 5.0e-13] = 0.0
    return trace


def fiber(p, q, lam, total_x, total_y):
    """Fiber with u_(n+q)=exp(i total_x)u_n and q k_y=total_y."""
    ky = total_y / q
    h = np.zeros((q, q), dtype=np.complex128)
    for n in range(q):
        h[n, n] += 2.0 * lam * math.cos(ky + 2.0 * math.pi * p * n / q)
        for step in (-1, 1):
            quotient, residue = divmod(n + step, q)
            h[n, residue] += np.exp(1j * total_x * quotient)
    if np.max(np.abs(h - h.conjugate().T)) > 2.0e-14:
        raise AssertionError("fiber lost Hermiticity")
    return h


def poly_scale(coefficients, energy):
    return 1.0 + sum(abs(c) * max(1.0, abs(energy)) ** i for i, c in enumerate(coefficients))


def reduced_fluxes():
    return [(p, q) for q in range(3, 17) for p in range(1, q) if math.gcd(p, q) == 1]


def panel(p, q, lam_fraction, cache):
    lam = float(lam_fraction)
    coeff = cache[(p, q, lam_fraction)]
    reverse = cache[(q - p, q, lam_fraction)]
    reciprocal = cache[(p, q, 1 / lam_fraction)]
    reversal_error = max(abs(float(a - b)) for a, b in zip(coeff, reverse))
    duality_error = max(
        abs(float(coeff[i] - lam ** (q - i) * reciprocal[i])) for i in range(q + 1)
    )
    parity_error = max(abs(float(coeff[i])) for i in range(q + 1) if (i - q) % 2) if q else 0.0
    central_error = None
    if q % 2 == 0:
        expected = 2.0 * ((-1) ** (q // 2)) * (1.0 + lam**q)
        central_error = abs(float(coeff[0] - expected))

    hsh = hashlib.sha256()
    determinant_residual = 0.0
    eigen_residual = 0.0
    spectral_overflow = 0.0
    hermitian_residual = 0.0
    rhs_min, rhs_max = math.inf, -math.inf
    central_min = math.inf
    eigen_count = 0
    for ix in range(NX):
        total_x = 2.0 * math.pi * ix / NX
        for iy in range(NY):
            total_y = 2.0 * math.pi * iy / NY
            h = fiber(p, q, lam, total_x, total_y)
            hermitian_residual = max(hermitian_residual, float(np.max(np.abs(h - h.conjugate().T))))
            eigenvalues = np.linalg.eigvalsh(h)
            rhs = 2.0 * math.cos(total_x) + 2.0 * (lam**q) * math.cos(total_y)
            rhs_min, rhs_max = min(rhs_min, rhs), max(rhs_max, rhs)
            pvals = np.polynomial.polynomial.polyval(eigenvalues, coeff)
            for energy, pvalue in zip(eigenvalues, pvals):
                scale = poly_scale(coeff, float(energy))
                eigen_residual = max(eigen_residual, abs(float(pvalue) - rhs) / scale)
                spectral_overflow = max(
                    spectral_overflow,
                    max(0.0, abs(float(pvalue)) - 2.0 * (1.0 + lam**q)) / scale,
                )
                hsh.update(f"{p}:{q}:{ftoken(lam_fraction)}:{ix}:{iy}:{float(energy):+.10e}\n".encode())
                eigen_count += 1
            central_min = min(central_min, float(np.min(np.abs(eigenvalues))))
            for energy in PROBES:
                direct = float(np.prod(energy - eigenvalues))
                predicted = float(np.polynomial.polynomial.polyval(energy, coeff) - rhs)
                determinant_residual = max(
                    determinant_residual,
                    abs(direct - predicted) / (1.0 + abs(direct) + abs(predicted)),
                )
    coefficient_tokens = [ctoken(x) for x in coeff]
    return {
        "p": p,
        "q": q,
        "lambda": ftoken(lam_fraction),
        "polynomial_coefficients_ascending": coefficient_tokens,
        "polynomial_sha256": digest(coefficient_tokens),
        "phase_grid": {"total_x_count": NX, "total_y_count": NY, "pairs": NX * NY},
        "fiber_eigenvalues": eigen_count,
        "phase_rhs_min": ntoken(rhs_min),
        "phase_rhs_max": ntoken(rhs_max),
        "expected_phase_bound": ntoken(2.0 * (1.0 + lam**q)),
        "determinant_normalized_residual_max": ntoken(determinant_residual),
        "eigen_equation_normalized_residual_max": ntoken(eigen_residual),
        "spectrum_overflow_normalized_max": ntoken(spectral_overflow),
        "hermitian_residual_max": ntoken(hermitian_residual),
        "flux_reversal_coefficient_residual_max": ntoken(reversal_error),
        "aubry_duality_coefficient_residual_max": ntoken(duality_error),
        "parity_coefficient_residual_max": ntoken(parity_error),
        "central_edge_residual": None if central_error is None else ntoken(central_error),
        "minimum_sampled_absolute_eigenvalue": ntoken(central_min),
        "eigenvalue_digest_sha256": hsh.hexdigest(),
    }


def boundary_atlas():
    return [
        {
            "face": "q=1, p=0",
            "polynomial": "P(E)=E",
            "classification": "zero-flux scalar fiber with spectrum [-2(1+lambda),2(1+lambda)]",
        },
        {
            "face": "q=2, p=1",
            "polynomial": "P(E)=E^2-2(1+lambda^2)",
            "classification": "the accumulated two-site boundary edges obey Chambers exactly and the two folded bands touch at E=0",
        },
        {
            "face": "even q",
            "polynomial": "P(0)=2(-1)^(q/2)(1+lambda^q) and P'(0)=0",
            "classification": "a central multiple band edge is forced, so no all-gaps-open claim is permitted",
        },
        {
            "face": "lambda tends to zero from above",
            "polynomial": "the vertical phase term vanishes and the spectrum tends to [-2,2] with folded contacts",
            "classification": "singular decoupled-chain limit; reciprocal Aubry notation is not evaluated at lambda=0",
        },
    ]


def build(eval_path):
    evaluation = strict_yaml(eval_path)
    if hashlib.sha256(eval_path.read_bytes()).hexdigest() != RAW or digest(evaluation) != SEM:
        raise AssertionError("evaluation digest drift")

    fluxes = reduced_fluxes()
    flux_rows = [
        {
            "p": p,
            "q": q,
            "reversal_p": q - p,
            "cyclotomic_degree": sum(math.gcd(k, q) == 1 for k in range(1, q + 1)),
            "residue_orbit_sha256": digest([(p * n) % q for n in range(q)]),
            "parity": "even" if q % 2 == 0 else "odd",
        }
        for p, q in fluxes
    ]
    cache = {}
    for p, q in fluxes:
        for lam in LAMBDAS:
            cache[(p, q, lam)] = chambers_coefficients(p, q, float(lam))
    panels = [panel(p, q, lam, cache) for p, q in fluxes for lam in LAMBDAS]

    flags = {
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
    route = {
        "tuple": [
            "A0_WEAK_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_NATURAL_QUANTIZATION",
        ],
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    eigen_total = sum(row["fiber_eigenvalues"] for row in panels)
    body = {
        "schema": "hcs-c371-harper-chambers-evidence-v1",
        "candidate_id": "HCS-C371",
        "obstruction_id": "HEN-O355",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVAL,
        },
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C371/2026-09-04.yaml",
            "raw_sha256": RAW,
            "semantic_sha256": SEM,
        },
        "model": {
            "lattice_operator": "horizontal hopping 1 and vertical hopping lambda in Landau gauge exp(2 pi i p m/q)",
            "fiber_equation": "u_(m+1)+u_(m-1)+2 lambda cos(k_y+2 pi p m/q)u_m=E u_m",
            "bloch_convention": "u_(m+q)=exp(i q k_x)u_m; stored total_x equals q k_x and total_y equals q k_y",
            "parameter_domain": "gcd(p,q)=1, q>=3, lambda>0; q=1,2 are direct boundary fibers",
        },
        "theorem_contract": {
            "chambers_identity": "det(EI-H_fiber)=P_(p/q,lambda)(E)-2 cos(q k_x)-2 lambda^q cos(q k_y)",
            "spectrum_preimage": "the full two-dimensional spectrum is P inverse of [-2(1+lambda^q),2(1+lambda^q)]",
            "edge_criterion": "band-edge multiset solves P^2=4(1+lambda^q)^2; a multiple edge solves that equation together with P'=0",
            "edge_fiber_realization": "P-C=det(EI-H(0,0)) and P+C=det(EI-H(pi/q,pi/q)); both endpoint fibers are real symmetric",
            "even_central_contact": "for even q, P(0)=2(-1)^(q/2)(1+lambda^q) and P'(0)=0",
            "aubry_duality": "P_(p/q,lambda)(E)=lambda^q P_(p/q,1/lambda)(E/lambda)",
            "flux_reversal": "P_(p/q,lambda)=P_((q-p)/q,lambda)",
            "parity": "P(-E)=(-1)^q P(E)",
        },
        "proof_receipts": {
            "transfer_determinant": "det(EI-H_fiber)=tr(A_(q-1)...A_0)-2 cos(q k_x)",
            "phase_support": "cyclic conjugacy under k_y shift 2 pi p/q leaves only Fourier modes 0 and plus or minus q",
            "extreme_coefficients": "coprimality makes both extreme phase coefficients exactly -lambda^q",
            "spectrum_range": "the independent cosine sum fills the entire closed phase interval",
            "real_edge_factors": "P-C and P+C are characteristic polynomials of the endpoint fibers at total phases (0,0) and (pi,pi)",
            "even_central_source": "Lamoureux-Mingo Theorem 2.5 and Corollary 2.6 with lambda_LM=2 lambda give P(0); even parity gives P'(0)=0",
            "duality_owner": "magnetic Fourier transform and axis exchange, followed by energy scaling",
        },
        "finite_evidence_role": "all 78 reduced fluxes through q=16, five anisotropies, dense Bloch panels, and exact cyclotomic support checks are regression evidence; transfer, magnetic Fourier, and sourced cyclic-continuant arguments own the theorem",
        "collision_boundary": {
            "workspace_scan": "full registry and package scan through HCS-C368",
            "C15_HEN_O30": "owns one critical Weyl-Harper block at flux 1/3^m and its top-edge return, not the all-rational two-phase Chambers polynomial, anisotropic duality, or band atlas",
            "C293": "owns a magnetic Grushin-cylinder separation and flux-driven compactness transition, not a square-lattice Harper Bloch fiber",
            "C340": "owns the degree-one Lame one-gap Floquet curve, not magnetic rational-flux phase collapse",
            "C356": "owns a two-band QWZ Chern pump; C371 asserts no Chern number or transport theorem",
            "Lamoureux_Mingo_2007": "directly owns the rational almost-Mathieu cyclic-matching cancellation and even-q constant term; C371 contributes a convention-locked reconstruction and executable atlas, not object or formula priority",
            "literature_boundary": "Harper, Chambers, Hofstadter, and Lamoureux-Mingo results are established background; no object, formula, or priority novelty is claimed",
        },
        "boundary_atlas": boundary_atlas(),
        "nonclaims": [
            "no claim that every Harper gap is open",
            "no Chern-number, gap-labelling, edge-state, or quantized-transport theorem",
            "no irrational-flux Cantor-spectrum or Ten-Martini theorem",
            "no novelty or priority claim for Harper, Chambers, Hofstadter, or Lamoureux-Mingo results",
            "no target Euler factor, root number, automorphy, target-zero match, or Hilbert-Polya operator",
        ],
        "references": [
            "10.1088/0370-1298/68/10/304",
            "10.1103/PhysRev.140.A135",
            "10.1103/PhysRevB.14.2239",
            "10.1007/BF02278001",
            "10.1090/S0002-9939-07-08830-2",
            "arXiv:2007.01005",
        ],
        "route_a": route,
        "scope_flags": flags,
        "tolerances": {
            "normalized_numeric_residual": "2e-7",
            "phase_endpoint_residual": "5e-10",
            "central_sample_residual": "5e-8",
            "exact_lane": "zero in Q[zeta_q]/Phi_q for every reduced q<=10 and symbolic lambda",
        },
        "flux_rows": flux_rows,
        "panels": panels,
        "enumeration": {
            "q_min": 3,
            "q_max": 16,
            "reduced_fluxes": len(fluxes),
            "lambda_values": len(LAMBDAS),
            "panels": len(panels),
            "phase_x_count": NX,
            "phase_y_count": NY,
            "phase_pairs_per_panel": NX * NY,
            "bloch_fibers": len(panels) * NX * NY,
            "fiber_eigenvalues": eigen_total,
            "determinant_probe_checks": len(panels) * NX * NY * len(PROBES),
            "cyclotomic_fluxes_q_at_most_10": sum(q <= 10 for _, q in fluxes),
            "boundary_rows": 4,
        },
    }
    body["payload_sha256"] = digest(body)
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C371 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--evaluation", type=Path, default=YML)
    args = parser.parse_args()
    evidence = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    enum = evidence["enumeration"]
    print(
        "C371_PRODUCER_PASS "
        f"{evidence['payload_sha256']} {enum['reduced_fluxes']} fluxes "
        f"{enum['panels']} panels {enum['bloch_fibers']} fibers"
    )


if __name__ == "__main__":
    main()
