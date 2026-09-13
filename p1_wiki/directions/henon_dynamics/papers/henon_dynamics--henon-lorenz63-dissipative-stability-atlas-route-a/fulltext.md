---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-lorenz63-dissipative-stability-atlas-route-a"
canonical_tex: "henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/paper/main.pdf"
source_sha256: "03e8d77c56a40592a79ac4b52e6a7cb7dd09d4a0443e9d65a9718feca7e490ed"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Global Dissipativity and Equilibrium-Stability Atlas for Lorenz--63

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close an all-parameter theorem for the Lorenz--63 equations rather than infer a parameter continuum from the familiar numerical attractor. For every $\sigma,\beta>0$ and $\rho\in\mathbb R$, a shifted quadratic form gives an exact dissipation ledger, a global forward bound, and an explicit absorbing ellipsoid. We list every equilibrium, factor the origin spectrum, and reduce the symmetric wings' cubic Routh--Hurwitz condition to one affine margin. This yields the exact stability split and, when $\sigma>\beta+1$, the surface $\rho_H=\sigma(\sigma+\beta+3)/(\sigma-\beta-1)$ with its imaginary frequency. Zero $\sigma$, zero $\beta$, their intersection, and the $\rho=1$ merger are resolved as separate singular faces. Only equilibrium and linear stability are claimed: neither nonlinear Hopf criticality nor universal chaos above $\rho_H$ is inferred. Independent exact reconstruction, symbolic checks, canonical replay, and hostile mutations audit the result.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'A Global Dissipativity and Equilibrium-Stability Atlas for Lorenz--63'
```

## Markdown 正文

suppressoptionalinfo 611

# Convention and global dissipativity

We freeze the Lorenz--63 system $$\dot x=\sigma(y-x),\qquad
 \dot y=x(\rho-z)-y,\qquad
 \dot z=xy-\beta z,                                  \tag{1}$$ on $\mathbb R^3$, with $\sigma,\beta>0$, $\rho\in\mathbb R$, and physical time $t$. It is equivariant under $(x,y,z)\mapsto(-x,-y,z)$, and its divergence is $-(\sigma+\beta+1)$. Volume contraction alone will not be used as a dissipativity proof.

[\[thm:absorb\]]{#thm:absorb label="thm:absorb"} Let $c=\rho+\sigma$, $$V=x^2+y^2+(z-c)^2,\qquad
 \kappa=\min\{2\sigma,2,\beta\}.$$ Every solution of (1) is global forward and $$\begin{aligned}
 \dot V
 &=-2\sigma x^2-2y^2-\beta z^2-\beta(z-c)^2+\beta c^2
                                                        \tag{2}\\
 &\le -\kappa V+\beta c^2,                              \tag{3}\\
 V(t)&\le e^{-\kappa t}V(0)+\frac{\beta c^2}{\kappa}
                    (1-e^{-\kappa t}).                  \tag{4}\end{aligned}$$ Hence every ellipsoid $V\le R$ with $R>\beta c^2/\kappa$ absorbs every trajectory.

Differentiate $V$ along (1). The $xyz$ terms cancel, while the remaining $xy$ coefficient vanishes because $c=\rho+\sigma$. The last term is closed by $$-2\beta z(z-c)=-\beta z^2-\beta(z-c)^2+\beta c^2,$$ which proves (2) and (3). Gronwall's inequality gives (4). The vector field is polynomial, so a maximal finite-time solution could fail only by escaping every bounded set; (4) excludes that. On $V=R>\beta c^2/\kappa$, (3) points strictly inward, and (4) gives eventual entry.

# Equilibria and exact characteristic polynomials

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} The origin $O$ exists for all $\rho$ and has $$\chi_O(\ell)=(\ell+\beta)
 [\ell^2+(\sigma+1)\ell+\sigma(1-\rho)].               \tag{5}$$ It is asymptotically stable for $\rho<1$, nonhyperbolic at $\rho=1$, and a saddle for $\rho>1$. If and only if $\rho>1$, there are two further equilibria $$E_\pm=(\pm\sqrt{\beta(\rho-1)},
        \pm\sqrt{\beta(\rho-1)},\rho-1),                \tag{6}$$ with common polynomial $$\chi_E(\ell)=\ell^3+(\sigma+\beta+1)\ell^2
 +\beta(\sigma+\rho)\ell+2\sigma\beta(\rho-1).         \tag{7}$$

The equilibrium equations give $y=x$, $xy=\beta z$, and $x(\rho-z-1)=0$, proving the list. Substitution in $$Df=\begin{pmatrix}-\sigma&\sigma&0\\
 \rho-z&-1&-x\\y&x&-\beta\end{pmatrix}$$ gives (5) and (7). The quadratic Routh criterion in (5) gives the origin classification.

\>0

# The wing stability surface

For the cubic (7), all coefficients are positive when $\rho>1$. The remaining Routh--Hurwitz condition is $$\begin{aligned}
 D&=(\sigma+\beta+1)(\sigma+\rho)-2\sigma(\rho-1)\\
  &=\sigma(\sigma+\beta+3)+(\beta+1-\sigma)\rho.
\end{aligned}                                           \tag{8}$$

[\[prop:hopf\]]{#prop:hopf label="prop:hopf"} If $\sigma\le\beta+1$, both wings are asymptotically stable for every $\rho>1$. If $\sigma>\beta+1$, define $$\rho_H=\frac{\sigma(\sigma+\beta+3)}
                 {\sigma-\beta-1}.                     \tag{9}$$ Then $\rho_H>1$; the wings are stable for $1<\rho<\rho_H$, lie on a linear Hopf boundary at equality, and are unstable for $\rho>\rho_H$. At equality, $$\chi_E(\ell)=(\ell+\sigma+\beta+1)
 [\ell^2+\beta(\sigma+\rho_H)],                         \tag{10}$$ so the crossing pair is $\ell=\pm i\sqrt{\beta(\sigma+\rho_H)}$.

Equation (8) is positive for all $\rho>1$ when its slope is nonnegative. For negative slope it has the unique zero (9), and $$(\rho_H-1)(\sigma-\beta-1)
   =(\sigma+1)(\sigma+\beta+1)>0.$$ The cubic Routh--Hurwitz criterion gives the sign classification. Substituting (9) into (7) gives (10). This is a linear spectral crossing; its nonlinear criticality is not part of the proposition.

# Singular parameter faces

The strict positivity assumption is structural. If $\sigma=0$ and $\beta>0$, $x=s$ is constant and the equilibria form $$E_s=\left(s,\frac{\beta\rho s}{\beta+s^2},
                 \frac{\rho s^2}{\beta+s^2}\right),
 \qquad
 \chi_s=\ell[\ell^2+(1+\beta)\ell+\beta+s^2].          \tag{11}$$ If $\beta=0$ and $\sigma>0$, the equilibria are $(0,0,z_0)$ and $$\chi_{z_0}=\ell[\ell^2+(\sigma+1)\ell
                    +\sigma(1-\rho+z_0)].              \tag{12}$$ They are transversely stable for $z_0>\rho-1$, saddles for $z_0<\rho-1$, and nonhyperbolic at equality. At $\sigma=\beta=0$ the equilibrium set is the union of $(0,0,z)$ and $(x,0,\rho)$. The tangent zero roots make clear why these faces are not silently included in Theorem [\[thm:absorb\]](#thm:absorb){reference-type="ref" reference="thm:absorb"}. At $\rho=1$, (6) merges with the origin; we claim the resulting nonhyperbolic boundary, not a center-manifold normal form.

# Source and claim boundary

Lorenz [@lorenz1963] introduced (1). Pade, Rauh and Tsarouhas [@pade1986] treat nonlinear Hopf direction, which is outside our theorem. Tucker [@tucker2002] and Guckenheimer--Williams [@gw1979] give rigorous classical-parameter and geometric-attractor context. We do not extrapolate those results to a global chaos classification: above $\rho_H$ the proved statement is linear instability of $E_\pm$, no more.

\>1

# Reproducible audit and Route-A result

The canonical ledger contains ten exact rational parameter rows spanning both sides of two Hopf points, the $\rho=1$ merger, a no-finite-Hopf regime and negative $\rho$. Five rational phase-space rows verify (2) through two independently written expressions. A producer-independent checker makes 231 assertions, SymPy reconstructs 14 generic identities, clean-process replay is byte identical, and 17 of 17 stale-hash, repaired-hash, schema, provenance and scope mutations are rejected. Finite rows audit formulas proved above; they do not establish a continuum by sampling.

The strict Route-A tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_FAIL},\mathtt{A2\_FAIL},
  \mathtt{A3\_FAIL},\mathtt{A4\_FAIL}),$$ with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. The model has no intrinsic rational-prime carrier or complete primitive-orbit ledger. Its finite Jacobian polynomials are not an orbit zeta or target Fredholm determinant; no target continuation, divisor, counting law, or natural unitary lift is constructed.

9 E. N. Lorenz, *Deterministic Nonperiodic Flow*, Journal of the Atmospheric Sciences 20 (1963), 130--141. [DOI link](https://doi.org/10.1175/1520-0469(1963)020%3C0130%3ADNF%3E2.0.CO%3B2). J. Pade, A. Rauh and G. Tsarouhas, *Analytical investigation of the Hopf bifurcation in the Lorenz model*, Physics Letters A 115 (1986), 93--96. DOI: 10.1016/0375-9601(86)90031-9. W. Tucker, *A Rigorous ODE Solver and Smale's 14th Problem*, Foundations of Computational Mathematics 2 (2002), 53--117. DOI: 10.1007/s002080010018. J. Guckenheimer and R. F. Williams, *Structural stability of Lorenz attractors*, Publications Mathématiques de l'IHÉS 50 (1979), 59--72. DOI: 10.1007/BF02684769.

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, target-zero, global-chaos, or Hilbert--Pólya claim. **Data and code.** The exact ledger and all audit programs accompany HCS-C227. **AI-use disclosure.** Generative tools assisted drafting and code generation; the released internal checks validate the displayed identities and metadata. This is not external peer review.
