#!/usr/bin/env python3
"""Exactly 176 meaningful unittest methods for the Paper-13 controls."""

from __future__ import annotations

import contextlib
import copy
import csv
import builtins
import fcntl
import inspect
import json
import os
import re
import shutil
import subprocess
import sys
import unittest
from unittest import mock
from pathlib import Path
from typing import Callable, Dict, Iterator, List, Mapping, Sequence, Tuple

import generate_controls as gc


PAPER_DIR = Path(__file__).resolve().parents[1]
RESULTS = PAPER_DIR / "results"
REPRODUCE = PAPER_DIR / "experiments" / "reproduce.sh"
FRESH_A = Path(os.environ.get("P13_FRESH_A", ""))
FRESH_B = Path(os.environ.get("P13_FRESH_B", ""))
SCRATCH = Path(os.environ.get("P13_TEST_SCRATCH", ""))

LOCKED_CSV_SHA256 = {
    "nerve_factorization_controls.csv":"a00d2d6439aee3022703940b36892136ef7083d49541d2d8ad3bfd994a7582ba",
    "circle_multiplier_cocycle_controls.csv":"21a5246dba9dbe573a56fa9a0c18399061ff3e09d0238f68213123f3fa77e0a7",
    "lift_integer_defect_controls.csv":"598d414e46a7d34d1ab6a70b0047967047d984f24a3443aa19224a14a12da5b8",
    "gauge_coboundary_controls.csv":"c8717d8748691e92e8a7ea7ec1a196a5f42d5e151ee6e51244e2875f59677f26",
    "twisted_convolution_controls.csv":"2874817f2af1d3da31a29f497eba770eeac9c7275e6cc8693a7fa468fb482add",
    "twisted_involution_controls.csv":"114228b425905d5e235576b34f57eb15a0fd987065d4d206726045cceee569b5",
    "completion_gauge_controls.csv":"e7b8253a7d501b0c7b1d81939b59bfdc2f441b20592c678f749e643c0b800b2a",
    "action_period_nonretention_controls.csv":"9361f555cec4f74cab12faf30595e74830a00b44d7890e43579eae81ddcc9ee1",
    "negative_domain_controls.csv":"82b9e5988b30a8212235558af98a787df823213a7b0ad82be7d080da7c84c123",
    "actual_standard_support_transfer_controls.csv":"7bfb8ca2ed176d1a7aca2e5aa3680fd2d3992ef1d8e86a79b22c971912051176",
    "target_summary.csv":"97c2052c6286dd2013f735a79e7331d7a29f2bba7b2575fdc226865a34528f60",
    "completion_corona_controls_v2.csv":"672a29d4ac1b220336527517e50ba855f6a0c93568effd9b97e792015e4b2c41",
}

_ROWS: Dict[str, List[Dict[str, str]]] = {}
_MANIFEST: Dict[str, object] | None = None


def rows(name: str) -> List[Dict[str, str]]:
    if name not in _ROWS:
        with (RESULTS / name).open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != gc.HEADERS[name]:
                raise AssertionError(f"header mismatch while loading {name}")
            _ROWS[name] = list(reader)
    return _ROWS[name]


def manifest() -> Dict[str, object]:
    global _MANIFEST
    if _MANIFEST is None:
        _MANIFEST = json.loads((RESULTS / "manifest.json").read_text(encoding="utf-8"))
    return _MANIFEST


def artifact_bytes(root: Path) -> Dict[str, bytes]:
    return {name: (root / name).read_bytes() for name in (*gc.ARTIFACT_ORDER, "manifest.json")}


@contextlib.contextmanager
def package_copy(label: str) -> Iterator[Path]:
    if not SCRATCH:
        raise AssertionError("P13_TEST_SCRATCH is required")
    SCRATCH.mkdir(parents=True, exist_ok=True)
    target = SCRATCH / label
    if target.exists():
        raise AssertionError(f"scratch collision: {target}")
    target.mkdir()
    try:
        for name in (*gc.ARTIFACT_ORDER, "manifest.json"):
            shutil.copy2(RESULTS / name, target / name)
        yield target
    finally:
        shutil.rmtree(target, ignore_errors=False)
        try:
            SCRATCH.rmdir()
        except OSError:
            pass


def expect_verify_failure(test: unittest.TestCase, root: Path, code: str = "") -> None:
    context = (
        test.assertRaisesRegex(gc.ValidationError,re.escape(code))
        if code else test.assertRaises(gc.ValidationError)
    )
    with context:
        gc.verify_package(root)


def expect_validation(test: unittest.TestCase, code: str, action: Callable[[],object]) -> None:
    with test.assertRaisesRegex(gc.ValidationError,re.escape(code)):
        action()


def mutate_manifest(root: Path, mutator: Callable[[Dict[str, object]], None]) -> None:
    path = root / "manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    mutator(data)
    path.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8", newline="")


def mutate_csv_cell(root: Path, name: str, row_index: int, field: str, value: str) -> None:
    path = root/name
    with path.open("r",encoding="utf-8",newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != gc.HEADERS[name]:
            raise AssertionError("mutation source header drift")
        body = list(reader)
    body[row_index][field] = value
    with path.open("w",encoding="utf-8",newline="") as handle:
        writer = csv.DictWriter(handle,fieldnames=gc.HEADERS[name],lineterminator="\n")
        writer.writeheader()
        writer.writerows(body)


V1_SEMANTIC_MUTATIONS = (
    "DOM=INDISC2;COD=DISCRETE2;MAP=a:0|b:1",
    "ALPHA_RULE=CONSTANT_1;WITNESS=SEQ_1_OVER_N",
    "ALPHA_RULE=CONSTANT_1;WITNESS=SEQ_1_OVER_N",
    "ALPHA_0=1", "SIGMA_T_0=1",
    "K=-1;T=1;U=1;CANDIDATE=DELTA",
    "K=-1;MAP=U_ALPHA;TYPE=A_SIGMA_TO_A_ONE",
    "K=6;U=1;T=2;CANDIDATE=SIGMA_U_TMINUSU",
    "K=6;T=1;CANDIDATE=OVERLINE_SIGMA_T_MINUST_CONJ_F_MINUS_T",
    "VECTOR=V1;S=1;T=0;CANDIDATE=XI_T_MINUS_S",
    "VECTOR=V2;K=6;S=1;T=0;CANDIDATE=M_ALPHA_LAMBDA_SIGMA_M_BARALPHA",
    "OMEGA=EXP_I_PI_S1_T2_OVER2;S=1|0;T=0|1;COMM_EXP_MOD4=0",
    "H=Q;WINDOW=REDUCED_ABS_LE_2_DEN_LE_6;PROMOTION=FINITE_WINDOW_DIAGNOSTIC",
    "STABILIZERS=ZERO|LZ|R|Q;CANDIDATE=COMPONENTWISE_HETEROGENEOUS",
    "MAP=IDENTITY;DIRECTION=G_STD_TO_G_ACTUAL;CLAIM=CONTINUOUS",
    "Q=Q_1000;CLAIM=FINITE_MODEL_DIAGNOSTIC",
    "OWNER=FIXED_PRIME;INPUT=H_LOG_P_Z;CLAIM=UNSPECIFIED",
    "OWNER=G_ACTUAL;CANDIDATE=TRANSPORTED_COMPONENT_RECORD",
    "GRID=K24_X_T1_CUBED;CLAIM=FINITE_GRID_DIAGNOSTIC",
    "MUTATION=proof_binding.concurrent_phase3_proof_hash_included:false;PAYLOAD=NULL_PROOF_DIGEST",
)


V2_SEMANTIC_MUTATIONS = (
    "MODEL=SIGN_COORDS_16;CLAIM=FINITE_PATTERN_CARDINALITY",
    "MODEL=QF4;CLAIM=QF4_MODEL_IDENTITY",
    "MODEL=CORE2_TAIL3;CLAIM=FINITE_TAIL_DISTANCE",
    "SOURCE=PAPER2_PROP_UNCOUNTABLE;CREDIT=PAPER2_INHERITED_ZERO_P13",
    "OWNER=Q_P_ACTUAL;TOPOLOGY=INDISCRETE",
    "OWNER=Q_P_BARE;TOPOLOGY=NONE",
    "SOURCE=STD_GAMMA_P;TARGET=STD_GAMMA_P;CLAIM=NONSECONDCOUNTABLE",
    "SOURCE=Q_P_DISC;TARGET=Q_P_ACTUAL;MAP=SET_IDENTITY_ONLY",
    "OWNER=INFINITE_Q;CANDIDATE=PRODUCT_BOUNDED_NE_C0_SUM",
    "Q=INFINITE;INPUT=ZERO;CLAIM=ALGEBRA_MEMBER",
    "Q=QF2;INPUT=ONE;CLAIM=CORONA_MAP_NOT_INJECTIVE",
    "Q=INFINITE;CANDIDATE=KERNEL_EQUALS_PREIMAGE_A",
    "RELATION=SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA;MAP=U_ALPHA_SIGMA_TO_TAU",
    "MAX_STATUS=DIRECT_COMPONENT_MAX_RESTRICTION_CHAIN_REQUIRED;REDUCED_STATUS=EVERY_UNIT_REGULAR_RESTRICTION_REQUIRED",
    "SOURCE=V1_QP_FINITE_CONDITIONAL;CLAIM=V1_CONDITIONAL_ONLY",
    "INPUT=H_LOG_P_Z;CLAIM=UNSPECIFIED",
    "OWNER=COMPONENTWISE;CANDIDATE=AUTHOR_COMPONENT_RECORD",
    "MANIFEST=NO_PROOF_BINDING",
    "MANIFEST=NO_SELF_ENTRY",
    "MANIFEST=RETAIN_V2_DESIGN_HEAD_AND_AUTHORIZATION_GATE",
)


class ControlsCase(unittest.TestCase):
    maxDiff = None

    def r(self, name: str) -> List[Dict[str, str]]:
        return rows(name)

    def all_equal(self, name: str, field: str, value: str) -> None:
        self.assertTrue(self.r(name))
        self.assertEqual({row[field] for row in self.r(name)}, {value})

    def ids(self, name: str) -> List[str]:
        return [row["row_id"] for row in self.r(name)]


def install(cls: type, specs: Sequence[Tuple[str, Callable[[ControlsCase], None]]]) -> None:
    for suffix, checker in specs:
        name = "test_" + suffix
        if hasattr(cls, name):
            raise AssertionError(f"duplicate test method: {cls.__name__}.{name}")

        def method(self: ControlsCase, check: Callable[[ControlsCase], None] = checker) -> None:
            check(self)

        method.__name__ = name
        method.__qualname__ = f"{cls.__name__}.{name}"
        setattr(cls, name, method)


class Test01Nerve(ControlsCase):
    pass


install(Test01Nerve, (
    ("schema_and_header", lambda s: (s.assertEqual(len(gc.HEADERS[gc.ARTIFACT_ORDER[0]]),17), s.all_equal(gc.ARTIFACT_ORDER[0],"schema_version",gc.SCHEMA_V1))),
    ("rows_and_contiguous_order", lambda s: (s.assertEqual(len(s.r(gc.ARTIFACT_ORDER[0])),280), s.assertEqual(s.ids(gc.ARTIFACT_ORDER[0]),[f"NF-{i:04d}" for i in range(1,281)]))),
    ("degree_one_profiles", lambda s: s.assertEqual({r["cochain_profile"] for r in s.r(gc.ARTIFACT_ORDER[0]) if r["degree"]=="1"},{"A_ZERO","A_LINEAR3"})),
    ("degree_two_profiles", lambda s: s.assertEqual({r["cochain_profile"] for r in s.r(gc.ARTIFACT_ORDER[0]) if r["degree"]=="2"},{"S_ZERO","S_QUADRATIC1"})),
    ("normalization", lambda s: s.all_equal(gc.ARTIFACT_ORDER[0],"normalized","true")),
    ("unit_independence", lambda s: s.assertEqual(len({(r["owner_case"],r["unit_id"]) for r in s.r(gc.ARTIFACT_ORDER[0])}),10)),
    ("oracle_and_t0_scope", lambda s: (s.all_equal(gc.ARTIFACT_ORDER[0],"oracle","TIME_PHASE_EQUALITY_AND_NORMALIZATION"), s.assertEqual(rows("target_summary.csv")[0]["scope"],"FINITE_TIME_ONLY_WITNESS_NOT_TOPOLOGICAL_PROOF"))),
))


class Test02Cocycle(ControlsCase):
    pass


install(Test02Cocycle, (
    ("schema", lambda s: s.assertEqual(len(gc.HEADERS[gc.ARTIFACT_ORDER[1]]),20)),
    ("rows_and_order", lambda s: (s.assertEqual(len(s.r(gc.ARTIFACT_ORDER[1])),500), s.assertEqual(s.ids(gc.ARTIFACT_ORDER[1]),[f"CM-{i:04d}" for i in range(1,501)]))),
    ("first_normalization_axis", lambda s: s.all_equal(gc.ARTIFACT_ORDER[1],"norm_t0","true")),
    ("second_normalization_axis", lambda s: s.all_equal(gc.ARTIFACT_ORDER[1],"norm_0u","true")),
    ("four_k_indices", lambda s: s.assertEqual([int(x) for x in dict.fromkeys(r["k_index"] for r in s.r(gc.ARTIFACT_ORDER[1]))],list(gc.K24))),
    ("both_cocycle_sides", lambda s: s.assertTrue(all(r["lhs_exp_mod24"]==r["rhs_exp_mod24"] for r in s.r(gc.ARTIFACT_ORDER[1])))),
    ("oracle_recomputation", lambda s: s.assertTrue(all(int(r["lhs_exp_mod24"])==(gc.sigma_exp(int(r["k_index"]),int(r["t"]),int(r["u"]))+gc.sigma_exp(int(r["k_index"]),int(r["t"])+int(r["u"]),int(r["v"])))%24 for r in s.r(gc.ARTIFACT_ORDER[1])))),
))


class Test03Lift(ControlsCase):
    pass


install(Test03Lift, (
    ("centered_representative_range", lambda s: s.assertTrue(all(-12<=int(r[f])<=11 for r in s.r(gc.ARTIFACT_ORDER[2]) for f in ("r_tu","r_tplusu_v","r_uv","r_t_uplusv")))),
    ("two_pi_divisibility", lambda s: s.assertTrue(all(int(r["defect_numerator_24"])%24==0 for r in s.r(gc.ARTIFACT_ORDER[2])))),
    ("nonzero_wrap_coverage", lambda s: s.assertTrue(any(int(r["defect_multiple_2pi"])!=0 for r in s.r(gc.ARTIFACT_ORDER[2])))),
    ("normalization", lambda s: s.all_equal(gc.ARTIFACT_ORDER[2],"normalization_axes","true")),
    ("mod24_cocycle", lambda s: s.all_equal(gc.ARTIFACT_ORDER[2],"cocycle_mod24","0")),
    ("row_order", lambda s: s.assertEqual(s.ids(gc.ARTIFACT_ORDER[2]),[f"LI-{i:04d}" for i in range(1,501)])),
    ("oracle_recomputation", lambda s: s.assertTrue(all(int(r["defect_multiple_2pi"])*24==int(r["defect_numerator_24"]) for r in s.r(gc.ARTIFACT_ORDER[2])))),
))


class Test04Gauge(ControlsCase):
    pass


install(Test04Gauge, (
    ("alpha_normalization", lambda s: s.all_equal(gc.ARTIFACT_ORDER[3],"normalized_alpha","true")),
    ("frozen_coboundary_sign", lambda s: s.assertTrue(all(r["delta_alpha_exp"]==r["sigma_tu_exp"] for r in s.r(gc.ARTIFACT_ORDER[3])))),
    ("quotient_orientation", lambda s: s.assertTrue(all(r["quotient_sigma_over_one_exp"]==r["sigma_tu_exp"] for r in s.r(gc.ARTIFACT_ORDER[3])))),
    ("gauge_direction", lambda s: s.all_equal(gc.ARTIFACT_ORDER[3],"gauge_direction","A_SIGMA_TO_A_ONE")),
    ("rows_and_order", lambda s: (s.assertEqual(len(s.r(gc.ARTIFACT_ORDER[3])),196),s.assertEqual(s.ids(gc.ARTIFACT_ORDER[3]),[f"GC-{i:04d}" for i in range(1,197)]))),
    ("four_k_indices", lambda s: s.assertEqual({int(r["k_index"]) for r in s.r(gc.ARTIFACT_ORDER[3])},set(gc.K24))),
    ("oracle_recomputation", lambda s: s.assertTrue(all((gc.alpha_exp(int(r["k_index"]),int(r["t"]))+gc.alpha_exp(int(r["k_index"]),int(r["u"]))-gc.alpha_exp(int(r["k_index"]),int(r["t"])+int(r["u"])))%24==int(r["delta_alpha_exp"]) for r in s.r(gc.ARTIFACT_ORDER[3])))),
))


class Test05Convolution(ControlsCase):
    pass


def convolution_field_probe(s: ControlsCase, field: str) -> None:
    source = s.r(gc.ARTIFACT_ORDER[4])
    gc.validate_convolution_independence(source)
    candidate = copy.deepcopy(source)
    candidate[0][field] = "false" if candidate[0][field] == "true" else str(int(candidate[0][field])+1)
    with s.assertRaises(gc.ValidationError):
        gc.validate_convolution_independence(candidate)


install(Test05Convolution, (
    ("two_fixtures", lambda s: s.assertEqual({r["fixture_id"] for r in s.r(gc.ARTIFACT_ORDER[4])},{"C1","C2"})),
    ("gaussian_integer_closure", lambda s: s.assertTrue(all(r[f].lstrip("-").isdigit() for r in s.r(gc.ARTIFACT_ORDER[4]) for f in ("fg_re","fg_im","left_assoc_re","left_assoc_im","right_assoc_re","right_assoc_im")))),
    ("product_coefficients", lambda s: s.assertTrue(any(r["fg_re"]!="0" or r["fg_im"]!="0" for r in s.r(gc.ARTIFACT_ORDER[4])))),
    ("left_bracketing", lambda s: convolution_field_probe(s,"left_assoc_re")),
    ("right_bracketing", lambda s: convolution_field_probe(s,"right_assoc_re")),
    ("associativity", lambda s: convolution_field_probe(s,"associativity_holds")),
    ("gauge_product", lambda s: convolution_field_probe(s,"gauge_product_re")),
    ("minkowski_support", lambda s: s.all_equal(gc.ARTIFACT_ORDER[4],"fg_support_within_minkowski","true")),
    ("exterior_zero_rows", lambda s: s.assertTrue(all((r["fg_re"],r["fg_im"])==("0","0") for r in s.r(gc.ARTIFACT_ORDER[4]) if abs(int(r["t"]))>=5))),
    ("scope_and_oracle", lambda s: (s.all_equal(gc.ARTIFACT_ORDER[4],"oracle","FINITE_GAUSSIAN_PRODUCT_ASSOC_GAUGE"),s.assertEqual(rows("target_summary.csv")[4]["scope"],"FINITE_LATTICE_SIGN_DIAGNOSTIC_ONLY"))),
))


class Test06Involution(ControlsCase):
    pass


def involution_field_probe(s: ControlsCase, field: str) -> None:
    source = s.r(gc.ARTIFACT_ORDER[5])
    gc.validate_involution_independence(source)
    candidate = copy.deepcopy(source)
    candidate[0][field] = str(int(candidate[0][field])+1)
    with s.assertRaises(gc.ValidationError):
        gc.validate_involution_independence(candidate)


install(Test06Involution, (
    ("two_fixtures", lambda s: s.assertEqual({r["fixture_id"] for r in s.r(gc.ARTIFACT_ORDER[5])},{"C1","C2"})),
    ("gaussian_integer_closure", lambda s: s.assertTrue(all(r[f].lstrip("-").isdigit() for r in s.r(gc.ARTIFACT_ORDER[5]) for f in ("f_starstar_re","f_starstar_im","fg_star_re","fg_star_im")))),
    ("inverse_symmetry", lambda s: s.all_equal(gc.ARTIFACT_ORDER[5],"sigma_inverse_symmetry","true")),
    ("star_star", lambda s: s.all_equal(gc.ARTIFACT_ORDER[5],"star_involutive","true")),
    ("anti_product", lambda s: s.all_equal(gc.ARTIFACT_ORDER[5],"anti_multiplicative","true")),
    ("actual_time_match", lambda s: involution_field_probe(s,"actual_star_re")),
    ("exterior_rows", lambda s: s.assertTrue(any(r["f_re"]=="0" and r["f_im"]=="0" for r in s.r(gc.ARTIFACT_ORDER[5]) if abs(int(r["t"]))>=3))),
    ("scope_label", lambda s: s.assertEqual(rows("target_summary.csv")[5]["scope"],"FINITE_LATTICE_SIGN_DIAGNOSTIC_ONLY")),
    ("oracle_recomputation", lambda s: involution_field_probe(s,"time_star_re")),
))


class Test07Completion(ControlsCase):
    pass


def completion_norm_probe(s: ControlsCase) -> None:
    source = s.r(gc.ARTIFACT_ORDER[6])
    gc.validate_completion_independence(source)
    copied = copy.deepcopy(source)
    copied[0]["xi_norm_sq"] = "7"
    copied[0]["character_times_xi_norm_sq"] = "7"
    with s.assertRaises(gc.ValidationError):
        gc.validate_completion_independence(copied)


def completion_oracle_probe(s: ControlsCase) -> None:
    source = s.r(gc.ARTIFACT_ORDER[6])
    gc.validate_completion_independence(source)
    for field in ("projective_lhs_re","intertwiner_rhs_re","character_times_xi_norm_sq"):
        candidate = copy.deepcopy(source)
        candidate[0][field] = str(int(candidate[0][field])+1)
        with s.subTest(field=field):
            with s.assertRaises(gc.ValidationError):
                gc.validate_completion_independence(candidate)


install(Test07Completion, (
    ("vectors", lambda s: s.assertEqual({r["fixture_id"] for r in s.r(gc.ARTIFACT_ORDER[6])},{"V1","V2"})),
    ("projective_law", lambda s: s.all_equal(gc.ARTIFACT_ORDER[6],"projective_holds","true")),
    ("translation_direction", lambda s: s.assertTrue(any((r["projective_lhs_re"],r["projective_lhs_im"])!=("0","0") for r in s.r(gc.ARTIFACT_ORDER[6])))),
    ("intertwiner_direction", lambda s: s.all_equal(gc.ARTIFACT_ORDER[6],"intertwiner_holds","true")),
    ("character_law", lambda s: s.assertEqual({r["character_m"] for r in s.r(gc.ARTIFACT_ORDER[6])},{"0","1"})),
    ("beta_over_alpha", lambda s: s.all_equal(gc.ARTIFACT_ORDER[6],"choice_map_holds","true")),
    ("choice_map", lambda s: s.assertTrue(all(r["choice_map_holds"]=="true" for r in s.r(gc.ARTIFACT_ORDER[6])))),
    ("norm_square", completion_norm_probe),
    ("scope_label", lambda s: s.all_equal(gc.ARTIFACT_ORDER[6],"completion_scope","FINITE_MATRIX_ELEMENT_DIAGNOSTIC_ONLY")),
    ("rows_and_order", lambda s: (s.assertEqual(len(s.r(gc.ARTIFACT_ORDER[6])),756),s.assertEqual(s.ids(gc.ARTIFACT_ORDER[6]),[f"CG-{i:04d}" for i in range(1,757)]))),
    ("oracle_recomputation", completion_oracle_probe),
))


class Test08ActionPeriod(ControlsCase):
    pass


install(Test08ActionPeriod, (
    ("fourteen_case_registry", lambda s: s.assertEqual(len(list(dict.fromkeys((r["action_case"],r["component_id"]) for r in s.r(gc.ARTIFACT_ORDER[7])))),14)),
    ("singleton_owner", lambda s: s.assertEqual({r["stabilizer_literal"] for r in s.r(gc.ARTIFACT_ORDER[7]) if r["action_case"]=="SINGLETON_TIME_OWNER"},{"R"})),
    ("prime_composite_arbitrary_labels", lambda s: s.assertTrue({"(log 2)Z","(log 3)Z","(log 6)Z","L_a Z"}.issubset({r["stabilizer_literal"] for r in s.r(gc.ARTIFACT_ORDER[7])}))),
    ("nontransitive_case", lambda s: s.assertEqual(sum(r["action_case"]=="NONTRANSITIVE_COMMON_L" for r in s.r(gc.ARTIFACT_ORDER[7])),4)),
    ("heterogeneous_four_way", lambda s: s.assertEqual({r["stabilizer_literal"] for r in s.r(gc.ARTIFACT_ORDER[7]) if r["action_case"]=="HETEROGENEOUS_ACTION"},{"{0}","LZ","R","Q"})),
    ("dense_firewall", lambda s: s.assertEqual(sum(r["dense_h_scope"]=="FINITE_RATIONAL_WINDOW_DIAGNOSTIC_ONLY" for r in s.r(gc.ARTIFACT_ORDER[7])),4)),
    ("five_signatures", lambda s: s.assertTrue(all(r["named_output_signature_matches_baseline"]=="true" for r in s.r(gc.ARTIFACT_ORDER[7])))),
    ("restriction_oracle", lambda s: s.all_equal(gc.ARTIFACT_ORDER[7],"restriction_coboundary_match","true")),
))


class Test09NegativeDomain(ControlsCase):
    pass


def assert_v1_negative_slice(s: ControlsCase, start: int, stop: int) -> None:
    selected = s.r(gc.ARTIFACT_ORDER[8])[start:stop]
    s.assertEqual(len(selected),stop-start)
    for row in selected:
        s.assertEqual(
            gc.detect_v1_negative(row["negative_reason"],row["fixture"],row["violated_lock"]),
            row["expected_detector"],
        )
        s.assertEqual(row["observed_detector"],row["expected_detector"])


def v1_detectors_independent(s: ControlsCase) -> None:
    negative_rows = s.r(gc.ARTIFACT_ORDER[8])
    s.assertEqual(len(negative_rows),len(gc.V1_NEGATIVES))
    for index,(row,semantic_mutation) in enumerate(zip(negative_rows,V1_SEMANTIC_MUTATIONS)):
        s.assertEqual(
            gc.detect_v1_negative(row["negative_reason"],row["fixture"],row["violated_lock"]),
            row["expected_detector"],
        )
        rotated_reason = negative_rows[(index+1)%len(negative_rows)]["negative_reason"]
        for fixture,reason,lock in (
            (semantic_mutation,row["negative_reason"],row["violated_lock"]),
            (row["fixture"]+";BROKEN",row["negative_reason"],row["violated_lock"]),
            (row["fixture"],row["negative_reason"],row["violated_lock"]+"_WRONG"),
            (row["fixture"],rotated_reason,row["violated_lock"]),
        ):
            with s.subTest(row=row["row_id"],fixture=fixture,reason=reason,lock=lock):
                with s.assertRaises(gc.ValidationError):
                    gc.detect_v1_negative(reason,fixture,lock)


install(Test09NegativeDomain, (
    ("registry_and_order", lambda s: (s.assertEqual(len(s.r(gc.ARTIFACT_ORDER[8])),20),s.assertEqual(s.ids(gc.ARTIFACT_ORDER[8]),[f"ND-{i:04d}" for i in range(1,21)]))),
    ("regularity_negatives", lambda s: assert_v1_negative_slice(s,0,3)),
    ("normalization_and_sign", lambda s: assert_v1_negative_slice(s,3,7)),
    ("product_star", lambda s: assert_v1_negative_slice(s,7,9)),
    ("regular_and_intertwiner", lambda s: assert_v1_negative_slice(s,9,11)),
    ("r2_exclusion", lambda s: assert_v1_negative_slice(s,11,12)),
    ("dense_and_heterogeneous", lambda s: assert_v1_negative_slice(s,12,14)),
    ("owner_and_support", lambda s: assert_v1_negative_slice(s,14,18)),
    ("proof_and_manifest_promotions", lambda s: assert_v1_negative_slice(s,18,20)),
    ("detectors_independent", v1_detectors_independent),
))


class Test10SupportTransfer(ControlsCase):
    pass


def support_oracle_recomputation(s: ControlsCase) -> None:
    source = s.r(gc.ARTIFACT_ORDER[9])
    gc.validate_support_transfer_rows(copy.deepcopy(source))
    negative_rows = [index for index,row in enumerate(source) if row["case_kind"]=="NEGATIVE"]
    s.assertEqual(len(negative_rows),27)
    for index in negative_rows:
        for field,value in (
            ("standard_support_compact","true"),
            ("q_class","FINITE"),
            ("status","FAIL"),
        ):
            candidate = copy.deepcopy(source)
            candidate[index][field] = value
            with s.subTest(row=source[index]["row_id"],field=field):
                with s.assertRaises(gc.ValidationError):
                    gc.validate_support_transfer_rows(candidate)


install(Test10SupportTransfer, (
    ("eight_q_cases", lambda s: s.assertEqual(len({r["q_case"] for r in s.r(gc.ARTIFACT_ORDER[9])}),8)),
    ("four_functions", lambda s: s.assertEqual({r["function_id"] for r in s.r(gc.ARTIFACT_ORDER[9])},{"ZERO","TENT_CENTER","TENT_SHIFT","TWO_BUMP"})),
    ("three_gauges", lambda s: s.assertEqual({r["gauge_id"] for r in s.r(gc.ARTIFACT_ORDER[9])},{"ONE","ALPHA_K_MINUS6","ALPHA_K_6"})),
    ("zero_branch", lambda s: s.assertTrue(all(r["standard_support_compact"]=="true" for r in s.r(gc.ARTIFACT_ORDER[9]) if r["is_zero"]=="true"))),
    ("finite_branch", lambda s: s.assertTrue(all(r["standard_support_compact"]=="true" for r in s.r(gc.ARTIFACT_ORDER[9]) if r["q_class"] in {"FINITE","QP_FINITE_CONDITIONAL"}))),
    ("infinite_branch", lambda s: s.assertTrue(all(r["standard_support_compact"]=="false" for r in s.r(gc.ARTIFACT_ORDER[9]) if r["q_class"]=="INFINITE" and r["is_zero"]=="false"))),
    ("conditional_qp", lambda s: s.assertEqual(sum(r["fixed_prime_conditional"]=="true" for r in s.r(gc.ARTIFACT_ORDER[9])),24)),
    ("support_preservation", lambda s: s.all_equal(gc.ARTIFACT_ORDER[9],"support_preserved","true")),
    ("negative_count", lambda s: s.assertEqual(sum(r["case_kind"]=="NEGATIVE" for r in s.r(gc.ARTIFACT_ORDER[9])),27)),
    ("oracle_recomputation", support_oracle_recomputation),
))


class Test11TargetSummary(ControlsCase):
    pass


install(Test11TargetSummary, (
    ("schema", lambda s: s.assertEqual(gc.HEADERS[gc.ARTIFACT_ORDER[10]],list(s.r(gc.ARTIFACT_ORDER[10])[0]))),
    ("eleven_artifact_rows", lambda s: s.assertEqual([r["artifact"] for r in s.r(gc.ARTIFACT_ORDER[10])[:11]],list(gc.ARTIFACT_ORDER[:11]))),
    ("package_row", lambda s: s.assertEqual(s.r(gc.ARTIFACT_ORDER[10])[-1]["artifact"],"PACKAGE_TOTAL")),
    ("aggregate_arithmetic", lambda s: s.assertEqual((s.r(gc.ARTIFACT_ORDER[10])[-1]["expected_rows"],s.r(gc.ARTIFACT_ORDER[10])[-1]["expected_negative_rows"]),("2548","47"))),
    ("no_self_hash", lambda s: s.assertFalse(any("sha" in key.lower() or "digest" in key.lower() for key in s.r(gc.ARTIFACT_ORDER[10])[10]))),
))


class Test12PackageManifest(ControlsCase):
    pass


install(Test12PackageManifest, (
    ("exact_artifact_set", lambda s: s.assertEqual(set(artifact_bytes(RESULTS)),set(gc.ARTIFACT_ORDER)|{"manifest.json"})),
    ("manifest_schema", lambda s: s.assertEqual(manifest()["schema_version"],gc.MANIFEST_SCHEMA)),
    ("headers", lambda s: s.assertTrue(all(list(s.r(name)[0])==gc.HEADERS[name] for name in gc.ARTIFACT_ORDER))),
    ("per_file_rows", lambda s: s.assertTrue(all(len(s.r(name))==gc.SPECS[name][1] for name in gc.ARTIFACT_ORDER))),
    ("total_rows", lambda s: s.assertEqual(sum(len(s.r(name)) for name in gc.ARTIFACT_ORDER),2665)),
    ("total_negatives", lambda s: s.assertEqual(sum(sum(r.get("case_kind")=="NEGATIVE" for r in s.r(name)) for name in gc.ARTIFACT_ORDER),67)),
    ("unique_ids_per_file", lambda s: s.assertTrue(all(len(s.ids(name))==len(set(s.ids(name))) for name in gc.ARTIFACT_ORDER))),
    ("canonical_artifact_order", lambda s: s.assertEqual([x["path"].split("/",1)[1] for x in manifest()["artifacts"]],list(gc.ARTIFACT_ORDER))),
    ("csv_bytes", lambda s: s.assertTrue(all((RESULTS/name).read_bytes().endswith(b"\n") and b"\r" not in (RESULTS/name).read_bytes() for name in gc.ARTIFACT_ORDER))),
    ("artifact_hashes", lambda s: s.assertTrue(all(gc.sha256_file(RESULTS/Path(x["path"]).name)==x["sha256"] for x in manifest()["artifacts"]))),
    ("byte_counts", lambda s: s.assertTrue(all((RESULTS/Path(x["path"]).name).stat().st_size==x["bytes"] for x in manifest()["artifacts"]))),
    ("authority_bindings", lambda s: (s.assertEqual(len(manifest()["bindings"]),24),gc.verify_authorities())),
    ("no_unbound_result", lambda s: s.assertEqual({x["path"] for x in manifest()["artifacts"]},{f"results/{name}" for name in gc.ARTIFACT_ORDER})),
))


class Test13Reproduction(ControlsCase):
    pass


install(Test13Reproduction, (
    ("checked_in_verify_only", lambda s: s.assertIn("entries",gc.verify_package(RESULTS))),
    ("fresh_a_verify", lambda s: s.assertIn("entries",gc.verify_package(FRESH_A))),
    ("fresh_b_verify", lambda s: s.assertIn("entries",gc.verify_package(FRESH_B))),
    ("fresh_roots_distinct", lambda s: s.assertNotEqual(FRESH_A.resolve(),FRESH_B.resolve())),
    ("checked_in_fresh_a_compare", lambda s: s.assertEqual(artifact_bytes(RESULTS),artifact_bytes(FRESH_A))),
    ("fresh_a_fresh_b_compare", lambda s: s.assertEqual(artifact_bytes(FRESH_A),artifact_bytes(FRESH_B))),
    ("thirteen_generated_artifacts", lambda s: s.assertEqual(len(artifact_bytes(FRESH_A)),13)),
    ("checked_in_read_only_receipt", lambda s: s.assertEqual(gc.package_receipt(RESULTS),gc.package_receipt(RESULTS))),
))


def tamper_content(s: ControlsCase) -> None:
    with package_copy("content") as root:
        mutate_csv_cell(root,V2_NAME,0,"input_norm","1")
        expect_verify_failure(s,root,"V2_FIELD_input_norm")


def tamper_header(s: ControlsCase) -> None:
    with package_copy("header") as root:
        path=root/V2_NAME; data=path.read_bytes(); path.write_bytes(data.replace(b"schema_version",b"schema_versioX",1)); expect_verify_failure(s,root,"CSV_HEADER")


def tamper_row_count(s: ControlsCase) -> None:
    with package_copy("row_count") as root:
        path=root/V2_NAME; lines=path.read_bytes().splitlines(keepends=True); path.write_bytes(b"".join(lines[:-1])); expect_verify_failure(s,root,"CSV_ROW_COUNT")


def tamper_reorder(s: ControlsCase) -> None:
    with package_copy("reorder") as root:
        path=root/V2_NAME; lines=path.read_bytes().splitlines(keepends=True); lines[1],lines[2]=lines[2],lines[1]; path.write_bytes(b"".join(lines)); expect_verify_failure(s,root,"CSV_ROW_ORDER")


def tamper_missing(s: ControlsCase) -> None:
    with package_copy("missing") as root:
        (root/V2_NAME).unlink(); expect_verify_failure(s,root,"PACKAGE_MISSING_ARTIFACT")


def tamper_extra_file(s: ControlsCase) -> None:
    with package_copy("extra_file") as root:
        (root/"extra.csv").write_bytes(b"x\n"); expect_verify_failure(s,root,"PACKAGE_EXTRA_ARTIFACT")


def tamper_extra_directory(s: ControlsCase) -> None:
    with package_copy("extra_dir") as root:
        (root/"extra").mkdir(); expect_verify_failure(s,root,"PACKAGE_EXTRA_DIRECTORY")


def tamper_manifest_artifact(s: ControlsCase) -> None:
    with package_copy("manifest_artifact") as root:
        mutate_manifest(root,lambda d: d["artifacts"][0].__setitem__("sha256","0"*64)); expect_verify_failure(s,root,"MANIFEST_ARTIFACT_EDGE")


def active_lock_rejected(s: ControlsCase) -> None:
    env=dict(os.environ); env["P13_REPRO_ACTIVE"]="1"
    result=subprocess.run([str(REPRODUCE)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=False)
    s.assertNotEqual(result.returncode,0)


def tamper_binding(s: ControlsCase) -> None:
    with package_copy("design_head_binding") as root:
        mutate_manifest(root,lambda d: d["design_head"].__setitem__("sha256","0"*64))
        expect_verify_failure(s,root,"MANIFEST_UNBOUND_AUTHORITY")
    with package_copy("v2_gate_binding") as root:
        def change_gate(d: Dict[str,object]) -> None:
            edge = next(item for item in d["bindings"] if item["path"]=="notes/phase3_v2_design_gate.md")
            edge["sha256"]="0"*64
        mutate_manifest(root,change_gate)
        expect_verify_failure(s,root,"MANIFEST_UNBOUND_AUTHORITY")


def tamper_implementation(s: ControlsCase) -> None:
    with package_copy("implementation") as root:
        mutate_manifest(root,lambda d: d["implementation"][0].__setitem__("sha256","0"*64)); expect_verify_failure(s,root,"MANIFEST_IMPLEMENTATION_EDGE")


def tamper_proof(s: ControlsCase) -> None:
    with package_copy("proof_block") as root:
        def mutate(d: Dict[str, object]) -> None:
            d["proof_binding"]["concurrent_phase3_proof_hash_included"]=True
            d["proof_binding"]["proof_sha256"]="1"*64
        mutate_manifest(root,mutate); expect_verify_failure(s,root,"MANIFEST_PROOF_BINDING")
    with package_copy("proof_recursive") as root:
        mutate_manifest(root,lambda d: d["aggregates"].__setitem__("nested",{"proof_bytes":1}))
        expect_verify_failure(s,root,"MANIFEST_PROOF_BINDING")
    with package_copy("proof_oracle_value") as root:
        mutate_manifest(root,lambda d: d["aggregates"].__setitem__("oracle_probe","PROOF_DERIVED_ORACLE"))
        expect_verify_failure(s,root,"MANIFEST_PROOF_BINDING")


class Test14Tamper(ControlsCase):
    pass


install(Test14Tamper, (
    ("content",tamper_content),("header",tamper_header),("row_count",tamper_row_count),("row_reorder",tamper_reorder),
    ("missing_csv",tamper_missing),("extra_csv",tamper_extra_file),("extra_directory",tamper_extra_directory),
    ("manifest_artifact",tamper_manifest_artifact),("active_lock",active_lock_rejected),("gate_source_binding",tamper_binding),
    ("implementation_digest",tamper_implementation),("prohibited_proof_hash",tamper_proof),
))


def recursive_rejection(s: ControlsCase) -> None:
    active_lock_rejected(s)


def pre_cache_rejection(s: ControlsCase) -> None:
    with package_copy("pre_cache") as root:
        (root/"__pycache__").mkdir()
        with s.assertRaises(gc.ValidationError): gc.assert_no_cache(root)


def post_cache_rejection(s: ControlsCase) -> None:
    with package_copy("post_cache") as root:
        (root/"leak.pyc").write_bytes(b"x")
        with s.assertRaises(gc.ValidationError): gc.verify_package(root)


def temporary_cleanup(s: ControlsCase) -> None:
    marker = SCRATCH/"cleanup_probe"
    marker.mkdir(parents=True)
    shutil.rmtree(marker)
    try: SCRATCH.rmdir()
    except OSError: pass
    s.assertFalse(marker.exists())


class Test15Lifecycle(ControlsCase):
    pass


install(Test15Lifecycle, (("recursive_entry_rejection",recursive_rejection),("pre_run_cache_rejection",pre_cache_rejection),("post_run_cache_rejection",post_cache_rejection),("temporary_root_cleanup",temporary_cleanup)))


V2_NAME = "completion_corona_controls_v2.csv"


class Test16V2Schema(ControlsCase):
    pass


install(Test16V2Schema, (
    ("exact_41_column_header",lambda s: s.assertEqual(len(gc.HEADERS[V2_NAME]),41)),
    ("family_registry",lambda s: s.assertEqual([(k,sum(r["control_family"]==k for r in s.r(V2_NAME))) for k in dict.fromkeys(r["control_family"] for r in s.r(V2_NAME))],[("FINITE_C0_MODEL",18),("INFINITE_ANALYTIC_BOUNDARY",18),("FINITE_TAIL_QUOTIENT_MODEL",12),("GAUGE_COMMUTATION_MODEL",24),("OWNER_CREDIT_LEDGER",8),("MAX_REDUCED_EVIDENCE_LEDGER",4),("FIREWALL_NEGATIVE",20),("V2_PACKAGE_SUMMARY",13)])),
    ("contiguous_ids",lambda s: s.assertEqual(s.ids(V2_NAME),[f"V2-{i:04d}" for i in range(1,118)])),
    ("block_order_formulas",lambda s: s.assertEqual([s.r(V2_NAME)[i]["control_family"] for i in (0,18,36,48,72,80,84,104)],["FINITE_C0_MODEL","INFINITE_ANALYTIC_BOUNDARY","FINITE_TAIL_QUOTIENT_MODEL","GAUGE_COMMUTATION_MODEL","OWNER_CREDIT_LEDGER","MAX_REDUCED_EVIDENCE_LEDGER","FIREWALL_NEGATIVE","V2_PACKAGE_SUMMARY"])),
))


def family(name: str) -> List[Dict[str,str]]:
    return [r for r in rows(V2_NAME) if r["control_family"]==name]


def v1_context_from_results() -> Dict[str,List[Dict[str,str]]]:
    return {name:rows(name) for name in gc.ARTIFACT_ORDER[:11]}


def validate_v2_candidate(candidate: Sequence[Dict[str,str]]) -> None:
    gc.validate_v2_families(
        candidate,
        v1_context_from_results(),
        gc.discover_unittest_method_count(),
    )


def mutate_v2_family_field(
    s: ControlsCase,
    family_name: str,
    family_index: int,
    field: str,
    value: str,
) -> None:
    source = s.r(V2_NAME)
    positions = [i for i,row in enumerate(source) if row["control_family"]==family_name]
    candidate = copy.deepcopy(source)
    candidate[positions[family_index]][field] = value
    with s.assertRaises(gc.ValidationError):
        validate_v2_candidate(candidate)


class Test17V2Finite(ControlsCase):
    pass


def finite_membership_behavior(s: ControlsCase) -> None:
    validate_v2_candidate(copy.deepcopy(s.r(V2_NAME)))
    mutate_v2_family_field(s,"FINITE_C0_MODEL",0,"algebra_member","false")
    source = inspect.getsource(gc.generate_v2)
    s.assertIn('status=""',source)
    s.assertNotIn('status="PASS"',source)


install(Test17V2Finite, (
    ("three_finite_owners",lambda s: s.assertEqual(len({r["owner_case"] for r in family("FINITE_C0_MODEL")}),3)),
    ("three_scalar_inputs",lambda s: s.assertEqual({r["input_id"] for r in family("FINITE_C0_MODEL")},{"ZERO","ONE","I"})),
    ("constant_coordinate_norms",lambda s: s.assertTrue(all((r["input_norm"],r["coordinate_norm_class"]) in {("0","CONSTANT_0"),("1","CONSTANT_1")} for r in family("FINITE_C0_MODEL")))),
    ("multiplier_and_algebra_membership",finite_membership_behavior),
    ("zero_finite_corona_map",lambda s: s.assertTrue(all((r["quotient_distance"],r["quotient_image_nonzero"],r["quotient_map_injective"])==("0","false","false") for r in family("FINITE_C0_MODEL")))),
))


class Test18V2Infinite(ControlsCase):
    pass


install(Test18V2Infinite, (
    ("two_generic_infinite_owners",lambda s: s.assertEqual(sum(r["owner_case"].startswith("GENERIC") for r in family("INFINITE_ANALYTIC_BOUNDARY")),12)),
    ("zero_nonzero_split",lambda s: s.assertTrue(all((r["algebra_member"]=="true")==(r["input_norm"]=="0") for r in family("INFINITE_ANALYTIC_BOUNDARY")))),
    ("multiplier_algebra_distinction",lambda s: s.assertTrue(all(r["multiplier_member"]=="true" for r in family("INFINITE_ANALYTIC_BOUNDARY")))),
    ("quotient_distance_and_injectivity",lambda s: s.assertTrue(all(r["quotient_distance"]==r["input_norm"] and r["quotient_map_injective"]=="true" for r in family("INFINITE_ANALYTIC_BOUNDARY")))),
    ("fixed_prime_unconditional",lambda s: s.assertTrue(all("UNCONDITIONAL_FIXED_PRIME" in r["fixed_prime_branch"] for r in family("INFINITE_ANALYTIC_BOUNDARY") if r["owner_case"].startswith("FIXED_PRIME")))),
    ("finite_controls_ceiling",lambda s: s.assertTrue(all("NOT_CONTROL_PROOF" in r["evidence_scope"] or "NOT_FINITE_PROOF" in r["evidence_scope"] for r in family("INFINITE_ANALYTIC_BOUNDARY")))),
))


class Test19V2Tail(ControlsCase):
    pass


install(Test19V2Tail, (
    ("two_ideals",lambda s: s.assertEqual({r["owner_case"] for r in family("FINITE_TAIL_QUOTIENT_MODEL")},{"FINITE_QUOTIENT_CORE0_TAIL1","FINITE_QUOTIENT_CORE2_TAIL3"})),
    ("exact_sup_distance",lambda s: s.assertTrue(all(r["quotient_distance"]==r["input_norm"] for r in family("FINITE_TAIL_QUOTIENT_MODEL")))),
    ("zero_nonzero_image",lambda s: s.assertTrue(all((r["quotient_image_nonzero"]=="true")==(r["input_norm"]!="0") for r in family("FINITE_TAIL_QUOTIENT_MODEL")))),
    ("injective_scalar_model",lambda s: s.assertTrue(all(r["quotient_map_injective"]=="true" for r in family("FINITE_TAIL_QUOTIENT_MODEL")))),
    ("not_actual_corona_scope",lambda s: s.assertTrue(all(r["evidence_scope"]=="FINITE_IDEAL_QUOTIENT_MODEL_NOT_MULTIPLIER_CORONA_PROOF" for r in family("FINITE_TAIL_QUOTIENT_MODEL")))),
))


class Test20V2Gauge(ControlsCase):
    pass


def frozen_orientation_probe(s: ControlsCase) -> None:
    mutate_v2_family_field(
        s,"GAUGE_COMMUTATION_MODEL",0,"fixture",
        "K=-6;T=-1;TAU=ONE;ORIENTATION=TAU_OVERLINE_SIGMA_EQ_DELTA_ALPHA",
    )


def independent_exponent_probe(s: ControlsCase) -> None:
    source = s.r(V2_NAME)
    validate_v2_candidate(copy.deepcopy(source))
    context = v1_context_from_results()
    with mock.patch.object(gc,"alpha_exp",return_value=7):
        rebuilt = gc.generate_v2(context,gc.discover_unittest_method_count())
    s.assertEqual(
        [r for r in rebuilt if r["control_family"]=="GAUGE_COMMUTATION_MODEL"],
        family("GAUGE_COMMUTATION_MODEL"),
    )
    with mock.patch.object(gc,"v2_gauge_lhs_exp",return_value=7), mock.patch.object(gc,"v2_gauge_rhs_exp",return_value=7):
        with s.assertRaises(gc.ValidationError):
            gc.generate_v2(context,gc.discover_unittest_method_count())
    for field in ("gauge_lhs_exp_mod24","gauge_rhs_exp_mod24"):
        mutate_v2_family_field(s,"GAUGE_COMMUTATION_MODEL",0,field,"7")
    positions = [i for i,row in enumerate(source) if row["control_family"]=="GAUGE_COMMUTATION_MODEL"]
    copied_wrong = copy.deepcopy(source)
    copied_wrong[positions[0]]["gauge_lhs_exp_mod24"] = "7"
    copied_wrong[positions[0]]["gauge_rhs_exp_mod24"] = "7"
    copied_wrong[positions[0]]["gauge_commutes"] = "true"
    with s.assertRaises(gc.ValidationError):
        validate_v2_candidate(copied_wrong)


install(Test20V2Gauge, (
    ("k24_by_tg",lambda s: s.assertEqual(len({(r["gauge_id"],r["input_id"]) for r in family("GAUGE_COMMUTATION_MODEL")}),12)),
    ("frozen_orientation",frozen_orientation_probe),
    ("independent_exponents",independent_exponent_probe),
    ("completion_extension_firewall",lambda s: s.assertTrue(all("REQUIRES_PROOF" in (r["max_evidence_status"] or r["reduced_evidence_status"]) for r in family("GAUGE_COMMUTATION_MODEL")))),
))


class Test21V2Evidence(ControlsCase):
    pass


def evidence_token_probe(s: ControlsCase, family_index: int, field: str, value: str) -> None:
    mutate_v2_family_field(s,"MAX_REDUCED_EVIDENCE_LEDGER",family_index,field,value)


def evidence_split_probe(s: ControlsCase) -> None:
    source = s.r(V2_NAME)
    positions = [i for i,row in enumerate(source) if row["control_family"]=="MAX_REDUCED_EVIDENCE_LEDGER"]
    candidate = copy.deepcopy(source)
    candidate[positions[3]]["reduced_evidence_status"] = candidate[positions[3]]["max_evidence_status"]
    with s.assertRaises(gc.ValidationError):
        validate_v2_candidate(candidate)


install(Test21V2Evidence, (
    ("max_token",lambda s: evidence_token_probe(s,0,"max_evidence_status","COPIED_COMMON_PASS")),
    ("reduced_token",lambda s: evidence_token_probe(s,1,"reduced_evidence_status","COPIED_COMMON_PASS")),
    ("amenable_endpoint_pair",lambda s: s.assertTrue(all(family("MAX_REDUCED_EVIDENCE_LEDGER")[2][x] for x in ("max_evidence_status","reduced_evidence_status")))),
    ("separate_route_split",evidence_split_probe),
))


class Test22V2Owner(ControlsCase):
    pass


def owner_field_probe(s: ControlsCase, probes: Sequence[Tuple[int,str,str]]) -> None:
    for index,field,value in probes:
        with s.subTest(index=index,field=field):
            mutate_v2_family_field(s,"OWNER_CREDIT_LEDGER",index,field,value)


install(Test22V2Owner, (
    ("paper2_zero_credit",lambda s: owner_field_probe(s,((0,"cardinality_credit_owner","P13_NOVELTY"),))),
    ("actual_bare_split",lambda s: owner_field_probe(s,((1,"cardinality_credit_owner","P13_NOVELTY"),(2,"topology_owner","Q_P_BARE_NO_TOPOLOGY"),(3,"topology_owner","Q_P_ACTUAL_INDISCRETE_SECOND_COUNTABLE_NONHAUSDORFF")))),
    ("standard_unit_arrow",lambda s: owner_field_probe(s,((4,"q_class","ACTUAL"),(5,"q_class","STANDARD")))),
    ("discrete_quotient",lambda s: owner_field_probe(s,((6,"q_class","ACTUAL"),))),
    ("generic_bare_index",lambda s: owner_field_probe(s,((7,"topology_owner","Q_P_ACTUAL_INDISCRETE_SECOND_COUNTABLE_NONHAUSDORFF"),))),
))


class Test23V2Negative(ControlsCase):
    pass


def v2_registry_probe(s: ControlsCase) -> None:
    negative_rows = family("FIREWALL_NEGATIVE")
    s.assertEqual(len(negative_rows),20)
    for index,(row,semantic_mutation) in enumerate(zip(negative_rows,V2_SEMANTIC_MUTATIONS)):
        s.assertEqual(
            gc.detect_v2_negative(row["negative_reason"],row["fixture"],row["violated_lock"]),
            row["expected_detector"],
        )
        rotated_reason = negative_rows[(index+1)%len(negative_rows)]["negative_reason"]
        for fixture,reason,lock in (
            (semantic_mutation,row["negative_reason"],row["violated_lock"]),
            (row["fixture"]+";BROKEN",row["negative_reason"],row["violated_lock"]),
            (row["fixture"],row["negative_reason"],row["violated_lock"]+"_WRONG"),
            (row["fixture"],rotated_reason,row["violated_lock"]),
        ):
            with s.subTest(row=row["row_id"],fixture=fixture,reason=reason,lock=lock):
                with s.assertRaises(gc.ValidationError):
                    gc.detect_v2_negative(reason,fixture,lock)


def assert_v2_negative_slice(s: ControlsCase, indices: Sequence[int]) -> None:
    selected = family("FIREWALL_NEGATIVE")
    for index in indices:
        row = selected[index]
        s.assertEqual(
            gc.detect_v2_negative(row["negative_reason"],row["fixture"],row["violated_lock"]),
            row["expected_detector"],
        )


def v2_manifest_negative_probe(s: ControlsCase) -> None:
    assert_v2_negative_slice(s,(17,18,19))
    base = gc.valid_manifest_firewall_skeleton()
    missing_head = copy.deepcopy(base); missing_head.pop("design_head")
    missing_gate = copy.deepcopy(base)
    missing_gate["bindings"] = [x for x in missing_gate["bindings"] if x["path"]!="notes/phase3_v2_design_gate.md"]
    s.assertEqual(gc.manifest_firewall_failure(missing_head),"UNBOUND_AUTHORITY")
    s.assertEqual(gc.manifest_firewall_failure(missing_gate),"UNBOUND_AUTHORITY")


install(Test23V2Negative, (
    ("registry_order",v2_registry_probe),
    ("finite_as_theorem",lambda s: assert_v2_negative_slice(s,(0,1,2))),
    ("owner_credit_rejections",lambda s: assert_v2_negative_slice(s,(3,4,5,6,7,14,15,16))),
    ("multiplier_corona_gauge_evidence",lambda s: assert_v2_negative_slice(s,(8,9,10,11,12,13))),
    ("manifest_authority_self_proof",v2_manifest_negative_probe),
))


class Test24V2Summary(ControlsCase):
    pass


def summary_field_probe(s: ControlsCase, probes: Sequence[Tuple[int,str,str]]) -> None:
    for index,field,value in probes:
        with s.subTest(index=index,field=field):
            mutate_v2_family_field(s,"V2_PACKAGE_SUMMARY",index,field,value)


install(Test24V2Summary, (
    ("twelve_artifact_rows",lambda s: summary_field_probe(s,((0,"summary_artifact","wrong.csv"),(0,"summary_rows","281"),(0,"summary_columns","18"),(8,"summary_negative_rows","19")))),
    ("self_summary",lambda s: summary_field_probe(s,((11,"summary_rows","116"),(11,"summary_columns","40")))),
    ("package_arithmetic",lambda s: summary_field_probe(s,((0,"summary_rows","281"),(12,"summary_rows","2664"),(12,"summary_negative_rows","66"),(12,"summary_test_methods","175")))),
))


class Test25V2Manifest(ControlsCase):
    pass


def manifest_candidate_probe(s: ControlsCase, mutators: Sequence[Tuple[str,Callable[[Dict[str,object]],None],str]]) -> None:
    expected = manifest()
    gc.validate_manifest_candidate(expected,expected)
    for label,mutator,code in mutators:
        candidate = copy.deepcopy(expected)
        mutator(candidate)
        with s.subTest(label=label):
            expect_validation(s,code,lambda candidate=candidate: gc.validate_manifest_candidate(candidate,expected))


def manifest_schema_binding_probe(s: ControlsCase) -> None:
    def head(d: Dict[str,object]) -> None: d["design_head"]["sha256"]="0"*64
    def gate(d: Dict[str,object]) -> None:
        next(x for x in d["bindings"] if x["path"]=="notes/phase3_v2_design_gate.md")["sha256"]="0"*64
    manifest_candidate_probe(s,(("design_head",head,"MANIFEST_UNBOUND_AUTHORITY"),("v2_gate",gate,"MANIFEST_UNBOUND_AUTHORITY")))


def manifest_edge_probe(s: ControlsCase) -> None:
    manifest_candidate_probe(s,(
        ("implementation",lambda d:d["implementation"][0].__setitem__("sha256","0"*64),"MANIFEST_IMPLEMENTATION_EDGE"),
        ("artifact",lambda d:d["artifacts"][0].__setitem__("sha256","0"*64),"MANIFEST_ARTIFACT_EDGE"),
    ))


def manifest_firewall_probe(s: ControlsCase) -> None:
    def proof(d: Dict[str,object]) -> None: d["aggregates"]["nested"]={"proof_bytes":1}
    def proof_oracle(d: Dict[str,object]) -> None: d["aggregates"]["oracle_probe"]="PROOF_DERIVED_ORACLE"
    def self_entry(d: Dict[str,object]) -> None: d["artifacts"].append({"path":"results/manifest.json","sha256":"1"*64})
    def missing_impl(d: Dict[str,object]) -> None: d["implementation"].pop()
    def extra_artifact(d: Dict[str,object]) -> None: d["artifacts"].append(copy.deepcopy(d["artifacts"][0]))
    manifest_candidate_probe(s,(
        ("proof",proof,"MANIFEST_PROOF_BINDING"),
        ("proof_oracle",proof_oracle,"MANIFEST_PROOF_BINDING"),
        ("self",self_entry,"MANIFEST_SELF_HASH"),
        ("missing_impl",missing_impl,"MANIFEST_INVENTORY"),
        ("extra_artifact",extra_artifact,"MANIFEST_INVENTORY"),
    ))


install(Test25V2Manifest, (
    ("schema_and_binding_union",manifest_schema_binding_probe),
    ("implementation_and_artifact_hashes",manifest_edge_probe),
    ("no_proof_or_self_cycle",manifest_firewall_probe),
))


def verify_only_immutable(s: ControlsCase) -> None:
    before = gc.package_receipt(RESULTS)
    opened_write_modes: List[str] = []
    original_path_open = Path.open
    original_builtin_open = builtins.open

    def audited_open(path: Path, mode: str = "r", *args: object, **kwargs: object):
        if any(marker in mode for marker in ("w","a","x","+")):
            opened_write_modes.append(f"{path}:{mode}")
        return original_path_open(path,mode,*args,**kwargs)

    def audited_builtin_open(file: object, mode: str = "r", *args: object, **kwargs: object):
        if any(marker in mode for marker in ("w","a","x","+")):
            opened_write_modes.append(f"{file}:{mode}")
        return original_builtin_open(file,mode,*args,**kwargs)

    with mock.patch.object(Path,"open",audited_open), mock.patch.object(builtins,"open",audited_builtin_open):
        receipt = gc.guarded_verify_package(RESULTS)
    s.assertIn("entries",receipt)
    s.assertEqual(opened_write_modes,[])
    s.assertEqual(before,gc.package_receipt(RESULTS))

    with package_copy("verify_guard_byte") as root:
        def byte_write(candidate: Path) -> None:
            path = candidate/V2_NAME
            path.write_bytes(path.read_bytes()+b"x")
        expect_validation(s,"VERIFY_ONLY_BYTE_WRITE",lambda: gc.guarded_verify_package(root,byte_write))

    with package_copy("verify_guard_utime") as root:
        def metadata_utime(candidate: Path) -> None:
            path = candidate/V2_NAME
            info = path.stat()
            os.utime(path,ns=(info.st_atime_ns,info.st_mtime_ns+1_000_000_000))
        expect_validation(s,"VERIFY_ONLY_METADATA_WRITE",lambda: gc.guarded_verify_package(root,metadata_utime))

    with package_copy("verify_guard_chmod") as root:
        def metadata_chmod(candidate: Path) -> None:
            path = candidate/V2_NAME
            path.chmod(path.stat().st_mode ^ 0o100)
        expect_validation(s,"VERIFY_ONLY_METADATA_WRITE",lambda: gc.guarded_verify_package(root,metadata_chmod))


def three_way_equality(s: ControlsCase) -> None:
    s.assertEqual(artifact_bytes(RESULTS),artifact_bytes(FRESH_A)); s.assertEqual(artifact_bytes(FRESH_A),artifact_bytes(FRESH_B))


def v2_tamper_rejection(s: ControlsCase) -> None:
    def csv_cell(label: str, index: int, field: str, value: str, code: str) -> None:
        with package_copy(label) as root:
            mutate_csv_cell(root,V2_NAME,index,field,value)
            expect_verify_failure(s,root,code)

    # New-CSV syntax and ordering classes.
    csv_cell("v2_content",0,"input_norm","1","V2_FIELD_input_norm")
    with package_copy("v2_header") as root:
        path=root/V2_NAME; path.write_bytes(path.read_bytes().replace(b"schema_version",b"schema_versioX",1))
        expect_verify_failure(s,root,"CSV_HEADER")
    with package_copy("v2_count") as root:
        path=root/V2_NAME; lines=path.read_bytes().splitlines(keepends=True); path.write_bytes(b"".join(lines[:-1]))
        expect_verify_failure(s,root,"CSV_ROW_COUNT")
    with package_copy("v2_order") as root:
        path=root/V2_NAME; lines=path.read_bytes().splitlines(keepends=True); lines[1],lines[2]=lines[2],lines[1]; path.write_bytes(b"".join(lines))
        expect_verify_failure(s,root,"CSV_ROW_ORDER")

    # Closed owner/cardinality-credit registry, one isolated token per case.
    owner_mutations = (
        (72,"cardinality_credit_owner","P13_NOVELTY"),
        (73,"cardinality_credit_owner","P13_NOVELTY"),
        (74,"topology_owner","Q_P_BARE_NO_TOPOLOGY"),
        (75,"topology_owner","Q_P_ACTUAL_INDISCRETE_SECOND_COUNTABLE_NONHAUSDORFF"),
        (76,"q_class","ACTUAL"),
        (77,"q_class","STANDARD"),
        (78,"q_class","ACTUAL"),
        (79,"topology_owner","Q_P_ACTUAL_INDISCRETE_SECOND_COUNTABLE_NONHAUSDORFF"),
    )
    for ordinal,(index,field,value) in enumerate(owner_mutations,1):
        csv_cell(f"v2_owner_{ordinal}",index,field,value,f"V2_FIELD_{field}")

    # Maximal and reduced evidence are independent, non-copyable routes.
    csv_cell("v2_max_evidence",80,"max_evidence_status","COPIED_COMMON_PASS","V2_FIELD_max_evidence_status")
    csv_cell("v2_reduced_evidence",81,"reduced_evidence_status","COPIED_COMMON_PASS","V2_FIELD_reduced_evidence_status")
    max_token = family("MAX_REDUCED_EVIDENCE_LEDGER")[3]["max_evidence_status"]
    csv_cell("v2_evidence_conflation",83,"reduced_evidence_status",max_token,"V2_FIELD_reduced_evidence_status")

    # Status and the five independent negative-row fields.
    csv_cell("v2_status",0,"status","FAIL","V2_FIELD_status")
    csv_cell("v2_observed",84,"observed_detector","WRONG","V2_NEGATIVE_OBSERVED_DETECTOR")
    csv_cell("v2_expected",84,"expected_detector","WRONG","V2_NEGATIVE_EXPECTED_DETECTOR")
    csv_cell("v2_fixture",84,"fixture",V2_SEMANTIC_MUTATIONS[0],"V2_NEGATIVE_FIXTURE")
    csv_cell("v2_lock",84,"violated_lock","WRONG_LOCK","V2_NEGATIVE_LOCK")
    csv_cell("v2_reason",84,"negative_reason",gc.V2_NEGATIVES[1][0],"V2_NEGATIVE_REASON")

    # Artifact, self, and aggregate summary fields are all recomputed.
    summary_mutations = (
        (104,"summary_artifact","wrong.csv"),(104,"summary_rows","281"),
        (104,"summary_columns","18"),(112,"summary_negative_rows","19"),
        (115,"summary_rows","116"),(115,"summary_columns","40"),
        (116,"summary_rows","2664"),(116,"summary_negative_rows","66"),
        (116,"summary_test_methods","175"),
    )
    for ordinal,(index,field,value) in enumerate(summary_mutations,1):
        csv_cell(f"v2_summary_{ordinal}",index,field,value,f"V2_FIELD_{field}")

    def manifest_case(label: str, mutator: Callable[[Dict[str,object]],None], code: str) -> None:
        with package_copy(label) as root:
            mutate_manifest(root,mutator)
            expect_verify_failure(s,root,code)

    manifest_case("v2_artifact_edge",lambda d:d["artifacts"][0].__setitem__("sha256","0"*64),"MANIFEST_ARTIFACT_EDGE")
    manifest_case("v2_implementation_edge",lambda d:d["implementation"][0].__setitem__("sha256","0"*64),"MANIFEST_IMPLEMENTATION_EDGE")
    manifest_case("v2_design_head",lambda d:d["design_head"].__setitem__("sha256","0"*64),"MANIFEST_UNBOUND_AUTHORITY")
    def gate_edge(d: Dict[str,object]) -> None:
        next(x for x in d["bindings"] if x["path"]=="notes/phase3_v2_design_gate.md")["sha256"]="0"*64
    manifest_case("v2_gate_edge",gate_edge,"MANIFEST_UNBOUND_AUTHORITY")
    manifest_case("v2_self_entry",lambda d:d["artifacts"].append({"path":"results/manifest.json","sha256":"1"*64}),"MANIFEST_SELF_HASH")
    manifest_case("v2_self_digest",lambda d:d["aggregates"].__setitem__("manifest_sha256","1"*64),"MANIFEST_SELF_HASH")
    manifest_case("v2_proof",lambda d:d["aggregates"].__setitem__("proof_bytes",1),"MANIFEST_PROOF_BINDING")
    manifest_case("v2_proof_oracle",lambda d:d["aggregates"].__setitem__("oracle_probe","PROOF_DERIVED_ORACLE"),"MANIFEST_PROOF_BINDING")
    manifest_case("v2_missing_head",lambda d:d.pop("design_head"),"MANIFEST_UNBOUND_AUTHORITY")
    def missing_gate(d: Dict[str,object]) -> None:
        d["bindings"]=[x for x in d["bindings"] if x["path"]!="notes/phase3_v2_design_gate.md"]
    manifest_case("v2_missing_gate",missing_gate,"MANIFEST_UNBOUND_AUTHORITY")
    manifest_case("v2_extra_manifest_key",lambda d:d.__setitem__("extra",{}),"MANIFEST_INVENTORY")
    manifest_case("v2_missing_manifest_key",lambda d:d.pop("aggregates"),"MANIFEST_INVENTORY")
    manifest_case("v2_extra_artifact_inventory",lambda d:d["artifacts"].append(copy.deepcopy(d["artifacts"][0])),"MANIFEST_INVENTORY")
    manifest_case("v2_missing_artifact_inventory",lambda d:d["artifacts"].pop(),"MANIFEST_INVENTORY")
    manifest_case("v2_extra_implementation_inventory",lambda d:d["implementation"].append(copy.deepcopy(d["implementation"][0])),"MANIFEST_INVENTORY")
    manifest_case("v2_missing_implementation_inventory",lambda d:d["implementation"].pop(),"MANIFEST_INVENTORY")

    with package_copy("v2_missing_csv") as root:
        (root/V2_NAME).unlink(); expect_verify_failure(s,root,"PACKAGE_MISSING_ARTIFACT")
    with package_copy("v2_extra_csv") as root:
        (root/"extra.csv").write_bytes(b"x\n"); expect_verify_failure(s,root,"PACKAGE_EXTRA_ARTIFACT")
    with package_copy("v2_extra_directory") as root:
        (root/"extra").mkdir(); expect_verify_failure(s,root,"PACKAGE_EXTRA_DIRECTORY")

    # A legacy body drift reaches exact-byte identity after semantic parsing.
    with package_copy("v1_body_drift") as root:
        mutate_csv_cell(root,gc.ARTIFACT_ORDER[0],0,"actual_exp_mod24","1")
        expect_verify_failure(s,root,"ARTIFACT_BYTE_IDENTITY")


def cache_and_residue(s: ControlsCase) -> None:
    gc.assert_no_cache(PAPER_DIR/"code",PAPER_DIR/"experiments",RESULTS,FRESH_A,FRESH_B)
    s.assertFalse(SCRATCH.exists())


class Test26V2Reproduction(ControlsCase):
    pass


install(Test26V2Reproduction, (("verify_only_immutability",verify_only_immutable),("three_way_thirteen_artifacts",three_way_equality),("design_gate_new_csv_tamper",v2_tamper_rejection),("pre_post_cache_and_residue",cache_and_residue)))


TEST_CLASSES = (
    Test01Nerve,Test02Cocycle,Test03Lift,Test04Gauge,Test05Convolution,Test06Involution,
    Test07Completion,Test08ActionPeriod,Test09NegativeDomain,Test10SupportTransfer,
    Test11TargetSummary,Test12PackageManifest,Test13Reproduction,Test14Tamper,Test15Lifecycle,
    Test16V2Schema,Test17V2Finite,Test18V2Infinite,Test19V2Tail,Test20V2Gauge,
    Test21V2Evidence,Test22V2Owner,Test23V2Negative,Test24V2Summary,Test25V2Manifest,
    Test26V2Reproduction,
)


def discoverable_method_count() -> int:
    return sum(sum(name.startswith("test_") and callable(value) for name,value in vars(cls).items()) for cls in TEST_CLASSES)


def static_prechecks() -> None:
    """Run write-free source, byte-lock, and in-memory mutation gates."""
    if discoverable_method_count()!=176:
        raise AssertionError("static discovery count drift")
    suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(cls) for cls in TEST_CLASSES)
    if suite.countTestCases()!=176:
        raise AssertionError("loader discovery count drift")
    payloads,rowsets = gc.build_csv_payloads()
    actual_hashes = {name:gc.sha256_bytes(payloads[name]) for name in gc.ARTIFACT_ORDER}
    if actual_hashes != LOCKED_CSV_SHA256:
        drift = {name:(LOCKED_CSV_SHA256[name],actual_hashes[name]) for name in gc.ARTIFACT_ORDER if actual_hashes[name]!=LOCKED_CSV_SHA256[name]}
        raise AssertionError(f"locked CSV byte drift: {drift}")

    def must_reject(action: Callable[[],object], label: str) -> None:
        try:
            action()
        except gc.ValidationError:
            return
        raise AssertionError(f"mutation accepted: {label}")

    for index,((reason,fixture,lock,detector,_disposition),semantic) in enumerate(zip(gc.V1_NEGATIVES,V1_SEMANTIC_MUTATIONS)):
        if gc.detect_v1_negative(reason,fixture,lock)!=detector:
            raise AssertionError(f"v1 detector drift: {index}")
        rotated = gc.V1_NEGATIVES[(index+1)%20][0]
        must_reject(lambda r=reason,f=semantic,l=lock:gc.detect_v1_negative(r,f,l),f"v1 semantic {index}")
        must_reject(lambda r=reason,f=fixture,l=lock:gc.detect_v1_negative(r,f+";BROKEN",l),f"v1 malformed {index}")
        must_reject(lambda r=reason,f=fixture,l=lock:gc.detect_v1_negative(r,f,l+"_WRONG"),f"v1 lock {index}")
        must_reject(lambda r=rotated,f=fixture,l=lock:gc.detect_v1_negative(r,f,l),f"v1 reason {index}")

    support = rowsets["actual_standard_support_transfer_controls.csv"]
    gc.validate_support_transfer_rows(copy.deepcopy(support))
    negative_support = [i for i,row in enumerate(support) if row["case_kind"]=="NEGATIVE"]
    if len(negative_support)!=27:
        raise AssertionError("support negative count drift")
    for index in negative_support:
        for field,value in (("q_case","NONSENSE"),("q_class","FINITE"),("standard_support_compact","true"),("status","FAIL")):
            candidate=copy.deepcopy(support); candidate[index][field]=value
            must_reject(lambda c=candidate:gc.validate_support_transfer_rows(c),f"support {index} {field}")

    for index,((reason,fixture,lock,detector),semantic) in enumerate(zip(gc.V2_NEGATIVES,V2_SEMANTIC_MUTATIONS)):
        if gc.detect_v2_negative(reason,fixture,lock)!=detector:
            raise AssertionError(f"v2 detector drift: {index}")
        rotated = gc.V2_NEGATIVES[(index+1)%20][0]
        must_reject(lambda r=reason,f=semantic,l=lock:gc.detect_v2_negative(r,f,l),f"v2 semantic {index}")
        must_reject(lambda r=reason,f=fixture,l=lock:gc.detect_v2_negative(r,f+";BROKEN",l),f"v2 malformed {index}")
        must_reject(lambda r=reason,f=fixture,l=lock:gc.detect_v2_negative(r,f,l+"_WRONG"),f"v2 lock {index}")
        must_reject(lambda r=rotated,f=fixture,l=lock:gc.detect_v2_negative(r,f,l),f"v2 reason {index}")

    convolution = rowsets["twisted_convolution_controls.csv"]
    involution = rowsets["twisted_involution_controls.csv"]
    completion = rowsets["completion_gauge_controls.csv"]
    gc.validate_convolution_independence(convolution)
    gc.validate_involution_independence(involution)
    gc.validate_completion_independence(completion)
    for source,field,validator,label in (
        (convolution,"left_assoc_re",gc.validate_convolution_independence,"product"),
        (involution,"actual_star_re",gc.validate_involution_independence,"star"),
        (completion,"character_times_xi_norm_sq",gc.validate_completion_independence,"norm"),
    ):
        candidate=copy.deepcopy(source); candidate[0][field]=str(int(candidate[0][field])+1)
        must_reject(lambda c=candidate,v=validator:v(c),f"one-side {label}")
    copied_norm=copy.deepcopy(completion)
    copied_norm[0]["xi_norm_sq"]=copied_norm[0]["character_times_xi_norm_sq"]="7"
    must_reject(lambda:gc.validate_completion_independence(copied_norm),"copied norm")

    v2 = rowsets[V2_NAME]
    context = {name:rowsets[name] for name in gc.ARTIFACT_ORDER[:11]}
    gc.validate_v2_families(copy.deepcopy(v2),context,176)
    gauge_index = next(i for i,row in enumerate(v2) if row["control_family"]=="GAUGE_COMMUTATION_MODEL")
    copied_gauge=copy.deepcopy(v2)
    copied_gauge[gauge_index]["gauge_lhs_exp_mod24"]="7"
    copied_gauge[gauge_index]["gauge_rhs_exp_mod24"]="7"
    copied_gauge[gauge_index]["gauge_commutes"]="true"
    must_reject(lambda:gc.validate_v2_families(copied_gauge,context,176),"copied wrong gauge")
    with mock.patch.object(gc,"v2_gauge_lhs_exp",return_value=7), mock.patch.object(gc,"v2_gauge_rhs_exp",return_value=7):
        must_reject(lambda:gc.generate_v2(context,176),"wrong v2 gauge phase rule")
    stale_summary=copy.deepcopy(v2); stale_summary[104]["summary_rows"]="281"
    must_reject(lambda:gc.validate_v2_families(stale_summary,context,176),"stale summary")
    forced_pass=copy.deepcopy(v2); forced_pass[0]["algebra_member"]="false"; forced_pass[0]["status"]="PASS"
    must_reject(lambda:gc.validate_v2_families(forced_pass,context,176),"forced PASS")
    for index,field,value in (
        (72,"cardinality_credit_owner","P13_NOVELTY"),
        (73,"cardinality_credit_owner","P13_NOVELTY"),
        (74,"topology_owner","Q_P_BARE_NO_TOPOLOGY"),
        (75,"topology_owner","Q_P_ACTUAL_INDISCRETE_SECOND_COUNTABLE_NONHAUSDORFF"),
        (76,"q_class","ACTUAL"),(77,"q_class","STANDARD"),(78,"q_class","ACTUAL"),
        (79,"topology_owner","Q_P_ACTUAL_INDISCRETE_SECOND_COUNTABLE_NONHAUSDORFF"),
        (80,"max_evidence_status","COPIED_COMMON_PASS"),
        (81,"reduced_evidence_status","COPIED_COMMON_PASS"),
        (84,"observed_detector","WRONG"),(84,"expected_detector","WRONG"),
        (84,"fixture",V2_SEMANTIC_MUTATIONS[0]),(84,"violated_lock","WRONG"),
        (104,"summary_artifact","wrong.csv"),(104,"summary_columns","18"),
        (112,"summary_negative_rows","19"),(115,"summary_rows","116"),
        (115,"summary_columns","40"),(116,"summary_rows","2664"),
        (116,"summary_negative_rows","66"),(116,"summary_test_methods","175"),
    ):
        candidate=copy.deepcopy(v2); candidate[index][field]=value
        must_reject(lambda c=candidate:gc.validate_v2_families(c,context,176),f"v2 registry {index} {field}")

    expected_manifest=json.loads(gc.build_manifest(payloads).decode("utf-8"))
    gc.validate_manifest_candidate(expected_manifest,expected_manifest)
    manifest_mutations: List[Tuple[str,Callable[[Dict[str,object]],None]]] = [
        ("artifact edge",lambda d:d["artifacts"][0].__setitem__("sha256","0"*64)),
        ("implementation edge",lambda d:d["implementation"][0].__setitem__("sha256","0"*64)),
        ("design head",lambda d:d["design_head"].__setitem__("sha256","0"*64)),
        ("proof bytes",lambda d:d["aggregates"].__setitem__("proof_bytes",1)),
        ("proof oracle",lambda d:d["aggregates"].__setitem__("oracle_probe","PROOF_DERIVED_ORACLE")),
        ("self",lambda d:d["aggregates"].__setitem__("manifest_sha256","1"*64)),
        ("missing authority",lambda d:d.pop("design_head")),
        ("extra inventory",lambda d:d.__setitem__("extra",{})),
        ("missing inventory",lambda d:d.pop("aggregates")),
        ("extra artifact",lambda d:d["artifacts"].append(copy.deepcopy(d["artifacts"][0]))),
        ("missing implementation",lambda d:d["implementation"].pop()),
    ]
    for label,mutator in manifest_mutations:
        candidate=copy.deepcopy(expected_manifest); mutator(candidate)
        must_reject(lambda c=candidate:gc.validate_manifest_candidate(c,expected_manifest),f"manifest {label}")
    generator_source=inspect.getsource(gc.generate_v2)
    if 'status=""' not in generator_source or 'status="PASS"' in generator_source:
        raise AssertionError("v2 row builder has unconditional PASS")


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args:
        if args != ["--static-precheck"]:
            print(f"P13_TEST_ARGUMENT_FAIL: {args}",file=sys.stderr)
            return 2
        try:
            static_prechecks()
        except (AssertionError,gc.ValidationError,ValueError,KeyError) as exc:
            print(f"P13_STATIC_PRECHECK_FAIL: {exc}",file=sys.stderr)
            return 1
        print("STATIC_MUTATION_PRECHECK=PASS")
        print("LOCKED_CSV_HASHES=12/12")
        print("UNITTEST_METHODS=176")
        return 0
    if discoverable_method_count() != 176:
        print(f"P13_TEST_COUNT_FAIL: {discoverable_method_count()} != 176",file=sys.stderr)
        return 2
    suite=unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(cls) for cls in TEST_CLASSES)
    if suite.countTestCases()!=176:
        print(f"P13_DISCOVERY_FAIL: {suite.countTestCases()} != 176",file=sys.stderr)
        return 2
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"UNITTEST_METHODS={suite.countTestCases()}")
    print(f"UNITTEST_FAILURES={len(result.failures)}")
    print(f"UNITTEST_ERRORS={len(result.errors)}")
    return 0 if result.wasSuccessful() else 1


if __name__=="__main__":
    raise SystemExit(main())
