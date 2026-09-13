---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-landau-zener-weber-scattering-route-a"
canonical_tex: "henon_dynamics/henon_landau_zener_weber_scattering_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_landau_zener_weber_scattering_route_a/paper/main.pdf"
source_sha256: "fd6d89863d9c49e41459707088aba703836a5972566668a540c1f22ff3009b18"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Landau--Zener--Weber Scattering: Exact Connection Data and\newline Finite-Window Unitary Controls

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_landau_zener_weber_scattering_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_landau_zener_weber_scattering_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_landau_zener_weber_scattering_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_landau_zener_weber_scattering_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We analyze the genuinely nonautonomous two-level crossing $i\dot\psi=[(vt/2)\sigma_z+g\sigma_x]\psi$, $v>0$. Eliminating one component gives a pair of parabolic-cylinder (Weber) equations. Their connection formula yields, in a fixed diabatic gauge, the exact asymptotic survival law $P_\mathrm{diab}=\exp(-2\pi g^2/v)$ and the Stokes/Gamma phase $\phi_S=\pi/4+\delta(\log\delta-1)+\arg\Gamma(1-i\delta)$. Wronskian conservation proves an $SU(2)$ scattering matrix, while elementary calculus gives strict monotonicity and sudden/adiabatic limits. A separate 80-digit, fixed-step RK4 ledger checks finite windows without calling them an exact finite-time formula. The source-local theorem is a unitary/scattering candidate only: it supplies no arithmetic owner, target divisor, or Hilbert--Polya bridge.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Landau--Zener--Weber Scattering: Exact Connection Data andFinite-Window Unitary Controls'
```

## Markdown 正文

suppressoptionalinfo 611

# Crossing and conventions

Set $\hbar=1$, $\sigma_z=\operatorname{diag}(1,-1)$, and use the diabatic basis at both ends of time: $$H(t)=\frac{vt}{2}\sigma_z+g\sigma_x,
 \qquad i\frac{d}{dt}\binom{a}{b}=H(t)\binom{a}{b},
 \qquad v>0,\ g\in\mathbb R .                         \label{eq:model}$$ The physical clock is $t$; there is no fitted repetition or target clock. We write $\delta=g^2/v$ and fix the asymptotic phase convention by the matrix in Theorem [\[thm:scattering\]](#thm:scattering){reference-type="ref" reference="thm:scattering"}. Conjugating by $\sigma_z$ maps $g$ to $-g$.

[\[thm:scattering\]]{#thm:scattering label="thm:scattering"} For $g\ne0$, the components of a solution of [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"} satisfy $$\begin{aligned}
 a''+\left(g^2+\frac{v^2t^2}{4}+\frac{iv}{2}\right)a&=0,\\
 b''+\left(g^2+\frac{v^2t^2}{4}-\frac{iv}{2}\right)b&=0.               \label{eq:weber}\end{aligned}$$ After the usual rotation of $t$ and affine rescaling these are Weber parabolic-cylinder equations. Unit-flux connection data from $t=-\infty$ to $t=+\infty$ are $$S(\delta)=\begin{pmatrix}
 \sqrt P&-\sqrt{1-P}\,e^{i\phi_S}\\
 \sqrt{1-P}\,e^{-i\phi_S}&\sqrt P
 \end{pmatrix},\quad
 P=e^{-2\pi\delta},\quad
 \phi_S=\frac\pi4+\delta(\log\delta-1)+\arg\Gamma(1-i\delta),       \label{eq:S}$$ with $\phi_S(0)=\pi/4$ by continuity. A different diagonal asymptotic phase convention conjugates $S$ by diagonal unitaries and leaves $P$ intact.

From the first component equation, $b=(ia'-(vt/2)a)/g$. Substitution into the second gives the first equation in [\[eq:weber\]](#eq:weber){reference-type="eqref" reference="eq:weber"}; exchanging components gives the second. The rotated equation is the standard parabolic-cylinder equation. Its connection identity and constant Wronskian produce the two entries in [\[eq:S\]](#eq:S){reference-type="eqref" reference="eq:S"}; the modulus identity $|\Gamma(1+i\delta)|^2=\pi\delta/\sinh(\pi\delta)$ reduces the diagonal coefficient to $e^{-\pi\delta}$. This is a source-local special function calculation, with no external spectral data.

[\[prop:inv\]]{#prop:inv label="prop:inv"} For real parameters, $H(t)=H(t)^*$ and every finite-time propagator preserves the Hermitian norm. The Weber Wronskian gives the same flux identity at the two ends, so $S^*S=I$ and $\det S=1$. Moreover $$\frac{dP}{d\delta}=-2\pi e^{-2\pi\delta}<0\quad(\delta>0),\qquad
 \left.\frac{\partial P}{\partial g}\right|_v=-\frac{4\pi g}{v}e^{-2\pi g^2/v},
 \label{eq:deriv}$$ and $\phi_S'(\delta)=\log\delta-\Re\psi(1-i\delta)$.

Hermiticity gives $(\psi^*\psi)'=0$; the Wronskian is the equivalent constant flux in the Weber basis. Direct multiplication of [\[eq:S\]](#eq:S){reference-type="eqref" reference="eq:S"} proves the $SU(2)$ identities. Differentiating $e^{-2\pi\delta}$ gives [\[eq:deriv\]](#eq:deriv){reference-type="eqref" reference="eq:deriv"}; differentiating $\log\Gamma(1-i\delta)$ gives the phase derivative.

# Limits, boundaries, and a finite-window control

The crossing parameter organizes the singular faces. As $\delta\downarrow0$, $$P=1-2\pi\delta+O(\delta^2),\qquad 1-P=2\pi\delta+O(\delta^2),$$ so the sudden limit $v\to\infty$ is diabatic. At fixed $g\ne0$, $v\downarrow0$ gives $P\to0$ (adiabatic following). At $g=0$ the two channels decouple exactly, and the continuous phase convention is used. The sign change $g\mapsto-g$ is a constant $\sigma_z$ gauge, not a new probability law. The point $t=0$ is the sole diabatic gap closing; it is the turning point of the Weber connection problem.

For validation, we integrated both basis vectors of [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"} on $[-T,T]$ with a fixed 2048-step classical RK4 scheme at 80 decimal digits. The ledger records all four complex entries, $P_{\rm window}=|U_{11}|^2$, $|P_{\rm window}-P|$, and $\|U^*U-I\|_{\max}$. It is a controlled numerical window, not an exact finite-time propagator. Representative exact rows are:

::: {#tab:scattering}
  case               $v$      $g$   $\delta$  $P_\mathrm{diab}$     $\phi_S$
  -------------- ------- -------- ---------- ------------------- --------------
  reference            1    $1/2$      $1/4$    0.2078795764      0.3270619133
  fast/weak            4    $1/3$     $1/36$    0.8398492016      0.6741033767
  slow/strong      $1/4$    $3/4$      $9/4$    0.0000007249      0.0372977224
  negative $g$         2   $-1/2$      $1/8$    0.4559381278      0.4718436007
  uncoupled        $3/2$        0          0          1           0.7853981634

  : Exact source-local scattering rows in the fixed gauge.
:::

The finite ledger has 15 rows ($T=2,4,8$ for each case). The largest Gram residual is $1.56\times10^{-5}$ with the 2048-step control; discrepancies are reported as finite-window effects. A producer-independent checker recomputes the ODE, while a separate SymPy program checks the signs in [\[eq:weber\]](#eq:weber){reference-type="eqref" reference="eq:weber"}, the Pauli square, $SU(2)$ determinant, monotonicity, and the coupling gauge. The machine-readable field is written literally as `P_diabatic`; the scope lock is `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Relation to the Route-A decision

The theorem is a complete physical scattering result, but a single swept crossing has no primitive periodic-orbit repetition law. The parameter $\delta$ is a source coupling ratio, not an arithmetic label; $P$ and $\phi_S$ are not target zeros or divisor data. Thus the strict tuple is

(A0\_FAIL, A1\_FAIL, A2\_FAIL, A3\_FAIL, A4\_UNITARY\_OR\_SCATTERING\_CANDIDATE),

with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. This nonautonomous model is intentionally distinct from the autonomous Jaynes--Cummings excitation blocks of C223. No target operator, Euler factor, root number, automorphy claim, or Hilbert--Polya bridge is made.

# Reproducibility and source note {#reproducibility-and-source-note .unnumbered}

The receipt is generated by `code/c224_landau_zener_producer.py` using exact rational sentinels, 80-digit Gamma evaluation, and deterministic RK4. The independent checker, symbolic cross-check, clean replay, and hostile mutation suite are run in separate processes. The fixed-epoch LuaLaTeX build is repeated twice; the three revision PDFs are content-distinct and the final `main.pdf` is byte-identical to round 2. The release manifest closes exactly 27 payload files and excludes itself and build sidecars.

The source audit records the following DOI-verified references:

9 C. Zener, "Non-adiabatic crossing of energy levels," *Proceedings of the Royal Society A* 137 (1932), 696--702. DOI: [10.1098/rspa.1932.0165](https://doi.org/10.1098/rspa.1932.0165). N. V. Vitanov and B. M. Garraway, "Landau-Zener model: Effects of finite coupling duration," *Physical Review A* 53 (1996), 4288--4304. DOI: [10.1103/PhysRevA.53.4288](https://doi.org/10.1103/PhysRevA.53.4288). S. N. Shevchenko, S. Ashhab, and F. Nori, "Landau-Zener-Stuckelberg interferometry," *Physics Reports* 492 (2010), 1--30. DOI: [10.1016/j.physrep.2010.03.002](https://doi.org/10.1016/j.physrep.2010.03.002).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic or Hilbert--Polya claim. **Data and code.** All rows and audits are released with HCS-C224. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked displayed claims and metadata. This is not external peer review.
