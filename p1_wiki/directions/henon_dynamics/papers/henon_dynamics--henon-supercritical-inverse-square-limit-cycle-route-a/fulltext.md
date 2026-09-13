---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-supercritical-inverse-square-limit-cycle-route-a"
canonical_tex: "henon_dynamics/henon_supercritical_inverse_square_limit_cycle_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_supercritical_inverse_square_limit_cycle_route_a/paper/main.pdf"
source_sha256: "9ffac9a395ebd4e5ec9a4b5934957652da0ebc380b6252863cc30cf896959acd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Supercritical Inverse-Square Dynamics: Domains, Collisions and the Complete Bound Ladder

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_supercritical_inverse_square_limit_cycle_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_supercritical_inverse_square_limit_cycle_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_supercritical_inverse_square_limit_cycle_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_supercritical_inverse_square_limit_cycle_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We reconstruct the complete self-adjoint boundary family of the strictly supercritical inverse-square Hamiltonian on the positive half-line. Its classical counterpart has an exact quadratic position law, and every trajectory reaches an excluded collision endpoint in at least one time direction. Endpoint analysis gives a circle of quantum boundary conditions, none selected by the classical differential expression. The Bessel Green function determines every simple negative level and its normalized eigenfunction. The levels form a bilateral geometric sequence with ratio $\exp(-2\pi/\sigma)$, accumulating at zero in one direction and diverging to minus infinity in the other. In particular, no self-adjoint realization has a ground state or a Friedrichs construction. The normalization is derived from a two-momentum Lagrange identity, and branch changes only relabel the levels. The formulas retain their classical literature ownership. This first draft closes the source clock, all boundary domains and the complete bound ladder; finite rational and special-function checks are distinguished from proof. We give a convention-complete spectral reconstruction of every unit-modulus boundary realization of the supercritical half-line inverse-square Hamiltonian. The classical collision flow and its quantum self-adjoint extension remain distinct sources of time evolution. An explicit Green function yields the entire bilateral negative ladder, while its positive boundary jump gives a continuous spectrum of multiplicity one and excludes hidden singular spectrum. Incoming waves are normalized to $(2\pi)^{-1/2}\exp(-\mathrm ikx)$. The resulting reflection amplitude has unit modulus, but differs by a minus sign from scattering relative to the free Dirichlet half-line. The hypotheses of the classical complete-wave-operator theorem are checked for every positive coupling parameter and every unit boundary phase. Independent high-precision tests compare 108 Green-kernel jumps with the spectral-density formula. These tests audit constants and phases; completeness comes from endpoint and spectral analysis. No target arithmetic interpretation or novel ownership of the classical inverse-square spectrum is claimed. We assemble a complete, domain-sensitive theorem for the strictly supercritical inverse-square Hamiltonian on the positive half-line. Every unit boundary phase defines a self-adjoint realization with a simple bilateral geometric negative ladder and a multiplicity-one absolutely continuous positive spectrum. Its normalized scattering amplitude is explicit. Dilation moves the boundary phase around a circle; one fixed self-adjoint domain is preserved exactly by the discrete subgroup $(\pi/\sigma)\mathbb Z$, and scattering has the corresponding least logarithmic momentum period. This domain cycle is not a physical-time return. The classical source reaches an excluded collision point, whereas the quantum group is complete and has no nonzero full return time. The negative ladder makes every positive-time heat operator unbounded; the continuum makes every resolvent noncompact; and the two ladder tails leave no convergence germ for an ordinary bilateral spectral zeta. Thus natural self-adjoint quantization alone supplies none of these global determinant constructions. The classical formulas are attributed, and exact algebra, independent Green/Stone checks and adversarial release tests delimit the package's reproducible contribution.
author:
- 'HCS-C391 theorem and reproducibility package'
date: 5 September 2026
title:
- |
  Supercritical Inverse-Square Dynamics:\
  Domains, Collisions and the Complete Bound Ladder
- |
  Supercritical Inverse-Square Dynamics:\
  Complete Spectral Resolution and Scattering
- |
  Supercritical Inverse-Square Dynamics:\
  Domain-Scale Cycles and the Ordinary-Determinant Obstruction
```

## Markdown 正文

=2em

**Keywords:** inverse-square Hamiltonian; self-adjoint domain; bilateral bound spectrum; continuous scattering; discrete scaling; determinant obstruction.

# A local Hamiltonian does not choose a boundary

Fix $\sigma>0$, put $g=\sigma^2+1/4$, and use units $\hbar=2m=1$. The classical source is $h(x,p)=p^2-g/x^2$ on $T^*(0,\infty)$. Its quantum expression is $\ell=-\partial_x^2-g/x^2$ on $\mathcal H=L^2((0,\infty),\,\mathrm dx)$. A unit complex number $\kappa$ will specify the missing boundary condition. It is independent physical input, not a value fitted to a desired eigenvalue or prime scale. Throughout, $I_\nu,J_\nu,K_\nu$ are ordinary Bessel functions.

The contribution is a single-convention source theorem and audit, not a new discovery of the inverse-square spectrum. Dereziński and Richard give the domain, spectrum and scattering theory in a substantially larger complex parameter family [@dr2017]. We retain the entire strictly supercritical self-adjoint subfamily, derive the constants used here, and connect them to the original source clock and the limits of ordinary global determinants. The critical value $\sigma=0$, nonunit $\kappa$, ultraviolet regularization and confinement are not part of this theorem.

For every initial point $(x_0,p_0)$, with energy $E=h(x_0,p_0)$, $$y(t)=x(t)^2=x_0^2+4x_0p_0t+4Et^2,\qquad
 p(t)=\frac{y'(t)}{4\sqrt{y(t)}}.
 \label{eq:classical}$$ Its maximal time interval is the component of $\{t:y(t)>0\}$ containing zero. Every orbit has a finite collision endpoint, and none is periodic in the declared phase space.

Hamilton's equations are $x'=2p$ and $p'=-2g/x^3$, so $y''=8E$. The reconstruction in [\[eq:classical\]](#eq:classical){reference-type="eqref" reference="eq:classical"} satisfies both equations. For $E\ne0$ the quadratic discriminant is $16g>0$. At $E<0$ its positive component is bounded; at $E>0$ it is a half-line. At $E=0$ the nonzero slope is $\pm4\sqrt g$, again giving a half-line. Each finite endpoint has $x=0$, which is excluded. No collision continuation has been added, so none of these intervals gives a periodic orbit.

# All self-adjoint domains and the bound ladder

Let $D_{\max}=\{f\in L^2:\ell f\in L^2\text{ distributionally}\}$ and let $D_{\min}$ be the graph closure of $C_c^\infty(0,\infty)$. Membership in $D_{\min}$ near zero means membership after multiplication by a smooth cutoff equal to one there. Define $$D_\kappa=\left\{f\in D_{\max}:\ %
 f-c(\kappa x^{1/2-\mathrm i\sigma}+x^{1/2+\mathrm i\sigma})
 \in D_{\min}\text{ near }0\text{ for some }c\in\mathbb C\right\}.
 \label{eq:domain}$$

The domains [\[eq:domain\]](#eq:domain){reference-type="eqref" reference="eq:domain"}, $|\kappa|=1$, are exactly the self-adjoint extensions of the minimal operator. None is semibounded, and there is no Friedrichs realization. Position-space complex conjugation preserves every one of these domains.

The zero-energy basis $u_\pm=x^{1/2\pm\mathrm i\sigma}$ is square integrable near zero. Variation of constants gives a unique expansion $f=a_fu_-+b_fu_+$ modulo $D_{\min}$ there. Indeed, the integrals of $u_\pm\ell f$ converge by Cauchy--Schwarz and their remainders are $o(x^{3/2})$, with derivatives $o(x^{1/2})$. Infinity is limit point since the potential is integrable on tails. Weyl's endpoint theorem therefore gives deficiency indices $(1,1)$. The boundary Wronskian is $$W_0(\overline f,v)=2\mathrm i\sigma
 (\overline{b_f}b_v-\overline{a_f}a_v).$$ Its maximal isotropic lines are exactly $a=\kappa b$, $|\kappa|=1$; neither coefficient of a nonzero isotropic vector can vanish. Conjugation changes the ratio to $1/\overline\kappa=\kappa$. For nonsemiboundedness, set $f(x)=x^{1/2}\chi(\log x)$ with a real compactly supported smooth function $\chi$. Direct substitution gives $$\langle f,\ell f\rangle=\int_{\mathbb R}
 (|\chi'(s)|^2-\sigma^2|\chi(s)|^2)\,\mathrm ds.$$ A sufficiently long plateau makes this negative. Normalized dilations make it arbitrarily negative. Every extension contains these minimal-domain test functions, so no semibounded extension exists.

Put $\varsigma=\kappa\Gamma(-\mathrm i\sigma)/\Gamma(\mathrm i\sigma)=\mathrm e^{\mathrm i\theta}$, using any real lift $\theta$. Powers of a right-half-plane momentum use the logarithm on $\mathop{\mathrm{Re}}\rho>0$.

Every negative spectral point of $H_{\sigma,\kappa}=\ell|_{D_\kappa}$ is a simple eigenvalue $$E_j=-\rho_j^2=-4\exp\!\left(-\frac{\theta+2\pi j}{\sigma}\right),
 \quad j\in\mathbb Z,\qquad
 \psi_j(x)=\rho_j\sqrt{\frac{2\sinh(\pi\sigma)}{\pi\sigma}}
 \sqrt x K_{\mathrm i\sigma}(\rho_jx).
 \label{eq:ladder}$$ The functions $\psi_j$ have unit norm. A different lift of $\theta$ merely reindexes the same spectrum.

At energy $-\rho^2$ the decaying solution at infinity is uniquely $\sqrt xK_{\mathrm i\sigma}(\rho x)$, up to a scalar. Its endpoint coefficients follow from $$K_{\mathrm i\sigma}(w)=\tfrac12\Gamma(\mathrm i\sigma)(w/2)^{-\mathrm i\sigma}
 +\tfrac12\Gamma(-\mathrm i\sigma)(w/2)^{\mathrm i\sigma}+o(1).$$ Their ratio equals $\kappa$ exactly when $\varsigma(\rho/2)^{2\mathrm i\sigma}=1$, giving [\[eq:ladder\]](#eq:ladder){reference-type="eqref" reference="eq:ladder"}. For $\mathop{\mathrm{Re}}\rho>0$ this equality forces $\arg\rho=0$ by taking absolute values. Away from these roots the Green kernel in the proof supplement gives a bounded inverse; hence no additional negative spectrum is omitted. Uniqueness of the decaying solution gives simplicity.

For $f_a(x)=\sqrt xK_{\mathrm i\sigma}(ax)$ and $f_b(x)=\sqrt xK_{\mathrm i\sigma}(bx)$, the Lagrange identity is $W(f_a,f_b)'=(b^2-a^2)f_af_b$. The Wronskian vanishes at infinity; its endpoint value is $\sigma|\Gamma(\mathrm i\sigma)|^2\sin(\sigma\log(a/b))$. Using $|\Gamma(\mathrm i\sigma)|^2=\pi/(\sigma\sinh\pi\sigma)$ gives $$\int_0^\infty xK_{\mathrm i\sigma}(ax)K_{\mathrm i\sigma}(bx)\,\mathrm dx
 =\frac{\pi\sin(\sigma\log(a/b))}{(a^2-b^2)\sinh(\pi\sigma)}.
 \label{eq:lagrange}$$ The coincident limit is $\pi\sigma/(2a^2\sinh\pi\sigma)$, proving the normalizer in [\[eq:ladder\]](#eq:ladder){reference-type="eqref" reference="eq:ladder"}. Endpoint $O(x)$ bounds and exponential tail decay justify that limit. Distinct ladder values give orthogonality in [\[eq:lagrange\]](#eq:lagrange){reference-type="eqref" reference="eq:lagrange"}. Finally $E_j\to0$ as $j\to+\infty$ and $E_j\to-\infty$ as $j\to-\infty$; there is no lowest level.

\>0

# Green jumps, completeness and scattering

For $z=-\rho^2$, $\mathop{\mathrm{Re}}\rho>0$, define $$\begin{aligned}
 T_\rho&=\varsigma(\rho/2)^{2\mathrm i\sigma},\nonumber\\
 u_\rho(x)&=\sqrt x\,[I_{\mathrm i\sigma}(\rho x)-T_\rho I_{-\mathrm i\sigma}(\rho x)],
 &v_\rho(x)&=\sqrt xK_{\mathrm i\sigma}(\rho x).\label{eq:uv}\end{aligned}$$ The Gamma recurrence gives the required endpoint ratio for $u_\rho$. Both $I$--$K$ Wronskians equal $-1$, so $W(u_\rho,v_\rho)=T_\rho-1$. Thus $$G_\kappa(-\rho^2;x,y)=
 \frac{u_\rho(\min(x,y))v_\rho(\max(x,y))}{1-T_\rho}.
 \label{eq:green}$$ Its first derivative jumps by $-1$. The $O(\sqrt{xy})$ behavior on compact endpoint squares and exponential tail bounds give a bounded inverse when the denominator is nonzero.

For positive $k$, put $t(k)=\varsigma(k/2)^{2\mathrm i\sigma}$, $a=\mathrm e^{\pi\sigma/2}$ and $b=\mathrm e^{-\pi\sigma/2}$. Define $$\phi_k(x)=\mathrm e^{-\mathrm i\pi/4}\sqrt{kx}\,
 \frac{J_{\mathrm i\sigma}(kx)-t(k)J_{-\mathrm i\sigma}(kx)}{b-t(k)a}.
 \label{eq:phi}$$ The denominator satisfies $|b-ta|\ge a-b>0$, uniformly in $k$ at fixed $\sigma$. The two Green boundary values give $$\frac{k}{\pi\mathrm i}\big[G_\kappa(k^2+\mathrm i0;x,y)-G_\kappa(k^2-\mathrm i0;x,y)\big]
 =\phi_k(x)\overline{\phi_k(y)}.
 \label{eq:stone}$$

The positive spectrum is absolutely continuous of multiplicity one, with momentum density $\phi_k(x)\overline{\phi_k(y)}\,\mathrm dk$. There are no positive or zero eigenvalues and no singular continuous spectrum. For every $f\in\mathcal H$, $$\|f\|^2=\sum_{j\in\mathbb Z}|\langle\psi_j,f\rangle|^2+
 \int_0^\infty|\langle\phi_k,f\rangle|^2\,\mathrm dk.
 \label{eq:parseval}$$ The transform is initially defined weakly on compactly supported test functions and extended by this identity.

The $I$--$J$ and $K$--Hankel identities in [\[eq:green\]](#eq:green){reference-type="eqref" reference="eq:green"} give [\[eq:stone\]](#eq:stone){reference-type="eqref" reference="eq:stone"}. On compact positive momentum intervals the boundary values are continuous between the weighted spaces used in limiting absorption, with weight exponent greater than $1/2$; endpoint and oscillatory tail bounds apply because $b-ta$ never vanishes. These are the nonexceptional hypotheses in [@dr2017 Theorem 6.1 and Proposition 6.7]. Stone's formula gives the displayed density and rules out singular spectrum on every such interval. Positive-energy Bessel waves have nondecaying oscillatory tails, so no nonzero solution is square integrable there. For every nonzero zero-energy combination, dilation by $\mathrm e^{\pi/\sigma}$ multiplies its squared norm on consecutive logarithmic annuli by $\mathrm e^{2\pi/\sigma}>1$, so it is not square integrable at infinity. A singular measure supported only at zero would be an eigenvalue atom, which is excluded. The full spectral theorem together with the negative resolvent classification now yields [\[eq:parseval\]](#eq:parseval){reference-type="eqref" reference="eq:parseval"}. One generalized eigenfunction per momentum gives multiplicity one.

The large-$x$ expansion, with no unspecified normalization phase, is $$\phi_k(x)=\frac{\mathrm e^{-\mathrm ikx}+R(k)\mathrm e^{\mathrm ikx}}{\sqrt{2\pi}}+O(x^{-1}),
 \qquad R(k)=-\mathrm i\frac{a-t(k)b}{b-t(k)a}.
 \label{eq:reflection}$$ Incoming means $\mathrm e^{-\mathrm ikx}$. Numerator and denominator in the ratio have equal modulus, so $|R|=1$. This is reflection, not yet relative scattering. The free Dirichlet half-line Hamiltonian $H_D$ has reflection $-1$. Under the convention $$W_\pm=\mathop{\mathrm{s-lim}}_{t\to\pm\infty}
 \mathrm e^{\mathrm itH_{\sigma,\kappa}}\mathrm e^{-\mathrm itH_D},\qquad S=W_+^*W_-,$$ the sine-representation multiplier is $S(k)=-R(k)$. Existence and completeness of these limits are the explicitly used external result [@dr2017 Proposition 6.10]. Its two parameter pairs are $(\mathrm i\sigma,\kappa)$ and $(1/2,0)$: both real parts lie strictly between minus one and one, both realizations are self-adjoint, and neither denominator is exceptional. Proposition 6.9 of that source agrees with the phase in [\[eq:reflection\]](#eq:reflection){reference-type="eqref" reference="eq:reflection"}. Completeness means $W_\pm^*W_\pm=I$ and $W_\pm W_\pm^*=P_{\rm ac}(H)$, not that negative bound states scatter freely.

\>1

# The scale cycle is not a return of time evolution

For the unitary dilation $(U_\tau f)(x)=\mathrm e^{\tau/2}f(\mathrm e^\tau x)$, substitution into [\[eq:domain\]](#eq:domain){reference-type="eqref" reference="eq:domain"} gives $$\begin{aligned}
 U_\tau D_\kappa&=D_{\kappa\mathrm e^{-2\mathrm i\sigma\tau}},\nonumber\\
 U_\tau H_{\sigma,\kappa}U_\tau^{-1}
 &=\mathrm e^{-2\tau}H_{\sigma,\kappa\mathrm e^{-2\mathrm i\sigma\tau}}.
 \label{eq:scale}\end{aligned}$$ Hence a fixed self-adjoint domain is invariant exactly when $\tau\in(\pi/\sigma)\mathbb Z$. No self-adjoint domain is continuously homogeneous. This cycle is in domain space; it does not use the original Hamiltonian time. The scattering formula has $$t(k\mathrm e^{\pi/\sigma})=t(k),\qquad
 R(k\mathrm e^{\pi/\sigma})=R(k),\qquad S(k\mathrm e^{\pi/\sigma})=S(k).$$ The logarithmic period $\pi/\sigma$ is the least positive one, because the Möbius map $t\mapsto(a-tb)/(b-ta)$ is injective: its determinant is $a^2-b^2\ne0$. The same scale produces the bound ratio $|E_{j+1}|/|E_j|=\mathrm e^{-2\pi/\sigma}$. Neither scale has a rational-prime origin.

For every unit boundary parameter, the group $\mathrm e^{-\mathrm itH}$ exists for every real time and has no nonzero full return time. For every $t>0$ the operator $\mathrm e^{-tH}$ is unbounded. Every resolvent of $H$ is noncompact and therefore belongs to no Schatten class. The bilateral series $\sum_{j\in\mathbb Z}(-E_j)^{-s}$ converges at no complex value of $s$.

Self-adjointness gives the unitary group. On the nonzero absolutely continuous subspace, multiplication by $\mathrm e^{-\mathrm itk^2}$ cannot be identically one unless $t=0$. The complete group is thus distinct from both the collision flow and the domain dilation cycle. Since $E_j\to-\infty$, the heat values $\mathrm e^{-tE_j}$ diverge along normalized eigenvectors for every $t>0$.

On a bounded positive spectral interval the resolvent is multiplication by $(k^2-z)^{-1}$, bounded away from zero. Infinitely many normalized functions with disjoint spectral supports have images separated in norm; therefore that resolvent is not compact. No ordinary Fredholm determinant of $I-w(H-z)^{-1}$ is available.

For the bilateral series, terms along $j\to+\infty$ fail to vanish when $\mathop{\mathrm{Re}}s\ge0$ and terms along $j\to-\infty$ fail when $\mathop{\mathrm{Re}}s\le0$. Both conditions are necessary, so no value of $s$ works. The corresponding unregularized product $\prod_j(1-w/E_j)$ has no nonzero neighborhood of convergence, since its factors fail to tend to one along $E_j\to0$.

The obstruction concerns *ordinary* constructions. It does not prohibit relative resolvents or explicitly renormalized determinants, and it does not identify any such different object with an arithmetic target. The strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}),$$ with overall `ROUTE_A_REJECTED`. A4 records only the natural differential expression and the proved domains; the free boundary parameter is not selected by the classical source. No arithmetic local data, target Euler factor, root number, automorphy, target divisor or counting law, target functional equation, target-zero match, or Hilbert--Pólya operator is claimed. Route B remains disabled. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Reproducibility and literature ownership

The exact producer contains 45 classical phase points, 27 boundary-flux rows and 15 algebraic scattering rows. A non-importing SymPy checker reconstructs their values and literal scalar types. Sixty bound-level and 36 continuum rows are stored to 60 digits after 100-digit evaluation and independently recomputed at 110 digits through endpoint-normalized coefficients. The separate symbolic lane checks eight identities. \>0 The 100-digit special-function lane checks 108 actual Stone-jump cells, 12 Green Wronskians, 12 differential-equation residuals, 12 endpoint matches, three bound-state normalization integrals and 36 logarithmic-period cells. In particular, testing $|R|=1$ alone is not treated as a spectral-density test. These finite grids are regression, not interval certification or a proof of spectral completeness. Two unrelated working-directory replays, repaired-hash attacks, strict YAML gates and smoke tests are distributed with the proof. The release rebuilds all three drafts in fresh directories with frozen epoch 1788566400 and retains actual settled compiler logs.

The external mathematical ownership is concentrated in one directly inspected primary source [@dr2017]; listing its journal and preprint as two independent works would be misleading. The paper does not claim priority for the self-adjoint family, geometric ladder or scattering formulas. Its package-level advance is the joined, auditable boundary between that complete source theorem and a target spectral construction it does not provide. The neighboring repository models are a Friedrichs Aharonov--Bohm Hamiltonian, a repulsive many-body Calogero--Moser system and a positive isotonic oscillator. They do not contain this strictly supercritical, imaginary-order, all-domain bilateral ladder. The proof and source audit preserve those owner differences.

Local collaborating AI agents reviewed the proof and its normalization; this is not external human peer review or cross-provider validation. An independent reading prompted direct Green/Stone tests and a fully expanded normalization identity, both implemented here. No outside model was invoked.

# Conclusion

Round zero: domains and the complete bound ladder. The original source has an explicit collision clock and a complete circle of quantum self-adjoint domains. The bilateral negative spectrum has no lowest level. This closes the endpoint and bound-state foundation without pretending that a classical collision law selected a boundary phase. Round one: complete continuum and scattering. The Green boundary jump and endpoint analysis close both spectral components. The normalized reflection and relative scattering phases remain distinct, and the precise external wave-operator theorem supplies time-dependent completeness only on the absolutely continuous subspace. Round two: scale cycles and ordinary-determinant obstruction. The domain circle, bilateral ladder and continuous scattering fit one convention-complete theorem. Natural self-adjointness gives a unitary group, but neither a ground state, a bounded heat operator, compact resolvent nor an ordinary bilateral-zeta germ. The negative Route-A verdict is part of the result, not a reason to change the source clock or insert target data.

1 J. Dereziński and S. Richard. On Schrödinger operators with inverse square potentials on the half-line. *Annales Henri Poincaré* **18**, 869--928 (2017). [doi:10.1007/s00023-016-0520-7](https://doi.org/10.1007/s00023-016-0520-7). Author manuscript: [arXiv:1604.03340v2](https://arxiv.org/abs/1604.03340v2). The theorem numbering used here follows that inspected preprint.
