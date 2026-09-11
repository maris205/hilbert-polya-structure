#!/usr/bin/env python3
"""Verify a lifecycle-only final refresh after the actual full audit.

No mathematical verifier is executed here. The earlier full audit ran every
author/A/B twice. Exact pins require all its scientific inputs, all ten sealed
reviews and all final build payload manifests to remain unchanged. This pass
then checks the refreshed full packages, PDF/build structures and globals.
"""
import audit_batch as a


def main():
    prior = a.SEQ / "qa/FINAL_TERMINAL_AUDIT.txt"
    text = prior.read_text(encoding="utf-8")
    a.check(text.endswith("status=PASS\n"), "prior actual full audit not PASS")
    a.check("paper_ids=197,199,200,202,203\n" in text
            and "author_replays=10\n" in text
            and "review_replays=20\n" in text,
            "prior full audit has wrong scope")
    scientific_pins = a.check_pins(a.SEQ / "qa/TERMINAL_SCIENTIFIC_INPUTS.sha256")
    a.check(scientific_pins == 57, "scientific input inventory drift")
    files = review_files = pages = input_pins = 0
    for n, p in a.PAPERS.items():
        a.check("INDIVIDUAL_TERMINAL_PASS" in
                (p / "PAPER_IMPROVEMENT_STATE.md").read_text(encoding="utf-8"),
                f"P{n} lifecycle not finalized")
        a.check(not list(p.rglob("__pycache__")) and not list(p.rglob("*.pyc")),
                f"P{n} cache appeared")
        files += len(a.complete_manifest(p)) + 1
        a.complete_manifest(p / "qa_final")
        a.frozen_round_gate(n, p)
        if n == 203:
            a.current_input_gate(p)
        for name, role in (("main_round0_original.pdf", "round0_original"),
                           ("main_round1.pdf", "round1"),
                           ("main_round2.pdf", "round2")):
            a.pdf_gate(n, p / name, role=role)
        pages += a.cold_gate(n, p)
        a.citation_gate(n, p)
        for suffix in ("a", "b"):
            review = a.SEQ / "reviews" / f"p{n}_{suffix}"
            a.review_manifest_gate(review)
            review_files += len(a.recursive_files(review))
            input_pins += a.check_pins(review / "PINNED_INPUTS.sha256")
    a.global_manifest_gate()
    print("scope=FINAL_LIFECYCLE_HASH_REFRESH_ONLY")
    print("prior_full_audit=qa/FINAL_TERMINAL_AUDIT.txt; status=PASS")
    print("paper_ids=197,199,200,202,203")
    print(f"scientific_input_pins_unchanged={scientific_pins}")
    print(f"paper_files={files}; review_files={review_files}; input_pins={input_pins}")
    print(f"pages_and_visual_files={pages}; cold_builds=10")
    print("new_mathematical_replays=0; new_builds=0; new_visual_views=0")
    print(f"mechanical_checks={a.ASSERTIONS}")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")
    print("status=HASH_REFRESH_PASS_NOT_A_NEW_REPLAY")


if __name__ == "__main__":
    main()
