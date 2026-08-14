# Paper Plan — SD-C24

**Title:** *Cofactor Holonomy on the Successor–Divisor Shift: Exact Class
Resolution and a Fredholm Trilemma*  
**Type:** mathematical theory with exact finite-audit protocol  
**Format:** anonymous A4 article  
**Primary family:** Symbolic Dynamics  
**Target length:** 15–18 pages including references and appendices  
**Review loop:** intentionally omitted by project instruction

## Claims–evidence matrix

| Claim | Evidence | Status | Manuscript location |
|---|---|---|---|
| The cofactor label is intrinsic to the frozen full-shift skeleton | \(S(F_n)\cong F_d\boxtimes F_q\iff n+1=dq\) | proved | Sections 2–3 |
| Every closed path has integer holonomy \(Q\ge2\) | telescoping product \(Q=\prod(1+1/n)\) | proved | Section 4 |
| The neutral group extension has no periodic paths | identity holonomy is impossible | proved | Section 4 |
| The cocycle is gauge-reducible to a source potential | \(q=(n/d)(1+1/n)\) | proved | Section 4 |
| \(Q=2\) is exactly the canonical family \(C_k\) | one cofactor \(2\), all others \(1\) | proved | Section 5 |
| Atomic holonomy \(p\) is exactly \(C_{k,p}\) | atomic factorization of the cofactor word | proved | Section 5 |
| Haar extraction gives exact connected class coefficients | finite fixed-period support plus character orthogonality | proved | Section 6 |
| The two-parameter \(\mathcal S_1\) domain has two sharp inequalities | rank-one row sum, fixed-row obstruction, successor Fourier extraction | proved | Section 7 |
| The regular lift is semifinite \(L^1\) but ordinarily noncompact | row calculation versus deck translations | proved | Section 8 |
| The neutral semifinite determinant equals one | every identity-holonomy trace vanishes | proved | Section 8 |
| Pure cofactor, endpoint regularization, and character twists form a trilemma | successor noncompactness, factorial damping, phase invariance | proved | Section 9 |
| Positive inventories preserve the canonical support | weights do not change graph or holonomy | proved | Section 10 |
| The exact candidate theorem package was not found in the bounded search | documented primary-source search | search-bounded | Section 2 |
| The candidate fails the prime Euler ledger | infinite \((p,k)\) multiplicity and wrong roofs | proved | Section 11 |

## Argument blueprint

### Core claim

The successor–divisor cofactor is a genuine and exactly resolvable symbolic
holonomy, but its abelian product creates a sharp analytic/arithmetic
trilemma rather than a prime Euler determinant.

### Reasoning chain

1. The same factor witness that creates an edge supplies a unique positive
   cofactor label.
2. Telescoping turns the cycle product into a strictly positive source
   potential, so the neutral group sector is empty.
3. Atomic holonomy forces a single nontrivial edge and yields an exact family
   \(C_{k,p}\), not one orbit per atom.
4. Character Fourier inversion resolves each class in the connected
   Fredholm ledger without deleting it.
5. A rank-one output-row decomposition gives the exact two-parameter
   trace-class phase diagram.
6. Pure cofactor weight violates compactness through the cofactor-one spine;
   endpoint weight repairs compactness only by factorial damping.
7. Unitary characters supply phases only, while the regular identity trace
   kills every orbit.
8. The resulting same-object mathematics is positive, but the target
   primitive/repetition ledger is rejected before any zero comparison.

### Counterarguments handled

- **“The neutral group trace selects desired recurrence.”**  It selects no
  recurrence; the local determinant is one.
- **“Semifinite \(L^1\) means an ordinary Fredholm determinant.”**  The deck
  lift is ordinarily noncompact, and the two trace notions are separated.
- **“A scalar character can cancel composite lengths.”**  Every \(C_k\)
  carries the same nonzero phase \(\chi(2)\); Fourier resolution removes
  cross-class cancellation as evidence.
- **“Drop the endpoint roof.”**  The successor component becomes an
  unweighted unilateral shift and the pure matrix is noncompact whenever
  bounded.
- **“Change the inventory.”**  Any positive inventory changes magnitudes but
  preserves the full canonical support.

## Section plan

### Abstract

State the positive holonomy, \(Q=2\) classification, exact connected
coefficient, sharp \(\mathcal S_1\) domain, and trilemma.  No citations.

### 1. Introduction

Frame the class-resolution question inherited from the cycle flood.  State
four contributions and the strict Route boundary.

### 2. Classical boundary

Synthesize shift determinants, twisted dynamical \(L\)-functions, voltage
graphs, graph-cover zetas, cocycle cohomology, and trace ideals.  State the
search-bounded novelty sentence.

### 3. Source and frozen operators

Define the full-shift skeleton, successor–divisor graph, cofactor cocycle,
roofs, scalar/character operators, regular lift, and determinant conventions.

### 4. Positive holonomy and gauge

Prove \(Q=\prod(1+1/n)>1\), neutral-sector extinction, and the exact gauge
decomposition.  Include the source/extension TikZ figure.

### 5. Exact atomic classes

Classify \(Q=2\) and \(Q=p\), prove primitivity and repetition exclusion, and
include the canonical-spine TikZ figure.

### 6. Character-resolved connected ledger

Use confinement, Haar extraction, and the trace logarithm to derive exact
\(\mathcal H_m\), \(\mathcal H_2\), and \(\mathcal H_p\) formulas.

### 7. Sharp two-parameter trace-class theorem

Give the row-nuclear sufficiency proof and both independent necessity
arguments.  State holomorphy and the character-fiber corollary.

### 8. The regular lift

Prove the semifinite \(L^1\) threshold, ordinary noncompactness, and trivial
neutral local determinant as three distinct statements.

### 9. Fredholm trilemma

Contrast pure cofactor, endpoint-regularized, and unitary-character choices.
Prove the first-return collapse statement.

### 10. Controls and scoped no-go

Prove abelian-holonomy blindness and arbitrary-inventory persistence.  State
the exact audit protocol without presenting computation as proof.

### 11. Route evaluation

Compare to the marked prime Euler ledger, freeze the tuple, reject Route A,
and lock Route B.

### 12. Conclusion

Restate the positive structural result and the closed abelian-product branch.

### Appendices

Give proof details for fixed-period support, trace-norm holomorphy, first
return, regular lifts, and a complete claim/route firewall.

## Figure plan

| ID | Type | Content | Source | Priority |
|---|---|---|---|---|
| Figure 1 | pure TikZ structural diagram | base cocycle, regular extension, character fibers, and neutral trace | definitions and Theorems 4.1–4.3 | high |
| Figure 2 | pure TikZ cycle/trilemma diagram | \(C_k\), one \(q=2\) return, and the three analytic choices | Theorems 5.1 and 9.1–9.3 | high |

No convergence plot is used to infer the sharp boundary.

## Table plan

1. nearest-literature boundary;
2. atomic holonomy class formulas;
3. ordinary versus semifinite lift distinctions;
4. Fredholm trilemma;
5. inventory controls;
6. strict Route-A claim ledger.

## Citation plan

- Introduction and determinant setup: Bowen–Lanford, Parry–Pollicott, Simon.
- Twists and extensions: Adachi–Sunada, Gross–Tucker, Stark–Terras, Clair,
  Sharp.
- Cohomology language: Kalinin, cited only for the general periodic-data
  context, not for the elementary candidate identity.
- Recent weighted graph-zeta adjacency: Ishikawa–Morita.
- All candidate-specific identities cite internal theorems.

## Page allocation

| Part | Pages |
|---|---:|
| Abstract/status/Introduction | 2.0 |
| Literature and frozen source | 2.0 |
| Holonomy and class resolution | 3.0 |
| Trace class and lift distinction | 3.5 |
| Trilemma, controls, route | 2.5 |
| Conclusion | 0.5 |
| References and appendices | 3–5 |

## Quality locks

- No prime or zero table in the source.
- No target-zero evaluation.
- No review loop.
- No determinant-versus-trace-log coefficient ambiguity.
- No ordinary-versus-semifinite determinant ambiguity.
- No pure-cofactor-versus-endpoint series ambiguity.
- Both \(\mathcal S_1\) boundary mechanisms appear in the theorem statement
  and proof.
- No global log determinant or primitive product at \(z=1\) without proof.
- No A3 credit for same-object Fredholm analyticity.
- No claim of absolute literature priority.

