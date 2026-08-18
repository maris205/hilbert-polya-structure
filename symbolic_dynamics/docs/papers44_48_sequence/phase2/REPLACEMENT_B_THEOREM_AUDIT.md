# Replacement B Theorem Audit — Isospectral Arithmetic Retractions

## Status and ownership subtraction

`PHASE2 GO / INDEPENDENT PROOF AUDIT PASSED / NO AUTHORITY WRITE`

Generic weighted-composition theory owns the rank-one fiber framework.
Papers 27--28 already own the project-level lessons that ordinary cyclic
invariants ignore oblique geometry, that one incidence family has a
similarity wall at one, and that adjoint Gram data can create separate
Schatten behavior.  None of those general lessons is counted here.

The candidate is admissible only as a new arithmetic theorem comparing two
isospectral retractions, including exact singular Weyl constants and their
crossover,
maximal-order Riesz instability, and a separate self-commutator ideal law.

## Frozen family

For `h>=2`, let `F_h` be the positive `h`-free integers and define

```text
tau_h(n)   = product_p p^min(v_p(n),h-1),
omega_h(n) = product_p p^(v_p(n) mod h).
```

On `ell^2(N)`, for complex `s` with `sigma=Re(s)>0`, define

```text
S_{h,s} e_n = n^(-s/2)e_{tau_h(n)},
M_{h,s} e_n = n^(-s/2)e_{omega_h(n)}.
```

Norm and ideal statements depend only on `sigma`; the complex phases are
absorbed by diagonal unitaries.  Both maps fix every `m in F_h`.

## Exact block theorem

For `m in F_h`, write

```text
J_h(m)={p:v_p(m)=h-1}.
```

The fibers are orthogonal rank-one blocks.  Their unique nonzero singular
values satisfy

```text
rho_S(m)^2 = m^(-sigma) product_{p in J_h(m)}(1-p^(-sigma))^(-1),
rho_M(m)^2 = m^(-sigma) zeta(h sigma).
```

The second formula is legal exactly for `sigma>1/h`, because
`omega_h(n)=m` iff `n=m a^h`.

Consequences:

```text
S bounded and compact  <=> sigma>0,
M bounded and compact  <=> sigma>1/h,
S in S_q               <=> sigma>2/q,
M in S_q               <=> sigma>max(1/h,2/q).
```

On each block `T^k=m^{-(k-1)s/2}T`.  Thus

```text
S^k in S_q <=> k sigma q>2,
M^k in S_q <=> sigma>1/h and k sigma q>2.
```

The second line explicitly retains the bounded-existence wall of `M`; a
formal power cannot be used to bypass it.

## Isospectral cyclic ledger

Both systems have the same simple nonzero eigenvalues

```text
{m^(-s/2):m in F_h}.
```

On the common bounded domain, and only when `k sigma>2`,

```text
Tr(S^k)=Tr(M^k)
       =sum_{m in F_h}m^(-ks/2)
       =zeta(ks/2)/zeta(hks/2).
```

All ordinary Fredholm or higher regularized determinants built from legal
power traces therefore coincide.  This equality is a negative control, not
evidence of geometric equivalence.

## Exact similarity phase

The spectral projection onto the nonzero eigenline in block `m` has norm

```text
P_S(m)=product_{p in J_h(m)}(1-p^(-sigma))^(-1/2),
P_M(m)=sqrt(zeta(h sigma)).
```

Uniform block diagonalizability gives

```text
S is boundedly similar to a compact normal diagonal operator <=> sigma>1,
M is boundedly similar to one throughout its domain sigma>1/h.
```

For `S`, the maximum over `m<=x` is attained by

```text
m=(product_{p<=y}p)^(h-1)
```

with the largest admissible `y`.  Hence

```text
sigma>1: max P_S(m) -> sqrt(zeta(sigma)),
sigma=1: max P_S(m) ~ sqrt(e^gamma log log x),
0<sigma<1:
 log max P_S(m)
 ~ (h-1)^(sigma-1)(log x)^(1-sigma)
    /[2(1-sigma)log log x].
```

These maximal-order laws, not the generic existence of oblique projections,
are part of the claimed arithmetic contribution.

## Singular versus eigenvalue Weyl laws

Define

```text
w_{h,sigma}(m)=m product_{p in J_h(m)}(1-p^(-sigma))^(1/sigma).
```

Then `rho_S(m)=w_{h,sigma}(m)^(-sigma/2)`.  Its Dirichlet series has a
simple pole at one with residue

```text
C_{h,sigma}=product_p (1-p^(-1)) *
 [1+sum_{e=1}^{h-2}p^(-e)
   +p^(-(h-1))(1-p^(-sigma))^(-1/sigma)].
```

The required Tauberian theorem is

```text
#{m in F_h:w_{h,sigma}(m)<=x} ~ C_{h,sigma}x,
s_n(S) ~ (C_{h,sigma}/n)^(sigma/2).
```

It follows from the exact generalized Dirichlet factorization

```text
F_(h,sigma)(z)=sum_(m in F_h) w_(h,sigma)(m)^(-z)
              =zeta(z)G_(h,sigma)(z),
G_(h,sigma)(z)=product_p (1-p^(-z))L_p(z),
L_p(z)=sum_(e=0)^(h-2)p^(-ez)
       +p^(-(h-1)z)(1-p^(-sigma))^(-z/sigma).
```

After the `p^(-z)` cancellation, the local remainder is
`O(p^(-h Re(z)))+O(p^(-(h-1)Re(z)-sigma))`.  Hence `G` is locally uniformly
convergent and holomorphic for

```text
Re(z)>theta_(h,sigma)
     =max(1/h,(1-sigma)/(h-1))<1.
```

The positive generalized counting measure and Wiener--Ikehara then give the
displayed residue and Weyl law.  This strip, positivity, and the simple pole
at one are part of the proof obligation; they are not inferred from a
finite numerical fit.

For the modulo retraction,

```text
D_{h,sigma}=zeta(h sigma)^(1/sigma)/zeta(h),
s_n(M) ~ (D_{h,sigma}/n)^(sigma/2).
```

The common eigenvalue sequence instead has constant `1/zeta(h)`:

```text
|lambda_n| ~ ((1/zeta(h))/n)^(sigma/2).
```

The two singular constants are reported by their explicit formulas; no
global inequality is claimed without a separate proof.  They have the exact
nontrivial coincidence at `sigma=1`:

```text
C_(h,1)=D_(h,1)=1 for every h>=2.
```

Indeed, every Euler local factor of `C_(h,1)` is one and
`D_(h,1)=zeta(h)/zeta(h)`.  At that same point the saturated system is not
boundedly similar to normal, while the modulo system is.  Thus identical
eigenvalues, regularized determinants, and even identical leading singular
Weyl constants at the crossover still do not determine the nonnormal
geometry.  Away from the crossover the explicit constants record a further
distortion.  The Tauberian continuation and endpoint hypotheses must be
proved, not inferred numerically.

## Self-commutator wall

For a rank-one block with singular norm `rho` and eigenvalue modulus `a`,
`[T^*,T]` has two equal nonzero singular values

```text
c=rho^2 sqrt(1-a^2/rho^2).
```

Therefore

```text
[S^*,S] in S_q <=> sigma>1/q,
[M^*,M] in S_q <=> sigma>max(1/h,1/q).
```

Necessity for `S` is visible after fixing one saturated prime.  For `h=2`,
vary a second saturated prime; for `h>=3`, vary a prime of exponent one.  In
both cases the angle factor is bounded below and the block is comparable to
`r^(-sigma)`.  Sufficiency follows from the Euler majorant for `rho^(2q)`.
For `h=2`, put

```text
lambda_m=product_{p|m}(p^sigma-1)^(-1),
delta_m=product_{p|m}(1-p^(-sigma)).
```

For `sigma>1/2`, each block has two singular values
`lambda_m sqrt(1-delta_m)`, and the following two Euler products converge
separately:

```text
||[S^*,S]||_2^2 = 2{
 product_p[1+(p^sigma-1)^(-2)]
 -product_p[1+p^(-2sigma)/(1-p^(-sigma))] }.
```

This wall `sigma=1/q` is distinct from the operator-ideal wall `2/q` and
the saturated similarity wall one.

## Required controls and evaluators

1. exact finite fiber matrices versus the closed block formulas;
2. independent Euler products for ideal norms and power traces;
3. singular-value counting versus both Weyl constants;
4. primorial maximum versus arbitrary squarefree/`h`-free search;
5. saturated versus modulo retraction with identical eigenvalue ledger;
6. a free-UFD atom clone, which must reproduce the theorem and therefore
   defeats every rational-prime-selectivity interpretation;
7. P27--P29 claim subtraction: no novelty credit for the generic
   obliqueness, similarity, adjoint/Gram, counterterm, or
   regularized-determinant mechanisms;
8. the standard `h`-free-part map and Paper 43's `h`-free inventory receive
   zero object-novelty credit.

## Admission decision

The `h=2` radical block formulas alone are `STOP`.  The all-`h` isospectral
comparison plus exact maximal-order instability, the two singular Weyl laws
and their `sigma=1` crossover, the self-commutator wall, and the free-UFD
control remain paper-sized after the mandatory source and P27--P30/P43
subtractions.  The independent hostile audit reproduced every endpoint, the
Tauberian strip and residue, the similarity iff, the maximal-order constant,
and the commutator law.  Final Phase-2 decision: `GO_WITH_FIREWALL`.
