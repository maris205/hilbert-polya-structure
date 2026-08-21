# Source lock and exact-quantifier ledger

## Search status

**As-of date:** 2026-08-20  
**Result:** `NO_EXACT_COLLISION_FOUND_IN_BOUNDED_SEARCH`  
**Consequence:** continue only to independent Stage-2 audit; do not convert
this result into an absolute novelty or priority claim.

The collision target was not merely “a theorem about Toeplitz factors.”  It
was the conjunction of these quantifiers:

```text
for every integer p>=3;
for every pair of exact-support, periodic, cyclic-neighbor-distinct
directives u,v in the explicit affine p-divisibility family;
for every continuous same-base factor map sending x_{p,u} to x_{p,v};
the map is the unique surjective coordinate letter quotient;
and all quotient targets are classified by the independent-set partitions
of the cyclic directive-adjacency graph.
```

The constructiveness subclaim was separately searched with its exact split:
essential `p^N` skeletons for all integer `p>=3`, but Hosseini--Yassawi
constructiveness exactly for prime `p`.

## Fresh query ledger

The following searches were run or rerun for this Stage-2 bridge.  Search
results were followed to primary publisher, journal, or arXiv full text
before a scope judgment was recorded.

- `simple Toeplitz subshift factor map letter quotient pointed`
- `Toeplitz flow homomorphism over zero t-symbol factor`
- `Toeplitz same period factor sliding block radius zero`
- `"pointed factor" "simple Toeplitz"`
- `"admissible partitions" "Toeplitz" factors`
- `"nu_p((p-1)k+1)" Toeplitz`
- `"(p-1)k+1" Toeplitz valuation`
- exact-title and cited-by followups centered on DKL (1995),
  Hosseini--Yassawi, Sell, Sell--Sieron, Downarowicz--Durand,
  Durand--Leroy, Bustos-Gajardo--Kellendonk--Yassawi, Espinoza,
  Gao--Li--Peng--Sun, and Salo.

The affine-formula queries returned no relevant symbolic-dynamics owner.
This is negative evidence from a bounded search, not proof that no owner
exists.

## Nearest primary owners

### 1. Downarowicz--Kwiatkowski--Lacroix is the closest general owner

T. Downarowicz, J. Kwiatkowski, Y. Lacroix, “A criterion for Toeplitz flows
to be topologically isomorphic and applications,” *Colloquium
Mathematicum* 68 (1995), 219--228, DOI
[`10.4064/cm-68-2-219-228`](https://www.impan.pl/get/doi/10.4064/cm-68-2-219-228),
[primary PDF](https://matwbn.icm.edu.pl/ksiazki/cm/cm68/cm6828.pdf).

Theorem 1, on PDF page 4, assumes two Toeplitz sequences with the same
period structure and classifies homomorphisms **over zero**.  Such a
homomorphism exists iff, at some level `t`, a function
`Pi:W_t(omega)->W_t(eta)` sends every aligned source `t`-symbol to the
corresponding target `t`-symbol; the function is bijective in the
isomorphism case.  The theorem therefore owns the general same-period,
over-zero, aligned-symbol criterion.

It does not state that, in the present affine one-hole family, an arbitrary
aligned-symbol map is induced by one source-letter quotient, nor does it
state the explicit admissible-partition refinement poset.  The Stage-2
rigidity theorem is a specialization and collapse of this nearest owner,
not a replacement for it.

### 2. Hosseini--Yassawi owns the constructive-period obstruction

M. Hosseini, R. Yassawi, “Obstacles to topological factoring of Toeplitz
shifts,” *Discrete and Continuous Dynamical Systems* 46 (2026), 413--432,
DOI [`10.3934/dcds.2025105`](https://www.aimsciences.org/article/doi/10.3934/dcds.2025105),
[arXiv:2412.04422v3](https://arxiv.org/abs/2412.04422).

Section 2.2.1 defines the essential period of a finite word as the least
common multiple of the essential periods of its positions.  Lemma 2.1 and
the following definition call a period structure constructive when the
initial block of length `p_N` has essential period `p_{N+1}`.  Theorem 1.1
assumes pointed factor maps between Toeplitz shifts having constructive
pure-power structures `(p^n)` and `(q^n)`; it proves `q` divides `p`, and
for pointed conjugacy proves `p=q`.

That theorem owns both the constructiveness terminology and the cross-base
necessary obstruction.  It neither asserts that every integer-base affine
example here is constructive (the composite examples are not) nor
classifies all same-base pointed maps as letter quotients.  The present
package therefore uses its definition exactly, proves the prime/composite
split, and leaves all cross-base sufficiency out of scope.

An independent retrieval cross-check, not an input to the proof, recorded
SHA-256

```text
arXiv source archive: 11c352bb3e340e575fe0d82d31f923315cef4d3238229691b60ee3533777b3f8
main TeX file:         4c50b0ffc7f47abffd4a36b7b75cad11bf3b2ba6a4094f48037d03c39532c71b
```

### 3. Simple-Toeplitz combinatorics

D. Sell, [“Combinatorics of One-Dimensional Simple Toeplitz
Subshifts,” arXiv:1801.08778](https://arxiv.org/abs/1801.08778), and
[“Simple Toeplitz subshifts: combinatorial properties and uniformity of
cocycles,” arXiv:2006.15348](https://arxiv.org/abs/2006.15348).

These works give systematic simple-Toeplitz language, complexity,
repetitivity, palindrome, and de Bruijn-graph results.  Their primary
abstracts and full-text routing do not state the frozen same-base pointed
factor classification or its quotient poset.

### 4. Updated finite-boundary/separated-hole neighbor

D. Sell, F. Sieron, [“Almost automorphic subshifts with finiteness
conditions for the boundary of the separating cover,”
arXiv:2409.06005v2](https://arxiv.org/abs/2409.06005), DOI
[`10.1080/14689367.2026.2679154`](https://doi.org/10.1080/14689367.2026.2679154).

The paper treats factors through general sliding block codes and, among
other results, gives necessary conditions for finite-boundary factors under
separated-hole hypotheses.  Its Theorem 5.4 concerns isolated value pairs
passing from a factor back to a separated-hole source.  The full text
explicitly retains a local rule on `[-J,J]`; it does not collapse all maps in
the affine family to radius zero or enumerate their kernels.

### 5. General factor and nearby classification frameworks

- T. Downarowicz, F. Durand, [“Factors of Toeplitz flows and other almost
  1-1 extensions over group rotations,” *Math. Scand.* 90 (2002),
  57--72](https://www.mscand.dk/article/view/14361): general almost
  one-to-one factor structure, not the affine letter-quotient theorem.
- F. Durand, J. Leroy, [“Decidability of the isomorphism and the
  factorization between minimal substitution subshifts,”
  arXiv:1806.04891v3](https://arxiv.org/abs/1806.04891): a computable radius
  bound and factor decision procedure for minimal substitution subshifts,
  not universal radius-zero rigidity for this family.
- A. Bustos-Gajardo, J. Kellendonk, R. Yassawi, [“Almost automorphic and
  bijective factors of substitution shifts,”
  arXiv:2307.01787](https://arxiv.org/abs/2307.01787): finite-semigroup
  criteria for constant-length substitution factors, not this simple
  Toeplitz quotient poset.
- B. Espinoza, [“Symbolic factors of S-adic subshifts of finite alphabet
  rank,” arXiv:2008.13689](https://arxiv.org/abs/2008.13689), DOI
  [`10.1017/etds.2022.21`](https://doi.org/10.1017/etds.2022.21): finite-rank
  factor/fiber and finiteness results, not the exact same-base formula.
- S. Gao, R. Li, B. Peng, Y. Sun, [“Toeplitz subshifts of finite rank,”
  arXiv:2504.05582](https://arxiv.org/abs/2504.05582): topological-rank,
  descriptive classification, bi-factor, inverse, and automorphism results,
  not the pointed letter-quotient classification.
- V. Salo, [“Toeplitz subshift whose automorphism group is not finitely
  generated,” arXiv:1411.3299](https://arxiv.org/abs/1411.3299): an important
  warning that unpointed Toeplitz automorphism behavior can be large.  It
  reinforces the need for the pointed restriction but is not an exact
  collision.

## Exact residual and stop rule

The bounded search leaves the following residual only:

1. explicit all-integer-base skeleton rigidity with constructiveness iff
   prime;
2. collapse of every same-base **pointed** sliding block factor in the
   affine p-divisibility family to a unique coordinate letter quotient
   (equivalently, the closest-owner aligned `t`-symbol description collapses
   to the radius-zero letter level in this family);
3. admissible kernels and the refinement-poset/graph-count corollaries.

If an independent search finds a primary source proving this same
conjunction with the same object and map quantifiers, status changes to
`EXACT_COLLISION` and the bridge stops.  Until that audit, the only permitted
source verdict is

```text
NO_EXACT_COLLISION_FOUND_IN_BOUNDED_SEARCH
```
