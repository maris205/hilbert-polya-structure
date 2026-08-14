# Proof Package

## Claim

Let \(\Gamma_0\) be a finite set of signed primitive determinant-one H6
monodromies.  For each \(\gamma\in\Gamma_0\), let \(\lambda_\gamma\) be its
signed unstable algebraic-unit multiplier, let
\(K_\gamma=\mathbb Q(\lambda_\gamma)\), and let
\(F_\gamma=K_\gamma^{\langle\lambda\mapsto\lambda^{-1}\rangle}\).  For a
finite set \(S\subset\{(\gamma,n):\gamma\in\Gamma_0,n>2\}\), define

\[
\beta_{\gamma,n}
=\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma)
\in\mathcal O_{F_\gamma}.
\]

Let \(\mathcal A_S\) be the set of triples
\((\gamma,n,\mathfrak q)\) for which
\(\mathfrak q\mid(\beta_{\gamma,n})\) in \(\mathcal O_{F_\gamma}\), and let

\[
\operatorname{Div}_{\rm tag}(S)
=\bigoplus_{(\gamma,n,\mathfrak q)\in\mathcal A_S}
\mathbb Z[\gamma,n,\mathfrak q].
\]

Then:

1. The tagged packet divisor

   \[
   \mathscr D_S=\sum_{(\gamma,n)\in S}
   \sum_{\mathfrak q}v_{\mathfrak q}(\beta_{\gamma,n})
   [\gamma,n,\mathfrak q]
   \]

   is canonical relative to the signed monodromy and the finite set \(S\).

2. The homomorphism

   \[
   \nu_S:[\gamma,n,\mathfrak q]\longmapsto
   f(\mathfrak q/p)[p],\qquad p=\mathfrak q\cap\mathbb Z,
   \]

   gives the exact rational norm divisor, packet by packet.

3. If \(\mathfrak P\) is a prime of \(K_\gamma\) above
   \(\mathfrak q\mid(\beta_{\gamma,n})\), with residue characteristic
   \(p\nmid n\), then the reduction of \(\lambda_\gamma\) in
   \((\mathcal O_{K_\gamma}/\mathfrak P)^\times\) has exact order \(n\).

4. On the H6 certificate formed by the exact signed primitive periods 1, 3,
   and 4 and indices \(3\le n\le20\), \(\nu_S\) has free kernel rank 30.
   Hence rational-prime-only pushforward is noninjective on this source data.

## Status

**PROVABLE AS STATED.**

Items 1--3 are elementary finite algebraic statements.  Item 4 is an exact
finite certificate.  No infinite direct sum, asymptotic prime law, analytic
continuation, or operator is claimed.

## Assumptions

- Every \(\lambda_\gamma\) is an algebraic unit, is not a root of unity, and
  has inversion as a nontrivial field automorphism.
- The signed branch is part of the source data.
- The cyclotomic index satisfies \(n>2\).
- The exact-order conclusion is asserted only when \(p\nmid n\).
- The tagged assembly is finite; no convergence issue is hidden in the
  definition.

## Notation

- \(\Phi_n\) is the \(n\)-th cyclotomic polynomial.
- \(v_{\mathfrak q}\) is the normalized prime-ideal valuation.
- \(f(\mathfrak q/p)=[\mathcal O_F/\mathfrak q:\mathbb F_p]\) is the residue
  degree.
- \([p]\) is the basis vector of the free abelian divisor group on rational
  primes.
- A multiplier prime \(\mathfrak P\) and its contracted trace-field prime
  \(\mathfrak q\) are distinct objects and are never conflated.

## Proof Strategy

Use HCS-P49 to place each unit-normalized cyclotomic value in the trace-field
integer ring.  Factor those principal ideals before taking norms.  The norm
identity follows from the definition of ideal norm.  Extend a supporting
trace prime to the multiplier field; away from residue characteristics
dividing \(n\), separability of \(X^n-1\) forces a root of \(\Phi_n\) to have
exact order \(n\).  Finally decompose the finite pushforward into one block
per rational prime and compute its free kernel rank.

## Dependency Map

1. HCS-P49 proves
   \(\beta_{\gamma,n}\in\mathcal O_{F_\gamma}\) for \(n>2\).
2. Unique factorization of nonzero ideals supplies the tagged atoms and
   valuations.
3. The standard ideal-norm identity supplies the residue-degree weights.
4. Cyclotomic factorization plus separability supplies exact residue order
   at \(p\nmid n\).
5. Elementary structure theory of homomorphisms of finite free abelian
   groups supplies the kernel rank.
6. The H6 counts, split-prime valuations, and collision witnesses are locked
   by `results/c50_certificate.json` and `code/test_c50.py`.

## Proof

### Step 1: trace-field integrality and canonical finite atoms

For \(n>2\), \(\varphi(n)\) is even.  Cyclotomic reciprocity gives

\[
\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma)
=\lambda_\gamma^{\varphi(n)/2}\Phi_n(\lambda_\gamma^{-1}),
\]

so \(\beta_{\gamma,n}\) is fixed by inversion.  Both factors in its
definition are algebraic integers because \(\lambda_\gamma\) is a unit.
Thus \(\beta_{\gamma,n}\in\mathcal O_{F_\gamma}\).  Unique factorization of
nonzero ideals gives

\[
(\beta_{\gamma,n})=
\prod_{\mathfrak q}\mathfrak q^{v_{\mathfrak q}(\beta_{\gamma,n})}.
\]

Because \(S\) is finite, taking the free direct sum of all source triples
introduces no convergence or ordering ambiguity.  The signed branch,
cyclotomic index, and prime ideal are part of the basis symbol, proving item
1.  “Canonical” here is relative to the fixed source data; no universal
minimality among all possible encodings is asserted.

### Step 2: exact norm pushforward

If \(p=\mathfrak q\cap\mathbb Z\), the absolute ideal norm of
\(\mathfrak q\) is \(p^{f(\mathfrak q/p)}\).  Therefore

\[
|N_{F_\gamma/\mathbb Q}(\beta_{\gamma,n})|
=\prod_{\mathfrak q\mid(\beta_{\gamma,n})}
p^{f(\mathfrak q/p)v_{\mathfrak q}(\beta_{\gamma,n})}.
\]

Taking the rational prime divisor of both sides gives exactly

\[
\operatorname{div}_{\mathbb Z}
|N_{F_\gamma/\mathbb Q}(\beta_{\gamma,n})|
=\nu_S\!\left(
\sum_{\mathfrak q}v_{\mathfrak q}(\beta_{\gamma,n})
[\gamma,n,\mathfrak q]\right).
\]

Linearity proves the corresponding identity for \(\mathscr D_S\).

### Step 3: good-characteristic residue order

Let \(\mathfrak P\) lie above a supporting trace prime \(\mathfrak q\).
Because \(\beta_{\gamma,n}\in\mathfrak q\subset\mathfrak P\) and
\(\lambda_\gamma^{\varphi(n)/2}\) is a unit,
\(\Phi_n(\lambda_\gamma)\in\mathfrak P\).  Let \(\bar\lambda\) denote the
reduction of \(\lambda_\gamma\) modulo \(\mathfrak P\).

Suppose the residue characteristic \(p\) does not divide \(n\).  Then
\(X^n-1\) is separable over characteristic \(p\).  Reducing

\[
X^n-1=\prod_{d\mid n}\Phi_d(X)
\]

modulo \(p\), its monic factors are pairwise coprime: a shared root would
make the product non-squarefree.  Since \(\Phi_n(\bar\lambda)=0\), we have
\(\bar\lambda^n=1\).  If its order were a proper divisor \(d<n\), then it
would also be a root of \(X^d-1=\prod_{e\mid d}\Phi_e(X)\), contradicting
coprimality with \(\Phi_n\).  Hence the order is exactly \(n\).

When \(p\mid n\), exact order \(n\) is impossible because the multiplicative
group of a finite field of characteristic \(p\) has order prime to \(p\).
Separability and pairwise coprimality can also fail.  The theorem therefore
makes no claim about the actual smaller order there.

### Step 4: finite pushforward kernel

Group the basis atoms by their contracted rational prime.  If \(m_p\) atoms
lie above \(p\), the corresponding block of \(\nu_S\) is

\[
\mathbb Z^{m_p}\longrightarrow\mathbb Z,
\qquad (x_1,\ldots,x_{m_p})\longmapsto
\sum_{i=1}^{m_p}f_i x_i,
\]

where every \(f_i>0\).  This block has rank one and hence a free kernel of
rank \(m_p-1\).  Summing over rational primes gives

\[
\operatorname{rank}\ker\nu_S
=\#\mathcal A_S-#\{p:\text{some atom lies over }p\}.
\]

The exact H6 certificate has 125 atoms and 95 distinct rational primes, so
the rank is \(125-95=30\).  Thus the pushforward is noninjective.

### Step 5: independent tag witnesses

The certificate records three independent finite failures of a coarser key.

- Orbit tag: at \(p=109,n=11\), atoms arise from periods one and three.
- Index tag: \(p=29\) supports certified orders 7, 14, and 15.
- Prime-ideal tag: period one at \(p=109,n=11\) has two distinct split trace
  primes.

The signed period-three branch is separately mutation-tested.  These
witnesses establish loss for the displayed coarsenings on this certificate;
they do not claim categorical minimality of the chosen representation. ∎

## Corrections or Missing Assumptions

- The proof distinguishes a trace-field prime \(\mathfrak q\) from a
  multiplier-field prime \(\mathfrak P\) above it.
- The exact-order theorem excludes \(p\mid n\); all 20 such certificate atoms
  are explicitly marked uncertified.
- The norm pushforward includes residue degree, not only ideal valuation.
- The finite direct sum is not silently promoted to an infinite all-orbit
  sum.

## Open Risks

- An all-orbit tagged divisor measure needs a pressure-compatible cutoff and
  a convergence theorem.
- A useful rational pushforward may require derived weights and controlled
  cancellation; noninjectivity alone does not rule that out.
- Existing primitive-divisor theorems do not provide the varying-orbit H6
  packet assembly or a von Mangoldt trace.
- No transfer operator, analytic continuation, functional equation, or
  self-adjoint operator has been constructed.
