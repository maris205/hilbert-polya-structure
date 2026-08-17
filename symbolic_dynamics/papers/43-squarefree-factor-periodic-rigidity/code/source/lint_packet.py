#!/usr/bin/env python3
"""Read-only structural linter for the Paper 43 raw packet.

The linter deliberately does not import the producer or either scientific
evaluator.  It checks the packet boundary, canonical serialization, exact
raw section bindings, portable paths, and the absence of derived answers.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import PurePosixPath
from typing import Any


TOP = (
    "candidate_contract", "claim_question", "control_grid",
    "factor_axiom_schema", "finite_p0_inputs", "integration_chronology",
    "literature_boundary_contract", "marker_contract", "operator_contract",
    "portable_source_input", "raw_route_contract", "raw_selection_cards",
    "schema", "selection_adapter_contract", "source_axiom_schema",
    "source_fixture_inputs", "terminal_contract", "type_ledger",
    "writer_sync_contract",
)
FORBIDDEN_KEYS = {
    "all_pass", "eligible", "expected_tuple", "gate_count", "output_count",
    "pass", "route_tuple", "survivor", "winner",
}
FORBIDDEN_VALUE_FRAGMENTS = tuple("/" + name + "/" for name in ("root", "tmp", "home")) \
    + ("TMP" + "_", "ROUTE_A_REJECTED")
SECTION_SHA256 = {
    "candidate_contract": "0161f6e46cb1f73ae8a2927bd145f1df8909fcb85a268dfb56bbba07fc9bfb57",
    "claim_question": "5bed6f938a1baf72a77d73c5e50ea7d1c11f116d4db922faae434341ac029abf",
    "control_grid": "bdfd5e1d0e7d5a7817636294dfbf7a082b5b7ce5f7e730f301119803273e31d4",
    "factor_axiom_schema": "0c23e45de89a595904e13e6648128cb1586bcb5077af65bb47ca17813a27f045",
    "finite_p0_inputs": "5d4a47893d39a11d584053414b4cd6e49375f964bc40b10144cc9c9845380089",
    "integration_chronology": "ea4cfc7e6a0a345ecd33823037e570500e1a1d1434e063a7d0328c3607b4dd1f",
    "literature_boundary_contract": "801bcba42c429342f7ac10a27fa5c9b4e381cd415ed9e447cfa5a52b17b1b87b",
    "marker_contract": "f2d529f80cdb90e866b64d36af5a0c7f5ca4ca879e0be4c490bb66e6b145d7f5",
    "operator_contract": "15624a07bc69fc8b8c32f57417eef682606d837297e5937843d5b7ba0d60da41",
    "portable_source_input": "3f504149e98b2c7eb06cc52a7863ed3f04c3689bd07948727acae124dcfc7bb0",
    "raw_route_contract": "e5f22a6bbe19f2e196b822ccd252c9276682daaadf2deecb2d55006b9acf72ca",
    "raw_selection_cards": "79d21c8f5067b43f9a74e8ecd5ed5e72b241d070a17245485df583dbb1e1b183",
    "schema": "7d5446c5a88ca086be0a3783596b8c55969a6502098ee756982fd67c4d2715c9",
    "selection_adapter_contract": "f84f273628c90261c2e8663607dd2de82df8451ec9601aebbe7fd09cf0b13223",
    "source_axiom_schema": "102a5c3dfd183a110289fac2c938bf987e2b770f05072031c348eb2b160899af",
    "source_fixture_inputs": "10fea290cd948cc8f9f078bd24c6a64b37223edf88c5b585128e9ebcb917d1c8",
    "terminal_contract": "2fc031b7df1f5370f267752e4ed0702c1aef3f9041ba9b5a81d1830a62c9901b",
    "type_ledger": "1fbc93d49548a4bb569a5b60ab2d7503bc82f8085d31f70e0a344da3db44dfb4",
    "writer_sync_contract": "748ec3d5e5e37ba3481c739f7200599ef2cf7e63b04c290a9f2ef8c2790c740f",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def walk(value: Any, path: str = "") -> None:
    if type(value) is dict:
        for key, child in value.items():
            if key in FORBIDDEN_KEYS:
                raise ValueError(f"derived answer key forbidden: {path}/{key}")
            walk(child, f"{path}/{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            walk(child, f"{path}/{index}")
    elif type(value) is float:
        raise ValueError(f"float forbidden: {path}")
    elif type(value) is str:
        if any(fragment in value for fragment in FORBIDDEN_VALUE_FRAGMENTS):
            raise ValueError(f"derived answer or host path forbidden: {path}")
    elif value is not None and type(value) not in (bool, int):
        raise ValueError(f"unsupported scalar: {path}")


def safe(path: str) -> bool:
    if type(path) is not str or not path or "\\" in path:
        return False
    pure = PurePosixPath(path)
    return not pure.is_absolute() and ".." not in pure.parts and "." not in pure.parts


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        raise SystemExit("usage: lint_packet.py PACKET.json")
    raw = open(argv[0], "rb").read()
    packet = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if canonical(packet) != raw:
        raise ValueError("packet is not canonical ASCII JSON")
    if tuple(sorted(packet)) != TOP:
        raise ValueError("packet exact top-level set/order vocabulary failure")
    if packet["schema"] != "paper43-squarefree-factor-raw-packet-v1":
        raise ValueError("packet schema failure")
    walk(packet)
    for key in TOP:
        actual = hashlib.sha256(canonical(packet[key])).hexdigest()
        if actual != SECTION_SHA256[key]:
            raise ValueError(f"raw section hash mismatch: {key}")
    entries = packet["portable_source_input"]["entries"]
    ids = [row["id"] for row in entries]
    if any(set(row) != {"container_sha256", "decoded_sha256", "id",
                        "relative_container"} for row in entries):
        raise ValueError("portable source row shape failure")
    paths = [row["relative_container"] for row in entries]
    if len(entries) != 40 or ids != sorted(ids) or len(ids) != len(set(ids)):
        raise ValueError("portable source ID exact-set/order failure")
    if len(paths) != len(set(paths)) or not all(safe(path) for path in paths):
        raise ValueError("portable source path failure")
    if any(re.fullmatch(r"[0-9a-f]{64}", row["container_sha256"]) is None
           or re.fullmatch(r"[0-9a-f]{64}", row["decoded_sha256"]) is None
           for row in entries):
        raise ValueError("portable source hash syntax failure")
    result = {
        "checks": {
            "canonical_ascii_json": True,
            "derived_answers_absent": True,
            "duplicate_keys_rejected": True,
            "exact_raw_section_hashes": True,
            "exact_top_level_schema": True,
            "floats_absent": True,
            "host_paths_absent": True,
            "portable_source_set_safe": True,
        },
        "checks_passed": 8,
        "checks_total": 8,
        "packet_sha256": hashlib.sha256(raw).hexdigest(),
        "schema": "paper43-raw-packet-lint-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
