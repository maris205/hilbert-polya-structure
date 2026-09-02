# RCR focused theorem contract

**Freeze status:** `MATHEMATICS FROZEN / OWNER_AMBER / HOLD_EXTERNAL`  
**Numbering status:** no paper number assigned  
**Scope:** uniform two-dimensional anchored lattice rectangles only

## Literal system

For positive integers `a,b`, let `(A_0,B_0)=(a,b)`.  Given
`(A_t,B_t)=(x,y)`, draw independent

```text
I_(t+1)~Uniform{1,...,x},
J_(t+1)~Uniform{1,...,y},
```

and set `(A_(t+1),B_(t+1))=(I_(t+1),J_(t+1))`.  State `(1,1)` is absorbing.
All hitting times start at time zero.

## Theorem A — one-coordinate exact law

Let `X_0=m`, let `X_(t+1)` be uniform on `{1,...,X_t}`, and set
`H_m=inf{t>=0:X_t=1}`.  Then `H_1=0`.  For every `m>=2`,

```text
E[z^H_m]=z(m-1)!/prod_(r=2)^m(r-z),             |z|<2.       (A1)
```

If `Z_2,...,Z_m` are independent and

```text
P(Z_r=q)=(r-1)/r^(q+1), q>=0,
```

then

```text
H_m =_d 1+sum_(r=2)^m Z_r.                                    (A2)
```

Put `A_(m,r)=(-1)^(r-2)binom(m-1,r-1)`.  For every integer `t>=0`,

```text
P(H_m>t)=sum_(r=2)^m A_(m,r)r^(-t),                            (A3)
P(H_m<=t)=1-sum_(r=2)^m A_(m,r)r^(-t).                         (A4)
```

For `t>=1`,

```text
P(H_m=t)=(m-1)sum_(r=2)^m
 (-1)^(r-2)binom(m-2,r-2)r^(-t).                              (A5)
```

Writing `h_n=sum_(q=1)^n q^(-1)` and
`h_n^(2)=sum_(q=1)^n q^(-2)`,

```text
E H_m=1+h_(m-1),
Var H_m=h_(m-1)+h_(m-1)^(2),
P(H_m=1)=1/m,
lim_(t->infinity)2^t P(H_m>t)=m-1.                            (A6)
```

The rational quotient in (A1) is the meromorphic continuation; the PGF has
exact radius two.

## Theorem B — exact rectangle absorption clock

Let

```text
T_(a,b)=inf{t>=0:(A_t,B_t)=(1,1)}.
```

On the literal product construction,

```text
T_(a,b)=max(H_a,H_b)                                          (B1)
```

with independent coordinate clocks.  If `F_m(t)=P(H_m<=t)` and
`F_m(-1)=0`, then for every integer `t>=0`,

```text
P(T_(a,b)<=t)=F_a(t)F_b(t),                                   (B2)
P(T_(a,b)=t)=F_a(t)F_b(t)-F_a(t-1)F_b(t-1).                   (B3)
```

With empty sums understood when a side is one, the PGF is

```text
E[z^T]=1+(z-1)[
 sum_(r=2)^a A_(a,r)/(1-z/r)
 + sum_(s=2)^b A_(b,s)/(1-z/s)
 - sum_(r=2)^a sum_(s=2)^b A_(a,r)A_(b,s)/(1-z/(rs))].       (B4)
```

For every nonabsorbing start this is a PGF on `|z|<2` and has exact radius
two.  The first two raw moments are

```text
E T=
 sum_r A_(a,r)r/(r-1) + sum_s A_(b,s)s/(s-1)
 - sum_(r,s)A_(a,r)A_(b,s)rs/(rs-1),                          (B5)

E T^2=
 sum_r A_(a,r)r(r+1)/(r-1)^2
 + sum_s A_(b,s)s(s+1)/(s-1)^2
 - sum_(r,s)A_(a,r)A_(b,s)rs(rs+1)/(rs-1)^2.                 (B6)
```

Moreover:

```text
T_(a,b)=0 a.s. iff (a,b)=(1,1);
P(T_(a,b)=1)=1/(ab) for (a,b)!=(1,1);
support(T_(a,b))={1,2,...} for (a,b)!=(1,1);
lim_(t->infinity)2^t P(T_(a,b)>t)=a+b-2.                      (B7)
```

If `a,b>=2`,

```text
max(EH_a,EH_b)<E T_(a,b)<EH_a+EH_b.                           (B8)
```

If one side is one, `T` equals the other coordinate clock and the
corresponding equalities replace (B8).

## Theorem C — every-target transition and Green atlas

For `1<=k<=r<=m`, define

```text
C_(m,k;r)=(-1)^(r-k)(m-1)!/[(k-1)!(r-k)!(m-r)!].              (C1)
```

For every accessible target `1<=i<=a`, `1<=j<=b` and every `t>=0`,

```text
P^t_((a,b),(i,j))
=sum_(r=i)^a sum_(s=j)^b
 C_(a,i;r)C_(b,j;s)(rs)^(-t).                                (C2)
```

The discounted every-target potential is

```text
U_((a,b),(i,j))(z)
=sum_(r=i)^a sum_(s=j)^b
 C_(a,i;r)C_(b,j;s)/(1-z/(rs)).                              (C3)
```

For a transient target `(i,j)!=(1,1)`, the Green kernel, visit probability,
and defective first-hit PGF are respectively

```text
K_((a,b),(i,j))=U_((a,b),(i,j))(1),                           (C4)

P_((a,b))(tau_(i,j)<infinity)
=(ij-1)K_((a,b),(i,j))/(ij),                                 (C5)

E_((a,b))[z^tau_(i,j);tau_(i,j)<infinity]
=(1-z/(ij))U_((a,b),(i,j))(z).                               (C6)
```

If the start equals the transient target, `K=ij/(ij-1)`, the hit probability
is one, and `tau=0`.  If `i>a` or `j>b`, all transition, potential, and hit
quantities are zero.  For target `(1,1)`, the hit probability is one, the
killed-before-absorption Green is zero, and ordinary occupation is infinite;
for `|z|<1`,

```text
U_((a,b),(1,1))(z)=E[z^T_(a,b)]/(1-z).                         (C7)
```

Theorem C is the structural/spatial axis; it is not a reformulation of the
absorption-time law.

## Proof and evidence contract

- `PROOF_PACKAGE.md` supplies the all-parameter deductions.
- `DERIVATION_PACKAGE.md` supplies the notation, scouting audit, derivation
  map, and exact formula development.
- `verify_rcr_focused.py` and `CANONICAL.txt` provide finite exact
  falsification pressure only.
- `OWNER_FOCUSED_AUDIT.md` owns the release ceiling.  A source non-hit proves
  neither novelty nor priority.

## Owner-subtracted ceiling

The strict embedded one-coordinate chain, its harmonic mean and independent
visit indicators, generic lower-triangular absorption theory, generic
first-step/resolvent algebra, independent-clock maxima, geometric sums, and
tensor-product transitions receive zero contribution credit.  The only
potentially residual conjunction is the literal anchored-rectangle process
with its complete two-dimensional exact clock and every-target potential.
That residual remains `OWNER_AMBER`, so no manuscript drafting, numbering,
posting, circulation, attribution, or submission is authorized.

## Nonclaims

No theorem is asserted for nonuniform sampling, continuous coordinates,
higher-dimensional boxes, moving anchors, noisy inference, cover times,
quasi-stationarity, scaling limits, or controlled variants.  No reduced-form
claim is made at cancelled rational poles.
