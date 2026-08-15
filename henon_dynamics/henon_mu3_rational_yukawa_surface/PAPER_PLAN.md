# HCS-C55 paper plan

Title: **A Four-Parameter CY3-Type Variation and Its Rational Yukawa Cubic**

Status: **DOCS_FINAL_NO_MORE_EDITS; the exact release-candidate tuple,
independent semantic/source/visual audit, and official compilation passed**.

One-sentence contribution: **The paper algebraizes the four-dimensional
rational equivariant deformation core of a \((2,3)\) Fano fivefold and
computes its rank-\(10\) CY3-type variation's exact projective Yukawa cubic,
whose zero locus is a smooth geometrically irreducible cubic surface over
\(\mathbf Q\).**

Paper type: theory plus exact symbolic verification.

Target: algebraic-geometry/Hodge-theory research article; no journal is
selected yet, so no venue-specific page limit or style is frozen.

## 0. Claims--evidence matrix

| Claim | Evidence | Current status | Paper location |
|---|---|---|---|
| A rational algebraic four-germ realizes all invariant abstract deformations | AKN and Kodaira vanishings, Hilbert tangent/obstruction theory, Romagny fixed-point smoothness, exact invariant dimension | PASS | Sections 2--3, Appendix A |
| The norm graph cuts a polarized rank-\(10\) CY3-type VHS after \(\mathbf Q(1)\) | finite group-scheme action, correspondence algebra, released central Hodge ledger | PASS | Section 4 |
| The projected period map is locally immersive | Hilbert-slice KS isomorphism and multiplication-by-\(y\) map | PASS | Section 5 |
| The projective Yukawa tensor is the displayed rational cubic | Nagel/Konno operator and pairing theorems, top-line descent, \(20\) reductions, direct-cube reconstruction | PASS | Section 6, Appendix B--C |
| Its zero locus is smooth and geometrically irreducible | exact gradient Hilbert series, length \(16\), independent quotient, geometric argument | PASS | Section 7, Appendix C |
| Cubic mismatch obstructs an honest four-modulus CY3 VHS realization | functoriality of Hodge line, connection, and polarization | proof complete | Section 8 |
| BCD quotients are currently comparable | full four-variable comparator tensor absent | NO; NOT-COMPARABLE-WITH-CURRENT-DATA | Section 9 |

## 1. Paper-level claim

Construct a four-dimensional rational algebraic equivariant deformation germ
of the HCS \((2,3)\) fivefold, extend the nonconstant Reynolds core over it,
prove local maximality of the resulting rank-\(10\) CY3-type VHS after the
exact twist \(\mathbf Q(1)\), compute its projective rational Yukawa cubic,
and prove that the cubic cuts out a smooth geometrically irreducible surface.
Then formulate projective cubic equivalence as a necessary honest-CY3
realization gate.

## 2. Proposed section structure

### Abstract

- one sentence on the rational descended fivefold and rank-\(10\) core;
- one sentence on the Hilbert-slice algebraization;
- one sentence on the exact cubic and smooth cubic surface;
- one sentence limiting the CY3 comparison to a necessary VHS gate.

No claim of an honest CY3 or motive.

### 1. Introduction

- relation to HCS-C52--C54;
- why Hodge numbers alone are insufficient;
- the role of a four-variable Yukawa tensor;
- statement of the four theorem parts;
- explicit list of scope firewalls.

### 2. The rational source and nonconstant symmetry

- equations over \(K=\mathbf Q(\rho)\);
- rational equation model;
- \(G=\operatorname{Dih}(C_{12})\);
- cocycle
  \(\tau(B^{-1}gB)=B^{-1}\delta(g)B\);
- descended ambient action and equation covariance.

The section must distinguish rank \(24\) from two rational points.

### 3. Algebraic equivariant deformation germ

- adjunction and \(H^2(T_X)=0\);
- normal bundle and \(H^1(N)=0\);
- Euler sequence and embedded KS surjectivity;
- Romagny fixed-locus smoothness;
- invariant tangent dimension from the exact Cayley certificate;
- rational transverse four-slice and restricted universal family;
- formal comparison with the fixed Kuranishi germ.

State explicitly that the whole fixed Hilbert germ need not have dimension
four and that no literal linear family is used.

### 4. Relative Reynolds core

- norm graph definition over the finite etale group scheme;
- idempotence and self-transpose;
- action on \(R^5f_*\mathbf Q\);
- central comparison with \(\pi_5e_{\mathscr G}\);
- rank and Hodge ledger;
- exact twist \(\mathbf Q(1)\);
- polarization and local constancy.

No relative Chow--Künneth decomposition.

### 5. Local maximality and Cayley operators

- Nagel/Konno residue and multiplication locators;
- \(R_{1,0}\) tangent operators;
- multiplication by \([y]\);
- exact four-dimensional first-image isomorphism;
- period-map immersion.

Include the FIK Section 5.6 warning that already contracted
\(R_{2,-3}\) classes are not simply multiplied inside the same bigrading.

### 6. The projective Yukawa cubic

- bidegree table;
- the three Gauss--Manin derivatives;
- the four roles
  \([yp]\), \([y^2p]\), \([y^4p^3]\), \([y^5p^3]\);
- the semilinear convention \(D(y)=y,D(z)=\rho z\) and the top-line
  descent calculation;
- perfect top pairing and common scalar;
- rational tangent basis;
- all \(20\) trace entries and \(1/3/6\) convention;
- displayed primitive polynomial.

### 7. The Yukawa cubic surface over Q

- exact partial derivatives;
- gradient quotient of length \(16\);
- Hilbert series \((1+t)^4\);
- independent projective saturation;
- geometric smoothness;
- geometric irreducibility from smoothness;
- clarification that “rational cubic” means defined over \(\mathbf Q\), not
  that the surface is proved \(\mathbf Q\)-rational;
- basis/projective invariance.

### 8. Honest-CY3 realization gate

- functoriality of Yukawa under pointed VHS isomorphism;
- projective \(\operatorname{GL}_4(\mathbf C)\) necessity;
- central-fiber versus family-level correspondence;
- hierarchy: cubic, jets, connection, monodromy, arithmetic, correspondence;
- why a match does not imply a motive.

### 9. BCD comparator audit

- generic \(\operatorname{Dic}_3\) and \(\mathbf Z_{12}\) quotient
  families;
- absence of a published full four-variable tensor in the bounded search;
- non-substitution of the mirror-side one-parameter calculation, and
  rejection of the nodal locus as a smooth substitute;
- exact current label
  NOT-COMPARABLE-WITH-CURRENT-DATA.

This section is an audit, not a named no-go theorem.

### 10. Exact replay and declarations

- frozen upstream hashes;
- producer/checker independence;
- scalar-leaf inventory and rebound sweep;
- negative mutation table;
- artifact and software provenance;
- machine-assisted versus conceptual proof boundary.

### Appendix A. Cohomology details

- adjunction;
- Kodaira/AKN vanishings;
- exact sequences;
- proof of the rational transverse-slice lemma.

### Appendix B. Cayley stage and normalization ledger

- all bidegrees;
- stage constants;
- top monomial;
- basis transformation;
- multinomial convention.

### Appendix C. Exact coefficient and gradient tables

- \(20\) symmetric traces;
- \(20\) primitive coefficients;
- four partial derivatives;
- Hilbert-function table.

## 3. Theorem numbering

- Theorem A: algebraic rational equivariant four-germ.
- Proposition B1: relative Reynolds idempotent.
- Theorem B: rank-\(10\) locally maximal CY3-type VHS.
- Theorem C: exact rational Yukawa cubic and smooth cubic surface.
- Theorem D: honest-CY3 necessary gate.
- Comparator Remark E: current BCD non-comparability.

## 4. Planned tables

1. claim/source/internal-certificate boundary;
2. Hodge and Tate-twist ledger;
3. Cayley stage/bidegree ledger;
4. \(20\)-coefficient tensor table;
5. exact gradient-algebra checks;
6. realization discriminator hierarchy;
7. hostile mutation outcomes.

No figure is required unless the final cubic-surface geometry yields a
mathematically informative visualization; aesthetic illustration alone is
out of scope.

## 5. Writing gates

The main mathematical prose was frozen after:

- the producer/checker agree on \(R_{1,0}\), multiplication by \(y\), top
  descent, all \(20\) traces, and direct cube reduction;
- the scalar-leaf fail-open is closed;
- the independent hostile read-only audit passes; no unpackaged temporary
  hash is promoted.

The abstract, conclusion, and exact-replay section are complete. The PDF and
its hash are generated only after every theorem-dependent field is frozen.

## 6. Independent outline review

The hostile mathematical review found no theorem blocker after checking:

- nonconstant group-scheme fixed-point smoothness;
- fixed Hilbert germ versus rational four-slice;
- the \(146-63\) dimension firewall;
- omission of relative Chow--Künneth claims;
- the full \(y,yp,y^2,y^3,y^4,y^5\) stage ledger and common scalar;
- the corrected convention \(D(z)=\rho z\).

The independent machine gates, exhaustive scalar-leaf rebound sweep, and
paper source audit pass. No theorem or source revision remains before the
single official clean build.
