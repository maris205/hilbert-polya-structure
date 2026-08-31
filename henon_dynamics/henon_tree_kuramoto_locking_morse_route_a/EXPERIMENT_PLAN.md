# Exact experiment plan

## Frozen regression family

- Enumerate all labeled trees for `2 <= N <= 7` from all Prüfer words in
  lexicographic order: `18,248` trees in total.
- Root every tree at vertex `0` and orient each edge from parent to child.
- Construct rational Pythagorean values for `F_e/K_e`, so every strict edge
  has an exact rational absolute cosine.
- Cycle deterministically through three regimes: all cuts strict, one cut
  saturated, and one cut violated.
- Recover `eta=B F` and `omega=Omega*1+eta`, then independently recover every
  subtree cut sum from `omega`.

## Gates

1. Producer schema, source, epoch, evaluator and scope locks.
2. Independent Prüfer decoding and rooted topology reconstruction.
3. Exact `B F=eta` and every child-subtree cut identity.
4. Exhaustive inverse-sine branch counts and binomial Morse histograms.
5. Exact saturated nullity and violated-cut no-solution labels.
6. Fresh SymPy incidence, congruence and determinant identities.
7. Two byte-identical producer replays.
8. Rehashed hostile semantic mutations all rejected.
9. Three substantively different PDFs, two fresh builds per round, embedded
   fonts, clean logs and final manifest closure.

Finite enumeration is a convention and implementation oracle.  The all-size
theorem rests on the analytic tree proof, not on extrapolation from `N<=7`.
