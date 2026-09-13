---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-pressure-weighted-all-orbit-abel-law"
canonical_tex: "henon_dynamics/henon_pressure_weighted_all_orbit_abel_law/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_pressure_weighted_all_orbit_abel_law/paper/paper.pdf"
source_sha256: "705f76ed4f5e838f093df172c0caba3d83a0179ca230270d505d23e2a8550016"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Pressure-Weighted All-Orbit Abel Laws for Hénon Cyclotomic Packets

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_pressure_weighted_all_orbit_abel_law>)
- [规范 TeX](<../../../../../henon_dynamics/henon_pressure_weighted_all_orbit_abel_law/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_pressure_weighted_all_orbit_abel_law/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_pressure_weighted_all_orbit_abel_law/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_pressure_weighted_all_orbit_abel_law/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the certified four-state survivor of the area-preserving Hénon map $H_6(q,p)=(1-6q^2-p,q)$, earlier work attached to every primitive orbit $\gamma$ and every $n>2$ an inversion-fixed half-cyclotomic integer $\beta_{\gamma,n}$ and its effective source-tagged divisor. A single period-four orbit was known to possess a totient Abel boundary, but interchanging that boundary with the complete pressure-weighted orbit sum was open. We prove that the packet mass satisfies $$\log|N_{F_\gamma/\mathbb Q}\beta_{\gamma,n}|
   =\frac{\varphi(n)}2\log M(f_{\lambda_\gamma})
   +O_\gamma\!\left(\sqrt n(1+\log n)^2\right),$$ where $f_{\lambda_\gamma}$ is the signed multiplier's minimal polynomial. The unit-circle conjugate case is paid by a lower bound for the argument of an algebraic power. Combining this orbitwise estimate with a separate, uniform positive packet envelope proves a locally uniform all-orbit Abel law in the previously certified pressure half-plane. The joint boundary of the primitive orbit and scaled cyclotomic index is the pressure-weighted Mahler-height orbit law times $\Gamma(2,1)$. In contrast, the renormalized source-tagged divisor vectors admit neither a norm-convergent nor a weakly convergent subnet. Thus a canonical scalar pressure boundary exists, but no pressure-critical continuation, prime trace, determinant, or operator is claimed.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Pressure-Weighted All-Orbit Abel Laws\
  for Hénon Cyclotomic Packets
```

## Markdown 正文

# Introduction

Periodic-orbit constructions often offer two incompatible kinds of information. Symbolic dynamics supplies an orbit census and pressure weights, while algebraic monodromy supplies exact multiplier fields and cyclotomic divisors. The present paper studies the boundary at which these two structures can first be summed simultaneously for a source-locked area-preserving Hénon system. The setting descends from the classical Hénon family [@Henon1976], but every statement below concerns one fixed certified survivor and not the full parameter family.

For a primitive orbit $\gamma$, previous stages constructed the signed unstable multiplier $\lambda_\gamma$, its trace field $F_\gamma=\mathbb Q(\lambda_\gamma+\lambda_\gamma^{-1})$, and the inversion-fixed integer $$\beta_{\gamma,n}
 =\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma),
 \qquad n>2.$$ Factoring this integer in $F_\gamma$ gives an effective divisor $D_{\gamma,n}$ in a universal weighted $\ell^1$ space. The exact norm identity is $$\|D_{\gamma,n}\|_{\rm tag}
 =\log|N_{F_\gamma/\mathbb Q}\beta_{\gamma,n}|.$$ The Abel-graded sum converges for $|u|<1$ and a certified right half-plane in the pressure variable, while the ungraded $u=1$ series already diverges on one exact orbit [@WangP51]. On that period-four orbit, the rescaling $(1-u)^2$ gives a nonzero scalar limit and a $\Gamma(2,1)$ scaled-index law [@WangP52].

The missing theorem was not another finite orbit calculation. It was the exchange $$\lim_{u\uparrow1}(1-u)^2
 \sum_\gamma e^{-s\widehat\ell_\gamma}
 \sum_{n\ge3}\|D_{\gamma,n}\|_{
 \rm tag}u^n,$$ including the identification of the correct orbit coefficient and a summable pressure-uniform majorant.

## Main contribution

Let $f_{\lambda_\gamma}$ be the monic minimal polynomial of the signed multiplier and put $$\mathcal H_\gamma=\log M(f_{\lambda_\gamma}).$$ Our first theorem identifies $\mathcal H_\gamma$, rather than merely $\log|\lambda_\gamma|$, as the exact coefficient of the totient main term. This matters whenever a nonphysical conjugate pair also lies outside the unit circle. We then prove, locally uniformly for $$\Re s>\sigma_0
 :=\frac{\log(2\phi)}{h_*\log J_*},
 \qquad J_*=\frac{\sqrt{17}+\sqrt{13}}2,$$ that $$\tau^2\sum_\gamma e^{-s\widehat\ell_\gamma}
 \sum_{n\ge3}\|D_{\gamma,n}\|_{\rm tag}e^{-\tau n}
 \longrightarrow
 \frac3{\pi^2}\sum_\gamma
 e^{-s\widehat\ell_\gamma}\mathcal H_\gamma.
 \label{eq:intro-main}$$ The source-locked numerical condition is $\Re s>3.125206884004728\ldots$.

For real $\sigma>\sigma_0$, the normalized joint distribution of $\gamma$ and $\tau n$ converges to $$\pi_\sigma\otimes\Gamma(2,1),
 \qquad
 \pi_\sigma(\gamma)
 \propto e^{-\sigma\widehat\ell_\gamma}\mathcal H_\gamma.$$ The source-tagged vector itself does not converge: every fixed coordinate vanishes while a bounded mass functional has a positive limit.

## Why the exchange is possible

For one frozen orbit, conjugates away from the unit circle have a uniformly bounded cyclotomic correction. A conjugate on the unit circle requires a Diophantine estimate. Yamada's lower bound for the argument of an algebraic power [@Yamada2025] gives an $O_\gamma(\sqrt n\log^2 n)$ aggregate remainder, which is negligible under $\tau^2$ Abel scaling.

Crucially, this sharp remainder is not made uniform in $\gamma$. Instead we use the earlier crude positive estimate $$\|D_{\gamma,n}\|_{\rm tag}\le 2^m(a+bm)n,
 \qquad m=m(\gamma),$$ after Abel normalization. The factor $\tau^2\sum ne^{-\tau n}$ is uniformly bounded, leaving exactly the convergent pressure series that defined the original germ. The sharp orbitwise theorem and crude all-orbit theorem perform different jobs.

## Claim boundary

Equation [\[eq:intro-main\]](#eq:intro-main){reference-type="eqref" reference="eq:intro-main"} is a scalar mass theorem in a safe right half-plane. We prove no analytic continuation to a pressure singularity, no prime-orbit theorem for the Mahler-height observable, no rational-prime von Mangoldt trace, no Fredholm determinant, and no Hilbert--Pólya operator. The explicit vector obstruction prevents the scalar boundary from being read as an unqualified divisor-valued limit.

# Source packets and Mahler spectral height

Let $H_6(q,p)=(1-6q^2-p,q)$ be restricted to the source-locked four-state survivor. Its adjacency matrix is $$A=\begin{pmatrix}
 1&0&1&0\\
 1&0&0&0\\
 0&1&0&1\\
 0&1&0&0
 \end{pmatrix}.$$ For a primitive orbit $\gamma$, let $m(\gamma)$ be its symbolic period and $M_\gamma\in SL_2$ its return derivative. Write $$\Lambda_\gamma=|\lambda_\gamma|>1,
 \qquad t_\gamma=\lambda_\gamma+\lambda_\gamma^{-1},
 \qquad F_\gamma=\mathbb Q(t_\gamma).$$ The signed branch is part of the source data. In particular, taking an absolute value before forming $t_\gamma$ is forbidden.

For $n>2$, cyclotomic reciprocity and the integral monodromy construction give [@WangP49] $$\beta_{\gamma,n}
 =\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma)
 \in\mathcal O_{F_\gamma}.
 \label{eq:beta}$$ Let $$D_{\gamma,n}
 =\sum_{\mathfrak q}v_{\mathfrak q}(\beta_{\gamma,n})
 [\gamma,n,\mathfrak q]$$ in the weighted source-tagged space $\mathcal B_{\mathrm{tag}}$. The ideal norm formula is the source mass identity of the all-orbit packet construction [@WangP51]: $$b_{\gamma,n}:=\|D_{\gamma,n}\|_{\rm tag}
 =\log|N_{F_\gamma/\mathbb Q}\beta_{\gamma,n}|.
 \label{eq:mass}$$

Put $K_\gamma=\mathbb Q(\lambda_\gamma)$. Inversion is a nontrivial automorphism and its fixed field is $F_\gamma$. Every embedding $\sigma:F_\gamma\hookrightarrow\mathbb C$ therefore has two extensions to $K_\gamma$, sending $\lambda_\gamma$ to the reciprocal roots of $$X^2-\sigma(t_\gamma)X+1.$$ Choose the root $\rho_\sigma$ of modulus at least one.

Let $f_\gamma$ be the monic minimal polynomial of $\lambda_\gamma$. Then $$\mathcal H_\gamma:=\log M(f_\gamma)
 =\sum_{\sigma:F_\gamma\hookrightarrow\mathbb C}
 \log|\rho_\sigma|.
 \label{eq:height}$$ Moreover $\mathcal H_\gamma\ge\log\Lambda_\gamma>0$.

The conjugates of the algebraic unit $\lambda_\gamma$ occur in reciprocal pairs $\rho_\sigma,\rho_\sigma^{-1}$. Their contribution to the Mahler measure is $|\rho_\sigma|$. Multiplying over the pairs proves [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"}. The physical real embedding contributes $\log\Lambda_\gamma$.

No $\rho_\sigma$ is a root of unity. If one were, irreducibility would make the minimal polynomial of $\lambda_\gamma$ cyclotomic, contradicting the physical root of modulus greater than one.

$\mathcal H_\gamma$ is the unnormalized logarithmic Mahler measure of the monic minimal polynomial. It is not the degree-normalized absolute Weil height. No hidden factor $[K_\gamma:\mathbb Q]^{-1}$ is present in the Abel coefficient.

The pressure length is $$\widehat\ell_\gamma=h_*\log\Lambda_\gamma.$$ The symbolic census and uniform unstable expansion inherited from the certified survivor give $$\#\{\gamma:m(\gamma)=m\}\le3\phi^m,
 \qquad
 \widehat\ell_\gamma\ge h_*m\log J_*.
 \label{eq:orbit-envelope}$$ These bounds will be used only after the orbitwise arithmetic asymptotic has been proved.

# The orbitwise cyclotomic asymptotic

For $n>2$, reciprocal symmetry gives a polynomial $q_n\in\mathbb Z[T]$ such that $$q_n(X+X^{-1})=X^{-\varphi(n)/2}\Phi_n(X).
 \label{eq:q-poly}$$ Thus $\beta_{\gamma,n}=q_n(t_\gamma)$. The cyclotomic Möbius product implies $$\log|\sigma(\beta_{\gamma,n})|
 =-\frac{\varphi(n)}2\log|\rho_\sigma|
 +\sum_{d\mid n}\mu(n/d)\log|\rho_\sigma^d-1|.
 \label{eq:embedding-log}$$

## Off-circle conjugates

If $|\rho_\sigma|>1$, then $$\log|\rho_\sigma^d-1|
 =d\log|\rho_\sigma|+\log|1-\rho_\sigma^{-d}|.$$ Using $\sum_{d\mid n}\mu(n/d)d=\varphi(n)$ in [\[eq:embedding-log\]](#eq:embedding-log){reference-type="eqref" reference="eq:embedding-log"} gives $$\log|\sigma(\beta_{\gamma,n})|
 =\frac{\varphi(n)}2\log|\rho_\sigma|
 +\epsilon_{\sigma,n}.
 \label{eq:off-circle}$$ The correction is bounded uniformly in $n$, because $$|\epsilon_{\sigma,n}|
 \le\sum_{d\ge1}-\log(1-|\rho_\sigma|^{-d})<\infty.$$

## Unit-circle conjugates

Suppose $|\rho_\sigma|=1$. Yamada's two-logarithm estimate [@Yamada2025 Theorem 1.2 and consequence (15)] implies that for an algebraic number of modulus one which is not a root of unity, $$\log|\arg(\rho_\sigma^d)|
 \ge-C_\sigma(1+\log d)^2.$$ Indeed, in Yamada's notation the integer nearest to the argument multiple is $O(d)$, so $b'=O_\sigma(d)$ and the displayed parameter $h=O_\sigma(1+\log d)$. All finitely many small $d$ are absorbed into $C_\sigma$. With the principal argument $\theta\in[-\pi,\pi]$, $$\frac2\pi|\theta|\le|1-e^{i\theta}|\le2.$$ Consequently $$|\log|1-\rho_\sigma^d||
 \le C'_\sigma(1+\log d)^2.
 \label{eq:unit-bound}$$ The elementary divisor bound $\tau(n)\le2\sqrt n$ then yields $$\left|
 \sum_{d\mid n}\mu(n/d)\log|1-\rho_\sigma^d|
 \right|
 \le2C'_\sigma\sqrt n(1+\log n)^2.
 \label{eq:unit-sum}$$ There is no height main term because $\log|\rho_\sigma|=0$.

For every primitive orbit $\gamma$, $$b_{\gamma,n}
 =\frac{\varphi(n)}2\mathcal H_\gamma+R_{\gamma,n},
 \qquad
 |R_{\gamma,n}|
 \le C_\gamma\sqrt n(1+\log n)^2.
 \label{eq:orbit-asymptotic}$$

Sum [\[eq:off-circle\]](#eq:off-circle){reference-type="eqref" reference="eq:off-circle"} and [\[eq:unit-sum\]](#eq:unit-sum){reference-type="eqref" reference="eq:unit-sum"} over the finitely many embeddings of $F_\gamma$. The main terms sum to [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"}; the embedding logarithms sum to [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"}.

The classical totient summatory estimate, or the elementary derivation given in the appendix, gives $$\tau^2\sum_{n\ge1}\varphi(n)e^{-\tau n}
 \longrightarrow\frac6{\pi^2}.
 \label{eq:totient-laplace}$$ Also $$\tau^2\sum_{n\ge3}\sqrt n(1+\log n)^2e^{-\tau n}
 =O\!\left(\tau^{1/2}(1+|\log\tau|)^2\right).$$ We therefore obtain the exact one-orbit coefficient.

[\[cor:one-orbit-abel\]]{#cor:one-orbit-abel label="cor:one-orbit-abel"} For every primitive orbit $\gamma$, $$\tau^2\sum_{n\ge3}b_{\gamma,n}e^{-\tau n}
 \longrightarrow\frac3{\pi^2}\mathcal H_\gamma.
 \label{eq:one-orbit-abel}$$

The factor one half in [\[eq:orbit-asymptotic\]](#eq:orbit-asymptotic){reference-type="eqref" reference="eq:orbit-asymptotic"} is intrinsic to the inversion-fixed packet. Replacing the right side of [\[eq:one-orbit-abel\]](#eq:one-orbit-abel){reference-type="eqref" reference="eq:one-orbit-abel"} by $6\mathcal H_\gamma/\pi^2$ is false.

# Pressure domination and the all-orbit boundary

The orbitwise error constant in [\[eq:orbit-asymptotic\]](#eq:orbit-asymptotic){reference-type="eqref" reference="eq:orbit-asymptotic"} is not uniform in $\gamma$, and we do not need it to be. The source construction gives a separate positive estimate. If $m=m(\gamma)$, then $$0\le b_{\gamma,n}\le K_m n,
 \qquad
 K_m=2^m(a+bm),
 \label{eq:crude}$$ where $$a=\log(2\sqrt3),
 \qquad b=\frac12\log(3+2\sqrt7).$$ For $0<\tau\le1$, $$\tau^2\sum_{n\ge3}ne^{-\tau n}
 \le\tau^2\frac{e^{-\tau}}{(1-e^{-\tau})^2}\le4.
 \label{eq:n-laplace}$$ Combining [\[eq:crude\]](#eq:crude){reference-type="eqref" reference="eq:crude"}, [\[eq:n-laplace\]](#eq:n-laplace){reference-type="eqref" reference="eq:n-laplace"}, and [\[eq:orbit-envelope\]](#eq:orbit-envelope){reference-type="eqref" reference="eq:orbit-envelope"}, one obtains, for $\sigma>\sigma_0$, $$12\sum_{m\ge1}(a+bm)
 \left(2\phi e^{-\sigma h_*\log J_*}\right)^m<\infty.
 \label{eq:majorant}$$

Let $\mathfrak m:\mathcal B_{\mathrm{tag}}\to\mathbb C$ be the norm-one logarithmic mass functional. For $\tau>0$ put $$Z(s,\tau)
 =\sum_{\gamma}e^{-s\widehat\ell_\gamma}
 \sum_{n\ge3}b_{\gamma,n}e^{-\tau n}.
 \label{eq:Z}$$ This is $\mathfrak m$ applied to the previously constructed Banach-valued germ at $u=e^{-\tau}$.

For $\Re s>\sigma_0$, $$\tau^2Z(s,\tau)\longrightarrow
 \mathcal A(s):=\frac3{\pi^2}
 \sum_{\gamma}e^{-s\widehat\ell_\gamma}\mathcal H_\gamma
 \label{eq:all-orbit}$$ locally uniformly in $s$. The series defining $\mathcal A$ converges normally, so $\mathcal A$ is holomorphic in this half-plane. Equivalently, $$(1-u)^2\mathfrak m(\mathcal G(s,u))\longrightarrow\mathcal A(s)
 \qquad(u\uparrow1).
 \label{eq:u-boundary}$$

Corollary [\[cor:one-orbit-abel\]](#cor:one-orbit-abel){reference-type="ref" reference="cor:one-orbit-abel"} gives the limit orbit by orbit, while [\[eq:majorant\]](#eq:majorant){reference-type="eqref" reference="eq:majorant"} dominates the normalized terms. Dominated convergence proves [\[eq:all-orbit\]](#eq:all-orbit){reference-type="eqref" reference="eq:all-orbit"}. For local uniformity, choose a common lower bound for $\Re s$ on a compact set, make the period tail of [\[eq:majorant\]](#eq:majorant){reference-type="eqref" reference="eq:majorant"} uniformly small, and then handle the finite orbit prefix.

The limit in the one-orbit theorem and the bound [\[eq:n-laplace\]](#eq:n-laplace){reference-type="eqref" reference="eq:n-laplace"} show that $\mathcal H_\gamma$ is bounded by a fixed multiple of $K_m$. Thus the series for $\mathcal A$ has the same normal majorant, proving holomorphy. Finally $(1-e^{-\tau})/\tau\to1$ proves [\[eq:u-boundary\]](#eq:u-boundary){reference-type="eqref" reference="eq:u-boundary"}.

The source-locked pressure estimate $h_*\ge0.277980$ gives the numerical safe condition $$\Re s>3.125206884004728\ldots .
 \label{eq:sigma-numeric}$$ The theorem does not assert convergence at equality or continuation beyond this sufficient domain.

The holomorphic function $\mathcal A(s)$ is not identified with a logarithmic derivative of a Ruelle or Fredholm determinant. In particular, no theorem here realizes $\mathcal H_\gamma$ as a Hölder potential, supplies repetition weights, or produces the trace-log combinatorics required by a determinant.

The use of two estimates is structural. The sharp arithmetic asymptotic identifies the limit for each orbit. The crude positive estimate justifies the all-orbit exchange. Trying to make the two-logarithm constant uniform over all multiplier fields would solve a stronger and unnecessary problem.

# A joint orbit--index product law

Fix real $\sigma>\sigma_0$ and write $$S_{\mathcal H}(\sigma)
 =\sum_\gamma e^{-\sigma\widehat\ell_\gamma}\mathcal H_\gamma.$$ This number is finite and positive. Define $$\pi_\sigma(\gamma)
 =\frac{e^{-\sigma\widehat\ell_\gamma}\mathcal H_\gamma}
 {S_{\mathcal H}(\sigma)}.
 \label{eq:orbit-law}$$ It is a canonical probability on the countable primitive orbit set. Each primitive orbit appears once; marked points and repetitions are not silently inserted into this marginal.

Equip the countable primitive-orbit set with the discrete topology. Define a probability on its product with $[0,\infty)$ by $$\nu_{\sigma,\tau}
 =\frac1{Z(\sigma,\tau)}
 \sum_\gamma\sum_{n\ge3}
 e^{-\sigma\widehat\ell_\gamma}b_{\gamma,n}e^{-\tau n}
 \delta_{(\gamma,\tau n)}.
 \label{eq:joint-measure}$$

As $\tau\downarrow0$, $$\nu_{\sigma,\tau}
 \Longrightarrow\pi_\sigma\otimes\Gamma(2,1),
 \label{eq:joint-limit}$$ where $\Gamma(2,1)$ has density $xe^{-x}\mathbf1_{x\ge0}\,\,\mathrm dx$.

Let $F$ be bounded on the primitive orbit set and $r\ge0$. Applying the all-orbit theorem at $(1+r)\tau$ gives $$\begin{aligned}
 &\lim_{\tau\downarrow0}
 \int F(\gamma)e^{-rx}\,\,\mathrm d\nu_{\sigma,\tau}(\gamma,x)\\
 &\qquad=\frac1{(1+r)^2}
 \sum_\gamma\pi_\sigma(\gamma)F(\gamma).\end{aligned}$$ The factor $(1+r)^{-2}$ is the Laplace transform of $\Gamma(2,1)$.

For completeness, tightness in the orbit coordinate follows from the summable period majorant [\[eq:majorant\]](#eq:majorant){reference-type="eqref" reference="eq:majorant"}. The crude packet estimate and $$\tau^2\sum_{\tau n\ge R}ne^{-\tau n}\ll(R+1)e^{-R}$$ give tightness in the scaled-index coordinate. The displayed mixed transforms therefore identify every subsequential limit, proving [\[eq:joint-limit\]](#eq:joint-limit){reference-type="eqref" reference="eq:joint-limit"}.

Two consequences are worth separating. First, the scaled index has the same $\Gamma(2,1)$ profile as the period-four packet, so the shape comes from the totient main term rather than a special multiplier. Second, the orbit marginal is not the unweighted pressure distribution: it is tilted by the complete Mahler spectral height.

The law [\[eq:orbit-law\]](#eq:orbit-law){reference-type="eqref" reference="eq:orbit-law"} remains trace-field arithmetic. It does not identify an orbit with a rational prime and does not preserve the individual prime-ideal factors inside $D_{\gamma,n}$.

# Escape from the source-tagged Banach space

For real $\sigma>\sigma_0$, consider the positive vector $$E_{\sigma,\tau}
 =\tau^2\sum_\gamma\sum_{n\ge3}
 e^{-\sigma\widehat\ell_\gamma}e^{-\tau n}D_{\gamma,n}
 \in\mathcal B_{\mathrm{tag}}.
 \label{eq:tagged-vector}$$ Positivity and the all-orbit theorem imply $$\|E_{\sigma,\tau}\|_{\rm tag}
 =\mathfrak m(E_{\sigma,\tau})
 \longrightarrow\frac3{\pi^2}S_{\mathcal H}(\sigma)>0.
 \label{eq:tagged-mass}$$

The family $E_{\sigma,\tau}$ has no norm-convergent subnet and no weakly convergent subnet as $\tau\downarrow0$.

Fix a source coordinate $(\gamma,n,\mathfrak q)$. Its coefficient in [\[eq:tagged-vector\]](#eq:tagged-vector){reference-type="eqref" reference="eq:tagged-vector"} is a fixed valuation multiplied by $\tau^2e^{-\sigma\widehat\ell_\gamma}e^{-\tau n}$, and hence tends to zero. Every norm limit would have all coordinates zero, so it would be the zero vector, contradicting [\[eq:tagged-mass\]](#eq:tagged-mass){reference-type="eqref" reference="eq:tagged-mass"}.

The same coordinate functionals force every possible weak limit to be zero. However, the bounded mass functional $\mathfrak m$ has the positive limit in [\[eq:tagged-mass\]](#eq:tagged-mass){reference-type="eqref" reference="eq:tagged-mass"}. This contradiction applies to every subnet.

This obstruction is not a defect in the scalar theorem. Mass moves to cyclotomic indices $n\asymp\tau^{-1}$, exactly as the Gamma scaling records. The boundary compactification retains total mass, orbit label and scaled index, but it does not retain a convergent vector of all prime-ideal atoms.

In particular, applying a rational-prime pushforward before taking the boundary cannot be called lossless: that pushforward already has a finite kernel on source packets, and the present theorem adds a separate topological escape.

# Certificate, route evaluation and open theorem

The finite certificate reconstructs the exact trace-field packet norms on the inherited primitive periods $1$, $3$ and $4$. Table [1](#tab:sentinels){reference-type="ref" reference="tab:sentinels"} lists the computed spectral heights. The physical multiplier is included to expose the failure of the physical-only substitution.

::: {#tab:sentinels}
  orbit            period   $\log\Lambda_\gamma$   $\mathcal H_\gamma$
  -------------- -------- ---------------------- ---------------------
  period one            1            1.967346...       3.0501161905...
  period three          3            4.882099...       8.9056092911...
  period four           4            6.359571...       6.3595708754...

  : Source-native H6 Mahler-height sentinels.
:::

The producer evaluates exact resultants for $3\le n\le72$ and compares their logarithms with the embedding formula. A separate reciprocal Salem polynomial $$X^4-X^3-X^2-X+1$$ has two unit-circle conjugates and exercises the branch controlled by [\[eq:unit-bound\]](#eq:unit-bound){reference-type="eqref" reference="eq:unit-bound"}. It is explicitly typed as non-H6 and is not used as a dynamical orbit. Four finite Abel scales and a three-orbit mixed Laplace profile approach the proved constants. An independent checker recomputes all dependency hashes, Mahler heights, exact norm sentinels, Gamma targets and claim-boundary statuses.

The numerical approach of these rows is a regression test only. The infinite orbit exchange is proved by the summable majorant [\[eq:majorant\]](#eq:majorant){reference-type="eqref" reference="eq:majorant"}; no finite period truncation is extrapolated.

Adversarial mutations reject:

1.  replacing $\mathcal H_\gamma$ by the physical $\log\Lambda_\gamma$;

2.  doubling the half-cyclotomic Abel coefficient;

3.  replacing $\Gamma(2,1)$ by an exponential law;

4.  promoting the scalar boundary to a tagged-vector limit;

5.  promoting the safe-half-plane theorem to a pressure-critical continuation, determinant or operator.

## Route-A evaluation

The source packet and its all-orbit scalar boundary are exact, but they do not yet supply a rational-prime distribution or a zero-counting determinant. The formal evaluation is therefore $$(A1_{\rm weak},A2_{\rm fail},A3_{\rm partial},A4_{\rm formal}),$$ with overall status `ROUTE_A_EXPLORATORY`. Route B is not invoked: there is no Hilbert space, dense operator domain, self-adjointness theorem, compact resolvent or completed determinant.

## The next theorem

The large remaining object is now explicit: $$\sum_\gamma e^{-s h_*\log\Lambda_\gamma}
 \log M(f_{\lambda_\gamma}).
 \label{eq:next-series}$$ One must determine whether the Mahler height is a Hölder, subadditive, or asymptotically additive observable on the symbolic survivor, or prove an obstruction to such a representation. Either outcome would clarify whether [\[eq:next-series\]](#eq:next-series){reference-type="eqref" reference="eq:next-series"} can be continued toward a genuine pressure singularity. The present paper supplies the arithmetic coefficient and the safe-domain boundary law, but it does not assume the missing thermodynamic theorem.

# Elementary Laplace estimates

We record the two elementary estimates used by the boundary proof. The classical summatory totient formula is $$S_\varphi(x):=\sum_{n\le x}\varphi(n)
 =\frac3{\pi^2}x^2+O(x\log(2x));$$ see, for example, @Apostol1976. Partial summation gives $$\sum_{n\ge1}\varphi(n)e^{-\tau n}
 =\tau\int_0^\infty S_\varphi(x)e^{-\tau x}\,\,\mathrm dx.$$ The main integral equals $6/(\pi^2\tau^2)$. Scaling $y=\tau x$ in the error integral gives $$\tau^2\sum_{n\ge1}\varphi(n)e^{-\tau n}
 =\frac6{\pi^2}+O(\tau\log(2/\tau)).$$

For the orbitwise remainder, split the sum at $n\le\tau^{-1}$ and compare the tail with an integral, or directly scale $x=\tau n$. One obtains $$\tau^2\sum_{n\ge3}\sqrt n(1+\log n)^2e^{-\tau n}
 \ll\tau^{1/2}(1+|\log\tau|)^2.$$ Both estimates are uniform for $0<\tau\le1/2$. Finally, $$\tau^2\sum_{\tau n\ge R}ne^{-\tau n}
 \ll(R+1)e^{-R}$$ follows from the corresponding exponential integral and is the scaled-index tightness estimate used in Section 5.
