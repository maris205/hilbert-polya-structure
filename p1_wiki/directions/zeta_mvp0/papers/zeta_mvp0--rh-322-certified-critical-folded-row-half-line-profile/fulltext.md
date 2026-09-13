---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-322-certified-critical-folded-row-half-line-profile"
canonical_tex: "zeta_mvp0/papers/RH-322-certified-critical-folded-row-half-line-profile/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-322-certified-critical-folded-row-half-line-profile/main.pdf"
source_sha256: "672e6237178c81b2baf54cba64753206e8052c812ae7641246f57fa30cbc720a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Certified Half-Line Limits for a Critical Folded Gaussian Row

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-322-certified-critical-folded-row-half-line-profile>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-322-certified-critical-folded-row-half-line-profile/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-322-certified-critical-folded-row-half-line-profile/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-322-certified-critical-folded-row-half-line-profile/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-322-certified-critical-folded-row-half-line-profile/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the first-alias clock, a distinguished deterministic row can have endpoint clearance of the same order as the Gaussian width. We compute the exact boundary rescaling of one physical folded row and prove that it converges in total variation to a clearance-parameterized half-line Gaussian. Both the direct lobe and the complete folded row have the same exact error $$2\,\overline\Phi(\sigma^{-1}-a)/\Phi(a)$$ in $L^1$, while changing the clearance ratio from $a$ to $d$ costs at most $|a-d|$. We also give the limiting moment recurrence and prove that distinct clearance phases produce distinct profiles. This is a one-row probability kernel theorem. It does not combine the parity layer, neighboring shell, or moving-order trace remainder, and is not a joint first-alias trace law.
author:
- Bin Wang
date: July 2026
title: 'Certified Half-Line Limits for a Critical Folded Gaussian Row'
```

## Markdown 正文

# The exact physical row

Let $$\phi(t)=\frac{e^{-t^2/2}}{\sqrt{2\pi}},\qquad
 \Phi(t)=\int_{-\infty}^t\phi(s)\,ds,\qquad
 \overline\Phi=1-\Phi.$$ Write $L=\sigma^{-1}$ and suppose that the Gaussian mean is $$p_{\sigma,a}=1-\sigma a,\qquad 0\le a\le L.$$ Thus $a$ is the clearance-to-noise ratio. The physical folded transition row on $[0,1]$ is $$\label{eq:physical-row}
 P_{\sigma,a}(y)=
 \frac{\phi_\sigma(y-p_{\sigma,a})+\phi_\sigma(y+p_{\sigma,a})}
 {Z_{\sigma,a}}\mathbf1_{[0,1]}(y),
 \qquad
 \phi_\sigma(t)=\sigma^{-1}\phi(t/\sigma).$$ Direct integration gives $$\label{eq:folded-normalizer}
 Z_{\sigma,a}=\Phi(a)-\overline\Phi(2L-a).$$ After the boundary change of variables $v=(1-y)/\sigma$, the pushed-forward density is $$\label{eq:folded-density}
 \widetilde h_{\sigma,a}(v)=
 \frac{\phi(v-a)+\phi(2L-v-a)}
 {\Phi(a)-\overline\Phi(2L-a)}\mathbf1_{[0,L]}(v).$$ The second term is the reflected lobe required by the exact folded kernel. For comparison, retaining only the direct lobe gives $$\label{eq:direct-density}
 h^+_{\sigma,a}(v)=
 \frac{\phi(v-a)}{\Phi(a)-\overline\Phi(L-a)}
 \mathbf1_{[0,L]}(v).$$ The half-line profile at fixed clearance ratio is $$\label{eq:limit-density}
 g_a(v)=\frac{\phi(v-a)}{\Phi(a)}\mathbf1_{[0,\infty)}(v).$$ This is the upper-conditioned Gaussian row already implicit in the endpoint geometry of RH-16. The new point here is the exact finite-interval and full folding transfer at critical clearance.

# Exact total variation and parameter stability

We use $d_{\mathrm{TV}}(f,g)=\tfrac12\|f-g\|_{L^1}$.

[\[thm:main\]]{#thm:main label="thm:main"} For every $\sigma>0$ and $0\le a\le\sigma^{-1}$, $$\label{eq:exact-tail}
 \|h^+_{\sigma,a}-g_a\|_1
 =\|\widetilde h_{\sigma,a}-g_a\|_1
 =\frac{2\overline\Phi(L-a)}{\Phi(a)}.$$ For every $a,d\ge0$, $$\label{eq:parameter-lipschitz}
 \|g_a-g_d\|_1\le |a-d|.$$ Consequently $$\label{eq:combined-bound}
 \boxed{
 \|\widetilde h_{\sigma,a}-g_d\|_1
 \le |a-d|+
 \frac{2\overline\Phi(\sigma^{-1}-a)}{\Phi(a)}.}$$ The same bound holds with $h^+_{\sigma,a}$ in place of the folded row.

The direct row is $g_a$ conditioned on $v\le L$. Its density exceeds $g_a$ on $[0,L]$ and vanishes beyond $L$, so its positive and negative $L^1$ parts both equal the discarded mass $$\int_L^\infty g_a(v)\,dv
 =\frac{\overline\Phi(L-a)}{\Phi(a)}.$$ For the folded row, the denominator in [\[eq:folded-density\]](#eq:folded-density){reference-type="eqref" reference="eq:folded-density"} is smaller than $\Phi(a)$ and the numerator contains the direct nonnegative term. Hence $\widetilde h_{\sigma,a}\ge g_a$ throughout $[0,L]$, while the folded row again vanishes beyond $L$. The same mass argument proves the second identity in [\[eq:exact-tail\]](#eq:exact-tail){reference-type="eqref" reference="eq:exact-tail"}.

For parameter stability put $r(a)=\phi(a)/\Phi(a)$. Differentiating [\[eq:limit-density\]](#eq:limit-density){reference-type="eqref" reference="eq:limit-density"} gives $$\partial_a g_a(v)=g_a(v)\{v-a-r(a)\}.$$ Under $g_a$, the random variable $V-a$ has mean $r(a)$ and variance $$1-a r(a)-r(a)^2\le1.$$ Cauchy--Schwarz therefore gives $\|\partial_a g_a\|_1\le1$. Integrating along the segment from $d$ to $a$ proves [\[eq:parameter-lipschitz\]](#eq:parameter-lipschitz){reference-type="eqref" reference="eq:parameter-lipschitz"}; the triangle inequality proves [\[eq:combined-bound\]](#eq:combined-bound){reference-type="eqref" reference="eq:combined-bound"}.

The exact tail also records its true exponential scale. If $a,d\in K=[m,A]\subset[0,\infty)$ and $L>A$, Mills' inequality gives $$\label{eq:compact-mills}
 \|\widetilde h_{\sigma,a}-g_d\|_1
 \le |a-d|+
 \frac{2\phi(L-A)}{\Phi(m)(L-A)}.$$ Uniformly for $a$ in a fixed compact set, $$\label{eq:tail-asymptotic}
 \frac{2\overline\Phi(L-a)}{\Phi(a)}
 =\frac{2\phi(L-a)}{\Phi(a)(L-a)}
 \bigl(1+O(\sigma^2)\bigr).$$ Thus a bound $C_K e^{-c/\sigma^2}$ is valid after choosing any sufficiently small fixed $c>0$. One must not replace the exact exponent $-(\sigma^{-1}-a)^2/2$ by $-1/(2\sigma^2)$ with a uniform fixed prefactor.

[\[cor:observables\]]{#cor:observables label="cor:observables"} If $a_\sigma\to d\ge0$, then both finite rows converge to $g_d$ in total variation. Every bounded measurable observable $F$ satisfies $$\left|\int F\widetilde h_{\sigma,a_\sigma}
       -\int Fg_d\right|
 \le \|F\|_\infty
 \left(|a_\sigma-d|+
 \frac{2\overline\Phi(\sigma^{-1}-a_\sigma)}{\Phi(a_\sigma)}\right).$$ The direct row also converges in Wasserstein distance. More precisely, $$\label{eq:wasserstein}
 W_1(h^+_{\sigma,a},g_a)=
 \frac{\phi(L-a)-r(a)\overline\Phi(L-a)}
 {\Phi(a)-\overline\Phi(L-a)},
 \qquad
 W_1(g_a,g_d)\le |a-d|.$$ In particular, $$W_1(h^+_{\sigma,a},g_d)\le |a-d|+
 \frac{\phi(L-a)-r(a)\overline\Phi(L-a)}
 {\Phi(a)-\overline\Phi(L-a)}.$$ Hence all Lipschitz observables, including unbounded ones of at most linear growth, obey the same quantitative convergence law.

The total-variation statement is [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The direct finite row is stochastically smaller than $g_a$, so its $W_1$ distance equals the difference of their means; direct integration gives the first formula in [\[eq:wasserstein\]](#eq:wasserstein){reference-type="eqref" reference="eq:wasserstein"}. The family $g_a$ has monotone likelihood ratio in $a$, hence is stochastically increasing. Its mean is $a+r(a)$ and its derivative is $1-a r(a)-r(a)^2\le1$, proving the second formula.

# Moments and the clearance-phase obstruction

Let $M_j(d)=\int_0^\infty v^j g_d(v)\,dv$. Integration by parts gives $$\label{eq:moment-recurrence}
 M_0(d)=1,\qquad M_1(d)=d+r(d),\qquad
 M_{j+1}(d)=dM_j(d)+jM_{j-1}(d)\quad(j\ge1).$$ In particular, $$\begin{aligned}
 \mathbb E_d V&=d+r(d),\label{eq:mean}\\
 \mathbb E_d V^2&=d^2+1+d r(d),\label{eq:second}\\
 \operatorname{Var}_d(V)&=1-d r(d)-r(d)^2.\label{eq:variance}\end{aligned}$$ The explicit Gaussian tails in [\[eq:folded-density\]](#eq:folded-density){reference-type="eqref" reference="eq:folded-density"} imply convergence of every polynomial moment. More quantitatively, for each $j$ and compact $K\subset[0,\infty)$ there are $C_{j,K},c_K>0$ such that, whenever $a,d\in K$ and $\sigma$ is sufficiently small with $\sigma^{-1}>\sup K$, $$\label{eq:moment-bound}
 \left|\int v^j\widetilde h_{\sigma,a}(v)\,dv-M_j(d)\right|
 \le C_{j,K}|a-d|+C_{j,K}e^{-c_K/\sigma^2}.$$

The parameter $d$ cannot be suppressed. Differentiating the limiting mean in [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"} gives $$\label{eq:mean-derivative}
 \frac{d}{dd}\{d+r(d)\}
 =1-d r(d)-r(d)^2
 =\operatorname{Var}_d(V)>0.$$ Thus $d\mapsto g_d$ is injective. If $a_\sigma$ has two subsequential limits $d_1\ne d_2$, the corresponding folded rows have two distinct total-variation limits. There is no phase-independent universal row profile without control of the clearance ratio.

For the boundary cycles archived in RH-17 and RH-19, with $\lambda=1.678573510428322\ldots$, $$\delta_k=C_{\mathrm b}\lambda^{-2k}(1+o(1)).$$ At the natural first-alias clock $k_\sigma=\log(1/\sigma)/(2\log\lambda)+O(1)$, the ratio $a_\sigma=\delta_{k_\sigma}/\sigma$ remains of order one, but the bounded integer phase need not converge. The theorem therefore supplies a complete subsequential one-row dictionary, not a unique phase-free replacement.

# Protocol, scope, and next interface

The reproduction code evaluates only the exact normalizers, Gaussian tails, Wasserstein correction, moments, and pairwise profile separations. No fitted exponent or transfer-matrix diagonalization enters the proof. The physical folded formula is checked independently against the sum of its direct and reflected masses.

At a critical source $x=\sqrt\sigma q$, RH-14 has $u_c=1.543689012692076\ldots$, $a=u_cq^2$, and row normalizer $\Phi(u_cq^2)+O(e^{-c/\sigma^2})$. Equation [\[eq:folded-normalizer\]](#eq:folded-normalizer){reference-type="eqref" reference="eq:folded-normalizer"} recovers that local factor exactly and shows why it cannot be replaced by one. It does not replace the RH-14 signed endpoint density, which integrates over all $q$, nor does it couple the endpoint row to the repelling-boundary profile.

RH-17 shows that the endpoint and first internal contact are simultaneously critical, and RH-19 shows that the neighboring critical sibling has order-one relative mass. Neither contribution appears in a one-row theorem. No moving-order Duhamel remainder, parity cancellation, neighboring-shell matching, full-trace replacement, or joint error $o(kR^{-2k})$ with $R=1.4$ is proved here. Gates A--E remain false/open; the paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace formula or zeta-divisor equality, and does not imply RH.

The next interface is a paired affine Gaussian chain retaining both critical contacts with their common clearance phase. Only after that pairing is combined with curvature, normalization, parity, shell coupling, and a moving-order remainder can it enter the first-alias trace equation.
