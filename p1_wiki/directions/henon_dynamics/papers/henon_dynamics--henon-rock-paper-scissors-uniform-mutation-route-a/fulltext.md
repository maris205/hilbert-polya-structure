---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-rock-paper-scissors-uniform-mutation-route-a"
canonical_tex: "henon_dynamics/henon_rock_paper_scissors_uniform_mutation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_rock_paper_scissors_uniform_mutation_route_a/paper/main.pdf"
source_sha256: "37f94d52ea81a06830bc3cc50ae9aa75cb43d170facd6604279ccf7ca953e5d1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uniform Mutation in a Three-Strategy Rock--Paper--Scissors Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_rock_paper_scissors_uniform_mutation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_rock_paper_scissors_uniform_mutation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_rock_paper_scissors_uniform_mutation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_rock_paper_scissors_uniform_mutation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a convention-complete theorem for the cyclic three-strategy flow $$\dot x=ax(y-z)+\mu(1/3-x),\qquad\text{cyclically in }(x,y,z),
   \qquad a,\mu\geq0,$$ on the unit simplex. At zero mutation and positive cyclic rate, the product $H=xyz$ is conserved: every regular interior level is one periodic orbit, the boundary is a cyclic heteroclinic network, and the physical period has an exact turning-point quadrature with center limit $2\pi\sqrt3/a$. Positive additive uniform mutation points inward, makes $\log H$ a strict Lyapunov function, and gives global convergence to the barycenter; the tangent rates are $-\mu\pm ia/\sqrt3$. We close the exactly solvable $a=0$ contraction and identity faces and keep finite numerical rows separate from the theorem. This is a source-local population-flow result: there is no arithmetic owner, target determinant, or Hilbert--Pólya claim.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Uniform Mutation in a Three-Strategy Rock--Paper--Scissors Flow'
```

## Markdown 正文

suppressoptionalinfo 611

# Model and simplex geometry

Let $$\Delta=\{(x,y,z)\in\mathbb R^3:x,y,z\ge0,\ x+y+z=1\}.$$ The vector field is $$F_{a,\mu}(x,y,z)=\bigl(ax(y-z)+\mu(1/3-x),
 ay(z-x)+\mu(1/3-y),
 az(x-y)+\mu(1/3-z)\bigr). \tag{1}$$ The cyclic terms cancel, hence $\dot x+\dot y+\dot z=0$. On a coordinate face and $\mu=0$ the face is invariant. If $\mu>0$, a zero coordinate has derivative $\mu/3$, so every trajectory enters the open simplex immediately. The barycenter $b=(1/3,1/3,1/3)$ is fixed for all parameters.

For $\mu=0$, $H=xyz$ is constant. If $a>0$, the barycenter is the only interior equilibrium, every level $0<h<1/27$ is a single regular periodic orbit, and as $h\downarrow0$ its closure tends to the three-edge heteroclinic network. If $a=0$, the flow is the identity instead.

On the interior, $$\frac{d}{dt}\log H=a[(y-z)+(z-x)+(x-y)]=0. \tag{2}$$ The equations $y+z=1-x$ and $yz=h/x$ have two distinct roots except at the barycenter. Consequently the compact positive level is a one-dimensional regular component. For $a>0$, the cyclic orientation of (1) gives a nonvanishing vector field on it, hence one periodic orbit. Setting one coordinate to zero gives the invariant edges and their cyclic connections; these are the $h=0$ boundary limit. For $a=0$ every point is fixed, as also follows directly from (1).

# Exact physical period

Assume $a>0$. From the two-root relation, $$(y-z)^2=(1-x)^2-\frac{4h}{x}.$$ Let $x_-<1/3<x_+$ be the physical roots of $$x(1-x)^2=4h,\qquad 0<h<1/27. \tag{3}$$ The two signs of $y-z$ traverse the closed level, so its exact period is $$T(h)=\frac2a\int_{x_-}^{x_+}
 \frac{dx}{x\sqrt{(1-x)^2-4h/x}}. \tag{4}$$ The cubic has a third root $x_3=2-x_--x_+>1$. With $$x(\theta)=\frac{x_-+x_+}{2}+\frac{x_+-x_-}{2}\sin\theta,
 \qquad -\frac\pi2\le\theta\le\frac\pi2,$$ the endpoint cosine cancels exactly and (4) becomes $$T(h)=\frac2a\int_{-\pi/2}^{\pi/2}
 \frac{d\theta}{\sqrt{x(\theta)\,[x_3-x(\theta)]}}. \tag{5}$$ This regular integral is the deterministic representation used by the ledger.

For $a>0$, $T(h)\to2\pi\sqrt3/a$ as $h\uparrow1/27$, while $T(h)\to+\infty$ as $h\downarrow0$.

At the center, both physical roots approach $1/3$ and $x_3$ approaches $4/3$; dominated convergence in (5) gives the displayed constant. At the lower endpoint, the factor $x(\theta)^{-1/2}$ develops a divergent integral, which is the familiar slowing near the heteroclinic edges.

# Uniform mutation and convergence

For $\mu>0$ and every interior point, $$\frac{d}{dt}\log(xyz)=\frac\mu3\left(\frac1x+\frac1y+\frac1z-9\right)\ge0, \tag{6}$$ with equality exactly at $b$. Every solution from $\Delta$ converges to $b$; there is no nonconstant recurrent trajectory.

The reciprocal AM--HM inequality and $x+y+z=1$ give $1/x+1/y+1/z\ge9$, with equality only when all coordinates are equal. A boundary initial condition enters the interior for positive time, after which $H>0$ and (6) applies. The compact positively invariant simplex supplies a nonempty omega-limit set. LaSalle's invariance principle puts it in the zero-derivative set, which is the singleton $\{b\}$.

At $b$, the ambient Jacobian has characteristic polynomial $$(\lambda+\mu)\left((\lambda+\mu)^2+\frac{a^2}{3}\right).$$ Thus the tangent-plane eigenvalues are $-\mu\pm ia/\sqrt3$. The imaginary part is the residual cyclic rotation; the negative real part is supplied only by the uniform mutation term.

\>0

# Degenerate faces and finite receipt

When $a=0$, the three coordinates decouple: $$x_i(t)=\frac13+\bigl(x_i(0)-\tfrac13\bigr)e^{-\mu t}. \tag{7}$$ When $a=\mu=0$, (1) is the identity on all of $\Delta$. For $\mu=0,a>0$, the edges remain invariant and the interior period family above is the whole recurrence statement. We make no extension to a general mutation matrix.

The receipt fixes three positive conservative rates, five rational product levels, three center-limit rows, six mutation starts (including all three coordinate boundaries), three exact contractions, and four tangent spectra. Fixed-step RK4 rows are explicitly labelled diagnostics. The independent checker does not import the producer; SymPy checks sixteen identities, byte replay uses two fresh temporary trees, and the hostile suite rejects 25/25 mutations, including a repaired-hash attempt to erase the positive-rate condition.

\>1

# Route-A boundary and audit supplement

The flow has no intrinsic rational-prime carrier, no prime-power repetition clock, no weighted primitive-orbit product, and no target divisor. Its finite periods are physical ODE periods on a continuum and are not an Artin--Mazur zeta. Accordingly the strict tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_WEAK},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),$$ with `ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.

The algebraic AM--HM remainder used by the checker is $$\frac1x+\frac1y+\frac1z-\frac9{x+y+z}
 =\frac{(x-y)^2z+(y-z)^2x+(z-x)^2y}{xyz(x+y+z)}\ge0.$$ The finite rows certify implementation identities and mass closure; they do not replace the compactness/LaSalle proof or establish any external spectral matching. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

9 R. M. May and W. J. Leonard, Nonlinear aspects of competition between three species, *SIAM Journal on Applied Mathematics* 29, 243--253 (1975). This citation supplies cyclic-competition context only; the frozen model here is the additive-uniform-mutation replicator field. J. Hofbauer and K. Sigmund, *Evolutionary Games and Population Dynamics*, Cambridge University Press (1998). J. P. LaSalle, Some extensions of Liapunov's second method, *IRE Transactions on Circuit Theory* 7 (1960).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, target-zero, determinant-matching, or Hilbert--Pólya claim. **Data and code.** All rows and audits accompany HCS-C235. This is not external peer review. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checks displayed formulas and metadata.
