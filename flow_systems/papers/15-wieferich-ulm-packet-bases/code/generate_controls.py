#!/usr/bin/env python3
"""Byte-bound deterministic subject for the Paper 15R control package.

This module has two, and only two, command-line modes.  It is intentionally
self-contained and is never imported by the independent oracle.  Runtime
authority comes from directory descriptors and immutable source bytes, not
from a pathname discovered after admission.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import os
import re
import stat
import sys
from typing import Iterable, Mapping, Sequence


SCHEMA = "paper15r-wieferich-ulm-controls/1"
MANIFEST_SCHEMA = "paper15r-wieferich-ulm-controls-manifest/1"
PACKAGE_ID = "paper15r-wieferich-ulm-controls"

DESIGN_LOCK = (
    "notes/phase2_control_design_lock.md",
    "db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d",
)
DESIGN_REVIEW = (
    "notes/phase2_control_design_peer_review.md",
    "2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19",
)
IMPLEMENTATION_GATE = (
    "notes/phase2_control_implementation_gate.md",
    "e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8",
)

IMPLEMENTATION_PATHS = (
    "code/generate_controls.py",
    "code/test_controls.py",
    "code/README.md",
    "experiments/reproduce.sh",
    "experiments/README.md",
    "results/README.md",
)

CSV_ARTIFACTS = (
    "valuation_normalization_controls.csv",
    "exponent_order_branch_controls.csv",
    "finite_kernel_truncation_controls.csv",
    "torsion_closure_type_controls.csv",
    "signature_nonpromotion_controls.csv",
    "owner_firewall_controls.csv",
    "proof_ceiling_controls.csv",
    "target_summary.csv",
)
GENERATED_BASENAMES = CSV_ARTIFACTS + ("manifest.json",)

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

EFFECTIVE_AMENDMENTS = (
    ("notes/phase2_control_design_amendment_v1.md", "cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe"),
    ("notes/phase2_control_design_amendment_v2.md", "c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea"),
    ("notes/phase2_control_design_amendment_v3.md", "f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b"),
    ("notes/phase2_control_design_amendment_v4.md", "f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592"),
    ("notes/phase2_control_design_amendment_v5.md", "2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8"),
    ("notes/phase2_control_design_amendment_v6.md", "0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363"),
    ("notes/phase2_control_design_amendment_v7.md", "bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7"),
    ("notes/phase2_control_design_amendment_v8.md", "e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147"),
    ("notes/phase2_control_design_amendment_v9.md", "0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829"),
    ("notes/phase2_control_design_amendment_v10.md", "d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f"),
    ("notes/phase2_control_design_amendment_v11.md", "7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269"),
    ("notes/phase2_control_design_amendment_v13.md", "4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27"),
    ("notes/phase2_control_design_amendment_v14.md", "b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c"),
)

DAG_NODES = ("A", "D", "R", "G", "I", "C", "M", "V")
DAG_EDGES = (
    ("A", "D"), ("D", "R"), ("R", "G"), ("G", "I"),
    ("I", "C"), ("C", "M"), ("M", "V"), ("A", "M"),
    ("D", "M"), ("R", "M"), ("G", "M"), ("I", "M"),
)

AGGREGATES = {
    "BYTE_IDENTICAL_COPIES": 3,
    "CSV_ARTIFACTS": 8,
    "CSV_BODY_ROWS": 120,
    "EXPECTED_NEGATIVES_DETECTED": 35,
    "EXPLICIT_NEGATIVE_ROWS": 35,
    "FRESH_GENERATIONS": 2,
    "GENERATED_ARTIFACTS_INCLUDING_MANIFEST": 9,
    "NEGATIVE_FAILURES": 0,
    "NETWORK_USED": False,
    "PACKAGE_MUTATION_CLASSES": 28,
    "RANDOM_USED": False,
    "SEMANTIC_MUTATION_CLASSES": 35,
    "TOLERANCE_POLICY": "EXACT_ZERO",
    "UNITTEST_ERRORS": 0,
    "UNITTEST_FAILURES": 0,
    "UNITTEST_METHODS": 173,
}

HEADERS = {
    "valuation_normalization_controls.csv": "schema_version,row_id,p,r,branch,expression,factorization,raw_valuation,normalization_subtrahend,kappa,principal_sign,mutation_id,case_kind,negative_reason,oracle,scope_ceiling,tolerance,status".split(","),
    "exponent_order_branch_controls.csv": "schema_version,row_id,witness_kind,p,r,m,ell,ell_minus_1,order_mod_ell,v_r_ell_minus_1,v_r_order,finite_group_model,claim_under_test,mutation_id,case_kind,negative_reason,oracle,scope_ceiling,status".split(","),
    "finite_kernel_truncation_controls.csv": "schema_version,row_id,model_kind,r,target_exponent,kappa,source_exponents,image_numerators,kernel_order,height_orders_d0_to_N,tail_order,depth,tail_vector,root_vector,phi_of_root,root_in_kernel,mutation_id,case_kind,negative_reason,oracle,scope_ceiling,status".split(","),
    "torsion_closure_type_controls.csv": "schema_version,row_id,model_kind,r,kappa,finite_model_id,discrete_tail_order,compact_quotient_order,source_owner,operation,target_owner,statement_scope,mutation_id,case_kind,negative_reason,oracle,status".split(","),
    "signature_nonpromotion_controls.csv": "schema_version,row_id,row_kind,p,q,prime_prefix,kappa_prefix_p,kappa_prefix_q,distinguishing_prime,authorized_conclusion,mutation_id,case_kind,negative_reason,oracle,scope_ceiling,status".split(","),
    "owner_firewall_controls.csv": "schema_version,row_id,row_kind,r,exponent,block_type,label_a,label_b,automorphism_matrix,determinant_mod_r,bare_type_preserved,source_owner,target_owner,claim_under_test,mutation_id,case_kind,negative_reason,oracle,status".split(","),
    "proof_ceiling_controls.csv": "schema_version,row_id,record_kind,binding_path,binding_sha256,claim_class,allowed_state,prohibited_promotion,mutation_id,case_kind,negative_reason,oracle,status".split(","),
    "target_summary.csv": "schema_version,row_id,artifact,expected_rows,expected_columns,expected_negative_rows,expected_mutation_classes,canonical_order_key,oracle_class,status".split(","),
}

ROW_COUNTS = dict(zip(CSV_ARTIFACTS, (16, 14, 18, 10, 12, 15, 26, 9)))
NEGATIVE_COUNTS = dict(zip(CSV_ARTIFACTS, (4, 2, 4, 3, 4, 9, 9, 0)))
ORDER_PREFIX = dict(zip(CSV_ARTIFACTS, ("VC", "EO", "FK", "TC", "SG", "OF", "PC", "TS")))

SEMANTIC_REGISTRY = (
    ("S01", "VC-013", "WRONG_LOCAL_COORDINATE", "E_BRANCH_DOMAIN"),
    ("S02", "VC-014", "WRONG_ODD_MINUS_ONE", "E_NORMALIZATION_ODD"),
    ("S03", "VC-015", "WRONG_TWO_MINUS_THREE", "E_NORMALIZATION_TWO"),
    ("S04", "VC-016", "ERASED_LOCAL_TWO_SIGN", "E_TWO_SIGN"),
    ("S05", "EO-013", "DIAGONAL_BOUNDED_SURJECTIVITY", "E_BOUNDED_EXTENSION"),
    ("S06", "EO-014", "MERE_DIVISIBILITY_AS_EXACT_ORDER", "E_EXACT_DOUBLE_VALUATION"),
    ("S07", "FK-015", "AMBIENT_ROOT_WITHOUT_KERNEL_EQUATION_R2_K1", "E_ROOT_NOT_IN_KERNEL"),
    ("S08", "FK-016", "AMBIENT_ROOT_WITHOUT_KERNEL_EQUATION_R2_K2", "E_ROOT_NOT_IN_KERNEL"),
    ("S09", "FK-017", "AMBIENT_ROOT_WITHOUT_KERNEL_EQUATION_R3_K1", "E_ROOT_NOT_IN_KERNEL"),
    ("S10", "FK-018", "AMBIENT_ROOT_WITHOUT_KERNEL_EQUATION_R3_K2", "E_ROOT_NOT_IN_KERNEL"),
    ("S11", "TC-008", "RAW_TORSION_FOR_CLOSURE", "E_CLOSURE_REQUIRED"),
    ("S12", "TC-009", "FINITE_MODEL_PROMOTED_TO_INFINITE_TYPE", "E_FINITE_MODEL_CEILING"),
    ("S13", "TC-010", "DISCRETE_TAIL_CONFUSED_WITH_COMPACT_CLOSURE", "E_OWNER_TYPE"),
    ("S14", "SG-009", "FINITE_PREFIX_EQUALITY_TO_GROUP_ISOMORPHISM", "E_PREFIX_NONPROMOTION"),
    ("S15", "SG-010", "ONE_COORDINATE_SEPARATION_TO_UNIVERSAL_RECOVERY", "E_RECOVERY_CEILING"),
    ("S16", "SG-011", "FINITE_RANGE_TO_GLOBAL_INJECTIVITY", "E_RANGE_NONPROMOTION"),
    ("S17", "SG-012", "OPEN_SIGNATURE_MAP_DECLARED_INJECTIVE", "E_OPEN_PROBLEM"),
    ("S18", "OF-007", "MARKED_TO_BARE_OWNER_SPLICE", "E_OWNER_SPLICE"),
    ("S19", "OF-008", "AMBIENT_MISSING_COORDINATE_IMPORTED", "E_AMBIENT_IMPORT"),
    ("S20", "OF-009", "ACTUAL_PACKET_TOPOLOGY_IMPORTED", "E_ACTUAL_IMPORT"),
    ("S21", "OF-010", "STANDARDIZED_FLOW_IMPORTED", "E_FLOW_IMPORT"),
    ("S22", "OF-011", "HAAR_CLAIM_ADDED", "E_HAAR_PROMOTION"),
    ("S23", "OF-012", "MEASURE_CLAIM_ADDED", "E_MEASURE_PROMOTION"),
    ("S24", "OF-013", "TRACE_CLAIM_ADDED", "E_TRACE_PROMOTION"),
    ("S25", "OF-014", "OPERATOR_CLAIM_ADDED", "E_OPERATOR_PROMOTION"),
    ("S26", "OF-015", "DETERMINANT_CLAIM_ADDED", "E_DETERMINANT_PROMOTION"),
    ("S27", "PC-018", "GRH_PROMOTION", "E_GRH"),
    ("S28", "PC-019", "DENSITY_PROMOTION", "E_DENSITY"),
    ("S29", "PC-020", "ABSOLUTE_PRIORITY_PROMOTION", "E_PRIORITY"),
    ("S30", "PC-021", "ROUTE_B_PROMOTION", "E_ROUTE_B"),
    ("S31", "PC-022", "UNIVERSAL_RECOVERY_PROMOTION", "E_RECOVERY_CEILING"),
    ("S32", "PC-023", "FINITE_CONTROL_AS_SYMBOLIC_PROOF", "E_PROOF_CEILING"),
    ("S33", "PC-024", "SOURCE_RECEIPT_AS_EXECUTED_THEOREM", "E_SOURCE_RECEIPT_CEILING"),
    ("S34", "PC-025", "FINITE_CONTROL_AS_CHEBOTAREV_PROOF", "E_CHEBOTAREV_CEILING"),
    ("S35", "PC-026", "FINITE_CONTROL_AS_ULM_PROOF", "E_ULM_CEILING"),
)
NEGATIVE_BY_ROW = {row: (mutation, reason, detector) for mutation, row, reason, detector in SEMANTIC_REGISTRY}

DENIED_NAMES = frozenset(("__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"))
DENIED_SUFFIXES = (".pyc", ".pyo", ".swp", ".swo", ".tmp", ".temp", ".lock")
OPEN_DIRECTORY = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
OPEN_REGULAR = os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC


class ControlFailure(Exception):
    def __init__(self, token: str, detail: str = "") -> None:
        super().__init__(token)
        self.token = token
        self.detail = detail


def reject(token: str, detail: str = "") -> None:
    raise ControlFailure(token, detail)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def decimal(text: str, *, nonzero: bool = False) -> int:
    if re.fullmatch(r"0|[1-9][0-9]*", text) is None:
        reject("E_SCALAR_GRAMMAR")
    value = int(text)
    if nonzero and value == 0:
        reject("E_SCALAR_GRAMMAR")
    return value


def path_components(relative: str) -> tuple[str, ...]:
    if not relative or relative.startswith("/") or "\x00" in relative:
        reject("E_SYMLINK")
    parts = tuple(relative.split("/"))
    if any(part in ("", ".", "..") for part in parts):
        reject("E_SYMLINK")
    return parts


def open_dir_beneath(root_fd: int, relative: str) -> int:
    current = os.dup(root_fd)
    try:
        for part in path_components(relative):
            following = os.open(part, OPEN_DIRECTORY, dir_fd=current)
            os.close(current)
            current = following
        st = os.fstat(current)
        if not stat.S_ISDIR(st.st_mode):
            reject("E_SYMLINK")
        return current
    except BaseException:
        try:
            os.close(current)
        except OSError:
            pass
        raise


def open_regular_beneath(root_fd: int, relative: str, token: str) -> int:
    parts = path_components(relative)
    parent = os.dup(root_fd)
    try:
        for part in parts[:-1]:
            following = os.open(part, OPEN_DIRECTORY, dir_fd=parent)
            os.close(parent)
            parent = following
        try:
            fd = os.open(parts[-1], OPEN_REGULAR, dir_fd=parent)
        except OSError:
            reject(token, parts[-1])
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode):
            os.close(fd)
            reject("E_SYMLINK", parts[-1])
        if st.st_nlink != 1:
            os.close(fd)
            reject("E_HARDLINK", parts[-1])
        return fd
    finally:
        os.close(parent)


def read_fd_all(fd: int) -> bytes:
    os.lseek(fd, 0, os.SEEK_SET)
    parts: list[bytes] = []
    while True:
        block = os.read(fd, 65536)
        if not block:
            return b"".join(parts)
        parts.append(block)


def read_regular_beneath(root_fd: int, relative: str, token: str) -> bytes:
    fd = open_regular_beneath(root_fd, relative, token)
    try:
        return read_fd_all(fd)
    finally:
        os.close(fd)


def open_argument_directory(argument: str) -> int:
    if not argument or "\x00" in argument:
        reject("E_MISSING_ARTIFACT")
    if argument.startswith("/"):
        root = os.open("/", OPEN_DIRECTORY)
        relative = argument[1:]
    else:
        root = os.open(".", OPEN_DIRECTORY)
        relative = argument
    try:
        return open_dir_beneath(root, relative)
    except OSError:
        reject("E_MISSING_ARTIFACT")
    finally:
        os.close(root)
    raise AssertionError("unreachable")


def valuation(number: int, prime: int) -> int:
    if number <= 0 or prime < 2:
        reject("E_ARITHMETIC_DOMAIN")
    count = 0
    while number % prime == 0:
        number //= prime
        count += 1
    return count


def factorization(number: int) -> str:
    if number < 1:
        reject("E_ARITHMETIC_DOMAIN")
    if number == 1:
        return "1"
    values: list[str] = []
    divisor = 2
    remaining = number
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            values.append(str(divisor) if exponent == 1 else f"{divisor}^{exponent}")
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        values.append(str(remaining))
    return "*".join(values)


def multiplicative_order(base: int, modulus: int) -> int:
    if modulus < 2 or base % modulus == 0:
        reject("E_ORDER_DOMAIN")
    residue = 1
    for order in range(1, modulus + 1):
        residue = residue * base % modulus
        if residue == 1:
            return order
    reject("E_ORDER_DOMAIN")
    raise AssertionError("unreachable")


def vector(values: Iterable[int]) -> str:
    return "[" + ";".join(str(value) for value in values) + "]"


def finite_kernel_invariants(r: int, target: int, exponents: Sequence[int], numerators: Sequence[int]) -> tuple[int, list[int]]:
    modulus = r ** target
    image_gcd = modulus
    for numerator in numerators:
        image_gcd = math.gcd(image_gcd, numerator)
    image_order = modulus // image_gcd
    kernel_order = r ** sum(exponents) // image_order
    heights: list[int] = []
    for depth in range(target + 1):
        torsion_source = r ** sum(min(exponent, depth) for exponent in exponents)
        restricted_gcd = modulus
        for exponent, numerator in zip(exponents, numerators):
            restricted_gcd = math.gcd(restricted_gcd, numerator * r ** max(exponent - depth, 0))
        restricted_image = modulus // restricted_gcd
        heights.append(kernel_order // (torsion_source // restricted_image))
    return kernel_order, heights


def base_row(header: Sequence[str], row_id: str, case_kind: str, oracle: str, scope: str = "") -> dict[str, str]:
    row = {field: "" for field in header}
    row["schema_version"] = SCHEMA
    row["row_id"] = row_id
    if "case_kind" in row:
        row["case_kind"] = case_kind
    if "oracle" in row:
        row["oracle"] = oracle
    if "scope_ceiling" in row:
        row["scope_ceiling"] = scope
    if "tolerance" in row:
        row["tolerance"] = "0"
    row["status"] = "PASS"
    if row_id in NEGATIVE_BY_ROW:
        mutation, reason, _detector = NEGATIVE_BY_ROW[row_id]
        row["mutation_id"] = mutation
        row["negative_reason"] = reason
    return row


def finish(row: dict[str, str], **values: object) -> dict[str, str]:
    for key, value in values.items():
        if key not in row:
            reject("E_INTERNAL_FIXTURE", key)
        if isinstance(value, bool):
            row[key] = "true" if value else "false"
        elif value is None:
            row[key] = ""
        else:
            row[key] = str(value)
    return row


def valuation_rows() -> list[dict[str, str]]:
    header = HEADERS[CSV_ARTIFACTS[0]]
    oracle = "EXACT_KAPPA_BRANCH_AND_FACTORIZATION"
    scope = "FINITE_INTEGER_DIAGNOSTIC_NOT_INFINITE_THEOREM"
    rows: list[dict[str, str]] = []
    positives = (("VC-001",2,3),("VC-002",5,3),("VC-003",7,5),("VC-004",53,3),("VC-005",2,11),("VC-006",3,11),("VC-007",3,2),("VC-008",5,2),("VC-009",7,2),("VC-010",17,2),("VC-011",2,2),("VC-012",3,3))
    for row_id, p, r in positives:
        row = base_row(header, row_id, "DIAGNOSTIC", oracle, scope)
        if p == r:
            rows.append(finish(row, p=p, r=r, branch="DIAGONAL", normalization_subtrahend=0, kappa=0))
        elif r == 2:
            expression = p * p - 1
            raw = valuation(expression, 2)
            rows.append(finish(row, p=p, r=r, branch="TWO_OFF_LOCAL", expression=expression, factorization=factorization(expression), raw_valuation=raw, normalization_subtrahend=3, kappa=raw-3, principal_sign=1 if p % 4 == 1 else -1))
        else:
            expression = p ** (r - 1) - 1
            raw = valuation(expression, r)
            rows.append(finish(row, p=p, r=r, branch="ODD_OFF_LOCAL", expression=expression, factorization=factorization(expression), raw_valuation=raw, normalization_subtrahend=1, kappa=raw-1))
    negatives = (
        ("VC-013", dict(p=3,r=3,branch="ODD_OFF_LOCAL_INVALID",expression=8,factorization="2^3",raw_valuation=0,normalization_subtrahend=1,kappa=-1)),
        ("VC-014", dict(p=7,r=5,branch="ODD_OFF_LOCAL",expression=2400,factorization="2^5*3*5^2",raw_valuation=2,normalization_subtrahend=0,kappa=2)),
        ("VC-015", dict(p=7,r=2,branch="TWO_OFF_LOCAL",expression=48,factorization="2^4*3",raw_valuation=4,normalization_subtrahend=2,kappa=2,principal_sign=-1)),
        ("VC-016", dict(p=3,r=2,branch="TWO_OFF_LOCAL",expression=8,factorization="2^3",raw_valuation=3,normalization_subtrahend=3,kappa=0)),
    )
    for row_id, values in negatives:
        rows.append(finish(base_row(header, row_id, "NEGATIVE", oracle, scope), **values))
    return rows


def order_rows() -> list[dict[str, str]]:
    header = HEADERS[CSV_ARTIFACTS[1]]
    oracle = "FINITE_ORDER_AND_BRANCH_FIREWALL"
    scope = "FINITE_WITNESS_ONLY_NOT_EXISTENCE_DENSITY_OR_CHEBOTAREV"
    specs = (
        ("EO-001","LOCAL_PRINCIPAL_UNIT",2,3,None,3,"LOCAL_ODD_COMPONENT_NONZERO",""),
        ("EO-002","LOCAL_TWO_PRINCIPAL_SIGN",3,2,None,2,"LOCAL_TWO_COMPONENT_NONZERO","u=-3;u_mod8=5"),
        ("EO-003","PRIMITIVE_DIVISOR_DETECTION",2,2,1,3,"PRIMITIVE_ORDER_EQUALS_P_POWER",""),
        ("EO-004","PRIMITIVE_DIVISOR_DETECTION",2,2,2,5,"PRIMITIVE_ORDER_EQUALS_P_POWER",""),
        ("EO-005","PRIMITIVE_DIVISOR_DETECTION",3,3,1,13,"PRIMITIVE_ORDER_EQUALS_P_POWER",""),
        ("EO-006","OFF_LOCAL_DOUBLE_VALUATION",2,3,1,7,"EXACT_DOUBLE_VALUATION_EQUALS_M",""),
        ("EO-007","OFF_LOCAL_DOUBLE_VALUATION",2,3,2,19,"EXACT_DOUBLE_VALUATION_EQUALS_M",""),
        ("EO-008","OFF_LOCAL_DOUBLE_VALUATION",7,5,1,11,"EXACT_DOUBLE_VALUATION_EQUALS_M",""),
        ("EO-009","OFF_LOCAL_DOUBLE_VALUATION",7,5,2,101,"EXACT_DOUBLE_VALUATION_EQUALS_M",""),
        ("EO-010","OFF_LOCAL_DOUBLE_VALUATION",3,2,1,7,"EXACT_DOUBLE_VALUATION_EQUALS_M",""),
        ("EO-011","OFF_LOCAL_DOUBLE_VALUATION",3,2,2,5,"EXACT_DOUBLE_VALUATION_EQUALS_M",""),
        ("EO-012","OFF_LOCAL_DOUBLE_VALUATION",3,2,3,41,"EXACT_DOUBLE_VALUATION_EQUALS_M",""),
    )
    rows: list[dict[str, str]] = []
    for row_id, kind, p, r, m, ell, claim, model in specs:
        values: dict[str, object] = dict(witness_kind=kind,p=p,r=r,m=m,ell=ell,finite_group_model=model,claim_under_test=claim)
        if row_id != "EO-002":
            order = multiplicative_order(p, ell)
            values.update(ell_minus_1=ell-1,order_mod_ell=order,v_r_ell_minus_1=valuation(ell-1,r),v_r_order=valuation(order,r))
        rows.append(finish(base_row(header,row_id,"DIAGNOSTIC",oracle,scope),**values))
    rows.append(finish(base_row(header,"EO-013","NEGATIVE",oracle,scope),witness_kind="DIAGONAL_BOUNDED_EXTENSION_REGRESSION",p=2,r=2,m=3,ell=17,ell_minus_1=16,order_mod_ell=8,v_r_ell_minus_1=4,v_r_order=3,finite_group_model="C16_SUPERGROUP_C8_SUBGROUP;bounded_image_order=4",claim_under_test="BOUNDED_ORDER_RESTRICTION_SURJECTIVE"))
    rows.append(finish(base_row(header,"EO-014","NEGATIVE",oracle,scope),witness_kind="MERE_DIVISIBILITY_AS_EXACT",p=2,r=3,m=1,ell=19,ell_minus_1=18,order_mod_ell=18,v_r_ell_minus_1=2,v_r_order=2,claim_under_test="DIVISIBILITY_IMPLIES_EXACT_DEPTH_M"))
    return rows


def kernel_rows() -> list[dict[str, str]]:
    header = HEADERS[CSV_ARTIFACTS[2]]
    oracle = "EXHAUSTIVE_FINITE_KERNEL_HEIGHT_AND_INTERNAL_ROOT"
    scope = "FINITE_TRUNCATION_ONLY_NOT_INFINITE_HEIGHT_OR_ULM_PROOF"
    specs = (
        ("FK-001","HOMOGENEOUS_BLOCK",2,3,None,(1,1,1),(4,4,0),None),
        ("FK-002","HOMOGENEOUS_BLOCK",3,3,None,(2,2,2),(3,6,0),None),
        ("FK-003","EXCEPTIONAL_MIXED_BLOCK",2,3,None,(1,1,2,2),(4,0,2,6),None),
        ("FK-004","EXCEPTIONAL_MIXED_BLOCK",3,3,None,(1,1,2,2),(9,0,3,6),None),
        ("FK-005","PHI_TRUNCATION",2,3,0,(1,2,3,3),(4,2,1,1),1),
        ("FK-006","PHI_TRUNCATION",2,3,1,(1,2,3,4),(4,2,1,1),2),
        ("FK-007","PHI_TRUNCATION",2,3,2,(1,2,3,5),(4,2,1,1),4),
        ("FK-008","PHI_TRUNCATION",3,2,0,(1,2,2),(3,1,1),1),
        ("FK-009","PHI_TRUNCATION",3,2,1,(1,2,3),(3,1,1),3),
        ("FK-010","PHI_TRUNCATION",3,2,2,(1,2,4),(3,1,1),9),
    )
    rows: list[dict[str, str]] = []
    inherited: dict[str, tuple[int,int,int,tuple[int,...],tuple[int,...]]] = {}
    for row_id, kind, r, target, kappa_value, exponents, images, tail in specs:
        kernel_order, heights = finite_kernel_invariants(r,target,exponents,images)
        rows.append(finish(base_row(header,row_id,"DIAGNOSTIC",oracle,scope),model_kind=kind,r=r,target_exponent=target,kappa=kappa_value,source_exponents=vector(exponents),image_numerators=vector(images),kernel_order=kernel_order,height_orders_d0_to_N=vector(heights),tail_order=tail))
        inherited[row_id] = (r,target,0 if kappa_value is None else kappa_value,exponents,images)
    roots = (
        ("FK-011","FK-006","INTERNAL_ROOT",1,(0,0,0,8),(1,0,0,4),"DIAGNOSTIC"),
        ("FK-012","FK-007","INTERNAL_ROOT",2,(0,0,0,8),(0,3,0,2),"DIAGNOSTIC"),
        ("FK-013","FK-009","INTERNAL_ROOT",1,(0,0,9),(2,0,3),"DIAGNOSTIC"),
        ("FK-014","FK-010","INTERNAL_ROOT",2,(0,0,9),(0,8,1),"DIAGNOSTIC"),
        ("FK-015","FK-006","AMBIENT_ROOT_NEGATIVE",1,(0,0,0,8),(0,0,0,4),"NEGATIVE"),
        ("FK-016","FK-007","AMBIENT_ROOT_NEGATIVE",2,(0,0,0,8),(0,0,0,2),"NEGATIVE"),
        ("FK-017","FK-009","AMBIENT_ROOT_NEGATIVE",1,(0,0,9),(0,0,3),"NEGATIVE"),
        ("FK-018","FK-010","AMBIENT_ROOT_NEGATIVE",2,(0,0,9),(0,0,1),"NEGATIVE"),
    )
    for row_id, source, kind, depth, tail_values, root_values, case_kind in roots:
        r,target,kappa_value,exponents,images = inherited[source]
        phi = sum(a*b for a,b in zip(images,root_values)) % (r ** target)
        rows.append(finish(base_row(header,row_id,case_kind,oracle,scope),model_kind=kind,r=r,target_exponent=target,kappa=kappa_value,source_exponents=vector(exponents),image_numerators=vector(images),depth=depth,tail_vector=vector(tail_values),root_vector=vector(root_values),phi_of_root=phi,root_in_kernel=(phi==0)))
    return rows


def torsion_rows() -> list[dict[str, str]]:
    header = HEADERS[CSV_ARTIFACTS[3]]
    oracle = "TORSION_CLOSURE_TYPE_AND_FINITE_QUOTIENT_FIREWALL"
    rows: list[dict[str, str]] = []
    index = 1
    for r in (2,3):
        for kappa_value in (0,1,2):
            order = r ** kappa_value
            rows.append(finish(base_row(header,f"TC-{index:03d}","RECEIPT",oracle),model_kind="FINITE_DUAL_MODEL",r=r,kappa=kappa_value,finite_model_id=f"PHI-R{r}-K{kappa_value}",discrete_tail_order=order,compact_quotient_order=order,source_owner="DISCRETE_TRUNCATED_KERNEL",operation="FINITE_ANNIHILATOR_ORDER_DUALITY",target_owner="FINITE_COMPACT_DUAL_MODEL",statement_scope="FINITE_TYPE_RECEIPT_ONLY_NOT_COMPACT_INFINITE_THEOREM"))
            index += 1
    rows.append(finish(base_row(header,"TC-007","RECEIPT",oracle),model_kind="SYMBOLIC_TYPE_RECEIPT",source_owner="DISCRETE_K",operation="ann(closure(Tor(COMPACT_B)))=r^omega(DISCRETE_K)",target_owner="COMPACT_B",statement_scope="SYMBOLIC_IDENTITY_BOUND_TO_PROOF_NOT_PROVED_BY_MODEL"))
    for row_id, source, operation, target in (
        ("TC-008","COMPACT_B","ann(Tor(COMPACT_B))=r^omega(DISCRETE_K)","DISCRETE_K"),
        ("TC-009","FINITE_COMPACT_DUAL_MODEL","FINITE_MODEL_PROVES_INFINITE_COMPACT_THEOREM","COMPACT_B"),
        ("TC-010","DISCRETE_K","r^omega(DISCRETE_K)=closure(Tor(COMPACT_B))","COMPACT_B"),
    ):
        rows.append(finish(base_row(header,row_id,"NEGATIVE",oracle),model_kind="POLICY_NEGATIVE",source_owner=source,operation=operation,target_owner=target,statement_scope="REJECTED_TYPE_OR_SCOPE_PROMOTION"))
    return rows


def kappa(p: int, r: int) -> int:
    if p == r:
        return 0
    return valuation(p*p-1,2)-3 if r == 2 else valuation(p**(r-1)-1,r)-1


def signature_rows() -> list[dict[str, str]]:
    header = HEADERS[CSV_ARTIFACTS[4]]
    oracle = "FINITE_SIGNATURE_PREFIX_AND_NONPROMOTION"
    scope = "FINITE_PREFIX_ONLY_GLOBAL_SIGNATURE_MAP_OPEN"
    primes = (2,3,5,7,11,13)
    prefix = vector(primes)
    values_by_prime: dict[int,str] = {}
    rows: list[dict[str,str]] = []
    for index,p in enumerate(primes,1):
        values = vector(kappa(p,r) for r in primes)
        values_by_prime[p] = values
        rows.append(finish(base_row(header,f"SG-{index:03d}","DIAGNOSTIC",oracle,scope),row_kind="PREFIX",p=p,prime_prefix=prefix,kappa_prefix_p=values,authorized_conclusion="FINITE_PREFIX_ONLY"))
    rows.append(finish(base_row(header,"SG-007","DIAGNOSTIC",oracle,scope),row_kind="AUTHORIZED_PAIR_SEPARATION",p=2,q=3,prime_prefix=prefix,kappa_prefix_p=values_by_prime[2],kappa_prefix_q=values_by_prime[3],distinguishing_prime=11,authorized_conclusion="r=11;B_2_NOT_ISOMORPHIC_B_3"))
    rows.append(finish(base_row(header,"SG-008","DIAGNOSTIC",oracle,scope),row_kind="FINITE_PREFIX_COLLISION_DIAGNOSTIC",p=2,q=5,prime_prefix=prefix,kappa_prefix_p=values_by_prime[2],kappa_prefix_q=values_by_prime[5],authorized_conclusion="NO_GLOBAL_CONCLUSION"))
    rows.append(finish(base_row(header,"SG-009","NEGATIVE",oracle,scope),row_kind="POLICY_NEGATIVE",p=2,q=5,prime_prefix=prefix,kappa_prefix_p=values_by_prime[2],kappa_prefix_q=values_by_prime[5],authorized_conclusion="B_2_ISOMORPHIC_B_5"))
    rows.append(finish(base_row(header,"SG-010","NEGATIVE",oracle,scope),row_kind="POLICY_NEGATIVE",p=2,q=3,prime_prefix=prefix,kappa_prefix_p=values_by_prime[2],kappa_prefix_q=values_by_prime[3],distinguishing_prime=11,authorized_conclusion="UNIVERSAL_RECOVER_P"))
    rows.append(finish(base_row(header,"SG-011","NEGATIVE",oracle,scope),row_kind="POLICY_NEGATIVE",prime_prefix=prefix,authorized_conclusion="SIGNATURE_MAP_GLOBALLY_INJECTIVE"))
    rows.append(finish(base_row(header,"SG-012","NEGATIVE",oracle,scope),row_kind="POLICY_NEGATIVE",authorized_conclusion="SIGNATURE_MAP_KNOWN_INJECTIVE"))
    return rows


def owner_rows() -> list[dict[str, str]]:
    header = HEADERS[CSV_ARTIFACTS[5]]
    oracle = "FINITE_BASIS_SWAP_AND_OWNER_TYPE_FIREWALL"
    rows = [
        finish(base_row(header,"OF-001","DIAGNOSTIC",oracle),row_kind="BASIS_SWAP",r=5,exponent=2,block_type="C_25+C_25",label_a=101,label_b=151,automorphism_matrix="[0;1]/[1;0]",determinant_mod_r=4,bare_type_preserved=True,source_owner="FINITE_MARKED_BLOCK",target_owner="FINITE_BARE_BLOCK",claim_under_test="LABEL_SWAP_PRESERVES_BARE_TYPE"),
        finish(base_row(header,"OF-002","DIAGNOSTIC",oracle),row_kind="BASIS_SWAP",r=3,exponent=2,block_type="C_9+C_9",label_a=19,label_b=37,automorphism_matrix="[0;1]/[1;0]",determinant_mod_r=2,bare_type_preserved=True,source_owner="FINITE_MARKED_BLOCK",target_owner="FINITE_BARE_BLOCK",claim_under_test="LABEL_SWAP_PRESERVES_BARE_TYPE"),
    ]
    for row_id, owner, claim in (
        ("OF-003","MARKED_EXACT_SEQUENCE","LABELLED_COORDINATE_SUPPORT"),
        ("OF-004","BARE_COMPACT_QUOTIENT","UNMARKED_TOPOLOGICAL_GROUP"),
        ("OF-005","AMBIENT_U_P","MISSING_LOCAL_COORDINATE_MARKER"),
        ("OF-006","ACTUAL_PACKET_Q_P","ACTUAL_INDISCRETE_TOPOLOGY"),
    ):
        rows.append(finish(base_row(header,row_id,"RECEIPT",oracle),row_kind="OWNER_RECORD",source_owner=owner,target_owner=owner,claim_under_test=claim))
    for row_id, source, target in (
        ("OF-007","MARKED_EXACT_SEQUENCE","BARE_COMPACT_QUOTIENT"),
        ("OF-008","AMBIENT_U_P","BARE_COMPACT_QUOTIENT"),
        ("OF-009","ACTUAL_PACKET_Q_P","BARE_COMPACT_QUOTIENT"),
        ("OF-010","STANDARDIZED_FLOW","BARE_COMPACT_QUOTIENT"),
        ("OF-011","BARE_COMPACT_QUOTIENT","HAAR_OWNER"),
        ("OF-012","BARE_COMPACT_QUOTIENT","MEASURED_OWNER"),
        ("OF-013","BARE_COMPACT_QUOTIENT","TRACE_OWNER"),
        ("OF-014","BARE_COMPACT_QUOTIENT","OPERATOR_OWNER"),
        ("OF-015","BARE_COMPACT_QUOTIENT","DETERMINANT_OWNER"),
    ):
        rows.append(finish(base_row(header,row_id,"NEGATIVE",oracle),row_kind="OWNER_NEGATIVE",source_owner=source,target_owner=target,claim_under_test=NEGATIVE_BY_ROW[row_id][1]))
    return rows


def ceiling_rows() -> list[dict[str, str]]:
    header = HEADERS[CSV_ARTIFACTS[6]]
    oracle = "BYTE_BINDING_DAG_AND_PROOF_CEILING"
    rows: list[dict[str,str]] = []
    for index,(path,digest) in enumerate(AUTHORITY_BINDINGS,1):
        rows.append(finish(base_row(header,f"PC-{index:03d}","RECEIPT",oracle),record_kind="AUTHORITY_BINDING",binding_path=path,binding_sha256=digest))
    for row_id, claim, allowed, promotion in (
        ("PC-015","FINITE_CONTROL_CEILING","DIAGNOSTIC_ONLY","SYMBOLIC_PROOF"),
        ("PC-016","SOURCE_RECEIPT","BYTE_BINDING_ONLY","EXECUTED_THEOREM"),
        ("PC-017","UNIVERSAL_RECOVERY","OPEN_NOT_AUTHORIZED","KNOWN_INJECTIVE"),
    ):
        rows.append(finish(base_row(header,row_id,"RECEIPT",oracle),record_kind="POLICY_RECEIPT",claim_class=claim,allowed_state=allowed,prohibited_promotion=promotion))
    for index in range(18,27):
        row_id = f"PC-{index:03d}"
        rows.append(finish(base_row(header,row_id,"NEGATIVE",oracle),record_kind="POLICY_NEGATIVE",claim_class="PROHIBITED_PROMOTION",allowed_state="REJECTED",prohibited_promotion=NEGATIVE_BY_ROW[row_id][1]))
    return rows


def summary_rows() -> list[dict[str, str]]:
    header = HEADERS[CSV_ARTIFACTS[7]]
    specs = (
        ("TS-001",CSV_ARTIFACTS[0],16,18,4,4,"VC_ASCENDING","EXACT_KAPPA_BRANCH_AND_FACTORIZATION"),
        ("TS-002",CSV_ARTIFACTS[1],14,19,2,2,"EO_ASCENDING","FINITE_ORDER_AND_BRANCH_FIREWALL"),
        ("TS-003",CSV_ARTIFACTS[2],18,22,4,4,"FK_ASCENDING","EXHAUSTIVE_FINITE_KERNEL_HEIGHT_AND_INTERNAL_ROOT"),
        ("TS-004",CSV_ARTIFACTS[3],10,17,3,3,"TC_ASCENDING","TORSION_CLOSURE_TYPE_AND_FINITE_QUOTIENT_FIREWALL"),
        ("TS-005",CSV_ARTIFACTS[4],12,16,4,4,"SG_ASCENDING","FINITE_SIGNATURE_PREFIX_AND_NONPROMOTION"),
        ("TS-006",CSV_ARTIFACTS[5],15,19,9,9,"OF_ASCENDING","FINITE_BASIS_SWAP_AND_OWNER_TYPE_FIREWALL"),
        ("TS-007",CSV_ARTIFACTS[6],26,13,9,9,"PC_ASCENDING","BYTE_BINDING_DAG_AND_PROOF_CEILING"),
        ("TS-008",CSV_ARTIFACTS[7],9,10,0,0,"TS_ASCENDING","COUNT_SCHEMA_NEGATIVE_MUTATION_TOTAL"),
        ("TS-009","PACKAGE_TOTAL",120,"MIXED",35,35,"SECTION_3_ARTIFACT_ORDER","COUNT_SCHEMA_NEGATIVE_MUTATION_TOTAL"),
    )
    return [finish(base_row(header,row_id,"",""),artifact=artifact,expected_rows=rows,expected_columns=columns,expected_negative_rows=negatives,expected_mutation_classes=mutations,canonical_order_key=order,oracle_class=oracle) for row_id,artifact,rows,columns,negatives,mutations,order,oracle in specs]


def all_rows() -> dict[str, list[dict[str, str]]]:
    tables = {
        CSV_ARTIFACTS[0]: valuation_rows(), CSV_ARTIFACTS[1]: order_rows(),
        CSV_ARTIFACTS[2]: kernel_rows(), CSV_ARTIFACTS[3]: torsion_rows(),
        CSV_ARTIFACTS[4]: signature_rows(), CSV_ARTIFACTS[5]: owner_rows(),
        CSV_ARTIFACTS[6]: ceiling_rows(), CSV_ARTIFACTS[7]: summary_rows(),
    }
    if tuple(tables) != CSV_ARTIFACTS or sum(map(len,tables.values())) != 120:
        reject("E_AGGREGATE")
    return tables


def csv_bytes(header: Sequence[str], rows: Sequence[Mapping[str,str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream,fieldnames=list(header),delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL,doublequote=True,escapechar=None,lineterminator="\n",extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    data = stream.getvalue().encode("utf-8")
    if data.startswith(b"\xef\xbb\xbf") or b"\r" in data or b"\x00" in data or not data.endswith(b"\n") or data.endswith(b"\n\n"):
        reject("E_CANONICAL_BYTES")
    return data


def canonical_json(value: object) -> bytes:
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode("utf-8")


def scan_tree(root_fd: int, root_index: int, relative: str = ".") -> tuple[tuple[object,...], ...]:
    records: list[tuple[object,...]] = []

    def visit(directory_fd: int, name: str) -> None:
        directory_stat = os.fstat(directory_fd)
        if not stat.S_ISDIR(directory_stat.st_mode):
            reject("E_VERIFY_ONLY_METADATA", name)
        records.append((root_index,name,"DIRECTORY",stat.S_IMODE(directory_stat.st_mode),directory_stat.st_size,"",directory_stat.st_mtime_ns,directory_stat.st_ctime_ns,directory_stat.st_nlink,directory_stat.st_dev,directory_stat.st_ino))
        try:
            names = sorted(os.listdir(directory_fd), key=lambda item:item.encode("utf-8"))
        except (OSError,UnicodeError):
            reject("E_VERIFY_ONLY_METADATA", name)
        for child_name in names:
            child_relative = child_name if name == "." else name + "/" + child_name
            try:
                lst = os.stat(child_name,dir_fd=directory_fd,follow_symlinks=False)
            except OSError:
                reject("E_VERIFY_ONLY_METADATA", child_relative)
            if stat.S_ISLNK(lst.st_mode):
                reject("E_SYMLINK", child_relative)
            if stat.S_ISREG(lst.st_mode) and lst.st_nlink != 1:
                reject("E_HARDLINK", child_relative)
            if child_name in DENIED_NAMES or child_name.endswith(DENIED_SUFFIXES):
                reject("E_CACHE_PRE", child_name)
            if stat.S_ISDIR(lst.st_mode):
                try:
                    child_fd = os.open(child_name,OPEN_DIRECTORY,dir_fd=directory_fd)
                except OSError:
                    reject("E_VERIFY_ONLY_METADATA", child_relative)
                try:
                    fst = os.fstat(child_fd)
                    if (fst.st_dev,fst.st_ino) != (lst.st_dev,lst.st_ino):
                        reject("E_VERIFY_ONLY_METADATA", child_relative)
                    visit(child_fd,child_relative)
                finally:
                    os.close(child_fd)
            elif stat.S_ISREG(lst.st_mode):
                if lst.st_nlink != 1:
                    reject("E_HARDLINK", child_relative)
                try:
                    child_fd = os.open(child_name,OPEN_REGULAR,dir_fd=directory_fd)
                except OSError:
                    reject("E_VERIFY_ONLY_METADATA", child_relative)
                try:
                    fst = os.fstat(child_fd)
                    if (fst.st_dev,fst.st_ino) != (lst.st_dev,lst.st_ino) or fst.st_nlink != 1:
                        reject("E_VERIFY_ONLY_METADATA", child_relative)
                    data = read_fd_all(child_fd)
                    records.append((root_index,child_relative,"REGULAR",stat.S_IMODE(fst.st_mode),fst.st_size,sha256_bytes(data),fst.st_mtime_ns,fst.st_ctime_ns,fst.st_nlink,fst.st_dev,fst.st_ino))
                finally:
                    os.close(child_fd)
            else:
                reject("E_VERIFY_ONLY_METADATA", child_relative)

    visit(root_fd,relative)
    return tuple(records)


def scope_receipt(package_fd: int, input_fd: int) -> tuple[tuple[object,...], ...]:
    roots: list[int] = []
    try:
        roots.append(open_dir_beneath(package_fd,"code"))
        roots.append(open_dir_beneath(package_fd,"experiments"))
        roots.append(os.dup(input_fd))
        records: list[tuple[object,...]] = []
        for index,root in enumerate(roots):
            records.extend(scan_tree(root,index))
        return tuple(sorted(records,key=lambda row:(int(row[0]),str(row[1]).encode("utf-8"))))
    finally:
        for fd in roots:
            try:
                os.close(fd)
            except OSError:
                pass


def generated_inventory(root_fd: int, *, checked_in: bool) -> dict[str,os.stat_result]:
    try:
        names = sorted(os.listdir(root_fd),key=lambda value:value.encode("utf-8"))
    except (OSError,UnicodeError):
        reject("E_MISSING_ARTIFACT")
    entries: dict[str,os.stat_result] = {}
    for name in names:
        try:
            st = os.stat(name,dir_fd=root_fd,follow_symlinks=False)
        except OSError:
            reject("E_MISSING_ARTIFACT",name)
        if stat.S_ISLNK(st.st_mode):
            reject("E_SYMLINK",name)
        if stat.S_ISREG(st.st_mode) and st.st_nlink != 1:
            reject("E_HARDLINK",name)
        if name in DENIED_NAMES or name.endswith(DENIED_SUFFIXES):
            reject("E_CACHE_PRE",name)
        if stat.S_ISDIR(st.st_mode):
            reject("E_EXTRA_DIRECTORY",name)
        if not stat.S_ISREG(st.st_mode):
            reject("E_EXTRA_FILE",name)
        if st.st_nlink != 1:
            reject("E_HARDLINK",name)
        entries[name] = st
    allowed = set(GENERATED_BASENAMES)
    if checked_in:
        allowed.add("README.md")
    missing = set(GENERATED_BASENAMES) - set(entries)
    if "manifest.json" in missing:
        reject("E_MANIFEST_MISSING")
    if missing:
        reject("E_MISSING_ARTIFACT",min(missing))
    extras = set(entries) - allowed
    if extras:
        name = min(extras,key=lambda value:value.encode("utf-8"))
        reject("E_EXTRA_ARTIFACT" if name.endswith(".csv") else "E_EXTRA_FILE",name)
    return entries


def binding(path: str, digest: str) -> dict[str,str]:
    return {"path":path,"sha256":digest}


def bind_regular(package_fd: int, relative: str, token: str) -> dict[str,object]:
    data = read_regular_beneath(package_fd,relative,token)
    return {"path":relative,"bytes":len(data),"sha256":sha256_bytes(data)}


def expected_effective_block(version: int) -> tuple[bytes,...]:
    count = version + 1
    values = [f"[P15R-EFFECTIVE-DESIGN-AMENDMENTS v{version}]".encode("ascii"),f"count={count}".encode("ascii")]
    for index,(path,digest) in enumerate(EFFECTIVE_AMENDMENTS[:count],1):
        values.append(f"{index}.path={path}".encode("ascii"))
        values.append(f"{index}.sha256={digest}".encode("ascii"))
    values.append(b"[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]")
    return tuple(values)


def authenticate_effective_blocks(package_fd: int, review: bytes) -> None:
    if review.startswith(b"\xef\xbb\xbf") or b"\r" in review or b"\x00" in review or not review.endswith(b"\n"):
        reject("E_REVIEW_BINDING")
    lines = review.splitlines()
    expected_versions = tuple(range(1,13))
    expected_begins = tuple(f"[P15R-EFFECTIVE-DESIGN-AMENDMENTS v{version}]".encode("ascii") for version in expected_versions)
    begin_locations: list[int] = []
    end_locations: list[int] = []
    tag_pattern = re.compile(br"\[/?P15R-EFFECTIVE-DESIGN-AMENDMENTS(?: v[0-9]+)?\]")
    for index,line in enumerate(lines):
        if tag_pattern.fullmatch(line) is not None:
            if line == b"[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]":
                end_locations.append(index)
            elif line in expected_begins:
                begin_locations.append(index)
            else:
                reject("E_REVIEW_BINDING")
    if len(begin_locations) != len(expected_versions) or len(end_locations) != len(expected_versions):
        reject("E_REVIEW_BINDING")
    for version,(begin,end) in zip(expected_versions,zip(begin_locations,end_locations)):
        expected = expected_effective_block(version)
        if begin >= end or tuple(lines[begin:end+1]) != expected:
            reject("E_REVIEW_BINDING")
    for relative,digest in EFFECTIVE_AMENDMENTS:
        if sha256_bytes(read_regular_beneath(package_fd,relative,"E_REVIEW_BINDING")) != digest:
            reject("E_REVIEW_BINDING",relative.rsplit("/",1)[-1])


def authenticate_authority(package_fd: int, repository_fd: int) -> None:
    for relative,digest in AUTHORITY_BINDINGS:
        if sha256_bytes(read_regular_beneath(repository_fd,relative,"E_AUTHORITY_BINDING")) != digest:
            reject("E_AUTHORITY_BINDING",relative.rsplit("/",1)[-1])
    for relative,digest,token in (
        (DESIGN_LOCK[0],DESIGN_LOCK[1],"E_DESIGN_BINDING"),
        (DESIGN_REVIEW[0],DESIGN_REVIEW[1],"E_REVIEW_BINDING"),
        (IMPLEMENTATION_GATE[0],IMPLEMENTATION_GATE[1],"E_IMPLEMENTATION_GATE_BINDING"),
    ):
        data = read_regular_beneath(package_fd,relative,token)
        if sha256_bytes(data) != digest:
            reject(token,relative.rsplit("/",1)[-1])
        if relative == DESIGN_REVIEW[0]:
            authenticate_effective_blocks(package_fd,data)


def manifest_dag(manifest: Mapping[str,object]) -> tuple[tuple[str,...],tuple[tuple[str,str],...]]:
    """Reconstruct the lifecycle graph from serialized semantic blocks.

    The frozen schema has no free-standing ``dag`` key.  Its graph is the
    dependency relation of the blocks that are actually present in the
    canonical manifest.  In particular, this refuses to bless a constant
    graph when one of A/D/R/G/I/C/M is absent or malformed.  V is the
    deliberately future review successor and is represented only by M's
    terminal PASS together with the required absence of a backward
    ``result_review`` edge.
    """
    top_keys={"schema_version","package_id","authority_bindings","design_lock","design_review","implementation_gate","implementation","artifacts","aggregates","reproduction","proof_ceiling","status"}
    implementation=manifest.get("implementation"); artifacts=manifest.get("artifacts")
    implementation_valid=isinstance(implementation,list) and len(implementation)==6 and all(isinstance(item,dict) and set(item)=={"path","bytes","sha256"} and item.get("path")==path and type(item.get("bytes")) is int and item["bytes"]>=0 and re.fullmatch(r"[0-9a-f]{64}",str(item.get("sha256",""))) is not None for item,path in zip(implementation,IMPLEMENTATION_PATHS))
    artifact_valid=isinstance(artifacts,list) and len(artifacts)==8 and all(isinstance(item,dict) and set(item)=={"path","schema","columns","rows","negative_rows","mutation_classes","bytes","sha256"} and item.get("path")=="results/"+name and item.get("schema")==SCHEMA and item.get("columns")==len(HEADERS[name]) and item.get("rows")==ROW_COUNTS[name] and item.get("negative_rows")==NEGATIVE_COUNTS[name] and item.get("mutation_classes")==NEGATIVE_COUNTS[name] and type(item.get("bytes")) is int and item["bytes"]>=0 and re.fullmatch(r"[0-9a-f]{64}",str(item.get("sha256",""))) is not None for item,name in zip(artifacts,CSV_ARTIFACTS))
    structural = {
        "A": manifest.get("authority_bindings") == [binding(path,digest) for path,digest in AUTHORITY_BINDINGS],
        "D": manifest.get("design_lock") == binding(*DESIGN_LOCK),
        "R": manifest.get("design_review") == binding(*DESIGN_REVIEW),
        "G": manifest.get("implementation_gate") == binding(*IMPLEMENTATION_GATE),
        "I": implementation_valid,
        "C": artifact_valid,
        "M": set(manifest)==top_keys and manifest.get("schema_version")==MANIFEST_SCHEMA and manifest.get("package_id")==PACKAGE_ID and manifest.get("aggregates")==AGGREGATES and manifest.get("reproduction")=={"deterministic":True,"fresh_generations":2,"byte_identical_copies":3,"random_used":False,"network_used":False,"verify_only_read_only":True} and manifest.get("proof_ceiling")=={"finite_controls_prove_theorem":False,"universal_recover_p":"OPEN_NOT_AUTHORIZED","route_b_authorized":False} and manifest.get("status")=="PASS",
        "V": "result_review" not in manifest and "self_sha256" not in manifest,
    }
    nodes = tuple(node for node in DAG_NODES if structural.get(node) is True)
    edges = tuple((source,target) for source,target in DAG_EDGES if structural.get(source) is True and structural.get(target) is True)
    return nodes,edges


def validate_dag(manifest: Mapping[str,object]) -> None:
    nodes,edges = manifest_dag(manifest)
    if nodes != DAG_NODES or edges != DAG_EDGES:
        reject("E_DAG_CYCLE")
    if len(nodes) != 8 or len(set(nodes)) != 8 or len(edges) != 12 or len(set(edges)) != 12:
        reject("E_DAG_CYCLE")
    incoming = {node:0 for node in nodes}
    outgoing = {node:[] for node in nodes}
    for source,target in edges:
        if source not in incoming or target not in incoming or source == target:
            reject("E_DAG_CYCLE")
        incoming[target] += 1
        outgoing[source].append(target)
    ready = [node for node in DAG_NODES if incoming[node] == 0]
    order: list[str] = []
    while ready:
        if len(ready) != 1:
            reject("E_DAG_CYCLE")
        ready.sort(key=nodes.index)
        node = ready.pop(0)
        order.append(node)
        for target in outgoing[node]:
            incoming[target] -= 1
            if incoming[target] == 0:
                ready.append(target)
    if tuple(order) != nodes:
        reject("E_DAG_CYCLE")


def build_manifest(package_fd: int, artifacts: Mapping[str,bytes]) -> dict[str,object]:
    implementation = [bind_regular(package_fd,path,"E_IMPLEMENTATION_BINDING") for path in IMPLEMENTATION_PATHS]
    artifact_rows = []
    for name in CSV_ARTIFACTS:
        data = artifacts[name]
        artifact_rows.append({"path":"results/"+name,"schema":SCHEMA,"columns":len(HEADERS[name]),"rows":ROW_COUNTS[name],"negative_rows":NEGATIVE_COUNTS[name],"mutation_classes":NEGATIVE_COUNTS[name],"bytes":len(data),"sha256":sha256_bytes(data)})
    manifest = {
        "schema_version":MANIFEST_SCHEMA,
        "package_id":PACKAGE_ID,
        "authority_bindings":[binding(path,digest) for path,digest in AUTHORITY_BINDINGS],
        "design_lock":binding(*DESIGN_LOCK),
        "design_review":binding(*DESIGN_REVIEW),
        "implementation_gate":binding(*IMPLEMENTATION_GATE),
        "implementation":implementation,
        "artifacts":artifact_rows,
        "aggregates":dict(AGGREGATES),
        "reproduction":{"deterministic":True,"fresh_generations":2,"byte_identical_copies":3,"random_used":False,"network_used":False,"verify_only_read_only":True},
        "proof_ceiling":{"finite_controls_prove_theorem":False,"universal_recover_p":"OPEN_NOT_AUTHORIZED","route_b_authorized":False},
        "status":"PASS",
    }
    validate_dag(manifest)
    return manifest


def expected_artifacts(package_fd: int) -> tuple[dict[str,bytes],bytes]:
    tables = all_rows()
    artifacts = {name:csv_bytes(HEADERS[name],tables[name]) for name in CSV_ARTIFACTS}
    return artifacts,canonical_json(build_manifest(package_fd,artifacts))


def parse_csv_strict(name: str, data: bytes) -> tuple[list[str],list[dict[str,str]]]:
    if data.startswith(b"\xef\xbb\xbf") or b"\r" in data or b"\x00" in data or not data.endswith(b"\n") or data.endswith(b"\n\n"):
        reject("E_CANONICAL_BYTES",name)
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        reject("E_CANONICAL_BYTES",name)
    reader = csv.DictReader(io.StringIO(text,newline=""),delimiter=",",quotechar='"',doublequote=True,escapechar=None)
    header = reader.fieldnames or []
    if header != HEADERS[name]:
        reject("E_HEADER",name)
    rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        reject("E_WIDTH",name)
    if len(rows) != ROW_COUNTS[name]:
        reject("E_ROW_COUNT",name)
    expected_ids = [f"{ORDER_PREFIX[name]}-{index:03d}" for index in range(1,ROW_COUNTS[name]+1)]
    if [row["row_id"] for row in rows] != expected_ids:
        reject("E_ROW_ORDER",name)
    if csv_bytes(header,rows) != data:
        reject("E_CANONICAL_BYTES",name)
    return header,rows


def parse_manifest_strict(data: bytes) -> dict[str,object]:
    if data.startswith(b"\xef\xbb\xbf") or b"\r" in data or b"\x00" in data or not data.endswith(b"\n") or data.endswith(b"\n\n"):
        reject("E_CANONICAL_BYTES","manifest.json")
    try:
        value = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError,json.JSONDecodeError):
        reject("E_CANONICAL_BYTES","manifest.json")
    if not isinstance(value,dict) or canonical_json(value) != data:
        reject("E_CANONICAL_BYTES","manifest.json")
    ambient = {"ambient_absolute_path","ambient_timestamp","ambient_host","ambient_pid","ambient_temp_root"}
    if ambient.intersection(value):
        reject("E_NONCANONICAL_METADATA")
    if "self_sha256" in value or "result_review" in value:
        reject("E_MANIFEST_CYCLE" if "self_sha256" in value else "E_DAG_CYCLE")
    return value


def verify_manifest(package_fd: int, repository_fd: int, manifest: Mapping[str,object], csv_data: Mapping[str,bytes]) -> None:
    keys = {"schema_version","package_id","authority_bindings","design_lock","design_review","implementation_gate","implementation","artifacts","aggregates","reproduction","proof_ceiling","status"}
    if set(manifest) != keys:
        reject("E_MANIFEST_SEMANTICS")
    validate_dag(manifest)
    if manifest.get("authority_bindings") != [binding(path,digest) for path,digest in AUTHORITY_BINDINGS]:
        reject("E_AUTHORITY_BINDING")
    if manifest.get("design_lock") != binding(*DESIGN_LOCK):
        reject("E_DESIGN_BINDING")
    if manifest.get("design_review") != binding(*DESIGN_REVIEW):
        reject("E_REVIEW_BINDING")
    if manifest.get("implementation_gate") != binding(*IMPLEMENTATION_GATE):
        reject("E_IMPLEMENTATION_GATE_BINDING")
    authenticate_authority(package_fd,repository_fd)
    expected_implementation = [bind_regular(package_fd,path,"E_IMPLEMENTATION_BINDING") for path in IMPLEMENTATION_PATHS]
    if manifest.get("implementation") != expected_implementation:
        reject("E_IMPLEMENTATION_BINDING")
    expected = build_manifest(package_fd,csv_data)
    for key in ("schema_version","package_id","aggregates","reproduction","proof_ceiling","status"):
        if manifest.get(key) != expected[key]:
            reject("E_MANIFEST_SEMANTICS")
    observed_artifacts = manifest.get("artifacts")
    wanted_artifacts = expected["artifacts"]
    if not isinstance(observed_artifacts,list) or not isinstance(wanted_artifacts,list) or len(observed_artifacts) != 8:
        reject("E_MANIFEST_SEMANTICS")
    for observed,wanted in zip(observed_artifacts,wanted_artifacts):
        if not isinstance(observed,dict) or observed != wanted:
            semantic = {"path","schema","columns","rows","negative_rows","mutation_classes"}
            if isinstance(observed,dict) and {key:observed.get(key) for key in semantic} == {key:wanted.get(key) for key in semantic}:
                reject("E_ARTIFACT_SHA256")
            reject("E_MANIFEST_SEMANTICS")


def verify_semantics(parsed: Mapping[str,Sequence[Mapping[str,str]]]) -> None:
    expected = all_rows()
    observed_negative: list[tuple[str,str,str]] = []
    for name in CSV_ARTIFACTS:
        for observed,wanted in zip(parsed[name],expected[name]):
            if observed != wanted:
                row_id = observed.get("row_id","")
                reject(NEGATIVE_BY_ROW.get(row_id,("","","E_SEMANTIC"))[2],row_id)
            if observed.get("case_kind") == "NEGATIVE":
                observed_negative.append((observed.get("mutation_id",""),observed["row_id"],observed.get("negative_reason","")))
    wanted_negative = [(mutation,row,reason) for mutation,row,reason,_detector in SEMANTIC_REGISTRY]
    if observed_negative != wanted_negative:
        reject("E_MUTATION_REGISTRY")


def verify(input_argument: str) -> None:
    package_fd = os.open(".",OPEN_DIRECTORY)
    repository_fd = os.open("../..",OPEN_DIRECTORY)
    input_fd = open_argument_directory(input_argument)
    checked_fd = open_dir_beneath(package_fd,"results")
    pending: ControlFailure | None = None
    before: tuple[tuple[object,...], ...] = ()
    try:
        checked_identity = os.fstat(checked_fd)
        input_identity = os.fstat(input_fd)
        is_checked = (checked_identity.st_dev,checked_identity.st_ino) == (input_identity.st_dev,input_identity.st_ino)
        before = scope_receipt(package_fd,input_fd)
        generated_inventory(input_fd,checked_in=is_checked)
        raw: dict[str,bytes] = {}
        parsed: dict[str,list[dict[str,str]]] = {}
        for name in CSV_ARTIFACTS:
            raw[name] = read_regular_beneath(input_fd,name,"E_MISSING_ARTIFACT")
            _header,parsed[name] = parse_csv_strict(name,raw[name])
        manifest_data = read_regular_beneath(input_fd,"manifest.json","E_MANIFEST_MISSING")
        manifest = parse_manifest_strict(manifest_data)
        verify_manifest(package_fd,repository_fd,manifest,raw)
        verify_semantics(parsed)
        if manifest_data != canonical_json(build_manifest(package_fd,raw)):
            reject("E_MANIFEST_SEMANTICS")
    except ControlFailure as failure:
        pending = failure
    finally:
        try:
            after = scope_receipt(package_fd,input_fd)
            if before and before != after:
                pending = ControlFailure("E_VERIFY_ONLY_METADATA")
        finally:
            os.close(checked_fd)
            os.close(input_fd)
            os.close(repository_fd)
            os.close(package_fd)
    if pending is not None:
        raise pending


def validate_generation_capability(output_argument: str) -> int:
    expected_names = {"P15R_GENERATION_ROOT_FD","P15R_GENERATION_PURPOSE","P15R_GENERATION_UID","P15R_GENERATION_DEV","P15R_GENERATION_INO"}
    present_names = {name for name in os.environ if name.startswith("P15R_GENERATION_")}
    if present_names != expected_names or os.environ.get("P15R_GENERATION_ROOT_FD") != "9":
        reject("E_OUTPUT_CAPABILITY")
    purpose = os.environ["P15R_GENERATION_PURPOSE"]
    canonical = purpose in ("CANONICAL_A","CANONICAL_B")
    mutation = re.fullmatch(r"MUTATION_P(?:0[1-9]|1[0-9]|2[0-6])_V1|MUTATION_P27_V[1-5]|MUTATION_P28_V[1-2]",purpose) is not None
    if canonical:
        if os.environ.get("P15R_REPRO_ACTIVE") != "1" or "P15R_TEST_CONTEXT" in os.environ:
            reject("E_OUTPUT_CAPABILITY")
    elif mutation:
        if os.environ.get("P15R_TEST_CONTEXT") != "1":
            reject("E_OUTPUT_CAPABILITY")
    else:
        reject("E_OUTPUT_CAPABILITY")
    try:
        root_stat = os.fstat(9)
    except OSError:
        reject("E_OUTPUT_CAPABILITY")
    uid = decimal(os.environ["P15R_GENERATION_UID"])
    dev = decimal(os.environ["P15R_GENERATION_DEV"])
    ino = decimal(os.environ["P15R_GENERATION_INO"],nonzero=True)
    if not stat.S_ISDIR(root_stat.st_mode) or stat.S_IMODE(root_stat.st_mode) != 0o700 or root_stat.st_uid != os.getuid() or (root_stat.st_uid,root_stat.st_dev,root_stat.st_ino) != (uid,dev,ino):
        reject("E_OUTPUT_CAPABILITY")
    argument_fd = open_argument_directory(output_argument)
    try:
        argument_stat = os.fstat(argument_fd)
        if (argument_stat.st_dev,argument_stat.st_ino,argument_stat.st_uid,stat.S_IMODE(argument_stat.st_mode)) != (dev,ino,uid,0o700):
            reject("E_OUTPUT_CAPABILITY")
    finally:
        os.close(argument_fd)
    if os.listdir(9):
        reject("E_NONEMPTY_OUTPUT")
    return 9


def write_exclusive(root_fd: int, name: str, data: bytes) -> None:
    if name not in GENERATED_BASENAMES or "/" in name or name in (".",".."):
        reject("E_OUTPUT_CAPABILITY")
    try:
        fd = os.open(name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW|os.O_CLOEXEC,0o600,dir_fd=root_fd)
    except OSError:
        reject("E_GENERATION_WRITE",name)
    failure: OSError | None = None
    try:
        view = memoryview(data)
        while view:
            count = os.write(fd,view)
            if count <= 0:
                reject("E_GENERATION_WRITE",name)
            view = view[count:]
        os.fchmod(fd,0o444)
        os.fsync(fd)
    except OSError as error:
        failure = error
    finally:
        try:
            os.close(fd)
        except OSError as error:
            if failure is None:
                failure = error
    if failure is not None:
        reject("E_GENERATION_WRITE",name)


def generate(output_argument: str) -> None:
    root_fd = validate_generation_capability(output_argument)
    package_fd = os.open(".",OPEN_DIRECTORY)
    repository_fd = os.open("../..",OPEN_DIRECTORY)
    try:
        authenticate_authority(package_fd,repository_fd)
        artifacts,manifest = expected_artifacts(package_fd)
        for name in CSV_ARTIFACTS:
            write_exclusive(root_fd,name,artifacts[name])
        write_exclusive(root_fd,"manifest.json",manifest)
        os.fsync(root_fd)
    finally:
        os.close(repository_fd)
        os.close(package_fd)


def parse_cli(arguments: Sequence[str]) -> tuple[str,str]:
    if "--repair" in arguments:
        reject("E_VERIFY_ONLY_WRITE")
    if len(arguments) == 3 and arguments[0] == "--verify-only" and arguments[1] == "--input-dir" and arguments[2]:
        return "VERIFY",arguments[2]
    if len(arguments) == 3 and arguments[0] == "--generate" and arguments[1] == "--output-dir" and arguments[2]:
        return "GENERATE",arguments[2]
    reject("E_USAGE")
    raise AssertionError("unreachable")


def main(arguments: Sequence[str]) -> int:
    try:
        mode,directory = parse_cli(arguments)
        if mode == "VERIFY":
            verify(directory)
        else:
            generate(directory)
        return 0
    except ControlFailure as failure:
        detail = failure.detail if failure.detail and "/" not in failure.detail and "\n" not in failure.detail else ""
        print(failure.token + ((" "+detail) if detail else ""),file=sys.stderr)
        return 2 if failure.token in {"E_USAGE","E_VERIFY_ONLY_WRITE","E_OUTPUT_CAPABILITY"} else 1
    except (OSError,ValueError,UnicodeError,MemoryError):
        print("E_POSSESSION_UNAVAILABLE",file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
