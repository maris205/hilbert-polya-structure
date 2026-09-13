---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-contracted-rotation-mode-locking-atlas"
canonical_tex: "henon_dynamics/henon_contracted_rotation_mode_locking_atlas/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_contracted_rotation_mode_locking_atlas/paper/main.pdf"
source_sha256: "6e96ad517a32f91a2991cf017bb26d138e2eb3a5923326648ff4271f19150c63"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Itinerary Intervals and Mode Locking for a Contracted Rotation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_contracted_rotation_mode_locking_atlas>)
- [规范 TeX](<../../../../../henon_dynamics/henon_contracted_rotation_mode_locking_atlas/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_contracted_rotation_mode_locking_atlas/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_contracted_rotation_mode_locking_atlas/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a finite, exact atlas for the discontinuous contracted rotation $f_{\lambda,\delta}(x)=\{\lambda x+\delta\}$ on $[0,1)$. A binary carry word determines an affine return map with slope $\lambda^n$, hence one candidate fixed point. For $\lambda\in\{1/2,2/3,3/4\}$ we enumerate all 747 primitive cyclic representatives through length 12 for each slope and intersect the half-open branch inequalities using rational arithmetic. The receipt contains 2241 word rows, 138 nonempty components, exact endpoint equalities, and 295 independent direct-iteration probes. Grouped carry rotation values expose mode-locking components, but we do not call their union maximal. A source-local factor $1-z^n\lambda^n$ is recorded only as itinerary bookkeeping. There is no arithmetic clock or target determinant; the strict Route-A verdict is `ROUTE_A_REJECTED`.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: Exact Itinerary Intervals and Mode Locking for a Contracted Rotation
```

## Markdown 正文

suppressoptionalinfo 611

# Map, branches, and the question

The fractional-part notation hides a genuine modelling choice at the jump. We freeze the half-open state space $I=[0,1)$ and write $$x_{j+1}=\lambda x_j+\delta-k_j,\qquad
 k_j\leq\lambda x_j+\delta<k_j+1,\qquad k_j\in\{0,1\}. \tag{1}$$ Thus the lower carry equality belongs to a branch and the upper equality does not. The research question is whether this convention permits an exact finite mode-locking certificate rather than a floating-point picture. The answer below is affirmative at an explicit cutoff, with all global claims carefully withheld.

# Affine words and exact admissibility

For $w=(k_0,\ldots,k_{n-1})$, $$f_w(x)=\lambda^n x+\delta\sum_{r=0}^{n-1}\lambda^r
 -\sum_{j=0}^{n-1}k_j\lambda^{n-1-j}. \tag{2}$$ Consequently the word has one candidate fixed point $$x_w(\delta)=\frac{\delta}{1-\lambda}
 -\frac{K_w}{1-\lambda^n},\qquad
 K_w=\sum_{j=0}^{n-1}k_j\lambda^{n-1-j}, \tag{3}$$ and derivative $(f_w)'=\lambda^n$.

Substitution of (1) gives (2). Since $0<\lambda^n<1$, solving $f_w(x)=x$ gives (3), and differentiating (2) gives the derivative.

Write $x_j(\delta)=a_j\delta+b_j$, beginning with (3), and update $(a_{j+1},b_{j+1})=(\lambda a_j+1,\lambda b_j-k_j)$. The next result is the computational core.

The parameter set for which $w$ is an admissible cycle is exactly $$\mathcal D_w=\left\{\delta\in[0,1):
 0\leq a_j\delta+b_j<1,\quad
 k_j\leq\lambda(a_j\delta+b_j)+\delta<k_j+1\ \forall j\right\}. \tag{4}$$ For rational $\lambda$, this is an exactly computable rational interval, possibly empty, with independently recorded endpoint closure.

The inequalities are necessary by the state domain and (1). If they hold, each selected carry is exactly $k_j$, so (2) returns the candidate to itself. Every inequality is an affine half-line in $\delta$, and finite intersection preserves exact rational endpoints and their open/closed status.

# Primitive representatives and the finite atlas

A word is primitive when it is not a repetition of a shorter block. We keep the lexicographically least cyclic rotation. Its source-local rotation label is $$\rho(w)=\frac{1}{n}\sum_{j=0}^{n-1}k_j. \tag{5}$$ The exact factor $1-z^n\lambda^n$ is useful for checking repetition and derivative bookkeeping, but it is not a target determinant.

The census uses all primitive canonical words of lengths 1 through 12. There are 747 per slope and 2241 rows in total. Only 138 rows have nonempty $\mathcal D_w$; grouped rows retain each component interval and its word id. Table [1](#tab:examples){reference-type="ref" reference="tab:examples"} gives representative rows (all omitted rows are in the machine-readable receipt).

::: {#tab:examples}
   $\lambda$   word   $\mathcal D_w$   $\rho(w)$   $\lambda^n$
  ----------- ------ ---------------- ----------- -------------
     $1/2$      0       $[0,1/2)$          0           1/2
     $1/2$      01     $[2/3,5/6)$        1/2          1/4
     $1/2$     001     $[4/7,9/14)$       1/3          1/8
     $2/3$      01    $[3/5,11/15)$       1/2          4/9
     $3/4$      01    $[4/7,19/28)$       1/2         9/16

  : Exact word-certified components. Every upper endpoint is open under the convention (1). These intervals are not asserted maximal.
:::

The endpoint audit evaluates every active equality, including the parameter constraint $\delta<1$. For example, the lower endpoint $2/3$ of the $\lambda=1/2$, word 01 component satisfies the carry-1 lower equality and is accepted; at $5/6$, carry-0 reaches its upper equality and is rejected. This is why a decimal plot alone cannot certify the interval.

# Independent iteration and literature boundary

For each slope we also probe eight base values $\delta=i/8$ and every distinct endpoint. A separate implementation runs 360 iterations at 90 decimal digits, detects a repeated suffix of length at most 12, and compares its affine fixed point with the exact rational candidate. The 295-row ledger is a control for the finite certificate, not a claim beyond the cutoff.

Laurent and Nogueira study this contracted-rotation family and its rotation number, including algebraic-parameter phenomena [@laurent2018]. The interval piecewise-contraction results of Nogueira and Pires give a finite periodic-orbit bound under their stated hypotheses [@nogueira2015]. No global one-periodic-orbit theorem is claimed here: their general two-branch theorem gives only an at-most-two bound under its hypotheses. Bugeaud and Conze supply the contracting-mod-one and Farey/Hecke--Mahler context [@bugeaud1999]. Our contribution is the reproducible finite Fraction census and boundary ledger, not a priority claim.

\>0

# Audit receipt and route boundary

The independent checker validates all 2241 word rows and 295 direct rows, SymPy validates 119 generic or rational identities, byte replay matches two fresh producer runs, and 33 repaired-hash hostile mutations are rejected. The three revision PDFs are content-distinct; each is built twice with the fixed epoch `1788048000`, and the final PDF equals round 2 byte-for-byte.

\>1 The source has no intrinsic rational-prime carrier, so A0 fails. A1 is limited to the finite analytic word certificate. A2 is an explicit target-match failure: no target determinant or zero comparison is defined. No continuation or functional equation is supplied (A3\_FAIL), and the scalar contraction gives only a formal lift hint (A4\_FORMAL\_HINT). Thus $$(\mathtt{A0\_FAIL},\mathtt{A1\_PASS\_ANALYTIC},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT})$$ and `ROUTE_A_REJECTED`; Route B is disabled.

9 M. Laurent and A. Nogueira, "Rotation number of contracted rotations," *Journal of Modern Dynamics* 12 (2018), 175--191, DOI: [10.3934/jmd.2018007](https://doi.org/10.3934/jmd.2018007). A. Nogueira and B. Pires, "Dynamics of piecewise contractions of the interval," *Ergodic Theory and Dynamical Systems* 35 (2015), 2198--2215, DOI: [10.1017/etds.2014.16](https://doi.org/10.1017/etds.2014.16). Y. Bugeaud and J.-P. Conze, "Calcul de la dynamique d'une classe de transformations linéaires contractantes mod 1 et arbre de Farey," *Acta Arithmetica* 88 (1999), 201--218, DOI: [10.4064/aa-88-3-201-218](https://doi.org/10.4064/aa-88-3-201-218).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; all determinant language is source-local itinerary bookkeeping. No target arithmetic, target-zero, Euler-factor, root-data, automorphy, or Hilbert--Pólya claim is made. **Data and code.** Exact rows, checker, replay, and mutation audit are included in the release. This is not external peer review. **AI-use disclosure.** Generative tools assisted drafting and code generation; displayed formulas and metadata are checked by the deterministic artifact chain.
