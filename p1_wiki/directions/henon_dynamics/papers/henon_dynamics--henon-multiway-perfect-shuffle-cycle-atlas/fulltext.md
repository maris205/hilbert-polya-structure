---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-multiway-perfect-shuffle-cycle-atlas"
canonical_tex: "henon_dynamics/henon_multiway_perfect_shuffle_cycle_atlas/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_multiway_perfect_shuffle_cycle_atlas/paper/main.pdf"
source_sha256: "68476d72d3012827c70f3167be163d3a3560e1bab10e5705da8743049c1b350a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An exact cycle atlas for multiway perfect shuffles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_multiway_perfect_shuffle_cycle_atlas>)
- [规范 TeX](<../../../../../henon_dynamics/henon_multiway_perfect_shuffle_cycle_atlas/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_multiway_perfect_shuffle_cycle_atlas/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_multiway_perfect_shuffle_cycle_atlas/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We treat a perfect multiway shuffle as a deterministic finite dynamical system. For integers $k\ge2$ and $n\ge1$, the $kn$ card positions are the nonzero residues modulo $M=kn+1$ and one tick is $\rho_{k,n}(i)=ki\pmod M$. A fixed-point congruence gives $\operatorname{Fix}(\rho^r)=\gcd(k^r-1,M)-1$; gcd strata give each position's least period, and Möbius inversion separates primitive cycles from repeats. We prove the resulting formulas for the whole parameter family, verify them against literal packet interleaving on 50 parameter pairs, and factor the source-local finite zeta and Koopman characteristic polynomial. The atlas is exact but deliberately makes no target arithmetic or Hilbert--Pólya claim.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: An exact cycle atlas for multiway perfect shuffles
```

## Markdown 正文

suppressoptionalinfo 611

# Frozen shuffle and packet convention

Fix $k\ge2$, $n\ge1$, put $M=kn+1$, and let $D_M=\{1,\ldots,M-1\}$. We use the in-shuffle convention of Ellis--Fan--Shallit: $k$ equal piles are interleaved in reverse pile order. If a position is written $i=jn+r$ with $0\le j<k$ and $1\le r\le n$, its literal packet destination is $$\pi_{k,n}(i)=kr-j.                                             \tag{1}$$ The elementary identity $$ki=kjn+kr\equiv kr-j\pmod{kn+1}$$ shows that (1) is the nonzero representative of $ki$ modulo $M$. Thus the packet operation and the residue map are the same map, while the two descriptions provide genuinely independent implementations.

# All-period theorem

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For every $r\ge1$, $$F_r:=|\operatorname{Fix}(\rho_{k,n}^r)|=\gcd(k^r-1,M)-1.               \tag{2}$$ Moreover $\gcd(\rho(i),M)=\gcd(i,M)$ and, with $q_i=M/\gcd(i,M)$, the least period of $i$ is $$\tau(i)=\operatorname{ord}_{q_i}(k).                                  \tag{3}$$

Because $M\equiv1\pmod k$, $k$ is a unit modulo $M$. A residue is fixed by the $r$th iterate exactly when $(k^r-1)i\equiv0\pmod M$. This congruence has $\gcd(k^r-1,M)$ solutions modulo $M$, one of which is the excluded zero, which proves (2). Multiplication by a unit preserves gcd with $M$. Dividing the congruence for a fixed position by $\gcd(i,M)$ leaves $k^r\equiv1\pmod{q_i}$; minimality gives (3).

[\[prop:zeta\]]{#prop:zeta label="prop:zeta"} Let $E_r$ be the number of positions of exact least period $r$ and $C_r$ the number of oriented cycles. Then $$E_r=\sum_{d\mid r}\mu(r/d)F_d,\qquad C_r=E_r/r,                         \tag{4}$$ and $C_r=0$ unless $r\mid\operatorname{ord}_M(k)$. If $P$ is the permutation matrix, the finite source factors are $$Z_{k,n}(z)=\prod_{r\ge1}(1-z^r)^{-C_r},\qquad
 \det(\lambda I-P)=\prod_{r\ge1}(\lambda^r-1)^{C_r}.                  \tag{5}$$

Every fixed point has one least period, so $F_r=\sum_{d\mid r}E_d$ and Möbius inversion gives (4). Each cycle contributes exactly $r$ positions. The cycle decomposition of a permutation matrix is a direct sum of cyclic shift blocks, whose zeta and characteristic factors are the two factors in (5).

\>0

# Gcd strata and cross-parameter evidence

The all-parameter statement is not a finite extrapolation: (2)--(5) are integer congruence identities for every $k,n$. The receipt nevertheless exhausts the grid $2\le k\le6$, $1\le n\le10$. It records each global order, all fixed and exact-period counts through that order, direct cycle lengths, and seven additional all-position ledgers. Composite moduli are retained; no coprimality assumption on $M$ beyond $\gcd(k,M)=1$ is inserted.

For an explicit independence check, the checker computes (1) from pile and within-pile indices and compares it to modular multiplication at all 1,100 positions in the 50-grid. It then traverses each permutation from scratch. The selected spectral rows expand the polynomial denominator $Z_{k,n}(z)^{-1}=\det(I-zP)$ and the Koopman characteristic polynomial in exact integer coefficients, making the finite factors auditable rather than typographical.

\>1

# Receipt, controls, and Route-A boundary

The deterministic producer emits 50 atlas rows, 74 position rows, six spectral rows and one representative cycle. The independent checker passes 2,303 assertions; an independent SymPy program passes 50 identities; byte replay is exact; and 44 hostile mutations are rejected, including repaired payload hashes, row reordering, citation edits, unknown keys and route/scope tampering. Two fresh LuaLaTeX builds per round use the fixed epoch `SOURCE_DATE_EPOCH=1788048000`.

The strict evaluation tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_PASS\_ANALYTIC},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_NATURAL\_QUANTIZATION}),$$ with `ROUTE_A_REJECTED`. The exact finite zeta in (5) is a source-local permutation identity; it is not a target divisor, functional equation, Euler product, or zero-set match. Deck size and modular order provide no intrinsic rational-prime labels or logarithmic clock.

9 J. Ellis, H. Fan, and J. Shallit, "The Cycles of the Multiway Perfect Shuffle Permutation," *Discrete Mathematics & Theoretical Computer Science* 5 (2002). DOI: [10.46298/dmtcs.308](https://doi.org/10.46298/dmtcs.308).

R. W. Packard and E. S. Packard, "The Order of a Perfect $k$-Shuffle," *The Fibonacci Quarterly* 32(2), 136--144 (1994). DOI: [10.1080/00150517.1994.12429237](https://doi.org/10.1080/00150517.1994.12429237).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; the paper contains no target arithmetic, Euler-factor, target-zero, automorphy or Hilbert--Pólya claim. **Data and code.** Exact formulas, direct cycle ledgers and independent audit programs accompany HCS-C239. **AI-use disclosure.** Generative tools assisted drafting and code generation; all displayed claims are checked by the declared programs. This is not external peer review.
