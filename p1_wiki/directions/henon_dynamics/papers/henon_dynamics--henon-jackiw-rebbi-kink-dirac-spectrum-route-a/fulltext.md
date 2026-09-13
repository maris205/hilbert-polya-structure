---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-jackiw-rebbi-kink-dirac-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_jackiw_rebbi_kink_dirac_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_jackiw_rebbi_kink_dirac_spectrum_route_a/paper/main.pdf"
source_sha256: "a47ccfe6c4f2a7bcb108ee6cda4d5038fe1140a17753e1bdb5bbc7fc97fbe1a7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Complete Integer-Kink Dirac Atlas: Zero Mode, Bound Ladder, Thresholds, and Reflectionlessness

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_jackiw_rebbi_kink_dirac_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_jackiw_rebbi_kink_dirac_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_jackiw_rebbi_kink_dirac_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_jackiw_rebbi_kink_dirac_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every positive integer height, we give a single proof of the complete spectral and scattering atlas of the one-dimensional hyperbolic-tangent Dirac kink. Bounded-perturbation theory fixes the self-adjoint domain; supersymmetric factorization and shape invariance exhaust the simple bound ladder; the unpaired kernel gives exactly one chiral zero mode; and Darboux images of the free zero-momentum state and plane waves settle both threshold resonances and reflectionlessness. Exact ledgers independently check 25 heights and 150 rational complex scattering values, but the all-integer conclusion comes from the analytic descent argument. No priority or arithmetic-target claim is made.
author:
- 'HCS-C352 source-local reconstruction'
date: 3 September 2026
title: |
  The Complete Integer-Kink Dirac Atlas:\
  Zero Mode, Bound Ladder, Thresholds, and Reflectionlessness
```

## Markdown 正文

**Revision certificate.** =0 Domain, factorization, and complete discrete-ladder closure. =1 Round-one threshold-resonance and reflectionless-scattering closure. Round-two spectral-type, boundary, evidence, and Route-A closure.

# Frozen operator and theorem

On $L^2(\mathbb R;\mathbb C^2)$ define, for $n\in\mathbb Z_{\geq1}$, $$A_n=\frac d{dx}+n\tanh x,\qquad
 A_n^*=-\frac d{dx}+n\tanh x,
 \qquad
 H_n=\begin{pmatrix}0&A_n^*\\A_n&0\end{pmatrix},          \tag{1}$$ with domain $H^1(\mathbb R;\mathbb C^2)$. "Upper" and "lower" always refer to the first and second spinor components in (1). A threshold resonance means a nonzero bounded distributional solution which is not in $L^2$.

[\[thm:main\]]{#thm:main label="thm:main"} For every integer $n\geq1$ the following statements hold.

1.  $H_n$ is self-adjoint on $H^1(\mathbb R;\mathbb C^2)$ and generates the unitary group $e^{-itH_n}$.

2.  Its essential spectrum is $$\sigma_{\rm ess}(H_n)=(-\infty,-n]\cup[n,\infty),$$ and the continuous spectral subspace is purely absolutely continuous.

3.  The complete point spectrum is $$\sigma_{\rm p}(H_n)=\{0\}\cup
     \left\{\,\pm\sqrt{j(2n-j)}:1\leq j\leq n-1\,\right\}.   \tag{2}$$ Every listed eigenvalue is simple. The zero eigenspace is spanned by the column spinor whose upper component is $\operatorname{sech}^n x$ and whose lower component is zero.

4.  Both $+n$ and $-n$ are resonances and neither is an $L^2$ eigenvalue.

5.  Both scalar channels of $H_n^2$, and consequently the Dirac scattering problem, are reflectionless.

For $n=1$, (2) contains only the zero mode; this nontrivial boundary case is included in the theorem.

# Self-adjoint square and shape invariance

The free off-diagonal derivative operator on $H^1$ is self-adjoint after the fixed signs in (1) are used. Multiplication by the bounded Hermitian matrix with entries $n\tanh x$ is a bounded self-adjoint perturbation. The Kato--Rellich bounded-perturbation theorem proves assertion (i), and Stone's theorem supplies the unitary group.

Direct multiplication, using $(\tanh x)'=\operatorname{sech}^2x$, gives $$\begin{aligned}
 B_n:=A_n^*A_n
  &=-\frac{d^2}{dx^2}+n^2-n(n+1)\operatorname{sech}^2x,\\
 C_n:=A_nA_n^*
  &=-\frac{d^2}{dx^2}+n^2-n(n-1)\operatorname{sech}^2x,\\
 H_n^2&=\operatorname{diag}(B_n,C_n).
\end{aligned}                                                   \tag{3}$$ The key identity is the exact shape invariance $$C_n=B_{n-1}+2n-1.                                      \tag{4}$$ Moreover $B_nA_n^*=A_n^*C_n$ and $A_nB_n=C_nA_n$.

[\[lem:scalar\]]{#lem:scalar label="lem:scalar"} The point spectrum of $B_n$ consists precisely of the simple values $$q_{n,j}=j(2n-j),\qquad j=0,\ldots,n-1.                 \tag{5}$$ Its essential spectrum is $[n^2,\infty)$ and is purely absolutely continuous. At $n^2$ there is a resonance and no eigenvalue. The same statements for $C_n$ hold with the list $j=1,\ldots,n-1$.

The seed $\phi_{m,0}=\operatorname{sech}^m x$ satisfies $A_m\phi_{m,0}=0$. For $0\leq j<m$, repeated use of (4) gives the nonzero state $$\phi_{m,j}=A_m^*A_{m-1}^*\cdots A_{m-j+1}^*
             \operatorname{sech}^{m-j}x,
 \qquad B_m\phi_{m,j}=j(2m-j)\phi_{m,j}.                \tag{6}$$ Its nodal degree, or equivalently the nonvanishing intertwining norms, shows that these states are simple and distinct.

Construction is not yet exhaustion. If a further $L^2$ eigenstate of $B_m$ had energy below $m^2$, applying $A_m,A_{m-1},\ldots$ either lands in one of the one-dimensional kernels already used in (6), or produces an $L^2$ eigenstate below the continuum of $B_0=-d^2/dx^2$. The latter has none. Reversing the intertwiners therefore leaves exactly (5).

It remains to prove the spectral type rather than infer it from formal Jost solutions. Put $$D_m=A_m^*A_{m-1}^*\cdots A_1^*,\qquad B_0=-d^2/dx^2,
 \qquad Q_m=\prod_{r=1}^m(B_0+r^2).$$ Induction from (4), first on Schwartz functions and then by closure, gives $$B_mD_m=D_m(B_0+m^2),\qquad D_m^*D_m=Q_m.               \tag{7}$$ Since $Q_m\geq(m!)^2$, the initially defined operator $U_m=D_mQ_m^{-1/2}$ extends to an isometry on $L^2(\mathbb R)$ and satisfies $B_mU_m=U_m(B_0+m^2)$. Its range is closed and equals the closure of $\operatorname{ran}D_m$; hence its orthogonal complement is $\ker D_m^*$.

Each of the $m$ states in (6) belongs to this kernel: applying the adjoint intertwining would otherwise create an $L^2$ eigenstate of $B_0+m^2$ below $m^2$. Conversely, $D_m^*$ is an order-$m$ differential operator, so its solution space, and therefore its $L^2$ kernel, has dimension at most $m$. Thus $$(\operatorname{ran}U_m)^\perp
 =\operatorname{span}\{\phi_{m,0},\ldots,\phi_{m,m-1}\}.$$ The restriction of $B_m$ to the orthogonal complement of these bound states is consequently unitarily equivalent to $B_0+m^2$. This proves at once that its remaining spectrum is $[m^2,\infty)$, purely absolutely continuous, with no embedded eigenvalue or singular-continuous part. Finally, (4) transfers the complete statement to $C_n$.

# Dirac point spectrum and chirality

The equations $A_nu=0$ and $A_n^*v=0$ give $u=c\operatorname{sech}^nx$ and $v=c'\cosh^nx$. Exactly the first is square-integrable, so $\ker H_n$ is one-dimensional and upper chiral. Its squared norm is $$\int_{\mathbb R}\operatorname{sech}^{2n}x\,dx
 =\frac{4^n n!(n-1)!}{(2n)!}.                            \tag{8}$$ For every $q>0$, $A_n$ and $A_n^*$ identify the $q$-eigenspaces of $B_n$ and $C_n$. If $B_nu=qu$, the two normalized linear combinations of $u$ and $q^{-1/2}A_nu$ have Dirac energies $\pm\sqrt q$. Lemma [\[lem:scalar\]](#lem:scalar){reference-type="ref" reference="lem:scalar"} now proves (2), including all multiplicities. The anticommutation of $H_n$ with $\operatorname{diag}(1,-1)$ is the structural reason for the nonzero sign pairing.

\>0

# Thresholds and reflectionless scattering {#sec:scattering}

Start with the free plane wave $e^{ikx}$, $k>0$, and set $$\Psi_{m,k}=A_m^*A_{m-1}^*\cdots A_1^*e^{ikx}.           \tag{9}$$ Intertwining gives $B_m\Psi_{m,k}=(m^2+k^2)\Psi_{m,k}$. With the time convention $e^{-iEt}$, each factor tends to $-ik+r$ at $+\infty$ and to $-ik-r$ at $-\infty$. Thus $$\Psi_{m,k}\sim C_-e^{ikx}\quad(x\to-\infty),\qquad
 \Psi_{m,k}\sim C_+e^{ikx}\quad(x\to+\infty),$$ where $C_-=\prod_{r=1}^m(-r-ik)$ and $C_+=\prod_{r=1}^m(r-ik)$. Normalizing the incoming coefficient at the left gives $$r_m(k)=0,\qquad
 t_m(k)=\frac{C_+}{C_-}
 =\prod_{r=1}^m\frac{k+ir}{k-ir},\qquad |t_m(k)|=1.       \tag{10}$$ This equation fixes the phase convention; changing the Jost convention may invert $t_m$ but cannot alter reflectionlessness. The lower channel is the adjacent member $B_{m-1}$ plus a constant, so it is reflectionless too. For nonzero Dirac energy the other spinor component is recovered by a first-order application of $A_n$ or $A_n^*$; no reflected exponential can be created. This proves assertion (v) without asserting a convention-independent Dirac transmission phase.

At $k=0$, (9) becomes $$F_m:=\Psi_{m,0}=D_m1,\qquad
 F_m(+\infty)=m!,\qquad F_m(-\infty)=(-1)^m m!.$$ Indeed, $F_m$ is a polynomial in $\tanh x$ and $B_mF_m=m^2F_m$; its endpoint values follow successively from the limiting coefficients $+r$ and $-r$. The threshold spinors are $$\begin{pmatrix}F_m\\ (\pm m)^{-1}A_mF_m\end{pmatrix}.$$ Because $(A_mF_m)(+\infty)=m\,m!$ and $(A_mF_m)(-\infty)=(-1)^{m+1}m\,m!$, they are bounded and nonzero at both ends, hence not in $L^2$. The unitary decomposition (7) shows that the free threshold has no hidden $L^2$ preimage, so neither Dirac threshold is an eigenvalue. This proves assertion (iv).

\>1

# Spectral type and boundary atlas

By the unitary decomposition (7), both scalar channels of $H_n^2$ have purely absolutely continuous spectrum on $[n^2,\infty)$ outside their listed finite eigenspaces. A singular or point component of $H_n$ away from zero would push forward under $E\mapsto E^2$ to the same type for $H_n^2$. The gap isolates the already classified zero mode. Functional calculus and the first-order component pairing therefore give $(-\infty,-n]\cup[n,\infty)$ as the purely absolutely continuous part of $H_n$, with no embedded eigenvalues or singular-continuous spectrum.

Three edges should not be silently folded into the theorem.

-   At $n=0$, $H_0$ is the free massless Dirac operator with spectrum $\mathbb R$; zero is not the edge of an open mass gap.

-   Replacing $\tanh x$ by $-\tanh x$ exchanges the chiral component of the unique zero mode while preserving the nonzero energies.

-   Introducing inverse length $a>0$ as $A_{n,a}=d/dx+na\tanh(ax)$ scales every energy and threshold by $a$. No independent spectral structure is created.

# Evidence, lineage, and scope

The exact certificate records $n=0,\ldots,24$, all 276 nonzero bound pairs in that panel, the factorization and zero-mode norm, and 150 rational complex evaluations of (10). A producer-independent checker reconstructs every row; a symbolic lane checks 171 operator and Darboux identities; two isolated replays agree byte for byte; and 58 repaired-hash or parser attacks are rejected. These checks catch signs and off-by-one errors. They do not prove the all-integer spectral theorem; Lemma [\[lem:scalar\]](#lem:scalar){reference-type="ref" reference="lem:scalar"} does.

Jackiw and Rebbi supply the historical zero-mode lineage [@jackiwrebbi]. Charmchi and Gousheh give a direct exact spectral and scattering study of the 1+1 dimensional model [@charmchi]. We claim no priority; the result here is a convention-frozen reconstruction with an auditable completeness proof.

The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ Self-adjointness genuinely supplies natural quantization, but the integer height is not arithmetic origin, (10) is not a target Euler product, and no target divisor, functional equation, counting law, or zero matching is defined. Route A is rejected and Route B is not invoked. In particular, this paper claims no arithmetic local data, Euler factors, root number, automorphy, target-zero identification, or Hilbert--Pólya operator.

9 R. Jackiw and C. Rebbi, "Solitons with fermion number 1/2," *Phys. Rev. D* 13 (1976), 3398--3409. [doi:10.1103/PhysRevD.13.3398](https://doi.org/10.1103/PhysRevD.13.3398).

F. Charmchi and S. S. Gousheh, "A Complete Spectral Analysis of the Jackiw--Rebbi Model, Including its Zero Mode," *Phys. Rev. D* 89 (2014), 025002. [doi:10.1103/PhysRevD.89.025002](https://doi.org/10.1103/PhysRevD.89.025002).
