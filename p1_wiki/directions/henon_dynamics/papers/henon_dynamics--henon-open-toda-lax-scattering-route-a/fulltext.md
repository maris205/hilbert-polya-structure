---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-open-toda-lax-scattering-route-a"
canonical_tex: "henon_dynamics/henon_open_toda_lax_scattering_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_open_toda_lax_scattering_route_a/paper/main.pdf"
source_sha256: "90b57390e334d9ac284b03032c92ade004a54d719807dbbba762b0912b5101a6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite Open Toda Flow: Lax Isospectrality, Sorting Scattering, and Norming Coordinates

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_open_toda_lax_scattering_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_open_toda_lax_scattering_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_open_toda_lax_scattering_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_open_toda_lax_scattering_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close a convention-complete theorem for the finite open Toda Hamiltonian $H=\frac12\sum p_j^2+\sum_{j<N}e^{q_j-q_{j+1}}$. The Flaschka variables turn its equations into a Lax flow of a positive Jacobi matrix. Conserved traces give global existence and prevent any finite-time edge collision. For simple spectrum, the eigenvalues are fixed and the Moser sorting theorem identifies the two asymptotic velocity orders; the first-component norming weights obey an exact normalized exponential law. For $N=2$ the full trajectory is a sech/tanh formula. We keep separate the noncompact positive scattering chamber, the phase-compactified isospectral torus, and the repeated-root block boundary. A deterministic ledger audits six rational source rows. This is a source-local integrability result: there is no arithmetic owner, target determinant, or Hilbert--Polya bridge.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Finite Open Toda Flow: Lax Isospectrality, Sorting Scattering, and Norming Coordinates'
```

## Markdown 正文

suppressoptionalinfo 611

# Model and Lax closure

For $N\ge2$, use $$H(q,p)=\frac12\sum_{j=1}^{N}p_j^2+
 \sum_{j=1}^{N-1}e^{q_j-q_{j+1}},\qquad
 \dot q_j=p_j,\quad
 \dot p_j=e^{q_{j-1}-q_j}-e^{q_j-q_{j+1}}, \tag{1}$$ where missing endpoint exponentials are zero. Set $a_j=\tfrac12e^{(q_j-q_{j+1})/2}>0,\ b_j=-p_j/2$, and let $L$ have diagonal $b_j$ and off-diagonal $a_j$. Let $B_{j,j+1}=a_j=-B_{j+1,j}$. Direct multiplication gives $$\dot L=[B,L],\qquad
 \dot a_j=a_j(b_{j+1}-b_j),\qquad
 \dot b_j=2(a_j^2-a_{j-1}^2),\quad a_0=a_N=0. \tag{2}$$

[\[thm:global\]]{#thm:global label="thm:global"} Every finite initial state has a solution for all $t\in\mathbb R$; all $a_j(t)$ remain positive. The eigenvalues of $L$ and $I_k=\operatorname{tr}(L^k)/k$ are constant, with $H=4I_2$ and $\sum_jp_j=-2\operatorname{tr}L$.

Since $B^T=-B$, cyclicity gives $\frac d{dt}\operatorname{tr}L^k=k\operatorname{tr}(L^{k-1}[B,L])=0$. In particular $\operatorname{tr}L^2$ bounds every matrix entry, so the smooth finite-dimensional vector field is complete. Also $a_j(t)=a_j(0)\exp(\int_0^t(b_{j+1}-b_j)\,ds)>0$; hence a zero edge is only a boundary limit. Reconstructing $q_j-q_{j+1}=2\log(2a_j)$ and $p_j=-2b_j$ proves the Hamiltonian statement.

# Simple spectrum and sorting

An irreducible real symmetric Jacobi matrix has simple real eigenvalues. Order them $\lambda_1>\cdots>\lambda_N$. The finite open Toda scattering theorem states $$b_j(t)\to\lambda_j\ (t\to+\infty),\qquad
 b_j(t)\to\lambda_{N+1-j}\ (t\to-\infty), \tag{3}$$ and $q_j(t)=-2\lambda_jt+c_j^++o(1)$ at $+\infty$, with reversed order at the other end. The recurrence proof of simplicity is short: an eigenvector with first component zero has every component zero.

For a normalized eigenvector $v(\lambda_k)$, define $\rho_k=|v_1(\lambda_k)|^2$. The Weyl residues are positive and sum to one, and $$\rho_k(t)=\frac{\rho_k(0)e^{2\lambda_kt}}
 {\sum_\ell\rho_\ell(0)e^{2\lambda_\ell t}},\qquad
 b_1(t)=\sum_k\lambda_k\rho_k(t). \tag{4}$$ Indeed $v_t=Bv$ gives $\dot\rho_k=2(\lambda_k-b_1)\rho_k$, which integrates to (4). The dominant exponent explains the two sorting ends; continued-fraction inversion of the Weyl function supplies the remaining diagonal limits.

\>0

# Closed two-body result and action--angle boundary

For $N=2$, writing $$d=\sqrt{(b_1-b_2)^2+4a_1^2},\qquad
 \alpha=\operatorname{artanh}\frac{b_1-b_2}{d},$$ gives the exact solution $$a_1(t)=\frac d2\operatorname{sech}(dt+\alpha),\qquad
 b_{1,2}(t)=\frac{b_1+b_2\pm d\tanh(dt+\alpha)}2. \tag{5}$$ Thus the edge is positive at finite time and decays only at the two scattering ends; the eigenvalues are $(b_1+b_2\pm d)/2$.

On the simple-spectrum regular set, ordered eigenvalues plus the positive norming simplex $\rho_k>0,\sum\rho_k=1$ are inverse-scattering coordinates. After removing the center-of-mass action, logarithmic norming variables furnish local canonical action--angle coordinates. The physical positive isospectral leaf is an open, noncompact scattering chamber, not a compact real Liouville torus. Adjoining complex norming phases compactifies the angles to an $(N-1)$-torus; that extension is a geometric boundary description, not a target operator or a periodic Toda claim. More explicitly, in the complexified inverse-spectral chart the nonzero residues have a common $\mathbb C^\times$ gauge; fixing their moduli leaves the phase fiber $(S^1)^N/S^1\simeq\mathbb T^{N-1}$ over each simple spectrum. For a direct all-$N$ check, define $r_k(t)=\rho_k(0)e^{2\lambda_k t}$ and the Hankel minors $$\tau_j=\sum_{|S|=j}\Bigl(\prod_{k\in S}r_k\Bigr)\Delta(\lambda_S)^2,\quad
 a_j=\frac{\sqrt{\tau_{j-1}\tau_{j+1}}}{\tau_j},\quad
 b_j=\frac12\partial_t\log\frac{\tau_j}{\tau_{j-1}}.$$ Dominant top/bottom subsets prove the two sorting ends exactly; the ledger uses the equivalent normalized-residue form.

# Reproducible ledger

The receipt uses six rational $a,b$ rows (three each for $N=2,3$), 256 RK4 steps per unit time, and 90-decimal arithmetic. It stores all 30 states at $t=-2,-1,0,1,2$, every trace invariant, sorted eigenvalues, positivity and drift. Fifteen $N=2$ rows compare (5) directly; nine $N=3$ rows compare (4) at $t=-1,0,1$. Six $T=8$ endpoint rows are finite diagnostics of (3), not exact limits. Representative initial spectra are

  case             $N$     $(a_j)$         $(b_j)$
  --------------- ----- ------------- ------------------
  N2 reference      2       $(1)$        $(1/2,-1/2)$
  N2 asymmetric     2      $(3/4)$       $(1/3,-1/6)$
  N3 symmetric      3      $(1,1)$        $(1,0,-1)$
  N3 generic        3    $(1/2,3/2)$   $(1/2,-1/4,1/3)$

The independent checker reconstructs the ODE and matrix spectrum without importing the producer. SymPy checks 25 identities; canonical replay is byte-identical and the hostile suite rejects 22 of 22 repaired mutations.

\>1

# Degenerate face and strict Route-A boundary

At $a_j=0$, $L$ splits into blocks and regular simplicity/action--angle coordinates stop applying. The explicit $N=3$ boundary $L=\operatorname{diag}(0,0,1)$ has characteristic polynomial $x^2(x-1)$: the repeated root is a block degeneracy, not a positive Jacobi spectrum. The finite characteristic polynomial $\det(\lambda I-L)$ is source-local and is not an orbit zeta or Fredholm determinant.

The strict evaluator tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_FAIL},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),$$ with `ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. The open chain has no rational-prime owner, primitive periodic repetition law, target divisor, or natural Hilbert--Polya lift. Its Hamiltonian scattering theorem remains a substantive positive result.

9 H. Flaschka, The Toda lattice. II. Existence of integrals, *Physical Review B* 9 (1974), 1924--1925. DOI: [10.1103/PhysRevB.9.1924](https://doi.org/10.1103/PhysRevB.9.1924). J. Moser, Finitely many mass points on the line under the influence of an exponential potential--an integrable system, in *Dynamical Systems, Theory and Applications*, Lecture Notes in Physics 38, Springer (1975), 467--497. DOI: [10.1007/3-540-07171-7\_12](https://doi.org/10.1007/3-540-07171-7_12). C. Tomei, The topology of isospectral manifolds of tridiagonal matrices, *Duke Mathematical Journal* 51 (1984), 981--996. DOI: [10.1215/S0012-7094-84-05144-5](https://doi.org/10.1215/S0012-7094-84-05144-5).

\>1

# Proof and audit supplement {#proof-and-audit-supplement .unnumbered}

The first-component identity behind (4) is exact. If $Lv_k=\lambda_kv_k$ and $\dot v_k=Bv_k$, then $(\dot v_k)_1=a_1(v_k)_2=(\lambda_k-b_1)(v_k)_1$; squaring and normalizing gives $\dot\rho_k=2(\lambda_k-b_1)\rho_k$. The positive residues and ordered eigenvalues determine the Weyl rational function $m(z)=\sum_k\rho_k/(z-\lambda_k)$. Its Stieltjes continued fraction uniquely recovers every positive Jacobi coefficient, so concentration of the residues at the two time ends yields the complete sorting statement rather than only the $b_1$ limit.

The finite receipt is a control on the implementation, not the proof of the limits. Across all stored times, the largest trace-invariant drift is $2.79\times10^{-10}$, the largest spectral drift is $1.17\times10^{-10}$, the largest two-body formula error is $4.55\times10^{-11}$, and the largest norming-law discrepancy is $1.71\times10^{-10}$. Weaker links converge more slowly at $T=8$, so their nonzero endpoint errors are retained. The producer-independent checker makes 596 assertions; all finite rows remain strictly inside the positive chamber.

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, target-zero, determinant matching, or Hilbert--Polya claim. **Data and code.** All rows and audits accompany HCS-C230. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checks displayed formulas and metadata. This is not external peer review.
