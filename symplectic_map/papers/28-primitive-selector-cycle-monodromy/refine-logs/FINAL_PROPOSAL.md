# Paper 28 final refined proposal

## Public-safe working title

Primitive Newton-Selector Cycles in Permutation-Twisted Hamiltonian Shears:
Normal-Fan Classification and Exact Monodromy

## Final theorem contract

Let \(\mathsf w\) be any rooted primitive selector-pair word of length
\(\ell\ge3\).  The paper constructs one fixed autonomous polynomial
symplectomorphism \(F_{\mathsf w}\) over a characteristic-zero field, on
\(2(\ell+1)\) affine symplectic coordinates, with positive-support,
equal-total collected supports and arbitrary nonzero displayed coefficients.  For an
explicit spike position weight and every positive momentum weight in the
exact first-carry chamber:

1. the prescribed support-pair word is selected strictly and endogenously;
2. strict selector feasibility in the general equal-total class is exactly
   membership in an open rational normal-fan intersection;
3. the max-plus degree transport is the actual polynomial weighted-degree
   transport, with coefficient-uniform leading-form survival;
4. both the selector word and the position-weight orbit modulo the diagonal
   line have least period \(\ell\);
5. the ordered prefix products and period monodromy have closed rank-one
   formulas; and
6. the marked monodromy recovers the rooted ordered support-vector word by a
   carry-free base-\(\lambda\) expansion.

With the labelled support dictionary, literal pair labels are recovered.
Without literal names, recovery is only up to independent renaming of the V
and W alphabets.  Without a marked phase, only the cyclic class is intrinsic.

## Exact construction

Write \(r=\ell+1\), let \(P\) cycle the moving coordinates and fix the star
coordinate, and choose integers \(H\ge2\), \(\rho\ge2\), and \(K\ge1\).  Put

\[
 u_0=\mathbf1+(H-1)e_0,
\]

and encode the occurrence sets \(S_a=\{j:a_j=a\}\) and
\(T_b=\{j:b_j=b\}\) by

\[
 \alpha_a=\rho\mathbf1+K\sum_{j\in S_a}e_j
 +K(\ell-|S_a|)e_\star,
\]

\[
 \beta_b=\rho\mathbf1+K\sum_{j\notin T_b}e_j
 +K|T_b|e_\star.
\]

All totals equal \(D=\rho r+K\ell\).  The selected matrices are

\[
 C_{a,b}=P+\mathbf1c_{a,b}^{\mathsf T},\qquad
 c_{a,b}=(D-1)\alpha_a-\beta_b,
\]

and \(\lambda=(D-1)^2\).  The incidence table gives the desired unique
selectors.  Every existing competitor is separated by
\(g=K(H-1)\); a singleton support has vacuous uniqueness and the full normal
cone, with no finite competitor gap assigned.

## Refinements incorporated

The final proposal incorporates every adversarial correction:

- all general automatic-carry statements assume \(r\ge2\), while the
  headline has \(r=\ell+1\ge4\);
- the exact momentum gate is
  \(0<m_0<A_{\alpha_{a_0}}u_0\), coordinatewise;
  \(0<m_0\le u_0\) is only a convenient sufficient subcone;
- the decoder inputs and outputs distinguish marked/unmarked phase,
  support vectors, labelled dictionaries, and arbitrary alphabet names;
- the position maximum recurrence begins at \(n=0\), whereas the
  complete-state maximum recurrence begins at \(n\ge1\) and extends to
  \(n=0\) iff its initial maximum equals the position maximum;
- moving-coordinate spike formulas and the fixed star-coordinate formula
  are stated separately, and the phase subsequence uses fresh notation;
- exact finite gaps are asserted only against competitors that exist; and
- weighted-degree chamber, tame/affine-triangular, cluster, max-plus,
  monomial-map, and polynomial-symplectomorphism predecessors are treated as
  established neighboring theories rather than folded into the novelty.

## Proof architecture

The main proof is organized as a dependency chain:

\[
 \text{symplectic map}
 \to \text{selected matrices}
 \to \text{normal-fan iff}
 \to \text{incidence realization}
 \to \text{strict carry and survival}
 \to \text{ordered cocycle}
 \to \text{digit decoder}
 \to \text{least periods and recurrences}.
\]

No theorem-critical argument is delegated to an appendix, a program, or a
certificate.  Counterexamples are placed beside the hypotheses they make
necessary.

## Anonymous article plan and mass

| Section | Target pages |
|---|---:|
| Abstract | 0.5 |
| Introduction and bounded positioning | 2.5 |
| Symplectic family and exact degree transport | 3.0 |
| Normal-fan iff | 4.0 |
| Incidence realization of primitive words | 4.0 |
| Strict carries and leading forms | 3.5 |
| Ordered monodromy and decoding | 4.0 |
| Least periods, scalar boundaries, and counterexamples | 3.5 |
| Limitations and conclusion | 1.5 |
| **Total anonymous content** | **26.5** |

References are excluded from the count.  The plan uses zero empirical plots,
zero datasets, and no proof appendix.  At most three hand-typeset tables are
needed.

## Locked anti-claims

The paper does not claim one universal map, fixed dimension, scalar word
decoding, minimal scalar recurrence, ordinary total-degree realization,
dynamical degree or entropy equality, integrability, generic nonconjugacy,
inverse reciprocity, cohomological spectra, positive-characteristic
validity, zero-coordinate support survival, or absolute literature priority.

## Readiness target

Source design is ready only if a fresh independent reviewer finds zero
Blocker, Major, Minor, and Ambiguity items after rederiving the full theorem
contract.  A source-design PASS opens only the later strict source-lock gate;
it does not itself authorize a manuscript or build.

BATCH07_PAPER28_FINAL_PROPOSAL_FROZEN
