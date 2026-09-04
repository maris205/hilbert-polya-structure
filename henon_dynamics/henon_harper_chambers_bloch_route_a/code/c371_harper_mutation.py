#!/usr/bin/env python3
"""Repaired-hash hostile mutations and strict-parser attacks for HCS-C371."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / "results/c371_harper_evidence.json"
YML = ROOT / "evaluations/route_a/HCS-C371/2026-09-04.yaml"
CHECKER = ROOT / "code/c371_harper_checker.py"
spec = importlib.util.spec_from_file_location("c371_independent_checker", CHECKER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repaired(obj):
    value = copy.deepcopy(obj)
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return value


def setpath(obj, path, value):
    cursor = obj
    for item in path[:-1]:
        cursor = cursor[item]
    cursor[path[-1]] = value


def rejected(obj, yaml_path=YML):
    with tempfile.TemporaryDirectory(prefix="c371-mut-") as directory:
        path = Path(directory) / "evidence.json"
        path.write_text(json.dumps(repaired(obj), sort_keys=True, indent=2) + "\n")
        try:
            module.check(path, yaml_path)
        except Exception:
            return True
    return False


def main():
    if sys.flags.optimize:
        raise RuntimeError("C371 mutation lane refuses optimized Python")
    base = json.loads(EV.read_text())
    attacks = [
        (["schema"], "wrong"),
        (["candidate_id"], "HCS-C370"),
        (["obstruction_id"], "HEN-O354"),
        (["evaluation_date"], "2026-09-03"),
        (["source_commit"], "0" * 40),
        (["fixed_epoch"], 1),
        (["fixed_epoch"], 1788480000.0),
        (["scope_literal"], "BROKEN"),
        (["evaluator", "authority"], "wrong"),
        (["evaluator", "version"], "0.1.0"),
        (["evaluator", "sha256"], "0" * 64),
        (["route_a_yaml", "relative_path"], "wrong"),
        (["route_a_yaml", "raw_sha256"], "0" * 64),
        (["route_a_yaml", "semantic_sha256"], "0" * 64),
        (["model", "lattice_operator"], "isotropic only"),
        (["model", "fiber_equation"], "wrong phase"),
        (["model", "bloch_convention"], "stored total_x equals k_x"),
        (["model", "parameter_domain"], "q arbitrary without coprimality"),
        (["theorem_contract", "chambers_identity"], "wrong sign"),
        (["theorem_contract", "spectrum_preimage"], "all real energies"),
        (["theorem_contract", "edge_criterion"], "all gaps open"),
        (["theorem_contract", "edge_fiber_realization"], "edge factors are not fibers"),
        (["theorem_contract", "even_central_contact"], "central gap open"),
        (["theorem_contract", "aubry_duality"], "missing lambda power"),
        (["theorem_contract", "flux_reversal"], "false"),
        (["theorem_contract", "parity"], "always even"),
        (["proof_receipts", "transfer_determinant"], "wrong Bloch phase"),
        (["proof_receipts", "phase_support"], "all Fourier modes"),
        (["proof_receipts", "extreme_coefficients"], "+lambda^q"),
        (["proof_receipts", "spectrum_range"], "discrete phase range"),
        (["proof_receipts", "real_edge_factors"], "complex endpoint factors"),
        (["proof_receipts", "even_central_source"], "finite q<=10 proves all q"),
        (["proof_receipts", "duality_owner"], "target functional equation"),
        (["finite_evidence_role"], "finite samples prove the continuum theorem"),
        (["collision_boundary", "workspace_scan"], "same-batch only"),
        (["collision_boundary", "C15_HEN_O30"], "no earlier Harper block"),
        (["collision_boundary", "C293"], "same operator"),
        (["collision_boundary", "C340"], "same operator"),
        (["collision_boundary", "C356"], "Chern theorem included"),
        (["collision_boundary", "Lamoureux_Mingo_2007"], "no direct precedent"),
        (["collision_boundary", "literature_boundary"], "priority claimed"),
        (["boundary_atlas", 1, "polynomial"], "P(E)=E^2"),
        (["boundary_atlas", 2, "classification"], "all gaps open"),
        (["nonclaims", 0], "all gaps are open"),
        (["references", 0], "bad"),
        (["references", 4], "missing Lamoureux-Mingo DOI"),
        (["route_a", "tuple", 0], "A0_STRONG_ARITHMETIC_RELATION"),
        (["route_a", "overall"], "ROUTE_A_ADVANCES"),
        (["route_a", "route_b_invocation_allowed"], True),
        (["route_a", "route_b_invocation_allowed"], 0),
        (["scope_flags", "claims_target_euler_factors"], True),
        (["scope_flags", "claims_root_number"], True),
        (["scope_flags", "claims_target_zero_match"], True),
        (["scope_flags", "claims_hilbert_polya_operator"], True),
        (["scope_flags", "invokes_route_b"], True),
        (["tolerances", "normalized_numeric_residual"], "1"),
        (["flux_rows", 0, "p"], 2),
        (["flux_rows", 0, "reversal_p"], 1),
        (["flux_rows", 0, "cyclotomic_degree"], 99),
        (["flux_rows", 0, "residue_orbit_sha256"], "0" * 64),
        (["panels", 0, "p"], 2),
        (["panels", 0, "lambda"], "2"),
        (["panels", 0, "polynomial_coefficients_ascending", 1], "0.0"),
        (["panels", 0, "polynomial_sha256"], "0" * 64),
        (["panels", 0, "phase_grid", "pairs"], 1),
        (["panels", 0, "fiber_eigenvalues"], 1),
        (["panels", 0, "phase_rhs_min"], "0"),
        (["panels", 0, "expected_phase_bound"], "0"),
        (["panels", 0, "determinant_normalized_residual_max"], "1"),
        (["panels", 0, "spectrum_overflow_normalized_max"], "1"),
        (["panels", 0, "flux_reversal_coefficient_residual_max"], "1"),
        (["panels", 0, "aubry_duality_coefficient_residual_max"], "1"),
        (["panels", 0, "parity_coefficient_residual_max"], "1"),
        (["panels", 0, "eigenvalue_digest_sha256"], "0" * 64),
    ]
    passed = 0
    for path, value in attacks:
        changed = copy.deepcopy(base)
        setpath(changed, path, value)
        if not rejected(changed):
            raise AssertionError(f"survived repaired mutation {path}")
        passed += 1

    for key in ("flux_rows", "panels", "boundary_atlas"):
        changed = copy.deepcopy(base)
        changed[key].pop()
        if not rejected(changed):
            raise AssertionError(f"survived truncation {key}")
        passed += 1
        changed = copy.deepcopy(base)
        changed[key][0], changed[key][1] = changed[key][1], changed[key][0]
        if not rejected(changed):
            raise AssertionError(f"survived reorder {key}")
        passed += 1

    for path in (
        ("evaluator", "authority"),
        ("theorem_contract", "chambers_identity"),
        ("proof_receipts", "phase_support"),
        ("proof_receipts", "even_central_source"),
        ("collision_boundary", "C15_HEN_O30"),
        ("collision_boundary", "Lamoureux_Mingo_2007"),
        ("scope_flags", "invokes_route_b"),
        ("panels", 0, "eigenvalue_digest_sha256"),
    ):
        changed = copy.deepcopy(base)
        cursor = changed
        for item in path[:-1]:
            cursor = cursor[item]
        del cursor[path[-1]]
        if not rejected(changed):
            raise AssertionError(f"survived deletion {path}")
        passed += 1

    changed = copy.deepcopy(base)
    changed["unexpected"] = 1
    if not rejected(changed):
        raise AssertionError("survived extra evidence key")
    passed += 1
    changed = copy.deepcopy(base)
    changed["panels"][0]["unexpected"] = False
    if not rejected(changed):
        raise AssertionError("survived extra panel key")
    passed += 1

    with tempfile.TemporaryDirectory(prefix="c371-stale-") as directory:
        changed = copy.deepcopy(base)
        changed["candidate_id"] = "bad"
        path = Path(directory) / "stale.json"
        path.write_text(json.dumps(changed))
        try:
            module.check(path, YML)
        except Exception:
            passed += 1
        else:
            raise AssertionError("stale outer hash survived")

    for raw in ('{"a":1,"a":2}', '{"x":NaN}', "[]"):
        with tempfile.TemporaryDirectory(prefix="c371-json-") as directory:
            path = Path(directory) / "bad.json"
            path.write_text(raw)
            try:
                module.check(path, YML)
            except Exception:
                passed += 1
            else:
                raise AssertionError("malformed JSON survived")

    yaml_raw = YML.read_text()
    yaml_changes = [
        ("candidate_id: HCS-C371", "candidate_id: HCS-C370"),
        ("obstruction_id: HEN-O355", "obstruction_id: HEN-O354"),
        ("evaluator_version: 0.2.0", "evaluator_version: 0.1.0"),
        ("evidence_status: PROVED", "evidence_status: STOP_SCOPED"),
        ("evidence_status: STOP_SCOPED", "evidence_status: PROVED"),
        ("route_b_invocation_allowed: false", "route_b_invocation_allowed: true"),
        ("claims_target_zero_match: false", "claims_target_zero_match: true"),
        (
            "strongest_evidence: reduced rational flux organizes exact cyclotomic magnetic translations and finite q-dimensional Bloch fibers",
            "strongest_evidence: altered",
        ),
        (
            "normalization: horizontal hopping one, vertical hopping lambda, Landau gauge phase exp of two pi i p m over q, and total horizontal Bloch multiplier exp of i q k_x",
            "normalization: wrong total phase",
        ),
        (
            "DOI:10.1090/S0002-9939-07-08830-2",
            "DOI:10.1090/removed",
        ),
    ]
    for old, new in yaml_changes:
        with tempfile.TemporaryDirectory(prefix="c371-yaml-") as directory:
            path = Path(directory) / "bad.yaml"
            path.write_text(yaml_raw.replace(old, new, 1))
            try:
                module.check(EV, path)
            except Exception:
                passed += 1
            else:
                raise AssertionError(f"YAML mutation survived: {old}")
    for extra in ("\ncandidate_id: DUPLICATE\n", "\nx: &a 1\ny: *a\n", "\n? [a,b]\n: c\n"):
        with tempfile.TemporaryDirectory(prefix="c371-yaml-") as directory:
            path = Path(directory) / "bad.yaml"
            path.write_text(yaml_raw + extra)
            try:
                module.check(EV, path)
            except Exception:
                passed += 1
            else:
                raise AssertionError("malformed YAML survived")

    print(f"C371 hostile mutation suite: PASS ({passed} attacks)")


if __name__ == "__main__":
    main()
