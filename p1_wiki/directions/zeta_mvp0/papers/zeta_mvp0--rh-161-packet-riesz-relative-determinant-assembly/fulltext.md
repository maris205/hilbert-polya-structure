---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-161-packet-riesz-relative-determinant-assembly"
canonical_tex: "zeta_mvp0/papers/RH-161-packet-riesz-relative-determinant-assembly/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-161-packet-riesz-relative-determinant-assembly/main.pdf"
source_sha256: "5cb89f50d0e73ac3537622d0736bc6bd0492da2503a47ea6487cf4b965c358d9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# From Reset Packets to Riesz Clouds: A Typed Relative-Determinant Assembly Theorem for Prime Dynamics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-161-packet-riesz-relative-determinant-assembly>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-161-packet-riesz-relative-determinant-assembly/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-161-packet-riesz-relative-determinant-assembly/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-161-packet-riesz-relative-determinant-assembly/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-161-packet-riesz-relative-determinant-assembly/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The minimum viable prime-dynamics roadmap isolates a canonical all-level intrinsic determinant as its first missing macro gate. Two rigorous pieces approach that gate from opposite sides. RH-80 proves exact moving-cloud factorization and a relative Fredholm determinant theorem once a reducing Riesz cloud and a trace-class complement are available. RH-160 proves conditional native and bounded-lag reset-support floors, but its output is a packet statistic rather than a spectral projection. The instruction to "feed the packet into the determinant" therefore hides a genuine type gap.

  We make that gap explicit for both determinant types used upstream. Fix $p\in\{1,2\}$, let $A_j\in\mathcal S_p$ be Schatten-class operators, $P_j$ finite packet projections, and $A_j^{(0)}$ the block diagonalization relative to $P_j$. On a contour $\Gamma$, if $$M_j\varepsilon_j<1,
   \qquad
   \delta_j:=\frac{|\Gamma|}{2\pi}
   \frac{M_j^2\varepsilon_j}{1-M_j\varepsilon_j}<1,$$ where $M_j$ bounds the block resolvent and $\varepsilon_j=\left\lVert A_j-A_j^{(0)}\right\rVert$, then $\Gamma$ remains in the full resolvent, its Riesz projection $\Pi_j$ has rank $\operatorname{rank}P_j$, and $\left\lVert\Pi_j-P_j\right\rVert\leq\delta_j$. The first inequality preserves spectral rank by homotopy; the stronger second inequality supplies a stable packet-to-Riesz graph bridge.

  Combining this lift with exact cloud division, a common-space $\mathcal S_p$ limit for the complementary blocks, a deterministic pole ledger, canonical zero-free normalization, and directed marked-trace convergence yields a canonical meromorphic relative determinant with retained temporal data. The $p=1$ branch is the two-step Fredholm version; the $p=2$ branch is the one-step regularized-determinant version required by the MVP roadmap. We prove the quantitative assembly theorem, determinant and marked-trace error bounds, and six omission witnesses. The architecture-relative completion frontier has two bundles, according to whether the native or adaptive-lag reset seed is used; both also require the five open interfaces $R,Q,U,Z,T$.

  This closes the abstract typed assembly implication, not its application. No eventual reset law, physical packet-to-Riesz estimate, uniform complement limit, canonical all-level determinant, Hilbert--Polya operator, zeta-zero identity, or Riemann-hypothesis conclusion is proved.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  **From Reset Packets to Riesz Clouds:**\
  A Typed Relative-Determinant Assembly Theorem for Prime Dynamics
```

## Markdown 正文

**Keywords:** Riesz projection; Fredholm determinant; regularized determinant; spectral packet; trace ideal; moving cloud; nonselfadjoint dynamics; research roadmap.

# The type error hidden inside Gate A

At fixed positive noise, the prime-dynamics program has intrinsic trace-ideal determinants and continuum bridges. RH-45 connects the one-step $\det_2$ object to its exact symmetric two-step Fredholm completion [@WangRH45]. In the small-noise regime, RH-80 proves that a fixed limiting pole factor cannot renormalize a disk across the cloud circle. Its valid replacement is the exact finite determinant carried by a reducing moving Riesz projection [@WangRH80]. RH-160, by contrast, constructs conditional lower bounds for reset packets from overlap, weak-mode separation, spectral spread, and---if needed---a bounded-lag fourth-cross interface [@WangRH160].

These outputs have different types: $$\text{reset packet }P_j
 \quad\not\equiv\quad
 \text{Riesz projection }\Pi_j.$$ A positive compression or fourth-cross statistic does not imply that the packet is invariant, that it encloses the correct spectral multiplicity, or that its complement is uniformly trace class. The MVP roadmap correctly left the resulting typed assembly open [@WangMVP1].

The purpose of RH-161 is to state and prove the missing abstract implication without promoting its physical hypotheses. It separates six obligations:

$S$

:   one eventual native or bounded-lag reset seed;

$R$

:   a contour-resolvent/coupling estimate lifting that packet to a same-rank Riesz cloud;

$Q$

:   an exact cloud coefficient bridge and deterministic pole ledger;

$U$

:   a common-space Schatten-norm limit of the complementary block;

$Z$

:   target-independent zero-free normalization and schedule independence;

$T$

:   convergence of the directed marked words needed to retain temporal orientation.

Only the functional-analytic implications below are proved. The current prime-dynamics status of $S$ is conditional, and $R,Q,U,Z,T$ are open.

# Packet-to-Riesz lifting

Let $A\in\mathcal B(\mathcal H)$, let $P$ be a finite-rank orthogonal projection, and put $Q=I-P$. Define the packet block diagonalization $$A^{(0)}=PAP+QAQ,
 \qquad E=A-A^{(0)}=PAQ+QAP.$$ Let $\Gamma$ be a positively oriented rectifiable Jordan curve. Assume that $\Gamma$ isolates the entire packet block and no complementary spectrum: $$\label{eq:block-riesz}
 P=\frac{1}{2\pi i}\int_\Gamma(z-A^{(0)})^{-1}\,dz,
 \qquad
 M:=\sup_{z\in\Gamma}\left\lVert(z-A^{(0)})^{-1}\right\rVert<\infty.$$ This equation is stronger than saying merely that $PAP$ has positive singular values; it is the spectral-separation input.

[\[thm:riesz-lift\]]{#thm:riesz-lift label="thm:riesz-lift"} Let [\[eq:block-riesz\]](#eq:block-riesz){reference-type="eqref" reference="eq:block-riesz"} hold, set $\varepsilon=\left\lVert E\right\rVert$, and suppose $M\varepsilon<1$. Then $\Gamma\subset\rho(A_t)$ for every $A_t=A^{(0)}+tE$, $0\leq t\leq1$, and the full Riesz projection $$\Pi=\frac{1}{2\pi i}\int_\Gamma(z-A)^{-1}\,dz$$ has $$\operatorname{rank}\Pi=\operatorname{rank}P.$$ Moreover, $$\label{eq:projector-bound}
 \left\lVert\Pi-P\right\rVert
 \leq \frac{|\Gamma|}{2\pi}
 \frac{M^2\varepsilon}{1-M\varepsilon}
 =:\delta.$$ If $\delta<1$, then $\Pi|_{\operatorname{Ran}P}:\operatorname{Ran}P\to\operatorname{Ran}\Pi$ is invertible and the true cloud is a stable graph over the reset packet.

For $z\in\Gamma$, $$z-A_t=\bigl(I-tE(z-A^{(0)})^{-1}\bigr)(z-A^{(0)}).$$ The first factor is invertible by a Neumann series because $t\varepsilon M<1$. Hence the contour stays in the resolvent throughout the homotopy. The Riesz projections $\Pi_t$ vary continuously in operator norm, so their finite rank is constant; at $t=0$ it is $\operatorname{rank}P$ [@Kato1995].

The resolvent bound $$\sup_{z\in\Gamma}\left\lVert(z-A)^{-1}\right\rVert
 \leq\frac{M}{1-M\varepsilon}$$ and the resolvent identity give $$\Pi-P=\frac{1}{2\pi i}\int_\Gamma
 (z-A)^{-1}E(z-A^{(0)})^{-1}\,dz.$$ Taking norms proves [\[eq:projector-bound\]](#eq:projector-bound){reference-type="eqref" reference="eq:projector-bound"}. Finally, if $x\in\operatorname{Ran}P$ and $\Pi x=0$, then $\left\lVert x\right\rVert=\left\lVert(P-\Pi)x\right\rVert\leq\delta\left\lVert x\right\rVert$, so $x=0$. The restriction is injective between spaces of the same finite dimension and hence invertible. Also $\left\lVert\Pi x\right\rVert\geq(1-\delta)\left\lVert x\right\rVert$ on $\operatorname{Ran}P$, so the inverse has norm at most $(1-\delta)^{-1}$. Similarly, for $y\in\operatorname{Ran}\Pi$, $\left\lVert Py\right\rVert\geq(1-\delta)\left\lVert y\right\rVert$, so $P|_{\operatorname{Ran}\Pi}$ is the inverse-direction isomorphism. Hence $\operatorname{Ran}\Pi$ is the graph of a bounded map $X:\operatorname{Ran}P\to\operatorname{Ran}Q$: if $J=\Pi|_{\operatorname{Ran}P}$, then $X=QJ(PJ)^{-1}$. Since $\left\lVert QJ\right\rVert\leq\delta$ and $\left\lVert PJ-I_{\operatorname{Ran}P}\right\rVert\leq\delta$, one has $\left\lVert X\right\rVert\leq\delta/(1-\delta)$.

The condition $M\varepsilon<1$ already certifies rank preservation. The stronger bound $\delta<1$ certifies a quantitatively usable graph bridge. If the latter test fails, the estimate is inconclusive; it does not prove that the actual spectral rank changes.

[\[cor:two-block\]]{#cor:two-block label="cor:two-block"} Assume $\Gamma$ encloses the full spectrum of $PAP$ on $\operatorname{Ran}P$ and no spectrum of $QAQ$ on $\operatorname{Ran}Q$. Put $$\begin{aligned}
 M_P&=\sup_{z\in\Gamma}
 \left\lVert(z-PAP|_{\operatorname{Ran}P})^{-1}\right\rVert,\\
 M_Q&=\sup_{z\in\Gamma}
 \left\lVert(z-QAQ|_{\operatorname{Ran}Q})^{-1}\right\rVert,\\
 M&=\max(M_P,M_Q),\qquad
 \varepsilon=\left\lVert PAQ+QAP\right\rVert.\end{aligned}$$ Then Theorem [\[thm:riesz-lift\]](#thm:riesz-lift){reference-type="ref" reference="thm:riesz-lift"} applies whenever $M\varepsilon<1$; one may further use $$\varepsilon\leq\left\lVert PAQ\right\rVert+\left\lVert QAP\right\rVert$$ in a separately assembled certificate.

The resolvent of $A^{(0)}$ is the direct sum of the two displayed block resolvents, so its norm is bounded by $M$. The off-diagonal estimate is the triangle inequality.

For a nonnormal block, spectral distance alone need not control $M_P$ or $M_Q$. The certificate is deliberately resolvent-based: replacing these quantities by an eigenvalue gap without a normality or conditioning theorem would reopen the pseudospectral error that the Riesz lift is meant to close.

# Exact relative determinants and complement convergence

Fix $p\in\{1,2\}$, let $A_j\in\mathcal S_p(\mathcal H_j)$, and let $\Pi_j$ be the Riesz projections supplied by Theorem [\[thm:riesz-lift\]](#thm:riesz-lift){reference-type="ref" reference="thm:riesz-lift"}. Write $\det_1=\det$ and let $\det_2$ denote the second regularized determinant. Riesz projections commute with $A_j$, so $$\mathcal H_j=\operatorname{Ran}\Pi_j\oplus\operatorname{Ran}(I-\Pi_j)$$ is an invariant topological direct sum. Write $$\begin{aligned}
 C_{j,p}(z)&=\det_{p,\operatorname{Ran}\Pi_j}(I-zA_j|_{\operatorname{Ran}\Pi_j}),\\
 R_{j,p}(z)&=\det_p(I-zS_j),
 \qquad S_j=A_j|_{\operatorname{Ran}(I-\Pi_j)}.\end{aligned}$$ The exact factorization $$\label{eq:factorization}
 \det_p(I-zA_j)=C_{j,p}(z)R_{j,p}(z)$$ fills every apparent quotient singularity at a cloud zero [@Simon2005]. For $p=1$ this is RH-80's two-step Fredholm determinant. For $p=2$ it is the one-step regularized determinant used in RH-MVP1. Multiplicativity is exact here because the decomposition is an invariant direct sum; no multiplicative anomaly crosses the blocks.

The branches are related but not interchangeable. For $T\in\mathcal S_2$, $$\det_2(I-zT)\det_2(I+zT)=\det(I-z^2T^2),$$ so the two-step Fredholm determinant is the symmetric completion of the one-step regularized determinant [@WangRH45]. It does not, by itself, select either one-step factor. We therefore carry $p$ as part of the output type instead of silently identifying the branches.

The spaces $\operatorname{Ran}(I-\Pi_j)$ vary, so an all-level limit requires explicit identifications. Assume bounded isomorphisms $V_j:\operatorname{Ran}(I-\Pi_j)\to\mathcal H_\infty$ and define $\widetilde S_j=V_jS_jV_j^{-1}\in\mathcal S_p(\mathcal H_\infty)$.

[\[prop:det-transfer\]]{#prop:det-transfer label="prop:det-transfer"} If $$\left\lVert\widetilde S_j-S_\infty\right\rVert_p\longrightarrow0,$$ then $R_{j,p}\to R_{\infty,p}:=\det_p(I-zS_\infty)$ locally uniformly on $\mathbb C$. More explicitly, if $\left\lVert\widetilde S_j-S_\infty\right\rVert_2\leq\eta_j$, $\left\lVert\widetilde S_j\right\rVert_2\leq K$, and $p=2$, then $$\label{eq:det2-bound}
 \sup_{|z|\leq r}|R_{j,2}(z)-R_{\infty,2}(z)|
 \leq r\eta_j
 \exp\!\left(\frac12\left[r(K+\left\lVert S_\infty\right\rVert_2)+1\right]^2\right).$$ If $p=1$, $\left\lVert\widetilde S_j-S_\infty\right\rVert_1\leq\eta_j$ and $\left\lVert\widetilde S_j\right\rVert_1\leq K$, then for every $r>0$, $$\label{eq:det-bound}
 \sup_{|z|\leq r}|R_{j,1}(z)-R_{\infty,1}(z)|
 \leq r\eta_j
 \exp\!\left(1+r(K+\left\lVert S_\infty\right\rVert_1)\right),$$ and the residual family is normal.

Similarity invariance identifies $R_{j,p}$ with $\det_p(I-z\widetilde S_j)$. For $p=2$, apply $$|\det_2(I+B)-\det_2(I+C)|
 \leq\left\lVert B-C\right\rVert_2
 \exp\!\left(\frac12(\left\lVert B\right\rVert_2+\left\lVert C\right\rVert_2+1)^2\right)$$ to $B=-z\widetilde S_j$ and $C=-zS_\infty$ [@Simon2005]. For $p=1$, apply the quantitative trace-class inequality $$|\det(I+B)-\det(I+C)|
 \leq\left\lVert B-C\right\rVert_1e^{1+\left\lVert B\right\rVert_1+\left\lVert C\right\rVert_1}$$ to $B=-z\widetilde S_j$ and $C=-zS_\infty$ [@Simon2005].

This proposition is not implied by a native packet floor. It is a separate absolute Schatten-ideal interface $U_p$. The physical program may use the $p=1$ two-step branch, the $p=2$ one-step branch, or both; the theorem does not identify their limits with each other.

# Directed marked traces

Ordinary two-factor spectra cannot record temporal orientation: $AB$ and $BA$ have the same nonzero spectrum. RH-8 therefore introduced directed three-step and parity-compatible six-step traces [@WangRH8]. A scalar determinant alone does not preserve these data automatically.

Let $$\tau_J(A_1,\ldots,A_m)=\operatorname{Tr}(JA_1\cdots A_m),$$ where $J\in\mathcal S_1$ is a fixed separating marker. The marker may encode a state--observable pairing or the commutator sector needed by the directed construction.

[\[prop:marked\]]{#prop:marked label="prop:marked"} Suppose $\left\lVert A_k\right\rVert,\left\lVert B_k\right\rVert\leq L$ and $\left\lVert A_k-B_k\right\rVert\leq e$ for $1\leq k\leq m$. Then $$\label{eq:marked-bound}
 |\tau_J(A_1,\ldots,A_m)-\tau_J(B_1,\ldots,B_m)|
 \leq \left\lVert J\right\rVert_1\,mL^{m-1}e.$$

Telescope the difference of the two noncommutative products, changing one factor at a time. Each of the $m$ summands has operator norm at most $L^{m-1}e$. Use $|\operatorname{Tr}(JX)|\leq\left\lVert J\right\rVert_1\left\lVert X\right\rVert$.

Thus a common-space operator bridge can transport the selected three/six-step marked traces. Merely knowing the ordinary determinant or unordered eigenvalues cannot.

Accordingly, the typed output is not a scalar determinant alone. For a fixed finite separating list of directed words $\mathcal W$, with word $w$ carrying marker $J_w$ and factors $A_{j,w,1},\ldots,A_{j,w,m_w}$, define the enhanced determinant datum $$\mathfrak D_{j,p}=(\mathcal D_{j,p},\Theta_j),
 \qquad
 \Theta_j=\left(
 \tau_{J_w}(A_{j,w,1},\ldots,A_{j,w,m_w})
 \right)_{w\in\mathcal W}.$$ The scalar component controls the spectral divisor; the marked component retains the temporal information that the scalar component cannot encode.

# Typed moving-cloud assembly

The deterministic small-noise target is meromorphic. Let $P_{\rm det}(z)$ be its exactly derived holomorphic pole-cancellation factor, normalized by $P_{\rm det}(0)=1$; its zeros, with multiplicity, are the deterministic pole divisor. Let $Z_j$ be zero-free holomorphic normalizations satisfying $Z_j(0)=1$ and independent of any target zero data. All objects in this paragraph are branch-specific after $p$ is fixed; no equality between the $p=1$ and $p=2$ pole ledgers or normalizations is assumed.

[\[thm:assembly\]]{#thm:assembly label="thm:assembly"} Fix $p\in\{1,2\}$. For an admissible all-level schedule, assume:

1.  one reset route $S_{\rm native}$ or $S_{\rm lagged}$ supplies finite packets of the required output type;

2.  interface $R$: Theorem [\[thm:riesz-lift\]](#thm:riesz-lift){reference-type="ref" reference="thm:riesz-lift"} holds eventually with a uniform $\delta<1$ and fixes the intended cloud rank;

3.  interface $Q$: $P_{\rm det}$ is the complete deterministic pole ledger and, as germs at zero, every Taylor coefficient of the exact finite cloud factor $C_{j,p}$ converges to the corresponding coefficient of $P_{\rm det}^{-1}$;

4.  interface $U$: the transported complementary blocks converge in Schatten norm $\mathcal S_p$ as in Proposition [\[prop:det-transfer\]](#prop:det-transfer){reference-type="ref" reference="prop:det-transfer"};

5.  interface $Z$: $Z_j\to Z_\infty$ locally uniformly, with a unique target-independent normalization, and every admissible schedule gives the same $Z_\infty R_{\infty,p}$;

6.  interface $T$: for one fixed separating list $\mathcal W$, the selected directed marked words converge under a common-space bridge to a schedule-independent vector $\Theta_\infty$.

Then $$\label{eq:assembled-object}
 \mathcal D_{j,p}(z):=Z_j(z)\frac{\det_p(I-zA_j)}{C_{j,p}(z)}
 =Z_j(z)R_{j,p}(z)
 \longrightarrow \mathcal D_{{\rm rel},p}(z):=Z_\infty(z)R_{\infty,p}(z)$$ locally uniformly on $\mathbb C$. The pole-completed object $$\label{eq:meromorphic-object}
 \mathcal D_{{\rm dyn},p}(z)=\frac{\mathcal D_{{\rm rel},p}(z)}{P_{\rm det}(z)}$$ is canonical and meromorphic and its cloud zeros are removed by exact factorization rather than pointwise division. The enhanced output $$\mathfrak D_{{\rm dyn},p}=(\mathcal D_{{\rm dyn},p},\Theta_\infty)$$ is therefore canonical and retains the specified directed data.

Interface $R$ supplies a reducing same-rank Riesz cloud, so [\[eq:factorization\]](#eq:factorization){reference-type="eqref" reference="eq:factorization"} makes every quotient in [\[eq:assembled-object\]](#eq:assembled-object){reference-type="eqref" reference="eq:assembled-object"} an entire determinant. Interface $U$ and Proposition [\[prop:det-transfer\]](#prop:det-transfer){reference-type="ref" reference="prop:det-transfer"} give $R_{j,p}\to R_{\infty,p}$ locally uniformly. Multiplication by the locally uniformly convergent zero-free $Z_j$ preserves convergence. Interface $Z$ makes the scalar limit schedule independent and fixes the otherwise arbitrary zero-free factor. Interface $Q$ attaches the exact deterministic pole divisor, yielding [\[eq:meromorphic-object\]](#eq:meromorphic-object){reference-type="eqref" reference="eq:meromorphic-object"}; it also shows coefficientwise near zero that $$Z_j(z)\det_p(I-zA_j)=Z_j(z)C_{j,p}(z)R_{j,p}(z)
 \longrightarrow \frac{Z_\infty(z)R_{\infty,p}(z)}{P_{\rm det}(z)},$$ so the meromorphic object is the identified full determinant germ rather than an arbitrary appended pole factor. Finally, interface $T$ and Proposition [\[prop:marked\]](#prop:marked){reference-type="ref" reference="prop:marked"} give the unique marked vector $\Theta_\infty$. No zero-data comparison enters the construction.

The $p=2$ conclusion has precisely the determinant type required by macro Gate $A$ from RH-MVP1, provided every physical premise is proved. The $p=1$ conclusion is the two-step RH-80 branch. The theorem does not prove those premises and does not identify their limits; it says nothing yet about a canonical scattering completion, self-adjoint generator, prime-power trace formula, or zeta divisor.

# Minimal frontier and omission witnesses

At the current statuses, the assembly formula is $$A_{\rm typed}
 =(S_{\rm native}\vee S_{\rm lagged})\wedge R\wedge Q\wedge U\wedge Z\wedge T.$$ The two seed implications are conditional; $R,Q,U,Z,T$ are open for the physical family.

The inclusion-minimal missing bundles are exactly $$\begin{aligned}
 \{S_{\rm native},R,Q,U,Z,T\},\qquad
 \{S_{\rm lagged},R,Q,U,Z,T\}.\end{aligned}$$

The formula is an OR between the two seed leaves followed by five conjunctive interfaces. Proved leaves would contribute no debt, a no-go leaf would kill only its branch, and every conditional or open leaf remains debt. Taking the inclusion-minimal antichain gives the two displayed bundles.

None of the six mathematical functions may be deleted without replacement:

1.  without $S$, an isolated cloud may exist while the selected reset packet becomes asymptotically orthogonal to it;

2.  without $R$, take $A=\operatorname{diag}(-1,2)$ and let $P$ project onto $(1,1)$: $PAP$ is positive, but $P$ is not invariant or Riesz;

3.  without $Q$, the same finite relative determinant can be attached to different deterministic pole ledgers, producing inequivalent meromorphic objects;

4.  without $U$, append rank-one complementary blocks with eigenvalue tending to infinity; their $\mathcal S_p$ norms diverge and the residual $\det_p$ family need not be locally bounded;

5.  without $Z$, replace $R_{j,p}(z)$ by $e^{c_jz}R_{j,p}(z)$ for schedule-dependent $c_j$; the zero divisor is unchanged but canonicity is lost;

6.  without $T$, let $A=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)$, $B=\left(\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right)$, and $J=\operatorname{diag}(1,0)$. The products $AB$ and $BA$ have the same determinant data, while $\operatorname{Tr}(JAB)=1$ and $\operatorname{Tr}(JBA)=0$.

These witnesses establish minimality only relative to the present typed architecture. A future theorem may replace two interfaces by one stronger construction, but it must still perform both functions.

![The typed assembly chain, an illustrative packet-to-Riesz certificate, quantitative determinant transfer, and independent interface failure modes. The numerical constants in panels (b)--(c) demonstrate the bounds; they are not measurements of the prime-dynamics operator.](<../../../../../zeta_mvp0/papers/RH-161-packet-riesz-relative-determinant-assembly/figures/typed_moving_cloud_assembly.pdf>){#fig:assembly width="\\textwidth"}

# Machine-readable audit

The audit evaluates the projector bound for six illustrative coupling values with $|\Gamma|=2\pi$ and $M=2$. Every value has $M\varepsilon<1$ and therefore certified spectral-rank preservation. Three also satisfy $\delta<1$ and give a stable packet graph; three fail only this stronger sufficient certificate. This balanced table is an algebraic regression test, not physical evidence.

It also records the standard trace-class determinant bound on $|z|\leq1/2$, the marked word bound at lengths two, three, and six, the two completion bundles, and the six omission mechanisms. The RH-8 temporal summary and the RH-45, RH-80, RH-160, and RH-MVP1 publication archives are hashed as external inputs. The audit verifies internal formulas and claim types, not the open all-level interfaces.

# Route consequence and boundary

RH-161 resolves an ambiguity in the roadmap. "Typed assembly" is no longer a black box: it is a conditional theorem with a quantitative first bridge and five remaining operator/analytic obligations. In particular, RH-160's native route can be used only if the downstream determinant needs compression support; a directional seed is necessary when the marked-trace bridge requires fourth-cross information. Either way, a reset floor cannot replace spectral isolation.

The best next target is interface $R$ on the actual finite/noisy family: construct a contour around the proposed cloud and jointly bound the block resolvent $M_j$ and off-packet coupling $\varepsilon_j$. A persistent $M_j\varepsilon_j\geq1$ would reject the current Neumann corridor, though not all possible Riesz constructions. If $R$ closes, the next decisive wall is $U_p$, the common-space complementary Schatten-norm limit: trace norm for the RH-80 two-step branch and Hilbert--Schmidt norm for the MVP one-step branch. This decides whether the relative determinants form a genuine fixed-disk normal family.

No eventual O/E/S/L law, physical packet-to-Riesz bridge, cloud coefficient bridge, Schatten complement limit, canonical Gate-A determinant, scattering completion, self-adjoint Hilbert--Polya operator, prime-power identity, zeta-zero identification, or proof of the Riemann Hypothesis is claimed.
