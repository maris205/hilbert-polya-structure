# Exact witness ledger

## Role and evidence boundary

These witnesses are deterministic consequences of the frozen definitions.
They are controls for implementations and review, not reported experiment
outcomes. Exact integers and algebraic identities are canonical; displayed
decimals are orientation aids only and may not certify a theorem.

## W0: one-symbol zero boundary

For every $q\ge2$ and $A=[1]$,

$$
W_0=W_1=W_2=\cdots=1,
\quad c_v=d_v=h=0,
\quad Z(N)=1,
\quad E_{A,q}\equiv0.
$$

This catches spurious chain multiplicities, an omitted $W_0$, and any
nonzero residue introduced by an implementation.

## W1: full-shift zero boundary

For $A=J_d$, the $d\times d$ all-one matrix,

$$
W_\ell=d^\ell,\qquad c_v=\log d,\qquad d_v=0,
$$

and hence

$$
Z(N)=d^N,\qquad h=\log d,\qquad E_{A,q}\equiv0.
$$

Although $J_d$ is primitive, its non-Perron eigenvalues vanish. This is an
exact degeneracy control inside the theorem domain.

## W2: exact chain-length histogram

For every $q\ge2$, $N\ge1$, and $\ell\ge1$, the number of roots whose
truncated chain has length exactly $\ell$ is

$$
C_\ell(N)=
\left\lfloor\frac{N}{q^{\ell-1}}\right\rfloor
-2\left\lfloor\frac{N}{q^\ell}\right\rfloor
+\left\lfloor\frac{N}{q^{\ell+1}}\right\rfloor.
$$

Canonical projections are

$$
\sum_{\ell\ge1}\ell C_\ell(N)=N,
\qquad
Z(N)=\prod_{\ell\ge1}W_\ell^{C_\ell(N)}.
$$

Both sums/products terminate once $q^{\ell-1}>N$.

## W3: golden word counts

For

$$
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},
$$

the exact word ledger is

| $\ell$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $W_\ell$ | 1 | 2 | 3 | 5 | 8 | 13 | 21 |

Thus the exact increment at a cutoff with $\nu_2(N)=v$ is

$$
\frac{Z(N)}{Z(N-1)}=\frac{F_{v+3}}{F_{v+2}}.
$$

## W4: golden prefix counts

Direct source enumeration and the independent chain product must project to
the following exact ledger:

| $N$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $Z(N)$ | 1 | 2 | 3 | 6 | 10 | 20 | 30 | 60 | 96 | 192 | 288 |

No logarithmic approximation is needed to compare this table.

## W5: valuation/increment controls

At $N=1,2,3,4,8$, respectively,

| $N$ | $\nu_2(N)$ | exact ratio $Z(N)/Z(N-1)$ |
|---:|---:|---:|
| 1 | 0 | $2$ |
| 2 | 1 | $3/2$ |
| 3 | 0 | $2$ |
| 4 | 2 | $5/3$ |
| 8 | 3 | $8/5$ |

The intervening odd cutoffs always have ratio $2$.

## W6: exact coefficientwise remainder identity

The entropy $h$ contains an infinite Perron tail even at fixed $N$, so it is
incorrect to reduce the full numerical remainder to a finite formal-log
basis. The exact evaluator instead checks the coefficient identity before
substitution.

Let

$$
p_j=\frac{q-1}{q^{j+1}},
\qquad
A_j(N)=\left\lfloor\frac N{q^j}\right\rfloor
-\left\lfloor\frac N{q^{j+1}}\right\rfloor.
$$

In the formal sequence $d_0,d_1,\ldots$, the coefficient on the left is

$$
A_j(N)-Np_j.
$$

After expanding

$$
-\sum_{v\ge1}(d_v-d_{v-1})\frac{r_v(N)}{q^v},
$$

the right coefficient is

$$
\begin{cases}
r_1(N)/q,&j=0,\\
-r_j(N)/q^j+r_{j+1}(N)/q^{j+1},&j\ge1.
\end{cases}
$$

Lemma 4 makes these expressions exactly equal for every $j\ge0$. A checker
may verify any finite initial segment using integer/rational arithmetic, but
the all-$j$ algebraic rule is the proof. Numerical comparison of the full
remainder must additionally enclose the common infinite Perron tail; it may
not silently truncate it.

## W7: two exact formulas for the golden coefficients

The canonical coefficient is simultaneously

$$
\gamma_k=-\sum_{v\ge k+1}(d_v-d_{v-1})2^{k-v}
$$

and

$$
\gamma_k=\sum_{m\ge1}
\frac{(1-r^m)^2}{m(2-r^m)}r^{m(k+2)},
\qquad r=-\varphi^{-2}.
$$

Certified interval implementations should contain, rather than fit, the
orientation values

```text
gamma_0  approximately  +0.12179039180736
gamma_1  approximately  -0.04410128883705
gamma_2  approximately  +0.01715793798372
```

The signs and the theorem are certified by the exact tail inequality below,
not by these decimals.

## W8: exact strong-separation certificate

With $t=(3-\sqrt5)/2$ and

$$
K=\frac{(1+t^2)^2}{2-t^2}=-6+3\sqrt5,
$$

the proof uses

$$
S\le\frac{Kt^4}{2(1-t^2)^2}
=\frac{-87+39\sqrt5}{20}
<a_1t^3=\frac{280-125\sqrt5}{11}.
$$

The difference is

$$
\frac{6557-2929\sqrt5}{220}>0,
$$

certified without decimals by

$$
6557^2-5\cdot2929^2=99044>0.
$$

Any algebra system used as a checker must reproduce all four displayed
equalities/inequalities in $\mathbb Q(\sqrt5)$.

## W9: geometric scale certificate

The contraction is

$$
t=\varphi^{-2},
$$

so a depth-$n$ cylinder has diameter $O(t^n)$, separation $\Omega(t^n)$,
and multiplicity $2^n$. The canonical dimension identity is

$$
\frac{\log2}{-\log t}=\frac{\log2}{2\log\varphi}.
$$

This is the dimension of the real boundary image, not of the original shift.

## W10: radial-tail certificate

If $\xi$ is primitive of order $2^v$, then

$$
\lim_{r_0\uparrow1}(1-r_0)G(r_0\xi)
=-\frac{\gamma_{v-1}}{2^{v-1}(1-\xi)}.
$$

At the first level, $v=1$ and $\xi=-1$, this becomes

$$
\lim_{r_0\uparrow1}(1-r_0)G(-r_0)=-\frac{\gamma_0}{2}.
$$

The evaluator must sum all residue levels $w\ge v$. Retaining only $w=v$
is the literal `MUT-POLELEVEL` error.

The normalization mutation needs a nonreal root. For $Q=4$ and $\xi=i$,

$$
P_4(i)=-2-2i=-\frac4{1-i},
$$

so

$$
\lim_{r_0\uparrow1}(1-r_0)R_4(r_0i)
=-\frac1{1-i}=\frac{-1-i}{2}.
$$

This differs from the superseded expression
$i/(1-i)=(-1+i)/2$ and is the canonical `MUT-RADIALXI` witness.

## Cross-evaluator canonical records

For finite counts, the only shared output schema is

```text
(q, row-major integer A, N, exact integer Z_N,
 exact numerator of Z_N/Z_(N-1), exact denominator)
```

For infinite series, each evaluator emits

```text
(formula_id, index, rational/algebraic center or interval,
 outward-rounded radius, truncation index, analytic tail certificate_id)
```

Implementations must be developed without sharing fixtures or expected
tables. This ledger is revealed for comparison only after both outputs have
been independently frozen.
