# Paper 8 Phase-3 operator proofs — fixed one-orbit audit

Date: 2026-08-14  
Status: **PASS — P8-2--P8-6 CLOSED ON ONE ACTUAL SOURCE ORBIT ONLY**  
Severity: **0 Critical / 0 Major / 0 Minor**

## 1. Exact scope and evidence lock

This note proves only the local theorem authorized by the Phase-2 final gate.
Fix one actual source orbit `O`, its source-proved period `L=log p`, and a
basepoint.  The Phase-2 topology audit identifies this orbit homeomorphically
with `R/(L Z)`.  Nothing below constructs a packet completion, a packet
regular von Neumann algebra, a transverse disintegration, or a same-map
transport from this orbit to a packet.

The proof was audited against these exact bytes:

| Active artifact | SHA-256 |
|---|---|
| `research_protocol.md` | `e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535` |
| `candidate_lock.md` | `8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e` |
| `phase2_domain_amendment.md` | `412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3` |
| `phase2_final_gate.md` | `22fd0376ad8e69e6816b3d005d88f4cde2cc5f4b243749c95aa2f19ab8164a3f` |
| `phase2_groupoid_source_audit.md` | `39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42` |
| `phase2_trace_source_audit.md` | `101d447a238cbf9ec6ea33a78b3f6be7456a1be30fdc206e13db91697d75c5f0` |

The fixed local map, and the only map used below, is

```text
A_L=C*(O rtimes R) -> A_(L,r)=C*_r(O rtimes R)
                    -> M_L^reg.
```

The first arrow will be proved to be an isomorphism.  The second is the
faithful fixed source-fibre regular representation proved in Section 6.  The
character representations start at `A_L`; they are not substituted for the
regular representation.

## 2. Locked groupoid and crossed-product conventions

Write `x=[u]` in `O=R/(L Z)`.  Length Haar is `du`, with
`du(O)=L`; probability Haar is separately denoted `du/L`.  An arrow `(x,t)`
has source `x` and range `x+t`.  Lebesgue `dt` is the action-groupoid Haar
system and `du` is invariant under the action.  The locked formulas are

```text
(a*b)(x,t) = integral_R a(x+v,t-v)b(x,v) dv,
a^*(x,t)   = conjugate(a(x+t,-t)).
```

These formulas really are the ordinary crossed-product formulas, rather than
a merely formal resemblance.  Put

```text
alpha_t(g)(y)=g(y-t),
F_a(t)(y)=a(y-t,t).
```

Then `a -> F_a` takes the displayed convolution and involution to those of
`C(O) rtimes_alpha R`.  Indeed,

```text
(F_a*F_b)(t)(y)
 = integral_R F_a(v)(y) alpha_v(F_b(t-v))(y) dv
 = integral_R a(y-v,v)b(y-t,t-v) dv
 = F_(a*b)(t)(y),
```

after `w=t-v`; the involution check is

```text
F_(a^*)(t)(y)=conjugate(a(y,-t))
             =alpha_t(F_a(-t)^*)(y).
```

Thus all completion and representation statements below apply to the locked
convolution itself.

The quotient normalization is also fixed, not inferred later:

```text
integral_R g(t) dt
 = integral_[0,L) sum_(r in Z) g(u+rL) du
 = L integral_(O,du/L) sum_(r in Z) g(u+rL).
```

This is the specialization of Williams's quotient integral formula (4.63)
to Lebesgue Haar on `R` and counting Haar on `L Z`.

## 3. Induced character representations and the sign audit

For `theta in [0,2pi)`, freeze

```text
chi_theta(rL)=exp(i r theta).
```

Williams's induced-function convention is

```text
H_theta = {eta:R->C measurable:
           eta(u+rL)=chi_theta(rL)^(-1)eta(u)=exp(-ir theta)eta(u),
           eta|_[0,L) in L2([0,L),du)},
(U_t eta)(u)=eta(u-t).
```

The inner product is the length integral on `[0,L)`.  With multiplication by
`C(O)`, the integrated form of the locked kernel is

```text
(pi_theta(a)eta)(y)
 = integral_R a([y-t],t) eta(y-t) dt.                 (3.1)
```

This follows directly from `F_a(t)(y)=a(y-t,t)` and therefore closes the
convention bridge between the locked groupoid and ordinary induction.
Williams, Proposition 5.4 and Theorem 5.12 (printed pp.153 and 161), supply
the sourced induced-function rule and its compatibility with Green/Rieffel
induction; equation (3.1) is the present-convention specialization.

The functions

```text
e_(n,theta)(u)=L^(-1/2) exp(i k_(n,theta)u),
k_(n,theta)=(2pi n-theta)/L,
```

form an orthonormal basis of `H_theta`.  Their boundary condition is

```text
e_(n,theta)(u+rL)=exp(-ir theta)e_(n,theta)(u),
```

and

```text
U_t e_(n,theta)=exp(-i t k_(n,theta))e_(n,theta).
```

Hence the locked character `chi_theta`, not `chi_(-theta)`, has frequencies
`(2pi n-theta)/L`.  This calculation also fixes the later return phase to be
`exp(+ir theta)`.  No target expression is used to choose either sign.

## 4. P8-2 — exact completion and Floquet field

The acting group `R` is amenable.  Williams, Theorem 7.13 (printed p.199),
therefore gives full/reduced equality for this action:

```text
C*(O rtimes R)=C*_r(O rtimes R).                      (4.1)
```

This conclusion comes from amenability, not from Morita equivalence.

Apply Williams, Theorem 4.30 (printed p.138), with `G=R`, the closed subgroup
`H=L Z`, `G/H=O`, counting Haar on `H`, and quotient length Haar `du`.
Together with Theorem 5.12, it gives the actual unstabilized isomorphism

```text
Phi:A_L -> C*(L Z) tensor K(H_0)
            ~= C(T) tensor K(H_0),
H_0=L2([0,L),du),                                    (4.2)
```

such that, after restriction of a quasi-periodic vector to `[0,L)`,

```text
Phi(a)(theta)=pi_theta(a).                            (4.3)
```

For clarity, (4.2) is stronger than Green's Morita-equivalence conclusion.
It is licensed by the separate homogeneous-space isomorphism theorem.  The
basepoint, fundamental interval, and trivialization make the displayed `Phi`
choice-dependent; no such choice is promoted to source data.  Its isomorphism
class and the evaluations (3.1) are enough for every statement below.

One can see compactness and field continuity directly on the dense locked
core.  For `y,u in [0,L)`, (3.1) has kernel

```text
K_a(theta;y,u)
 = sum_(r in Z) a([u],y-u+rL) exp(i r theta).          (4.4)
```

Only finitely many summands occur for `a in C_c(O rtimes R)`.  Thus (4.4) is
continuous in all variables and defines a compact operator, continuously in
`theta`.  Williams's theorem supplies the nontrivial surjectivity and norm
completion of this dense calculation.

Therefore P8-2 closes as an **unstabilized C*-isomorphism plus a continuous
field of induced representations**, not merely a stable isomorphism, Morita
equivalence, or as-yet-unidentified measurable decomposition.

## 5. P8-3 — trace class and shifted Poisson formula

Freeze the Fourier transform

```text
fhat(xi)=integral_R f(t)exp(-it xi)dt.
```

For `f in C_c^infinity(R)`, set `a_f(x,t)=f(t)`.  Section 3 gives

```text
pi_theta(a_f)=integral_R f(t)U_t dt,
pi_theta(a_f)e_(n,theta)
  =fhat((2pi n-theta)/L)e_(n,theta).                  (5.1)
```

The Fourier transform of a compactly supported smooth function is Schwartz.
Consequently, for every `N>1`,

```text
sup_(theta in [0,2pi))
 sum_(n in Z) |fhat((2pi n-theta)/L)| < infinity.     (5.2)
```

Thus every operator in (5.1) is trace class, uniformly over the character
circle, and

```text
T_theta(f)=Tr(pi_theta(a_f))
 =sum_(n in Z) fhat((2pi n-theta)/L).                 (5.3)
```

To determine the sign without guessing, let

```text
g(t)=f(t)exp(i theta t/L).
```

Then `ghat(2pi n/L)=fhat((2pi n-theta)/L)`.  The scaled unshifted Poisson
formula therefore yields

```text
T_theta(f)
 =L sum_(r in Z) g(rL)
 =L sum_(r in Z) f(rL)exp(+i r theta).                (5.4)
```

The last sum is finite because `f` has compact support.  Laugesen, Definition
14.1 and Theorems 14.10--14.11 (printed pp.79, 84--85), own the Fourier sign
and decay input; Theorem 23.5 (printed p.137) owns the unshifted Poisson
formula.  Modulation, the shifted sign, (5.1), and (5.4) are new elementary
specializations proved here.  They establish P8-3.

## 6. Fixed regular representation, faithfulness, and bicommutant

Fix the source fibre at the chosen basepoint.  Identifying that fibre with
`R`, the locked left-regular formula on `L2(R,ds)` is

```text
(lambda_L(a)xi)(s)
 =integral_R a([v],s-v)xi(v)dv
 =integral_R a([s-t],t)xi(s-t)dt.                    (6.1)
```

Define the Zak transform first on compactly supported vectors by

```text
(Zxi)(theta,u)=sum_(r in Z) xi(u+rL)exp(i r theta),
theta in [0,2pi), u in [0,L).                        (6.2)
```

Parseval for `Z` gives

```text
integral_0^(2pi) integral_0^L |Zxi(theta,u)|^2 du dtheta/(2pi)
 =integral_R |xi(s)|^2 ds.                           (6.3)
```

Moreover, extension in `u` satisfies

```text
Zxi(theta,u+rL)=exp(-ir theta)Zxi(theta,u).
```

Thus `Z` extends to a unitary

```text
L2(R) -> direct_integral_T H_theta dm(theta),
dm(theta)=dtheta/(2pi).                               (6.4)
```

A direct substitution in (6.1), using `v=u+jL`, gives

```text
Z lambda_L(a) Z^(-1)
 =direct_integral_T pi_theta(a) dm(theta),            (6.5)
```

with exactly the kernel (4.4).  This proves that the fixed source-fibre
regular representation is the dual-Haar direct integral of the same
character field used in (4.3), not an abstractly isomorphic replacement.

### 6.1 Faithfulness

Under (4.2), (6.5) is the multiplication representation of
`C(T,K(H_0))` on `L2(T,dm;H_0)`.  If a continuous compact-operator field is
nonzero, its norm is positive on a nonempty open subset of `T`; full-support
Haar gives that subset positive measure.  Its multiplication operator is
therefore nonzero.  Hence `lambda_L` is faithful.  Equivalently, transitivity
makes all source-fibre regular representations unitarily equivalent, and
(4.1) identifies their reduced norm with the full norm.

This verifies both arrows of the fixed local map; faithfulness is not inferred
solely from the abstract algebra isomorphism.

### 6.2 Bicommutant

After the fixed trivialization in (4.2), the represented algebra is

```text
C(T) tensor K(H_0)
 subset B(L2(T,dm) tensor H_0).
```

Because `C(T)''=L-infinity(T,dm)` in its Haar multiplication representation
and `K(H_0)''=B(H_0)`, the tensor bicommutant theorem gives

```text
M_L^reg := lambda_L(A_L)''
 =L-infinity(T,dm) bar_tensor B(H_0).                 (6.6)
```

This is the bicommutant of the **fixed faithful regular representation** in
(6.1), not a packet algebra and not a representation chosen after seeing the
trace.  In particular, there is no omitted packet multiplicity in (6.6).

For later normalization checks, Parseval applied to (4.4) yields, for
`a in C_c(O rtimes R)`,

```text
integral_T ||pi_theta(a)||_HS^2 dm(theta)
 =integral_0^L integral_R |a([u],t)|^2 dt du.         (6.7)
```

## 7. P8-4 — the exact FNS trace and its domains

On the positive cone of the concrete von Neumann algebra (6.6), define

```text
Tau_L(X)=integral_T Tr_(H_0)(X(theta)) dm(theta),
X in (M_L^reg)_+.                                    (7.1)
```

Here a positive decomposable operator field is understood up to Haar-a.e.
equality and the integrand is an extended nonnegative measurable function.
The definition uses dual **probability** Haar `dm=dtheta/(2pi)` associated to
counting Haar on `L Z`; the length factor remains in the fibre Hilbert space
and quotient formula.  It does not use probability Haar `du/L` on the orbit.

The exact bounded domains are

```text
(m_Tau)_+ = {X in (M_L^reg)_+:
             integral_T Tr(X(theta))dm(theta)<infinity},
n_Tau     = {X in M_L^reg:
             integral_T Tr(X(theta)^* X(theta))dm(theta)<infinity},
m_Tau     = span((m_Tau)_+)
          = span{Y^* Z: Y,Z in n_Tau},
```

where the last expression means the linear span of products `Y^*Z` with
`Y,Z in n_Tau`.  The bounded part of the noncommutative `L1` space is

```text
L1(M_L^reg,Tau_L) intersect M_L^reg
 = {X in M_L^reg:
    integral_T Tr(|X(theta)|)dm(theta)<infinity}.     (7.2)
```

Equation (7.2) is not a claim that the full noncommutative `L1` space contains
only bounded operators.

The trace in (7.1) is faithful, normal, and semifinite:

- Faithfulness follows fibrewise from the faithful operator trace and then
  from equality a.e.
- Normality follows from the normality of the fibre trace and monotone
  convergence for the integral.
- For semifiniteness, choose finite-rank projections `P_N increasing to 1`
  on `H_0`.  For bounded `X>=0`,
  `X^(1/2)(1 tensor P_N)X^(1/2)` increases strongly to `X`, lies below `X`,
  and has trace at most `N||X||` because `m(T)=1`.
- The identity `Tau_L(Y^*Y)=Tau_L(YY^*)` follows fibrewise, first on its finite
  domain and then in the extended-positive sense.

Thus (7.1) is an FNS trace, not merely a Plancherel weight whose traciality was
left implicit.  Renault (physical pp.3--4) owns the general Plancherel-weight
and Fourier-isometric dual-Haar normalization; Bourne--Rennie, Lemma 7.4
(physical p.36), owns the invariant-measure crossed-product trace template.
Formula (7.1), its bicommutant owner, and the domain checks above specialize
those templates to the fixed map.

On the dense groupoid core, (6.7) gives the exact identity-coefficient formula

```text
Tau_L(lambda_L(a)^* lambda_L(a))
 =integral_0^L integral_R |a([u],t)|^2 dt du
 =integral_0^L (a^* * a)([u],0)du.                   (7.3)
```

For the complex time kernel, the trace-class estimate is stronger than mere
membership in the C*-algebra:

```text
integral_T sum_(n in Z)
 |fhat((2pi n-theta)/L)| dm(theta)
 =L/(2pi) integral_R |fhat(xi)|dxi < infinity.        (7.4)
```

Therefore `lambda_L(a_f)` belongs to the bounded linear `L1` domain (7.2), so
its trace is legitimately defined.  Fubini/Tonelli is justified by (7.4), and
(5.4) gives

```text
Tau_L(lambda_L(a_f))
 =integral_T T_theta(f)dm(theta)
 =L sum_(r in Z) f(rL) integral_T exp(ir theta)dm(theta)
 =L f(0).                                             (7.5)
```

Every nonzero return `r!=0` is killed by dual Haar.  At probability orbit
scale the entire trace is `Tau_L/L` and the value is `f(0)`; the proof never
mixes this rescaling with the locked length-scale value (7.5).  This closes
P8-4.

## 8. P8-5 — character-fibre C*-traces

Use the fixed isomorphism `Phi` and define, for `a in (A_L)_+`,

```text
tau_theta(a)=Tr_(H_0)(Phi(a)(theta)) in [0,infinity]. (8.1)
```

Its exact positive domain is

```text
D_(tau_theta)+
 ={a in (A_L)_+: Tr(Phi(a)(theta))<infinity}.
```

Its linear trace ideal is the pullback of the trace-class ideal under the
single evaluation representation; in particular it contains every `a_f` by
(5.2).  Equation (8.1) has the following properties.

1. It is a trace because the ordinary extended trace on `K(H_0)` is tracial.
2. It is norm lower semicontinuous: evaluation is continuous and the positive
   operator trace is the supremum of its finite-rank compressions.  This is
   also the pullback principle of ERS, Theorem 3.11 (physical p.12).
3. It is densely defined and semifinite.  For `a>=0`, functional calculus
   gives `(a-epsilon)_+ -> a` in norm; at the chosen fibre the positive compact
   operator `(Phi(a)(theta)-epsilon)_+` is finite rank, so each approximant
   has finite `tau_theta`.
4. It is nonfaithful: if a nonzero positive `g in C(T)` satisfies
   `g(theta)=0` and `e` is rank one, then `g tensor e` is nonzero but has
   zero weight.
5. It is genuinely unbounded: `tau_theta(1 tensor P_N)=N` for finite-rank
   projections of rank `N`.

The ordinary/extended-positive/linear domains have therefore not been
conflated.  On the time kernels, (5.3)--(5.4) give

```text
tau_theta(a_f)
 =L sum_(r in Z) f(rL)exp(ir theta).                  (8.2)
```

In particular the group-theoretically frozen trivial character gives

```text
tau_0(a_f)=L sum_(r in Z) f(rL).                      (8.3)
```

This proves the full two-sided repetition ledger and closes P8-5.  It does
not make `tau_0` normal on (6.6), nor does agreement on the kernels `a_f`
identify it with the regular trace.

## 9. P8-6 — finite corner and no normal extension

The Hilbert space `H_0` is infinite dimensional.  From (4.2),

```text
A_L=C(T) tensor K(H_0),
Z(A_L)=0,
ZM(A_L)=C(T) tensor 1.
```

The centre is zero because the only scalar compact operator on an
infinite-dimensional Hilbert space is zero.  Also,
`tau_theta(f tensor 1)=infinity` whenever `f>=0` and `f(theta)>0`; the
multiplier centre is therefore not the finite witness.

Choose a rank-one projection `e in K(H_0)` and put

```text
p=1 tensor e in A_L.
```

This is a full projection because `K(H_0)eK(H_0)` densely spans
`K(H_0)`, and

```text
pA_Lp=C(T)p ~= C(T),
tau_theta(p)=1.                                      (9.1)
```

Under the same faithful regular representation, not a new representation,

```text
pM_L^reg p=L-infinity(T,dm)p ~= L-infinity(T,dm).     (9.2)
```

This proves the image and closure of the same full finite projection along the
fixed local map.

### 9.1 Decreasing-peak contradiction

Suppose an extended-positive normal weight `W` on `(M_L^reg)_+` extends the
same `tau_theta` from `(A_L)_+`.  A fortiori this covers a hypothetical normal
trace extension.  Since `W(p)=1`, its compression to the positive cone of
`pM_L^reg p` is finite and bounded:

```text
0<=x<=||x||p  implies  W(x)<=||x||W(p)=||x||.
```

It is therefore a normal positive functional `omega` on (9.2).  On the
continuous corner, extension means

```text
omega(hp)=h(theta),  h in C(T), h>=0.                 (9.3)
```

Let `d` be the circle metric and

```text
h_n(z)=max(1-n d(z,theta),0).
```

Then `h_n` decreases to zero as an element of `L-infinity(T,dm)`: its
pointwise limit is supported on the Haar-null singleton `{theta}`.  Normality
of the finite functional forces `omega(h_np)` to decrease to zero.  But (9.3)
gives `omega(h_np)=1` for every `n`, a contradiction.

Hence there is **no normal extended-positive weight**, and in particular no
normal trace, on `M_L^reg` extending `tau_theta` along the fixed local map.
The argument uses only the finite corner and does not pretend that point
evaluation is defined on an arbitrary `L-infinity` representative.

The obstruction is independent of the proof-device projection.  More
generally, if `q in C(T,K(H_0))` is any continuous full rank-one projection,
then fibrewise rank one gives

```text
qA_Lq={h q:h in C(T)},
qM_L^reg q={h q:h in L-infinity(T,dm)},
tau_theta(q)=1.
```

The scalar coefficient is continuous in the first line and measurable in the
second, so the same peaks give the same contradiction.  Constant rank-one
projections are, in addition, unitarily conjugate by constant unitaries.  Thus
neither the chosen matrix unit nor the choice-dependent trivialization is
inserted into source data.  Point evaluation is intrinsic on the continuous
corner because `h -> hq` is injective; it is never applied to an arbitrary
Haar-a.e. representative before compression.

### 9.2 Singular corner-state extensions exist and are nonunique

The preceding theorem excludes **normal** extension.  It does not say that
point evaluation has no positive extension to the measurable corner.
Because `C(T)` embeds isometrically in `L-infinity(T,dm)` (Haar has full
support), the positive Hahn--Banach/state-extension theorem gives states on
`L-infinity(T,dm)` extending `delta_theta`.

Nonuniqueness can be seen without selecting a value for a null-set
representative.  Choose a measurable set `E` with alternating shrinking
annuli about `theta`, so that every sufficiently small neighbourhood contains
positive-measure subsets of both `E` and `E^c`.  Let `A_n` and `B_n` be such
subsets inside the radius-`1/n` neighbourhood, with `A_n subset E` and
`B_n subset E^c`, and form the normal averaging states

```text
omega_n^E(x)=m(A_n)^(-1) integral_(A_n) x dm,
omega_n^c(x)=m(B_n)^(-1) integral_(B_n) x dm.
```

Weak-* cluster points in the state space of `L-infinity(T,dm)` agree with
`delta_theta` on every continuous function, by uniform continuity.  One has
value one on `1_E`; the other has value zero.  They are therefore distinct
state extensions.  Each cluster state is purely singular: if a normal
positive functional `psi` were dominated by it, the measure
`psi|_(C(T))` would both be absolutely continuous with respect to Haar and be
dominated by `delta_theta`, hence would vanish; then `psi(1)=0`.

Via (9.2), these are singular states of the finite corner.  Compression also
produces states of `M_L^reg` that agree with point evaluation on `pA_Lp`.
They are **not** asserted to extend the full unbounded character trace
`tau_theta` on all of `A_L`; this proof neither constructs nor rules out a
singular extended-positive trace on all of `M_L^reg`.  This distinction is
essential: the proved negative statement is exactly no **normal** extension
of `tau_theta`, while singular corner-state extensions exist and are
nonunique.

Sections 9.1--9.2 close P8-6 on the fixed one-orbit map.

## 10. Source ownership and new-proof ledger

| Ingredient | Exact owner / locator | Use in this note |
|---|---|---|
| Homogeneous-space completion and induced representations | Williams, Theorems 4.30 and 5.12, printed pp.138 and 161; retained `grp-williams-crossed-products-draft3.1.pdf`, SHA `3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2` | Load-bearing source theorem for (4.2)--(4.3) |
| Full/reduced equality | Williams, Theorem 7.13, printed p.199, same retained file | Load-bearing amenability theorem for (4.1) |
| Historical imprimitivity | Green, Proposition 3, printed p.203; retained `grp-green-local-structure-1978.pdf`, SHA `bca0701f16e965424563004c5e6d9eec2a9310e05b860857f23d97b2f8819b3d` | Corroborative only; not used to upgrade Morita equivalence |
| Plancherel weight and dual Haar normalization | Renault, physical pp.3--4; retained `trace-renault-2021-dual-haar.pdf`, SHA `d703672f7d3f70256a3f83ae5ba6c3cdd7ab87a65249fb51d7b544cc3095387f` | Source template for dual Haar and FNS weight properties |
| Invariant-measure crossed-product trace | Bourne--Rennie, Lemma 7.4, physical p.36; retained `trace-bourne-rennie-2018-crossed-product.pdf`, SHA `57e7ba6c1908a20956f783efbd8288be6d75e10d42d1d1b026f7f46bbef4f5f5` | Source template corroborating (7.1)--(7.3) |
| Pullback of l.s.c. traces | ERS, Theorem 3.11, physical p.12; retained `trace-elliott-robert-santiago-2011-lsc-traces.pdf`, SHA `5d2bebc7199c8243b4532db96bf1677e5ee54f968d8d16be671b58c4fa93d4da` | Source theorem corroborating lower semicontinuity in Section 8 |
| Fourier decay and unshifted Poisson summation | Laugesen, Definition 14.1, Theorems 14.10--14.11 and 23.5, physical pp.79, 84--85, 137; retained `harm-laugesen-2009-harmonic-analysis.pdf`, SHA `b1ef00490b91e492cd9906849256a172a0ea261f7d19fa6b6265ef425d78d51c` | Load-bearing analytic inputs for Section 5 |
| Morita induction of l.s.c. traces | Combes--Zettl, retained `trace-combes-zettl-1983-morita-traces.pdf`, SHA `3e7ba9278b12848df4af02fe00ffef8f26114c44ec9ab7c4d995db29614e0a39` | Corroborative only; the exact evaluation pullback is proved directly |

The retained trace/analysis PDFs have passing preflight records.  The older
Williams and Green sidecars report environmental `UNAVAILABLE`, not damaged
files; their text extraction, page counts, printed theorem locators, and the
Williams induced-function formulas were independently checked in the Phase-2
audit.  No unverified secondary summary is load-bearing here.

The following are Paper-8 elementary/operator lemmas proved in this note,
rather than claims attributed to those sources:

- conversion of the locked convolution to the crossed-product convention;
- the exact frequency and return-phase calculation;
- the concrete Zak intertwiner, its faithfulness consequence, and the fixed
  bicommutant (6.6);
- the Hilbert--Schmidt/identity-coefficient formula and exact FNS domains;
- trace-class membership, shifted Poisson summation, and justified dual-Haar
  cancellation;
- l.s.c./semifiniteness/nonfaithfulness of the evaluation trace on the exact
  pullback domain; and
- the full finite-corner decreasing-peak obstruction and the separate
  nonuniqueness of singular corner-state extensions.

## 11. Devil's-advocate closure and theorem status

| Target | Verdict | Exact result |
|---|---|---|
| P8-2 | **CLOSED, one orbit** | `A_L=C*_r(O rtimes R) ~= C(T) tensor K(H_0)` as an actual unstabilized isomorphism; induced field and sign fixed |
| P8-3 | **CLOSED, one orbit** | every `pi_theta(a_f)` is trace class and satisfies the `+ir theta` shifted Poisson formula |
| P8-4 | **CLOSED, one orbit** | faithful fixed regular representation, bicommutant `L-infinity(T) bar_tensor B(H_0)`, exact FNS domains, and value `L f(0)` |
| P8-5 | **CLOSED, one orbit** | `tau_0=delta_0 tensor Tr` is an l.s.c. densely defined semifinite nonfaithful C*-trace and gives the full repetition ledger |
| P8-6 | **CLOSED, fixed one-orbit map** | full trace-finite rank-one corner; singular corner states exist/nonunique; no normal extended-positive extension of `tau_theta` |

Final adversarial checks:

- The source-fibre regular representation is explicitly written, intertwined,
  and proved faithful before its bicommutant is named.
- `Tau_L` is defined first on the positive cone; `m_Tau`, `n_Tau`, and the
  bounded `L1` domain are separately stated before tracing a complex kernel.
- Length Haar `du`, probability orbit Haar `du/L`, and dual probability Haar
  `dtheta/(2pi)` never exchange roles.
- The character weight is finite on the chosen full corner, generally
  infinite on the multiplier centre, and nonfaithful on `A_L`.
- The peak argument rules out only normal extension.  Singular corner-state
  extensions are explicitly constructed and are not misreported as
  extensions of the full unbounded trace.
- No proof borrows a packet algebra, transverse probability, packet mass,
  Paper-7 proxy, target Euler expression, fitted phase, determinant, or zero
  data.

The packet Hausdorff/LCH completion, packet regular algebra, and packet
same-map finite-corner transport remain withheld by `phase2_final_gate.md`.
Accordingly the registered packet-level primary extension outcome remains
`NOT_TESTABLE`; this local no-normal-extension theorem is not promoted to a
packet `REFUTE`.  No A2 determinant, A3 structure, A4, or Route-B credit is
created by P8-2--P8-6.
