# Proof package — Paper 30 / SD-C32

## 1. Admissible decorated sources

An object of the category \(\mathcal C\) is

\[
X=(|X|,\le,\bot,\operatorname{At},\vee,\mu,(F_N)_N,w,G,\mathfrak A),
\]

where \(|X|\) is a locally finite pointed order, \(\operatorname{At}(X)\) is the cover set of \(\bot\), \(\vee\) records every defined finite join, \(\mu\) is the interval Möbius function, \((F_N)_N\) is a compatible ambient active-atom filtration, and \(w,G,\mathfrak A\) denote the admitted roof, Gram, and compiled analytic decorations.  A morphism used in the theorem is an isomorphism preserving and reflecting all displayed data.  Möbius preservation is redundant once interval isomorphism is known, but making it explicit fixes the information boundary.

An invariant \(I\) may take values in scalars, tuple kernels, formal frequency ledgers, holomorphic functions, operator coefficients, or other objects with a specified pullback action.  Naturality at isomorphisms means

\[
I(X)=\phi^*I(Y)
\quad\text{whenever}\quad \phi:X\xrightarrow{\sim}Y.
\]

No locality, finite arity, linearity, additivity, or polynomiality is assumed.

## 2. Boolean tuple weight

Let \(A=(a_1,\ldots,a_r)\) be a tuple of distinct atoms, \(r\in\{2,3\}\), and suppose \(j(A)=\bigvee_i a_i\) exists.  Define

\[
\beta_A:2^{[r]}\longrightarrow[\bot,j(A)],\qquad
\beta_A(S)=\bigvee_{i\in S}a_i,
\]

with \(\beta_A(\varnothing)=\bot\), and set

\[
K_r^{\mathrm B}(A)=
\mathbf 1_{\beta_A\text{ is a pointed order isomorphism}}
(-1)^r\mu_X(\bot,j(A)). \tag{2.1}
\]

### Proposition 2.1 — naturality

If \(\phi:X\to Y\) is an admissible isomorphism, then

\[
K^{\mathrm B}_{r,Y}(\phi A)=K^{\mathrm B}_{r,X}(A).
\]

**Proof.**  The isomorphism sends atoms to atoms, preserves every subset join, and restricts to a pointed interval isomorphism

\[
[\bot,j_X(A)]\cong[\bot,j_Y(\phi A)].
\]

Thus \(\beta_A\) is an isomorphism exactly when \(\beta_{\phi A}\) is.  Incidence Möbius values are invariant under interval isomorphism, so both factors in (2.1) agree.  ∎

### Proposition 2.2 — conditional uniqueness

Among tuple weights that are (i) \(\{0,1\}\)-valued, (ii) supported exactly on tuples with pointed join interval \(B_r\), and (iii) normalized to one on that supported isomorphism class, (2.1) is unique.

**Proof.**  Conditions (ii) and (iii) fix the value on and off the support.  On \(B_r\),

\[
\mu_{B_r}(\hat0,\hat1)=(-1)^r,
\]

so (2.1) realizes the prescribed values.  ∎

### Proposition 2.3 — scheme freedom

Isomorphism naturality alone does not select (2.1).

**Proof.**  Let \(\mathfrak I_r\) be the set of pointed isomorphism classes of tuple-join intervals.  Every function \(f:\mathfrak I_r\to\mathbb C\) gives an interval-local natural weight

\[
K_f(A)=f([\bot,j(A)]_{\mathrm{pt}}).
\]

Distinct \(f\) give distinct natural schemes.  A construction allowed to inspect the full filtered source has at least as much freedom.  Therefore support and normalization are substantive axioms, not consequences of naturality.  ∎

## 3. Connected-cumulant cancellation

For a fixed moment system \(m(A_S)\), define

\[
\kappa_r(A)=
\sum_{\pi\in\Pi_r}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}m(A_B). \tag{3.1}
\]

### Lemma 3.1 — factorization cancellation

If \(m(A_S)=\prod_{i\in S}u_i\) for every nonempty \(S\subseteq[r]\), then \(\kappa_r(A)=0\) for every \(r\ge2\).

**Proof.**  For each partition \(\pi\),

\[
\prod_{B\in\pi}m(A_B)=\prod_{i=1}^r u_i.
\]

After factoring this common product from (3.1), the remaining coefficient is

\[
c_r=\sum_{\pi\in\Pi_r}(-1)^{|\pi|-1}(|\pi|-1)!.
\]

Its exponential generating function is

\[
\sum_{r\ge1}c_r\frac{z^r}{r!}
=\log\!\left(\sum_{r\ge0}\frac{z^r}{r!}\right)
=\log(e^z)=z.
\]

Hence \(c_1=1\) and \(c_r=0\) for \(r\ge2\).  ∎

### Corollary 3.2 — exact baseline failure

In a free commutative divisibility source, each distinct-atom subset spans its Boolean squarefree interval.  If the frozen moment is one on every such nonempty subset, then \(\kappa_r=0\) for all \(r\ge2\), both on the integer baseline and on the formal clone.

The transform (3.1) is canonical only relative to \(m\).  Replacing \(m\) by a nonfactorizing scheme may make \(\kappa_r\) nonzero, but the scheme is transported unchanged by the isomorphism in the next theorem.

### Executable five-predicate refinement

The final exact suite uses \(\chi_r(A)\), the conjunction of unique join,
Boolean interval, M{\"o}bius sign, roof multiplicativity, and associative
binary-join ownership.  Each predicate is preserved by an admissible
decorated-source isomorphism, so \(\chi_r\) is natural.  Its triangle
contraction

\[
\Theta_3=2\sum_{a<b<c}\chi_3(a,b,c)
\frac{G_{ab}G_{bc}G_{ca}}{w(a)w(b)w(c)}
\]

is a separate connected graph contraction, not the partition-lattice
cumulant and not the full \(\operatorname{Tr}B^6\).  It may be nonzero on a
factorizing baseline, but Theorem 4.1 below forces the same value on the
transported UFD clone.

## 4. Free-monoid indistinguishability

Let

\[
M_{\mathbb Z}=(\mathbb N_{>0},\mid,1,\operatorname{lcm})
\]

and let \(P=\operatorname{At}(M_{\mathbb Z})\).  Define the formal free commutative monoid

\[
F(P)=\bigoplus_{p\in P}\mathbb N e_p
\]

with zero vector as bottom, coordinatewise comparison, and coordinatewise maximum as join.  Define

\[
\Phi(n)=(v_p(n))_{p\in P}. \tag{4.1}
\]

For each admitted decoration, set

\[
F_N'=\Phi(F_N),\qquad
w'(\Phi(n))=w(n),\qquad
G'_{\Phi(m),\Phi(n)}=G_{m,n}, \tag{4.2}
\]

and transport every component of \(\mathfrak A\) in the same way.

### Theorem 4.1 — decorated free-monoid indistinguishability

The map \(\Phi\) is an isomorphism in \(\mathcal C\) from the decorated integer-divisibility source to the transported formal free-commutative/UFD source.  Consequently, every isomorphism-natural invariant \(I\) of the admitted data satisfies

\[
I(M_{\mathbb Z})=\Phi^*I(F(P)). \tag{4.3}
\]

This holds for local or nonlocal \(I\), at every arity, and for scalar-, kernel-, ledger-, operator-coefficient-, or function-valued output.

**Proof.**

1. Unique factorization gives a bijection between positive integers and finitely supported exponent vectors, so (4.1) is bijective.
2. For positive integers \(m,n\),
   \[
   m\mid n\quad\Longleftrightarrow\quad v_p(m)\le v_p(n)
   \text{ for every }p.
   \]
   Thus \(\Phi\) preserves and reflects the order and sends \(1\) to the zero vector.
3. Covers of \(1\) are sent exactly to unit vectors.  Hence atoms are preserved and reflected.
4. For every prime cover \(p\),
   \[
   v_p(\operatorname{lcm}(n_1,\ldots,n_k))
   =\max_i v_p(n_i).
   \]
   Thus every finite join is preserved.  Each pointed interval is carried isomorphically to its exponent-vector interval, so incidence Möbius functions agree.
5. Equation (4.2) makes every cutoff and analytic decoration commute with \(\Phi\) by transport.  This is the required comparison of an object with an isomorphic control, not coefficient fitting.
6. Naturality of \(I\) at this decorated-source isomorphism gives (4.3).  None of the preceding steps invokes locality, arity, or an algebraic form for \(I\).  ∎

### Corollary 4.2 — inconsistent universal selectivity gate

There is no admissible natural invariant \(I\) satisfying

\[
I(M_{\mathbb Z})\ne0
\quad\text{and}\quad
I(U)=0\quad\text{for every free-commutative/UFD control }U. \tag{4.4}
\]

**Proof.**  The universal quantifier in (4.4) includes the transported clone \(F(P)\).  Theorem 4.1 gives equality of the two values, contradicting (4.4).  ∎

### Corollary 4.3 — Boolean and cumulant dichotomy

The Boolean weight (2.1) equals one on every distinct-atom tuple in both free sources, so it fails the UFD-zero gate.  The connected cumulant of the factorizing Boolean moment equals zero in both, so it fails the baseline-nonzero gate.  A different natural moment or global contraction remains equal across the two sources by Theorem 4.1.

## 5. Exact theorem boundary

Theorem 4.1 covers:

- pair, triple, and arbitrary finite-arity join/lcm coherence;
- incidence Möbius transforms, incidence-Hopf primitives, and connected/logarithmic transforms;
- any source-natural moment followed by partition-lattice cumulants;
- invariants of the complete filtered tower rather than a single interval;
- transported roof, metric, Gram, and compiled-operator data;
- ordinary traces or determinant coefficients when honestly constructed from those data; and
- newly declared same-object functionals natural in those data.

It does not assert that adding any operation to the integers preserves the clone.  A source-derived operation relating addition to multiplication, a congruence correspondence, or a genuine transfer operator can define a new category.  The burden is then to prove that the enrichment is not transported by \(\Phi\).  Excluding the clone from the controls or adding nontransportable labels changes the advertised gate.

## 6. Analytic mixed functional

For distinct atoms with numerical roof marks \(p,q\), take

\[
G_{pq}=\frac{1}{(p^{2\eta}+1)(q^{2\eta}+1)},\qquad \eta>0,
\]

and let \(|K_2(p,q)|\le1\).  Define

\[
\mathcal M_K(s)=2\sum_{p<q}K_2(p,q)G_{pq}
\left(p^{-s}q^{s-1}+q^{-s}p^{s-1}\right). \tag{6.1}
\]

### Proposition 6.1 — normal convergence and holomorphy

The series (6.1) converges normally on compact subsets of

\[
1-2\eta<\operatorname{Re}s<2\eta
\]

and is holomorphic there.

**Proof.**  Write \(\sigma=\operatorname{Re}s\).  Since \(G_{pq}\le p^{-2\eta}q^{-2\eta}\), the two absolute summands are bounded by

\[
p^{-(2\eta+\sigma)}q^{-(2\eta+1-\sigma)},\qquad
q^{-(2\eta+\sigma)}p^{-(2\eta+1-\sigma)}.
\]

Both exponents exceed one precisely in the stated strip.  Replacing prime-cover sums by all-integer sums gives a convergent product majorant.  On a compact substrip both exponents stay uniformly above one, so the Weierstrass \(M\)-test gives normal convergence.  Termwise holomorphy proves the claim.  ∎

### Proposition 6.2 — critical-line marker ownership

For \(s=\tfrac12+it\),

\[
\mathcal M_K\!\left(\tfrac12+it\right)
=4\sum_{p<q}\frac{K_2(p,q)G_{pq}}{\sqrt{pq}}
\cos\!\left(t\log\frac qp\right). \tag{6.2}
\]

Thus the formal marker is \(q/p\leftrightarrow\log(q/p)\), with squared coefficient

\[
\frac{16K_2(p,q)^2G_{pq}^2}{pq}. \tag{6.3}
\]

For \(K_2=K_2^{\mathrm B}\), the clone has the identical marker ledger after transport.

### Ownership declaration

Equation (6.1) defines a new source-weighted mixed functional.  No trace-class operator with ordinary trace (6.1) is constructed.  It is not a relative determinant, \(\det_2\), \(\det_3\), or any other \(\det_m\).  The inherited honest \(\det_3\) removes the quadratic power in full and continues to own A2.  Exponentiating (6.1), a finite part of it, or a chosen cubic contraction would define further scheme-dependent functionals, not a determinant upgrade.

## 7. Auxiliary trace-class determinant

Define the zero-diagonal atom matrix

\[
H_{pq}=\chi_2(p,q)\frac{G_{pq}}{\sqrt{pq}},\qquad H_{pp}=0.
\]

At \(\eta=2\), \(|H_{pq}|\le p^{-9/2}q^{-9/2}\), whence
\(\sum_{p,q}|H_{pq}|<\infty\).  The matrix-unit decomposition is nuclear,
so \(H\) is trace class and \(\det(I+zH)\) is an honest ordinary Fredholm
determinant, entire in \(z\).  Its first coefficients are

\[
[z^2]\det(I+zH)=-\sum_{p<q}H_{pq}^2,
\qquad
[z^3]\det(I+zH)=2\sum_{p<q<r}H_{pq}H_{qr}H_{pr}.
\]

This does not change the ownership declaration for (6.1).  The auxiliary
operator is different from the original chiral transfer family; its
phase-decorated cutoffs are diagonally conjugate, so its characteristic
coefficients have no \(t\)-motion.  The transported clone has the same
matrix and determinant coefficients.

## 8. Exact authority certificate

The final package reports 28/28 regression tests and 1616/1616 independent
checks.  Two fresh builds produce 17 byte-identical artifacts, with aggregate
SHA-256
`b2ea8f6c6803ef5a0a01999452f7e68ed099ccb04f2e24c8592b97b5e1fef316`.
The 31-entry canonical authority-ledger SHA-256 is
`99be21c67f12234d5b5b6ae854bd2c6695aabebec953fa8fe217bce452045bd0`.
The finite suite establishes implementation facts, not the infinite theorem.

## 9. Closure theorem

### Theorem 9.1 — multiplicative incidence/counterterm branch closure

Under the frozen information boundary, changing a natural join/Möbius kernel, tuple arity, cumulant convention, cutoff prescription, finite part, or same-object contraction cannot satisfy exact integer-nonzero/every-UFD-zero selectivity.

**Proof.**  Each change still produces an invariant natural in the same transported decorated source.  Theorem 4.1 therefore forces equality on the integer source and its formal UFD clone.  ∎

The only permitted successor is a new problem with source-derived nonmultiplicative data and a proof that those data break the clone isomorphism.
