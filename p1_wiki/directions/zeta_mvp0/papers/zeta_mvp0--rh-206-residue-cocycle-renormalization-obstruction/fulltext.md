---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-206-residue-cocycle-renormalization-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-206-residue-cocycle-renormalization-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-206-residue-cocycle-renormalization-obstruction/main.pdf"
source_sha256: "e07489e73e39274f426db95dea2b4c38a53db6b01bfafd4f30f3e9bdc8a88e6d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Gauge-Invariant Residue Cocycles and a Scalar Renormalization Obstruction Physical Weights Along the Two Conjugate Branches

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-206-residue-cocycle-renormalization-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-206-residue-cocycle-renormalization-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-206-residue-cocycle-renormalization-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-206-residue-cocycle-renormalization-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-206-residue-cocycle-renormalization-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The branch correspondence of RH-204 permits a gauge-free comparison of source--observation residues across scales. For matched nonzero residues $r_{c,j},r_{f,j}$, the exact diagonal multiplier is $m_j=r_{f,j}/r_{c,j}$. These multipliers compose under refinement and occur in conjugate pairs for real physical data.

  We test whether the four multipliers can be replaced by one scale-dependent complex scalar. The least-squares optimum is explicit. On the four physical transitions its relative residual ranges from $0.32371$ to $0.99985$; on the first left transition the optimal scalar is nearly zero while the two branch multipliers have moduli $0.10961$ and $0.15002$ with different phases. The exact diagonal cocycle residual is below $1.29\times10^{-16}$, and conjugation symmetry holds within $3.23\times10^{-14}$.

  Thus a common scalar normalization cannot transport the physical transfer weights, even though a branch-diagonal endpoint cocycle always can. The cocycle is source/observation dependent and differs between left and right channels by as much as $1.05364$; it is therefore not yet an intrinsic spectral renormalization. The negative result motivates separating the weighted transfer ledger from the unweighted quartet divisor.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Gauge-Invariant Residue Cocycles and a Scalar Renormalization Obstruction\
  Physical Weights Along the Two Conjugate Branches
```

## Markdown 正文

# Residues after branch matching

For a simple eigenvalue $\lambda$ with right and left vectors $v,w$ chosen so that $w^*v=1$, the spectral projector and physical residue are $$\label{eq:residue}
 P_\lambda=vw^*,\qquad
 r_\lambda=\operatorname{tr}(OP_\lambda S).$$ RH-195 proves that this is also the Frobenius pairing of the source and observation channel states [@WangRH195].

RH-204 supplies the matched labels $j\in\{-,+\}$ for the two upper-half-plane branches and their conjugates [@WangRH204]. No eigenvector phase is used in this labeling.

# Gauge invariance

[\[prop:gauge\]]{#prop:gauge label="prop:gauge"} Under the biorthogonal rescaling $$v\mapsto \alpha v,\qquad
 w\mapsto \overline\alpha^{-1}w,
 \qquad \alpha\ne0,$$ both $P_\lambda$ and $r_\lambda$ are unchanged.

The rescaled outer product is $(\alpha v)(\overline\alpha^{-1}w)^*=vw^*$. Substitute this identity into [\[eq:residue\]](#eq:residue){reference-type="eqref" reference="eq:residue"}.

Consequently, the large residue changes in RH-202 cannot be removed by rephasing or balancing individual eigenvectors.

# Diagonal residue cocycle

For every matched nonzero residue define $$\label{eq:multiplier}
 m_j(c,f)=\frac{r_{f,j}}{r_{c,j}}.$$

[\[thm:cocycle\]]{#thm:cocycle label="thm:cocycle"} For three levels $a,b,c$ on one consistently labeled branch, $$\label{eq:cocycle}
 m_j(a,c)=m_j(b,c)m_j(a,b).$$ If the operators, source, and observation are real, then $$\label{eq:conjugate}
 m_{\overline j}(a,b)=\overline{m_j(a,b)}.$$

Equation [\[eq:cocycle\]](#eq:cocycle){reference-type="eqref" reference="eq:cocycle"} is cancellation of the intermediate nonzero residue. Reality gives $r_{\overline\lambda}=\overline{r_\lambda}$, and taking ratios gives [\[eq:conjugate\]](#eq:conjugate){reference-type="eqref" reference="eq:conjugate"}.

The diagonal cocycle is exact but endpoint dependent. It does not predict a new residue from coarse data alone.

# Best common scalar

Let $r_c,r_f\in\mathbb C^4$ collect the ordered quartet residues. Consider $$\label{eq:ls}
 \min_{\alpha\in\mathbb C}\left\lVert r_f-\alpha r_c\right\rVert_2.$$

[\[prop:scalar\]]{#prop:scalar label="prop:scalar"} If $r_c\ne0$, the unique minimizer is $$\label{eq:alpha}
 \alpha_*=\frac{r_c^*r_f}{r_c^*r_c}.$$ The normalized residual vanishes if and only if $r_f$ is a scalar multiple of $r_c$, equivalently all nonzero branch multipliers agree.

This is a strict, basis-free test of scalar scale renormalization. A large residual means that no global amplitude and phase correction can align all physical weights.

# Physical multiplier table

The upper-half-plane branch multipliers and scalar residuals are:

  step            side                 $m_-$               $m_+$   scalar residual
  --------------- ------- ------------------ ------------------- -----------------
  $0.04\to0.02$   left      $0.1037+0.0356i$   $-0.0269-0.1476i$         $0.99985$
  $0.04\to0.02$   right     $0.1009+0.1534i$    $0.0372-0.1966i$         $0.97654$
  $0.02\to0.01$   left      $1.5204-0.3314i$    $1.3920+0.6344i$         $0.39406$
  $0.02\to0.01$   right     $0.4963-0.0836i$    $0.9778+0.3073i$         $0.32371$

The first transition is nearly orthogonal to a common-scalar description. Even on the finer transition, one scalar leaves a $32$--$39\%$ residual.

The diagonal reconstruction $$r_f=\operatorname{diag}(m_1,\ldots,m_4)r_c$$ has maximum relative residual $1.2846\times10^{-16}$, as required by the exact definition. Conjugate multiplier errors are below $3.23\times10^{-14}$.

# Channel dependence

At $0.04\to0.02$, the largest difference between corresponding left and right branch multipliers is $0.11781$. At $0.02\to0.01$ it is $1.05364$. Therefore the multiplier is not currently universal across the two physical realizations.

Across both transitions, the composed upper-branch multipliers are

  side        $m_-(0.04,0.01)$     $m_+(0.04,0.01)$
  ------- -------------------- --------------------
  left      $0.16942+0.01977i$   $0.05617-0.22251i$
  right     $0.06290+0.06770i$   $0.09681-0.18076i$

The telescoping law is exact, but the two-step numbers reinforce rather than remove branch and channel dependence.

This is expected from [\[eq:residue\]](#eq:residue){reference-type="eqref" reference="eq:residue"}: changing $S$ or $O$ changes the weights without changing the eigenvalue divisor. A transfer determinant may need this cocycle, while an unweighted spectral determinant should not.

# Three distinct notions of renormalization

The audit separates:

1.  *eigenvector gauge*, which leaves residues unchanged;

2.  *common scalar scale normalization*, rejected in the four cases;

3.  *branch-diagonal endpoint cocycle*, exact but source dependent.

Conflating these notions would hide the obstruction by fitting one multiplier per datum.

# Consequence for determinant design

The weighted moments $$\label{eq:weighted}
 h_q=\sum_jr_j\lambda_j^q$$ carry the residue cocycle. The Newton traces $$\label{eq:unweighted}
 s_q=\sum_j\lambda_j^q$$ do not. RH-199 already proves that these two ledgers must not be identified. The present obstruction strengthens the practical reason to study the unweighted quartic divisor separately before attempting a physical feedback factor.

# Claim boundary and next step

The gauge and cocycle statements are exact finite algebra. The rejection of a common scalar is a four-case floating result, not an all-level theorem. No residue lower bound, source-independent cocycle, von Mangoldt weight, or arithmetic trace identity is obtained. RH-207 next studies the unweighted quartic divisor across channels and scales.

# What a useful residue theorem would require

An all-level weighted transfer ledger would need more than nonzero endpoint residues. One needs a uniform lower bound preventing loss of observability, an upper bound on cocycle products, and compatibility with the growing-cloud selection. If multipliers are allowed to be fitted independently at every branch and level, exact reconstruction is tautological and provides no compactness. A useful theorem must derive them from source/observation regularity and operator dynamics.
