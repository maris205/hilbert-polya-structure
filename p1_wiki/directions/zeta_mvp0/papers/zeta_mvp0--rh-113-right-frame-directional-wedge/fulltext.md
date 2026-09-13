---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-113-right-frame-directional-wedge"
canonical_tex: "zeta_mvp0/papers/RH-113-right-frame-directional-wedge/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-113-right-frame-directional-wedge/main.pdf"
source_sha256: "802b9980aa93e587d25b9928abc61eaaaf4e9ee4b1f5961cf4dc2e512715a678"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Right-Frame Directional Wedge Certificates Four Actions Recover the Fourth Exterior Support

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-113-right-frame-directional-wedge>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-113-right-frame-directional-wedge/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-113-right-frame-directional-wedge/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-113-right-frame-directional-wedge/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-113-right-frame-directional-wedge/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Global norm-only perturbation of the fourth exterior power is sharp but inefficient. We retain an orthonormal right four-frame $Q$ and use the restricted action $KQ$. Its column volume $\det((KQ)^*KQ)^{1/2}$ is always bounded by $\left\lVert\bigwedge^4K\right\rVert_2$, and the supremum over $Q$ equals that exterior norm. If $\widehat Y$ approximates $KQ$ within $\epsilon$, the product $\prod_{j=1}^4(\sigma_j(\widehat Y)-\epsilon)_+$ gives a rigorous lower certificate. For the recent top right frame and the global tail radius this is exactly product Weyl, but a frame-resolved residual can be smaller. In a 360-record five-scale audit, the recent frame captures at least $0.99999531005$ of the full spectral four-volume and is exact on the fine chain to $3.9\times10^{-15}$; the directional residual radius gains a factor up to $2.40578$. The result reduces the next theoretical target to a four-dimensional tail Gramian.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Right-Frame Directional Wedge Certificates\
  Four Actions Recover the Fourth Exterior Support
```

## Markdown 正文

# Directional replacement for a global exterior map

Let $K:\mathcal H\to\mathcal G$ have at least four columns. RH-112 showed that perturbing $\bigwedge^4K$ using only $\left\lVert K\right\rVert$ is universally dominated by individual singular-value Weyl bounds. The discarded information is the right frame on which the large four-volume is attained.

Take an isometry $Q:\mathbb C^4\to\mathcal H$ and define $$D_4(K;Q)=\det(Q^*K^*KQ)^{1/2}.$$ This number requires four actions of $K$, followed by a $4\times4$ Gram determinant. It does not require a full singular decomposition of $K$.

# Frame variational theorem

[\[thm:frame\]]{#thm:frame label="thm:frame"} For every orthonormal right four-frame $Q$, $$D_4(K;Q)\leq\left\lVert\bigwedge^4K\right\rVert_2
 =s_1(K)s_2(K)s_3(K)s_4(K).$$ Moreover, equality is attained when $Q$ spans four leading right singular vectors. Hence the supremum over all such frames equals the spectral fourth exterior norm.

The vector $q_1\wedge\cdots\wedge q_4$ has unit norm and its image under $\bigwedge^4K$ has norm $D_4(K;Q)$. This is at most the operator norm. A leading right singular frame maps to mutually orthogonal vectors of lengths $s_1,\ldots,s_4$, proving equality [@HornJohnson1991].

The theorem makes any fixed frame a one-sided certificate. A stale frame can lose volume but can never create a false positive.

# Approximate action certificate

Suppose only a four-column approximation $\widehat Y$ to $KQ$ is available.

[\[thm:approx\]]{#thm:approx label="thm:approx"} If $\left\lVert KQ-\widehat Y\right\rVert\leq\epsilon$ and $U\geq\left\lVert K\right\rVert$, then $$\label{eq:cert}
 \frac{\left\lVert\bigwedge^4K\right\rVert_2}{\left\lVert K\right\rVert^4}
 \geq \frac{\prod_{j=1}^4
 (\sigma_j(\widehat Y)-\epsilon)_+}{U^4}.$$

Theorem [\[thm:frame\]](#thm:frame){reference-type="ref" reference="thm:frame"} lower-bounds the exterior norm by the column volume of $KQ$. Weyl's inequality gives $\sigma_j(KQ)\geq(\sigma_j(\widehat Y)-\epsilon)_+$, and $\left\lVert K\right\rVert^4\leq U^4$.

Let $A$ be a recent operator, $\left\lVert K-A\right\rVert\leq\delta$, and let $Q_A$ be its top right four-frame. Then the singular values of $AQ_A$ are $s_1(A),\ldots,s_4(A)$. Choosing $\widehat Y=AQ_A$, $\epsilon=\delta$, and $U=s_1(A)+\delta$ turns [\[eq:cert\]](#eq:cert){reference-type="eqref" reference="eq:cert"} into $$\frac{\prod_{j=1}^4(s_j(A)-\delta)_+}{(s_1(A)+\delta)^4}.$$ Thus the standard product-Weyl exterior certificate is already a right-frame directional certificate. If a separate bound $\left\lVert(K-A)Q_A\right\rVert\leq\epsilon_Q<\delta$ is available, the same formula uses $\epsilon_Q$ in the numerator while retaining the safe denominator.

# Sharpness and the frame-selection barrier

Both one-sided steps above are sharp. If $\widehat Y=\operatorname{diag}(a_1,a_2,a_3,a_4)$ with $a_4\geq\epsilon$ and $KQ=\widehat Y-\epsilon I$, then every singular-value lower endpoint in Theorem [\[thm:approx\]](#thm:approx){reference-type="ref" reference="thm:approx"} is attained simultaneously. If $Q$ is a leading right frame of $K$, Theorem [\[thm:frame\]](#thm:frame){reference-type="ref" reference="thm:frame"} is also an equality. Therefore no uniformly larger certificate can be inferred from only the four singular values of $\widehat Y$, the scalar action radius, and the leading upper bound.

There is also no nontrivial lower bound for an arbitrary fixed frame. On an eight-dimensional domain, take $K=[I_4\;0]$. Its spectral four-volume is one, but the frame supported on the last four coordinates has directional volume zero. Recent-frame tracking is thus not cosmetic: it is the datum that avoids this exact blindness example.

The two observations delimit the gain available in RH-113. Accuracy can improve only through a better frame or a smaller directional residual, and not through a sharper manipulation of the same three scalar inputs. They also suggest a stable implementation: update $Q_A$ only when the packet is refreshed, evaluate four matrix-free actions, and form a $4\times4$ Gramian. The expensive ambient singular decomposition is needed only for audit, not for applying the directional theorem.

# Five-scale audit

We recompute the RH-110 packet chain at five scales, two channels, and three thresholds. At each update we form the recent right frame, its exact full directional action, and the omitted directional residual. Outward guards are retained in the finite binary64 audit.

Across 360 records there are no failures of the frame variational inequality, the leading upper bound, or the identity with product Weyl. The minimum capture ratio over the full chain is $0.99999531005$; on the 234 fine records the maximum capture loss is $3.9\times10^{-15}$. The fine packets have four right columns, so this exactness is structural rather than an unexplained numerical coincidence. On wider coarse packets, the recent frame still loses less than $4.7\times10^{-6}$.

  threshold     global-frame   frame-tail   exact frame   spectral
  ----------- -------------- ------------ ------------- ----------
  $10^{-8}$               78           78            78         78
  $10^{-6}$               72           72            72         72
  $10^{-4}$               55           55            55         55

  : Fine certified updates out of 78. The frame-tail refinement is quantitatively stronger on some records but does not cross a new threshold.

![Left: loss of the recent frame relative to the optimal full exterior frame. Right: ratio of the global tail radius to the measured four-frame residual radius; values above one favor directional control.](<../../../../../zeta_mvp0/papers/RH-113-right-frame-directional-wedge/figures/right_frame_directional_wedge.pdf>){width="\\textwidth"}

The largest directional radius gain is $2.40578$. A small number of roundoff-dominated records have a guarded ratio just below one; taking the maximum of the global and directional certificates preserves monotonicity.

# What has and has not been reduced

RH-113 replaces a global exterior operator by four actions and a determinant. It proves that no spectral support is lost by this replacement when the frame is optimal, and the audit shows the recent physical frame is essentially optimal. The unresolved input is now directional: control $(K-A)Q_A$ or its $4\times4$ Gramian.

RH-114 will study a PSD-Rayleigh relative tail condition. This paper does not prove that condition at all scales, an all-level physical exterior lower law, uniform Stage A, a Hilbert--Polya operator, identification of zeta zeros, or the Riemann Hypothesis.
