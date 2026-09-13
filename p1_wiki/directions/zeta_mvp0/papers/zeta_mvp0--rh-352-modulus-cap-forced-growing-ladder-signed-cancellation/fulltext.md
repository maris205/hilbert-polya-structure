---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-352-modulus-cap-forced-growing-ladder-signed-cancellation"
canonical_tex: "zeta_mvp0/papers/RH-352-modulus-cap-forced-growing-ladder-signed-cancellation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-352-modulus-cap-forced-growing-ladder-signed-cancellation/main.pdf"
source_sha256: "c911d2be76029f026d4681c22ed046558d4e7c56a5a936714cf86fc4452ab521"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Modulus-Cap-Forced Growing-Ladder Signed Cancellation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-352-modulus-cap-forced-growing-ladder-signed-cancellation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-352-modulus-cap-forced-growing-ladder-signed-cancellation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-352-modulus-cap-forced-growing-ladder-signed-cancellation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-352-modulus-cap-forced-growing-ladder-signed-cancellation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-352-modulus-cap-forced-growing-ladder-signed-cancellation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove an actual moving-order theorem on the triangular lower-even window of RH-350. Let $m_{k,j}=k-j$, $2\le j\le J_k$, where $J_k\to\infty$ and $J_k=o(k)$. The direct physical coefficient has the two source-locked representations $$p_{k,j}=\tau_{\sigma,2m_{k,j}}-a_{2m_{k,j}}
   =Y_{k,j}+\mathcal P_{k,j}-S_{k,j}.$$ The modulus-complete spectral tail gives $|\tau_{\sigma,n}|\le\sigma^{-1}2^{2-n}$, while the deterministic target envelope gives $|a_n|<48q_*^n$ with $q_*=(r_H\lambda)^{-1}$. For $H_m=mR^{-2m}$, $R=7/5$, and $x=(R/(r_H\sqrt\lambda))^2$, these separate bounds become jointly subunit on the local natural scale: $$\limsup_{k\to\infty}
   \left(
    \sup_{2\le j\le J_k}
    \frac{|p_{k,j}|}{2H_{m_{k,j}}x^{m_{k,j}}}
   \right)^{1/k}
   \le
   \max\left\{\frac{r_H^2\lambda^3}{4},\frac1\lambda\right\}<1.$$ The noisy rate is strictly below $1419857/1600000$. Hence the actual normalized selected direct budget decays exponentially. Combining this with RH-350 forces the actual signed remainder to track $S-\mathcal P$ uniformly at the natural scale and gives $$\mathcal Y_k^{\rm act}
   =\frac{F_{J_k-2}(a_k)}{C_M}+o(1),
   \qquad
   \liminf\mathcal Y_k^{\rm act}\ge
   \frac1{C_M}\left(\frac1{x-1}-\frac1{x\lambda-1}\right)>0.$$ Thus RH-350's aggregate small-$Y$ hypothesis is false for the actual coefficients. This is normalized selected-ladder cancellation only. The unnormalized noisy modulus majorant has root $\lambda^2(qR)^2>9604/7225>1$, so it yields no unnormalized prefix closure. The full off-alias aggregate, RH-288, Gates A--E, and every Riemann-hypothesis claim remain open.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: 'Modulus-Cap-Forced Growing-Ladder Signed Cancellation'
```

## Markdown 正文

# Source-locked actual coefficient

Fix the physical constants $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad q=\frac12,\qquad R=\frac75,
 \qquad \frac{28}{17}<\lambda<\frac{17}{10}.$$ The lower inequality is the strict deterministic boundary certificate of RH-262, and the upper inequality follows from the algebraic multiplier certificate in RH-336 [@WangBoundaryBudget2026; @WangProjectorMass2026]. Put $$\label{eq:scales}
 \beta=\frac1{r_H\sqrt\lambda},\qquad
 q_*=\frac1{r_H\lambda},\qquad
 H_m=mR^{-2m},\qquad
 x=(\beta R)^2.$$ Then $$\label{eq:x-identities}
 x\lambda=\left(\frac{R}{r_H}\right)^2
 =\left(\frac{28}{17}\right)^2>2,
 \qquad x>1,
 \qquad q_*R=\frac{28}{17\lambda}<1.$$

Let $\sigma=\sigma_k\downarrow0$ follow the physical natural clock and define its bounded phase by $$\label{eq:clock}
 \eta_k=k-\frac{\log(1/\sigma_k)}{2\log\lambda},
 \qquad \sup_k|\eta_k|<\infty.$$ Thus, exactly, $$\label{eq:sigma-clock}
 \sigma_k^{-1}=\lambda^{2(k-\eta_k)}.$$ Take any integer-valued depth satisfying $$\label{eq:window}
 J_k\longrightarrow\infty,\qquad J_k=o(k),\qquad J_k\ge3,$$ and set $$\label{eq:indices}
 m_{k,j}=k-j,\qquad n_{k,j}=2m_{k,j},\qquad 2\le j\le J_k.$$ Since $k-J_k\to\infty$, the whole window eventually lies in the physical RH-348 ladder.

RH-282 constructs the modulus-complete normal spectral complement $C_\sigma$ and proves $$\label{eq:tau-bound}
 \tau_{\sigma,n}=\operatorname{Tr}C_\sigma^n,\qquad
 |\tau_{\sigma,n}|\le\sigma^{-1}q^{n-2}\quad(n\ge2).$$ RH-267 proves the all-order deterministic numerator bound $$\label{eq:a-bound}
 |a_n|<48q_*^n\quad(n\ge2).$$ These are different source estimates, but RH-288 and RH-340 identify their difference as one actual direct coefficient: $$\label{eq:p-tau-a}
 p_{\sigma,k,n}=\tau_{\sigma,n}-a_n.$$ Equations [\[eq:tau-bound\]](#eq:tau-bound){reference-type="eqref" reference="eq:tau-bound"}--[\[eq:p-tau-a\]](#eq:p-tau-a){reference-type="eqref" reference="eq:p-tau-a"} are respectively the modulus-complement, deterministic-target, and direct-coefficient data types; no head/counterloop substitution is made [@WangSpectralTail2026; @WangUnifiedEnvelope2026; @WangGluing2026; @WangSynchronization2026].

On the lower-even ladder, RH-348 supplies the second exact representation $$\label{eq:p-YPS}
 \boxed{
 p_{k,j}:=p_{\sigma,k,2m_{k,j}}
 =Y_{k,j}+\mathcal P_{k,j}-S_{k,j},}$$ where $$\label{eq:Y-actual}
 Y_{k,j}=\mathcal T_{k,m_{k,j}}^{\rm rest}
          -d_{\sigma,k,2m_{k,j}}.$$ This $Y$ is an actual signed physical remainder, not a free completion variable [@WangLowerLadder2026; @WangSignedCompletion2026].

Finally, RH-350 proves, uniformly on [\[eq:window\]](#eq:window){reference-type="eqref" reference="eq:window"}, $$\begin{aligned}
 \epsilon_k^S&:=
 \sup_j\left|
 \frac{C_MS_{k,j}}{2H_{m_{k,j}}x^{m_{k,j}}}-1
 \right|\longrightarrow0,
 \label{eq:S-uniform}\\
 \epsilon_k^P&:=
 \sup_j\left|
 \frac{C_M\mathcal P_{k,j}}{2H_{m_{k,j}}x^{m_{k,j}}}
 -a_k\lambda^{2-j}
 \right|\longrightarrow0,
 \label{eq:P-uniform}\end{aligned}$$ where $C_M>0$ is fixed and $a_k=C_*C_M\lambda^{\eta_k-2}>0$ [@WangGrowingSidebands2026]. The new input below is not another estimate of $S$ or $\mathcal P$; it is the direct bound on the actual $p$ supplied by [\[eq:tau-bound\]](#eq:tau-bound){reference-type="eqref" reference="eq:tau-bound"} and [\[eq:a-bound\]](#eq:a-bound){reference-type="eqref" reference="eq:a-bound"}.

# Exponential local natural-scale theorem

Define $$\label{eq:U}
 U_k=\sup_{2\le j\le J_k}
 \frac{|p_{k,j}|}{2H_{m_{k,j}}x^{m_{k,j}}},$$ and the two fixed root rates $$\label{eq:rates}
 \rho_N=\frac{r_H^2\lambda^3}{4},
 \qquad \rho_T=\frac1\lambda.$$

[\[thm:uniform-cap\]]{#thm:uniform-cap label="thm:uniform-cap"} For every clock and growing window satisfying [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}--[\[eq:window\]](#eq:window){reference-type="eqref" reference="eq:window"}, $$\label{eq:U-rate}
 \boxed{
 \limsup_{k\to\infty}U_k^{1/k}
 \le\max\{\rho_N,\rho_T\}<1.}$$ More precisely, $$\label{eq:rate-certificates}
 \rho_N<\frac{1419857}{1600000}<1,
 \qquad
 \rho_T<\frac{17}{28}<1.$$

Write $m=m_{k,j}$. Since $2H_mx^m=2m\beta^{2m}$, [\[eq:tau-bound\]](#eq:tau-bound){reference-type="eqref" reference="eq:tau-bound"} gives $$\begin{aligned}
 \frac{|\tau_{\sigma,2m}|}{2H_mx^m}
 &\le \frac{\sigma^{-1}q^{2m-2}}{2m\beta^{2m}}\notag\\
 &=\frac{2}{m}\sigma^{-1}
       (q^2r_H^2\lambda)^m.\label{eq:noisy-coordinate}\end{aligned}$$ Put $$\label{eq:bN}
 b_N=q^2r_H^2\lambda.$$ The upper bound on $\lambda$ gives $b_N<4913/16000<1$. Using [\[eq:sigma-clock\]](#eq:sigma-clock){reference-type="eqref" reference="eq:sigma-clock"} and $m=k-j$, the right side of [\[eq:noisy-coordinate\]](#eq:noisy-coordinate){reference-type="eqref" reference="eq:noisy-coordinate"} becomes $$\label{eq:noisy-factorization}
 \frac{2\lambda^{-2\eta_k}}{m}
 \rho_N^k b_N^{-j}.$$ Here $m\ge k-J_k$, the phase factor is bounded, and $b_N^{-J_k}=\exp(o(k))$. Therefore $$\label{eq:noisy-root}
 \limsup_{k\to\infty}
 \left(
 \sup_j\frac{|\tau_{\sigma,2m_{k,j}}|}
 {2H_{m_{k,j}}x^{m_{k,j}}}
 \right)^{1/k}
 \le\rho_N.$$

For the target, [\[eq:a-bound\]](#eq:a-bound){reference-type="eqref" reference="eq:a-bound"} and $q_*^2/\beta^2=1/\lambda$ give $$\label{eq:target-coordinate}
 \frac{|a_{2m}|}{2H_mx^m}
 <\frac{24}{m}\left(\frac1\lambda\right)^m
 =\frac{24}{m}\lambda^{-k}\lambda^j.$$ Since $j\le J_k=o(k)$, $$\label{eq:target-root}
 \limsup_{k\to\infty}
 \left(
 \sup_j\frac{|a_{2m_{k,j}}|}
 {2H_{m_{k,j}}x^{m_{k,j}}}
 \right)^{1/k}
 \le\rho_T.$$ The triangle inequality in [\[eq:p-tau-a\]](#eq:p-tau-a){reference-type="eqref" reference="eq:p-tau-a"} and the standard root bound for a sum of nonnegative sequences prove [\[eq:U-rate\]](#eq:U-rate){reference-type="eqref" reference="eq:U-rate"}.

Finally, $r_H=17/20$ and $\lambda<17/10$ imply $$\rho_N<\frac{(17/20)^2(17/10)^3}{4}
 =\frac{1419857}{1600000}<1.$$ The lower bound $\lambda>28/17$ gives $\rho_T<17/28<1$.

The theorem is genuinely uniform on a moving window. The factors generated by $J_k$ are subexponential because $J_k=o(k)$; no finite collection of fixed-$j$ limits is promoted to a growing-order claim.

Define the actual normalized selected direct budget $$\label{eq:L-act}
 \mathcal L_k^{\rm act}
 =\frac1{x^{k-2}}
 \sum_{j=2}^{J_k}\frac{|p_{k,j}|}{2H_{m_{k,j}}}.$$

[\[cor:L\]]{#cor:L label="cor:L"} One has $$\label{eq:L-root}
 \boxed{
 \limsup_{k\to\infty}(\mathcal L_k^{\rm act})^{1/k}
 \le\max\{\rho_N,\rho_T\}<1,}$$ and hence $\mathcal L_k^{\rm act}\to0$ exponentially.

Since $m_{k,j}=k-j$, $$\begin{aligned}
 \mathcal L_k^{\rm act}
 &=\sum_{j=2}^{J_k}x^{2-j}
 \frac{|p_{k,j}|}{2H_{m_{k,j}}x^{m_{k,j}}}\\
 &\le U_k\sum_{j=2}^{\infty}x^{2-j}
 =\frac{U_k}{1-x^{-1}}.\end{aligned}$$ The fixed geometric factor has $k$th root tending to one, so [\[thm:uniform-cap\]](#thm:uniform-cap){reference-type="ref" reference="thm:uniform-cap"} proves the result.

# Forced actual signed completion

The exact identity [\[eq:p-YPS\]](#eq:p-YPS){reference-type="eqref" reference="eq:p-YPS"} can now be solved for the actual remainder without changing data type: $$\label{eq:Y-solve}
 Y_{k,j}=S_{k,j}-\mathcal P_{k,j}+p_{k,j}.$$

[\[thm:Y-tracking\]]{#thm:Y-tracking label="thm:Y-tracking"} On every window [\[eq:window\]](#eq:window){reference-type="eqref" reference="eq:window"}, $$\label{eq:Y-tracking}
 \boxed{
 \sup_{2\le j\le J_k}
 \left|
 \frac{C_MY_{k,j}}{2H_{m_{k,j}}x^{m_{k,j}}}
 -\bigl(1-a_k\lambda^{2-j}\bigr)
 \right|\longrightarrow0.}$$ Thus the actual $Y$ array asymptotically tracks the RH-351 close completion $S-\mathcal P$ at the local natural scale.

Substitute [\[eq:Y-solve\]](#eq:Y-solve){reference-type="eqref" reference="eq:Y-solve"} and apply the triangle inequality. The left side of [\[eq:Y-tracking\]](#eq:Y-tracking){reference-type="eqref" reference="eq:Y-tracking"} is at most $$\epsilon_k^S+\epsilon_k^P+C_MU_k.$$ The first two terms vanish by [\[eq:S-uniform\]](#eq:S-uniform){reference-type="eqref" reference="eq:S-uniform"}--[\[eq:P-uniform\]](#eq:P-uniform){reference-type="eqref" reference="eq:P-uniform"}; the last vanishes exponentially by [\[thm:uniform-cap\]](#thm:uniform-cap){reference-type="ref" reference="thm:uniform-cap"}.

For $N\ge0$ recall the RH-350 weighted functional $$\label{eq:F}
 F_N(a)=\sum_{r=0}^{N}x^{-r}|a\lambda^{-r}-1|.$$ Its exact minimum is $$\begin{aligned}
 A_N:=\inf_{a>0}F_N(a)
 &=\frac{1-x^{-N}}{x-1}
 -\frac{1-(x\lambda)^{-N}}{x\lambda-1},\label{eq:AN}\\
 A_N&\nearrow A_\infty
 =\frac1{x-1}-\frac1{x\lambda-1}>0.
 \label{eq:Ainf}\end{aligned}$$ Define the actual normalized selected signed-remainder budget $$\label{eq:Yagg}
 \mathcal Y_k^{\rm act}
 =\frac1{x^{k-2}}
 \sum_{j=2}^{J_k}\frac{|Y_{k,j}|}{2H_{m_{k,j}}}.$$

[\[cor:Yagg\]]{#cor:Yagg label="cor:Yagg"} With $N_k=J_k-2$, $$\label{eq:Yagg-law}
 \boxed{
 \mathcal Y_k^{\rm act}
 =\frac{F_{N_k}(a_k)}{C_M}+o(1),}$$ and $$\label{eq:Yagg-liminf}
 \boxed{
 \liminf_{k\to\infty}\mathcal Y_k^{\rm act}
 \ge\frac{A_\infty}{C_M}
 =\frac1{C_M}
 \left(\frac1{x-1}-\frac1{x\lambda-1}\right)>0.}$$ Consequently the actual aggregate small-$Y$ hypothesis used conditionally in RH-350 is false.

Let $$z_{k,j}=\frac{C_MY_{k,j}}
 {2H_{m_{k,j}}x^{m_{k,j}}}.$$ By [\[thm:Y-tracking\]](#thm:Y-tracking){reference-type="ref" reference="thm:Y-tracking"}, uniformly in $j$, $z_{k,j}=1-a_k\lambda^{2-j}+o(1)$. Since $||z|-|w||\le|z-w|$ and $\sum_{j=2}^{\infty}x^{2-j}<\infty$, $$\begin{aligned}
 \mathcal Y_k^{\rm act}
 &=\frac1{C_M}
 \sum_{j=2}^{J_k}x^{2-j}|z_{k,j}|\\
 &=\frac1{C_M}
 \sum_{j=2}^{J_k}x^{2-j}
 |1-a_k\lambda^{2-j}|+o(1)\\
 &=\frac{F_{J_k-2}(a_k)}{C_M}+o(1).\end{aligned}$$ Because $a_k>0$, [\[eq:AN\]](#eq:AN){reference-type="eqref" reference="eq:AN"} gives $F_{N_k}(a_k)\ge A_{N_k}$. Now $N_k\to\infty$, so [\[eq:Ainf\]](#eq:Ainf){reference-type="eqref" reference="eq:Ainf"} proves [\[eq:Yagg-liminf\]](#eq:Yagg-liminf){reference-type="eqref" reference="eq:Yagg-liminf"}.

This conclusion is about the actual $Y$ in [\[eq:Y-actual\]](#eq:Y-actual){reference-type="eqref" reference="eq:Y-actual"}, not a formal coefficient ledger. It nevertheless remains local to the selected lower-even window and to the normalization in [\[eq:Yagg\]](#eq:Yagg){reference-type="eqref" reference="eq:Yagg"}.

# Why the unnormalized prefix remains open

Remove the factor $x^{m}$ from the denominator in [\[eq:noisy-coordinate\]](#eq:noisy-coordinate){reference-type="eqref" reference="eq:noisy-coordinate"}. The RH-282 modulus estimate then gives the explicit separate majorant $$\label{eq:raw-noisy-majorant}
 \frac{|\tau_{\sigma,2m}|}{2H_m}
 \le\widehat N_{k,j}
 :=\frac{2}{m}\sigma^{-1}(qR)^{2m}.$$ On the same window, bounded phase and $J_k=o(k)$ give $$\label{eq:raw-root}
 \lim_{k\to\infty}
 \left(\sup_{2\le j\le J_k}\widehat N_{k,j}\right)^{1/k}
 =\lambda^2(qR)^2.$$ This rate is strictly superunit: $$\label{eq:raw-superunit}
 \lambda^2(qR)^2
 >\left(\frac{28}{17}\right)^2
   \left(\frac7{10}\right)^2
 =\frac{9604}{7225}>1.$$ By contrast, the separate target majorant has unnormalized root $(q_*R)^2<1$. Equivalently, $$\label{eq:scale-conversion}
 x\rho_N=\lambda^2(qR)^2>1.$$

Equations [\[eq:raw-root\]](#eq:raw-root){reference-type="eqref" reference="eq:raw-root"}--[\[eq:scale-conversion\]](#eq:scale-conversion){reference-type="eqref" reference="eq:scale-conversion"} are a method boundary, not a lower bound for the actual coefficient. The actual difference $p=\tau-a$ may contain additional signed or complex cancellation, but the two separate absolute source bounds do not reveal it. Therefore [\[thm:uniform-cap\]](#thm:uniform-cap){reference-type="ref" reference="thm:uniform-cap"} and [\[cor:L\]](#cor:L){reference-type="ref" reference="cor:L"} cannot be multiplied by the removed $x^k$ scale to conclude that the unnormalized selected prefix tends to zero. Such a conclusion requires a stronger theorem directly on $\tau-a$.

# Executable protocol and claim boundary

The executable artifact performs exact rational checks of [\[eq:x-identities\]](#eq:x-identities){reference-type="eqref" reference="eq:x-identities"}, [\[eq:rate-certificates\]](#eq:rate-certificates){reference-type="eqref" reference="eq:rate-certificates"}, and [\[eq:raw-superunit\]](#eq:raw-superunit){reference-type="eqref" reference="eq:raw-superunit"}. At the in-range fixture $\lambda=5/3$ and $\eta_k=0$, it reproduces the finite coordinate majorants [\[eq:noisy-coordinate\]](#eq:noisy-coordinate){reference-type="eqref" reference="eq:noisy-coordinate"} and [\[eq:target-coordinate\]](#eq:target-coordinate){reference-type="eqref" reference="eq:target-coordinate"} on windows $J=\lfloor\sqrt{k}\rfloor$. It also checks the finite algebra $Y=S-\mathcal P+p$. These rows are formula-reproduction checks only: they are not observations of $\tau$, $a$, $p$, or $Y$, are not interval certificates for the physical multiplier, and are not asymptotic evidence.

RH-352 proves actual normalized/local natural-scale signed cancellation on one growing lower-even ladder. It does not prove that the unnormalized selected prefix vanishes; control the critical, first-lower, odd, or upper-alias orders; decide the full $E_{\rm off}$ aggregate; or prove the RH-241 moving noisy all-order envelope and coefficient bridge. It does not activate the RH-288 determinant-gluing criterion. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
