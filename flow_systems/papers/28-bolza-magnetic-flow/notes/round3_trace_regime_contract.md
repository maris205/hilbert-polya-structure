# P28 Round-3 source-bound trace-regime contract

Date: **2026-08-27**

ARS scope: Stage 1 research / Route A A0--A1.  This note freezes an exact
semiclassical trace subtype; it does not enumerate Bolza magnetic orbits,
instantiate the non-arithmetic control, or transfer credit to fixed `Delta^L`.

## 1. Primary-source lock

The governing source is Kordyukov and Taimanov, *Trace formula for the magnetic
Laplacian on a compact hyperbolic surface*, arXiv:2202.06055v3,
https://arxiv.org/abs/2202.06055 (Theorem 3 and equations (15), (16), and
(19)).  The source was checked directly on **2026-08-27**.

For a compact curvature-minus-one hyperbolic surface, a constant field `B=1`,
let `K` denote the source's degree-two quantization bundle.  For the tensor
family `K^m`, the source defines

```text
lambda_(m,j) = sqrt(nu_(m,j)+m^2),
Y_m(phi)     = sum_j phi(lambda_(m,j)-E m).
```

For `E>sqrt(2)`, `phi in S(R)` with compactly supported Fourier transform, the
source proves a full asymptotic expansion as `m->infinity`.  When
`supp(phi_hat)` avoids zero, its first periodic-orbit coefficient is a sum over
primitive conjugacy classes `h` and nonzero repetitions `k`.  At general `E`,
the period and action factors are

```text
T#(h) = E/sqrt(E^2-2) * log Norm(h),
S_k(h)= k sqrt(E^2-2) * log Norm(h)  (modulo the source phase convention).
```

The paper proves that above the critical level the closed magnetic orbits are
isolated and nondegenerate.  This is a theorem about primitive hyperbolic
conjugacy-class owners; it is not a rational-prime dictionary.

## 2. Frozen subtype: a source-compatible square root

The project field `b=+1/2` has a degree-one Hermitian line bundle `L` with
curvature `(1/2) Omega_g`.  Since multiplication by two on the degree-zero
Picard torus is surjective, a degree-two bundle on a genus-two surface admits
degree-one square roots.  A compatible unitary connection is selected along
with the root.  Such roots are not canonical: flat two-torsion changes the
choice.  Round 3 therefore narrows the candidate by the following explicit
`[MODELING_CHOICE]`:

```text
(L,connection) is chosen so that (L^2,connection^2)
is the B=1 quantization bundle K used by the source theorem.
```

This is a subtype, not a claim about every degree-one connection.  The
negative-field subtype uses `L_dual`.  Restrict to the even tensor subsequence

```text
N=2m,        L^N=(L^2)^m=K^m.
```

The identity is exact at the bundle, connection, Hilbert-space, and operator
levels under the stated modeling choice.

## 3. Project operator, shell, and energy window

For even `N`, freeze a real-even `phi in S(R)` whose Fourier transform has
compact support disjoint from zero, and set

```text
P_N       = sqrt(Delta^(L^N)+N^2/4),
h         = 1/N,
h P_N     = N^(-1) sqrt(Delta^(L^N)+N^2/4),
E_project = sqrt(5)/2,
Y_N(phi)  = Tr phi(P_N-(sqrt(5)/2)N).
```

The principal Hamiltonian is

```text
H_(1/2)(x,p)=sqrt(|p|^2+1/4).
```

Therefore the frozen center `H_(1/2)=sqrt(5)/2` gives

```text
|p|^2 = 5/4-1/4 = 1,
```

exactly the unit-speed shell fixed in Stage 1.  Since `b^2=1/4`, this shell is
strictly above the magnetic critical level.

The shell and the clock are not conflated.  The Stage-1 physical Hamiltonian is
`H0=|p|^2/2`, whose velocity has norm one on this shell.  The trace theorem uses
`H_(1/2)=sqrt(2H0+1/4)`, so on the frozen shell

```text
X_trace=(2/sqrt(5)) X_physical,
T_trace=(sqrt(5)/2) T_physical.
```

The two clocks have the same oriented trajectories but different periods.

If `lambda=(sqrt(5)/2)N+s` with `s=O(1)`, then the corresponding magnetic
Laplacian eigenvalue satisfies the exact algebraic identity

```text
nu = N^2 + sqrt(5) N s + s^2.
```

Thus the contract is an `O(1)` window for `P_N` and an `O(N)` window about
`nu=N^2` for `Delta^(L^N)`.  This is not the high-energy window of one fixed
operator.

## 4. Exact reduction and same-owner scaling lemma

With `m=N/2`, set the source energy to

```text
E=sqrt(5),       E0=E^2-1=4.
```

Then

```text
sqrt(nu_(N,j)+N^2/4)=sqrt(nu_(m,j)+m^2),
(sqrt(5)/2)N=sqrt(5)m,
Y_N(phi)=Y_m(phi).
```

The equality of spectral observables is not by itself an orbit-owner proof.
Let `Phi(x,p)=(x,q=2p)` map the project cotangent variables to the source
variables.  With the same sign convention for the canonical and magnetic
forms,

```text
Phi^*(omega_source)
  = Phi^*(omega_0(q)+Omega_g)
  = 2 omega_0(p)+Omega_g
  = 2(omega_0(p)+(1/2)Omega_g)
  = 2 omega_project,

Phi^* H_source
  = sqrt(|2p|^2+1)
  = 2 sqrt(|p|^2+1/4)
  = 2 H_project.
```

Both the symplectic form and Hamiltonian acquire the same factor two, so the
Hamiltonian vector fields are `Phi`-related with the same trace time.  The map
preserves the base curve, orientation, primitive/repetition owner, and trace
period.  It therefore supplies the missing same-owner identification between
the source `B=1,|q|=2` flow and the project `b=1/2,|p|=1` trace flow.

The source theorem now applies after the exact reindexing `m=N/2` on the
positive-field even subsequence.  Its expansion is in powers
`m^(1-j)=(N/2)^(1-j)`.  Specializing its primitive-orbit coefficient gives

```text
T#(h) = sqrt(5/3) log Norm(h),
phase = exp(-i k (sqrt(3)/2) N log Norm(h)).
```

Here `T#` is the trace-Hamiltonian period.  In the original physical unit-speed
clock the same primitive orbit has period

```text
T#_physical(h)=2/sqrt(3) log Norm(h).
```

Hence, for the source-compatible subtype,

```text
SEMICLASSICAL_EVEN_SUBSEQUENCE_TRACE_REGIME=SOURCE_BOUND
SEMICLASSICAL_EVEN_SUBSEQUENCE_MAGNETIC_ORBIT_OWNERSHIP=PROVED
```

The negative-field even subsequence follows by the antiunitary duality and
classical time reversal proved in Round 2.  We pair a positive-field oriented
owner `(h,k)` with the reversed negative-field owner `(h^(-1),k)`: the
primitive representative is reversed while the repetition index is held
fixed.  Thus the represented group elements are `h^k` and `h^(-k)`, the norm
is unchanged, and the action exponent changes sign.  For the frozen real-even
test function, the trace distribution is correspondingly paired.  This avoids
claiming an unqualified termwise conjugacy formula for arbitrary complex test
functions.  The result is `[PROVED]` trace ownership for the stated subtype,
not evidence for arithmetic-specific prime coding.

## 5. Control and claim boundary

The same syntactic window is registered for `b=0`, but its trace owner remains
`[OPEN]` in this project until the zero-field theorem is separately bound.  A
non-arithmetic genus-two metric with the same area and field is still
uninstantiated.  Odd `N`, arbitrary degree-one flat twists, and the full
all-`N` sequence are not covered by this exact reduction.

Nothing here transfers to the fixed operator `Delta^L`:

```text
FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN
FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
FIXED_OPERATOR_CREDIT_TRANSFER_ALLOWED=false
```

No formal A0--A4 tuple is assigned and Route B remains disallowed.  The next
executable artifact is a primitive Bolza conjugacy/magnetic-orbit ledger using
the frozen period, repetition, stability, holonomy, and action columns, followed
by the metric-matched non-arithmetic control.
