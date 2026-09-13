---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-three-disk-open-billiard-route-a"
canonical_tex: "henon_dynamics/henon_three_disk_open_billiard_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_three_disk_open_billiard_route_a/paper/main.pdf"
source_sha256: "12706bb598c2dd03981526546115f3e8771bb76d23a53e0aeda3412423e2455e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Convex Coding and Hyperbolic Ledgers for the Equilateral Three-Disk Open Billiard

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_three_disk_open_billiard_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_three_disk_open_billiard_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_three_disk_open_billiard_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_three_disk_open_billiard_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Three equal circular obstacles of radius $r$ have centers at an equilateral triangle of side $d$. In the sharp strict no-eclipse chamber $d>4r/\sqrt3$, we prove that cyclically reduced cyclic classes are in bijection with periodic-ray iterates---primitive oriented geometric rays paired with positive traversal multiplicities. Primitive classes give unique non-grazing, isolated, hyperbolic primitive rays. =0 The proof uses compact convex minimization, not a finite orbit search. \>0 We derive the all-period primitive ledger, time reversal, length bounds, and positive determinant-one optical monodromy. \>1 We also give a sharp boundary atlas and a deterministic evidence certificate, while separating the source-local collision zeta from every target arithmetic or spectral claim.
author:
- 'Route-A source-local certificate HCS-C294'
date: 2 September 2026
title: |
  Exact Convex Coding and Hyperbolic Ledgers\
  for the Equilateral Three-Disk Open Billiard
```

## Markdown 正文

trailerid \[\<C2942026090200000000000000000000\>\<C2942026090200000000000000000000\>\]

# Model, conventions, and No-eclipse geometry

Let $c_0,c_1,c_2\in\mathbb R^2$ be the vertices of an equilateral triangle of side $d$, and let $$K_i=\{x\in\mathbb R^2:|x-c_i|\le r\},\qquad i=0,1,2.$$ The billiard moves at unit speed in the complement of the interiors of the $K_i$ and reflects specularly. We sample immediately after each collision, so the clock is one bounce. Rays are oriented; changing the initial collision only cyclically shifts the itinerary. Time reversal is not quotiented.

A cyclic word $w=(i_0,\ldots,i_{n-1})$ is *reduced* when $i_j\ne i_{j+1}$, including $i_{n-1}\ne i_0$. It is primitive when it is not a proper power. Every cyclic class has a unique form $[w]=[u^m]$ with $[u]$ primitive and $m\ge1$. A *periodic-ray iterate* is a primitive oriented geometric ray paired with its positive traversal multiplicity $m$. Length-one reduced words do not exist.

[\[lem:gap\]]{#lem:gap label="lem:gap"} The convex hull of either two disks is disjoint from the third disk exactly when $$d>\frac{4r}{\sqrt3}.$$ In that chamber the separation is $\sqrt3d/2-2r>0$.

The convex hull of two radius-$r$ disks is the closed radius-$r$ neighborhood of their center segment. The third center has distance $\sqrt3d/2$ from that segment. Removing the capsule radius and the third-disk radius leaves $\sqrt3d/2-2r$, proving both assertions.

# Convex variational coding

For a reduced word $w$, put $X_w=\prod_{j=0}^{n-1}K_{i_j}$ and, with cyclic indices, define $$\label{eq:length}
 \mathcal L_w(q_0,\ldots,q_{n-1})
   =\sum_{j=0}^{n-1}|q_{j+1}-q_j|.$$

[\[thm:coding\]]{#thm:coding label="thm:coding"} Assume $r>0$ and $d>4r/\sqrt3$. Cyclically reduced cyclic classes are in bijection with periodic-ray iterates. If $[w]=[u^m]$, its image is the $m$-fold traversal of the unique primitive oriented exterior ray coded by $[u]$. Every such geometric support is non-grazing, isolated, and hyperbolic, and $$[w]\longmapsto[\operatorname{rev}(w)]$$ is the time-reversal involution.

The continuous convex functional [\[eq:length\]](#eq:length){reference-type="eqref" reference="eq:length"} attains a minimum on the compact convex set $X_w$. Fix a minimizing vertex $q_j$. If it were in the interior of $K_{i_j}$, then it would minimize $|x-q_{j-1}|+|q_{j+1}-x|$ without a local constraint. Equality in the triangle inequality places every such minimizer on $[q_{j-1},q_{j+1}]$. That segment lies in the convex hull of one or two disks other than $K_{i_j}$ and is disjoint from $K_{i_j}$ by Lemma [\[lem:gap\]](#lem:gap){reference-type="ref" reference="lem:gap"}, a contradiction. Thus all vertices lie on their assigned circles.

Suppose $q$ and $q'$ were distinct minimizers. Convexity makes $(q+q')/2$ another minimizer. At a coordinate where they differ, strict convexity of the disk puts the midpoint in its interior, contradicting the preceding paragraph. The minimizer is therefore unique.

At a minimizing boundary vertex, the tangential part of $$\frac{q_j-q_{j-1}}{|q_j-q_{j-1}|}
 -\frac{q_{j+1}-q_j}{|q_{j+1}-q_j|}$$ vanishes. The normal multiplier is nonzero: if it vanished, the two unit vectors would agree and $q_j$ would lie between its neighbors, again contradicting no-eclipse. The incoming and outgoing tangential components therefore agree and their nonzero normal components are opposite. This is precisely non-grazing specular reflection. The supporting half-plane at an endpoint keeps a flight out of its endpoint disks, and Lemma [\[lem:gap\]](#lem:gap){reference-type="ref" reference="lem:gap"} keeps it out of the remaining disk. Hence the minimizing polygon is a physical exterior ray.

Conversely, the reflection law and the exterior orientation give the normal multiplier with the minimizing sign. They are the first-order optimality conditions for the convex functional on $X_w$, and hence are sufficient for global minimality. Uniqueness identifies every coded iterate with the constructed minimizer. If $w=u^m$, shifting the minimizing tuple by $|u|$ coordinates preserves $X_w$ and $\mathcal L_w$; uniqueness forces the shift to fix the tuple, so the polygon is the $m$-fold traversal of the primitive polygon for $u$. Conversely, a smaller geometric collision period makes $w$ a proper power. This proves the primitive/iterate statement. For example, $[01]$ and $[0101]$ share one geometric support but have traversal multiplicities one and two. Reversal follows directly from the itinerary. Non-grazing makes the finite itinerary locally constant, while uniqueness rules out a neighboring periodic ray with that itinerary; equivalently, the hyperbolicity proved below also gives isolation.

\>0

#### Why the proof is not a finite computation.

Compactness gives existence for an arbitrary word length. No-eclipse and strict convexity, not an enumeration cutoff, give boundary contact and uniqueness. The converse is included because a stationary reflected polygon would otherwise not automatically be the unique convex minimizer.

# Monodromy and uniform length control

Let $\ell_j>0$ be a free-flight length and let $\phi_j$ be the incidence angle measured from the obstacle normal, so $\cos\phi_j>0$. In transverse Jacobi coordinates, free flight followed by a dispersing reflection is represented, up to the standard collision-chart conjugacy, by $$\label{eq:block}
 B_j=R(a_j)F(\ell_j)
 =\begin{pmatrix}1&0\\a_j&1\end{pmatrix}
  \begin{pmatrix}1&\ell_j\\0&1\end{pmatrix}
 =\begin{pmatrix}1&\ell_j\\a_j&1+a_j\ell_j\end{pmatrix},
 \qquad a_j=\frac{2}{r\cos\phi_j}>0.$$

[\[prop:hyp\]]{#prop:hyp label="prop:hyp"} For every periodic ray, the monodromy $M=B_{n-1}\cdots B_0$ has determinant one, positive entries, and $\operatorname{tr}M>2$. Thus its multipliers are real positive reciprocals $\Lambda,\Lambda^{-1}$ with $\Lambda>1$.

Each factor, and hence their product, has determinant one and strictly positive entries. Thus $M_{11}M_{22}=1+M_{12}M_{21}>1$, and the arithmetic--geometric mean inequality gives $\operatorname{tr}M=M_{11}+M_{22}\ge2\sqrt{M_{11}M_{22}}>2$. The characteristic polynomial $\lambda^2-(\operatorname{tr}M)\lambda+1$ has two distinct positive reciprocal roots, one larger than one.

Every flight joins two distinct disks whose centers are distance $d$ apart, so the triangle inequalities give $$\label{eq:bounds}
 d-2r\le\ell_j\le d+2r,
 \qquad n(d-2r)\le L_w\le n(d+2r).$$ At $r=1,d=3$, the symmetric orbit $[01]$ has two flights of length one and $a=2$. Its block squared is $$\begin{pmatrix}1&1\\2&3\end{pmatrix}^{\!2}
 =\begin{pmatrix}3&4\\8&11\end{pmatrix},\qquad \operatorname{tr}M=14.$$ The symmetric orbit $[012]$ has flight length $3-\sqrt3$, incidence cosine $\sqrt3/2$, and total length $9-3\sqrt3$; its positive optical product is again hyperbolic.

# Exact symbolic and primitive ledgers

Let $A=J_3-I_3$ be the adjacency matrix: $A_{ij}=1$ exactly when $i\ne j$. Its eigenvalues are $2,-1,-1$. Therefore the number of collision-marked reduced $n$-bounce return records, including iterates whose primitive periods divide $n$, is $$\label{eq:fixed}
 F_n=\operatorname{tr}(A^n)=2^n+2(-1)^n.$$ Every exact-period rooted word has a free orbit of size $n$ under cyclic shift. Möbius inversion consequently gives $$\label{eq:primitive}
 P_n=\sum_{e\mid n}\mu(e)F_{n/e},
 \qquad O_n=\frac{P_n}{n},$$ where $O_n$ counts primitive oriented geometric rays of collision period $n$. Reversal can fix some cyclic classes, so it is an involution rather than permission to divide all $O_n$ by two.

With bounce count as the only variable, the source collision-code zeta is $$\label{eq:zeta}
 \zeta_{\rm coll}(z)
 =\exp\!\left(\sum_{n\ge1}\frac{F_n}{n}z^n\right)
 =\det(I-zA)^{-1}
 =\frac{1}{(1-2z)(1+z)^2}.$$ Equations [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}--[\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} are exact for every period because Theorem [\[thm:coding\]](#thm:coding){reference-type="ref" reference="thm:coding"} supplies the geometric bridge.

\>1

# Boundary atlas

  Parameter regime             Certified conclusion
  ---------------------------- -----------------------------------------------
  $d>4r/\sqrt3$, $r>0$         full reduced-word theorem
  $d=4r/\sqrt3$                capsule touches the third disk; excluded
  $2r<d<4r/\sqrt3$             disks disjoint, but full coding not certified
  $d=2r$                       neighboring disks touch
  $d<2r$                       neighboring obstacles overlap
  $r=0$                        point-scatterer singular limit, excluded
  nonreduced or grazing code   outside the collision section

At the equality surface a connecting capsule has zero clearance, so the strict segment-exclusion step in Theorem [\[thm:coding\]](#thm:coding){reference-type="ref" reference="thm:coding"} is unavailable. The weaker disjointness condition $d>2r$ cannot replace no-eclipse.

# Evidence, Route-A verdict, and scope

The archived evidence contains exact count rows through $n=16$, direct word enumeration through $n=10$, the zeta series through degree 16, six strict geometry cases, two symmetric orbits, and 175 rational optical products. An independent checker imports no producer code; a separate SymPy lane checks the determinant, trace, series, chamber, and Möbius identities. Byte replay, hostile repaired-hash mutations, duplicate-key rejection, and six fresh fixed-epoch manuscript builds close the reproducibility contract. These finite checks audit conventions only and do not prove geometric uniqueness.

The frozen Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_PASS\_ANALYTIC},
   \mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
   \mathrm{A4\_NATURAL\_QUANTIZATION}).$$ A1 passes because word powers are analytically identified with traversal multiplicities and primitive classes with primitive rays at all periods. A0 fails because the alphabet has no target arithmetic-local meaning; A2 fails because bounce count is not an arithmetic clock; A3 fails because [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} is not a target completed function. The exterior Dirichlet Laplacian is a natural quantization only, not a Hilbert--Pólya operator. The overall verdict is `ROUTE_A_REJECTED`, and Route B is locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.

No target Euler factor, root number, automorphy, target divisor law, target functional equation, zero correspondence, or target spectral realization is claimed. Nor do we claim literary priority for classical dispersing-billiard or three-disk mechanisms.

#### Reproducibility statement.

All released JSON and YAML have strict schemas and duplicate-key rejection. The evidence producer is deterministic; the checker, symbolic cross-check, replay, mutation suite, PDF build audit, and self-excluding manifest can be rerun from the package root.

#### AI-use statement.

A generative language model assisted with drafting and verification-code scaffolding. The mathematical claims, source boundaries, exact outputs, and release artifacts were independently checked under the recorded scripts; responsibility for the final content remains with the authors.

# Source lineage {#source-lineage .unnumbered}

Sinai's dispersing-billiard work supplies historical context [@Sinai1970]; Ikawa supplies neighboring several-convex-body and no-eclipse context [@Ikawa1988]; Gaspard and Rice are a direct owner in the three-hard-disk scattering neighborhood [@GR1989]. These citations do not assert novelty priority, and the proof above is self-contained.

9 Y. G. Sinai, "Dynamical systems with elastic reflections: ergodic properties of dispersing billiards," *Russian Mathematical Surveys* 25 (1970). DOI: [10.1070/RM1970v025n02ABEH003794](https://doi.org/10.1070/RM1970v025n02ABEH003794).

M. Ikawa, "Decay of solutions of the wave equation in the exterior of several convex bodies," *Annales de l'Institut Fourier* 38 (1988). DOI: [10.5802/aif.1137](https://doi.org/10.5802/aif.1137).

P. Gaspard and S. A. Rice, "Semiclassical quantization of the scattering from a classically chaotic repellor," *Journal of Chemical Physics* 90 (1989). DOI: [10.1063/1.456019](https://doi.org/10.1063/1.456019).
