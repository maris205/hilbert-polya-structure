# Exact experiment plan — HCS-C248

This is a proof-and-receipt experiment, not a floating-point simulation.

* Generate the fixed point through length 1024 and verify the four-letter
  substitution matrix and its positive cube.
* Generate \(P_k,Q_k\) for \(0\le k\le10\), checking every coefficient, energy
  sum, and bound certificate.
* Generate \(R,S,T,U\) Laurent coefficient ledgers for \(0\le k\le7\) and
  independently verify all four shifted recurrences.
* Record 64 exact finite aperiodicity mismatches and the declared Cesàro/van
  Hove diffraction boundary.
* Run the producer-independent checker, SymPy cross-check, byte replay, and
  42 hostile mutations (including repaired payload hashes).
* Compile three content-distinct LuaLaTeX revisions twice each with
  `SOURCE_DATE_EPOCH=1788048000`; retain only settled PDFs and reports.

All arithmetic in the certificate is integer or symbolic exact arithmetic.  A
finite receipt is never promoted to a periodic-orbit or target-arithmetic
claim.
