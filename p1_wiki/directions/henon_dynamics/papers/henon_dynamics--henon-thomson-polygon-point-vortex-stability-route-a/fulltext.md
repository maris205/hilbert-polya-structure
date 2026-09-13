---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-thomson-polygon-point-vortex-stability-route-a"
canonical_tex: "henon_dynamics/henon_thomson_polygon_point_vortex_stability_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_thomson_polygon_point_vortex_stability_route_a/paper/main.pdf"
source_sha256: "de93f64650313aba7165de357edb6b799468cbd25e18e13ebbf0e50a0a735275"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Thomson Polygon from Its Cartesian Hessian: Exact Fourier Blocks and the Sharp Linear Stability Threshold

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_thomson_polygon_point_vortex_stability_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_thomson_polygon_point_vortex_stability_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_thomson_polygon_point_vortex_stability_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_thomson_polygon_point_vortex_stability_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For identical positive point vortices on a planar regular $N$-gon, we derive the rotating relative equilibrium directly from the logarithmic Hamiltonian and reduce its raw Cartesian Hessian by a vertexwise radial--tangential discrete Fourier transform. If $c=\Gamma/(4\pi R^2)$ and $q_m=m(N-m)$, the $m$th Hamiltonian block is $$c\begin{pmatrix}0&q_m\\-[2(N-1)-q_m]&0\end{pmatrix}.$$ Root-of-unity orthogonality proves this formula for every $N\ge3$. Consequently the symmetry-reduced polygon is linearly elliptic for $3\le N\le6$, linearly degenerate only in the conjugate modes $m=3,4$ when $N=7$, and hyperbolic for every $N\ge8$. \>0 We separate rotation, scale, translations, and the centered first-harmonic complement, and close the $\Gamma$, $R$, collision, and low-$N$ faces. \>1 An independent checker reconstructs every raw $2N\times2N$ Hessian for $3\le N\le64$; exact symbolic and mutation audits close the release. The heptagon statement is strictly linear. The result is a self-contained reconstruction of a classical owner theorem, not a claim of literature priority or nonlinear heptagon stability.
author:
- HCS Research Program
date: 2 September 2026
title: |
  The Thomson Polygon from Its Cartesian Hessian:\
  Exact Fourier Blocks and the Sharp Linear Stability Threshold
```

## Markdown 正文

# Frozen Hamiltonian and relative equilibrium

Let $z_j=(x_j,y_j)\in\mathbb R^2$ and give every vortex the same circulation $\Gamma>0$. We freeze the convention $$H(z)=-\frac{\Gamma^2}{2\pi}\sum_{j<k}\log|z_j-z_k|,
 \qquad
 \Gamma\dot z_j=\mathsf J\nabla_jH,
 \qquad
 \mathsf J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.                 \label{eq:model}$$ Thus $-\mathsf J$ generates counterclockwise rotation. Take $$a_j=R(\cos\theta_j,\sin\theta_j),\qquad
 \theta_j=\frac{2\pi j}{N},\qquad N\ge3,\quad R>0.          \label{eq:polygon}$$ Thomson [@Thomson1883] and Havelock [@Havelock1931] are cited as classical owners of the polygon and its linear-stability question. Cabral and Schmidt [@CabralSchmidt2000] provide later stability context, and Celli, Lacomba, and Pérez-Chavela [@Celli2011] document polygonal relative-equilibrium lineage. No calculation or proof below is outsourced to these sources, and no literature-priority claim is made.

The configuration [\[eq:polygon\]](#eq:polygon){reference-type="eqref" reference="eq:polygon"} is a relative equilibrium with $$\Omega=\frac{\Gamma(N-1)}{4\pi R^2}.                       \label{eq:omega}$$ For $G=H+(\Gamma\Omega/2)\sum_j|z_j|^2$, one has $\nabla G(a)=0$.

Differentiating [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"} gives $$\nabla_jH=-\frac{\Gamma^2}{2\pi}
 \sum_{k\ne j}\frac{z_j-z_k}{|z_j-z_k|^2}.$$ At $j=0$, each summand inside the sum has radial component $1/(2R)$; tangential components cancel between $k$ and $N-k$. Rotational covariance therefore gives $$\sum_{k\ne j}\frac{a_j-a_k}{|a_j-a_k|^2}
 =\frac{N-1}{2R^2}a_j.$$ Hence $\nabla_jH(a)=-\Gamma\Omega a_j$ with [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"}, proving both claims and the sign of rotation under [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"}.

The rotating-frame linearization is $$\mathcal L=\mathsf J_N\,\Gamma^{-1}D^2G(a),
 \qquad \mathsf J_N=\operatorname{diag}(\mathsf J,\ldots,\mathsf J).                           \label{eq:linearization}$$ All stability statements below refer to [\[eq:linearization\]](#eq:linearization){reference-type="eqref" reference="eq:linearization"}; they do not silently change the Hamiltonian or clock.

# Raw Cartesian Hessian and exact Fourier blocks

For $d\ne0$, put $$A(d)=\frac{\mathsf I}{|d|^2}-\frac{2dd^T}{|d|^4}.$$ The pairwise Cartesian blocks are $$D^2_{jj}H=-\frac{\Gamma^2}{2\pi}A(d_{jk}),
 \qquad
 D^2_{jk}H=+\frac{\Gamma^2}{2\pi}A(d_{jk}),                \label{eq:rawhessian}$$ and the augmentation adds $\Gamma\Omega\mathsf I$ to each diagonal block. Equation [\[eq:rawhessian\]](#eq:rawhessian){reference-type="eqref" reference="eq:rawhessian"}, rather than the final closed formula, is the starting point of the independent checker.

Let $Q_j$ have the radial and counterclockwise tangential unit vectors at $a_j$ as columns. Set $$c=\frac{\Gamma}{4\pi R^2},\qquad q_m=m(N-m),\qquad
 \sigma_m=2(N-1)-q_m.                                      \label{eq:notation}$$

In the local radial--tangential DFT, for every $m=0,\ldots,N-1$, $$\begin{aligned}
 \widehat{\Gamma^{-1}D^2G}_m
   &=c\operatorname{diag}(\sigma_m,q_m),                                  \label{eq:hblock}\\
 \mathcal L_m
   &=c\begin{pmatrix}0&q_m\\-\sigma_m&0\end{pmatrix},
 &\mathcal L_m^2&=-c^2q_m\sigma_m\mathsf I.                      \label{eq:lblock}\end{aligned}$$

For $k\ne0$, let $\theta=\theta_k$ and $d=a_0-a_k$. Since $|d|^2=4R^2\sin^2(\theta/2)$, substitution in $A(d)$ gives $$A(d)=\frac1{4R^2\sin^2(\theta/2)}
 \begin{pmatrix}\cos\theta&\sin\theta\\
                 \sin\theta&-\cos\theta\end{pmatrix}.$$ Multiplication by $Q_k$ turns the displayed matrix into $\operatorname{diag}(1,-1)$. Thus the local off-diagonal block in the first block row is $$B_k=\frac{c}{1-\cos\theta_k}\operatorname{diag}(1,-1).$$ If $A_N=\sum_{k=1}^{N-1}(1-\cos\theta_k)^{-1}$, the raw diagonal block is $B_0=c\operatorname{diag}(2(N-1)-A_N,A_N)$. Pairing $k$ with $N-k$ cancels the sine parts of the DFT and yields $$\widehat{\Gamma^{-1}D^2G}_m
 =c\operatorname{diag}(2(N-1)-S_m,S_m),
 \quad
 S_m=\sum_{k=1}^{N-1}
 \frac{1-\cos(m\theta_k)}{1-\cos\theta_k}.                 \label{eq:rootsum}$$

For $\zeta=e^{2\pi i/N}$, $$\frac{1-\cos(m\theta)}{1-\cos\theta}
 =\left|\sum_{r=0}^{m-1}e^{ir\theta}\right|^2.$$ Root-of-unity orthogonality therefore gives $$\sum_{k=0}^{N-1}\left|\sum_{r=0}^{m-1}\zeta^{kr}\right|^2=Nm.$$ The $k=0$ term is $m^2$, so $S_m=Nm-m^2=q_m$. This proves [\[eq:hblock\]](#eq:hblock){reference-type="eqref" reference="eq:hblock"}. The local rotations preserve $\mathsf J$; multiplying by $\mathsf J$ and squaring proves [\[eq:lblock\]](#eq:lblock){reference-type="eqref" reference="eq:lblock"}.

# The sharp linear threshold

After center, angular-impulse, and rotation reduction:

1.  every block is semisimple elliptic for $3\le N\le6$;

2.  for $N=7$, exactly $m=3,4$ are nonzero nilpotent blocks;

3.  every $N\ge8$ has a real hyperbolic pair.

The middle statement is linear degeneracy only; it does not assert nonlinear stability or instability of the heptagon.

For $m\ne0$, $q_m>0$, so [\[eq:lblock\]](#eq:lblock){reference-type="eqref" reference="eq:lblock"} is elliptic, nilpotent, or hyperbolic according as $\sigma_m$ is positive, zero, or negative. The maximum of $q_m$ is $\lfloor N^2/4\rfloor$. Hence the least sign is $$2(N-1)-\lfloor N^2/4\rfloor.$$ It is positive for $N=3,4,5,6$ and zero at $N=7$, where $m(7-m)=12$ only for $m=3,4$. For $N=2k\ge8$, $k^2-(4k-2)>0$; for $N=2k+1\ge9$, $k(k+1)-4k=k(k-3)>0$. Thus the maximal-$q_m$ block is hyperbolic from eight onward. The symmetry directions removed in the statement are identified explicitly below in the revised manuscript and do not alter these signs. \>1 The labels $m=3,4$ at $N=7$ are conjugate. On their real four-dimensional isotypic component, the zero eigenvalue has algebraic multiplicity four and geometric multiplicity two. This refines the linear degeneracy statement but does not supply a nonlinear conclusion.

  $N$             controlling $\sigma_m$   reduced linear type   strict boundary
  --------------- ------------------------ --------------------- --------------------
  $3$--$6$        positive                 elliptic              semisimple
  $7$             zero at $m=3,4$          degenerate            no nonlinear claim
  $8$ and above   negative for some $m$    hyperbolic            real pair

\>0

# Symmetry slice and parameter faces

The full Fourier ledger prevents symmetry modes from being mislabeled as instabilities. At $m=0$, $$\mathcal L_0=c\begin{pmatrix}0&0\\-2(N-1)&0\end{pmatrix}. \label{eq:mzero}$$ Uniform tangential displacement is rotation; uniform radial displacement is its scale generalized vector. Fixing angular impulse and quotienting rotation remove [\[eq:mzero\]](#eq:mzero){reference-type="eqref" reference="eq:mzero"}.

The conjugate first harmonics contain the translation plane. If local coordinates are $\xi_j,\eta_j$ and $w_j=\xi_j+i\eta_j$, then the center variation is $$\delta\!\left(\sum_jz_j\right)=\sum_je^{i\theta_j}w_j.$$ Fixing the center removes this complex translation plane. It does not remove the entire first-harmonic isotypic component: because $q_1=\sigma_1=N-1$, the Hessian there is the scalar $c(N-1)\mathsf I$ and its centered complementary plane remains elliptic with frequency $c(N-1)=\Omega$. The centered, fixed-impulse rotational slice therefore removes exactly the intended Euclidean and scale directions while retaining every genuine shape degree of freedom.

The physical parameter faces are also explicit.

-   $R=0$ is a logarithmic collision and is excluded. As $R\to\infty$, all frequencies vanish like $R^{-2}$ while the sign atlas remains fixed.

-   $\Gamma=0$ degenerates the weighted symplectic form; it is recorded only as a zero-velocity limit. Common $\Gamma<0$ reverses time and preserves all stability signs.

-   $N=1$ is trivial. After centering, $N=2$ has no reduced shape degree of freedom, so the theorem begins at $N=3$.

-   $N=7,m=3,4$ is an exact nonzero nilpotent face. A higher-order nonlinear conclusion would require a different theorem and is not inferred.

# Independent executable reconstruction

The finite certificate tests the derivation without pretending to prove it. The producer emits [\[eq:notation\]](#eq:notation){reference-type="eqref" reference="eq:notation"}--[\[eq:lblock\]](#eq:lblock){reference-type="eqref" reference="eq:lblock"} as exact integer cells. The checker shares no producer function: for each $N=3,\ldots,64$ it constructs [\[eq:rawhessian\]](#eq:rawhessian){reference-type="eqref" reference="eq:rawhessian"} in global Cartesian coordinates, verifies the augmented equilibrium, checks the complete $2N\times2N$ symmetry, rotates every block by the $Q_j$, verifies cyclicity, performs the DFT, and applies the raw Hessian and Hamiltonian linearization to explicit rotation, scale, translation, and centered first-harmonic vectors.

SymPy separately differentiates and transforms exact raw Hessians for $N=3,4,6$ and verifies the same slice actions. Its root-sum audit covers every one of the 2,077 archived mode cells by coefficient counting rather than by inserting the closed value. Two unrelated fresh output paths must reproduce the canonical JSON byte-for-byte. The checker rejects duplicate keys, nonstandard constants, unknown or missing fields, bool/type confusion, reordered or semantically duplicated rows, and all altered contract values, even when the payload hash is repaired.

\>1

# Receipt, ownership, and Route-A boundary

The deterministic receipt contains 2,077 exact mode rows, 62 polygon rows, 64 exact $\Gamma/R^2$ scale cells, seven symmetry-slice rows, and eight boundaries. The independent raw checker passes 65,655 assertions, the symbolic reconstruction passes 4,585 identities, the two-path replay is byte-exact, and 76/76 hostile specimens are rejected. The latter comprise 73 repaired-hash attacks plus stale-hash, raw duplicate-key, and nonstandard constant controls. The evidence SHA-256 begins `4fed9820df14c399` and ends `8123fcdfb39db9462a53`.

These counts are implementation evidence. The arbitrary-$N$ theorem rests on [\[eq:rootsum\]](#eq:rootsum){reference-type="eqref" reference="eq:rootsum"} and the exact maximum of $m(N-m)$, not on the cutoff at $N=64$. The source audit likewise separates lineage from proof: classical owners receive explicit attribution, while the workspace increment is only the convention-frozen synthesis and independently executable closure.

The honest Route-A evaluation is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}),
 \qquad \mathrm{ROUTE\_A\_REJECTED}.                        \label{eq:route}$$ The polygons provide a natural relative-periodic family, justifying only the weak A1 label. Their clock varies continuously with $\Gamma/R^2$; one symmetric family is not an isolated primitive-orbit census. There is no rational-prime carrier, logarithmic-prime clock, target determinant, target divisor, functional equation, target zero match, Hilbert--Pólya operator, or same-clock quantum lift. Route B is not authorized. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

The strict nonclaims are therefore substantive: no nonlinear stability result for the Thomson heptagon, no proof by finite enumeration, no literature priority claim, and no arithmetic or spectral-target bridge.

# Conclusion

The logarithmic pair Hessian and one root-of-unity sum determine every Fourier block of the equal-vortex polygon. Once rotation, scale, and translations are handled explicitly, the sign $2(N-1)-m(N-m)$ yields the exact reduced linear transition at seven and eight vortices. \>0 The parameter ledger prevents zero circulation, collision, infinite radius, or the first harmonics from being folded into the shape theorem. \>1 The executable audit reconstructs, rather than assumes, the Cartesian-to-DFT step. Its strongest limitation is intentional: linear degeneracy at $N=7$ is not promoted to a nonlinear statement, and classical reconstruction is not presented as new literature.

9 J. J. Thomson, *A Treatise on the Motion of Vortex Rings*, Macmillan, London (1883).

T. H. Havelock, "The stability of motion of rectilinear vortices in ring formation," *Philosophical Magazine* **11** (70), 617--633 (1931), [doi:10.1080/14786443109461714](https://doi.org/10.1080/14786443109461714).

H. E. Cabral and D. S. Schmidt, "Stability of relative equilibria in the problem of $N+1$ vortices," *SIAM J. Math. Anal.* **31** (2), 231--250 (2000), [doi:10.1137/S0036141098302124](https://doi.org/10.1137/S0036141098302124).

M. Celli, E. A. Lacomba, and E. Pérez-Chavela, "On polygonal relative equilibria in the $N$-vortex problem," *J. Math. Phys.* **52**, 103101 (2011), [doi:10.1063/1.3646115](https://doi.org/10.1063/1.3646115).
