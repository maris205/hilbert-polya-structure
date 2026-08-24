# Source audit

The source is completely frozen in this package: the two maps
`phi_a(z)=1/(a+z)` for `a=3,6`, normalized Bergman space, the unweighted
composition sum, integer branch matrices, word-composition convention, and
Fredholm determinant.  No fitted parameter or external dataset occurs.

The proof uses standard background facts only: the normalized Bergman
monomial basis, the ideal property of trace-class operators, the Fredholm
determinant logarithm near the origin, and bounded invertibility of composition
by a disk automorphism.  Every numerical headline is rederived from exact
integer or rational arithmetic in the producer, an independent checker, and
a separate SymPy reconstruction.  No literature novelty search or external
referee score was performed, and none is claimed.

The evidence cutoff `n<=10` supplies 2,046 exact rooted-word receipts.  It is
not used to infer the universal statements: trace class, the word formula,
the all-`n` trace identity, and the primitive product are proved analytically.

No prime table, zero table, arithmetic Euler factor, root number, target
spectrum, automorphy, or Hilbert--Pólya assertion is imported.  The product in
this package is a dynamical Fredholm product of the frozen operator only.
