---
p1_kind: "derived-fulltext-reading-copy"
route: "logistic_dynamics"
logical_paper_id: "logistic_dynamics--coprime-0001-scalar-boundary"
canonical_tex: "logistic_dynamics/projects/coprime_0001_scalar_boundary/paper/main.tex"
canonical_pdf: "logistic_dynamics/projects/coprime_0001_scalar_boundary/paper/main.pdf"
source_sha256: "0249048d089c53376965cededd41648125394491c44429f07cf22296619a34a4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Scalar Continuation and the Endpoint Barrier for the COPRIME-0001 Renewal Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../logistic_dynamics/projects/coprime_0001_scalar_boundary>)
- [规范 TeX](<../../../../../logistic_dynamics/projects/coprime_0001_scalar_boundary/paper/main.tex>)
- [关联 PDF](<../../../../../logistic_dynamics/projects/coprime_0001_scalar_boundary/paper/main.pdf>)
- [支撑 Markdown](<../../../../../logistic_dynamics/projects/coprime_0001_scalar_boundary/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We continue the target-free audit of the countable coprime renewal suspension. The frozen transfer kernel is $$(L_s)_{mn}=\mathbf 1_{(m,n)=1}(mn)^{-s/2},\qquad m,n\ge2,$$ with determinant $D_{\mathrm{cop}}(s)=\operatorname{det}_{F}(I-L_s)$ initially defined on $\Re s>1$. A squarefree-divisor Sylvester lift produces an explicit Hilbert--Schmidt family $C_s=\zeta(s)T_s-P_1$, so $\operatorname{det}_{2}(I-C_s)$ is a scalar continuation on $\{\Re s>1/2\}\setminus\{1\}$ and agrees with $D_{\mathrm{cop}}$ on its defining half-plane. A separate min--max argument, using a temporary label-one completion, proves that infinitely many positive real zeros of $D_{\mathrm{cop}}$ approach $s=1$. Hence no holomorphic or meromorphic germ of the same scalar determinant crosses that endpoint. No zeros are computed, and no prime or Riemann-zero data enter the construction.
author:
- Anonymous Research Team
date: August 2026
title: |
  Scalar Continuation and the Endpoint Barrier\
  for the COPRIME-0001 Renewal Determinant
```

## Markdown 正文

# Introduction

The first COPRIME-0001 stage established a genuinely recurrent countable symbolic object and an exact Fredholm trace ledger on $\Re s>1$. The next question is narrower than a Riemann-zero comparison: can the scalar determinant itself cross the sharp operator boundary? This paper answers that question with a split result.

First, a divisor-coordinate factorization gives a controlled scalar continuation away from one distinguished endpoint. Second, the endpoint is not removable: the original determinant has infinitely many real zeros accumulating there. The two statements are compatible because the continuation is punctured and the auxiliary $\operatorname{det}_{2}$ expression is not identified with a bounded extension of the original $\ell^2$ matrix.

The audit is deliberately target-free. The gcd rule is retained as an intrinsic transition rule, while rational primes appear only as formal factorization coordinates in the proof. No prime table, zero table, determinant evaluation, or fitted normalization is consulted.

#### Contributions.

We prove an $S_2$-valued continuation representation on $\Re s>1/2$, prove equality with the original Fredholm determinant on $\Re s>1$, and establish the endpoint zero-accumulation obstruction at $s=1$. The resulting Route-A tuple is $$\begin{gathered}
\mathrm{A1\_WEAK},\quad \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
\mathrm{A3\_CONTROLLED\_CONTINUATION},\quad \mathrm{A4\_FAIL}.
\end{gathered}$$

# Frozen object and source lock

Let $$I=\{2,3,\ldots\},\qquad
 \Sigma_{\mathrm{cop}}=\{(n_k)_{k\in\mathbb Z}:n_k\in I,
                    \ (n_k,n_{k+1})=1\},$$ with roof $\tau(n_k)=\log n_0$. The symmetric half-roof transfer kernel is $$(L_s)_{mn}=\mathbf 1_{(m,n)=1}(mn)^{-s/2}.$$ The only determinant convention in the original source lock is $$D_{\mathrm{cop}}(s)=\operatorname{det}_{F}(I-L_s),\qquad \Re s>1.$$

The clock is the cyclic sum $\sum_i\log n_i$, and the normalization excludes label one. All finite checks use exact symbolic or rational arithmetic. Root searches and comparisons with the Riemann divisor are outside the lock.

The earlier trace-class result follows from $$\mathbf 1_{(m,n)=1}=\sum_{d\mid m,n}\mu(d),$$ and the same object is unbounded on the frozen counting-measure $\ell^2$ space when $\Re s\le1$. The latter is an operator statement; it does not, by itself, decide scalar continuation.

# Squarefree-divisor continuation

Let $\mathcal S$ be the squarefree positive integers and define $$V_s(m,d)=\mathbf 1_{d\mid m}m^{-s/2},
 \qquad M(d,d)=\mu(d).$$ On $\Re s>1$, $$L_s=V_s M V_s^{\mathsf T}.$$ The Gram matrix is $$(V_s^{\mathsf T}V_s)_{de}
 =\zeta(s)[d,e]^{-s}-\delta_{d=e=1}.$$ Therefore, with $P_1=e_1\otimes e_1$, $$C_s:=V_s^{\mathsf T}V_sM=\zeta(s)T_s-P_1,
 \qquad (T_s)_{de}=\mu(e)[d,e]^{-s}.$$ Sylvester's identity gives $$\operatorname{det}_{F}(I-L_s)=\operatorname{det}_{F}(I-C_s),\qquad \Re s>1.$$

Put $H_s(d,e)=[d,e]^{-s}$. Squarefree Euler factorization yields $$\|H_s\|_{S_2}^2
 =\sum_{d,e\in\mathcal S}[d,e]^{-2\Re s}
 =\prod_p(1+3p^{-2\Re s}).$$ Thus $T_s=H_sM$ is a locally holomorphic Hilbert--Schmidt family for $\Re s>1/2$. On $$\Omega=\{s\in\mathbb C:\Re s>1/2,\ s\ne1\}$$ define $$\widetilde D(s)=\operatorname{det}_{2}(I-C_s).$$ For $\Re s>1$, $C_s$ is trace class and $$\operatorname{Tr}C_s=\zeta(s)\sum_{d\in\mathcal S}\mu(d)d^{-s}-1=0.$$ Since $\operatorname{det}_{2}(I-C)=\operatorname{det}_{F}(I-C)e^{\operatorname{Tr}C}$, we obtain $$\widetilde D(s)=D_{\mathrm{cop}}(s),\qquad \Re s>1.$$

The continuation is a scalar identity. It does not say that the original matrix $L_s$ is bounded, compact, or trace class below its defining half-plane. The $\operatorname{det}_{2}$ representation is kept as a separately named ledger throughout.

# The endpoint at one

We now temporarily add label one and write $$(K_s)_{mn}=\mathbf 1_{(m,n)=1}(mn)^{-s/2},qquad m,n\ge1.$$ For real $s>1$, this is compact self-adjoint, and $L_s$ is its codimension-one compression to $e_1^\perp$.

For a prime coordinate $p$, set $q=p^{-s}$. On the exponent space $\ell^2(\mathbb N_0)$, the local kernel has rank two and nonzero eigenvalues $$\alpha_p^\pm(s)=\frac{1\pm\sqrt{(1+3q)/(1-q)}}2.$$ For a finite coordinate set $P$, tensoring the local blocks gives the nonzero eigenvalues $$\Lambda_{S,P}(s)=\left(\prod_{p\in P}\alpha_p^+(s)\right)
 \prod_{p\in S}\rho_p(s),
 \qquad \rho_p=\alpha_p^-/\alpha_p^+.$$ Even-cardinality $S$ give positive values. The inequality $$\frac{1+3q}{1-q}-(1+2q)^2=\frac{4q^3}{1-q}\ge0$$ implies $\alpha_p^+(s)\ge1+p^{-s}$. Hence Euler's product forces the positive top product to diverge as $s\downarrow1$. Choosing arbitrarily many fixed even sets and then a sufficiently large finite $P$, min--max gives, for every fixed $M$, $$\lambda_M^+(L_s)\longrightarrow+\infty,qquad s\downarrow1.$$

At the safe point $s=3$, the initial trace-class estimate gives $$\|L_3\|\le\frac{\zeta(3)^2}{\zeta(6)}-1
 <\left(\frac54\right)^2-1=\frac9{16}<1.$$ The ordered positive eigenvalues are continuous for $s>1$. For every $\varepsilon>0$, compactness of $L_{1+\varepsilon}$ makes $\lambda_M^+(L_{1+\varepsilon})$ small for large $M$, while the preceding limit makes it exceed one near the endpoint. The intermediate value theorem therefore supplies level-one crossings inside $(1,1+\varepsilon)$. Since the eigenvalue one has finite multiplicity for a compact operator, these crossings yield distinct zeros $s_j\downarrow1$ of $D_{\mathrm{cop}}$.

The scalar determinant $D_{\mathrm{cop}}$ has no holomorphic or meromorphic germ through $s=1$.

Indeed, a meromorphic germ has only a finite-order pole. Multiplying by a finite power of $s-1$ would produce a holomorphic function with zeros accumulating at an interior point, forcing it to vanish identically. This contradicts $D_{\mathrm{cop}}(3)\ne0$.

# Route-A interpretation

The analytic tuple is $$\begin{gathered}
\mathrm{A1\_WEAK},\quad \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
\mathrm{A3\_CONTROLLED\_CONTINUATION},\quad \mathrm{A4\_FAIL}.
\end{gathered}$$ The first two entries record the intrinsic recurrent object and its trace-class determinant; the third records only the punctured scalar domain $\Re s>1/2$, $s\ne1$. For the completed-Riemann target the tuple remains $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$

The gcd rule has not produced a prime-to-orbit correspondence or a von-Mangoldt repetition amplitude. There is no functional equation, Gamma or trivial-zero ledger, $T\log T$ divisor theorem, or natural quantization. Route B is therefore not authorized. The scoped audit is `STOP_SCOPED`, with the endpoint accumulation registered as a reusable obstruction.

# Reproducibility and data firewall

The project source lock fixes the object, clock, normalization, determinant conventions, and stopping conditions. The generator emits a deterministic JSON certificate containing the local-factor, Sylvester, and endpoint logic. The certificate uses no prime enumeration, zero table, determinant value, or floating-point root calculation.

From the project directory:

    PYTHONPATH=. python3 experiments/coprime_0001_scalar_boundary.py --quiet \
      --output artifacts/coprime_0001/scalar_boundary_certificate.json
    PYTHONPATH=. python3 -m unittest -v tests/test_coprime_0001_scalar_boundary.py
    sha256sum -c results/ARTIFACT_HASHES.sha256

The focused test suite checks source-lock/evaluation parity, the symbolic Euler-factor identities, the continuation domain, the endpoint barrier, the data firewall, and byte-identical certificate regeneration.

# Proof details

For completeness, the local rank-two calculation uses the normalized vector $$u_q=\frac{(0,q^{1/2},q,q^{3/2},\ldots)}{\sqrt{q/(1-q)}}.$$ In the basis $\{e_0,u_q\}$, the local block is $$\begin{pmatrix}1&\sqrt{q/(1-q)}\\
 \sqrt{q/(1-q)}&0\end{pmatrix},$$ whose characteristic polynomial is $\lambda^2-\lambda-q/(1-q)$.

The squarefree Hilbert--Schmidt product follows by choosing, for each prime, whether the exponent occurs in neither coordinate, the first coordinate, the second coordinate, or both. The last three choices all contribute $p^{-2\Re s}$, giving the local factor $1+3p^{-2\Re s}$.

Finally, $\zeta(3)<5/4$ follows from $$\zeta(3)=1+2^{-3}+\sum_{n\ge3}n^{-3}<1+\frac18+\int_2^\infty x^{-3}\,dx=\frac54.$$ This yields the safe norm margin at $s=3$ used in the spectral-flow argument.
