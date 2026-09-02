# Algebraic/arithmetic/permutation Stage-1 scout — P152--P156 intake

**External status:** `HOLD_EXTERNAL`.  
**Paper numbering:** deliberately unassigned.  
**Research role:** breadth-first counterexample and owner-risk screen, not a
paper, proof by computation, novelty claim, or release recommendation.

## Outcome first

Fourteen genuinely different literal finite systems were defined and
enumerated.  The deterministic audit exercised **137,719 state-box
incidences** and **254,034 exact assertions**.  One candidate has a coherent
owner-thin residual theorem contract after a direct family hit.  A second
mathematically clean candidate is
retained only to document why direct ownership defeats attractive data; it is
not a second survivor and must not fill a quota.

| rank | handle | literal carrier and update | independent signal | owner/internal risk | verdict |
|---:|---|---|---|---|---|
| 1 | `QTS` | `E=F_{q^2}`, `x -> Tr(x)^2 inv0(x)` for odd `q` | trace-kernel star; complement conjugate to a norm-indexed radial--Frobenius permutation; full cycles and `q/1/0` fibres | Hou directly owns the containing trinomial family; only the full nonpermutation graph conjunction is eligible | **`SELECT_INTERNAL_OWNER_THIN_PENDING`** |
| 2 | `PDG` | monic `deg<=N` polynomials, `f -> gcd(f,f')`, `char>N` | sharp maximum-multiplicity clock and every-target squarefree inverse product | Yun/Musser square-free decomposition directly owns multiplicity decrement | **`RESERVE_OWNER_COMPRESSED`** |
| 3 | `MBI` | `p Z/p^e Z`, `x -> x/(1+x)` | all periods `p^max(0,e-2v_p(x))` | literal unipotent Möbius action; generic group-orbit kill | `KILL_DIRECT_OWNER` |
| 4 | `MCH` | `M_2(F_p)`, `A -> A^2-tr(A)A` | Cayley--Hamilton scalar collapse plus exact determinant fibres | immediate scalar power map; P102/P103 neighbourhood | `KILL_INTERNAL_REDUCTION` |
| 5 | `TQI` | `F_{p^2}`, `x -> Tr(x)inv0(x)` | trace--norm image curve, involutive recurrent core, complete fibres | same trace-normalization root as `QTS`; theorem shallow | `KILL_SAME_ROOT` |
| 6 | `NTF` | `F_{p^2}`, `x -> x^p/Tr(x)` with trace-zero sent to zero | trace-one affine image and conjugation core | same root as `QTS/TQI`; projective normalization | `KILL_SAME_ROOT` |
| 7 | `DDE` | divisors `p^a|p^e`, `p^a -> p^max(0,2a-e)` | exact dyadic deficit clock | literal exponent-tent neighbour of P142 | `KILL_INTERNAL_COLLISION` |
| 8 | `RDF` | `{1,...,B}`, `n -> n/rad(n)` | absorption time is largest prime multiplicity | direct factor-multiplicity peeling; inverse cutoff irregular | `KILL_OWNER_THIN` |
| 9 | `EGD` | squarefree divisors, `d -> gcd(d,phi(d))` | Pratt-chain peeling gives binomial depth layers | support-DAG mechanism transfers from P133 | `KILL_INTERNAL_COLLISION` |
| 10 | `FPD` | permutations of size at most `N`; delete fixed points and standardize | apparent recursive deletion collapses in one step | idempotent derangement reduction | `KILL_THEOREM_THIN` |
| 11 | `DSP` | `S_n`, `pi -> pi^(1+des(pi))` | nontrivial small tails and cycles | permanent state-dependent group-power exclusion | `KILL_HARD_EXCLUSION` |
| 12 | `CRH` | binary linear codes, `C -> C intersect C^perp` | exact hull image | idempotent lattice closure | `KILL_HARD_EXCLUSION` |
| 13 | `DUA` | dual numbers `F_p[eps]/(eps^2)`, `z -> z^p-z` | rank-one image with sign-involution core | generic Artin--Schreier linear operator; P109/P115 | `KILL_OWNER_LINEAR` |
| 14 | `QRM` | `F_p`, `x -> 1-inv0(x)` | explicit `2/3`-cycle census | projective Möbius order three with one point spliced out | `KILL_DIRECT_OWNER_THIN` |

`QTS_FREEZE_CONTRACT.md` gives the freeze-level theorem and collision
contract.  `OWNER_SEARCH_LOG.md` records the actual queries, primary sources,
and bounded-non-hit boundary.

## Exact computational contract

The standard-library verifier is `verify_algebraic_scout.py`; its exact stdout
is frozen in `CANONICAL.txt`.  It builds literal carriers, checks closure and
functional graphs, and independently compares them with the proposed
formulae.  Enumeration is counterexample pressure only.

| handles | boxes | state-box incidences | assertions | principal checks |
|---|---:|---:|---:|---|
| `QTS` | 13 | 8,253 | 33,291 | every state/target, skew coordinates, pointwise period, fixed iterates through `2(p-1)` |
| `PDG` | 6 | 12,034 | 72,204 | literal polynomial gcd/derivative, factor multiplicities, depths, image and every fibre |
| `TQI+NTF` | 20 | 6,708 | 60 | image sizes, temporal layers, fibre multisets, recurrent involutions |
| `MBI` | 15 | 23,875 | 23,890 | every pointwise period over 15 local rings |
| `DDE` | 79 | 3,318 | 3,318 | every exponent clock for `2<=e<=80` |
| `RDF+EGD` | 2 | 5,016 | 5,002 | 5,000 integer clocks and Pratt-chain profile |
| `FPD+DSP` | 13 | 52,145 | 98,378 | 46,233 idempotence/derangement pairs and 5,912 group-power closure checks |
| `MCH` | 4 | 17,748 | 17,748 | every target's determinant fibre |
| `CRH` | 4 | 90 | 90 | every binary code hull through length four |
| `DUA+QRM` | 26 | 8,532 | 52 | exact temporal/fibre silhouettes over thirteen primes |
| meta registry | -- | -- | 1 | exactly fourteen distinct handles |
| **total** | **182** | **137,719** | **254,034** | **PASS** |

The verifier deliberately represents `F_{p^2}` as
`F_p[s]/(s^2-d)` for a literal nonsquare `d`; the theorem is not constructed
from its predicted orbit graph.  The PDG lane enumerates coefficient tuples,
computes formal derivatives and Euclidean gcds, and factors independently.

## 1. `QTS` — quadratic trace-square reciprocal

### Early anomaly

For every odd prime power `q`, let `E=F_{q^2}` and

```text
F(x)=Tr(x)^2 inv0(x).
```

Despite the reciprocal notation, this is the global polynomial function

```text
F(x)=x+2x^q+x^(2q-1).
```

It has exactly one transient feature: the `q-1` nonzero elements of the
trace-zero line feed zero in one step.  Every nonzero-trace point is recurrent.
The useful anomaly is what happens after trace normalization.  The bijection

```text
x <-> (a,u)=(Tr(x),x/Tr(x)) in F_q^* x {Tr(u)=1}
```

conjugates the complement dynamics to

```text
(a,u) -> (a/N(u),u^q).
```

Thus a nonlinear-looking field polynomial becomes a norm-indexed radial
rotation coupled to the order-two Frobenius conjugation, without losing any
point information.

### Freeze-level theorem profile

The candidate contract proves or proposes, for all odd prime powers:

1. the coordinate bijection and iterate
   `(a,u)->(a N(u)^(-t),u^(q^t))`;
2. recurrent count `q^2-q+1`, temporal polynomial
   `q^2-q+1+(q-1)z`, and the complete star at zero;
3. every-target fibre sizes `q` at zero, zero at nonzero trace-zero targets,
   and one at every nonzero-trace target;
4. the trace-one norm multiset: `1/4` once, and every
   `c` with nonsquare `1-4c` twice;
5. pointwise periods `ord(4)` on the base-field ray and
   `lcm(2,ord(N(u)))` on every other trace-one ray;
6. a fixed-iterate formula, direct cycle census, and finite zeta product.

All formulas and proofs are written explicitly in `QTS_FREEZE_CONTRACT.md`.
Prime-field exact tests saw maximum periods `2,4,6,10,...,42` for
`p=3,5,7,11,...,43`, while the claimed formula, rather than that empirical
sequence, is the contract.

### Owner and internal collision boundary

Rewriting QTS as `x(1+x^(q-1))^2` produced a direct owner hit: Hou's
2014/2015 work completely classifies the permutation members of the containing
family `a x+b x^q+x^(2q-1)`.  QTS is its `(a,b)=(1,2)` member.  Polynomial
construction, the `x h(x^(q-1))` reduction, and permutation status therefore
receive zero credit.  The bounded search did not locate the **complete
iterative graph conjunction**; that narrower non-hit is not novelty evidence.
Adjacent primary literature on rational functions and trace-based many-to-one
diagrams is also subtracted.

The internal firewall compares P102, P125, and P150.  The closest visual
collision is P150 because both have `q^2` states and `q/1/0` fibres.  QTS is,
however, polynomial without an essential totalization and has a single linear
kernel star plus a bijective complement; P150 has denominator-created
singular strata, a depth-three tree, and the Lyness period-five locus.  Status:
`SELECT_INTERNAL_OWNER_THIN_PENDING`.

## 2. `PDG` — derivative-gcd multiplicity peeling

### Literal system and exact theorem

Let `K` be a finite field of characteristic greater than `N`, and let `X_N`
be all monic polynomials of degree at most `N`, including `1`.  Define

```text
G(f)=gcd(f,f').
```

If `f=product_P P^(m_P)`, then

```text
G^t(f)=product_P P^max(m_P-t,0),
tau(f)=max_P m_P.                                           (16)
```

The sharp global depth is `N`; exactly `|K|` states `(x-a)^N` attain it.  If
`g=product P^r_P`, all one-step sources are uniquely

```text
f=g rad(g) h,
```

where `h` is squarefree and coprime to `g`.  Therefore `g` is in the bounded
image exactly when

```text
deg(g)+deg(rad(g))<=N,                                      (17)
```

and the degree-refined fibre generating function is

```text
z^(deg(g)+deg(rad(g))) product_{P not dividing g}(1+z^deg(P)),   (18)
```

truncated through degree `N`.  Likewise the number of states absorbed by time
`t` in each degree is generated by

```text
product_P (1+z^deg(P)+...+z^(t deg(P))).                    (19)
```

The verifier checks (16)--(18) literally in six boxes.  At `(p,N)=(7,4)`, for
example, the 2,801 states have depths
`{0:1,1:2401,2:343,3:49,4:7}` and 64 image points.

### Why it is not a survivor

Yun's 1976 square-free decomposition work, including revamped Musser
algorithms, directly owns the derivative-gcd multiplicity mechanism.  The
bounded-carrier temporal polynomial and inverse product are clean consequences
but do not supply an independent forward engine after owner subtraction.
Verdict: `RESERVE_OWNER_COMPRESSED`, never a quota filler.

## 3. Trace-family negative controls

### `TQI`

Define `T(x)=Tr(x)inv0(x)` on `F_{p^2}`.  The image is

```text
{0} union {y!=0:Tr(y)=N(y)}.
```

Zero has `p` sources; each nonzero image point has `p-1`; all other targets
are empty.  On its image the map is Frobenius conjugation, so the recurrent
count is `p+1`, all other states have tail one, and periods are at most two.
This is a useful control confirming the normalization algebra, but it is
strictly shallower and shares QTS's root.

### `NTF`

Define `R(x)=x^p/Tr(x)` for nonzero trace and send the trace-zero line to zero.
Its image is `{0} union {u:Tr(u)=1}`; nonzero image fibres have size `p-1`,
and the recurrent action is again conjugation.  It is a projective
normalization sibling of TQI/QTS, not a separate paper direction.

## 4. Independent arithmetic and algebraic controls

### `MBI` — local Möbius ideal

On `p Z/p^e Z`, set `M(x)=x/(1+x)`.  Since `1+x` is always a unit,

```text
M^t(x)=x/(1+tx),
per(x)=p^max(0,e-2v_p(x))                                  (20)
```

for nonzero `x`, with zero fixed.  Fifteen complete rings confirmed (20),
including maximum period 2,401 at `(p,e)=(7,6)`.  The formula is strong but
is literally one unipotent Möbius matrix being powered.  This meets the
permanent generic group-action exclusion.

### `DDE` — divisor deficit doubling

On divisors `p^a|p^e`, use

```text
p^a -> p^max(0,2a-e).
```

The endpoints `1,p^e` are fixed; for `0<a<e`, the exact tail to `1` is

```text
ceil(log_2(e/(e-a))).                                      (21)
```

This is a clean dyadic deficit law, but it is the same prime-exponent tent
engine already occupied by P142.

### `RDF` — radical descent

On `{1,...,B}`, define `R(n)=n/rad(n)`.  If
`n=product p^e_p`, the depth is `max e_p`.  Exhaustion through `B=5000` gave
maximum depth 12 at 4,096.  This is simultaneous multiplicity decrement with
no independent inverse theorem under the hard size cutoff.

### `EGD` — Euler gcd descent

On squarefree divisors, define `E(d)=gcd(d,phi(d))`.  Prime support survives
according to divisibility edges `p|(r-1)`.  For the chain
`2,3,7,43`, the exact tail layers are `1,4,6,4,1`.  This is precisely Pratt-DAG
support peeling, so P133's proof engine transfers.

### `MCH` — Cayley--Hamilton collapse

For `A in M_2(F_p)`, set

```text
C(A)=A^2-tr(A)A=-det(A)I.
```

Every nonscalar target has empty fibre.  A nonzero scalar target has
`p(p^2-1)` sources, and the zero target has the number of singular matrices.
After the first step, the scalar update is `s->-s^2`.  Thus both the temporal
and inverse axes collapse to classical Cayley--Hamilton/determinant and a
generic power map; P103 is the nearest internal owner.

### `CRH` — code hull closure

For a binary linear code, `H(C)=C intersect C^perp`.  The image is
self-orthogonal, hence `H^2=H`.  Exact enumeration found `1,2,4,11` distinct
images for lengths `1,2,3,4`.  The one-step fibre question is a static code
hull problem; the dynamics is an idempotent lattice closure.

### `DUA` — dual-number Artin--Schreier map

On `F_p[eps]/(eps^2)`, for odd `p`,

```text
(a+b eps)^p-(a+b eps)=-b eps.
```

The nilpotent line is recurrent under sign reversal and every other point has
tail one.  This is a rank-one linear image theorem and lies in the
P109/P115 Artin--Schreier/Frobenius neighbourhood.

## 5. Permutation and projective controls

### `FPD` — delete fixed points

Delete all fixed positions and their equal values from a permutation, then
standardize.  Equality of positions and values is preserved by the same
order-preserving relabelling, so no new fixed point can appear.  All 46,233
permutations through `S_8` confirmed the resulting idempotence.  The apparent
iteration is only the ordinary derangement reduction.

### `DSP` — descent-powered permutation

Set `P(pi)=pi^(1+des(pi))`.  Exact graphs through `S_7` have maximum tails
`1,1,3,3,4,5` and maximum periods `1,2,2,4,4,6`.  These signals do not overcome
the explicit permanent kill on state-dependent symmetric-group powers: the
only general proof route is cycle-partition arithmetic.

### `QRM` — totalized order-three Möbius map

On `F_p`, set `Q(x)=1-inv0(x)`.  The points zero and one form a two-cycle;
all remaining nonfixed points lie on three-cycles inherited from the
projective Möbius transformation, while fixed points solve
`x^2-x+1=0`.  This is a bijection, but the theorem is the classical
projective order-three action with its infinity point spliced out.

## Recommendation to root

Advance only QTS's **owner-thin residual graph conjunction** to an independent
owner audit and hostile theorem review.  Do not credit discovery of its
trinomial or its nonpermutation status.  The conjunction is precise enough to
test, but Hou's direct family ownership and the active trace/rational
neighbourhood make rejection a live outcome; a graph-level hit is fatal.  Keep
`PDG` solely as an owner-compressed mathematical control.  Kill the other
twelve systems now; changing parameters or notation will not repair their
literal/internal reductions.

No paper number, authorship, posting, contact, submission, or public claim is
authorized.  Everything in this lane remains `HOLD_EXTERNAL`.
