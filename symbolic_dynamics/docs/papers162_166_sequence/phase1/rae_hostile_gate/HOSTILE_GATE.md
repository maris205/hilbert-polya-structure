# RAE fresh independent hostile gate

**Literal system:** independently and uniformly choose an alphabet letter at
each epoch and delete all of its occurrences from the current finite word  
**Review date:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`  
**Decision:** **`KILL_DEPENDENT_FIBRE_AXIS_AND_OCCUPIED_PROJECTION_MEET_LANE`**  
**Mathematical findings:** **0 Critical / 2 Major / 3 minor**

## 1. Outcome first

The displayed formulas in the RAE scout are mathematically correct.  A fresh
implementation, importing no author code, confirms the commuting-idempotent
normal form, the full arbitrary-source kernel (including unreachable targets),
the absorption law, the random-operator image distribution, the all-source
fibre formula and its ordinary generating function, all target classes and all
mass identities.  It also derives and checks the complete spectrum on every
capped word carrier.

RAE nevertheless fails the P162--P166 selection threshold.  The claimed
second axis is not independent of the first:

```text
A_(q,t,n)(v) = sum_(u in A^n) K_t(u,v).                    (G1)
```

Thus Theorem B is exactly a source-layer column sum of the complete kernel in
Theorem A.  Its insertion proof is an efficient evaluation of that sum, not a
new invariant or logically separate inverse theorem.  After subtracting the
classical coupon collector, standard subalphabet projection, elementary
Stirling/binomial counts, and the Boolean-semigroup action of commuting
idempotents, no paper-sized second theorem remains.  The historical portfolio
also expressly excluded projection/overwrite/coupon processes, and same-batch
RPS was killed for the analogous random-meet silhouette.  RTI and P158 already
occupy stronger, genuinely target-structured stochastic-intersection slots.

This is a **value/allocation kill, not a counterexample kill**.  An exact
name-level owner of the whole RAE package was not found in the bounded search;
that non-hit does not repair the theorem-axis failure and is not evidence of
novelty.

## 2. Pinned author package

The following hashes were taken before any review artifact was created.  A
final recheck is required to match them byte for byte:

| author file | SHA-256 |
|---|---|
| `SCOUT.md` | `f3008b01c98604ab24f185c38bb729e798d6a93321e0b45282774242f244d365` |
| `OWNER_SEARCH_LOG.md` | `371e9173f9ab762763559e073fd5b30ad23f04463bc97b5d984266a7c98f0487` |
| `verify_scout.py` | `c44ae347a25262870af4ba3b9b32f1cd8e9217517dd218c48fb2be7851487f8b` |
| `CANONICAL.txt` | `a974af3288ee2fc5b830ad34511355ee20c299667116fc316643c2d9856ed459` |

No author file was edited.

## 3. Cold derivation from the literal map

Let the alphabet be `A`, with `|A|=q`, and let `E_a` delete all occurrences
of `a`.  For a subset `C` of the alphabet, write `pi_C` for the word morphism
that retains precisely the letters in `C`.

### 3.1 Commuting all-occurrence erasers

For all letters `a,c` and every word `w`,

```text
E_a E_a(w)=E_a(w),              E_a E_c(w)=E_c E_a(w).     (G2)
```

Both equalities follow position by position: a position survives exactly when
its letter is outside the set of erasers used.  Hence a history
`h=(h_1,...,h_t)` has the pathwise action

```text
E_h(w)=pi_(A \ supp(h))(w).                                (G3)
```

This includes `t=0`, where the history support is empty and the action is the
identity.  Sequential order carries no information beyond the coupon-support
set.

### 3.2 Arbitrary-source, every-target `t`-step kernel

Fix source `u` and target `v`.  Put

```text
B=supp(v),                   D=supp(u) \ B.
```

A history can send `u` to `v` only if

```text
B subseteq supp(u)  and  pi_B(u)=v.                        (G4)
```

Under (G4), it must avoid all `b=|B|` retained letters and hit every one of
the `d=|D|` deleted source letters.  Letters absent from `u` are free.  By
inclusion--exclusion, the exact history count is

```text
K_t(u,v)=sum_(j=0)^d (-1)^j binom(d,j)(q-b-j)^t.           (G5)
```

It is zero when (G4) fails.  At `t=0`, (G5) is `1` exactly for `u=v` and is
zero otherwise.  For the empty target, `B` is empty and (G5) requires every
source letter to have appeared in the eraser history.  Dividing by `q^t`
gives the full Markov kernel.

### 3.3 Coupon absorption and last surviving colour

If `u` has support size `b`, absorption is exactly the collection time of its
`b` relevant letters in iid draws from all `q` letters.  Consequently

```text
Pr(tau_u <= t)
 = q^(-t) sum_(j=0)^b (-1)^j binom(b,j)(q-j)^t,            (G6)

E[tau_u]=q H_b.                                            (G7)
```

An independent first-step derivation of (G7) is useful.  If `e_b` denotes the
mean time with `b` relevant letters uncollected, then

```text
e_0=0,      e_b=1+(q-b)e_b/q+b e_(b-1)/q,
```

so `e_b-e_(b-1)=q/b`.  For `b>=1`, symmetry of the relative first-occurrence
order makes each initial support letter the last one erased with probability
`1/b`; immediately before that erasure the word is the corresponding
monochromatic projection.  There is no “last nonempty projection” when
`b=0`.

Among words of length at most `L`, the largest mean is
`q H_min(q,L)`, achieved exactly by support-maximal words.  This includes the
boundary `L=0`, where the empty word is the sole state and the mean is zero.

### 3.4 Coupon support and random-operator image

The number of length-`t` histories with exactly `s` distinct erasers is

```text
(q)_s S(t,s).                                               (G8)
```

For any such history, (G3) shows that its image on the capped carrier
`A^(<=L)` is the set of words over the `q-s` retained letters.  Its size is

```text
I_L(s)=sum_(m=0)^L (q-s)^m.                                (G9)
```

Equations (G8)--(G9) determine the image-size distribution after pushing the
support law through `s -> I_L(s)`.  For `L>=1` this map is injective.  For
`L=0`, all supports give image size one, so equal-size contributions must be
aggregated.

### 3.5 All-source/every-target source-length fibre

Fix a target `v` of length `m` and support `B`, `|B|=b`.  Fix a history
support `H subseteq A\B` of size `s`.  There are `s! S(t,s)` histories with
exact support `H`.  A source of length `n` is obtained uniquely by selecting
the `m` positions that contain `v`, in its given order, and filling all other
positions with letters of `H`.  This gives `binom(n,m)s^(n-m)` sources.  After
choosing `H`,

```text
A_(q,t,n)(v)
 = binom(n,m) sum_(s=0)^min(q-b,t)
       (q-b)_s S(t,s) s^(n-m),                             (G10)
```

for `n>=m`, and zero for `n<m`; the convention `0^0=1` is necessary.  Summing
the binomial series gives

```text
sum_(n>=m) A_(q,t,n)(v) z^n
 = z^m sum_s (q-b)_s S(t,s)/(1-sz)^(m+1).                 (G11)
```

The number of length-`m` targets with support `b` is the elementary onto-word
count `(q)_b S(m,b)`.  Summing all output fibres gives `q^(n+t)` because each
source/history pair has one output.

All edge cases survive: the empty target has `m=b=0`; at `t=0`, only `s=0`
contributes; at `n=m`, every history avoiding `B` fixes `v`; and targets longer
than the source have zero fibre.

### 3.6 The decisive dependence identity

By definition, `K_t(u,v)` counts histories for one source, whereas
`A_(q,t,n)(v)` counts the same histories after allowing every `u in A^n`.
Therefore (G1) holds before either closed form is evaluated.  It is not merely
a numerical coincidence checked on small boxes.  The insertion calculation
proves a useful summation identity between (G5) and (G10), but it cannot be
used as the “genuinely separate inverse, fibre, structural, extremal, or
identifiability conclusion” demanded by the batch anchor.

The source-length “spectrum” in (G11) also contains no new hidden dynamics:
its bases `s` are precisely history-support sizes, and its pole orders arise
from the binomial insertion factor.

### 3.7 Complete capped Markov-operator spectrum

There is an additional exact conclusion, but it does not rescue the package.
On `A^(<=L)`, let `C=sum_(a in A) E_a`, so the transition matrix is `P=C/q`.
Order words by nondecreasing length.  Each `E_a` either fixes a word or moves
it to a strictly shorter word, hence `C` is triangular.  A word with support
size `b` has diagonal entry `q-b`.  Since the erasers commute and are
idempotent, they are simultaneously diagonalizable over characteristic zero.
Thus

```text
lambda_b = 1-b/q,                         0<=b<=min(q,L),  (G12)
M_(q,L)(b)=sum_(n=b)^L (q)_b S(n,b).                       (G13)
```

The independent verifier checks the squarefree annihilator
`product_b(C-(q-b)I)=0` directly.  But (G12)--(G13) are an immediate Boolean
semilattice/commuting-projection specialization plus the same Stirling word
census.  Brown's left-regular-band theory and later R-trivial-monoid theory
make this spectral mechanism zero credit; it is not a third axis.

## 4. Findings and executable repairs

### Major RAE-M1 — the advertised second theorem is a kernel marginal

The scout says that (3)--(5) and (6)--(8) have separated proof mechanisms.
They do use two counting presentations, but (G1) shows that the full value of
Theorem B is already determined by Theorem A.  The target spectrum depends
only on `(m,b)`, exactly the data exposed by the same history-support
projection.

**Repair:** do not describe the two theorems as independent axes.  Promotion
would require a new all-parameter result not obtainable as a row/column sum,
specialization, generating transform, moment, or elementary marking of the
kernel.  No such result is present, so this repair cannot promote RAE.

### Major RAE-M2 — owner and portfolio subtraction changes GREEN to KILL

The owner log omits the general semigroup-walk owner for commuting idempotent
random maps and the strongest internal precedents.  More importantly, the
P107--P111 stochastic breadth ledger explicitly lists
`projection/overwrite/coupon processes` among its hard exclusions; the
P112--P116 kill ledger separately treats theorem-thin projections as a kill
class.  Same-batch RPS has already been killed as a generic random-meet process
with no independent target inverse atlas.  RTI survives only because its
stabilizer/coset polynomial is not a rank marginal, while P158 has labelled
component geometry and a nontrivial saturation obstruction.

**Repair:** add Brown/Ayyer--Schilling--Steinberg--Thiery to zero credit; record
the historical hard exclusion and the RPS/RTI/P158 coexistence test; change the
candidate status to KILL.  An exact literal owner non-hit is not a basis for
overriding these gates.

### Minor RAE-m1 — the author kernel verifier does not test infeasible targets

`verify_scout.py` constructs a counter of observed outputs and loops over
`for target in observed`.  It therefore checks all positive cells but not the
zero values of (G5) for every infeasible candidate target, contrary to the
statement in `SCOUT.md`.

**Repair:** for each tested source enumerate every word of length at most the
source length (and at least one overlength layer), compare
`observed[target]` to the formula, and require explicit zero-cell coverage.
The independent verifier does this for **287,027 zero cells**.

### Minor RAE-m2 — the mean-time check is tautological

The author verifier assigns `expected=sum(q/j)` and compares it to a second
calculation of the same sum.  This does not independently test the stochastic
claim.

**Repair:** use the first-step recurrence in Section 3.3, or sum independently
enumerated exact tails.  The gate verifier uses the recurrence.

### Minor RAE-m3 — two degenerate boundaries need explicit wording

The last-survivor probability `1/b` is undefined for the empty initial word,
and at `L=0` all possible history-support sizes induce the same image size
one.  Neither issue invalidates the formulas, but the prose currently states
them without the necessary branch/aggregation.

**Repair:** restrict the last-survivor sentence to `b>=1`; state the `b=0`
empty boundary; and describe (G8)--(G9) as a pushforward distribution that
aggregates supports with equal image size (especially `L=0`).

## 5. Independent executable evidence

`verify_gate.py` is a standard-library implementation written from the
literal map.  It imports no author module and checks:

- idempotence, commutation, and history projection on three alphabet/cap
  boxes;
- every candidate target, including zero and overlength fibres, for the
  arbitrary-source kernel;
- the coupon CDF, a genuinely independent first-step mean recurrence, and the
  last-colour symmetry with the empty-support boundary separated;
- the history-support law and the complete pushed-forward image-size law,
  including collisions at `L=0`;
- all-source/every-target fibres on three boxes, global mass, the direct
  column-sum identity (G1), OGF coefficients, and support-class counts; and
- the full capped operator matrices in dimensions `31`, `40`, and `21`, their
  triangular diagonals, multiplicities, and squarefree annihilators.

The frozen run contains **572,070 exact assertions**.  Two fresh runs are
required to byte-match `CANONICAL.txt`.  Enumeration is counterexample
pressure, not proof; Sections 3.1--3.7 are the all-parameter arguments.

## 6. Final gate

```text
MATHEMATICS PASS
THEOREM_AXIS FAIL: ALL-SOURCE FIBRE = SOURCE-LAYER COLUMN SUM OF KERNEL
OWNER_SUBTRACTION FAIL: COUPON + PROJECTION + BOOLEAN SEMIGROUP + ELEMENTARY COUNTS
PORTFOLIO FAIL: HISTORICAL EXCLUSION + RPS/P158/RTI STOCHASTIC-MEET CROWDING
RAE KILL_DEPENDENT_FIBRE_AXIS_AND_OCCUPIED_PROJECTION_MEET_LANE
HOLD_EXTERNAL
```

No paper number should be allocated.  Re-entry would require a genuinely new
literal dynamic or a new structural theorem that is not a transform or
marginal of the complete kernel; adding more moments, support marks, or capped
spectra is insufficient.
