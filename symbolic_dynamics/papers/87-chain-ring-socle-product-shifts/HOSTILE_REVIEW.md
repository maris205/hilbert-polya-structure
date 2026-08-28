# Hostile Review — P87

Audit date: 2026-08-28 UTC.

Disposition: **PROVABLE AFTER TWO AUDIT CORRECTIONS; GO for internal freeze;
external HOLD**.

## Independent two-round audit record

### Round 1 — theorem and control attack

The valuation law, block spectrum, MME simplex, all-period ledger, recovery
map, and layerwise conjugacy were rederived from the definitions.  The exact
control was rerun independently and again passed all 700,499 assertions.  One
edge-case overstatement failed: when `a=1`, the involution `i -> a-i` has only
one orbit, so the full shift is irreducible of period two, not reducible.  The
manuscript now says reducible exactly for `a>=2`; every displayed theorem and
formula was already valid at `a=1`.

### Round 2 — owner, wording, build, and visual attack

A reverse literature search found the closer 2026 owner omitted from the
first draft: Dolžan's fixed-product matrix is `A_u=(1_(xy=u))`.  P87's
matrix, after removing the isolated zero state, is exactly the sum of `A_u`
over `u in Soc(R)\{0}`.  Dolžan is now positively cited, and the residual
claim is narrowed to the nonzero-socle union and its symbolic consequences.
The manuscript was rebuilt from TeX/BibTeX, its text was extracted, all five
pages were inspected, and all fonts and warning counters were checked.

## Claim

For every finite commutative chain ring `R` with maximal ideal `(pi)`,
residue-field size `q`, and length `a+1 >= 2`, the SFT defined by

```text
xy in Soc(R) \ {0}
```

has the valuation decomposition, rank, equal-entropy SCCs, parity-dependent
mixing/MME structure, fixed-point and zeta formulas, four-period recovery,
and ring-structure collapse stated in `main.tex`.

## Status

**PROVABLE IN THE CORRECTED MANUSCRIPT.**  The theorem package survives.  The
two new changes are an `a=1` transitivity correction outside the theorem
statements and explicit subtraction of the closer fixed-product-matrix owner.

## Assumptions

- `R` is finite, commutative, unital, and its ideals form a chain.
- Its maximal ideal is `(pi)` and satisfies
  `(pi)^(a+1)=0 != (pi)^a` with `a>=1`.
- `q=|R/(pi)|`, hence `q` is a prime power and `q>=2`.
- `Soc(R)=Ann_R((pi))`.
- The adjacency convention retains a loop whenever `x^2` is a nonzero
  socle element.
- Fixed points and zeta are those of the two-sided edge shift.

## Notation

- `V_i=(pi)^i \ (pi)^(i+1)` is the valuation-`i` layer.
- `w_i=|V_i|=(q-1)q^(a-i)`.
- `rho=(q-1)q^(a/2)` and `rho^2=(q-1)^2q^a`.
- `F_n=#Fix(sigma^n)`.
- `A_R` is the zero-one adjacency matrix on `R\{0}`.

## Proof Strategy

Reduce the ring multiplication rule to an equality of valuations.  The
resulting graph is a direct sum of complete bipartite blocks and possibly one
all-ones block.  All dynamical statements then follow from this direct-sum
normal form.  The recovery theorem is an exact inversion of the first four
trace formulas, and the collapse theorem is a layerwise graph isomorphism.

## Dependency Map

1. The entire package depends on the layer formula and product-valuation law.
2. Rank, spectrum, entropy, SCC period, fixed counts, and zeta depend only on
   the block decomposition.
3. MME counting uses equal block radii plus Parry uniqueness for each
   irreducible SFT.
4. Four-period recovery uses the parity split in the trace formulas and the
   strict monotonicity of `(q-1)^2 q^a` in `q`.
5. Ring collapse uses only equality of corresponding layer sizes and the
   fact that adjacency is determined by valuations.

## Proof

### Step 1 — valuation layers and the socle

Multiplication by `pi^i` maps `R/(pi)` bijectively onto
`(pi)^i/(pi)^(i+1)`: a unit cannot map into `(pi)^(i+1)`, while every
nonunit lies in `(pi)`.  Each quotient therefore has `q` elements.  It
follows that

```text
|(pi)^i| = q^(a+1-i),
|V_i| = q^(a+1-i)-q^(a-i) = (q-1)q^(a-i).
```

Every nonzero element of `V_i` is `pi^i` times a unit.  Thus the product of
elements in `V_i,V_j` has valuation `i+j` when `i+j<=a`, and is zero when
`i+j>=a+1`.  Also `(pi)^a` is annihilated by `(pi)`, while an element of
`V_i`, `i<a`, is not annihilated by `pi`.  Hence

```text
Soc(R)=(pi)^a,
xy in Soc(R)\{0} iff v(x)+v(y)=a.
```

This is the only ring-theoretic input used later.

### Step 2 — graph normal form

The last equivalence joins every vertex of `V_i` to every vertex of
`V_(a-i)` and to no other layer.  When `i<a-i` this gives the symmetric
complete-bipartite block

```text
[[0, J_(w_i,w_(a-i))],
 [J_(w_(a-i),w_i), 0]].
```

When `a=2b`, the central layer `V_b` gives `J_(w_b,w_b)`, including its
diagonal.  The blocks are disjoint and exhaust every valuation layer.

### Step 3 — rank, spectrum, and entropy

A complete-bipartite block has rank two and nonzero eigenvalues
`+/-sqrt(w_i w_(a-i))`.  Since

```text
w_i w_(a-i)=(q-1)^2q^a=rho^2,
```

every such block has eigenvalues `+/-rho`.  The central all-ones block, when
present, has rank one and sole nonzero eigenvalue
`w_(a/2)=(q-1)q^(a/2)=rho`.  Counting two ranks per pair and one central rank
for even `a` gives exactly `a+1`.  The displayed characteristic polynomials
follow with zero multiplicity `q^(a+1)-1-(a+1)`.  Every irreducible block has
spectral radius `rho`; therefore the finite union has entropy `log rho`.

### Step 4 — SCCs and maximal measures

Each two-layer block is irreducible and bipartite, so its exact period is
two.  The central all-ones block exists exactly for even `a` and is primitive
because it has loops.  The number of valuation orbits under `i -> a-i` is
`floor(a/2)+1`.

All components have the same maximal entropy.  Parry uniqueness supplies one
ergodic MME per irreducible component.  Any invariant measure decomposes over
the finitely many disjoint invariant clopen components, and its entropy is
the weighted sum of the component entropies.  Consequently the complete MME
set is the convex hull of the component Parry measures.  A period-two
component cannot be mixing because the two layer indicators alternate.  The
central Parry measure is the uniform Bernoulli measure and is mixing.  This
proves the exact parity statement.  For `a>=2` the full shift is reducible.
For `a=1` it is one irreducible period-two component, hence transitive but not
mixing.

### Step 5 — all periods and zeta

Taking powers of the nonzero spectrum gives, for `a=2b`,

```text
F_n=rho^n((b+1)+b(-1)^n),
```

and for `a=2b+1`,

```text
F_n=(b+1)(1+(-1)^n)rho^n.
```

This yields the stated odd/even cases.  Factoring `det(I-zA_R)` over the
same spectrum gives

```text
(1-rho z)(1-rho^2 z^2)^b          if a=2b,
(1-rho^2 z^2)^(b+1)               if a=2b+1.
```

Its reciprocal is the Bowen--Lanford zeta.  Möbius inversion then gives
every least-period point and orbit count.

### Step 6 — four-period recovery and ring collapse

For even `a`, `F_1=rho>0` and `F_2=(a+1)rho^2`, so
`a=F_2/F_1^2-1` and `rho^2=F_1^2`.  For odd `a`, `F_1=F_3=0`, while
`F_2=(a+1)rho^2` and `F_4=(a+1)rho^4`; hence
`a=F_2^2/F_4-1` and `rho^2=F_4/F_2`.  Once `a` is known, the positive
integer function `(q-1)^2q^a` is strictly increasing for `q>=2`, so it
recovers `q` uniquely.

If two rings have the same `(q,a)`, their corresponding layers have the same
sizes.  Any family of layerwise bijections preserves the equality
`v(x)+v(y)=a`, so it is an adjacency isomorphism and extends coordinatewise
to a one-block conjugacy.  Conversely, conjugacy preserves the first four
fixed counts and therefore the recovered parameter pair.  This proves both
directions of the classification theorem.  The rings `Z/p^(a+1)Z` and
`F_p[t]/(t^(a+1))` witness genuine collapse because their characteristics
are different for `a>=1`.

Therefore the full theorem package follows.  ∎

## Corrections or Missing Assumptions

- The manuscript now defines `Soc(R)=Ann_R(m)` before its first proof.
- The parity language is explicitly about mixing maximal components and
  ergodic MMEs.  The full SFT is reducible for `a>=2`; at `a=1` it is
  irreducible of period two.
- Loops are retained by definition.  Removing them would destroy the even
  central full-shift statement and is not an equivalent convention.
- The excluded field case `a=0` is not needed for the frozen contract or
  controls.  Its inclusion would require only a separate trivial full-shift
  sentence, but is deliberately outside scope.
- Dolžan's fixed-product matrices are prior art.  The identity
  `A_R=sum_(u in Soc(R)\{0}) A_u`, after removing zero, is now stated rather
  than hidden behind the more distant zero-divisor-graph comparison.

## Open Risks

- **No surviving mathematical blocker.**  The proof depends only on the
  standard finite-chain-ring filtration and standard SFT facts cited in the
  manuscript.
- **Ownership risk remains medium.**  The relation is adjacent both to the
  extensive zero-divisor graph literature and to Dolžan's directly relevant
  fixed-product matrices.  All three owner lines are positively subtracted,
  but a specialist priority search is still required before any external
  claim.
- **Release status:** internal freeze is supported; public posting,
  submission, author contact, and absolute novelty language remain `HOLD`.

## Reproducibility and release checks

- Exact control: **PASS — 700,499 integer/rational/polynomial assertions**.
- Abstract coverage: all `q=2,3,4,5`, `a=1,...,5`.
- Concrete coverage: `Z/p^r Z` and `F_p[t]/(t^r)` for `p=2,3,5`,
  `r=2,...,6`; plus `F_4[t]/(t^r)`.
- Four-stage TeX/BibTeX build: all exits zero.
- Final PDF: **5 A4 pages, 313,957 bytes, PDF 1.5**.
- Undefined references/citations: **0/0**.
- LaTeX/package warnings and overfull/underfull boxes: **0**.
- Fonts: **24/24 embedded, subsetted, and Unicode-mapped**.
- All five rendered pages inspected; no clipping, overlap, or stray text.
- PDF SHA-256:
  `c642f7ac4f95d5181b01b852a4550e2c88cbc9193fd38497a97fa05c82aebfd0`.
