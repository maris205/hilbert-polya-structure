# Derivation and Proof Package: Final-Denominator-Only Scope

## Target

Derive and prove the exact theorem chain behind the modular open--closed clock obstruction:

1. classify oriented cusp double cosets and recover the totient Dirichlet factor;
2. prove that no nonzero function of a fixed scaled final denominator \(\alpha|c(g)|\) satisfies universal closed-orbit square repetition;
3. derive the Chebyshev power identity for \(c(g^n)\);
4. compute the exact power defect of the logarithmic denominator height and its stable homogenization;
5. deduce the scoped primitive-hyperbolic Euler-product no-go;
6. prove that affine reparametrization and entire zero-free normalization cannot turn the modular scattering quotient into one entire \(\xi\).

The immediate role is a compatibility theorem and Route-A termination certificate.  It is not a construction of a new transfer operator or self-adjoint spectral model.

## Status

**COHERENT AFTER REFRAMING / EXTRA ASSUMPTION.**

The original broad wording “the cusp denominator cannot be a roof” is not justified: a local roof need not itself be a class function, and an enlarged cocycle can use more than the final denominator.  The corrected theorem is **PROVABLE AS STATED** for the explicit class
\[
R_F(g)=F(\alpha|c(g)|),
\qquad
F:\alpha\mathbb N_{>0}\to\mathbb R,
\qquad \alpha>0\text{ fixed},
\]
when \(R_F\) is proposed as the total period of a closed hyperbolic orbit.

## Invariant Object

The organizing object is the **type of the clock and its indexing category**:

- the open arithmetic height \(\tau_P\) is a function on oriented double cosets \(P\backslash\Gamma/P\);
- a closed total period \(L\) is a function on hyperbolic conjugacy classes and must be homogeneous under powers.

The lower-left denominator is an invariant of the first object but not of the second.  The proof never silently replaces one indexing object by the other.

## Assumptions

- \(\Gamma=\operatorname{PSL}_2(\mathbb Z)\).
- \(P=\Gamma_\infty=\langle T\rangle\), where
  \[
  T=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
  \]
- Matrix calculations use lifts in \(\widetilde\Gamma=\operatorname{SL}_2(\mathbb Z)\).
- In the big Bruhat cell, the PSL sign is fixed by \(c(g)>0\).
- For a hyperbolic PSL element, the SL sign is fixed by \(t=\operatorname{tr}(g)>2\).
- The scale \(\alpha>0\) is fixed before \(F\) is chosen.  The domain of \(F\) is exactly \(\alpha\mathbb N_{>0}\).
- A proposed closed total-period clock is representative independent and satisfies exact power homogeneity.
- In the divisor theorem, the allowed scalar normalizer is entire and zero-free, and the affine coefficient \(a\) is nonzero.

No form of the Riemann hypothesis is assumed.

## Notation

- For
  \[
  g=\begin{pmatrix}a&b\\c&d\end{pmatrix},
  \]
  write \(c(g)=c\) and \(t(g)=\operatorname{tr}(g)\).
- \([g]\) denotes the hyperbolic conjugacy class of \(g\).
- \(U_n\) is the Chebyshev polynomial of the second kind, normalized by
  \[
  U_{-1}=0,\qquad U_0=1,\qquad
  U_{n+1}(x)=2xU_n(x)-U_{n-1}(x).
  \]
- For hyperbolic \(g\) with \(t>2\),
  \[
  \lambda(g)=\frac{t+\sqrt{t^2-4}}2,
  \qquad
  \ell(g)=2\log\lambda(g).
  \]
- The scaled literal denominator height is
  \[
  H_\alpha(g)=2\log(\alpha|c(g)|).
  \]
- Euler's totient is \(\varphi\), and the Möbius function is \(\mu\).
- The completed zeta and entire xi functions are
  \[
  \Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u),
  \qquad
  \xi(u)=\tfrac12u(u-1)\Lambda(u).
  \]

## Derivation Strategy

The derivation has two exact branches.

1. **Arithmetic/open branch:** quotient by the left and right cusp actions, identify the invariants \((c,d\bmod c)\), and sum the resulting channel weights.
2. **Hyperbolic/closed branch:** impose the exact repetition axiom on a final-denominator-only total period, use an explicit positive hyperbolic family to prove vanishing, then use Cayley--Hamilton to compute the asymptotic behavior of the literal logarithmic height.

The divisor theorem is logically supporting rather than needed for the clock theorem.  It uses the global divisor of the completed scattering coefficient and a precisely limited normalization class.

## Derivation Map

1. Proposition 1 classifies \(P\backslash\Gamma/P\) in the big cell.
2. Corollary 2 counts channels by \(\varphi(c)\) and derives the Dirichlet identity for \(\Re s>1\).
3. Proposition 3 shows that \(|c(g)|\) does not descend to hyperbolic conjugacy classes.
4. Theorem 4 uses only the square law on \(g_{m,n}\) to force arbitrary \(F\) to vanish on \(\alpha\mathbb N_{>0}\).
5. Proposition 5 derives the Chebyshev power identity from Cayley--Hamilton.
6. Theorem 6 substitutes the eigenvalue form of \(U_{n-1}\) and obtains the exact defect and stable limit.
7. Corollary 7 applies Theorem 4 to the repetition axiom of a primitive-hyperbolic Euler product.
8. Theorem 8 maps each nontrivial zeta zero into a pole and a shifted zero of \(\Phi\), then observes that an entire zero-free normalizer cannot cancel the poles.

No approximation enters Propositions 1, 3, and 5, Theorems 4, 6, and 8, or Corollaries 2 and 7.  Numerical work is a regression audit only.

## Main Derivation

### Proposition 1: classification of oriented cusp double cosets

Let \(P\) be the image in \(\Gamma\) of
\[
\widetilde P=\{\pm T^n:n\in\mathbb Z\}\subset\operatorname{SL}_2(\mathbb Z).
\]
The double coset with \(c=0\) is the identity double coset \(P\).  After choosing \(c>0\), the nonidentity double cosets are in bijection with
\[
\mathcal D
=\{(c,\bar d):c\ge1,\ \bar d\in(\mathbb Z/c\mathbb Z)^\times\}.
\]

#### Proof

Let
\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z).
\]
If \(c=0\), the equation \(ad-bc=1\) gives \(ad=1\), so \(a=d=1\) or \(a=d=-1\).  Modulo \(-I\), such a matrix lies in the image of \(\langle T\rangle\).  Hence all matrices with \(c=0\) represent \(P\).

Assume \(c\ne0\).  Replacing \(g\) by \(-g\) fixes the PSL class and lets us impose \(c>0\).  Direct multiplication gives
\[
T^m gT^n
=\begin{pmatrix}
a+mc & an+b+m(cn+d)\\
c & cn+d
\end{pmatrix}.
\]
Therefore \(c\) and \(d\bmod c\) are invariant under the left and right \(P\)-actions.  Since \(ad-bc=1\), one has \(\gcd(c,d)=1\), so \(\bar d\) is a unit modulo \(c\).

Conversely, fix \(c\ge1\) and a unit \(\bar d\bmod c\).  Choose an integer representative \(d\), choose \(a\) satisfying
\[
ad\equiv1\pmod c,
\]
and set
\[
b=\frac{ad-1}{c}.
\]
Then
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\in\operatorname{SL}_2(\mathbb Z),
\]
so every pair in \(\mathcal D\) occurs.

It remains to prove uniqueness.  Suppose \(g\) and \(g'\) have the same positive \(c\) and the same residue \(d\bmod c\).  Right multiplication of \(g\) by some \(T^n\) makes its bottom row equal to that of \(g'\).  If two determinant-one integer matrices have the same bottom row \((c,d')\), the difference \((x,y)\) of their top rows satisfies
\[
xd'-yc=0.
\]
Because \(\gcd(c,d')=1\), there is \(k\in\mathbb Z\) with
\[
(x,y)=k(c,d').
\]
Left multiplication by \(T^k\) makes the top rows equal.  Thus the two matrices lie in the same double coset.  This proves the bijection. \(\square\)

### Corollary 2: totient channel count and Dirichlet identity

At fixed \(c\ge1\), the number of oriented double cosets is \(\varphi(c)\).  With
\[
\tau_P(PgP)=2\log c(g),
\]
one has, for \(\Re s>1\),
\[
\sum_{PgP\ne P}e^{-s\tau_P(PgP)}
=\sum_{c\ge1}\frac{\varphi(c)}{c^{2s}}
=\frac{\zeta(2s-1)}{\zeta(2s)}.
\]

#### Proof

The first statement follows from Proposition 1 because the group of units modulo \(c\) has cardinality \(\varphi(c)\).  For \(w\) with \(\Re w>2\), use
\[
\varphi(n)=n\sum_{d\mid n}\frac{\mu(d)}d.
\]
Absolute convergence permits rearrangement:
\[
\begin{aligned}
\sum_{n\ge1}\frac{\varphi(n)}{n^w}
&=\sum_{n\ge1}n^{1-w}\sum_{d\mid n}\frac{\mu(d)}d\\
&=\sum_{d,m\ge1}(dm)^{1-w}\frac{\mu(d)}d\\
&=\left(\sum_{d\ge1}\frac{\mu(d)}{d^w}\right)
  \left(\sum_{m\ge1}\frac1{m^{w-1}}\right)\\
&=\frac{\zeta(w-1)}{\zeta(w)}.
\end{aligned}
\]
Set \(w=2s\).  The convergence condition becomes \(\Re s>1\). \(\square\)

#### Interpretation

This is an oriented open-channel coefficient ledger.  It is not a primitive closed-orbit Euler product.  The full modular scattering coefficient also contains the Archimedean factor:
\[
\Phi(s)
=\sqrt\pi\frac{\Gamma(s-\tfrac12)}{\Gamma(s)}
 \frac{\zeta(2s-1)}{\zeta(2s)}.
\]

### Proposition 3: the final denominator does not descend to closed conjugacy classes

The function \(g\mapsto|c(g)|\) is not invariant under conjugation in \(\operatorname{PSL}_2(\mathbb Z)\).

#### Proof

Let
\[
g=\begin{pmatrix}1&1\\2&3\end{pmatrix},
\qquad
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Both matrices lie in \(\operatorname{SL}_2(\mathbb Z)\), and direct multiplication gives
\[
S^{-1}gS
=\begin{pmatrix}3&-2\\-1&1\end{pmatrix}.
\]
The matrices \(g\) and \(S^{-1}gS\) are hyperbolic because their common trace is \(4\), but
\[
|c(g)|=2,
\qquad
|c(S^{-1}gS)|=1.
\]
Hence \(|c|\) does not descend to the conjugacy class. \(\square\)

#### PSL Gauss-word cyclic witness

For the standard inverse-branch matrices
\[
A_a=\begin{pmatrix}0&1\\1&a\end{pmatrix},
\]
set
\[
g=A_1A_1A_1A_2=\begin{pmatrix}2&5\\3&8\end{pmatrix},
\quad
g'=A_1A_2A_1A_1=\begin{pmatrix}3&5\\4&7\end{pmatrix},
\]
and
\[
Q=A_1A_1=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]
Then \(\det Q=1\), direct multiplication gives \(g'=Q^{-1}gQ\), and
\[
|c(g)|=3\ne4=|c(g')|.
\]
The two-digit shift is used so that the conjugacy is inside \(\operatorname{PSL}_2\), not merely \(\operatorname{PGL}_2\).

#### Boundary of the proposition

This proposition rules out the final entry itself as a representative-independent total period.  It does not require, or claim, that each local term of a roof function be conjugacy invariant.  Only the full periodic sum must descend to the closed orbit.

### Theorem 4: arbitrary scaled denominator-only square-law rigidity

Fix \(\alpha>0\).  Let
\[
F:\alpha\mathbb N_{>0}\to\mathbb R
\]
be any function.  Assume that
\[
F(\alpha|c(g^2)|)=2F(\alpha|c(g)|)
\tag{4.1}
\]
for every hyperbolic \(g\in\operatorname{SL}_2(\mathbb Z)\) whose four entries
are strictly positive. Then
\[
F(\alpha n)=0
\qquad\text{for every }n\in\mathbb N_{>0}.
\]

#### Proof

For integers \(m,n\ge1\), define
\[
g_{m,n}=\begin{pmatrix}1&m\\n&1+mn\end{pmatrix}.
\]
Its determinant and trace are
\[
\det g_{m,n}=1,
\qquad
\operatorname{tr}(g_{m,n})=2+mn>2.
\]
Thus every \(g_{m,n}\) is hyperbolic.  Its lower-left entry is \(n\).  Multiplication gives
\[
c(g_{m,n}^2)=n+n(1+mn)=n(2+mn).
\tag{4.2}
\]

First set \(n=1\).  Equations (4.1) and (4.2) give
\[
F(\alpha(m+2))=2F(\alpha)
\qquad(m\ge1).
\]
Equivalently,
\[
F(\alpha r)=2F(\alpha)
\qquad(r\ge3).
\tag{4.3}
\]

Next fix an integer \(r\ge3\) and take \((m,n)=(1,r)\).  Equation (4.1) gives
\[
F(\alpha r(r+2))=2F(\alpha r).
\tag{4.4}
\]
Since both \(r\) and \(r(r+2)\) are at least \(3\), equation (4.3) evaluates the two sides of (4.4) as
\[
2F(\alpha)=4F(\alpha).
\]
Therefore
\[
F(\alpha)=0.
\]
Equation (4.3) now yields
\[
F(\alpha r)=0
\qquad(r\ge3).
\]

It remains to handle \(r=2\).  Take \((m,n)=(1,2)\).  Equation (4.2) gives \(c(g_{1,2}^2)=8\), so
\[
F(8\alpha)=2F(2\alpha).
\]
The left side is zero because \(8\ge3\).  Hence \(F(2\alpha)=0\).  Together with \(F(\alpha)=0\), this proves the theorem on all of \(\alpha\mathbb N_{>0}\). \(\square\)

#### Consequences and exact scope

- All repetitions imply the square law, so the theorem rules out any nonzero denominator-only exact closed clock satisfying full power homogeneity.
- No regularity assumption on \(F\) was used.
- The theorem does not apply if the total period depends on trace, endpoints, word chronology, local increments, or additional state.

### Proposition 5: Chebyshev formula for powers

Let \(g\in\operatorname{SL}_2(\mathbb Z)\), let \(t=\operatorname{tr}(g)\), and let \(n\ge1\).  Then
\[
g^n=U_{n-1}(t/2)g-U_{n-2}(t/2)I,
\tag{5.1}
\]
and therefore
\[
c(g^n)=c(g)U_{n-1}(t/2).
\tag{5.2}
\]

#### Proof

The characteristic polynomial of \(g\) is
\[
x^2-tx+1
\]
because \(\det g=1\).  Cayley--Hamilton gives
\[
g^2=tg-I.
\tag{5.3}
\]

For \(n=1\), equation (5.1) reads
\[
g=U_0(t/2)g-U_{-1}(t/2)I=g.
\]
For \(n=2\), it reads \(g^2=tg-I\), which is (5.3).

Assume (5.1) holds at \(n\).  Multiplying by \(g\) and using (5.3),
\[
\begin{aligned}
g^{n+1}
&=U_{n-1}(t/2)g^2-U_{n-2}(t/2)g\\
&=\bigl(tU_{n-1}(t/2)-U_{n-2}(t/2)\bigr)g
  -U_{n-1}(t/2)I\\
&=U_n(t/2)g-U_{n-1}(t/2)I,
\end{aligned}
\]
where the last equality is the defining recurrence for \(U_n\).  Induction proves (5.1).  Taking lower-left entries gives (5.2), because the lower-left entry of \(I\) is zero. \(\square\)

### Theorem 6: exact power defect and stable homogenization

Let \(g\in\operatorname{SL}_2(\mathbb Z)\) be hyperbolic with lift chosen so that
\[
t=\operatorname{tr}(g)>2.
\]
Then \(c(g)\ne0\).  Define
\[
\lambda=\frac{t+\sqrt{t^2-4}}2>1,
\qquad
\ell(g)=2\log\lambda,
\qquad
H_\alpha(g)=2\log(\alpha|c(g)|).
\]
For every \(n\ge1\),
\[
H_\alpha(g^n)
=n\ell(g)
+2\log\frac{\alpha|c(g)|}{\sqrt{t^2-4}}
+2\log(1-\lambda^{-2n}).
\tag{6.1}
\]
Consequently,
\[
\lim_{n\to\infty}\frac{H_\alpha(g^n)}n=\ell(g).
\tag{6.2}
\]

#### Proof

If \(c(g)=0\), integrality and determinant one imply that both diagonal entries are \(1\) or both are \(-1\), so \(|\operatorname{tr}(g)|=2\).  This contradicts hyperbolicity; hence \(c(g)\ne0\).

The two eigenvalues of \(g\) are \(\lambda\) and \(\lambda^{-1}\), and
\[
\lambda-\lambda^{-1}=\sqrt{t^2-4}.
\tag{6.3}
\]
The standard closed form of the Chebyshev polynomial is
\[
U_{n-1}(t/2)
=\frac{\lambda^n-\lambda^{-n}}{\lambda-\lambda^{-1}}
=\frac{\lambda^n(1-\lambda^{-2n})}{\sqrt{t^2-4}}.
\tag{6.4}
\]
For \(t>2\), every factor on the right of (6.4) is positive.  Combining (5.2) and (6.4),
\[
|c(g^n)|
=\frac{|c(g)|\lambda^n(1-\lambda^{-2n})}{\sqrt{t^2-4}}.
\]
Multiply by \(\alpha\), take \(2\log\), and use \(2\log\lambda=\ell(g)\).  This proves (6.1).

Divide (6.1) by \(n\).  The middle term is constant in \(n\), so its quotient tends to zero.  Since \(\lambda>1\),
\[
\log(1-\lambda^{-2n})\longrightarrow0,
\]
and its quotient by \(n\) also tends to zero.  Equation (6.2) follows. \(\square\)

#### Conditional rigidity inside the asymptotic class

Let \(L\) be a closed clock on hyperbolic conjugacy classes satisfying
\[
L([g^n])=nL([g]).
\]
If, for a fixed hyperbolic \(g\),
\[
L([g^n])-H_\alpha(g^n)=o(n),
\tag{6.5}
\]
then division by \(n\) gives
\[
L([g])-\frac{H_\alpha(g^n)}n\longrightarrow0.
\]
By (6.2),
\[
L([g])=\ell(g).
\]

This is a rigidity statement only within the explicit asymptotic class (6.5).  It is not a theorem that every possible repair or every homogeneous class function equals \(\ell\).

### Corollary 7: primitive-hyperbolic Euler-product no-go

There is no nontrivial primitive-hyperbolic Euler product whose total period is
\[
R_F(g)=F(\alpha|c(g)|)
\]
for a fixed \(\alpha>0\) and which satisfies the standard repetition law on every hyperbolic class.

#### Proof

A representative-independent primitive closed-orbit construction assigns a period to every primitive class and extends it to repetitions by
\[
R_F(g^n)=nR_F(g).
\]
In particular, it satisfies the square law for every hyperbolic \(g\):
\[
F(\alpha|c(g^2)|)=2F(\alpha|c(g)|).
\]
Theorem 4 gives \(F\equiv0\) on \(\alpha\mathbb N_{>0}\).  Hence every proposed period is zero and every local norm
\[
N_F(g)=e^{R_F(g)}
\]
equals \(1\).  Such data do not define a nontrivial standard dynamical Euler product. \(\square\)

#### Scope of the corollary

The corollary does not apply to the open Dirichlet series of Corollary 2, because that series is indexed by double cosets rather than primitive hyperbolic conjugacy classes.  It also does not apply to an Euler product whose norm uses trace, eigenvalue, full word data, or an enlarged cocycle.

### Theorem 8: zero-free-normalization divisor no-go

Let
\[
\Phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
\]
Let \(a,b\in\mathbb C\) with \(a\ne0\), and let \(h:\mathbb C\to\mathbb C\) be entire and zero-free.  Then
\[
h(s)\Phi(as+b)
\]
is not entire.  Consequently, it cannot equal \(\xi(s)\) as a global meromorphic identity.

#### Proof

Let \(\rho\) be any nontrivial zero of \(\zeta\), with multiplicity \(m\).  The completed function \(\Lambda\) has a zero of multiplicity \(m\) at \(\rho\).

At \(s=\rho/2\), the denominator of \(\Phi(s)\) equals \(\Lambda(\rho)=0\).  The numerator is \(\Lambda(\rho-1)\).  The functional equation
\[
\Lambda(u)=\Lambda(1-u)
\]
gives
\[
\Lambda(\rho-1)=\Lambda(2-\rho).
\]
Since \(0<\Re\rho<1\), one has \(\Re(2-\rho)>1\).  In that half-plane, \(\zeta\) is nonzero, while the gamma and power-of-\(\pi\) factors are finite and nonzero.  Hence
\[
\Lambda(\rho-1)\ne0.
\]
Therefore \(\Phi\) has a pole of multiplicity \(m\) at \(s=\rho/2\).

Likewise, at \(s=(1+\rho)/2\), the numerator is \(\Lambda(\rho)=0\), while the denominator is \(\Lambda(1+\rho)\ne0\) because \(\Re(1+\rho)>1\).  Thus \(\Phi\) has a zero of multiplicity \(m\) at the shifted point.  In particular, the nontrivial poles are not canceled internally.

Because \(a\ne0\), the affine map \(s\mapsto as+b\) is bijective.  Hence \(\Phi(as+b)\) has a pole at
\[
s_\rho=\frac{\rho/2-b}{a}.
\]
The value \(h(s_\rho)\) is finite and nonzero because \(h\) is entire and zero-free.  Multiplication by \(h\) cannot remove the pole.  Thus \(h(s)\Phi(as+b)\) is not entire.  Since \(\xi(s)\) is entire, the two functions cannot be globally identical. \(\square\)

#### Relation to \(\xi\)

From
\[
\xi(u)=\tfrac12u(u-1)\Lambda(u)
\]
one obtains the exact identity
\[
\Phi(s)
=\frac{s}{s-1}\frac{\xi(2s-1)}{\xi(2s)}.
\]
This makes the two shifted nontrivial divisors explicit and separates them from the elementary rational factor.

#### Cusp scaling belongs to the allowed class

Suppose the constant term of a normalized Eisenstein series is
\[
y^s+\Phi(s)y^{1-s}.
\]
Set \(y'=r y\) with \(r>0\).  Since \(y=y'/r\), the same term becomes
\[
r^{-s}y'^s+\Phi(s)r^{s-1}y'^{1-s}.
\]
Multiplying the Eisenstein series by \(r^s\) restores incoming coefficient \(1\) and changes the scattering coefficient to
\[
\Phi_r(s)=r^{2s-1}\Phi(s).
\]
The factor \(r^{2s-1}=\exp((2s-1)\log r)\) is entire and zero-free, so Theorem 8 applies.

#### Boundary of the divisor theorem

The conclusion is a global meromorphic-identity no-go.  If a normalizer is allowed to have zeros at the poles of \(\Phi(as+b)\), or is allowed to carry a compensating meromorphic zeta divisor, then cancellation can occur.  Such a factor lies outside the theorem because it inserts the missing divisor rather than changing only the cusp normalization.

## Remarks and Interpretation

1. **Open and closed clocks are different types.**  The totient coefficient is naturally indexed by oriented cusp double cosets.  The Selberg clock is naturally indexed by hyperbolic conjugacy classes.  The proof does not manufacture a power law on the double-coset set.

2. **The square-law theorem is the main exact obstruction.**  Failure of \(2\log c\) alone would be a special example.  Theorem 4 rules out every final-denominator-only function, with no regularity assumptions and at every fixed positive scale.

3. **The stable limit is a positive-control bridge.**  The literal height is not exactly homogeneous, but its power growth rate is the translation length.  This explains why power stabilization returns to the Mayer--Selberg clock.

4. **No uniqueness beyond the stated class.**  The stable limit is canonical for the sequence \(H_\alpha(g^n)/n\).  The package does not classify all homogeneous class functions and does not claim a unique repair.

5. **The divisor theorem is supporting.**  It prevents a zero-free normalization from converting a quotient with shifted poles into a single entire xi function.  It is not the source of the main theorem delta.

## Boundaries and Non-Claims

The theorem package does not exclude any of the following:

- local denominator increments whose periodic Birkhoff sum is not a function of final \(|c(g)|\) alone;
- cyclic sums, cyclic symmetrizations, or cohomological corrections;
- observables depending on \(c(g)\) together with trace, eigenvalues, endpoints, or full word chronology;
- matrix-valued, projective, or noncommutative cocycles;
- subadditive pressure or asymptotically additive potentials;
- open scattering groupoids, relative trace formulae, or non-Euler-product channel series;
- multi-cusp, congruence, Bianchi, or \(S\)-arithmetic extensions;
- homogeneous class functions that are not \(o(n)\)-close to \(H_\alpha(g^n)\) along powers;
- meromorphic or divisor-carrying normalizers with zeros placed to cancel scattering poles;
- a separately derived self-adjoint operator or another Hilbert--Pólya route.

The package also does not claim a proof of RH, a new formula for the scattering coefficient, a new Selberg determinant, or a new interpretation of scattering geodesics.

## Verification Ledger

The universal claims are proved above.  The existing machine outputs provide the following independent regression checks:

- `double_coset_counts.csv`: exact counts through \(c=80\), all equal to \(\varphi(c)\);
- `exact_certificates.json`: exact conjugacy, Gauss cyclic, positive-family, and Chebyshev certificates;
- `gauss_word_clock_audit.csv`: 274 ordered words audited, 259 with cyclic denominator variation, and no literal square-additivity pass;
- `homogenization.csv`: exact-formula high-precision residual below \(2.7\times10^{-79}\);
- `dirichlet_convergence.csv`: finite Dirichlet sums checked against an explicit elementary tail bound;
- `summary.json`: confirms that no prime or Riemann-zero table entered the producer.
- `independent_check.json`: records a 110-digit, non-importing reimplementation
  of all six producer artifacts and 910 audited rows.

These outputs are not used to infer the theorems and do not change their quantifiers.

## Open Risks

- The standalone external novelty is limited because most ingredients are classical; the contribution is their exact compatibility synthesis and the arbitrary-\(F\) rigidity theorem.
- The divisor theorem is elementary once the allowed normalization class is frozen; it should remain a supporting corollary.
- A broader title could be misread as excluding all cusp-derived roofs.  Every paper title and abstract must retain “final-denominator-only” or an equivalent scope marker.
- A successor construction may evade the theorem by introducing extra state.  Such an escape is legitimate, but its extra structure and its source must be stated explicitly rather than described as a repair within the proved class.
