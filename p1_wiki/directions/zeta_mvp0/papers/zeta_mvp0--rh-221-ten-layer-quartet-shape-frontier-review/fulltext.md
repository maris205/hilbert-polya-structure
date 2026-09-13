---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-221-ten-layer-quartet-shape-frontier-review"
canonical_tex: "zeta_mvp0/papers/RH-221-ten-layer-quartet-shape-frontier-review/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-221-ten-layer-quartet-shape-frontier-review/main.pdf"
source_sha256: "e876c07ee5f35da1eb54a2267cfda074ed92f3bd77dd856c245e66cf64761dd1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ten Layers at the Quartet-Shape Frontier RH-212--RH-220 Review and the Rank-Growing Gate-A Route

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-221-ten-layer-quartet-shape-frontier-review>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-221-ten-layer-quartet-shape-frontier-review/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-221-ten-layer-quartet-shape-frontier-review/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-221-ten-layer-quartet-shape-frontier-review/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-221-ten-layer-quartet-shape-frontier-review/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  This paper reviews RH-212--RH-220, a nine-paper investigation of the finite dual-channel quartic divisor left by the transport-frontier review RH-211. The batch begins with a negative result: determinant-radius and centered-RMS normalizations do not contract the eight-level coefficient flow, and raw coefficients remain the most stable of the three tested representations.

  The failed contraction exposes an exact structure. Every centered, RMS-normalized, branch-labeled conjugate quartet lies on a two-dimensional shape manifold with coordinates $(u,\eta)$ and coefficient identity $$c_3^2=4(2-c_2)(1-c_4).$$ Across sixteen scales and both physical channels, $u$ increases strictly through all fifteen transitions, while mature $\eta$ remains in corridors of width below $0.038$. A power-gap model wins two held-out scales on both channels, but its error remains about $0.01$ and no asymptotic law is claimed.

  Three exact theorems then delimit the route. The shape discriminant factors completely, and $u\to1$ is equivalent to collapse toward $(z^2-1)^2$. Transverse coefficient sensitivity is $O(1-u)$ while axial sensitivity stays nonzero. Yet arbitrary finite shape orbits admit exact polynomial recurrences, so finite recurrence existence is non-identifying; the tested low-complexity maps also fail holdout. Finally, a fixed quartic or its powers cannot supply a locally finite growing spectral count: degree can reach 256 in the audit while distinct support remains four.

  Restoring the affine gauge completes the local state type. Center $\mu$, RMS radius $r$, and shape $(u,\eta)$ reconstruct every raw physical quartic with coefficient error below $7.8\times10^{-16}$. The revised coordinate is $$\texttt{finite\_gauge\_complete\_shape\_flow\_open\_rank\_growing\_divisor}.$$ The aggregate reproducibility ledger contains 2,140 finite items and zero identity failures. Gate A remains open; Gates B--E, Hilbert--Pólya, zeta-zero identification, and RH are untouched.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Ten Layers at the Quartet-Shape Frontier\
  RH-212--RH-220 Review and the Rank-Growing Gate-A Route
```

## Markdown 正文

# Coordinate inherited from RH-211

RH-211 ended with a split transport verdict [@WangRH211]. Naive Haar transport of fixed and expanded edge clouds was rejected, while conjugate branch correspondence and a dual-channel quartic divisor survived. The declared coordinate was $$\texttt{finite\_dual\_channel\_divisor\_flow\_open\_renormalization}.$$

The next problem was deliberately local: before attempting a growing determinant, determine whether the finite quartet has an intrinsic cross-scale coordinate. RH-212--RH-220 answer this in four stages: $$\label{eq:batchroute}
 \begin{gathered}
 \text{normalization audit}
 \longrightarrow \text{exact shape quotient}\\
 \longrightarrow \text{finite dynamics and boundary geometry}\\
 \longrightarrow \text{fixed-factor obstruction}
 \longrightarrow \text{gauge-complete reconstruction}.
 \end{gathered}$$

The result is not a completed determinant. It is a rigorous classification of what the fixed quartet can and cannot do.

# Layer-by-layer verdict

  paper    principal result                                                           strict status
  -------- -------------------------------------------------------------------------- -------------------------
  RH-212   radial and centered normalizations do not contract                         finite negative
  RH-213   exact $(u,\eta)$ shape manifold and coefficient identity                   exact theorem
  RH-214   sixteen-level monotone axial clock and mature corridor                     finite positive
  RH-215   power-gap wins two holdouts but leaves $\sim0.01$ error                    finite mixed
  RH-216   discriminant stratification and uniform axial collapse                     exact theorem
  RH-217   transverse coefficient sensitivity quenches as $u\to1$                     exact theorem
  RH-218   simple recurrence fails holdout; arbitrary finite fit is non-identifying   exact + finite negative
  RH-219   fixed or repeated quartic cannot yield growing locally finite support      exact obstruction
  RH-220   center-radius-shape coordinates reconstruct every raw factor               exact + route decision

The sections below explain how the layers constrain one another. Positive and negative results are equally important because each removes an ambiguity from the next Gate-A construction.

# RH-212: two natural normalizations fail to contract

For the raw quartet $$D_{\sigma,s}(z)=\prod_{j=1}^{4}(z-\lambda_{\sigma,s,j}),$$ RH-212 compares:

1.  raw monic coefficients;

2.  determinant-radius roots $\lambda_j/|\prod\lambda_j|^{1/4}$;

3.  centered-RMS roots $(\lambda_j-\mu)/r$.

The audit uses eight predeclared levels; an additional eight levels are frozen for later work [@WangRH212].

With adjacent error $$E_f=\frac{\left\lVert C_f-C_c\right\rVert_2}{\left\lVert C_f\right\rVert_2},$$ the results are:

  representation           minimum     maximum        mean   max channel error
  -------------------- ----------- ----------- ----------- -------------------
  raw                    $0.04419$   $0.18945$   $0.10661$          $0.008112$
  determinant radius     $0.06062$   $0.36787$   $0.19322$          $0.019881$
  centered RMS           $0.05941$   $0.23389$   $0.16592$          $0.009368$

Thus no natural scalar normalization gives the desired contraction. The raw vector remains most stable. The correct route consequence is not to fit a fourth scalar after seeing the failures. Centered-RMS normalization is instead treated as an affine quotient whose residual geometry should be classified exactly.

# RH-213: the exact shape manifold

A centered conjugate quartet has roots $$a\pm ib,\qquad -a\pm id,$$ and unit mean square modulus imposes $$a^2+\frac{b^2+d^2}{2}=1.$$ Set $$u=a^2,qquad \eta=\frac{b^2-d^2}{b^2+d^2}.$$ Then $$\label{eq:canonicalroots}
 \sqrt u\pm i\sqrt{(1-u)(1+\eta)},qquad
 -\sqrt u\pm i\sqrt{(1-u)(1-\eta)}.$$

The monic polynomial is $$\label{eq:shapeformula}
 Q_{u,\eta}(z)=z^4+(2-4u)z^2
 +4\sqrt u(1-u)\eta z+1-\eta^2(1-u)^2.$$ Therefore $$\label{eq:identity}
 c_3^2=4(2-c_2)(1-c_4).$$ The interior map has rank two and explicit inverse $$u=\frac{2-c_2}{4},qquad
 \eta=\frac{c_3}{4\sqrt u(1-u)}.$$

This is an exact theorem, not a numerical pattern. All 32 physical endpoints satisfy it with maximum residual $8.81\times10^{-15}$, and 400 random checks have formula error below $6.7\times10^{-16}$ [@WangRH213].

The boundary fibers are also explicit: all $\eta$ collapse at $u=1$, while the unlabeled pair orientation is lost at $u=0$. These caveats prevent overstating the quotient as a globally injective rectangle.

# RH-214: one dominant finite clock

On both channels the axial coordinate rises through every one of the fifteen observed transitions. Net changes are $0.69809$ and $0.69673$; the minimum increments remain positive at $0.01529$ and $0.01513$ [@WangRH214].

For $\sigma\le0.02$, the asymmetry ranges are $$\eta_L\in[-0.10444,-0.06886],qquad
 \eta_R\in[-0.10748,-0.07031].$$ Their widths are $0.03557$ and $0.03717$. Mature channel discrepancies are at most $0.003006$ in $u$ and $0.003043$ in $\eta$.

Strict finite ordering defines an invertible piecewise-linear clock on the sampled log-scale interval. It does not prove all-level monotonicity or a limit. The justified description is a dominant axial motion with a narrow, nonmonotone transverse corridor.

# RH-215: prediction tempers the clock interpretation

Seven fine scales train affine-log, logistic-log, and power-gap models; the last two scales are withheld [@WangRH215]. The affine and logistic models have the best training $R^2$, but overpredict the holdouts. On the left, two-point RMS errors are $$0.03039,\quad0.02057,\quad0.00989,$$ and on the right $$0.03064,\quad0.02083,\quad0.01003.$$ Power gap wins every held-out point on both channels. Yet it still misses by about $0.01$, so the conditional law $$1-u_\sigma\asymp C\sigma^{0.361}$$ is not promoted to an asymptotic theorem.

This layer illustrates the value of predeclared holdouts. High in-sample fit would otherwise have selected a more aggressive and less predictive curve.

# RH-216: exact boundary geometry

The shape polynomial factors into the two conjugate quadratics in [\[eq:canonicalroots\]](#eq:canonicalroots){reference-type="eqref" reference="eq:canonicalroots"}. Their discriminants and cross resultant give $$\label{eq:disc}
 \operatorname{Disc}Q_{u,\eta}
 =256(1-u)^2(1-\eta^2)
  [4u+(1-u)^2\eta^2]^2$$ [@WangRH216].

Repeated roots occur exactly when $$u=1,\qquad |\eta|=1,
 \qquad\text{or}\qquad (u,\eta)=(0,0).$$ Along $u\to1$, root matching to $\{1,1,-1,-1\}$ obeys $$\label{eq:rootbound}
 d_{\rm match}\le \sqrt{2(1-u)}+\frac{1-u}{1+\sqrt u},$$ uniformly in $\eta$. Coefficient distance to $(z^2-1)^2$ is exactly $4(1-u)$ in maximum norm.

Thus $u\to1$, coefficient convergence, and root-multiset convergence are equivalent. The theorem is conditional geometry. The finest physical $u\approx0.718$ remains far enough away that the coefficient distance is about $1.13$.

# RH-217: exact transverse quenching

For $\Phi(u,\eta)=(c_2,c_3,c_4)$, direct differentiation gives $$\partial_\eta\Phi=
 \begin{pmatrix}
 0\\4\sqrt u(1-u)\\-2\eta(1-u)^2
 \end{pmatrix}.$$ Every transverse chord satisfies $$\label{eq:quench}
 \left\lVert\Phi(u,\eta_1)-\Phi(u,\eta_2)\right\rVert_2
 \le2(1-u)\sqrt{4u+(1-u)^2}|\eta_1-\eta_2|.$$ Meanwhile $\partial_uc_2=-4$, so axial sensitivity never vanishes [@WangRH217].

This proves a genuine asymptotic anisotropy of the coefficient map: if $u\to1$, transverse coefficient effects vanish even if $\eta$ does not converge. The physical transverse-to-axial Jacobian ratio falls from at most $0.3752$ at $\sigma=0.02$ to $0.2389$ at the finest level. This supports the mechanism but not its premise.

# RH-218: recurrence is both too rigid and too flexible

On the equal-log-step dyadic subsequence, a two-dimensional affine map fits three channelwise training transitions to roundoff, then misses the last two by up to $0.0426$ on the left and $0.0506$ on the right. A pooled map has training error $0.00205$ and holdout error $0.04685$ [@WangRH218].

At the opposite extreme, every finite orbit $x_k=(u_k,\eta_k)$ with distinct current $u_k$ admits an exact autonomous polynomial map. Lagrange interpolation constructs $$F(u,\eta)=(P(u),Q(u)),\qquad F(x_k)=x_{k+1}.$$ The physical six-state orbit has a degree-four interpolant with residual below $2\times10^{-15}$.

The lesson is structural: $$\text{simple map: predictive failure},qquad
 \text{arbitrary map: exact but non-identifying}.$$ Further fitted recurrence work on the fixed quartet is therefore deprioritized unless accompanied by uniform error, composition, or analytic generator estimates.

# RH-219: the fixed-factor wall

Suppose optimistically that the quartet were controlled perfectly. A locally uniform limit of monic quartics remains a quartic; it has only four zeros counted with multiplicity. Powering the factor gives $$Q(z)^N=\prod_{j=1}^{r}(z-\lambda_j)^{Nm_j},qquad r\le4.$$ Degree grows, but distinct support does not. As $N\to\infty$, divisor mass on every neighborhood of a zero diverges, violating local finiteness of a nonzero holomorphic divisor [@WangRH219; @Conway1978].

The finite illustration reaches degree 256 at $N=64$ while keeping exactly four support points. Its height-counting function has the same finite jump locations with larger jumps. This cannot become an extended locally finite spectrum.

The quartet is therefore a local seed and factor, not the final determinant. Gate A requires genuinely new roots as rank grows.

# RH-220: completing the finite state type

Normalization discards center and radius. Restore $$\mu=\frac14\sum_j\lambda_j,qquad
 r^2=\frac14\sum_j|\lambda_j-\mu|^2.$$ Then $$\label{eq:gaugecomplete}
 D(z)=r^4Q_{u,\eta}\!\left(\frac{z-\mu}{r}\right)
 =(z-\mu)^4+c_2r^2(z-\mu)^2+c_3r^3(z-\mu)+c_4r^4$$ [@WangRH220].

The parameters $(\mu,r,u,\eta)$ reconstruct all 32 raw endpoint quartets. Maximum errors are $3.15\times10^{-16}$ for roots and $7.78\times10^{-16}$ for coefficients. Shape alone is non-injective because translation and positive dilation leave it unchanged.

An exact gauge-first, shape-second decomposition of all 30 adjacent transitions finds eight gauge-dominant and 22 shape-dominant cases. Both ledgers are necessary. This is the finite state type to be generalized to a growing cloud.

# Combined logical picture

The batch separates four statements that could otherwise be conflated:

Finite quotient

:   The quartet has an exact affine-gauge decomposition and a compact shape rectangle.

Finite trajectory

:   The physical points show strict axial ordering, a narrow mature corridor, and dual-channel coherence.

Asymptotic trajectory

:   No limit or autonomous law has been proved; simple extrapolants and affine recurrences retain material holdout error.

Infinite determinant

:   A fixed quartet is structurally incapable of supplying a growing locally finite zero divisor, even if its asymptotic trajectory were known.

The local theory is therefore useful and essentially complete enough to specify the next experiment, but it is not Gate A itself.

# Revised Gate-A subroute

The next family should be $$\label{eq:growingcloud}
 \Lambda_{\sigma,k}
 =\{\lambda_{\sigma,1},\ldots,\lambda_{\sigma,k}\},
 \qquad k=k(\sigma)\longrightarrow\infty.$$ For each whole cloud define one center and one RMS radius: $$\mu_{\sigma,k}=\frac1k\sum_{j=1}^{k}\lambda_{\sigma,j},
 \qquad
 r_{\sigma,k}^2=\frac1k\sum_{j=1}^{k}
 |\lambda_{\sigma,j}-\mu_{\sigma,k}|^2.$$ The normalized empirical root measure is $$\label{eq:measure}
 \nu_{\sigma,k}=\frac1k\sum_{j=1}^{k}
 \delta_{(\lambda_{\sigma,j}-\mu_{\sigma,k})/r_{\sigma,k}}.$$

The predeclared rank-growing audit should test:

1.  nested or otherwise canonical root selection;

2.  conjugate closure and radial/contour separation;

3.  tightness and moment bounds for $\nu_{\sigma,k}$;

4.  left/right cloud matching in gauge-complete coordinates;

5.  stability of logarithmic derivatives on compact test domains;

6.  omitted-factor bounds between consecutive ranks;

7.  whether one normalization works without rankwise fitting.

Only after these pass should one form canonical products or seek a Fredholm/dynamical determinant. The route is $$\label{eq:nextroute}
 \begin{gathered}
 \text{rank-growing physical cloud}
 \longrightarrow \text{global gauge and tight root measures}\\
 \longrightarrow \text{locally uniform canonical product}
 \longrightarrow \text{dynamical/Fredholm realization}.
 \end{gathered}$$

# Reproducibility ledger

The batch freezes source, JSON outputs, tests, theorem ledgers, roadmaps, and publication archives. Counting endpoint, transition, random identity, prediction, sensitivity, recurrence, counting, and reconstruction records gives 2,140 finite ledger items. Exact-identity thresholds report zero failures.

The largest matrix computation is avoided by a sparse modulus-cloud extraction that reproduces the inherited dense anchor spectra. Downstream papers read the frozen RH-212 atlas, preventing model changes from silently altering earlier endpoints.

Archive verification establishes file integrity and implementation reproducibility. It does not convert floating observations into all-level theorems.

# Position in the five macro gates

-   **Gate A.** The fixed local factor now has exact shape and gauge theory. A rank-growing physical divisor, local uniform limit, and dynamical/Fredholm realization remain open.

-   **Gate B.** A time-oriented unitary or scattering completion is untouched.

-   **Gate C.** A self-adjoint generator and internally derived $T\log T$ count are untouched.

-   **Gate D.** A prime-power/von Mangoldt trace identity is untouched.

-   **Gate E.** Equality with the completed zeta divisor is untouched.

The route coordinate is $$\boxed{\texttt{finite\_gauge\_complete\_shape\_flow\_open\_rank\_growing\_divisor}}.$$

No Hilbert--Pólya operator, zeta-zero identification, Riemann-hypothesis implication, or arithmetic trace formula is asserted. The present progress is narrower but solid: it converts a numerical fixed quartet into a complete local theory and proves exactly why the program must now grow beyond it.
