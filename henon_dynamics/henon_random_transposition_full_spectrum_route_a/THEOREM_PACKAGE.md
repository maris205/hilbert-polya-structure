# C183 theorem package: random transpositions

## Frozen object

For \(n\ge 2\), let \(\mu_n(e)=1/n\) and \(\mu_n(\tau)=2/n^2\) for each transposition \(\tau\in S_n\). Equivalently, draw an ordered pair \((i,j)\) uniformly and apply \((ij)\), interpreting \((ii)=e\). On \(L^2(S_n,u_n)\), where \(u_n\) is uniform probability, define

\[
(P_nf)(\sigma)=\sum_{g\in S_n}\mu_n(g)f(\sigma g).
\]

One application of \(P_n\) is the only clock. The determinant convention is the finite matrix polynomial \(\det(I-zP_n)\). On the frozen state space \(S_n\), it is not an unweighted Artin--Mazur orbit determinant.

## Theorem 1: complete all-size spectrum

For every partition \(\lambda\vdash n\), let \(d_\lambda\) be the Specht dimension and let \(\tau\) be any transposition. Centrality and Schur's lemma make \(P_n\) scalar on each copy of the \(\lambda\)-representation. The scalar is

\[
\beta_\lambda
=\frac1n+\frac{n-1}{n}\frac{\chi_\lambda(\tau)}{d_\lambda}
=\frac1n+\frac1{n^2}\sum_{i\ge1}
\left(\lambda_i^2-(2i-1)\lambda_i\right).
\]

In the regular representation, the \(\lambda\)-isotypic component has dimension \(d_\lambda^2\). Hence

\[
\operatorname{Spec}(P_n)=
\{\beta_\lambda\text{ with multiplicity }d_\lambda^2:\lambda\vdash n\},
\]

\[
\det(I-zP_n)=\prod_{\lambda\vdash n}(1-z\beta_\lambda)^{d_\lambda^2},
\qquad
\operatorname{Tr}(P_n^k)=\sum_{\lambda\vdash n}d_\lambda^2\beta_\lambda^k.
\]

Zero eigenvalues contribute the unit factor, so the polynomial degree is the total multiplicity of nonzero sectors and can be smaller than \(n!\).

### Proof

The probability measure \(\mu_n\) is constant on conjugacy classes. Its group Fourier transform at an irreducible representation \(\rho_\lambda\) therefore commutes with \(\rho_\lambda(S_n)\) and is scalar. Taking its trace gives \(1/n+(n-1)\chi_\lambda(\tau)/(nd_\lambda)\). The Frobenius transposition formula gives the displayed content sum. The regular representation contains \(d_\lambda\) copies of a \(d_\lambda\)-dimensional irreducible, yielding multiplicity \(d_\lambda^2\). Multiplying or summing the spectral factors proves the determinant and trace identities.

The hook-length formula gives \(d_\lambda=n!/\prod_{c\in\lambda}h(c)\). The identity \(\sum_{\lambda\vdash n}d_\lambda^2=n!\) verifies that no sector is missing.

## Theorem 2: return and exact \(L^2\) laws

Let \(X_k\) start at the identity. Translation invariance gives

\[
\Pr(X_k=e)=\frac1{n!}\operatorname{Tr}(P_n^k)
=\frac1{n!}\sum_{\lambda\vdash n}d_\lambda^2\beta_\lambda^k.
\]

Since each step has \(n^2\) equiprobable ordered-pair labels, \(n^{2k}\Pr(X_k=e)\) is the exact number of length-\(k\) ordered-pair words returning to the identity. If \(h_k=(d\Pr(X_k\in\cdot)/du_n)-1\), Plancherel and centrality give

\[
\|h_k\|_{L^2(u_n)}^2
=\sum_{\lambda\ne(n)}d_\lambda^2\beta_\lambda^{2k}.
\]

Conjugating a Young diagram twists by the sign representation, hence its transposition ratio changes sign and

\[
\beta_{\lambda'}=\frac2n-\beta_\lambda.
\]

The trivial sector has eigenvalue \(1\); the \((n-1,1)\)-sector has \(1-2/n\), which is the largest nontrivial eigenvalue, while the sign sector has \(-1+2/n\), the bottom eigenvalue. Thus the spectral gap is exactly \(2/n\). The classical total-variation cutoff at \(\tfrac12n\log n\) belongs to Diaconis and Shahshahani; this package does not claim priority for it.

## Theorem 3: exact owner boundary

Because \(\mu_n(g)=\mu_n(g^{-1})\), the operator \(P_n\) is self-adjoint. On frozen \(S_n\), each state has several positive-probability successors, so \(P_n\) is not induced by a single-valued deterministic map. It is also not a permutation Koopman operator. An abstract unitary dilation exists only after enlarging the Hilbert space and does not restore deterministic source orbits on \(S_n\).

This frozen-space statement does not forbid every primitive-cycle factorization after changing the object. Let the directed support graph of \(P_n\) have edge weight \(P_n(x,y)\), and let \([\gamma]\) range over primitive closed directed paths modulo cyclic rotation, with

\[
w(\gamma)=\prod_{e\in\gamma}P_n(e).
\]

Then, as a formal power series,

\[
\det(I-zP_n)^{-1}
=\exp\!\left(\sum_{k\ge1}\frac{\operatorname{Tr}(P_n^k)}{k}z^k\right)
=\prod_{[\gamma]\ \mathrm{primitive}}
\left(1-w(\gamma)z^{|\gamma|}\right)^{-1}.
\]

The first equality is the finite-matrix trace--log identity. Expanding each trace as a sum over weighted closed paths and grouping every closed path by its primitive cyclic core proves the second. This weighted edge/path-space product is canonical for the Markov matrix, but its owner is a path shift rather than the frozen chain as a deterministic map on \(S_n\). It is therefore not an unweighted Artin--Mazur zeta on the original phase space.

Route-A gate A1 remains `FAIL` for the stated rubric: A0 already fails, and the frozen source supplies no primitive orbit carrying an A0 arithmetic payload. The reason is not an absolute absence of primitive-cycle products after an enlarged or changed phase space.

Prime and composite \(n\) obey the identical partition formula. No rational-prime carrier, prime-power repetition law, logarithmic prime clock, target divisor, functional equation, or Weil compression emerges. The strict evaluation is

\[
(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FORMAL\ HINT}),
\]

with overall `ROUTE_A_REJECTED` and Route B false.

## Scope and edge cases

- \(n=1\) is the one-state identity chain and lies outside the frozen family.
- Laziness is part of the clock; deleting it changes the spectrum and introduces parity periodicity.
- Zero eigenvalues reduce \(\deg\det(I-zP_n)\) by their full multiplicity.
- The frozen determinant is Markov-spectral; its reciprocal gains a weighted primitive-cycle product only on the changed path-space owner.
- No novelty is claimed for the classical random-transposition spectrum or cutoff.
- No external review or literature-wide novelty certificate is claimed.
- Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.
