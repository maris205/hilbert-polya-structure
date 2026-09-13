---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-complete-graph-quantum-search-detuning-route-a"
canonical_tex: "henon_dynamics/henon_complete_graph_quantum_search_detuning_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_complete_graph_quantum_search_detuning_route_a/paper/main.pdf"
source_sha256: "887ebafec473872d95f13b3965d7bc49a0e230b0c271d86541d9e4ff2e5279e9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Resonance and Detuning Geometry in Complete-Graph Quantum Search

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_complete_graph_quantum_search_detuning_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_complete_graph_quantum_search_detuning_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_complete_graph_quantum_search_detuning_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_complete_graph_quantum_search_detuning_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For continuous-time search with $M$ marked vertices among $N$, we retain the entire Hilbert space rather than only the initialized two-level reduction. A bright--dark decomposition gives every eigenvalue and multiplicity and an exact success law for arbitrary nonnegative driver strength. In the nontrivial marked-fraction regime, perfect search occurs if and only if the driver and oracle are resonant. \>0 The off-resonance defect yields a critical detuning window, while a scalar shift closes the conversion to complete-graph adjacency. All missing-sector faces are resolved directly. \>1 Exact, high-precision, replay, and hostile evidence audit the convention boundary. The Hamiltonian is a natural quantization, but it carries no target arithmetic data and Route A is rejected.
author:
- 'Route-A source-local certificate HCS-C323'
date: 3 September 2026
title: 'Exact Resonance and Detuning Geometry in Complete-Graph Quantum Search'
```

## Markdown 正文

trailerid \[\<C3232026090300000000000000000000\>\<C3232026090300000000000000000000\>\]

# Exact success law and full spectrum

Let $\mathcal H=\mathbb C^N$ have its computational basis, let $W$ be a marked set of size $M$, and let $P_W$ project onto its span. Write $$\label{eq:model}
 H_g=-g|s\rangle\langle s|-P_W,\qquad
 |s\rangle=N^{-1/2}\sum_{j=1}^{N}|j\rangle,\qquad g\geq0.$$ The oracle coefficient is one. Success means projection onto the *full* marked subspace, not the probability of one selected marked basis vector.

Assume first that $N\geq2$ and $0<M<N$, and put $a=M/N$. The normalized uniform marked and unmarked vectors obey $$\label{eq:brightstate}
 |s\rangle=\sqrt a|w\rangle+\sqrt{1-a}|r\rangle.$$ Let $D_W$ comprise marked vectors whose coordinates sum to zero, and define $D_R$ analogously on the unmarked coordinates.

[\[thm:main\]]{#thm:main label="thm:main"} The orthogonal decomposition $$\label{eq:decomp}
 \mathcal H=D_W\oplus D_R\oplus\operatorname{span}\{|w\rangle,|r\rangle\}$$ reduces $H_g$. Its dark spectral data are

   sector   eigenvalue   multiplicity
  -------- ------------ --------------
   $D_W$       $-1$         $M-1$
   $D_R$       $0$         $N-M-1$.

On the bright sector the two eigenvalues are $$\label{eq:eigenvalues}
 \lambda_\pm=-\frac{g+1}{2}\pm\frac{\Omega}{2},\qquad
 \Omega^2=(g-1)^2+4ga.$$ Starting from $|s\rangle$, the marked-subspace probability is $$\label{eq:success}
 p_W(t)=a+\frac{4ga(1-a)}{\Omega^2}
 \sin^2\!\left(\frac{\Omega t}{2}\right).$$ For $0<a<1$, perfect success occurs if and only if $g=1$. Its first hitting time at resonance is $$\label{eq:firsthit}
 t_{\rm hit}=\frac{\pi}{2\sqrt a}=\frac{\pi}{2}\sqrt{\frac NM}.$$ For $g>0$, the first peak is at $t_{\rm peak}=\pi/\Omega$, and $$\begin{aligned}
 p_{\max}&=a+\frac{4ga(1-a)}{(g-1)^2+4ga},\label{eq:pmax}\\
 1-p_{\max}&=\frac{(1-a)(g-1)^2}{(g-1)^2+4ga}.\label{eq:defect}\end{aligned}$$ For $g=0$, $p_W(t)=a$ at every time.

Every vector in $D_W$ is orthogonal to $|s\rangle$ and lies in the range of $P_W$, so $H_g=-I$ there. Every vector in $D_R$ is annihilated by both summands in [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"}. The two dimensions and [\[eq:decomp\]](#eq:decomp){reference-type="eqref" reference="eq:decomp"} follow immediately. In the ordered bright basis $(|w\rangle,|r\rangle)$, $$\label{eq:brightmatrix}
 H_B=-\begin{pmatrix}
 1+ga&g\sqrt{a(1-a)}\\
 g\sqrt{a(1-a)}&g(1-a)
 \end{pmatrix}.$$ Its trace is $-(g+1)$ and its determinant is $g(1-a)$. The discriminant is $(g+1)^2-4g(1-a)=\Omega^2$, proving [\[eq:eigenvalues\]](#eq:eigenvalues){reference-type="eqref" reference="eq:eigenvalues"} and completing the full multiplicity ledger.

Set $B=H_B+(g+1)I/2$. Cayley--Hamilton gives $B^2=\Omega^2I/4$, hence $$\label{eq:exp}
 e^{-\mathrm{i}tH_B}=e^{\mathrm{i}t(g+1)/2}
 \left[\cos\!\left(\frac{\Omega t}{2}\right)I
 -\frac{2\mathrm{i}}{\Omega}\sin\!\left(\frac{\Omega t}{2}\right)B\right].$$ Moreover $\langle w|B|s\rangle=-(g+1)\sqrt a/2$. The initial state has no marked dark component, so its full marked probability is the squared bright amplitude. Equation [\[eq:exp\]](#eq:exp){reference-type="eqref" reference="eq:exp"} therefore gives $$a\cos^2(\Omega t/2)+\frac{a(g+1)^2}{\Omega^2}
 \sin^2(\Omega t/2),$$ which equals [\[eq:success\]](#eq:success){reference-type="eqref" reference="eq:success"} because $(g+1)^2-\Omega^2=4g(1-a)$. At a peak, direct subtraction yields [\[eq:defect\]](#eq:defect){reference-type="eqref" reference="eq:defect"}. Its denominator is positive for $0<a<1$, and the defect vanishes exactly when $g=1$. Then $\Omega=2\sqrt a$, proving [\[eq:firsthit\]](#eq:firsthit){reference-type="eqref" reference="eq:firsthit"}. At $g=0$ the mixing coefficient vanishes, completing the exceptional statement.

\>0

# Critical detuning window and boundary atlas

The factored defect is stronger than a statement that resonance suffices: it also fixes the scale on which inaccurate driving remains useful.

[\[cor:window\]]{#cor:window label="cor:window"} Let $k\in\mathbb N$, take $M=1$, $N=k^2$ (so $a=k^{-2}$), and set $g=1+c/k$, where $c\in\mathbb R$ is fixed and $k>|c|$. Then $$\label{eq:windowomega}
 \Omega^2=\frac{c^2+4+4c/k}{k^2},$$ and, as $k\to\infty$, $$\label{eq:window}
 p_{\max}\longrightarrow\frac{4}{c^2+4},\qquad
 \sqrt a\,t_{\rm peak}\longrightarrow\frac{\pi}{\sqrt{c^2+4}}.$$ Thus the nontrivial high-fidelity window has width $O(\sqrt a)$ around $g=1$; fixed nonzero detuning instead drives $p_{\max}$ to zero.

Substituting $a=k^{-2}$ and $g=1+c/k$ gives [\[eq:windowomega\]](#eq:windowomega){reference-type="eqref" reference="eq:windowomega"}. Substitution into [\[eq:pmax\]](#eq:pmax){reference-type="eqref" reference="eq:pmax"} and $t_{\rm peak}=\pi/\Omega$ proves both limits. For fixed $g\ne1$, the numerator of the oscillatory increment is $O(a)$ while the denominator tends to $(g-1)^2$.

The usual complete-graph formulation has no hidden normalization discrepancy. Indeed, for the adjacency matrix $A(K_N)$, $$\label{eq:adjacency}
 A(K_N)=N|s\rangle\langle s|-I.$$ If $g=\gamma N$, then $$\label{eq:shift}
 -\gamma A(K_N)-P_W=H_g+\gamma I,
 \qquad
 e^{-\mathrm{i}t(-\gamma A-P_W)}=e^{-\mathrm{i}\gamma t}e^{-\mathrm{i}tH_g}.$$ Thus every probability agrees, although absolute eigenvalue ledgers differ by $\gamma$. Equation [\[eq:shift\]](#eq:shift){reference-type="eqref" reference="eq:shift"} is a global-phase equivalence, not an equality of Hamiltonians.

[\[thm:faces\]]{#thm:faces label="thm:faces"} For $N\geq1$ the boundary data are as follows.

1.  If $M=0$, the spectrum is $-g$ once and $0$ with multiplicity $N-1$; success is identically zero.

2.  If $M=N$, the spectrum is $-(g+1)$ once and $-1$ with multiplicity $N-1$; success is identically one.

3.  These formulas include $N=1$: the orthogonal multiplicity is zero, so no nonexistent dark vector is introduced.

4.  If $0<M<N$ and $g=0$, the spectrum is $-1$ with multiplicity $M$ and $0$ with multiplicity $N-M$, while success is the constant $M/N$.

When $M=0$, $P_W=0$ and the rank-one projector $|s\rangle\langle s|$ supplies the first spectrum. When $M=N$, $P_W=I$ supplies the second. A one-dimensional space has no orthogonal complement. Finally $g=0$ leaves the oracle projector alone, so marked and unmarked amplitudes cannot mix.

\>1

# Evidence collision and Route boundary

The machine-readable evidence enumerates all $N=2,\ldots,32$, every $M=1,\ldots,N-1$, and $$g\in\{0,1/4,1/2,1,3/2,2,4\},$$ giving 3,472 exact interior rows. It adds 28 critical-window witnesses and 256 boundary rows, for 75,296 audited scalar leaves. An independently written checker reconstructs the schema, both hashes of the locked Route-A YAML, every exact row, and selected full-matrix spectra and exponentials at 72 digits: 77,169 checks. SymPy closes 17,885 exact identities; two isolated producer runs replay byte for byte; 41 repaired-hash, parser, nonfinite, duplicate-key, and semantic mutations must fail. The finite grid is a regression certificate. Theorems [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} and [\[thm:faces\]](#thm:faces){reference-type="ref" reference="thm:faces"} and Corollary [\[cor:window\]](#cor:window){reference-type="ref" reference="cor:window"} have the stated all-parameter domains.

Farhi and Gutmann introduced continuous-time Hamiltonian search and its square-root clock in the rank-one marked setting [@farhigutmann]. The present arbitrary-$M$, arbitrary-detuning closure is a source-local reconstruction; no literature-priority claim is made. It is also disjoint from the workspace's C143 discrete-time coined five-cycle walk, C171 stochastic Ehrenfest hypercube, C183 random-transposition Markov operator, C223 Jaynes--Cummings blocks, and C318 one-dimensional SSH chain. The distinguishing object here is a permutation-symmetric oracle Hamiltonian and its exact resonance window.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ The dynamics has a genuine physical unitary clock and source-native Hermitian quantization, but no rational-prime payload, arithmetic primitive-orbit ledger, Euler product, target divisor, counting law, functional equation, or target zero correspondence. In particular $H_g$ is not claimed to be a Hilbert--Pólya operator. Route A is rejected and Route B remains locked.

9 E. Farhi and S. Gutmann, "An analog analogue of a digital quantum computation," *Physical Review A* **57** (1998), 2403--2406. [doi:10.1103/PhysRevA.57.2403](https://doi.org/10.1103/PhysRevA.57.2403); [quant-ph/9612026](https://arxiv.org/abs/quant-ph/9612026).
