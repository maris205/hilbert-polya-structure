---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-heisenberg-primary-quadratic-module-route-a"
canonical_tex: "henon_dynamics/henon_heisenberg_primary_quadratic_module_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_heisenberg_primary_quadratic_module_route_a/paper/main.pdf"
source_sha256: "a81ea34bdd455ae4005a9bfa722c5962839c35e333a8e1ef5412169d85ea70aa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Primary Quadratic Modules for Heisenberg Fixed Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_heisenberg_primary_quadratic_module_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_heisenberg_primary_quadratic_module_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_heisenberg_primary_quadratic_module_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_heisenberg_primary_quadratic_module_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a frozen Heisenberg lattice automorphism we determine the Smith type of every horizontal fixed-class group, reduce the universal central-rotation denominator to its group exponent, and split the resulting quadratic function into orthogonal primary components. Exact component ledgers through iterate fourteen turn the clean fixed-circle count into a product of primary zero counts. Primary is finite-group terminology here, not an arithmetic factorization.
author:
- 'Route-A structural certificate C156'
title: Primary Quadratic Modules for Heisenberg Fixed Fibres
```

## Markdown 正文

suppressoptionalinfo 512 trailerid

**Keywords:** Heisenberg nilmanifold; finite quadratic module; Smith normal form; primary decomposition; fixed fibres; exact verification.

# Smith form and the exponent bound

Let $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$, $B=A^n$, and $M=B-I$. With $F_n,L_n$ denoting Fibonacci and Lucas numbers, the standard doubling and Cassini identities give $$M=\begin{cases}
L_n\left(\begin{smallmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{smallmatrix}\right),&n\ \text{odd},\\[2pt]
F_n\left(\begin{smallmatrix}L_{n+1}&L_n\\L_n&L_{n-1}\end{smallmatrix}\right),&n\ \text{even}.
\end{cases}                                                     \tag{1}$$ The cofactors have determinants $-1$ and $-5$, respectively; the latter has content one for even $n$. Consequently $$G_n=\mathbb Z^2/M\mathbb Z^2\cong
\begin{cases}(\mathbb Z/L_n\mathbb Z)^2,&n\text{ odd},\\
\mathbb Z/F_n\mathbb Z\times\mathbb Z/(5F_n)\mathbb Z,&n\text{ even}.
\end{cases}                                                     \tag{2}$$ Its exponent is $h_n=L_n$ for odd $n$ and $h_n=5F_n$ for even $n$.

For $B=(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})$, the canonical lattice correction is $$q_B(x,y)=\frac{ac}{2}x(x-1)+bcxy+\frac{bd}{2}y(y-1).             \tag{3}$$ The polarization of (3) is $(Bv)_1(Bw)_2-v_1w_2$. The actual iterate correction has the same polarization, so $q_n=q_{A^n}+\ell_n$ with $\ell_n$ integer linear. This drift cannot be dropped when zero levels are counted. For $m=Mv$, define $\rho_n([m])=q_n(v)-m_1v_2\pmod1$.

Here is the parity step behind the improved denominator. Write $M=gU$, $U=(\begin{smallmatrix}r&s\\s&t\end{smallmatrix})$, where $(g,\det U,h)=(L_n,-1,L_n)$ in the odd branch and $(F_n,-5,5F_n)$ in the even branch. By (2), $W=hv=(X,Y)$ is integral. Formula (3) gives $$N:=2h\{q_{A^n}(v)-m_1v_2\}
=X(m_2-ac)-Y(m_1+bd)+hm_1m_2\in\mathbb Z.        \tag{4}$$ Modulo two, division by five in the even branch is harmless. Substitution of $B=I+gU$ reduces (4) to $$N\equiv s(gr+1)(g+1)X+s(gt+1)(g+1)Y
 +\{g(rt+s^2)+r+t\}XY.                           \tag{5}$$ Both Fibonacci and Lucas numbers have parity period $0,1,1$. If $3\mid n$, then $g=s=0$ and $r=t=1$; otherwise $g=1$, $rt+s^2=1$, and $r+t=1$. Thus (5) vanishes. Since $h\ell_n(v)$ is also integral, this proves $$h_n\rho_n([m])=0\quad\text{in }\mathbb Q/\mathbb Z.             \tag{6}$$ This is an all-iterate divisibility result. Equality of the observed denominator with $h_n$ is recorded only for $2\le n\le14$.

# Orthogonal primary decomposition

If $u=Mw$, direct expansion gives the bilinear polarization $$\beta_n([m],[u])=v_1u_2-u_1v_2+m_1u_2\pmod1.                   \tag{7}$$ Thus primary components of $G_n$ at distinct primes are orthogonal, and the restriction to a component of exponent $p^e$ takes values in $p^{-e}\mathbb Z/\mathbb Z$. Uniqueness of primary torsion in $\mathbb Q/\mathbb Z$ gives $$C_n=\prod_{p\mid h_n}C_{n,p},\qquad
C_{n,p}=\frac1{p^e}\sum_{a\bmod p^e}\sum_{x\in G_{n,p}}
e^{2\pi i a\rho_n(x)}.                                         \tag{8}$$ Indeed, bilinearity kills cross-prime polarizations. The identity $\rho(kx)=k\rho(x)+\binom{k}{2}\beta(x,x)$ makes each odd-primary value $p$-primary; for $p=2$, (6) removes the possible extra factor two. The formula is a finite root-of-unity zero projector, not an operator trace formula or an arithmetic local factor.

# Exact certificate and boundary

CRT idempotents applied to the two standard generators, followed by column Hermite reduction, enumerate each primary component exactly. The counts are $$\begin{array}{c|rrrrrrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\ \hline
C_n&1&1&4&1&21&4&57&1&148&105&397&144&1041&57
\end{array}$$ For example, the $2$-, $3$-, and $5$-primary zero counts at $n=12$ are $16,9,1$, while the $5$-, $13$-, and $29$-primary counts at $n=14$ are $1,1,57$; their products give $144$ and $57$. The producer, direct-cocycle checker, and SymPy path independently verify the ledger. The strict tuple is $(\texttt{A1\_FAIL},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT})$. Fixed sets remain clean circles and the ordinary isolated stability factor remains singular. We claim no isolated primitive-orbit determinant, target divisor, target functional equation or counting law, arithmetic local/Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data availability.** All claim-bearing data are the exact JSON evidence and scripts distributed in this C156 package. No external dataset is used. **Ethics.** The work uses no human participants, animals, or sensitive personal data. **Author contributions/CRediT.** This is an anonymous technical certificate with no individual authorship assignment; package provenance records the roles Conceptualization, Formal analysis, Software, Validation, and Writing. **Competing interests.** None known. **Funding.** No external funding is reported. **AI-use disclosure.** An AI coding assistant supported drafting, proof-check planning, and code review. Every quantitative statement is regenerated and independently checked by the packaged scripts; the assistant was not treated as an external peer reviewer.
