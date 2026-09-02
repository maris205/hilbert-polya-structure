# Derivation Package — traceless determinant shear

## Target

Independently derive the complete finite dynamics of

```text
X_m = { [[a,b],[c,a]] : a,b,c in F_{2^m} },
Phi(A)=A+det(A)I,
```

including iterates, recurrence, depths, images, every-target fibres, fixed
counts, exact periods, and recurrent-target ancestry.  The derivation also
tests whether the matrix presentation leaves a theorem-sized residual after
generic Frobenius/Artin--Schreier linear dynamics is assigned zero credit.

## Status

**COHERENT AFTER REFRAMING / EXTRA ASSUMPTION.**

The displayed iterate, depth, image, fibre, trace, and fixed-count formulas
are coherent.  The necessary reframe is decisive: determinant is not merely
a semiconjugacy.  The coordinate map

```text
H(A)=(b,c,det A)
```

is a bijective conjugacy from `Phi` to `id x id x D`, where
`D(x)=x^2+x`.  Thus the matrix wrapper has no residual functional-graph
content after the mandated Artin--Schreier subtraction.  Also, “cumulative
ancestry” equals the simple `2^min(t,s)` law only for a fixed recurrent
target; for a nonfixed recurrent target that number is the exact `t`-step
fibre, not the union of fibres through time `t`.

## Invariant Object

The organizing object is the determinant coordinate

```text
e=det A=a^2+bc,
```

viewed as a vector in the `m`-dimensional `F_2`-space `F_{2^m}` under the
Artin--Schreier linear operator `D=F+I`, with `F(x)=x^2`.

## Assumptions

- `m>=1`, `q=2^m`, and all matrix entries lie in the true finite field
  `F_q`.
- Matrices are represented by triples `(a,b,c)` for
  `[[a,b],[c,a]]`; characteristic two makes these exactly the traceless
  `2 x 2` matrices.
- `R_0(z)=0` and `R_t(z)=1+z+...+z^{t-1}` for `t>=1`.
- `s=2^{v_2(m)}` is the two-primary part of `m`.
- Depth means distance to the recurrent set.  “Exact `t`-step fibre” means
  `Phi^{-t}(B)`; “cumulative ancestry” means the literal union
  `union_{0<=j<=t} Phi^{-j}(B)`.
- Generic finite-field Frobenius, Artin--Schreier image/trace facts, primary
  decomposition of a linear map, kernel/image counts, and Möbius conversion
  receive zero contribution credit.

## Notation

- `delta(A)=det A=a^2+bc`.
- `F(x)=x^2` and `D=F+I`, so `D(x)=x^2+x`.
- `V=F_q` regarded as an `m`-dimensional `F_2`-space.
- `chi_m(z)=(z+1)^m+1`, the characteristic and minimal polynomial of `D`
  in a normal basis.
- `N` and `W` denote the zero-primary and invertible primary summands of
  `D`, respectively.

## Derivation Strategy

First replace the matrix coordinates by `(b,c,det A)` and prove this is a
bijection, not a lossy invariant.  Every temporal and inverse formula then
becomes ordinary linear algebra for `D`.  A normal basis supplies the cyclic
`F_2[z]`-module and its zero-primary multiplicity `s`; the nilpotent and
invertible factors give the depth, image, fibre, and period laws.  Finally,
keep exact-time fibres separate from cumulative unions along a nontrivial
cycle.

## Derivation Map

1. The scalar update of `a` gives the determinant update `e -> D(e)`.
2. Perfectness of `F_q` makes `(a,b,c) -> (b,c,e)` bijective.
3. Therefore the full functional graph is `q^2` copies of the graph of `D`.
4. A normal basis makes `D` cyclic with polynomial `chi_m`; the exact
   zero-primary exponent is `s`.
5. Primary decomposition yields the clock, core, depth census, image size,
   and uniform fibres.
6. The displacement polynomial `R_t` yields the matrix iterate and fixed
   count; Möbius inversion yields exact periods.
7. Cycle phase distinguishes exact-time ancestry from cumulative ancestry.

## Main Derivation

### Step 1 — determinant semiconjugacy

For `A=(a,b,c)`, characteristic two gives

```text
delta(A)=a^2+bc,
Phi(A)=(a+delta(A),b,c).
```

Hence

```text
delta(Phi(A))
 = (a+delta(A))^2+bc
 = delta(A)^2+delta(A)
 = D(delta(A)).
```

This establishes the claimed semiconjugacy, but it is not the strongest
available statement.

### Step 2 — the semiconjugacy is a full conjugacy

Define

```text
H:X_m -> F_q^3,       H(A)=(b,c,delta(A)).
```

Given `(b,c,e)`, the missing coordinate must satisfy

```text
a^2=e+bc.
```

Squaring is an automorphism of a finite field, so this equation has the
unique solution `a=(e+bc)^{2^{m-1}}`.  Thus `H` is bijective.  Step 1 now
gives the identity

```text
H Phi H^{-1}(b,c,e)=(b,c,D(e)).                 (1)
```

Equation (1) is the decisive gate result: the two off-diagonal entries are
passive labels and every component is copied `q^2` times from the classical
linearized polynomial `D`.

### Step 3 — pointwise iterates

Let `e=delta(A)`.  At round `j`, the diagonal entry is incremented by
`D^j(e)`.  Therefore, exactly,

```text
Phi^t(A)=A+R_t(D)e I,                             (2)
delta(Phi^t(A))=D^t(e).                           (3)
```

The relation between (2) and (3) is consistent because

```text
(D+I)R_t(D)=D^t+I,
```

and `D+I=F` is the squaring automorphism.

### Step 4 — the zero-primary exponent

Choose a normal basis of `F_q/F_2`.  Frobenius `F` acts as one cyclic shift,
so its characteristic and minimal polynomial are `z^m+1`.  Replacing
`F` by `D+I` gives

```text
chi_m(z)=(z+1)^m+1.                               (4)
```

Write `m=su` with `u` odd and `s=2^{v_2(m)}`.  In characteristic two,

```text
chi_m(z)=((z+1)^u+1)^s.
```

The polynomial `(z+1)^u+1` has a simple zero at `z=0`, since its linear
coefficient is `u=1 mod 2`.  Thus the exact `z`-adic order of `chi_m` is
`s`.  Cyclicity gives the primary decomposition

```text
V=N direct_sum W,
N isomorphic to F_2[z]/(z^s),
dim W=m-s,
D|_W invertible.                                  (5)
```

In particular the nilpotent part is one block of exact length `s`.

### Step 5 — recurrent core and depth census

The recurrent set of `D` is `W=im D^s`.  From (1),

```text
Rec(Phi)=H^{-1}(F_q^2 x W),
|Rec(Phi)|=q^2 2^{m-s}.                            (6)
```

The maximum tail is exactly `s`.  A state has depth at most `t` exactly
when its `N`-coordinate lies in `ker(D^t|_N)`, whose dimension is
`min(t,s)`.  Hence

```text
# {A:depth(A)<=t}=q^2 2^{m-s+min(t,s)},            (7)
```

and the exact shells are

```text
depth 0: q^2 2^{m-s},
depth j: q^2 2^{m-s+j-1},       1<=j<=s.           (8)
```

These sum to `q^3`.

### Step 6 — images and every-target fibres

Equation (1) gives

```text
im Phi^t=H^{-1}(F_q^2 x im D^t),
|im Phi^t|=q^2 2^{m-min(t,s)}.                     (9)
```

For a target `B` with `e=det B`,

```text
|Phi^{-t}(B)| =
  2^{min(t,s)},  if e in im D^t,
  0,             otherwise.                       (10)
```

The proposed condition

```text
R_t(D)e in im D^t                                (11)
```

is equivalent to `e in im D^t`, not an additional matrix constraint.  On
the quotient `V/im D^t`, the induced `D` is nilpotent and `R_t(D)` has
constant term one, so `R_t(D)` is invertible there.  Thus (11) vanishes in
the quotient exactly when `e` does.

At `t=1`, the standard Artin--Schreier identity

```text
im D=ker Tr_{F_q/F_2}
```

reduces (10) to `Tr(det B)=0`, with two sources for a feasible target.

### Step 7 — fixed counts and exact periods

By (2),

```text
Phi^k(A)=A iff R_k(D)e=0.                          (12)
```

Since `D` is cyclic with polynomial (4), the kernel of `R_k(D)` has
dimension

```text
kappa_m(k)=deg gcd(R_k(z),chi_m(z)).               (13)
```

The two passive coordinates give

```text
#Fix(Phi^k)=q^2 2^{kappa_m(k)}.                    (14)
```

For `k>=1`, the number of points of exact period `k` and the number of
`k`-cycles are, respectively,

```text
P_k=sum_{d|k} mu(k/d)#Fix(Phi^d),
C_k=P_k/k.                                         (15)
```

These are standard cyclic-module/Möbius consequences of (1).

### Step 8 — exact-time versus cumulative ancestry

Let `B` be recurrent, and let its determinant coordinate `e in W` have
period `r` under `D|_W`.  For every `t`, (10) gives the exact-time law

```text
|Phi^{-t}(B)|=2^{min(t,s)}.                        (16)
```

However, the recurrent coordinate of a `t`-step source is
`D_W^{-t}e`.  Exact fibres at different times are disjoint unless their
times agree modulo `r`; within one residue class their nilpotent kernels are
nested.  If

```text
t_j=j+r floor((T-j)/r),      0<=j<=min(T,r-1),
```

then the literal cumulative union has size

```text
| union_{0<=t<=T} Phi^{-t}(B) |
 = sum_{j=0}^{min(T,r-1)} 2^{min(t_j,s)}.           (17)
```

Only when `r=1` does (17) reduce to `2^{min(T,s)}`.  A minimal hostile
sentinel occurs at `m=3`: the nonzero recurrent determinant coordinates have
period three and `s=1`.  For such a target,

```text
|Phi^{-1}(B)|=2,
|Phi^0(B)^{-1} union Phi^{-1}(B)|=1+2=3.           (18)
```

Thus an unrestricted “recurrent-target cumulative ancestry equals
`2^{min(t,s)}`” claim is false.  It is correct if “ancestry” means exact
`t`-step fibre, or if the target is required to be fixed.

## Remarks and Interpretation

- The matrix formula looks nonlinear in `(a,b,c)`, but determinant is an
  invertible replacement for `a` once `b,c` are fixed.  The nonlinearity is
  therefore a coordinate artifact.
- The sharp tail `s` is the multiplicity of the zero factor in `chi_m`, not
  a new matrix-geometric invariant.
- The feasibility condition using `R_t(D)e` is algebraically correct but
  disguises the simpler direct condition `e in im D^t` supplied by the
  conjugacy.
- The exact period formula and Möbius census add no independent theorem axis
  after (1); they are ordinary linear functional-graph bookkeeping.

## Boundaries and Non-Claims

- `m=1`: `s=1`; there are four recurrent fixed matrices and four depth-one
  matrices.
- `m` a power of two: `s=m` and `W=0`; all recurrent points are fixed and
  the core has size `q^2`.
- `m` odd: `s=1`; exactly half of all states are recurrent and half have
  depth one, but the recurrent permutation can have nontrivial cycles.
- `t=0`: image is the whole carrier and every target fibre has size one.
- `t>=s`: image and fibre sizes stabilize, although the recurrent part can
  continue moving periodically.
- `k=0`: every state is fixed by `Phi^0`; formula (14) extends if
  `gcd(0,chi_m)=chi_m` is adopted.
- No novelty, priority, paper allocation, or external-release claim follows
  from the exact formulas.

## Open Risks

There is no unresolved algebraic risk in the tested contract.  The blocking
risk is value/ownership: (1) reduces the entire system to a standard
linearized polynomial.  Under the gate's mandatory zero-credit rule, no
owner-distinct or proof-engine-distinct residual remains.  The correct
candidate decision is therefore
`KILL_CONJUGATE_TO_CLASSICAL_ARTIN_SCHREIER_LINEAR_MAP`.
