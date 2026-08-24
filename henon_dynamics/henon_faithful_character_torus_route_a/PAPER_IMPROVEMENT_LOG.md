# C134 paper improvement log

No external reviewer, novelty score, or acceptance prediction was used.  The
two revisions below are internal proof, claim/evidence, and presentation
audits, each followed by a fixed-epoch recompilation and retained PDF.

## Round 0

Artifact: `paper/main_round0_original.pdf`

SHA-256: `84e5d1eb91433d3ad2f751c3b8169dfb17eabc3250fd5fe267e4cf66fd26c8ca`

The baseline establishes uniform scaled separation, the character-family
Hardy owner, all-order trace/Fredholm/primitive formulas, Laurent Newton
recovery, the `k=1`/`k=6` control, and the strict Route-A boundary.  Its main
weakness is that the uniform nuclearity estimate and the exact faithfulness of
the Gaussian-rational anchor are compressed into headlines.

## Round 1

Artifact: `paper/main_round1.pdf`

SHA-256: `751171724c399735be658f1f0d5c47343ac988a7406773f165300944301f1b7d`

The first revision adds the scale conjugacy, the explicit restriction ratio
`85/96` and summable degree majorant, and the minimal-polynomial proof that
`q=(3+4i)/5` is not torsion.  It also explains why exact evaluation at any
known faithful character remains injective on Laurent monomials.

## Round 2

Artifacts: `paper/main_round2.pdf`, `paper/main.pdf`

SHA-256: `404b2618ff7e51c6018a7b9c007b0d683dd3ade8ac6af0484f3f782692d651d5`

The final revision distinguishes the general three-state three-jet algebra
from the zero-sum consistency certificate in the frozen permutation family.
It adds a compact quotient-versus-faithful control table and derives the exact
labelled-parameter relation
`D_{-t,u}(z)=D_{t,u^{-1}}(z)`.  The text explicitly identifies this as
character-parameter inversion, never a reciprocal determinant, and explains
why dense faithful phases do not imply finite-precision stability.
The release audit then synchronized the displayed independent-checker and
mutation totals with the expanded source-lock/Newton-jet hostile suite; this
changed validation reporting only, not the theorem or evidence payload.

All versions are two pages and have distinct hashes.  Two fresh isolated
fixed-epoch builds of the final source are byte-identical to each other and to
the checked-in final PDF.  Every font is embedded; the logs contain no warning,
overfull or underfull box, undefined reference, undefined citation, or
multiply-defined label.  Both rendered final pages were visually inspected
without clipping, collision, truncation, unintended blank space, or broken
equation/table layout.
