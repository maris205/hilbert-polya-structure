---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-luroth-countable-branch-periodic-atlas"
canonical_tex: "henon_dynamics/henon_luroth_countable_branch_periodic_atlas/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_luroth_countable_branch_periodic_atlas/paper/main.pdf"
source_sha256: "153df117b8d731dd53e688d26da8f96af649c12438fdd8b3f4cd5f155c1b38d9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact periodic words for the classical Lüroth map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_luroth_countable_branch_periodic_atlas>)
- [规范 TeX](<../../../../../henon_dynamics/henon_luroth_countable_branch_periodic_atlas/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_luroth_countable_branch_periodic_atlas/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_luroth_countable_branch_periodic_atlas/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a source-local periodic-orbit atlas for the classical Lüroth map, whose branch alphabet is countably infinite. On $I_m=(1/m,1/(m-1)]$, $m\ge2$, the map is affine with slope $a_m=m(m-1)$ and image $(0,1]$; the isolated endpoint $0$ is fixed by convention. Every finite branch word has one rational fixed point of its inverse contraction, an exact product multiplier, and a forward itinerary. Möbius inversion separates primitive necklaces from repetitions. We prove the finite weighted identity and state the countable limit with a sharp domain distinction: absolute primitive-product/log convergence needs both $\operatorname{Re}(s)>1/2$ and $|z|A(\operatorname{Re}(s))<1$, whereas $1/(1-zA(s))$ is a meromorphic continuation away from denominator zeros in the larger half-plane. No target arithmetic or Hilbert--Pölya claim is made.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: Exact periodic words for the classical Lüroth map
```

## Markdown 正文

suppressoptionalinfo 611

# Map, branches, and endpoint convention

For $x\in(0,1]$ put $m=\lfloor1/x\rfloor+1$ and define $$T_L(x)=m(m-1)x-(m-1),\qquad T_L(0)=0.                         \tag{1}$$ The intervals $I_m=(1/m,1/(m-1)]$ partition $(0,1]$. On $I_m$, the derivative is $a_m=m(m-1)$ and the image is $(0,1]$: the right endpoint maps to $1$, while $0$ is only the limit at the excluded left endpoint. The inverse branch is $$\phi_m(y)=\frac{y+m-1}{m(m-1)},\qquad y\in(0,1].                  \tag{2}$$ Although (2) formally gives $\phi_m(0)=1/m$, that boundary point is not in $I_m$; this prevents a hidden double coding.

# Word theorem

Let $w=(w_1,\ldots,w_r)$ be a finite word over $\{2,3,\ldots\}$. In forward itinerary order set $$\Phi_w=\phi_{w_1}\circ\cdots\circ\phi_{w_r}(y)=u_wy+v_w,\qquad
 u_w=\prod_{j=1}^r a_{w_j}^{-1}.                                  \tag{3}$$ Since $0<u_w<1$, contraction gives $x_w=v_w/(1-u_w)$. Exact interval substitution verifies that its itinerary is $w$ (with the endpoint convention above), and hence $$(T_L^r)'(x_w)=A_w=\prod_{j=1}^r w_j(w_j-1).                       \tag{4}$$

Every finite word has exactly one coded fixed point of (3). Its least physical period is the least repetition period of the word. Cyclic rotations give the same oriented orbit, and primitive necklaces are primitive words modulo these rotations. For a finite alphabet of size $q$, the number of primitive necklaces of length $r$ is $$N_r(q)=\frac1r\sum_{d\mid r}\mu(d)q^{r/d}.                       \tag{5}$$

Equation (3) is a strict affine contraction, so its fixed point is unique. Applying the forward branch maps to that point recovers the symbols in order; repeating a shorter word is therefore equivalent to a shorter physical return. The cyclic action preserves the orbit orientation. Finally, words of length $r$ decompose uniquely according to their least period, and Möbius inversion of $q^r=\sum_{d\mid r}dN_d(q)$ yields (5).

The full alphabet is countable. For every $r\ge1$, choosing the first symbol from infinitely many labels while fixing the remaining symbols produces countably infinitely many distinct coded words and periodic points (apart from the separately declared endpoint $0$). A finite cutoff is thus a receipt slice, not a finite model of the mathematical map.

# Weighted identity and convergence boundaries

Let $w_m(s)=a_m^{-s}$ and $A_M(s)=\sum_{m=2}^M w_m(s)$. Concatenating finite words gives $$Z_M(z,s)=\sum_{r\ge0}z^rA_M(s)^r
 =\frac{1}{1-zA_M(s)}.                                             \tag{6}$$ The primitive-necklace factors reproduce (6) as a formal power series (and analytically where $|z|A_M(\operatorname{Re}s)<1$).

For the countable alphabet put $A(s)=\sum_{m\ge2}[m(m-1)]^{-s}$. Comparison with $\sum_{m\ge2}(m-1)^{-2\operatorname{Re}s}$ proves absolute convergence for $\operatorname{Re}(s)>1/2$. The following distinction is essential:

-   The primitive product/log expansion is absolutely convergent only when $\operatorname{Re}(s)>1/2$ *and* $|z|A(\operatorname{Re}s)<1$.

-   In the half-plane $\operatorname{Re}(s)>1/2$, the closed expression $1/(1-zA(s))$ is meromorphic away from denominator zeros. This is a continuation statement, broader than the absolute product domain.

At $\operatorname{Re}(s)=1/2$, $A(s)$ diverges, so no full-alphabet product condition is assigned to that boundary. At $s=1$, $$A(1)=\sum_{m=2}^{\infty}\frac1{m(m-1)}
 =\sum_{m=2}^{\infty}\left(\frac1{m-1}-\frac1m\right)=1,              \tag{7}$$ and $z=1$ is a denominator pole/boundary. For a cutoff $M$, the omitted tail in (7) is exactly $1/M$.

\>0

# Auditable atlas

The JSON receipt fixes branches $m=2,\ldots,12$, all 780 words over $\{2,\ldots,6\}$ of lengths 1--4, 30 finite-cutoff necklace rows, 88 weighted rows (including explicit $s=1/2$ divergence labels), three limit rows, and two formal-product rows. Every fraction, itinerary, least period, multiplier, Möbius count, and cutoff tail is recomputed by an independent checker.

\>1

# Validation and Route-A boundary

The independent checker passes its full recursive schema and arithmetic suite; an exact SymPy cross-check verifies affine inverses, all word fixed equations, the telescoping sum, and finite formal products; clean replay is byte-identical; and hostile mutations (including repaired payload hashes) are all rejected. LuaLaTeX is run twice in fresh directories for each revision under `SOURCE_DATE_EPOCH=1788048000`. The locked evaluation tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_PASS\_ANALYTIC},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),$$ with `ROUTE_A_REJECTED`. The source-local identity (6) is not a target Euler product, divisor, functional equation, or zero correspondence; branch labels are not rational primes and no Hilbert--Pölya operator is proposed.

9 J. Barrionuevo, R. M. Burton, K. Dajani, and C. Kraaikamp, "Ergodic properties of generalized Lüroth series," *Acta Arithmetica* 74(4), 311--327 (1996). DOI: [10.4064/aa-74-4-311-327](https://doi.org/10.4064/aa-74-4-311-327).

J. Galambos, "Some remarks on the Lüroth expansion," *Czechoslovak Mathematical Journal* 22(2), 266--271 (1972). DOI: [10.21136/CMJ.1972.101097](https://dml.cz/dmlcz/101097).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; this paper contains no target arithmetic, prime/zero table, Euler factor, root number, automorphy, target divisor, functional equation, or Hilbert--Pölya claim. **Data and code.** Exact formulas and audit programs accompany HCS-C241. **AI-use disclosure.** Generative tools assisted drafting and code generation; displayed claims are checked by the declared programs. This is not external peer review. Audit tokens: `Luroth`, `Re(s)>1/2`, and `z=1`.
