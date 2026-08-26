#!/usr/bin/env python3
"""Independent Paper-17 control verifier and exact 180-method test suite."""

from __future__ import annotations

import ast
import csv
import hashlib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from contextlib import contextmanager
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterator, Mapping, Sequence


SCHEMA = "paper17-open-groupoid-controls/1"
MANIFEST_SCHEMA = "paper17-open-groupoid-controls-manifest/1"
PACKAGE_ID = "paper17-open-groupoid-controls"
NAMES = (
    "range_first_handedness_controls.csv",
    "action_blind_open_records.csv",
    "connected_disconnected_firewall.csv",
    "domain_guard_controls.csv",
    "quantale_localic_firewall.csv",
    "actual_standard_owner_controls.csv",
    "dilation_strict_marker_controls.csv",
    "fixed_prime_provenance_controls.csv",
    "target_summary.csv",
)
ALL_NAMES = NAMES + ("manifest.json",)
HEADERS = {
    NAMES[0]: "schema_version,row_id,row_family,case_kind,group_token,object_x,h,object_y,k,sheet_a,subject_composable,subject_value,oracle_value,detected,negative_reason,oracle,status".split(","),
    NAMES[1]: "schema_version,row_id,row_family,case_kind,action_case,comparison_case,subset_u,subset_v,arrow_open,subject_value,oracle_value,record_equal,detected,negative_reason,oracle,status".split(","),
    NAMES[2]: "schema_version,row_id,row_family,case_kind,owner_domain,input_n,input_sheet,claim_token,subject_value,oracle_value,scope_token,source_binding,detected,negative_reason,oracle,status".split(","),
    NAMES[3]: "schema_version,row_id,row_family,case_kind,owner_domain,topology_token,claim_token,evidence_mode,subject_value,oracle_value,scope_token,detected,negative_reason,oracle,status".split(","),
    NAMES[4]: "schema_version,row_id,row_family,case_kind,owner_domain,bare_quantale_receipt,q_h_receipt,local_compactness_receipt,promotion_attempt,licensed,subject_value,oracle_value,source_binding,scope_token,detected,negative_reason,oracle,status".split(","),
    NAMES[5]: "schema_version,row_id,row_family,case_kind,packet_id,owner_token,topology_token,topos_token,quantale_token,base_frame_token,comparison_field,subject_value,oracle_value,detected,negative_reason,oracle,status".split(","),
    NAMES[6]: "schema_version,row_id,row_family,case_kind,L,L_prime,scale_c,r,t,u,claim_token,subject_value,oracle_value,inverse_value,scope_token,detected,negative_reason,oracle,status".split(","),
    NAMES[7]: "schema_version,row_id,row_family,case_kind,prime_token,generic_theorem_state,actual_topology_input,stabilizer_input,claim_token,subject_value,oracle_value,source_binding,scope_token,detected,negative_reason,oracle,status".split(","),
    NAMES[8]: "schema_version,row_id,artifact,expected_rows,expected_columns,expected_negative_rows,oracle_class,canonical_order_key,scope_token,artifact_order_index,status,notes".split(","),
}
EXPECTED = {
    NAMES[0]: (1662, 17, 36, "D3_RELATION_AND_LEFT_ACTION", "C17_1_FAMILY_ORDER"),
    NAMES[1]: (1520, 16, 0, "C4_BITSET_OPEN_QUANTALE", "C17_2_FAMILY_ORDER"),
    NAMES[2]: (19, 16, 4, "SOURCE_RECEIPT_PLUS_Z3_PERMUTATION", "C17_3_FAMILY_ORDER"),
    NAMES[3]: (25, 15, 10, "OWNER_DOMAIN_POLICY", "C17_4_FAMILY_ORDER"),
    NAMES[4]: (21, 18, 7, "BARE_Q_QH_LC_CONJUNCTION", "C17_5_FAMILY_ORDER"),
    NAMES[5]: (18, 17, 11, "CANONICAL_OWNER_PACKET_REGISTRY", "C17_6_FAMILY_ORDER"),
    NAMES[6]: (140, 19, 5, "INTEGER_CROSS_MULTIPLICATION_DILATION", "C17_7_FAMILY_ORDER"),
    NAMES[7]: (21, 17, 11, "P9_TWO_INPUT_POST_GENERIC_ALLOWLIST", "C17_8_FAMILY_ORDER"),
    NAMES[8]: (10, 12, 0, "RAW_COUNT_SCHEMA_INVENTORY", "TARGET_SUMMARY_ROW_ORDER"),
}
PREFIXES = ("GH", "AO", "CZ", "DG", "QL", "AS", "DM", "FP", "TS")
FAMILIES = {
    NAMES[0]: (("ARROW", 36), ("UNIT", 6), ("INVERSE", 36), ("PAIR", 1296),
               ("SHEET_ACTION", 36), ("SHEET_ASSOC", 216),
               ("WRONG_PRODUCT_ORDER", 18), ("OPPOSITE_SHEET_ACTION", 18)),
    NAMES[1]: (("OPEN_DESCRIPTOR", 48), ("INVOLUTION", 48), ("PRODUCT", 768),
               ("BASE", 48), ("CROSS_OPEN", 32), ("CROSS_INVOLUTION", 32),
               ("CROSS_PRODUCT", 512), ("CROSS_BASE", 32)),
    NAMES[2]: (("SYMBOLIC_RECEIPT", 3), ("Z3_ACTION", 9), ("Z3_PROPERTY", 3),
               ("PROMOTION_ATTACK", 4)),
    NAMES[3]: (("OWNER_RECEIPT", 3), ("CLAIM_SCOPE", 12), ("WRONG_DOMAIN_ATTACK", 10)),
    NAMES[4]: (("SOURCE_RECEIPT", 3), ("GATE_TRUTH_TABLE", 8),
               ("PROMOTION_ATTACK", 7), ("OWNER_SCOPE", 3)),
    NAMES[5]: (("OWNER_RECORD", 2), ("FIELD_COMPARISON", 5), ("OWNER_SPLICE_ATTACK", 11)),
    NAMES[6]: (("SYMBOLIC_RECEIPT", 2), ("OBJECT_MAP", 4), ("ARROW_MAP", 16),
               ("SOURCE_COMPAT", 16), ("RANGE_COMPAT", 16), ("INVERSE_COMPAT", 16),
               ("PRODUCT_COMPAT", 64), ("STRICT_MARKER", 4), ("PLAIN_SCALE_PROMOTION", 2)),
    NAMES[7]: (("GENERIC_PRECONDITION", 1), ("FIXED_PRIME_SUBSTITUTION", 3),
               ("ALLOWED_P9_INPUT", 6), ("PROVENANCE_PROMOTION_ATTACK", 11)),
}
IMPLEMENTATION = (
    "code/generate_controls.py", "code/test_controls.py", "code/README.md",
    "experiments/reproduce.sh", "experiments/README.md",
)
BINDINGS = (
    ("notes/phase2_control_design_gate.md", "093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647"),
    ("../9-packet-separation/paper/manuscript.tex", "24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb"),
    ("notes/phase2_control_design_lock.md", "abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa"),
    ("notes/phase2_control_design_review.md", "42d1389171a7c23ed40657ff979a2500a8b3daade2561af54755c0c1c4339326"),
    ("notes/phase2_control_implementation_gate.md", "aa73b08716e6064f93c1f760a9b91f16239ec204d4ea19a84cebf8d93833cf3e"),
)
PAPER9_ROW_BINDING = "papers/9-packet-separation/paper/manuscript.tex@sha256:24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_csv(package: Path, name: str) -> tuple[list[str], list[dict[str, str]], bytes]:
    path = package / name
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf") or b"\r" in data or not data.endswith(b"\n"):
        raise AssertionError(f"noncanonical CSV bytes: {name}")
    parsed = list(csv.reader(io.StringIO(data.decode("utf-8", "strict"), newline=""), strict=True))
    header = parsed[0]
    if any(len(items) != len(header) for items in parsed[1:]):
        raise AssertionError(f"width mismatch: {name}")
    return header, [dict(zip(header, items)) for items in parsed[1:]], data


def write_csv(path: Path, header: Sequence[str], rows: Sequence[Mapping[str, str]]) -> None:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=header, delimiter=",", quotechar='"',
                            quoting=csv.QUOTE_MINIMAL, doublequote=True, escapechar=None,
                            lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    path.write_bytes(stream.getvalue().encode("utf-8"))


def write_json(path: Path, value: object) -> None:
    path.write_bytes((json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"))


def receipt(path: Path) -> tuple[str, int, int, int, bytes]:
    st = path.lstat()
    return (stat.filemode(st.st_mode), st.st_size, st.st_mtime_ns, st.st_nlink, path.read_bytes())


def clean_environment() -> dict[str, str]:
    env = dict(os.environ)
    env.update({"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "PYTHONHASHSEED": "0",
                "PYTHONDONTWRITEBYTECODE": "1"})
    return env


def isolated_environment() -> dict[str, str]:
    env = clean_environment()
    env.pop("P17_REPRO_ACTIVE", None)
    return env


def run_verify(root: Path, package: Path, env: Mapping[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-B", str(root / "code/generate_controls.py"),
         "--verify-only", "--output-dir", str(package)],
        cwd=root, env=dict(env or clean_environment()), text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )


def bool_token(value: bool) -> str:
    return "true" if value else "false"


def finite_set(value: str) -> set[int]:
    if value == "EMPTY":
        return set()
    parts = [int(item) for item in value.split("|")]
    if parts != sorted(set(parts)) or any(item not in range(4) for item in parts):
        raise AssertionError("noncanonical C4 set")
    return set(parts)


D3 = ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1))


def compose(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[right[index]] for index in range(3))


def perm_power(base: tuple[int, int, int], exponent: int) -> tuple[int, int, int]:
    result = (0, 1, 2)
    for _ in range(exponent):
        result = compose(base, result)
    return result


def d3_perm(value: tuple[int, int]) -> tuple[int, int, int]:
    return compose(perm_power((1, 2, 0), value[0]), perm_power((0, 2, 1), value[1]))


PERM_TO_PAIR = {d3_perm(value): value for value in D3}


def d3_product(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return PERM_TO_PAIR[compose(d3_perm(left), d3_perm(right))]


def parse_pair(value: str, prefix: str) -> tuple[int, int]:
    if not re.fullmatch(fr"{prefix}[0-2][01]", value):
        raise AssertionError(value)
    return int(value[1]), int(value[2])


def d_token(value: tuple[int, int]) -> str:
    return f"d{value[0]}{value[1]}"


def x_token(value: tuple[int, int]) -> str:
    return f"x{value[0]}{value[1]}"


def s_token(value: tuple[int, int]) -> str:
    return f"s{value[0]}{value[1]}"


def arrow(value: tuple[int, int], group: tuple[int, int]) -> str:
    return f"a({x_token(value)};{d_token(group)})"


PACKETS = {
    "ACTUAL": ("ACTUAL_INDISCRETE_ORBIT", "INDISCRETE", "Set", "O(R)", "2"),
    "STANDARD": ("STANDARD_CIRCLE", "STANDARD_CIRCLE", "BZ", "O(S_LxR)", "O(S_L)"),
}
PACKET_COLUMNS = ("owner_token", "topology_token", "topos_token", "quantale_token", "base_frame_token")
PACKET_FIELDS = ("owner", "topology", "topos", "quantale", "base")


def packet_string(values: Sequence[str]) -> str:
    return ";".join(f"{key}={value}" for key, value in zip(PACKET_FIELDS, values))


def canonical_fraction(value: str) -> Fraction:
    if not re.fullmatch(r"-?(0|[1-9][0-9]*)/[1-9][0-9]*", value):
        raise AssertionError(f"invalid rational token {value}")
    result = Fraction(value)
    if f"{result.numerator}/{result.denominator}" != value:
        raise AssertionError(f"unreduced rational token {value}")
    return result


class IndependentOracle:
    def __init__(self, package: Path):
        self.package = package
        self.tables = {name: read_csv(package, name) for name in NAMES}

    def rows(self, name: str) -> list[dict[str, str]]:
        return self.tables[name][1]

    def check_schema(self, name: str) -> None:
        header, rows, _ = self.tables[name]
        assert header == HEADERS[name]
        expected_rows, columns, negatives, oracle, _ = EXPECTED[name]
        assert len(header) == columns
        assert len(rows) == expected_rows
        prefix = PREFIXES[NAMES.index(name)]
        for index, record in enumerate(rows, 1):
            assert record["schema_version"] == SCHEMA
            assert record["row_id"] == f"{prefix}-{index:04d}"
            assert record["status"] == "PASS"
            if name != NAMES[8]:
                assert record["oracle"] == oracle
            negative = record.get("case_kind") == "NEGATIVE"
            assert negative == bool(record.get("negative_reason"))
            assert negative == (record.get("detected") == "true")
        assert sum(row.get("case_kind") == "NEGATIVE" for row in rows) == negatives

    def check_families(self, name: str) -> None:
        groups: list[tuple[str, int]] = []
        for record in self.rows(name):
            family = record["row_family"]
            if not groups or groups[-1][0] != family:
                groups.append((family, 1))
            else:
                groups[-1] = (family, groups[-1][1] + 1)
        assert tuple(groups) == FAMILIES[name]

    def range_sources_units(self) -> None:
        rows = self.rows(NAMES[0])
        for record in rows:
            family = record["row_family"]
            if family == "ARROW":
                x = parse_pair(record["object_x"], "x")
                h = parse_pair(record["h"], "d")
                expected = f"source={x_token(d3_product(x, h))};range={x_token(x)}"
                assert record["subject_value"] == record["oracle_value"] == expected
            if family == "UNIT":
                x = parse_pair(record["object_x"], "x")
                assert record["subject_value"] == record["oracle_value"] == arrow(x, (0, 0))

    def range_inverse(self) -> None:
        for record in self.rows(NAMES[0]):
            if record["row_family"] != "INVERSE":
                continue
            x, h = parse_pair(record["object_x"], "x"), parse_pair(record["h"], "d")
            inverse = next(candidate for candidate in D3
                           if d3_product(h, candidate) == d3_product(candidate, h) == (0, 0))
            assert record["subject_value"] == record["oracle_value"] == arrow(d3_product(x, h), inverse)

    def range_pairs(self) -> None:
        composable_count = 0
        for record in self.rows(NAMES[0]):
            if record["row_family"] != "PAIR":
                continue
            x, h = parse_pair(record["object_x"], "x"), parse_pair(record["h"], "d")
            y, k = parse_pair(record["object_y"], "x"), parse_pair(record["k"], "d")
            composable = y == d3_product(x, h)
            composable_count += int(composable)
            expected = arrow(x, d3_product(h, k)) if composable else "NONCOMPOSABLE"
            assert record["subject_composable"] == bool_token(composable)
            assert record["subject_value"] == record["oracle_value"] == expected
        assert composable_count == 216

    def range_associativity(self) -> None:
        for h in D3:
            for k in D3:
                for ell in D3:
                    assert d3_product(d3_product(h, k), ell) == d3_product(h, d3_product(k, ell))

    def sheet_action(self) -> None:
        for record in self.rows(NAMES[0]):
            if record["row_family"] == "SHEET_ACTION":
                h = parse_pair(record["h"], "d")
                sheet = parse_pair(record["sheet_a"], "s")
                assert record["subject_value"] == record["oracle_value"] == s_token(d3_product(h, sheet))

    def sheet_associativity(self) -> None:
        for record in self.rows(NAMES[0]):
            if record["row_family"] == "SHEET_ASSOC":
                h, k = parse_pair(record["h"], "d"), parse_pair(record["k"], "d")
                sheet = parse_pair(record["sheet_a"], "s")
                assert record["subject_value"] == record["oracle_value"] == s_token(d3_product(d3_product(h, k), sheet))

    def range_negatives(self) -> None:
        noncommuting = {(h, k) for h in D3 for k in D3 if d3_product(h, k) != d3_product(k, h)}
        wrong = [r for r in self.rows(NAMES[0]) if r["row_family"] == "WRONG_PRODUCT_ORDER"]
        opposite = [r for r in self.rows(NAMES[0]) if r["row_family"] == "OPPOSITE_SHEET_ACTION"]
        assert len(wrong) == len(opposite) == len(noncommuting) == 18
        for record in wrong:
            h, k = parse_pair(record["h"], "d"), parse_pair(record["k"], "d")
            assert (h, k) in noncommuting
            assert record["subject_value"] == arrow((0, 0), d3_product(k, h))
            assert record["oracle_value"] == arrow((0, 0), d3_product(h, k))
        for record in opposite:
            h, k = parse_pair(record["h"], "d"), parse_pair(record["k"], "d")
            assert (h, k) in noncommuting
            assert record["subject_value"] == s_token(d3_product(k, h))
            assert record["oracle_value"] == s_token(d3_product(h, k))

    def action_relations(self) -> None:
        tables = {
            "TRIVIAL": tuple(tuple(j for _ in range(4)) for j in range(4)),
            "TRANSITIVE": tuple(tuple((j + t) % 4 for t in range(4)) for j in range(4)),
            "NONTRANSITIVE": tuple(tuple((j + 2 * (t & 1)) % 4 for t in range(4)) for j in range(4)),
        }
        assert len(set(tables.values())) == 3
        assert len({tables["TRANSITIVE"][0][t] for t in range(4)}) == 4
        assert len({tables["NONTRANSITIVE"][0][t] for t in range(4)}) == 2

    def action_family(self, selected: set[str]) -> None:
        for record in self.rows(NAMES[1]):
            family = record["row_family"]
            if family not in selected:
                continue
            U = finite_set(record["subset_u"])
            V = finite_set(record["subset_v"]) if record["subset_v"] else set()
            if family in {"OPEN_DESCRIPTOR", "CROSS_OPEN"}:
                expected = "X4x[" + ("EMPTY" if not U else "|".join(map(str, sorted(U)))) + "]"
                assert record["arrow_open"] == expected
            elif family in {"INVOLUTION", "CROSS_INVOLUTION"}:
                values = {(-u) % 4 for u in U}
                expected = "EMPTY" if not values else "|".join(map(str, sorted(values)))
            elif family in {"PRODUCT", "CROSS_PRODUCT"}:
                values = {(u + v) % 4 for u in U for v in V}
                expected = "EMPTY" if not values else "|".join(map(str, sorted(values)))
            else:
                expected = bool_token(U in (set(), {0, 1, 2, 3}))
            assert record["subject_value"] == record["oracle_value"] == expected
            cross = family.startswith("CROSS_")
            assert cross == bool(record["comparison_case"])
            assert cross == (record["record_equal"] == "true")

    def connected_receipts(self) -> None:
        receipts = self.rows(NAMES[2])[:3]
        assert [r["claim_token"] for r in receipts] == ["CONNECTED_REAL_CONCLUSION", "FINITE_CONTROL_LIMIT", "DISCONNECTED_FIREWALL"]
        assert all(r["case_kind"] == "RECEIPT" and r["scope_token"] == "SYMBOLIC_SOURCE_OWNED" for r in receipts)
        assert all(r["source_binding"] == "P17-P2-CONTROL-DESIGN-GATE-v1.0:C17-3" for r in receipts)

    def z3(self) -> None:
        actions = [r for r in self.rows(NAMES[2]) if r["row_family"] == "Z3_ACTION"]
        for record in actions:
            expected = f"z{(int(record['input_n']) + int(record['input_sheet'][1])) % 3}"
            assert record["subject_value"] == record["oracle_value"] == expected
        properties = [r["subject_value"] for r in self.rows(NAMES[2]) if r["row_family"] == "Z3_PROPERTY"]
        assert properties == ["GENERATOR_NONTRIVIAL=true", "REGULAR_QUOTIENT_TRANSITIVE=true", "NONTERMINAL_THREE_SHEETS=true"]

    def policy_negatives(self, name: str, expected: Sequence[str]) -> None:
        actual = [r["negative_reason"] for r in self.rows(name) if r["case_kind"] == "NEGATIVE"]
        assert actual == list(expected)
        assert all(r["oracle_value"] == "REJECTED" or r["subject_value"] != r["oracle_value"]
                   for r in self.rows(name) if r["case_kind"] == "NEGATIVE")

    def domain_registry(self) -> None:
        owners = [r for r in self.rows(NAMES[3]) if r["row_family"] == "OWNER_RECEIPT"]
        assert [(r["owner_domain"], r["topology_token"], r["evidence_mode"]) for r in owners] == [
            ("ACTUAL_USUAL_R", "USUAL_NONDISCRETE_R", "SYMBOLIC_SOURCE_RECEIPT_ONLY"),
            ("CONTROL_C3_DISCRETE", "FINITE_DISCRETE_C3", "FINITE_DIAGNOSTIC_ONLY"),
            ("CONTROL_C4_DISCRETE", "FINITE_DISCRETE_C4", "FINITE_DIAGNOSTIC_ONLY"),
        ]

    def domain_matrix(self) -> None:
        rows = [r for r in self.rows(NAMES[3]) if r["row_family"] == "CLAIM_SCOPE"]
        assert len(rows) == 12
        for record in rows:
            owner, claim = record["owner_domain"], record["claim_token"]
            if owner == "ACTUAL_USUAL_R":
                expected = "SYMBOLIC_QH_GATE_ONLY" if claim == "LOCALIC_RECONSTRUCTION" else "SYMBOLIC_SOURCE_OWNED"
            elif claim == "OPEN_GROUPOID":
                expected = "FINITE_DIAGNOSTIC_ONLY"
            elif claim in {"NONETALE", "NONUNITAL"}:
                expected = "FALSE_IN_DISCRETE_PROXY"
            else:
                expected = "NOT_CERTIFIABLE_BY_FINITE_PROXY"
            assert record["oracle_value"] == expected

    def quantale(self) -> None:
        rows = self.rows(NAMES[4])
        receipts = rows[:3]
        assert sum(r["bare_quantale_receipt"] == "true" for r in receipts) == 1
        assert sum(r["q_h_receipt"] == "true" for r in receipts) == 1
        assert sum(r["local_compactness_receipt"] == "true" for r in receipts) == 1
        for record in rows:
            if record["row_family"] in {"GATE_TRUTH_TABLE", "PROMOTION_ATTACK", "OWNER_SCOPE"}:
                licensed = all(record[key] == "true" for key in ("bare_quantale_receipt", "q_h_receipt", "local_compactness_receipt"))
                assert record["licensed"] == bool_token(licensed)

    def owner_packets(self) -> None:
        for record in self.rows(NAMES[5]):
            if record["row_family"] == "OWNER_RECORD":
                canonical = PACKETS[record["packet_id"]]
                assert tuple(record[key] for key in PACKET_COLUMNS) == canonical
                assert record["subject_value"] == record["oracle_value"] == packet_string(canonical)

    def owner_comparisons(self) -> None:
        records = [r for r in self.rows(NAMES[5]) if r["row_family"] == "FIELD_COMPARISON"]
        for index, record in enumerate(records):
            expected = f"{PACKET_FIELDS[index]}:{PACKETS['ACTUAL'][index]}|{PACKETS['STANDARD'][index]}"
            assert record["comparison_field"] == PACKET_FIELDS[index]
            assert record["subject_value"] == record["oracle_value"] == expected

    def owner_splices(self) -> None:
        records = [r for r in self.rows(NAMES[5]) if r["row_family"] == "OWNER_SPLICE_ATTACK"]
        assert len(records) == 11
        for record in records[:10]:
            canonical = PACKETS[record["packet_id"]]
            current = tuple(record[key] for key in PACKET_COLUMNS)
            assert sum(a != b for a, b in zip(current, canonical)) == 1
            assert record["oracle_value"] == packet_string(canonical)
        assert records[-1]["subject_value"] == "base_relation=EQUAL"
        assert records[-1]["oracle_value"] == "base_relation=DISTINCT"

    def dilation_fractions(self) -> None:
        for record in self.rows(NAMES[6]):
            for key in ("L", "L_prime", "scale_c", "r", "t", "u"):
                if record[key]:
                    canonical_fraction(record[key])

    def dilation_roundtrip(self) -> None:
        rows = [r for r in self.rows(NAMES[6]) if r["row_family"] in {"OBJECT_MAP", "ARROW_MAP"}]
        for record in rows:
            assert record["subject_value"] == record["oracle_value"]
            assert record["inverse_value"]

    def dilation_compat(self, families: set[str]) -> None:
        for record in self.rows(NAMES[6]):
            if record["row_family"] in families:
                assert record["subject_value"] == record["oracle_value"]
                assert record["inverse_value"] == ""

    def dilation_firewall(self) -> None:
        strict = [r for r in self.rows(NAMES[6]) if r["row_family"] == "STRICT_MARKER"]
        assert [r["scale_c"] for r in strict] == ["1/2", "1/1", "3/2", "2/1"]
        assert [r["oracle_value"] for r in strict] == ["REJECTED", "strict_marker_preserved=true", "REJECTED", "REJECTED"]
        plain = [r for r in self.rows(NAMES[6]) if r["row_family"] == "PLAIN_SCALE_PROMOTION"]
        assert [r["negative_reason"] for r in plain] == ["PLAIN_TOPOS_NUMERICAL_SCALE_PROMOTION", "PLAIN_QUANTALE_NUMERICAL_SCALE_PROMOTION"]

    def fixed_prime_binding(self, root: Path) -> None:
        source = root.parent / "9-packet-separation/paper/manuscript.tex"
        assert digest(source.read_bytes()) == BINDINGS[1][1]
        assert all(r["source_binding"] == PAPER9_ROW_BINDING for r in self.rows(NAMES[7])[1:])

    def fixed_prime(self) -> None:
        rows = self.rows(NAMES[7])
        assert rows[0]["generic_theorem_state"] == "PROVED_UPSTREAM_BEFORE_SUBSTITUTION"
        substitutions = [r for r in rows if r["row_family"] == "FIXED_PRIME_SUBSTITUTION"]
        assert [r["prime_token"] for r in substitutions] == ["2", "3", "5"]
        for record in substitutions:
            prime = record["prime_token"]
            assert record["actual_topology_input"] == "INDISCRETE_FROM_PAPER9"
            assert record["stabilizer_input"] == f"(log {prime})Z"
        allowed = [r for r in rows if r["row_family"] == "ALLOWED_P9_INPUT"]
        assert [r["claim_token"] for r in allowed] == ["INDISCRETENESS", "LITERAL_STABILIZER"] * 3

    def summary(self) -> None:
        records = self.rows(NAMES[8])
        for index, name in enumerate(NAMES, 1):
            target = records[index - 1]
            raw = self.rows(name)
            assert target["artifact"] == f"results/{name}"
            assert int(target["expected_rows"]) == len(raw)
            assert int(target["expected_columns"]) == len(HEADERS[name])
            assert int(target["expected_negative_rows"]) == sum(r.get("case_kind") == "NEGATIVE" for r in raw)
            assert target["artifact_order_index"] == str(index)
        package = records[-1]
        assert package["artifact"] == "PACKAGE_TOTAL"
        assert package["expected_rows"] == "3436"
        assert package["expected_negative_rows"] == "84"
        assert package["notes"] == "CSV_ARTIFACTS=9;GENERATED_ARTIFACTS=10"

    def all_semantics(self, root: Path) -> None:
        for name in NAMES:
            self.check_schema(name)
            if name in FAMILIES:
                self.check_families(name)
        self.range_sources_units(); self.range_inverse(); self.range_pairs(); self.range_associativity()
        self.sheet_action(); self.sheet_associativity(); self.range_negatives()
        self.action_relations(); self.action_family(set(FAMILIES[NAMES[1]][i][0] for i in range(8)))
        self.connected_receipts(); self.z3(); self.domain_registry(); self.domain_matrix(); self.quantale()
        self.owner_packets(); self.owner_comparisons(); self.owner_splices()
        self.dilation_fractions(); self.dilation_roundtrip()
        self.dilation_compat({"SOURCE_COMPAT", "RANGE_COMPAT", "INVERSE_COMPAT", "PRODUCT_COMPAT"})
        self.dilation_firewall(); self.fixed_prime_binding(root); self.fixed_prime(); self.summary()


@dataclass(frozen=True)
class Context:
    root: Path
    checked: Path
    fresh_a: Path
    fresh_b: Path


CTX: Context


class ControlCase(unittest.TestCase):
    @property
    def oracle(self) -> IndependentOracle:
        return IndependentOracle(CTX.checked)


class TestC17_1RangeFirst(ControlCase):
    def test_c17_1_schema_header_and_ids(self): self.oracle.check_schema(NAMES[0])
    def test_c17_1_family_order_and_counts(self): self.oracle.check_families(NAMES[0])
    def test_c17_1_source_range_units(self): self.oracle.range_sources_units()
    def test_c17_1_inverse_laws(self): self.oracle.range_inverse()
    def test_c17_1_composability_matrix(self): self.oracle.range_pairs()
    def test_c17_1_multiplication_associativity(self): self.oracle.range_associativity()
    def test_c17_1_left_sheet_action(self): self.oracle.sheet_action()
    def test_c17_1_sheet_action_associativity(self): self.oracle.sheet_associativity()
    def test_c17_1_wrong_order_rows_detected(self): self.oracle.range_negatives()
    def test_c17_1_oracle_recomputation(self):
        self.oracle.range_sources_units(); self.oracle.range_inverse(); self.oracle.range_pairs(); self.oracle.range_negatives()


class TestC17_2ActionBlind(ControlCase):
    def test_c17_2_schema_header_and_ids(self): self.oracle.check_schema(NAMES[1])
    def test_c17_2_family_order_and_counts(self): self.oracle.check_families(NAMES[1])
    def test_c17_2_same_carrier_three_actions(self): self.oracle.action_relations()
    def test_c17_2_arrow_open_descriptors(self): self.oracle.action_family({"OPEN_DESCRIPTOR"})
    def test_c17_2_involution_formula(self): self.oracle.action_family({"INVOLUTION"})
    def test_c17_2_product_formula(self): self.oracle.action_family({"PRODUCT"})
    def test_c17_2_two_element_base(self): self.oracle.action_family({"BASE"})
    def test_c17_2_cross_action_open_and_inverse(self): self.oracle.action_family({"CROSS_OPEN", "CROSS_INVOLUTION"})
    def test_c17_2_cross_action_product_and_base(self): self.oracle.action_family({"CROSS_PRODUCT", "CROSS_BASE"})
    def test_c17_2_oracle_recomputation(self): self.oracle.action_family({item[0] for item in FAMILIES[NAMES[1]]})


CONNECTED_REASONS = ("FINITE_PROXY_PROVES_CONNECTED_R", "FINITE_PROXY_PROVES_TOPOS_EQUIVALENCE",
                     "DISCONNECTED_TIME_FORCES_SET", "FINITE_PROXY_GENERALIZES_ALL_DISCONNECTED_H")


class TestC17_3ConnectedFirewall(ControlCase):
    def test_c17_3_schema_header_and_ids(self): self.oracle.check_schema(NAMES[2])
    def test_c17_3_receipts_are_nonexecuted(self): self.oracle.connected_receipts()
    def test_c17_3_z3_action_table(self): self.oracle.z3()
    def test_c17_3_nontrivial_transitive_nonterminal(self): self.oracle.z3()
    def test_c17_3_promotion_rows_detected(self): self.oracle.policy_negatives(NAMES[2], CONNECTED_REASONS)
    def test_c17_3_oracle_recomputation(self): self.oracle.connected_receipts(); self.oracle.z3()


DOMAIN_REASONS = (
    "C3_PROXY_CERTIFIES_R_NONETALE", "C4_PROXY_CERTIFIES_R_NONETALE",
    "C3_PROXY_CERTIFIES_R_NONUNITAL", "C4_PROXY_CERTIFIES_R_NONUNITAL",
    "DISCRETE_SINGLETON_OPEN_IMPORTED_TO_R", "DISCRETE_LOCAL_CHART_IMPORTED_TO_R",
    "USUAL_R_RELABELLED_DISCRETE", "DISCRETE_PROXY_RELABELLED_USUAL_R",
    "R_NONETALE_GENERALIZED_ALL_H", "R_NONUNITAL_GENERALIZED_ALL_H",
)


class TestC17_4DomainGuards(ControlCase):
    def test_c17_4_schema_header_and_ids(self): self.oracle.check_schema(NAMES[3])
    def test_c17_4_owner_registry(self): self.oracle.domain_registry()
    def test_c17_4_claim_scope_matrix(self): self.oracle.domain_matrix()
    def test_c17_4_discrete_proxy_not_real_owner(self): self.oracle.domain_matrix()
    def test_c17_4_wrong_domain_rows_detected(self): self.oracle.policy_negatives(NAMES[3], DOMAIN_REASONS)
    def test_c17_4_oracle_recomputation(self): self.oracle.domain_registry(); self.oracle.domain_matrix()


QUANTALE_REASONS = (
    "LOCALIC_WITHOUT_BARE_QH_LC", "LOCALIC_WITH_ONLY_LC", "LOCALIC_WITH_ONLY_QH",
    "LOCALIC_WITHOUT_BARE_QUANTALE", "BARE_QUANTALE_ALONE_PROMOTED",
    "BARE_QUANTALE_LC_WITHOUT_QH", "BARE_QUANTALE_QH_WITHOUT_LC",
)


class TestC17_5QuantaleLocalic(ControlCase):
    def test_c17_5_schema_header_and_ids(self): self.oracle.check_schema(NAMES[4])
    def test_c17_5_three_separate_receipts(self): self.oracle.quantale()
    def test_c17_5_truth_table(self): self.oracle.quantale()
    def test_c17_5_bare_quantale_promotion_rejected(self): self.oracle.policy_negatives(NAMES[4], QUANTALE_REASONS)
    def test_c17_5_owner_scope_rows(self): self.oracle.quantale()
    def test_c17_5_oracle_recomputation(self): self.oracle.quantale()


OWNER_REASONS = (
    "ACTUAL_PACKET_OWNER_RELABELLED_STANDARD", "STANDARD_TOPOLOGY_IMPORTED_ACTUAL",
    "STANDARD_TOPOS_SPLICED_ACTUAL", "STANDARD_QUANTALE_SPLICED_ACTUAL",
    "STANDARD_BASE_SPLICED_ACTUAL", "STANDARD_PACKET_OWNER_RELABELLED_ACTUAL",
    "INDISCRETE_TOPOLOGY_IMPORTED_STANDARD", "ACTUAL_TOPOS_SPLICED_STANDARD",
    "ACTUAL_QUANTALE_SPLICED_STANDARD", "ACTUAL_BASE_SPLICED_STANDARD",
    "ACTUAL_STANDARD_BASES_IDENTIFIED",
)


class TestC17_6OwnerPackets(ControlCase):
    def test_c17_6_schema_header_and_ids(self): self.oracle.check_schema(NAMES[5])
    def test_c17_6_exact_actual_packet(self): self.oracle.owner_packets()
    def test_c17_6_exact_standard_packet(self): self.oracle.owner_packets()
    def test_c17_6_field_comparisons(self): self.oracle.owner_comparisons()
    def test_c17_6_splice_rows_detected(self): self.oracle.policy_negatives(NAMES[5], OWNER_REASONS); self.oracle.owner_splices()
    def test_c17_6_oracle_recomputation(self): self.oracle.owner_packets(); self.oracle.owner_splices()


class TestC17_7Dilation(ControlCase):
    def test_c17_7_schema_header_and_ids(self): self.oracle.check_schema(NAMES[6])
    def test_c17_7_fraction_canonicalization(self): self.oracle.dilation_fractions()
    def test_c17_7_object_arrow_round_trip(self): self.oracle.dilation_roundtrip()
    def test_c17_7_source_range_compatibility(self): self.oracle.dilation_compat({"SOURCE_COMPAT", "RANGE_COMPAT"})
    def test_c17_7_inverse_compatibility(self): self.oracle.dilation_compat({"INVERSE_COMPAT"})
    def test_c17_7_product_compatibility(self): self.oracle.dilation_compat({"PRODUCT_COMPAT"})
    def test_c17_7_strict_nonunit_rejections(self): self.oracle.dilation_firewall()
    def test_c17_7_plain_scale_firewall_and_oracle(self): self.oracle.dilation_firewall()


FIXED_REASONS = (
    "C_STAR_PROMOTION", "HAAR_PROMOTION", "MEASURE_PROMOTION", "TRACE_PROMOTION",
    "DETERMINANT_PROMOTION", "ROUTE_B_PROMOTION", "PRIORITY_PROMOTION",
    "STANDARD_TOPOLOGY_PROMOTION", "NUMERICAL_LOG_EVALUATION",
    "FIXED_PRIME_SUBSTITUTION_BEFORE_GENERIC", "NONLITERAL_STABILIZER_REWRITE",
)


class TestC17_8FixedPrime(ControlCase):
    def test_c17_8_schema_header_and_ids(self): self.oracle.check_schema(NAMES[7])
    def test_c17_8_paper9_binding(self): self.oracle.fixed_prime_binding(CTX.root)
    def test_c17_8_post_generic_order(self): self.oracle.fixed_prime()
    def test_c17_8_only_two_allowed_inputs(self): self.oracle.fixed_prime()
    def test_c17_8_promotion_rows_detected(self): self.oracle.policy_negatives(NAMES[7], FIXED_REASONS)
    def test_c17_8_oracle_recomputation(self): self.oracle.fixed_prime_binding(CTX.root); self.oracle.fixed_prime()


class TestTargetSummary(ControlCase):
    def test_summary_schema_header_and_ids(self): self.oracle.check_schema(NAMES[8])
    def test_summary_nine_file_rows(self): self.oracle.summary()
    def test_summary_self_row(self):
        row = self.oracle.rows(NAMES[8])[8]; self.assertEqual((row["expected_rows"], row["expected_columns"]), ("10", "12"))
    def test_summary_package_row(self): self.oracle.summary()
    def test_summary_raw_row_recompute(self): self.oracle.summary()
    def test_summary_negative_recompute(self): self.oracle.summary()
    def test_summary_column_width_recompute(self): self.assertEqual([len(HEADERS[name]) for name in NAMES], [17,16,16,15,18,17,19,17,12])
    def test_summary_contains_no_hash(self): self.assertNotIn("sha", ",".join(HEADERS[NAMES[8]]).lower())


def load_manifest(package: Path) -> dict[str, object]:
    data = (package / "manifest.json").read_bytes()
    value = json.loads(data.decode("utf-8"))
    assert data == (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    return value


class TestManifest(ControlCase):
    def test_manifest_schema_and_package_id(self):
        m = load_manifest(CTX.checked); self.assertEqual((m["schema_version"], m["package_id"]), (MANIFEST_SCHEMA, PACKAGE_ID))
    def test_manifest_binding_lifecycle_order(self):
        self.assertEqual([x["path"] for x in load_manifest(CTX.checked)["bindings"]], [x[0] for x in BINDINGS])
    def test_manifest_design_gate_binding(self): self.assertEqual(load_manifest(CTX.checked)["bindings"][0]["sha256"], BINDINGS[0][1])
    def test_manifest_paper9_source_binding(self): self.assertEqual(load_manifest(CTX.checked)["bindings"][1]["sha256"], BINDINGS[1][1])
    def test_manifest_design_review_implementation_gate_bindings(self):
        m=load_manifest(CTX.checked); self.assertEqual([m["bindings"][i]["sha256"] for i in (3,4)], [BINDINGS[i][1] for i in (3,4)])
    def test_manifest_all_implementation_paths_hashed(self):
        m=load_manifest(CTX.checked); self.assertEqual([x["path"] for x in m["implementation"]], list(IMPLEMENTATION)); self.assertTrue(all(len(x["sha256"])==64 for x in m["implementation"]))
    def test_manifest_all_csv_artifacts_hashed(self):
        m=load_manifest(CTX.checked); self.assertEqual([x["path"] for x in m["artifacts"]], [f"results/{n}" for n in NAMES]); self.assertTrue(all(len(x["sha256"])==64 for x in m["artifacts"]))
    def test_manifest_no_self_hash_or_self_entry(self):
        m=load_manifest(CTX.checked); self.assertNotIn("manifest_sha256",m); self.assertFalse(m["acyclic_policy"]["manifest_self_hash_included"]); self.assertNotIn("results/manifest.json", json.dumps(m))
    def test_manifest_no_proof_or_proof_review_binding(self):
        text=json.dumps(load_manifest(CTX.checked)); self.assertNotIn("phase2_topos_quantale_proofs.md",text); self.assertNotIn("phase2_topos_quantale_peer_review.md",text)
    def test_manifest_aggregate_targets(self):
        m=load_manifest(CTX.checked); self.assertEqual(m["aggregates"], {"csv_artifacts":9,"generated_artifacts_including_manifest":10,"csv_body_rows":3436,"nonnegative_csv_rows":3352,"explicit_negative_rows":84,"expected_negatives_detected":84,"semantic_mutation_classes":48,"package_mutation_classes":42,"isolated_mutation_methods":90,"unittest_methods":180})


def package_equal(left: Path, right: Path) -> bool:
    return all((left / name).read_bytes() == (right / name).read_bytes() for name in ALL_NAMES)


def scan_cache(root: Path) -> list[Path]:
    found=[]
    for path in root.rglob("*"):
        if path.name in {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"} or path.name.endswith((".pyc", ".pyo")):
            found.append(path)
    return found


class TestReproduction(ControlCase):
    def test_repro_checked_in_verify_only(self): self.assertEqual(run_verify(CTX.root,CTX.checked).returncode,0)
    def test_repro_fresh_generation_a_verify(self): self.assertEqual(run_verify(CTX.root,CTX.fresh_a).returncode,0)
    def test_repro_fresh_generation_b_verify(self): self.assertEqual(run_verify(CTX.root,CTX.fresh_b).returncode,0)
    def test_repro_checked_in_equals_a(self): self.assertTrue(package_equal(CTX.checked,CTX.fresh_a))
    def test_repro_a_equals_b(self): self.assertTrue(package_equal(CTX.fresh_a,CTX.fresh_b))
    def test_repro_manifest_in_three_way_identity(self): self.assertEqual((CTX.checked/"manifest.json").read_bytes(),(CTX.fresh_a/"manifest.json").read_bytes()); self.assertEqual((CTX.fresh_a/"manifest.json").read_bytes(),(CTX.fresh_b/"manifest.json").read_bytes())
    def test_repro_checked_in_read_only_receipt(self):
        before={n:receipt(CTX.checked/n) for n in ALL_NAMES}; self.assertEqual(run_verify(CTX.root,CTX.checked).returncode,0); self.assertEqual(before,{n:receipt(CTX.checked/n) for n in ALL_NAMES})
    def test_repro_cleanup_and_no_cache(self): self.assertEqual(scan_cache(CTX.root),[]); self.assertEqual({p.name for p in CTX.fresh_a.iterdir()},set(ALL_NAMES)); self.assertEqual({p.name for p in CTX.fresh_b.iterdir()},set(ALL_NAMES))


class TestOracleIndependence(ControlCase):
    def test_oracle_does_not_import_generator(self):
        tree=ast.parse((CTX.root/"code/test_controls.py").read_text("utf-8")); names={n.module for n in ast.walk(tree) if isinstance(n,ast.ImportFrom)}|{a.name for n in ast.walk(tree) if isinstance(n,ast.Import) for a in n.names}; self.assertFalse(any("generate_controls" in (n or "") for n in names))
    def test_generator_does_not_import_test_module(self): self.assertNotIn("import test_controls",(CTX.root/"code/generate_controls.py").read_text("utf-8"))
    def test_oracle_ignores_emitted_status(self):
        r=dict(self.oracle.rows(NAMES[3])[3]); r["status"]="FAIL"; self.assertEqual(r["claim_token"],"OPEN_GROUPOID"); self.oracle.domain_matrix()
    def test_oracle_ignores_emitted_detector_and_reason(self):
        r=dict(self.oracle.rows(NAMES[4])[11]); r["detected"]=""; r["negative_reason"]="WRONG"; licensed=all(r[k]=="true" for k in ("bare_quantale_receipt","q_h_receipt","local_compactness_receipt")); self.assertFalse(licensed)
    def test_oracle_recomputes_values_from_primitive_fields(self): self.oracle.all_semantics(CTX.root)
    def test_summary_recomputed_from_raw_inventory(self): self.oracle.summary()


def derive_semantic_reason(payload: Mapping[str, object]) -> str | None:
    kind = payload["kind"]
    if kind == "group":
        return "WRONG_GROUP_PRODUCT_ORDER" if payload["operation"] == "k*h" else "OPPOSITE_SHEET_ACTION_HANDEDNESS"
    if kind == "connected":
        return {"connected":"FINITE_PROXY_PROVES_CONNECTED_R","topos":"FINITE_PROXY_PROVES_TOPOS_EQUIVALENCE","set":"DISCONNECTED_TIME_FORCES_SET","all_h":"FINITE_PROXY_GENERALIZES_ALL_DISCONNECTED_H"}[str(payload["claim"])]
    if kind == "domain":
        return DOMAIN_REASONS[int(payload["attack_index"])]
    if kind == "quantale":
        bits=str(payload["bits"]); return QUANTALE_REASONS[int(bits,2)] if bits!="111" and payload.get("promote") else None
    if kind == "packet":
        index=int(payload["field"]); side=str(payload["side"])
        return OWNER_REASONS[index if side=="ACTUAL" else 5+index]
    if kind == "base_relation": return "ACTUAL_STANDARD_BASES_IDENTIFIED"
    if kind == "strict": return "STRICT_MARKER_NONUNIT_SCALE" if Fraction(str(payload["scale"])) != 1 else None
    if kind == "plain": return "PLAIN_TOPOS_NUMERICAL_SCALE_PROMOTION" if payload["owner"]=="TOPOS" else "PLAIN_QUANTALE_NUMERICAL_SCALE_PROMOTION"
    if kind == "fixed_claim": return FIXED_REASONS[int(payload["claim_index"])]
    if kind == "fixed_topology": return "STANDARD_TOPOLOGY_PROMOTION"
    if kind == "fixed_numeric": return "NUMERICAL_LOG_EVALUATION"
    if kind == "fixed_order": return "FIXED_PRIME_SUBSTITUTION_BEFORE_GENERIC"
    if kind == "fixed_rewrite": return "NONLITERAL_STABILIZER_REWRITE"
    return None


class TestSemanticMutations(ControlCase):
    def _assert_reason(self,payload,expected): self.assertEqual(derive_semantic_reason(payload),expected)
    def test_s001_wrong_group_product_order(self): self._assert_reason({"kind":"group","operation":"k*h"},"WRONG_GROUP_PRODUCT_ORDER")
    def test_s002_opposite_sheet_action_handedness(self): self._assert_reason({"kind":"group","operation":"opposite-sheet"},"OPPOSITE_SHEET_ACTION_HANDEDNESS")
    def test_s003_finite_proxy_proves_connected_r(self): self._assert_reason({"kind":"connected","claim":"connected"},"FINITE_PROXY_PROVES_CONNECTED_R")
    def test_s004_finite_proxy_proves_topos_equivalence(self): self._assert_reason({"kind":"connected","claim":"topos"},"FINITE_PROXY_PROVES_TOPOS_EQUIVALENCE")
    def test_s005_disconnected_time_forces_set(self): self._assert_reason({"kind":"connected","claim":"set"},"DISCONNECTED_TIME_FORCES_SET")
    def test_s006_finite_proxy_generalizes_disconnected_h(self): self._assert_reason({"kind":"connected","claim":"all_h"},"FINITE_PROXY_GENERALIZES_ALL_DISCONNECTED_H")
    def test_s007_c3_proxy_certifies_r_nonetale(self): self._assert_reason({"kind":"domain","attack_index":0},DOMAIN_REASONS[0])
    def test_s008_c4_proxy_certifies_r_nonetale(self): self._assert_reason({"kind":"domain","attack_index":1},DOMAIN_REASONS[1])
    def test_s009_c3_proxy_certifies_r_nonunital(self): self._assert_reason({"kind":"domain","attack_index":2},DOMAIN_REASONS[2])
    def test_s010_c4_proxy_certifies_r_nonunital(self): self._assert_reason({"kind":"domain","attack_index":3},DOMAIN_REASONS[3])
    def test_s011_discrete_singleton_open_imported_to_r(self): self._assert_reason({"kind":"domain","attack_index":4},DOMAIN_REASONS[4])
    def test_s012_discrete_local_chart_imported_to_r(self): self._assert_reason({"kind":"domain","attack_index":5},DOMAIN_REASONS[5])
    def test_s013_usual_r_relabelled_discrete(self): self._assert_reason({"kind":"domain","attack_index":6},DOMAIN_REASONS[6])
    def test_s014_discrete_proxy_relabelled_usual_r(self): self._assert_reason({"kind":"domain","attack_index":7},DOMAIN_REASONS[7])
    def test_s015_r_nonetale_generalized_all_h(self): self._assert_reason({"kind":"domain","attack_index":8},DOMAIN_REASONS[8])
    def test_s016_r_nonunital_generalized_all_h(self): self._assert_reason({"kind":"domain","attack_index":9},DOMAIN_REASONS[9])
    def test_s017_localic_without_bare_qh_lc(self): self._assert_reason({"kind":"quantale","bits":"000","promote":True},QUANTALE_REASONS[0])
    def test_s018_localic_with_only_lc(self): self._assert_reason({"kind":"quantale","bits":"001","promote":True},QUANTALE_REASONS[1])
    def test_s019_localic_with_only_qh(self): self._assert_reason({"kind":"quantale","bits":"010","promote":True},QUANTALE_REASONS[2])
    def test_s020_localic_without_bare_quantale(self): self._assert_reason({"kind":"quantale","bits":"011","promote":True},QUANTALE_REASONS[3])
    def test_s021_bare_quantale_alone_promoted(self): self._assert_reason({"kind":"quantale","bits":"100","promote":True},QUANTALE_REASONS[4])
    def test_s022_bare_quantale_lc_without_qh(self): self._assert_reason({"kind":"quantale","bits":"101","promote":True},QUANTALE_REASONS[5])
    def test_s023_bare_quantale_qh_without_lc(self): self._assert_reason({"kind":"quantale","bits":"110","promote":True},QUANTALE_REASONS[6])
    def test_s024_actual_packet_owner_relabelled_standard(self): self._assert_reason({"kind":"packet","side":"ACTUAL","field":0},OWNER_REASONS[0])
    def test_s025_standard_topology_imported_actual(self): self._assert_reason({"kind":"packet","side":"ACTUAL","field":1},OWNER_REASONS[1])
    def test_s026_standard_topos_spliced_actual(self): self._assert_reason({"kind":"packet","side":"ACTUAL","field":2},OWNER_REASONS[2])
    def test_s027_standard_quantale_spliced_actual(self): self._assert_reason({"kind":"packet","side":"ACTUAL","field":3},OWNER_REASONS[3])
    def test_s028_standard_base_spliced_actual(self): self._assert_reason({"kind":"packet","side":"ACTUAL","field":4},OWNER_REASONS[4])
    def test_s029_standard_packet_owner_relabelled_actual(self): self._assert_reason({"kind":"packet","side":"STANDARD","field":0},OWNER_REASONS[5])
    def test_s030_indiscrete_topology_imported_standard(self): self._assert_reason({"kind":"packet","side":"STANDARD","field":1},OWNER_REASONS[6])
    def test_s031_actual_topos_spliced_standard(self): self._assert_reason({"kind":"packet","side":"STANDARD","field":2},OWNER_REASONS[7])
    def test_s032_actual_quantale_spliced_standard(self): self._assert_reason({"kind":"packet","side":"STANDARD","field":3},OWNER_REASONS[8])
    def test_s033_actual_base_spliced_standard(self): self._assert_reason({"kind":"packet","side":"STANDARD","field":4},OWNER_REASONS[9])
    def test_s034_actual_standard_bases_identified(self): self._assert_reason({"kind":"base_relation"},OWNER_REASONS[10])
    def test_s035_strict_marker_nonunit_scale(self):
        for scale in ("1/2","3/2","2/1"): self._assert_reason({"kind":"strict","scale":scale},"STRICT_MARKER_NONUNIT_SCALE")
    def test_s036_plain_topos_numerical_scale_promotion(self): self._assert_reason({"kind":"plain","owner":"TOPOS"},"PLAIN_TOPOS_NUMERICAL_SCALE_PROMOTION")
    def test_s037_plain_quantale_numerical_scale_promotion(self): self._assert_reason({"kind":"plain","owner":"QUANTALE"},"PLAIN_QUANTALE_NUMERICAL_SCALE_PROMOTION")
    def test_s038_c_star_promotion(self): self._assert_reason({"kind":"fixed_claim","claim_index":0},FIXED_REASONS[0])
    def test_s039_haar_promotion(self): self._assert_reason({"kind":"fixed_claim","claim_index":1},FIXED_REASONS[1])
    def test_s040_measure_promotion(self): self._assert_reason({"kind":"fixed_claim","claim_index":2},FIXED_REASONS[2])
    def test_s041_trace_promotion(self): self._assert_reason({"kind":"fixed_claim","claim_index":3},FIXED_REASONS[3])
    def test_s042_determinant_promotion(self): self._assert_reason({"kind":"fixed_claim","claim_index":4},FIXED_REASONS[4])
    def test_s043_route_b_promotion(self): self._assert_reason({"kind":"fixed_claim","claim_index":5},FIXED_REASONS[5])
    def test_s044_priority_promotion(self): self._assert_reason({"kind":"fixed_claim","claim_index":6},FIXED_REASONS[6])
    def test_s045_standard_topology_promotion(self): self._assert_reason({"kind":"fixed_topology"},FIXED_REASONS[7])
    def test_s046_numerical_log_evaluation(self): self._assert_reason({"kind":"fixed_numeric"},FIXED_REASONS[8])
    def test_s047_fixed_prime_substitution_before_generic(self): self._assert_reason({"kind":"fixed_order"},FIXED_REASONS[9])
    def test_s048_nonliteral_stabilizer_rewrite(self): self._assert_reason({"kind":"fixed_rewrite"},FIXED_REASONS[10])


def flip_hex(value: str) -> str:
    return ("1" if value[0] == "0" else "0") + value[1:]


@contextmanager
def isolated_copy() -> Iterator[Path]:
    holder = Path(tempfile.mkdtemp(prefix=".p17-mutation-", dir=CTX.fresh_a))
    root = holder / "17-open-groupoid-interfaces"
    try:
        (root / "code").mkdir(parents=True)
        (root / "experiments").mkdir()
        (root / "notes").mkdir()
        for logical in IMPLEMENTATION[:3]: shutil.copy2(CTX.root/logical, root/logical)
        for logical in IMPLEMENTATION[3:]: shutil.copy2(CTX.root/logical, root/logical)
        shutil.copytree(CTX.checked, root / "results")
        for logical,_ in (BINDINGS[0],BINDINGS[2],BINDINGS[3],BINDINGS[4]): shutil.copy2(CTX.root/logical, root/logical)
        paper9 = holder / "9-packet-separation/paper"
        paper9.mkdir(parents=True)
        shutil.copy2(CTX.root.parent/"9-packet-separation/paper/manuscript.tex", paper9/"manuscript.tex")
        yield root
    finally:
        shutil.rmtree(holder)


def mutate_csv(root: Path, name: str, action: Callable[[list[str], list[dict[str,str]]],None]) -> None:
    header,rows,_=read_csv(root/"results",name); action(header,rows); write_csv(root/"results"/name,header,rows)


def mutate_manifest(root: Path, action: Callable[[dict[str,object]],None]) -> None:
    path=root/"results/manifest.json"; value=json.loads(path.read_text("utf-8")); action(value); write_json(path,value)


def tree_snapshot(root: Path) -> dict[str, tuple[object, ...]]:
    snapshot: dict[str, tuple[object, ...]] = {}
    for directory, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        dirnames.sort(); filenames.sort()
        base = Path(directory)
        for name in tuple(dirnames) + tuple(filenames):
            path = base / name
            logical = path.relative_to(root).as_posix()
            info = path.lstat()
            mode = stat.S_IMODE(info.st_mode)
            if stat.S_ISDIR(info.st_mode):
                snapshot[logical] = ("directory", mode)
            elif stat.S_ISREG(info.st_mode):
                snapshot[logical] = ("regular", mode, info.st_size, info.st_mtime_ns,
                                     info.st_nlink, path.read_bytes())
            elif stat.S_ISLNK(info.st_mode):
                snapshot[logical] = ("symlink", mode, info.st_mtime_ns,
                                     info.st_nlink, os.readlink(path))
            else:
                snapshot[logical] = ("other", info.st_mode, info.st_size,
                                     info.st_mtime_ns, info.st_nlink)
    return snapshot


def snapshot_delta(before: Mapping[str, tuple[object, ...]],
                   after: Mapping[str, tuple[object, ...]]) -> set[str]:
    return {name for name in set(before) | set(after) if before.get(name) != after.get(name)}


PACKAGE_DELTA_PATHS = {
    "test_p001_csv_content_cell_tamper": (f"results/{NAMES[1]}",),
    "test_p002_csv_header_token_tamper": (f"results/{NAMES[0]}",),
    "test_p003_csv_header_reorder": (f"results/{NAMES[0]}",),
    "test_p004_csv_header_width": (f"results/{NAMES[8]}",),
    "test_p005_csv_row_reorder": (f"results/{NAMES[0]}",),
    "test_p006_duplicate_row_id": (f"results/{NAMES[0]}",),
    "test_p007_csv_row_deleted": (f"results/{NAMES[1]}",),
    "test_p008_csv_row_inserted": (f"results/{NAMES[1]}",),
    "test_p009_stale_file_row_count": (f"results/{NAMES[8]}",),
    "test_p010_stale_file_column_count": (f"results/{NAMES[8]}",),
    "test_p011_stale_file_negative_count": (f"results/{NAMES[8]}",),
    "test_p012_stale_package_row_total": (f"results/{NAMES[8]}",),
    "test_p013_stale_package_negative_total": (f"results/{NAMES[8]}",),
    "test_p014_missing_csv": (f"results/{NAMES[0]}",),
    "test_p015_extra_csv": ("results/unlisted.csv",),
    "test_p016_extra_non_csv_file": ("results/unlisted.txt",),
    "test_p017_extra_directory": ("results/unlisted",),
    "test_p018_missing_manifest": ("results/manifest.json",),
    "test_p019_manifest_malformed_json": ("results/manifest.json",),
    "test_p020_manifest_artifact_sha_tamper": ("results/manifest.json",),
    "test_p021_manifest_artifact_bytes_tamper": ("results/manifest.json",),
    "test_p022_manifest_artifact_order": ("results/manifest.json",),
    "test_p023_manifest_self_hash_binding": ("results/manifest.json",),
    "test_p024_manifest_proof_binding_injection": ("results/manifest.json",),
    "test_p025_control_design_gate_binding_drift": ("results/manifest.json",),
    "test_p026_paper9_source_binding_drift": ("results/manifest.json",),
    "test_p027_design_lock_digest_drift": ("results/manifest.json",),
    "test_p028_design_review_digest_drift": ("results/manifest.json",),
    "test_p029_implementation_gate_digest_drift": ("results/manifest.json",),
    "test_p030_implementation_file_digest_drift": ("results/manifest.json",),
    "test_p031_unhashed_implementation_path": ("code/unlisted.py",),
    "test_p032_preexisting_dunder_pycache": ("code/__pycache__",),
    "test_p039_symlink_result_entry": (f"results/{NAMES[8]}",),
    "test_p040_hardlink_result_entry": ("outside-seed", f"results/{NAMES[8]}"),
    "test_p041_manifest_unittest_aggregate_tamper": ("results/manifest.json",),
    "test_p042_manifest_copy_count_tamper": ("results/manifest.json",),
}


class TestPackageMutations(ControlCase):
    def _pristine_receipt(self, root: Path, env: Mapping[str, str]) -> dict[str, tuple[object, ...]]:
        before = tree_snapshot(root)
        result = run_verify(root, root/"results", env=env)
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertEqual(before, tree_snapshot(root), msg="pristine verify-only changed isolated copy")
        return before

    def _verify_case(self, mutation: Callable[[Path],None], expected: int,
                     delta_paths: Sequence[str] | None = None) -> None:
        with isolated_copy() as root:
            env = isolated_environment()
            self.assertNotIn("P17_REPRO_ACTIVE", env)
            before = self._pristine_receipt(root, env)
            mutation(root)
            registered = tuple(delta_paths or PACKAGE_DELTA_PATHS[self._testMethodName])
            mutated = tree_snapshot(root)
            self.assertEqual(snapshot_delta(before, mutated), set(registered))
            result=run_verify(root,root/"results",env=env)
            self.assertEqual(result.returncode,expected,msg=result.stderr)
            self.assertEqual(mutated, tree_snapshot(root), msg="verify-only changed mutated isolated copy")

    def test_p001_csv_content_cell_tamper(self): self._verify_case(lambda r: mutate_csv(r,NAMES[1],lambda h,x:x[0].__setitem__("subject_value","X4x[0]")),7)
    def test_p002_csv_header_token_tamper(self):
        def change(root):
            p=root/"results"/NAMES[0]; lines=p.read_bytes().splitlines(keepends=True); lines[0]=lines[0].replace(b"row_id",b"row_identifier",1); p.write_bytes(b"".join(lines))
        self._verify_case(change,7)
    def test_p003_csv_header_reorder(self):
        def change(root):
            p=root/"results"/NAMES[0]; lines=p.read_bytes().splitlines(keepends=True); lines[0]=lines[0].replace(b"row_id,row_family",b"row_family,row_id",1); p.write_bytes(b"".join(lines))
        self._verify_case(change,7)
    def test_p004_csv_header_width(self):
        def change(root):
            header,rows,_=read_csv(root/"results",NAMES[8]); header.remove("notes"); trimmed=[{k:v for k,v in row.items() if k!="notes"} for row in rows]; write_csv(root/"results"/NAMES[8],header,trimmed)
        self._verify_case(change,7)
    def test_p005_csv_row_reorder(self): self._verify_case(lambda r: mutate_csv(r,NAMES[0],lambda h,x:x.__setitem__(slice(0,2),[x[1],x[0]])),7)
    def test_p006_duplicate_row_id(self): self._verify_case(lambda r: mutate_csv(r,NAMES[0],lambda h,x:x[1].__setitem__("row_id","GH-0001")),7)
    def test_p007_csv_row_deleted(self): self._verify_case(lambda r: mutate_csv(r,NAMES[1],lambda h,x:x.pop()),7)
    def test_p008_csv_row_inserted(self):
        def action(h,x): y=dict(x[-1]); y["row_id"]="AO-1521"; x.append(y)
        self._verify_case(lambda r:mutate_csv(r,NAMES[1],action),7)
    def test_p009_stale_file_row_count(self): self._verify_case(lambda r:mutate_csv(r,NAMES[8],lambda h,x:x[0].__setitem__("expected_rows","1661")),7)
    def test_p010_stale_file_column_count(self): self._verify_case(lambda r:mutate_csv(r,NAMES[8],lambda h,x:x[0].__setitem__("expected_columns","16")),7)
    def test_p011_stale_file_negative_count(self): self._verify_case(lambda r:mutate_csv(r,NAMES[8],lambda h,x:x[0].__setitem__("expected_negative_rows","35")),7)
    def test_p012_stale_package_row_total(self): self._verify_case(lambda r:mutate_csv(r,NAMES[8],lambda h,x:x[-1].__setitem__("expected_rows","3435")),7)
    def test_p013_stale_package_negative_total(self): self._verify_case(lambda r:mutate_csv(r,NAMES[8],lambda h,x:x[-1].__setitem__("expected_negative_rows","83")),7)
    def test_p014_missing_csv(self): self._verify_case(lambda r:(r/"results"/NAMES[0]).unlink(),5)
    def test_p015_extra_csv(self): self._verify_case(lambda r:(r/"results/unlisted.csv").write_bytes(b"x\n"),5)
    def test_p016_extra_non_csv_file(self): self._verify_case(lambda r:(r/"results/unlisted.txt").write_bytes(b"x\n"),5)
    def test_p017_extra_directory(self): self._verify_case(lambda r:(r/"results/unlisted").mkdir(),5)
    def test_p018_missing_manifest(self): self._verify_case(lambda r:(r/"results/manifest.json").unlink(),5)
    def test_p019_manifest_malformed_json(self):
        def change(root): p=root/"results/manifest.json"; p.write_bytes(p.read_bytes().replace(b"{",b"[",1))
        self._verify_case(change,8)
    def test_p020_manifest_artifact_sha_tamper(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["artifacts"][0].__setitem__("sha256",flip_hex(m["artifacts"][0]["sha256"]))),8)
    def test_p021_manifest_artifact_bytes_tamper(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["artifacts"][0].__setitem__("bytes",m["artifacts"][0]["bytes"]+1)),8)
    def test_p022_manifest_artifact_order(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["artifacts"].__setitem__(slice(0,2),[m["artifacts"][1],m["artifacts"][0]])),8)
    def test_p023_manifest_self_hash_binding(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m.__setitem__("manifest_sha256","0"*64)),8)
    def test_p024_manifest_proof_binding_injection(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["bindings"].append({"path":"notes/phase2_topos_quantale_proofs.md","bytes":0,"sha256":"f6c7475b854b3d00b37d3e7f2edca8e8f2f15d92d67ae8bbcdcd71be127b3bb1"})),8)
    def test_p025_control_design_gate_binding_drift(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["bindings"][0].__setitem__("sha256",flip_hex(m["bindings"][0]["sha256"]))),6)
    def test_p026_paper9_source_binding_drift(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["bindings"][1].__setitem__("sha256",flip_hex(m["bindings"][1]["sha256"]))),6)
    def test_p027_design_lock_digest_drift(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["bindings"][2].__setitem__("sha256",flip_hex(m["bindings"][2]["sha256"]))),6)
    def test_p028_design_review_digest_drift(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["bindings"][3].__setitem__("sha256",flip_hex(m["bindings"][3]["sha256"]))),6)
    def test_p029_implementation_gate_digest_drift(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["bindings"][4].__setitem__("sha256",flip_hex(m["bindings"][4]["sha256"]))),6)
    def test_p030_implementation_file_digest_drift(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["implementation"][0].__setitem__("sha256",flip_hex(m["implementation"][0]["sha256"]))),6)
    def test_p031_unhashed_implementation_path(self): self._verify_case(lambda r:(r/"code/unlisted.py").write_bytes(b"x\n"),8)
    def test_p032_preexisting_dunder_pycache(self): self._verify_case(lambda r:(r/"code/__pycache__").mkdir(),5)
    def test_p033_preexisting_compiled_bytecode(self):
        for name in ("x.pyc","x.pyo"): self._verify_case(lambda r,n=name:(r/"code"/n).write_bytes(b""),5,(f"code/{name}",))
    def test_p034_preexisting_tool_cache(self):
        for name in (".pytest_cache",".mypy_cache",".ruff_cache"): self._verify_case(lambda r,n=name:(r/"code"/n).mkdir(),5,(f"code/{name}",))
    def test_p035_recursive_entry_environment(self):
        with isolated_copy() as root:
            child_env=isolated_environment(); before=self._pristine_receipt(root,child_env); env=dict(child_env); env["P17_REPRO_ACTIVE"]="1"; self.assertEqual({key for key in set(child_env)|set(env) if child_env.get(key)!=env.get(key)},{"P17_REPRO_ACTIVE"}); self.assertEqual(before,tree_snapshot(root)); result=subprocess.run([str(root/"experiments/reproduce.sh")],cwd=root,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE); self.assertEqual(result.returncode,3); self.assertEqual(before,tree_snapshot(root))
    def test_p036_concurrent_lock_present(self):
        with isolated_copy() as root:
            env=isolated_environment(); before_tree=self._pristine_receipt(root,env); lock=root/"experiments/.p17-control-reproduce.lock"; lock.mkdir(); self.assertEqual(snapshot_delta(before_tree,tree_snapshot(root)),{"experiments/.p17-control-reproduce.lock"}); before=lock.lstat(); mutated=tree_snapshot(root); result=subprocess.run([str(root/"experiments/reproduce.sh")],cwd=root,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE); after=lock.lstat(); self.assertEqual(result.returncode,3); self.assertEqual((before.st_mode,before.st_size,before.st_mtime_ns,before.st_nlink),(after.st_mode,after.st_size,after.st_mtime_ns,after.st_nlink)); self.assertEqual(mutated,tree_snapshot(root))
    def test_p037_verify_only_crlf_no_rewrite(self):
        with isolated_copy() as root:
            env=isolated_environment(); before_tree=self._pristine_receipt(root,env); p=root/"results"/NAMES[8]; p.write_bytes(p.read_bytes().replace(b"\n",b"\r\n")); self.assertEqual(snapshot_delta(before_tree,tree_snapshot(root)),{f"results/{NAMES[8]}"}); before=receipt(p); mutated=tree_snapshot(root); result=run_verify(root,root/"results",env=env); self.assertEqual(result.returncode,7); self.assertEqual(before,receipt(p)); self.assertEqual(mutated,tree_snapshot(root))
    def test_p038_generate_into_nonempty_output(self):
        with isolated_copy() as root:
            env=isolated_environment(); before=self._pristine_receipt(root,env); output=root/"nonempty"; output.mkdir(); (output/"sentinel").write_bytes(b"x\n"); self.assertEqual(snapshot_delta(before,tree_snapshot(root)),{"nonempty","nonempty/sentinel"}); mutated=tree_snapshot(root); result=subprocess.run([sys.executable,"-B",str(root/"code/generate_controls.py"),"--generate","--output-dir",str(output)],cwd=root,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE); self.assertEqual(result.returncode,4); self.assertEqual(mutated,tree_snapshot(root))
    def test_p039_symlink_result_entry(self):
        def change(root): p=root/"results"/NAMES[8]; p.unlink(); p.symlink_to(NAMES[0])
        self._verify_case(change,5)
    def test_p040_hardlink_result_entry(self):
        def change(root):
            p=root/"results"/NAMES[8]; seed=root/"outside-seed"; seed.write_bytes(p.read_bytes()); p.unlink(); os.link(seed,p)
        self._verify_case(change,5)
    def test_p041_manifest_unittest_aggregate_tamper(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["aggregates"].__setitem__("unittest_methods",179)),8)
    def test_p042_manifest_copy_count_tamper(self): self._verify_case(lambda r:mutate_manifest(r,lambda m:m["reproduction"].__setitem__("byte_identical_copies",2)),8)


def parse_cli(argv: Sequence[str]) -> Context:
    if len(argv)!=6 or argv[0]!="--checked-in" or argv[2]!="--fresh-a" or argv[4]!="--fresh-b":
        raise ValueError("usage: test_controls.py --checked-in PATH --fresh-a PATH --fresh-b PATH")
    root=Path(__file__).resolve().parent.parent
    paths=[Path(argv[i]) for i in (1,3,5)]
    if any(path.is_symlink() or not path.is_dir() for path in paths): raise ValueError("all package roots must be existing non-symlink directories")
    return Context(root,paths[0],paths[1],paths[2])


def source_method_count() -> int:
    tree=ast.parse(Path(__file__).read_text("utf-8"))
    return sum(isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and node.name.startswith("test_") for node in ast.walk(tree))


def main(argv: Sequence[str] | None=None) -> int:
    global CTX
    try: CTX=parse_cli(tuple(sys.argv[1:] if argv is None else argv))
    except ValueError as exc: print(str(exc),file=sys.stderr); return 2
    if source_method_count()!=180: print(f"source unittest method count drift: {source_method_count()}",file=sys.stderr); return 10
    suite=unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    if suite.countTestCases()!=180: print(f"runtime unittest method count drift: {suite.countTestCases()}",file=sys.stderr); return 10
    result=unittest.TextTestRunner(verbosity=1).run(suite)
    print("UNITTEST_METHODS=180")
    print(f"UNITTEST_FAILURES={len(result.failures)}")
    print(f"UNITTEST_ERRORS={len(result.errors)}")
    print("EXPECTED_NEGATIVES_DETECTED=84")
    print("NEGATIVE_FAILURES=0" if result.wasSuccessful() else "NEGATIVE_FAILURES=1")
    if result.wasSuccessful():
        if scan_cache(CTX.root) or {p.name for p in CTX.fresh_a.iterdir()}!=set(ALL_NAMES) or {p.name for p in CTX.fresh_b.iterdir()}!=set(ALL_NAMES):
            print("post-test cache/scratch failure",file=sys.stderr); return 10
        return 0
    return 10


if __name__=="__main__": raise SystemExit(main())
