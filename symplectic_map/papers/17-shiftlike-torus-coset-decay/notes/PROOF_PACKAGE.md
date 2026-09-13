# Proof Package

## 0. Purpose and dependency declaration

This document gives a complete author proof of the two proposed main theorems.
The only indispensable external theorem is Laurent's qualitative
Mordell--Lang theorem for subvarieties of algebraic tori and division groups.
All character, independence, sharpness, support-phase, and scalar-compatibility
arguments are proved here.

No computation, CAS output, finite sampling, or experimental evidence is used.

## 1. Exact setup

Let `Omega` be an algebraically closed field of characteristic zero. Fix

`k>=2`, `1<=nu<=k-1`, and `a in Omega*`.

For a polynomial `P in Omega[X]`, define

`S(z_1,...,z_k)=(z_2,...,z_k,P(z_{k-nu+1})+a z_1)`.

With zero-based scalar coordinates, a state at time `n` is

`(x_n,...,x_{n+k-1})`,

and the scalar recurrence is

`x_{n+k}=P(x_{n+k-nu})+a x_n`.                                      (1.1)

For `m>=0`, let `V_m=V_m(S)` be the closed subvariety of
`(G_m)^(k+m)` with coordinates `x_0,...,x_{k+m-1}` and equations

`F_n:=x_{n+k}-P(x_{n+k-nu})-a x_n=0`, `0<=n<m`.                       (1.2)

Set `V_0=(G_m)^k`.

If `K` is any characteristic-zero field, `S` is defined over `K`, and
`Gamma<=K*`, define

`T_m(S,Gamma)={z in Gamma^k:S^j(z) in Gamma^k for 0<=j<=m}`.          (1.3)

Every initial tuple determines all future scalar coordinates uniquely, so
projection to `x_0,...,x_{k-1}` is a bijection

`V_m intersect Gamma^(k+m) -> T_m(S,Gamma)`.                         (1.4)

This also checks that `m` is the number of equations/transitions.

## 2. Algebraic preliminaries

### Lemma 2.1: group-algebra singleton principle

Let `H` be a connected algebraic torus over `Omega`, let
`M=X*(H)` be its character lattice, and suppose

`sum_{i=1}^N c_i chi_i=0` in `Omega[M]`,

where `c_i in Omega*` and `chi_i in M`. After equal characters are collected,
the coefficient of every character is zero. In particular, no character can
occur in exactly one nonzero summand.

#### Proof

The coordinate ring of `H` is the group algebra `Omega[M]`. The characters
form its distinguished `Omega`-basis. Linear independence of this basis gives
the assertion. `square`

The same statement applies to a translated torus `xi H`: restricting the
ambient coordinate `x_i` gives

`x_i|_{xi H}=xi_i chi_i`,

where `xi_i in Omega*` and `chi_i in M`.

### Lemma 2.2: powers of a nontrivial character

If `chi in X*(H)` is nontrivial and
`0<e_1<...<e_s`, then

`1,chi^(e_1),...,chi^(e_s)`

are pairwise distinct.

#### Proof

The character lattice of a connected torus is a free abelian group. Thus
`chi^u=chi^v` implies `(u-v)chi=0`, hence `u=v`; and a positive power of
nontrivial `chi` cannot be trivial. `square`

### Lemma 2.3: ambient coordinates generate

If `H <= (G_m)^N` is a connected subtorus and `chi_i` is the restriction of
the `i`th ambient coordinate character, then the `chi_i` generate `X*(H)`.

#### Proof

Restriction of characters gives a surjection

`X*((G_m)^N)=Z^N -> X*(H)`.

Equivalently, the defining relation lattice of a connected subtorus is
saturated and `X*(H)` is the corresponding quotient. `square`

Consequently, if every `chi_i` is trivial, then `H` is zero-dimensional.

### Lemma 2.4: disconnected subgroup audit

Suppose `D` is a possibly disconnected algebraic subgroup of an ambient torus
and `xi D subset X`. Let `H=D^0`. Then `D` is a finite union of translates of
`H`, every corresponding translate is contained in `X`, and
`dim D=dim H`.

#### Proof

An algebraic group has finitely many connected components, each a translate of
the identity component. Containment of the union implies containment of every
component. `square`

Thus it suffices in every dimension argument to treat connected `H`; finite
component groups cannot hide a torsion character in `X*(H)`.

## 3. Laurent's theorem and the exact arithmetic scope

### External Theorem L: torus Mordell--Lang

Let `X` be a closed subvariety of a complex algebraic torus `G`, let
`Lambda <= G(C)` be finitely generated, and put

`Lambda^div={g in G(C):g^N in Lambda for some N>=1}`.

Then there are finitely many torus cosets `zeta_i H_i subset X` such that

`X intersect Lambda^div`

is the union of the sets

`(zeta_i H_i) intersect Lambda^div`.                                 (3.1)

This is the torus consequence of Laurent, *Equations diophantiennes
exponentielles*, Invent. Math. 78 (1984), 299--327,
DOI `10.1007/BF01388597`.

Only the following qualitative corollary is used.

### Corollary 3.1

If `X` contains no positive-dimensional torus coset, then
`X intersect Lambda^div` is finite.

#### Proof

Every `H_i` in (3.1) is zero-dimensional, so every displayed intersection is
finite, and there are finitely many of them. `square`

### Lemma 3.2: arbitrary finite rank, including infinite torsion

Let `Gamma` be an abelian group with

`rank(Gamma/Gamma_tor)=r<infinity`.

There is a finitely generated subgroup `Gamma_0<=Gamma` such that

`Gamma subset Gamma_0^div`.                                         (3.2)

#### Proof

Choose `gamma_1,...,gamma_r` whose images form a `Q`-basis of
`Gamma tensor_Z Q`, and set `Gamma_0=<gamma_1,...,gamma_r>`. For any
`gamma in Gamma`, some positive integer `N` makes the class of `gamma^N`
an integral combination of the classes of the `gamma_i`. Therefore

`tau=gamma^N prod_i gamma_i^(-n_i)`

is torsion for suitable integers `n_i`. If `tau` has order `M`, then

`gamma^(NM) in Gamma_0`.

This proves (3.2). The argument is elementwise and places no bound on torsion.
In particular, every root of unity lies in the division group of the identity,
so a subgroup containing `mu_infinity` is covered. `square`

### Lemma 3.3: arbitrary characteristic-zero fields

Let `K` be any characteristic-zero field, let `X` be a torus subvariety defined
by finitely many coefficients in `K`, and let `Gamma<=K*` have finite rank.
If `X_Omega` contains no positive-dimensional torus coset over an algebraic
closure `Omega` of `K`, then `X intersect Gamma^N` is finite.

#### Proof

Choose `Gamma_0` as in Lemma 3.2. Let `L` be the subfield of `Omega` generated
over `Q` by the finitely many defining coefficients of `X` and the finitely
many generators of `Gamma_0`. Then `L` is finitely generated over `Q` and
admits an embedding into `C`. Every element of `Gamma` is algebraic over `L`
because some positive power belongs to `Gamma_0`. Extend the embedding of `L`
to an embedding of an algebraic closure of `L` into `C`.

Under this embedding, all points of `X intersect Gamma^N` lie in the division
group of the finitely generated group `Gamma_0^N`. Geometric absence of a
positive-dimensional coset is preserved by field embedding. Corollary 3.1
therefore gives finiteness, and injectivity of the embedding returns finiteness
over `K`. `square`

This is why Laurent remains the only external proof theorem. No embedding of
the entire, possibly very large field `K` into `C` is asserted.

## 4. Part A: anchored torus-coset decay

Assume throughout this section that

`P(X)=c+sum_{j=1}^s b_j X^(e_j)`,                                   (4.1)

with

`0<e_1<...<e_s`, `a,c,b_j in Omega*`, and `s>=2`.

### Theorem A

For every `0<=m<=k`, every connected torus coset

`xi H subset V_m`

satisfies

`dim H<=k-m`.                                                        (4.2)

If `a=1` and `P(1)=0`, a saturated subtorus of dimension `k-m` is
contained in `V_m` for every `0<=m<=k`.

### Proof of the upper bound

Fix `xi H subset V_m`, put `M=X*(H)`, and write

`x_i|_{xi H}=xi_i chi_i`, `chi_i in M`.                              (4.3)

For a fixed equation index `0<=n<m`, put

`t=k+n-nu`.

Restriction of `F_n=0` to `xi H` gives the group-algebra identity

`xi_{n+k} chi_{n+k} - a xi_n chi_n - c`

` - sum_{j=1}^s b_j xi_t^(e_j) chi_t^(e_j)=0`.                       (4.4)

#### Step A1: the middle character is trivial

Suppose `chi_t!=1`. By Lemma 2.2, the constant character and the `s` power
characters

`1,chi_t^(e_1),...,chi_t^(e_s)`

are `s+1>=3` distinct characters. The two endpoint terms in (4.4) can match at
most two of them. At least one constant-or-power character is therefore a
singleton with a nonzero coefficient. Lemma 2.1 gives a contradiction. Hence

`chi_{k+n-nu}=1`.                                                    (4.5)

This is the group-algebra singleton step. It uses both `c!=0` and `s>=2`.

#### Step A2: the `P(xi)` zero/nonzero split

After (4.5), collect all polynomial terms in (4.4):

`xi_{n+k} chi_{n+k}-a xi_n chi_n-P(xi_t)=0`.                         (4.6)

If `P(xi_t)!=0`, the nonzero trivial-character term in (4.6) forces

`chi_n=chi_{n+k}=1`.                                                 (4.7)

Indeed, if the endpoint characters are unequal, at least one is a singleton;
if they are equal and nontrivial, the trivial character is a singleton.

If `P(xi_t)=0`, (4.6) has two nonzero terms, so

`chi_{n+k}=chi_n` and `xi_{n+k}=a xi_n`.                             (4.8)

Thus both branches imply the two character relations

`chi_{k+n-nu}=1`, `chi_{k+n}=chi_n`.                                (4.9)

The scalar equality in (4.8) is recorded even though the dimension bound needs
only the character equality.

#### Step A3: independence of all `2m` lattice relations

Let `epsilon_0,...,epsilon_{k+m-1}` be the standard basis of
`Z^(k+m)`, and let

`phi:Z^(k+m)->M`, `epsilon_i |-> chi_i`.

For `0<=n<m`, (4.9) places in `ker(phi)` the vectors

`A_n=epsilon_{k+n-nu}`,                                              (4.10)

`B_n=epsilon_{k+n}-epsilon_n`.                                      (4.11)

We prove that the `2m` vectors `A_n,B_n` are independent over `Z`.

The `A_n` have distinct pivot indices in the interval

`I=[k-nu,k+m-1-nu]`,                                                 (4.12)

which has `m` elements and span `m-1<=k-1`. The endpoint pairs

`{n,k+n}`, `0<=n<m`,                                                 (4.13)

are pairwise disjoint: all low endpoints are below `m<=k`, all high endpoints
are at least `k`, and different `n` give different endpoints. No pair (4.13)
can lie wholly in `I`, because its two entries differ by `k`, while the span
of `I` is at most `k-1`.

In any relation

`sum_n u_n A_n + sum_n v_n B_n=0`,                                  (4.14)

choose, for each `B_n`, an endpoint outside `I`. That coordinate appears in no
`A_j` and in no other `B_j`, so its coefficient in (4.14) is `v_n` or
`-v_n`. Hence every `v_n=0`. The distinct pivots then give every `u_n=0`.
This proves independence integrally, not merely over `Q`.

It follows that

`rank(im phi)<=k+m-2m=k-m`.                                         (4.15)

By Lemma 2.3, `im(phi)=M`, so `dim H=rank M<=k-m`.

#### Step A4: future-character generation and the no-gcd audit

The same relations give a useful transparent check. Every future character is
a copy of an initial one:

`chi_{k+n}=chi_n`, `0<=n<m`.                                        (4.16)

Therefore the initial characters generate `M`. The middle relation (4.5)
kills the initial character with residue

`r_n=n-nu mod k`.                                                    (4.17)

For `n<nu`, this is the initial index `k+n-nu`; for `n>=nu`, the middle
coordinate is future and (4.16) identifies it with initial index `n-nu`.
The set

`R_m={n-nu mod k:0<=n<m}`                                           (4.18)

has exactly `m` elements because translation modulo `k` is injective on any
interval of length at most `k`. This is not an orbit under repeated subtraction
of `nu`, and no value of `gcd(k,nu)` enters.

Steps A1--A4 prove (4.2). `square`

### Disconnected-coset extension

If `xi D subset V_m` with `D` possibly disconnected, apply the theorem to
each translate of `D^0` supplied by Lemma 2.4. Since
`dim D=dim D^0`, the same bound holds. This also shows that finite component
groups cannot evade the torsion-free character-lattice argument.

### Proposition 4.1: explicit saturated equality family

Assume `a=1` and `P(1)=0`. For `0<=m<=k`, let `R_m` be (4.18). Define
`H_m subset (G_m)^(k+m)` by

`x_r=1` for `r in R_m`,                                              (4.19)

`x_{k+n}=x_n` for `0<=n<m`,                                         (4.20)

with the initial coordinates outside `R_m` free. Then

`H_m subset V_m`, `H_m isomorphic to (G_m)^(k-m)`,

and its defining lattice is saturated.

#### Proof

Fix `0<=n<m`. If `n<nu`, then

`k+n-nu in R_m`

as an initial index, so `x_{k+n-nu}=1`. If `n>=nu`, (4.20) and (4.19) give

`x_{k+n-nu}=x_{n-nu}=1`.

Thus the `n`th recurrence is

`x_{k+n}=x_n=P(1)+x_n`,

and every defining equation of `V_m` holds.

Projection to the `k-m` initial coordinates outside `R_m` is an explicit
inverse to the monomial parameterization of `H_m`. On character lattices, the
ambient lattice maps surjectively to a free lattice with those `k-m` basis
elements; fixed coordinates map to zero and copied coordinates map to their
initial basis element. The kernel is therefore a direct summand, hence
saturated. The image is a connected subtorus of dimension `k-m`. `square`

The hypotheses `a=1,P(1)=0` are sufficient for equality, not claimed
necessary. For every prescribed collected support with `s>=2`, the choice
`b_j=1,c=-s` realizes `P(1)=0` in characteristic zero.

### Corollary 4.2: finite-rank window and sharpness

Let `K` be any characteristic-zero field, let the anchored sparse map be
defined over `K`, and let `Gamma<=K*` have arbitrary finite rank. Then

`T_k(S,Gamma)` is finite.                                             (4.21)

For every prescribed support and every `k,nu`, there are rational coefficients
and the rank-one group `Gamma=<2>` for which `T_{k-1}` is infinite.

#### Proof

At `m=k`, Theorem A excludes positive-dimensional torus cosets in `V_k`.
Lemma 3.3 and (1.4) give (4.21). If `m>=k`, then `T_m subset T_k`, so all
longer windows are finite as well.

For sharpness, use `a=1,b_j=1,c=-s` and Proposition 4.1 at `m=k-1`. The set
`R_{k-1}` contains every initial residue except

`q=k-1-nu`.                                                         (4.22)

Set `x_q=t`, set all other initial coordinates to `1`, and use (4.20) for the
future coordinates. For `t=2^N`, all coordinates lie in `Gamma=<2>`, and
distinct `N` give distinct initial states. Hence `T_{k-1}` is infinite.
`square`

## 5. Part B: local character partitions when `c=0`

Fix for the rest of the proof

`k=2`, `nu=1`,

and

`P(X)=sum_{e in E} b_e X^e`,                                        (5.1)

where `E` is a nonempty finite subset of positive integers and every `b_e` is
nonzero. The recurrence is

`x_{n+2}=P(x_{n+1})+a x_n`,                                         (5.2)

and `V_m^0 subset (G_m)^(m+2)` is cut out by (5.2) for `0<=n<m`.

Let `xi H subset V_m^0`, put `M=X*(H)`, and write

`x_i=xi_i chi_i` on the coset. In additive notation for `M`, write
`u_i` for `chi_i`. The `n`th local identity is

`xi_{n+2}[u_{n+2}]-a xi_n[u_n]`

`-sum_{e in E}b_e xi_{n+1}^e[e u_{n+1}]=0` in `Omega[M]`.            (5.3)

Here brackets only emphasize a group-algebra basis character.

### Lemma 5.1: trivial-middle and root-copy branches

Suppose `u_{n+1}=0`.

1. If `P(xi_{n+1})!=0`, then `u_n=u_{n+2}=0`.
2. If `P(xi_{n+1})=0`, then

   `u_{n+2}=u_n` and `xi_{n+2}=a xi_n`.                              (5.4)

#### Proof

All middle terms aggregate at the trivial character, reducing (5.3) to

`xi_{n+2}[u_{n+2}]-a xi_n[u_n]-P(xi_{n+1})[0]=0`.

If the last coefficient is nonzero, the singleton principle forces both
endpoint characters to be trivial. If it is zero, the two endpoint terms must
have the same character and cancel scalarly. `square`

We call the character relation

`A: u_{n+1}=0, u_{n+2}=u_n`                                         (5.5)

the trivial-middle label. A nonzero endpoint in an `A` label necessarily lies
in the root-copy subcase (5.4); when all characters are trivial, the scalar
equation need not be a root-copy unless the middle scalar is a root. This split
will not be suppressed.

## 6. Complete support analysis in the plane

### 6.1 Linear support `E={1}`

Let `P(X)=beta X`. Choose a root `r` of

`r^2=beta r+a`.                                                      (6.1)

Since `a!=0`, every root is nonzero. For every `m>=0`, define

`L_{r,m}={(t,rt,...,r^(m+1)t):t in G_m}`.                            (6.2)

Each recurrence reads

`r^(n+2)t=beta r^(n+1)t+a r^n t`,

so `L_{r,m} subset V_m^0`. It is a translate of the diagonal one-dimensional
subtorus. Hence no finite geometric window exists for linear support.

This can be arithmetically compatible: take `beta=2,a=-1`, so `r=1`, and
`Gamma=<2>`. Then the constant scalar chains `(t,...,t)`, `t=2^N`, lie in
every `T_m`.

### 6.2 Nonlinear monomial support `E={d}`, `d>=2`

If `u_{n+1}=0`, the nonzero monomial coefficient in (5.3) and Lemma 2.1 force
both endpoint characters to be zero. If `u_{n+1}!=0`, the three nonzero terms
in (5.3) can have no singleton only when all three characters agree:

`u_{n+2}=u_n=d u_{n+1}`.                                            (6.3)

For two consecutive equations, a nontrivial branch would give

`u_2=u_0=d u_1`,

`u_3=u_1=d u_2`.

Thus `(d^2-1)u_1=0`. The lattice `M` is torsion-free and `d>=2`, so
`u_1=0`, and then all four coordinate characters are zero. By Lemma 2.3,
`V_2^0` contains no positive-dimensional torus coset.

This is a finite-window phase, not a no-finite-window exception.

### 6.3 Supports of size at least three

Assume `|E|>=3`. If `u_{n+1}!=0`, the characters

`e u_{n+1}`, `e in E`,

are pairwise distinct. The two endpoints can match at most two of them, so at
least one middle term is a singleton. Hence every local equation forces

`u_{n+1}=0`.                                                        (6.4)

In `V_2^0`, the two local equations give `u_1=u_2=0`. The first equation then
forces `u_0=0` and the second forces `u_3=0`, using Lemma 5.1 or directly the
singleton principle. Thus all coordinate characters are trivial and
`V_2^0` has no positive-dimensional torus coset.

This argument includes every pattern of scalar root cancellation: if the first
equation is a root-copy, then `u_2=u_0`; the second equation independently
forces its middle character `u_2` to be zero, hence also `u_0=0`. There is no
free root-copy branch left unclosed.

### 6.4 Binomial support and all two-term orientations

Let

`E={p,q}`, `1<=p<q`,

and write

`P(X)=b_p X^p+b_q X^q`.                                             (6.5)

Fix one local equation and put `u=u_{n+1}`.

If `u=0`, Lemma 5.1 gives label `A` in (5.5), with the explicit
`P(xi)=0/P(xi)!=0` scalar split already recorded.

Suppose `u!=0`. Then `p u` and `q u` are distinct. In the four-term identity
(5.3), a partition with no singleton must pair each endpoint with one distinct
middle character. This is exhaustive: an endpoint-endpoint pair would leave
both distinct middle characters single, and a block containing only one middle
character is also forbidden. There are exactly two orientations:

`B: u_n=p u, u_{n+2}=q u`,                                          (6.6)

`C: u_n=q u, u_{n+2}=p u`.                                          (6.7)

The scalar cancellations are part of the labels, not postponed:

- for `B`,

  `a xi_n=-b_p xi_{n+1}^p`,

  `xi_{n+2}=b_q xi_{n+1}^q`;                                       (6.8)

- for `C`,

  `a xi_n=-b_q xi_{n+1}^q`,

  `xi_{n+2}=b_p xi_{n+1}^p`.                                       (6.9)

Equations (6.6)--(6.9) cover all nontrivial group-algebra partitions, including
both endpoint-to-power orientations.

#### Two-label transition audit

Any adjacent word containing `A` has only the zero character solution:

- `A A`: the first label gives `u_1=0,u_2=u_0`; the second gives
  `u_2=0,u_3=u_1`, hence every `u_i=0`;
- `A B` or `A C`: the second label requires nonzero middle `u_2`, but its lag
  `u_1` is a positive multiple of `u_2`, contradicting `u_1=0`;
- `B A` or `C A`: the second label requires middle `u_2=0`, contradicting the
  nonzero output of the first label.

For the four nontrivial words, take `u_1!=0` and use torsion-freeness:

| Word | Compatibility equation | Nonzero possibility |
|---|---|---|
| `B B` | `u_1=p u_2=pq u_1` | requires `pq=1`, impossible |
| `B C` | `u_1=q u_2=q^2 u_1` | requires `q^2=1`, impossible |
| `C B` | `u_1=p u_2=p^2 u_1` | requires `p^2=1`, hence `p=1` |
| `C C` | `u_1=q u_2=pq u_1` | requires `pq=1`, impossible |

Therefore the unique nonzero two-equation character word is

`C B` with support `{1,d}`, d=q>=2`.                                (6.10)

This proves immediately that every binomial `{p,q}` with `p>=2` has no
positive-dimensional torus coset in `V_2^0`.

## 7. The unique `{1,d}` resonance

Write

`P(X)=beta X+delta X^d`, `d>=2`.                                    (7.1)

For the word `C B`, let the first middle character be `u=u_1!=0`. The
character vector is forced to be

`(u_0,u_1,u_2,u_3)=(d u,u,u,d u)`.                                  (7.2)

### Scalar compatibility

The first label is `C`. Equations (6.9) give

`a xi_0=-delta xi_1^d`,

`xi_2=beta xi_1`.                                                    (7.3)

The second label is `B`. Equations (6.8) give

`a xi_1=-beta xi_2`,

`xi_3=delta xi_2^d`.                                                 (7.4)

Substituting `xi_2=beta xi_1` into (7.4), and using `xi_1!=0`, yields the
necessary coefficient condition

`a=-beta^2`.                                                        (7.5)

On this locus, (7.3)--(7.4) give

`xi_0=(delta/beta^2)xi_1^d`,

`xi_2=beta xi_1`,

`xi_3=delta beta^d xi_1^d`.                                         (7.6)

Therefore every positive-dimensional connected coset in `V_2^0` is contained
in

`C_d={((delta/beta^2)t^d,t,beta t,delta beta^d t^d):t in G_m}`.      (7.7)

Conversely, direct substitution shows that (7.7) is contained in `V_2^0` when
`a=-beta^2`:

`beta t+delta t^d-beta^2(delta/beta^2)t^d=beta t`,

`beta(beta t)+delta(beta t)^d-beta^2 t=delta beta^d t^d`.

The character vector (7.2) shows that all ambient coordinate characters lie in
the cyclic subgroup generated by `u`. Since ambient characters generate
`X*(H)`, any positive-dimensional `H` has dimension one. A nonzero character
of a one-dimensional torus is surjective over `Omega`; hence `t=x_1` ranges
over all of `G_m`, and the coset is exactly `C_d`, not a proper
positive-dimensional subcoset. Thus `C_d` is the unique connected
positive-dimensional torus coset in `V_2^0`.

Off (7.5), the only possible nonzero character word fails its scalar
compatibility, so `V_2^0` has no positive-dimensional torus coset.

### Third-equation closure

On the `C B` word, the first four characters are

`(d u,u,u,d u)`, `u!=0`.

For a third label with middle `u_3=d u` and lag `u_2=u`:

- label `A` is impossible because its middle must be zero;
- label `B` would require `u_2=u_3`, hence `(d-1)u=0`;
- label `C` would require `u_2=d u_3=d^2u`, hence `(d^2-1)u=0`.

All are impossible in a torsion-free lattice for `d>=2`. If the first four
characters are already zero, the third local identity forces `u_4=0` as well.
Therefore

`V_3^0 contains no positive-dimensional torus coset`                    (7.8)

for `{1,d}` support, including the resonant locus.

Combining Sections 6 and 7 also gives (7.8) for every nonlinear support: for
monomial, size-at-least-three, nonresonant binomial, or binomial with `p>=2`,
the first two equations make `u_0,...,u_3` trivial and the third makes `u_4`
trivial.

## 8. Exact zero-constant phase theorem

### Theorem B

Let `a!=0` and let `P` have actual positive-exponent support `E` as in (5.1).

1. If `E={1}`, every `V_m^0` contains the one-dimensional coset (6.2).
2. If `E={1,d}`, `d>=2`, then `V_2^0` contains a positive-dimensional
   connected torus coset if and only if `a=-beta^2`; on that locus the unique
   coset is `C_d` in (7.7). Every `V_3^0` has no positive-dimensional coset.
3. For every other nonlinear support, `V_2^0` has no
   positive-dimensional torus coset.

#### Proof

Section 6.1 proves (1). Sections 6.2--6.4 exhaust respectively nonlinear
monomials, supports of size at least three, and binomials. Section 7 proves the
unique binomial exception and its third-step closure. These cases exhaust all
finite nonempty actual supports in the positive integers. `square`

### Corollary 8.1: arithmetic windows

Let `K` be any characteristic-zero field and let `Gamma<=K*` have arbitrary
finite rank, including arbitrary infinite torsion.

- For every nonlinear support other than a resonant `{1,d}` support,
  `T_2(S,Gamma)` is finite.
- On the resonant `{1,d}` locus, `T_3(S,Gamma)` is finite.

#### Proof

Apply Lemma 3.3 to `V_2^0` or `V_3^0` using Theorem B, then use the bijection
(1.4). `square`

These are qualitative finiteness statements. Laurent supplies no explicit
cardinality or enumeration here.

## 9. Sharp examples and geometric/arithmetic separation

### 9.1 Resonant `T_2` infinitude is compatible, not universal

Take

`beta=delta=1`, `a=-1`, `Gamma=<2>`.

For `t=2^N`, the scalar tuple

`(x_0,x_1,x_2,x_3)=(t^d,t,t,t^d)`                                  (9.1)

lies on `C_d` and hence gives infinitely many points of `T_2`. This demonstrates
sharpness of the third transition on a compatible finite-rank group.

For a different fixed `Gamma`, the intersection `C_d intersect Gamma^4` may be
finite or empty. The geometric theorem alone never asserts otherwise.

### 9.2 Nonlinear monomial `T_1` family: orientation audit

Take `P(X)=X^e`, `e>=2`, `a=1`, and `Gamma=<2>`. For `t=2^N`, use

`(x_0,x_1,x_2)=(t^e,t,2t^e)`.                                      (9.2)

Indeed,

`x_2=P(x_1)+a x_0=t^e+t^e=2t^e`.

The tuple `(t,t^e,2t^e)` would not satisfy the displayed recurrence in
general; (9.2) explicitly corrects that earlier orientation drift.

### 9.3 Every prescribed multi-support has infinite `T_1`

Let `E` have size `s>=2`. Choose nonzero rational coefficients with
`sum_{e in E}b_e=0`; for example, set the first `s-1` coefficients to `1` and
the last to `-(s-1)`. Then `P(1)=0`. With `a=1`, `Gamma=<2>`, and `t=2^N`,

`(x_0,x_1,x_2)=(t,1,t)`                                             (9.3)

satisfies the recurrence. Thus the two-transition finiteness away from the
resonance is coefficient-uniformly sharp at one transition.

### 9.4 Linear all-window family

The choice `P(X)=2X`, `a=-1`, `Gamma=<2>` gives the constant chain
`x_n=t=2^N` for all `n`. This is a compatible arithmetic witness for the
geometric no-finite-window linear phase.

## 10. Paper16 overlap and non-absorption proof audit

Paper16 treats only `k=2` generalized Henon maps with `c!=0` and proves:

- for actual nonconstant support `s>=2`, an explicit cardinality bound for
  `T_2` and rank-one `T_1` sharpness; and
- for support one, an explicit `T_4` bound and rank-one `T_3` sharpness, fully
  absorbing its own predecessor.

The `k=2,m=2` specialization of Theorem A merely says that `V_2` contains no
positive-dimensional torus coset and, via Laurent, that `T_2` is finite. It is
strictly weaker than Paper16's explicit count and is not presented as an
improvement. Paper17 does not reproduce or absorb Paper16's quantitative proof.

The genuinely new axes are:

- all dimensions `k`, all standard types `nu`, and the exact profile
  `dim H<=k-m` for every `0<=m<=k`;
- a saturated equality family at every window;
- the arbitrary-`k` sharp finite-rank threshold `k/(k-1)`; and
- the complete `c=0` planar geometric phase, including the exact resonance
  locus and third-step closure.

## 11. Counterexample and scope audit

The proofs above have been tested against the following possible failure modes.

| Failure mode | Resolution |
|---|---|
| `P(xi_t)=0` might destroy a Part A relation | It changes endpoint killing to the copy relation (4.8); both `A_n` and `B_n` remain. |
| The `2m` relations might overlap | The interval/pair argument in Step A3 proves integral independence. |
| A future middle coordinate might not kill an initial character | Equation (4.16) copies it to residue `n-nu mod k`. |
| `gcd(k,nu)>1` might reduce the number killed | The killed set is a translation of `m` consecutive residues, not a rotation orbit. |
| Equality might define a nonconnected image | The parameter lattice map is surjective with saturated kernel. |
| Infinite torsion might escape Laurent | Every torsion element is in the division hull; Lemmas 3.2--3.3 are explicit. |
| A root-copy might survive two `c=0` equations | It is closed explicitly in the size-at-least-three and `A`-transition audits. |
| A four-term partition might be omitted | `A`, `B`, and `C` exhaust trivial-middle and both nontrivial pair orientations. |
| Another binomial resonance might occur | The four-word table leaves only `C B` and forces `p=1`; scalar equations force only `a=-beta^2`. |
| `C_d` might be only one of several translates | Every surviving scalar and character is forced by (7.2)--(7.6), and the middle character is surjective. |
| The resonance might extend to `V_3` | The third label contradicts `d>=2` in every case. |
| The monomial sharp tuple might be transposed | Direct substitution fixes the order as `(t^e,t,2t^e)`. |

Excluded from the theorem are positive characteristic, `a=0`, negative
Laurent exponents, rational maps, arbitrary polynomial automorphisms, affine-
conjugacy invariance of support, height bounds, periodic classifications, and
effective enumeration.

## 12. Proof-stage conclusion

All internal proof obligations are closed at author level:

- exact `V_m` and `T_m` orientation;
- group-algebra singleton;
- full `P(xi)` split;
- integral independence of `2m` relations;
- future-character generation and no-gcd bookkeeping;
- disconnected components;
- saturated equality and rank-one sharpness;
- arbitrary fields, finite rank, division groups, and infinite torsion;
- all `c=0` support partitions and scalar orientations;
- unique `{1,d}` resonance and exact `C_d`;
- third-step closure; and
- Paper16 non-overclaim.

**AUTHOR PROOF STATUS: COMPLETE / PENDING INDEPENDENT SOURCE REVIEW.**
