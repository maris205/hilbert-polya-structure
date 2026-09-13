---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mixed-lcg-hull-dobell-route-a"
canonical_tex: "henon_dynamics/henon_mixed_lcg_hull_dobell_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mixed_lcg_hull_dobell_route_a/paper/main.pdf"
source_sha256: "4d26c1ef45fc23c5bdff3013ef55c1a1e5159396aa5514ed28cd6931709ece0b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Full-Period Mixed Congruential Dynamics: A Prime-Power and CRT Classification

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mixed_lcg_hull_dobell_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mixed_lcg_hull_dobell_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mixed_lcg_hull_dobell_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mixed_lcg_hull_dobell_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every $m\ge2$ we classify the affine maps $F(x)=ax+c$ on $\mathbb Z/m\mathbb Z$ that form one cycle through all $m$ states. The criterion is proved on prime-power quotients and assembled by the Chinese remainder theorem (CRT). The resulting primitive ledger and fixed counts are exact. This finite-ring theorem uses no target spectral data.
author:
- 'Route-A source-local certificate HCS-C258'
date: 31 August 2026
title: |
  Full-Period Mixed Congruential Dynamics:\
  A Prime-Power and CRT Classification
```

## Markdown 正文

trailerid \[\<C2582026083100000000000000000000\>\<C2582026083100000000000000000000\>\]

# Frozen owner and full-period theorem

One application of $F$ is one unit of source time. Let $$L(m)=
 \begin{cases}
 \operatorname{lcm}(\operatorname{rad}m,4),&4\mid m,\\
 \operatorname{rad}m,&4\nmid m.
 \end{cases}$$

The map $F$ is one $m$-cycle if and only if $$(c,m)=1,\qquad p\mid a-1\quad(p\mid m),\qquad
 4\mid a-1\quad\hbox{when }4\mid m.                 \tag{1}$$ Exactly $\varphi(m)m/L(m)$ residue pairs $(a,c)$ satisfy (1).

The classical criterion is due to Hull and Dobell [@HD]; the proof below is included to freeze the precise convention used by the certificate.

# Necessity and sufficiency

If $F$ is transitive modulo $m$, every prime quotient is transitive. When $a\not\equiv1\pmod p$, the induced affine map has a fixed point (or is not a permutation), which excludes a $p$-cycle. Thus $a\equiv1\pmod p$ and $c\not\equiv0\pmod p$. If $4\mid m$ but $a\equiv3\pmod4$, then $F^2(x)=a^2x+c(a+1)\equiv x\pmod4$, excluding a four-cycle. This proves necessity.

For sufficiency, write $p^e\Vert m$ and $$S_n=1+a+\cdots+a^{n-1},\qquad
 F^n(x)-x=S_n\bigl((a-1)x+c\bigr).                   \tag{2}$$ The second factor is a $p$-adic unit. The standard lifting identity gives $v_p(S_n)=v_p(n)$ for odd $p$, and also for $p=2$ under the mod-four condition. The $e=1$ dyadic face follows directly from oddness. Hence every state has exact period $p^e$ modulo $p^e$. CRT gives exact period $\operatorname{lcm}_{p^e\Vert m}p^e=m$, so all states comprise one cycle. The congruences select $m/L(m)$ multipliers and $\varphi(m)$ increments.

# Local valuation and sharp failure faces

The local step can be made bidirectional. Since $d_x=(a-1)x+c$ is a unit at every $p\mid m$, equation (2) gives $$F^n(x)\equiv x\pmod {p^e}
 \quad\Longleftrightarrow\quad v_p(S_n)\ge e
 \quad\Longleftrightarrow\quad p^e\mid n.             \tag{3}$$ For odd $p$ this is the quotient of $v_p(a^n-1)=v_p(a-1)+v_p(n)$. For $p=2$ and $e\ge2$, $a\equiv1\pmod4$ gives the identical quotient; for $e=1$, the first increment is odd and the second return gap is even. Thus no earlier local return is hidden by the affine shift.

The three hypotheses are individually visible. If $p\mid(c,m)$, the translation on the $p$-quotient is not transitive. If $a\not\equiv1\pmod p$, that quotient has a fixed point or loses bijectivity. If $4\mid m$ and $a\equiv3\pmod4$, its square is the identity modulo four. The theorem does not claim a full cycle decomposition after a hypothesis fails.

# Primitive, zeta, and Koopman closure

For an admissible pair there is exactly one primitive orbit, of length $m$, and $$\#\operatorname{Fix}(F^n)=
 \begin{cases}m,&m\mid n,\\0,&m\nmid n.\end{cases}
 \qquad
 \zeta_F(t)=\exp\!\left(\sum_{n\ge1}
 \frac{\#\operatorname{Fix}(F^n)}n t^n\right)
 =\frac1{1-t^m}.                                    \tag{4}$$ The counting-measure Koopman operator is a unitary $m$-cycle permutation. Its eigenvalues are the $m$-th roots of unity once each, and $\det(uI-U_F)=u^m-1$.

The full-period theorem gives one $m$-cycle. Its $n$-th power fixes the whole cycle exactly at multiples of $m$, proving the fixed count. Substitution in the exponential definition gives $\exp(\sum_{k\ge1}t^{km}/k)=(1-t^m)^{-1}$. A cyclic permutation is unitary in the counting basis, and the discrete Fourier basis gives the stated spectrum.

This finite-ring affine owner differs from the repository's C172 primitive finite-field multiplication and C204 linear rational-canonical owner: translation, composite prime-power quotients, the mod-four exception, and the Hull--Dobell parameter chamber are essential here. Equation (4) remains a source zeta, not a target Fredholm determinant.

# Exact certificate and boundary

The producer and an independent implementation enumerate all $299{,}535$ affine pairs for $2\le m\le96$ with no criterion mismatch. Six complete cycle ledgers and odd/dyadic valuation controls are reconstructed exactly; finite enumeration is a regression oracle rather than the all-$m$ proof. The checker closes $300{,}210$ assertions, the symbolic implementation closes $69$ identities, byte replay is exact, and semantic mutation rejects $37/37$ repaired-hash changes.

The intrinsic prime-power structure supports only `A0_WEAK_ARITHMETIC_RELATION`. There is no rational-prime orbit dictionary, logarithmic prime clock, target divisor, or target analytic structure. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$\texttt{(A0\_WEAK\_ARITHMETIC\_RELATION,A1\_WEAK,A2\_FAIL,
A3\_FAIL,A4\_NATURAL\_QUANTIZATION)}.$$ The verdict is `ROUTE_A_EXPLORATORY`; Route B is disabled. The natural unitary earns only the source-local A4 coordinate: it does not repair the failed target determinant and analytic-structure gates.

9 T. E. Hull and A. R. Dobell, *Random number generators*, *SIAM Review* **4** (1962), 230--254, [doi:10.1137/1004061](https://doi.org/10.1137/1004061).
