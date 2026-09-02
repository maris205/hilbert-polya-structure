#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for the independent C308 checker."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("C308 mutation lane requires assertions; python -O is forbidden")

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c308_hatano_nelson_checker.py"
EVIDENCE = ROOT / "results/c308_hatano_nelson_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C308/2026-09-03.yaml"


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def run(evidence: Path, evaluation: Path) -> bool:
    completed = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(evidence), "--evaluation", str(evaluation)], capture_output=True, text=True)
    return completed.returncode != 0


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    yaml_raw = EVALUATION.read_text()
    mutations = []

    def semantic(name, change, repair=True):
        value = copy.deepcopy(pristine); change(value)
        if repair:
            value["payload_sha256"] = payload_hash(value)
        mutations.append((name, json.dumps(value, sort_keys=True, indent=2) + "\n", yaml_raw))

    semantic("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    semantic("extra_top", lambda x: x.__setitem__("extra", 1))
    semantic("bool_epoch", lambda x: x.__setitem__("fixed_epoch", True))
    semantic("float_epoch", lambda x: x.__setitem__("fixed_epoch", 1788393600.0))
    semantic("model_formula", lambda x: x["model"].__setitem__("obc", "wrong"))
    semantic("condition_formula", lambda x: x["theorem_contract"].__setitem__("condition_number", "wrong"))
    semantic("route_verdict", lambda x: x["route_a"].__setitem__("overall", "PASS"))
    semantic("forbidden_flag", lambda x: x["scope_flags"].__setitem__("claims_topological_invariant", True))
    semantic("collision_value", lambda x: x["collision_boundary"].__setitem__("C267", "wrong owner"))
    semantic("reference_id", lambda x: x["references"][0].__setitem__("identifier", "wrong"))
    semantic("bool_N", lambda x: x["positive_obc_rows"][0].__setitem__("N", True))
    semantic("float_N", lambda x: x["positive_obc_rows"][0].__setitem__("N", 2.0))
    semantic("positive_extra_key", lambda x: x["positive_obc_rows"][0].__setitem__("extra", 0))
    semantic("char_truncate", lambda x: x["positive_obc_rows"][0]["characteristic_coefficients_descending"].pop())
    semantic("fraction_noncanonical", lambda x: x["positive_obc_rows"][0].__setitem__("t_R", "2/2"))
    semantic("char_value", lambda x: x["positive_obc_rows"][0]["characteristic_coefficients_descending"].__setitem__(0, "2/1"))
    semantic("kappa_value", lambda x: x["positive_obc_rows"][1].__setitem__("kappa2_squared", "1/1"))
    semantic("duplicate_positive_case", lambda x: x["positive_obc_rows"].__setitem__(1, copy.deepcopy(x["positive_obc_rows"][0])))
    semantic("resolvent_z", lambda x: x["resolvent_rows"][0].__setitem__("z", "1/1"))
    semantic("resolvent_trace", lambda x: x["resolvent_rows"][0].__setitem__("trace_resolvent", "0/1"))
    semantic("one_orientation", lambda x: x["one_sided_rows"][0].__setitem__("orientation", "up"))
    semantic("rank_bool", lambda x: x["one_sided_rows"][0]["rank_sequence_H_power_0_through_N"].__setitem__(0, True))
    semantic("rank_truncate", lambda x: x["one_sided_rows"][0]["rank_sequence_H_power_0_through_N"].pop())
    semantic("nilpotency_bool", lambda x: x["one_sided_rows"][0].__setitem__("nilpotency_index", True))
    semantic("pbc_bool_N", lambda x: x["pbc_rows"][0].__setitem__("N", True))
    semantic("pbc_extra_row", lambda x: x["pbc_rows"].append(copy.deepcopy(x["pbc_rows"][0])))
    semantic("pbc_trace", lambda x: x["pbc_rows"][0]["trace_powers_1_through_N"].__setitem__(0, "1/1"))
    semantic("pbc_normal", lambda x: x["pbc_rows"][0].__setitem__("normal", False))
    semantic("boundary_warning", lambda x: x["boundary_rows"][4].__setitem__("warning", "wrong"))
    semantic("summary_bool", lambda x: x["summary"].__setitem__("audited_rows", True))
    semantic("summary_count", lambda x: x["summary"].__setitem__("audited_rows", 122))
    semantic("nonclaim", lambda x: x["nonclaims"].__setitem__(1, "topology asserted"))
    semantic("stale_payload_hash", lambda x: x.__setitem__("candidate_id", "stale"), repair=False)

    raw = EVIDENCE.read_text()
    mutations.append(("duplicate_json_key", raw.replace('"candidate_id": "HCS-C308",', '"candidate_id": "HCS-C308",\n  "candidate_id": "HCS-C308",', 1), yaml_raw))
    mutations.append(("json_nan", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw))
    mutations.append(("json_top_list", "[]\n", yaml_raw))

    def yaml_case(name, replacement):
        altered = replacement(yaml_raw)
        value = copy.deepcopy(pristine)
        value["evaluation_file_sha256"] = hashlib.sha256(altered.encode()).hexdigest()
        value["payload_sha256"] = payload_hash(value)
        mutations.append((name, json.dumps(value, sort_keys=True, indent=2) + "\n", altered))

    yaml_case("yaml_duplicate", lambda s: s.replace("candidate_id: HCS-C308", "candidate_id: HCS-C308\ncandidate_id: HCS-C308", 1))
    yaml_case("yaml_anchor_alias", lambda s: s.replace("candidate_id: HCS-C308", "candidate_id: &cid HCS-C308\ntitle_alias: *cid", 1))
    yaml_case("yaml_merge", lambda s: s.replace("schema: route-a-evaluation-v0.2.0", "base: &base {x: 1}\n<<: *base\nschema: route-a-evaluation-v0.2.0", 1))
    yaml_case("yaml_bool_epoch", lambda s: s.replace("fixed_epoch: 1788393600", "fixed_epoch: true", 1))
    yaml_case("yaml_extra_key", lambda s: s + "extra_top: false\n")
    yaml_case("yaml_overall", lambda s: s.replace("overall_verdict: ROUTE_A_REJECTED", "overall_verdict: PASS", 1))
    # Stale YAML-hash control: changed YAML, untouched evidence.
    mutations.append(("stale_evaluation_hash", EVIDENCE.read_text(), yaml_raw.replace("overall_verdict: ROUTE_A_REJECTED", "overall_verdict: PASS", 1)))

    passed = 0
    with tempfile.TemporaryDirectory(prefix="c308-mutation-") as tmp:
        for index, (name, evidence_raw, evaluation_raw) in enumerate(mutations):
            ep = Path(tmp) / f"e{index}.json"; yp = Path(tmp) / f"y{index}.yaml"
            ep.write_text(evidence_raw); yp.write_text(evaluation_raw)
            if not run(ep, yp):
                raise AssertionError(f"surviving mutation: {name}")
            passed += 1
    print(f"C308 hostile mutation suite: PASS ({passed}/{len(mutations)} rejected; repaired-hash semantic, parser, and stale-hash controls)")


if __name__ == "__main__":
    main()
