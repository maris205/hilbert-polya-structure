# C135 paper improvement log

No external reviewer, novelty score, or acceptance prediction was used.  The
two revisions below are internal proof, claim/evidence, and presentation
audits, each followed by a fixed-epoch recompilation and retained PDF.

## Round 0

Artifact: `paper/main_round0_original.pdf`

SHA-256: `b183a2c1d6235192dbfa27abd64c04b45f85f427ffe639e582b4068fb9144000`

The baseline gives the four-variable determinant, all-period trace and
primitive product, nonlattice specialization, the requested period-six
separation, the residual collision, and the strict boundary.  Its main
weakness is that the formal-product and analytic convergence arguments, and
the exact trace multiplicities, are stated too tersely.

## Round 1

Artifact: `paper/main_round1.pdf`

SHA-256: `0f69e7f668e6d4bd3b5922a72937a4baad226c1b059f812df2495e8841b1a0a3`

The first revision proves coefficientwise well-definedness in the completed
edge-degree ring, supplies Perron domination for absolute convergence when
`Re(s)>h`, and gives the sign-automorphism proof of radical-basis
independence.  It also explains the rooted multiplicities 6 and 12 from the
one-versus-two primitive necklaces in the two edge sectors.

## Round 2

Artifacts: `paper/main_round2.pdf`, `paper/main.pdf`

SHA-256: `0a0ab1a405e2fdec843d26a6fa1de81d74ce12768721dd21dcee29502882c808`

The final revision adds the no-nonzero-imaginary-period control and a
cutoff-free telescoping proof of `N01=N10`.  It identifies the observable
off-diagonal quotient in two independent ways: closed-word conservation and
the occurrence of only `x01*x10` in the determinant.  The explicit
`(tau01+a,tau10-a)` family makes the remaining nonidentifiability auditable.
The release audit also repaired two malformed roman-font control sequences in
the displayed primitive-orbit formulas; this changed presentation only, not
the theorem, evidence, or checker outputs.

All versions are two pages and have distinct hashes.  Two fresh isolated
fixed-epoch builds of the final source are byte-identical to each other and to
the checked-in final PDF.  Every font is embedded; the logs contain no warning,
overfull or underfull box, undefined reference, undefined citation, or
multiply-defined label.  Both rendered final pages were visually inspected
without clipping, collision, truncation, unintended blank space, or broken
equation/table layout.
