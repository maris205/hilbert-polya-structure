# C185 manuscript improvement log

Status: complete three-round internal drafting sequence.  The three PDFs are
content-distinct, the final manuscript is byte-identical to Round 2, and two
isolated fixed-epoch builds reproduce the released final PDF.  This process is
not external peer review and not an independent error process.

## Round 0 — global theorem skeleton

- Freeze the simple source spectrum and strict diagonal target.
- Prove compact global existence, Lax isospectrality, and the squared-norm
  Lyapunov identity.
- State the Route-A tuple without arithmetic promotion.

Released artifact: `paper/main_round0_original.pdf` (one page), SHA-256
`2077903e4bf4ad9a04fc307ec6dd870362c702e1ffba04f62de6507e20632e1b`.

## Round 1 — local-to-global dynamics

- Add every permutation equilibrium and pair-mode rate.
- Identify the inversion count with unstable dimension and the Morse index of
  the sorting energy.
- Add compact convergence, stable-manifold generic sorting, and the recurrence
  obstruction.

Released artifact: `paper/main_round1.pdf` (two pages), SHA-256
`5f15f53c6f6acf893fd7754a48776fe25a970441e6c40ec6353a899795bc650b`.

## Round 2 — release boundary

- Add exact repeated-spectrum sentinels, distinguish source stabilizer rates
  from target-degenerate tangent zero modes, and decline full
  Bruhat/Schubert or Morse--Bott classification.
- Lock Brockett attribution, exact checker/SymPy/mutation counts, and the A4
  state-dependent-generator limitation.
- Synchronize the final paper, compile report, results, YAML, and manifest.

Released artifacts: `paper/main_round2.pdf` and `paper/main.pdf` (two pages
each), both SHA-256
`94fd82d3077217c35edd8d92f035e91425206af838c8881dca76596bd6f38497`.

## Release checks

- Every round was built twice with LuaLaTeX at
  `SOURCE_DATE_EPOCH=1787702400`; the final pass of every round has zero
  warning, bad-box, missing-glyph, undefined-reference, and error matches.
- Two additional isolated directories reproduced the final PDF byte for byte.
- `pdffonts` reports every font embedded.  Both final pages were rendered to
  PNG and visually inspected; no clipping, overlap, truncation, or blank page
  was observed.
