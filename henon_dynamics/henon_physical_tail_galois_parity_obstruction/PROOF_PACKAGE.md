# Proof package

## 1. Frozen recurrence and derivative

For

\[
H_6(q,p)=(1-6q^2-p,q),
\]

a periodic coordinate chain obeys

\[
q_{j+1}=1-6q_j^2-q_{j-1},\qquad
D(q)=\begin{pmatrix}-12q&-1\\1&0\end{pmatrix}.
\]

## 2. Three reflection closures

The vertex chain starts at

\[
q_0=a,\qquad q_1=(1-6a^2)/2,
\]

and the edge chain starts at

\[
q_0=a,\qquad q_1=1-6a^2-a.
\]

Iterating the recurrence gives:

```text
A8 (vertex--vertex): (a,b,c,d,e,d,c,b), 1-6e^2-2d=0;
B8 (edge--edge):     (a,a,b,c,d,d,c,b), 1-6d^2-c-d=0;
A9/B9 (vertex--edge):(a,b,c,d,e,e,d,c,b), 1-6e^2-d-e=0.
```

The selected primitive coordinate factors have degrees 24, 12, and 28.

## 3. Trace fields

Chronological multiplication of `D(q_j)` followed by elimination of `a`
produces trace factors of degrees 12, 6, and 28.  Their coefficient-list
SHA256 values are

```text
A8 c10a3536d0781bdbbfbb320d48441a97583af9cd18517991c76e71813936c8ab
B8 49e0a21377ff47f504fa00d85f8ed3cee17d70d0677085bdc52e4203f4ac77fd
P9 f52d222e2934061dc367950e3e98e56d4fb9e0e6bd95c7b383fec9061bd7ac3b
```

They are irreducible modulo 7, 53, and 71, respectively.  The locked Sturm
intervals contain exactly one root each and exhaust the degree, so all three
trace fields are totally real.  The period-eight resultants have
multiplicity two because reflection has two axis choices; the period-nine
resultant has multiplicity one.

Rational boxes identify

```text
A8: a in (551939742238,551939742239)/10^12, T in (-2793061,-2793060);
B8: a in (-603835740359,-603835740358)/10^12, T in (1652592,1652593);
A9: a in (551940301478,551940301479)/10^12, T in (-19975348,-19975347);
B9: a in (-606695536138,-606695536137)/10^12, T in (11819577,11819578).
```

## 4. Exact signs

For every `u>2`,

\[
\log(u-1)<\operatorname{arcosh}(u/2)<\log u.
\]

Applying the lower bound to the terms on the negative side and the upper
bound to the positive side gives two integer comparisons.  The certificate
records the complete products and positive integer margins.  Therefore

\[
\Delta_6=E(A_6)+E(B_8)-E(A_7)-E(B_7)<0
\]

and

\[
\Delta_7=E(A_7)+E(B_9)-E(A_8)-E(B_8)>0.
\]

The decimal values are diagnostics, not proof inputs.

## 5. Physical tail versus Galois scale

The negative fixed point is

\[
q_-=-(1+\sqrt7)/6.
\]

Its derivative trace is `2+2sqrt(7)`.  The stable eigenvalue is positive and
smaller than the common signed inverse-branch contraction `2/sqrt(17)`.
Thus the selected physical reflection tail is exponentially localized.

Galois excess, however, sums the instability lengths of every nonphysical
trace embedding.  The physical contraction theorem controls one summand's
local coordinate selection; it contains no estimate for the number or size
of all conjugates.  The exact degree split at period eight and the shared
degree-28 field at period nine make this data-type mismatch explicit.

## 6. Boundary

The four observed signs from widths four through seven alternate, but a
finite sign sequence proves no eventual law.  The next theorem must count or
control the complete primitive reflection ensemble uniformly in the period.
