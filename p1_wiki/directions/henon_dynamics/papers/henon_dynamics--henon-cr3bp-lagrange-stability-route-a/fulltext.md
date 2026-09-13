---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-cr3bp-lagrange-stability-route-a"
canonical_tex: "henon_dynamics/henon_cr3bp_lagrange_stability_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_cr3bp_lagrange_stability_route_a/paper/main.pdf"
source_sha256: "72fba939b9357f5d0f90ac1d6de4d82ac8ac0e1cb0a878d869b75ebfec536ffc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Five Lagrange Equilibria in the Planar CR3BP: Exact Linear Types and the Defective Routh Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_cr3bp_lagrange_stability_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_cr3bp_lagrange_stability_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_cr3bp_lagrange_stability_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_cr3bp_lagrange_stability_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the normalized planar circular restricted three-body problem with $0<\mu\leq1/2$, we derive all five equilibria and their complete linear spectral atlas. Each collinear point is uniquely located in its collision- free interval and is saddle--times--center. At the equilateral points the characteristic polynomial is $\lambda^4+\lambda^2+27\mu(1-\mu)/4$. Writing $\mu_R=(1-\sqrt{23/27})/2$, the linear flow is bounded elliptic below $\mu_R$ and has an unstable Hamiltonian quartet above it. At equality each of $\pm i/\sqrt2$ has algebraic multiplicity two and geometric multiplicity one: the linearization is defective, has linearly growing solutions, and is *not* stable. \>0 We keep collisions, the zero-mass limit, and nonlinear stability outside the claim and audit both signs of the triangular mixed Hessian entry. \>1 Independent raw-Jacobian, symbolic, replay, and hostile-mutation lanes close 38 finite regression cells without replacing the all-parameter proof.
author:
- 'Route-A source-local certificate HCS-C290'
date: 2 September 2026
title: |
  The Five Lagrange Equilibria in the Planar CR3BP:\
  Exact Linear Types and the Defective Routh Boundary
```

## Markdown 正文

trailerid \[\<C2902026090200000000000000000000\>\<C2902026090200000000000000000000\>\]

# Frozen normalization and claim level

The primaries of masses $1-\mu$ and $\mu$ occupy $(-\mu,0)$ and $(1-\mu,0)$ in the synodic frame. For $$r_1^2=(x+\mu)^2+y^2,\qquad
 r_2^2=(x-1+\mu)^2+y^2,$$ set $$\label{eq:potential}
 \Omega(x,y)=\frac{x^2+y^2}{2}+\frac{1-\mu}{r_1}+\frac{\mu}{r_2}.$$ The equations, including our Coriolis convention, are $$\label{eq:eom}
 \ddot x-2\dot y=\Omega_x,\qquad
 \ddot y+2\dot x=\Omega_y.$$ Both collision points are removed. "Linearly stable" below means that all solutions of the constant-coefficient variational equation are bounded, including at mass ratios where the two linear frequencies are resonant. It does not assert nonlinear stability, control resonance bifurcations, or invoke KAM theory.

The equilateral configuration goes back to Lagrange [@Lagrange1772]. Gascheau's 1843 thesis is the first historical owner of the Newtonian triangular stability criterion [@Gascheau1843]; Routh's 1874 paper gives a subsequent treatment and inverse-power-law generalization [@Routh1874]. A modern Hamiltonian treatment is given by Meyer, Hall, and Offin [@MHO2009]. Neither the five points nor the threshold is claimed as literature originality; all formulas needed for our convention are rederived here.

[\[thm:main\]]{#thm:main label="thm:main"} For every $0<\mu\leq1/2$, the collision-free plane has exactly five equilibria.

1.  There is exactly one collinear equilibrium in each interval $(-\infty,-\mu)$, $(-\mu,1-\mu)$, and $(1-\mu,\infty)$. Every one is of saddle--times--center type and is linearly unstable.

2.  The two remaining equilibria are $$L_{4,5}=\left(\frac12-\mu,\ \mathord\pm\frac{\sqrt3}{2}\right).$$ Their characteristic polynomial is $$\label{eq:trianglepoly}
     p_\mu(\lambda)=\lambda^4+\lambda^2+\frac{27}{4}\mu(1-\mu).$$ With $\mu_R=(1-\sqrt{23/27})/2$, their linearized flow is bounded for $0<\mu<\mu_R$, defective with linear growth (hence not stable) for $\mu=\mu_R$, and exponentially unstable for $\mu_R<\mu\leq1/2$.

At equality, each eigenvalue $\pm i/\sqrt2$ has algebraic multiplicity two and geometric multiplicity one.

# Why there are exactly five points

Define $$\label{eq:S}
 S(x,y)=\frac{1-\mu}{r_1^3}+\frac{\mu}{r_2^3}.$$ Direct differentiation gives $\Omega_y=y(1-S)$. Thus an equilibrium either has $y=0$ or satisfies $S=1$.

On the axis, put $$\label{eq:f}
 f_\mu(x)=x-(1-\mu)\frac{x+\mu}{|x+\mu|^3}
              -\mu\frac{x-1+\mu}{|x-1+\mu|^3}.$$ Away from collisions, $$\label{eq:monotone}
 f_\mu'(x)=1+2\left(\frac{1-\mu}{|x+\mu|^3}
                    +\frac{\mu}{|x-1+\mu|^3}\right)>0.$$ On $(-\infty,-\mu)$ its limiting signs are negative and positive; on $(-\mu,1-\mu)$ they are negative and positive; and on $(1-\mu,\infty)$ they are negative and positive. The intermediate value theorem and [\[eq:monotone\]](#eq:monotone){reference-type="eqref" reference="eq:monotone"} give precisely three roots.

If $y\ne0$, then $S=1$. Writing $u=r_1^{-3}$ and $w=r_2^{-3}$, a direct rearrangement yields $$\label{eq:offaxis}
 \Omega_x-x(1-S)=\mu(1-\mu)(w-u).$$ Because $0<\mu<1$, equilibrium implies $r_1=r_2$, hence $x=1/2-\mu$. Now $S=1$ becomes $r_1=r_2=1$, so $y^2=3/4$. These are exactly $L_4$ and $L_5$, proving the count.

# The raw rotating-frame determinant

At any equilibrium let $a=\Omega_{xx}$, $c=\Omega_{yy}$, and $d=\Omega_{xy}$. In coordinates $(\xi,\eta,u,w)=(\delta x,\delta y,\delta\dot x,\delta\dot y)$ the raw variational matrix is $$\label{eq:M}
 M=\begin{pmatrix}
 0&0&1&0\\0&0&0&1\\a&d&0&2\\d&c&-2&0
 \end{pmatrix}.$$ Expanding, without appealing to a stability label, $$\label{eq:generalpoly}
 \det(\lambda I-M)=
 \lambda^4+(4-a-c)\lambda^2+ac-d^2.$$

At a collinear root, $d=0$ and $$\label{eq:colhess}
 a=1+2S,\qquad c=1-S,$$ where now $S$ is [\[eq:S\]](#eq:S){reference-type="eqref" reference="eq:S"} at $y=0$. We verify $S>1$ on all three branches. Between the primaries, $r_1+r_2=1$, so $r_1,r_2<1$ and $S>(1-\mu)+\mu=1$. To the right, write $d=x-1+\mu>0$. At $d=\mu^{1/3}$, equation [\[eq:f\]](#eq:f){reference-type="eqref" reference="eq:f"} becomes $$f_\mu=(1-\mu)\{1-(1+d)^{-2}\}>0.$$ Since $f_\mu$ is increasing in $x$ and tends to $-\infty$ at the right side of the collision, its root has $d<\mu^{1/3}$; hence $S>\mu/d^3>1$. To the left, put $d=-x-\mu>0$. At $d=(1-\mu)^{1/3}$ one obtains $$f_\mu=-\mu\{1-(1+d)^{-2}\}<0.$$ Here increasing $d$ decreases $x$, so the root has $d<(1-\mu)^{1/3}$ and $S>(1-\mu)/d^3>1$. Substitution in [\[eq:generalpoly\]](#eq:generalpoly){reference-type="eqref" reference="eq:generalpoly"} gives $$\label{eq:colpoly}
 \lambda^4+(2-S)\lambda^2+(1+2S)(1-S).$$ Its constant term is negative. The two roots in $z=\lambda^2$ have opposite signs, so there is one real pair and one imaginary pair. This proves the collinear assertion.

At either triangular point direct differentiation of [\[eq:potential\]](#eq:potential){reference-type="eqref" reference="eq:potential"} gives $$\label{eq:trihess}
 a=\frac34,\qquad c=\frac94,\qquad
 d=\mathord\pm\frac{3\sqrt3}{4}(1-2\mu).$$ Thus $a+c=3$ and $ac-d^2=27\mu(1-\mu)/4$, proving [\[eq:trianglepoly\]](#eq:trianglepoly){reference-type="eqref" reference="eq:trianglepoly"} for both $L_4$ and $L_5$.

# Open chambers and the critical Jordan structure

Set $z=\lambda^2$. The two roots of [\[eq:trianglepoly\]](#eq:trianglepoly){reference-type="eqref" reference="eq:trianglepoly"} are $$\label{eq:zroots}
 z_\pm=\frac{-1\pm\sqrt{1-27\mu(1-\mu)}}{2}.$$ On $(0,1/2]$, the expression $27\mu(1-\mu)$ is strictly increasing until the included endpoint and equals one precisely at $\mu_R$. Below $\mu_R$, both $z_\pm$ are distinct and negative, giving four distinct imaginary eigenvalues and a bounded diagonalizable linear flow. Above it, the $z$ roots are nonreal conjugates; their square roots form a quartet $\{\pm\alpha\pm i\beta\}$ with $\alpha,\beta>0$, giving exponential growth.

At equality, $$\label{eq:criticalpoly}
 p_{\mu_R}(\lambda)=(\lambda^2+\tfrac12)^2.$$ Algebraic multiplicity is not enough to decide boundedness. For an eigenvalue $\lambda$, the position components solve $$\label{eq:pencil}
 \begin{pmatrix}
 \lambda^2-a&-2\lambda-d\\2\lambda-d&\lambda^2-c
 \end{pmatrix}\binom{\xi}{\eta}=0.$$ At $\lambda=\pm i/\sqrt2$ the determinant vanishes. The matrix cannot be zero: its two off-diagonal entries would imply simultaneously $2\lambda=-d$ and $2\lambda=d$, hence $\lambda=0$. Therefore it has rank one and a one-dimensional kernel. Velocities are then uniquely $(u,w)=\lambda(\xi,\eta)$, so each eigenspace of $M$ has dimension one. Each double eigenvalue consequently has a nontrivial size-two Jordan block. The exponential contains $t e^{\pm it/\sqrt2}$ terms and is unbounded. This proves the critical statement and, in particular, excludes linear stability.

\>0

# Boundary ledger and interpretation

The lower mass boundary $\mu=0$ is excluded for a geometric reason, not merely to avoid division by a parameter. Then $\Omega=(x^2+y^2)/2+(x^2+y^2)^{-1/2}$ and $\nabla\Omega=(1-r^{-3})(x,y)$, so the entire unit circle is a continuum of equilibria. The five-isolated-point theorem cannot extend to that face.

The endpoint $\mu=1/2$ is included. The two triangular points persist, but $27\mu(1-\mu)>1$, so they lie in the quartet chamber. At all positive mass ratios the primary positions remain singular and are not silently counted as solutions of $\nabla\Omega=0$.

For $0<\mu<\mu_R$, "bounded elliptic" is exactly a statement about the constant linear system $\dot z=Mz$ and remains true at resonant mass ratios in that open chamber. The theorem does not resolve the nonlinear consequences of resonance, construct Lyapunov periodic families, or prove nonlinear/KAM stability. At $\mu_R$, even the linear boundedness statement fails because of the Jordan factor. Calling equality "spectrally stable" without this qualification would conceal real linear growth and is not done here.

# Two sign checks for the triangular pair

Reflection $(x,y)\mapsto(x,-y)$ takes $L_4$ to $L_5$. It fixes the diagonal Hessian entries and reverses $d$ in [\[eq:trihess\]](#eq:trihess){reference-type="eqref" reference="eq:trihess"}. Formula [\[eq:generalpoly\]](#eq:generalpoly){reference-type="eqref" reference="eq:generalpoly"} depends on $d^2$, so both points share the same eigenvalues. This is more than a symmetry slogan: the executable checker constructs both raw matrices for every tested $\mu$, and the symbolic lane differentiates [\[eq:potential\]](#eq:potential){reference-type="eqref" reference="eq:potential"} at both signs independently.

\>1

# Executable evidence and adversarial closure

The canonical evidence uses eight rational masses $$\frac1{1000},\frac1{100},\frac1{50},\frac1{30},
 \frac1{25},\frac1{10},\frac14,\frac12.$$ They give eight paired triangular cells and 24 collinear-root cells, plus one exact algebraic critical cell and five explicit boundaries, for 38 cells. The producer uses high-precision root finding. The checker imports no producer code: it bisects each collision-free interval independently, reconstructs [\[eq:M\]](#eq:M){reference-type="eqref" reference="eq:M"}, and verifies the raw determinant and spectrum. It tests both signs of $d$ for every triangular mass and computes all four exact critical ranks---$L_4$ and $L_5$ at both $\lambda=\pm i/\sqrt2$---over $\mathbb Q(\sqrt{23/27},i\sqrt2)$.

A separate SymPy lane differentiates the potential rather than copying the stored Hessian. Two isolated producer paths must agree byte-for-byte with the archive. The strict JSON loader rejects duplicate keys before hashing. The 65/65 hostile suite includes repaired-hash theorem, proof, row, scope, grid, source, and four-critical-rank attacks; boolean--integer substitutions in Route B, critical counts, multiplicities, defect, growth, and stability are rejected by exact-type checks. Its strict YAML lane rejects unknown, missing, duplicate, merge/anchor, type, tuple, scope, and Route-B changes. A stale-hash control is separate. These finite checks validate the implementation; the preceding analysis proves the theorem for every allowed $\mu$.

# Route-A audit, limitations, and declarations

The frozen tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),$$ with overall `ROUTE_A_REJECTED`. The equilibria are constant orbits and this paper proves no intrinsic primitive-period family, so A1 is FAIL. Hamiltonian form motivates only a formal A4 hint. There is no arithmetic local data, Euler factor, root number, automorphy, target divisor or counting law, target functional equation, target zero match, or target Hilbert--Pólya operator. Route B is false. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Limitations.

We treat planar, circular, normalized CR3BP equilibria and their linearized flow only. Spatial motion, eccentric primaries, collision regularization, periodic-orbit families, nonlinear stability, and transport are outside scope.

#### Data and code availability.

The canonical evidence, independent checker, symbolic reconstruction, replay, mutations, LaTeX source, and release manifest are included in the package; no external dataset is required.

#### Ethics, conflicts, and funding.

No human participants, animals, or personal data were involved. The author declares no conflict of interest and no external funding.

#### CRediT and AI-use statement.

The package author performed conceptualization, formal analysis, software, validation, writing, and reproducibility curation. An AI language model assisted drafting and code generation; all claims remain the author's responsibility and are exposed to the recorded checks.

9 J.-L. Lagrange, *Essai sur le Problème des trois Corps*, Prix de l'Académie royale des sciences de Paris, tome IX (1772); Oeuvres, tome VI, 229--331. [digitized transcription](https://fr.wikisource.org/wiki/M%C3%A9moires_extraits_des_recueils_de_l%E2%80%99Acad%C3%A9mie_des_sciences_de_Paris_et_de_l%E2%80%99Institut_de_France/Essai_sur_le_Probl%C3%A8me_des_trois_Corps).

G. Gascheau, *Mouvements relatifs d'un système de corps*, thèse de mécanique, Faculté des sciences de Paris, Bachelier, 1843, 36 pp. and plate. [BnF Gallica ark:/12148/bpt6k5789653w](https://gallica.bnf.fr/ark:/12148/bpt6k5789653w).

E. J. Routh, *On Laplace's Three Particles, with a Supplement on the Stability of Steady Motion*, Proc. London Math. Soc. s1-6 (1874), 86--97. [doi:10.1112/plms/s1-6.1.86](https://doi.org/10.1112/plms/s1-6.1.86).

K. R. Meyer, G. R. Hall, and D. Offin, *Introduction to Hamiltonian Dynamical Systems and the N-Body Problem*, 2nd ed., Springer, 2009. [doi:10.1007/978-0-387-09724-4](https://doi.org/10.1007/978-0-387-09724-4).
