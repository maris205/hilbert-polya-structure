#!/usr/bin/env python3
"""Build or verify the deterministic P47 two-round improvement record."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def write_exclusive(path: Path, raw: bytes) -> None:
    descriptor = os.open(
        path,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o644,
    )
    try:
        os.fchmod(descriptor, 0o644)
        offset = 0
        while offset < len(raw):
            offset += os.write(descriptor, raw[offset:])
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def build(root: Path) -> tuple[bytes, bytes]:
    round1 = (root / "reviews" / "ROUND1_REVIEW_RAW.md").read_text("utf-8").rstrip()
    round2 = (root / "reviews" / "ROUND2_REVIEW_RAW.md").read_text("utf-8").rstrip()
    if "Counts: C0 / M2 / m3" not in round1 or not round1.endswith("ROUND1_FIX"):
        raise SystemExit("ROUND1_REVIEW")
    if "Counts: C0 / M0 / m0" not in round2 or not round2.endswith("ROUND2_READY"):
        raise SystemExit("ROUND2_REVIEW")
    hashes = {
        "figure2": sha256(root / "figures" / "fig2_phase_diagram.tex"),
        "final_bibliography": sha256(root / "evidence" / "FINAL_BIBLIOGRAPHY.bbl"),
        "final_compile_log": sha256(root / "evidence" / "FINAL_COMPILE.log"),
        "main_pdf": sha256(root / "main.pdf"),
        "main_round0_original_pdf": sha256(root / "main_round0_original.pdf"),
        "main_round1_pdf": sha256(root / "main_round1.pdf"),
        "main_round2_pdf": sha256(root / "main_round2.pdf"),
        "pdf_qa": sha256(root / "evidence" / "PDF_QA.md"),
    }
    if hashes["main_pdf"] != hashes["main_round2_pdf"]:
        raise SystemExit("FINAL_PDF_IDENTITY")
    if len({hashes["main_round0_original_pdf"], hashes["main_round1_pdf"], hashes["main_round2_pdf"]}) != 3:
        raise SystemExit("ROUND_PDF_DISTINCTNESS")

    log = f"""# P47 paper improvement log

## Review progression

| Manuscript state | Independent review | Findings | Disposition |
|---|---|---:|---|
| Round 0 original | GPT-5.4 xhigh Round 1 | C0 / M2 / m3 | `ROUND1_FIX` |
| After Round 1 fixes | GPT-5.4 xhigh Round 2, same thread | C0 / M0 / m0 | `ROUND2_READY` |
| Round 2 review-ready state | post-review build and writer QA | zero automated QA defect | superseded after independent visual HOLD |
| Visual-HOLD repair | writer-side deterministic rebuild and full QA | repaired; fresh independent recheck required | `HOLD_FOR_INDEPENDENT_WRITER_AUDIT` |

No numerical score is invented: the independent reviewer reported severity
counts and dispositions rather than a score.

## Round 1 raw review

<details>
<summary>GPT-5.4 xhigh Round 1 review (verbatim)</summary>

{round1}

</details>

### Fixes implemented after Round 1

1. Corrected the abstract normalization to
   `[z^2] log det_2(I-zE_s) = -Tr(E_s^2)/2`.
2. Replaced the malformed overlap exponent with
   `det_2(I-zE_s)=det(I-zE_s) exp(z Tr(E_s))`.
3. Added the exact divisor conditions `d|m^2`, `d<m` to the abstract.
4. Restricted the introductory negative-minor conclusion to real `s>1` and
   the real trace-class regime.
5. Synchronized the reviewed paper plan with the `-1/2` determinant
   normalization.

The warning-free Round-1 PDF has SHA-256
`{hashes['main_round1_pdf']}`.

## Round 2 raw review

<details>
<summary>GPT-5.4 xhigh Round 2 review (verbatim; same reviewer thread)</summary>

{round2}

</details>

### Post-Round-2 build repair

Text-extraction QA found 13 illegal C0 characters in the Round-1 PDF, all
emitted by extensible mathematical delimiter glyphs.  Replacing the affected
delimiters with fixed parentheses changed no formula, theorem, domain, or
evidence claim.  Default, layout, and raw extraction now each contain zero
illegal C0/DEL/C1 and zero replacement characters.

Two clean fixed-epoch builds reproduced the final PDF, bibliography, and
compile log byte for byte.  All 14 A4 pages passed individual visual
inspection; 29/29 fonts are embedded, subsetted, and Unicode mapped; both
bbox modes contain zero out-of-page word boxes.  Full details are in
`evidence/PDF_QA.md`.

### Independent visual-HOLD repair

The independent writer audit rejected the earlier Round-2 rendering because
the three thick domain bands in Figure 2 crossed their labels, while the
strict-endpoint note collided with the ticks and the negative-domain label.
That rendering and its seal are permanently withdrawn:

- withdrawn PDF SHA-256:
  `bb30f866ecac88b8b5467dadecef968daa60dc9383af46eea0e7e5602a794eb0`;
- withdrawn writer-seal SHA-256:
  `cfb71220d7838d92345d9df70d47e6f2d669607a794cf1f2ee78b7a07f81f5b0`.

The repaired vector figure places each label above its corresponding band
and moves the strict-endpoint explanation into an independent white callout
to the right of the axis.  The open endpoints, thresholds
`0, 1/2, 1`, band extents, color encoding, and negative-domain statement are
unchanged.  The repaired Figure-2 source has SHA-256 `{hashes['figure2']}`.
The resulting paper has again undergone fixed-epoch A/B reproduction plus
full writer-side text, font, bounding-box, and per-page visual QA.  These are
writer checks, not a substitute for the required fresh independent audit.

## Artifact hashes

- Round 0 original PDF: `{hashes['main_round0_original_pdf']}`;
- Round 1 PDF: `{hashes['main_round1_pdf']}`;
- final `main.pdf` / Round 2 PDF: `{hashes['main_pdf']}`;
- final bibliography: `{hashes['final_bibliography']}`;
- final compile log: `{hashes['final_compile_log']}`;
- PDF QA record: `{hashes['pdf_qa']}`;
- repaired Figure-2 source: `{hashes['figure2']}`.
"""
    state = {
        "completed_at_utc": "2026-08-18T00:00:00Z",
        "current_round": 2,
        "final_counts": {"critical": 0, "major": 0, "minor": 0},
        "final_disposition": "ROUND2_READY",
        "final_pdf_sha256": hashes["main_pdf"],
        "review_model": "GPT-5.4 xhigh",
        "review_thread": "/root/p47_writer/p47_manuscript_reviewer",
        "schema": "paper47.paper-improvement-state.v2",
        "status": "completed_pending_independent_writer_audit",
        "visual_hold_repair": {
            "figure2_sha256": hashes["figure2"],
            "status": "writer_repaired_pending_fresh_independent_recheck",
            "withdrawn_pdf_sha256": "bb30f866ecac88b8b5467dadecef968daa60dc9383af46eea0e7e5602a794eb0",
            "withdrawn_writer_seal_sha256": "cfb71220d7838d92345d9df70d47e6f2d669607a794cf1f2ee78b7a07f81f5b0",
        },
        "writer_handoff_status": "HOLD_FOR_INDEPENDENT_WRITER_AUDIT",
    }
    state_raw = (
        json.dumps(state, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode("ascii")
    return log.encode("utf-8"), state_raw


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    if not root.is_absolute() or root.is_symlink() or root.resolve(strict=True) != root:
        raise SystemExit("ROOT_NOT_CANONICAL")
    targets = [
        (root / "PAPER_IMPROVEMENT_LOG.md", None),
        (root / "PAPER_IMPROVEMENT_STATE.json", None),
    ]
    log, state = build(root)
    targets[0] = (targets[0][0], log)
    targets[1] = (targets[1][0], state)
    if args.write:
        if any(os.path.lexists(path) for path, _ in targets):
            raise SystemExit("OUTPUT_NOT_NEW")
        for path, raw in targets:
            assert raw is not None
            write_exclusive(path, raw)
        print(
            "WROTE "
            + " ".join(
                f"{path.name}={hashlib.sha256(raw).hexdigest()}"
                for path, raw in targets
                if raw is not None
            )
        )
        return 0
    for path, raw in targets:
        assert raw is not None
        if not path.is_file() or path.read_bytes() != raw:
            raise SystemExit(f"RECORD_MISMATCH:{path.name}")
    print("PASS rounds=2 final=ROUND2_READY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
