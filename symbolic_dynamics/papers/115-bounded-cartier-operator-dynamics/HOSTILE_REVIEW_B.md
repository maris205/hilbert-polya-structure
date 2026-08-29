# Hostile Review B — P115

## Independence, scope, and review posture

This is an independent, non-author review of the raw manuscript, its supporting
documents, `code/verify.py`, and the stored verifier output.  I did **not** read
`HOSTILE_REVIEW_A.md`.  I did not modify any existing paper file, perform final
QA, compute release hashes, or use Git.  External release, novelty, and priority
remain **HOLD**.

I reconstructed the map directly from coefficients, treated it as an
`F_p`-linear finite system without assuming `F_q`-linearity, recomputed all
boundary cases, built a separate literal `F_4` model, and attacked the phrases
“complete finite dynamics” and “entire functional graph” against the actual
theorem package.  I also performed a bounded primary-source owner audit of
Cartier/section operators and finite linear functional graphs.

## Provisional verdict

**MAJOR REVISION / HOLD.**  I found no false displayed formula and no
counterexample to the iterate, image, fibre, depth, periodic, lattice, or
recovery theorems.  The mathematical core is correct in its present literal
scope.  Two issues block circulation:

1. “complete functional graph” is stronger than what is explicitly stated.
   The paper gives a complete iterate and temporal census, but it does not give
   the customary component/basin/attached-tree decomposition of the functional
   graph.  Either weaken that language throughout or add the missing graph
   theorem.
2. The owner boundary is materially underdeveloped.  The system is an
   `F_p`-linear map, so classical and modern complete descriptions of linear
   finite dynamical systems are direct owners.  Reis 2023 alone is not an
   adequate historical or theorem-level subtraction, and the Cartier-side
   bibliography should include the broader section-operator literature.

These are scope and ownership defects, not evidence that the formulas are
wrong.

## Independent mathematical reconstruction

### 1. Semilinearity and conventions

Let `q=p^a`, let `sigma(c)=c^p`, and let

```text
C(sum_{j=0}^n c_j x^j)
  = sum_{0<=j<=floor(n/p)} sigma^{-1}(c_{pj}) x^j.
```

The notation `c^{p^{-t}}` is correctly defined as `sigma^{-t}(c)`, not as a
rational power.  Frobenius and its inverse are additive and `F_p`-linear, but
for `a>1` they are generally not `F_q`-linear.  Consequently `C` is an
`F_p`-linear endomorphism of the `a(n+1)`-dimensional `F_p`-space underlying
`F_q^{n+1}`.  The manuscript never uses the false `F_q`-linear shortcut.

The zero polynomial convention `deg 0=-infinity` makes the image/fibre case
split well-defined.  The constant subspace `K=F_q*1` is invariant, and on it
the map is `sigma^{-1}`.

### 2. Iterates

One application selects indices divisible by `p`, divides those indices by
`p`, and applies one inverse Frobenius to their coefficients.  Iteration gives

```text
C^t(f)=sum_{0<=j<=floor(n/p^t)} sigma^{-t}(c_{p^t j}) x^j
```

for every `t>=0`.  At `t=0`, this is the identity.  Once `p^t>n`, only `j=0`
remains and the output is the constant `sigma^{-t}(c_0)`.  Different input
indices never merge into one coefficient, so there is no hidden cancellation
in this formula.

### 3. Images and all iterated fibres

Put `r_t=floor(n/p^t)`.  The selected input coordinates
`c_0,c_{p^t},...,c_{r_t p^t}` are independently arbitrary, and inverse
Frobenius is bijective.  Hence, under zero padding,

```text
im(C^t)=F_q[x]_{<=r_t},                    #image=q^(r_t+1).
```

For a target in this image the selected coordinates are uniquely prescribed
and the other `n-r_t` input coordinates are free.  Thus

```text
#(C^t)^(-1)(g) = q^(n-r_t)  if deg(g)<=r_t,
                  0          otherwise.
```

The boundary checks are correct:

- `t=0`: full image and singleton fibres;
- `p^t>n`: exactly `q` constant targets and fibre size `q^n`;
- `n=0`: the phase space already is `K`, and every iterate is a permutation.

The rank factorization `C^t=J_t Phi_t R_t` is also correct over `F_p`, with
rank `a(r_t+1)` and kernel dimension `a(n-r_t)`.  It repackages the same
selected-coordinate information as linear algebra.

### 4. Pointwise depth and all shells

For an occupied positive index `j=p^v u`, with `p` not dividing `u`, its
coefficient survives at a positive index through time `v` and disappears at
time `v+1`.  Since index chains are disjoint and inverse Frobenius preserves
nonzero coefficients,

```text
tau(f)=0                                                       if f is constant,
tau(f)=1+max{v_p(j): j>0 and c_j!=0}                           otherwise.
```

The event `tau(f)<=t` requires precisely the positive coordinates at indices
divisible by `p^t` to vanish.  There are `r_t` such coordinates, giving

```text
# {f:tau(f)<=t}=q^(n+1-r_t),       P(tau<=t)=q^(-r_t).
```

CDF differencing yields the shell formula.  For `n>0`, the largest valuation
among `1,...,n` is `floor(log_p n)`, so the sharp maximum is

```text
D=1+floor(log_p n).
```

It is attained, for example, by `x^(p^(D-1))`.  With
`s=floor(n/p^(D-1))`, the deepest states are exactly those for which at least
one of the `s` top-chain coefficients is nonzero, and their count is
`q^(n+1)-q^(n+1-s)`.  The separate `n=0` statement is necessary and correct.

### 5. Stable core, fixed points, cycles, and zeta

The nested images eventually equal `K`, so the stable image is `K`.  Any
periodic point belongs to every sufficiently deep image and therefore lies in
`K`; conversely, inverse Frobenius permutes `K`.  Thus

```text
Core(C)=Per(C)=K,                  C|_K=sigma^(-1).
```

A point fixed by `C^m` is a constant fixed by `sigma^m`, namely an element of
`F_{p^gcd(a,m)}`.  Therefore

```text
#Fix(C^m)=p^gcd(a,m).
```

For `d|a`, Möbius inversion gives the exact-period point count

```text
A_d=sum_{e|d} mu(d/e) p^e,
```

so there are `A_d/d` cycles of length `d` and no other periods.  The Euler
product

```text
zeta_C(z)=product_{d|a}(1-z^d)^(-A_d/d)
```

then follows.  At `a=1`, all `p=q` constants are fixed and this reduces to
`(1-z)^(-p)`.  At `n=0`, the same cycle census describes the whole phase
space.  Transients correctly contribute no zeta factor.

### 6. Exact lattice layers

For `1<=alpha<p` and `n_L=floor(alpha p^L)`, one has

```text
p^L <= n_L < p^(L+1),
```

so the maximum depth is exactly `L+1`.  If
`Delta_L=L+1-tau(F_L)`, then for fixed `k>=1` and `L>=k-1`,

```text
P(Delta_L>=k)
 = q^(-floor(n_L/p^(L+1-k)))
 = q^(-floor(alpha p^(k-1))).
```

The nested-floor identity is valid for arbitrary real `alpha`, not just the
rational values used by the verifier.  These tails decrease to zero, and their
successive differences define a probability law.  The endpoint `alpha=1` is
valid; `alpha=p` belongs to the next lattice interval and is correctly
excluded.

### 7. Recovery

For the signature `N=|X|` and `F_m=#Fix(C^m)`, the formulas imply

```text
p=F_1,
q=max_m F_m,
a=min{m>=1:F_m=q},
n=log_q(N)-1.
```

Indeed `F_m=q` exactly when `a|m`.  This remains valid at `a=1` and `n=0`.
The claim uses the entire infinite fixed sequence; it should not be silently
restated as recovery from an unspecified short prefix.

## The “complete functional graph” claim

The explicit iterate formula is a complete orbit calculator, and the paper
does determine images, fibres, preperiods, cycles, and fixed counts.  That is
substantial.  However, the abstract says “complete finite dynamics,” the
introduction asks for the “entire functional graph,” and the README advertises
a “complete bounded functional-graph package.”  In functional-graph papers,
that wording normally includes a component decomposition and a description of
the rooted trees attached to periodic vertices.  Neither is stated as a
theorem here.

The missing information is readily accessible but is not identical to the
current global shell census.  For example, independent reconstruction gives:

- a constant belongs to a Frobenius cycle of some `d|a`;
- the weak component containing that cycle has exactly `d q^n` states;
- for each specified periodic constant `y`, the number of states whose first
  entry into `K` occurs at time `t` at `y` is

  ```text
  1                                                    for t=0,
  q^(n-r_t)-q^(n-r_(t-1))                              for 1<=t<=D;
  ```

- one-step indegrees are zero outside `im(C)` and equal
  `q^(n-floor(n/p))` inside it.

These observations begin, but do not by themselves replace, a rooted-tree
isomorphism statement.  The author has two acceptable repairs:

1. **scope-down repair:** replace “entire/complete functional graph” by
   “exact iterate and temporal census” in the abstract, introduction, README,
   plan, and narrative report; or
2. **graph-completion repair:** add and prove a component/basin/tree theorem,
   with component sizes, root-level counts, indegree types, and an explicit
   statement of whether all trees attached to cycle vertices are isomorphic.

Without one of those repairs, the contribution language outruns the displayed
results even though the formulas themselves are correct.

## Counterexample campaign

I tested or reconstructed the following failure modes:

- false `F_q`-linearity in extension fields;
- a root-exponent ambiguity in `p^{-t}`;
- coefficient collision or cancellation along iterates;
- a target outside the padded image with a nonempty fibre;
- nonuniform nonempty fibres at `t=0` and after total truncation;
- a constant incorrectly assigned positive depth;
- same-degree polynomials incorrectly forced to have the same depth;
- a nonconstant periodic point;
- an extension field whose core has only fixed points;
- a Möbius count at a nondivisor of `a`;
- a lattice off-by-one at `alpha=1`, `L=0`, or `k=L+1`;
- failure of parameter recovery at `a=1` or `n=0`;
- a component size inconsistent with the core cycle length.

No formula-level counterexample survived.  A separate literal `F_4` model at
`n=3`, using the actual inverse-Frobenius permutation
`(0,1,w,1+w) -> (0,1,1+w,w)`, produced

```text
depths {0:4, 1:60, 2:192},
fixed counts 2,4,2,4,2,4,
components (cycle points, states) = (1,64), (1,64), (2,128).
```

It also reproduced every iterated image/fibre through post-truncation times.
A non-verifier rational lattice value `alpha=137/100` passed the exact nested
floor identity through eight levels.

## Fresh verifier, byte comparison, build, fonts, and visual audit

All commands were run in a newly created `/tmp` directory.  No build product
was copied into the paper directory.

| Check | Fresh result |
|---|---:|
| verifier | PASS |
| exact assertions | 1,917,054 |
| fresh stdout vs stored stdout | byte-identical |
| field lanes | `F_2,F_3,F_4,F_8,F_9,F_16`, plus every `n=0` boundary |
| rational lattice lanes | 33 through `L=9` |
| fresh PDF pages | 5 |
| fresh PDF bytes | 379,547 |
| LaTeX/BibTeX warnings, overfull/underfull boxes, undefined references | 0 |
| fonts | 27/27 embedded, 27/27 subset, 27/27 Unicode-mapped |

I rendered and visually inspected all five pages.  There are no clipped
displays, blank pages, missing glyphs, collisions, broken table rules, or
obvious hyperlink defects.  Page breaks across the periodic proof and lattice
proof are readable.

## Bounded owner audit

This audit records located owners and search risk.  Failure to locate an exact
bounded Cartier functional-graph paper is **not** novelty evidence.

### Cartier and section-operator side

1. Bridy's
   [*Automatic Sequences and Curves over Finite Fields*](https://arxiv.org/abs/1604.08241)
   (journal DOI
   [10.2140/ant.2017.11.685](https://doi.org/10.2140/ant.2017.11.685))
   explicitly uses the rooted coefficient-section convention and compositions
   of the `Lambda_i`.  P115 cites it, but the owner paragraph should say more
   plainly that the `t`-fold coefficient-decimation formula is an immediate
   zero-digit specialization of established composition machinery.
2. Sangtae Jeong,
   [*Cartier operators on fields of positive characteristic p*](https://arxiv.org/abs/1509.01650),
   studies two Cartier-operator families on `F_q[[T]]` and their finite-field
   coefficient-extraction structure.  It is a closer operator-family owner
   than the 1957 historical citation alone and should be audited explicitly.
3. Cartier 1957 owns the geometric origin, but it is not a substitute for the
   later power-series/section-operator literature.

### Finite linear functional-graph side

The map in P115 is literally a finite `F_p`-linear dynamical system.  The
following are direct, not merely adjacent, owner lines:

1. Elspas, *The Theory of Autonomous Linear Sequential Networks*, IRE
   Transactions on Circuit Theory 6 (1959), 45--60, DOI
   [10.1109/TCT.1959.1086506](https://doi.org/10.1109/TCT.1959.1086506),
   is foundational state-diagram/linear-network work.
2. Wang, *Transition graphs of affine transformation on vector spaces over
   finite fields*, Journal of the Franklin Institute 283 (1967), 55--72, DOI
   [10.1016/0016-0032(67)90115-9](https://doi.org/10.1016/0016-0032(67)90115-9),
   explicitly analyzes transition-graph structure over finite fields.
3. Hernández Toledo, *Linear Finite Dynamical Systems*, Communications in
   Algebra 33 (2005), 2977--2989, DOI
   [10.1081/AGB-200066211](https://doi.org/10.1081/AGB-200066211),
   advertises a complete description through nilpotent and bijective
   components.  This is the most important missing generic owner for P115's
   transient/core split.
4. Panario--Reis,
   [*The functional graph of linear maps over finite fields and applications*](https://doi.org/10.1007/s10623-018-0547-5),
   Designs, Codes and Cryptography 87 (2019), 437--453, directly treats linear
   functional graphs, cycles, and preperiod data.
5. Reis 2023, already cited, counts isomorphism types and relies on earlier
   structural results.  It does not by itself discharge the historical or
   specialized owner audit.

Because the operator is `F_p`-linear, describing rank, nilpotent extinction,
the bijective Frobenius core, cycles, and functional-graph decomposition as a
new general mechanism would collide with this literature.  Only the explicit
specialization and its exact bounded formulas can remain in the residual
scope, subject to a direct-owner search.

### Residual scope after subtraction

The bounded search did not locate the exact conjunction of:

- Bridy's root-twisted zero-digit section restricted to one polynomial degree
  bound;
- closed iterated-image/fibre and entry-shell formulas in `p`-adic index
  coordinates;
- the particular reverse-depth lattice limit; and
- recovery of `(p,a,n)` from phase size plus the fixed sequence.

That is a search outcome, not a novelty claim.  The proof density is also low
after subtraction: most finite formulas are short consequences of coefficient
selection plus generic finite-linear decomposition.  The lattice and recovery
corollaries are the clearest residual differentiators, but they too require a
specialist audit before circulation.

### Internal collision firewall

The named internal distinctions survive inspection:

- P100 erases one least-valuation base-`p` digit on a residue ring; P115
  decimates a coefficient vector and retains a Frobenius permutation core.
- P103 evolves matrices by a double adjugate.
- P107 evolves ideals by annihilator and power.
- P109 evolves subspaces under the image of a regular nilpotent map; it is the
  closest internal proof-engine collision, but its phase points, fibre geometry,
  and unique absorbing core differ from P115.

There is no internal model collision.  There is, however, a recurring internal
motif—exact iterates, depth layers, core cycles, zeta, and parameter recovery—so
P115 must earn its place through the Cartier-specific coefficient formulas and
not generic packaging vocabulary.

## Findings by severity

### CRITICAL

**None found.**  I found no false theorem, invalid field model, unhandled
`n=0`/`a=1` case, zeta corruption, or verifier mismatch.

### MAJOR (mathematics / claim scope)

**M-M1 — “complete functional graph” is not explicitly delivered.**  The
iterate formula completely determines orbits, but the manuscript does not
state the component, basin, or attached-tree structure conventionally meant
by a complete functional-graph theorem.

Actionable repair: choose one of the two repairs in the dedicated section
above.  A simple vocabulary edit is acceptable if the intended contribution is
an exact temporal census.  If the stronger phrase is retained, add a theorem
with component sizes, entry strata per periodic vertex, indegree types, and
tree-isomorphism information, plus independent exact assertions for it.

**M-M2 — do not overstate independence of proof route II.**  The rank route is
a genuinely different counting language, but its displayed factorization is
read directly from the coefficient iterate.  It is an independent count after
the coordinate formula is known, not a logically independent derivation of the
iterate.

Actionable repair: use “second count” or “linear-algebraic reconstruction” in
the abstract/supporting documents; reserve “independent proof” for exactly the
fibre size/CDF conclusions that are recomputed by rank-nullity.

### MAJOR (owner scope)

**M-O1 — direct finite-linear owners are missing.**  Citing Reis 2023 while
omitting Elspas, Wang, Hernández Toledo, and Panario--Reis leaves the central
nilpotent/bijective functional-graph owner line unsubtracted.

Actionable repair:

1. add the four direct sources and state exactly what they own;
2. express P115 as a specialization of generic `F_p`-linear dynamics, not an
   alternative general theory;
3. compare the ranks/kernel sequence and core permutation with the canonical
   decomposition used in those sources;
4. identify only formulas not already automatic from generic theory as
   residual.

**M-O2 — the Cartier-side audit is too short.**  Bridy is appropriate, but
Cartier 1957 plus one Bridy equation does not cover later section-operator
families, compositions, and finite-field power-series work.

Actionable repair: audit Jeong 2015 and the section-operator/automatic-sequence
line cited inside Bridy; document searches for “Cartier iterate,” “section
operator dynamics,” “zero digit/residue section,” bounded polynomials, ranks,
and functional graphs.  Search absence must remain explicitly non-probative.

**M-O3 — contribution density must be recalibrated after subtraction.**  The
coefficient iterate is immediate from established section composition; the
stable-core split is generic finite-linear machinery; fixed subfields, Möbius
inversion, and zeta conversion are standard.  The manuscript already gestures
toward this subtraction but still packages their conjunction as if the package
itself supplied substantial novelty.

Actionable repair: make the lattice stabilization and signature recovery the
lead residual results, state their dependence on the elementary bounded
specialization, and avoid novelty adjectives pending specialist confirmation.

### MINOR

**m1 — “zero-residue” is terminologically ambiguous.**  In Cartier geometry,
“residue” also refers to the residue of a differential.  Here it means the
index residue class `0 mod p`.

Actionable repair: say “residue-class-zero Cartier section” on first use, or
define “zero-residue” explicitly in the abstract.

**m2 — define `Per(C)` when it first appears.**  The notation is standard but
the manuscript defines the stable image and entry time, not the union/set of
periodic points.

**m3 — qualify the recovery data.**  State consistently that `(F_m)_{m>=1}` is
the full fixed sequence.  The theorem does not claim a universally specified
finite observation window, even though `a` observations suffice once its value
is reached.

**m4 — add graph-level verifier assertions if graph language remains.**  The
current verifier exhausts orbits, fibres, depths, cycles, and zeta, but it does
not print/check weak-component sizes or rooted-tree profiles.  Those controls
should accompany any new graph-completion theorem.

**m5 — preserve the edge cases in every shortened statement.**  In particular:
`n=0` has depth zero; `a=1` has fixed constant core; targets outside the image
have empty fibres; and `alpha=p` is excluded from the selected lattice window.

## Required repair checklist

- [ ] Scope down “complete/entire functional graph” or add the missing graph
      decomposition theorem and controls.
- [ ] Calibrate the “independent proof route” language.
- [ ] Add Elspas 1959, Wang 1967, Hernández Toledo 2005, and Panario--Reis
      2019 to the owner analysis.
- [ ] Audit Jeong 2015 and the broader section-operator lineage.
- [ ] Reframe generic finite-linear and Cartier-composition consequences as
      owned machinery.
- [ ] Lead residual scope with the exact lattice and recovery corollaries.
- [ ] Define “zero-residue” and `Per(C)` explicitly.
- [ ] Preserve all `t=0`, `n=0`, `a=1`, empty-fibre, and lattice-endpoint
      conventions.
- [ ] After repairs, re-run the exact verifier/output comparison, fresh build,
      font check, and all-page visual audit.
- [ ] Keep external release, novelty, and priority on HOLD pending an
      independent direct-owner review.

## Final recommendation

The displayed mathematics is correct and impressively well controlled, but
the present package should not circulate as a complete functional-graph result.
I recommend **MAJOR REVISION**, with one claim-scope repair and a substantially
deeper owner subtraction.  No release, novelty, or priority decision follows
from this review.
