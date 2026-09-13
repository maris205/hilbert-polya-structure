---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-bose-josephson-dimer-phase-portrait"
canonical_tex: "henon_dynamics/henon_bose_josephson_dimer_phase_portrait/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_bose_josephson_dimer_phase_portrait/paper/main.pdf"
source_sha256: "ab3559fcffde91ea8e8974f7c46ffce71228a620f78f07df4d3f7f39288b1f87"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Coordinate-Safe Phase Portrait for the Bose--Josephson Dimer

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_bose_josephson_dimer_phase_portrait>)
- [规范 TeX](<../../../../../henon_dynamics/henon_bose_josephson_dimer_phase_portrait/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_bose_josephson_dimer_phase_portrait/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_bose_josephson_dimer_phase_portrait/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the normalized two-mode Bose--Josephson dimer $H(z,\phi)=\Lambda z^2/2-\sqrt{1-z^2}\cos\phi$, $\Lambda\ge0$. Passing to the Bloch sphere removes the apparent coordinate singularity at $z=\pm1$. We classify $(0,0)$, $(0,\pi)$, and the $\Lambda>1$ symmetry-broken equilibria, including the $\Lambda=1$ pitchfork. Elimination of the phase gives an exact quartic in $z$; its roots yield complete-elliptic-$K$ periods on crossing and self-trapped components. The $H=1$ sech homoclinic, its $\Lambda=2$ pole limit, and the reverse component criterion are stated without assigning a finite period to a separatrix. This is a source-local phase-portrait theorem: no arithmetic owner or target determinant is claimed.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: 'A Coordinate-Safe Phase Portrait for the Bose--Josephson Dimer'
```

## Markdown 正文

suppressoptionalinfo 611

# Hamiltonian and Bloch regularization

Set $$H(z,\phi)=\frac{\Lambda z^2}{2}-\sqrt{1-z^2}\cos\phi,
 \qquad \Lambda\ge0,$$ with canonical equations $$\dot z=-\sqrt{1-z^2}\sin\phi,\qquad
 \dot\phi=\Lambda z+\frac{z\cos\phi}{\sqrt{1-z^2}}. \tag{1}$$ The Bloch variables $x=\sqrt{1-z^2}\cos\phi$, $y=\sqrt{1-z^2}\sin\phi$ satisfy $$\dot x=-\Lambda zy,\qquad \dot y=z(1+\Lambda x),\qquad \dot z=-y. \tag{2}$$ Thus the north and south poles have $\dot y=+1$ and $-1$, respectively; they are not equilibria and no value of the singular angle $\phi$ is assigned there.

The points $(0,0)$ and $(0,\pi)$ exist for every $\Lambda$. The first has energy $-1$, linearization $\left[\begin{smallmatrix}0&-1\\\Lambda+1&0\end{smallmatrix}\right]$, and frequency $\sqrt{\Lambda+1}$. The second has energy $+1$ and linearization $\left[\begin{smallmatrix}0&1\\\Lambda-1&0\end{smallmatrix}\right]$: it is elliptic for $\Lambda<1$, parabolic at $\Lambda=1$, and hyperbolic for $\Lambda>1$. For $\Lambda>1$, two additional elliptic points are $$z=\pm\sqrt{1-\Lambda^{-2}},\quad \phi=\pi,\quad
 H_{\max}=\frac{\Lambda+\Lambda^{-1}}2. \tag{3}$$ In the canonical $(z,\phi-\pi)$ coordinates their matrix is $\left[\begin{smallmatrix}0&1/\Lambda\\-\Lambda(\Lambda^2-1)&0\end{smallmatrix}\right]$, so their small-amplitude period is $2\pi/\sqrt{\Lambda^2-1}$. The zero-phase crossing limit is $2\pi/\sqrt{\Lambda+1}$, and (3) coalesces with $(0,\pi)$ at the pitchfork $\Lambda=1$.

Differentiate (1) and solve $\dot z=\dot\phi=0$ away from the poles. The displayed matrices follow by first-order expansion. Equation (2) is obtained by the chain rule and extends the vector field over both poles.

# Energy quartic and regular periods

On $H=h$, $$\dot z^2=(1-z^2)-\left(\frac{\Lambda z^2}{2}-h\right)^2
 =-\frac{\Lambda^2}{4}z^4+(\Lambda h-1)z^2+1-h^2. \tag{4}$$ For $\Lambda>0$, let $$y_\pm=\frac{2(\Lambda h-1\pm
 \sqrt{\Lambda^2-2\Lambda h+1})}{\Lambda^2}. \tag{5}$$ Then $\dot z^2=(\Lambda^2/4)(y_+-z^2)(z^2-y_-)$. If $-1<h<1$, $y_-<0<y_+$, the level is one connected crossing component and $$T_{\rm cross}=\frac{8}{\Lambda\sqrt{y_+-y_-}}
 K\!\left(\sqrt{\frac{y_+}{y_+-y_-}}\right). \tag{6}$$ If $\Lambda>1$ and $1<h<H_{\max}$, there are two sign-preserving components and each has $$T_{\rm self}=\frac{4}{\Lambda\sqrt{y_+}}
 K\!\left(\sqrt{1-\frac{y_-}{y_+}}\right). \tag{7}$$ Here $K$ uses the modulus convention; the code passes its square to the numerical library. The limits near the two elliptic centers are exactly the frequencies stated above.

# Separatrix and component criterion

For $\Lambda>1,h=1$, (4) has the homoclinic solution $$z(t)=\pm\frac{2\sqrt{\Lambda-1}}{\Lambda}
 \operatorname{sech}(\sqrt{\Lambda-1}\,t). \tag{8}$$ The full critical level is connected through the saddle at $z=0$, with two one-sided homoclinic branches. At its turning point the phase is $\pi$ for $1<\Lambda<2$, the point is a Bloch pole at $\Lambda=2$, and the phase is 0 for $\Lambda>2$. Formula (8) has infinite period; it is not a regular periodic orbit.

For regular $\Lambda>1$ levels, $1<h<H_{\max}$ is exactly the self-trapped regime: the two connected components preserve the sign of $z$, and changing the initial sign selects the reflected component. For $-1<h<1$, the single component crosses $z=0$, so both signs occur. At $h=1$, sign change is only asymptotic. At $\Lambda=1,h=1$, (4) reduces to $-z^4/4$, so only the isolated degenerate point $z=0$ remains. At $\Lambda=0$, $H=-x$ gives rigid Bloch rotation of period $2\pi$ on regular circles.

\>0

# Certified finite receipt

The accompanying receipt contains 14 fixed-point rows, 8 pole rows, 13 level rows, and 5 component criteria. A producer-independent checker makes 995 assertions. SymPy verifies the Hamilton/Bloch identities, quartic roots, pitchfork and sech profile, while three independent transformed quadratures reproduce (6)--(7). Byte replay passes and a hostile suite rejects 28/28 repaired-hash mutations.

\>1

# Route-A boundary

Regular levels form a continuum, so the result is A1\_WEAK rather than a discrete primitive-orbit atlas. There is no intrinsic rational-prime carrier, target weighted zeta, Fredholm determinant, or target-zero match. The locked tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_WEAK},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_NATURAL\_QUANTIZATION}),$$ with `ROUTE_A_REJECTED`, Route B disabled, and scope literal `NO_BAD_EULER_OR_ROOT_NUMBER`. Source-local phase portraits must not be reinterpreted as target arithmetic structures.

9 A. Smerzi, S. Fantoni, S. Giovanazzi and S. Shenoy, Quantum coherent atomic tunneling between two trapped Bose--Einstein condensates, *Phys. Rev. Lett.* 79 (1997), 4950--4953, DOI: 10.1103/PhysRevLett.79.4950, <https://doi.org/10.1103/PhysRevLett.79.4950>. S. Raghavan, A. Smerzi, S. Fantoni and S. Shenoy, Coherent oscillations between two weakly coupled Bose--Einstein condensates, *Phys. Rev. A* 59 (1999), 620--633, DOI: 10.1103/PhysRevA.59.620, <https://doi.org/10.1103/PhysRevA.59.620>.

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, target-zero, determinant-matching, or Hilbert--Pólya claim. **Data and code.** All rows and audits accompany HCS-C243. This is not external peer review. **AI-use disclosure.** Generative tools assisted drafting and code generation; the artifact chain checks displayed formulas and metadata.
