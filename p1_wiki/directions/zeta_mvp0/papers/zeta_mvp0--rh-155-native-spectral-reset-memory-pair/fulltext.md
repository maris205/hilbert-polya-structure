---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-155-native-spectral-reset-memory-pair"
canonical_tex: "zeta_mvp0/papers/RH-155-native-spectral-reset-memory-pair/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-155-native-spectral-reset-memory-pair/main.pdf"
source_sha256: "2510b974a864ec35ebc36d646739bf1319fbc9ac38427a9306239f158c780389"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Native Spectral-Reset Memory Pairs A Universal Tail-Mass Theorem and 130 Subunit Loewner Certificates

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-155-native-spectral-reset-memory-pair>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-155-native-spectral-reset-memory-pair/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-155-native-spectral-reset-memory-pair/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-155-native-spectral-reset-memory-pair/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-155-native-spectral-reset-memory-pair/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-153 proved that a correlated Gram--tail pair transports through reset overlaps without changing its generalized tail ratio, and RH-154 isolated a well-conditioned terminal half. The missing object was a native pair on the spectral reset packet itself.

  Let a geometric memory be $M_t=R_t+T_t$, where $R_t$ contains ages below a fixed depth $d$ and $T_t$ contains the older terms. Each normalized snapshot is positive semidefinite with trace one, so $$\|T_t\|\leq\tau_t:=\sum_{a=d}^{t}\eta^a
   \leq\frac{\eta^d}{1-\eta}.$$ If $U_t$ is the rank-$r$ top spectral packet of $M_t$ and $\lambda_r(M_t)\geq\ell_t>\tau_t$, then for the native compressions $G_t=U_t^*R_tU_t$ and $D_t=U_t^*T_tU_t$ we prove the sharp bound $$D_t\preceq\frac{\tau_t}{\ell_t-\tau_t}G_t.$$ The ratio is subunit exactly at the scalar-information gate $\ell_t>2\tau_t$.

  Combining the dynamics-free tail mass with the RH-151 outward selected eigenvalue lowers certifies all 130 frozen snapshots. The worst ratio upper is $0.224696$ and the minimum $\ell_t/(2\tau_t)$ margin is $2.72523$. All 62 RH-154 terminal-half snapshots also certify. Direct nominal ratios are much smaller---at most $2.879\times10^{-5}$---but are not needed for the proof. This closes a native reset memory pair. It does not yet identify that pair with the directional cross-action Gram used in the earlier support architecture.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Native Spectral-Reset Memory Pairs\
  A Universal Tail-Mass Theorem and 130 Subunit Loewner Certificates
```

## Markdown 正文

# A reset pair that respects the memory construction

Let $S_j\succeq0$ with $\operatorname{tr}S_j=1$ and fix $0\leq\eta<1$. At time $t$ define $$M_t=\sum_{a=0}^{t}\eta^aS_{t-a},\quad
 R_t=\sum_{0\leq a<d}\eta^aS_{t-a},\quad
 T_t=\sum_{d\leq a\leq t}\eta^aS_{t-a}.$$ Empty sums are zero. Then $M_t=R_t+T_t$ exactly. Unlike an arbitrary ambient recent Gram, $R_t$ may be singular. Positivity is recovered only after compressing to a packet selected by the full memory.

# Universal tail mass and packet recovery

[\[thm:mass\]]{#thm:mass label="thm:mass"} For every snapshot sequence, $$0\preceq T_t\preceq\tau_t I,
 \qquad
 \tau_t=\sum_{a=d}^{t}\eta^a
 \leq\tau_\infty:=\frac{\eta^d}{1-\eta}.$$ The constants are sharp from trace-one positivity alone.

Every eigenvalue of a positive trace-one matrix lies in $[0,1]$, so $S_j\preceq I$. Sum the weighted inequalities. Rank-one snapshots aligned with one fixed direction attain the operator upper.

Let $U$ have orthonormal columns spanning the top $r$ eigenspace of $M$ and assume $\lambda_r(M)\geq\ell>0$. Define $$H=U^*MU,\qquad G=U^*RU,\qquad D=U^*TU.$$

[\[thm:pair\]]{#thm:pair label="thm:pair"} If $\|T\|\leq\tau<\ell$, then $$H\succeq\ell I,\quad D\preceq\tau I,\quad
 G=H-D\succeq(\ell-\tau)I,$$ and therefore $$D\preceq xG,qquad x=\frac{\tau}{\ell-\tau}.$$ Also $D\preceq yH$ with $y=\tau/\ell$ and $x=y/(1-y)$. All constants are sharp for the available scalar endpoints.

The spectral definition of $U$ gives $H\succeq\ell I$. Theorem [\[thm:mass\]](#thm:mass){reference-type="ref" reference="thm:mass"} gives $D\preceq\tau I$, hence $G=H-D\succeq(\ell-\tau)I$. Combining the last two scalar matrix bounds gives $D\preceq\tau(\ell-\tau)^{-1}G$. A one-dimensional pair with $H=\ell$ and $D=\tau$ attains every displayed endpoint [@Bhatia1997; @HornJohnson2013].

[\[cor:gate\]]{#cor:gate label="cor:gate"} The bound in Theorem [\[thm:pair\]](#thm:pair){reference-type="ref" reference="thm:pair"} is below one exactly when $\ell>2\tau$. At equality, the endpoint information permits $D=G$; when $\ell<2\tau$, it permits $D\succ G$.

This criterion converts the tail problem into one selected-eigenvalue lower. The tail side is universal and already uniform in time.

# The 130-snapshot audit

We use $\eta=1/512$ and depth $d=5$, giving $$\tau_\infty=\frac{(1/512)^5}{1-1/512}
 =2.8477329214\times10^{-14}.$$ At each frozen snapshot, RH-151 supplies an Arb ambient matrix radius and a polar-corrected spectral-center error. Subtracting both from the nominal selected eigenvalue gives the outward $\ell_t$. No reset-frame perturbation is inserted: Theorem [\[thm:pair\]](#thm:pair){reference-type="ref" reference="thm:pair"} uses the exact spectral packet and is therefore correlation preserving.

All 130 snapshots pass $\ell_t>2\tau_t$. Eighty have an active old tail; the earlier fifty have $T_t=0$. The worst ratio upper is $0.2246959$ at the terminal $\sigma=0.01$ left snapshot. Its margin is still $\ell_t/(2\tau_t)=2.72523$. The other fine terminal ratios are $0.16128$, $0.08926$, and $0.07327$, while all coarser maxima are below $0.00104$.

The RH-154 terminal-half selection contains 62 target snapshots and all 62 remain subunit. Because the worst weak eigenvalue is terminal, delayed start does not improve the maximum tail upper; its purpose was to remove overlap birth conditioning, not terminal spectral thinning.

For diagnosis we also directly compress the nominal recent and tail matrices onto the nominal reset frames. The largest observed generalized ratio is $2.8789\times10^{-5}$ and every nominal value lies below the universal certificate. The large gap shows conservatism, but the universal theorem is already strong enough for a finite support factor.

![Subunit native memory-pair bounds, channel maxima, sharp gate margins, and comparison with direct nominal generalized ratios.](<../../../../../zeta_mvp0/papers/RH-155-native-spectral-reset-memory-pair/figures/native_spectral_reset_memory_pair.pdf>){#fig:audit width="\\textwidth"}

# Consequence and claim boundary

RH-155 supplies the correlated object required by RH-153. On any certified snapshot, the native recent Gram is positive definite and the old tail is a strictly subunit Loewner fraction of it. Congruence transport preserves that fraction exactly, so no inverse-overlap square is incurred.

The remaining conceptual interface is important: $G_t=U_t^*R_tU_t$ is a native memory Gram, whereas RH-130--RH-148 used a recent projected-cross action Gram and additional wedge/capacity factors. We have not proved those objects equivalent, supplied an all-level selected-eigenvalue lower, closed Stage A, constructed a Hilbert--Polya operator, identified zeta zeros, or proved the Riemann Hypothesis.
