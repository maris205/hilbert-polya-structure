# Paper improvement log — P134

## Round 0

The anonymous five-page note froze the whole-table update, exact image and
recurrent atlas, sharp piecewise transient, and factorial fibre extremum.  Its
1,694,506-assertion verifier and immutable `main_round0_original.pdf` passed
the initial reproducibility gate under `HOLD_EXTERNAL`.

## Round 1 — implementation of Hostile Review A

Review A found no critical or major defect and required two exposition
repairs:

- `A134-1`: the mismatch proof now shows explicitly that the entire shared
  prefix determines `Q(q)=B_(r+1)` or `Q(q)=A_(k-1)`; it no longer attributes
  the template parameter to the second coordinate alone.
- `A134-2`: the maximizer proof now handles `n=2` as an empty product with its
  two literal sources before invoking `e_2` in the `n>=3` suffix argument.

The theorem statements, verifier, canonical output, and contribution boundary
are unchanged.  The fresh 1,694,506-assertion replay passed byte for byte; the
repository and isolated builds agreed; both repaired proof locations were
visually checked; and `main_round1.pdf` was frozen at SHA-256
`d1c1ed8fe7667bb192c6c00e59259e1a80403c5a18e52735be99e907c7662525`.
External status remains `HOLD_EXTERNAL`; no Git action was taken.

## Round 2 — implementation of Hostile Review B

Round B independently reconstructed every theorem and returned no critical or
major finding.  `B134-1` replaced a stale “first paragraph” pointer by the
exact preceding `A_r`-case argument.  `B134-2` updated `README.md` and
`PAPER_PLAN.md` from their superseded Round-0/deferred-review state.  The
literal map, theorem formulas, proof argument, bibliography, verifier,
canonical stdout, and contribution ceiling are unchanged; the editorial
pointer changes the compiled source and therefore requires a distinct
Round-2 PDF freeze.

That freeze is complete.  The fresh verifier passed; the repository and
isolated builds agreed byte for byte; `main.pdf` and `main_round2.pdf` have
SHA-256
`7d69a1e9338e9421ef31ac3e265a35317e0d11c836f1a652a76a69c36b923962`.
The Round-1 and Round-0 artifacts remain immutable.  External status is
`HOLD_EXTERNAL`.

The original reviewer independently rechecked both repairs, the unchanged
verifier, the repository and isolated builds, and all three PDF generations.
Both findings are closed; final Round-B severity is critical 0, major 0,
minor 0 with `GO_INTERNAL / HOLD_EXTERNAL`.
