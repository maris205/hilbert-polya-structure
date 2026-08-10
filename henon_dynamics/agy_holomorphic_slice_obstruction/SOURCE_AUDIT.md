# HCS-C26 source and prior-work audit

## Audit conclusion

HCS-C26 does not duplicate the earlier holomorphic Hénon pinning and graded
Ruelle programs.  It uses the countable AGY return system selected in C25
and answers the exact operator-space question that C25 left open.  The new
positive-prefix complex domain also produces a scalar determinant and a
chronological algebraic trace formula.  The infinite oscillator twist is
then tested on that same domain rather than on an unrelated analytic model.

## Primary-source passports

### S1. Avila--Gouëzel--Yoccoz induced map

- Artur Avila, Sébastien Gouëzel, and Jean-Christophe Yoccoz,
  *Exponential Mixing for the Teichmüller Flow*, Publications
  Mathématiques de l'IHÉS **104** (2006), 143--211.
- Published article: <https://www.numdam.org/item/PMIHES_2006__104__143_0/>
- Preprint: <https://arxiv.org/abs/math/0511614>
- DOI: `10.1007/s10240-006-0001-5`.
- **Use in C26:** the strongly positive neat prefix; the return-branch
  grammar in Section 4.1.3 and Lemma 4.4 (pp. 162 and 165); the inverse
  Jacobian and roof formulas; uniform real expansion/distortion; and
  exponential tails.  C26 combines the published grammar with chronological
  Rauzy multiplication to deduce `B_gamma^T=P C_gamma`.
- **Firewall:** the published formula is authoritative.  The common complex
  cone and holomorphic weight estimates are C26 deductions, not statements
  attributed to AGY.  The invariant density is only `C_b^1`; C26 does not
  holomorphically normalize by it.

The relevant published construction makes every nontrivial branch path have
the form `gamma_* gamma_0 gamma_*` (with `gamma_*` itself also a branch).
Because later Rauzy arrows multiply on the left, transposition places the
fixed positive length-matrix factor on the left.  This C26 algebraic
deduction, rather than real Hilbert contraction in isolation, is what
permits the uniform complex domain.

### S2. Holomorphic transfer nuclearity and trace formulas

- Oscar F. Bandtlow and Oliver Jenkinson,
  *On the Ruelle Eigenvalue Sequence*, Ergodic Theory and Dynamical Systems
  **28** (2008), 1701--1711.
- Preprint: <https://arxiv.org/abs/0802.1468>
- DOI: `10.1017/S0143385708000059`.
- **Use in C26:** strongly nuclear holomorphic map-weight systems, favorable
  spaces, wordwise trace convergence, and the fixed-point trace formula.

- Oscar F. Bandtlow and Oliver Jenkinson,
  *Explicit Eigenvalue Estimates for Transfer Operators Acting on Spaces of
  Holomorphic Functions*, Advances in Mathematics **218** (2008), 902--925.
- Preprint: <https://arxiv.org/abs/0802.1638>
- DOI: `10.1016/j.aim.2008.02.005`.
- **Use in C26:** compactly contained branch images plus summable holomorphic
  weights imply an exponential singular-value class on Bergman space.  In
  complex dimension three this is `E(c,1/3)`, hence trace class.
- **Firewall:** C26 verifies the common domain, compact containment, one
  principal logarithm, and countable weight sum before invoking either
  paper.  A scalar trace-class theorem is not silently transferred to the
  infinite-dimensional vector fibre.

### S3. Infinite oscillator character boundary

- Teruji Thomas, *The Character of the Weil Representation*, Journal of the
  London Mathematical Society **77** (2008), 221--239.
- Preprint: <https://arxiv.org/abs/math/0610644>
- DOI: `10.1112/jlms/jdm098`.
- **Use in C26:** scope only.  The Weil character is a representation
  character/distribution; it is not an ordinary trace of an isolated
  infinite-dimensional unitary.

- Joachim Hilgert, *A Note on Howe's Oscillator Semigroup*, Annales de
  l'Institut Fourier **39** (1989), 663--688.
- Article: <https://aif.centre-mersenne.org/item/AIF_1989__39_3_663_0/>
- DOI: `10.5802/aif.1182`.
- **Use in C26:** scope only.  Analytic oscillator extensions live in a
  constrained semigroup and the Schrödinger and Bargmann--Fock versions are
  intertwined.  Merely complexifying the AGY base does not insert such a
  semigroup cocycle.

### S4. Vector-valued analytic composition boundary

- José M. Bonet, M. Carmen Gómez-Collado, David Jornet, and Elke Wolf,
  *Operator-Weighted Composition Operators between Weighted Spaces of
  Vector-Valued Analytic Functions*, Annales Academiæ Scientiarum Fennicæ
  Mathematica **37** (2012), 319--338.
- Article: <https://afm.journal.fi/article/view/135399>
- DOI: `10.5186/aasfm.2012.3723`.
- **Use in C26:** related-work boundary.  Vector-valued compactness depends
  on the operator weight/fibre; strict contraction of the scalar base is not
  by itself a fibre compactifier.

### S5. Finite Weil next door

- Shamgar Gurevich and Ronny Hadani,
  *Quantization of Symplectic Vector Spaces over Finite Fields*, Journal of
  Symplectic Geometry **7** (2009), 475--502.
- Preprint: <https://arxiv.org/abs/0705.4556>
- DOI: `10.4310/JSG.2009.v7.n4.a4`.
- **Use in C26:** future-model source.  For odd finite fields the construction
  supplies a canonical finite Weil representation.  C26 proposes using it
  only after reduction of the exact chronological symplectic cocycle.

## Internal theorem dependencies

### D1. HCS-C24 discrete metaplectic atoms

File:
[`../rauzy_metaplectic_obstruction/THEOREM_PACKAGE.md`](../rauzy_metaplectic_obstruction/THEOREM_PACKAGE.md).

C24 proves that an `ell^1` sum of distinct metaplectic atoms has essential
norm at least the `ell^2` coefficient norm.  C26 invokes this theorem after
evaluation; it does not claim a new proof of coherent-state separation.

### D2. HCS-C25 exact AGY family

Files:

- [`../agy_metaplectic_transfer_obstruction/SOURCE_AUDIT.md`](../agy_metaplectic_transfer_obstruction/SOURCE_AUDIT.md);
- [`../agy_metaplectic_transfer_obstruction/THEOREM_PACKAGE.md`](../agy_metaplectic_transfer_obstruction/THEOREM_PACKAGE.md);
- [`../agy_metaplectic_transfer_obstruction/results/c25_certificate.json`](../agy_metaplectic_transfer_obstruction/results/c25_certificate.json).

C25 supplies:

- the exact strongly positive neat length-128 prefix;
- the full countable return family and correct roof/Jacobian convention;
- real branch-norm summability for `Re(s)>-sigma_0`;
- the all-length fixed-start matrix decoder;
- the full-rank `H(2)` symplectic projection;
- the exact matrix, point, normalizer, and Jacobian used in C26.

The finite length-22 decoder replay remains a mutation sentinel.  The
all-length theorem, not that finite ledger, closes atom collisions.

## Duplication audit against the Hénon track

| Earlier line | What it already did | Why C26 is different |
|---|---|---|
| Hénon pinning / residue programs | Finite-word holomorphic pinning kernels and determinant blueprints | C26 treats the published countable AGY induced map and an infinite oscillator fibre. |
| Hénon graded Ruelle complex | Conditional finite-alphabet nuclear/Lefschetz construction | C26 proves its common complex domain and countable weight sum from a fixed positive Rauzy prefix. |
| C24 Rauzy--metaplectic obstruction | Abstract discrete-atom theorem and finite singular-cycle evidence | C26 creates the actual scalar holomorphic determinant and applies the atom theorem through evaluation. |
| C25 AGY transfer obstruction | Noncompactness on vector `C_b^1` and normalized `L^2` using branch/local measure structure | C26 removes the localizer and proves a same-domain scalar/twisted dichotomy on Bergman space. |

## Claim--evidence matrix

| Claim | Evidence | Status |
|---|---|---|
| One complex domain works for all AGY inverse branches | AGY branch grammar plus chronology; C26 deduction `A_gamma=P C_gamma` and complex-cone Lemma 2.1 | Proved |
| Complex weights use one logarithm and have an `ell^1` sup sum | Right-half-plane sector, uniform comparison with one real point, C25 real sum | Proved |
| Scalar `L_s` is trace class on `A^2(Omega)` | Verified Bandtlow--Jenkinson hypotheses in complex dimension three | Proved |
| Scalar word trace is `lambda^(-(s+1))/chi'(lambda)` | Exact normalizer telescoping and quotient derivative determinant | Proved; exact examples are computationally replayed |
| Literal vector Bergman branch sum is bounded | Uniform evaluation on the common compact image plus complex weight sum | Proved |
| The oscillator-twisted operator is noncompact | Exact evaluation slice, C25 atom injectivity, C24 essential-norm theorem | Proved |
| Ordinary infinite-fibre Fredholm determinant fails | Noncompactness excludes trace class and nuclear determinant class | Proved with ordinary-theory scope |
| Finite Weil fibres are the next viable arithmetic model | Finite representation source and C26 obstruction analysis | Proposed, not yet tested |
| Any determinant zeros match Riemann zeros | No evidence | Not claimed |

## Citation integrity notes

- Bibliographic metadata is inherited only from the verified C24/C25
  bibliography or checked against the DOI/article landing page.
- The complex cone proof is self-contained and is not attributed to a source
  that proves only real contraction.
- “Algebraic unit” follows from `A_word in SL(4,Z)`.  No prime-orbit law,
  automorphic identification, field discriminant identity, or RH conclusion
  is inferred from that fact.
- All claims about trace and determinant explicitly distinguish scalar
  Bergman trace class from the unsmoothed infinite oscillator fibre.
