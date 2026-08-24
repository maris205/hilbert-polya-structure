# Compile report — C121

- engine: pdfLaTeX through `latexmk`;
- fixed environment: `SOURCE_DATE_EPOCH=0`, `TZ=UTC`;
- isolated build A SHA-256:
  `fa46eca15628ef467fb7731123f400bb62c6f88c0fc2fcd58119040bc4b8fc7a`;
- isolated build B SHA-256:
  `fa46eca15628ef467fb7731123f400bb62c6f88c0fc2fcd58119040bc4b8fc7a`;
- final `main.pdf` SHA-256:
  `fa46eca15628ef467fb7731123f400bb62c6f88c0fc2fcd58119040bc4b8fc7a`;
- round-zero snapshot SHA-256:
  `fa46eca15628ef467fb7731123f400bb62c6f88c0fc2fcd58119040bc4b8fc7a`;
- round-one snapshot SHA-256:
  `fa46eca15628ef467fb7731123f400bb62c6f88c0fc2fcd58119040bc4b8fc7a`;
- round-two snapshot SHA-256:
  `fa46eca15628ef467fb7731123f400bb62c6f88c0fc2fcd58119040bc4b8fc7a`;
- pages: 2;
- deterministic byte comparison: pass;
- checked-in PDF agrees with both isolated builds: pass;
- font audit: every reported font is embedded;
- final log audit: no unresolved reference or citation, overfull or underfull
  box, undefined or multiply-defined label, or material warning;
- two-page raster inspection: pass, with no clipping, collision, or blank
  content page.

All three named round snapshots were regenerated from the corrected final
source so that none retains the obsolete noncanonical route labels.  Their
byte identity is intentional and documented in the improvement log.

The ordinary first-pass cross-reference rerun was resolved by `latexmk`; both
final isolated logs are clean.
