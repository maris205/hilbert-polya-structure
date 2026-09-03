# Hostile Review B — P174

**Manuscript:** *Minimum-Pivot Möbius Feedback on Projective-Line Subsets*  
**Role:** independent hostile reviewer B; not a P174 author and not Review A  
**Proof status:** `PROVABLE AS STATED`  
**Verdict:** `PASS WITH ONE MINOR SOURCE REPAIR`  
**Counts:** Critical **0** · Major **0** · Minor **1**  
**Lifecycle:** `PROVISIONAL_AMBER / HOLD_EXTERNAL` (unchanged)  
**Edit boundary:** no manuscript, bibliography, author verifier, or PDF was
modified during this review.

## 1. Decision

Every theorem in the live manuscript survives an independent derivation.
The two-stage image tower is exact in both directions; the three depth layers
are pointwise, not merely aggregate; the core is precisely inversion; the
fixed and two-cycle counts include the binary boundary; and the inverse
calculation really gives every target, every valid pivot, the entire fibre
histogram, and the unique maximum.

The internal AQN kill switch remains live but is not triggered by the material
inspected.  AQN removes all value from “choose a state-dependent section and
then expose a classical group action.”  It does not supply P174's two forced-
point image conditions or its target-dependent modular initial interval.
Conversely, those residual facts are short and depend on an artificial order,
so they justify only the existing amber internal note—not green status.

One omitted primary neighbor should be added to the artificial-order owner
subtraction.  This is a source-boundary repair, not a theorem repair.  A
bounded non-hit after the repair remains non-evidence for novelty, priority,
ownership, freedom to operate, or release.

The external second-model endpoint prescribed by the review workflow was not
available in this environment; no such corroboration is claimed.  Review-B
independence consists of a fresh all-parameter proof audit and a separately
implemented executable that imports no project code.

## 2. Finding

### P174-RB-MIN-01 — ordered canonical-image machinery is absent from the
owner subtraction

**Severity:** Minor while `HOLD_EXTERNAL` remains in force.  It is a mandatory
source-gate repair before any future release decision.

The live source log searches “minimum pivot,” state-dependent Möbius maps,
and projective subset normalization, but it does not record the established
*minimal image*, *canonical image*, *canonizing element*, or *dynamic
ordering* vocabulary for ordered subset actions.  The following primary
neighbor was verified:

- Christopher Jefferson, Eliza Jonauskyte, Markus Pfeiffer, and Rebecca
  Waldecker, “Minimal and Canonical Images,” *Journal of Algebra* **521**
  (2019), 481–506, DOI
  [10.1016/j.jalgebra.2018.11.009](https://doi.org/10.1016/j.jalgebra.2018.11.009),
  primary preprint [arXiv:1703.00197v2](https://arxiv.org/abs/1703.00197v2).

That paper formalizes canonical images of subsets under permutation-group
actions, canonizing elements, total orders on the ground set and induced
orders on subsets, and static/dynamic orderings used to find orbit
representatives.  Those concepts are directly relevant pressure on any value
claim based merely on choosing a group element from an artificially ordered
subset.

It is **not** a literal owner of P174.  A canonical image `C` is constant on
each group orbit and selects a distinguished orbit representative.  P174's
map does neither in general: it applies only the particular projectivity
selected by the current least finite point, and then feeds the resulting set
back into the selector.  For example, at `p=5`, the translation-equivalent
sets `{0,4}` and `{0,1}` have P174 images `{4,infinity}` and `{1,infinity}`,
respectively.  Thus the P174 update is not a canonical-image map for the
translation action.  Jefferson–Jonauskyte–Pfeiffer–Waldecker do not give the
iterated forced-point tower, the inversion core, the modular no-wrap
criterion, or the nonuniform target fibre `0<=a<h(T)`.  Their machinery
therefore supplies no proof transfer of the retained theorem conjunction.

**Mandatory repair:** add this source to the paper's artificial-order
subtraction, to `SOURCE_VERIFICATION.md`, and to the scouting owner log; run
and record query variants using “minimal/canonical image,” “canonizing
element,” “ordered subset group action,” and “dynamic ordering.”  Canonical-
image and canonizing-element machinery must receive zero contribution credit.
A source that specializes those tools to P174's state-feedback iterate and
target-local interval remains an immediate kill switch.

Suggested `references.bib` record:

```bibtex
@article{JeffersonEtAl2019,
  author  = {Jefferson, Christopher and Jonauskyte, Eliza and
             Pfeiffer, Markus and Waldecker, Rebecca},
  title   = {Minimal and Canonical Images},
  journal = {Journal of Algebra},
  volume  = {521},
  pages   = {481--506},
  year    = {2019},
  doi     = {10.1016/j.jalgebra.2018.11.009}
}
```

Suggested zero-credit language for `SOURCE_VERIFICATION.md`:

> Jefferson–Jonauskyte–Pfeiffer–Waldecker own minimal/canonical images of
> subsets under ordered permutation-group actions, including canonizing
> elements and order-sensitive search. This removes all credit for artificial
> ordering or ordered group normalization as such. P174 is not constant on
> translation orbits and is not a canonical-image map; the source does not
> imply its state-feedback image tower or target-dependent modular pivot
> interval.

Suggested manuscript sentence, with the citation key above:

> Ordered canonical images and canonizing elements for subset actions are
> established machinery \citep{JeffersonEtAl2019}; artificial ordering and
> state-selected group normalization therefore receive no contribution
> credit here.

**Acceptance criteria:**

1. `references.bib` contains the verified record and `main.tex` cites it in
   the owner-boundary discussion, with no uncited entry;
2. `SOURCE_VERIFICATION.md` states both the zero-credit assignment and the
   precise non-transfer above;
3. the owner log records the alternate query vocabulary and retains a direct
   specialization/general-theorem kill switch; and
4. the lifecycle remains `PROVISIONAL_AMBER / HOLD_EXTERNAL` even if the
   expanded search produces no literal hit.

## 3. Re-derivation of the complete functional graph

Let `infinity` denote the projective point and let

```text
a(S) = min(S intersection F_p),
gamma_a(x) = 1/(x-a),
M(S) = gamma_(a(S))(S).
```

The hypotheses `2<=k<=p` ensure that every state has a finite point and that
a state avoiding infinity exists.

### 3.1 First and second images

For every pivot `a`, `gamma_a(a)=infinity`; hence every image contains
infinity.  Conversely, if `T` contains infinity, then
`S=gamma_0(T)` contains zero, has pivot zero, and
`M(S)=gamma_0^2(T)=T`.  Therefore

```text
im(M) = Z = {T : infinity in T}.
```

The unique preimage of zero under `gamma_a` is infinity.  A source avoiding
infinity consequently maps into `Z\Y`; a source containing infinity maps
into `Y`, where

```text
Y = {T : {0,infinity} subseteq T}.
```

Thus `M(Z) subseteq Y`.  On `Y`, the pivot is zero and `M` is projective
inversion, which swaps `0` and `infinity` and sends each nonzero `x` to
`x^(-1)`.  Its square is the identity, so every point of `Y` lies in
`im(M^2)`.  Hence `im(M^2)=Y`, `Y` is exactly the recurrent set, and
`M^4=M^2` on the full carrier.

**Disposition:** no change.

### 3.2 Exact tails and layer sizes

The forced-point alternatives give pointwise tails:

- `Y`: tail zero;
- `Z\Y`: one step into `Y`, so tail one;
- `X\Z`: one step into `Z\Y` and then `Y`, so tail two.

The corresponding counts are

```text
binom(p-1,k-2),  binom(p-1,k-1),  binom(p,k).
```

They sum to `binom(p+1,k)`.  The last count is positive because `k<=p`, so
tail two is attained rather than merely bounded by two.

**Disposition:** no change.

### 3.3 Recurrent periods, fixed points, and weak components

Every recurrent state is uniquely `{0,infinity} union A`, where `A` is a
`(k-2)`-subset of `F_p^*`.  For odd `p`, inversion on `F_p^*` has singleton
orbits `{1}` and `{-1}` and `(p-3)/2` two-element orbits.  An invariant
subset is a union of those orbits, so its size enumerator is

```text
(1+v)^2 (1+v^2)^((p-3)/2).
```

Taking the coefficient of `v^(k-2)` proves the fixed census.  Every other
core state is paired with its inverse, giving
`(R_(p,k)-F_(p,k))/2` two-cycles.  Since each functional-graph component has
one recurrent cycle, the weak-component count is
`(R_(p,k)+F_(p,k))/2`.

If a point is fixed by a positive iterate, it is periodic and hence belongs
to `Y`.  Odd iterates of inversion fix precisely the `F_(p,k)` fixed states;
even iterates fix all `R_(p,k)` core states.  This proves the displayed
fixed-iterate formula without including transient points.

At `p=2,k=2`, the core is `{0,infinity}` and is fixed, so the separately
declared `F_(2,2)=R_(2,2)=1` makes all formulas valid.

**Disposition:** no change.

## 4. Re-derivation of every target fibre

Every output contains infinity, so a target outside `Z` has no parent.  Let
`T` contain infinity and propose a pivot `a`.  Because `gamma_a` is a
projectivity, the only possible source is

```text
S_a = gamma_a^(-1)(T).
```

Its forced finite point is `a`, and every nonzero finite `y` in `T`
contributes the finite representative

```text
overline(a + y^(-1)).
```

For representatives `0<=a<p` and `1<=b<p`, there are exactly two cases:

```text
overline(a+b) >= a  iff  a+b<p  iff  a<p-b.
```

Therefore `a` is actually the least finite point of `S_a` exactly when

```text
0 <= a < p - max({overline(y^(-1)) : y in T intersection F_p^*} union {0})
          = h(T).
```

Each valid pivot yields one source, and two pivots cannot yield the same
source because both would have to be its least finite point.  The actual
pivots are consequently the initial interval `0,...,h(T)-1`, proving both
the fibre size and the coefficient-one marked polynomial.

This also classifies incoming depths: a core target has one recurrent
pivot-zero parent and `h(T)-1` depth-one parents; a target in `Z\Y` has
`h(T)` depth-two parents; a target outside `Z` has none.

**Disposition:** no wrap, uniqueness, or labelling repair.

## 5. Fibre distribution and unique maximum

Inversion permutes `F_p^*`.  Put `j=p-q`.  For a target containing infinity
with `beta(T)=j>=1`:

- if zero is absent, the inverse-label set has size `k-1`, includes `j`,
  and otherwise lies in `{1,...,j-1}`, giving `binom(j-1,k-2)` targets;
- if zero is present, that set has size `k-2`, giving
  `binom(j-1,k-3)` targets.

Pascal's identity gives `binom(j,k-2)=binom(p-q,k-2)`.  At `j=0`, the only
possibility is `T={0,infinity}` when `k=2`, matching `binom(0,k-2)` exactly.
Targets avoiding infinity contribute the separate `binom(p,k)` zero fibres.

A positive fibre exists exactly when `q<=p-k+2`.  At equality the count is
`binom(k-2,k-2)=1`; explicitly, the unique maximum target is

```text
{0,infinity} union {b^(-1) : 1<=b<=k-2}.
```

Finally, summing indegrees over all targets gives

```text
sum_(q=1)^p q binom(p-q,k-2) = binom(p+1,k),
```

which agrees with the carrier size.

**Disposition:** no change.

## 6. Boundary audit

- `p=2,k=2`: the three states form the displayed depth-two chain into the
  fixed core; direct reconstruction agrees with the manuscript.
- `k=2`: the empty maximum in `beta` occurs only for `{0,infinity}` and gives
  height `p`, including the endpoint `q=p` of the histogram.
- `k=p`: the depth-two layer and depth-one layer each remain nonempty; the
  unique maximum fibre has size two.
- `k=1`: the finite singletons map to `{infinity}`, which itself has no
  finite pivot, so the full singleton carrier does not support the stated
  autonomous map.
- `k=p+1`: the full projective line has pivot zero and is a separate fixed
  state.  Its exclusion is explicit and correct.
- prime powers are not claimed; the proof uses the ordered standard
  representatives of the prime field.

**Disposition:** all stated and excluded boundaries are coherent.

## 7. Independent executable audit

The Review-B program is
`docs/papers172_176_sequence/reviews/p174_review_b/verify_review_b.py`.
It imports only Python's standard library and imports no author, scouting, or
Review-A file.  Its representation and check strategy are distinct from
Review A's bit-mask implementation:

- every `gamma_a` is first materialized as a point permutation and inverted
  as a table;
- states are `frozenset` objects and fibres are recovered from the complete
  reverse edge relation;
- inverses in `F_p` are found by finite search rather than Fermat powering;
- tails and periods are recovered by generic orbit tracing;
- weak components are independently recovered by union--find;
- fixed iterates are counted directly for six exponents;
- a second symbolic layer checks every no-wrap pair and all depth/fibre
  identities for every prime through 101.

The frozen run performs **4,755,152 exact assertions**.  It exhausts every
allowed `k` for `p=2,3,5,7,11,13,17`: **51 complete boxes** and **282,889
states**.  It then checks **1,135** parameter boxes across all 26 primes not
exceeding 101 at the arithmetic/counting level.  The `k=1`, `k=p+1`, and
smallest graph boundaries are explicit controls.

Fresh-process replay with `PYTHONHASHSEED=0` is byte-identical to the
canonical transcript.  Pinned SHA-256 values are:

```text
c2eab055bb997ab974219ffdbaf5a6ce42f9bbd9add62ec31ca656b6fec7722c  verify_review_b.py
94fde0f68053fc5130357f598666a9b1e224d25d96113bae6cd0225a1dc81537  CANONICAL.txt
```

The executable is counterexample pressure, not the all-parameter proof or a
source-clearance mechanism.

## 8. Source and kill-switch audit

The four live references were re-opened on primary records and remain
accurately subtracted:

- [El Abdalaoui–Shparlinski](https://arxiv.org/abs/1711.11062) study
  trajectories of one fixed fractional-linear map; no state-selected pivot
  or subset fibre law is supplied.
- [Tricot](https://arxiv.org/abs/2408.14714) studies the
  `PGL(2,q)` action on projective-line subsets; ordinary group orbits are
  zero credit.
- [Aluffi–Faber](https://arxiv.org/abs/alg-geom/9205005) study `PGL(2)`
  orbits of projective configurations; configuration-orbit geometry is zero
  credit.
- [Grinberg–Mao v4](https://arxiv.org/abs/2405.08937v4) own the cyclic-
  rotation/simultaneous-group-multiplication quotient relevant to the killed
  AQN architecture; it is external pressure, not a P174 theorem input.

Internally, P96, P168, fixed-`PGL_2` controls, and especially AQN are properly
assigned zero credit.  AQN's hostile gate kills the general adaptive-section
story because its image and constant translation-orbit fibres follow from an
owned quotient action.  P174's source set is instead cut by a
target-dependent no-wrap inequality.  Neither AQN nor the newly located
canonical-image source produces that interval, the two nested forced-point
images, or their composition as a state-feedback iterate.  This is why the
kill switch stays open rather than firing now.

The residual is nevertheless narrow: a two-step clock, a classical
involution, one elementary modular threshold, and an explicitly artificial
order.  Review B therefore confirms only

```text
PROVABLE AS STATED / PROVISIONAL_AMBER / HOLD_EXTERNAL.
```

It does not recommend upgrading the value gate.

## 9. Closure

After `P174-RB-MIN-01` satisfies its four acceptance criteria, Review B has
no remaining mathematical or executable repair.  The final allowed status
is still

```text
PASS / PROVISIONAL_AMBER / HOLD_EXTERNAL.
```

No bounded search outcome or successful verifier run authorizes external
circulation.

## 10. Round-2 delta acceptance --- CLOSED

**Read-only acceptance date:** 2026-09-03 UTC  
**Open finding counts after acceptance:** **Critical 0 / Major 0 / Minor 0**  
**Disposition:** `P174-RB-MIN-01 CLOSED / PROVISIONAL_AMBER / HOLD_EXTERNAL`

The coordinator's Round-2 repair satisfies all four acceptance criteria:

1. `main.tex` now cites Jefferson--Jonauskyte--Pfeiffer--Waldecker at the
   precise owner boundary and `references.bib` contains the verified 2019
   *Journal of Algebra* record, DOI `10.1016/j.jalgebra.2018.11.009`, and
   arXiv identifier `1703.00197`; the entry is neither uncited nor used as
   positive evidence.
2. `SOURCE_VERIFICATION.md`, `README.md`, and `CLAIMS_EVIDENCE.md`
   consistently assign minimal/canonical images and canonizing elements
   zero credit.  They also state the exact non-transfer: canonical-image
   machinery minimizes over a group and is orbit-constant, whereas P174
   applies one current-pivot-selected projectivity, is orbit-nonconstant,
   and asks for a state-feedback tower and target-dependent pivot interval.
   No claim that the cited source proves those residual statements appears.
3. The live owner log now records the three missing query families
   `minimal canonical image permutation group subset`, `canonizing element
   ordered finite set group action`, and `dynamic ordering canonical image
   finite group`; it records the same primary metadata and preserves the
   specialization/general-owner kill switch.  In particular, it explicitly
   says that a later theorem transferring to the orbit-nonconstant feedback,
   two-step tower, or pivot interval would kill the residual.
4. Every lifecycle surface remains `PROVISIONAL_AMBER / HOLD_EXTERNAL`;
   neither the subtraction nor this closure upgrades value or novelty.

The accepted source/PDF pins are

```text
5d1790a4fc0f15a79e3632646783598cc3d97da61fca11735c20f881c58df958  main.tex
18b4f989c2bb17ef4c53a2685214b3d2e111924bcca997efb43aca640ecc1066  references.bib
b428c24be406d8c2cef9c1d6fc5a2630495f2eed54473ed1dec7b1120444ff7f  main.pdf
b428c24be406d8c2cef9c1d6fc5a2630495f2eed54473ed1dec7b1120444ff7f  main_round2.pdf
2bc0f372f81436e74d2ee8672fbb10c59638f0f1e80f2aeca4f9fd9ab095737d  OWNER_SEARCH_LOG.md
```

The historical Review-B ledger still contains one Minor finding, but it is
closed; there is no remaining repair.  This was a delta acceptance only: the
reviewer made no change to the Round-2 manuscript, bibliography, PDF, or
source ledger.
