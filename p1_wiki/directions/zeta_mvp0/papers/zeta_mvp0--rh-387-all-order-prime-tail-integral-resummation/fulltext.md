---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-387-all-order-prime-tail-integral-resummation"
canonical_tex: "zeta_mvp0/papers/RH-387-all-order-prime-tail-integral-resummation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-387-all-order-prime-tail-integral-resummation/main.pdf"
source_sha256: "f03d935192e9cfd122de3e85569062e836f15ef6375e9772fd114b160d0b184b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# All-Order Prime-Tail Integral Resummation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-387-all-order-prime-tail-integral-resummation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-387-all-order-prime-tail-integral-resummation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-387-all-order-prime-tail-integral-resummation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-387-all-order-prime-tail-integral-resummation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-387-all-order-prime-tail-integral-resummation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $3=p_1<p_2<\cdots$ be the odd primes, put $x=p_y$ and $L=\log x\ge512$, and let $$V=L^{3/5}(\log L)^{-1/5},\qquad
   \varepsilon_x=0.027L^{1.801}e^{-0.1853V}.$$ For $c=1,\ldots,7$ we resum the whole family of strict tails $P_r(y)=\sum_{p>x}(p^2-1)^{-r}$ into the coordinates $\Phi^{P}_c=\sum_{r\ge1}c^rP_r/r$, and compare them with two integral coordinates $\Phi^{J}_c$ and $\Phi^{I}_c$. Summing the absolute Stieltjes error before taking relative logarithms gives $$\max_c|\Phi^{P}_c-\Phi^{J}_c|\le \frac{28\varepsilon_x}{ xL},\qquad
   0\le\max_c(\Phi^{J}_c-\Phi^{I}_c)\le \frac{14}{3x^3L}.$$ The exact square-clock endpoint map is Lipschitz from $\ell^\infty$ to $\mathbb R$ with dual $\ell^1$ gradient bound $126$ on the required seven-dimensional cube. Consequently, for precisely defined gaps $\operatorname{Gap}_{P},\operatorname{Gap}_{J},\operatorname{Gap}_{I}$, $$\pi^2|\operatorname{Gap}_{P}-\operatorname{Gap}_{J}|\le \frac{3528\varepsilon_x}{ xL},\qquad
   \pi^2|\operatorname{Gap}_{J}-\operatorname{Gap}_{I}|\le \frac{588}{ x^3L}.$$ This is an infinite-order source--kernel exchange and endpoint Lipschitz theorem, not a termwise consequence of a finite-partition result. Since $\varepsilon_xx^2\to\infty$, it gives no second-order or $P_2$-scale precision. A 42-row exact artifact reproduces the algebraic interfaces but is not an analytic proof.
author:
- RH research program
bibliography:
- references.bib
date: 'August 8, 2026'
title: 'All-Order Prime-Tail Integral Resummation'
```

## Markdown 正文

**Keywords:** explicit prime number theorem; strict prime tails; all-order logarithmic resummation; endpoint map; uniform Lipschitz bound.

# Statement and scope

Let $\vartheta(t)=\sum_{p\le t}\log p$. Johnston and Yang prove the explicit Vinogradov--Korobov estimate used below in their Theorem 1.4, equation (1.8), printed page 2 [@JohnstonYang2023]. In the present notation it yields $$|\vartheta(t)-t|\le t\varepsilon_t,\qquad
 \varepsilon_t=0.027(\log t)^{1.801}
 \exp\!\left[-0.1853(\log t)^{3/5}(\log\log t)^{-1/5}\right]
 \label{eq:JY}$$ for $t\ge23$. Direct differentiation shows that $\varepsilon_t$ decreases once $\log t\ge512$; this is also the source transfer frozen in RH-386 [@RH386]. Hence $|\vartheta(t)-t|\le t\varepsilon_x$ for $t\ge x$.

For every integer $r\ge1$ define $$P_r(y)=\sum_{p>x}(p^2-1)^{-r},\quad
 h_r(t)=\frac{1}{(t^2-1)^r\log t},\quad
 J_r=\int_x^\infty h_r(t)\,dt,\quad
 I_{2r}=\int_x^\infty \frac{t^{-2r}}{\log t}\,dt.
 \label{eq:tails}$$ The endpoint $p>x$ is strict throughout. For $1\le c\le7$ set $$\begin{aligned}
 \Phi^{P}_c&=\sum_{r\ge1}\frac{c^rP_r(y)}{ r},\label{eq:PhiP}\tag{P}\\
 \Phi^{J}_c&=\int_x^\infty\frac{-\log(1-c/(t^2-1))}{\log t}\,dt,
 \label{eq:PhiJ}\tag{J}\\
 \Phi^{I}_c&=\int_x^\infty\frac{-\log(1-c/t^2)}{\log t}\,dt.
 \label{eq:PhiI}\tag{I}\end{aligned}$$ We use the corresponding undecorated symbols for the seven-vectors: $$\Phi^{P}=(\Phi^{P}_1,\ldots,\Phi^{P}_7),\qquad
 \Phi^{J}=(\Phi^{J}_1,\ldots,\Phi^{J}_7),\qquad
 \Phi^{I}=(\Phi^{I}_1,\ldots,\Phi^{I}_7).
 \label{eq:coordinate-vectors}$$

The exact endpoint map $F$ and the three gaps are defined in Section [5](#sec:endpoint){reference-type="ref" reference="sec:endpoint"}. The main result is the following.

[\[thm:main\]]{#thm:main label="thm:main"} For every $y$ with $x=p_y$ and $L=\log x\ge512$, all three coordinate vectors lie in $[0,1/2]^7$, and $$\begin{aligned}
 \max_{1\le c\le7}|\Phi^{P}_c-\Phi^{J}_c|
 &\le \frac{28\varepsilon_x}{ xL},\label{eq:coordinate-source}\\
 0\le\max_{1\le c\le7}(\Phi^{J}_c-\Phi^{I}_c)
 &\le \frac{14}{3x^3L}.\label{eq:coordinate-power}\end{aligned}$$ Moreover $$\begin{aligned}
 \pi^2|\operatorname{Gap}_{P}-\operatorname{Gap}_{J}|&\le \frac{3528\varepsilon_x}{ xL},
 \label{eq:gap-source}\\
 \pi^2|\operatorname{Gap}_{J}-\operatorname{Gap}_{I}|&\le \frac{588}{ x^3L},
 \label{eq:gap-power}\\
 \pi^2|\operatorname{Gap}_{P}-\operatorname{Gap}_{I}|&\le \frac{3528\varepsilon_x}{ xL}+\frac{588}{ x^3L}.
 \label{eq:gap-combined}\end{aligned}$$ All constants are uniform in the seven real integer channels $c\in\{1,\ldots,7\}$.

# Strict Stieltjes transfer before resummation

Write $E(t)=\vartheta(t)-t$. Stieltjes integration at the strict endpoint gives $$\begin{aligned}
 P_r&=\int_{(x,\infty)}h_r(t)\,d\vartheta(t)
 =-\vartheta(x)h_r(x)-\int_x^\infty\vartheta(t)h_r'(t)\,dt,
 \label{eq:stieltjes}\\
 J_r&=-xh_r(x)-\int_x^\infty t h_r'(t)\,dt.\label{eq:Jparts}\end{aligned}$$ Thus no prime at $x$ is included and $$P_r-J_r=-E(x)h_r(x)-\int_x^\infty E(t)h_r'(t)\,dt.
 \label{eq:error-identity}$$ Since $h_r$ decreases, [\[eq:JY\]](#eq:JY){reference-type="eqref" reference="eq:JY"} and [\[eq:Jparts\]](#eq:Jparts){reference-type="eqref" reference="eq:Jparts"} imply the absolute bound $$|P_r-J_r|\le\varepsilon_x\{2xh_r(x)+J_r\}.
 \label{eq:absolute-stieltjes}$$ This is the crucial order of operations: we will sum [\[eq:absolute-stieltjes\]](#eq:absolute-stieltjes){reference-type="eqref" reference="eq:absolute-stieltjes"} over every $r$ directly. The relative estimate $|\log(P_r/J_r)|\le14r\varepsilon_x$ from RH-386 has an $r$-dependent smallness condition and cannot be summed over all orders.

[\[prop:source\]]{#prop:source label="prop:source"} For $1\le c\le7$, $$|\Phi^{P}_c-\Phi^{J}_c|
 \le \frac{3c\varepsilon_x}{ xL\{1-(1+c)/x^2\}}
 <\frac{4c\varepsilon_x}{ xL}.
 \label{eq:per-c-source}$$

All summands are nonnegative and $c/(p^2-1)\le7/24<1$. Tonelli's theorem and $-\log(1-z)=\sum_{r\ge1}z^r/r$ give $$\Phi^{P}_c=\sum_{p>x}-\log\!\left(1-\frac{c}{ p^2-1}\right),
 \qquad
 \Phi^{J}_c=\sum_{r\ge1}\frac{c^rJ_r}{ r},
 \label{eq:tonelli}$$ and the latter sum is precisely the integral in [\[eq:PhiJ\]](#eq:PhiJ){reference-type="eqref" reference="eq:PhiJ"}. Now sum [\[eq:absolute-stieltjes\]](#eq:absolute-stieltjes){reference-type="eqref" reference="eq:absolute-stieltjes"} with weights $c^r/r$. At the boundary, $$\sum_{r\ge1}\frac{c^rh_r(x)}{ r}
 =\frac{ -\log(1-c/(x^2-1))}{ L}
 \le \frac{c}{ L(x^2-1-c)}.$$ In the integral, $-\log(1-z)\le z/(1-z)$ and $t\ge x$ give $$\Phi^{J}_c\le \frac{c}{ L\{1-(1+c)/x^2\}}
 \int_x^\infty t^{-2}\,dt
 =\frac{c}{ xL\{1-(1+c)/x^2\}}.$$ The two boundary units and one integral unit total the first constant in [\[eq:per-c-source\]](#eq:per-c-source){reference-type="eqref" reference="eq:per-c-source"}. Since $x>256$ and $c\le7$, the denominator is greater than $3/4$, proving the strict $4c$ bound. Taking $c\le7$ yields [\[eq:coordinate-source\]](#eq:coordinate-source){reference-type="eqref" reference="eq:coordinate-source"}.

# Power-kernel resummation

The same nonnegative Tonelli argument gives the second integral identity $$\Phi^{I}_c=\sum_{r\ge1}\frac{c^rI_{2r}}{ r}.
 \label{eq:I-tonelli}$$

[\[prop:power\]]{#prop:power label="prop:power"} For $1\le c\le7$, $$0\le\Phi^{J}_c-\Phi^{I}_c
 \le \frac{c}{3x^3L\{1-(1+c)/x^2\}}
 <\frac{2c}{3x^3L}.
 \label{eq:per-c-power}$$

The difference of the two logarithmic integrands is nonnegative, and $$\begin{aligned}
 \log\frac{1-c/t^2}{1-c/(t^2-1)}
 &=\log\!\left(1+\frac{c}{ t^2(t^2-1-c)}\right)\\
 &\le \frac{c}{ t^2(t^2-1-c)}
 \le \frac{ct^{-4}}{1-(1+c)/x^2}.\end{aligned}$$ Use $1/\log t\le1/L$ and $\int_x^\infty t^{-4}dt=1/(3x^3)$. Because $x>256$ the displayed denominator exceeds $1/2$. Maximizing $2c/3$ over $c\le7$ proves [\[eq:coordinate-power\]](#eq:coordinate-power){reference-type="eqref" reference="eq:coordinate-power"}.

# The real coordinate cube {#sec:cube}

The analytic domain is deliberately much smaller than the source theorem's $x\ge23$. Since $L\ge512$, $$x=e^L>2^L\ge2^{512}>256.
 \label{eq:cube-bridge}$$ For integral $x$ the telescoping identity $$\sum_{n>x}\frac{1}{ n^2-1}=\frac{1}{2}\left(\frac{1}{ x}+\frac{1}{ x+1}\right)
 \label{eq:integer-tail}$$ and $-\log(1-z)\le2z$ for $0\le z\le1/2$ show $$0\le\Phi^{P}_c\le c\left(\frac{1}{ x}+\frac{1}{ x+1}\right)
 <\frac{2c}{ x}<\frac{14}{256}<\frac{1}{2}.$$ The direct integral bounds used above give the same conclusion for $\Phi^{J}_c$ and $\Phi^{I}_c$ (also $0\le\Phi^{I}_c\le\Phi^{J}_c$). Therefore all three vectors and every line segment joining two of them belong to the convex cube $[0,1/2]^7$.

# Exact endpoint map and its Lipschitz ledger {#sec:endpoint}

For $2\le m\le8$ put $$u_m=\prod_{\substack{p\ \mathrm{odd}\\p\ \mathrm{prime}}}
     \frac{1-m/p^2}{1-1/p^2}
     =\prod_{\substack{p\ \mathrm{odd}\\p\ \mathrm{prime}}}
     \left(1-\frac{m-1}{p^2-1}\right).
 \label{eq:u}$$ For fixed $m\le8$, $$\sum_{p\ \mathrm{odd}}\frac{m-1}{p^2-1}<\infty.$$ Thus the standard infinite-product criterion shows that [\[eq:u\]](#eq:u){reference-type="eqref" reference="eq:u"} converges to a positive value, not merely a product of positive finite factors. All factors after $p=3$ are at most one, so retaining the $p=3$ factor gives $$0<u_m\le \frac{9-m}{8}.
 \label{eq:u-bound}$$ Index the endpoint arrays by $m=2,\ldots,8$: $$(\alpha_m)=(-2,2,-2,2,-2,2,-2),\qquad
 (\beta_m)=(1,-2,2,-2,2,-2,2),
 \label{eq:arrays}$$ and define $$C(V)=1+\sum_{m=2}^8\alpha_mV_m,\qquad
 W(V)=\sum_{m=2}^8\beta_mV_m.$$ For $z=(z_1,\ldots,z_7)\in\mathbb R^7$, write $V_m(z)=u_me^{z_{m-1}}$ and set $$F(z)=2\{C(u)-C(V(z))\}
      -4W(V(z))(1-e^{-z_1}).
 \label{eq:F}$$

The exact endpoint normal form of RH-383 [@RH383] applies to [\[eq:PhiP\]](#eq:PhiP){reference-type="eqref" reference="eq:PhiP"}. With $$q_y=4\prod_{i\le y}p_i^2,\qquad
 \operatorname{Gap}_{P}:=B_{\infty}-G(q_y)=\frac{F(\Phi^{P})}{\pi^2},\qquad
 \operatorname{Gap}_{J}:=\frac{F(\Phi^{J})}{\pi^2},\qquad
 \operatorname{Gap}_{I}:=\frac{F(\Phi^{I})}{\pi^2},
 \label{eq:gaps}$$ $\operatorname{Gap}_{P}$ is the actual square-clock gap, while $\operatorname{Gap}_{J}$ and $\operatorname{Gap}_{I}$ are the two integral surrogates introduced here. These are the only three gap objects used in the theorem.

[\[lem:lipschitz\]]{#lem:lipschitz label="lem:lipschitz"} For every $z\in[0,1/2]^7$, $$\|\nabla F(z)\|_1<126.
 \label{eq:gradient}$$ Consequently $|F(z)-F(z')|\le126\|z-z'\|_\infty$ for any two points of the cube.

The bound [\[eq:u-bound\]](#eq:u-bound){reference-type="eqref" reference="eq:u-bound"} and the exact arrays give the two ledgers $$A:=\sum_{m=2}^8|\alpha_m|u_m\le7,\qquad
 B:=\sum_{m=2}^8|\beta_m|u_m\le\frac{49}{8}.
 \label{eq:AB}$$ Differentiate [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}. The $C$ term, the derivative falling on $W$, and the derivative falling on $1-e^{-z_1}$ have respective coefficients $$2,\qquad4,\qquad4.
 \label{eq:derivative-terms}$$ On the cube, $V_m(z)\le e^{1/2}u_m$, $0\le1-e^{-z_1}\le1$, and $e^{-z_1}\le1$. Therefore the three contributions to the $\ell^1$ gradient are bounded by $2e^{1/2}A$, $4e^{1/2}B$, and $4e^{1/2}B$. Since $e^{1/2}<2$, $$\|\nabla F(z)\|_1
 \le e^{1/2}\left(2\cdot7+4\cdot\frac{49}{8}
                         +4\cdot\frac{49}{8}\right)
 =63e^{1/2}<126.$$ The final assertion is the mean-value theorem along the segment from $z$ to $z'$, with the $\ell^\infty$ input norm paired with its dual $\ell^1$ gradient norm.

# Proof of the main theorem

The coordinate assertions and the cube membership were proved in Propositions [\[prop:source\]](#prop:source){reference-type="ref" reference="prop:source"} and [\[prop:power\]](#prop:power){reference-type="ref" reference="prop:power"} and Section [4](#sec:cube){reference-type="ref" reference="sec:cube"}. Apply Lemma [\[lem:lipschitz\]](#lem:lipschitz){reference-type="ref" reference="lem:lipschitz"} on the segment from $\Phi^{P}$ to $\Phi^{J}$. Equations [\[eq:gaps\]](#eq:gaps){reference-type="eqref" reference="eq:gaps"} and [\[eq:coordinate-source\]](#eq:coordinate-source){reference-type="eqref" reference="eq:coordinate-source"} give $$\pi^2|\operatorname{Gap}_{P}-\operatorname{Gap}_{J}|
 =|F(\Phi^{P})-F(\Phi^{J})|
 \le126\,\frac{28\varepsilon_x}{ xL}
 =\frac{3528\varepsilon_x}{ xL}.$$ The same argument between $\Phi^{J}$ and $\Phi^{I}$ gives $$\pi^2|\operatorname{Gap}_{J}-\operatorname{Gap}_{I}|
 \le126\,\frac{14}{3x^3L}=\frac{588}{ x^3L}.$$ Their sum proves [\[eq:gap-combined\]](#eq:gap-combined){reference-type="eqref" reference="eq:gap-combined"} and completes the proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

# Novelty and sharp scope

The preceding proof is not obtained by inserting every $r$ into the growing-order partition theorem of RH-386. That theorem controls a finite partition through a relative logarithmic estimate whose source condition includes $7R\varepsilon_x\le1/2$, where $R$ is the largest active order. The vector [\[eq:PhiP\]](#eq:PhiP){reference-type="eqref" reference="eq:PhiP"} contains every $r\ge1$, so no finite $R$ exists. Here the absolute strict Stieltjes error [\[eq:absolute-stieltjes\]](#eq:absolute-stieltjes){reference-type="eqref" reference="eq:absolute-stieltjes"} is summed first by Tonelli; only then is the result passed through the entire, partition-infinite endpoint map by the new uniform Lipschitz bound. This simultaneous $r$-infinite and partition-infinite source--kernel exchange is the genuine new theorem.

The available source error does not resolve the next power-kernel scale. Indeed $$\log(\varepsilon_x x^2)
 =2L+\log(0.027)+1.801\log L-0.1853V(L)\longrightarrow+\infty,
 \label{eq:no-P2}$$ because $V(L)=o(L)$. Thus the source term $\varepsilon_x/(xL)$ is asymptotically larger than the $r=2$ scale $1/(x^3L)$. In particular, Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} claims neither a second-order coefficient nor $P_2$-scale (and hence no cubic) precision.

All channels in this paper are the seven real integers $1\le c\le7$. There is no complex-$c$ extension, no prefix/prime-index simultaneous limit exchange, and no clock varying with a prefix length. The frozen phasewise class retains $c_{11}=0$; active $c_{11}$ is outside the source theory. The result supplies no adaptive capacity and no operator, trace, or prime-power trace; it makes no zeta-zero identification and does not prove the Riemann hypothesis. Gates A--E are all false.

# Executable reproduction and source integrity {#sec:artifact}

The companion exact artifact has epistemic role `reproduction_not_analytic_proof`. Its 42 oracle rows comprise 12 analytic/source-interface rows, seven channel rows, seven endpoint rows, 14 finite formal-resummation rows, and two ledger rows. They independently recompute the exact fractions, the cube bridge, the $2,4,4$ derivative ledger, $126$, $3528$, and $588$. The 14 finite rows are degree-four truncations of the formal logarithm/product compiler, but they neither truncate nor prove the analytic theorem.

Twenty-four genuine field-level mutations are rejected, including altered Vinogradov--Korobov constants, a reversed log--log exponent, the wrong domain or channel range, an inclusive prime endpoint, a missing series divisor or Stieltjes boundary, false $3c$ and $21$ source constants, interchanged $J/I$ kernels, wrong endpoint signs, deletion of the final loss derivative, the wrong norm pair, and an illicit claim of $P_2$ precision. Strict JSON parsing rejects duplicates, nonfinite values, wrong top-level types, and Boolean-for-integer aliases. These tests check the algebraic declaration; Johnston--Yang's estimate, Stieltjes integration, Tonelli's theorem, and the mean-value argument remain the analytic proof above.

The immutable evidentiary closure contains 68 Git blobs: 59 inherited RH-386 source rows, the eight standard RH-386 release files, and its external-lock blob. One canonical remote Johnston--Yang lock makes 69 logical sources. The author-manuscript PDF and source tar are not vendored or archived. Network verification is disabled by default and is available only as an explicit opt-in check of the versioned URLs, redirect policy, PDF MIME type, byte counts, page count, and SHA-256 values.

The immutable source identifiers are, in order, the RH-386 release commit, the ordered 68-Git-row digest, the 69-logical-source digest, and the canonical remote-lock digest:

  ------------------------------------------------------------------
  9778e3515d45816665d672a641947b93906abf54
  19def5cbed919da8e9652012cf011f3b5728efd4b24a9eef0911bb7346467d27
  5016397fe59962954514b3b42d68e9de6dfeff0dae949791b01c6a516f5c61fe
  d53b93212b7c5b5b6b3f7e890099c48ce8e35f2bff9bdd49f9c330a9b5039786
  ------------------------------------------------------------------

The arXiv nonexclusive-distribution permission is granted to arXiv; it is not a third-party republication license for this release. The version of record is Copyright 2023 Elsevier Inc., all rights reserved, so the remote payload is recorded as nonredistributable. The lock also records two out-of-scope source typos, one in a Section 5.2 reference to Corollary 1.2/equation (1.5) and one in Theorem 1.4/equation (1.9). Neither typo, Corollary 1.2, nor its table-based fallback is used in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}; its sole external analytic input is Theorem 1.4/equation (1.8).

# Declarations {#declarations .unnumbered}

#### Data and code availability.

The proof, exact certificate compiler, strict tests, official closed Draft 2020--12 schema, source-lock records, offline-by-default verifier, and release replay tools accompany the paper. The Johnston--Yang PDF and source tar are not redistributed; their exact remote identifiers are recorded in the external lock.

#### Author contributions.

The author is responsible for the conceptualization, proof, software, validation, writing, and release audit.

#### Funding.

No external funding was received.

#### Competing interests.

The author declares no competing interests.

#### Ethics.

No human participants, animals, personal data, or clinical interventions are involved.

#### AI assistance.

AI-assisted tools were used for symbolic-interface enumeration, adversarial testing, manuscript drafting, and release auditing. All mathematical claims, citations, source locks, and final text were reviewed under author responsibility.
