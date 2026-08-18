# P47 independent-writer-audit handoff

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

Audit the exact paper 47 writer overlay.  Do not infer installation,
publication, or authority-write permission from this writer-side handoff.

The prior PDF `bb30f866...` and prior writer seal `cfb71220...` were rejected
for a Figure-2 visual collision and are withdrawn.  Only the complete new
anchors below identify the candidate to audit.

## External anchors

- `PAPER_MANIFEST.tsv` SHA-256:
  `10bc900a80497637ec397bbc7c7d43c5be736845dee413129252fa07920a98cf`;
- `WRITER_REPORT.md` SHA-256:
  `2df05cac26f0a7b904e0617537977a4c3985f417970bebdf830fda1804de510a`;
- final `main.pdf` and `main_round2.pdf` SHA-256:
  `b6c4d6aa27fe23f74b4c9e63628cd9b34b83d1d4d0908b040cc923af4c0ae12d`;
- final compile-log SHA-256:
  `23cf89d34d194a01ff9a4c3bcd3611670099f7286bccc121c336dbf89e7973d2`;
- final bibliography SHA-256:
  `dd828b408bbe3bb486a8d8ea7fc8794d9c6759ac564176befae50dadf5a235dc`;
- final PDF-QA record SHA-256:
  `e761980bddd67519af3bc6da2e120c088c435a32871b00abe50f11f38b4b8cc1`;
- repaired Figure-2 source SHA-256:
  `1da86f01205cb0ea57af2a7dc47bcb5993e1e3374229237cf7464fe320904c52`;
- portable protected-State-A manifest SHA-256:
  `30a79c4be4bc9b9333cb2a9f809d2039430cebc86686a054765734a782eea473`;
- protected-State-A replay SHA-256:
  `bd172e5a1f7523211f8784a4384c6e885f33d681b6bc8dc728bbd96ea378f4c3`;
- writer canonical-summary SHA-256:
  `45185ea8750dec4557b055f0381137076df5d1615c51c482fa96e623f8ed1d7f`.

## Required independent checks

1. Verify `WRITER_SEAL.json`, then independently recompute the handoff,
   report, and manifest hashes without trusting their embedded values.
2. Run `scripts/build_writer_manifest.py --root ABS_ROOT --check`; require
   exactly 51 manifest-covered content rows, 55 final regular files, exact
   nine-directory closure, modes 0644/0755, and no symlink, cache, LaTeX
   auxiliary, protected copy, `outputs/**`, `evidence/publication_gate/**`,
   Git, README, or mirror path.
3. Require `main.pdf` and `main_round2.pdf` to be byte-identical and match
   the new final hash.  Preserve the distinct Round-0 and Round-1 PDFs with
   hashes `3cab9e5f...` and `5837f352...`.
4. In two separate isolated copies, rebuild with epoch `1787011200` and
   require the final PDF, bibliography, and compile-log hashes to reproduce.
   Do not build in the frozen candidate itself.
5. Run `scripts/check_pdf_qa.py` on an isolated exact copy and independently
   repeat font, text, bbox, A4 page-size, and 14-page visual checks.
6. Inspect final PDF page 7 at sufficient resolution.  Require all three
   labels to have clear white separation from their thick domain bands and
   require the strict-wall callout to be separate from the `0`, `1/2`, `1`
   ticks and from `no bounded operator`.  Confirm that thresholds, open
   endpoints, band extents, and domain/color semantics are unchanged.
7. Run `scripts/capture_protected_statea.py --check` with the explicit live
   paper-47 authority, Stage0 candidate, and an isolated exact writer copy.
   Require 91 nodes, 67 regular files, 24 directories, Stage0 62 nodes,
   State-A outputs 29 nodes/20 files, repeated equal captures, and zero
   mismatch or mutation.
8. Re-run `scripts/extract_canonical_results.py --check` and
   `figures/gen_canonical_table.py --check`; require byte-identical summary,
   tables, and writer ledger.
9. Confirm the current plan's post-review `-1/2` normalization and the same
   GPT-5.4 xhigh thread's Round-2 `C0/M0/m0 / ROUND2_READY` verdict from the
   raw review, without treating that verdict as an independent writer audit.
10. Independently recheck that analytic proofs own every infinite endpoint
    and trace identity, while finite PASS/mutation/route records remain
    implementation and provenance evidence only.
11. Confirm that the old PDF hash
    `bb30f866ecac88b8b5467dadecef968daa60dc9383af46eea0e7e5602a794eb0`
    and old seal hash
    `cfb71220d7838d92345d9df70d47e6f2d669607a794cf1f2ee78b7a07f81f5b0`
    are treated as withdrawn, not as alternate valid anchors.

The manifest excludes exactly four downstream closure files:
`PAPER_MANIFEST.tsv`, `WRITER_REPORT.md`, `HANDOFF.md`, and
`WRITER_SEAL.json`.  The dependency direction is content to manifest to
report to handoff to seal.  All four closure files belong to the final writer
overlay; none belongs to the protected authority tree.
