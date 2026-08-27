#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C192 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C192_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c192_hyperplane_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


EXPECTED_FILES = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c192_hyperplane_checker.py", "code/c192_hyperplane_producer.py",
    "code/c192_mutation.py", "code/c192_release_manifest.py", "code/c192_replay.py",
    "code/c192_sympy_crosscheck.py", "evaluation/route_a_result.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf",
    "paper/main_round1.pdf", "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md",
    "results/RESULTS.md", "results/TEST_REPORT.md", "results/c192_hyperplane_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def is_sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["candidate_id"] == "HCS-C192"
    assert evidence["evaluation_date"] == "2026-08-27"
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"] == {
        "version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256,
    }
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == "82b486a8f4e1dcfd9f532c9cc76847874276e7c214783c92a51b399817a876d9"
    assert digest(EVIDENCE) == "7a6e111aeb06f2d47ec9f0830958edca762f1f7d73ef3f6e6c1b26f3e4539b8b"
    assert evidence["route_a"] == {
        "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "qualifications": {
            "A0": "No intrinsic rational-prime or target-zero indexing is present.",
            "A1": "The chamber spectrum does not recover target arithmetic data.",
            "A2": "No target functional equation or continuation is produced.",
            "A3": "Finite-state mixing bounds are not target counting laws.",
            "A4": "The exact finite operator determinant is only a formal operator hint, with no target divisor identification.",
        },
        "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    }
    assert evidence["forbidden_claims"] == {
        "automorphy": False, "bad_euler_or_root_number": False, "global_novelty": False,
        "hilbert_polya_operator": False, "local_or_euler_factors": False, "root_numbers": False,
        "strict_strong_stationary_time": False, "target_divisor_identified": False,
    }

    yaml = (ROOT / "evaluation/route_a_result.yaml").read_text()
    for literal in (
        "source_commit: " + SOURCE_COMMIT,
        "scope_literal: " + SCOPE,
        "tuple: [A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT]",
        "overall: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
        "strict_sst_claimed: false",
    ):
        assert literal in yaml

    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or is_sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    assert set(files) == EXPECTED_FILES, sorted(set(files) ^ EXPECTED_FILES)

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    assert round_hashes == [
        "d9d24d5eac9d820472df18318478b350155da52b94f82d362a3a5886dc60372f",
        "e393b8371c48a0bcd9f26721f6e614f1fb15d32ec998ddc3e72c5c16324bfb83",
        "32d7b5d7230986cb8f8d00e2cdcffcbe3e083b99be180320132bcf195333ef45",
    ]
    pdf_info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in pdf_info.splitlines() if line.startswith("Pages:")))
    assert pages == 2
    font_lines = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert font_lines and all(line.split()[4] == "yes" for line in font_lines if line.strip())

    finite = evidence["finite_regression"]
    result = {
        "schema": "hcs-c192-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C192",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": (
            "The Brown--Diaconis chamber walk on every finite real hyperplane arrangement has an exact "
            "flat-indexed spectrum, operator determinant, stationary sampler, mixing bound, and "
            "nonseparating stationary-simplex classification"
        ),
        "gates": {
            "G0_provenance_source_and_scope": "PASS_WITH_A0_FAIL",
            "G1_all_arrangement_spectrum_and_operator_corollaries": "PASS_SOURCE_LOCKED",
            "G2_stationary_sampler_and_mixing": "PASS_WITH_STRICT_SST_BOUNDARY",
            "G3_nonseparating_and_oriented_matroid_ceiling": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_three_round_double_compile_fonts_layout_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            **finite,
            "independent_checker_assertions": 20609,
            "sympy_checks": 3398,
            "repaired_hash_mutation_rejections": 74,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 1,
            "reference_registry_population": 1,
            "pdf_pages": pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": [
            "a new proof or priority claim for the Brown--Diaconis all-arrangement theorem",
            "strict strong-stationary-time independence for the chamber-hitting stopping rule",
            "self-adjointness, reversibility, or universal sharpness of the mixing bound",
            "an oriented-matroid extension beyond the scope stated in Brown--Diaconis Section 6",
            "local factors, Euler factors, root numbers, automorphy, or target arithmetic data",
            "a target functional equation, counting law, divisor, or Hilbert--Polya operator",
            "Route-B authorization, global novelty, external peer review, or acceptance score",
        ],
        "excluded_from_manifest": [
            "C192_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/*.aux", "paper/*.log",
            "paper/*.out", "paper/*.fdb_latexmk", "paper/*.fls", "paper/*.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C192_MANIFEST_PASS", "file_count": len(files),
        "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
