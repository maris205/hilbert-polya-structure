---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-darboux-halphen-modular-dynamics-route-a"
canonical_tex: "henon_dynamics/henon_darboux_halphen_modular_dynamics_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_darboux_halphen_modular_dynamics_route_a/paper/main.pdf"
source_sha256: "85f40649c2eeb709880d30a965dd305335486dfcc2593a45560bef236aa93cb8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Convention-Closed Darboux--Halphen Atlas: Theta Series, Modular Covariance, and Collision Strata

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_darboux_halphen_modular_dynamics_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_darboux_halphen_modular_dynamics_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_darboux_halphen_modular_dynamics_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_darboux_halphen_modular_dynamics_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We lock a polynomial, nome, and theta convention for the Darboux--Halphen system and prove that the logarithmic derivatives of the three Jacobi theta constants solve it. Their exact series also give an Eisenstein divisor-sum bridge. \>0 We prove the affine weight-two covariance, its modular-generator permutations, the Chazy reduction, and discriminant transport. \>1 We close every pair-collision branch, including coordinate-axis equilibria, and state the full cusp/pole and Route-A boundary.
author:
- 'Route-A source-local certificate HCS-C320'
date: 3 September 2026
title: |
  A Convention-Closed Darboux--Halphen Atlas:\
  Theta Series, Modular Covariance, and Collision Strata
```

## Markdown 正文

trailerid \[\<C3202026090300000000000000000000\>\<C3202026090300000000000000000000\>\]

# Polynomial convention and theta/q-series lock

Let a prime mean $\mathrm d/\mathrm d\tau$ and fix $$\label{eq:DH}
 x_1'=x_2x_3-x_1(x_2+x_3),\quad
 x_2'=x_3x_1-x_2(x_3+x_1),\quad
 x_3'=x_1x_2-x_3(x_1+x_2).$$ For $\tau\in\mathbb H$, set $Q=e^{\pi\mathrm i\tau}$ and use theta constants with this nome. Define $$\label{eq:seed}
 (x_1,x_2,x_3)=-2\frac{\mathrm d}{\mathrm d\tau}
 (\log\vartheta_2,\log\vartheta_3,\log\vartheta_4).$$

[\[thm:theta\]]{#thm:theta label="thm:theta"} The triple [\[eq:seed\]](#eq:seed){reference-type="eqref" reference="eq:seed"} solves [\[eq:DH\]](#eq:DH){reference-type="eqref" reference="eq:DH"}. Put $D=Q\,\mathrm d/\mathrm dQ$ and $X_j=x_j/(\pi\mathrm i)$. Then $DX_1=X_2X_3-X_1(X_2+X_3)$, cyclically, and $$\begin{aligned}
\vartheta_2&=2Q^{1/4}\sum_{m\geq0}Q^{m(m+1)},\nonumber\\
\vartheta_3&=1+2\sum_{m\geq1}Q^{m^2},\qquad
\vartheta_4=1+2\sum_{m\geq1}(-1)^mQ^{m^2}.
\label{eq:theta-series}\end{aligned}$$ In particular $X(0)=(-1/2,0,0)$. Moreover $$\label{eq:E2}
 X_1+X_2+X_3=-\frac12E_2(\tau)
 =-\frac12+12\sum_{n\geq1}\sigma_1(n)Q^{2n}.$$

Jacobi's triple products give [\[eq:theta-series\]](#eq:theta-series){reference-type="eqref" reference="eq:theta-series"}. Their logarithmic derivatives converge normally on compact subsets of $|Q|<1$. The standard theta derivative identities are $$\begin{aligned}
 \frac1{\pi\mathrm i}(\log\vartheta_2)'&=\frac1{12}
 (E_2+\vartheta_3^4+\vartheta_4^4),\\
 \frac1{\pi\mathrm i}(\log\vartheta_3)'&=\frac1{12}
 (E_2+\vartheta_2^4-\vartheta_4^4),\\
 \frac1{\pi\mathrm i}(\log\vartheta_4)'&=\frac1{12}
 (E_2-\vartheta_2^4-\vartheta_3^4).\end{aligned}$$ Substitution, using $\vartheta_3^4=\vartheta_2^4+\vartheta_4^4$, $$E_4=\tfrac12(\vartheta_2^8+\vartheta_3^8+\vartheta_4^8),\qquad
 DE_2=\tfrac16(E_2^2-E_4)$$ for the present square-root nome $Q$, reduces each residual in [\[eq:DH\]](#eq:DH){reference-type="eqref" reference="eq:DH"} to zero. Since $\mathrm d/\mathrm d\tau=\pi\mathrm iD$, the scaled polynomial law follows without an omitted factor. Finally $\vartheta_2\vartheta_3\vartheta_4=2\eta^3$ and $(\log\eta)'=\pi\mathrm iE_2/12$ give [\[eq:E2\]](#eq:E2){reference-type="eqref" reference="eq:E2"}; its last equality is the standard $E_2$ series in $Q^2$.

Equation [\[eq:E2\]](#eq:E2){reference-type="eqref" reference="eq:E2"} is an intrinsic quasimodular divisor-sum identity. It is neither a target $\Lambda$-function nor a prime-orbit correspondence.

\>0

# PSL2 covariance, Chazy, and discriminant

Let $F_i(x)$ denote the right side of [\[eq:DH\]](#eq:DH){reference-type="eqref" reference="eq:DH"}. A direct expansion gives, for a common scalar $r$, $$\label{eq:shift}
 F_i(w_1+r,w_2+r,w_3+r)=F_i(w)-2rw_i-r^2.$$

[\[thm:covariance\]]{#thm:covariance label="thm:covariance"} If $\gamma\in\mathrm{SL}_2(\mathbb C)$ has entries $a,b,c,d$ with $ad-bc=1$ and $x$ solves [\[eq:DH\]](#eq:DH){reference-type="eqref" reference="eq:DH"}, then, wherever defined, $$\label{eq:covariance}
 x_i^\gamma(\tau)=(c\tau+d)^{-2}x_i(\gamma\tau)
 +\frac c{c\tau+d}$$ is another solution. For the theta seed, the modular generators act by $$\begin{aligned}
 T:\quad &(x_1,x_2,x_3)(\tau+1)=(x_1,x_3,x_2)(\tau),\label{eq:T}\\
 S:\quad &\tau^{-2}(x_1,x_2,x_3)(-1/\tau)+\tau^{-1}(1,1,1)
 =(x_3,x_2,x_1)(\tau).\label{eq:S}\end{aligned}$$

Write $u=c\tau+d$. Since $(\gamma\tau)'=u^{-2}$, differentiating [\[eq:covariance\]](#eq:covariance){reference-type="eqref" reference="eq:covariance"} gives $u^{-4}F_i(x)-2cu^{-3}x_i-c^2u^{-2}$; equation [\[eq:shift\]](#eq:shift){reference-type="eqref" reference="eq:shift"} gives the same expression on its right side. This proves covariance. The standard theta transformations under $\tau\mapsto\tau+1$ and $\tau\mapsto-1/\tau$, followed by logarithmic differentiation, give [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"}--[\[eq:S\]](#eq:S){reference-type="eqref" reference="eq:S"}; constant eighth-root multipliers disappear.

[\[thm:chazy\]]{#thm:chazy label="thm:chazy"} For $$S=x_1+x_2+x_3,\qquad
 \Delta=(x_1-x_2)(x_2-x_3)(x_3-x_1),$$ every solution satisfies $$\label{eq:chazy}
 S'''=-4SS''+6(S')^2,
 \qquad \Delta'=-2S\Delta.$$ Consequently $\Delta=0$ is an invariant union of collision strata.

Summing [\[eq:DH\]](#eq:DH){reference-type="eqref" reference="eq:DH"} first gives $S'=-(x_1x_2+x_2x_3+x_3x_1)$. Differentiate twice and eliminate every $x_i'$ with [\[eq:DH\]](#eq:DH){reference-type="eqref" reference="eq:DH"}; collecting symmetric monomials yields the first identity. Subtracting two cyclic equations gives, for example, $(x_1-x_2)'=-2x_3(x_1-x_2)$. Multiplication of the three corresponding relations proves the second identity and invariance.

\>1

# Collision strata, cusp/poles, and audit

[\[thm:collision\]]{#thm:collision label="thm:collision"} On $x_1=x_2=a$, $x_3=b$, the reduced equations are $$\label{eq:reduced}
 a'=-a^2,\qquad b'=a^2-2ab.$$ For $c,C\in\mathbb C$, every local solution with $a$ not identically zero is, on a domain where $\tau\ne c$, $$\label{eq:collision}
 a=\frac1{\tau-c},\qquad
 b=\frac1{\tau-c}+\frac C{(\tau-c)^2}.$$ The layer $C=0$ is the nonzero fully diagonal Riccati solution. If $a\equiv0$, then $b\equiv B$ is arbitrary for $B\in\mathbb C$, giving the equilibrium axis $(0,0,B)$. Cyclic permutation gives all collision strata and all three coordinate axes; the axes meet at the origin.

Substitution gives [\[eq:reduced\]](#eq:reduced){reference-type="eqref" reference="eq:reduced"}. If $a$ vanishes once, uniqueness for the polynomial ODE forces $a\equiv0$. Otherwise a Riccati solution is the first formula in [\[eq:collision\]](#eq:collision){reference-type="eqref" reference="eq:collision"}; its second equation is linear and integration gives the stated $C$. If $a=0$, the second equation says $b'=0$. Cyclic symmetry completes the atlas.

The theta products are holomorphic and nonvanishing for $\tau\in\mathbb H$, so the theta chart is regular there. The face $Q=0$ is the cusp limit $X=(-1/2,0,0)$, not an interior time. In [\[eq:covariance\]](#eq:covariance){reference-type="eqref" reference="eq:covariance"}, $c\tau+d=0$ is a chart pole. Theta-zero logarithmic-derivative poles are only a risk after analytic continuation outside $\mathbb H$. The invariant collision union, its reciprocal diagonal, and its coordinate-axis equilibria are separate declared layers; no exhaustive classification of all meromorphic continuations is claimed.

#### Finite evidence.

Exact evidence contains 129 coefficient rows through $Q^{128}$, six high-precision theta/ODE/$S,T$ rows, 18 reciprocal collision rows, and 15 axis equilibria: 1,705 scalar leaves. A producer-independent Jacobi-product checker performs 1,945 checks, SymPy closes 345 identities, isolated replay is byte exact, and 56 repaired-digest/parser attacks fail. Sampling is a convention lock; the displayed derivations prove the analytic statements.

#### Registry collision boundary.

C186 is the Euler-top Jacobi action--angle flow and C244 the spherical pendulum's elliptic/focus--focus atlas. C17--C18 concern modular scattering clocks and open traces; C35 is adelic Hénon--theta scattering. None is the present classical three-component modular differential system.

#### Route-A result and nonclaims.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the tuple is $$\begin{aligned}
 (&\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},\mathrm{A1\_FAIL},
 \mathrm{A2\_FAIL},\\
 &\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_FAIL}).
 \end{aligned}$$ The source owns theta/$E_2$ divisor sums and strong analytic covariance, but no target-prime local data, isolated primitive ledger, Euler product, target functional equation, Weil compression, natural self-adjoint quantization, or target-zero match. Route A is rejected and Route B remains locked. No root number, automorphy transfer, or Hilbert--Pólya operator is claimed.

#### AI use.

A generative language model assisted drafting and code scaffolding. The displayed derivations, independent reconstructions, hostile tests, and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 Y. Ohyama, "Differential Relations of Theta Functions," *Osaka Journal of Mathematics* 32 (1995), 431--450. Repository copy: [ocu-omu.repo.nii.ac.jp](https://ocu-omu.repo.nii.ac.jp/record/2009467/files/111F0000002-03202-12.pdf).

J. A. Cruz Morales, H. Movasati, Y. Nikdelan, R. Roychowdhury, and M. A. C. Torres, "Manifold Ways to Darboux--Halphen System," *SIGMA* 14 (2018), 003. DOI: [10.3842/SIGMA.2018.003](https://doi.org/10.3842/SIGMA.2018.003).

J. Harnad and J. McKay, "Modular Invariants and Generalized Halphen Systems," arXiv: [solv-int/9902012](https://arxiv.org/abs/solv-int/9902012).
