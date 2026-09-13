---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-crow-kimura-single-peak-quasispecies-route-a"
canonical_tex: "henon_dynamics/henon_crow_kimura_single_peak_quasispecies_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_crow_kimura_single_peak_quasispecies_route_a/paper/main.pdf"
source_sha256: "b5dc24725512ea2e49c70a1f0579fb1a080e473aa136621e185a9cac54e49d4f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Single-Peak Crow--Kimura Dynamics: Complete Finite-Genome Spectrum and Exact Projective Gap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_crow_kimura_single_peak_quasispecies_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_crow_kimura_single_peak_quasispecies_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_crow_kimura_single_peak_quasispecies_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_crow_kimura_single_peak_quasispecies_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the continuous-time mutation--selection equation on binary strings of length $L$, with symmetric point mutation and one master-sequence fitness spike, we identify the nonlinear simplex flow exactly with a projectivized positive linear semigroup. Walsh decomposition shows that each Hamming eigenvalue retains an explicit codimension-one multiplicity, while all remaining eigenvalues are the roots of one degree-$(L+1)$ secular polynomial. \>0 The secular roots are simple and strictly interlace the mutation poles. The two largest roots therefore give the exact projective spectral gap, with a sharp generic convergence law. \>1 Zero selection, zero mutation and the one-locus model are closed separately; finite-length analyticity is not promoted to an infinite-genome error threshold. Exact computation is used only as an implementation receipt.
author:
- 'Route-A source-local certificate HCS-C336'
date: 3 September 2026
title: |
  Single-Peak Crow--Kimura Dynamics:\
  Complete Finite-Genome Spectrum and Exact Projective Gap
```

## Markdown 正文

trailerid \[\<C3362026090300000000000000000000\>\<C3362026090300000000000000000000\>\]

# Frozen mutation--selection owner

Let $\mathcal H_L=\mathbb R^{\{0,1\}^L}$, let $F_i$ flip bit $i$, and let $e_0$ denote the all-zero genotype. For $L\geq1$ and $U,s>0$ define $$\label{eq:operator}
 M_L=\frac UL\sum_{i=1}^L(F_i-I),\qquad
 A_L=M_L+s e_0e_0^{\mathsf T}.$$ Both matrices are real symmetric and $\mathrm{1}^{\mathsf T}M_L=0$. On the probability simplex the Crow--Kimura equation in this normalization is $$\label{eq:nonlinear}
 \dot p=A_Lp-(\mathrm{1}^{\mathsf T}A_Lp)p=A_Lp-sp_0p.$$

[\[thm:flow\]]{#thm:flow label="thm:flow"} For every probability vector $p^{\rm in}$, $$\label{eq:quotient}
 p(t)=\frac{e^{tA_L}p^{\rm in}}
 {\mathrm{1}^{\mathsf T}e^{tA_L}p^{\rm in}}$$ is the unique solution of [\[eq:nonlinear\]](#eq:nonlinear){reference-type="eqref" reference="eq:nonlinear"}. The denominator is positive, the simplex is preserved, and $p(t)$ converges to the uniquely normalized positive Perron eigenvector of $A_L$.

Write $q(t)=e^{tA_L}p^{\rm in}$ and $Z(t)=\mathrm{1}^{\mathsf T}q(t)$. Positivity of the irreducible hypercube semigroup gives $q(t)>0$ for $t>0$, hence $Z(t)>0$. Moreover $Z'=\mathrm{1}^{\mathsf T}A_Lq=sq_0$. Differentiating $q/Z$ gives exactly [\[eq:nonlinear\]](#eq:nonlinear){reference-type="eqref" reference="eq:nonlinear"}. The same calculation shows that its entries sum to one. Since $A_L$ is irreducible Metzler and symmetric, its largest eigenvalue is simple and has a strictly positive eigenvector. The Perron coefficient of every nonzero nonnegative initial vector is positive; dividing the spectral expansion by $Z(t)$ proves the limit.

The phrase *projective semigroup owner* records the theorem content of the original manuscript round.

# Complete finite-genome spectrum

For $S\subseteq\{1,\ldots,L\}$ let $$\phi_S(x)=2^{-L/2}(-1)^{\sum_{i\in S}x_i}.$$ These Walsh characters form an orthonormal basis and $$\label{eq:mutation-spectrum}
 M_L\phi_S=d_{|S|}\phi_S,\qquad
 d_k=-\frac{2Uk}{L},\qquad
 \langle e_0,\phi_S\rangle=2^{-L/2}.$$ Put $m_k=L!/[k!(L-k)!]$, $w_k=m_k/2^L$.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} The complete characteristic polynomial of $A_L$ is $$\begin{aligned}
 \det(\lambda I-A_L)
 &=q_L(\lambda)\prod_{k=0}^L
       (\lambda-d_k)^{m_k-1},\label{eq:full-factor}\\
 q_L(\lambda)
 &=\prod_{k=0}^L(\lambda-d_k)
   -s\sum_{k=0}^Lw_k\prod_{j\ne k}(\lambda-d_j).
   \label{eq:secular-polynomial}\end{aligned}$$ Thus $d_k$ is retained with multiplicity $m_k-1$ and the remaining $L+1$ eigenvalues are precisely the roots, away from the poles, of $$\label{eq:secular}
 1=s\sum_{k=0}^L\frac{w_k}{\lambda-d_k}.$$ The multiplicities in [\[eq:full-factor\]](#eq:full-factor){reference-type="eqref" reference="eq:full-factor"} sum to $2^L$.

Let $E_k=\operatorname{span}\{\phi_S:|S|=k\}$. The subspace of $E_k$ whose Walsh coefficients sum to zero is orthogonal to $e_0$ and has dimension $m_k-1$; $A_L$ acts there by $d_k$. Its orthogonal complement over all $k$ has basis $$u_k=m_k^{-1/2}\sum_{|S|=k}\phi_S,
 \qquad \langle e_0,u_k\rangle=\sqrt{w_k}.$$ The restriction of $A_L$ is $D+svv^{\mathsf T}$, where $D=\operatorname{diag}(d_0,\ldots,d_L)$ and $v_k=\sqrt{w_k}$. The matrix determinant lemma gives [\[eq:secular-polynomial\]](#eq:secular-polynomial){reference-type="eqref" reference="eq:secular-polynomial"}; adjoining the retained orthogonal spaces gives [\[eq:full-factor\]](#eq:full-factor){reference-type="eqref" reference="eq:full-factor"}.

\>0

# Strict interlacing and projective rate

Order the mutation poles as $d_L<\cdots<d_1<d_0=0$ and set $R(\lambda)=s\sum_kw_k/(\lambda-d_k)$. On every pole-free interval, $$\label{eq:derivative}
 R'(\lambda)=-s\sum_{k=0}^L\frac{w_k}{(\lambda-d_k)^2}<0.$$ At the left and right ends of each internal gap, $R$ has limits $+\infty$ and $-\infty$, respectively. Above $d_0$, it decreases from $+\infty$ to $0$; below $d_L$ it is negative.

[\[thm:gap\]]{#thm:gap label="thm:gap"} The $L+1$ secular roots $\rho_0>\rho_1>\cdots>\rho_L$ are simple and obey $$\label{eq:interlace}
 \rho_0>d_0=0>\rho_1>d_1>\rho_2>\cdots>d_{L-1}>\rho_L>d_L.$$ In particular, the two largest eigenvalues of the full $2^L$-dimensional matrix are $\rho_0$ and $\rho_1$. With $$\label{eq:gap}
 \Delta_L(U,s)=\rho_0-\rho_1,$$ every simplex orbit satisfies $p(t)-p_\infty=O(e^{-\Delta_Lt})$. This exponent is attained whenever the coefficient of the $\rho_1$ eigenvector in the projective expansion is nonzero.

Equation [\[eq:derivative\]](#eq:derivative){reference-type="eqref" reference="eq:derivative"} and the one-sided pole limits give exactly one root in every internal gap, one above $d_0$, and none below $d_L$. The retained eigenvalue nearest the top is $d_1<\rho_1$, so $\rho_1$ is the true second eigenvalue. Divide the real-symmetric spectral expansion in Theorem [\[thm:flow\]](#thm:flow){reference-type="ref" reference="thm:flow"} by its Perron term. All remaining exponents are at most $\rho_1-\rho_0$; a nonzero $\rho_1$ coefficient gives the stated leading term.

The phrase *strict secular interlacing* records the substantive Round-1 addition.

\>1

# Reducible faces and evidence boundary

If $s=0$, selection disappears and $d_k$ has its full multiplicity $m_k$; the mutation semigroup converges to the uniform law. If $U=0$, writing $a(t)=p_0(t)$ gives $\dot a=sa(1-a)$. Initial data with $a(0)>0$ converge to $e_0$, whereas the whole face $a(0)=0$ is stationary. Thus no irreducible Perron conclusion is smuggled onto that face. For $L=1$, no $d_k$ is retained and direct diagonalization gives $$\label{eq:l-one}
 \lambda_\pm=\frac{s-2U\pm\sqrt{s^2+4U^2}}2.$$

The exact evidence enumerates rational parameter fixtures, reconstructs the factorization independently, directly compares small hypercube matrices, counts secular roots symbolically, checks Walsh eigenvectors and quotient derivatives, and attacks signs, weights, multiplicities, scopes and parser conventions. These finite checks are regression receipts, not an extrapolation proof. At every fixed finite $L$ the strictly interlacing roots vary smoothly in the positive chamber; this paper makes no singular infinite-genome error- threshold claim.

# Ownership and Route-A boundary

Crow--Kimura mutation--selection theory and the permutation-invariant linear reduction are historical source owners. Nearby workspace packages treat the mutation-only Ehrenfest cube, Moran fixation, Wright--Fisher diffusion and network SIS; none contains the single-peak rank-one full spectrum proved here. The phrase *finite-length boundary and route firewall* records the substantive Round-2 addition.

The Hamming cube supplies neither rational-prime local data nor a logarithmic prime clock. This positive normalized flow has no isolated arithmetic primitive ledger, and [\[eq:full-factor\]](#eq:full-factor){reference-type="eqref" reference="eq:full-factor"} is a source characteristic polynomial, not a target Euler factor or divisor. Real symmetry gives only a formal source-operator hint. Under scope `NO_BAD_EULER_OR_ROOT_NUMBER`, the tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ The verdict is `ROUTE_A_REJECTED`; Route B is locked. No target arithmetic datum, Euler factor, root number, automorphy, target functional equation or zero match, or Hilbert--Polya operator is claimed.
