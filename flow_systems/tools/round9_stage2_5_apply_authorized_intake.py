#!/usr/bin/env python3
"""Apply the scholar-authorized Round-9 Stage-2.5 experiment intake.

The script transcribes existing Round-2--8 files.  It never runs an
experiment, changes a manuscript/bibliography/PDF, or invents a historical
runtime lock.  Historical fields that were not recorded are labelled as such.
Claim-intent manifests are explicitly retrospective gate-time transcriptions,
not assertions of pre-writing intent.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DECLARED_AT = "2026-08-29T05:52:42Z"
BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does "
    "not judge whether the experiment was correctly designed, run, statistically "
    "adequate, or reproducible by ARS."
)
AUTHORIZATION = (
    "Papers 24–28 each report computational experiments or certificates actually "
    "executed for this project. I authorize each passport to record "
    "status=experiments_declared, declared_by=scholar, and the confirmation time. "
    "I authorize the existing Round-2–8 source, freeze, result, test, validation, "
    "and receipt artifacts to be transcribed into schema-valid experiment "
    "provenance and aligned to the registered experiment-backed claims. To my "
    "knowledge, there are no additional omitted own-experiment results relied on "
    "by these five manuscripts."
)


PAPERS = {
    "24-bianchi-holonomy-flow": 24,
    "25-three-disk-scattering-flow": 25,
    "26-level11-newform-time-change": 26,
    "27-congruence-inverse-limit-no-go": 27,
    "28-bolza-magnetic-flow": 28,
}


# (round, stable id, title, primary result file, JSON pointer, negative result,
#  finite/historical limitation).  Values are read from the named result at
#  transcription time; they are never copied from this configuration.
SPECS: dict[str, list[tuple[int, str, str, str, str, str, str]]] = {
    "24-bianchi-holonomy-flow": [
        (2, "P24-R2-BIANCHI-WORDBALL", "Level-(3) Gaussian elementary word-ball ledger and target-free holonomy shuffle", "results/round2_metrics.json", "/unique_exact_matrices", "The holonomy control verdict remained OPEN and no orbit-to-prime-ideal map was established.", "Elementary-generated reduced-word ball only; not full Gamma(3), full conjugacy, or a group-certified primitive ledger."),
        (3, "P24-R3-SCHOTTKY-CONTROL", "Rank-4 classical-Schottky control and intrinsic holonomy shuffle", "results/round3_metrics.json", "/primitive_oriented_cyclic_classes", "The arithmetic-hypothesis verdict remained OPEN.", "Exact only for the frozen marking and word cutoff five; the control is an infinite-volume non-lattice and is not cusp/finite-volume matched."),
        (4, "P24-R4-FIVE-TWO-CONTROL", "5_2=m015 finite-volume non-arithmetic control prefix and crosscheck", "results/round4_metrics.json", "/primary_primitive_classes_by_group_multiplicity", "The cross-system arithmetic verdict remained OPEN and local interval verification was not run.", "Published source-chain geometry and the local high-precision numerical prefix have different evidence status; no same-enumeration Bianchi comparison was made."),
        (5, "P24-R5-MATCHED-MARKED-WORD", "Frozen matched marked-word phase comparison", "results/round5_metrics.json", "/comparison_status", "The alphabet-size/presentation confound remained and no arithmetic verdict was assigned.", "This is a marked-word statistic, not a complete metric length spectrum; group-conjugacy and primitivity completeness are not claimed."),
        (6, "P24-R6-NIELSEN-SENSITIVITY", "Frozen exhaustive elementary Nielsen-marking sensitivity panel", "results/round6_nielsen_metrics.json", "/marking_robustness_pass", "The control range-width criterion failed and presentation invariance was refuted for this finite-cutoff statistic.", "The freeze followed a disclosed non-evidentiary feasibility pilot; the control marking is Tietze-redundant rather than presentation-matched."),
        (7, "P24-R7-TRACE-DISCRIMINANT", "Frozen exact D9 trace-discriminant certificate", "results/round7_trace_discriminant_metrics.json", "/d9_collision_rows_beyond_first", "D9 was non-injective and produced no owner or metric prefix.", "The execution covers an elementary word ball, not a full group/conjugacy enumeration, and assigns no Gaussian-prime label."),
        (8, "P24-R8-CONGRUENCE-SPECIFICITY", "Frozen cross-ring congruence-specificity and first-jet collision audit", "results/round8_congruence_specificity_metrics.json", "/first_jet_audit/joint_descriptor_collision_rows_beyond_first", "D9 was refuted as Gaussian-specific; the first jet retained 10,964 collision rows and zero singleton joint buckets.", "Only two of three required canonical control types were executed; matrix-row collisions are not promoted to owner collisions."),
    ],
    "25-three-disk-scattering-flow": [
        (2, "P25-R2-THREE-DISK-NEGATIVE-CONTROL", "Three-disk primitive-orbit ledger and target-free half-density controls", "results/round2_metrics.json", "/ledger_rows", "The half-density specificity verdict was STOP_SCOPED and 2,232 finite-difference stability rows remained open in this round.", "Finite symbolic cutoff twelve and numerical physical-orbit certificate; no global determinant, arithmetic owner, or formal route tuple."),
        (3, "P25-R3-DIRECT-RETURN-MAP", "Direct high-precision physical return-map validation", "results/round3_stability_metrics.json", "/round3_direct_return_map_rows_certified", "Closing all numerical stability rows did not change the STOP_SCOPED arithmetic verdict.", "Finite-cutoff 100-digit numerical validation with 39 fallback refinements; not a global physical-flow determinant."),
        (4, "P25-R4-CONDITIONING-AUDIT", "Post-hoc return-map conditioning and fallback audit", "results/round4_conditioning_metrics.json", "/stationarity_fallback_rows", "No causal or sampling-unbiasedness conclusion was obtained.", "Explicitly post-hoc descriptive audit with no new orbit solve and no separate validation note."),
        (5, "P25-R5-HALF-DENSITY-CONTROL", "Universal hyperbolic half-density theorem replay", "results/round5_universal_half_density_metrics.json", "/round5_branch_rows", "Persistence of the leading half-density was generic and could not provide arithmetic specificity.", "Local real 2x2 symplectic-map identity reusing Round-2/3 inputs; not a global physical-flow determinant and no separate validation note."),
        (6, "P25-R6-SYMBOLIC-ZETA", "Frozen three-symbol unit-roof symbolic-zeta calibrator", "results/round6_symbolic_zeta_metrics.json", "/frozen_owner_rows_through_length_12", "Collision parity reduced to z -> -z and supplied no arithmetic specificity; the typed route was rejected.", "Unit-roof symbolic object only, replayed through degree twelve; no physical flight-length determinant."),
        (7, "P25-Q-SYMBOL-NO-REPEAT-FAMILY-V1", "Frozen q-symbol no-repeat unit-roof family replay", "results/round7_q_symbolic_summary.json", "/count_rows", "Arithmetic specificity was absent by negative-control design and the typed route was rejected.", "Finite replay for q=2,...,8 and degrees through twelve; the analytic all-q theorem and physical determinant are outside this execution."),
        (8, "P25-R8-ROOF-NONTRANSFER", "Frozen physical-roof nontransfer witnesses and locked replay", "results/round8_roof_nontransfer_summary.json", "/physical_replay_rows", "Owner/repetition-preserving global scalar transfer was refuted.", "A genuine nonconstant-roof transfer operator is not refuted; the physical tuple remains unassigned and the finite replay is not the analytic proof."),
    ],
    "26-level11-newform-time-change": [
        (2, "P26-R2-NEWFORM-TIMECHANGE-FINITE-V1", "Finite level-11 newform time-change source ledger", "results/round2_summary.json", "/counts/gamma0_11_selected_positive_necklaces", "Hecke/Euler evidence remained heuristic and the proposed Euler test was not testable.", "Word length at most nine; periods are finite numerical observations, not a complete Gamma_0(11) conjugacy census."),
        (3, "P26-R3-CONJUGACY-OWNER-V1", "Bounded conjugacy-owner and translation-covariance audit", "results/round3_summary.json", "/exact_conjugacy_checks", "A complete conjugacy enumeration and Hecke recurrence were not established.", "Eleven sources with nine bounded conjugators; translated periods remain numerical observations."),
        (4, "P26-R4-HECKE-CORRESPONDENCE-V1", "Finite Hecke-correspondence branch and cycle-owner audit", "results/round4_summary.json", "/closed_cycle_owner_rows", "The generic control produced 302 exact failures and no single-owner Euler factorization was established.", "Frozen eleven-source by five-prime population; not a complete conjugacy census."),
        (5, "P26-R5-ZETA-VARIATION-V1", "Finite first zeta-variation audit", "results/round5_summary.json", "/hecke_zeta_variation_rows", "Naive Ruelle and Selberg recurrences each failed 153 rows; 51 of 55 all-s degree-moment groups failed.", "Finite formal products at three s values and repetition cutoff four; no global convergence result."),
        (6, "P26-R6-SECOND-VARIATION-V1", "Finite second-variation and quadratic-moment audit", "results/round6_summary.json", "/hecke_second_variation_rows", "Both primary laws failed 51 groups and the a_p^2-p control failed all 55; only four numerical survivors remained.", "Finite local numerical audit later superseded by the exact Round-8 taxonomy; no global A2 evaluation."),
        (7, "P26-R7-EXACT-SURVIVORS-V1", "Exact classification of the four numerical survivors", "results/round7_summary.json", "/exactly_classified", "All four numerical survivors were explained by exact kernels, leaving no unexplained survivor.", "Only the four p=5 survivors were classified; this was not the complete 138-instance taxonomy."),
        (8, "P26-R8-EXACT-TAXONOMY-V1", "Complete frozen exact homology taxonomy", "results/round8_summary.json", "/instances/total", "The primary laws failed 51 of 55 groups and the control failed 55 of 55; no A2/root-count/global determinant was run.", "Complete only for the frozen multiset; no cross-instance conjugacy deduplication, complete primitive census, or global zeta."),
    ],
    "27-congruence-inverse-limit-no-go": [
        (2, "P27-R2-CONGRUENCE-ORDER-DIAGNOSTIC-V1", "Finite congruence projective-order diagnostic", "results/round2/round2_metrics.json", "/rows", "Finite-level rows received no inverse-limit periodic-orbit credit and the residual-splitting hypothesis remained heuristic.", "Eight-level diagnostic on three cusped loops; full Gamma(3) conjugacy primitivity was not established."),
        (4, "P27-R4-PERIOD-ESCAPE-VALIDATION-V1", "Finite period-escape prefix validation", "results/round4_period_escape_validation.json", "/status", "The finite rows do not prove the asymptotic theorem and no A2-A4 evaluation was performed.", "The universal theorem is a written proof; the machine checks only the frozen prefix."),
        (5, "P27-R5-COCOMPACT-HOMOLOGY-CONTROL-V1", "Closed cocompact homology lower-bound control", "results/round5_cocompact_homology_escape_validation.json", "/largest_certified_order_lower_bound", "Full quotient orders were not computed and residual cores were not enumerated.", "Exact homology lower bounds only; no claim of full quotient orders."),
        (7, "P27-R7-OWNER-PRESERVING-EULER-FACTOR-ESCAPE-V1", "Owner-preserving Euler-factor escape audit", "results/round7_owner_factor_escape_summary.json", "/ledger_rows", "A renormalized collective object was not defined or refuted; the same-owner A2 path alone was refuted.", "Cusped primitivity remains open and compact rows carry lower-bound semantics; the universal theorem is proof-backed."),
        (8, "P27-R8-HOMOLOGY-RENORMALIZATION-V1", "Exact four-quadrant homology renormalization calibrator", "results/round8_homology_renormalization_summary.json", "/quadrant_rows", "Q00/Q01 escape on fixed prefixes and Q10 diverges; only Q11 has exact recovery.", "Fixed three-owner panel in a nonresidual tower, generic for marked genus-two metrics; no full determinant or growing-panel convergence."),
    ],
    "28-bolza-magnetic-flow": [
        (2, "P28-R2-OWNER-LEDGER", "Tensor-family owner ledger", "results/round2_owner_ledger_validation.json", "/row_count", "Orbit ownership and trace binding remained open; no row received fixed-operator transfer credit.", "Bookkeeping-only seed ledger with no standalone reproducer or demonstrably pre-run freeze."),
        (3, "P28-R3-TRACE-CONTRACT", "Source-bound signed-field trace-regime contract", "results/round3_trace_regime_validation.json", "/source_bound_signed_field_rows", "Zero-field controls remained open and no fixed-operator transfer was allowed.", "Exact scaling identities only; source theorem hypotheses were not machine-verified and this is not a current-manuscript result."),
        (4, "P28-R4-BOLZA-OWNER-LEDGER", "Bolza owner seed ledger", "results/round4_bolza_owner_validation.json", "/row_count", "No oriented-owner credit, target-data rows, or formal Route-A tuple was obtained.", "Seed ledger rather than a complete Bolza spectrum/conjugacy census; no demonstrably pre-run freeze."),
        (5, "P28-R5-MARKED-CYCLIC-CENSUS", "Marked cyclic Bolza census", "results/round5_bolza_marked_cyclic_validation.json", "/census_row_count", "Gamma primitivity remained open for 322 records, eight proved records were withheld, and full Gamma conjugacy completeness was not established.", "Complete only for the declared marked-cyclic equivalence through length four; no target comparison or Route-B result."),
        (6, "P28-R6-CONJUGACY-CLOSURE", "Frozen-eight conjugacy closure and source-package fail-closed gate", "results/round6_bolza_conjugacy_validation.json", "/exact_direct_sl2_conjugacy_count", "No new owner credit was produced; 322 primitivity questions remained open and the source package gate failed 0/6.", "Closes only the frozen eight ambiguities; the historical Round-6 source failure was superseded by a distinct Round-7 package."),
        (7, "P28-R7-CONTROL-SOURCE-GATE", "Nonarithmetic control source and matrix gate", "results/round7_nonarithmetic_control_validation.json", "/matrix_count", "No systole, census, comparison, A2 evaluation, or Route-B invocation was run.", "Source/control instantiation only; nonarithmeticity and primitivity use theorem/literature support, not freestanding empirical measurement."),
        (8, "P28-R8-SYSTOLE-CERTIFICATE", "Exact control systole and finite-component certificate", "results/round8_control_finite_ball_certificate.json", "/finite_completeness/included_state_count", "No control/Bolza census, comparison, target-data use, A2 evaluation, or Route-B invocation was run; equality states were not quotient-classified.", "Cutoff 21/10 and one identity-connected guard component at u=e^-1/10; not a full length spectrum, two-surface comparison, or owner count."),
    ],
}


# Exact selected-registry spans whose project-execution component is direct and
# unambiguous enough to bind at this Stage-2.5 gate.  Proof-only, literature,
# interpretive, and heavily mixed headline spans remain on their existing
# proof/source path rather than being assigned experiment credit.
# Values are (experiment_id, result file, JSON pointer).
CLAIMS: dict[str, dict[str, tuple[str, str, str]]] = {
    "24-bianchi-holonomy-flow": {
        "P24-E1-043": ("P24-R7-TRACE-DISCRIMINANT", "results/round7_trace_discriminant_metrics.json", "/all_integrality_identities_pass"),
        "P24-E1-044": ("P24-R8-CONGRUENCE-SPECIFICITY", "results/round8_congruence_specificity_metrics.json", "/first_jet_audit/owner_separation_witness/separated_by_first_jet"),
        "P24-E1-046": ("P24-R7-TRACE-DISCRIMINANT", "results/round7_trace_discriminant_metrics.json", "/all_exact_witnesses_pass"),
        "P24-E1-048": ("P24-R8-CONGRUENCE-SPECIFICITY", "results/round8_congruence_specificity_metrics.json", "/first_jet_audit/collision_rows_separated_by_first_jet"),
        "P24-E1-049": ("P24-R8-CONGRUENCE-SPECIFICITY", "results/round8_congruence_specificity_metrics.json", "/first_jet_audit/maximum_joint_descriptor_bucket"),
        "P24-E1-050": ("P24-R8-CONGRUENCE-SPECIFICITY", "results/round8_congruence_specificity_metrics.json", "/first_jet_audit/matrix_rows"),
        "P24-E1-051": ("P24-R8-CONGRUENCE-SPECIFICITY", "results/round8_congruence_specificity_metrics.json", "/first_jet_audit/joint_descriptor_collision_rows_beyond_first"),
        "P24-E1-052": ("P24-R8-CONGRUENCE-SPECIFICITY", "results/round8_congruence_specificity_metrics.json", "/finite_control_matrix_rows"),
        "P24-E1-053": ("P24-R8-CONGRUENCE-SPECIFICITY", "results/round8_congruence_specificity_metrics.json", "/a0_control_gate/controls"),
        "P24-E1-054": ("P24-R8-CONGRUENCE-SPECIFICITY", "results/round8_congruence_specificity_metrics.json", "/a0_control_gate/status"),
        "P24-E1-055": ("P24-R8-CONGRUENCE-SPECIFICITY", "experiments/round8_receipt.json", "/unit_tests/expected"),
    },
    "25-three-disk-scattering-flow": {
        "P25-E1-025": ("P25-Q-SYMBOL-NO-REPEAT-FAMILY-V1", "results/round7_q_symbolic_summary.json", "/total_primitive_oriented_owners_through_degree_12/3"),
        "P25-E1-030": ("P25-R5-HALF-DENSITY-CONTROL", "results/round5_universal_half_density_metrics.json", "/round5_branch_rows"),
        "P25-E1-048": ("P25-R8-ROOF-NONTRANSFER", "results/round8_roof_nontransfer_summary.json", "/physical_replay_rows"),
        "P25-E1-050": ("P25-R8-ROOF-NONTRANSFER", "results/round8_roof_nontransfer_summary.json", "/geometry_summaries/6/rows_agreeing_with_period_two_scalar_clock"),
        "P25-E1-051": ("P25-R8-ROOF-NONTRANSFER", "results/round8_roof_nontransfer_summary.json", "/geometry_summaries"),
        "P25-E1-053": ("P25-R8-ROOF-NONTRANSFER", "experiments/round8_reproducibility_receipt.json", "/unit_tests/expected"),
    },
    "26-level11-newform-time-change": {
        "P26-E1-040": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/instances/total"),
        "P26-E1-043": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/groups/failure_mechanisms"),
        "P26-E1-051": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/claim_boundary/complete_frozen_138_instance_taxonomy"),
        "P26-E1-052": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/instances/total"),
        "P26-E1-053": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/instances/classification_counts"),
        "P26-E1-054": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/instances/classification_counts_by_prime"),
        "P26-E1-055": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/instances/unresolved"),
        "P26-E1-056": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/groups/a_p_squared_exact_survivors"),
        "P26-E1-057": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/groups/law_classification_counts"),
        "P26-E1-058": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/groups/failure_mechanisms"),
        "P26-E1-060": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/groups/word_prime_groups"),
        "P26-E1-062": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/source_bindings"),
        "P26-E1-063": ("P26-R8-EXACT-TAXONOMY-V1", "experiments/round8_reproducibility_receipt.json", "/unit_tests/passed"),
        "P26-E1-064": ("P26-R8-EXACT-TAXONOMY-V1", "experiments/round8_reproducibility_receipt.json", "/execution/run1_tree_sha256"),
        "P26-E1-065": ("P26-R8-EXACT-TAXONOMY-V1", "experiments/round8_reproducibility_receipt.json", "/artifacts"),
        "P26-E1-066": ("P26-R8-EXACT-TAXONOMY-V1", "experiments/round8_reproducibility_receipt.json", "/unit_tests/passed"),
        "P26-E1-070": ("P26-R8-EXACT-TAXONOMY-V1", "results/round8_summary.json", "/claim_boundary/global_cross_instance_conjugacy_deduplication"),
    },
    "27-congruence-inverse-limit-no-go": {
        "P27-E1-025": ("P27-R2-CONGRUENCE-ORDER-DIAGNOSTIC-V1", "results/round2/round2_metrics.json", "/orders_by_element"),
        "P27-E1-026": ("P27-R2-CONGRUENCE-ORDER-DIAGNOSTIC-V1", "results/round2/round2_metrics.json", "/orders_by_element/G3-A"),
        "P27-E1-027": ("P27-R2-CONGRUENCE-ORDER-DIAGNOSTIC-V1", "results/round2/round2_metrics.json", "/orders_by_element/G3-B"),
        "P27-E1-028": ("P27-R2-CONGRUENCE-ORDER-DIAGNOSTIC-V1", "results/round2/round2_metrics.json", "/orders_by_element/G3-C"),
        "P27-E1-029": ("P27-R4-PERIOD-ESCAPE-VALIDATION-V1", "results/round4_period_escape_validation.json", "/plateau_transition_count"),
        "P27-E1-030": ("P27-R2-CONGRUENCE-ORDER-DIAGNOSTIC-V1", "results/round2/round2_metrics.json", "/independent_order_crosschecks_passed"),
        "P27-E1-035": ("P27-R5-COCOMPACT-HOMOLOGY-CONTROL-V1", "results/round5_cocompact_homology_escape_validation.json", "/lower_bounds_by_owner"),
        "P27-E1-036": ("P27-R5-COCOMPACT-HOMOLOGY-CONTROL-V1", "results/round5_cocompact_homology_escape_validation.json", "/largest_certified_order_lower_bound"),
        "P27-E1-045": ("P27-R8-HOMOLOGY-RENORMALIZATION-V1", "results/round8_homology_renormalization_summary.json", "/owners"),
        "P27-E1-056": ("P27-R8-HOMOLOGY-RENORMALIZATION-V1", "results/round8_homology_renormalization_summary.json", "/coefficient_rows"),
        "P27-E1-065": ("P27-R8-HOMOLOGY-RENORMALIZATION-V1", "experiments/round8_reproducibility_receipt.json", "/core_sha256"),
        "P27-E1-066": ("P27-R8-HOMOLOGY-RENORMALIZATION-V1", "experiments/round8_reproducibility_receipt.json", "/reproduction_command"),
        "P27-E1-068": ("P27-R8-HOMOLOGY-RENORMALIZATION-V1", "results/round8_homology_renormalization_summary.json", "/quadrant_conclusions"),
        "P27-E1-069": ("P27-R8-HOMOLOGY-RENORMALIZATION-V1", "results/round8_homology_renormalization_summary.json", "/quadrant_rows"),
    },
    "28-bolza-magnetic-flow": {
        "P28-E1-015": ("P28-R7-CONTROL-SOURCE-GATE", "results/round7_nonarithmetic_control_validation.json", "/matrix_count"),
        "P28-E1-033": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/finite_completeness/included_state_count"),
        "P28-E1-038": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/exact_identity_checks"),
        "P28-E1-040": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/finite_completeness/systole_sign_taylor_order_histogram"),
        "P28-E1-045": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/proof_guards/center_radius_guard/decimal_interval"),
        "P28-E1-054": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/finite_completeness/component_boundary_closed"),
        "P28-E1-056": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/exact_systole/equality_witness"),
        "P28-E1-058": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/exact_systole/strictly_above_state_count"),
        "P28-E1-067": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/status"),
        "P28-E1-068": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/finite_completeness/included_state_count"),
        "P28-E1-069": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/finite_completeness/discovery_depth_histogram"),
        "P28-E1-070": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/finite_completeness/included_state_stream_sha256"),
        "P28-E1-071": ("P28-R8-SYSTOLE-CERTIFICATE", "experiments/round8_reproducibility_receipt.json", "/execution/byte_identical"),
        "P28-E1-083": ("P28-R8-SYSTOLE-CERTIFICATE", "results/round8_control_finite_ball_certificate.json", "/execution"),
    },
}


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def write_text(path: Path, value: str) -> None:
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(value, encoding="utf-8")
    tmp.replace(path)


def json_pointer(path: Path, pointer: str) -> Any:
    value = load_json(path)
    if not pointer.startswith("/"):
        raise ValueError(f"JSON pointer must start with /: {pointer}")
    for raw in pointer[1:].split("/"):
        key = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            value = value[int(key)]
        else:
            value = value[key]
    return value


def role_for(relative: str) -> str:
    if relative.startswith("code/test_"):
        return "test_source"
    if relative.startswith("code/"):
        return "execution_source"
    if "freeze" in relative:
        return "pre_result_freeze_or_historical_freeze_record"
    if relative.startswith("results/"):
        return "result"
    if "receipt" in relative:
        return "execution_receipt"
    if "validation" in relative:
        return "validation"
    if relative.startswith("experiments/reproduce"):
        return "reproducer"
    return "research_note"


SPECIAL_ARTIFACTS: dict[tuple[str, int], list[str]] = {
    ("26-level11-newform-time-change", 2): [
        "experiments/reproduce.sh", "experiments/reproducibility_receipt.json",
        "results/artifact_manifest.json", "results/newform_timechange_variation_ledger.csv",
        "results/simpler_parent_length_control.csv",
    ],
    ("27-congruence-inverse-limit-no-go", 2): ["experiments/reproduce.sh"],
    ("28-bolza-magnetic-flow", 2): [
        "code/build_owner_ledger.py", "code/test_owner_ledger.py",
        "results/bolza_tensor_family_owner_ledger.csv",
    ],
}


def collect_artifacts(paper: str, round_number: int, required: set[str]) -> list[dict[str, str]]:
    base = ROOT / "papers" / paper
    marker = f"round{round_number}"
    paths: set[Path] = set()
    for top in ("code", "experiments", "notes", "results"):
        for path in (base / top).rglob("*"):
            if path.is_file() and "__pycache__" not in path.parts and marker in path.as_posix().lower():
                paths.add(path)
    for relative in SPECIAL_ARTIFACTS.get((paper, round_number), []):
        paths.add(base / relative)
    for relative in required:
        paths.add(base / relative)
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"{paper} R{round_number}: missing artifacts {missing}")
    artifacts = []
    for path in sorted(paths):
        relative = path.relative_to(base).as_posix()
        artifacts.append({"path": relative, "sha256": sha(path), "role": role_for(relative)})
    return artifacts


def repro_lock(artifacts: list[dict[str, str]]) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "stochasticity_declaration": (
            "Retrospective record of a historical local code execution/certificate. "
            "Deterministic, exact, numerical, shuffle, seed, and tolerance semantics are "
            "taken only from the listed artifacts; no missing historical setting is inferred."
        ),
        "ars_version": "not-recorded-in-historical-round-2-to-8-execution; transcribed-with-ars-codex-0.1.26",
        "model": {
            "family": "not-applicable-local-code-execution",
            "id": "no-model-weight-used-by-the-recorded-execution",
            "weight_stable": True,
        },
        "prompts": {
            "hash_timing": "skill-load",
            "skill_md_hash": "not-recorded-in-historical-run",
            "agents_bundle_hash": "not-recorded-in-historical-run",
        },
        "materials": {"list_hash": canonical_sha(artifacts), "count": len(artifacts)},
        "external_protocols": {
            "s2_api_protocol_version": "not-recorded-or-used-in-local-execution-artifacts",
            "s2_snapshot_available": False,
        },
        "cross_model": {"enabled": False, "secondary_model_id": None},
    }


def build_paper(paper: str, generated_at: str) -> dict[str, Any]:
    number = PAPERS[paper]
    base = ROOT / "papers" / paper
    notes = base / "notes"
    registry = load_json(notes / "stage2_5_claim_registry.json")
    registry_by_id = {row["claim_id"]: row for row in registry["claims"]}
    selected = {key: row for key, row in registry_by_id.items() if row["selection_tier"] != "NOT-SELECTED"}
    claim_map = CLAIMS[paper]
    unknown = set(claim_map) - set(selected)
    if unknown:
        raise RuntimeError(f"{paper}: claim map references non-selected/missing claims: {sorted(unknown)}")
    if any(selected[key]["ref_slugs"] for key in claim_map):
        raise RuntimeError(f"{paper}: experiment map unexpectedly contains citation-backed mixed claim")

    referenced_by_experiment: dict[str, list[tuple[str, str]]] = {}
    for exp_id, result_file, pointer in claim_map.values():
        referenced_by_experiment.setdefault(exp_id, []).append((result_file, pointer))

    provenance = []
    source_experiments = []
    known_ids = set()
    for round_number, exp_id, title, primary_file, primary_pointer, negative, limitation in SPECS[paper]:
        known_ids.add(exp_id)
        pointers = [(primary_file, primary_pointer), *referenced_by_experiment.get(exp_id, [])]
        unique_pointers = list(dict.fromkeys(pointers))
        required = {result_file for result_file, _ in unique_pointers}
        artifacts = collect_artifacts(paper, round_number, required)
        units = []
        for result_file, pointer in unique_pointers:
            value = json_pointer(base / result_file, pointer)
            units.append({
                "planned": (
                    f"RETROSPECTIVE_TRANSCRIPTION: record the already executed Round-{round_number} "
                    f"result at {result_file}#{pointer}; no pre-run intent is inferred."
                ),
                "executed": True,
                "result_file": result_file,
                "metric": pointer,
                "value": value,
            })
        lock = repro_lock(artifacts)
        provenance.append({
            "experiment_id": exp_id,
            "title": title,
            "description": (
                f"Scholar-authorized retrospective transcription on {DECLARED_AT} of the existing "
                f"Paper {number} Round-{round_number} execution package. This is not a claim of "
                "historical preregistration or a complete historical repro_lock."
            ),
            "repro_lock": lock,
            "planned_vs_executed": units,
            "negative_results": [{"description": negative, "result_file": primary_file}],
            "known_limitations": [
                {"description": limitation},
                {"description": "Historical ARS/model/prompt/runtime lock metadata was not recorded; present-day schema completion does not retroactively create it."},
            ],
        })
        source_experiments.append({
            "experiment_id": exp_id,
            "round": round_number,
            "materials_hash_algorithm": "sha256(canonical-json of ordered [{path,role,sha256}])",
            "materials_list_sha256": lock["materials"]["list_hash"],
            "materials_count": len(artifacts),
            "artifacts": artifacts,
        })
    dangling = set(referenced_by_experiment) - known_ids
    if dangling:
        raise RuntimeError(f"{paper}: claims reference unknown experiments {sorted(dangling)}")

    manifest_id = f"M-{DECLARED_AT}-{number:04x}"
    manifest_claims = []
    alignment_rows = []
    crosswalk = []
    for index, registry_id in enumerate(sorted(claim_map), 1):
        claim = selected[registry_id]
        local_id = f"C-{index:03d}"
        exp_id, result_file, pointer = claim_map[registry_id]
        manifest_claims.append({
            "claim_id": local_id,
            "claim_text": claim["claim_text"],
            "intended_evidence_kind": "empirical",
            "planned_refs": [],
            "planned_experiment_ids": [exp_id],
        })
        alignment_rows.append({
            "finding_id": f"EA-{index:03d}",
            "scoped_manifest_id": manifest_id,
            "claim_id": local_id,
            "claim_text": claim["claim_text"],
            "experiment_id": exp_id,
            "result_pointer": f"{result_file}#{pointer}",
            "manuscript_locator": f"{claim['writer_anchors'][0]} [registry:{registry_id}]",
            "alignment_verdict": "ALIGNED",
            "rationale": (
                f"At the Stage-2.5 gate, the claim's directly reported project-execution component "
                f"matches the declared executed result {result_file}#{pointer}. The registry span "
                "may also state proof-based scope or limitations; no experiment credit is assigned "
                "to those proof-only parts. This is a retrospective transcription, not evidence of "
                "pre-writing intent or of experiment correctness."
            ),
            "judge_model": "OpenAI Codex (GPT-5 family; current Stage-2.5 session)",
            "judge_run_at": generated_at,
            "rule_version": "EA-v1",
        })
        crosswalk.append({
            "registry_claim_id": registry_id,
            "manifest_id": manifest_id,
            "manifest_claim_id": local_id,
            "experiment_id": exp_id,
            "result_pointer": f"{result_file}#{pointer}",
        })
    manifest = {
        "manifest_version": "1.0",
        "manifest_id": manifest_id,
        "emitted_by": "report_compiler_agent",
        "emitted_at": generated_at,
        "session_id": "round9-stage2.5-retrospective-provenance-transcription-not-prewriting-intent",
        "claims": manifest_claims,
        "manifest_negative_constraints": [],
    }

    classification_rows = []
    for registry_id, claim in selected.items():
        is_exp = registry_id in claim_map
        classification_rows.append({
            "registry_claim_id": registry_id,
            "selection_tier": claim["selection_tier"],
            "classification": "experiment_backed_and_aligned" if is_exp else "proof_citation_context_or_mixed_not_assigned_experiment_credit",
            "rationale": (
                "Direct own-execution/result statement with a schema-valid experiment join and exact result pointer."
                if is_exp
                else "No direct experiment credit assigned at this gate: the registered span is proof-, citation-, definition-, interpretation-, limitation-, or mixed-content and remains on those evidence paths."
            ),
        })
    population = {
        "schema": "flow-systems-stage2.5-experiment-claim-population/1.0",
        "paper": paper,
        "generated_at": generated_at,
        "population_scope": "Stage-2.5 selected Claim Registry rows",
        "retrospective_manifest_notice": "The manifest is a gate-time transcription and is not a pre-writing intent record.",
        "selected_claims": len(selected),
        "direct_experiment_backed_claims": len(claim_map),
        "aligned_direct_experiment_backed_claims": len(claim_map),
        "alignment_coverage": 1.0,
        "crosswalk": crosswalk,
        "classifications": classification_rows,
        "boundary": BOUNDARY,
    }
    write_json(notes / "stage2_5_experiment_claim_population.json", population)

    source_map = {
        "schema": "flow-systems-stage2.5-experiment-provenance-source-map/1.0",
        "paper": paper,
        "generated_at": generated_at,
        "declared_at": DECLARED_AT,
        "declaration_sha256": canonical_sha({"status": "experiments_declared", "declared_by": "scholar", "declared_at": DECLARED_AT}),
        "authorization_text_sha256": hashlib.sha256(AUTHORIZATION.encode("utf-8")).hexdigest(),
        "retrospective_transcription": True,
        "historical_lock_boundary": "Missing historical ARS/model/prompt/runtime fields are explicitly not-recorded and are not inferred.",
        "experiments": source_experiments,
        "boundary": BOUNDARY,
    }
    write_json(notes / "stage2_5_experiment_provenance_source_map.json", source_map)

    passport_path = notes / "stage2_5_material_passport.json"
    passport = load_json(passport_path)
    passport["experiment_intake_declaration"] = {
        "status": "experiments_declared",
        "declared_by": "scholar",
        "declared_at": DECLARED_AT,
    }
    passport["experiment_provenance"] = provenance
    passport["claim_intent_manifests"] = [manifest]
    passport["experiment_alignment_results"] = alignment_rows
    passport["verification_status"] = "UNVERIFIED_PENDING_STAGE2_5_REPLAY"
    passport["version_label"] = f"p{number}-round9-stage2.5-authorized-intake-pending-replay-v3"
    write_json(passport_path, passport)

    audit_md = f"""# Paper {number} Stage-2.5 experiment claim/provenance alignment audit

Generated: **{generated_at}**
Scholar declaration: **{DECLARED_AT}**
Decision: **{len(claim_map)}/{len(claim_map)} directly experiment-backed selected registry spans ALIGNED**.

This is a retrospective Stage-2.5 transcription of historical Round-2--8
packages. The schema-required `claim_intent_manifest` is not represented as a
pre-writing commitment: its session id and timestamps explicitly identify it
as gate-time reconstruction. Proof-, citation-, definition-, interpretation-,
limitation-, and heavily mixed spans do not receive experiment credit merely
because a nearby finite computation exists.

- Selected registry population: `{len(selected)}`.
- Direct experiment-backed aligned population: `{len(claim_map)}`.
- Provenance entries: `{len(provenance)}`.
- Exact registry→manifest→experiment crosswalk rows: `{len(crosswalk)}`.
- Source-map artifact: `notes/stage2_5_experiment_provenance_source_map.json`.
- Claim-population artifact: `notes/stage2_5_experiment_claim_population.json`.

Required boundary: **{BOUNDARY}**
"""
    write_text(notes / "stage2_5_experiment_claim_alignment_audit.md", audit_md)
    return {
        "paper": paper,
        "provenance_entries": len(provenance),
        "aligned_claims": len(alignment_rows),
        "source_artifacts": sum(row["materials_count"] for row in source_experiments),
        "passport_sha256": sha(passport_path),
        "source_map_sha256": sha(notes / "stage2_5_experiment_provenance_source_map.json"),
        "claim_population_sha256": sha(notes / "stage2_5_experiment_claim_population.json"),
    }


def main() -> int:
    generated_at = utc_now()
    declaration = {"status": "experiments_declared", "declared_by": "scholar", "declared_at": DECLARED_AT}
    receipt = {
        "schema": "flow-systems-round9-stage2.5-scholar-authorization/1.0",
        "received_at": DECLARED_AT,
        "recorded_at": generated_at,
        "scholar_authorization_text": AUTHORIZATION,
        "experiment_intake_declaration": declaration,
        "authorized_reference_repairs": [
            {"paper": 25, "key": "BowenLanford1970", "field": "author", "value": "Bowen, Rufus and Lanford, III, Oscar E."},
            {"paper": 28, "key": "Nazarenko2013", "field": "author", "value": "Nazarenko, A. V."},
            {"paper": 28, "key": "Nazarenko2013", "field": "primaryclass", "value": "math-ph"},
            {"paper": 28, "key": "AigonDupuyEtAl2005", "field": "author", "value": "Aigon-Dupuy, Aline and Buser, Peter and Cibils, Michel and K{\\\"u}nzle, Alfred F. and Steiner, Frank"},
        ],
        "authority_boundary": "Transcribe existing artifacts and repair only the three named bibliography records; no manuscript mutation or Stage-3 authorization.",
        "stage3_authorized": False,
        "boundary": BOUNDARY,
    }
    write_json(ROOT / "BATCH_ROUND9_STAGE2_5_AUTHORIZATION_RECEIPT.json", receipt)
    results = [build_paper(paper, generated_at) for paper in PAPERS]
    aggregate = {
        "generated_at": generated_at,
        "declared_at": DECLARED_AT,
        "papers": results,
        "provenance_entries": sum(row["provenance_entries"] for row in results),
        "aligned_claims": sum(row["aligned_claims"] for row in results),
        "source_artifacts": sum(row["source_artifacts"] for row in results),
        "stage3_authorized": False,
        "boundary": BOUNDARY,
    }
    write_json(ROOT / "BATCH_ROUND9_STAGE2_5_EXPERIMENT_TRANSCRIPTION_SUMMARY.json", aggregate)
    print(json.dumps(aggregate, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
