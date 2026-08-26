#!/usr/bin/env python3
"""Independent literal 173-method oracle for Paper 15R controls.

The oracle never imports the deterministic subject.  Semantic failures are
derived from primitive typed predicates before a detector is translated.
Process and filesystem mutations are requested on the authenticated FD4/FD5
lanes and are performed only by the guardian's admitted direct children.
"""

from __future__ import annotations

import csv
import hashlib
import io
import itertools
import json
import math
import os
import re
import socket
import stat
import struct
import sys
import unittest
from dataclasses import dataclass
from typing import Callable, Iterable, Mapping, Sequence


SCHEMA = "paper15r-wieferich-ulm-controls/1"
MANIFEST_SCHEMA = "paper15r-wieferich-ulm-controls-manifest/1"
PACKAGE_ID = "paper15r-wieferich-ulm-controls"
DESIGN_LOCK = ("notes/phase2_control_design_lock.md","db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d")
DESIGN_REVIEW = ("notes/phase2_control_design_peer_review.md","2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19")
IMPLEMENTATION_GATE = ("notes/phase2_control_implementation_gate.md","e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8")
CSV_NAMES = (
    "valuation_normalization_controls.csv",
    "exponent_order_branch_controls.csv",
    "finite_kernel_truncation_controls.csv",
    "torsion_closure_type_controls.csv",
    "signature_nonpromotion_controls.csv",
    "owner_firewall_controls.csv",
    "proof_ceiling_controls.csv",
    "target_summary.csv",
)
GENERATED_NAMES = CSV_NAMES + ("manifest.json",)
ROW_COUNTS = (16,14,18,10,12,15,26,9)
WIDTHS = (18,19,22,17,16,19,13,10)
NEGATIVE_COUNTS = (4,2,4,3,4,9,9,0)
PREFIXES = ("VC","EO","FK","TC","SG","OF","PC","TS")
HEADERS = (
    "schema_version,row_id,p,r,branch,expression,factorization,raw_valuation,normalization_subtrahend,kappa,principal_sign,mutation_id,case_kind,negative_reason,oracle,scope_ceiling,tolerance,status".split(","),
    "schema_version,row_id,witness_kind,p,r,m,ell,ell_minus_1,order_mod_ell,v_r_ell_minus_1,v_r_order,finite_group_model,claim_under_test,mutation_id,case_kind,negative_reason,oracle,scope_ceiling,status".split(","),
    "schema_version,row_id,model_kind,r,target_exponent,kappa,source_exponents,image_numerators,kernel_order,height_orders_d0_to_N,tail_order,depth,tail_vector,root_vector,phi_of_root,root_in_kernel,mutation_id,case_kind,negative_reason,oracle,scope_ceiling,status".split(","),
    "schema_version,row_id,model_kind,r,kappa,finite_model_id,discrete_tail_order,compact_quotient_order,source_owner,operation,target_owner,statement_scope,mutation_id,case_kind,negative_reason,oracle,status".split(","),
    "schema_version,row_id,row_kind,p,q,prime_prefix,kappa_prefix_p,kappa_prefix_q,distinguishing_prime,authorized_conclusion,mutation_id,case_kind,negative_reason,oracle,scope_ceiling,status".split(","),
    "schema_version,row_id,row_kind,r,exponent,block_type,label_a,label_b,automorphism_matrix,determinant_mod_r,bare_type_preserved,source_owner,target_owner,claim_under_test,mutation_id,case_kind,negative_reason,oracle,status".split(","),
    "schema_version,row_id,record_kind,binding_path,binding_sha256,claim_class,allowed_state,prohibited_promotion,mutation_id,case_kind,negative_reason,oracle,status".split(","),
    "schema_version,row_id,artifact,expected_rows,expected_columns,expected_negative_rows,expected_mutation_classes,canonical_order_key,oracle_class,status".split(","),
)

AUTHORITY_BINDINGS = (
    ("papers/14-global-periodic-topology/notes/papers14_18_batch_design_lock.md", "2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8"),
    ("papers/14-global-periodic-topology/notes/papers14_18_batch_amendment_v1.md", "afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802"),
    ("papers/14-global-periodic-topology/notes/papers14_18_batch_amendment_v2.md", "3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b"),
    ("papers/15-mixed-clock-rigidity/notes/phase1_transverse_ulm_precheck.md", "02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb"),
    ("papers/15-wieferich-ulm-packet-bases/notes/research_protocol.md", "02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a"),
    ("papers/15-wieferich-ulm-packet-bases/notes/candidate_lock.md", "811b4b515dd3f3c45cc96390a139e1d5e3a361d4fea566f0a473d91b8a73d722"),
    ("papers/15-wieferich-ulm-packet-bases/notes/phase1_amendment_v1.md", "2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc"),
    ("papers/15-wieferich-ulm-packet-bases/notes/phase1_amendment_v2.md", "386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80"),
    ("papers/15-wieferich-ulm-packet-bases/notes/phase1_source_precedent_audit.md", "287bba68fa191a1971c6c060b7eae43bf2ca2f02cbf64f6dfb8959d5c546de97"),
    ("papers/15-wieferich-ulm-packet-bases/notes/phase1_methodology_devils_review.md", "5af721d6a0ba05731ce2e18397e006b87ef90f327a9edd931c171ad6b889f1ae"),
    ("papers/15-wieferich-ulm-packet-bases/notes/phase1_final_gate.md", "949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd"),
    ("papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_proofs.md", "7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355"),
    ("papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_peer_review.md", "2b889ba09b95b3d97be62780f026e4a9e3de58379eb9abb8c720c8b6cd792cc7"),
    ("papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_gate.md", "0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3"),
)
IMPLEMENTATION_PATHS = ("code/generate_controls.py","code/test_controls.py","code/README.md","experiments/reproduce.sh","experiments/README.md","results/README.md")
DAG_NODES = ("A","D","R","G","I","C","M","V")
DAG_EDGES = (("A","D"),("D","R"),("R","G"),("G","I"),("I","C"),("C","M"),("M","V"),("A","M"),("D","M"),("R","M"),("G","M"),("I","M"))
MANIFEST_AGGREGATES = {
    "BYTE_IDENTICAL_COPIES":3,"CSV_ARTIFACTS":8,"CSV_BODY_ROWS":120,"EXPECTED_NEGATIVES_DETECTED":35,
    "EXPLICIT_NEGATIVE_ROWS":35,"FRESH_GENERATIONS":2,"GENERATED_ARTIFACTS_INCLUDING_MANIFEST":9,
    "NEGATIVE_FAILURES":0,"NETWORK_USED":False,"PACKAGE_MUTATION_CLASSES":28,"RANDOM_USED":False,
    "SEMANTIC_MUTATION_CLASSES":35,"TOLERANCE_POLICY":"EXACT_ZERO","UNITTEST_ERRORS":0,
    "UNITTEST_FAILURES":0,"UNITTEST_METHODS":173,
}
MAX_PACKET = 4096
STREAM_LIMIT = 16_777_216
OUTCOME_RE = r"(?:UNSET|ABSENT|DISPLACED_OWNED|DISPLACED_CLEANED|FOREIGN_RETAINED|ERROR|CRASH_TEARDOWN)"
RECEIPT_FIELDS = ("row_id","case_kind","mutation_id","negative_reason","oracle","scope_ceiling","status","expected_class","expected_detector")
EXACT_TEST_NAMES = (
    "test_val_001","test_val_002","test_val_003","test_val_004","test_val_005","test_val_006","test_val_007","test_val_008","test_val_009","test_val_010",
    "test_ord_001","test_ord_002","test_ord_003","test_ord_004","test_ord_005","test_ord_006","test_ord_007","test_ord_008","test_ord_009","test_ord_010",
    "test_ker_001","test_ker_002","test_ker_003","test_ker_004","test_ker_005","test_ker_006","test_ker_007","test_ker_008","test_ker_009","test_ker_010","test_ker_011","test_ker_012","test_ker_013","test_ker_014",
    "test_tor_001","test_tor_002","test_tor_003","test_tor_004","test_tor_005","test_tor_006","test_tor_007","test_tor_008","test_tor_009",
    "test_sig_001","test_sig_002","test_sig_003","test_sig_004","test_sig_005","test_sig_006","test_sig_007","test_sig_008","test_sig_009","test_sig_010",
    "test_own_001","test_own_002","test_own_003","test_own_004","test_own_005","test_own_006","test_own_007","test_own_008","test_own_009","test_own_010","test_own_011","test_own_012",
    "test_ceil_001","test_ceil_002","test_ceil_003","test_ceil_004","test_ceil_005","test_ceil_006","test_ceil_007","test_ceil_008","test_ceil_009","test_ceil_010","test_ceil_011","test_ceil_012",
    "test_sum_001","test_sum_002","test_sum_003","test_sum_004","test_sum_005",
    "test_pkg_001","test_pkg_002","test_pkg_003","test_pkg_004","test_pkg_005","test_pkg_006","test_pkg_007","test_pkg_008","test_pkg_009","test_pkg_010","test_pkg_011","test_pkg_012","test_pkg_013","test_pkg_014","test_pkg_015","test_pkg_016","test_pkg_017","test_pkg_018",
    "test_rep_001","test_rep_002","test_rep_003","test_rep_004","test_rep_005","test_rep_006","test_rep_007","test_rep_008","test_rep_009","test_rep_010",
    "test_semantic_s01_wrong_local_coordinate","test_semantic_s02_wrong_odd_minus_one","test_semantic_s03_wrong_two_minus_three","test_semantic_s04_erased_local_two_sign","test_semantic_s05_diagonal_bounded_surjectivity","test_semantic_s06_mere_divisibility_as_exact","test_semantic_s07_ambient_root_r2_k1","test_semantic_s08_ambient_root_r2_k2","test_semantic_s09_ambient_root_r3_k1","test_semantic_s10_ambient_root_r3_k2","test_semantic_s11_raw_torsion_for_closure","test_semantic_s12_finite_model_promotion","test_semantic_s13_discrete_compact_confusion","test_semantic_s14_prefix_equality_promotion","test_semantic_s15_separation_to_recovery","test_semantic_s16_finite_range_injectivity","test_semantic_s17_open_map_injective","test_semantic_s18_marked_bare_splice","test_semantic_s19_ambient_marker_import","test_semantic_s20_actual_topology_import","test_semantic_s21_standardized_flow_import","test_semantic_s22_haar_claim","test_semantic_s23_measure_claim","test_semantic_s24_trace_claim","test_semantic_s25_operator_claim","test_semantic_s26_determinant_claim","test_semantic_s27_grh_promotion","test_semantic_s28_density_promotion","test_semantic_s29_priority_promotion","test_semantic_s30_route_b_promotion","test_semantic_s31_universal_recovery","test_semantic_s32_control_as_proof","test_semantic_s33_receipt_as_theorem","test_semantic_s34_control_as_chebotarev","test_semantic_s35_control_as_ulm",
    "test_package_p01_cell_content_tamper","test_package_p02_header_tamper","test_package_p03_stale_row_count","test_package_p04_row_reorder","test_package_p05_missing_csv","test_package_p06_extra_csv","test_package_p07_missing_manifest","test_package_p08_extra_file","test_package_p09_extra_directory","test_package_p10_manifest_field_tamper","test_package_p11_manifest_self_hash","test_package_p12_authority_binding_drift","test_package_p13_design_lock_drift","test_package_p14_design_review_drift","test_package_p15_implementation_gate_drift","test_package_p16_implementation_digest_drift","test_package_p17_symlink_input","test_package_p18_hardlink_input","test_package_p19_pre_run_cache","test_package_p20_post_run_cache","test_package_p21_recursive_entry","test_package_p22_concurrent_second_entry","test_package_p23_verify_only_repair_attempt","test_package_p24_forced_cleanup_failure","test_package_p25_nonempty_generation_root","test_package_p26_future_result_cycle_edge","test_package_p27_ambient_metadata","test_package_p28_noncanonical_json_or_newline",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: object) -> bytes:
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode("utf-8")


def independent_manifest_graph(manifest: Mapping[str,object], raw_artifacts: Mapping[str,bytes]) -> tuple[tuple[str,...],tuple[tuple[str,str],...]]:
    top={"schema_version","package_id","authority_bindings","design_lock","design_review","implementation_gate","implementation","artifacts","aggregates","reproduction","proof_ceiling","status"}
    if set(manifest)!=top or manifest.get("schema_version")!=MANIFEST_SCHEMA or manifest.get("package_id")!=PACKAGE_ID or manifest.get("status")!="PASS":
        raise AssertionError("manifest top")
    if manifest.get("authority_bindings")!=[{"path":path,"sha256":digest} for path,digest in AUTHORITY_BINDINGS]:
        raise AssertionError("manifest authority")
    for key,literal in (("design_lock",DESIGN_LOCK),("design_review",DESIGN_REVIEW),("implementation_gate",IMPLEMENTATION_GATE)):
        if manifest.get(key)!={"path":literal[0],"sha256":literal[1]}:
            raise AssertionError("manifest "+key)
    implementation=manifest.get("implementation")
    if not isinstance(implementation,list) or len(implementation)!=6:
        raise AssertionError("manifest implementation")
    for item,path in zip(implementation,IMPLEMENTATION_PATHS):
        if not isinstance(item,dict) or set(item)!={"path","bytes","sha256"} or item.get("path")!=path or type(item.get("bytes")) is not int or item["bytes"]<0 or re.fullmatch(r"[0-9a-f]{64}",str(item.get("sha256",""))) is None:
            raise AssertionError("manifest implementation row")
    artifacts=manifest.get("artifacts")
    if not isinstance(artifacts,list) or len(artifacts)!=8:
        raise AssertionError("manifest artifacts")
    for item,name,rows,columns,negatives in zip(artifacts,CSV_NAMES,ROW_COUNTS,WIDTHS,NEGATIVE_COUNTS):
        data=raw_artifacts[name]
        expected={"path":"results/"+name,"schema":SCHEMA,"columns":columns,"rows":rows,"negative_rows":negatives,"mutation_classes":negatives,"bytes":len(data),"sha256":sha256(data)}
        if item!=expected:
            raise AssertionError("manifest artifact row")
    if manifest.get("aggregates")!=MANIFEST_AGGREGATES:
        raise AssertionError("manifest aggregates")
    if manifest.get("reproduction")!={"deterministic":True,"fresh_generations":2,"byte_identical_copies":3,"random_used":False,"network_used":False,"verify_only_read_only":True}:
        raise AssertionError("manifest reproduction")
    if manifest.get("proof_ceiling")!={"finite_controls_prove_theorem":False,"universal_recover_p":"OPEN_NOT_AUTHORIZED","route_b_authorized":False}:
        raise AssertionError("manifest proof ceiling")
    if any(forbidden in manifest for forbidden in ("self_sha256","result_review","ambient_absolute_path","ambient_timestamp","ambient_host","ambient_pid","ambient_temp_root","dag")):
        raise AssertionError("manifest forbidden key")
    nodes=("A","D","R","G","I","C","M","V")
    edges=(("A","D"),("D","R"),("R","G"),("G","I"),("I","C"),("C","M"),("M","V"),("A","M"),("D","M"),("R","M"),("G","M"),("I","M"))
    incoming={node:0 for node in nodes}; outgoing={node:[] for node in nodes}
    if len(set(edges))!=12:
        raise AssertionError("manifest graph edge cardinality")
    for source,target in edges:
        if source not in incoming or target not in incoming or source==target:
            raise AssertionError("manifest graph edge")
        incoming[target]+=1; outgoing[source].append(target)
    order=[]
    while len(order)<len(nodes):
        ready=[node for node in nodes if incoming[node]==0 and node not in order]
        if len(ready)!=1:
            raise AssertionError("manifest graph unique order")
        node=ready[0]; order.append(node)
        for target in outgoing[node]: incoming[target]-=1
    if tuple(order)!=nodes:
        raise AssertionError("manifest graph order")
    return nodes,edges


def parse_vector(text: str) -> tuple[int,...]:
    if text == "[]":
        return ()
    if re.fullmatch(r"\[(?:0|[1-9][0-9]*)(?:;(?:0|[1-9][0-9]*))*\]",text) is None:
        raise AssertionError("noncanonical vector")
    return tuple(int(value) for value in text[1:-1].split(";"))


def parse_matrix_2x2(text: str) -> tuple[int,int,int,int]:
    match=re.fullmatch(r"\[(0|[1-9][0-9]*);(0|[1-9][0-9]*)\]/\[(0|[1-9][0-9]*);(0|[1-9][0-9]*)\]",text)
    if match is None:
        raise AssertionError("canonical 2x2 matrix")
    return tuple(int(match.group(index)) for index in range(1,5))


def fresh_valuation(number: int, prime: int) -> int:
    if number <= 0 or prime < 2:
        raise AssertionError("valuation domain")
    count = 0
    while number % prime == 0:
        number //= prime
        count += 1
    return count


def fresh_factorization(number: int) -> str:
    if number < 1:
        raise AssertionError("factor domain")
    original = number
    factors: list[tuple[int,int]] = []
    candidate = 2
    while candidate * candidate <= number:
        exponent = 0
        while number % candidate == 0:
            number //= candidate
            exponent += 1
        if exponent:
            factors.append((candidate,exponent))
        candidate += 1
    if number > 1:
        factors.append((number,1))
    if math.prod(prime**exponent for prime,exponent in factors) != original:
        raise AssertionError("factor receipt")
    return "*".join(str(prime) if exponent == 1 else f"{prime}^{exponent}" for prime,exponent in factors) or "1"


def prime_factors(number: int) -> tuple[int,...]:
    values: list[int] = []
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            values.append(divisor)
            while number % divisor == 0:
                number //= divisor
        divisor += 1
    if number > 1:
        values.append(number)
    return tuple(values)


def fresh_order(base: int, modulus: int) -> int:
    candidate = modulus - 1
    for factor in prime_factors(candidate):
        while candidate % factor == 0 and pow(base,candidate//factor,modulus) == 1:
            candidate //= factor
    if pow(base,candidate,modulus) != 1 or any(pow(base,candidate//factor,modulus) == 1 for factor in prime_factors(candidate)):
        raise AssertionError("order witness")
    return candidate


def enumerate_kernel(r: int, target: int, exponents: Sequence[int], numerators: Sequence[int]) -> set[tuple[int,...]]:
    modulus = r ** target
    return {element for element in itertools.product(*(range(r**exponent) for exponent in exponents)) if sum(a*x for a,x in zip(numerators,element)) % modulus == 0}


def multiply_elements(elements: Iterable[tuple[int,...]], multiplier: int, moduli: Sequence[int]) -> set[tuple[int,...]]:
    return {tuple(multiplier*value % modulus for value,modulus in zip(element,moduli)) for element in elements}


def primitive_kappa(p: int, r: int) -> int:
    if p == r:
        return 0
    return fresh_valuation(p*p-1,2)-3 if r == 2 else fresh_valuation(p**(r-1)-1,r)-1


def is_prime(value: int) -> bool:
    return value >= 2 and all(value % divisor for divisor in range(2,math.isqrt(value)+1))


def parse_sg_conclusion(conclusion: bytes) -> tuple[object,...]:
    if not conclusion or not conclusion.isascii():
        raise AssertionError("conclusion bytes")
    text=conclusion.decode("ascii")
    closed = {
        "NO_GLOBAL_CONCLUSION":("NONE","GLOBAL"),
        "FINITE_PAIR_SEPARATION_ONLY":("SEPARATION","FINITE_PAIR"),
        "FINITE_RANGE_ONLY":("RANGE","FINITE"),
        "OPEN_NOT_AUTHORIZED":("OPEN","NOT_AUTHORIZED"),
        "SIGNATURE_MAP_GLOBALLY_INJECTIVE":("INJECTIVE","GLOBAL"),
        "SIGNATURE_MAP_KNOWN_INJECTIVE":("INJECTIVE","KNOWN"),
        "UNIVERSAL_RECOVER_P":("RECOVER_P","UNIVERSAL"),
    }
    if text in closed:
        return closed[text]
    canonical_ge2=r"(?:[2-9]|[1-9][0-9]+)"
    separated=re.fullmatch(rf"r=({canonical_ge2});B_({canonical_ge2})_NOT_ISOMORPHIC_B_({canonical_ge2})",text)
    if separated is not None:
        return ("SEPARATION","COORDINATE",int(separated.group(1)),int(separated.group(2)),int(separated.group(3)))
    isomorphic=re.fullmatch(rf"B_({canonical_ge2})_ISOMORPHIC_B_({canonical_ge2})",text)
    if isomorphic is not None:
        return ("ISOMORPHIC","GLOBAL",int(isomorphic.group(1)),int(isomorphic.group(2)))
    raise AssertionError("closed conclusion grammar")


def SG_SCOPE(projection: Mapping[str,object]) -> tuple[str,str|None,object]:
    forbidden = set(RECEIPT_FIELDS) | {"row_kind"}
    if forbidden.intersection(projection):
        raise AssertionError("receipt reached SG_SCOPE")
    kind = projection.get("kind")
    conclusion = projection.get("proposed_conclusion")
    if not isinstance(conclusion,bytes):
        raise AssertionError("opaque conclusion")
    typed_conclusion=parse_sg_conclusion(conclusion)
    if kind in {"PAIR","PAIR_WITNESS"}:
        p,q = projection.get("p"),projection.get("q")
        coordinates = tuple(projection.get("coordinates",()))
        if not isinstance(p,int) or not isinstance(q,int) or not is_prime(p) or not is_prime(q) or p == q:
            raise AssertionError("primitive pair")
        if len(set(coordinates)) != len(coordinates) or any(not isinstance(r,int) or not is_prime(r) for r in coordinates):
            raise AssertionError("primitive coordinates")
        left = tuple(primitive_kappa(p,r) for r in coordinates)
        right = tuple(primitive_kappa(q,r) for r in coordinates)
        if kind == "PAIR_WITNESS":
            witness = projection.get("distinguishing_coordinate")
            if coordinates.count(witness) != 1 or left[coordinates.index(witness)] == right[coordinates.index(witness)]:
                return "INVALID_WITNESS","SG_WITNESS_INVALID",(left,right)
            licensed = ("SEPARATION","COORDINATE",witness,p,q)
            return "FINITE_PAIR_SEPARATION",None if typed_conclusion == licensed else "SG_RECOVERY_PROMOTION",(left,right)
        derived = "FINITE_COLLISION" if left == right else "FINITE_PAIR_SEPARATION"
        licensed = ("NONE","GLOBAL") if derived == "FINITE_COLLISION" else ("SEPARATION","FINITE_PAIR")
        return derived,None if typed_conclusion == licensed else "SG_PREFIX_PROMOTION",(left,right)
    registry = tuple(projection.get("registry",()))
    if len(set(registry)) != len(registry) or any(not isinstance(p,int) or not is_prime(p) for p in registry):
        raise AssertionError("primitive registry")
    matrix = tuple(tuple(primitive_kappa(p,r) for r in registry) for p in registry)
    if kind == "FINITE_REGISTRY":
        derived = "FINITE_RANGE" if registry else "NO_INFINITE_EVIDENCE"
        licensed = ("RANGE","FINITE") if registry else ("OPEN","NOT_AUTHORIZED")
        return derived,None if typed_conclusion == licensed else "SG_RANGE_PROMOTION",matrix
    if kind == "OPEN_REGISTRY" and projection.get("typed_infinite_witness") == "ABSENT_BY_SCHEMA":
        derived = "FINITE_RANGE" if registry else "NO_INFINITE_EVIDENCE"
        licensed = ("RANGE","FINITE") if registry else ("OPEN","NOT_AUTHORIZED")
        return derived,None if typed_conclusion == licensed else "SG_OPEN_PROMOTION",matrix
    raise AssertionError("SG kind")


FAILURE_TO_DETECTOR = {
    "VC_DOMAIN_INVALID":"E_BRANCH_DOMAIN","VC_ODD_INVALID":"E_NORMALIZATION_ODD","VC_TWO_INVALID":"E_NORMALIZATION_TWO","VC_SIGN_INVALID":"E_TWO_SIGN",
    "EO_BOUNDED_INVALID":"E_BOUNDED_EXTENSION","EO_EXACT_INVALID":"E_EXACT_DOUBLE_VALUATION","FK_ROOT_INVALID":"E_ROOT_NOT_IN_KERNEL",
    "TC_CLOSURE_INVALID":"E_CLOSURE_REQUIRED","TC_FINITE_INVALID":"E_FINITE_MODEL_CEILING","TC_OWNER_INVALID":"E_OWNER_TYPE",
    "SG_PREFIX_PROMOTION":"E_PREFIX_NONPROMOTION","SG_RECOVERY_PROMOTION":"E_RECOVERY_CEILING","SG_RANGE_PROMOTION":"E_RANGE_NONPROMOTION","SG_OPEN_PROMOTION":"E_OPEN_PROBLEM",
    "OF_MARKED_BARE":"E_OWNER_SPLICE","OF_AMBIENT":"E_AMBIENT_IMPORT","OF_ACTUAL":"E_ACTUAL_IMPORT","OF_FLOW":"E_FLOW_IMPORT","OF_HAAR":"E_HAAR_PROMOTION","OF_MEASURE":"E_MEASURE_PROMOTION","OF_TRACE":"E_TRACE_PROMOTION","OF_OPERATOR":"E_OPERATOR_PROMOTION","OF_DETERMINANT":"E_DETERMINANT_PROMOTION",
    "PC_GRH":"E_GRH","PC_DENSITY":"E_DENSITY","PC_PRIORITY":"E_PRIORITY","PC_ROUTE_B":"E_ROUTE_B","PC_RECOVERY":"E_RECOVERY_CEILING","PC_SYMBOLIC":"E_PROOF_CEILING","PC_THEOREM":"E_SOURCE_RECEIPT_CEILING","PC_CHEBOTAREV":"E_CHEBOTAREV_CEILING","PC_ULM":"E_ULM_CEILING",
}


def predicate_vc_domain(row: Mapping[str,str]) -> str|None:
    p,r=int(row["p"]),int(row["r"])
    return None if p==r and is_prime(p) and row["branch"] == "DIAGONAL" else "VC_DOMAIN_INVALID"


def predicate_vc_odd(row: Mapping[str,str]) -> str|None:
    p,r=int(row["p"]),int(row["r"])
    if p==r or not is_prime(p) or not is_prime(r) or r%2!=1:
        return "VC_ODD_INVALID"
    valuation=fresh_valuation(p**(r-1)-1,r)
    return None if row["branch"] == "ODD_OFF_LOCAL" and int(row["raw_valuation"])==valuation and row["normalization_subtrahend"] == "1" and int(row["kappa"])==valuation-1 else "VC_ODD_INVALID"


def predicate_vc_two(row: Mapping[str,str]) -> str|None:
    p,r=int(row["p"]),int(row["r"])
    if r!=2 or p==2 or p%2!=1 or not is_prime(p):
        return "VC_TWO_INVALID"
    valuation=fresh_valuation(p*p-1,2)
    return None if row["branch"] == "TWO_OFF_LOCAL" and int(row["raw_valuation"])==valuation and row["normalization_subtrahend"] == "3" and int(row["kappa"])==valuation-3 else "VC_TWO_INVALID"


def predicate_vc_sign(row: Mapping[str,str]) -> str|None:
    p,r=int(row["p"]),int(row["r"]); expected = "1" if p % 4 == 1 else "-1"
    return None if r==2 and p!=2 and p%2==1 and is_prime(p) and row["branch"] == "TWO_OFF_LOCAL" and row["principal_sign"] == expected else "VC_SIGN_INVALID"


def predicate_eo_bounded(row: Mapping[str,str]) -> str|None:
    p,r,m,ell=map(int,(row["p"],row["r"],row["m"],row["ell"]))
    if not is_prime(p) or not is_prime(r) or not is_prime(ell) or p==ell or re.fullmatch(r"BOUNDED_ORDER_RESTRICTION_(?:NOT_SURJECTIVE|SURJECTIVE)",row["claim_under_test"]) is None:
        return "EO_BOUNDED_INVALID"
    factorization=fresh_factorization(ell-1); order=fresh_order(p,ell)
    characters=tuple(range(16))
    bounded=tuple(character for character in characters if 16//math.gcd(16,character)<=8)
    restricted={character%8 for character in bounded}
    not_surjective=len(restricted)==4 and restricted!={0,1,2,3,4,5,6,7}
    valid = p==r==2 and m==3 and factorization=="2^4" and order==8 and len(bounded)==8 and not_surjective and row["claim_under_test"] == "BOUNDED_ORDER_RESTRICTION_NOT_SURJECTIVE"
    return None if valid else "EO_BOUNDED_INVALID"


def predicate_eo_exact(row: Mapping[str,str]) -> str|None:
    p,r,m,ell = map(int,(row["p"],row["r"],row["m"],row["ell"]))
    if not is_prime(p) or not is_prime(r) or not is_prime(ell) or p==ell or m<0 or re.fullmatch(r"DIVISIBILITY_(?:DOES_NOT_IMPLY|IMPLIES)_EXACT_DEPTH_M",row["claim_under_test"]) is None:
        return "EO_EXACT_INVALID"
    order=fresh_order(p,ell)
    ell_depth=fresh_valuation(ell-1,r); order_depth=fresh_valuation(order,r)
    exact=ell_depth==m and order_depth==m
    expected="DIVISIBILITY_IMPLIES_EXACT_DEPTH_M" if exact else "DIVISIBILITY_DOES_NOT_IMPLY_EXACT_DEPTH_M"
    valid = row["claim_under_test"]==expected
    return None if valid else "EO_EXACT_INVALID"


def predicate_fk_root(row: Mapping[str,str]) -> str|None:
    r,target,depth = int(row["r"]),int(row["target_exponent"]),int(row["depth"])
    exponents=parse_vector(row["source_exponents"]); numerators=parse_vector(row["image_numerators"])
    tail=parse_vector(row["tail_vector"]); root=parse_vector(row["root_vector"])
    if not is_prime(r) or target<=0 or depth<=0 or not exponents or len({len(exponents),len(numerators),len(tail),len(root)})!=1 or any(exponent<=0 for exponent in exponents) or any(value<0 or value>=r**target for value in numerators):
        return "FK_ROOT_INVALID"
    moduli=tuple(r**exponent for exponent in exponents)
    bounded=all(0<=value<modulus for vector in (tail,root) for value,modulus in zip(vector,moduli))
    lifts=tuple((r**depth)*value%modulus for value,modulus in zip(root,moduli))==tail
    phi=sum(coefficient*value for coefficient,value in zip(numerators,root))%(r**target)
    return None if bounded and lifts and phi==0 else "FK_ROOT_INVALID"


def parse_tc_operation(text: str) -> tuple[object,...]:
    closed={
        "ann(closure(Tor(COMPACT_B)))=r^omega(DISCRETE_K)":("EQUALITY","ann(closure(Tor(COMPACT_B)))","r^omega(DISCRETE_K)"),
        "ann(Tor(COMPACT_B))=r^omega(DISCRETE_K)":("EQUALITY","ann(Tor(COMPACT_B))","r^omega(DISCRETE_K)"),
        "r^omega(DISCRETE_K)=ann(closure(Tor(COMPACT_B)))":("EQUALITY","r^omega(DISCRETE_K)","ann(closure(Tor(COMPACT_B)))"),
        "r^omega(DISCRETE_K)=closure(Tor(COMPACT_B))":("EQUALITY","r^omega(DISCRETE_K)","closure(Tor(COMPACT_B))"),
        "FINITE_MODEL_DOES_NOT_PROVE_INFINITE_COMPACT_THEOREM":("FINITE_MODEL",False),
        "FINITE_MODEL_PROVES_INFINITE_COMPACT_THEOREM":("FINITE_MODEL",True),
    }
    if text not in closed: raise AssertionError("closed torsion operation")
    return closed[text]


def predicate_tc_closure(row: Mapping[str,str]) -> str|None:
    parsed=parse_tc_operation(row["operation"])
    return None if parsed==("EQUALITY","ann(closure(Tor(COMPACT_B)))","r^omega(DISCRETE_K)") and (row["source_owner"],row["target_owner"])==("COMPACT_B","DISCRETE_K") else "TC_CLOSURE_INVALID"


def predicate_tc_finite(row: Mapping[str,str]) -> str|None:
    return None if parse_tc_operation(row["operation"]) == ("FINITE_MODEL",False) and (row["source_owner"],row["target_owner"])==("FINITE_COMPACT_DUAL_MODEL","COMPACT_B") else "TC_FINITE_INVALID"


def predicate_tc_owner(row: Mapping[str,str]) -> str|None:
    parsed=parse_tc_operation(row["operation"])
    return None if parsed==("EQUALITY","r^omega(DISCRETE_K)","ann(closure(Tor(COMPACT_B)))") and (row["source_owner"],row["target_owner"])==("DISCRETE_K","COMPACT_B") else "TC_OWNER_INVALID"


OWNER_FAILURES = {
    ("MARKED_EXACT_SEQUENCE","BARE_COMPACT_QUOTIENT"):"OF_MARKED_BARE",("AMBIENT_U_P","BARE_COMPACT_QUOTIENT"):"OF_AMBIENT",("ACTUAL_PACKET_Q_P","BARE_COMPACT_QUOTIENT"):"OF_ACTUAL",("STANDARDIZED_FLOW","BARE_COMPACT_QUOTIENT"):"OF_FLOW",
    ("BARE_COMPACT_QUOTIENT","HAAR_OWNER"):"OF_HAAR",("BARE_COMPACT_QUOTIENT","MEASURED_OWNER"):"OF_MEASURE",("BARE_COMPACT_QUOTIENT","TRACE_OWNER"):"OF_TRACE",("BARE_COMPACT_QUOTIENT","OPERATOR_OWNER"):"OF_OPERATOR",("BARE_COMPACT_QUOTIENT","DETERMINANT_OWNER"):"OF_DETERMINANT",
}


def predicate_owner(row: Mapping[str,str]) -> str|None:
    source,target=row["source_owner"],row["target_owner"]
    owners={value for pair in OWNER_FAILURES for value in pair}
    if source not in owners or target not in owners:
        raise AssertionError("unknown owner enum")
    if source==target:
        return None
    if (source,target) not in OWNER_FAILURES:
        raise AssertionError("unauthorized owner direction")
    return OWNER_FAILURES[(source,target)]


PC_AUTHORITY = {
    ("GRH","NONPROMOTION",""):None,("GRH","PROMOTION",""):"PC_GRH",
    ("DENSITY","NONPROMOTION",""):None,("DENSITY","PROMOTION",""):"PC_DENSITY",
    ("ABSOLUTE_PRIORITY","NONPROMOTION",""):None,("ABSOLUTE_PRIORITY","PROMOTION",""):"PC_PRIORITY",
    ("ROUTE_B","NONPROMOTION",""):None,("ROUTE_B","PROMOTION",""):"PC_ROUTE_B",
    ("UNIVERSAL_RECOVERY","NONPROMOTION",""):None,("UNIVERSAL_RECOVERY","PROMOTION",""):"PC_RECOVERY",
    ("FINITE_CONTROL","NOT_AS","SYMBOLIC_PROOF"):None,("FINITE_CONTROL","AS","SYMBOLIC_PROOF"):"PC_SYMBOLIC",
    ("SOURCE_RECEIPT","NOT_AS","EXECUTED_THEOREM"):None,("SOURCE_RECEIPT","AS","EXECUTED_THEOREM"):"PC_THEOREM",
    ("FINITE_CONTROL","NOT_AS","CHEBOTAREV_PROOF"):None,("FINITE_CONTROL","AS","CHEBOTAREV_PROOF"):"PC_CHEBOTAREV",
    ("FINITE_CONTROL","NOT_AS","ULM_PROOF"):None,("FINITE_CONTROL","AS","ULM_PROOF"):"PC_ULM",
}


def parse_pc_authority(text: str) -> tuple[str,str,str]:
    promotion=re.fullmatch(r"(GRH|DENSITY|ABSOLUTE_PRIORITY|ROUTE_B|UNIVERSAL_RECOVERY)_(NONPROMOTION|PROMOTION)",text)
    if promotion is not None:
        return promotion.group(1),promotion.group(2),""
    proof=re.fullmatch(r"(FINITE_CONTROL|SOURCE_RECEIPT)_(NOT_AS|AS)_(SYMBOLIC_PROOF|EXECUTED_THEOREM|CHEBOTAREV_PROOF|ULM_PROOF)",text)
    if proof is not None:
        return proof.group(1),proof.group(2),proof.group(3)
    raise AssertionError("closed proof-ceiling grammar")


def predicate_pc(row: Mapping[str,str]) -> str|None:
    key=parse_pc_authority(row["prohibited_promotion"])
    if key not in PC_AUTHORITY:
        raise AssertionError("unauthorized proof-ceiling tuple")
    return PC_AUTHORITY[key]


def serialize_projection(header: Sequence[str], projection: Mapping[str,str]) -> bytes:
    if not header or header[0]!="schema_version" or len(set(header))!=len(header) or set(projection)-set(header):
        raise AssertionError("projection schema")
    if "schema_version" in projection and projection["schema_version"]!=SCHEMA:
        raise AssertionError("projection schema override")
    row = {field:"" for field in header}
    row["schema_version"]=SCHEMA
    for field,value in projection.items():
        if not isinstance(value,str):
            raise AssertionError("projection value type")
        row[field] = value
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream,fieldnames=list(header),delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL,doublequote=True,escapechar=None,lineterminator="\n",extrasaction="raise")
    writer.writeheader(); writer.writerow(row)
    return stream.getvalue().encode("utf-8")


def independent_parse_projection(data: bytes, header: Sequence[str]) -> dict[str,str]:
    if data.startswith(b"\xef\xbb\xbf") or b"\r" in data or b"\x00" in data or not data.endswith(b"\n"):
        raise AssertionError("projection bytes")
    reader = csv.reader(io.StringIO(data.decode("utf-8"),newline=""),delimiter=",",quotechar='"',doublequote=True,escapechar=None)
    rows = list(reader)
    if len(rows) != 2 or rows[0] != list(header) or len(rows[1]) != len(header):
        raise AssertionError("projection shape")
    return dict(zip(header,rows[1]))


@dataclass(frozen=True)
class Delta:
    changes: tuple[tuple[str,str,str],...]

    def __post_init__(self) -> None:
        fields=tuple(field for field,_before,_after in self.changes)
        if not fields or len(set(fields))!=len(fields) or any(not field or before==after for field,before,after in self.changes):
            raise AssertionError("invalid atomic delta")

    @property
    def footprint(self) -> frozenset[str]:
        return frozenset(field for field,_before,_after in self.changes)

    def apply(self, state: Mapping[str,str], *, inverse: bool=False) -> dict[str,str]:
        for field,before,after in self.changes:
            expected=after if inverse else before
            if field not in state or state[field]!=expected:
                raise AssertionError("delta precondition")
        result=dict(state)
        for field,before,after in self.changes:
            replacement=before if inverse else after
            result[field]=replacement
        return result


@dataclass(frozen=True,init=False)
class SemanticProgram:
    artifact: str
    row_id: str
    seed: tuple[tuple[str,str],...]
    delta: Delta
    predicate: Callable[[Mapping[str,str]],str|None]
    failure: str
    sg_kind: str = ""

    def __init__(self, artifact: str, row_id: str, seed: Sequence[tuple[str,str]], after: Sequence[tuple[str,str]], changed: frozenset[str], predicate: Callable[[Mapping[str,str]],str|None], failure: str, sg_kind: str="") -> None:
        seed_tuple=tuple(seed); after_tuple=tuple(after)
        if not seed_tuple or len({field for field,_value in seed_tuple})!=len(seed_tuple) or tuple(field for field,_value in seed_tuple)!=tuple(field for field,_value in after_tuple):
            raise AssertionError("semantic program field order")
        delta=Delta(tuple((field,before,after_value) for (field,before),(_after_field,after_value) in zip(seed_tuple,after_tuple) if before!=after_value))
        if not delta.changes or delta.footprint!=changed:
            raise AssertionError("semantic delta footprint")
        object.__setattr__(self,"artifact",artifact); object.__setattr__(self,"row_id",row_id)
        object.__setattr__(self,"seed",seed_tuple); object.__setattr__(self,"delta",delta)
        object.__setattr__(self,"predicate",predicate); object.__setattr__(self,"failure",failure); object.__setattr__(self,"sg_kind",sg_kind)

    def seed_map(self) -> dict[str,str]:
        return dict(self.seed)


def semantic_programs() -> tuple[SemanticProgram,...]:
    fk_common = {
        "S07":("FK-015",2,3,1,"[1;2;3;4]","[4;2;1;1]",1,"[0;0;0;8]","[1;0;0;4]","[0;0;0;4]"),
        "S08":("FK-016",2,3,2,"[1;2;3;5]","[4;2;1;1]",2,"[0;0;0;8]","[0;3;0;2]","[0;0;0;2]"),
        "S09":("FK-017",3,2,1,"[1;2;3]","[3;1;1]",1,"[0;0;9]","[2;0;3]","[0;0;3]"),
        "S10":("FK-018",3,2,2,"[1;2;4]","[3;1;1]",2,"[0;0;9]","[0;8;1]","[0;0;1]"),
    }
    values: list[SemanticProgram] = [
        SemanticProgram(CSV_NAMES[0],"VC-013",(("p","3"),("r","3"),("branch","DIAGONAL")),(("p","3"),("r","3"),("branch","ODD_OFF_LOCAL_INVALID")),frozenset({"branch"}),predicate_vc_domain,"VC_DOMAIN_INVALID"),
        SemanticProgram(CSV_NAMES[0],"VC-014",(("p","7"),("r","5"),("branch","ODD_OFF_LOCAL"),("raw_valuation","2"),("normalization_subtrahend","1"),("kappa","1")),(("p","7"),("r","5"),("branch","ODD_OFF_LOCAL"),("raw_valuation","2"),("normalization_subtrahend","0"),("kappa","2")),frozenset({"normalization_subtrahend","kappa"}),predicate_vc_odd,"VC_ODD_INVALID"),
        SemanticProgram(CSV_NAMES[0],"VC-015",(("p","7"),("r","2"),("branch","TWO_OFF_LOCAL"),("raw_valuation","4"),("normalization_subtrahend","3"),("kappa","1")),(("p","7"),("r","2"),("branch","TWO_OFF_LOCAL"),("raw_valuation","4"),("normalization_subtrahend","2"),("kappa","2")),frozenset({"normalization_subtrahend","kappa"}),predicate_vc_two,"VC_TWO_INVALID"),
        SemanticProgram(CSV_NAMES[0],"VC-016",(("p","3"),("r","2"),("branch","TWO_OFF_LOCAL"),("principal_sign","-1")),(("p","3"),("r","2"),("branch","TWO_OFF_LOCAL"),("principal_sign","")),frozenset({"principal_sign"}),predicate_vc_sign,"VC_SIGN_INVALID"),
        SemanticProgram(CSV_NAMES[1],"EO-013",(("p","2"),("r","2"),("m","3"),("ell","17"),("claim_under_test","BOUNDED_ORDER_RESTRICTION_NOT_SURJECTIVE")),(("p","2"),("r","2"),("m","3"),("ell","17"),("claim_under_test","BOUNDED_ORDER_RESTRICTION_SURJECTIVE")),frozenset({"claim_under_test"}),predicate_eo_bounded,"EO_BOUNDED_INVALID"),
        SemanticProgram(CSV_NAMES[1],"EO-014",(("p","2"),("r","3"),("m","1"),("ell","19"),("claim_under_test","DIVISIBILITY_DOES_NOT_IMPLY_EXACT_DEPTH_M")),(("p","2"),("r","3"),("m","1"),("ell","19"),("claim_under_test","DIVISIBILITY_IMPLIES_EXACT_DEPTH_M")),frozenset({"claim_under_test"}),predicate_eo_exact,"EO_EXACT_INVALID"),
    ]
    for key in ("S07","S08","S09","S10"):
        row,r,target,kappa_value,source,images,depth,tail,root,post_root = fk_common[key]
        seed = (("r",str(r)),("target_exponent",str(target)),("kappa",str(kappa_value)),("source_exponents",source),("image_numerators",images),("depth",str(depth)),("tail_vector",tail),("root_vector",root))
        post = seed[:-1] + (("root_vector",post_root),)
        values.append(SemanticProgram(CSV_NAMES[2],row,seed,post,frozenset({"root_vector"}),predicate_fk_root,"FK_ROOT_INVALID"))
    values.extend((
        SemanticProgram(CSV_NAMES[3],"TC-008",(("source_owner","COMPACT_B"),("operation","ann(closure(Tor(COMPACT_B)))=r^omega(DISCRETE_K)"),("target_owner","DISCRETE_K")),(("source_owner","COMPACT_B"),("operation","ann(Tor(COMPACT_B))=r^omega(DISCRETE_K)"),("target_owner","DISCRETE_K")),frozenset({"operation"}),predicate_tc_closure,"TC_CLOSURE_INVALID"),
        SemanticProgram(CSV_NAMES[3],"TC-009",(("source_owner","FINITE_COMPACT_DUAL_MODEL"),("operation","FINITE_MODEL_DOES_NOT_PROVE_INFINITE_COMPACT_THEOREM"),("target_owner","COMPACT_B")),(("source_owner","FINITE_COMPACT_DUAL_MODEL"),("operation","FINITE_MODEL_PROVES_INFINITE_COMPACT_THEOREM"),("target_owner","COMPACT_B")),frozenset({"operation"}),predicate_tc_finite,"TC_FINITE_INVALID"),
        SemanticProgram(CSV_NAMES[3],"TC-010",(("source_owner","DISCRETE_K"),("operation","r^omega(DISCRETE_K)=ann(closure(Tor(COMPACT_B)))"),("target_owner","COMPACT_B")),(("source_owner","DISCRETE_K"),("operation","r^omega(DISCRETE_K)=closure(Tor(COMPACT_B))"),("target_owner","COMPACT_B")),frozenset({"operation"}),predicate_tc_owner,"TC_OWNER_INVALID"),
    ))
    sg_specs = (
        ("SG-009",(("p","2"),("q","5"),("prime_prefix","[2;3;5;7;11;13]"),("kappa_prefix_p","[0;0;0;0;0;0]"),("kappa_prefix_q","[0;0;0;0;0;0]"),("distinguishing_prime",""),("authorized_conclusion","NO_GLOBAL_CONCLUSION")),"B_2_ISOMORPHIC_B_5","SG_PREFIX_PROMOTION","PAIR"),
        ("SG-010",(("p","2"),("q","3"),("prime_prefix","[2;3;5;7;11;13]"),("kappa_prefix_p","[0;0;0;0;0;0]"),("kappa_prefix_q","[0;0;0;0;1;0]"),("distinguishing_prime","11"),("authorized_conclusion","r=11;B_2_NOT_ISOMORPHIC_B_3")),"UNIVERSAL_RECOVER_P","SG_RECOVERY_PROMOTION","PAIR_WITNESS"),
        ("SG-011",(("prime_prefix","[2;3;5;7;11;13]"),("authorized_conclusion","FINITE_RANGE_ONLY")),"SIGNATURE_MAP_GLOBALLY_INJECTIVE","SG_RANGE_PROMOTION","FINITE_REGISTRY"),
        ("SG-012",(("prime_prefix",""),("authorized_conclusion","OPEN_NOT_AUTHORIZED")),"SIGNATURE_MAP_KNOWN_INJECTIVE","SG_OPEN_PROMOTION","OPEN_REGISTRY"),
    )
    for row,seed,new_conclusion,failure,kind in sg_specs:
        post = tuple((field,new_conclusion if field == "authorized_conclusion" else value) for field,value in seed)
        values.append(SemanticProgram(CSV_NAMES[4],row,seed,post,frozenset({"authorized_conclusion"}),predicate_sg,failure,kind))
    owner_specs = (("OF-007","MARKED_EXACT_SEQUENCE","BARE_COMPACT_QUOTIENT","OF_MARKED_BARE"),("OF-008","AMBIENT_U_P","BARE_COMPACT_QUOTIENT","OF_AMBIENT"),("OF-009","ACTUAL_PACKET_Q_P","BARE_COMPACT_QUOTIENT","OF_ACTUAL"),("OF-010","STANDARDIZED_FLOW","BARE_COMPACT_QUOTIENT","OF_FLOW"),("OF-011","BARE_COMPACT_QUOTIENT","HAAR_OWNER","OF_HAAR"),("OF-012","BARE_COMPACT_QUOTIENT","MEASURED_OWNER","OF_MEASURE"),("OF-013","BARE_COMPACT_QUOTIENT","TRACE_OWNER","OF_TRACE"),("OF-014","BARE_COMPACT_QUOTIENT","OPERATOR_OWNER","OF_OPERATOR"),("OF-015","BARE_COMPACT_QUOTIENT","DETERMINANT_OWNER","OF_DETERMINANT"))
    for row,source,target,failure in owner_specs:
        values.append(SemanticProgram(CSV_NAMES[5],row,(("source_owner",source),("target_owner",source)),(("source_owner",source),("target_owner",target)),frozenset({"target_owner"}),predicate_owner,failure))
    pc_specs = (("PC-018","GRH_NONPROMOTION","GRH_PROMOTION","PC_GRH"),("PC-019","DENSITY_NONPROMOTION","DENSITY_PROMOTION","PC_DENSITY"),("PC-020","ABSOLUTE_PRIORITY_NONPROMOTION","ABSOLUTE_PRIORITY_PROMOTION","PC_PRIORITY"),("PC-021","ROUTE_B_NONPROMOTION","ROUTE_B_PROMOTION","PC_ROUTE_B"),("PC-022","UNIVERSAL_RECOVERY_NONPROMOTION","UNIVERSAL_RECOVERY_PROMOTION","PC_RECOVERY"),("PC-023","FINITE_CONTROL_NOT_AS_SYMBOLIC_PROOF","FINITE_CONTROL_AS_SYMBOLIC_PROOF","PC_SYMBOLIC"),("PC-024","SOURCE_RECEIPT_NOT_AS_EXECUTED_THEOREM","SOURCE_RECEIPT_AS_EXECUTED_THEOREM","PC_THEOREM"),("PC-025","FINITE_CONTROL_NOT_AS_CHEBOTAREV_PROOF","FINITE_CONTROL_AS_CHEBOTAREV_PROOF","PC_CHEBOTAREV"),("PC-026","FINITE_CONTROL_NOT_AS_ULM_PROOF","FINITE_CONTROL_AS_ULM_PROOF","PC_ULM"))
    for row,seed,post,failure in pc_specs:
        values.append(SemanticProgram(CSV_NAMES[6],row,(("prohibited_promotion",seed),),(("prohibited_promotion",post),),frozenset({"prohibited_promotion"}),predicate_pc,failure))
    if len(values) != 35:
        raise AssertionError("semantic registry cardinality")
    return tuple(values)


def predicate_sg_with_kind(row: Mapping[str,str], kind: str) -> str|None:
    coordinates = parse_vector(row.get("prime_prefix","")) if row.get("prime_prefix","") else ()
    if kind == "PAIR":
        p,q=int(row["p"]),int(row["q"])
        left=tuple(primitive_kappa(p,r) for r in coordinates); right=tuple(primitive_kappa(q,r) for r in coordinates)
        if parse_vector(row["kappa_prefix_p"])!=left or parse_vector(row["kappa_prefix_q"])!=right:
            return "SG_PREFIX_PROMOTION"
        projection = {"kind":kind,"p":p,"q":q,"coordinates":coordinates,"proposed_conclusion":row["authorized_conclusion"].encode("ascii")}
    elif kind == "PAIR_WITNESS":
        p,q=int(row["p"]),int(row["q"])
        left=tuple(primitive_kappa(p,r) for r in coordinates); right=tuple(primitive_kappa(q,r) for r in coordinates)
        if parse_vector(row["kappa_prefix_p"])!=left or parse_vector(row["kappa_prefix_q"])!=right:
            return "SG_RECOVERY_PROMOTION"
        projection = {"kind":kind,"p":p,"q":q,"coordinates":coordinates,"distinguishing_coordinate":int(row["distinguishing_prime"]),"proposed_conclusion":row["authorized_conclusion"].encode("ascii")}
    elif kind == "FINITE_REGISTRY":
        projection = {"kind":kind,"registry":coordinates,"proposed_conclusion":row["authorized_conclusion"].encode("ascii")}
    else:
        projection = {"kind":"OPEN_REGISTRY","registry":coordinates,"typed_infinite_witness":"ABSENT_BY_SCHEMA","proposed_conclusion":row["authorized_conclusion"].encode("ascii")}
    return SG_SCOPE(projection)[1]


def predicate_sg(row: Mapping[str,str]) -> str|None:
    raise AssertionError("SG_SCOPE requires the program's unparameterized primitive kind")


PROGRAMS = semantic_programs()


def open_root(argument: str) -> int:
    if not argument or "\x00" in argument:
        raise AssertionError("root argument")
    fd = os.open(argument,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW|os.O_CLOEXEC)
    st = os.fstat(fd)
    if not stat.S_ISDIR(st.st_mode):
        os.close(fd)
        raise AssertionError("root type")
    return fd


def read_root_member(root_fd: int, name: str) -> bytes:
    if name not in GENERATED_NAMES:
        raise AssertionError("member registry")
    fd = os.open(name,os.O_RDONLY|os.O_NOFOLLOW|os.O_CLOEXEC,dir_fd=root_fd)
    try:
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1:
            raise AssertionError("member identity")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(fd,65536)
            if not chunk:
                return b"".join(chunks)
            chunks.append(chunk)
    finally:
        os.close(fd)


def parse_csv_bytes(data: bytes, expected_header: Sequence[str]) -> list[dict[str,str]]:
    if data.startswith(b"\xef\xbb\xbf") or b"\r" in data or b"\x00" in data or not data.endswith(b"\n") or data.endswith(b"\n\n"):
        raise AssertionError("CSV canonical bytes")
    reader = csv.DictReader(io.StringIO(data.decode("utf-8"),newline=""),delimiter=",",quotechar='"',doublequote=True,escapechar=None)
    if reader.fieldnames != list(expected_header):
        raise AssertionError("CSV header")
    rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise AssertionError("CSV width")
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream,fieldnames=list(expected_header),delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL,doublequote=True,escapechar=None,lineterminator="\n",extrasaction="raise")
    writer.writeheader(); writer.writerows(rows)
    if stream.getvalue().encode("utf-8") != data:
        raise AssertionError("CSV round trip")
    return rows


def parse_fields(record: str, name: str, fields: Sequence[tuple[str,str]]) -> dict[str,str]:
    pieces = [re.escape(name)]
    for field,grammar in fields:
        pieces.append(re.escape(field)+"=(?P<"+field+">"+grammar+")")
    match = re.fullmatch(" ".join(pieces),record)
    if match is None:
        raise AssertionError("closed wire grammar: "+name)
    return match.groupdict()


def p_owned_endpoint_coordinates() -> tuple[int,int]:
    namespace=globals()
    if set(("P15R_AUDIT_HANDLE","P15R_AUTH_SERIAL"))-set(namespace):
        raise AssertionError("missing P-issued endpoint coordinates")
    audit,auth_serial=namespace["P15R_AUDIT_HANDLE"],namespace["P15R_AUTH_SERIAL"]
    if type(audit) is not int or audit<0 or type(auth_serial) is not int or auth_serial!=0:
        raise AssertionError("invalid P-issued endpoint coordinates")
    return audit,auth_serial


class GuardianClient:
    """Exact requester endpoint: FD4 RPC and child-unique FD5 audit/auth."""

    def __init__(self) -> None:
        self.rpc = socket.socket(fileno=4)
        self.audit = socket.socket(fileno=5)
        if self.rpc.type & socket.SOCK_SEQPACKET != socket.SOCK_SEQPACKET or self.audit.type & socket.SOCK_SEQPACKET != socket.SOCK_SEQPACKET:
            raise AssertionError("request endpoint type")
        self.request = 0
        self.audit_id,self.auth_serial = p_owned_endpoint_coordinates()
        self.audit_serial = 0
        self.auth = ""
        self.session = ""
        self.active_cap = ""
        self.pending_spawns: dict[int,bytes] = {}
        self.consumed_spawn_children: set[int] = set()
        self.closed = False
        self._authenticate()

    @staticmethod
    def _ascii(text: str) -> bytes:
        data = text.encode("ascii")
        if not data or len(data) > MAX_PACKET or b"\x00" in data or b"\n" in data:
            raise AssertionError("wire ASCII")
        return data

    def bare_send(self, text: str) -> None:
        data = self._ascii(text)
        if self.audit.send(data) != len(data):
            raise AssertionError("FD5 short send")

    def bare_send_bytes(self, data: bytes) -> None:
        if not data or len(data) > MAX_PACKET or b"\x00" in data or b"\n" in data or not data.isascii():
            raise AssertionError("FD5 raw bytes")
        if self.audit.send(data) != len(data):
            raise AssertionError("FD5 raw short send")

    def bare_receive(self) -> str:
        data,ancillary,flags,_address = self.audit.recvmsg(MAX_PACKET+1,1)
        if ancillary or flags & (socket.MSG_TRUNC|socket.MSG_CTRUNC) or not data or len(data) > MAX_PACKET or b"\x00" in data or b"\n" in data or not data.isascii():
            raise AssertionError("FD5 receive")
        return data.decode("ascii")

    def framed_send(self, text: str) -> None:
        payload = self._ascii(text)
        packet = struct.pack(">I",len(payload))+payload
        if self.rpc.send(packet) != len(packet):
            raise AssertionError("FD4 short send")

    def framed_send_payload(self, payload: bytes) -> None:
        if not payload or len(payload) > MAX_PACKET or b"\x00" in payload or b"\n" in payload or not payload.isascii():
            raise AssertionError("FD4 raw payload")
        packet = struct.pack(">I",len(payload))+payload
        if self.rpc.send(packet) != len(packet):
            raise AssertionError("FD4 raw payload short send")

    def framed_send_bytes(self, packet: bytes) -> None:
        if len(packet) < 5 or len(packet)-4 != struct.unpack(">I",packet[:4])[0] or len(packet)-4 > MAX_PACKET:
            raise AssertionError("FD4 raw frame")
        if self.rpc.send(packet) != len(packet):
            raise AssertionError("FD4 raw short send")

    def framed_receive(self) -> str:
        packet,ancillary,flags,_address = self.rpc.recvmsg(MAX_PACKET+5,1)
        if ancillary or flags & (socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(packet) < 5:
            raise AssertionError("FD4 packet")
        size = struct.unpack(">I",packet[:4])[0]
        payload = packet[4:]
        if size == 0 or size > MAX_PACKET or len(payload) != size or b"\x00" in payload or b"\n" in payload or not payload.isascii():
            raise AssertionError("FD4 frame")
        return payload.decode("ascii")

    def _authenticate(self) -> None:
        self.request += 1
        method = "test_pkg_001"
        trigger = "NONE"
        owner = "SUITE_173"
        self.bare_send(f"SESSION_AUTH_OPEN audit={self.audit_id} auth_serial={self.auth_serial} request={self.request} method={method} trigger={trigger} owner={owner}")
        challenge = parse_fields(self.bare_receive(),"SESSION_AUTH_CHALLENGE",(("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*")))
        if challenge["audit"] != str(self.audit_id) or challenge["auth_serial"] != str(self.auth_serial):
            raise AssertionError("auth challenge join")
        self.auth,self.session = challenge["auth"],challenge["session"]
        registration = f"request={self.request} method={method} trigger={trigger} owner={owner} fd4_inode={os.fstat(4).st_ino} rpc_inner_pid={os.getpid()} rpc_inner_uid=0 rpc_inner_gid=0"
        registration_bytes = registration.encode("ascii")
        digest = sha256(registration_bytes)
        self.bare_send(f"SESSION_AUTH_REGISTERED audit={self.audit_id} auth_serial={self.auth_serial} auth={self.auth} session={self.session} request={self.request} method={method} trigger={trigger} owner={owner} registration={registration_bytes.hex()} digest={digest}")
        receipt = parse_fields(self.bare_receive(),"SESSION_AUTH_RECEIPT",(("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("digest",r"[0-9a-f]{64}"),("create_cap",r"[0-9a-f]{64}"),("create",r"(?:[0-9a-f]{2})+")))
        if (receipt["auth"],receipt["session"],receipt["request"],receipt["digest"]) != (self.auth,self.session,str(self.request),digest):
            raise AssertionError("auth receipt join")
        create_frame = bytes.fromhex(receipt["create"])
        if receipt["create_cap"].encode("ascii") not in create_frame:
            raise AssertionError("create capability source")
        self.framed_send_bytes(create_frame)
        created = parse_fields(self.framed_receive(),"SESSION_CREATED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("reply_nonce",r"[0-9a-f]{64}")))
        if created["request"] != str(self.request):
            raise AssertionError("create reply")
        created_payload = f"SESSION_CREATED request={created['request']} session={created['session']} reply_nonce={created['reply_nonce']}".encode("ascii")
        self.bare_send(f"SESSION_AUTH_ACTIVATED audit={self.audit_id} auth_serial={self.auth_serial} auth={self.auth} session={self.session} request={self.request} reply_nonce={created['reply_nonce']} created={created_payload.hex()}")
        active = parse_fields(self.bare_receive(),"SESSION_AUTH_ACTIVE_RECEIPT",(("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("active_cap",r"[0-9a-f]{64}"),("created_digest",r"[0-9a-f]{64}")))
        if (active["auth"],active["session"],active["request"]) != (self.auth,self.session,str(self.request)) or active["created_digest"] != sha256(created_payload):
            raise AssertionError("active receipt")
        self.active_cap = active["active_cap"]

    def next_request(self) -> int:
        self.request += 1
        return self.request

    def audited_spawn(self, core: str, trigger: str) -> bytes:
        audit = self.audit_id
        serial = self.audit_serial
        self.bare_send(f"AUDIT_OPEN audit={audit} serial={serial}")
        challenge = parse_fields(self.bare_receive(),"AUDIT_CHALLENGE",(("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}")))
        if (challenge["audit"],challenge["serial"]) != (str(audit),str(serial)):
            raise AssertionError("audit challenge")
        core_bytes = core.encode("ascii")
        digest = sha256(core_bytes)
        outer = f"AUDITED_SPAWN audit={audit} serial={serial} nonce={challenge['nonce']} digest={digest} trigger={trigger} core={core_bytes.hex()}".encode("ascii")
        self.bare_send_bytes(outer)
        receipt = parse_fields(self.bare_receive(),"AUDIT_RECEIPT",(("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}")))
        if receipt != {"audit":str(audit),"serial":str(serial),"nonce":challenge["nonce"],"digest":digest}:
            raise AssertionError("audit receipt")
        self.audit_serial += 1
        return outer

    def request_reply(self, request: str, reply_name: str, fields: Sequence[tuple[str,str]]) -> dict[str,str]:
        self.framed_send(request)
        return parse_fields(self.framed_receive(),reply_name,fields)

    def spawn(self, session: str, target: str, method: str, purpose: str, handle: str, trigger: str = "NONE") -> tuple[int,bytes,bytes]:
        request = self.next_request()
        core = f"SPAWN request={request} session={session} target={target} method={method} purpose={purpose} handle={handle}"
        authorization = self.audited_spawn(core,trigger)
        if request in self.pending_spawns:
            raise AssertionError("duplicate pending spawn")
        outer = parse_fields(authorization.decode("ascii"),"AUDITED_SPAWN",(("audit",re.escape(str(self.audit_id))),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}"),("trigger",re.escape(trigger)),("core",r"(?:[0-9a-f]{2})+")))
        core_bytes=bytes.fromhex(outer["core"])
        if core_bytes!=core.encode("ascii") or outer["digest"]!=sha256(core_bytes):
            raise AssertionError("pending spawn authorization")
        self.pending_spawns[request]=authorization
        self.framed_send_payload(authorization)
        stdout = bytearray(); stderr = bytearray()
        stdout_seq = stderr_seq = 0
        while True:
            record = self.framed_receive()
            stdout_match = re.fullmatch(rf"SPAWN_STDOUT request={request} seq=(0|[1-9][0-9]*) hex=([0-9a-f]*)",record)
            stderr_match = re.fullmatch(rf"SPAWN_STDERR request={request} seq=(0|[1-9][0-9]*) hex=([0-9a-f]*)",record)
            if stdout_match is not None:
                if int(stdout_match.group(1)) != stdout_seq: raise AssertionError("stdout order")
                encoded=stdout_match.group(2)
                if len(encoded)>2048 or len(encoded)%2: raise AssertionError("stdout chunk")
                chunk=bytes.fromhex(encoded)
                if len(stdout)+len(chunk)>STREAM_LIMIT: raise AssertionError("stdout ceiling")
                stdout.extend(chunk); stdout_seq += 1
            elif stderr_match is not None:
                if int(stderr_match.group(1)) != stderr_seq: raise AssertionError("stderr order")
                encoded=stderr_match.group(2)
                if len(encoded)>2048 or len(encoded)%2: raise AssertionError("stderr chunk")
                chunk=bytes.fromhex(encoded)
                if len(stderr)+len(chunk)>STREAM_LIMIT: raise AssertionError("stderr ceiling")
                stderr.extend(chunk); stderr_seq += 1
            elif record.startswith("SPAWN_RESULT "):
                pending=self.pending_spawns.get(request)
                if pending is None or pending!=authorization:
                    raise AssertionError("spawn result without pending authorization")
                result=parse_fields(record,"SPAWN_RESULT",(
                    ("request",re.escape(str(request))),("audit",re.escape(outer["audit"])),("serial",re.escape(outer["serial"])),
                    ("nonce",re.escape(outer["nonce"])),("digest",re.escape(outer["digest"])),("outer_sha256",re.escape(sha256(pending))),
                    ("target",re.escape(target)),("method",re.escape(method)),("purpose",re.escape(purpose)),("handle",re.escape(handle)),
                    ("child",r"[1-9][0-9]*"),("status",r"(?:0|[1-9][0-9]*)"),("outcome",r"EXITED"),
                    ("stdout_bytes",r"(?:0|[1-9][0-9]*)"),("stderr_bytes",r"(?:0|[1-9][0-9]*)"),
                    ("stdout_chunks",r"(?:0|[1-9][0-9]*)"),("stderr_chunks",r"(?:0|[1-9][0-9]*)"),
                    ("stdout_sha256",r"[0-9a-f]{64}"),("stderr_sha256",r"[0-9a-f]{64}"),("capability_sha256",r"[0-9a-f]{64}"),
                ))
                child=int(result["child"])
                if child in self.consumed_spawn_children or int(result["stdout_bytes"])!=len(stdout) or int(result["stderr_bytes"])!=len(stderr) or int(result["stdout_chunks"])!=stdout_seq or int(result["stderr_chunks"])!=stderr_seq:
                    raise AssertionError("spawn cardinality")
                if sha256(bytes(stdout))!=result["stdout_sha256"] or sha256(bytes(stderr))!=result["stderr_sha256"]:
                    raise AssertionError("spawn digest")
                result_core=record.rsplit(" capability_sha256=",1)[0].encode("ascii")
                capability=sha256(b"P15R-SPAWN-RESULT-CAP-v1"+struct.pack(">Q",len(result_core))+result_core)
                if capability!=result["capability_sha256"]:
                    raise AssertionError("spawn capability")
                self.pending_spawns.pop(request)
                self.consumed_spawn_children.add(child)
                return int(result["status"]),bytes(stdout),bytes(stderr)
            else:
                raise AssertionError("spawn reply enum")

    def close(self) -> None:
        if self.closed:
            raise AssertionError("duplicate top close")
        request = self.next_request()
        self.framed_send(f"SESSION_CLOSE request={request} session={self.session} active_cap={self.active_cap}")
        packet,ancillary,flags,_address = self.rpc.recvmsg(MAX_PACKET+5,1)
        if ancillary or flags & (socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(packet) < 5 or len(packet)-4 != struct.unpack(">I",packet[:4])[0]:
            raise AssertionError("terminal frame")
        payload = packet[4:].decode("ascii")
        terminal = parse_fields(payload,"SESSION_CLOSED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("terminal_cap",r"[0-9a-f]{64}")))
        digest = sha256(b"P15R-TERMINAL-REPLY-v7 "+packet)
        self.bare_send(f"SESSION_AUTH_TERMINAL_OBSERVED audit={self.audit_id} auth_serial={self.auth_serial} auth={self.auth} session={self.session} close_request={request} outcome={terminal['outcome']} terminal_cap={terminal['terminal_cap']} reply_digest={digest} reply={packet.hex()}")
        receipt = parse_fields(self.bare_receive(),"SESSION_AUTH_TERMINAL_RECEIPT",(("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("close_request",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("terminal_cap_sha256",r"[0-9a-f]{64}"),("reply_digest",r"[0-9a-f]{64}")))
        if receipt["reply_digest"] != digest or receipt["close_request"] != str(request):
            raise AssertionError("terminal receipt")
        self.rpc.close(); self.audit.close(); self.closed = True


@dataclass(frozen=True)
class MutationSurface:
    method: str
    mutation: str
    kind: str
    coordinate: str
    before: str
    after: str
    variants: int = 1
    target: str = "VERIFY_ONLY_GENERATOR"
    trigger: str = "NONE"


PACKAGE_DETECTORS = (
    ("test_package_p01_cell_content_tamper","P01",1,"E_ARTIFACT_SHA256"),
    ("test_package_p02_header_tamper","P02",1,"E_HEADER"),
    ("test_package_p03_stale_row_count","P03",1,"E_ROW_COUNT"),
    ("test_package_p04_row_reorder","P04",1,"E_ROW_ORDER"),
    ("test_package_p05_missing_csv","P05",1,"E_MISSING_ARTIFACT"),
    ("test_package_p06_extra_csv","P06",1,"E_EXTRA_ARTIFACT"),
    ("test_package_p07_missing_manifest","P07",1,"E_MANIFEST_MISSING"),
    ("test_package_p08_extra_file","P08",1,"E_EXTRA_FILE"),
    ("test_package_p09_extra_directory","P09",1,"E_EXTRA_DIRECTORY"),
    ("test_package_p10_manifest_field_tamper","P10",1,"E_MANIFEST_SEMANTICS"),
    ("test_package_p11_manifest_self_hash","P11",1,"E_MANIFEST_CYCLE"),
    ("test_package_p12_authority_binding_drift","P12",1,"E_AUTHORITY_BINDING"),
    ("test_package_p13_design_lock_drift","P13",1,"E_DESIGN_BINDING"),
    ("test_package_p14_design_review_drift","P14",1,"E_REVIEW_BINDING"),
    ("test_package_p15_implementation_gate_drift","P15",1,"E_IMPLEMENTATION_GATE_BINDING"),
    ("test_package_p16_implementation_digest_drift","P16",1,"E_IMPLEMENTATION_BINDING"),
    ("test_package_p17_symlink_input","P17",1,"E_SYMLINK"),
    ("test_package_p18_hardlink_input","P18",1,"E_HARDLINK"),
    ("test_package_p19_pre_run_cache","P19",1,"E_CACHE_PRE"),
    ("test_package_p20_post_run_cache","P20",1,"E_CACHE_POST"),
    ("test_package_p21_recursive_entry","P21",1,"E_RECURSIVE_ENTRY"),
    ("test_package_p22_concurrent_second_entry","P22",1,"E_CONCURRENT_ENTRY"),
    ("test_package_p23_verify_only_repair_attempt","P23",1,"E_VERIFY_ONLY_WRITE"),
    ("test_package_p24_forced_cleanup_failure","P24",1,"E_CLEANUP"),
    ("test_package_p25_nonempty_generation_root","P25",1,"E_NONEMPTY_OUTPUT"),
    ("test_package_p26_future_result_cycle_edge","P26",1,"E_DAG_CYCLE"),
    ("test_package_p27_ambient_metadata","P27",5,"E_NONCANONICAL_METADATA"),
    ("test_package_p28_noncanonical_json_or_newline","P28",2,"E_CANONICAL_BYTES"),
)


def independent_package_detector(surface: MutationSurface) -> str:
    if tuple(row[1] for row in PACKAGE_DETECTORS)!=tuple(f"P{index:02d}" for index in range(1,29)) or len({row[0] for row in PACKAGE_DETECTORS})!=28 or len({row[3] for row in PACKAGE_DETECTORS})!=28:
        raise AssertionError("detector registry closure")
    matches=[row for row in PACKAGE_DETECTORS if (row[0],row[1])==(surface.method,surface.mutation)]
    if len(matches)!=1 or matches[0][2]!=surface.variants:
        raise AssertionError("detector method/variant registry")
    return matches[0][3]


def variant_value(value: str, variant: int, variants: int) -> str:
    values = value.split("||")
    if len(values) == 1:
        return value
    if len(values) != variants:
        raise AssertionError("variant literal cardinality")
    return values[variant-1]


def receipt_compare(before: Sequence[tuple[object,...]], after: Sequence[tuple[object,...]]) -> str|None:
    return None if tuple(before) == tuple(after) else "E_VERIFY_ONLY_METADATA"


def tuple_differences(before: Sequence[tuple[object,...]], after: Sequence[tuple[object,...]], coordinates: Sequence[str]) -> set[tuple[object,...]]:
    if len(before) != len(after):
        raise AssertionError("receipt cardinality")
    differences: set[tuple[object,...]] = set()
    for left,right in zip(before,after):
        if len(left) != len(coordinates) or len(right) != len(coordinates) or left[0] != right[0]:
            raise AssertionError("receipt shape")
        for index,name in enumerate(coordinates):
            if left[index] != right[index]:
                differences.add((left[0],name,left[index],right[index]))
    return differences


def validate_actual_receipt(receipt: object) -> tuple[tuple[object,...],...]:
    if not isinstance(receipt,(list,tuple)):
        raise AssertionError("receipt container")
    rows=tuple(tuple(cell for cell in row) if isinstance(row,(list,tuple)) else () for row in receipt)
    if any(len(row)!=10 for row in rows):
        raise AssertionError("receipt width")
    paths: list[str]=[]
    for path,kind,mode,size,digest,mtime_ns,ctime_ns,nlink,dev,ino in rows:
        if not isinstance(path,str) or not path or "\x00" in path or path.startswith("/"):
            raise AssertionError("receipt path")
        if path!="." and any(part in ("",".","..") for part in path.split("/")):
            raise AssertionError("receipt relative path")
        if kind not in ("REGULAR","DIRECTORY") or type(mode) is not int or not 0<=mode<=0o7777:
            raise AssertionError("receipt type/mode")
        integers=(size,mtime_ns,ctime_ns,nlink,dev,ino)
        if any(type(value) is not int for value in integers) or size<0 or mtime_ns<0 or ctime_ns<0 or nlink<1 or dev<0 or ino<1:
            raise AssertionError("receipt integer domain")
        if not isinstance(digest,str) or (kind=="REGULAR" and re.fullmatch(r"[0-9a-f]{64}",digest) is None) or (kind=="DIRECTORY" and digest!=""):
            raise AssertionError("receipt digest")
        paths.append(path)
    if not rows or paths.count(".")!=1 or rows[paths.index(".")][1]!="DIRECTORY" or paths!=sorted(paths,key=lambda value:value.encode("utf-8")) or len(set(paths))!=len(paths):
        raise AssertionError("receipt inventory")
    return rows


class ControlsOracle(unittest.TestCase):
    root_arguments: tuple[str,str,str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.root_fds = tuple(open_root(argument) for argument in cls.root_arguments)
        identities = [(os.fstat(fd).st_dev,os.fstat(fd).st_ino) for fd in cls.root_fds]
        if len(set(identities)) != 3:
            raise AssertionError("three roots are not distinct")
        cls.tables: list[dict[str,list[dict[str,str]]]] = []
        cls.raw: list[dict[str,bytes]] = []
        cls.manifests: list[dict[str,object]] = []
        for root_fd in cls.root_fds:
            table_set: dict[str,list[dict[str,str]]] = {}
            raw_set: dict[str,bytes] = {}
            for name,header in zip(CSV_NAMES,HEADERS):
                data = read_root_member(root_fd,name)
                raw_set[name] = data
                table_set[name] = parse_csv_bytes(data,header)
            manifest_data = read_root_member(root_fd,"manifest.json")
            manifest = json.loads(manifest_data.decode("utf-8"))
            if canonical_json(manifest) != manifest_data or not isinstance(manifest,dict):
                raise AssertionError("manifest canonical")
            independent_manifest_graph(manifest,raw_set)
            cls.tables.append(table_set); cls.raw.append(raw_set); cls.manifests.append(manifest)
        cls.client = GuardianClient()

    @classmethod
    def tearDownClass(cls) -> None:
        failure: BaseException|None = None
        try:
            cls.client.close()
        except BaseException as error:
            failure = error
        for fd in cls.root_fds:
            try: os.close(fd)
            except OSError as error:
                if failure is None: failure = error
        if failure is not None:
            raise failure

    def rows(self, name: str, copy_index: int = 0) -> list[dict[str,str]]:
        return self.tables[copy_index][name]

    def row(self, name: str, row_id: str) -> dict[str,str]:
        matches = [row for row in self.rows(name) if row["row_id"] == row_id]
        self.assertEqual(len(matches),1)
        return dict(matches[0])

    def family_check(self, family: str, index: int) -> None:
        name_index = {"val":0,"ord":1,"ker":2,"tor":3,"sig":4,"own":5,"ceil":6,"sum":7}[family]
        name = CSV_NAMES[name_index]; rows = self.rows(name)
        if index == 1: self.assertEqual(list(rows[0]),HEADERS[name_index])
        elif index == 2: self.assertEqual([row["row_id"] for row in rows],[f"{PREFIXES[name_index]}-{number:03d}" for number in range(1,ROW_COUNTS[name_index]+1)])
        elif index == 3: self.assertTrue(all(row["schema_version"] == SCHEMA for row in rows))
        elif index == 4: self.assertEqual(sum(row.get("case_kind") == "NEGATIVE" for row in rows),NEGATIVE_COUNTS[name_index])
        elif index == 5: self.assertTrue(all(row["status"] == "PASS" for row in rows))
        elif index == 6: self.assertEqual(len(HEADERS[name_index]),WIDTHS[name_index])
        elif index == 7: self.assertEqual(len(rows),ROW_COUNTS[name_index])
        elif index == 8: self.assertEqual(len({row["row_id"] for row in rows}),len(rows))
        elif index == 9: self.assertEqual(self.raw[0][name],self.raw[1][name])
        elif index == 10: self.assertEqual(self.raw[1][name],self.raw[2][name])
        elif index == 11: self.assertFalse(any("ULM_THEOREM_PROVED" in value for row in rows for value in row.values()))
        elif index == 12: self.assertTrue(all("\n" not in value and "\r" not in value for row in rows for value in row.values()))
        elif index == 13: self.assertEqual(sum(bool(row.get("mutation_id")) for row in rows),NEGATIVE_COUNTS[name_index])
        elif index == 14: self.assertTrue(all(row.get("tolerance","") in {"","0"} for row in rows))
        else: raise AssertionError("family index")

    @staticmethod
    def semantic_predicate(program: SemanticProgram, row: Mapping[str,str]) -> str|None:
        if program.sg_kind:
            return predicate_sg_with_kind(row,program.sg_kind)
        return program.predicate(row)

    def run_semantic(self, program_index: int) -> None:
        program = PROGRAMS[program_index]
        header = HEADERS[CSV_NAMES.index(program.artifact)]

        def projection(state: Mapping[str,str]) -> dict[str,str]:
            return {field:state[field] for field,_value in program.seed}

        def complete_diff(left: Mapping[str,str], right: Mapping[str,str]) -> tuple[tuple[str,str,str],...]:
            if set(left)!=set(right):
                raise AssertionError("semantic state keys")
            return tuple((field,left[field],right[field]) for field in header if left[field]!=right[field])

        # 1. Primitive literal seed -> canonical serialization -> independent
        # parse/type check -> acceptance.  No detector registry is touched.
        seed_literal = program.seed_map()
        seed_bytes = serialize_projection(header,seed_literal)
        seed = independent_parse_projection(seed_bytes,header)
        seed_projection = projection(seed)
        self.assertIsNone(self.semantic_predicate(program,seed_projection),"E_INVALID_SEED")

        # 2. Apply one typed atomic delta to the parsed seed.  Validation of
        # every before-value precedes all replacements.
        post_state=program.delta.apply(seed)
        self.assertIsNot(post_state,seed)
        self.assertEqual(complete_diff(seed,post_state),program.delta.changes)
        self.assertEqual(program.delta.footprint,frozenset(field for field,_before,_after in complete_diff(seed,post_state)))
        self.assertEqual(seed,independent_parse_projection(seed_bytes,header))

        # 3. Embed in the exact artifact header and use a new serializer/parser.
        post_bytes = serialize_projection(tuple(header),post_state)
        post_row = independent_parse_projection(bytes(post_bytes),tuple(header))
        self.assertEqual(complete_diff(seed,post_row),program.delta.changes)

        # 4. Reparse the raw artifact independently and join one persisted
        # negative only on the causally changed predicate coordinates.
        post_projection = projection(post_row)
        persisted_rows=parse_csv_bytes(self.raw[0][program.artifact],header)
        persisted_matches=[row for row in persisted_rows if row["row_id"]==program.row_id]
        self.assertEqual(len(persisted_matches),1)
        persisted_projection = projection(persisted_matches[0])
        self.assertEqual(post_projection,persisted_projection)

        # 5. Typed rejection occurs before typed-failure -> detector translation.
        failure = self.semantic_predicate(program,post_projection)
        self.assertEqual(failure,program.failure)
        if failure is None:
            raise AssertionError("E_PREMATURE_DETECTOR")
        detector = FAILURE_TO_DETECTOR[failure]
        self.assertRegex(detector,r"^E_[A-Z0-9_]+$")

        # 6. Apply the printed inverse to the independently parsed post, then
        # serialize that result.  Recovery is never copied from the seed map.
        recovered_state=program.delta.apply(post_row,inverse=True)
        inverse_diff=complete_diff(post_row,recovered_state)
        expected_inverse=tuple((field,after,before) for field,before,after in program.delta.changes)
        self.assertEqual(inverse_diff,expected_inverse)
        recovered_bytes = serialize_projection(header,recovered_state)
        recovered = independent_parse_projection(recovered_bytes,header)
        recovered_projection = projection(recovered)
        self.assertEqual(recovered_bytes,seed_bytes)
        self.assertEqual(recovered_projection,seed_projection)
        self.assertIsNone(self.semantic_predicate(program,recovered_projection))

        # 7. Receipt/case counterfactuals cannot affect the predicate decision.
        variations: list[tuple[str,str]] = [("row_id",""),("row_id","WRONG-999")]
        variations.extend(("case_kind",value) for value in ("","DIAGNOSTIC","RECEIPT","NEGATIVE"))
        for field in ("mutation_id","negative_reason","oracle","scope_ceiling","status","expected_class","expected_detector"):
            variations.extend(((field,""),(field,"WRONG"),(field,"SWAPPED")))
        for field,value in variations:
            overlay = dict(post_row); overlay[field] = value
            self.assertEqual(self.semantic_predicate(program,projection(overlay)),failure)
            counter_inverse=program.delta.apply(overlay,inverse=True)
            self.assertIsNone(self.semantic_predicate(program,projection(counter_inverse)))
            self.assertEqual(complete_diff({name:overlay[name] for name in header},{name:counter_inverse[name] for name in header}),expected_inverse)
        receipt = (seed_bytes,post_bytes,recovered_bytes,program.delta.changes,failure,detector)
        self.assertEqual(receipt[0],receipt[2])
        self.assertEqual(receipt[3],complete_diff(seed,post_row))
        self.assertEqual(tuple((field,after,before) for field,before,after in receipt[3]),complete_diff(post_row,recovered))

        # Frozen primitive counterfactuals for unparameterized SG_SCOPE.
        if program.sg_kind == "PAIR":
            self.assertEqual(SG_SCOPE({"kind":"PAIR","p":2,"q":3,"coordinates":(2,3,5,7,11,13),"proposed_conclusion":b"FINITE_PAIR_SEPARATION_ONLY"})[0],"FINITE_PAIR_SEPARATION")
        elif program.sg_kind == "PAIR_WITNESS":
            self.assertEqual(SG_SCOPE({"kind":"PAIR_WITNESS","p":2,"q":3,"coordinates":(2,3,5,7,11,13),"distinguishing_coordinate":13,"proposed_conclusion":b"r=13;B_2_NOT_ISOMORPHIC_B_3"})[0],"INVALID_WITNESS")
        elif program.sg_kind == "FINITE_REGISTRY":
            self.assertEqual(SG_SCOPE({"kind":"FINITE_REGISTRY","registry":(),"proposed_conclusion":b"OPEN_NOT_AUTHORIZED"})[0],"NO_INFINITE_EVIDENCE")
        elif program.sg_kind == "OPEN_REGISTRY":
            self.assertEqual(SG_SCOPE({"kind":"OPEN_REGISTRY","registry":(2,),"typed_infinite_witness":"ABSENT_BY_SCHEMA","proposed_conclusion":b"FINITE_RANGE_ONLY"})[0],"FINITE_RANGE")

    def run_package(self, surface: MutationSurface) -> None:
        expected=independent_package_detector(surface)
        observed_variants: list[str] = []
        for variant in range(1,surface.variants+1):
            create_request = self.client.next_request()
            descriptor_value = {"after":variant_value(surface.after,variant,surface.variants),"before":variant_value(surface.before,variant,surface.variants),"coordinate":variant_value(surface.coordinate,variant,surface.variants),"kind":surface.kind,"method":surface.method,"mutation":surface.mutation,"target":surface.target,"trigger":surface.trigger,"variant":variant,"variants":surface.variants}
            descriptor = (json.dumps(descriptor_value,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode("utf-8").hex()
            created = self.client.request_reply(f"SESSION_CREATE request={create_request} method={surface.method} trigger={surface.trigger} mutation={descriptor} active_cap={self.client.active_cap}","SESSION_CREATED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*")))
            self.assertEqual(created["request"],str(create_request))
            session = created["session"]
            lock_request = self.client.next_request()
            self.client.framed_send(f"LOCK_ACQUIRE request={lock_request} session={session} active_cap={self.client.active_cap}")
            lock_record = self.client.framed_receive()
            lock_match = re.fullmatch(rf"LOCK_ACQUIRED request={lock_request} session={session} lock=([1-9][0-9]*) state=OWNED",lock_record)
            rejected_match = re.fullmatch(rf"LOCK_REJECTED request={lock_request} session={session} status=74 outcome=(UNSET|FOREIGN_RETAINED)",lock_record)
            self.assertIsNone(rejected_match)
            self.assertIsNotNone(lock_match)
            lock = lock_match.group(1) if lock_match else "0"
            purpose = f"MUTATION_{surface.mutation}_V{variant}"
            root_request = self.client.next_request()
            root = self.client.request_reply(f"ROOT_CREATE request={root_request} session={session} purpose={purpose} active_cap={self.client.active_cap}","ROOT_CREATED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*")))
            self.assertEqual((root["request"],root["session"]),(str(root_request),session))
            handle = root["handle"]

            baseline_status,baseline_out,baseline_err = self.client.spawn(session,"GENERATE_MUTATION",surface.method,purpose,handle)
            self.assertEqual((baseline_status,baseline_out,baseline_err),(0,b"",b""))
            validate_request = self.client.next_request()
            validated = self.client.request_reply(f"ROOT_VALIDATE request={validate_request} session={session} handle={handle} active_cap={self.client.active_cap}","ROOT_VALIDATED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*")))
            self.assertEqual(validated,{"request":str(validate_request),"session":session,"handle":handle})
            pass_status,pass_out,pass_err = self.client.spawn(session,"VERIFY_ONLY_GENERATOR",surface.method,"NONE",handle)
            self.assertEqual((pass_status,pass_out,pass_err),(0,b"",b""))

            inject_request = self.client.next_request()
            injected = self.client.request_reply(f"INJECT_EXCHANGE request={inject_request} session={session} handle={handle} trigger={surface.trigger} active_cap={self.client.active_cap}","INJECTED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("outcome",OUTCOME_RE)))
            self.assertEqual((injected["request"],injected["session"],injected["handle"]),(str(inject_request),session,handle))
            if surface.trigger in ("P15R_TEST_REPLACE_CANONICAL_ROOT","P15R_TEST_REPLACE_MUTATION_ROOT","P15R_TEST_REPLACE_P25_ROOT"):
                actor_status,actor_stdout,actor_stderr = self.client.spawn(session,"REPLACEMENT_ACTOR",surface.method,"NONE",handle,surface.trigger)
                self.assertEqual((actor_status,actor_stdout,actor_stderr),(0,b"",b""))
            status,mutated_stdout,stderr = self.client.spawn(session,surface.target,surface.method,"NONE",handle,surface.trigger)
            self.assertEqual(status,1); self.assertEqual(mutated_stdout,b"")
            self.assertEqual(stderr,(expected+"\n").encode("ascii"))
            actual=stderr[:-1].decode("ascii")
            self.assertEqual(actual,expected)

            clean_request = self.client.next_request()
            cleaned = self.client.request_reply(f"CLEAN request={clean_request} session={session} handle={handle} active_cap={self.client.active_cap}","CLEANED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("detector",r"E_[A-Z0-9_]+")))
            cleanup_detector="E_CLEANUP" if surface.trigger in ("P15R_TEST_REPLACE_CANONICAL_ROOT","P15R_TEST_REPLACE_MUTATION_ROOT","P15R_TEST_REPLACE_P25_ROOT") else expected
            self.assertEqual((cleaned["request"],cleaned["session"],cleaned["handle"],cleaned["detector"]),(str(clean_request),session,handle,cleanup_detector))
            audit_request = self.client.next_request()
            audited = self.client.request_reply(f"FOREIGN_AUDIT request={audit_request} session={session} handle={handle} active_cap={self.client.active_cap}","FOREIGN_AUDITED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("outcome",OUTCOME_RE)))
            self.assertEqual((audited["request"],audited["session"],audited["handle"]),(str(audit_request),session,handle))
            if lock != "0":
                release_request = self.client.next_request()
                released = self.client.request_reply(f"LOCK_RELEASE request={release_request} session={session} lock={lock} active_cap={self.client.active_cap}","LOCK_RELEASED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("lock",r"[1-9][0-9]*"),("outcome",OUTCOME_RE)))
                self.assertEqual((released["request"],released["session"],released["lock"]),(str(release_request),session,lock))
            close_request = self.client.next_request()
            closed = self.client.request_reply(f"SESSION_CLOSE request={close_request} session={session} active_cap={self.client.active_cap}","SESSION_CLOSED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("terminal_cap",r"[0-9a-f]{64}")))
            self.assertEqual((closed["request"],closed["session"]),(str(close_request),session))
            observed_variants.append(actual)
        self.assertEqual(observed_variants,[expected]*surface.variants)

    def run_empty_p25_replacement(self) -> None:
        """First P25 serial subfixture: an empty owned root is displaced and cleaned."""
        surface=MutationSurface("test_package_p25_nonempty_generation_root","P25","NONEMPTY","generation_root/occupied","ABSENT","REGULAR_EMPTY",target="GENERATE_MUTATION",trigger="P15R_TEST_REPLACE_MUTATION_ROOT")
        descriptor_value={"after":surface.after,"before":surface.before,"coordinate":surface.coordinate,"kind":surface.kind,"method":surface.method,"mutation":surface.mutation,"target":surface.target,"trigger":surface.trigger,"variant":1,"variants":1}
        descriptor=(json.dumps(descriptor_value,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode("utf-8").hex()
        request=self.client.next_request(); created=self.client.request_reply(f"SESSION_CREATE request={request} method={surface.method} trigger={surface.trigger} mutation={descriptor} active_cap={self.client.active_cap}","SESSION_CREATED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*")))
        session=created["session"]
        request=self.client.next_request(); self.client.framed_send(f"LOCK_ACQUIRE request={request} session={session} active_cap={self.client.active_cap}")
        locked=parse_fields(self.client.framed_receive(),"LOCK_ACQUIRED",(("request",str(request)),("session",session),("lock",r"[1-9][0-9]*"),("state",r"OWNED")))
        request=self.client.next_request(); root=self.client.request_reply(f"ROOT_CREATE request={request} session={session} purpose=MUTATION_P25_V1 active_cap={self.client.active_cap}","ROOT_CREATED",(("request",str(request)),("session",session),("handle",r"[1-9][0-9]*"))); handle=root["handle"]
        request=self.client.next_request(); self.client.request_reply(f"ROOT_VALIDATE request={request} session={session} handle={handle} active_cap={self.client.active_cap}","ROOT_VALIDATED",(("request",str(request)),("session",session),("handle",handle)))
        request=self.client.next_request(); self.client.request_reply(f"INJECT_EXCHANGE request={request} session={session} handle={handle} trigger={surface.trigger} active_cap={self.client.active_cap}","INJECTED",(("request",str(request)),("session",session),("handle",handle),("outcome",r"UNSET")))
        status,_stdout,stderr=self.client.spawn(session,"REPLACEMENT_ACTOR",surface.method,"NONE",handle,surface.trigger); self.assertEqual((status,stderr),(0,b""))
        request=self.client.next_request(); cleaned=self.client.request_reply(f"CLEAN request={request} session={session} handle={handle} active_cap={self.client.active_cap}","CLEANED",(("request",str(request)),("session",session),("handle",handle),("outcome",OUTCOME_RE),("detector",r"E_CLEANUP"))); self.assertEqual(cleaned["detector"],"E_CLEANUP")
        request=self.client.next_request(); audit=self.client.request_reply(f"FOREIGN_AUDIT request={request} session={session} handle={handle} active_cap={self.client.active_cap}","FOREIGN_AUDITED",(("request",str(request)),("session",session),("handle",handle),("outcome",r"FOREIGN_RETAINED"))); self.assertEqual(audit["outcome"],"FOREIGN_RETAINED")
        request=self.client.next_request(); self.client.request_reply(f"LOCK_RELEASE request={request} session={session} lock={locked['lock']} active_cap={self.client.active_cap}","LOCK_RELEASED",(("request",str(request)),("session",session),("lock",locked["lock"]),("outcome",r"ABSENT")))
        request=self.client.next_request(); self.client.request_reply(f"SESSION_CLOSE request={request} session={session} active_cap={self.client.active_cap}","SESSION_CLOSED",(("request",str(request)),("session",session),("outcome",r"FOREIGN_RETAINED"),("terminal_cap",r"[0-9a-f]{64}")))

    def run_canonical_replacement(self) -> None:
        method="test_rep_009"; trigger="P15R_TEST_REPLACE_CANONICAL_ROOT"
        request=self.client.next_request(); created=self.client.request_reply(f"SESSION_CREATE request={request} method={method} trigger={trigger} active_cap={self.client.active_cap}","SESSION_CREATED",(("request",str(request)),("session",r"[1-9][0-9]*"))); session=created["session"]
        request=self.client.next_request(); self.client.framed_send(f"LOCK_ACQUIRE request={request} session={session} active_cap={self.client.active_cap}"); locked=parse_fields(self.client.framed_receive(),"LOCK_ACQUIRED",(("request",str(request)),("session",session),("lock",r"[1-9][0-9]*"),("state",r"OWNED")))
        request=self.client.next_request(); root=self.client.request_reply(f"ROOT_CREATE request={request} session={session} purpose=CANONICAL_A active_cap={self.client.active_cap}","ROOT_CREATED",(("request",str(request)),("session",session),("handle",r"[1-9][0-9]*"))); handle=root["handle"]
        status,_stdout,stderr=self.client.spawn(session,"GENERATE_CANONICAL_A",method,"CANONICAL_A",handle); self.assertEqual((status,stderr),(0,b""))
        request=self.client.next_request(); self.client.request_reply(f"ROOT_VALIDATE request={request} session={session} handle={handle} active_cap={self.client.active_cap}","ROOT_VALIDATED",(("request",str(request)),("session",session),("handle",handle)))
        request=self.client.next_request(); self.client.request_reply(f"INJECT_EXCHANGE request={request} session={session} handle={handle} trigger={trigger} active_cap={self.client.active_cap}","INJECTED",(("request",str(request)),("session",session),("handle",handle),("outcome",r"UNSET")))
        status,_stdout,stderr=self.client.spawn(session,"REPLACEMENT_ACTOR",method,"NONE",handle,trigger); self.assertEqual((status,stderr),(0,b""))
        request=self.client.next_request(); cleaned=self.client.request_reply(f"CLEAN request={request} session={session} handle={handle} active_cap={self.client.active_cap}","CLEANED",(("request",str(request)),("session",session),("handle",handle),("outcome",r"DISPLACED_CLEANED"),("detector",r"E_CLEANUP"))); self.assertEqual(cleaned["detector"],"E_CLEANUP")
        request=self.client.next_request(); audit=self.client.request_reply(f"FOREIGN_AUDIT request={request} session={session} handle={handle} active_cap={self.client.active_cap}","FOREIGN_AUDITED",(("request",str(request)),("session",session),("handle",handle),("outcome",r"FOREIGN_RETAINED"))); self.assertEqual(audit["outcome"],"FOREIGN_RETAINED")
        request=self.client.next_request(); self.client.request_reply(f"LOCK_RELEASE request={request} session={session} lock={locked['lock']} active_cap={self.client.active_cap}","LOCK_RELEASED",(("request",str(request)),("session",session),("lock",locked["lock"]),("outcome",r"ABSENT")))
        request=self.client.next_request(); self.client.request_reply(f"SESSION_CLOSE request={request} session={session} active_cap={self.client.active_cap}","SESSION_CLOSED",(("request",str(request)),("session",session),("outcome",r"FOREIGN_RETAINED"),("terminal_cap",r"[0-9a-f]{64}")))

    def run_signal_boundary(self) -> None:
        method="test_rep_009"; trigger="P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN"
        request=self.client.next_request(); created=self.client.request_reply(f"SESSION_CREATE request={request} method={method} trigger={trigger} active_cap={self.client.active_cap}","SESSION_CREATED",(("request",str(request)),("session",r"[1-9][0-9]*"))); session=created["session"]
        request=self.client.next_request(); locked=self.client.request_reply(f"LOCK_ACQUIRE request={request} session={session} active_cap={self.client.active_cap}","LOCK_ACQUIRED",(("request",str(request)),("session",session),("lock",r"[1-9][0-9]*"),("state",r"OWNED")))
        request=self.client.next_request(); root=self.client.request_reply(f"ROOT_CREATE request={request} session={session} purpose=NONE active_cap={self.client.active_cap}","ROOT_CREATED",(("request",str(request)),("session",session),("handle",r"[1-9][0-9]*"))); handle=root["handle"]
        status,stdout,stderr=self.client.spawn(session,"COPIED_REPRODUCE",method,"NONE",handle,trigger)
        self.assertEqual((status,stdout,stderr),(1,b"",b"E_SIGNAL_ACQUIRE\n"))
        request=self.client.next_request(); cleaned=self.client.request_reply(f"CLEAN request={request} session={session} handle={handle} active_cap={self.client.active_cap}","CLEANED",(("request",str(request)),("session",session),("handle",handle),("outcome",r"ABSENT"),("detector",r"E_SIGNAL_ACQUIRE")))
        request=self.client.next_request(); audited=self.client.request_reply(f"FOREIGN_AUDIT request={request} session={session} handle={handle} active_cap={self.client.active_cap}","FOREIGN_AUDITED",(("request",str(request)),("session",session),("handle",handle),("outcome",r"ABSENT")))
        request=self.client.next_request(); self.client.request_reply(f"LOCK_RELEASE request={request} session={session} lock={locked['lock']} active_cap={self.client.active_cap}","LOCK_RELEASED",(("request",str(request)),("session",session),("lock",locked["lock"]),("outcome",r"ABSENT")))
        request=self.client.next_request(); self.client.request_reply(f"SESSION_CLOSE request={request} session={session} active_cap={self.client.active_cap}","SESSION_CLOSED",(("request",str(request)),("session",session),("outcome",r"ABSENT"),("terminal_cap",r"[0-9a-f]{64}")))

    def run_lock_replacement(self, trigger: str) -> None:
        method="test_rep_009"
        request=self.client.next_request(); created=self.client.request_reply(f"SESSION_CREATE request={request} method={method} trigger={trigger} active_cap={self.client.active_cap}","SESSION_CREATED",(("request",str(request)),("session",r"[1-9][0-9]*"))); session=created["session"]
        if trigger=="P15R_TEST_REPLACE_LOCK_ACQUIRING":
            request=self.client.next_request(); self.client.request_reply(f"INJECT_EXCHANGE request={request} session={session} handle=0 trigger={trigger} active_cap={self.client.active_cap}","INJECTED",(("request",str(request)),("session",session),("handle",r"0"),("outcome",r"UNSET")))
            status,_stdout,stderr=self.client.spawn(session,"REPLACEMENT_ACTOR",method,"NONE","0",trigger); self.assertEqual((status,stderr),(0,b""))
        request=self.client.next_request(); self.client.framed_send(f"LOCK_ACQUIRE request={request} session={session} active_cap={self.client.active_cap}"); locked=parse_fields(self.client.framed_receive(),"LOCK_ACQUIRED",(("request",str(request)),("session",session),("lock",r"[1-9][0-9]*"),("state",r"OWNED")))
        if trigger=="P15R_TEST_REPLACE_LOCK_CLEANING":
            request=self.client.next_request(); self.client.request_reply(f"INJECT_EXCHANGE request={request} session={session} handle=0 trigger={trigger} active_cap={self.client.active_cap}","INJECTED",(("request",str(request)),("session",session),("handle",r"0"),("outcome",r"UNSET")))
            status,_stdout,stderr=self.client.spawn(session,"REPLACEMENT_ACTOR",method,"NONE","0",trigger); self.assertEqual((status,stderr),(0,b""))
        request=self.client.next_request(); released=self.client.request_reply(f"LOCK_RELEASE request={request} session={session} lock={locked['lock']} active_cap={self.client.active_cap}","LOCK_RELEASED",(("request",str(request)),("session",session),("lock",locked["lock"]),("outcome",r"DISPLACED_CLEANED"))); self.assertEqual(released["outcome"],"DISPLACED_CLEANED")
        request=self.client.next_request(); audit=self.client.request_reply(f"FOREIGN_AUDIT request={request} session={session} handle=0 active_cap={self.client.active_cap}","FOREIGN_AUDITED",(("request",str(request)),("session",session),("handle",r"0"),("outcome",r"FOREIGN_RETAINED"))); self.assertEqual(audit["outcome"],"FOREIGN_RETAINED")
        request=self.client.next_request(); self.client.request_reply(f"SESSION_CLOSE request={request} session={session} active_cap={self.client.active_cap}","SESSION_CLOSED",(("request",str(request)),("session",session),("outcome",r"FOREIGN_RETAINED"),("terminal_cap",r"[0-9a-f]{64}")))

    def actual_receipt(self) -> tuple[tuple[object,...],...]:
        method = "test_rep_010"
        request = self.client.next_request()
        created = self.client.request_reply(f"SESSION_CREATE request={request} method={method} trigger=NONE active_cap={self.client.active_cap}","SESSION_CREATED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*")))
        session = created["session"]
        status,stdout,stderr = self.client.spawn(session,"COPIED_REPRODUCE",method,"NONE","0")
        self.assertEqual((status,stderr),(0,b""))
        value = json.loads(stdout.decode("utf-8"))
        self.assertIsInstance(value,dict)
        self.assertEqual(set(value),{"before","after"})
        before = validate_actual_receipt(value["before"])
        after = validate_actual_receipt(value["after"])
        self.assertEqual(before,after)
        close_request = self.client.next_request()
        self.client.request_reply(f"SESSION_CLOSE request={close_request} session={session} active_cap={self.client.active_cap}","SESSION_CLOSED",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("terminal_cap",r"[0-9a-f]{64}")))
        return before

    def test_val_001(self): self.family_check("val",1)
    def test_val_002(self): self.family_check("val",2)
    def test_val_003(self): self.assertEqual({row["branch"] for row in self.rows(CSV_NAMES[0])[:12]},{"ODD_OFF_LOCAL","TWO_OFF_LOCAL","DIAGONAL"})
    def test_val_004(self): self.assertTrue(all(not row["expression"] or fresh_factorization(int(row["expression"])) == row["factorization"] for row in self.rows(CSV_NAMES[0])[:12]))
    def test_val_005(self): self.assertTrue(all(not row["raw_valuation"] or fresh_valuation(int(row["expression"]),int(row["r"])) == int(row["raw_valuation"]) for row in self.rows(CSV_NAMES[0])[:12]))
    def test_val_006(self): self.assertTrue(all((row["branch"]=="DIAGONAL" and row["kappa"]=="0") or row["branch"]!="DIAGONAL" for row in self.rows(CSV_NAMES[0])[:12]))
    def test_val_007(self): self.assertEqual([row["principal_sign"] for row in self.rows(CSV_NAMES[0])[6:10]],["-1","1","-1","1"])
    def test_val_008(self): self.assertEqual(sorted({int(row["kappa"]) for row in self.rows(CSV_NAMES[0])[:12]}),[0,1,2])
    def test_val_009(self): self.assertEqual([row["row_id"] for row in self.rows(CSV_NAMES[0]) if row["branch"]=="DIAGONAL"],["VC-011","VC-012"])
    def test_val_010(self): self.family_check("val",10)

    def test_ord_001(self): self.family_check("ord",1)
    def test_ord_002(self): self.family_check("ord",2)
    def test_ord_003(self): self.assertEqual(self.row(CSV_NAMES[1],"EO-001")["claim_under_test"],"LOCAL_ODD_COMPONENT_NONZERO")
    def test_ord_004(self): self.assertTrue(all(fresh_order(int(row["p"]),int(row["ell"])) == int(row["order_mod_ell"]) for row in self.rows(CSV_NAMES[1]) if row["order_mod_ell"]))
    def test_ord_005(self): self.assertEqual([row["m"] for row in self.rows(CSV_NAMES[1])[5:9]],["1","2","1","2"])
    def test_ord_006(self): self.assertEqual([row["m"] for row in self.rows(CSV_NAMES[1])[9:12]],["1","2","3"])
    def test_ord_007(self): self.assertEqual(self.row(CSV_NAMES[1],"EO-013")["order_mod_ell"],"8")
    def test_ord_008(self): self.assertEqual(self.row(CSV_NAMES[1],"EO-002")["finite_group_model"],"u=-3;u_mod8=5")
    def test_ord_009(self): self.family_check("ord",9)
    def test_ord_010(self): self.family_check("ord",10)

    def test_ker_001(self): self.family_check("ker",1)
    def test_ker_002(self): self.family_check("ker",2)
    def test_ker_003(self): self.assertEqual([row["model_kind"] for row in self.rows(CSV_NAMES[2])[:4]],["HOMOGENEOUS_BLOCK","HOMOGENEOUS_BLOCK","EXCEPTIONAL_MIXED_BLOCK","EXCEPTIONAL_MIXED_BLOCK"])
    def test_ker_004(self): self.assertEqual(sum(row["model_kind"]=="PHI_TRUNCATION" for row in self.rows(CSV_NAMES[2])),6)
    def test_ker_005(self): self.assertEqual([row["kernel_order"] for row in self.rows(CSV_NAMES[2])[:4]],["4","81","16","81"])
    def test_ker_006(self):
        for row in self.rows(CSV_NAMES[2])[:10]: self.assertEqual(len(enumerate_kernel(int(row["r"]),int(row["target_exponent"]),parse_vector(row["source_exponents"]),parse_vector(row["image_numerators"]))),int(row["kernel_order"]))
    def test_ker_007(self):
        for row in self.rows(CSV_NAMES[2])[:10]:
            r=int(row["r"]); exponents=parse_vector(row["source_exponents"]); kernel=enumerate_kernel(r,int(row["target_exponent"]),exponents,parse_vector(row["image_numerators"])); moduli=tuple(r**value for value in exponents)
            self.assertEqual(tuple(len(multiply_elements(kernel,r**depth,moduli)) for depth in range(int(row["target_exponent"])+1)),parse_vector(row["height_orders_d0_to_N"]))
    def test_ker_008(self): self.assertEqual([row["tail_order"] for row in self.rows(CSV_NAMES[2])[4:10]],["1","2","4","1","3","9"])
    def test_ker_009(self): self.assertTrue(all(predicate_fk_root(row) is None for row in self.rows(CSV_NAMES[2])[10:14]))
    def test_ker_010(self): self.assertTrue(all(predicate_fk_root(row)=="FK_ROOT_INVALID" for row in self.rows(CSV_NAMES[2])[14:18]))
    def test_ker_011(self): self.family_check("ker",11)
    def test_ker_012(self): self.family_check("ker",12)
    def test_ker_013(self): self.family_check("ker",13)
    def test_ker_014(self): self.family_check("ker",14)

    def test_tor_001(self): self.family_check("tor",1)
    def test_tor_002(self): self.family_check("tor",2)
    def test_tor_003(self): self.assertEqual([row["compact_quotient_order"] for row in self.rows(CSV_NAMES[3])[:6]],["1","2","4","1","3","9"])
    def test_tor_004(self): self.assertIn("closure(Tor(COMPACT_B))",self.row(CSV_NAMES[3],"TC-007")["operation"])
    def test_tor_005(self): self.assertEqual(self.row(CSV_NAMES[3],"TC-007")["source_owner"],"DISCRETE_K")
    def test_tor_006(self): self.assertEqual(self.row(CSV_NAMES[3],"TC-007")["target_owner"],"COMPACT_B")
    def test_tor_007(self): self.assertTrue(all("NOT_COMPACT_INFINITE_THEOREM" in row["statement_scope"] for row in self.rows(CSV_NAMES[3])[:6]))
    def test_tor_008(self): self.assertEqual(self.row(CSV_NAMES[3],"TC-007")["statement_scope"],"SYMBOLIC_IDENTITY_BOUND_TO_PROOF_NOT_PROVED_BY_MODEL")
    def test_tor_009(self): self.family_check("tor",10)

    def test_sig_001(self): self.family_check("sig",1)
    def test_sig_002(self): self.family_check("sig",2)
    def test_sig_003(self): self.assertEqual(parse_vector(self.row(CSV_NAMES[4],"SG-001")["prime_prefix"]),(2,3,5,7,11,13))
    def test_sig_004(self):
        for row in self.rows(CSV_NAMES[4])[:6]: self.assertEqual(parse_vector(row["kappa_prefix_p"]),tuple(primitive_kappa(int(row["p"]),r) for r in (2,3,5,7,11,13)))
    def test_sig_005(self): self.assertEqual(self.row(CSV_NAMES[4],"SG-007")["distinguishing_prime"],"11")
    def test_sig_006(self): self.assertEqual(self.row(CSV_NAMES[4],"SG-008")["authorized_conclusion"],"NO_GLOBAL_CONCLUSION")
    def test_sig_007(self): self.assertEqual(sum(row["case_kind"]=="NEGATIVE" for row in self.rows(CSV_NAMES[4])),4)
    def test_sig_008(self): self.assertEqual(self.row(CSV_NAMES[4],"SG-012")["prime_prefix"],"")
    def test_sig_009(self): self.assertTrue(all(row["scope_ceiling"]=="FINITE_PREFIX_ONLY_GLOBAL_SIGNATURE_MAP_OPEN" for row in self.rows(CSV_NAMES[4])))
    def test_sig_010(self): self.family_check("sig",10)

    def test_own_001(self): self.family_check("own",1)
    def test_own_002(self): self.family_check("own",2)
    def test_own_003(self): self.assertEqual([row["determinant_mod_r"] for row in self.rows(CSV_NAMES[5])[:2]],["4","2"])
    def test_own_004(self):
        for row in self.rows(CSV_NAMES[5])[:2]:
            r,exponent=int(row["r"]),int(row["exponent"]); modulus=r**exponent
            self.assertIn((r,exponent,modulus),((5,2,25),(3,2,9)))
            self.assertEqual(row["automorphism_matrix"],"[0;1]/[1;0]")
            a,b,c,d=parse_matrix_2x2(row["automorphism_matrix"])
            self.assertEqual(row["block_type"],f"C_{modulus}+C_{modulus}")
            determinant=(a*d-b*c)%r
            self.assertEqual(determinant,int(row["determinant_mod_r"])); self.assertNotEqual(determinant,0)
            elements=tuple(itertools.product(range(modulus),repeat=2))
            def action(element: tuple[int,int]) -> tuple[int,int]:
                x,y=element
                image=((a*x+b*y)%modulus,(c*x+d*y)%modulus)
                self.assertTrue(all(0<=coordinate<modulus for coordinate in image))
                return image
            images={action(element) for element in elements}
            self.assertEqual(len(images),modulus*modulus); self.assertEqual(action((0,0)),(0,0))
            for left in elements:
                for right in elements:
                    total=((left[0]+right[0])%modulus,(left[1]+right[1])%modulus)
                    left_image,right_image=action(left),action(right)
                    self.assertEqual(action(total),((left_image[0]+right_image[0])%modulus,(left_image[1]+right_image[1])%modulus))
            e1,e2=(1,0),(0,1)
            self.assertEqual((action(e1),action(e2)),(e2,e1))
            label_a,label_b=int(row["label_a"]),int(row["label_b"])
            self.assertNotEqual(label_a,label_b)
            labels={e1:label_a,e2:label_b}
            self.assertEqual((labels[action(e1)],labels[action(e2)]),(label_b,label_a))
            derived_bare_type_preserved=len(images)==modulus*modulus and determinant!=0 and action(e1)==e2 and action(e2)==e1
            self.assertEqual(row["bare_type_preserved"],"true" if derived_bare_type_preserved else "false")
    def test_own_005(self): self.assertTrue(all(row["bare_type_preserved"]=="true" for row in self.rows(CSV_NAMES[5])[:2]))
    def test_own_006(self): self.assertEqual(sum(row["row_kind"]=="OWNER_RECORD" for row in self.rows(CSV_NAMES[5])),4)
    def test_own_007(self): self.assertEqual(self.row(CSV_NAMES[5],"OF-003")["source_owner"],"MARKED_EXACT_SEQUENCE")
    def test_own_008(self): self.assertEqual(self.row(CSV_NAMES[5],"OF-004")["source_owner"],"BARE_COMPACT_QUOTIENT")
    def test_own_009(self): self.assertEqual(self.row(CSV_NAMES[5],"OF-005")["source_owner"],"AMBIENT_U_P")
    def test_own_010(self): self.assertEqual(self.row(CSV_NAMES[5],"OF-006")["source_owner"],"ACTUAL_PACKET_Q_P")
    def test_own_011(self): self.assertEqual(len({predicate_owner(row) for row in self.rows(CSV_NAMES[5])[6:]}),9)
    def test_own_012(self): self.family_check("own",12)

    def test_ceil_001(self): self.family_check("ceil",1)
    def test_ceil_002(self): self.family_check("ceil",2)
    def test_ceil_003(self): self.assertEqual([(row["binding_path"],row["binding_sha256"]) for row in self.rows(CSV_NAMES[6])[:14]],list(AUTHORITY_BINDINGS))
    def test_ceil_004(self):
        repository_fd=os.open("../..",os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW|os.O_CLOEXEC)
        try:
            for relative,digest in AUTHORITY_BINDINGS:
                parts=relative.split("/"); parent=os.dup(repository_fd)
                try:
                    for part in parts[:-1]:
                        following=os.open(part,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW|os.O_CLOEXEC,dir_fd=parent); os.close(parent); parent=following
                    fd=os.open(parts[-1],os.O_RDONLY|os.O_NOFOLLOW|os.O_CLOEXEC,dir_fd=parent)
                    try:
                        chunks=[]
                        while True:
                            chunk=os.read(fd,65536)
                            if not chunk: break
                            chunks.append(chunk)
                        self.assertEqual(sha256(b"".join(chunks)),digest)
                    finally: os.close(fd)
                finally: os.close(parent)
        finally: os.close(repository_fd)
    def test_ceil_005(self): self.assertEqual([row["allowed_state"] for row in self.rows(CSV_NAMES[6])[14:17]],["DIAGNOSTIC_ONLY","BYTE_BINDING_ONLY","OPEN_NOT_AUTHORIZED"])
    def test_ceil_006(self): self.assertEqual(len({predicate_pc(row) for row in self.rows(CSV_NAMES[6])[17:]}),9)
    def test_ceil_007(self): self.assertFalse(any(row["allowed_state"]=="KNOWN_INJECTIVE" for row in self.rows(CSV_NAMES[6])))
    def test_ceil_008(self): self.assertEqual(DAG_NODES,("A","D","R","G","I","C","M","V"))
    def test_ceil_009(self): self.assertEqual(len(set(DAG_EDGES)),12)
    def test_ceil_010(self): self.assertNotIn(("M","M"),DAG_EDGES)
    def test_ceil_011(self): self.assertNotIn(("V","M"),DAG_EDGES)
    def test_ceil_012(self): self.family_check("ceil",12)

    def test_sum_001(self): self.family_check("sum",1)
    def test_sum_002(self): self.assertEqual([row["artifact"] for row in self.rows(CSV_NAMES[7])[:8]],list(CSV_NAMES))
    def test_sum_003(self): self.assertEqual(self.row(CSV_NAMES[7],"TS-009")["expected_rows"],"120")
    def test_sum_004(self): self.assertEqual(sum(int(row["expected_negative_rows"]) for row in self.rows(CSV_NAMES[7])[:8]),35)
    def test_sum_005(self): self.assertTrue(all("sha" not in field.lower() for field in HEADERS[7]))

    def test_pkg_001(self):
        identities=[(os.fstat(fd).st_dev,os.fstat(fd).st_ino) for fd in self.root_fds]; self.assertEqual(len(set(identities)),3)
    def test_pkg_002(self): self.assertEqual(tuple(self.raw[0]),CSV_NAMES)
    def test_pkg_003(self): self.assertEqual([len(self.rows(name)) for name in CSV_NAMES],list(ROW_COUNTS))
    def test_pkg_004(self): self.assertEqual([len(self.rows(name)[0]) for name in CSV_NAMES],list(WIDTHS))
    def test_pkg_005(self): self.assertEqual(sum(NEGATIVE_COUNTS),35)
    def test_pkg_006(self): self.assertTrue(all(data.endswith(b"\n") and not data.endswith(b"\n\n") for data in self.raw[0].values()))
    def test_pkg_007(self): self.assertTrue(all(not data.startswith(b"\xef\xbb\xbf") and b"\r" not in data for data in self.raw[0].values()))
    def test_pkg_008(self): self.assertEqual(self.manifests[0]["schema_version"],MANIFEST_SCHEMA)
    def test_pkg_009(self): self.assertEqual(len(self.manifests[0]["authority_bindings"]),14)
    def test_pkg_010(self): self.assertEqual([item["path"] for item in self.manifests[0]["implementation"]],list(IMPLEMENTATION_PATHS))
    def test_pkg_011(self): self.assertEqual([item["path"] for item in self.manifests[0]["artifacts"]],["results/"+name for name in CSV_NAMES])
    def test_pkg_012(self): self.assertNotIn("self_sha256",self.manifests[0])
    def test_pkg_013(self): self.assertNotIn("result_review",self.manifests[0])
    def test_pkg_014(self): self.assertEqual(self.manifests[0]["aggregates"]["CSV_BODY_ROWS"],120)
    def test_pkg_015(self): self.assertEqual(self.manifests[0]["proof_ceiling"]["universal_recover_p"],"OPEN_NOT_AUTHORIZED")
    def test_pkg_016(self): self.assertFalse(self.manifests[0]["proof_ceiling"]["route_b_authorized"])
    def test_pkg_017(self): self.assertEqual(independent_manifest_graph(self.manifests[0],self.raw[0]),(DAG_NODES,DAG_EDGES))
    def test_pkg_018(self):
        source_names=tuple(name for name,value in ControlsOracle.__dict__.items() if name.startswith("test_") and callable(value))
        self.assertEqual(source_names,EXACT_TEST_NAMES); self.assertEqual((len(EXACT_TEST_NAMES),len(set(EXACT_TEST_NAMES))),(173,173))
        names=unittest.TestLoader().getTestCaseNames(type(self)); self.assertEqual(tuple(names),tuple(sorted(EXACT_TEST_NAMES)))
        self.assertTrue(all(callable(ControlsOracle.__dict__.get(name)) for name in EXACT_TEST_NAMES))
        counts=(sum(name.startswith("test_val_") for name in names),sum(name.startswith("test_ord_") for name in names),sum(name.startswith("test_ker_") for name in names),sum(name.startswith("test_tor_") for name in names),sum(name.startswith("test_sig_") for name in names),sum(name.startswith("test_own_") for name in names),sum(name.startswith("test_ceil_") for name in names),sum(name.startswith("test_sum_") for name in names),sum(name.startswith("test_pkg_") for name in names),sum(name.startswith("test_rep_") for name in names),sum(name.startswith("test_semantic_") for name in names),sum(name.startswith("test_package_") for name in names))
        self.assertEqual(counts,(10,10,14,9,10,12,12,5,18,10,35,28))

    def test_rep_001(self):
        self.assertEqual(set(os.listdir(self.root_fds[0])),set(GENERATED_NAMES)|{"README.md"})
        for root_fd in self.root_fds[1:]: self.assertEqual(set(os.listdir(root_fd)),set(GENERATED_NAMES))
    def test_rep_002(self): self.assertEqual(tuple(self.raw[0]),GENERATED_NAMES[:-1])
    def test_rep_003(self): self.assertTrue(all(self.raw[0][name]==self.raw[1][name] for name in CSV_NAMES))
    def test_rep_004(self): self.assertTrue(all(self.raw[1][name]==self.raw[2][name] for name in CSV_NAMES))
    def test_rep_005(self): self.assertTrue(all(self.raw[0][name]==self.raw[2][name] for name in CSV_NAMES))
    def test_rep_006(self): self.assertEqual(self.manifests[0],self.manifests[1])
    def test_rep_007(self): self.assertEqual(self.manifests[1],self.manifests[2])
    def test_rep_008(self): self.assertEqual(self.manifests[0]["reproduction"]["fresh_generations"],2)
    def test_rep_009(self):
        self.assertEqual(self.manifests[0]["reproduction"]["byte_identical_copies"],3)
        self.run_signal_boundary()
        self.run_canonical_replacement()
        self.run_lock_replacement("P15R_TEST_REPLACE_LOCK_ACQUIRING")
        self.run_lock_replacement("P15R_TEST_REPLACE_LOCK_CLEANING")
    def test_rep_010(self):
        Q=self.actual_receipt(); Q_frozen=tuple(tuple(cell for cell in row) for row in Q)
        selected="papers/15-wieferich-ulm-packet-bases/results/valuation_normalization_controls.csv"; matches=[index for index,row in enumerate(Q) if row[0]==selected]
        self.assertEqual(len(matches),1); index=matches[0]; row=Q[index]
        coordinates=("relative_path","type","mode","size","digest","mtime_ns","ctime_ns","nlink","dev","ino")
        self.assertEqual((row[1],row[2]),("REGULAR",0o444))
        Q_mode=tuple(tuple((0o644 if row_index==index and column==2 else cell) for column,cell in enumerate(record)) for row_index,record in enumerate(Q))
        Q_mtime=tuple(tuple((int(cell)+1_000_000_000 if row_index==index and column==5 else cell) for column,cell in enumerate(record)) for row_index,record in enumerate(Q))
        self.assertIsNot(Q,Q_mode); self.assertIsNot(Q,Q_mtime); self.assertIsNot(Q_mode,Q_mtime)
        self.assertTrue(all(Q[row_index] is not Q_mode[row_index] and Q[row_index] is not Q_mtime[row_index] and Q_mode[row_index] is not Q_mtime[row_index] for row_index in range(len(Q))))
        self.assertTrue(all(isinstance(cell,(str,int)) and not isinstance(cell,(list,dict,set,bytearray)) for receipt in (Q,Q_mode,Q_mtime) for record in receipt for cell in record))
        validate_actual_receipt(Q_mode); validate_actual_receipt(Q_mtime)
        mode_differences=tuple_differences(Q,Q_mode,coordinates)
        mtime_differences=tuple_differences(Q,Q_mtime,coordinates)
        self.assertEqual(mode_differences,{(selected,"mode",0o444,0o644)})
        self.assertEqual(mtime_differences,{(selected,"mtime_ns",row[5],int(row[5])+1_000_000_000)})
        self.assertEqual(Q[index][6],Q_mode[index][6]); self.assertEqual(Q[index][6],Q_mtime[index][6])
        self.assertEqual(receipt_compare(Q,Q_mode),"E_VERIFY_ONLY_METADATA"); self.assertEqual(receipt_compare(Q,Q_mtime),"E_VERIFY_ONLY_METADATA")
        self.assertEqual(Q,Q_frozen)

    def test_semantic_s01_wrong_local_coordinate(self): self.run_semantic(0)
    def test_semantic_s02_wrong_odd_minus_one(self): self.run_semantic(1)
    def test_semantic_s03_wrong_two_minus_three(self): self.run_semantic(2)
    def test_semantic_s04_erased_local_two_sign(self): self.run_semantic(3)
    def test_semantic_s05_diagonal_bounded_surjectivity(self): self.run_semantic(4)
    def test_semantic_s06_mere_divisibility_as_exact(self): self.run_semantic(5)
    def test_semantic_s07_ambient_root_r2_k1(self): self.run_semantic(6)
    def test_semantic_s08_ambient_root_r2_k2(self): self.run_semantic(7)
    def test_semantic_s09_ambient_root_r3_k1(self): self.run_semantic(8)
    def test_semantic_s10_ambient_root_r3_k2(self): self.run_semantic(9)
    def test_semantic_s11_raw_torsion_for_closure(self): self.run_semantic(10)
    def test_semantic_s12_finite_model_promotion(self): self.run_semantic(11)
    def test_semantic_s13_discrete_compact_confusion(self): self.run_semantic(12)
    def test_semantic_s14_prefix_equality_promotion(self): self.run_semantic(13)
    def test_semantic_s15_separation_to_recovery(self): self.run_semantic(14)
    def test_semantic_s16_finite_range_injectivity(self): self.run_semantic(15)
    def test_semantic_s17_open_map_injective(self): self.run_semantic(16)
    def test_semantic_s18_marked_bare_splice(self): self.run_semantic(17)
    def test_semantic_s19_ambient_marker_import(self): self.run_semantic(18)
    def test_semantic_s20_actual_topology_import(self): self.run_semantic(19)
    def test_semantic_s21_standardized_flow_import(self): self.run_semantic(20)
    def test_semantic_s22_haar_claim(self): self.run_semantic(21)
    def test_semantic_s23_measure_claim(self): self.run_semantic(22)
    def test_semantic_s24_trace_claim(self): self.run_semantic(23)
    def test_semantic_s25_operator_claim(self): self.run_semantic(24)
    def test_semantic_s26_determinant_claim(self): self.run_semantic(25)
    def test_semantic_s27_grh_promotion(self): self.run_semantic(26)
    def test_semantic_s28_density_promotion(self): self.run_semantic(27)
    def test_semantic_s29_priority_promotion(self): self.run_semantic(28)
    def test_semantic_s30_route_b_promotion(self): self.run_semantic(29)
    def test_semantic_s31_universal_recovery(self): self.run_semantic(30)
    def test_semantic_s32_control_as_proof(self): self.run_semantic(31)
    def test_semantic_s33_receipt_as_theorem(self): self.run_semantic(32)
    def test_semantic_s34_control_as_chebotarev(self): self.run_semantic(33)
    def test_semantic_s35_control_as_ulm(self): self.run_semantic(34)

    def test_package_p01_cell_content_tamper(self): self.run_package(MutationSurface("test_package_p01_cell_content_tamper","P01","ARTIFACT","results/valuation_normalization_controls.csv:VC-001.kappa","0","1"))
    def test_package_p02_header_tamper(self): self.run_package(MutationSurface("test_package_p02_header_tamper","P02","HEADER","results/valuation_normalization_controls.csv:header[raw_valuation]","raw_valuation","raw_valuatioN"))
    def test_package_p03_stale_row_count(self): self.run_package(MutationSurface("test_package_p03_stale_row_count","P03","ROW_COUNT","results/valuation_normalization_controls.csv:row[VC-016]","PRESENT","ABSENT"))
    def test_package_p04_row_reorder(self): self.run_package(MutationSurface("test_package_p04_row_reorder","P04","ROW_ORDER","results/valuation_normalization_controls.csv:order[0:2]","VC-001,VC-002","VC-002,VC-001"))
    def test_package_p05_missing_csv(self): self.run_package(MutationSurface("test_package_p05_missing_csv","P05","MISSING_ARTIFACT","results/valuation_normalization_controls.csv","REGULAR","ABSENT"))
    def test_package_p06_extra_csv(self): self.run_package(MutationSurface("test_package_p06_extra_csv","P06","EXTRA_CSV","results/extra.csv","ABSENT","REGULAR_EMPTY"))
    def test_package_p07_missing_manifest(self): self.run_package(MutationSurface("test_package_p07_missing_manifest","P07","MISSING_MANIFEST","results/manifest.json","REGULAR","ABSENT"))
    def test_package_p08_extra_file(self): self.run_package(MutationSurface("test_package_p08_extra_file","P08","EXTRA_FILE","results/extra.txt","ABSENT","REGULAR_EMPTY"))
    def test_package_p09_extra_directory(self): self.run_package(MutationSurface("test_package_p09_extra_directory","P09","EXTRA_DIRECTORY","results/extra","ABSENT","DIRECTORY"))
    def test_package_p10_manifest_field_tamper(self): self.run_package(MutationSurface("test_package_p10_manifest_field_tamper","P10","MANIFEST","results/manifest.json:status","PASS","FAIL"))
    def test_package_p11_manifest_self_hash(self): self.run_package(MutationSurface("test_package_p11_manifest_self_hash","P11","SELF_CYCLE","results/manifest.json:self_sha256","ABSENT","0000000000000000000000000000000000000000000000000000000000000000"))
    def test_package_p12_authority_binding_drift(self): self.run_package(MutationSurface("test_package_p12_authority_binding_drift","P12","AUTHORITY","results/manifest.json:authority_bindings[0].sha256","2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8","0d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8"))
    def test_package_p13_design_lock_drift(self): self.run_package(MutationSurface("test_package_p13_design_lock_drift","P13","DESIGN","results/manifest.json:design_lock.sha256","db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d","0b590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d"))
    def test_package_p14_design_review_drift(self): self.run_package(MutationSurface("test_package_p14_design_review_drift","P14","REVIEW","results/manifest.json:design_review.sha256","2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19","0bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19"))
    def test_package_p15_implementation_gate_drift(self): self.run_package(MutationSurface("test_package_p15_implementation_gate_drift","P15","GATE","results/manifest.json:implementation_gate.sha256","e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8","05834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8"))
    def test_package_p16_implementation_digest_drift(self): self.run_package(MutationSurface("test_package_p16_implementation_digest_drift","P16","IMPLEMENTATION","code/README.md:terminal_byte","EOF","58"))
    def test_package_p17_symlink_input(self): self.run_package(MutationSurface("test_package_p17_symlink_input","P17","LINK_SYMLINK","results/valuation_normalization_controls.csv:type","REGULAR","SYMLINK_TO_METHOD_COPY"))
    def test_package_p18_hardlink_input(self): self.run_package(MutationSurface("test_package_p18_hardlink_input","P18","LINK_HARDLINK","results/valuation_normalization_controls.csv:nlink","1","2"))
    def test_package_p19_pre_run_cache(self): self.run_package(MutationSurface("test_package_p19_pre_run_cache","P19","CACHE_PRE","results/__pycache__/p15r_pre_probe.pyc","ABSENT","REGULAR_EMPTY"))
    def test_package_p20_post_run_cache(self): self.run_package(MutationSurface("test_package_p20_post_run_cache","P20","CACHE_POST","fresh-a/__pycache__/p15r_post_probe.pyc","ABSENT","REGULAR_EMPTY",target="COPIED_REPRODUCE",trigger="P15R_TEST_CREATE_POST_CACHE"))
    def test_package_p21_recursive_entry(self): self.run_package(MutationSurface("test_package_p21_recursive_entry","P21","RECURSIVE_ENTRY","environment:P15R_REPRO_ACTIVE","ABSENT","1",target="COPIED_REPRODUCE"))
    def test_package_p22_concurrent_second_entry(self): self.run_package(MutationSurface("test_package_p22_concurrent_second_entry","P22","CONCURRENT_LOCK","abstract_package_lock","FREE","EADDRINUSE",target="COPIED_REPRODUCE"))
    def test_package_p23_verify_only_repair_attempt(self): self.run_package(MutationSurface("test_package_p23_verify_only_repair_attempt","P23","CLI_REPAIR","argv","--verify-only --input-dir results","--verify-only --input-dir results --repair"))
    def test_package_p24_forced_cleanup_failure(self): self.run_package(MutationSurface("test_package_p24_forced_cleanup_failure","P24","CLEANUP","environment:P15R_TEST_ABORT_AFTER_FRESH_A","ABSENT","1",target="COPIED_REPRODUCE",trigger="P15R_TEST_ABORT_AFTER_FRESH_A"))
    def test_package_p25_nonempty_generation_root(self):
        self.run_empty_p25_replacement()
        self.run_package(MutationSurface("test_package_p25_nonempty_generation_root","P25","NONEMPTY","generation_root/occupied","ABSENT","REGULAR_EMPTY",target="GENERATE_MUTATION",trigger="P15R_TEST_REPLACE_P25_ROOT"))
    def test_package_p26_future_result_cycle_edge(self): self.run_package(MutationSurface("test_package_p26_future_result_cycle_edge","P26","FUTURE_CYCLE","results/manifest.json:result_review","ABSENT",'{"path":"notes/phase2_control_result_review.md","sha256":"0000000000000000000000000000000000000000000000000000000000000000"}'))
    def test_package_p27_ambient_metadata(self): self.run_package(MutationSurface("test_package_p27_ambient_metadata","P27","AMBIENT","results/manifest.json:ambient_absolute_path||results/manifest.json:ambient_timestamp||results/manifest.json:ambient_host||results/manifest.json:ambient_pid||results/manifest.json:ambient_temp_root","ABSENT||ABSENT||ABSENT||ABSENT||ABSENT","/tmp/p15r-forbidden||2026-08-16T00:00:00Z||forbidden-host||1||p15r-temp-forbidden",variants=5))
    def test_package_p28_noncanonical_json_or_newline(self): self.run_package(MutationSurface("test_package_p28_noncanonical_json_or_newline","P28","CANONICAL","results/manifest.json:encoding||results/target_summary.csv:terminal_lf","indent2_sorted||LF","compact_sorted||ABSENT",variants=2))


def parse_cli(arguments: Sequence[str]) -> tuple[str,str,str]:
    if len(arguments) != 6 or tuple(arguments[::2]) != ("--checked-in","--fresh-a","--fresh-b") or any(not arguments[index] for index in (1,3,5)):
        raise SystemExit(2)
    return arguments[1],arguments[3],arguments[5]


class _BoundedTestSink:
    LIMIT = STREAM_LIMIT

    def __init__(self) -> None:
        self.data=bytearray(); self.overflow=False

    def write(self, value: object) -> int:
        text=str(value); encoded=text.encode("ascii","backslashreplace")
        room=self.LIMIT-len(self.data)
        if len(encoded)>room:
            self.data.extend(encoded[:max(room,0)]); self.overflow=True
        else: self.data.extend(encoded)
        return len(text)

    def flush(self) -> None:
        return None


class _BoundedTestResult(unittest.TextTestResult):
    TRACE_LIMIT = 4096

    def __init__(self, *arguments: object, **keywords: object) -> None:
        super().__init__(*arguments,**keywords); self.subtest_anomalies: list[str]=[]

    def _exc_info_to_string(self, err: object, test: object) -> str:
        text=super()._exc_info_to_string(err,test).encode("ascii","backslashreplace")
        if len(text)>self.TRACE_LIMIT:
            digest=hashlib.sha256(text).hexdigest().encode("ascii")
            text=text[:self.TRACE_LIMIT-82]+b"\n[TRACE_TRUNCATED sha256="+digest+b"]\n"
        return text.decode("ascii")

    def addSubTest(self, test: object, subtest: object, err: object) -> None:
        if err is not None:
            identity=getattr(subtest,"id",lambda:"<subtest>")()
            self.subtest_anomalies.append(str(identity))
        super().addSubTest(test,subtest,err)


def _test_identity(test: object) -> str:
    identity=getattr(test,"id",lambda:"<unknown-test>")()
    return str(identity)


def _write_test_failure(payload: Mapping[str,object]) -> None:
    data=(json.dumps(payload,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\n").encode("ascii")
    if len(data)>_BoundedTestSink.LIMIT: data=b'{"error":"E_TEST_SUMMARY_CEILING"}\n'
    offset=0
    while offset<len(data):
        count=os.write(2,data[offset:])
        if count<=0: raise RuntimeError("test failure write")
        offset+=count


def _run_exact_suite() -> int:
    sink=_BoundedTestSink()
    try:
        loader=unittest.TestLoader(); names=loader.getTestCaseNames(ControlsOracle)
        if loader.errors or tuple(names)!=tuple(sorted(EXACT_TEST_NAMES)) or len(EXACT_TEST_NAMES)!=173 or len(set(EXACT_TEST_NAMES))!=173 or any(re.fullmatch(r"test_[a-z0-9_]+",name) is None for name in names) or any(not callable(ControlsOracle.__dict__.get(name)) for name in EXACT_TEST_NAMES):
            raise RuntimeError("literal loader cardinality")
        suite=unittest.TestSuite(ControlsOracle(name) for name in names)
        runner=unittest.TextTestRunner(stream=sink,verbosity=1,resultclass=_BoundedTestResult)
        result=runner.run(suite)
    except BaseException as error:
        _write_test_failure({"error":"E_TEST_LOADER","exception_type":type(error).__name__,"sink_overflow":sink.overflow,"sink_sha256":hashlib.sha256(bytes(sink.data)).hexdigest()})
        return 1
    failure_rows=sorted((_test_identity(test),hashlib.sha256(trace.encode("ascii","backslashreplace")).hexdigest()) for test,trace in result.failures)
    error_rows=sorted((_test_identity(test),hashlib.sha256(trace.encode("ascii","backslashreplace")).hexdigest()) for test,trace in result.errors)
    skipped_rows=sorted((_test_identity(test),str(reason)) for test,reason in result.skipped)
    expected_rows=sorted((_test_identity(test),hashlib.sha256(trace.encode("ascii","backslashreplace")).hexdigest()) for test,trace in result.expectedFailures)
    unexpected_rows=sorted(_test_identity(test) for test in result.unexpectedSuccesses)
    subtest_rows=sorted(result.subtest_anomalies)
    clean=result.testsRun==173 and not failure_rows and not error_rows and not skipped_rows and not expected_rows and not unexpected_rows and not subtest_rows and not sink.overflow and result.wasSuccessful()
    if clean: return 0
    _write_test_failure({"error":"E_TEST_SUITE","errors":error_rows,"expected_failures":expected_rows,"failures":failure_rows,"skipped":skipped_rows,"sink_overflow":sink.overflow,"sink_sha256":hashlib.sha256(bytes(sink.data)).hexdigest(),"subtest_anomalies":subtest_rows,"tests_run":result.testsRun,"unexpected_successes":unexpected_rows})
    return 1


if __name__ == "__main__":
    ControlsOracle.root_arguments = parse_cli(sys.argv[1:])
    raise SystemExit(_run_exact_suite())
