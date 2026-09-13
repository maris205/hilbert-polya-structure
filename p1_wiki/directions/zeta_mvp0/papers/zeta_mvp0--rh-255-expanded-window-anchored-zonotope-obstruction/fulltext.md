---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-255-expanded-window-anchored-zonotope-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-255-expanded-window-anchored-zonotope-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-255-expanded-window-anchored-zonotope-obstruction/main.pdf"
source_sha256: "b6084a76d0888405cb9582833c68b5c77c4e03d2fc0e06f8222537f71251c659"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Expanded-Window Anchored Zonotope Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-255-expanded-window-anchored-zonotope-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-255-expanded-window-anchored-zonotope-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-255-expanded-window-anchored-zonotope-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-255-expanded-window-anchored-zonotope-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-255-expanded-window-anchored-zonotope-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-254 doubles the resolved candidate margin and supplies 16 new roots at each archived endpoint. We now perform the required anchored reachability audit rather than a zero-target fit. After discarding incomplete boundary pairs, every conjugate shell receives a single-use weight $0\le w_j\le1$. The resulting convex zonotope has zero passes at all 32 endpoints. Its weighted distance from the deterministic target ranges from $0.143585$ to $0.423998$, with primal--dual gaps below $5.83\times10^{-15}$. Hence every prefix and each of the 62,030,604,700 eligible binary subsets also fails. This is a finite margin-32 obstruction, not a global nonexistence theorem.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Expanded-Window Anchored Zonotope Obstruction'
```

## Markdown 正文

# Anchored expanded class

For orders $n=2,\dots,12$, let $a=(a_n)$ be the deterministic target of RH-243 [@WangRH243]. At a fixed noise/channel endpoint, remove the Perron and parity traces from the full matrix powers and write the remaining base vector as $b$. If $S_j$ is a conjugate-complete shell from RH-254, put $$v_j=\left(\sum_{\mu\in S_j}\mu^n\right)_{n=2}^{12}.
 \label{eq:shell}$$ All $v_j$ are real up to the archived conjugacy tolerance.

The expanded single-use class is the zonotope $$\mathcal Z=\left\{b-\sum_jw_jv_j:0\le w_j\le1\right\}.
 \label{eq:box}$$ Its anchored distance is measured by $$d(\mathcal Z,a)=\min_{0\le w\le1}
 \sum_{n=2}^{12}\frac{|b_n-a_n-(Vw)_n|}{n}.
 \label{eq:distance}$$

[\[prop:dominance\]]{#prop:dominance label="prop:dominance"} Every shell prefix, contiguous shell interval, and binary single-use subset is contained in the box class [\[eq:box\]](#eq:box){reference-type="eqref" reference="eq:box"}. Therefore $d(\mathcal Z,a)>\varepsilon$ excludes all such selectors at tolerance $\varepsilon$.

Each listed discrete selector has a weight vector with coordinates in $\{0,1\}$, hence lies in $[0,1]^J$. Minimizing over the larger box can only decrease the distance.

# Primal--dual audit

The weighted $\ell^1$ problem [\[eq:distance\]](#eq:distance){reference-type="eqref" reference="eq:distance"} is a linear program. We solve both its box primal and explicit zonotope dual, then compare their objectives. The shell-complete ranks range from 33 to 64; no incomplete conjugate fragment enters the optimization [@WangRH254].

  quantity                                    value
  -------------------------- ----------------------
  endpoints                                      32
  eligible prefixes                             836
  eligible binary subsets            62,030,604,700
  prefix passes                                   0
  box passes                                      0
  box distance range             0.143585--0.423998
  distance/tolerance range            10.17--117.66
  minimum failure margin                   0.142335
  maximum primal--dual gap     $5.83\times10^{-15}$

All 32 expanded distances improve relative to the frozen RH-248 box [@WangRH248]; the improvement ranges from $2.43\times10^{-7}$ to $0.00583514$. Improvement is not reachability: the best expanded point remains more than ten local tolerances away.

At each archived endpoint, no prefix or binary subset of the margin-32 conjugate-complete shells reaches the deterministic anchor within the local noise tolerance.

The computed box distance is larger than tolerance at all endpoints, and Proposition [\[prop:dominance\]](#prop:dominance){reference-type="ref" reference="prop:dominance"} applies. The dual objectives agree with the primal values to the stated floating tolerance.

# Boundary and next route

The conclusion is confined to the finite margin-32 single-use shell class. It does not exclude a still larger resolved window, unbounded weights, or a signed/complex selector forced by invariant quotient algebra. It also does not provide interval enclosures for the eigensolver roots.

The live next route is therefore structural rather than another box scan: derive signed or complex coefficients from a quotient identity and audit whether they form a legal selector. Gates A--E remain false/open. No Hilbert--Polya operator, Riemann-zero identification, zeta-divisor equality, or RH implication is claimed.
