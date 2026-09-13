---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kneading-pruning-hofbauer"
canonical_tex: "henon_dynamics/henon_kneading_pruning_hofbauer/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kneading_pruning_hofbauer/paper/main.pdf"
source_sha256: "5e08d6ea47e82d2fc9052dcfe1af1c7ed81f2e15a128a46fa6d501a8786a11de"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Finite Kneading/Pruning Gate for a Hénon Symbolic Candidate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kneading_pruning_hofbauer>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kneading_pruning_hofbauer/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kneading_pruning_hofbauer/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kneading_pruning_hofbauer/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test a source-locked finite kneading candidate for the certified two-branch Hénon interface. Cyclic binary words are admitted only when all lexicographic comparisons are decided by a frozen 32-symbol pair. Through period twelve we enumerate rooted periodic words, invert repetitions exactly, and compute the formal determinant prefix $D(z)=\exp(-\sum_n t_nz^n/n)$. Independent reconstruction and symbolic checks agree. The result is a finite A2 certificate, not an infinite Hénon coding theorem: unresolved comparisons remain excluded, so A1 is open and no analytic Fredholm determinant or arithmetic interpretation is claimed.
author:
- 'Anonymous Route-A report'
title: A Finite Kneading/Pruning Gate for a Hénon Symbolic Candidate
```

## Markdown 正文

# Frozen candidate

Let $K^-<K^+$ be the frozen lower and upper binary bounds generated from a fixed morphic seed. For a word $w$ of length $n$, every cyclic suffix is compared with both bounds. A word is accepted only if every comparison is decided within 32 symbols and lies in the interval. This convention makes the finite object deterministic and prevents unresolved tails from being silently promoted.

# Exact finite ledger

Write $t_n$ for the number of accepted rooted words and $p_n$ for primitive necklaces. The exact repetition identity is $$t_n=\sum_{d\mid n}d p_d.$$ The observed rooted counts for $n=1,\ldots,12$ are $$0,2,6,14,30,62,112,238,456,902,1804,3542.$$ Formal determinant coefficients are generated recursively from $$n[z^n]D=-\sum_{k=1}^n t_k[z^{n-k}]D,
\qquad D(0)=1.$$

The producer and an independent implementation agree on every accepted word, primitive count, and determinant coefficient through degree twelve.

Both implementations enumerate all binary words directly, apply the same frozen comparison length, and independently check rotation invariance. The divisor identity and the coefficient recurrence then give exact rational cross-checks; a SymPy series calculation agrees coefficient by coefficient.

  object                                 count
  ------------------------------------ -------
  periods checked                           12
  accepted rooted words at period 12      3542
  primitive necklaces at period 12         289
  independent checks                         5

# A1/A2 boundary

The finite ledger supports 'A2\_CERTIFIED\_PREFIX'. It does not prove that the frozen pair is the infinite kneading invariant of the Hénon repeller, that every accepted word lifts to a geometric orbit, or that the Hofbauer operator is positive recurrent/nuclear. Thus the preregistered verdict is 'A1\_OPEN', 'A2\_CERTIFIED\_PREFIX', 'A3\_NOT\_ADDRESSED', and 'A4\_FAIL'. No prime table, Riemann-zero table, Euler factor, automorphy statement, or Hilbert--Pólya operator is used.

# Reproducibility

The JSON evidence, independent checker, SymPy check, replay test, mutation audit, and release manifest are shipped with this paper. A future upgrade must add a source-backed infinite coding theorem and a tail/nuclearity bound for the same transfer object.
