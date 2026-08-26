# C179 theorem package

Fix coprime integers \(a>b\geq1\).  Whenever \(N\geq2\) and
\((N,ab)=1\), put

\[
U_N=(\mathbb Z/N\mathbb Z)^\times,
\qquad q_N=ab^{-1}\pmod N,
\qquad R_N(x)=q_Nx,
\]

and mark \(1\in U_N\).  One application of \(R_N\) is one source-time step.

## Theorem 1: primitive divisors are primitive returns

For a prime \(p\) and \(n\geq2\), the following are equivalent:

1. \(p\mid a^n-b^n\) and \(p\nmid a^m-b^m\) for \(1\leq m<n\);
2. \(p\nmid ab\) and \(\operatorname{ord}_p(ab^{-1})=n\);
3. the marked point \(1\) has least positive return \(n\) under \(R_p\).

Moreover, a primitive return prime exists for every \(n\geq2\), except
when \((a,b,n)=(2,1,6)\), or when \(n=2\) and \(a+b\) is a power of two.
The existence and exception sentence is exactly the classical Zsigmondy
theorem and is not claimed new here.

### Proof

A prime dividing \(a^n-b^n\) cannot divide \(ab\).  Hence
\(a^m\equiv b^m\pmod p\) is equivalent to
\((ab^{-1})^m\equiv1\pmod p\).  Absence at all earlier times is precisely
minimality of the multiplicative order, and the orbit of \(1\) is
\(1,q_p,q_p^2,\ldots\).  This proves the three-way equivalence.  The final
existence statement, including both exception forms, is Zsigmondy's
attributed theorem. \(\square\)

Every primitive return prime at \(n\geq2\) is odd: if \(a,b\) are both odd,
then 2 already divides \(a-b\); otherwise \(a^n-b^n\) is odd.

## Theorem 2: exact prime-power return tower

Let \(p\) be a primitive return prime at time \(n\), and write

\[
e=v_p(a^n-b^n).
\]

Then for every \(k\geq1\),

\[
\operatorname{ord}_{p^k}(ab^{-1})
=n p^{\max(0,k-e)}.
\]

Consequently every orbit of \(R_{p^k}\) has this length, and the number of
cycles is

\[
\frac{\varphi(p^k)}{n p^{\max(0,k-e)}}.
\]

### Proof

Theorem 1 gives \(n=\operatorname{ord}_p(ab^{-1})\), so \(n\mid p-1\) and
\(p\nmid n\).  If \(q=ab^{-1}\) is read modulo powers of \(p\), then
\(v_p(q^n-1)=e\), because \(b\) is a \(p\)-adic unit.  An exponent returning
modulo \(p^k\) must be \(nr\).  The odd-prime lifting-the-exponent identity
gives

\[
v_p(q^{nr}-1)=v_p(q^n-1)+v_p(r)=e+v_p(r).
\]

The least positive \(r\) making this valuation at least \(k\) is
\(p^{\max(0,k-e)}\).  Translation by a group element has all cycles equal to
the order of that element, proving the cycle count. \(\square\)

## Theorem 3: every finite fiber

For any admissible \(N\), let \(L_N=\operatorname{ord}_N(q_N)\).  Then:

\[
U_N\text{ is the disjoint union of }\frac{\varphi(N)}{L_N}
\text{ cycles, each of length }L_N,
\]

\[
\#\operatorname{Fix}(R_N^t)=
\begin{cases}
\varphi(N),&L_N\mid t,\\
0,&L_N\nmid t,
\end{cases}
\]

and therefore

\[
\zeta_N(z)=(1-z^{L_N})^{-\varphi(N)/L_N},\qquad
\det(I-z\mathcal U_N)=(1-z^{L_N})^{\varphi(N)/L_N},
\]

where \(\mathcal U_N\) is the permutation Koopman operator on functions on
\(U_N\).  Inversion \(J_N(x)=x^{-1}\) is a reversor:
\(J_NR_NJ_N=R_N^{-1}\).

### Proof

The orbit of \(x\) closes at time \(t\) exactly when \(q_N^t=1\), independent
of \(x\), so every orbit has least length \(L_N\).  This gives the cycle and
fixed-point formulas.  Each length-\(L_N\) permutation block has
characteristic factor \(1-z^{L_N}\), and the fixed-count exponential gives
its reciprocal.  Finally,
\((q_Nx^{-1})^{-1}=xq_N^{-1}=R_N^{-1}(x)\). \(\square\)

## Theorem 4: two globalizations and the single-owner no-go

Adjoin the singleton \(U_1\).  On the disjoint union
\(\mathcal D_{a,b}=\bigsqcup_{(N,ab)=1}U_N\), let \(R\) act fiberwise.  Then
for every \(n\geq1\),

\[
\#\operatorname{Fix}(R^n)
=\sum_{N\mid a^n-b^n}\varphi(N)=a^n-b^n.
\]

Thus

\[
\zeta_{\mathcal D}(z)
=\exp\!\left(\sum_{n\geq1}\frac{a^n-b^n}{n}z^n\right)
=\frac{1-bz}{1-az},
\]

and the number of primitive cycles of length \(n\) is

\[
C_n=\frac1n\sum_{d\mid n}\mu(n/d)(a^d-b^d).
\]

In contrast, let \(\widehat U^{(ab)}=\varprojlim_{(N,ab)=1}U_N\) and translate
it by the compatible element \(q=a/b\).  This profinite map has no fixed
point at any positive time, hence its fixed-count source zeta is \(1\).

Therefore the same finite congruence system supports two source-natural
globalizations with incompatible fixed ledgers.  The collection of finite
fibers alone cannot select a unique global periodic-orbit determinant owner.
This is a no-go for uniqueness without extra structure, not a theorem that
all conceivable enlarged owners are impossible.

### Proof

The \(N\)-fiber is fixed at time \(n\) exactly when
\(N\mid a^n-b^n\).  Every such divisor is automatically coprime to \(ab\),
and the classical identity \(\sum_{N\mid m}\varphi(N)=m\) proves the first
formula.  The Taylor identity
\(\sum_{n\geq1}c^nz^n/n=-\log(1-cz)\) gives the rational zeta; Möbius
inversion gives \(C_n\).

A translation of a group has a fixed point at time \(n\) only if its
translator satisfies \(q^n=1\).  In the inverse limit this would require
\(N\mid a^n-b^n\) for every admissible \(N\), which is impossible: choose a
prime not dividing \(ab(a^n-b^n)\).  Hence the profinite fixed set is empty.
The incompatible ledgers prove nonselection. \(\square\)

## Route boundary

The strict tuple is

`(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL,
A4_NATURAL_QUANTIZATION)`; overall `ROUTE_A_EXPLORATORY`.

A0 is weak because primitive rational primes emerge intrinsically as return
moduli, but there is no selected single global prime-orbit owner and no
logarithmic prime clock.  A1 is weak because all finite primitive dynamics
are exact while the global primitive ledger depends on globalization.  A2
and A3 fail: there is no target divisor, frozen target validation protocol,
functional equation comparison, continuation comparison, counting-law
comparison, or Weil compression.  A4 records the canonical finite
permutation unitaries and the profinite Haar Koopman unitary on the same
source clock; it repairs none of A0--A3.  Route B remains unauthorized.
