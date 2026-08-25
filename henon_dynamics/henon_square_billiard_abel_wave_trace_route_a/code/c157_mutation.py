#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C157."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c157_abel_trace_evidence.json"
CHECKER = ROOT / "code/c157_abel_trace_checker.py"


def payload_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def delete_path(data, path):
    target = data
    for key in path[:-1]:
        target = target[key]
    del target[path[-1]]


def main():
    source = json.loads(EVIDENCE.read_text())
    mutations = [
        ("schema", ("schema",), "forged"),
        ("candidate", ("candidate_id",), "HCS-X"),
        ("date", ("evaluation_date",), "2026-08-24"),
        ("scope", ("scope_literal",), "BAD"),
        ("commit", ("source_commit",), "0"*40),
        ("object", ("source_lock", "object"), "torus"),
        ("frequency", ("source_lock", "frequencies"), "wrong"),
        ("trace", ("source_lock", "abel_half_wave_trace"), "wrong"),
        ("clock", ("source_lock", "clock"), "forged clock"),
        ("domain", ("source_lock", "domain"), "Re(s)>=0"),
        ("direction", ("source_lock", "ordered_direction_convention"), "unordered"),
        ("direction_suffix", ("source_lock", "ordered_direction_convention"),
         source["source_lock"]["ordered_direction_convention"] + "; forged suffix"),
        ("cutoff", ("source_lock", "shell_cutoff"), 499),
        ("precision", ("source_lock", "precision"), "float"),
        ("precision_suffix", ("source_lock", "precision"),
         source["source_lock"]["precision"] + "; forged suffix"),
        ("forbidden", ("source_lock", "forbidden_data"), "none"),
        ("source_lock_extra", ("source_lock", "forged"), False),
        ("poisson", ("poisson_theorem", "formula"), "wrong constant"),
        ("transform", ("poisson_theorem", "radial_transform"), "wrong"),
        ("fourier_convention", ("poisson_theorem", "fourier_convention"), "wrong"),
        ("branch", ("poisson_theorem", "branch"), "unspecified"),
        ("branch_suffix", ("poisson_theorem", "branch"),
         source["poisson_theorem"]["branch"] + "; forged suffix"),
        ("convergence", ("poisson_theorem", "absolute_convergence"), "conditional"),
        ("convergence_suffix", ("poisson_theorem", "absolute_convergence"),
         source["poisson_theorem"]["absolute_convergence"] + "; forged suffix"),
        ("proof_route", ("poisson_theorem", "proof_route"), "wrong"),
        ("poisson_extra", ("poisson_theorem", "forged"), False),
        ("weyl", ("geometric_decomposition", "weyl_zero_mode"), "0"),
        ("axis", ("geometric_decomposition", "axis_dual_term"), "wrong"),
        ("boundary", ("geometric_decomposition", "boundary_subtraction"), "0"),
        ("nonaxis", ("geometric_decomposition", "nonaxis_primitive_term"), "wrong"),
        ("nonaxis_suffix", ("geometric_decomposition", "nonaxis_primitive_term"),
         source["geometric_decomposition"]["nonaxis_primitive_term"] + "; forged suffix"),
        ("length", ("geometric_decomposition", "length"), "sqrt"),
        ("multiplicity", ("geometric_decomposition", "multiplicity_rule"), "one sign"),
        ("multiplicity_suffix", ("geometric_decomposition", "multiplicity_rule"),
         source["geometric_decomposition"]["multiplicity_rule"] + "; forged suffix"),
        ("determinant", ("geometric_decomposition", "isolated_orbit_determinant"), True),
        ("geometry_extra", ("geometric_decomposition", "forged"), False),
        ("approach", ("boundary_singularity_theorem", "approach"), "real axis"),
        ("singular_weyl", ("boundary_singularity_theorem", "weyl_zero_mode"), "none"),
        ("nonaxis_branch", ("boundary_singularity_theorem", "nonaxis_branch_locations"), "wrong"),
        ("axis_branch", ("boundary_singularity_theorem", "axis_branch_locations"), "wrong"),
        ("boundary_poles", ("boundary_singularity_theorem", "boundary_subtraction_poles"), "none"),
        ("overlap", ("boundary_singularity_theorem", "overlap_boundary"), "cancel"),
        ("overlap_suffix", ("boundary_singularity_theorem", "overlap_boundary"),
         source["boundary_singularity_theorem"]["overlap_boundary"] + "; forged suffix"),
        ("singularity_type", ("boundary_singularity_theorem", "singularity_type"), "pole"),
        ("singularity_type_suffix", ("boundary_singularity_theorem", "singularity_type"),
         source["boundary_singularity_theorem"]["singularity_type"] + "; forged suffix"),
        ("repetitions", ("boundary_singularity_theorem", "all_repetitions_retained"), False),
        ("exhaustive", ("boundary_singularity_theorem", "branch_locations_exhaust_all_boundary_singularities"), True),
        ("singularity_extra", ("boundary_singularity_theorem", "forged"), False),
        ("primitive_norm", ("primitive_direction_ledger", 10, "primitive_squared_norm"), 1),
        ("primitive_length", ("primitive_direction_ledger", 11, "length_symbol"), "wrong"),
        ("primitive_count", ("primitive_direction_ledger", 12, "ordered_positive_direction_count"), 99),
        ("primitive_direction", ("primitive_direction_ledger", 13, "directions", 0, 0), 99),
        ("shell_norm", ("dual_shell_ledger", 10, "dual_squared_norm"), 1),
        ("shell_count", ("dual_shell_ledger", 11, "ordered_positive_vector_count"), 99),
        ("sign_count", ("dual_shell_ledger", 12, "sign_lifted_dual_multiplicity"), 99),
        ("base_norm", ("dual_shell_ledger", 13, "primitive_repetition_decomposition", 0, "primitive_squared_norm"), 1),
        ("repetition", ("dual_shell_ledger", 14, "primitive_repetition_decomposition", 0, "repetition"), 99),
        ("decomp_mass", ("dual_shell_ledger", 15, "primitive_repetition_decomposition", 0, "primitive_ordered_multiplicity"), 99),
        ("collision_norm", ("collision_sentinel", "first_fourfold_ordered_primitive_squared_norm"), 50),
        ("collision_direction", ("collision_sentinel", "directions", 0, 0), 2),
        ("collision_sign", ("collision_sentinel", "sign_lifted_multiplicity"), 4),
        ("primal_bound", ("numerical_method", "primal_tail_bound"), "none"),
        ("primal_bound_suffix", ("numerical_method", "primal_tail_bound"),
         source["numerical_method"]["primal_tail_bound"] + "; forged suffix"),
        ("dual_acceleration", ("numerical_method", "dual_acceleration"), "none"),
        ("dual_acceleration_suffix", ("numerical_method", "dual_acceleration"),
         source["numerical_method"]["dual_acceleration"] + "; forged suffix"),
        ("complex_remainder", ("numerical_method", "complex_remainder_bound"), "none"),
        ("square_shell_bound", ("numerical_method", "square_shell_bound"), "none"),
        ("dual_bound", ("numerical_method", "dual_tail_bound"), "none"),
        ("dual_bound_suffix", ("numerical_method", "dual_tail_bound"),
         source["numerical_method"]["dual_tail_bound"] + "; forged suffix"),
        ("numerical_extra", ("numerical_method", "forged"), False),
        ("primal_cutoff", ("numerical_method", "sentinels", 0, "primal_box_cutoff"), 1),
        ("dual_cutoff", ("numerical_method", "sentinels", 1, "dual_accelerated_box_cutoff"), 1),
        ("overlap_receipt", ("numerical_method", "sentinels", 0, "intervals_overlap"), False),
        ("sentinel_s", ("numerical_method", "sentinels", 0, "s", "real"), "0.9000000001"),
        ("sentinel_primal_value", ("numerical_method", "sentinels", 0, "primal_value", "real"), "0"),
        ("sentinel_dual_value", ("numerical_method", "sentinels", 1, "dual_value", "imag"), "0"),
        ("sentinel_primal_tail", ("numerical_method", "sentinels", 1, "primal_tail_bound"), "1e-2"),
        ("sentinel_extra", ("numerical_method", "sentinels", 0, "forged"), False),
        ("sentinel_s_extra", ("numerical_method", "sentinels", 0, "s", "forged"), "0"),
        ("sentinel_primal_complex_extra", ("numerical_method", "sentinels", 0, "primal_value", "forged"), "0"),
        ("sentinel_dual_complex_extra", ("numerical_method", "sentinels", 0, "dual_value", "forged"), "0"),
        ("self_adjoint", ("formal_lift", "self_adjoint"), False),
        ("target_operator", ("formal_lift", "target_operator_claimed"), True),
        ("formal_lift_extra", ("formal_lift", "forged"), False),
        ("route_tuple", ("route_a", "tuple", 0), "A1_PASS"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("claim_flag", ("claim_boundary", "euler_factors"), True),
        ("claim_boundary_extra_false", ("claim_boundary", "forged"), False),
        ("extra", ("route_a", "forged"), True),
    ]
    deletions = [
        ("source_lock_delete_clock", ("source_lock", "clock")),
        ("poisson_delete_proof_route", ("poisson_theorem", "proof_route")),
        ("geometry_delete_length", ("geometric_decomposition", "length")),
        ("singularity_delete_overlap", ("boundary_singularity_theorem", "overlap_boundary")),
        ("numerical_delete_dual_bound", ("numerical_method", "dual_tail_bound")),
        ("sentinel_delete_absolute_difference",
         ("numerical_method", "sentinels", 0, "absolute_difference")),
        ("sentinel_s_delete_imag", ("numerical_method", "sentinels", 0, "s", "imag")),
        ("sentinel_primal_complex_delete_real",
         ("numerical_method", "sentinels", 0, "primal_value", "real")),
        ("sentinel_dual_complex_delete_imag",
         ("numerical_method", "sentinels", 0, "dual_value", "imag")),
        ("formal_lift_delete_source", ("formal_lift", "source_derived")),
        ("route_delete_overall", ("route_a", "overall")),
        ("claim_boundary_delete_root_numbers", ("claim_boundary", "root_numbers")),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c157-mutations-") as temporary:
        def require_rejection(name, candidate):
            candidate["payload_sha256"] = payload_hash(candidate)
            output = Path(temporary)/f"{name}.json"
            output.write_text(json.dumps(candidate, sort_keys=True, indent=2)+"\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(output), "--quick"],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)

        for name, path, value in mutations:
            candidate = deepcopy(source)
            set_path(candidate, path, value)
            require_rejection(name, candidate)
        for name, path in deletions:
            candidate = deepcopy(source)
            delete_path(candidate, path)
            require_rejection(name, candidate)
        candidate = deepcopy(source)
        candidate["numerical_method"]["sentinels"].pop()
        require_rejection("sentinel_delete", candidate)
        candidate = deepcopy(source)
        candidate["numerical_method"]["sentinels"].append(
            deepcopy(source["numerical_method"]["sentinels"][0]))
        require_rejection("sentinel_append", candidate)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0"*64
        output = Path(temporary)/"stale.json"
        output.write_text(json.dumps(stale, sort_keys=True, indent=2)+"\n")
        if subprocess.run([sys.executable, str(CHECKER), str(output), "--quick"],
                          capture_output=True, text=True).returncode == 0:
            raise AssertionError("checker accepted stale hash")
    print(json.dumps({
        "status": "C157_MUTATION_PASS", "repaired_hash_rejected": len(rejected),
        "stale_hash_rejected": 1, "total": len(rejected)+1, "names": rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
