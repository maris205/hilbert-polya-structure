---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-four-block-marker-suspension-route-a"
canonical_tex: "henon_dynamics/henon_four_block_marker_suspension_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_four_block_marker_suspension_route_a/paper/main.pdf"
source_sha256: "359944eae1d852ab997908fa6cdaba79d5a559dffef4b696714599514e43c0d4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Minimal Four-Block Refinement of a Directed-Edge Nonlattice Suspension

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_four_block_marker_suspension_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_four_block_marker_suspension_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_four_block_marker_suspension_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_four_block_marker_suspension_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We add one cyclic four-block marker to a directed-edge roof on the full binary shift. An exact eight-state determinant owns the rooted trace and primitive product at every period. The primitive words $001011$ and $001101$ have the same cyclic block populations through width three, but different $0011$ counts; hence the frozen marker gives a coding-relative minimal forward-memory refinement. The improvement is deliberately limited: two primitive period- seven necklaces retain the same complete clock vector. This is an intrinsic symbolic-dynamical certificate, not a target or arithmetic factorization.
author:
- 'Route-A structural certificate C139'
title: |
  A Minimal Four-Block Refinement of a\
  Directed-Edge Nonlattice Suspension
```

## Markdown 正文

# Frozen suspension and exact determinant

Let $\Sigma=\{0,1\}^{\mathbb Z}$ with the left shift. Freeze $$\tau=\begin{pmatrix}1&\sqrt2\\ \sqrt3&\sqrt6\end{pmatrix},\qquad
r(x)=\tau_{x_0x_1}+\sqrt5\,\mathbf 1_{\{x_0x_1x_2x_3=0011\}},$$ and form the suspension by $(x,t+r(x))\sim(\sigma x,t)$. On the ordered three-block states $000,001,\ldots,111$, define $$M_{abc,bcd}(x,y)=x_{ab}y^{\mathbf 1_{\{abcd=0011\}}},\qquad d\in\{0,1\}.
\tag{1}$$ All other entries vanish. Direct sparse expansion gives $$\Delta_{139}(x,y)=\det(I-M)
=1-x_{00}-x_{11}-x_{01}x_{10}+x_{00}x_{11}
+(1-y)x_{00}x_{01}x_{10}x_{11}.                 \tag{2}$$ At $y=1$, this is exactly the two-state directed-edge determinant. Indeed, the map sending a cyclic word $w$ to the states $w_jw_{j+1}w_{j+2}$ is a bijection of closed paths and preserves edge weights. The presentations therefore have equal traces in every positive power; the formal log-determinant identity and constant term one give $\det(I-M(x,1))=1-x_{00}-x_{11}+x_{00}x_{11}-x_{01}x_{10}$. Only $(I-M)_{001,011}=-x_{00}y$ depends on $y$, so the determinant is affine. Put $a=x_{00},b=x_{01},c=x_{10},d=x_{11}$. Laplace expansion of its cofactor minor in the first two columns gives $(-c)\det Q$, where $$Q=\begin{pmatrix}
1&-b&-b&0&0\\0&0&0&-b&-b\\-c&0&1&0&0\\
0&-d&-d&1&0\\0&0&0&-d&1-d
\end{pmatrix}.$$ Adding $c$ times the first row to the third and expanding gives $\det Q=-bd$. The cofactor is therefore $bcd$, and $\partial_y\Delta=-x_{00}x_{01}x_{10}x_{11}$ and integration from $y=1$ proves (2), including its sign.

# All-period product and clock sectors

For every $n\geq1$, closed state paths in (1) are bijective with rooted cyclic binary words. Matrix multiplication therefore proves $$\operatorname{Tr}M(x,y)^n
=\sum_{|w|=n}y^{N_{0011}(w)}\prod_{a,b}x_{ab}^{N_{ab}(w)}. \tag{3}$$ In the total-transition-degree completion, $-\log\det(I-M)=\sum_{n\geq1}\operatorname{Tr}(M^n)/n$. Grouping each rooted word by its unique primitive root gives the cutoff-free identity $$\Delta_{139}(x,y)=\prod_{[\gamma]\ \mathrm{primitive}}
\left(1-y^{N_{0011}(\gamma)}\prod_{a,b}x_{ab}^{N_{ab}(\gamma)}\right).
\tag{4}$$ Every coefficient is a finite regrouping because only finitely many necklaces have a fixed total degree.

With $x_{ab}=z e^{-s\tau_{ab}}$ and $y=e^{-\sqrt5s}$, (4) becomes $$\Delta_{139}(z,s)=\prod_{[\gamma]}
\left(1-z^{|\gamma|}e^{-s\ell(\gamma)}\right),
\quad
\ell=N_{00}+\sqrt2N_{01}+\sqrt3N_{10}+\sqrt6N_{11}+\sqrt5N_{0011}.$$ The identity is formal in $z$. It is also absolutely convergent wherever the entrywise absolute-value matrix has spectral radius below one, because its trace logarithm then is dominated by the corresponding nonnegative matrix series.

The five displayed clock numbers are rationally independent. Sign changes of $\sqrt2$ and $\sqrt3$ isolate the first four coefficients. If $\sqrt5$ lay in $K=\mathbb Q(\sqrt2,\sqrt3)$, its four conjugates would be only $\pm\sqrt5$, so a nontrivial automorphism would fix it. It would then lie in one of $\mathbb Q(\sqrt2)$, $\mathbb Q(\sqrt3)$, or $\mathbb Q(\sqrt6)$. Squaring $\sqrt5=a+b\sqrt m$ forces $2ab=0$ and gives an immediate contradiction for $m\in\{2,3,6\}$. Thus equal times force equal complete feature vectors. The fixed cycles $[0]$ and $[1]$ have lengths $1$ and $\sqrt6$, so the roof is nonlattice.

# The minimal-memory advance

For a forward roof depending on $k$ consecutive symbols, its periodic sum is the dot product of its values with the cyclic $k$-block population. The two primitive words below have the exact counts

  word         $k=1$    $k=2$ in order $00,01,10,11$   $N_{0011}$
  ---------- --------- ------------------------------ ------------
  $001011$    $(3,3)$           $(1,2,2,1)$               $0$
  $001101$    $(3,3)$           $(1,2,2,1)$               $1$

Their common $k=3$ vector, in lexicographic order, is $(0,1,1,1,1,1,1,0)$. Therefore no forward roof of memory at most three separates their periodic sums. The frozen four-block roof does: $$\ell(001101)-\ell(001011)=\sqrt5\ne0.             \tag{5}$$ Any nontrivial period of a length-six word is $1$, $2$, or $3$; neither word is a repetition of the corresponding prefix. They are primitive, and their different cyclic marker counts exclude a rotation. This is minimality relative to the frozen forward binary coding; it is not claimed to survive arbitrary recoding or roof cohomology.

# Residual collision, validation, and boundary

The primitive words $0101111$ and $0110111$ are not cyclic rotations, yet both have feature vector $$(N_{00},N_{01},N_{10},N_{11},N_{0011})=(0,2,2,3,0).$$ Thus the new clock is not orbit injective. Exact replay through period twelve contains 8,190 rooted words, 747 primitive cycles, 258 rooted feature cells, and 229 primitive feature cells; it locates the first such collision at period seven but is not used to prove (2)--(4). The independent checker passes 16,467 assertions, SymPy passes 35 checks, byte replay passes, and all 49 hostile cases (48 repaired-hash and one stale-hash) are rejected.

The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_FAIL})$, overall `ROUTE_A_EXPLORATORY`. We claim no target divisor, target functional equation or counting law, arithmetic/local factor, Euler factor, root number, automorphy, natural self-adjoint or unitary lift, Hilbert--Pólya operator, or Route-B authorization. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
