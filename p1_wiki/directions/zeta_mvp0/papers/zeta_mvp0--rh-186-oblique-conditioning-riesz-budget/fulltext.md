---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-186-oblique-conditioning-riesz-budget"
canonical_tex: "zeta_mvp0/papers/RH-186-oblique-conditioning-riesz-budget/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-186-oblique-conditioning-riesz-budget/main.pdf"
source_sha256: "c844e03045e59a37e454ea7e603bf5fc9ca99556ef5885609d2999729c4cdf9c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Oblique Conditioning in the Temporal Riesz Budget Why Small Bi-Krylov Residuals Are Not Yet a Shell Certificate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-186-oblique-conditioning-riesz-budget>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-186-oblique-conditioning-riesz-budget/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-186-oblique-conditioning-riesz-budget/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-186-oblique-conditioning-riesz-budget/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-186-oblique-conditioning-riesz-budget/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-185 produces twelve finite windows with both directed bi-Krylov residuals below $0.10$. It would be unsafe to pass these raw numbers directly into a Riesz or Schur theorem because the right and left temporal frames are highly oblique. This paper isolates the exact conditioning factor.

  For balanced frames $V,W$ with $W^*V=I$ and cross-Gram minimum singular value $\gamma$, the oblique projector $P=VW^*$ satisfies $\left\lVert P\right\rVert=\left\lVert I-P\right\rVert=\gamma^{-1}$. A perturbation of size $\delta$ in a directed packet equation is transported through the oblique coordinates with the factor $\chi=\gamma^{-1}$. The natural Neumann/Banach sufficient gate for this coordinate transport is $\chi\epsilon<1$, where $\epsilon$ is the larger directed relative residual. A separate projector perturbation bound has the pole $1-\chi\delta$.

  Replaying all 126 RH-185 windows gives cross-angle condition numbers between $48.2$ and $4.33\times10^5$. Although 12 windows pass the raw $0.10$ gate, the minimum amplified residual is $10.253$, so none passes the conditioning- aware contraction gate. This is a precise negative result for a coarse oblique norm budget, not a no-go theorem for sharp directional Schur bounds or exact complement resolvents.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Oblique Conditioning in the Temporal Riesz Budget\
  Why Small Bi-Krylov Residuals Are Not Yet a Shell Certificate
```

## Markdown 正文

# The conditioning issue

The balanced biorthogonal construction of RH-184 and its physical calibration in RH-185 replace one orthogonal packet by right and left frames $V,W$ with $W^*V=I$ [@WangRH184; @WangRH185]. The compressed matrix $K=W^*AV$ is well typed, and the directed residuals are $$\label{eq:residuals}
 R_R=AV-VK,
 \qquad R_L=A^*W-WK^*.$$ The relative residuals can be small while the coordinate map from the oblique decomposition to the ambient Hilbert space is badly conditioned. A Riesz shell theorem sees both pieces of information.

Let $Q_R,Q_L$ be orthonormal bases of the two temporal subspaces and put $H=Q_L^*Q_R$. Write $$\label{eq:gamma}
 \gamma=\sigma_{\min}(H),
 \qquad \chi=\gamma^{-1}.$$

# Oblique projector norm

[\[thm:oblique-norm\]]{#thm:oblique-norm label="thm:oblique-norm"} For the balanced frames of RH-184, $$\label{eq:p-norm}
 P=VW^*,\qquad P^2=P,qquad
 \left\lVert P\right\rVert=\left\lVert I-P\right\rVert=\chi.$$ The equality for $I-P$ is understood on a nontrivial complementary decomposition; in the degenerate full-space case the complement is absent.

The SVD formula from RH-184 gives $P=Q_RV_H\Sigma^{-1}U_H^*Q_L^*$. Hence $\left\lVert P\right\rVert=\left\lVert\Sigma^{-1}\right\rVert=\gamma^{-1}$. For an oblique projection with both range and kernel nonzero, $P$ and $I-P$ have the same nonzero principal angle singular value and therefore the same norm. This also follows by writing the two operators in the two-dimensional principal-angle blocks.

The value $\chi$ is an intrinsic property of the pair of subspaces, not a bad choice of frame. RH-184 proves that no other biorthogonal frame pair on the same subspaces lowers the product of right and left norms [@WangRH184].

The factor is sharp in the smallest possible model. Take $\mathcal R=\operatorname{span}(e_1)$ and $\mathcal L=\operatorname{span}(\cos\theta\,e_1+\sin\theta\,e_2)$ with $0<\theta<\pi/2$. Then $\gamma=\cos\theta$ and the projection onto $\mathcal R$ along $\mathcal L^\perp$ is $$\label{eq:two-dimensional-projector}
 P_\theta=
 \begin{pmatrix}1&\tan\theta\\0&0\end{pmatrix},
 \qquad \left\lVert P_\theta\right\rVert=\sec\theta=\gamma^{-1}.$$ A perturbation vector in the maximizing singular direction attains the full factor $\chi$. Therefore no universal maximum-norm transport theorem can replace $\chi$ by a smaller constant without using additional directional structure.

# A coordinate-transport gate

Suppose a nominal packet equation has a normalized error $E$ with $\left\lVert E\right\rVert\le\epsilon$. Applying the oblique coordinate projection produces $$\label{eq:transport}
 \left\lVert PE\right\rVert\le\chi\epsilon.$$ Consequently a Neumann correction $(I-PE)^{-1}$ is guaranteed by $$\label{eq:conditioned-gate}
 \chi\epsilon<1.$$ This is only a sufficient norm gate. It is nevertheless the correct first audit before invoking more refined resolvent information.

[\[prop:projector-perturb\]]{#prop:projector-perturb label="prop:projector-perturb"} Let $P$ be an oblique projection with $\left\lVert P\right\rVert\le\chi$ and let a directed subspace perturbation have norm at most $\delta$. Whenever $\chi\delta<1$, the elementary fixed-point correction obeys $$\label{eq:projector-bound}
 \left\lVert\Delta P\right\rVert
 \le \frac{\chi^2\delta}{1-\chi\delta}.$$ If $\chi\delta\ge1$, this norm-only argument supplies no finite bound.

The perturbed coordinate equation has the form $X=X_0+P\Delta X+F$, with $\left\lVert F\right\rVert\le\chi\delta\left\lVert X_0\right\rVert$ and $\left\lVert P\right\rVert\le\chi$. The Neumann series for $(I-P\Delta)^{-1}$ converges when $\chi\delta<1$. Summing the geometric series and applying the outer projection factor gives [\[eq:projector-bound\]](#eq:projector-bound){reference-type="eqref" reference="eq:projector-bound"}.

The bound is deliberately coarse. It makes the next logical dependency visible: a small raw residual is not a small oblique residual unless the cross angle is also controlled.

# Physical replay

The RH-185 archive has 126 windows, of which 12 are below $0.10$ in both directed relative residuals. The conditioning-aware quantity is $$\label{eq:amplified}
 \epsilon_{\rm amp}
 =\frac{\max(\epsilon_R,\epsilon_L)}{\gamma}.$$ Its summary is:

  quantity                                      value
  ------------------------------ --------------------
  minimum $\chi$                            $48.2196$
  median $\chi$                             $768.746$
  maximum $\chi$                   $4.3273\times10^5$
  minimum $\epsilon_{\rm amp}$              $10.2530$
  median $\epsilon_{\rm amp}$               $902.203$
  maximum $\epsilon_{\rm amp}$     $1.5855\times10^8$
  raw two-sided gate count                         12
  conditioned gate count                            0

The smallest principal angle cosine is attained in the nearly orthogonal late temporal subspaces. The local $L=4$ candidate therefore does not yet provide a stable ambient coordinate system for an outward Riesz calculation.

The corresponding principal angles range from $88.812^\circ$ to $89.99987^\circ$, with median $89.9255^\circ$. These angles give a more geometric reading of the large condition numbers: the right and left packet spaces intersect transversely, but only through very narrow angles. Exact biorthogonality is therefore compatible with severe sensitivity.

# Necessary scale of improvement for the coarse route

The sufficient gate [\[eq:conditioned-gate\]](#eq:conditioned-gate){reference-type="eqref" reference="eq:conditioned-gate"} can be rewritten as $$\label{eq:residual-angle-condition}
 \max(\epsilon_R,\epsilon_L)<\gamma.$$ Hence a raw residual threshold such as $0.10$ has no intrinsic meaning until it is compared with the cross angle. In the present archive the best ratio between the two sides of [\[eq:residual-angle-condition\]](#eq:residual-angle-condition){reference-type="eqref" reference="eq:residual-angle-condition"} is $10.253$. Even the most favorable window would therefore need an order-of-magnitude reduction of the larger relative residual, an order-of-magnitude increase of $\gamma$, or a proof that avoids this maximum-norm comparison.

There are three mathematically different ways forward:

1.  change the physical subspaces so that their smallest cross singular value increases;

2.  regularize the dual pair and explicitly pay a biorthogonality defect;

3.  retain the present pair but estimate the two directed couplings and complement resolvent in a product rather than through one maximum.

The first changes the model, the second changes the coordinate identity, and the third keeps the model but seeks a sharper theorem. RH-187--188 examine the latter two in that order.

# Status of the perturbation estimate

Proposition [\[prop:projector-perturb\]](#prop:projector-perturb){reference-type="ref" reference="prop:projector-perturb"} is an architecture-level sufficient bound. It is sharp only at the level of submultiplicative norms and does not claim that the physical perturbation aligns with the worst singular direction in [\[eq:two-dimensional-projector\]](#eq:two-dimensional-projector){reference-type="eqref" reference="eq:two-dimensional-projector"}. Its failure therefore means that a black-box Banach correction is unavailable. It does not mean that every structured perturbation changes the packet by the displayed amount.

For a publishable positive shell certificate, the perturbation object must be specified explicitly: operator ball, frame ball, contour displacement, and inverse defect. Each factor can then be transported in its own direction. The present negative audit is useful precisely because it shows that replacing this structured ledger by one residual maximum is too expensive on all 126 windows.

# Why this is not a complete negative result

The gate [\[eq:conditioned-gate\]](#eq:conditioned-gate){reference-type="eqref" reference="eq:conditioned-gate"} multiplies the larger relative residual by the full oblique condition number. RH-163 and RH-188 instead emphasize a directed Schur product of separate left and right couplings. It is possible for that product to be small while the maximum-residual norm gate fails. Moreover, a contour resolvent can be much sharper than the norm bound $\left\lVert(z-D)^{-1}\right\rVert\le(|z|-\left\lVert D\right\rVert)^{-1}$.

The correct conclusion is therefore: $$\label{eq:conclusion}
 \text{raw bi-Krylov residuals pass locally}
 \quad\not\Rightarrow\quad
 \text{coarse oblique Riesz budget passes}.$$ The directional product and the exact complement resolvent remain to be tested separately.

# Relation to the physical leaves

RH-171's physical interface required ambient realization $X$, finite data $D$, uniform margins $K$, and shell transport $H$. RH-185 gives a local floating $X$ candidate. This paper shows that $D$ cannot be populated by raw relative residuals alone. A validated interval or resolvent estimate must carry the oblique factor, or else exploit cancellation absent from the norm-only argument.

No uniform lower bound on $\gamma$ is observed in the five-anchor corpus. The data do not prove that $\gamma$ tends to zero asymptotically; they only show that the current finite windows are badly conditioned.

# Boundary

The paper proves exact finite oblique conditioning and a transparent coordinate-transport budget. The physical audit rejects the coarse conditioned gate on all 126 windows. It does not reject sharp directional Schur certificates, contour-specific complement resolvents, regularized dual frames, or later scale embeddings. It does not close R, Gate A, or any downstream Hilbert--Polya/RH claim.
