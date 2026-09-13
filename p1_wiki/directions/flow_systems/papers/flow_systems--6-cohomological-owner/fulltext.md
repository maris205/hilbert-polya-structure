---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--6-cohomological-owner"
canonical_tex: "flow_systems/papers/6-cohomological-owner/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/6-cohomological-owner/paper/paper.pdf"
source_sha256: "d36783ebbfabd67fdda7f04d1aae3556e72b137e51985b7cd6448a35f0cb8219"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Which Operator Owns the Zeta? Koopman and Frobenius Ledgers of an Arithmetic Suspension

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/6-cohomological-owner>)
- [规范 TeX](<../../../../../flow_systems/papers/6-cohomological-owner/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/6-cohomological-owner/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/6-cohomological-owner/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/6-cohomological-owner/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An arithmetic parent can generate an exact orbit zeta and a natural self-adjoint flow operator without making the two constructions one spectral determinant. We prove this distinction for the constant-roof Frobenius suspension of $\mathbb P^1/\mathbb F_2$. Closed points, primitive suspension circles, point counts, and graded $\ell$-adic Frobenius traces form one exact native ledger: $$\sum_{d\mid n}d a_d=1+2^n
   \quad\text{and}\quad
   Z(X,t)=\frac1{(1-t)(1-2t)}.$$ The determinant owner is Frobenius on finite-dimensional graded $\ell$-adic cohomology. The natural Koopman owner of suspension time is instead the self-adjoint periodic derivative $A_K$ on the Hilbert direct sum of all closed-point circles. Its point spectrum is $(2\pi/\log2)\mathbb Q$, every eigenvalue has countably infinite multiplicity, and its full and essential spectra equal $\mathbb R$. Hence its resolvent is noncompact and its Gaussian heat operator is not trace class. The two operators are not unitarily equivalent, and adjoining any finite-dimensional realization of Frobenius to $A_K$ preserves the essential-spectrum obstruction. The substitution $t=2^{-s}$ merely lifts the two native factors to pole lattices on $\operatorname{Re}s=0,1$; it does not create a self-adjoint energy spectrum. This is an exact same-parent Lefschetz positive control and a frozen-object Route-B obstruction, not a universal no-go theorem for future cohomological flows.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: 13 August 2026
title: |
  **Which Operator Owns the Zeta?**\
  Koopman and Frobenius Ledgers of an Arithmetic Suspension
```

## Markdown 正文

**摘要**

同一个算术母体可以同时产生精确的轨道 zeta 与自然的自伴流算子，但这并不 意味着二者属于同一个谱行列式。本文在 $\mathbb P^1/\mathbb F_2$ 的常值屋顶 Frobenius 悬挂流上严格证明这种 区别。闭点、本原悬挂圆周、点计数与分次 $\ell$-进 Frobenius 迹构成一个 精确的有限域账本：$\sum_{d\mid n}d a_d=1+2^n$，且 $Z(X,t)=((1-t)(1-2t))^{-1}$。这个行列式的拥有者是有限维分次 $\ell$-进上同调上的 Frobenius。悬挂时间的自然 Koopman 拥有者则是所有 闭点圆周 Hilbert 直和上的周期导数 $A_K$。该算子自伴，点谱为 $(2\pi/\log2)\mathbb Q$，每个特征值均具有可数无穷重数，全谱与本质谱 均为 $\mathbb R$；因此预解算子不紧，Gaussian 热算子也非迹类。两个 算子不可能酉等价；把 Frobenius 的任意有限维实现直和到 $A_K$ 上，仍然 保留本质谱阻碍。变量代换 $t=2^{-s}$ 只把两个有限域因子提升成 $\operatorname{Re}s=0,1$ 上的极点格，并不会产生新的自伴能谱。该结果是 精确的同母体 Lefschetz 正控与冻结对象上的 Route-B 阻碍，而不是对未来 所有上同调流的普遍不可行定理。

**Keywords:** Frobenius suspension; Hasse--Weil zeta; Lefschetz trace; Koopman generator; operator ownership; essential spectrum.

# Introduction

Scalar equality is weaker than operator identity. This is especially easy to overlook when several constructions arise from the same arithmetic scheme. Closed points of a finite-field variety give an Euler product; their geometric Frobenius cycles give a suspension flow; and étale cohomology gives an exact graded determinant. The first two papers in this branch established an exact finite-field orbit-zeta positive control and then classified its canonical Koopman lift. The present paper asks which operator actually owns the determinant.

For the frozen example $X=\mathbb P^1_{\mathbb F_2}$, all three classical ledgers are exact. Deligne's trace and determinant formulas identify the owner of the native zeta as Frobenius on graded étale cohomology [@Deligne1974]. Koopman's construction, Stone's theorem, and the orthogonal-sum theorem independently identify a complete self-adjoint generator of suspension time [@Koopman1931; @Stone1932; @Teschl2009]. Those are positive results, but they belong to different analytic operators.

The distinction is decisive for Route B. A certificate cannot take self-adjointness from the Koopman derivative and a determinant from cohomological Frobenius unless an operator-level morphism and trace theorem transport both properties. Here an explicit spectral comparison rules out that identification for the frozen pair. It does not rule out a new cohomological flow, anisotropic transfer operator, or source-derived bridge.

# Frozen parent and three typed ledgers

Let $$X=\mathbb P^1_{\mathbb F_2},\qquad
 S=X(\overline{\mathbb F}_2)_{\rm disc},\qquad F(a)=a^2,
 \qquad \tau=\log2.$$ We use "square-map Frobenius" for $F$; sources that distinguish arithmetic and geometric Frobenius may use inverse conventions. Inverting the permutation reverses every finite cycle but preserves its degree and the suspension lengths used below.

The mapping torus and vertical flow are $$M_F=(S\times\mathbb R)/\mathbb Z,\qquad
 n\cdot(a,u)=(F^na,u-n\tau),\qquad
 \phi^t[a,u]=[a,u+t].$$ Closed points are the finite Frobenius orbits on geometric points [@Deligne1974 Sec. 1.4]. A closed point $x$ of degree $d_x$ therefore gives the primitive circle $$C_x=\mathbb R/(d_x\tau\mathbb Z),\qquad \ell_x=d_x\tau=\log N(x),
 \qquad M_F\cong\coprod_{x\in|X|}C_x.$$ The coproduct topology is a disclosed modeling choice; it is not the scheme topology.

Fix an auxiliary prime $\ell\ne2$, and write $$H^i_{\rm et}=H^i_{\rm et}(X_{\overline{\mathbb F}_2},\mathbb Q_\ell),\qquad
 \Phi=F^*:H^i_{\rm et}\longrightarrow H^i_{\rm et},$$ where $F^*$ is exactly the pullback convention in Deligne's equations (1.5.1)--(1.5.4). In Deligne's Galois terminology this action corresponds to geometric Frobenius, whereas the displayed point map remains the square map $a\mapsto a^2$. This convention statement, rather than an informal name, fixes every trace and determinant below.

Table [\[tab:owners\]](#tab:owners){reference-type="ref" reference="tab:owners"} freezes the three ledgers. A common parent is a real provenance relation, but it is not an operator conjugacy.

\@p0.16p0.22YY@ Ledger & Space/objects & Action or owner & Exact output\
Orbit & primitive circles $C_x$ & repeats of lengths $d_x\log2$ & closed-point Euler product\
Koopman & $\bigoplus_x L^2(C_x,w_xdu)$ & $A_K=-i\,d/du$, periodic domain & self-adjoint time; dense essential spectrum\
Cohomology & $\bigoplus_iH^i_{\rm et}(X_{\overline{\mathbb F}_2},\mathbb Q_\ell)$ & graded Frobenius $\Phi$ & exact Lefschetz trace and determinant\

# Closed points in every degree

Let $a_d$ be the number of degree-$d$ closed points of $X$. The factorization of $T^{2^n}-T$ as the product of all monic irreducible polynomials whose degrees divide $n$ gives $2^n=\sum_{d\mid n}dI_d$. Möbius inversion therefore gives $$a_1=3,\qquad
 a_d=\frac1d\sum_{e\mid d}\mu(e)2^{d/e}\quad(d>1).$$

[\[lem:degrees\]]{#lem:degrees label="lem:degrees"} For every integer $d\ge1$, $a_d>0$.

The degree-one points are $0,1,\infty$. For $d\ge2$, discard all positive summands except $2^d$ and bound the others absolutely: $$d a_d\ge 2^d-\sum_{\substack{e\mid d\\e\ge2}}2^{d/e}
 \ge2^d-\sum_{m=1}^{\lfloor d/2\rfloor}2^m
 =2^d-2^{\lfloor d/2\rfloor+1}+2>0.$$ Since $a_d$ is an integer, it is positive.

Only existence, rather than the exponential size of $a_d$, is needed for the spectral obstruction. One component in each positive degree already produces all denominators infinitely often.

# Exact point, cycle, and cohomological traces

[\[thm:ledgers\]]{#thm:ledgers label="thm:ledgers"} For every $n\ge1$, $$\sum_{d\mid n}d a_d
 =\#\mathbb P^1(\mathbb F_{2^n})
 =1+2^n
 =\sum_i(-1)^i\operatorname{Tr}(\Phi^n\mid H^i_{\rm et}).
 \label{eq:three-traces}$$ Consequently, as a formal series and analytically for $|t|<1/2$, $$\begin{split}
 Z(X,t)
 &=\exp\!\left(\sum_{n\ge1}\frac{1+2^n}{n}t^n\right)\\
 &=\prod_{x\in|X|}(1-t^{d_x})^{-1}
 =\prod_i\det(1-t\Phi\mid H^i_{\rm et})^{(-1)^{i+1}}\\
 &=\frac1{(1-t)(1-2t)}.
 \end{split}\label{eq:graded-determinant}$$

A primitive cycle of length $d$ contributes all $d$ of its points to $\operatorname{Fix}(F^n)$ exactly when $d\mid n$, proving the first equality. The projective line over $\mathbb F_{2^n}$ has $2^n+1$ points. Deligne's Lefschetz formula gives the final equality in [\[eq:three-traces\]](#eq:three-traces){reference-type="eqref" reference="eq:three-traces"}, and his determinant formula identifies the graded product in [\[eq:graded-determinant\]](#eq:graded-determinant){reference-type="eqref" reference="eq:graded-determinant"} [@Deligne1974 Eqs. (1.5.1)--(1.5.4)]. Equivalently, the two nonzero graded trace eigenvalues are $1$ and $2$. Applying $-\log(1-z)=\sum_{n\ge1}z^n/n$ proves the remaining identities and their absolute convergence for $|t|<1/2$.

The theorem answers the native ownership question: the exact determinant is the graded finite-dimensional cohomological determinant of $\Phi$. It is not thereby a Fredholm or spectral-zeta determinant of the Koopman generator. The Stacks trace chapter supplies an independent modern convention check; Deligne remains the load-bearing primary source [@StacksTrace2026].

# Complete Koopman owner of suspension time

Choose arbitrary component constants $0<w_x<\infty$ and define $$\mathcal H_w=\bigoplus_{x\in|X|}L^2(C_x,w_xdu),\qquad
 (U_t^{(w)}f)_x(u)=f_x(u-t).$$ Translation invariance gives a unitary group, and finite-component approximation proves strong continuity. This is the standard Koopman pullback construction [@TerElstLemanczyk2017]. The candidate uses the Stone convention $U_t^{(w)}=\mathrm e^{-itA_w}$.

Define $$A_w=\bigoplus_x\left(-i\frac d{du}\right)_x$$ on the complete graph domain $$\mathcal D(A_w)=\left\{f=(f_x):
 \begin{array}{l}
 f_x\in H^1_{\rm per}(0,d_x\log2)\text{ for every }x,\\
 \displaystyle\sum_xw_x\bigl(\|f_x\|_{L^2(du)}^2+
                   \|f_x'\|_{L^2(du)}^2\bigr)<\infty
 \end{array}\right\}.
 \label{eq:domain}$$

[\[thm:selfadjoint\]]{#thm:selfadjoint label="thm:selfadjoint"} The operator $A_w$ on [\[eq:domain\]](#eq:domain){reference-type="eqref" reference="eq:domain"} is self-adjoint and is the unique Stone generator of $U_t^{(w)}$. All positive component-weight choices are unitarily equivalent.

On a degree-$d_x$ component, periodic Fourier series give the normalized basis $$e_{x,n}^{(w)}(u)=(w_xd_x\log2)^{-1/2}
   \mathrm e^{2\pi inu/(d_x\log2)},\qquad
 A_we_{x,n}^{(w)}=\frac{2\pi n}{d_x\log2}e_{x,n}^{(w)}.$$ Thus each component is real multiplication on its maximal periodic $H^1$ domain. The countable orthogonal-sum theorem gives self-adjointness on exactly [\[eq:domain\]](#eq:domain){reference-type="eqref" reference="eq:domain"} [@Teschl2009 Thm. 2.23], and Stone's theorem identifies the translation generator [@Teschl2009 Thms. 5.1--5.2]. Finally, $(W_wf)_x=\sqrt{w_x}f_x$ is a unitary map to the unweighted space and commutes with translations and differentiation.

This establishes a genuine complete operator and self-adjointness. It does not establish a suitable spectral type or an arithmetic trace.

# Exact Koopman spectral type

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} For every positive component-weight family, $$\sigma_{\rm p}(A_w)=\frac{2\pi}{\log2}\mathbb Q,
 \qquad
 \sigma(A_w)=\sigma_{\rm ess}(A_w)=\mathbb R.
 \label{eq:spectrum}$$ Every point eigenvalue has countably infinite multiplicity, and $\sigma_{\rm disc}(A_w)=\varnothing$.

Lemma [\[lem:degrees\]](#lem:degrees){reference-type="ref" reference="lem:degrees"} and the component Fourier formula give $$\bigcup_{d\ge1}\frac{2\pi}{d\log2}\mathbb Z
 =\frac{2\pi}{\log2}\mathbb Q.$$ For a reduced rational $a/b$, degrees $kb$ and modes $ka$, $k\ge1$, give mutually orthogonal eigenvectors with the same eigenvalue. The basis is countable, so the multiplicity is countably infinite. The orthogonal-sum spectrum is the closure of the component spectra, hence $\mathbb R$. Rational points already have infinite-dimensional eigenspaces. At an irrational $\lambda$, choose rational eigenvalues $\lambda_j\to\lambda$ on mutually distinct components; their normalized eigenvectors are a singular Weyl sequence. Every real point is therefore essential.

The Fourier eigenvectors form a complete basis, so every vector spectral measure is pure point. This is compatible with $\sigma_{\rm c}(A_w)=\mathbb R\setminus(2\pi/\log2)\mathbb Q$ in the set-theoretic operator decomposition: the irrational points are non-eigenvalue accumulation points with dense nonsurjective range.

[\[cor:heat\]]{#cor:heat label="cor:heat"} The resolvent of $A_w$ is not compact. Every interval of positive width has infinite-rank spectral projection, and $\mathrm e^{-tA_w^2}$ is not trace class for any $t>0$. Deleting the zero eigenspace does not repair these failures.

The zero Fourier mode on each of the countably many components gives an infinite-dimensional kernel. The resolvent acts by the same nonzero scalar on that subspace, and the heat operator acts as the identity. After deleting the kernel, fix any nonzero rational eigenvalue; its infinite-dimensional eigenspace gives the same argument. Every positive-width interval contains a rational eigenvalue of infinite multiplicity.

# The operator-ownership theorem

[\[thm:owner\]]{#thm:owner label="thm:owner"} For the frozen parent $(X,F)$:

1.  $A_w$ is the self-adjoint owner of suspension time;

2.  $\Phi$ is the owner of the exact native graded determinant [\[eq:graded-determinant\]](#eq:graded-determinant){reference-type="eqref" reference="eq:graded-determinant"};

3.  no unitary equivalence identifies these two operators;

4.  adjoining any finite-dimensional complex realization of $\Phi$ to $A_w$ leaves essential spectrum $\mathbb R$, noncompact resolvent, and non-trace-class heat.

Thus a Route-B certificate cannot combine self-adjointness from $A_w$ with the trace or determinant of $\Phi$ without proving a new one-operator bridge.

The first two claims are Theorems [\[thm:selfadjoint\]](#thm:selfadjoint){reference-type="ref" reference="thm:selfadjoint"} and [\[thm:ledgers\]](#thm:ledgers){reference-type="ref" reference="thm:ledgers"}. The Koopman owner acts on an infinite-dimensional complex Hilbert space and has spectrum $\mathbb R$; the cohomological owner is a two-dimensional graded $\mathbb Q_\ell$-linear action with eigenvalue ledger $\{1,2\}$. They are not even operators over the same scalar field as frozen, and after any noncanonical complex realization their spectra exclude unitary equivalence. A finite-dimensional direct summand cannot remove the infinite-dimensional eigenspaces in Theorem [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"}, so every claim in Corollary [\[cor:heat\]](#cor:heat){reference-type="ref" reference="cor:heat"} persists.

The theorem is object-specific. A genuinely new cohomological flow, anisotropic space, coupling, or boundary condition must be frozen as a new candidate and re-audited; it is not ruled out here.

# The exponential lift is a variable preimage

[\[prop:lift\]]{#prop:lift label="prop:lift"} For $\alpha\in\{1,2\}$, the solutions of $1-\alpha2^{-s}=0$ are $$s=\frac{\log\alpha+2\pi ik}{\log2},\qquad k\in\mathbb Z.$$ Consequently the two inverse factors have pole lattices on $\operatorname{Re}s=0$ and $\operatorname{Re}s=1$, with imaginary period $2\pi/\log2$.

The equation is $\exp(\log\alpha-s\log2)=1$. Solving modulo $2\pi i\mathbb Z$ and renaming the integer sign gives the formula.

The infinitely many preimages arise because $s\mapsto2^{-s}$ is periodic. They are not new Frobenius eigenvalues or energies of $A_w$, and their divisor is not the completed Riemann $\xi$ divisor.

# Same-object certificate and route decisions

The orbit and cohomological ledgers pass a native same-parent certificate: Deligne's theorem supplies a typed global trace and determinant, not merely a coordinate splice. The stronger single-operator certificate fails because the self-adjoint and determinant owners differ. Table [\[tab:routes\]](#tab:routes){reference-type="ref" reference="tab:routes"} records the two target scopes separately.

@\>p0.19\>p0.25YY@ Scope & Positive result & Blocking result & Overall\
Native finite field & A0 arithmetic, A1 closed orbits, A2 exact determinant, A3 continuation, A4 unitary lift & Koopman not determinant owner; one characteristic only & scoped Route-A success; not Route-B ready\
Riemann target & same native definitions only & wrong prime clock, divisor, counting, and trace & `ROUTE_A_REJECTED`\
Limited Route B & B1 complete operator; B2 self-adjoint & B3, B4, and B5 fail for the frozen operator/target & `ROUTE_B_REJECTED`\

The exact formal limited verdict is $$\begin{gathered}
 \texttt{B1\_COMPLETE\_OPERATOR\_DEFINITION},\qquad
 \texttt{B2\_SELF\_ADJOINT},\\
 \texttt{B3\_FAIL},\qquad \texttt{B4\_FAIL},\qquad
 \texttt{B5\_FAIL}.
 \end{gathered}$$ B4 fails because no rational-prime/von-Mangoldt trace of $A_w$ exists in the candidate; the native Lefschetz trace belongs to $\Phi$. B5 fails because neither owner supplies a global determinant equal to completed $\xi$. The Hilbert--Pólya claim flag is therefore false.

# Deterministic controls and limitations

The standard-library reproduction suite checks exact finite consequences of the proofs: Möbius counts and fixed-point reconstruction through degree and iterate 24, equality of cycle/point/cohomological trace rows, rational Koopman multiplicity witnesses, and the lifted divisor ledger. The command

    ./experiments/reproduce.sh

runs ten tests and regenerates five hash-locked artifacts. All ten tests pass. The manifest SHA-256 is `4a78e430d08134bca09b88b4e5f3adf25b68692212893f6abeaad407d1711c16`. The suite uses exact integers and rationals, no Riemann zeros, fitted parameters, randomness, network data, or floating-point root finding. Finite controls are regressions; the infinite claims are proved above.

The main limitation is scope. The base is explicitly discretized and the suspension is a neutral countable coproduct of circles. The result neither tests nor excludes a coupled or hyperbolic arithmetic flow. It excludes the ordinary compact-resolvent/heat-determinant route for the frozen Koopman operator, not every possible relative or regularized trace. The cohomological action is naturally $\mathbb Q_\ell$-linear; copying its two eigenvalues into a complex diagonal matrix would add a realization rather than derive a Hilbert--Pólya Hamiltonian. Finally, the exact finite-field identity contains only characteristic two and cannot be promoted to the rational-prime target by analogy.

# Conclusion

The finite-field branch supplies a sharp positive and negative result at once. The orbit and graded cohomological ledgers share a genuine arithmetic parent and obey an exact global Lefschetz determinant identity. The natural self-adjoint flow-time operator is nevertheless a different owner with dense, infinitely degenerate essential spectrum. Exact zeta plus self-adjointness is therefore not enough when the credits belong to distinct operators.

The smallest admissible next theorem must construct a source-derived single operator whose complete domain, spectral type, arithmetic return trace, and determinant are proved together. Its spectral type must be audited before any prime-power or completed-$\xi$ promotion.

# Reproducibility and declarations {#reproducibility-and-declarations .unnumbered}

#### Data and code availability.

All source-lock notes, local-source hashes, exact Python controls, tests, generated ledgers, manifests, TikZ source, bibliography, and manuscript source are included in . No external target dataset was created or analyzed.

#### Ethics statement.

This theoretical and deterministic computational study involves no human participants, animals, personal data, or intervention. Institutional ethics review was not required.

#### CRediT authorship contribution statement.

Liang Wang: Conceptualization, Methodology, Formal analysis, Investigation, Software, Validation, Data curation, Visualization, Writing---original draft, and Writing---review and editing.

#### Funding.

No project-specific external funding source was declared.

#### Conflict of interest.

The author declares no financial or non-financial conflict of interest.

#### AI-assistance disclosure.

OpenAI Codex assisted with source triage, deterministic implementation, source-to-claim auditing, adversarial proof checking, native TikZ preparation, and manuscript drafting. No generative system is credited as an author. The named author is responsible for source verification, mathematical claims, artifact release, and the final text.

# Typed artifact map

  Relative path   Role
  --------------- ----------------------------------------------------------------
  Relative path   Role
                  frozen question, exclusions, and route scope
                  source identities, hashes, locators, and convention boundaries
                  complete exact theorem and adversarial-control proofs
                  manuscript claim boundary
                  exact degree, trace, spectrum-witness, and divisor controls
                  ten deterministic unit tests
                  one-command artifact regeneration
                  typed owner and Route certificate
                  generated artifact hashes
