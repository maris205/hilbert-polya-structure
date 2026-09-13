---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-bowen-pressure-gate"
canonical_tex: "henon_dynamics/henon_bowen_pressure_gate/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_bowen_pressure_gate/paper/main.pdf"
source_sha256: "9921014314cd7229d658f6876c210dee6a80fbfef5a37be2f287041495d428bb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Certified Bowen-Pressure Gate for an Area-Preserving Hénon Horseshoe

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_bowen_pressure_gate>)
- [规范 TeX](<../../../../../henon_dynamics/henon_bowen_pressure_gate/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_bowen_pressure_gate/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_bowen_pressure_gate/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_bowen_pressure_gate/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We certify an intrinsic geometric benchmark for a prominent positive value previously observed in finite instability-weighted cycle sections of the area-preserving Hénon map $H_6(q,p)=(1-6q^2-p,q)$. On an exact four-state hyperbolic survivor, the unstable expansion defines a positive Hölder roof. We prove that its adapted and Euclidean representatives are explicitly cohomologous and sharpen the inherited cone bound to $$J^u_{\mathrm{ad}}
    \ge \frac{\sqrt{17}+\sqrt{13}}{2}.$$ We then enclose the roof on every admissible length-13 cylinder. The resulting higher-block graph has 714 vertices and 1156 chronological edges. Outward rational square-root, logarithm, and exponential bounds, together with exact Collatz--Wielandt inequalities, prove that the unique pressure root satisfies $$0.277980<h_*<0.277987.$$ The earlier period-20 value $0.277982981676189\ldots$ lies strictly inside this independently certified interval. This containment is a certified comparison, not a proof that the finite sections converge. Standard pressure-zeta and Bowen-dimension theorems identify $h_*$ as the leading suspension-zeta boundary and the unstable-slice Hausdorff dimension of the local Hénon basic set. The old signal is therefore consistent with a genuine geometric invariant to the certified resolution, but supplies no unexplained arithmetic resonance. No prime correspondence, functional equation, critical-line law, or self-adjoint Hilbert--Pólya operator follows.
author:
- Anonymous Research Note
bibliography:
- references.bib
date: 11 August 2026
title: |
  A Certified Bowen-Pressure Gate for an\
  Area-Preserving Hénon Horseshoe
```

## Markdown 正文

# Introduction {#sec:introduction}

A stable zero of a finite cycle expansion can be either a glimpse of an infinite dynamical divisor or a familiar thermodynamic quantity in numerical disguise. Distinguishing these cases matters especially in dynamical approaches to Hilbert--Pólya, where generic hyperbolic spectral features can otherwise be mistaken for arithmetic structure.

The motivating area-preserving Hénon model was proposed as a numerical route from deterministic dynamics to spectra resembling the Riemann zeros [@Wang2026HenonModel]. A later proof-driven program isolated a different parameter regime, $a=6$, and certified a compact local survivor conjugate to a four-state subshift. An intrinsic instability clock $T_p=\log|\Lambda_{u,p}|$ removed the exact lattice obstruction of unit map time. Complete primitive-cycle sections through period 20 then displayed a stable positive zero $$s_{20}=0.27798298167618902348\ldots .$$ That value was reported correctly as a finite-section observation: no limiting determinant or uniform tail theorem had been proved at the zero.

This paper replaces cutoff extension with a pressure test. Let $\tau_{\mathrm{ad}}$ be the adapted one-step unstable expansion on the certified survivor, pulled back to its exact symbolic model. The function $$s\longmapsto P_{\Sigma_A}(-s\tau_{\mathrm{ad}})$$ is strictly decreasing and has a unique positive root $h_*$. We enclose that root without using the old cycle value. The computation retains every chronological length-13 word, encloses the roof on all of its bi-infinite extensions, and proves two rational Collatz inequalities for the ordered higher-block matrices.

The contributions are four concrete statements.

1.  We prove that the source-locked survivor is a mixing, locally maximal hyperbolic set and give an explicit coboundary between the adapted and Euclidean unstable roofs.

2.  We solve a self-consistent invariant-cone inequality and improve the uniform adapted expansion to $(\sqrt{17}+\sqrt{13})/2$. This also enlarges the certified absolute instability-Euler radius.

3.  A finite, independently checkable certificate proves $0.277980<h_*<0.277987$. Floating point proposes positive Collatz vectors but supplies no proof-critical inequality.

4.  Pressure-zeta and dimension theory identify $h_*$ as the geometric leading singularity and unstable Hausdorff dimension. The earlier finite value lies in its certified bracket; this explains the observation to the stated resolution without asserting convergence of the old sections, and removes it as independent arithmetic evidence.

The last point is intentionally negative for Hilbert--Pólya exploration. The result strengthens the mathematics of the Hénon survivor while lowering the evidential status of its most conspicuous positive zero. The remainder of the paper fixes the source conventions, proves the geometric lemmas, describes the certificate, and states the Route-A boundary.

# Thermodynamic and operator context {#sec:context}

#### Pressure and suspended zeta functions.

For a mixing subshift of finite type and a positive Hölder roof $\tau$, thermodynamic formalism gives a unique real solution of $P(-s\tau)=0$. It is the topological entropy of the suspension. The same transfer family controls the leading pole of the suspension Ruelle zeta function; non-lattice periodic data exclude a vertical arithmetic progression of competing boundary poles [@Bowen1975; @ParryPollicott1990; @Ruelle1976]. These facts make pressure the mandatory control for any positive real signal in an instability-weighted Euler product.

#### Bowen dimension.

For a locally maximal hyperbolic set with one-dimensional unstable bundle, the derivative is conformal on that bundle. The unstable-slice Hausdorff dimension is the unique zero of the pressure of the negative unstable geometric potential. This is the surface horseshoe formula of McCluskey--Manning and its local conformal-basic-set formulation [@McCluskeyManning1983; @Manning1985Erratum; @PesinSadovskaya2001; @Pesin1997; @Barreira2013]. We verify local maximality and the norm-gauge interface rather than assuming those hypotheses.

#### Analytic pinning operators.

Rugh-type pinning coordinates and mixed Cauchy kernels give powerful dynamical determinants for analytic surface maps. Baladi, Pujals, and Sambarino prove chronological composition, order-zero nuclearity, and trace identities under their analytic hyperbolic hypotheses [@BaladiPujalsSambarino2005]. The existing H6 domains specialize this framework. Those qualitative all-word statements are therefore prior art, not a contribution of the present paper. Our new object is the explicit finite error certificate for the geometric pressure root.

#### Relation to the original Hénon proposal.

The original model studies an area-preserving Hénon lift near a numerically selected transition and compares quantum and dissipative solvers with zero data [@Wang2026HenonModel]. Here $a=6$ is a target-free, proof-selected hyperbolic control. We use no Riemann zeros or primes, and our conclusion concerns one local survivor rather than the full plane.

# The source-locked H6 survivor {#sec:survivor}

Consider $$H_6(q,p)=(1-6q^2-p,q),
  \qquad \det DH_6=1.$$ Let $$X_\pm=\pm[1/3,5/8],
  \qquad Y_\pm=\pm[5/16,81/128],
  \qquad N_{st}=X_s\times Y_t.$$ In the state order $(--,-+,+-,++)$, the frozen adjacency matrix is $$A=\begin{pmatrix}
 1&0&1&0\\
 1&0&0&0\\
 0&1&0&1\\
 0&1&0&0
 \end{pmatrix}.$$ The inherited exact contraction theorem identifies $$\Lambda_*=\bigcap_{k\in\mathbb Z}H_6^{-k}
      \left(\bigcup_{s,t}N_{st}\right)$$ with the two-sided subshift $\Sigma_A$. A state at time $i$ is $(\varepsilon_i,\varepsilon_{i-1})$. Every admissible sign sequence has a unique coordinate sequence satisfying $$q_i=\varepsilon_i
 \sqrt{\frac{1-q_{i-1}-q_{i+1}}6}.
 \tag{3.1}\label{eq:recurrence}$$ The square-root transform contracts in the sup norm by at most $2/\sqrt{17}$.

The same radicand audit gives the sharper pointwise range $$\frac{\sqrt{17}}{12}\le |q_i|\le \sqrt{\frac38}.
  \tag{3.2}\label{eq:q-range}$$ In particular every realized coordinate lies strictly inside its $X$-box, with uniform margin at least $(\sqrt{17}-4)/12$. Since $X_\pm\Subset Y_\pm$, the whole survivor lies in the interior of $N=\bigcup N_{st}$.

[\[prop:basic\]]{#prop:basic label="prop:basic"} The set $\Lambda_*$ is a compact, mixing, locally maximal uniformly hyperbolic set for $H_6$.

Compactness, invariance, conjugacy, and uniform hyperbolicity are the source-locked R058--R059 conclusions. Put $U=\operatorname{int}N$. Equation [\[eq:q-range\]](#eq:q-range){reference-type="eqref" reference="eq:q-range"} and the strict $X\Subset Y$ inclusion give $\Lambda_*\subset U$. Because $U\subset N$, $$\mathop{\mathrm{Inv}}(U)\subset\mathop{\mathrm{Inv}}(N)=\Lambda_*\subset\mathop{\mathrm{Inv}}(U),$$ so $\Lambda_*=\mathop{\mathrm{Inv}}(U)$ is locally maximal. Finally, a direct integer calculation gives $A^4>0$ entrywise. Thus $\Sigma_A$, and hence $\Lambda_*$, is mixing.

The characteristic polynomial $$\det(\lambda I-A)
 =(\lambda^2-\lambda-1)(\lambda^2+1)$$ gives $h_{\mathrm{top}}(H_6|_{\Lambda_*})=\log\varphi$, where $\varphi=(1+\sqrt5)/2$.

# The unstable roof and a self-consistent cone bound {#sec:roof}

The source cone proof uses normalized tangent coordinates with half-widths $$r_x=\frac7{48},\qquad r_y=\frac{41}{256},
 \qquad r=\frac{r_y}{r_x}=\frac{123}{112},
 \qquad a_0=r^{-1}.$$ Write the normalized unstable line as $(1,\mu(z))$. Its projective recurrence is $$\mu(H_6z)=\frac{a_0}{-12q(z)-r\mu(z)}.
 \tag{4.1}\label{eq:slope-recurrence}$$

[\[lem:cone\]]{#lem:cone label="lem:cone"} Let $$\rho_0=\frac{\sqrt{17}-\sqrt{13}}2.$$ Then $$\sup_{\Lambda_*}|\mu|
 \le a_0\rho_0,
 \qquad
 J^u_{\mathrm{ad}}(z)=|-12q(z)-r\mu(z)|
 \ge \rho_0^{-1}
 =\frac{\sqrt{17}+\sqrt{13}}2.
 \tag{4.2}\label{eq:cone-sharpening}$$ Moreover, $$J^u_{\mathrm{ad}}(z)\le 3\sqrt6+\rho_0.
 \tag{4.3}\label{eq:j-upper}$$

Compactness makes $M=\max_{\Lambda_*}|\mu|$ well defined. The inherited cone gives $M\le1/2$. Equations [\[eq:q-range\]](#eq:q-range){reference-type="eqref" reference="eq:q-range"} and [\[eq:slope-recurrence\]](#eq:slope-recurrence){reference-type="eqref" reference="eq:slope-recurrence"} imply $$M\le \frac{a_0}{\sqrt{17}-rM},
 \quad\text{hence}\quad
 rM^2-\sqrt{17}M+a_0\ge0.$$ The two roots are $a_0\rho_0$ and $a_0/\rho_0$. The second is larger than $1/2$, so the inherited branch selection forces $M\le a_0\rho_0$. Since $ra_0=1$ and $\rho_0+\rho_0^{-1}=\sqrt{17}$, the lower bound follows. The upper bound uses $12|q|\le3\sqrt6$ and $rM\le\rho_0$.

Define the adapted roof $$\tau_{\mathrm{ad}}(z)=\log J^u_{\mathrm{ad}}(z).$$ It is positive and Hölder. To compare it with the Euclidean geometric potential, use the physical frame $$e^u_{\mathrm{ad}}(z)=(r_x,r_y\mu(z)).$$ Equation [\[eq:slope-recurrence\]](#eq:slope-recurrence){reference-type="eqref" reference="eq:slope-recurrence"} is equivalent to $$DH_6(z)e^u_{\mathrm{ad}}(z)
 =\lambda(z)e^u_{\mathrm{ad}}(H_6z),
 \qquad \lambda(z)=-12q(z)-r\mu(z).$$

[\[prop:coboundary\]]{#prop:coboundary label="prop:coboundary"} Let $b(z)=\log\|e^u_{\mathrm{ad}}(z)\|_2$. Then $$\tau_E^u(z)=\tau_{\mathrm{ad}}(z)+b(H_6z)-b(z).
 \tag{4.4}\label{eq:roof-coboundary}$$ Consequently the two roofs have the same pressure and identical sums on every periodic orbit.

Normalize $e^u_{\mathrm{ad}}(z)$ to Euclidean length one in the displayed invariant-frame identity. Taking logarithms gives [\[eq:roof-coboundary\]](#eq:roof-coboundary){reference-type="eqref" reference="eq:roof-coboundary"}. The unstable line is Hölder on a compact uniformly hyperbolic set, and the frame never vanishes, so $b$ is bounded Hölder. Pressure is invariant under a coboundary, and a periodic sum telescopes.

As an immediate quantitative consequence, the absolute periodic majorant for the instability-weighted Euler series is valid for $$|z|<\frac{\rho_0^{-1}}{\varphi}
 =\frac{\sqrt{17}+\sqrt{13}}{1+\sqrt5}
 =2.38828632613\ldots .
 \tag{4.5}\label{eq:euler-radius}$$ This is an instability-weight radius, not a scalar BPS flat-trace radius.

# A finite certificate for the infinite pressure root {#sec:certificate}

The pressure computation uses no periodic-orbit truncation. Fix a centered state word $$w=(x_{-6},\ldots,x_6)$$ of length 13. It determines the signs $\varepsilon_{-7},\ldots,\varepsilon_6$. Initialize every coordinate by its exact sign box. Hold the two exterior coordinates fixed at those boxes and repeatedly intersect the twelve interior intervals with the image of the signed recurrence [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. Every finite intersection remains an outer enclosure; convergence of the interval iteration is not an assumption.

Starting at time $-6$ with the inherited cone $\mu_{-6}\in[-1/2,1/2]$, interval evaluation of [\[eq:slope-recurrence\]](#eq:slope-recurrence){reference-type="eqref" reference="eq:slope-recurrence"} through time zero gives rational numbers $$0<J_-(w)\le J^u_{\mathrm{ad}}(x)\le J_+(w)
 \quad\text{for every }x\in[w].
 \tag{5.1}\label{eq:cylinder-j}$$ Square roots are rounded outward to a fixed $10^{-50}$ rational grid.

The length-12 admissible words are the vertices of a higher-block graph, and the length-13 words are chronological edges from prefix to suffix. Exact enumeration gives $$\#V=714,\qquad \#E=1156.$$ For real $s\ge0$, define two nonnegative matrices by $$(L_s^-)_{uv}
 =\sum_{w:u\to v}J_+(w)^{-s},
 \qquad
 (L_s^+)_{uv}
 =\sum_{w:u\to v}J_-(w)^{-s}.
 \tag{5.2}\label{eq:bounding-matrices}$$ The endpoint reversal is forced because $x^{-s}$ decreases in $x$. Monotonicity of pressure gives $$\log\mathop{\mathrm{rad}}(L_s^-)
 \le P_{\Sigma_A}(-s\tau_{\mathrm{ad}})
 \le \log\mathop{\mathrm{rad}}(L_s^+).
 \tag{5.3}\label{eq:pressure-order}$$

[\[thm:bracket\]]{#thm:bracket label="thm:bracket"} The unique positive solution of $$P_{\Sigma_A}(-h_*\tau_{\mathrm{ad}})=0$$ satisfies $$\boxed{0.277980<h_*<0.277987.}
 \tag{5.4}\label{eq:root-bracket}$$

The machine certificate reconstructs all 714 vertices and 1156 edges, proves [\[eq:cylinder-j\]](#eq:cylinder-j){reference-type="eqref" reference="eq:cylinder-j"} for every edge, and encloses every matrix weight in [\[eq:bounding-matrices\]](#eq:bounding-matrices){reference-type="eqref" reference="eq:bounding-matrices"}. For $s_L=277980/10^6$, it supplies a positive rational vector $v^-$ such that $$\min_i\frac{(\underline L_{s_L}^-v^-)_i}{v_i^-}>1,
 \tag{5.5}\label{eq:collatz-lower}$$ where $\underline L^-$ uses lower rational enclosures of its weights. For $s_U=277987/10^6$, a second positive rational vector satisfies $$\max_i\frac{(\overline L_{s_U}^+v^+)_i}{v_i^+}<1.
 \tag{5.6}\label{eq:collatz-upper}$$ The Collatz--Wielandt inequalities prove $\mathop{\mathrm{rad}}(L_{s_L}^-)>1$ and $\mathop{\mathrm{rad}}(L_{s_U}^+)<1$. Equation [\[eq:pressure-order\]](#eq:pressure-order){reference-type="eqref" reference="eq:pressure-order"} therefore gives opposite signs for the true pressure at the two endpoints. Positivity of the roof makes the pressure strictly decreasing, proving the claim.

The logarithm enclosure uses $$\log y=2\sum_{k=0}^{K}\frac{t^{2k+1}}{2k+1}+R_K,
 \qquad t=\frac{y-1}{y+1},$$ after power-of-two range reduction, with an exact geometric bound on $R_K$. Since every exponent lies in $(-1,0)$, odd and even partial sums of the alternating exponential series enclose each weight. Floating point is used only to propose $v^\pm$; the proof trusts only the rational inequalities [\[eq:collatz-lower\]](#eq:collatz-lower){reference-type="eqref" reference="eq:collatz-lower"}--[\[eq:collatz-upper\]](#eq:collatz-upper){reference-type="eqref" reference="eq:collatz-upper"}.

# What the certified root means {#sec:meaning}

For a primitive orbit $p$ of map period $n_p$, let $T_p=\log|\Lambda_{u,p}|$. The suspension zeta function is $$\zeta_\tau(s)
 =\prod_p\left(1-e^{-sT_p}\right)^{-1}.
 \tag{6.1}\label{eq:suspension-zeta}$$ The exact symbolic conjugacy supplies the primitive/repetition convention. By [\[prop:coboundary\]](#prop:coboundary){reference-type="ref" reference="prop:coboundary"}, $$T_p=\sum_{j=0}^{n_p-1}\tau_{\mathrm{ad}}(H_6^j x_p).$$ For the mixing subshift and positive Hölder roof, the leading real pole of [\[eq:suspension-zeta\]](#eq:suspension-zeta){reference-type="eqref" reference="eq:suspension-zeta"} occurs at the unique root of $P(-s\tau_{\mathrm{ad}})=0$ [@ParryPollicott1990]. The inherited non-lattice certificate supplies the usual non-arithmetic boundary condition.

The period-20 finite-section calculation produced $$s_{20}=0.27798298167618902348\ldots .$$ This number lies strictly inside [\[eq:root-bracket\]](#eq:root-bracket){reference-type="eqref" reference="eq:root-bracket"}. The certification is independent of that value: the interval recursion and the two pressure-sign proofs do not use it as input. We do not infer from containment alone that the particular finite cycle sections converge. Rather, the zeta theorem and pressure certificate identify an intrinsic infinite-system quantity consistent with the value numerically shared by those sections.

[\[cor:dimension\]]{#cor:dimension label="cor:dimension"} For every $z\in\Lambda_*$, $$h_*=\dim_H\bigl(\Lambda_*\cap W^u_{\mathrm{loc}}(z)\bigr).
 \tag{6.2}\label{eq:unstable-dimension}$$ Moreover, the stable slice has the same dimension and $$0.555960<\dim_H\Lambda_*<0.555974.
 \tag{6.3}\label{eq:total-dimension}$$

By [\[prop:basic\]](#prop:basic){reference-type="ref" reference="prop:basic"}, $\Lambda_*$ is a locally maximal mixing hyperbolic set. Its unstable bundle is one-dimensional and hence conformal. The local Bowen-dimension theorem identifies the unstable slice dimension with the root of the Euclidean geometric pressure [@PesinSadovskaya2001 Remark 4.1]. Proposition [\[prop:coboundary\]](#prop:coboundary){reference-type="ref" reference="prop:coboundary"} identifies that pressure with the adapted one.

For the stable line, area preservation gives $$J_E^u(z)J_E^s(z)
 \frac{\sin\alpha(H_6z)}{\sin\alpha(z)}=1,$$ where $\alpha$ is the angle between the invariant lines. Uniform cone separation makes $\log\sin\alpha$ bounded Hölder, so the positive stable contraction roof is cohomologous to the unstable expansion roof. The two slice dimensions agree. The local surface basic-set product formula then gives $\dim_H\Lambda_*=2h_*$ [@Barreira2013 Theorem 1.2]. Doubling [\[eq:root-bracket\]](#eq:root-bracket){reference-type="eqref" reference="eq:root-bracket"} gives [\[eq:total-dimension\]](#eq:total-dimension){reference-type="eqref" reference="eq:total-dimension"}.

Thus $h_*$ is a geometric dimension signal, while the old finite-section value is consistent with it to certified resolution. Stability near this benchmark is expected from the spectral stability of pressure and is not, by itself, evidence of a hidden prime law.

# Route-A decision and conclusion {#sec:routea}

The project advances the mathematical status of one Hénon signal and closes its arithmetic interpretation. Primitive orbits, orientation, repetition, and the instability clock are intrinsic and reproducible, so the primitive-orbit layer remains meaningful. The pressure family is an exact analytic transfer object on the real axis, and the leading root is now certified rather than merely cutoff-stable.

The same result supplies a decisive control. A positive real root of $P(-s\tau)=0$ is generic thermodynamic geometry. It does not provide

-   a correspondence between primitive Hénon cycles and primes;

-   von Mangoldt repetition amplitudes or logarithmic prime lengths;

-   a completed determinant with gamma factor and functional equation;

-   a Riemann--von Mangoldt counting law or critical-line symmetry; or

-   a self-adjoint operator whose spectrum is the Riemann-zero set.

Accordingly, the strict Route-A tuple for the arithmetic interpretation is $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),$$ with overall verdict `ROUTE_A_REJECTED`. The pressure enclosure is separately numerically certified and its analytic consequences are proved; neither status supplies an A2 Riemann-divisor match. Route B is not authorized.

The main theorem can be stated without qualification: on the source-locked H6 survivor, the Bowen pressure root is the unstable Hausdorff dimension and satisfies $0.277980<h_*<0.277987$. The old positive finite-section value lies in this interval, but C31 does not prove equality or convergence of those sections. Extending only that cutoff would therefore not open a new Hilbert--Pólya mechanism. The next genuinely different large gate is a canonical arithmetic fibre or twist over this proven hyperbolic base, with chronology and the intrinsic roof left intact.

# Proof arithmetic {#app:arithmetic}

This appendix records why the certificate does not depend on floating-point rounding.

#### Square roots.

For a nonnegative rational $x=a/b$ and $B=10^{50}$, compute $$k=\left\lfloor\sqrt{aB^2/b}\right\rfloor$$ by integer square root. Then $k/B\le\sqrt{x}\le(k+1)/B$, with equality detected exactly. All interval additions, multiplications, intersections, and reciprocal operations use rational arithmetic and explicit sign checks.

#### Logarithms.

After writing $x=2^m y$, $1\le y<2$, use $$t=\frac{y-1}{y+1},\qquad
 \log y=2\sum_{k=0}^{K}\frac{t^{2k+1}}{2k+1}+R_K.$$ Since $0\le t\le1/3$, $$0\le R_K
 \le\frac{2t^{2K+3}}{(2K+3)(1-t^2)}.$$ The same formula encloses $\log2$. Every elementary operation is rounded outward to the common rational grid.

#### Exponentials.

All proof inputs have $0<x<1$. The alternating series for $e^{-x}$ has decreasing terms, so an odd partial sum is a lower bound and the following even partial sum is an upper bound. The release uses order 61/62 before the final outward grid projection.

#### Collatz inequalities.

For any nonnegative matrix $M$ and positive vector $v$, $$\min_i\frac{(Mv)_i}{v_i}
 \le\mathop{\mathrm{rad}}(M)\le
 \max_i\frac{(Mv)_i}{v_i}.$$ The producer may construct $v$ by floating-point power iteration. It then quantizes $v$ to positive integers. The checker reconstructs every interval and evaluates the final ratios as rational numbers. Thus an inaccurate floating-point vector can only make a proof fail; it cannot create a false strict inequality.

#### Chronology.

Rows of $A$ are sources and columns are targets. A length-13 word is an edge from its length-12 prefix to its length-12 suffix. The time-zero roof is attached before any matrix aggregation. No averaged transition matrix or unordered word statistic enters the proof.

# Reproducibility and claim boundary {#app:reproducibility}

The release contains a canonical producer, an independently written checker, mutation tests, the complete cylinder ledger, the two Collatz vectors, and a SHA-256 manifest. The default runner regenerates into a temporary directory and compares against frozen artifacts; it does not silently refresh hashes.

The proof-critical source lock includes the exact R058 cone/covering package, the R059 symbolic-contraction theorem, the instability-roof implementation, and the actual cutoff-20 root chain: frozen protocol, raw robustness ledger, analysis summary, and its independent audit. The old root value is used only for the final containment comparison. Prime tables, Riemann-zero tables, zeta evaluations, post hoc rescaling, and target fitting are forbidden.

The pressure bracket certifies one real thermodynamic root. It is not by itself a global Fredholm-determinant continuation theorem, a certification of every complex finite-section zero, or a convergence theorem for the old degree-truncated sections. Generic analytic pinning-kernel nuclearity remains classical background. The local Bowen-dimension conclusion uses the exact locally maximal hyperbolic set and the one-dimensional conformal geometric potential; it makes no claim about the full Hénon nonwandering set.
