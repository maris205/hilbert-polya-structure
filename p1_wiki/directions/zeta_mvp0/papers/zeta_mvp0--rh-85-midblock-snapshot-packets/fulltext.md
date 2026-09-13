---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-85-midblock-snapshot-packets"
canonical_tex: "zeta_mvp0/papers/RH-85-midblock-snapshot-packets/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-85-midblock-snapshot-packets/main.pdf"
source_sha256: "6fee553450ad632bc2076990fb3f99b2a61f082eb572a8e839140d36294865e5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Midblock Snapshot Packets and Prefix-Only Captured-Energy Certificates Dynamic Right Spaces, a Prefix-Gramian No-Go, and 192-Bit Evidence

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-85-midblock-snapshot-packets>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-85-midblock-snapshot-packets/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-85-midblock-snapshot-packets/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-85-midblock-snapshot-packets/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-85-midblock-snapshot-packets/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-84 reduced the preferred Stage-A effective-rank corridor to captured energy in a clock-dimensional postcritical packet space. The optimal packet from the terminal singular-value decomposition is tautological, while raw coordinate and scale embeddings are not supported numerically. This paper constructs the first temporally intrinsic alternative: a right packet formed strictly before the terminal production horizon.

  For $X_j=A^jS$ and any rank-$r$ packet $V$, the snapshot transfer theorem is $$\left\lVert X_M(I-VV^*)\right\rVert_2
   \le \left\lVert A^{M-j}\right\rVert\,\left\lVert X_j(I-VV^*)\right\rVert_2.$$ Consequently the leading right singular space of $X_j$, computed from the prefix through time $j<M$, supplies a valid rank-$r$ approximation of the terminal state. This is a prefix-only certificate: the terminal singular vectors do not enter its construction.

  The natural unweighted prefix Gramian is not a safe replacement. An explicit two-channel diagonal family has a prefix Gramian dominated by a transient mode while its terminal state is asymptotically supported on the other mode; the resulting rank-one packet misses asymptotically all terminal energy.

  At the five archived scales we choose $j=\lceil2M/3\rceil$ and $r=\lceil H_\sigma\rceil+2$. Direct 192-bit Arb evaluation certifies a maximum relative terminal residual below $4.5\times10^{-6}$ and minimum captured energy above $0.99999999997$. By contrast, source-only packets leave up to $84.9\%$ relative residual and unweighted prefix-Gramian packets up to $32.6\%$. The audit proves finite frozen certificates, not an all-level packet-decay theorem. Stage A, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Midblock Snapshot Packets and Prefix-Only Captured-Energy Certificates\
  Dynamic Right Spaces, a Prefix-Gramian No-Go, and 192-Bit Evidence
```

## Markdown 正文

**Keywords:** dynamic packet; captured energy; snapshot transfer; effective rank; interval arithmetic; transient growth.

**MSC 2020:** 47B10; 47A75; 15A18; 65G20.

# From optimal tails to constructible packets

RH-77 discovered strong postblock compression at five scales [@WangRankCompression2026]; RH-82 supplied the half-logarithmic rank clock [@WangHalfLog2026]. RH-84 then showed that only a captured-energy lower bound is needed [@WangKyFan2026]. The remaining issue is to build a packet from the dynamics rather than from the terminal state itself.

Let $A:\mathcal H\to\mathcal H$ be bounded, let $S:\mathcal K\to\mathcal H$ be Hilbert--Schmidt, and set $X_j=A^jS$. A matrix $V:\mathbb C^r\to\mathcal K$ with orthonormal columns defines the right packet projection $P=VV^*$. The candidate $X_MP$ has rank at most $r$.

# The snapshot transfer theorem

[\[thm:transfer\]]{#thm:transfer label="thm:transfer"} For integers $0\le j\le M$ and every rank-$r$ orthogonal projection $P$ on $\mathcal K$, $$\boxed{\left\lVert X_M(I-P)\right\rVert_2
 \le \left\lVert A^{M-j}\right\rVert\,\left\lVert X_j(I-P)\right\rVert_2.}
 \label{eq:transfer}$$ If $P_{j,r}$ is the leading right singular projection of $X_j$, then $$\tau_r(X_M)
 \le \left\lVert X_M(I-P_{j,r})\right\rVert_2
 \le \left\lVert A^{M-j}\right\rVert\tau_r(X_j).
 \label{eq:optimal-transfer}$$ The packet $P_{j,r}$ depends only on the prefix ending at $j$.

The identity $X_M(I-P)=A^{M-j}X_j(I-P)$ and the ideal inequality $\left\lVert BC\right\rVert_2\le\left\lVert B\right\rVert\left\lVert C\right\rVert_2$ give [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"}. The leading right singular projection minimizes $\left\lVert X_j(I-P)\right\rVert_2$ among rank-$r$ projections by Eckart--Young [@Bhatia1997]. Since $X_MP_{j,r}$ has rank at most $r$, the first inequality in [\[eq:optimal-transfer\]](#eq:optimal-transfer){reference-type="eqref" reference="eq:optimal-transfer"} follows as well.

The theorem separates two tasks. One must prove a low-rank tail at an intermediate snapshot and control the unused suffix power. Importantly, one need not identify the terminal singular directions.

If $M-j=kb+s$, $0\le s<b$, $\left\lVert A^b\right\rVert\le q<1$, and $\max_{0\le t<b}\left\lVert A^t\right\rVert\le C_b$, then $$\left\lVert X_M(I-P_{j,r})\right\rVert_2\le C_bq^k\tau_r(X_j).$$

# Why the unweighted prefix Gramian is unsafe

One might aggregate every prefix snapshot and choose the leading eigenspace of $G_M=\sum_{j=0}^MX_j^*X_j$. The following proposition rules out a general terminal certificate of this form.

[\[prop:nogo\]]{#prop:nogo label="prop:nogo"} For every $M\ge1$, let $$A=\operatorname{diag}(1/2,1),\qquad
 S=\operatorname{diag}(\sqrt{2(M+1)},1).$$ The leading rank-one eigenspace of $G_M$ is the first coordinate, whereas the relative terminal residual left by that packet is $$\frac{1}{\sqrt{1+2(M+1)4^{-M}}}\longrightarrow1.$$

The two diagonal prefix energies are $$2(M+1)\frac{1-4^{-(M+1)}}{1-1/4}
 \quad\text{and}\quad M+1.$$ The first is larger, so the prefix Gramian selects the transient coordinate. At time $M$ the squared terminal energies are $2(M+1)4^{-M}$ and $1$. Discarding the second coordinate gives the stated relative residual.

Thus a useful aggregate must discount early transients or localize near the terminal end of the available prefix.

# Five-scale 192-bit audit

For each directional production model, we freeze the archived horizon $M$, construct the clock-rank packet from $X_{\lceil2M/3\rceil}$ in binary64, lift its entries exactly as binary rationals, and evaluate $X_M-X_MVV^*$ in 192-bit Arb arithmetic. Rank at most $r$ is exact even if the lifted columns have a tiny orthogonality defect. The same calculation certifies the Frobenius-norm version of [\[thm:transfer\]](#thm:transfer){reference-type="ref" reference="thm:transfer"}.

::: {#tab:audit}
    $\sigma$   $M$   packet time   rank   worst relative residual
  ---------- ----- ------------- ------ -------------------------
        0.16     4             3      4       $4.09\times10^{-6}$
        0.08     9             6      5       $9.46\times10^{-8}$
        0.04    16            11      6        $2.0\times10^{-7}$
        0.02    25            17      6        $5.0\times10^{-7}$
        0.01    32            22      7        $2.0\times10^{-7}$

  : Worst directional channel at each scale. Values are direct 192-bit upper bounds rounded conservatively.
:::

The numerical values in [1](#tab:audit){reference-type="ref" reference="tab:audit"} are generated automatically and are checked against a $4.5\times10^{-6}$ global gate. The minimum certified captured energy exceeds $0.99999999997$. The packet rank grows from four to seven while the ambient fine dimension grows from $32$ to $512$.

![Interval prefix certificates, comparison with source and unweighted prefix packets, the explicit no-go family, and packet cost versus dimension.](<../../../../../zeta_mvp0/papers/RH-85-midblock-snapshot-packets/figures/midblock_snapshot_packets.pdf>){#fig:audit width="\\textwidth"}

# Boundary and next target

RH-85 supplies a natural finite-scale packet and an exact mechanism for propagating it. It does not yet prove that $\tau_{r_\sigma}(X_{\lfloor M_\sigma/2\rfloor})$ has a uniform polylogarithmic-rank bound, nor that the suffix constants are uniform in $\sigma$. The failed unweighted aggregate points to the next object: a terminally weighted snapshot Gramian or a short block-local packet whose certificate depends only on a controlled late prefix window.

No all-level effective-rank law, unconditional Stage A1 or Stage A4, relative fixed-disk determinant, self-adjoint Hilbert--Polya operator, zeta-zero identification, or Riemann Hypothesis proof is claimed.
