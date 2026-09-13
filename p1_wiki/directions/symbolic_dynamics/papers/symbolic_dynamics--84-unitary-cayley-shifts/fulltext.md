---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--84-unitary-cayley-shifts"
canonical_tex: "symbolic_dynamics/papers/84-unitary-cayley-shifts/main.tex"
canonical_pdf: "symbolic_dynamics/papers/84-unitary-cayley-shifts/main.pdf"
source_sha256: "fca2a4571c97b3e0403fd612da42daacaf3a6330623a5e48539b602709db4574"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ramanujan Period Spectra and Rigidity of Unitary Cayley Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/84-unitary-cayley-shifts>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/84-unitary-cayley-shifts/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/84-unitary-cayley-shifts/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/84-unitary-cayley-shifts/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/84-unitary-cayley-shifts/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $n\geq2$, let $X_n$ be the nearest-neighbor shift on $\mathbb Z/n\mathbb Z$ in which $x_j$ may be followed by $x_{j+1}$ exactly when their difference is a unit modulo $n$. We compute its complete periodic spectrum from Ramanujan sums: $$\#\operatorname{Fix}(\sigma^k)=
   \sum_{d\mid n}\varphi(d)
   \left(\mu(d)\frac{\varphi(n)}{\varphi(d)}\right)^k.$$ Consequently $$\zeta_{X_n}(z)=
   \prod_{\substack{d\mid n\\ \mu(d)\ne0}}
   \left(1-\mu(d)\frac{\varphi(n)}{\varphi(d)}z\right)^{-\varphi(d)}.$$ The shift is irreducible with entropy $\log\varphi(n)$; it is mixing for odd $n$ and has exact period two for even $n$. Its unique maximal-entropy law is the uniform unit-increment Markov chain. For odd $n$, correlations of vertex observables decay at the sharp spectral rate $(p_{\min}-1)^{-k}$, where $p_{\min}$ is the least prime factor of $n$. Finally, entropy together with the two-period count $n\varphi(n)$ recovers $n$, so distinct members of the family are not topologically conjugate; equivalently, the dynamical zeta function is rigid inside this family.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: Ramanujan Period Spectra and Rigidity of Unitary Cayley Shifts
```

## Markdown 正文

# Introduction

The unitary Cayley graph on $\mathbb Z/n\mathbb Z$ joins two residues when their difference is invertible modulo $n$. Its graph spectrum is classical: Fourier characters diagonalize its adjacency matrix and the eigenvalues are Ramanujan sums. Klotz and Sander established this formula and a broad set of graph-theoretic properties [@KlotzSander2007]. We use that owned spectral input to solve the symbolic dynamics of the associated edge constraint.

For a finite-type shift with adjacency matrix $A$, periodic counts are $\operatorname{tr}(A^k)$ and the Bowen--Lanford identity is $\zeta(z)=\det(I-zA)^{-1}$ [@BowenLanford1970]. Applying these standard facts to the Ramanujan spectrum produces more than a restatement of graph regularity: it gives a divisor-indexed orbit spectrum, an arithmetic mixing-period dichotomy, a sharp correlation rate, and a two-observable conjugacy classifier.

The narrow contribution is this complete dynamical package for the unitary Cayley shift. We do not claim the graph definition, its integral spectrum, Ramanujan-sum identities, the Parry construction, or the finite-type zeta determinant.

# Definition and irreducibility

Let $U_n=(\mathbb Z/n\mathbb Z)^\times$ and let $A_n$ be the $n\times n$ zero-one matrix $$(A_n)_{ab}=\mathbf 1_{\{b-a\in U_n\}},
 \qquad a,b\in\mathbb Z/n\mathbb Z.$$ Define the two-sided vertex shift $$X_n=\{x\in(\mathbb Z/n\mathbb Z)^\mathbb Z:A_{x_jx_{j+1}}=1\text{ for every }j\},$$ with left shift $\sigma$. Every row and column of $A_n$ has $\varphi(n)$ ones. Since $1\in U_n$, the directed graph is connected.

[\[prop:period\]]{#prop:period label="prop:period"} For every $n\geq2$, $X_n$ is irreducible and $$h_{\mathrm{top}}(X_n)=\log\varphi(n).$$ If $n$ is odd, $X_n$ is mixing. If $n$ is even, its exact topological period is two.

Steps by $+1$ connect all residues, proving irreducibility. The constant vector is a positive eigenvector of $A_n$ with eigenvalue $\varphi(n)$; the maximum row sum bounds the spectral radius from above by the same number. The entropy formula follows.

Every edge can be immediately reversed because $-U_n=U_n$, so closed walks of length two exist. If $n$ is odd, $n$ successive $+1$ steps give an odd closed walk; the gcd of $2$ and $n$ is one. If $n$ is even, every unit is odd, so every step changes parity and all closed walks have even length. The existing two-cycles make the period exactly two.

# Ramanujan orbit spectrum

Let $\omega=e^{2\pi i/n}$. The Fourier vector $v_r=(\omega^{ra})_{a\in\mathbb Z/n\mathbb Z}$ is an eigenvector of $A_n$ with eigenvalue $$c_n(r)=\sum_{u\in U_n}\omega^{ru},$$ the Ramanujan sum. If $$d=\frac{n}{\gcd(n,r)},$$ then the classical formula, in the notation convenient here, is $$\label{eq:ramanujan}
 c_n(r)=\mu(d)\frac{\varphi(n)}{\varphi(d)}.$$ Exactly $\varphi(d)$ residues $r$ give a specified divisor $d\mid n$. Indeed, they are $r=(n/d)s$ with $s$ running through the reduced residue classes modulo $d$. This includes the unique class $r=0$ for $d=1$.

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} For every $n\geq2$ and $k\geq1$, $$\label{eq:fixed}
 P_k(n):=\#\operatorname{Fix}_{X_n}(\sigma^k)
 =\sum_{d\mid n}\varphi(d)
 \left(\mu(d)\frac{\varphi(n)}{\varphi(d)}\right)^k.$$ The Artin--Mazur zeta function is the rational function $$\label{eq:zeta}
 \zeta_{X_n}(z)
 =\prod_{\substack{d\mid n\\\mu(d)\ne0}}
 \left(1-\mu(d)\frac{\varphi(n)}{\varphi(d)}z\right)^{-\varphi(d)}.$$ In particular, $$P_1(n)=0,\qquad P_2(n)=n\varphi(n).$$

A point fixed by $\sigma^k$ is a based closed walk of length $k$, so its number is $\operatorname{tr}(A_n^k)$. Summing the $k$th powers of the eigenvalues in [\[eq:ramanujan\]](#eq:ramanujan){reference-type="eqref" reference="eq:ramanujan"}, grouped by $d$, proves [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}. The determinant identity of Bowen and Lanford gives $$\zeta_{X_n}(z)=\det(I-zA_n)^{-1};$$ inserting the eigenvalues and omitting zero factors gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. There are no self-loops, proving $P_1=0$. Alternatively, a based two-step loop is specified by its starting residue and one of $\varphi(n)$ unit increments, so $P_2=n\varphi(n)$.

For example, if $p$ is prime then $X_p$ is the complete graph shift without self-loops and $$\zeta_{X_p}(z)=\frac{1}{(1-(p-1)z)(1+z)^{p-1}}.$$ If $n=2^a$, the only nonzero adjacency eigenvalues are $\pm2^{a-1}$, each simple, and $$\zeta_{X_{2^a}}(z)=\frac{1}{1-2^{2a-2}z^2}.$$ The remaining $n-2$ zero eigenvalues are invisible to periodic counts but not to the alphabet size; the two-period formula retains that size.

# The maximal measure and a sharp mixing rate

Because $A_n$ is irreducible, the shift has a unique measure of maximal entropy, the Parry measure [@Parry1964]. Regularity makes it elementary: the stationary distribution is uniform on $\mathbb Z/n\mathbb Z$ and $$\label{eq:transition}
 \mathbb P(x_{j+1}=b\mid x_j=a)
 =\frac{(A_n)_{ab}}{\varphi(n)}.$$ Equivalently, the increments $x_{j+1}-x_j$ are independent and uniform on $U_n$, with an independent uniform initial residue.

For odd $n$, let $p_{\min}$ be its smallest prime divisor. The normalized transition operator $K_n=A_n/\varphi(n)$ is self-adjoint in uniform $L^2$, and [\[eq:ramanujan\]](#eq:ramanujan){reference-type="eqref" reference="eq:ramanujan"} gives its eigenvalues $$\label{eq:normalized}
 \frac{c_n(r)}{\varphi(n)}=\frac{\mu(d)}{\varphi(d)}.$$ Among $d\mid n$, $d>1$, the largest nonzero modulus is $1/(p_{\min}-1)$.

[\[thm:mixing\]]{#thm:mixing label="thm:mixing"} Suppose $n$ is odd. For mean-zero real-valued functions $f,g$ on $\mathbb Z/n\mathbb Z$, $$\left|\mathbb E_{\mu_n}[f(x_0)g(x_k)]\right|
 \leq (p_{\min}-1)^{-k}
 \|f\|_{L^2(u_n)}\|g\|_{L^2(u_n)},$$ where $u_n$ is the uniform law. The exponential factor is sharp for every $k$: equality is attained by normalized real eigenfunctions whose associated divisor is $p_{\min}$.

On the orthogonal complement of constants, [\[eq:normalized\]](#eq:normalized){reference-type="eqref" reference="eq:normalized"} bounds the operator norm of $K_n^k$ by $(p_{\min}-1)^{-k}$. The Markov correlation is $\langle f,K_n^kg\rangle_{L^2(u_n)}$, so Cauchy--Schwarz gives the inequality. The divisor $p_{\min}$ occurs with multiplicity $\varphi(p_{\min})$ and has normalized eigenvalue $-1/(p_{\min}-1)$. The real or imaginary part of a nonzero Fourier eigenvector is a real eigenfunction; taking $f=g$ to be its normalization proves sharpness after the absolute value.

For even $n$, the eigenvalue $-1$ arising from $d=2$ is the spectral form of the parity obstruction in [\[prop:period\]](#prop:period){reference-type="ref" reference="prop:period"}; ordinary mixing cannot hold.

# Rigidity inside the family

Euler's totient is not injective, so entropy alone does not classify these shifts. The first nonzero periodic statistic repairs exactly that loss.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} If $X_m$ and $X_n$, with $m,n\geq2$, are topologically conjugate, then $m=n$. More precisely, the pair $$\left(h_{\mathrm{top}}(X_n),\#\operatorname{Fix}(\sigma^2)\right)
 =\left(\log\varphi(n),n\varphi(n)\right)$$ recovers $n$. Hence equality of the dynamical zeta functions also forces $m=n$ within this family.

Conjugacy preserves entropy and periodic-point counts. Equality of the entropies gives $\varphi(m)=\varphi(n)$. Equality of the two-period counts then gives $m\varphi(m)=n\varphi(n)$, hence $m=n$. If the zeta functions are equal, all periodic counts agree. Their exponential growth recovers the entropy of an irreducible finite-type shift. More precisely, Perron--Frobenius theory gives $$\limsup_{k\to\infty}P_k(n)^{1/k}=\varphi(n),$$ so the same argument applies even in the period-two case.

# Controls and ownership boundary

The deterministic control constructs $A_n$ directly, multiplies it over the integers, compares traces with [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}, checks the grouped Ramanujan characteristic polynomial, verifies parity/mixing witnesses, and tests the rigidity pair over a finite registry. These computations guard the divisor indexing and endpoints; the proofs establish the formulas for all $n$.

The adjacency spectrum, including its Ramanujan-sum expression, belongs to the unitary-Cayley-graph literature [@KlotzSander2007]. Rational zeta and trace identities for finite-type shifts belong to Bowen and Lanford [@BowenLanford1970]; the maximal-entropy Markov law is the Parry construction [@Parry1964]. Our residual claim is only the explicit symbolic-dynamical synthesis, the sharp odd-modulus correlation rate in this notation, and the two-statistic rigidity statement. No absolute novelty or priority claim is made.
