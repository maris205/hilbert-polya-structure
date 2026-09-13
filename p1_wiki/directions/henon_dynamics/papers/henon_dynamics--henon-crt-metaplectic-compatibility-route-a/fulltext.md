---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-crt-metaplectic-compatibility-route-a"
canonical_tex: "henon_dynamics/henon_crt_metaplectic_compatibility_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_crt_metaplectic_compatibility_route_a/paper/main.pdf"
source_sha256: "3b4048dad1ae7f7d0f94cd4fcf1d8d9cbb62b85093336827a5638d513ddf718e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact CRT and Antiunitary Coherence for an Odd-Level Metaplectic Hénon Family

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_crt_metaplectic_compatibility_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_crt_metaplectic_compatibility_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_crt_metaplectic_compatibility_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_crt_metaplectic_compatibility_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The odd-level quantization of the toral Hénon matrix $A=\left(\begin{smallmatrix}3&-1\\1&0\end{smallmatrix}\right)$ is defined separately at every odd modulus, but a per-level theorem does not fix its cross-level phases. We enlarge the family by a unit additive-character parameter and prove exact Chinese-remainder tensor identities for the Weyl, Fourier, chirp, and evolution operators at every pair of coprime odd levels. The same generalized family has a canonical antiunitary involution that reverses evolution, swaps Weyl coordinates, and factors under CRT. The induced local characters contain inverse cofactor scalings. For fixed ordered leaves, iteration is independent of binary split schedule and parenthesization. Exact certificates cover 1,131,414 modular cases. At levels $3$ and $5$, the naive tensor of the standard local characters has exponent $8$ rather than $1$ modulo $15$; more generally, the canonical standard-character unitary tensor cannot be repaired by an overall scalar. The result is a cross-level quantization theorem, not a target spectral or arithmetic claim.
author:
- 'Hénon Route-A Working Series, C136'
date: 24 August 2026
title: 'Exact CRT and Antiunitary Coherence for an Odd-Level Metaplectic Hénon Family'
```

## Markdown 正文

# Progress over the per-level gate

For an odd $r\ge3$, write $\omega_r=e^{2\pi i/r}$ and let $h_r=2^{-1}\pmod r$. The earlier per-level family used $$Q_r|x\rangle=\omega_r^x|x\rangle,\qquad
 P_r|x\rangle=|x+1\rangle,$$ $$W_r(q,p)=\omega_r^{-h_rqp}Q_r^qP_r^p,\quad
 (\mathcal F_r)_{xy}=r^{-1/2}\omega_r^{xy},\quad
 (C_r)_{xx}=\omega_r^{3h_rx^2},\quad U_r=C_r\mathcal F_r^{-1}.$$ It gives exact Egorov covariance at each odd level. That theorem deliberately left cross-level projective compatibility open. The unresolved question is whether the canonical residue-basis identification at a product level respects the frozen phases. Dimension counting alone cannot answer it: the global primitive character need not restrict to the standard primitive characters on the factors.

# Generalized additive characters

Let $c\in(\mathbb Z/r\mathbb Z)^\times$. Define $$W_{r,c}(q,p)=\omega_r^{-ch_rqp}Q_r^{cq}P_r^p,$$ $$(\mathcal F_{r,c})_{xy}=r^{-1/2}\omega_r^{cxy},\qquad
 (C_{r,c})_{xx}=\omega_r^{3ch_rx^2},\qquad
 U_{r,c}=C_{r,c}\mathcal F_{r,c}^{-1}.$$ Let $K_r$ denote coefficientwise conjugation in the standard residue basis and define the antiunitary $$\Theta_{r,c}=\mathcal F_{r,c}K_r.$$ The original family is the fiber $c=1$.

[\[prop:egorov\]]{#prop:egorov label="prop:egorov"} For every odd $r\ge3$ and unit $c$, $U_{r,c}$ is unitary and $$U_{r,c}W_{r,c}(q,p)U_{r,c}^{-1}=W_{r,c}(3q-p,q).$$ Thus one quantum step still implements one application of $A$.

The root $\omega_r^c$ is primitive, so finite Fourier orthogonality proves that $\mathcal F_{r,c}$ is unitary. The chirp is diagonal unitary. Direct generator conjugation gives $\mathcal F_{r,c}^{-1}Q_r^c\mathcal F_{r,c}=P_r$ and $\mathcal F_{r,c}^{-1}P_r\mathcal F_{r,c}=Q_r^{-c}$. After chirp conjugation these become $W_{r,c}(3,1)$ and $W_{r,c}(-1,0)$. The symmetric half-phases cancel in a general Weyl product, giving the displayed identity without a scalar.

[\[thm:antiunitary\]]{#thm:antiunitary label="thm:antiunitary"} For every odd $r\ge3$, unit $c$, and $(q,p)\in(\mathbb Z/r\mathbb Z)^2$, $$\Theta_{r,c}^2=I,\qquad
 \Theta_{r,c}U_{r,c}\Theta_{r,c}^{-1}=U_{r,c}^{-1},\qquad
 \Theta_{r,c}W_{r,c}(q,p)\Theta_{r,c}^{-1}=W_{r,c}(p,q).$$

Coefficientwise conjugation gives $\overline{\mathcal F_{r,c}}=\mathcal F_{r,c}^{-1}$ and $\overline{C_{r,c}}=C_{r,c}^{-1}$, hence $\Theta_{r,c}^2=\mathcal F_{r,c}\overline{\mathcal F_{r,c}}=I$. Since $\overline{U_{r,c}}=C_{r,c}^{-1}\mathcal F_{r,c}$, $$\Theta_{r,c}U_{r,c}\Theta_{r,c}^{-1}
 =\mathcal F_{r,c}\overline{U_{r,c}}\mathcal F_{r,c}^{-1}
 =\mathcal F_{r,c}C_{r,c}^{-1}=U_{r,c}^{-1}.$$ Moreover $K_rW_{r,c}(q,p)K_r=W_{r,c}(-q,p)$, while $\mathcal F_{r,c}Q_r^{ca}\mathcal F_{r,c}^{-1}=P_r^{-a}$ and $\mathcal F_{r,c}P_r^b\mathcal F_{r,c}^{-1}=Q_r^{cb}$. Thus $$\mathcal F_{r,c}W_{r,c}(-q,p)\mathcal F_{r,c}^{-1}
 =\omega_r^{ch_rqp}P_r^qQ_r^{cp}=W_{r,c}(p,q),$$ using $P_r^qQ_r^{cp}=\omega_r^{-cpq}Q_r^{cp}P_r^q$ and $h_r-1=-h_r\pmod r$.

# Exact two-factor CRT identity

Let $M,N>1$ be coprime odd integers and $L=MN$. Put $$a=N^{-1}\pmod M,\qquad b=M^{-1}\pmod N,$$ and, for a unit $c\pmod L$, $$c_M=(c\bmod M)a\pmod M,\qquad
 c_N=(c\bmod N)b\pmod N.$$ The canonical unitary is $$J_{M,N}|x\bmod L\rangle
 =|x\bmod M\rangle\otimes|x\bmod N\rangle.$$

The inverse coefficients are forced by the global character, rather than chosen to make the theorem true. Indeed, for residues $x_M,x_N,y_M,y_N$, $$\label{eq:phase-split}
 \frac{cxy}{MN}\equiv
 \frac{c_Mx_My_M}{M}+\frac{c_Nx_Ny_N}{N}\pmod1.$$

[\[thm:crt\]]{#thm:crt label="thm:crt"} Under this identification, $$\begin{aligned}
 J\mathcal F_{L,c}J^{-1}&=\mathcal F_{M,c_M}\otimes\mathcal F_{N,c_N},&
 JC_{L,c}J^{-1}&=C_{M,c_M}\otimes C_{N,c_N},\\
 JW_{L,c}(q,p)J^{-1}&=W_{M,c_M}(q_M,p_M)\otimes
 W_{N,c_N}(q_N,p_N),&
 JU_{L,c}J^{-1}&=U_{M,c_M}\otimes U_{N,c_N}.\end{aligned}$$ All four linear identities are exact. In addition, $$J\Theta_{L,c}J^{-1}
 =\Theta_{M,c_M}\mathbin{\widehat{\otimes}}\Theta_{N,c_N}.$$ Here $\mathbin{\widehat{\otimes}}$ denotes the canonical conjugate-linear product map in the ordered residue bases: define it on pure tensors by sending $v\otimes w$ to $\Theta_{M,c_M}v\otimes\Theta_{N,c_N}w$, then extend conjugate-linearly to the full tensor product.

The CRT idempotents $e_M=Na$ and $e_N=Mb$ reconstruct $x=e_Mx_M+e_Nx_N\pmod L$. Their cross product vanishes modulo $L$, and $$\frac{xy}{L}\equiv\frac{a x_My_M}{M}+\frac{b x_Ny_N}{N}\pmod1.$$ Multiplication by $c$ proves [\[eq:phase-split\]](#eq:phase-split){reference-type="eqref" reference="eq:phase-split"}. Since $h_L$ reduces to $h_M$ and $h_N$, the same calculation factors the chirp and the symmetric Weyl phase. More explicitly, $$JQ_L^{cq}J^{-1}=Q_M^{c_Mq_M}\otimes Q_N^{c_Nq_N},\qquad
 JP_L^pJ^{-1}=P_M^{p_M}\otimes P_N^{p_N}.$$ The exponent $cq$ in the first identity is essential. Shifting by $p$ moves both residue coordinates, so the prefactor and monomial action of the Weyl operator factor together. These facts give the first three identities entry by entry; multiplying the chirp and inverse Fourier identities gives the fourth. Finally, $L^{-1/2}=M^{-1/2}N^{-1/2}$ with positive roots, so no normalization phase is left over. Finally $J$ is a real basis permutation, so it intertwines $K_L$ with coefficientwise conjugation in the ordered product basis. Combining this with the Fourier identity proves the antiunitary factorization.

# Finite-factor coherence

Fix an ordered list $r_1,\ldots,r_k>1$ of pairwise coprime odd levels and put $L=\prod_jr_j$. For a unit $c\pmod L$, define $$c_j=(c\bmod r_j)(L/r_j)^{-1}\pmod{r_j}.$$

[\[thm:coherence\]]{#thm:coherence label="thm:coherence"} Under the canonical residue-basis identification, $$J U_{L,c}J^{-1}=\bigotimes_{j=1}^k U_{r_j,c_j}.$$ The analogous ordered-basis antiunitary identity also holds. For these fixed ordered leaves, the local characters and both operator identities are independent of the binary split schedule and parenthesization used to construct the CRT map, after canonical tensor associators. No factor-permutation or symmetric-monoidal coherence is claimed.

Apply Theorem [\[thm:crt\]](#thm:crt){reference-type="ref" reference="thm:crt"} recursively. If $L=RS$ and $r_j\mid R$, the first split contributes $S^{-1}$ and the split inside $R$ contributes $(R/r_j)^{-1}$. Their product is $(L/r_j)^{-1}\pmod{r_j}$. Induction gives the direct coefficient above for every bracketing, and both the linear and antiunitary identities compose exactly. No induction step permutes the leaves.

The word "coherence" here has a deliberately narrow meaning: the objects are the generalized fibers $(\mathcal H_r,U_{r,c})$, and every arrow is the canonical residue-basis CRT map. The theorem neither chooses intertwiners from an induced character back to $c=1$ nor asserts that such choices would obey an associativity law; it also does not compare reordered factor lists.

# The standard-character obstruction

The exact theorem belongs to the induced-character family. It cannot be silently rewritten using the standard $c=1$ fiber at each factor.

[\[prop:obstruction\]]{#prop:obstruction label="prop:obstruction"} For nontrivial coprime odd $M,N$, there is no scalar $\zeta$ such that $$J_{M,N}U_{MN,1}J_{M,N}^{-1}
 =\zeta\,(U_{M,1}\otimes U_{N,1}).$$

In CRT coordinates, every entry of the output row $(x_M,x_N)=(0,0)$ equals $(MN)^{-1/2}$ for both kernels, so $\zeta=1$. Let $a=N^{-1}\pmod M$. In output row $(1,0)$, the ratio of input column $(1,0)$ to column $(0,0)$ is $\omega_M^{-a}$ for the induced kernel and $\omega_M^{-1}$ for the standard kernel. Equality forces $a=1\pmod M$. The analogous ratio at the $N$ factor forces $b=M^{-1}=1\pmod N$. These congruences would require both $N=1\pmod M$ and $M=1\pmod N$, which is impossible for $M,N>1$.

At $(M,N)=(3,5)$ one has $a=b=2$. The smallest Fourier control is $$\begin{array}{c|ccc}
&\text{global level }15&\text{naive }c=1\text{ tensor}&\text{induced tensor}\\\hline
\text{exponent at }x=y=1&1&5+3=8&5\cdot2+3\cdot2=16\equiv1
\end{array}$$ modulo $15$. This entry-level discrepancy is consistent with the universal unitary obstruction and catches an omitted inverse immediately.

# Certificate and Route-A boundary

The deterministic receipt exhausts eight two-factor and four three-factor systems: 13,520 Fourier, 306 chirp, 13,520 unitary, 658,314 Weyl, and 381,672 three-factor unitary cases. Antiunitary ledgers add 64,082 cases spanning conjugation bases, CRT kernels, involution, evolution reversal, and Weyl swap. A four-factor system compares left, right, and balanced bracketings. These are replay sentinels, not the basis of the universal quantifier, which follows from the idempotent proof. An independent implementation reconstructs all 1,131,414 cases and closes the schema without importing the producer; a symbolic path adds 96,449 congruence checks, and all 83 checksum-repaired plus one stale-checksum mutation are rejected.

The controls distinguish three separate boundaries. For $(M,N)=(5,7)$, using raw residues in place of inverses changes the test exponent from $1$ to $4$ modulo $35$. The pair $(3,9)$ is excluded because its residue map is not a product-ring bijection. At level $4$, the inverse of two does not exist, so the literal half-phase convention is unavailable.

The last control is not a no-go theorem for doubled-phase or other even-level Weil conventions. Likewise, Proposition [\[prop:obstruction\]](#prop:obstruction){reference-type="ref" reference="prop:obstruction"} concerns the canonical CRT identification; it is not a classification of every possible local Clifford correction. No correction back to standard local characters, factor-permutation theorem, noncoprime replacement, semiclassical trace match, target divisor, Euler factor, root number, automorphy, or Hilbert--Pólya operator is asserted.

The strict Route-A tuple is $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_NATURAL\_QUANTIZATION}),$$ and Route B is unauthorized.

# Conclusion

Inverse-scaled characters give an exact CRT tensor family with its one-step clock and a CRT-compatible antiunitary reversal. This closes C131's cross-level gate while the canonical standard-character shortcut fails. Whether natural local intertwiners remove the induced twists remains a separate problem.
