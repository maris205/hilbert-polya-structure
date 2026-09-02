# QTS freeze candidate — quadratic trace-square reciprocal dynamics

**Stage:** theorem-contract candidate, not a paper number.  
**Decision:** `SELECT_INTERNAL_OWNER_THIN_PENDING` -- direct polynomial-family
owner found; only the iterated functional-graph conjunction remains eligible.  
**External status:** `HOLD_EXTERNAL`.  
**Claim ceiling:** a bounded owner non-hit is not novelty, priority, or release
clearance.

## 1. Literal map and scope

Let `q` be an odd prime power, let `E=F_{q^2}`, and write

```text
Tr(x)=x+x^q,       N(x)=x^(q+1).
```

The carrier is the **whole field** `E`.  Define

```text
F(x)=Tr(x)^2 inv0(x),       inv0(0)=0.
```

This notation does not hide an essential denominator convention.  On every
element of `E`, including zero, the same function is the polynomial function

```text
F(x)=x+2x^q+x^(2q-1).                                      (1)
```

Indeed, for `x!=0`, expand `(x+x^q)^2/x`; both sides of (1) vanish at zero.
The odd-characteristic hypothesis is used by the trace-one conic and its
quadratic-discriminant census.  No characteristic-two claim is in scope.

## 2. Coordinate bijection and exact iterate

Put

```text
H={u in E: Tr(u)=1}.
```

The map

```text
E \ ker(Tr)  ->  F_q^* x H,
x             |-> (a,u)=(Tr(x),x/Tr(x))                    (2)
```

is a bijection with inverse `(a,u)|->au`.  If `c=N(u)`, then `c!=0`, and
direct calculation gives

```text
F(a,u)=(a/c,u^q).                                           (3)
```

Here the notation on the left means the coordinates (2), not a new map.  In
particular, `N(u^q)=N(u)=c`, so `c` is an invariant.  Induction gives the
pointwise all-iterate formula

```text
F^t(a,u)=(a c^(-t), u^(q^t)),       t>=0,                  (4)
```

where `u^(q^t)` is `u` for even `t` and `u^q` for odd `t`.

**Proof route.**  For `x=au`, inversion gives
`x^(-1)=a^(-1)u^q/N(u)`.  Hence
`F(x)=a u^q/c`.  Its trace is `a/c`, so renormalizing to trace one gives
`u^q`.  This simultaneously proves (3), preservation of `c`, and (4).

## 3. Recurrent set and sharp temporal law

The trace-zero line is the complete zero fibre:

```text
F^(-1)(0)=ker(Tr),       |ker(Tr)|=q.                       (5)
```

Every nonzero trace-zero point has tail one into the fixed point zero.  By
(3), the complement of the trace-zero line is permuted, so all of its
`q^2-q` points are recurrent.  Thus

```text
Rec(F)={0} union {x:Tr(x)!=0},       |Rec(F)|=q^2-q+1,
D_q(z)=q^2-q+1+(q-1)z.                                 (6)
```

The bound one is sharp for every odd `q`.  The component of zero is exactly a
fixed point with `q-1` depth-one leaves; every other component is a bare
directed cycle.

## 4. Every-target inverse theorem

For a target `y`, the fibre sizes are

```text
|F^(-1)(y)| = q,   y=0;
                 = 0,   y!=0 and Tr(y)=0;
                 = 1,   Tr(y)!=0.                           (7)
```

For the nonzero-trace case, put `b=Tr(y)`, `v=y/b`, and `c=N(v)`.  The unique
source in the coordinates (2) is

```text
u=v^q,       a=bc,       x=bc v^q.                          (8)
```

Equation (3) sends this source to `(b,v)`, and the coordinate bijection proves
uniqueness.  Consequently

```text
im(F)={0} union {y:Tr(y)!=0},       |im(F)|=q^2-q+1.        (9)
```

The fibre histogram is one target of size `q`, `q^2-q` targets of size one,
and `q-1` empty targets.  Its edge mass is therefore exactly `q^2`.

## 5. Norm-section census and pointwise periods

Let `chi` be the quadratic character of `F_q`, with `chi(0)=0`, and define

```text
S_q={c in F_q^*: chi(1-4c)=-1}.
```

The norm multiset on `H` is completely explicit:

```text
c=1/4       occurs once, at u=1/2;
c in S_q    occurs twice, at the conjugate pair u,u^q;
all others  occur zero times.                              (10)
```

Indeed, `u in F_q` and `Tr(u)=1` force `u=1/2`.  Otherwise the minimal
polynomial of `u` is `X^2-X+c`; it is irreducible exactly when its
discriminant `1-4c` is a nonsquare.  Conversely each such irreducible
quadratic supplies its two conjugate trace-one roots.  In particular,
`|S_q|=(q-1)/2`.

Write `ord(c)` for multiplicative order in `F_q^*` and put

```text
r_0=ord(4),
ell(c)=lcm(2,ord(c)).
```

The exact pointwise periods are:

```text
per(a/2)=r_0                            for a in F_q^*;
per(au)=ell(N(u))                       for u in H\{1/2}.   (11)
```

The first line follows because `F(a/2)=4(a/2)`.  In the second line, (4)
requires both `c^t=1` and an even `t`, since `u^q!=u`.

## 6. Fixed iterates, cycles, and zeta

For every `t>=1`, let `A_t=|Fix(F^t)|`.  Equations (10)--(11) give

```text
A_t = 1 +(q-1) 1_{r_0|t}
        +2(q-1) 1_{2|t} #{c in S_q: ord(c)|t}.             (12)
```

Equivalently, the first indicator can be written `1_{4^t=1}`, and the set in
the last term can be written `{c in S_q:c^t=1}`.  The exact number of cycles
of length `m` is either obtained from

```text
C_m=(1/m) sum_{d|m} mu(m/d) A_d,                            (13)
```

or read directly as

```text
C_m = 1_{m=1}
      +1_{m=r_0}(q-1)/r_0
      +sum_{c in S_q: ell(c)=m} 2(q-1)/m.                  (14)
```

Formula (14) accounts for all `q^2-q+1` recurrent points.  It also makes the
integrality transparent: for each `c`, the permutation (3) partitions its
`2(q-1)` points into cycles of their common period `ell(c)`.

The finite-map Artin--Mazur zeta function is therefore

```text
zeta_F(z)=(1-z)^(-1)
          (1-z^r_0)^(-(q-1)/r_0)
          product_{c in S_q}
          (1-z^ell(c))^(-2(q-1)/ell(c)).                  (15)
```

Generic Möbius inversion and zeta bookkeeping receive zero contribution
credit; the map-specific content is the coordinate conjugacy (2)--(4), norm
section (10), and their conjunction with (7).

## 7. External owner subtraction

Equation (1) places QTS literally inside Xiang-dong Hou's directly studied
trinomial family

```text
a x+b x^q+x^(2q-1)
```

at `(a,b)=(1,2)`.  Hou's 2014/2015 work completely determines which members
of that family are permutation polynomials, and the standard rewrite as
`x h(x^(q-1))` is explicit there.  Therefore the following receive **zero
credit**:

- the construction or identification of polynomial (1);
- its membership in the trinomial / `x h(x^(q-1))` family;
- the fact that it is not a permutation of the whole field;
- generic unit-circle, cyclotomic-mapping, or permutation-polynomial tools.

The only eligible residual is the conjunction of the full nonpermutation
functional graph: the explicit trace-kernel component, coordinate dynamics
(3)--(4), every-target law (7), norm-order cycle census (10)--(14), and zeta
product (15).  The retrieved owner text classifies permutation status; it did
not present this complete iterative graph.  That bounded distinction is not
clearance.  A source owning the graph conjunction kills QTS.

## 8. Internal collision firewall

| occupied paper | literal and temporal difference | proof/fibre difference | zero-credit overlap |
|---|---|---|---|
| P102, involutive norm dynamics | `a->aa*` on a split cyclic group algebra first synchronizes involution pairs and then squares; QTS is one quadratic field element, has a one-step trace-kernel star, and permutes its complement by (3) | P102 uses split Fourier inversion orbits and scalar squaring, with depth controlled by the `2`-part of `q-1`; QTS uses trace-one normalization, the norm conic, and conjugation, with `q/1/0` target fibres | fixed-iterate counts, scalar orders, Möbius inversion, and zeta products are generic and earn no separation credit |
| P125, quadratic-state shear | characteristic-two carrier `V x V`, pair update `(y,x+Q(x)y)`, depths through two and only periods `1/2/3/4`; QTS is odd-characteristic `E`, depth at most one, and periods from arbitrary norm orders | P125 uses a polar-bit quotient, quadratic-form type counts, and `0/1/2` fibres; QTS uses the bijection (2), discriminant census (10), and `q/1/0` fibres | the words “quadratic”, “finite field”, fibre atlas, and component/zeta census are zero credit |
| P150, zero-totalized Lyness | P150's affine pair recurrence has essential denominator strata, a depth-three exceptional in-tree, and generic period five.  QTS is the global polynomial (1), has only the trace-kernel star, and is a permutation off that line | P150 proves a five-stratum singular partition and Lyness arrows; QTS proves a trace/norm skew product.  Although both have `q/1/0` fibres and setwise carriers of size `q^2`, the image sizes and temporal silhouettes come from different equations | totalized inversion, finite-field rational-map language, fibre histograms, and zeta conversion are all zero credit |

The polynomial identity (1) is a sentinel against presenting QTS as another
arbitrary totalization convention.  P150's totalization changes singular
Lyness arrows; QTS's apparent inverse notation is merely a compact expression
for a globally defined polynomial function.

## 9. Exact control and remaining proof obligations

The deterministic verifier `verify_algebraic_scout.py` checks, over thirteen
odd prime fields `3<=p<=43`:

- all `8,253` literal states and targets;
- closure, the coordinate formula (3), pointwise periods (11), temporal law
  (6), image, and every fibre (7);
- every fixed count (12) for `1<=t<=2(p-1)`.

The QTS lane contributes `33,291` exact assertions.  The stored output is
`CANONICAL.txt`.  Enumeration is falsification pressure only.

Before any paper freeze, root review must still:

1. replay the theorem for nonprime odd prime powers with an independent
   finite-field implementation (the proof already treats prime powers);
2. citation-chain Hou's trinomial family and explicitly verify that no source
   owns the nonpermutation functional-graph conjunction;
3. independently rederive (10)--(15), especially characteristic three and
   order-one factor merging in the zeta product;
4. decide whether the residual conjunction is substantial after all generic
   finite-field, order, and zeta machinery is subtracted.

No paper number is assigned here.  The correct intake label is
`SELECT_INTERNAL_OWNER_THIN_PENDING`, not literal non-hit.  All external
actions remain `HOLD_EXTERNAL`.
