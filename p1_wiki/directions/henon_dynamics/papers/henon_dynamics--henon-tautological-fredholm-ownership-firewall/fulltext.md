---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-tautological-fredholm-ownership-firewall"
canonical_tex: "henon_dynamics/henon_tautological_fredholm_ownership_firewall/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_tautological_fredholm_ownership_firewall/paper/paper.pdf"
source_sha256: "f90d9c50f62908ec3f4e74024c44098171b2c526eefe9946e413cda0e13affbe"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Fredholm Ownership Firewall for the Weighted Hénon Reflection Euler Family

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_tautological_fredholm_ownership_firewall>)
- [规范 TeX](<../../../../../henon_dynamics/henon_tautological_fredholm_ownership_firewall/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_tautological_fredholm_ownership_firewall/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_tautological_fredholm_ownership_firewall/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_tautological_fredholm_ownership_firewall/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The weighted reflection Euler family of the full Hénon horseshoe has an explicit punctured scalar continuation. We ask whether a Fredholm determinant representation gives that continuation meaningful operator ownership. Its logarithmic channels can indeed be placed on the diagonal of a locally trace-class holomorphic family $A(z,q)$, and $\det_{\mathrm F}(\exp A)=\exp(\operatorname{Tr}A)$ recovers the continuation exactly. This realization is nevertheless tautological: every nonvanishing holomorphic scalar $F$ satisfies $F=\det_{\mathrm F}(I+(F-1)P)$ for a fixed rank-one projection $P$. In the opposite direction, each primitive source word owns a finite weighted cyclic block $B_\omega$ with $\det(I-zB_\omega)=1-z^nq^{S_n\chi(\omega)}$. This is the P70 Euler denominator, whose reciprocal is the corresponding Euler factor. Its singular values are the physical edge weights in $\{1,q\}$. Primitive singleton reflection words at every odd length therefore put a uniform positive singular-value floor in the undamped full orbit-block direct sum. That sum is bounded but noncompact, belongs to no finite Schatten ideal, and has no ordinary trace-class Fredholm determinant. The comparison furnishes a claim firewall: analytic determinant realization is proved but tautological, finite source blocks are exact, and a genuine source-derived transfer owner remains open.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 16, 2026'
title: |
  A Fredholm Ownership Firewall for the\
  Weighted Hénon Reflection Euler Family
```

## Markdown 正文

# The operator question after scalar continuation

The Hénon horseshoe admits a full-shift model in the hyperbolic regime relevant here [@DevaneyNitecki1979; @Arai2007]. Previous steps of the present programme associated to its marked reflection packets the weighted channel expansion $$\label{eq:channel-expansion}
 \mathcal L(z,q)=\sum_{m\geq1}h_m(z,q),\qquad
 h_m(z,q)=c_m\frac{2(qz)^m}
 {1-(1+q^{2m})z^{2m}},$$ where $$\label{eq:coefficient}
 c_m=\frac1m\prod_{\substack{p\mid m\\p\ \mathrm{odd}}}(1-p),
 \qquad 0<|c_m|\leq1.$$ For fixed $q>0$, put $$\begin{aligned}
 L(q)&=\min(1,q^{-1}),\\
 \rho_m(q)&=(1+q^{2m})^{-1/(2m)},\\
 \Sigma_q&=\{\rho_m(q)e^{\pi i k/m}:m\geq1,\ 0\leq k<2m\},\\
 \Omega_q&=\{z:|z|<L(q)\}\setminus\Sigma_q.\end{aligned}$$ The preceding scalar theory proves that [\[eq:channel-expansion\]](#eq:channel-expansion){reference-type="eqref" reference="eq:channel-expansion"} converges normally on compact subsets of $\Omega_q$ and defines the nonvanishing continuation $$\label{eq:zch}
 \mathcal Z_{\mathrm{ch}}(z,q)=\exp \mathcal L(z,q).$$ It also classifies the limiting circle; we do not revisit or cross that boundary. Instead we distinguish two questions:

1.  Can the known scalar [\[eq:zch\]](#eq:zch){reference-type="eqref" reference="eq:zch"} be represented by a legitimate trace-class Fredholm determinant?

2.  Does an operator built independently from the source dynamics own the same determinant?

The first answer is yes. The second is not implied by the first.

# A locally trace-class channel realization

Let $(e_m)_{m\geq1}$ be the standard basis of $\ell^2(\mathbb N)$ and let $P_m$ project onto $\mathbb C e_m$. Define $$\label{eq:A}
 A(z,q)=\sum_{m\geq1}h_m(z,q)P_m
       =\operatorname{diag}(h_1(z,q),h_2(z,q),\ldots).$$

[\[thm:channel\]]{#thm:channel label="thm:channel"} For every fixed $q>0$, $A:\Omega_q\to\mathcal S_1$ is holomorphic in trace norm. The family $$K_{\mathrm{ch}}(z,q)=\exp A(z,q)-I$$ is likewise trace-class holomorphic, and $$\label{eq:channel-det}
 \det_{\mathrm F}(I+K_{\mathrm{ch}}(z,q))
 =\exp(\operatorname{Tr}A(z,q))
 =\mathcal Z_{\mathrm{ch}}(z,q).$$

Let $C\Subset\Omega_q$. Choose $r<L(q)$ such that $|z|\leq r$ on $C$. Then $r<1$ and $qr<1$. All finitely many early denominators in [\[eq:channel-expansion\]](#eq:channel-expansion){reference-type="eqref" reference="eq:channel-expansion"} are uniformly separated from zero on $C$. For all sufficiently large $m$ and all $z\in C$, $$\left|1-(1+q^{2m})z^{2m}\right|
 \geq1-r^{2m}-(qr)^{2m}\geq\frac12.$$ Using [\[eq:coefficient\]](#eq:coefficient){reference-type="eqref" reference="eq:coefficient"}, $$\label{eq:tail}
 \sup_{z\in C}|h_m(z,q)|\leq4(qr)^m$$ for the same tail. Thus $\sum_m h_mP_m$ converges locally uniformly in $\mathcal S_1$, since the trace norm of a diagonal operator is the sum of the absolute diagonal entries. The Banach-valued Weierstrass theorem gives trace-norm holomorphy, and $\operatorname{Tr}A=\sum_mh_m=\mathcal L$.

The exponential remains in $I+\mathcal S_1$. More explicitly, for the diagonal tail, $$|e^{h_m}-1|\leq e^{|h_m|}|h_m|,$$ so [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} again gives locally uniform trace-norm convergence. The standard trace-ideal identity $\det_{\mathrm F}(e^A)=e^{\operatorname{Tr}A}$ [@Simon2005] now yields [\[eq:channel-det\]](#eq:channel-det){reference-type="eqref" reference="eq:channel-det"}.

This theorem is an exact analytic statement. It is not yet a test of dynamical provenance, because the entries of $A$ were read from the already completed scalar logarithm.

# The universal rank-one firewall

[\[lem:rankone\]]{#lem:rankone label="lem:rankone"} Let $U\subset\mathbb C$ be a domain, let $F$ be a nonvanishing holomorphic function on $U$, and let $P$ be a fixed rank-one orthogonal projection on an arbitrary Hilbert space. Then $$K_F(z)=(F(z)-1)P$$ is trace-class holomorphic and $$\label{eq:rankone}
 \det_{\mathrm F}(I+K_F(z))=F(z),\qquad z\in U.$$

Scalar multiplication makes $K_F$ holomorphic in trace norm. It has one possibly nonzero eigenvalue, $F(z)-1$. The finite-rank definition of the Fredholm determinant therefore gives $\det_{\mathrm F}(I+K_F)=1+(F-1)=F$.

is deliberately elementary. It shows that the bare existence of a parameter-dependent trace-class family with determinant $F$ is universal and therefore cannot, by itself, identify a transfer mechanism, periodic-point trace, or dynamically selected state space. We call such a construction a *scalar-built realization*. A genuine source owner would have to be specified from the dynamics independently of the already known $F$ and then derive $F$ as a consequence. In this sense is `PROVED_TAUTOLOGICAL`: correct and useful for analysis, but insufficient as an ownership theorem.

# Finite source-native cyclic blocks

The literal source construction has more provenance. Let $\omega$ be a primitive marked reflection word of odd length $n$. Write $$\chi_j=\chi(\sigma^j\omega)\in\{0,1\},\qquad
 S(\omega)=\sum_{j=0}^{n-1}\chi_j.$$ On $\mathbb C^n$, with indices read modulo $n$, set $$\label{eq:block}
 B_\omega e_j=q^{\chi_j}e_{j+1}.$$ These are the physical edge weights; no period damping has been inserted.

[\[prop:block\]]{#prop:block label="prop:block"} For every $q>0$ and every such $\omega$, $$\begin{aligned}
 B_\omega^n&=q^{S(\omega)}I,\label{eq:turn}\\
 \det(I-zB_\omega)&=1-z^nq^{S(\omega)},\label{eq:block-det}\end{aligned}$$ and the singular values of $B_\omega$ are precisely the multiset $\{q^{\chi_0},\ldots,q^{\chi_{n-1}}\}\subset\{1,q\}$. Consequently $$\label{eq:block-bounds}
 \min(1,q)\|x\|\leq\|B_\omega x\|
 \leq\max(1,q)\|x\|.$$

After one full cycle, every $e_j$ has acquired every edge weight once, which proves [\[eq:turn\]](#eq:turn){reference-type="eqref" reference="eq:turn"}. Moreover $e_0,B_\omega e_0,\ldots,B_\omega^{n-1}e_0$ are nonzero multiples of the standard basis, so $e_0$ is cyclic. Hence the minimal polynomial has degree $n$; by [\[eq:turn\]](#eq:turn){reference-type="eqref" reference="eq:turn"} it is $\lambda^n-q^{S(\omega)}$, which is also the characteristic polynomial. Substitution gives [\[eq:block-det\]](#eq:block-det){reference-type="eqref" reference="eq:block-det"}. Finally, $$B_\omega^*B_\omega e_j=q^{2\chi_j}e_j.$$ Taking positive square roots proves the singular-value statement and [\[eq:block-bounds\]](#eq:block-bounds){reference-type="eqref" reference="eq:block-bounds"}.

Thus every finite Euler denominator has an exact source-native owner, and the corresponding P70 Euler factor is the reciprocal determinant $\det(I-zB_\omega)^{-1}$. The issue is whether all of these blocks are summable in a determinant class.

# The full source sum is not compact

For every odd $n\geq3$, let $\omega_n=(1,0,\ldots,0)$ with the singleton at the chosen reflection center. Reflection fixes $\omega_n$. It is primitive: repetition of a shorter word would create more than one symbol equal to $1$. Exactly the two sites adjacent to the singleton have unequal distance-two neighbours, so $$\label{eq:singleton-energy}
 S(\omega_n)=n-2.$$

Let $\mathfrak R$ be the countable collection of physical primitive marked reflection words and form the Hilbert direct sum $$\label{eq:direct-sum}
 \mathcal H=\bigoplus_{\omega\in\mathfrak R}\mathbb C^{|\omega|},
 \qquad B_q=\bigoplus_{\omega\in\mathfrak R}B_\omega.$$

[\[thm:obstruction\]]{#thm:obstruction label="thm:obstruction"} For every $q>0$, $B_q$ is bounded and noncompact. It belongs to no Schatten class $\mathcal S_p$ with $0<p<\infty$. In particular, for $z\ne0$ the expression $\det_{\mathrm F}(I-zB_q)$ is not an ordinary trace-class Fredholm determinant.

The uniform bounds [\[eq:block-bounds\]](#eq:block-bounds){reference-type="eqref" reference="eq:block-bounds"} pass to the Hilbert direct sum: $$\min(1,q)\|x\|\leq\|B_qx\|\leq\max(1,q)\|x\|.$$ Choose one unit basis vector $u_n$ from each singleton block. The vectors $u_n$ are orthonormal, their images lie in mutually orthogonal blocks, and $\|B_qu_n\|\geq\min(1,q)>0$. Hence $(B_qu_n)$ has no convergent subsequence, so $B_q$ is not compact. Every finite Schatten class is contained in the compact operators. Thus $B_q\notin\mathcal S_p$ for every finite $p$; in particular $zB_q\notin\mathcal S_1$ when $z\ne0$, which excludes the ordinary trace-class determinant.

The theorem concerns the literal undamped source blocks. It does not refute every conceivable transfer operator. It says that compactness or nuclearity must come from additional source-derived structure, rather than from taking the naive full direct sum.

# A graded ledger is not an operator trace

There is a useful but dangerous remnant of trace combinatorics. From the cyclic shift action, $$\label{eq:ledger}
 \sum_{j=0}^{n-1}\langle e_j,B_\omega^re_j\rangle=
 \begin{cases}
 0,&n\nmid r,\\
 nq^{(r/n)S(\omega)},&n\mid r.
 \end{cases}$$ For fixed $r$, only the finitely many lengths $n\mid r$ contribute, and there are finitely many binary source words at each such length. Therefore [\[eq:ledger\]](#eq:ledger){reference-type="eqref" reference="eq:ledger"} reproduces a locally finite coefficient ledger after summing over blocks.

This does not contradict . The left side of [\[eq:ledger\]](#eq:ledger){reference-type="eqref" reference="eq:ledger"} is a finite-block diagonal sum; its aggregate is tied to the canonical block basis. Since $B_q^r$ is still bounded below and noncompact, it is not trace class. The aggregate cannot be promoted to a basis-independent Hilbert-space trace or used in the Fredholm trace expansion. We retain it only as a formal graded identity.

# Executable certificate and claim boundary

The accompanying standard-library certificate performs exact rational Gaussian elimination on finite cyclic blocks, verifies representative weighted full turns, compares channel trace exponentials with products of diagonal exponentials, and tests unrelated rank-one realizations. A second program reconstructs the formulas without importing the primary module. Normal and optimized unit-test runs enforce the same schema, and mutation tests reject promotions of the operator and arithmetic claims. These computations audit finite identities; the local trace-norm and noncompactness arguments remain the proofs.

  Claim                                   Status
  --------------------------------------- -----------------------
  Punctured analytic determinant          `PROVED_TAUTOLOGICAL`
  Universal rank-one firewall             `PROVED`
  Finite source cyclic blocks             `PROVED`
  Full source direct sum trace class      `REFUTED`
  Genuine source-derived transfer owner   `OPEN`
  Arithmetic trace or Route B             `NO / NOT AUTHORIZED`

No rational-prime semantics, von Mangoldt trace, self-adjoint Hilbert--Pólya operator, or arithmetic advance follows. The constructive next question is precise: find a dynamically forced state space and a source-derived compactness mechanism whose genuine operator traces produce the weighted channels without inserting the completed scalar function.
