# C388 — connected algebraic lattice resonance

The source is the compact connected circle-valued action defined by the integral
relation `1+u+v`. Every finite-index lattice has an exact quotient matrix and Smith
presentation. Resonance occurs precisely at HNF triples satisfying `3|a` and
`b=c (mod 3)`; then the fixed group has a two-torus factor and the component
count is `3/N^2` times its nonzero Fourier product.

The smallest index-three quotient also supplies an exact correction to the
uncorrected finite-lattice formula printed in arXiv:0912.5169v1, Lemma 2.1.
It does not refute the source entropy theorem. Classical resonance and entropy
owners are stated positively; this package is source-local and owner-heavy.

Read [the proof](proof/ANALYTIC_PROOF.md), [the final paper](paper/main.pdf),
[results](results/RESULTS.md), and [reproduction instructions](REPRODUCIBILITY.md).
The final paper is byte-identical to revision two. The finite grid is a
certificate audit, not the proof of the all-lattice statement.

Strict tuple: `A0_WEAK_ARITHMETIC_RELATION / A1_WEAK / A2_FAIL / A3_FAIL / A4_FORMAL_HINT`.
All target-claim flags remain false; Route B is disabled.
`NO_BAD_EULER_OR_ROOT_NUMBER`.
