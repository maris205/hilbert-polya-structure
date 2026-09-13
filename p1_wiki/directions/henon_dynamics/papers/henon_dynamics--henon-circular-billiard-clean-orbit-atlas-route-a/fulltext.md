---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-circular-billiard-clean-orbit-atlas-route-a"
canonical_tex: "henon_dynamics/henon_circular_billiard_clean_orbit_atlas_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_circular_billiard_clean_orbit_atlas_route_a/paper/main.pdf"
source_sha256: "cf2c868641ae71a8193ab7d2c2e033e4e3a3d07bf30e5d3a77f06aadc40aefa7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Clean Primitive-Family Atlas for the Circular Billiard

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_circular_billiard_clean_orbit_atlas_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_circular_billiard_clean_orbit_atlas_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_circular_billiard_clean_orbit_atlas_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_circular_billiard_clean_orbit_atlas_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  In the disk, the billiard map is exactly a rigid translation in the boundary angle and signed half-chord-angle coordinates. We prove one all-parameter closure theorem: every reduced fraction $(m/n)$, with $1\le m<n/2$, gives two orientation-separated clean $S^1$ families, with explicit chord length, caustic, action, repetitions, and unipotent return shear. The diameter and grazing faces are treated separately. The auxiliary $p=\sin\alpha$ is not called a canonical momentum. This is a geometric Route-A result; no target arithmetic or spectral match is asserted.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: 'A Clean Primitive-Family Atlas for the Circular Billiard'
```

## Markdown 正文

suppressoptionalinfo 611

# Frozen disk and incidence convention

Let $D_R=\{x^2+y^2<R^2\}$. At a collision write $\theta\in\mathbb R/2\pi\mathbb Z$ for boundary angle and $\alpha\in(-\pi/2,\pi/2)$ for the signed half-chord angle defined by the oriented central increment $\theta'-\theta=2\alpha\pmod {2\pi}$. Its absolute value is the acute angle-to-tangent magnitude and its sign records direction. The auxiliary incidence amplitude $p=\sin\alpha$ records the sign and angle magnitude; it is not a canonical momentum. In the working angle chart the exact map is $$B(\theta,\alpha)=(\theta+2\alpha,\alpha)\pmod {2\pi},
 \qquad DB=\begin{pmatrix}1&2\\0&1\end{pmatrix}.       \label{eq:map}$$ The physical billiard symplectic form is expressed using the appropriate canonical boundary momentum; we make no claim that $\,\mathrm d\theta\wedge\,\mathrm d\alpha$ is that form.

=0 The baseline receipt records ([\[eq:map\]](#eq:map){reference-type="ref" reference="eq:map"}) and the fundamental rational range. Endpoint faces and clean-return kernels are reserved for the later rounds.

# Primitive rational families

[\[thm:families\]]{#thm:families label="thm:families"} For $\gcd(m,n)=1$ and $1\le m<n/2$, put $\alpha_\varepsilon=\varepsilon\pi m/n$, $\varepsilon\in\{+1,-1\}$. Then $B^n(\theta,\alpha_\varepsilon)=(\theta,\alpha_\varepsilon)$ for every $\theta$, and $n$ is the minimal positive bounce period. Conversely, every interior rational rotation family has this form.

Iterating [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} gives $B^q(\theta,\alpha)=(\theta+2q\alpha,\alpha)$. For $\alpha=\varepsilon\pi m/n$, the shift after $n$ bounces is $\varepsilon2\pi m$. If a smaller $q$ closes, $qm/n\in\mathbb Z$, which contradicts $\gcd(m,n)=1$. Conversely, a rational rotation in the fundamental interval has a unique reduced numerator/denominator and one of the two signs.

\>0

[\[prop:geometry\]]{#prop:geometry label="prop:geometry"} For either orientation the chord, polygon length, concentric caustic radius, and fixed-speed geometric action are $$\ell_{m,n}=2R\sin(\pi m/n),\quad
 L_{m,n}=2nR\sin(\pi m/n),\quad
 r_c=R\cos(\pi m/n),\quad S_{m,n}=p_0L_{m,n}.          \label{eq:geometry}$$ At the frozen unit speed $p_0=1$, $S=L$. The $k$-fold repetition has $kn$ bounces and multiplies both $L$ and $S$ by $k$; its unreduced label $(km,kn)$ is retained but is not primitive.

The central angle between successive endpoints is $2\pi m/n$, so the chord is the corresponding isosceles-triangle base. Its distance from the center is $R\cos(\pi m/n)$, proving the caustic statement. Summing $n$ equal chords and integrating unit-speed momentum gives [\[eq:geometry\]](#eq:geometry){reference-type="eqref" reference="eq:geometry"}; repetition is immediate.

   $(m,n)$   orientation   $\alpha$     $\ell$      $L=S$      $r_c$
  --------- ------------- ----------- ---------- ----------- ----------
   $(1,3)$       $+$        $\pi/3$    $1.7321$   $5.1962$    $0.5000$
   $(1,4)$       $-$       $-\pi/4$    $1.4142$   $5.6569$    $0.7071$
   $(2,5)$       $+$       $2\pi/5$    $1.9021$   $19.0211$   $0.3090$
   $(3,7)$       $-$       $-3\pi/7$   $1.9499$   $27.2986$   $0.2225$

  : Selected rows from the finite exact/high-precision receipt (R=1).

# Clean return and determinant obstruction

For a primitive row, the fixed set is the one-dimensional family $\operatorname{Fix}(B^n)\supset\{(\theta,\alpha_\varepsilon):\theta\in S^1\}$. In the angle chart, $$DB^n=\begin{pmatrix}1&2n\\0&1\end{pmatrix},\qquad
 DB^n-I=\begin{pmatrix}0&2n\\0&0\end{pmatrix}.         \label{eq:shear}$$ Hence $$\ker(DB^n-I)=\operatorname{span}\{(1,0)\}=T(S^1_\theta),\quad
 \det(I-DB^n)=0.                                      \label{eq:kernel}$$ The return is unipotent, with both eigenvalues one. Thus an isolated-orbit determinant denominator is obstructed: the clean family must not be assigned an isolated amplitude. The finite receipt verifies the kernel itself, not only the vanishing determinant.

=1

# Revision-one ledger

The producer enumerates every primitive pair through $n=12$, both signs, six explicit repetitions, and the endpoint rows. Chebyshev relations $T_n(\cos(\pi m/n))=(-1)^m$ provide an algebraic/high-precision receipt. An independent checker makes more than two thousand assertions and a SymPy script repeats the trigonometric and shear identities.

# Diameter, grazing, and natural quantization

The diameter case $(m,n)=(1,2)$, $\alpha=\pm\pi/2$, is one endpoint-equivalent family, not two families. Its angle-chart return matrix for two bounces is the boundary value $\left[\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\right]$, but it is not an interior regular row. At $\alpha=0$, $p=0$, the chord has zero length; the receipt records one grazing row with two one-sided oriented limits. No boundary degeneration is silently counted as a new primitive flight.

For A4 we record only the standard self-adjoint quantizations of the same disk: $-\Delta_{D_R}$ with $f|_{\partial D_R}=0$ (Dirichlet), or with $\partial_\nu f|_{\partial D_R}=0$ (Neumann). This is a definition of a source-local quantization problem, not an eigenvalue table or a target match.

\>1

# Verification and Route-A boundary

The final receipt contains 44 primitive rows, six repetitions, two boundary rows, 13 exact identities, independent checks, byte replay, and 31 hostile repaired-hash mutations. The frozen scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; no prime/zero table, Euler factor, root number, automorphy claim, target determinant, or Hilbert--Pólya operator is used. Therefore the locked tuple is `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL, A4_NATURAL_QUANTIZATION)`, with overall verdict `ROUTE_A_REJECTED`.

9 G. D. Birkhoff, "On the periodic motions of dynamical systems," *Acta Mathematica* 50 (1927), 359--379, DOI [10.1007/BF02421325](https://doi.org/10.1007/BF02421325). R. L. Bishop, "Circular Billiard Tables, Conjugate Loci, and a Cardioid," *Regular and Chaotic Dynamics* 8 (2003), 83--95, DOI [10.1070/RD2003v008n01ABEH000227](https://doi.org/10.1070/RD2003v008n01ABEH000227).
