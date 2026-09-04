#!/usr/bin/env python3
"""Independent fiber-characteristic checker for HCS-C371.

This file never imports the producer.  In particular it recovers every
Chambers polynomial from a reference Hermitian fiber characteristic
polynomial, rather than from transfer-polynomial multiplication.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / "results/c371_harper_evidence.json"
YML = ROOT / "evaluations/route_a/HCS-C371/2026-09-04.yaml"
RAW = "96ed0db538adbf9e123ef89787d281430dd62d14f37b6256e7d306d1a92ccd8f"
SEM = "9d10dd13dee407f999937a3642bb533a10d04a1770bbd3235ee84ef2d15a3d32"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROUTE = [
    "A0_WEAK_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_NATURAL_QUANTIZATION",
]
LAMBDAS = (F(1, 2), F(2, 3), F(1), F(3, 2), F(2))
NX, NY = 12, 16
PROBES = (-2.75, 0.125, 3.5)
TOL = 2.0e-7

TOP = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date",
    "source_commit", "fixed_epoch", "scope_literal", "evaluator",
    "route_a_yaml", "model", "theorem_contract", "proof_receipts",
    "finite_evidence_role", "collision_boundary", "boundary_atlas",
    "nonclaims", "references", "route_a", "scope_flags", "tolerances",
    "flux_rows", "panels", "enumeration", "payload_sha256",
}
PANEL_KEYS = {
    "p", "q", "lambda", "polynomial_coefficients_ascending",
    "polynomial_sha256", "phase_grid", "fiber_eigenvalues",
    "phase_rhs_min", "phase_rhs_max", "expected_phase_bound",
    "determinant_normalized_residual_max",
    "eigen_equation_normalized_residual_max",
    "spectrum_overflow_normalized_max", "hermitian_residual_max",
    "flux_reversal_coefficient_residual_max",
    "aubry_duality_coefficient_residual_max",
    "parity_coefficient_residual_max", "central_edge_residual",
    "minimum_sampled_absolute_eigenvalue", "eigenvalue_digest_sha256",
}


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


def strict_json(path):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out

    return json.loads(
        path.read_text(),
        object_pairs_hook=unique,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)),
    )


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def keys(value, expected):
    if type(value) is not dict or set(value) != set(expected):
        raise AssertionError("schema drift")


def typed_equal(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(typed_equal(left[k], right[k]) for k in left)
    if type(left) in (list, tuple):
        return len(left) == len(right) and all(typed_equal(a, b) for a, b in zip(left, right))
    return left == right


def ftoken(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def ntoken(value):
    value = float(value)
    if abs(value) < 5.0e-13:
        value = 0.0
    return f"{value:.12e}"


def reference_fiber(p, q, lam, total_x, total_y):
    """Independent explicit q>=3 cyclic matrix construction."""
    ky = total_y / q
    h = np.zeros((q, q), dtype=np.complex128)
    for n in range(q):
        h[n, n] = 2.0 * lam * math.cos(ky + 2.0 * math.pi * p * n / q)
    for n in range(q - 1):
        h[n, n + 1] = 1.0
        h[n + 1, n] = 1.0
    h[0, q - 1] = np.exp(-1j * total_x)
    h[q - 1, 0] = np.exp(1j * total_x)
    return h


def reference_polynomial(p, q, lam):
    eigenvalues = np.linalg.eigvalsh(reference_fiber(p, q, lam, 0.0, 0.0))
    coefficients = np.poly(eigenvalues)[::-1].real
    coefficients[0] += 2.0 + 2.0 * lam**q
    coefficients[np.abs(coefficients) < 5.0e-12] = 0.0
    return coefficients


def poly_scale(coefficients, energy):
    return 1.0 + sum(abs(c) * max(1.0, abs(energy)) ** i for i, c in enumerate(coefficients))


def expected_boundaries():
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


def validate_yaml(x, yaml_path):
    count = 0
    y = strict_yaml(yaml_path)
    assert hashlib.sha256(yaml_path.read_bytes()).hexdigest() == RAW and digest(y) == SEM
    count += 2
    ykeys = {
        "schema", "candidate_id", "title", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
        "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
        "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
        "arithmetic_origin", "clock", "normalization", "determinant_convention",
        "orbit_cutoff", "precision", "training_data", "forbidden_data",
        "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple",
        "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
        "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
    }
    keys(y, ykeys)
    count += 1
    assert y["schema"] == "route-a-evaluation-v0.2.0"
    assert y["candidate_id"] == "HCS-C371" and y["obstruction_id"] == "HEN-O355"
    assert y["evaluation_date"] == "2026-09-04" and y["source_commit"] == SOURCE
    assert typed_equal(y["fixed_epoch"], 1788480000) and y["scope_literal"] == SCOPE
    count += 6
    assert y["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md"
    assert y["evaluator_version"] == "0.2.0" and y["evaluator_authority_sha256"] == EVAL
    assert y["tuple"] == ROUTE and y["overall_verdict"] == "ROUTE_A_REJECTED"
    assert y["route_b_invocation_allowed"] is False
    count += 6
    gates = {
        "a0": (
            "A0_WEAK_ARITHMETIC_RELATION", "PROVED",
            "reduced rational flux organizes exact cyclotomic magnetic translations and finite q-dimensional Bloch fibers",
            "flux denominators are source parameters and supply no canonical rational-prime carrier, prime-power repetition law, arithmetic local weight, or logarithmic-prime clock",
        ),
        "a1": (
            "A1_FAIL", "PROVED",
            "every Bloch fiber and its complete band-edge multiplicity atlas are exact in the same source normalization",
            "Bloch waves and quasimomenta do not form an isolated classical primitive-periodic-orbit ledger with source-derived prime labels",
        ),
        "a2": (
            "A2_FAIL", "STOP_SCOPED",
            "the Chambers polynomial is a canonical finite source characteristic polynomial independent of both Bloch phases after explicit terms are removed",
            "the finite magnetic characteristic polynomial is not a primitive-orbit Euler product, target Fredholm determinant, or target divisor",
        ),
        "a3": (
            "A3_FAIL", "STOP_SCOPED",
            "Chambers phase collapse, spectral preimage, duality, flux reversal, parity, and every declared small-q boundary are analytic",
            "no target continuation, functional equation, counting law, divisor match, or Weil compression is constructed",
        ),
        "a4": (
            "A4_NATURAL_QUANTIZATION", "PROVED",
            "the source object is already a bounded self-adjoint magnetic tight-binding Hamiltonian with canonical unitary time evolution",
            "its source Bloch bands are not a target-zero spectrum or Hilbert--Polya realization",
        ),
    }
    for name, (verdict, status, evidence, failure) in gates.items():
        keys(y[name], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"})
        assert typed_equal(
            y[name],
            {
                "verdict": verdict,
                "evidence_status": status,
                "strongest_evidence": evidence,
                "strongest_failure": failure,
            },
        )
        count += 2
    assert y["theorem_status"] == "PROVABLE_AS_STATED"
    assert y["finite_evidence_role"] == "all-flux dense phase and spectral regression plus exact cyclotomic support checks; transfer matrices, magnetic Fourier duality, and the sourced cyclic-continuant identity prove the continuum theorem"
    assert y["source_owner_tokens"] == [
        "DOI:10.1088/0370-1298/68/10/304",
        "DOI:10.1103/PhysRev.140.A135",
        "DOI:10.1103/PhysRevB.14.2239",
        "DOI:10.1007/BF02278001",
        "DOI:10.1090/S0002-9939-07-08830-2",
    ]
    assert typed_equal(x["scope_flags"], y["scope_flags"])
    assert all(type(value) is bool and value is False for value in y["scope_flags"].values())
    count += 5
    return count


def check(evidence=EV, yaml_path=YML):
    count = 0
    x = strict_json(evidence)
    keys(x, TOP)
    count += 1
    claimed = x.pop("payload_sha256")
    assert claimed == hashlib.sha256(canonical(x)).hexdigest()
    x["payload_sha256"] = claimed
    count += 1
    assert x["schema"] == "hcs-c371-harper-chambers-evidence-v1"
    assert x["candidate_id"] == "HCS-C371" and x["obstruction_id"] == "HEN-O355"
    assert x["evaluation_date"] == "2026-09-04" and x["source_commit"] == SOURCE
    assert typed_equal(x["fixed_epoch"], 1788480000) and x["scope_literal"] == SCOPE
    count += 7
    assert typed_equal(
        x["evaluator"],
        {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVAL},
    )
    assert typed_equal(
        x["route_a_yaml"],
        {
            "relative_path": "evaluations/route_a/HCS-C371/2026-09-04.yaml",
            "raw_sha256": RAW,
            "semantic_sha256": SEM,
        },
    )
    count += 2
    count += validate_yaml(x, yaml_path)

    model = {
        "lattice_operator": "horizontal hopping 1 and vertical hopping lambda in Landau gauge exp(2 pi i p m/q)",
        "fiber_equation": "u_(m+1)+u_(m-1)+2 lambda cos(k_y+2 pi p m/q)u_m=E u_m",
        "bloch_convention": "u_(m+q)=exp(i q k_x)u_m; stored total_x equals q k_x and total_y equals q k_y",
        "parameter_domain": "gcd(p,q)=1, q>=3, lambda>0; q=1,2 are direct boundary fibers",
    }
    theorem = {
        "chambers_identity": "det(EI-H_fiber)=P_(p/q,lambda)(E)-2 cos(q k_x)-2 lambda^q cos(q k_y)",
        "spectrum_preimage": "the full two-dimensional spectrum is P inverse of [-2(1+lambda^q),2(1+lambda^q)]",
        "edge_criterion": "band-edge multiset solves P^2=4(1+lambda^q)^2; a multiple edge solves that equation together with P'=0",
        "edge_fiber_realization": "P-C=det(EI-H(0,0)) and P+C=det(EI-H(pi/q,pi/q)); both endpoint fibers are real symmetric",
        "even_central_contact": "for even q, P(0)=2(-1)^(q/2)(1+lambda^q) and P'(0)=0",
        "aubry_duality": "P_(p/q,lambda)(E)=lambda^q P_(p/q,1/lambda)(E/lambda)",
        "flux_reversal": "P_(p/q,lambda)=P_((q-p)/q,lambda)",
        "parity": "P(-E)=(-1)^q P(E)",
    }
    proof = {
        "transfer_determinant": "det(EI-H_fiber)=tr(A_(q-1)...A_0)-2 cos(q k_x)",
        "phase_support": "cyclic conjugacy under k_y shift 2 pi p/q leaves only Fourier modes 0 and plus or minus q",
        "extreme_coefficients": "coprimality makes both extreme phase coefficients exactly -lambda^q",
        "spectrum_range": "the independent cosine sum fills the entire closed phase interval",
        "real_edge_factors": "P-C and P+C are characteristic polynomials of the endpoint fibers at total phases (0,0) and (pi,pi)",
        "even_central_source": "Lamoureux-Mingo Theorem 2.5 and Corollary 2.6 with lambda_LM=2 lambda give P(0); even parity gives P'(0)=0",
        "duality_owner": "magnetic Fourier transform and axis exchange, followed by energy scaling",
    }
    assert typed_equal(x["model"], model) and typed_equal(x["theorem_contract"], theorem)
    assert typed_equal(x["proof_receipts"], proof)
    assert x["finite_evidence_role"] == "all 78 reduced fluxes through q=16, five anisotropies, dense Bloch panels, and exact cyclotomic support checks are regression evidence; transfer, magnetic Fourier, and sourced cyclic-continuant arguments own the theorem"
    count += 4
    collision = {
        "workspace_scan": "full registry and package scan through HCS-C368",
        "C15_HEN_O30": "owns one critical Weyl-Harper block at flux 1/3^m and its top-edge return, not the all-rational two-phase Chambers polynomial, anisotropic duality, or band atlas",
        "C293": "owns a magnetic Grushin-cylinder separation and flux-driven compactness transition, not a square-lattice Harper Bloch fiber",
        "C340": "owns the degree-one Lame one-gap Floquet curve, not magnetic rational-flux phase collapse",
        "C356": "owns a two-band QWZ Chern pump; C371 asserts no Chern number or transport theorem",
        "Lamoureux_Mingo_2007": "directly owns the rational almost-Mathieu cyclic-matching cancellation and even-q constant term; C371 contributes a convention-locked reconstruction and executable atlas, not object or formula priority",
        "literature_boundary": "Harper, Chambers, Hofstadter, and Lamoureux-Mingo results are established background; no object, formula, or priority novelty is claimed",
    }
    assert typed_equal(x["collision_boundary"], collision)
    assert typed_equal(x["boundary_atlas"], expected_boundaries())
    assert x["nonclaims"] == [
        "no claim that every Harper gap is open",
        "no Chern-number, gap-labelling, edge-state, or quantized-transport theorem",
        "no irrational-flux Cantor-spectrum or Ten-Martini theorem",
        "no novelty or priority claim for Harper, Chambers, Hofstadter, or Lamoureux-Mingo results",
        "no target Euler factor, root number, automorphy, target-zero match, or Hilbert-Polya operator",
    ]
    assert x["references"] == [
        "10.1088/0370-1298/68/10/304", "10.1103/PhysRev.140.A135",
        "10.1103/PhysRevB.14.2239", "10.1007/BF02278001",
        "10.1090/S0002-9939-07-08830-2", "arXiv:2007.01005",
    ]
    assert typed_equal(x["route_a"], {"tuple": ROUTE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    assert typed_equal(
        x["tolerances"],
        {
            "normalized_numeric_residual": "2e-7",
            "phase_endpoint_residual": "5e-10",
            "central_sample_residual": "5e-8",
            "exact_lane": "zero in Q[zeta_q]/Phi_q for every reduced q<=10 and symbolic lambda",
        },
    )
    count += 6

    fluxes = [(p, q) for q in range(3, 17) for p in range(1, q) if math.gcd(p, q) == 1]
    expected_flux_rows = [
        {
            "p": p, "q": q, "reversal_p": q - p,
            "cyclotomic_degree": sum(math.gcd(k, q) == 1 for k in range(1, q + 1)),
            "residue_orbit_sha256": digest([(p * n) % q for n in range(q)]),
            "parity": "even" if q % 2 == 0 else "odd",
        }
        for p, q in fluxes
    ]
    assert typed_equal(x["flux_rows"], expected_flux_rows)
    count += len(fluxes)
    expected_order = [(p, q, lam) for p, q in fluxes for lam in LAMBDAS]
    assert len(x["panels"]) == len(expected_order)
    by_key = {}
    for row, (p, q, lam_fraction) in zip(x["panels"], expected_order):
        keys(row, PANEL_KEYS)
        assert typed_equal(row["p"], p) and typed_equal(row["q"], q)
        assert row["lambda"] == ftoken(lam_fraction)
        assert typed_equal(row["phase_grid"], {"total_x_count": NX, "total_y_count": NY, "pairs": NX * NY})
        coefficients = np.array([float(token) for token in row["polynomial_coefficients_ascending"]])
        assert len(coefficients) == q + 1 and abs(coefficients[-1] - 1.0) < 1.0e-10
        assert row["polynomial_sha256"] == digest(row["polynomial_coefficients_ascending"])
        reference = reference_polynomial(p, q, float(lam_fraction))
        assert np.max(np.abs(coefficients - reference) / (1.0 + np.abs(reference))) < 1.0e-7
        by_key[(p, q, lam_fraction)] = (row, coefficients)
        count += q + 8

    for p, q, lam_fraction in expected_order:
        row, coefficients = by_key[(p, q, lam_fraction)]
        reverse = by_key[(q - p, q, lam_fraction)][1]
        reciprocal = by_key[(p, q, 1 / lam_fraction)][1]
        lam = float(lam_fraction)
        reversal = max(abs(float(a - b)) for a, b in zip(coefficients, reverse))
        duality = max(abs(float(coefficients[i] - lam ** (q - i) * reciprocal[i])) for i in range(q + 1))
        parity = max(abs(float(coefficients[i])) for i in range(q + 1) if (i - q) % 2)
        assert row["flux_reversal_coefficient_residual_max"] == ntoken(reversal)
        assert row["aubry_duality_coefficient_residual_max"] == ntoken(duality)
        assert row["parity_coefficient_residual_max"] == ntoken(parity)
        assert max(reversal, duality, parity) < TOL
        if q % 2:
            assert row["central_edge_residual"] is None
        else:
            central = abs(float(coefficients[0] - 2.0 * ((-1) ** (q // 2)) * (1.0 + lam**q)))
            assert row["central_edge_residual"] == ntoken(central) and central < TOL
        count += 5

        hsh = hashlib.sha256()
        determinant_residual = 0.0
        eigen_residual = 0.0
        overflow = 0.0
        rhs_min, rhs_max = math.inf, -math.inf
        central_min = math.inf
        eigen_count = 0
        for ix in range(NX):
            total_x = 2.0 * math.pi * ix / NX
            for iy in range(NY):
                total_y = 2.0 * math.pi * iy / NY
                h = reference_fiber(p, q, lam, total_x, total_y)
                assert np.max(np.abs(h - h.conjugate().T)) < 2.0e-14
                eigenvalues = np.linalg.eigvalsh(h)
                rhs = 2.0 * math.cos(total_x) + 2.0 * lam**q * math.cos(total_y)
                rhs_min, rhs_max = min(rhs_min, rhs), max(rhs_max, rhs)
                pvalues = np.polynomial.polynomial.polyval(eigenvalues, coefficients)
                for energy, pvalue in zip(eigenvalues, pvalues):
                    scale = poly_scale(coefficients, float(energy))
                    eigen_residual = max(eigen_residual, abs(float(pvalue) - rhs) / scale)
                    overflow = max(
                        overflow,
                        max(0.0, abs(float(pvalue)) - 2.0 * (1.0 + lam**q)) / scale,
                    )
                    hsh.update(f"{p}:{q}:{ftoken(lam_fraction)}:{ix}:{iy}:{float(energy):+.10e}\n".encode())
                    eigen_count += 1
                central_min = min(central_min, float(np.min(np.abs(eigenvalues))))
                for energy in PROBES:
                    direct = float(np.prod(energy - eigenvalues))
                    predicted = float(np.polynomial.polynomial.polyval(energy, coefficients) - rhs)
                    determinant_residual = max(
                        determinant_residual,
                        abs(direct - predicted) / (1.0 + abs(direct) + abs(predicted)),
                    )
        bound = 2.0 * (1.0 + lam**q)
        assert row["eigenvalue_digest_sha256"] == hsh.hexdigest()
        assert typed_equal(row["fiber_eigenvalues"], eigen_count)
        assert row["phase_rhs_min"] == ntoken(rhs_min) and row["phase_rhs_max"] == ntoken(rhs_max)
        assert row["expected_phase_bound"] == ntoken(bound)
        assert row["minimum_sampled_absolute_eigenvalue"] == ntoken(central_min)
        assert abs(rhs_min + bound) < 5.0e-10 and abs(rhs_max - bound) < 5.0e-10
        assert determinant_residual < TOL and eigen_residual < TOL and overflow < TOL
        assert float(row["determinant_normalized_residual_max"]) < TOL
        assert float(row["eigen_equation_normalized_residual_max"]) < TOL
        assert float(row["spectrum_overflow_normalized_max"]) < TOL
        assert float(row["hermitian_residual_max"]) < TOL
        if q % 2 == 0:
            assert central_min < 5.0e-8
        count += eigen_count + NX * NY * (len(PROBES) + 1) + 13

    eigen_total = sum(q * NX * NY for p, q, lam in expected_order)
    enum = {
        "q_min": 3, "q_max": 16, "reduced_fluxes": 78, "lambda_values": 5,
        "panels": 390, "phase_x_count": NX, "phase_y_count": NY,
        "phase_pairs_per_panel": NX * NY, "bloch_fibers": 390 * NX * NY,
        "fiber_eigenvalues": eigen_total,
        "determinant_probe_checks": 390 * NX * NY * len(PROBES),
        "cyclotomic_fluxes_q_at_most_10": 30, "boundary_rows": 4,
    }
    assert typed_equal(x["enumeration"], enum)
    count += 1
    return count


def main():
    if sys.flags.optimize:
        raise RuntimeError("C371 checker refuses optimized Python")
    print(f"C371 independent Harper checker: PASS ({check()} assertions)")


if __name__ == "__main__":
    main()
