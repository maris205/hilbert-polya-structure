---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-neumann-uhlenbeck-integrable-sphere-route-a"
canonical_tex: "henon_dynamics/henon_neumann_uhlenbeck_integrable_sphere_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_neumann_uhlenbeck_integrable_sphere_route_a/paper/main.pdf"
source_sha256: "650dbb947b4cd2b0d26b5ecdc6dbf750d92d6d6b42c3e9cb86b6bc3a7361c742"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uhlenbeck Integrals, a Rational Lax Matrix, and Compact Liouville Fibers for the Neumann Sphere

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_neumann_uhlenbeck_integrable_sphere_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_neumann_uhlenbeck_integrable_sphere_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_neumann_uhlenbeck_integrable_sphere_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_neumann_uhlenbeck_integrable_sphere_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the anisotropic Neumann oscillator on the round two-sphere we prove global completeness and derive all three Uhlenbeck integrals with their two linear relations. \>0 A rational $2\times2$ Lax matrix generates the integrals as determinant residues. Direct Dirac-bracket involution and compactness close the regular Liouville two-tori and their necessary-and-sufficient rational-frequency return criterion. \>1 The six axial equilibria, invariant coordinate circles, repeated-spectrum $SO(2)$ faces, isotropic great circles, and natural compact quantization are closed separately. Exact finite receipts test conventions but do not replace the continuum proof.
author:
- 'Route-A source-local certificate HCS-C349'
date: 3 September 2026
title: |
  Uhlenbeck Integrals, a Rational Lax Matrix, and\
  Compact Liouville Fibers for the Neumann Sphere
```

## Markdown 正文

trailerid \[\<C3492026090300000000000000000000\>\<C3492026090300000000000000000000\>\]

# Frozen constrained system and theorem

Let $A=\operatorname{diag}(a_1,a_2,a_3)$ with $a_1<a_2<a_3$. On $$T^*S^2=\{(x,p)\in\mathbb R^3\times\mathbb R^3:|x|^2=1,
                  \ x\mathbin{\cdot}p=0\}$$ take $$\label{eq:N}
 H=\frac12(|p|^2+x^TAx),\qquad
 \dot x=p,\qquad
 \dot p=-Ax+\alpha x,\quad \alpha=x^TAx-|p|^2.$$ Put $L_{ij}=x_ip_j-x_jp_i$ and $$\label{eq:F}
 F_i=x_i^2+\sum_{j\ne i}\frac{L_{ij}^2}{a_i-a_j}.$$

[\[thm:main\]]{#thm:main label="thm:main"} The flow [\[eq:N\]](#eq:N){reference-type="eqref" reference="eq:N"} is complete. The $F_i$ are conserved, pairwise Dirac--Poisson commuting, and satisfy $$\sum_iF_i=1,\qquad \sum_i a_iF_i=2H.$$ \>0 They are the residues of the rational Lax determinant in Section [3](#sec:lax){reference-type="ref" reference="sec:lax"}. Every connected regular common fiber of two independent integrals is a Liouville two-torus; the physical flow on it is periodic precisely when its frequency vector has a common period. \>1 The axial, coordinate, repeated-spectrum, and isotropic clauses in Section [4](#sec:boundary){reference-type="ref" reference="sec:boundary"} exhaust the declared parameter boundaries. The source Hamiltonian has the natural self-adjoint compact-resolvent quantization stated there.

# Completeness and the Uhlenbeck identities

The two constraint derivatives are $$\frac d{dt}|x|^2=2x\mathbin{\cdot}p,\qquad
 \frac d{dt}(x\mathbin{\cdot}p)=|p|^2-x^TAx+\alpha=0$$ on $T^*S^2$. Also $\dot H=0$. On $H=E$ the identity $|p|^2=2E-x^TAx$ bounds $p$; the orbit remains in a compact subset, and the smooth vector field is complete.

The angular momenta satisfy $$\label{eq:Ldot}
 \dot L_{ij}=(a_i-a_j)x_ix_j.$$ Hence $$\dot F_i=2x_i\left(p_i+\sum_{j\ne i}L_{ij}x_j\right)=0,$$ because the parenthesis equals $p_i+x_i(x\mathbin{\cdot}p)-p_i|x|^2$. Pairing $(i,j)$ and $(j,i)$ proves $\sum F_i=1$. The weighted pairing and the Gram identity give $$\sum_i a_iF_i=x^TAx+\sum_{i<j}L_{ij}^2
 =x^TAx+|p|^2=2H.$$ This is the *compact Uhlenbeck owner* added in revision round zero.

\>0

# Resolvent Lax generator {#sec:lax}

For $\lambda\notin\{a_1,a_2,a_3\}$ let $$R_\lambda=(\lambda I-A)^{-1},\quad
 U=x^TR_\lambda x,\quad V=x^TR_\lambda p,\quad
 W=1+p^TR_\lambda p$$ and define $$\label{eq:lax}
 \mathcal L=\begin{pmatrix}V&U\\-W&-V\end{pmatrix},\qquad
 \mathcal M=\begin{pmatrix}0&1\\\alpha-\lambda&0\end{pmatrix}.$$ Using $a_i/(\lambda-a_i)=\lambda/(\lambda-a_i)-1$ in [\[eq:N\]](#eq:N){reference-type="eqref" reference="eq:N"} gives $$\dot U=2V,\qquad
 \dot V=W+(\alpha-\lambda)U,
 \qquad \dot W=2(\alpha-\lambda)V.$$ These are exactly $\dot{\mathcal L}=[\mathcal L,\mathcal M]$. Moreover, $$\label{eq:residue}
 \det\mathcal L=UW-V^2
 =\sum_{i=1}^3\frac{F_i}{\lambda-a_i}.$$ Indeed, the residue at $a_i$ is [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}; both rational functions vanish at infinity and have no other poles.

The constrained bracket is $$\{x_i,x_j\}_D=0,\quad
 \{x_i,p_j\}_D=\delta_{ij}-x_ix_j,\quad
 \{p_i,p_j\}_D=x_jp_i-x_ip_j.$$ Differentiating [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}, substituting these three coordinate brackets, and pairing the denominators $a_i-a_j$ and $a_j-a_i$ gives $$\label{eq:commute}
 \{F_i,F_j\}_D=0\qquad(1\le i,j\le3).$$ The full finite-sum cancellation is recorded in the proof package and is independently expanded by the symbolic lane.

The two linear relations leave two generically independent integrals. A regular common fiber is closed in a compact energy shell. Liouville--Arnold therefore identifies each connected component with $\mathbb T^2$ and gives $\theta(t)=\theta(0)+t\omega$. Return occurs exactly when $$\label{eq:return}
 T\omega\in2\pi\mathbb Z^2\quad\hbox{for some }T>0.$$ For two nonzero components this is $\omega_1/\omega_2\in\mathbb Q$. Continuously selected resonant tori are not an isolated primitive-orbit ledger. Equations [\[eq:lax\]](#eq:lax){reference-type="eqref" reference="eq:lax"}--[\[eq:return\]](#eq:return){reference-type="eqref" reference="eq:return"} are the *resolvent torus owner* of revision round one.

\>1

# All declared degenerations and quantization {#sec:boundary}

At $x=\pm e_i,p=0$, a tangent component $q_j$, $j\ne i$, obeys $$\ddot q_j=-(a_j-a_i)q_j.$$ Thus the two copies over $e_1,e_2,e_3$ are respectively elliptic--elliptic, saddle--center, and saddle--saddle. Every face $x_i=p_i=0$ is invariant and reduces to $$H_i=\frac12\dot\theta^2+\frac12
     (a_j\cos^2\theta+a_k\sin^2\theta),
 \qquad \{i,j,k\}=\{1,2,3\}.$$

If $a_1=a_2$, the individual fractions $F_1,F_2$ are not used. Equation [\[eq:Ldot\]](#eq:Ldot){reference-type="eqref" reference="eq:Ldot"} instead preserves the $SO(2)$ Noether momentum $J_{12}=L_{12}$, while $F_3$ remains nonsingular and $SO(2)$ invariant. Thus, writing $a_1=a_2=a\ne b=a_3$, $$\label{eq:double}
 \{J_{12},F_3\}_D=0,\qquad
 2H=a+J_{12}^2+(b-a)F_3.$$ This commuting pair is independent on a nonempty open set. Indeed, at $x=(3/5,0,4/5)$ and $p=(0,t,0)$, its differential determinant on the tangent variations $((-4/5,0,3/5),0)$ and $(0,(0,1,0))$ is $$-\frac{8\bigl(9(b-a)+25t^2\bigr)}{125(b-a)},$$ which is nonzero after avoiding the sole possible exceptional value of $t>0$. The other double faces follow by permutation. If $A=aI$, then $\dot p=-|p|^2x$: $p=0$ is the equilibrium sphere and $p\ne0$ is a great circle of least period $2\pi/|p|$.

Fix a positive Planck parameter $\hbar>0$. The canonical source quantization is $$\label{eq:quantum}
 \widehat H=-\frac{\hbar^2}{2}\Delta_{S^2}+\frac12x^TAx,
 \qquad D(\widehat H)=H^2(S^2)\subset L^2(S^2).$$ The round Laplacian is self-adjoint with compact resolvent, and the real smooth potential is bounded. The bounded-perturbation theorem preserves both properties. The excluded value $\hbar=0$ would instead require the maximal $L^2(S^2)$ domain for the bounded multiplication operator. No closed anisotropic spectrum is asserted.

# Evidence, sources, and Route-A boundary

The exact ledger has 60 rational tangent-state rows, 120 rational resolvent probes, 30 axial rows, 30 coordinate-face rows, and explicit axisymmetric and isotropic boundaries. A producer-independent checker recomputes every fraction. A separate symbolic lane expands the Poisson brackets, resolvent identity, and Lax equation. These receipts test implementation conventions; the preceding proof handles the continuum.

The nearest workspace owners are C186 Euler top, C244 spherical pendulum, C313 round-sphere geodesics, and C344 resonant-triad elliptic dynamics. None has this holonomic anisotropic sphere potential and its Uhlenbeck--resolvent generator.

The conservative tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ There is no rational-prime carrier, logarithmic-prime clock, target Euler factor, root number, automorphy, target divisor or functional equation, target-zero match, or Hilbert--Polya operator. Route A is rejected and Route B is false. This is the *boundary and route firewall* of the final revision.

# Source boundary {#source-boundary .unnumbered}

Neumann owns the original mechanical problem; Moser owns the modern quadrics/spectral lineage; Knoerrer owns the geodesic correspondence cited here. This convention-locked reconstruction makes no priority claim.

9 C. Neumann, "De problemate quodam mechanico, quod ad primam integralium ultraellipticorum classem revocatur," *J. Reine Angew. Math.* 56 (1859), 46--63, DOI [10.1515/crll.1859.56.46](https://doi.org/10.1515/crll.1859.56.46). J. Moser, "Geometry of Quadrics and Spectral Theory," in *The Chern Symposium 1979*, Springer (1980), 147--188, DOI [10.1007/978-1-4613-8109-9\_7](https://doi.org/10.1007/978-1-4613-8109-9_7). H. Knoerrer, "Geodesics on quadrics and a mechanical problem of C. Neumann," *J. Reine Angew. Math.* 334 (1982), 69--78, DOI [10.1515/crll.1982.334.69](https://doi.org/10.1515/crll.1982.334.69).
