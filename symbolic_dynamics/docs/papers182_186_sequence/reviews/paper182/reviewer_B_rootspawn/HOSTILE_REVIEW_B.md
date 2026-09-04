# Hostile Review B — P182 cyclic subspace-lattice comparator

**Reviewer process:** `/root/reviewer_a_p183_p184`, process-separated from the
P182 author and from P182 Review A  
**Review date:** 2026-09-03 UTC  
**Frozen input:** immutable Round 1  
**Decision:** `ACCEPT_ROUND1_FOR_COORDINATOR_GATE`  
**External lifecycle:** `HOLD_EXTERNAL`

## Bottom line

The Round-1 theorem package is provable as stated.  I found zero Critical,
Major, and Minor defects after reopening the universal lattice identity, every
finite-field population, every target fibre, the full fibre histogram, exact
extremizer sets, low-dimensional boundaries, the non-prime field case, source
scope, and artifact agreement.

This review authorizes only the next internal coordinator gate.  It does not
authorize posting or submission and does not convert the bounded owner-search
non-hit into novelty, priority, completeness, or freedom-to-operate evidence.
The paper remains `OWNER_AMBER / HOLD_EXTERNAL`.

This is process separation, not a claim of statistically independent errors.
The processes share the theorem specification, standard finite-geometry
identities, and the Python runtime, even though their mathematical encodings
and graph checks differ.

## Frozen binding and read-only discipline

No file under `papers/182-cyclic-subspace-lattice-comparator/` was edited.
The review binds:

| frozen object | SHA-256 |
|---|---|
| `main.tex` | `9d496bf69fc3d7426c1f95bb7bacdaf0ea0cd6c7e3b36c5d3c55f64236f088c7` |
| `main_round1.pdf` | `880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07` |

Round 1 is byte-identical to `main_round0_original.pdf`, as expected after a
zero-finding Review A.  The author manifest verifies all 19 non-self rows and
the Review-A manifest verifies all four non-self rows.  The Round-1 PDF is
329,096 bytes and four A4 pages, unencrypted, with no JavaScript; all fonts are
embedded and subset.  Its text contains the `328,700`-transition and
`1,667,850`-assertion author receipts, all declarations, and `HOLD_EXTERNAL`.
The build logs contain no undefined reference/citation or box warning.

**Terminal-manifest rebind (2026-09-03).**  The original theorem source, PDF,
and every mathematical attack in Review B are unchanged.  Only the terminal
paper manifest binding expanded from 15 to 19 rows, adding
`IMPROVEMENT_LOG.md`, `FINAL_QA.md`, `main_round1.pdf`, and
`main_round2.pdf`.  These four hashes hard-fail on mismatch but are excluded
from the original scientific assertion census, so the exact receipt remains
2,421,778.  The verifier prints `terminal_manifest_rows=19` and
`terminal_lifecycle_checks_excluded_from_exact_assertions=4`.  The rebound
verifier SHA-256 is
`4c9c36ac431ec55ce2193a356bdefe758c44a1cd84668c1795da23fa5c1e7959`
and the canonical-output SHA-256 is
`0653af8f6d3a196eaf5f05c6d531a57d0809a05f749c89b66e090fb85dcb91d8`.

## Reviewer-owned representation

The verifier imports neither previous verifier.  It does not represent a
subspace by an RREF basis (author route), nor by a closure-generated bitset of
all vectors (Review-A route).

Instead, a primal subspace is represented by its **annihilator flat** in the
dual projective geometry.  The flat is a `frozenset` of normalized
one-dimensional linear functionals.  Projective flats are enumerated from
independent point sets; Gaussian elimination is used only as a rank oracle,
not as the stored subspace representation.  Primal meet and join are computed
through the dual identities

\[
 (A\cap B)^\perp=A^\perp+B^\perp,
 \qquad
 (A+B)^\perp=A^\perp\cap B^\perp.
\]

Functional-graph status is checked pointwise from explicit `T`, `T^2`, and
`T^4` values and algebraic recurrence predicates.  This uses neither the
author's forward-orbit decomposition nor Review A's indegree peeling and
reverse breadth-first distances.

The field `GF(4)` is implemented as
`F_2[x]/(x^2+x+1)`.  All field axioms and all nonzero inverses are checked
before its projective geometries are constructed.

## Exact audit coverage

The reviewer control contains 19 finite-field boxes:

\[
\{2\}\times\{0,1,2,3,4\}\ \cup\
\{3,4\}\times\{0,1,2,3\}\ \cup\
\{5,7\}\times\{0,1,2\}.
\]

It includes four genuine `GF(4)` boxes, 414,236 explicit transitions, and
2,421,778 assertions.  All author rows in this overlap agree exactly, including
the complete `(q,d)=(2,4)` census and the `(7,2)` fibre value `kappa_2=58`.

The universal part is separately tested on chains of sizes 1, 2, 4, and 7,
the Boolean lattice `B_3`, the nondistributive modular diamond `M3`, and the
nondistributive nonmodular pentagon `N5`.  These are not evidence for all
lattices by exhaustion; they specifically pressure-test whether the displayed
proof accidentally imports distributivity or modularity.

Two fresh processes reproduced `CANONICAL.txt` byte for byte before the
package was sealed.

## Hostile theorem audit

### 1. Universal square and `T^4=T^2`

Put `m=a meet b` and `j=a join b`.  Direct substitution gives

\[
T^2(a,b,c)=(j,c\wedge m,c\vee m).
\]

With `u=c meet m` and `v=c join m`, absorption gives
`T^3=(v,u,j)` because `u<=m<=j`, and then `T^4=(j,u,v)=T^2` because
`u<=v`.  Only lattice order and absorption occur.  The argument survives on
both `M3` and `N5`; no modular or distributive step is hidden.

The temporal inference is valid: for `y=T^2x`, one has `T^2y=y`.  Therefore
`y` lies on a cycle of length one or two, excluding longer recurrent cycles
without a finiteness loophole.

**Verdict:** survives.

### 2. Exact image, recurrence, fixed points, two-cycles, and depth

Every image is `(c,m,j)` with `m<=j`, and
`T(m,j,c)=(c,m,j)` proves the converse.  Hence the stated image is exact,
not merely an upper bound.

Solving `T^2(a,b,c)=(a,b,c)` first gives `b<=a`; after that substitution,
the remaining equations give `b<=c`.  On this set `T(a,b,c)=(c,b,a)`, so a
recurrent point is fixed precisely when `a=c`; every other recurrent orbit is
one strict two-cycle.  The manuscript explicitly defines “strict two-cycle”
as an orbit, making `(rho-alpha)/2` the correct object count rather than a
state count.

The first image is recurrent exactly when `a meet b <= c`.  Thus a source not
already recurrent has depth one under that condition and depth two otherwise.
The depth classes are disjoint and exhaustive.  For every `d>=1`, taking
`a=b` to be a line and `c=0` realizes depth two; `d=0` is separately the
unique depth-zero fixed state.

The reviewer checked these predicates pointwise in all finite boxes and all
seven auxiliary lattices, then checked the exact image and strict-cycle sets.

**Verdict:** survives.

### 3. Population formulas

For a middle subspace `B` of dimension `b`, its superspaces are in bijection
with subspaces of `V/B`.  One superspace gives `alpha_d` fixed points; two
independent superspaces give `rho_d` recurrent states.  An arbitrary first
coordinate times an interval gives `g_d alpha_d` image points, and the
outer-swap pairs the `rho_d-alpha_d` nonfixed recurrent states.

For `Q_n`, projection modulo a fixed `a`-space sends a disjoint `s`-space
injectively to an `s`-space in the quotient.  A fixed quotient subspace has
`q^(as)` graph lifts.  For `eta_d`, the value `M=A meet B` is unique; quotient
images of `A,B` are disjoint, while `C/M` is arbitrary.  Consequently the
formula counts every source with `A meet B <= C` exactly once.

Direct dual-projective enumeration agrees with `g_d`, `Q_d`, `alpha_d`,
`rho_d`, `eta_d`, every depth population, and all displayed sample rows.

**Verdict:** survives.

### 4. Target-local complement fibres

A predecessor of `(C,M,J)` has third coordinate forced to `C` and must satisfy
`A meet B=M`, `A+B=J`.  If `M` is not below `J`, there is no predecessor.  If
`M<=J`, quotienting by `M` is a bijection to ordered complementary pairs in
`J/M`; no lift multiplicity is lost because both `A` and `B` contain `M` and
lie in `J`.

This review tests more than total indegree.  For **every** interval `[M,J]`
and every first subspace `A` in that interval, it directly counts the valid
second complements and obtains

\[
q^{a(k-a)},\qquad
k=\dim(J/M),\quad a=\dim(A/M).
\]

Summation gives `kappa_k`, and every carrier target has exactly the predicted
indegree.  Empty fibres, positive-fibre mass, and the image set agree exactly.

**Verdict:** survives.

### 5. Full histogram and complete extremizers

An interval of quotient dimension `k` is specified uniquely by choosing
`M` of dimension `m` and then `J/M` as a `k`-subspace of `V/M`.  Multiplying
by the arbitrary target coordinate `C` produces exactly

\[
g_d\sum_{m=0}^{d-k}{d\brack m}_q{d-m\brack k}_q
\]

targets of fibre `kappa_k`.  The other `g_d^3-g_d alpha_d` targets are exactly
the empty-fibre set.

The hyperplane injection from ordered decompositions in dimension `k` to
dimension `k+1` misses the explicit pair `(ell,H)`, so the `kappa` sequence is
strictly increasing.  The control checks the entire histogram and exact set
equality for both extremal classes:

- maximum `kappa_d`: precisely all `(C,0,V)`, exactly `g_d` targets;
- minimum positive fibre 1: precisely all `(C,M,M)`, exactly `g_d^2` targets.

For `d=0`, these are the same unique target and all formulas return one.  For
`d=1`, the verifier explicitly obtains `kappa=(1,2)`, so the first strict step
and both extremizer descriptions are nonvacuous and correct.

**Verdict:** survives.

## Source and owner-language audit

All five bibliography keys resolve and are cited.  The manuscript uses
Birkhoff only for lattice axioms/absorption; Goldman--Rota for finite-vector-
space enumeration; Chajda--Länger for subspace and complement counts; Hong for
a different one-register Tamari pop operator; and Gasanova--Nicklasson for
static Hibi meet/join sorting relations.  None is represented as supporting
the literal three-register functional graph.

The primary metadata agree with the bibliography at the
[AMS Birkhoff volume surface](https://bookstore.ams.org/COLL/25),
[Goldman--Rota Wiley record](https://onlinelibrary.wiley.com/doi/10.1002/sapm1970493239),
[Chajda--Länger Springer record](https://link.springer.com/article/10.1007/s00500-019-03866-y),
[Hong article record](https://www.sciencedirect.com/science/article/abs/pii/S019688582200046X),
and [Gasanova--Nicklasson Springer record](https://link.springer.com/article/10.1007/s10801-023-01294-8).
In particular, Chajda--Länger Theorem 11 states the exact
`q^(a(k-a))` fixed-subspace complement count assigned zero credit here.

The ownership paragraph remains disciplined: it assigns standard ingredients
zero contribution credit, labels the exact-owner screen as bounded, expressly
denies novelty and priority consequences, and makes a later literal or
equivalent owner a kill switch.  The internal collision subtraction is not
presented as external priority evidence.

**Verdict:** sources and lifecycle language survive; `HOLD_EXTERNAL` retained.

## Findings ledger

### Critical findings (0)

None.

### Major findings (0)

None.

### Minor findings (0)

None.

No paper repair is requested.  A byte-identical Round-2 receipt is acceptable.
Any content change for another reason reopens every proof, source, artifact,
and reproducibility gate.

## Residual risks that are not findings

1. The finite controls are bounded falsifiers, not proofs of the all-lattice
   or all-prime-power statements; the generic proofs carry those quantifiers.
2. Process separation does not imply independent errors.
3. Ownership remains amber until the planned deeper database and citation-
   chain search is completed.

## Reproduction

From the repository root:

```bash
python3 docs/papers182_186_sequence/reviews/paper182/reviewer_B_rootspawn/verify_review_b_p182.py
```

Acceptance requires exit code zero and stdout byte-identical to
`CANONICAL.txt`.  Its terminal receipt includes
`terminal_manifest_rows=19`,
`terminal_lifecycle_checks_excluded_from_exact_assertions=4`,
`author_manifest_rows=19`, and `exact_assertions=2421778`.  The package
`SHA256SUMS` excludes itself.
