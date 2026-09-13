---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-luroth-meromorphic-hardy-route-a"
canonical_tex: "henon_dynamics/henon_luroth_meromorphic_hardy_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_luroth_meromorphic_hardy_route_a/paper/main.pdf"
source_sha256: "5f1da48fccafec1c4436a1bce403f2d7265f342045e2d015acd5538d1f6351e8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Meromorphic Hardy Family for Lüroth Dynamics: \ifcase\CRevisionRound Complete Spectrum and Periodic Traces \or Whole-Plane Continuation and Finite-Rank Residues \else Determinant-Invisible Poles and an Exact Divisor Obstruction\fi

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_luroth_meromorphic_hardy_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_luroth_meromorphic_hardy_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_luroth_meromorphic_hardy_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_luroth_meromorphic_hardy_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The countably branched Lüroth map admits a concrete trace-class transfer family on the Hardy space of the disk of radius two. We determine its complete nonzero spectrum, including algebraic multiplicities, and identify the Fredholm determinant with an absolutely convergent primitive stability product in its correct two-variable domain. Explicit trace-norm tails justify the passage from polynomial sections to the infinite-dimensional operator. \>0 A centered branch parameter continues this family meromorphically to the whole complex plane. Its Taylor coefficients give finite-rank residues at every half-integer at or below one half. \>1 The residues at nonpositive integers are nonzero and square to zero, although the determinant is holomorphic there. At the remaining poles the frozen determinant has exactly increasing pole orders, which no zero-free entire normalization removes. Finite exact matrices, complete small-word itineraries and independent symbolic calculations audit the formulas, not the infinite quantifiers. The result distinguishes source dynamics, analytic continuation and determinant visibility. It neither identifies rational primes with periodic trajectories nor asserts a target spectral correspondence.
author:
- 'HCS-C392 theorem and reproducibility package'
date: 5 September 2026
title: |
  A Meromorphic Hardy Family for Lüroth Dynamics:\
  Complete Spectrum and Periodic Traces Whole-Plane Continuation and Finite-Rank Residues Determinant-Invisible Poles and an Exact Divisor Obstruction
```

## Markdown 正文

**Keywords:** Lüroth map; Hardy space; trace class; meromorphic family; nilpotent residue; dynamical determinant.

chinese-simplified

中文摘要

本文为可数分支的吕罗映射指定具体的 [Hardy]{lang="en"} 空间，证明转移算子的迹类性质， 给出完整非零谱、代数重数和本原轨道稳定性乘积，并保留有限截断误差。 \>0 利用分支参数的中心展开，将算子族亚纯延拓至整个复平面，逐点确定有限秩留数。 \>1 非正整数处的留数非零且平方为零，但行列式在这些位置解析；其余半整数位置 仍具有精确递增的极点阶数，不能用无零点整函数因子消除。 独立精确复算和符号计算只用于验证公式与规范，不替代无限维证明。 源系统的解析对象与目标算术谱之间仍有明确边界。

关键词：吕罗映射；[Hardy]{lang="en"}空间；迹类算子；亚纯延拓；幂零留数；动力学行列式。

# From a scalar word identity to an operator

The scalar weight sum of a full shift does not by itself determine which Hilbert space owns its spectrum or which parameter singularities are visible to a determinant. We address those questions for $$a_n=\frac1{n(n+1)},\quad b_n=\frac1{n+1},\quad
 h_n(z)=b_n+a_nz,\qquad n\ge1.$$ The positive real source is $T(x)=n(n+1)x-n$ on $(1/(n+1),1/n]$, with the separate convention $T(0)=0$. Each $h_n$ maps $(0,1]$ into its specified half-open interval. The isolated fixed point zero has no branch-derivative weight and is excluded from the operator. This is an explicit source component, not a missing orbit.

Lüroth expansions and their generalized ergodic systems have classical owners [@bbdk]. The general holomorphic trace and determinant framework is due to Ruelle and Mayer; Bandtlow--Jenkinson [@bj], Theorem 4.2, establish a broad function-space version. We prove the required one-dimensional trace-class statements directly. Within this project, C241 already supplied positive periodic coding and the scalar word identity. The present object adds the infinite operator and its parameter singularities; neither a finite triangular matrix nor the word sum alone supplies that conclusion. We make no certified literature-priority assertion.

Put $H=H^2(D_2)$ with normalized boundary measure and orthonormal basis $e_j(z)=(z/2)^j$. For $\operatorname{Re}s>1/2$ define $$\label{family}
 L_sf=\sum_{n\ge1}a_n^sf\circ h_n,\qquad A(s)=\sum_{n\ge1}a_n^s .$$ All powers use the real logarithm of $a_n$; $s$ is an inverse-derivative exponent, not map time. The clock remains one application of $T$.

# Full spectrum with a trace-norm tail

[\[spectrum\]]{#spectrum label="spectrum"} The family [\[family\]](#family){reference-type="eqref" reference="family"} is holomorphic with values in trace-class operators. If $P_J$ projects onto degrees below $J$, then $$\|L_s-L_sP_J\|_1\le4A(\operatorname{Re}s)(3/4)^J.$$ Its complete nonzero eigenvalue list, counted algebraically, is $\{A(s+j):j\ge0,\ A(s+j)\ne0\}$. Its determinant is entire in $u$ and equals $$\label{det}
 D(u,s)=\det(I-uL_s)=\prod_{j\ge0}(1-uA(s+j)).$$

For $|z|\le2$, $$|h_n(z)|/2\le(n+2)/(2n(n+1))\le3/4.$$ The expansion $C_{h_n}f=\sum_{j\ge0}\langle f,e_j\rangle e_j\circ h_n$ is a sum of rank-one operators with norms at most $(3/4)^j$. Thus $\|C_{h_n}\|_1\le4$ and $\|L_s\|_1\le4A(\operatorname{Re}s)$. Uniform convergence on compact right-half-plane sets, also after $s$ derivatives, proves holomorphy and the displayed tail. Affineness gives $\operatorname{ran}(L_sP_J)\subset P_JH$. Its polynomial matrix is triangular with diagonal $A(s+j)$ for $j<J$. Continuity of Fredholm determinants in trace norm proves [\[det\]](#det){reference-type="eqref" reference="det"}. The spectral zero theorem for a trace-class determinant then proves completeness and algebraic multiplicity; a merely formal diagonal does not.

Since $|A(s+j)|\le2^{-j}A(\operatorname{Re}s)$, $$\label{tail}
 \left|\prod_{j\ge J}(1-uA(s+j))-1\right|
 \le \exp\!\left(2^{1-J}|u|A(\operatorname{Re}s)\right)-1 .$$ For real $s>1/2$ the eigenvalues are strictly decreasing, positive and simple. For complex $s$ collisions may occur; we claim no absence of Jordan chains. Nor do polynomial eigenvectors automatically form a Riesz basis. Zero is in the spectrum by compactness on the infinite-dimensional space.

# Every periodic word and the two products

For a word $w=(n_1,\ldots,n_r)$, write $h_w=h_{n_1}\circ\cdots\circ h_{n_r}=a_wz+b_w$. It maps $[0,1]$ into $(0,1]$, is a strict contraction, and has the unique fixed point $x_w=b_w/(1-a_w)$. The inverse-branch inclusions prove its full itinerary without any endpoint extrapolation. Cyclic rotations give the same oriented cycle; a primitive word has no shorter repetition. The forward multiplier is $a_w^{-1}$, and a repeated primitive cycle has inverse multiplier $a_\gamma^k$. Reversing a word preserves its slope but generally changes its point.

The triangular diagonal of $C_{h_w}$ gives $\operatorname{tr}C_{h_w}=(1-a_w)^{-1}$. Absolute trace-norm summability now implies $$\operatorname{tr}L_s^r=\sum_{|w|=r}\frac{a_w^s}{1-a_w}
         =\sum_{j\ge0}A(s+j)^r.$$ Expanding the logarithm for $\operatorname{Re}s>1/2$ and $|u|A(\operatorname{Re}s)<1$ yields $$\label{primitive}
 D(u,s)=\prod_{\gamma\ {\rm primitive}}\prod_{j\ge0}
       (1-u^{|\gamma|}a_\gamma^{s+j}).$$ Absolute convergence justifies regrouping words into necklaces and repeats. The source's unstabilized word product is a different object: $$Z_{\rm word}(u,s)=\frac1{1-uA(s)}=\frac{D(u,s+1)}{D(u,s)}.$$ The isolated zero orbit is in neither derivative-weighted product. Continuation beyond this domain will not mean ordinary convergence of [\[family\]](#family){reference-type="eqref" reference="family"} or [\[primitive\]](#primitive){reference-type="eqref" reference="primitive"} there.

\>0

# Whole-plane continuation

Hurwitz zeta has a meromorphic continuation with sole simple pole of residue one at its first argument one [@dlmf]. Writing $t_n=(n+1/2)^{-1}$ gives the locally normal scalar expansion $$\label{scalar}
 A(s)=\sum_{r\ge0}\frac{(s)_r}{4^rr!}
           \zeta(2s+2r,3/2).$$ Indeed $a_n=t_n^2/(1-t_n^2/4)$; the binomial series proves equality in the initial half-plane. On compact $s$ sets the rising-factorial quotient has at most polynomial growth in $r$, whereas the remaining tail is $O_K(9^{-r})$. This proves meromorphic continuation. At $s_m=1/2-m$ exactly the term $r=m$ is singular, with residue $$\label{scalarres}
 r_m=\frac{(1/2-m)_m}{2\,4^m m!}
     =\frac{(-1)^m}{2\,16^m}\binom{2m}{m}\ne0.$$ The factor $1/2$ comes from the pole's argument $2s+2m$.

For the operator define, near $|t|\le1/3$, $$h_t(z)=\frac{t+(z-1/2)t^2}{1-t^2/4},\qquad
 E_s(t)f=(1-t^2/4)^{-s} f\circ h_t
       =\sum_{l\ge0} E_l(s)f\,t^l.$$ Use the analytic logarithm of $1-t^2/4$ vanishing at zero. On this circle, $|h_t(z)|\le22/35<2$ for $|z|\le2$. The rank-one argument proves joint trace-class holomorphy and the Cauchy estimate $\|E_l(s)\|_1\le M_K3^l$ on compact $s$ sets. Separating the first three branches gives $$\label{opcont}
 L_s=\sum_{n=1}^3a_n^s C_{h_n}
        +\sum_{l\ge0}E_l(s)\zeta(2s+l,9/2).$$ For large $l$ the second zeta factor is $O_K((9/2)^{-l})$. Hence the trace-class tail has geometric ratio $2/3$ and converges normally away from its poles. Identity on the initial half-plane proves the unique whole-plane meromorphic continuation.

# Constructive residue operators

At $s=(1-l)/2$ the residue of [\[opcont\]](#opcont){reference-type="eqref" reference="opcont"} is $R_l=\tfrac12 E_l((1-l)/2)$. For input monomials, $$\label{coeff}
 E_l(s)z^j=[t^{l-j}](1+(z-1/2)t)^j(1-t^2/4)^{-s-j}.$$ This vanishes for $j>l$. A contributing term has $j+b+2r=l$ and output degree at most $b\le j$, so that $b\le\min(j,l-j)\le\lfloor l/2\rfloor$. Thus $R_l$ uses only derivatives at zero through order $l$ and has range in polynomials of degree at most $\lfloor l/2\rfloor$. This finite matrix is exact; its construction is not a finite-dimensional replacement for the meromorphic operator theorem.

For $l=2m$, restrict to degrees $j\le m$. The triangular diagonal is $r_{m-j}$, by [\[scalarres\]](#scalarres){reference-type="eqref" reference="scalarres"}. Every entry is nonzero, so $\operatorname{rank}R_{2m}=m+1$. The remaining parity requires a different argument: zero diagonal does not mean the residue operator is zero.

\>1

# Nonzero nilpotent poles and determinant blindness

[\[nilpotent\]]{#nilpotent label="nilpotent"} For every $m\ge0$, $L_s$ has a genuine simple pole at $s=-m$. Its residue $R_{2m+1}$ has rank $m+1$ and satisfies $R_{2m+1}^2=0$. Nevertheless $D(u,s)$ extends holomorphically across every such point.

At $s=-m$, input degree $j\le m$ gives the polynomial $$t^j(1+(z-1/2)t)^j(1-t^2/4)^{m-j},$$ whose degree in $t$ is at most $2m$. Its coefficient of $t^{2m+1}$ is zero. The residue therefore annihilates its own range, proving square-zero. For $j=m+1,\ldots,2m+1$, the output leading degree is $2m+1-j$, with nonzero coefficient $\frac12\binom{j}{2m+1-j}$. These distinct degrees prove rank $m+1$, hence a genuine operator pole.

On any compact $s$ set, sufficiently large $j$ satisfy $|A(s+j)|=O_K(2^{-j})$. Thus [\[det\]](#det){reference-type="eqref" reference="det"} continues normally in its tail. Its finite factors have poles only at half-integers $1/2-m$, by [\[scalar\]](#scalar){reference-type="eqref" reference="scalar"}. None has a pole at a nonpositive integer. The product is consequently holomorphic there, despite the operator pole.

For example $R_1 f=f'(0)/2$: it is rank one, nonzero, and squares to zero. A determinant's regular value at this parameter is a continued value, not the determinant of the undefined branch-sum operator at the pole.

[\[obstruction\]]{#obstruction label="obstruction"} The frozen determinant $D(1,s)$ has a pole of exact order $m+1$ at $s=1/2-m$ for every $m\ge0$. It cannot equal a zero-free entire factor times an entire target function.

The first $m+1$ factors in [\[det\]](#det){reference-type="eqref" reference="det"} have nonzero simple-pole residues. At this parameter the remaining factors are $1-A(1/2+j-m)$ for $j\ge m+1$. Their arguments are at least $3/2$. Telescoping gives $A(1)=1$; strict monotonicity on the real half-plane gives $0<A(v)<1$ for $v>1$. The tail is a convergent, nonzero product. Hence there is no pole cancellation. Multiplication by a zero-free entire function cannot remove any such pole.

# Audit, controls and the target boundary

The finite exact ledger contains 12 branches, 16 seven-dimensional matrices, 10 operator residue matrices, 10 scalar residues and all 340 words of lengths one through four over four branches. A separate checker reconstructs affine powers by polynomial multiplication, residue coefficients by two-variable convolution, and words by composition from the other end. It checks every rank and square-zero identity; its 1,169 matrix cells do not prove an infinite-dimensional theorem.

SymPy independently checks 220 exact identities. Two distinct Hurwitz expansions agree at six declared arguments with 100 working digits and tolerance $10^{-80}$; these are numerical observations, not interval certificates. An initial phase test accidentally included a real argument, failed, and was corrected to the three genuinely complex arguments. No theorem or exact evidence was changed by that repair.

The positive branch endpoint, the divergent $s=1/2$ source sum, the telescoping $s=1$ face, composite slopes, finite-alphabet parent, complex phases and determinant-versus-operator poles are explicit controls. A Hurwitz-zeta rewriting supplies no rational-prime orbit carrier. The conservative route tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT})$, overall rejected. Corollary [\[obstruction\]](#obstruction){reference-type="ref" reference="obstruction"} concerns this particular frozen determinant, not every possible renormalized source object.

The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`: all nine target and Route-B flags remain false.

# Conclusion

The Hardy space and trace-norm approximation make the source spectrum an operator theorem rather than a formal matrix observation. \>0 The centered branch expansion supplies the whole-plane meromorphic owner. \>1 Its residue parity separates real operator singularities from determinant singularities and leaves a precise obstruction for the frozen target candidate. This is one paper with three substantive revisions; the record is Round zeroonetwo. The complete derivation and independently executable receipts accompany the manuscript.

9 J. Barrionuevo, R. Burton, K. Dajani and C. Kraaikamp. Ergodic properties of generalized Lüroth series. *Acta Arithmetica* 74(4), 311--327 (1996). [doi:10.4064/aa-74-4-311-327](https://doi.org/10.4064/aa-74-4-311-327). O. F. Bandtlow and O. Jenkinson. On the Ruelle eigenvalue sequence. *Ergodic Theory and Dynamical Systems* 28(6), 1701--1711 (2008). [doi:10.1017/S0143385708000059](https://doi.org/10.1017/S0143385708000059). NIST Digital Library of Mathematical Functions. Section 25.11, Hurwitz zeta function. <https://dlmf.nist.gov/25.11>. Accessed 5 September 2026.
