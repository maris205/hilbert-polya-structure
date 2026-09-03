# P174: Minimum-Pivot Möbius Feedback on Projective-Line Subsets

**Status:** `FINAL ROUND 2 / DUAL-REVIEW CLOSED / PROVISIONAL_AMBER / HOLD_EXTERNAL`

This AMS short note studies the literal map that translates a fixed-size
subset of `P^1(F_p)` by its least finite point and then applies inversion.
For every prime `p` and `2<=k<=p`, it proves the complete depth-two
functional graph, the identity `M^4=M^2`, the fixed/2-cycle census, and an
every-target pivot-marked inverse law.

The value boundary is intentionally narrow.  Fixed Möbius dynamics,
`PGL(2,q)` subset actions, projective-configuration orbits, ordered
canonical-image/canonizing-element machinery, inversion, and binomial counts
are zero-credit background.  P174 is not a canonical-image map: it neither
minimizes over the group nor stays constant on group orbits.  P96, P168, and
the killed AQN control are explicitly subtracted in the manuscript.  Only
the literal two-stage containment tower and target-dependent modular pivot
interval remain under evaluation.  A bounded direct-owner non-hit is not
novelty, priority, ownership, freedom-to-operate, or release evidence.

## Final artifact package

- `main.tex`, `references.bib`: anonymous AMS source and verified five-entry
  bibliography.
- `main.pdf`: canonical four-page final Round-2 PDF.
- `main_round0_original.pdf`: immutable byte-identical Round-0 freeze.
- `main_round1.pdf`, `main_round2.pdf`: preserved review rounds; the latter
  is byte-identical to `main.pdf`.
- `NARRATIVE_REPORT.md`: theorem story and owner/internal subtraction.
- `PAPER_PLAN.md`: short-note structure and claim/evidence placement.
- `CLAIMS_EVIDENCE.md`: formal claim matrix and exclusion boundary.
- `SOURCE_VERIFICATION.md`: primary-source metadata and bounded-search log.
- `verify_p174.py`: independent standard-library verifier.
- `verification_output.txt`: canonical 131,018,555-assertion transcript.
- `BUILD.md`: replay, compilation, PDF, and hash ledger.
- `SELF_QA.md`: author-side mathematical, source, anonymity, and visual QA.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`: both independent hostile
  reviews and the closed Review-B delta ledger.
- `SHA256SUMS`: integrity manifest, regenerated at final closeout.

Review A returned no finding.  Review B independently passed 4,755,152
assertions and found one minor source-boundary omission: ordered
canonical-image/canonizing-element machinery.  Jefferson et al. (2019) is
now cited and assigned zero credit; the owner-search vocabulary was expanded,
and the reviewer marked the repair `CLOSED`.  The theorem and amber gate were
unchanged.

## Exact replay

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p174.py > /tmp/p174_replay.txt
cmp -s /tmp/p174_replay.txt verification_output.txt
sha256sum -c SHA256SUMS
```

Expected verifier metadata:

```text
complete parameter boxes: 69
assertions: 131,018,555
stdout SHA-256: 1faac49f7cb9cdfb7be13caf1a533f36a07851cdff1a9a955b85a3ec593e0646
decision: AUTHOR_ROUND0_PASS
external status: PROVISIONAL_AMBER / HOLD_EXTERNAL
```

## Build

`latexmk` is unavailable in the environment.  The equivalent settling
sequence is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The canonical and final source-only cold builds are byte-identical.  See
`BUILD.md` for exact hashes and diagnostics.  A successful internal build
does not authorize posting, submission, author contact, or circulation.
