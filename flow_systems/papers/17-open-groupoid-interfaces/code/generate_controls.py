#!/usr/bin/env python3
"""Generate or independently verify the frozen Paper-17 control package.

The command surface is deliberately closed.  This module uses only the Python
standard library, performs no network access, and never writes in verify-only
mode.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import stat
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Iterator, Mapping, Sequence


DESIGN_SCHEMA = "paper17-open-groupoid-controls/1"
MANIFEST_SCHEMA = "paper17-open-groupoid-controls-manifest/1"
PACKAGE_ID = "paper17-open-groupoid-controls"

RESULT_NAMES = (
    "range_first_handedness_controls.csv",
    "action_blind_open_records.csv",
    "connected_disconnected_firewall.csv",
    "domain_guard_controls.csv",
    "quantale_localic_firewall.csv",
    "actual_standard_owner_controls.csv",
    "dilation_strict_marker_controls.csv",
    "fixed_prime_provenance_controls.csv",
    "target_summary.csv",
    "manifest.json",
)

CSV_NAMES = RESULT_NAMES[:-1]

IMPLEMENTATION_PATHS = (
    "code/generate_controls.py",
    "code/test_controls.py",
    "code/README.md",
    "experiments/reproduce.sh",
    "experiments/README.md",
)

BINDINGS = (
    ("notes/phase2_control_design_gate.md", "093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647"),
    ("../9-packet-separation/paper/manuscript.tex", "24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb"),
    ("notes/phase2_control_design_lock.md", "abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa"),
    ("notes/phase2_control_design_review.md", "42d1389171a7c23ed40657ff979a2500a8b3daade2561af54755c0c1c4339326"),
    ("notes/phase2_control_implementation_gate.md", "aa73b08716e6064f93c1f760a9b91f16239ec204d4ea19a84cebf8d93833cf3e"),
)

PAPER9_BINDING = (
    "papers/9-packet-separation/paper/manuscript.tex@sha256:"
    "24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb"
)
GATE_C17_3 = "P17-P2-CONTROL-DESIGN-GATE-v1.0:C17-3"
GATE_C17_5 = "P17-P2-CONTROL-DESIGN-GATE-v1.0:C17-5"
GATE_C17_8 = "P17-P2-CONTROL-DESIGN-GATE-v1.0:C17-8"

HEADERS = {
    CSV_NAMES[0]: "schema_version,row_id,row_family,case_kind,group_token,object_x,h,object_y,k,sheet_a,subject_composable,subject_value,oracle_value,detected,negative_reason,oracle,status".split(","),
    CSV_NAMES[1]: "schema_version,row_id,row_family,case_kind,action_case,comparison_case,subset_u,subset_v,arrow_open,subject_value,oracle_value,record_equal,detected,negative_reason,oracle,status".split(","),
    CSV_NAMES[2]: "schema_version,row_id,row_family,case_kind,owner_domain,input_n,input_sheet,claim_token,subject_value,oracle_value,scope_token,source_binding,detected,negative_reason,oracle,status".split(","),
    CSV_NAMES[3]: "schema_version,row_id,row_family,case_kind,owner_domain,topology_token,claim_token,evidence_mode,subject_value,oracle_value,scope_token,detected,negative_reason,oracle,status".split(","),
    CSV_NAMES[4]: "schema_version,row_id,row_family,case_kind,owner_domain,bare_quantale_receipt,q_h_receipt,local_compactness_receipt,promotion_attempt,licensed,subject_value,oracle_value,source_binding,scope_token,detected,negative_reason,oracle,status".split(","),
    CSV_NAMES[5]: "schema_version,row_id,row_family,case_kind,packet_id,owner_token,topology_token,topos_token,quantale_token,base_frame_token,comparison_field,subject_value,oracle_value,detected,negative_reason,oracle,status".split(","),
    CSV_NAMES[6]: "schema_version,row_id,row_family,case_kind,L,L_prime,scale_c,r,t,u,claim_token,subject_value,oracle_value,inverse_value,scope_token,detected,negative_reason,oracle,status".split(","),
    CSV_NAMES[7]: "schema_version,row_id,row_family,case_kind,prime_token,generic_theorem_state,actual_topology_input,stabilizer_input,claim_token,subject_value,oracle_value,source_binding,scope_token,detected,negative_reason,oracle,status".split(","),
    CSV_NAMES[8]: "schema_version,row_id,artifact,expected_rows,expected_columns,expected_negative_rows,oracle_class,canonical_order_key,scope_token,artifact_order_index,status,notes".split(","),
}

EXPECTED = {
    CSV_NAMES[0]: (1662, 17, 36, "D3_RELATION_AND_LEFT_ACTION", "C17_1_FAMILY_ORDER"),
    CSV_NAMES[1]: (1520, 16, 0, "C4_BITSET_OPEN_QUANTALE", "C17_2_FAMILY_ORDER"),
    CSV_NAMES[2]: (19, 16, 4, "SOURCE_RECEIPT_PLUS_Z3_PERMUTATION", "C17_3_FAMILY_ORDER"),
    CSV_NAMES[3]: (25, 15, 10, "OWNER_DOMAIN_POLICY", "C17_4_FAMILY_ORDER"),
    CSV_NAMES[4]: (21, 18, 7, "BARE_Q_QH_LC_CONJUNCTION", "C17_5_FAMILY_ORDER"),
    CSV_NAMES[5]: (18, 17, 11, "CANONICAL_OWNER_PACKET_REGISTRY", "C17_6_FAMILY_ORDER"),
    CSV_NAMES[6]: (140, 19, 5, "INTEGER_CROSS_MULTIPLICATION_DILATION", "C17_7_FAMILY_ORDER"),
    CSV_NAMES[7]: (21, 17, 11, "P9_TWO_INPUT_POST_GENERIC_ALLOWLIST", "C17_8_FAMILY_ORDER"),
    CSV_NAMES[8]: (10, 12, 0, "RAW_COUNT_SCHEMA_INVENTORY", "TARGET_SUMMARY_ROW_ORDER"),
}

ORACLES = tuple(EXPECTED[name][3] for name in CSV_NAMES)
ROW_PREFIXES = ("GH", "AO", "CZ", "DG", "QL", "AS", "DM", "FP", "TS")
ROW_WIDTHS = (4, 4, 4, 4, 4, 4, 4, 4, 4)


class ControlError(Exception):
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_bytes(path: Path) -> bytes:
    return path.read_bytes()


def sha256_file(path: Path) -> str:
    return sha256_bytes(file_bytes(path))


def one_link_regular(path: Path, code: int = 5) -> os.stat_result:
    try:
        st = path.lstat()
    except FileNotFoundError as exc:
        raise ControlError(code, f"missing file: {path}") from exc
    if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1:
        raise ControlError(code, f"not a regular single-link file: {path}")
    return st


def root_from_script() -> Path:
    script = Path(__file__)
    if script.is_symlink():
        raise ControlError(5, "generator script may not be a symlink")
    root = script.resolve().parent.parent
    if root.is_symlink() or not root.is_dir():
        raise ControlError(5, "invalid Paper-17 root")
    return root


def row(header: Sequence[str], **values: str) -> dict[str, str]:
    unknown = set(values).difference(header)
    if unknown:
        raise AssertionError(f"unknown row fields: {sorted(unknown)}")
    result = {name: "" for name in header}
    result.update(values)
    result["schema_version"] = DESIGN_SCHEMA
    result["status"] = "PASS"
    return result


def mark_negative(values: dict[str, str], reason: str) -> dict[str, str]:
    values["case_kind"] = "NEGATIVE"
    values["detected"] = "true"
    values["negative_reason"] = reason
    return values


def bool_token(value: bool) -> str:
    return "true" if value else "false"


def set_token(values: Iterable[int]) -> str:
    members = sorted(set(values))
    return "EMPTY" if not members else "|".join(str(value) for value in members)


D3 = ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1))


def d3_token(value: tuple[int, int]) -> str:
    return f"d{value[0]}{value[1]}"


def x_token(value: tuple[int, int]) -> str:
    return f"x{value[0]}{value[1]}"


def s_token(value: tuple[int, int]) -> str:
    return f"s{value[0]}{value[1]}"


def d3_mul(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    i, j = left
    k, ell = right
    return ((i + (-1 if j else 1) * k) % 3, (j + ell) % 2)


def d3_inv(value: tuple[int, int]) -> tuple[int, int]:
    for candidate in D3:
        if d3_mul(value, candidate) == (0, 0) and d3_mul(candidate, value) == (0, 0):
            return candidate
    raise AssertionError("D3 inverse missing")


def arrow(x: tuple[int, int], h: tuple[int, int]) -> str:
    return f"a({x_token(x)};{d3_token(h)})"


def build_range_first() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[0]]
    rows: list[dict[str, str]] = []
    oracle = "D3_RELATION_AND_LEFT_ACTION"

    def add(family: str, kind: str = "DIAGNOSTIC", **values: str) -> None:
        values.update(row_family=family, case_kind=kind, group_token="D3", oracle=oracle)
        rows.append(row(header, **values))

    for x in D3:
        for h in D3:
            value = f"source={x_token(d3_mul(x, h))};range={x_token(x)}"
            add("ARROW", object_x=x_token(x), h=d3_token(h), subject_value=value, oracle_value=value)
    for x in D3:
        value = arrow(x, (0, 0))
        add("UNIT", object_x=x_token(x), subject_value=value, oracle_value=value)
    for x in D3:
        for h in D3:
            value = arrow(d3_mul(x, h), d3_inv(h))
            add("INVERSE", object_x=x_token(x), h=d3_token(h), subject_value=value, oracle_value=value)
    arrows = tuple((x, h) for x in D3 for h in D3)
    for x, h in arrows:
        for y, k in arrows:
            composable = y == d3_mul(x, h)
            value = arrow(x, d3_mul(h, k)) if composable else "NONCOMPOSABLE"
            add(
                "PAIR",
                object_x=x_token(x), h=d3_token(h), object_y=x_token(y), k=d3_token(k),
                subject_composable=bool_token(composable), subject_value=value, oracle_value=value,
            )
    for h in D3:
        for sheet in D3:
            value = s_token(d3_mul(h, sheet))
            add("SHEET_ACTION", h=d3_token(h), sheet_a=s_token(sheet), subject_value=value, oracle_value=value)
    for h in D3:
        for k in D3:
            for sheet in D3:
                value = s_token(d3_mul(d3_mul(h, k), sheet))
                add("SHEET_ASSOC", h=d3_token(h), k=d3_token(k), sheet_a=s_token(sheet), subject_value=value, oracle_value=value)
    noncommuting = tuple((h, k) for h in D3 for k in D3 if d3_mul(h, k) != d3_mul(k, h))
    for h, k in noncommuting:
        values = row(
            header, row_family="WRONG_PRODUCT_ORDER", case_kind="NEGATIVE", group_token="D3",
            object_x="x00", h=d3_token(h), object_y=x_token(h), k=d3_token(k),
            subject_composable="true", subject_value=arrow((0, 0), d3_mul(k, h)),
            oracle_value=arrow((0, 0), d3_mul(h, k)), detected="true",
            negative_reason="WRONG_GROUP_PRODUCT_ORDER", oracle=oracle,
        )
        rows.append(values)
    for h, k in noncommuting:
        rows.append(row(
            header, row_family="OPPOSITE_SHEET_ACTION", case_kind="NEGATIVE", group_token="D3",
            h=d3_token(h), k=d3_token(k), sheet_a="s00",
            subject_value=s_token(d3_mul(k, h)), oracle_value=s_token(d3_mul(h, k)),
            detected="true", negative_reason="OPPOSITE_SHEET_ACTION_HANDEDNESS", oracle=oracle,
        ))
    for index, record in enumerate(rows, 1):
        record["row_id"] = f"GH-{index:04d}"
    return rows


def c4_action(action: str, j: int, time: int) -> int:
    if action == "TRIVIAL":
        return j
    if action == "TRANSITIVE":
        return (j + time) % 4
    if action == "NONTRANSITIVE":
        return (j + 2 * (time % 2)) % 4
    raise AssertionError(action)


def subset_from_mask(mask: int) -> tuple[int, ...]:
    return tuple(value for value in range(4) if mask & (1 << value))


def explicit_open_descriptor(action: str, subset: Sequence[int]) -> str:
    arrows = tuple((j, t, c4_action(action, j, t)) for j in range(4) for t in subset)
    times = tuple(t for t in range(4) if any(a[1] == t for a in arrows))
    return f"X4x[{set_token(times)}]"


def explicit_inverse(action: str, subset: Sequence[int]) -> str:
    arrows = tuple((j, t, c4_action(action, j, t)) for j in range(4) for t in subset)
    inverse_times = tuple((-t) % 4 for _, t, _ in arrows)
    return set_token(inverse_times)


def explicit_product(action: str, left: Sequence[int], right: Sequence[int]) -> str:
    left_arrows = tuple((j, t, c4_action(action, j, t)) for j in range(4) for t in left)
    right_arrows = tuple((j, t, c4_action(action, j, t)) for j in range(4) for t in right)
    product_times = []
    for range_x, left_t, source_x in left_arrows:
        for right_range, right_t, _ in right_arrows:
            if right_range == source_x:
                product_times.append((left_t + right_t) % 4)
    return set_token(product_times)


def explicit_base(action: str, subset: Sequence[int]) -> str:
    descriptor = explicit_open_descriptor(action, subset)
    return bool_token(descriptor in ("X4x[EMPTY]", "X4x[0|1|2|3]"))


def build_action_blind() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[1]]
    rows: list[dict[str, str]] = []
    actions = ("TRIVIAL", "TRANSITIVE", "NONTRANSITIVE")
    oracle = "C4_BITSET_OPEN_QUANTALE"

    def add(family: str, action: str, u: int, v: int | None = None, comparison: str = "") -> None:
        U = subset_from_mask(u)
        V = subset_from_mask(v) if v is not None else ()
        effective = comparison or action
        if family.endswith("OPEN") or family == "OPEN_DESCRIPTOR":
            value = explicit_open_descriptor(effective, U)
            arrow_open = value
        elif family.endswith("INVOLUTION") or family == "INVOLUTION":
            value = explicit_inverse(effective, U)
            arrow_open = ""
        elif family.endswith("PRODUCT") or family == "PRODUCT":
            value = explicit_product(effective, U, V)
            arrow_open = ""
        elif family.endswith("BASE") or family == "BASE":
            value = explicit_base(effective, U)
            arrow_open = ""
        else:
            raise AssertionError(family)
        rows.append(row(
            header, row_family=family, case_kind="DIAGNOSTIC", action_case=action,
            comparison_case=comparison, subset_u=set_token(U),
            subset_v=set_token(V) if v is not None else "", arrow_open=arrow_open,
            subject_value=value, oracle_value=value,
            record_equal="true" if comparison else "", oracle=oracle,
        ))

    for family in ("OPEN_DESCRIPTOR", "INVOLUTION"):
        for action in actions:
            for u in range(16):
                add(family, action, u)
    for action in actions:
        for u in range(16):
            for v in range(16):
                add("PRODUCT", action, u, v)
    for action in actions:
        for u in range(16):
            add("BASE", action, u)
    for family in ("CROSS_OPEN", "CROSS_INVOLUTION"):
        for comparison in actions[1:]:
            for u in range(16):
                add(family, "TRIVIAL", u, comparison=comparison)
    for comparison in actions[1:]:
        for u in range(16):
            for v in range(16):
                add("CROSS_PRODUCT", "TRIVIAL", u, v, comparison)
    for comparison in actions[1:]:
        for u in range(16):
            add("CROSS_BASE", "TRIVIAL", u, comparison=comparison)
    for index, record in enumerate(rows, 1):
        record["row_id"] = f"AO-{index:04d}"
    return rows


def build_connected() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[2]]
    oracle = "SOURCE_RECEIPT_PLUS_Z3_PERMUTATION"
    rows: list[dict[str, str]] = []
    receipts = (
        ("CONNECTED_REAL_CONCLUSION", "B(G(X,R))~=Set"),
        ("FINITE_CONTROL_LIMIT", "NO_FINITE_PROOF_OF_CONNECTED_R_OR_TOPOS_EQUIVALENCE"),
        ("DISCONNECTED_FIREWALL", "DO_NOT_INFER_SET_FOR_ARBITRARY_DISCONNECTED_TIME"),
    )
    for claim, value in receipts:
        complete = f"{claim}={value}"
        rows.append(row(header, row_family="SYMBOLIC_RECEIPT", case_kind="RECEIPT",
                        owner_domain="ACTUAL_USUAL_R", claim_token=claim,
                        subject_value=complete, oracle_value=complete,
                        scope_token="SYMBOLIC_SOURCE_OWNED", source_binding=GATE_C17_3, oracle=oracle))
    for n in range(3):
        for sheet in range(3):
            value = f"z{(n + sheet) % 3}"
            rows.append(row(header, row_family="Z3_ACTION", case_kind="DIAGNOSTIC",
                            owner_domain="DISCRETE_Z_VIA_C3_QUOTIENT", input_n=str(n),
                            input_sheet=f"z{sheet}", subject_value=value, oracle_value=value,
                            scope_token="FINITE_Z3_FALSIFIER_ONLY", oracle=oracle))
    properties = ("GENERATOR_NONTRIVIAL", "REGULAR_QUOTIENT_TRANSITIVE", "NONTERMINAL_THREE_SHEETS")
    for claim in properties:
        complete = f"{claim}=true"
        rows.append(row(header, row_family="Z3_PROPERTY", case_kind="DIAGNOSTIC",
                        owner_domain="DISCRETE_Z_VIA_C3_QUOTIENT", claim_token=claim,
                        subject_value=complete, oracle_value=complete,
                        scope_token="FINITE_Z3_FALSIFIER_ONLY", oracle=oracle))
    attacks = (
        ("CERTIFY_CONNECTED_R", "FINITE_PROXY_PROVES_CONNECTED_R"),
        ("CERTIFY_TOPOS_EQUIVALENCE", "FINITE_PROXY_PROVES_TOPOS_EQUIVALENCE"),
        ("FORCE_SET_FOR_DISCONNECTED_TIME", "DISCONNECTED_TIME_FORCES_SET"),
        ("GENERALIZE_ALL_DISCONNECTED_H", "FINITE_PROXY_GENERALIZES_ALL_DISCONNECTED_H"),
    )
    for claim, reason in attacks:
        rows.append(row(header, row_family="PROMOTION_ATTACK", case_kind="NEGATIVE",
                        owner_domain="DISCRETE_Z_VIA_C3_QUOTIENT", claim_token=claim,
                        subject_value=f"CLAIM[{reason}]", oracle_value="REJECTED",
                        scope_token="FINITE_Z3_FALSIFIER_ONLY", detected="true",
                        negative_reason=reason, oracle=oracle))
    for index, record in enumerate(rows, 1):
        record["row_id"] = f"CZ-{index:04d}"
    return rows


DOMAIN_OWNERS = (
    ("ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "SYMBOLIC_SOURCE_RECEIPT_ONLY"),
    ("CONTROL_C3_DISCRETE", "FINITE_DISCRETE_C3", "FINITE_DIAGNOSTIC_ONLY"),
    ("CONTROL_C4_DISCRETE", "FINITE_DISCRETE_C4", "FINITE_DIAGNOSTIC_ONLY"),
)
DOMAIN_CLAIMS = ("OPEN_GROUPOID", "NONETALE", "NONUNITAL", "LOCALIC_RECONSTRUCTION")
DOMAIN_ATTACKS = (
    ("C3_PROXY_CERTIFIES_R_NONETALE", "ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "NONETALE", "FINITE_C3_PROXY"),
    ("C4_PROXY_CERTIFIES_R_NONETALE", "ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "NONETALE", "FINITE_C4_PROXY"),
    ("C3_PROXY_CERTIFIES_R_NONUNITAL", "ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "NONUNITAL", "FINITE_C3_PROXY"),
    ("C4_PROXY_CERTIFIES_R_NONUNITAL", "ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "NONUNITAL", "FINITE_C4_PROXY"),
    ("DISCRETE_SINGLETON_OPEN_IMPORTED_TO_R", "ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "OPEN_GROUPOID", "DISCRETE_SINGLETON_OPEN"),
    ("DISCRETE_LOCAL_CHART_IMPORTED_TO_R", "ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "OPEN_GROUPOID", "DISCRETE_LOCAL_CHART"),
    ("USUAL_R_RELABELLED_DISCRETE", "ACTUAL_USUAL_R", "FINITE_DISCRETE_C3", "OPEN_GROUPOID", "SYMBOLIC_SOURCE_RECEIPT_ONLY"),
    ("DISCRETE_PROXY_RELABELLED_USUAL_R", "CONTROL_C3_DISCRETE", "USUAL_NONDISCRETE_R", "OPEN_GROUPOID", "FINITE_DIAGNOSTIC_ONLY"),
    ("R_NONETALE_GENERALIZED_ALL_H", "ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "NONETALE_FOR_ALL_H", "SYMBOLIC_SOURCE_RECEIPT_ONLY"),
    ("R_NONUNITAL_GENERALIZED_ALL_H", "ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "NONUNITAL_FOR_ALL_H", "SYMBOLIC_SOURCE_RECEIPT_ONLY"),
)


def domain_policy(owner: str, claim: str) -> str:
    if owner == "ACTUAL_USUAL_R":
        return "SYMBOLIC_QH_GATE_ONLY" if claim == "LOCALIC_RECONSTRUCTION" else "SYMBOLIC_SOURCE_OWNED"
    if claim == "OPEN_GROUPOID":
        return "FINITE_DIAGNOSTIC_ONLY"
    if claim in ("NONETALE", "NONUNITAL"):
        return "FALSE_IN_DISCRETE_PROXY"
    return "NOT_CERTIFIABLE_BY_FINITE_PROXY"


def build_domain_guards() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[3]]
    oracle = "OWNER_DOMAIN_POLICY"
    rows: list[dict[str, str]] = []
    for owner, topology, evidence in DOMAIN_OWNERS:
        value = f"owner={owner};topology={topology};evidence={evidence}"
        scope = "SYMBOLIC_SOURCE_OWNED" if owner == "ACTUAL_USUAL_R" else "FINITE_DIAGNOSTIC_ONLY"
        rows.append(row(header, row_family="OWNER_RECEIPT", case_kind="RECEIPT",
                        owner_domain=owner, topology_token=topology, evidence_mode=evidence,
                        subject_value=value, oracle_value=value, scope_token=scope, oracle=oracle))
    for owner, topology, evidence in DOMAIN_OWNERS:
        for claim in DOMAIN_CLAIMS:
            scope = "SYMBOLIC_SOURCE_OWNED" if owner == "ACTUAL_USUAL_R" else "FINITE_DIAGNOSTIC_ONLY"
            rows.append(row(header, row_family="CLAIM_SCOPE", case_kind="RECEIPT",
                            owner_domain=owner, topology_token=topology, claim_token=claim,
                            evidence_mode=evidence, subject_value=f"{claim}=true",
                            oracle_value=domain_policy(owner, claim), scope_token=scope, oracle=oracle))
    for reason, owner, topology, claim, evidence in DOMAIN_ATTACKS:
        rows.append(row(header, row_family="WRONG_DOMAIN_ATTACK", case_kind="NEGATIVE",
                        owner_domain=owner, topology_token=topology, claim_token=claim,
                        evidence_mode=evidence, subject_value=f"CLAIM[{reason}]",
                        oracle_value="REJECTED", scope_token="NO_REAL_OR_LOCALIC_CERTIFICATION",
                        detected="true", negative_reason=reason, oracle=oracle))
    for index, record in enumerate(rows, 1):
        record["row_id"] = f"DG-{index:04d}"
    return rows


QL_REASONS = (
    "LOCALIC_WITHOUT_BARE_QH_LC",
    "LOCALIC_WITH_ONLY_LC",
    "LOCALIC_WITH_ONLY_QH",
    "LOCALIC_WITHOUT_BARE_QUANTALE",
    "BARE_QUANTALE_ALONE_PROMOTED",
    "BARE_QUANTALE_LC_WITHOUT_QH",
    "BARE_QUANTALE_QH_WITHOUT_LC",
)


def build_quantale() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[4]]
    oracle = "BARE_Q_QH_LC_CONJUNCTION"
    rows: list[dict[str, str]] = []
    receipts = (
        ("BARE_QUANTALE", "bare_quantale_receipt", "BARE_QUANTALE=O(G)~=O(H)_DIRECT"),
        ("Q_H_COMPARISON", "q_h_receipt", "Q_H_COMPARISON=q_H_REQUIRED_SEPARATELY"),
        ("LOCAL_COMPACTNESS", "local_compactness_receipt", "LOCAL_COMPACTNESS=SOURCE_DOMAIN_REQUIRED_SEPARATELY"),
    )
    for _, field, value in receipts:
        values = dict(row_family="SOURCE_RECEIPT", case_kind="RECEIPT", owner_domain="GENERIC_H",
                      subject_value=value, oracle_value=value, source_binding=GATE_C17_5,
                      scope_token="SYMBOLIC_SOURCE_RECEIPT_ONLY", oracle=oracle)
        values[field] = "true"
        rows.append(row(header, **values))
    bit_triples = tuple(f"{value:03b}" for value in range(8))
    for bits in bit_triples:
        licensed = bits == "111"
        rows.append(row(header, row_family="GATE_TRUTH_TABLE", case_kind="DIAGNOSTIC",
                        bare_quantale_receipt=bool_token(bits[0] == "1"),
                        q_h_receipt=bool_token(bits[1] == "1"),
                        local_compactness_receipt=bool_token(bits[2] == "1"),
                        promotion_attempt="false", licensed=bool_token(licensed),
                        subject_value=bool_token(licensed), oracle_value=bool_token(licensed),
                        scope_token="NO_REAL_OR_LOCALIC_CERTIFICATION", oracle=oracle))
    for bits, reason in zip(bit_triples[:-1], QL_REASONS):
        rows.append(row(header, row_family="PROMOTION_ATTACK", case_kind="NEGATIVE",
                        bare_quantale_receipt=bool_token(bits[0] == "1"),
                        q_h_receipt=bool_token(bits[1] == "1"),
                        local_compactness_receipt=bool_token(bits[2] == "1"),
                        promotion_attempt="true", licensed="false",
                        subject_value=f"CLAIM[{reason}]", oracle_value="REJECTED",
                        scope_token="NO_REAL_OR_LOCALIC_CERTIFICATION", detected="true",
                        negative_reason=reason, oracle=oracle))
    owner_rows = (
        ("ACTUAL_USUAL_R", True, True, True, "SYMBOLIC_SOURCE_THEOREM_ONLY", "SYMBOLIC_SOURCE_OWNED"),
        ("CONTROL_Z_DISCRETE", True, True, True, "SYMBOLIC_SOURCE_THEOREM_ONLY", "SYMBOLIC_SOURCE_OWNED"),
        ("ARBITRARY_TOPOLOGICAL_H", True, False, False, "BARE_ONLY_NO_RECONSTRUCTION", "NO_REAL_OR_LOCALIC_CERTIFICATION"),
    )
    for owner, bare, qh, lc, value, scope in owner_rows:
        licensed = bare and qh and lc
        rows.append(row(header, row_family="OWNER_SCOPE", case_kind="RECEIPT", owner_domain=owner,
                        bare_quantale_receipt=bool_token(bare), q_h_receipt=bool_token(qh),
                        local_compactness_receipt=bool_token(lc), promotion_attempt="false",
                        licensed=bool_token(licensed), subject_value=value, oracle_value=value,
                        source_binding=GATE_C17_5, scope_token=scope, oracle=oracle))
    for index, record in enumerate(rows, 1):
        record["row_id"] = f"QL-{index:04d}"
    return rows


PACKETS = {
    "ACTUAL": ("ACTUAL_INDISCRETE_ORBIT", "INDISCRETE", "Set", "O(R)", "2"),
    "STANDARD": ("STANDARD_CIRCLE", "STANDARD_CIRCLE", "BZ", "O(S_LxR)", "O(S_L)"),
}
PACKET_FIELDS = ("owner", "topology", "topos", "quantale", "base")
PACKET_COLUMNS = ("owner_token", "topology_token", "topos_token", "quantale_token", "base_frame_token")
SPLICE_REASONS = (
    "ACTUAL_PACKET_OWNER_RELABELLED_STANDARD", "STANDARD_TOPOLOGY_IMPORTED_ACTUAL",
    "STANDARD_TOPOS_SPLICED_ACTUAL", "STANDARD_QUANTALE_SPLICED_ACTUAL",
    "STANDARD_BASE_SPLICED_ACTUAL", "STANDARD_PACKET_OWNER_RELABELLED_ACTUAL",
    "INDISCRETE_TOPOLOGY_IMPORTED_STANDARD", "ACTUAL_TOPOS_SPLICED_STANDARD",
    "ACTUAL_QUANTALE_SPLICED_STANDARD", "ACTUAL_BASE_SPLICED_STANDARD",
    "ACTUAL_STANDARD_BASES_IDENTIFIED",
)


def packet_value(values: Sequence[str]) -> str:
    return ";".join(f"{key}={value}" for key, value in zip(PACKET_FIELDS, values))


def build_owner_packets() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[5]]
    oracle = "CANONICAL_OWNER_PACKET_REGISTRY"
    rows: list[dict[str, str]] = []
    for packet in ("ACTUAL", "STANDARD"):
        values = PACKETS[packet]
        fields = dict(zip(PACKET_COLUMNS, values))
        complete = packet_value(values)
        rows.append(row(header, row_family="OWNER_RECORD", case_kind="RECEIPT",
                        packet_id=packet, subject_value=complete, oracle_value=complete,
                        oracle=oracle, **fields))
    for index, field in enumerate(PACKET_FIELDS):
        value = f"{field}:{PACKETS['ACTUAL'][index]}|{PACKETS['STANDARD'][index]}"
        rows.append(row(header, row_family="FIELD_COMPARISON", case_kind="RECEIPT",
                        packet_id="CROSS_PACKET", comparison_field=field,
                        subject_value=value, oracle_value=value, oracle=oracle))
    for offset in range(5):
        mutated = list(PACKETS["ACTUAL"])
        mutated[offset] = PACKETS["STANDARD"][offset]
        reason = SPLICE_REASONS[offset]
        rows.append(row(header, row_family="OWNER_SPLICE_ATTACK", case_kind="NEGATIVE",
                        packet_id="ACTUAL", comparison_field=PACKET_FIELDS[offset],
                        subject_value=packet_value(mutated), oracle_value=packet_value(PACKETS["ACTUAL"]),
                        detected="true", negative_reason=reason, oracle=oracle,
                        **dict(zip(PACKET_COLUMNS, mutated))))
    for offset in range(5):
        mutated = list(PACKETS["STANDARD"])
        mutated[offset] = PACKETS["ACTUAL"][offset]
        reason = SPLICE_REASONS[5 + offset]
        rows.append(row(header, row_family="OWNER_SPLICE_ATTACK", case_kind="NEGATIVE",
                        packet_id="STANDARD", comparison_field=PACKET_FIELDS[offset],
                        subject_value=packet_value(mutated), oracle_value=packet_value(PACKETS["STANDARD"]),
                        detected="true", negative_reason=reason, oracle=oracle,
                        **dict(zip(PACKET_COLUMNS, mutated))))
    rows.append(row(header, row_family="OWNER_SPLICE_ATTACK", case_kind="NEGATIVE",
                    packet_id="CROSS_PACKET", comparison_field="base",
                    subject_value="base_relation=EQUAL", oracle_value="base_relation=DISTINCT",
                    detected="true", negative_reason=SPLICE_REASONS[-1], oracle=oracle))
    for index, record in enumerate(rows, 1):
        record["row_id"] = f"AS-{index:04d}"
    return rows


def frac(value: Fraction | int | str) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def frac_token(value: Fraction | int | str) -> str:
    value = frac(value)
    return f"{value.numerator}/{value.denominator}"


def mod_fraction(value: Fraction, modulus: Fraction) -> Fraction:
    quotient = value // modulus
    return value - quotient * modulus


def q_token(value: Fraction, modulus: Fraction) -> str:
    return f"q({frac_token(mod_fraction(value, modulus))}mod{frac_token(modulus)})"


def g_token(r: Fraction, modulus: Fraction, time: Fraction) -> str:
    return f"g({q_token(r, modulus)};{frac_token(time)})"


def build_dilation() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[6]]
    oracle = "INTEGER_CROSS_MULTIPLICATION_DILATION"
    rows: list[dict[str, str]] = []
    receipts = ("UNMARKED_DILATION_ALGEBRA_ONLY", "STRICT_MARKER_EXTRA_STRUCTURE")
    for claim in receipts:
        rows.append(row(header, row_family="SYMBOLIC_RECEIPT", case_kind="RECEIPT",
                        claim_token=claim, subject_value=claim, oracle_value=claim,
                        scope_token="SYMBOLIC_SOURCE_RECEIPT_ONLY", oracle=oracle))
    L, Lp, c = Fraction(2), Fraction(3), Fraction(3, 2)
    r_values = tuple(map(Fraction, (0, Fraction(1, 2), 1, Fraction(3, 2))))
    times = tuple(map(Fraction, (-1, 0, 1, 2)))
    common = {"L": frac_token(L), "L_prime": frac_token(Lp), "scale_c": frac_token(c)}
    for r_value in r_values:
        forward = q_token(c * r_value, Lp)
        inverse = q_token((Fraction(1, 1) / c) * mod_fraction(c * r_value, Lp), L)
        rows.append(row(header, row_family="OBJECT_MAP", case_kind="DIAGNOSTIC", r=frac_token(r_value),
                        subject_value=forward, oracle_value=forward, inverse_value=inverse,
                        scope_token="ALGEBRAIC_RATIONAL_FIXTURE_ONLY", oracle=oracle, **common))
    for r_value in r_values:
        for time in times:
            forward = g_token(c * r_value, Lp, c * time)
            inverse = g_token((Fraction(1, 1) / c) * mod_fraction(c * r_value, Lp), L, time)
            rows.append(row(header, row_family="ARROW_MAP", case_kind="DIAGNOSTIC",
                            r=frac_token(r_value), t=frac_token(time), subject_value=forward,
                            oracle_value=forward, inverse_value=inverse,
                            scope_token="ALGEBRAIC_RATIONAL_FIXTURE_ONLY", oracle=oracle, **common))
    for family in ("SOURCE_COMPAT", "RANGE_COMPAT", "INVERSE_COMPAT"):
        for r_value in r_values:
            for time in times:
                if family == "SOURCE_COMPAT":
                    value = q_token(c * (r_value + time), Lp)
                elif family == "RANGE_COMPAT":
                    value = q_token(c * r_value, Lp)
                else:
                    value = g_token(c * (r_value + time), Lp, -c * time)
                rows.append(row(header, row_family=family, case_kind="DIAGNOSTIC",
                                r=frac_token(r_value), t=frac_token(time), subject_value=value,
                                oracle_value=value, scope_token="ALGEBRAIC_RATIONAL_FIXTURE_ONLY",
                                oracle=oracle, **common))
    for r_value in r_values:
        for time in times:
            for u_value in times:
                value = g_token(c * r_value, Lp, c * (time + u_value))
                rows.append(row(header, row_family="PRODUCT_COMPAT", case_kind="DIAGNOSTIC",
                                r=frac_token(r_value), t=frac_token(time), u=frac_token(u_value),
                                subject_value=value, oracle_value=value,
                                scope_token="ALGEBRAIC_RATIONAL_FIXTURE_ONLY", oracle=oracle, **common))
    strict_scales = (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2))
    for scale in strict_scales:
        accepted = scale == 1
        values = row(header, row_family="STRICT_MARKER",
                     case_kind="DIAGNOSTIC" if accepted else "NEGATIVE", L="2/1",
                     L_prime=frac_token(scale * 2), scale_c=frac_token(scale),
                     claim_token="STRICT_TIME_MARKER", subject_value="strict_marker_preserved=true",
                     oracle_value="strict_marker_preserved=true" if accepted else "REJECTED",
                     scope_token="ALGEBRAIC_RATIONAL_FIXTURE_ONLY",
                     detected="" if accepted else "true",
                     negative_reason="" if accepted else "STRICT_MARKER_NONUNIT_SCALE", oracle=oracle)
        rows.append(values)
    for claim, reason in (
        ("PLAIN_TOPOS_RECOVERS_L", "PLAIN_TOPOS_NUMERICAL_SCALE_PROMOTION"),
        ("PLAIN_QUANTALE_RECOVERS_L", "PLAIN_QUANTALE_NUMERICAL_SCALE_PROMOTION"),
    ):
        rows.append(row(header, row_family="PLAIN_SCALE_PROMOTION", case_kind="NEGATIVE",
                        L="2/1", L_prime="3/1", scale_c="3/2", claim_token=claim,
                        subject_value=f"CLAIM[{reason}]", oracle_value="REJECTED",
                        scope_token="NO_REAL_OR_LOCALIC_CERTIFICATION", detected="true",
                        negative_reason=reason, oracle=oracle))
    for index, record in enumerate(rows, 1):
        record["row_id"] = f"DM-{index:04d}"
    return rows


FP_REASONS = (
    "C_STAR_PROMOTION", "HAAR_PROMOTION", "MEASURE_PROMOTION", "TRACE_PROMOTION",
    "DETERMINANT_PROMOTION", "ROUTE_B_PROMOTION", "PRIORITY_PROMOTION",
    "STANDARD_TOPOLOGY_PROMOTION", "NUMERICAL_LOG_EVALUATION",
    "FIXED_PRIME_SUBSTITUTION_BEFORE_GENERIC", "NONLITERAL_STABILIZER_REWRITE",
)
FP_CLAIMS = ("C_STAR", "HAAR", "MEASURE", "TRACE", "DETERMINANT", "ROUTE_B", "PRIORITY")
GENERIC_STATE = "PROVED_UPSTREAM_BEFORE_SUBSTITUTION"


def fp_complete(prime: str, topology: str, stabilizer: str) -> str:
    return f"prime={prime};topology={topology};stabilizer={stabilizer}"


def build_fixed_prime() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[7]]
    oracle = "P9_TWO_INPUT_POST_GENERIC_ALLOWLIST"
    rows: list[dict[str, str]] = []
    receipt = f"generic_theorem_state={GENERIC_STATE}"
    rows.append(row(header, row_family="GENERIC_PRECONDITION", case_kind="RECEIPT",
                    generic_theorem_state=GENERIC_STATE, claim_token="GENERIC_PRECONDITION",
                    subject_value=receipt, oracle_value=receipt, source_binding=GATE_C17_8,
                    scope_token="SYMBOLIC_SOURCE_RECEIPT_ONLY", oracle=oracle))
    for prime in ("2", "3", "5"):
        stabilizer = f"(log {prime})Z"
        value = fp_complete(prime, "INDISCRETE_FROM_PAPER9", stabilizer)
        rows.append(row(header, row_family="FIXED_PRIME_SUBSTITUTION", case_kind="RECEIPT",
                        prime_token=prime, generic_theorem_state=GENERIC_STATE,
                        actual_topology_input="INDISCRETE_FROM_PAPER9", stabilizer_input=stabilizer,
                        claim_token="FIXED_PRIME_SUBSTITUTION", subject_value=value, oracle_value=value,
                        source_binding=PAPER9_BINDING, scope_token="FIXED_PRIME_SUBSTITUTION_ONLY", oracle=oracle))
    for prime in ("2", "3", "5"):
        stabilizer = f"(log {prime})Z"
        for claim, value in (("INDISCRETENESS", "INDISCRETE_FROM_PAPER9"),
                             ("LITERAL_STABILIZER", stabilizer)):
            rows.append(row(header, row_family="ALLOWED_P9_INPUT", case_kind="RECEIPT",
                            prime_token=prime, generic_theorem_state=GENERIC_STATE,
                            actual_topology_input="INDISCRETE_FROM_PAPER9", stabilizer_input=stabilizer,
                            claim_token=claim, subject_value=value, oracle_value=value,
                            source_binding=PAPER9_BINDING, scope_token="FIXED_PRIME_SUBSTITUTION_ONLY", oracle=oracle))
    for offset, reason in enumerate(FP_REASONS):
        claim = "FIXED_PRIME_SUBSTITUTION"
        topology = "INDISCRETE_FROM_PAPER9"
        stabilizer = "(log 2)Z"
        generic = GENERIC_STATE
        if offset < 7:
            claim = FP_CLAIMS[offset]
        elif reason == "STANDARD_TOPOLOGY_PROMOTION":
            topology = "STANDARD_CIRCLE"
        elif reason == "NUMERICAL_LOG_EVALUATION":
            stabilizer = "NUMERICAL_LOG_2"
        elif reason == "FIXED_PRIME_SUBSTITUTION_BEFORE_GENERIC":
            generic = "NOT_PROVED_UPSTREAM_BEFORE_SUBSTITUTION"
        elif reason == "NONLITERAL_STABILIZER_REWRITE":
            stabilizer = "LOG_2_Z_EQUIVALENT_REWRITE"
        rows.append(row(header, row_family="PROVENANCE_PROMOTION_ATTACK", case_kind="NEGATIVE",
                        prime_token="2", generic_theorem_state=generic,
                        actual_topology_input=topology, stabilizer_input=stabilizer,
                        claim_token=claim, subject_value=f"CLAIM[{reason}]", oracle_value="REJECTED",
                        source_binding=PAPER9_BINDING, scope_token="FIXED_PRIME_SUBSTITUTION_ONLY",
                        detected="true", negative_reason=reason, oracle=oracle))
    for index, record in enumerate(rows, 1):
        record["row_id"] = f"FP-{index:04d}"
    return rows


def build_summary() -> list[dict[str, str]]:
    header = HEADERS[CSV_NAMES[8]]
    rows: list[dict[str, str]] = []
    for index, name in enumerate(CSV_NAMES, 1):
        expected_rows, columns, negatives, oracle, order = EXPECTED[name]
        rows.append(row(header, row_id=f"TS-{index:04d}", artifact=f"results/{name}",
                        expected_rows=str(expected_rows), expected_columns=str(columns),
                        expected_negative_rows=str(negatives), oracle_class=oracle,
                        canonical_order_key=order, scope_token="COUNT_AND_SERIALIZATION_ONLY",
                        artifact_order_index=str(index), notes=""))
    rows.append(row(header, row_id="TS-0010", artifact="PACKAGE_TOTAL", expected_rows="3436",
                    expected_columns="MIXED", expected_negative_rows="84",
                    oracle_class="RAW_COUNT_SCHEMA_INVENTORY",
                    canonical_order_key="SECTION_2_ARTIFACT_ORDER",
                    scope_token="COUNT_AND_SERIALIZATION_ONLY", artifact_order_index="PACKAGE",
                    notes="CSV_ARTIFACTS=9;GENERATED_ARTIFACTS=10"))
    return rows


BUILDERS = (
    build_range_first,
    build_action_blind,
    build_connected,
    build_domain_guards,
    build_quantale,
    build_owner_packets,
    build_dilation,
    build_fixed_prime,
    build_summary,
)


def csv_bytes(header: Sequence[str], records: Sequence[Mapping[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=header, delimiter=",", quotechar='"',
                            quoting=csv.QUOTE_MINIMAL, doublequote=True, escapechar=None,
                            lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows(records)
    return stream.getvalue().encode("utf-8")


def binding_path(root: Path, logical: str) -> Path:
    return root / logical


def metadata(path: Path, logical: str) -> dict[str, object]:
    data = file_bytes(path)
    return {"path": logical, "bytes": len(data), "sha256": sha256_bytes(data)}


def build_manifest(root: Path, csv_payloads: Mapping[str, bytes]) -> dict[str, object]:
    bindings = []
    for logical, expected_hash in BINDINGS:
        path = binding_path(root, logical)
        one_link_regular(path, 6)
        data = file_bytes(path)
        if sha256_bytes(data) != expected_hash:
            raise ControlError(6, f"authority digest drift: {logical}")
        bindings.append({"path": logical, "bytes": len(data), "sha256": expected_hash})
    implementation = []
    for logical in IMPLEMENTATION_PATHS:
        path = root / logical
        one_link_regular(path, 6)
        implementation.append(metadata(path, logical))
    artifacts = []
    for name in CSV_NAMES:
        data = csv_payloads[name]
        expected_rows, columns, negatives, _, _ = EXPECTED[name]
        artifacts.append({
            "path": f"results/{name}", "schema": DESIGN_SCHEMA, "columns": columns,
            "rows": expected_rows, "negative_rows": negatives,
            "bytes": len(data), "sha256": sha256_bytes(data),
        })
    return {
        "schema_version": MANIFEST_SCHEMA,
        "package_id": PACKAGE_ID,
        "bindings": bindings,
        "acyclic_policy": {
            "manifest_self_hash_included": False,
            "manifest_self_entry_included": False,
            "p17_proof_hash_included": False,
            "p17_proof_review_hash_included": False,
            "authority_policy": "CONTROL_DESIGN_GATE_INDIRECT_PROOF_AUTHORITY",
        },
        "implementation": implementation,
        "artifacts": artifacts,
        "aggregates": {
            "csv_artifacts": 9,
            "generated_artifacts_including_manifest": 10,
            "csv_body_rows": 3436,
            "nonnegative_csv_rows": 3352,
            "explicit_negative_rows": 84,
            "expected_negatives_detected": 84,
            "semantic_mutation_classes": 48,
            "package_mutation_classes": 42,
            "isolated_mutation_methods": 90,
            "unittest_methods": 180,
        },
        "reproduction": {
            "deterministic": True,
            "random_used": False,
            "network_used": False,
            "ambient_clock_used": False,
            "fresh_generations": 2,
            "byte_identical_copies": 3,
            "verify_only_rewrites": False,
        },
        "status": "PASS",
    }


def scan_closed_residue(root: Path, allow_owned_lock: bool) -> None:
    lock = root / "experiments/.p17-control-reproduce.lock"
    for directory, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        base = Path(directory)
        for name in tuple(dirnames) + tuple(filenames):
            path = base / name
            if allow_owned_lock and path == lock:
                continue
            if name in {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}:
                raise ControlError(5, f"cache residue: {path}")
            if name.endswith((".pyc", ".pyo")):
                raise ControlError(5, f"bytecode residue: {path}")
            if name.startswith(".p17-control-"):
                raise ControlError(5, f"task residue: {path}")


def exact_result_inventory(output: Path) -> None:
    try:
        entries = list(output.iterdir())
    except FileNotFoundError as exc:
        raise ControlError(5, "missing output directory") from exc
    if {entry.name for entry in entries} != set(RESULT_NAMES) or len(entries) != len(RESULT_NAMES):
        raise ControlError(5, "generated-result inventory drift")
    for name in RESULT_NAMES:
        one_link_regular(output / name, 5)


def parse_csv_strict(path: Path, expected_header: Sequence[str]) -> tuple[bytes, list[dict[str, str]]]:
    data = file_bytes(path)
    if data.startswith(b"\xef\xbb\xbf") or not data.endswith(b"\n") or b"\r" in data:
        raise ControlError(7, f"noncanonical CSV bytes: {path.name}")
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise ControlError(7, f"non-UTF8 CSV: {path.name}") from exc
    try:
        parsed = list(csv.reader(io.StringIO(text, newline=""), strict=True))
    except csv.Error as exc:
        raise ControlError(7, f"CSV parse failure: {path.name}") from exc
    if not parsed or parsed[0] != list(expected_header):
        raise ControlError(7, f"CSV header mismatch: {path.name}")
    if any(len(items) != len(expected_header) for items in parsed[1:]):
        raise ControlError(7, f"CSV width mismatch: {path.name}")
    records = [dict(zip(expected_header, items)) for items in parsed[1:]]
    return data, records


def permutation(value: tuple[int, int]) -> tuple[int, int, int]:
    r = (1, 2, 0)
    s = (0, 2, 1)

    def compose(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(left[right[index]] for index in range(3))

    def power(base: tuple[int, int, int], exponent: int) -> tuple[int, int, int]:
        result = (0, 1, 2)
        for _ in range(exponent):
            result = compose(base, result)
        return result

    return compose(power(r, value[0]), power(s, value[1]))


PERM_TO_D3 = {permutation(value): value for value in D3}


def perm_mul(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    p, q = permutation(left), permutation(right)
    composed = tuple(p[q[index]] for index in range(3))
    return PERM_TO_D3[composed]


def expected_families() -> tuple[tuple[tuple[str, int], ...], ...]:
    return (
        (("ARROW", 36), ("UNIT", 6), ("INVERSE", 36), ("PAIR", 1296),
         ("SHEET_ACTION", 36), ("SHEET_ASSOC", 216), ("WRONG_PRODUCT_ORDER", 18),
         ("OPPOSITE_SHEET_ACTION", 18)),
        (("OPEN_DESCRIPTOR", 48), ("INVOLUTION", 48), ("PRODUCT", 768), ("BASE", 48),
         ("CROSS_OPEN", 32), ("CROSS_INVOLUTION", 32), ("CROSS_PRODUCT", 512), ("CROSS_BASE", 32)),
        (("SYMBOLIC_RECEIPT", 3), ("Z3_ACTION", 9), ("Z3_PROPERTY", 3), ("PROMOTION_ATTACK", 4)),
        (("OWNER_RECEIPT", 3), ("CLAIM_SCOPE", 12), ("WRONG_DOMAIN_ATTACK", 10)),
        (("SOURCE_RECEIPT", 3), ("GATE_TRUTH_TABLE", 8), ("PROMOTION_ATTACK", 7), ("OWNER_SCOPE", 3)),
        (("OWNER_RECORD", 2), ("FIELD_COMPARISON", 5), ("OWNER_SPLICE_ATTACK", 11)),
        (("SYMBOLIC_RECEIPT", 2), ("OBJECT_MAP", 4), ("ARROW_MAP", 16),
         ("SOURCE_COMPAT", 16), ("RANGE_COMPAT", 16), ("INVERSE_COMPAT", 16),
         ("PRODUCT_COMPAT", 64), ("STRICT_MARKER", 4), ("PLAIN_SCALE_PROMOTION", 2)),
        (("GENERIC_PRECONDITION", 1), ("FIXED_PRIME_SUBSTITUTION", 3),
         ("ALLOWED_P9_INPUT", 6), ("PROVENANCE_PROMOTION_ATTACK", 11)),
        (),
    )


def validate_common(name: str, records: Sequence[Mapping[str, str]], index: int) -> None:
    expected_rows, _, negatives, oracle, _ = EXPECTED[name]
    if len(records) != expected_rows:
        raise ControlError(7, f"row-count mismatch: {name}")
    prefix = ROW_PREFIXES[index]
    for position, record in enumerate(records, 1):
        if record.get("schema_version") != DESIGN_SCHEMA:
            raise ControlError(7, f"schema mismatch: {name}")
        if record.get("row_id") != f"{prefix}-{position:04d}":
            raise ControlError(7, f"row identity/order mismatch: {name}")
        if record.get("status") != "PASS":
            raise ControlError(7, f"status receipt mismatch: {name}")
        for value in record.values():
            if value != value.strip() or "\x00" in value:
                raise ControlError(7, f"scalar grammar failure: {name}")
        if name != CSV_NAMES[8] and record.get("oracle") != oracle:
            raise ControlError(7, f"oracle token mismatch: {name}")
        is_negative = record.get("case_kind") == "NEGATIVE"
        if is_negative != bool(record.get("negative_reason")):
            raise ControlError(7, f"negative reason mismatch: {name}")
        if is_negative != (record.get("detected") == "true"):
            raise ControlError(7, f"negative detector mismatch: {name}")
        if not is_negative and (record.get("negative_reason") or record.get("detected")):
            raise ControlError(7, f"receipt on nonnegative row: {name}")
    if sum(record.get("case_kind") == "NEGATIVE" for record in records) != negatives:
        raise ControlError(7, f"negative-count mismatch: {name}")
    families = expected_families()[index]
    if families:
        actual: list[tuple[str, int]] = []
        for record in records:
            family = record["row_family"]
            if not actual or actual[-1][0] != family:
                actual.append((family, 1))
            else:
                actual[-1] = (family, actual[-1][1] + 1)
        if tuple(actual) != families:
            raise ControlError(7, f"family order/count mismatch: {name}")


def parse_d3(value: str, prefix: str) -> tuple[int, int]:
    if not re.fullmatch(fr"{prefix}[0-2][01]", value):
        raise ControlError(7, "invalid D3 token")
    return int(value[1]), int(value[2])


def validate_range(records: Sequence[Mapping[str, str]]) -> None:
    noncommuting = {(h, k) for h in D3 for k in D3 if perm_mul(h, k) != perm_mul(k, h)}
    wrong_seen: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    opposite_seen: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for record in records:
        family = record["row_family"]
        if family == "ARROW":
            x, h = parse_d3(record["object_x"], "x"), parse_d3(record["h"], "d")
            expected = f"source={x_token(perm_mul(x, h))};range={x_token(x)}"
            if record["subject_value"] != expected or record["oracle_value"] != expected:
                raise ControlError(7, "range/source oracle failure")
        elif family == "UNIT":
            x = parse_d3(record["object_x"], "x")
            expected = arrow(x, (0, 0))
            if record["subject_value"] != expected or record["oracle_value"] != expected:
                raise ControlError(7, "unit oracle failure")
        elif family == "INVERSE":
            x, h = parse_d3(record["object_x"], "x"), parse_d3(record["h"], "d")
            inverse = next(candidate for candidate in D3 if perm_mul(h, candidate) == (0, 0))
            expected = arrow(perm_mul(x, h), inverse)
            if record["subject_value"] != expected or record["oracle_value"] != expected:
                raise ControlError(7, "inverse oracle failure")
        elif family == "PAIR":
            x, h = parse_d3(record["object_x"], "x"), parse_d3(record["h"], "d")
            y, k = parse_d3(record["object_y"], "x"), parse_d3(record["k"], "d")
            composable = y == perm_mul(x, h)
            expected = arrow(x, perm_mul(h, k)) if composable else "NONCOMPOSABLE"
            if record["subject_composable"] != bool_token(composable):
                raise ControlError(7, "composability receipt failure")
            if record["subject_value"] != expected or record["oracle_value"] != expected:
                raise ControlError(7, "product oracle failure")
        elif family in ("SHEET_ACTION", "SHEET_ASSOC"):
            h = parse_d3(record["h"], "d")
            sheet = parse_d3(record["sheet_a"], "s")
            result = perm_mul(h, sheet)
            if family == "SHEET_ASSOC":
                k = parse_d3(record["k"], "d")
                result = perm_mul(perm_mul(h, k), sheet)
            expected = s_token(result)
            if record["subject_value"] != expected or record["oracle_value"] != expected:
                raise ControlError(7, "sheet oracle failure")
        elif family == "WRONG_PRODUCT_ORDER":
            h, k = parse_d3(record["h"], "d"), parse_d3(record["k"], "d")
            if (h, k) not in noncommuting:
                raise ControlError(7, "commuting wrong-order negative")
            wrong_seen.add((h, k))
            if record["subject_value"] != arrow((0, 0), perm_mul(k, h)) or record["oracle_value"] != arrow((0, 0), perm_mul(h, k)):
                raise ControlError(7, "wrong-order detector failure")
        elif family == "OPPOSITE_SHEET_ACTION":
            h, k = parse_d3(record["h"], "d"), parse_d3(record["k"], "d")
            if (h, k) not in noncommuting:
                raise ControlError(7, "commuting handedness negative")
            opposite_seen.add((h, k))
            if record["subject_value"] != s_token(perm_mul(k, h)) or record["oracle_value"] != s_token(perm_mul(h, k)):
                raise ControlError(7, "opposite-action detector failure")
    if wrong_seen != noncommuting or opposite_seen != noncommuting:
        raise ControlError(7, "noncommuting witness inventory failure")


def token_to_set(value: str) -> set[int]:
    if value == "EMPTY":
        return set()
    if not re.fullmatch(r"[0-3](\|[0-3])*", value):
        raise ControlError(7, "invalid finite-set token")
    values = [int(item) for item in value.split("|")]
    if values != sorted(set(values)):
        raise ControlError(7, "noncanonical finite-set token")
    return set(values)


def validate_action(records: Sequence[Mapping[str, str]]) -> None:
    action_maps = {
        "TRIVIAL": tuple(tuple(j for _ in range(4)) for j in range(4)),
        "TRANSITIVE": tuple(tuple((j + t) % 4 for t in range(4)) for j in range(4)),
        "NONTRANSITIVE": tuple(tuple((j + 2 * (t & 1)) % 4 for t in range(4)) for j in range(4)),
    }
    if len(set(action_maps.values())) != 3:
        raise ControlError(7, "action table collapse")
    orbit_counts = {}
    for action, table in action_maps.items():
        unseen = set(range(4))
        orbits = 0
        while unseen:
            seed = min(unseen)
            orbit = set(table[seed])
            unseen -= orbit
            orbits += 1
        orbit_counts[action] = orbits
    if orbit_counts["TRANSITIVE"] != 1 or orbit_counts["NONTRANSITIVE"] != 2:
        raise ControlError(7, "action orbit guard failure")
    for record in records:
        family = record["row_family"]
        U = token_to_set(record["subset_u"])
        V = token_to_set(record["subset_v"]) if record["subset_v"] else set()
        if family in ("OPEN_DESCRIPTOR", "CROSS_OPEN"):
            expected = f"X4x[{set_token(U)}]"
            if record["arrow_open"] != expected:
                raise ControlError(7, "arrow-open receipt failure")
        elif family in ("INVOLUTION", "CROSS_INVOLUTION"):
            expected = set_token({(-u) % 4 for u in U})
        elif family in ("PRODUCT", "CROSS_PRODUCT"):
            expected = set_token({(u + v) % 4 for u in U for v in V})
        elif family in ("BASE", "CROSS_BASE"):
            expected = bool_token(U in (set(), {0, 1, 2, 3}))
        else:
            raise ControlError(7, "unknown action family")
        if record["subject_value"] != expected or record["oracle_value"] != expected:
            raise ControlError(7, "C4 bitset oracle failure")
        is_cross = family.startswith("CROSS_")
        if is_cross:
            if record["action_case"] != "TRIVIAL" or record["comparison_case"] not in ("TRANSITIVE", "NONTRANSITIVE") or record["record_equal"] != "true":
                raise ControlError(7, "cross-action record failure")
        elif record["comparison_case"] or record["record_equal"]:
            raise ControlError(7, "unexpected cross-action receipt")


def validate_policy_rows(name: str, records: Sequence[Mapping[str, str]]) -> None:
    # The policy artifacts are validated from closed typed registries rather
    # than from stored reason, detector, status, or oracle-value receipts.
    if name == CSV_NAMES[2]:
        reasons = [item[1] for item in (
            ("CERTIFY_CONNECTED_R", "FINITE_PROXY_PROVES_CONNECTED_R"),
            ("CERTIFY_TOPOS_EQUIVALENCE", "FINITE_PROXY_PROVES_TOPOS_EQUIVALENCE"),
            ("FORCE_SET_FOR_DISCONNECTED_TIME", "DISCONNECTED_TIME_FORCES_SET"),
            ("GENERALIZE_ALL_DISCONNECTED_H", "FINITE_PROXY_GENERALIZES_ALL_DISCONNECTED_H"),
        )]
        attacks = [record for record in records if record["row_family"] == "PROMOTION_ATTACK"]
        if [record["negative_reason"] for record in attacks] != reasons:
            raise ControlError(7, "connected-firewall reason registry failure")
        actions = [record for record in records if record["row_family"] == "Z3_ACTION"]
        for record in actions:
            n = int(record["input_n"])
            sheet = int(record["input_sheet"][1])
            expected = f"z{(n + sheet) % 3}"
            if record["subject_value"] != expected or record["oracle_value"] != expected:
                raise ControlError(7, "Z3 permutation oracle failure")
        for record in records[:3]:
            if record["source_binding"] != GATE_C17_3 or record["subject_value"] != record["oracle_value"]:
                raise ControlError(7, "connected receipt binding failure")
    elif name == CSV_NAMES[3]:
        attacks = [record for record in records if record["row_family"] == "WRONG_DOMAIN_ATTACK"]
        if [record["negative_reason"] for record in attacks] != [item[0] for item in DOMAIN_ATTACKS]:
            raise ControlError(7, "domain attack registry failure")
        typed = [(r["owner_domain"], r["topology_token"], r["claim_token"], r["evidence_mode"]) for r in attacks]
        if typed != [(a[1], a[2], a[3], a[4]) for a in DOMAIN_ATTACKS]:
            raise ControlError(7, "domain typed-delta failure")
        for record in records:
            if record["row_family"] == "CLAIM_SCOPE":
                expected = domain_policy(record["owner_domain"], record["claim_token"])
                if record["oracle_value"] != expected or record["subject_value"] != f"{record['claim_token']}=true":
                    raise ControlError(7, "domain policy failure")
    elif name == CSV_NAMES[4]:
        attacks = [record for record in records if record["row_family"] == "PROMOTION_ATTACK"]
        if [record["negative_reason"] for record in attacks] != list(QL_REASONS):
            raise ControlError(7, "quantale reason registry failure")
        for record in records:
            if record["row_family"] in ("GATE_TRUTH_TABLE", "PROMOTION_ATTACK", "OWNER_SCOPE"):
                licensed = all(record[field] == "true" for field in
                               ("bare_quantale_receipt", "q_h_receipt", "local_compactness_receipt"))
                if record["licensed"] != bool_token(licensed):
                    raise ControlError(7, "quantale conjunction failure")
            if record["row_family"] in ("SOURCE_RECEIPT", "OWNER_SCOPE") and record["source_binding"] != GATE_C17_5:
                raise ControlError(7, "quantale source binding failure")
    elif name == CSV_NAMES[5]:
        attacks = [record for record in records if record["row_family"] == "OWNER_SPLICE_ATTACK"]
        if [record["negative_reason"] for record in attacks] != list(SPLICE_REASONS):
            raise ControlError(7, "owner splice registry failure")
        for record in records:
            family = record["row_family"]
            if family == "OWNER_RECORD":
                canonical = PACKETS[record["packet_id"]]
                if tuple(record[column] for column in PACKET_COLUMNS) != canonical or record["subject_value"] != packet_value(canonical):
                    raise ControlError(7, "canonical owner packet failure")
            elif family == "FIELD_COMPARISON":
                offset = PACKET_FIELDS.index(record["comparison_field"])
                expected = f"{PACKET_FIELDS[offset]}:{PACKETS['ACTUAL'][offset]}|{PACKETS['STANDARD'][offset]}"
                if record["subject_value"] != expected or record["oracle_value"] != expected:
                    raise ControlError(7, "owner field comparison failure")
            elif record["packet_id"] in PACKETS:
                canonical = PACKETS[record["packet_id"]]
                values = tuple(record[column] for column in PACKET_COLUMNS)
                differences = sum(a != b for a, b in zip(values, canonical))
                if differences != 1 or record["oracle_value"] != packet_value(canonical):
                    raise ControlError(7, "owner one-field splice failure")
    elif name == CSV_NAMES[6]:
        strict = [record for record in records if record["row_family"] == "STRICT_MARKER"]
        if [record["scale_c"] for record in strict] != ["1/2", "1/1", "3/2", "2/1"]:
            raise ControlError(7, "strict-scale fixture failure")
        for record in strict:
            accepted = record["scale_c"] == "1/1"
            expected = "strict_marker_preserved=true" if accepted else "REJECTED"
            if record["oracle_value"] != expected:
                raise ControlError(7, "strict-marker policy failure")
        for record in records:
            if record["row_family"] in {"OBJECT_MAP", "ARROW_MAP", "SOURCE_COMPAT", "RANGE_COMPAT", "INVERSE_COMPAT", "PRODUCT_COMPAT"}:
                for field in ("L", "L_prime", "scale_c", "r"):
                    if not re.fullmatch(r"-?(0|[1-9][0-9]*)/[1-9][0-9]*", record[field]):
                        raise ControlError(7, "rational grammar failure")
                if record["subject_value"] != record["oracle_value"]:
                    raise ControlError(7, "dilation integer-oracle receipt failure")
        reasons = Counter(record["negative_reason"] for record in records if record["case_kind"] == "NEGATIVE")
        if reasons != Counter({"STRICT_MARKER_NONUNIT_SCALE": 3,
                               "PLAIN_TOPOS_NUMERICAL_SCALE_PROMOTION": 1,
                               "PLAIN_QUANTALE_NUMERICAL_SCALE_PROMOTION": 1}):
            raise ControlError(7, "dilation reason multiplicity failure")
    elif name == CSV_NAMES[7]:
        source = binding_path(root_from_script(), "../9-packet-separation/paper/manuscript.tex")
        if sha256_file(source) != BINDINGS[1][1]:
            raise ControlError(6, "Paper-9 source binding drift")
        attacks = [record for record in records if record["row_family"] == "PROVENANCE_PROMOTION_ATTACK"]
        if [record["negative_reason"] for record in attacks] != list(FP_REASONS):
            raise ControlError(7, "fixed-prime reason registry failure")
        for record in records[1:]:
            if record["source_binding"] != PAPER9_BINDING:
                raise ControlError(7, "fixed-prime row binding failure")
        for record in records:
            if record["row_family"] == "FIXED_PRIME_SUBSTITUTION":
                prime = record["prime_token"]
                stabilizer = f"(log {prime})Z"
                expected = fp_complete(prime, "INDISCRETE_FROM_PAPER9", stabilizer)
                if record["generic_theorem_state"] != GENERIC_STATE or record["subject_value"] != expected or record["oracle_value"] != expected:
                    raise ControlError(7, "fixed-prime substitution failure")


def validate_summary(records: Sequence[Mapping[str, str]], raw_records: Mapping[str, Sequence[Mapping[str, str]]]) -> None:
    if len(records) != 10:
        raise ControlError(7, "summary count failure")
    for index, name in enumerate(CSV_NAMES, 1):
        record = records[index - 1]
        expected_rows, columns, negatives, oracle, order = EXPECTED[name]
        actual = raw_records[name]
        actual_negatives = sum(item.get("case_kind") == "NEGATIVE" for item in actual)
        if name == CSV_NAMES[8]:
            actual_negatives = 0
        expected_fields = {
            "artifact": f"results/{name}", "expected_rows": str(len(actual)),
            "expected_columns": str(len(HEADERS[name])), "expected_negative_rows": str(actual_negatives),
            "oracle_class": oracle, "canonical_order_key": order,
            "scope_token": "COUNT_AND_SERIALIZATION_ONLY", "artifact_order_index": str(index),
            "status": "PASS", "notes": "",
        }
        if any(record[field] != value for field, value in expected_fields.items()):
            raise ControlError(7, f"stale summary row: {name}")
        if len(actual) != expected_rows or len(HEADERS[name]) != columns or actual_negatives != negatives:
            raise ControlError(7, f"raw summary target failure: {name}")
    package = records[-1]
    package_expected = {
        "artifact": "PACKAGE_TOTAL", "expected_rows": "3436", "expected_columns": "MIXED",
        "expected_negative_rows": "84", "oracle_class": "RAW_COUNT_SCHEMA_INVENTORY",
        "canonical_order_key": "SECTION_2_ARTIFACT_ORDER",
        "scope_token": "COUNT_AND_SERIALIZATION_ONLY", "artifact_order_index": "PACKAGE",
        "status": "PASS", "notes": "CSV_ARTIFACTS=9;GENERATED_ARTIFACTS=10",
    }
    if any(package[field] != value for field, value in package_expected.items()):
        raise ControlError(7, "stale package summary")


def exact_object_keys(value: Mapping[str, object], keys: set[str], label: str) -> None:
    if set(value) != keys:
        raise ControlError(8, f"manifest {label} key-shape failure")


def validate_manifest(root: Path, output: Path, raw_bytes: Mapping[str, bytes], raw_records: Mapping[str, Sequence[Mapping[str, str]]]) -> None:
    path = output / "manifest.json"
    data = file_bytes(path)
    if data.startswith(b"\xef\xbb\xbf") or not data.endswith(b"\n") or b"\r" in data:
        raise ControlError(8, "noncanonical manifest bytes")
    try:
        manifest = json.loads(data.decode("utf-8", "strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ControlError(8, "manifest parse failure") from exc
    if not isinstance(manifest, dict):
        raise ControlError(8, "manifest is not an object")
    canonical = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    if data != canonical:
        raise ControlError(8, "manifest serialization failure")
    exact_object_keys(manifest, {"schema_version", "package_id", "bindings", "acyclic_policy",
                                 "implementation", "artifacts", "aggregates", "reproduction", "status"}, "top-level")
    if manifest["schema_version"] != MANIFEST_SCHEMA or manifest["package_id"] != PACKAGE_ID or manifest["status"] != "PASS":
        raise ControlError(8, "manifest identity failure")
    serialized = data.decode("utf-8")
    forbidden_paths = ("phase2_topos_quantale_proofs.md", "phase2_topos_quantale_peer_review.md")
    if any(pathname in serialized for pathname in forbidden_paths):
        raise ControlError(8, "prohibited proof binding")
    policy = manifest["acyclic_policy"]
    if not isinstance(policy, dict):
        raise ControlError(8, "acyclic policy shape failure")
    exact_object_keys(policy, {"manifest_self_hash_included", "manifest_self_entry_included",
                               "p17_proof_hash_included", "p17_proof_review_hash_included",
                               "authority_policy"}, "acyclic-policy")
    if policy != {
        "manifest_self_hash_included": False, "manifest_self_entry_included": False,
        "p17_proof_hash_included": False, "p17_proof_review_hash_included": False,
        "authority_policy": "CONTROL_DESIGN_GATE_INDIRECT_PROOF_AUTHORITY",
    }:
        raise ControlError(8, "acyclic policy failure")
    if "manifest_sha256" in manifest:
        raise ControlError(8, "manifest self binding")

    bindings = manifest["bindings"]
    if not isinstance(bindings, list) or len(bindings) != 5:
        raise ControlError(8, "binding inventory failure")
    for item in bindings:
        if not isinstance(item, dict):
            raise ControlError(8, "binding shape failure")
        exact_object_keys(item, {"path", "bytes", "sha256"}, "binding")
    if [item["path"] for item in bindings] != [item[0] for item in BINDINGS]:
        raise ControlError(8, "binding order failure")

    implementation = manifest["implementation"]
    if not isinstance(implementation, list) or len(implementation) != 5:
        raise ControlError(8, "implementation manifest inventory failure")
    for item in implementation:
        if not isinstance(item, dict):
            raise ControlError(8, "implementation shape failure")
        exact_object_keys(item, {"path", "bytes", "sha256"}, "implementation")
    if [item["path"] for item in implementation] != list(IMPLEMENTATION_PATHS):
        raise ControlError(8, "implementation order failure")
    code_entries = set(path.name for path in (root / "code").iterdir())
    experiment_entries = set(path.name for path in (root / "experiments").iterdir())
    allowed_experiments = {"reproduce.sh", "README.md"}
    if os.environ.get("P17_REPRO_ACTIVE"):
        allowed_experiments.add(".p17-control-reproduce.lock")
    if code_entries != {"generate_controls.py", "test_controls.py", "README.md"} or experiment_entries != allowed_experiments:
        raise ControlError(8, "unlisted or unhashed implementation path")

    artifacts = manifest["artifacts"]
    if not isinstance(artifacts, list) or len(artifacts) != 9:
        raise ControlError(8, "artifact manifest inventory failure")
    for item in artifacts:
        if not isinstance(item, dict):
            raise ControlError(8, "artifact shape failure")
        exact_object_keys(item, {"path", "schema", "columns", "rows", "negative_rows", "bytes", "sha256"}, "artifact")
    if [item["path"] for item in artifacts] != [f"results/{name}" for name in CSV_NAMES]:
        raise ControlError(8, "artifact order failure")

    # Authority and implementation bindings are checked only after manifest
    # shape/self/proof/unhashed-path validation, as frozen by the gate.
    for item, (logical, digest) in zip(bindings, BINDINGS):
        source = binding_path(root, logical)
        one_link_regular(source, 6)
        source_data = file_bytes(source)
        if item != {"path": logical, "bytes": len(source_data), "sha256": digest} or sha256_bytes(source_data) != digest:
            raise ControlError(6, f"authority binding failure: {logical}")
    for item, logical in zip(implementation, IMPLEMENTATION_PATHS):
        source = root / logical
        one_link_regular(source, 6)
        source_data = file_bytes(source)
        if item != {"path": logical, "bytes": len(source_data), "sha256": sha256_bytes(source_data)}:
            raise ControlError(6, f"implementation binding failure: {logical}")

    for item, name in zip(artifacts, CSV_NAMES):
        expected_rows, columns, negatives, _, _ = EXPECTED[name]
        expected_item = {
            "path": f"results/{name}", "schema": DESIGN_SCHEMA, "columns": columns,
            "rows": expected_rows, "negative_rows": negatives,
            "bytes": len(raw_bytes[name]), "sha256": sha256_bytes(raw_bytes[name]),
        }
        if item != expected_item:
            raise ControlError(8, f"artifact hash/byte/aggregate failure: {name}")

    aggregates = {
        "csv_artifacts": 9, "generated_artifacts_including_manifest": 10,
        "csv_body_rows": 3436, "nonnegative_csv_rows": 3352,
        "explicit_negative_rows": 84, "expected_negatives_detected": 84,
        "semantic_mutation_classes": 48, "package_mutation_classes": 42,
        "isolated_mutation_methods": 90, "unittest_methods": 180,
    }
    reproduction = {
        "deterministic": True, "random_used": False, "network_used": False,
        "ambient_clock_used": False, "fresh_generations": 2,
        "byte_identical_copies": 3, "verify_only_rewrites": False,
    }
    if manifest["aggregates"] != aggregates or manifest["reproduction"] != reproduction:
        raise ControlError(8, "manifest aggregate/reproduction failure")


def generate(root: Path, output: Path) -> None:
    if output.is_symlink() or not output.is_dir():
        raise ControlError(4, "generate output must be an existing non-symlink directory")
    if any(output.iterdir()):
        raise ControlError(4, "generate output must be empty")
    payloads: dict[str, bytes] = {}
    for name, builder in zip(CSV_NAMES, BUILDERS):
        records = builder()
        expected_rows, columns, negatives, _, _ = EXPECTED[name]
        if len(records) != expected_rows or len(HEADERS[name]) != columns:
            raise ControlError(7, f"internal generation count failure: {name}")
        if sum(record.get("case_kind") == "NEGATIVE" for record in records) != negatives:
            raise ControlError(7, f"internal generation negative failure: {name}")
        payloads[name] = csv_bytes(HEADERS[name], records)
        with (output / name).open("xb") as handle:
            handle.write(payloads[name])
    manifest = build_manifest(root, payloads)
    manifest_data = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    with (output / "manifest.json").open("xb") as handle:
        handle.write(manifest_data)


def verify(root: Path, output: Path) -> None:
    if output.is_symlink() or not output.is_dir():
        raise ControlError(5, "verify output must be an existing non-symlink directory")
    allow_lock = bool(os.environ.get("P17_REPRO_ACTIVE"))
    scan_closed_residue(root, allow_owned_lock=allow_lock)
    exact_result_inventory(output)
    raw_bytes: dict[str, bytes] = {}
    raw_records: dict[str, list[dict[str, str]]] = {}
    for index, name in enumerate(CSV_NAMES):
        data, records = parse_csv_strict(output / name, HEADERS[name])
        raw_bytes[name] = data
        raw_records[name] = records
        validate_common(name, records, index)
        if name == CSV_NAMES[0]:
            validate_range(records)
        elif name == CSV_NAMES[1]:
            validate_action(records)
        elif name in CSV_NAMES[2:8]:
            validate_policy_rows(name, records)
    validate_summary(raw_records[CSV_NAMES[8]], raw_records)
    validate_manifest(root, output, raw_bytes, raw_records)


def parse_cli(argv: Sequence[str]) -> tuple[str, Path]:
    if len(argv) != 3 or argv[0] not in ("--generate", "--verify-only") or argv[1] != "--output-dir" or not argv[2]:
        raise ControlError(2, "usage: generate_controls.py (--generate|--verify-only) --output-dir PATH")
    return argv[0], Path(argv[2])


def main(argv: Sequence[str] | None = None) -> int:
    try:
        mode, output = parse_cli(tuple(sys.argv[1:] if argv is None else argv))
        root = root_from_script()
        if mode == "--generate":
            generate(root, output)
        else:
            verify(root, output)
        print(f"P17_CONTROLS_{'GENERATE' if mode == '--generate' else 'VERIFY'}=PASS")
        return 0
    except ControlError as exc:
        print(f"P17_CONTROLS_ERROR[{exc.code}]={exc}", file=sys.stderr)
        return exc.code
    except Exception as exc:  # fail closed; never convert an exception to success
        print(f"P17_CONTROLS_ERROR[7]={type(exc).__name__}: {exc}", file=sys.stderr)
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
