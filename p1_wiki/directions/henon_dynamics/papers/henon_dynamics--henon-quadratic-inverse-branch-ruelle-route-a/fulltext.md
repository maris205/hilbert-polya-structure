---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-quadratic-inverse-branch-ruelle-route-a"
canonical_tex: "henon_dynamics/henon_quadratic_inverse_branch_ruelle_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_quadratic_inverse_branch_ruelle_route_a/paper/main.pdf"
source_sha256: "d87ad2b720e4263cfec761e17dedf018fb57b12707aff744a9eaeb92eaf1a75d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A quadratic inverse-branch Ruelle operator: exact stability traces and a scoped primitive product

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_quadratic_inverse_branch_ruelle_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_quadratic_inverse_branch_ruelle_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_quadratic_inverse_branch_ruelle_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_quadratic_inverse_branch_ruelle_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $F(z)=z^2-6$ we construct two strict inverse branches on $\mathbb D_4$ and a trace-class weighted composition operator on $H^2(\mathbb D_4)$. Every periodic point is exhausted by inverse words. The weights $m=0,1$ collapse exactly, whereas $m=2$ gives nontrivial multiplier traces, six exact coefficients, and a primitive product beginning at stability index $k=2$. The determinant is entire; the displayed raw product is claimed only in its proved disk $|u|<4$. This is a source-side benchmark, not a target-divisor or quantization result.
author:
- Hénon Dynamics Structure Program
date: 25 August 2026
title: |
  A quadratic inverse-branch Ruelle operator:\
  exact stability traces and a scoped primitive product
```

## Markdown 正文

#### Frozen model.

Put $\mathbb D_4=\{z:|z|<4\}$. The disk $6+\mathbb D_4=D(6,4)$ is contained in the right half-plane, so its principal square root defines $$\psi_\pm(z)=\pm\sqrt{z+6},\qquad
 (\mathcal L_m f)(z)=\sum_{\epsilon=\pm}(\psi_\epsilon'(z))^m
 f(\psi_\epsilon(z)),\quad m=0,1,2.$$ The owner is $H^2(\mathbb D_4)$ with $e_j(z)=(z/4)^j$; one branch is one clock step and $D_2(u)=\det(I-u\mathcal L_2)$.

[\[thm:main\]]{#thm:main label="thm:main"} Each $\mathcal L_m$ is trace class. For every $n\ge1$, the $2^n$ roots of $F^n(z)-z$ are simple, lie in $\mathbb D_4$, and are the fixed points of the $2^n$ rooted inverse words. Writing $\Lambda_n(p)=(F^n)'(p)$, $$\label{eq:trace}
 \operatorname{Tr}\mathcal L_m^n=\sum_{F^n(p)=p}
 \frac{\Lambda_n(p)^{-m}}{1-\Lambda_n(p)^{-1}}.$$ In particular $\operatorname{Tr}\mathcal L_0^n=2^n$, $\operatorname{Tr}\mathcal L_1^n=0$, and $$\operatorname{Tr}\mathcal L_2^n=\sum_{F^n(p)=p}\frac1{\Lambda_n(p)(\Lambda_n(p)-1)}.$$ Thus $\det(I-u\mathcal L_0)=1-2u$, $\det(I-u\mathcal L_1)=1$, and $D_2$ is entire. For $|u|<4$ it also has the absolutely convergent product $$\label{eq:product}
 D_2(u)=\prod_{[p]\,\mathrm{primitive}}\prod_{k=2}^{\infty}
 \bigl(1-u^{\ell(p)}\Lambda_p^{-k}\bigr).$$ No convergence of the raw product [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} is asserted outside $|u|<4$.

On $\overline{\mathbb D}_4$, $2\le|z+6|\le10$, hence $|\psi_\pm(z)|\le\sqrt{10}<4$ and $|\psi_\pm'(z)|\le q=1/(2\sqrt2)$. The principal-root formula also gives $\Re\psi_+\ge\sqrt2$ and $\Re\psi_-\le-\sqrt2$. For $m=2$, $$M_{(\psi_\epsilon')^2}C_{\psi_\epsilon}
 =\sum_{j\ge0}\bigl[(\psi_\epsilon')^2
 (\psi_\epsilon/4)^j\bigr]\otimes e_j^*.$$ The coefficient functionals have norm one and bounded holomorphic functions have Hardy norm at most their supremum. Therefore $$\|\mathcal L_2\|_1\le2\frac{1/8}{1-\sqrt{10}/4}
 =\frac1{4-\sqrt{10}}.$$ The same geometric expansion, with the corresponding bounded weights, proves trace class for $m=0,1$.

If $|z|>3$, then $|F(z)|\ge |z|^2-6>|z|$, so every periodic point lies in $\mathbb D_4$. Each length-$n$ inverse word is a $q^n$ contraction into the interior and has one fixed point. Conversely, a periodic point chooses one sign at each inverse step, uniquely because the branch images are separated. These points exhaust the monic degree-$2^n$ polynomial $F^n-z$. At the fixed point attached to a word $w$, the chain rule gives $\psi_w'(p)=\Lambda_n(p)^{-1}$; its modulus is at most $q^n<1$, so no root is multiple.

For a strict disk map $\phi$, holomorphic weight $g$, and fixed point $a$, conjugating $a$ to zero makes $M_gC_\phi$ triangular, with diagonal $g(a)\phi'(a)^j$. Its nuclear trace is $g(a)/(1-\phi'(a))$. Expanding $\mathcal L_m^n$ over inverse words and applying the chain rule proves [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"}.

Let $P_n=F^n-z$. It is monic of degree $2^n$, $P_n'(p)=\Lambda_n(p)-1$, and Lagrange interpolation gives $\sum_{P_n(p)=0}1/P_n'(p)=0$. Equation [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"} now gives the $m=0,1$ formulas. Their determinant identities follow first near zero from the trace logarithm and then globally by entireness.

For a primitive orbit put $\mu_p=\Lambda_p^{-1}$. In the rooted trace at time $n=r\ell(p)$ that orbit occurs at each of its $\ell(p)$ points; this cancels the same factor in $1/n$. Regrouping the trace logarithm and using $$\frac{\mu_p^{2r}}{1-\mu_p^r}=\sum_{k\ge2}\mu_p^{kr}$$ gives [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"}; in particular the lower index is forced to be $2$. There are at most $2^n/n$ primitive length-$n$ orbits and $|\mu_p|\le q^n$, so the sum of absolute values of the factor deviations is bounded by $$\sum_{n\ge1}\frac{|u|^n4^{-n}}{n(1-q^n)},$$ which converges locally uniformly for $|u|<4$. The resulting product agrees with the Fredholm determinant near zero and hence throughout this disk by the identity theorem.

#### Exact receipt.

Möbius inversion gives primitive counts $2,1,2,3,6,9$ for $n=1,\ldots,6$. Exact arithmetic in $\mathbb Q[z]/(F^n-z)$ gives the traces and Fredholm coefficients below; $c_0=1$ and $D_2(u)=\sum c_j u^j$.

   $n$   $\operatorname{Tr}\mathcal L_2^n$  $c_n$
  ----- ----------------------------------- ----------------------------
    1             $\frac{1}{12}$            $-\frac{1}{12}$
    2             $\frac{7}{720}$           $-\frac{1}{720}$
    3          $\frac{239}{257472}$         $-\frac{1}{1287360}$
    4      $\frac{1255703}{13810694400}$    $-\frac{1}{2057793465600}$

The two longest exact rows are displayed separately to preserve legibility: $$\begin{aligned}
 \operatorname{Tr}\mathcal L_2^5&=\frac{235072563599}{26491011084499968},
 &c_5&=-\frac{1}{2628907672975559586892800},\\
 \operatorname{Tr}\mathcal L_2^6&=\frac{655398850662090042240821783}{756396676602907446734765701632000},\\[-2pt]
 c_6&=-\frac{1}{2145321764151480887652914286846712748095922688000}.\end{aligned}$$ The recurrence is $c_n=-n^{-1}\sum_{j=1}^n c_{n-j}\operatorname{Tr}\mathcal L_2^j$. The six rows are a replay prefix, not a theorem cutoff.

#### Negative control, progress, and boundary.

For $z^2-2$ the same $\mathbb D_4$ construction fails because the branch point $-2$ lies inside the disk; other owner spaces are not excluded. Relative to finite polynomial matrices, real count models, and Möbius word matrices in this series, the advance is one nonlinear complex polynomial with intrinsic branches, unconditional nuclearity, all-period exhaustion, and a stability-weight ladder. No external novelty claim for general Ruelle theory is made.

The product in [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} is a source dynamical product, not an arithmetic Euler product. The strict Route-A tuple is $(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},\mathrm{A4\_FAIL})$; Route B is false. There is no prime-like target correspondence, target divisor or functional equation, arithmetic/local data, Euler factor, root number, automorphy, natural unitary or self-adjoint quantization, or Hilbert--Pólya claim.

#### Reproducibility and declarations.

The release contains a standard-library producer, an independent extended-Euclid checker (82 assertions), a SymPy/resultant cross-check (38 checks), byte replay, and 36 repaired-hash plus one stale-hash mutation rejection. The canonical evidence SHA-256 begins `50fc0cd93885`; all data are package-local and exactly reproducible. No human-subject or animal data, external funding, or competing interest applies. The authoring system assisted code and prose generation; every displayed claim is bounded by the checked evidence and internal theorem audits recorded with the release.
