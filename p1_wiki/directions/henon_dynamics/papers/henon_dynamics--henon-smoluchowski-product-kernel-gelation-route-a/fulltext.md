---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-smoluchowski-product-kernel-gelation-route-a"
canonical_tex: "henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/paper/main.pdf"
source_sha256: "ab73bf9e26f501949af1f22cb5cb153d21a8ac0c4a96812dc6518c21844c9588"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Product-Kernel Gelation and the Smoluchowski--Flory Postgel Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a convention-complete solution atlas for monodisperse discrete coagulation with multiplicative kernel. Cayley tree coefficients close every cluster concentration before gelation, while rooted and unrooted tree functions give the mass and number generating functions. The second moment diverges at $t=1$, where the concentrations have the critical $k^{-5/2}$ tail. We then resolve a postgel ambiguity explicitly. With the Smoluchowski finite-sol loss, one Stockmayer continuation freezes the critical shape and has sol mass $1/t$. With gel-reactive Flory loss, the pregel coefficient formula continues and has sol mass $q=-W_0(-te^{-t})/t$. The two families agree at $t=1$ but direct substitution shows that they solve different equations afterward. No universal weak-solution uniqueness is claimed. Exact independent reconstruction, symbolic identities, canonical replay, and hostile mutations audit the theorem.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Exact Product-Kernel Gelation and the Smoluchowski--Flory Postgel Boundary'
```

## Markdown 正文

suppressoptionalinfo 611

# Frozen kinetic convention

For $k\ge1$, set $$\dot c_k=\frac12\sum_{i+j=k}ijc_ic_j-kc_kM_1(t),
 \qquad M_q(t)=\sum_{k\ge1}k^q c_k(t),                 \tag{1}$$ with $c_1(0)=1$ and $c_k(0)=0$ for $k>1$. Thus $K(i,j)=ij$, the unordered gain has factor $1/2$, and (1) uses only finite-cluster mass in its loss. A different gel-reactive loss will be introduced only after its convention is named.

Define the rooted and unrooted labelled-tree series $$T(u)=\sum_{k\ge1}\frac{k^{k-1}}{k!}u^k,\qquad
 U(u)=\sum_{k\ge1}\frac{k^{k-2}}{k!}u^k.              \tag{2}$$ Cayley's formula and Lagrange inversion give $T=ue^T$, $U=T-T^2/2$, and $uU'(u)=T(u)$.

[\[thm:pre\]]{#thm:pre label="thm:pre"} For $0\le t\le1$, $$c_k(t)=a_kt^{k-1}e^{-kt},\qquad
 a_k=\frac{k^{k-2}}{k!}.                               \tag{3}$$ If $u=tze^{-t}$, the mass and number generating functions are $$G(z,t)=\sum_{k\ge1}kc_kz^k=\frac{T(u)}t,\qquad
 C(z,t)=\sum_{k\ge1}c_kz^k=\frac{U(u)}t,              \tag{4}$$ as formal power series in $z$, and analytically on the principal convergence disk (in particular $0\le z\le1$), with continuous $t=0$ values. For $t<1$, $$M_0=1-\frac t2,\quad M_1=1,\quad
 M_2=\frac1{1-t},\quad M_3=\frac1{(1-t)^3}.            \tag{5}$$ At $t_g=1$, $$c_k(1)\sim\frac1{\sqrt{2\pi}}k^{-5/2},               \tag{6}$$ so $M_2$ diverges. For fixed $0<t<1$, $$c_k(t)\sim\frac{k^{-5/2}}{\sqrt{2\pi}\,t}
              [te^{1-t}]^k.                            \tag{7}$$

Coefficient extraction from $T=ue^T$, or the standard labelled-tree edge decomposition, gives $$(k-1)a_k=\frac12\sum_{i+j=k}ij a_i a_j.               \tag{8}$$ At $t=0$, equation (3) means its continuous limit: $c_1=1$ and $c_k=0$ for $k>1$, so no $0^0$ convention is left implicit. Differentiating (3), using (8), and imposing $M_1=1$ proves (1) coefficient by coefficient. Substitution in (2) gives (4). On the branch reached from zero, $T(te^{-t})=t$ for $t\le1$, so $U=t-t^2/2$. Applying $z\partial_z$ to $G$ and using $uT'(u)=T/(1-T)$ gives (5); equivalently $\dot M_2=M_2^2$ and $\dot M_3=3M_2M_3$. Stirling's formula applied to (3) gives (6) and (7), and (6) makes $\sum k^2c_k$ divergent.

\>0

# Two inequivalent postgel closures

[\[prop:s\]]{#prop:s label="prop:s"} For equation (1), one explicit continuation for $t\ge1$ is $$c_k^{\mathrm S}(t)=a_k\frac{e^{-k}}t.                 \tag{9}$$ It is continuous coefficientwise at $t=1$ and has $$M_0^{\mathrm S}=\frac1{2t},\qquad
 M_1^{\mathrm S}=\frac1t,\qquad M_2^{\mathrm S}=\infty. \tag{10}$$

At the critical argument, $T(e^{-1})=1$ and $U(e^{-1})=1/2$, giving (10). By (8), the gain in (1) is $(k-1)c_k^{\mathrm S}/t$; the loss is $kc_k^{\mathrm S}M_1^{\mathrm S}=kc_k^{\mathrm S}/t$. Their difference is $-c_k^{\mathrm S}/t=\dot c_k^{\mathrm S}$. The critical tail (6), merely scaled by $1/t$, makes $M_2$ infinite.

Now change the postgel equation: keep the same gain but replace its loss by $-kc_kM_1(0)=-kc_k$. This is the gel-reactive Flory convention; finite clusters may continue to collide with the gel.

[\[prop:f\]]{#prop:f label="prop:f"} For the Flory loss and $t\ge1$, $$c_k^{\mathrm F}(t)=a_kt^{k-1}e^{-kt}.                 \tag{11}$$ For $t>1$, let $$r=-W_0(-te^{-t})\in(0,1),\qquad q=r/t.                \tag{12}$$ Then $q=e^{-t(1-q)}$ and $$M_0^{\mathrm F}=q-\frac t2q^2,\quad M_1^{\mathrm F}=q,\quad
 M_2^{\mathrm F}=\frac q{1-r},\quad
 M_3^{\mathrm F}=\frac q{(1-r)^3}.                    \tag{13}$$

Equation (8) gives gain $(k-1)c_k^{\mathrm F}/t$; Flory loss is $kc_k^{\mathrm F}$. Their difference equals $[(k-1)/t-k]c_k^{\mathrm F}=\dot c_k^{\mathrm F}$. The principal Lambert branch solves $re^{-r}=te^{-t}$ and selects $r<1$, yielding the fixed-point equation for $q$. Equations (4) and $U=T-T^2/2$, evaluated at $T=r$, give $M_0$ and $M_1$. Two applications of $z\partial_z$ give the remaining moments.

The same fixed-point equation also has the formal root $q=1$: for $t>1$ it comes from $W_{-1}(-te^{-t})=-t$. The coefficient generating series selects the principal branch $W_0$, hence $r<1$ and $q<1$; the $W_{-1}$ root is not the finite-cluster mass of (11).

Equations (9) and (11) agree at $t=1$. For every $t>1$, however, their loss masses are respectively $1/t$ and $1$, and their sol masses are respectively $1/t$ and $q$. Agreement at one boundary therefore cannot identify the two dynamical closures. We verify these explicit continuations but make no claim of uniqueness among all weak postgel solutions.

# Source and collision boundary

McLeod [@mcleod1; @mcleod2] is a primary owner for the infinite nonlinear system and its classical exact analysis. Ziff--Stell [@ziffstell] treat polymer gelation conventions; Normand--Zambotti [@nz] and Norris [@norris] delimit global solution and uniqueness questions. We claim no priority for the tree law, gel exponent, or named postgel branches. The local contribution is an executable convention firewall.

No earlier local paper owns this kinetic system. Linear branching and the finite Kingman coalescent have different states and generators; neither has the concentration-mass gel boundary above.

\>1

# Audit and strict Route-A boundary

The canonical evidence has 40 exact recurrence rows, five pregel/critical rows, four rows for each postgel closure, and five critical-tail controls. Each time row checks the first 20 cluster equations at 90 digits. A producer-independent checker makes 696 assertions; SymPy reconstructs 29 generic identities; clean replay is byte identical; and 28 of 28 stale-hash, repaired-hash, nested-schema, branch, provenance and scope mutations are rejected. These finite rows audit exact proofs; they do not establish an infinite tail by regression.

The Route-A tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_FAIL},\mathtt{A2\_FAIL},
  \mathtt{A3\_FAIL},\mathtt{A4\_FAIL}),$$ with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. Cluster labels have no rational-prime semantics; coagulation histories are not a primitive periodic-orbit ledger; the tree series are not a target zeta/Fredholm determinant; and no target analytic structure or natural unitary lift is constructed.

9 J. B. McLeod, *On an Infinite Set of Non-Linear Differential Equations*, Quarterly Journal of Mathematics 13 (1962), 119--128. DOI: 10.1093/qmath/13.1.119. J. B. McLeod, *On an Infinite Set of Non-Linear Differential Equations, II*, Quarterly Journal of Mathematics 13 (1962), 193--205. DOI: 10.1093/qmath/13.1.193. R. M. Ziff and G. Stell, *Kinetics of polymer gelation*, Journal of Chemical Physics 73(7) (1980), 3492--3499. DOI: 10.1063/1.440502. C. Normand and L. Zambotti, *Uniqueness of post-gelation solutions of a class of coagulation equations*, Annales de l'Institut Henri Poincaré C 28(2) (2011), 189--215. DOI: 10.1016/j.anihpc.2010.10.005. J. R. Norris, *Smoluchowski's coagulation equation: uniqueness, nonuniqueness and a hydrodynamic limit for the stochastic coalescent*, Annals of Applied Probability 9(1) (1999), 78--109. DOI: 10.1214/aoap/1029962598.

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, target-zero, universal postgel-uniqueness, or Hilbert--Pólya claim. **Data and code.** The exact coefficient ledger and all audits accompany HCS-C228. **AI-use disclosure.** Generative tools assisted drafting and code generation; the released internal chain checks the displayed formulas and metadata. This is not external peer review.
