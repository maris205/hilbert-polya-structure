# Slot-14 S14-C2 rank-two common-quotient fail-fast

Date: 2026-08-16  
Scope: independent mathematical, source-owner, and standalone precheck only  
Candidate: `S14-C2`  

```text
MATHEMATICS                     = PASS
SOURCE_STATUS                   = SOURCE_FEASIBLE_AT_COMPACT_CHART_OWNER
SOURCE_MAP_OWNER                = PASS_WITH_DERIVED_CHART_CEILING
DIRECT_SOURCE_EXACT_PACKAGE     = false
FINDINGS                        = C0/M1/m0
FULL_PAPER                      = NO
DISPOSITION                     = MERGE_P15R / STOP_SLOT14
NEXT_BATCH_ACTION               = retain only a P15R common-quotient/Smith corollary;
                                  create no Slot-14 protocol, proof, controls, Route,
                                  manuscript, or Git action
```

The one major finding is standalone, not mathematical: after the maximum
P15R subtraction, the two-prime answer is one Smith minimum attached to a
formal cokernel.  The finite-set extension replaces that minimum by the
Smith invariant factors of the same incidence matrix.  No additional
relative Ulm tail and no nonformal functorial theorem survive.  The binding
batch fail-fast therefore requires `MERGE_P15R / STOP_SLOT14` even though the
candidate mathematics closes.

## 1. Authorities and review discipline

The following frozen records were rehashed and read in full before this
precheck.

| Record | SHA-256 | Use here |
|---|---|---|
| Papers 14--18 batch design lock | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | original slot and nonredundancy rules |
| batch amendment v1 | `afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802` | one-technical-note and replacement rules |
| batch amendment v2 | `3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b` | fail-fast authority |
| replacement screen v3 | `9d46719c7c84e4c3809d40d997ed31a802ec0506a2385f8a5a6c3be4afb9c8b2` | unique `HOLD S14-C2` theorem signature and hard merge gate |
| P15R protocol | `02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a` | rank-one scope and gates |
| P15R amendment v1 | `2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc` | off-local Kummer and exceptional-primary split |
| P15R amendment v2 | `386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80` | typed kernel absorption and full-ledger obligations |
| P15R final source/precedent audit | `287bba68fa191a1971c6c060b7eae43bf2ca2f02cbf64f6dfb8959d5c546de97` | exact source ceilings and bounded negative search |
| P15R methodology/devil review | `5af721d6a0ba05731ce2e18397e006b87ef90f327a9edd931c171ad6b889f1ae` | arrow typing, hidden-height, and nonredundancy attacks |
| P15R final gate | `949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd` | current authorized ceiling |

The current P15R symbolic proof ledger was also read in full at
`7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355`
as a subtraction surface, not promoted above the frozen authorities.  Its
independent exact-byte peer review was then read in full at
`2b889ba09b95b3d97be62780f026e4a9e3de58379eb9abb8c720c8b6cd792cc7`;
that review freezes `PASS C0/M0/m0` on the P15R proof.  The ledger already
contains the rank-one local logarithm, the exact bounded saturation away
from the owner prime, the exceptional-primary absorption lemma, the
internal-root proof, the complete Ulm ledger, reducedness, and the Kiehlmann
classification step.  The later P15R proof PASS strengthens, rather than
relaxes, the maximum-subtraction requirement applied here.

The complete ARS academic-research-suite instructions were applied together
with the complete deep-research workflow, source-verification agent,
source-quality hierarchy, deep-research devil's advocate, academic-paper
review workflow, methodology reviewer, domain reviewer, reviewer devil's
advocate, and review-quality/nonredundancy rules.  In particular, primary
bytes outrank internal audit prose; a negative bounded search is not a
priority claim; and mathematical correctness is separated from standalone
paper weight.

## 2. Notation and exact source-owner ceiling

Put

```text
A   = Zhat^x = product_l Z_l^x,
U_p = product_(l != p) Z_l^x,
e_p : Zhat -> U_p,                 n |-> p^n,
H_p = im(e_p),
B_p = U_p/H_p.
```

Let `pi_p:A->U_p` drop the `p` coordinate and define

```text
beta_p = (U_p -> B_p) o pi_p,
K_p    = ker(beta_p).
```

Deninger v4, equations (32), (34)--(40), directly owns the finite-field
root-of-unity construction, `U_p`, the Frobenius subgroup `p^Zhat`, the
compact quotient `B_p`, the choice-dependent set bijections/fibration, and
the canonical time projection.  The paragraph immediately after (39)
expressly says that the displayed charts and fibration depend on the choices
`x` and `iota`.  It does **not** state a simultaneous family `beta_p`, the
two-prime cokernel below, a topology identification with the actual packet
orbit quotient, or an Ulm classification.

The earlier source-transition calculation derives from those explicit
formulas that replacing the common root-of-unity injection by
`iota o ( )^epsilon`, `epsilon in A`, translates the `p`-chart by the class
of `pi_p(epsilon)` in `B_p` (up to the harmless inverse convention).  A
change of the residue point adds the cyclotomic character, and equation (34)
kills the decomposition-group ambiguity modulo `p^Zhat`.  Consequently the
family `(beta_p)_p` is induced by a **common source choice transition**.  It
is not a family of arbitrarily selected homomorphisms.

This passes the bare-owner attack only in the following precise sense:

```text
SOURCE_STATED_OWNER       = compact B_p presentation and choice-dependent charts
SOURCE_FORMULA_DERIVATION = simultaneous common-iota translation maps beta_p
NOT_LICENSED              = actual packet quotient topology, canonical base point,
                            or a source-stated rank-two theorem
```

All conclusions below therefore concern the compact group/source-chart
owner.  They are not silently transported to the actual indiscrete packet
orbit topology.

## 3. Formal common quotient: exact sequence and away-coordinate model

The map `beta_p` is onto and

```text
K_p = {a in A : pi_p(a)=p^n for some n in Zhat},
B_p ~= A/K_p.
```

All these kernels are closed.  For distinct rational primes `p,q`, define

```text
beta_pq = (beta_p,beta_q):A -> B_p x B_q,
C_pq    = coker(beta_pq).
```

### 3.1 Exact sequence

In multiplicative notation set

```text
delta:B_p x B_q -> A/(K_p K_q),
delta(aK_p,bK_q)=ab^(-1)K_pK_q.
```

This is well-defined and onto.  If `ab^(-1)=k_pk_q`, then
`c=ak_p^(-1)=bk_q` satisfies

```text
(aK_p,bK_q)=(cK_p,cK_q),
```

so the kernel is exactly the diagonal image.  Conversely every diagonal
element is killed.  Thus there is a topologically exact sequence

```text
0 -> A/(K_p cap K_q)
  -> B_p x B_q
  -> C_pq
  -> 0,                                                    (3.1)

C_pq ~= A/(K_pK_q),
beta_pq(A)=B_p x_(C_pq) B_q.                              (3.2)
```

Products of the compact subgroups `K_p,K_q` are compact and hence closed;
all algebraic quotients in (3.1)--(3.2) are therefore Hausdorff compact
quotients, not merely abstract cokernels.

### 3.2 Dropping the two owner coordinates

Put

```text
U_pq = product_(l notin {p,q}) Z_l^x,
e_pq:Zhat^2 -> U_pq,              (n,m) |-> p^n q^m,
H_pq=im(e_pq),
rho_pq:A->U_pq.
```

The exact preimage identity is

```text
rho_pq^(-1)(H_pq)=K_pK_q.                                (3.3)
```

Indeed a product from `K_pK_q` has away coordinates `p^nq^m`.  Conversely,
if the away coordinates of `a` are `p^nq^m`, take the exponent-`n` element
of `K_p` and the exponent-`m` element of `K_q`; their free `p` and `q`
coordinates can be chosen respectively as `a_p q^(-m)` and
`a_q p^(-n)`.
Their product is `a`.  The kernel of `rho_pq` is already contained in
`K_pK_q`.  The compact first-isomorphism theorem now gives

```text
C_pq ~= A/(K_pK_q) ~= U_pq/H_pq.                          (3.4)
```

No injectivity assumption on `e_pq` was used in the formal identity (3.4).
Injectivity is proved next.

## 4. The simultaneous exponent map is a closed embedding

The map `e_pq` is continuous.  It suffices to prove injectivity on every
pro-`r` component `Z_r^2`, because both source and target are abelian
profinite groups with canonical primary decompositions.

### 4.1 A direct reduction witness at every prime, including `r=p,q,2`

Perucca, arXiv:0909.4806, Theorem 14 applies to

```text
G_1=G_2=G_m,
R=(p,q) in G_m^2(Q).
```

The smallest algebraic subgroup containing `R` is the full torus: a proper
subtorus or a translate component would give a relation
`p^a q^b` equal to a root of unity, and the valuations at `p` and `q` force
`a=b=0`.  Hence the connected-owner condition in that theorem is automatic.
For every prime `r` and every `m>=1`, there are therefore infinitely many
rational primes `l`, outside any fixed finite forbidden set, having either

```text
(v_r(ord_l(p)),v_r(ord_l(q)))=(m,0)                       (4.1)
```

or

```text
(v_r(ord_l(p)),v_r(ord_l(q)))=(0,m).                      (4.2)
```

Let `(x,y) in Z_r^2` be in the pro-`r` kernel.  At a prime satisfying
(4.1), project `F_l^x` to its `r`-Sylow.  The reduction of `p` has exact
order `r^m`, while the reduction of `q` has trivial `r`-part.  Thus
`x in r^mZ_r`.  A prime satisfying (4.2) similarly gives
`y in r^mZ_r`.  Since this holds for every `m`, `(x,y)=0`.

This argument is valid without change for `r=p` and `r=q`: all witness
primes may be chosen away from `p,q`.  It is also valid for `r=2`, including
the cases `p=2` or `q=2`.

### 4.2 Kummer cross-check and the root-of-unity firewall

Debry--Perucca, arXiv:1312.6620v2, Sections 2--4, Definition 8, Lemma 9,
Theorem 17, and Example 21 provide a compatible Kummer check.  For odd `r`,
the valuation vectors of `p,q` make them strongly `r`-independent: if an
exponent vector is not in `rZ^2`, its valuation at `p` or `q` is not
divisible by `r`; the rational `r`-power roots of unity introduce no hidden
relation.  In Theorem 17's stated odd-`r` cyclotomic range, Example 21
therefore gives the full rank-two Kummer degree.  Chebotarev then
cross-checks separation of every nonzero finite `r`-power functional,
including when `r=p` or `r=q`.  The all-prime exact reduction-order witnesses
actually used in Section 4.1 remain solely the specialization of Perucca's
Theorem 14.

There is a genuine `2`-adic guard.  If `p,q` are odd, they remain strongly
`2`-independent over `Q(i)` because an odd valuation at a prime above `p` or
`q` cannot be repaired by any of `+-1,+-i`.  If one owner prime is `2`, that
uniform base-change argument is forbidden: for example

```text
2i=(1+i)^2 in Q(i).                                       (4.3)
```

Thus this precheck does **not** claim a false uniform full-degree Kummer
lemma at the owner `2`.  The direct Perucca-Theorem-14 reduction witness in
Section 4.1 proves exactly the needed injectivity there.

### 4.3 Closedness

Every pro-primary kernel is zero, hence `e_pq` is injective.  A continuous
injection from the compact group `Zhat^2` to the Hausdorff group `U_pq` is a
homeomorphism onto its compact image, and that image is closed.  Therefore

```text
e_pq:Zhat^2 -> U_pq is a closed topological embedding.     (4.4)
```

The claim includes, rather than suppresses, the branches `r=p`, `r=q`, and
`r=2`.

## 5. Exact rank-two bounded saturation away from the owners

The reduction-order witnesses of Section 4 prove embedding but do not by
themselves prove bounded character extension: if
`v_r(l-1)>m`, a faithful character on an order-`r^m` subgroup can require
ambient order greater than `r^m`.  The P15R regression example
`ord_17(2)=8`, `v_2(16)=4`, is exactly this warning.  The Ulm internal-root
argument below instead needs primes satisfying the two conditions

```text
v_r(l-1)=m
and an invertible rank-two reduction-log matrix modulo r.  (5.1)
```

These exist when `r notin {p,q}`.

### 5.1 Odd `r`

Let `F=Q(zeta_r)` and

```text
L=F(p^(1/r),q^(1/r)).
```

Because `r` differs from `p,q`, the valuations above `p,q` prove that the
Kummer classes of `p,q` are independent, so
`Gal(L/F)~=(Z/r)^2`.  Every nontrivial degree-`r` subextension is ramified
above `p` or `q`.  It therefore has trivial intersection over `F` with
`Q(zeta_(r^(m+1)))`, whose new ramification is only above `r`.

Choose an automorphism of the cyclotomic tower that fixes
`zeta_(r^m)` but not `zeta_(r^(m+1))`, and independently choose Kummer
characters with patterns `(nonzero,0)` and `(0,nonzero)`.  Qualitative
Chebotarev gives two rational primes.  They have
`v_r(l-1)=m`, and the two discrete-log rows of `p,q` are respectively
`(*,0)` and `(0,*)` modulo `r`.  Their determinant is an `r`-adic unit, so
the full matrix is invertible modulo `r^m`.

### 5.2 `r=2` away from the owners

Here `p,q` are odd.  The biquadratic field

```text
L=Q(sqrt(p),sqrt(q))
```

meets `Q(zeta_(2^(m+1)))` only in `Q`: every nontrivial quadratic subfield
of `L` is ramified at `p` or `q`, whereas the cyclotomic field is ramified
only at `2`.  Choose the exact cyclotomic Frobenius and the two Legendre
patterns `(non-square,square)` and `(square,non-square)`.  This works also
for `m=1`, where the exact cyclotomic condition is `l=3 mod 4`.  Again (5.1)
holds.

The local factor `Z_2^x=C_2 x (1+4Z_2)` has not been replaced by a false
single logarithmic copy.  Its finite sign dual is retained in the finite
summand called `S_2` below; the two away-prime witnesses already give the
required bounded surjectivity, so the sign cannot change the result.

### 5.3 Dual bounded-saturation statement

For `r notin {p,q}`, write the finite-coordinate part of the dual as

```text
S_r ~= direct_sum_(n>=1) (C_(r^n))^(aleph_0).
```

If `g_r:S_r->(C_(r^infty))^2` is restriction to the two exponent
coordinates after the single local `Z_r` factor has been separated, the
two exact-level witnesses prove

```text
g_r(S_r[r^m])=(C_(r^infty)[r^m])^2 for every m>=1.         (5.2)
```

This is the precise rank-two saturation used below.  No such bounded claim
is needed or asserted in the exceptional branches `r=p,q`.

## 6. Dual kernels and the complete Ulm ledger

Let

```text
K_pq,r = (C_pq,(r))^*.
```

By (4.4), Pontryagin duality gives a surjective restriction map onto
`(C_(r^infty))^2`.  Up to the registered finite sign at `2`, the ambient
dual is

```text
r in {p,q}:      S_r,
r notin {p,q}:   S_r direct_sum C_(r^infty).               (6.1)
```

### 6.1 The owner-primary branches `r=p` or `r=q`

Here

```text
K_pq,r=ker(g:S_r -> (C_(r^infty))^2).                     (6.2)
```

For each homogeneous block
`S_(r,n)=(C_(r^n))^(aleph_0)`, its image is a subgroup of
`(C_(r^n))^2` and is generated by at most two elements.  Select at most two
pivot basis images (Nakayama over `Z/r^nZ`) and subtract their combinations
from every remaining basis vector.  This is a triangular automorphism of
the algebraic direct sum and gives

```text
S_r=T direct_sum R,
T~=S_r,
g(T)=0,
R=direct_sum_n R_n,   each R_n generated by at most two C_(r^n)'s. (6.3)
```

Thus `ker(g)=T direct_sum ker(g|R)`.  Hill's Corollary 2 applies at its
exact domain: `ker(g|R)` is a subgroup of a direct sum of cyclic primary
groups, hence is a direct sum of finite cyclic groups.  It is countable,
and all its multiplicities are absorbed by the already countably infinite
multiplicity of every order in `T`.  Therefore

```text
K_pq,r ~= S_r,
r^omega K_pq,r=0,
u_n(K_pq,r)=aleph_0 for every n<omega,
u_alpha(K_pq,r)=0 for every alpha>=omega.                 (6.4)
```

In particular the two-coordinate target creates no exceptional-primary
tail.  This is the rank-two version of the P15R absorption lemma, not a new
arithmetic invariant.

### 6.2 The off-owner branches

Assume `r notin {p,q}` and put

```text
a=kappa_r(p),  b=kappa_r(q),  h=min(a,b),                 (6.5)

kappa_r(s)=v_r(s^(r-1)-1)-1       for odd r != s,
kappa_2(s)=v_2(s^2-1)-3           for r=2 and s odd.
```

The exact P15R logarithm calculation, now applied to both columns, permits
independent target-unit normalizations and gives

```text
Phi_r(s,z)=g_r(s)+(r^a z,r^b z),
K_pq,r=ker(Phi_r).                                        (6.6)
```

At `r=2`, the finite sign contributions remain inside `g_2`; only the
principal Prüfer column is normalized in (6.6).

The infinite-height subgroup is a literal subgroup of the displayed
ambient group:

```text
r^omega K_pq,r = 0 direct_sum C_(r^h).                    (6.7)
```

For the upper inclusion, an element in every `r^mK` projects to an element
of every `r^mS_r`, hence its `S_r` coordinate is zero.  The kernel equation
then says that both `r^az` and `r^bz` vanish, i.e. `z` has order at most
`r^h`.

For the reverse inclusion, take `z in C_(r^infty)[r^h]` and, for an
arbitrary `m`, choose `w_m` with `r^mw_m=z`.  The vector

```text
(r^a w_m,r^b w_m)
```

has order at most `r^m`.  Equation (5.2) supplies
`s_m in S_r[r^m]` with the negative of that image.  Then
`(s_m,w_m)` lies inside `K_pq,r` and

```text
r^m(s_m,w_m)=(0,z).
```

This proves the internal, rather than merely ambient, roots required for
(6.7).

Apply the two-pivot split (6.3) to `g_r`.  The killed direct summand
`T~=S_r` lies in `K_pq,r`; it supplies countably many independent classes
at every finite height, while the whole kernel is countable.  Consequently

```text
u_n(K_pq,r)=aleph_0 for every n<omega.                     (6.8)
```

The complete transfinite ledger follows from (6.7):

```text
h=0:  u_alpha=0 for every alpha>=omega;

h>0:  r^(omega+j)K_pq,r ~= C_(r^(h-j)),  0<=j<=h,
      u_(omega+h-1)=1,
      u_alpha=0 for every other alpha>=omega.              (6.9)
```

If a divisible subgroup of `K_pq,r` existed, it would lie in the finite
group (6.7), hence would be zero.  Together with (6.4), every primary dual
kernel is countable and reduced before any classification theorem is used.

### 6.3 Compact interpretation

Let `N_r=r^omega K_pq,r`.  The direct annihilator argument used in P15R
gives

```text
ann(closure(Tor(C_pq,(r))))=N_r.                           (6.10)
```

The quotient `K_pq,r/N_r` contains the killed summand `T`, has no nonzero
infinite-height element (because `N_r subset r^mK_pq,r` for every `m`), and
has all finite Ulm invariants `aleph_0`.
Pruefer/Hill absorption therefore identifies it with `S_r`.  Hence

```text
closure(Tor(C_pq,(r))) ~= P_r,
C_pq,(r)/closure(Tor(C_pq,(r))) ~= C_(r^h),                (6.11)
```

where `h=0` in the owner-primary branches.  Formula (6.11) is intrinsic to
the bare compact primary factor; it does not retain a labelled ambient
coordinate.

## 7. Correct common-quotient classification signature

Define

```text
h_r(p,q)=0                                      if r in {p,q};
h_r(p,q)=min(kappa_r(p),kappa_r(q))             otherwise, (7.1)
```

with the odd and `2`-adic definitions in (6.5).  Then the correct theorem
signature is

```text
C_pq ~=_top C_p'q'
  iff
h_r(p,q)=h_r(p',q') for every rational prime r.            (7.2)
```

Necessity follows from the characteristic pro-`r` factor and the intrinsic
finite quotient in (6.11).  For sufficiency, (6.4), (6.8), and (6.9) give
equal complete Ulm sequences for countable reduced primary duals.
Kiehlmann's countably based dual-reduced classification applies factor by
factor, and the unrestricted product of the primary homeomorphisms gives
(7.2).

No recovery statement for the unordered pair `{p,q}` follows.  Zero defect
coordinates can hide owner primes, and equality of all functions (7.1) has
not been shown to force equality of the pairs.

## 8. Finite owner sets: formal cokernel plus Smith form

Let `F={p_1,...,p_d}` with `d>=2`, and put

```text
C_F=coker(A -> product_(i=1)^d B_(p_i)).
```

Define

```text
j_F:A -> product_i U_(p_i),
V_F=coker(j_F).
```

Then, without any arithmetic input,

```text
C_F = V_F / im(E_F),
E_F:Zhat^d -> V_F,                                        (8.1)
```

where `E_F` is induced by the `d` exponent subgroups.  Coordinatewise,

```text
V_F,l = (Z_l^x)^d/diag(Z_l^x)             if l notin F,
V_F,l = (Z_l^x)^(d-1)/diag(Z_l^x)         if l in F.       (8.2)
```

For every pair `i,j`, coordinate projection induces
`V_F->V_{p_i,p_j}`.  Under the standard ratio identification
`V_{p_i,p_j}~=U_{p_i,p_j}`, it sends `E_F` to

```text
(n_i,n_j) |-> p_i^(n_i) p_j^(-n_j),
```

which is `e_(p_i,p_j)` precomposed with the automorphism
`diag(1,-1)` of `Zhat^2`.  Since every signed pair map is a closed
embedding, `E_F` is a closed embedding as well.

### 8.1 The local matrix

Fix `r` and set

```text
I_r=F                 if r notin F,
I_r=F\{r}             if r in F,
t_r=|I_r|-1.                                           (8.3)
```

After the finite sign at `2` is absorbed into `S_r`, the local dual has

```text
V_F,(r)^* ~= S_r direct_sum (C_(r^infty))^(t_r),
```

and restriction has the form

```text
Phi_F,r(s,z)=g_F,r(s)+M_F,r z
 : S_r direct_sum (C_(r^infty))^(t_r)
   -> (C_(r^infty))^d.                                  (8.4)
```

If `r notin F`, choose the last owner as a difference base.  The primal
principal-unit matrix is

```text
[ c_1  0    ... 0   -c_d ]
[ 0    c_2  ... 0   -c_d ]
[             ...          ],                            (8.5)
```

where `v_r(c_i)=kappa_r(p_i)`.  If `r=p_k in F`, the same matrix is formed
from the `d-1` coefficients with `i!=k`; the `p_k` exponent has no local
column.

Sort the coefficient valuations for `p in I_r`:

```text
lambda_(r,1)<=...<=lambda_(r,|I_r|).
```

The ideal of the `j`-minors of (8.5) is generated by all products of `j`
distinct coefficients, so its valuation is the sum of the `j` smallest
`lambda` values.  Hence the Smith exponents are exactly

```text
lambda_(r,1),...,lambda_(r,t_r);                           (8.6)
```

the largest coefficient valuation is discarded.

### 8.2 No new higher-rank saturation theorem

The pair projections already provide every bounded lift needed for (8.4).
If `r notin F`, choose a pair containing a desired owner coordinate and use
the pair saturation (5.2) with the other target value zero.  Its pullback to
`V_F` is supported on away primes and gives any desired coordinate of
`(C_(r^infty)[r^m])^d`.

If `r=p_k in F`, the local matrix image has zero `k`-th target coordinate.
For `d>=3`, pair projections among the owners different from `p_k` give
every bounded vector in that zero-`k` subspace; for `d=2`, `t_r=0` and no
lift is needed.  Thus the pair result, not a new rank-`d` Kummer theorem,
supplies the internal roots.

It follows exactly as in Section 6 that

```text
r^omega (C_F,(r))^*
  ~= direct_sum_(j=1)^(t_r) C_(r^lambda_(r,j)),             (8.7)

u_n=aleph_0 for every n<omega,
u_(omega+s-1)=#{j:lambda_(r,j)=s} for every s>0,
all other transfinite Ulm invariants vanish.               (8.8)
```

The dual is reduced.  The finite compact quotient by the closure of torsion
has the same Smith invariant factors.  When `d=2`, (8.6) is exactly the
single minimum (7.1); at an owner primary there are no factors.  Thus the
finite-set extension is **not an additional relative tail**: it is the
ordinary Smith-minor/order-statistic generalization of the minimum.

For an inclusion `F subset F'`, projection of packet factors gives the
natural surjection `C_F'->C_F`.  On the local presentations it is the
corresponding incidence-matrix map.  Smith reduction computes its finite
tails, but introduces no new arithmetic or canonical basis.  This is formal
cokernel functoriality, not the nonformal compatibility theorem required by
the screen's full-paper gate.

## 9. Primary-source ceilings

| Source | Exact support used | Ceiling enforced |
|---|---|---|
| Deninger, [arXiv:1807.06400v4](https://arxiv.org/abs/1807.06400v4), equations (32), (34)--(40), paragraph after (39) | compact `B_p` presentation, Frobenius quotient, chosen chart/fibration, explicit choice dependence | no printed simultaneous `beta_p`; no actual-packet topology identification; no common quotient or Ulm theorem |
| Perucca, [arXiv:0909.4806](https://arxiv.org/abs/0909.4806), Theorem 14 | simultaneous prescribed `r`-adic valuations of reduction orders; specialization to the independent torus point `(p,q)` | proves the reduction witnesses, not the compact cokernel, internal roots, Ulm ledger, or classification |
| Debry--Perucca, [arXiv:1312.6620v2](https://arxiv.org/abs/1312.6620v2), Sections 2--4, Theorem 17, Example 21 | strong independence and maximal Kummer degrees for torsion-free finitely generated multiplicative groups | Kummer feasibility/cross-check only; its `2`-adic root-of-unity exceptions must be retained |
| Kiehlmann, [arXiv:1101.3005v3](https://arxiv.org/abs/1101.3005v3), Theorems 1.1, 1.4, 1.8; Proposition 2.3 | closure-of-torsion/infinite-height translation and classification of countably based dual-reduced abelian pro-primary groups by the full sequence | no packet kernel, Kummer saturation, Smith minimum, or source-owner map |
| Hill, [Pacific J. Math. 42 (1972), Corollary 2](https://msp.org/pjm/1972/42-1/pjm-v42-n1-p08-p.pdf) | a subgroup of a direct sum of cyclic primary groups is a direct sum of cyclic groups | no multiplicity, kernel identification, Ulm tail, or packet conclusion |

The bounded primary/official search found nearby reduction/Kummer sources but
no source stating the exact combined package (3.1)--(3.4), (4.4),
(6.7)--(7.2).  The only permitted negative conclusion is

```text
NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH.
```

It is not evidence of priority and does not increase the candidate's
standalone score.

## 10. Maximum P15R subtraction and hard decision

The claim-delta ledger is:

| Component | Already removed by source/P15R | Residual S14-C2 work | Standalone weight |
|---|---|---|---|
| compact packet base | Deninger | source-induced common-choice diagonal | owner check only |
| local primary model and `kappa_r(p)` | P15R, including the `2` sign/principal split | put two coefficients in one row | Smith input |
| bounded off-owner restriction | P15R rank one | two independent Kummer rows; direct specialization of standard finite-rank Kummer/Chebotarev | short lemma, no new tail |
| exceptional owner primary | P15R arbitrary-map absorption into `S_r` | use at most two pivots instead of one | formal finite-rank extension |
| infinite internal roots and full Ulm bookkeeping | P15R | kernel of the column `(r^a,r^b)`, hence `h=min(a,b)` | one Smith minimum |
| reducedness and primary/global classification | P15R plus Kiehlmann/Hill | substitute `h_r(p,q)` | direct substitution |
| common quotient | elementary compact-group algebra | equations (3.1)--(3.4) | appendix-sized formal cokernel |
| finite-set extension | pair result plus formal projections | incidence matrix and Smith minors | no nonformal functorial theorem |

There is no residual rank-two infinite-height direction: (6.7) is cyclic of
order `r^min(a,b)`.  There is no additional Ulm datum: all finite invariants
remain `aleph_0` and the only nonzero transfinite invariant is the terminal
class of that cyclic group.  There is no finite-set rescue: (8.7) is just
the Smith list, and inclusion maps are the already present cokernel
projections.

Accordingly the screen's hard condition is met exactly:

```text
STANDALONE_DELTA = formal common quotient
                   + source-feasibility specialization
                   + one Smith minimum
                   + finite-set Smith minors;

TRUE_RELATIVE_TAIL_THEOREM = false;
NONFORMAL_FUNCTORIAL_THEOREM = false;
FULL_PAPER = NO;
FINDINGS = C0/M1/m0;
FINAL = MERGE_P15R / STOP_SLOT14.                           (10.1)
```

The mathematically useful residue may be retained, after P15R itself is
stable, as a compact P15R corollary or appendix: the exact common quotient,
the function `h_r(p,q)`, and optionally the finite-set Smith formula.  It
does not authorize a Slot-14 research protocol, proof ledger, controls,
Route, manuscript, or Git operation.  The unique `HOLD` candidate is
exhausted; Slot 14 should remain stopped/unassigned unless a future batch
authority supplies a genuinely different owner-sensitive theorem.
