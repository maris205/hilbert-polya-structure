#!/usr/bin/env python3
"""Repaired-hash semantics, strict types, and actual hostile release-write refusal."""
if not __debug__:
    raise RuntimeError("c394 mutation refuses optimized Python")
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from c394_interpolation_checker import check, evaluation, canonical, EVAL

ROOT = Path(__file__).resolve().parents[1]

def main():
    original = json.loads((ROOT/"results/c394_interpolation_evidence.json").read_text())
    check(ROOT/"results/c394_interpolation_evidence.json")
    cases = [
        ("baseline", ["source_commit"], "0"*40),
        ("epoch_bool", ["fixed_epoch"], True),
        ("route_bool_zero", ["route_a", "route_b_invocation_allowed"], 0),
        ("scope_bool_zero", ["scope_flags", "claims_target_zero_match"], 0),
        ("scope_bool_float", ["scope_flags", "invokes_route_b"], 0.0),
        ("route_upgrade", ["route_a", "tuple", 1], "A1_PASS_ANALYTIC"),
        ("overall_upgrade", ["route_a", "overall_verdict"], "ROUTE_A_PROMISING"),
        ("prime_float", ["finite_levels", 0, "p"], 2.0),
        ("parameter_bool", ["finite_levels", 0, "a"], True),
        ("level_bool", ["finite_levels", 0, "N"], True),
        ("radius_bool", ["finite_levels", 0, "shells", 0, "r"], False),
        ("shell_population", ["finite_levels", 3, "shells", 0, "points"], 1),
        ("shell_period", ["finite_levels", 3, "shells", 0, "period"], 1),
        ("shell_cycles", ["finite_levels", 3, "shells", 0, "cycles"], 1),
        ("cycle_length_bool", ["finite_levels", 0, "cycle_histogram", 0, 0], True),
        ("fixed_iterate_bool", ["finite_levels", 0, "fixed_iterates", 0, "n"], True),
        ("fixed_count", ["finite_levels", 0, "fixed_iterates", 0, "points"], 1),
        ("displacement_prime_bool", ["displacements", 0, "p"], True),
        ("displacement_radius_bool", ["displacements", 0, "r"], False),
        ("base_time_bool", ["displacements", 0, "s"], False),
        ("end_time", ["displacements", 0, "t"], 4),
        ("precision_cap", ["displacements", 0, "precision"], 1),
        ("observed_valuation", ["displacements", 0, "observed_valuation"], 99),
        ("difference_coordinate", ["displacements", 0, "difference", 0], 99),
        ("difference_order_bool", ["polynomial_differences", 0, "m"], False),
        ("coefficient_exponent_bool", ["polynomial_differences", 0, "coordinates", 0, 0, 0], False),
        ("coefficient_bool", ["polynomial_differences", 0, "coordinates", 0, 0, 3], True),
        ("coefficient_value", ["polynomial_differences", 2, "coordinates", 0, 0, 3], 999),
        ("factorial_valuation_bool", ["tails", 0, "factorial_valuation"], False),
        ("tail_bound", ["tails", 4, "gauss_valuation_lower_bound"], 0),
        ("dyadic_margin", ["tails", 1, "strict_margins", 0], 0),
        ("zero_parameter_control", ["controls", "zero_parameter", "fixed"], 1),
        ("threshold_control", ["controls", "dyadic_threshold_counterexample", "orbit", 1], 1),
        ("pointwise_control", ["controls", "pointwise_not_coefficientwise", 0, "coefficient_minimum_valuation"], 1),
        ("genuine_periodic_control", ["controls", "genuine_periodic_points"], [[0, 0], [1, 0]]),
        ("origin_derivative", ["controls", "origin_derivative", 0, 0], 2),
        ("clock_promotion", ["controls", "clock_boundary", 1], "finite cycles prove genuine periods"),
    ]
    for flag in original["scope_flags"]:
        cases.append(("flag_"+flag, ["scope_flags", flag], True))
    labels = []
    with tempfile.TemporaryDirectory(prefix="c394-hostile-") as directory:
        temporary = Path(directory)
        path = temporary/"evidence.json"
        def reject(label, raw):
            path.write_text(raw)
            try:
                check(path)
            except (AssertionError, ValueError, KeyError, TypeError, IndexError):
                labels.append(label)
            else:
                raise RuntimeError("hostile payload accepted: "+label)
        for label, keys, value in cases:
            bad = deepcopy(original)
            node = bad
            for key in keys[:-1]:
                node = node[key]
            node[keys[-1]] = value
            assert canonical(bad) != canonical(original), "ineffective attack "+label
            bad.pop("payload_sha256")
            bad["payload_sha256"] = hashlib.sha256(canonical(bad)).hexdigest()
            reject(label, json.dumps(bad))
        for label, edit in (("unknown_root", lambda b: b.update(extra=0)), ("unknown_nested", lambda b: b["finite_levels"][0].update(extra=0)), ("missing_level", lambda b: b["finite_levels"].pop()), ("reordered_displacements", lambda b: b["displacements"].reverse())):
            bad = deepcopy(original)
            edit(bad)
            bad.pop("payload_sha256")
            bad["payload_sha256"] = hashlib.sha256(canonical(bad)).hexdigest()
            reject(label, json.dumps(bad))
        repaired = len(labels)
        raw = json.dumps(original)
        reject("duplicate_json", raw[:-1]+',"candidate_id":"HCS-C394"}')
        reject("nan_json", raw[:-1]+',"extra":NaN}')
        reject("infinity_json", raw[:-1]+',"extra":Infinity}')
        original_yaml = EVAL.read_text()
        evaluation(EVAL)
        def inject(field):
            return original_yaml.rstrip()[:-1]+",\n"+field+"\n}\n"
        variants = [
            ("unknown", inject('"unknown": 0')),
            ("false_to_zero", original_yaml.replace('"claims_target_zero_match": false', '"claims_target_zero_match": 0')),
            ("unquoted_date", original_yaml.replace('"evaluation_date": "2026-09-05"', '"evaluation_date": 2026-09-05')),
            ("duplicate", inject('"candidate_id": "HCS-C394"')),
            ("anchor", original_yaml.replace('"invokes_route_b": false', '"invokes_route_b": &lock false')),
            ("alias", inject('"unknown": *missing')),
            ("merge", inject('"<<": {"unknown": 1}')),
            ("nonstring", inject('1: false')),
            ("promotion", original_yaml.replace('"A1_WEAK"', '"A1_PASS_ANALYTIC"')),
            ("route_b", original_yaml.replace('"route_b_invocation_allowed": false', '"route_b_invocation_allowed": true')),
        ]
        # Minimal copied release tree; its protected manifest must not be touched.
        copied = temporary/"copied-package"
        (copied/"code").mkdir(parents=True)
        target_eval = copied/"evaluations/route_a/HCS-C394/2026-09-05.yaml"
        target_eval.parent.mkdir(parents=True)
        for name in ("c394_interpolation_checker.py", "c394_release_manifest.py"):
            shutil.copy2(ROOT/"code"/name, copied/"code"/name)
        sentinel = copied/"C394_RELEASE_MANIFEST.json"
        sentinel.write_bytes(b"protected-before-refusal\n")
        for label, bad in variants:
            assert bad != original_yaml, "ineffective YAML attack "+label
            target_eval.write_text(bad)
            before = {str(p.relative_to(copied)): p.read_bytes() for p in copied.rglob("*") if p.is_file()}
            proc = subprocess.run([sys.executable, "-B", str(copied/"code/c394_release_manifest.py"), "--write"], capture_output=True, text=True, cwd=temporary)
            assert proc.returncode != 0 and "EVALUATION_REFUSED" in proc.stdout+proc.stderr, "actual write did not refuse at evaluation: "+label
            after = {str(p.relative_to(copied)): p.read_bytes() for p in copied.rglob("*") if p.is_file()}
            assert before == after, "refused write changed files: "+label
            labels.append("yaml_write_"+label)
        target_eval.write_text(original_yaml)
        (copied/"unlisted-link").symlink_to(sentinel)
        before = {str(p.relative_to(copied)): (p.is_symlink(), p.read_bytes()) for p in copied.rglob("*") if p.is_file()}
        proc = subprocess.run([sys.executable, "-B", str(copied/"code/c394_release_manifest.py"), "--write"], capture_output=True, text=True, cwd=temporary)
        assert proc.returncode != 0 and "SYMLINK_REFUSED" in proc.stdout+proc.stderr, "symlink write survived"
        after = {str(p.relative_to(copied)): (p.is_symlink(), p.read_bytes()) for p in copied.rglob("*") if p.is_file()}
        assert before == after, "symlink refusal changed copied files"
        labels.append("actual_symlink_write_refusal")
    print("C394 hostile PASS: "+json.dumps({"repaired_hash": repaired, "strict_json": 3, "actual_yaml_write_refusals": 10, "actual_symlink_write_refusals": 1, "rejected": len(labels), "total": len(labels), "names": labels}, sort_keys=True))

if __name__ == "__main__":
    main()
