---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-abel-graded-all-orbit-packet-germ"
canonical_tex: "henon_dynamics/henon_abel_graded_all_orbit_packet_germ/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_abel_graded_all_orbit_packet_germ/paper/paper.pdf"
source_sha256: "97dff8ca519f7759248a78931394f09d7b5355d7e549bc525a953a0c46a5c4bb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Abel-Graded All-Orbit Prime-Ideal Packet Germs for a Hénon Survivor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_abel_graded_all_orbit_packet_germ>)
- [规范 TeX](<../../../../../henon_dynamics/henon_abel_graded_all_orbit_packet_germ/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_abel_graded_all_orbit_packet_germ/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_abel_graded_all_orbit_packet_germ/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_abel_graded_all_orbit_packet_germ/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct an all-primitive-orbit arithmetic packet germ for a certified area-preserving Hénon survivor. For a primitive orbit $\gamma$ and cyclotomic index $n>2$, the inversion-fixed value $\beta_{\gamma,n}=\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma)$ is an algebraic integer in the trace field. Its prime-ideal divisor is placed in a universal weighted tagged $\ell^1$ space retaining the orbit, index, and prime ideal. A uniform conjugate-height estimate, the exact four-state orbit census, and pressure expansion imply that the two-variable series $$\mathcal G(s,u)=\sum_{\gamma\ {\rm primitive}}
  e^{-s h_*\log|\Lambda_\gamma|}
  \sum_{n\ge3}u^n\mathop{\mathrm{Div}}(\beta_{\gamma,n})$$ is normally convergent and Banach-valued holomorphic for $$|u|<1,\qquad
  \Re s>\frac{\log(2\varphi)}{h_*\log J_*}.$$ The certified safe half-plane is $\Re s>3.125206884004\ldots$. Residue-degree norm pushforward extends as a norm-one map to the rational-prime divisor space. The Abel grading is necessary: Flatters' quadratic primitive-divisor theorem forces the packet norm on one exact period-four orbit to be at least $\log2$ for every $n>12$. Its $u$-radius is exactly one and the raw value $u=1$ diverges. Thus an all-orbit analytic germ is proved, while any ungraded zeta, von-Mangoldt law, determinant, or operator remains open.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
bibliography:
- references.bib
date: 'Preprint, August 2026'
title: |
  Abel-Graded All-Orbit Prime-Ideal Packet Germs\
  for a Hénon Survivor
```

## Markdown 正文

# Introduction

Periodic-orbit methods naturally produce products or traces indexed by primitive closed orbits. Arithmetic interpretations are substantially more rigid: a local label must retain its field, multiplicity, repetition law, and global convergence. In the Hénon pressure/orbit program considered here, exact multiplier labels are algebraic units rather than rational primes. Cyclotomic resultants survive this obstruction, but full multiplier-field norms count reciprocal roots twice and become squares. The smallest source-native arithmetic objects are therefore inversion-fixed cyclotomic values in orbit-dependent trace fields and their prime-ideal divisors.

A previous finite certificate assembled these divisors with complete tags and proved that rational norm pushforward is noninjective. The open question was whether packets from *all* primitive orbits and all cyclotomic indices can coexist in one topology. This paper answers that question in a deliberately local analytic domain.

Our first contribution is a universal weighted tagged $\ell^1$ space. Its basis records $(\gamma,n,\mathfrak q)$ and its weight is the logarithm of the prime-ideal norm. Thus each packet has norm exactly equal to the logarithm of its absolute field norm. The varying number fields no longer need to be embedded in one common field.

The second contribution is an all-orbit convergence theorem. Three independent growth mechanisms must be paid: $$\text{symbolic orbits } \varphi^m,\qquad
\text{field degree }2^m,\qquad
\text{packet height }O(nm).$$ Pressure length gives exponential decay in $m$, while an Abel variable $u^n$ pays the cyclotomic index. The resulting domain is explicit and nonempty. Omitting the degree factor would give an invalid larger half-plane; our executable checker rejects precisely that mutation.

The third contribution is a boundary theorem. The Abel variable is not a technical convenience that may be deleted after convergence. On one exact period-four orbit, Flatters' theorem [@flatters2009] supplies a new rational divisor at every index after twelve. The packet terms therefore do not tend to zero at $|u|=1$.

Cyclic-resultant theory [@hillar2005], primitive-divisor theory [@flatters2009; @bhv2001], and prime-orbit asymptotics [@parrypollicott1983] provide important neighboring structures. None of those sources proves the all-orbit tagged theorem below. The proof instead combines previously certified H6 interfaces with a new uniform height estimate.

#### Claim boundary.

We prove a Banach-valued analytic germ and a continuous norm pushforward. We do not prove analytic continuation, a boundary value at $u=1$, a functional equation, a von-Mangoldt identity, a Fredholm determinant, or a self-adjoint operator.

# The source object and the universal tagged space

Consider $$H_6(q,p)=(1-6q^2-p,q)$$ on the certified four-rectangle survivor. Its symbolic adjacency matrix is $$A=\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.$$ Let $\gamma$ be a primitive orbit, $m=m(\gamma)$ its symbolic period, $M_\gamma\in SL_2$ its chronological return derivative, and $\lambda_\gamma$ its signed unstable multiplier. Define the positive unstable modulus $\Lambda_\gamma=|\lambda_\gamma|>1$ and $$t_\gamma=\lambda_\gamma+\lambda_\gamma^{-1},
\qquad F_\gamma=\mathbb Q(t_\gamma).$$ The all-period integral-monodromy theorem and reciprocal cyclotomic factorization imply that, for every $n>2$ (so $\varphi(n)$ is even), $$\beta_{\gamma,n}
=\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma)
\in\mathcal O_{F_\gamma}.
\tag{2.1}$$ This element is nonzero because the unstable multiplier is not a root of unity.

Let $\mathscr A$ be the set of triples $(\gamma,n,\mathfrak q)$ where $\gamma$ is primitive, $n>2$, and $\mathfrak q$ is a nonzero prime ideal of $\mathcal O_{F_\gamma}$. If $\mathfrak q\mid p$ has residue degree $f_{\mathfrak q}$, set $$w(\gamma,n,\mathfrak q)=f_{\mathfrak q}\log p$$ and define $$\mathcal B_{\mathrm{tag}}=\ell^1(\mathscr A,w).
\tag{2.2}$$

For a nonzero packet define its effective tagged divisor $$D_{\gamma,n}
=\sum_{\mathfrak q}
v_{\mathfrak q}(\beta_{\gamma,n})[\gamma,n,\mathfrak q].
\tag{2.3}$$

[\[prop:packet-norm\]]{#prop:packet-norm label="prop:packet-norm"} Every $D_{\gamma,n}$ lies in $\mathcal B_{\mathrm{tag}}$ and $$\|D_{\gamma,n}\|_{\rm tag}
=\log\left|\mathop{\mathrm{N}}_{F_\gamma/\mathbb Q}\beta_{\gamma,n}\right|.
\tag{2.4}$$

The divisor has finite support because $\beta_{\gamma,n}$ is a nonzero algebraic integer. The standard ideal factorization $\mathop{\mathrm{N}}\mathfrak q=p^{f_{\mathfrak q}}$ gives $$\log|\mathop{\mathrm{N}}(\beta_{\gamma,n})|
=\sum_{\mathfrak q}v_{\mathfrak q}(\beta_{\gamma,n})
\log\mathop{\mathrm{N}}\mathfrak q,$$ which is exactly (2.4).

The topology is intentionally tagged. Distinct orbits, indices, or prime ideals remain distinct even when they lie above the same rational prime. This is what makes a common space possible without pretending that the varying trace fields are canonically one field.

# A uniform all-period packet-height envelope

The convergence proof needs a bound uniform in both the orbit and its number field. Set $x_i=6q_i$ along a period-$m$ fixed point. The cyclic fixed equations are $$x_i^2+x_{i-1}+x_{i+1}-6=0.
\tag{3.1}$$ They are monic and their fixed algebra is finite free over $\mathbb Z$ of rank $2^m$.

[\[lem:height\]]{#lem:height label="lem:height"} For every complex conjugate fixed point, $$\max_i|x_i|\le1+\sqrt7.
\tag{3.2}$$ Writing $C_0=3+2\sqrt7$, every conjugate return trace satisfies $$|\sigma(t_\gamma)|\le2C_0^m.
\tag{3.3}$$

Choose $j$ with $M=|x_j|=\max_i|x_i|$. Equation (3.1) gives $$M^2\le6+|x_{j-1}|+|x_{j+1}|\le6+2M,$$ so $M\le1+\sqrt7$. Each chronological derivative step is $$J_i=\begin{pmatrix}-2x_i&-1\\1&0\end{pmatrix},$$ and hence $\|J_i\|_\infty\le3+2\sqrt7=C_0$. Submultiplicativity and $|\mathop{\mathrm{tr}}M|\le2\|M\|_\infty$ prove (3.3).

[\[lem:packet-envelope\]]{#lem:packet-envelope label="lem:packet-envelope"} For a primitive period-$m$ orbit and every $n>2$, $$\log\left|\mathop{\mathrm{N}}_{F_\gamma/\mathbb Q}\beta_{\gamma,n}\right|
\le2^m n\left(\log(2\sqrt3)+\frac m2\log C_0\right).
\tag{3.4}$$

Because $F_\gamma$ is generated by a function on the rank-$2^m$ fixed algebra, $$[F_\gamma:\mathbb Q]\le2^m.
\tag{3.5}$$ The trace field lies in the residue field of the selected geometric fixed point. Every embedding $\sigma:F_\gamma\hookrightarrow\mathbb C$ extends to that residue field, and the fixed equations are preserved under this extension. Thus Lemma [\[lem:height\]](#lem:height){reference-type="ref" reference="lem:height"} applies to every conjugate trace. Extend $\sigma$ further to the multiplier field. Of the two reciprocal roots of $z^2-\sigma(t_\gamma)z+1$, choose $\mu$ with $|\mu|\ge1$. Lemma [\[lem:height\]](#lem:height){reference-type="ref" reference="lem:height"} and the Cauchy root bound give $$|\mu|\le1+|\sigma(t_\gamma)|\le3C_0^m.
\tag{3.6}$$ Using the product over primitive $n$th roots of unity, $$\begin{aligned}
|\sigma(\beta_{\gamma,n})|
&=|\mu|^{-\varphi(n)/2}|\Phi_n(\mu)|\\
&\le\left(\sqrt{|\mu|}+|\mu|^{-1/2}\right)^{\varphi(n)}\\
&\le\left(2\sqrt3\,C_0^{m/2}\right)^n.
\end{aligned}
\tag{3.7}$$ Multiplication over at most $2^m$ embeddings proves (3.4).

The factor $2^m$ is not an artifact of the certificate. It is the source-native degree cap needed to compare norms in varying trace fields. Deleting it replaces the true outer ratio $2\varphi e^{-\sigma h_*\log
J_*}$ by a false smaller ratio.

# The all-orbit Abel-graded germ

The marked period-$m$ count is $$N_m=\mathop{\mathrm{tr}}(A^m)
=\varphi^m+(-\varphi^{-1})^m+i^m+(-i)^m.
\tag{4.1}$$ In particular, $N_m\le3\varphi^m$ for $m\ge1$. This also bounds the number of primitive period-$m$ orbits.

Let $h_*$ be the certified pressure root and let $$\widehat\ell_\gamma=h_*\log|\Lambda_\gamma|
\tag{4.2}$$ be the pressure-normalized length. Uniform expansion on the survivor gives $$\widehat\ell_\gamma\ge h_*m(\gamma)\log J_*,
\qquad J_*=\frac{\sqrt{17}+\sqrt{13}}2.
\tag{4.3}$$

[\[thm:germ\]]{#thm:germ label="thm:germ"} The series $$\mathcal G(s,u)=
\sum_{\gamma\ {\rm primitive}}e^{-s\widehat\ell_\gamma}
\sum_{n\ge3}u^nD_{\gamma,n}
\tag{4.4}$$ converges absolutely in $\mathcal B_{\mathrm{tag}}$, locally uniformly, and defines a jointly holomorphic $\mathcal B_{\mathrm{tag}}$-valued function on $$|u|<1,\qquad
\Re s>\frac{\log(2\varphi)}{h_*\log J_*}.
\tag{4.5}$$ The certified source-only subdomain is $$|u|<1,\qquad \Re s>3.125206884004728\ldots .
\tag{4.6}$$

Put $r=|u|$, $\sigma=\Re s$, $a=\log(2\sqrt3)$, and $b=\frac12\log C_0$. Proposition [\[prop:packet-norm\]](#prop:packet-norm){reference-type="ref" reference="prop:packet-norm"}, Lemma [\[lem:packet-envelope\]](#lem:packet-envelope){reference-type="ref" reference="lem:packet-envelope"}, and (4.1)--(4.3) give $$\begin{aligned}
\|\mathcal G(s,u)\|_{\rm tag}
&\le3\sum_{m\ge1}\varphi^m e^{-\sigma h_*m\log J_*}
2^m(a+bm)\sum_{n\ge3}nr^n\\
&\le\frac{3r}{(1-r)^2}
\sum_{m\ge1}(a+bm)
\left(2\varphi e^{-\sigma h_*\log J_*}\right)^m.
\end{aligned}
\tag{4.7}$$ The final series converges if the ratio in parentheses is less than one, which is (4.5). On every compact subset of that domain, $r$ stays below one and the outer ratio stays uniformly below one. The Weierstrass theorem for Banach-valued series therefore proves joint holomorphy.

The pressure certificate gives $h_*\ge0.277980$. Replacing $h_*$ by this lower bound in (4.5) gives $$\frac{\log(2\varphi)}{0.277980\log J_*}
=3.125206884004728\ldots ,$$ which proves (4.6).

Figure [1](#fig:domain){reference-type="ref" reference="fig:domain"} displays the certified outer contraction and the independent one-orbit boundary lower bound proved in Section [6](#sec:boundary){reference-type="ref" reference="sec:boundary"}.

![Left: the source-locked all-orbit geometric ratio and its certified threshold. Right: the primitive-divisor lower bound for one period-four orbit. The data are generated directly from the compact certificate.](<../../../../../henon_dynamics/henon_abel_graded_all_orbit_packet_germ/figures/abel_pressure_domain.pdf>){#fig:domain width="\\textwidth"}

# Continuous rational norm pushforward

Let $$\mathcal B_{\mathrm{rat}}=\ell^1(\{p:p\text{ rational prime}\},\log p).
\tag{5.1}$$ On tagged basis vectors define $$\nu[\gamma,n,\mathfrak q]=f_{\mathfrak q}[p],
\qquad \mathfrak q\mid p.
\tag{5.2}$$

[\[prop:pushforward\]]{#prop:pushforward label="prop:pushforward"} The map $\nu$ extends uniquely to a bounded linear map $\nu:\mathcal B_{\mathrm{tag}}\to\mathcal B_{\mathrm{rat}}$ with $\|\nu\|=1$. For every packet, $$\|\nu D_{\gamma,n}\|_{\rm rat}
=\|D_{\gamma,n}\|_{\rm tag}.
\tag{5.3}$$ Consequently $\nu\mathcal G(s,u)$ is obtained by termwise pushforward in the domain of Theorem [\[thm:germ\]](#thm:germ){reference-type="ref" reference="thm:germ"}.

For finitely supported complex coefficients, $$\begin{aligned}
\|\nu c\|_{\rm rat}
&=\sum_p\left|
\sum_{\substack{\gamma,n,\mathfrak q\\\mathfrak q\mid p}}
f_{\mathfrak q}c_{\gamma,n,\mathfrak q}\right|\log p\\
&\le\sum_{\gamma,n,\mathfrak q}
|c_{\gamma,n,\mathfrak q}|f_{\mathfrak q}\log p
=\|c\|_{\rm tag}.
\end{aligned}$$ Thus $\nu$ extends with norm at most one. Equality on every basis vector shows that the norm is one. Packet coefficients are nonnegative, so the triangle inequality is an equality and (5.3) follows. Continuity and the normal convergence of Theorem [\[thm:germ\]](#thm:germ){reference-type="ref" reference="thm:germ"} justify termwise application.

The proposition solves the topology problem without solving the information problem. The finite tagged certificate already has nontrivial kernel after rational pushforward: several orbit/index/prime-ideal atoms can map to the same rational-prime basis vector. Therefore (5.3) is not an injectivity statement and does not define a rational-prime clock orbit by orbit.

# The Abel boundary is a genuine obstruction {#sec:boundary}

Consider the exact primitive period-four multiplier $$L_4=289+24\sqrt{145}.
\tag{6.1}$$ It is a positive unit of norm one in $\mathbb Q(\sqrt{145})$. Its inversion-fixed trace is $L_4+L_4^{-1}=578$, so every packet $$\beta_{4,n}=L_4^{-\varphi(n)/2}\Phi_n(L_4)
\tag{6.2}$$ is an ordinary integer.

[\[thm:boundary\]]{#thm:boundary label="thm:boundary"} The $\mathcal B_{\mathrm{tag}}$-valued fixed-orbit series $$\mathcal G_4(u)=\sum_{n\ge3}u^nD_{\gamma_4,n}
\tag{6.3}$$ has radius of convergence exactly one. In particular, it diverges for every $|u|=1$.

For a fixed period, Lemma [\[lem:packet-envelope\]](#lem:packet-envelope){reference-type="ref" reference="lem:packet-envelope"} gives $\|D_{\gamma_4,n}\|=O(n)$, hence (6.3) converges for $|u|<1$.

Flatters' Theorem 1.4 [@flatters2009] gives a primitive rational prime divisor $p_n$ of $$\Delta_n=\mathop{\mathrm{N}}_{\mathbb Q(\sqrt{145})/\mathbb Q}(L_4^n-1)$$ for every $n>12$. Since $$L_4^n-1=\prod_{d\mid n}\Phi_d(L_4),$$ suppose that $p_n$ divided $\mathop{\mathrm{N}}(\Phi_d(L_4))$ for some proper divisor $d<n$. It would then divide $\mathop{\mathrm{N}}(L_4^d-1)=\Delta_d$, contradicting primitivity. Hence the factor at $d=n$ is the only possible cyclotomic carrier and $p_n\mid\mathop{\mathrm{N}}(\Phi_n(L_4))$. Reciprocal normalization gives $$\mathop{\mathrm{N}}(\Phi_n(L_4))=\beta_{4,n}^{\,2}.$$ Therefore $p_n\mid\beta_{4,n}$ and $$\|D_{\gamma_4,n}\|_{\rm tag}
=\log|\beta_{4,n}|\ge\log p_n\ge\log2
\qquad(n>12).
\tag{6.4}$$ For $|u|=1$, the terms of (6.3) have norm at least $\log2$ and do not tend to zero. Equivalently, the coefficient bounds $$\log2\le\|D_{\gamma_4,n}\|_{\rm tag}\le Cn
\qquad(n>12)$$ give $\limsup_{n\to\infty}\|D_{\gamma_4,n}\|_{\rm tag}^{1/n}=1$. The Banach-valued Cauchy--Hadamard formula proves exact radius one.

For any finite $s\in\mathbb C$, the pressure factor $e^{-s\widehat\ell_{\gamma_4}}$ cannot repair the $u=1$ divergence in the all-orbit series.

The factor is a fixed nonzero complex scalar on this orbit.

The result is stronger than failure of the particular global majorant in (4.7): it says the raw boundary object itself does not exist in the chosen source-native Banach topology.

# Executable certificate and adversarial controls

The proof is analytic, but every inherited interface is frozen in a compact certificate. Table [1](#tab:certificate){reference-type="ref" reference="tab:certificate"} summarizes the finite checks.

::: {#tab:certificate}
  Interface             Check                        Result
  --------------------- ---------------------------- ---------------------
  Dependencies          P31/P43/P46/P49/P50 hashes   $8/8$
  Symbolic census       periods $1$ through $32$     exact
  Degree envelope       rank cap $2^m$               exact
  Period-four packets   indices $3$ through $20$     $18/18$ P50 matches
  Extended packets      indices $3$ through $24$     $22/22$ nonzero
  Pressure domain       certified threshold          $3.125206884004728$
  Independent tests     unit/adversarial             $10/10$

  : Compact HCS-P51 audit ledger.
:::

The producer reconstructs the exact marked census from the four-state matrix, builds the inversion-fixed period-four packets from cyclotomic polynomials, and records the analytic constants. The independent checker does not import the producer. It recomputes the census and constants and independently rereads all eight hash-locked dependency files. It then attacks four possible promotions:

1.  deleting the $2^m$ field-degree cost;

2.  replacing $|u|<1$ by $u=1$;

3.  promoting norm pushforward to injective;

4.  promoting an open continuation, determinant, or operator claim.

All four are rejected.

The finite computation does not establish Theorem [\[thm:germ\]](#thm:germ){reference-type="ref" reference="thm:germ"} by extrapolation. It verifies the constants and dependency contracts used by the proof. The all-period conclusion comes from Lemmas [\[lem:height\]](#lem:height){reference-type="ref" reference="lem:height"} and [\[lem:packet-envelope\]](#lem:packet-envelope){reference-type="ref" reference="lem:packet-envelope"} and the exact geometric majorant.

#### Reproducibility.

The certificate, independent checker, unit tests, figure generator, source audit, and compiled PDF are included in the project directory. No table of rational primes or zeta zeros is consumed.

#### Data availability.

All finite data displayed in the paper are generated from . The figure carries a machine-readable trace file recording the certificate hash and panel claims.

# Route evaluation and next theorem

Theorem [\[thm:germ\]](#thm:germ){reference-type="ref" reference="thm:germ"} is a genuine all-orbit analytic advance. It solves the varying-field topology problem left open by the finite tagged ledger and makes rational norm pushforward continuous. Theorem [\[thm:boundary\]](#thm:boundary){reference-type="ref" reference="thm:boundary"} simultaneously explains why the resulting object is a two-variable germ rather than an ungraded zeta function.

The strict Route-A tuple is $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\mathrm{A4\_FORMAL\_HINT}),$$ with overall verdict **ROUTE\_A\_EXPLORATORY**. The entries have the following meanings.

-   A1 is weak: the packet clock is intrinsic, but there is no all-rational-prime orbit correspondence.

-   A2 fails: a Banach-valued series is not a transfer operator or Fredholm determinant.

-   A3 is partial: normal convergence and joint holomorphy are proved in a right-half-plane times the unit disk, but no continuation, functional equation, zero law, or von-Mangoldt trace follows.

-   A4 remains a formal hint: exact $SL_2$ monodromy and residue orders do not define a Hilbert--Pólya operator.

The next theorem should address the Abel boundary rather than generate more finite packet rows. Natural possibilities include a source-native subtraction, a logarithmic derivative, a distributional boundary value, or a Tauberian normalization as $u\uparrow1$. Any acceptable construction must retain the orbit, index, and prime-ideal tags until after the boundary operation and must connect to the pressure/von-Mangoldt mass scale without fitting target prime data.

#### Conclusion.

The finite packet ledger has become an all-orbit analytic germ. The first remaining wall is now equally precise: the raw Abel boundary diverges on one certified orbit. This positive theorem plus scoped obstruction identifies a single, testable next bridge.
