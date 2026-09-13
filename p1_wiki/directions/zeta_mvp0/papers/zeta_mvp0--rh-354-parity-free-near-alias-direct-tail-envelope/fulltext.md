---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-354-parity-free-near-alias-direct-tail-envelope"
canonical_tex: "zeta_mvp0/papers/RH-354-parity-free-near-alias-direct-tail-envelope/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-354-parity-free-near-alias-direct-tail-envelope/main.pdf"
source_sha256: "732a264fa2855de2a7b933bbf32713760e8e43c2b4ef7477d51b342385a82fd5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Parity-Free Near-Alias Actual Direct-Tail Envelope

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-354-parity-free-near-alias-direct-tail-envelope>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-354-parity-free-near-alias-direct-tail-envelope/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-354-parity-free-near-alias-direct-tail-envelope/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-354-parity-free-near-alias-direct-tail-envelope/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-354-parity-free-near-alias-direct-tail-envelope/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-352 and RH-353 control normalized actual direct coefficients on selected lower-even and boundary orders. We remove the parity and order restrictions. On one bounded-phase physical clock let $$N_k=2k-L_k,\qquad p_{\sigma,k,n}=\tau_{\sigma,n}-a_n,$$ where $0\le L_k\le2k-2$. Put $s=qR$, $t=q_*R$, $x=(\beta R)^2$, $u=s/\sqrt{x}$, and $v=t/\sqrt{x}$. The source-locked all-order caps imply the complete direct Wiener-tail bound $$\mathfrak W_k:=x^{-N_k/2}\sum_{n\ge N_k}|p_{\sigma,k,n}|R^n
   \le
   \frac{q^{-2}\lambda^{-2\eta_k}}{1-s}\rho_N^ku^{-L_k}
   +\frac{48}{1-t}\rho_T^kv^{-L_k},$$ where $$\rho_N=\lambda^2u^2=\frac{r_H^2\lambda^3}{4},
   \qquad \rho_T=v^2=\frac1\lambda.$$ Thus, for every $L_k=o(k)$, $$\limsup_{k\to\infty}\mathfrak W_k^{1/k}
   \le\rho_N<\frac{1419857}{1600000}<1.$$ This single actual theorem includes every odd and even order above the cut: in particular the critical order, the first-lower order whenever $L_k\ge2$, the complete upper-alias band, and every later order. Moreover, $$x^{-k}\sum_{N_k\le n<4k}
   \frac{|p_{\sigma,k,n}|R^n}{n}$$ decays with the same root ceiling; so does the full logarithmic tail from $N_k$ onward. Exact linear-depth frontiers are derived for both normalizations. The unnormalized separate noisy majorant has superunit root $\lambda^2(qR)^2>9604/7225$, which is a method boundary and not actual noncancellation. Since $p=q-d$, no full-trace $E_{\rm off}$ conclusion follows without head-defect control. RH-241, RH-288, Gates A--E, and every Riemann-hypothesis claim remain open.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  A Parity-Free Near-Alias\
  Actual Direct-Tail Envelope
```

## Markdown 正文

# One direct type at every order

Fix the physical constants $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad q=\frac12,\qquad R=\frac75,
 \qquad \frac{28}{17}<\lambda<\frac{17}{10}.$$ The strict lower and upper multiplier bounds are certified in RH-262 and RH-336, respectively [@WangBoundaryBudget2026; @WangProjectorMass2026]. Put $$\label{eq:scales}
 \beta=\frac1{r_H\sqrt\lambda},\qquad
 q_*=\frac1{r_H\lambda},\qquad
 x=(\beta R)^2>1.$$ Let $\sigma=\sigma_k\downarrow0$ lie on a bounded-phase physical clock: $$\label{eq:clock}
 \eta_k=k-\frac{\log(1/\sigma_k)}{2\log\lambda},
 \qquad \sup_k|\eta_k|<\infty,
 \qquad \sigma_k^{-1}=\lambda^{2(k-\eta_k)}.$$

RH-282 constructs the modulus-complete normal spectral complement and proves, for all $n\ge2$, $$\label{eq:tau-cap}
 \tau_{\sigma,n}=\operatorname{Tr}C_\sigma^n,
 \qquad |\tau_{\sigma,n}|\le\sigma^{-1}q^{n-2}.$$ RH-267 proves the deterministic numerator envelope $$\label{eq:a-cap}
 |a_n|<48q_*^n\qquad(n\ge2).$$ The latter theorem treats odd and even orders explicitly. RH-288 and RH-340 lock their difference as one actual direct coefficient, at every finite order, $$\label{eq:p-type}
 \boxed{p_{\sigma,k,n}:=\tau_{\sigma,n}-a_n
 =q_{\sigma,k,n}-d_{\sigma,k,n}.}$$ No orbit, parity, or alias decomposition is used below [@WangSpectralTail2026; @WangUnifiedEnvelope2026; @WangGluing2026; @WangSynchronization2026].

Define four subunit geometric parameters $$\label{eq:geometric}
 s=qR=\frac7{10},\qquad
 t=q_*R=\frac{28}{17\lambda},\qquad
 u=\frac{s}{\sqrt x}=qr_H\sqrt\lambda,
 \qquad v=\frac{t}{\sqrt x}=\lambda^{-1/2}.$$ Indeed $s,t,v<1$, while $$u^2=q^2r_H^2\lambda
 <\frac{4913}{16000}<1.$$ The two natural root rates are $$\label{eq:rates}
 \rho_N=\lambda^2u^2=\frac{r_H^2\lambda^3}{4},
 \qquad \rho_T=v^2=\frac1\lambda.$$ They satisfy $$\label{eq:rate-certificates}
 \rho_T<\rho_N<\frac{1419857}{1600000}<1,
 \qquad \rho_T<\frac{17}{28}<1.$$ The upper bounds are those of RH-352. For the ordering, the lower multiplier bound gives $r_H\lambda^2>2$, hence $\rho_N/\rho_T=r_H^2\lambda^4/4>1$ [@WangModulusCancellation2026].

# A complete bottom-normalized direct tail

Let $L_k$ be any integer sequence satisfying $$\label{eq:depth-domain}
 0\le L_k\le2k-2,
 \qquad N_k=2k-L_k\ge2.$$ Define the bottom-normalized coefficient $\ell^1$ tail $$\label{eq:W}
 \mathfrak W_k(L_k)
 =x^{-N_k/2}\sum_{n\ge N_k}|p_{\sigma,k,n}|R^n.$$ Both source series converge because $s,t<1$.

[\[thm:W\]]{#thm:W label="thm:W"} For every depth sequence in [\[eq:depth-domain\]](#eq:depth-domain){reference-type="eqref" reference="eq:depth-domain"}, $$\label{eq:W-bound}
 \boxed{
 \mathfrak W_k(L_k)
 \le
 \frac{q^{-2}\lambda^{-2\eta_k}}{1-s}
 \rho_N^ku^{-L_k}
 +\frac{48}{1-t}\rho_T^kv^{-L_k}.}$$ Consequently, if $L_k=o(k)$, then $$\label{eq:W-root}
 \boxed{
 \limsup_{k\to\infty}\mathfrak W_k(L_k)^{1/k}
 \le\rho_N<\frac{1419857}{1600000}<1.}$$

The triangle inequality in [\[eq:p-type\]](#eq:p-type){reference-type="eqref" reference="eq:p-type"} and [\[eq:tau-cap\]](#eq:tau-cap){reference-type="eqref" reference="eq:tau-cap"} give $$\begin{aligned}
 x^{-N_k/2}\sum_{n\ge N_k}|\tau_{\sigma,n}|R^n
 &\le \frac{q^{-2}\sigma^{-1}}{1-s}
       \left(\frac{s}{\sqrt x}\right)^{N_k}\\
 &=\frac{q^{-2}\lambda^{-2\eta_k}}{1-s}
   (\lambda^2u^2)^k u^{-L_k}.\end{aligned}$$ Likewise [\[eq:a-cap\]](#eq:a-cap){reference-type="eqref" reference="eq:a-cap"} gives $$\begin{aligned}
 x^{-N_k/2}\sum_{n\ge N_k}|a_n|R^n
 &<\frac{48}{1-t}
       \left(\frac{t}{\sqrt x}\right)^{N_k}\\
 &=\frac{48}{1-t}(v^2)^kv^{-L_k}.\end{aligned}$$ These are the two terms in [\[eq:W-bound\]](#eq:W-bound){reference-type="eqref" reference="eq:W-bound"}. Bounded phase and $L_k=o(k)$ make every factor outside $\rho_N^k$ and $\rho_T^k$ subexponential. Apply the standard root bound for a sum and [\[eq:rate-certificates\]](#eq:rate-certificates){reference-type="eqref" reference="eq:rate-certificates"}.

The theorem is stronger than a finite near-alias-band estimate: it controls every order from $N_k$ to infinity. It is also parity-free. The only order-specific information is the moving lower cut.

# The complete near-alias logarithmic band

Define the alias-clock logarithmic tail and band $$\begin{aligned}
 \mathfrak T_k(L_k)
 &=x^{-k}\sum_{n\ge N_k}
   \frac{|p_{\sigma,k,n}|R^n}{n},
 \label{eq:T}\\
 \mathfrak B_k(L_k)
 &=x^{-k}\sum_{N_k\le n<4k}
   \frac{|p_{\sigma,k,n}|R^n}{n}.
 \label{eq:B}\end{aligned}$$

[\[cor:band\]]{#cor:band label="cor:band"} For every depth sequence in [\[eq:depth-domain\]](#eq:depth-domain){reference-type="eqref" reference="eq:depth-domain"}, $$\label{eq:T-from-W}
 \mathfrak B_k(L_k)\le\mathfrak T_k(L_k)
 \le\frac{x^{-L_k/2}}{N_k}\mathfrak W_k(L_k).$$ In particular, if $L_k=o(k)$, then $$\label{eq:B-root}
 \boxed{
 \limsup_{k\to\infty}\mathfrak T_k(L_k)^{1/k}
 \le\rho_N<1,\qquad
 \limsup_{k\to\infty}\mathfrak B_k(L_k)^{1/k}
 \le\rho_N<1.}$$

The first inequality is nonnegativity. Since $n\ge N_k$ and $k-N_k/2=L_k/2$, $$\mathfrak T_k(L_k)
 \le\frac{x^{-k}}{N_k}\sum_{n\ge N_k}|p_{\sigma,k,n}|R^n
 =\frac{x^{-L_k/2}}{N_k}\mathfrak W_k(L_k).$$ For $L_k=o(k)$, the additional factors have $k$th root tending to one. Apply [\[thm:W\]](#thm:W){reference-type="ref" reference="thm:W"}.

The band in [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} contains both parities, the critical order $2k$, the first-lower order $2k-2$ whenever it lies above the lower cut, and every upper-alias order $2k<n<4k$. This statement concerns the direct coefficient $p$ only. It does not assert all-order decompositions of the form $Y+\mathcal P-S$.

# Linear-depth frontiers

The source estimates allow a strict extension beyond sublinear depth. Let $$\label{eq:ell}
 \ell=\limsup_{k\to\infty}\frac{L_k}{k}\in[0,2].$$

[\[thm:frontiers\]]{#thm:frontiers label="thm:frontiers"} For the two normalized tails, $$\begin{aligned}
 \limsup_{k\to\infty}\mathfrak W_k(L_k)^{1/k}
 &\le\max\{\rho_Nu^{-\ell},\rho_Tv^{-\ell}\},
 \label{eq:W-linear}\\
 \limsup_{k\to\infty}\mathfrak T_k(L_k)^{1/k}
 &\le\max\{\rho_Ns^{-\ell},\rho_Tt^{-\ell}\}.
 \label{eq:T-linear}\end{aligned}$$ Define $$\label{eq:alphas}
 \alpha_{\rm nat}
 =\frac{\log(1/\rho_N)}{\log(1/u)},
 \qquad
 \alpha_{\rm alias}
 =\frac{\log(1/\rho_N)}{\log(1/s)}.$$ Then $0<\alpha_{\rm nat}<\alpha_{\rm alias}<2$. The bound [\[eq:W-linear\]](#eq:W-linear){reference-type="eqref" reference="eq:W-linear"} is strictly subunit for $\ell<\alpha_{\rm nat}$, and [\[eq:T-linear\]](#eq:T-linear){reference-type="eqref" reference="eq:T-linear"} is strictly subunit for $\ell<\alpha_{\rm alias}$.

Apply [\[eq:W-bound\]](#eq:W-bound){reference-type="eqref" reference="eq:W-bound"} along the definition of the upper limit. This gives [\[eq:W-linear\]](#eq:W-linear){reference-type="eqref" reference="eq:W-linear"}. Combining [\[eq:T-from-W\]](#eq:T-from-W){reference-type="eqref" reference="eq:T-from-W"} with $x^{-\ell/2}u^{-\ell}=s^{-\ell}$ and $x^{-\ell/2}v^{-\ell}=t^{-\ell}$ gives [\[eq:T-linear\]](#eq:T-linear){reference-type="eqref" reference="eq:T-linear"}.

The noisy thresholds in [\[eq:alphas\]](#eq:alphas){reference-type="eqref" reference="eq:alphas"} are positive because $\rho_N<1$, and $u<s<1$ gives $\alpha_{\rm nat}<\alpha_{\rm alias}$. At depth two, $$\rho_Nu^{-2}=\lambda^2>1,
 \qquad
 \rho_Ns^{-2}=\frac{r_H^2\lambda^3}{R^2}
 >\frac{R}{r_H}=\frac{28}{17}>1,$$ so both noisy thresholds are below two. The target threshold for [\[eq:W-linear\]](#eq:W-linear){reference-type="eqref" reference="eq:W-linear"} is exactly two because $\rho_T=v^2$. For the alias normalization, $\rho_Tt^{-2}=x^{-1}<1$, so the target term is still subunit through the whole permitted interval $[0,2]$. Hence the noisy terms determine the stated frontiers.

Substitution of the archived physical decimal for $\lambda$ gives the diagnostics $$\alpha_{\rm nat}=0.263953\ldots,
 \qquad \alpha_{\rm alias}=0.441576\ldots.$$ They are descriptive evaluations of the exact formulas, not interval certificates and not finite evidence for the theorem.

At the alias frontier the polynomial factor in the logarithmic tail still matters.

[\[prop:critical\]]{#prop:critical label="prop:critical"} If $$\label{eq:critical-condition}
 \rho_N^ks^{-L_k}=o(N_k),
 \qquad \rho_T^kt^{-L_k}=o(N_k),$$ then $\mathfrak T_k(L_k)\to0$ and hence $\mathfrak B_k(L_k)\to0$. In particular, $$\label{eq:critical-linear}
 L_k=\alpha_{\rm alias}k+O(1)$$ implies $\mathfrak T_k(L_k)=O(k^{-1})$.

Insert [\[eq:W-bound\]](#eq:W-bound){reference-type="eqref" reference="eq:W-bound"} into [\[eq:T-from-W\]](#eq:T-from-W){reference-type="eqref" reference="eq:T-from-W"}; the two terms are fixed bounded factors times the ratios in [\[eq:critical-condition\]](#eq:critical-condition){reference-type="eqref" reference="eq:critical-condition"}. Under [\[eq:critical-linear\]](#eq:critical-linear){reference-type="eqref" reference="eq:critical-linear"}, the noisy numerator is bounded because $\rho_N=s^{\alpha_{\rm alias}}$. The target numerator remains exponentially small because its root at $\alpha_{\rm alias}<2$ is strictly subunit. Finally $N_k\asymp k$.

The critical statement is an upper-bound theorem only. It does not assert that the source estimate is sharp for the actual coefficient.

# Normalization and claim boundary

Remove the factor $x^{-k}$ from the near-alias logarithmic budget. At every sublinear depth, the RH-282 separate noisy majorant has root $$\label{eq:raw-root}
 \lambda^2(qR)^2=x\rho_N.$$ The certified lower multiplier bound gives $$\label{eq:raw-superunit}
 \lambda^2(qR)^2
 >\left(\frac{28}{17}\right)^2\left(\frac7{10}\right)^2
 =\frac{9604}{7225}>1.$$ The separate deterministic majorant has root $(q_*R)^2<1$. Therefore the two absolute source caps cannot prove unnormalized direct-band closure. This is a strict scoped failure of the modulus-cap method, not a lower bound for $p=\tau-a$: additional signed or complex cancellation may be present.

The normalized theorem also does not close the full-trace off-alias budget. Equation [\[eq:p-type\]](#eq:p-type){reference-type="eqref" reference="eq:p-type"} gives only $$\label{eq:pqd}
 p_{\sigma,k,n}=q_{\sigma,k,n}-d_{\sigma,k,n}.$$ RH-340 proves that transfer between direct and full-trace prefix budgets requires a same-clock estimate for the head/counterloop defect $d$. No such estimate is supplied here. Thus the new parity-free direct theorem is not a theorem for $E_{\rm off}$ [@WangSynchronization2026; @WangBoundaryGap2026].

The executable artifact checks the exact rational identities in [\[eq:geometric\]](#eq:geometric){reference-type="eqref" reference="eq:geometric"}--[\[eq:rate-certificates\]](#eq:rate-certificates){reference-type="eqref" reference="eq:rate-certificates"}, the two finite geometric majorants, the linear root functions, and the superunit raw certificate. Its finite rows use the in-range rational fixture $\lambda=5/3$ and both odd and even lower cuts. They reproduce formulas only; they are not observations of $\tau$, $a$, $p$, the noisy operator, or an asymptotic sequence.

RH-354 proves an actual normalized direct-coefficient tail theorem. It does not control the low prefix $2\le n<N_k$, prove head transport, identify the direct budget with full $E_{\rm off}$, close the RH-241 moving noisy all-order envelope or coefficient bridge, or activate RH-288. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt-weighted prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
