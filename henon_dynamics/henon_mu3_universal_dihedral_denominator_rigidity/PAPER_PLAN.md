# HCS-C54 paper plan

## Working title

**Universal Dihedral Symmetry and Split-Denominator Rigidity in a
Cubic--Quadric Source Tower**

The title says “symmetry,” not “full automorphism group,” and says “split” to
prevent a global-root reading.

## One-sentence contribution

The paper proves that the full projective monomial ideal stabilizer of the
source tower is \(\operatorname{Dih}(C_{3n})\) for every \(n\ge2\), and
that an actual rational compatible system realizes the prescribed complete
split-local exponent \(4/n\) in a packet-admissible row exactly when
\(n\mid4\).

## Central theorem hierarchy

1. **Theorem A:** universal projective monomial source group and support exact
   sequence.
2. **Theorem B:** nonconstant rational group form with exactly two rational
   geometric elements.
3. **Theorem C:** split-trace and complete split-factor ordinary realization
   if and only if \(n\mid4\), for packet-admissible rows.
4. **Theorem D:** exact \(n=3\) common-geometric-group character and central
   source-sector no-go.
5. **Proposition E:** split-invisible counterpackets restrict to zero and
   cannot alter the \(K\)-side obstruction.

## Claims-evidence matrix

| Claim | Formal evidence | Exact control | Main location |
|---|---|---|---|
| full group \(\operatorname{Dih}(C_{3n})\) | ideal grading, recurrence, parity closure, presentation | scans and small-row brute force | Sections 2--3 |
| rational group form | semilinear generator transport, congruences | fixed points through row 256 | Section 4 |
| ordinary iff \(n\mid4\) | fixed-\(\ell\) semisimplification, K0 identity, purity, rank divisibility, converse | divisor table and scan | Section 5 |
| no \(n=3\) central sector | exact Cayley/Fermat characters | quotient/group-law replay | Section 6 |
| twist kernel does not help | restriction-zero theorem | explicit kernel example | Section 7 |

## Section plan

1. **Introduction.** State the classification question, the two quantifier
   scopes, the answer \(n=2,4\), and the global firewall.
2. **Source ideal and category.** Define the weighted pair and prove that ideal
   stabilization preserves both equation lines.
3. **Universal monomial symmetry.** Derive the edge recurrence, prove
   exhaustiveness, and identify \(\operatorname{Dih}(C_{3n})\).
4. **Rational group form.** Recall only the descent datum needed for transport,
   prove the generator formulas, count rational points, and separate Reynolds
   averaging from transfer.
5. **Split-denominator rigidity.** Define packet-admissibility and the local
   logarithm, prove the fixed-\(\ell\) K0 identity, separate weights, give the
   divisor table, and prove the complete-factor converse.
6. **Exact third-row character.** Build the Cayley quotient, include the
   residue factor, reconstruct both characters, and close the central-sector
   escape hatch.
7. **Counterpackets and global boundary.** State the virtual restriction
   kernel, rational descent caveat, and inert polynomial identity.
8. **Exact replay and limitations.** Record semantic gates and release hashes
   after code promotion; state all exclusions.
9. **Declarations.** Reproducibility, data, ethics, contribution, funding, and
   conflict statements.
10. **Appendix.** Recurrence closure algebra, generator relations, character
    reconstruction, coefficient-orbit check, and optional Fermat diagonal
    refinement with its stronger symmetry assumption.

## Paper-shape decisions

- The all-\(n\) group theorem is the opening technical result.
- HCS-C53 rational equations are recalled only to define the group transport;
  they are not presented as a new contribution.
- HCS-C53 packet data are used without importing a semisimplicity theorem.
- The main arithmetic theorem uses both weights.  The total-rank calculation
  appears only as a negative control.
- The exact \(n=3\) character is supporting theorem mass, not a substitute for
  the universal classification.
- The optional full Fermat diagonal-sector argument stays in the appendix
  because the complete-intersection rail does not carry that full diagonal
  group.
- No fixed-prime Frobenius table appears.
- No CY3 candidate or Gate-B realization claim enters the contribution list.

## Abstract checklist

- [x] Starts with the actual group and denominator classifications.
- [x] Defines full as projective monomial ideal stabilizer.
- [x] Separates all-\(n\) equation algebra from packet-admissible rows.
- [x] States inherited packet rows \(2,3,4\) without semisimplicity promotion.
- [x] States the complete split-factor iff result.
- [x] Includes the \(n=3\) common-group no-go and twist caveat compactly.
- [x] Excludes inert/global root and analytic promotion.

## Finalization status

- [x] Insert exact semantic-gate and unit-test counts after release promotion.
- [x] Insert certificate, payload, independent-check, schema, and scoped
  code/results-manifest hashes.
- [x] Perform the one final clean compile against those stable identifiers.
- [x] Run citation, warning, box, font, byte, delimiter, and visual-page
  audits.
