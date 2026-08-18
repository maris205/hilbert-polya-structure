# Proof Package — Harmonic/Egyptian Adjacency

## Claim

For

$$
E_s(m,n)=\mathbf 1_{\{m+n\mid mn\}}(mn)^{-s/2},
\qquad \sigma=\Re s,
$$

on \(\ell^2(\mathbb N)\):

1. \(E_s\) is bounded and compact iff \(\sigma>0\);
2. \(E_s\in S_2\) iff \(\sigma>1/2\);
3. \(E_s\in S_1\) iff \(\sigma>1\);
4. ordered edges have the unique coprime-scale parameterization;
5. the stated first and second trace formulas hold in their legal domains.

## Status

PROVABLE AS STATED

## Step 1: remove complex phases

For \(s=\sigma+i\tau\), let \(U_\tau e_n=n^{-i\tau/2}e_n\). Then

$$
E_s=U_\tau E_\sigma U_\tau.
$$

Two-sided unitary multiplication preserves singular values. Ideal membership
and boundedness depend only on \(\sigma\).

## Step 2: unique edge parameterization

Let \(g=(m,n)\), \(m=ga\), \(n=gb\), and \((a,b)=1\). The edge condition is

$$
g(a+b)\mid g^2ab,
$$

or \(a+b\mid gab\). Since \((a+b,ab)=1\), this is equivalent to
\(a+b\mid g\). Write \(g=t(a+b)\). Then

$$
m=t a(a+b),\qquad n=t b(a+b),
$$

and the harmonic quotient is \(k=tab\). The gcd reconstruction makes
\(t,a,b\) unique. Conversely, every such ordered triple gives a legal edge.

## Step 3: row parameterization by divisors

Fix \(m\) and put \(k=mn/(m+n)\) and \(d=m-k\). Solving for \(n\) gives

$$
n=\frac{m^2}{d}-m.
$$

Thus neighbors of \(m\) are in bijection with divisors \(d\mid m^2\) with
\(d<m\). The absolute row sum is

$$
R_m=m^{-\sigma}
\sum_{\substack{d\mid m^2\\d<m}}
\left(\frac d{m-d}\right)^{\sigma/2}.
$$

## Step 4: boundedness and compactness for \(\sigma>0\)

Split the divisors at \(m/2\). If \(d\le m/2\), then
\(d/(m-d)\le1\), so this part is at most

$$
m^{-\sigma}\tau(m^2).
$$

If \(d>m/2\), put \(e=m-d\). Since \(d\mid m^2\) and \(m=d+e\), one has
\(d\mid e^2\). Hence \(e\ge\sqrt{m/2}\), and every corresponding summand is
at most a constant times \(m^{-3\sigma/4}\). Therefore

$$
R_m\ll_\sigma
\tau(m^2)\bigl(m^{-\sigma}+m^{-3\sigma/4}\bigr)\longrightarrow0
$$

by the standard bound \(\tau(n)=n^{o(1)}\). The symmetric Schur test gives
boundedness. Vanishing row sums and finite tail control give norm
approximation by finite compressions, hence compactness.

## Step 5: unboundedness for \(\sigma\le0\)

For \(\sigma<0\), every even \(m\) has a loop of modulus \(m^{-\sigma}\),
which is unbounded.

At \(\sigma=0\), the squared \(\ell^2\) norm of row \(m\) is its degree. The
divisors of \(m^2\) pair around \(m\), so

$$
\deg(m)=\frac{\tau(m^2)-1}{2}.
$$

For squarefree \(m\) with arbitrarily many prime factors,
\(\tau(m^2)=3^{\omega(m)}\) is unbounded. Hence the operator is unbounded.

## Step 6: Hilbert–Schmidt threshold

The ordered edge parameterization gives, with absolute convergence
understood,

$$
\|E_s\|_2^2
=\zeta(2\sigma)
\cdot\sum_{\substack{a,b\ge1\\(a,b)=1}}
[ab(a+b)^2]^{-\sigma}.
$$

Necessity of \(\sigma>1/2\) already follows from the scale sum along the
loops \(m=n=2t\). For sufficiency, \((a+b)^2\ge4ab\), so

$$
[ab(a+b)^2]^{-\sigma}
\le4^{-\sigma}a^{-2\sigma}b^{-2\sigma}.
$$

The double sum converges when \(\sigma>1/2\). Thus the Hilbert–Schmidt
threshold is exact.

## Step 7: trace-class threshold

For \(\sigma>1\), the absolute entry sum is

$$
\zeta(\sigma)
\cdot\sum_{\substack{a,b\ge1\\(a,b)=1}}
[ab(a+b)^2]^{-\sigma/2},
$$

which is at most \(2^{-\sigma}\zeta(\sigma)^3\). Hence \(E_s\) is trace
class.

Conversely, if \(E_s\) is trace class, the absolute diagonal sum in the
standard basis is bounded by its trace norm. Since the loops are exactly the
even integers,

$$
\sum_m|\langle E_se_m,e_m\rangle|
=\sum_{2\mid m}m^{-\sigma}.
$$

This diverges for \(\sigma\le1\). Therefore \(E_s\in S_1\) exactly when
\(\sigma>1\).

## Step 8: first trace

In the trace-class domain,

$$
\operatorname{Tr}(E_s)
=\sum_{2\mid m}m^{-s}
=2^{-s}\zeta(s).
$$

## Step 9: the \((s,s;2s)\) primitive Mordell–Tornheim second trace

In the Hilbert–Schmidt domain \(E_s^2\) is trace class and

$$
\operatorname{Tr}(E_s^2)
=\sum_{m\sim n}(mn)^{-s}.
$$

The edge parameterization yields

$$
\operatorname{Tr}(E_s^2)
=\zeta(2s)
\cdot\sum_{\substack{a,b\ge1\\(a,b)=1}}
a^{-s}b^{-s}(a+b)^{-2s}.
$$

Decomposing arbitrary \(a,b\) by their gcd shows

$$
\zeta_{\rm MT}(s,s;2s)
=\zeta(4s)
\cdot\sum_{\substack{a,b\ge1\\(a,b)=1}}
a^{-s}b^{-s}(a+b)^{-2s}.
$$

Thus

$$
\operatorname{Tr}(E_s^2)
=\frac{\zeta(2s)}{\zeta(4s)}
\cdot\zeta_{\rm MT}(s,s;2s).
$$

Absolute convergence holds for \(\sigma>1/2\), exactly the
Hilbert–Schmidt domain.

## Step 10: mixed-cycle and sign controls

The vertices \(15,30,60\) form a triangle because their harmonic quotients
are respectively \(10,20,12\). Thus the graph does not collapse to disjoint
rank-one scale blocks.

For real \(s>1\), the principal block on vertices \(3,6\) has zero
\((3,3)\) entry, a positive off-diagonal entry, and a positive \((6,6)\)
entry. Its determinant is negative. Hence the symmetric operator is not
positive semidefinite, even in its trace-class domain.

## Corrections and risks

- The formulas use ordered edges; no extra factor of two is inserted.
- Loops are indispensable.
- The word “primitive” in the second trace refers only to coprime
  \((a,b)\), not to primitive temporal cycles.
- External novelty remains search-bounded.
