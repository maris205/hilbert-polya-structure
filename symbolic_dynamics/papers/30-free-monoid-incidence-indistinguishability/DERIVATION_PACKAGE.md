# Derivation package — Paper 30 / SD-C32

## 1. From distinct atoms to a Boolean certificate

For a distinct atom tuple \(A=(a_1,\ldots,a_r)\), form all subset joins in the fixed ambient source:

\[
j_S(A)=\bigvee_{i\in S}a_i,
\qquad j_\varnothing(A)=\bot.
\]

The map \(\beta_A:S\mapsto j_S(A)\) is a pointed order map from \(2^{[r]}\) into \([\bot,j_{[r]}(A)]\).  It is a pointed order isomorphism exactly when:

1. every subset join exists;
2. distinct subsets have distinct joins;
3. every element below the full join is one of those subset joins; and
4. inclusion of subsets agrees with the source order.

On that event, the interval is the Boolean lattice \(B_r\).  Its top Möbius value is

\[
\mu_{B_r}(\hat0,\hat1)=(-1)^r.
\]

Therefore

\[
K_r^{\mathrm B}(A)
=\mathbf 1_{\beta_A\cong B_r}(-1)^r\mu(\bot,j(A))
=1
\]

on every accepted tuple and is zero otherwise.  The Möbius factor supplies the unit normalization; it does not create an additional signed statistic.

For positive-integer divisibility, distinct prime covers \(p_1,\ldots,p_r\) have full join \(\prod_i p_i\), and the elements below this squarefree product are precisely the subset products.  Hence every distinct prime tuple is accepted.  In a formal free commutative monoid, the same statement holds with squarefree formal monomials.  This is the first exact collision.

## 2. Canonicity boundary

Let \(\mathfrak I_r\) denote pointed isomorphism classes of tuple-join intervals.  Naturality permits

\[
K_f(A)=f([\bot,j(A)]_{\mathrm{pt}})
\]

for every \(f:\mathfrak I_r\to\mathbb C\).  In particular, the zero function, a signed Möbius function, an indicator of a different interval class, and arbitrary normalized combinations are all natural.  Full-source invariants add functions of the complete filtered isomorphism class.  Thus the phrase “canonical Boolean weight” is valid only after the support, range, and normalization axioms are written.

## 3. Connected cumulant at ranks two and three

The partition-lattice definition gives

\[
\kappa_2(a,b)=m(ab)-m(a)m(b),
\]

and

\[
\begin{split}
\kappa_3(a,b,c)={}&m(abc)-m(ab)m(c)-m(ac)m(b)-m(bc)m(a)\\
&+2m(a)m(b)m(c).
\end{split}
\]

For the Boolean moment on a free source, every nonempty subset moment is one.  Therefore

\[
\kappa_2=1-1=0,
\qquad
\kappa_3=1-1-1-1+2=0.
\]

More generally, if \(m(A_S)=\prod_{i\in S}u_i\), every partition product is \(\prod_i u_i\).  The partition coefficient is the higher cumulant of a constant and vanishes for all \(r\ge2\).  The connected transform therefore detects departure from factorization; it cannot supply a nonzero signal on a perfectly free multiplicative baseline with the frozen factorizing moment.

## 4. Valuation isomorphism

Write the free commutative monoid additively as

\[
F(P)=\{\alpha:P\to\mathbb N:\operatorname{supp}\alpha\text{ finite}\}.
\]

The valuation map is

\[
\Phi:\mathbb N_{>0}\to F(P),
\qquad \Phi(n)(p)=v_p(n).
\]

Unique factorization gives the inverse

\[
\alpha\longmapsto\prod_{p\in P}p^{\alpha(p)}.
\]

For all \(m,n\),

\[
m\mid n
\iff
\Phi(m)(p)\le\Phi(n)(p)\quad(\forall p),
\]

and

\[
\Phi(\operatorname{lcm}(m,n))(p)
=\max\{\Phi(m)(p),\Phi(n)(p)\}.
\]

The bottom \(1\) maps to zero, prime covers map to coordinate unit vectors, and finite joins map to coordinatewise maxima.  A divisor interval \([m,n]\) maps to the coordinate box \([\Phi(m),\Phi(n)]\); hence its incidence recurrence and Möbius values are identical.

If \(F_N\) is an active cutoff, define \(F_N'=\Phi(F_N)\).  If \(w\) is a roof mark, define \(w'=w\circ\Phi^{-1}\).  If \(G\) is a two-index Gram kernel, define

\[
G'_{\Phi(m),\Phi(n)}=G_{m,n}.
\]

Every compiled tensor or operator coefficient is transported by applying the corresponding index map.  The resulting clone is not merely an abstract monoid isomorphism: it is an isomorphism of the entire admissible decorated object.

## 5. Universal-control contradiction

Suppose an isomorphism-natural invariant \(I\) obeyed

\[
I(M_{\mathbb Z})\ne0,
\qquad I(U)=0\text{ for every UFD control }U.
\]

The transported \(F(P)\) is a free-commutative/UFD control, so the second condition gives \(I(F(P))=0\).  Naturality gives

\[
I(M_{\mathbb Z})=\Phi^*I(F(P))=0,
\]

a contradiction.  This argument does not inspect the formula for \(I\).  Consequently, adding more atoms, using all intervals, taking connected or Hopf logarithms, or using the complete filtered tower cannot evade it.

## 6. Mixed Gram embedding

For the inherited normalization, distinct active atoms have

\[
G_{pq}=\frac{1}{(p^{2\eta}+1)(q^{2\eta}+1)}.
\]

The symmetric pair contribution weighted by \(K_2\) is

\[
\mathcal M_K(s)
=2\sum_{p<q}K_2(p,q)G_{pq}
\left(p^{-s}q^{s-1}+q^{-s}p^{s-1}\right). \tag{6.1}
\]

At \(s=\tfrac12+it\),

\[
p^{-s}q^{s-1}
=\frac{e^{it\log(q/p)}}{\sqrt{pq}},
\qquad
q^{-s}p^{s-1}
=\frac{e^{-it\log(q/p)}}{\sqrt{pq}}.
\]

Thus

\[
\mathcal M_K\!\left(\tfrac12+it\right)
=4\sum_{p<q}\frac{K_2(p,q)G_{pq}}{\sqrt{pq}}
\cos\!\left(t\log\frac qp\right). \tag{6.2}
\]

The amplitude of the cosine is \(4K_2G_{pq}/\sqrt{pq}\), so its exact squared amplitude is

\[
16K_2(p,q)^2G_{pq}^2/(pq).
\]

No numerical cosine need be sampled.  The rational ratio \(q/p\), its formal logarithm, and the exact coefficient form the marker ledger.  Under \(\Phi\), these roof marks and Gram entries are transported, so the clone ledger is identical.

## 7. Summability and holomorphy

Let \(\sigma=\operatorname{Re}s\) and \(|K_2|\le1\).  Since

\[
G_{pq}\le p^{-2\eta}q^{-2\eta},
\]

the two terms of (6.1) satisfy

\[
|G_{pq}p^{-s}q^{s-1}|
\le p^{-(2\eta+\sigma)}q^{-(2\eta+1-\sigma)},
\]

\[
|G_{pq}q^{-s}p^{s-1}|
\le q^{-(2\eta+\sigma)}p^{-(2\eta+1-\sigma)}.
\]

Both exponents exceed one if and only if

\[
1-2\eta<\sigma<2\eta.
\]

The double prime sum is bounded by the corresponding product of all-integer zeta tails.  Compact subsets of the strip have a uniform exponent margin, proving normal convergence and holomorphy by the Weierstrass \(M\)-test.  At the inherited executable value \(\eta=2\), the strip is \(-3<\operatorname{Re}s<4\).

## 8. Functional type and rank-three boundary

The derivation of (6.1) constructs a convergent scalar series.  It does not construct a trace-class operator whose ordinary trace equals that series.  The series is therefore a new mixed functional.

The inherited third-regularized determinant satisfies a logarithmic expansion beginning at powers \(m\ge3\); in the chiral setting its quadratic term is removed.  It cannot own a retained quadratic mixed series.  Relative determinants additionally require a declared reference and trace-class relative hypotheses not supplied here.

The rank-three weight has no canonical slot in the inherited two-point Gram contraction.  The final executable suite declares the separate triangle contraction

\[
\Theta_3
=2\sum_{a<b<c}\chi_3(a,b,c)
\frac{G_{ab}G_{bc}G_{ca}}{w(a)w(b)w(c)}.
\]

Here \(\chi_3\) is the conjunction of unique join, Boolean interval,
Möbius sign, roof multiplicativity, and associative join ownership.  This is
additional but preregistered scheme data.  The result is not the
partition-lattice cumulant and not the full \(\operatorname{Tr}B^6\).
Naturality transports it to the formal clone, so no selectivity upgrade
follows.

## 9. Auxiliary determinant derivation

For the pair selector, define

\[
H_{pq}=\chi_2(p,q)\frac{G_{pq}}{\sqrt{pq}},\qquad H_{pp}=0.
\]

At \(\eta=2\),

\[
\sum_{p,q}|H_{pq}|
\le \left(\sum_{n\ge2}n^{-9/2}\right)^2<\infty.
\]

Writing \(H=\sum_{p,q}H_{pq}E_{pq}\), the matrix units have trace norm one,
so the absolute coefficient sum is a nuclear decomposition.  Thus \(H\) is
trace class and \(\det(I+zH)\) is an ordinary Fredholm determinant.  For a
zero-diagonal symmetric matrix,

\[
[z^2]\det(I+zH)=-\sum_{p<q}H_{pq}^2,
\]

\[
[z^3]\det(I+zH)=2\sum_{p<q<r}H_{pq}H_{qr}H_{pr}.
\]

This operator is auxiliary.  Its phase-decorated finite cutoffs are
diagonally conjugate, so the characteristic coefficients lose the
\(t\)-phase.  It neither owns the mixed series in Section 6 nor upgrades the
original chiral \(\det_3\).

## 10. Final exact census

The full selector yields pair/triple counts \(10/10\), \(21/35\), and
\(45/120\) at integer cutoffs 12, 18, and 30.  The mutated-cover control has
three pairs and zero triples; composite-only, seeded generic-DAG, and seeded
random inventories have zero pairs and triples.  The transported clone at
cutoff 30 has \(45/120\), exactly matching the baseline.  The canonical
package passes 28/28 tests and 1616/1616 independent checks; two 17-artifact
fresh runs are byte-identical.

## 11. Branch endpoint

The obstruction is categorical rather than numerical.  Another coefficient family, higher cumulant, cutoff convention, or finite-part constant remains a natural function of the same decorated free monoid and is therefore clone-invariant.  Only a new source-derived nonmultiplicative operation can pose a genuinely different question.
