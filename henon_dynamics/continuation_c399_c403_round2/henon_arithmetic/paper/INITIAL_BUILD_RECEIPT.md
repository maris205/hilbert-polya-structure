# C401 initial compilation receipt

Status: **initial compilation complete; not a final independent build or a final review receipt**. The main coordinator owns mathematical re-review, complete final PDF inspection, and the two fresh-directory reproducibility builds.

## Frozen artifact

- Artifact: `main.pdf`, 13 A4 pages, 396,787 bytes, PDF 1.5.
- SHA256: `fcd14059ed2504dae82188c585d8bc2a05f040fc27775251728d72c5408e891a`.
- Full local build inputs: `SOURCE_INPUTS.sha256` (main TeX, commands, eight section files, bibliography).
- Frozen upstream provenance: `FROZEN_UPSTREAM.sha256` (contract, exact-check code, saved results, prior proof review).
- Runtime inputs from the final pdfTeX recorder, plus the BibTeX bibliography/style inputs: `initial_build/RUNTIME_INPUTS.sha256`. This captures the actual initial environment and is not a promise of cross-version reproducibility.
- All manuscript TeX and bibliography files are frozen for handoff. The plan, Chinese abstract, verification note, and receipts are not PDF build inputs.

## Actual build and repair history

The build ran in the newly created directory `/tmp/c401-initial.p1sMnl`, with copied local sources. No frozen computational experiment was run. The build command was:

```sh
env SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The shell used `set -o pipefail` while recording stdout with `tee`, so the recorded successful outcome is the compiler pipeline's outcome rather than merely that of its final log-writing process.

1. Attempt 1 returned exit 12: the date field contained a paragraph construct rejected by `\date`. Replaced by a line break and a small-font internal-series line.
2. Attempt 2 returned exit 12: an undefined arrow macro was replaced by the standard `\longmapsto`. The introduction's long displayed line was also split to remove an overfull box.
3. Attempt 3 returned exit 0 and produced a complete 13-page PDF with all proofs and six references.
4. A final prose-only clarification distinguished the slice's construction from numerical coincidence with the zeta of affine two-space. Incremental `latexmk` returned exit 0 after this change. The final PDF above comes from this post-polish build.

Failed attempts are retained as `initial_build/attempt-1.*` and `attempt-2.*`, the first successful attempt as `attempt-3.*`, and the post-polish build as `final.*`. They are openly recorded; the final clean log does not conceal the earlier repairs. Only the final local sources are frozen and hashed.

## Initial checks actually performed

- `pdfinfo`: 13 pages, A4, 396,787 bytes, not encrypted. Metadata identifies Anonymous Authors and Internal research series C401, with no fabricated journal identity.
- `pdffonts`: all 23 reported font rows are embedded; all are Type 1.
- The final TeX and BibTeX logs contain zero matches for `Warning`, `Overfull`, `Underfull`, `undefined`, `Error`, or `Missing character`.
- The final PDF was converted using `pdftotext -layout`; the output is retained as `initial_build/final.txt`.
- Actual rendered pages 1, 6, and 13 were visually inspected: title/abstract, the central boundary-length proof, and bibliography are readable without observed clipping or overflow. This is a three-page initial spot check, **not** an all-page visual certification.
- Actual citation keys and theorem labels were checked against the final auxiliary data. The bibliography has six entries and seven citation commands, all resolved. `SOURCE_VERIFICATION.md` lists every actual citation context and full-proof locator.
- The frozen upstream contract, code, saved JSON results, and prior proof review retain their original SHA256 values. The manuscript reports the existing 47 exact checks as bounded support, not proof; no numerical rerun was performed during drafting.

Toolchain: pdfTeX `3.141592653-2.6-1.40.22` (TeX Live 2022/dev/Debian), BibTeX `0.99d`, latexmk `4.76` (20 November 2021). The TeX source suppresses PDF timestamps, uses an empty trailer ID, suppresses pdfTeX source metadata, and fixes the displayed date to 5 September 2026. This setup supports the coordinator's later deterministic-build check but does not replace actually performing it.

No CURRENT file, evaluation record, Git state, frozen proof contract, saved experimental code/result, or external publishing service was modified as part of this manuscript task. The source-ownership and target-route evaluations remain separate from successful typesetting. No claim is made here that C401 passed the target evaluation or a global novelty test.
