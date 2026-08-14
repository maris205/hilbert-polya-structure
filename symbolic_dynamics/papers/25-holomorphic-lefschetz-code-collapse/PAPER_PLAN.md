# Paper Plan — SD-C27

**Title:** *Holomorphic Lefschetz Fibers over Logarithmic Codes: Exact
Stability Cancellation, Renewal Flooding, and Atom-Loop Collapse*  
**One-sentence contribution:** a canonical holomorphic de Rham fiber cancels
the fixed-point denominator of every logarithmic-code return at all powers,
but the full graded determinant retracts to degree-zero cohomology, leaving
mixed necklaces in a shared renewal system and only supplied atom loops in a
disjoint system.  
**Type:** mathematical theory with exact symbolic audit  
**Format:** anonymous A4 article  
**Primary family:** Symbolic Dynamics  
**Target length:** 18–22 pages including appendices  
**Review loop:** intentionally omitted by instruction

## Claims–evidence matrix

| Claim | Evidence | Status | Manuscript location |
|---|---|---|---|
| Elias gamma histories have \(O(\log n)\) length and affine ratio \(q_n=2^{-\ell(n)}\) | direct code and derivative calculation | proved | Section 3 |
| A zero-form repetition has trace \(w^r/(1-q^r)\) | holomorphic fixed-point trace; centered monomial spectrum | proved | Section 4 |
| Scalar normalization works at all powers only for \(q=0\) | powers one and two | proved | Section 4 |
| No ordinary trace-class tensor fiber has moments \(1-q^r\) for \(0<|q|<1\) | entire Fredholm determinant versus a forced pole | proved | Section 4 |
| The canonical \(0|1\) de Rham pair has supertrace \(w^r\) at every power | trace subtraction and exact polynomial complex | proved | Section 5 |
| Its graded ratio is \(1-zw\), while the ordinary block determinant is a product | full Fredholm identities | proved/firewalled | Section 5 |
| A shared family has supertrace \((\sum_jw_j)^r\) | ordered-word expansion; finite cohomology quotient | proved | Section 6 |
| Mixed primitive necklaces survive the grading | two-label coefficient ledger and general word formula | proved | Section 6 |
| Disjoint components give \(\prod_j(1-zw_j)\) | direct-sum factorization and cohomology | proved | Section 7 |
| The disjoint result is determinant-equivalent to atom loops for every inventory | surviving diagonal cohomology operator | proved/control | Section 7 |
| The degree-zero modes prevent trace-class continuation through \(\Re s=1\) for primes | divergence of \(\sum_pp^{-\sigma}\) | proved | Section 8 |
| Digit time retains \(u^{\ell(n)}\); return time uses \(z\) | exact marker ledger | proved | Section 8 |
| Classical transfer/Lefschetz technology bounds novelty | primary-source audit | verified | Section 2 |
| A2 succeeds in a graded sense, while A1/A3/A4 fail | theorem ledger | evaluated | Section 10 |

## Argument blueprint

### Core claim

Holomorphic function space is not itself the obstruction.  The canonical
exterior numerator really cancels the analytic stability denominator.  The
obstruction reappears one layer later: cohomology remembers legal return
combinatorics but forgets the logarithmic code fiber that was meant to
explain arithmetic selection.

### Reasoning chain

1. Freeze a prefix-free logarithmic integer code and its affine disk
   contractions.
2. Compute the ordinary zero-form trace and expose \((1-q^r)^{-1}\).
3. Rule out scalar and ordinary tensor repairs at all repetitions.
4. Insert the source-canonical one-form pullback and prove exact cancellation
   at every power and at full determinant level.
5. Expand a shared renewal operator over all return words and show that the
   grading preserves every mixed necklace.
6. Separate the branches and identify the surviving determinant with a
   diagonal atom-loop inventory.
7. Audit marker ownership and the trace-class half-plane.
8. Award scoped A2 credit but close Route A at A1, A3, and A4.

## Section plan

### Abstract

State the scalar/tensor rigidity, canonical graded escape, shared/disjoint
dichotomy, marker firewall, analytic ceiling, and route verdict.  No
citations.

### 1. Introduction

Open with the fixed-point denominator and the missing exterior numerator.
State the positive result before its collapse.  Give five falsifiable
contributions and show the hero diagram.

### 2. Literature boundary

Synthesize Ruelle transfer determinants, Atiyah–Bott/Lefschetz alternating
traces, Bergman nuclearity, exterior-form factorizations, and universal
integer coding.  Present the 2026 preprint only as a non-peer-reviewed
ownership firewall, never as theorem authority.

### 3. Frozen code and analytic object

Define the gamma code, digit maps, affine code branches, Bergman spaces,
finite polynomial complex, two assemblies, determinant convention, and
analytic domain.

### 4. Scalar and ordinary-fiber rigidity

Prove the local trace formula, scalar two-power rigidity, rank-one boundary,
and ordinary trace-class tensor obstruction.  State the nontensor scope
limit.

### 5. Canonical de Rham escape

Give trace, polynomial-cohomology, and centered spectral telescoping proofs.
Place the ordinary-versus-graded firewall in a boxed proposition and table.

### 6. Shared renewal and mixed words

Prove \(\operatorname{Str}L^r=(\sum w)^r\), identify the shared determinant,
enumerate the first mixed necklaces, and generalize to a constrained branch
graph.

### 7. Disjoint components and atom-loop collapse

Factor the degreewise determinants over components, identify the surviving
diagonal cohomology operator, and run arbitrary-inventory controls.

### 8. Marker and analytic ceilings

Contrast digit marker \(u\) with return marker \(z\), prove the
\(\Re s>1\) cohomology barrier for primes, and separate analytic continuation
of a scalar function from continuation of the trace-class family.

### 9. Exact audit protocol

Specify rational polynomial-matrix identities, ordinary/graded regression,
shared/disjoint controls, primitive necklace enumeration, arbitrary
inventories, and double-run integrity.  Report only separately finalized
artifacts.

### 10. Route evaluation

Give the strict tuple, overall rejection, and the smallest Paper26
selector-or-collapse obligation.  Route B remains locked.

### 11. Conclusion

Restate the exact purchase and ceiling of the analytic loophole.

### Appendix A

Supply fixed-point, determinant, finite-complex, direct-sum, marker, and
convergence proof details.

### Appendix B

Give the claim/source/ownership ledger and explicit nonclaims.

## Figure plan

| ID | Type | Description | Source | Priority |
|---|---|---|---|---|
| Figure 1 | pure TikZ hero diagram | scalar denominator, canonical \(0|1\) cancellation, then shared/disjoint cohomology fork | theorem chain | high |
| Figure 2 | pure TikZ ownership diagram | shared versus disjoint cycle ledger crossed with digit versus return marker | Sections 6–8 | high |

### Figure 1 caption draft

A logarithmic code branch carries the ordinary stability factor
\((1-q^r)^{-1}\).  Scalar and ordinary tensor repairs fail, whereas the
canonical zero-/one-form supertrace supplies \(1-q^r\) at every power.  The
successful graded determinant then retracts to cohomology: one shared
constant state retains mixed necklaces, while one constant per disjoint disk
is exactly an atom-loop inventory.

### Figure 2 caption draft

Two independent choices determine the ledger.  Shared recurrence permits
all mixed return necklaces, while disjoint recurrence removes them by
component separation.  Return time assigns one \(z\) per completed code;
digit time retains \(u^{\ell(n)}\).  Neither exterior cancellation nor the
specialization \(u=1\) identifies these dynamical objects.

## Table plan

1. closest literature and bounded novelty;
2. scalar, tensor, graded, shared, and disjoint determinant identities;
3. arbitrary-inventory control ledger;
4. ordinary/graded and digit/return ownership firewall;
5. strict Route-A evaluation;
6. Paper26 admission test.

## Citation plan

- Introduction and local traces: Ruelle 1976; Bandtlow–Jenkinson 2008.
- Literature boundary: Atiyah–Bott 1967; Ruelle 1990;
  Hadfield–Kandel–Schiavina 2020; Elias 1975; Parry–Pollicott 1990.
- Trace-class determinant obstruction: Simon 1977.
- The 2026 Randolph preprint appears only in the literature firewall and is
  labelled non-peer-reviewed.

Only primary or authoritative records are used for theorem-bearing claims.

## Quality locks

- Every occurrence of “Fredholm determinant” identifies ordinary degreewise
  determinants or the graded ratio explicitly.
- The ordinary block sum is never assigned the graded quotient.
- Shared and disjoint assemblies are never switched inside a derivation.
- Digit marker \(u\) and induced-return marker \(z\) are never identified.
- The infinite Bergman proof does not assume that \(d\) is bounded.
- The ordinary tensor theorem is not promoted to a universal nuclear no-go.
- Arbitrary inventories accompany every disjoint prime product.
- No analytic continuation of \(1/\zeta\) is called continuation of the
  trace-class family.
- The strict tuple and verdict are identical in every artifact.
- No target-zero data and no review loop are used.

## Workflow note

The external outline-confirmation and manuscript-review stages are skipped
because the standing project instruction requests autonomous writing without
a review loop.  The source lock, claims–evidence matrix, primary-source audit,
and final compilation checks remain mandatory.
