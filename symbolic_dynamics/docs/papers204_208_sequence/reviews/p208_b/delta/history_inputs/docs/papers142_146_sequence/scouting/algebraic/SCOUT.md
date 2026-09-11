# Algebraic/arithmetic breadth scout for the P142--P146 intake

**Status:** `SCOUT_ONLY / NO_PAPER_NUMBER / NO_GIT / HOLD_EXTERNAL`
**Owner-search date:** 2026-09-01 UTC
**Mechanical status:** **PASS; 10 literal systems; 344,658 exact assertions**

## 1. Outcome first

This lane fixed and executed ten literal finite self-maps on ten genuinely
different algebraic or arithmetic carriers.  A parameter box is never counted
as another system.  The only finalist is `VGT`; `DNT` is a replacement reserve
whose main structural inputs are owner-heavy.  The other eight systems are
permanently killed, including the superficially attractive numerical-semigroup
and projective-Cremona controls.

| rank | handle | early theorem signal | honest disposition |
|---:|---|---|---|
| 1 | `VGT` | On the divisors of an odd prime power, the literal gcd update becomes the integer map `a -> min(2a,e-a)`.  It has a complete fixed/two-cycle band, a pointwise entry-time formula, a unique sharp deepest divisor, all fixed-iterate counts, an exact temporal polynomial, an interval image, and every-target fibres. | **FINALIST / INTERNAL CONTRACT.**  No literal owner was located in the bounded search.  General piecewise-linear and discretized-tent dynamics are zero credit, and the arithmetic lift may still be killed as cosmetic. |
| 2 | `DNT` | Normalizer iteration on every subgroup of a dihedral `2`-group is a binary inverse tree: the dihedral step parameter halves, giving a sharp clock, exact depth polynomial, image, and all fibres. | **RESERVE / OWNER COMPRESSED.**  Dihedral subgroup classification and normalizer towers are classical.  Retain only if the global batch needs a replacement and a stronger residual survives specialist subtraction. |
| 3 | `PCR` | The projective quadratic Cremona map has a complete torus involution, boundary depth-two law, and exact fibres. | **PERMANENT KILL.**  It is classical Cremona inversion and a diagonal/projective adjugation restriction too close to P103. |

No bounded search miss below is evidence of novelty, priority, or freedom to
operate.  No public posting, submission, specialist contact, authorship,
priority language, or release is authorized.

## 2. Intake firewall and counting

The comparison set included the P1--P141 paper-directory names, the P137--P141
problem anchor and permanent kill ledger, the P137--P141 collision firewall,
and the consolidated
[`HISTORICAL_OCCUPANCY.md`](../../phase1/HISTORICAL_OCCUPANCY.md).  In
particular, this lane did **not** re-enter any of the following:

- p-group rank-feedback splitting or another finite-abelian-group functor;
- state-dependent group powers, Jordan powers, or ordinary finite-linear
  functional graphs as a claimed advance;
- derived-centralizer orbit partitions or a centralizer-partition variant;
- the finite-group Thue--Morse product-exchange map;
- Euclidean quotient queues, continued-fraction recodings, or subtractive
  Euclid under another schedule; or
- partition split/join, relation cubing, ideal closure, or a comparator under a
  renamed carrier.

An assertion is one deterministic Boolean equality or membership check in
`verify_algebraic_scout.py`.  Literal integer gcds, finite group multiplication
and conjugation, finite-field arithmetic, exact subspace enumeration, and exact
finite-carrier enumeration are used throughout.  No floating point, random
sampling, symbolic package, or external CAS appears.

| handle | carrier | exact boxes / states visited | assertions |
|---|---|---:|---:|
| `VGT` | divisors of odd prime powers | 508 / 33,528 | 266,209 |
| `DNT` | all subgroups of dihedral `2`-groups | 8 / 1,056 | 7,448 |
| `PCR` | finite projective planes plus a sink | 13 / 8,558 | 34,297 |
| `FAI` | embedded subalgebras of truncated polynomial algebras | 18 / 62 | 294 |
| `BCH` | binary linear codes | 5 / 464 | 3,258 |
| `QCI` | primitive reduced binary quadratic forms | 100 / 488 | 2,640 |
| `LPS` | labelled Latin squares | 3 / 590 | 2,956 |
| `RCC` | primitive cyclotomic divisors over finite fields | 13 / 100 | 513 |
| `CHE` | prime finite fields | 45 / 4,225 | 16,855 |
| `NSB` | bounded numerical semigroups | 5 / 1,453 | 10,186 |
| **per-system subtotal** | **10 different carriers** | **718 boxes / 50,524 states** | **344,656** |
| global breadth/uniqueness sentinels | -- | -- | 2 |
| **total** | -- | -- | **344,658** |

The canonical replay is:

```bash
python docs/papers142_146_sequence/scouting/algebraic/verify_algebraic_scout.py
cmp docs/papers142_146_sequence/scouting/algebraic/CANONICAL.txt \
  <(python docs/papers142_146_sequence/scouting/algebraic/verify_algebraic_scout.py)
```

Enumeration is a falsifier.  The all-parameter statements in Sections 4 and 5
are proof contracts, not inductions from the finite boxes.

## 3. Literal catalogue and permanent disposition

| handle | literal finite system | bounded signal | disposition and controlling reason |
|---|---|---|---|
| `VGT` | Fix an odd prime `p` and `e>=2`.  On `d|p^e`, set `F(d)=gcd(p^e,d^2+p^e/d)`. | Exhausted four primes and every `2<=e<=128`; checked the literal gcd, complete functional graph, eight fixed iterates, temporal polynomial, all fibres, and the sharp witness. | **FINALIST.**  Strong residual, no internal literal collision found, but arithmetic-lift and owner risks remain explicit. |
| `DNT` | On all subgroups of `D_(2^(m+1))`, set `H -> N_G(H)`. | All subgroups through `m=8` were built as element sets; every normalizer was recomputed by literal conjugation.  Sharp depth `m`, exact image and fibres. | **RESERVE.**  The normalizer-halving proof is clean but owner-compressed. |
| `PCR` | On `P^2(F_p)` plus a sink, apply `[x:y:z] -> [yz:zx:xy]`, sending base points to the sink. | Torus plus sink recurrent; four torus fixed points; boundary depths `1,2`; all target fibres exact. | **KILL INTERNAL/CLASSICAL.**  Standard quadratic Cremona involution; on diagonal matrices it is projective adjugation, too close to P103's occupied adjugate lane. |
| `FAI` | In `F_p[x,y]/(x^r,y^s)`, replace an embedded subalgebra by its Frobenius image. | Unique constant subalgebra; sharp chain length `ceil(log_p max(r,s))`. | **KILL OWNER/THIN.**  Generic Frobenius-image filtration with only one chain and no inverse theorem. |
| `BCH` | On binary linear codes `C<=F_2^n`, set `C -> C+C^perp`. | Exhausted every code through `n=5`; the image is dual-containing and the map is idempotent. | **KILL STATIC RETRACTION.**  `C+C^perp=(C intersect C^perp)^perp`; the historical one-step-retraction exclusion applies. |
| `QCI` | On the symmetric carrier of primitive reduced positive binary quadratic forms, set `(a,b,c)->(a,-b,c)`. | Complete fixed/two-cycle census for all valid discriminants through absolute value `200`. | **KILL DIRECT INVOLUTION.**  This is classical form/class conjugation and has no transient spine. |
| `LPS` | On labelled Latin squares, exchange the right input and output, i.e. take the right-division parastrophe. | Exhausted all `2+12+576` labelled squares of orders `2,3,4`; exact fixed/two-cycle counts. | **KILL DIRECT PARASTROPHE.**  A coordinate permutation of a quasigroup law. |
| `RCC` | On squarefree divisors of `Phi_N` over `F_q`, set `f -> Phi_N/f^*`; on cyclotomic-factor supports this is reciprocal-complement. | Fixed points exist exactly when the reciprocal factor permutation has no fixed orbit; otherwise all states pair. | **KILL DIRECT DUALITY.**  Explicit Boolean involution; unlike P128, it has no erosion or clock. |
| `CHE` | On `F_p`, set `x -> x^2-2`. | Exact functional graphs for every odd prime through `199`; checked `u+u^-1` semiconjugacy to squaring. | **KILL DIRECT OWNER.**  Chebyshev finite-field dynamics is mature, and the powering semiconjugacy is the standard proof engine. |
| `NSB` | On numerical semigroups with gaps in `[1,B]`, adjoin the Frobenius number. | Pointwise depth equals genus; the ordinary semigroup is the unique depth-`B` state; every fibre is an effective-generator inverse. | **KILL DIRECT OWNER.**  This is precisely the standard numerical-semigroup tree orientation, so its attractive clock and inverse rule are definition-level owner material. |

The negative rows are permanent evidence.  A changed prime, dimension, field,
boundary convention, or orientation does not revive them.

## 4. Finalist contract: `VGT` prime-power divisor gcd dynamics

### 4.1 Literal map and valuation conjugacy

Fix an odd prime `p` and an integer `e>=2`.  Let

```text
X_(p,e) = {p^a : 0<=a<=e},
F_(p,e)(d) = gcd(p^e, d^2 + p^e/d).
```

Write `d=p^a`.  The frozen first lemma is the **literal** identity

```text
F_(p,e)(p^a) = p^T_e(a),
T_e(a) = min(2a,e-a).                                      (4.1)
```

Indeed, factor the sum by its smaller `p`-power.  If `3a!=e`, the
remaining factor is `1+p^k`, a `p`-adic unit.  If `3a=e`, the remaining
factor is `2`, still a unit because `p` is odd.  This is exactly why the
contract excludes `p=2`: for `e=3a`, the binary valuation is `2a+1`, not
`2a`.  The verifier checks sixteen such characteristic-two failures,
including the smallest witness `(p,e,a)=(2,3,1)`.

Put

```text
L = ceil(e/3),     U = floor(2e/3),
R = U-L+2,         A = 1 + [2 divides e].                   (4.2)
```

### 4.2 Complete recurrence and fixed iterates

The recurrent exponent set is exactly

```text
{0} union {L,L+1,...,U}.                                   (4.3)
```

Zero is fixed.  On `[L,U]`, `T_e(a)=e-a`; hence `e/2` is the only other
fixed exponent when `e` is even, and every remaining recurrent exponent is
in a strict complement two-cycle.  Thus there are `R` recurrent states,
`A` fixed states, and `(R-A)/2` strict two-cycles.  For every integer `k>=1`,

```text
Fix(T_e^k) = A,     k odd,
             R,     k even.                                (4.4)
```

Equivalently, after all classical finite-map bookkeeping is credited, the
formal Artin--Mazur zeta control is

```text
zeta_e(z) = (1-z)^(-A) (1-z^2)^(-(R-A)/2).                 (4.5)
```

### 4.3 Pointwise entry time and unique sharp clock

Let `tau_e(a)` be the least time at which `T_e^t(a)` is recurrent.  With
`ceil(log_2 x)` understood as the least integer `j` such that `2^j>=x`, the
complete pointwise law is

```text
tau_e(a) = 0,                                      a=0 or L<=a<=U;
           ceil(log_2(L/a)),                       1<=a<L;
           1,                                      a=e;
           1+ceil(log_2(L/(e-a))),                 U<a<e.   (4.6)
```

For `a<L`, every step doubles `a` until the first entry into `[L,U]`; the
last doubling cannot overshoot `U`.  For `a>U`, the first step reflects to
`e-a<L`, after which the same doubling argument applies.

Let `m=ceil(log_2 L)`.  The maximum tail is

```text
M_e = 1+m.                                                   (4.7)
```

For `e>=4`, the **unique** deepest exponent is `a=e-1`, so the unique sharp
divisor is `p^(e-1)`.  For `e=2,3`, the maximum is one and the unique deepest
exponent is `a=e`.  Uniqueness for `e>=4` follows because the reflected
positive distance `b=e-a` has maximal doubling time only at `b=1`, while the
unreflected lower branch is shorter by one step.

### 4.4 Exact temporal polynomial

For `1<=j<=m`, define

```text
c_j = ceil(L/2^(j-1)) - ceil(L/2^j).                        (4.8)
```

The `c_j` lower-branch exponents have depth `j`; their reflected partners
have depth `j+1`; and `a=e` contributes the remaining depth-one state.
Therefore the complete depth generating polynomial is

```text
D_e(z) = sum_(a=0)^e z^tau_e(a)
       = R + z + (1+z) sum_(j=1)^m c_j z^j.                 (4.9)
```

At `e=128`, for example, the exact coefficients are

```text
D_128(z)=44+22z+32z^2+16z^3+8z^4+4z^5+2z^6+z^7,
```

with the unique depth-seven exponent `127`.

### 4.5 Image and every-target fibres

The exponent image is the full interval

```text
im(T_e) = {0,1,...,U},       |im(T_e)|=U+1.                 (4.10)
```

For every target exponent `b`, including targets outside the image,

```text
T_e^(-1)(b) = {e-b} union ({b/2} if b is even),   0<=b<=U,
                empty,                            U<b<=e,   (4.11)
```

where the displayed union is a set: its two candidates coincide precisely
when `3b=2e`.  Hence every fibre has size `0`, `1`, or `2`; the maximum fibre
is exactly two.  Formula (4.11) is checked target by target in all 508 boxes.

### 4.6 Proof routes, controls, and zero-credit boundary

The intended proof has three short, separately falsifiable spines.

1. **Valuation spine:** factor `p^(2a)+p^(e-a)` and use oddness of `p` to
   prove (4.1), with the binary equal-valuation case as a sharp negative
   control.
2. **Band/doubling spine:** isolate `[L,U]`, prove complement pairing there,
   and prove the two lower-branch entry laws in (4.6).  This yields recurrence,
   fixed iterates, the unique clock witness, and (4.9).
3. **Inverse-branch spine:** solve `2a=b` and `e-a=b` under their branch
   inequalities.  This proves the full interval image and (4.11) without
   summing a functional graph.

General valuation identities, piecewise-monotone interval-map theory,
finite-grid tent maps, functional-graph/zeta bookkeeping, and ceiling-log
algebra receive **zero contribution credit**.  In particular, the real map
`x -> min(2x,1-x)` already exposes the band/doubling silhouette; the possible
residual is only the conjunction of the literal divisor-gcd system with its
complete finite arithmetic atlas.  If the global value gate judges that lift
cosmetic, `VGT` must be killed rather than reframed.

The closest occupied system is P133, but the literal and proof mechanisms
separate: P133 uses squarefree prime-support bits, a Pratt divisibility DAG,
source phases, and inclusion--exclusion fibres; `VGT` uses one prime-power
valuation chain, a two-branch scalar map, a unique logarithmic extremizer, and
two explicit inverse branches.  It is also not P137 rank-feedback p-group
splitting and contains no Euclidean quotient queue from P131.

## 5. Replacement-reserve contract: `DNT` dihedral normalizer towers

Let

```text
G_m = <r,s : r^(2^m)=s^2=1, srs=r^(-1)>.
```

Every subgroup is either

```text
R_k = <r^(2^k)>                                  (0<=k<=m),
H_(k,j) = <r^(2^k), r^j s>     (0<=k<=m, 0<=j<2^k).        (5.1)
```

The literal update is `N(H)=N_(G_m)(H)`.  The proposed reserve theorem is

```text
N(R_k)=G_m,
N(H_(0,0))=G_m,
N(H_(k,j))=H_(k-1, j mod 2^(k-1))               (k>=1).    (5.2)
```

The proof conjugates `r^j s` by `r^a`; normalization is equivalent to
`2a=0 mod 2^k`, which halves the step.  Formula (5.2) gives:

- `2^(m+1)+m` states, one recurrent/fixed state `G_m`, and maximum tail `m`;
- for `m>=2`, exactly the `2^m` reflection subgroups `H_(m,j)` attain the
  sharp clock;
- temporal polynomial

  ```text
  1 + (m+3)z + sum_(k=2)^m 2^k z^k;                         (5.3)
  ```

- image size `2^m-1`;
- fibre size `m+4` over `G_m`;
- fibre size two over every `H_(k,j)` with `1<=k<m`, its preimages being
  `H_(k+1,j)` and `H_(k+1,j+2^k)`; and
- empty fibres for every remaining target.

The verifier constructs every subgroup as an actual element set, computes
every normalizer by literal conjugation, and then independently checks
(5.1)--(5.3) through `m=8`.

This is only a reserve.  Cavior's classical dihedral-subgroup classification
owns (5.1), and normalizer towers own the update mechanism.  The closest
portfolio rows are P119 (Engel group-word dynamics) and P135 (derived
centralizer orbit partitions), but neither has this carrier or inflationary
normalizer tree.  That internal separation does not overcome the external
owner compression.

## 6. Bounded owner search

Only primary papers, official publisher records, arXiv records, and an
official university-hosted research source were used.  Search misses are
reported only as bounded non-hits.

### 6.1 `VGT`

Literal/arithmetic queries included:

```text
"gcd(p^e" "d^2" divisor dynamics
"gcd(n" "d^2+n/d" divisors iteration
"gcd(p^n" "p^{2k}"
"min(2a,e-a)" dynamics
divisor self-map gcd prime power iteration dynamical system
```

No screened result stated the literal divisor map, the valuation conjugacy
(4.1), or the package (4.3)--(4.11).  **Conclusion: literal owner not located;
owner status remains unresolved.**

The second search lane used `finite discretized tent map functional graph`,
`discretized tent map finite grid periodic points`, `piecewise linear interval
map slopes 2 and -1`, and `turning point 1/3 piecewise linear map dynamics`.
The following primary sources establish a crowded zero-credit background but
do not state the exact `VGT` finite map in the material screened:

- John Milnor and William Thurston,
  [*On Iterated Maps of the Interval*](https://public.websites.umich.edu/~kochsc/MilnorThurston.pdf),
  in *Dynamical Systems*, Lecture Notes in Mathematics 1342 (1988), own the
  general kneading/piecewise-monotone framework.
- Yuriy E. Kuzovlev,
  [*Length Distribution of Periodic Orbits of Unitary Discrete Tent
  Maps*](https://arxiv.org/abs/cond-mat/0412366) (2004), studies finite
  reversible tent discretizations and their cycle statistics; those maps have
  long cycles and are not (4.1).
- The official publisher record for
  [*Some New Maximally Chaotic Discrete Maps*](https://doi.org/10.3390/e28010131)
  (2026) treats bijective finite skew-tent constructions, again with a
  different literal map and temporal silhouette.

All tent-map language, real band dynamics, and generic finite discretization
facts are therefore explicitly subtracted.  A later source proving the exact
arithmetic conjunction, or a value review finding that (4.1) is only a
decorative encoding, kills `VGT`.

### 6.2 `DNT`

Queries included `normalizer of subgroups of dihedral 2-groups paper`,
`"normalizer tower" dihedral group subgroups`, `"D2m is
self-normalizing" "D2n"`, and `"normalizer of a maximal dihedral
subgroup"`.

- Stephan R. Cavior,
  [*The Subgroups of the Dihedral
  Group*](https://doi.org/10.1080/0025570X.1975.11976454), *Mathematics
  Magazine* 48 (1975), 107, is a direct primary owner for the subgroup
  classification and subgroup count.
- An official university-hosted research text,
  [*Regular polytopes and almost
  simple groups*](https://www.famnit.upr.si/sl/resources/files/konference/rogla2016/lecturesrogla-dimitri.pdf),
  explicitly records a normalizer lemma for maximal dihedral subgroups and
  recursive use of it.  This materially increases owner risk even though the
  exact full functional graph (5.2)--(5.3) was not found in the screened text.

Conclusion: **structural owner hit; exact dynamic package non-hit is not enough
to promote.**  `DNT` remains a replacement reserve only.

## 7. Collision gate and handoff

| candidate | closest occupied interface | separating invariant | remaining kill risk |
|---|---|---|---|
| `VGT` | P133 divisor arithmetic; P137 p-group feedback; P131 Euclid queue | prime-power exponent chain, two-branch valuation map, unique logarithmic deepest state, explicit two-branch fibres | the arithmetic carrier may be only a cosmetic encoding of `min(2x,1-x)`; direct owner still unresolved |
| `DNT` | P119 group-word dynamics; P135 centralizer-derived partitions | all-subgroup normalizer inflation, unique full-group sink, binary inverse tree | classical subgroup/normalizer results may compress the residual below paper scale |

The lane recommendation is therefore:

1. carry `VGT` to the global collision/value gate as one anonymous internal
   theorem contract;
2. keep `DNT` as a clearly labelled owner-compressed reserve; and
3. keep all eight negative rows killed.

There is no paper-number assignment in this scout.  External status remains
`HOLD_EXTERNAL`.
