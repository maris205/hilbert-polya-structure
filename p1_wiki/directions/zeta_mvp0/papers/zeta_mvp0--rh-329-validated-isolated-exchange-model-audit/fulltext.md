---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-329-validated-isolated-exchange-model-audit"
canonical_tex: "zeta_mvp0/papers/RH-329-validated-isolated-exchange-model-audit/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-329-validated-isolated-exchange-model-audit/main.pdf"
source_sha256: "9c44fbeaf8dc1dab31c2899cef525f62fb219c928ec3fc0ab1f1aadddcf3d68a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Validated Isolated Exchange-Model Audit: Reachable Demand, Fixed-Contrast Failure, and a Scoped No-Go

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-329-validated-isolated-exchange-model-audit>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-329-validated-isolated-exchange-model-audit/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-329-validated-isolated-exchange-model-audit/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-329-validated-isolated-exchange-model-audit/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-329-validated-isolated-exchange-model-audit/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The joint first-alias certificate requires a boundary observation, a fixed reference, a shell scale and contrast, every Duhamel weight, and a far remainder from one coherent data source. We freeze a graded finite-dimensional source defined from exact rational data and audit it without fitting any field after the demand is known. Two-state exchange blocks give $\operatorname{Tr}K_c^m=1+c^m$; diagonal alias blocks and scalar parity blocks realize the other packets exactly. The boundary, observation error, Duhamel defects, and far remainder vanish in this model. Nevertheless its frozen contrast $4/5$ fails the joint equation. We prove $$\frac{\mathcal P_k}{\mathcal A_k}\longrightarrow C_*C_M\in(0,1),\qquad
   \frac{e_k}{\mathcal A_k}\longrightarrow-(1-C_*C_M)<0,
   \qquad \frac{e_k}{kR^{-2k}}\longrightarrow-\infty.$$ The required even power remains eventually reachable, but its contrast radius tends to one. Thus zero best-case reachability does not imply matching for this pre-frozen isolated model. The family is graded rather than one all-order operator, and it is not identified with the actual noisy transfer operator. No full-trace replacement, full-trace divergence, or Riemann-hypothesis conclusion follows.
author:
- Bin Wang
date: July 2026
title: |
  A Validated Isolated Exchange-Model Audit:\
  Reachable Demand, Fixed-Contrast Failure, and a Scoped No-Go
```

## Markdown 正文

# Frozen data and the audit question

All constants in this paper are model definitions, and the audit domain is the set of integers $k\ge2$. Put $$\begin{aligned}
 r_H&=\frac{17}{20},& R&=\frac75,
 &\Lambda&=\frac{2098216888035403}{1250000000000000},
 \label{eq:radii}\\
 C_M&=\frac{9731714526004839}{5000000000000000},
 &C_*&=\frac{26314633984227}{250000000000000},
 &C_b&=\frac{1152012873}{2500000000}.
 \label{eq:constants}\end{aligned}$$ The terminating decimal strings from which these fractions arise are treated as exact rationals. They are not interval enclosures of physical constants. We also freeze $$c_{\rm iso}=\frac45,
 \qquad c_0=\frac35,
 \qquad c_b=\frac12,
 \qquad \eta=0,
 \qquad \sigma_k=\Lambda^{-2k}.
 \label{eq:frozen-contrasts}$$ The clearance metadata are $C_b$ and the inherited orientation $(+,-,+)$. Because the boundary blocks below are identical, these metadata do not enter a fitted correction.

Define $$\beta^2=\frac{1}{r_H^2\Lambda},
 \qquad
 a_k=\frac{2k-2}{C_M}+2,
 \qquad
 \mathcal A_k=a_k\beta^{2k},
 \qquad
 H_k=kR^{-2k}.
 \label{eq:scales}$$ The RH-328 fixed-reference equation asks whether $$e_k=\mathcal B_k+\mathcal S_k+\mathcal R_k+\mathcal P_k-\mathcal A_k=o(H_k)
 \label{eq:joint-ledger}$$ for data obtained before inspecting the demand. Our answer is negative for the model defined below.

For each $k$ we define a finite-dimensional collection of blocks. Their dimensions and some roots depend on $k$. We do not claim that one operator has all these power traces simultaneously. This distinction is part of the theorem statement, not a technical omission.

# Exact block realization

For $0\le c\le1$ let $$K_c=\frac12
 \begin{pmatrix}1+c&1-c\\1-c&1+c\end{pmatrix}.
 \label{eq:exchange}$$ The symmetric and antisymmetric unit vectors are eigenvectors with eigenvalues $1$ and $c$.

The positive contrast range is a deliberate model restriction. We do not claim to identify the sign in the larger even-power class $|c|\le1$.

For every integer $m\ge1$, $$\operatorname{Tr}K_c^m=1+c^m.
 \label{eq:exchange-trace}$$

Diagonalize $K_c$ in its symmetric--antisymmetric basis and take the trace.

Let $\beta_k>0$ be the unique root satisfying $$\beta_k^{2k}=\frac{\beta^{2k}}{C_M}
 \label{eq:beta-k}$$ and define the $2k$-dimensional alias block $$C_k=\operatorname{diag}(\beta_k I_{2k-2},\beta I_2).
 \label{eq:alias-block}$$ For the parity channel put $$\delta_k=C_*\Lambda^{-k},\qquad
 J_k^{\rm ref}=[r_H^{-1}],\qquad
 J_k^{\rm iso}=[r_H^{-1}(1-\delta_k)].
 \label{eq:parity-blocks}$$ Finally set $s_k=\mathcal A_k^{1/(2k)}$ and define $$\begin{aligned}
 D_k^{\rm iso}&=D_k^{\rm ref}=s_kK_{c_b},
 \label{eq:boundary-blocks}\\
 Q_k^{\rm iso}&=s_kK_{c_{\rm iso}},
 &Q_k^{\rm ref}&=s_kK_{c_0}.
 \label{eq:shell-blocks}\end{aligned}$$

The blocks above give $$\begin{aligned}
 \operatorname{Tr}C_k^{2k}
 &=\left(\frac{2k-2}{C_M}+2\right)\beta^{2k}=\mathcal A_k,
 \label{eq:alias-identity}\\
 \mathcal P_k
 &:=\operatorname{Tr}\{(J_k^{\rm ref})^{2k}-(J_k^{\rm iso})^{2k}\}
 =r_H^{-2k}\{1-(1-\delta_k)^{2k}\},
 \label{eq:parity-identity}\\
 \mathcal B_k
 &:=\operatorname{Tr}\{(D_k^{\rm iso})^{2k}-(D_k^{\rm ref})^{2k}\}=0,
 \label{eq:boundary-identity}\\
 \mathcal S_k
 &:=\operatorname{Tr}\{(Q_k^{\rm iso})^{2k}-(Q_k^{\rm ref})^{2k}\}
 =\mathcal A_k(c_{\rm iso}^{2k}-c_0^{2k}).
 \label{eq:shell-identity}\end{aligned}$$ There is no omitted block, so $\mathcal R_k=0$, and the matrix observation is the definition of the shell, so $\mathcal E_k^{\rm obs}=0$.

Equation [\[eq:beta-k\]](#eq:beta-k){reference-type="eqref" reference="eq:beta-k"} and the multiplicities in [\[eq:alias-block\]](#eq:alias-block){reference-type="eqref" reference="eq:alias-block"} give [\[eq:alias-identity\]](#eq:alias-identity){reference-type="eqref" reference="eq:alias-identity"}. The scalar power difference gives [\[eq:parity-identity\]](#eq:parity-identity){reference-type="eqref" reference="eq:parity-identity"}. Identical boundary blocks give [\[eq:boundary-identity\]](#eq:boundary-identity){reference-type="eqref" reference="eq:boundary-identity"}. Apply [\[eq:exchange-trace\]](#eq:exchange-trace){reference-type="eqref" reference="eq:exchange-trace"} to the two scaled shell blocks; the common eigenvalue-one contribution cancels and $s_k^{2k}=\mathcal A_k$, proving [\[eq:shell-identity\]](#eq:shell-identity){reference-type="eqref" reference="eq:shell-identity"}.

Every scale and contrast in this proposition is frozen by [\[eq:radii\]](#eq:radii){reference-type="eqref" reference="eq:radii"}--[\[eq:frozen-contrasts\]](#eq:frozen-contrasts){reference-type="eqref" reference="eq:frozen-contrasts"}. In particular, we do not solve the matching equation for $c_{\rm iso}$ and then insert the result into the model.

# Exact matching equation and asymptotic no-go

In this model the signed demand and required even power are $$\begin{aligned}
 D_k&=\mathcal A_k-\mathcal P_k-\mathcal B_k=\mathcal A_k-\mathcal P_k,
 \label{eq:demand}\\
 y_k&=c_0^{2k}+\frac{D_k}{\mathcal A_k}
 =c_0^{2k}+1-\frac{\mathcal P_k}{\mathcal A_k}.
 \label{eq:required-power}\end{aligned}$$ The best-case RH-328 reachability screen is zero precisely when $y_k\in[0,1]$. The actual fixed-contrast mismatch is different: $$\frac{e_k}{\mathcal A_k}
 =c_{\rm iso}^{2k}-y_k
 =c_{\rm iso}^{2k}-c_0^{2k}
   +\frac{\mathcal P_k}{\mathcal A_k}-1.
 \label{eq:normalized-residual}$$

If $x_k=C_*\Lambda^{-k}$, then $$\frac{1-(1-x_k)^{2k}}{2kx_k}\longrightarrow1.
 \label{eq:binomial-limit}$$

Here $x_k\to0$ and $kx_k\to0$. The inequalities $1-(1-x)^n\le nx$ and $1-(1-x)^n\ge nx-\binom n2x^2$ for $0\le x\le1$ squeeze the ratio between $1-(2k-1)x_k/2$ and $1$ for all sufficiently large $k$.

[\[thm:no-go\]]{#thm:no-go label="thm:no-go"} For the frozen graded family, $$\begin{aligned}
 \frac{\mathcal P_k}{\mathcal A_k}&\longrightarrow\gamma:=C_*C_M,
 &0&<\gamma<1,
 \label{eq:parity-alias-limit}\\
 y_k&\longrightarrow1-\gamma\in(0,1),
 \label{eq:y-limit}\\
 \frac{e_k}{\mathcal A_k}&\longrightarrow-(1-\gamma)<0,
 \label{eq:e-alias-limit}\\
 \frac{\mathcal A_k}{H_k}&\longrightarrow+\infty,
 &\frac{e_k}{H_k}&\longrightarrow-\infty.
 \label{eq:target-divergence}\end{aligned}$$ Thus the reachability screen is eventually exactly zero, while the frozen model fails the target matching condition. If $r_k=y_k^{1/(2k)}$ is the required contrast radius, then $$r_k\longrightarrow1,
 \qquad r_k-c_{\rm iso}\longrightarrow\frac15.
 \label{eq:radius-failure}$$ Moreover, the RH-328 precision scales are exactly $$\frac{H_k}{\mathcal A_k}
 =\frac{k}{a_k}(\beta R)^{-2k},
 \qquad
 \frac{H_k}{k\mathcal A_k}
 =\frac{1}{a_k}(\beta R)^{-2k}.
 \label{eq:precision-scales}$$ The power mismatch in [\[eq:normalized-residual\]](#eq:normalized-residual){reference-type="eqref" reference="eq:normalized-residual"} is not $o(H_k/\mathcal A_k)$, and the radius gap in [\[eq:radius-failure\]](#eq:radius-failure){reference-type="eqref" reference="eq:radius-failure"} is not $o(H_k/(k\mathcal A_k))$.

Because $\beta^{2k}=r_H^{-2k}\Lambda^{-k}$, the preceding lemma yields $$\frac{\mathcal P_k}{\mathcal A_k}
 =\frac{2kC_*}{a_k}\{1+o(1)\}
 \longrightarrow C_*C_M,$$ since $a_k/k\to2/C_M$. Exact integer comparison gives $$\gamma
 =\frac{256086505790802487295251674453}
        {1250000000000000000000000000000}\in(0,1).
 \label{eq:exact-gamma}$$ Both fixed contrasts are strictly subunit, so [\[eq:required-power\]](#eq:required-power){reference-type="eqref" reference="eq:required-power"} and [\[eq:normalized-residual\]](#eq:normalized-residual){reference-type="eqref" reference="eq:normalized-residual"} prove [\[eq:y-limit\]](#eq:y-limit){reference-type="eqref" reference="eq:y-limit"} and [\[eq:e-alias-limit\]](#eq:e-alias-limit){reference-type="eqref" reference="eq:e-alias-limit"}. In particular, $y_k\in(0,1)$ for all sufficiently large $k$.

Next, $$\frac{\mathcal A_k}{H_k}
 =\frac{a_k}{k}(\beta R)^{2k},
 \qquad
 (\beta R)^2
 =\frac{980000000000000000}{606384680642231467}>1.
 \label{eq:growth-certificate}$$ The first factor tends to $2/C_M>0$, proving alias-to-target divergence. Multiplying it by the negative nonzero limit in [\[eq:e-alias-limit\]](#eq:e-alias-limit){reference-type="eqref" reference="eq:e-alias-limit"} proves $e_k/H_k\to-\infty$. Finally $\log y_k$ converges to the finite number $\log(1-\gamma)$, so $\log r_k=(\log y_k)/(2k)\to0$. Hence $r_k\to1$ and [\[eq:radius-failure\]](#eq:radius-failure){reference-type="eqref" reference="eq:radius-failure"} follows. Inverting [\[eq:growth-certificate\]](#eq:growth-certificate){reference-type="eqref" reference="eq:growth-certificate"} gives the first identity in [\[eq:precision-scales\]](#eq:precision-scales){reference-type="eqref" reference="eq:precision-scales"}; division by $k$ gives the second. Both right sides tend to zero exponentially, whereas [\[eq:normalized-residual\]](#eq:normalized-residual){reference-type="eqref" reference="eq:normalized-residual"} has the nonzero limit $-(1-\gamma)$ and the radius gap tends to $1/5$. This proves both precision failures.

This theorem is stronger than a finite failed fit: its sign and target-scale failure hold eventually by exact asymptotics. It is weaker than an actual noisy-trace theorem because every block belongs only to the isolated model.

# Duhamel and omitted-remainder audit

The product comparison is deliberately recorded leg by leg even though the model representation is exact. In each shell channel $c\in\{c_{\rm iso},c_0\}$, compare the $2k$ factors $$A_{j,k}^{(c)}=G_{j,k}^{(c)}=Q_{c,k},
 \qquad 1\le j\le2k.
 \label{eq:identical-legs}$$ For the spectral matrix norm, $\lVert K_c\rVert=1$ and hence $\lVert Q_{c,k}\rVert=s_k$. The trace observation on two-dimensional matrices obeys $|\operatorname{Tr}X|\le2\lVert X\rVert$. Therefore every telescoping weight is $$W_{j,k}^{(c)}=2s_k^{2k-1}
 =2\mathcal A_k^{(2k-1)/(2k)},
 \label{eq:duhamel-weight}$$ while every leg defect is $\delta_{j,k}^{(c)}=\lVert A_{j,k}^{(c)}-G_{j,k}^{(c)}\rVert=0$.

Across the noisy and reference shell channels there are exactly $4k$ prefix/suffix weights. None is discarded, and $$\mathcal U_k
 =\sum_{c\in\{c_{\rm iso},c_0\}}
   \sum_{j=1}^{2k}W_{j,k}^{(c)}\delta_{j,k}^{(c)}=0.
 \label{eq:zero-majorant}$$ Together with $\mathcal E_k^{\rm obs}=\mathcal R_k=0$, the best- and worst-case uncertainty residuals both equal $|e_k|$.

The zero in [\[eq:zero-majorant\]](#eq:zero-majorant){reference-type="eqref" reference="eq:zero-majorant"} certifies internal implementation of the isolated block identity. It does not bound the defect between an actual noisy critical leg and this model. Likewise $\mathcal R_k=0$ says that the model has no omitted block; it is not an estimate for the physical far region.

# Deterministic experiment protocol

The executable ledger uses Python rational arithmetic for all constants, packets, signs, reachability decisions, and target-window verdicts. Decimal endpoints are rounded outward only for display. Matrix multiplication and powers independently check [\[eq:exchange-trace\]](#eq:exchange-trace){reference-type="eqref" reference="eq:exchange-trace"}. The selected orders are $k=2,4,8,16,24,32$; across them the ledger retains 344 Duhamel weights. The following subset is printed compactly.

    $k$   $\mathcal P_k/\mathcal A_k$      $y_k$   $e_k/\mathcal A_k$           $|e_k|/H_k$
  ----- ----------------------------- ---------- -------------------- ---------------------
      2                      0.131466   0.998134          $-0.588534$               2.32697
      4                      0.158186   0.858610          $-0.690838$               5.98856
      8                      0.180921   0.819361          $-0.791213$               42.3139
     16                      0.193349   0.806651          $-0.805859$               1899.64
     32                      0.198985   0.801015          $-0.801015$   $3.97557\times10^6$

Every displayed row has $y_k\in[0,1]$ and $|e_k|>H_k$, with both decisions made before decimal conversion. These rows reproduce formulas; they are not used to infer any limit in [\[thm:no-go\]](#thm:no-go){reference-type="ref" reference="thm:no-go"}.

# Boundary and RH-330 handoff

The validated conclusion is precisely this: the pre-frozen graded isolated exchange family fails the RH-328 joint matching equation, even though its best-case contrast reachability screen eventually passes. The conclusion does not identify the family with the actual noisy operator, establish a physical shell scale or contrast, control actual moving-order Duhamel defects, prove an actual far-remainder little-$o$ estimate, replace the full trace, or prove actual full-trace divergence.

RH-330 must state a transfer criterion retaining boundary, shell, parity, alias, observation, and far-remainder terms on one clock. It must quantify the replacement of every isolated field and preserve signed cancellation at scale $o(H_k)$. Passing or failing a different isolated model cannot bypass that transfer step.

All five program gates remain false/open: no canonical intrinsic dynamical spectral determinant, oriented unitary completion, self-adjoint generator with an intrinsic $T\log T$ law, von Mangoldt prime-power trace, or equality with the completed-zeta divisor is proved. In particular, no Hilbert--Polya operator is constructed, no Riemann zero is identified, and the Riemann Hypothesis is not proved.
