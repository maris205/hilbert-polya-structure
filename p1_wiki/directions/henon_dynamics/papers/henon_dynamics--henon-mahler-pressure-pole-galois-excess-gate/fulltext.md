---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mahler-pressure-pole-galois-excess-gate"
canonical_tex: "henon_dynamics/henon_mahler_pressure_pole_galois_excess_gate/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_mahler_pressure_pole_galois_excess_gate/paper/paper.pdf"
source_sha256: "d3b989edf47fbebc61dffbb3a5c4bbf2abdb37804954aef7e2574440b4dda55c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Physical Pressure Pole and the Galois-Excess Gate for Hénon Mahler Heights

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mahler_pressure_pole_galois_excess_gate>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mahler_pressure_pole_galois_excess_gate/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mahler_pressure_pole_galois_excess_gate/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mahler_pressure_pole_galois_excess_gate/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mahler_pressure_pole_galois_excess_gate/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a certified mixing hyperbolic survivor of the area-preserving Hénon map, an earlier all-orbit Abel law attached to every primitive orbit $\gamma$ the Mahler height $\mathcal H_\gamma$ of its algebraic return multiplier. Its pressure-critical behavior remained hidden behind a crude algebraic-degree majorant. We prove the canonical splitting $\mathcal H_\gamma=\ell_\gamma+\mathcal E_\gamma$, where $\ell_\gamma=\log\Lambda_\gamma$ is the physical instability length and $\mathcal E_\gamma\ge0$ is the contribution of nonphysical reciprocal Galois pairs. The physical primitive amplitude is the first-repetition part of the logarithmic derivative of the entropy-one suspension zeta. It therefore has a meromorphic germ at the pressure line $s=1$, with simple-pole residue $3/(\pi^2h_*)$. Exact periods one, three and four show that the full Mahler height is not a constant rescaling of the instability roof, even modulo a coboundary. We formulate an exact trichotomy using the convergence abscissa of the Galois excess and prove conditionally that a single Hölder periodic-sum realization of that excess would give the full amplitude a critical simple pole with an equilibrium-average residue. The physical pole is unconditional; the Hölder realization, rational-prime trace and operator interpretation remain open.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  A Physical Pressure Pole and the Galois-Excess Gate\
  for Hénon Mahler Heights
```

## Markdown 正文

# Introduction

Periodic-orbit constructions inspired by Hilbert--Pólya require two kinds of discipline. The orbit weights must be intrinsic to the dynamics, and a finite or safely convergent expansion must not be confused with a global spectral determinant. This distinction is especially sharp for algebraic weights attached to a hyperbolic Hénon survivor.

We work with the area-preserving map $$H_6(q,p)=(1-6q^2-p,q),$$ a conservative member of the Hénon family introduced in [@Henon1976]. The repository chain HCS-C31 and HCS-C45 certified a mixing four-state hyperbolic survivor, a positive non-lattice instability roof $\tau=\log J^u$, and its pressure normalization $\widehat\tau=h_*\tau$ with entropy one [@WangP31; @WangP45]. HCS-P53 then associated to each primitive orbit a source-tagged cyclotomic packet whose Abel coefficient is the full Mahler height of the algebraic return multiplier [@WangP53]. The resulting all-orbit amplitude is $$\mathcal A(s)=\frac3{\pi^2}
\sum_{\gamma\ \mathrm{primitive}}
\mathcal H_\gamma e^{-s h_*\ell_\gamma},
\qquad
\ell_\gamma=\log\Lambda_\gamma.
\label{eq:total-amplitude}$$ It was proved only for $\Re s>3.125206\ldots$, far to the right of the normalized pressure line $\Re s=1$.

The key point of this paper is that $\mathcal H_\gamma$ contains two mathematically different quantities. The physical real embedding contributes exactly $\ell_\gamma$, a Hölder periodic sum. Every other reciprocal Galois pair outside the unit circle contributes an additional nonnegative amount. We call the latter the *Galois excess*. Separating these terms turns the vague question "is Mahler height thermodynamic?" into two precise questions: what singularity is already forced by the physical roof, and what must be proved about the excess?

Our first main result answers the former completely. Parry and Pollicott's zeta theorem for weak-mixing suspensions [@ParryPollicott1990 Theorem 6.3 and Corollary 6.3.1] shows that the entropy-one suspension zeta has a simple pole at $s=1$. After removing the normally convergent repetition tail, its logarithmic derivative gives the primitive physical amplitude and the exact residue $3/(\pi^2h_*)$.

The second result isolates the arithmetic gate. Exact orbit multipliers show positive Galois excess at periods one and three but zero excess at period four. Thus no constant multiple of the instability roof, even after adding a coboundary, can realize the full height. We define the excess convergence abscissa and derive a three-regime pressure classification. Finally, using the two-parameter theorem of @ParryPollicott1990 [Theorem 6.4 and Corollary 6.4.1], we prove that an exact Hölder periodic-sum realization of the excess would close the full critical pole and determine its residue.

The qualifier is essential. No source currently identifies the nonphysical Galois embeddings of an orbit multiplier with a local observable on the physical symbolic survivor. We therefore obtain a proved physical pole, a proved obstruction to the easiest completion, and a conditional full-pole theorem---not a completed Riemann determinant or Hilbert--Pólya operator.

# The frozen pressure-normalized survivor

Let $\Sigma_A$ be the four-state mixing subshift conjugate to the certified locally maximal H6 survivor. On $\Sigma_A$, the adapted unstable Jacobian has a positive Hölder logarithm $\tau$, unique at the periodic-sum level up to a Hölder coboundary. Its pressure root is defined intrinsically by $$P_{\Sigma_A}(-h_*\tau)=0,
\qquad
0.277980<h_*<0.277987.
\label{eq:pressure-root}$$ Set $\widehat\tau=h_*\tau$. The suspension over $\Sigma_A$ with roof $\widehat\tau$ has entropy one. The inherited exact multiplier comparison proves that the roof is non-lattice, hence the suspension is weak mixing.

For a primitive orbit $\gamma$ of symbolic period $m(\gamma)$, choose a point $x_\gamma$ on the cycle and write $$\ell_\gamma=S_{m(\gamma)}\tau(x_\gamma)
=\log\Lambda_\gamma,
\qquad
\widehat\ell_\gamma=h_*\ell_\gamma.
\label{eq:lengths}$$ All objects in [\[eq:pressure-root\]](#eq:pressure-root){reference-type="eqref" reference="eq:pressure-root"}--[\[eq:lengths\]](#eq:lengths){reference-type="eqref" reference="eq:lengths"} are fixed before the arithmetic Mahler coefficient is examined.

The normalized suspension zeta is $$\zeta_{\widehat\tau}(s)
=\prod_{\gamma\ \mathrm{primitive}}
\left(1-e^{-s\widehat\ell_\gamma}\right)^{-1}.
\label{eq:zeta}$$ The prime orbit theorem gives $$\#\{\gamma:\widehat\ell_\gamma\le T\}\sim e^T/T
\qquad(T\to\infty)
\label{eq:pot}$$ by @ParryPollicott1990 [Theorem 6.9]. This is a theorem about dynamical primes. No rational-prime identification is used in the present paper.

# Mahler height and the Galois excess

Let $f_\gamma\in\mathbb Z[X]$ be the monic minimal polynomial of the signed unstable multiplier $\lambda_\gamma$. Its conjugates occur in reciprocal pairs. From each pair choose $\rho$ with $|\rho|\ge1$. The P53 embedding formula is $$\mathcal H_\gamma=\log M(f_\gamma)
=\sum_{\rho}\log|\rho|.
\label{eq:height-embedding}$$ The physical real pair contributes $\log\Lambda_\gamma=\ell_\gamma$.

The *Galois excess* of $\gamma$ is $$\mathcal E_\gamma
=\sum_{\substack{\rho\ \mathrm{nonphysical}\\|\rho|\ge1}}
\log|\rho|
=\mathcal H_\gamma-\ell_\gamma.
\label{eq:excess}$$

For every primitive orbit, $$\mathcal H_\gamma=\ell_\gamma+\mathcal E_\gamma,
\qquad \mathcal E_\gamma\ge0.
\label{eq:split}$$ Consequently, wherever [\[eq:total-amplitude\]](#eq:total-amplitude){reference-type="eqref" reference="eq:total-amplitude"} converges absolutely, $$\mathcal A=\mathcal A_{\rm phys}+\mathcal A_{\rm Gal},
\label{eq:amp-split}$$ with $$\begin{aligned}
\mathcal A_{\rm phys}(s)
&=\frac3{\pi^2}\sum_\gamma
\ell_\gamma e^{-s\widehat\ell_\gamma},
\label{eq:physical}\\
\mathcal A_{\rm Gal}(s)
&=\frac3{\pi^2}\sum_\gamma
\mathcal E_\gamma e^{-s\widehat\ell_\gamma}.
\label{eq:galois}\end{aligned}$$

Every term in [\[eq:height-embedding\]](#eq:height-embedding){reference-type="eqref" reference="eq:height-embedding"} is nonnegative. Isolating the physical reciprocal pair proves [\[eq:split\]](#eq:split){reference-type="eqref" reference="eq:split"}; substitution proves [\[eq:amp-split\]](#eq:amp-split){reference-type="eqref" reference="eq:amp-split"}.

This splitting is intrinsic. It does not choose a fitted observable or change the pressure clock. It also shows why replacing $\mathcal H_\gamma$ by $\ell_\gamma$ without an error ledger would discard arithmetic information.

# The physical pressure pole

Logarithmic differentiation of [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} in its convergence half-plane gives $$-\frac{\zeta'_{\widehat\tau}}{\zeta_{\widehat\tau}}(s)
=\sum_\gamma\sum_{k\ge1}
\widehat\ell_\gamma e^{-sk\widehat\ell_\gamma}.
\label{eq:logder}$$ Because the suspension is weak mixing and $P(-\widehat\tau)=0$, @ParryPollicott1990 [Theorem 6.3 and Corollary 6.3.1] give $$-\frac{\zeta'_{\widehat\tau}}{\zeta_{\widehat\tau}}(s)
=\frac1{s-1}+G_0(s)
\label{eq:zeta-principal}$$ as a meromorphic germ, with $G_0$ holomorphic near $s=1$.

The series $$R(s)=\sum_\gamma\sum_{k\ge2}
\widehat\ell_\gamma e^{-sk\widehat\ell_\gamma}
\label{eq:tail}$$ converges normally for $\Re s>1/2$.

The prime orbit theorem [\[eq:pot\]](#eq:pot){reference-type="eqref" reference="eq:pot"} implies convergence of $\sum_\gamma\widehat\ell_\gamma e^{-u\widehat\ell_\gamma}$ for every real $u>1$, by Stieltjes integration. Fix a compact set on which $\Re s\ge\sigma>1/2$, and let $L_{\min}>0$ be the minimum primitive suspension length. Then $$\sum_{k\ge2}\widehat\ell_\gamma
 |e^{-sk\widehat\ell_\gamma}|
 \le
 \frac{\widehat\ell_\gamma e^{-2\sigma\widehat\ell_\gamma}}
 {1-e^{-\sigma L_{\min}}}.$$ The sum of the right-hand side over $\gamma$ converges because $2\sigma>1$. The Weierstrass test proves normal convergence.

The primitive physical amplitude has a meromorphic germ at $s=1$ and $$\boxed{
\mathcal A_{\rm phys}(s)
=\frac{3}{\pi^2h_*}\frac1{s-1}+G_{\rm phys}(s)},
\label{eq:physical-pole}$$ where $G_{\rm phys}$ is holomorphic near $1$. Moreover, $$1.093445200412297389\ldots
<\operatorname*{Res}_{s=1}\mathcal A_{\rm phys}
<1.093472735186032499\ldots.
\label{eq:residue-interval}$$

Subtract [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} from [\[eq:logder\]](#eq:logder){reference-type="eqref" reference="eq:logder"} and use [\[eq:zeta-principal\]](#eq:zeta-principal){reference-type="eqref" reference="eq:zeta-principal"}. The remaining first-repetition series has principal part $(s-1)^{-1}$. Since $\ell_\gamma=\widehat\ell_\gamma/h_*$, equation [\[eq:physical\]](#eq:physical){reference-type="eqref" reference="eq:physical"} gives [\[eq:physical-pole\]](#eq:physical-pole){reference-type="eqref" reference="eq:physical-pole"}. The endpoint values in [\[eq:residue-interval\]](#eq:residue-interval){reference-type="eqref" reference="eq:residue-interval"} follow from [\[eq:pressure-root\]](#eq:pressure-root){reference-type="eqref" reference="eq:pressure-root"} and the monotonicity of $3/(\pi^2h_*)$.

The theorem is all-period and source-backed. No finite orbit section is used to infer the pole.

# Exact Galois witnesses and a cohomological no-go

For a real reciprocal pair with trace $t$, $|t|>2$, the outside root has logarithmic modulus $$L(t)=\operatorname{arcosh}(|t|/2).
\label{eq:pair-log}$$ The exact inherited trace polynomials yield Table [1](#tab:excess){reference-type="ref" reference="tab:excess"}.

::: {#tab:excess}
   period   trace polynomial  trace roots                     Galois excess
  -------- ------------------ ------------------ ----------------------------------------
     1        $T^2-4T-24$     $2\pm2\sqrt7$        $\operatorname{arcosh}(\sqrt7-1)>0$
     3       $T^2+76T-7376$   $-38\pm42\sqrt5$    $\operatorname{arcosh}(21\sqrt5-19)>0$
     4          $T-578$       $578$                                $0$

  : Exact physical and nonphysical reciprocal-pair data.
:::

Numerically, the triples $(\ell_\gamma,\mathcal H_\gamma,\mathcal E_\gamma)$ are $$\begin{aligned}
m=1:&\quad(1.9673466291,\ 3.0501161905,\ 1.0827695614),\\
m=3:&\quad(4.8820992058,\ 8.9056092911,\ 4.0235100852),\\
m=4:&\quad(6.3595708754,\ 6.3595708754,\ 0).\end{aligned}$$

There do not exist a constant $c$ and a function $u$ on the symbolic survivor such that every primitive cycle satisfies $$\mathcal H_\gamma
=c\ell_\gamma+S_{m(\gamma)}(u-u\circ\sigma).
\label{eq:scalar-coboundary}$$

Periodic sums of a coboundary vanish. The period-four orbit has $\mathcal H_4=\ell_4>0$, so [\[eq:scalar-coboundary\]](#eq:scalar-coboundary){reference-type="eqref" reference="eq:scalar-coboundary"} forces $c=1$. The period-one orbit then contradicts $\mathcal E_1>0$.

Thus the full arithmetic height cannot be obtained by merely retuning the pressure parameter. This theorem does not exclude a new, non-proportional Hölder potential.

# The Galois-excess pressure trichotomy

Define the abscissa of the positive excess series by $$\sigma_{\rm Gal}
=\inf\left\{\sigma\in\mathbb R:
\sum_\gamma \mathcal E_\gamma
e^{-\sigma\widehat\ell_\gamma}<\infty\right\}.
\label{eq:sigma-gal}$$ The P53 all-orbit majorant proves $$\sigma_{\rm Gal}
\le \frac{\log(2\phi)}{h_*\log J_*}
<3.125207.
\label{eq:sigma-upper}$$ The physical series has abscissa one by Theorem 4.2 and the prime orbit theorem. Since both coefficient systems are nonnegative, the defining total series has abscissa $$\sigma_{\mathcal A}=\max\{1,\sigma_{\rm Gal}\}.
\label{eq:total-abscissa}$$

Exactly one of the following occurs.

1.  If $\sigma_{\rm Gal}<1$, then $\mathcal A_{\rm Gal}$ is holomorphic near $1$, and the full amplitude has the physical pole and residue [\[eq:physical-pole\]](#eq:physical-pole){reference-type="eqref" reference="eq:physical-pole"}.

2.  If $\sigma_{\rm Gal}=1$, then the excess occupies the same critical abscissa, but the abscissa alone determines neither convergence at $1$ nor the existence or residue of a singularity there. Those boundary data require a weighted thermodynamic theorem or equivalent analytic input.

3.  If $\sigma_{\rm Gal}>1$, then the positive defining excess series loses convergence before the physical pressure line.

Positive generalized Dirichlet series converge normally and define holomorphic functions to the right of their abscissa. Combine this fact with [\[eq:amp-split\]](#eq:amp-split){reference-type="eqref" reference="eq:amp-split"}, Theorem 4.2 and [\[eq:total-abscissa\]](#eq:total-abscissa){reference-type="eqref" reference="eq:total-abscissa"}.

The third case is a statement about the defining series. It does not exclude an analytic continuation established by a different theorem. The trichotomy replaces the crude safe half-plane by one exact unknown scalar, $\sigma_{\rm Gal}$.

# Conditional Hölder completion

We now state the precise theorem that would complete the pressure-critical bridge. Assume that there exists one real Hölder function $\psi:\Sigma_A\to\mathbb R$, fixed independently of the orbit, such that $$\mathcal E_\gamma=S_{m(\gamma)}\psi(x_\gamma)
\quad\text{for every primitive }\gamma.
\label{eq:holder-hypothesis}$$ This is not obtained by finite interpolation.

Consider the two-parameter zeta $$\zeta(s,z)=\prod_\gamma
\left(1-e^{-s\widehat\ell_\gamma+z\mathcal E_\gamma}\right)^{-1}.
\label{eq:two-param}$$ With $f=\widehat\tau$, $g=0$, $c=1$, and $k=\psi$, @ParryPollicott1990 [Theorem 6.4 and Corollary 6.4.1] gives $$\left.\partial_z\log\zeta(s,z)\right|_{z=0}
=\frac{\int\psi\,\mathrm d\mu}{\int\widehat\tau\,\mathrm d\mu}
\frac1{s-1}+G_\psi(s),
\label{eq:weighted-principal}$$ where $\mu$ is the equilibrium state of $-\widehat\tau$ and $G_\psi$ is holomorphic near one.

Here the source convention is $P(g-cf)=0$ and $$\mathfrak Z(s,z)=
 \exp\!\left(
 \sum_{n\ge1}\frac1n\sum_{\sigma^nx=x}
 e^{S_ng-csS_nf+zS_nk}
 \right).$$ Thus the above choices give exactly [\[eq:two-param\]](#eq:two-param){reference-type="eqref" reference="eq:two-param"}; in particular the source denominator $c\int f\,\mathrm d\mu$ becomes $\int\widehat\tau\,\mathrm d\mu$. We use only the resulting local meromorphic germ at $(s,z)=(1,0)$.

Under [\[eq:holder-hypothesis\]](#eq:holder-hypothesis){reference-type="eqref" reference="eq:holder-hypothesis"}, the full Mahler amplitude has a meromorphic simple-pole germ at $s=1$, with $$\boxed{
\operatorname*{Res}_{s=1}\mathcal A(s)
=\frac3{\pi^2}
\frac{\int(\tau+\psi)\,\mathrm d\mu}
{\int h_*\tau\,\mathrm d\mu}}.
\label{eq:full-residue}$$

Differentiating the Euler factors in [\[eq:two-param\]](#eq:two-param){reference-type="eqref" reference="eq:two-param"} shows that the left side of [\[eq:weighted-principal\]](#eq:weighted-principal){reference-type="eqref" reference="eq:weighted-principal"} equals $\sum_{\gamma,k\ge1}\mathcal E_\gamma
e^{-sk\widehat\ell_\gamma}$. If $a=\min\widehat\tau>0$, then $m(\gamma)\le\widehat\ell_\gamma/a$, and hence $|\mathcal E_\gamma|\le
\|\psi\|_\infty\widehat\ell_\gamma/a$. The $k\ge2$ weighted tail is therefore absolutely and normally dominated near one by the repetition tail of Lemma 4.1. The primitive excess series has the same residue. Adding the physical residue from Theorem 4.2 gives [\[eq:full-residue\]](#eq:full-residue){reference-type="eqref" reference="eq:full-residue"}.

For real $s>1$, the differentiated excess Euler product has nonnegative coefficients because every $\mathcal E_\gamma\ge0$. Multiplying [\[eq:weighted-principal\]](#eq:weighted-principal){reference-type="eqref" reference="eq:weighted-principal"} by $s-1$ and letting $s\downarrow1$ shows $\int\psi\,\mathrm d\mu/\int\widehat\tau\,\mathrm d\mu\ge0$. The physical residue is strictly positive, so the residue in [\[eq:full-residue\]](#eq:full-residue){reference-type="eqref" reference="eq:full-residue"} is strictly positive and the full pole cannot cancel.

Equation [\[eq:holder-hypothesis\]](#eq:holder-hypothesis){reference-type="eqref" reference="eq:holder-hypothesis"} remains open. The minimal-polynomial conjugates are global arithmetic data, whereas a Hölder potential is local on the physical symbolic survivor. An asymptotically additive replacement could also be useful, but would require its own weighted-zeta theorem and uniform error ledger.

# Certificate, Route-A status and limitations

The finite certificate is deliberately smaller than the source theorem. It locks eight inherited artifacts, reconstructs all reciprocal trace roots for the three exact orbits, verifies the residue interval and the primitive versus repetition logarithmic-derivative identity, and rejects twelve adversarial mutations in an independent implementation. Ten unit tests cover the same interfaces. The complete finite audit is reproduced by `bash code/run_c54.sh` from the project directory.

The exact rows have two roles. They ensure that no code path silently equates Mahler height with the physical multiplier, and they prove the scalar-roof obstruction. They do not establish a Hölder potential or estimate $\sigma_{\rm Gal}$.

For Route A, the normalized physical suspension already has an analytic dynamical zeta, while the full Galois-weighted amplitude has no known Euler or Fredholm determinant. We therefore report the coordinatewise assessment $$\begin{aligned}
(&\texttt{A1\_WEAK},
\ \texttt{A2\_ANALYTIC\_DETERMINANT}
   \text{ (physical subsystem)},\\
 &\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\ \texttt{A4\_FORMAL\_HINT}),
\end{aligned}$$ with overall status `ROUTE_A_EXPLORATORY`. The word "physical" is part of the A2 scope. For the full Galois-weighted candidate, the dynamical determinant interface remains open and no A2 pass is claimed. Route B is not authorized.

The strongest positive result is the exact pressure pole of the physical Mahler summand. The strongest obstruction is the failure of scalar pressure retuning and the absence of any exact symbolic realization of the Galois excess. The next theorem should either construct a Hölder or controlled asymptotically additive excess observable, or compute the excess abscissa $\sigma_{\rm Gal}$ directly.

Nothing here supplies rational-prime labels, von Mangoldt amplitudes, a functional equation, a completed Riemann divisor, or a self-adjoint operator.

# Exact trace-root and tail details

For a reciprocal quadratic $X^2-tX+1$ with real $|t|>2$, the outside root has modulus $$\frac{|t|+\sqrt{t^2-4}}2,$$ whose logarithm is $\operatorname{arcosh}(|t|/2)$. Applying this identity to the nonphysical trace roots in Table [1](#tab:excess){reference-type="ref" reference="tab:excess"} gives the exact excess formulas used by the checker.

For a single primitive length $L>0$, the finite Euler identity used as a sign and repetition control is $$\frac{L}{e^{sL}-1}
=\sum_{k\ge1}Le^{-skL}
=Le^{-sL}+\sum_{k\ge2}Le^{-skL}.$$ The certificate evaluates this identity independently on all three inherited lengths. In the proof of Theorem 4.2, normal convergence is global rather than orbitwise: the prime orbit theorem controls the sum over primitive lengths, and the positive minimum roof length controls the geometric sum over repetitions.

Finally, the certified pressure interval gives $$\frac{3}{\pi^2(0.277987)}
<\frac3{\pi^2h_*}
<\frac{3}{\pi^2(0.277980)},$$ which is the interval reported in [\[eq:residue-interval\]](#eq:residue-interval){reference-type="eqref" reference="eq:residue-interval"}.
