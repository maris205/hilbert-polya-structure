# A genuine nonhyperbolic FAD example

2026-09-06. This is an application and verification supplement to
`PROOF_PACKAGE.md`, not a separate novelty claim or a new C-candidate.

## 1. A concrete Salem toral automorphism

Put
$$
P(X)=X^4-X^3-X^2-X+1,
\qquad
A=\begin{pmatrix}
0&0&0&-1\\
1&0&0&1\\
0&1&0&1\\
0&0&1&1
\end{pmatrix}.
$$
This is the companion matrix of $P$, so $\det A=1$ and $A$ induces an
automorphism $T_A$ of the genuine compact group $\mathbb R^4/\mathbb Z^4$.

The polynomial is irreducible over $\mathbb Q$. Indeed, modulo 2 it is
$X^4+X^3+X^2+X+1$. It has no roots in $\mathbb F_2$, and the only monic
irreducible quadratic $X^2+X+1$ does not divide it: reduction modulo that
quadratic gives $X+1$. These observations exclude every possible proper
factorization of this monic quartic over $\mathbb F_2$; Gauss's lemma
then gives the assertion over $\mathbb Q$.

For $X\ne0$, division by $X^2$ and setting $Y=X+X^{-1}$ gives
$$
X^{-2}P(X)=Y^2-Y-3.
$$
The two values $y_+=(1+\sqrt{13})/2>2$ and
$y_-=(1-\sqrt{13})/2\in(-2,2)$ therefore show that the four roots of
$P$ are $\lambda,\lambda^{-1},\eta,\eta^{-1}$, where $\lambda>1$,
$|\eta|=1$, and $\eta$ is nonreal. None is a root of unity: for
$\eta$ this follows because its irreducible polynomial also has the
real root $\lambda>1$, whereas all conjugates of a root of unity are
roots of unity. In particular every $A^n-I$ is invertible over
$\mathbb Q$.

The fixed subgroup of $T_A^n$ is naturally identified with
$\mathbb Z^4/(A^n-I)\mathbb Z^4$. Smith normal form, or the index of
an integer lattice, gives its cardinality
$$
\tag{E1}
t_n=|\det(A^n-I)|
=(\lambda^n+\lambda^{-n}-2)(2-\eta^n-\eta^{-n})>0.
$$
No density-of-orbits theorem is needed for this fixed-count identity.

## 2. A genuine wild additive system

Let $p$ be an odd prime and let $U$ be the endomorphism
$U(x)=x^p+x$ of the additive group $\overline{\mathbb F}_p$. Write
$\Phi(x)=x^p$, so $U=1+\Phi$ in its endomorphism ring. If $n=p^a m$
with $p\nmid m$, the characteristic-$p$ polynomial identity gives
$$
(1+T)^n-1=\big((1+T)^m-1\big)^{p^a}.
$$
Its lowest nonzero $T$-degree is $p^a$, with nonzero coefficient, and
its highest degree is $n$. Substituting the commuting endomorphism
$\Phi$ shows that $U^n-1$ is an additive polynomial of ordinary
degree $p^n$ whose smallest nonzero monomial has ordinary degree
$p^{p^a}$. Since the coefficient field is perfect, it is a
$p^{p^a}$-th power of a separable polynomial of degree
$p^{n-p^a}$. The latter polynomial has nonzero linear coefficient and
splits with distinct roots over $\overline{\mathbb F}_p$. Thus
$$
\tag{E2}
u_n=\#\operatorname{Fix}(U^n)=p^{n-p^{v_p(n)}}.
$$
This standard wild fixed-count formula is reverified here only to make
the example self-contained. Its previous use in the project is not
counted as new work.

## 3. The product and the genuinely nonhyperbolic conclusion

Let $X=(\mathbb R^4/\mathbb Z^4)\times\overline{\mathbb F}_p$ and
$f=T_A\times U$, a self-map of an actual set. Product fixed sets and
(E1)–(E2) give
$$
\tag{E3}
f_n=|\det(A^n-I)|\,p^n\,p^{-p^{v_p(n)}}.
$$
Every $f_n$ is finite and positive. This is a FAD presentation with
$c=p$, $r_n=1$, $S=\{p\}$, $s_{p,n}=0$, $t_{p,n}=1$; all periodic
data have period one and meet the gcd-sequence restrictions.

With $\Lambda=p\lambda$, its dominant normalized factor is
$$
2-\eta^n-\eta^{-n}.
$$
The three dominant characteristic roots are
$\Lambda,\Lambda\eta,\Lambda\eta^{-1}$, with respective nonzero
multiplicities $2,-1,-1$. They belong to different root-of-unity ratio
classes: $\eta$ is not torsion, and if $\eta^2$ were torsion then so
would be $\eta$. Consequently the system is **not hyperbolic in the
unique-dominant-root sense of BCH Definition 10.3.9**. It does not enter
the old natural-boundary theorem by a relabeling of terms or by an
iterate removing torsion.

The theorem in `PROOF_PACKAGE.md` now gives a natural boundary, even
against meromorphic continuation, at
$$
|z|=(p\lambda)^{-1}
$$
for both $\sum_{n\ge1}f_nz^n$ and
$\zeta_f(z)=\exp(\sum_{n\ge1}f_nz^n/n)$. Here the wild active fibre is
already the unique period-one residue. This conclusion concerns the
actual product system and its ordinary integer clock.

The example is supplied to demonstrate the removed hypothesis; neither
the toral determinant formula nor the additive fixed-count formula is
claimed as a new theorem. The example also does not assert an algebraic
group realization of this mixed characteristic-zero/positive-characteristic
product. Such a realization is unnecessary for a FAD **system**.

## 4. Why the general denominator criterion cannot simply be applied

For clarity, the normalized coefficients $a_n=f_n/(p\lambda)^n$ lie
in a number field. An embedding sending $\lambda$ to
$\lambda^{-1}$ sends $a_n$ to $\lambda^{2n}a_n$, since $f_n$ is an
integer. On integers coprime to $p$, the wild normalized factor is the
fixed positive number $p^{-1}$. Along a subsequence in one such residue
class, $2-\eta^n-\eta^{-n}$ is bounded below by a positive constant:
otherwise its entire irrational rotation orbit would converge to zero,
which is impossible, or directly use density of the powers of
$\eta^p$. Thus $\limsup |a_n|^{1/n}=1$ and the conjugated normalized
series has radius $\lambda^{-2}<1$.

Hence the all-embeddings unit-disc convergence assumption in
Bell–Gunn–Nguyen–Saunders Theorems 1.2 and 1.6 is not available here.
This is a failure of that sufficient criterion, not a criticism of it.
