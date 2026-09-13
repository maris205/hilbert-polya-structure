---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-inhomogeneous-coined-quantum-walk-route-a"
canonical_tex: "henon_dynamics/henon_inhomogeneous_coined_quantum_walk_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_inhomogeneous_coined_quantum_walk_route_a/paper/main.pdf"
source_sha256: "ee87678af8b68debc2b46b4924083028b0ce1d4a34eac1ed523817c4ddb49435"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Order-Sensitive Secular Determinants for an Inhomogeneous Coined Quantum Walk

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_inhomogeneous_coined_quantum_walk_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_inhomogeneous_coined_quantum_walk_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_inhomogeneous_coined_quantum_walk_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_inhomogeneous_coined_quantum_walk_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct a spatially inhomogeneous two-state coined quantum walk on a five-cycle. Rational reflection coins and a flip-flop shift give a source-derived real unitary $U=SC$ with involutive antiunitary reversal $\Theta=CK$. Its trace expansion retains signed primitive path amplitudes. Two coin arrangements with the same local population but different spatial order have distinct degree-ten secular polynomials; their difference factors exactly. Population averaging both erases this distinction and destroys unitarity. The result reaches a unitary Route-A subgate but makes no arithmetic or target spectral identification.
author:
- 'Hénon Route-A Working Series, C143'
date: 25 August 2026
title: |
  Order-Sensitive Secular Determinants\
  for an Inhomogeneous Coined Quantum Walk
```

## Markdown 正文

# Frozen coined dynamics

On $\mathcal H=\mathbb C^5\otimes\mathbb C^2$, order the basis as $(0,+),(0,-),\ldots,(4,+),(4,-)$. Freeze the real reflection coins $$C_0=\frac15\begin{pmatrix}3&4\\4&-3\end{pmatrix},\qquad
 C_1=\frac1{13}\begin{pmatrix}5&12\\12&-5\end{pmatrix}.$$ For a spatial word $w=w_0\cdots w_4$, let $C_w=\bigoplus_xC_{w_x}$. The flip-flop shift is $$S|x,+\rangle=|x+1,-\rangle,\qquad
 S|x,-\rangle=|x-1,+\rangle,$$ with positions modulo five. One coin-then-shift step is $U_w=SC_w$. This convention, clock, basis, and the determinant $D_w(z)=\det(I_{10}-zU_w)$ are fixed before comparison.

# Unitary and antiunitary structure

[\[thm:unitary\]]{#thm:unitary label="thm:unitary"} For every $w$, $U_w$ is real orthogonal. With $K$ denoting coefficientwise conjugation, the antiunitary $\Theta_w=C_wK$ obeys $$\Theta_w^2=I,\qquad
 \Theta_wU_w\Theta_w^{-1}=U_w^{-1}.$$ Moreover $P_w=|U_w|^2$ is doubly stochastic and has the same one-step support and clock.

Each displayed coin is real symmetric and squares to $I$; the real symmetric permutation $S$ also satisfies $S^2=I$. Therefore $U_w^*U_w=C_wSS C_w=I$. Since $K$ fixes both real matrices, $$(C_wK)^2=C_w^2=I,\qquad
 (C_wK)(SC_w)(KC_w)=C_wS=U_w^{-1}.$$ The row and column sums of squared moduli of a unitary are one.

This antiunitary is source-derived from the same local coin that defines the evolution; it is not added after examining the determinant. It reverses one discrete-time step on the same frozen spatial arrangement. It does not map a word to its spatial reflection, and the stochastic shadow is not asserted to be a unique classical antecedent.

# Signed primitive path ownership

A directed state path carries the product of the corresponding entries of $U_w$, including every sign. For a primitive cycle $p$, write its step clock as $\ell_p$ and signed amplitude as $A_p$.

[\[prop:product\]]{#prop:product label="prop:product"} For $|z|<5/7$, $$\label{eq:product}
 D_w(z)=\prod_{[p]}(1-A_pz^{\ell_p}),$$ where $[p]$ runs over primitive directed state cycles. The left side gives the global polynomial continuation; no raw-product convergence outside the displayed disk is asserted.

Expanding $-\log D_w(z)=\sum_{n\ge1}\operatorname{Tr}(U_w^n)z^n/n$ enumerates rooted closed paths with signed amplitudes. Primitive-root decomposition and cyclic invariance of an amplitude product give [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"}. Every column of $|U_w|$ has sum at most $7/5$, so the total absolute rooted-path mass is bounded by $10(7/5)^n$. This proves absolute convergence on the stated disk and justifies regrouping without discarding cancellations.

# Equal populations, different determinants

Compare $$w=00011,\qquad v=00101.$$ Both have population $(N_0,N_1)=(3,2)$, but they are not related by a cyclic rotation or a reflection followed by rotation: the two $1$ symbols are adjacent on the cycle for $w$ and nonadjacent for $v$, a dihedral invariant. Writing $D(z)=\sum_{k=0}^{10}d_kz^k$, exact Newton recursion $$kd_k=-\sum_{j=1}^{k}d_{k-j}\operatorname{Tr}(U^j),\qquad d_0=1,$$ gives $$\begin{aligned}
D_w(z)={}&1+\frac{5617}{4225}z^2+\frac{6798}{4225}z^4
-\frac{18432}{21125}z^5+\frac{6798}{4225}z^6
+\frac{5617}{4225}z^8+z^{10},\\
D_v(z)={}&1+\frac{417}{325}z^2+\frac{538}{325}z^4
-\frac{18432}{21125}z^5+\frac{538}{325}z^6
+\frac{417}{325}z^8+z^{10}.\end{aligned}$$ Consequently $$\label{eq:difference}
 D_w-D_v=\frac{196}{4225}z^2(z-1)^2(z+1)^2(z^2+1)\ne0.$$ Spatial coin order is therefore visible to the exact determinant.

Both polynomials are palindromic. Indeed, $S$ is a product of five transpositions and $C_w$ of five reflections, so $\det U_w=1$; real orthogonality then gives $D_w(z)=z^{10}D_w(1/z)$. This finite source symmetry is not a target functional equation.

# Why population averaging is invalid

The seemingly natural averaged coin is $$\overline C=\frac{3C_0+2C_1}{5}
 =\frac1{325}\begin{pmatrix}167&276\\276&-167\end{pmatrix}.$$ It satisfies $$\overline C^{T}\overline C-I=-\frac{24}{1625}I,\qquad
 \det\overline C=-\frac{1601}{1625}.$$ Thus averaging destroys unitarity as well as order. It is a negative control, not an alternative representation of either walk.

# Exact receipt and scope

For each arrangement the evidence reconstructs 12 traces and every signed rooted path through clock ten; at clock ten there are 1,270 rooted closed paths and 125 primitive cycles. The producer-independent checker makes 62 assertions, a separate SymPy route makes 39 exact checks, replay is byte-identical, and 29 repaired-hash plus one stale-hash mutations are rejected.

The strict verdict is $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
 \mathrm{A4\_UNITARY\_OR\_SCATTERING\_CANDIDATE}).$$ There is no target divisor, missing/extra-zero census, target counting law, prime correspondence, arithmetic local factor, Euler factor, root number, automorphy claim, or self-adjoint Hilbert--Pólya operator. The dimension is fixed and no growing-level limit, canonical logarithm of $U_w$, or self-adjoint spectral realization is claimed. Route B remains unauthorized under `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Conclusion

C143 shows that one source-derived discrete unitary can retain chronological spatial order, signed orbit amplitudes, and exact reversal simultaneously. Connecting this finite walk to any external target remains open.
