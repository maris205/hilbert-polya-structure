# Independent hostile gate — multiplicity-profile descent (MPD)

**Date:** 2026-09-03  
**Verdict:** `RED / KILL_DIRECT_TEMPORAL_OWNER`  
**Mathematics:** `PASS_AFTER_N1_HEIGHT_SYNTAX_REPAIR`  
**External status:** `HOLD_EXTERNAL`  
**Paper consequence:** do **not** allocate or draft P170 from this candidate.

This is a kill-first gate.  A correct theorem is not enough.  The frozen
contract says that a direct source owning either proposed residual pillar
kills the candidate.  The forward map and frequency-depth programme are
already recorded literally in OEIS A225485/A225486, their depth census and
maximal-depth refinements are recorded in A325280/A325282, and their plateau
lengths are explicitly identified with first differences of Levine's sequence
in A325258.  In addition, Claes--Miyamoto (2026) define exactly the proposed
canonical lift, list its orbit from `(2)`, give its tail-sum/conjugation form,
and give its weighted-size identity.  This is a direct temporal-owner hit,
not a bounded non-hit and not merely a thematic neighbour.

The every-target fibre series survives the bounded search as a correct
target-resolved interpretation, but it is one remaining axis built from a
standard monomial-symmetric specialization.  It cannot restore the two-axis
paper contract after the literal dynamics, maximum-depth sequence, Levine
lift, and threshold platform have been subtracted.

## 1. Literal normalization

Partitions below are written in weakly decreasing order.  For a nonempty
partition `lambda`, let

```text
D(lambda) = decreasing sort of the positive multiplicities of its
            distinct parts.
```

For `mu=(mu_1>=...>=mu_r)`, let

```text
L(mu) = (r repeated mu_r times, ..., 2 repeated mu_2 times,
         1 repeated mu_1 times).
```

Thus `D(L(mu))=mu`.  The absorption depth `tau(lambda)` is the number of
arrows needed to reach `(1)`, so `tau((1))=0`.  This convention must be kept
separate from sources that assign a positive depth to an already-singleton
multiset; all nonterminal examples and all maxima for weights at least two
are unaffected.

## 2. Independent derivation

No proof step below imports the scout's induction or its verifier.

### 2.1 Ferrers containment

Let `mu=D(lambda)` and let `r` be the number of distinct parts of `lambda`.
The `k`th column of `L(mu)` has length

```text
(L(mu))'_k = mu_k+...+mu_r.                         (2.1)
```

Among `r` distinct positive integers, at least `r-k+1` are at least `k`.
Their multiplicities have sum at least the sum of the `r-k+1` smallest
multiplicities of `lambda`, namely the right side of (2.1).  Since
`lambda'_k` sums the multiplicities of *all* parts at least `k`,

```text
L(D(lambda)) subseteq lambda.                       (2.2)
```

This proves the claim column by column and does not use the numerical Levine
prefix.

### 2.2 Monotonicity of the lift

If `mu subseteq nu` in Ferrers order, then `mu_i<=nu_i` for every row of
`mu`.  Applying (2.1), and adding the nonnegative extra tail of `nu` when it
has more rows, gives

```text
(L(mu))'_k <= (L(nu))'_k
```

for every `k`.  Hence `L(mu) subseteq L(nu)`.  Combining this with (2.2)
inductively gives the useful, stronger statement

```text
L^j(D^j(lambda)) subseteq lambda                    (2.3)
```

for every defined iterate `j`.

### 2.3 Recurrence and termination

The new total is

```text
|D(lambda)| = length(lambda) <= |lambda|.
```

Equality holds only for `lambda=(1^m)`.  If `m>1`, then

```text
(1^m) -> (m) -> (1),
```

so a strict total decrease occurs within two arrows.  Therefore every orbit
reaches `(1)`, and `(1)` is the unique recurrent (hence unique periodic and
fixed) state.

### 2.4 Exact depth versus at-least depth

Set `Lambda_1=(2)` and `Lambda_d=L^(d-1)(2)`.  The depth-one base must be
handled literally: every exact-depth-one partition is a singleton part
`(m)` with `m>=2`, so it contains `(2)`.  In particular, one must not try to
prove this base by applying `L(D(lambda))`.

For `d>=2`, an exact-depth-`d` state satisfies

```text
D^(d-1)(lambda)=(m),  m>=2.
```

Since `(2) subseteq (m)`, lift monotonicity and (2.3) give

```text
Lambda_d
  = L^(d-1)(2)
  subseteq L^(d-1)(D^(d-1)(lambda))
  subseteq lambda.                                  (2.4)
```

Also `D after L` is the identity, so `Lambda_d` really has exact depth `d`.
Containment plus equal size forces equality of partitions.  Thus the least
size at exact depth `d` is `a_d=|Lambda_d|`, uniquely at `Lambda_d`.

This does not by itself settle the union of all deeper layers.  Here
`Lambda_1=(2)` and `Lambda_2=(1,1)` are incomparable and both have size two.
From `d=2` onward, `Lambda_d` is strictly contained in `Lambda_(d+1)`:
containment follows from `(1,1) subset (2,1)` and lift monotonicity; strictness
follows from injectivity of `L` (`D after L` is the identity).  Therefore
`a_2<a_3<a_4<...`.  It follows separately that:

- depth at least one has exactly two size-two minimizers, `(2)` and `(1,1)`;
- for every `d>=2`, depth at least `d` has the unique minimizer `Lambda_d`.

The first thresholds are

```text
2, 2, 3, 4, 7, 14, 42, 213, 2837, 175450.
```

### 2.5 The N=1 boundary

The contract's display

```text
H(N)=max {d>=0 : a_d<=N}
```

is syntactically undefined at `d=0`, because only `a_d` for `d>=1` was
defined.  The minimal repair is

```text
H(N)=max( {0} union {d>=1 : a_d<=N} ).              (2.5)
```

Equivalently one may define `a_0=1`.  Formula (2.5) gives `H(1)=0`, as it
must because the carrier is just `{(1)}`.  For `N>=2`, it gives the proposed
threshold inverse.

### 2.6 Every-target fibre, repeated parts included

Fix a target `mu` of length `r`.  A source in its fibre has increasing
distinct part values

```text
1 <= x_1 < ... < x_r
```

and their multiplicities form one **distinct** permutation
`alpha=(alpha_1,...,alpha_r)` of the parts of `mu`.  Put `x_0=0`,
`g_j=x_j-x_(j-1)>=1`, and `S_j(alpha)=alpha_j+...+alpha_r`.  Then

```text
source size
 = sum_i alpha_i x_i
 = sum_j g_j S_j(alpha).
```

Summing independently over the positive gaps gives

```text
Phi_mu(q)
 = sum_{alpha in Orb(mu)}
     product_j q^(S_j(alpha))/(1-q^(S_j(alpha))).   (2.6)
```

`Orb(mu)` must be a set of distinct permutations.  For example, for
`mu=(2,2)`, summing over both labelled permutations doubles every coefficient.
Direct enumeration confirms this exact factor-two failure of the naive
`r!`-term version.

Equivalently, choose the distinct positive indices `x_i` first and assign the
exponents given by a distinct permutation of `mu`; this is precisely
`m_mu(q,q^2,...)`.  It is the specialization beginning with `q`, not the
occasionally used stable convention beginning with `1`.

Since `x_i>=i`, rearrangement gives

```text
sum_i alpha_i x_i >= sum_i i mu_i =: w(mu).
```

Equality forces `x_i=i` and the descending multiplicity order
`alpha=mu`.  Repeated equal parts do not create new distinct orders.  Thus the
coefficient of `q^w(mu)` is one, its source is `L(mu)`, and a target occurs in
the bounded image exactly when `w(mu)<=N`.  At `N=1`, (2.6) gives
`Phi_(1)(q)=q/(1-q)`, so the sole bounded source is `(1)`.

## 3. Reproducible mathematical audit

The original scout verifier was rerun unchanged and passed **3,935,761**
assertions with payload SHA-256
`3f8b945d6618657798756049cf96651a758180571a00a51abab7c93524ff3494`.

The hostile verifier `verify_mpd_hostile.py` is standalone, imports no scout
code, uses decreasing rather than increasing notation, and checks:

- all 313,064 partitions of weights 1 through 42;
- both exact-weight and capped heights, all exact-depth containment witnesses,
  and exact versus at-least minima through depth 7;
- `D after L`, one-step and iterated Ferrers containment, the tail-sum
  conjugate identity, and the unique recurrent state;
- 14,688 comparable pairs for lift monotonicity;
- all 28,628 sources through weight 30 against 683 target series through
  target weight 15, including 547 repeated-part targets;
- 66 direct monomial-symmetric specializations by a separate index-subset
  enumeration; and
- the singleton carrier and singleton fibre independently.

It passes **7,156,962** exact assertions.  Two cold executions are
byte-identical, each with transcript SHA-256
`f81645ab0699b64629ed6358a9ab60d78e1ba4a60de224c8aae6ed656c90df41`.
The verifier SHA-256 is
`7b6916b15dc019581c2ec73910e71bcc0715b1690b07b5c442e79826abe79f82`;
its canonical payload SHA-256 is
`cb9f3e83ff257b9cd81d07d887b26195177f546c63b7106953dde57e92f77ba1`.
The frozen transcript is `hostile_verification_output.txt`.

This establishes mathematical correctness after (2.5).  It is not evidence
of novelty or ownership clearance.

## 4. Primary-source owner audit

### 4.1 Direct literal and temporal owners

1. [OEIS A225485](https://oeis.org/A225485), entered by Clark Kimberling on
   2013-05-08, defines `F(S)` as the multiset of frequencies of the distinct
   elements, iterates `F`, names frequency depth, and tabulates partitions by
   that depth.  Its partition comment gives the literal orbit
   `(32211)->(221)->(21)->(11)->(2)->(1)`.  This is the candidate's `D`
   iteration, apart from the already-singleton convention.
2. [OEIS A225486](https://oeis.org/A225486), also entered by Kimberling on
   2013-05-08, is explicitly “Maximal frequency depth for the partitions of
   n.”  Its values begin `0,2,3,4,4,4,5,...`, exactly the candidate's
   exact-weight (and hence capped) height from weight one onward.  The record
   states that its run lengths are A325258, the first differences of Levine's
   sequence A011784.
3. [OEIS A325280](https://oeis.org/A325280) tabulates the number of integer
   partitions of `n` by adjusted frequency depth, while
   [A325282](https://oeis.org/A325282) gives the maximum adjusted depth and
   isolates its difference from A225486 at the singleton boundary.
   [A325258](https://oeis.org/A325258) states directly that the lengths of
   the maximum-depth plateaux are first differences of Levine's sequence.
   [A325254](https://oeis.org/A325254) and
   [A325283](https://oeis.org/A325283) additionally enumerate and list the
   partitions attaining maximum adjusted depth.  These are database records,
   not peer-reviewed proofs, but they are direct public ownership of the
   literal question, data, extrema, and Levine linkage.  The gate does not
   permit re-presenting those objects as a fresh temporal axis merely by
   supplying a new proof.
4. Claes and Miyamoto,
   [*Golombic and Levine sequences*](https://arxiv.org/abs/2602.10992v2),
   arXiv:2602.10992v2 (2026), Section 1, define the Levine operator exactly as
   the proposed `L`, display its iterates from `(2)`, state
   `L(a)=(tail-sum(a))^*`, and state
   `|L(a)|=sum_i i a_i`.  Their Levine-number convention records the lengths
   of the iterates, so the proposed threshold sizes are its one-step shift.
   This 2026 primary source removes any possible claim that the lift, its
   canonical orbit, or its weighted-size mechanism is an unowned construction.

Together, items 1--4 own the forward map, depth statistic and census, maximum
height sequence, Levine plateau relation, canonical inverse orbit, and the
size mechanism driving its thresholds.  They trigger the frozen direct-owner
kill rule.

### 4.2 Older Levine and multiplicity-description sources

- Sloane,
  [*My Favorite Integer Sequences*](https://arxiv.org/abs/math/0207175),
  published in the SETA '98 proceedings (1999), Section 8, records Lionel
  Levine's reversed multiplicity-row construction, the sequence
  `1,2,2,3,4,7,14,42,...`, the row length/sum/last-entry identities, and a
  proof sketch for `log L_n ~ c phi^n`.  Sloane attributes the asymptotic to
  Bjorn Poonen and Eric Rains as a 1997 personal communication; this audit did
  not locate a separate Poonen--Rains paper and does not fabricate one.
- Eliahou and Erickson,
  [*Mutually describing multisets and integer partitions*](https://doi.org/10.1016/j.disc.2012.11.014),
  *Discrete Mathematics* 313(4) (2013), 422--433, is a close primary
  multiplicity-dynamics owner.  The publisher abstract defines
  `d(A)` by **adjoining the support** of `A` to its multiplicities and says
  that the paper introduces a related fixed-`n` partition system.  That
  abstract-level map is not the discard-support map `D`.  The full text could
  not be retrieved reproducibly: the ScienceDirect PDF endpoint returned an
  access challenge and the public metadata/API route exposed only the
  abstract.  Accordingly this audit assigns it strong neighbourhood credit
  but does **not** claim that its inaccessible partition map owns the residual
  formula.  The kill above does not depend on that unresolved reading.
- Dougherty and McCammond,
  [*Geometric Combinatorics of Polynomials II*](https://arxiv.org/abs/2410.03047),
  use the static map from a multiset to the integer partition consisting of
  its multiplicities.  This confirms that the one-step shape map is standard
  cross-domain infrastructure; it receives zero credit and is not needed for
  the temporal kill.

The bounded searches did not locate the exact source-size fibre series (2.6)
as a named theorem.  That non-hit has zero positive evidentiary weight.

## 5. Internal collision audit

| Internal item | Literal comparison | Proof/theorem silhouette | Disposition |
|---|---|---|---|
| P113, principal-hook partition dynamics | Same Ferrers carrier vocabulary, but P113 preserves a fixed weight and regroups diagonal hooks; MPD discards part values and changes total. | Both package a sharp partition depth with target fibres.  P113's gap clock and Frobenius fibre are not transferable to MPD. | No literal collision; substantial portfolio subtraction. |
| P126, balanced composition refinement | Ordered compositions; synchronously split every part into balanced halves. | Canonical iterate kernels, image decoder, and every-target product fibres already occupy the refinement/decoder silhouette. | No literal collision; no rescue for MPD. |
| P137, rank-feedback p-group splitting | Fixed-order abelian `p`-group types; recomputed-rank split map. | Fixed/recurrent census, sharp partition-type clock, and every-target inverse already form the same high-level package. | No literal collision; different algebraic engine. |
| P147, adjacent-run consolidation | Ordered compositions; merge equal adjacent runs and preserve total. | Sharp depth plus complete target-resolved fibres is already occupied on a neighbouring composition carrier. | No literal collision; distinct run engine. |

More decisively, the internal intake ledgers had already made this mechanism a
permanent exclusion:

- `docs/papers122_126_sequence/STAGE1_LITERATURE_LANDSCAPE.md` says that
  frequency/inventory partition dynamics were removed after direct multiset
  and inventory owners were identified;
- the corresponding P122--P126 kill ledger lists multiplicity/inventory
  partitions among direct/mechanical intake kills;
- `docs/papers132_136_sequence/STAGE1_LITERATURE_LANDSCAPE.md` assigns
  iterated multiplicity descriptions zero-credit context; and
- `docs/papers147_151_sequence/phase1/OWNER_AUDIT_EQC.md` kills a neighbouring
  equal-cardinality coarsening because its temporal shape factors through a
  multiplicity-driven partition map with unresolved Eliahou--Erickson risk.

The current OEIS and 2026 Claes--Miyamoto hits resolve the present candidate
more strongly than those earlier cautious ledgers did.  Promoting MPD would
violate the corpus's own permanent-kill rule.

## 6. Claim subtraction and final decision

| Candidate component | Post-audit credit |
|---|---|
| Literal `D`, convergence, frequency depth | **Zero:** A225485 and its refinements own the exact programme. |
| Depth distribution and maximum by weight | **Zero:** A225485/A225486/A325280/A325282. |
| Levine thresholds and plateau relation | **Zero:** A225486/A325258/A011784 and Sloane. |
| Canonical lift `L`, its orbit, tail-sum conjugate form, weighted size | **Zero:** Claes--Miyamoto 2026, with older Levine construction in Sloane. |
| Ferrers containment and uniqueness proof | Correct proof presentation, but it sharpens an already directly recorded extremal programme; insufficient as an independent paper axis. |
| Every-target source-size fibre series and `w(mu)` image test | Correct residual axis; generic monomial-symmetric specialization is zero-credit background.  No exact owner located in a bounded search, which is not novelty evidence. |
| `N=1` | Requires the explicit repair (2.5); no contribution credit. |

**Final verdict:** `RED / KILL_DIRECT_TEMPORAL_OWNER`.

The correct fibre identity may be retained as a lemma bank for a genuinely
different future system, but MPD itself must not be promoted, renamed, or
re-entered by adding the containment proof.  No `papers/170-*` directory is
created from this candidate.
