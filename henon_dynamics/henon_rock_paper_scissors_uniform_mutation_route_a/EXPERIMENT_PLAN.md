# Deterministic experiment and audit plan

## Frozen design

The producer uses exact rational parameters and 90-decimal `mpmath`.  The
conservative grid has \(a\in\{1,2,3\}\) and
\(h\in\{1/1000,1/100,1/50,1/30,1/28\}\).  Three center-limit rows use
\(h=1/27\).  Six mutation rows cover small/large mutation and each coordinate
boundary.  Three exact \(a=0\) contraction rows and four tangent-linearization
rows cover the degenerate faces.

## Evidence protocol

The two positive turning roots are bracketed independently on
\((0,1/3)\) and \((1/3,1)\).  The singular endpoint in the requested
quadrature is removed analytically using \(x=x(\theta)\), giving the regular
integrand \([x(x_3-x)]^{-1/2}\).  Fixed-step RK4 is stored only as a labelled
finite diagnostic; theorem statements use the exact vector-field identities.

## Controls and failure tests

The checker reimplements every root, quadrature and RK4 row without importing
the producer.  SymPy verifies mass, product, AM–HM, tangent characteristic,
turning and contraction identities.  Byte replay uses two fresh temporary
trees.  Twenty-five mutations include stale and repaired hashes, altered
roots/periods, the positive-rate period hypothesis, counts, faces, route
flags, scope flags, and unknown keys.  Any
accepted mutation or nonpositive/incorrect mass row is a release failure.

The finite ledger is implementation evidence, not a numerical proof of
LaSalle's theorem and not a primitive-periodic-orbit census for Route A.
