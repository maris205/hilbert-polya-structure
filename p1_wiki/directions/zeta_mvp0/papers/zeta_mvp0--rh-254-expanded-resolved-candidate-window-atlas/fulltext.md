---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-254-expanded-resolved-candidate-window-atlas"
canonical_tex: "zeta_mvp0/papers/RH-254-expanded-resolved-candidate-window-atlas/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-254-expanded-resolved-candidate-window-atlas/main.pdf"
source_sha256: "3ff41f1a35447cb41f191c7e114b6fb09c2e04f3b669e2ac4783956825f8d5bc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Expanded Resolved Candidate-Window Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-254-expanded-resolved-candidate-window-atlas>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-254-expanded-resolved-candidate-window-atlas/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-254-expanded-resolved-candidate-window-atlas/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-254-expanded-resolved-candidate-window-atlas/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-254-expanded-resolved-candidate-window-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The frozen RH-244/RH-248 shell class was exhausted, so RH-251 required a genuinely expanded resolved window before another anchor test. We double the RH-222 candidate margin from 16 to 32 at all 32 noise/channel endpoints [@WangRH222; @WangRH248]. The expanded eigensolver returns 16 additional bulk roots at every endpoint, and the archived roots match with maximum discrepancy $7.41\times10^{-9}$. A fixed-count window is not always shell-complete: 11 endpoints terminate in a split conjugate pair. After removing those boundary fragments, the complete expanded ranks lie between 33 and 64. This paper supplies the finite spectral input for RH-255; it does not yet test the deterministic anchor.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Expanded Resolved Candidate-Window Atlas'
```

## Markdown 正文

# Expansion protocol

The RH-222 atlas uses noise scales [@WangRH222] $$\begin{gathered}
 0.04,0.032,0.025,0.02,0.016,0.0125,0.01,0.008,\\
 0.00625,0.005,0.004,0.0032,0.0025,0.002,0.0016,0.00125.
\end{gathered}$$ and two channels (fine and Haar-coarse). At target rank $k$, the old resolution requested $k+16$ leading eigenvalues; the present audit requests $k+32$. The same deterministic starting vector, tolerance, and Hardy scaling are used, so the comparison is a controlled enlargement rather than a change of operator.

[\[prop:window\]]{#prop:window label="prop:window"} At each of the 32 endpoints the expanded computation resolves 16 more bulk roots than the archived window. Matching every old root to a distinct new root gives maximum error $$7.4054691027\times10^{-9},$$ while Perron and parity discrepancies are below $10^{-14}$.

The experiment constructs the same sparse folded-Gaussian matrix and calls the same deterministic eigensolver with the larger candidate count. A rectangular absolute-difference cost matrix is solved by a one-to-one assignment, and the reported maximum is the largest matched distance. The two distinguished roots are compared directly with their archived values.

# Conjugate-shell boundary

Because the matrices are real, a legitimate shell selector must use real roots or complete conjugate pairs. The final root of a finite eigensolver window can be one member of a pair. The audit therefore partitions the expanded roots by the RH-222 shell rule and reports both raw and shell-complete ranks.

  quantity                                           value
  ---------------------------------- ---------------------
  endpoints                                             32
  raw expanded rank range                           34--64
  new raw roots per endpoint                            16
  shell-complete rank range                         33--64
  shell-complete endpoints                           21/32
  split-pair endpoints                               11/32
  maximum discarded boundary roots                       1
  maximum old/new matching error       $7.41\times10^{-9}$

The split-pair count is a boundary artifact of fixed-count resolution, not a claim that the underlying operator lacks conjugate symmetry. RH-255 uses only the complete shells and records the discarded fragments explicitly.

# Scope and next result

This is a finite expanded candidate window, not an interval-certified spectral set and not a uniform small-noise theorem. No anchor has yet been shown to be reachable, and the old frozen obstruction is not silently reused. The next paper must perform an anchored zonotope/cone audit on the complete expanded shells. Gates A--E remain false/open; no Hilbert--Polya operator, zeta-divisor identification, Riemann-zero identification, or RH implication is asserted.
