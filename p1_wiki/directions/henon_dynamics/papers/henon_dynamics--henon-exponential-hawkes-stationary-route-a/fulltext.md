---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-exponential-hawkes-stationary-route-a"
canonical_tex: "henon_dynamics/henon_exponential_hawkes_stationary_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_exponential_hawkes_stationary_route_a/paper/main.pdf"
source_sha256: "4bf04900943f12b180af9f0399fc13cc207958c01a08e5a0262959db31b767f6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Affine Transforms, Three Covariances, and Borel Clusters of an Exponential Hawkes Process

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_exponential_hawkes_stationary_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_exponential_hawkes_stationary_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_exponential_hawkes_stationary_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_exponential_hawkes_stationary_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the exponential Hawkes process, we close the joint count--intensity transform, the stationary intensity law, and a triangular recurrence for all moments. The subcritical condition is treated together with its parameter faces.\>0 We then separate intensity covariance, complete counting covariance (including its Dirac atom), and the Bartlett spectrum under a frozen Fourier convention, obtaining exact window-count variance. \>1 Finally, the Poisson genealogy gives the Borel total cluster law, and an executable certificate audits every stated boundary. All results are source-local; no arithmetic or target spectral data enter.
author:
- 'Route-A source-local certificate HCS-C265'
date: 31 August 2026
title: |
  Affine Transforms, Three Covariances, and Borel Clusters\
  of an Exponential Hawkes Process
```

## Markdown 正文

trailerid \[\<C2652026083100000000000000000000\>\<C2652026083100000000000000000000\>\]

# The predictable Markov owner

Let $b>0$, $a,\nu\geq0$, and let $N$ be a simple point process whose predictable event rate is the left limit $\lambda_{t-}$, where $$\,\mathrm d\lambda_t=-b(\lambda_t-\nu)\,\mathrm dt+a\,\mathrm dN_t.       \tag{1}$$ Thus an event is sampled with the pre-jump intensity, then raises the post-jump intensity by $a$. Its Markov generator is $$\mathcal Gf(x)=b(\nu-x)f'(x)+x\{f(x+a)-f(x)\}.       \tag{2}$$ This convention prevents the common but consequential confusion between $\lambda_{t-}$ and $\lambda_t$ at an event.

For $0\leq z\leq1$, $s\geq0$, and $\lambda_0=x$, $$\mathbb E_x\!\left[z^{N_t-N_0}e^{-s\lambda_t}\right]
   =e^{-A_t-B_tx},                                    \tag{3}$$ where $B_0=s$, $A_0=0$, and $$B'_t=1-bB_t-ze^{-aB_t},\qquad A'_t=b\nu B_t.         \tag{4}$$

In the backward equation, a jump multiplies the transform by $z$. Substituting $F(t,x)=e^{-A_t-B_tx}$ into (2), with $f(x+a)$ replaced by $zf(x+a)$, gives constant coefficient $-b\nu B_t$ and $x$-coefficient $bB_t+ze^{-aB_t}-1$. Equating these with $-A'_t-B'_tx$ proves (4). The transform is bounded on the stated parameter domain, so localization and bounded convergence close the calculation.

# Stationarity, Laplace law, and every moment

Suppose first that $a<b$, set $\delta=b-a$, and put $\mu=b\nu/\delta$. The excitation kernel is $h(t)=ae^{-bt}{\bf1}_{t>0}$ and has mass $a/b<1$.

For $\nu>0$ there is a unique finite-intensity stationary Hawkes law. Its intensity Laplace transform $L(s)=\mathbb Ee^{-s\lambda}$ is the unique normalized solution $$\frac{L'(s)}{L(s)}=
 -\frac{b\nu s}{bs+e^{-as}-1},\qquad L(0)=1.          \tag{5}$$ Writing $m_n=\mathbb E\lambda^n$ and $m_0=1$, every moment is finite and $$m_n=\frac{nb\nu m_{n-1}+\displaystyle\sum_{k=0}^{n-2}
 \binom{n}{k}a^{n-k}m_{k+1}}{n\delta},\qquad n\geq1. \tag{6}$$ In particular, $\mathbb E\lambda=\mu$ and $\operatorname{Var}\lambda=\mu a^2/(2\delta)$.

The immigration--Poisson-cluster construction is subcritical, hence locally finite and stationary; the same genealogy gives uniqueness among finite-intensity stationary Hawkes processes. Applying stationary (2) to $e^{-sx}$ gives $$0=-b\nu sL(s)-\{bs+e^{-as}-1\}L'(s).$$ The bracket has derivative $b-ae^{-as}>0$ and vanishes only at zero, so (5) has one normalized solution. Applying (2) to $x^n$, expanding $x\{(x+a)^n-x^n\}$, and isolating the coefficient $n(b-a)m_n$ gives (6). Induction closes every moment, and its first two instances give the displayed mean and variance.

\>0

# Three covariances and exact window variance

The following objects have different dimensions and must not be conflated. The first is a covariance function of the stochastic intensity; the second is a measure for point counts and contains a same-event atom; the third is the Fourier transform of that complete measure.

In the subcritical stationary regime, $$\begin{aligned}
 C_\lambda(t)&=\operatorname{Cov}(\lambda_t,\lambda_0)
   =\frac{\mu a^2}{2\delta}e^{-\delta|t|},             \tag{7}\\
 \Gamma(\,\mathrm dt)&=\mu\delta_0(\,\mathrm dt)
   +\frac{\mu a(2b-a)}{2\delta}e^{-\delta|t|}\,\mathrm dt.  \tag{8}\end{aligned}$$ Under the convention with no $1/(2\pi)$ factor, $$S(\omega):=\int_{\mathbb R}e^{-i\omega t}\Gamma(\,\mathrm dt)
   =\mu\frac{b^2+\omega^2}{\delta^2+\omega^2}.        \tag{9}$$ Consequently, for a stationary count in a window of length $T$, $$\operatorname{Var}(N_T-N_0)=\mu T+\mu a(2b-a)
 \left\{\frac{T}{\delta^2}-
 \frac{1-e^{-\delta T}}{\delta^3}\right\}.           \tag{10}$$

Conditional first moments solve $u'(t)=b\nu-\delta u(t)$, so $\mathbb E(\lambda_t\mid\lambda_0=x)=\mu+(x-\mu)e^{-\delta t}$. Multiplication by $\lambda_0-\mu$ and the variance above give (7).

For counts, Hawkes's complete point spectrum is $\mu/|1-a/(b+i\omega)|^2$ [@Hawkes1971]. Algebra gives $$S(\omega)=\mu+\frac{\mu a(2b-a)}{\delta^2+\omega^2}.$$ Because $e^{-\delta|t|}$ transforms to $2\delta/(\delta^2+\omega^2)$ in the frozen convention, inversion gives (8), including the indispensable $\mu\delta_0$ term. Finally integrate $\Gamma$ over $[0,T]^2$: the atom contributes $\mu T$, while the continuous part is twice its positive-lag coefficient times $\int_0^T(T-t)e^{-\delta t}\,\mathrm dt$. This is (10), whose long-window slope is $S(0)=\mu b^2/\delta^2$.

  object                                includes same-event atom?   coefficient of $e^{-\delta|t|}$
  ------------------------------------- --------------------------- ---------------------------------
  intensity covariance $C_\lambda(t)$   not applicable              $\mu a^2/(2\delta)$
  counting covariance $\Gamma$          yes, $\mu\delta_0$          $\mu a(2b-a)/(2\delta)$
  Bartlett spectrum $S(\omega)$         atom becomes $\mu$          Fourier-domain rational law

\>1

# Borel genealogy and the complete boundary atlas

One event has Poisson offspring mean $m=a/b$. If $K$ is the total family size descended from one immigrant, its probability generating function $T(z)$ satisfies $T(z)=z\exp\{m(T(z)-1)\}$. Lagrange inversion therefore gives the Borel law $$\Pr\{K=n\}=e^{-mn}\frac{(mn)^{n-1}}{n!},\qquad n\geq1. \tag{11}$$ For $m<1$, this is a probability distribution with $\mathbb EK=(1-m)^{-1}$ and $\operatorname{Var}K=m(1-m)^{-3}$.

At $a=0$, (1) is stationary at $\lambda\equiv\nu$ and $N$ is homogeneous Poisson. At $\nu=0$, the empty process is stationary for every $a,b$; this does not assert uniqueness outside the subcritical face. If $\nu>0$, the mean equation $r'=b\nu+(a-b)r$ grows linearly at $a=b$ and exponentially at $a>b$. Hence neither face has a stationary law of finite intensity. This last qualification is essential: no claim is made here about exotic infinite-mean objects.

# Executable certificate, collisions, and Route A

The exact certificate contains $320$ stable rational cases, $3{,}520$ moment cells, $3{,}200$ window-series cells, $160$ Borel-cluster rows, and six boundary rows. An independent checker closes $27{,}893$ assertions, SymPy closes $1{,}304$ exact symbolic and stored-row checks, fresh byte replay is exact, and repaired-hash hostile testing rejects $28/28$ semantic or provenance changes. These finite tables are regression oracles for the all-parameter proof, not its substitute.

Nearest registered owners C208, C214, C233, C246, and C263 cover different renewal, queue, branching, diffusion, and exchangeable-urn mechanisms. None contains the present joint affine transform together with the three-way covariance separation and Borel genealogy; this is a collision audit, not a claim of literature novelty. Hawkes's primary spectral source is explicitly retained [@Hawkes1971].

Events, clusters, and the Markov generator supply neither rational-prime ownership nor a logarithmic prime clock, target divisor, functional equation, or determinant-class Hilbert--Pólya operator. The formal generator analogy does not cross that boundary. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)}.$$ The verdict is `ROUTE_A_REJECTED`; Route B is disabled. No Euler factor, root number, automorphy statement, target zero table, or source-to- target spectral identification is claimed.

9 A. G. Hawkes, *Spectra of some self-exciting and mutually exciting point processes*, Biometrika **58** (1971), 83--90, [doi:10.1093/biomet/58.1.83](https://doi.org/10.1093/biomet/58.1.83).
