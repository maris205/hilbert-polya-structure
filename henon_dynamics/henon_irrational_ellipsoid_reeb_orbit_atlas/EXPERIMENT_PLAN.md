# C242 experiment and certification plan

## Frozen question

Can one turn the Reeb flow on a four-dimensional ellipsoid into a complete,
reproducible finite atlas of simple coordinate orbits, iterates, transverse
return multipliers, and Conley--Zehnder indices while exposing the rational
Morse--Bott boundary rather than silently applying the irrational formula?

## Claim-driven tests

1. Reconstruct the two coordinate families from the explicit diagonal flow and
   certify that an orbit with both coordinates nonzero closes only when
   \(a/b\in\mathbb Q\).
2. For \(a/b=\sqrt2\) and \(1/\sqrt2\), enumerate \(k=1,\ldots,12\) for both
   axes. Use integer-square inequalities for every floor and high precision
   only for the displayed cosine/sine pair.
3. For \(2/1,3/2,5/3\), check \(qa=pb\), the common period, full-boundary
   Morse--Bott family, unit transverse return, and explicit null CZ field.
4. Run an independent schema checker, SymPy identities, byte replay, and a
   29-case repaired-hash mutation suite. Compile the manuscript twice per
   revision under a fixed epoch and close the content-addressed manifest.

## Falsifiers and boundaries

Any non-square-certified floor, a missing non-coordinate closed orbit in the
irrational rows, a rational row that reports a nondegenerate CZ integer, a
changed source/evaluator lock, or a non-reproducible byte stream is a release
failure. The calculation has no arithmetic labels and therefore cannot pass
the A0 arithmetic gate or A2 target-match gate.
