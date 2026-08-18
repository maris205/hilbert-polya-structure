#!/usr/bin/env python3
"""Verify and extract the sealed P45 result projection used by the paper."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED = {
    "SHA256SUMS.txt": "2fae66ff866b63e7119fce7b86c928f589570572728cae942d758f4e599ad734",
    "comparator_x.json": "6a8404c802342e9ea37fc311ecb23492f2503fa7137258a46b416aafaaee12c5",
    "evaluation_report.json": "4c5efa633213cd6f056b550c562dbf9929b3a7145aae33149b482ecd3fec0b5b",
    "evaluator_a.json": "ba3f374f1e65e3598c7d4e769144514e911f5be268ae36afc90000df5a5154da",
    "evaluator_b.json": "ac8226e8d9a726ebf78e753d66b19e200ba382a5ecdc926ff79a262c7c81a675",
    "integrity_audit.json": "fef14966637e160367f545e7c6ee9f53399c6f3de3f6a01b74614ac3bff94c9b",
    "mutation_outcomes.json": "8042263d0ddd43b3b2c8c27737c10a053b422e1dfbf9667f292a4b5bba4f147b",
    "proof_auditor_p.json": "1a62f35af5b7147599d23139231f17443c14970612ac115387a484b84b60ce4d",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authority-root", required=True, type=Path)
    parser.add_argument("--json-out", required=True, type=Path)
    parser.add_argument("--tex-out", required=True, type=Path)
    args = parser.parse_args()

    result_root = args.authority_root / "results"
    actual = {name: sha256(result_root / name) for name in EXPECTED}
    if actual != EXPECTED:
        mismatches = {
            name: {"expected": EXPECTED[name], "actual": actual.get(name)}
            for name in EXPECTED
            if actual.get(name) != EXPECTED[name]
        }
        raise SystemExit(f"sealed input mismatch: {json.dumps(mismatches, sort_keys=True)}")

    a = load_json(result_root / "evaluator_a.json")
    b = load_json(result_root / "evaluator_b.json")
    p = load_json(result_root / "proof_auditor_p.json")
    x = load_json(result_root / "comparator_x.json")
    report = load_json(result_root / "evaluation_report.json")
    mutations = load_json(result_root / "mutation_outcomes.json")
    integrity = load_json(result_root / "integrity_audit.json")

    primorial_a = [
        row for row in a["finite_records"]
        if row["case_id"] == "FIN-PRIMORIAL-H3-THREE-REGIMES"
    ]
    primorial_b = [
        row for row in b["finite_records"]
        if row["case_id"] == "FIN-PRIMORIAL-H3-THREE-REGIMES"
    ]
    if primorial_a != primorial_b or len(primorial_a) != 3:
        raise SystemExit("finite primorial projections are not exact A/B triples")

    if not (
        len(a["finite_records"]) == 21
        and len(a["infinite_records"]) == 0
        and len(b["finite_records"]) == 21
        and len(b["infinite_records"]) == 15
        and len(p["per_case_audits"]) == 15
        and p["findings"] == []
        and p["verdict"] == "PASS"
        and x["exact_mismatch_count"] == 0
        and x["interval_mismatch_count"] == 0
        and x["verdict"] == "PASS"
        and report["c1"] == "PASS"
        and report["c2"] == "PASS"
        and len(mutations["outcomes"]) == 168
        and integrity["verdict"] == "PASS"
        and integrity["second_run_zero_replacements"] is True
        and integrity["late_failure_identity_verified"] is True
    ):
        raise SystemExit("canonical result envelope failed")

    survivor_count = sum(row.get("outcome") != "REJECT" for row in mutations["outcomes"])
    rejection_codes = sorted({
        row["rejection_code"] for row in mutations["outcomes"]
        if "rejection_code" in row
    })
    if survivor_count != 0 or len(rejection_codes) != 75:
        raise SystemExit("mutation envelope failed")

    summary = {
        "schema": "paper45.writer-canonical-summary.v1",
        "source_sha256": EXPECTED,
        "contract_sha256": a["contract_sha256"],
        "infinite_case_set_sha256": a["declared_infinite_case_set_sha256"],
        "counts": {
            "a_finite": len(a["finite_records"]),
            "a_infinite": len(a["infinite_records"]),
            "b_finite": len(b["finite_records"]),
            "b_infinite": len(b["infinite_records"]),
            "p_audits": len(p["per_case_audits"]),
            "x_case_ids": len(x["finite_case_ids"]),
            "x_exact_mismatches": x["exact_mismatch_count"],
            "x_interval_mismatches": x["interval_mismatch_count"],
            "physical_mutation_outcomes": len(mutations["outcomes"]),
            "registered_rejection_codes": len(rejection_codes),
            "mutation_survivors": survivor_count,
        },
        "verdicts": {
            "c1": report["c1"],
            "c2": report["c2"],
            "p": p["verdict"],
            "x": x["verdict"],
            "integrity": integrity["verdict"],
        },
        "primorial_rows": primorial_a,
        "infinite_case_ids": b["infinite_case_ids"],
    }

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(summary, sort_keys=True, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "% Generated by scripts/extract_canonical_results.py; do not edit.",
        "\\begin{tabular}{@{}ccrrl@{}}",
        "\\toprule",
        "$\\sigma$ & cutoff $x$ & maximizer & primorial label & ties \\\\",
        "\\midrule",
    ]
    for row in primorial_a:
        ties = ", ".join(row["tie_labels"])
        lines.append(
            f"${row['sigma']}$ & {row['x_cutoff']} & {row['maximizer_label']} & "
            f"{row['primorial_label']} & {ties} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    args.tex_out.parent.mkdir(parents=True, exist_ok=True)
    args.tex_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

