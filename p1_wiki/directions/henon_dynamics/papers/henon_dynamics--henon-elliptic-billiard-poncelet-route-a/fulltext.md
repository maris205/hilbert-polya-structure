---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-elliptic-billiard-poncelet-route-a"
canonical_tex: "henon_dynamics/henon_elliptic_billiard_poncelet_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_elliptic_billiard_poncelet_route_a/paper/main.pdf"
source_sha256: "28db7e5762b7745606e2e2bb430658a85a1011f4171b0cde155280226d7b2d7a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Elliptic Billiards as Exact Poncelet Rotations: Monotonicity, Porisms, and the Clean-Family Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_elliptic_billiard_poncelet_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_elliptic_billiard_poncelet_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_elliptic_billiard_poncelet_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_elliptic_billiard_poncelet_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the billiard inside a confocal ellipse, restricted to positively oriented orbits with an elliptic caustic, we give the exact Jacobi covering and rigid rotation number. \>0 We prove strict monotonicity in both eccentricities, both rotation endpoints, and that reduced rotation $p/q$ makes every orbit on the caustic curve a least-period-$q$ Poncelet polygon. \>1 The $q$th restricted return is the identity with unit tangent derivative on a full periodic circle, obstructing the requested ordinary isolated-orbit product. A 613-cell receipt audits every convention. The theorem excludes hyperbolic caustics and makes no ambient unipotent or target spectral claim.
author:
- 'Route-A source-local certificate HCS-C275'
date: 1 September 2026
title: |
  Elliptic Billiards as Exact Poncelet Rotations:\
  Monotonicity, Porisms, and the Clean-Family Obstruction
```

## Markdown 正文

suppressoptionalinfo 767 trailerid \[\<C2752026090100000000000000000000\>\<C2752026090100000000000000000000\>\]

# The frozen confocal owner

For $0<\varepsilon<1$ let $$E(\varepsilon)=\left\{(x,y):\varepsilon^2x^2+
 \frac{\varepsilon^2}{1-\varepsilon^2}y^2=1\right\}.$$ Its foci are $(\pm1,0)$. Fix $0<f<e<1$: $E(f)$ is the outer billiard boundary and $E(e)$ is an inner elliptic caustic. We keep the positive orientation and one-reflection clock. The corresponding Poncelet circle map is denoted $B_e^f:E(f)\to E(f)$. This is precisely the elliptic-caustic sector analyzed in the primary rotation-number sources [@LM; @Kol; @CF]; hyperbolic caustics are not included.

Our convention is $$F(\phi,e)=\int_0^\phi\frac{d\tau}{\sqrt{1-e^2\sin^2\tau}},
 \qquad K(e)=F(\tfrac\pi2,e),$$ so $e$ is the Jacobi modulus (software parameter $m=e^2$). Define $$\begin{aligned}
 \omega(e,f)&=\arcsin\sqrt{\frac{e^2-f^2}{e^2(1-f^2)}},\label{eq:omega}\\
 \rho(e,f)&=\frac{F(\omega(e,f),e)}{2K(e)}.\label{eq:rho}\end{aligned}$$

The period-one covering $$\pi_e^f(\theta)=\frac1f\left(
 -\operatorname{sn}(4K(e)\theta,e),
 \sqrt{1-f^2}\,\operatorname{cn}(4K(e)\theta,e)\right)                 \tag{3}$$ satisfies $$B_e^f\circ\pi_e^f=\pi_e^f\circ R_{\rho(e,f)},
 \qquad R_\rho(\theta)=\theta+\rho.$$ In particular, [\[eq:rho\]](#eq:rho){reference-type="eqref" reference="eq:rho"} is the rotation number.

The identity $\operatorname{sn}^2+\operatorname{cn}^2=1$ puts (3) on $E(f)$, and the $4K(e)$ period gives the deck map $\theta\mapsto\theta+1$. Set $v=2F(\omega,e)$. The Jacobi addition formulas, together with [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"}, show that the line through $\pi_e^f(\theta)$ and $\pi_e^f(\theta+v/(4K(e)))$ obeys $$C^2=A^2/e^2+(1-e^2)B^2/e^2$$ when written as $Ax+By+C=0$. This is the dual equation for tangency to $E(e)$. Positive orientation selects the next intersection, proving the conjugacy; $v/(4K(e))$ is exactly [\[eq:rho\]](#eq:rho){reference-type="eqref" reference="eq:rho"}. This also verifies the hypotheses and conclusion of the confocal covering theorem in [@LM].

\>0

# Strict parameter rigidity and endpoints

The inverse form of [\[eq:rho\]](#eq:rho){reference-type="eqref" reference="eq:rho"} is especially effective: $$\rho(e,f)=\ell\quad\Longleftrightarrow\quad
 f=R(\ell,e):=e\,\operatorname{cd}(2K(e)\ell,e),
 \qquad 0<\ell<\tfrac12.                                \tag{4}$$

Throughout $0<f<e<1$, $$\partial_e\rho(e,f)>0,\qquad \partial_f\rho(e,f)<0.$$ Moreover, $$\lim_{f\to e^-}\rho=\lim_{e\to f^+}\rho=0,
 \qquad
 \lim_{f\to0^+}\rho=\lim_{e\to1^-}\rho=\tfrac12,$$ where the parameter not tending to its boundary is held fixed.

Let $u=2K(e)\ell$ and $\mathcal E(u,e)=\int_0^u\operatorname{dn}^2(t,e)\,dt$. Differentiating (4) gives $$R_\ell=-\frac{2e(1-e^2)K(e)\operatorname{sn}(u,e)}{\operatorname{dn}^2(u,e)}<0$$ and $$R_e=\operatorname{cd}(u,e)+\frac{\operatorname{sn}(u,e)}{\operatorname{dn}^2(u,e)}
 [\mathcal E(u,e)-2\ell\mathcal E(K(e),e)].$$ Since $\operatorname{dn}^2(t,e)$ strictly decreases on $(0,K(e))$, its average on $[0,u]$ exceeds its average on $[0,K(e)]$; the bracket and hence $R_e$ are positive. Implicit differentiation of $f=R(\rho,e)$ yields $\rho_f=1/R_\ell<0$ and $\rho_e=-R_e/R_\ell>0$.

The two coalescing limits follow from $\omega\to0$; $f\to0$ gives $\omega\to\pi/2$ and $F\to K$. For fixed $f$ and $e\to1^-$, put $e'=\sqrt{1-e^2}$. Then $\cos\omega=O(e')$ and $$0\le K(e)-F(\omega,e)=
 \int_\omega^{\pi/2}\frac{dt}{\sqrt{1-e^2\sin^2t}}=O(1),$$ whereas $K(e)\sim\log(4/e')\to\infty$. Thus $F/K\to1$ and the last limit is $1/2$.

If $\rho(e,f)=p/q$ with $0<p/q<1/2$ and $\gcd(p,q)=1$, every orbit on this caustic curve has minimal period $q$.

In the covering coordinate, the $q$th iterate sends $\theta$ to $\theta+p$, a deck-equivalent point. If $0<k<q$ returned, then $kp/q$ would be integral; coprimality would force $q\mid k$, a contradiction. The arbitrary starting value of $\theta$ produces the continuous Poncelet family, recovering the porism statement of [@CF].

\>1

# The clean family and the Route-A boundary

The conjugacy gives more than a period count: $$(R_{p/q})^q(\theta)=\theta+p,\qquad
 D_\theta(R_{p/q})^q=1.$$ Consequently $(B_e^f)^q$ restricted to this invariant circle is the identity, and its tangent derivative is one at every point. The fixed set is a circle, not a discrete collection. Hence the ordinary isolated-primitive-orbit product requested at A2, and a nondegenerate isolated-fixed-point denominator, are unavailable on the rational caustic. This does not rule out a separately defined Morse--Bott or Berry--Tabor regularization. It also does not determine the transverse multiplier or assert an ambient Jordan/unipotent form.

The receipt contains 32 rotation-formula cells, 192 covering and tangent-chord cells, 117 strict-monotonicity values, 96 endpoint values, 24 inverse-porism cases, 128 polygon vertices, and 24 restricted-return derivative cells. A producer-independent checker, 208 exact symbolic checks, fresh byte replay, and 24 repaired-hash mutations audit the package. Finite cells test conventions; the preceding arguments prove the parameter theorem.

Let $\Omega_f$ be the smooth bounded interior of $E(f)$. Its standard ambient Dirichlet operator is self-adjoint with compact resolvent on $L^2(\Omega_f)$, with $$-\Delta_D,\qquad
 \mathcal D(-\Delta_D)=H^2(\Omega_f)\cap H_0^1(\Omega_f).$$ The unitary group $U(t)=\exp[-it(-\Delta_D)]$ uses continuous physical flight time. Complex conjugation $C$ is antiunitary and obeys $CU(t)C=U(-t)$. This is a coherent ambient quantum billiard, but the frozen classical owner is the one-reflection Poincaré map. No same-clock quantum return has been constructed, and no theorem shows that such a return retains the fixed-caustic orbit phases and weights. Therefore A4 is only $$\texttt{A4\_FORMAL\_HINT}.$$ No quantum spectrum is identified with a target divisor. The frozen scope is $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$ Its strict tuple is $$\begin{gathered}
 \texttt{(A0\_FAIL,A1\_PASS\_ANALYTIC,A2\_FAIL,}\\
 \texttt{A3\_FAIL,A4\_FORMAL\_HINT)}.
 \end{gathered}$$ The overall verdict is `ROUTE_A_REJECTED`; Route B is disabled. The theorem covers only the positive-orientation elliptic-caustic sector.

9 H. E. Lomelí and J. D. Meiss, *Symmetry Reduction and Rotation Numbers for Poncelet maps*, arXiv:2309.08013v1 (2023), [doi:10.48550/arXiv.2309.08013](https://doi.org/10.48550/arXiv.2309.08013). R. Kołodziej, *The rotation number of some transformation related to billiards in an ellipse*, Studia Math. 81 (1985), 293--302, [doi:10.4064/sm-81-3-293-302](https://doi.org/10.4064/sm-81-3-293-302). S.-J. Chang and R. Friedberg, *Elliptical billiards and Poncelet's theorem*, J. Math. Phys. 29 (1988), 1537--1550, [doi:10.1063/1.527900](https://doi.org/10.1063/1.527900).
