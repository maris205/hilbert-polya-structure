---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--24-hamiltonian-period-two-selector-exchange"
canonical_tex: "symplectic_map/papers/24-hamiltonian-period-two-selector-exchange/paper/main.tex"
canonical_pdf: "symplectic_map/papers/24-hamiltonian-period-two-selector-exchange/paper/main.pdf"
source_sha256: "0e15bba5b8ae9438049f595950c6b0793ab2e37757a4e283e27eb3bcfac9890f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/24-hamiltonian-period-two-selector-exchange>)
- [规范 TeX](<../../../../../symplectic_map/papers/24-hamiltonian-period-two-selector-exchange/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/24-hamiltonian-period-two-selector-exchange/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/24-hamiltonian-period-two-selector-exchange/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/24-hamiltonian-period-two-selector-exchange/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Over any field $\mathbb{K}$ of characteristic zero, let $m\geq2$, $s\geq1$, and $A,B,C,D\in\mathbb{K}^\times$, and define $V_m=Aq_1^m q_2^2+Bq_1q_2^{2m}$, $W_{m,s}=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1}$, $S(\boldsymbol{q},\boldsymbol{p})=(\boldsymbol{q},\boldsymbol{p}+\nabla V_m(\boldsymbol{q}))$, $T(\boldsymbol{q},\boldsymbol{p})=(\boldsymbol{q}+\nabla W_{m,s}(\boldsymbol{p}),\boldsymbol{p})$, and $F_{m,s}=T\circ S$. Starting from ordinary total degree, its selected support rows exchange strictly with period two between the open chambers $r=u_1/u_2<2$ and $r>2$; no assertion is made on the wall $r=2$. With $H=m^2(2m+1)^2$ and $L=2m(m+1)$, the exact two-step monodromy gives $\lambda_1(F_{m,s})=sm(2m+1)$ and the stride-two recurrence $d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n$. The contribution is bounded to this explicit family: the proof establishes true temporal carry, no-cancellation/top-form survival, and $q_1$-visibility of actual degrees, and obtains the exact parity laws; we make no priority claim.
author:
- Anonymous
bibliography:
- references.bib
title: 'Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears'
```

## Markdown 正文

# Introduction, theorem preview, and bounded positioning {#sec:introduction}

Degree growth for a polynomial self-map is elementary to define but often subtle to transport through iteration. If leading terms are selected by weighted degree, then a tie wall can change the active monomial. A matrix calculation made on the wrong side of that wall may describe a formal tropical orbit while missing the degree of the actual polynomial iterate. There are three logically separate questions. Which support row is selected? Does that row dominate coordinates carried from the preceding half-step? And does a coordinate attaining the formal degree really survive addition and remain visible in the total degree of the full map? The example studied here is designed so that none of these questions can be suppressed: the ordinary seed crosses a common wall on every iterate.

General degree-growth and dynamical-degree viewpoints motivate the language but do not settle these local questions; see Bellon--Viallet for algebraic entropy context, Hasselblatt--Propp for instructive behavior of monomial-map degree sequences, and Dang--Favre for spectral interpretations of dynamical degrees [@BellonVialletAlgebraicEntropy; @HasselblattProppMonomialDegreeGrowth; @DangFavreSpectralInterpretations]. Polynomial symplectomorphisms form a broader class in which the present two shears sit [@JaneczkoJelonekPolynomialSymplectomorphisms]. These references organize the questions; every calculation used below is proved directly for the displayed family.

Periodic piecewise-linear behavior also occurs in cluster settings. Symplectic cluster maps, cluster Poisson structures, and sign-stable mutation loops provide nearby mechanisms in a different birational formalism [@FordyHoneSymplecticCluster; @FordyHoneClusterPoisson; @IshibashiKanoSignStableEntropy]. Accordingly, periodic switching or a spectral formula by itself is not the point of the result. The work below is the simultaneous verification of a strict common-wall exchange, true-polynomial temporal carry, coefficient- uniform top-form survival, and coordinate visibility for one explicit Hamiltonian product-shear family.

Weighted-degree and affine-triangular results give another useful comparison class [@BlancVanSantenAffineTriangular; @ShaoSunDimensionFour]. We use them only to delimit the question: no affine-triangular realization or noncollision statement is inferred from those sources, and no bibliography item is invoked as proof of a local identity. In particular, the spectral radius calculated here is obtained from the explicit two-step matrix after the polynomial degree transport has been established.

Write $\deg G$ for the maximum ordinary total degree of the coordinate polynomials of a polynomial map $G$, and put $$\lambda_1(G)=\lim_{n\to\infty}(\deg G^n)^{1/n}$$ whenever the limit exists. For the maps below the closed formulas prove the existence of this limit. We use column vectors, and a matrix written on the left acts after a matrix written on the right.

[\[thm:main\]]{#thm:main label="thm:main"} Let $\mathbb{K}$ be any field of characteristic zero. Let $m\geq2$ and $s\geq1$ be integers, and let $A,B,C,D\in\mathbb{K}^\times$. Define $$V_m=Aq_1^m q_2^2+Bq_1q_2^{2m},\qquad
W_{m,s}=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},$$ $$S(\boldsymbol{q},\boldsymbol{p})=(\boldsymbol{q},\boldsymbol{p}+\nabla V_m(\boldsymbol{q})),\qquad
T(\boldsymbol{q},\boldsymbol{p})=(\boldsymbol{q}+\nabla W_{m,s}(\boldsymbol{p}),\boldsymbol{p}),
\qquad F_{m,s}=T\circ S.$$ Then the following statements hold.

1.  The maps $S,T,F_{m,s}$ are polynomial automorphisms of $\mathbb{K}^4$, and each preserves $\mathrm{d}q_1\wedge\mathrm{d}p_1+
    \mathrm{d}q_2\wedge\mathrm{d}p_2$.

2.  For the ordinary seed $\boldsymbol{u}_0=(1,1)^{\mathsf{T}}$, the two common support selectors alternate strictly as $A_{-},A_{+},A_{-},A_{+},\ldots$. No iterate lies on the wall $u_1=2u_2$. Both half-step carry comparisons are strict, and the formal degrees are true degrees for every choice of the four nonzero coefficients.

3.  With $B_m=\mathop{\mathrm{diag}}(2m+1,m)$, $C_{-}=sB_mA_{-}$, $C_{+}=sB_mA_{+}$, and $$P_m=(B_mA_{+})(B_mA_{-}),$$ the complete-step position-degree vectors satisfy $$\boldsymbol{u}_{2j}=(s^2P_m)^j(1,1)^{\mathsf{T}},\qquad
    \boldsymbol{u}_{2j+1}=sB_mA_{-}(s^2P_m)^j(1,1)^{\mathsf{T}}.$$ For every $n\geq1$, the first position coordinate is strictly larger in degree than the other three coordinates. Hence $d_n:=\deg(F_{m,s}^n)=u_{n,1}$, while $d_0=1$.

4.  The two eigenvalues of $P_m$ are $$H=m^2(2m+1)^2,\qquad L=2m(m+1),$$ and $H>L>0$. Consequently $$\lambda_1(F_{m,s})=sm(2m+1).$$ The sequence $(d_n)$ obeys $$d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n$$ with $$\begin{aligned}
    d_0&=1,&d_1&=2m(2m+1)s,\\
    d_2&=2m(m+1)(2m-1)(2m+1)s^2,&
    d_3&=8m^4(m+1)(2m+1)s^3.\end{aligned}$$

5.  The wall gaps are exactly $$u_{2j,1}-2u_{2j,2}=-(s^2L)^j,\qquad
    u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.$$ Writing $\Delta_m=4m^3+4m^2-m-2$, the even vectors and both parity degree laws are $$\begin{aligned}
    \boldsymbol{u}_{2j}=\frac{s^{2j}}{\Delta_m}\bigg[&
    2(m+1)(2m^2-1)H^j\binom{2}{1}
    +L^j\binom{-(2m+1)(2m^2+m-2)}{m}\bigg],\\
    d_{2j}=\frac{s^{2j}}{\Delta_m}\big[&
    4(m+1)(2m^2-1)H^j
    -(2m+1)(2m^2+m-2)L^j\big],\\
    d_{2j+1}=\frac{2m(2m+1)s^{2j+1}}{\Delta_m}\big[&
    2(m+1)(2m^2-1)H^j+mL^j\big].\end{aligned}$$ Although these expressions have a denominator, their values are integers; this follows from the integer matrix formulas, equivalently from the integer recurrence and initial data.

The five conclusions of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} are coupled, but no later conclusion can be used to justify an earlier one. Symplecticity is a literal Jacobian fact and says nothing by itself about degree. The selector exchange is a statement about competing linear support rows, not yet about sums of polynomials. Temporal carry and leading-form survival promote those rows to true coordinate degrees. Visibility then promotes one coordinate degree to the degree of the whole map. Only at that point can the monodromy spectrum be interpreted dynamically. This order explains why the proof contains more than the matrix multiplication in Section [5](#sec:visibility){reference-type="ref" reference="sec:visibility"}.

There are two complementary strictness certificates. The rational branch maps show locally that each open chamber is sent into the other. The signed wall functional later gives a closed expression for the unnormalized gap at every iterate. The first certificate discovers and inductively proves the itinerary; the second proves that diagonalization has not silently placed an iterate on the boundary. Their agreement is also a symbolic consistency check on the temporal order of $C_{-}$ and $C_{+}$.

The coefficient statement is stronger than a positive-coefficient example but narrower than a perturbation theorem. Weighted support differences do not see coefficient size, yet polynomial cancellation can still matter when two sources tie. Here the orbit is strictly off the wall, each selected top source is unique, and every selected factor is nonzero in a domain. Those facts are what allow all $(A,B,C,D)\in(\mathbb{K}^\times)^4$. They do not allow a coefficient to vanish or an additional support monomial to be inserted.

The parity formulas have a similarly precise role. The integer matrix laws are primary: they determine degrees, signs of wall gaps, and integrality. Diagonalization then resolves those laws into $H^j$ and $L^j$ components. It is therefore harmless that the closed forms display the denominator $\Delta_m$; the numerator is divisible because it represents an entry of an integer matrix power. No arithmetic cancellation assumption is placed on $m$ or $s$.

The proof is deliberately separated into its necessary layers. Section [2](#sec:family){reference-type="ref" reference="sec:family"} establishes the literal polynomial and symplectic formulas. Section [3](#sec:selector){reference-type="ref" reference="sec:selector"} proves the support selection and the strict period-two projective itinerary. Section [4](#sec:carry){reference-type="ref" reference="sec:carry"} turns that itinerary into a coefficient-uniform statement about actual polynomial iterates. Section [5](#sec:visibility){reference-type="ref" reference="sec:visibility"} proves visibility before using the monodromy. Section [6](#sec:recurrence){reference-type="ref" reference="sec:recurrence"} derives the recurrence, signed wall gaps, and closed forms. Section [7](#sec:structural){reference-type="ref" reference="sec:structural"} states the bounded structural criterion and the conditional technical lemma. The final section records the precise boundary of every assertion.

# Family, inverses, symplecticity, and support rows {#sec:family}

## Literal phases and inverse maps

Set $\boldsymbol{q}=(q_1,q_2)^{\mathsf{T}}$ and $\boldsymbol{p}=(p_1,p_2)^{\mathsf{T}}$. Differentiating the two Hamiltonians gives $$\begin{aligned}
\frac{\partial V_m}{\partial q_1}
&=mAq_1^{m-1}q_2^2+Bq_2^{2m},
&
\frac{\partial V_m}{\partial q_2}
&=2Aq_1^mq_2+2mBq_1q_2^{2m-1},
\label{eq:grad-v}\\
\frac{\partial W_{m,s}}{\partial p_1}
&=\bigl(s(2m+1)+1\bigr)C p_1^{s(2m+1)},
&
\frac{\partial W_{m,s}}{\partial p_2}
&=(sm+1)D p_2^{sm}.
\label{eq:grad-w}\end{aligned}$$ Every displayed scalar is nonzero in $\mathbb{K}$: this is the first place where characteristic zero is essential. It is also why the coefficient hypothesis is $A,B,C,D\neq0$, rather than a sign or positivity hypothesis.

The order of the phases is fixed. The map $S$ is applied first, so the arguments of $\nabla W_{m,s}$ in the second phase are the updated momenta. Explicitly, $$\begin{aligned}
p_1'&=p_1+mAq_1^{m-1}q_2^2+Bq_2^{2m},\notag\\
p_2'&=p_2+2Aq_1^mq_2+2mBq_1q_2^{2m-1},\notag\\
q_1'&=q_1+\bigl(s(2m+1)+1\bigr)C(p_1')^{s(2m+1)},\notag\\
q_2'&=q_2+(sm+1)D(p_2')^{sm}.
\label{eq:complete-coordinate-map}\end{aligned}$$ The block-triangular dependence in this display fixes more than the inverse order. If $$\widetilde{\boldsymbol{p}}=\boldsymbol{p}+\nabla V_m(\boldsymbol{q}),$$ then the complete map can be read without suppressing its intermediate state as $$F_{m,s}(\boldsymbol{q},\boldsymbol{p})
=\bigl(\boldsymbol{q}+\nabla W_{m,s}(\widetilde{\boldsymbol{p}}),
       \widetilde{\boldsymbol{p}}\bigr).
\label{eq:intermediate-state}$$ Thus the first phase leaves both position arguments unchanged while adding to the old momenta, and the second phase evaluates its pure powers at those updated momenta while carrying the old positions. In particular, $\nabla W_{m,s}$ is never evaluated at the pre-$S$ momentum. This literal dependence is the source of the two later temporal comparisons: a selected term of $\nabla V_m$ must first beat a carried momentum, and its pure power must then beat a carried position. Recording the intermediate state prevents either comparison from being hidden inside the notation $T\circ S$.

The subtraction formulas $$S^{-1}(\boldsymbol{q},\boldsymbol{p})=(\boldsymbol{q},\boldsymbol{p}-\nabla V_m(\boldsymbol{q})),
\qquad
T^{-1}(\boldsymbol{q},\boldsymbol{p})=(\boldsymbol{q}-\nabla W_{m,s}(\boldsymbol{p}),\boldsymbol{p})$$ are polynomial, and $$F_{m,s}^{-1}=S^{-1}\circ T^{-1}.$$ Thus no rational inversion or algebraic closure of $\mathbb{K}$ is involved.

## Direct symplectic calculation

In the coordinate order $(q_1,q_2,p_1,p_2)$, let $$\Omega=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix}.$$ Writing $H_V$ and $H_W$ for the two Hessian matrices evaluated at the relevant variables, the Jacobians are $$J_S=\begin{pmatrix}I_2&0\\H_V&I_2\end{pmatrix},
\qquad
J_T=\begin{pmatrix}I_2&H_W\\0&I_2\end{pmatrix}.$$ For reference, symmetry is visible entry by entry: $$H_V=\begin{pmatrix}
m(m-1)Aq_1^{m-2}q_2^2
&2mAq_1^{m-1}q_2+2mBq_2^{2m-1}\\
2mAq_1^{m-1}q_2+2mBq_2^{2m-1}
&2Aq_1^m+2m(2m-1)Bq_1q_2^{2m-2}
\end{pmatrix},
\label{eq:hessian-v}$$ while $$H_W=\begin{pmatrix}
s(2m+1)(s(2m+1)+1)Cp_1^{s(2m+1)-1}&0\\
0&sm(sm+1)Dp_2^{sm-1}
\end{pmatrix}.
\label{eq:hessian-w}$$ The off-diagonal equality in [\[eq:hessian-v\]](#eq:hessian-v){reference-type="eqref" reference="eq:hessian-v"} is simply equality of the two mixed partial derivatives; [\[eq:hessian-w\]](#eq:hessian-w){reference-type="eqref" reference="eq:hessian-w"} is diagonal because the two momentum variables are separated in $W_{m,s}$. These literal expressions also show that the Jacobian calculation is valid for arbitrary coefficient values in $\mathbb{K}^\times$, without a positivity convention. Both Hessians are symmetric over $\mathbb{K}$. Direct block multiplication gives $$\begin{aligned}
J_S^{\mathsf{T}}\Omega J_S
&=\begin{pmatrix}I_2&H_V\\0&I_2\end{pmatrix}
  \begin{pmatrix}H_V&I_2\\-I_2&0\end{pmatrix}
=\begin{pmatrix}H_V-H_V^{\mathsf{T}}&I_2\\-I_2&0\end{pmatrix}
=\Omega,\\
J_T^{\mathsf{T}}\Omega J_T
&=\begin{pmatrix}I_2&0\\H_W&I_2\end{pmatrix}
  \begin{pmatrix}0&I_2\\-I_2&-H_W\end{pmatrix}
=\begin{pmatrix}0&I_2\\-I_2&H_W^{\mathsf{T}}-H_W\end{pmatrix}
=\Omega.\end{aligned}$$ The signs in this calculation can also be checked once in a generic shear. For an arbitrary square matrix $H$, set $$L_H=\begin{pmatrix}I_2&0\\H&I_2\end{pmatrix},
\qquad
U_H=\begin{pmatrix}I_2&H\\0&I_2\end{pmatrix}.$$ Then direct multiplication, before any specialization to the displayed potentials, gives $$\begin{aligned}
L_H^{\mathsf{T}}\Omega L_H
&=\begin{pmatrix}H-H^{\mathsf{T}}&I_2\\-I_2&0\end{pmatrix},\\
U_H^{\mathsf{T}}\Omega U_H
&=\begin{pmatrix}0&I_2\\-I_2&H^{\mathsf{T}}-H\end{pmatrix}.\end{aligned}$$ Consequently each triangular shear preserves $\Omega$ exactly when its off-diagonal block is symmetric. Here those blocks are Hessians, so their symmetry is an identity of mixed partials rather than an extra assumption. Both triangular Jacobians also have determinant one. These observations separate the symplectic argument from every later degree comparison: no support selector, coefficient sign, or chamber inequality is needed to prove preservation of the form.

It follows that $J_{F_{m,s}}^{\mathsf{T}}\Omega J_{F_{m,s}}=\Omega$. Equivalently, $F_{m,s}$ preserves $\mathrm{d}q_1\wedge\mathrm{d}p_1+\mathrm{d}q_2\wedge\mathrm{d}p_2$. This proves Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(i) without appealing to a normal-form or generation theorem.

## Support rows before selection

For a positive degree vector $\boldsymbol{u}=(u_1,u_2)^{\mathsf{T}}$, the weighted degree of $q_1^xq_2^y$ is $xu_1+yu_2$. The two terms in each coordinate of $\nabla V_m$ therefore compete by linear rows. Once a row of the first phase is chosen, the pure powers in $\nabla W_{m,s}$ multiply its two output degrees by $s(2m+1)$ and $sm$. After factoring out the common $s$, this is the diagonal matrix $B_m$.

The full selector and branch ledger is recorded in Table [\[tab:selector-ledger\]](#tab:selector-ledger){reference-type="ref" reference="tab:selector-ledger"}. It lists supports, not coefficients; the survival of the corresponding polynomial top forms is proved only after the temporal carry inequalities in Section [4](#sec:carry){reference-type="ref" reference="sec:carry"}.

@\>p0.24Y@ Object & Exact support row, matrix, or identity\
$\partial_{q_1}V_m$, mixed & $(m-1,2)$, from $mAq_1^{m-1}q_2^2$\
$\partial_{q_1}V_m$, pure & $(0,2m)$, from $Bq_2^{2m}$\
$\partial_{q_2}V_m$, mixed & $(m,1)$, from $2Aq_1^mq_2$\
$\partial_{q_2}V_m$, pure & $(1,2m-1)$, from $2mBq_1q_2^{2m-1}$\
$\partial_{p_1}W_{m,s}$, pure & multiplier $s(2m+1)$ on the first selected momentum degree\
$\partial_{p_2}W_{m,s}$, pure & multiplier $sm$ on the second selected momentum degree\
Negative selector & $\displaystyle A_{-}=\begin{pmatrix}0&2m\\1&2m-1\end{pmatrix}$, for $u_1<2u_2$\
Positive selector & $\displaystyle A_{+}=\begin{pmatrix}m-1&2\\m&1\end{pmatrix}$, for $u_1>2u_2$\
Pure-power multiplier & $\displaystyle B_m=\mathop{\mathrm{diag}}(2m+1,m)$ and $C_{-}=sB_mA_{-}$, $C_{+}=sB_mA_{+}$\
Negative branch & $\displaystyle h_m(r)=\frac{2(2m+1)}{r+2m-1}$\
Positive branch & $\displaystyle \ell_m(r)=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}$\
Negative wall gap & $\displaystyle h_m(r)-2=\frac{2(2-r)}{r+2m-1}$\
Positive lower gap & $\displaystyle \ell_m(r)-1=\frac{(m^2-m-1)r+3m+2}{m(mr+1)}$\
Positive wall gap & $\displaystyle 2-\ell_m(r)=\frac{(m+1)(r-2)}{m(mr+1)}$\
Chamber images & $0<r<2\Rightarrow h_m(r)>2$, while $r>2\Rightarrow1<\ell_m(r)<2$; equality with $2$ occurs only at $r=2$\

# Common wall, branch algebra, and strict selector exchange {#sec:selector}

The two gradient coordinates have a common wall for a literal algebraic reason. In the first coordinate of $\nabla V_m$, the mixed row minus the pure row evaluates as $$\begin{aligned}
\bigl((m-1)u_1+2u_2\bigr)-2mu_2
  &=(m-1)(u_1-2u_2).\end{aligned}$$ In the second coordinate the corresponding difference is $$\begin{aligned}
\bigl(mu_1+u_2\bigr)-\bigl(u_1+(2m-1)u_2\bigr)
  &=(m-1)(u_1-2u_2).\end{aligned}$$ Because $m-1>0$, both coordinates select their pure $B$-terms when $u_1<2u_2$, and both select their mixed $A$-terms when $u_1>2u_2$. At $u_1=2u_2$, both pairs tie. Thus the wall is neither a notational convenience nor a chamber included by convention: it is a genuine two-coordinate tie locus.

For positive $u_1,u_2$, put $r=u_1/u_2$. In the negative chamber the selected momentum-degree vector before the pure-power shear is $$\boldsymbol{v}=A_{-}\boldsymbol{u}
=\binom{2mu_2}{u_1+(2m-1)u_2}.
\label{eq:minus-selected-v}$$ After the second phase, the common factor $s$ cancels from the projective ratio and gives $$\frac{(B_m\boldsymbol{v})_1}{(B_m\boldsymbol{v})_2}
=\frac{(2m+1)2m}{m(r+2m-1)}
=h_m(r)=\frac{2(2m+1)}{r+2m-1}.
\label{eq:h-branch}$$ In the positive chamber, $$\boldsymbol{v}=A_{+}\boldsymbol{u}
=\binom{(m-1)u_1+2u_2}{mu_1+u_2},
\label{eq:plus-selected-v}$$ and therefore $$\frac{(B_m\boldsymbol{v})_1}{(B_m\boldsymbol{v})_2}
=\ell_m(r)
=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}.
\label{eq:ell-branch}$$ The corresponding complete-step matrices, including the common factor $s$, are $$\begin{aligned}
C_{-}
&=s\begin{pmatrix}
0&2m(2m+1)\\
m&m(2m-1)
\end{pmatrix},
\label{eq:c-minus-expanded}\\
C_{+}
&=s\begin{pmatrix}
(m-1)(2m+1)&2(2m+1)\\
m^2&m
\end{pmatrix}.
\label{eq:c-plus-expanded}\end{aligned}$$ These matrices transport degrees only on their stated open chambers. Their entries being nonnegative does not choose a chamber; the support-row differences choose it first. Conversely, the common factor $s$ affects the size of the degree vector but not the projective branch ratio.

It is useful to retain every cancellation in the ratio calculation. In the negative chamber, factoring out $u_2$ from [\[eq:minus-selected-v\]](#eq:minus-selected-v){reference-type="eqref" reference="eq:minus-selected-v"} gives $$\begin{aligned}
r'
&=\frac{(2m+1)(2mu_2)}
        {m(u_1+(2m-1)u_2)}
=\frac{2(2m+1)}{r+2m-1}.\end{aligned}$$ In the positive chamber the same operation gives $$\begin{aligned}
r'
&=\frac{(2m+1)((m-1)u_1+2u_2)}
        {m(mu_1+u_2)}
=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}.\end{aligned}$$ The factor $s$ cancels because it multiplies both output coordinates, whereas the unequal entries of $B_m$ remain and are responsible for the wall exchange.

Both maps are decreasing on the positive ray. Their derivatives are the constant-sign expressions $$h_m'(r)=-\frac{2(2m+1)}{(r+2m-1)^2},
\qquad
\ell_m'(r)=-\frac{(2m+1)(m+1)}{m(mr+1)^2}.
\label{eq:branch-derivatives}$$ Moreover, $$h_m(2)=\ell_m(2)=2,
\qquad
\lim_{r\to\infty}\ell_m(r)
=\frac{(2m+1)(m-1)}{m^2}>1,$$ where the last inequality is equivalent to $m^2-m-1>0$. Thus monotonicity already shows the global direction of both chamber images. The exact differences below are retained because they also provide the strict algebraic margins used later, without relying on a limit or a graph of the branches.

The next proposition supplies strict exchange, including the lower bound on the positive branch that will later be needed for coordinate visibility.

[\[prop:strict-exchange\]]{#prop:strict-exchange label="prop:strict-exchange"} For $m\geq2$, the branches in [\[eq:h-branch\]](#eq:h-branch){reference-type="eqref" reference="eq:h-branch"} and [\[eq:ell-branch\]](#eq:ell-branch){reference-type="eqref" reference="eq:ell-branch"} satisfy $$0<r<2\Longrightarrow h_m(r)>2,
\qquad
r>2\Longrightarrow 1<\ell_m(r)<2.$$ Moreover, either branch takes the value $2$ at the common boundary $r=2$, and nowhere else in its positive domain.

All denominators below are positive. Direct subtraction, without an estimate, gives $$h_m(r)-2=\frac{2(2-r)}{r+2m-1}.
\label{eq:h-minus-two}$$ This proves the first implication and identifies its equality case. For the positive branch, the two required differences are $$\begin{aligned}
\ell_m(r)-1
&=\frac{(m^2-m-1)r+3m+2}{m(mr+1)},
\label{eq:ell-minus-one}\\
2-\ell_m(r)
&=\frac{(m+1)(r-2)}{m(mr+1)}.
\label{eq:two-minus-ell}\end{aligned}$$ The numerator in [\[eq:ell-minus-one\]](#eq:ell-minus-one){reference-type="eqref" reference="eq:ell-minus-one"} is positive because $m^2-m-1\geq1$ for $m\geq2$ and $r>0$. Equation [\[eq:two-minus-ell\]](#eq:two-minus-ell){reference-type="eqref" reference="eq:two-minus-ell"} is positive precisely when $r>2$, and it vanishes precisely when $r=2$. These identities prove every assertion.

[\[cor:seed-itinerary\]]{#cor:seed-itinerary label="cor:seed-itinerary"} Let $\boldsymbol{u}_0=(1,1)^{\mathsf{T}}$. The recursively selected vectors $$\boldsymbol{u}_{n+1}=\begin{cases}
C_{-}\boldsymbol{u}_n,&u_{n,1}<2u_{n,2},\\
C_{+}\boldsymbol{u}_n,&u_{n,1}>2u_{n,2}
\end{cases}$$ are well defined for every $n\geq0$, never meet the wall, and use the primitive itinerary $$A_{-},A_{+},A_{-},A_{+},\ldots.$$ Equivalently, $r_{2j}<2<r_{2j+1}$ for every $j\geq0$.

The seed ratio is $r_0=1<2$, so $A_{-}$ is selected strictly. Positive entries and positive input show that every resulting degree vector has positive coordinates. Proposition [\[prop:strict-exchange\]](#prop:strict-exchange){reference-type="ref" reference="prop:strict-exchange"} sends every positive ratio below $2$ strictly above $2$, and sends every ratio above $2$ strictly into $(1,2)$. Induction alternates the two open chambers. At no stage is a tie-breaking convention used.

The first crossing can be seen without induction: $$r_1=h_m(1)=\frac{2(2m+1)}{2m}=2+\frac1m>2.$$ The next ratio is $r_2=\ell_m(r_1)$, which lies strictly in $(1,2)$ by Proposition [\[prop:strict-exchange\]](#prop:strict-exchange){reference-type="ref" reference="prop:strict-exchange"}. Thereafter the same two implications repeat. This explicit first pair matters because the itinerary is anchored to ordinary degree, not chosen by starting in an arbitrary chamber.

Keeping the scale, rather than only the ratios, gives the first two vectors $$\begin{aligned}
\boldsymbol{u}_1
&=\binom{2m(2m+1)s}{2m^2s},\\
\boldsymbol{u}_2
&=\binom{2m(m+1)(2m-1)(2m+1)s^2}
{4m^3(m+1)s^2}.\end{aligned}$$ Their signed wall values are $$(1,-2)\boldsymbol{u}_1=2ms>0,
\qquad
(1,-2)\boldsymbol{u}_2=-2m(m+1)s^2=-s^2L<0.$$ These identities are the first instances of the exact wall-gap law proved in Section [6](#sec:recurrence){reference-type="ref" reference="sec:recurrence"}. Here they serve only as a scale-sensitive check that the temporal order $C_{-}$ followed by $C_{+}$ agrees with the projective branch order. The induction still comes from the chamber implications, not from inspecting this finite prefix.

This argument is projective: it identifies a candidate itinerary of support rows. It does not yet establish that a selected derivative beats the old momentum coordinate, that the pure power beats the old position coordinate, or that the leading polynomial is nonzero. Those are temporal and algebraic questions, addressed next. Keeping the stages separate prevents a strict chamber inequality from being mistaken for a proof about the full four-coordinate polynomial map.

# Temporal carry and arbitrary-nonzero top homogeneous survival {#sec:carry}

We now attach the projective selector calculation to actual iterates of [\[eq:complete-coordinate-map\]](#eq:complete-coordinate-map){reference-type="eqref" reference="eq:complete-coordinate-map"}. At the end of the $n$-th complete iterate, let $\boldsymbol{u}_n$ be the degree vector of the two position coordinates. Let $\boldsymbol{v}_n$ be the degree vector of the two momentum coordinates after the first shear in that same complete iterate. Thus the second shear leaves $\boldsymbol{v}_n$ unchanged. Once both carry phases are justified, the relation is $$\boldsymbol{u}_n=sB_m\boldsymbol{v}_n\qquad(n\geq1).
\label{eq:u-v-relation}$$ Consequently, at the beginning of the next first phase, the degrees of the carried momentum coordinates are exactly $$\left(\frac{u_{n,1}}{s(2m+1)},\frac{u_{n,2}}{sm}\right).
\label{eq:carried-momentum-degrees}$$ The fractions in this identity are degrees already known to be integers; the display is a convenient comparison, not a divisibility assumption.

Table [\[tab:carry-ledger\]](#tab:carry-ledger){reference-type="ref" reference="tab:carry-ledger"} collects the comparisons used in this section and the two visibility comparisons proved in Section [5](#sec:visibility){reference-type="ref" reference="sec:visibility"}. Every inequality is valid at $s=1$; none is an asymptotic-in-$s$ shortcut.

@\>p0.23Y@ Stage & Exact vector or strict comparison\
Seed carry & $A_{-}(1,1)^{\mathsf{T}}=(2m,2m)^{\mathsf{T}}>(1,1)^{\mathsf{T}}$, and $sB_mA_{-}(1,1)^{\mathsf{T}}=(2m(2m+1)s,2m^2s)^{\mathsf{T}}>(1,1)^{\mathsf{T}}$ coordinatewise\
Carried momentum degrees & $\displaystyle \deg\boldsymbol{p}^{(n)}=
\left(u_{n,1}/(s(2m+1)),u_{n,2}/(sm)\right)^{\mathsf{T}}$, for $n\geq1$\
Negative chamber, first carry & If $u_{n,1}<2u_{n,2}$, then $2mu_{n,2}>u_{n,1}/(s(2m+1))$ and $u_{n,1}+(2m-1)u_{n,2}>u_{n,2}/(sm)$\
Negative chamber, second carry & $s(2m+1)2mu_{n,2}>u_{n,1}$ and $sm(u_{n,1}+(2m-1)u_{n,2})>u_{n,2}$\
Positive chamber, first carry & If $u_{n,1}>2u_{n,2}$, then $(m-1)u_{n,1}+2u_{n,2}>u_{n,1}/(s(2m+1))$ and $mu_{n,1}+u_{n,2}>u_{n,2}/(sm)$\
Positive chamber, second carry & $s(2m+1)((m-1)u_{n,1}+2u_{n,2})>u_{n,1}$ and $sm(mu_{n,1}+u_{n,2})>u_{n,2}$\
Negative visibility equality & $\displaystyle u_{n+1,1}=sm\,h_m(r_n)v_{n+1,2}>v_{n+1,2}$, while $u_{n+1,1}=s(2m+1)v_{n+1,1}>v_{n+1,1}$\
Positive visibility difference & $\displaystyle u_{n+1,1}-v_{n+1,2}=
s(2m+1)((m-1)u_{n,1}+2u_{n,2})-(mu_{n,1}+u_{n,2})>0$, and $u_{n+1,1}=s(2m+1)v_{n+1,1}>v_{n+1,1}$\

[\[prop:carry\]]{#prop:carry label="prop:carry"} For every step of the itinerary in Corollary [\[cor:seed-itinerary\]](#cor:seed-itinerary){reference-type="ref" reference="cor:seed-itinerary"}, the newly selected coordinate of $\nabla V_m$ strictly exceeds the corresponding carried momentum degree. The newly selected pure-power coordinate of $\nabla W_{m,s}$ then strictly exceeds the corresponding carried position degree. Hence [\[eq:u-v-relation\]](#eq:u-v-relation){reference-type="eqref" reference="eq:u-v-relation"} holds and $$\boldsymbol{v}_{n+1}=A_{-}\boldsymbol{u}_n\quad\hbox{or}\quad
\boldsymbol{v}_{n+1}=A_{+}\boldsymbol{u}_n$$ according to the strict chamber of $\boldsymbol{u}_n$.

For the seed, the old momentum and position degrees are all one. Since $m\geq2$, $$A_{-}(1,1)^{\mathsf{T}}=(2m,2m)^{\mathsf{T}}>(1,1)^{\mathsf{T}},$$ and $$sB_mA_{-}(1,1)^{\mathsf{T}}
=(2m(2m+1)s,2m^2s)^{\mathsf{T}}>(1,1)^{\mathsf{T}}.$$ This establishes both phases on the first complete iterate and gives [\[eq:u-v-relation\]](#eq:u-v-relation){reference-type="eqref" reference="eq:u-v-relation"} for $n=1$.

Assume now that a complete iterate has been justified, so the carried momentum degrees are [\[eq:carried-momentum-degrees\]](#eq:carried-momentum-degrees){reference-type="eqref" reference="eq:carried-momentum-degrees"}. If $u_{n,1}<2u_{n,2}$, the new vector is the one in [\[eq:minus-selected-v\]](#eq:minus-selected-v){reference-type="eqref" reference="eq:minus-selected-v"}. The first comparison follows from $$\frac{u_{n,1}}{s(2m+1)}
<\frac{2u_{n,2}}{s(2m+1)}\leq\frac{2u_{n,2}}{2m+1}<2mu_{n,2}.$$ For the second comparison, $u_{n,1}+(2m-1)u_{n,2}>u_{n,2}\geq u_{n,2}/(sm)$. After the pure powers act, the new position degrees satisfy $$s(2m+1)2mu_{n,2}>2u_{n,2}>u_{n,1},$$ and $$sm\bigl(u_{n,1}+(2m-1)u_{n,2}\bigr)>u_{n,2}.$$ These are the two negative-chamber carry phases.

If $u_{n,1}>2u_{n,2}$, use [\[eq:plus-selected-v\]](#eq:plus-selected-v){reference-type="eqref" reference="eq:plus-selected-v"}. Since $m-1\geq1$, $$(m-1)u_{n,1}+2u_{n,2}>u_{n,1}
>\frac{u_{n,1}}{s(2m+1)}.$$ Likewise $mu_{n,1}+u_{n,2}>u_{n,2}>u_{n,2}/(sm)$. For the second phase, $$s(2m+1)((m-1)u_{n,1}+2u_{n,2})>u_{n,1}$$ and $$sm(mu_{n,1}+u_{n,2})>u_{n,2}.$$ This proves both positive-chamber comparisons. Induction completes the argument, including the limiting case $s=1$.

The weakest carry case is already $s=1$; the margins can be displayed without suppressing that endpoint. In the negative chamber, the two first-phase differences satisfy $$\begin{aligned}
2mu_{n,2}-\frac{u_{n,1}}{s(2m+1)}
&>\left(2m-\frac{2}{s(2m+1)}\right)u_{n,2}>0,\\
u_{n,1}+(2m-1)u_{n,2}-\frac{u_{n,2}}{sm}
&=u_{n,1}+\left(2m-1-\frac1{sm}\right)u_{n,2}>0.\end{aligned}$$ The corresponding second-phase differences are $$\begin{aligned}
2ms(2m+1)u_{n,2}-u_{n,1}
&>\bigl(2ms(2m+1)-2\bigr)u_{n,2}>0,\\
sm\bigl(u_{n,1}+(2m-1)u_{n,2}\bigr)-u_{n,2}
&=smu_{n,1}+\bigl(sm(2m-1)-1\bigr)u_{n,2}>0.\end{aligned}$$ Every coefficient on the final right-hand sides is nonnegative, and each line has a strictly positive term for $m\geq2$ and $s\geq1$.

In the positive chamber, the analogous margins are even more direct: $$\begin{aligned}
&\left(m-1-\frac1{s(2m+1)}\right)u_{n,1}+2u_{n,2}>0,\\
&mu_{n,1}+\left(1-\frac1{sm}\right)u_{n,2}>0,\\
&\bigl(s(2m+1)(m-1)-1\bigr)u_{n,1}
  +2s(2m+1)u_{n,2}>0,\\
&sm^2u_{n,1}+(sm-1)u_{n,2}>0.\end{aligned}$$ The first two lines compare the selected derivative with the carried momentum; the last two compare its pure-power image with the carried position. Writing all eight margins separately makes clear that increasing $s$ only strengthens carry. No eventual-in-$s$ or asymptotic argument is being used to pass from a support selector to a polynomial degree.

Strict degree comparison eliminates cancellation between an old coordinate and a newly selected derivative, but one more point is needed: the selected top homogeneous expression itself must be nonzero after substitution into an iterate. That point cannot be replaced by positivity because the field need not be ordered and the coefficients are arbitrary nonzero elements.

[\[lem:top-survival\]]{#lem:top-survival label="lem:top-survival"} At every half-step, each coordinate selected in Proposition [\[prop:carry\]](#prop:carry){reference-type="ref" reference="prop:carry"} has a nonzero top homogeneous part of the asserted degree. This holds for every $A,B,C,D\in\mathbb{K}^\times$.

Proceed by induction from the coordinate variables, whose top homogeneous parts are nonzero. In a strict negative chamber, the unique top source in each coordinate of $\nabla V_m$ is its displayed $B$-monomial; in a strict positive chamber, it is its displayed $A$-monomial. After substitution, its top homogeneous part is a nonzero derivative scalar times $A$ or $B$, multiplied by powers of the already nonzero top homogeneous parts of the two position coordinates. The ring $\mathbb{K}[q_1,q_2,p_1,p_2]$ is a domain, so this product is nonzero. The strict first-phase carry inequality means no carried momentum term has the same degree, hence none can cancel it.

In the second phase, each coordinate of $\nabla W_{m,s}$ has only one pure-power source. Its top homogeneous part is a nonzero scalar times $C$ or $D$ and a positive power of the corresponding nonzero momentum top form. It is again nonzero in the same domain. The strict second-phase carry inequality excludes cancellation with the old position coordinate. Characteristic zero makes all derivative scalars in [\[eq:grad-v\]](#eq:grad-v){reference-type="eqref" reference="eq:grad-v"}--[\[eq:grad-w\]](#eq:grad-w){reference-type="eqref" reference="eq:grad-w"} nonzero. Thus the induction propagates through both phases and all iterates.

To make the induction concrete, denote by $Q_{n,i}$ and $P_{n,i}$ the top homogeneous parts of the two position and momentum coordinates at the end of the $n$-th complete iterate. In a negative chamber, the top forms created by the first phase have the shapes $$P_{n+1,1}=B(Q_{n,2})^{2m},
\qquad
P_{n+1,2}=2mB\,Q_{n,1}(Q_{n,2})^{2m-1},
\label{eq:negative-top-forms}$$ with their displayed nonzero derivative scalars. In a positive chamber they have the shapes $$P_{n+1,1}=mA(Q_{n,1})^{m-1}(Q_{n,2})^2,
\qquad
P_{n+1,2}=2A(Q_{n,1})^mQ_{n,2}.
\label{eq:positive-top-forms}$$ The second phase then has $$\begin{aligned}
Q_{n+1,1}
&=\bigl(s(2m+1)+1\bigr)C
  (P_{n+1,1})^{s(2m+1)},
\label{eq:first-q-top-form}\\
Q_{n+1,2}
&=(sm+1)D(P_{n+1,2})^{sm}.
\label{eq:second-q-top-form}\end{aligned}$$ Substitution makes the complete-step top-form recursion equally explicit. For a negative-chamber step, define $$c_1^-=(s(2m+1)+1)C B^{s(2m+1)},
\qquad
c_2^-=(sm+1)D(2mB)^{sm}.$$ Then [\[eq:negative-top-forms\]](#eq:negative-top-forms){reference-type="eqref" reference="eq:negative-top-forms"}--[\[eq:second-q-top-form\]](#eq:second-q-top-form){reference-type="eqref" reference="eq:second-q-top-form"} give $$\begin{aligned}
Q_{n+1,1}
&=c_1^-(Q_{n,2})^{2ms(2m+1)},\\
Q_{n+1,2}
&=c_2^-(Q_{n,1})^{sm}(Q_{n,2})^{sm(2m-1)}.\end{aligned}$$ For a positive-chamber step, put $$c_1^+=(s(2m+1)+1)C(mA)^{s(2m+1)},
\qquad
c_2^+=(sm+1)D(2A)^{sm}.$$ The corresponding recursion is $$\begin{aligned}
Q_{n+1,1}
&=c_1^+(Q_{n,1})^{s(2m+1)(m-1)}
             (Q_{n,2})^{2s(2m+1)},\\
Q_{n+1,2}
&=c_2^+(Q_{n,1})^{sm^2}(Q_{n,2})^{sm}.\end{aligned}$$ All four constants lie in $\mathbb{K}^\times$. The exponent rows in these recursions are precisely the rows transported by $sB_mA_{-}$ or $sB_mA_{+}$; the formulas therefore connect the matrix state to actual top homogeneous polynomials rather than only to formal weighted degrees. Even if the two top forms share factors, the domain property keeps every displayed product nonzero. Strict selection also leaves no second source at the same degree, so common factors cannot create an additive cancellation.

These displays describe top homogeneous parts, not the full coordinate polynomials. They expose every factor responsible for the asserted degree: a nonzero field scalar and powers of top forms already known to be nonzero. Equations [\[eq:negative-top-forms\]](#eq:negative-top-forms){reference-type="eqref" reference="eq:negative-top-forms"} and [\[eq:positive-top-forms\]](#eq:positive-top-forms){reference-type="eqref" reference="eq:positive-top-forms"} alternate strictly by Corollary [\[cor:seed-itinerary\]](#cor:seed-itinerary){reference-type="ref" reference="cor:seed-itinerary"}; equations [\[eq:first-q-top-form\]](#eq:first-q-top-form){reference-type="eqref" reference="eq:first-q-top-form"} and [\[eq:second-q-top-form\]](#eq:second-q-top-form){reference-type="eqref" reference="eq:second-q-top-form"} follow each of them. Thus the polynomial-domain argument is an explicit recursive certificate, not an appeal to generic leading terms.

Two nonzero homogeneous polynomials can have overlapping monomials after substitution, but that causes no issue here. Within a strictly selected derivative coordinate there is only one source at the top degree, so there is no second same-degree source with which to cancel. The carried coordinate has strictly lower degree. Products and positive powers of a nonzero polynomial remain nonzero in a domain. These observations cover, respectively, selection, addition, and substitution.

Combining Proposition [\[prop:carry\]](#prop:carry){reference-type="ref" reference="prop:carry"} with Lemma [\[lem:top-survival\]](#lem:top-survival){reference-type="ref" reference="lem:top-survival"} shows that the selector vectors are exact ordinary total-degree vectors of the polynomial iterates. This proves the carry and arbitrary-nonzero coefficient assertions in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(ii). Uniqueness of a selected support gives a single candidate top source. The domain proves that source nonzero, and strict carry keeps it separate from the older coordinate. None of these steps is a generic-coefficient argument.

# $q_1$ visibility, monodromy, determinant, and spectrum {#sec:visibility}

The two entries of $\boldsymbol{u}_n$ describe only the position coordinates. To identify $u_{n,1}$ with the degree of the full four-coordinate map, it must also be compared with the two momentum entries $\boldsymbol{v}_n$. This is not a formal consequence of the chamber itinerary. The negative chamber, in particular, requires an exact equality before the final strict comparison.

[\[prop:q1-visibility\]]{#prop:q1-visibility label="prop:q1-visibility"} For every $n\geq1$, $$u_{n,1}>u_{n,2},\qquad
u_{n,1}>v_{n,1},\qquad
u_{n,1}>v_{n,2}.$$ Consequently $\deg(F_{m,s}^n)=u_{n,1}$ for $n\geq1$. At $n=0$, all four coordinate degrees equal one, so $d_0=1$ is a tied seed rather than a strict visibility statement.

By Corollary [\[cor:seed-itinerary\]](#cor:seed-itinerary){reference-type="ref" reference="cor:seed-itinerary"} and Proposition [\[prop:strict-exchange\]](#prop:strict-exchange){reference-type="ref" reference="prop:strict-exchange"}, every positive-step ratio is either greater than $2$ or lies strictly between $1$ and $2$. Thus $u_{n,1}>u_{n,2}$ for $n\geq1$.

Suppose first that $\boldsymbol{u}_{n+1}$ is produced from a negative-chamber vector $\boldsymbol{u}_n$. The relation $\boldsymbol{u}_{n+1}=sB_m\boldsymbol{v}_{n+1}$ and the definition of the branch ratio give the exact identity $$u_{n+1,1}=sm\,h_m(r_n)v_{n+1,2}.
\label{eq:negative-visibility-equality}$$ Since $h_m(r_n)>2$ and $sm\geq2$, this is strictly larger than $v_{n+1,2}$. The other momentum comparison is immediate but distinct: $$u_{n+1,1}=s(2m+1)v_{n+1,1}>v_{n+1,1}.$$ Notice that [\[eq:negative-visibility-equality\]](#eq:negative-visibility-equality){reference-type="eqref" reference="eq:negative-visibility-equality"} is an equality followed by an inequality. Replacing it by a purported strict inequality before the equality would lose the actual coordinate relation.

Suppose instead that $\boldsymbol{u}_n$ lies in the positive chamber. Again $u_{n+1,1}=s(2m+1)v_{n+1,1}>v_{n+1,1}$. For the second momentum coordinate, substituting [\[eq:plus-selected-v\]](#eq:plus-selected-v){reference-type="eqref" reference="eq:plus-selected-v"} gives $$\begin{aligned}
u_{n+1,1}-v_{n+1,2}
={}&s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)
  -\bigl(mu_{n,1}+u_{n,2}\bigr).
\label{eq:positive-visibility-difference}\end{aligned}$$ It is enough to take $s=1$, when the right-hand side becomes $$(2m^2-2m-1)u_{n,1}+(4m+1)u_{n,2}>0.$$ Both coefficients are positive for $m\geq2$. Increasing $s$ only increases the positive first term in [\[eq:positive-visibility-difference\]](#eq:positive-visibility-difference){reference-type="eqref" reference="eq:positive-visibility-difference"}. Thus the comparison is strict in both chambers. Lemma [\[lem:top-survival\]](#lem:top-survival){reference-type="ref" reference="lem:top-survival"} guarantees that these are true coordinate degrees, so the maximum of all four is $u_{n,1}$.

The last comparison can be unpacked into coefficientwise margins. In the positive chamber, $$\begin{aligned}
u_{n+1,1}-v_{n+1,2}
={}&\bigl(s(2m+1)(m-1)-m\bigr)u_{n,1}\\
&+\bigl(2s(2m+1)-1\bigr)u_{n,2}.\end{aligned}$$ At $s=1$, these two coefficients are $$2m^2-2m-1\geq3,
\qquad
4m+1\geq9,$$ and they increase with $s$. In the negative chamber, [\[eq:negative-visibility-equality\]](#eq:negative-visibility-equality){reference-type="eqref" reference="eq:negative-visibility-equality"} gives the quantitative ratio $$\frac{u_{n+1,1}}{v_{n+1,2}}
=smh_m(r_n)>2sm\geq4.$$ Finally, $u_{n+1,1}/v_{n+1,1}=s(2m+1)\geq5$ in either chamber. Thus visibility is not merely the comparison $u_{n+1,1}>u_{n+1,2}$ already encoded by the projective ratio. It is a separate, uniformly strict comparison with both momentum coordinates of the four-variable iterate. This is the precise step that licenses reading the first entry of the later matrix recursion as $\deg(F_{m,s}^n)$.

We can now form a matrix cocycle without confusing a formal support maximum with the degree of the full map. The two unscaled complete-step matrices are $$\begin{aligned}
B_mA_{-}
&=\begin{pmatrix}
0&2m(2m+1)\\
m&m(2m-1)
\end{pmatrix},
\label{eq:bm-am}\\
B_mA_{+}
&=\begin{pmatrix}
(2m+1)(m-1)&2(2m+1)\\
m^2&m
\end{pmatrix}.
\label{eq:bm-ap}\end{aligned}$$ The entries of the two-step product can be audited row by row. If $X=B_mA_{-}$ and $Y=B_mA_{+}$, then $$\begin{aligned}
(YX)_{11}&=2(2m+1)m=2m(2m+1),\\
(YX)_{21}&=m\cdot m=m^2,\\
(YX)_{12}
&=2m(2m+1)^2(m-1)+2m(2m+1)(2m-1)\\
&=2m(2m+1)(2m^2+m-2),\\
(YX)_{22}
&=2m^3(2m+1)+m^2(2m-1)\\
&=m^2(4m^2+4m-1).\end{aligned}$$ This expansion fixes two common sources of an erroneous monodromy: reversing $X$ and $Y$, or applying the diagonal pure-power multiplier before the wrong selector. Both mistakes would preserve nonnegative entries while changing the spectrum. The phase order in [\[eq:intermediate-state\]](#eq:intermediate-state){reference-type="eqref" reference="eq:intermediate-state"} instead forces the product displayed below.

The itinerary begins with the negative chamber, then uses the positive chamber. Accordingly, the two-step monodromy in column-vector order is $$P_m=(B_mA_{+})(B_mA_{-})
=\begin{pmatrix}
2m(2m+1)&2m(2m+1)(2m^2+m-2)\\
m^2&m^2(4m^2+4m-1)
\end{pmatrix}.
\label{eq:monodromy}$$ Restoring the two factors of $s$, Corollary [\[cor:seed-itinerary\]](#cor:seed-itinerary){reference-type="ref" reference="cor:seed-itinerary"} and Proposition [\[prop:carry\]](#prop:carry){reference-type="ref" reference="prop:carry"} give $$\boldsymbol{u}_{2j}=(s^2P_m)^j\boldsymbol{u}_0,\qquad
\boldsymbol{u}_{2j+1}=sB_mA_{-}(s^2P_m)^j\boldsymbol{u}_0.
\label{eq:vector-laws}$$

[\[prop:spectrum\]]{#prop:spectrum label="prop:spectrum"} For $$H=m^2(2m+1)^2,\qquad L=2m(m+1),$$ the matrix $P_m$ has the two right eigenpairs $$P_m\binom{2}{1}=H\binom{2}{1},
\qquad
P_m\binom{-(2m+1)(2m^2+m-2)}{m}
=L\binom{-(2m+1)(2m^2+m-2)}{m}.
\label{eq:eigenpairs}$$ Its characteristic polynomial is $$\chi_{P_m}(t)=t^2-(H+L)t+HL,$$ and $H>L>0$.

Multiplication of [\[eq:monodromy\]](#eq:monodromy){reference-type="eqref" reference="eq:monodromy"} by the two displayed columns gives [\[eq:eigenpairs\]](#eq:eigenpairs){reference-type="eqref" reference="eq:eigenpairs"}. For the first column, for example, the two resulting entries are $$2m(2m+1)\bigl(2+2m^2+m-2\bigr)=2H$$ and $$2m^2+m^2(4m^2+4m-1)=H.$$ The second equality follows by the same direct collection of the terms containing $(2m+1)(2m^2+m-2)$; it yields $-L$ times that factor in the first entry and $Lm$ in the second.

For clarity, write $\alpha=(2m+1)(2m^2+m-2)$. The first coordinate of $P_m(-\alpha,m)^{\mathsf{T}}$ is $$\begin{aligned}
&-2m(2m+1)\alpha
+2m^2(2m+1)(2m^2+m-2)\\
&\qquad=-2m(m+1)\alpha=-L\alpha.\end{aligned}$$ The second coordinate is $$\begin{aligned}
&-m^2\alpha+m^3(4m^2+4m-1)\\
&\qquad=2m^2(m+1)=Lm.\end{aligned}$$ This verifies the second right eigenvector entry by entry.

The trace is $$\mathop{\mathrm{tr}}(P_m)=4m^4+4m^3+3m^2+2m=H+L.
\label{eq:trace}$$ For completeness, the determinant is not inferred merely from the proposed eigenvalues. Its $ad-bc$ expansion is $$\begin{aligned}
\det(P_m)
={}&2m(2m+1)\,m^2(4m^2+4m-1)\notag\\
&\quad-2m(2m+1)(2m^2+m-2)\,m^2\notag\\
={}&2m^3(2m+1)\bigl((4m^2+4m-1)-(2m^2+m-2)\bigr)\notag\\
={}&2m^3(m+1)(2m+1)^2=HL.
\label{eq:determinant-expansion}\end{aligned}$$ The trace and determinant give the characteristic polynomial. Finally, $$H-L=m(4m^3+4m^2-m-2)>0$$ for $m\geq2$, while both values are positive.

[\[cor:dynamical-degree\]]{#cor:dynamical-degree label="cor:dynamical-degree"} The limit defining $\lambda_1(F_{m,s})$ exists and equals $$\lambda_1(F_{m,s})=sm(2m+1).$$

The eigenvectors in [\[eq:eigenpairs\]](#eq:eigenpairs){reference-type="eqref" reference="eq:eigenpairs"} are linearly independent because $H\neq L$. The seed has a nonzero component in the $H$-eigendirection; indeed, its exact decomposition is displayed in [\[eq:seed-decomposition\]](#eq:seed-decomposition){reference-type="eqref" reference="eq:seed-decomposition"} below, with a positive $H$-coefficient. Thus the even vectors grow with two-step factor $s^2H$. Moreover, $$sB_mA_{-}\binom{2}{1}=sm(2m+1)\binom{2}{1},$$ so the same dominant component remains visible on the odd residue class. Proposition [\[prop:q1-visibility\]](#prop:q1-visibility){reference-type="ref" reference="prop:q1-visibility"} identifies the first component with the actual degree. Taking the square root of the two-step factor gives $\sqrt{s^2H}=sm(2m+1)$. This conclusion concerns the first dynamical degree only; no equality with a separately defined entropy is used.

# Recurrence, wall gaps, parity closed forms, and integrality {#sec:recurrence}

The monodromy contains more information than its spectral radius. It fixes the scalar recurrence, the exact distance from the switching wall, and both parity subsequences. Table [\[tab:degree-law-ledger\]](#tab:degree-law-ledger){reference-type="ref" reference="tab:degree-law-ledger"} gathers the final formulas. The derivations following the table explain why the rational- looking closed forms are nevertheless integer-valued.

@\>p0.20Y@ Object & Exact law\
Monodromy $P_m$ & $\displaystyle
\begin{pmatrix}2m(2m+1)&2m(2m+1)(2m^2+m-2)\\
m^2&m^2(4m^2+4m-1)\end{pmatrix}$\
Right eigenpair $H$ & $\displaystyle P_m(2,1)^{\mathsf{T}}=H(2,1)^{\mathsf{T}}$\
Right eigenpair $L$ & $\displaystyle P_m(-(2m+1)(2m^2+m-2),m)^{\mathsf{T}}
=L(-(2m+1)(2m^2+m-2),m)^{\mathsf{T}}$\
Stride-two recurrence & $\displaystyle d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n$\
Initial scalar data & $\displaystyle d_0=1,\ d_1=2m(2m+1)s,\
d_2=2m(m+1)(2m-1)(2m+1)s^2,\
d_3=8m^4(m+1)(2m+1)s^3$\
Corrected third vector & $\displaystyle \boldsymbol{u}_3=\binom{8m^4(m+1)(2m+1)s^3}
{2m^2(m+1)(2m-1)(2m^2+2m+1)s^3}$\
Wall gaps & $\displaystyle u_{2j,1}-2u_{2j,2}=-(s^2L)^j,\quad
u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j$\
Even vector & $\displaystyle \boldsymbol{u}_{2j}=\frac{s^{2j}}{\Delta_m}
\left[2(m+1)(2m^2-1)H^j\binom21
+L^j\binom{-(2m+1)(2m^2+m-2)}m\right]$\
Even degree & $\displaystyle d_{2j}=\frac{s^{2j}}{\Delta_m}
\left[4(m+1)(2m^2-1)H^j
-(2m+1)(2m^2+m-2)L^j\right]$\
Odd degree & $\displaystyle d_{2j+1}=\frac{2m(2m+1)s^{2j+1}}{\Delta_m}
\left[2(m+1)(2m^2-1)H^j+mL^j\right]$\
Integrality source & Integer matrices $C_{-},C_{+}$ and the integer seed; equivalently, the integer recurrence with the displayed integer initial data\

## Cayley--Hamilton recurrence and initial vectors

Proposition [\[prop:spectrum\]](#prop:spectrum){reference-type="ref" reference="prop:spectrum"} gives the matrix identity $$P_m^2-(H+L)P_m+HL I_2=0.
\label{eq:cayley-hamilton}$$ Applying it to $(s^2P_m)^j\boldsymbol{u}_0$, with the powers of $s$ restored, yields $$\boldsymbol{u}_{n+4}=s^2(H+L)\boldsymbol{u}_{n+2}-s^4HL\boldsymbol{u}_n
\label{eq:vector-recurrence}$$ on the even residue class. Left multiplication by $sB_mA_{-}$ gives the same identity on the odd residue class. Taking the first coordinate and using Proposition [\[prop:q1-visibility\]](#prop:q1-visibility){reference-type="ref" reference="prop:q1-visibility"} proves $$d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n
\qquad(n\geq0).
\label{eq:scalar-recurrence}$$

The initial vectors are best computed before simplifying to scalar degrees: $$\begin{aligned}
\boldsymbol{u}_0&=\binom11,
\label{eq:u0}\\
\boldsymbol{u}_1&=C_{-}\boldsymbol{u}_0
=\binom{2m(2m+1)s}{2m^2s},
\label{eq:u1}\\
\boldsymbol{u}_2&=C_{+}\boldsymbol{u}_1
=\binom{2m(m+1)(2m-1)(2m+1)s^2}
{4m^3(m+1)s^2},
\label{eq:u2}\\
\boldsymbol{u}_3&=C_{-}\boldsymbol{u}_2
=\binom{8m^4(m+1)(2m+1)s^3}
{2m^2(m+1)(2m-1)(2m^2+2m+1)s^3}.
\label{eq:u3}\end{aligned}$$ The second coordinate in [\[eq:u3\]](#eq:u3){reference-type="eqref" reference="eq:u3"} comes from $$\begin{aligned}
sm\bigl(u_{2,1}+(2m-1)u_{2,2}\bigr)
&=sm\,2m(m+1)(2m-1)s^2
   \bigl((2m+1)+2m^2\bigr)\\
&=2m^2(m+1)(2m-1)(2m^2+2m+1)s^3.\end{aligned}$$ Taking first coordinates gives exactly the four initial values in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(iv). In particular, the recurrence is not initialized from a numerical sample or inferred from a finite prefix.

The parity structure of the recurrence can be seen before interleaving the two subsequences. Put $$e_j=d_{2j},\qquad o_j=d_{2j+1}.$$ Since the characteristic polynomial of $s^2P_m$ is $$t^2-s^2(H+L)t+s^4HL,$$ Cayley--Hamilton first gives $$\begin{aligned}
e_{j+2}&=s^2(H+L)e_{j+1}-s^4HL e_j,\\
o_{j+2}&=s^2(H+L)o_{j+1}-s^4HL o_j.\end{aligned}$$ The second line follows by left multiplication with the fixed odd prefix $sB_mA_{-}$ before taking the visible first coordinate. Thus the even subsequence starts from $(d_0,d_2)$, while the odd subsequence starts from $(d_1,d_3)$, and both are controlled by the same quadratic. Replacing $e_j,o_j$ by their definitions is exactly the stride-two relation [\[eq:scalar-recurrence\]](#eq:scalar-recurrence){reference-type="eqref" reference="eq:scalar-recurrence"}; no interaction between different parity classes is being assumed.

## A left eigenfunctional and exact wall gaps

Let $\boldsymbol{w}=(1,-2)$, so that $\boldsymbol{w}\boldsymbol{u}=u_1-2u_2$ is the signed wall functional. Direct multiplication by the one-step matrices gives $$\boldsymbol{w}C_{-}=-2ms\,\boldsymbol{w},
\qquad
\boldsymbol{w}C_{+}=-(m+1)s\,\boldsymbol{w}.
\label{eq:left-wall-laws}$$ Thus $\boldsymbol{w}P_m=L\boldsymbol{w}$. Since $\boldsymbol{w}\boldsymbol{u}_0=-1$, the even vector law in [\[eq:vector-laws\]](#eq:vector-laws){reference-type="eqref" reference="eq:vector-laws"} gives $$u_{2j,1}-2u_{2j,2}=-(s^2L)^j.
\label{eq:even-wall-gap}$$ Applying the first identity in [\[eq:left-wall-laws\]](#eq:left-wall-laws){reference-type="eqref" reference="eq:left-wall-laws"} one additional time gives $$u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.
\label{eq:odd-wall-gap}$$ The signs prove the strict itinerary independently of the branch-map induction. They also quantify a useful distinction: the projective ratios can approach the wall while the unnormalized integer vectors remain a nonzero, explicitly signed distance from it.

## Eigenvector decomposition and parity laws

Put $$\Delta_m=4m^3+4m^2-m-2.$$ The positivity of $H-L=m\Delta_m$ shows $\Delta_m>0$. This denominator has a direct eigenbasis meaning. With $$\alpha=(2m+1)(2m^2+m-2),\qquad
\boldsymbol{v}_H=\binom21,
\qquad
\boldsymbol{v}_L=\binom{-\alpha}{m},$$ the determinant of the eigenvector matrix is $$\begin{aligned}
\det\begin{pmatrix}2&-\alpha\\1&m\end{pmatrix}
&=2m+\alpha
=4m^3+4m^2-m-2
=\Delta_m.\end{aligned}$$ Writing $\boldsymbol{u}_0=a\boldsymbol{v}_H+b\boldsymbol{v}_L$ gives $$2a-\alpha b=1,
\qquad
a+mb=1.$$ Hence $$b=\frac1{\Delta_m},
\qquad
a=1-\frac{m}{\Delta_m}
=\frac{2(m+1)(2m^2-1)}{\Delta_m}.$$ Thus solving for the seed in the eigenbasis [\[eq:eigenpairs\]](#eq:eigenpairs){reference-type="eqref" reference="eq:eigenpairs"} gives the exact identity $$\boldsymbol{u}_0=
\frac{2(m+1)(2m^2-1)}{\Delta_m}\binom21
+\frac1{\Delta_m}
\binom{-(2m+1)(2m^2+m-2)}m.
\label{eq:seed-decomposition}$$ Indeed, the second coordinate reduces to $$\frac{2(m+1)(2m^2-1)+m}{\Delta_m}=1,$$ and the first coordinate reduces to one after the same expansion. Applying $(s^2P_m)^j$ proves $$\boldsymbol{u}_{2j}=\frac{s^{2j}}{\Delta_m}\left[
2(m+1)(2m^2-1)H^j\binom21
+L^j\binom{-(2m+1)(2m^2+m-2)}m\right].
\label{eq:even-vector-closed}$$ Its first coordinate is $$d_{2j}=\frac{s^{2j}}{\Delta_m}\left[
4(m+1)(2m^2-1)H^j
-(2m+1)(2m^2+m-2)L^j\right].
\label{eq:even-degree-closed}$$

For the odd degrees, apply $sB_mA_{-}$ to [\[eq:even-vector-closed\]](#eq:even-vector-closed){reference-type="eqref" reference="eq:even-vector-closed"}. The first coordinates of the two resulting eigenvector images are, respectively, $$2m(2m+1)s
\quad\hbox{and}\quad
2m^2(2m+1)s.$$ Therefore $$d_{2j+1}=\frac{2m(2m+1)s^{2j+1}}{\Delta_m}\left[
2(m+1)(2m^2-1)H^j+mL^j\right].
\label{eq:odd-degree-closed}$$ Equations [\[eq:even-vector-closed\]](#eq:even-vector-closed){reference-type="eqref" reference="eq:even-vector-closed"}--[\[eq:odd-degree-closed\]](#eq:odd-degree-closed){reference-type="eqref" reference="eq:odd-degree-closed"} are the three parity formulas asserted in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(v).

The even formula also quantifies the difference between projective approach to the wall and literal contact with it. Its second coordinate is $$u_{2j,2}=\frac{s^{2j}}{\Delta_m}\left[
2(m+1)(2m^2-1)H^j+mL^j\right].$$ Combining this expression with [\[eq:even-wall-gap\]](#eq:even-wall-gap){reference-type="eqref" reference="eq:even-wall-gap"} gives the normalized signed gap $$\frac{u_{2j,1}-2u_{2j,2}}{u_{2j,2}}
=-\frac{\Delta_mL^j}
{2(m+1)(2m^2-1)H^j+mL^j}.
\label{eq:normalized-even-wall-gap}$$ Because $0<L/H<1$, the right-hand side tends to zero. Thus the even projective ratios approach two from below. Equation [\[eq:even-wall-gap\]](#eq:even-wall-gap){reference-type="eqref" reference="eq:even-wall-gap"}, however, says that the unnormalized numerator is exactly $-(s^2L)^j$ at every finite step. The limiting projective wall is therefore never an actual selector tie. The dominant $H$-component controls scale, while the subdominant $L$-component retains the complete signed chamber information.

The denominators in these diagonalized expressions do not introduce a divisibility hypothesis. The original formula $\boldsymbol{u}_{2j}=(s^2P_m)^j\boldsymbol{u}_0$ uses an integer matrix and an integer seed, and $\boldsymbol{u}_{2j+1}=sB_mA_{-}\boldsymbol{u}_{2j}$ does the same. Hence every coordinate and every $d_n$ is an integer. Alternatively, the two parity subsequences are generated by the integer recurrence [\[eq:scalar-recurrence\]](#eq:scalar-recurrence){reference-type="eqref" reference="eq:scalar-recurrence"} from the integer initial values. Diagonalization explains the expression; the matrix recursion proves integrality.

Several endpoint substitutions check the closed forms symbolically. At $j=0$, equation [\[eq:even-vector-closed\]](#eq:even-vector-closed){reference-type="eqref" reference="eq:even-vector-closed"} reduces to the seed decomposition [\[eq:seed-decomposition\]](#eq:seed-decomposition){reference-type="eqref" reference="eq:seed-decomposition"}, so $d_0=1$. Equation [\[eq:odd-degree-closed\]](#eq:odd-degree-closed){reference-type="eqref" reference="eq:odd-degree-closed"} at $j=0$ gives $$\begin{aligned}
d_1
&=\frac{2m(2m+1)s}{\Delta_m}
  \left(2(m+1)(2m^2-1)+m\right)\\
&=2m(2m+1)s,\end{aligned}$$ because the parenthesis is $\Delta_m$. Applying the even formula at $j=1$, or directly multiplying $P_m(1,1)^{\mathsf{T}}$, gives the stated $d_2$. The odd prefix then gives $d_3$, including the second-coordinate calculation in [\[eq:u3\]](#eq:u3){reference-type="eqref" reference="eq:u3"}. These are algebraic reductions of the general formulas, not data used to guess them.

The wall laws provide another independent reduction. Applying $(1,-2)$ to the even closed vector cancels the $H^j$ component because $(1,-2)(2,1)^{\mathsf{T}}=0$. The same functional applied to the $L$-eigenvector equals $-\Delta_m$. Equation [\[eq:even-vector-closed\]](#eq:even-vector-closed){reference-type="eqref" reference="eq:even-vector-closed"} therefore becomes $-(s^2L)^j$, exactly [\[eq:even-wall-gap\]](#eq:even-wall-gap){reference-type="eqref" reference="eq:even-wall-gap"}. This explains why the subdominant eigenvalue, rather than the dominant one, measures distance from the selector wall.

The dominant terms in the parity laws also make the root limit transparent. Since $H>L>0$ and $2(m+1)(2m^2-1)>0$, the $H^j$ coefficient in the even vector is nonzero and positive. Its first coordinate therefore has asymptotic two-step factor $s^2H$. The odd formula has the same nonzero $H^j$ coefficient multiplied by the fixed positive prefix $2m(2m+1)s$. Hence neither parity class loses the dominant spectral component. Polynomial factors from a repeated eigenvalue do not arise because $H\neq L$. Taking $n$-th roots on the two residue classes gives the same value $sm(2m+1)$, agreeing with Corollary [\[cor:dynamical-degree\]](#cor:dynamical-degree){reference-type="ref" reference="cor:dynamical-degree"}.

At the same time, the normalized wall gap is governed by the ratio $L/H<1$. Thus the projective orbit approaches the wall along each parity class even though equations [\[eq:even-wall-gap\]](#eq:even-wall-gap){reference-type="eqref" reference="eq:even-wall-gap"} and [\[eq:odd-wall-gap\]](#eq:odd-wall-gap){reference-type="eqref" reference="eq:odd-wall-gap"} show that no unnormalized degree vector reaches it. This coexistence of projective approach and exact strict exclusion is the reason a limiting argument alone would be inadequate: only the signed formulas retain the integer-scale separation needed for every finite iterate.

# Bounded structural lemma and conditional period-$k$ lemma {#sec:structural}

The explicit family suggests two reusable statements, but their scope must be kept narrow. The first identifies exactly when a crossed binomial followed by diagonal pure powers exchanges the two open chambers determined by its single synchronous wall. It classifies an exponent ratio inside that ansatz, not all Newton fans or all Hamiltonian shears. The second records the standard linear-algebra consequence of an already verified strict periodic itinerary. Its hypotheses include precisely the polynomial facts that were proved separately in Sections [4](#sec:carry){reference-type="ref" reference="sec:carry"} and [5](#sec:visibility){reference-type="ref" reference="sec:visibility"}.

## Crossed-binomial wall fixing

Consider positive integer exponents satisfying $$a>c\geq1,\qquad d>b\geq1,
\label{eq:crossed-exponents}$$ and nonzero coefficients in a characteristic-zero field. Set $$V=Aq_1^a q_2^b+Bq_1^c q_2^d,\qquad
W=Cp_1^{e+1}+Dp_2^{f+1},
\label{eq:bounded-ansatz}$$ where $e,f$ are positive integers. The crossing data are $$R=\frac{d-b}{a-c},\qquad
L_{\mathrm{wall}}=aR+b=cR+d.
\label{eq:R-Lwall}$$ The assumptions make $R>0$. For either support exponent $(x,y)\in\{(a,b),(c,d)\}$, define $$g_{x,y}(r)=\frac ef\,
\frac{(x-1)r+y}{xr+y-1}\qquad(r>0).
\label{eq:gxy}$$

[\[lem:bounded-criterion\]]{#lem:bounded-criterion label="lem:bounded-criterion"} For the ansatz [\[eq:bounded-ansatz\]](#eq:bounded-ansatz){reference-type="eqref" reference="eq:bounded-ansatz"}, both coordinates of $\nabla V$ switch synchronously at $r=R$. Each branch $g_{x,y}$ is strictly decreasing on $(0,\infty)$. The two selected branches exchange the two open chambers globally, $$0<r<R\Longrightarrow g_{c,d}(r)>R,
\qquad
r>R\Longrightarrow g_{a,b}(r)<R,
\label{eq:global-exchange}$$ if and only if $$\frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
\label{eq:ratio-iff}$$ At this ratio both branches take the common boundary value $R$ at $r=R$.

The two terms of $\partial V/\partial q_1$ have support rows $(a-1,b)$ and $(c-1,d)$. Their weighted-degree difference is $$\begin{aligned}
\bigl((a-1)u_1+bu_2\bigr)
-\bigl((c-1)u_1+du_2\bigr)
&=(a-c)u_1-(d-b)u_2\\
&=(a-c)u_2(r-R).\end{aligned}$$ The rows in $\partial V/\partial q_2$ are $(a,b-1)$ and $(c,d-1)$, and their difference is the same quantity. Thus both coordinates choose the $(c,d)$-monomial when $r<R$, choose the $(a,b)$-monomial when $r>R$, and tie simultaneously at $R$.

If $(x,y)$ is the selected monomial, its two gradient degrees, after dividing by $u_2$, are $$(x-1)r+y
\quad\hbox{and}\quad
xr+y-1.$$ The pure powers in $\nabla W$ multiply these by $e$ and $f$, respectively. This proves [\[eq:gxy\]](#eq:gxy){reference-type="eqref" reference="eq:gxy"}. Differentiating its fractional linear part gives $$g_{x,y}'(r)=\frac ef\,
\frac{1-x-y}{(xr+y-1)^2}<0.
\label{eq:g-derivative}$$ Here $x,y\geq1$, so the denominator is positive for $r>0$ and $1-x-y<0$. Each branch is therefore strictly decreasing on the entire positive ray.

At the wall, either support satisfies $xR+y=L_{\mathrm{wall}}$. Hence both branches have the same value $$g_{x,y}(R)=\frac ef\,
\frac{L_{\mathrm{wall}}-R}{L_{\mathrm{wall}}-1}.
\label{eq:g-at-wall}$$ If [\[eq:ratio-iff\]](#eq:ratio-iff){reference-type="eqref" reference="eq:ratio-iff"} holds, this value is $R$. Strict decrease then sends every $r<R$ above $R$ and every $r>R$ below $R$, proving [\[eq:global-exchange\]](#eq:global-exchange){reference-type="eqref" reference="eq:global-exchange"}.

Conversely, assume the two global implications in [\[eq:global-exchange\]](#eq:global-exchange){reference-type="eqref" reference="eq:global-exchange"}. Continuity of $g_{c,d}$ and the limit from the left imply $g_{c,d}(R)\geq R$. Continuity of $g_{a,b}$ and the limit from the right imply $g_{a,b}(R)\leq R$. The two wall values are equal by [\[eq:g-at-wall\]](#eq:g-at-wall){reference-type="eqref" reference="eq:g-at-wall"}, so both must equal $R$. Solving that identity for $e/f$ gives [\[eq:ratio-iff\]](#eq:ratio-iff){reference-type="eqref" reference="eq:ratio-iff"}. This proves necessity as well as sufficiency.

The positivity of the denominator in [\[eq:ratio-iff\]](#eq:ratio-iff){reference-type="eqref" reference="eq:ratio-iff"} is intrinsic to the stated exponent range: $$L_{\mathrm{wall}}-R=(a-1)R+b>0,\qquad L_{\mathrm{wall}}-1=aR+b-1>0.$$ Thus the criterion does not hide a sign case. It is nevertheless only a projective support statement. It does not compare a selected gradient with a carried coordinate, does not prove nonzero top forms after substitution, and does not identify a visible coordinate of a full polynomial iterate. Those omissions are deliberate; adding them to the conclusion of Lemma [\[lem:bounded-criterion\]](#lem:bounded-criterion){reference-type="ref" reference="lem:bounded-criterion"} would be logically unjustified.

[\[cor:structural-specialization\]]{#cor:structural-specialization label="cor:structural-specialization"} For $$(a,b,c,d)=(m,2,1,2m),$$ one has $$R=2,\qquad L_{\mathrm{wall}}=2m+2,\qquad
\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}=\frac{2m+1}{m}.$$ Because $\gcd(m,2m+1)=1$, the positive integer pairs $(e,f)$ with this ratio are exactly $$(e,f)=s(2m+1,m),\qquad s\geq1.$$ These are precisely the pure-power derivative exponents used in $W_{m,s}$.

The identities follow by substitution: $$R=\frac{2m-2}{m-1}=2,\qquad
L_{\mathrm{wall}}=m\cdot2+2=2m+2.$$ Then $$\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}
=\frac{2(2m+1)}{2m}=\frac{2m+1}{m}.$$ Any common divisor of $m$ and $2m+1$ divides $(2m+1)-2m=1$, so the two integers are coprime. Hence every positive integer realization of the ratio has $(e,f)=s(2m+1,m)$ for a positive integer $s$.

The case $R=1$ illustrates why a wall-fixing ratio is not by itself a strict ordinary-seed theorem. Ordinary total degree begins at $r_0=1$. If $R=1$, both gradient coordinates tie at the seed, and the open-chamber implications in [\[eq:global-exchange\]](#eq:global-exchange){reference-type="eqref" reference="eq:global-exchange"} say nothing about which polynomial top form is selected there. Coefficients may combine on the wall, and no strict period-two itinerary follows. The explicit family avoids this obstruction because $R=2$ and $r_0=1<2$.

## Conditional selector-to-monodromy passage

The next lemma is intentionally stated as a technical implication. It does not produce a period-$k$ example, prove that a proposed itinerary occurs, or classify periodic selector words. Instead, it identifies the exact additional facts needed before a periodic list of support matrices can be used to calculate true polynomial degree growth.

[\[lem:conditional-period-k\]]{#lem:conditional-period-k label="lem:conditional-period-k"} Let a polynomial iteration in a domain have a positive degree state $\boldsymbol{u}_n$, and suppose a proposed selector itinerary has primitive or nonprimitive period $k\geq1$, with matrices $C_0,\ldots,C_{k-1}$. Assume all six of the following hypotheses.

1.  At every half-step and every iterate, each asserted support face is the unique strict maximizer; no tie wall is used.

2.  Every newly selected coordinate strictly dominates the corresponding coordinate carried from the preceding temporal phase.

3.  After substitution, every selected top homogeneous part is nonzero in the ambient polynomial domain, so the formal maximum is an actual polynomial degree.

4.  On the verified faces, degree transport is linear and is represented in the stated temporal order by the fixed matrices $C_0,\ldots,C_{k-1}$.

5.  For each residue class modulo $k$, a specified coordinate or linear functional sees the true total degree of the full polynomial map, including all coordinates omitted from $\boldsymbol{u}_n$.

6.  Write $M=C_{k-1}\cdots C_0$ and $\rho=\rho(M)>0$. For each residue class, expand the visible scalar from (5), after the relevant prefix, into Jordan terms. Among the terms with eigenvalue modulus $\rho$, group those at the maximal surviving polynomial order $h_j$. After normalization by $\rho^\ell\ell^{h_j}$, their combined leading coefficient is uniformly bounded away from zero in absolute value for all sufficiently large $\ell$. This spectral-circle noncancellation condition is called Perron-class visibility.

Define $D_0=I$ and $$D_j=C_{j-1}\cdots C_0\qquad(1\leq j<k).$$ Then, for $\ell\geq0$ and $0\leq j<k$, $$\boldsymbol{u}_{k\ell+j}=D_jM^\ell\boldsymbol{u}_0.
\label{eq:period-k-vector-law}$$ Each visible scalar residue subsequence satisfies the linear recurrence given by the characteristic polynomial of $M$. Moreover, the resulting polynomial map has $$\lambda_1=\rho(M)^{1/k}.
\label{eq:period-k-lambda}$$

Hypotheses (1)--(3) identify the formal state with the actual degree state: strict support selection chooses one top source, strict carry excludes the older temporal coordinate, and domain survival excludes zero after substitution. Hypothesis (4) therefore gives the genuine recursion $$\boldsymbol{u}_{n+1}=C_{n\bmod k}\boldsymbol{u}_n.$$ Multiplying one verified period in temporal order gives $\boldsymbol{u}_{k(\ell+1)}=M\boldsymbol{u}_{k\ell}$. Induction yields $\boldsymbol{u}_{k\ell}=M^\ell\boldsymbol{u}_0$, and applying the first $j$ matrices of the next period proves [\[eq:period-k-vector-law\]](#eq:period-k-vector-law){reference-type="eqref" reference="eq:period-k-vector-law"}.

Write the characteristic polynomial as $$\chi_M(t)=t^r+c_1t^{r-1}+\cdots+c_r.$$ Cayley--Hamilton gives $$M^{\ell+r}+c_1M^{\ell+r-1}+\cdots+c_rM^\ell=0.$$ Left multiplication by any fixed visible functional composed with $D_j$, and right application to $\boldsymbol{u}_0$, gives the corresponding scalar recurrence on residue class $j$. Hypothesis (5) is what turns that scalar into the degree of the full map rather than merely one entry of a reduced state.

Finally, fix a residue class $j$ and write $a_{\ell,j}$ for its visible scalar. A finite-dimensional Jordan expansion gives an upper bound $$|a_{\ell,j}|\leq C_j\ell^{r-1}\rho^\ell$$ for all sufficiently large $\ell$. At the maximal surviving order $h_j$, the spectral-circle terms are $\rho^\ell\ell^{h_j}$ times the normalized combined leading coefficient from (6); all remaining spectral-circle terms have lower polynomial order, and all terms inside the spectral circle are exponentially smaller. The uniform noncancellation in (6) therefore also gives $$|a_{\ell,j}|\geq c_j\ell^{h_j}\rho^\ell$$ for some $c_j>0$ and all sufficiently large $\ell$. The upper and lower bounds imply $\lim_{\ell\to\infty}|a_{\ell,j}|^{1/\ell}=\rho$. Hypothesis (5) identifies $a_{\ell,j}$ with the positive degree $d_{k\ell+j}$, so $$\lim_{\ell\to\infty}d_{k\ell+j}^{1/(k\ell+j)}=\rho^{1/k}.$$ Every index lies in one of the finitely many residue classes, so the full root limit exists and proves [\[eq:period-k-lambda\]](#eq:period-k-lambda){reference-type="eqref" reference="eq:period-k-lambda"}, rather than only a limsup statement. No claim is made when any of the six hypotheses is absent.

For $k=2$, the explicit proof above instantiates every hypothesis rather than assuming it. Proposition [\[prop:strict-exchange\]](#prop:strict-exchange){reference-type="ref" reference="prop:strict-exchange"} supplies (1), Proposition [\[prop:carry\]](#prop:carry){reference-type="ref" reference="prop:carry"} supplies (2), Lemma [\[lem:top-survival\]](#lem:top-survival){reference-type="ref" reference="lem:top-survival"} supplies (3), equations [\[eq:bm-am\]](#eq:bm-am){reference-type="eqref" reference="eq:bm-am"}--[\[eq:vector-laws\]](#eq:vector-laws){reference-type="eqref" reference="eq:vector-laws"} supply (4), Proposition [\[prop:q1-visibility\]](#prop:q1-visibility){reference-type="ref" reference="prop:q1-visibility"} supplies (5), and the decomposition [\[eq:seed-decomposition\]](#eq:seed-decomposition){reference-type="eqref" reference="eq:seed-decomposition"} together with the odd prefix calculation supplies (6). This checklist is the proper relation between the technical lemma and Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}; the lemma is not an independent novelty claim and does not assert realization for any $k>2$.

# Boundaries, coefficient scope, limitations, and conclusion {#sec:boundaries}

The theorem is uniform in its stated coefficients and sharply bounded in its combinatorial and arithmetic assumptions. This section records what happens at the edges of those assumptions and distinguishes consequences actually proved from tempting but unsupported extensions.

## The wall and the ordinary seed

At $u_1=2u_2$, both row differences computed in Section [3](#sec:selector){reference-type="ref" reference="sec:selector"} vanish. Each coordinate of $\nabla V_m$ then has two terms of equal weighted degree. The identities $$h_m(2)=\ell_m(2)=2$$ describe the common limiting projective value, but they do not select one of the two tied polynomial terms. On such a tie, the top homogeneous part is a sum rather than the unique product used in Lemma [\[lem:top-survival\]](#lem:top-survival){reference-type="ref" reference="lem:top-survival"}; its behavior can depend on coefficients and on the already substituted top forms. The theorem therefore contains no assertion on the wall.

The ordinary seed is safely off the wall because $\boldsymbol{u}_0=(1,1)^{\mathsf{T}}$ has ratio one. Strictness is then preserved in two independent ways: the branch calculation sends open chambers into opposite open chambers, and the exact wall laws [\[eq:even-wall-gap\]](#eq:even-wall-gap){reference-type="eqref" reference="eq:even-wall-gap"}--[\[eq:odd-wall-gap\]](#eq:odd-wall-gap){reference-type="eqref" reference="eq:odd-wall-gap"} never vanish. The latter formulas are stronger than a floating-point or asymptotic separation: for every admissible $m,s,j$, they are nonzero integers with prescribed signs. They do not, however, give a rule for a different initial weighted-degree seed placed on the wall. The result concerns ordinary total degree of the displayed polynomial map.

The structural criterion has the analogous boundary. When its wall ratio is $R=1$, the ordinary seed is exactly tied, even if the exponent ratio [\[eq:ratio-iff\]](#eq:ratio-iff){reference-type="eqref" reference="eq:ratio-iff"} makes the two continuous branches fix $R$. Thus the criterion is an if-and-only-if statement about exchange of open projective chambers, not a theorem selecting a face at their boundary.

## Why each arithmetic hypothesis is present

The condition $m\geq2$ makes the wall genuine. If $m=1$, then $$q_1^m q_2^2=q_1q_2^2=q_1q_2^{2m},$$ so the two advertised terms of $V_m$ have the same support. The common row difference has the factor $m-1=0$, and there are no two crossed supports to exchange. Treating $m=1$ as a limiting member of the theorem would therefore change the combinatorial object rather than add a harmless endpoint.

The condition $s\geq1$ ensures that both pure-power derivative exponents $s(2m+1)$ and $sm$ are positive and that every carry inequality is already valid at its smallest value. We used $s\geq1$, not a large- parameter estimate, in Proposition [\[prop:carry\]](#prop:carry){reference-type="ref" reference="prop:carry"} and in the positive visibility comparison. The symbol $s=0$ would change $W_{m,s}$ to a different low-degree expression and remove the matrices used throughout; it is not an additional case.

Characteristic zero enters at the derivative level. The coefficients $m$, $2m$, $s(2m+1)+1$, and $sm+1$ in [\[eq:grad-v\]](#eq:grad-v){reference-type="eqref" reference="eq:grad-v"}--[\[eq:grad-w\]](#eq:grad-w){reference-type="eqref" reference="eq:grad-w"} are then nonzero elements of $\mathbb{K}$. In positive characteristic, one or more may vanish, deleting a support row or a pure-power phase. The selector, carry, and top-survival arguments would then need to be rebuilt case by case. No positive-characteristic conclusion is asserted. By contrast, algebraic closedness never enters: inversion uses subtraction, symplecticity uses symmetric Hessians, and noncancellation uses only that a polynomial ring over a field is a domain.

## Arbitrary nonzero coefficients, not generic coefficients

There is no magnitude, sign, positivity, or Zariski-open qualification on $A,B,C,D$. In each strict chamber, exactly one of the two supports is of higher degree in each gradient coordinate. Its coefficient is a product of one of $A,B,C,D$, a nonzero derivative scalar, and nonzero top homogeneous forms. This proves survival for every point of $(\mathbb{K}^\times)^4$, not merely outside an exceptional cancellation set.

The exclusion of zero coefficients is substantive. Setting $A=0$ or $B=0$ deletes one side of the crossed support, so the common switching wall no longer describes a competition. Setting $C=0$ or $D=0$ deletes one diagonal pure-power coordinate, invalidating $B_m$, the carry comparison, and visibility. We do not classify these degenerate families. Similarly, adding further monomials can introduce new faces, while reversing the phase order changes which variables are carried into the pure powers. Neither operation is covered by the displayed theorem.

It is also important that coefficient uniformity is proved after strictness. On a tie wall, two equal-degree contributions could combine, and arbitrary nonzero coefficients alone would not rule out cancellation. Off the wall, the unique selected support and strict temporal separation make coefficient uniformity possible. Thus "arbitrary nonzero" is a conclusion of the support-and-domain proof, not a substitute for it.

## Formal selector laws versus polynomial degree laws

The calculation exposes three failure modes that a matrix-only analysis would miss. First, a support row can be maximal among terms of a derivative but still fail to beat the old coordinate to which that derivative is added. This is why both first-phase carry inequalities appear in Table [\[tab:carry-ledger\]](#tab:carry-ledger){reference-type="ref" reference="tab:carry-ledger"}. Second, even after the first phase succeeds, a pure power of the updated momentum must beat the old position coordinate; this is the separate second carry phase. Third, a correct reduced position vector does not automatically equal the degree of the four-coordinate map. The negative-chamber identity [\[eq:negative-visibility-equality\]](#eq:negative-visibility-equality){reference-type="eqref" reference="eq:negative-visibility-equality"} and the positive-chamber difference [\[eq:positive-visibility-difference\]](#eq:positive-visibility-difference){reference-type="eqref" reference="eq:positive-visibility-difference"} are the missing visibility checks.

These are not hypothetical technicalities appended to a spectral proof. They establish the hypotheses needed before $P_m$ can be interpreted as a true degree monodromy. The logical direction is $$\begin{aligned}
\text{strict faces}
&\Longrightarrow \text{strict temporal carry}\\
&\Longrightarrow \text{nonzero top forms}\\
&\Longrightarrow \text{visible true degrees}\\
&\Longrightarrow \text{monodromy laws}.
\end{aligned}$$ Reversing this direction would allow the spectral calculation to certify its own unproved input. The conditional Lemma [\[lem:conditional-period-k\]](#lem:conditional-period-k){reference-type="ref" reference="lem:conditional-period-k"} therefore lists all six assumptions rather than packaging them under a vague stability condition.

## Scope of the two structural statements

Lemma [\[lem:bounded-criterion\]](#lem:bounded-criterion){reference-type="ref" reference="lem:bounded-criterion"} is an exact if-and-only-if result only for the crossed-binomial/diagonal-pure-power ansatz [\[eq:bounded-ansatz\]](#eq:bounded-ansatz){reference-type="eqref" reference="eq:bounded-ansatz"}. It determines the ratio $e/f$ that makes the single synchronous wall fixed and globally exchanges the two open chambers. It does not classify potentials with three or more supports, nonsynchronous walls, coupled monomials in $W$, or higher-dimensional selector fans. In particular, it does not prove that the resulting fan is maximal or necessary among other ansatz classes.

Lemma [\[lem:conditional-period-k\]](#lem:conditional-period-k){reference-type="ref" reference="lem:conditional-period-k"} is likewise conditional and technical. It says what follows after a period-$k$ itinerary, carry, survival, linearity, total-degree visibility, and spectral visibility have all been verified. It supplies no example with $k>2$, no arbitrary selector word, no arbitrary word of Hamiltonian shears, and no finite-automaton realization. The only realized itinerary here has period two, and every part of that realization is checked directly. No novelty assertion is attached to the abstract selector-to-monodromy implication.

## Claims not made

The exact first dynamical degree in Corollary [\[cor:dynamical-degree\]](#cor:dynamical-degree){reference-type="ref" reference="cor:dynamical-degree"} concerns forward ordinary degree growth. We do not compute degrees of inverse iterates, and the subtraction formulas for the inverse do not imply that their degree sequence matches the forward one. We also do not equate $\log\lambda_1$ with any topological, measure-theoretic, or algebraic entropy. Such an equality would require a separate theorem and additional hypotheses.

Nothing in the degree calculation proves integrability, nonintegrability, generic dynamics, periodic points, arithmetic orbit behavior, or nonconjugacy. Symplecticity alone supplies none of these conclusions. The two eigenvalues of $P_m$ and the exact recurrence describe polynomial degree transport, not phase-space orbit classification.

No priority or firstness statement is intended. Periodic tropical switching, monodromy methods, spectral degree growth, polynomial symplectomorphisms, and Perron-type realization questions have broader literatures, some of which were cited in Section [1](#sec:introduction){reference-type="ref" reference="sec:introduction"} to make that separation explicit. The contribution proved here is the closed chain of formulas for this family, with its strict period-two selector exchange and true-polynomial verification. Nor is any computation used as proof: all matrices, determinants, recurrences, wall gaps, and closed forms follow from the displayed symbolic identities. In particular, there is no claim of a first Perron realization, a first tropical switching result, or a first symplectic-shear degree mechanism.

## Conclusion

The family $F_{m,s}=T\circ S$ provides a controlled setting in which the ordinary degree orbit is forced to change Newton chamber at every iterate. The common wall comes from identical row differences in both coordinates of $\nabla V_m$; the pure-power exponents are exactly those that fix and exchange that wall. Strict branch inequalities alone are not enough, so the proof verifies seed carry, both later carry phases, nonzero top homogeneous survival over an arbitrary characteristic-zero field, and visibility against all four coordinates.

Only after those steps does the two-step monodromy become a degree theorem. Its explicit determinant and eigenpairs yield the dynamical degree, while Cayley--Hamilton and the wall eigenfunctional yield the stride-two recurrence, corrected initial vectors, signed wall gaps, and exact parity laws. The matrix form also explains integrality without extracting it from the denominators of the diagonalized expressions. The bounded structural criterion and conditional period-$k$ lemma isolate which parts of this argument are reusable and, equally importantly, which parts must be proved again in any different family.
