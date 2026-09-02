# HTM/BTB focused owner-and-formula freeze gate

**Audit date:** 2026-09-02 UTC.  
**External status:** `HOLD_EXTERNAL`.  
**Scope effect:** no paper number, no draft, no novelty or priority claim.  
**Stage-1 canonical:** read-only; this audit does not alter it.

## 1. Outcome first

| system | owner result | formula result | freeze verdict |
|---|---|---|---|
| HTM, hierarchical tree meet | Brown and descendants directly own the finite-semigroup/LRB random-product framework and generic absorption machinery.  Fuchs--Steel is a same-observable MRCA neighbour.  No checked primary source states the surviving nested-cylinder/inverse/area-exchange conjunction. | Exact layer law, all-time transform, clock, known-time inverse, area, and sharp fixed-multiset extremizers rederive correctly, including the unknown-time ambiguity and `h=1` boundary. | **`PASS_OWNER_THIN`** |
| BTB, balanced-triad dynamics on a triangular book | Antal--Krapivsky--Redner and Istrate directly own the update kernel; Istrate owns its XOR/triadic-dual representation and generic recurrence/absorption questions.  Signed-book work owns the carrier and its `r+1` switching classes.  No checked primary source gives the triangular-book exact law. | Strong lumping, Chebyshev elimination, joint transform, quadratic mean, parity inverse, and absorption bound rederive correctly.  The `r=1`, `r=2`, and `z=0` exceptions are explicit. | **`PASS_OWNER_THIN`** |

Neither verdict means “novel.”  It means only that this bounded primary-source
gate did not find a direct owner of the deliberately narrowed residual.  BTB is
the stronger internal theorem package, although it carries the more severe
same-kernel subtraction.  HTM is mathematically clean but thinner after Brown's
framework and the elementary order-statistic calculation are removed.

The kill rule used here was conservative: a source that determines the complete
special-carrier law after a routine substitution would cause `KILL_DIRECT`, even
if it used different coordinates.  No such source was found.  A generic framework
or the exact update without the special-carrier law causes zero-credit subtraction,
not an automatic kill.  A formula defect requiring a theorem change would cause
`REPAIR`; the independent replay found none.

## 2. Audit method and bounded-search limitation

### 2.1 Primary-source channels actually checked

- arXiv title/abstract records and author-posted full PDFs;
- publisher or DOI metadata for the journal versions;
- Kenneth Brown's Cornell publication page and author-hosted survey;
- Project Euclid for the tree-shuffle neighbour; and
- official journal/arXiv full text for the signed-book and social-balance chain.

Search-engine and index snippets were used only to locate primary records.  They
were not used as evidence for a theorem-level non-hit.  The decisive comparisons
below come from the full papers.

### 2.2 Query families

The following query families were run with spelling and hyphen variants.

```text
HTM:
  semilattice random walk absorption
  meet semigroup Markov chain
  left regular band meet random product
  random LCA / random lowest common ancestor
  longest common prefix Markov chain
  repeated meet random leaves rooted tree
  branching profile inverse from LCA depth
  MRCA depth random sample
  random-to-front shuffle tree Brown

BTB:
  signed book graph social balance dynamics
  triangular book triadic dynamics
  K_{1,1,r} social balance / edge flip
  shared-edge triangles balance process
  book graph XOR hyperedge switching
  star hypergraph annihilating walk exact absorption
  friendship graph / windmill social balance
  book graph Chebyshev absorption generating function
```

Within downloaded full text, targeted phrase searches included `lowest common
ancestor`, `longest common prefix`, `branching profile`, `depth area`,
`Chebyshev`, `book graph`, `friendship graph`, `windmill`, `spine flip`,
`bivariate`, and `inverse problem`.  Phrase non-hits are only routing evidence;
they are not novelty evidence.

### 2.3 Classification vocabulary

- **Direct:** same literal kernel or a theorem whose specialization determines
  the claimed object.
- **Same object:** same carrier/observable but a different update or random
  carrier law.
- **Nearest neighbour:** common algebraic framework or vocabulary without the
  same object and kernel.
- **Zero credit:** material that cannot be counted as an internal contribution,
  whether or not the residual survives.

Subscription-only exhaustive citation databases were not treated as completed.
The final verdicts therefore remain `OWNER_THIN` and `HOLD_EXTERNAL`.

## 3. HTM: frozen object and claim subtraction

Fix `h>=1` and integers `b_i>=2`.  Vertices of the level-homogeneous rooted
tree are mixed-radix words; a leaf has length `h`.  Fix a leaf `v`, start at
`X_0=v`, sample independent uniform leaves `U_t`, and set

```text
X_t = X_{t-1} meet U_t = LCA(X_{t-1},U_t).
```

Write `D_t=depth(X_t)`, `B_k=product_{j<=k} b_j`, and
`T=inf{t>=1:D_t=0}`.

### 3.1 Brown chain: direct generic owner

1. Kenneth S. Brown,
   [*Semigroups, rings, and Markov chains*](https://arxiv.org/abs/math/0006145),
   *Journal of Theoretical Probability* 13 (2000), 871--938,
   [DOI 10.1023/A:1007822931408](https://doi.org/10.1023/A:1007822931408).
   Section 1.1 defines a random walk on a finite left-regular band by
   `s -> x s`, with `x` sampled from fixed weights.  A meet-semilattice is a
   commutative idempotent semigroup and hence a left-regular band.  HTM is
   literally this random product, with the sampling measure supported on the
   leaves and initial element `v`.  Brown also supplies generic spectral
   diagonalization.  This is **direct framework ownership**, not merely an
   analogy.

2. Brown,
   [*Semigroup and Ring Theoretical Methods in Probability*](https://pi.math.cornell.edu/~kbrown/papers/toronto.pdf),
   Fields Institute Communications 40 (2004), 3--26.  The author-hosted survey
   develops the same semigroup and band machinery.  It reinforces, rather than
   narrows, the zero-credit boundary.

3. Ayyer, Schilling, Steinberg, and Thiéry,
   [*Markov chains, R-trivial monoids and representation theory*](https://arxiv.org/abs/1401.4250),
   *International Journal of Algebra and Computation* 25 (2015), 169--231,
   [DOI 10.1142/S0218196715400081](https://doi.org/10.1142/S0218196715400081).
   Corollary 4.15 and Theorem 4.16 give convolution/absorption formulas and an
   exact Möbius expression for expected absorption time on left-regular bands;
   Example 4.17 explicitly treats a semilattice coupon collector.  Thus generic
   finite-time convolution, absorption-time expectation, and Möbius/spectral
   extraction cannot be marketed as HTM-specific advances.

4. Rhodes and Schilling,
   [*Unified theory for finite Markov chains*](https://arxiv.org/abs/1711.10689),
   *Advances in Mathematics* 347 (2019), 739--779,
   [DOI 10.1016/j.aim.2019.03.004](https://doi.org/10.1016/j.aim.2019.03.004),
   extends random-walk analysis to general finite semigroups using expansions,
   normal forms, and stationary/mixing formulas.  It is a **generic descendant**.

5. Pang,
   [*Lumpings of Algebraic Markov Chains arise from Subquotients*](https://arxiv.org/abs/1508.01570),
   *Journal of Theoretical Probability* 32 (2019), 1804--1844,
   [DOI 10.1007/s10959-018-0834-0](https://doi.org/10.1007/s10959-018-0834-0),
   and Nestoridi,
   [*Random walks on hyperplane arrangements and stopping times*](https://arxiv.org/abs/1605.08339),
   are additional algebraic-lumping/stopping-time descendants.  They do not
   state the HTM tree-cylinder formulas, but they prevent a broad claim about
   algebraic lumping or stopping-time methodology.

### 3.2 Tree/MRCA citation neighbours

- Björner,
  [*Random-to-front shuffles on trees*](https://doi.org/10.1214/ECP.v14-1445),
  *Electronic Communications in Probability* 14 (2009), 36--41, uses a fixed
  rooted tree, leaf-driven updates, and Brown's semigroup theory.  Its state is
  an ordering of children and its update is a random-to-front reordering.  It
  is a **same-carrier nearest neighbour**, not the LCA meet chain.

- Nestoridi and Nguyen,
  [*On the spectrum of random walks on complete finite d-ary trees*](https://arxiv.org/abs/1912.06771),
  analyze nearest-neighbour simple random walk on the vertices of a complete
  finite tree.  This is a **different kernel on a similar carrier**.

- Fuchs and Steel,
  [*Predicting the depth of the most recent common ancestor of a random sample
  of k species: the impact of phylogenetic tree shape*](https://arxiv.org/abs/2501.09270),
  gives exact and asymptotic MRCA-depth results for samples from random
  phylogenetic trees.  It is the closest checked **same-observable source**.
  Its tree shape is random, its tips are sampled without the HTM repeated-meet
  state process, and it does not infer a fixed branching profile from one known
  time layer or optimize depth-area over factor order.

No checked paper in this chain prints the conjunction

```text
nested deterministic cylinder tails
+ known-positive-time recovery of every b_i
+ fixed-multiset sharp area extremizers.
```

That is a bounded non-hit, not a novelty finding.

### 3.3 HTM zero-credit ledger

The following must receive zero credit in any later contract:

- the representation as a meet-semilattice, left-regular band, or finite
  semigroup walk;
- the iid-product identity as an abstract semigroup fact;
- generic diagonalization, eigenvalue, rational-resolvent, convolution,
  lumping, and absorption-time machinery;
- the general language of a random sample's LCA/MRCA depth; and
- the fact that a minimum of iid prefix depths has a product tail, considered
  without the inverse/extremal conjunction.

The only residual allowed through this gate is the **map-specific conjunction**
of the explicit nested layer, known-time branching inverse, and sharp
fixed-multiset depth-area exchange theorem.  The root clock and transform may
support that conjunction, but cannot alone carry a paper.

## 4. HTM: independent formula rederivation

### 4.1 Pathwise identity and exact layers

Meet is associative, commutative, and idempotent, so induction gives

```text
X_t = LCA(v,U_1,...,U_t).
```

For `1<=k<=h`, the event `D_t>=k` says that every one of the `t` sampled
leaves lies in the depth-`k` cylinder containing `v`.  That cylinder has mass
`1/B_k`; independence therefore gives

```text
P(D_t>=k)=B_k^(-t).                              (HTM.1)
```

This includes `t=0`.  For `t>=1`, differencing the tails gives

```text
P(D_t=0)=1-b_1^(-t),
P(D_t=d)=B_d^(-t)-B_{d+1}^(-t)       (1<=d<h),
P(D_t=h)=B_h^(-t).
```

### 4.2 All-time transform

For any integer-valued `D` in `{0,...,h}`,

```text
y^D = 1 + sum_{k=1}^h (y^k-y^(k-1)) 1_{D>=k}.
```

Insert (HTM.1), sum the geometric series in `t`, and obtain, for `|z|<1`,

```text
sum_{t>=0} z^t E[y^{D_t}]
 = 1/(1-z)
   + sum_{k=1}^h (y^k-y^(k-1))/(1-z/B_k).        (HTM.2)
```

The independent verifier also solves the finite resolvent system
`H_d=y^d+z sum_j P(d,j)H_j` from the literal leaf kernel and matches (HTM.2).
This prevents the transform from being a circular restatement of the tail
formula in the computational evidence.

### 4.3 Root clock and its information ceiling

At every positive depth, the next state reaches the root precisely when the
first symbol of the fresh leaf differs from that of `v`, an event of probability
`(b_1-1)/b_1`.  Hence

```text
P(T>t)=b_1^(-t),
E[z^T]=(b_1-1)z/(b_1-z),
E T=b_1/(b_1-1),
Var(T)=b_1/(b_1-1)^2.                            (HTM.3)
```

The clock cannot distinguish any two profiles with the same `b_1`; this is an
explicit nonidentifiability theorem, not an omitted case.

### 4.4 Known-time inverse and unknown-time ambiguity

If `t>0` is known and the entire exact depth layer is known, then its tails give

```text
B_k = P(D_t>=k)^(-1/t),
b_1=B_1,                 b_k=B_k/B_{k-1}.         (HTM.4)
```

The domain qualifications matter.

- At `t=0`, every tail is one and no profile is recoverable.
- If `t` is unknown, perfect-power ambiguity occurs.  Profiles `(4,9)` at time
  one and `(2,3)` at time two have prefix products `(4,36)` and `(2,6)` and
  therefore the same complete tails `(1/4,1/36)`.
- With a nonuniform leaf law, (HTM.1) recovers nested cylinder masses, not
  integer branching factors.
- On an irregular tree there need not be a single level branching profile.

### 4.5 Depth-area and sharp factor order

Let `A=sum_{t>=0}D_t`.  Tonelli and tail summation give

```text
E A = sum_{k=1}^h sum_{t>=0} B_k^(-t)
    = sum_{k=1}^h B_k/(B_k-1)
    = h + sum_{k=1}^h 1/(B_k-1).                 (HTM.5)
```

Fix a multiset of branching factors.  Consider adjacent factors `a,b` after a
prefix product `P`.  Swapping them changes no prefix product except the first
one in the pair: it replaces the summand

```text
1/(Pa-1)  by  1/(Pb-1).
```

If `a<b`, the former is strictly larger.  Repeated adjacent exchanges prove:

- nondecreasing factor order uniquely maximizes `E A`;
- nonincreasing factor order uniquely minimizes `E A`; and
- uniqueness is modulo exchanges of equal factors.

For `h=1`, both orders coincide and the extremizer statement is tautological.
The assumption `b_i>=2` is essential: `b_1=1` gives zero root hazard and makes
the corresponding area summand divergent.

### 4.6 HTM verdict

**`PASS_OWNER_THIN`.**  There is no formula repair and no direct checked owner
of the narrowed conjunction.  However, Brown's ownership is broad enough that
any later draft must lead with the tree-cylinder inverse and exchange theorem,
not with semigroups, iid products, rational transforms, spectra, or generic
absorption.  HTM remains a thin reserve rather than a frozen paper assignment.

## 5. BTB: exact relation to the owner kernel

Let `B_r=B(3,r)=K_{1,1,r}` be `r>=1` triangles sharing one common spine
edge.  Give every physical edge a sign.  Let `x_i=1` when page `i` is
imbalanced.  At an update epoch, choose an imbalanced page uniformly, choose
one of its three edges uniformly, and flip it.  Stop at `x=0`.

Write `K=sum_i x_i`, `T` for the number of update epochs to absorption, and
`J` for the number of common-spine flips.

### 5.1 Antal--Krapivsky--Redner: update owner

- Antal, Krapivsky, and Redner,
  [*Dynamics of Social Balance on Networks*](https://arxiv.org/abs/cond-mat/0506476),
  *Physical Review E* 72 (2005), 036121,
  [DOI 10.1103/PhysRevE.72.036121](https://doi.org/10.1103/PhysRevE.72.036121).
  The 2005 LTD clock first chooses a random triad; a balanced triad is a no-op.
  At `p=1/3`, the three edges of an imbalanced target are equiprobable.  On a
  triangular book, BTB is exactly its chain embedded at non-no-op update epochs.

- Antal, Krapivsky, and Redner,
  [*Social Balance on Networks: The Dynamics of Friendship and Enmity*](https://arxiv.org/abs/physics/0605183),
  *Physica D* 224 (2006), 130--136,
  [DOI 10.1016/j.physd.2006.09.028](https://doi.org/10.1016/j.physd.2006.09.028).
  Section 2 instead states the update-epoch formulation directly: choose a
  random imbalanced triad; at `p=1/3` flip each edge equiprobably.  On `B_r`
  this is the **same kernel without a clock change**.

The social-balance motivation, imbalanced-triad selection rule, and `p=1/3`
edge rule are therefore direct-owner material.

### 5.2 Istrate chain: exact probabilistic and XOR owner

Gabriel Istrate,
[*On the dynamics of Social Balance on general networks (with an application
to XOR-SAT)*](https://arxiv.org/abs/0811.0381), *Fundamenta Informaticae* 91
(2009), 341--356,
[DOI 10.3233/FI-2009-0047](https://doi.org/10.3233/FI-2009-0047), is still
closer.

- Definition 2 chooses a uniformly random imbalanced triangle.  At `p=1/3`,
  each of its edges is selected with probability `1/3` (for one-negative and
  three-negative triangles alike).  This is BTB's literal update.
- Definition 4 forms the triadic dual: a physical edge becomes the hyperedge
  containing all triangles that use it, and a private physical edge becomes a
  self-loop.  For `B_r`, the dual has one size-`r` hyperedge plus two self-loops
  at every one of the `r` page vertices.
- The hyperedge-switching/XOR representation is therefore also directly owned.
- Theorem 1 characterizes recurrent states when each physical edge is in at
  most two triangles.  It covers the qualitative absorption statement for
  `r=1,2` because the book has private edges, but its hypothesis fails for
  `r>=3`, where the spine belongs to `r` triangles.  It does not give the
  book-specific exact transform or clock law.

Istrate, Bonchis, and Marin,
[*Interactive Particle Systems on Hypergraphs, Drift Analysis and the WalkSAT
algorithm*](https://arxiv.org/abs/1909.12353), further formalizes the same
random-live-node/random-incident-hyperedge annihilating process, allows multiple
self-loops, and studies convergence by drift/odd-Cheeger parameters.  This
subtracts generic hypergraph annihilation, WalkSAT duality, reachability, and
generic expected-time bounds.  Full-text screening found no specialization to
the one-size-`r`-edge-plus-two-loops carrier and no BTB exact law.

### 5.3 Same carrier: signed-book static owner

Sehrawat and Bhattacharjya,
[*Chromatic Polynomials of Signed Book Graphs*](https://arxiv.org/abs/2206.08580),
*Theory and Applications of Graphs* 9 (2022), article 4,
[DOI 10.20429/tag.2022.090104](https://doi.org/10.20429/tag.2022.090104),
define `B(m,n)` as `n` copies of `C_m` with one common edge.  Theorem 2.1
proves that there are `n+1` switching-nonisomorphic signatures, classified by
the number of negative pages.  At `m=3`, that statistic is precisely `K`.

Thus the triangular-book carrier, switching reduction, and static `r+1` class
census are zero-credit.  The paper studies chromatic and zero-free chromatic
polynomials; full-text searches found no Markov dynamics or hitting law.

### 5.4 Book versus windmill/friendship carriers

Terminology is a real collision risk.

```text
triangular book B(3,r) = K_{1,1,r}:
    r triangles share one EDGE;

friendship / Dutch windmill F_r = K_1 join r K_2:
    r triangles share one VERTEX and no edge.
```

They do not induce the same dynamics.  In the friendship graph every selected
edge belongs only to the chosen page, so every update simply clears that page:
`K -> K-1` and `T=K` deterministically.  The reflection `k -> r-k` is caused
specifically by the triangular book's common edge.  Some graph literature also
uses “book graph” for quadrilateral-page graphs such as `K_{1,r} square P_2`.
Any later title/definition must say **triangular book `B(3,r)=K_{1,1,r}`**.

### 5.5 BTB owner classification

| source family | relation | zero-credit consequence |
|---|---|---|
| AKR 2005 | same edge rule; BTB is embedded non-no-op chain | update, balance semantics, `p=1/3` choice |
| AKR 2006 | same update-epoch kernel | entire literal stochastic rule |
| Istrate 2009 | same kernel on arbitrary graph; exact triadic dual | XOR/hyperedge encoding, generic recurrence/absorption |
| Istrate--Bonchis--Marin 2019 | same generic live-particle hypergraph process | generic convergence-time/drift program |
| Sehrawat--Bhattacharjya 2022 | same signed triangular-book carrier and `K` class statistic | carrier, switching classes, static quotient |
| friendship/windmill work | different shared-vertex carrier | terminology and generic graph facts only |

No checked source gives the surviving conjunction

```text
exact triangular-book count transition
+ bivariate (T,J) transform
+ sharp mean extrema
+ spine-parity law and two-statistic inverse.
```

Again, this is a bounded non-hit only.

## 6. BTB: independent formula rederivation

### 6.1 Literal quotient

A private-edge flip clears only the selected page, whereas a spine flip toggles
every page.  Consequently the full bit process is strongly lumpable by `K`:

```text
k -> k-1       with probability 2/3,
k -> r-k       with probability 1/3.             (BTB.1)
```

When the two targets coincide, their masses add.  The exact verifier enumerates
all three literal physical-edge choices from every nonzero bit vector through
`r=9`; all 1,013 states have the same quotient law within a count class.

### 6.2 Joint transform and Chebyshev elimination

Define

```text
F_k(z,u)=E_k[z^T u^J],       F_0=1.
```

First-step conditioning gives

```text
F_k = z[(2/3)F_{k-1}+(u/3)F_{r-k}].              (BTB.2)
```

For `1<=k<r`, use (BTB.2) at `k`, `r-k`, and `k+1`.  First,

```text
u F_{r-k}=3F_k/z-2F_{k-1}.
```

The reflected equation gives

```text
F_{r-k-1}=3F_{r-k}/(2z)-(u/2)F_k.
```

Substitution into the `k+1` equation yields

```text
F_{k+1}=2 xi F_k-F_{k-1},
xi=[9+z^2(4-u^2)]/(12z).                         (BTB.3)
```

Let `U_j` be the second-kind Chebyshev polynomials, with `U_{-1}=0`.
The solution satisfying `F_0=1` is

```text
F_k=U_{k-1}(xi)F_1-U_{k-2}(xi).                 (BTB.4)
```

The final Bellman condition

```text
F_r=(2z/3)F_{r-1}+zu/3
```

therefore gives, for `r>=2`,

```text
F_1 = [3U_{r-2}(xi)-2zU_{r-3}(xi)+zu]
      /[3U_{r-1}(xi)-2zU_{r-2}(xi)].             (BTB.5)
```

This is an identity of rational functions.  For the probability transform it
is immediately safe on `|z|<1, |u|<=1`; removable values are taken by
continuity from the Bellman system.

### 6.3 The `r=1`, `r=2`, and `z=0` boundaries

- `r=1`: every update absorbs, with a private edge in two of the three cases
  and the spine in one.  Thus

  ```text
  F_1=z(2+u)/3.
  ```

  Formula (BTB.5) is not invoked because it would require `U_{-2}`.

- `r=2`: from count one, a spine flip is a self-loop.  Directly,

  ```text
  F_1=2z/(3-zu).
  ```

  The displayed Chebyshev ratio initially reads
  `(3+zu)/(6xi-2z)`.  Since

  ```text
  6xi-2z=(3-zu)(3+zu)/(2z),
  ```

  the factor `3+zu` cancels.  The theorem must state rational identity or
  continuation; uncancelled pointwise substitution can create a false `0/0`.

- `z=0`: `xi` is undefined, whereas the Bellman solution is simply
  `F_0=1` and `F_k=0` for `k>0`.  The Chebyshev display is interpreted through
  its reduced rational continuation, not by substituting `z=0` into `xi`.

These are presentation boundaries, not theorem repairs.

### 6.4 Mean and sharp extrema

Let `m_k=E_k T`.  Then

```text
m_0=0,
m_k=1+(2/3)m_{k-1}+(1/3)m_{r-k}.                (BTB.6)
```

Eliminating the reflected term gives

```text
m_{k+1}-2m_k+m_{k-1}=-1,
```

and the terminal condition is `m_r=1+(2/3)m_{r-1}`.  Hence

```text
m_k=k(r+2-k)/2.                                  (BTB.7)
```

For `r>1`, this concave quadratic has unique minimum at `k=1`, equal to
`(r+1)/2`.  Its maxima are

```text
r even:  k=(r+2)/2,                    value (r+2)^2/8;
r odd:   k=(r+1)/2,(r+3)/2,            value ((r+2)^2-1)/8.
```

For `r=1`, the sole nonzero state is both minimum and maximum, with mean one.

### 6.5 Spine parity and inverse boundary

Put `h_k=E_k[(-1)^J]`.  A private flip preserves the sign and a spine flip
reverses it, so

```text
h_0=1,
h_k=(2/3)h_{k-1}-(1/3)h_{r-k}.
```

Direct substitution gives

```text
h_k=(r+2-2k)/(r+2),
q:=P_k(J odd)=k/(r+2).                           (BTB.8)
```

Combining (BTB.7) and (BTB.8),

```text
m=(r+2)^2 q(1-q)/2,
r+2=sqrt[2m/{q(1-q)}],
k=q(r+2).                                        (BTB.9)
```

This inverse is exact only for a nonabsorbing start `1<=k<=r`, so `0<q<1`.
The recovered square root and `k` must pass integer feasibility.  The central
case `q=1/2` is valid and occurs for even `r`; it is not a singular boundary.
No stability or noisy-data identifiability follows from (BTB.9).

### 6.6 Absorption

At every pre-absorption update the selected physical edge is private with
probability `2/3`, independent of the current count.  Every private update
reduces `K` by one.  Thus a pre-generated block of `r` private edge types forces
absorption, possibly before the block ends, and has probability `(2/3)^r`.
By the Markov property,

```text
P_k(T>nr) <= [1-(2/3)^r]^n.                      (BTB.10)
```

This proves almost-sure absorption and an exponential tail.  It is a special
book certificate, not a claim that generic triadic dynamics always absorbs.

### 6.7 Clock and symmetry qualifications

- Equations (BTB.2)--(BTB.10) count **imbalanced-triad update epochs**.  Under
  AKR 2005's all-triad clock, balanced pages create state-dependent geometric
  holding times.  The embedded jump chain is still BTB, but physical time is
  not `T`.
- Uniform page selection and uniform physical-edge selection are essential.
  Nonuniform page weights generally destroy count lumpability; nonuniform edge
  weights alter both coefficients.
- `J` counts common-spine flips, not generic sign flips.

### 6.8 BTB residual-value decision

After all direct-owner subtraction, the following remains a coherent
special-carrier theorem package:

1. the exact one-dimensional triangular-book transition law;
2. the full bivariate `(T,J)` Chebyshev-rational transform with repaired small
   boundaries;
3. the quadratic mean and sharp count extremizers;
4. the affine spine-parity law and two-statistic inverse; and
5. a uniform block certificate for exponential absorption.

The package has at least two independent axes--the full joint transform and
the mean/parity inverse--rather than a single finite recurrence.  It is therefore
paper-sized enough for an **internal thin pass** even though the model itself,
its XOR representation, and its static carrier quotient are fully owned.

**Verdict: `PASS_OWNER_THIN`.**  A direct triangular-book law or a direct
specialization of an unexamined star-hypergraph exact theorem would immediately
change this to `KILL_DIRECT`.  Until another owner gate clears that possibility,
it stays `HOLD_EXTERNAL` and unnumbered.

## 7. Independent exact replay

The audit verifier is
[`verify_htm_btb_focused_audit.py`](verify_htm_btb_focused_audit.py).  It does
not import the Stage-1 verifier and uses only integers and
`fractions.Fraction`.  Its frozen output is
[`HTM_BTB_FOCUSED_AUDIT_VERIFICATION.txt`](HTM_BTB_FOCUSED_AUDIT_VERIFICATION.txt).

The replay checks:

- HTM literal mixed-radix leaf enumeration, seven exact time layers, two
  finite-resolvent transform points per profile, Bellman depth-area, time-one
  reconstruction, clock moments, unknown-time ambiguity, every fixed-multiset
  extremizer over the audited range, adjacent-swap signs, and `h=1/b_1=1`
  boundaries;
- BTB every literal nonzero bit state through `r=9`, full transform vectors at
  four rational `(z,u)` points through `r=20`, Bellman and Chebyshev recurrences,
  `r=1/r=2/z=0`, direct rational mean and parity systems through `r=60`, all
  inverse states through `r=300`, and the `r`-private absorption certificate.

```text
BTB Chebyshev elimination: 4416
BTB inverse/absorption certificate: 180600
BTB literal lumpability: 2026
BTB mean/parity/extrema: 3958
BTB r=1/r=2/z=0 boundaries: 278
HTM boundary cases: 27
HTM clock/area/inverse: 2732
HTM fixed-multiset extremizers: 4240
HTM literal layers/transform: 6672
PASS assertions=204949
```

This replay is falsification evidence for the formulas; it says nothing about
novelty.

## 8. Frozen claim ceilings

### HTM ceiling

Permitted internal claim:

> On a fixed level-homogeneous rooted tree with uniform leaf sampling, the
> meet-depth process has explicit nested-cylinder layers; one known positive
> layer recovers the branching profile; and expected depth-area has sharp
> fixed-multiset factor-order extremizers.

Forbidden inflation: new semigroup framework, new random-product method, new
generic absorption theorem, first study of random LCA/MRCA depth, or robust
unknown-time/nonuniform inverse.

### BTB ceiling

Permitted internal claim:

> Specializing the owned `p=1/3` triadic dynamics to the triangular book
> `B(3,r)=K_{1,1,r}` yields an exactly solvable count quotient with a joint
> absorption/spine-flip transform, sharp mean law, parity inverse, and explicit
> absorption certificate.

Forbidden inflation: new social-balance dynamics, new XOR/hyperedge duality,
new signed-book classification, first generic convergence result, or a theorem
for friendship/windmill graphs.

Both ceilings remain internal.  No paper assignment or release should occur
from this document alone.

## 9. Primary-source ledger

### HTM

1. Brown 2000: [arXiv full text](https://arxiv.org/abs/math/0006145),
   [journal DOI](https://doi.org/10.1023/A:1007822931408).
2. Brown 2004: [author-hosted full text](https://pi.math.cornell.edu/~kbrown/papers/toronto.pdf),
   [author publication ledger](https://pi.math.cornell.edu/~kbrown/publications.html).
3. Ayyer--Schilling--Steinberg--Thiéry:
   [arXiv full text](https://arxiv.org/abs/1401.4250),
   [journal DOI](https://doi.org/10.1142/S0218196715400081).
4. Rhodes--Schilling:
   [arXiv full text](https://arxiv.org/abs/1711.10689),
   [journal DOI](https://doi.org/10.1016/j.aim.2019.03.004).
5. Pang: [arXiv full text](https://arxiv.org/abs/1508.01570),
   [journal DOI](https://doi.org/10.1007/s10959-018-0834-0).
6. Nestoridi: [arXiv full text](https://arxiv.org/abs/1605.08339).
7. Björner: [Project Euclid/DOI full text](https://doi.org/10.1214/ECP.v14-1445).
8. Nestoridi--Nguyen: [arXiv full text](https://arxiv.org/abs/1912.06771).
9. Fuchs--Steel: [arXiv full text](https://arxiv.org/abs/2501.09270).

### BTB

1. Antal--Krapivsky--Redner 2005:
   [arXiv full text](https://arxiv.org/abs/cond-mat/0506476),
   [journal DOI](https://doi.org/10.1103/PhysRevE.72.036121).
2. Antal--Krapivsky--Redner 2006:
   [arXiv full text](https://arxiv.org/abs/physics/0605183),
   [journal DOI](https://doi.org/10.1016/j.physd.2006.09.028).
3. Istrate 2009: [arXiv full text](https://arxiv.org/abs/0811.0381),
   [journal DOI](https://doi.org/10.3233/FI-2009-0047).
4. Istrate--Bonchis--Marin:
   [author manuscript](https://arxiv.org/abs/1909.12353).
5. Sehrawat--Bhattacharjya:
   [arXiv full text](https://arxiv.org/abs/2206.08580),
   [journal DOI](https://doi.org/10.20429/tag.2022.090104).

## 10. Final gate statement

- **HTM: `PASS_OWNER_THIN / HOLD_EXTERNAL`.**  Correct, no direct special
  conjunction owner found, but generic ownership leaves a thin elementary
  residual.
- **BTB: `PASS_OWNER_THIN / HOLD_EXTERNAL`.**  Correct and internally
  paper-sized as a special-carrier exact-law package; the kernel and static
  quotient are explicitly zero-credit.
- **No `KILL_DIRECT` and no theorem `REPAIR` at this gate.**  The BTB `r=2`
  cancellation, BTB `z=0` continuation, HTM known-time condition, and carrier
  terminology are mandatory statement repairs already incorporated into this
  frozen ceiling.
- No claim in this audit should be read as novelty, priority, or permission to
  draft or release.
