# HCS-C54 research question

## Primary question

For the source-ordered cubic--quadric tower

\[
X_n=V(C_n,Q_{n,\rho})\subset\mathbf P_K^{2n-1},
\]

can one classify the full projective monomial symmetry for every row and,
without changing the split-prime Euler object, classify exactly when the
rational exponent \(4/n\) is realized by an actual finite-rank rational
compatible system?

## Answer

Here “ordinary” means an actual finite-rank compatible realization with
integral multiplicities; it is not \(p\)-adic or Newton-polygon ordinarity.

Yes, with two different quantifier scopes.

1. **Unconditional equation scope.** For every \(n\ge2\), the full
   projective monomial stabilizer of the ideal is
   \(\operatorname{Dih}(C_{3n})\) of order \(6n\).  Its HCS-C53 descent is
   a nonconstant finite etale rational group scheme with two rational
   geometric elements.
2. **Packet-admissible scope.** For every row carrying the stated smooth
   rational pure packets, an ordinary split-trace realization exists if and
   only if \(n\mid4\).  The same classification holds for the stronger
   complete split-factor identity.  The inherited certified rows are only
   \(n=2,3,4\), so the unconditional certified answer is \(n=2,4\).
3. **Third-row symmetry escape hatch.** Over the common geometric group
   \(G_3\), no nonzero central source-isotypic summand has multiplicities
   divisible by three on both pure rails.  Source symmetry therefore does
   not repair the \(4/3\) factor.
4. **Invisible counterpackets.** In the fixed-\(\ell\) category generated
   by finite-dimensional continuous semisimple realizations of the in-scope
   compatible systems, unramified outside a common finite set, a rational
   virtual class invisible outside a relative-Dirichlet-density-zero subset
   of the rational split primes lies in the kernel of restriction to \(G_K\).
   Such a class can change an inert rational extension, but it has rank zero
   over \(K\) and cannot remove either denominator obstruction.

## Why this is an independent paper

HCS-C53 constructs rational descent and identifies the split exponent
\(4/n\).  HCS-C54 does not repackage that construction.  It solves the new
classification problem: it enumerates the universal source group, determines
its rational form, proves an if-and-only-if denominator theorem for every
packet-admissible row, and closes the central-projector and twist-counterpacket
loopholes.

## Questions deliberately left open

- Is \(\operatorname{PMonStab}(C_n,Q_{n,\rho})\) the full projective
  automorphism group in any or all rows?
- Are the source intersections smooth, and do the required packets exist, for
  \(n\ge5\)?
- Does the rank-10 fourth-row core have an honest Calabi--Yau threefold
  carrier?
- Can any global Euler object extend the split-local exponent-one fourth-row
  factor through inert and bad places?

None of these questions is an input to the HCS-C54 theorem.
