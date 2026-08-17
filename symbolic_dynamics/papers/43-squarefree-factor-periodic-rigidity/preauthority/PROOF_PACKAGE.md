# Proof package

## Main theorem

### Theorem: squarefree factor periodic rigidity

Let

\[
X_{\rm sf}=\{x\in\{0,1\}^{\mathbb Z}:
\operatorname{supp}(x)\bmod p^2
\ne\mathbb Z/p^2\mathbb Z\text{ for every rational prime }p\}
\]

with the two-sided left shift \(\sigma\). Let \((Y,S)\) be a compact
metrizable \(\mathbb Z\)-system and let
\(\pi:X_{\rm sf}\twoheadrightarrow Y\) be continuous, surjective, and
equivariant. Then

\[
\operatorname{Per}(Y,S)=\{\pi(0^{\mathbb Z})\}.
\]

In particular, for every \(m\ge1\),

\[
\#\operatorname{Fix}(S^m)=1,
\qquad
\zeta_{\rm AM,Y}(z)=\frac1{1-z},
\qquad
D_{\rm AM,Y}(z)=1-z.
\]

### Status

`PROVED`, subject to independent verification of the frozen definitions and
literature collision boundary.

## Assumptions

1. Every rational-prime-square exclusion in the definition is enforced.
2. Both source and target carry \(\mathbb Z\)-actions by homeomorphisms.
3. The factor map is continuous, onto, and equivariant for all integer times.
4. Periodic objects are ordinary point orbits under \(S\).
5. The determinant is the inverse Artin--Mazur zeta from fixed-point counts.

No finite-to-one, finite-memory, finite-alphabet, expansivity, soficity, or
smoothness assumption is used.

## Dependency map

```text
source topology <- finite cylinder witnesses
source proximality <- infinitely many distinct primes + CRT
factor proximality <- surjectivity + compact uniform continuity + equivariance
periodic rigidity <- proximality + fixed-point image + finite-orbit separation
zeta identity <- exact fixed-point counts + sum z^m/m = -log(1-z)
primitive firewall <- unique primitive orbit + temporal repetition definition
```

## Lemma 1: the source is a compact shift system

For a fixed prime \(p\), let \(F_p\) be the set of sequences whose support
meets every residue class modulo \(p^2\). If \(x\in F_p\), choose for each of
the finitely many residues a coordinate in that residue at which \(x\) is one.
The cylinder forcing those finitely many coordinates to remain one is
contained in \(F_p\). Hence \(F_p\) is open, and its complement is closed.

Therefore

\[
X_{\rm sf}=\bigcap_{p\in\mathbb P}(\{0,1\}^{\mathbb Z}\setminus F_p)
\]

is closed in the compact full shift. Translation of a support permutes its
residue classes modulo every \(p^2\), so \(X_{\rm sf}\) is shift invariant.
Thus it is a compact metrizable \(\mathbb Z\)-system. The all-zero point
belongs to it and is fixed. \(\square\)

## Lemma 2: the source is proximal

Take arbitrary \(x,y\in X_{\rm sf}\). Fix \(L\ge0\). For every
\(j\in\{-L,\ldots,L\}\), choose two rational primes \(p_{j,x}\) and
\(p_{j,y}\), with all \(2(2L+1)\) primes distinct.

Because \(x\) is admissible, choose

\[
a_{j,x}\notin\operatorname{supp}(x)\bmod p_{j,x}^2.
\]

Likewise choose

\[
a_{j,y}\notin\operatorname{supp}(y)\bmod p_{j,y}^2.
\]

All chosen prime squares are pairwise coprime. By the Chinese remainder
theorem, there is an integer \(n_L\), which may be chosen nonnegative, such
that simultaneously

\[
n_L+j\equiv a_{j,x}\pmod{p_{j,x}^2},
\qquad
n_L+j\equiv a_{j,y}\pmod{p_{j,y}^2}
\]

for all \(j\in[-L,L]\). Hence

\[
x_{n_L+j}=y_{n_L+j}=0
\qquad(-L\le j\le L).
\]

Thus \(\sigma^{n_L}x\) and \(\sigma^{n_L}y\) agree on \([-L,L]\). In any
compatible product metric their distance tends to zero as \(L\to\infty\).
Every pair is proximal. \(\square\)

## Lemma 3: a continuous factor of a proximal compact system is proximal

Let \(y_1,y_2\in Y\). By surjectivity, choose \(x_1,x_2\in X_{\rm sf}\)
with \(\pi(x_i)=y_i\). For \(\varepsilon>0\), uniform continuity of \(\pi\)
gives \(\delta>0\) such that

\[
d_X(u,v)<\delta\Longrightarrow d_Y(\pi u,\pi v)<\varepsilon.
\]

By Lemma 2, some \(n\ge0\) satisfies
\(d_X(\sigma^n x_1,\sigma^n x_2)<\delta\). Equivariance gives

\[
d_Y(S^n y_1,S^n y_2)<\varepsilon.
\]

Since \(\varepsilon\) was arbitrary, \((y_1,y_2)\) is proximal. \(\square\)

## Lemma 4: a proximal compact system with a fixed point has no other periodic point

Let \((Y,S)\) be proximal and let \(y_0\) be fixed. Suppose \(y\) is
periodic of least period \(r\).

If \(r=1\) and \(y\ne y_0\), then

\[
d_Y(S^n y,S^n y_0)=d_Y(y,y_0)>0
\]

for every \(n\), so the pair is not proximal.

If \(r>1\), the \(r\) pairs
\((S^k y,S^{k+1}y)\), \(0\le k<r\), are all pairs of distinct points. Hence

\[
\delta=\min_{0\le k<r}d_Y(S^k y,S^{k+1}y)>0.
\]

For every \(n\ge0\), reduction of \(n\) modulo \(r\) gives

\[
d_Y(S^n y,S^n(Sy))\ge\delta.
\]

The pair \((y,Sy)\) is not proximal, again a contradiction. Therefore the
only periodic point is \(y_0\). \(\square\)

## Proof of the main theorem

By equivariance,

\[
y_0=\pi(0^{\mathbb Z})
\]

is fixed. Lemmas 2 and 3 make \(Y\) proximal. Lemma 4 then shows that
\(y_0\) is its unique periodic point. Therefore
\(\operatorname{Fix}(S^m)=\{y_0\}\) for all \(m\ge1\).

The Artin--Mazur definition now gives

\[
\zeta_{\rm AM,Y}(z)
=\exp\left(\sum_{m\ge1}\frac{z^m}{m}\right)
=\frac1{1-z},
\]

and inversion gives \(D_{\rm AM,Y}(z)=1-z\). \(\square\)

## Proposition: primitive-support obstruction

Under the frozen primitive and marker types, no lawful factor ledger can be
identified bijectively with the rational-prime primitive ledger.

### Proof

The main theorem gives one primitive orbit, the fixed orbit
\(\mathcal O_0\). Every term \(z^r\) in the logarithm is an \(r\)-fold
traversal of \(\mathcal O_0\), not a new primitive orbit. The rational-prime
ledger has one distinct primitive atom for every rational prime, hence
infinitely many primitive atoms. A bijection of primitive types cannot exist.
This failure precedes any assignment of clock weights. \(\square\)

## Proposition: no finite prime-square approximation suffices

Let \(P_0\subset\mathbb P\) be finite and define

\[
Q=\prod_{p\in P_0}p^2.
\]

For nonempty \(P_0\), define \(x\in\{0,1\}^{\mathbb Z}\) by

\[
x_n=1\quad\Longleftrightarrow\quad n\equiv1\pmod Q.
\]

The point is nonzero and \(Q\)-periodic. For every \(p\in P_0\), divisibility
\(p^2\mid Q\) gives

\[
\operatorname{supp}(x)\bmod p^2=\{1\bmod p^2\},
\]

which is a proper subset of \(\mathbb Z/p^2\mathbb Z\). Hence \(x\) satisfies
all finite constraints. Its least positive period is \(Q\): if \(d>0\) is a
period, then \(x_1=1\) forces \(x_{1+d}=1\), so \(Q\mid d\).

If \(P_0\) is empty, take \(Q=1\) and \(x=1^{\mathbb Z}\); the constraints
are vacuous, and this second fixed point already precludes proximality with
\(0^{\mathbb Z}\).

Thus every finite prime-square approximation has a nonzero periodic point.
For nonempty \(P_0\) it has a nontrivial period-\(Q\) orbit; for empty
\(P_0\) it has two distinct fixed points. In either case, the source-only
periodic collapse and the all-factor proximal conclusion fail. \(\square\)

## Sharpness and edge cases

1. **Infinite exclusions are essential.** The preceding proposition gives a
   nonzero periodic point for every finite prime set. With only modulus four,
   \((0111)^{\mathbb Z}\) is an additional least-period-four example.
2. **Proximality is essential.** Absence of source periodic points alone does
   not prevent a periodic factor.
3. **Surjectivity is used.** It supplies lifts of arbitrary target pairs.
4. **Continuity is used.** It transports small source distances to the target.
5. **Equivariance is used.** It identifies shifted images and makes
   \(\pi(0^{\mathbb Z})\) fixed.
6. **The target action is a \(\mathbb Z\)-action.** The theorem is not stated
   for an unrelated noninvertible observation.
7. **The periodic-core matrix is limited.** It certifies the singleton count
   but is not a full dynamical transfer operator.

## Claim boundary

The theorem applies only to continuous surjective equivariant factors of the
exact all-prime-square admissible shift. It does not prohibit cycles in
finite-modulus approximants, extensions, products, induced systems, or
changed observables, and it does not claim a completed arithmetic determinant.
