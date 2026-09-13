---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-linear-birth-death-branching-route-a"
canonical_tex: "henon_dynamics/henon_linear_birth_death_branching_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_linear_birth_death_branching_route_a/paper/main.pdf"
source_sha256: "503e0ff5ac93875092bd0a6fb9687f0d868580b494369713472e9486709ebab3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Linear Birth--Death Branching at Every Nonnegative Rate Pair: An Exact Finite-Time Möbius and Transition Theorem

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_linear_birth_death_branching_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_linear_birth_death_branching_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_linear_birth_death_branching_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_linear_birth_death_branching_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the continuous-time branching chain with per-particle birth and death rates $\lambda,\mu\geq0$, we prove one formula package valid for every initial population $z\in\mathbb N_0$. The one-ancestor probability generating function is a Möbius semigroup. Off criticality its clock is $\delta=e^{-(\lambda-\mu)t}$; at criticality the nonsingular clock is $\tau=\lambda t$. Its zero-modified geometric expansion yields the exact $z$-ancestor transition as a binomial mixture over surviving ancestral lineages, with a conditional negative-binomial sum. This prevents the common, nonuniform replacement by one negative-binomial law. Differentiation gives the mean and variance, including all pure and zero-rate boundaries. \>0 The same formulas prove the subcritical geometric quasi-stationary law, the critical Yaglom exponential scaling, and the supercritical martingale limit as an atom plus a binomial mixture of gamma laws. \>1 Independent exact arithmetic, symbolic limits, byte replay and hostile mutations validate the artifact while remaining separate from the proof. The source has no intrinsic prime arithmetic or target spectral object and is rejected by every Route-A stage.
author:
- 'Route-A structural certificate C208'
title:
- 'Linear Birth--Death Branching at Every Nonnegative Rate Pair: An Exact Finite-Time Möbius and Transition Theorem'
- 'Linear Birth--Death Branching at Every Nonnegative Rate Pair: Exact Transitions and the Subcritical--Critical--Supercritical Limit Atlas'
- 'Linear Birth--Death Branching at Every Nonnegative Rate Pair: Möbius Semigroup, Survivor-Mixture Transitions, and Complete Limit Atlas'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Markov branching process; linear birth--death chain; probability generating function; quasi-stationarity; Yaglom limit; martingale limit.

chinese-simplified

中文摘要

本文对任意非负出生率、死亡率及任意非负整数初值，给出线性出生死亡分枝过程的完整公式。 单祖先概率生成函数构成[Möbius]{lang="en"}半群；任意初值的转移律是幸存祖先数的二项混合， 给定幸存祖先数后才是负二项和，不能在全参数范围内统一误写成一个负二项分布。 \>0 同一公式还导出次临界准平稳几何极限、临界[Yaglom]{lang="en"}指数缩放， 以及超临界原子加[Gamma]{lang="en"}混合极限。 全部纯出生、纯死亡、零速率、零初值和零时刻边界均被显式闭合。

关键词：出生死亡过程；分枝过程；概率生成函数；准平稳分布；鞅极限。

# Source lock and model

Let $Z=(Z_t)_{t\geq0}$ be the minimal continuous-time Markov chain on $\mathbb N_0$ with generator $$\label{eq:generator}
 (Gf)(n)=\lambda n\{f(n+1)-f(n)\}
          +\mu n\{f(n-1)-f(n)\},
 \qquad \lambda,\mu\geq0.$$ State zero is absorbing and $Z_0=z\in\mathbb N_0$. A Yule process with rate $\lambda$ dominates the number of births, so the chain is nonexplosive at every finite time. Distinct initial particles found independent descendant families. Consequently, if $$F_t(s)=\mathbb E_1[s^{Z_t}],\qquad 0\leq s\leq1,$$ then $\mathbb E_z[s^{Z_t}]=F_t(s)^z$. This precise source family and its linear growth terminology are locked to the classical report of Karlin and McGregor [@KM58]; no priority claim is made here.

# The finite-time theorem

Put $r=\lambda-\mu$. For $r\ne0$ define $\delta=e^{-rt}$; for $r=0$ put $\tau=\lambda t$.

#### Theorem 1 (Möbius PGF semigroup).

For all $\lambda,\mu\geq0$ and $t\geq0$, $$\begin{aligned}
 r\ne0:\quad
 F_t(s)&=\frac{\mu(1-s)-\delta(\mu-\lambda s)}
 {\lambda(1-s)-\delta(\mu-\lambda s)}, \label{eq:offpgf}\\
 r=0:\quad
 F_t(s)&=\frac{\tau+(1-\tau)s}{1+\tau-\tau s}. \label{eq:critpgf}\end{aligned}$$ The second line includes $\lambda=\mu=0$, when $\tau=0$ and $F_t(s)=s$. Moreover $F_t\circ F_u=F_{t+u}$.

#### Proof.

Conditioning over the first event of one particle gives the backward equation $$\label{eq:riccati}
 \partial_tF_t=\lambda(F_t^2-F_t)+\mu(1-F_t)
              =(F_t-1)(\lambda F_t-\mu),\qquad F_0(s)=s.$$ Separating the two roots gives [\[eq:offpgf\]](#eq:offpgf){reference-type="eqref" reference="eq:offpgf"}; when the roots coalesce, integrating $\partial_tF=\lambda(F-1)^2$ gives [\[eq:critpgf\]](#eq:critpgf){reference-type="eqref" reference="eq:critpgf"}. The formulas also follow from the matrices, acting by $\bigl(As+B\bigr)/\bigl(Cs+D\bigr)$, $$M_\delta=\frac1r
 \begin{pmatrix}
 \delta\lambda-\mu&\mu(1-\delta)\\
 \lambda(\delta-1)&\lambda-\delta\mu
 \end{pmatrix},\qquad
 N_\tau=\begin{pmatrix}1-\tau&\tau\\-\tau&1+\tau\end{pmatrix}.$$ Direct multiplication yields $M_{\delta_1}M_{\delta_2}=M_{\delta_1\delta_2}$ and $N_{\tau_1}N_{\tau_2}=N_{\tau_1+\tau_2}$; both matrices are the identity at zero time. Since $\delta(t+u)=\delta(t)\delta(u)$ and $\tau(t+u)=\tau(t)+\tau(u)$, the semigroup claim follows. $\square$

#### Theorem 2 (one ancestor and every-$z$ transition).

Define, for $r\ne0$, $$\label{eq:pb-off}
 p_0=\frac{\mu(1-\delta)}{\lambda-\mu\delta},\qquad
 \beta=\frac{\lambda(1-\delta)}{\lambda-\mu\delta},$$ and, for $r=0$, define $$\label{eq:pb-critical}
 p_0=\beta=\frac{\tau}{1+\tau}.$$ Then $0\leq p_0\leq1$, $0\leq\beta<1$, and $$\label{eq:one-law}
 \mathbb P_1(Z_t=0)=p_0,\qquad
 \mathbb P_1(Z_t=n)=(1-p_0)(1-\beta)\beta^{n-1},\quad n\geq1.$$ For every $z\in\mathbb N_0$, $$\begin{aligned}
 \mathbb P_z(Z_t=0)&=p_0^z, \label{eq:z-zero}\\
 \mathbb P_z(Z_t=n)&=
 \sum_{k=1}^{\min(z,n)}\binom zk p_0^{z-k}(1-p_0)^k
 \binom{n-1}{k-1}(1-\beta)^k\beta^{n-k},\quad n\geq1. \label{eq:z-law}\end{aligned}$$

#### Proof.

Algebra rewrites either PGF in Theorem 1 as $$\label{eq:zmgeom}
 F_t(s)=p_0+(1-p_0)\frac{(1-\beta)s}{1-\beta s}.$$ For $r>0$, $0<\delta\leq1$; for $r<0$, $\delta\geq1$. These two sign cases in [\[eq:pb-off\]](#eq:pb-off){reference-type="eqref" reference="eq:pb-off"}, together with the pure-rate edges, give the claimed parameter ranges. Expanding the geometric denominator proves [\[eq:one-law\]](#eq:one-law){reference-type="eqref" reference="eq:one-law"}.

For $z$ independent ancestral lines, let $K$ be the number nonextinct at time $t$. Then $K\sim\operatorname{Bin}(z,1-p_0)$. Given $K=k$, the $k$ positive family sizes are independent geometric variables on $\{1,2,\ldots\}$ with success $1-\beta$; their sum has probability $\binom{n-1}{k-1}(1-\beta)^k\beta^{n-k}$. Mixing over $K$ gives [\[eq:z-zero\]](#eq:z-zero){reference-type="eqref" reference="eq:z-zero"}--[\[eq:z-law\]](#eq:z-law){reference-type="eqref" reference="eq:z-law"}. $\square$

#### Why this is not uniformly one negative-binomial law.

The mixing shape $K$ is random whenever several ancestral lines can independently die. Thus the all-parameter law must retain the binomial survivor mixture; only after conditioning on $K=k$ is the positive sum one negative-binomial law with fixed shape $k$. At special parameter values the mixture can collapse---for example, if $p_0+\beta=1$, then $F_t(s)^z$ itself has an ordinary negative-binomial form. This exception is exactly why the claim is about the uniform formula rather than an impossible pointwise ban.

#### Corollary 3 (moments).

For every $z\in\mathbb N_0$, $$\begin{aligned}
 \mathbb E_z Z_t&=ze^{rt}, \label{eq:mean}\\
 \operatorname{Var}_z Z_t&=
 \begin{cases}
 \displaystyle z\frac{\lambda+\mu}{r}e^{rt}(e^{rt}-1),&r\ne0,\\[4pt]
 2z\lambda t,&r=0.
 \end{cases} \label{eq:variance}\end{aligned}$$

#### Proof.

Differentiate $F_t(s)^z$ at $s=1$. From [\[eq:zmgeom\]](#eq:zmgeom){reference-type="eqref" reference="eq:zmgeom"}, one ancestral family has mean $(1-p_0)/(1-\beta)$ and second moment $(1-p_0)(1+\beta)/(1-\beta)^2$. Substitution of [\[eq:pb-off\]](#eq:pb-off){reference-type="eqref" reference="eq:pb-off"} or [\[eq:pb-critical\]](#eq:pb-critical){reference-type="eqref" reference="eq:pb-critical"}, followed by addition across independent ancestors, gives [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}--[\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}. $\square$

#### All finite-time degeneracies.

The formulas are literal at every boundary:

  Boundary          One-ancestor parameters             Result for $z$ ancestors
  ----------------- ----------------------------------- -----------------------------------------------------------------------------------------
  $t=0$             $p_0=\beta=0$                       $Z_t=z$
  $z=0$             any admissible pair                 $Z_t=0$
  $\lambda=\mu=0$   $p_0=\beta=0$ for all $t$           $Z_t=z$
  $\mu=0<\lambda$   $p_0=0$, $\beta=1-e^{-\lambda t}$   shifted negative-binomial sum
  $\lambda=0<\mu$   $p_0=1-e^{-\mu t}$, $\beta=0$       $\operatorname{Bin}(z,e^{-\mu t})$
  $\lambda=\mu>0$   $p_0=\beta=\tau/(1+\tau)$           critical formula [\[eq:z-law\]](#eq:z-law){reference-type="eqref" reference="eq:z-law"}

\>0

# The three long-time regimes

The finite-time exact ledger above uses rational sentinels for $\delta$ and $\tau$. The following limits are instead symbolic consequences of the all-parameter formulas; they are not inferred from a finite cutoff.

#### Theorem 4 (subcritical quasi-stationarity).

Suppose $0\leq\lambda<\mu$ and $z\geq1$. With $\rho=\lambda/\mu$, $$\mathbb P_z(Z_t=n\mid Z_t>0)\longrightarrow
 (1-\rho)\rho^{n-1},\qquad n\geq1.$$ This limiting law is genuinely quasi-stationary: its PGF $$\label{eq:qsd-pgf}
 g(s)=\frac{(1-\rho)s}{1-\rho s}$$ satisfies, for every $t\geq0$, $$\label{eq:qsd-invariance}
 \frac{g(F_t(s))-g(F_t(0))}{1-g(F_t(0))}=g(s).$$ For $\lambda=0$ this is the point mass at one, with $g(s)=s$.

#### Proof.

Substitution of the off-critical formula [\[eq:offpgf\]](#eq:offpgf){reference-type="eqref" reference="eq:offpgf"} into [\[eq:qsd-invariance\]](#eq:qsd-invariance){reference-type="eqref" reference="eq:qsd-invariance"} gives the identity after cancellation. The numerator in its left-hand side removes the absorption atom and the denominator is the survival probability, so the identity is exactly invariance under the transition semigroup conditional on nonabsorption. As $t\to\infty$, $\delta\to\infty$, hence $p_0\to1$ and $\beta\to\rho$. Given survival of one line, [\[eq:one-law\]](#eq:one-law){reference-type="eqref" reference="eq:one-law"} is geometric with success $1-\beta$. For $z$ lines put $q_t=1-p_0\to0$. Since $K\sim\operatorname{Bin}(z,q_t)$, $\mathbb P(K\geq2)/\mathbb P(K\geq1)=O(q_t)$. Conditional on population survival, exactly one ancestral line therefore survives with limiting probability one, proving the result. $\square$

#### Theorem 5 (critical Yaglom scaling).

If $\lambda=\mu=c>0$ and $z\geq1$, then $$\mathcal L\left(\frac{Z_t}{ct}\,\middle|\,Z_t>0\right)
 \Longrightarrow \operatorname{Exp}(1).$$

#### Proof.

Here $\tau=ct\to\infty$, $1-p_0=(1+\tau)^{-1}$, and again only one ancestral line survives conditionally. For that line, at $s=e^{-\theta/\tau}$, $$\mathbb E[s^{Z_t}\mid Z_t>0]
 =\frac{s}{1+\tau-\tau s}\longrightarrow\frac1{1+\theta},$$ the Laplace transform of a unit-rate exponential law. The vanishing multiple-lineage probability transfers the same limit to every fixed $z\geq1$. $\square$

#### Theorem 6 (supercritical martingale and gamma mixture).

Suppose $\lambda>\mu\geq0$, put $r=\lambda-\mu$ and $W_t=e^{-rt}Z_t=\delta Z_t$. Then $W_t\to W$ almost surely and in $L^2$. For one ancestor, $$\label{eq:super-laplace}
 \mathbb E_1e^{-\theta W}
 =\frac\mu\lambda+
 \frac{r^2}{\lambda(r+\lambda\theta)}.$$ For $z$ ancestors let $K\sim\operatorname{Bin}(z,r/\lambda)$. The limit has atom $$\mathbb P_z(W=0)=(\mu/\lambda)^z,$$ and, conditional on $K=k\geq1$, $$W\sim\operatorname{Gamma}\!\left(k,\text{rate }r/\lambda\right).$$ Thus the positive law is a binomially weighted gamma mixture, with the binomial weights conditioned on $K\geq1$ if one conditions on $W>0$. Moreover $\mathbb E_zW=z$ and $\operatorname{Var}_zW=z(\lambda+\mu)/r$.

#### Proof.

The branching property and [\[eq:generator\]](#eq:generator){reference-type="eqref" reference="eq:generator"} make $W_t$ a nonnegative martingale. Equation [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"} shows that its second moments are uniformly bounded, giving almost-sure and $L^2$ convergence. In [\[eq:offpgf\]](#eq:offpgf){reference-type="eqref" reference="eq:offpgf"}, substitute $s=e^{-\theta\delta}$ and let $\delta\downarrow0$ to obtain [\[eq:super-laplace\]](#eq:super-laplace){reference-type="eqref" reference="eq:super-laplace"}. With $q=r/\lambda$, its right side is $$\frac\mu\lambda+q\frac{q}{q+\theta},$$ the transform of an atom of mass $\mu/\lambda$ plus, with mass $q$, an exponential variable of rate $q$. The $z$-ancestor limit is the sum of $z$ independent copies. Counting its nonzero summands gives the stated binomial variable $K$, and a sum of $k$ rate-$q$ exponentials is gamma. The limiting moments follow either from this mixture or by scaling [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}--[\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}. $\square$

#### Asymptotic boundary ledger.

The quasi-stationary and Yaglom statements require $z\geq1$ because conditioning on survival is undefined at $z=0$. The Yaglom statement requires $c>0$; at $c=0$ the chain is the identity. In the pure-birth edge $\mu=0$, Theorem 6 has $K=z$ and a single $\operatorname{Gamma}(z,1)$ component (with the usual point mass at zero when $z=0$). These clauses close rather than silently divide by every degenerate parameter.

\>1

# Exact certificate and Route-A decision

Thirteen exact parameter sentinels cross supercritical, subcritical, critical, pure-birth, pure-death, zero-time and zero-rate cases. For $z=0,\ldots,4$ and $n=0,\ldots,12$, the evidence records 845 transition coefficients, 195 survivor weights, 130 moment values, 26 one-lineage parameters and 36 semigroup coefficients: 1,232 exact scalar identities. The standard-library checker imports no producer code, reconstructs every transition by polynomial convolution, and enforces all nested key sets. A separate SymPy path checks the Riccati equations, both semigroup clocks, moments, critical continuity, pure-rate boundaries, all reported coefficients and all three long-time transforms. Byte replay is exact; 22 repaired-hash attacks and one stale-hash attack are rejected. These finite checks validate the artifact, while Theorems 1--6 carry the continuum proof.

The probability generating function is a normalized expectation, not a dynamical zeta or determinant. The rates have no intrinsic rational-prime semantics; genealogical events are stochastic branches, not deterministic primitive periodic orbits; no target divisor or analytic target is matched; and the Markov evolution supplies no same-clock self-adjoint target quantization. Under the frozen evaluator, $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FAIL}),$$ so the verdict is `ROUTE_A_REJECTED` and Route B is not invoked. The evaluation scope is frozen by the exact literal

`NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Claim firewall.

We claim no classical priority, population-data inference, prime table, target-zero table, arithmetic local datum, Euler factor, root number, automorphy, target divisor or functional equation, Hilbert--Pólya operator, external review, acceptance score or Route-B authorization.

#### Revision focus.

Round 0 closes the Möbius semigroup, exact survivor-mixture transition, moments and every finite-time degeneracy.

#### Revision focus.

Round 1 adds separate proofs of the subcritical quasi-stationary, critical Yaglom and supercritical atom--gamma limit regimes.

#### Revision focus.

Round 2 adds independent validation, hostile controls, source ownership, PGF naming discipline and the strict Route-A stop.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local synthetic exact evidence and deterministic code accompany the paper. No observational population data are used.

#### Ethics.

No human, animal, personal, clinical or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.

1 S. Karlin and J. McGregor, "Linear Growth, Birth and Death Processes," Technical Report KAR ONR 3, Stanford University, January 1958. <https://statistics.stanford.edu/technical-reports/linear-growth-birth-and-death-processes>; persistent record <https://purl.stanford.edu/fx071vs8733>.
