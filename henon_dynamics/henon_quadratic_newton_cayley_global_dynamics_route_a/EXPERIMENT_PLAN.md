# HCS-C257 exact verification plan

## Claim contract

The theorem is analytic and all-state.  Computation must verify exact algebra,
integer orbit ledgers, root-order tails, and release provenance; a finite
receipt is not used to infer the theorem.

## Gates

1. Freeze $p_a,N_a,C_a$, $a\ne0$, source commit, evaluator hash, epoch,
   scope, and nonclaims.
2. Derive the Cayley conjugacy, inverse, basin inequalities, iterate formulas,
   root-error identities, critical points, and scale covariance independently.
3. Recompute $F_n,P_n,O_n$ for $1\le n\le16$ by Möbius inversion.
4. Recompute exact tails and periods for every root order $1\le m\le128$.
5. Check the Cauchy boundary map on an exact rational grid and the zeta
   logarithmic derivative through order 12.
6. Require producer-independent checking, SymPy reconstruction, clean-process
   byte replay, and at least 20 repaired-hash hostile mutations.
7. Build three substantively different LuaLaTeX rounds twice each under
   `SOURCE_DATE_EPOCH=1788048000`; require byte identity, embedded/subset fonts,
   clean logs, extractable theorem/verdict/scope text, and visual inspection.
8. Hash exactly 27 payloads in a self-excluded manifest.

## Failure policy

Any mismatch blocks release.  In particular, a repaired payload hash may not
hide a changed theorem, period count, tail, citation, evaluator tuple, or scope
flag.  No passing finite prefix can be promoted to arithmetic evidence.
