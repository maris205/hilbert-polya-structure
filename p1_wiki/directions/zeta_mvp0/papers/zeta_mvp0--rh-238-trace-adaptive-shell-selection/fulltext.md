---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-238-trace-adaptive-shell-selection"
canonical_tex: "zeta_mvp0/papers/RH-238-trace-adaptive-shell-selection/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-238-trace-adaptive-shell-selection/main.pdf"
source_sha256: "8663b604bd42f7e111ee5d93d9116692c7551bb7501f156da06544aaba2e9350"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Trace-Adaptive Shell-Complete Cloud Selection

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-238-trace-adaptive-shell-selection>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-238-trace-adaptive-shell-selection/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-238-trace-adaptive-shell-selection/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-238-trace-adaptive-shell-selection/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-238-trace-adaptive-shell-selection/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The RH-222 cloud ranks were prescribed by a simple geometric schedule. We replace that external schedule by a finite determinant-intrinsic rule. List the conjugacy-closed candidate shells by decreasing modulus. Among prefixes of rank at least four, choose the first for which the cloud-extracted order-$12$ logarithmic jet obeys $$J_{12}(\tau)=\sum_{n=2}^{12}\frac{|\tau_n|}{n}
   \le\varepsilon_\sigma,
   \qquad \varepsilon_\sigma=\sigma.$$

  Every one of the 32 archived endpoints has an admissible prefix. The adaptive ranks range from $5$ to $38$, the smallest tolerance slack is $4.73\times10^{-5}$, and the largest left/right rank mismatch is nine. The candidate windows contain between one and ten admissible prefixes, so taking the first is a genuine normalization choice.

  The selector is canonical for a fixed order, disk, tolerance rule, and candidate atlas. It does not prove asymptotic candidate availability, all-order determinant control, or preservation of the intended deterministic numerator.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'Trace-Adaptive Shell-Complete Cloud Selection'
```

## Markdown 正文

# From rank schedule to trace tolerance

The selected cloud should remove the moving singular part while leaving a controlled complement. A fixed target rank does not directly express that goal. RH-236 supplies a finite complement jet, and RH-237 shows that it is stable across the two discretization channels [@WangRH236; @WangRH237]. This suggests choosing rank by the jet itself.

Let $S_1,S_2,\ldots$ be real shells or conjugate-pair shells, sorted by decreasing modulus. Set $C_k=S_1\cup\cdots\cup S_k$ and compute the residual moments $\tau_n(C_k)$ by subtracting the peripheral and cloud powers from the full sparse traces.

# Minimal admissible prefix

[\[thm:selector\]]{#thm:selector label="thm:selector"} Fix a maximum order $m\ge2$, radius $R\ge0$, minimum rank $r_0$, and tolerance $\varepsilon\ge0$. If at least one shell prefix $C_k$ of rank at least $r_0$ satisfies $$J_{m,R}(C_k):=\sum_{n=2}^m\frac{|\tau_n(C_k)|}{n}R^n\le\varepsilon,$$ then there is a unique first admissible prefix. The selection is invariant under permutations inside each shell and preserves conjugacy closure.

The prefixes are totally ordered by shell index, so every nonempty admissible set has a unique least index. Permuting entries inside a shell leaves every power sum unchanged. Each prefix is a union of complete shells and is therefore conjugacy closed.

The theorem does not assert monotonicity of $J_{m,R}(C_k)$ in $k$. Adding a conjugate shell can increase or decrease the modulus of a complex power sum. This is why the first admissible prefix, rather than the smallest jet norm, is used.

[\[prop:parameters\]]{#prop:parameters label="prop:parameters"} Write $k(\varepsilon,r_0)$ for the first admissible shell index whenever it exists. If $\varepsilon'\ge\varepsilon$, then $$k(\varepsilon',r_0)\le k(\varepsilon,r_0).$$ If $r_0'\ge r_0$, then $$k(\varepsilon,r_0')\ge k(\varepsilon,r_0)$$ whenever both selectors exist.

Increasing the tolerance enlarges the admissible set, so its least element cannot move to the right. Increasing the minimum rank removes an initial segment of eligible prefixes, so the least remaining admissible element cannot move to the left.

This monotonicity concerns the external parameters, not the oscillatory jet norm along the shell list. It gives a useful consistency test when changing the target disk or tolerance but does not supply an asymptotic rank law.

# Selector algorithm and finite cost

Once the full traces have been computed, the adaptive scan requires no new matrix powers. For each order $2\le n\le m$, maintain the cumulative shell power sum $$U_{k,n}=\sum_{\lambda\in C_k}\lambda^n.$$ After adding shell $S_k$, update $U_{k,n}$, form $$\tau_n(C_k)=\operatorname{tr}(A^n)-p^n-q^n-U_{k,n},$$ and evaluate $J_{m,R}(C_k)$. Stop at the first eligible prefix below the tolerance. For $s$ shells this postprocessing costs $O(ms)$ arithmetic and $O(m)$ working storage beyond the archived roots and traces.

The 543 evaluated prefixes correspond to an average of about 17 scans per endpoint. This modest finite cost is important because it separates the selection question from the expensive sparse-power computation of RH-236.

# Archived selection

We take $m=12$, $R=1$, $r_0=4$, and $\varepsilon_\sigma=\sigma$. The candidate windows are exactly those of RH-222; no new eigenvalue solve is introduced.

  Statistic                                          value
  --------------------------------- ----------------------
  Endpoint count                                        32
  Successful selections                                 32
  Adaptive rank range                            $5$--$38$
  Maximum selected jet norm                     $0.024953$
  Minimum tolerance slack             $4.728\times10^{-5}$
  Maximum channel rank difference                        9
  Admissible-prefix count range                  $1$--$10$
  Evaluated shell prefixes                             543

  : The frozen trace-adaptive selector.

The rank need not agree with the RH-222 target rank and need not be monotone between adjacent scales. It answers a different question: how many outer shells are needed to force the first eleven nontrivial logarithmic coefficients below the current noise scale?

# Finite robustness and parameter dependence

The selector is canonical only relative to the tuple $(m,R,r_0,\varepsilon_\sigma)$ and the candidate shell atlas. Changing the maximum order can expose a coefficient spike; increasing $R$ weights later orders more strongly; changing the tolerance modifies the stopping index according to Proposition [\[prop:parameters\]](#prop:parameters){reference-type="ref" reference="prop:parameters"}. These are normalization choices, not implementation details.

The minimum selected tolerance slack is $4.73\times10^{-5}$. This proves that every archived selected prefix lies strictly inside its floating gate. It does not by itself certify the selected index: an earlier rejected prefix could lie arbitrarily close to the same boundary. A validated selector would need outward error bounds both for the accepted prefix and for every earlier eligible rejection.

The left/right rank mismatch of as much as nine is compatible with the small jet discrepancy of RH-237. Different shell combinations can approximate the same first eleven logarithmic coefficients, an identifiability issue that is invisible to the scalar tolerance alone.

# No-over-extraction issue

A small residual jet is not automatically the desired residual jet. If too many regular eigenvalues are absorbed into the cloud, the quotient can be driven artificially toward one and lose the deterministic numerator sought in RH-80 [@WangRH80]. The present selector limits that ambiguity by taking the first admissible prefix, but it does not prove that this prefix separates singular cloud modes from regular background modes.

More generally, if the intended deterministic numerator has logarithmic coefficients $a_2,\ldots,a_m$, then the intrinsically anchored finite target would be $$\sum_{n=2}^m\frac{|\tau_n(C_k)-a_n|}{n}R^n
 \le\varepsilon_\sigma,$$ not necessarily a target of zero. The present experiment uses zero because the coefficients $a_n$ have not yet been derived independently. Therefore its success proves finite compressibility of the trace germ, not correctness of the limiting normalization.

Two additional theorems are therefore needed:

1.  availability: admissible prefixes exist for all sufficiently small noise under a fixed rule;

2.  anchoring: the selected cloud coefficients converge to the intended singular factor, leaving the deterministic numerator unchanged.

RH-239 proves the finite-jet contraction implied by vanishing tolerances and then isolates the all-order obstruction. No determinant or arithmetic gate is closed here.
