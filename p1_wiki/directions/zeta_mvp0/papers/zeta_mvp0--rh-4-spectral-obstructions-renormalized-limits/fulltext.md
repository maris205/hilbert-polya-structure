---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-4-spectral-obstructions-renormalized-limits"
canonical_tex: "zeta_mvp0/papers/RH-4-spectral-obstructions-renormalized-limits/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-4-spectral-obstructions-renormalized-limits/spectral-obstructions-renormalized-limits.pdf"
source_sha256: "e9c6c16a4ba073fc89d1b757b185e0bde7297b0f2ac44459054d633cc5dcf7ad"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Spectral Obstructions and Renormalized Limits for Quadratic Models of Riemann-Zero Statistics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-4-spectral-obstructions-renormalized-limits>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-4-spectral-obstructions-renormalized-limits/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-4-spectral-obstructions-renormalized-limits/spectral-obstructions-renormalized-limits.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-4-spectral-obstructions-renormalized-limits/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-4-spectral-obstructions-renormalized-limits/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Recent numerical models compare spectra extracted from logarithmically driven quadratic transfer matrices and from a quartic-regularized area-preserving Hénon model with the ordinates of the nontrivial zeros of the Riemann zeta function. We determine rigorously which parts of such comparisons are intrinsic and which can arise from algebraic symmetry, smooth counting laws, or fixed-resolution limits.

  First, the orbit pair-frequency formula used in the empirical construction is a joint occupation matrix, not a conditional transition matrix; row normalization generally changes its spectrum. Sorting eigenphases in the open upper half-plane before applying the standard phase-unwrapping recursion then makes the recursion telescope exactly: the "unwrapped" phase is the original principal phase. Moreover, augmenting data by conjugate pairs $(\phi_j,\gamma_j)$ and $(-\phi_j,-\gamma_j)$ forces the least-squares intercept to vanish and is exactly equivalent to a zero-intercept fit on the positive branch. The Riemann--von Mangoldt formula implies, without assuming the Riemann hypothesis, $$\gamma_n=\frac{2\pi n}{W(n/e)}+O(1),$$ so an arithmetic-free smooth envelope already has vanishing pointwise relative error and vanishing mean percentage error.

  For a fixed-resolution operator family $A(u)$ driven by $u_n=u_{\mathrm c}+\kappa(\log(n+c))^{-p}+O((\log n)^{-p-1})$, we prove operator freezing of the Cesàro average $\overline A_T=T^{-1}\sum_{n\le T}A(u_n)$. Under Hölder continuity the rate is $O((\log T)^{-p\eta})$; under differentiability the first-order renormalized limit is $$(\log T)^p(\overline A_T-A(u_{\mathrm c}))\longrightarrow \kappa A'(u_{\mathrm c}).$$ For an endpoint-anchored triangular schedule, the leading $(\log T)^{-p}$ average cancels and the response begins at order $(\log T)^{-p-1}$. We derive the corresponding simple-eigenvalue and eigenphase response formulas and state the uniform double-limit conditions needed when the spatial resolution also varies. Finally, for the confining quartic Hamiltonian used in the Hénon regularization, the one-dimensional Weyl law gives $N_H(E)\asymp E^{3/4}$, which is incompatible with $N_\zeta(T)\asymp T\log T$ under every fixed affine rescaling.

  These results neither prove nor disprove the Riemann hypothesis and do not construct a Hilbert--Pólya operator. They identify the centering, unfolding, resolution control, and order-sensitive spectral objects required for a nontrivial future comparison beyond finite-window agreement.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Spectral Obstructions and Renormalized Limits**\
  **for Quadratic Models of Riemann-Zero Statistics**
```

## Markdown 正文

**Keywords:** Riemann zeros; quadratic dynamics; transfer operator; phase unwrapping; spectral perturbation; Riemann--von Mangoldt formula; Weyl law; Hénon map.

**MSC 2020:** 11M26; 37M25; 47A55; 47B33; 81Q50.

# Introduction

The Hilbert--Pólya idea asks for a natural self-adjoint operator whose spectrum accounts for the nontrivial zeros of the Riemann zeta function [@BerryKeating1999; @SchumayerHutchinson2011]. It is much stronger than a finite affine fit between two ordered lists. The distinction is especially important for numerical models: conjugate symmetry, a fitted mean density, discretization, and phase relabeling can each produce accurate-looking plots without defining an operator correspondence.

Two recent manuscripts in the prime-dynamics program motivate the present analysis. The first extracts eigenphases from time-averaged finite transition matrices for a logarithmically driven quadratic map and compares affine images of those phases with zero ordinates [@WangSpectralFlow2026]. The second lifts the dynamics to an area-preserving Hénon map and studies both a direct unitary solver and a quartic-regularized continuum Hamiltonian [@WangHenon2026]. Those papers report finite numerical observations. Here we isolate exact mathematical consequences of their constructions and delimit the claims that the observations can support.

The dynamical foundation has been strengthened independently. The prime-sieve correspondence has an exact kneading-coordinate reformulation [@WangReformulation2026]; sparse admissible repair preserves the centered Fourier limit of prime and sieve words [@WangPrimeSpectrum2026]; and the limiting quadratic map has a genuine period-two mode which requires a parity-resolved transfer-operator decomposition [@WangParity2026]. These results justify concrete symbolic and dynamical objects. They do not, by themselves, identify Riemann-zero ordinates with eigenvalues of a self-adjoint operator.

Our purpose is constructive: before seeking a positive spectral bridge, one should remove mechanisms that are forced by algebra or by a smooth envelope. The surviving comparison must then be formulated at the level of centered and unfolded fluctuations, with a controlled continuum limit.

## Main results {#main-results .unnumbered}

The paper proves the following statements.

1.  *Joint occupation is not conditional transition.* The empirical pair-frequency matrix displayed in the finite-orbit construction has row sums equal to source-bin occupation frequencies. A row-stochastic transition estimator requires an additional normalization, which generally changes the spectrum.

2.  *Sorted phase unwrapping is an identity.* If principal phases are first restricted to $(0,\pi)$ and sorted, every adjacent increment already lies in the principal branch. The usual unwrapping recursion telescopes and returns the sorted input exactly.

3.  *Conjugate doubling forces a zero intercept.* Ordinary least squares on the symmetric data $(\pm\phi_j,\pm\gamma_j)$ has intercept zero. Its slope and residual are precisely those of the positive data with the intercept constrained to zero.

4.  *Mean-density matching has vanishing relative error.* If $\gamma_n$ denotes the positive ordinate of the $n$th nontrivial zero, counted with multiplicity and without assuming that its real part is $1/2$, then $$\gamma_n=\Gamma_n+O(1),
            \qquad
            \Gamma_n=\frac{2\pi n}{W(n/e)}.$$ Thus any sequence with the correct leading $2\pi n/\log n$ envelope has relative error tending to zero, even if it contains no zero fluctuation data.

5.  *Fixed-resolution averages freeze.* For a Hölder operator family and a logarithmic schedule approaching $u_{\mathrm c}$, the time-averaged operator converges to the frozen operator $A(u_{\mathrm c})$. If $A$ is differentiable, the logarithmically rescaled difference converges to the derivative $A'(u_{\mathrm c})$, and simple eigenvalues have the corresponding first-order response. Endpoint anchoring cancels the leading average and improves the response scale from $(\log T)^{-p}$ to $(\log T)^{-p-1}$.

6.  *The continuum and long-time limits cannot be interchanged for free.* To observe the renormalized response while the grid is refined, the discretization bias must be little-$o$ of the logarithmic response scale and the derivatives must converge uniformly. A trajectory-estimated matrix additionally requires a sequential law of large numbers at that same scale.

7.  *The quartic continuum regularization has the wrong asymptotic counting exponent.* A one-dimensional Schrödinger operator with positive quartic leading coefficient has $N_H(E)\sim C E^{3/4}$. Consequently its eigenvalues cannot be affinely and relatively matched to the Riemann ordinates at high index.

Results **R1--R4** and the quartic Weyl-law obstruction are unconditional. The fixed-resolution statements are abstract theorems with explicit regularity hypotheses and are unconditional for any concrete finite matrix family satisfying them. Application to a continuum Perron--Frobenius family or to a single-orbit empirical estimator requires the additional uniform estimates stated below.

## What is not claimed {#what-is-not-claimed .unnumbered}

Nothing in this paper locates a zero in the complex plane, proves a zero-free region, or proves the Riemann hypothesis. Matching a real list to the ordinates $\gamma_n$ alone does not determine the real parts of the zeros. Moreover, any prescribed real sequence can be installed artificially as the diagonal of an abstract self-adjoint operator. A Hilbert--Pólya result would require a natural operator, constructed independently of the target data, together with a complete theorem connecting its spectrum to all nontrivial zeros. We make no such assertion.

# A hierarchy of spectral statements {#sec:hierarchy}

Let $\rho=\beta+i\gamma$ range over the nontrivial zeros of $\zeta(s)$ in the upper half-plane, counted with multiplicity, and write $$0<\gamma_1\le\gamma_2\le\cdots.$$ This definition is unconditional: it does not assume $\beta=1/2$.

[\[def:levels\]]{#def:levels label="def:levels"} Let $z_1,\ldots,z_m$ be spectral data produced by a model.

1.  A *finite affine fit* minimizes $\sum_{j\le m}|a z_j+b-\gamma_j|^2$ or a related finite error.

2.  A *counting-law match* compares the leading asymptotics of the two counting functions.

3.  A *local-statistics match* first unfolds each list by its own smooth counting function and then compares spacings, correlation functions, or form factors.

4.  A *spectral-measure correspondence* identifies specified spectral measures, including their atoms and continuous parts, under a stated limiting procedure.

5.  An *operator spectral realization* constructs an operator independently of the zeros and proves a complete spectral identity with controlled multiplicities and no missing or spurious levels.

These levels are not interchangeable. A small error in (i) may come almost entirely from (ii); agreement at (iii) is shared by broad universality classes and need not determine individual levels; and neither statement supplies the complete operator construction and spectral identity required in (v). In particular, diagonalizing a real Markov matrix produces complex resonances, whereas a self-adjoint Hamiltonian produces real energies and a unitary operator produces phases modulo $2\pi$. They are different spectral objects until an explicit transform relates them.

[\[rem:ordinates-rh\]]{#rem:ordinates-rh label="rem:ordinates-rh"} Suppose a natural self-adjoint operator were shown merely to have eigenvalue list $(\gamma_n)$. This identifies real numbers already defined as imaginary parts of zeros; it does not by itself prove that the corresponding real parts are $1/2$. The Hilbert--Pólya implication requires a stronger identity that characterizes every nontrivial zero as $1/2+i\lambda$ for an eigenvalue $\lambda$, with completeness. The distinction prevents a numerical ordinate comparison from being read as evidence of a proof.

# Exact finite-dimensional diagnostics {#sec:algebraic}

## Joint occupation and conditional transition

Let $B_1,\ldots,B_d$ be a measurable partition, and let $x_0,\ldots,x_T$ be any finite orbit segment. Define the empirical pair-occupation matrix $$\label{eq:joint-matrix}
    C_{ij}^{(T)}
    =\frac1T\sum_{t=0}^{T-1}
      \mathbf 1_{B_i}(x_t)\mathbf 1_{B_j}(x_{t+1})$$ and the source-bin frequencies $$\label{eq:source-frequencies}
    \pi_i^{(T)}=\frac1T\sum_{t=0}^{T-1}\mathbf 1_{B_i}(x_t).$$

[\[prop:joint-transition\]]{#prop:joint-transition label="prop:joint-transition"} Assume $d\ge2$. For every $i$, $$\label{eq:joint-row-sum}
    \sum_{j=1}^d C_{ij}^{(T)}=\pi_i^{(T)}.$$ Thus $C^{(T)}$ is a joint two-time frequency matrix, not a row-stochastic transition matrix. If every $\pi_i^{(T)}>0$, the conditional transition estimator is $$\label{eq:conditional-matrix}
    K_T=D_T^{-1}C^{(T)},
    \qquad
    D_T=\operatorname{diag}(\pi_1^{(T)},\ldots,\pi_d^{(T)}),$$ and $K_T\mathbf 1=\mathbf 1$. In general $C^{(T)}$ and $K_T$ are not similar and do not have the same spectrum.

Because the $B_j$ form a partition, $$\sum_{j=1}^d\mathbf 1_{B_j}(x_{t+1})=1.$$ Summing [\[eq:joint-matrix\]](#eq:joint-matrix){reference-type="eqref" reference="eq:joint-matrix"} over $j$ proves [\[eq:joint-row-sum\]](#eq:joint-row-sum){reference-type="eqref" reference="eq:joint-row-sum"}. Equation [\[eq:conditional-matrix\]](#eq:conditional-matrix){reference-type="eqref" reference="eq:conditional-matrix"} then gives row sum one. Spectral equality fails already for $$C=\begin{pmatrix}0.4&0.1\\0.1&0.4\end{pmatrix},
    \qquad D=\tfrac12 I,
    \qquad K=D^{-1}C=2C:$$ $C$ has eigenvalues $0.5,0.3$, whereas $K$ has eigenvalues $1,0.6$.

[\[cor:four-objects\]]{#cor:four-objects label="cor:four-objects"} The joint count $C^{(T)}$, the row-normalized estimator $K_T$, the deterministic kernel average $T^{-1}\sum_{t<T}K(u_t)$, and the non-autonomous propagation product $K(u_{T-1})\cdots K(u_0)$ are generally four different matrices. A spectral statement about one does not transfer to another without an explicit theorem.

[\[prop:markov-not-unitary\]]{#prop:markov-not-unitary label="prop:markov-not-unitary"} Let $d\ge2$ and let $K\in\mathbb R^{d\times d}$ be row-stochastic with every entry strictly positive. Then $K$ is not unitary in the standard Euclidean inner product. Moreover, $1$ is a simple eigenvalue and every other eigenvalue satisfies $|\lambda|<1$.

If $K$ were unitary, its distinct rows would be orthogonal. The Euclidean inner product of any two strictly positive rows is strictly positive, a contradiction. The final assertions are the Perron--Frobenius theorem for a primitive stochastic matrix.

Gaussian-smoothed transition matrices at fixed grid size are therefore Markov resonance models rather than unitary evolution operators, and they do not by themselves define self-adjoint Hamiltonians. Their nonreal eigenvalues may have arguments, but those arguments are not automatically quantum energies.

[\[rem:conjugate\]]{#rem:conjugate label="rem:conjugate"} Every real matrix has a real characteristic polynomial, so $\lambda\in\operatorname{spec}K$ implies $\overline\lambda\in\operatorname{spec}K$. For a nonreal eigenvalue this produces principal arguments $\pm\theta$. This generic conjugacy does not by itself define a Hamiltonian particle-hole, chiral, or charge-conjugation symmetry, and $-\theta$ cannot be called a negative energy without an additional operator structure.

## Sorted upper-half-plane unwrapping

For $x\in\mathbb R$, let $\operatorname{wrap}(x)$ denote its representative in $(-\pi,\pi]$. Given principal phases $\theta_1,\ldots,\theta_m$, the standard recursive unwrapping rule is $$\label{eq:unwrap-recursion}
    \Phi_1=\theta_1,
    \qquad
    \Phi_j=\Phi_{j-1}+\operatorname{wrap}(\theta_j-\theta_{j-1}),
    \quad 2\le j\le m.$$

[\[prop:unwrap\]]{#prop:unwrap label="prop:unwrap"} If $$0<\theta_1\le\theta_2\le\cdots\le\theta_m<\pi,$$ then $$\label{eq:unwrap-identity}
    \Phi_j=\theta_j
    \qquad (1\le j\le m).$$ In particular, the recursion adds no winding information and its output remains in $(0,\pi)$.

For every $j\ge2$, $$0\le\theta_j-\theta_{j-1}<\pi.$$ Hence $\operatorname{wrap}(\theta_j-\theta_{j-1})=\theta_j-\theta_{j-1}$. Substitution into [\[eq:unwrap-recursion\]](#eq:unwrap-recursion){reference-type="eqref" reference="eq:unwrap-recursion"} gives $$\Phi_j
    =\theta_1+\sum_{k=2}^j(\theta_k-\theta_{k-1})
    =\theta_j.$$

[\[rem:ordering\]]{#rem:ordering label="rem:ordering"} Genuine phase unwrapping follows a continuously tracked eigenvalue branch as an external parameter varies. Sorting a static set of phases by size is not such a continuation. With a different arbitrary ordering, [\[eq:unwrap-recursion\]](#eq:unwrap-recursion){reference-type="eqref" reference="eq:unwrap-recursion"} can insert multiples of $2\pi$, but those integers then encode the chosen ordering rather than an intrinsic winding number. An unbounded energy coordinate therefore requires an independently defined branch-tracking or counting rule.

## Symmetric regression

Let $(x_j,y_j)\in\mathbb R^2$, $1\le j\le m$, with $\sum_jx_j^2>0$. Form the conjugate-symmetric data set $$\label{eq:symmetric-data}
    \mathcal D_\pm
    =\{(x_j,y_j),(-x_j,-y_j):1\le j\le m\}.$$

[\[prop:symmetric-regression\]]{#prop:symmetric-regression label="prop:symmetric-regression"} The ordinary least-squares minimizer of $$\sum_{(x,y)\in\mathcal D_\pm}(y-a x-b)^2$$ is $$\label{eq:symmetric-fit}
    b_*=0,
    \qquad
    a_*=\frac{\sum_{j=1}^m x_jy_j}{\sum_{j=1}^m x_j^2}.$$ Moreover, $$\label{eq:symmetric-sse}
    \min_{a,b}\sum_{(x,y)\in\mathcal D_\pm}(y-a x-b)^2
    =2\min_a\sum_{j=1}^m(y_j-a x_j)^2.$$ Thus a free-intercept fit on the doubled data is exactly a zero-intercept fit on the positive branch.

The sample means of both coordinates on $\mathcal D_\pm$ vanish. The least-squares normal equation for the intercept therefore gives $b_*=\overline y-a_*\overline x=0$. With $b=0$, the two residuals associated with index $j$ are $$y_j-a x_j,
    \qquad
    -y_j-a(-x_j)=-(y_j-a x_j),$$ so their squared sum is $2(y_j-a x_j)^2$. Minimization gives [\[eq:symmetric-fit\]](#eq:symmetric-fit){reference-type="eqref" reference="eq:symmetric-fit"} and [\[eq:symmetric-sse\]](#eq:symmetric-sse){reference-type="eqref" reference="eq:symmetric-sse"}.

[\[cor:zeroing\]]{#cor:zeroing label="cor:zeroing"} If the full-spectrum regression is formed only by duplicating the same positive phase-energy pairs through $(x,y)\mapsto(-x,-y)$ with equal weights, a fitted intercept $b=0$ is forced algebraically. It is not an independent dynamical prediction. A different slope or residual between the two procedures proves that some other part of the data selection, weighting, or pairing has also changed.

# The smooth zero envelope already gives relative accuracy {#sec:envelope}

Define the smooth Riemann--von Mangoldt main term $$\label{eq:F-def}
    F(T)=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right).$$ The zero-counting function satisfies the unconditional estimate [@Titchmarsh1986; @Edwards1974] $$\label{eq:RVM}
    N_\zeta(T)=F(T)+O(\log T).$$ The $O(\log T)$ term is deliberately sufficient here; no hypothesis about the real parts of the zeros is used.

Let $W$ be the principal Lambert function, characterized by $W(x)e^{W(x)}=x$ for $x>0$ [@CorlessEtAl1996], and put $$\label{eq:Gamma-def}
    \Gamma_n=\frac{2\pi n}{W(n/e)}.$$

[\[thm:smooth-zero\]]{#thm:smooth-zero label="thm:smooth-zero"} As $n\to\infty$, $$\label{eq:zero-O1}
    \gamma_n=\Gamma_n+O(1).$$ Consequently, $$\label{eq:zero-relative}
    \frac{|\gamma_n-\Gamma_n|}{\gamma_n}
    =O\left(\frac{\log n}{n}\right),$$ and $$\label{eq:mape-envelope}
    \frac1N\sum_{n=1}^N
    \frac{|\gamma_n-\Gamma_n|}{\gamma_n}
    =O\left(\frac{(\log N)^2}{N}\right).$$ The constants may absorb finitely many low-index zeros.

Write $w=W(n/e)$. Since $we^w=n/e$, $$\frac{\Gamma_n}{2\pi}=\frac{n}{w}=e^{w+1},
    \qquad
    \log\frac{\Gamma_n}{2\pi}-1=w.$$ Therefore $F(\Gamma_n)=n$ exactly.

The Riemann--von Mangoldt estimate gives $$\label{eq:F-gamma}
    F(\gamma_n)=n+O(\log\gamma_n),$$ where a possible jump caused by several zeros with the same ordinate is absorbed by the same error term. Indeed, if $$J(T)=N_\zeta(T)-N_\zeta(T^-),$$ then [\[eq:RVM\]](#eq:RVM){reference-type="eqref" reference="eq:RVM"} gives $$J(T)\le N_\zeta(T+1)-N_\zeta(T-1)=O(\log T).$$ Thus $N_\zeta(\gamma_n)=n+O(\log\gamma_n)$ regardless of the position of $n$ inside a multiplicity block, which proves [\[eq:F-gamma\]](#eq:F-gamma){reference-type="eqref" reference="eq:F-gamma"}. The standard first inversion of [\[eq:RVM\]](#eq:RVM){reference-type="eqref" reference="eq:RVM"} gives $$\gamma_n\asymp\Gamma_n\asymp\frac{n}{\log n}.$$ For large arguments, $$F'(T)=\frac1{2\pi}\log\frac{T}{2\pi}\asymp\log n$$ throughout the interval joining $\gamma_n$ and $\Gamma_n$. The mean-value theorem applied to [\[eq:F-gamma\]](#eq:F-gamma){reference-type="eqref" reference="eq:F-gamma"} and $F(\Gamma_n)=n$ yields [\[eq:zero-O1\]](#eq:zero-O1){reference-type="eqref" reference="eq:zero-O1"}. Since $\gamma_n\asymp n/\log n$, [\[eq:zero-relative\]](#eq:zero-relative){reference-type="eqref" reference="eq:zero-relative"} follows. Finally, $$\sum_{n\le N}\frac{\log(n+1)}{n}
    =O((\log N)^2),$$ which proves [\[eq:mape-envelope\]](#eq:mape-envelope){reference-type="eqref" reference="eq:mape-envelope"} after absorbing the initial terms.

[\[cor:raw-metrics\]]{#cor:raw-metrics label="cor:raw-metrics"} For the smooth null sequence $(\Gamma_n)$ in [\[eq:Gamma-def\]](#eq:Gamma-def){reference-type="eqref" reference="eq:Gamma-def"}, $$\label{eq:relative-l2}
    \frac{\sum_{n\le N}(\gamma_n-\Gamma_n)^2}
         {\sum_{n\le N}\gamma_n^2}
    \longrightarrow0.$$ The Pearson correlation of the two raw vectors $(\gamma_1,\ldots,\gamma_N)$ and $(\Gamma_1,\ldots,\Gamma_N)$ tends to $1$.

By [\[thm:smooth-zero\]](#thm:smooth-zero){reference-type="ref" reference="thm:smooth-zero"}, the numerator of [\[eq:relative-l2\]](#eq:relative-l2){reference-type="eqref" reference="eq:relative-l2"} is $O(N)$. On the other hand, summation of the regularly varying sequence $\gamma_n\sim2\pi n/\log n$ gives $$\sum_{n\le N}\gamma_n
      \sim\frac{\pi N^2}{\log N},
    \qquad
    \sum_{n\le N}\gamma_n^2
      \sim\frac{4\pi^2N^3}{3(\log N)^2}.$$ Consequently, with $\overline\gamma_N=N^{-1}\sum_{n\le N}\gamma_n$, $$\sum_{n\le N}(\gamma_n-\overline\gamma_N)^2
    \sim\frac{\pi^2N^3}{3(\log N)^2}.$$ Thus [\[eq:relative-l2\]](#eq:relative-l2){reference-type="eqref" reference="eq:relative-l2"} follows. If $e_n=\Gamma_n-\gamma_n$, then $\|e-\overline e\,\mathbf1\|_2=O(N^{1/2})$, while the centered norm of $(\gamma_n)_{n\le N}$ has order $N^{3/2}/\log N$. Their ratio is $O((\log N)/N)\to0$. Normalized centered vectors therefore approach one another, and their inner product, which is the Pearson correlation, tends to $1$.

[\[cor:relative-not-fluctuation\]]{#cor:relative-not-fluctuation label="cor:relative-not-fluctuation"} Every positive sequence $g_n$ satisfying $$g_n\sim\frac{2\pi n}{\log n}$$ also satisfies $g_n/\gamma_n\to1$. In particular, vanishing relative error, high raw correlation, or accurate macroscopic density can occur without encoding any individual zero fluctuation.

The Lambert asymptotic $W(n/e)\sim\log n$ and [\[thm:smooth-zero\]](#thm:smooth-zero){reference-type="ref" reference="thm:smooth-zero"} give $\gamma_n\sim2\pi n/\log n$. The conclusion follows by transitivity of asymptotic equivalence.

[\[rem:unfolding\]]{#rem:unfolding label="rem:unfolding"} To remove the effect in [\[cor:relative-not-fluctuation\]](#cor:relative-not-fluctuation){reference-type="ref" reference="cor:relative-not-fluctuation"}, one unfolds the ordinates using a smooth counting function, for example $$\overline N_\zeta(T)=F(T)+\frac78,
    \qquad
    \xi_n=\overline N_\zeta(\gamma_n),$$ and studies centered spacings or correlation functions of the $\xi_n$. Montgomery's pair-correlation framework is of this local type [@Montgomery1973]. A global affine fit and an unfolded local-statistics comparison answer different questions.

# Fixed-resolution operator freezing {#sec:freezing}

For the quadratic map $f_u(x)=1-u x^2$, fixed grid centers $c_1,\ldots,c_d$, and fixed Gaussian width $\sigma>0$, the smoothed row kernel used in the finite-resolution construction is $$\label{eq:gaussian-kernel}
    K_{ij}^{(d,\sigma)}(u)
    =\frac{\exp\left(-(c_j-f_u(c_i))^2/(2\sigma^2)\right)}
    {\sum_{k=1}^d\exp\left(-(c_k-f_u(c_i))^2/(2\sigma^2)\right)}.$$ Every entry is strictly positive and real analytic in $u$, and every row sums to one. Hence [\[prop:markov-not-unitary\]](#prop:markov-not-unitary){reference-type="ref" reference="prop:markov-not-unitary"} applies, and on every compact parameter interval the family is Lipschitz and differentiable to every order. The finite-dimensional instances of the results below therefore apply directly to [\[eq:gaussian-kernel\]](#eq:gaussian-kernel){reference-type="eqref" reference="eq:gaussian-kernel"}. They do not automatically identify its grid limit with a continuum transfer operator.

Let $\mathcal B$ be a complex Banach space. Let $A(u)\in\mathcal L(\mathcal B)$ be defined and uniformly bounded on a compact parameter interval containing the full schedule below; regularity assumptions will be imposed only near $u_{\mathrm c}$. For fixed $c>1$, $p>0$, and $\kappa\in\mathbb R$, consider $$\label{eq:log-schedule}
    u_n=u_{\mathrm c}+\delta_n,
    \qquad
    \delta_n=\frac{\kappa}{(\log(n+c))^p}
    +O\left(\frac1{(\log(n+c))^{p+1}}\right),$$ and define the long-exposure average $$\label{eq:operator-average}
    \overline A_T=\frac1T\sum_{n=1}^T A(u_n).$$

[\[lem:slow-average\]]{#lem:slow-average label="lem:slow-average"} For every $\alpha>0$ and fixed $c>1$, $$\label{eq:slow-average}
    \frac1T\sum_{n=1}^T\frac1{(\log(n+c))^\alpha}
    =\frac1{(\log T)^\alpha}
      \left(1+\frac{\alpha}{\log T}
      +O\left(\frac1{(\log T)^2}\right)\right).$$

The summand is positive and eventually decreasing, so the sum differs from the corresponding integral by $O(1)$. Integration by parts, or differentiation of $x(\log x)^{-\alpha}$, gives $$\int_2^T\frac{dx}{(\log x)^\alpha}
    =\frac{T}{(\log T)^\alpha}
      \left(1+\frac{\alpha}{\log T}
      +O\left(\frac1{(\log T)^2}\right)\right).$$ Replacing $x$ by $x+c$ changes only lower-order terms. Division by $T$ proves the claim.

[\[thm:holder-freezing\]]{#thm:holder-freezing label="thm:holder-freezing"} Assume that for some $L>0$ and $0<\eta\le1$, $$\label{eq:holder-family}
    \|A(u)-A(u_{\mathrm c})\|_{\mathcal L(\mathcal B)}
    \le L|u-u_{\mathrm c}|^\eta$$ near $u_{\mathrm c}$. Then $$\label{eq:freezing-rate}
    \|\overline A_T-A(u_{\mathrm c})\|_{\mathcal L(\mathcal B)}
    =O\left((\log T)^{-p\eta}\right).$$ Every fixed-resolution family continuous at $u_{\mathrm c}$ and bounded along the schedule freezes to its critical matrix by Cesàro convergence; the Hölder hypothesis gives the quantitative rate in [\[eq:freezing-rate\]](#eq:freezing-rate){reference-type="eqref" reference="eq:freezing-rate"}.

Choose $n_0$ so that [\[eq:holder-family\]](#eq:holder-family){reference-type="eqref" reference="eq:holder-family"} applies for every $n\ge n_0$. Uniform boundedness makes the finitely many earlier terms contribute $O(T^{-1})$. For the remaining terms, [\[eq:holder-family\]](#eq:holder-family){reference-type="eqref" reference="eq:holder-family"} gives $$\|\overline A_T-A(u_{\mathrm c})\|
    \le O(T^{-1})+\frac LT\sum_{n=n_0}^T|\delta_n|^\eta.$$ Equation [\[eq:log-schedule\]](#eq:log-schedule){reference-type="eqref" reference="eq:log-schedule"} gives $|\delta_n|^\eta=O((\log(n+c))^{-p\eta})$, and [\[lem:slow-average\]](#lem:slow-average){reference-type="ref" reference="lem:slow-average"} completes the proof.

The next result identifies the first-order limit at fixed resolution.

[\[thm:response\]]{#thm:response label="thm:response"} Assume that $A$ is Fréchet differentiable at $u_{\mathrm c}$ in operator norm: $$\label{eq:frechet}
    A(u_{\mathrm c}+t)=A(u_{\mathrm c})+tA'(u_{\mathrm c})+r(t),
    \qquad
    \frac{\|r(t)\|}{|t|}\longrightarrow0.$$ For the schedule [\[eq:log-schedule\]](#eq:log-schedule){reference-type="eqref" reference="eq:log-schedule"}, $$\label{eq:response-limit}
    (\log T)^p\bigl(\overline A_T-A(u_{\mathrm c})\bigr)
    \longrightarrow \kappa A'(u_{\mathrm c})$$ in operator norm.

Substitute [\[eq:frechet\]](#eq:frechet){reference-type="eqref" reference="eq:frechet"} into [\[eq:operator-average\]](#eq:operator-average){reference-type="eqref" reference="eq:operator-average"}: $$\label{eq:response-split}
    \overline A_T-A(u_{\mathrm c})
    =A'(u_{\mathrm c})\frac1T\sum_{n=1}^T\delta_n
     +\frac1T\sum_{n=1}^T r(\delta_n).$$ By [\[lem:slow-average\]](#lem:slow-average){reference-type="ref" reference="lem:slow-average"} and [\[eq:log-schedule\]](#eq:log-schedule){reference-type="eqref" reference="eq:log-schedule"}, $$\label{eq:delta-average}
    \frac1T\sum_{n=1}^T\delta_n
    =\frac{\kappa}{(\log T)^p}
     +O((\log T)^{-p-1}).$$ Fix $\varepsilon>0$. For all sufficiently large $n$, $\|r(\delta_n)\|\le\varepsilon|\delta_n|$. The finitely many remaining terms contribute $O(T^{-1})$, while [\[lem:slow-average\]](#lem:slow-average){reference-type="ref" reference="lem:slow-average"} gives $$\frac1T\sum_{n=1}^T\|r(\delta_n)\|
    \le o((\log T)^{-p})+O(T^{-1}).$$ Multiplying [\[eq:response-split\]](#eq:response-split){reference-type="eqref" reference="eq:response-split"} by $(\log T)^p$ proves [\[eq:response-limit\]](#eq:response-limit){reference-type="eqref" reference="eq:response-limit"}.

[\[prop:second-response\]]{#prop:second-response label="prop:second-response"} Assume $\kappa\ne0$ and that $A$ is twice Fréchet differentiable at $u_{\mathrm c}$: $$A(u_{\mathrm c}+t)=A(u_{\mathrm c})+tA'(u_{\mathrm c})
      +\frac{t^2}{2}A''(u_{\mathrm c})+o(t^2).$$ Write $\overline\delta_T=T^{-1}\sum_{n\le T}\delta_n$. Then $$\label{eq:second-response}
    (\log T)^{2p}
    \left(\overline A_T-A(u_{\mathrm c})-\overline\delta_TA'(u_{\mathrm c})\right)
    \longrightarrow \frac{\kappa^2}{2}A''(u_{\mathrm c}).$$ Here $A''(u_{\mathrm c})$ denotes the scalar-parameter second derivative $D^2A(u_{\mathrm c})[1,1]$.

Average the second-order expansion. The square average satisfies $$\frac1T\sum_{n=1}^T\delta_n^2
    =\frac{\kappa^2+o(1)}{(\log T)^{2p}}$$ by [\[lem:slow-average\]](#lem:slow-average){reference-type="ref" reference="lem:slow-average"}. The averaged $o(\delta_n^2)$ remainder is $o((\log T)^{-2p})$ by the same finite-initial-segment argument used in [\[thm:response\]](#thm:response){reference-type="ref" reference="thm:response"}. This gives [\[eq:second-response\]](#eq:second-response){reference-type="eqref" reference="eq:second-response"}.

[\[prop:anchored\]]{#prop:anchored label="prop:anchored"} For a triangular schedule ending exactly at $u_{\mathrm c}$, $$\label{eq:anchored-schedule}
    u_{n,T}=u_{\mathrm c}+\kappa\left[
      \frac1{(\log(n+c))^p}
      -\frac1{(\log(T+c))^p}
    \right],
    \qquad 1\le n\le T,$$ one has $$\label{eq:anchored-mean}
    \frac1T\sum_{n=1}^T(u_{n,T}-u_{\mathrm c})
    =\frac{p\kappa+o(1)}{(\log T)^{p+1}}.$$ If $A$ is Lipschitz at $u_{\mathrm c}$, its average freezes at rate $O((\log T)^{-p-1})$; if $A$ is differentiable, then $$\label{eq:anchored-response}
    (\log T)^{p+1}
    \left(\frac1T\sum_{n=1}^T A(u_{n,T})-A(u_{\mathrm c})\right)
    \longrightarrow p\kappa A'(u_{\mathrm c}).$$ For $p=2$, the anchored rate is $(\log T)^{-3}$ rather than $(\log T)^{-2}$.

Subtract $(\log(T+c))^{-p}$ from both sides of [\[eq:slow-average\]](#eq:slow-average){reference-type="eqref" reference="eq:slow-average"}. The leading terms cancel and leave [\[eq:anchored-mean\]](#eq:anchored-mean){reference-type="eqref" reference="eq:anchored-mean"}. Since the bracket in [\[eq:anchored-schedule\]](#eq:anchored-schedule){reference-type="eqref" reference="eq:anchored-schedule"} has a fixed sign over $1\le n\le T$, the same asymptotic controls the average absolute displacement. The Lipschitz assertion follows as in [\[thm:holder-freezing\]](#thm:holder-freezing){reference-type="ref" reference="thm:holder-freezing"}; the differentiable assertion follows as in [\[thm:response\]](#thm:response){reference-type="ref" reference="thm:response"}.

[\[rem:p2\]]{#rem:p2 label="rem:p2"} One unanchored schedule in the quadratic model has $p=2$ and an additional $(\log n)^{-3}$ correction. At fixed resolution, [\[thm:response\]](#thm:response){reference-type="ref" reference="thm:response"} gives $$(\log T)^2(\overline A_T-A(u_{\mathrm c}))\longrightarrow\kappa_1A'(u_{\mathrm c}).$$ The coefficient of the $(\log n)^{-3}$ term does not enter this leading limit. More precisely, for $\delta_n=\kappa_1(\log(n+c))^{-2}+\kappa_2(\log(n+c))^{-3}$, $$\overline\delta_T
    =\frac{\kappa_1}{(\log T)^2}
     +\frac{2\kappa_1+\kappa_2}{(\log T)^3}
     +O((\log T)^{-4}).$$ Thus the unscaled matrix loses the drive, while the leading rescaled matrix retains one derivative and one scalar coefficient. After subtracting the exact mean linear response, [\[prop:second-response\]](#prop:second-response){reference-type="ref" reference="prop:second-response"} gives a $(\log T)^4$ second-derivative limit. These limits form a Taylor jet of the fixed critical matrix, not a newly generated infinite spectrum.

## Simple eigenvalues and phases

We now specialize to $A(u)\in\mathbb C^{d\times d}$ with fixed $d$. Let $\lambda_0\ne0$ be a simple eigenvalue of $A(u_{\mathrm c})$, with right and left eigenvectors $r_0$ and $\ell_0$ normalized by $\ell_0^*r_0=1$.

[\[cor:eigen-response\]]{#cor:eigen-response label="cor:eigen-response"} Under the hypotheses of [\[thm:response\]](#thm:response){reference-type="ref" reference="thm:response"}, for all sufficiently large $T$ a fixed isolating disk around $\lambda_0$ contains exactly one eigenvalue of $\overline A_T$, counted with algebraic multiplicity; denote it by $\lambda_T$. Then $$\label{eq:eigen-response}
    (\log T)^p(\lambda_T-\lambda_0)
    \longrightarrow
    \kappa\,\ell_0^*A'(u_{\mathrm c})r_0.$$ For a continuous choice of argument near $\lambda_0$, $$\label{eq:phase-response}
    (\log T)^p\bigl(\operatorname{Arg}\lambda_T-\operatorname{Arg}\lambda_0\bigr)
    \longrightarrow
    \kappa\,\operatorname{Im}
    \left(\frac{\ell_0^*A'(u_{\mathrm c})r_0}{\lambda_0}\right).$$

The first-order perturbation formula for a simple eigenvalue [@Kato1995] gives $$\lambda_T-\lambda_0
    =\ell_0^*(\overline A_T-A(u_{\mathrm c}))r_0
     +o(\|\overline A_T-A(u_{\mathrm c})\|).$$ Combine this with [\[thm:response\]](#thm:response){reference-type="ref" reference="thm:response"} to obtain [\[eq:eigen-response\]](#eq:eigen-response){reference-type="eqref" reference="eq:eigen-response"}. Since $d\operatorname{Arg}z=\operatorname{Im}(dz/z)$ away from zero, [\[eq:phase-response\]](#eq:phase-response){reference-type="eqref" reference="eq:phase-response"} follows.

[\[cor:no-square-root\]]{#cor:no-square-root label="cor:no-square-root"} If a fixed-resolution matrix family $A(u)$ is analytic and $\lambda_0\ne0$ is simple at $u=u_{\mathrm c}$, then its local eigenvalue and eigenphase branches are analytic and $$\lambda(u)-\lambda_0=O(|u-u_{\mathrm c}|),
    \qquad
    \operatorname{Arg}\lambda(u)-\operatorname{Arg}\lambda_0=O(|u-u_{\mathrm c}|).$$ A square-root law in $u-u_{\mathrm c}$ requires a separately verified defective collision or another singular mechanism; it does not follow merely from the quadratic critical point of the state-space map.

Analytic perturbation theory for a simple isolated eigenvalue gives an analytic eigenvalue branch. The argument is analytic after choosing a local branch away from zero. The stated estimates are their first Taylor bounds.

[\[cor:fixed-dimension\]]{#cor:fixed-dimension label="cor:fixed-dimension"} A fixed $d\times d$ long-exposure matrix has at most $d$ eigenvalues, and by [\[thm:holder-freezing\]](#thm:holder-freezing){reference-type="ref" reference="thm:holder-freezing"} each limiting spectral cluster is determined by $A(u_{\mathrm c})$. It cannot, without an external repetition or relabeling rule, provide a one-to-one asymptotic realization of the unbounded sequence $(\gamma_n)$. Within the finite-matrix discretization architecture, such a proposal requires $d=d(T)\to\infty$; alternatively, one must construct and analyze a genuinely infinite-dimensional operator directly.

## The required double-limit control

Let $A_\varepsilon(u)$ be a discretized family, embedded in a common operator space, and let $P_{u_{\mathrm c}}$ be a proposed continuum limit. Put $s_T=(\log T)^{-p}$.

[\[prop:double-limit\]]{#prop:double-limit label="prop:double-limit"} Assume the families are uniformly bounded on the parameter interval traversed by the schedule. Assume also, uniformly along a choice $\varepsilon=\varepsilon(T)\to0$, that $$\begin{aligned}
    A_\varepsilon(u_{\mathrm c}+t)
      &=A_\varepsilon(u_{\mathrm c})+tA_\varepsilon'(u_{\mathrm c})+r_\varepsilon(t),
      &\lim_{h\downarrow0}\ \sup_\varepsilon\ \sup_{0<|t|\le h}
       \frac{\|r_\varepsilon(t)\|}{|t|}&=0,
      \label{eq:uniform-diff}\\
    \|A_\varepsilon(u_{\mathrm c})-P_{u_{\mathrm c}}\|&=o(s_T),
      &\|A_\varepsilon'(u_{\mathrm c})-D\|&=o(1).
      \label{eq:double-errors}\end{aligned}$$ Then $$\label{eq:double-limit}
    s_T^{-1}\bigl(\overline A_{\varepsilon(T),T}-P_{u_{\mathrm c}}\bigr)
    \longrightarrow\kappa D.$$ Conversely, an $O(s_T)$ or larger discretization bias may contribute to, or dominate, the proposed renormalized response.

Apply the proof of [\[thm:response\]](#thm:response){reference-type="ref" reference="thm:response"} uniformly to $A_{\varepsilon(T)}$. Uniform boundedness makes every fixed initial segment contribute $O(T^{-1})$, and [\[eq:uniform-diff\]](#eq:uniform-diff){reference-type="eqref" reference="eq:uniform-diff"} controls the remaining averaged Taylor remainders. It gives $$\overline A_{\varepsilon(T),T}-A_{\varepsilon(T)}(u_{\mathrm c})
    =\kappa s_T A_{\varepsilon(T)}'(u_{\mathrm c})+o(s_T).$$ Add $A_{\varepsilon(T)}(u_{\mathrm c})-P_{u_{\mathrm c}}$, divide by $s_T$, and use [\[eq:double-errors\]](#eq:double-errors){reference-type="eqref" reference="eq:double-errors"}.

[\[rem:empirical\]]{#rem:empirical label="rem:empirical"} Theorems [\[thm:holder-freezing\]](#thm:holder-freezing){reference-type="ref" reference="thm:holder-freezing"}--[\[prop:double-limit\]](#prop:double-limit){reference-type="ref" reference="prop:double-limit"} concern the deterministic average $T^{-1}\sum_n A(u_n)$. The row-normalized estimator from one non-autonomous trajectory is instead $$\widehat K_{ij,T}
    =\frac{\sum_{t=0}^{T-1}
      \mathbf1_{B_i}(x_t)\mathbf1_{B_j}(x_{t+1})}
    {\sum_{t=0}^{T-1}\mathbf1_{B_i}(x_t)},$$ when the denominator is nonzero. Its rows weight times according to source-bin occupation, so even an ideal noiseless limit need not equal the unweighted kernel average $\overline A_T$. One first needs lower bounds on source counts and a theorem identifying the deterministic target of $\widehat K_T$ with $\overline A_T$, or else with an explicitly occupation-weighted alternative. Only after that identification does the triangle inequality give $$\|\widehat K_T-A(u_{\mathrm c})\|
    \le \|\widehat K_T-\overline A_T\|
       +\|\overline A_T-A(u_{\mathrm c})\|.$$ To inherit [\[eq:response-limit\]](#eq:response-limit){reference-type="eqref" reference="eq:response-limit"}, one needs the stronger estimate $\|\widehat K_T-\overline A_T\|=o((\log T)^{-p})$. This includes deterministic occupation bias as well as sampling error and is a sequential memory-loss problem, not a consequence of pointwise matrix continuity. The parity-resolved two-step architecture in @WangParity2026 identifies appropriate abstract hypotheses but does not assert them for every quadratic logarithmic schedule.

# The area-preserving lift and a quartic Weyl-law obstruction {#sec:weyl}

The area-preserving recurrence considered in @WangHenon2026, in the quadratic family introduced by @Henon1969, is $$\label{eq:henon-recurrence}
    x_{n+1}=1-a x_n^2-x_{n-1}.$$ As a map of the plane it is $$\label{eq:henon-map}
    F_a(x,y)=(1-a x^2-y,x).$$ Its conservative structure is exact, not numerical.

[\[prop:henon-structure\]]{#prop:henon-structure label="prop:henon-structure"} The map $F_a$ preserves $dx\wedge dy$ and is reversible under $R(x,y)=(y,x)$: $$\label{eq:reversibility}
    \det DF_a=1,
    \qquad
    RF_aR=F_a^{-1}.$$ It is generated by $$\label{eq:generating-function}
    S_a(x,X)=xX+\frac a3x^3-x,$$ in the convention $y=-\partial_xS_a$ and $Y=\partial_XS_a$.

Direct differentiation gives $$DF_a(x,y)=
    \begin{pmatrix}-2ax&-1\\1&0\end{pmatrix},
    \qquad \det DF_a=1.$$ Solving $(X,Y)=F_a(x,y)$ for $(x,y)$ gives $F_a^{-1}(X,Y)=(Y,1-aY^2-X)=RF_aR(X,Y)$. Finally, $$-\partial_xS_a=1-a x^2-X=y,
    \qquad
    \partial_XS_a=x=Y,$$ which is equivalent to [\[eq:henon-map\]](#eq:henon-map){reference-type="eqref" reference="eq:henon-map"}. Moreover, $$dS_a=-y\,dx+Y\,dX,
    \qquad
    F_a^*(Y\,dX)-y\,dx=dS_a,$$ which makes exact symplecticity explicit.

[\[rem:fio\]]{#rem:fio label="rem:fio"} Equation [\[eq:generating-function\]](#eq:generating-function){reference-type="eqref" reference="eq:generating-function"} yields the Fourier integral operator $$\label{eq:fio}
    (U_{a,\hbar}\psi)(X)
    =\frac1{\sqrt{2\pi\hbar}}
      \int_{\mathbb R}e^{iS_a(x,X)/\hbar}\psi(x)\,dx.$$ It is unitary on $L^2(\mathbb R)$ because it is a semiclassical inverse Fourier transform composed with multiplication by the unit-modulus factor $\exp(i(a x^3/3-x)/\hbar)$. This is a natural quantization of the exact map, but no discrete Riemann-zero spectrum follows from unitarity alone.

[\[prop:quartic-changes-map\]]{#prop:quartic-changes-map label="prop:quartic-changes-map"} Put $v_n=x_n-x_{n-1}$ and $$V_{a,\lambda}(q)=-q+q^2+\frac a3q^3+\lambda q^4.$$ The kick--drift equations $$v_{n+1}=v_n-V_{a,\lambda}'(x_n),
    \qquad x_{n+1}=x_n+v_{n+1}$$ reduce for $\lambda=0$ to [\[eq:henon-recurrence\]](#eq:henon-recurrence){reference-type="eqref" reference="eq:henon-recurrence"}. For $\lambda>0$ they instead give $$\label{eq:modified-henon}
    x_{n+1}=1-a x_n^2-x_{n-1}-4\lambda x_n^3.$$ Thus quartic confinement is mathematically useful, but it is not a dynamically neutral regularization of the original quadratic Hénon map.

Since $V_{a,\lambda}'(q)=-1+2q+a q^2+4\lambda q^3$, $$v_{n+1}=v_n+1-2x_n-a x_n^2-4\lambda x_n^3.$$ Substitute $v_n=x_n-x_{n-1}$ into $x_{n+1}=x_n+v_{n+1}$ to obtain [\[eq:modified-henon\]](#eq:modified-henon){reference-type="eqref" reference="eq:modified-henon"}.

The continuum approximation in @WangHenon2026 instead introduces a confining Schrödinger Hamiltonian. We analyze that separate operator. Let $$\label{eq:quartic-potential}
    V(q)=c_4q^4+c_3q^3+c_2q^2+c_1q+c_0,
    \qquad c_4>0,$$ and $$\label{eq:schrodinger}
    H=-\frac{\hbar^2}{2m}\frac{d^2}{dq^2}+V(q)$$ on $L^2(\mathbb R)$, with $m,\hbar>0$. The model potential is the case $m=1$ and $V(q)=0.05q^4+(1.02/3)q^3+q^2-q$.

[\[thm:quartic-weyl\]]{#thm:quartic-weyl label="thm:quartic-weyl"} The closure of [\[eq:schrodinger\]](#eq:schrodinger){reference-type="eqref" reference="eq:schrodinger"} initially defined on $C_c^\infty(\mathbb R)$ is self-adjoint, bounded below, and has compact resolvent. If $N_H(E)$ counts its eigenvalues not exceeding $E$, with multiplicity, then $$\label{eq:quartic-weyl}
    N_H(E)\sim C_{m,\hbar,c_4}E^{3/4},
    \qquad E\to\infty,$$ where $$\label{eq:weyl-constant}
    C_{m,\hbar,c_4}
    =\frac{\sqrt{2m}}{\pi\hbar}\,c_4^{-1/4}
      \int_{-1}^{1}\sqrt{1-t^4}\,dt.$$ Equivalently, if $\lambda_n(H)$ is the increasing eigenvalue sequence, $$\label{eq:quartic-eigen-asymptotic}
    \lambda_n(H)\sim
    \left(\frac{n}{C_{m,\hbar,c_4}}\right)^{4/3}.$$

Since $V$ is a real polynomial, is bounded below, and satisfies $V(q)\to+\infty$ as $|q|\to\infty$, the standard one-dimensional Schrödinger theory gives essential self-adjointness and semiboundedness on $C_c^\infty(\mathbb R)$; its closure has compact resolvent [@ReedSimonIV1978]. The one-dimensional Weyl formula [@Rozenblum1974] is $$\label{eq:phase-volume}
    N_H(E)
    \sim\frac1{2\pi\hbar}
    \operatorname{vol}\left\{(q,p):\frac{p^2}{2m}+V(q)\le E\right\}
    =\frac{\sqrt{2m}}{\pi\hbar}
      \int_{V(q)<E}\sqrt{E-V(q)}\,dq.$$ Set $q=(E/c_4)^{1/4}t$. On bounded $t$-sets, $$E^{-1}V((E/c_4)^{1/4}t)=t^4+O(E^{-1/4}),$$ and the scaled turning points converge to $-1$ and $1$. Dominated convergence in [\[eq:phase-volume\]](#eq:phase-volume){reference-type="eqref" reference="eq:phase-volume"} gives $$\int_{V(q)<E}\sqrt{E-V(q)}\,dq
    \sim c_4^{-1/4}E^{3/4}
          \int_{-1}^{1}\sqrt{1-t^4}\,dt,$$ which proves [\[eq:quartic-weyl\]](#eq:quartic-weyl){reference-type="eqref" reference="eq:quartic-weyl"}. Monotone inversion yields [\[eq:quartic-eigen-asymptotic\]](#eq:quartic-eigen-asymptotic){reference-type="eqref" reference="eq:quartic-eigen-asymptotic"}.

[\[cor:weyl-obstruction\]]{#cor:weyl-obstruction label="cor:weyl-obstruction"} For every fixed $\alpha>0$ and $\beta\in\mathbb R$, $$\label{eq:ratio-diverges}
    \frac{\alpha\lambda_n(H)+\beta}{\gamma_n}
    \longrightarrow+\infty.$$ Equivalently, $$\label{eq:counting-ratio}
    \frac{N_{\alpha H+\beta}(T)}{N_\zeta(T)}
    \sim 2\pi C_{m,\hbar,c_4}\alpha^{-3/4}
       \frac{T^{-1/4}}{\log T}
    \longrightarrow0.$$ Thus no fixed affine change of energy can make the quartic Hamiltonian counting law asymptotic to the Riemann--von Mangoldt counting law.

By [\[thm:smooth-zero,thm:quartic-weyl\]](#thm:smooth-zero,thm:quartic-weyl){reference-type="ref" reference="thm:smooth-zero,thm:quartic-weyl"}, $$\lambda_n(H)\asymp n^{4/3},
    \qquad
    \gamma_n\asymp\frac{n}{\log n}.$$ Their ratio is therefore bounded below and above by constant multiples of $n^{1/3}\log n$, which tends to infinity. This proves [\[eq:ratio-diverges\]](#eq:ratio-diverges){reference-type="eqref" reference="eq:ratio-diverges"}. The equivalent counting-law statement compares $E^{3/4}$ with $E\log E$. More explicitly, $$N_{\alpha H+\beta}(T)
    =N_H\left(\frac{T-\beta}{\alpha}\right)
    \sim C_{m,\hbar,c_4}\alpha^{-3/4}T^{3/4},$$ and division by [\[eq:RVM\]](#eq:RVM){reference-type="eqref" reference="eq:RVM"} proves [\[eq:counting-ratio\]](#eq:counting-ratio){reference-type="eqref" reference="eq:counting-ratio"}.

[\[rem:weyl-scope\]]{#rem:weyl-scope label="rem:weyl-scope"} The corollary applies to the quartic-regularized continuum Hamiltonian [\[eq:schrodinger\]](#eq:schrodinger){reference-type="eqref" reference="eq:schrodinger"}. It does not rule out every quantization of the Hénon map, every energy-dependent change of variables, or an unrelated Hilbert--Pólya construction. In particular, the unitary operator [\[eq:fio\]](#eq:fio){reference-type="eqref" reference="eq:fio"} is not the same operator as [\[eq:schrodinger\]](#eq:schrodinger){reference-type="eqref" reference="eq:schrodinger"}. What is ruled out is any high-energy identification for this fixed quartic regularization under a fixed affine scale.

[\[rem:box\]]{#rem:box label="rem:box"} If the Schrödinger operator is instead placed on a fixed periodic box $[-L,L)$, the potential is bounded on that box and the high-energy law is $$N_{H,L}(E)\sim
    \frac{2L\sqrt{2m}}{\pi\hbar}E^{1/2}.$$ If the grid dimension is also fixed, there are only finitely many matrix eigenvalues and no high-energy limit at all. The full-line quartic operator, fixed-box operator, and finite FFT matrix are therefore three distinct spectral objects; none has the $E\log E$ zero-counting law.

# What a nontrivial spectral bridge must retain {#sec:criteria}

The preceding results suggest a precise replacement for raw spectral matching. The replacement is not a theorem that the Riemann zeros arise from quadratic dynamics; it is a set of mathematical conditions under which such a claim would become nontrivial and testable.

[\[crit:target-free\]]{#crit:target-free label="crit:target-free"} Parameters used to construct the operator must be fixed independently of the zero ordinates on which the claim is evaluated. A low-index anchor may define units, but optimization on the same target list must be reported as a fit, with held-out levels or an arithmetic-free null model. Otherwise operator construction and validation are not logically separated.

[\[crit:objects\]]{#crit:objects label="crit:objects"} The comparison must specify whether it concerns Markov resonances, Koopman spectral measures, unitary eigenphases, or self-adjoint energies. Unitary eigenphases are defined modulo $2\pi$, and a principal-branch representative is bounded. Comparison with an unbounded real sequence therefore requires a separately defined effective self-adjoint generator or an intrinsic and controlled branch-lifting rule. Markov eigenvalues inside the unit disk are not Hermitian energies.

[\[crit:center\]]{#crit:center label="crit:center"} Centering must respect the spectral object. For operator response, use $\overline A_T-A(u_{\mathrm c})$. For an observable spectral measure, separate the mean atom and any deterministic parity atom at frequency $1/2$ [@WangParity2026]. For an energy list, unfold by an independently specified smooth counting function. On the arithmetic side, subtract the Riemann--von Mangoldt mean or unfold by $\overline N_\zeta$. Only like residual objects should enter a claim of arithmetic specificity.

[\[crit:double\]]{#crit:double label="crit:double"} If $T\to\infty$ and the resolution grows, specify a path $\varepsilon(T)\to0$ and prove an analogue of [\[eq:uniform-diff\]](#eq:uniform-diff){reference-type="eqref" reference="eq:uniform-diff"}--[\[eq:double-errors\]](#eq:double-errors){reference-type="eqref" reference="eq:double-errors"}. At the $p=2$ response scale, the critical discretization bias must be $o((\log T)^{-2})$. Grid refinement without a quantitative relation to observation time leaves the limiting spectrum undefined.

[\[crit:order\]]{#crit:order label="crit:order"} The average $T^{-1}\sum A(u_n)$ forgets the order of the operators and, by [\[thm:response\]](#thm:response){reference-type="ref" reference="thm:response"}, retains only a first derivative at leading scale. Arithmetic fluctuations, if present in the drive, require an order-sensitive object such as a controlled product cocycle, a correlation function, or a trace formula. Near the band-merging parameter, the primitive sequential object is the parity-preserving two-step block rather than an uncorrected one-step product [@WangParity2026].

[\[crit:rh\]]{#crit:rh label="crit:rh"} Any statement intended to imply the Riemann hypothesis must go beyond the preceding statistical criteria. It must construct a natural self-adjoint operator $H$ and prove, with multiplicity and completeness, $$\{\rho:\zeta(\rho)=0,\ 0<\operatorname{Re}\rho<1\}
    =\left\{\frac12\pm i\lambda:
      \lambda\in\operatorname{spec}(H)\right\}.$$ None of the finite fits, counting asymptotics, or response limits in this paper meets that standard.

The criteria can be summarized by the following flow: $$\begin{aligned}
&\text{raw finite phases and ordinates}\\[-0.1em]
&\quad\xrightarrow{\text{subtract symmetry and smooth means}}
  \text{centered, unfolded fluctuations}\\[0.2em]
&\quad\xrightarrow{\text{control }T\to\infty,\ \varepsilon\to0}
  \text{limiting spectral statistic or cocycle}\\[0.2em]
&\quad\xrightarrow{\text{new theorem, not assumed here}}
  \text{arithmetic correspondence}.
\end{aligned}$$ The first two arrows are mathematical normalization and limiting problems. The final arrow is the genuinely open bridge.

# Discussion {#sec:discussion}

## What remains valid in the numerical studies

The exact results above do not invalidate finite numerical computations. A finite transition matrix can have reproducible complex eigenvalues and eigenvalue arguments; a Hénon solver can exhibit level repulsion; and a fitted list can approximate low-lying ordinates. The conclusions change at the level of interpretation:

-   a sorted upper-half-plane unwrap is a relabeling identity, not a recovered winding number;

-   a zero intercept from conjugate doubling is a symmetry constraint, not a new prediction;

-   small percentage error at high index can be supplied by the smooth zero count;

-   a fixed-resolution long-exposure matrix approaches the critical matrix and has only derivative-level information after rescaling;

-   a confining quartic Hamiltonian may fit a finite window, but its asymptotic density cannot be the Riemann-zero density.

These statements turn qualitative cautions into exact propositions and indicate which plots require new null comparisons.

## The positive role of renormalization

Operator freezing is not merely a negative result. It identifies the natural first scale: $$\mathcal R_T=(\log T)^p(\overline A_T-A(u_{\mathrm c})).$$ At fixed resolution, $\mathcal R_T\to\kappa A'(u_{\mathrm c})$. This gives a reproducible response observable and a quantitative benchmark for discretization. If a future construction produces residual fluctuations beyond this derivative after target-independent calibration and controlled grid refinement, those residuals cannot be attributed to the leading logarithmic drift alone.

For continuum transfer operators of quadratic maps, differentiability is delicate because critical orbits and inverse branches move with the parameter. Hölder strong-to-weak stability may be available even when ordinary linear response fails [@KellerLiverani1999; @Baladi2014]. Accordingly, [\[thm:holder-freezing\]](#thm:holder-freezing){reference-type="ref" reference="thm:holder-freezing"} and [\[thm:response\]](#thm:response){reference-type="ref" reference="thm:response"} are deliberately separated: the first needs only Hölder continuity, while the second states the additional differentiability needed for a derivative limit.

## Relation to the prime-dynamics program

The prime-sieve results and the present zero-spectrum analysis concern different spectral objects. The centered, energy-normalized periodogram of the prime indicator converges weakly to Haar measure [@WangPrimeSpectrum2026]; the band-merging observable spectrum can also contain a deterministic atom at frequency $1/2$ [@WangParity2026]. Neither measure is the list of Riemann-zero ordinates. Their value is foundational: they show exactly which dynamical and Fourier statements follow from the sieve construction before a zeta-zero bridge is proposed.

A plausible next mathematical target is therefore not another raw affine fit. It is an order-sensitive, parity-resolved cocycle or trace formula whose centered fluctuation can be compared with unfolded zero statistics under a joint long-time and continuum limit. Constructing such an object remains open.

# Conclusion

We have proved several exact algebraic and asymptotic obstructions, together with a hierarchy of renormalized response theorems for quadratic spectral models. Joint pair occupation is not conditional transition; sorted upper-half-plane unwrapping telescopes; conjugate-symmetric regression forces its own zero intercept; the Riemann--von Mangoldt envelope already yields vanishing relative error; and a fixed quartic Schrödinger regularization has a counting exponent incompatible with the zeta zeros. Meanwhile, logarithmically driven fixed-resolution operator averages freeze at the limiting critical operator and, when the corresponding operator-norm derivatives exist, have first- and second-order responses governed by those derivatives.

The appropriate theoretical program is therefore narrower and more precise than a raw claim of spectral isomorphism. One must remove the smooth arithmetic count and deterministic dynamical modes, control the resolution-time double limit, retain operator order, and compare like spectral objects. These steps advance the analysis toward a falsifiable spectral bridge while making no claim about the truth of the Riemann hypothesis.

# Data and code availability {#data-and-code-availability .unnumbered}

This paper is theoretical and introduces no new numerical data. Its source files and compiled manuscript are available at <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-4-spectral-obstructions-renormalized-limits>.

# Acknowledgments {#acknowledgments .unnumbered}

The author acknowledges the use of an AI language model for assistance with mathematical cross-checking, manuscript organization, and typesetting. The author verified the final arguments and assumes responsibility for the content.
