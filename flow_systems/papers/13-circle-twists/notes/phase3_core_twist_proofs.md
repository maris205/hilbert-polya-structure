# Paper 13 Phase-3 core twist proofs: P13-1--P13-5

Date: 2026-08-15  
Status: **CORE PROOF CANDIDATE COMPLETE / INDEPENDENT PROOF REVIEW REQUIRED**  
Proof scope: P13-1--P13-5 only  
Standalone status: **not claimed**  
`route_b_invocation_allowed: false`

## 1. Authority, byte lock, and proof boundary

This note is authorized by `notes/phase2_final_review.md`, SHA-256
`ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9`.
The exact governing tuple rehashed at proof intake as follows:

| artifact | SHA-256 | role |
|---|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` | active protocol |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` | active candidate lock |
| `notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` | active state bytes |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | controlling amendment |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` | final source/framework ceiling |
| `notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` | corrected convention/owner audit |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` | Phase-3 authorization |

The inherited companion manuscripts also rehashed exactly:

| companion | SHA-256 | permitted premise |
|---|---|---|
| Paper 11 `papers/11-indiscrete-convolution/paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | author global-QC domain, support, untwisted fibre algebra, and untwisted transported records |
| Paper 12 `papers/12-marked-time-cohomology/paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | all-degree T0 factorization and exact time-pullback direction |

This note proves only the frozen P13-1--P13-5 statements. It does not run or
design controls, prove P13-6--P13-8, create Route material, draft a
manuscript, change a source or lock, or decide `STANDALONE_PASS`.

## 2. Owners and notation

Let `X` be any nonempty set with the global indiscrete topology and a right
action of `(R,+)`. The actual range-first action groupoid is

    G=G_actual(X)=X x R,
    r(x,t)=x,                 s(x,t)=x.t,
    (x,t)(x.t,u)=(x,t+u),    (x,t)^(-1)=(x.t,-t).

The degree-one and degree-two time maps are

    pi_1:G->R,                 pi_1(x,t)=t,
    pi_2:G^(2)->R^2,           pi_2(x;t,u)=(t,u).

The coefficient is the usual Hausdorff circle `T`; it is a T0 topological
abelian group and the action on it is trivial. Pointwise multiplication is
used on all circle-valued cochain groups.

For the one-object usual real-line group, freeze

    (delta alpha)(t,u)
      =alpha(t)alpha(u)overline{alpha(t+u)}.

For the actual owner, freeze

    (delta a)(x;t,u)
      =a(x,t)a(x.t,u)overline{a(x,t+u)}.

A normalized continuous `T`-valued group 2-cocycle (projective multiplier)
on `R` obeys

    sigma(t,u)sigma(t+u,v)
      =sigma(u,v)sigma(t,u+v),
    sigma(t,0)=sigma(0,u)=1.

The actual cocycle equation is

    Sigma(x;t,u)Sigma(x;t+u,v)
      =Sigma(x.t;u,v)Sigma(x;t,u+v).

No quotient topology is placed on a cochain group or on `H^2_tw`.

## 3. P13-1: inherited factorization re-lock

### Theorem 3.1 (degree-one and degree-two time factorization)

Every continuous map `F:X x R^n -> T`, for `n=1,2`, is independent of the
`X` coordinate. Consequently pullback gives canonical bijections

    pi_1^*:C(R,T) -> C(G,T),
    pi_2^*:C(R^2,T) -> C(G^(2),T).

Evaluation at any `x_0 in X` is the inverse, and that inverse is independent
of `x_0`.

#### Proof

For fixed `r in R^n`, the points `(x,r)` and `(y,r)` have exactly the same
open neighborhoods: the global indiscrete topology cannot distinguish their
`X` coordinates. If a continuous `F` took distinct values at those points,
the T0 property of `T` would provide an open set containing one value but not
the other. Its inverse image would distinguish the two domain points, a
contradiction. Thus `F(x,r)=F(y,r)`.

Choose `x_0` only to write `f(r)=F(x_0,r)`. The section
`r |-> (x_0,r)` is continuous, hence so is `f`, and `F=pi_n^*f`.
Surjectivity of `pi_n` gives uniqueness. Since `F` is already independent of
`x`, evaluation at any other base point gives the same `f`. This is the
degree-one/two specialization of Paper 12 `thm:factorization`, locked at
manuscript lines 436--464. The proof is inherited and re-locked here; it is
not a Paper-13 novelty claim. `square`

Normalization is preserved in both directions. For example,
`Sigma(x;t,0)=Sigma(x;0,u)=1` is equivalent, after
`Sigma=pi_2^*sigma`, to `sigma(t,0)=sigma(0,u)=1`.

## 4. P13-2: exact normalized complex and gauge quotient

### Lemma 4.1 (the frozen coboundary is a normalized cocycle)

If `a:G->T` is continuous and normalized by `a(x,0)=1`, then `delta a` is
continuous, normalized, and satisfies the actual cocycle equation.

#### Proof

Continuity is immediate from continuity of the groupoid structure maps and
the circle operations. At the two normalized faces,

    (delta a)(x;t,0)=a(x,t)a(x.t,0)overline{a(x,t)}=1,
    (delta a)(x;0,u)=a(x,0)a(x,u)overline{a(x,u)}=1.

For the cocycle equation, the left-hand side expands to

    a(x,t)a(x.t,u)a(x.(t+u),v)
      overline{a(x,t+u+v)}.

Expanding

    (delta a)(x.t;u,v)(delta a)(x;t,u+v)

gives the same expression after the middle factors
`a(x.t,u+v)` and its conjugate cancel. Hence `delta a` is a normalized
cocycle. `square`

The same calculation with no `x` coordinate proves the one-object formula.
It also shows that `delta` is a homomorphism from normalized one-cochains to
normalized two-cocycles.

### Theorem 4.2 (typed reduction of the normalized multiplier complex)

The maps `pi_1^*` and `pi_2^*` restrict to isomorphisms

    C^1_n,cont(R;T)  ~=  C^1_n,cont(G;T),
    Z^2_n,cont(R;T)  ~=  Z^2_n,cont(G;T),

and they commute with the frozen coboundary:

    delta_G(pi_1^*alpha)=pi_2^*(delta_R alpha).

They therefore identify the coboundary subgroups and induce a canonical
isomorphism of abstract groups

    H^2_tw(R;T) ~= H^2_tw(G;T).

#### Proof

Theorem 3.1 gives the two underlying continuous-cochain bijections and shows
that they commute with pointwise multiplication and inversion. If
`a(x,t)=alpha(t)`, then

    (delta_G a)(x;t,u)
      =alpha(t)alpha(u)overline{alpha(t+u)}
      =(pi_2^*delta_R alpha)(x;t,u).

If `Sigma(x;t,u)=sigma(t,u)`, its actual cocycle equation becomes

    sigma(t,u)sigma(t+u,v)
      =sigma(u,v)sigma(t,u+v),

because the factor at `x.t` has the same time-only value. The converse is
the same substitution read backwards. Normalization was checked after
Theorem 3.1. Thus cocycles correspond and the displayed coboundary square
commutes. Its image subgroups correspond, so passage to the algebraic
quotients gives the last isomorphism. `square`

In particular, for normalized multipliers `sigma,tau`, the relation

    sigma overline{tau}=delta alpha

has exactly the same meaning before and after actual time pullback. No
external real-group theorem has been applied directly to the actual owner;
the typed pullback/evaluation bridge has been proved first.

## 5. P13-3: direct continuous classification on the real line

### Theorem 5.1 (continuous real-line multiplier collapse)

Every continuous normalized circle multiplier `sigma:R^2->T` has a
continuous normalized trivializer `alpha:R->T` satisfying

    sigma=delta alpha.

Consequently

    H^2_tw(R;T)=0,

and, by Theorem 4.2, `H^2_tw(G_actual(X);T)=0` for every nonempty globally
indiscrete right-real action owner. If `alpha` and `beta` are two
trivializers of the same multiplier, `beta/alpha` is a continuous character
of `R`; conversely multiplication by any continuous character produces
another trivializer.

The proof below is direct. Sorkin's inaccessible full text is not used as a
proof or as a source for a sign, normalization, or splitting step.

### Step 1: fixed-base phase lift and exact axis normalization

The exponential map

    exp(i .):R->T

is a covering map. Since `R^2` is simply connected, the continuous map
`sigma` has a unique continuous lift `q:R^2->R` once

    q(0,0)=0,    sigma(s,t)=exp(i q(s,t))

is fixed. Normalization gives

    q(s,0) in 2 pi Z,    q(0,t) in 2 pi Z.

Each expression is continuous on a connected axis and is zero at the
origin. Hence

    q(s,0)=q(0,t)=0

as equalities in `R`, not merely modulo `2 pi`.

Define the lifted cocycle defect

    D(s,t,u)
      =q(s,t)+q(s+t,u)-q(t,u)-q(s,t+u).

The circle cocycle equation says `D(s,t,u) in 2 pi Z`. The function `D` is
continuous on connected `R^3`, so it is constant; the normalized value at
the origin is zero. Thus

    q(s,t)+q(s+t,u)=q(t,u)+q(s,t+u)                 (5.1)

exactly. The phase lift is a normalized continuous real 2-cocycle.

### Step 2: one-dimensional commutator/bicharacter audit

Put

    b(s,t)=q(s,t)-q(t,s).

It is continuous, alternating, and additive in each variable. For example,
two applications of (5.1) give

    b(s+t,u)
      =q(t,u)-q(u,s)+q(s,t+u)-q(s+u,t)
      =b(t,u)+b(s,u).

Additivity in the second variable follows either by the same calculation or
from `b(s,t)=-b(t,s)`. For fixed `t`, the continuous Cauchy theorem gives

    b(s,t)=s b(1,t).

The function `t |-> b(1,t)` is itself continuous and additive, so for a
constant `kappa` one has

    b(s,t)=kappa s t.

But `b(t,t)=0` for every `t`, forcing `kappa=0`. Therefore

    q(s,t)=q(t,s).                                  (5.2)

This is the one-dimensional step. It is false as a dimension-free argument;
the `R^2` falsifier is recorded after the proof.

### Step 3: smoothing without changing the cohomology class

Choose `rho in C_c^infinity(R)` with

    integral_R rho(u)du=1.

Define

    h(s)=integral_R q(s,u)rho(u)du.

The integral is over a fixed compact set. Joint continuity of `q` therefore
makes `h` continuous, and `h(0)=0`. Use the real coboundary

    (delta h)(s,t)=h(s)+h(t)-h(s+t)

and put `q_1=q-delta h`. It remains a continuous normalized real cocycle and
is symmetric because both `q` and `delta h` are symmetric. Integrating
(5.1) in its third variable gives the useful exact formula

    q_1(s,t)
      =integral_R [q(s,t+u)-q(s,u)]rho(u)du.         (5.3)

After `v=t+u`, this is

    q_1(s,t)
      =integral_R q(s,v)rho(v-t)dv-h(s).

For fixed `s` the right-hand side is smooth in `t`. Differentiation under
the integral is valid because, on every compact set of `(s,t)`, the moving
support remains in a fixed compact set and the continuous factor `q` is
bounded there. Moreover

    partial_2 q_1(s,t)
      =-integral_R q(s,v)rho'(v-t)dv,                (5.4)

so this partial derivative is jointly continuous. Set

    a(r)=partial_2 q_1(r,0).

Then `a` is continuous.

### Step 4: continuous splitting and the frozen sign

The cocycle identity for `q_1` is

    q_1(s,t)+q_1(s+t,u)=q_1(t,u)+q_1(s,t+u).

Differentiate in `u` at `u=0`, using (5.4). This gives

    a(s+t)=a(t)+partial_2 q_1(s,t),

or

    partial_2 q_1(s,t)=a(s+t)-a(t).                 (5.5)

Let

    A(t)=integral_0^t a(v)dv.

The integral is oriented when `t<0`; `A` is continuously differentiable and
`A(0)=0`. Integrating (5.5) from `0` to `t` and using
`q_1(s,0)=0` yields

    q_1(s,t)
      =A(s+t)-A(s)-A(t)
      =(delta(-A))(s,t).                            (5.6)

Since `q_1=q-delta h`, equations (5.6) and additivity of `delta` give

    q=delta(h-A).

Put

    p=h-A,    alpha(t)=exp(i p(t)).

Both are continuous, `p(0)=0`, and therefore `alpha(0)=1`. Finally,

    (delta alpha)(s,t)
      =exp(i[p(s)+p(t)-p(s+t)])
      =exp(i q(s,t))
      =sigma(s,t).

This is the required continuous normalized trivializer with the exact
frozen sign.

### Step 5: uniqueness modulo continuous characters

If `delta alpha=delta beta=sigma`, set

    chi=beta/alpha.

Then `chi` is continuous, normalized, and

    delta chi=(delta beta)/(delta alpha)=1.

Thus

    chi(s+t)=chi(s)chi(t),

so `chi` is a continuous character. Conversely, `delta chi=1` for every
continuous character, hence `alpha chi` is another trivializer. This proves
the uniqueness statement and completes Theorem 5.1. `square`

### Sharp sign and dimension controls

For

    sigma_kappa(s,t)=exp(i kappa s t),
    alpha_kappa(t)=exp(-i kappa t^2/2),

one has

    delta(-kappa t^2/2)(s,t)=kappa s t,

so `delta alpha_kappa=sigma_kappa` in the frozen orientation.

On `R^2`, however,

    omega_theta(s,t)=exp(i theta s_1 t_2)

is a normalized continuous multiplier whose commutator is

    exp(i theta(s_1 t_2-t_1 s_2)).

For `theta!=0` this is not identically one, whereas every coboundary on an
abelian group is symmetric. Thus the one-dimensional step cannot be promoted
to an arbitrary vector group.

## 6. P13-4: twisted global-QC test algebra

Fix a continuous normalized multiplier `sigma` on `R`. As a vector space set

    A_sigma=C_c(R)

and define

    (f *_sigma g)(t)
      =integral_R f(u)g(t-u)sigma(u,t-u)du,          (6.1)

    f^{*sigma}(t)
      =overline{sigma(t,-t)}overline{f(-t)}.         (6.2)

### Lemma 6.1 (closure, continuity, and support)

For `f,g in C_c(R)`, the integral (6.1) is absolutely finite and continuous,
and

    supp(f *_sigma g) subseteq supp(f)+supp(g).

Also `f^{*sigma}` is continuous and

    supp(f^{*sigma})=-supp(f).

#### Proof

Let `K=supp(f)` and `L=supp(g)`. Since `|sigma|=1`,

    integral_R |f(u)g(t-u)sigma(u,t-u)|du
      <= ||g||_infinity ||f||_1.

For `t` in a compact neighborhood of `t_0`, the integrand may be integrated
over the fixed compact set `K`; the factors involving `(u,t-u)` vary
uniformly there. Dominated convergence, or uniform continuity on that
compact set, proves continuity in `t`. If `t` is outside `K+L`, no `u` can
make both scalar functions nonzero, proving the product support inclusion.
The star assertion follows directly from (6.2), continuity of `sigma`, and
the fact that its circle value never vanishes. `square`

### Lemma 6.2 (absolute Fubini and associativity)

The product (6.1) is associative.

#### Proof

For `f,g,h in C_c(R)`, the absolute double integral arising in either
parenthesization satisfies

    double_integral |f(u)g(v-u)h(t-v)|du dv
      <= ||h||_infinity ||f||_1 ||g||_1.            (6.3)

Thus Fubini and the substitutions below are legitimate. Expanding the left
parenthesization gives the coefficient

    sigma(u,v-u)sigma(v,t-v).

The cocycle equation at `(u,v-u,t-v)` gives

    sigma(u,v-u)sigma(v,t-v)
      =sigma(v-u,t-v)sigma(u,t-u).                  (6.4)

After setting `w=v-u`, the right-hand side of the expanded integral is
exactly

    f *_sigma (g *_sigma h).

Equations (6.3)--(6.4) prove associativity. `square`

### Lemma 6.3 (inverse-face identity and involution)

Normalization and the cocycle equation imply

    sigma(t,-t)=sigma(-t,t).                        (6.5)

Consequently `(f^{*sigma})^{*sigma}=f`.

#### Proof

Insert `(t,-t,t)` in the cocycle equation. The two normalized face values
are one, leaving (6.5). Then

    (f^{*sigma})^{*sigma}(t)
      =overline{sigma(t,-t)}sigma(-t,t)f(t)=f(t).

Conjugate linearity is immediate. `square`

### Lemma 6.4 (oriented gauge-star isomorphism)

Let `sigma,tau` be normalized continuous multipliers and let a normalized
continuous `a:R->T` satisfy

    sigma overline{tau}=delta a.

Then

    U_a:A_sigma->A_tau,    (U_a f)(t)=a(t)f(t)

is a support-preserving star-algebra isomorphism. Its inverse is
`U_overline(a)`.

#### Proof

At the convolution variables `(u,t-u)`, the gauge relation is

    a(t)sigma(u,t-u)=a(u)a(t-u)tau(u,t-u).           (6.6)

Multiplying (6.1) by `a(t)` and using (6.6) proves

    U_a(f *_sigma g)=(U_a f)*_tau(U_a g).           (6.7)

At `(t,-t)`, normalization gives

    sigma(t,-t)overline{tau(t,-t)}=a(t)a(-t).

After conjugating and rearranging,

    a(t)overline{sigma(t,-t)}
      =overline{tau(t,-t)}overline{a(-t)}.           (6.8)

Equation (6.8) proves

    U_a(f^{*sigma})=(U_a f)^{*tau}.                 (6.9)

Because `|a|=1`, multiplication by `a` and by its inverse preserve the
nonzero locus and support exactly. Finally,
`tau overline{sigma}=delta(overline a)`, so `U_overline(a)` is the inverse.
`square`

By Theorem 5.1, every `sigma` is `delta alpha`; hence

    U_alpha:A_sigma->A_1.

For `A_1`, direct conjugation and the change of variable in ordinary group
convolution give

    (f*g)^*=g^* * f^*.

Indeed,

    overline{(f*g)(-t)}
      =integral_R overline{f(v-t)}overline{g(-v)}dv
      =(g^* * f^*)(t).

Transport through the bijective map `U_alpha`, together with Lemma 6.3,
proves both star laws for `A_sigma`. Thus `A_sigma` is a well-defined
associative star algebra for every continuous normalized multiplier.

### The actual author domain

Let `C_glob(G)` be the Paper-11 author global-QC test space and let

    Phi:C_c(R)->C_glob(G),    Phi(f)(x,t)=f(t).

Paper 11 `thm:phi`, locked lines 465--484, proves this is a linear bijection
and

    supp_G(Phi(f))=X x supp_R(f).

By Theorems 3.1 and 4.2 every actual multiplier has the form

    Sigma(x;t,u)=sigma(t,u).

For `F=Phi(f)` and `G_0=Phi(g)`, define the frozen author operations

    (F *_Sigma G_0)(x,t)
      =integral_R F(x,u)G_0(x.u,t-u)Sigma(x;u,t-u)du,

    F^{*Sigma}(x,t)
      =overline{Sigma(x;t,-t)}overline{F(x.t,-t)}.

Substitution gives the exact identities

    Phi(f)*_Sigma Phi(g)=Phi(f *_sigma g),
    Phi(f)^{*Sigma}=Phi(f^{*sigma}).                 (6.10)

Thus closure, associativity, both star laws, and the gauge-star map on the
actual author domain follow through a proved bijection, not by invoking a
standard actual-groupoid theorem. The absolute Fubini estimate is exactly
(6.3), because every function and multiplier in the integrand is time-only.

The actual inverse-face identity is also direct: the cocycle equation at
`(x;t,-t,t)` gives

    Sigma(x;t,-t)=Sigma(x.t;-t,t).                  (6.11)

The product and star supports satisfy

    supp_G(F *_Sigma G_0)
      subseteq X x (supp_R(f)+supp_R(g)),

    supp_G(F^{*Sigma})=X x (-supp_R(f)).

These are quasi-compact actual supports by Paper 11 `thm:qc`, locked lines
359--376. An actual gauge is `pi_1^*a`; multiplication by it preserves the
support exactly. This completes P13-4 on both the time and actual author
domains. No standard actual-groupoid C-star algebra has been asserted.

## 7. P13-5: projective regular representation and transported norms

### Proposition 7.1 (intrinsic twisted left regular representation)

For `s in R`, define on `L^2(R)`

    (lambda_sigma(s)xi)(t)=sigma(s,t-s)xi(t-s).     (7.1)

Each operator is unitary, the map is strongly continuous, and

    lambda_sigma(s)lambda_sigma(u)
      =sigma(s,u)lambda_sigma(s+u).                 (7.2)

#### Proof

Translation and multiplication by a circle-valued function both preserve
the `L^2` norm, so (7.1) is unitary. Strong continuity first follows on the
dense subspace `C_c(R)` from translation continuity and uniform continuity
of `sigma` on the compact region swept out near a fixed `s`; the unitary norm
bound extends it to all of `L^2(R)`.

For the projective law,

    [lambda_sigma(s)lambda_sigma(u)xi](t)
      =sigma(s,t-s)sigma(u,t-s-u)xi(t-s-u).

The cocycle equation at `(s,u,t-s-u)` identifies its scalar coefficient
with

    sigma(s,u)sigma(s+u,t-s-u),

which is (7.2). `square`

For `f in C_c(R)`, its integrated form is the bounded operator

    Lambda_sigma(f)=integral_R f(s)lambda_sigma(s)ds,

with `||Lambda_sigma(f)||<=||f||_1`, and

    [Lambda_sigma(f)xi](t)
      =integral_R f(u)sigma(u,t-u)xi(t-u)du.         (7.3)

The integral is first understood weakly or on compactly supported vectors;
the norm estimate gives the unique bounded extension.

### Proposition 7.2 (integrated star representation)

The map `Lambda_sigma` is a star representation of `A_sigma`:

    Lambda_sigma(f *_sigma g)
      =Lambda_sigma(f)Lambda_sigma(g),
    Lambda_sigma(f^{*sigma})=Lambda_sigma(f)^*.

#### Proof

The projective law (7.2), norm-Fubini, and the substitution `r=s+u` turn the
double integrated product into (6.1). For the adjoint, (7.2) and (6.5) give

    lambda_sigma(s)^*
      =overline{sigma(s,-s)}lambda_sigma(-s).

Hence, after `r=-s`,

    Lambda_sigma(f)^*
      =integral_R overline{f(-r)}
         overline{sigma(-r,r)}lambda_sigma(r)dr
      =Lambda_sigma(f^{*sigma}),

where (6.5) was used in the last equality. `square`

### Proposition 7.3 (exact gauge intertwiner)

Let `sigma=delta alpha` be the trivialization from Theorem 5.1, and let

    (M_alpha xi)(t)=alpha(t)xi(t),
    (U_alpha f)(t)=alpha(t)f(t).

Then

    Lambda_sigma(f)
      =M_overline(alpha) lambda(U_alpha f)M_alpha,   (7.4)

equivalently

    M_alpha Lambda_sigma(f)M_overline(alpha)
      =lambda(U_alpha f).                           (7.5)

Here `lambda` is the ordinary integrated left regular representation of
`R`.

#### Proof

For a compactly supported vector, the right-hand side of (7.4) evaluated at
`t` is

    integral_R f(u)
      overline{alpha(t)}alpha(u)alpha(t-u)xi(t-u)du.

The scalar factor is

    (delta alpha)(u,t-u)=sigma(u,t-u),

so the expression is exactly (7.3). Density and boundedness extend the
identity to all `L^2` vectors. `square`

It follows at once that `Lambda_sigma` is faithful on `C_c(R)`: `U_alpha`
is injective and the ordinary left regular representation is faithful on
`C_c(R)` by the locked Paper-11 argument. Thus its operator norm is a norm,
not merely a seminorm.

### Proposition 7.4 (standard-norm identification and owner-safe transport)

Multiplication by `alpha` extends, because `|alpha|=1`, to an isometric
Banach star-algebra isomorphism

    U_alpha:L^1(R,sigma)->L^1(R).

Consequently, on `C_c(R)`,

    ||f||_{C*(R,sigma)}
      =||U_alpha f||_{C*(R)},                       (7.6)

    ||f||_{C*_r(R,sigma)}
      =||Lambda_sigma(f)||
      =||lambda(U_alpha f)||.                       (7.7)

#### Proof

Lemma 6.4 proves the product and star identities, while circle multiplication
preserves the `L^1` norm. The inverse is `U_overline(alpha)`, so the `L^1`
map is an isometric Banach star-algebra isomorphism: the identities extend
from `C_c(R)` by its `L^1` density and the usual `L^1` convolution bounds.
Composition with this isomorphism bijects all nondegenerate star
representations of the two `L^1` algebras; taking their universal norm
suprema proves (7.6). Equation (7.7) is the unitary equivalence (7.4).
`square`

For an actual global-QC element `F=Phi(f)`, define only the author transported
norms

    ||F||_(full,Sigma,alpha)=||U_alpha f||_{C*(R)},
    ||F||_(r,Sigma,alpha)=||lambda(U_alpha f)||.     (7.8)

Equations (7.6)--(7.7) identify (7.8) exactly with the restrictions of the
standard **time-group** twisted norms under the proved map `Phi`. They do not
define or import a standard C-star algebra of the actual groupoid.

### Proposition 7.5 (choice independence)

The two norms in (7.8) are independent of the continuous normalized
trivializer.

#### Proof

Let `beta` be another trivializer and set `chi=beta/alpha`. Theorem 5.1 gives
that `chi` is a continuous character, and

    U_beta=C_chi U_alpha,    (C_chi h)(t)=chi(t)h(t).

Character multiplication is an invertible star automorphism of the ordinary
convolution algebra. Indeed, the character law gives, pointwise,

    C_chi(h*k)=(C_chi h)*(C_chi k),

and `chi(-t)=overline{chi(t)}` gives the exact star check

    C_chi(h^*)(t)
      =chi(t)overline{h(-t)}
      =overline{chi(-t)h(-t)}
      =(C_chi h)^*(t).

It preserves the universal norm because composition by `C_chi` and its
inverse `C_overline(chi)` bijects all star representations. For the reduced
norm, direct calculation gives

    lambda(C_chi h)=M_chi lambda(h)M_overline(chi).  (7.9)

Thus both full and reduced norms of `U_beta f` equal those of `U_alpha f`.
The equality holds on the common dense test algebra itself, so the resulting
completed isometric star-isomorphism classes are choice-independent.
`square`

### Theorem 7.6 (amenable equality and completed author records)

The full and reduced norms in (7.8) agree. Their completions are the
choice-independent author records

    TW-FULL-TRANSPORT(Sigma),
    TW-RED-TRANSPORT(Sigma),

and `U_alpha` induces isometric star isomorphisms

    TW-FULL-TRANSPORT(Sigma) ~= C*(R,sigma) ~= C*(R),
    TW-RED-TRANSPORT(Sigma)   ~= C*_r(R,sigma) ~= C*_r(R).

The corresponding full and reduced records are isometrically isomorphic.

#### Proof

The usual real-line group is locally compact, Hausdorff, abelian, and
amenable. The exact audited analytic locator is Austad Proposition 2.4,
printed p. 7, citing Leptin Satz 6: on an amenable locally compact group with
a continuous 2-cocycle, the twisted left-regular norm is the maximal C-star
norm on the twisted `L^1` algebra. Apply it only to the one-object group
`R`. Equations (7.6)--(7.8) have already identified the author norms with
the restrictions of those standard time-group norms, so maximal and reduced
agree on the author test algebra. Completion and Propositions 7.4--7.5 give
the displayed, choice-independent isomorphisms. `square`

When `X={*}`, the actual owner is literally this one-object Hausdorff group,
so the group statement applies directly. When `|X|>=2`, the actual records
remain the author transports in (7.8). The proof invokes no standard
Hausdorff, étale, or locally Hausdorff groupoid theorem on that owner, no
actual-to-standard proxy completion, and no Haar or completion theorem on a
dense stabilizer.

## 8. Sign, domain, and fail-closed audit

| audited surface | exact result | prohibited promotion retained |
|---|---|---|
| `pi_1,pi_2` | pullback is time-to-actual; evaluation is its base-point-independent inverse | no external group theorem jumps directly to actual |
| normalized `delta` | actual and time formulas commute exactly; `delta a` is normalized and a cocycle | no Borel/measurable/smooth substitution |
| phase lift | fixed base, both axes exactly zero, defect in `2 pi Z` and then zero | lift alone not presented as the splitting proof |
| real cocycle splitting | `q=delta(h-A)`; `alpha=exp(i(h-A))` | inaccessible Sorkin text not used as proof |
| uniqueness | all trivializers form one torsor under continuous characters | no arbitrary discontinuous gauges |
| gauge direction | `sigma overline{tau}=delta a` gives `U_a:A_sigma->A_tau` | no reversed `U_a` |
| product/associativity | cocycle coefficient (6.4) and absolute Fubini (6.3) | no finite diagnostic used as proof |
| star | inverse-face identity, involution, anti-product law, and gauge-star identity all close | no missing conjugation or modular term (`Delta_R=1`) |
| actual domain | operations transport through the proved `Phi:C_c(R)->C_glob(G)` | no standard actual-groupoid C-star label |
| projective regular law | (7.2), integrated kernel (7.3), and intertwiner (7.4)--(7.5) agree | no source/target reversal |
| transported norms | exact restrictions of standard time-group norms; choice independent | no proxy completion map |
| full/reduced equality | imported only from amenability of standard group `R` after norm identification | no actual-owner amenability claim |

The P13-3 nontrivial-class branch is not triggered: the direct construction
produces a normalized continuous trivializer for an arbitrary input in the
frozen complex. The P13-4 formula-failure branch is not triggered: closure,
associativity, Fubini, both star laws, support, and gauge-star compatibility
are established. The P13-5 choice/norm branch is not triggered: the exact
intertwiner, standard-norm restrictions, character isometries, and amenable
equality are proved.

These are proof-author conclusions and remain subject to independent proof
review. If review invalidates any direct splitting, domain, Fubini, star, or
norm step, the corresponding claim reopens under the active fail-closed
branch. P13-6--P13-8, deterministic controls, nonredundancy, standalone
status, Route, manuscript, and release remain outside this note.

## 9. Claim matrix

| claim | result in this note | exact owner/ceiling | proof status |
|---|---|---|---|
| P13-1 | every continuous actual degree-two circle cochain factors uniquely through `pi_2`; degree one through `pi_1` | inherited Paper-12 T0 theorem, exact-lock reverified; no novelty credit | **CLOSED / INHERITED RE-LOCK** |
| P13-2 | normalization, cocycle predicate, coboundary, pointwise group law, gauge equivalence, and algebraic quotient commute with time pullback/evaluation | Paper-13 typed bridge between actual owner and `TIME-R-CONT-TWIST` | **PROVED** |
| P13-3 | `H^2_tw(R;T)=0`; direct normalized continuous trivializer; uniqueness modulo continuous characters; actual quotient corollary | usual one-object `R`; Sorkin is prior-art sentinel only and supplies no proof step | **PROVED** |
| P13-4 | time and actual author twisted global-QC product/star algebra, closure, support, absolute Fubini, associativity, both star laws, and oriented gauge-star isomorphism | `A_sigma=C_c(R)` and Paper-11 `C_glob(G)` only; no standard actual-groupoid C-star claim | **PROVED** |
| P13-5 | projective left regular representation, integrated star representation, exact `M_alpha` intertwiner, standard-norm restriction, trivializer-choice independence, and amenable full/reduced equality | standard group `R` plus author transported actual records; Austad Proposition 2.4/Leptin ceiling | **PROVED** |

Core proof disposition: **P13-1--P13-5 closed in this proof candidate, pending
independent proof review.** No standalone or downstream authorization follows
from this note alone.
