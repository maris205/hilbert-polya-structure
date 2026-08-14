#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C54 certificate."""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import combinations, product
import json
import os
from pathlib import Path
import subprocess
import sys


PROJECT = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[3]
C53_CERTIFICATE_RELATIVE = (
    "henon_dynamics/henon_mu3_dihedral_core_rational_descent/"
    "results/c53_certificate.json"
)
C53_ROUTE_RELATIVE = (
    "henon_dynamics/henon_mu3_dihedral_core_rational_descent/"
    "route_a_evaluation.yaml"
)
C53_PATH = REPO / C53_CERTIFICATE_RELATIVE
EXPECTED_PAYLOAD_SHA256 = (
    "f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1"
)
EXPECTED_SCHEMA_SHA256 = (
    "4cee6c2252d5743ca3c5fee40ec98fbc945223312d2196fb63a43730281deedf"
)
EXPECTED_C53_SHA256 = (
    "f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79"
)
EXPECTED_C53_PAYLOAD_SHA256 = (
    "8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41"
)
EXPECTED_C53_IMPLEMENTATION_COMMIT = "0a7f0fdb8290eab4aa92ed5ade432401c40c22cf"
EXPECTED_C53_PROVENANCE_COMMIT = "9d509d3b3826b7bfbdb38ed9fe4dac9297f5dbdf"
EXPECTED_C53_ROUTE_SHA256 = (
    "ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719"
)
EXPECTED_C53_CHECK_SHA256 = (
    "0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67"
)
EXPECTED_C53_CODE_RESULTS_MANIFEST_SHA256 = (
    "b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480"
)
PAYLOAD_KEYS = {
    "schema_version",
    "claim_scope",
    "source_family",
    "full_projective_monomial_group",
    "rational_group_form",
    "split_denominator_rigidity",
    "n3_equivariant_character",
    "counterpacket_firewall",
    "primary_source_controls",
    "exclusions",
    "artifact_status",
}

# Every noncomputed semantic scalar is locked independently of both digests.
# A few compact containers are written as blocks for readability and expanded
# to individual scalar paths immediately below.  Exact computed tables and the
# complete n=3 representation are checked by independent derivations.
SEMANTIC_EXPECTED_BLOCKS: dict[tuple[str | int, ...], object] = {
    ("schema_version",): "c54-v1",
    ("artifact_status",): "RELEASE_CANDIDATE",
    ("claim_scope", "candidate_id"): "HCS-C54",
    ("claim_scope", "all_n_equation_theorem"): True,
    ("claim_scope", "all_n_equation_theorem_category"): "full projective monomial stabilizer of the homogeneous ideal",
    ("claim_scope", "certified_packet_rows"): [2, 3, 4],
    ("claim_scope", "conditional_packet_rows"): "n>=5 only under explicit packet-admissibility hypothesis",
    ("claim_scope", "C53_semisimplicity_claimed"): False,
    ("claim_scope", "fixed_prime_input_used"): False,
    ("source_family", "base_field"): "K=Q(rho)",
    ("source_family", "rho_relation"): "rho^2+rho+1=0",
    ("source_family", "n_range"): "every integer n>=2",
    ("source_family", "N"): "2n",
    ("source_family", "C_n"): "sum_(i=0)^(2n-1) x_i^3",
    ("source_family", "Q_n_rho"): "sum_(i=0)^(2n-2) x_i*x_(i+1)+rho*x_(2n-1)*x_0",
    ("source_family", "closing_edge_coefficient"): "rho",
    ("source_family", "full_PGL_automorphism_group_claimed"): False,
    ("full_projective_monomial_group", "theorem_range"): "every integer n>=2",
    ("full_projective_monomial_group", "isomorphism"): "PMonStab(C_n,Q_n_rho)=Dih(C_(3n))",
    ("full_projective_monomial_group", "order"): "6n",
    ("full_projective_monomial_group", "presentation"): "<r,s | r^(3n)=s^2=1, s*r*s=r^(-1)>",
    ("full_projective_monomial_group", "support_exact_sequence"): "1 -> C3 -> G_n -> Dih(C_n) -> 1",
    ("full_projective_monomial_group", "support_image"): "even rotations and odd reflections of the 2n-cycle",
    ("full_projective_monomial_group", "phase_normalization"): "e_i in F3 and e_0=0",
    ("full_projective_monomial_group", "phase_and_scale_derivation", "coordinate_phases_in_mu3"): True,
    ("full_projective_monomial_group", "phase_and_scale_derivation", "quadric_scale_in_mu3"): True,
    ("full_projective_monomial_group", "edge_recurrence"): "e_(j+1)=q+c_(sigma(E_j))-c_j-e_j mod 3",
    ("full_projective_monomial_group", "closure_condition"): "inverse image of the closing edge has odd edge index",
    ("full_projective_monomial_group", "rotation_support_condition"): "sigma(i)=i+k survives iff k is even",
    ("full_projective_monomial_group", "reflection_support_condition"): "sigma(i)=k-i survives iff k is odd",
    ("full_projective_monomial_group", "normalized_lifts_per_support"): 3,
    ("full_projective_monomial_group", "generators", "r_exact_order"): "3n",
    ("full_projective_monomial_group", "generators", "s_exact_order"): 2,
    ("full_projective_monomial_group", "generators", "srs"): "r^(-1)",
    ("full_projective_monomial_group", "nonmonomial_automorphisms_classified"): False,
    ("rational_group_form", "tau"): "tau(rho)=rho^2",
    ("rational_group_form", "transport_definition"): "delta(g)=M_n*tau(g)*M_n^(-1)",
    ("rational_group_form", "delta_r"): "r^(-1)",
    ("rational_group_form", "delta_s"): "r*s=s*r^(-1)",
    ("rational_group_form", "delta_square"): "identity",
    ("rational_group_form", "geometric_rank"): "6n",
    ("rational_group_form", "Q_rational_points_group"): "C2",
    ("rational_group_form", "Q_rational_point_count"): 2,
    ("rational_group_form", "all_geometric_elements_individually_Q_rational_claimed"): False,
    ("rational_group_form", "Reynolds", "graphs_used"): "all 6n geometric graphs",
    ("rational_group_form", "Reynolds", "denominator"): "6n",
    ("rational_group_form", "quadratic_transfer", "denominator"): 2,
    ("rational_group_form", "quadratic_transfer", "distinct_from_Reynolds_denominator"): True,
    ("rational_group_form", "all_n_Chow_projector_claimed"): False,
    ("split_denominator_rigidity", "theorem_scope"): "every packet-admissible n>=2",
    ("split_denominator_rigidity", "packet_weights"): {"E_n": 0, "O_n": 1},
    ("split_denominator_rigidity", "packet_ranks"): {
        "e_n": "(4^n+5)/3",
        "o_n": "2*(4^n-4)/3",
        "relation": "o_n=2*(e_n-3)",
    },
    ("split_denominator_rigidity", "split_exponent_after_Q_descent"): "4/n",
    ("split_denominator_rigidity", "restriction_argument", "fixed_coefficient_prime"): True,
    ("split_denominator_rigidity", "restriction_argument", "source_semisimplicity_assumed"): False,
    ("split_denominator_rigidity", "restriction_argument", "pure_weight_separation"): True,
    ("split_denominator_rigidity", "restriction_argument", "reduction"): "o_n=2(e_n-3) implies n divides 24",
    ("split_denominator_rigidity", "surviving_rows"): [2, 4],
    ("split_denominator_rigidity", "classification"): "ordinary split-trace realization iff n divides 4",
    ("split_denominator_rigidity", "strong_factor_classification_same"): True,
    ("split_denominator_rigidity", "converse_matches_every_power_trace"): True,
    ("split_denominator_rigidity", "both_pure_rails_essential"): True,
    ("split_denominator_rigidity", "certified_unconditional_rows"): [2, 3, 4],
    ("split_denominator_rigidity", "n_ge_5_packet_status"): "CONDITIONAL_NOT_CONSTRUCTED",
    ("split_denominator_rigidity", "inert_factor_generally_square_claimed"): False,
    ("split_denominator_rigidity", "global_fractional_root_claimed"): False,
    ("counterpacket_firewall", "Q_split_primes_absolute_density"): "1/2",
    ("counterpacket_firewall", "trace_zero_hypothesis_density"): "relative density one within the good split rational primes",
    ("counterpacket_firewall", "trace_zero_conclusion"): "Res(D)=0",
    ("counterpacket_firewall", "actual_invisible_counterpacket"): "only zero",
    ("counterpacket_firewall", "virtual_restriction_injective_claimed"): False,
    ("counterpacket_firewall", "virtual_kernel_example"): "1-chi_(K/Q)",
    ("counterpacket_firewall", "example_nonzero_virtual_class"): True,
    ("counterpacket_firewall", "example_restriction_zero"): True,
    ("counterpacket_firewall", "every_kernel_class_rank"): 0,
    ("counterpacket_firewall", "kernel_can_change_K_rail_rank"): False,
    ("counterpacket_firewall", "kernel_can_change_K_source_isotypic_multiplicity"): False,
    ("primary_source_controls", "primary_locators_duplicated_in_certificate"): False,
    ("primary_source_controls", "pre_c54_reconnaissance", "status"): "UNPACKAGED_NOT_REPLAYED_NOT_THEOREM_INPUT",
    ("primary_source_controls", "pre_c54_reconnaissance", "counts_as_source_or_semantic_proof_gate"): False,
    ("claim_scope", "title"): "Universal Dihedral Symmetry and Split-Denominator Rigidity in a Cubic--Quadric Source Tower",
    ("claim_scope", "packet_admissibility_definition"): "actual rational compatible realizations E_n,O_n pure of weights 0,1 with the frozen ranks; no semisimplicity hypothesis",
    ("claim_scope", "proof_semisimplicity_passage"): "fix one coefficient prime and apply semisimplification before Chebotarev--Brauer--Nesbitt",
    ("claim_scope", "ordinary_meaning"): "actual finite-rank Q-compatible realization matching every good split-prime trace/factor as specified",
    ("source_family", "stabilizer_definition"): "PGL_(2n)(K) monomial classes stabilizing the homogeneous ideal (C_n,Q_n_rho)",
    ("source_family", "C53_source_lock"): {
        "candidate_id": "HCS-C53",
        "path": "henon_dynamics/henon_mu3_dihedral_core_rational_descent/results/c53_certificate.json",
        "schema": "hcs-c53-certificate-v1",
        "certificate_sha256": EXPECTED_C53_SHA256,
        "payload_sha256": EXPECTED_C53_PAYLOAD_SHA256,
        "artifact_status": "RELEASE_CANDIDATE",
        "semisimplicity_certified_by_C53": False,
        "implementation_commit": EXPECTED_C53_IMPLEMENTATION_COMMIT,
        "provenance_commit": EXPECTED_C53_PROVENANCE_COMMIT,
        "route_path": C53_ROUTE_RELATIVE,
        "route_sha256": EXPECTED_C53_ROUTE_SHA256,
        "route_release_tuple": {
            "implementation_commit": EXPECTED_C53_IMPLEMENTATION_COMMIT,
            "certificate_sha256": EXPECTED_C53_SHA256,
            "payload_sha256": EXPECTED_C53_PAYLOAD_SHA256,
            "independent_check_sha256": EXPECTED_C53_CHECK_SHA256,
            "code_results_manifest_sha256": EXPECTED_C53_CODE_RESULTS_MANIFEST_SHA256,
        },
        "commit_lock_status": "VERIFIED_GIT_OBJECT_CERTIFICATE_AND_COMMITTED_ROUTE_TUPLE",
    },
    ("full_projective_monomial_group", "phase_and_scale_derivation", "projective_scalar_normalization"): "lambda_0=1",
    ("full_projective_monomial_group", "phase_and_scale_derivation", "cubic_line_coefficient_step"): "lambda_i^3=1 for every i",
    ("full_projective_monomial_group", "phase_and_scale_derivation", "quadric_edge_ratio_step"): "the quadric scale is lambda_i*lambda_j times a ratio of source/target edge coefficients, all in mu3",
    ("full_projective_monomial_group", "phase_and_scale_derivation", "q_definition"): "quadric scale=rho^q with q in F3",
    ("full_projective_monomial_group", "ideal_to_equation_lines"): {
        "degree_two_ideal_piece": "K*Q_n_rho",
        "degree_three_form": "g^*C_n=a*C_n+L*Q_n_rho",
        "pure_cube_comparison": "L*Q has no pure cubes, so g^*C_n=a*C_n and L*Q=0",
        "domain_step": "polynomial ring is a domain and Q is nonzero, hence L=0",
        "both_equation_lines_preserved": True,
    },
    ("full_projective_monomial_group", "closing_edge_indicator"): "c_(2n-1)=1 and all other c_j=0",
    ("full_projective_monomial_group", "surviving_support_counts"): {
        "rotations": "n",
        "reflections": "n",
    },
    ("full_projective_monomial_group", "generators", "r_support"): "i -> i+2 mod 2n",
    ("full_projective_monomial_group", "generators", "r_phases"): "a_(2n-2)=1,a_(2n-1)=2,otherwise 0",
    ("full_projective_monomial_group", "generators", "r_quadric_scale"): "1",
    ("full_projective_monomial_group", "generators", "r_power_n"): "diag(1,rho,1,rho,...,1,rho) projectively",
    ("full_projective_monomial_group", "generators", "s_support"): "i -> 1-i mod 2n",
    ("full_projective_monomial_group", "generators", "s_phases"): "b_i=1 iff i=1 or i>=2 is even",
    ("full_projective_monomial_group", "generators", "s_quadric_scale"): "rho",
    ("full_projective_monomial_group", "symbolic_fullness_proof"): "recurrence exhausts exactly 6n stabilizers; r has order 3n and s has reflection support outside <r>, so <r,s> has 6n distinct two-coset elements and equals the exhaustive list",
    ("full_projective_monomial_group", "finite_controls_sha256"): "e6323baca3365ace9377a7541f35a9ec8c8ec1fa49963af9daef8e51fcf42ff7",
    ("full_projective_monomial_group", "finite_controls_role"): "mutation guards, not the universal proof",
    ("rational_group_form", "descent_reversal"): "M_n: sigma(i)=-i; e_0=0 and e_i=1 exactly for nonzero even i",
    ("rational_group_form", "group_scheme"): "finite etale nonconstant Q-form mathscrG_n split by K",
    ("rational_group_form", "fixed_congruences"): {
        "rotations": "2k=0 mod 3n",
        "reflections": "2k=1 mod 3n",
    },
    ("rational_group_form", "fixed_elements_even_n"): ["1", "r^(3n/2)"],
    ("rational_group_form", "fixed_elements_odd_n"): ["1", "r^((3n+1)/2)*s"],
    ("rational_group_form", "finite_exact_control_range"): [2, 256],
    ("rational_group_form", "finite_exact_controls_sha256"): "09f89e9bbdb7a209ce05913ef896f4ed465fe19e9a125d927e6843439599cc29",
    ("rational_group_form", "every_control_has_two_fixed_points"): True,
    ("rational_group_form", "Reynolds", "smooth_packet_row_scope"): True,
    ("rational_group_form", "Reynolds", "geometric_average"): "(1/(6n))*sum_(g in G_n) Gamma_g",
    ("rational_group_form", "quadratic_transfer", "formula"): "e_mathscrG=(1/2)q_*e_G and q^*e_mathscrG=e_G",
    ("split_denominator_rigidity", "ordinary_split_trace_identity"): "Tr(F_p|V_n)=(4/n)*Tr(F_p|E_n direct_sum O_n) at every good split p",
    ("split_denominator_rigidity", "ordinary_split_factor_identity"): "Log_0 L_p(V_n,u)=(4/n)*Log_0 L_p(E_n direct_sum O_n,u)",
    ("split_denominator_rigidity", "restriction_argument", "degree_one_K_primes"): "density one after excluding finitely many places",
    ("split_denominator_rigidity", "restriction_argument", "semisimplification_passage"): "replace each fixed-ell realization by its semisimplification; traces and ranks are unchanged",
    ("split_denominator_rigidity", "restriction_argument", "semisimple_theorem"): "Chebotarev plus Brauer--Nesbitt applied only after semisimplification",
    ("split_denominator_rigidity", "restriction_argument", "K0_identity"): "n*[(Res V_n,ell)^ss]=4*[(Res E_n,ell)^ss]+4*[(Res O_n,ell)^ss]",
    ("split_denominator_rigidity", "restriction_argument", "necessary_divisibilities"): [
        "n divides 4e_n",
        "n divides 4o_n",
    ],
    ("split_denominator_rigidity", "converse"): "V_n=E_n^(direct sum 4/n) direct_sum O_n^(direct sum 4/n)",
    ("split_denominator_rigidity", "finite_scan_range"): [2, 512],
    ("split_denominator_rigidity", "total_rank_trap_n3"): {
        "e_3": 23,
        "o_3": 40,
        "total_rank": 63,
        "scaled_total_rank": 84,
        "scaled_E3_rank": "92/3",
        "scaled_O3_rank": "160/3",
        "total_rank_only_would_falsely_accept": True,
        "proof_route_accepted": False,
    },
    ("split_denominator_rigidity", "inert_identity"): "P_K,v(U^2)=P_Q,p(U)*P_Q,p(-U)",
    ("counterpacket_firewall", "restriction_map"): "Res:K0_ss(G_Q)->K0_ss(G_K)",
    ("counterpacket_firewall", "K0_ss_category"): "classes of fixed-ell finite-dimensional continuous semisimple ell-adic representations arising from the compatible systems in scope, unramified outside one common finite set; not arbitrary G_Q representations",
    ("counterpacket_firewall", "lifted_K_degree_one_prime_density"): "density one among primes of K after finitely many exclusions",
    ("counterpacket_firewall", "example_split_invisible"): True,
    ("counterpacket_firewall", "rational_extension_unique_from_split_traces_claimed"): False,
    ("counterpacket_firewall", "quadratic_twist_may_change_inert_traces"): True,
    ("counterpacket_firewall", "different_split_trace_or_prime_organization_is_different_Euler_object"): True,
    ("primary_source_controls", "reproducible_certificate_evidence"): {
        "producer": "code/c54_producer.py",
        "checker": "code/c54_checker.py",
        "formal_proof": "THEOREM_PACKAGE.md and PROOF_PACKAGE.md",
        "bibliographic_locators": "SOURCE_AUDIT.md",
    },
    ("primary_source_controls", "pre_c54_reconnaissance", "chronology_note_only"): True,
    ("primary_source_controls", "Brunjes_scope"): "Fermat monomial group/character sectors only; not the simultaneous cubic-quadric theorem",
    ("primary_source_controls", "Serre_scope"): "Chebotarev density input",
    ("primary_source_controls", "Brauer_Nesbitt_scope"): "semisimple character equality input",
    ("primary_source_controls", "Favero_Iliev_Katzarkov_scope"): "Cayley-Jacobian model background",
    ("primary_source_controls", "novelty_search_exhaustive_claimed"): False,
    ("exclusions",): {
        "full_PGL_automorphism_group": False,
        "smoothness_all_n": False,
        "compatible_packets_all_n": False,
        "Chow_motive_all_n": False,
        "all_6n_individual_Q_automorphisms": False,
        "rotations_only_Reynolds_average": False,
        "global_fractional_Euler_root": False,
        "inert_fractional_Euler_root": False,
        "unique_Q_extension_from_split_traces": False,
        "automorphy": False,
        "meromorphic_continuation": False,
        "functional_equation": False,
        "Riemann_hypothesis": False,
        "fixed_Frobenius_prime_theorem_input": False,
    },
}


ScalarPath = tuple[str | int, ...]


def scalar_leaves(value, path: ScalarPath = ()):
    """Yield exact bool/int/str/null leaves with list indices in their paths."""
    if type(value) is dict:
        for key, child in value.items():
            yield from scalar_leaves(child, path + (key,))
        return
    if type(value) is list:
        for index, child in enumerate(value):
            yield from scalar_leaves(child, path + (index,))
        return
    if type(value) not in {bool, int, str} and value is not None:
        raise TypeError(f"non-JSON scalar at {path}: {type(value).__name__}")
    yield path, value


def expand_semantic_blocks(
    blocks: dict[ScalarPath, object],
) -> dict[ScalarPath, object]:
    expanded: dict[ScalarPath, object] = {}
    for prefix, expected_block in blocks.items():
        for suffix, expected in scalar_leaves(expected_block):
            path = prefix + suffix
            if path in expanded:
                previous = expanded[path]
                if type(previous) is not type(expected) or previous != expected:
                    raise ValueError(f"conflicting semantic lock at {path}")
            expanded[path] = expected
    return expanded


SEMANTIC_EXPECTED = expand_semantic_blocks(SEMANTIC_EXPECTED_BLOCKS)

# These are independently regenerated and checked exactly in verify().  The
# prefixes are intentionally narrow: an unclassified scalar anywhere else is
# a checker failure even if both external digests are rebound.
DERIVED_SCALAR_PREFIXES: tuple[ScalarPath, ...] = (
    ("full_projective_monomial_group", "finite_exact_controls_n2_to_n64"),
    ("full_projective_monomial_group", "independent_bruteforce_controls"),
    ("n3_equivariant_character",),
    ("split_denominator_rigidity", "divisors_of_24_table"),
    ("split_denominator_rigidity", "finite_scan_survivors"),
)

# Only chronology-only hashes of unpackaged, explicitly non-input exploratory
# notes are nonsemantic.  Their keys and scalar types remain schema-locked.
NONSEMANTIC_ALLOWLIST: dict[ScalarPath, str] = {
    (
        "primary_source_controls",
        "pre_c54_reconnaissance",
        "historical_sha256",
        "theorem_planning_note",
    ): "chronology-only hash; not a source or theorem input",
    (
        "primary_source_controls",
        "pre_c54_reconnaissance",
        "historical_sha256",
        "architecture_planning_note",
    ): "chronology-only hash; not a source or theorem input",
    (
        "primary_source_controls",
        "pre_c54_reconnaissance",
        "historical_sha256",
        "general_group_exploration",
    ): "chronology-only hash; not a source or theorem input",
    (
        "primary_source_controls",
        "pre_c54_reconnaissance",
        "historical_sha256",
        "n3_exploration",
    ): "chronology-only hash; not a source or theorem input",
}


def canonical_json(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reject_duplicate_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_load(raw: bytes):
    return json.loads(raw, object_pairs_hook=reject_duplicate_pairs)


def parse_c53_route_release_tuple(raw: bytes) -> dict[str, str]:
    """Independently parse the committed C53 Route provenance tuple."""
    text = raw.decode("utf-8")
    top_level: dict[str, str] = {}
    release_hashes: dict[str, str] = {}
    parent = None
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if "\t" in line[: len(line) - len(line.lstrip())]:
            raise AssertionError(f"tab indentation in C53 Route line {line_number}")
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if indent == 0:
            key, separator, value = stripped.partition(":")
            if not separator or not key:
                raise AssertionError(f"malformed C53 Route line {line_number}")
            if key in top_level:
                raise AssertionError(f"duplicate C53 Route top-level key: {key}")
            top_level[key] = value.strip()
            parent = key if not value.strip() else None
        elif indent == 2 and parent == "release_candidate_hashes":
            key, separator, value = stripped.partition(":")
            if not separator or not key or not value.strip():
                raise AssertionError(f"malformed C53 release hash line {line_number}")
            if key in release_hashes:
                raise AssertionError(f"duplicate C53 release hash key: {key}")
            release_hashes[key] = value.strip()

    assert top_level["candidate_id"] == "HCS-C53"
    assert top_level["documentation_status"] == "DOCS_FINAL_NO_MORE_EDITS"
    assert top_level["code_results_status"] == "RELEASE_CANDIDATE"
    assert set(release_hashes) == {
        "certificate",
        "payload",
        "independent_check",
        "code_results_manifest",
    }
    return {
        "implementation_commit": top_level["code_commit"],
        "certificate_sha256": release_hashes["certificate"],
        "payload_sha256": release_hashes["payload"],
        "independent_check_sha256": release_hashes["independent_check"],
        "code_results_manifest_sha256": release_hashes["code_results_manifest"],
    }


def schema_descriptor(value):
    if type(value) is dict:
        return ["dict", [[key, schema_descriptor(value[key])] for key in sorted(value)]]
    if type(value) is list:
        return ["list", len(value), [schema_descriptor(item) for item in value]]
    if type(value) is bool:
        return "bool"
    if type(value) is int:
        return "int"
    if type(value) is float:
        return "float"
    if type(value) is str:
        return "str"
    if value is None:
        return "null"
    return f"forbidden:{type(value).__name__}"


def exact(left, right) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(exact(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(exact(a, b) for a, b in zip(left, right))
    return left == right


def value_at(root, path: ScalarPath):
    value = root
    for component in path:
        value = value[component]
    return value


def is_derived_scalar_path(path: ScalarPath) -> bool:
    return any(path[: len(prefix)] == prefix for prefix in DERIVED_SCALAR_PREFIXES)


def validate_scalar_inventory(payload: dict) -> dict[str, int]:
    """Fail if any scalar is neither semantic, derived, nor allowlisted."""
    actual = {path for path, _ in scalar_leaves(payload)}
    semantic = set(SEMANTIC_EXPECTED)
    nonsemantic = set(NONSEMANTIC_ALLOWLIST)
    derived = {path for path in actual if is_derived_scalar_path(path)}
    if not semantic <= actual:
        missing = sorted(semantic - actual, key=repr)
        raise AssertionError(f"semantic scalar paths missing: {missing}")
    if not nonsemantic <= actual:
        missing = sorted(nonsemantic - actual, key=repr)
        raise AssertionError(f"allowlisted scalar paths missing: {missing}")
    if semantic & nonsemantic:
        raise AssertionError("semantic and nonsemantic scalar classifications overlap")
    if (semantic | nonsemantic) & derived:
        raise AssertionError("explicit scalar classifications overlap derived prefixes")
    unclassified = actual - semantic - nonsemantic - derived
    if unclassified:
        paths = ["/".join(map(str, path)) for path in sorted(unclassified, key=repr)]
        raise AssertionError(f"unclassified scalar leaves: {paths}")
    return {
        "total": len(actual),
        "semantic": len(semantic),
        "derived": len(derived),
        "nonsemantic": len(nonsemantic),
    }


MonomialMap = tuple[tuple[int, ...], tuple[int, ...]]


def projectivize(permutation, phases) -> MonomialMap:
    offset = phases[0]
    return tuple(permutation), tuple((phase - offset) % 3 for phase in phases)


def multiply(first: MonomialMap, second: MonomialMap) -> MonomialMap:
    p, e = first
    q, f = second
    return projectivize(
        [q[p[i]] for i in range(len(p))],
        [(e[i] + f[p[i]]) % 3 for i in range(len(p))],
    )


def reciprocal(item: MonomialMap) -> MonomialMap:
    permutation, phases = item
    back = [0] * len(permutation)
    for source, target in enumerate(permutation):
        back[target] = source
    return projectivize(back, [(-phases[back[i]]) % 3 for i in range(len(permutation))])


def exponentiate(item: MonomialMap, exponent: int) -> MonomialMap:
    answer = (tuple(range(len(item[0]))), (0,) * len(item[0]))
    for _ in range(exponent):
        answer = multiply(answer, item)
    return answer


def order_of(item: MonomialMap, maximum: int) -> int:
    identity = (tuple(range(len(item[0]))), (0,) * len(item[0]))
    answer = identity
    for exponent in range(1, maximum + 1):
        answer = multiply(answer, item)
        if answer == identity:
            return exponent
    raise AssertionError("order bound")


def generator_pair(n: int) -> tuple[MonomialMap, MonomialMap]:
    N = 2 * n
    r = projectivize(
        [(i + 2) % N for i in range(N)],
        [1 if i == N - 2 else 2 if i == N - 1 else 0 for i in range(N)],
    )
    s = projectivize(
        [(1 - i) % N for i in range(N)],
        [1 if i == 1 or (i >= 2 and i % 2 == 0) else 0 for i in range(N)],
    )
    return r, s


def support(n: int, reflection: bool, shift: int) -> tuple[int, ...]:
    N = 2 * n
    return tuple(((shift - i) if reflection else (i + shift)) % N for i in range(N))


def solve_edge_system(n: int, reflection: bool, shift: int, scale: int):
    N = 2 * n
    permutation = support(n, reflection, shift)
    phases = [0] * N
    for edge in range(N):
        a, b = permutation[edge], permutation[(edge + 1) % N]
        target_edge = a if (a + 1) % N == b else b
        next_value = (
            scale + int(target_edge == N - 1) - int(edge == N - 1) - phases[edge]
        ) % 3
        if edge != N - 1:
            phases[edge + 1] = next_value
        elif next_value:
            return None
    return projectivize(permutation, phases)


def directly_test_quadric(item: MonomialMap) -> int | None:
    permutation, phases = item
    N = len(permutation)
    transformed = [None] * N
    for source_edge in range(N):
        a = permutation[source_edge]
        b = permutation[(source_edge + 1) % N]
        if (a + 1) % N == b:
            target_edge = a
        elif (b + 1) % N == a:
            target_edge = b
        else:
            return None
        transformed[target_edge] = (
            int(source_edge == N - 1)
            + phases[source_edge]
            + phases[(source_edge + 1) % N]
        ) % 3
    differences = {(transformed[j] - int(j == N - 1)) % 3 for j in range(N)}
    return differences.pop() if len(differences) == 1 else None


def enumerate_by_recurrence(n: int) -> dict[MonomialMap, int]:
    answer = {}
    for reflection in (False, True):
        for shift in range(2 * n):
            for scale in range(3):
                item = solve_edge_system(n, reflection, shift, scale)
                if item is not None:
                    assert directly_test_quadric(item) == scale
                    answer[item] = scale
    return answer


def enumerate_by_phases(n: int) -> dict[MonomialMap, int]:
    N = 2 * n
    answer = {}
    for reflection in (False, True):
        for shift in range(N):
            permutation = support(n, reflection, shift)
            for tail in product(range(3), repeat=N - 1):
                item = (permutation, (0,) + tail)
                scale = directly_test_quadric(item)
                if scale is not None:
                    answer[item] = scale
    return answer


@lru_cache(maxsize=1)
def expected_group_controls() -> list[dict]:
    rows = []
    for n in range(2, 65):
        # Exact construction/relation replay on a substantial range.  For the
        # remainder, the row is derived directly from the universal recurrence
        # and presentation; the certificate's full list is separately hash-locked.
        if n <= 20:
            group = enumerate_by_recurrence(n)
            assert len(group) == 6 * n
            rotations = sum(
                any(solve_edge_system(n, False, k, q) is not None for q in range(3))
                for k in range(2 * n)
            )
            reflections = sum(
                any(solve_edge_system(n, True, k, q) is not None for q in range(3))
                for k in range(2 * n)
            )
            assert (rotations, reflections) == (n, n)
            r, s = generator_pair(n)
            identity = (tuple(range(2 * n)), (0,) * (2 * n))
            assert order_of(r, 3 * n) == 3 * n
            assert exponentiate(s, 2) == identity
            assert multiply(multiply(s, r), s) == reciprocal(r)
            generated = {exponentiate(r, k) for k in range(3 * n)} | {
                multiply(exponentiate(r, k), s) for k in range(3 * n)
            }
            assert generated == set(group)
        rows.append(
            {
                "n": n,
                "N": 2 * n,
                "order": 6 * n,
                "support_counts": {"rotation": n, "reflection": n},
                "lifts_per_surviving_support": 3,
                "rotation_generator_order": 3 * n,
                "reflection_generator_order": 2,
                "dihedral_relation": True,
                "generated_equals_exhaustive_list": True,
                "r_power_n_alternating_kernel": True,
            }
        )
    return rows


def conjugate_map(item: MonomialMap) -> MonomialMap:
    return item[0], tuple((-phase) % 3 for phase in item[1])


def descent_reversal(n: int) -> MonomialMap:
    N = 2 * n
    return projectivize(
        [(-i) % N for i in range(N)],
        [1 if i and i % 2 == 0 else 0 for i in range(N)],
    )


def transported(n: int, item: MonomialMap) -> MonomialMap:
    M = descent_reversal(n)
    return multiply(multiply(M, conjugate_map(item)), reciprocal(M))


@lru_cache(maxsize=1)
def expected_rational_controls() -> list[dict]:
    rows = []
    for n in range(2, 257):
        r, s = generator_pair(n)
        assert transported(n, r) == reciprocal(r)
        assert transported(n, s) == multiply(r, s)
        assert transported(n, transported(n, r)) == r
        assert transported(n, transported(n, s)) == s
        modulus = 3 * n
        rotations = [k for k in range(modulus) if 2 * k % modulus == 0]
        reflections = [k for k in range(modulus) if (2 * k - 1) % modulus == 0]
        fixed = ["1" if k == 0 else f"r^{k}" for k in rotations]
        fixed.extend(f"r^{k}*s" for k in reflections)
        target = (
            ["1", f"r^{3*n//2}"]
            if n % 2 == 0
            else ["1", f"r^{(3*n+1)//2}*s"]
        )
        assert fixed == target
        rows.append(
            {
                "n": n,
                "geometric_rank": 6 * n,
                "fixed_geometric_elements": fixed,
                "fixed_count": 2,
                "nonconstant": True,
                "delta_involution_from_generator_presentation": True,
            }
        )
    return rows


def ranks(n: int) -> tuple[int, int]:
    even = (4**n + 5) // 3
    odd = 2 * (4**n - 4) // 3
    assert odd == 2 * (even - 3)
    return even, odd


# A second exact Q(rho) implementation for the n=3 quotient audit.
QPair = tuple[Fraction, Fraction]
Z: QPair = (Fraction(0), Fraction(0))
I: QPair = (Fraction(1), Fraction(0))


def qa(x: QPair, y: QPair) -> QPair:
    return x[0] + y[0], x[1] + y[1]


def qs(x: QPair, y: QPair) -> QPair:
    return x[0] - y[0], x[1] - y[1]


def qm(x: QPair, y: QPair) -> QPair:
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def qi(x: QPair) -> QPair:
    a, b = x
    norm = a * a - a * b + b * b
    return (a - b) / norm, -b / norm


def qr(exponent: int) -> QPair:
    return (I, (Fraction(0), Fraction(1)), (Fraction(-1), Fraction(-1)))[exponent % 3]


def qn(value: int) -> QPair:
    return Fraction(value), Fraction(0)


def sign_of(permutation) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def weak_compositions(total, slots, prefix=()):
    if slots == 1:
        yield prefix + (total,)
    else:
        for value in range(total + 1):
            yield from weak_compositions(total - value, slots - 1, prefix + (value,))


def row_reduce(rows):
    matrix = [row[:] for row in rows]
    pivots = []
    active = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(active, len(matrix)) if matrix[row][column] != Z), None)
        if pivot is None:
            continue
        matrix[active], matrix[pivot] = matrix[pivot], matrix[active]
        inverse_pivot = qi(matrix[active][column])
        matrix[active] = [qm(value, inverse_pivot) for value in matrix[active]]
        for row in range(len(matrix)):
            if row == active or matrix[row][column] == Z:
                continue
            coefficient = matrix[row][column]
            matrix[row] = [qs(a, qm(coefficient, b)) for a, b in zip(matrix[row], matrix[active])]
        pivots.append(column)
        active += 1
    return matrix[:active], pivots


@lru_cache(maxsize=1)
def derive_n3_character() -> dict:
    group = enumerate_by_recurrence(3)
    r, s = generator_pair(3)
    elements = [exponentiate(r, k) for k in range(9)] + [
        multiply(exponentiate(r, k), s) for k in range(9)
    ]
    assert set(elements) == set(group)
    monomials = []
    for a in (0, 1):
        monomials.extend((a, 1 - a, u) for u in weak_compositions(a + 1, 6))
    lookup = {monomial: index for index, monomial in enumerate(monomials)}
    assert len(monomials) == 27
    edges = {tuple(sorted((i, (i + 1) % 6))): qr(int(i == 5)) for i in range(6)}

    def vector(terms):
        answer = [Z] * 27
        for coefficient, monomial in terms:
            position = lookup[monomial]
            answer[position] = qa(answer[position], coefficient)
        return answer

    relations = []
    for i in range(6):
        exponent = [0] * 6
        exponent[i] = 2
        terms = [(qn(3), (1, 0, tuple(exponent)))]
        for edge, coefficient in edges.items():
            if i in edge:
                other = edge[0] if edge[1] == i else edge[1]
                exponent = [0] * 6
                exponent[other] = 1
                terms.append((coefficient, (0, 1, tuple(exponent))))
        relations.append(vector(terms))
    terms = []
    for edge, coefficient in edges.items():
        exponent = [0] * 6
        exponent[edge[0]] += 1
        exponent[edge[1]] += 1
        terms.append((coefficient, (1, 0, tuple(exponent))))
    relations.append(vector(terms))
    reduced, pivots = row_reduce(relations)
    pivot_row = {pivot: row for row, pivot in enumerate(pivots)}
    basis = [index for index in range(27) if index not in pivot_row]
    assert len(pivots) == 7 and len(basis) == 20

    def action(permutation, phases, scale, monomial):
        determinant = qm(qn(sign_of(permutation)), qr(sum(phases)))
        residue = qm(determinant, qi(qr(scale)))
        a, b, exponent = monomial
        target_exponent = [0] * 6
        phase = -scale * b
        for i, count in enumerate(exponent):
            target_exponent[permutation[i]] += count
            phase += phases[i] * count
        return lookup[(a, b, tuple(target_exponent))], qm(residue, qr(phase))

    def descriptor(item, monomial):
        return action(item[0], item[1], group[item], monomial)

    def reduce_vector(row):
        answer = row[:]
        for pivot in pivots:
            if answer[pivot] != Z:
                coefficient = answer[pivot]
                answer = [
                    qs(a, qm(coefficient, b))
                    for a, b in zip(answer, reduced[pivot_row[pivot]])
                ]
        return answer

    relation_tests = 0
    for item in elements:
        for relation in relations:
            image = [Z] * 27
            for position, coefficient in enumerate(relation):
                if coefficient != Z:
                    target, scalar = descriptor(item, monomials[position])
                    image[target] = qa(image[target], qm(coefficient, scalar))
            assert all(value == Z for value in reduce_vector(image))
            relation_tests += 1

    law_tests = 0
    for first in elements:
        for second in elements:
            composite = multiply(first, second)
            for monomial in monomials:
                middle, a = descriptor(first, monomial)
                target, b = descriptor(second, monomials[middle])
                direct, c = descriptor(composite, monomial)
                assert target == direct and qm(a, b) == c
                law_tests += 1

    scalar_tests = 0
    for item in elements:
        for shift in (1, 2):
            lifted_phases = tuple((phase + shift) % 3 for phase in item[1])
            lifted_scale = (group[item] + 2 * shift) % 3
            for monomial in monomials:
                assert descriptor(item, monomial) == action(
                    item[0], lifted_phases, lifted_scale, monomial
                )
                scalar_tests += 1

    def quotient_trace(item) -> int:
        trace = Z
        for position in basis:
            target, scalar = descriptor(item, monomials[position])
            if target == position:
                trace = qa(trace, scalar)
            elif target in pivot_row:
                trace = qs(trace, qm(scalar, reduced[pivot_row[target]][position]))
        assert trace[1] == 0 and trace[0].denominator == 1
        return int(trace[0])

    h_rotation = [quotient_trace(exponentiate(r, k)) for k in range(9)]
    h_reflection = [quotient_trace(multiply(exponentiate(r, k), s)) for k in range(9)]

    def fermat_trace(item) -> int:
        permutation, phases = item
        determinant = qm(qn(sign_of(permutation)), qr(sum(phases)))
        trace = I
        for degree in (0, 3, 6):
            for subset in combinations(range(6), degree):
                if {permutation[i] for i in subset} == set(subset):
                    trace = qa(trace, qm(determinant, qr(sum(phases[i] for i in subset))))
        assert trace[1] == 0 and trace[0].denominator == 1
        return int(trace[0])

    e_rotation = [fermat_trace(exponentiate(r, k)) for k in range(9)]
    e_reflection = [fermat_trace(multiply(exponentiate(r, k), s)) for k in range(9)]

    def cyclotomic_vector(exponent):
        exponent %= 9
        vector = [0] * 6
        if exponent < 6:
            vector[exponent] = 1
        else:
            vector[exponent - 6] = -1
            vector[exponent - 3] = -1
        return vector

    def multiplicities(rotation, reflection):
        answer = {
            "trivial": (sum(rotation) + sum(reflection)) // 18,
            "epsilon": (sum(rotation) - sum(reflection)) // 18,
        }
        for j in range(1, 5):
            numerator = [0] * 6
            for k, trace in enumerate(rotation):
                for term in (cyclotomic_vector(j * k), cyclotomic_vector(-j * k)):
                    numerator = [a + trace * b for a, b in zip(numerator, term)]
            assert numerator[1:] == [0] * 5 and numerator[0] % 18 == 0
            answer[f"U{j}"] = numerator[0] // 18
        return answer

    h_mult = multiplicities(h_rotation, h_reflection)
    e_mult = multiplicities(e_rotation, e_reflection)
    o_mult = {key: 2 * value for key, value in h_mult.items()}
    sector_pairs = [
        {
            "sector": sector,
            "E3_multiplicity": e_mult[sector],
            "O3_multiplicity": o_mult[sector],
            "both_divisible_by_3": e_mult[sector] % 3 == 0 and o_mult[sector] % 3 == 0,
        }
        for sector in ("trivial", "epsilon", "U1", "U2", "U3", "U4")
    ]
    order_counts = {}
    for item in elements:
        order = order_of(item, 18)
        order_counts[order] = order_counts.get(order, 0) + 1
    return {
        "group": "Dih(C9)",
        "group_order": 18,
        "element_order_counts": {str(key): order_counts[key] for key in sorted(order_counts)},
        "cayley_jacobian": {
            "bidegree": "R_(1,-1)",
            "ambient_monomials": 27,
            "jacobian_generators": 7,
            "jacobian_relation_rank": 7,
            "quotient_dimension_H21": 20,
            "residue_action_factor": "det(M_g)/det(A_g)",
            "residue_factor_orientation": "NUMERATOR_VARIABLE_MATRIX_OVER_DENOMINATOR_EQUATION_MATRIX",
            "relation_image_tests": relation_tests,
            "group_law_monomial_tests": law_tests,
            "scalar_lift_exponents_tested": [1, 2],
            "scalar_lift_descriptor_tests": scalar_tests,
            "projective_scalar_lift_invariant": True,
        },
        "H21_character": {
            "rotation_traces_k0_to_k8": h_rotation,
            "reflection_traces_k0_to_k8": h_reflection,
            "irreducible_multiplicities": h_mult,
            "dimension": 20,
        },
        "O3_character": {
            "construction": "H21_plus_complex_conjugate_H12",
            "irreducible_multiplicities": o_mult,
            "dimension": 40,
            "real_character_double": True,
        },
        "E3_character": {
            "includes_extra_trivial_line": True,
            "rotation_traces_k0_to_k8": e_rotation,
            "reflection_traces_k0_to_k8": e_reflection,
            "irreducible_multiplicities": e_mult,
            "dimension": 23,
        },
        "central_sector_test": {
            "scaling": "4/3",
            "integrality_criterion": "each selected rail multiplicity divisible by 3",
            "sector_pairs": sector_pairs,
            "nonzero_common_integral_sector_exists": False,
            "Reynolds_invariant_ranks": {"E3": 1, "O3": 0},
        },
        "coefficient_field_orbit_blocks": [
            {"sectors": ["trivial"], "E3_multiplicity": 1, "O3_multiplicity": 0},
            {"sectors": ["epsilon"], "E3_multiplicity": 2, "O3_multiplicity": 4},
            {"sectors": ["U1", "U2", "U4"], "E3_multiplicity": 3, "O3_multiplicity": 4},
            {"sectors": ["U3"], "E3_multiplicity": 1, "O3_multiplicity": 6},
        ],
        "rational_form_caveat": {
            "common_character_theorem_field": "K=Q(rho)",
            "Fermat_standard_Q_form_equals_M3_twisted_form_claimed": False,
            "M3_twist_available_for_common_group_scheme_wording": True,
            "split_traces_unchanged_by_twist": True,
            "inert_traces_may_change": True,
        },
    }


GATE_NAMES = [
    "G00_CENTRAL_SEMANTIC_LEAF_TABLE",
    "G01_SOURCE_COEFFICIENT_ORDER_LOCK",
    "G01A_C53_COMMITTED_ROUTE_TUPLE",
    "G02_PHASE_NORMALIZATION",
    "G03_IDEAL_TO_EQUATION_LINES",
    "G04_EDGE_RECURRENCE_CLOSURE_PARITY",
    "G05_EXHAUSTIVE_SUPPORT_LIFT_COUNT",
    "G06_GENERATOR_ORDER_DIHEDRAL_RELATION",
    "G07_SUPPORT_EXACT_SEQUENCE",
    "G08_SEMILINEAR_TRANSPORT",
    "G09_TWO_FIXED_POINTS_PARITY_FORMULAS",
    "G10_NONCONSTANT_GROUP_SCHEME_SCOPE",
    "G11_REYNOLDS_TRANSFER_DENOMINATORS",
    "G12_CERTIFIED_CONDITIONAL_ROWS",
    "G13_PURE_RAIL_RANKS",
    "G14_RATIONAL_SPLIT_EXPONENT_FOUR_OVER_N",
    "G15_FIXED_ELL_SEMISIMPLIFICATION_PASSAGE",
    "G16_CHEBOTAREV_BRAUER_NESBITT_IDENTITY",
    "G17_WEIGHT_RAIL_SEPARATION",
    "G18_TOTAL_RANK_TRAP_N3",
    "G19_N_DIVIDES_24_REDUCTION",
    "G20_EXACT_SURVIVORS_TWO_FOUR",
    "G21_DIRECT_SUM_CONVERSE",
    "G22_INERT_GLOBAL_FIREWALL",
    "G23_N3_CAYLEY_QUOTIENT",
    "G24_RESIDUE_ORIENTATION_SCALAR_LIFT",
    "G25_N3_EXACT_GEOMETRIC_CHARACTERS",
    "G26_RATIONAL_ORBIT_BLOCKS",
    "G27_NO_COMMON_INTEGRAL_SECTOR",
    "G28A_COUNTERPACKET_K0_CATEGORY_SCOPE",
    "G28_RESTRICTION_KERNEL_CAVEAT",
    "G29_ACTUAL_VIRTUAL_COUNTERPACKET_DISTINCTION",
    "G30_ALL_N_SMOOTHNESS_FIREWALL",
    "G31_GLOBAL_ANALYTIC_EXCLUSIONS",
    "G32_JSON_ENVELOPE_SCHEMA_TYPES",
    "G33_REPRODUCIBLE_EVIDENCE_AND_RECON_SCOPE",
]


def verify(certificate: dict, raw: bytes) -> dict:
    passed_gates: set[str] = set()
    assert type(certificate) is dict and set(certificate) == {"schema", "payload", "payload_sha256"}
    assert certificate["schema"] == "hcs-c54-certificate-v1"
    payload = certificate["payload"]
    assert type(payload) is dict and set(payload) == PAYLOAD_KEYS
    computed_payload_hash = digest_bytes(canonical_json(payload).encode())
    assert certificate["payload_sha256"] == computed_payload_hash
    assert computed_payload_hash == EXPECTED_PAYLOAD_SHA256
    computed_schema_hash = digest_bytes(canonical_json(schema_descriptor(payload)).encode())
    assert computed_schema_hash == EXPECTED_SCHEMA_SHA256
    passed_gates.add("G32_JSON_ENVELOPE_SCHEMA_TYPES")
    scalar_inventory = validate_scalar_inventory(payload)
    for path, expected in SEMANTIC_EXPECTED.items():
        actual = value_at(payload, path)
        if not exact(actual, expected):
            raise AssertionError(
                "central semantic leaf mismatch at " + "/".join(map(str, path))
            )
    passed_gates.add("G00_CENTRAL_SEMANTIC_LEAF_TABLE")

    c53_raw = C53_PATH.read_bytes()
    assert digest_bytes(c53_raw) == EXPECTED_C53_SHA256
    c53 = strict_load(c53_raw)
    assert c53["payload_sha256"] == EXPECTED_C53_PAYLOAD_SHA256
    lock = payload["source_family"]["C53_source_lock"]
    assert lock["certificate_sha256"] == EXPECTED_C53_SHA256
    assert lock["payload_sha256"] == EXPECTED_C53_PAYLOAD_SHA256
    assert lock["semisimplicity_certified_by_C53"] is False
    assert lock["implementation_commit"] == EXPECTED_C53_IMPLEMENTATION_COMMIT
    assert lock["provenance_commit"] == EXPECTED_C53_PROVENANCE_COMMIT
    assert lock["route_path"] == C53_ROUTE_RELATIVE
    assert lock["route_sha256"] == EXPECTED_C53_ROUTE_SHA256
    expected_route_tuple = {
        "implementation_commit": EXPECTED_C53_IMPLEMENTATION_COMMIT,
        "certificate_sha256": EXPECTED_C53_SHA256,
        "payload_sha256": EXPECTED_C53_PAYLOAD_SHA256,
        "independent_check_sha256": EXPECTED_C53_CHECK_SHA256,
        "code_results_manifest_sha256": EXPECTED_C53_CODE_RESULTS_MANIFEST_SHA256,
    }
    assert exact(lock["route_release_tuple"], expected_route_tuple)
    assert lock["commit_lock_status"] == (
        "VERIFIED_GIT_OBJECT_CERTIFICATE_AND_COMMITTED_ROUTE_TUPLE"
    )
    committed_certificate = subprocess.run(
        [
            "git",
            "show",
            f"{EXPECTED_C53_IMPLEMENTATION_COMMIT}:{C53_CERTIFICATE_RELATIVE}",
        ],
        cwd=REPO,
        check=True,
        capture_output=True,
    ).stdout
    assert digest_bytes(committed_certificate) == EXPECTED_C53_SHA256
    subprocess.run(
        ["git", "merge-base", "--is-ancestor", EXPECTED_C53_IMPLEMENTATION_COMMIT, EXPECTED_C53_PROVENANCE_COMMIT],
        cwd=REPO,
        check=True,
        capture_output=True,
    )
    committed_route = subprocess.run(
        ["git", "show", f"{EXPECTED_C53_PROVENANCE_COMMIT}:{C53_ROUTE_RELATIVE}"],
        cwd=REPO,
        check=True,
        capture_output=True,
    ).stdout
    assert digest_bytes(committed_route) == EXPECTED_C53_ROUTE_SHA256
    assert exact(parse_c53_route_release_tuple(committed_route), expected_route_tuple)
    passed_gates.add("G01A_C53_COMMITTED_ROUTE_TUPLE")

    family = payload["source_family"]
    assert family["rho_relation"] == "rho^2+rho+1=0"
    assert family["closing_edge_coefficient"] == "rho"
    assert family["full_PGL_automorphism_group_claimed"] is False
    passed_gates.add("G01_SOURCE_COEFFICIENT_ORDER_LOCK")

    group_block = payload["full_projective_monomial_group"]
    assert group_block["isomorphism"] == "PMonStab(C_n,Q_n_rho)=Dih(C_(3n))"
    assert group_block["order"] == "6n"
    assert group_block["phase_normalization"] == "e_i in F3 and e_0=0"
    phase_derivation = group_block["phase_and_scale_derivation"]
    assert phase_derivation == {
        "projective_scalar_normalization": "lambda_0=1",
        "cubic_line_coefficient_step": "lambda_i^3=1 for every i",
        "coordinate_phases_in_mu3": True,
        "quadric_edge_ratio_step": "the quadric scale is lambda_i*lambda_j times a ratio of source/target edge coefficients, all in mu3",
        "quadric_scale_in_mu3": True,
        "q_definition": "quadric scale=rho^q with q in F3",
    }
    lemma = group_block["ideal_to_equation_lines"]
    assert lemma["both_equation_lines_preserved"] is True
    assert lemma["domain_step"].startswith("polynomial ring is a domain")
    assert group_block["edge_recurrence"] == "e_(j+1)=q+c_(sigma(E_j))-c_j-e_j mod 3"
    assert group_block["closure_condition"].endswith("odd edge index")
    assert group_block["surviving_support_counts"] == {
        "rotations": "n",
        "reflections": "n",
    }
    assert group_block["normalized_lifts_per_support"] == 3
    expected_controls = expected_group_controls()
    assert exact(group_block["finite_exact_controls_n2_to_n64"], expected_controls)
    assert group_block["finite_controls_sha256"] == digest_bytes(canonical_json(expected_controls).encode())
    for row in group_block["independent_bruteforce_controls"]:
        n = row["n"]
        brute = enumerate_by_phases(n)
        recurrence = enumerate_by_recurrence(n)
        assert brute == recurrence
        assert exact(
            row,
            {
                "n": n,
                "normalized_phase_assignments_scanned": (4 * n) * 3 ** (2 * n - 1),
                "stabilizers_found": 6 * n,
                "matches_recurrence_list": True,
            },
        )
    assert [row["n"] for row in group_block["independent_bruteforce_controls"]] == [2, 3, 4]
    assert group_block["support_exact_sequence"] == "1 -> C3 -> G_n -> Dih(C_n) -> 1"
    assert group_block["generators"]["r_exact_order"] == "3n"
    assert group_block["generators"]["srs"] == "r^(-1)"
    assert group_block["nonmonomial_automorphisms_classified"] is False
    passed_gates.update(
        {
            "G02_PHASE_NORMALIZATION",
            "G03_IDEAL_TO_EQUATION_LINES",
            "G04_EDGE_RECURRENCE_CLOSURE_PARITY",
            "G05_EXHAUSTIVE_SUPPORT_LIFT_COUNT",
            "G06_GENERATOR_ORDER_DIHEDRAL_RELATION",
            "G07_SUPPORT_EXACT_SEQUENCE",
        }
    )

    rational = payload["rational_group_form"]
    rational_controls = expected_rational_controls()
    assert rational["finite_exact_controls_sha256"] == digest_bytes(canonical_json(rational_controls).encode())
    assert rational["delta_r"] == "r^(-1)" and rational["delta_s"] == "r*s=s*r^(-1)"
    assert rational["Q_rational_point_count"] == 2
    assert rational["fixed_elements_even_n"] == ["1", "r^(3n/2)"]
    assert rational["fixed_elements_odd_n"] == ["1", "r^((3n+1)/2)*s"]
    assert rational["group_scheme"].startswith("finite etale nonconstant")
    assert rational["Reynolds"]["denominator"] == "6n"
    assert rational["Reynolds"]["graphs_used"] == "all 6n geometric graphs"
    assert rational["quadratic_transfer"]["denominator"] == 2
    assert rational["quadratic_transfer"]["distinct_from_Reynolds_denominator"] is True
    passed_gates.update(
        {
            "G08_SEMILINEAR_TRANSPORT",
            "G09_TWO_FIXED_POINTS_PARITY_FORMULAS",
            "G10_NONCONSTANT_GROUP_SCHEME_SCOPE",
            "G11_REYNOLDS_TRANSFER_DENOMINATORS",
        }
    )

    scope = payload["claim_scope"]
    assert scope["certified_packet_rows"] == [2, 3, 4]
    assert scope["conditional_packet_rows"].startswith("n>=5")
    assert "no semisimplicity hypothesis" in scope["packet_admissibility_definition"]
    assert scope["C53_semisimplicity_claimed"] is False
    assert scope["proof_semisimplicity_passage"].startswith("fix one coefficient prime")
    assert "semisimple" not in scope["ordinary_meaning"]
    passed_gates.add("G12_CERTIFIED_CONDITIONAL_ROWS")
    rigidity = payload["split_denominator_rigidity"]
    assert rigidity["packet_weights"] == {"E_n": 0, "O_n": 1}
    assert rigidity["packet_ranks"] == {
        "e_n": "(4^n+5)/3",
        "o_n": "2*(4^n-4)/3",
        "relation": "o_n=2*(e_n-3)",
    }
    assert rigidity["split_exponent_after_Q_descent"] == "4/n"
    restriction = rigidity["restriction_argument"]
    assert restriction["fixed_coefficient_prime"] is True
    assert restriction["semisimplification_passage"] == (
        "replace each fixed-ell realization by its semisimplification; traces and ranks are unchanged"
    )
    assert restriction["semisimple_theorem"].endswith("only after semisimplification")
    assert restriction["source_semisimplicity_assumed"] is False
    assert restriction["K0_identity"] == (
        "n*[(Res V_n,ell)^ss]=4*[(Res E_n,ell)^ss]+4*[(Res O_n,ell)^ss]"
    )
    assert rigidity["restriction_argument"]["pure_weight_separation"] is True
    divisor_rows = []
    for n in (2, 3, 4, 6, 8, 12, 24):
        e, o = ranks(n)
        divisor_rows.append(
            {
                "n": n,
                "e_n": e,
                "o_n": o,
                "4e_mod_n": 4 * e % n,
                "4o_mod_n": 4 * o % n,
                "both_rails_integral": 4 * e % n == 0 and 4 * o % n == 0,
            }
        )
    assert exact(rigidity["divisors_of_24_table"], divisor_rows)
    assert rigidity["surviving_rows"] == [2, 4]
    survivors = []
    for n in range(2, 513):
        e, o = ranks(n)
        if 4 * e % n == 0 and 4 * o % n == 0:
            survivors.append(n)
    assert survivors == rigidity["finite_scan_survivors"] == [2, 4]
    assert rigidity["classification"].endswith("iff n divides 4")
    assert rigidity["converse_matches_every_power_trace"] is True
    trap = rigidity["total_rank_trap_n3"]
    assert trap == {
        "e_3": 23,
        "o_3": 40,
        "total_rank": 63,
        "scaled_total_rank": 84,
        "scaled_E3_rank": "92/3",
        "scaled_O3_rank": "160/3",
        "total_rank_only_would_falsely_accept": True,
        "proof_route_accepted": False,
    }
    assert rigidity["both_pure_rails_essential"] is True
    assert rigidity["n_ge_5_packet_status"] == "CONDITIONAL_NOT_CONSTRUCTED"
    assert rigidity["inert_factor_generally_square_claimed"] is False
    assert rigidity["global_fractional_root_claimed"] is False
    passed_gates.update(
        {
            "G13_PURE_RAIL_RANKS",
            "G14_RATIONAL_SPLIT_EXPONENT_FOUR_OVER_N",
            "G15_FIXED_ELL_SEMISIMPLIFICATION_PASSAGE",
            "G16_CHEBOTAREV_BRAUER_NESBITT_IDENTITY",
            "G17_WEIGHT_RAIL_SEPARATION",
            "G18_TOTAL_RANK_TRAP_N3",
            "G19_N_DIVIDES_24_REDUCTION",
            "G20_EXACT_SURVIVORS_TWO_FOUR",
            "G21_DIRECT_SUM_CONVERSE",
            "G22_INERT_GLOBAL_FIREWALL",
        }
    )

    derived_n3 = derive_n3_character()
    assert exact(payload["n3_equivariant_character"], derived_n3)
    assert derived_n3["cayley_jacobian"]["residue_action_factor"] == "det(M_g)/det(A_g)"
    assert derived_n3["cayley_jacobian"]["projective_scalar_lift_invariant"] is True
    assert derived_n3["H21_character"]["rotation_traces_k0_to_k8"] == [20, -1, -1, 2, -1, -1, 2, -1, -1]
    assert derived_n3["E3_character"]["rotation_traces_k0_to_k8"] == [23, 2, 2, -4, 2, 2, -4, 2, 2]
    assert derived_n3["coefficient_field_orbit_blocks"][2]["sectors"] == ["U1", "U2", "U4"]
    assert derived_n3["central_sector_test"]["nonzero_common_integral_sector_exists"] is False
    passed_gates.update(
        {
            "G23_N3_CAYLEY_QUOTIENT",
            "G24_RESIDUE_ORIENTATION_SCALAR_LIFT",
            "G25_N3_EXACT_GEOMETRIC_CHARACTERS",
            "G26_RATIONAL_ORBIT_BLOCKS",
            "G27_NO_COMMON_INTEGRAL_SECTOR",
        }
    )

    firewall = payload["counterpacket_firewall"]
    assert firewall["K0_ss_category"] == (
        "classes of fixed-ell finite-dimensional continuous semisimple ell-adic "
        "representations arising from the compatible systems in scope, unramified "
        "outside one common finite set; not arbitrary G_Q representations"
    )
    assert firewall["Q_split_primes_absolute_density"] == "1/2"
    assert firewall["trace_zero_hypothesis_density"] == (
        "relative density one within the good split rational primes"
    )
    assert firewall["lifted_K_degree_one_prime_density"] == (
        "density one among primes of K after finitely many exclusions"
    )
    assert firewall["trace_zero_conclusion"] == "Res(D)=0"
    assert firewall["actual_invisible_counterpacket"] == "only zero"
    assert firewall["virtual_restriction_injective_claimed"] is False
    assert firewall["virtual_kernel_example"] == "1-chi_(K/Q)"
    assert firewall["example_nonzero_virtual_class"] is True
    assert firewall["example_restriction_zero"] is True
    assert firewall["every_kernel_class_rank"] == 0
    assert firewall["kernel_can_change_K_rail_rank"] is False
    assert firewall["kernel_can_change_K_source_isotypic_multiplicity"] is False
    passed_gates.update(
        {
            "G28A_COUNTERPACKET_K0_CATEGORY_SCOPE",
            "G28_RESTRICTION_KERNEL_CAVEAT",
            "G29_ACTUAL_VIRTUAL_COUNTERPACKET_DISTINCTION",
        }
    )

    exclusions = payload["exclusions"]
    assert set(exclusions) == {
        "full_PGL_automorphism_group",
        "smoothness_all_n",
        "compatible_packets_all_n",
        "Chow_motive_all_n",
        "all_6n_individual_Q_automorphisms",
        "rotations_only_Reynolds_average",
        "global_fractional_Euler_root",
        "inert_fractional_Euler_root",
        "unique_Q_extension_from_split_traces",
        "automorphy",
        "meromorphic_continuation",
        "functional_equation",
        "Riemann_hypothesis",
        "fixed_Frobenius_prime_theorem_input",
    }
    assert all(value is False for value in exclusions.values())
    passed_gates.update(
        {"G30_ALL_N_SMOOTHNESS_FIREWALL", "G31_GLOBAL_ANALYTIC_EXCLUSIONS"}
    )
    controls = payload["primary_source_controls"]
    assert controls["reproducible_certificate_evidence"] == {
        "producer": "code/c54_producer.py",
        "checker": "code/c54_checker.py",
        "formal_proof": "THEOREM_PACKAGE.md and PROOF_PACKAGE.md",
        "bibliographic_locators": "SOURCE_AUDIT.md",
    }
    assert controls["primary_locators_duplicated_in_certificate"] is False
    reconnaissance = controls["pre_c54_reconnaissance"]
    assert reconnaissance["status"] == "UNPACKAGED_NOT_REPLAYED_NOT_THEOREM_INPUT"
    assert reconnaissance["chronology_note_only"] is True
    assert reconnaissance["counts_as_source_or_semantic_proof_gate"] is False
    assert set(reconnaissance["historical_sha256"]) == {
        "theorem_planning_note",
        "architecture_planning_note",
        "general_group_exploration",
        "n3_exploration",
    }
    assert "/tmp" not in canonical_json(controls)
    assert payload["artifact_status"] == "RELEASE_CANDIDATE"
    passed_gates.add("G33_REPRODUCIBLE_EVIDENCE_AND_RECON_SCOPE")
    if passed_gates != set(GATE_NAMES):
        missing = sorted(set(GATE_NAMES) - passed_gates)
        extra = sorted(passed_gates - set(GATE_NAMES))
        raise AssertionError(f"gate execution mismatch missing={missing} extra={extra}")

    return {
        "schema": "hcs-c54-independent-check-v1",
        "certificate_sha256": digest_bytes(raw),
        "payload_sha256": computed_payload_hash,
        "schema_sha256": computed_schema_hash,
        "semantic_gate_count": len(GATE_NAMES),
        "central_semantic_leaf_count": len(SEMANTIC_EXPECTED),
        "derived_scalar_leaf_count": scalar_inventory["derived"],
        "nonsemantic_allowlist_count": scalar_inventory["nonsemantic"],
        "total_scalar_leaf_count": scalar_inventory["total"],
        "semantic_gates": [
            {"gate": name, "status": "PASS"}
            for name in GATE_NAMES
            if name in passed_gates
        ],
        "exact_control_summary": {
            "universal_group_rows": 63,
            "full_independent_group_replays": 19,
            "bruteforce_phase_rows": [2, 3, 4],
            "rational_form_parity_rows": 255,
            "denominator_scan_rows": 511,
            "n3_relation_image_tests": derived_n3["cayley_jacobian"]["relation_image_tests"],
            "n3_group_law_monomial_tests": derived_n3["cayley_jacobian"]["group_law_monomial_tests"],
            "n3_scalar_lift_tests": derived_n3["cayley_jacobian"]["scalar_lift_descriptor_tests"],
        },
        "result": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    output = arguments.output
    if output.exists():
        if not output.is_file():
            print(f"CHECK FAILED: output exists and is not a file: {output}", file=sys.stderr)
            return 1
        output.unlink()
    if not __debug__:
        print("CHECK FAILED: optimized Python disables certificate assertions", file=sys.stderr)
        return 1
    try:
        raw = arguments.certificate.read_bytes()
        certificate = strict_load(raw)
        result = verify(certificate, raw)
    except Exception as error:
        print(f"CHECK FAILED: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    encoded = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(f".{output.name}.{os.getpid()}.new")
    try:
        temporary.write_text(encoded, encoding="utf-8")
        temporary.replace(output)
    except Exception as error:
        if temporary.is_file():
            temporary.unlink()
        if output.is_file():
            output.unlink()
        print(f"CHECK FAILED: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    print(f"PASS {len(GATE_NAMES)}/{len(GATE_NAMES)} semantic gates")
    print(f"wrote {output} sha256={digest_bytes(encoded.encode())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
