#!/usr/bin/env python3
"""Read-only final audit for Round 10 / Papers 29--33 / ARS Stage 3.

The script replays the official ARS validators, checks all frozen inputs, and
verifies the exact transport topology of the standalone roadmap, Schema-6
package, and provenance carrier.  It intentionally does not authorize or
perform Stage-4 manuscript changes.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
CONTRACT = ROOT / "BATCH_ROUND10_STAGE3_SPRINT_CONTRACT.json"

PAPERS = {
    "P29": {
        "dir": "29-bianchi-ideal-owner-refinement",
        "canonical": {
            "paper/manuscript.tex": "5bee689a055f99819fb6df1f6e992610fe0dea7ebffc87219758116bf06bd034",
            "paper/references.bib": "c78ea003596e5c27fb1332643db2654dd6a67f96b9ba25b923cd2af655540555",
            "paper/paper.pdf": "14dd360e0152da9c976c88bfe3ca197449017d49e09ea75279d4099457f1044e",
            "notes/stage3_revision_base.tex": "8b9352de028c2eeb9a93b4e8abbb44d25be145282778e18a95618283fe51cf50",
            "notes/stage3_revision_base.block-manifest.json": "798d8fd01bf1e432825d374021f0c49bf5ce25dea21ea4e92416a5a33530d478",
            "notes/stage3_review_panel_provenance.json": "19b65e9633e0c3192302fea81612635356f10b7460591538f1e11cc2b206641a",
            "notes/stage3_review_panel_provenance_carrier.json": "c7106c8b49bf95ca64cdf189eb7b50a24c71283b7b90ac6c5b9deb886e536a20",
        },
        "weaknesses": 12,
        "roadmap_items": 11,
        "obligations": {"must_fix": 5, "should_fix": 6, "consider": 0},
        "dimensions": "[D1=warn, D2=warn, D3=warn, D4=warn, D5=warn, D6=block]",
    },
    "P30": {
        "dir": "30-three-disk-nonconstant-roof-determinant",
        "canonical": {
            "paper/manuscript.tex": "af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506",
            "paper/references.bib": "1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f",
            "paper/paper.pdf": "c8f54cf535ca1fa12a14662a248889b332c8a3b0c5b4db6d7abae707827f313e",
            "notes/stage3_revision_base.tex": "5c5d363184749528be1fcc637ab128d33478006311b08e5591caabaea7bf94b4",
            "notes/stage3_revision_base.block-manifest.json": "c660ed68c2078f2df16256a587fc8b0b21c40774af7d740ec74d8015e60efd3f",
            "notes/stage3_review_panel_provenance.json": "3b609c217252545229f7641455502effaa678c3417d3313b077ed35aeca39890",
            "notes/stage3_review_panel_provenance_carrier.json": "6ae7ae98d2502a2cb64b6c7d7b6eda37ccb281b7b4dcbb9726df0a69bca5c629",
        },
        "weaknesses": 13,
        "roadmap_items": 9,
        "obligations": {"must_fix": 8, "should_fix": 1, "consider": 0},
        "dimensions": "[D1=warn, D2=warn, D3=warn, D4=warn, D5=warn, D6=block]",
    },
    "P31": {
        "dir": "31-level11-conjugacy-owner-ledger",
        "canonical": {
            "paper/manuscript.tex": "f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a",
            "paper/references.bib": "b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958",
            "paper/paper.pdf": "f40a230291ea432d44b197e005d333147a21fc3f9c3a24f2444e4d2ec90d7722",
            "notes/stage3_revision_base.tex": "028746b57b86e8fc2c57cee864cc225efb380c807c7971b55acdc81254ad09f0",
            "notes/stage3_revision_base.block-manifest.json": "dd2095b26ce89f2c1196d16f5eb1a6904011ee34a54682e8f3cfde0162d47d86",
            "notes/stage3_review_panel_provenance.json": "0a5cdae92e3165c19cac5213acd0bb9a01ee8255b894af2cd91fc48001370027",
            "notes/stage3_review_panel_provenance_carrier.json": "0e2763241aa0f64ede657e58d9e6fafb46fc5a52c63007ec2786a8111bacfbac",
        },
        "weaknesses": 13,
        "roadmap_items": 11,
        "obligations": {"must_fix": 11, "should_fix": 0, "consider": 0},
        "dimensions": "[D1=warn, D2=warn, D3=block, D4=warn, D5=warn, D6=block]",
    },
    "P32": {
        "dir": "32-homology-cover-renormalization-uniformity",
        "canonical": {
            "paper/manuscript.tex": "4a3e1f084dc1e27005479971299fd9da67bb6c817278d5de0de6cf03cbc8000a",
            "paper/references.bib": "e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9",
            "paper/paper.pdf": "66948e247c72a3388a7f3da1f80be1d74860afa1261c99fb18c85e2b8bb84f93",
            "notes/stage3_revision_base.tex": "9b4006823a9ca59bc1fb8856133570430e9d0bbf915a01f99298f027b0a032e8",
            "notes/stage3_revision_base.block-manifest.json": "2b90bd63c20f5cfd081d6ec4a38d55767eddd90e6d507a8b2a13a814e1b1e4d1",
            "notes/stage3_review_panel_provenance.json": "267b1303921eca3c48165320fd1963d452ad81c90acfd8f9bb2545fdb0b5ef03",
            "notes/stage3_review_panel_provenance_carrier.json": "7223e30006f72cced16a4c73536cd4eff90d0fa052e769be5d3335a47340a498",
        },
        "weaknesses": 13,
        "roadmap_items": 12,
        "obligations": {"must_fix": 7, "should_fix": 5, "consider": 0},
        "dimensions": "[D1=warn, D2=warn, D3=block, D4=warn, D5=warn, D6=block]",
    },
    "P33": {
        "dir": "33-bolza-control-matched-census",
        "canonical": {
            "paper/manuscript.tex": "b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3",
            "paper/references.bib": "12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0",
            "paper/paper.pdf": "487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031",
            "notes/stage3_revision_base.tex": "4b6e8ed908df0aad7b58cd22829a669b24b4a2a42cf715c535f977f74e222250",
            "notes/stage3_revision_base.block-manifest.json": "61899cac0d700875e0d96eca2c42fb5a88d056e64eff4b4d250735140bec5234",
            "notes/stage3_review_panel_provenance.json": "82a5cf6d8048524757951390685a234a4a5f8df2edd9a4047b5ab93711a52290",
            "notes/stage3_review_panel_provenance_carrier.json": "5a20acf494a834011289678c970f085f7c3fca838315d17cd55b29191f0adb6e",
        },
        "weaknesses": 15,
        "roadmap_items": 13,
        "obligations": {"must_fix": 7, "should_fix": 6, "consider": 0},
        "dimensions": "[D1=warn, D2=warn, D3=warn, D4=warn, D5=warn, D6=block]",
    },
}

REPORT_FILES = [
    "stage3_phase2_eic.md",
    "stage3_phase2_methodology.md",
    "stage3_phase2_domain.md",
    "stage3_phase2_perspective.md",
    "stage3_phase2_da.md",
]
PHASE1_FILES = [
    "stage3_phase1_eic.md",
    "stage3_phase1_methodology.md",
    "stage3_phase1_domain.md",
    "stage3_phase1_perspective.md",
    "stage3_phase1_da.md",
]
ROLES = "eic,methodology,domain,perspective,da"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run(command: list[str]) -> tuple[bool, str]:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    return proc.returncode == 0, output


def find_forbidden_keys(value: object, trail: tuple[str, ...] = ()) -> list[str]:
    hits: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {
                "recommendation",
                "recommended_decision",
                "acceptance_recommendation",
                "author_triage",
                "work_order",
                "execution_authorization",
            }:
                hits.append("/".join((*trail, key)))
            hits.extend(find_forbidden_keys(child, (*trail, key)))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            hits.extend(find_forbidden_keys(child, (*trail, str(index))))
    return hits


def main() -> int:
    failures: list[str] = []
    results: dict[str, object] = {}
    phase2_receipt = json.loads(
        (ROOT / "BATCH_ROUND10_STAGE3_PHASE2_VALIDATION.json").read_text()
    )
    phase1_receipt = json.loads(
        (ROOT / "BATCH_ROUND10_STAGE3_PHASE1_VALIDATION.json").read_text()
    )
    phase1_hashes = {
        row["paper_id"]: row["phase1"] for row in phase1_receipt["papers"]
    }
    receipt_hashes = {
        row["paper_id"]: row["phase2_sha256"] for row in phase2_receipt["papers"]
    }

    for paper_id, spec in PAPERS.items():
        paper = ROOT / "papers" / spec["dir"]
        notes = paper / "notes"
        local: dict[str, object] = {"checks": []}

        for relpath, expected in spec["canonical"].items():
            actual = digest(paper / relpath)
            if actual != expected:
                failures.append(f"{paper_id}: frozen hash mismatch {relpath}: {actual}")
        local["checks"].append("frozen_hashes")

        phase1_paths = [notes / name for name in PHASE1_FILES]
        phase1_role_names = ["eic", "methodology", "domain", "perspective", "da"]
        for role, path in zip(phase1_role_names, phase1_paths, strict=True):
            actual = digest(path)
            expected = phase1_hashes[paper_id][role]
            if actual != expected:
                failures.append(f"{paper_id}: Phase-1 {role} hash mismatch: {actual}")
            text = path.read_text()
            if "criteria_binding_unavailable" not in text:
                failures.append(f"{paper_id}: Phase-1 {role} lacks binding literal")
            if not text.rstrip().endswith("[CONTRACT-ACKNOWLEDGED]"):
                failures.append(f"{paper_id}: Phase-1 {role} lacks final contract ACK")
        local["checks"].append("phase1_hash_binding_and_ack_replay")

        phase2_paths = [notes / name for name in REPORT_FILES]
        receipt_role_names = ["eic", "methodology", "domain", "perspective", "da"]
        for role, path in zip(receipt_role_names, phase2_paths, strict=True):
            actual = digest(path)
            expected = receipt_hashes[paper_id][role]
            if actual != expected:
                failures.append(f"{paper_id}: Phase-2 {role} hash mismatch: {actual}")
            text = path.read_text()
            if "criteria_binding_unavailable" not in text:
                failures.append(f"{paper_id}: Phase-2 {role} lacks binding literal")
        local["checks"].append("phase2_hash_and_binding_replay")

        synthesis = notes / "stage3_editorial_synthesis.md"
        command = [
            sys.executable,
            str(ARS / "scripts/check_panel_synthesis.py"),
            "--contract",
            str(CONTRACT),
        ]
        for path in phase2_paths:
            command.extend(["--report", str(path)])
        command.extend(["--roles", ROLES, "--synthesis", str(synthesis)])
        passed, output = run(command)
        if not passed or "PANEL-SYNTHESIS: PASS" not in output:
            failures.append(f"{paper_id}: panel synthesis validator failed: {output}")
        local["checks"].append("official_panel_synthesis")

        layer_command = [
            sys.executable,
            str(ARS / "scripts/check_panel_synthesis.py"),
            "--contract",
            str(CONTRACT),
        ]
        for path in phase2_paths:
            layer_command.extend(["--report", str(path)])
        layer_command.extend(["--roles", ROLES, "--layer1-only"])
        passed, output = run(layer_command)
        if not passed or "LAYER1-ONLY: PASS" not in output:
            failures.append(f"{paper_id}: layer-1 validator failed: {output}")
        local["checks"].append("official_layer1")

        roadmap_path = notes / "stage3_revision_roadmap.json"
        package_path = notes / "stage3_review_package.json"
        carrier_path = notes / "stage3_review_panel_provenance_carrier.json"
        roadmap = json.loads(roadmap_path.read_text())
        package = json.loads(package_path.read_text())
        carrier = json.loads(carrier_path.read_text())

        passed, output = run(
            [
                sys.executable,
                str(ARS / "scripts/revision_roadmap.py"),
                "validate-roadmap",
                str(roadmap_path),
                "--base",
                str(notes / "stage3_revision_base.tex"),
                "--block-manifest",
                str(notes / "stage3_revision_base.block-manifest.json"),
            ]
        )
        if not passed or "revision roadmap ok" not in output:
            failures.append(f"{paper_id}: roadmap validator failed: {output}")
        local["checks"].append("official_roadmap_replay")

        passed, output = run(
            [
                sys.executable,
                str(ARS / "scripts/review_panel_provenance.py"),
                "validate-schema6",
                str(package_path),
                "--mode",
                "reviewer_full",
                "--artifact-root",
                str(paper),
            ]
        )
        if not passed or "PASS" not in output:
            failures.append(f"{paper_id}: Schema-6 validator failed: {output}")
        local["checks"].append("official_schema6_replay")

        if package.get("revision_roadmap") != roadmap:
            failures.append(f"{paper_id}: embedded roadmap differs from standalone")
        if package.get("review_panel_provenance") != carrier:
            failures.append(f"{paper_id}: embedded provenance differs from carrier")
        local["checks"].append("embedded_deep_equality")

        items = roadmap.get("items", [])
        source_refs = [
            (ref["seat"], ref["channel"], ref["ordinal"], ref["subclaim_ordinal"])
            for item in items
            for ref in item.get("source_refs", [])
        ]
        reports = {row["reviewer_id"]: row for row in package["reviewer_reports"]}
        expected_ref_triples = {
            (seat, "finding", ordinal)
            for seat, report in reports.items()
            for ordinal in range(1, len(report.get("weaknesses", [])) + 1)
        }
        if len(items) != spec["roadmap_items"]:
            failures.append(f"{paper_id}: roadmap item count {len(items)}")
        if len(source_refs) != spec["weaknesses"] or len(set(source_refs)) != len(source_refs):
            failures.append(f"{paper_id}: source-ref count/uniqueness failure")
        actual_ref_triples = {(seat, channel, ordinal) for seat, channel, ordinal, _ in source_refs}
        if actual_ref_triples != expected_ref_triples:
            failures.append(f"{paper_id}: source-ref set differs from all package weaknesses")
        obligations = Counter(item["obligation_class"] for item in items)
        normalized_obligations = {
            key: obligations.get(key, 0) for key in ("must_fix", "should_fix", "consider")
        }
        if normalized_obligations != spec["obligations"]:
            failures.append(
                f"{paper_id}: obligation counts {normalized_obligations} != {spec['obligations']}"
            )
        if package.get("editorial_decision") != "Major Revision":
            failures.append(f"{paper_id}: editorial decision is not Major Revision")
        if package.get("consensus") != "SPLIT":
            failures.append(f"{paper_id}: consensus is not SPLIT")
        if package.get("calibration_status") != "NOT_CALIBRATED":
            failures.append(f"{paper_id}: calibration is not NOT_CALIBRATED")
        if len(package.get("reviewer_reports", [])) != 5:
            failures.append(f"{paper_id}: reviewer report count is not five")
        if any(len(report.get("criterion_judgements", [])) != 6 for report in reports.values()):
            failures.append(f"{paper_id}: a reviewer report lacks six criterion rows")
        forbidden = find_forbidden_keys(package)
        if forbidden:
            failures.append(f"{paper_id}: forbidden authority/recommendation keys: {forbidden}")
        local["checks"].append("source_coverage_and_authority_boundary")

        synthesis_text = synthesis.read_text()
        required_lines = [
            f"dimension_verdicts: {spec['dimensions']}",
            "fired_conditions: [F2, F3, F5]",
            "da_critical_adjudications: []",
            "editorial_decision=major_revision",
        ]
        for line in required_lines:
            if line not in synthesis_text:
                failures.append(f"{paper_id}: synthesis lacks exact audit line {line!r}")
        local["checks"].append("exact_mechanical_audit_lines")

        local.update(
            {
                "editorial_decision": package["editorial_decision"],
                "weaknesses": len(source_refs),
                "roadmap_items": len(items),
                "obligation_counts": normalized_obligations,
                "sha256": {
                    "editorial_synthesis": digest(synthesis),
                    "revision_roadmap": digest(roadmap_path),
                    "review_package": digest(package_path),
                    "provenance_artifact": digest(
                        notes / "stage3_review_panel_provenance.json"
                    ),
                    "provenance_carrier": digest(carrier_path),
                    "revision_base": digest(notes / "stage3_revision_base.tex"),
                    "block_manifest": digest(
                        notes / "stage3_revision_base.block-manifest.json"
                    ),
                },
            }
        )
        results[paper_id] = local

    summary = {
        "status": "PASS" if not failures else "FAIL",
        "papers": results,
        "totals": {
            "phase1_cards": 25,
            "phase2_cards": 25,
            "editorial_decisions": 5,
            "major_revision": sum(
                1 for value in results.values() if value["editorial_decision"] == "Major Revision"
            ),
            "source_weaknesses": sum(value["weaknesses"] for value in results.values()),
            "roadmap_items": sum(value["roadmap_items"] for value in results.values()),
            "must_fix": sum(
                value["obligation_counts"]["must_fix"] for value in results.values()
            ),
            "should_fix": sum(
                value["obligation_counts"]["should_fix"] for value in results.values()
            ),
            "consider": sum(
                value["obligation_counts"]["consider"] for value in results.values()
            ),
            "canonical_mutations": 0 if not any("frozen hash" in item for item in failures) else None,
        },
        "failures": failures,
        "boundaries": {
            "stage4_authorized": False,
            "manuscript_mutation_authorized": False,
            "scientific_execution_authorized": False,
            "route_advancement": "NONE",
            "route_b_invoked": False,
        },
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
