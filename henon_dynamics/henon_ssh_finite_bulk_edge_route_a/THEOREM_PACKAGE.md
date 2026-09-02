# Exact finite SSH theorem package

Let `M>=2`, let `v,w>=0`, and order the basis as
`(A_1,...,A_M,B_1,...,B_M)`.  Under open boundaries,

`H_O=[[0,T],[T*,0]]`,  `T=vI+wS_-`,

where `(S_-)_(j,j-1)=1`.  The chiral involution is
`Gamma=diag(I_M,-I_M)` and `Gamma H_O Gamma=-H_O`.

## 1. Characteristic polynomial

For `q_M(y)=det(yI-TT*)`,

```text
q_0=1,
q_1=y-v^2,
q_m=(y-v^2-w^2)q_(m-1)-v^2 w^2 q_(m-2).
```

If `v,w>0` and `x=(E^2-v^2-w^2)/(2vw)`, then

`det(EI-H_O)=(vw)^M[U_M(x)+(w/v)U_(M-1)(x)]`.

The prefactor is essential.  Since `det(T)=v^M`, there is no exact open
zero eigenvalue when `v>0`.

## 2. Sharp finite hyperbolic edge theorem

Write `r=w/v`.  A secular root has the hyperbolic form
`x=-cosh(kappa)<-1` exactly when

`r=sinh((M+1)kappa)/sinh(M kappa)`.

The right side is strictly increasing from `(M+1)/M` to infinity.
Therefore the open chain has exactly one hyperbolic root, hence exactly one
pair `+-E_edge`, if and only if

`w/v>(M+1)/M`.

For that unique `kappa>0`,

```text
E_edge = v sinh(kappa)/sinh(M kappa)
       = w sinh(kappa)/sinh((M+1)kappa),
a_j = (-1)^(j-1) sinh((M+1-j)kappa),
b_j = (-1)^(j-1) sinh(j kappa).
```

Then `(a,b)` has energy `+E_edge` and `(a,-b)` has energy `-E_edge`.
The inward ratios satisfy

```text
|a_(j+1)|/|a_j| < exp(-kappa),
|b_j|/|b_(j+1)| < exp(-kappa).
```

At equality `w/v=(M+1)/M`, `x=-1` and `E=v/M`.  The raw hyperbolic
vectors vanish as `kappa -> 0`; after dividing both sublattice vectors by
the common factor `kappa` (equivalently, after overall normalization), their
limiting signed linear tapers are `a_j=(-1)^(j-1)(M+1-j)` and
`b_j=(-1)^(j-1)j`.  This is a band-edge state, not a strict hyperbolic
state.  For fixed `r>1` and large `M`, `kappa_M -> log r` and

`E_edge ~ w(1-r^-2)r^-M`.

## 3. Periodic bulk and finite parity

For momenta `k_n=2pi n/M`, define

`q(k)=v+w exp(ik)`,
`h(k)=[[0,conj(q(k))],[q(k),0]]`.

The energies are `+-|q(k)|`.  Distinguish the continuum Bloch gap-to-zero
from the finite-ring sampled gap:

```text
Delta_infinity = min_{k in [-pi,pi]} |q(k)| = |v-w|,
Delta_M = min_{0<=n<M} |q(k_n)|
        = |v-w|                                      if M is even,
        = sqrt(v^2+w^2-2vw cos(pi/M))                if M is odd.
```

The corresponding central band gaps are `2 Delta_infinity` and
`2 Delta_M`.  With increasing `k`, the loop winds counterclockwise: its
winding is `+1` for `w>v`, `0` for `v>w`, and undefined at `v=w`.

Thus the bulk threshold is `w/v=1`, strictly below the finite open
hyperbolic threshold.  At `v=w>0`, a finite ring has a two-dimensional
zero sector exactly when `M` is even.  Odd `M` does not sample `k=pi` and
instead has `Delta_M=2v sin(pi/(2M))>0`, despite the gapless continuum
symbol.

## 4. Boundary faces

- `w=0`, `v>0`: `M` isolated `v`-dimers; `+v` and `-v` each have
  multiplicity `M`.
- `v=0`, `w>0`: `M-1` isolated `w`-dimers plus exact edge zeros at `A_1`
  and `B_M`; zero multiplicity `2`, and `+-w` each have multiplicity
  `M-1`.
- `v=w=0`: the `2M`-dimensional zero matrix.
- `v=w>0` under open boundaries: the uniform `2M`-site path with energies
  `2v cos(ell pi/(2M+1))`, `ell=1,...,2M`, hence no zero.
- `M=1`: the open intercell bond is absent and the eigenvalues are `+-v`;
  under the declared periodic convention it merges with the intracell bond
  and the eigenvalues are `+-(v+w)`.

## 5. Boundary-safe unitary propagation

Define `sinc(z)=sin(z)/z` by its entire continuation, `sinc(0)=1`.  Then

```text
U(t)=exp(-itH_O)
 = [[ cos(t sqrt(TT*)),       -it sinc(t sqrt(TT*)) T ],
    [ -it sinc(t sqrt(T*T))T*, cos(t sqrt(T*T))          ]].
```

No inverse is used, so the formula holds on every singular face.  Moreover
`Gamma U(t) Gamma=U(-t)=U(t)*`.

## 6. Exact mode-quench corollary

Let the initial and final hoppings be strictly positive and gapped.  For an
initial lower-band Bloch state, the final-evolution mode amplitude is

```text
g_k(t)=cos(E_f(k)t)+i c(k) sin(E_f(k)t),
c(k)=Re(conj(q_i(k))q_f(k))/(|q_i(k)||q_f(k)|).
```

A continuum momentum has `g_k(t)=0` at some real time if and only if

`(v_i-w_i)(v_f-w_f)<0`.

In that case

```text
cos(k*)=-(v_i v_f+w_i w_f)/(v_i w_f+w_i v_f),
t_n=(pi/2+n pi)/E_f(k*).
```

For a finite ring, this criterion is necessary but not sufficient: an exact
zero occurs only if some `k_n=2pi n/M` has the displayed cosine.  For the
audited quench `(3,1)->(1,5)`, `cos(k*)=-1/2`, so the grid is hit precisely
when `3` divides `M`.  This is a single-particle mode statement, not a
many-body DQPT claim.

## 7. Route-A verdict

The tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` and the
overall verdict is `ROUTE_A_REJECTED`.  The Hamiltonian is a natural
self-adjoint source quantization only; no target zero match is asserted.
