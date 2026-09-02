# FTC focused freeze audit: factorial-collapse skew map

**Object.** For an odd prime `p`, let

\[
T:\mathbb F_p^2\longrightarrow\mathbb F_p^2,
\qquad T(x,y)=(x+1,xy).
\]

**Gate verdict:** `PASS_OWNER_THIN`  
**External state:** `HOLD_EXTERNAL`  
**Paper allocation:** none; this file is a focused theorem/owner audit, not a
paper draft and not a novelty claim.

The theorem package is mathematically exact and has two complete axes: the
whole functional graph and the all-time fibre/inverse atlas.  Ownership is
thin because, after exchanging coordinates, the literal map is already a
parameter specialization of the Ostafe--Shparlinski triangular polynomial
family.  The only residual assessed here is the *conjunction* of the complete
nonpermutation graph, temporal polynomial, all-time fibres, inverse
identifiability, and fixed/zeta data.

## 1. Frozen theorem contract

Put

\[
P_t(X)=\prod_{j=0}^{t-1}(X+j),\qquad P_0(X)=1.
\]

For every odd prime `p`, the following statements hold.

1. **Closed iterate and collapse.** For every `t>=0`,
   \[
   T^t(x,y)=\bigl(x+t,\ yP_t(x)\bigr).
   \tag{1}
   \]
   In particular,
   \[
   T^p(x,y)=(x,0),
   \qquad
   T^t(x,y)=(x+t,0)\quad(t\ge p).
   \tag{2}
   \]

2. **Complete labelled graph.** The axis
   `C={(x,0):x in F_p}` is one cycle of length `p`.  The other `p(p-1)`
   states form exactly `p-1` pairwise disjoint directed arms, each with `p`
   transient vertices and `p` arrows before its common entry at `(1,0)`.
   If an arm is labelled by its ordinate `a in F_p^*` at depth one, its
   depth-`t` vertex is
   \[
   v_{a,t}=\left(1-t,
      \frac{a}{(-1)^{t-1}(t-1)!}\right),
   \qquad 1\le t\le p.
   \tag{3}
   \]
   Thus `v_{a,1}=(0,a)`, `T(v_{a,1})=(1,0)`, and
   `T(v_{a,t})=v_{a,t-1}` for `2<=t<=p`.  The leaf is
   \[
   v_{a,p}=(1,-a),
   \tag{4}
   \]
   so the correct leaf label is the negative of the depth-one label.

3. **Temporal polynomial.** If `tail(s)` is the least time at which `s`
   reaches the recurrent set, then
   \[
   \Theta_p(z):=\sum_{s\in\mathbb F_p^2}z^{\operatorname{tail}(s)}
      =p+(p-1)(z+z^2+\cdots+z^p).
   \tag{5}
   \]

4. **All-time image and target fibres.** For a target `(u,v)` define
   \[
   C_t(u)=P_t(u-t)=\prod_{r=1}^{t}(u-r),\qquad C_0(u)=1.
   \tag{6}
   \]
   The complete fibre is
   \[
   (T^t)^{-1}(u,v)=
   \begin{cases}
   \{(u-t,v/C_t(u))\},& C_t(u)\ne0,\\[2mm]
   \{(u-t,y):y\in\mathbb F_p\},& C_t(u)=0,\ v=0,\\[2mm]
   \varnothing,& C_t(u)=0,\ v\ne0.
   \end{cases}
   \tag{7}
   \]
   Let `r_t=min(t,p)`.  At every time `t>=0`,
   \[
   |\operatorname{im}T^t|=p(p-r_t)+r_t,
   \tag{8}
   \]
   and the numbers of codomain targets with fibre sizes `1`, `p`, and `0`
   are respectively
   \[
   N_1(t)=p(p-r_t),\qquad
   N_p(t)=r_t,\qquad
   N_0(t)=r_t(p-1).
   \tag{9}
   \]
   In particular, for `0<=t<=p`, the requested image formula is
   `p(p-t)+t`; for `t>=p`, the image is exactly the axis and has size `p`.

5. **Inverse identifiability.** From a feasible time-`t` observation `(u,v)`,
   the initial first coordinate is always identifiable as `x=u-t`.  The
   initial second coordinate is identifiable exactly when `C_t(u)!=0`.
   When `C_t(u)=0` and `v=0`, all `p` possible ordinates are observationally
   indistinguishable; when `v!=0`, the observation is impossible.  This is a
   pointwise statement, not merely a fibre-size distribution.

6. **Periodic data and zeta.** The only periodic points are the `p` axis
   points, and they constitute one cycle of least period `p`.  For `n>=1`,
   \[
   \#\operatorname{Fix}(T^n)=
   \begin{cases}
   p,&p\mid n,\\
   0,&p\nmid n.
   \end{cases}
   \tag{10}
   \]
   Hence the exact-period point counts and cycle counts are
   \[
   E_m=p\,\mathbf 1_{m=p},\qquad
   A_m=\mathbf 1_{m=p},
   \tag{11}
   \]
   and the finite-map Artin--Mazur zeta series is
   \[
   \zeta_T(z)=
   \exp\!\left(\sum_{n\ge1}\frac{\#\operatorname{Fix}(T^n)}n z^n\right)
   =\frac1{1-z^p}.
   \tag{12}
   \]

## 2. Proof audit

### 2.1 Closed iterate and factorial collapse

Equation (1) is an induction on `t`.  It is the identity at `t=0`.  If it
holds at `t`, then

\[
\begin{aligned}
T^{t+1}(x,y)
 &=T\bigl(x+t,yP_t(x)\bigr)\\
 &=\bigl(x+t+1,(x+t)yP_t(x)\bigr)\\
 &=\bigl(x+t+1,yP_{t+1}(x)\bigr).
\end{aligned}
\]

The elements `-j`, `0<=j<p`, run through all of `F_p`, so the monic
polynomials with those roots give

\[
P_p(X)=\prod_{j=0}^{p-1}(X+j)=X^p-X.
\tag{13}
\]

Every `x in F_p` satisfies `x^p=x`; consequently `P_p(x)=0` pointwise and
`T^p(x,y)=(x,0)`.  Once the orbit lies on `y=0`, it remains there, giving the
second clause of (2).  The assertion is equality of functions on
`F_p^2`; the formal polynomial `X^p-X` is not the zero polynomial.

### 2.2 First collapse time and the temporal polynomial

Suppose `y!=0`.  Before a zero multiplier occurs, every factor is nonzero and
the ordinate remains nonzero.  The first zero multiplier is the unique step
with

\[
x+j=0,\qquad 0\le j<p.
\]

Counting that transition itself, the tail is

\[
d(x)=\text{the representative of }1-x\pmod p\text{ in }\{1,\ldots,p\}.
\tag{14}
\]

At that time the state is `(x+d(x),0)=(1,0)`.  For each depth
`t in {1,...,p}`, the first coordinate is uniquely `x=1-t`, while `y` has
`p-1` nonzero choices.  Therefore there are `p-1` states at every positive
depth `1,...,p`, and the `p` axis states have depth zero.  This proves (5).

It also proves that every off-axis orbit enters the same cycle point `(1,0)`.
On the axis the map is `x -> x+1`, hence the axis is a single `p`-cycle.

### 2.3 Exact arm labels

Take a state of depth `t`; its first coordinate is `1-t`.  After `t-1`
nonsingular steps it reaches first coordinate zero, and its ordinate is

\[
y\prod_{j=0}^{t-2}(1-t+j)
 =y\prod_{k=1}^{t-1}(-k)
 =y(-1)^{t-1}(t-1)!.
\tag{15}
\]

Calling this ordinate `a` gives (3).  Direct substitution shows
`T(v_{a,t})=v_{a,t-1}` for `t>=2`, while `(0,a)` maps to `(1,0)`.
Different labels give different ordinates at depth one, hence disjoint arms;
their total size `(p-1)p` is the full off-axis population.

For `t=p`, Wilson's theorem and oddness of `p` give

\[
(-1)^{p-1}(p-1)!=(p-1)!=-1,
\]

which proves `v_{a,p}=(1,-a)`.  This sign is the principal arm-labelling
off-by-one risk and was checked independently in every replay box.

The literal indegrees provide a second graph check: `(1,0)` has `p`
predecessors, every `(1,v)` with `v!=0` has none, and every other vertex has
exactly one.  Thus no hidden branch or component remains.

### 2.4 Target-by-target fibres and images

Fix `t` and a target `(u,v)`.  Equation (1) forces the unique source first
coordinate

\[
x=u-t.
\]

The remaining target equation is

\[
v=yP_t(u-t)=yC_t(u),
\]

and reindexing the factors yields (6).  A nonzero coefficient has exactly one
solution for `y`; a zero coefficient has all `p` solutions when `v=0` and no
solution otherwise.  This proves the pointwise atlas (7) and the inverse
statement.

For `0<=t<=p`, the roots of `C_t(u)` are the `t` distinct target columns

\[
u=1,2,\ldots,t\pmod p.
\tag{16}
\]

Each of the other `p-t` columns contains `p` targets with singleton fibres.
Each collapsed column contributes one target with fibre `p` and `p-1`
impossible targets.  Therefore

\[
N_1=p(p-t),\qquad N_p=t,\qquad N_0=t(p-1),
\]

and `|im T^t|=N_1+N_p=p(p-t)+t`.  When `t>=p`, the product in (6) contains a
complete residue system, so `C_t(u)=0` for every `u`; (8)--(9) follow with
`r_t=p`.  The two conservation checks are

\[
N_1+N_p+N_0=p^2,
\qquad
1\cdot N_1+p\cdot N_p=p^2.
\tag{17}
\]

### 2.5 Fixed iterates, cycles, and zeta

If `p` does not divide `n`, the first coordinate of `T^n(x,y)` is `x+n`, so
there are no fixed points.  If `p` divides `n`, then `n>=p`; (2) gives
`T^n(x,y)=(x,0)`, which is fixed exactly when `y=0`.  This proves (10).

Every axis point has least period `p`, and Section 2.2 shows that every other
point is transient.  Thus (11) follows.  Finally,

\[
\sum_{n\ge1}\frac{\#\operatorname{Fix}(T^n)}n z^n
=\sum_{k\ge1}\frac{p}{kp}z^{kp}
=\sum_{k\ge1}\frac{z^{kp}}k
=-\log(1-z^p),
\]

which proves (12).  No characteristic-three exception or zeta-factor merger
occurs: there is one factor and its exponent is exactly one.

## 3. Deterministic exact replay

The verifier is
[`verify.py`](../scouting/ftc/verify.py), and frozen stdout is
[`CANONICAL.txt`](../scouting/ftc/CANONICAL.txt).

Run it from the repository root with

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers152_156_sequence/scouting/ftc/verify.py
```

The verifier uses no randomness and no external package.  Its independent
lanes are:

1. literal one-step trajectory tables versus the rising-factorial iterate,
   with direct-product anchor times;
2. first-repetition orbit discovery for every state, independent of the arm
   parametrization;
3. literal indegrees and the separate factorial arm labels, including
   `v_{a,p}=(1,-a)`;
4. literal images followed by every-target source-set comparison at every
   `0<=t<=p+3`;
5. fixed-set comparison at every `1<=n<=3p`; and
6. integer target-partition and source-mass identities.

The frozen run covers the 25 odd primes

`3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101`,

for a total of **75,993 states** and **18,942,551 assertions**.  It ends with

```text
PROFILE_SHA256 b44a7815c886a98409b5f56a0c26ce24f8644fa4f6b57a238d5a50d8a2d83810
TOTAL boxes=25 states=75993 assertions=18942551
VERDICT PASS_EXACT_REPLAY
```

Enumeration is falsification pressure and a regression seal, not a proof and
not an ownership certificate; Sections 1--2 are the proof.

## 4. Owner audit and residual boundary

The full query/source ledger is
[`OWNER_LOG.md`](../scouting/ftc/OWNER_LOG.md).  The decisive facts are:

- Under the coordinate exchange `(Y,X)=(y,x)`, FTC becomes
  `(Y,X)->(YX,X+1)`.  This is the `m=1` specialization
  `g_0(X)=X`, `h_0=0`, `a=b=1` of the Ostafe--Shparlinski family in
  [arXiv:0902.3884](https://arxiv.org/abs/0902.3884).  That source even singles
  out `g_i=X_{i+1}` with constant `h_i` and poses study of periods.  Therefore
  the construction, family, degree-growth engine, and elementary factorial
  iteration are fully owner-compressed.
- The follow-up [arXiv:0908.4519](https://arxiv.org/abs/0908.4519) retains the
  same triangular family but studies exponential sums, discrepancy,
  permutation averages, and hash functions, not this whole nonpermutation
  graph/fibre conjunction.
- Maubach's [arXiv:1106.5800](https://arxiv.org/abs/1106.5800) and
  [arXiv:1307.6469](https://arxiv.org/abs/1307.6469) own characteristic-`p`
  triangular automorphism/permutation, conjugacy, and maximal-orbit theory.
  FTC has Jacobian determinant `x` and collapses the `x=0` column, so those
  invertible theorems do not state its fibres or arms.
- [Konyagin et al., arXiv:1307.2718](https://arxiv.org/abs/1307.2718) is
  general zero-credit functional-graph background for univariate
  polynomials, not a bivariate FTC classification.
- Exact-string, recurrence, factorial, cocycle, and functional-graph queries
  gave no direct source for the full five-part conjunction.  This is only a
  bounded conjunction non-hit.  It cannot support novelty or priority
  language.

Accordingly the only allowed residual description is:

> complete nonpermutation functional graph and temporal polynomial, coupled
> with an all-time every-target fibre/inverse atlas and the resulting
> fixed/zeta package, for one already-owned triangular specialization.

## 5. Internal collision audit

| Prior paper | Prior engine/package | FTC separation |
|---|---|---|
| P99 | The unipotent matrix `[[1,1],[0,1]]` permutes fixed-index sublattices of `Z^2`; HNF divisor layers yield cycles, fixed counts, valuation staircases, and zeta. | FTC acts on `F_p^2`, is noninvertible, has one translating base cycle and factorial-collapse arms.  There are no HNF layers, sublattices, divisor sums, or valuation staircase. |
| P104 | Random products of two invertible real `2x2` monomial matrices; occupation normal form, singular values, Lyapunov limits, folded CLT, and annealed pressure. | FTC is a deterministic finite-field triangular map.  Its product is a scalar rising-factorial cocycle that becomes zero; there are no random words, singular-value asymptotics, Lyapunov exponents, or transfer pressure. |
| P150 | A zero-totalized rational Lyness map on the whole `F_q^2`; periods `1/2/4/5`, a sharp depth-three exceptional tree, one-time `0/1/q` fibres, and zeta. | This is the closest interface collision, so generic graph/fibre/zeta language is zero credit.  FTC is a global polynomial map with one `p`-cycle, depth growing exactly to `p`, `p-1` equal arms, and a progressive all-time image/fibre atlas `p(p-t)+t`.  It has no rational totalization or Lyness identity. |

The collision check passes at the literal system and proof-engine levels.
Nevertheless, P150 makes the generic “finite-plane graph plus fibres plus
zeta” narrative unavailable as a residual claim; FTC must be presented, if
ever used, through its factorial collapse schedule and all-time inverse atlas.

## 6. Gate decision and limitations

| Gate | Result |
|---|---|
| Closed iterate and `T^p` | `PASS` |
| Correct arm labels and graph completeness | `PASS`; leaf is `(1,-a)` |
| Temporal polynomial | `PASS` |
| `0<=t<=p` image/fibre formula | `PASS` |
| Saturated `t>=p` fibre atlas | `PASS` |
| Fixed/cycle/zeta package | `PASS` |
| Deterministic exact replay | `PASS_EXACT_REPLAY` |
| Exact theorem-conjunction owner | bounded non-hit only |
| Construction/family ownership | direct family inclusion; zero credit |
| Portfolio collision | no literal/engine collision; generic interface compressed |
| External release | `HOLD_EXTERNAL` |

**Final verdict: `PASS_OWNER_THIN`.**  This means the contract is safe to
freeze as an internally verified reserve candidate, but it is not an
ownership-clean construction and is not yet allocated a paper number.  The
proof is unusually short because every theorem is driven by one factorial
zero; that elegance is also a compression risk.  A later paper gate would
need to judge whether the residual conjunction is substantial enough after
fully crediting the Ostafe--Shparlinski specialization and P150's internal
interface precedent.
