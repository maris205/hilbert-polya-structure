---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-quantum-kicked-rotor-integer-resonance-route-a"
canonical_tex: "henon_dynamics/henon_quantum_kicked_rotor_integer_resonance_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_quantum_kicked_rotor_integer_resonance_route_a/paper/main.pdf"
source_sha256: "154b79238923cb8f99c7d71944af7b7a450f4f2bd57e2f4b165aeb0e23f1d112"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Integer Quantum Resonance and Antiresonance of the Kicked Rotor: An Exact Parity Sheet

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_quantum_kicked_rotor_integer_resonance_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_quantum_kicked_rotor_integer_resonance_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_quantum_kicked_rotor_integer_resonance_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_quantum_kicked_rotor_integer_resonance_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve the positive-integer resonance sheet of the quantum kicked rotor in a fixed free-after-kick convention. Parity of the integer resonance index gives a complete dichotomy: an exact Bessel propagator with ballistic momentum variance, or a state-independent two-kick antiresonance. \>0 On the resonant face we also derive the full momentum characteristic function, survival probability, and centered moments through order six. \>1 All momentum seeds, zero kick strength, zero elapsed kicks, vector phases, operator ordering, source ownership, and Route-A exclusions are closed explicitly; general rational resonance and detuning remain outside scope.
author:
- 'Route-A source-local certificate HCS-C337'
date: 3 September 2026
title: |
  Integer Quantum Resonance and Antiresonance of the Kicked Rotor:\
  An Exact Parity Sheet
```

## Markdown 正文

trailerid \[\<C3372026090300000000000000000000\>\<C3372026090300000000000000000000\>\]

# Frozen Floquet owner

Let $$\mathcal H=L^2(\mathbb T,d\theta/(2\pi)),\qquad
 |n\rangle(\theta)=e^{\mathrm in\theta},\qquad
 \widehat n=-\mathrm i\partial_\theta.$$ The periodic $H^1$ realization of $\widehat n$ is self-adjoint, and $\widehat n^2$ is self-adjoint on periodic $H^2$. For $\kappa\in\mathbb R$ put $$K_\kappa=e^{-\mathrm i\kappa\cos\theta},\qquad
 U_\tau=e^{-\mathrm i\tau\widehat n^2/2}K_\kappa.$$ Here $K_\kappa$ denotes unit-modulus multiplication. Spectral calculus and bounded multiplication make both factors, hence $U_\tau$, unitary. The ordering is part of the definition: one kick followed by free rotation.

We restrict to $$\label{eq:sheet}
 \tau=2\pi\ell,\qquad \ell\in\mathbb Z_{>0}.$$ No assertion below concerns another rational sheet or a detuned value.

[\[lem:parity\]]{#lem:parity label="lem:parity"} At [\[eq:sheet\]](#eq:sheet){reference-type="eqref" reference="eq:sheet"}, the free factor is $I$ for even $\ell$ and the half-turn $$(Rf)(\theta)=f(\theta+\pi)$$ for odd $\ell$.

On $|n\rangle$ the free eigenvalue is $e^{-\mathrm i\pi\ell n^2}$. Since $n^2-n=n(n-1)$ is even, this equals $e^{-\mathrm i\pi\ell n}$. It is one for even $\ell$ and $(-1)^n$ for odd $\ell$. The latter is precisely the Fourier action of $R$.

[\[thm:main\]]{#thm:main label="thm:main"} Fix $m\in\mathbb Z$ and $t\in\mathbb Z_{\geq0}$.

1.  If $\ell$ is even, then $$\label{eq:kernel}
     \langle n|U_{2\pi\ell}^{t}|m\rangle
     =(-\mathrm i)^{n-m}J_{n-m}(\kappa t).$$ Consequently the momentum law is $J_{n-m}(\kappa t)^2$, its mean is $m$, and $$\label{eq:ballistic}
     \operatorname{Var}(n)=\frac{\kappa^2t^2}{2},\qquad
     \mathbb E_m[\widehat n^2/2]_t
     =\frac{m^2}{2}+\frac{\kappa^2t^2}{4}.$$

2.  If $\ell$ is odd, then $U_{2\pi\ell}=RK_\kappa$ and $$\label{eq:involution}
     U_{2\pi\ell}^{2}=I.$$ At even $t$ the amplitude is $\delta_{nm}$, while at odd $t$ it is $$\label{eq:odd-kernel}
     (-1)^n(-\mathrm i)^{n-m}J_{n-m}(\kappa).$$

For even $\ell$, Lemma [\[lem:parity\]](#lem:parity){reference-type="ref" reference="lem:parity"} gives $U=K_\kappa$ and $U^t=K_{t\kappa}$. The Jacobi--Anger expansion $$e^{-\mathrm ix\cos\theta}
 =\sum_{q\in\mathbb Z}(-\mathrm i)^qJ_q(x)e^{\mathrm iq\theta}$$ with $q=n-m$ proves [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}. The moment statements follow from Fourier orthogonality: $$\sum_q J_q(x)^2e^{\mathrm iqu}=J_0\!(2x\sin(u/2)).$$ Two derivatives at $u=0$ give mean displacement zero and variance $x^2/2$; translation by $m$ gives [\[eq:ballistic\]](#eq:ballistic){reference-type="eqref" reference="eq:ballistic"}.

For odd $\ell$, the free factor is $R$. Since the half-turn reverses the cosine, $$RK_\kappa R=K_{-\kappa}=K_\kappa^{-1}.$$ Thus $(RK_\kappa)^2=I$. Even powers are $I$, and odd powers are $RK_\kappa$. Applying $R$ after the Jacobi--Anger expansion multiplies the $n$th Fourier coefficient by $(-1)^n$, which proves [\[eq:odd-kernel\]](#eq:odd-kernel){reference-type="eqref" reference="eq:odd-kernel"}.

The phrase *operator parity owner* records the first paper round: the all-time dichotomy is an operator theorem, not a finite-lattice simulation.

\>0

# Exact momentum statistics

Let $x=\kappa t$ on the even sheet and set $q=n-m$. If $c_q=(-\mathrm i)^qJ_q(x)$, Fourier orthogonality gives $$\begin{aligned}
 \Phi_x(u)
 &=\sum_{q\in\mathbb Z}|c_q|^2e^{\mathrm iqu}\label{eq:char}\\
 &=\frac1{2\pi}\int_0^{2\pi}
 e^{-\mathrm ix\cos(\theta+u)}e^{\mathrm ix\cos\theta}\,d\theta
 =J_0\!(2x\sin(u/2)).\nonumber\end{aligned}$$ The last equality follows by shifting the integration variable in the standard integral representation of $J_0$; its sign is immaterial because $J_0$ is even. At $u=0$, [\[eq:char\]](#eq:char){reference-type="eqref" reference="eq:char"} also proves normalization.

[\[thm:moments\]]{#thm:moments label="thm:moments"} For even $\ell$, the survival probability is $$\Pr_m\{n_t=m\}=J_0(\kappa t)^2,$$ and the centered odd moments through order six vanish. The nonzero centered moments are $$\begin{aligned}
 \mu_2&=\frac{x^2}{2},\label{eq:moments}\\
 \mu_4&=\frac{x^2}{2}+\frac{3x^4}{8},\nonumber\\
 \mu_6&=\frac{x^2}{2}+\frac{15x^4}{8}+\frac{5x^6}{16}.\nonumber\end{aligned}$$ For odd $\ell$, the law is the point mass at $m$ at even times and the one-kick Bessel law $J_{n-m}(\kappa)^2$ at odd times; use $x=0$ and $x=\kappa$, respectively, in [\[eq:moments\]](#eq:moments){reference-type="eqref" reference="eq:moments"}.

The survival formula is [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} at $n=m$. For a characteristic function, $\mathbb E(q^r)=\Phi_x^{(r)}(0)/\mathrm i^r$. Six direct differentiations of the final expression in [\[eq:char\]](#eq:char){reference-type="eqref" reference="eq:char"} give [\[eq:moments\]](#eq:moments){reference-type="eqref" reference="eq:moments"}; evenness in $u$ annihilates the odd derivatives. The odd-sheet statement follows from Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

The phrase *Bessel characteristic owner* marks the substantive first revision. It upgrades a variance statement to an exact distributional identity and moments through sixth order.

\>1

# Boundary atlas and convention audit

At $t=0$, $J_q(0)=\delta_{q0}$ closes both parity formulas. At $\kappa=0$, the even sheet has $U=I$, while the odd sheet has $U=R$. Hence every momentum probability is stationary. On the odd sheet a vector $|m\rangle$ acquires $(-1)^m$ after one kick, although its ray is fixed; this distinguishes vector equality from measurement equality. For nonzero $\kappa$, the even-sheet variance in [\[eq:ballistic\]](#eq:ballistic){reference-type="eqref" reference="eq:ballistic"} is exactly quadratic at every integer time. Negative and zero momentum seeds need no separate argument, because every formula is translation-covariant in $m$.

Equation [\[eq:involution\]](#eq:involution){reference-type="eqref" reference="eq:involution"} is an operator identity on all of $\mathcal H$. It does not say that every vector has least period two: eigenvectors of the involution may return projectively after one step. Conversely, we do not replace $e^{-\mathrm i\tau\widehat n^2/2}K_\kappa$ by the reversed product. Such a convention can be related by a strobe change, but its raw amplitudes are not silently asserted here.

# Evidence and collision audit

The certificate contains 396 exact parity rows, 435 Gaussian-rational formal Fourier coefficients, 882 exact moment rows, 120 operator-word rows, and seven 90-digit Bessel spot checks. It audits 22,444 scalar leaves. A producer-independent checker performs 47,531 assertions; an independent SymPy lane proves 13,188 identities; two isolated generations are byte identical; and 133 repaired-hash, parser, theorem, boundary, and evaluator attacks are rejected. High-precision Bessel sums are labeled `NUMERICAL_OBSERVATION`; the infinite identities follow from the Fourier proof, not from truncation.

The closest workspace owners are C110 (classical nonautonomous Hénon Floquet dynamics), C143 (coined quantum walk), C148 (open Walsh quantum baker), C178 (harmonic metaplectic strobe), C224 (two-level Landau--Zener scattering), C318 (static SSH lattice), and C323 (finite continuous-time quantum search). None owns the cosine-kicked rotor's infinite momentum lattice and its exact integer parity sheet. This is a workspace collision statement, never a claim of literature priority.

# Source boundary and Route-A decision

Dana, Eisenberg and Shnerb identify quantum antiresonance with exact periodic recurrence [@Dana1996]. Dana and Dorofeev study general kicked-particle resonances and exact transport quantities [@DanaDorofeev2006]; Ryu et al. experimentally report rational-Talbot-time resonance and ballistic momentum transfer [@Ryu2006]. These primary records establish provenance and physical context. The displayed theorem is independently derived here, and no priority claim is made for its ingredients or assembly.

The phrase *parity boundary and route firewall* marks the final revision. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ The Floquet unitary is a natural source quantization with the physical kick clock, but its recurrences are not an isolated arithmetic primitive-orbit ledger. There is no prime-power clock, orbit Euler product, target Fredholm determinant, target divisor, functional equation, Weil compression, target-zero match, or Hilbert--Polya operator. Route A is rejected and Route B remains locked. No target arithmetic local data, Euler factor, root number, or automorphy object is asserted.

#### AI use.

A generative language model assisted proof organization, code scaffolding, and manuscript drafting. The analytic derivation, producer-independent checker, symbolic lane, hostile tests, and deterministic artifacts define the audit record.

9 I. Dana, E. Eisenberg, and N. Shnerb, "Antiresonance and localization in quantum dynamics," *Physical Review E* 54 (1996), 5948--5963. DOI: [10.1103/PhysRevE.54.5948](https://doi.org/10.1103/PhysRevE.54.5948).

I. Dana and D. L. Dorofeev, "General Quantum Resonances of the Kicked Particle," *Physical Review E* 73 (2006), 026206. DOI: [10.1103/PhysRevE.73.026206](https://doi.org/10.1103/PhysRevE.73.026206); [arXiv:nlin/0509035](https://arxiv.org/abs/nlin/0509035).

C. Ryu, M. F. Andersen, A. Vaziri, M. B. d'Arcy, J. M. Grossman, K. Helmerson, and W. D. Phillips, "High-Order Quantum Resonances Observed in a Periodically Kicked Bose--Einstein Condensate," *Physical Review Letters* 96 (2006), 160403. DOI: [10.1103/PhysRevLett.96.160403](https://doi.org/10.1103/PhysRevLett.96.160403).
