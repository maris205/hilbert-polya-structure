# Narrative report

Linear preferential attachment has two scales that are often discussed separately.  A vertex born at a fixed time is repeatedly favored by its accumulated degree and grows on the square-root scale.  The degree population, in contrast, stabilizes after division by the current number of vertices and has a cubic tail.  This package derives both statements from the same convention-locked update.

The local calculation closes at every factorial order.  If a fixed vertex currently has degree `d`, then its rising factorial is multiplied in conditional expectation by `1+r/[2(n-1)]`.  Product iteration gives a gamma quotient.  Order one supplies a nonnegative martingale; the full hierarchy supplies all `Lp` bounds and exact moments of the square-root limit.  Carleman's divergence then identifies the limit law by those moments.

The population recursion is not the fixed-vertex recursion in disguise.  A new leaf enters class one, and the selected old endpoint shifts between adjacent degree classes.  The drift is lower triangular.  Its equilibrium gives `p_k=4/[k(k+1)(k+2)]`, while bounded martingale innovations and a componentwise second-moment induction upgrade the usual mean calculation to `L2` convergence.

Exact enumeration checks both representations through nine vertices.  It does not prove either asymptotic theorem.  The package avoids seed ambiguity, makes no maximum-degree claim, and fails every Route-A branch because the stochastic graph growth carries no target arithmetic or natural operator bridge.
