# Paper 11 Phase-3 core proofs: `P11-1`--`P11-5`

**Proof date:** 2026-08-15 (Asia/Shanghai)  
**Primary verdict:** **`CONFIRM_CONVOLUTION_COLLAPSE`**  
**Target status:** **`P11-1`--`P11-5` PROVED**  
**Standard actual-groupoid `C*` theorem invoked:** **no**

This file proves only the topology, factorization, global function algebra,
author-defined fibre/convolution record, source-fibre regular
representations, and transported completions registered as `P11-1`--`P11-5`.
It writes no Route decision, manuscript text, code, deterministic-control
result, proxy completion map, or result for the full packet or suspension.

## 1. Exact binding, source ceiling, and notation

The proof is bound to these exact active and Phase-2 bytes:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `27c0ffd9c233301528e36f401e9cdf3f4030d65cea8002aafcf6fb97e557f860` |
| `notes/candidate_lock.md` | `a97e9c30bca6bf9cee3e5543b5d83b72ab7291e5485fa9604811dfa3ce4c8012` |
| `notes/pipeline_state.md` | `317ab9e8b3082b2d8bc75590618a6e86ca742bb8c23a899c3b612ea6304125e6` |
| `notes/phase2_final_gate.md` | `96d5bb1e82bb5db416d9b52993b13fdc6c5eb25e26e0e1896b265138b800f0fb` |
| `notes/phase2_framework_source_audit.md` | `a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439` |
| `notes/phase2_owner_proxy_audit.md` | `18116cf52c2359a840c9996fb6424fae56260f590990fac79704c040245fa761` |

The only inherited Paper-9 bytes used as mathematical premises are its proof
audit
`c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8`
and source audit
`20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20`,
both already locked in the active candidate. Paper 10 is not used to prove an
arrow result; the factorization theorems below are proved directly, which
preserves the nonredundancy boundary.

The proof first treats the exact generic domain needed to expose which
conclusions are arithmetic-blind.

> **Generic domain.** Let `X` be a nonempty indiscrete space and let
> `(x,t) |-> x dot t` be any right action of the additive group `R` on its
> underlying set. Put `G=X x R` with the product topology and
> `pi_R(x,t)=t`. Give `G` the range-first groupoid operations
>
> ```text
> r(x,t)=x,
> s(x,t)=x dot t,
> (x,t)(x dot t,u)=(x,t+u),
> (x,t)^(-1)=(x dot t,-t).
> ```

Any such action is jointly continuous because its codomain `X` is
indiscrete. No transitivity, freeness, fixed period, or stabilizer is assumed
in the generic proof.

For the arithmetic specialization, fix an arbitrary rational prime `p` and
an arbitrary normalized Paper-9 orbit label `a`, and take

```text
X=X_{p,a}=ACT-ORBIT-p-a,
G=G_{p,a}^{act},
L_p=log p.
```

Paper 9 supplies that this `X` is nonempty, nontrivial, and indiscrete.
Deninger supplies the underlying right action and stabilizer `L_p Z`.
Nothing below imports an ordinary-circle topology, and none of the proofs
uses the stabilizer.

## 2. `P11-1`: exact arrow topology, quasi-compactness, and groupoid maps

### Lemma 2.1 — opens, closed sets, subspaces, and closures

For the generic domain:

1. the open subsets of `G` are exactly `X x U` with `U` open in `R`;
2. the closed subsets are exactly `X x F` with `F` closed in `R`;
3. for every `A subset G`,

   ```text
   closure_G(A)=X x closure_R(pi_R(A));
   ```

4. for every `K subset G`, every open subset of the subspace `K` has the
   form

   ```text
   K intersect pi_R^(-1)(U)
   ```

   for an open `U subset R`.

**Proof.** The only open subsets of `X` are `emptyset` and `X`. Hence every
nonempty basic product open is `X x U`, and arbitrary unions preserve that
form. Taking complements proves the closed-set statement.

A point `(x,t)` lies in `closure_G(A)` exactly when every neighborhood
`X x U` with `t in U` meets `A`. This is equivalent to every neighborhood
`U` of `t` meeting `pi_R(A)`, or
`t in closure_R(pi_R(A))`, independently of `x`. This proves the closure
formula. Intersecting the classified ambient opens with `K` gives the last
statement. QED.

The projection `pi_R:G->R` is continuous, open, and surjective. After
choosing any `x_0 in X`, the map

```text
j_{x_0}:R->G,       j_{x_0}(t)=(x_0,t),
```

is a continuous section.

### Theorem 2.2 — exact quasi-compactness criterion

For every subset `K subset G`, in the frozen open-cover convention,

```text
K is quasi-compact  iff  pi_R(K) is compact in the usual Hausdorff R.
```

**Proof.** If `K` is quasi-compact, its continuous image `pi_R(K)` is
quasi-compact. Since `R` is Hausdorff, this is precisely ordinary compactness.

Conversely, suppose `pi_R(K)` is compact and let `(O_i)_{i in I}` be an
arbitrary open cover of `K`. By Lemma 2.1, write

```text
O_i=K intersect pi_R^(-1)(U_i)
```

with `U_i` open in `R`. For each `t in pi_R(K)`, some point `(x,t) in K`
exists and belongs to an `O_i`; hence `t in U_i`. Thus `(U_i)` covers the
compact set `pi_R(K)`. A finite subfamily covers `pi_R(K)`, and the
corresponding finite subfamily of `(O_i)` covers `K`. QED.

This proof permits arbitrary `K`: it does not assume that `K` is closed,
saturated, a product, or Hausdorff.

### Corollary 2.3 — the two local variants and separation

The following hold in the generic domain.

1. `G` is second countable. A countable base is
   `{X x (q_1,q_2):q_1,q_2 in Q, q_1<q_2}`.
2. Every `(x,t)` has a quasi-compact neighborhood, for example
   `X x [t-epsilon,t+epsilon]` for `epsilon>0`.
3. Every point has a basis of open neighborhoods with quasi-compact closure:

   ```text
   closure_G(X x (t-epsilon,t+epsilon))
     =X x [t-epsilon,t+epsilon].
   ```

   Given a larger open neighborhood, `epsilon` may be chosen so that this
   closed interval lies inside its time projection.
4. No nonempty open subset of `G` is quasi-compact.

**Proof.** The first three statements follow from the usual countable base
and local compact intervals in `R`, Lemma 2.1, and Theorem 2.2. For the last,
a nonempty open is `X x U` with `U` a nonempty open subset of `R`. If it were
quasi-compact, Theorem 2.2 would make `U` compact. A compact subset of the
Hausdorff line is closed, so `U` would be nonempty and clopen in the connected
line. Then `U=R`, which is not compact, a contradiction. QED.

If `X` has more than one point, then additionally:

```text
G is not T0 and hence is not Hausdorff;
no nonempty open subset of G is Hausdorff;
G is nowhere locally Hausdorff.
```

Indeed, for distinct `x,y in X`, the points `(x,t)` and `(y,t)` belong to
exactly the same opens. Every nonempty open `X x U` contains such a pair for
any `t in U`, so that subspace is not even `T0`.

For the actual Paper-11 owner, Paper 9 gives `|X_{p,a}|>1`. Therefore all
three negative conclusions apply, and the frozen raw diagnostic has the
direct value

```text
C_c^HOp(G_{p,a}^{act})={0}.
```

There is no nonempty Hausdorff open `U` from which to obtain a nonzero patch
generator; the empty-patch extension is zero. This is a direct diagnostic
calculation, not the assertion that any standard groupoid algebra is zero.
The Phase-2 `NOT_APPLICABLE` framework verdict remains separate.

### Theorem 2.4 — topological groupoid and composable-pair chart

The displayed operations make `G` a topological groupoid. Moreover, the
frozen coordinate bijection

```text
Psi:X x R x R -> G^(2),
Psi(x,t,u)=((x,t),(x dot t,u))
```

is a homeomorphism, where `G^(2)` has the subspace topology from `G x G`.

**Proof.** The groupoid identities are direct consequences of the right-action
law and addition in `R`. For example,

```text
(x,t)(x dot t,u)(x dot (t+u),v)=(x,t+u+v),
(x,t)(x dot t,-t)=(x,0),
(x dot t,-t)(x,t)=(x dot t,0).
```

The product `G x G` has no topology-sensitive unit coordinates: after
reordering its factors, its opens are pullbacks of opens in `R^2` under the
two time projections. Hence the subspace opens of `G^(2)` are exactly the
sets whose `(t,u)` coordinates lie in an open subset of `R^2`. The same is
true of `X x R x R`. Since `Psi` is bijective and preserves `(t,u)`, both
`Psi` and `Psi^(-1)` are continuous.

The maps `r` and `s` are continuous because their codomain `X` is
indiscrete. For the remaining maps, preimages of a basic open `X x U` are

```text
unit^(-1)(X x U) = X       if 0 in U, and emptyset otherwise;
inv^(-1)(X x U)  = X x (-U);
(m o Psi)^(-1)(X x U)
  = X x {(t,u):t+u in U}.
```

These are open. Thus units, inversion, and multiplication are continuous.
QED.

This establishes every `P11-1` assertion for every rational prime `p` and
every normalized orbit label `a`, while retaining the exact two positive
local quasi-compact variants and the two negative open-set statements.

## 3. `P11-2`: continuous and measurable factorization through time

### Theorem 3.1 — continuous maps to `T0` targets

Let `Y` be any `T0` topological space. A map `F:G->Y` is continuous if and
only if there is a unique continuous `g:R->Y` such that

```text
F=g o pi_R.
```

**Proof.** For fixed `t`, all points in `X x {t}` are topologically
indistinguishable. Their images under a continuous map to a `T0` space must
therefore be equal. Define `g(t)=F(x_0,t)` for one fixed `x_0 in X`; then
`F=g o pi_R`. The section from Lemma 2.1 gives
`g=F o j_{x_0}`, so `g` is continuous. Conversely, `g o pi_R` is continuous
whenever `g` is. Surjectivity of `pi_R` gives uniqueness. QED.

The `T0` hypothesis is essential: a nonconstant map into a nontrivial
indiscrete target may be continuous.

### Lemma 3.2 — exact arrow Borel sigma-algebra

The topology-generated Borel sigma-algebra is

```text
B(G)={X x B:B in B(R)}.
```

**Proof.** The displayed family is a sigma-algebra containing every open
`X x U`, so `B(G)` is contained in it. Conversely, the family

```text
{B subset R:X x B belongs to B(G)}
```

is a sigma-algebra containing every open subset of `R`; it therefore contains
`B(R)`. QED.

The projection `pi_R` and every section `j_x` are measurable for these exact
sigma-algebras.

### Theorem 3.3 — measurable maps to countably separated targets

Let `(Y,Sigma_Y)` be countably separated. A map

```text
F:(G,B(G))->(Y,Sigma_Y)
```

is measurable if and only if there is a unique measurable

```text
g:(R,B(R))->(Y,Sigma_Y)
```

with `F=g o pi_R`.

**Proof.** Let `(E_n)_{n>=1}` be a countable measurable family separating
the points of `Y`. If `F(x,t)!=F(y,t)`, some `E_n` contains exactly one of
these values. But Lemma 3.2 says

```text
F^(-1)(E_n)=X x B_n
```

for a Borel `B_n subset R`, so membership at a fixed time `t` cannot depend
on the unit coordinate. This contradiction shows that `F` is constant on
every time fibre. Define `g(t)=F(x_0,t)`. Since
`g=F o j_{x_0}` and the section is measurable, `g` is measurable. The
converse follows from measurability of `pi_R`, and uniqueness again follows
from its surjectivity. QED.

If `|X|>1`, the measurable space `(G,B(G))` is not countably separated. In
fact, no Borel set distinguishes `(x,t)` from `(y,t)` for distinct `x,y`.
Notice that `B(G)` is nevertheless countably generated because `B(R)` is;
countable generation and countable separation are different properties.

The actual arrow measurable space is therefore not countably separated, and
Theorems 3.1 and 3.3 prove `P11-2` without reusing the unit-space theorem of
Paper 10.

## 4. `P11-3`: global continuous quasi-compact-support collapse

For `g:R->C`, write

```text
Phi(g)(x,t)=g(t).
```

### Theorem 4.1 — exact function and support classification

`Phi` is a linear bijection

```text
Phi:C_c(R) -> C_qc^glob(G).
```

For every continuous `g:R->C`, whether or not it has compact support,

```text
supp_G(Phi(g))=X x supp_R(g).
```

**Proof.** Since `C` is Hausdorff and hence `T0`, Theorem 3.1 says that every
globally continuous `f:G->C` has a unique form `f=Phi(g)` with `g` continuous
on `R`. Conversely every such pullback is continuous.

Let `N_g={t:g(t)!=0}`. The nonzero locus of `Phi(g)` is `X x N_g`.
Lemma 2.1 gives

```text
closure_G(X x N_g)
  =X x closure_R(N_g)
  =X x supp_R(g).
```

This proves the support identity, including `g=0`. By Theorem 2.2 this
support is quasi-compact exactly when `supp_R(g)` is compact. That is exactly
`g in C_c(R)`. Thus `Phi` restricts to the claimed bijection. QED.

Both directions of the support gate are explicit: quasi-compactness of the
arrow support projects to compactness of `supp_R(g)`, and compactness of
`supp_R(g)` lifts back to quasi-compactness of the arrow support. No
Hausdorff compactness is asserted for the nonzero arrow support itself.

## 5. `P11-4`: author fibre family and the global convolution `*`-algebra

### Theorem 5.1 — `GLOB-FIBRE-FAMILY` satisfies its exact contract

For `x in X`, let

```text
rho_x:R->G^x,       rho_x(t)=(x,t),
lambda^x=(rho_x)_*(dt).
```

Then:

1. `rho_x` is a homeomorphism from `R` onto the range fibre `G^x`;
   `lambda^x` is a positive Radon measure on that locally compact Hausdorff
   fibre and has full fibre support;
2. for every `f=Phi(g) in C_qc^glob(G)`, the fibre integral is absolutely
   finite and

   ```text
   integral_(G^x) f d lambda^x=integral_R g(t)dt;
   ```

   the resulting function of `x` is constant and hence continuous; and
3. for every arrow `gamma` and every licensed `f`, the frozen left-invariance
   identity holds.

**Proof.** The subspace opens in `{x} x R` are `{x} x U`, so `rho_x` is a
homeomorphism. The Radon and full-support assertions are transported from
Lebesgue measure on `R`.

Theorem 4.1 gives `g in C_c(R)`, hence
`integral |g(t)|dt<infinity`; the displayed integral formula follows from the
definition of `lambda^x` and is independent of `x`.

For left invariance, write `gamma=(x,t)`. A range-fibre element over
`s(gamma)=x dot t` has the form `eta=(x dot t,u)`, and the frozen product is
`gamma eta=(x,t+u)`. Therefore

```text
integral_(G^(s(gamma))) f(gamma eta) d lambda^(s(gamma))(eta)
  = integral_R g(t+u)du
  = integral_R g(v)dv
  = integral_(G^(r(gamma))) f(eta) d lambda^(r(gamma))(eta).
```

Only translation invariance of Lebesgue measure was used. QED.

This proves the author contract. It does not convert the family into a Haar
system in any retained published framework.

### Theorem 5.2 — convolution, involution, and support

Give `C_c(R)` its ordinary additive-group operations

```text
(g*k)(t)=integral_R g(u)k(t-u)du,
g^sharp(t)=conjugate(g(-t)).
```

For all `g,k in C_c(R)`, the frozen arrow formulas are absolutely defined and

```text
Phi(g)*Phi(k)=Phi(g*k),
Phi(g)^*=Phi(g^sharp).
```

Moreover,

```text
supp_R(g*k) subset supp_R(g)+supp_R(k),
supp_R(g^sharp)=-supp_R(g),
```

so the outputs again belong to `C_qc^glob(G)`.

**Proof.** Put `f=Phi(g)` and `h=Phi(k)`. For every `(x,t)`,

```text
(f*h)(x,t)
  = integral_R f(x,u)h(x dot u,t-u)du
  = integral_R g(u)k(t-u)du.
```

The integrand is continuous and supported in the compact set
`supp(g) intersect (t-supp(k))`, so the integral is absolutely finite. The
continuity claim can be checked without an implicit groupoid theorem: a
compactly supported continuous function on `R` is uniformly continuous, and

```text
|(g*k)(t+h)-(g*k)(t)|
 <= integral_R |g(u)| |k(t+h-u)-k(t-u)|du
 <= ||g||_1 sup_(v in R)|k(v+h)-k(v)| -> 0
```

as `h->0`, uniformly in `t`. If
`t` is outside `supp(g)+supp(k)`, every integrand value is zero; the sum of
the two compact supports is compact. Thus `g*k in C_c(R)` with the stated
support control.

The frozen inverse and involution give

```text
f^*(x,t)
  =conjugate(f(x dot t,-t))
  =conjugate(g(-t))
  =Phi(g^sharp)(x,t).
```

Reflection preserves compactness and gives the exact involution support.
QED.

No action, stabilizer, period, or modular term survives these formulas. This
is a derived conclusion, not an inserted group convention.

### Theorem 5.3 — associativity and the `*` identities

The frozen operations make `C_qc^glob(G)` a `*`-algebra, and

```text
Phi:(C_c(R),*,sharp) -> C_qc^glob(G)
```

is a `*`-isomorphism.

**Proof.** It remains only to verify the algebra identities. For
`g,k,l in C_c(R)`, the associativity integrand is absolutely integrable for
each `t`, since

```text
integral_R integral_R
  |g(u)k(v-u)l(t-v)|du dv
 <= ||l||_infinity ||g||_1 ||k||_1 < infinity.
```

Thus Fubini and the measure-preserving substitution `w=v-u` give

```text
((g*k)*l)(t)
 = integral_R integral_R g(u)k(v-u)l(t-v)du dv
 = integral_R g(u)
     [integral_R k(w)l(t-u-w)dw]du
 = (g*(k*l))(t).
```

For the anti-multiplicative involution, the same absolute-integrability
record permits conjugation under the integral, and the substitution
`u=v-t` gives

```text
(k^sharp*g^sharp)(t)
 = integral_R conjugate(k(-v)) conjugate(g(v-t))dv
 = integral_R conjugate(g(u)k(-t-u))du
 = (g*k)^sharp(t).
```

Reflection twice also gives

```text
(g^sharp)^sharp=g.
```

The convolution is bilinear and `sharp` is conjugate-linear. Theorem 5.2
transports all these identities through the bijection of Theorem 4.1. QED.

This proves the primary research question at the dense algebra level for the
generic domain, and hence for every actual `(p,a)` owner.

## 6. `P11-5`: source fibres, regular representations, and completions

### Lemma 6.1 — exact source-fibre coordinate and measure

For `x in X`,

```text
G_x=s^(-1)(x)
   ={(x dot (-t),t):t in R},
vartheta_x(t)=(x dot (-t),t).
```

The map `vartheta_x:R->G_x` is a homeomorphism. If

```text
lambda_x=(inversion)_* lambda^x,
```

then

```text
lambda_x=(vartheta_x)_*(dt).
```

Consequently

```text
U_x:L^2(G_x,lambda_x)->L^2(R,dt),
(U_x xi)(t)=xi(vartheta_x(t)),
```

is unitary.

**Proof.** The right-action law gives
`(x dot (-t)) dot t=x`, and if `y dot t=x`, then
`y=x dot (-t)`, proving the set parametrization. Subspace opens of `G_x` are
its intersections with `X x U`, hence precisely `vartheta_x(U)`; this proves
the homeomorphism.

On the range fibre, inversion sends

```text
(x,v) -> (x dot v,-v)=vartheta_x(-v).
```

The change of variable `t=-v` preserves Lebesgue measure, so inversion
pushforward is exactly `(vartheta_x)_*(dt)`. The norm identity

```text
integral_R |xi(vartheta_x(t))|^2dt
  = integral_(G_x)|xi(eta)|^2d lambda_x(eta)
```

and the inverse composition with `vartheta_x^(-1)` prove unitarity. QED.

### Theorem 6.2 — exact kernel formula and boundedness

Initially let `f=Phi(g) in C_qc^glob(G)` and
`xi in C_c(G_x)`, and define

```text
[Ind_x(f)xi](gamma)
  = integral_(G_x) f(gamma eta^(-1))xi(eta)d lambda_x(eta).
```

This integral is pointwise absolutely finite on the dense domain
`C_c(G_x)`. It extends uniquely to a bounded operator on
`H_x=L^2(G_x,lambda_x)`, and for `zeta in C_c(R)` one has pointwise

```text
[U_x Ind_x(Phi(g)) U_x^(-1)zeta](t)
  = integral_R g(t-u)zeta(u)du.
```

For arbitrary `zeta in L^2(R)`, the same equality holds in `L^2` and almost
everywhere after representatives are chosen. Moreover,

```text
||Ind_x(Phi(g))|| <= ||g||_1.
```

**Proof.** Write

```text
gamma=vartheta_x(t)=(x dot (-t),t),
eta=vartheta_x(u)=(x dot (-u),u).
```

Then

```text
eta^(-1)=(x,-u),
gamma eta^(-1)=(x dot (-t),t-u).
```

The endpoints match because `s(gamma)=x=r(eta^(-1))`. Hence

```text
f(gamma eta^(-1))=g(t-u),
```

Under `vartheta_x`, the dense space `C_c(G_x)` is exactly `C_c(R)`; density
follows from the ordinary Lebesgue `L^2(R)` record. For fixed `t`, the
product `g(t-u)zeta(u)` is bounded and supported in the compact set
`(t-supp(g)) intersect supp(zeta)`, so its integral is absolutely finite.
Lemma 6.1 converts `lambda_x` to `du`, proving the kernel formula. On
`C_c(R)` the right side is ordinary left convolution `lambda_R(g)zeta`.
Writing it as

```text
lambda_R(g)zeta(t)=integral_R g(v)zeta(t-v)dv
```

and using translation invariance of the `L^2` norm gives Young's bound

```text
||lambda_R(g)zeta||_2
 <= integral_R |g(v)| ||zeta(.-v)||_2 dv
 = ||g||_1 ||zeta||_2.
```

Therefore the operator extends from the dense domain to all of `L^2(R)`;
unitary conjugation gives the unique bounded extension on `H_x`. QED.

The dense-domain statement avoids interpreting a pointwise integral as
defined at every point for an arbitrary `L^2` equivalence class.

### Theorem 6.3 — `Ind_x` is a bounded `*`-representation

For every `x`, the extended map

```text
Ind_x:C_qc^glob(G)->B(H_x)
```

is a bounded `*`-representation in the sense that each algebra element gives
a bounded operator and

```text
Ind_x(f*h)=Ind_x(f)Ind_x(h),
Ind_x(f^*)=Ind_x(f)^*.
```

**Proof.** Linearity is immediate from the defining integral. On `C_c(R)`,
Theorem 5.3 applied once more to a vector `zeta in C_c(R)` gives

```text
lambda_R(g*k)zeta=(g*k)*zeta=g*(k*zeta)
  =lambda_R(g)lambda_R(k)zeta.
```

The operators on both sides are bounded by Theorem 6.2, so equality on this
dense domain proves operator equality.

Use the convention
`<zeta,eta>=integral_R zeta(t)conjugate(eta(t))dt`. For
`zeta,eta in C_c(R)`, absolute Fubini and the displayed definition of
`g^sharp` give the exact adjoint calculation

```text
<lambda_R(g)zeta,eta>
 = integral_R zeta(u)
     [integral_R g(t-u)conjugate(eta(t))dt]du
 = <zeta,lambda_R(g^sharp)eta>.
```

so `lambda_R(g)^*=lambda_R(g^sharp)` after bounded extension. Theorems 5.2
and 6.2 and the unitary `U_x` transport these identities to `Ind_x`. QED.

### Corollary 6.4 — exact reduced norm

For every `g in C_c(R)` and every unit `x`,

```text
||Ind_x(Phi(g))||=||lambda_R(g)||.
```

Since `X` is nonempty,

```text
||Phi(g)||_(red,glob)
  =sup_(x in X)||Ind_x(Phi(g))||
  =||lambda_R(g)||.
```

This is a norm rather than only a seminorm. If `g!=0`, put
`zeta(u)=conjugate(g(-u))`. Then `zeta in C_c(R)` and

```text
[lambda_R(g)zeta](0)=integral_R |g(-u)|^2du>0.
```

The convolution representative is continuous by Theorem 5.2, so a nonzero
value at `0` makes it nonzero on a set of positive measure. Thus its `L^2`
class is nonzero and `lambda_R(g)!=0`.

All unit representations have the same norm and kernel formula. This
equality was proved from the frozen source fibre and inversion measure; it
was not inferred from a standard actual-groupoid regular representation.

### Theorem 6.5 — transported full/reduced completions and Fourier model

Define, exactly as locked,

```text
||Phi(g)||_(full,glob)=||g||_(C*(R)).
```

Then `Phi` extends by completion to author-defined `*`-isomorphisms

```text
C*(R)   ~= C^full_glob(G),
C_r*(R) ~= C^red_glob(G).
```

The second line follows from Corollary 6.4. Since `R` is abelian and hence
amenable, its universal and reduced norms agree. Therefore the identity on
the dense global algebra extends to

```text
C^full_glob(G) ~= C^red_glob(G).
```

With the frozen sign

```text
Fourier(g)(xi)=integral_R g(t)exp(-it xi)dt,
```

the group Fourier transform yields

```text
C^full_glob(G) ~= C^red_glob(G) ~= C_0(R).
```

**Source ownership and locators.** These last group facts use the exact
Williams draft-3.1 manifestation locked in Phase 2:

| Locator | Group-owned result used here |
|---|---|
| physical p. 38 / printed p. 26, Example 1.80 | every character of `R` is `t |-> exp(-it xi)` and `Rhat` has the usual topology |
| physical p. 94 / printed p. 82, Proposition 3.1 | Fourier transform extends to `C*(R) ~= C_0(Rhat)` |
| physical p. 210 / printed p. 198, Definition 7.7 and Example 7.9 | the reduced group norm is the left-regular norm |
| physical pp. 210--211 / printed pp. 198--199, Example 7.11 | direct abelian-group full/reduced equality |
| physical p. 211 / printed p. 199, discussion and Theorem 7.13 | abelian groups are amenable; amenability gives universal/reduced equality |

The universal norm is the group norm obtained from integrated strongly
continuous unitary representations of `R`. Full/reduced equality belongs to
amenability of the **group `R`**, not to an actual-groupoid amenability claim.
The Fourier theorem likewise belongs to the group and is transferred only
through the proved `Phi` and regular-norm identities.

Accordingly, this proof uses only the locked names

```text
C^full_glob(G_{p,a}^{act}),
C^red_glob(G_{p,a}^{act}).
```

It does not rename them `C^*(G_{p,a}^{act})` or
`C_r^*(G_{p,a}^{act})`, and it proves no map from either completion into the
standard-circle proxy completion.

## 7. Quantified specialization, falsifiers, and ownership ledger

The generic hypotheses hold for every actual `X_{p,a}`. Since `p` and `a`
were arbitrary, the following table is quantified over every rational prime
and every normalized Paper-9 orbit label.

| Target | Exact proved result | Registered falsifier excluded by the proof | Status |
|---|---|---|---|
| `P11-1` | opens/closed sets and closures classified; `K` quasi-compact iff `pi_R(K)` compact; both positive local variants; second countable; actual arrow space non-`T0`, non-Hausdorff, with no nonempty quasi-compact or Hausdorff open; `Psi` a homeomorphism; all groupoid maps continuous | an open depending on `x`, a projection/compactness mismatch, a nonempty legal Hausdorff patch, or a discontinuous frozen operation | **PROVED** |
| `P11-2` | all continuous `T0`-target maps and countably-separated measurable-target maps factor uniquely through `pi_R`; `B(G)={X x B}`; actual arrow measurable space not countably separated | a separated target map varying within one time fibre, an extra arrow Borel set, or a Borel set separating equal-time unit labels | **PROVED** |
| `P11-3` | every global licensed function is uniquely `Phi(g)` for `g in C_c(R)` and `supp_G(Phi g)=X x supp_R(g)` | unit-coordinate variation or failure of either support direction | **PROVED** |
| `P11-4` | author fibre contract, absolute domains, continuity, left invariance, closure, associativity, involution identities, and exact `Phi` intertwining | a surviving action/stabilizer term, divergent licensed integral, or failure of group convolution/support | **PROVED** |
| `P11-5` | `vartheta_x` is measure preserving; `U_x` unitary; every `Ind_x` is the bounded left regular representation under `U_x`; reduced norm exact; full/reduced/Fourier completions transported with source locators | a sign error in `g(t-u)`, unit-dependent norm, non-bounded operator, failed `*` identity, or completion attribution to the actual groupoid | **PROVED** |

The exact ownership split is:

| Record | Owner after this proof | Non-credit |
|---|---|---|
| actual orbit set, right action, `L_p Z` stabilizer | Deninger source ledger | no arrow topology or convolution source claim |
| actual nonempty nontrivial indiscrete topology | Paper 9 | no standard-circle topology |
| arrow topology/groupoid, generic topology theorem, `Phi`, fibre family, convolution, `Ind_x` | Paper 11 direct proof | no retained standard groupoid-framework credit |
| `C*(R)`, `C_r*(R)`, amenability, Fourier | ordinary group `R`, Williams locators above | no actual-groupoid amenability or standard completion name |
| `C^full_glob`, `C^red_glob` | Paper 11 author-defined completions transported through the proved dense/regular maps | no automatic proxy embedding or completion extension of `I` |

The generic theorem remains valid for trivial and nontransitive actions and
for arbitrary unit labels. That breadth explains why the abstract global
algebra and transported completions carry no arithmetic credit merely from
their isomorphism classes; this file does not perform the later Route or full
`P11-8` adjudication.

## 8. Final Phase-3 core verdict and remaining boundary

The requirements for the scoped verdict in the candidate lock are met:

```text
P11-1: PROVED
P11-2: PROVED
P11-3: PROVED
P11-4: PROVED
P11-5: PROVED
primary_verdict: CONFIRM_CONVOLUTION_COLLAPSE
standard_actual_groupoid_framework_invoked: false
standard_actual_groupoid_Cstar_name_used_as_result: false
proxy_completion_map_proved: false
route_decision_made: false
manuscript_or_code_written: false
```

The topological proof also computes the direct diagnostic value
`C_c^HOp(G_{p,a}^{act})=0`, but the stronger scoped verdict
`CONFIRM_CONVENTION_SPLIT` remains withheld until the separate
`P11-6`--`P11-8` proof package and the registered controls are complete. No
standard actual-groupoid `C*` theorem, proxy theorem, or norm extension of
`I` receives credit from this file.
