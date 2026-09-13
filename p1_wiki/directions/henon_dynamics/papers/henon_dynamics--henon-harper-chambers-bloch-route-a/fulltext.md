---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-harper-chambers-bloch-route-a"
canonical_tex: "henon_dynamics/henon_harper_chambers_bloch_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_harper_chambers_bloch_route_a/paper/main.pdf"
source_sha256: "0e11d5b07bb987ce386dd559678f42a2f7ba1c070938052407e95436f03d08d6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rational-Flux Anisotropic Harper Dynamics: Chambers Phase Collapse and the Algebraic Bloch-Band Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_harper_chambers_bloch_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_harper_chambers_bloch_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_harper_chambers_bloch_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_harper_chambers_bloch_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every reduced rational magnetic flux and every positive hopping anisotropy, we fix one magnetic-cell phase convention and derive the exact Chambers characteristic identity. The proof exposes why the vertical transfer trace has only three Laurent modes and fixes both phase signs. \>0 We then recover the full two-dimensional spectrum as a polynomial preimage, give the exact algebraic band-contact criterion, prove Aubry duality, flux reversal and parity, and isolate the forced central contact at every even denominator. The one- and two-site cells are computed separately. \>1 An exact cyclotomic lane and 74,880 independently reconstructed Bloch fibers audit the result. Harper--Chambers theory is established background, and the final Route-A verdict remains negative despite natural quantization.
author:
- 'HCS-C371 / HEN-O355'
date: 4 September 2026
title: 'Rational-Flux Anisotropic Harper Dynamics: Chambers Phase Collapse and the Algebraic Bloch-Band Atlas'
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<C3712026090400000000000000000000\>\<C3712026090400000000000000000000\>\]

# Magnetic owner and phase convention

Let $(p,q)=1$, $q\ge3$, and $\lambda>0$. On $\ell^2(\mathbb Z^2)$ consider the bounded self-adjoint operator $$\begin{aligned}
 (\mathsf H_{p/q,\lambda}\Psi)_{m,n}
 ={}&\Psi_{m+1,n}+\Psi_{m-1,n}\notag\\
 &+\lambda e^{2\pi i pm/q}\Psi_{m,n+1}
 +\lambda e^{-2\pi i pm/q}\Psi_{m,n-1}.
 \label{eq:lattice}\end{aligned}$$ Fourier transformation in the second coordinate and magnetic Bloch reduction give the $q$-dimensional fiber $$(\mathsf H(k_x,k_y)u)_m=u_{m+1}+u_{m-1}
 +2\lambda\cos\!\left(k_y+\frac{2\pi pm}{q}\right)u_m,
 \qquad u_{m+q}=e^{iqk_x}u_m .
 \label{eq:fiber}$$ Thus $X=qk_x$ is the *total* horizontal boundary phase. This distinction is essential: throughout, $$D_{p/q,\lambda}(E;k_x,k_y)
 :=\det\!\left(EI_q-\mathsf H_{p/q,\lambda}(k_x,k_y)\right).
 \label{eq:D}$$ This manuscript's first revision is the **Chambers phase-collapse owner**.

# The Chambers polynomial

Put $\zeta=e^{2\pi i/q}$, $y=e^{ik_y}$, and $$A_m(E,y)=
 \begin{pmatrix}
 E-\lambda(y\zeta^{pm}+y^{-1}\zeta^{-pm})&-1\\
 1&0
 \end{pmatrix},
 \qquad M_q=A_{q-1}\cdots A_0 .
 \label{eq:transfer}$$

[\[thm:chambers\]]{#thm:chambers label="thm:chambers"} There is a unique real monic polynomial $\mathcal P_{p/q,\lambda}$ of degree $q$ such that $$D_{p/q,\lambda}(E;k_x,k_y)
 =\mathcal P_{p/q,\lambda}(E)-2\cos(qk_x)
 -2\lambda^q\cos(qk_y)
 \label{eq:chambers}$$ for every real $E,k_x,k_y$.

Since $\det A_m=1$, the Floquet multipliers of $M_q$ are $e^{\pm iqk_x}$. Both sides below are monic of degree $q$ and have the same roots, hence $$D_{p/q,\lambda}=\operatorname{tr}M_q-2\cos(qk_x).
 \label{eq:traceD}$$ Replacing $y$ by $\zeta^p y$ cyclically permutes the potential sequence in [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"}. The monodromy changes by cyclic conjugacy, so its trace is invariant. Because $p$ is invertible modulo $q$, a Laurent polynomial of $y$ with degrees between $-q$ and $q$ and this invariance can use only the modes $-q,0,q$.

The coefficient of $y^q$ has one contribution: select $-\lambda y\zeta^{pm}$ in every upper-left entry. It equals $$(-\lambda)^q\zeta^{p q(q-1)/2}=-\lambda^q .
 \label{eq:extreme}$$ Indeed, odd $q$ makes $q-1$ even, while even $q$ forces $p$ odd. Complex conjugation gives the same coefficient for $y^{-q}$. The remaining mode is independent of both phases, real, and monic; call it $\mathcal P_{p/q,\lambda}(E)$. Equations [\[eq:traceD\]](#eq:traceD){reference-type="eqref" reference="eq:traceD"} and [\[eq:extreme\]](#eq:extreme){reference-type="eqref" reference="eq:extreme"} prove [\[eq:chambers\]](#eq:chambers){reference-type="eqref" reference="eq:chambers"}. Monicity gives uniqueness.

The theorem is convention-complete: using the boundary character $X$ in place of $k_x$ rewrites the horizontal term as $-2\cos X$, not $-2\cos(qX)$. This is precisely the convention tested by the executable fibers.

\>0

# Spectrum and algebraic band contacts

This revision is the **spectrum, duality, and edge owner**. Write $$\mathcal C_{q,\lambda}=2(1+\lambda^q),\qquad
 B_{p/q,\lambda}(E)=\mathcal P_{p/q,\lambda}(E)^2-\mathcal C_{q,\lambda}^2.
 \label{eq:edgepoly}$$

[\[lem:central\]]{#lem:central label="lem:central"} If $q$ is even, then $$\mathcal P_{p/q,\lambda}(0)=2(-1)^{q/2}(1+\lambda^q).
 \label{eq:centralvalue}$$

Lamoureux and Mingo use $h_{\theta,L}=u+u^{-1}+(L/2)(v+v^{-1})$. Their Theorem 2.5 proves the vanishing of every intermediate cyclic-matching sum, and their Corollary 2.6 gives, for even $q$, $$\Delta_{p/q,L}(0)=2(-1)^{q/2}\bigl(1+(L/2)^q\bigr)
 \quad\cite{LamoureuxMingo}.$$ Our diagonal potential is $2\lambda\cos(\cdot)$, so their parameter is $L=2\lambda$. Comparing the phase-independent monic term in their Chambers formula with Theorem [\[thm:chambers\]](#thm:chambers){reference-type="ref" reference="thm:chambers"} identifies $\Delta_{p/q,2\lambda}=\mathcal P_{p/q,\lambda}$: their defining vertical phase $\pi/(2q)$ kills the explicit $q$th cosine, while our transfer trace then equals $\mathcal P$. This also fixes our $\det(EI-\mathsf H)$ convention. Substitution gives [\[eq:centralvalue\]](#eq:centralvalue){reference-type="eqref" reference="eq:centralvalue"}. Thus this all-$q$ step is sourced rather than inferred from the finite cyclotomic audit.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} The full two-dimensional spectrum of [\[eq:lattice\]](#eq:lattice){reference-type="eqref" reference="eq:lattice"} is $$\operatorname{Spec}(\mathsf H_{p/q,\lambda})
 =\{E\in\mathbb R:|\mathcal P_{p/q,\lambda}(E)|\le\mathcal C_{q,\lambda}\}.
 \label{eq:preimage}$$ The two edge factors are actual fiber characteristic polynomials: $$\mathcal P(E)-\mathcal C_{q,\lambda}=D(E;0,0),\qquad
 \mathcal P(E)+\mathcal C_{q,\lambda}=D(E;\pi/q,\pi/q).
 \label{eq:edgefibers}$$ Consequently the algebraic band-edge multiset is the real zero multiset of $B$. An edge label is multiple precisely when $$\mathcal P(E)=\pm\mathcal C_{q,\lambda},\qquad \mathcal P'(E)=0.
 \label{eq:contact}$$ Moreover, $$\begin{aligned}
 \mathcal P_{p/q,\lambda}(E)
 &=\lambda^q\mathcal P_{p/q,1/\lambda}(E/\lambda),
 \label{eq:duality}\\
 \mathcal P_{p/q,\lambda}(E)&=\mathcal P_{(q-p)/q,\lambda}(E),
 \label{eq:reversal}\\
 \mathcal P_{p/q,\lambda}(-E)&=(-1)^q\mathcal P_{p/q,\lambda}(E).
 \label{eq:parity}\end{aligned}$$ If $q$ is even, then $$\mathcal P_{p/q,\lambda}(0)=2(-1)^{q/2}(1+\lambda^q),
 \qquad \mathcal P'_{p/q,\lambda}(0)=0,
 \label{eq:central}$$ so zero is a multiple central edge.

Magnetic Bloch theory is a direct-integral decomposition into [\[eq:fiber\]](#eq:fiber){reference-type="eqref" reference="eq:fiber"}. By [\[eq:chambers\]](#eq:chambers){reference-type="eqref" reference="eq:chambers"}, $E$ lies in some fiber spectrum exactly when $$\mathcal P(E)=2\cos(qk_x)+2\lambda^q\cos(qk_y).$$ The phases vary independently, and their sum fills $[-\mathcal C_{q,\lambda},\mathcal C_{q,\lambda}]$, proving [\[eq:preimage\]](#eq:preimage){reference-type="eqref" reference="eq:preimage"}. Putting $(k_x,k_y)=(0,0)$ and $(\pi/q,\pi/q)$ in [\[eq:chambers\]](#eq:chambers){reference-type="eqref" reference="eq:chambers"} proves [\[eq:edgefibers\]](#eq:edgefibers){reference-type="eqref" reference="eq:edgefibers"}. Both endpoint fibers are real symmetric: their total horizontal boundary phases are $0$ and $\pi$, and their diagonal potentials are real. Thus both edge factors have only real roots, with multiplicity, and $B=(\mathcal P-\mathcal C)(\mathcal P+\mathcal C)$ is real-rooted. Equation [\[eq:contact\]](#eq:contact){reference-type="eqref" reference="eq:contact"} follows from $B'=2\mathcal P\mathcal P'$ and $\mathcal P\ne0$ at an edge. It is an algebraic coalescence criterion, not a claim that every remaining gap is open.

Exchange of the two lattice axes reverses the magnetic orientation and swaps the hopping amplitudes. After division by $\lambda$, magnetic Fourier duality identifies the result with $\lambda\mathsf H_{(q-p)/q,1/\lambda}$. Complex conjugation identifies the fluxes $p/q$ and $(q-p)/q$. Comparing the phase-independent monic terms in [\[eq:chambers\]](#eq:chambers){reference-type="eqref" reference="eq:chambers"} proves [\[eq:duality\]](#eq:duality){reference-type="eqref" reference="eq:duality"}--[\[eq:reversal\]](#eq:reversal){reference-type="eqref" reference="eq:reversal"}.

The bipartite involution $\Gamma\Psi_{m,n}=(-1)^{m+n}\Psi_{m,n}$ conjugates $\mathsf H$ to $-\mathsf H$ and shifts both quasimomenta by $\pi$. Substitution in [\[eq:chambers\]](#eq:chambers){reference-type="eqref" reference="eq:chambers"} proves [\[eq:parity\]](#eq:parity){reference-type="eqref" reference="eq:parity"}. For even $q$, Lemma [\[lem:central\]](#lem:central){reference-type="ref" reference="lem:central"} gives the first formula in [\[eq:central\]](#eq:central){reference-type="eqref" reference="eq:central"}. Equation [\[eq:parity\]](#eq:parity){reference-type="eqref" reference="eq:parity"} makes $\mathcal P$ even, so $\mathcal P'(0)=0$. This proves the derivative formula without extrapolating the finite exact lane.

[\[prop:small\]]{#prop:small label="prop:small"} When coincident wrap neighbors are added rather than overwritten, Theorem [\[thm:chambers\]](#thm:chambers){reference-type="ref" reference="thm:chambers"} has the direct boundary polynomials $$q=1,\ p=0:\quad \mathcal P(E)=E,
 \qquad
 q=2,\ p=1:\quad \mathcal P(E)=E^2-2(1+\lambda^2).
 \label{eq:small}$$ The two $q=2$ folded bands meet at zero. As $\lambda\downarrow0$, the spectrum tends to the decoupled horizontal-chain interval $[-2,2]$; reciprocal duality is not evaluated at $\lambda=0$.

For $q=1$ the scalar fiber is $2\cos k_x+2\lambda\cos k_y$. For $q=2$, write $X=e^{2ik_x}$ and $Y=e^{ik_y}$. The off-diagonal entries are $1+X^{-1}$ and $1+X$, while the diagonal entries are $\pm\lambda(Y+Y^{-1})$. Its determinant is $$E^2-2(1+\lambda^2)-(X+X^{-1})
 -\lambda^2(Y^2+Y^{-2}),$$ which proves [\[eq:small\]](#eq:small){reference-type="eqref" reference="eq:small"} and the asserted contact.

\>1

# Independent evidence

This revision is the **evidence, collision, and route owner**. The evidence exhausts all reduced fractions with $3\le q\le16$ and the five anisotropies $1/2,2/3,1,3/2,2$.

::: {#tab:evidence}
  receipt                                                          count
  ------------------------------------------- --------------------------
  reduced fluxes / parameter panels                         $78$ / $390$
  Bloch total-phase grid per panel                          $12\times16$
  Hermitian fibers / eigenvalues                $74{,}880$ / $825{,}600$
  characteristic-determinant probes                          $224{,}640$
  exact cyclotomic reduced fluxes, $q\le10$                         $30$

  : Finite regression scale. Sampling is not the proof.
:::

The producer obtains $\mathcal P$ from transfer-polynomial multiplication. The checker never imports it: it reconstructs $\mathcal P$ from the characteristic polynomial of one Hermitian reference fiber and then rebuilds every matrix in Table [1](#tab:evidence){reference-type="ref" reference="tab:evidence"}. A third lane works exactly in $\mathbb Q[\zeta_q]/(\Phi_q)$ with a symbolic anisotropy degree; it checks the Laurent support, both extreme coefficients, duality, reversal, parity, and [\[eq:central\]](#eq:central){reference-type="eqref" reference="eq:central"} through $q=10$. It is a regression check, not the all-denominator proof supplied by Lemma [\[lem:central\]](#lem:central){reference-type="ref" reference="lem:central"}. Isolated replay, repaired-hash mutations and strict JSON/YAML parsers close the computational boundary.

# Source and collision audit

Harper's magnetic difference equation, Chambers' rational-flux relation, and Hofstadter's magnetic bands are classical [@Harper; @Chambers; @Hofstadter; @Avron; @JKK]. Lamoureux and Mingo directly precede the cyclic-matching cancellation and even-denominator constant-term formula used in Lemma [\[lem:central\]](#lem:central){reference-type="ref" reference="lem:central"} [@LamoureuxMingo]. We claim no priority for these objects or formulas. The package contribution is a convention-locked reconstruction, the explicit real endpoint-fiber edge factorization [\[eq:edgefibers\]](#eq:edgefibers){reference-type="eqref" reference="eq:edgefibers"}, and an independently replayable atlas.

The direct workspace neighbor is HCS-C15/HEN-O30. It owns a critical Weyl--Harper block $U+U^*+V+V^*$ at flux $1/3^m$ and the return of its top spectral edge along a Heisenberg congruence tower. It does not own the two-phase identity [\[eq:chambers\]](#eq:chambers){reference-type="eqref" reference="eq:chambers"}, all reduced fluxes, anisotropic duality, or the edge polynomial [\[eq:edgepoly\]](#eq:edgepoly){reference-type="eqref" reference="eq:edgepoly"}. C293 is a magnetic Grushin cylinder, C340 is a Lamé Floquet operator, and C356 is a QWZ Chern pump. No Chern, transport, edge-state, irrational-flux Cantor-spectrum, or Ten-Martini result is imported here.

# Route decision and nonclaims

Reduced rational flux gives exact cyclotomic magnetic translations, earning $A0_{\rm WEAK\_ARITHMETIC\_RELATION}$. It does not give rational-prime ownership, prime-power repetition, an isolated primitive-orbit ledger, or a logarithmic prime clock, so $A1_{\rm FAIL}$. The finite source characteristic polynomial is neither a target Euler product nor a target Fredholm determinant, so $A2_{\rm FAIL}$; no target continuation, functional equation, divisor or zero-counting law exists, so $A3_{\rm FAIL}$. Equation [\[eq:lattice\]](#eq:lattice){reference-type="eqref" reference="eq:lattice"} is already a bounded self-adjoint Hamiltonian, hence $A4_{\rm NATURAL\_QUANTIZATION}$, but its Bloch bands are not target zeros or a Hilbert--Pólya realization.

The overall verdict is `ROUTE_A_REJECTED` under the literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`. No target arithmetic local datum, Euler factor, root number, automorphy, target-zero match, or Hilbert--Pólya operator is asserted. Route B remains locked.

9 P. G. Harper, *Single band motion of conduction electrons in a uniform magnetic field*, Proc. Phys. Soc. A 68 (1955), 874--878. W. G. Chambers, *Linear-network model for magnetic breakdown in two dimensions*, Phys. Rev. 140 (1965), A135--A143. D. R. Hofstadter, *Energy levels and wave functions of Bloch electrons in rational and irrational magnetic fields*, Phys. Rev. B 14 (1976), 2239--2249. J. Avron, P. H. M. van Mouche, and B. Simon, *On the measure of the spectrum for the almost Mathieu operator*, Comm. Math. Phys. 132 (1990), 103--118. M. P. Lamoureux and J. A. Mingo, *On the characteristic polynomial of the almost Mathieu operator*, Proc. Amer. Math. Soc. 135 (2007), 3205--3215. <https://doi.org/10.1090/S0002-9939-07-08830-2>. S. Jitomirskaya, L. Konstantinov, and I. Krasovsky, *On the spectrum of critical almost Mathieu operators in the rational case*, arXiv:2007.01005.
