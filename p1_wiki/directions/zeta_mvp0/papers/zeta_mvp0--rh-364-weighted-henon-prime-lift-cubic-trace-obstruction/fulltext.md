---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-364-weighted-henon-prime-lift-cubic-trace-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-364-weighted-henon-prime-lift-cubic-trace-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-364-weighted-henon-prime-lift-cubic-trace-obstruction/main.pdf"
source_sha256: "44df56838023323b55fbb0e90e7b47d8d697686dbfddfb245ff3a5dd70917345"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Weighted Hénon prime lifts: analytic domains, Fredholm regions, and a cubic trace obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-364-weighted-henon-prime-lift-cubic-trace-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-364-weighted-henon-prime-lift-cubic-trace-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-364-weighted-henon-prime-lift-cubic-trace-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-364-weighted-henon-prime-lift-cubic-trace-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-364-weighted-henon-prime-lift-cubic-trace-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the integral area-preserving Hénon map $H_6(x,y)=(1-6x^2-y,x)$, a locked source constructs a local mixing hyperbolic survivor conjugate to a four-state subshift. We extract two all-order consequences. First, if $L_o$ is the unstable multiplier modulus of a primitive survivor orbit, the exact cone expansion $L_o\ge(773/224)^{n_o}$, together with the four-state orbit count, gives a certified zero-free disk and an explicit primitive-period tail for every nonnegative multiplier weight. The Euler/flat correction has a larger analytic disk, but does not continue the complete determinants or certify the reported finite-section root.

  Second, we copy the same four-state matrix over all rational primes with one common Dirichlet clock. The resulting direct sum is in $S_q$ exactly when $q\operatorname{Re}s>1$, has an ordinary Fredholm determinant for $\operatorname{Re}s>1$, and genuine regularized determinants on their exact Schatten half-planes. Its inverse determinant factors into Riemann zeta functions, but its prime-power trace weights begin $(F_1,F_2,F_3)=(1,1,4)$: primes and squares match von Mangoldt, while cubes have exact surplus $3\log p$. Positive multiplier weights produce a fractional non-meromorphic singularity at $s=1$; the unique common scalar normalization repairs orders one and two but still fails at cubes.

  The local survivor is intrinsic, but copying it over prime labels is an engineered functor rather than a finite-field reduction or canonical global operator. Gates A--E remain false/open. No Hilbert--Pólya operator, Riemann-zero identification, completed-zeta divisor equality, or proof of the Riemann Hypothesis is claimed.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Weighted Hénon prime lifts:\
  analytic domains, Fredholm regions, and a cubic trace obstruction
```

## Markdown 正文

# Frozen foundation and exact scope

The RH-1--RH-361 corpus remains frozen in four provenance-preserving volumes [@WangRHCorpus2026]. RH-362 and RH-363 opened an independent arithmetic-dynamical branch, but left the physical route coordinate $$\texttt{actual\_same\_clock\_unnormalized\_head\_transport\_open}
 \label{eq:physical-coordinate}$$ unchanged [@WangRH3632026]. Nothing here estimates the physical same-clock defect, supplies a typed $q/E_{\rm off}$ theorem, or closes the RH-241 moving noisy trace envelope.

The external source studied in this paper is the map $$H_6(x,y)=(1-6x^2-y,x)
 \label{eq:henon-map}$$ and the explicitly defined compact survivor $\Lambda_*$ in four rational state rectangles [@WangWeightedHenon2026]. On $\Lambda_*$, the map is conjugate to the mixing subshift with adjacency matrix $$A=\begin{pmatrix}
 1&0&1&0\\
 1&0&0&0\\
 0&1&0&1\\
 0&1&0&0
 \end{pmatrix}.
 \label{eq:adjacency}$$ The same source proves an exact period-preserving bijection between primitive symbolic necklaces and primitive Hénon orbits in $\Lambda_*$, as well as a two-sided cone certificate. These are theorems about this local survivor, not the full nonwandering set of the Hénon plane.

Write $$\varphi=\frac{1+\sqrt5}{2},
 \qquad
 \kappa=\frac{773}{224}.
 \label{eq:constants}$$ The numerical finite-volume matrices and the period-eight through period-twelve root table in the source remain finite experiments. We use neither as asymptotic evidence.

# Symbolic counts and a certified weighted Euler disk

Let $F_n=\operatorname{Tr}(A^n)$ and let $p_n$ be the number of primitive survivor orbits of period $n$.

[\[thm:symbolic-ledger\]]{#thm:symbolic-ledger label="thm:symbolic-ledger"} For every $n\ge1$, $$\begin{aligned}
 \det(\lambda I-A)
 &=(\lambda^2-\lambda-1)(\lambda^2+1),
 \label{eq:characteristic}\\
 F_n
 &=\mathsf L_n+2\cos\!\left(\frac{n\pi}{2}\right),
 \label{eq:trace-lucas}\\
 p_n
 &=\frac1n\sum_{d\mid n}\mu(d)F_{n/d},
 \qquad
 0\le p_n\le\frac{F_n}{n}\le\frac{4\varphi^n}{n},
 \label{eq:primitive-envelope}\end{aligned}$$ where $\mathsf L_n=\varphi^n+(-\varphi^{-1})^n$ is the $n$-th Lucas number.

Direct expansion of $\det(\lambda I-A)$ gives [\[eq:characteristic\]](#eq:characteristic){reference-type="eqref" reference="eq:characteristic"}. The eigenvalues are $\varphi,-\varphi^{-1},i,-i$, so taking power traces proves [\[eq:trace-lucas\]](#eq:trace-lucas){reference-type="eqref" reference="eq:trace-lucas"}. The period-preserving conjugacy and finite-state fixed-point identity give $F_n=\sum_{d\mid n}d p_d$; Möbius inversion gives the first part of [\[eq:primitive-envelope\]](#eq:primitive-envelope){reference-type="eqref" reference="eq:primitive-envelope"}. Since the points on primitive period-$n$ orbits form a subset of $\operatorname{Fix}(A^n)$, one has $np_n\le F_n$. Finally, $|\mathsf L_n|\le\varphi^n+1$ and $|2\cos(n\pi/2)|\le2$, which is at most $4\varphi^n$.

For a primitive survivor orbit $o$, let $n_o$ be its primitive period, $\sigma_o\in\{-1,1\}$ the sign of its unstable multiplier, and $L_o>1$ its modulus. The cone certificate acts on the invariant unstable line at every iterate and gives $$L_o\ge\kappa^{n_o}.
 \label{eq:multiplier-envelope}$$ Here $L_o$ is a monodromy multiplier of $H_6$; it is not an eigenvalue of the four-state matrix $A$.

For real $\beta\ge0$, define $$Z_\beta(z)=\prod_{o\in\mathcal P_*}
 (1-z^{n_o}L_o^{-\beta})^{-1},
 \qquad
 D_{E,\beta}(z)=Z_\beta(z)^{-1}.
 \label{eq:weighted-euler}$$

[\[thm:weighted-disk\]]{#thm:weighted-disk label="thm:weighted-disk"} For every real $\beta\ge0$, both objects in [\[eq:weighted-euler\]](#eq:weighted-euler){reference-type="eqref" reference="eq:weighted-euler"} converge normally, are holomorphic, and are zero-free on $$|z|<R_\beta:=\frac{\kappa^\beta}{\varphi}.
 \label{eq:weighted-radius}$$ Fix $0<R<R_\beta$, put $t=R\kappa^{-\beta}$ and $q=\varphi t$. If the logarithm is truncated after all primitive periods at most $N$, then $$\sup_{|z|\le R}
 \left|\log Z_\beta(z)-\log Z_\beta^{(\mathrm{prim}\le N)}(z)\right|
 \le
 \frac{4q^{N+1}}
 {(N+1)(1-q)(1-t^{N+1})}.
 \label{eq:euler-tail}$$

For an orbit of period $n$, equation [\[eq:multiplier-envelope\]](#eq:multiplier-envelope){reference-type="eqref" reference="eq:multiplier-envelope"} bounds its logarithmic repetition sum by $t^n/(1-t^n)$ on the closed disk. Theorem [\[thm:symbolic-ledger\]](#thm:symbolic-ledger){reference-type="ref" reference="thm:symbolic-ledger"} therefore gives $$\begin{aligned}
 \sum_{n>N}p_n\frac{t^n}{1-t^n}
 &\le
 \frac{4}{(N+1)(1-t^{N+1})}
 \sum_{n>N}(\varphi t)^n,\end{aligned}$$ which is [\[eq:euler-tail\]](#eq:euler-tail){reference-type="eqref" reference="eq:euler-tail"}. Normal convergence supplies a canonical holomorphic logarithm. Exponentiating it and its negative proves the zero-free statements.

This is a certified disk, not a maximal-domain theorem. In particular, for $\beta=1$, $$R_1=\frac{\kappa}{\varphi}=2.132769077248\ldots,
 \label{eq:euler-beta-one-radius}$$ while the source reports a finite-section reciprocal root near $3.429$. That numerical value lies outside the proved disk.

## The larger flat correction

The periodic-point flat determinant has the formal factorization $$D_F(z)=\prod_{o\in\mathcal P_*}\prod_{j\ge0}
 \left(1-\sigma_o^jL_o^{-(j+1)}z^{n_o}\right)^{j+1}.
 \label{eq:flat-factorization}$$ Its $j=0$ factor is $D_{E,1}$. Define the remaining correction $$C_F(z)=\prod_{o\in\mathcal P_*}\prod_{j\ge1}
 \left(1-\sigma_o^jL_o^{-(j+1)}z^{n_o}\right)^{j+1}.
 \label{eq:flat-correction}$$

[\[thm:flat-correction\]]{#thm:flat-correction label="thm:flat-correction"} The product $C_F$ converges normally and is holomorphic and zero-free on $$|z|<R_F^{\rm corr}:=\frac{\kappa^2}{\varphi}
 =7.359957574612\ldots.
 \label{eq:flat-correction-radius}$$ The analytic identity $D_F=D_{E,1}C_F$ is directly licensed by the products only on the common smaller disk $|z|<\kappa/\varphi$. The larger correction disk alone does not continue either complete determinant.

For $0<x<1$, $$\sum_{j\ge1}(j+1)x^{j+1}
 =\frac{x^2(2-x)}{(1-x)^2}.
 \label{eq:flat-geometric}$$ Use $x=L_o^{-r}$, sum the logarithmic repetitions, and apply [\[eq:multiplier-envelope\]](#eq:multiplier-envelope){reference-type="eqref" reference="eq:multiplier-envelope"}. Uniformly in $n_o$ and $r$, the right side of [\[eq:flat-geometric\]](#eq:flat-geometric){reference-type="eqref" reference="eq:flat-geometric"} is bounded by a constant times $\kappa^{-2rn_o}$. The remaining orbit sum is dominated by $\sum_n4\varphi^n u^n/(1-u^n)$ with $u=|z|\kappa^{-2}$, which converges when $\varphi u<1$. Each factor is then nonzero, so the normal product is zero-free. The final scope statement follows because theorem [\[thm:weighted-disk\]](#thm:weighted-disk){reference-type="ref" reference="thm:weighted-disk"} controls the $j=0$ Euler factor only to $\kappa/\varphi$.

# A common-clock prime-copy operator

Let $\ell$ denote a rational prime and use the real logarithm in $\ell^{-s}=e^{-s\log\ell}$. On $\mathcal H=\bigoplus_{\ell}\mathbb C^4$, define $$\mathcal T_s=\bigoplus_{\ell\ \mathrm{prime}}\ell^{-s}A.
 \label{eq:prime-copy-operator}$$ This is a common-clock copy: every prime receives the same local matrix and the same exponent $s$. It is not a reduction of $H_6$ modulo $\ell$. We use the standard Schatten and regularized-determinant conventions of @Simon2005.

[\[thm:schatten\]]{#thm:schatten label="thm:schatten"} The operator $\mathcal T_s$ is bounded exactly for $\operatorname{Re}s\ge0$, and compact exactly for $\operatorname{Re}s>0$. For every finite $q>0$, $$\|\mathcal T_s\|_{S_q}^q
 =\|A\|_{S_q}^q\sum_{\ell}\ell^{-q\operatorname{Re}s},
 \qquad
 \mathcal T_s\in S_q\Longleftrightarrow q\operatorname{Re}s>1.
 \label{eq:schatten-law}$$

The norm of the $\ell$-block is $\ell^{-\operatorname{Re}s}\|A\|$. These block norms are uniformly bounded exactly for $\operatorname{Re}s\ge0$, and tend to zero exactly for $\operatorname{Re}s>0$. Each singular value of $A$ is multiplied by $\ell^{-\operatorname{Re}s}$, so summing their $q$-powers gives [\[eq:schatten-law\]](#eq:schatten-law){reference-type="eqref" reference="eq:schatten-law"}. The prime Dirichlet series converges exactly when its real exponent exceeds one.

The unweighted survivor determinant is $$D_{E,0}(z)=\det(I-zA)=1-z-z^3-z^4
 =(1+z^2)(1-z-z^2).
 \label{eq:unweighted-polynomial}$$

[\[thm:fredholm\]]{#thm:fredholm label="thm:fredholm"} For $\operatorname{Re}s>1$, $$\begin{aligned}
 \mathcal D_A(s):=\det_F(I-\mathcal T_s)
 &=\prod_{\ell}
 \left(1-\ell^{-s}-\ell^{-3s}-\ell^{-4s}\right)
 \label{eq:fredholm-product}\\
 &=\prod_{n\ge1}\zeta(ns)^{-p_n}.
 \label{eq:fredholm-zeta}\end{aligned}$$ Consequently $$\mathcal Z_A(s):=\mathcal D_A(s)^{-1}
 =\prod_{n\ge1}\zeta(ns)^{p_n}
 \label{eq:inverse-zeta-product}$$ in the same region. The scalar right sides continue meromorphically to $$\operatorname{Re}s>\log_2\varphi,
 \label{eq:scalar-continuation-region}$$ but below $\operatorname{Re}s>1$ they are not ordinary Fredholm determinants of $\mathcal T_s$.

Theorem [\[thm:schatten\]](#thm:schatten){reference-type="ref" reference="thm:schatten"} makes $\mathcal T_s$ trace class for $\operatorname{Re}s>1$. The Fredholm determinant then factors normally over the finite-dimensional blocks, and [\[eq:unweighted-polynomial\]](#eq:unweighted-polynomial){reference-type="eqref" reference="eq:unweighted-polynomial"} gives [\[eq:fredholm-product\]](#eq:fredholm-product){reference-type="eqref" reference="eq:fredholm-product"}. The primitive-orbit identity $\det(I-zA)=\prod_n(1-z^n)^{p_n}$ and absolute convergence permit interchange of the prime and period products, giving [\[eq:fredholm-zeta\]](#eq:fredholm-zeta){reference-type="eqref" reference="eq:fredholm-zeta"}. The sign is essential: positive zeta exponents belong to the inverse determinant.

For a compact set in $\operatorname{Re}s>\log_2\varphi$, the large-$n$ estimate $|\log\zeta(ns)|\ll2^{-n\operatorname{Re}s}$ combines with $p_n\le4\varphi^n/n$. The tail product therefore converges normally; finitely many initial zeta factors are meromorphic.

[\[thm:regularized\]]{#thm:regularized label="thm:regularized"} Let $m\ge1$ be an integer. On $m\operatorname{Re}s>1$, the regularized determinant exists and has the branch-free block product $$\det_m(I-\mathcal T_s)
 =\prod_{\ell}
 \left[
  \left(1-\ell^{-s}-\ell^{-3s}-\ell^{-4s}\right)
  \exp\!\left(
   \sum_{r=1}^{m-1}\frac{F_r}{r}\ell^{-rs}
  \right)
 \right].
 \label{eq:regularized-product}$$ In particular $\det_2(I-\mathcal T_s)$ is a genuine regularized determinant on $\operatorname{Re}s>1/2$.

Theorem [\[thm:schatten\]](#thm:schatten){reference-type="ref" reference="thm:schatten"} gives $\mathcal T_s\in S_m$ exactly in the stated region. In finite dimension, $$\det_m(I-zA)=\det(I-zA)
 \exp\!\left(\sum_{r=1}^{m-1}\frac{z^r\operatorname{Tr}(A^r)}r\right).
 \label{eq:finite-regularization}$$ The defining regularized product converges normally because its local remainder begins at order $m$, and $\sum_\ell\ell^{-m\operatorname{Re}s}<\infty$. Equations [\[eq:unweighted-polynomial\]](#eq:unweighted-polynomial){reference-type="eqref" reference="eq:unweighted-polynomial"} and [\[eq:finite-regularization\]](#eq:finite-regularization){reference-type="eqref" reference="eq:finite-regularization"} give [\[eq:regularized-product\]](#eq:regularized-product){reference-type="eqref" reference="eq:regularized-product"}.

The power-trace logarithm $-\sum_{r\ge m}F_r\sum_\ell\ell^{-rs}/r$ is directly absolutely convergent only after also imposing $\operatorname{Re}s>\log_2\varphi$. The block product [\[eq:regularized-product\]](#eq:regularized-product){reference-type="eqref" reference="eq:regularized-product"}, not an unlicensed logarithm branch, is the global statement on the full $S_m$ half-plane.

[\[cor:entropy-zero\]]{#cor:entropy-zero label="cor:entropy-zero"} At the positive real point $$s_2=\log_2\varphi=0.694241913630\ldots,
 \label{eq:entropy-zero}$$ the operator belongs to $S_2$ and $\det_2(I-\mathcal T_{s_2})=0$.

The $\ell=2$ block has scalar $2^{-s_2}=\varphi^{-1}$, and [\[eq:unweighted-polynomial\]](#eq:unweighted-polynomial){reference-type="eqref" reference="eq:unweighted-polynomial"} vanishes at $z=\varphi^{-1}$. The regularizing exponential is nonzero. Also $2s_2>1$, so theorem [\[thm:regularized\]](#thm:regularized){reference-type="ref" reference="thm:regularized"} applies.

This zero is the topological-entropy zero of one copied $\ell=2$ block. It is not a Riemann zero, a self-adjoint eigenvalue, or evidence for Gate E.

# The first arithmetic defect is at prime cubes

In $\operatorname{Re}s>1$, differentiate the inverse determinant logarithm: $$-\frac{\mathcal Z_A'}{\mathcal Z_A}(s)
 =\sum_{\ell}\sum_{r\ge1}
 F_r\log\ell\,\ell^{-rs}.
 \label{eq:trace-ledger}$$ The classical von Mangoldt ledger would have coefficient one at every power $\ell^r$.

[\[thm:cubic-obstruction\]]{#thm:cubic-obstruction label="thm:cubic-obstruction"} The first symbolic ledgers are $$(F_1,F_2,F_3)=(1,1,4),
 \qquad
 (p_1,p_2,p_3)=(1,0,1).
 \label{eq:first-ledgers}$$ Thus [\[eq:trace-ledger\]](#eq:trace-ledger){reference-type="eqref" reference="eq:trace-ledger"} gives the classical weight $\log\ell$ at primes and prime squares, but gives $4\log\ell$ at prime cubes. The first surplus is exactly $3\log\ell$.

Theorem [\[thm:symbolic-ledger\]](#thm:symbolic-ledger){reference-type="ref" reference="thm:symbolic-ledger"} gives $F_1=1,F_2=1,F_3=4$. Möbius inversion gives $p_1=1$, $p_2=(F_2-F_1)/2=0$, and $p_3=(F_3-F_1)/3=1$. Substitution in [\[eq:trace-ledger\]](#eq:trace-ledger){reference-type="eqref" reference="eq:trace-ledger"} proves the weight statement.

Equivalently, the first zeta factors of $\mathcal Z_A$ are $$\mathcal Z_A(s)=\zeta(s)\zeta(3s)\zeta(4s)^2\cdots.
 \label{eq:first-zeta-factors}$$ The factor $\zeta(s)$ comes from the unique survivor fixed orbit. The first chaotic surplus is the unique primitive period-three orbit and the factor $\zeta(3s)$. The appearance of Riemann zeta here is forced by copying the same finite-state orbit factor over the prime labels; it is not spectral recovery of Riemann zeros.

# Positive weights and common scalar normalization

The full real Hénon map has two fixed points. Only one belongs to the certified survivor.

[\[lem:fixed-atom\]]{#lem:fixed-atom label="lem:fixed-atom"} The unique fixed point in $\Lambda_*$ is $$P_*=(x_*,x_*),
 \qquad
 x_*=-\frac{1+\sqrt7}{6}.
 \label{eq:fixed-point}$$ Its unstable multiplier modulus is $$L_*=1+\sqrt7+\sqrt{7+2\sqrt7}
 =7.151675243800\ldots.
 \label{eq:fixed-multiplier}$$

The fixed-point equation is $6x^2+2x-1=0$. The negative root lies in the negative state interval; the positive root does not lie in either certified state interval. At the negative root, the derivative has determinant one and trace $-12x_*=2+2\sqrt7$. Solving its quadratic characteristic equation gives [\[eq:fixed-multiplier\]](#eq:fixed-multiplier){reference-type="eqref" reference="eq:fixed-multiplier"}.

For real $\beta\ge0$ and $c>0$, define, initially in a sufficiently far right half-plane, $$\mathfrak Z_{\beta,c}(s)
 =\prod_{\ell}Z_\beta(c\ell^{-s}).
 \label{eq:weighted-prime-lift}$$

[\[thm:fractional\]]{#thm:fractional label="thm:fractional"} For $c=1$ and every real $\beta\ge0$, the product [\[eq:weighted-prime-lift\]](#eq:weighted-prime-lift){reference-type="eqref" reference="eq:weighted-prime-lift"} converges normally and is holomorphic and zero-free on $\operatorname{Re}s>1$. As real $\sigma\downarrow1$, $$\log\mathfrak Z_{\beta,1}(\sigma)
 =L_*^{-\beta}\log\frac1{\sigma-1}+O(1).
 \label{eq:fractional-asymptotic}$$ For $\beta=0$, the singularity is an ordinary simple pole. For every real $\beta>0$, the exponent lies strictly between zero and one, so $\mathfrak Z_{\beta,1}$ has no meromorphic continuation through $s=1$. Along the real boundary, its inverse has corresponding fractional-order vanishing; this is not a holomorphic zero through $s=1$.

Theorem [\[thm:weighted-disk\]](#thm:weighted-disk){reference-type="ref" reference="thm:weighted-disk"} gives $R_\beta\ge1/\varphi>1/2$. Thus all local arguments $\ell^{-s}$ stay in one compact subdisk for $\operatorname{Re}s\ge1$, and $$\log Z_\beta(z)=L_*^{-\beta}z+O(z^2)
 \label{eq:local-fixed-expansion}$$ uniformly there. Summing the linear term over primes gives $L_*^{-\beta}\sum_\ell\ell^{-s}$, while the quadratic remainders converge normally near $s=1$. The prime zeta asymptotic [@Tenenbaum2015] $\sum_\ell\ell^{-\sigma}=\log(1/(\sigma-1))+O(1)$ proves [\[eq:fractional-asymptotic\]](#eq:fractional-asymptotic){reference-type="eqref" reference="eq:fractional-asymptotic"}. A meromorphic function has an integer zero or pole order, so a noninteger leading logarithmic coefficient is impossible.

To test whether one common scalar can repair the arithmetic trace weights, put $$G_m(\beta)=\sum_{o:n_o\mid m}
 n_oL_o^{-\beta m/n_o},
 \qquad
 Q_m(\beta,c)=c^mG_m(\beta).
 \label{eq:weighted-ledger}$$ Whenever [\[eq:weighted-prime-lift\]](#eq:weighted-prime-lift){reference-type="eqref" reference="eq:weighted-prime-lift"} is expanded in a common convergence half-plane, $$-\frac{\mathfrak Z_{\beta,c}'}{\mathfrak Z_{\beta,c}}(s)
 =\sum_{\ell,m\ge1}Q_m(\beta,c)
 \log\ell\,\ell^{-ms}.
 \label{eq:weighted-trace-ledger}$$

[\[thm:scalar-obstruction\]]{#thm:scalar-obstruction label="thm:scalar-obstruction"} Fix real $\beta\ge0$. If $c>0$ is required to match the prime weight, $Q_1(\beta,c)=1$, then uniquely $$c=L_*^\beta.
 \label{eq:forced-scalar}$$ For this scalar, $$Q_2(\beta,L_*^\beta)=1,
 \qquad
 Q_3(\beta,L_*^\beta)
 =1+3\left(\frac{L_*^3}{L_3}\right)^\beta>1,
 \label{eq:weighted-cubic-defect}$$ where $L_3$ is the unstable multiplier modulus of the unique primitive period-three survivor orbit. At $\beta=0$, the cubic value is four. Therefore no common positive scalar normalization produces von Mangoldt weights at all prime powers.

Only the fixed orbit divides order one, so $Q_1=cL_*^{-\beta}$, proving [\[eq:forced-scalar\]](#eq:forced-scalar){reference-type="eqref" reference="eq:forced-scalar"}. Since $p_2=0$, order two contains only the second repetition of the fixed orbit and hence $Q_2=c^2L_*^{-2\beta}=1$. Since $p_3=1$, order three contains the third fixed repetition and one primitive period-three orbit, giving $G_3=L_*^{-3\beta}+3L_3^{-\beta}$. Multiplication by $c^3=L_*^{3\beta}$ gives [\[eq:weighted-cubic-defect\]](#eq:weighted-cubic-defect){reference-type="eqref" reference="eq:weighted-cubic-defect"}.

The coefficient obstruction is valid for every real $\beta\ge0$. The analytic normalized product near $s=1$ requires an additional strict radius condition.

[\[prop:beta-threshold\]]{#prop:beta-threshold label="prop:beta-threshold"} The all-order source bound proves that the normalized local arguments in [\[eq:weighted-prime-lift\]](#eq:weighted-prime-lift){reference-type="eqref" reference="eq:weighted-prime-lift"}, with $c=L_*^\beta$, lie strictly inside the weighted Euler disk at $s=1$ exactly when $$0\le\beta<\beta_0,
 \qquad
 \beta_0=
 \frac{\log(2/\varphi)}{\log(L_*/\kappa)}
 =0.290834898770\ldots.
 \label{eq:beta-threshold}$$ In this range the normalized prime lift has a simple zeta pole times a holomorphic nonzero factor near $s=1$. For $\beta\ge\beta_0$, the exact coefficient identities [\[eq:forced-scalar\]](#eq:forced-scalar){reference-type="eqref" reference="eq:forced-scalar"}-- [\[eq:weighted-cubic-defect\]](#eq:weighted-cubic-defect){reference-type="eqref" reference="eq:weighted-cubic-defect"} remain valid, but the present source does not license the same near-$s=1$ infinite-product statement.

At $s=1$, the largest local argument is the $\ell=2$ argument $L_*^\beta/2$. Theorem [\[thm:weighted-disk\]](#thm:weighted-disk){reference-type="ref" reference="thm:weighted-disk"} places it strictly inside the certified disk precisely when $L_*^\beta/2<\kappa^\beta/\varphi$, which is [\[eq:beta-threshold\]](#eq:beta-threshold){reference-type="eqref" reference="eq:beta-threshold"}. In the strict range, the local logarithm has first coefficient one and a uniformly summable quadratic remainder, so the global product is $\zeta(s)$ times a holomorphic nonzero factor. Equality or reversal of the radius inequality supplies no such continuation theorem.

Complex and negative weights are outside the theorem. Because every $L_o>0$, complex powers can be defined using the real logarithm, but the absolute-value estimates then depend on $\operatorname{Re}\beta$, and $Q_3$ has no real order relation. Negative real weights require an explicit all-order multiplier upper envelope that is not established in this paper.

# Route A value, Route B obstruction, and Gates

  Route     Exact verdict
  --------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Route A   **GO.** The local survivor yields an all-order weighted analytic theorem and a larger flat correction domain. The prime-copy functor has exact compact/Schatten/Fredholm regions, a scalar zeta factorization, a fractional singularity theorem, and a strict cubic normalization obstruction.
  Route B   **STOP\_SCOPED.** The first fatal mismatch is Gate A data type: copying one local matrix over all prime labels is engineered, not a canonical arithmetic globalization. Even if this functor is accepted, Gate D fails at prime cubes because the trace weight is four rather than one.

The following distinctions are mandatory.

1.  The survivor $\Lambda_*$ is an intrinsic local hyperbolic set, but $\mathcal T_s$ is not the reduction of that real set modulo primes. The prime labels are added by definition.

2.  Neither $\mathcal D_A$ nor $\det_2(I-\mathcal T_s)$ is the stationary-centered physical noisy determinant used in the original RH route.

3.  The factorization into $\zeta(ns)$ is an exact consequence of copying the same primitive orbit factors over prime labels. It is not a discovery of Riemann zeros in the Hénon spectrum.

4.  The cube obstruction excludes common scalar normalization of this positive orbit ledger. It does not exclude signed cancellations, orbit-dependent weights, or a different intrinsic global construction.

5.  The larger flat correction disk does not certify the source's finite root near $3.429$, and finite root stability is not analytic continuation.

Thus the Gate ledger remains

  Gate   Status       First missing or failed object
  ------ ------------ -------------------------------------------------
  A      false/open   canonical intrinsic global physical determinant
  B      false/open   time-oriented scattering or unitary completion
  C      false/open   self-adjoint generator and intrinsic $T\log T$
  D      false/open   cube weight is $4\log p$, not $\log p$
  E      false/open   completed-zeta divisor equality

No Hilbert--Pólya operator, self-adjoint generator, Riemann-zero spectral identification, completed-zeta divisor equality, or proof of the Riemann Hypothesis follows.

# Executable protocol

The artifact performs finite exact reproduction and provenance checks only:

1.  it hashes the locked survivor theorem, contraction, weighted-zeta, orbit, limitation, RH-363, and four-volume sources;

2.  it recomputes $F_1,\ldots,F_{12}$, the Lucas trace identity, and $p_1,\ldots,p_{12}$;

3.  it checks $\det(I-zA)=1-z-z^3-z^4$, the exact fixed point and multiplier, the two certified radii, and $\beta_0$;

4.  it verifies the source contains exactly one selected survivor orbit at periods one and three and reproduces representative scalar-normalization ledgers;

5.  it requires every Gate and every forbidden macro claim to remain false.

These rows do not prove the all-order convergence theorems; sections 2--5 do. They also do not promote the stored multiplier decimals to interval certificates beyond the exact symbolic multiplicities and analytic formulas used in the proofs.

# Conclusion

The certified survivor supplies more than a finite cycle table: its exact symbolic entropy and cone expansion give a rigorous weighted analytic domain. Prime copying then yields unusually clean operator ideals and Fredholm formulas. Precisely because the construction is clean, its arithmetic failure is visible at the first nontrivial primitive orbit: the unique period-three orbit changes the cube trace weight from one to four.

This is useful Route A structure and a sharp Route B boundary. The natural next questions are a positive-radius theorem for the unweighted return-cycle bouquet, a genuine primitive-divisor theorem for its coefficient anchors, or an intrinsic globalization that does not add prime copies by hand. The original physical same-clock route remains open and unchanged.
