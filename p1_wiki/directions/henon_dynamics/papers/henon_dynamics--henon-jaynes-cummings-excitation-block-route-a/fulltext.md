---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-jaynes-cummings-excitation-block-route-a"
canonical_tex: "henon_dynamics/henon_jaynes_cummings_excitation_block_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_jaynes_cummings_excitation_block_route_a/paper/main.pdf"
source_sha256: "b5eb94748e5d1fdcf6dc0c673049e36353cf638b4d4234352c42bc49c35d3750"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Excitation Blocks, Propagators, and Revivals in the Jaynes--Cummings Model

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_jaynes_cummings_excitation_block_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_jaynes_cummings_excitation_block_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_jaynes_cummings_excitation_block_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_jaynes_cummings_excitation_block_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a convention-complete spectral and dynamical atlas for the single-mode rotating-wave Jaynes--Cummings Hamiltonian. Total excitation decomposes the atom--Fock space into a separate vacuum and exact two-dimensional blocks. We derive every dressed pair, the full block propagator, transition probability, trace and determinant. For a finite active set, universal bare-population revival is equivalent to rational commensurability of its positive Rabi frequencies; full state-vector revival requires additional center and vacuum phase alignment. Resonance, zero coupling, block indexing, coupling-sign gauge, finite cutoffs and the noncompact full-Fock unitary are kept explicit. Independent exact/high-precision, symbolic, replay and hostile-mutation audits accompany the theorem.
author:
- HCS Research Program
date: 28 August 2026(revision 2)
title: 'Exact Excitation Blocks, Propagators, and Revivals in the Jaynes--Cummings Model'
```

## Markdown 正文

suppressoptionalinfo 611

# Hamiltonian and excitation convention

Set $\hbar=1$ and $$H=\omega_c a^\dagger a+\frac{\omega_q}{2}\sigma_z
   +g(a^\dagger\sigma_-+a\sigma_+),\qquad
 N=a^\dagger a+\sigma_+\sigma_- .                       \tag{1}$$ We use $\sigma_z|e\rangle=|e\rangle$ and $\sigma_z|g\rangle=-|g\rangle$. For $n\ge1$, excitation block $n$ has the ordered basis $\{|e,n-1\rangle,|g,n\rangle\}$; this shift is part of the frozen convention.

[\[thm:block\]]{#thm:block label="thm:block"} The operators in (1) satisfy $[H,N]=0$. The vacuum $|g,0\rangle$ is an eigenstate with energy $-\omega_q/2$. On block $n\ge1$, $$H_n=c_nI+\frac{\Delta}{2}\sigma_z+g\sqrt n\,\sigma_x,
 \quad c_n=(n-\tfrac12)\omega_c,
 \quad \Delta=\omega_q-\omega_c .                       \tag{2}$$ Let $\Omega_n=(\Delta^2+4g^2n)^{1/2}$. The dressed energies are $$E_{n,\pm}=c_n\pm\frac{\Omega_n}{2},                    \tag{3}$$ and the exact propagator is $$U_n(t)=e^{-ic_nt}\left[
 \cos\frac{\Omega_nt}{2}I
 -i\frac{\sin(\Omega_nt/2)}{\Omega_n}
 (\Delta\sigma_z+2g\sqrt n\,\sigma_x)\right],           \tag{4}$$ with its continuous identity limit when $\Omega_n=0$. In particular, $$P_{|e,n-1\rangle\to|g,n\rangle}(t)
 =\frac{4g^2n}{\Omega_n^2}\sin^2\frac{\Omega_nt}{2},    \tag{5}$$ where the simultaneous $g=\Delta=0$ value is zero. Every $U_n$ is unitary, and $$\operatorname{tr}U_n=2e^{-ic_nt}\cos(\Omega_nt/2),
 \qquad \det U_n=e^{-2ic_nt}.                            \tag{6}$$

Each interaction monomial creates one photon while destroying one atomic excitation, or reverses that operation, proving $[H,N]=0$. Applying $H$ to the ordered bare basis yields (2). If $B_n=H_n-c_nI$, then $B_n^2=(\Omega_n^2/4)I$. The characteristic polynomial gives (3), while the even and odd parts of $e^{-itB_n}$ give (4), including the continuous zero-frequency limit. Its off-diagonal modulus gives (5). The Pauli-square identity gives unitarity; its two eigenphases give (6).

\>0

# Finite-support revival theorem

Call a block active and coupled when the initial support includes it and $g\sqrt n\ne0$.

[\[prop:rev\]]{#prop:rev label="prop:rev"} For a finite set $S$ of active coupled blocks, there is a time $T>0$ that restores every bare population for every bare initial state in those blocks if and only if $$\Omega_nT\in2\pi\mathbb Z\qquad(n\in S).               \tag{7}$$ Equivalently, the positive frequencies $\{\Omega_n:n\in S\}$ are rationally commensurate. If $\Omega_nT=2\pi k_n$, then $U_n(T)=e^{-ic_nT}(-1)^{k_n}I$. A common state-vector revival therefore also requires these phases, together with any occupied vacuum phase $e^{i\omega_qT/2}$, to agree up to one global phase.

For a coupled block the coefficient in (5) is positive, so universal bare- population restoration is equivalent to $\sin(\Omega_nT/2)=0$. This is (7). A finite positive frequency set admits a common such $T$ exactly when all frequency ratios are rational. Substitution in (4) gives the parity and center phase, proving the stronger-state clause.

# Singular and operator boundaries

When $g=0$, the bare states decouple; the case $g=\Delta=0$ uses the continuous limit in (4), not a $0/0$ expression. At resonance, $\Omega_n=2|g|\sqrt n$ and the exchange amplitude in (5) is one. The vacuum is one-dimensional and is never inserted into an $n\ge1$ square-root formula. Conjugation by a diagonal atomic phase maps $g$ to $-g$, so energies and probabilities agree although the signed off-diagonal amplitude changes.

A finite Fock compression retains every excitation block below its dangling top state. On the full infinite-dimensional space, a unitary maps an orthonormal sequence to another orthonormal sequence; it is therefore not compact, and its infinitely many singular values equal one. Thus it is not Schatten or trace class, and no ordinary full-space trace or Fredholm determinant is asserted.

\>1

# Independent audit and Route-A boundary

The canonical ledger contains four parameter cases, 32 blocks and 64 propagators, including resonance, two detuning signs, negative coupling and the degenerate uncoupled face. A producer-independent checker makes 1,100 assertions and directly builds a ten-dimensional truncated Fock Hamiltonian, verifying its excitation commutator and blocks. SymPy reconstructs 13 generic identities; byte replay is exact. Twenty-four repaired-hash semantic/schema mutations and one stale-hash mutation are rejected. These finite rows are regression controls, not the proof of the infinite block family.

The strict Route-A tuple is

(A0\_FAIL, A1\_FAIL, A2\_FAIL, A3\_FAIL, A4\_NATURAL\_QUANTIZATION),

with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. Natural quantization refers only to the source Hamiltonian. Excitation labels are not rational-prime owners, the block oscillations supply no target orbit clock, and no target divisor, analytic target or Hilbert--Polya bridge is constructed.

# Source note {#source-note .unnumbered}

Jaynes and Cummings [@jc1963] introduced the rotating-wave atom--mode owner. Shore and Knight [@sk1993] review its dressed dynamics and collapse/revival context. We claim no priority for those classical results; coherent-field asymptotic collapse and revival are outside the theorem.

9 E. T. Jaynes and F. W. Cummings, *Comparison of quantum and semiclassical radiation theories with application to the beam maser*, *Proceedings of the IEEE* 51 (1963), 89--109. DOI: 10.1109/PROC.1963.1664. B. W. Shore and P. L. Knight, *The Jaynes--Cummings model*, *Journal of Modern Optics* 40 (1993), 1195--1238. DOI: 10.1080/09500349314551321.

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, target-zero or Hilbert--Polya claim. **Data and code.** The theorem, ledger and independent audits are released with HCS-C223. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked the displayed claims and metadata. This is not external peer review.
